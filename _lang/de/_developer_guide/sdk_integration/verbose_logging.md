---
page_order: 1.4
nav_title: Ausführliche Protokollierung
article_title: Ausführliche Protokollierung
description: "Erfahren Sie, wie Sie die ausführliche Protokollierung für das Braze SDK aktivieren, Protokolle zur Fehlerbehebung erfassen und diese an den Braze-Support weiterleiten können."
---

# Ausführliche Protokollierung

> Die ausführliche Protokollierung liefert detaillierte Low-Level-Informationen aus dem Braze SDK und bietet Ihnen Einblick in die Initialisierung des SDK, die Kommunikation mit Servern und die Verarbeitung von Messaging-Kanälen wie Push-Benachrichtigungen, In-App-Nachrichten und Content-Cards.

Wenn etwas nicht wie erwartet funktioniert – beispielsweise eine Push-Benachrichtigung nicht ankommt, eine In-App-Nachricht nicht angezeigt wird oder Nutzerdaten nicht synchronisiert werden –, helfen Ihnen ausführliche Protokolle dabei, die Ursache zu identifizieren. Anstatt zu vermuten, können Sie genau sehen, was das SDK bei jedem Schritt ausführt.

{% alert tip %}
Wenn Sie debuggen möchten, ohne die ausführliche Protokollierung manuell zu aktivieren, können Sie den [SDK-Debugger]({{site.baseurl}}/developer_guide/sdk_integration/debugging) verwenden, um Debugging-Sitzungen direkt im Braze-Dashboard zu erstellen.
{% endalert %}

## Wann sollte ausführliche Protokollierung verwendet werden?

Aktivieren Sie die ausführliche Protokollierung, wenn erforderlich:

- **Überprüfen Sie die Initialisierung des SDK**: Bitte überprüfen Sie, ob das SDK mit dem korrekten SDK-API-Schlüssel und Endpunkt ordnungsgemäß startet.
- **Fehlerbehebung bei der Zustellung von Nachrichten**: Bitte überprüfen Sie, ob Push-Token registriert sind, In-App-Nachrichten ausgelöst werden oder Content-Cards synchronisiert sind.
- **Deeplinks debuggen**: Bitte überprüfen Sie, ob das SDK Deeplinks aus Push-Benachrichtigungen, In-App-Nachrichten oder Content-Cards empfängt und öffnet.
- **SitzungsTracking überprüfen**: Bitte bestätigen Sie, dass die Sitzungen wie erwartet beginnen und enden.
- **Diagnose von Verbindungsproblemen**: Bitte überprüfen Sie die Netzwerkanfragen und -antworten zwischen dem SDK und den Braze-Servern.

## Ausführliche Protokollierung Enablement aktivieren

{% alert important %}
Ausführliche Protokolle sind ausschließlich für Entwicklungs- und Testumgebungen vorgesehen. Bitte deaktivieren Sie die ausführliche Protokollierung, bevor Sie Ihre App in die Produktion freigeben, um zu verhindern, dass vertrauliche Informationen offengelegt werden.
{% endalert %}

{% tabs %}
{% tab Android %}

Bitte aktivieren Sie die ausführliche Protokollierung vor allen anderen SDK-Aufrufen in Ihrer`Application.onCreate()`Methode, um die vollständigsten Ergebnisse zu erfassen.

**Im Code:**

{% subtabs %}
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

**In`braze.xml`:**

```xml
<integer name="com_braze_logger_initial_log_level">2</integer>
```

Um zu überprüfen, ob die ausführliche Protokollierung aktiviert ist, suchen Sie in Ihrer `V/Braze`Logcat-Ausgabe nach. Zum Beispiel:

```
2077-11-19 16:22:49.591 ? V/Braze v9.0.01 .bo.app.d3: Request started
```

