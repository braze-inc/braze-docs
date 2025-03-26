---
nav_title: Google Tag Manager
article_title: Google Tag Manager für iOS
platform: Swift
page_order: 3
description: "Dieser Artikel beschreibt, wie Sie den Google Tag Manager für das Swift SDK initialisieren, konfigurieren und implementieren."

---

# Google Tag Manager

> Das Braze Swift SDK kann durch Tags, die im Google Tag Manager konfiguriert wurden, initialisiert und gesteuert werden.

Als Voraussetzung für diese Implementierung muss Ihre Swift SDK-Integration vollständig sein.

## Konfigurieren Sie Ihren Google Tag Manager {#configuring-ios-google-tag-manager}

In diesem Beispiel tun wir so, als ob wir eine Musik-Streaming-App wären, die verschiedene Ereignisse protokollieren möchte, während die Benutzer Lieder hören. Mit dem Google Tag Manager für iOS können wir kontrollieren, welche unserer Drittanbieter dieses Ereignis erhalten und Tags speziell für Braze erstellen.

### Angepasste Events

Benutzerdefinierte Ereignisse werden protokolliert, wenn `actionType` auf `logEvent` eingestellt ist. Der Braze Custom Tag Provider in unserem Beispiel erwartet, dass der Name des benutzerdefinierten Ereignisses mit `eventName` festgelegt wird.

Um zu beginnen, erstellen Sie einen Trigger, der nach einem `eventName` sucht, das `played song` entspricht.

![Ein angepasster Trigger in Google Tag Manager, der für einige Events triggert, wenn "eventName" gleich "played song" ist.]({% image_buster /assets/img/android_google_tag_manager/gtm_android_trigger.png %})

