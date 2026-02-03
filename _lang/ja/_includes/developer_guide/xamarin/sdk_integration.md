## .NET MAUI SDKを統合する

Braze .NET MAUI（旧Xamarin）SDKを統合することで、基本的な分析機能だけでなく、ユーザーをエンゲージメントできるアプリ内メッセージも利用できるようになる。 

### 前提条件

.NET MAUI Braze SDKを統合する前に、以下の要件を満たしていることを確認すること：

- `version 3.0.0` 以降、この SDK では、NET 6以降を使用する必要があり、Xamarin フレームワークを使用するプロジェクトのサポートが削除されます。
- `version 4.0.0` 以降、このSDKはXamarin& Xamarin.Forms のサポートを停止し、.NET MAUIのサポートを追加した。Xamarinのサポート終了前後の[Microsoftのポリシー](https://dotnet.microsoft.com/en-us/platform/support/policy/xamarin)を参照してください。

### ステップ 1: .NET MAUIバインディングを取得する

{% tabs %}
{% tab android %}
.NET MAUIバインディングは、.NET MAUIアプリでネイティブ・ライブラリを使用する方法である。バインディングの実装は、ライブラリに対して C# インターフェイスを構築し、アプリケーションでそのインターフェイスを使用することから構成されます。 [.NET MAUIドキュメントを](http://developer.xamarin.com/guides/android/advanced_topics/java_integration_overview/binding_a_java_library_%28.jar%29/)参照のこと。Braze SDK バインディングを含めるには、NuGet を使用する方法と、ソースからコンパイルする方法の2つがあります。

{% subtabs local %}
{% subtab NuGet %}
最も単純な統合方式では、[NuGet.org](https://www.nuget.org/)中央リポジトリーからBraze SDKを取得します。Visual Studio サイドバーで、`Packages` フォルダを右クリックし、`Add Packages...` をクリックします。 'Braze' を検索し、[`BrazePlatform.BrazeAndroidBinding`](https://www.nuget.org/packages/BrazePlatform.BrazeAndroidBinding/) パッケージをプロジェクトにインストールします。
{% endsubtab %}

{% subtab Source %}
2 番目の統合方法は、[バインディングソース](https://github.com/braze-inc/braze-xamarin-sdk) を含めることです。その下に [`appboy-component/src/androidnet6`](https://github.com/braze-inc/braze-xamarin-sdk/tree/master/appboy-component/src/androidnet6/BrazeAndroidNet6Binding)あなたの.NET MAUIアプリケーションの```BrazeAndroidBinding.csproj``` にプロジェクト参照を追加すると、バインディングがあなたのプロジェクトと一緒にビルドされ、Braze Android SDKにアクセスできるようになる。
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab ios %}
{% alert important %}
.NET MAUI SDKバージョン4.0.0以降のiOSバインディングは[Braze Swift SDKを](https://github.com/braze-inc/braze-swift-sdk/)使用し、以前のバージョンは[従来のAppboyKit SDKを](https://github.com/Appboy/Appboy-ios-sdk)使用する。
{% endalert %}

.NET MAUIバインディングは、.NET MAUIアプリでネイティブ・ライブラリを使用する方法である。バインディングの実装は、ライブラリに対して C# インターフェイスを構築し、アプリケーションでそのインターフェイスを使用することから構成されます。Braze SDK バインディングを含めるには、NuGet を使用する方法と、ソースからコンパイルする方法の2つがあります。

{% subtabs local %}
{% subtab NuGet %}
最も単純な統合方式では、[NuGet.org](https://www.nuget.org/)中央リポジトリーからBraze SDKを取得します。Visual Studio サイドバーで、`Packages` フォルダを右クリックし、`Add Packages...` をクリックします。 Braze」を検索し、最新の.NET MAUI iOS NuGetパッケージをインストールする： [Braze.iOS.BrazeKit](https://www.nuget.org/packages/Braze.iOS.BrazeKit), [Braze.iOS.BrazeUI](https://www.nuget.org/packages/Braze.iOS.BrazeUI)そして [Braze.iOS.BrazeLocation](https://www.nuget.org/packages/Braze.iOS.BrazeLocation)をプロジェクトにインストールする。

.NET MAUI への移行を容易にするために、互換性ライブラリパッケージ [Braze.iOS.BrazeKitCompat](https://www.nuget.org/packages/Braze.iOS.BrazeKitCompat) および [Braze.iOS.BrazeUICompat](https://www.nuget.org/packages/Braze.iOS.BrazeUICompat) も提供しています。
{% endsubtab %}

{% subtab Source %}
2 番目の統合方法は、[バインディングソース](https://github.com/braze-inc/braze-xamarin-sdk) を含めることです。その下に [`appboy-component/src/iosnet6`](https://github.com/braze-inc/braze-xamarin-sdk/tree/master/appboy-component/src/iosnet6/BrazeiOSNet6Binding)あなたの.NET MAUIアプリケーションの```BrazeiOSBinding.csproj``` にプロジェクト参照を追加すると、バインディングがあなたのプロジェクトと一緒にビルドされ、Braze iOS SDKにアクセスできるようになる。プロジェクトの「リファレンス」フォルダに `BrazeiOSBinding.csproj` が表示されていることを確認します。
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### ステップ2:Brazeインスタンスの設定

{% tabs %}
{% tab android %}
#### ステップ 2.1: Braze.xmlでBraze SDKを構成する

ライブラリが統合されたので、プロジェクトの`Resources/values` フォルダに`Braze.xml` ファイルを作成する必要があります。ファイルの内容は、次のコードスニペットのようになります。

{% alert note %}
Braze ダッシュボードの**Settings**> **API キーs**にあるAPI キーで`YOUR_API_KEY`を必ず置き換えてください。
<br><br>
[古いナビゲーション]({{site.baseurl}}/user_guide/administrative/access_braze/navigation/) を使用している場合は、**デベロッパコンソール**> **API 設定**.にAPI キーがあります。
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
バインディングソースを手動で含める場合は、コードから `<item>NUGET</item>` を削除します。

{% alert tip %}
`Braze.xml` の例については、[Android MAUI サンプルアプリ](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/appboy-component/samples/android-net-maui/BrazeAndroidMauiSampleApp/BrazeAndroidMauiSampleApp/Resources/values/Braze.xml)を参照してください。
{% endalert %}

#### ステップ 2.2:Androidマニフェストに必要な権限を追加する

API キーを追加したので、次の権限を `AndroidManifest.xml` ファイルに追加する必要があります。

```xml
<uses-permission android:name="android.permission.INTERNET" />
```
`AndroidManifest.xml` の例については、[Android MAUI](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/appboy-component/samples/android-net-maui/BrazeAndroidMauiSampleApp/BrazeAndroidMauiSampleApp/AndroidManifest.xml) サンプルアプリケーションを参照してください。

#### ステップ 2.3:ユーザー セッションs の追跡とアプリ内メッセージs の登録

ユーザーセッショントラッキングを有効にし、アプリ内メッセージ用にアプリを登録するには、アプリの `Application` クラスの `OnCreate()` ライフサイクルメソッドに次の呼び出しを追加します。

```kotlin
RegisterActivityLifecycleCallbacks(new BrazeActivityLifecycleCallbackListener());
```
{% endtab %}

{% tab ios %}
Braze インスタンスを設定したら、次のスニペットを追加して、インスタンスを設定します。

{% alert note %}
Braze ダッシュボードの**Settings**> **API キーs**にあるAPI キーで`YOUR_API_KEY`を必ず置き換えてください。

[古いナビゲーション]({{site.baseurl}}/user_guide/administrative/access_braze/navigation/) を使用している場合は、**デベロッパコンソール**> **API 設定**.にAPI キーがあります。
{% endalert %}

```csharp
var configuration = new BRZConfiguration("YOUR_API_KEY", "YOUR_ENDPOINT");
configuration.Api.AddSDKMetadata(new[] { BRZSDKMetadata.Xamarin });
braze = new Braze(configuration);
```

[iOS MAUI](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/appboy-component/samples/ios-net-maui/BrazeiOSMauiSampleApp/BrazeiOSMauiSampleApp/App.xaml.cs)サンプルアプリライケーションの`App.xaml.cs`ファイルを参照してください。
{% endtab %}
{% endtabs %}

### ステップ3: 統合をテストする

{% tabs %}
{% tab android %}
これで、アプリケーションを起動して、セッションが Braze ダッシュボードに (デバイス情報やその他の分析と共に) 記録されているのを確認できます。基本的なSDKインテグレーションのベストプラクティスの詳細については、[Androidインテグレーション命令]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android)を参照してください。
{% endtab %}

{% tab ios %}
これで、アプリケーションを起動して、セッションが Braze ダッシュボードに記録されているのを確認できます。基本的なSDKインテグレーションのベストプラクティスの詳細については、[iOSインテグレーションの手順]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=swift)を参照してください。

{% alert important %}
私たちが現在公開しているiOS SDK用の.NET MAUIバインディングは、iOS Facebook SDK（ソーシャルデータのリンク）には接続できず、IDFAをBrazeに送信することも含まれていない。
{% endalert %}
{% endtab %}
{% endtabs %}
