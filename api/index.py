import os
import sys

# Add project root directory to path so imports work seamlessly on Vercel
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app
