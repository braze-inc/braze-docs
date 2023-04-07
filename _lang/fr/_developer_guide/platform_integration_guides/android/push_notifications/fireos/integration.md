---
nav_title: Intégration
article_title: Intégration de notifications push pour FireOS
platform: FireOS
page_order: 0
page_type: solution
description: "Cet article de référence vous explique comment intégrer les notifications push Braze dans votre application FireOS."
channel: push
search_rank: 0.9
---

# Intégration

Une notification push est une alerte hors application qui apparaît sur l’écran de l’utilisateur lorsqu’une mise à jour importante se produit. Les notifications push constituent un moyen précieux de fournir à vos utilisateurs un contenu urgent et pertinent, ou de les réengager dans votre application.

ADM (Amazon Device Messaging) n’est pas pris en charge sur les appareils ne faisant pas partie d’Amazon. Pour tester la notification push Kindle, vous devez avoir un [appareil FireOS][32]. Découvrez notre [article d’aide][8] pour de meilleures pratiques supplémentaires.

Braze envoie des notifications push aux appareils Amazon en utilisant [Amazon Device Messaging (ADM)][14].

## Étape 1 : Activer ADM

1. Créer un compte auprès du [Portail des développeurs des applications et des jeux Amazon][10] si vous ne l’avez pas déjà fait.
2. Obtenez les [identifiants OAuth (ID client et secret client) et une clé API ADM][11].
3. Activez **Enregistrement ADM automatique activé** dans la fenêtre de configuration de Braze Unity. 
  - Vous pouvez également ajouter la ligne suivante à votre `res/values/braze.xml` pour activer l’enregistrement ADM :

  ```xml
  <bool name="com_braze_push_adm_messaging_registration_enabled">true</bool>
  ```

## Étape 2 : Mettre à jour AndroidManifest.xml

Dans AndroidManifest.xml de votre application, ajoutez l’espace de nom d’Amazon à la balise `<>manifest</>` :

```xml
  xmlns:amazon="http://schemas.amazon.com/apk/res/android"
```

Ensuite, déclarez les autorisations requises pour prendre en charge ADM en ajoutant les éléments `<>permission</>` et `<>uses-permission</>` après le `<>manifest</> element` :

  ```xml
  <manifest xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:amazon="http://schemas.amazon.com/apk/res/android"
    package="[YOUR PACKAGE NAME]"
    android:versionCode="1"
    android:versionName="1.0">

  <!-- This permission ensures that no other application can intercept your ADM messages. -->
  <permission
    android:name="[YOUR PACKAGE NAME].permission.RECEIVE_ADM_MESSAGE"
    android:protectionLevel="signature" />
  <uses-permission android:name="[YOUR PACKAGE NAME].permission.RECEIVE_ADM_MESSAGE" />

   <!-- This permission allows your app access to receive push notifications from ADM. -->
  <uses-permission android:name="com.amazon.device.messaging.permission.RECEIVE" />

  <!-- ADM uses WAKE_LOCK to keep the processor from sleeping when a message is received. -->
  <uses-permission android:name="android.permission.WAKE_LOCK" />
    ...
  </manifest>
```

Ensuite, déclarez que votre application utilise la fonction ADM de l’appareil et que votre application est conçue pour rester fonctionnelle sans qu’ADM soit présent sur l’appareil (`android:required="false"`) en ajoutant un élément `amazon:enable-feature` à l’élément d’application du manifeste. Il est sans danger de régler `android:required` sur `"false"` parce que le code ADM de Braze se dégrade proprement lorsque ADM n’est pas présent sur l’appareil :

  ```xml
  ...
  <application
    android:icon="@drawable/ic_launcher"
    android:label="@string/app_name"
    android:theme="@style/AppTheme">

    <amazon:enable-feature android:name="com.amazon.device.messaging" android:required="false"/>
  ...
  ```

Enfin, ajoutez des filtres d’intention pour gérer les intentions `REGISTRATION` et `RECEIVE` d’ADM dans votre fichier `AndroidManifest.xml` Braze. Immédiatement après `amazon:enable-feature`, ajoutez les éléments suivants :

