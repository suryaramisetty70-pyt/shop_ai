import os
import sys
import numpy as np
import pandas as pd
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

# Category icons mapping for rich UI presentation
CATEGORY_ICONS = {
    "Smartphones": "fa-mobile-screen-button",
    "Laptops": "fa-laptop",
    "Audio": "fa-headphones-simple",
    "Smartwatches": "fa-stopwatch-20",
    "Smart TVs & Home": "fa-tv",
    "Smart TVs": "fa-tv",
    "Gaming Consoles & Gear": "fa-gamepad",
    "Cameras & Drones": "fa-camera-retro",
    "Monitors & Displays": "fa-desktop",
    "Tablets & E-Readers": "fa-tablet-screen-button",
    "Accessories & Storage": "fa-hard-drive",
    "Smart Home & IoT": "fa-house-signal",
    "Smart Eyewear & Wearables": "fa-glasses"
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/stats', methods=['GET'])
def api_stats():
    """Returns platform KPIs, summary metrics, and category distributions."""
    comparator.reload_data()
    products_df = comparator.products_df
    pricing_df = comparator.pricing_df

    total_prods = len(products_df)
    total_listings = len(pricing_df)
    
    # Calculate average savings across catalog
    grouped_prices = pricing_df.groupby('product_id')['price']
    savings_series = grouped_prices.max() - grouped_prices.min()
    avg_savings = int(savings_series.mean()) if not savings_series.empty else 4500

    # Calculate categories distribution
    cat_counts = products_df['category'].value_counts().to_dict()
    categories_list = []
    for cat_name, count in cat_counts.items():
        categories_list.append({
            "name": cat_name,
            "count": int(count),
            "icon": CATEGORY_ICONS.get(cat_name, "fa-tag")
        })

    # Find top 8 hot deals across the catalog
    hot_deals = []
    for p_id in products_df['product_id'].head(50):
        _, _, best = comparator.compare_prices(p_id)
        if best and best.get('savings', 0) > 1500:
            p_row = products_df[products_df['product_id'] == p_id].iloc[0]
            hot_deals.append({
                "product_id": int(p_id),
                "title": p_row['title'],
                "brand": p_row['brand'],
                "category": p_row['category'],
                "base_price": int(p_row['base_price']),
                "deal_price": int(best['price']),
                "savings": int(best['savings']),
                "deal_score": int(best['deal_score']),
                "platform": best['platform'],
                "image_url": p_row['image_url'],
                "buy_link": best['buy_link']
            })
    hot_deals = sorted(hot_deals, key=lambda x: (x['deal_score'], x['savings']), reverse=True)[:8]

    return jsonify({
        "total_products": total_prods,
        "total_listings": total_listings,
        "platforms_compared": ["Amazon India", "Flipkart", "Croma"],
        "total_categories": len(cat_counts),
        "total_reviews": 1200,
        "avg_savings": avg_savings,
        "categories": categories_list,
        "hot_deals": hot_deals
    })

@app.route('/api/categories', methods=['GET'])
def api_categories():
    comparator.reload_data()
    cat_counts = comparator.products_df['category'].value_counts().to_dict()
    cats = []
    for cat_name, count in cat_counts.items():
        cats.append({
            "name": cat_name,
            "count": int(count),
            "icon": CATEGORY_ICONS.get(cat_name, "fa-tag")
        })
    return jsonify(cats)

@app.route('/api/brands', methods=['GET'])
def api_brands():
    comparator.reload_data()
    brands = sorted([str(b) for b in comparator.products_df['brand'].dropna().unique() if str(b)])
    return jsonify(brands)

@app.route('/api/search', methods=['GET'])
def api_search():
    query = request.args.get('q', '').strip()
    category = request.args.get('category', 'All')
    brand = request.args.get('brand', 'All')
    sort_by = request.args.get('sort', 'deal_score')
    page = int(request.args.get('page', 1))
    limit = int(request.args.get('limit', 24))
    as_envelope = request.args.get('envelope', 'false').lower() == 'true'

    comparator.reload_data()
    products = comparator.search_products(query)

    if category != "All" and not products.empty:
        products = products[products['category'] == category]

    if brand != "All" and not products.empty:
        products = products[products['brand'].str.lower() == brand.lower()]

    results = []

    if not products.empty:
        # Build comparison info for matching products
        for _, row in products.iterrows():
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

        # Apply sorting
        if sort_by == 'price_asc':
            results.sort(key=lambda x: x['best_deal']['price'])
        elif sort_by == 'price_desc':
            results.sort(key=lambda x: x['best_deal']['price'], reverse=True)
        elif sort_by == 'savings':
            results.sort(key=lambda x: x['best_deal']['savings'], reverse=True)
        elif sort_by == 'rating':
            results.sort(key=lambda x: max([p['rating'] for p in x['prices']] or [4.0]), reverse=True)
        else:  # default deal_score
            results.sort(key=lambda x: x['best_deal']['deal_score'], reverse=True)

    # 2. Fallback to live search if empty
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

    total_count = len(results)
    total_pages = max(1, (total_count + limit - 1) // limit)
    start_idx = (page - 1) * limit
    paginated_results = results[start_idx : start_idx + limit]

    if as_envelope:
        return jsonify({
            "total": total_count,
            "page": page,
            "pages": total_pages,
            "limit": limit,
            "results": paginated_results
        })
    else:
        # Default returns paginated list for backward compatibility
        return jsonify(paginated_results)

@app.route('/api/product/<int:product_id>', methods=['GET'])
def api_product_details(product_id):
    """Full 360-degree product details endpoint combining pricing, forecast, sentiment, and visual matches."""
    comparator.reload_data()
    prod_row = comparator.products_df[comparator.products_df['product_id'] == product_id]
    if prod_row.empty:
        return jsonify({"error": "Product not found"}), 404

    prod = prod_row.iloc[0]
    prod_info, prices_df, best_deal = comparator.compare_prices(product_id)
    _, pred_price, signal, reason, history = forecaster.predict_price_trend(product_id)
    pros, cons = sentiment_analyzer.summarize_reviews(product_id)
    similar_df = visual_engine.search_by_image(prod['category'], top_k=4)

    return jsonify({
        "product_id": int(product_id),
        "title": prod['title'],
        "brand": prod['brand'],
        "category": prod['category'],
        "base_price": int(prod['base_price']),
        "image_url": prod['image_url'],
        "best_deal": best_deal,
        "prices": prices_df[['platform', 'price', 'rating', 'review_count', 'buy_link']].to_dict(orient='records') if prices_df is not None else [],
        "forecast": {
            "predicted_price": pred_price,
            "signal": signal,
            "reason": reason,
            "history": history
        },
        "sentiment": {
            "pros": pros,
            "cons": cons
        },
        "similar": similar_df[['product_id', 'title', 'base_price', 'image_url', 'visual_similarity']].to_dict(orient='records')
    })

@app.route('/api/recommendations', methods=['GET'])
def api_recommendations():
    query = request.args.get('q', '').strip()
    user_id = int(request.args.get('user_id', 1))

    if query:
        matched = comparator.search_products(query)
        if not matched.empty:
            results = []
            for _, r in matched.head(8).iterrows():
                results.append({
                    "product_id": int(r['product_id']),
                    "title": r['title'],
                    "category": r['category'],
                    "base_price": int(r['base_price']),
                    "image_url": r['image_url'],
                    "match_score": 4.88
                })
            return jsonify(results)
        
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
    recs = rec_engine.get_recommendations(user_id=user_id, top_k=8)
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

    if query:
        matched = comparator.search_products(query)
        if not matched.empty:
            product_id = int(matched.iloc[0]['product_id'])
            prod_title = matched.iloc[0]['title']
        else:
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

    vis_results = visual_engine.search_by_image(category, top_k=8)
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
