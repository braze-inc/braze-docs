---
nav_title: Desativar o rastreamento do Web SDK
article_title: Desativar o rastreamento do Web SDK
platform: Web
page_order: 6
page_type: reference
description: "Este artigo aborda a desativação do rastreamento do Web SDK, incluindo por que, como e as implicações disso para a Web."

---

# Desativar rastreamento do Web SDK

{% multi_lang_include archive/web-v4-rename.md %}

> Para cumprir as normas de privacidade de dados, a atividade de rastreamento de dados no Web SDK pode ser interrompida completamente usando o método [`disableSDK()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#disablesdk). 

Este método sincronizará todos os dados registrados antes de `disableSDK()` ser chamado e fará com que todas as chamadas subsequentes ao Braze Web SDK para esta página e carregamentos futuros de páginas sejam ignoradas. Para retomar a coleta de dados, use o método [`enableSDK()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#enablesdk).

Se você deseja oferecer aos usuários a opção de parar o rastreamento, recomendamos criar uma página simples com dois links ou botões, um que chama `disableSDK()` quando clicado, e outro que chama `enableSDK()` para permitir que os usuários optem por voltar. Você pode usar esses controles para iniciar ou parar o rastreamento por meio de outros sub-processadores de dados também.

Note que o SDK da Braze não precisa ser inicializado para chamar `disableSDK()`, permitindo que você desative o rastreamento para usuários totalmente anônimos. Por outro lado, `enableSDK()` não inicializa o SDK da Braze, então você também deve chamar `initialize()` depois para ativar o rastreamento.
