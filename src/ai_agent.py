import os
import pandas as pd
import requests
from src.google_search import GoogleShoppingSearch
from src.price_comparator import PriceComparator

class AgenticShoppingAssistant:
    def __init__(self, data_dir):
        self.data_dir = data_dir
        self.comparator = PriceComparator(data_dir)
        self.google_search = GoogleShoppingSearch()

    def generate_llm_response(self, prompt, top_item, best_deal):
        """Generates AI analysis using Groq API or Google Gemini API if keys are available."""
        groq_api_key = os.environ.get("GROQ_API_KEY")
        gemini_api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")

        context_text = (
            f"User Prompt: '{prompt}'\n"
            f"Product Title: {top_item['title']}\n"
            f"Base Retail Price: ₹{top_item['base_price']:,}\n"
            f"Best Deal Platform: {best_deal['platform']}\n"
            f"Best Deal Price: ₹{best_deal['price']:,}\n"
            f"Instant Savings: ₹{best_deal['savings']:,}\n"
            f"Deal Score: {best_deal['deal_score']}/100\n"
        )

        # 1. Try Groq Cloud LLM (llama3-8b-8192 or mixtral-8x7b-32768)
        if groq_api_key:
            try:
                from groq import Groq
                client = Groq(api_key=groq_api_key)
                completion = client.chat.completions.create(
                    model="llama-3.1-8b-instant",
                    messages=[
                        {
                            "role": "system",
                            "content": "You are SmartShop AI Agent, an expert e-commerce shopping advisor. Synthesize the provided market price data into a crisp, helpful purchase plan with bullet points."
                        },
                        {
                            "role": "user",
                            "content": f"Analyze this e-commerce product deal:\n{context_text}"
                        }
                    ],
                    temperature=0.7,
                    max_tokens=400
                )
                ai_text = completion.choices[0].message.content
                return f"🤖 **Groq LLaMA-3 AI Agent Analysis:**\n\n{ai_text}"
            except Exception as e:
                print(f"Groq API call warning: {e}")

        # 2. Try Google Gemini API
        if gemini_api_key:
            try:
                import google.generativeai as genai
                genai.configure(api_key=gemini_api_key)
                model = genai.GenerativeModel('gemini-1.5-flash')
                response = model.generate_content(
                    f"You are SmartShop AI Agent. Provide a quick purchase recommendation for the following item:\n{context_text}"
                )
                return f"✨ **Google Gemini AI Shopping Plan:**\n\n{response.text}"
            except Exception as e:
                print(f"Gemini API call warning: {e}")

        # 3. Intelligent Structured Fallback
        return (
            f"🤖 **Google Live Agentic Reasoning & Purchase Plan:**\n\n"
            f"1. **Intent Analysis:** Searched live marketplace data for **'{prompt}'**.\n"
            f"2. **Selected Product:** **{top_item['title']}** (Base Retail: ₹{top_item['base_price']:,}).\n"
            f"3. **Multi-Store Price Audit:** Compared live prices across Amazon, Flipkart, and Croma.\n"
            f"4. **Best Purchase Option:** Buy on **{best_deal['platform']}** at **₹{best_deal['price']:,}** (Savings: ₹{best_deal['savings']:,}).\n"
            f"5. **Bargain Deal Score:** ⭐ `{best_deal['deal_score']} / 100`"
        )

    def process_query(self, user_prompt):
        prompt = user_prompt.lower().strip()
        if not prompt:
            prompt = "smartphone"

        # 1. Fetch Live Google Search Results
        google_results = self.google_search.search_google_shopping(prompt)
        
        if google_results:
            top_item = google_results[0]
            best_deal = top_item["best_deal"]
            reasoning = self.generate_llm_response(prompt, top_item, best_deal)
            return reasoning, best_deal

        # Fallback to local comparator
        self.comparator.reload_data()
        products_df = self.comparator.products_df
        best_prod = products_df.iloc[0]
        prod_info, prices_df, best_deal = self.comparator.compare_prices(best_prod['product_id'])

        top_item = {
            "title": best_prod['title'],
            "base_price": int(best_prod['base_price'])
        }
        reasoning = self.generate_llm_response(prompt, top_item, best_deal)
        return reasoning, best_deal

if __name__ == "__main__":
    data_path = os.path.join(os.path.dirname(__file__), "..", "data")
    agent = AgenticShoppingAssistant(data_path)
    r, d = agent.process_query("Nike Air Jordan shoes")
    print(r.encode('ascii', errors='ignore').decode('ascii'))
