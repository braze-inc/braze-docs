---
nav_title: 初期SDKセットアップ
article_title: Windows Universal 用の初期SDK セットアップ
platform: Windows Universal
page_order: 0
description: "このリファレンス記事では、Windows Universal プラットフォームでBraze SDK を統合するための最初のSDK 統合手順について説明します。"
search_rank: 1
hidden: true
---

# 初期SDK統合
{% multi_lang_include archive/windows_deprecation.md %}

Braze SDK は、分析、セグメンテーション、エンゲージメントで使用される情報をレポートするためのAPI と、プッシュおよび受信のためのユーザ登録機能を提供します。

>  Windows Universal SDK は、Xamarin Windows Apps とも互換性があります。

## ステップ 3:NuGetパッケージマネージャを使用したSDKのインストール

Windows Universal SDK は、[NuGet Package Manager][14] 経由でインストールされます。NuGet を使用してBraze Windows SDK をインストールするには:

1. プロジェクトファイルを右クリックする
2. "Manage NuGet Packages&quotをクリックします。
3. 左側のドロップダウンメニューで、"Online"をクリックします
4. &quot で検索;NuGet.org" for "Appboy"
5. "AppboyPlatform.Universal.Release" NuGetパッケージをクリックし、インストールをクリックします

>  Windows Universal Library は、すべてのWindows 8.1、Windows Phone 8.1、およびUWP アプリケーションに使用する必要があります。

## ステップ 3:AppboyConfiguration.xmlの作成と設定

プロジェクトのルートディレクトリに`AppboyConfiguration.xml` というファイルを作成し、そのファイルに次のコードスニペットを追加します。

```xml
    <?xml version="1.0" encoding="utf-8"?>
    <AppboyConfig>
        <ApiKey>YOUR_API_KEY_HERE</ApiKey>
    </AppboyConfig>
```

>  [APIキー]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/)ページにあるAPIキーで`YOUR_API_KEY_HERE`を更新してください。

そのスニペットを追加したら、以下のファイルプロパティを変更してください `AppboyConfiguration.xml`

1. `Build Action` を `Content`
2. `Copy to Output Directory`が`Copy Always`に設定されました

## ステップ 3:package.appxmanifest の設定

"Capabilities タブで、`Internet (Client)` がチェックされていることを確認します。
![][18]

## ステップ 4: アプリクラスの編集

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

## 基本SDK統合完了

これで、Braze はアプリケーションからデータを収集するはずです。[attributes]({{site.baseurl}}/developer_guide/platform_integration_guides/windows_universal/analytics/setting_custom_attributes/)、[events]({{site.baseurl}}/developer_guide/platform_integration_guides/windows_universal/analytics/logging_custom_events)、および[purchases]({{site.baseurl}}/developer_guide/platform_integration_guides/windows_universal/analytics/logging_purchases)をSDKに記録し、プッシュメッセージを計測する方法については、次の記事を参照してください。

>  同じアプリでBraze Unity プロジェクトを使用している場合、Braze への呼び出しを"AppboyPlatform.Universal.Appboy&quot として完全修飾する必要がある場合があります。

[14]: http://www.nuget.org/
[18]: {% image_buster /assets/img_archive/internet_client.png %}
