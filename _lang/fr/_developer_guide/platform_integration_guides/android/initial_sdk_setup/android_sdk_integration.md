---
nav_title: Intégration SDK Android
article_title: Intégration SDK Android pour Android et FireOS
page_order: 0
platform: 
  - Android
  - FireOS
description: "Cet article de référence explique comment intégrer le SDK Android à votre application Android ou FireOS."
search_rank: 4
---

# Intégration SDK Android

L’installation du SDK Braze vous fournira des fonctionnalités d’analytique de base ainsi que des messages in-app opérationnels avec lesquels vous pouvez engager vos utilisateurs.

{% alert note %}
Pour des performances optimales sur Android 12, nous recommandons de mettre à niveau vers le [SDK Braze pour Android v13.1.2 et ultérieurs](https://github.com/Appboy/appboy-android-sdk/blob/master/CHANGELOG.md#1312) dès que possible. Pour plus d’informations, consultez notre [Guide de mise à niveau vers Android 12]({{site.baseurl}}/developer_guide/platform_integration_guides/android/android_12/).
{% endalert %}

## Étape 1 : Intégrez la bibliothèque Braze

Le SDK Braze pour Android peut être intégré en option sans composants d’IU. Cependant, les cartes de contenu, et les messages in-app seront inutilisables, sauf si vous transmettez les données personnalisées à une IU que vous avez entièrement conçue. De plus, les notifications push ne fonctionneront pas parce que notre code de gestion de notification push se trouve dans la bibliothèque d’IU. Il est important de noter que ces éléments d’IU sont ouverts et entièrement personnalisables. Nous recommandons vivement l’intégration de ces fonctions. Reportez-vous à la documentation sur les [cartes de contenu]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/about/#advantages-of-using-content-cards) et les [messages in-app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/about/) pour voir une liste des avantages à utiliser chaque canal ou outil.

### Intégration de base

Pour accéder aux fonctions de messagerie de Braze, vous devez intégrer la bibliothèque d’IU. Consultez les instructions suivantes d’Android Studio pour l’intégration de la bibliothèque d’IU en fonction de votre EDI :

#### Ajouter notre référentiel

Dans votre projet de premier niveau `build.gradle`, ajoutez les éléments suivants comme référentiels dans **allprojects > repositories**. Par exemple :

```gradle
allprojects {
  repositories {
    google()
    maven { url "https://appboy.github.io/appboy-android-sdk/sdk" }
  }
}
```

{% alert note %}
Le kit SDK Braze pour Android utilise les dépendances Jetpack d’AndroidX à partir de la version 10.0.0 du SDK.
{% endalert %}

Vous pouvez également trouver directement les fichiers AAR d’artefact sur notre [référentiel Maven][71].

#### Ajouter une dépendance Braze

Ajouter la dépendance `android-sdk-ui` au `build.gradle` de votre application . 

Si vous utilisez une fonctionnalité de localisation ou Braze Geofence, incluez également le `android-sdk-location` dans le `build.gradle` de votre appli.

{% alert important %}
Si vous utilisez un Android SDK non natif (Flutter, Cordova, Unity, etc.), ce SDK a déjà la `android-sdk-ui` dépendance pour la version correcte de l’Android SDK. Ne mettez pas à jour la version manuellement.
{% endalert %}

```gradle
dependencies {
  implementation "com.braze:android-sdk-ui:+"
  implementation "com.braze:android-sdk-location:+"
}
```

L’exemple suivant montre où placer la ligne de dépendance dans votre `build.gradle`. Remarquez que la version utilisée dans l’exemple est ancienne. Consultez les [versions du SDK Braze pour Android][60] pour trouver la version la plus récente.

![Studio Android affichant le « build.gradle ». Dans cette capture d’écran, le code de dépendance est ajouté au bas du fichier.][32]

#### Synchronisation Gradle

Assurez-vous d’effectuer une synchronisation Gradle pour construire votre projet et d’incorporer les [ajouts de dépendance](#add-braze-dependency)..

![Studio Android affichant une bannière et un bouton en haut de l’application qui dit : « Les fichiers Gradle ont changé depuis la dernière synchronisation du projet. Une synchronisation de projet peut être nécessaire pour que l’EDI fonctionne correctement. Sync Now.»][38]

## Étape 2 : Configurer le SDK Braze en braze.xml

{% alert note %}
À partir de décembre 2019, les endpoints personnalisés ne sont plus fournis. Si vous disposez d’un endpoint personnalisé préexistant, vous pouvez continuer à l’utiliser. Pour plus de détails, consultez notre <a href="{{site.baseurl}}/api/basics/#endpoints">liste d'endpoints disponibles</a>.
{% endalert %}

Maintenant que les bibliothèques ont été intégrées, vous devez créer un fichier `braze.xml` dans le dossier `res/values` de votre projet. Si vous êtes sur un cluster de données spécifique ou disposez d’un endpoint personnalisé préexistant, vous devez également spécifier l’endpoint dans votre fichier `braze.xml`. 

Le contenu de ce fichier devrait ressembler à l’extrait de code suivant : Assurez-vous de remplacer `YOUR_APP_IDENTIFIER_API_KEY` avec l’identifiant trouvé dans la page **Manage Settings** du tableau de bord de Braze. Pour connaître votre cluster ou votre endpoint spécifique, demandez à votre gestionnaire du succès des clients ou ouvrez un [ticket de support][support].

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
<string name="com_braze_api_key">YOUR_APP_IDENTIFIER_API_KEY</string>
<string translatable="false" name="com_braze_custom_endpoint">YOUR_CUSTOM_ENDPOINT_OR_CLUSTER</string>
</resources>
```

## Étape 3 : Ajouter les autorisations requises au AndroidManifest.xml
Maintenant que vous avez ajouté votre clé API, vous devez ajouter les autorisations suivantes à votre `AndroidManifest.xml` :

```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
```

> Avec la sortie d’Android M, Android est passé d’un modèle d’autorisation de temps d’installation à un de temps d’exécution. Cependant, ces deux autorisations sont normales et accordées automatiquement si elles sont répertoriées dans le manifeste de l’application. Pour plus d’informations, consultez la [documentation Android sur les autorisations][46].

## Étape 4 : Suivre les sessions utilisateur dans Android

### Intégration de la fonction de rappel du cycle de vie de l’activité

Les appels vers `openSession()`, `closeSession()`, [`ensureSubscribedToInAppMessageEvents()`][64] et l’enregistrement `InAppMessageManager` sont gérés automatiquement de manière optionnelle.

#### Enregistrer les fonctions de rappel du cycle de vie des activités

Ajoutez le code suivant à la méthode `onCreate()` de votre classe `Application` :

{% tabs %}
{% tab JAVA %}

```java
public class MyApplication extends Application {
  @Override
  public void onCreate() {
    super.onCreate();
    registerActivityLifecycleCallbacks(new BrazeActivityLifecycleCallbackListener(sessionHandlingEnabled, inAppMessagingRegistrationEnabled));
  }
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
class MyApplication : Application() {
  override fun onCreate() {
    super.onCreate()
    registerActivityLifecycleCallbacks(BrazeActivityLifecycleCallbackListener(sessionHandlingEnabled, inAppMessagingRegistrationEnabled))
  }
}
```

{% endtab %}
{% endtabs %}

Le premier argument demande à l’écouteur de gérer les appels `openSession()` et `closeSession()`.
Le deuxième argument demande à l’écouteur de gérer les appels `registerInAppMessageManager()` et `unregisterInAppMessageManager()`.

Consultez notre [KDoc][63] pour plus d’informations. Notez que toute intégration manuelle de session non standard n’est pas entièrement prise en charge.

## Étape 5 : Activer le suivi de localisation

Si vous désirez activer le recueil de positions Braze, mettez à jour votre fichier `braze.xml` pour inclure `com_braze_enable_location_collection` et assurez-vous que sa valeur est définie sur `true` :

```xml
<bool name="com_braze_enable_location_collection">true</bool>
```

{% alert important %}
À partir de la version 3.6.0 du SDK Braze pour Android, le recueil de position Braze est désactivé par défaut.
{% endalert %}

## Intégration SDK terminée

Braze devrait maintenant pouvoir collecter des [données spécifiées depuis votre application]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/) et votre intégration de base devrait être terminée.

Consultez les articles suivants pour activer le [suivi des événements personnalisés]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_custom_events/), la [messagerie de notification push]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/), les [cartes de contenu]({{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/integration/) et la suite complète de fonctionnalités Braze.

[2]: {{site.baseurl}}/user_guide/introduction/
[32]: {% image_buster /assets/img_archive/androidstudio2.png %}
[38]: {% image_buster /assets/img_archive/androidstudio3.png %}
[46]: https://developer.android.com/training/permissions/index.html
[60]: https://github.com/Appboy/appboy-android-sdk/blob/master/CHANGELOG.md
[63]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-activity-lifecycle-callback-listener/index.html
[64]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/ensure-subscribed-to-in-app-message-events.html
[support]: {{site.baseurl}}/braze_support/
[71]: https://appboy.github.io/appboy-android-sdk/sdk/com/braze
