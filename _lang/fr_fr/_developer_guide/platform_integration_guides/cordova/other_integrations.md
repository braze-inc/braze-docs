---
nav_title: Autres intégrations
article_title: Autres intégrations
page_order: 6
---

# Autres intégrations

> Voici les autres intégrations prises en charge dans le SDK Braze Cordova.

{% multi_lang_include cordova/prerequisites.md %}

## Envoi de messages in-app

Le SDK Cordova prend en charge par défaut les messages in-app sans modification. Consultez les exemples d'intégration [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/integration/) ou [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/in-app_messaging/overview/) pour obtenir des informations sur la personnalisation des messages in-app. En outre, vous pouvez consulter l'[exemple d'application Cordova](https://github.com/braze-inc/braze-cordova-sdk/blob/master/sample-project/www/js/index.js) ou l'exemple d'application [Android](https://github.com/braze-inc/braze-android-sdk) ou [iOS](https://github.com/braze-inc/braze-swift-sdk) pour obtenir des exemples de mise en œuvre.

### Support GIF

{% multi_lang_include wrappers/gif_support/in_app_messaging.md %}

## Fil d’actualité

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

Consultez les instructions d'intégration pour [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/news_feed/integration/) et [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/legacy_sdks/ios/news_feed/integration/) pour savoir comment intégrer le fil d'actualité dans votre application Cordova. Sinon, notre plugin Cordova propose une méthode, `launchNewsFeed`, qui lancera un fil d’actualité modal sans intégration supplémentaire.

Le SDK Braze pour Cordova dispose de plusieurs méthodes pour obtenir le nombre de cartes de fil d'actualité lues ou non lues pour différentes catégories. Consultez un [exemple de mise en œuvre de projet](https://github.com/braze-inc/braze-cordova-sdk/blob/master/sample-project/www/js/index.js).
