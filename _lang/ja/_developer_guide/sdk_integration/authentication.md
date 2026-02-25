---
page_order: 1.2
nav_title: 認証
article_title: Braze SDKの認証設定
description: "この参考記事では、SDK 認証と、Braze SDK でこの機能を有効にする方法について説明します。"
platform:
  - iOS
  - Android
  - Web
  
---

# SDK認証の設定

> SDK 認証を使用すると、ログインしているユーザーの代わりに行われた SDK リクエストに対して (サーバー側で生成された) 暗号証明を提供できます。

## 仕組み

アプリでこの機能を有効にした後、無効または欠落しているJSON Web Token (JWT) を含むリクエストを拒否するようにBraze ダッシュボードを設定できます。これには次のものが含まれます。

- カスタムイベント、属性、購入、セッションデータを送信する
- Brazeワークスペースに新しいユーザーを作成する
- 標準ユーザープロファイル属性を更新する
- メッセージを受信またはトリガーする

これで、認証されていないログインユーザーがアプリのSDK APIキーを使って、他のユーザーに偽装するなどの悪意のあるアクションを実行するのを防ぐことができます。

## 認証のセットアップ

### ステップ1:サーバーのセットアップ {#server-side-integration}

#### ステップ1.1：公開鍵と秘密鍵のペアを生成する {#generate-keys}

RSA256公開鍵/秘密鍵ペアを生成します。公開キーは最終的に Braze のダッシュボードに追加されますが、秘密キーはサーバーに安全に保管する必要があります。

RS256 JWTアルゴリズムで使用する2048ビットのRSA鍵を推奨します。

{% alert warning %}
秘密キーは_非公開_にしておくことを忘れないでください。アプリやWeb サイトに秘密キーを公開したり、ハードコードしたりしてはなりません。あなたの秘密キーを知っている人なら誰でも、あなたのアプリケーションに代わってユーザーになりすましたり、ユーザーを作成したりすることができます。
{% endalert %}

#### ステップ1.2：現在のユーザーのJSONウェブトークンを作成する {#create-jwt}

秘密キーが手に入ったら、サーバー側のアプリケーションはそれを使って、現在ログインしているユーザーのアプリまたは Web サイトに JWT を返す必要があります。

通常、このロジックは、アプリが通常現在のユーザーのプロファイルをリクエストする任意の場所に配置できます。たとえば、ログインエンドポイントや、アプリが現在のユーザープロファイルを更新する場所などです。

JWTを生成する際には、以下のフィールドが期待されます：

**JWT ヘッダー**

| フィールド | 必須 | 説明                         |
| ----- | -------- | ----------------------------------- |
| `alg` | はい  | サポートされているアルゴリズムは`RS256`です。 |
| `typ` | はい  | タイプは `JWT` と同じでなければなりません。        |

