# Tarjetas de contenido con Jetpack Compose

> En este artículo de referencia se cubre la integración de la tarjeta de contenido utilizando Jetpack Compose para tu aplicación Android o FireOS.

En Android, puedes añadir la fuente de la tarjeta de contenido a tu aplicación Compose utilizando `ContentCardsList()`. Por ejemplo:

```kotlin
setContent {
    ContentCardsList()
}
```

## Gestión de los clics de la tarjeta

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

## Habilitar las notificaciones de despido

Para recibir una notificación cuando se descarta una tarjeta, pasa una función a la función `onCardDismissed`.

```kotlin
ContentCardsList(
    onCardDismissed = { card ->
        // Do what you need with the card
    }
)
```
