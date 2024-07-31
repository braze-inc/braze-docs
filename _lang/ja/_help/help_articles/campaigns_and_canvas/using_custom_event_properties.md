---
nav_title: カスタムイベントプロパティの記録
article_title: カスタムイベントプロパティの記録
page_order: 3
page_type: solution
description: "このヘルプ記事では、カスタムイベントが期待通りに記録されていることを確認するための3つの重要なチェックについて説明します。"
tool: 
- Campaigns
- Canvas
---

# カスタムイベントプロパティの記録

カスタムイベントが期待通りに記録されていることを確認するために実施する重要なチェックが3つあります:

* [どのイベントが記録されるかを確立する](#verify-events)
* [ログを確認する](#verify-log)
* [値を確認する](#verify-values)

## カスタムイベントプロパティを確認する

[カスタムイベント][22]プロパティは、カスタムイベントを説明するメタデータです。カスタムイベントが記録されるたびに、複数のプロパティが記録される場合があります。

### イベントを確認する

どのイベントプロパティが追跡されているかを開発者に確認してください。すべてのイベントプロパティは大文字と小文字を区別することに注意してください。カスタムイベントのトラッキングに関する追加情報については、ご使用のプラットフォームに基づいたこれらの記事をご覧ください。

* [Android][51]
* [iOS][23]
* [Web][52]

### ログを確認する

イベントプロパティが正常に追跡されていることを確認するには、**カスタムイベント**ページからすべてのイベントプロパティを表示できます。

1. **データ設定** > **カスタムイベント** に移動します。
2. リストからカスタムイベントを見つけます。
3. イベントの場合は、**プロパティの管理**をクリックします。これにより、イベントに関連付けられたプロパティの名前が表示されます。

### 値を確認する

ユーザーをテストユーザーとして追加した後、次の手順に従って値を確認してください: 

1. アプリ内でカスタムイベントを実行します。
2. データがフラッシュされるのを約10秒待ちます。
3. [イベントユーザーログ][24]を更新して、カスタムイベントとそれに渡されたイベントプロパティ値を表示します。

まだ助けが必要ですか？[サポートチケット]({{site.baseurl}}/braze_support/)を開封する。

_最終更新日：2023年4月10日_

[22]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-properties
[23]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/tracking_custom_events/
[24]: {{site.baseurl}}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab
[51]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_custom_events/ 
[52]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/tracking_custom_events/
