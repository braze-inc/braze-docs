---
nav_title: SDK の初期セットアップ
article_title: ウィンドウズユニバーサル用の最初のSDK設定
platform: Windows Universal
page_order: 0
description: "このリファレンス記事では、Windows ユニバーサルプラットフォームにBraze SDKを統合するための最初のSDKインテグレーションステップについて説明します。"
search_rank: 1
hidden: true
---

# SDK の初期統合
{% multi_lang_include archive/windows_deprecation.md %}

Braze SDKは、分析、セグメンテーション、およびエンゲージメントで使用されるレポート情報へのAPI、および通知s のプッシュおよび受信のためのユーザーs の登録機能を提供します。

>  Windows ユニバーサルSDKは、Xamarin Windows アプリと互換性があります。

## ステップ 1:NuGet パッケージマネージャーを使用したSDKのインストール

Windows ユニバーサルSDKは、[NuGet Package Manager][14] を使用してインストールします。NuGet を使用してBraze Windows SDKをインストールするには:

1. プロジェクトファイルを右クリックする
2. "Manage NuGet Packages&quotをクリックします。
3. 左側のドロップダウンメニューで、"Online"をクリックします
4. &quot で検索;NuGet.org" " Appboy"
5. "AppboyPlatform.Universal.Release"NuGet Package をクリックし、Install をクリックします

>  Windows Universal Libraryは、Windows 8.1、Windows Phone 8.1、およびUWP アプリのすべてのアプリケーションで使用する必要があります。

## ステップ2:作成と設定 AppboyConfiguration.xml

プロジェクトのルートディレクトリに`AppboyConfiguration.xml` という名前のファイルを作成し、そのファイルに次のコード スニペットを追加します。

```xml
    <?xml version="1.0" encoding="utf-8"?>
    <AppboyConfig>
        <ApiKey>YOUR_API_KEY_HERE</ApiKey>
    </AppboyConfig>
```

>  [ API キー s]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/) ページにあるAPI キーで`YOUR_API_KEY_HERE` を必ず更新してください。

そのスニペットを追加したら、以下のファイルプロパティを変更してください `AppboyConfiguration.xml`

1. `Build Action` を `Content`
2. `Copy to Output Directory`を `Copy Always`

## ステップ 3:設定 package.appxmanifest

"Capabilities タブで、`Internet (Client)` がチェックされていることを確認します。
![][18]

## ステップ 4:アプリを編集する

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

## 基本SDK一体化完了

Braze はアプリライセンスからデータを収集するようになりました。[属性 s]({{site.baseurl}}/developer_guide/platform_integration_guides/windows_universal/analytics/setting_custom_attributes/)、[events]({{site.baseurl}}/developer_guide/platform_integration_guides/windows_universal/analytics/logging_custom_events)、および[purchases]({{site.baseurl}}/developer_guide/platform_integration_guides/windows_universal/analytics/logging_purchases)をSDKに記録し、プッシュメッセージングを計測する方法については、次の記事を参照してください。

>  同じアプリでBraze Unity プロジェクトを使用している場合は、Braze の呼び出しを"AppboyPlatform.Universal.Appboy" として完全修飾する必要がある場合があります。

[14]: http://www.nuget.org/
[18]: {% image_buster /assets/img_archive/internet_client.png %}
