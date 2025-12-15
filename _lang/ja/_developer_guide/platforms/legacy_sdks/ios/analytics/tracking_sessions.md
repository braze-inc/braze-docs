---
nav_title: セッションを追跡する
article_title: iOS のセッションを追跡する
platform: iOS
page_order: 0
description: "このリファレンス記事では、iOS アプリケーションのセッション最新情報を配信登録する方法を説明します。"

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# iOS のセッショントラッキング

Braze SDK では、ユーザーエンゲージメントなど、ユーザーについて理解するうえで不可欠な分析情報を計算するために Braze ダッシュボードで使用されるセッションデータがレポートされます。SDK では、以下のセッションセマンティクスに基づいて、Braze ダッシュボード内で表示可能なセッションの長さとセッション数を考慮した「セッション開始」と「セッション終了」のデータポイントが生成されます。

## セッションライフサイクル

`[[Appboy sharedInstance]` `startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions]` を呼び出すとセッションが開始されます。その後はデフォルトで、`UIApplicationWillEnterForegroundNotification` 通知が発行されると (アプリがフォアグラウンドに入ったときなど) セッションが開始され、アプリがフォアグラウンドを離れると (`UIApplicationDidEnterBackgroundNotification` 通知が発行されたときや、アプリが終了したときなど) セッションが終了します。

{% alert note %}
新しいセッションを強制する必要がある場合、ユーザーを変更することで強制が可能になります。
{% endalert %}

## セッションタイムアウトのカスタマイズ

Braze iOS SDK v3.14.1から、Info.plist ファイルを使用してセッションタイムアウトを設定できるようになった。`Braze` ディクショナリを `Info.plist` ファイルに追加します。`Braze` ディクショナリ内に `SessionTimeout` 番号サブエントリを追加し、値をカスタムセッションタイムアウトに設定します。なお、Braze iOS SDK v4.0.2 より前のバージョンでは、`Braze` の代わりにディクショナリキー `Appboy` を使用する必要があります。

または、[`startWithApiKey`](https://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#afd911d60dfe7e5361afbfb364f5d20f9) に渡される `appboyOptions` オブジェクト内の `ABKSessionTimeoutKey` キーを目的の整数値に設定することもできます。

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
// Sets the session timeout to 60 seconds
[Appboy startWithApiKey:@"YOUR-API_KEY"
          inApplication:application
      withLaunchOptions:options
      withAppboyOptions:@{ ABKSessionTimeoutKey : @(60) }];
```

{% endtab %}
{% tab swift %}

```swift
// Sets the session timeout to 60 seconds
Appboy.start(withApiKey: "YOUR-API-KEY",
                 in:application,
                 withLaunchOptions:launchOptions,
                 withAppboyOptions:[ ABKSessionTimeoutKey : 60 ])
```
{% endtab %}
{% endtabs %}

セッションタイムアウトを設定した場合、セッションセマンティクスの長さはすべてそのカスタマイズされたタイムアウトになります。

{% alert note %}
`sessionTimeoutInSeconds` の最小値は 1 秒です。デフォルト値は 10 秒です。
{% endalert %}

## セッショントラッキングをテストする

ユーザーを介してセッションを検出するには、ダッシュボードでユーザーを見つけ、ユーザープロファイルの [**アプリの利用状況**] に移動します。「セッション」指標が想定どおりに増加していることを確認することで、セッショントラッキングが機能していることを確認できます。

![ユーザープロファイルのアプリ使用セクションで、セッション数、最終使用日、初使用日が表示される。]({% image_buster /assets/img_archive/test_session.png %})

