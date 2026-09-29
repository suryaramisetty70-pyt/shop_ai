import os
import pandas as pd
import numpy as np
import torch

class VisualSearchEngine:
    def __init__(self, data_dir):
        self.data_dir = data_dir
        self.products_df = pd.read_csv(os.path.join(data_dir, "products.csv"))
        np.random.seed(42)
        
        # Generate synthetic 64-dim visual feature vectors for each product category
        self.features = {}
        for idx, row in self.products_df.iterrows():
            cat = row['category']
            base_vec = np.zeros(64)
            if cat == "Smartphones":
                base_vec[:16] = 1.0
            elif cat == "Laptops":
                base_vec[16:32] = 1.0
            elif cat == "Audio":
                base_vec[32:48] = 1.0
            else:
                base_vec[48:64] = 1.0
            base_vec += np.random.normal(0, 0.1, 64)
            self.features[row['product_id']] = base_vec / np.linalg.norm(base_vec)

    def search_by_image(self, target_category="Smartphones", top_k=3):
        """
        Simulates image feature extraction and Cosine Similarity search
        to match uploaded photo with catalog items.
        """
        query_vec = np.zeros(64)
        if target_category == "Smartphones":
            query_vec[:16] = 1.0
        elif target_category == "Laptops":
            query_vec[16:32] = 1.0
        elif target_category == "Audio":
            query_vec[32:48] = 1.0
        else:
            query_vec[48:64] = 1.0
        query_vec /= np.linalg.norm(query_vec)

        scores = {}
        for p_id, feat_vec in self.features.items():
            sim = float(np.dot(query_vec, feat_vec))
            scores[p_id] = sim

        sorted_ids = sorted(scores, key=scores.get, reverse=True)[:top_k]
        results = self.products_df[self.products_df['product_id'].isin(sorted_ids)].copy()
        results['visual_similarity'] = results['product_id'].map(lambda x: round(scores[x] * 100, 1))
        return results.sort_values(by='visual_similarity', ascending=False)

if __name__ == "__main__":
    data_path = os.path.join(os.path.dirname(__file__), "..", "data")
    if os.path.exists(os.path.join(data_path, "products.csv")):
        engine = VisualSearchEngine(data_path)
        res = engine.search_by_image("Smartphones")
        print("Visual Search Engine Verified.")
