---
nav_title: Live-Aktivitäten
article_title: Live-Aktivitäten für iOS
platform: Swift
page_order: 1
description: "Dieser Artikel beschreibt die Verwendung von Braze zur Verwaltung von Token für Live-Aktivitäten für das Swift SDK."

---

# Live-Aktivitäten

> Live-Aktivitäten sind dauerhafte, interaktive Benachrichtigungen, die auf Ihrem Sperrbildschirm angezeigt werden, sodass Sie in Echtzeit informiert werden. Da sie auf dem Sperrbildschirm angezeigt werden, ist sichergestellt, dass Sie keine Benachrichtigungen mehr verpassen. Da sie beständig sind, können Sie Ihren Nutzern aktuelle Inhalte anzeigen, ohne dass sie ihr Telefon entsperren müssen. 

![Live-Aktivität mit Zustellungs-Tracker auf dem Sperrbildschirm eines iPhones. Eine Statusleiste mit einem Auto ist fast zur Hälfte gefüllt. Der Text lautet "2 Minuten bis zur Abholung"]({% image_buster /assets/img/swift/live_activities/example_2.png %}){: style="max-width:40%;float:right;margin-left:15px;"}

Live-Aktivitäten stellen eine Kombination aus statischen und dynamischen Informationen dar, die Sie aktualisieren. Sie können zum Beispiel eine Live-Aktivität mit einem Status-Tracker für eine Zustellung erstellen. Diese Live-Aktivität enthält den Namen Ihres Unternehmens als statische Information sowie eine dynamische "Zeit bis zur Lieferung", die aktualisiert wird, wenn sich der Zusteller seinem Ziel nähert.

Als Entwickler können Sie mit Braze Ihre Live-Aktivitäts-Lebenszyklen verwalten, die Braze REST API aufrufen, um Live-Aktivitäts-Updates durchzuführen, und dafür sorgen, dass alle abonnierten Geräte das Update so schnell wie möglich erhalten. Und da Sie die Live-Aktivitäten über Braze verwalten, können Sie sie zusammen mit Ihren anderen Nachrichtenkanälen – Push-Benachrichtigungen, In-App-Nachrichten, Content-Cards – einsetzen, um die Akzeptanz zu steigern.

## Voraussetzungen 

{% sdk_min_versions swift:5.11.0 %}

Weitere Voraussetzungen sind:

