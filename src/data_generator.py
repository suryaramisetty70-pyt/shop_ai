import os
import pandas as pd
import numpy as np
import random

def generate_500_products_dataset(output_dir):
    """
    Generates a massive, realistic 500-product dataset across 10 e-commerce categories
    with 1,500 multi-store price listings, 5,000+ user interactions, 1,000+ customer reviews,
    and 15,000 price history logs.
    """
    os.makedirs(output_dir, exist_ok=True)
    np.random.seed(42)
    random.seed(42)

    categories = {
        "Smartphones": {
            "brands": ["Apple", "Samsung", "OnePlus", "Google", "Xiaomi", "Realme", "Vivo", "OPPO", "Nothing", "Motorola", "iQOO"],
            "base_min": 9999, "base_max": 159900,
            "images": [
                "https://images.unsplash.com/photo-1695048133142-1a20484d2569?w=400",
                "https://images.unsplash.com/photo-1610945265064-0e34e5519bbf?w=400",
                "https://images.unsplash.com/photo-1598327105666-5b89351aff97?w=400",
                "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=400"
            ]
        },
        "Laptops": {
            "brands": ["Apple", "Dell", "HP", "Lenovo", "ASUS", "Acer", "MSI", "Samsung", "LG"],
            "base_min": 29990, "base_max": 249900,
            "images": [
                "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=400",
                "https://images.unsplash.com/photo-1593642632823-8f785ba67e45?w=400",
                "https://images.unsplash.com/photo-1603302576837-37561b2e2302?w=400",
                "https://images.unsplash.com/photo-1541807084-5c52b6b3adef?w=400"
            ]
        },
        "Audio": {
            "brands": ["Sony", "Bose", "Apple", "JBL", "Sennheiser", "boAt", "Noise", "Skullcandy", "Marshall"],
            "base_min": 1499, "base_max": 39990,
            "images": [
                "https://images.unsplash.com/photo-1546435770-a3e426bf472b?w=400",
                "https://images.unsplash.com/photo-1600294037681-c80b4cb5b434?w=400",
                "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=400",
                "https://images.unsplash.com/photo-1545454675-3531b543be5d?w=400"
            ]
        },
        "Smartwatches": {
            "brands": ["Apple", "Samsung", "Garmin", "Fitbit", "Noise", "Fire-Boltt", "Amazfit", "Fossil"],
            "base_min": 1999, "base_max": 89900,
            "images": [
                "https://images.unsplash.com/photo-1508685096489-7aacd43bd3b1?w=400",
                "https://images.unsplash.com/photo-1579586337278-3befd40fd17a?w=400",
                "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=400"
            ]
        },
        "Accessories": {
            "brands": ["Logitech", "Anker", "Samsung", "SanDisk", "TP-Link", "Belkin", "Seagate", "WD"],
            "base_min": 499, "base_max": 19990,
            "images": [
                "https://images.unsplash.com/photo-1609592424074-1b156b823e25?w=400",
                "https://images.unsplash.com/photo-1615663245857-ac93bb7c39e7?w=400",
                "https://images.unsplash.com/photo-1597872200969-2b65d56bd16b?w=400"
            ]
        },
        "Gaming": {
            "brands": ["Sony PlayStation", "Microsoft Xbox", "Nintendo", "Razer", "Logitech G", "Corsair"],
            "base_min": 2499, "base_max": 59990,
            "images": [
                "https://images.unsplash.com/photo-1606813907291-d86efa9b94db?w=400",
                "https://images.unsplash.com/photo-1621259182978-fbf93132d53d?w=400"
            ]
        },
        "Cameras & Drones": {
            "brands": ["Sony", "Canon", "Nikon", "DJI", "GoPro", "Fujifilm"],
            "base_min": 24990, "base_max": 289900,
            "images": [
                "https://images.unsplash.com/photo-1516035069371-29a1b244cc32?w=400",
                "https://images.unsplash.com/photo-1507679799987-c73779587ccf?w=400"
            ]
        },
        "Smart TVs & Home": {
            "brands": ["Sony", "Samsung", "LG", "TCL", "Xiaomi", "OnePlus", "Hisense"],
            "base_min": 14990, "base_max": 199900,
            "images": [
                "https://images.unsplash.com/photo-1593784991095-a205069470b6?w=400",
                "https://images.unsplash.com/photo-1593359677879-a4bb92f829d1?w=400"
            ]
        },
        "Tablets & E-Readers": {
            "brands": ["Apple", "Samsung", "Lenovo", "Amazon Kindle", "Xiaomi"],
            "base_min": 9999, "base_max": 129900,
            "images": [
                "https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=400"
            ]
        },
        "Monitors & Displays": {
            "brands": ["LG", "Samsung", "Dell", "BenQ", "Acer", "ViewSonic"],
            "base_min": 7999, "base_max": 89900,
            "images": [
                "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=400"
            ]
        }
    }

    products_data = []
    prod_id = 101

    product_name_templates = {
        "Smartphones": ["Pro Max 5G", "Ultra 5G", "Lite Edition", "Fold 5G", "Flip 5G", "Prime 5G", "Nord Edition", "Neo 5G"],
        "Laptops": ["Thin & Light Laptop", "Gaming Laptop RTX 4060", "Ultrabook 14", "Studio Edition", "Creator Laptop 16"],
        "Audio": ["Wireless Noise Cancelling Headphones", "True Wireless Earbuds", "Portable Bluetooth Speaker", "Soundbar 5.1"],
        "Smartwatches": ["GPS Fitness Smartwatch", "AMOLED Calling Watch", "Sports Edition Watch", "Classic Leather Watch"],
        "Accessories": ["Wireless Mechanical Keyboard", "Ergonomic Optical Mouse", "Ultra High-Speed NVMe SSD 1TB", "100W GaN Fast Charger"],
        "Gaming": ["Console Edition", "Wireless Controller", "Mechanical Gaming Keyboard", "Surround Sound Gaming Headset"],
        "Cameras & Drones": ["Mirrorless Camera 4K", "Action Camera Waterproof", "Compact 4K Drone", "Vlogging Kit"],
        "Smart TVs & Home": ["4K Ultra HD Smart QLED TV", "OLED Cinema Display TV", "Dolby Vision Smart TV 55 inch"],
        "Tablets & E-Readers": ["11-inch Wi-Fi Tablet", "Paperwhite E-Reader", "Pro 12.9 Tablet"],
        "Monitors & Displays": ["27-inch 144Hz Gaming Monitor", "4K IPS Color Accurate Monitor", "34-inch Curved Ultrawide Monitor"]
    }

    for cat_name, cat_info in categories.items():
        # Generate 50 products per category -> total 500 products!
        for i in range(50):
            brand = random.choice(cat_info["brands"])
            suffix = random.choice(product_name_templates[cat_name])
            model_num = random.choice([10, 12, 14, 15, 20, 24, 30, 50, 100, 200, 500, 1000])
            
            title = f"{brand} {cat_name[:-1] if cat_name.endswith('s') else cat_name} {model_num} {suffix}"
            base_price = round(random.randint(cat_info["base_min"], cat_info["base_max"]), -2)
            img = random.choice(cat_info["images"])

            products_data.append({
                "product_id": prod_id,
                "title": title,
                "category": cat_name,
                "brand": brand,
                "base_price": base_price,
                "image_url": img
            })
            prod_id += 1

    df_products = pd.DataFrame(products_data)
    df_products.to_csv(os.path.join(output_dir, "products.csv"), index=False)

    # Multi-Store Prices (500 products x 3 stores = 1,500 listings)
    platforms = ["Amazon", "Flipkart", "Croma"]
    pricing_records = []

    for item in products_data:
        p_id = item["product_id"]
        base = item["base_price"]

        variations = {
            "Amazon": round(base * random.uniform(0.92, 0.98), -1),
            "Flipkart": round(base * random.uniform(0.90, 0.96), -1),
            "Croma": round(base * random.uniform(0.93, 0.99), -1)
        }

        for plat in platforms:
            price = variations[plat]
            rating = round(random.uniform(4.0, 4.9), 1)
            reviews = random.randint(150, 9500)
            
            pricing_records.append({
                "product_id": p_id,
                "platform": plat,
                "price": price,
                "rating": rating,
                "review_count": reviews,
                "in_stock": True,
                "buy_link": f"https://www.{plat.lower()}.com/search?q={item['title'].replace(' ', '+')}"
            })

    df_pricing = pd.DataFrame(pricing_records)
    df_pricing.to_csv(os.path.join(output_dir, "platform_prices.csv"), index=False)

    # User Interaction Stream (200 users, 5,000+ interactions)
    num_users = 200
    interaction_records = []
    for u_id in range(1, num_users + 1):
        fav_cat = random.choice(list(categories.keys()))
        interacted_prods = random.sample([p["product_id"] for p in products_data], random.randint(15, 35))
        for p_id in interacted_prods:
            prod = next(p for p in products_data if p["product_id"] == p_id)
            if prod["category"] == fav_cat:
                rating = random.choice([4.0, 4.5, 5.0])
            else:
                rating = random.choice([2.0, 3.0, 3.5, 4.0])
            interaction_records.append({
                "user_id": u_id,
                "product_id": p_id,
                "rating": rating,
                "timestamp": pd.Timestamp.now()
            })
    df_interactions = pd.DataFrame(interaction_records)
    df_interactions.to_csv(os.path.join(output_dir, "user_interactions.csv"), index=False)

    # Customer Reviews (1,000 reviews)
    review_records = []
    for item in products_data:
        review_records.append({
            "product_id": item["product_id"],
            "review_text": f"Excellent value for money. Build quality of {item['title']} is outstanding and performance is smooth.",
            "rating": 4.5
        })
        review_records.append({
            "product_id": item["product_id"],
            "review_text": f"Good product, fast delivery. Price could be slightly lower, but battery and display performance are top notch.",
            "rating": 4.0
        })
    df_reviews = pd.DataFrame(review_records)
    df_reviews.to_csv(os.path.join(output_dir, "product_reviews.csv"), index=False)

    # Price History Logs (500 products x 30 days = 15,000 price entries)
    history_records = []
    dates = pd.date_range(end=pd.Timestamp.now(), periods=30, freq='D')
    for item in products_data:
        base = item["base_price"]
        trend = np.linspace(base * random.uniform(1.03, 1.07), base * random.uniform(0.92, 0.96), 30)
        noise = np.random.normal(0, base * 0.008, 30)
        prices = np.round(trend + noise, -1)
        for i, d in enumerate(dates):
            history_records.append({
                "product_id": item["product_id"],
                "date": d.strftime('%Y-%m-%d'),
                "price": prices[i]
            })
    df_history = pd.DataFrame(history_records)
    df_history.to_csv(os.path.join(output_dir, "price_history.csv"), index=False)

    print(f"Generated 500-Product Massive Dataset in '{output_dir}':")
    print(f"   - products.csv ({len(products_data)} products)")
    print(f"   - platform_prices.csv ({len(df_pricing)} store listings)")
    print(f"   - user_interactions.csv ({len(df_interactions)} user logs)")
    print(f"   - product_reviews.csv ({len(df_reviews)} reviews)")
    print(f"   - price_history.csv ({len(df_history)} price trend entries)")

generate_datasets = generate_500_products_dataset

if __name__ == "__main__":
    data_path = os.path.join(os.path.dirname(__file__), "..", "data")
    generate_500_products_dataset(data_path)
