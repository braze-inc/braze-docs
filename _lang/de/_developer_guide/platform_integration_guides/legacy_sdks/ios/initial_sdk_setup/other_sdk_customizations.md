---
nav_title: Andere SDK-Anpassungen
article_title: Andere SDK-Anpassungen für iOS
platform: iOS
description: "Dieser Referenzartikel beschreibt die Anpassung des SDK, wie z. B. die Protokollstufe, die IDFA-Erfassung und andere Anpassungen."
page_order: 3

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Andere SDK-Anpassungen

## Braze Protokollstufe

Die Standard-Protokollstufe für das Braze iOS SDK ist minimal oder `8` im folgenden Chart. Diese Stufe unterdrückt den größten Teil der Protokollierung, sodass in einer für die Produktion freigegebenen Anwendung keine sensiblen Informationen protokolliert werden.

Die verfügbaren Protokollstufen sind der folgenden Liste zu entnehmen:

### Protokollstufen

| Ebene    | Beschreibung |
|----------|-------------|
| 0        | Ausführlich. Alle Protokollinformationen werden in der iOS-Konsole protokolliert.  |
| (1 %)        | Fehlerbehebung. Debug- und höhere Protokollinformationen werden in der iOS-Konsole protokolliert.  |
| (2 %)        | Warnung. Warnungen und höhere Protokollinformationen werden in der iOS-Konsole protokolliert.  |
| (4 %)        | Fehler. Fehler- und höhere Protokollinformationen werden in der iOS-Konsole protokolliert.  |
| (8 %)        | Minimal. Minimale Informationen werden in der iOS-Konsole protokolliert. Die Standardeinstellung des SDK. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Ausführliche Protokollierung

Sie können die Protokollstufe auf jeden verfügbaren Wert einstellen. Die Einstellung der Protokollstufe "Ausführlich" oder `0` kann jedoch bei der Fehlersuche in Ihrer Integration sehr nützlich sein. Diese Stufe ist nur für Entwicklungsumgebungen vorgesehen und sollte nicht in einer veröffentlichten Anwendung gewählt werden. Die ausführliche Protokollierung sendet keine zusätzlichen oder neuen Benutzerinformationen an Braze.

### Einstellung der Protokollstufe

Die Protokollstufe kann entweder zur Kompilierzeit oder zur Laufzeit zugewiesen werden:

{% tabs local %}
{% tab Kompilierzeit %}

Fügen Sie ein Wörterbuch mit dem Namen `Braze` zu Ihrer Datei `Info.plist` hinzu. Fügen Sie im Wörterbuch `Braze` den String-Untereintrag `LogLevel` hinzu und setzen Sie den Wert auf `0`. 

{% alert note %}
Vor Braze iOS SDK v4.0.2 muss der Wörterbuchschlüssel `Appboy` anstelle von `Braze` verwendet werden.
{% endalert %} 

Beispiel `Info.plist` Inhalt:

```
<key>Braze</key>
<dict>
  <key>LogLevel</key>
  <string>0</string>
</dict>
```

{% endtab %}
{% tab Laufzeit %}

Fügen Sie `ABKLogLevelKey` im Parameter `appboyOptions` hinzu, der an `startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions:` übergeben wird. Setzen Sie seinen Wert auf die Ganzzahl `0`.

{% subtabs %}
{% subtab OBJECTIVE-C %}

```objc
NSMutableDictionary *appboyOptions = [NSMutableDictionary dictionary];
appboyOptions[ABKLogLevelKey] = @(0);
[Appboy startWithApiKey:@"YOUR-API-KEY"
          inApplication:application
      withLaunchOptions:launchOptions
      withAppboyOptions:appboyOptions];
```

{% endsubtab %}
{% subtab swift %}

```swift
let appboyOptions: [AnyHashable: Any] = [
  ABKLogLevelKey : 0
]
Appboy.start(withApiKey: "YOUR-API-KEY", in:application, withLaunchOptions:launchOptions, withAppboyOptions:appboyOptions)
```

{% endsubtab %}
{% endsubtabs %}

{% alert note %}
Zur Laufzeit kann die Protokollstufe nur mit Braze iOS SDK v4.4.0 oder neuer eingestellt werden. Wenn Sie eine frühere SDK-Version verwenden, legen Sie die Protokollstufe stattdessen bei der Kompilierung fest.
{% endalert %} 

{% endtab %}
{% endtabs %}

## Optionale IDFV-Erhebung - Swift

In früheren Versionen des Braze iOS Swift SDK wurde das Feld IDFV (Identifier for Vendors) automatisch als Geräte-ID des Nutzers erfasst. 

Ab Swift SDK v5.7.0 kann das IDFV-Feld optional deaktiviert werden. Stattdessen setzt Braze eine zufällige UUID als Geräte ID. Weitere Informationen finden Sie unter [Sammeln von IDFV]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/swift_idfv/).

## Optionale IDFA-Erfassung

Die IDFA-Erfassung ist im Braze SDK optional und standardmäßig deaktiviert. Die IDFA-Erfassung ist in Braze nur erforderlich, wenn Sie unsere [Install-Attribution-Integrationen]({{site.baseurl}}/partners/advertising_technologies/attribution/adjust/) verwenden möchten. Die Speicherung des IDFA ist kostenlos, sodass Sie die Vorteile dieser Optionen sofort nach der Veröffentlichung ohne zusätzliche Entwicklungsarbeit nutzen können.

