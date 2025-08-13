---
nav_title: Google Tag Manager
article_title: Google Tag Manager für iOS
platform: iOS
page_order: 7
description: "Dieser Artikel beschreibt, wie Sie den Google Tag Manager initialisieren, konfigurieren und in Ihre iOS App implementieren."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Google Tag Manager für iOS

## Initialisierung des SDK {#initializing-ios-google-tag-provider}

Das Braze iOS SDK kann durch Tags, die im [Google Tag Manager](https://tagmanager.google.com/):in konfiguriert wurden, initialisiert und gesteuert werden.

Bevor Sie Google Tag Manager verwenden, müssen Sie zunächst die [SDK-Ersteinrichtung]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/) durchführen.

## Konfigurieren Sie Ihren Google Tag Manager {#configuring-ios-google-tag-manager}

In diesem Beispiel tun wir so, als ob wir eine Musik-Streaming-App wären, die verschiedene Ereignisse protokollieren möchte, während die Benutzer Lieder hören. Mit dem Google Tag Manager für iOS können wir kontrollieren, welche unserer Drittanbieter dieses Ereignis erhalten und Tags speziell für Braze erstellen.

### Angepasste Events

Benutzerdefinierte Ereignisse werden protokolliert, wenn `actionType` auf `logEvent` eingestellt ist. Der Braze Custom Tag Provider in unserem Beispiel erwartet, dass der Name des angepassten Events mit `eventName` festgelegt wird.

Um zu beginnen, erstellen Sie einen Trigger, der nach dem "event name" namens `played song` sucht.

![Ein angepasster Trigger im Google Tag Manager, der für einige Events ausgelöst wird, wenn der "event name" "played song" lautet.]({% image_buster /assets/img/android_google_tag_manager/gtm_android_trigger.png %})