```xml
<receiver android:name="com.braze.push.BrazeAmazonDeviceMessagingReceiver" android:permission="com.amazon.device.messaging.permission.SEND">
  <intent-filter>
      <action android:name="com.amazon.device.messaging.intent.RECEIVE" />
      <action android:name="com.amazon.device.messaging.intent.REGISTRATION" />
      <category android:name="com.yourapp.packagename" />
  </intent-filter>
</receiver>
```

## Étape 3 : Stocker votre clé API ADM

Enregistrez d’abord votre clé API ADM dans un fichier nommé `api_key.txt` et enregistrez-le dans votre dossier [`Assets/Plugins/Android/assets`][54] de projet. Ensuite, [obtenez une clé API ADM pour votre application][11].

Amazon ne reconnaîtra pas votre clé si `api_key.txt` contient des caractères blancs, comme un saut de ligne.

## Étape 4 : Ajouter des liens profonds

#### Activer l’ouverture automatique du lien profond

Pour permettre à Braze d’ouvrir automatiquement votre application et les liens profonds lorsqu’une notification push est cliquée, définissez `com_braze_handle_push_deep_links_automatically` sur `true` dans votre fichier `braze.xml` :

```
<bool name="com_braze_handle_push_deep_links_automatically">true</bool>
```

Si vous souhaitez personnaliser la gestion des liens profonds, vous devrez créer une fonction de rappel de notification push qui écoute la réception de notifications push et l’ouverture des intentions Braze. Consultez la [gestion personnalisée des reçus et des ouvertures de notifications push][52] dans la documentation sur les notifications push Android pour plus d’informations.

## Étape 5 : Ajoutez un secret client et un ID client au tableau de bord de Braze

Enfin, vous devez ajouter le secret client et l’ID client que vous avez obtenu au cours de l’[étape 1][2] à la page **Manage Settings** du tableau de bord de Braze.

![][34]

## Enregistrement manuel de la notification push

Braze ne recommande pas d’utiliser l’enregistrement manuel, mais si vous devez gérer l’enregistrement ADM vous-même, ajoutez ce qui suit dans votre [braze.xml][12] :

```xml
<!-- This will disable automatic registration for ADM via the Braze SDK-->
<bool name="com_braze_push_adm_messaging_registration_enabled">false</bool>
```
Ensuite, utilisez [`Braze.setRegisteredPushToken()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/registered-push-token.html) pour transmettre l’ADM de votre utilisateur `registration_id` à Braze :

{% tabs local %}
{% tab Java %}

```java
Braze.getInstance(context).setRegisteredPushToken(registration_id);
```

{% endtab %}
{% tab Kotlin %}

```kotlin
Braze.getInstance(context).registeredPushToken = registration_id
```

{% endtab %}
{% endtabs %}

## Compléments ADM

Les utilisateurs peuvent envoyer des paires clé-valeur personnalisées avec un message de notification push Kindle en tant qu’`extras` pour la [création de liens profonds][29], suivre des URL, etc. Contrairement à la notification push Android, les utilisateurs de notification push Kindle ne peuvent pas utiliser les touches réservées de Braze en tant que clés lors de la définition des paires clé-valeur `extra`.

Les clés réservées comprennent :

- `_ab`
- `a`
- `cid`
- `p`
- `s`
- `t`
- `ttl`
- `uri`

Si une clé réservée Kindle est détectée, Braze retourne `Status Code 400: Kindle Push Reserved Key Used`.

[2]: #step-1-enable-adm
[8]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/fireos/troubleshooting/
[10]: https://developer.amazon.com/public
[11]: https://developer.amazon.com/public/apis/engage/device-messaging/tech-docs/02-obtaining-adm-credentials
[12]: https://developer.amazon.com/public/apis/engage/device-messaging/tech-docs/03-setting-up-adm
[14]: https://developer.amazon.com/public/apis/engage/device-messaging
[29]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/deep_linking/
[32]: https://developer.amazon.com/appsandservices/apis/engage/device-messaging/tech-docs/04-integrating-your-app-with-adm
[34]: {% image_buster /assets/img_archive/fire_os_dashboard.png %}
[52]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#android-push-listener-callback