Wir empfehlen daher, den IDFA weiterhin zu erfassen, wenn Sie eines der folgenden Kriterien erfüllen:

- Sie ordnen die Installation einer App einer zuvor geschalteten Werbung zu
- Sie ordnen eine Aktion innerhalb der Anwendung einer zuvor geschalteten Anzeige zu

### iOS 14.5 AppTrackingTransparenz

Apple verlangt eine Genehmigungsabfrage zur IDFA-Erfassung, der die Nutzer aktiv zustimmen müssen.

Zusätzlich zur Implementierung unseres `ABKIDFADelegate`-Protokolls muss Ihre Anwendung zur IDFA-Erfassung auch die Zustimmung der Nutzer über Apples `ATTrackingManager` im App Tracking Transparenz-Framework einholen. Weitere Informationen finden Sie in Apples [Artikel zum Datenschutz für Benutzer](https://developer.apple.com/app-store/user-privacy-and-data-use/).

Die Genehmigungsabfrage im Rahmen der App Tracking-Transparenz erfordert den Eingang `Info.plist`, um Ihre Nutzung des Bezeichners zu erklären:

```
<key>NSUserTrackingUsageDescription</key>
<string>To retarget ads and build a global profile to better serve you things you would like.</string>
```

### Implementieren der IDFA-Erfassung

Gehen Sie zur Implementierung der IDFA-Erfassung wie folgt vor:

##### Schritt 1: ABKIDFADelegate implementieren

Erstellen Sie eine Klasse, die dem Protokoll [`ABKIDFADelegate`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKIDFADelegate.h) entspricht:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
#import "IDFADelegate.h"
#import <AdSupport/ASIdentifierManager.h>
#import <AppTrackingTransparency/AppTrackingTransparency.h>

@implementation IDFADelegate

- (NSString *)advertisingIdentifierString {
  return [[[ASIdentifierManager sharedManager] advertisingIdentifier] UUIDString];
}

- (BOOL)isAdvertisingTrackingEnabledOrATTAuthorized {
  if (@available(iOS 14, *)) {
    return [ATTrackingManager trackingAuthorizationStatus] == ATTrackingManagerAuthorizationStatusAuthorized;
  }
  return [[ASIdentifierManager sharedManager] isAdvertisingTrackingEnabled];
}

@end
```

{% endtab %}
{% tab schnell %}

```swift
import Appboy_iOS_SDK
import AdSupport
import AppTrackingTransparency

class IDFADelegate: NSObject, ABKIDFADelegate {
   func advertisingIdentifierString() -> String {
    return ASIdentifierManager.shared().advertisingIdentifier.uuidString
  }

  func isAdvertisingTrackingEnabledOrATTAuthorized() -> Bool {
    if #available(iOS 14, *) {
      return ATTrackingManager.trackingAuthorizationStatus ==  ATTrackingManager.AuthorizationStatus.authorized
    }
    return ASIdentifierManager.shared().isAdvertisingTrackingEnabled
  }
}
```
{% endtab %}
{% endtabs %}

##### Schritt 2: Delegaten während der Braze-Initialisierung festlegen

Legen Sie in dem an `startWithApiKey:inApplication:withAppboyOptions:` übergebenen Wörterbuch `appboyOptions` den Schlüssel `ABKIDFADelegateKey` auf eine Instanz Ihrer mit `ABKIDFADelegate` übereinstimmenden Klasse fest.

## Ungefähre Größe des iOS SDK {#ios-sdk-size}

Die ungefähre Größe der iOS SDK-Framework-Datei beträgt 30 MB. Die ungefähre Größe der -ipa-Datei (zusätzlich zur App-Datei) liegt zwischen 1 MB und 2 MB.

Braze misst die Größe unseres iOS-SDKs, indem es die Auswirkungen des SDKs auf die Größe der `.ipa` beobachtet. Dieser Vorgehensweise liegen die [Empfehlungen von Apple zur App-Größe](https://developer.apple.com/library/content/qa/qa1795/_index.html) zugrunde. Wenn Sie den Größenzuwachs Ihrer Anwendung durch das iOS SDK berechnen, empfehlen wir Ihnen, [einen Bericht zur App-Größe abzurufen](https://developer.apple.com/library/content/qa/qa1795/_index.html), um den Größenunterschied der `.ipa` vor und nach der Integration des Braze iOS SDK zu vergleichen. Wenn Sie die Größen aus dem Bericht zur App-Ausdünnung vergleichen, empfehlen wir Ihnen, auch die App-Größen für ausgedünnte `.ipa` Dateien zu betrachten, da die universellen `.ipa` Dateien größer sind als die Binärdateien, die aus dem App Store heruntergeladen und auf den Benutzergeräten installiert werden.

{% alert note %}
Wenn Sie über CocoaPods mit `use_frameworks!` integrieren, stellen Sie `Enable Bitcode = NO` in den Build-Einstellungen des Ziels ein, um eine genaue Größenbestimmung zu erreichen.
{% endalert %}