Als Nächstes erstellen Sie ein neues Tag ("Funktionsaufruf") und geben den Klassenpfad Ihres [Custom Tag Provider](#adding-ios-google-tag-provider) ein, der später in diesem Artikel beschrieben wird. 

Dieses Tag wird ausgelöst, wenn Sie das soeben erstellte Event `played song` protokollieren. 

In den benutzerdefinierten Parametern (Schlüssel-Wert-Paare) unseres Beispiel-Tags haben wir `eventName` auf `played song` gesetzt. Das ist der Name des angepassten Events, der in Braze protokolliert wird.

{% alert important %}
Wenn Sie ein angepasstes Event senden, setzen Sie `actionType` auf `logEvent` und legen einen Wert für `eventName` fest, wie im folgenden Beispiel gezeigt. 

Der angepasste Tag-Anbieter in unserem Beispiel verwendet diese Schlüssel, um zu bestimmen, welche Aktion er durchführen und welchen Event-Namen er an Braze senden soll, wenn er Daten vom Google Tag Manager erhält.
{% endalert %}

![Ein Tag in Google Tag Manager mit Klassenpfad und Schlüssel-Wert-Paar-Feldern. Dieses Tag ist so eingestellt, dass es mit dem zuvor erstellten Trigger "played song" ausgelöst wird.]({% image_buster /assets/img/android_google_tag_manager/gtm_android_function_call_tag.png %})

Sie können dem Tag auch zusätzliche Schlüssel-Wert-Paar-Argumente hinzufügen, die als Eigenschaften des angepassten Events an Braze gesendet werden. `eventName` und `actionType` werden für angepasste Event-Eigenschaften nicht ignoriert. Im folgenden Beispiel-Tag übergeben wir `genre`, das über eine Tag-Variable im Google Tag Manager definiert wurde und aus dem angepassten Event stammt, das wir in unserer App protokolliert haben.

Die Event-Eigenschaft `genre` wird als Variable "Firebase - Event Parameter" an Google Tag Manager gesendet, da Google Tag Manager für iOS Firebase als Datenebene verwendet.

![Eine Variable im Google Tag Manager, bei der "genre" als Event-Parameter für das Tag "Braze - Played Song Event" hinzugefügt wird.]({% image_buster /assets/img/android_google_tag_manager/gtm_android_eventname_variable.png %})

Wenn ein Benutzer einen Song in unserer App abspielt, protokollieren wir ein Ereignis über Firebase und den Google Tag Manager unter Verwendung des Firebase-Analytics-Ereignisnamens, der mit dem Auslösernamen unseres Tags übereinstimmt: `played song`:

{% tabs %}
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
{% tab OBJECTIVE-C %}

```obj-c
NSDictionary *parameters = @{@"customAttributeKey" : @"favorite song",
                             @"customAttributeValue" : @"Private Eyes"};
[FIRAnalytics logEventWithName:@"customAttribute" parameters:parameters];
```

{% endtab %}
{% endtabs %}

### Aufruf von changeUser

Anrufe an `changeUser()` erfolgen über ein `actionType`, das auf `changeUser` eingestellt ist. Der Braze Custom Tag Provider erwartet, dass die Braze-Benutzer-ID über das Schlüssel-Wert-Paar `externalUserId` in Ihrem Tag festgelegt wird:

{% tabs %}
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

Achten Sie darauf, den "Klassenpfad" der Datei zu notieren. Diesen geben Sie ein, wenn Sie ein Tag in der [Google Tag Manager-Konsole](https://tagmanager.google.com/) einrichten.

Dieses Beispiel zeigt eine von vielen Möglichkeiten, wie Sie Ihren benutzerdefinierten Tag-Provider strukturieren können. Dabei bestimmen wir anhand des vom GTM-Tag gesendeten Schlüssel-Wert-Paares `actionType`, welche Methode des Braze SDK aufgerufen werden soll.

Die `actionType`, die wir in unserem Beispiel unterstützt haben, sind `logEvent`, `customAttribute` und `changeUser`, aber Sie können ändern, wie Ihr Tag Provider die Daten von Google Tag Manager verarbeitet.

Fügen Sie den folgenden Code in Ihre Datei `BrazeGTMTagManager.h` ein:

{% tabs %}
{% tab OBJECTIVE-C %}

```obj-c
@import Firebase;
@import GoogleTagManager;

@interface BrazeGTMTagManager : NSObject <TAGCustomFunction>

@end
```

{% endtab %}
{% endtabs %}

Und fügen Sie den folgenden Code in Ihre `BrazeGTMTagManager.m` Datei ein:

{% tabs %}
{% tab OBJECTIVE-C %}

```obj-c
#import <Foundation/Foundation.h>
#import "BrazeGTMTagManager.h"
#import "Appboy-iOS-SDK/AppboyKit.h"

static NSString *const ActionTypeKey = @"actionType";

// Custom Events
static NSString *const LogEventActionType = @"logEvent";
static NSString *const LogEventEventName = @"eventName";

// Custom Attributes
static NSString *const CustomAttributeActionType = @"customAttribute";
static NSString *const CustomAttributeKey = @"customAttributeKey";
static NSString *const CustomAttributeValueKey = @"customAttributeValue";

// Change User
static NSString *const ChangeUserActionType = @"changeUser";
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
  
  if ([actionType isEqualToString:LogEventActionType]) {
    [self logEvent:mutableParameters];
  } else if ([actionType isEqualToString:CustomAttributeActionType]) {
    [self logCustomAttribute:mutableParameters];
  } else if ([actionType isEqualToString:ChangeUserActionType]) {
    [self changeUser:mutableParameters];
  } else {
    NSLog(@"Invalid action type. Doing nothing.");
  }
  return nil;
}

- (void)logEvent:(NSMutableDictionary *)parameters {
  NSString *eventName = parameters[LogEventEventName];
  [parameters removeObjectForKey:LogEventEventName];
  [[Appboy sharedInstance] logCustomEvent:eventName withProperties:parameters];
}

- (void)logCustomAttribute:(NSMutableDictionary *)parameters {
  NSString *customAttributeKey = parameters[CustomAttributeKey];
  id customAttributeValue = parameters[CustomAttributeValueKey];
  
  if ([customAttributeValue isKindOfClass:[NSString class]]) {
    [[Appboy sharedInstance].user setCustomAttributeWithKey:customAttributeKey
                                             andStringValue:customAttributeValue];
  } else if ([customAttributeValue isKindOfClass:[NSDate class]]) {
    [[Appboy sharedInstance].user setCustomAttributeWithKey:customAttributeKey
                                               andDateValue:customAttributeValue];
  } else if ([customAttributeValue isKindOfClass:[NSNumber class]]) {
    if (strcmp([customAttributeValue objCType], [@(YES) objCType]) == 0) {
      [[Appboy sharedInstance].user setCustomAttributeWithKey:customAttributeKey
                                                 andBOOLValue:[(NSNumber *)customAttributeValue boolValue]];
    } else if (strcmp([customAttributeValue objCType], @encode(short)) == 0 ||
               strcmp([customAttributeValue objCType], @encode(int)) == 0 ||
               strcmp([customAttributeValue objCType], @encode(long)) == 0) {
      [[Appboy sharedInstance].user setCustomAttributeWithKey:customAttributeKey
                                              andIntegerValue:[(NSNumber *)customAttributeValue integerValue]];
    } else if (strcmp([customAttributeValue objCType], @encode(float)) == 0 ||
               strcmp([customAttributeValue objCType], @encode(double)) == 0) {
      [[Appboy sharedInstance].user setCustomAttributeWithKey:customAttributeKey
                                               andDoubleValue:[(NSNumber *)customAttributeValue doubleValue]];
    } else {
      NSLog(@"Could not map NSNumber value to Appboy custom attribute:%@", customAttributeValue);
    }
  } else if ([customAttributeValue isKindOfClass:[NSArray class]]) {
    [[Appboy sharedInstance].user setCustomAttributeArrayWithKey:customAttributeKey
                                                           array:customAttributeValue];
  }
}

- (void)changeUser:(NSMutableDictionary *)parameters {
  NSString *userId = parameters[ChangeUserExternalUserId];
  [[Appboy sharedInstance] changeUser:userId];
}

@end
```

{% endtab %}
{% endtabs %}

