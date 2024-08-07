---
nav_title: セッションを追跡する
article_title: Windowsユニバーサルのセッションをトラッキングする
platform: Windows Universal
page_order: 0
description: "このリファレンス記事では、Windowsユニバーサルプラットフォームでセッションを追跡する方法について説明する。"
hidden: true
---

# 分析
{% multi_lang_include archive/windows_deprecation.md %}

## セッショントラッキング

Braze SDKは、Brazeダッシュボードで使用されるセッションデータを報告し、ユーザーエンゲージメントや、ユーザーを理解するために不可欠なその他の分析を計算します。以下のセッションセマンティクスに基づき、SDKは、Brazeダッシュボード内で表示可能なセッションの長さとセッション数を考慮した「セッション開始」と「セッション終了」のデータポイントを生成します。

### セッションライフサイクル

私たちのウィンドウズ統合ログ・セッションは、アプリが起動すると開き、アプリが終了すると閉じる。`sessionTimeoutInSeconds` の最小値は 1 秒です。新しいセッションを強制する必要がある場合、ユーザーを変更することで強制が可能になります。

### セッショントラッキングをテストする

ユーザー経由でセッションを検出するには、ダッシュボードでユーザーを見つけ、ユーザープロファイルの「App Usage」に移動する。セッション "メトリクスが期待通りに増加していることを確認することで、セッショントラッキングが機能していることを確認できる。

![アプリの利用が25セッション、最後に利用されたのが2時間前、最初に利用されたのが20日前であることを示すユーザープロファイル]\[session_tracking_7]

\[session_tracking_1] ： {{ site.baseurl }}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/overview#customizing-braze-on-startup
\[session_tracking_3] ： {{ site.baseurl }}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-2-configure-the-braze-sdk-in-appboyxml
\[session_tracking_5] ： https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize
\[session_tracking_6] ： http://msdn.microsoft.com/en-us/library/windows/apps/hh464925.aspx
\[session_tracking_7] ： {% image_buster /assets/img_archive/test_session.png %}
\[session_tracking_8] ： {{ site.baseurl }}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-4-tracking-user-sessions-in-android

