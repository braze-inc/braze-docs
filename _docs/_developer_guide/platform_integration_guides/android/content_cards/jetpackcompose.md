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

In Android, the Content Card feed is available to add into your Compose application by simply adding `ContentCardList()`. 

```kotlin
setContent {
    ContentCardsList()
}
```

### Styling Content Cards
Styling can be applied in two ways. The first is to pass a `ContentCardListStyling` and `ContentCardStyling` to `ContentCardList()`

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

Alternatively, you can also use `BrazeStyle` to create a global styling that can be used for Braze components below it in the Compose tree.

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

#### Filtering content cards
When using Jetpack Compose, you can easily filter and sort the Content Cards by setting the `cardUpdateHandler` parameter. For example, to only show Short News Content Cards, you can use:

```kotlin
ContentCardsList(
    cardUpdateHandler = {
        it.filter { card -> card.cardType == CardType.SHORT_NEWS}
    }
) 
```

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

#### Handling card dismissal
To be notified when a card is dismissed, pass a function to the `onCardDismissed` function.

```kotlin
ContentCardsList(
    onCardDismissed = { card ->
        // Do what you need with the card
    }
)
```

#### Complete card customization
To handle ALL the aspects of rendering a card, pass a function to the `customCardComposer` that can take a card and then either compose it and return `true`, or return `false` and have the card rendered in the default manner. This can be useful is you want to render using a 3rd party library such as Lottie.

If you use this, you are responsible for handling all aspects of card rendering (unread, pinned, etc.). You also need to handle card clicks (See `BrazeContentCardUtils.handleCardClick`). For example, if you'd like to intercept cards and turn them into a basic marquee, you could do this:

```kotlin
// Moving this to a val to make the code easier to read
val myCustomCardRenderer: @Composable ((Card) -> Boolean) = { card ->
    if (card.extras.containsKey("marquee")) {
        val textCard = card as TextAnnouncementCard
        Box(
            Modifier
                .padding(10.dp)
                .fillMaxWidth()
                .background(color = Color.Red)
                .clickable {
                    BrazeContentCardUtils.handleCardClick(context, card, clickHandler)
                }
        ) {
            Text(
                modifier = Modifier
                    .align(Alignment.Center)
                    .fillMaxWidth()
                    .basicMarquee(iterations = Int.MAX_VALUE),
                fontSize = 35.sp,
                text = textCard.description
            )
        }
        true
    } else {
        false
    }
}
...
ContentCardsList(
    customCardComposer = myCustomCardRenderer
)

```