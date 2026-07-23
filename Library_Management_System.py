

library = {}



def add_book():
    category = input("Enter Category: ")
    book = input("Enter Book Name: ")


    if category not in library:
        library[category] = {}


    if book in library[category]:
        print("Book already exists.")

    else:
        library[category][book] = "Available"
        print("Book added successfully.")



def borrow_book():
    category = input("Enter Category: ")
    book = input("Enter Book Name: ")

    if category not in library:
        print("Category not found.")

    elif book not in library[category]:
        print("Book not found.")

    elif library[category][book] == "Borrowed":
        print("Book already borrowed.")

    else:
        library[category][book] = "Borrowed"
        print("Book borrowed successfully.")



def return_book():
    category = input("Enter Category: ")
    book = input("Enter Book Name: ")

    if category not in library:
        print("Category not found.")

    elif book not in library[category]:
        print("Book not found.")

    elif library[category][book] == "Available":
        print("Book is already available.")

    else:
        library[category][book] = "Available"
        print("Book returned successfully.")



def search_book():
    category = input("Enter Category: ")
    book = input("Enter Book Name: ")

    if category not in library:
        print("Category not found.")

    elif book not in library[category]:
        print("Book not found.")

    else:
        print("Book Found")
        print("Status :", library[category][book])



def show_all_books():

    if len(library) == 0:
        print("Library is empty.")
        return

    print("\n========== Library ==========")

    for category in library:

        print(f"\nCategory : {category}")

        for book in library[category]:
            print(f"   {book} --> {library[category][book]}")



def show_category():

    category = input("Enter Category: ")

    if category not in library:
        print("Category not found.")

    else:

        print(f"\nBooks in {category}:\n")

        for book in library[category]:
            print(book, "-->", library[category][book])



while True:

    print("\n========== Library Management System ==========")
    print("1. Add Book")
    print("2. Borrow Book")
    print("3. Return Book")
    print("4. Search Book")
    print("5. Show All Books")
    print("6. Show Books By Category")
    print("7. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        add_book()

    elif choice == "2":
        borrow_book()

    elif choice == "3":
        return_book()

    elif choice == "4":
        search_book()

    elif choice == "5":
        show_all_books()

    elif choice == "6":
        show_category()

    elif choice == "7":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")