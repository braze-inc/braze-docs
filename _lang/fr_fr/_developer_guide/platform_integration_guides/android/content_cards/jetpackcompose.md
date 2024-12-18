---
nav_title: Jetpack Compose
article_title: Intégration de cartes de contenu pour Android et FireOS avec Jetpack Compose
page_order: 1
platform: 
  - Android
  - FireOS
description: "Cet article de référence traite de l'intégration des cartes de contenu à l'aide de Jetpack Compose pour votre application Android ou FireOS."
channel:
  - content cards
search_rank: 1
---

# Cartes de contenu avec Jetpack Compose

> Cet article de référence traite de l'intégration des cartes de contenu à l'aide de Jetpack Compose pour votre application Android ou FireOS.

Sous Android, vous pouvez ajouter le flux de cartes de contenu à votre application Compose à l'aide de `ContentCardsList()`. Par exemple :

```kotlin
setContent {
    ContentCardsList()
}
```

### Mise en forme des cartes de contenu

Vous pouvez appliquer la stylisation de deux manières. La première consiste à passer un `ContentCardListStyling` et un `ContentCardStyling` à un `ContentCardsList()`, comme dans l'exemple suivant :

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

La seconde consiste à utiliser `BrazeStyle` dans le but de créer un style global pour les composants de Braze, comme dans l'exemple suivant :

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

### Personnalisation plus poussée

#### Traitement des clics de carte

Pour gérer les clics de carte, transmettez une fonction qui prend une `Card` et renvoie un `Boolean` à `onCardClicked`. Si la valeur `true` est renvoyée, Braze ne traitera rien sur le clic à part sa consignation pour les analyses. Si la valeur `false` est renvoyée, Braze traitera le clic.

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

#### Activation des notifications de licenciement

Pour être informé du rejet d’une carte, transmettez une fonction à la fonction `onCardDismissed`.

```kotlin
ContentCardsList(
    onCardDismissed = { card ->
        // Do what you need with the card
    }
)
```
