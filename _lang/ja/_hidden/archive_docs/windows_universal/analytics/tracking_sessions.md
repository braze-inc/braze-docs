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

Braze SDK は、Braze ダッシュボードで使用されるセッションデータをレポートし、ユーザーエンゲージメントや、ユーザーを理解するために不可欠なその他の分析を計算します。以下のセッションセマンティクスに基づき、SDK は、Braze ダッシュボード内で表示可能なセッションの長さとセッション数を考慮した「セッション開始」と「セッション終了」のデータポイントを生成します。

### セッションライフサイクル

Windows 統合では、アプリが起動されるとセッションオープンが記録され、アプリケーションが閉じられるとセッションクローズが記録されます。`sessionTimeoutInSeconds` の最小値は 1 秒です。新しいセッションを強制する必要がある場合、ユーザーを変更することで強制が可能になります。

### セッショントラッキングをテストする

ユーザーを介してセッションを検出するには、ダッシュボードでユーザーを見つけ、ユーザープロファイルの [アプリの利用状況] に移動します。セッショントラッキングが機能していることを確認するには、「セッション」メトリクスが期待どおりに増加することを確認します。

![ユーザープロファイルには、アプリの利用状況が表示されており、25セッション、最後の使用が2時間前、初めての使用が20日前と表示されています。][session_tracking_7]

[session_tracking_1]: {{ site.baseurl }}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/overview#customizing-braze-on-startup
[session_tracking_3]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-2-configure-the-braze-sdk-in-appboyxml
[session_tracking_5]: https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize
[session_tracking_6]: http://msdn.microsoft.com/en-us/library/windows/apps/hh464925.aspx
[session_tracking_7]: {% image_buster /assets/img_archive/test_session.png %}
[session_tracking_8]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-4-tracking-user-sessions-in-android

