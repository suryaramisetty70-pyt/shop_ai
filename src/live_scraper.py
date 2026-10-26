import os
import requests
import re
import random
from bs4 import BeautifulSoup
from src.google_search import GoogleShoppingSearch

class LiveMarketScraper:
    def __init__(self, data_dir):
        self.data_dir = data_dir
        self.searcher = GoogleShoppingSearch()

    def fetch_live_market_data(self, query):
        """
        Delegates to GoogleShoppingSearch engine for unified multi-platform lookup.
        """
        return self.searcher.search_google_shopping(query)

if __name__ == "__main__":
    scraper = LiveMarketScraper(".")
    res = scraper.fetch_live_market_data("iPhone 15 Pro")
    print("Live Scraper Verified:", res[0]["title"])
