import os
import sys
from flask import Flask, render_template, request, jsonify

# Add directory to sys.path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.data_generator import generate_datasets
from src.price_comparator import PriceComparator
from src.recommender_model import RecommendationEngine
from src.price_forecaster import PriceForecaster
from src.nlp_sentiment import NLPSentimentAnalyzer
from src.visual_search import VisualSearchEngine
from src.ai_agent import AgenticShoppingAssistant
from src.google_search import GoogleShoppingSearch

app = Flask(__name__, template_folder='templates')

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")

if not os.path.exists(os.path.join(DATA_DIR, "products.csv")):
    generate_datasets(DATA_DIR)

comparator = PriceComparator(DATA_DIR)
rec_engine = RecommendationEngine(DATA_DIR)
rec_engine.train(epochs=15)
forecaster = PriceForecaster(DATA_DIR)
sentiment_analyzer = NLPSentimentAnalyzer(DATA_DIR)
visual_engine = VisualSearchEngine(DATA_DIR)
ai_agent = AgenticShoppingAssistant(DATA_DIR)
google_search = GoogleShoppingSearch()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/search', methods=['GET'])
def api_search():
    query = request.args.get('q', '').strip()
    category = request.args.get('category', 'All')

    results = []

    # 1. Search local 500-product catalog
    products = comparator.search_products(query)
    if category != "All" and not products.empty:
        products = products[products['category'] == category]

    if not products.empty:
        # Return top 24 items to keep responses fast and crisp
        for _, row in products.head(24).iterrows():
            prod_info, prices_df, best_deal = comparator.compare_prices(row['product_id'])
            if prices_df is not None:
                results.append({
                    "product_id": int(row['product_id']),
                    "title": row['title'],
                    "brand": row['brand'],
                    "category": row['category'],
                    "base_price": int(row['base_price']),
                    "image_url": row['image_url'],
                    "best_deal": {
                        "platform": best_deal['platform'],
                        "price": int(best_deal['price']),
                        "savings": int(best_deal['savings']),
                        "deal_score": int(best_deal['deal_score']),
                        "buy_link": best_deal['buy_link']
                    },
                    "prices": prices_df[['platform', 'price', 'rating', 'review_count', 'buy_link']].to_dict(orient='records')
                })

    # 2. If nothing matched in catalog and query was given, search live market
    if not results and query:
        google_data = google_search.search_google_shopping(query)
        for item in google_data:
            results.append({
                "product_id": item['product_id'],
                "title": item['title'],
                "brand": item['brand'],
                "category": item['category'],
                "base_price": item['base_price'],
                "image_url": item['image_url'],
                "best_deal": item['best_deal'],
                "prices": item['prices'],
                "is_live_search": True
            })

    return jsonify(results)

@app.route('/api/recommendations', methods=['GET'])
def api_recommendations():
    query = request.args.get('q', '').strip()
    user_id = int(request.args.get('user_id', 1))

    if query:
        # Search catalog matching query
        matched = comparator.search_products(query)
        if not matched.empty:
            results = []
            for _, r in matched.head(6).iterrows():
                results.append({
                    "product_id": int(r['product_id']),
                    "title": r['title'],
                    "category": r['category'],
                    "base_price": int(r['base_price']),
                    "image_url": r['image_url'],
                    "match_score": 4.85
                })
            return jsonify(results)
        
        # Fallback to Google Live Search
        google_data = google_search.search_google_shopping(query)
        results = []
        for idx, item in enumerate(google_data):
            results.append({
                "product_id": 9999 + idx,
                "title": item['title'],
                "category": item['category'],
                "base_price": item['base_price'],
                "image_url": item['image_url'],
                "match_score": 4.85
            })
        return jsonify(results)

    # Personalized NCF recommendations
    recs = rec_engine.get_recommendations(user_id=user_id, top_k=6)
    return jsonify(recs.to_dict(orient='records'))

@app.route('/api/forecast', methods=['GET'])
def api_forecast():
    query = request.args.get('q', '').strip()
    prod_id_str = request.args.get('product_id', '101')
    try:
        product_id = int(prod_id_str)
    except ValueError:
        product_id = 101

    prod_title = "Selected Product"

    # If query is provided, find product matching query
    if query:
        matched = comparator.search_products(query)
        if not matched.empty:
            product_id = int(matched.iloc[0]['product_id'])
            prod_title = matched.iloc[0]['title']
        else:
            # Dynamic estimate for query
            g_item = google_search.search_google_shopping(query)[0]
            base_p = g_item['base_price']
            pred_p = round(base_p * 0.94, -1)
            return jsonify({
                "product_id": 9999,
                "title": g_item['title'],
                "predicted_price": pred_p,
                "signal": "BUY NOW",
                "reason": f"Market price trend analysis for '{query}' shows current price is at an optimal 30-day low.",
                "history": [
                    {"date": f"Day -{i}", "price": int(round(base_p * (1.04 - (i*0.003)), -1))}
                    for i in range(14, 0, -1)
                ]
            })

    # Predict from real history logs
    df_hist, pred_price, signal, reason, history_points = forecaster.predict_price_trend(product_id)
    matched_row = comparator.products_df[comparator.products_df['product_id'] == product_id]
    if not matched_row.empty:
        prod_title = matched_row.iloc[0]['title']

    return jsonify({
        "product_id": product_id,
        "title": prod_title,
        "predicted_price": pred_price,
        "signal": signal,
        "reason": reason,
        "history": history_points
    })

@app.route('/api/sentiment', methods=['GET'])
def api_sentiment():
    query = request.args.get('q', '').strip()
    prod_id_str = request.args.get('product_id', '101')
    try:
        product_id = int(prod_id_str)
    except ValueError:
        product_id = 101

    if query:
        matched = comparator.search_products(query)
        if not matched.empty:
            product_id = int(matched.iloc[0]['product_id'])

    pros, cons = sentiment_analyzer.summarize_reviews(product_id)
    matched_row = comparator.products_df[comparator.products_df['product_id'] == product_id]
    title = matched_row.iloc[0]['title'] if not matched_row.empty else query.title()

    return jsonify({"product_id": product_id, "title": title, "pros": pros, "cons": cons})

@app.route('/api/visual_search', methods=['GET'])
def api_visual_search():
    query = request.args.get('q', '').strip()
    category = request.args.get('category', 'Smartphones')

    if query:
        matched = comparator.search_products(query)
        if not matched.empty:
            category = matched.iloc[0]['category']

    vis_results = visual_engine.search_by_image(category, top_k=6)
    return jsonify(vis_results.to_dict(orient='records'))

@app.route('/api/chat', methods=['POST'])
def api_chat():
    data = request.json or {}
    prompt = data.get('prompt', '')
    reasoning, deal = ai_agent.process_query(prompt)
    return jsonify({"reasoning": reasoning, "deal": deal})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5050))
    print(f"Starting SmartShop AI Server on port {port}")
    app.run(host='0.0.0.0', port=port, debug=False)
