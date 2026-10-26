import os
import sys
import re
import pandas as pd

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
try:
    from src.google_search import GoogleShoppingSearch
except ImportError:
    from google_search import GoogleShoppingSearch

class PriceComparator:
    def __init__(self, data_dir):
        self.data_dir = data_dir
        self.google_searcher = GoogleShoppingSearch()
        self.reload_data()

    def reload_data(self):
        self.products_df = pd.read_csv(os.path.join(self.data_dir, "products.csv"))
        self.pricing_df = pd.read_csv(os.path.join(self.data_dir, "platform_prices.csv"))

    def search_products(self, query):
        self.reload_data()
        if not query or query.strip() == "":
            return self.products_df.copy()

        q_clean = query.strip().lower()
        
        # Check if there is a budget constraint (e.g. "under 50000", "below 70000")
        budget = None
        budget_match = re.search(r'\b(?:under|below|less than|upto|budget)\s*(\d{4,6})\b', q_clean)
        if budget_match:
            budget = int(budget_match.group(1))
            q_clean = re.sub(r'\b(?:under|below|less than|upto|budget)\s*\d{4,6}\b', '', q_clean).strip()

        tokens = [t for t in q_clean.split() if len(t) > 1]

        synonyms = {
            "phone": ["smartphones", "iphone", "galaxy", "pixel", "oneplus", "mobile"],
            "mobile": ["smartphones", "iphone", "galaxy", "pixel", "oneplus"],
            "laptop": ["laptops", "macbook", "xps", "rog", "spectre", "dell", "hp", "lenovo", "asus", "acer"],
            "macbook": ["apple", "macbook", "laptops"],
            "headphone": ["audio", "sony", "airpods", "bose", "earbuds", "speaker", "jbl", "sennheiser"],
            "earphone": ["audio", "earbuds", "airpods", "boat"],
            "earbuds": ["audio", "earbuds", "airpods", "boat", "sony"],
            "watch": ["smartwatches", "apple watch", "galaxy watch", "garmin", "fitbit"],
            "smartwatch": ["smartwatches", "apple watch", "galaxy watch", "garmin"],
            "tv": ["smart tvs & home", "television", "sony", "samsung", "lg", "bravia", "oled"],
            "camera": ["cameras & drones", "sony", "canon", "nikon", "fujifilm", "gopro", "dji"],
            "drone": ["cameras & drones", "dji", "mini 4 pro"],
            "monitor": ["monitors & displays", "lg", "samsung", "dell", "benq", "asus"],
            "tablet": ["tablets & e-readers", "ipad", "galaxy tab", "kindle"],
            "ipad": ["apple", "ipad", "tablets & e-readers"],
            "mouse": ["accessories & storage", "logitech", "mouse"],
            "keyboard": ["accessories & storage", "keychron", "logitech", "keyboard"],
            "ssd": ["accessories & storage", "sandisk", "samsung", "wd", "crucial"]
        }

        expanded_tokens = set(tokens)
        for t in tokens:
            if t in synonyms:
                expanded_tokens.update(synonyms[t])

        scores = []
        for _, row in self.products_df.iterrows():
            text = f"{row['title']} {row['brand']} {row['category']}".lower()
            match_count = sum(1 for t in expanded_tokens if t in text)
            
            # If budget constraint, prioritize items within budget
            if budget is not None:
                if row['base_price'] <= budget:
                    match_count += 3
                else:
                    match_count -= 2

            scores.append(match_count)

        self.products_df['search_score'] = scores
        matched_df = self.products_df[self.products_df['search_score'] > 0].sort_values(by='search_score', ascending=False)

        if matched_df.empty:
            return pd.DataFrame(columns=self.products_df.columns)

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
        best_deal['savings'] = int(savings)

        discount_pct = max(0, (base_price - best_price) / base_price * 100)
        rating_score = best_deal['rating'] * 10
        deal_score = min(99, int(52 + rating_score * 0.5 + discount_pct * 2.8))
        best_deal['deal_score'] = deal_score

        return prod_info, prices_sorted, best_deal

if __name__ == "__main__":
    data_path = os.path.join(os.path.dirname(__file__), "..", "data")
    if os.path.exists(os.path.join(data_path, "products.csv")):
        comparator = PriceComparator(data_path)
        res = comparator.search_products("iPhone 15")
        print(f"Price Comparator search test for 'iPhone 15': {len(res)} matches found")
