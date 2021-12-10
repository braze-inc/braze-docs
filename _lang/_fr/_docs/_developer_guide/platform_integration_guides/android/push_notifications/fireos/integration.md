---
nav_title: Intégration
article_title: Intégration de Push pour FireOS
platform: Pare-feu
page_order: 0
page_type: Solution
description: "Cet article vous guide dans la façon d'intégrer les notifications push de Braze à votre application FireOS."
channel: Pousser
---

# Intégration

Une notification push est une alerte hors application qui apparaît à l'écran de l'utilisateur lorsqu'une mise à jour importante se produit. Les notifications push sont un moyen précieux de fournir à vos utilisateurs un contenu sensible au temps et pertinent ou de les réengager avec votre application.

> ADM (Amazon Device Messaging) n'est pas pris en charge sur les appareils non-Amazon. Pour tester Kindle Push vous devez avoir un appareil FireOS ([voir la liste Amazon des périphériques pris en charge][32]).

Consultez [la section Aide][8] pour les meilleures pratiques additionnelles.

Braze envoie des notifications push aux appareils Amazon en utilisant [Amazon Device Messaging (ADM)][14].

> La messagerie de l'appareil Amazon (ADM) est prise en charge __seulement__ sur les téléphones Feu et tablettes (à l'exception de la génération Kindle Fire 1er). Vous ne pouvez pas tester la messagerie ADM sur un appareil Android normal.

## Étape 1 : Activer l'ADM

- Créez un compte avec le [Amazon Apps & Games Developer Portal][10] si vous ne l'avez pas déjà fait.
- Obtenez les identifiants OAuth (Client ID et Client Secret) et une clé API ADM en suivant les instructions dans [Obtention des identifiants de messagerie Amazon][11].
- Ajoutez la ligne suivante à votre fichier `res/values/braze.xml` pour activer ADM:

  ```xml
  <bool name="com_appboy_push_adm_messaging_registration_enabled">vrai</bool>
  ```

## Étape 2 : Mettre à jour AndroidManifest.xml

- Dans votre application AndroidManifest.xml, ajoutez l'espace de noms d'Amazon à la balise `<>manifeste</>`.

  ```xml
  xmlns:<unk> ="http://schemas.Ω.com/apk/res/android"
  ```
- Déclarer les permissions requises pour supporter ADM en ajoutant `<>permission</>` et `<>uses-permission</>` éléments après le manifeste `<></> élément`.

  ```xml
  <manifest xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:amazon="http://schemas.amazon.com/apk/res/android"
    package="[YOUR PACKAGE NAME]"
    android:versionCode="1"
    android:versionName="1.0">

  <!-- Cette autorisation garantit qu'aucune autre application ne peut intercepter vos messages ADM. -->
  <permission
    android:name="[YOUR PACKAGE NAME].permission.RECEIVE_ADM_MESSAGE"
    android:protectionLevel="signature" />
  <uses-permission android:name="[YOUR PACKAGE NAME].permission.RECEIVE_ADM_MESSAGE" />

   <!-- Cette autorisation permet à votre application d'accéder à la réception de notifications push par ADM. -->
  <uses-permission android:name="com.amazon.device.messaging.permission.RECEIVE" />

  <!-- ADM utilise WAKE_LOCK pour empêcher le processeur de dormir quand un message est reçu. -->
  <uses-permission android:name="android.permission.WAKE_LOCK" />
    ...
  </manifest>
  ```

- Déclarer que votre application utilise la fonctionnalité ADM de l'appareil et déclarer que votre application est conçue pour rester fonctionnelle sans ADM présent sur l'appareil (android:required="false") en ajoutant un élément ★ :enable-fonctionnalité à l'élément d'application du manifeste.  Il est sûr de définir android:required à "false" car le code ADM de Braze se dégrade gracieusement lorsque l'ADM n'est pas présent sur l'appareil.

  ```xml
  ...
  <application
    android:icon="@drawable/ic_launcher"
    android:label="@string/app_name"
    android:theme="@style/AppTheme">

    <amazon:enable-feature android:name="com.amazon.device.messaging" android:required="false"/>
  ...
  ```
