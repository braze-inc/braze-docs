---
nav_title: Verzögerte Initialisierung
article_title: Verzögerte Initialisierung für das Braze Swift SDK
platform: Swift
page_order: 6
description: "Dieser Artikel beschreibt, wie Sie die verzögerte Initialisierung des Swift SDK implementieren, um die Handhabung von Push-Benachrichtigungen zu erhalten, wenn das SDK asynchron initialisiert wird."

---

# Verzögerte Initialisierung für das Braze Swift SDK

> Lernen Sie, wie Sie Ihr Braze Swift SDK asynchron initialisieren und dabei sicherstellen, dass die Push-Benachrichtigung erhalten bleibt. Dies kann nützlich sein, wenn Sie vor der Initialisierung des SDK andere Dienste einrichten müssen, wie z. B. das Abrufen von Konfigurationsdaten von einem Server oder das Warten auf die Nutzerzustimmung.

## Verzögerte Initialisierung einrichten

### Schritt 1: SDK für die verzögerte Initialisierung vorbereiten

Wenn ein:e Endnutzer:in Ihre Push-Benachrichtigung öffnet, während sich Ihre App in einem beendeten Zustand befindet, kann die Push-Benachrichtigung standardmäßig nicht verarbeitet werden, bevor das SDK initialisiert ist.

Ab [Braze Swift SDK Version 10.1.0](https://github.com/braze-inc/braze-swift-sdk/releases/tag/10.1.0) können Sie dies mit der statischen Hilfsmethode [Braze.prepareForDelayedInitialization(pushAutomation:)](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/preparefordelayedinitialization(pushautomation:)) erledigen. Diese Methode bereitet das SDK auf die verzögerte Initialisierung vor, indem sie das Push-Automatisierungssystem einrichtet.

Bevor das SDK initialisiert wird, werden alle Push-Benachrichtigungen, die von Braze stammen, erfasst und in eine Warteschlange gestellt. Nach der Initialisierung des SDK werden diese Push-Benachrichtigungen vom SDK verarbeitet. Diese Methode muss so früh wie möglich im Lebenszyklus Ihrer Anwendung aufgerufen werden, entweder in oder vor der Methode `application(_:didFinishLaunchingWithOptions:)` Methode von `AppDelegate`.

{% alert note %}
Das Swift SDK erfasst keine Push-Benachrichtigungen, die nicht von Braze stammen – diese werden weiterhin von den Systemdelegiertenmethoden behandelt.
{% endalert %}

{% tabs %}
{% tab Swift - UIKit %}
```swift
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
  // Prepare the SDK for delayed initialization
  Braze.prepareForDelayedInitialization()

  // ... Additional non-Braze setup code

  return true
}
```
{% endtab %}

{% tab Swift - SwiftUI %}
SwiftUI-Anwendungen erfordern die Implementierung des Wrappers der Eigenschaft [@UIApplicationDelegateAdaptor](https://developer.apple.com/documentation/swiftui/uiapplicationdelegateadaptor), um die Methode `prepareForDelayedInitialization()` aufzurufen.

```swift
@main
struct MyApp: App {
  @UIApplicationDelegateAdaptor var appDelegate: AppDelegate

  var body: some Scene {
    WindowGroup {
      ContentView()
    }
  }
}

class AppDelegate: NSObject, UIApplicationDelegate {
  
  func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey : Any]? = nil) -> Bool {
    // Prepare the SDK for delayed initialization
    Braze.prepareForDelayedInitialization()

    // ... Additional non-Braze setup code

    return true
  }
  
}
```
{% endtab %}

{% tab Objective-C %}
```objc
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  // Prepare the SDK for delayed initialization
  [Braze prepareForDelayedInitialization];
  
  // ... Additional non-Braze setup code

  return YES;
}

```
{% endtab %}
{% endtabs %}

{% alert note %}
[Braze.prepareForDelayedInitialization(pushAutomation:)](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/preparefordelayedinitialization(pushautomation:)) nimmt einen optionalen `pushAutomation`-Parameter entgegen, der die Automatisierung für Push-Benachrichtigungen darstellt. Wenn [Braze.Configuration.Push.Automation](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/push-swift.class/automation-swift.class)`nil` ist, sind alle Features der Automatisierung aktiviert, mit Ausnahme der Autorisierungsanfrage beim Start.
{% endalert %}

### Schritt 2: Initialisierung des Braze SDK

Nachdem Sie das SDK für eine verzögerte Initialisierung vorbereitet haben, können Sie das SDK jederzeit in der Zukunft asynchron initialisieren. Dann verarbeitet das SDK alle Push-Benachrichtigungen in der Warteschlange, die von Braze stammen.

Um das Braze SDK zu initialisieren, befolgen Sie den [Standard-Initialisierungsprozess des Swift SDK]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/completing_integration/).

## Überlegungen

Wenn Sie `Braze.prepareForDelayedInitialization(pushAutomation:)` verwenden, konfigurieren Sie das SDK so, dass es automatisch die Features zur Automatisierung von Push-Benachrichtigungen verwendet. Alle Systemdelegiertenmethoden, die Push-Benachrichtigungen verarbeiten, werden nicht für Push-Benachrichtigungen aufgerufen, die von Braze stammen.

Das SDK verarbeitet eine Push-Benachrichtigung von Braze und die daraus resultierende Aktion erst, **nachdem** das SDK initialisiert wurde. Wenn ein:e Nutzer:in zum Beispiel auf eine Push-Benachrichtigung tippt, die einen Deeplink setzt, wird der Deeplink erst geöffnet, nachdem die `Braze`-Instanz initialisiert wurde.

Wenn Sie Push-Benachrichtigungen von Braze zusätzlich verarbeiten müssen, lesen Sie den Abschnitt [Updates für Push-Benachrichtigungen abonnieren]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#subscribing-to-push-notifications-updates). Denken Sie daran: Um Updates für Push-Benachrichtigungen zu erhalten, die zuvor in die Warteschlange gestellt wurden, müssen Sie den Handler für Abonnements direkt nach der Initialisierung des SDK implementieren.
