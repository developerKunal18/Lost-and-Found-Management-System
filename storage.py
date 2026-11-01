import json
import os
from config import DATA_DIR, ITEMS_FILE


def initialize_storage():
    os.makedirs(DATA_DIR, exist_ok=True)

    if not os.path.exists(ITEMS_FILE):
        with open(ITEMS_FILE, "w") as file:
            json.dump([], file, indent=4)


def load_items():
    initialize_storage()

    try:
        with open(ITEMS_FILE, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return []


def save_items(items):
    initialize_storage()

    with open(ITEMS_FILE, "w") as file:
        json.dump(items, file, indent=4)
