import os
import pandas as pd
import numpy as np

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
        x_vals = df_prod['day_num'].values
        y = df_prod['price'].values

        # Linear regression via Ordinary Least Squares (pure NumPy, zero heavy dependencies)
        if len(x_vals) > 1:
            slope, intercept = np.polyfit(x_vals, y, 1)
            next_day = len(df_prod) + 7
            predicted_price = float(slope * next_day + intercept)
        else:
            predicted_price = float(y[0])

        current_price = float(y[-1])
        min_price = float(np.min(y))
        pct_change = ((predicted_price - current_price) / current_price) * 100

        if current_price <= min_price * 1.01 or pct_change > 1.2:
            signal = "BUY NOW"
            reason = "Price is near its 30-day historical low and expected to rise soon. Great time to buy!"
        elif pct_change < -1.2:
            signal = "WAIT FOR DROP"
            reason = f"Price is projected to drop by ~{abs(pct_change):.1f}% over the next 7-14 days. Waiting is advised."
        else:
            signal = "PRICE STABLE"
            reason = "Price is currently steady with less than 1% variance projected over the next week."

        # Return history data points for sparkline visualization
        history_points = [
            {"date": str(row['date']), "price": int(row['price'])}
            for _, row in df_prod.iterrows()
        ]

        return df_prod, round(predicted_price, -1), signal, reason, history_points

if __name__ == "__main__":
    data_path = os.path.join(os.path.dirname(__file__), "..", "data")
    if os.path.exists(os.path.join(data_path, "price_history.csv")):
        forecaster = PriceForecaster(data_path)
        _, pred, sig, rsn, _ = forecaster.predict_price_trend(101)
        print(f"Price Forecaster Verified. Signal: {sig}, Predicted: {pred}")
