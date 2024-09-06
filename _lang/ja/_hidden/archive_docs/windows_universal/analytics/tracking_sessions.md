---
nav_title: セッションを追跡する
article_title: Windows Universal のセッションの追跡
platform: Windows Universal
page_order: 0
description: "このリファレンス記事では、Windows ユニバーサルプラットフォームでセッションを追跡する方法について説明します。"
hidden: true
---

# 分析
{% multi_lang_include archive/windows_deprecation.md %}

## セッショントラッキング

Braze SDK レポートは、次のセッションセマンティクスに基づいて、Braze ダッシュボードがユーザー エンゲージメントやユーザーを理解するために必要な他の分析を計算するために使用されるセッションを生成します。これにより、"start セッション"close セッション"Braze ダッシュボード内で表示可能なセッション長と分析数を考慮したデータポイントsがSDKで生成されます。

### セッションライフサイクル

当社のウィンドウズインテグレーションは、アプリが起動するとセッション 開封を記録し、アプリライセンスが終了するとセッションを記録します。`sessionTimeoutInSeconds` の最小値は 1 秒です。新しいセッションを強制する必要がある場合、ユーザーを変更することで強制が可能になります。

### セッショントラッキングをテストする

ユーザーでセッションs を検出するには、ダッシュボードでユーザーを見つけ、ユーザープロファイルで"App Usage" に移動します。セッション "トラッキングが機能していることを確認するには、" セッション s" メトリクスが期待どおりに増えることを確認します。

![アプリの使用量を25 セッション s として表示するユーザープロファイル。2 時間前に最後に使用され、最初に20 日前に使用された]\[セッション_"トラッキング_7]

\[セッション_"トラッキング_1]: {{ site.baseurl }}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/overview#customizing-braze-on-startup
\[セッション_"トラッキング_3]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-2-configure-the-braze-sdk-in-appboyxml
\[セッション_"トラッキング_5]: https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize
\[セッション_"トラッキング_6]: http://msdn.microsoft.com/en-us/library/windows/apps/hh464925.aspx
\[セッション_"トラッキング_7]: {% image_buster /assets/img_archive/test_session.png %}
\[セッション_"トラッキング_8]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-4-tracking-user-sessions-in-android

