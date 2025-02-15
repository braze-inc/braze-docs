# Content Cards with Jetpack Compose

> This reference article covers the Content Card integration using Jetpack Compose for your Android or FireOS application.

In Android, you can add the Content Card feed to your Compose application using `ContentCardsList()`. For example:

```kotlin
setContent {
    ContentCardsList()
}
```

## Handling card clicks

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

## Enabling notifications for dismissals

To be notified when a card is dismissed, pass a function to the `onCardDismissed` function.

```kotlin
ContentCardsList(
    onCardDismissed = { card ->
        // Do what you need with the card
    }
)
```
