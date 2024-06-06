---
nav_title: SDK の初期セットアップ
article_title: Xamarin用の初期SDKセットアップ
platform: 
  - Xamarin
  - iOS
  - Android
page_order: 0
description: "この記事では、Xamarinプラットフォーム用の初期iOS、Android、およびFireOS SDKセットアップについて説明します。"
search_rank: 1
---

# SDK の初期セットアップ

> このリファレンス記事では、Braze SDK for Xamarinのインストール方法について説明します。Braze SDK をインストールすると、基本的な分析機能と、ユーザーエンゲージメントのためのアプリ内メッセージが提供されます。 

## Android

### ステップ 1:Xamarin バインディングの取得

Xamarin バインディングは、Xamarin アプリでネイティブライブラリを使用する方法です。バインドの実装は、ライブラリへのC# インターフェイスを構築し、アプリケーションでそのインターフェイスを使用することで構成されます。 [Xamarin のドキュメント][2]を参照してください。

Braze SDK バインディングを含めるには2 つの方法があります。

#### オプション 1: ニューゲット

最も単純な統合方法では、[Nuget.org][9]中央リポジトリからBraze SDK を取得します。Visual Studio サイドバーで、`Packages` フォルダを右クリックし、`Add Packages...` をクリックします。 'Braze' を検索し、[`AppboyPlatform.AndroidBinding`][13] パッケージをプロジェクトにインストールします。

#### オプション 2: ソース

2 番目の統合方法は、[バインディングソース][3] を含めることです。`appboy-component\src\android` の下にバインディングソースコードがあります。Xamarin アプリケーションの```AppboyPlatform.XamarinAndroidBinding.csproj``` にプロジェクト参照を追加すると、バインディングがプロジェクトと共にビルドされ、Braze Android SDK にアクセスできるようになります。

>  Braze Nuget パッケージは、[`Xamarin.Android.Support.v4`][12] Nuget パッケージによって異なります。

### ステップ 2: braze.xml で Braze SDK を設定する
ライブラリが統合されたので、プロジェクトの`Resources/values` フォルダに`braze.xml` ファイルを作成する必要があります。ファイルの内容は、次のコードスニペットのようになります。

>  Braze ダッシュボードの**Settings** > **API Keys** にあるAPI キーで`REPLACE_WITH_YOUR_API_KEY` を必ず置き換えてください。

{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation)を使用している場合は、**Developer Console**> **API Settings**.にAPI キーがあります。
{% endalert %}

```java
    <?xml version="1.0" encoding="utf-8"?>
    <resources>
    <string name="com_braze_api_key">REPLACE_WITH_YOUR_API_KEY</string>
    <string translatable="false" name="com_braze_custom_endpoint">YOUR_CUSTOM_ENDPOINT_OR_CLUSTER</string>
    <string-array name="com_braze_internal_sdk_metadata">
      <item>XAMARIN</item>
      <item>NUGET</item>
    </string-array>
    </resources>
```
バインドソースを手動で含める場合は、`<item>NUGET</item>` をコードから削除します。

### ステップ 3: Android マニフェストに必要な権限を追加する
API キーを追加したので、次の権限を `AndroidManifest.xml` に追加する必要があります。

```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
```

### ステップ 4: ユーザーセッションの追跡とアプリ内メッセージの登録
ユーザーセッション追跡を有効にし、アプリ内メッセージ用にアプリを登録するには、アプリ内の`OnCreate()` クラスの`Application` ライフサイクルメソッドに次の呼び出しを追加します。

```csharp
RegisterActivityLifecycleCallbacks(new BrazeActivityLifecycleCallbackListener());
```

### SDK 統合の完了

これで、アプリケーションを起動し、セッションがBraze ダッシュボードに(デバイス情報やその他の分析とともに) ログ記録されていることを確認できるようになります。  

> 基本的なSDK 統合のベストプラクティスの詳細については、[Android 統合手順][8] を参照してください。

## iOS

