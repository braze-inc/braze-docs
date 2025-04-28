---
nav_title: Google Tag Manager
article_title: Google Tag Manager for iOS
platform: Swift
page_order: 3
description: "この記事では、Swift SDK 用の Google Tag Manager の初期化、設定、および実装の方法について説明します。"

---

# Google Tag Manager

> Braze Swift SDK は、Google Tag Manager 内で設定されたタグによって初期化および制御できます。

この実装の前提条件として、Swift SDK の統合が完了している必要があります。

## Google Tag Manager の設定 {#configuring-ios-google-tag-manager}

この例は、ユーザーが曲を聴いている間に別のイベントをロギングする必要がある音楽ストリーミングアプリを想定しています。Google Tag Manager for iOS を使用して、どのサードパーティベンダーがこのイベントを受信し、Braze 固有のタグを作成するのかを制御できます。

### カスタムイベント

カスタムイベントは、`logEvent` に設定した `actionType` によってログに記録されます。この例の Braze カスタムタグプロバイダーは、`eventName` を使用してカスタムイベント名を設定することを想定しています。

最初に、`played song` である `eventName` を検索するトリガーを作成します。

![「eventName」が「played song」である場合に一部のイベントに対してトリガーするよう設定された Google Tag Manager のカスタムトリガー。]({% image_buster /assets/img/android_google_tag_manager/gtm_android_trigger.png %})

次に、新しいタグ (「Function Call」) を作成し、この記事で後述する[カスタムタグプロバイダー](#adding-ios-google-tag-provider)のクラスパスを入力します。 

このタグは、先ほど作成した `played song` イベントをロギングするとトリガーされます。 

サンプルタグのカスタムパラメーター (キーと値のペア) では、`eventName` を `played song` に設定しました。これが、Braze にロギングされるカスタムイベント名になります。

{% alert important %}
カスタムイベントの送信時に、`actionType` を `logEvent` に設定し、`eventName` の値を次の例のように設定します。
<br><br>
この例のカスタムタグプロバイダーは、これらのキーを使用して、Google Tag Manager からのデータ受信時に実行するアクションと Braze に送信するイベント名を決定します。
{% endalert %}

![classpath フィールドと、キーと値のペアフィールドを含む Google Tag Manager のタグ。このタグは、以前に作成された「再生された曲」トリガーでトリガーされるように設定されています。]({% image_buster /assets/img/android_google_tag_manager/gtm_android_function_call_tag.png %})

また、追加のキーと値のペア引数をタグに含めることもできます。この引数は、カスタムイベントプロパティとして Braze に送信されます。`eventName` および `actionType` は、カスタムイベントプロパティで無視されません。次のサンプルタグでは、`genre` を渡します。これは、Google Tag Manager でタグ変数を使用して定義されており、アプリでロギングしたカスタムイベントから取得されます。

`genre` イベントプロパティが、「Firebase - Event Parameter」変数として Google Tag Manager に送信されます。Google Tag Manager for iOS では、Firebase がデータレイヤーとして使用されるためです。

![Google Tag Manager の変数で、「Braze - Played Song Event」タグのイベントパラメータとして「genre」が追加されます。]({% image_buster /assets/img/android_google_tag_manager/gtm_android_eventname_variable.png %})

最後に、ユーザーがアプリで曲を再生すると、タグのトリガー名 `played song` と一致する Firebase 分析イベント名を使用し、Firebase と Google Tag Manager を介してイベントがロギングされます。

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

### カスタム属性のロギング

カスタム属性は、`customAttribute` に設定された `actionType` を介して設定されます。Braze カスタムタグプロバイダーは、カスタム属性のキーと値が `customAttributeKey` および `customAttributeValue` を介して設定されることを想定しています。

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

### changeUser の呼び出し

`changeUser()` の呼び出しは、`changeUser` に設定された `actionType` を介して行われます。Braze カスタムタグプロバイダーは、Braze ユーザー ID がタグ内のキーと値のペア `externalUserId` を介して設定されることを想定しています。

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

## Braze SDK カスタムタグプロバイダー {#adding-ios-google-tag-provider}

タグとトリガーが設定されたら、iOS アプリに Google Tag Manager を実装する必要もあります。これについては、Google の[ドキュメント](https://developers.google.com/tag-manager/ios/v5/)に記載されています。

Google Tag Manager がアプリにインストールされたら、カスタムタグプロバイダーを追加し、Google Tag Manager 内で設定したタグに基づいて Braze SDK メソッドを呼び出します。 

[Google Tag Manager](https://tagmanager.google.com/)コンソールでタグを設定するときに入力するのは、ファイルに"Class Path"を必ず書き留めておいてください。

この例は、カスタムタグプロバイダーを構築する多くの方法の1つを示しています。ここでは、Google Tag Manager から送信されたキーと値のペア `actionType` に基づいて、呼び出す Braze SDK メソッドを決定します。この例では、AppDelegate で変数として Braze インスタンスを割り当てていると仮定しています。

この例でサポートされている `actionType` は `logEvent`、`customAttribute`、`changeUser` ですが、タグプロバイダーによる Google Tag Manager からのデータの処理方法を変更することもできます。
{% tabs %}
{% tab SWIFT %}

以下のコードを `BrazeGTMTagManager.swift` ファイルに追加します。
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
以下のコードを `BrazeGTMTagManager.h` ファイルに追加します。

```obj-c
@import Firebase;
@import GoogleTagManager;

@interface BrazeGTMTagManager : NSObject <TAGCustomFunction>

@end
```

以下のコードを `BrazeGTMTagManager.m` ファイルに追加します。

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

