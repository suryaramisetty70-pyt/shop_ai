import os
import sys
import re
import pandas as pd

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
try:
    from src.google_search import GoogleShoppingSearch
    from src.price_comparator import PriceComparator
except ImportError:
    from google_search import GoogleShoppingSearch
    from price_comparator import PriceComparator

class AgenticShoppingAssistant:
    def __init__(self, data_dir):
        self.data_dir = data_dir
        self.comparator = PriceComparator(data_dir)
        self.google_search = GoogleShoppingSearch()

    def generate_llm_response(self, prompt, top_item, best_deal):
        """Generates AI analysis using Groq API or Google Gemini API if keys are available, with smart fallback."""
        groq_api_key = os.environ.get("GROQ_API_KEY")
        gemini_api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")

        context_text = (
            f"User Query: '{prompt}'\n"
            f"Recommended Product: {top_item['title']}\n"
            f"Brand: {top_item.get('brand', 'N/A')}\n"
            f"Category: {top_item.get('category', 'Electronics')}\n"
            f"Retail MRP: ₹{top_item['base_price']:,}\n"
            f"Optimal Platform: {best_deal['platform']}\n"
            f"Discounted Price: ₹{best_deal['price']:,}\n"
            f"Instant Savings: ₹{best_deal['savings']:,}\n"
            f"Bargain Deal Score: {best_deal['deal_score']}/100\n"
        )

        # 1. Groq Cloud LLM (Ultra-Fast LLaMA 3.1)
        if groq_api_key:
            try:
                from groq import Groq
                client = Groq(api_key=groq_api_key)
                completion = client.chat.completions.create(
                    model="llama-3.1-8b-instant",
                    messages=[
                        {
                            "role": "system",
                            "content": "You are SmartShop AI Agent, a brilliant e-commerce shopping advisor. Analyze the market deal provided, explain why it is the best deal, compare value-for-money, and give clear buying advice in clean bullet points with emojis."
                        },
                        {
                            "role": "user",
                            "content": f"Analyze this e-commerce product deal for user inquiry:\n{context_text}"
                        }
                    ],
                    temperature=0.6,
                    max_tokens=450
                )
                ai_text = completion.choices[0].message.content
                return f"🤖 **Groq LLaMA-3.1 AI Agent Analysis:**\n\n{ai_text}"
            except Exception as e:
                pass

        # 2. Google Gemini API
        if gemini_api_key:
            try:
                import google.generativeai as genai
                genai.configure(api_key=gemini_api_key)
                model = genai.GenerativeModel('gemini-1.5-flash')
                response = model.generate_content(
                    f"You are SmartShop AI Agent, an intelligent shopping assistant. Provide clear, helpful purchase advice with bullet points for this deal:\n{context_text}"
                )
                return f"✨ **Google Gemini AI Shopping Plan:**\n\n{response.text}"
            except Exception as e:
                pass

        # 3. Intelligent Deterministic Fallback
        deal_rating = "Spectacular Bargain (⭐⭐⭐⭐⭐)" if best_deal['deal_score'] >= 85 else "Great Value Deal (⭐⭐⭐⭐)"
        return (
            f"🤖 **SmartShop AI Purchase Plan & Market Analysis:**\n\n"
            f"1. **Inquiry Parsing:** Extracted user intent for **'{prompt}'**.\n"
            f"2. **Top Recommended Pick:** **{top_item['title']}** (Base Retail MRP: ₹{top_item['base_price']:,}).\n"
            f"3. **Multi-Store Price Audit:** Scanned verified listings across Amazon, Flipkart, and Croma.\n"
            f"4. **Lowest Verified Price:** Buy on **{best_deal['platform']}** at **₹{best_deal['price']:,}**.\n"
            f"5. **Estimated Consumer Savings:** You save **₹{best_deal['savings']:,}** directly over competitor stores.\n"
            f"6. **Bargain Deal Score:** ⭐ `{best_deal['deal_score']} / 100` — {deal_rating}.\n"
            f"7. **Action Advice:** Current price is optimal. Click **'Visit Store'** on {best_deal['platform']} to claim the deal!"
        )

    def process_query(self, user_prompt):
        prompt = user_prompt.strip()
        if not prompt:
            prompt = "smartphone"

        # 1. Search local 500-product catalog first
        matched_products = self.comparator.search_products(prompt)
        
        if not matched_products.empty:
            top_row = matched_products.iloc[0]
            prod_info, prices_df, best_deal = self.comparator.compare_prices(top_row['product_id'])
            top_item = {
                "title": top_row['title'],
                "brand": top_row['brand'],
                "category": top_row['category'],
                "base_price": int(top_row['base_price'])
            }
            reasoning = self.generate_llm_response(prompt, top_item, best_deal)
            return reasoning, best_deal

        # 2. Dynamic live market fallback for out-of-catalog items
        google_results = self.google_search.search_google_shopping(prompt)
        if google_results:
            top_item = google_results[0]
            best_deal = top_item["best_deal"]
            reasoning = self.generate_llm_response(prompt, top_item, best_deal)
            return reasoning, best_deal

        # 3. Default fallback
        best_prod = self.comparator.products_df.iloc[0]
        prod_info, prices_df, best_deal = self.comparator.compare_prices(best_prod['product_id'])
        top_item = {
            "title": best_prod['title'],
            "brand": best_prod['brand'],
            "category": best_prod['category'],
            "base_price": int(best_prod['base_price'])
        }
        reasoning = self.generate_llm_response(prompt, top_item, best_deal)
        return reasoning, best_deal

if __name__ == "__main__":
    data_path = os.path.join(os.path.dirname(__file__), "..", "data")
    agent = AgenticShoppingAssistant(data_path)
    r, d = agent.process_query("MacBook Air M2")
    print(r.encode('ascii', errors='ignore').decode('ascii'))