Als Nächstes erstellen Sie ein neues Tag ("Funktionsaufruf") und geben den Klassenpfad Ihres [Custom Tag Provider](#adding-ios-google-tag-provider) ein, der später in diesem Artikel beschrieben wird. 

Dieses Tag wird ausgelöst, wenn Sie das soeben erstellte Ereignis `played song` protokollieren. 

In den angepassten Parametern (Schlüssel-Wert-Paare) unseres Beispiel-Tags haben wir `eventName` auf `played song` gesetzt – den Namen des angepassten Events, der in Braze protokolliert wird.

{% alert important %}
Wenn Sie ein angepasstes Event senden, setzen Sie `actionType` auf `logEvent` und legen einen Wert für `eventName` fest, wie im folgenden Beispiel gezeigt.
<br><br>
Der angepasste Tag-Anbieter in unserem Beispiel verwendet diese Schlüssel, um zu bestimmen, welche Aktion er durchführen und welchen Event-Namen er an Braze senden soll, wenn er Daten vom Google Tag Manager erhält.
{% endalert %}

![Ein Tag in Google Tag Manager mit Klassenpfad und Schlüssel-Wert-Paar-Feldern. Dieses Tag ist so eingestellt, dass es mit dem zuvor erstellten Trigger "played song" ausgelöst wird.]({% image_buster /assets/img/android_google_tag_manager/gtm_android_function_call_tag.png %})

Sie können dem Tag auch zusätzliche Schlüssel-Wert-Paar-Argumente hinzufügen, die als Eigenschaften des angepassten Events an Braze gesendet werden. `eventName` und `actionType` werden für angepasste Event-Eigenschaften nicht ignoriert. Im folgenden Beispiel-Tag übergeben wir `genre`, das über eine Tag-Variable im Google Tag Manager definiert wurde und aus dem angepassten Event stammt, das wir in unserer App protokolliert haben.

Die Event-Eigenschaft `genre` wird als Variable "Firebase - Event Parameter" an Google Tag Manager gesendet, da Google Tag Manager für iOS Firebase als Datenebene verwendet.

![Eine Variable im Google Tag Manager, bei der "genre" als Event-Parameter für das Tag "Braze - Played Song Event" hinzugefügt wird.]({% image_buster /assets/img/android_google_tag_manager/gtm_android_eventname_variable.png %})

Wenn ein Benutzer einen Song in unserer App abspielt, protokollieren wir ein Ereignis über Firebase und den Google Tag Manager unter Verwendung des Firebase-Analytics-Ereignisnamens, der mit dem Auslösernamen unseres Tags übereinstimmt: `played song`:

{% tabs %}
{% tab SWIFT %}

```swift
let parameters: [String: Any] = ["genre": "pop",
                                 "number of times listened": 42]
Analytics.logEvent("played song", parameters: parameters)
```

{% endtab %}
{% tab OBJECTIVE-C %}

```obj-c
NSDictionary *parameters = @{@"genre" : @"pop",
                             @"number of times listened" : @42};
[FIRAnalytics logEventWithName:@"played song" parameters:parameters];
```

{% endtab %}
{% endtabs %}

### Benutzerdefinierte Attribute protokollieren

Benutzerdefinierte Attribute werden über `actionType` gesetzt, das auf `customAttribute` eingestellt ist. Der Braze Custom Tag Provider erwartet, dass der Schlüsselwert "angepasstes Attribut" über `customAttributeKey` und `customAttributeValue` gesetzt wird:

{% tabs %}
{% tab SWIFT %}
```swift
let parameters: [String: Any] = ["customAttributeKey": "favoriteSong",
                                 "customAttributeValue": "Private Eyes"]
FIRAnalytics.logEvent(withName:"customAttribute", parameters: parameters)
```
{% endtab %}
{% tab OBJECTIVE-C %}

```obj-c
NSDictionary *parameters = @{@"customAttributeKey" : @"favoriteSong",
                             @"customAttributeValue" : @"Private Eyes"};
[FIRAnalytics logEventWithName:@"customAttribute" parameters:parameters];
```

{% endtab %}

{% endtabs %}

### Aufruf von changeUser

Anrufe an `changeUser()` erfolgen über ein `actionType`, das auf `changeUser` eingestellt ist. Der Braze Custom Tag Provider erwartet, dass die Braze-Benutzer-ID über das Schlüssel-Wert-Paar `externalUserId` in Ihrem Tag festgelegt wird:

{% tabs %}
{% tab SWIFT %}
```swift
let parameters: [String: Any] = ["externalUserId": "favorite userId"]
Analytics.logEvent(withName:"changeUser", parameters: parameters)
```
{% endtab %}
{% tab OBJECTIVE-C %}

```obj-c
NSDictionary *parameters = @{@"externalUserId" : userId};
[FIRAnalytics logEventWithName:@"changeUser" parameters:parameters];
```

{% endtab %}

{% endtabs %}

## Braze SDK Custom Tag Provider {#adding-ios-google-tag-provider}

Wenn Sie die Tags und Trigger eingerichtet haben, müssen Sie auch den Google Tag Manager in Ihrer iOS App implementieren, den Sie in der Dokumentation von Google finden.

Sobald Google Tag Manager in Ihrer App installiert ist, fügen Sie einen benutzerdefinierten Tag-Anbieter hinzu, um Braze SDK-Methoden auf der Grundlage der Tags aufzurufen, die Sie in Google Tag Manager konfiguriert haben. 

Achten Sie darauf, den "Class Path" der Datei zu notieren - diesen geben Sie ein, wenn Sie einen Tag in der [Google Tag Manager](https://tagmanager.google.com/) Konsole einrichten.

Dieses Beispiel zeigt eine von vielen Möglichkeiten, wie Sie Ihren angepassten Tag-Anbieter strukturieren können. Dabei bestimmen wir anhand des vom Google Tag Manager:in gesendeten Schlüssel-Wert-Paares `actionType`, welche Methode des Braze SDK aufgerufen werden soll. Dieses Beispiel setzt voraus, dass Sie die Braze-Instanz als Variable im AppDelegate zugewiesen haben.

Die `actionType`, die wir in unserem Beispiel unterstützt haben, sind `logEvent`, `customAttribute` und `changeUser`, aber Sie können ändern, wie Ihr Tag Provider die Daten von Google Tag Manager verarbeitet.
{% tabs %}
{% tab SWIFT %}

Fügen Sie den folgenden Code in Ihre Datei `BrazeGTMTagManager.swift` ein.
```swift
import FirebaseAnalytics
import GoogleTagManager
import BrazeKit

let ActionTypeKey: String = "actionType"

// Custom Events
let LogEventAction: String = "logEvent"
let LogEventName: String = "eventName"

// Custom Attributes
let CustomAttributeAction: String = "customAttribute"
let CustomAttributeKey: String = "customAttributeKey"
let CustomAttributeValueKey: String = "customAttributeValue"

// Change User
let ChangeUserAction: String = "changeUser"
let ChangeUserExternalUserId: String = "externalUserId"

@objc(BrazeGTMTagManager)
final class BrazeGTMTagManager : NSObject, TAGCustomFunction {
  @objc func execute(withParameters parameters: [AnyHashable : Any]!) -> NSObject! {
    var parameters: [String : Any] = parameters as! [String : Any]
    guard let actionType: String = parameters[ActionTypeKey] as? String else {
      print("There is no Braze action type key in this call. Doing nothing.")
      return nil
    }
    parameters.removeValue(forKey: ActionTypeKey)
    if actionType == LogEventAction {
      logEvent(parameters: parameters)
    } else if actionType == CustomAttributeAction {
      logCustomAttribute(parameters: parameters)
    } else if actionType == ChangeUserAction {
      changeUser(parameters: parameters)
    }
    return nil
  }
  
  func logEvent(parameters: [String : Any]) {
    var parameters: [String : Any] = parameters
    guard let eventName: String = parameters[LogEventName] as? String else { return }
    parameters.removeValue(forKey: LogEventName)
    AppDelegate.braze?.logCustomEvent(name: eventName, properties: parameters)
  }
  
  func logCustomAttribute(parameters: [String: Any]) {
    guard let customAttributeKey = parameters[CustomAttributeKey] as? String else { return }
    let customAttributeValue = parameters[CustomAttributeValueKey]
    
    if let customAttributeValue = customAttributeValue as? String {
      AppDelegate.braze?.user.setCustomAttribute(key: customAttributeKey, value: customAttributeValue)
    } else if let customAttributeValue = customAttributeValue as? Date {
      AppDelegate.braze?.user.setCustomAttribute(key: customAttributeKey, value: customAttributeValue)
    } else if let customAttributeValue = customAttributeValue as? Double {
      AppDelegate.braze?.user.setCustomAttribute(key: customAttributeKey, value: customAttributeValue)
    } else if let customAttributeValue = customAttributeValue as? Bool {
      AppDelegate.braze?.user.setCustomAttribute(key: customAttributeKey, value: customAttributeValue)
    } else if let customAttributeValue = customAttributeValue as? Int {
      AppDelegate.braze?.user.setCustomAttribute(key: customAttributeKey, value: customAttributeValue)
    } else if let customAttibuteValue = customAttributeValue as? [String] {
      AppDelegate.braze?.user.setCustomAttributeArray(key: customAttributeKey, array: customAttibuteValue)
    }
  }
  
  func changeUser(parameters: [String: Any]) {
    guard let userId = parameters[ChangeUserExternalUserId] as? String else { return }
    AppDelegate.braze?.changeUser(userId: userId)
  }
}
```
{% endtab %}
{% tab OBJECTIVE-C %}
Fügen Sie den folgenden Code in Ihre Datei `BrazeGTMTagManager.h` ein:

```obj-c
@import Firebase;
@import GoogleTagManager;

@interface BrazeGTMTagManager : NSObject <TAGCustomFunction>

@end
```

Und fügen Sie den folgenden Code in Ihre `BrazeGTMTagManager.m` Datei ein:

```obj-c
#import <Foundation/Foundation.h>
#import "BrazeGTMTagManager.h"
#import "BrazeKit"
#import "AppDelegate.h"

static NSString *const ActionTypeKey = @"actionType";

// Custom Events
static NSString *const LogEventAction = @"logEvent";
static NSString *const LogEventEventName = @"eventName";

// Custom Attributes
static NSString *const CustomAttributeAction = @"customAttribute";
static NSString *const CustomAttributeKey = @"customAttributeKey";
static NSString *const CustomAttributeValueKey = @"customAttributeValue";

// Change User
static NSString *const ChangeUserAction = @"changeUser";
static NSString *const ChangeUserExternalUserId = @"externalUserId";

@implementation BrazeGTMTagManager

- (NSObject *)executeWithParameters:(NSDictionary *)parameters {
  NSMutableDictionary *mutableParameters = [parameters mutableCopy];
  
  NSString *actionType = mutableParameters[ActionTypeKey];
  if (!actionType) {
    NSLog(@"There is no Braze action type key in this call. Doing nothing.", nil);
    return nil;
  }
  
  [mutableParameters removeObjectForKey:ActionTypeKey];
  
  if ([actionType isEqualToString:LogEventAction]) {
    [self logEvent:mutableParameters];
  } else if ([actionType isEqualToString:CustomAttributeAction]) {
    [self logCustomAttribute:mutableParameters];
  } else if ([actionType isEqualToString:ChangeUserAction]) {
    [self changeUser:mutableParameters];
  } else {
    NSLog(@"Invalid action type. Doing nothing.");
  }
  return nil;
}

- (void)logEvent:(NSMutableDictionary *)parameters {
  NSString *eventName = parameters[LogEventEventName];
  [parameters removeObjectForKey:LogEventEventName];
  [AppDelegate.braze logCustomEvent:eventName
                         properties:parameters];
}

- (void)logCustomAttribute:(NSMutableDictionary *)parameters {
  NSString *customAttributeKey = parameters[CustomAttributeKey];
  id customAttributeValue = parameters[CustomAttributeValueKey];
  
  if ([customAttributeValue isKindOfClass:[NSString class]]) {
    [AppDelegate.braze logCustomEvent:customAttributeKey
                           properties:parameters];
  } else if ([customAttributeValue isKindOfClass:[NSDate class]]) {
    [AppDelegate.braze.user setCustomAttributeWithKey:customAttributeKey
                                            dateValue:customAttributeValue];
  } else if ([customAttributeValue isKindOfClass:[NSNumber class]]) {
    if (strcmp([customAttributeValue objCType], [@(YES) objCType]) == 0) {
      [AppDelegate.braze.user setCustomAttributeWithKey:customAttributeKey
                                              boolValue:[(NSNumber *)customAttributeValue boolValue]];
    } else if (strcmp([customAttributeValue objCType], @encode(short)) == 0 ||
               strcmp([customAttributeValue objCType], @encode(int)) == 0 ||
               strcmp([customAttributeValue objCType], @encode(long)) == 0) {
      [AppDelegate.braze.user setCustomAttributeWithKey:customAttributeKey
                                               intValue:[(NSNumber *)customAttributeValue integerValue]];
    } else if (strcmp([customAttributeValue objCType], @encode(float)) == 0 ||
               strcmp([customAttributeValue objCType], @encode(double)) == 0) {
      [AppDelegate.braze.user setCustomAttributeWithKey:customAttributeKey
                                            doubleValue:[(NSNumber *)customAttributeValue doubleValue]];
    } else {
      NSLog(@"Could not map NSNumber value to Braze custom attribute:%@", customAttributeValue);
    }
  } else if ([customAttributeValue isKindOfClass:[NSArray class]]) {
    [AppDelegate.braze.user setCustomAttributeArrayWithKey:customAttributeKey
                                                     array:customAttributeValue];
  }
}

- (void)changeUser:(NSMutableDictionary *)parameters {
  NSString *userId = parameters[ChangeUserExternalUserId];
  [AppDelegate.braze changeUser:userId];
}

@end
```
{% endtab %}
{% endtabs %}

