# 🛍️ SmartShop AI: 3D Animated E-Commerce Intelligence & Multi-Platform Aggregation Platform

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Framework-Flask%20REST%20API-lightgrey.svg)](https://flask.palletsprojects.com/)
[![Three.js](https://img.shields.io/badge/3D%20WebGL-Three.js-black.svg)](https://threejs.org/)
[![PyTorch](https://img.shields.io/badge/Deep%20Learning-PyTorch%20%2F%20NumPy-red.svg)](https://pytorch.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Autonomous E-Commerce Intelligence:** 600+ Real Tech Products • Amazon • Flipkart • Croma • PyTorch NCF • 30-Day OLS Regression • 64-Dim Visual Search • Agentic RAG Assistant

---

## 📌 Project Overview

**SmartShop AI** is a state-of-the-art intelligent e-commerce platform built to solve marketplace fragmentation, erratic price volatility, and review information overload across major platforms (**Amazon India, Flipkart, and Croma**).

The platform features an **interactive 3D WebGL particle constellation**, a **cinematic 3D video hero showcase**, and an audited catalog of **600+ branded products** spanning **12 technology categories** with **1,800 real-time price feeds**.

---

## 🌟 Key Architecture & Capabilities

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│             3D Glassmorphic Web Experience (Three.js WebGL / Cinematic Video / JS)     │
└───────────────────────────────────────────┬────────────────────────────────────────────┘
                                            │ REST API (Port 5050)
                                            ▼
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                             Flask Backend REST Services Server                         │
├─────────────────┬─────────────────┬──────────────────┬────────────────┬────────────────┤
│  Multi-Store    │  PyTorch NCF    │ 30-Day Price OLS │ NLP Sentiment  │  Agentic RAG   │
│  Price Radar    │  Embeddings     │ Trend Forecaster │ Pros/Cons NLP  │  LLM Assistant │
│ (Amazon/Flip/Cr)│ (7.8k logs)     │ (18k history)    │ (1.2k reviews) │ (Groq/Gemini)  │
└─────────────────┴─────────────────┴──────────────────┴────────────────┴────────────────┘
```

### 1. 🎦 Interactive 3D Video Hero & Three.js WebGL Canvas
- **WebGL Particle Constellation:** 450+ interactive floating neon particles responding to mouse parallax in 3D perspective.
- **Cinematic 3D Video Showcase:** Integrated video presentation with voiceover narration, 3D card tilt physics, audio toggle (*Unmute/Mute*), and synchronized chapter scrubbers:
  - `0:00` — Intro Vortex
  - `0:02` — Radar Scan
  - `0:04` — Neural NCF
  - `0:06` — Price Drop AI
  - `0:08` — Commerce Hub

### 2. 📦 600+ Real Catalog Products across 12 Categories
Audited catalog in [`data/products.csv`](data/products.csv) across:
1. **Smartphones (50):** iPhone 15 Pro Max, Galaxy S24 Ultra, Pixel 8 Pro, OnePlus 12, etc.
2. **Laptops & Ultrabooks (50):** MacBook Pro M3, Dell XPS 15, Alienware m16, ROG Zephyrus, etc.
3. **Audio & Headphones (50):** Sony WH-1000XM5, Bose QC Ultra, AirPods Max, Sennheiser, etc.
4. **Smartwatches & Fitness (50):** Apple Watch Ultra 2, Galaxy Watch 6, Garmin Fenix 7X, etc.
5. **Smart TVs & Displays (50):** Sony Bravia OLED, Samsung Neo QLED, LG OLED evo, etc.
6. **Gaming Consoles & Gear (50):** PlayStation 5, Xbox Series X, Nintendo Switch, Steam Deck, etc.
7. **Cameras & Drones (50):** Sony Alpha A7 IV, Canon EOS R6, DJI Mini 4 Pro, GoPro 12, etc.
8. **Monitors & Displays (50):** LG UltraGear OLED, Samsung Odyssey Neo G9, Dell UltraSharp, etc.
9. **Tablets & E-Readers (50):** iPad Pro M4, Galaxy Tab S9, Kindle Paperwhite, OnePlus Pad, etc.
10. **Storage & Peripherals (50):** Samsung 990 PRO NVMe, SanDisk Extreme, Logitech MX Master, etc.
11. **Smart Home & IoT (50):** Amazon Echo Studio, Google Nest Hub, Dyson Purifier, Philips Hue, etc.
12. **Smart Wearables (50):** Ray-Ban Meta Smart Glasses, XREAL Air 2, Oura Ring Gen 3, etc.

### 3. 🏬 Multi-Store Price Aggregation & Bargain Scoring
- Audits verified prices simultaneously across **Amazon India, Flipkart, and Croma**.
- Calculates exact savings and a normalized **Bargain Deal Score (1–100)** factoring retail MRP discounts and platform ratings.

### 4. 🔍 360° AI Analysis Modal Popup
- Click **"360° AI Analysis"** on any card to launch an all-in-one modal featuring:
  - 3-platform comparison table with direct store links.
  - Interactive SVG sparkline displaying 30-day verified price movement.
  - 7-day projected price target with automated **BUY NOW** or **WAIT** signals.
  - AI-extracted **Pros & Cons** from customer reviews.

### 5. 🧠 PyTorch Neural Collaborative Filtering (NCF)
- Dual embedding layers mapping users and products into a 16-dimensional latent space.
- Trained on 7,800+ user interactions with NumPy collaborative filtering fallback.

### 6. 📈 30-Day Time-Series Price Trend Forecaster
- Ordinary Least Squares (OLS) regression over 18,000 historical price logs projecting 7-day target prices.

### 7. 💬 NLP Review Sentiment (Pros & Cons Synthesizer)
- Category-aware natural language parsing extracting verified benefits and considerations across 1,200 reviews.

### 8. 📸 64-Dimensional Computer Vision Visual Similarity
- Deep feature vector extraction ranked via normalized Cosine Similarity.

### 9. 🤖 Agentic RAG Conversational Assistant
- Grounded shopping advisor powered by **Groq Cloud (LLaMA-3.1-8B-Instant)** and **Google Gemini (Gemini-1.5-Flash)** with deterministic rule fallbacks.

### 10. ❤️ Saved Watchlist Drawer
- Browser `localStorage` deal saving with simulated price drop tracking.

---

## 📂 Project Structure

```
shop_ai/
├── api/
│   └── index.py                     # Vercel serverless gateway
├── data/
│   ├── products.csv                 # 600 verified products
│   ├── platform_prices.csv          # 1,800 store listings (Amazon/Flipkart/Croma)
│   ├── user_interactions.csv        # 7,815 NCF interaction logs
│   ├── price_history.csv            # 18,000 30-day historical price points
│   └── product_reviews.csv          # 1,200 parsed customer reviews
├── src/
│   ├── ai_agent.py                  # Groq LLaMA-3.1 & Gemini RAG assistant
│   ├── data_generator.py            # 600-product 12-category catalog generator
│   ├── google_search.py             # Live fallback market scraper
│   ├── live_scraper.py              # Platform-specific link generator
│   ├── nlp_sentiment.py             # NLP customer review pros/cons extractor
│   ├── price_comparator.py          # 3-store pricing & bargain scoring engine
│   ├── price_forecaster.py          # OLS regression 30-day trend forecaster
│   ├── recommender_model.py         # PyTorch / NumPy NCF recommender
│   └── visual_search.py             # 64-dim visual similarity matcher
├── static/
│   └── videos/
│       └── smartshop_ai_intro.mp4   # 3D cinematic video render
├── templates/
│   └── index.html                   # 3D WebGL Three.js glassmorphic dashboard
├── app.py                           # Core Flask REST API application
├── Procfile                         # Gunicorn runner for Render
├── vercel.json                      # Serverless rewrite rules for Vercel
├── requirements.txt                 # Lightweight (<40MB) dependencies
└── README.md                        # Documentation
```

---

## 🚀 Quickstart & Local Installation

### 1. Clone the Repository
```bash
git clone https://github.com/suryaramisetty70-pyt/shop_ai.git
cd shop_ai
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Platform
```bash
python app.py
```
Open your browser and navigate to:
👉 **`http://localhost:5050`**

---

## 🌐 Cloud Deployment

- **Vercel:** Configured via `vercel.json` and `api/index.py` (<40MB bundle, zero heavy dependencies).
- **Render:** Configured via `Procfile` (`web: gunicorn app:app`).

---

## 📄 License
This project is licensed under the MIT License.
