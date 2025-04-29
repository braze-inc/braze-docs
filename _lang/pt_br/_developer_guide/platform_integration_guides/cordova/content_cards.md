---
nav_title: Cartões de conteúdo
article_title: Integração de cartões de conteúdo
page_order: 2
---

# Integração de cartões de conteúdo

> Saiba como integrar os cartões de conteúdo ao Cordova Braze SDK.

{% multi_lang_include cordova/prerequisites.md %}

## Feeds de cartões

O SDK do Braze inclui um feed de cartão padrão. Para mostrar o feed do cartão padrão, você pode usar o método `launchContentCards()`. Esse método lida com todos os rastreamentos de análises de dados, descartes e renderizações dos cartões de conteúdo de um usuário.

## Cartões de conteúdo

Você pode usar esses métodos adicionais para criar um feed de cartões de conteúdo personalizado em seu aplicativo:

|Método | Descrição |
|---|---|
|`requestContentCardsRefresh()`|Envia uma solicitação em segundo plano para solicitar os cartões de conteúdo mais recentes do servidor do SDK da Braze.|
|`getContentCardsFromServer(successCallback, errorCallback)`|Recupera os cartões de conteúdo do Braze SDK. Solicitará os cartões de conteúdo mais recentes do servidor e retornará a lista de cartões após a conclusão.|
|`getContentCardsFromCache(successCallback, errorCallback)`|Recupera os cartões de conteúdo do Braze SDK. Retornará a lista mais recente de cartões do cache local, que foi atualizada na última atualização.|
|`logContentCardClicked(cardId)`|Registra um clique para o Content Card ID fornecido.|
|`logContentCardImpression(cardId)`|Registra uma impressão para o ID do cartão de conteúdo fornecido.|
|`logContentCardDismissed(cardId)`|Registra um descarte de cartão para o cartão de conteúdo ID fornecido.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Suporte a GIF

{% multi_lang_include wrappers/gif_support/content_cards.md %}
