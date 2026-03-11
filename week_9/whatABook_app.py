"""
Title: whatabook_app.py
Author: Group 3
Date: 3/11/2026
Description: Console application for the WhatABook MongoDB database
"""

from pymongo import MongoClient
from getpass import getpass
import sys


# --------------------------------------------------
# MongoDB Cluster Configuration
# --------------------------------------------------

CLUSTER_ADDRESS = "bellevueuniversity.agiceyx.mongodb.net"   # Replace with your Atlas cluster
DATABASE_NAME = "whatABookDB"


# --------------------------------------------------
# Startup Banner
# --------------------------------------------------

def show_banner():

    print("\n===================================")
    print("        Welcome to WhatABook")
    print("      Bellevue University Demo")
    print("===================================")


# --------------------------------------------------
# MongoDB Login Prompt
# --------------------------------------------------

def connect_to_database():

    print("\n--- MongoDB Login ---")

    username = input("Enter MongoDB username: ")
    password = getpass("Enter MongoDB password: ")

    connection_string = f"mongodb+srv://{username}:{password}@{CLUSTER_ADDRESS}/{DATABASE_NAME}?retryWrites=true&w=majority"

    try:
        client = MongoClient(connection_string)
        client.admin.command("ping")

        print("\nConnection successful.\n")

        return client[DATABASE_NAME]

    except Exception as e:
        print("\nConnection failed.")
        print(e)
        sys.exit()


# --------------------------------------------------
# Database Statistics
# --------------------------------------------------

def show_database_stats(db):

    books = db["books"]
    customers = db["customers"]
    wishlist = db["wishlistitems"]

    print("Database Loaded Successfully")
    print("--------------------------------")

    print(f"Books Available: {books.count_documents({})}")
    print(f"Customers: {customers.count_documents({})}")
    print(f"Wishlist Items: {wishlist.count_documents({})}")

    print("--------------------------------\n")


# --------------------------------------------------
# Display all books
# --------------------------------------------------

def display_books(books):

    print("\n--- Available Books ---")

    for book in books.find({}, {"_id": 0}):
        print(f"{book['bookId']} | {book['title']} | {book['author']} | {book['genre']}")


# --------------------------------------------------
# Display books by genre
# --------------------------------------------------

def display_books_by_genre(books):

    print("\n--- Select a Genre ---")

    genres = sorted(books.distinct("genre"))

    for index, genre in enumerate(genres, start=1):
        print(f"{index}. {genre}")

    try:
        selection = int(input("\nChoose genre number: "))

        if selection < 1 or selection > len(genres):
            print("Invalid selection.")
            return

        selected_genre = genres[selection - 1]

    except ValueError:
        print("Please enter a number.")
        return

    print(f"\n--- Books in {selected_genre} ---")

    results = books.find({"genre": selected_genre}, {"_id": 0})

    for book in results:
        print(f"{book['bookId']} | {book['title']} | {book['author']}")


# --------------------------------------------------
# Display customer wishlist (Aggregation + $lookup)
# --------------------------------------------------

def display_wishlist(customers, wishlist):

    customer_id = input("\nEnter customerId (c1007, c1008, c1009): ")

    customer = customers.find_one({"customerId": customer_id})

    if not customer:
        print("Invalid customerId.")
        return

    print(f"\n--- Wishlist for {customer['firstName']} {customer['lastName']} ---")

    pipeline = [
        {"$match": {"customerId": customer_id}},
        {
            "$lookup": {
                "from": "books",
                "localField": "bookId",
                "foreignField": "bookId",
                "as": "book"
            }
        },
        {"$unwind": "$book"}
    ]

    results = wishlist.aggregate(pipeline)

    found = False

    for item in results:
        book = item["book"]
        print(f"{book['title']} by {book['author']} ({book['genre']})")
        found = True

    if not found:
        print("Wishlist is empty.")


# --------------------------------------------------
# Add book to wishlist
# --------------------------------------------------

def add_to_wishlist(books, customers, wishlist):

    customer_id = input("\nEnter customerId: ")

    if not customers.find_one({"customerId": customer_id}):
        print("Invalid customerId.")
        return

    try:
        book_id = int(input("Enter bookId: "))
    except ValueError:
        print("BookId must be a number.")
        return

    if not books.find_one({"bookId": book_id}):
        print("Book does not exist.")
        return

    if wishlist.find_one({"customerId": customer_id, "bookId": book_id}):
        print("Book already in wishlist.")
        return

    wishlist.insert_one({
        "customerId": customer_id,
        "bookId": book_id
    })

    print("Book added to wishlist.")


# --------------------------------------------------
# Remove book from wishlist
# --------------------------------------------------

def remove_from_wishlist(wishlist):

    customer_id = input("\nEnter customerId: ")

    try:
        book_id = int(input("Enter bookId: "))
    except ValueError:
        print("BookId must be a number.")
        return

    result = wishlist.delete_one({
        "customerId": customer_id,
        "bookId": book_id
    })

    if result.deleted_count > 0:
        print("Book removed from wishlist.")
    else:
        print("Wishlist item not found.")


# --------------------------------------------------
# Application Menu
# --------------------------------------------------

def menu(db):

    books = db["books"]
    customers = db["customers"]
    wishlist = db["wishlistitems"]

    while True:

        print("\n====== WhatABook Menu ======")
        print("1. View all books")
        print("2. View books by genre")
        print("3. View customer wishlist")
        print("4. Add book to wishlist")
        print("5. Remove book from wishlist")
        print("6. Exit")

        choice = input("\nSelect option: ")

        if choice == "1":
            display_books(books)

        elif choice == "2":
            display_books_by_genre(books)

        elif choice == "3":
            display_wishlist(customers, wishlist)

        elif choice == "4":
            add_to_wishlist(books, customers, wishlist)

        elif choice == "5":
            remove_from_wishlist(wishlist)

        elif choice == "6":
            print("\nGoodbye.")
            break

        else:
            print("Invalid selection.")


# --------------------------------------------------
# Program Entry Point
# --------------------------------------------------

def main():

    show_banner()

    db = connect_to_database()

    show_database_stats(db)

    menu(db)


if __name__ == "__main__":
    main()