{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

**JWT ペイロード**

| フィールド | 必須 | 説明                                                                            |
| ----- | -------- | -------------------------------------------------------------------------------------- |
| `sub` | はい  | 「subject」は、`changeUser` の呼び出し時に Braze SDK に指定したユーザー ID と同じである必要があります。  |
| `exp` | はい | このトークンをいつ期限切れにするかの「有効期限」。                                |

{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert tip %}
JSONウェブトークンについての詳細や、この署名プロセスを簡素化する多くのオープンソースライブラリを参照するには、[https://jwt.io](https://jwt.io) をチェックしてください。
{% endalert %}

### ステップ2:SDK の設定 {#sdk-integration}

この機能は、以下の [SDK バージョン]({{ site.baseurl }}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions)から利用可能です：

{% sdk_min_versions swift:5.0.0 android:14.0.0 web:3.3.0 %}

{% alert note %}
iOS 統合については、このページで Braze Swift SDK のステップを詳しく説明します。レガシー AppboyKit iOS SDK での使用例については、[このファイル](https://github.com/Appboy/appboy-ios-sdk/blob/master/Example/Stopwatch/Sources/AppDelegate.m)と[このファイル](https://github.com/Appboy/appboy-ios-sdk/blob/master/Example/Stopwatch/Sources/Utils/SdkAuthDelegate.m)を参照してください。
{% endalert %}

#### ステップ 2.1:Braze SDK で認証を有効にする

この機能が有効な場合、Braze SDK は、Braze サーバーに対して行われたネットワークリクエストに、現在のユーザーの最新の既知の JWT を追加します。

{% alert note %}
このオプションだけで初期化しても、Brazeダッシュボード内で[認証の適用を](#braze-dashboard)開始するまでは、データ収集には何の影響もないのでご心配なく。
{% endalert %}

{% tabs %}
{% tab Web %}
`initialize` を呼び出す際には、オプションの `enableSdkAuthentication` プロパティを `true` に設定します。
```javascript
import * as braze from "@braze/web-sdk";
braze.initialize("YOUR-API-KEY-HERE", {
  baseUrl: "YOUR-SDK-ENDPOINT-HERE",
  enableSdkAuthentication: true,
});
```
{% endtab %}
{% tab React Native %}
SDK認証は、ネイティブSDKの初期化中に有効にする必要があります。iOSとAndroidのネイティブコードに以下の設定を追加してください：

**iOS (AppDelegate.swift)**

```swift
import BrazeKit
import braze_react_native_sdk

let configuration = Braze.Configuration(
  apiKey: "{YOUR-BRAZE-API-KEY}",
  endpoint: "{YOUR-BRAZE-ENDPOINT}"
)
configuration.api.sdkAuthentication = true
let braze = BrazeReactBridge.perform(
  #selector(BrazeReactBridge.initBraze(_:)),
  with: configuration
).takeUnretainedValue() as! Braze
```

**Android (braze.xml)**

```xml
<bool name="com_braze_sdk_authentication_enabled">true</bool>
```

ネイティブレイヤーでSDK認証を有効にしたら、以下のステップで示すReact Native JavaScriptのメソッドを使用できます。
{% endtab %}
{% tab Java %}
Brazeインスタンスを設定するときは、`setIsSdkAuthenticationEnabled` を`true` に設定して呼び出します。
```java
BrazeConfig.Builder brazeConfigBuilder = new BrazeConfig.Builder()
    .setIsSdkAuthenticationEnabled(true);
Braze.configure(this, brazeConfigBuilder.build());
```

あるいは、braze.xml に`<bool name="com_braze_sdk_authentication_enabled">true</bool>` を追加することもできます。
{% endtab %}
{% tab KOTLIN %}
Brazeインスタンスを設定するときは、`setIsSdkAuthenticationEnabled` を`true` に設定して呼び出します。
```kotlin
BrazeConfig.Builder brazeConfigBuilder = BrazeConfig.Builder()
    .setIsSdkAuthenticationEnabled(true)
Braze.configure(this, brazeConfigBuilder.build())
```

あるいは、braze.xml に`<bool name="com_braze_sdk_authentication_enabled">true</bool>` を追加することもできます。
{% endtab %}
{% tab Objective-C %}
SDK 認証を有効にするには、Braze インスタンスを初期化する前に、`BRZConfiguration` オブジェクトの `configuration.api.sdkAuthentication` プロパティを `YES` に設定します。

```objc
BRZConfiguration *configuration =
    [[BRZConfiguration alloc] initWithApiKey:@"{BRAZE_API_KEY}"
                                    endpoint:@"{BRAZE_ENDPOINT}"];
configuration.api.sdkAuthentication = YES;
Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
AppDelegate.braze = braze;
```
{% endtab %}
{% tab Swift %}
SDK認証を有効にするには、SDKを初期化する際に、`Braze.Configuration` オブジェクトの`configuration.api.sdkAuthentication` プロパティを`true` に設定します：

```swift
let configuration = Braze.Configuration(apiKey: "{YOUR-BRAZE-API-KEY}",
                                        endpoint: "{YOUR-BRAZE-ENDPOINT}")
configuration.api.sdkAuthentication = true
let braze = Braze(configuration: configuration)
AppDelegate.braze = braze
```
{% endtab %}
{% tab Dart %}
現在、SDK 認証は、iOS と Android のネイティブコードで SDK を初期化する際に有効にする必要があります。Flutter SDK で SDK 認証を有効にするには、他のタブの iOS と Android の統合に従ってください。SDK 認証を有効にした後、残りの機能を Dart に統合することができます。
{% endtab %}
{% tab Flutter %}
SDK認証は、iOSやAndroidのネイティブコードでSDKを初期化する際に有効にする必要があります。ネイティブレイヤーで有効にすると、Flutter SDKのメソッドを使ってJWTシグネチャを渡すことができます。

**iOS**

SDK 認証を有効にするには、iOS ネイティブコードで`configuration.api.sdkAuthentication` プロパティを`true` に設定します：

```swift
let configuration = Braze.Configuration(apiKey: "{YOUR-BRAZE-API-KEY}", endpoint: "{YOUR-BRAZE-ENDPOINT}")
configuration.api.sdkAuthentication = true
let braze = Braze(configuration: configuration)
```

**Android (braze.xml)**

```xml
<bool name="com_braze_sdk_authentication_enabled">true</bool>
```

ネイティブレイヤーでSDK認証を有効にしたら、次のステップで示すFlutter SDKのメソッドを使うことができます。
{% endtab %}
{% tab Unity %}
SDK認証は、ネイティブSDKの初期化中に有効にする必要があります。iOSとAndroidのネイティブコードに以下の設定を追加してください：

**iOS**

設定ファイルで、`SDKAuthenticationEnabled` プロパティを`true` に設定します：

```xml
<key>SDKAuthenticationEnabled</key>
<true/>
```

**Android (braze.xml)**

```xml
<bool name="com_braze_sdk_authentication_enabled">true</bool>
```

ネイティブレイヤーでSDK認証を有効にした後、以下のステップで示すUnity C#メソッドを使用できます。
{% endtab %}
{% tab Cordova %}
SDK認証は、ネイティブSDKの初期化中に有効にする必要があります。iOSとAndroidのネイティブコードに以下の設定を追加してください：

**iOS**

SDK 認証を有効にするには、`config.xml` の`enableSDKAuthentication` プロパティを`true` に設定します：

```xml
<preference name="com.braze.ios_enable_sdk_authentication" value="true" />
```

**Android (braze.xml)**

```xml
<bool name="com_braze_sdk_authentication_enabled">true</bool>
```

ネイティブレイヤーでSDK認証を有効にした後、以下のステップで示すCordova JavaScriptのメソッドを使用することができます。
{% endtab %}
{% tab .NET MAUI (Xamarin) %}
SDK認証は、ネイティブSDKの初期化中に有効にする必要があります。SDK認証をiOSとAndroidで別々に設定します：

**iOS**

SDK 認証を有効にするには、SDK の初期化時に`configuration.Api.SdkAuthentication` プロパティを`true` に設定します：

```csharp
var configuration = new BRZConfiguration("YOUR-API-KEY", "YOUR-ENDPOINT");
configuration.Api.SdkAuthentication = true;
var braze = new Braze(configuration);
```

**Android (braze.xml)**

```xml
<bool name="com_braze_sdk_authentication_enabled">true</bool>
```

SDK認証を有効にした後、以下のステップで示す.NET MAUIメソッドを使用できます。
{% endtab %}
{% tab Expo %}
Braze Expoプラグインを使用する場合は、アプリの設定で`enableSdkAuthentication` プロパティを`true` に設定します。これにより、手動でネイティブコードを変更することなく、ネイティブiOSおよびAndroidレイヤーのSDK認証が自動的に設定されます。

**app.json または app.config.js**

```json
{
  "expo": {
    "plugins": [
      [
        "@braze/expo-plugin",
        {
          "enableSdkAuthentication": true
        }
      ]
    ]
  }
}
```

アプリの設定でSDK認証を有効にした後、React Nativeタブに表示されているReact Native JavaScriptメソッドを以下のステップで使用できます。

{% alert note %}
完全な実装例については、GitHubの[Braze Expoプラグインサンプルアプリ](https://github.com/braze-inc/braze-expo-plugin/blob/main/example/components/Braze.tsx)を参照してください。
{% endalert %}
{% endtab %}
{% endtabs %}

#### ステップ 2.2:現在のユーザーのJWT を設定する

アプリが Braze `changeUser` メソッドを呼び出すたびに、[サーバー側で生成された](#braze-dashboard) JWT も指定します。

また、トークンが現在のユーザーのセッションの途中でリフレッシュされるように設定することもできます。

{% alert note %}
`changeUser` は、ユーザー ID が_実際に変更された_場合にのみ呼び出す必要があることに注意してください。ユーザーID が変更されていない場合は、この方法を認証トークン(JWT) の更新方法として使用しないでください。
{% endalert %}

{% tabs %}
{% tab Web %}
[`changeUser`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser) の呼び出し時に JWT を指定します:

```javascript
import * as braze from "@braze/web-sdk";
braze.changeUser("NEW-USER-ID", "JWT-FROM-SERVER");
```

または、セッションの途中でユーザーのトークンをリフレッシュした場合：

```javascript
import * as braze from "@braze/web-sdk";
braze.setSdkAuthenticationSignature("NEW-JWT-FROM-SERVER");
```
{% endtab %}
{% tab React Native %}

[`changeUser`](https://braze-inc.github.io/braze-react-native-sdk/classes/Braze.Braze-1.html#changeUser) の呼び出し時に JWT を指定します:

```typescript
import Braze from '@braze/react-native-sdk';

Braze.changeUser("NEW-USER-ID", "JWT-FROM-SERVER");
```

または、セッションの途中でユーザーのトークンをリフレッシュした場合：

```typescript
import Braze from '@braze/react-native-sdk';

Braze.setSdkAuthenticationSignature("NEW-JWT-FROM-SERVER");
```
{% endtab %}
{% tab Java %}

[`changeUser`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/change-user.html) の呼び出し時に JWT を指定します:

```java
Braze.getInstance(this).changeUser("NEW-USER-ID", "JWT-FROM-SERVER");
```

または、セッションの途中でユーザーのトークンをリフレッシュした場合：

```java
Braze.getInstance(this).setSdkAuthenticationSignature("NEW-JWT-FROM-SERVER");
```
{% endtab %}
{% tab KOTLIN %}

[`changeUser`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/change-user.html) の呼び出し時に JWT を指定します:

```kotlin
Braze.getInstance(this).changeUser("NEW-USER-ID", "JWT-FROM-SERVER")
```

または、セッションの途中でユーザーのトークンをリフレッシュした場合：

```kotlin
Braze.getInstance(this).setSdkAuthenticationSignature("NEW-JWT-FROM-SERVER")
```
{% endtab %}
{% tab Objective-C %}

[`changeUser`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/changeuser(userid:sdkauthsignature:fileid:line:)) の呼び出し時に JWT を指定します:

```objc
[AppDelegate.braze changeUser:@"userId" sdkAuthSignature:@"JWT-FROM-SERVER"];
```

または、セッションの途中でユーザーのトークンをリフレッシュした場合：

```objc
[AppDelegate.braze setSDKAuthenticationSignature:@"NEW-JWT-FROM-SERVER"];
```
{% endtab %}
{% tab Swift %}

[`changeUser`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/changeuser(userid:sdkauthsignature:fileid:line:)) の呼び出し時に JWT を指定します:

```swift
AppDelegate.braze?.changeUser(userId: "userId", sdkAuthSignature: "JWT-FROM-SERVER")
```
または、セッションの途中でユーザーのトークンをリフレッシュした場合：

```swift
AppDelegate.braze?.set(sdkAuthenticationSignature: "NEW-JWT-FROM-SERVER")
```
{% endtab %}
{% tab Dart %}

[`changeUser`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser) の呼び出し時に JWT を指定します:

```dart
braze.changeUser("userId", sdkAuthSignature: "JWT-FROM-SERVER")
```
または、セッションの途中でユーザーのトークンをリフレッシュした場合：

```dart
braze.setSdkAuthenticationSignature("NEW-JWT-FROM-SERVER")
```

{% endtab %}
{% tab Flutter %}

`changeUser` を呼び出す際に JWT を提供します：

```dart
import 'package:braze_plugin/braze_plugin.dart';

BrazePlugin braze = BrazePlugin();
braze.changeUser("NEW-USER-ID", sdkAuthSignature: "JWT-FROM-SERVER");
```

または、セッションの途中でユーザーのトークンをリフレッシュした場合：

```dart
import 'package:braze_plugin/braze_plugin.dart';

BrazePlugin braze = BrazePlugin();
braze.setSdkAuthenticationSignature("NEW-JWT-FROM-SERVER");
```
{% endtab %}
{% tab Unity %}

`ChangeUser` を呼び出す際に JWT を提供します：

```csharp
BrazeBinding.ChangeUser("NEW-USER-ID", "JWT-FROM-SERVER");
```

または、セッションの途中でユーザーのトークンをリフレッシュした場合：

```csharp
BrazeBinding.SetSdkAuthenticationSignature("NEW-JWT-FROM-SERVER");
```
{% endtab %}
{% tab Cordova %}

`changeUser` を呼び出す際に JWT を提供します：

```javascript
BrazePlugin.changeUser("NEW-USER-ID", "JWT-FROM-SERVER");
```

または、セッションの途中でユーザーのトークンをリフレッシュした場合：

```javascript
BrazePlugin.setSdkAuthenticationSignature("NEW-JWT-FROM-SERVER");
```
{% endtab %}
{% tab .NET MAUI (Xamarin) %}

`ChangeUser` を呼び出す際に JWT を提供します：

**iOS**

```csharp
Braze.SharedInstance?.ChangeUser("NEW-USER-ID", "JWT-FROM-SERVER");
```

または、セッションの途中でユーザーのトークンをリフレッシュした場合：

```csharp
Braze.SharedInstance?.SetSDKAuthenticationSignature("NEW-JWT-FROM-SERVER");
```

**Android**

```csharp
Braze.GetInstance(this).ChangeUser("NEW-USER-ID", "JWT-FROM-SERVER");
```

または、セッションの途中でユーザーのトークンをリフレッシュした場合：

```csharp
Braze.GetInstance(this).SetSdkAuthenticationSignature("NEW-JWT-FROM-SERVER");
```
{% endtab %}
{% tab Expo %}

Braze Expoプラグインを使用する場合は、同じReact Native SDKのメソッドを使用します。`changeUser` を呼び出す際に JWT を提供します：

```typescript
import Braze from '@braze/react-native-sdk';

Braze.changeUser("NEW-USER-ID", "JWT-FROM-SERVER");
```

または、セッションの途中でユーザーのトークンをリフレッシュした場合：

```typescript
import Braze from '@braze/react-native-sdk';

Braze.setSdkAuthenticationSignature("NEW-JWT-FROM-SERVER");
```
{% endtab %}
{% endtabs %}

#### ステップ 2.3:無効なトークンのコールバック関数を登録する {#sdk-callback}

この機能が[必須](#enforcement-options)に設定されている場合、以下のシナリオでSDKリクエストがBrazeによって拒否されます：
- Braze APIが受信した時点でJWTの有効期限が切れていた
- JWTが空または欠落していた
- Brazeダッシュボードにアップロードした公開鍵でJWTの検証に失敗した

`subscribeToSdkAuthenticationFailures` を使用して、これらのいずれかの理由で SDK リクエストが失敗したときに通知を受け取るようにサブスクライブできます。コールバック関数には、関連する[`errorCode`](#error-codes)、エラーの`reason`、リクエストの`userId`（ユーザーは匿名にできない）、エラーの原因となった認証トークン（JWT）を持つオブジェクトが含まれます。

失敗したリクエストは、アプリが新しい有効な JWT を提供するまで、定期的に再試行されます。そのユーザーがまだログインしている場合、このコールバックをサーバーに新しいJWTを要求する機会として使用し、この新しい有効なトークンをBraze SDKに供給することができます。

認証エラーを受け取ったら、エラーの`userId`が現在ログインしているユーザーと一致することを確認し、サーバーから新しい署名を取得してBraze SDKに提供してください。これらのエラーは、モニタリングサービスやエラーレポートサービスに記録することもできます。

{% alert tip %}
これらのコールバックメソッドは、独自の監視サービスやエラーログサービスを追加して、Brazeリクエストが拒否される頻度を追跡するのに最適な場所です。
{% endalert %}

{% tabs %}
{% tab Web %}
```javascript
import * as braze from "@braze/web-sdk";

braze.subscribeToSdkAuthenticationFailures((error) => {
  console.error("SDK authentication failed:", error);
  console.log("Error code:", error.errorCode);
  console.log("User ID:", error.userId);
  // Note: Do not log error.signature as it contains sensitive authentication credentials
  
  // Verify the error.userId matches the currently logged-in user
  // Fetch a new token from your server and set it
  fetchNewSignature(error.userId).then((newSignature) => {
    braze.setSdkAuthenticationSignature(newSignature);
  });
});
```
{% endtab %}
{% tab React Native %}
```typescript
import Braze from '@braze/react-native-sdk';

const sdkAuthErrorSubscription = Braze.addListener(
  Braze.Events.SDK_AUTHENTICATION_ERROR,
  (error) => {
    console.log(`SDK Authentication for ${error.userId} failed with error code ${error.errorCode}.`);
    
    const updated_jwt = getNewTokenSomehow(error);
    Braze.setSdkAuthenticationSignature(updated_jwt);
  }
);

// Don't forget to remove the listener when done
// sdkAuthErrorSubscription.remove();
```
{% endtab %}
{% tab Java %}
```java
Braze.getInstance(this).subscribeToSdkAuthenticationFailures(error -> {
    String newToken = getNewTokenSomehow(error);
    Braze.getInstance(getContext()).setSdkAuthenticationSignature(newToken);
});
```
{% endtab %}
{% tab KOTLIN %}
```kotlin
Braze.getInstance(this).subscribeToSdkAuthenticationFailures({ error: BrazeSdkAuthenticationErrorEvent ->
    val newToken: String = getNewTokenSomehow(error)
    Braze.getInstance(getContext()).setSdkAuthenticationSignature(newToken)
})
```
{% endtab %}
{% tab Objective-C %}

```objc
Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
braze.sdkAuthDelegate = delegate;
AppDelegate.braze = braze;

// Method to implement in delegate
- (void)braze:(Braze *)braze sdkAuthenticationFailedWithError:(BRZSDKAuthenticationError *)error {
  NSLog(@"Invalid SDK Authentication Token.");
  NSString *newSignature = getNewTokenSomehow(error);
  [AppDelegate.braze setSDKAuthenticationSignature:newSignature];
}
```
{% endtab %}
{% tab Swift %}

```swift
let braze = Braze(configuration: configuration)
braze.sdkAuthDelegate = delegate
AppDelegate.braze = braze

// Method to implement in delegate
func braze(_ braze: Braze, sdkAuthenticationFailedWithError error: Braze.SDKAuthenticationError) {
  print("Invalid SDK Authentication Token.")
  let newSignature = getNewTokenSomehow(error)
  AppDelegate.braze?.set(sdkAuthenticationSignature: newSignature)
}
```
{% endtab %}
{% tab Dart %}
```dart
braze.setBrazeSdkAuthenticationErrorCallback((BrazeSdkAuthenticationError error) async {
  print("Invalid SDK Authentication Token.");
  final newSignature = getNewTokenSomehow(error);
  braze.setSdkAuthenticationSignature(newSignature);
});
```
{% endtab %}
{% tab Flutter %}
```dart
import 'package:braze_plugin/braze_plugin.dart';

BrazePlugin braze = BrazePlugin();

braze.setBrazeSdkAuthenticationErrorCallback((BrazeSdkAuthenticationError error) async {
  print("SDK Authentication for ${error.userId} failed with error code ${error.errorCode}.");
  
  String newSignature = getNewTokenSomehow(error);
  braze.setSdkAuthenticationSignature(newSignature);
});
```
{% endtab %}
{% tab Unity %}
**iOS**

SDK認証デリゲートをiOSネイティブ実装に設定します：

```csharp
public class SdkAuthDelegate : BRZSdkAuthDelegate
{
  public void Braze(Braze braze, BRZSDKAuthenticationError error)
  {
    Debug.Log("Invalid SDK Authentication Token.");
    string newSignature = GetNewTokenSomehow(error);
    BrazeBinding.SetSdkAuthenticationSignature(newSignature);
  }
}
```

**Android**

```csharp
Braze.GetInstance(this).SubscribeToSdkAuthenticationFailures((error) => {
  string newToken = GetNewTokenSomehow(error);
  Braze.GetInstance(this).SetSdkAuthenticationSignature(newToken);
});
```
{% endtab %}
{% tab Cordova %}
```javascript
BrazePlugin.subscribeToSdkAuthenticationFailures((error) => {
  console.log(`SDK Authentication for ${error.user_id} failed with error code ${error.error_code}.`);
  
  const newSignature = getNewTokenSomehow(error);
  BrazePlugin.setSdkAuthenticationSignature(newSignature);
});
```
{% endtab %}
{% tab .NET MAUI (Xamarin) %}
**iOS**

`Braze` インスタンスに SDK 認証デリゲートを設定します：

```csharp
public class SdkAuthDelegate : BRZSdkAuthDelegate
{
  public override void Braze(Braze braze, BRZSDKAuthenticationError error)
  {
    Console.WriteLine("Invalid SDK Authentication Token.");
    string newSignature = GetNewTokenSomehow(error);
    Braze.SharedInstance?.SetSDKAuthenticationSignature(newSignature);
  }
}

// Set the delegate during initialization
var configuration = new BRZConfiguration("YOUR-API-KEY", "YOUR-ENDPOINT");
configuration.Api.SdkAuthentication = true;
var braze = new Braze(configuration);
braze.SdkAuthDelegate = new SdkAuthDelegate();
```

**Android**

```csharp
Braze.GetInstance(this).SubscribeToSdkAuthenticationFailures((error) => {
  string newToken = GetNewTokenSomehow(error);
  Braze.GetInstance(this).SetSdkAuthenticationSignature(newToken);
});
```
{% endtab %}
{% tab Expo %}
Braze Expoプラグインを使用する場合は、同じReact Native SDKのメソッドを使用します：

```typescript
import Braze from '@braze/react-native-sdk';

const sdkAuthErrorSubscription = Braze.addListener(
  Braze.Events.SDK_AUTHENTICATION_ERROR,
  (error) => {
    console.log(`SDK Authentication for ${error.userId} failed with error code ${error.errorCode}.`);
    
    const updated_jwt = getNewTokenSomehow(error);
    Braze.setSdkAuthenticationSignature(updated_jwt);
  }
);

// Don't forget to remove the listener when done
// sdkAuthErrorSubscription.remove();
```
{% endtab %}
{% endtabs %}

### ステップ 3:ダッシュボードで認証を有効にする {#braze-dashboard}

次に、前に設定したアプリのBraze ダッシュボードで認証を有効にできます。

Braze ダッシュボードでアプリの SDK 認証設定が「**必須**」に設定されていない限り、SDK リクエストは認証なしで通常どおり処理され続けることに注意してください。

統合に何か問題が発生した場合（例えば、アプリがSDKにトークンを不正に渡している、またはサーバーが無効なトークンを生成している）、Brazeダッシュボードでこの機能を無効にすると、データは検証なしで通常通り流れるようになります。

#### 適用オプション {#enforcement-options}

ダッシュボードの**設定の管理**ページでは、各アプリに3つのSDK認証ステートがあり、Brazeがどのようにリクエストを検証するかを制御します。

| 設定| 説明|
| ------ | ---------- |
| **無効** | Brazeは、ユーザーに提供されたJWTを検証しません。（デフォルト設定）|
| **オプション** | Brazeは、ログインしているユーザーのリクエストを検証しますが、無効なリクエストは拒否しません。 |
| **必須** | Brazeは、ログインしているユーザーのリクエストを検証し、無効なJWTは拒否します。|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![]({% image_buster /assets/img/sdk-auth-settings.png %})

**オプション**設定は、この機能がアプリのSDKトラフィックに与える潜在的な影響を監視するのに便利な方法です。

無効な JWT は**オプション**と**必須**の両方の状態でレポートされますが、**必須**状態でのみ SDK リクエストが拒否され、アプリは再試行して新しい JWT をリクエストします。

## 公開鍵の管理 {#key-management}

### 公開鍵を追加する

アプリごとに、プライマリ、セカンダリ、ターシャリの最大3つの公開キーを追加できます。必要に応じて、同じキーを複数のアプリに追加することもできます。公開鍵を追加するには：

1. Brazeのダッシュボードに行き、**「設定」**>「**アプリ設定**」を選択します。
2. 利用可能なアプリのリストからアプリを選びます。
3. [**SDK 認証**] で、[**公開キーを追加**] を選択します。
4. オプションの説明を入力し、公開キーを貼り付け、[**公開キーを追加**] を選択します。

### 新しいプライマリキーを割り当てる

セカンダリキーまたはターシャリキーを新しいプライマリキーとして割り当てるには：

1. Brazeのダッシュボードに行き、**「設定」**>「**アプリ設定**」を選択します。
2. 利用可能なアプリのリストからアプリを選びます。
3. [**SDK 認証**] でキーを選択し、[**管理**] > [**プライマリキーに設定**] を選択します。

### キーを削除する

プライマリキーを削除するには、まず[新たなプライマリキーを割り当て](#assign-a-new-primary-key)、それからキーを削除します。非プライマリキーを削除するには：

1. Brazeのダッシュボードに行き、**「設定」**>「**アプリ設定**」を選択します。
2. 利用可能なアプリのリストからアプリを選びます。
3. [**SDK 認証**] でプライマリキー以外のキーを選択し、[**管理**] > [**公開キーを削除**] を選択します。

## 分析 {#analytics}

各アプリには、この機能が**オプション**状態と**必須**状態にある間に収集された SDK 認証エラーの内訳が表示されます。

データはリアルタイムで入手でき、チャート上のポイントにカーソルを合わせると、指定した日付のエラーの内訳を見ることができます。

![認証エラーの発生件数を示すグラフ。また、エラーの総数、エラーの種類、調整可能な日付範囲も表示される。]({% image_buster /assets/img/sdk-auth-analytics.png %}){: style="max-width:80%"}

## エラーコード {#error-codes}

| エラーコード| エラーの理由 | 説明 | 解決手順 |
| --------  | ------------ | ---------  | ---------  |
| 10 | `EXPIRATION_REQUIRED` | Braze を使用する場合、有効期限は必須フィールドです。| JWT作成ロジックに`exp` または有効期限フィールドを追加してください。 |
| 20 | `DECODING_ERROR` | 公開鍵が一致しないか、一般的な捕捉不能エラーが発生しました。| JWTテストツールにJWTをコピーして、JWTが無効なフォーマットである理由を診断してください。 |
| 21 | `SUBJECT_MISMATCH` | 期待されるサブジェクトと実際のサブジェクトが一致しません。| `sub` フィールドは、`changeUser` SDK メソッドに渡されたユーザー ID と同じでなければなりません。 |
| 22 | `EXPIRED` | 提供されたトークンの有効期限が切れています。| 有効期限を延長するか、有効期限が切れる前に定期的にトークンをリフレッシュしてください。 |
| 23 | `INVALID_PAYLOAD` | トークンのペイロードが無効です。| JWTテストツールにJWTをコピーして、JWTが無効なフォーマットである理由を診断してください。 |
| 24 | `INCORRECT_ALGORITHM` | トークンのアルゴリズムはサポートされていません。| JWTを`RS256` 暗号化を使用するように変更してください。その他のタイプには対応していません。 |
| 25 | `PUBLIC_KEY_ERROR` | 公開鍵が適切な形式に変換できませんでした。| JWTテストツールにJWTをコピーして、JWTが無効なフォーマットである理由を診断してください。 |
| 26 | `MISSING_TOKEN` | リクエストにトークンが指定されていません。| `changeUser(id, token)` を呼び出す際にトークンを渡していること、トークンが空白でないことを確認してください。|
| 27 | `NO_MATCHING_PUBLIC_KEYS` | 提供されたトークンに一致する公開鍵がありませんでした。| JWTで使用されている秘密キーが、アプリに設定されている公開キーと一致しません。公開キーを、このAPIキーと一致するワークスペース内の正しいアプリに追加したことを確認してください。|
| 28 | `PAYLOAD_USER_ID_MISMATCH` | リクエストのペイロードに含まれるすべてのユーザーIDが、要求されたとおりに一致しません。| これは予期しないエラーであり、不正なペイロードを引き起こす可能性があります。サポートチケットを開いてサポートを受けてください。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## よくある質問 (FAQ) {#faq}

#### この機能はすべてのアプリで同時に有効にする必要がありますか？ {#faq-app-by-app}

いいえ、この機能は特定のアプリに対して有効にすることができ、すべてのアプリで一度に使用する必要はありません。

#### アプリの古いバージョンを使っているユーザーはどうなりますか？ {#faq-sdk-backward-compatibility}

この機能を適用し始めると、古いバージョンのアプリによるリクエストは Braze によって拒否され、SDK によって再試行されます。ユーザーがアプリをサポートされたバージョンにアップグレードすると、キューに入れられたリクエストは再び受け入れられるようになります。

可能であれば、他の必須アップグレードと同様に、ユーザーにアップグレードを勧めてください。あるいは、許容できる割合のユーザーがアップグレードしたことを確認するまで、この機能を[オプショナル](#enforcement-options)にしておくこともできます。

#### JWT を生成するときには、どのような有効期限を使用する必要がありますか？ {#faq-expiration}

平均セッション期間、セッション Cookie/トークンの有効期限、またはアプリケーションが現在のユーザープロファイルをそれ以外の方法で更新する頻度のうち、高い方の値を使用することをお勧めします。

#### ユーザーのセッションの途中でJWTの有効期限が切れた場合はどうなりますか？ {#faq-jwt-expiration}

ユーザーのトークンがセッション中に期限切れになると、SDK は[コールバック関数](#sdk-callback)を呼び出して、Braze にデータを送信し続けるために新しいJWT が必要であることをアプリに知らせます。

#### サーバー側の統合が壊れ、JWT を作成できなくなった場合はどうなりますか？ {#faq-server-downtime}

サーバーが JWT を提供できない場合、または統合に問題がある場合は、Braze ダッシュボードでいつでも機能を無効にできます。

一度無効にすると、保留中の失敗したSDKリクエストは最終的にSDKによって再試行され、Brazeによって受け入れられます。

#### なぜこの機能では、共有シークレットではなく公開キー/秘密キーを使うのでしょうか？ {#faq-shared-secrets}

共有シークレットを使う場合、Brazeのダッシュボードページなど、その共有シークレットにアクセスできる人なら誰でも、トークンを生成してエンドユーザーになりすますことができます。

その代わり、公開鍵/秘密鍵を使用することで、Brazeの従業員でさえ（ダッシュボードのユーザーはもちろん）秘密キーにアクセスできないようにしています。

#### 拒否されたリクエストはどのように再試行されますか？ {#faq-retry-logic}

認証エラーが原因でリクエストが拒否されると、SDK はユーザーのJWT を更新するために使用されるコールバックを呼び出します。

リクエストは指数バックオフアプローチを使用して定期的に再試行されます。50回連続で失敗すると、次のセッション開始まで再試行は一時停止されます。各 SDK には、手動でデータフラッシュをリクエストするメソッドもあります。

#### SDK認証を匿名ユーザーに使用できますか？ {#faq-anonymous-users}

いいえ。SDK認証は匿名ユーザーには適用されません。