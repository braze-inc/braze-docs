---
nav_title: カスタムイベントプロパティのロギング
article_title: カスタムイベントプロパティのロギング
page_order: 3
page_type: solution
description: "このヘルプ記事では、カスタムイベントが期待通りにログに記録されているかどうかを確認するための3つの重要なチェック方法について説明する。"
tool: 
- Campaigns
- Canvas
---

# カスタムイベントプロパティをロギングする

カスタムイベントが想定どおりにロギングされていることを確認するための重要なチェックが3つあります。

* [ロギングされるイベントを設定する](#verify-events)
* [ログを確認する](#verify-log)
* [値を確認する](#verify-values)

## カスタムイベントプロパティを確認する

[カスタムイベントプロパティー]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-properties) は、カスタムイベントs を記述するメタデータです。カスタムイベントがログに記録されるたびに、複数のプロパティーがログに記録されます。

### イベントを検証する

どのイベント・プロパティがトラッキングされているかを開発者に確認する。すべてのイベント・プロパティは大文字と小文字を区別することに留意してほしい。カスタム・イベントのトラッキングに関する追加情報については、プラットフォーム別に以下の記事を参照されたい：

* [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_custom_events/)
* [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/tracking_custom_events/)
* [Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/tracking_custom_events/)

### ログを確認する

イベント・プロパティが正常に追跡されていることを確認するには、**カスタム・イベント・**ページからすべてのイベント・プロパティを見ることができる。

1. [**データ設定**] > [**カスタムイベント**] に移動します。
2. リストからカスタムイベントを探す。
3. イベントの「**プロパティの管理**」をクリックする。これは、イベントに関連するプロパティの名前を表示する。

### 値を確認する

テストユーザーとしてユーザーを追加した後、以下の手順に従って値を検証する： 

1. アプリ内でカスタムイベントを実行する。
2. データがフラッシュされるまで約10秒待ちます。
3. [イベントユーザーログ]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab)を更新して、渡されたカスタムイベントとイベントプロパティの値を表示します。

それでもサポートが必要な場合は、[サポートチケットを]({{site.baseurl}}/braze_support/)を登録してください。

_最終更新日：2023年4月10日_

