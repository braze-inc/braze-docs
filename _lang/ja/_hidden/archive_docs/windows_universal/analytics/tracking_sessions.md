---
nav_title: セッションの追跡
article_title: Windows Universal のセッションの追跡
platform: Windows Universal
page_order: 0
description: "このリファレンス記事では、Windows Universal プラットフォームでセッションを追跡する方法について説明します。"
hidden: true
---

# 分析
{% multi_lang_include archive/windows_deprecation.md %}

## セッション追跡

Braze SDK は、ユーザーの理解に不可欠なユーザーエンゲージメントおよびその他の分析を計算するためにBraze ダッシュボードによって使用されるセッションデータをレポートします。次のセッションセマンティクスに基づいて、SDK は"start session"および"close session"セッションの長さとセッションカウントを考慮したデータポイントをBraze ダッシュボード内で表示可能にします。

### セッションライフサイクル

Windows 統合では、アプリが起動されるとセッションがログに記録され、アプリケーションが閉じられるとセッションが閉じます。`sessionTimeoutInSeconds`の最小値は1秒です。新しいセッションを強制する必要がある場合は、ユーザーを変更して実行できます。

### セッショントラッキングのテスト

ユーザー経由でセッションを検出するには、ダッシュボードでユーザーを検索し、ユーザープロファイルで"App Usage" に移動します。セッショントラッキングが機能していることを確認するには、"Sessions"メトリクスが期待どおりに増加することを確認します。

![アプリの使用状況を25 セッションとして表示するユーザープロファイル、最後に2 時間前に使用され、最初に20 日前に使用されたもの][session\_tracking\_7]

[session\_tracking\_1]: {{ site.baseurl }}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/overview#customizing-braze-on-startup
[session\_tracking\_3]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-2-configure-the-braze-sdk-in-appboyxml
[session\_tracking\_5]: https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize
[session\_tracking\_6]: http://msdn.microsoft.com/en-us/library/windows/apps/hh464925.aspx
[session\_tracking\_7]: {% image_buster /assets/img_archive/test_session.png %}
[session\_tracking\_8]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-4-tracking-user-sessions-in-android