- Live-Aktivitäten sind nur für iPhones und iPads mit iOS 16.1 und höher verfügbar. Um dieses Feature zu nutzen, stellen Sie sicher, dass Ihr Projekt für diese iOS-Version ausgelegt ist.
- In Ihrem Xcode-Projekt muss die Berechtigung `Push Notification` unter **Signing & Capabilities** hinzugefügt werden.
- Live-Aktivitäten erfordern die Verwendung eines `.p8`-Schlüssels, um die Benachrichtigung zu senden. Ältere Dateien wie `.p12` oder `.pem` werden nicht unterstützt.
- Ab Version 8.2.0 des Braze Swift SDK wird die [Remote-Registrierung einer Live-Aktivität](#step-2-start-the-activity) unterstützt. Um dieses Features zu nutzen, ist iOS 17.2 oder höher erforderlich.

{% alert note %}
Live-Aktivitäten und Push-Benachrichtigungen sind zwar ähnlich, aber ihre Systemberechtigungen sind unterschiedlich. Standardmäßig sind alle Features für Live-Aktivitäten aktiviert, aber die Nutzer können dieses Feature pro App deaktivieren.
{% endalert %}

## Eine Live-Aktivität implementieren

### Schritt 1: Eine Aktivität erstellen

Vergewissern Sie sich zunächst, dass Sie in Ihrer iOS-Anwendung Live-Aktivitäten wie unter [Displaying live data with Live Activities](https://developer.apple.com/documentation/activitykit/displaying-live-data-with-live-activities) in der Dokumentation von Apple beschrieben eingerichtet haben. Als Teil dieser Aufgabe stellen Sie sicher, dass Sie `NSSupportsLiveActivities` mit der Einstellung `YES` in Ihr `Info.plist` aufnehmen.

Da die genaue Art Ihrer Live-Aktivität spezifisch für Ihren Geschäftsfall sein wird, müssen Sie die [Aktivitätsobjekte](https://developer.apple.com/documentation/activitykit/activityattributes) einrichten und initialisieren. Insbesondere muss Folgendes definiert werden:
* `ActivityAttributes`: Dieses Protokoll definiert die statischen (unveränderlichen) und die dynamischen (sich ändernden) Inhalte Ihrer Live-Aktivität.
* `ActivityAttributes.ContentState`: Dieser Typ definiert die dynamischen Daten, die im Verlauf der Aktivität aktualisiert werden.

Außerdem verwenden Sie SwiftUI, um die UI-Präsentation des Sperrbildschirms und des Dynamic Island auf unterstützten Geräten zu erstellen. 

Stellen Sie sicher, dass Sie mit den [Voraussetzungen und Einschränkungen](https://developer.apple.com/documentation/activitykit/displaying-live-data-with-live-activities#Understand-constraints) von Apple für Live-Aktivitäten vertraut sind, da diese Einschränkungen unabhängig von Braze sind.

{% alert note %}
Wenn Sie erwarten, dass Sie häufig Push-Nachrichten an dieselbe Live-Aktivität senden, können Sie vermeiden, dass Sie von Apples Budgetgrenze gedrosselt werden, indem Sie `NSSupportsLiveActivitiesFrequentUpdates` in Ihrer `Info.plist` Datei auf `YES` setzen. Weitere Einzelheiten finden Sie im Abschnitt [`Determine the update frequency`](https://developer.apple.com/documentation/activitykit/updating-and-ending-your-live-activity-with-activitykit-push-notifications#Determine-the-update-frequency) der ActivityKit-Dokumentation.
{% endalert %}

#### Beispiel

Stellen wir uns vor, wir möchten eine Live-Aktivität erstellen, um unsere Nutzer über die Show Superb Owl auf dem Laufenden zu halten, bei der zwei konkurrierende Tierrettungsorganisationen Punkte für die Eulen erhalten, die sie im Haus haben. Für dieses Beispiel haben wir eine Struktur namens `SportsActivityAttributes` erstellt. Sie können jedoch auch Ihre eigene Implementierung von `ActivityAttributes` verwenden.

```swift
#if canImport(ActivityKit)
  import ActivityKit
#endif

@available(iOS 16.1, *)
struct SportsActivityAttributes: ActivityAttributes {
  public struct ContentState: Codable, Hashable {
    var teamOneScore: Int
    var teamTwoScore: Int
  }

  var gameName: String
  var gameNumber: String
}
```

### Schritt 2: Starten Sie die Aktivität

Wählen Sie zunächst, wie Sie Ihre Aktivität registrieren möchten:

- **Remote:** Verwenden Sie die Methode [`registerPushToStart`](<http://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/liveactivities-swift.class/registerpushtostart(fortype:name:)>) so früh wie möglich im Anwendungs- und Nutzer-Lebenszyklus (und bevor das Push to Start-Token benötigt wird). Starten Sie dann eine Aktivität über den Endpunkt [`/messages/live_activity/start`]({{site.baseurl}}/api/endpoints/messaging/live_activity/start).
- **Lokal:** Erstellen Sie eine Instanz Ihrer Live-Aktivität und verwenden Sie dann die [`launchActivity`](<https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/liveactivities-swift.class/launchactivity(pushtokentag:activity:fileid:line:)>) Methode, um Push-Token zu erstellen, die Braze verwalten soll.

{% tabs local %}
{% tab remote %}
{% alert important %}
Um eine Live-Aktivität remote zu registrieren, ist iOS 17.2 oder höher erforderlich.
{% endalert %}

#### Schritt 2.1: BrazeKit zu Ihrer Widget-Erweiterung hinzufügen

Wählen Sie im Xcode-Projekt den Namen Ihrer App und dann **Allgemein** aus. Prüfen Sie unter **Frameworks und Bibliotheken**, ob `BrazeKit` aufgeführt ist.

![BrazeKit-Framework unter "Frameworks und Bibliotheken" in einem Xcode-Beispielprojekt.]({% image_buster /assets/img/swift/live_activities/xcode_frameworks_and_libraries.png %})

#### Schritt 2.2: Fügen Sie das Protokoll BrazeLiveActivityAttributes hinzu

Fügen Sie in der Implementierung von `ActivityAttributes` Konformität mit dem Protokoll `BrazeLiveActivityAttributes` hinzu und fügen Sie dann den String `brazeActivityId` zu Ihrem Attributmodell hinzu. Sie müssen dieser Zeichenkette keinen Wert zuweisen.

```swift
import BrazeKit

#if canImport(ActivityKit)
  import ActivityKit
#endif

@available(iOS 16.1, *)
struct SportsActivityAttributes: ActivityAttributes, BrazeLiveActivityAttributes {
  public struct ContentState: Codable, Hashable {
    var teamOneScore: Int
    var teamTwoScore: Int
  }

  var gameName: String
  var gameNumber: String
  var brazeActivityId: String?
}
```

#### Schritt 2.3: Für Push-to-Start registrieren

Als nächstes registrieren Sie den Typ der Live-Aktivität, damit Braze alle Push-to-Start-Token und Live-Aktivitätsinstanzen, die mit diesem Typ verbunden sind, verfolgen kann.

{% alert warning %}
Das iOS-Betriebssystem erzeugt Push-to-Start-Tokens nur bei der ersten App-Installation nach dem Neustart eines Geräts. Um sicherzustellen, dass Ihre Token zuverlässig registriert sind, rufen Sie `registerPushToStart` in der Methode `didFinishLaunchingWithOptions` auf.
{% endalert %}

###### Beispiel

Im folgenden Beispiel werden Objekte des Typs "Live-Aktivität" von der Klasse `LiveActivityManager` verarbeitet. Dann erfolgt die Registrierung von `SportActivityAttributes` mit der Methode `registerPushToStart`:

```swift
import BrazeKit

#if canImport(ActivityKit)
  import ActivityKit
#endif

class LiveActivityManager {

  @available(iOS 17.2, *)
  func registerActivityType() {
    // This method returns a Swift background task.
    // You may keep a reference to this task if you need to cancel it wherever appropriate, or ignore the return value if you wish.
    let pushToStartObserver: Task = Self.braze?.liveActivities.registerPushToStart(
      forType: Activity<SportsActivityAttributes>.self,
      name: "SportsActivityAttributes"
    )
  }

}
```

#### Schritt 2.4: Push-to-Start-Benachrichtigung senden

Senden Sie remote eine Push-to-Start-Benachrichtigung über den Endpunkt [`/messages/live_activity/start`]({{site.baseurl}}/api/endpoints/messaging/live_activity/start).
{% endtab %}

{% tab local %}
Sie können [Apples ActivityKit Framework](https://developer.apple.com/documentation/activitykit) verwenden, um ein Push-Token zu erhalten, das das Braze SDK für Sie verwalten kann. Damit können Sie Live-Aktivitäten über die Braze API aktualisieren, da Braze das Push-Token an den Apple Push Notification Service (APNs) im Backend sendet.

1. Erstellen Sie eine Instanz Ihrer Live Activity-Implementierung unter Verwendung der ActivityKit-APIs von Apple.
2. Stellen Sie den Parameter `pushType` auf `.token` ein. 
3. Geben Sie die von Ihnen definierten Live-Aktivitäten `ActivitiesAttributes` und `ContentState` ein. 
4. Registrieren Sie Ihre Aktivität bei der Braze-Instanz, indem Sie sie in [`launchActivity(pushTokenTag:activity:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/liveactivities-swift.class) übergeben. Der Parameter `pushTokenTag` ist eine von Ihnen definierte Zeichenkette. Sie sollte für jede Live-Aktivität, die Sie erstellen, eindeutig sein.

Sobald Sie die Live-Aktivität registriert haben, extrahiert und beobachtet das Braze SDK Änderungen an den Push-Tokens.

#### Beispiel

Für unser Beispiel erstellen wir eine Klasse namens `LiveActivityManager` als Schnittstelle für unsere Live Activity-Objekte. Dann setzen wir die `pushTokenTag` auf `"sports-game-2024-03-15"`.

```swift
import BrazeKit

#if canImport(ActivityKit)
  import ActivityKit
#endif

class LiveActivityManager {
  
  @available(iOS 16.2, *)
  func createActivity() {
    let activityAttributes = SportsActivityAttributes(gameName: "Superb Owl", gameNumber: "Game 1")
    let contentState = SportsActivityAttributes.ContentState(teamOneScore: "0", teamTwoScore: "0")
    let activityContent = ActivityContent(state: contentState, staleDate: nil)
    if let activity = try? Activity.request(attributes: activityAttributes,
                                            content: activityContent,
      // Setting your pushType as .token allows the Activity to generate push tokens for the server to watch.
                                            pushType: .token) {
      // Register your Live Activity with Braze using the pushTokenTag.
      // This method returns a Swift background task.
      // You may keep a reference to this task if you need to cancel it wherever appropriate, or ignore the return value if you wish.
      let liveActivityObserver: Task = AppDelegate.braze?.liveActivities.launchActivity(pushTokenTag: "sports-game-2024-03-15",
                                                                                        activity: activity)
    }
  }
  
}
```

Ihr Live-Aktivitäts-Widget zeigt Ihren Nutzern diese ersten Inhalte an. 

![Eine Live-Aktivität auf dem Sperrbildschirm eines iPhones mit den Spielständen von zwei Mannschaften. Beide Teams – das Wild Bird Fund Team und das Owl Rehab Team – haben eine Punktzahl von 0.]({% image_buster /assets/img/swift/live_activities/example_1_1.png %}){: style="max-width:40%;"}
{% endtab %}
{% endtabs %}

### Schritt 3: Aktivitäts-Tracking fortsetzen

So stellen Sie sicher, dass Braze Ihre Live-Aktivitäten beim Start der App verfolgt:

1. Öffnen Sie Ihre `AppDelegate` Datei.
2. Importieren Sie das Modul `ActivityKit`, wenn es verfügbar ist.
3. Rufen Sie [`resumeActivities(ofType:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/liveactivities-swift.class/resumeactivities(oftype:))`ActivityAttributes` in `application(_:didFinishLaunchingWithOptions:)` für alle Typen auf, die Sie in Ihrer Anwendung registriert haben.

Dadurch kann Braze die Aufgaben zur Verfolgung von Push-Token-Aktualisierungen für alle aktiven Live-Aktivitäten wieder aufnehmen. Beachten Sie, dass die Live-Aktivität als entfernt gilt, wenn ein Benutzer sie explizit von seinem Gerät entfernt hat, und dass Braze sie dann nicht mehr verfolgt.

###### Beispiel

```swift
import UIKit
import BrazeKit

#if canImport(ActivityKit)
  import ActivityKit
#endif

@main
class AppDelegate: UIResponder, UIApplicationDelegate {

  static var braze: Braze? = nil

  func application(
    _ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
  ) -> Bool {
    
    if #available(iOS 16.1, *) {
      Self.braze?.liveActivities.resumeActivities(
        ofType: Activity<SportsActivityAttributes>.self
      )
    }

    return true
  }
}
```

### Schritt 4: Aktivität aktualisieren

![Eine Live-Aktivität auf dem Sperrbildschirm eines iPhones mit den Spielständen zweier Mannschaften. Das Wild Bird Fund Team hat 2 Punkte und das Owl Rehab Team hat 4 Punkte.]({% image_buster /assets/img/swift/live_activities/example_1_2.png %}){: style="max-width:40%;float:right;margin-left:15px;"}

Über den Endpunkt [`/messages/live_activity/update`]({{site.baseurl}}/api/endpoints/messaging/live_activity/update) können Sie eine Live-Aktivität durch Push-Benachrichtigungen aktualisieren, die über die Braze REST API übermittelt werden. Verwenden Sie diesen Endpunkt, um den `ContentState` Ihrer Live-Aktivität zu aktualisieren.

Durch die Aktualisierung von `ContentState` werden im Widget "Live-Aktivität" die neuen Informationen angezeigt. So könnte die Superb Owl Show am Ende der ersten Hälfte aussehen.

Ausführliche Informationen finden Sie in unserem Artikel [`/messages/live_activity/update` endpoint]({{site.baseurl}}/api/endpoints/messaging/live_activity/update).

### Schritt 5: Aktivität beenden

Wenn eine Live-Aktivität aktiv ist, wird sie sowohl auf dem Sperrbildschirm des Nutzers als auch in der Dynamic Island angezeigt. Es gibt verschiedene Möglichkeiten, eine Live-Aktivität zu beenden und aus der UI eines Nutzers zu entfernen. 

* **Ausblendung durch den Nutzer**: Ein Benutzer kann eine Live-Aktivität manuell beenden.
* **Timeout**: Nach einer Standardzeit von 8 Stunden entfernt iOS die Live-Aktivität aus der Dynamic Island des Nutzers. Nach einer Standardzeit von 12 Stunden entfernt iOS die Live-Aktivität vom Sperrbildschirm des Nutzers. 
* **Ausblendungsdatum**: Sie können ein Datum angeben, zu dem eine Live-Aktivität vor Ablauf der Zeit aus der Benutzeroberfläche entfernt werden soll. Dieses wird entweder in der `ActivityUIDismissalPolicy` der Aktivität oder über den Parameter `dismissal_date` in Anfragen an den Endpunkt `/messages/live_activity/update` definiert.
* **Beenden der Aktivität**: Sie können `end_activity` in einer Anfrage an den Endpunkt `/messages/live_activity/update` auf `true` setzen, um eine Live-Aktivität sofort zu beenden.

Ausführliche Informationen finden Sie in unserem Artikel [`/messages/live_activity/update` endpoint]({{site.baseurl}}/api/endpoints/messaging/live_activity/update).

## Fehlersuche

Weitere Details zur Fehlerbehebung oder häufig gestellte Fragen finden Sie in unseren [FAQ]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/live_activities/faq/).

