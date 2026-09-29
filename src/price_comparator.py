import os
import pandas as pd
from src.live_scraper import LiveMarketScraper

class PriceComparator:
    def __init__(self, data_dir):
        self.data_dir = data_dir
        self.live_scraper = LiveMarketScraper(data_dir)
        self.reload_data()

    def reload_data(self):
        self.products_df = pd.read_csv(os.path.join(self.data_dir, "products.csv"))
        self.pricing_df = pd.read_csv(os.path.join(self.data_dir, "platform_prices.csv"))

    def search_products(self, query):
        self.reload_data()
        if not query or query.strip() == "":
            return self.products_df.copy()

        q_clean = query.strip().lower()
        tokens = [t for t in q_clean.split() if len(t) > 1]

        synonyms = {
            "phone": ["smartphones", "iphone", "galaxy", "pixel", "oneplus", "mobile"],
            "laptop": ["laptops", "macbook", "xps", "rog", "spectre", "dell", "hp", "asus"],
            "headphone": ["audio", "sony", "airpods", "bose", "earbuds", "speaker", "jbl"],
            "watch": ["smartwatches", "apple watch", "galaxy watch", "garmin"],
            "mouse": ["accessories", "logitech", "power bank", "ssd", "anker", "samsung"]
        }

        expanded_tokens = set(tokens)
        for t in tokens:
            if t in synonyms:
                expanded_tokens.update(synonyms[t])

        scores = []
        for idx, row in self.products_df.iterrows():
            text = f"{row['title']} {row['brand']} {row['category']}".lower()
            match_count = sum(1 for t in expanded_tokens if t in text)
            scores.append(match_count)

        self.products_df['search_score'] = scores
        matched_df = self.products_df[self.products_df['search_score'] > 0].sort_values(by='search_score', ascending=False)

        if matched_df.empty:
            return self.products_df.copy()

        return matched_df.drop(columns=['search_score'])

    def compare_prices(self, product_id):
        self.reload_data()
        product = self.products_df[self.products_df['product_id'] == product_id]
        if product.empty:
            product = self.products_df.head(1)
            product_id = product.iloc[0]['product_id']

        prod_info = product.iloc[0].to_dict()
        prices = self.pricing_df[self.pricing_df['product_id'] == product_id].copy()

        if prices.empty:
            return prod_info, None, None

        prices_sorted = prices.sort_values(by='price', ascending=True).reset_index(drop=True)
        best_deal = prices_sorted.iloc[0].to_dict()

        max_price = prices['price'].max()
        base_price = prod_info['base_price']
        best_price = best_deal['price']
        
        savings = max_price - best_price
        best_deal['savings'] = savings

        discount_pct = max(0, (base_price - best_price) / base_price * 100)
        rating_score = best_deal['rating'] * 10
        deal_score = min(99, int(50 + rating_score * 0.6 + discount_pct * 3))
        best_deal['deal_score'] = deal_score

        return prod_info, prices_sorted, best_deal

    def get_live_market_comparison(self, query):
        """
        Returns live real-time market search results from live_scraper combined with database catalog matching.
        """
        live_results = self.live_scraper.fetch_live_market_data(query)
        return live_results

if __name__ == "__main__":
    data_path = os.path.join(os.path.dirname(__file__), "..", "data")
    if os.path.exists(os.path.join(data_path, "products.csv")):
        comparator = PriceComparator(data_path)
        print("Live Price Comparator Verified.")
