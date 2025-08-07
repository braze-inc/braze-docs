---
nav_title: Andere Integrationen
article_title: Andere Integrationen
page_order: 6
---

# Andere Integrationen

> Dies sind die anderen Integrationen, die im Cordova Braze SDK unterstützt werden.

{% multi_lang_include cordova/prerequisites.md %}

## In-App-Nachrichten

Standardmäßig unterstützt das Cordova SDK In-App-Nachrichten ohne Änderungen. In den Beispielen für die [Android-]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/integration/) oder [iOS-Integration]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/in-app_messaging/overview/) finden Sie Informationen zur Anpassung von In-App-Nachrichten. Außerdem können Sie sich die [Beispiel-Cordova-Anwendung](https://github.com/braze-inc/braze-cordova-sdk/blob/master/sample-project/www/js/index.js) oder die [Beispiel-Android-](https://github.com/braze-inc/braze-android-sdk) oder [iOS-Anwendung](https://github.com/braze-inc/braze-swift-sdk) als Implementierungsbeispiele ansehen.

### GIF-Unterstützung

{% multi_lang_include wrappers/gif_support/in_app_messaging.md %}

## Newsfeed

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

In den Anleitungen zur [Android-]({{site.baseurl}}/developer_guide/platform_integration_guides/android/news_feed/integration/) und [iOS-Integration]({{site.baseurl}}/developer_guide/platform_integration_guides/legacy_sdks/ios/news_feed/integration/) finden Sie Informationen darüber, wie Sie den News Feed in Ihre Cordova-App integrieren. Alternativ dazu stellt das Cordova-Plugin die Methode `launchNewsFeed` bereit, die einen modalen Newsfeed ohne weitere Integration startet.

Das Braze Cordova SDK verfügt über mehrere Methoden, um die Anzahl der gelesenen oder ungelesenen Newsfeed-Cards für verschiedene Kategorien abzurufen. Sehen Sie sich ein [Beispiel für eine Projektimplementierung](https://github.com/braze-inc/braze-cordova-sdk/blob/master/sample-project/www/js/index.js) an.
