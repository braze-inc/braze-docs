---
nav_title: Jetpack Compose
article_title: Content Card Integration for Android and FireOS using Jetpack Compose
page_order: 1
platform: 
  - Android
  - FireOS
description: "This reference article covers the Content Card integration using Jetpack Compose for your Android or FireOS application."
channel:
  - content cards
search_rank: 1
---

# Content Cards with Jetpack Compose

> This reference article covers the Content Card integration using Jetpack Compose for your Android or FireOS application.

In Android, you can add the Content Card feed to your Compose application using `ContentCardsList()`. For example:

```kotlin
setContent {
    ContentCardsList()
}
```

### Styling Content Cards

You can apply styling in one of two ways. The first is to pass a `ContentCardListStyling` and `ContentCardStyling` to `ContentCardsList()`, like in the following example:

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

The second is to use `BrazeStyle` to create a global styling for Braze components, like in the following example:

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

### Further customization

#### Handling card clicks

To handle card clicks, pass in a function that takes a `Card` and returns a `Boolean` to `onCardClicked`. If `true` is returned, Braze will not process anything on the click besides logging it for analytics. If `false` is returned, Braze will handle the the click.

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

#### Enabling notifications for dismissals

To be notified when a card is dismissed, pass a function to the `onCardDismissed` function.

```kotlin
ContentCardsList(
    onCardDismissed = { card ->
        // Do what you need with the card
    }
)
```
