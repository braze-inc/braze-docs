---
nav_title: カスタムイベントプロパティのロギング
article_title: カスタムイベントプロパティのロギング
page_order: 3
page_type: solution
description: "このヘルプ記事では、カスタムイベントが予期したとおりに記録されていることを確認するための3つの重要なチェックについて説明します。"
tool: 
- Campaigns
- Canvas
---

# カスタムイベントプロパティのロギング

カスタムイベントが予期したとおりに記録されていることを確認するために、以下の3 つの重要なチェックを実行します。

* [ログに記録されるイベントを設定する](#verify-events)
* [ログの検証](#verify-log)
* [値の確認](#verify-values)

## カスタムイベントプロパティの確認

[カスタムイベントプロパティ][22] は、カスタムイベントを説明するメタデータです。カスタムイベントがログに記録されるたびに、複数のプロパティがログに記録される場合があります。

### イベントの検証

どのイベントプロパティが追跡されているか、開発者に確認してください。すべてのイベントプロパティでは大文字と小文字が区別されることに注意してください。カスタムイベントの追跡の詳細については、プラットフォームに基づいて以下の記事をチェックしてください。

* [Android][51]
* [iOS][23]
* [Web][52]

### ログの検証

イベントプロパティが正常に追跡されたことを確認するには、**カスタムイベント** ページからすべてのイベントプロパティを表示できます。

1. **Data Settings** > **Custom Events**に移動します。
2. リストからカスタムイベントを見つけます。
3. イベントの場合は、**Manage Properties**をクリックします。これにより、イベントに関連付けられているプロパティの名前が表示されます。

### 値の確認

ユーザーをテストユーザーとして追加した後、次の手順に従って値を確認します。 

1. アプリ内でカスタムイベントを実行します。
2. データがフラッシュされるまで約10 秒お待ちください。
3. [Event User Log][24] を更新して、カスタムイベントとそれに渡されたイベントプロパティ値を表示します。

それでも助けが必要ですか?[サポートチケット]({{site.baseurl}}/braze_support/)を開きます。

_最終更新日2023年4月10日_

[22]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-properties
[23]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/tracking_custom_events/
[24]: {{site.baseurl}}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab
[51]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_custom_events/ 
[52]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/tracking_custom_events/