{% alert important %}
Xamarin SDK バージョン4.0.0 以降のiOS バインディングでは、[Braze Swift SDK](https://github.com/braze-inc/braze-swift-sdk/) を使用しますが、以前のバージョンでは[legacy AppboyKit SDK](https://github.com/Appboy/Appboy-ios-sdk) を使用します。
{% endalert %}

### ステップ 1:Xamarin バインディングの取得

Xamarin バインディングは、Xamarin アプリでネイティブライブラリを使用する方法です。 バインドの実装は、C# インタフェースをライブラリに構築し、アプリケーションでそのインタフェースを使用することで構成されます。

Braze SDK バインディングを含めるには2 つの方法があります。

#### オプション 1: ニューゲット

最も単純な統合方法では、[Nuget.org][19]中央リポジトリからBraze SDK を取得します。Visual Studio サイドバーで、`Packages` フォルダを右クリックし、`Add Packages...` をクリックします。 'Braze' を検索し、[`AppboyPlatformXamariniOSBinding`][111] パッケージをプロジェクトにインストールします。

#### オプション 2: ソース

2 番目の統合方法は、[バインディングソース][113] を含めることです。[ our GitHub repository][17] にバインディングソースコードがあります。Xamarin アプリケーションの```AppboyPlatformXamariniOSBinding.csproj``` にプロジェクト参照を追加すると、バインディングがプロジェクトとともに構築され、Braze iOS SDK にアクセスできるようになります。プロジェクトの"Reference"フォルダに`AppboyPlatformXamariniOSBinding`が表示されていることを確認します。

### ステップ 2: アプリデリゲートを更新し、Xamarin の使用を宣言する

`AppDelegate.cs` ファイル内で、`FinishedLaunching` メソッド内に次のスニペットを追加します。

>  **Developer Console**ページの正しい値で`YOUR-API-KEY`を更新してください。

```csharp
// C#
 Appboy.StartWithApiKey ("YOUR-API-KEY", UIApplication.SharedApplication, options);
 Appboy.SharedInstance.SdkFlavor = ABKSDKFlavor.Xamarin;
 Appboy.SharedInstance.AddSdkMetadata(new []{ ABKSdkMetadata.ABKSdkMetadataXamarin, ABKSdkMetadata.ABKSdkMetadataNuGet });
```
バインドソースを手動で含める場合は、`ABKSdkMetadata.ABKSdkMetadataNuGet` をコードから削除します。

**実装例**

[TestApp.XamariniOS][110]サンプルアプリの`AppDelegate.cs`ファイルを参照してください。

### ステップ 3: SDK エンドポイントをinfo.plist ファイルに追加する

`Info.plist` ファイル内で、次のスニペットを追加します。

>  `YOUR-SDK-ENDPOINT` は必ず、Settings ページの正しい値で更新してください。

```csharp
// C#
<key>Braze</key>
<dict>
 <key>Endpoint</key>
 <string>YOUR-SDK-ENDPOINT</string>
</dict>
```

オプションで、次のスニペットを含めることで、詳細ロギングを含めることができます。

```csharp
// C#
<key>Braze</key>
<dict>
 <key>LogLevel</key>
 <string>0</string>
 <key>Endpoint</key>
 <string>YOUR-SDK-ENDPOINT</string>
</dict>
```

なお、Braze iOS SDK v4.0.2 より前のバージョンでは、`Braze` の代わりにディクショナリキー `Appboy` を使用する必要があります。

### SDK 統合の完了

これで、Braze はアプリケーションからデータを収集しており、基本的な統合は完了しているはずです。[カスタムイベントトラッキング]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/analytics/#tracking-custom-events)、[プッシュメッセージング]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/push_notifications/)、および Braze 機能の完全なスイートを有効にするには、次の記事を参照してください。

>  iOS SDK 用の現在のパブリックXamarin バインディングは、iOS Facebook SDK(ソーシャルデータをリンクする)には接続されず、Braze へのIDFA の送信は含まれません。

[2]: http://developer.xamarin.com/guides/android/advanced_topics/java_integration_overview/binding_a_java_library_%28.jar%29/
[3]: https://github.com/braze-inc/braze-xamarin-sdk
[8]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/
[9]: https://www.nuget.org/
[12]: https://www.nuget.org/packages/Xamarin.Android.Support.v4/
[13]: https://www.nuget.org/packages/AppboyPlatform.AndroidBinding/
[113]: https://github.com/braze-inc/braze-xamarin-sdk
[17]: https://github.com/braze-inc/braze-xamarin-sdk/tree/master/appboy-component/src/ios-unified
[19]: https://www.nuget.org/
[110]: https://github.com/braze-inc/braze-xamarin-sdk/tree/master/appboy-component/samples/ios-unified/TestApp.XamariniOS
[111]: https://www.nuget.org/packages/AppboyPlatformXamariniOSBinding/

