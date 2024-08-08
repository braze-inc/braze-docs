---
nav_title: Jetpack Compose
article_title: Jetpack Compose を使用した Android と FireOS のコンテンツカード統合
page_order: 1
platform: 
  - Android
  - FireOS
description: "このリファレンス記事では、Android または FireOS アプリケーションの Jetpack Compose を使用したコンテンツカード統合について説明します。"
channel:
  - content cards
search_rank: 1
---

# Jetpack Compose を使用したコンテンツカード

> このリファレンス記事では、Android または FireOS アプリケーションの Jetpack Compose を使用したコンテンツカード統合について説明します。

Android では、`ContentCardsList()`を使用して Compose アプリケーションにコンテンツカードフィードを追加できます。以下はその例です。

```kotlin
setContent {
    ContentCardsList()
}
```

### コンテンツカードのスタイリング

2つの方法のいずれかでスタイルを適用できます。1つ目は、次の例のように`ContentCardListStyling`と`ContentCardStyling`を`ContentCardsList()`に渡します。

```kotlin
ContentCardsList(
    style = ContentCardListStyling(listBackgroundColor = Color.Red),
    cardStyle = ContentCardStyling(
        titleTextStyle = TextStyle(
            fontFamily = fontFamily,
            fontSize = 25.sp
        ),
        shadowRadius = 10.dp,
        shortNewsContentCardStyle = BrazeShortNewsContentCardStyling(
            shadowRadius = 15.dp
        )
    )
)
```

2つ目は、次の例のように、`BrazeStyle`を使用して Braze コンポーネントのグローバルスタイルを作成することです。

```kotlin
BrazeStyle(
    contentCardStyle = ContentCardStyling(
        textAnnouncementContentCardStyle = BrazeTextAnnouncementContentCardStyling(
            cardBackgroundColor = Color.Red,
            descriptionTextStyle = TextStyle(
                fontFamily = fontFamily,
                fontSize = 25.sp,
            )
        ),
        titleTextColor = Color.Magenta
    )
) {
    // Your app here, including any ContentCardsList() in it
}
```

### さらなるカスタマイズ

#### カードのクリックを処理する

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

#### 却下の通知を有効にする

カードが却下されたときに通知を受けるには、`onCardDismissed`関数に関数を渡します。

```kotlin
ContentCardsList(
    onCardDismissed = { card ->
        // Do what you need with the card
    }
)
```
