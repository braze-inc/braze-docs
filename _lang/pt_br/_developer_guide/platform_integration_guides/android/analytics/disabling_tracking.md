---
nav_title: Desativar o rastreamento do SDK
article_title: Desativar a coleta de dados para Android e FireOS
platform: 
  - Android
  - FireOS
page_order: 8
description: "Este artigo mostra como desativar a coleta de dados para seu app Android ou FireOS."

---

# Desativar o rastreamento do SDK

> Este artigo mostra como desativar a coleta de dados para seu app Android ou FireOS.

Para cumprir as normas de privacidade de dados, a atividade de rastreamento de dados no SDK do Android pode ser interrompida completamente usando o método [`disableSDK()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/disable-sdk.html). Esse método fará com que todas as conexões de rede sejam canceladas, e o SDK da Braze não passará nenhum dado para os servidores da Braze. Para retomar a coleta de dados, use o método [`enableSDK()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/enable-sdk.html).

Além disso, você pode usar o método [`wipeData()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/wipe-data.html) para limpar completamente todos os dados do lado do cliente armazenados no dispositivo.

