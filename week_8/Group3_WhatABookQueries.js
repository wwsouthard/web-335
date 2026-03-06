/**
 * Title: group3-whatabook.js
 * Author: Group 3
 * Date: 3/6/2026
 * Description: Queries to showcase the WhatABook database.
 */

use("whatABookDB");

/*
 * Query 1: Display a list of books.
 */
db.books.find({}, {
  _id: 0,
  bookId: 1,
  title: 1,
  genre: 1,
  author: 1
}).pretty();

/*
 * Query 2: Display a list of books by genre.
 * Example genre: Sci-Fi
 */
db.books.find({ genre: "Sci-Fi" }, {
  _id: 0,
  bookId: 1,
  title: 1,
  genre: 1,
  author: 1
}).pretty();

/*
 * Query 3: Display a list of books by author.
 * Example author: Jane Austen
 */
db.books.find({ author: "Jane Austen" }, {
  _id: 0,
  bookId: 1,
  title: 1,
  genre: 1,
  author: 1
}).pretty();

/*
 * Query 4: Display a book by bookId.
 * Example bookId: 1002
 */
db.books.findOne({ bookId: 1002 }, {
  _id: 0,
  bookId: 1,
  title: 1,
  genre: 1,
  author: 1
});