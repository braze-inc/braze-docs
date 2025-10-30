## Acerca de los atributos anidados

Los atributos anidados te permiten construir segmentos más ricos y personalizar mensajes con datos de un único objeto personalizado de atributo.

En el siguiente ejemplo, el atributo personalizado `favorite_book` contiene los atributos anidados `title`, `author` y `publishing_date`. Este objeto puede utilizarse para dirigirse a los usuarios por autor, filtrar por fecha de publicación o insertar el título del libro directamente en un mensaje:

```json
"favorite_book": {
  "title": "The Hobbit",
  "author": "J.R.R. Tolkien",
  "publishing_date": "1937"
}
```