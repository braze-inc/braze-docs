---
nav_title: Datenschutz-Manifest
article_title: Datenschutz-Manifest
page_order: 7
platform: Swift
description: "Erfahren Sie, wie Sie Ihre Braze-Tracking-Daten im Datenschutzmanifest Ihrer App deklarieren."
---

# Datenschutz-Manifest

> Wenn Ihr Braze SDK Tracking-Daten sammelt, verlangt Apple, dass Sie ein Datenschutzmanifest hinzufügen, in dem Sie den Grund und die Methode für die Sammlung von Tracking-Daten beschreiben.

## Was sind Tracking-Daten?

Apple definiert "Tracking-Daten" als Daten, die in Ihrer App über einen Endnutzer oder ein Gerät gesammelt werden und die mit Daten von Drittanbietern (z.B. gezielte Werbung) oder einem Datenbroker verknüpft sind. Eine vollständige Definition mit Beispielen finden Sie unter [Apple: Tracking](https://developer.apple.com/app-store/app-privacy-details/#user-tracking).

Standardmäßig sammelt das Braze SDK keine Tracking Daten. Je nach Konfiguration Ihres Braze SDK müssen Sie jedoch möglicherweise Braze-spezifische Daten im Datenschutzmanifest Ihrer App aufführen.

## Was ist ein Datenschutzmanifest?

Ein Datenschutzmanifest ist eine Datei in Ihrem Xcode-Projekt, die den Grund für die Datenerfassung durch Ihre App und SDKs von Drittanbietern sowie deren Datenerfassungsmethoden beschreibt. Jedes Ihrer externen SDKs, das Daten trackt, benötigt ein eigenes Datenschutzmanifest. Wenn Sie [den Datenschutzbericht Ihrer App erstellen](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests#4239187), werden diese Datenschutzmanifestdateien automatisch in einem einzigen Bericht zusammengefasst.

## API Tracking-Daten-Domains

Ab iOS 17.2 blockiert Apple alle deklarierten Tracking Endpunkte in Ihrer App, bis der Nutzer:in eine [Aufforderung zur Transparenz von Ad Tracking (ATT](https://support.apple.com/en-us/HT212025)) zustimmt. Braze stellt Tracking-Endpunkte bereit, über die Sie Ihre Tracking-Daten weiterleiten können. Gleichzeitig ist es zulässig, First-Party-Daten, die nicht zum Tracking gehören, an den ursprünglichen Endpunkt weiterzuleiten. 

## Deklarieren der Tracking-Daten von Braze

{% alert tip %}
Eine vollständige Anleitung finden Sie in der [Anleitung zum Tracken von geschützten Daten](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/e1-privacy-tracking/).
{% endalert %}

### Schritt 1: Überprüfen Sie Ihre aktuellen Richtlinien

Lassen Sie die aktuellen Datenerfassungseinstellungen in Ihrem Braze SDK rechtlich prüfen, um festzustellen, ob die Erfassung von Tracking-Daten in Ihrer App den [Vorgaben von Apple](#what-is-tracking-data) entspricht. Wenn Sie keine Tracking-Daten sammeln, müssen Sie Ihr Datenschutzmanifest für das Braze SDK zu diesem Zeitpunkt nicht anpassen. Weitere Informationen über die Einstellungen im Braze SDK zur Datenerfassung finden Sie unter [Datenerfassung im SDK]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/sdk_data_collection/).

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
