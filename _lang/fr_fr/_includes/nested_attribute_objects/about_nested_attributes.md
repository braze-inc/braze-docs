## À propos des attributs imbriqués

Les attributs imbriqués vous permettent de créer des segments plus riches et de personnaliser les messages à l'aide des données d'un seul objet d'attribut personnalisé.

Dans l'exemple suivant, l'attribut personnalisé `favorite_book` contient les attributs imbriqués `title`, `author` et `publishing_date`. Cet objet peut être utilisé pour cibler les utilisateurs par auteur, filtrer par date de publication ou insérer le titre du livre directement dans un message :

```json
"favorite_book": {
  "title": "The Hobbit",
  "author": "J.R.R. Tolkien",
  "publishing_date": "1937"
}
```