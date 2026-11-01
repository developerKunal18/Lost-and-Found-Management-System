from datetime import datetime


def get_next_id(items):
    if not items:
        return 1

    return max(item["id"] for item in items) + 1


def get_date():
    return datetime.now().strftime("%Y-%m-%d")


def print_line():
    print("-" * 65)


def input_required(message):
    while True:
        value = input(message).strip()

        if value:
            return value

        print("This field cannot be empty.")


def display_item(item):
    print_line()
    print(f"ID          : {item['id']}")
    print(f"Item Name   : {item['name']}")
    print(f"Type        : {item['type']}")
    print(f"Description : {item['description']}")
    print(f"Location    : {item['location']}")
    print(f"Date        : {item['date']}")
    print(f"Contact     : {item['contact']}")
    print(f"Status      : {item['status']}")
