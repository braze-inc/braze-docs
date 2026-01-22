## Intégration du SDK Android

### Étape 1 : Mettez à jour votre `build.gradle`

Dans votre `build.gradle`, ajoutez [`mavenCentral()`](https://docs.gradle.org/current/kotlin-dsl/gradle/org.gradle.api.artifacts.dsl/-repository-handler/maven-central.html) à votre liste de dépôts.

```kotlin
repositories {
  mavenCentral()
}
```

Ensuite, ajoutez Braze à vos dépendances.

{% tabs local %}
{% tab base uniquement %}
Si vous ne prévoyez pas d'utiliser les composants de l'interface utilisateur de Braze, ajoutez le code suivant à votre site `build.gradle`. Remplacez `SDK_VERSION` par la version actuelle de votre SDK Braze Android. Pour obtenir la liste complète des versions, consultez le [journal des modifications]({{site.baseurl}}/developer_guide/changelogs/?sdktab=android).

```kotlin
dependencies {
    implementation 'com.braze:android-sdk-base:SDK_VERSION' // (Required) Adds dependencies for the base Braze SDK.
    implementation 'com.braze:android-sdk-location:SDK_VERSION' // (Optional) Adds dependencies for Braze location services.
}
```
{% endtab %}

{% tab avec des composants ui %}
Si vous prévoyez d'utiliser ultérieurement les composants de l'interface utilisateur de Braze, ajoutez le code suivant à votre site `build.gradle`.  Remplacez `SDK_VERSION` par la version actuelle de votre SDK Braze Android. Pour obtenir la liste complète des versions, consultez le [journal des modifications]({{site.baseurl}}/developer_guide/changelogs/?sdktab=android).

```kotlin
dependencies {
    implementation 'com.braze:android-sdk-ui:SDK_VERSION' // (Required) Adds dependencies for the Braze SDK and Braze UI components. 
    implementation 'com.braze:android-sdk-location:SDK_VERSION' // (Optional) Adds dependencies for Braze location services.
}
```
{% endtab %}
{% endtabs %}

### Étape 2 : Configurez votre `braze.xml`

{% alert note %}
À partir de décembre 2019, les endpoints personnalisés ne sont plus fournis. Si vous disposez d’un endpoint personnalisé préexistant, vous pouvez continuer à l’utiliser. Pour plus de détails, consultez notre <a href="{{site.baseurl}}/api/basics/#endpoints">liste d’endpoints disponibles</a>.
{% endalert %}

Créez un fichier `braze.xml` dans le dossier `res/values` de votre projet. Si vous êtes sur un cluster de données spécifique ou disposez d’un endpoint personnalisé préexistant, vous devez également spécifier l’endpoint dans votre fichier `braze.xml`. 

Le contenu de ce fichier devrait ressembler à l’extrait de code suivant : Veillez à remplacer `YOUR_APP_IDENTIFIER_API_KEY` par l'identifiant figurant dans la page **Gérer les paramètres** du tableau de bord Braze. Connectez-vous à [dashboard.braze.com](https://dashboard.braze.com) pour trouver [l’adresse de votre cluster]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints). 

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
  <string translatable="false" name="com_braze_api_key">YOUR_APP_IDENTIFIER_API_KEY</string>
  <string translatable="false" name="com_braze_custom_endpoint">YOUR_CUSTOM_ENDPOINT_OR_CLUSTER</string>
</resources>
```

### Étape 3 : Ajoutez des autorisations à `AndroidManifest.xml`

Ensuite, ajoutez les permissions suivantes à votre `AndroidManifest.xml`:

```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
```

{% alert note %}
Avec la sortie d’Android M, Android est passé d’un modèle d’autorisation de temps d’installation à un de temps d’exécution. Cependant, ces deux autorisations sont normales et accordées automatiquement si elles sont répertoriées dans le manifeste de l’application. Pour plus d’informations, consultez la [documentation sur les autorisations](https://developer.android.com/training/permissions/index.html) d’Android.
{% endalert %}

### Étape 4 : Activer l'initialisation différée (optionnel)

Pour utiliser l'initialisation différée, la version minimale du SDK de Braze est requise :

{% sdk_min_versions android:38.0.0 %}

{% alert note %}
Lorsque l'initialisation différée est activée, toutes les connexions réseau sont annulées, ce qui empêche le SDK d'envoyer des données aux serveurs de Braze.
{% endalert %}

#### Étape 4.1 : Mettez à jour votre `braze.xml`

L'initialisation différée est désactivée par défaut. Pour l'activer, utilisez l'une des options suivantes :

{% tabs %}
{% tab Fichier XML de Braze %}
Dans le fichier `braze.xml` de votre projet, définissez `com_braze_enable_delayed_initialization` comme `true`.

```xml
<bool name="com_braze_enable_delayed_initialization">true</bool>
```
{% endtab %}

{% tab Au moment de l'exécution %}
Pour activer l'initialisation différée au moment de l'exécution, utilisez la méthode suivante.

{% subtabs %}
{% subtab JAVA %}

```java
Braze.enableDelayedInitialization(context);
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.enableDelayedInitialization(context)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

#### Étape 4.2 : Configurer l'analyse/analytique push (facultatif)

Lorsque l'initialisation différée est activée, les analyses/analytiques push sont mises en file d'attente par défaut. Cependant, vous pouvez choisir de [mettre explicitement en file d'attente](#explicitly-queue-push-analytics) ou d'[abandonner l'](#drop-push-analytics) analyse/analytique push (si vous utilisez l'analyse/analytique push).

##### File d'attente explicite {#explicitly-queue-push-analytics}

Pour mettre explicitement en file d'attente l'analyse/analytique push, choisissez l'une des options suivantes :

{% tabs %}
{% tab Fichier XML de Braze %}
Dans votre fichier `braze.xml`, définissez `com_braze_delayed_initialization_analytics_behavior` comme `QUEUE`:

```xml
<string name="com_braze_delayed_initialization_analytics_behavior">QUEUE</string>
```
{% endtab %}

{% tab Au moment de l'exécution %}
Ajoutez `QUEUE` à votre [`Braze.enableDelayedInitialization()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/enable-delayed-initialization.html) méthode :

{% subtabs %}
{% subtab JAVA %}

```java
Braze.enableDelayedInitialization(context, DelayedInitializationAnalyticsBehavior.QUEUE);
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.enableDelayedInitialization(context, DelayedInitializationAnalyticsBehavior.QUEUE)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

##### Chute {#drop-push-analytics}

Pour abandonner l'analyse/analytique push, choisissez l'une des options suivantes :

{% tabs %}
{% tab Fichier XML de Braze %}
Dans votre fichier `braze.xml`, définissez `com_braze_delayed_initialization_analytics_behavior` comme `DROP`: 

```xml
<string name="com_braze_delayed_initialization_analytics_behavior">DROP</string>
```
{% endtab %}

{% tab Au moment de l'exécution %}
Ajoutez `DROP` à la [`Braze.enableDelayedInitialization()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/enable-delayed-initialization.html) méthode :

{% subtabs %}
{% subtab JAVA %}

```java
Braze.enableDelayedInitialization(context, DelayedInitializationAnalyticsBehavior.DROP);
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.enableDelayedInitialization(context, DelayedInitializationAnalyticsBehavior.DROP)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

#### Étape 4.3 : Initialiser manuellement le SDK

Après le délai que vous avez choisi, utilisez la méthode [`Braze.disableDelayedInitialization()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/disable-delayed-initialization.html) pour initialiser manuellement le SDK.

{% tabs local %}
{% tab JAVA %}

```java
Braze.disableDelayedInitialization(context);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.disableDelayedInitialization(context)
```

{% endtab %}
{% endtabs %}

### Étape 5 : Activer le suivi de la session de l'utilisateur

Lorsque vous activez le suivi des sessions utilisateur, les appels à `openSession()`, `closeSession()`,[`ensureSubscribedToInAppMessageEvents()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/ensure-subscribed-to-in-app-message-events.html)et `InAppMessageManager` peuvent être traités automatiquement.

Pour enregistrer les rappels de cycle de vie des activités, ajoutez le code suivant à la méthode `onCreate()` de votre classe `Application`. 

{% tabs local %}
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

Pour la liste des paramètres disponibles, voir [`BrazeActivityLifecycleCallbackListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-activity-lifecycle-callback-listener/index.html).

{% endtab %}
{% endtabs %}

## Tester le suivi de session

{% alert tip %}
Vous pouvez également utiliser le [débogueur SDK]({{site.baseurl}}/developer_guide/debugging) pour diagnostiquer les problèmes liés au SDK.
{% endalert %}

Si vous rencontrez des problèmes lors de vos tests, activez la [journalisation en mode verbeux](#android_enabling-logs), puis utilisez logcat pour détecter les appels `openSession` et `closeSession` manquants dans vos activités.

1. Dans Braze, allez dans **Aperçu**, sélectionnez votre application, puis dans le menu déroulant **Afficher les données d'aperçu**, choisissez **Aujourd'hui.**
    ![La page "Aperçu" de Braze, avec le champ "Afficher les données pour" réglé sur "Aujourd'hui".]({% image_buster /assets/img_archive/android_sessions.png %})
2. Ouvrez votre appli, puis actualisez le tableau de bord de Braze. Vérifiez que vos indicateurs ont augmenté de 1.
3. Naviguez dans votre application et vérifiez qu'une seule session a été enregistrée sur Braze.
4. Faites passer l'application en arrière-plan pendant au moins 10 secondes, puis ramenez-la au premier plan. Vérifiez qu'une nouvelle session a été enregistrée.

## Configurations optionnelles

### Configuration du temps d’exécution

Pour définir vos options Braze dans le code plutôt que dans votre fichier `braze.xml`, utilisez la [configuration d'exécution](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/configure.html). Si une valeur existe aux deux endroits, c'est la valeur d'exécution qui sera utilisée. Une fois que tous les paramètres requis ont été fournis au moment de l'exécution, vous pouvez supprimer votre fichier `braze.xml`.

Dans l'exemple suivant, un [objet générateur](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/index.html) est créé puis transmis à [`Braze.configure()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/configure.html). Notez que seules quelques-unes des options d'exécution disponibles sont affichées - reportez-vous à notre [KDoc](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/index.html) pour la liste complète.

{% tabs %}
{% tab JAVA %}

```java
BrazeConfig brazeConfig = new BrazeConfig.Builder()
        .setApiKey("api-key-here")
        .setCustomEndpoint("YOUR_CUSTOM_ENDPOINT_OR_CLUSTER")
        .setSessionTimeout(60)
        .setHandlePushDeepLinksAutomatically(true)
        .setGreatNetworkDataFlushInterval(10)
        .build();
Braze.configure(this, brazeConfig);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
val brazeConfig = BrazeConfig.Builder()
        .setApiKey("api-key-here")
        .setCustomEndpoint("YOUR_CUSTOM_ENDPOINT_OR_CLUSTER")
        .setSessionTimeout(60)
        .setHandlePushDeepLinksAutomatically(true)
        .setGreatNetworkDataFlushInterval(10)
        .build()
Braze.configure(this, brazeConfig)
```

{% endtab %}
{% endtabs %}

{% alert tip %}
Vous cherchez un autre exemple ? Consultez notre [exemple d'application Hello Braze](https://github.com/braze-inc/braze-android-sdk/blob/master/samples/hello-braze/src/main/java/com/braze/helloworld/CustomApplication.java).
{% endalert %}

### ID publicitaire Google

L'[identifiant publicitaire Google (GAID)](https://support.google.com/googleplay/android-developer/answer/6048248/advertising-id?hl=en) est un identifiant publicitaire facultatif, spécifique à l'utilisateur, anonyme, unique et réinitialisable, fourni par les services Google Play. Le GAID permet aux utilisateurs de réinitialiser leur identifiant, de désactiver les publicités axées sur les centres d’intérêt dans les applications Google Play et de fournir aux développeurs un système simple et standard pour continuer à monétiser leurs applications.

L’ID publicitaire Google n’est pas automatiquement collecté par le SDK Braze et doit être défini manuellement via la méthode [`Braze.setGoogleAdvertisingId()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/set-google-advertising-id.html).

{% tabs local %}
{% tab JAVA %}

```java
new Thread(new Runnable() {
  @Override
  public void run() {
    try {
      AdvertisingIdClient.Info idInfo = AdvertisingIdClient.getAdvertisingIdInfo(getApplicationContext());
      Braze.getInstance(getApplicationContext()).setGoogleAdvertisingId(idInfo.getId(), idInfo.isLimitAdTrackingEnabled());
    } catch (Exception e) {
      e.printStackTrace();
    }
  }
}).start();
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
suspend fun fetchAndSetAdvertisingId(
  context: Context,
  scope: CoroutineScope = GlobalScope
) {
  scope.launch(Dispatchers.IO) {
    try {
      val idInfo = AdvertisingIdClient.getAdvertisingIdInfo(context)
      Braze.getInstance(context).setGoogleAdvertisingId(
        idInfo.id,
        idInfo.isLimitAdTrackingEnabled
      )
    } catch (e: Exception) {
      e.printStackTrace()
    }
  }
}
```

{% endtab %}
{% endtabs %}

{% alert important %}
Google exige que l’ID publicitaire soit collecté sur un fil non-IU.
{% endalert %}


### Suivi de localisation

Pour activer la collecte d'emplacements/localisations de Braze, définissez `com_braze_enable_location_collection` comme `true` dans votre fichier `braze.xml`:

```xml
<bool name="com_braze_enable_location_collection">true</bool>
```

{% alert important %}
À partir de la version 3.6.0 du SDK Braze pour Android, le recueil des données de localisation Braze est désactivé par défaut.
{% endalert %}

### Journalisation

Par défaut, le niveau de journalisation du SDK Android de Braze est défini sur `INFO`. Vous pouvez [supprimer ces journaux](#android_suppressing-logs) ou [définir un niveau de journal différent](#android_enabling-logs), tel que `VERBOSE`, `DEBUG`, ou `WARN`.

#### Activation des journaux

Pour faciliter la résolution des problèmes dans votre application ou réduire les délais de résolution des problèmes avec le service d'assistance de Braze, vous devez activer les journaux détaillés pour le SDK. Lorsque vous envoyez des journaux verbeux à l'assistance Braze, veillez à ce qu'ils commencent dès le lancement de votre application et se terminent bien après l'apparition de votre problème.

Gardez à l'esprit que les journaux verbeux ne sont destinés qu'à votre environnement de développement, et que vous devez donc les désactiver avant de rendre votre application publique.

{% alert important %}
Activez l'option "verbose logs" avant tout autre appel dans `Application.onCreate()` pour vous assurer que vos logs sont aussi complets que possible.
{% endalert %}

{% tabs local %}
{% tab Application %}
Pour activer les journaux directement dans votre application, ajoutez ce qui suit à la méthode `onCreate()` de votre application avant toute autre méthode.

{% subtabs local %}
{% subtab JAVA %}
```java
BrazeLogger.setLogLevel(Log.MIN_LOG_LEVEL);
```
{% endsubtab %}

{% subtab KOTLIN %}
```kotlin
BrazeLogger.logLevel = Log.MIN_LOG_LEVEL
```
{% endsubtab %}
{% endsubtabs %}

Remplacez `MIN_LOG_LEVEL` par la **constante** du niveau de journalisation que vous souhaitez définir comme niveau de journalisation minimum. Tous les journaux d'un niveau `>=` au `MIN_LOG_LEVEL` que vous avez défini seront transmis à la méthode [`Log`](https://developer.android.com/reference/android/util/Log) par défaut d'Android. Tous les journaux `<` au `MIN_LOG_LEVEL` que vous avez défini seront rejetés.

| Constant    | Valeur          | Description                                                               |
|-------------|----------------|---------------------------------------------------------------------------|
| `VERBOSE`   | 2              | Enregistre les messages les plus détaillés pour le débogage et le développement.            |
| `DEBUG`     | 3              | Enregistre des messages descriptifs pour le débogage et le développement.                  |
| `INFO`      | 4              | Enregistre des messages d'information pour les faits marquants.                       |
| `WARN`      | 5              | Enregistre les messages d'avertissement pour identifier les situations potentiellement dangereuses.     |
| `ERROR`     | 6              | Enregistre les messages d'erreur pour indiquer les échecs de l'application ou les problèmes graves. |
| `ASSERT`    | 7              | Enregistre les messages d'assertion lorsque les conditions sont fausses pendant le développement.     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Par exemple, le code suivant transmettra les niveaux de journalisation `2`, `3`, `4`, `5`, `6` et `7` à la méthode `Log`.

{% subtabs local %}
{% subtab JAVA %}
```java
BrazeLogger.setLogLevel(Log.VERBOSE);
```
{% endsubtab %}

{% subtab KOTLIN %}
```kotlin
BrazeLogger.logLevel = Log.VERBOSE
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab xml %}
Pour activer les journaux dans le `braze.xml`, ajoutez ce qui suit à votre fichier :

```xml
<integer name="com_braze_logger_initial_log_level">MIN_LOG_LEVEL</integer>
```

Remplacez `MIN_LOG_LEVEL` par la **valeur** du niveau de journalisation que vous souhaitez définir comme niveau de journalisation minimum. Tous les journaux d'un niveau `>=` au `MIN_LOG_LEVEL` que vous avez défini seront transmis à la méthode [`Log`](https://developer.android.com/reference/android/util/Log) par défaut d'Android. Tous les journaux `<` au `MIN_LOG_LEVEL` que vous avez défini seront rejetés.

| Constant    | Valeur          | Description                                                               |
|-------------|----------------|---------------------------------------------------------------------------|
| `VERBOSE`   | 2              | Enregistre les messages les plus détaillés pour le débogage et le développement.            |
| `DEBUG`     | 3              | Enregistre des messages descriptifs pour le débogage et le développement.                  |
| `INFO`      | 4              | Enregistre des messages d'information pour les faits marquants.                       |
| `WARN`      | 5              | Enregistre les messages d'avertissement pour identifier les situations potentiellement dangereuses.     |
| `ERROR`     | 6              | Enregistre les messages d'erreur pour indiquer les échecs de l'application ou les problèmes graves. |
| `ASSERT`    | 7              | Enregistre les messages d'assertion lorsque les conditions sont fausses pendant le développement.     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Par exemple, le code suivant transmettra les niveaux de journalisation `2`, `3`, `4`, `5`, `6` et `7` à la méthode `Log`.

```xml
<integer name="com_braze_logger_initial_log_level">2</integer>
```
{% endtab %}
{% endtabs %}

#### Vérification des journaux de bord (verbose logs)

Pour vérifier que vos journaux sont définis sur `VERBOSE`, vérifiez si `V/Braze` apparaît quelque part dans vos journaux. Si c'est le cas, c'est que l'option de journalisation en mode verbeux a été activée avec succès. Par exemple :

```
2077-11-19 16:22:49.591 ? V/Braze v9.0.01 .bo.app.d3: Request started
```

#### Suppression des journaux

Pour supprimer tous les journaux pour le SDK Android de Braze, définissez le niveau de journal sur `BrazeLogger.SUPPRESS` dans la méthode `onCreate()` de votre application _avant toute_ autre méthode.

{% tabs local %}
{% tab JAVA %}
```java
BrazeLogger.setLogLevel(BrazeLogger.SUPPRESS);
```
{% endtab %}

{% tab KOTLIN %}
```kotlin
BrazeLogger.setLogLevel(BrazeLogger.SUPPRESS)
```
{% endtab %}
{% endtabs %}

### Plusieurs clés API

Le cas d’usage le plus fréquent pour les clés API multiples est la séparation des clés API entre les variantes de version de débogage et de publication.

Pour basculer facilement entre plusieurs clés API dans vos versions, nous vous recommandons de créer un fichier `braze.xml` pour chaque [variante de version](https://developer.android.com/studio/build/build-variants.html) pertinente. Une variante de version est une combinaison du type de version et de la variété du produit. Par défaut, les nouveaux projets Android sont créés avec les [types de construction`debug` et `release` ](https://developer.android.com/reference/tools/gradle-api/8.3/null/com/android/build/api/dsl/BuildType) et sans aucun produit.

Pour chaque variante de création concernée, créez un nouveau site `braze.xml` dans le répertoire `src/<build variant name>/res/values/`. Lorsque la variante de version est compilée, elle utilisera la nouvelle clé API.

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
<string name="com_braze_api_key">REPLACE_WITH_YOUR_BUILD_VARIANT_API_KEY</string>
</resources>
```

{% alert tip %}
Pour savoir comment configurer la clé API dans votre code, consultez la rubrique [Configuration de l'exécution.]({{site.baseurl}}/developer_guide/sdk_initalization/?sdktab=android)
{% endalert %}

### Message in-app exclusif TalkBack

Conformément aux [directives d'accessibilité d'Android](https://developer.android.com/guide/topics/ui/accessibility), le SDK Android de Braze propose par défaut Android Talkback. Pour vous assurer que seul le contenu des messages in-app est lu à haute voix, sans inclure d'autres éléments de l'écran tels que la barre de titre de l'application ou la navigation, vous pouvez activer le mode exclusif pour TalkBack.

Pour activer le mode exclusif pour les messages in-app :

{% tabs local %}
{% tab Braze XML %}
```xml
<bool name="com_braze_device_in_app_message_accessibility_exclusive_mode_enabled">true</bool>
```
{% endtab %}

{% tab Kotlin %}
```kotlin
val brazeConfigBuilder = BrazeConfig.Builder()
brazeConfigBuilder.setIsInAppMessageAccessibilityExclusiveModeEnabled(true)
Braze.configure(this, brazeConfigBuilder.build())
```
{% endtab %}

{% tab Java %}
```java
BrazeConfig.Builder brazeConfigBuilder = new BrazeConfig.Builder()
brazeConfigBuilder.setIsInAppMessageAccessibilityExclusiveModeEnabled(true);
Braze.configure(this, brazeConfigBuilder.build());
```
{% endtab %}
{% endtabs %}

### R8 et ProGuard

La configuration de la [réduction du code](https://developer.android.com/build/shrink-code) est automatiquement incluse dans votre intégration de Braze.

Les applications client qui obscurcissent le code Braze doivent stocker des fichiers de mappage de libération pour Braze afin d’interpréter les traces de pile. Si vous souhaitez continuer à conserver tous les codes Braze, ajoutez ce qui suit à votre fichier ProGuard :

```
-keep class bo.app.** { *; }
-keep class com.braze.** { *; }
```
