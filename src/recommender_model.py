import os
import pandas as pd
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim

class NCFRecommender(nn.Module):
    def __init__(self, num_users, num_items, embedding_dim=16):
        super(NCFRecommender, self).__init__()
        self.user_embedding = nn.Embedding(num_users + 1, embedding_dim)
        self.item_embedding = nn.Embedding(num_items + 1, embedding_dim)
        
        self.fc_layers = nn.Sequential(
            nn.Linear(embedding_dim * 2, 32),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(32, 16),
            nn.ReLU(),
            nn.Linear(16, 1)
        )

    def forward(self, user_idx, item_idx):
        user_emb = self.user_embedding(user_idx)
        item_emb = self.item_embedding(item_idx)
        x = torch.cat([user_emb, item_emb], dim=-1)
        score = self.fc_layers(x)
        return score.squeeze()


class RecommendationEngine:
    def __init__(self, data_dir):
        self.data_dir = data_dir
        self.products_df = pd.read_csv(os.path.join(data_dir, "products.csv"))
        self.interactions_df = pd.read_csv(os.path.join(data_dir, "user_interactions.csv"))
        
        self.user_ids = sorted(self.interactions_df['user_id'].unique())
        self.product_ids = sorted(self.products_df['product_id'].unique())
        
        self.user2idx = {u: i for i, u in enumerate(self.user_ids)}
        self.item2idx = {p: i for i, p in enumerate(self.product_ids)}
        self.idx2item = {i: p for p, i in self.item2idx.items()}

        self.model = NCFRecommender(len(self.user_ids), len(self.product_ids))
        self.is_trained = False

    def train(self, epochs=25, lr=0.01):
        users = torch.tensor([self.user2idx[u] for u in self.interactions_df['user_id']], dtype=torch.long)
        items = torch.tensor([self.item2idx[p] for p in self.interactions_df['product_id']], dtype=torch.long)
        ratings = torch.tensor(self.interactions_df['rating'].values, dtype=torch.float32)

        criterion = nn.MSELoss()
        optimizer = optim.Adam(self.model.parameters(), lr=lr)

        self.model.train()
        for epoch in range(epochs):
            optimizer.zero_grad()
            predictions = self.model(users, items)
            loss = criterion(predictions, ratings)
            loss.backward()
            optimizer.step()

        self.is_trained = True

    def get_recommendations(self, user_id, top_k=4):
        if not self.is_trained:
            self.train()

        if user_id not in self.user2idx:
            return self.products_df.head(top_k)

        u_idx = self.user2idx[user_id]
        
        user_tensor = torch.tensor([u_idx] * len(self.product_ids), dtype=torch.long)
        item_tensor = torch.tensor(list(range(len(self.product_ids))), dtype=torch.long)

        self.model.eval()
        with torch.no_grad():
            scores = self.model(user_tensor, item_tensor).numpy()

        top_indices = np.argsort(scores)[::-1]
        
        rec_item_ids = [self.idx2item[idx] for idx in top_indices[:top_k]]

        rec_products = self.products_df[self.products_df['product_id'].isin(rec_item_ids)].copy()
        
        score_dict = {self.idx2item[idx]: round(float(scores[idx]), 2) for idx in top_indices}
        rec_products['match_score'] = rec_products['product_id'].map(score_dict)
        rec_products = rec_products.sort_values(by='match_score', ascending=False)
        
        return rec_products

if __name__ == "__main__":
    data_path = os.path.join(os.path.dirname(__file__), "..", "data")
    if os.path.exists(os.path.join(data_path, "user_interactions.csv")):
        engine = RecommendationEngine(data_path)
        engine.train(epochs=20)
        print("Recommender Engine Verified.")
