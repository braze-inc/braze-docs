## Über verschachtelte Attribute

Mit verschachtelten Attributen können Sie umfangreichere Segmente erstellen und Nachrichten mit Daten aus einem einzigen angepassten Attribut-Objekt personalisieren.

Im folgenden Beispiel enthält das angepasste Attribut `favorite_book` die verschachtelten Attribute `title`, `author`, und `publishing_date`. Mit diesem Objekt können Sie Nutzer:innen nach Autor zusammenstellen, nach dem Veröffentlichungsdatum filtern oder den Buchtitel direkt in eine Nachricht einfügen:

```json
"favorite_book": {
  "title": "The Hobbit",
  "author": "J.R.R. Tolkien",
  "publishing_date": "1937"
}
```