# 🛍️ SmartShop AI: 7-Module E-Commerce Price Comparison & AI Recommendation System

**Course:** Minor Project-I (VTU / CSE - AI & Data Science)  
**Project Title:** SmartShop AI – Multi-Platform Price Aggregation, Neural Collaborative Filtering, Price Drop Forecasting, NLP Sentiment Analysis, Visual Search, and Agentic RAG Assistant  
**Stack:** Python 3.10+, Flask REST API, PyTorch, Scikit-Learn, HTML5 / Glassmorphic CSS3 / Vanilla JS  

---

## 📌 Project Overview
**SmartShop AI** is an end-to-end intelligent e-commerce shopping platform built to solve information overload and price disparity across e-commerce marketplaces (**Amazon, Flipkart, Croma**).

The system unifies **500 catalog products** across 10 main categories with **live Google Search scraping capabilities** for unlimited product search, combined with 6 advanced AI/ML modules.

---

## 🌟 7 Core Modules & Features

1. 💰 **Multi-Platform Price Comparison Engine**
   - Side-by-side real-time price, rating, and review count comparison across Amazon, Flipkart, and Croma.
   - Calculates exact savings and a **Bargain Deal Score (1–100)**.
2. 🔍 **Unlimited Google Search Live Scraping**
   - Automatically fallback-queries live Google Search results for products outside the local catalog.
3. 🤖 **PyTorch Neural Collaborative Filtering (NCF)**
   - Uses deep user/item embedding networks (16-dimensional latent space) trained on 5,000+ interaction logs to deliver personalized product recommendations.
4. 📈 **Price Drop Forecasting & Trend Analysis**
   - Time-series linear regression model trained on 90-day price trends.
   - Provides clear decision signals: **"BUY NOW"** or **"WAIT FOR PRICE DROP"**.
5. 💬 **NLP Review Sentiment Analysis (Pros & Cons)**
   - Natural Language Processing pipeline that extracts positive and negative sentiment markers (Pros & Cons) from user reviews.
6. 📷 **Visual Search & Computer Vision Matching**
   - Cosine similarity matching over 64-dimensional visual feature vectors to locate visually similar items.
7. 🧠 **Agentic RAG Shopping Assistant**
   - Retrieval-Augmented Generation (RAG) assistant parsing natural language queries with live search integration.

---

## 🏗️ Architecture Diagram

```
┌───────────────────────────────────────────────────────────────────────────────┐
│                      Glassmorphic SPA UI (HTML5 / Vanilla JS)                 │
└──────────────────────────────────────┬────────────────────────────────────────┘
                                       │ REST API calls (Port 5050)
                                       ▼
┌───────────────────────────────────────────────────────────────────────────────┐
│                           Flask Backend REST API Server                       │
├──────────────┬──────────────┬──────────────┬──────────────┬───────────────────┤
│ Price Engine │ NCF Model    │ Price Forecast│ Sentiment NLP│ Visual & AI Agent │
│ (3 Platforms)│ (PyTorch)    │ (Regression) │ (Pros/Cons)  │ (Google Search)   │
└──────────────┴──────────────┴──────────────┴──────────────┴───────────────────┘
```

---

## 🛠️ Tech Stack & Dependencies

- **Backend Framework:** Flask (Python 3.10+)
- **Deep Learning:** PyTorch (`torch`), Scikit-Learn (`scikit-learn`)
- **Data Engineering:** Pandas, NumPy
- **Image Processing & NLP:** Pillow, Regex NLP Tokenizer
- **Frontend Stack:** Glassmorphism UI, FontAwesome 6, Vanilla JS Async `fetch()`
- **Web Scraping:** Google Search / DuckDuckGo HTML Parser (`requests`, `BeautifulSoup4`)

---

## 🚀 Quick Start & Installation

### 1. Clone the Repository
```bash
git clone https://github.com/suryaramisetty70-pyt/shop_ai.git
cd shop_ai
```

### 2. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 3. Generate Datasets (500 Products & 5,000 Interaction Logs)
```bash
python src/data_generator.py
```

### 4. Run the Flask Web Application
```bash
python app.py
```

Open your browser at: **[http://localhost:5050](http://localhost:5050)**

---

## 📁 Directory Structure

```
shop_ai/
├── app.py                     # Main Flask REST API & Web Server (Port 5050)
├── requirements.txt           # Python dependency manifest
├── README.md                  # Project documentation
├── templates/
│   └── index.html             # Glassmorphic Bento Grid SPA Frontend
├── data/                      # 500-product e-commerce datasets
│   ├── products.csv
│   ├── platform_prices.csv
│   ├── user_interactions.csv
│   ├── price_history.csv
│   └── product_reviews.csv
└── src/                       # AI/ML Engine Source Modules
    ├── data_generator.py      # Dataset pipeline generator
    ├── price_comparator.py    # Multi-store price comparison & bargain scoring
    ├── recommender_model.py   # PyTorch NCF Deep Learning Model
    ├── price_forecaster.py    # Time-series price drop forecasting
    ├── nlp_sentiment.py       # NLP review sentiment pros/cons extractor
    ├── visual_search.py       # Computer vision similarity matcher
    ├── ai_agent.py            # RAG AI shopping assistant
    └── google_search.py       # Live web search scraper
```

---

## 🎓 Viva & Presentation Guide

When presenting to evaluation panel / faculty:
1. **Multi-Platform Price Comparison:** Search for `"iPhone"` or `"Sony Headphones"` to demonstrate Amazon, Flipkart, and Croma price comparison with deal scores.
2. **AI Recommendation Engine:** Toggle user IDs (`User #1`, `User #5`) to demonstrate dynamic PyTorch NCF recommendations.
3. **Price Forecasting:** Select any product to view 30-day price trend graphs and **BUY NOW / WAIT** decision badges.
4. **Live Google Search:** Enter any product outside the catalog to show live internet market data integration.
