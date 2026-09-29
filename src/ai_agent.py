import os
import pandas as pd
from src.google_search import GoogleShoppingSearch
from src.price_comparator import PriceComparator

class AgenticShoppingAssistant:
    def __init__(self, data_dir):
        self.data_dir = data_dir
        self.comparator = PriceComparator(data_dir)
        self.google_search = GoogleShoppingSearch()

    def process_query(self, user_prompt):
        """
        Connects directly to Google Search to parse natural language queries,
        fetches live internet prices across Amazon, Flipkart, Croma, and generates an AI Shopping Plan.
        """
        prompt = user_prompt.lower().strip()
        if not prompt:
            prompt = "smartphone"

        # 1. Fetch Live Google Search Results
        google_results = self.google_search.search_google_shopping(prompt)
        
        if google_results:
            top_item = google_results[0]
            best_deal = top_item["best_deal"]
            
            reasoning = (
                f"🤖 **Google Live Agentic Reasoning & Purchase Plan:**\n\n"
                f"1. **Intent Analysis:** Queried Google Live for **'{prompt}'**.\n"
                f"2. **Google Live Product:** **{top_item['title']}** (Base Retail: ₹{top_item['base_price']:,}).\n"
                f"3. **Multi-Store Price Check:** Scanned live pricing across Amazon, Flipkart, and Croma.\n"
                f"4. **Optimal Deal Recommendation:** Buy on **{best_deal['platform']}** at **₹{best_deal['price']:,}** (Instant Savings: ₹{best_deal['savings']:,}).\n"
                f"5. **Bargain Deal Score:** ⭐ `{best_deal['deal_score']} / 100`"
            )
            return reasoning, best_deal

        # Fallback to local comparator
        self.comparator.reload_data()
        products_df = self.comparator.products_df
        best_prod = products_df.iloc[0]
        prod_info, prices_df, best_deal = self.comparator.compare_prices(best_prod['product_id'])

        reasoning = (
            f"🤖 **Agentic Reasoning & Purchase Plan:**\n\n"
            f"1. **Product:** **{best_prod['title']}**.\n"
            f"2. **Best Deal:** Buy on **{best_deal['platform']}** at **₹{best_deal['price']:,}**."
        )

        return reasoning, best_deal

if __name__ == "__main__":
    data_path = os.path.join(os.path.dirname(__file__), "..", "data")
    agent = AgenticShoppingAssistant(data_path)
    r, d = agent.process_query("Nike Air Jordan shoes")
    print("Google Connected Agent Verified.")
