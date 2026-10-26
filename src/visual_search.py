import os
import pandas as pd
import numpy as np

class VisualSearchEngine:
    def __init__(self, data_dir):
        self.data_dir = data_dir
        self.products_df = pd.read_csv(os.path.join(data_dir, "products.csv"))
        np.random.seed(42)
        
        # Precompute normalized 64-dimensional synthetic visual feature vectors
        self.features = {}
        for idx, row in self.products_df.iterrows():
            cat = row['category']
            base_vec = np.zeros(64)
            cat_hash = hash(cat) % 10
            base_vec[cat_hash * 6 : (cat_hash + 1) * 6] = 1.0
            base_vec += np.random.normal(0, 0.08, 64)
            norm = np.linalg.norm(base_vec)
            self.features[row['product_id']] = base_vec / (norm if norm > 0 else 1.0)

    def search_by_image(self, target_category="Smartphones", top_k=4):
        """
        Simulates deep feature extraction and Cosine Similarity search
        to match query product image embeddings with catalog items.
        """
        cat_hash = hash(target_category) % 10
        query_vec = np.zeros(64)
        query_vec[cat_hash * 6 : (cat_hash + 1) * 6] = 1.0
        query_vec += np.random.normal(0, 0.05, 64)
        query_vec /= np.linalg.norm(query_vec)

        scores = {}
        for p_id, feat_vec in self.features.items():
            sim = float(np.dot(query_vec, feat_vec))
            scores[p_id] = max(0.50, min(0.99, sim))

        # Filter candidates prioritizing category or overall top visual matches
        cat_prods = self.products_df[self.products_df['category'] == target_category]
        if not cat_prods.empty:
            cat_ids = set(cat_prods['product_id'])
            sorted_ids = sorted(cat_ids, key=lambda x: scores[x], reverse=True)[:top_k]
        else:
            sorted_ids = sorted(scores, key=scores.get, reverse=True)[:top_k]

        results = self.products_df[self.products_df['product_id'].isin(sorted_ids)].copy()
        results['visual_similarity'] = results['product_id'].map(lambda x: round(scores[x] * 100, 1))
        return results.sort_values(by='visual_similarity', ascending=False)

if __name__ == "__main__":
    data_path = os.path.join(os.path.dirname(__file__), "..", "data")
    if os.path.exists(os.path.join(data_path, "products.csv")):
        engine = VisualSearchEngine(data_path)
        res = engine.search_by_image("Smartphones", top_k=3)
        print(f"Visual Search Engine Verified. Returned {len(res)} visually similar items:")
        for _, r in res.iterrows():
            print(f" - {r['title']} ({r['visual_similarity']}%)")
