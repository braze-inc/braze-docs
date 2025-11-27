## React Native Braze SDKについて

React Native Braze SDKを統合することで、基本的な分析機能を提供し、1つのコードベースだけでiOSとAndroidの両方のアプリ内メッセージとコンテンツカードを統合できる。

## 新アーキテクチャーの互換性

以下の最小SDKバージョンは、[React Nativeの新アーキテクチャを](https://reactnative.dev/docs/the-new-architecture/landing-page)使用するすべてのアプリと互換性がある：

{% sdk_min_versions reactnative:2.0.1 %}

SDKバージョン6.0.0から、BrazeはReact Native Turbo Moduleを使用しており、New Architectureとレガシーブリッジアーキテクチャの両方に対応している。

{% alert warning %}
あなたのiOSアプリが`RCTAppDelegate` に準拠し、前回の`AppDelegate` のセットアップに従っている場合は、Turboモジュールのイベントをサブスクライバーする際にクラッシュが発生しないように、[Complete native setupの](#reactnative_step-2-complete-native-setup)サンプルを確認してほしい。
{% endalert %}

## React Native SDKを統合する

### 前提条件

SDKを統合するには、React Nativeバージョン0.71以降が必要である。サポートされているバージョンの完全なリストについては、 [React Native SDK GitHub リポジトリ](https://github.com/braze-inc/braze-react-native-sdk?tab=readme-ov-file#version-support)を参照してください。

### ステップ 1: Braze ライブラリーの統合

{% tabs local %}
{% tab npm %}
```bash
npm install @braze/react-native-sdk
```
{% endtab %}
{% tab yarn %}
```bash
yarn add @braze/react-native-sdk
```
{% endtab %}
{% endtabs %}

### ステップ 2: セットアップオプションを選択する

Braze SDKは、Braze Expoプラグインまたはネイティブレイヤーのいずれかを使用して管理できる。Expoプラグインを使えば、ネイティブレイヤーにコードを書くことなく、特定のSDK機能を設定できる。アプリのニーズに最も適したオプションを選択しよう。

{% tabs %}
{% tab Expo %}
#### ステップ2.1: Braze Expo プラグインのインストール

Braze React Native SDK のバージョンが1.37.0以降であることを確認してください。サポートされているバージョンの全リストは、[Braze React Native](https://github.com/braze-inc/braze-expo-plugin?tab=readme-ov-file#version-support)リポジトリをチェックしてほしい。

Braze Expoプラグインをインストールするには、以下のコマンドを実行する：

```bash
npx expo install @braze/expo-plugin
```

#### ステップ 2.2:app.json にプラグインを追加する

`app.json` で、Braze Expo プラグインを追加します。次の構成オプションを指定できます。

| 方法                                        | タイプ    | 説明                                                                                                                                              |
| --------------------------------------------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `androidApiKey`                               | ストリング  | 必須です。Braze ダッシュボードの [**設定の管理**] にある Android アプリケーションの [API キー]({{site.baseurl}}/api/identifier_types/)。 |
| `iosApiKey`                                   | ストリング  | 必須です。Braze ダッシュボードの [**設定の管理**] にある iOS アプリケーションの [API キー]({{site.baseurl}}/api/identifier_types/)。     |
| `baseUrl`                                     | ストリング  | 必須です。Braze ダッシュボードの [**設定の管理**] にあるアプリケーションの [SDK エンドポイント]({{site.baseurl}}/api/basics/#endpoints)。    |
| `enableBrazeIosPush`                          | ブーリアン | iOSのみ。iOS でのプッシュ通知の処理に Braze を使用するかどうか。React Native SDK v1.38.0とExpo Plugin v0.4.0で導入された。                       |
| `enableFirebaseCloudMessaging`                | ブーリアン | Android のみ。プッシュ通知に Firebase Cloud Messaging を使用するかどうか。React Native SDK v1.38.0とExpo Plugin v0.4.0で導入された。             |
| `firebaseCloudMessagingSenderId`              | ストリング  | Android のみ。Firebase Cloud Messaging の送信者 ID。React Native SDK v1.38.0とExpo Plugin v0.4.0で導入された。                                    |
| `sessionTimeout`                              | 整数 | アプリケーションの Braze セッションタイムアウト (秒単位)。                                                                                               |
| `enableSdkAuthentication`                     | ブーリアン | [SDK認証](https://www.braze.com/docs/developer_guide/platform_wide/sdk_authentication#sdk-authentication)機能を有効にするかどうか。      |
| `logLevel`                                    | 整数 | アプリケーションのログレベル。デフォルトのログレベルは8で、最小限の情報をロギングします。デバッグのために冗長ロギングを有効にするには、ログレベル0を使う。    |
| `minimumTriggerIntervalInSeconds`             | 整数 | トリガー間の最小時間間隔 (秒単位)。デフォルトは30秒です。                                                                           |
| `enableAutomaticLocationCollection`           | ブーリアン | 自動位置情報収集が有効かどうか（ユーザーが許可した場合）。                                                                                  |
| `enableGeofence`                              | ブーリアン | ジオフェンスを有効にするかどうか。                                                                                                                           |
| `enableAutomaticGeofenceRequests`             | ブーリアン | ジオフェンスリクエストを自動で行うかどうか。                                                                                                  |
| `dismissModalOnOutsideTap`                    | ブーリアン | iOSのみ。ユーザーがアプリ内メッセージの外側をクリックしたときに、モーダルアプリ内メッセージが閉じられるかどうか。                                           |
| `androidHandlePushDeepLinksAutomatically`     | ブーリアン | Android のみ。Braze SDKが自動的にプッシュディープリンクを処理するかどうか。                                                                         |
| `androidPushNotificationHtmlRenderingEnabled` | ブーリアン | Android のみ。`android.text.Html.fromHtml` を使って、プッシュ通知のテキストコンテンツをHTMLとして解釈し、レンダリングするかどうかを設定する。        |
| `androidNotificationAccentColor`              | ストリング  | Android のみ。Android通知のアクセントカラーを設定する。                                                                                                |
| `androidNotificationLargeIcon`                | ストリング  | Android のみ。Androidの通知アイコンを大きく設定する。                                                                                                  |
| `androidNotificationSmallIcon`                | ストリング  | Android のみ。Androidの通知小アイコンを設定する。                                                                                                  |
| `iosRequestPushPermissionsAutomatically`      | ブーリアン | iOSのみ。アプリの起動時にユーザーにプッシュ許可を自動的に求めるかどうか。                                                          |
| `enableBrazeIosRichPush`                      | ブーリアン | iOSのみ。iOSのリッチプッシュ機能を有効にするかどうか。                                                                                                  |
| `enableBrazeIosPushStories`                   | ブーリアン | iOSのみ。iOSのBraze Push Storiesを有効にするかどうか。                                                                                                  |
| `iosPushStoryAppGroup`                        | ストリング  | iOSのみ。iOSのプッシュストーリーズに使われているアプリ群だ。                                                                                                       |
| `iosUseUUIDAsDeviceId`                        | ブーリアン | iOSのみ。デバイスIDにランダムに生成されたUUIDを使用するかどうか。                                                                                       |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

構成例:

```json
{
  "expo": {
    "plugins": [
      [
        "@braze/expo-plugin",
        {
          "androidApiKey": "YOUR-ANDROID-API-KEY",
          "iosApiKey": "YOUR-IOS-API-KEY",
          "baseUrl": "YOUR-SDK-ENDPOINT",
          "sessionTimeout": 60,
          "enableGeofence": false,
          "enableBrazeIosPush": false,
          "enableFirebaseCloudMessaging": false,
          "firebaseCloudMessagingSenderId": "YOUR-FCM-SENDER-ID",
          "androidHandlePushDeepLinksAutomatically": true,
          "enableSdkAuthentication": false,
          "logLevel": 0,
          "minimumTriggerIntervalInSeconds": 0,
          "enableAutomaticLocationCollection": false,
          "enableAutomaticGeofenceRequests": false,
          "dismissModalOnOutsideTap": true,
          "androidPushNotificationHtmlRenderingEnabled": true,
          "androidNotificationAccentColor": "#ff3344",
          "androidNotificationLargeIcon": "@drawable/custom_app_large_icon",
          "androidNotificationSmallIcon": "@drawable/custom_app_small_icon",
          "iosRequestPushPermissionsAutomatically": false,
          "enableBrazeIosPushStories": true,
          "iosPushStoryAppGroup": "group.com.example.myapp.PushStories"
        }
      ],
    ]
  }
}
```

#### ステップ 2.3:アプリケーションのビルドおよび実行

アプリケーションを事前にビルドすることで、Braze Expoプラグインが動作するために必要なネイティブファイルが生成される。

```bash
npx expo prebuild
```

[Expo ドキュメント](https://docs.expo.dev/workflow/customizing/)の指定に従い、アプリケーションを実行します。コンフィギュレーション・オプションに変更を加えると、アプリケーションのプリビルドと再実行が必要になることを覚えておいてほしい。
{% endtab %}

{% tab Android %}

#### ステップ2.1: リポジトリの追加

最上位プロジェクト `build.gradle` で、`buildscript` > `dependencies` から以下を追加します。

```groovy
buildscript {
    dependencies {
        ...
        // Choose your Kotlin version
        classpath("org.jetbrains.kotlin:kotlin-gradle-plugin:1.8.10")
    }
}
```

これにより、Kotlin がプロジェクトに追加されます。

#### ステップ2.2: Braze SDK の構成

Braze サーバーに接続するには、プロジェクトの `res/values` フォルダで `braze.xml` ファイルを作成します。次のコードを貼り付け、API [キー]({{site.baseurl}}/api/identifier_types/)および[エンドポイント]({{site.baseurl}}/api/basics/#endpoints)を実際の値に置き換えます。

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
  <string translatable="false" name="com_braze_api_key">YOU_APP_IDENTIFIER_API_KEY</string>
  <string translatable="false" name="com_braze_custom_endpoint">YOUR_CUSTOM_ENDPOINT_OR_CLUSTER</string>
</resources>
```

必要な権限をファイル `AndroidManifest.xml` に追加します。

```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
```

{% alert tip %}
Braze SDK バージョン12.2.0 以降では、`importBrazeLocationLibrary=true` を`gradle.properties` ファイルに設定することで、android-sdk-location ライブラリを自動的にプルインできます。
{% endalert %}

#### ステップ2.3: ユーザーセッショントラッキングの実装

`openSession()` および `closeSession()` への呼び出しは自動的に処理されます。
`MainApplication` クラスの `onCreate()` メソッドに次のコードを追加します。

{% subtabs local %}
{% subtab JAVA %}
```java
import com.braze.BrazeActivityLifecycleCallbackListener;

@Override
public void onCreate() {
    super.onCreate();
    ...
    registerActivityLifecycleCallbacks(new BrazeActivityLifecycleCallbackListener());
}
```
{% endsubtab %}
{% subtab KOTLIN %}
```kotlin
import com.braze.BrazeActivityLifecycleCallbackListener

override fun onCreate() {
    super.onCreate()
    ...
    registerActivityLifecycleCallbacks(BrazeActivityLifecycleCallbackListener())
}
```
{% endsubtab %}
{% endsubtabs %}

#### ステップ2.4: インテント更新の処理

MainActivity で `android:launchMode` が `singleTask` に設定されている場合は、次のコードを `MainActivity` クラスに追加します。

{% subtabs local %}
{% subtab JAVA %}
```java
@Override
public void onNewIntent(Intent intent) {
    super.onNewIntent(intent);
    setIntent(intent);
}
```
{% endsubtab %}
{% subtab KOTLIN %}
```kotlin
override fun onNewIntent(intent: Intent) {
    super.onNewIntent(intent)
    setIntent(intent)
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab iOS %}

#### ステップ2.1: (オプション) ダイナミック XCFramework に関する Podfile の構成

BrazeUI などの特定の Braze ライブラリーを Objective-C++ ファイルにインポートするには、`#import` 構文を使用する必要があります。Braze Swift SDKのバージョン7.4.0以降、バイナリにはこの構文と互換性のある[ダイナミック XCFramework としてのオプションの配布チャネル](https://github.com/braze-inc/braze-swift-sdk-prebuilt-dynamic)があります。

この配布チャネルを使用する場合は、Podfile で CocoaPods のソースの場所を手動で上書きします。以下のサンプルを参照し、インポートする関連バージョンで `{your-version}` を置き換えてください。

```ruby
pod 'BrazeKit', :podspec => 'https://raw.githubusercontent.com/braze-inc/braze-swift-sdk-prebuilt-dynamic/{your-version}/BrazeKit.podspec'
pod 'BrazeUI', :podspec => 'https://raw.githubusercontent.com/braze-inc/braze-swift-sdk-prebuilt-dynamic/{your-version}/BrazeUI.podspec'
pod 'BrazeLocation', :podspec => 'https://raw.githubusercontent.com/braze-inc/braze-swift-sdk-prebuilt-dynamic/{your-version}/BrazeLocation.podspec'
```

#### ステップ 2.2:ポッドのインストール

React Native ではライブラリーがネイティブプラットフォームに自動でリンクされるため、CocoaPods を使用して SDK をインストールできます。

プロジェクトのルートフォルダから:

```bash
# To install using the React Native New Architecture
cd ios && pod install

# To install using the React Native legacy architecture
cd ios && RCT_NEW_ARCH_ENABLED=0 pod install
```

#### ステップ 2.3:Braze SDK の構成

{% subtabs local %}
{% subtab SWIFT %}

`AppDelegate.swift` ファイルの先頭にある Braze SDK をインポートします。
```swift
import BrazeKit
```

`application(_:didFinishLaunchingWithOptions:)` メソッドで、API [キー]({{site.baseurl}}/api/identifier_types/)および[エンドポイント]({{site.baseurl}}/api/basics/#endpoints)をアプリの値に置き換えます。次に、構成を使用して Braze インスタンスを作成し、簡単にアクセスできるよう `AppDelegate` で静的プロパティを作成します。

{% alert note %}
この例では、React Native 設定で多くの抽象化を提供する [RCTAppDelegate](https://github.com/facebook/react-native/blob/e64756ae5bb5c0607a4d97a134620fafcb132b3b/packages/react-native/Libraries/AppDelegate/RCTAppDelegate.h) の実装を前提としています。アプリに別の設定を使用している場合は、必要に応じて実装を調整してください。
{% endalert %}

```swift
func application(
    _ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey : Any]? = nil
) -> Bool {
    // Setup Braze
    let configuration = Braze.Configuration(
        apiKey: "{BRAZE_API_KEY}",
        endpoint: "{BRAZE_ENDPOINT}")
    // Enable logging and customize the configuration here.
    configuration.logger.level = .info
    let braze = BrazeReactBridge.perform(
      #selector(BrazeReactBridge.initBraze(_:)),
      with: configuration
    ).takeUnretainedValue() as! Braze

    AppDelegate.braze = braze

    /* Other configuration */

    return true
}

// MARK: - AppDelegate.braze

static var braze: Braze? = nil
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

`AppDelegate.m` ファイルの先頭にある Braze SDK をインポートします。
```objc
#import <BrazeKit/BrazeKit-Swift.h>
#import "BrazeReactBridge.h"
```

`application:didFinishLaunchingWithOptions:` メソッドで、API [キー]({{site.baseurl}}/api/identifier_types/)および[エンドポイント]({{site.baseurl}}/api/basics/#endpoints)をアプリの値に置き換えます。次に、構成を使用して Braze インスタンスを作成し、簡単にアクセスできるよう `AppDelegate` で静的プロパティを作成します。

{% alert note %}
この例では、React Native 設定で多くの抽象化を提供する [RCTAppDelegate](https://github.com/facebook/react-native/blob/e64756ae5bb5c0607a4d97a134620fafcb132b3b/packages/react-native/Libraries/AppDelegate/RCTAppDelegate.h) の実装を前提としています。アプリに別の設定を使用している場合は、必要に応じて実装を調整してください。
{% endalert %}

```objc
- (BOOL)application:(UIApplication *)application
    didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  // Setup Braze
  BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:@"{BRAZE_API_KEY}"
                                                                    endpoint:@"{BRAZE_ENDPOINT}"];
  // Enable logging and customize the configuration here.
  configuration.logger.level = BRZLoggerLevelInfo;
  Braze *braze = [BrazeReactBridge initBraze:configuration];
  AppDelegate.braze = braze;

  /* Other configuration */

  return YES;
}

#pragma mark - AppDelegate.braze

static Braze *_braze = nil;

+ (Braze *)braze {
  return _braze;
}

+ (void)setBraze:(Braze *)braze {
  _braze = braze;
}
```

{% endsubtab %}
{% endsubtabs %}

{% endtab %}
{% endtabs %}

### ステップ 3: ライブラリーをインポートする

次に、React Nativeのコードでライブラリを`import` 。詳しくは[サンプル・プロジェクトを](https://github.com/braze-inc/braze-react-native-sdk/tree/master/BrazeProject)ご覧いただきたい。 

```javascript
import Braze from "@braze/react-native-sdk";
```

### ステップ 4: 統合をテストする（オプション）

SDKの統合をテストするには、アプリで以下のコードを呼び出して、どちらのプラットフォームでもユーザーの新しいセッションを開始する。

```javascript
Braze.changeUser("userId");
```

たとえば、アプリの起動時にユーザー ID を割り当てることができます。

```javascript
import React, { useEffect } from "react";
import Braze from "@braze/react-native-sdk";

const App = () => {
  useEffect(() => {
    Braze.changeUser("some-user-id");
  }, []);

  return (
    <div>
      ...
    </div>
  )
```

Brazeのダッシュボードで、[ユーザー検索に]({{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search#using-user-search)行き、`some-user-id` に一致するIDを持つユーザーを探す。ここで、セッションデータとデバイスデータが記録されたことを確認できる。
