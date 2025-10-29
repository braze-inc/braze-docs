{% multi_lang_include developer_guide/prerequisites/swift.md %}

## Google Tag Manager:in für Swift verwenden

Im folgenden Beispiel möchte eine App für das Streamen von Musik verschiedene Ereignisse protokollieren, wenn Nutzer:innen Lieder anhören. Mit dem Google Tag Manager für iOS können sie steuern, welche der Braze-Drittanbieter dieses Ereignis erhalten und Tags speziell für Braze erstellen.

### Schritt 1: Erstellen Sie einen Trigger für angepasste Events

Benutzerdefinierte Ereignisse werden protokolliert, wenn `actionType` auf `logEvent` eingestellt ist. In diesem Beispiel erwartet der Anbieter der angepassten Tags von Braze, dass der Name des angepassten Events mit `eventName` festgelegt wird.

Erstellen Sie zunächst einen Trigger, der nach einer `eventName` sucht, die gleich `played song` ist.

![Ein angepasster Trigger in Google Tag Manager, der für einige Events triggert, wenn "eventName" gleich "played song" ist.]({% image_buster /assets/img/android_google_tag_manager/gtm_android_trigger.png %})

Als nächstes erstellen Sie ein neues Tag (auch "Funktionsaufruf" genannt) und geben den Klassenpfad Ihres [angepassten Tag-Anbieters](#adding-ios-google-tag-provider) ein, der später in diesem Artikel beschrieben wird. Dieser Tag wird ausgelöst, wenn Sie das Ereignis `played song` protokollieren. Da `eventName` auf `played song` eingestellt ist, wird es als angepasster Event-Name verwendet, der in Braze protokolliert wird.

{% alert important %}
Wenn Sie ein angepasstes Event senden, setzen Sie `actionType` auf `logEvent`, und legen Sie einen Wert für `eventName` fest, damit Braze den richtigen Eventnamen und die richtige Aktion erhält.
{% endalert %}

![Ein Tag in Google Tag Manager mit Klassenpfad und Schlüssel-Wert-Paar-Feldern. Dieses Tag ist so eingestellt, dass es mit dem zuvor erstellten Trigger "played song" ausgelöst wird.]({% image_buster /assets/img/android_google_tag_manager/gtm_android_function_call_tag.png %})

Sie können dem Tag auch zusätzliche Schlüssel-Wert-Paar-Argumente hinzufügen, die als Eigenschaften des angepassten Events an Braze gesendet werden. `eventName` und `actionType` werden für angepasste Event-Eigenschaften nicht ignoriert. Im folgenden Beispiel-Tag übergeben Sie `genre`, das über eine Tag-Variable im Google Tag Manager definiert wurde und aus dem angepassten Event stammt, das in der App protokolliert wurde.

Die Event-Eigenschaft `genre` wird als Variable "Firebase - Event Parameter" an Google Tag Manager gesendet, da Google Tag Manager für iOS Firebase als Datenebene verwendet.

![Eine Variable im Google Tag Manager, bei der "genre" als Event-Parameter für das Tag "Braze - Played Song Event" hinzugefügt wird.]({% image_buster /assets/img/android_google_tag_manager/gtm_android_eventname_variable.png %})

Wenn ein Nutzer:in der App ein Lied abspielt, protokollieren Sie ein Ereignis über Firebase und Google Tag Manager unter Verwendung des Firebase Analytics-Ereignisnamens, der mit dem Triggernamen des Tags übereinstimmt, `played song`:

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

### Schritt 2: Angepasste Attribute protokollieren

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

### Schritt 3: Rufen Sie `changeUser()` auf

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

### Schritt 4: Einen angepassten Tag-Anbieter hinzufügen {#adding-ios-google-tag-provider}

Wenn Sie die Tags und Trigger eingerichtet haben, müssen Sie auch den Google Tag Manager in Ihrer iOS App implementieren, den Sie in der Dokumentation von Google finden.

Nachdem Google Tag Manager in Ihrer App installiert ist, fügen Sie einen angepassten Tag-Anbieter hinzu, um Braze SDK-Methoden auf der Grundlage der Tags aufzurufen, die Sie im Google Tag Manager konfiguriert haben.

Achten Sie darauf, den "Class Path" der Datei zu notieren - diesen geben Sie ein, wenn Sie einen Tag in der [Google Tag Manager](https://tagmanager.google.com/) Konsole einrichten.

Dieses Beispiel zeigt eine der vielen Möglichkeiten, wie Sie Ihren angepassten Tag-Anbieter strukturieren können. Insbesondere wird gezeigt, wie Sie anhand des vom GTM Tag gesendeten Schlüssel-Wert-Paares `actionType` ermitteln, welche Methode des Braze SDK aufgerufen werden soll. Dieses Beispiel setzt voraus, dass Sie die Braze-Instanz als Variable im AppDelegate zugewiesen haben.

Die in diesem Beispiel unterstützten `actionType` sind `logEvent`, `customAttribute` und `changeUser`, aber Sie können es vorziehen, zu ändern, wie Ihr Tag-Anbieter Daten von Google Tag Manager:in behandelt.
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
