# Cartes de contenu avec Jetpack Compose

> Cet article de référence traite de l'intégration des cartes de contenu à l'aide de Jetpack Compose pour votre application Android ou FireOS.

Sous Android, vous pouvez ajouter le flux de cartes de contenu à votre application Compose à l'aide de `ContentCardsList()`. Par exemple :

```kotlin
setContent {
    ContentCardsList()
}
```

## Traitement des clics de carte

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

## Activation des notifications de licenciement

Pour être informé du rejet d’une carte, transmettez une fonction à la fonction `onCardDismissed`.

```kotlin
ContentCardsList(
    onCardDismissed = { card ->
        // Do what you need with the card
    }
)
```
