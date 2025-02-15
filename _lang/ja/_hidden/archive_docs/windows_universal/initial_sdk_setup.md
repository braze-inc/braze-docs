---
nav_title: SDK の初期セットアップ
article_title: Windows Universal 用の SDK 初期設定
platform: Windows Universal
page_order: 0
description: "このリファレンス記事では、Windows ユニバーサルプラットフォームにBraze SDKを統合するための最初のSDKインテグレーションステップについて説明します。"
search_rank: 1
hidden: true
---

# SDK の初期統合
{% multi_lang_include archive/windows_deprecation.md %}

Braze SDK は、分析、セグメンテーション、エンゲージメントで使用される情報をレポートするための API と、プッシュ通知と通知の受信用にユーザーを登録する機能を提供します。

>  Windows Universal SDK は、Xamarin Windows アプリとも互換性があります。

## ステップ1:NuGet パッケージマネージャーを使用したSDKのインストール

Windows ユニバーサルSDKは、[NuGet Package Manager][14] を使用してインストールします。NuGet を使用してBraze Windows SDKをインストールするには:

1. プロジェクトファイルを右クリックする
2. [Manage NuGet Packages (NuGet パッケージの管理)]をクリックします。
3. 左側のドロップダウンメニューで、[オンライン] をクリックします
4. 「NuGet.org」で「Appboy」を検索
5. [AppboyPlatform.Universal.Release] NuGet パッケージをクリックし、[インストール] をクリックします

>  Windows Universal ライブラリは、Windows 8.1、Windows Phone 8.1、および UWP のすべてのアプリケーションで使用する必要があります。

## ステップ2:AppboyConfiguration.xml の作成と設定

プロジェクトのルートディレクトリに`AppboyConfiguration.xml` という名前のファイルを作成し、そのファイルに次のコード スニペットを追加します。

```xml
    <?xml version="1.0" encoding="utf-8"?>
    <AppboyConfig>
        <ApiKey>YOUR_API_KEY_HERE</ApiKey>
    </AppboyConfig>
```

>  [[API キー]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/)] ページにある API キーで `YOUR_API_KEY_HERE` を更新してください。

そのスニペットを追加したら、以下の `AppboyConfiguration.xml` のファイルプロパティを変更してください。

1. `Build Action` を `Content` に設定します
2. `Copy to Output Directory` を `Copy Always` に設定します

## ステップ3:package.appxmanifest の設定

[機能] タブで、`Internet (Client)` がオンになっていることを確認します。
![][18]

## ステップ4:アプリクラスの編集

- `App.xaml.cs` ファイルの`usings` に以下を追加します。

```csharp
using AppboyPlatform.PCL.Managers;
using AppboyPlatform.Universal;
using AppboyPlatform.Universal.Managers.PushArgs;
```

- `OnLaunched` ライフサイクルメソッド内で以下を呼び出します。

```csharp
Appboy.SharedInstance.OpenSession();
```

- `OnSuspending` ライフサイクルメソッド内で以下を呼び出します。

```csharp
Appboy.SharedInstance.CloseSession();
```

## 基本的な SDK 統合の完了

これで Braze はアプリケーションからデータを収集するようになるはずです。[属性]({{site.baseurl}}/developer_guide/platform_integration_guides/windows_universal/analytics/setting_custom_attributes/)、[イベント]({{site.baseurl}}/developer_guide/platform_integration_guides/windows_universal/analytics/logging_custom_events)、および[購入]({{site.baseurl}}/developer_guide/platform_integration_guides/windows_universal/analytics/logging_purchases)を SDK に記録する方法と、プッシュメッセージングを実装する方法については、次の記事を参照してください。

>  同じアプリで Braze Unity プロジェクトを使用している場合は、Braze への呼び出しを「AppboyPlatform.Universal.Appboy」として完全修飾する必要があります。

[14]: http://www.nuget.org/
[18]: {% image_buster /assets/img_archive/internet_client.png %}
