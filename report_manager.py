from storage import load_items


def show_report():
    items = load_items()

    total = len(items)

    lost = sum(
        1 for item in items
        if item["type"] == "Lost"
    )

    found = sum(
        1 for item in items
        if item["type"] == "Found"
    )

    pending = sum(
        1 for item in items
        if item["status"] == "Pending"
    )

    resolved = sum(
        1 for item in items
        if item["status"] == "Resolved"
    )

    print("\n========== ITEM REPORT ==========")
    print(f"Total Items   : {total}")
    print(f"Lost Items    : {lost}")
    print(f"Found Items   : {found}")
    print(f"Pending Items : {pending}")
    print(f"Resolved      : {resolved}")
    print("=================================")
