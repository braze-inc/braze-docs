---
nav_title: Intégration d'Android SDK
article_title: Intégration d'Android SDK pour Android/FireOS
page_order: 0
platform:
  - Android
  - Pare-feu
description: "Cet article de référence couvre la façon d'intégrer le SDK Android dans votre application Android."
---

# Intégration d'Android SDK

L'installation du Braze SDK vous fournira des fonctionnalités d'analyse de base ainsi que des messages dans l'application avec lesquels vous pouvez engager vos utilisateurs.

{% alert note %}
Pour des performances optimales sur Android 12, nous vous recommandons de passer à [Braze Android SDK v13.1.2+](https://github.com/Appboy/appboy-android-sdk/blob/master/CHANGELOG.md#1312) dès que possible. Pour plus d'informations, veuillez consulter notre [Guide de mise à niveau pour Android 12](https://www.braze.com/docs/developer_guide/platform_integration_guides/android/android_12/).
{% endalert %}

## Étape 1 : Intégrer la bibliothèque Braze

Le SDK Android Braze peut éventuellement être intégré sans composants d’interface utilisateur. Cependant, les cartes de contenu, les fils d'actualités et les messages intégrés seront rendus inopérants à moins que vous ne transmettiez les données personnalisées à une interface utilisateur uniquement de votre design. De plus, les notifications push ne fonctionneront pas parce que notre code de gestion des push est dans la bibliothèque de l'interface utilisateur. Veuillez noter que ces éléments de l'interface utilisateur sont open source et entièrement personnalisables. Nous recommandons fortement l'intégration de ces fonctionnalités. Veuillez vous référer au [guide de l'utilisateur Braze][2] pour les avantages d'utiliser les Cartes de contenu de Braze, le fil d'actualités et l'interface de message In-App.

### Intégration de base

Pour accéder aux fonctions de messagerie de Braze, vous devez intégrer la bibliothèque de l'interface utilisateur. Veuillez consulter les instructions Android suivantes pour intégrer la bibliothèque de l'interface utilisateur en fonction de votre IDE :

#### Ajouter notre dépôt

Dans votre projet de premier niveau `build.gradle`, ajoutez ce qui suit en tant que dépôts dans `tous les projets` -> `dépôts`.

Par exemple :

```gradle
allprojects {
  dépôts {
    google()
    maven { url "https://appboy.github.io/appboy-android-sdk/sdk" }
  }
 } }
```

{% alert note %}
Le SDK Android Braze utilise les dépendances AndroidX Jetpack depuis la version SDK 10.0.0.
{% endalert %}

Vous pouvez également trouver directement les fichiers AAR sur notre [dépôt maven][71].

#### Ajouter une dépendance Braze

Ajoutez la dépendance `android-sdk-ui` à votre application `build.gradle`:

```gradle
dépendances {
  implémentation "com.appboy:android-sdk-ui:+"
}
```

L'exemple ci-dessous montre où placer la ligne de dépendance dans votre `build.gradle`. Notez que la version utilisée dans l'exemple utilise une ancienne version. Veuillez visiter [Braze Android SDK Releases][60] pour la version la plus à jour du Braze Android SDK.

!\[MavenScreen2\]\[32\]

#### Effectuer la synchronisation de gradle

Assurez-vous d'effectuer une Gradle Sync pour construire votre projet et incorporer les ajouts de dépendances mentionnés ci-dessus.

!\[GradleSync\]\[38\]

## Étape 2 : Configurer le Braze SDK dans braze.xml

{% alert note %}
Notez qu'à partir de décembre 2019, les points de terminaison personnalisés ne sont plus donnés, si vous avez un point de terminaison personnalisé préexistant, vous pouvez continuer à l'utiliser. Pour plus de détails, reportez-vous à notre <a href="{{site.baseurl}}/api/basics/#endpoints">liste de terminaux disponibles</a>.
{% endalert %}

Maintenant que les bibliothèques ont été intégrées, vous devez créer un fichier `braze.xml` dans le dossier `res/values` de votre projet. Si vous êtes sur une grappe de données spécifique ou que vous avez un point de terminaison personnalisé préexistant, vous devez spécifier le point de terminaison dans votre frein `. ml` fichier aussi. Le contenu de ce fichier devrait ressembler à l'extrait de code suivant :

> Assurez-vous de remplacer votre [clé API d'identification de l'application]({{site.baseurl}}/api/api_key/#the-app-identifier-api-key) trouvée dans la page  **Paramètres** du tableau de bord de Braze par `VOTRE_APP_IDENTIFIER_API_KEY`. Pour connaître votre cluster ou votre point de terminaison spécifique, veuillez demander à votre Customer Success Manager ou ouvrir un [ticket de support][support].

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
<string name="com_appboy_api_key">YOU_APP_IDENTIFIER_API_KEY</string>
<string translatable="false" name="com_appboy_custom_endpoint">VOTRE_CUSTOM_ENDPOINT_OR_CLUSTER</string>
</resources>
```

## Étape 3 : Ajouter les permissions requises à AndroidManifest.xml
Maintenant que vous avez ajouté votre clé API, vous devez ajouter les permissions suivantes à votre `AndroidManifest.xml`:

```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
```

> Avec la sortie d'Android M, Android est passé d'un modèle d'autorisation d'installation à un modèle d'autorisation d'exécution. Cependant, ces deux autorisations sont des autorisations normales et sont accordées automatiquement si elles sont listées dans le manifeste de l'application. Pour plus d'informations, visitez la [documentation de permission][46] d'Android.

## Étape 4 : Suivi des sessions utilisateur sur Android

### Intégration de callback du cycle de vie de l'activité

Les appels à `openSession()`, `closeSession()`,[`ensureSubscribedToInAppMessageEvents()`][64], et `InAppMessageManager` l'enregistrement sont optionnellement gérés automatiquement.

#### Instructions
Ajoute le code suivant à la méthode `onCreate()` de votre classe d'application:

{% tabs %}
{% tab JAVA %}

```java
la classe publique MyApplication étend l'application {
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

Le premier argument indique au listener de gérer les appels `openSession()` et `closeSession()`. Le deuxième argument indique à l'écouteur de gérer les appels `registerInAppMessageManager()` et `unregisterInAppMessageManager()`.

Consultez le [KDoc][63] pour plus d'informations. Veuillez noter que toute intégration de session manuelle non standard n'est pas entièrement prise en charge.

## Étape 5 : Configuration personnalisée du point de terminaison {#step-5-optional-custom-endpoint-setup}

{% alert note %}
Notez qu'à partir de décembre 2019, les points de terminaison personnalisés ne sont plus donnés, si vous avez un point de terminaison personnalisé préexistant, vous pouvez continuer à l'utiliser. Pour plus de détails, reportez-vous à notre <a href="{{site.baseurl}}/api/basics/#endpoints">liste de terminaux disponibles</a>.
{% endalert %}

Votre représentant de Braze aurait déjà dû vous aviser du [bon terminaison]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/).

Pour mettre à jour le point de terminaison par défaut dans votre intégration des SDK Braze, veuillez ajouter le code suivant à votre `braze.xml`:

```xml
<string translatable="false" name="com_appboy_custom_endpoint">YOUR_CUSTOM_ENDPOINT_OR_CLUSTER</string>
```

## Étape 6 : Activer le suivi de localisation

Si vous souhaitez activer la collecte de l'emplacement de Braze, mettez à jour votre `brasier. ml` fichier à inclure `com_appboy_enable_location_collection` et s'assurer que sa valeur est définie à `true`.

```xml
<bool name="com_appboy_enable_location_collection">vrai</bool>
```

{% alert important %}
La collection d'emplacement Braze Android SDK 3.6.0 Braze est désactivée par défaut.
{% endalert %}

## Intégration du SDK terminée

Braze sera maintenant en mesure de collecter [données spécifiées de votre application]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/) et votre intégration de base devrait être terminée.

Veuillez consulter les sections suivantes afin d'activer [le suivi d'événements personnalisés]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_custom_events/#tracking-custom-events), [la messagerie push]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/), [Cartes de Contenu]({{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/overview/) et la [suite complète]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/) de fonctionnalités Braze.
[32]: {% image_buster /assets/img_archive/androidstudio2.png %} [38]: {% image_buster /assets/img_archive/androidstudio3.png %}

[2]: {{site.baseurl}}/user_guide/introduction/
[46]: https://developer.android.com/training/permissions/index.html
[60]: https://github.com/Appboy/appboy-android-sdk/releases
[63]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-activity-lifecycle-callback-listener/index.html
[64]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/index.html#ensureSubscribedToInAppMessageEvents-android.content.Context-
[support]: {{site.baseurl}}/braze_support/
[71]: https://appboy.github.io/appboy-android-sdk/sdk/com/braze
