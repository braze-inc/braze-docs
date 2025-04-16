# Cartões de conteúdo com o Jetpack Compose

> Este artigo de referência aborda a integração de cartões de conteúdo usando o Jetpack Compose para seu app Android ou FireOS.

No Android, você pode adicionar o feed de cartões de conteúdo ao seu app Compose usando `ContentCardsList()`. Por exemplo:

```kotlin
setContent {
    ContentCardsList()
}
```

## Manuseio de cliques em cartões

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

## Ativação de notificações para demissões

Para receber uma notificação quando um cartão for descartado, passe uma função para a função `onCardDismissed`.

```kotlin
ContentCardsList(
    onCardDismissed = { card ->
        // Do what you need with the card
    }
)
```