- Ajoutez des filtres d'intention pour gérer `INSCRIPTION` et `RECEVEZ` les effets de l'ADM dans le fichier `AndroidManifest.xml` de votre récepteur de diffusion Braze. Immédiatement après `文:enable-feature`, ajouter les éléments suivants :

  ```xml
  <receiver android:name="com.appboy.AppboyAdmReceiver" android:permission="com.amazon.device.messaging.permission.SEND">
    <intent-filter>
        <action android:name="com.amazon.device.messaging.intent.RECEIVE" />
        <action android:name="com.amazon.device.messaging.intent.REGISTRATION" />
        <category android:name="com.yourapp.packagename" />
    </intent-filter>
  </receiver>
  ```

## Étape 3 : Stockez votre clé API ADM

- Enregistrez votre clé API ADM dans un fichier nommé `api_key.txt` et sauvegardez-la dans le dossier `assets` de votre projet.
- Pour savoir comment obtenir une clé API ADM pour votre application, consultez la documentation d'Amazon sur [l'obtention d'une clé API ADM][11].
- Amazon ne reconnaîtra pas votre clé si `api_key.txt` contient des caractères d'espace blanc, comme un saut de ligne suivant.

## Étape 4 : Ajouter des liens profonds

#### Activation de l'ouverture automatique des liens profonds

Pour activer Braze pour ouvrir automatiquement votre application et tous les liens profonds quand une notification push est cliquée, mettez `com_appboy_handle_push_deep_links_automatically` à `true` dans votre `braze. ml`:

```
<bool name="com_appboy_handle_push_deep_links_automatically">vrai</bool>
```

Si vous souhaitez gérer des liens profonds, vous aurez besoin de créer un `BroadcastReceiver` qui écoute les messages reçus et ouverts de Braze. Reportez-vous à notre section sur [Recettes de Push et Ouvre][52] dans la documentation de push Android pour plus d'informations.

## Étape 5 : Ajouter le Client Secret et l'ID Client au tableau de bord Braze

Enfin, vous devez ajouter le Client Secret et l'ID Client que vous avez obtenu dans [Étape 1][2] à la page "Gérer les paramètres" du tableau de bord Braze comme illustré ci-dessous :

!\[Tableau de bord FireOS\]\[34\]

## Inscription manuelle de push
Si vous avez besoin de gérer l'enregistrement ADM vous-même, vous devriez faire ce qui suit :

- Dans [braze.xml][12] ajoutez ce qui suit :

  ```xml
  <!-- Cela désactivera l'enregistrement automatique pour ADM via le SDK Braze -->
  <bool name="com_appboy_push_adm_messaging_registration_enabled">faux</bool>
  ```
- Utilisez la méthode [registerPushToken()][37] pour passer l'ADM de votre utilisateur `registration_id` au Brésil :

  ```java
  Braze.getInstance(context).registerPushToken(registration_id);
  ```

> Braze ne recommande pas l'utilisation de l'enregistrement manuel si possible.

## ADM extras

Les utilisateurs peuvent envoyer des paires clé-valeur personnalisées avec un message push Kindle comme "extras" pour ["Deep Linking"][29], des urls de suivi, etc. Veuillez noter que, contrairement à Android push, les utilisateurs de Kindle push ne peuvent pas utiliser les clés réservées de Braze comme clés lors de la définition des paires "extra".

Les clés réservées comprennent :

- `_ab`
- `a`
- `cid`
- `p`
- `s`
- `t`
- `ttl`
- `uri`

Si une clé réservée de Kindle est détectée, Braze retourne le Code de Statut 400: Kindle Push Reserved Key Used.
[34]: {% image_buster /assets/img_archive/fire_os_dashboard.png %}


[2]: #step-1-enable-adm
[8]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/fireos/troubleshooting/
[10]: https://developer.amazon.com/public
[11]: https://developer.amazon.com/public/apis/engage/device-messaging/tech-docs/02-obtaining-adm-credentials
[11]: https://developer.amazon.com/public/apis/engage/device-messaging/tech-docs/02-obtaining-adm-credentials
[12]: https://developer.amazon.com/public/apis/engage/device-messaging/tech-docs/03-setting-up-adm
[14]: https://developer.amazon.com/public/apis/engage/device-messaging
[29]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/deep_linking/
[32]: https://developer.amazon.com/appsandservices/apis/engage/device-messaging/tech-docs/04-integrating-your-app-with-adm
[37]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/Appboy.html#registerPushToken-java.lang.String-
[52]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/#custom-handling-for-push-receipts-opens-dismissals-and-key-value-pairs
