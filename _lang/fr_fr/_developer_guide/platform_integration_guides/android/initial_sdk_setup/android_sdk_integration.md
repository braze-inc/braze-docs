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

> Cet article de référence explique comment intégrer le SDK Android à votre application Android ou FireOS. L’installation du SDK Braze vous fournira des fonctionnalités d’analyse de base ainsi que des messages in-app opérationnels avec lesquels vous pouvez engager vos utilisateurs.

{% alert note %}
Pour des performances optimales sur Android 12, nous vous recommandons de mettre à jour vers [Braze Android SDK v13.1.2+](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#1312) dès que possible. Pour plus d'informations, consultez notre [Guide de mise à niveau vers Android 12]({{site.baseurl}}/android_12/).
{% endalert %}

## Étape 1 : Intégrez la bibliothèque Braze

Le SDK Braze pour Android peut être intégré en option sans composants d’IU. Cependant, les cartes de contenu et les messages in-app seront rendus inutilisables, sauf si vous transmettez les données personnalisées à une IU qui est uniquement de votre conception. De plus, les notifications push ne fonctionneront pas parce que notre code de gestion de notification push se trouve dans la bibliothèque d’IU. Il est important de noter que ces éléments de l'interface utilisateur sont entièrement personnalisables. Nous recommandons vivement l’intégration de ces fonctions. Reportez-vous aux [cartes de contenu]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/about/#advantages-of-using-content-cards) et à la documentation des [messages in-app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/about/) pour obtenir une liste des avantages liés à l'utilisation de chaque canal ou outil.

### Intégration de base

Pour accéder aux fonctionnalités d'envoi de messages de Braze, vous devez intégrer la bibliothèque d'interface utilisateur. Consultez les instructions suivantes d’Android Studio pour l’intégration de la bibliothèque d’IU en fonction de votre EDI :

#### Ajouter une dépendance Braze

Ajouter la dépendance `android-sdk-ui` au `build.gradle` de votre application. 

Si vous utilisez un emplacement ou la fonctionnalité Braze Geofence, incluez également `android-sdk-location` dans le `build.gradle` de votre application.

{% alert important %}
Si vous utilisez un SDK Android non natif (par exemple, Flutter, Cordova, Unity, etc.), ce SDK possède déjà la dépendance `android-sdk-ui` pour la version correcte du SDK Android. Ne mettez pas à jour la version manuellement.
{% endalert %}

```gradle
dependencies {
  implementation "com.braze:android-sdk-ui:+"
  implementation "com.braze:android-sdk-location:+"
}
```

L’exemple suivant montre où placer la ligne de dépendance dans votre `build.gradle`. Remarquez que la version utilisée dans l’exemple est ancienne. Consultez les [versions du](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md) SDK Android de Braze pour obtenir la version la plus récente du SDK Android de Braze.

![Android studio affiche le fichier "build.gradle", avec le code de dépendance ajouté à la fin du fichier.]({% image_buster /assets/img_archive/androidstudio2.png %})

#### Effectuer la synchronisation de Gradle

Veillez à effectuer une synchronisation Gradle pour créer votre projet et intégrer les [ajouts de dépendances](#add-braze-dependency).

![Une bannière dans Android Studio indiquant : "Les fichiers Gradle ont changé depuis la dernière synchronisation du projet. Une synchronisation de projet peut être nécessaire pour que l’EDI fonctionne correctement. Sync Now".]({% image_buster /assets/img_archive/androidstudio3.png %})

## Étape 2 : Configurez le SDK de Braze dans braze.xml

{% alert note %}
À partir de décembre 2019, les endpoints personnalisés ne sont plus fournis. Si vous disposez d’un endpoint personnalisé préexistant, vous pouvez continuer à l’utiliser. Pour plus de détails, consultez notre <a href="{{site.baseurl}}/api/basics/#endpoints">liste d’endpoints disponibles</a>.
{% endalert %}

Maintenant que les bibliothèques ont été intégrées, vous devez créer un fichier `braze.xml` dans le dossier `res/values` de votre projet. Si vous êtes sur un cluster de données spécifique ou disposez d’un endpoint personnalisé préexistant, vous devez également spécifier l’endpoint dans votre fichier `braze.xml`. 

Le contenu de ce fichier devrait ressembler à l’extrait de code suivant : Veillez à remplacer `YOUR_APP_IDENTIFIER_API_KEY` par l'identifiant figurant dans la page **Gérer les paramètres** du tableau de bord Braze. Connectez-vous à [dashboard.braze.com](https://dashboard.braze.com) pour trouver [l’adresse de votre cluster]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints). 

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
<string name="com_braze_api_key">YOUR_APP_IDENTIFIER_API_KEY</string>
<string translatable="false" name="com_braze_custom_endpoint">YOUR_CUSTOM_ENDPOINT_OR_CLUSTER</string>
</resources>
```

## Étape 3 : Ajoutez les autorisations nécessaires à AndroidManifest.xml
Maintenant que vous avez ajouté votre clé API, vous devez ajouter les autorisations suivantes à votre `AndroidManifest.xml` :

```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
```

{% alert note %}
Avec la sortie d’Android M, Android est passé d’un modèle d’autorisation de temps d’installation à un de temps d’exécution. Cependant, ces deux autorisations sont normales et accordées automatiquement si elles sont répertoriées dans le manifeste de l’application. Pour plus d’informations, consultez la [documentation sur les autorisations](https://developer.android.com/training/permissions/index.html) d’Android.
{% endalert %}

## Étape 4 : Suivre les sessions utilisateur dans Android

### Intégration de la fonction de rappel du cycle de vie de l’activité

Les appels à `openSession()`, `closeSession()`,[`ensureSubscribedToInAppMessageEvents()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/ensure-subscribed-to-in-app-message-events.html)et `InAppMessageManager` sont automatiquement traités en option.

#### Enregistrer les fonctions de rappel du cycle de vie des activités

Ajoutez le code suivant à la méthode `onCreate()` de votre classe `Application` :

{% tabs %}
{% tab JAVA %}

```java
public class MyApplication extends Application {
  @Override
  public void onCreate() {
    super.onCreate();
    registerActivityLifecycleCallbacks(new BrazeActivityLifecycleCallbackListener());
  }
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
class MyApplication : Application() {
  override fun onCreate() {
    super.onCreate()
    registerActivityLifecycleCallbacks(BrazeActivityLifecycleCallbackListener())
  }
}
```

{% endtab %}
{% endtabs %}

Consultez la documentation de référence de notre SDK pour plus d'informations sur les paramètres disponibles pour la fonction [`BrazeActivityLifecycleCallbackListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-activity-lifecycle-callback-listener/index.html).

## Étape 5 : Activer le suivi de localisation

Si vous souhaitez activer la collecte d'emplacements/localisations de Braze, mettez à jour votre fichier `braze.xml` pour y inclure `com_braze_enable_location_collection` et assurez-vous que sa valeur est fixée à `true`:

```xml
<bool name="com_braze_enable_location_collection">true</bool>
```

{% alert important %}
À partir de la version 3.6.0 du SDK Braze pour Android, le recueil des données de localisation Braze est désactivé par défaut.
{% endalert %}

## Intégration SDK terminée

Braze sera maintenant en mesure de collecter les [données spécifiées de votre application]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/) et votre intégration de base devrait être terminée.

Consultez les articles suivants afin d'activer le [suivi des événements personnalisés]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_custom_events/), les [messages push]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/), les [cartes de contenu]({{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/integration/) et la suite complète des fonctionnalités de Braze.

