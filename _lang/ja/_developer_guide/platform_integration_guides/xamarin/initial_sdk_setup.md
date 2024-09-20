---
nav_title: SDK の初期セットアップ
article_title: ザマリンの初回SDK設定
platform: 
  - Xamarin
  - iOS
  - Android
page_order: 0
toc_headers: h2
description: "ここでは、Xamarin プラットフォームの最初のiOS、Android、およびFireOS SDKの設定について説明します。"
search_rank: 1
---

# SDK の初期セットアップ

> ザマリンのBraze SDKをインストールする方法について説明します。Braze SDK をインストールすると、基本的な分析機能と、ユーザーs を操作できる作業アプリ内メッセージが提供されます。 

{% alert important %}
`version 3.0.0` 以降、このSDKでは。NET 6+ を使用する必要があり、Xamarin フレームワークを使用するプロジェクトのサポートが削除されます。
`version 4.0.0` 以降、このSDKはXamarin & Xamarin.Forms のサポートを削除し、。NET MAUI のサポートを追加しました。
Xamarinのサポート終了前後の[Microsoftのポリシー](https://dotnet.microsoft.com/en-us/platform/support/policy/xamarin)を参照してください。
{% endalert %}

## ステップ 1:Xamarin バインディングの取得

{% tabs %}
{% tab アンドロイド %}
Xamarin結合は、Xamarin アプリ sでネイティブライブラリを使用する方法です。バインドのインプリメンテーションは、C# インターフェイスをライブラリーに構築し、そのインターフェイスをアプリライセンスで使用することで構成されます。 [Xamarin ドキュメント](http://developer.xamarin.com/guides/android/advanced_topics/java_integration_overview/binding_a_java_library_%28.jar%29/)を参照してください。Braze SDKバインドを含めるには、NuGet を使用する方法とソースからコンパイルする方法の2 つがあります。

{% subtabs local %}
{% subtab NuGet %}
最も単純な統合方式では、[NuGet.org](https://www.nuget.org/)中央リポジトリーからBraze SDKを取得します。Visual Studio サイドバーで、`Packages` フォルダを右クリックし、`Add Packages...` をクリックします。 'Braze' を検索し、[`BrazePlatform.BrazeAndroidBinding`](https://www.nuget.org/packages/BrazePlatform.BrazeAndroidBinding/) パッケージをプロジェクトにインストールします。
{% endsubtab %}

{% subtab Source %}
2 番目の統合方法は、[バインディングソース](https://github.com/braze-inc/braze-xamarin-sdk) を含めることです。[`appboy-component/src/androidnet6`](https://github.com/braze-inc/braze-xamarin-sdk/tree/master/appboy-component/src/androidnet6/BrazeAndroidNet6Binding) にバインディングソースコードがあります。Xamarin アプリ ライケーションの```BrazeAndroidBinding.csproj``` にプロジェクトリファレンスを追加すると、バインディングがプロジェクトと共に構築され、Braze Android SDKにアクセスできるようになります。
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab イオス %}
{% alert important %}
Xamarin SDK バージョン4.0.0 以降のiOS バインディングでは、[ Braze Swift SDK](https://github.com/braze-inc/braze-swift-sdk/) が使用され、以前のバージョンでは[ レガシーAppboyKit SDK](https://github.com/Appboy/Appboy-ios-sdk) が使用されます。
{% endalert %}

Xamarin結合は、Xamarin アプリ sでネイティブライブラリを使用する方法です。 バインドのインプリメンテーションは、C# インターフェイスをライブラリーに構築し、そのインターフェイスをアプリライセンスで使用することで構成されます。Braze SDKバインドを含めるには、NuGet を使用する方法とソースからコンパイルする方法の2 つがあります。

{% subtabs local %}
{% subtab NuGet %}
最も単純な統合方式では、[NuGet.org](https://www.nuget.org/)中央リポジトリーからBraze SDKを取得します。Visual Studio サイドバーで、`Packages` フォルダを右クリックし、`Add Packages...` をクリックします。 「Braze」を検索し、最新のXamarin iOS パッケージをインストールします: [Braze.iOS.BrazeKit](https://www.nuget.org/packages/Braze.iOS.BrazeKit)、[Braze.iOS.BrazeUI](https://www.nuget.org/packages/Braze.iOS.BrazeUI)、\[Braze.iOS.BrazeLocation]https://www.nuget.org/packages/Braze.iOS.BrazeLocation

また、。NET MAUI への移行を容易にするために、互換性ライブラリパッケージ[Braze.iOS.BrazeKitCompat](https://www.nuget.org/packages/Braze.iOS.BrazeKitCompat) および[Braze.iOS.BrazeUICompat](https://www.nuget.org/packages/Braze.iOS.BrazeUICompat) も提供しています。
{% endsubtab %}

{% subtab Source %}
2 番目の統合方法は、[バインディングソース](https://github.com/braze-inc/braze-xamarin-sdk) を含めることです。[`appboy-component/src/iosnet6`](https://github.com/braze-inc/braze-xamarin-sdk/tree/master/appboy-component/src/iosnet6/BrazeiOSNet6Binding) では、バインディングソースコードが表示されます。Xamarin アプリライケーションの```BrazeiOSBinding.csproj``` にプロジェクトリファレンスを追加すると、バインディングがプロジェクトと共に構築され、Braze iOS SDKにアクセスできるようになります。プロジェクトの"Reference"フォルダに`BrazeiOSBinding.csproj`が表示されていることを確認します。
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## ステップ2:Brazeインスタンスの設定

{% tabs %}
{% tab アンドロイド %}
### ステップ 2.1:Braze SDKの設定 Braze.xml

ライブラリが統合されたので、プロジェクトの`Resources/values` フォルダに`Braze.xml` ファイルを作成する必要があります。そのファイルのコンテンツは、次のコードのスニペットに似ている必要があります。

{% alert note %}
Braze ダッシュボードの**Settings**> **API キーs**にあるAPI キーで`YOUR_API_KEY`を必ず置き換えてください。
<br><br>
[古いナビゲーション]({{site.baseurl}}/navigation) を使用している場合は、**デベロッパコンソール**> **API 設定**.にAPI キーがあります。
{% endalert %}

```xml
  <?xml version="1.0" encoding="utf-8"?>
  <resources>
    <string translatable="false" name="com_braze_api_key">YOUR_API_KEY</string>
    <string translatable="false" name="com_braze_custom_endpoint">YOUR_CUSTOM_ENDPOINT_OR_CLUSTER</string>
    <string-array name="com_braze_internal_sdk_metadata">
      <item>XAMARIN</item>
      <item>NUGET</item>
    </string-array>
  </resources>
```
バインドソースを手動で含める場合は、`<item>NUGET</item>` をコードから削除します。

{% alert tip %}
例`Braze.xml` を表示するには、[ Android MAUI サンプルアプリ](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/appboy-component/samples/android-net-maui/BrazeAndroidMauiSampleApp/BrazeAndroidMauiSampleApp/Resources/values/Braze.xml) を確認します。
{% endalert %}

### ステップ 2.2:Androidマニフェストに必要な権限を追加する

API キーを追加したので、`AndroidManifest.xml` に次の権限を追加する必要があります。

```xml
<uses-permission android:name="android.permission.INTERNET" />
```
`AndroidManifest.xml` のサンプルについては、[ Android MAUI](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/appboy-component/samples/android-net-maui/BrazeAndroidMauiSampleApp/BrazeAndroidMauiSampleApp/AndroidManifest.xml) サンプルアプリのライセンスを参照してください。

### ステップ 2.3:ユーザー セッションs の追跡とアプリ内メッセージs の登録

ユーザー セッション "トラッキング を有効にしてアプリをアプリ内メッセージ s に登録するには、アプリの`Application` クラスの`OnCreate()` ライフサイクルメソッドに次の呼び出しを追加します。

```kotlin
RegisterActivityLifecycleCallbacks(new BrazeActivityLifecycleCallbackListener());
```
{% endtab %}

{% tab イオス %}
Brazeインスタンスを設定したら、次のスニペットを追加して、インスタンスを設定します。

{% alert note %}
Braze ダッシュボードの**Settings**> **API キーs**にあるAPI キーで`YOUR_API_KEY`を必ず置き換えてください。

[古いナビゲーション]({{site.baseurl}}/navigation) を使用している場合は、**デベロッパコンソール**> **API 設定**.にAPI キーがあります。
{% endalert %}

```csharp
var configuration = new BRZConfiguration("YOUR_API_KEY", "YOUR_ENDPOINT");
configuration.Api.AddSDKMetadata(new[] { BRZSDKMetadata.Xamarin });
braze = new Braze(configuration);
```

[iOS MAUI](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/appboy-component/samples/ios-net-maui/BrazeiOSMauiSampleApp/BrazeiOSMauiSampleApp/App.xaml.cs)サンプルアプリライケーションの`App.xaml.cs`ファイルを参照してください。
{% endtab %}
{% endtabs %}

## ステップ 3:統合をテストする

{% tabs %}
{% tab アンドロイド %}
これで、アプリライセンスを起動し、セッションがBraze ダッシュボードに(機器情報や他の分析とともに)記録されていることを確認できます。基本的なSDKインテグレーションのベストプラクティスの詳細については、[Androidインテグレーション命令]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/)を参照してください。
{% endtab %}

{% tab イオス %}
これで、アプリライセンスを起動し、Braze ダッシュボードに記録されているセッションを確認できます。基本的なSDKインテグレーションのベストプラクティスの詳細については、[iOSインテグレーションの手順]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/overview/)を参照してください。

{% alert important %}
現行のiOS SDK向けのパブリックXamarinバインディングはiOS FaceBook SDK(ソーシャルデータのリンク)には接続されず、BrazeへのIDFAの送信は含まれていません。
{% endalert %}
{% endtab %}
{% endtabs %}
