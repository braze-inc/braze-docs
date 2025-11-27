# Jetpack Compose を使用したコンテンツカード

> このリファレンス記事では、Android または FireOS アプリケーションの Jetpack Compose を使用したコンテンツカード統合について説明します。

Android では、`ContentCardsList()`を使用して Compose アプリケーションにコンテンツカードフィードを追加できます。以下に例を示します。

```kotlin
setContent {
    ContentCardsList()
}
```

## カードのクリックを処理する

カードのクリックを処理するには、`Card`を受け取り、`Boolean`を返す関数を`onCardClicked`に渡します。`true`が返された場合、Braze は分析用にログを取る以外に、クリックに対して何も処理しません。`false`が返された場合、Braze はクリックを処理します。

```kotlin
ContentCardsList(
    onCardClicked = { card ->
        if (card.extras.containsKey("mySpecialKey")) {
            // handle the click here
            true
        } else {
            // Let Braze handle the click
            false
        }
    }
)
```

## 却下の通知を有効にする

カードが却下されたときに通知を受けるには、`onCardDismissed`関数に関数を渡します。

```kotlin
ContentCardsList(
    onCardDismissed = { card ->
        // Do what you need with the card
    }
)
```
