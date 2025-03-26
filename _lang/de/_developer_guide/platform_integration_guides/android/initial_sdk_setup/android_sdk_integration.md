---
nav_title: Android SDK Integration
article_title: Android SDK Integration für Android und FireOS
page_order: 0
platform: 
  - Android
  - FireOS
description: "Dieser Referenzartikel beschreibt, wie Sie das Android SDK in Ihre Android- oder FireOS-Anwendung integrieren."
search_rank: 4
---

# Android SDK Integration

> Dieser Referenzartikel beschreibt, wie Sie das Android SDK in Ihre Android- oder FireOS-Anwendung integrieren. Durch die Installation des Braze SDK erhalten Sie grundlegende Analytics-Funktionen und funktionierende In-App-Nachrichten für Ihre Nutzer.

{% alert note %}
Für optimale Performance unter Android 12 empfehlen wir, so bald wie möglich ein Upgrade auf [Braze Android SDK v13.1.2+](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#1312) vorzunehmen. Weitere Informationen finden Sie in unserer [Android 12 Upgrade-Anleitung]({{site.baseurl}}/android_12/).
{% endalert %}

## Schritt 1: Braze-Bibliothek integrieren

Das Braze Android SDK kann optional auch ohne UI-Komponenten integriert werden. Content Cards und In-App-Nachrichten sind jedoch nicht funktionsfähig, es sei denn, Sie übergeben die benutzerdefinierten Daten an eine Benutzeroberfläche, die ausschließlich von Ihnen entworfen wurde. Außerdem werden keine Push-Benachrichtigungen unterstützt, da der Code für die Push-Verarbeitung in der UI-Bibliothek enthalten ist. Es ist wichtig zu wissen, dass diese UI-Elemente vollständig anpassbar sind. Wir empfehlen nachdrücklich die Integration dieser Funktionen. In der Dokumentation zu den [Content Cards]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/about/#advantages-of-using-content-cards) und den [In-App-Nachrichten]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/about/) finden Sie eine Liste der Vorteile, die sich aus der Verwendung der einzelnen Kanäle oder Tools ergeben.

### Grundlegende Integration

Um auf die Messaging-Features von Braze zuzugreifen, müssen Sie die UI-Bibliothek integrieren. Sehen Sie sich die folgenden Anleitungen für Android Studio an, um die UI Bibliothek je nach Ihrer IDE zu integrieren:

#### Braze-Abhängigkeit hinzufügen

Fügen Sie die Abhängigkeit `android-sdk-ui` zu Ihrer App `build.gradle` hinzu. 

Wenn Sie Standort- oder Braze Geofence-Funktionalität verwenden, fügen Sie außerdem `android-sdk-location` in `build.gradle` Ihrer App ein.

{% alert important %}
Wenn Sie ein nicht-natives Android SDK (z. B. Flutter, Cordova, Unity) verwenden, verfügt dieses bereits über die Abhängigkeit `android-sdk-ui` für die richtige Version des Android SDK. Aktualisieren Sie diese Version nicht manuell.
{% endalert %}

```gradle
dependencies {
  implementation "com.braze:android-sdk-ui:+"
  implementation "com.braze:android-sdk-location:+"
}
```

Das folgende Beispiel zeigt, wo Sie die Abhängigkeitszeile in `build.gradle` platzieren können. Beachten Sie, dass die im Beispiel verwendete Version eine alte Version ist. Die aktuellste Version des Braze Android SDK finden Sie unter [Braze Android SDK-Releases](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md).

![Android Studio zeigt "build.gradle" an, wobei der Abhängigkeitscode am Ende der Datei hinzugefügt wurde.]({% image_buster /assets/img_archive/androidstudio2.png %})

#### Gradle-Synchronisation durchführen

Stellen Sie sicher, dass Sie eine Gradle-Synchronisierung durchführen, um Ihr Projekt zu erstellen und die [hinzugefügten Abhängigkeiten](#add-braze-dependency) einzubinden.

![Ein Banner in Android Studio mit dem Hinweis: "Gradle-Dateien wurden seit der letzten Projekt-Synchronisierung geändert. Damit die IDE richtig funktioniert, kann eine Projekt-Synchronisierung erforderlich sein. Jetzt synchronisieren."]({% image_buster /assets/img_archive/androidstudio3.png %})

## Schritt 2: Braze SDK in braze.xml konfigurieren

{% alert note %}
Ab Dezember 2019 werden keine benutzerdefinierten Endpunkte mehr vergeben. Wenn Sie einen bereits bestehenden benutzerdefinierten Endpunkt haben, können Sie diesen weiterhin verwenden. Weitere Einzelheiten finden Sie in unserer <a href="{{site.baseurl}}/api/basics/#endpoints">Liste der verfügbaren Endpunkte</a>.
{% endalert %}

Nach der Integration der Bibliotheken müssen Sie eine Datei namens `braze.xml` im Ordner `res/values` Ihres Projekts erstellen. Wenn Sie mit einem bestimmten Daten-Cluster arbeiten oder einen zuvor angepassten Endpunkt verwenden, müssen Sie den Endpunkt ebenfalls in der Datei `braze.xml` angeben. 

Der Inhalt dieser Datei sollte dem folgenden Codeschnipsel ähneln. Stellen Sie sicher, dass Sie `YOUR_APP_IDENTIFIER_API_KEY` durch die Kennung ersetzen, die Sie auf der Seite **Einstellungen verwalten** des Braze Dashboards finden. Melden Sie sich unter [dashboard.braze.com](https://dashboard.braze.com) an, um die [Cluster-Adresse]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints) zu finden. 

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
<string name="com_braze_api_key">YOUR_APP_IDENTIFIER_API_KEY</string>
<string translatable="false" name="com_braze_custom_endpoint">YOUR_CUSTOM_ENDPOINT_OR_CLUSTER</string>
</resources>
```

## Schritt 3: Erforderliche Berechtigungen zu AndroidManifest.xml hinzufügen
Nachdem Sie den API-Schlüssel hinzugefügt haben, müssen Sie die folgenden Berechtigungen zu `AndroidManifest.xml` hinzufügen:

```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
```

{% alert note %}
Mit der Veröffentlichung von Android M wechselte Android von einem Installationszeit- zu einem Laufzeit-Berechtigungsmodell. Diese beiden Berechtigungen sind jedoch normale Berechtigungen. Sie werden automatisch gewährt, wenn sie im App-Manifest aufgeführt sind. Weitere Informationen finden Sie in der [Dokumentation zu den Berechtigungen](https://developer.android.com/training/permissions/index.html) von Android.
{% endalert %}

## Schritt 4: Nutzersitzungen in Android tracken

### Integration von Callbacks für den Lebenszyklus von Aktivitäten

Aufrufe von `openSession()`, `closeSession()`, [`ensureSubscribedToInAppMessageEvents()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/ensure-subscribed-to-in-app-message-events.html) und die Registrierung von `InAppMessageManager` werden optional automatisch verarbeitet.

#### Lebenszyklusrückrufe für Aktivitäten registrieren

Fügen Sie den folgenden Code in die Methode `onCreate()` Ihrer Klasse `Application` ein:

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

In unserer SDK-Referenzdokumentation finden Sie weitere Informationen zu den für [`BrazeActivityLifecycleCallbackListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-activity-lifecycle-callback-listener/index.html) verfügbaren Parametern.

## Schritt 5: Standort-Tracking aktivieren

Wenn Sie die Braze-Standortermittlung aktivieren möchten, aktualisieren Sie die Datei `braze.xml` so, dass sie `com_braze_enable_location_collection` enthält, und stellen Sie sicher, dass der Wert auf `true` festgelegt ist:

```xml
<bool name="com_braze_enable_location_collection">true</bool>
```

{% alert important %}
Ab Version 3.6.0 des Braze Android-SDK ist die Braze-Standortermittlung standardmäßig deaktiviert.
{% endalert %}

## SDK-Integration abgeschlossen

Braze ist nun in der Lage, [bestimmte Daten aus Ihrer Anwendung]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/) zu erfassen, und Ihre grundlegende Integration sollte abgeschlossen sein.

Lesen Sie die folgenden Artikel, um die [benutzerdefinierte Ereignisverfolgung]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_custom_events/), [Push-Nachrichten]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/), [Content Cards]({{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/integration/) und die gesamte Palette der Braze-Funktionen zu aktivieren.

