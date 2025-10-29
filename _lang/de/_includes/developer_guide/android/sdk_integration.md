## Integration des Android SDK

### Schritt 1: Aktualisieren Sie Ihr `build.gradle`

Fügen Sie in Ihrem `build.gradle` [`mavenCentral()`](https://docs.gradle.org/current/kotlin-dsl/gradle/org.gradle.api.artifacts.dsl/-repository-handler/maven-central.html) zu Ihrer Liste der Repositories hinzu.

```kotlin
repositories {
  mavenCentral()
}
```

Als nächstes fügen Sie Braze zu Ihren Abhängigkeiten hinzu.

{% tabs local %}
{% tab nur Basis %}
Wenn Sie nicht vorhaben, Braze UI-Komponenten zu verwenden, fügen Sie den folgenden Code zu Ihrem `build.gradle` hinzu. Ersetzen Sie `SDK_VERSION` durch die aktuelle Version Ihres Android Braze SDK. Die vollständige Liste der Versionen finden Sie unter [Changelogs]({{site.baseurl}}/developer_guide/changelogs/?sdktab=android).

```kotlin
dependencies {
    implementation 'com.braze:android-sdk-base:SDK_VERSION' // (Required) Adds dependencies for the base Braze SDK.
    implementation 'com.braze:android-sdk-location:SDK_VERSION' // (Optional) Adds dependencies for Braze location services.
}
```
{% endtab %}

{% tab mit UI-Komponenten %}
Wenn Sie später Braze UI-Komponenten verwenden möchten, fügen Sie den folgenden Code zu Ihrem `build.gradle` hinzu.  Ersetzen Sie `SDK_VERSION` durch die aktuelle Version Ihres Android Braze SDK. Die vollständige Liste der Versionen finden Sie unter [Changelogs]({{site.baseurl}}/developer_guide/changelogs/?sdktab=android).

```kotlin
dependencies {
    implementation 'com.braze:android-sdk-ui:SDK_VERSION' // (Required) Adds dependencies for the Braze SDK and Braze UI components. 
    implementation 'com.braze:android-sdk-location:SDK_VERSION' // (Optional) Adds dependencies for Braze location services.
}
```
{% endtab %}
{% endtabs %}

### Schritt 2: Konfigurieren Sie Ihr `braze.xml`

{% alert note %}
Ab Dezember 2019 werden keine benutzerdefinierten Endpunkte mehr vergeben. Wenn Sie einen bereits bestehenden benutzerdefinierten Endpunkt haben, können Sie diesen weiterhin verwenden. Weitere Einzelheiten finden Sie in unserer <a href="{{site.baseurl}}/api/basics/#endpoints">Liste der verfügbaren Endpunkte</a>.
{% endalert %}

Erstellen Sie eine Datei `braze.xml` im Ordner `res/values` Ihres Projekts. Wenn Sie mit einem bestimmten Daten-Cluster arbeiten oder einen zuvor angepassten Endpunkt verwenden, müssen Sie den Endpunkt ebenfalls in der Datei `braze.xml` angeben. 

Der Inhalt dieser Datei sollte dem folgenden Codeschnipsel ähneln. Stellen Sie sicher, dass Sie `YOUR_APP_IDENTIFIER_API_KEY` durch die Kennung ersetzen, die Sie auf der Seite **Einstellungen verwalten** des Braze Dashboards finden. Melden Sie sich unter [dashboard.braze.com](https://dashboard.braze.com) an, um die [Cluster-Adresse]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints) zu finden. 

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
  <string translatable="false" name="com_braze_api_key">YOUR_APP_IDENTIFIER_API_KEY</string>
  <string translatable="false" name="com_braze_custom_endpoint">YOUR_CUSTOM_ENDPOINT_OR_CLUSTER</string>
</resources>
```

### Schritt 3: Berechtigungen hinzufügen zu `AndroidManifest.xml`

Fügen Sie als Nächstes die folgenden Berechtigungen zu Ihrem `AndroidManifest.xml` hinzu:

```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
```

{% alert note %}
Mit der Veröffentlichung von Android M wechselte Android von einem Installationszeit- zu einem Laufzeit-Berechtigungsmodell. Diese beiden Berechtigungen sind jedoch normale Berechtigungen. Sie werden automatisch gewährt, wenn sie im App-Manifest aufgeführt sind. Weitere Informationen finden Sie in der [Dokumentation zu den Berechtigungen](https://developer.android.com/training/permissions/index.html) von Android.
{% endalert %}

### Schritt 4: Verzögerte Initialisierung einschalten (optional)

Um die verzögerte Initialisierung zu verwenden, ist die Mindestversion des Braze SDK erforderlich:

{% sdk_min_versions android:38.0.0 %}

{% alert note %}
Während die verzögerte Initialisierung aktiviert ist, werden alle Netzwerkverbindungen abgebrochen, so dass das SDK keine Daten an die Braze Server senden kann.
{% endalert %}

#### Schritt 4.1: Aktualisieren Sie Ihr `braze.xml`

Die verzögerte Initialisierung ist standardmäßig deaktiviert. Zum Enablement verwenden Sie eine der folgenden Optionen:

{% tabs %}
{% tab Braze XML Datei %}
In der Datei `braze.xml` Ihres Projekts setzen Sie `com_braze_enable_delayed_initialization` auf `true`.

```xml
<bool name="com_braze_enable_delayed_initialization">true</bool>
```
{% endtab %}

{% tab Zur Laufzeit %}
Um die verzögerte Initialisierung zur Laufzeit zu aktivieren, verwenden Sie die folgende Methode.

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

#### Schritt 4.2: Konfigurieren Sie Push Analytics (optional)

Wenn die verzögerte Initialisierung aktiviert ist, werden Push Analytics standardmäßig in eine Warteschlange gestellt. Sie können Push Analytics jedoch auch [explizit in die Warteschlange stellen](#explicitly-queue-push-analytics) oder [ablehnen](#drop-push-analytics).

##### Ausdrücklich Warteschlange {#explicitly-queue-push-analytics}

Um Push Analytics explizit in die Warteschlange zu stellen, wählen Sie eine der folgenden Optionen:

{% tabs %}
{% tab Braze XML Datei %}
Setzen Sie in Ihrer Datei `braze.xml` `com_braze_delayed_initialization_analytics_behavior` auf `QUEUE`:

```xml
<string name="com_braze_delayed_initialization_analytics_behavior">QUEUE</string>
```
{% endtab %}

{% tab Zur Laufzeit %}
Fügen Sie `QUEUE` zu Ihrer [`Braze.enableDelayedInitialization()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/enable-delayed-initialization.html) Methode hinzu:

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

##### Ablegen {#drop-push-analytics}

Um Push Analytics zu löschen, wählen Sie eine der folgenden Optionen:

{% tabs %}
{% tab Braze XML Datei %}
Setzen Sie in Ihrer Datei `braze.xml` `com_braze_delayed_initialization_analytics_behavior` auf `DROP`: 

```xml
<string name="com_braze_delayed_initialization_analytics_behavior">DROP</string>
```
{% endtab %}

{% tab Zur Laufzeit %}
Fügen Sie `DROP` zu der [`Braze.enableDelayedInitialization()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/enable-delayed-initialization.html) Methode hinzu:

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

#### Schritt 4.3: Manuelles Initialisieren des SDK

Nach der von Ihnen gewählten Verzögerungszeit verwenden Sie die [`Braze.disableDelayedInitialization()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/disable-delayed-initialization.html) Methode, um das SDK manuell zu initialisieren.

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

### Schritt 5: Enablement des Trackings von Nutzer:innen-Sitzungen

Wenn Sie das Tracking von Nutzersitzungen aktivieren, können Aufrufe von `openSession()`, `closeSession()`,[`ensureSubscribedToInAppMessageEvents()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/ensure-subscribed-to-in-app-message-events.html)und die `InAppMessageManager` Registrierung automatisch verarbeitet werden.

Um Callbacks für den Lebenszyklus einer Aktivität zu registrieren, fügen Sie den folgenden Code in die Methode `onCreate()` Ihrer Klasse `Application` ein. 

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

Für die Liste der verfügbaren Parameter siehe [`BrazeActivityLifecycleCallbackListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-activity-lifecycle-callback-listener/index.html).

{% endtab %}
{% endtabs %}

## Testen des Sitzungs-Trackings

{% alert tip %}
Sie können auch den [SDK Debugger]({{site.baseurl}}/developer_guide/debugging) verwenden, um Probleme mit dem SDK zu diagnostizieren.
{% endalert %}

Wenn Sie beim Testen auf Probleme stoßen, aktivieren Sie die [ausführliche Protokollierung](#android_enabling-logs) und verwenden Sie dann logcat, um fehlende `openSession` und `closeSession` Aufrufe in Ihren Aktivitäten zu entdecken.

1. Gehen Sie in Braze zu **Übersicht**, wählen Sie Ihre App aus und wählen Sie dann in der Dropdown-Liste **Daten anzeigen für die** Option **Heute**.
    ![Die Seite "Übersicht" in Braze, wobei das Feld "Daten anzeigen für" auf "Heute" eingestellt ist.]({% image_buster /assets/img_archive/android_sessions.png %})
2. Öffnen Sie Ihre App und aktualisieren Sie dann das Braze-Dashboard. Überprüfen Sie, ob sich Ihre Metriken um 1 erhöht haben.
3. Navigieren Sie durch Ihre App und überprüfen Sie, ob nur eine Sitzung bei Braze angemeldet wurde.
4. Versetzen Sie die App für mindestens 10 Sekunden in den Hintergrund und holen Sie sie dann in den Vordergrund. Überprüfen Sie, ob eine neue Sitzung protokolliert wurde.

## Optionale Konfigurationen

### Laufzeitkonfiguration

Um Ihre Braze-Optionen im Code und nicht in der Datei `braze.xml` festzulegen, verwenden Sie die [Laufzeitkonfiguration](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/configure.html). Wenn ein Wert an beiden Stellen existiert, wird stattdessen der Laufzeitwert verwendet. Nachdem alle erforderlichen Einstellungen zur Laufzeit vorgenommen wurden, können Sie Ihre `braze.xml` Datei löschen.

Im folgenden Beispiel wird ein [Builder-Objekt](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/index.html) erstellt und dann an [`Braze.configure()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/configure.html). Beachten Sie, dass nur einige der verfügbaren Laufzeitoptionen angezeigt werden - die vollständige Liste finden Sie in unserer [KDoc](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/index.html).

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
Sie suchen ein weiteres Beispiel? Sehen Sie sich unsere [Hello Braze Beispiel App](https://github.com/braze-inc/braze-android-sdk/blob/master/samples/hello-braze/src/main/java/com/braze/helloworld/CustomApplication.java) an.
{% endalert %}

### Google Advertising ID

Die [Google Advertising ID (GAID)](https://support.google.com/googleplay/android-developer/answer/6048248/advertising-id?hl=en) ist eine optionale nutzerspezifische, anonyme, eindeutige und zurücksetzbare ID für Werbung, die von Google Play Diensten bereitgestellt wird. GAID gibt Nutzern:innen die Möglichkeit, ihren Bezeichner zurückzusetzen, interessenbezogene Werbung in Google Play Apps abzulehnen und bietet Entwicklern:innen ein einfaches, standardisiertes System, um ihre Apps weiterhin zu monetarisieren.

Die Google Advertising ID wird nicht automatisch vom Braze SDK erfasst und muss manuell über die Methode [`Braze.setGoogleAdvertisingId()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/set-google-advertising-id.html) festgelegt werden.

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
Google verlangt, dass die Advertising ID auf einem Nicht-UI-Thread erfasst wird.
{% endalert %}


### Standort-Tracking

Um die Erfassung von Braze-Standorten zu aktivieren, setzen Sie `com_braze_enable_location_collection` in Ihrer Datei `braze.xml` auf `true`:

```xml
<bool name="com_braze_enable_location_collection">true</bool>
```

{% alert important %}
Ab Version 3.6.0 des Braze Android-SDK ist die Braze-Standortermittlung standardmäßig deaktiviert.
{% endalert %}

### Protokollieren

Standardmäßig ist der Braze Android SDK Loglevel auf `INFO` eingestellt. Sie können [diese Protokolle unterdrücken](#android_suppressing-logs) oder [eine andere Protokollstufe einstellen](#android_enabling-logs), z. B. `VERBOSE`, `DEBUG` oder `WARN`.

#### Enablement von Protokollen

Um die Fehlerbehebung in Ihrer App zu erleichtern oder die Bearbeitungszeit beim Braze Support zu verkürzen, sollten Sie ausführliche Protokolle für das SDK aktivieren. Wenn Sie ausführliche Protokolle an den Braze-Support senden, stellen Sie sicher, dass diese beginnen, sobald Sie Ihre Anwendung starten und weit nach dem Auftreten des Problems enden.

Denken Sie daran, dass ausführliche Protokolle nur für Ihre Entwicklungsumgebung gedacht sind. Sie sollten sie also deaktivieren, bevor Sie Ihre App veröffentlichen.

{% alert important %}
Aktivieren Sie ausführliche Protokolle vor allen anderen Aufrufen in `Application.onCreate()`, um sicherzustellen, dass Ihre Protokolle so vollständig wie möglich sind.
{% endalert %}

{% tabs local %}
{% tab Anwendung %}
Um Protokolle direkt in Ihrer App zu aktivieren, fügen Sie der Methode `onCreate()` Ihrer Anwendung vor allen anderen Methoden Folgendes hinzu.

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

Ersetzen Sie `MIN_LOG_LEVEL` durch die **Konstante** der Protokollstufe, die Sie als minimale Protokollstufe festlegen möchten. Alle Protokolle auf der Ebene `>=`, die Sie unter `MIN_LOG_LEVEL` eingestellt haben, werden an die standardmäßige [`Log`](https://developer.android.com/reference/android/util/Log)-Methode in Android weitergeleitet. Alle Protokolle `<` Ihrer Einstellung `MIN_LOG_LEVEL` werden verworfen.

| Konstant    | Wert          | Beschreibung                                                               |
|-------------|----------------|---------------------------------------------------------------------------|
| `VERBOSE`   | (2 %)              | Protokolliert die detailliertesten Nachrichten zur Fehlersuche und Entwicklung.            |
| `DEBUG`     | 3              | Protokolliert beschreibende Nachrichten zur Fehlersuche und Entwicklung.                  |
| `INFO`      | (4 %)              | Protokolliert informative Nachrichten für allgemeine Highlights.                       |
| `WARN`      | (5 %)              | Protokolliert Nachrichten mit Warnungen zur Identifizierung potenziell schädlicher Situationen.     |
| `ERROR`     | 6              | Protokolliert Fehlermeldungen, die auf Anwendungsfehler oder schwerwiegende Probleme hinweisen. |
| `ASSERT`    | (7 %)              | Protokolliert Messaging-Nachrichten, wenn Bedingungen während der Entwicklung falsch sind.     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Der folgende Code leitet zum Beispiel die Protokollstufen `2`, `3`, `4`, `5`, `6` und `7` an die Methode `Log` weiter.

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
Um Protokolle in `braze.xml` zu aktivieren, fügen Sie Folgendes zu Ihrer Datei hinzu:

```xml
<integer name="com_braze_logger_initial_log_level">MIN_LOG_LEVEL</integer>
```

Ersetzen Sie `MIN_LOG_LEVEL` durch den **Wert** der Protokollstufe, die Sie als minimale Protokollstufe festlegen möchten. Alle Protokolle auf der Ebene `>=`, die Sie unter `MIN_LOG_LEVEL` eingestellt haben, werden an die standardmäßige [`Log`](https://developer.android.com/reference/android/util/Log)-Methode in Android weitergeleitet. Alle Protokolle `<` Ihrer Einstellung `MIN_LOG_LEVEL` werden verworfen.

| Konstant    | Wert          | Beschreibung                                                               |
|-------------|----------------|---------------------------------------------------------------------------|
| `VERBOSE`   | (2 %)              | Protokolliert die detailliertesten Nachrichten zur Fehlersuche und Entwicklung.            |
| `DEBUG`     | 3              | Protokolliert beschreibende Nachrichten zur Fehlersuche und Entwicklung.                  |
| `INFO`      | (4 %)              | Protokolliert informative Nachrichten für allgemeine Highlights.                       |
| `WARN`      | (5 %)              | Protokolliert Nachrichten mit Warnungen zur Identifizierung potenziell schädlicher Situationen.     |
| `ERROR`     | 6              | Protokolliert Fehlermeldungen, die auf Anwendungsfehler oder schwerwiegende Probleme hinweisen. |
| `ASSERT`    | (7 %)              | Protokolliert Messaging-Nachrichten, wenn Bedingungen während der Entwicklung falsch sind.     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Der folgende Code leitet zum Beispiel die Protokollstufen `2`, `3`, `4`, `5`, `6` und `7` an die Methode `Log` weiter.

```xml
<integer name="com_braze_logger_initial_log_level">2</integer>
```
{% endtab %}
{% endtabs %}

#### Überprüfen von ausführlichen Protokollen

Um zu überprüfen, ob Ihre Protokolle auf `VERBOSE` eingestellt sind, prüfen Sie, ob `V/Braze` irgendwo in Ihren Protokollen vorkommt. Wenn dies der Fall ist, dann sind die ausführlichen Protokolle aktiviert. Zum Beispiel:

```
2077-11-19 16:22:49.591 ? V/Braze v9.0.01 .bo.app.d3: Request started
```

#### Protokolle unterdrücken

Um alle Protokolle für das Braze Android SDK zu unterdrücken, setzen Sie die Protokollstufe in der Methode `onCreate()` Ihrer Anwendung _vor_ allen anderen Methoden auf `BrazeLogger.SUPPRESS`.

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

### Mehrere API-Schlüssel

Der häufigste Anwendungsfall für mehrere API-Schlüssel ist die Trennung von API-Schlüsseln für Debug- und Release-Build-Varianten.

Um in Ihren Builds einfach zwischen mehreren API-Schlüsseln wechseln zu können, empfehlen wir, für jede relevante [Variante des Builds](https://developer.android.com/studio/build/build-variants.html) eine eigene `braze.xml` Datei zu erstellen. Eine Build-Variante ist eine Kombination aus Build-Typ und Produkt-Flavor. Standardmäßig werden neue Android-Projekte mit den [Build-Typen`debug` und `release` ](https://developer.android.com/reference/tools/gradle-api/8.3/null/com/android/build/api/dsl/BuildType) und ohne Produkt-Flavors konfiguriert.

Erstellen Sie für jede relevante Variante eine neue `braze.xml` im Verzeichnis `src/<build variant name>/res/values/`. Wenn die Build-Variante kompiliert wird, wird sie den neuen API-Schlüssel verwenden.

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
<string name="com_braze_api_key">REPLACE_WITH_YOUR_BUILD_VARIANT_API_KEY</string>
</resources>
```

{% alert tip %}
Wie Sie den API-Schlüssel in Ihrem Code einrichten können, erfahren Sie unter [Laufzeitkonfiguration]({{site.baseurl}}/developer_guide/sdk_initalization/?sdktab=android).
{% endalert %}

### Exklusive In-App-Nachricht TalkBack

In Übereinstimmung mit den [Android-Richtlinien für Barrierefreiheit](https://developer.android.com/guide/topics/ui/accessibility) bietet das Braze Android SDK standardmäßig Android Talkback. Um sicherzustellen, dass nur der Inhalt von In-App-Nachrichten laut vorgelesen wird - ohne andere Bildschirmelemente wie die Titelleiste der App oder die Navigation einzubeziehen - können Sie den Exklusivmodus für TalkBack aktivieren.

So aktivieren Sie den exklusiven Modus für In-App-Nachrichten:

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

### R8 und ProGuard

Die [Codeshrinking](https://developer.android.com/build/shrink-code)-Konfiguration ist automatisch in Ihrer Braze Integration enthalten.

Client-Apps, die den Braze-Code verschleiern, müssen Release-Mapping-Dateien speichern, damit Braze die Stack-Traces interpretieren kann. Wenn Sie den gesamten Braze-Code beibehalten möchten, fügen Sie Folgendes in Ihre ProGuard-Datei ein:

```
-keep class bo.app.** { *; }
-keep class com.braze.** { *; }
```
