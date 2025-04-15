---
nav_title: Jetpack Compose
article_title: Integração de cartões de conteúdo para Android e FireOS usando o Jetpack Compose
page_order: 1
platform: 
  - Android
  - FireOS
description: "Este artigo de referência aborda a integração de cartões de conteúdo usando o Jetpack Compose para seu app Android ou FireOS."
channel:
  - content cards
search_rank: 1
---

# Cartões de conteúdo com o Jetpack Compose

> Este artigo de referência aborda a integração de cartões de conteúdo usando o Jetpack Compose para seu app Android ou FireOS.

No Android, você pode adicionar o feed de cartões de conteúdo ao seu app Compose usando `ContentCardsList()`. Por exemplo:

```kotlin
setContent {
    ContentCardsList()
}
```

### Estilização de cartões de conteúdo

Você pode aplicar o estilo de duas maneiras. A primeira é passar `ContentCardListStyling` e `ContentCardStyling` para `ContentCardsList()`, como no exemplo a seguir:

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

A segunda é usar `BrazeStyle` para criar um estilo global para os componentes da Braze, como no exemplo a seguir:

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

### Personalização adicional

#### Manuseio de cliques em cartões

Para lidar com cliques em cartões, passe uma função que receba um `Card` e retorne um `Boolean` para `onCardClicked`. Se retornar `true`, a Braze não processará nada sobre o clique, além de registrá-lo para análise de dados. Se retornar `false`, a Braze tratará o clique.

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

#### Ativação de notificações para demissões

Para receber uma notificação quando um cartão for descartado, passe uma função para a função `onCardDismissed`.

```kotlin
ContentCardsList(
    onCardDismissed = { card ->
        // Do what you need with the card
    }
)
```
