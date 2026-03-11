/**
 * Title: Group3-whatABook-installation.js
 * Author: Group 3
 * Date: 3/11/2026
 * Description: MongoDB Shell script to build and seed the WhatABook database.
 *
 * How to run (mongosh):
 *   1) Connect to your cluster
 *   2) load("Group3-whatABook-installation.js")
 */

// ------------------------------
// Database Reset
// ------------------------------
const DB_NAME = "whatABookDB";
db = db.getSiblingDB(DB_NAME);

print(`\n--- Resetting database: ${DB_NAME} ---`);
db.dropDatabase();

// ------------------------------
// Seed Data
// ------------------------------
const books = [
  { bookId: 1001, title: "The Great Gatsby", genre: "Fiction", author: "F. Scott Fitzgerald" },
  { bookId: 1002, title: "Dune", genre: "Sci-Fi", author: "Frank Herbert" },
  { bookId: 1003, title: "Pride and Prejudice", genre: "Romance", author: "Jane Austen" },
  { bookId: 1004, title: "The Hobbit", genre: "Fantasy", author: "J.R.R. Tolkien" },
  { bookId: 1005, title: "1984", genre: "Dystopian", author: "George Orwell" },
  { bookId: 1006, title: "The Da Vinci Code", genre: "Mystery", author: "Dan Brown" },
  { bookId: 1007, title: "Sapiens", genre: "Nonfiction", author: "Yuval Noah Harari" },
  { bookId: 1008, title: "The Martian", genre: "Sci-Fi", author: "Andy Weir" }
];

const customers = [
  { customerId: "c1007", firstName: "Emily", lastName: "Carter" },
  { customerId: "c1008", firstName: "Lucas", lastName: "Andrade" },
  { customerId: "c1009", firstName: "Robert", lastName: "Martinez" }
];

// customerId + bookId pairs (wishlistitems collection)
const wishlistitems = [
  { customerId: "c1007", bookId: 1002 },
  { customerId: "c1007", bookId: 1004 },
  { customerId: "c1008", bookId: 1001 },
  { customerId: "c1008", bookId: 1008 },
  { customerId: "c1009", bookId: 1003 },
  { customerId: "c1009", bookId: 1005 }
];

// ------------------------------
// Inserts
// ------------------------------
print("\n--- Inserting books ---");
db.books.insertMany(books);

print("\n--- Inserting customers ---");
db.customers.insertMany(customers);

print("\n--- Inserting wishlist items ---");
db.wishlistitems.insertMany(wishlistitems);

// ------------------------------
// Indexes (helps queries + prevents duplicate IDs)
// ------------------------------
print("\n--- Creating indexes ---");

// Unique identifiers
db.books.createIndex({ bookId: 1 }, { unique: true });
db.customers.createIndex({ customerId: 1 }, { unique: true });

// Prevent the same customer from adding the same book twice
db.wishlistitems.createIndex({ customerId: 1, bookId: 1 }, { unique: true });

// Helpful lookup/search indexes
db.books.createIndex({ genre: 1 });
db.books.createIndex({ author: 1 });
db.books.createIndex({ title: 1 });

// ------------------------------
// Verification Output
// ------------------------------
print("\n--- Verification ---");
print(`Books: ${db.books.countDocuments()}`);
print(`Customers: ${db.customers.countDocuments()}`);
print(`Wishlist Items: ${db.wishlistitems.countDocuments()}`);

print("\n--- Sample book ---");
printjson(db.books.findOne({ bookId: 1002 }));

print("\n--- Install complete ---\n");