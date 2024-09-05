---
nav_title: カスタムイベント・プロパティを記録する
article_title: カスタムイベント・プロパティを記録する
page_order: 3
page_type: solution
description: "このヘルプ記事では、カスタムイベントが期待通りにログに記録されているかどうかを確認するための3つの重要なチェック方法について説明する。"
tool: 
- Campaigns
- Canvas
---

# カスタムイベント・プロパティを記録する

カスタムイベントが期待通りに記録されているかどうかを確認するには、3つの重要なチェックがある：

* [どのイベントをログに記録するかを設定する](#verify-events)
* [ログを確認する](#verify-log)
* [数値を確認する](#verify-values)

## カスタムイベントプロパティを確認する

[カスタムイベント・プロパティは][22]、カスタムイベントを記述するメタデータである。カスタムイベントが記録されるたびに、複数のプロパティが記録される可能性がある。

### イベントを検証する

どのイベント・プロパティがトラッキングされているかを開発者に確認する。すべてのイベント・プロパティは大文字と小文字を区別することに留意してほしい。カスタム・イベントのトラッキングに関する追加情報については、プラットフォーム別に以下の記事を参照されたい：

* [Android][51]
* [iOS][23]
* [Web][52]

### ログを確認する

イベント・プロパティが正常に追跡されていることを確認するには、**カスタム・イベント・**ページからすべてのイベント・プロパティを見ることができる。

1. **データ設定**＞**カスタム**イベントに移動する。
2. リストからカスタムイベントを探す。
3. イベントの「**プロパティの管理**」をクリックする。これは、イベントに関連するプロパティの名前を表示する。

### 数値を確認する

テストユーザーとしてユーザーを追加した後、以下の手順に従って値を検証する： 

1. アプリ内でカスタムイベントを実行する。
2. データがフラッシュされるまでおよそ10秒待つ。
3. [イベント・ユーザー・ログを][24]リフレッシュして、カスタム・イベントと、それと一緒に渡されたイベント・プロパティ値を表示する。

まだ助けが必要か？[サポートチケットを]({{site.baseurl}}/braze_support/)開く。

_最終更新日：2023年4月10日_

[22]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-properties
[23]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/tracking_custom_events/
[24]: {{site.baseurl}}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab
[51]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_custom_events/ 
[52]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/tracking_custom_events/
