## About nested attributes

Nested attributes let you build richer segments and personalize messages with data from a single custom attribute object.

In the following example, the custom attribute `favorite_book` contains the nested attributes `title`, `author`, and `publishing_date`. This object can be used to target users by author, filter by publishing date, or insert the book title directly into a message:

```json
"favorite_book": {
  "title": "The Hobbit",
  "author": "J.R.R. Tolkien",
  "publishing_date": "1937"
}
```