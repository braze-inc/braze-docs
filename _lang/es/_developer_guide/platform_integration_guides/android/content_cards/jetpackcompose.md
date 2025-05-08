---
nav_title: Jetpack Compose
article_title: Integración de tarjetas de contenido para Android y FireOS mediante Jetpack Compose
page_order: 1
platform: 
  - Android
  - FireOS
description: "En este artículo de referencia se cubre la integración de la tarjeta de contenido utilizando Jetpack Compose para tu aplicación Android o FireOS."
channel:
  - content cards
search_rank: 1
---

# Tarjetas de contenido con Jetpack Compose

> En este artículo de referencia se cubre la integración de la tarjeta de contenido utilizando Jetpack Compose para tu aplicación Android o FireOS.

En Android, puedes añadir la fuente de la tarjeta de contenido a tu aplicación Compose utilizando `ContentCardsList()`. Por ejemplo:

```kotlin
setContent {
    ContentCardsList()
}
```

### Estilización de las tarjetas de contenido

Puedes aplicar el estilizado de dos formas. La primera consiste en pasar un `ContentCardListStyling` y un `ContentCardStyling` a `ContentCardsList()`, como en el ejemplo siguiente:

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

La segunda es utilizar `BrazeStyle` para crear un estilo global para los componentes de Braze, como en el siguiente ejemplo:

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

### Más personalización

#### Gestión de los clics de la tarjeta

Para gestionar los clics de las tarjetas, pasa una función que tome un `Card` y devuelva un `Boolean` a `onCardClicked`. Si se devuelve `true`, Braze no procesará nada del clic aparte de registrarlo para análisis. Si se devuelve `false`, Braze se encargará del clic.

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

#### Habilitar las notificaciones de despido

Para recibir una notificación cuando se descarta una tarjeta, pasa una función a la función `onCardDismissed`.

```kotlin
ContentCardsList(
    onCardDismissed = { card ->
        // Do what you need with the card
    }
)
```
