## Sobre atributos aninhados

Atributos aninhados permitem que você construa segmentos mais ricos e personalize mensagens com dados de um único objeto de atributo personalizado.

No exemplo a seguir, o atributo personalizado `favorite_book` contém os atributos aninhados `title`, `author` e `publishing_date`. Este objeto pode ser usado para segmentar usuários por autor, filtrar por data de publicação ou inserir o título do livro diretamente em uma mensagem:

```json
"favorite_book": {
  "title": "The Hobbit",
  "author": "J.R.R. Tolkien",
  "publishing_date": "1937"
}
```