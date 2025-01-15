---
nav_title: Outras Integrações
article_title: Outras integrações
page_order: 6
---

# Outras integrações

> Estas são as outras integrações suportadas no Cordova Braze SDK.

{% multi_lang_include cordova/prerequisites.md %}

## Envio de mensagens no app

Por padrão, o Cordova SDK é compatível com mensagens no app sem alterações. Consulte os exemplos de integração do [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/integration/) ou [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/in-app_messaging/overview/) para obter informações sobre como personalizar mensagens no app. Além disso, você pode olhar o [aplicativo de amostra Cordova](https://github.com/braze-inc/braze-cordova-sdk/blob/master/sample-project/www/js/index.js) ou o exemplo de implementação de app para [Android](https://github.com/braze-inc/braze-android-sdk) ou [iOS](https://github.com/braze-inc/braze-swift-sdk).

### Suporte a GIF

{% multi_lang_include wrappers/gif_support/in_app_messaging.md %}

## Feed de notícias

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

Veja as instruções de integração do [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/news_feed/integration/) e [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/legacy_sdks/ios/news_feed/integration/) para obter informações sobre como integrar o feed de notícias no seu app Cordova. Alternativamente, nosso plugin Cordova oferece um método, `launchNewsFeed`, que lançará um feed de notícias modal sem integração adicional.

O SDK Braze Cordova possui vários métodos para obter o número de cartões de feed de notícias lidos ou não lidos para diferentes categorias. Confira uma [implementação de projeto de amostra](https://github.com/braze-inc/braze-cordova-sdk/blob/master/sample-project/www/js/index.js) para um exemplo.
