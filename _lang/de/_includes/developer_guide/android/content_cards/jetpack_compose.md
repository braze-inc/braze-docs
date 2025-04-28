# Content-Cards mit Jetpack Compose

> Dieser Referenzartikel  behandelt die Content-Card-Integration mit Jetpack Compose für Ihre Android- oder FireOS-App.

In Android können Sie den Content-Card-Feed mit `ContentCardsList()` zu Ihrer Compose-Anwendung hinzufügen. Zum Beispiel:

```kotlin
setContent {
    ContentCardsList()
}
```

## Umgang mit Card-Klicks

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

## Aktivieren von Benachrichtigungen für Ausblendungen

Um benachrichtigt zu werden, wenn eine Card ausgeblendet entlassen wird, übergeben Sie eine Funktion an die Funktion `onCardDismissed`.

```kotlin
ContentCardsList(
    onCardDismissed = { card ->
        // Do what you need with the card
    }
)
```
