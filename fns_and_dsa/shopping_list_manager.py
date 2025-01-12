""" Shopping list manager that allows users to add items, view current items, and remove items from a list. """

def display_menu():
    """ Display the menu options for the shopping list manager. """
    print("Shopping List Manager")
    print("1. Add item")
    print("2. Remove item")
    print("3. View list")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            item = input("Enter the item to add: ")
            shopping_list.append(item)

        elif choice == '2':
            item = input("Enter the item to remove: ")
            try:
                shopping_list.remove(item)
            except ValueError:
                print(f"{item} not found in the list!")
        elif choice == '3':
            print("Shopping List:")
            for item in shopping_list:
                print(item)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()