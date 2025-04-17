## Apples Manifest zum Datenschutz {#privacy-manifest}

### Was sind Tracking-Daten?

Apple definiert "Tracking-Daten" als Daten, die in Ihrer App über einen Endnutzer oder ein Gerät gesammelt werden und die mit Daten von Drittanbietern (z.B. gezielte Werbung) oder einem Datenbroker verknüpft sind. Eine vollständige Definition mit Beispielen finden Sie unter [Apple: Tracking](https://developer.apple.com/app-store/app-privacy-details/#user-tracking).

Standardmäßig sammelt das Braze SDK keine Tracking Daten. Je nach Konfiguration Ihres Braze SDK müssen Sie jedoch möglicherweise Braze-spezifische Daten im Datenschutzmanifest Ihrer App aufführen.

### Was ist ein Datenschutzmanifest?

Ein Datenschutzmanifest ist eine Datei in Ihrem Xcode-Projekt, die den Grund für die Datenerfassung durch Ihre App und SDKs von Drittanbietern sowie deren Datenerfassungsmethoden beschreibt. Jedes Ihrer externen SDKs, das Daten trackt, benötigt ein eigenes Datenschutzmanifest. Wenn Sie [den Datenschutzbericht Ihrer App erstellen](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests#4239187), werden diese Datenschutzmanifestdateien automatisch in einem einzigen Bericht zusammengefasst.

### API Tracking-Daten-Domains

Ab iOS 17.2 blockiert Apple alle deklarierten Tracking Endpunkte in Ihrer App, bis der Nutzer:in eine [Aufforderung zur Transparenz von Ad Tracking (ATT](https://support.apple.com/en-us/HT212025)) zustimmt. Braze stellt Tracking-Endpunkte bereit, über die Sie Ihre Tracking-Daten weiterleiten können. Gleichzeitig ist es zulässig, First-Party-Daten, die nicht zum Tracking gehören, an den ursprünglichen Endpunkt weiterzuleiten. 

## Deklarieren der Tracking-Daten von Braze

{% alert tip %}
Eine vollständige Anleitung finden Sie in der [Anleitung zum Tracken von geschützten Daten](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/e1-privacy-tracking/).
{% endalert %}

### Voraussetzungen

Die folgende Version des Braze SDK ist erforderlich, um dieses Feature zu implementieren:

{% sdk_min_versions swift:9.0.0 %}

### Schritt 1: Überprüfen Sie Ihre aktuellen Richtlinien

Lassen Sie die aktuellen Datenerfassungseinstellungen in Ihrem Braze SDK rechtlich prüfen, um festzustellen, ob die Erfassung von Tracking-Daten in Ihrer App den [Vorgaben von Apple](#what-is-tracking-data) entspricht. Wenn Sie keine Tracking-Daten sammeln, müssen Sie Ihr Datenschutzmanifest für das Braze SDK zu diesem Zeitpunkt nicht anpassen. Weitere Informationen über die Einstellungen im Braze SDK zur Datenerfassung finden Sie unter [Datenerfassung im SDK]({{site.baseurl}}/user_guide/data/user_data_collection/sdk_data_collection/).

{% alert important %}
Wenn eines Ihrer SDKs, das nicht von Braze stammt, Tracking-Daten sammelt, müssen Sie diese separat prüfen.
{% endalert %}

### Schritt 2: Erstellen Sie ein Datenschutzmanifest

Prüfen Sie zunächst, ob Sie bereits ein Datenschutzmanifest haben, indem Sie in Ihrem Xcode-Projekt nach einer `PrivacyInfo.xcprivacy` Datei suchen. Wenn Sie diese Datei bereits haben, können Sie mit dem nächsten Schritt fortfahren. Ansonsten siehe [Apple: Datenschutzmanifest erstellen](sdk-tracking.iad-01.braze.com).

### Schritt 3: Fügen Sie Ihren Endpunkt zum Datenschutzmanifest hinzu

Öffnen Sie in Ihrem Xcode-Projekt die Datei `PrivacyInfo.xcprivacy` Ihrer App, klicken Sie mit der rechten Maustaste auf die Tabelle und aktivieren Sie **Raw Keys and Values**.

{% alert note %}

{% endalert %}

![Ein Xcode-Projekt mit geöffnetem Kontextmenü und markierter Option "Raw Keys and Values".]({% image_buster /assets/img/apple/privacy_manifest/check_raw_keys_and_values.png %})

Wählen Sie unter **App-Datenschutzkonfiguration** **NSPrivacyTracking** und setzen Sie den Wert auf **YES**.

![Die geöffnete Datei "PrivacyInfo.xcprivacy" mit "NSPrivacyTracking" auf "YES" gesetzt.]({% image_buster /assets/img/apple/privacy_manifest/add_nsprivacytracking.png %})

Wählen Sie unter **App-Datenschutzkonfiguration** **NSPrivacyTrackingDomains**. Fügen Sie im Array domains ein neues Element hinzu und setzen Sie dessen Wert auf den Endpunkt, den Sie [zuvor zu Ihrem `AppDelegate` mit dem Präfix `sdk-tracking` hinzugefügt haben]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/completing_integration/#update-your-app-delegate).

![Die geöffnete Datei "PrivacyInfo.xcprivacy" mit einem Braze-Tracking-Endpunkt, der unter "NSPrivacyTrackingDomains" aufgeführt ist.]({% image_buster /assets/img/apple/privacy_manifest/add_nsprivacytrackingdomains.png %})

### Schritt 4: Deklarieren Sie Ihre Tracking Daten

Als Nächstes öffnen Sie `AppDelegate.swift` und listen alle [Tracking-Eigenschaften](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/trackingproperty/) auf, die Sie deklarieren möchten, indem Sie eine statische oder dynamische Tracking-Liste erstellen. Denken Sie daran, dass Apple diese Eigenschaften blockiert, bis der Endnutzer die ATT-Aufforderung akzeptiert. Führen Sie also nur die Eigenschaften auf, die Sie und Ihre Rechtsberatung als Tracking betrachten. Zum Beispiel:

{% tabs %}
{% tab statisches Beispiel %}
Im folgenden Beispiel werden `dateOfBirth`, `customEvent` und `customAttribute` als Tracking Daten innerhalb einer statischen Liste deklariert. 

```swift
import UIKit
import BrazeKit

@main
class AppDelegate: UIResponder, UIApplicationDelegate {

  static var braze: Braze? = nil

  func application(
    _ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
  ) -> Bool {
    let configuration = Braze.Configuration(apiKey: brazeApiKey, endpoint: brazeEndpoint)
    // Declare which types of data you wish to collect for user tracking.
    configuration.api.trackingPropertyAllowList = [
      .dateOfBirth,
      .customEvent(["event-1"]),
      .customAttribute(["attribute-1", "attribute-2"])
    ]
    let braze = Braze(configuration: configuration)
    AppDelegate.braze = braze
    return true
  }
}
```
{% endtab %}

{% tab dynamisches Beispiel %}
In dem folgenden Beispiel wird die Tracking-Liste automatisch aktualisiert, nachdem der Endnutzer die ATT-Aufforderung akzeptiert hat.

```swift
func applicationDidBecomeActive(_ application: UIApplication) {
  // Request and check your user's tracking authorization status.
  ATTrackingManager.requestTrackingAuthorization { status in
    // Let Braze know whether user data is allowed to be collected for tracking.
    let enableAdTracking = status == .authorized
    AppDelegate.braze?.set(adTrackingEnabled: enableAdTracking)

    // Add the `.firstName` and `.lastName` properties, while removing the `.everything` configuration.
    AppDelegate.braze.updateTrackingAllowList(
      adding: [.firstName, .lastName],
      removing: [.everything]
    )
  }
}
```
{% endtab %}
{% endtabs %}

### Schritt 5: Verhindern Sie unendliche Wiederholungsschleifen

Um zu verhindern, dass das SDK in eine unendliche Wiederholungsschleife gerät, verwenden Sie die Methode `set(adTrackingEnabled: enableAdTracking)` zur Behandlung von ATT-Berechtigungen. Die Eigenschaft `adTrackingEnabled` in Ihrer Methode sollte ähnlich wie die folgende behandelt werden:

```swift
func applicationDidBecomeActive(_ application: UIApplication) {
    // Request and check your user's tracking authorization status.
    ATTrackingManager.requestTrackingAuthorization { status in
      // Let Braze know whether user data is allowed to be collected for tracking.
      let enableAdTracking = status == .authorized
      AppDelegate.braze?.set(adTrackingEnabled: enableAdTracking)
    }
}
```

## Deaktivieren des Trackings von Daten

Um die Daten-Tracking-Aktivität im Swift SDK zu deaktivieren, setzen Sie die [`enabled`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/enabled) Eigenschaft in Ihrer Braze-Instanz auf `false`. Wenn `enabled` auf `false` eingestellt ist, ignoriert das Braze SDK alle Aufrufe an die öffentliche API. Das SDK bricht auch alle In-Flight-Aktionen ab, z. B. Netzwerkanfragen, Eventverarbeitung usw. 

## Löschen von zuvor gespeicherten Daten

Sie können die [`wipeData()`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/wipedata()) Methode verwenden, um lokal gespeicherte SDK-Daten auf dem Gerät eines Nutzers:innen vollständig zu löschen.

Für Braze Swift Versionen 7.0.0 und höher generieren das SDK und die `wipeData()` Methode zufällig eine UUID für ihre Geräte ID. Wenn Ihr `useUUIDAsDeviceId` jedoch auf `false` eingestellt ist _oder_ Sie Swift SDK Version 5.7.0 oder früher verwenden, müssen Sie auch eine Post-Anfrage an [`/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/) stellen, da Ihr Identifier for Vendors (IDFV) automatisch als Bezeichner für das Gerät des Nutzers:innen verwendet wird.

## Wiederaufnahme des Trackings von Daten

Um die Datenerfassung wieder aufzunehmen, setzen Sie [`enabled`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/enabled/) auf `true`. Denken Sie daran, dass dadurch keine zuvor gelöschten Daten wiederhergestellt werden können.

## IDFV-Sammlung (Identifier for Vendors)

In früheren Versionen des Braze iOS SDK wurde das Feld IDFV (Identifier for Vendors) automatisch als Geräte-ID des Nutzers erfasst. Ab dem Swift SDK `v5.7.0` wurde das IDFV-Feld optional deaktiviert und stattdessen setzte Braze eine zufällige UUID als Geräte ID. Ab Swift SDK `v7.0.0` wird das IDFV-Feld standardmäßig nicht mehr erfasst und stattdessen eine UUID als Geräte ID festgelegt.

Das Feature `useUUIDAsDeviceId` konfiguriert das [Swift SDK](https://github.com/braze-inc/braze-swift-sdk) so, dass die Geräte-ID als UUID gesetzt wird. Traditionell würde das iOS SDK den von Apple generierten IDFV-Wert als Geräte-ID zuweisen. Wenn diese Funktion in Ihrer iOS-App standardmäßig aktiviert ist, wird allen neuen Benutzern, die über das SDK erstellt werden, eine Geräte-ID zugewiesen, die einer UUID entspricht.

Wenn Sie IDFV dennoch separat erfassen möchten, können Sie [`set(identifierforvendor:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(identifierforvendor:)).

### Überlegungen

#### SDK Version

Wenn `useUUIDAsDeviceId` im Swift SDK `v7.0.0+` aktiviert ist (Standard), wird allen neu angelegten Nutzer:innen eine zufällige Geräte ID zugewiesen. Für alle bereits bestehenden Nutzer wird der Wert der Geräte-ID, was möglicherweise der IDFV war, beibehalten.

Wenn dieses Feature deaktiviert ist, wird den Geräten bei der Erstellung weiterhin der IDFV zugewiesen.

#### Downstream 

**Technologie-Partner**: Wenn dieses Feature aktiviert ist, haben alle Technologiepartner, die den IDFV-Wert von der Braze Geräte-ID ableiten, keinen Zugriff mehr auf diese Daten. Wenn der vom Gerät abgeleitete IDFV-Wert für Ihre Partnerintegration benötigt wird, empfehlen wir Ihnen, dieses Feature auf `false` zu setzen.

**Currents**: `useUUIDAsDeviceId` auf true gesetzt bedeutet, dass die in Currents gesendete Geräte-ID nicht mehr dem IDFV-Wert entspricht.

### Häufig gestellte Fragen

#### Wird sich diese Änderung auf meine bestehenden Benutzer in Braze auswirken?

Nein. Wenn diese Funktion aktiviert ist, überschreibt sie keine Benutzerdaten in Braze. Neue UUID-Geräte-IDs werden nur für neue Geräte erstellt oder wenn `wipedata()` aufgerufen wird.

#### Kann ich diese Funktion ausschalten, nachdem ich sie eingeschaltet habe?

Ja, diese Funktion kann nach Ihrem Ermessen ein- und ausgeschaltet werden. Zuvor gespeicherte Geräte-IDs werden niemals überschrieben.

#### Kann ich den IDFV-Wert auch anderweitig über Braze erfassen?

Ja, Sie können den IDFV weiterhin optional über das Swift SDK erfassen (die Erfassung ist standardmäßig deaktiviert). 
