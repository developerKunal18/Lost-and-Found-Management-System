from storage import load_items, save_items
from config import ITEM_TYPES, ITEM_STATUSES
from utils import get_next_id, get_date, input_required, display_item


def add_item():
    items = load_items()

    print("\n1. Lost Item")
    print("2. Found Item")

    choice = input("Select item type: ").strip()

    if choice == "1":
        item_type = "Lost"
    elif choice == "2":
        item_type = "Found"
    else:
        print("Invalid selection.")
        return

    name = input_required("Enter item name: ")
    description = input_required("Enter description: ")
    location = input_required("Enter location: ")
    contact = input_required("Enter contact details: ")

    item = {
        "id": get_next_id(items),
        "name": name,
        "type": item_type,
        "description": description,
        "location": location,
        "date": get_date(),
        "contact": contact,
        "status": "Pending"
    }

    items.append(item)
    save_items(items)

    print("\nItem reported successfully!")


def view_items():
    items = load_items()

    if not items:
        print("\nNo records available.")
        return

    print("\nALL LOST AND FOUND ITEMS")

    for item in items:
        display_item(item)


def search_items():
    items = load_items()

    keyword = input_required(
        "Enter item name or location to search: "
    ).lower()

    results = [
        item for item in items
        if keyword in item["name"].lower()
        or keyword in item["location"].lower()
    ]

    if not results:
        print("\nNo matching records found.")
        return

    print("\nSEARCH RESULTS")

    for item in results:
        display_item(item)


def update_status():
    items = load_items()

    try:
        item_id = int(input("Enter item ID: "))
    except ValueError:
        print("Please enter a valid numeric ID.")
        return

    item = next(
        (item for item in items if item["id"] == item_id),
        None
    )

    if not item:
        print("Item not found.")
        return

    print("\n1. Pending")
    print("2. Resolved")

    choice = input("Select new status: ").strip()

    if choice == "1":
        item["status"] = "Pending"
    elif choice == "2":
        item["status"] = "Resolved"
    else:
        print("Invalid status.")
        return

    save_items(items)
    print("Item status updated successfully!")


def delete_item():
    items = load_items()

    try:
        item_id = int(input("Enter item ID to delete: "))
    except ValueError:
        print("Please enter a valid numeric ID.")
        return

    updated_items = [
        item for item in items
        if item["id"] != item_id
    ]

    if len(updated_items) == len(items):
        print("Item not found.")
        return

    save_items(updated_items)
    print("Item deleted successfully!")
