/**
 * Title: Group3_whatABookQueries.js
 * Author: Group 3
 * Date: 3/11/2026
 * Description: Queries to showcase the WhatABook database.
 */

use("whatABookDB");

/*
 * Query 1: Display a list of books.
 */

print("\n--- Query 1: Display a list of books ---");

db.books.find({}, {
  _id: 0,
  bookId: 1,
  title: 1,
  genre: 1,
  author: 1
}).forEach(printjson);


/*
 * Query 2: Display a list of books by genre.
 * Example genre: Sci-Fi
 */

print("\n--- Query 2: Display books by genre (Sci-Fi) ---");

db.books.find({ genre: "Sci-Fi" }, {
  _id: 0,
  bookId: 1,
  title: 1,
  genre: 1,
  author: 1
}).forEach(printjson);


/*
 * Query 3: Display a list of books by author.
 * Example author: Jane Austen
 */

print("\n--- Query 3: Display books by author (Jane Austen) ---");

db.books.find({ author: "Jane Austen" }, {
  _id: 0,
  bookId: 1,
  title: 1,
  genre: 1,
  author: 1
}).forEach(printjson);


/*
 * Query 4: Display a book by bookId.
 * Example bookId: 1002
 */

print("\n--- Query 4: Display book by bookId (1002) ---");

printjson(
  db.books.findOne({ bookId: 1002 }, {
    _id: 0,
    bookId: 1,
    title: 1,
    genre: 1,
    author: 1
  })
);