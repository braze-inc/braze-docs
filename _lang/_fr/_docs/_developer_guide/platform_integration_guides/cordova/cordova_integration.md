---
nav_title: Intégration de Cordova
article_title: Intégration de Cordova
platform:
  - Cordova
  - iOS
  - Android
page_order: 1
page_type: Référence
description: "Cet article couvre les étapes initiales de configuration du SDK pour les applications Android et FireOS exécutées sur Cordova."
---

# Intégration de Cordova

## Définition d'un point de terminaison API personnalisé

Un point de terminaison personnalisé de l'API peut être configuré via le `config.xml`. Par exemple, pour utiliser le point de terminaison de l'UE, voyez ce qui suit:

{% tabs %}
{% tab Android %}

```
<platform name="android">
    ...
    <preference name="com.appboy.android_api_endpoint" value="sdk.fra-01.braze.eu" />
</platform>
```
{% endtab %}
{% tab iOS %}

```
<platform name="ios">
    ...
    <preference name="com.appboy.ios_api_endpoint" value="sdk.fra-01.braze.eu" />
</platform>
```
{% endtab %}
{% endtabs %}

## Notifications push

Si vous utilisez la configuration par défaut de Cordova SDK, vous n'aurez pas à faire de nouveaux changements côté client. Pour les intégrations modifiées, consultez les instructions d'intégration [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/) ou [iOS]({{ site.baseurl }}/developer_guide/platform_integration_guides/ios/push_notifications/integration/).

## Messagerie intégrée
{% tabs %}
{% tab Android %}
Par défaut, le SDK Cordova prend en charge les messages dans l'application sans aucune modification. Voir [les instructions d'intégration Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/integration/) pour plus d'informations sur la personnalisation des messages dans l'application. En outre, vous pouvez regarder le [exemple d'application Cordova](https://github.com/Appboy/appboy-cordova-sdk/blob/master/sample-project/www/js/index.js) ou le [exemple d'application Android](https://github.com/Appboy/appboy-android-sdk) pour des exemples d'implémentation.
{% endtab %}
{% tab iOS %}
Par défaut, le SDK Cordova prend en charge les messages dans l'application sans aucune modification. Voir [les instructions d'intégration iOS]({{ site.baseurl }}/developer_guide/platform_integration_guides/ios/in-app_messaging/overview/) pour plus d'informations sur la personnalisation des messages dans l'application. En outre, vous pouvez regarder le [exemple d'application Cordova](https://github.com/Appboy/appboy-cordova-sdk/blob/master/sample-project/www/js/index.js) ou le [exemple d'application iOS](https://github.com/Appboy/appboy-ios-sdk) pour des exemples d'implémentation.
{% endtab %}
{% endtabs %}

## Analyses

### Paramétrage des identifiants d'utilisateur

Consultez les instructions d'intégration [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids/) et [iOS]({{ site.baseurl }}/developer_guide/platform_integration_guides/ios/analytics/setting_user_ids/) pour une discussion approfondie sur le moment de définir et de modifier un ID d'utilisateur.

```javascript
AppboyPlugin.changeUser("VOTRE_USER_ID");
```

### Journalisation des événements personnalisés

Consultez les instructions d'intégration [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_custom_events/#tracking-custom-events) et [iOS]({{ site.baseurl }}/developer_guide/platform_integration_guides/ios/analytics/tracking_custom_events/) pour une discussion approfondie sur les meilleures pratiques et interfaces de suivi des événements.

```javascript
var properties = {};
properties["KeyOne"] = "Val1";
AppboyPlugin.logCustomEvent("cordovaCustomEventWithProperties", properties);
```

### Paramétrage des attributs personnalisés

Consultez les instructions d'intégration [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_custom_attributes/) et [iOS]({{ site.baseurl }}/developer_guide/platform_integration_guides/ios/analytics/setting_custom_attributes/) pour une discussion approfondie sur les meilleures pratiques et interfaces de suivi des attributs.

```javascript
AppboyPlugin.setFirstName("firstName");
```

### Achats de journalisation

Consultez les instructions d'intégration [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/logging_purchases/#logging-purchases) et [iOS]({{ site.baseurl }}/developer_guide/platform_integration_guides/ios/analytics/logging_purchases/) pour une discussion approfondie sur les meilleures pratiques et interfaces de suivi des revenus.

```javascript
var properties = {};
properties["KeyOne"] = "ValueOne";
AppboyPlugin.logPurchase("testPurchaseWithNullCurrency", 10, null, 5, properties);
```

## Flux d'actualité

Consultez les instructions d'intégration [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/news_feed/#news-feed) et [iOS]({{ site.baseurl }}/developer_guide/platform_integration_guides/ios/news_feed/) pour plus d'informations sur la façon d'intégrer le flux d'actualités dans votre application Cordova. Alternativement, notre plugin Cordova fournit une méthode, `launchNewsFeed`, qui lancera un flux d'actualités modal sans plus d'intégration.

Le Braze Cordova SDK a plusieurs méthodes pour obtenir le nombre de cartes de flux de nouvelles lues/non lues pour différentes catégories. Voir notre [exemple de mise en œuvre de projet](https://github.com/Appboy/appboy-cordova-sdk/blob/master/sample-project/www/js/index.js) pour un exemple.

Vous pouvez regarder l'échantillon d'application [Android](https://github.com/Appboy/appboy-android-sdk) ou [iOS](https://github.com/Appboy/appboy-ios-sdk) et tester Cordova Android](https://github.com/Appboy/appboy-android-sdk) ou [iOS](https://github.com/Appboy/appboy-ios-sdk) implémentations d'applications.
