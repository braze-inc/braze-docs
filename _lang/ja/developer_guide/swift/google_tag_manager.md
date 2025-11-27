{% multi_lang_include developer_guide/prerequisites/swift.md %}

## SwiftでGoogleタグマネージャーを使う

次の例では、ある音楽ストリーミングアプリが、ユーザーが曲を聴くときにさまざまなイベントを記録したいとする。iOS用のGoogle Tagマネージャーを使えば、Brazeのどのサードパーティーベンダーがこのイベントを受け取るかをコントロールし、Braze専用のタグを作成することができる。

### ステップ 1: カスタムイベントのトリガーを作成する

カスタムイベントは、`logEvent` に設定した `actionType` によってログに記録されます。この例では、Brazeカスタムタグプロバイダーは、`eventName` を使用してカスタムイベント名が設定されることを期待している。

まず、`played song` に等しい`eventName` を探すトリガーを作成する。

![「eventName」が「played song」である場合に一部のイベントに対してトリガーするように設定された Google Tag Manager のカスタムトリガー。]({% image_buster /assets/img/android_google_tag_manager/gtm_android_trigger.png %})

次に、新しいタグ（「ファンクション・コール」とも呼ばれる）を作成し、この記事の後半で説明する[カスタム・タグ・プロバイダーの](#adding-ios-google-tag-provider)クラス・パスを入力する。このタグは、`played song` イベントを記録したときにトリガーされる。`eventName` が`played song` に設定されているため、Brazeに記録されるカスタムイベント名として使用される。

{% alert important %}
カスタムイベントを送信するときは、`actionType` を`logEvent` に設定し、`eventName` に値を設定して、Brazeが正しいイベント名とアクションを受信するようにする。
{% endalert %}

![classpath フィールドと、キーと値のペアフィールドを含む Google Tag Manager のタグ。このタグは、以前に作成された「再生された曲」トリガーでトリガーされるように設定されています。]({% image_buster /assets/img/android_google_tag_manager/gtm_android_function_call_tag.png %})

また、追加のキーと値のペア引数をタグに含めることもできます。この引数は、カスタムイベントプロパティとして Braze に送信されます。`eventName` および `actionType` は、カスタムイベントプロパティで無視されません。以下のタグの例では、`genre` を渡す。 は、Googleタグマネージャーでタグ変数を使用して定義され、アプリに記録されたカスタムイベントから取得される。

`genre` イベントプロパティが、「Firebase - Event Parameter」変数として Google Tag Manager に送信されます。Google Tag Manager for iOS では、Firebase がデータレイヤーとして使用されるためです。

![Google Tag Managerの変数で、「Braze - Played Song Event」タグのイベントパラメータとして「genre」が追加されます。]({% image_buster /assets/img/android_google_tag_manager/gtm_android_eventname_variable.png %})

ユーザーがアプリで曲を再生したら、タグのトリガー名と一致するFirebaseアナリティクスのイベント名を使用して、FirebaseとGoogleタグマネージャーを介してイベントをログに記録する`played song` ：

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

### ステップ 2: カスタム属性を記録する

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

### ステップ 3: 電話

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

### ステップ 4: カスタムタグプロバイダーを追加する {#adding-ios-google-tag-provider}

タグとトリガーが設定されたら、iOS アプリに Google Tag Manager を実装する必要もあります。これについては、Google の[ドキュメント](https://developers.google.com/tag-manager/ios/v5/)に記載されています。

アプリにGoogle Tag Managerをインストールしたら、Google Tag Manager内で設定したタグに基づいてBraze SDKメソッドを呼び出すカスタムタグプロバイダを追加する。

[Google Tag Manager](https://tagmanager.google.com/)コンソールでタグを設定するときに入力するのは、ファイルに"Class Path"を必ず書き留めておいてください。

この例では、カスタムタグ・プロバイダーを構成するさまざまな方法のひとつを紹介している。具体的には、GTMタグから送信された`actionType` キーと値のペアに基づいて、どのBraze SDKメソッドを呼び出すかを決定する方法を示す。この例では、AppDelegate で変数として Braze インスタンスを割り当てていると仮定しています。

この例でサポートされている`actionType` は、`logEvent` 、`customAttribute` 、`changeUser` であるが、タグプロバイダーがGoogleタグマネージャーからのデータをどのように扱うかを変更した方がよいかもしれない。
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
