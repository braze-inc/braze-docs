---
nav_title: SDK の初期セットアップ
article_title: Windowsユニバーサル用SDKの初期セットアップ
platform: Windows Universal
page_order: 0
description: "このリファレンス記事では、WindowsユニバーサルプラットフォームにBraze SDKを統合するための最初のSDK統合手順について説明する。"
search_rank: 1
hidden: true
---

# SDK の初期統合
{% multi_lang_include archive/windows_deprecation.md %}

Braze SDKは、アナリティクス、セグメンテーション、エンゲージメントに使用する情報をレポートするためのAPIを提供するほか、ユーザーをプッシュ登録し、通知を受け取る機能も提供する。

>  Windows Universal SDKは、Xamarin Windowsアプリとも互換性がある。

## ステップ 1:NuGetパッケージ・マネージャー経由でSDKをインストールする。

Windows Universal SDKは、[NuGetパッケージマネージャ][14]経由でインストールされる。NuGet経由でBraze Windows SDKをインストールする：

1. プロジェクトファイルを右クリックする
2. "Manage NuGet Packages "をクリックする。
3. 左のドロップダウンメニューから「オンライン」をクリックする。
4. NuGet.org" で "Appboy" を検索する。
5. AppboyPlatform.Universal.Release" NuGet Packageをクリックし、Installをクリックする。

>  Windowsユニバーサル・ライブラリは、すべてのWindows 8.1、Windows Phone 8.1、UWPアプリケーションに使用されるべきである。

## ステップ2:の作成と設定 AppboyConfiguration.xml

プロジェクトのルート・ディレクトリに`AppboyConfiguration.xml` というファイルを作成し、そのファイルに以下のコード・スニペットを追加する：

```xml
    <?xml version="1.0" encoding="utf-8"?>
    <AppboyConfig>
        <ApiKey>YOUR_API_KEY_HERE</ApiKey>
    </AppboyConfig>
```

>  [API]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/)キーのページで確認できるAPIキーで、`YOUR_API_KEY_HERE` 。

このスニペットを追加したら、以下のファイルのプロパティを変更してほしい。 `AppboyConfiguration.xml`

1. `Build Action` を設定する。 `Content`
2. `Copy to Output Directory` を設定する。 `Copy Always`

## ステップ 3:設定する package.appxmanifest

Capabilities "タブで、`Internet (Client)` がチェックされていることを確認する。
![][18]

## ステップ 4:アプリのクラスを編集する

- `App.xaml.cs` ファイルの`usings` に以下を追加する：

```csharp
using AppboyPlatform.PCL.Managers;
using AppboyPlatform.Universal;
using AppboyPlatform.Universal.Managers.PushArgs;
```

- `OnLaunched` ライフサイクルメソッド内で以下を呼び出す：

```csharp
Appboy.SharedInstance.OpenSession();
```

- `OnSuspending` ライフサイクルメソッド内で以下を呼び出す：

```csharp
Appboy.SharedInstance.CloseSession();
```

## SDKの基本的な統合が完了した

これでBrazeはアプリケーションからデータを収集するようになるはずだ。当社のSDKに[属性]({{site.baseurl}}/developer_guide/platform_integration_guides/windows_universal/analytics/setting_custom_attributes/)、[イベント]({{site.baseurl}}/developer_guide/platform_integration_guides/windows_universal/analytics/logging_custom_events)、[購入を]({{site.baseurl}}/developer_guide/platform_integration_guides/windows_universal/analytics/logging_purchases)記録する方法と、プッシュ・メッセージングを計測する方法については、以下の記事を参照のこと。

>  同じアプリでBraze Unityプロジェクトを使用している場合、Brazeへの呼び出しを"AppboyPlatform.Universal.Appboy"として完全に修飾する必要があるかもしれない。

[14]: http://www.nuget.org/
[18]: {% image_buster /assets/img_archive/internet_client.png %}
