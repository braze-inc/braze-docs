---
nav_title: SDK統合ガイド（オプション）
article_title: iOS 用 Braze SDK の統合ガイド (オプション)
alias: "/ios_sdk/"
description: "この iOS 統合ガイドでは、最初に iOS SDK とそのコアコンポーネントをアプリケーションに統合するときに、セットアップのベストプラクティスについて段階的に説明します。このガイドは、BrazeManager.swift ヘルパーファイルの作成に役立ちます。"
page_order: 10
platform: iOS

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Braze iOS SDK 統合ガイド

> このオプションの iOS 統合ガイドでは、最初に iOS SDK とそのコアコンポーネントをアプリケーションに統合するときに、セットアップのベストプラクティスについて段階的に説明します。このガイドは、`BrazeManager.swift` ヘルパーファイルを作成する際に役立ちます。このヘルパーファイルは、Braze iOS SDK への依存関係をプロダクションコードの残りの部分から切り離し、アプリケーション全体で 1 つの `import AppboyUI` を生成します。このアプローチでは、過剰な SDK インポートから発生する問題が制限されるため、コードの追跡、デバッグ、および変更が容易になります。 

{% alert important %}
このガイドでは、すでに [SDK]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/overview/) を Xcode プロジェクトに追加していることを前提としています。
{% endalert %}

## 統合の概要

以下の手順は、プロダクション・コードが呼び出す `BrazeManager` ヘルパー・ファイルの作成に役立ちます。このヘルパーファイルは、リストされている以下の統合トピックのさまざまな拡張機能を追加することで、Braze 関連のすべての依存関係を処理します。各トピックには、Swift と Objective-C の両方の水平タブステップとコードスニペットが含まれます。アプリケーションでこれらのチャネルを使用する予定がない場合、統合にはコンテンツカードとアプリ内メッセージのステップは必要ありません。

