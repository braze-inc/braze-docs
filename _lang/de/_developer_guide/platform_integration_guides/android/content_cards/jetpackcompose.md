---
nav_title: Jetpack Komponieren
article_title: Content-Card Integration für Android und FireOS mit Jetpack Compose
page_order: 1
platform: 
  - Android
  - FireOS
description: "Dieser Referenzartikel  behandelt die Content-Card-Integration mit Jetpack Compose für Ihre Android- oder FireOS-App."
channel:
  - content cards
search_rank: 1
---

# Content-Cards mit Jetpack Compose

> Dieser Referenzartikel  behandelt die Content-Card-Integration mit Jetpack Compose für Ihre Android- oder FireOS-App.

In Android können Sie den Content-Card-Feed mit `ContentCardsList()` zu Ihrer Compose-Anwendung hinzufügen. Zum Beispiel:

```kotlin
setContent {
    ContentCardsList()
}
```

### Content-Cards gestalten

Es gibt zwei Möglichkeiten, einen Stil anzuwenden. Die erste besteht darin, `ContentCardListStyling` und `ContentCardStyling` wie im folgenden Beispiel an `ContentCardsList()` zu übergeben:

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

Die zweite Möglichkeit ist die Verwendung von `BrazeStyle`, um globale Stile für Braze-Komponenten zu erstellen, wie im folgenden Beispiel:

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

### Weitere Anpassungen

#### Umgang mit Card-Klicks

Um Klicks auf die Card zu verarbeiten, übergeben Sie eine Funktion, die eine `Card` annimmt und eine `Boolean` an `onCardClicked` zurückgibt. Wenn `true` zurückgegeben wird, verarbeitet Braze den Klick nicht weiter, sondern protokolliert ihn nur für Analytics. Wenn `false` zurückgegeben wird, wird Braze den Klick ausführen.

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

#### Aktivieren von Benachrichtigungen für Ausblendungen

Um benachrichtigt zu werden, wenn eine Card ausgeblendet entlassen wird, übergeben Sie eine Funktion an die Funktion `onCardDismissed`.

```kotlin
ContentCardsList(
    onCardDismissed = { card ->
        // Do what you need with the card
    }
)
```