Ausführliche Informationen finden Sie unter [Android SDK-Protokollierung]({{site.baseurl}}/developer_guide/sdk_integration#android_enabling-logs).

{% endtab %}
{% tab Swift %}

Stellen Sie die Protokollstufe während der Initialisierung auf`.debug` Ihrem`Braze.Configuration`Objekt ein.

{% subtabs %}
{% subtab SWIFT %}
```swift
let configuration = Braze.Configuration(
  apiKey: "<BRAZE_API_KEY>",
  endpoint: "<BRAZE_ENDPOINT>"
)
configuration.logger.level = .debug
let braze = Braze(configuration: configuration)
```
{% endsubtab %}
{% subtab OBJECTIVE-C %}
```objc
BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:@"<BRAZE_API_KEY>"
                                                                  endpoint:@"<BRAZE_ENDPOINT>"];
[configuration.logger setLevel:BRZLoggerLevelDebug];
Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
```
{% endsubtab %}
{% endsubtabs %}

Die`.debug`Stufe ist die ausführlichste und wird für die Fehlerbehebung empfohlen. Ausführliche Informationen finden Sie unter [SWIFT SDK-Protokollierung]({{site.baseurl}}/developer_guide/sdk_integration#swift_log-levels).

{% endtab %}
{% tab Web %}

Fügen Sie`?brazeLogging=true`als URL-Parameter hinzu oder aktivieren Sie die Protokollierung während der SDK-Initialisierung:

```javascript
braze.initialize('YOUR-API-KEY', {
    baseUrl: 'YOUR-SDK-ENDPOINT',
    enableLogging: true
});
```

Sie können die Protokollierung auch nach der Initialisierung umschalten:

```javascript
braze.toggleLogging();
```

Die Protokolle werden auf dem Tab **„Konsole“** der Entwicklertools Ihres Browsers angezeigt. Ausführliche Informationen finden Sie unter [Internet-SDK-Protokollierung]({{site.baseurl}}/developer_guide/sdk_integration#web_logging).

{% endtab %}
{% tab Unity %}

1. Öffnen Sie die Einstellungen für die Braze-Konfiguration, indem Sie zu **Braze** > **Braze-Konfiguration** navigieren.
2. Bitte wählen Sie das Dropdown-Menü **„Braze Android-Einstellungen anzeigen“** aus.
3. Geben Sie im Feld **„SDK-Protokollstufe**“ bitte ein`0`.

{% endtab %}
{% tab React Native %}

Legen Sie die Protokollstufe während der SDK-Konfiguration fest:

```javascript
const configuration = new Braze.BrazeConfiguration('YOUR-API-KEY', 'YOUR-SDK-ENDPOINT');
configuration.logLevel = Braze.LogLevel.Verbose;
```

{% endtab %}
{% endtabs %}

## Protokolle sammeln

Nachdem Sie die ausführliche Protokollierung aktiviert haben, reproduzieren Sie bitte das Problem, das Sie bei der Fehlerbehebung beheben möchten, und erfassen Sie anschließend die Protokolle über die Konsole oder das Debugging-Tool Ihrer Plattform.

{% tabs %}
{% tab Android %}

Verwenden Sie **Logcat** in Android Studio, um Protokolle zu erfassen:

1. Bitte schließen Sie Ihr Gerät an oder starten Sie einen Emulator.
2. Öffnen Sie in Android Studio **Logcat** über das untere Panel.
3. Bitte verwenden Sie den Filter für`V/Braze`  oder , um die Braze`D/Braze` SDK-Ausgabe zu isolieren.
4. Bitte stellen Sie das Problem nach.
5. Bitte kopieren Sie die relevanten Protokolle und speichern Sie diese in einer Textdatei.

{% endtab %}
{% tab iOS %}

Verwenden Sie die **Konsolen**-App unter MacOS, um Protokolle zu erfassen:

1. Bitte installieren Sie die App auf Ihrem Gerät mit aktivierter ausführlicher Protokollierung.
2. Bitte schließen Sie Ihr Gerät an Ihren Mac an.
3. Öffnen Sie die **Konsolen**-App und wählen Sie Ihr Gerät aus der Seitenleiste **„Geräte“** aus.
4. Bitte verwenden Sie den Filter, um die Protokolle nach`Braze`  oder`BrazeKit`  in der Suchleiste zu filtern.
5. Bitte stellen Sie das Problem nach.
6. Bitte kopieren Sie die relevanten Protokolle und speichern Sie diese in einer Textdatei.

{% endtab %}
{% tab Web %}

Bitte nutzen Sie die Entwicklertools Ihres Browsers:

1. Öffnen Sie die Entwicklertools Ihres Browsers (in der Regel **F12** oder **Cmd+Option+I**).
2. Bitte gehen Sie zum Tab **„Konsole**“.
3. Bitte stellen Sie das Problem nach.
4. Bitte kopieren Sie die Konsolenausgabe und speichern Sie sie in einer Textdatei.

{% endtab %}
{% endtabs %}

{% alert tip %}
Wenn Sie Protokolle für den Braze-Support sammeln, beginnen Sie bitte mit der Protokollierung, bevor Sie Ihre App starten, und setzen Sie diese fort, bis das Problem aufgetreten ist. Dies unterstützt die Erfassung der gesamten Abfolge von Ereignissen.
{% endalert %}

## Ausführliche Protokolle lesen

Ausführliche Protokolle folgen einer einheitlichen Struktur, die Ihnen dabei hilft, die Aktivitäten des SDK nachzuvollziehen. Informationen zur Interpretation der Protokollausgabe für bestimmte Kanäle, einschließlich der zu suchenden Schlüsseleinträge und gängiger Muster der Fehlerbehebung, finden Sie unter [Ausführliche Protokolle lesen]({{site.baseurl}}/developer_guide/sdk_integration/reading_verbose_logs).

## Weitergabe von Protokollen an den Braze-Support

Wenn Sie sich wegen eines SDK-Problems an den Braze-Support wenden, geben Sie bitte Folgendes an:

1. **Ausführliche Protokolldatei**: Eine vollständige Protokollierung vom Zeitpunkt vor dem Start der App bis zum Vorkommen des Problems.
2. **Schritte zur Reproduktion**: Eine klare Beschreibung der Handlungen, die das Problem triggern.
3. **Erwartetes vs. tatsächliches Verhalten**: Was Sie erwartet haben und was stattdessen eingetreten ist.
4. **SDK-Version**: Die Version des Braze SDK, die Sie verwenden.
5. **Plattform und Betriebssystemversion**: Beispielsweise iOS 18.0, Android 14 oder Chrome 120.