- [BrazeManager.swift の作成](#create-brazemanagerswift)
- [SDK の初期化](#initialize-the-sdk)
- [プッシュ通知](#push-notifications)
- [ユーザー変数とメソッドへのアクセス](#access-user-variables-and-methods)
- [ログ分析](#log-analytics)
- [アプリ内メッセージ (オプション)](#in-app-messages)
- [コンテンツカード (オプション)](#content-cards)
- [次のステップ](#next-steps)

### BrazeManager.swift の作成

{% tabs local %}
{% tab Create BrazeManager swift %}

##### BrazeManager.swift の作成
`BrazeManager.swift` ファイルを作成するには、_BrazeManager_ という名前の新しい Swift ファイルを作成し、目的の場所のプロジェクトに追加します。次に、`import Foundation` を SPM の `import AppboyUI` に置き換えてから (CocoaPods の場合は `import Appboy_iOS_SDK`)、`BrazeManager` クラスを作成します。これは、すべての Braze 関連のメソッドと変数をホストするために使用されます。`Appboy_iOS_SDK`

{% alert note %}
- `BrazeManager` は `NSObject` クラスであり、構造体ではないため、`ABKInAppMessageUIDelegate` などの ABK デリゲートに準拠できます。
- `BrazeManager` は、このクラスのインスタンスが1 つだけ使用されるように設計されたシングルトンクラスです。これは、オブジェクトへの統合されたアクセスポイントを提供するために行われます。
{% endalert %} 

1. `BrazeManager`クラスを初期化する _shared_ という名前の静的変数を追加します。これは、一度だけ遅延開始されることが保証されています。
2. 次に、_apiKey_ という名前のプライベート定数変数を追加し、Braze ダッシュボードのワークスペースから API キー値として設定します。
3. _appboyOptions_ という名前のプライベート計算変数を追加します。これにより SDK の構成値が格納されます。今のところ空です。

{% subtabs global %}
{% subtab Swift %}

```swift
class BrazeManager: NSObject {
  // 1
  static let shared = BrazeManager()
  
  // 2
  private let apikey = "YOUR-API-KEY"
  
  // 3
  private var appboyOptions: [String:Any] {
    return [:]
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
@implementation BrazeManager
 
// 1
+ (instancetype)shared {
    static BrazeManager *shared = nil;
    static dispatch_once_t onceToken;
    dispatch_once(&onceToken, ^{
        shared = [[BrazeManager alloc] init];
        // Do any other initialisation stuff here
    });
    return shared;
}
 
// 2
- (NSString *)apiKey {
  return @"YOUR-API-KEY";
}
 
// 3
- (NSDictionary *)appboyOptions {
  return [NSDictionary dictionary];
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### SDK の初期化

{% tabs local %}
{% tab Step 1: Initialize SDK from BrazeManager swift %}

##### BrazeManager.swift から SDK を初期化する
次に、SDK を初期化する必要があります。このガイドでは、すでに [SDK]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/overview/) を Xcode プロジェクトに追加していることを前提としています。また、[ワークスペース SDK エンドポイント]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/completing_integration/#step-2-specify-your-data-cluster) および [`LogLevel`]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/other_sdk_customizations/#braze-log-level) を `Info.plist` ファイルまたは `appboyOptions` に設定する必要があります。

`didFinishLaunchingWithOptions` メソッドを `AppDelegate.swift` ファイルから `BrazeManager.swift` ファイルに戻りタイプなしで追加します。`BrazeManager.swift` ファイルに同様のメソッドを作成すると、`import AppboyUI` ステートメントは `AppDelegate.swift` ファイルにはありません。 

次に、新しく宣言した `apiKey` および `appboyOptions` 変数を使用して SDK を初期化します。

{% alert important %}
初期化はメインスレッドで行う必要があります。
{% endalert %}

{% subtabs global %}
{% subtab Swift %}
```swift
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) {
  Appboy.start(withApiKey: apikey, in: application, withLaunchOptions: launchOptions, withAppboyOptions: appboyOptions)
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  [Appboy startWithApiKey:[self apiKey] inApplication:application withLaunchOptions:launchOptions withAppboyOptions:[self appboyOptions]];
}
```
{% endsubtab %}
{% endsubtabs %}

{% endtab %}
{% tab Step 2: Handle Appboy Initialization %}

##### AppDelegate.swift での Appboy の初期化処理
次に、`AppDelegate.swift` ファイルに戻り、AppDelegate の `didFinishLaunchingWithOptions` メソッドに以下のコードスニペットを追加して、`BrazeManager.swift` ヘルパーファイルから Appboy の初期化を処理します。`AppDelegate.swift` に `import AppboyUI` ステートメントを追加する必要はありません。

{% subtabs global %}
{% subtab Swift %}

```swift
func application(
  _ application: UIApplication, 
  didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
) -> Bool {
  // Override point for customization after application launch

  BrazeManager.shared.application(application, didFinishLaunchingWithOptions: launchOptions)

  return true
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  // Override point for customization after application launch
 
  [[BrazeManager shared] application:application didFinishLaunchingWithOptions:launchOptions];
   
  return YES;
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

{% alert checkpoint %}
コードのコンパイルとアプリケーションの実行に進みます。<br><br>この時点で、SDK が稼働している必要があります。ダッシュボードで、セッションがログに記録されていることを確認してから、さらに進みます。
{% endalert %}

### プッシュ通知

{% tabs local %}
{% tab Step 1: Add Push Certificate %}

##### プッシュ証明書の追加

Braze ダッシュボードで既存のワークスペースに移動します。**プッシュ通知設定 ngs** で、プッシュ証明書ファイルを Braze ダッシュボードにアップロードして保存します。 

![]({% image_buster /assets/img/ios_sdk/ios_sdk2.png %}){: style="max-width:60%;"}

{% endtab %}
{% tab Step 2: Register for Notifications %}

{% alert important %}
この手順の最後にある専用チェックポイントをお見逃しなく！
{% endalert %}

##### プッシュ通知の登録

次に、プッシュ通知を登録します。このガイドでは、Apple 開発者ポータルおよび Xcode プロジェクトで[プッシュ認証情報を正しく設定]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/integration/)していることを前提としています。 

プッシュ通知を登録するコードは、`BrazeManager.swift` ファイルの `didFinishLaunching...` メソッドに追加されます。初期化コードは最終的に次のようになります。

1. ユーザと対話する権限を要求するためのコンテンツを設定します。これらのオプションは例としてリストされています。
2. ユーザにプッシュ通知を送信する権限を要求します。プッシュ通知を許可または拒否するユーザの応答は、`granted` 変数で追跡されます。
3. ユーザが通知プロンプトを操作した後、プッシュ承認の結果を Braze に転送します。
4. APN で登録プロセスを開始します。これはメインスレッドで行う必要があります。登録が成功すると、アプリは `AppDelegate` オブジェクトの `didRegisterForRemoteNotificationsWithDeviceToken` メソッドを呼び出します。 

{% subtabs global %}
{% subtab Swift %}
```swift
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions:[UIApplication.LaunchOptionsKey:Any]?) {
  Appboy.start(withAPIKey: apikey, in: application, withLaunchOptions: launchOptions, withAppboyOptions: appboyOptions)
  // 1 
  let options: UNAuthorizationOptions = [.alert, .sound, .badge]
  // 2 
  UNUserNotificationCenter.current().requestAuthorization(option: options) { (granted, error) in
  // 3 
    Appboy.sharedInstance()?.pushAuthorization(fromUserNotificationCenter: granted)
  }
  
  // 4 
  UIApplications.shared.registerForRemoteNotificiations()
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  [Appboy startWithApiKey:[self apiKey] inApplication:application withLaunchOptions:launchOptions withAppboyOptions:[self appboyOptions]];
   
  // 1
  UNAuthorizationOptions options = (UNAuthorizationOptionSound | UNAuthorizationOptionAlert | UNAuthorizationOptionBadge);
   
  // 2
  [[UNUserNotificationCenter currentNotificationCenter] requestAuthorizationWithOptions:options completionHandler:^(BOOL granted, NSError * _Nullable error) {
  // 3
    [[Appboy sharedInstance] pushAuthorizationFromUserNotificationCenter:granted];
  }];
 
  // 4
  [[UIApplication sharedApplication] registerForRemoteNotifications];
}
```
{% endsubtab %}
{% endsubtabs %}

{% alert checkpoint %}
コードのコンパイルとアプリケーションの実行に進みます。
- アプリで、プッシュ通知を求めるプロンプトが表示されていることを確認してから、先に進みます。
- プロンプトが表示されない場合は、アプリの削除と再インストールを試して、プッシュ通知のプロンプトが以前に表示されていないことを確認します。

プッシュ通知を求めるプロンプトが表示されていることを確認してから、先に進みます。
{% endalert %}

{% endtab %}
{% tab Step 3: Forward Methods %}

##### プッシュ通知メソッドの転送

次に、システムのプッシュ通知メソッドを `AppDelegate.swift` から `BrazeManager.swift` に転送し、Braze iOS SDK で処理されるようにします。

###### ステップ1:プッシュ通知コードの拡張子を作成する

`BrazeManager.swift` ファイルにプッシュ通知コードの拡張子を作成し、ヘルパーファイルで提供されている目的について、より組織的な方法で読み取るようにします。以下に例を示します。

1. `import AppboyUI` ステートメントを `AppDelegate` に含めないパターンに従って、`BrazeManager.swift` ファイルのプッシュ通知メソッドを処理します。ユーザのデバイストークンは、`didRegisterForRemote...` メソッドから Braze に渡される必要があります。このメソッドは、サイレントプッシュ通知を実装するために必要です。次に、`BrazeManager` クラスの `AppDelegate` から同じメソッドを追加します。
2. 以下の行をメソッド内に追加して、デバイストークンを Braze に登録します。これは、Braze がトークンを現在のデバイスに関連付けるために必要です。 

{% subtabs global %}
{% subtab Swift %}

```swift
// MARK - Push Notifications
extension BrazeManager {
  // 1 
  func application(
    _ application: UIApplication,
    didRegisterForRemoteNotificationsWithDeviceToken deviceToken: Data
  ) {
    // 2 
    Appboy.sharedInstance().?registerDeviceToken(deviceToken)
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
// MARK - Push Notifications
// 1
- (void)application:(UIApplication *)application didRegisterForRemoteNotificationsWithDeviceToken:(NSData *)deviceToken {
  // 2
  [[Appboy sharedInstance] registerDeviceToken:deviceToken];
}
```
{% endsubtab %}
{% endsubtabs %}

###### ステップ2:リモート通知のサポート
**Signing& Capabilities**タブで、**Background Modes**supportを追加し、**Remote notificationsを**選択して、Brazeから発信されるリモートプッシュ通知のサポートを開始する。<br><br>![署名& 機能]({% image_buster /assets/img/ios_sdk/ios_sdk3.png %})

###### ステップ 3:リモート通知処理
Braze SDK は、Braze から発信されるリモートプッシュ通知を処理できます。Braze にリモート通知を転送します。SDK は Braze から発信されたものではないプッシュ通知を自動的に無視します。プッシュ通知拡張子で、`BrazeManager.swift` ファイルに次のメソッドを追加します。

{% subtabs global %}
{% subtab Swift %}
```swift
func application(
  _ application: UIApplication, 
  didReceiveRemoteNotification userInfo: [AnyHashable : Any], 
  fetchCompletionHandler completionHandler: @escaping (UIBackgroundFetchResult) -> Void
) {
  Appboy.sharedInstance()?.register(
    application, 
    didReceiveRemoteNotification: userInfo, 
    fetchCompletionHandler: completionHandler
  )
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)application:(UIApplication *)application didReceiveRemoteNotification:(NSDictionary *)userInfo fetchCompletionHandler:(void (^)(UIBackgroundFetchResult))completionHandler {
  [[Appboy sharedInstance] registerApplication:application didReceiveRemoteNotification:userInfo fetchCompletionHandler:completionHandler];
}
```
{% endsubtab %}
{% endsubtabs %}

###### ステップ 4:通知応答の転送

Braze SDK は、Braze から発信されるプッシュ通知の応答を処理できます。通知の応答を Braze に転送します。SDK は、Braze から発信されていないプッシュ通知からの応答を自動的に無視します。以下のメソッドを `BrazeManager.swift` ファイルに追加します。

{% subtabs global %}
{% subtab Swift %}

```swift
func userNotificationCenter(
  _ center: UNUserNotificationCenter, 
  didReceive response: UNNotificationResponse, 
  withCompletionHandler completionHandler: @escaping () -> Void
) {
  Appboy.sharedInstance()?.userNotificationCenter(
    center, 
    didReceive: response, 
    withCompletionHandler: completionHandler
  )
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)userNotificationCenter:(UNUserNotificationCenter *)center
didReceiveNotificationResponse:(UNNotificationResponse *)response 
         withCompletionHandler:(void (^)(void))completionHandler {
  [[Appboy sharedInstance] userNotificationCenter:center 
                   didReceiveNotificationResponse:response 
                            withCompletionHandler:completionHandler];
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

{% alert checkpoint %}
コードのコンパイルとアプリケーションの実行に進みます。<br><br>Braze ダッシュボードからプッシュ通知を送信してみて、プッシュ通知から分析がログに記録されていることを確認してから、次に進みます。
{% endalert %}

### ユーザー変数とメソッドへのアクセス

{% tabs local %}
{% tab Create User Variables and Methods %}

##### ユーザー変数とメソッドの作成

次に、`ABKUser` の変数とメソッドに簡単にアクセスできるようにします。`BrazeManager.swift` ファイルでユーザコードの拡張子を作成し、ヘルパーファイルで提供されている目的について、以下のように整理された方法で読み込むようにします。

1. `ABKUser` オブジェクトは、iOS アプリケーションの既知または匿名ユーザを表します。計算変数を追加して `ABKUser` を取得します。この変数は、ユーザーに関する変数を取得するために再利用されます。
2. `userId` に簡単にアクセスするには、ユーザー変数をクエリします。他の変数の中で、`ABKUser` オブジェクトは (`firstName`、`lastName`、`phone`、`homeCity` など) の原因となります。
3. 対応する `userId` で `changeUser()` を呼び出してユーザーを設定します。

{% subtabs global %}
{% subtab Swift %}

```swift
// MARK: - User
extension BrazeManager {
  // 1
  var user: ABKUser? {
    return Appboy.sharedInstance()?.user
  }

  // 2 
  var userId: String? {
    return user?.userID
  }

  // 3
  func changeUser(_ userId: String) {
    Appboy.sharedInstance()?.changeUser(userId)
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
// MARK: - User
  // 1
- (ABKUser *)user {
  return [[Appboy sharedInstance] user];
}
   
   // 2 
- (NSString *)userId {
  return [self user].userID;
}
 
  // 3
- (void)changeUser:(NSString *)userId {
  [[Appboy sharedInstance] changeUser:userId];
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

{% alert checkpoint %}
コードのコンパイルとアプリケーションの実行に進みます。<br><br>サインイン/サインアップに成功したユーザーを識別してみてください。何が適切なユーザー識別子であり、何が適切なユーザー識別子でないかをしっかりと理解してください。<br><br>ダッシュボードで、ユーザー識別子がログに記録されていることを確認してから、先に進みます。
{% endalert %} 

### ログ分析

{% tabs local %}
{% tab Step 1: Custom Events %}

##### カスタムイベント記録メソッドの作成

以下の Braze SDK `logCustomEvent` メソッドに基づいて、一致するメソッドを作成します。 

**Braze `logCustomEvent` 参照メソッド**<br>
Braze iOS SDK のメソッドに直接アクセスできるのは `BrazeManager.swift` ファイルだけなので、これは仕様です。したがって、マッチングメソッドを作成することで、結果は同じになり、プロダクションコード内の Braze iOS SDK に直接依存することなく実行されます。

```
open func logCustomEvent(_ eventName: String, withProperties properties: [AnyHashable : Any]?)
```

**マッチングメソッド**<br>
`Appboy` オブジェクトから Braze にカスタムイベントを記録します。`Properties` はオプションのパラメータで、デフォルト値は nil です。カスタムイベントにはプロパティは必要ありませんが、名前を付ける必要があります。 

{% subtabs global %}
{% subtab Swift %}
```swift
func logCustomEvent(_ eventName: String, withProperties properties: [AnyHashable: Any]? = nil) {
  Appboy.sharedInstance()?.logCustomEvent(eventName, withProperties: properties)
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)logCustomEvent:(NSString *)eventName withProperties:(nullable NSDictionary *)properties {
  [[Appboy sharedInstance] logCustomEvent:eventName withProperties:properties];
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Step 2: Custom Attributes %}

##### カスタム属性記録メソッドの作成 

SDK は、カスタム属性として多数のタイプをログに記録できます。設定可能な値タイプごとにヘルパーメソッドを作成する必要はありません。代わりに、適切な値に絞り込むことができる1つのメソッドのみを公開します。

```
- (BOOL)setCustomAttributeWithKey:(NSString *)key andBOOLValue:(BOOL)value; 
- (BOOL)setCustomAttributeWithKey:(NSString *)key andIntegerValue:(NSIntenger)value; 
- (BOOL)setCustomAttributeWithKey:(NSString *)key andDoubleValue:(double)value; 
- (BOOL)setCustomAttributeWithKey:(NSString *)key andStringValue:(NSString *)value; 
- (BOOL)setCustomAttributeWithKey:(NSString *)key andDateValue:(NSDate *)value;
```

カスタム属性は、`ABKUser` オブジェクトからログに記録されます。 

属性に設定可能なすべての使用可能なタイプを包含できる**1つのメソッド**を作成します。分析拡張の `BrazeManager.swift` ファイルにこのメソッドを追加します。これは、有効なカスタム属性タイプをフィルタリングして、一致するタイプに関連付けられたメソッドを呼び出すことによって行うことができます。

- パラメーター　`value` は、`Equatable` プロトコルに準拠する汎用型です。これは明示的に行われます。そのため、タイプが Braze iOS SDK が期待するものでない場合、コンパイル時エラーが発生します。
- パラメータ `key` および `value` はオプションのパラメータで、メソッドで条件付きでアンラップされます。これは、Nil 以外の値が Braze iOS SDK に渡されるようにする1つの方法です。

{% subtabs global %}
{% subtab Swift %}

```swift
func setCustomAttributeWithKey<T: Equatable>(_ key: String?, andValue value: T?) {
  guard let key = key, let value = value else { return }
  switch value.self {
  case let value as Date:
    user?.setCustomAttributeWithKey(key, andDateValue: value)
  case let value as Bool:
    user?.setCustomAttributeWithKey(key, andBOOLValue: value)
  case let value as String:
    user?.setCustomAttributeWithKey(key, andStringValue: value)
  case let value as Double:
    user?.setCustomAttributeWithKey(key, andDoubleValue: value)
  case let value as Int:
    user?.setCustomAttributeWithKey(key, andIntegerValue: value)
  default:
   return
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)setCustomAttributeWith:(NSString *)key andValue:(id)value {
  if ([value isKindOfClass:[NSDate class]]) {
    [[self user] setCustomAttributeWithKey:key andDateValue:value];
  } else if ([value isKindOfClass:[NSString class]]) {
    [[self user] setCustomAttributeWithKey:key andStringValue:value];
  } else if ([value isKindOfClass:[NSNumber class]]) {
    if (strcmp([value objCType], @encode(double)) == 0) {
      [[self user] setCustomAttributeWithKey:key andDoubleValue:[value doubleValue]];
    } else if (strcmp([value objCType], @encode(int)) == 0) {
      [[self user] setCustomAttributeWithKey:key andIntegerValue:[value integerValue]];
    } else if ([value boolValue]) {
      [[self user] setCustomAttributeWithKey:key andBOOLValue:[value boolValue]];
    }
  }
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Step 3: Purchases %}

##### 購入記録メソッドの作成

次に、以下の Braze SDK `logPurchase` メソッドに基づいて、マッチングメソッドを作成します。 

**Braze `logPurchase` 参照メソッド**<br>
Braze iOS SDK のメソッドに直接アクセスできるのは `BrazeManager.swift` ファイルだけなので、これは仕様です。したがって、マッチングメソッドを作成することで、結果は同じになり、プロダクションコード内の Braze iOS SDK に直接依存することなく実行されます。 

```
open func logPurchase(_ productIdentifier: String, inCurrency currency: String, atPrice price: NSDecimalNumber, withoutQuantity quantity: UInt)
```
**マッチングメソッド**<br>
`Appboy` オブジェクトからの購入を Braze に記録します。SDK には、購入を記録するための複数の方法があり、これは 1 つの例にすぎません。このメソッドは、`NSDecimal` および`UInt` オブジェクトの作成も処理します。その部分をどのように処理するかはあなた次第ですが、以下はほんの一例に過ぎません。

{% subtabs global %}
{% subtab Swift %}

```swift
func logPurchase(_ productIdentifier: String, inCurrency currency: String, atPrice price:
String, withQuantity quantity: Int) {

  Appboy.sharedInstance()?.logPurchase(productIdentifier, inCurrency: currency, atPrice: NSDecimalNumber(string: price), withQuantity: UInt(quantity))

}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)logPurchase:(NSString *)productIdentifier inCurrency:(nonnull NSString *)currencyCode atPrice:(nonnull NSDecimalNumber *)price withQuantity:(NSUInteger)quantity {
  [[Appboy sharedInstance] logPurchase:productIdentifier inCurrency:currencyCode atPrice:price withQuantity:quantity];
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

{% alert checkpoint %}
コードのコンパイルとアプリケーションの実行に進みます。<br><br>カスタムイベントを記録してみてください。<br><br>ダッシュボードで、カスタムイベントがログに記録されていることを確認してから先に進みます。
{% endalert %}

### アプリ内メッセージ

{% tabs local %}
{% tab Step 1: Conform to Delegate %}

{% alert important %}
アプリケーションでこのチャネルを使用する予定がない場合、以下のアプリ内メッセージセクションは統合には必要ありません。
{% endalert %}

##### ABKInAppMessageUIDelegate に準拠する

次に、`BrazeManager.swift` ファイルコードを有効にして、`ABKInAppMessageUIDelegate` に準拠し、関連付けられたメソッドを直接処理します。 

デリゲートに準拠するコードは、`BrazeManager.swift` ファイルの `didFinishLaunching...` メソッドに追加されます。初期化コードは最終的に次のようになります。

{% subtabs global %}
{% subtab swift %}
```swift
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) {
  Appboy.start(withApiKey: apiKey, in: application, withLaunchOptions: launchOptions, withAppboyOptions: appboyOptions)

  let options: UNAuthorizationOptions = [.alert, .sound, .badge]
  UNUserNotificationCenter.current().requestAuthorization(options: options) { (granted, error) in
    Appboy.sharedInstance()?.pushAuthorization(fromUserNotificationCenter: granted)
  }
  UIApplication.shared.registerForRemoteNotifications()

  Appboy.sharedInstance()?.inAppMessageController.inAppMessageUIController?.setInAppMessageUIDelegate?(self)
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  [Appboy startWithApiKey:[self apiKey] inApplication:application withLaunchOptions:launchOptions withAppboyOptions:[self appboyOptions]];
   
  UNAuthorizationOptions options = (UNAuthorizationOptionSound | UNAuthorizationOptionAlert | UNAuthorizationOptionBadge);
  [[UNUserNotificationCenter currentNotificationCenter] requestAuthorizationWithOptions:options completionHandler:^(BOOL granted, NSError * _Nullable error) {
    [[Appboy sharedInstance] pushAuthorizationFromUserNotificationCenter:granted];
  }];
  [[UIApplication sharedApplication] registerForRemoteNotifications];
   
  [[Appboy sharedInstance].inAppMessageController.inAppMessageUIController setInAppMessageUIDelegate:self];
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Step 2: Add Delegate Methods %}

##### デリゲートメソッドの追加
次に、`ABKInAppMessageUIDelegate` に準拠する拡張子を作成します。

次のスニペットを分析セクションに追加します。`BrazeManager.swift` オブジェクトがデリゲートとして設定されていることに注意してください。これは、`BrazeManager.swift` ファイルがすべての `ABKInAppMessageUIDelegate` メソッドを処理する場所です。 

{% alert important %}
`ABKInAppMessageUIDelegate` には、必要なメソッドはありませんが、以下は1つの例です。
{% endalert %}

{% subtabs global %}
{% subtab Swift %}
```swift
// MARK: - ABKInAppMessage UI Delegate
extension AppboyManager: ABKInAppMessageUIDelegate{
  func inAppMessageViewControllerWith(_ inAppMessage: ABKInAppMessage) -> ABKInAppMessageViewController {
    switch inAppMessage {
    case is ABKInAppMessageSlideup:
      return ABKInAppMessageSlideupViewController(inAppMessage: inAppMessage)
    case is ABKInAppMessageModal:
      return ABKInAppMessageModalViewController(inAppMessage: inAppMessage)
    case is ABKInAppMessageFull:
      return ABKInAppMessageFullViewController(inAppMessage: inAppMessage)
    case is ABKInAppMessageHTML:
      return ABKInAppMessageHTMLViewController(inAppMessage: inAppMessage)
    default:
      return ABKInAppMessageViewController(inAppMessage: inAppMessage)
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
// MARK: - ABKInAppMessage UI Delegate
- (ABKInAppMessageViewController *)inAppMessageViewControllerWithInAppMessage:(ABKInAppMessage *)inAppMessage {
  if ([inAppMessage isKindOfClass:[ABKInAppMessageSlideup class]]) {
    return [[ABKInAppMessageSlideupViewController alloc] initWithInAppMessage:inAppMessage];
  } else if ([inAppMessage isKindOfClass:[ABKInAppMessageModal class]]) {
    return [[ABKInAppMessageModalViewController alloc] initWithInAppMessage:inAppMessage];
  } else if ([inAppMessage isKindOfClass:[ABKInAppMessageFull class]]) {
    return [[ABKInAppMessageFullViewController alloc] initWithInAppMessage:inAppMessage];
  } else if ([inAppMessage isKindOfClass:[ABKInAppMessageHTML class]]) {
    return [[ABKInAppMessageHTMLViewController alloc] initWithInAppMessage:inAppMessage];
  }
  return nil;
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

{% alert checkpoint %}
コードのコンパイルとアプリケーションの実行に進みます。<br><br>アプリ内メッセージを送信してみてください。<br><br>`BrazeManager.swift` ファイルで、`ABKInAppMessageUIDelegate` メソッドの例のエントリにブレークポイントを設定します。アプリ内メッセージを送信し、ブレークポイントに到達したことを確認してから、さらに進みます。
{% endalert %}

### コンテンツカード

{% tabs local %}
{% tab Create Content Card Variables and Methods %}

{% alert important %}
アプリケーションでこのチャネルを使用する予定がない場合、以下のコンテンツカードセクションは統合には必要ありません。
{% endalert %}

##### コンテンツカードの変数とメソッドの作成

不要な `import AppboyUI` ステートメントを必要とせずに、コンテンツカードビューコントローラを表示するようにプロダクションコードを有効にします。 

`BrazeManager.swift` ファイルにコンテンツカードコードの拡張子を作成します。ヘルパーファイルで提供されている目的について、以下のように整理された方法で読み込むようにします。

1. `ABKContentCardsTableViewController` を表示します。オプションの `navigationController` は、ビューコントローラーを表示またはプッシュするために必要な唯一のパラメーターです。
2. `ABKContentCardsTableViewController` オブジェクトを初期化し、オプションでタイトルを変更します。初期化されたビューコントローラーをナビゲーションスタックに追加する必要もあります。

{% subtabs global %}
{% subtab Swift %}
```swift
// MARK: - Content Cards
extension BrazeManager {

  // 1 
  func displayContentCards(navigationController: UINavigationController?) {
      
    // 2 
    let contentCardsVc = ABKContentCardsTableViewController()
    contentCardsVc.title = "Content Cards"
    navigationController?.pushViewController(contentCardsVc, animated: true)
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
// MARK: - Content Cards
  // 1
- (void)displayContentCards:(UINavigationController *)navigationController {
  // 2
  ABKContentCardsTableViewController *contentCardsVc = [[ABKContentCardsTableViewController alloc] init];
  contentCardsVc.title = @"Content Cards";
  [navigationController pushViewController:contentCardsVc animated:YES];
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

{% alert checkpoint %}
コードのコンパイルとアプリケーションの実行に進みます。<br><br>アプリケーションで `ABKContentCardsTableViewController` を表示してみてから先に進んでください。
{% endalert %}

## 次のステップ

おめでとうございます！このベストプラクティス統合ガイドを完了しました！`BrazeManager` ヘルパーファイルの例は、[GitHub](https://github.com/braze-inc/braze-growth-shares-ios-demo-app/blob/master/Braze-Demo/BrazeManager.swift) にあります。

これで、Braze iOS SDK への依存関係をプロダクションコードの残りの部分から切り離したので、オプションの高度な実装ガイドをいくつかご覧ください。
- [高度なプッシュ通知実装ガイド]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/implementation_guide/)
- [高度なアプリ内メッセージ実装ガイド]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/in-app_messaging/implementation_guide/)
- [高度なコンテンツカード実装ガイド]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/content_cards/implementation_guide/)

