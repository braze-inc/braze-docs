{% multi_lang_include developer_guide/prerequisites/swift.md %}

## 遅延初期化の使用

Braze Swift SDK は非同期に初期化できますが、プッシュ通知の処理は保持されます。これは、サーバーから構成データを取得したり、ユーザーの同意を待ったりするなど、SDK を初期化する前に他のサービスを設定する必要がある場合に役立ちます。

### 考慮事項

`Braze.prepareForDelayedInitialization(pushAutomation:)` を使用すると、SDK が自動的にプッシュ通知自動化機能を使用するように設定されます。プッシュ通知を処理するシステムデリゲートメソッドは、Brazeから発信されたプッシュ通知に対しては呼び出されない。

SDK は、SDK が初期化された**後**にのみ、Braze プッシュ通知とその結果のアクションを処理します。例えば、ユーザーがディープリンクを開くプッシュ通知をタップした場合、ディープリンクは `Braze` インスタンスが初期化された後にのみ開きます。

Braze プッシュ通知で追加の処理を実行する必要がある場合は、[[プッシュ通知更新を購読する]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#subscribing-to-push-notifications-updates)] を参照してください。以前にキューに登録されたプッシュ通知の更新を受信するには、SDK を初期化した後、サブスクリプションハンドラを直接実装する必要があることに留意してください。

### ステップ1:SDKの準備

デフォルトでは、アプリが終了状態にあるときにエンドユーザーがプッシュ通知を開いた場合、SDK が初期化されるまでプッシュ通知を処理できません。

[Braze Swift SDK バージョン 10.1.0](https://github.com/braze-inc/braze-swift-sdk/releases/tag/10.1.0) 以降では、静的ヘルパーメソッド [Braze.prepareForDelayedInitialization(pushAutomation:)](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/preparefordelayedinitialization(pushautomation:)) を使用してこれを処理できます。このメソッドは、プッシュオートメーションシステムを設定することで、遅延初期化用に SDK を準備します。

SDKが初期化される前に、Brazeから発信されるすべてのプッシュ通知がキャプチャされ、キューに入れられる。SDK が初期化されると、それらのプッシュ通知は SDK によって処理されます。このメソッドは、アプリケーションのライフサイクルのできるだけ早い段階で、`AppDelegate` の `application(_:didFinishLaunchingWithOptions:)` メソッド内またはその前に呼び出す必要があります。

{% alert note %}
Swift SDK は Braze 以外のプッシュ通知をキャプチャしません。そのような通知は引き続きシステムデリゲートメソッドによって処理されます。
{% endalert %}

{% tabs %}
{% tab Swift %}
{% subtabs local %}
{% subtab UIKit %}
```swift
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
  // Prepare the SDK for delayed initialization
  Braze.prepareForDelayedInitialization()

  // ... Additional non-Braze setup code

  return true
}
```
{% endsubtab %}

{% subtab SwiftUI %}
SwiftUI アプリケーションは`prepareForDelayedInitialization()` メソッドを呼び出すために[@UIApplicationDelegateAdaptor](https://developer.apple.com/documentation/swiftui/uiapplicationdelegateadaptor)プロパティラッパーを実装する必要がある。

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
{% endsubtab %}
{% endsubtabs %}
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
[Braze.prepareForDelayedInitialization(pushAutomation:)](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/preparefordelayedinitialization(pushautomation:)) は、プッシュ通知のオートメーション設定を表すオプションの `pushAutomation` パラメータを取ります。[Braze.Configuration.Push.Automation](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/push-swift.class/automation-swift.class) が `nil` の場合、起動時に承認を要求することを除き、すべてのオートメーション機能が有効になります。
{% endalert %}

### ステップ2:SDK の初期化

遅延初期化用に SDK を準備したら、将来いつでも SDK を非同期的に初期化できます。次に、SDK は Braze から発信されキューに入れられたすべてのプッシュ通知イベントを処理します。

Braze SDK を初期化するには、[標準の Swift SDK 初期化プロセス]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/sdk_integration/#step-2-update-your-app-delegate)に従います。

## Google タグマネージャの使用

Braze Swift SDK は、Google Tag Manager 内で設定されたタグによって初期化および制御できます。

次の例では、音楽ストリーミングアプリは、ユーザーが曲を聴くときに異なるイベントを記録することを求めています。Google Tag Manager for iOS を使用すると、Braze のサードパーティベンダーのどのベンダーがこのイベントを受信し、Braze に固有のタグを作成するかを制御できます。

### ステップ1:カスタムイベントのトリガーを作成する

カスタムイベントは、`logEvent` に設定した `actionType` によってログに記録されます。この例では、Braze カスタムタグプロバイダは、`eventName` を使用してカスタムイベント名を設定することを期待しています。

まず、`played song` に等しい`eventName` を探すトリガを作成します。

![「eventName」が「played song」である場合に一部のイベントに対してトリガーするよう設定された Google Tag Manager のカスタムトリガー。]({% image_buster /assets/img/android_google_tag_manager/gtm_android_trigger.png %})

次に、新しいタグ("Function Call"とも呼ばれます)を作成し、この記事で後述する[カスタムタグプロバイダー](#adding-ios-google-tag-provider)のクラスパスを入力します。このタグは、`played song` イベントをログに記録するとトリガーされます。`eventName` は`played song` に設定されているため、Braze に記録されるカスタムイベント名として使用されます。

{% alert important %}
カスタムイベントを送信する場合、`actionType` を`logEvent` に設定し、`eventName` の値を設定すると、Braze は正しいイベント名とアクションを受け取ります。
{% endalert %}

![classpath フィールドと、キーと値のペアフィールドを含む Google Tag Manager のタグ。このタグは、以前に作成された「再生された曲」トリガーでトリガーされるように設定されています。]({% image_buster /assets/img/android_google_tag_manager/gtm_android_function_call_tag.png %})

また、追加のキーと値のペア引数をタグに含めることもできます。この引数は、カスタムイベントプロパティとして Braze に送信されます。`eventName` および `actionType` は、カスタムイベントプロパティで無視されません。次の例のタグでは、`genre` を渡します。これは、Google タグマネージャでタグ変数を使用して定義され、アプリに記録されたカスタムイベントから取得されます。

`genre` イベントプロパティが、「Firebase - Event Parameter」変数として Google Tag Manager に送信されます。Google Tag Manager for iOS では、Firebase がデータレイヤーとして使用されるためです。

![Google Tag Manager の変数で、「Braze - Played Song Event」タグのイベントパラメータとして「genre」が追加されます。]({% image_buster /assets/img/android_google_tag_manager/gtm_android_eventname_variable.png %})

ユーザがアプリで曲を再生すると、Firebase とGoogle Tag Manager を介して、タグのトリガ名`played song` に一致するFirebase 分析イベント名を使用してイベントをログに記録します。

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

### ステップ2:カスタム属性のログ

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

### ステップ 3:コール `changeUser()`

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

### ステップ 4:カスタムタグプロバイダの追加 {#adding-ios-google-tag-provider}

タグとトリガーが設定されたら、iOS アプリに Google Tag Manager を実装する必要もあります。これについては、Google の[ドキュメント](https://developers.google.com/tag-manager/ios/v5/)に記載されています。

Googleタグマネージャがアプリにインストールされたら、カスタムタグプロバイダを追加して、Googleタグマネージャで設定したタグに基づいてBraze SDK メソッドを呼び出します。

[Google Tag Manager](https://tagmanager.google.com/)コンソールでタグを設定するときに入力するのは、ファイルに"Class Path"を必ず書き留めておいてください。

この例では、カスタムタグプロバイダを構築するさまざまな方法の1 つを強調表示します。具体的には、GTM タグから送信された`actionType` キーと値のペアに基づいて、どのBraze SDK メソッドを呼び出すかを決定する方法を示します。この例では、AppDelegate で変数として Braze インスタンスを割り当てていると仮定しています。

この例でサポートされている`actionType` は、`logEvent`、`customAttribute`、および`changeUser` ですが、タグプロバイダーによるGoogle タグマネージャからのデータの処理方法を変更することをお勧めします。
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
