---
nav_title: Manipulação manual de cliques
article_title: Manipulação manual de cliques no feed de notícias para Android e FireOS
page_order: 3
platform: 
  - Android
  - FireOS
description: "Este artigo de referência aborda como lidar manualmente com os cliques no feed de notícias em seu aplicativo para Android ou FireOS."
channel:
  - news feed
  
---

# Tratamento manual de cliques

> Este artigo de referência aborda como lidar manualmente com os cliques no feed de notícias em seu aplicativo para Android ou FireOS.

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

Você pode lidar com os cliques no feed de notícias manualmente, configurando um ouvinte de cliques no feed de notícias personalizado. Isso ativa casos de uso, como o uso seletivo do navegador da Web nativo para abrir links da Web.

## Etapa 1: Implementar um ouvinte de cliques no feed de notícias

Crie uma classe que implemente o [`IFeedClickActionListener`](https://github.com/braze-inc/braze-android-sdk/blob/master/android-sdk-ui/src/main/java/com/braze/ui/feed/listeners/IFeedClickActionListener.java). Implemente o método `onFeedCardClicked()`, que será chamado quando o usuário clicar em um cartão do feed de notícias.

## Etapa 2: Instrua a Braze a usar seu ouvinte de cliques do feed de notícias

Depois que seu `IFeedClickActionListener` for criado, chame `BrazeFeedManager.getInstance().setFeedCardClickActionListener()` para instruir `BrazeFeedManager` a usar seu `IFeedClickActionListener` personalizado.

