## ネストされた属性について

ネストされた属性を使用すると、よりリッチなSegments を作成し、単一のカスタム属性 オブジェクトからのデータを使用してメッセージをカスタマイズできます。

次の例では、カスタム属性`favorite_book` には、ネストされた属性s `title`、`author`、および`publishing_date` が含まれます。このオブジェクトを使用すると、作成者がユーザーを対象にしたり、日付を公開してフィルターしたり、ブックのタイトルを直接メッセージに挿入したりできます。

```json
"favorite_book": {
  "title": "The Hobbit",
  "author": "J.R.R. Tolkien",
  "publishing_date": "1937"
}
```