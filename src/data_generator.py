import os
import pandas as pd
import numpy as np
import random

def generate_500_products_dataset(output_dir):
    """
    Generates a realistic 500-product dataset across 10 genuine consumer electronics categories
    with authentic brand names, accurate Indian market pricing (INR), multi-store price listings,
    user interaction logs, customer reviews, and 30-day historical price logs.
    """
    os.makedirs(output_dir, exist_ok=True)
    np.random.seed(42)
    random.seed(42)

    # 10 Detailed Categories with 50 REAL Product Items Each = 500 Products Total
    catalog_blueprint = {
        "Smartphones": [
            ("Apple iPhone 15 Pro Max (256GB)", "Apple", 159900, "https://images.unsplash.com/photo-1695048133142-1a20484d2569?w=400"),
            ("Apple iPhone 15 Pro (128GB)", "Apple", 134900, "https://images.unsplash.com/photo-1695048133142-1a20484d2569?w=400"),
            ("Apple iPhone 15 Plus (128GB)", "Apple", 89900, "https://images.unsplash.com/photo-1695048133142-1a20484d2569?w=400"),
            ("Apple iPhone 15 (128GB)", "Apple", 79900, "https://images.unsplash.com/photo-1695048133142-1a20484d2569?w=400"),
            ("Apple iPhone 14 (128GB)", "Apple", 61900, "https://images.unsplash.com/photo-1610945265064-0e34e5519bbf?w=400"),
            ("Apple iPhone 13 (128GB)", "Apple", 52900, "https://images.unsplash.com/photo-1610945265064-0e34e5519bbf?w=400"),
            ("Apple iPhone SE (64GB, 2022)", "Apple", 43900, "https://images.unsplash.com/photo-1610945265064-0e34e5519bbf?w=400"),
            ("Samsung Galaxy S24 Ultra 5G (256GB)", "Samsung", 129999, "https://images.unsplash.com/photo-1610945265064-0e34e5519bbf?w=400"),
            ("Samsung Galaxy S24+ 5G (256GB)", "Samsung", 99999, "https://images.unsplash.com/photo-1610945265064-0e34e5519bbf?w=400"),
            ("Samsung Galaxy S24 5G (128GB)", "Samsung", 74999, "https://images.unsplash.com/photo-1610945265064-0e34e5519bbf?w=400"),
            ("Samsung Galaxy S23 Ultra 5G", "Samsung", 109999, "https://images.unsplash.com/photo-1610945265064-0e34e5519bbf?w=400"),
            ("Samsung Galaxy S23 FE 5G (128GB)", "Samsung", 49999, "https://images.unsplash.com/photo-1610945265064-0e34e5519bbf?w=400"),
            ("Samsung Galaxy Z Fold 5 5G (256GB)", "Samsung", 154999, "https://images.unsplash.com/photo-1598327105666-5b89351aff97?w=400"),
            ("Samsung Galaxy Z Flip 5 5G (256GB)", "Samsung", 99999, "https://images.unsplash.com/photo-1598327105666-5b89351aff97?w=400"),
            ("Samsung Galaxy A55 5G (128GB)", "Samsung", 39999, "https://images.unsplash.com/photo-1598327105666-5b89351aff97?w=400"),
            ("Samsung Galaxy A35 5G (128GB)", "Samsung", 30999, "https://images.unsplash.com/photo-1598327105666-5b89351aff97?w=400"),
            ("Samsung Galaxy M34 5G (128GB)", "Samsung", 16999, "https://images.unsplash.com/photo-1598327105666-5b89351aff97?w=400"),
            ("Google Pixel 8 Pro (128GB)", "Google", 106999, "https://images.unsplash.com/photo-1598327105666-5b89351aff97?w=400"),
            ("Google Pixel 8 5G (128GB)", "Google", 75999, "https://images.unsplash.com/photo-1598327105666-5b89351aff97?w=400"),
            ("Google Pixel 8a 5G (128GB)", "Google", 52999, "https://images.unsplash.com/photo-1598327105666-5b89351aff97?w=400"),
            ("Google Pixel 7 Pro (128GB)", "Google", 68999, "https://images.unsplash.com/photo-1598327105666-5b89351aff97?w=400"),
            ("OnePlus 12 5G (16GB RAM, 512GB)", "OnePlus", 69999, "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=400"),
            ("OnePlus 12R 5G (8GB RAM, 128GB)", "OnePlus", 39999, "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=400"),
            ("OnePlus Open Foldable 5G (512GB)", "OnePlus", 139999, "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=400"),
            ("OnePlus Nord 4 5G (256GB)", "OnePlus", 32999, "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=400"),
            ("OnePlus Nord CE 4 5G (128GB)", "OnePlus", 24999, "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=400"),
            ("Xiaomi 14 Ultra (16GB RAM, 512GB)", "Xiaomi", 99999, "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=400"),
            ("Xiaomi 14 5G (12GB RAM, 512GB)", "Xiaomi", 69999, "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=400"),
            ("Redmi Note 13 Pro+ 5G (256GB)", "Xiaomi", 31999, "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=400"),
            ("Redmi Note 13 5G (128GB)", "Xiaomi", 17999, "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=400"),
            ("Vivo X100 Pro 5G (Zeiss Optics, 512GB)", "Vivo", 89999, "https://images.unsplash.com/photo-1598327105666-5b89351aff97?w=400"),
            ("Vivo V30 Pro 5G (512GB)", "Vivo", 46999, "https://images.unsplash.com/photo-1598327105666-5b89351aff97?w=400"),
            ("Vivo T3 5G (128GB)", "Vivo", 19999, "https://images.unsplash.com/photo-1598327105666-5b89351aff97?w=400"),
            ("iQOO 12 5G (Snapdragon 8 Gen 3)", "iQOO", 52999, "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=400"),
            ("iQOO Neo 9 Pro 5G (256GB)", "iQOO", 37999, "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=400"),
            ("iQOO Z9 5G (128GB)", "iQOO", 19999, "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=400"),
            ("Nothing Phone (2) 5G (12GB/256GB)", "Nothing", 39999, "https://images.unsplash.com/photo-1598327105666-5b89351aff97?w=400"),
            ("Nothing Phone (2a) 5G (128GB)", "Nothing", 23999, "https://images.unsplash.com/photo-1598327105666-5b89351aff97?w=400"),
            ("Motorola Edge 50 Ultra 5G (512GB)", "Motorola", 59999, "https://images.unsplash.com/photo-1598327105666-5b89351aff97?w=400"),
            ("Motorola Edge 50 Pro 5G (256GB)", "Motorola", 31999, "https://images.unsplash.com/photo-1598327105666-5b89351aff97?w=400"),
            ("Motorola Razr 40 Ultra Flip Phone", "Motorola", 69999, "https://images.unsplash.com/photo-1598327105666-5b89351aff97?w=400"),
            ("Motorola Moto G84 5G (256GB)", "Motorola", 18999, "https://images.unsplash.com/photo-1598327105666-5b89351aff97?w=400"),
            ("Realme GT 6 5G (Snapdragon 8s Gen 3)", "Realme", 40999, "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=400"),
            ("Realme 12 Pro+ 5G (Periscope Camera)", "Realme", 29999, "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=400"),
            ("Realme Narzo 70 Pro 5G", "Realme", 19999, "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=400"),
            ("OPPO Find N3 Flip 5G", "OPPO", 94999, "https://images.unsplash.com/photo-1598327105666-5b89351aff97?w=400"),
            ("OPPO Reno 11 Pro 5G", "OPPO", 39999, "https://images.unsplash.com/photo-1598327105666-5b89351aff97?w=400"),
            ("POCO X6 Pro 5G (Dimensity 8300 Ultra)", "POCO", 26999, "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=400"),
            ("POCO F6 5G (Snapdragon 8s Gen 3)", "POCO", 31999, "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=400"),
            ("POCO M6 5G (128GB)", "POCO", 10999, "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=400")
        ],
        "Laptops": [
            ("Apple MacBook Air M3 (13.6-inch, 8GB/256GB)", "Apple", 114900, "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=400"),
            ("Apple MacBook Air M3 (15.3-inch, 16GB/512GB)", "Apple", 154900, "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=400"),
            ("Apple MacBook Air M2 (13.6-inch, 8GB/256GB)", "Apple", 99900, "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=400"),
            ("Apple MacBook Pro 14-inch (M3 Pro, 18GB/512GB)", "Apple", 199900, "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=400"),
            ("Apple MacBook Pro 16-inch (M3 Max, 36GB/1TB)", "Apple", 349900, "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=400"),
            ("Dell XPS 13 Plus (Core i7 13th Gen, 16GB/1TB OLED)", "Dell", 169990, "https://images.unsplash.com/photo-1593642632823-8f785ba67e45?w=400"),
            ("Dell XPS 15 9530 (Core i9, RTX 4070, 32GB/1TB)", "Dell", 249990, "https://images.unsplash.com/photo-1593642632823-8f785ba67e45?w=400"),
            ("Dell Inspiron 15 3520 (Core i5 12th Gen, 16GB/512GB)", "Dell", 54990, "https://images.unsplash.com/photo-1593642632823-8f785ba67e45?w=400"),
            ("Dell Alienware m16 R2 Gaming Laptop (RTX 4070)", "Dell", 214990, "https://images.unsplash.com/photo-1603302576837-37561b2e2302?w=400"),
            ("Dell G15 5530 Gaming (Core i7, RTX 4060, 16GB)", "Dell", 99990, "https://images.unsplash.com/photo-1603302576837-37561b2e2302?w=400"),
            ("HP Spectre x360 14 2-in-1 OLED (Core Ultra 7)", "HP", 164999, "https://images.unsplash.com/photo-1541807084-5c52b6b3adef?w=400"),
            ("HP Envy x360 15 (Core i7, 16GB/1TB SSD Touch)", "HP", 109999, "https://images.unsplash.com/photo-1541807084-5c52b6b3adef?w=400"),
            ("HP Pavilion 15 (Core i5 13th Gen, 16GB/512GB)", "HP", 64999, "https://images.unsplash.com/photo-1541807084-5c52b6b3adef?w=400"),
            ("HP OMEN 16 Gaming Laptop (Ryzen 7, RTX 4070)", "HP", 139999, "https://images.unsplash.com/photo-1603302576837-37561b2e2302?w=400"),
            ("HP Victus 15 Gaming (Core i5, RTX 3050, 16GB)", "HP", 68999, "https://images.unsplash.com/photo-1603302576837-37561b2e2302?w=400"),
            ("HP 15s Thin & Light (Core i3 12th Gen, 8GB/512GB)", "HP", 38999, "https://images.unsplash.com/photo-1541807084-5c52b6b3adef?w=400"),
            ("Lenovo ThinkPad X1 Carbon Gen 11 (Core i7, 16GB/1TB)", "Lenovo", 189990, "https://images.unsplash.com/photo-1593642632823-8f785ba67e45?w=400"),
            ("Lenovo Yoga Slim 7i Carbon (Core i7 13th Gen, 1kg)", "Lenovo", 129990, "https://images.unsplash.com/photo-1541807084-5c52b6b3adef?w=400"),
            ("Lenovo IdeaPad Slim 3 (Core i5 12th Gen, 16GB/512GB)", "Lenovo", 52990, "https://images.unsplash.com/photo-1593642632823-8f785ba67e45?w=400"),
            ("Lenovo Legion Pro 5i Gaming (Core i9, RTX 4070)", "Lenovo", 179990, "https://images.unsplash.com/photo-1603302576837-37561b2e2302?w=400"),
            ("Lenovo LOQ 15 Gaming (Core i5 13th Gen, RTX 4050)", "Lenovo", 78990, "https://images.unsplash.com/photo-1603302576837-37561b2e2302?w=400"),
            ("ASUS ROG Zephyrus G14 (Ryzen 9, RTX 4070, OLED)", "ASUS", 174990, "https://images.unsplash.com/photo-1603302576837-37561b2e2302?w=400"),
            ("ASUS ROG Strix G16 (Core i9 14th Gen, RTX 4080)", "ASUS", 219990, "https://images.unsplash.com/photo-1603302576837-37561b2e2302?w=400"),
            ("ASUS TUF Gaming F15 (Core i7 12th Gen, RTX 4060)", "ASUS", 89990, "https://images.unsplash.com/photo-1603302576837-37561b2e2302?w=400"),
            ("ASUS ZenBook 14 OLED (Intel Core Ultra 7, 16GB)", "ASUS", 109990, "https://images.unsplash.com/photo-1541807084-5c52b6b3adef?w=400"),
            ("ASUS Vivobook 16X (Ryzen 7, 16GB/512GB SSD)", "ASUS", 58990, "https://images.unsplash.com/photo-1541807084-5c52b6b3adef?w=400"),
            ("Acer Predator Helios 16 Gaming (Core i9, RTX 4080)", "Acer", 239990, "https://images.unsplash.com/photo-1603302576837-37561b2e2302?w=400"),
            ("Acer Nitro V 15 (Core i5 13th Gen, RTX 4050)", "Acer", 72990, "https://images.unsplash.com/photo-1603302576837-37561b2e2302?w=400"),
            ("Acer Swift Go 14 OLED (Core i5 13th Gen, 16GB)", "Acer", 62990, "https://images.unsplash.com/photo-1541807084-5c52b6b3adef?w=400"),
            ("Acer Aspire 5 Thin & Light (Core i5 12th Gen)", "Acer", 48990, "https://images.unsplash.com/photo-1541807084-5c52b6b3adef?w=400"),
            ("MSI Katana 15 Gaming (Core i7 13th Gen, RTX 4060)", "MSI", 104990, "https://images.unsplash.com/photo-1603302576837-37561b2e2302?w=400"),
            ("MSI Cyborg 15 (Core i5 12th Gen, RTX 4050)", "MSI", 67990, "https://images.unsplash.com/photo-1603302576837-37561b2e2302?w=400"),
            ("MSI Stealth 14 Studio (Core i7 13th Gen, RTX 4060)", "MSI", 149990, "https://images.unsplash.com/photo-1603302576837-37561b2e2302?w=400"),
            ("Samsung Galaxy Book 4 Pro 360 (Core Ultra 7, AMOLED)", "Samsung", 179990, "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=400"),
            ("Samsung Galaxy Book 4 (Core i5 13th Gen, 16GB/512GB)", "Samsung", 74990, "https://images.unsplash.com/photo-1541807084-5c52b6b3adef?w=400"),
            ("LG Gram 16 Ultra-Lightweight (Intel Core Ultra 7, 1.1kg)", "LG", 154990, "https://images.unsplash.com/photo-1541807084-5c52b6b3adef?w=400"),
            ("LG Gram 14 (Core i7 13th Gen, 16GB/1TB SSD)", "LG", 119990, "https://images.unsplash.com/photo-1541807084-5c52b6b3adef?w=400"),
            ("Microsoft Surface Laptop 5 (Core i7, 16GB/512GB)", "Microsoft", 149999, "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=400"),
            ("Microsoft Surface Pro 9 2-in-1 Touch (Core i5, 8GB)", "Microsoft", 98999, "https://images.unsplash.com/photo-1541807084-5c52b6b3adef?w=400"),
            ("Xiaomi Notebook Pro 120G (Core i5 12th Gen)", "Xiaomi", 68999, "https://images.unsplash.com/photo-1541807084-5c52b6b3adef?w=400"),
            ("Infinix ZERO BOOK ULTRA (Core i9 13th Gen, 32GB)", "Infinix", 79990, "https://images.unsplash.com/photo-1541807084-5c52b6b3adef?w=400"),
            ("Razer Blade 15 Gaming Laptop (Core i7, RTX 4070)", "Razer", 249999, "https://images.unsplash.com/photo-1603302576837-37561b2e2302?w=400"),
            ("Gigabyte AORUS 15 Gaming (Core i7, RTX 4070)", "Gigabyte", 129990, "https://images.unsplash.com/photo-1603302576837-37561b2e2302?w=400"),
            ("Realme Book Slim (Core i3 11th Gen, 2K Display)", "Realme", 36990, "https://images.unsplash.com/photo-1541807084-5c52b6b3adef?w=400"),
            ("Honor MagicBook X16 (Core i5 12th Gen, 16GB)", "Honor", 44990, "https://images.unsplash.com/photo-1541807084-5c52b6b3adef?w=400"),
            ("Dell Vostro 3520 (Core i3 12th Gen, 8GB/512GB)", "Dell", 37990, "https://images.unsplash.com/photo-1541807084-5c52b6b3adef?w=400"),
            ("HP Chromebook 14 (MediaTek MT8183, 4GB/64GB)", "HP", 22990, "https://images.unsplash.com/photo-1541807084-5c52b6b3adef?w=400"),
            ("Lenovo Chromebook Duet 3 (Snapdragon 7c Gen 2)", "Lenovo", 26990, "https://images.unsplash.com/photo-1541807084-5c52b6b3adef?w=400"),
            ("ASUS Chromebook Flip CX5 (Core i5, 8GB/256GB)", "ASUS", 49990, "https://images.unsplash.com/photo-1541807084-5c52b6b3adef?w=400"),
            ("Acer Chromebook Spin 513 (Qualcomm Kryo 468)", "Acer", 31990, "https://images.unsplash.com/photo-1541807084-5c52b6b3adef?w=400")
        ],
        "Audio": [
            ("Sony WH-1000XM5 Wireless Noise-Cancelling Headphones", "Sony", 29990, "https://images.unsplash.com/photo-1546435770-a3e426bf472b?w=400"),
            ("Sony WH-1000XM4 Wireless Over-Ear Headphones", "Sony", 22990, "https://images.unsplash.com/photo-1546435770-a3e426bf472b?w=400"),
            ("Sony WF-1000XM5 True Wireless Noise Cancelling Earbuds", "Sony", 24990, "https://images.unsplash.com/photo-1600294037681-c80b4cb5b434?w=400"),
            ("Sony WH-CH720N Wireless Noise Canceling Headphones", "Sony", 9990, "https://images.unsplash.com/photo-1546435770-a3e426bf472b?w=400"),
            ("Sony HT-S20R 5.1ch Soundbar with Bluetooth (400W)", "Sony", 17990, "https://images.unsplash.com/photo-1545454675-3531b543be5d?w=400"),
            ("Apple AirPods Pro (2nd Generation, USB-C MagSafe)", "Apple", 24900, "https://images.unsplash.com/photo-1600294037681-c80b4cb5b434?w=400"),
            ("Apple AirPods Max Wireless Over-Ear Headphones", "Apple", 59900, "https://images.unsplash.com/photo-1546435770-a3e426bf472b?w=400"),
            ("Apple AirPods (3rd Generation with Lightning Case)", "Apple", 19900, "https://images.unsplash.com/photo-1600294037681-c80b4cb5b434?w=400"),
            ("Bose QuietComfort Ultra Noise Cancelling Headphones", "Bose", 35900, "https://images.unsplash.com/photo-1546435770-a3e426bf472b?w=400"),
            ("Bose QuietComfort 45 Bluetooth Headphones", "Bose", 26900, "https://images.unsplash.com/photo-1546435770-a3e426bf472b?w=400"),
            ("Bose QuietComfort Ultra True Wireless Earbuds", "Bose", 29900, "https://images.unsplash.com/photo-1600294037681-c80b4cb5b434?w=400"),
            ("Bose SoundLink Flex Bluetooth Portable Speaker", "Bose", 13900, "https://images.unsplash.com/photo-1545454675-3531b543be5d?w=400"),
            ("Sennheiser Momentum 4 Wireless ANC Headphones (60h)", "Sennheiser", 27990, "https://images.unsplash.com/photo-1546435770-a3e426bf472b?w=400"),
            ("Sennheiser Accentum Plus Wireless ANC Headphones", "Sennheiser", 15990, "https://images.unsplash.com/photo-1546435770-a3e426bf472b?w=400"),
            ("Sennheiser HD 450SE Bluetooth Wireless Headphones", "Sennheiser", 7990, "https://images.unsplash.com/photo-1546435770-a3e426bf472b?w=400"),
            ("JBL Tour One M2 Wireless Over-Ear Headphones", "JBL", 19999, "https://images.unsplash.com/photo-1546435770-a3e426bf472b?w=400"),
            ("JBL Live 660NC Wireless Over-Ear Headphones", "JBL", 9999, "https://images.unsplash.com/photo-1546435770-a3e426bf472b?w=400"),
            ("JBL Flip 6 Portable Waterproof Bluetooth Speaker", "JBL", 9999, "https://images.unsplash.com/photo-1545454675-3531b543be5d?w=400"),
            ("JBL Charge 5 Bluetooth Speaker with Powerbank", "JBL", 14999, "https://images.unsplash.com/photo-1545454675-3531b543be5d?w=400"),
            ("JBL Bar 500 5.1ch Dolby Atmos Soundbar (590W)", "JBL", 44999, "https://images.unsplash.com/photo-1545454675-3531b543be5d?w=400"),
            ("boAt Nirvana Ion ANC True Wireless Earbuds (120h)", "boAt", 2499, "https://images.unsplash.com/photo-1600294037681-c80b4cb5b434?w=400"),
            ("boAt Rockerz 550 Over-Ear Wireless Headphones", "boAt", 1799, "https://images.unsplash.com/photo-1546435770-a3e426bf472b?w=400"),
            ("boAt Airdopes 141 True Wireless Earbuds (42h Playtime)", "boAt", 1299, "https://images.unsplash.com/photo-1600294037681-c80b4cb5b434?w=400"),
            ("boAt Stone 1200 14W Portable Bluetooth Speaker", "boAt", 3999, "https://images.unsplash.com/photo-1545454675-3531b543be5d?w=400"),
            ("Marshall Major IV Wireless Bluetooth Headphones (80h)", "Marshall", 12999, "https://images.unsplash.com/photo-1546435770-a3e426bf472b?w=400"),
            ("Marshall Stanmore III Home Bluetooth Speaker", "Marshall", 39999, "https://images.unsplash.com/photo-1545454675-3531b543be5d?w=400"),
            ("Marshall Emberton II Portable Waterproof Speaker", "Marshall", 17999, "https://images.unsplash.com/photo-1545454675-3531b543be5d?w=400"),
            ("OnePlus Buds Pro 2 Wireless Earbuds (Dynaudio)", "OnePlus", 9999, "https://images.unsplash.com/photo-1600294037681-c80b4cb5b434?w=400"),
            ("OnePlus Buds 3 Wireless Earbuds (44dB ANC)", "OnePlus", 5499, "https://images.unsplash.com/photo-1600294037681-c80b4cb5b434?w=400"),
            ("Realme Buds Air 5 Pro ANC Earbuds (50dB ANC, LDAC)", "Realme", 4999, "https://images.unsplash.com/photo-1600294037681-c80b4cb5b434?w=400"),
            ("Samsung Galaxy Buds 2 Pro Wireless ANC Earbuds", "Samsung", 14999, "https://images.unsplash.com/photo-1600294037681-c80b4cb5b434?w=400"),
            ("Samsung Galaxy Buds FE Wireless Earbuds", "Samsung", 7999, "https://images.unsplash.com/photo-1600294037681-c80b4cb5b434?w=400"),
            ("Nothing Ear (2) True Wireless Hi-Res Earbuds", "Nothing", 9999, "https://images.unsplash.com/photo-1600294037681-c80b4cb5b434?w=400"),
            ("Nothing Ear (a) Wireless ANC Earbuds", "Nothing", 6999, "https://images.unsplash.com/photo-1600294037681-c80b4cb5b434?w=400"),
            ("Skullcandy Crusher Evo Sensory Bass Headphones", "Skullcandy", 14999, "https://images.unsplash.com/photo-1546435770-a3e426bf472b?w=400"),
            ("Skullcandy Rail ANC True Wireless Earbuds", "Skullcandy", 7999, "https://images.unsplash.com/photo-1600294037681-c80b4cb5b434?w=400"),
            ("Audio-Technica ATH-M50x Professional Studio Headphones", "Audio-Technica", 13990, "https://images.unsplash.com/photo-1546435770-a3e426bf472b?w=400"),
            ("Audio-Technica ATH-M20x Professional Studio Headphones", "Audio-Technica", 4990, "https://images.unsplash.com/photo-1546435770-a3e426bf472b?w=400"),
            ("Beyerdynamic DT 770 PRO 80 Ohm Studio Headphones", "Beyerdynamic", 13999, "https://images.unsplash.com/photo-1546435770-a3e426bf472b?w=400"),
            ("Sonos Era 100 Smart Home Bluetooth Speaker", "Sonos", 29999, "https://images.unsplash.com/photo-1545454675-3531b543be5d?w=400"),
            ("Sonos Beam Gen 2 Compact Dolby Atmos Soundbar", "Sonos", 54999, "https://images.unsplash.com/photo-1545454675-3531b543be5d?w=400"),
            ("Harman Kardon Aura Studio 4 Bluetooth Speaker", "Harman Kardon", 27999, "https://images.unsplash.com/photo-1545454675-3531b543be5d?w=400"),
            ("Anker Soundcore Space One Active Noise Cancelling", "Anker", 9999, "https://images.unsplash.com/photo-1546435770-a3e426bf472b?w=400"),
            ("Anker Soundcore Motion+ 30W Bluetooth Speaker", "Anker", 7999, "https://images.unsplash.com/photo-1545454675-3531b543be5d?w=400"),
            ("Noise Buds VS102 True Wireless Earbuds (50h)", "Noise", 1199, "https://images.unsplash.com/photo-1600294037681-c80b4cb5b434?w=400"),
            ("Boult Audio Z40 True Wireless Earbuds (60h)", "Boult", 1399, "https://images.unsplash.com/photo-1600294037681-c80b4cb5b434?w=400"),
            ("Portronics SoundDrum P 20W Bluetooth Speaker", "Portronics", 1999, "https://images.unsplash.com/photo-1545454675-3531b543be5d?w=400"),
            ("Mivi Fort S60 Soundbar with Subwoofer (60W)", "Mivi", 3499, "https://images.unsplash.com/photo-1545454675-3531b543be5d?w=400"),
            ("Zebronics Juke Bar 9500 Pro 5.1ch Soundbar (525W)", "Zebronics", 13999, "https://images.unsplash.com/photo-1545454675-3531b543be5d?w=400"),
            ("Philips TAB8967 5.1.2ch Dolby Atmos Soundbar (780W)", "Philips", 34990, "https://images.unsplash.com/photo-1545454675-3531b543be5d?w=400")
        ],
        "Smartwatches": [
            ("Apple Watch Ultra 2 (GPS + Cellular, 49mm Titanium)", "Apple", 89900, "https://images.unsplash.com/photo-1508685096489-7aacd43bd3b1?w=400"),
            ("Apple Watch Series 9 (GPS + Cellular, 45mm Aluminum)", "Apple", 54900, "https://images.unsplash.com/photo-1508685096489-7aacd43bd3b1?w=400"),
            ("Apple Watch Series 9 (GPS, 41mm Midnight Aluminum)", "Apple", 41900, "https://images.unsplash.com/photo-1508685096489-7aacd43bd3b1?w=400"),
            ("Apple Watch SE 2nd Gen (GPS, 44mm Starlight)", "Apple", 29900, "https://images.unsplash.com/photo-1508685096489-7aacd43bd3b1?w=400"),
            ("Samsung Galaxy Watch 6 Classic (Bluetooth, 47mm)", "Samsung", 36999, "https://images.unsplash.com/photo-1579586337278-3befd40fd17a?w=400"),
            ("Samsung Galaxy Watch 6 (Bluetooth, 44mm Graphite)", "Samsung", 29999, "https://images.unsplash.com/photo-1579586337278-3befd40fd17a?w=400"),
            ("Samsung Galaxy Watch 5 Pro (GPS + LTE, 45mm)", "Samsung", 34999, "https://images.unsplash.com/photo-1579586337278-3befd40fd17a?w=400"),
            ("Samsung Galaxy Fit 3 Fitness Tracker (1.6 AMOLED)", "Samsung", 4999, "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=400"),
            ("Garmin Fenix 7 Pro Solar Multisport GPS Watch", "Garmin", 84990, "https://images.unsplash.com/photo-1508685096489-7aacd43bd3b1?w=400"),
            ("Garmin Forerunner 265 Running Smartwatch (AMOLED)", "Garmin", 48990, "https://images.unsplash.com/photo-1508685096489-7aacd43bd3b1?w=400"),
            ("Garmin Venu 3 GPS Smartwatch (14 Days Battery)", "Garmin", 47990, "https://images.unsplash.com/photo-1508685096489-7aacd43bd3b1?w=400"),
            ("Garmin Instinct 2X Solar Rugged GPS Watch", "Garmin", 44990, "https://images.unsplash.com/photo-1508685096489-7aacd43bd3b1?w=400"),
            ("Fitbit Sense 2 Health & Fitness Smartwatch", "Fitbit", 24999, "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=400"),
            ("Fitbit Versa 4 Fitness Smartwatch (6+ Days Battery)", "Fitbit", 18999, "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=400"),
            ("Fitbit Charge 6 Fitness Tracker with Google Apps", "Fitbit", 14999, "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=400"),
            ("OnePlus Watch 2 (Wear OS 4, Snapdragon W5, 100h)", "OnePlus", 24999, "https://images.unsplash.com/photo-1579586337278-3befd40fd17a?w=400"),
            ("Amazfit Cheetah Pro GPS Running Watch (Titanium)", "Amazfit", 29999, "https://images.unsplash.com/photo-1508685096489-7aacd43bd3b1?w=400"),
            ("Amazfit GTR 4 Smartwatch with Dual-Band GPS", "Amazfit", 16999, "https://images.unsplash.com/photo-1579586337278-3befd40fd17a?w=400"),
            ("Amazfit Active Edge Rugged Sport Smartwatch", "Amazfit", 12999, "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=400"),
            ("Amazfit Bip 5 Smartwatch with 1.91-inch Display", "Amazfit", 7499, "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=400"),
            ("Fossil Gen 6 Touchscreen Smartwatch (Stainless Steel)", "Fossil", 24995, "https://images.unsplash.com/photo-1579586337278-3befd40fd17a?w=400"),
            ("Noise ColorFit Pro 5 Max with 1.96-inch AMOLED", "Noise", 4999, "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=400"),
            ("Noise Halo Plus Elite Edition Metallic Calling Watch", "Noise", 3499, "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=400"),
            ("Noise Pulse 2 Max Bluetooth Calling Smartwatch", "Noise", 1499, "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=400"),
            ("Fire-Boltt Invincible Plus 1.43 AMOLED (4GB Storage)", "Fire-Boltt", 3999, "https://images.unsplash.com/photo-1579586337278-3befd40fd17a?w=400"),
            ("Fire-Boltt Gladiator 1.96 HD Bluetooth Calling", "Fire-Boltt", 1799, "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=400"),
            ("boAt Ultima Prism 1.96 AMOLED Smartwatch", "boAt", 2499, "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=400"),
            ("boAt Wave Call 2 Bluetooth Calling Smartwatch", "boAt", 1299, "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=400"),
            ("Titan Smart Pro GPS Smartwatch with AMOLED Display", "Titan", 9995, "https://images.unsplash.com/photo-1579586337278-3befd40fd17a?w=400"),
            ("Fastrack Limitless FS1 Pro 1.96 Super AMOLED", "Fastrack", 2995, "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=400"),
            ("Realme Watch S Pro 1.39 AMOLED GPS Smartwatch", "Realme", 7999, "https://images.unsplash.com/photo-1579586337278-3befd40fd17a?w=400"),
            ("Redmi Watch 4 with 1.97 AMOLED & 20 Days Battery", "Xiaomi", 7999, "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=400"),
            ("Redmi Watch 3 Active Bluetooth Calling Smartwatch", "Xiaomi", 2999, "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=400"),
            ("CMF by Nothing Watch Pro (1.96 AMOLED, Multi-GPS)", "Nothing", 4499, "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=400"),
            ("Suunto 9 Peak Pro GPS Multisport Watch", "Suunto", 49999, "https://images.unsplash.com/photo-1508685096489-7aacd43bd3b1?w=400"),
            ("Polar Pacer Pro Advanced GPS Running Watch", "Polar", 34999, "https://images.unsplash.com/photo-1508685096489-7aacd43bd3b1?w=400"),
            ("Casio G-Shock G-SQUAD GBD-H2000 GPS Watch", "Casio", 37995, "https://images.unsplash.com/photo-1508685096489-7aacd43bd3b1?w=400"),
            ("Withings ScanWatch 2 Hybrid Smartwatch (ECG/SpO2)", "Withings", 34999, "https://images.unsplash.com/photo-1579586337278-3befd40fd17a?w=400"),
            ("Crossbeats Nexus 2.01 Super AMOLED Smartwatch", "Crossbeats", 3999, "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=400"),
            ("Pebble Cosmos Prime 1.93 High-Res Display Watch", "Pebble", 2299, "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=400"),
            ("Dizo Watch D Pro with D1 Chip & AMOLED", "Dizo", 2499, "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=400"),
            ("Hammer Pulse X Bluetooth Calling Smart Watch", "Hammer", 1699, "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=400"),
            ("Timex Fit 2.0 Calling Smartwatch with Heart Rate", "Timex", 4995, "https://images.unsplash.com/photo-1579586337278-3befd40fd17a?w=400"),
            ("TAGG Verve Connect Ultra 1.78 AMOLED Display", "TAGG", 2799, "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=400"),
            ("Gizmore Cloud 1.9 IPS Curved Display Calling Watch", "Gizmore", 1399, "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=400"),
            ("Cultsport Beats 1.85 HD Calling Bluetooth Watch", "Cultsport", 1999, "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=400"),
            ("Ambrane Wise Eon Max 2.01 Bluetooth Calling", "Ambrane", 1599, "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=400"),
            ("French Connection Touchscreen Smartwatch Unisex", "French Connection", 3999, "https://images.unsplash.com/photo-1579586337278-3befd40fd17a?w=400"),
            ("Helix by Timex Smart 2.0 Health Tracker Watch", "Helix", 2495, "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=400"),
            ("Inbase Urban Pro X Bluetooth Calling Watch", "Inbase", 1799, "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=400")
        ],
        "Smart TVs & Home": [
            ("Sony Bravia 65-inch XR OLED 4K Google TV (A80L)", "Sony", 249990, "https://images.unsplash.com/photo-1593784991095-a205069470b6?w=400"),
            ("Sony Bravia 55-inch 4K Ultra HD Smart LED Google TV (X80L)", "Sony", 74990, "https://images.unsplash.com/photo-1593784991095-a205069470b6?w=400"),
            ("Sony Bravia 43-inch 4K HDR Google TV (X74L)", "Sony", 41990, "https://images.unsplash.com/photo-1593784991095-a205069470b6?w=400"),
            ("Samsung 65-inch Neo QLED 4K Smart TV (QN90C)", "Samsung", 194990, "https://images.unsplash.com/photo-1593784991095-a205069470b6?w=400"),
            ("Samsung 55-inch The Frame QLED 4K TV (Art Mode)", "Samsung", 84990, "https://images.unsplash.com/photo-1593359677879-a4bb92f829d1?w=400"),
            ("Samsung 55-inch Crystal 4K Vivid Pro Smart TV", "Samsung", 44990, "https://images.unsplash.com/photo-1593359677879-a4bb92f829d1?w=400"),
            ("Samsung 43-inch Crystal 4K iSmart Ultra HD TV", "Samsung", 28990, "https://images.unsplash.com/photo-1593359677879-a4bb92f829d1?w=400"),
            ("LG 55-inch OLED evo C3 4K Smart Cinema TV", "LG", 119990, "https://images.unsplash.com/photo-1593784991095-a205069470b6?w=400"),
            ("LG 65-inch OLED evo G3 Gallery Design 4K TV", "LG", 269990, "https://images.unsplash.com/photo-1593784991095-a205069470b6?w=400"),
            ("LG 50-inch 4K Ultra HD Smart LED TV (UR7500)", "LG", 41990, "https://images.unsplash.com/photo-1593359677879-a4bb92f829d1?w=400"),
            ("LG 43-inch 4K UHD Smart NanoCell TV (NANO77)", "LG", 37990, "https://images.unsplash.com/photo-1593359677879-a4bb92f829d1?w=400"),
            ("TCL 65-inch 4K Mini LED Google TV (C755)", "TCL", 89990, "https://images.unsplash.com/photo-1593784991095-a205069470b6?w=400"),
            ("TCL 55-inch 4K Ultra HD QLED Google TV (T6G)", "TCL", 38990, "https://images.unsplash.com/photo-1593359677879-a4bb92f829d1?w=400"),
            ("TCL 43-inch 4K Metallic Bezel-Less Google TV (V6B)", "TCL", 23990, "https://images.unsplash.com/photo-1593359677879-a4bb92f829d1?w=400"),
            ("Xiaomi Smart TV X 55-inch 4K Dolby Vision TV", "Xiaomi", 37999, "https://images.unsplash.com/photo-1593359677879-a4bb92f829d1?w=400"),
            ("Xiaomi Smart TV X 43-inch 4K Google TV", "Xiaomi", 26999, "https://images.unsplash.com/photo-1593359677879-a4bb92f829d1?w=400"),
            ("Xiaomi Smart TV A 32-inch HD Ready Smart Google TV", "Xiaomi", 11999, "https://images.unsplash.com/photo-1593359677879-a4bb92f829d1?w=400"),
            ("OnePlus TV 65 Q2 Pro 4K QLED Smart Google TV", "OnePlus", 99999, "https://images.unsplash.com/photo-1593784991095-a205069470b6?w=400"),
            ("OnePlus TV 50 Y1S Pro 4K Ultra HD Smart TV", "OnePlus", 32999, "https://images.unsplash.com/photo-1593359677879-a4bb92f829d1?w=400"),
            ("OnePlus TV 43 Y1S Edge Full HD Smart Android TV", "OnePlus", 22999, "https://images.unsplash.com/photo-1593359677879-a4bb92f829d1?w=400"),
            ("Hisense 55-inch 4K QLED Tornado 3.0 TV (102W Audio)", "Hisense", 39990, "https://images.unsplash.com/photo-1593359677879-a4bb92f829d1?w=400"),
            ("Hisense 65-inch Mini-LED 4K Google TV (U7K 144Hz)", "Hisense", 84990, "https://images.unsplash.com/photo-1593784991095-a205069470b6?w=400"),
            ("Vu 55-inch The Masterpiece Glo QLED 4K TV (800 Nits)", "Vu", 48999, "https://images.unsplash.com/photo-1593359677879-a4bb92f829d1?w=400"),
            ("Vu 43-inch The GloLED 4K Smart Google TV", "Vu", 26999, "https://images.unsplash.com/photo-1593359677879-a4bb92f829d1?w=400"),
            ("Toshiba 55-inch 4K Ultra HD Smart QLED TV (M550MP)", "Toshiba", 41990, "https://images.unsplash.com/photo-1593359677879-a4bb92f829d1?w=400"),
            ("Acer 55-inch Advanced I Series 4K Google TV", "Acer", 31999, "https://images.unsplash.com/photo-1593359677879-a4bb92f829d1?w=400"),
            ("Acer 43-inch V Series 4K Ultra HD Smart QLED TV", "Acer", 24999, "https://images.unsplash.com/photo-1593359677879-a4bb92f829d1?w=400"),
            ("Panasonic 55-inch 4K Ultra HD Smart LED Google TV", "Panasonic", 44990, "https://images.unsplash.com/photo-1593359677879-a4bb92f829d1?w=400"),
            ("Panasonic 43-inch 4K HDR Google TV (TH-43MX660DX)", "Panasonic", 32990, "https://images.unsplash.com/photo-1593359677879-a4bb92f829d1?w=400"),
            ("Philips 55-inch 4K UHD LED Smart Google TV", "Philips", 39990, "https://images.unsplash.com/photo-1593359677879-a4bb92f829d1?w=400"),
            ("Kodak 55-inch 4K Ultra HD Smart QLED Google TV", "Kodak", 29999, "https://images.unsplash.com/photo-1593359677879-a4bb92f829d1?w=400"),
            ("Thomson 50-inch 4K Smart Google TV with Dolby Atmos", "Thomson", 25999, "https://images.unsplash.com/photo-1593359677879-a4bb92f829d1?w=400"),
            ("Motorola EnvisionX 55-inch 4K QLED Google TV", "Motorola", 34999, "https://images.unsplash.com/photo-1593359677879-a4bb92f829d1?w=400"),
            ("iFFALCON 55-inch 4K Ultra HD Smart Google TV", "iFFALCON", 27999, "https://images.unsplash.com/photo-1593359677879-a4bb92f829d1?w=400"),
            ("Blaupunkt 55-inch 4K QLED Ultra HD Smart Google TV", "Blaupunkt", 34999, "https://images.unsplash.com/photo-1593359677879-a4bb92f829d1?w=400"),
            ("Sansui 55-inch 4K Ultra HD Smart Google TV", "Sansui", 28990, "https://images.unsplash.com/photo-1593359677879-a4bb92f829d1?w=400"),
            ("Coocaa 55-inch 4K Ultra HD Smart Google TV", "Coocaa", 25999, "https://images.unsplash.com/photo-1593359677879-a4bb92f829d1?w=400"),
            ("Dyson V15 Detect Extra Cordless Vacuum Cleaner", "Dyson", 65900, "https://images.unsplash.com/photo-1526170375885-4d8ecf77b99f?w=400"),
            ("Dyson Purifier Hot+Cool Air Purifier HP07", "Dyson", 56900, "https://images.unsplash.com/photo-1526170375885-4d8ecf77b99f?w=400"),
            ("Philips Air Fryer HD9252/90 4.1L Touch Screen", "Philips", 8999, "https://images.unsplash.com/photo-1526170375885-4d8ecf77b99f?w=400"),
            ("Instant Pot Duo 7-in-1 Electric Pressure Cooker 6L", "Instant Pot", 8999, "https://images.unsplash.com/photo-1526170375885-4d8ecf77b99f?w=400"),
            ("Eureka Forbes Aquaguard Ritz RO+UV Water Purifier", "Eureka Forbes", 15999, "https://images.unsplash.com/photo-1526170375885-4d8ecf77b99f?w=400"),
            ("Kent Grand Plus RO+UV+UF+TDS Water Purifier 9L", "Kent", 16999, "https://images.unsplash.com/photo-1526170375885-4d8ecf77b99f?w=400"),
            ("ECOVACS DEEBOT N8 Robotic Vacuum & Mop Cleaner", "ECOVACS", 24900, "https://images.unsplash.com/photo-1526170375885-4d8ecf77b99f?w=400"),
            ("Xiaomi Smart Air Purifier 4 (OLED Display, True HEPA)", "Xiaomi", 13999, "https://images.unsplash.com/photo-1526170375885-4d8ecf77b99f?w=400"),
            ("Morphy Richards Digital Microwave Oven 24L", "Morphy Richards", 9499, "https://images.unsplash.com/photo-1526170375885-4d8ecf77b99f?w=400"),
            ("Havells Meditate Air Purifier with SpaceTech UV", "Havells", 21990, "https://images.unsplash.com/photo-1526170375885-4d8ecf77b99f?w=400"),
            ("Panasonic 27L Convection Microwave Oven (NN-CT645BFDG)", "Panasonic", 12990, "https://images.unsplash.com/photo-1526170375885-4d8ecf77b99f?w=400"),
            ("Bajaj Rex 500W Mixer Grinder with 3 Jars", "Bajaj", 2199, "https://images.unsplash.com/photo-1526170375885-4d8ecf77b99f?w=400"),
            ("Prestige Iris Plus 750W Mixer Grinder with 4 Jars", "Prestige", 3199, "https://images.unsplash.com/photo-1526170375885-4d8ecf77b99f?w=400")
        ],
        "Gaming Consoles & Gear": [
            ("Sony PlayStation 5 Slim Disc Edition (1TB SSD)", "Sony", 54990, "https://images.unsplash.com/photo-1606813907291-d86efa9b94db?w=400"),
            ("Sony PlayStation 5 Digital Edition (1TB SSD)", "Sony", 44990, "https://images.unsplash.com/photo-1606813907291-d86efa9b94db?w=400"),
            ("Sony PlayStation VR2 Headset for PS5", "Sony", 57990, "https://images.unsplash.com/photo-1621259182978-fbf93132d53d?w=400"),
            ("Sony DualSense Wireless Controller for PS5 (White)", "Sony", 5890, "https://images.unsplash.com/photo-1606813907291-d86efa9b94db?w=400"),
            ("Sony Pulse 3D Wireless Headset for PS5", "Sony", 8590, "https://images.unsplash.com/photo-1621259182978-fbf93132d53d?w=400"),
            ("Microsoft Xbox Series X 1TB Console (4K 120fps)", "Microsoft", 55990, "https://images.unsplash.com/photo-1606813907291-d86efa9b94db?w=400"),
            ("Microsoft Xbox Series S 512GB All-Digital Console", "Microsoft", 34990, "https://images.unsplash.com/photo-1606813907291-d86efa9b94db?w=400"),
            ("Microsoft Xbox Wireless Controller (Carbon Black)", "Microsoft", 5390, "https://images.unsplash.com/photo-1606813907291-d86efa9b94db?w=400"),
            ("Microsoft Xbox Elite Series 2 Wireless Controller", "Microsoft", 15990, "https://images.unsplash.com/photo-1606813907291-d86efa9b94db?w=400"),
            ("Nintendo Switch OLED Model (Neon Red & Neon Blue)", "Nintendo", 31999, "https://images.unsplash.com/photo-1606813907291-d86efa9b94db?w=400"),
            ("Nintendo Switch Lite Handheld Console (Turquoise)", "Nintendo", 18999, "https://images.unsplash.com/photo-1606813907291-d86efa9b94db?w=400"),
            ("Nintendo Switch Pro Wireless Controller", "Nintendo", 5999, "https://images.unsplash.com/photo-1606813907291-d86efa9b94db?w=400"),
            ("Valve Steam Deck OLED Handheld Gaming PC (512GB)", "Valve", 59999, "https://images.unsplash.com/photo-1606813907291-d86efa9b94db?w=400"),
            ("ASUS ROG Ally Z1 Extreme Handheld Gaming Console", "ASUS", 59990, "https://images.unsplash.com/photo-1606813907291-d86efa9b94db?w=400"),
            ("Lenovo Legion Go Handheld Gaming Console (AMD Z1 Extreme)", "Lenovo", 74990, "https://images.unsplash.com/photo-1606813907291-d86efa9b94db?w=400"),
            ("Razer DeathAdder V3 Pro Wireless Gaming Mouse", "Razer", 12999, "https://images.unsplash.com/photo-1615663245857-ac93bb7c39e7?w=400"),
            ("Razer BlackWidow V4 Pro Mechanical Gaming Keyboard", "Razer", 19999, "https://images.unsplash.com/photo-1609592424074-1b156b823e25?w=400"),
            ("Razer BlackShark V2 Pro Wireless Gaming Headset", "Razer", 16999, "https://images.unsplash.com/photo-1621259182978-fbf93132d53d?w=400"),
            ("Razer Huntsman Mini 60% Optical Gaming Keyboard", "Razer", 9999, "https://images.unsplash.com/photo-1609592424074-1b156b823e25?w=400"),
            ("Logitech G502 X PLUS Wireless RGB Gaming Mouse", "Logitech G", 13995, "https://images.unsplash.com/photo-1615663245857-ac93bb7c39e7?w=400"),
            ("Logitech G Pro X Superlight 2 Wireless Mouse (60g)", "Logitech G", 14995, "https://images.unsplash.com/photo-1615663245857-ac93bb7c39e7?w=400"),
            ("Logitech G915 LIGHTSPEED Wireless Mechanical Keyboard", "Logitech G", 19995, "https://images.unsplash.com/photo-1609592424074-1b156b823e25?w=400"),
            ("Logitech G733 LIGHTSPEED Wireless RGB Headset", "Logitech G", 12995, "https://images.unsplash.com/photo-1621259182978-fbf93132d53d?w=400"),
            ("Corsair K70 RGB PRO Mechanical Gaming Keyboard", "Corsair", 14499, "https://images.unsplash.com/photo-1609592424074-1b156b823e25?w=400"),
            ("Corsair HS80 RGB Wireless Gaming Headset with Spatial Audio", "Corsair", 12999, "https://images.unsplash.com/photo-1621259182978-fbf93132d53d?w=400"),
            ("Corsair Scimitar RGB Elite Optical MOBA/MMO Mouse", "Corsair", 6999, "https://images.unsplash.com/photo-1615663245857-ac93bb7c39e7?w=400"),
            ("SteelSeries Arctis Nova Pro Wireless Multi-System Headset", "SteelSeries", 34999, "https://images.unsplash.com/photo-1621259182978-fbf93132d53d?w=400"),
            ("SteelSeries Apex Pro TKL Mechanical Gaming Keyboard", "SteelSeries", 18999, "https://images.unsplash.com/photo-1609592424074-1b156b823e25?w=400"),
            ("SteelSeries Aerox 3 Wireless Ultra-Light Gaming Mouse", "SteelSeries", 7999, "https://images.unsplash.com/photo-1615663245857-ac93bb7c39e7?w=400"),
            ("HyperX Cloud III Wireless Gaming Headset (120h Battery)", "HyperX", 13990, "https://images.unsplash.com/photo-1621259182978-fbf93132d53d?w=400"),
            ("HyperX Alloy Origins Core Tenkeyless Mechanical Keyboard", "HyperX", 7990, "https://images.unsplash.com/photo-1609592424074-1b156b823e25?w=400"),
            ("HyperX Pulsefire Haste 2 Wireless Gaming Mouse", "HyperX", 6990, "https://images.unsplash.com/photo-1615663245857-ac93bb7c39e7?w=400"),
            ("Elgato Stream Deck MK.2 with 15 LCD Keys", "Elgato", 14499, "https://images.unsplash.com/photo-1606813907291-d86efa9b94db?w=400"),
            ("Elgato Wave:3 Premium USB Condenser Microphone", "Elgato", 14999, "https://images.unsplash.com/photo-1621259182978-fbf93132d53d?w=400"),
            ("Elgato HD60 X External Capture Card 4K30 HDR10", "Elgato", 17999, "https://images.unsplash.com/photo-1606813907291-d86efa9b94db?w=400"),
            ("Blue Yeti USB Microphone for Streaming & Podcasting", "Logitech", 10995, "https://images.unsplash.com/photo-1621259182978-fbf93132d53d?w=400"),
            ("Logitech G29 Driving Force Racing Wheel & Pedals", "Logitech G", 28995, "https://images.unsplash.com/photo-1606813907291-d86efa9b94db?w=400"),
            ("Thrustmaster T300 RS GT Edition Racing Wheel", "Thrustmaster", 42999, "https://images.unsplash.com/photo-1606813907291-d86efa9b94db?w=400"),
            ("Secretlab TITAN Evo 2022 Ergonomic Gaming Chair", "Secretlab", 49999, "https://images.unsplash.com/photo-1606813907291-d86efa9b94db?w=400"),
            ("Green Soul Monster Ultimate Ergonomic Gaming Chair", "Green Soul", 17990, "https://images.unsplash.com/photo-1606813907291-d86efa9b94db?w=400"),
            ("Razer Kiyo Pro Streaming Webcam (1080p 60fps HDR)", "Razer", 9999, "https://images.unsplash.com/photo-1615663245857-ac93bb7c39e7?w=400"),
            ("Seagate Storage Expansion Card for Xbox Series X/S 1TB", "Seagate", 18999, "https://images.unsplash.com/photo-1606813907291-d86efa9b94db?w=400"),
            ("WD_BLACK SN850X 2TB NVMe SSD with Heatsink for PS5", "Western Digital", 16999, "https://images.unsplash.com/photo-1609592424074-1b156b823e25?w=400"),
            ("Redragon K552 Kumara RGB Mechanical Gaming Keyboard", "Redragon", 2799, "https://images.unsplash.com/photo-1609592424074-1b156b823e25?w=400"),
            ("Cosmic Byte CB-GK-16 Firefly TKL Mechanical Keyboard", "Cosmic Byte", 2199, "https://images.unsplash.com/photo-1609592424074-1b156b823e25?w=400"),
            ("Ant Esports GM320 RGB Optical Gaming Mouse", "Ant Esports", 699, "https://images.unsplash.com/photo-1615663245857-ac93bb7c39e7?w=400"),
            ("Razer Goliathus Chroma Extended RGB Gaming Mouse Pad", "Razer", 4499, "https://images.unsplash.com/photo-1615663245857-ac93bb7c39e7?w=400"),
            ("SteelSeries QcK Heavy XXL Gaming Mouse Pad (Thickness 6mm)", "SteelSeries", 3299, "https://images.unsplash.com/photo-1615663245857-ac93bb7c39e7?w=400"),
            ("BenQ ZOWIE CAMADE II Esports Cable Management Bungee", "BenQ", 2490, "https://images.unsplash.com/photo-1606813907291-d86efa9b94db?w=400"),
            ("Meta Quest 3 128GB All-In-One VR Headset", "Meta", 49999, "https://images.unsplash.com/photo-1621259182978-fbf93132d53d?w=400")
        ],
        "Cameras & Drones": [
            ("Sony Alpha 7 IV Full-Frame Mirrorless Camera (Body)", "Sony", 214990, "https://images.unsplash.com/photo-1516035069371-29a1b244cc32?w=400"),
            ("Sony Alpha 7C II Compact Full-Frame Mirrorless (Body)", "Sony", 194990, "https://images.unsplash.com/photo-1516035069371-29a1b244cc32?w=400"),
            ("Sony Alpha 6700 APS-C Mirrorless Camera with 18-135mm", "Sony", 149990, "https://images.unsplash.com/photo-1516035069371-29a1b244cc32?w=400"),
            ("Sony ZV-E10 Mirrorless Interchangeable Lens Vlog Camera", "Sony", 61490, "https://images.unsplash.com/photo-1516035069371-29a1b244cc32?w=400"),
            ("Sony FE 24-70mm f/2.8 GM II G Master Standard Zoom Lens", "Sony", 189990, "https://images.unsplash.com/photo-1516035069371-29a1b244cc32?w=400"),
            ("Canon EOS R6 Mark II Mirrorless Camera (Body)", "Canon", 215995, "https://images.unsplash.com/photo-1516035069371-29a1b244cc32?w=400"),
            ("Canon EOS R8 Full-Frame Mirrorless Camera with 24-50mm", "Canon", 132995, "https://images.unsplash.com/photo-1516035069371-29a1b244cc32?w=400"),
            ("Canon EOS R50 Content Creator Kit with 18-45mm", "Canon", 64995, "https://images.unsplash.com/photo-1516035069371-29a1b244cc32?w=400"),
            ("Canon RF 24-105mm f/4L IS USM Professional Lens", "Canon", 109995, "https://images.unsplash.com/photo-1516035069371-29a1b244cc32?w=400"),
            ("Canon EOS 1500D DSLR Camera with 18-55mm Lens", "Canon", 41990, "https://images.unsplash.com/photo-1516035069371-29a1b244cc32?w=400"),
            ("Nikon Z6 III Full-Frame Mirrorless Camera (Body)", "Nikon", 247990, "https://images.unsplash.com/photo-1516035069371-29a1b244cc32?w=400"),
            ("Nikon Zf Retro Mirrorless Full-Frame Camera (Body)", "Nikon", 179990, "https://images.unsplash.com/photo-1516035069371-29a1b244cc32?w=400"),
            ("Nikon Z50 Mirrorless Camera with 16-50mm VR Lens", "Nikon", 72990, "https://images.unsplash.com/photo-1516035069371-29a1b244cc32?w=400"),
            ("Nikon D7500 DSLR Camera with 18-140mm VR Lens", "Nikon", 87990, "https://images.unsplash.com/photo-1516035069371-29a1b244cc32?w=400"),
            ("DJI Mini 4 Pro Fly More Combo with RC 2 Controller", "DJI", 109990, "https://images.unsplash.com/photo-1507679799987-c73779587ccf?w=400"),
            ("DJI Air 3 Drone with Dual Primary Cameras & RC 2", "DJI", 149990, "https://images.unsplash.com/photo-1507679799987-c73779587ccf?w=400"),
            ("DJI Osmo Pocket 3 Creator Combo Handheld Gimbal Camera", "DJI", 63990, "https://images.unsplash.com/photo-1507679799987-c73779587ccf?w=400"),
            ("DJI Osmo Action 4 Standard Combo Waterproof Camera", "DJI", 31990, "https://images.unsplash.com/photo-1507679799987-c73779587ccf?w=400"),
            ("DJI RS 3 Mini 3-Axis Gimbal Stabilizer for Mirrorless", "DJI", 26990, "https://images.unsplash.com/photo-1507679799987-c73779587ccf?w=400"),
            ("GoPro HERO12 Black Action Camera with HDR 5.3K Video", "GoPro", 37990, "https://images.unsplash.com/photo-1516035069371-29a1b244cc32?w=400"),
            ("GoPro HERO11 Black Mini Waterproof Action Camera", "GoPro", 27990, "https://images.unsplash.com/photo-1516035069371-29a1b244cc32?w=400"),
            ("GoPro Max 360 Waterproof Action Camera (5.6K)", "GoPro", 44990, "https://images.unsplash.com/photo-1516035069371-29a1b244cc32?w=400"),
            ("Fujifilm X-T5 Mirrorless Digital Camera (Body, 40MP)", "Fujifilm", 169999, "https://images.unsplash.com/photo-1516035069371-29a1b244cc32?w=400"),
            ("Fujifilm X-S20 Mirrorless Camera with 15-45mm Lens", "Fujifilm", 124999, "https://images.unsplash.com/photo-1516035069371-29a1b244cc32?w=400"),
            ("Fujifilm Instax Mini 12 Instant Camera (Pastel Blue)", "Fujifilm", 6499, "https://images.unsplash.com/photo-1516035069371-29a1b244cc32?w=400"),
            ("Fujifilm Instax Mini Evo Hybrid Instant Camera", "Fujifilm", 18999, "https://images.unsplash.com/photo-1516035069371-29a1b244cc32?w=400"),
            ("Panasonic Lumix S5 II Full-Frame Mirrorless (20-60mm)", "Panasonic", 184990, "https://images.unsplash.com/photo-1516035069371-29a1b244cc32?w=400"),
            ("Panasonic Lumix G7 4K Digital Mirrorless Camera", "Panasonic", 42490, "https://images.unsplash.com/photo-1516035069371-29a1b244cc32?w=400"),
            ("Insta360 X4 8K 360-Degree Action Camera", "Insta360", 54990, "https://images.unsplash.com/photo-1516035069371-29a1b244cc32?w=400"),
            ("Insta360 Ace Pro 4K120fps Co-Engineered with Leica", "Insta360", 41990, "https://images.unsplash.com/photo-1516035069371-29a1b244cc32?w=400"),
            ("Insta360 GO 3 Tiny Action Cam (64GB, 35g)", "Insta360", 38990, "https://images.unsplash.com/photo-1516035069371-29a1b244cc32?w=400"),
            ("Sigma 24-70mm f/2.8 DG DN Art Lens for Sony E-Mount", "Sigma", 94990, "https://images.unsplash.com/photo-1516035069371-29a1b244cc32?w=400"),
            ("Sigma 16mm f/1.4 DC DN Contemporary Lens", "Sigma", 34990, "https://images.unsplash.com/photo-1516035069371-29a1b244cc32?w=400"),
            ("Tamron 28-75mm f/2.8 Di III VXD G2 Lens for Sony E", "Tamron", 74990, "https://images.unsplash.com/photo-1516035069371-29a1b244cc32?w=400"),
            ("Zhiyun Weebill 3S Handheld Gimbal Stabilizer", "Zhiyun", 29990, "https://images.unsplash.com/photo-1507679799987-c73779587ccf?w=400"),
            ("Zhiyun Smooth 5S Smartphone Gimbal Stabilizer", "Zhiyun", 14990, "https://images.unsplash.com/photo-1507679799987-c73779587ccf?w=400"),
            ("Rode Wireless PRO Dual-Channel Wireless Microphone", "Rode", 39900, "https://images.unsplash.com/photo-1516035069371-29a1b244cc32?w=400"),
            ("Rode VideoMic GO II Lightweight Directional Mic", "Rode", 8900, "https://images.unsplash.com/photo-1516035069371-29a1b244cc32?w=400"),
            ("DJI Mic 2 Wireless Microphone (2 Transmitters + Receiver)", "DJI", 34990, "https://images.unsplash.com/photo-1507679799987-c73779587ccf?w=400"),
            ("Godox SL-60W 60W Continuous LED Studio Video Light", "Godox", 9999, "https://images.unsplash.com/photo-1516035069371-29a1b244cc32?w=400"),
            ("Godox V1 Round Head Camera Flash Speedlite for Sony", "Godox", 18990, "https://images.unsplash.com/photo-1516035069371-29a1b244cc32?w=400"),
            ("Manfrotto Befree Advanced Carbon Fiber Travel Tripod", "Manfrotto", 24900, "https://images.unsplash.com/photo-1516035069371-29a1b244cc32?w=400"),
            ("Digitek DTR 550LW Heavy Duty Aluminium Tripod (67 inch)", "Digitek", 1899, "https://images.unsplash.com/photo-1516035069371-29a1b244cc32?w=400"),
            ("Peak Design Everyday Backpack 20L V2 (Black)", "Peak Design", 26999, "https://images.unsplash.com/photo-1516035069371-29a1b244cc32?w=400"),
            ("Lowepro ProTactic BP 450 AW II Professional Backpack", "Lowepro", 21990, "https://images.unsplash.com/photo-1516035069371-29a1b244cc32?w=400"),
            ("SanDisk 128GB Extreme PRO SDXC UHS-I Card (200MB/s)", "SanDisk", 2499, "https://images.unsplash.com/photo-1516035069371-29a1b244cc32?w=400"),
            ("Lexar Professional 2000x 128GB SDXC UHS-II Card", "Lexar", 9999, "https://images.unsplash.com/photo-1516035069371-29a1b244cc32?w=400"),
            ("Atomos Ninja V 5-inch 4K HDMI HDR Recording Monitor", "Atomos", 44990, "https://images.unsplash.com/photo-1516035069371-29a1b244cc32?w=400"),
            ("SmallRig Black Mamba Camera Cage for Canon R6 Mark II", "SmallRig", 9990, "https://images.unsplash.com/photo-1516035069371-29a1b244cc32?w=400"),
            ("PolarPro Variable ND 2-5 Stop Filter (Peter McKinnon)", "PolarPro", 22990, "https://images.unsplash.com/photo-1516035069371-29a1b244cc32?w=400")
        ],
        "Monitors & Displays": [
            ("LG UltraGear 27-inch OLED QHD 240Hz 0.03ms Gaming Monitor (27GR95QE)", "LG", 79999, "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=400"),
            ("LG UltraGear 32-inch QHD 165Hz HDR10 Gaming Monitor", "LG", 24999, "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=400"),
            ("LG UltraWide 34-inch Curved WQHD IPS Monitor (34WN780 Ergo)", "LG", 46999, "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=400"),
            ("LG 27-inch 4K UHD IPS Display with USB Type-C (27UP850)", "LG", 33999, "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=400"),
            ("Samsung Odyssey OLED G9 49-inch Curved Dual QHD 240Hz", "Samsung", 139999, "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=400"),
            ("Samsung Odyssey G7 32-inch 1000R Curved 240Hz QHD Monitor", "Samsung", 48999, "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=400"),
            ("Samsung ViewFinity S9 27-inch 5K Studio Display with 4K Camera", "Samsung", 99999, "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=400"),
            ("Samsung Smart Monitor M8 32-inch 4K UHD with SlimFit Cam", "Samsung", 42999, "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=400"),
            ("Dell UltraSharp 27-inch 4K USB-C Hub Monitor (U2723QE IPS Black)", "Dell", 59990, "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=400"),
            ("Dell Alienware 34-inch Curved QD-OLED Gaming Monitor (AW3423DWF)", "Dell", 89990, "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=400"),
            ("Dell S2721DGF 27-inch Gaming Monitor QHD 165Hz IPS", "Dell", 27990, "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=400"),
            ("Dell 24-inch FHD IPS Monitor with ComfortView (S2421HN)", "Dell", 11990, "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=400"),
            ("BenQ ZOWIE XL2546K 24.5-inch 240Hz DyAc+ Esports Gaming Monitor", "BenQ", 39990, "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=400"),
            ("BenQ PD2705U 27-inch 4K UHD Designer Color-Accurate Monitor", "BenQ", 47990, "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=400"),
            ("BenQ MOBIUZ EX2710Q 27-inch QHD 165Hz IPS Gaming Monitor", "BenQ", 28990, "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=400"),
            ("BenQ GW2780 27-inch 1080p Eye-Care IPS Monitor", "BenQ", 12490, "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=400"),
            ("ASUS ROG Swift OLED 27-inch 240Hz 0.03ms Monitor (PG27AQDM)", "ASUS", 89990, "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=400"),
            ("ASUS TUF Gaming VG27AQ 27-inch 2K HDR 165Hz G-SYNC", "ASUS", 26990, "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=400"),
            ("ASUS ProArt Display PA278CV 27-inch 100% sRGB Color Accurate", "ASUS", 32990, "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=400"),
            ("Acer Predator XB283K 28-inch 4K UHD 144Hz Gaming Monitor", "Acer", 54990, "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=400"),
            ("Acer Nitro VG270 S 27-inch Full HD IPS 165Hz 0.5ms", "Acer", 14990, "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=400"),
            ("ViewSonic ColorPro VP2768a 27-inch QHD 100% sRGB Pantone", "ViewSonic", 34990, "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=400"),
            ("ViewSonic VX2758A-2K-PRO 27-inch QHD 170Hz Gaming Monitor", "ViewSonic", 19990, "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=400"),
            ("MSI MAG 274UPF 27-inch 4K UHD Rapid IPS 144Hz 1ms", "MSI", 44990, "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=400"),
            ("MSI Optix G241 23.8-inch IPS 144Hz 1ms Gaming Monitor", "MSI", 13990, "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=400"),
            ("Gigabyte M27Q 27-inch 170Hz 1440P KVM Gaming Monitor", "Gigabyte", 26990, "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=400"),
            ("Gigabyte AORUS FO48U 48-inch 4K 120Hz OLED Gaming Display", "Gigabyte", 99990, "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=400"),
            ("AOC 24G2 23.8-inch Frameless Gaming IPS 144Hz 1ms", "AOC", 12990, "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=400"),
            ("AOC Agon Pro AG274QZM 27-inch Mini-LED 240Hz Gaming", "AOC", 74990, "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=400"),
            ("Lenovo Legion Y27q-30 27-inch QHD 180Hz Gaming Monitor", "Lenovo", 24990, "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=400"),
            ("Lenovo L24i-40 23.8-inch FHD IPS Ultra-Slim Monitor", "Lenovo", 8990, "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=400"),
            ("HP OMEN 27k 27-inch 4K 144Hz Gaming Monitor with KVM", "HP", 46990, "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=400"),
            ("HP M27f 27-inch FHD IPS Ultra-Slim Micro-Edge Monitor", "HP", 14490, "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=400"),
            ("Xiaomi Mi Curved Gaming Monitor 34-inch 144Hz WQHD", "Xiaomi", 29999, "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=400"),
            ("Xiaomi Desktop Monitor 27-inch Full HD 75Hz", "Xiaomi", 11999, "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=400"),
            ("Philips Momentum 279M1RV 27-inch 4K 144Hz Designed for Xbox", "Philips", 64990, "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=400"),
            ("Zebronics AC32FHD 32-inch Curved 165Hz Gaming Monitor", "Zebronics", 16999, "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=400"),
            ("BenQ ScreenBar Halo LED Monitor Light with Wireless Controller", "BenQ", 15990, "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=400"),
            ("Ergotron LX Desk Mount Single Monitor Arm (Polished Aluminum)", "Ergotron", 17990, "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=400"),
            ("AmazonBasics Heavy-Duty Single Monitor Display Mounting Arm", "AmazonBasics", 2999, "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=400"),
            ("LG 22MP68VQ 22-inch Full HD IPS Monitor with AMD FreeSync", "LG", 7999, "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=400"),
            ("Samsung 24-inch FHD Flat Monitor with Bezel-Less Design", "Samsung", 8499, "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=400"),
            ("Acer EK220Q 21.5-inch Full HD VA Eye Care Monitor", "Acer", 6299, "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=400"),
            ("ViewSonic VA2432-H 24-inch IPS 100Hz Frameless Monitor", "ViewSonic", 8299, "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=400"),
            ("ASUS Eye Care VY249HE 23.8-inch FHD IPS 75Hz Monitor", "ASUS", 8990, "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=400"),
            ("Dell SE2422H 24-inch FHD Monitor with 75Hz AMD FreeSync", "Dell", 8790, "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=400"),
            ("Lenovo D24-40 23.8-inch Full HD 75Hz Refresh Monitor", "Lenovo", 7490, "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=400"),
            ("BenQ GW2480 24-inch Eye-Care FHD IPS Monitor with B.I. Tech", "BenQ", 8990, "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=400"),
            ("MSI PRO MP241X 23.8-inch Professional Office Monitor", "MSI", 6999, "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=400"),
            ("Zebronics S32A 32-inch Full HD LED Monitor with Built-in Speakers", "Zebronics", 11999, "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=400")
        ],
        "Tablets & E-Readers": [
            ("Apple iPad Pro 13-inch (M4 Chip, 256GB Wi-Fi, Space Black)", "Apple", 129900, "https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=400"),
            ("Apple iPad Pro 11-inch (M4 Chip, 256GB Wi-Fi, Silver)", "Apple", 99900, "https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=400"),
            ("Apple iPad Air 13-inch (M2 Chip, 128GB Wi-Fi)", "Apple", 79900, "https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=400"),
            ("Apple iPad Air 11-inch (M2 Chip, 128GB Wi-Fi, Starlight)", "Apple", 59900, "https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=400"),
            ("Apple iPad 10th Generation (10.9-inch, 64GB Wi-Fi, Blue)", "Apple", 34900, "https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=400"),
            ("Apple iPad 9th Generation (10.2-inch, 64GB Wi-Fi)", "Apple", 27900, "https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=400"),
            ("Apple iPad mini 6th Gen (8.3-inch Liquid Retina, 64GB)", "Apple", 49900, "https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=400"),
            ("Apple Pencil Pro for iPad Pro M4 & iPad Air M2", "Apple", 11900, "https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=400"),
            ("Apple Magic Keyboard for iPad Pro 13-inch (M4)", "Apple", 33900, "https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=400"),
            ("Samsung Galaxy Tab S9 Ultra (14.6 Dynamic AMOLED 2X, 256GB)", "Samsung", 108999, "https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=400"),
            ("Samsung Galaxy Tab S9+ (12.4 Dynamic AMOLED 2X, 256GB)", "Samsung", 90999, "https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=400"),
            ("Samsung Galaxy Tab S9 (11.0 Dynamic AMOLED, 128GB)", "Samsung", 72999, "https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=400"),
            ("Samsung Galaxy Tab S9 FE+ (12.4 Display, 128GB)", "Samsung", 46999, "https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=400"),
            ("Samsung Galaxy Tab S9 FE (10.9 Display, 128GB)", "Samsung", 34999, "https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=400"),
            ("Samsung Galaxy Tab A9+ (11.0 90Hz Display, 128GB Wi-Fi)", "Samsung", 20999, "https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=400"),
            ("Samsung Galaxy Tab A9 (8.7 Display, 64GB Wi-Fi)", "Samsung", 12999, "https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=400"),
            ("OnePlus Pad 2 (12.1 3K 144Hz Display, Snapdragon 8 Gen 3)", "OnePlus", 39999, "https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=400"),
            ("OnePlus Pad Go (11.35 2.4K Eye Care Display, 128GB)", "OnePlus", 19999, "https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=400"),
            ("Xiaomi Pad 6 (11.0 2.8K 144Hz, Snapdragon 870, 256GB)", "Xiaomi", 28999, "https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=400"),
            ("Redmi Pad Pro 5G (12.1 2.5K 120Hz, 10000mAh Battery)", "Xiaomi", 24999, "https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=400"),
            ("Redmi Pad SE (11.0 FHD+ 90Hz Display, 128GB)", "Xiaomi", 12999, "https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=400"),
            ("Lenovo Tab P12 with Precision Pen Plus (12.7 3K)", "Lenovo", 26999, "https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=400"),
            ("Lenovo Tab M11 with Tab Pen (11.0 WUXGA, 128GB)", "Lenovo", 15999, "https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=400"),
            ("Lenovo Yoga Tab 11 (11.0 2K Dolby Vision, JBL Quad Speakers)", "Lenovo", 23999, "https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=400"),
            ("Lenovo Tab M10 Plus 3rd Gen (10.61 2K IPS, 128GB)", "Lenovo", 16999, "https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=400"),
            ("Amazon Kindle Paperwhite (16GB, 6.8-inch Display, Warm Light)", "Amazon", 14999, "https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=400"),
            ("Amazon Kindle Paperwhite Signature Edition (32GB Wireless Charging)", "Amazon", 17999, "https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=400"),
            ("Amazon Kindle 11th Gen 2022 (16GB, 6-inch 300 ppi Glare-Free)", "Amazon", 9999, "https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=400"),
            ("Amazon Kindle Oasis (7-inch 300 ppi Ergonomic Design)", "Amazon", 21999, "https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=400"),
            ("Amazon Kindle Scribe (10.2-inch 300 ppi with Basic Pen)", "Amazon", 33999, "https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=400"),
            ("Kobo Clara 2E Eco-Conscious 6-inch E-Reader", "Kobo", 14999, "https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=400"),
            ("Kobo Libra 2 7-inch E-Ink Carta 1200 Touchscreen E-Reader", "Kobo", 19999, "https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=400"),
            ("Kobo Elipsa 2E 10.3-inch Digital Notebook & E-Reader with Stylus", "Kobo", 39999, "https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=400"),
            ("realme Pad 2 (11.5 2K 120Hz Display, 33W Charging, 128GB)", "Realme", 19999, "https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=400"),
            ("realme Pad Mini (8.7 Display, 6400mAh Battery, 64GB)", "Realme", 10999, "https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=400"),
            ("Honor Pad 9 with Free Bluetooth Keyboard (12.1 2.5K)", "Honor", 22999, "https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=400"),
            ("Honor Pad X8 (10.1 FHD Display, 64GB Storage)", "Honor", 11999, "https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=400"),
            ("Nokia T21 Tablet with Active Stylus Support (10.36 2K)", "Nokia", 16999, "https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=400"),
            ("Nokia T20 Tablet (10.4 2K Display, 8200mAh)", "Nokia", 13999, "https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=400"),
            ("Motorola Moto Tab G70 LTE (11-inch 2K IPS, Quad Speakers)", "Motorola", 19999, "https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=400"),
            ("Motorola Moto Tab G62 (10.61 2K IPS, Snapdragon 680)", "Motorola", 14999, "https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=400"),
            ("Acer One 10 T9-1212L 4G LTE Tablet (10.1 FHD, 64GB)", "Acer", 12999, "https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=400"),
            ("Onyx Boox Note Air 3 B/W 10.3 E-Ink Android Tablet", "Onyx", 44999, "https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=400"),
            ("Onyx Boox Palma 6.13 Mobile-Sized E-Ink Android Device", "Onyx", 28999, "https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=400"),
            ("reMarkable 2 The Next-Generation Paper Tablet (10.3 inch)", "reMarkable", 42999, "https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=400"),
            ("Wacom One 13.3-inch Pen Display Creative Drawing Tablet", "Wacom", 34999, "https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=400"),
            ("Wacom Intuos Pro Medium Graphic Drawing Tablet (PTH-660)", "Wacom", 29999, "https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=400"),
            ("XP-PEN Artist 12 2nd Gen Drawing Tablet with 11.9 Screen", "XP-PEN", 21999, "https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=400"),
            ("XP-PEN Deco 01 V2 Graphic Drawing Tablet (10x6.25 inch)", "XP-PEN", 3699, "https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=400"),
            ("Huion Kamvas Pro 13 2.5K QHD Drawing Pen Display", "Huion", 31999, "https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=400")
        ],
        "Accessories & Storage": [
            ("Logitech MX Master 3S Wireless Performance Mouse (8K DPI)", "Logitech", 9495, "https://images.unsplash.com/photo-1615663245857-ac93bb7c39e7?w=400"),
            ("Logitech MX Keys S Wireless Illuminated Keyboard", "Logitech", 11995, "https://images.unsplash.com/photo-1609592424074-1b156b823e25?w=400"),
            ("Logitech C920x HD Pro Webcam (Full HD 1080p/30fps)", "Logitech", 7495, "https://images.unsplash.com/photo-1615663245857-ac93bb7c39e7?w=400"),
            ("Logitech Brio 4K Ultra HD Pro Webcam with RightLight 3", "Logitech", 18995, "https://images.unsplash.com/photo-1615663245857-ac93bb7c39e7?w=400"),
            ("Logitech K380 Multi-Device Bluetooth Wireless Keyboard", "Logitech", 2995, "https://images.unsplash.com/photo-1609592424074-1b156b823e25?w=400"),
            ("Logitech Pebble M350 Wireless Silent Mouse", "Logitech", 1595, "https://images.unsplash.com/photo-1615663245857-ac93bb7c39e7?w=400"),
            ("SanDisk Extreme Portable SSD 1TB (Up to 1050MB/s NVMe)", "SanDisk", 8999, "https://images.unsplash.com/photo-1597872200969-2b65d56bd16b?w=400"),
            ("SanDisk Extreme PRO Portable SSD 2TB (Up to 2000MB/s)", "SanDisk", 18999, "https://images.unsplash.com/photo-1597872200969-2b65d56bd16b?w=400"),
            ("SanDisk Ultra Dual Drive Luxe USB Type-C 128GB", "SanDisk", 1399, "https://images.unsplash.com/photo-1597872200969-2b65d56bd16b?w=400"),
            ("SanDisk 1TB Ultra microSDXC UHS-I Card with Adapter", "SanDisk", 7999, "https://images.unsplash.com/photo-1597872200969-2b65d56bd16b?w=400"),
            ("Samsung T7 Shield Portable SSD 1TB (Rugged, 1050MB/s)", "Samsung", 9999, "https://images.unsplash.com/photo-1597872200969-2b65d56bd16b?w=400"),
            ("Samsung 990 PRO NVMe M.2 Internal SSD 2TB (7450MB/s)", "Samsung", 17999, "https://images.unsplash.com/photo-1597872200969-2b65d56bd16b?w=400"),
            ("Samsung EVO Plus microSDXC 256GB Memory Card", "Samsung", 1899, "https://images.unsplash.com/photo-1597872200969-2b65d56bd16b?w=400"),
            ("Western Digital WD 2TB My Passport Portable External HDD", "Western Digital", 6299, "https://images.unsplash.com/photo-1597872200969-2b65d56bd16b?w=400"),
            ("Western Digital WD 4TB Elements Desktop External Hard Drive", "Western Digital", 9999, "https://images.unsplash.com/photo-1597872200969-2b65d56bd16b?w=400"),
            ("Western Digital WD Black SN770 1TB NVMe PCIe Gen4 SSD", "Western Digital", 6999, "https://images.unsplash.com/photo-1597872200969-2b65d56bd16b?w=400"),
            ("Crucial P3 Plus 1TB PCIe M.2 2280 SSD (5000MB/s)", "Crucial", 5699, "https://images.unsplash.com/photo-1597872200969-2b65d56bd16b?w=400"),
            ("Crucial X9 Pro 1TB Portable SSD (1050MB/s Water-Resistant)", "Crucial", 8499, "https://images.unsplash.com/photo-1597872200969-2b65d56bd16b?w=400"),
            ("Anker 737 Power Bank (PowerCore 24K, 140W Fast Charging)", "Anker", 12999, "https://images.unsplash.com/photo-1609592424074-1b156b823e25?w=400"),
            ("Anker Prime 100W GaN Wall Charger (3-Port Fast Charger)", "Anker", 6999, "https://images.unsplash.com/photo-1609592424074-1b156b823e25?w=400"),
            ("Anker 5-in-1 USB-C Hub with 4K HDMI & SD Card Reader", "Anker", 2499, "https://images.unsplash.com/photo-1609592424074-1b156b823e25?w=400"),
            ("Anker 321 MagGo Magnetic Wireless Power Bank (5000mAh)", "Anker", 2999, "https://images.unsplash.com/photo-1609592424074-1b156b823e25?w=400"),
            ("TP-Link Archer AX73 AX5400 Dual-Band Gigabit WiFi 6 Router", "TP-Link", 8999, "https://images.unsplash.com/photo-1609592424074-1b156b823e25?w=400"),
            ("TP-Link Deco X50 Mesh WiFi 6 System (3-Pack Home Coverage)", "TP-Link", 18999, "https://images.unsplash.com/photo-1609592424074-1b156b823e25?w=400"),
            ("TP-Link Tapo C210 Pan/Tilt Home Security 2K 3MP WiFi Camera", "TP-Link", 2499, "https://images.unsplash.com/photo-1609592424074-1b156b823e25?w=400"),
            ("Belkin BoostCharge Pro 3-in-1 Wireless Charger Stand (MagSafe 15W)", "Belkin", 13999, "https://images.unsplash.com/photo-1609592424074-1b156b823e25?w=400"),
            ("Belkin Connect Thunderbolt 4 Pro Dock (12-in-1 Power Delivery)", "Belkin", 32999, "https://images.unsplash.com/photo-1609592424074-1b156b823e25?w=400"),
            ("Keychron K2 V2 Wireless Mechanical Keyboard (Gateron Brown)", "Keychron", 7999, "https://images.unsplash.com/photo-1609592424074-1b156b823e25?w=400"),
            ("Keychron Q1 Pro QMK/VIA Custom Mechanical Keyboard", "Keychron", 18999, "https://images.unsplash.com/photo-1609592424074-1b156b823e25?w=400"),
            ("Keychron M3 Wireless Optical Gaming Mouse (PAW3395)", "Keychron", 4999, "https://images.unsplash.com/photo-1615663245857-ac93bb7c39e7?w=400"),
            ("Apple 20W USB-C Power Adapter (Original)", "Apple", 1900, "https://images.unsplash.com/photo-1609592424074-1b156b823e25?w=400"),
            ("Apple MagSafe Charger (15W Fast Wireless)", "Apple", 4500, "https://images.unsplash.com/photo-1609592424074-1b156b823e25?w=400"),
            ("Apple AirTag (4 Pack Bluetooth Tracker)", "Apple", 11900, "https://images.unsplash.com/photo-1609592424074-1b156b823e25?w=400"),
            ("Apple Magic Mouse (Wireless, Bluetooth, Multi-Touch Surface)", "Apple", 7500, "https://images.unsplash.com/photo-1615663245857-ac93bb7c39e7?w=400"),
            ("Apple Magic Keyboard with Touch ID and Numeric Keypad", "Apple", 17500, "https://images.unsplash.com/photo-1609592424074-1b156b823e25?w=400"),
            ("MI 20000mAh 18W Fast Charging Power Bank 3i", "Xiaomi", 1999, "https://images.unsplash.com/photo-1609592424074-1b156b823e25?w=400"),
            ("MI Wireless Mouse 2 (Silent Click, Ergonomic)", "Xiaomi", 599, "https://images.unsplash.com/photo-1615663245857-ac93bb7c39e7?w=400"),
            ("boAt EnergyShroom 20000mAh 22.5W Fast Charging Power Bank", "boAt", 1799, "https://images.unsplash.com/photo-1609592424074-1b156b823e25?w=400"),
            ("Ambrane 27000mAh 65W Power Delivery Power Bank (Stylo Pro)", "Ambrane", 3499, "https://images.unsplash.com/photo-1609592424074-1b156b823e25?w=400"),
            ("Portronics 6-in-1 Mport Plus USB-C Hub with 4K HDMI", "Portronics", 1499, "https://images.unsplash.com/photo-1609592424074-1b156b823e25?w=400"),
            ("Satechi Aluminum Multi-Port Adapter V2 4K HDMI (Space Gray)", "Satechi", 7999, "https://images.unsplash.com/photo-1609592424074-1b156b823e25?w=400"),
            ("CalDigit TS4 Thunderbolt 4 18-Port Dock (98W Charging)", "CalDigit", 39999, "https://images.unsplash.com/photo-1609592424074-1b156b823e25?w=400"),
            ("Baseus 65W GaN Charger 3-Port Desktop Fast Charger", "Baseus", 3299, "https://images.unsplash.com/photo-1609592424074-1b156b823e25?w=400"),
            ("UGREEN Revodok 10-in-1 USB C Hub with Dual 4K HDMI", "UGREEN", 5499, "https://images.unsplash.com/photo-1609592424074-1b156b823e25?w=400"),
            ("UGREEN Nexode 140W USB C GaN Charger (PD 3.1 Fast Charge)", "UGREEN", 8999, "https://images.unsplash.com/photo-1609592424074-1b156b823e25?w=400"),
            ("Seagate One Touch 1TB External Hard Drive with Rescue Services", "Seagate", 4999, "https://images.unsplash.com/photo-1597872200969-2b65d56bd16b?w=400"),
            ("Transcend StoreJet 25M3 1TB Military-Grade Shock Resistant HDD", "Transcend", 4499, "https://images.unsplash.com/photo-1597872200969-2b65d56bd16b?w=400"),
            ("Spigen Rugged Armor Case for iPhone 15 Pro Max", "Spigen", 1399, "https://images.unsplash.com/photo-1609592424074-1b156b823e25?w=400"),
            ("Ringke Fusion-X Shockproof Case for Galaxy S24 Ultra", "Ringke", 1299, "https://images.unsplash.com/photo-1609592424074-1b156b823e25?w=400"),
            ("ESR MagSafe Car Mount Wireless Charger with HaloLock (15W)", "ESR", 2599, "https://images.unsplash.com/photo-1609592424074-1b156b823e25?w=400")
        ]
    }

    products_data = []
    prod_id = 101

    for category_name, items in catalog_blueprint.items():
        for title, brand, base_price, img in items:
            products_data.append({
                "product_id": prod_id,
                "title": title,
                "category": category_name,
                "brand": brand,
                "base_price": base_price,
                "image_url": img
            })
            prod_id += 1

    df_products = pd.DataFrame(products_data)
    df_products.to_csv(os.path.join(output_dir, "products.csv"), index=False)

    # 2. Multi-Store Price Listings (Amazon, Flipkart, Croma)
    platforms = ["Amazon", "Flipkart", "Croma"]
    pricing_records = []

    for item in products_data:
        p_id = item["product_id"]
        base = item["base_price"]

        # Realistic price spreads across retailers
        variations = {
            "Amazon": round(base * random.uniform(0.92, 0.98), -1),
            "Flipkart": round(base * random.uniform(0.90, 0.96), -1),
            "Croma": round(base * random.uniform(0.93, 0.99), -1)
        }

        for plat in platforms:
            price = variations[plat]
            rating = round(random.uniform(4.1, 4.9), 1)
            reviews = random.randint(350, 18500)
            
            # Real live store search link URLs
            encoded_title = item['title'].replace(' ', '+').replace('&', '%26')
            if plat == "Amazon":
                buy_link = f"https://www.amazon.in/s?k={encoded_title}"
            elif plat == "Flipkart":
                buy_link = f"https://www.flipkart.com/search?q={encoded_title}"
            else:
                buy_link = f"https://www.croma.com/searchB?q={encoded_title}"

            pricing_records.append({
                "product_id": p_id,
                "platform": plat,
                "price": price,
                "rating": rating,
                "review_count": reviews,
                "in_stock": True,
                "buy_link": buy_link
            })

    df_pricing = pd.DataFrame(pricing_records)
    df_pricing.to_csv(os.path.join(output_dir, "platform_prices.csv"), index=False)

    # 3. User Interactions Stream (200 users, 5,000+ interactions)
    num_users = 200
    interaction_records = []
    category_list = list(catalog_blueprint.keys())

    for u_id in range(1, num_users + 1):
        fav_cat = random.choice(category_list)
        interacted_prods = random.sample([p["product_id"] for p in products_data], random.randint(18, 35))
        for p_id in interacted_prods:
            prod = next(p for p in products_data if p["product_id"] == p_id)
            if prod["category"] == fav_cat:
                rating = random.choice([4.0, 4.5, 5.0])
            else:
                rating = random.choice([2.5, 3.0, 3.5, 4.0])
            interaction_records.append({
                "user_id": u_id,
                "product_id": p_id,
                "rating": rating,
                "timestamp": pd.Timestamp.now()
            })

    df_interactions = pd.DataFrame(interaction_records)
    df_interactions.to_csv(os.path.join(output_dir, "user_interactions.csv"), index=False)

    # 4. Realistic Category-Specific Reviews (1,000 customer reviews)
    review_templates = {
        "Smartphones": [
            ("Outstanding display quality, fluid 120Hz refresh rate, and premium build. Camera excels in low-light photography.", 4.8),
            ("Solid performance and fast charging. Battery easily lasts 1.5 days under moderate use. Highly recommended.", 4.5),
            ("Great daily driver phone. Crisp stereo speakers and smooth software. Slightly warms up during heavy gaming.", 4.2),
            ("Premium look and feel in hand. Haptics and display brightness under direct sunlight are top tier.", 4.6)
        ],
        "Laptops": [
            ("Blazing fast processing speed, silent fan operation, and exceptional battery backup. Keyboard travel is comfortable.", 4.9),
            ("Superb color accurate display, great for creative workflows and coding. Lightweight and portable chassis.", 4.6),
            ("Excellent performance and fast SSD loading times. Build quality is solid aluminum. Runs slightly warm under full render load.", 4.3),
            ("Remarkable keyboard and trackpad experience. Audio from stereo speakers is surprisingly rich.", 4.7)
        ],
        "Audio": [
            ("Class-leading active noise cancellation and crystal clear audio profile. Bass is punchy without overpowering vocals.", 4.9),
            ("Exceptional battery life and fast USB-C charging. Multi-point Bluetooth connection seamlessly switches devices.", 4.6),
            ("Very comfortable ear cushions for long listening sessions. Mic clarity on calls is clear and crisp.", 4.4),
            ("High resolution sound stage and deep sub-bass response. Premium compact carrying case included.", 4.7)
        ],
        "Smartwatches": [
            ("Comprehensive health and fitness tracking metrics. Heart rate and sleep stage tracking are accurate. Bright AMOLED display.", 4.8),
            ("Seamless smartphone notifications and crystal clear Bluetooth calling. Battery lasts several days between charges.", 4.5),
            ("Elegant metallic finish and comfortable wrist strap. GPS locks on quickly for outdoor workouts and runs.", 4.6),
            ("Great companion for fitness enthusiasts. Water resistance holds up well during swimming.", 4.4)
        ],
        "Smart TVs & Home": [
            ("Breathtaking 4K picture quality with deep inky blacks and vivid contrast. Dolby Vision and Atmos deliver cinema feel.", 4.9),
            ("Smooth smart TV interface with zero lag. Audio output is loud and clear for movie dialogue.", 4.5),
            ("Sleek minimalist bezel design. Multiple HDMI 2.1 ports for next-gen console gaming at 120Hz.", 4.7),
            ("Exceptional value for money. Bright panel visible even in sunny living rooms.", 4.4)
        ],
        "Gaming Consoles & Gear": [
            ("Incredible responsiveness, ultra-low latency, and tactile mechanical feedback. Ergonomic grip reduces hand fatigue.", 4.9),
            ("Stunning next-gen gaming graphics and lightning fast SSD load times. Immersive spatial audio.", 4.8),
            ("Premium build materials and durable switches. Customizable RGB lighting and intuitive companion software.", 4.6),
            ("Essential upgrade for competitive gamers. Accurate tracking sensor with zero smoothing or acceleration.", 4.7)
        ],
        "Cameras & Drones": [
            ("Sensational image sensor dynamic range and lightning-fast subject autofocus tracking. 4K 60fps video is pin-sharp.", 4.9),
            ("Exceptional in-body image stabilization. Ergonomic grip and weather-sealed magnesium alloy chassis.", 4.8),
            ("Stunning color science straight out of camera. Dual card slots provide peace of mind on critical shoots.", 4.7),
            ("Intuitive menu system and crisp electronic viewfinder. Battery life easily covers a full day shoot.", 4.5)
        ],
        "Monitors & Displays": [
            ("Gorgeous color accuracy and wide viewing angles. Ultra-fast refresh rate eliminates ghosting in fast-paced content.", 4.8),
            ("Versatile ergonomic stand with full height, tilt, and pivot adjustments. Clean integrated cable management.", 4.6),
            ("Sharp pixel density and excellent brightness. USB-C single cable connectivity powers laptop while transmitting video.", 4.7),
            ("Immersive curved panel enhances productivity by fitting multiple windows comfortably side by side.", 4.5)
        ],
        "Tablets & E-Readers": [
            ("Incredible screen responsiveness and buttery smooth stylus drawing experience. Thin and featherweight in backpack.", 4.9),
            ("Paper-like reading display that causes zero eye fatigue even under bright sunlight. Weeks of battery life.", 4.8),
            ("Ideal for productivity, note-taking, and media consumption. Loud quad speakers with wide stereo separation.", 4.6),
            ("Versatile multitasking capabilities and desktop-class browsing speed. Magnetic keyboard snaps on securely.", 4.5)
        ],
        "Accessories & Storage": [
            ("Extremely fast transfer speeds across large file libraries. Robust shock-resistant casing keeps data safe.", 4.9),
            ("Compact form factor that slips easily into pockets. Fast charging capability powers all devices reliably.", 4.7),
            ("Flawless compatibility across macOS, Windows, and mobile devices. Outstanding build reliability.", 4.6),
            ("Premium tactile switches and satisfying click feel. Seamless multi-device pairing via Bluetooth and 2.4GHz.", 4.5)
        ]
    }

    review_records = []
    for item in products_data:
        cat = item["category"]
        templates = review_templates.get(cat, review_templates["Accessories & Storage"])
        chosen_reviews = random.sample(templates, 2)
        for text, r_val in chosen_reviews:
            review_records.append({
                "product_id": item["product_id"],
                "review_text": f"{text} The {item['title']} is a top choice in its class.",
                "rating": r_val
            })

    df_reviews = pd.DataFrame(review_records)
    df_reviews.to_csv(os.path.join(output_dir, "product_reviews.csv"), index=False)

    # 5. Price History Logs (500 products x 30 days = 15,000 entries)
    history_records = []
    dates = pd.date_range(end=pd.Timestamp.now(), periods=30, freq='D')
    for item in products_data:
        base = item["base_price"]
        trend = np.linspace(base * random.uniform(1.02, 1.05), base * random.uniform(0.93, 0.97), 30)
        noise = np.random.normal(0, base * 0.005, 30)
        prices = np.round(trend + noise, -1)
        for i, d in enumerate(dates):
            history_records.append({
                "product_id": item["product_id"],
                "date": d.strftime('%Y-%m-%d'),
                "price": prices[i]
            })

    df_history = pd.DataFrame(history_records)
    df_history.to_csv(os.path.join(output_dir, "price_history.csv"), index=False)

    print(f"Successfully generated 500-Product Real Catalog in '{output_dir}':")
    print(f"   - products.csv ({len(products_data)} products)")
    print(f"   - platform_prices.csv ({len(df_pricing)} store listings)")
    print(f"   - user_interactions.csv ({len(df_interactions)} user logs)")
    print(f"   - product_reviews.csv ({len(df_reviews)} customer reviews)")
    print(f"   - price_history.csv ({len(df_history)} price trend logs)")

generate_datasets = generate_500_products_dataset

if __name__ == "__main__":
    data_path = os.path.join(os.path.dirname(__file__), "..", "data")
    generate_500_products_dataset(data_path)
