from storage import initialize_storage
from item_manager import (
    add_item,
    view_items,
    search_items,
    update_status,
    delete_item
)
from report_manager import show_report


def main():
    initialize_storage()

    while True:
        print("\n===================================")
        print("   LOST AND FOUND MANAGEMENT SYSTEM")
        print("===================================")

        print("1. Report Lost or Found Item")
        print("2. View All Items")
        print("3. Search Items")
        print("4. Update Item Status")
        print("5. Delete Item")
        print("6. View Reports")
        print("7. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            add_item()

        elif choice == "2":
            view_items()

        elif choice == "3":
            search_items()

        elif choice == "4":
            update_status()

        elif choice == "5":
            delete_item()

        elif choice == "6":
            show_report()

        elif choice == "7":
            print("\nThank you for using the system!")
            break

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()
