---
nav_title: Intégration
article_title: Intégration Cordova
platform: 
  - Cordova
  - iOS
  - Android
page_order: 1
page_type: reference
description: "Cet article couvre les étapes initiales de configuration du SDK pour les applications Android et FireOS fonctionnant sur Cordova."

---
 
# Intégration Cordova

## Définition d’un endpoint API personnalisé

Un endpoint API personnalisé peut être configuré via `config.xml`. Par exemple, pour utiliser l’endpoint de l’UE, voir ce qui suit :

#### Android
```
<platform name="android">
    ...
    <preference name="com.appboy.android_api_endpoint" value="sdk.fra-01.braze.eu" />
</platform>
```
#### iOS
```
<platform name="ios">
    ...
    <preference name="com.appboy.ios_api_endpoint" value="sdk.fra-01.braze.eu" />
</platform>
```

## Notifications push

Si vous utilisez la configuration par défaut du SDK Cordova, vous n’aurez pas à effectuer de nouveaux changements côté client. Pour les intégrations modifiées, voir les instructions d’intégration [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/) ou [iOS]({{ site.baseurl }}/developer_guide/platform_integration_guides/ios/push_notifications/integration/).

## Messagerie In-App

Le SDK Cordova prend en charge par défaut les messages in-app sans modification. Consultez les exemples d’intégration d’[Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/integration/) ou [iOS]({{ site.baseurl }}/developer_guide/platform_integration_guides/ios/in-app_messaging/overview/) pour plus d’informations sur la personnalisation des messages dans l’application. Vous pouvez en outre regarder l’[exemple d’application Cordova](https://github.com/Appboy/appboy-cordova-sdk/blob/master/sample-project/www/js/index.js), [Android](https://github.com/braze-inc/braze-android-sdk) ou [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/overview/) pour des modèles d’implémentation.

## Analytique

### Définir des ID utilisateur

Consultez les instructions d’intégration [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids/) et [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/setting_user_ids/) pour une explication approfondie sur le moment auquel définir et modifier un ID utilisateur.

```javascript
AppboyPlugin.changeUser("YOUR_USER_ID");
```

### Enregistrer des événements personnalisés

Consultez les instructions d’intégration [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_custom_events/#tracking-custom-events) et [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/tracking_custom_events/) pour une explication approfondie des meilleures pratiques de suivi des événements et des interfaces.

```javascript
var properties = {};
properties["KeyOne"] = "Val1";
AppboyPlugin.logCustomEvent("cordovaCustomEventWithProperties", properties);
```

### Définir des attributs personnalisés

Consultez les instructions d’intégration [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_custom_attributes/) et [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/setting_custom_attributes/) pour une explication approfondie des meilleures pratiques de suivi des attributs et des interfaces.

```javascript
AppboyPlugin.setFirstName("firstName");
```

### Enregistrer des achats

Consultez les instructions d’intégration [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/logging_purchases/#logging-purchases) et [iOS]({{ site.baseurl }}/developer_guide/platform_integration_guides/ios/analytics/logging_purchases/) pour une explication approfondie des meilleures pratiques de suivi des revenus et des interfaces.

```javascript
var properties = {};
properties["KeyOne"] = "ValueOne";
AppboyPlugin.logPurchase("product_id_with_null_currency", 10, null, 5, properties);
```

#### Journaliser les achats au niveau de la commande
Si vous souhaitez journaliser les achats au niveau de la commande au lieu du niveau de produit, vous pouvez utiliser le nom de la commande ou la catégorie de commande comme `product_id`. Consultez notre [spécification d’objet d’achat]({{site.baseurl}}/api/objects_filters/purchase_object/#product-id-naming-conventions) pour en savoir plus. 

## Fil d’actualité

Consultez les instructions d’intégration [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/news_feed/#news-feed) et [iOS]({{ site.baseurl }}/developer_guide/platform_integration_guides/ios/news_feed/) pour savoir comment intégrer le fil d’actualité dans votre application Cordova. Sinon, notre plugin Cordova propose une méthode, `launchNewsFeed`, qui lancera un fil d’actualité modal sans intégration supplémentaire. 

Le SDK Braze pour Cordova dispose de plusieurs méthodes pour obtenir le nombre de cartes de fil d'actualité lues ou non lues pour différentes catégories. Vous pouvez consulter un [exemple d’implémentation de projet](https://github.com/Appboy/appboy-cordova-sdk/blob/master/sample-project/www/js/index.js).
