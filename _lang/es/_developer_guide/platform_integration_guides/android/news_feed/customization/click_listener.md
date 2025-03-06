---
nav_title: Manejar los clics manualmente
article_title: Manejar manualmente los clics en la fuente de noticias para Android y FireOS
page_order: 3
platform: 
  - Android
  - FireOS
description: "Este artículo de referencia explica cómo gestionar manualmente los clics en la fuente de noticias en tu aplicación Android o FireOS."
channel:
  - news feed
  
---

# Manejar los clics manualmente

> Este artículo de referencia explica cómo gestionar manualmente los clics en la fuente de noticias en tu aplicación Android o FireOS.

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

Puedes gestionar los clics de la Fuente de noticias manualmente configurando un receptor de clics de la Fuente de noticias personalizado. Esto habilita casos de uso como el uso selectivo del navegador web nativo para abrir enlaces web.

## Paso 1: Implementar una escucha de clics del canal de noticias

Crea una clase que implemente [`IFeedClickActionListener`](https://github.com/braze-inc/braze-android-sdk/blob/master/android-sdk-ui/src/main/java/com/braze/ui/feed/listeners/IFeedClickActionListener.java). Implementa el método `onFeedCardClicked()`, al que se llamará cuando el usuario haga clic en una tarjeta de canal de noticias.

## Paso 2: Ordena a Braze que utilice tu escucha de clics del canal de noticias

Una vez creado tu `IFeedClickActionListener`, llama a `BrazeFeedManager.getInstance().setFeedCardClickActionListener()` para indicar a `BrazeFeedManager` que utilice tu `IFeedClickActionListener` personalizado.

