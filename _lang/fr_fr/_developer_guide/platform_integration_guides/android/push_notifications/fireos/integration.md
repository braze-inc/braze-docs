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

# Intégration de notifications push pour FireOS

> Cet article de référence vous explique comment intégrer les notifications push Braze dans votre application FireOS.

Une notification push est une alerte hors application qui apparaît sur l’écran de l’utilisateur lorsqu’une mise à jour importante se produit. Les notifications push constituent un moyen précieux de fournir à vos utilisateurs un contenu urgent et pertinent, ou de les réengager dans votre application.

ADM (Amazon Device Messaging) n’est pas pris en charge sur les appareils ne faisant pas partie d’Amazon. Pour tester Kindle push, vous devez disposer d'un [appareil sous FireOS.](https://developer.amazon.com/appsandservices/apis/engage/device-messaging/tech-docs/04-integrating-your-app-with-adm) Consultez notre [article d'aide]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/fireos/troubleshooting/) pour connaître d’autres bonnes pratiques.

Braze envoie des notifications push aux appareils Amazon à l'aide du [service Amazon Device Messaging (ADM).](https://developer.amazon.com/public/apis/engage/device-messaging)

## Étape 1 : Activer ADM

1. Créez un compte avec le [Portail des développeurs d'applications et de jeux Amazon](https://developer.amazon.com/public) si vous ne l'avez pas encore fait.
2. Obtenez les [identifiants OAuth (ID client et secret client) et une clé API ADM](https://developer.amazon.com/public/apis/engage/device-messaging/tech-docs/02-obtaining-adm-credentials).
3. Activez **Enregistrement ADM automatique activé** dans la fenêtre de configuration de Braze Unity. 
  - Vous pouvez également ajouter la ligne suivante à votre `res/values/braze.xml` pour activer l’enregistrement ADM :

  ```xml
  <bool name="com_braze_push_adm_messaging_registration_enabled">true</bool>
  ```

## Étape 2 : Mise à jour AndroidManifest.xml

Dans la page AndroidManifest.xml de votre application, ajoutez l'espace de noms Amazon à l'étiquette `<>manifest</>`:

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

  <!-- This permission verifies that no other application can intercept your ADM messages. -->
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
    <receiver
      android:name="com.braze.push.BrazeAmazonDeviceMessagingReceiver"
      android:exported="true"
      android:permission="com.amazon.device.messaging.permission.SEND">
      <intent-filter>
        <action android:name="com.amazon.device.messaging.intent.RECEIVE" />
        <action android:name="com.amazon.device.messaging.intent.REGISTRATION" />

        <category android:name="${applicationId}" />
      </intent-filter>
    </receiver>
```

## Étape 3 : Stocker votre clé API ADM

Enregistrez d’abord votre clé API ADM dans un fichier nommé `api_key.txt` et enregistrez-le dans le dossier [`Assets/Plugins/Android/assets`][54] de votre projet. Ensuite, [obtenez une clé API ADM pour votre application](https://developer.amazon.com/public/apis/engage/device-messaging/tech-docs/02-obtaining-adm-credentials).

Amazon ne reconnaîtra pas votre clé si `api_key.txt` contient des caractères blancs, comme un saut de ligne.

## Étape 4 : Ajouter des liens profonds

#### Activer l’ouverture automatique du lien profond

Pour permettre à Braze d’ouvrir automatiquement votre application et les liens profonds lorsqu’une notification push est cliquée, définissez `com_braze_handle_push_deep_links_automatically` sur `true` dans votre fichier `braze.xml` :

```
<bool name="com_braze_handle_push_deep_links_automatically">true</bool>
```

Si vous souhaitez gérer de manière personnalisée les liens profonds, vous devrez créer un rappel de poussée qui écoute les poussées reçues et les intentions d'ouverture de Braze. Pour plus d'informations, consultez la section [Gestion personnalisée des reçus et des ouvertures de push]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#android-push-listener-callback) dans la documentation Android push.

## Étape 5 : Ajoutez un secret client et un ID client au tableau de bord de Braze

Enfin, vous devez ajouter le Secret Client et l'ID Client que vous avez obtenus dans [l'Étape 1](#step-1-enable-adm) à la page **Gérer les paramètres** du tableau de bord de Braze.

![]({% image_buster /assets/img_archive/fire_os_dashboard.png %})

## Enregistrement manuel de la notification push

Braze ne recommande pas l'utilisation de l'enregistrement manuel, mais si vous devez gérer vous-même l'enregistrement de l'ADM, ajoutez ce qui suit dans votre fichier [braze.xml](https://developer.amazon.com/public/apis/engage/device-messaging/tech-docs/03-setting-up-adm):

```xml
<!-- This will disable automatic registration for ADM via the Braze SDK-->
<bool name="com_braze_push_adm_messaging_registration_enabled">false</bool>
```
Ensuite, utilisez [`Braze.setRegisteredPushToken()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/registered-push-token.html) pour transmettre l'ADM `registration_id` de votre utilisateur à Braze :

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

Les utilisateurs peuvent envoyer des paires clé-valeur personnalisées avec un message push Kindle comme `extras` pour les [liens profonds]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/deep_linking/), les URL de suivi, etc. Contrairement à la notification push Android, les utilisateurs de notification push Kindle ne peuvent pas utiliser les touches réservées de Braze en tant que clés lors de la définition des paires clé-valeur `extra`.

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

