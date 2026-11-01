import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
ITEMS_FILE = os.path.join(DATA_DIR, "items.json")

ITEM_TYPES = ["Lost", "Found"]
ITEM_STATUSES = ["Pending", "Resolved"]
