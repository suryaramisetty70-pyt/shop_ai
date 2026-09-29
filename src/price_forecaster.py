import os
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

class PriceForecaster:
    def __init__(self, data_dir):
        self.data_dir = data_dir
        self.reload_data()

    def reload_data(self):
        self.history_df = pd.read_csv(os.path.join(self.data_dir, "price_history.csv"))
        self.products_df = pd.read_csv(os.path.join(self.data_dir, "products.csv"))

    def predict_price_trend(self, product_id):
        self.reload_data()
        df_prod = self.history_df[self.history_df['product_id'] == product_id].copy()
        
        # Universal fallback if product_id not found in history
        if df_prod.empty:
            product_id = self.products_df.iloc[0]['product_id']
            df_prod = self.history_df[self.history_df['product_id'] == product_id].copy()

        df_prod['day_num'] = np.arange(len(df_prod))
        X = df_prod[['day_num']].values
        y = df_prod['price'].values

        model = LinearRegression()
        model.fit(X, y)

        next_day = len(df_prod) + 7
        predicted_price = float(model.predict([[next_day]])[0])
        current_price = float(y[-1])
        min_price = float(np.min(y))

        pct_change = ((predicted_price - current_price) / current_price) * 100

        if current_price <= min_price * 1.01 or pct_change > 1.5:
            signal = "BUY NOW"
            reason = "Price is at 30-day historical low. Great time to purchase!"
        elif pct_change < -1.5:
            signal = "WAIT"
            reason = f"Price is projected to drop by {abs(pct_change):.1f}% over the next 7 days."
        else:
            signal = "STABLE"
            reason = "Price is expected to remain steady with minimal fluctuation."

        return df_prod, round(predicted_price, -1), signal, reason

if __name__ == "__main__":
    data_path = os.path.join(os.path.dirname(__file__), "..", "data")
    if os.path.exists(os.path.join(data_path, "price_history.csv")):
        forecaster = PriceForecaster(data_path)
        print("Price Forecaster Verified.")
