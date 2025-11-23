# Simple Library Management System

import csv
import os
import sys

# store all the details of book
library = []

# Load data from CSV file
def load_data():
    if os.path.exists("books.csv"):
        with open("books.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                library.append(row)

# Save data to CSV file
def save_data():
    with open("books.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["id", "title", "author", "status"])
        writer.writeheader()
        writer.writerows(library)

def add_book():
    print("\nAdd Book")
    bid = input("Book ID       : ")
    title = input("Book Name     : ")
    writer = input("Author Name   : ")

    record = {
        "id": bid,
        "title": title,
        "author": writer,
        "status": "Available"
    }

    library.append(record)
    save_data()
    print("Book added.\n")

def show_books():
    print("\nAll Books in Library")
    if library == []:
        print("No records found.\n")
        return

    print("{:<10} {:<25} {:<20} {:<10}".format("ID", "Title", "Author", "Status"))
    print("-" * 70)
    for book in library:
        print("{:<10} {:<25} {:<20} {:<10}".format(book["id"], book["title"], book["author"], book["status"]))
    print()

def search_book():
    print("\nSearch Book")
    bid = input("Enter Book ID: ")
    for book in library:
        if book["id"] == bid:
            print("Match Found!")
            print("ID     :", book["id"])
            print("Title  :", book["title"])
            print("Author :", book["author"])
            print("Status :", book["status"], "\n")
            return
    print("No such book.\n")

def issue_book():
    print("\nIssue Book")
    bid = input("Book ID: ")
    for book in library:
        if book["id"] == bid:
            if book["status"] == "Available":
                book["status"] = "Issued"
                save_data()
                print("Book issued.\n")
            else:
                print("Already issued.\n")
            return
    print("Book not found.\n")

def return_book():
    print("\nReturn Book")
    bid = input("Book ID: ")
    for book in library:
        if book["id"] == bid:
            if book["status"] == "Issued":
                book["status"] = "Available"
                save_data()
                print("Book returned.\n")
            else:
                print("This book was not issued.\n")
            return
    print("Book not found.\n")


# program for library menu
load_data()

while True:
    print("=== LIBRARY MENU ===")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Exit")

    ch = input("Choose (1-6): ")

    if ch == "1":
        add_book()
    elif ch == "2":
        show_books()
    elif ch == "3":
        search_book()
    elif ch == "4":
        issue_book()
    elif ch == "5":
        return_book()
    elif ch == "6":
        print("Goodbye")
        break
    else:
        print("Invalid choice.\n")
