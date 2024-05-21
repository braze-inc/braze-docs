---
nav_title: トラブルシューティング
article_title: Web 向けアプリ内メッセージのトラブルシューティング
platform: Web
page_order: 5
channel: in-app messages
description: "このページには、アプリ内メッセージの配信または表示に関する一般的な問題に対するトラブルシューティング手順が記載されています。"

---

# トラブルシューティング

> この記事では、Web SDK のトラブルシューティング シナリオをいくつか紹介します。

## インプレッションが予想より低い

トリガーはセッション開始時にデバイスに同期するのに時間がかかります。そのため、ユーザーがセッション開始直後にイベントをログに記録したり購入したりすると、競合状態が発生する可能性があります。考えられる回避策の 1 つは、キャンペーンを変更してセッションの開始をトリガーし、目的のイベントまたは購入をセグメント化することです。なお、イベント発生後の次回セッション開始時にアプリ内メッセージが配信されることに注意してください。

## 予期したアプリ内メッセージが表示されなかった

ほとんどのアプリ内メッセージの問題は、配信と表示の 2 つの主要なカテゴリに分けることができます。予想されるアプリ内メッセージがデバイスで表示されない原因をトラブルシューティングするには、まず、[アプリ内メッセージがデバイスに配信された][troubleshooting\_iams\_11]ことを確認してから[メッセージ表示のトラブルシューティング][troubleshooting\_iams\_12]を行う必要があります。

## アプリ内メッセージ配信 {#troubleshooting-in-app-message-delivery}

SDK はセッション開始時に Braze サーバーからアプリ内メッセージを要求します。アプリ内メッセージがデバイスに配信されているかどうかを確認するには、アプリ内メッセージが SDK によってリクエストされ、Braze サーバーによって返されていることを確認する必要があります。

### メッセージが要求され、返されたかどうかを確認する

1. ダッシュボードで[テストユーザー][troubleshooting\_iams\_1]として自分自身を追加します。
2. ユーザーを対象としたアプリ内メッセージキャンペーンを設定します。
3. アプリケーションで新しいセッションが発生することを確認します。
4. [イベントユーザーログ][troubleshooting\_iams\_3]を使用して、セッション開始時にデバイスがアプリ内メッセージを要求していることを確認します。テストユーザーのセッション開始イベントに関連付けられた SDK リクエストを見つけます。
  - トリガーされたアプリ内メッセージをリクエストするためのアプリであれば、[**レスポンスデータ**] の [**リクエスト済みレスポンス**] フィールドに `trigger` が表示されます。
  - アプリが元のアプリ内メッセージをリクエストするためのものだった場合、[**レスポンスデータ］**] の [**リクエスト済みレスポンス**] フィールドに `in_app` が表示されます。
5. [イベントユーザーログ][troubleshooting\_iams\_3]を使用して、応答データで正しいアプリ内メッセージが返されるかどうかを確認します。<br>![][troubleshooting\_iams\_5]

### リクエストされていないメッセージのトラブルシューティング

アプリ内メッセージがリクエストされていない場合、アプリ内メッセージはセッション開始時にリフレッシュされるため、アプリがセッションを正しくトラッキングしていない可能性があります。また、アプリのセッションタイムアウトセマンティクスに基づいて、アプリが実際にセッションを開始していることを確認してください:

![成功したセッション開始イベントを表示するイベントユーザーログで見つかった SDK リクエスト。][troubleshooting\_iams\_10]

### メッセージが返されない問題のトラブルシューティング

アプリ内メッセージが返されない場合、キャンペーンターゲティングの問題が発生している可能性があります。

- セグメントにユーザーが含まれていない。
  - ユーザーの[\*\*エンゲージメント**][troubleshooting_iams_6]タブで、[**セグメント**] に正しいセグメントが表示されているかどうかを確認します。
- ユーザーが以前にアプリ内メッセージを受け取ったことがあり、再度受け取る資格がなかった。
  - **キャンペーン作成ツール**の**配信**ステップの[キャンペーン再適格性設定][troubleshooting\_iams\_7]を確認し、再適格性設定がテスト設定と整合していることを確認します。
- ユーザーがキャンペーンのフリークエンシーキャップに達した。
  - キャンペーン[フリークエンシーキャップ設定][troubleshooting\_iams\_8]を確認し、テスト設定と整合していることを確認します。
- キャンペーンにコントロールグループが存在した場合、ユーザーがコントロールグループに分類された可能性があります。
  - キャンペーンバリアントが [**制御**] に設定されている受信キャンペーンバリアントフィルターでセグメントを作成し、ユーザーがそのセグメントに分類されたかどうかを確認することで、これが発生したかどうかを確認できます。
  - 統合テスト目的でキャンペーンを作成する場合は、コントロールグループの追加をオプトアウトしてください。

## アプリ内メッセージ表示 {#troubleshooting-in-app-message-display}

アプリがアプリ内メッセージのリクエストと受信に成功しているのに表示されない場合は、デバイス側のロジックによって表示が妨げられている可能性があります。

- トリガーされたアプリ内メッセージは、[トリガー間の最小時間間隔][troubleshooting\_iams\_9] (デフォルトは30秒) に基づいてレート制限されます。
- アプリ内メッセージ処理をカスタマイズしている場合は、 `braze.subscribeToInAppMessage` または `appboy.subscribeToNewInAppMessages`サブスクリプションをチェックして、アプリ内メッセージの表示に影響がないことを確認してください。

[troubleshooting\_iams\_1]: {{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#adding-test-users
[troubleshooting\_iams\_2]: {{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab
[troubleshooting\_iams\_3]: {{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab
[troubleshooting\_iams\_4]: #session-tracking
[troubleshooting\_iams\_5]:  {% image_buster /assets/img_archive/event_user_log_iams.png %}
[troubleshooting\_iams\_6]: {{ site.baseurl }}/user_guide/engagement_tools/segments/using_user_search/#engagement-tab
[troubleshooting\_iams\_7]: {{ site.baseurl }}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/
[troubleshooting\_iams\_8]: {{ site.baseurl }}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping
[troubleshooting\_iams\_9]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/in-app_messaging/in-app_message_delivery/#minimum-time-interval-between-triggers
[troubleshooting\_iams\_10]: {% image_buster /assets/img_archive/event_user_log_session_start.png %}
[troubleshooting\_iams\_11]: #troubleshooting-in-app-message-delivery
[troubleshooting\_iams\_12]: #troubleshooting-in-app-message-display
