---
nav_title: トラブルシューティング
article_title: Web のアプリケーション内メッセージのトラブルシューティング
platform: Web
page_order: 5
channel: in-app messages
description: "ここでは、インアプリ メッセージング配信またはディスプレイに関する一般的な問題のトラブルシューティングステップについて説明します。"

---

# トラブルシューティング

> ここでは、いくつかのWeb SDKなトラブルシューティングについて説明します。

## インプレッションが予想より低い

トリガはセッション起動時に機器と同期するまでに時間がかかります。これにより、セッションの起動直後にユーザーがイベントを記録したり、購入したりすると競合が発生する可能性があります。考えられる回避策の 1 つは、キャンペーンを変更してセッションの開始をトリガーし、目的のイベントまたは購入をセグメント化することです。なお、イベント発生後の次回セッション開始時にアプリ内メッセージが配信されることに注意してください。

## 予期したアプリ内メッセージが表示されなかった

ほとんどのアプリ内メッセージの問題は、配信と表示の 2 つの主要なカテゴリに分けることができます。予期したアプリ内メッセージがデバイスに表示されなかった理由をトラブルシューティングするには、まず\[アプリ内メッセージがデバイス]\[トラブルシューティング_iams_11]に配信されたことを確認し、次に\[トラブルシューティングメッセージディスプレイ]\[トラブルシューティング_iams_12]に配信されたことを確認します。

## アプリ内メッセージ配信 {#troubleshooting-in-app-message-delivery}

SDK はセッション開始時に Braze サーバーからアプリ内メッセージを要求します。アプリ内メッセージがデバイスに配信されているかどうかを確認するには、アプリ内メッセージが SDK によってリクエストされ、Braze サーバーによって返されていることを確認する必要があります。

### メッセージが要求され、返されたかどうかを確認する

1. ダッシュボードの\[テストユーザー]\[トラブルシューティング_iams_1]] として自分自身を追加します。
2. ユーザーを対象としたアプリ内メッセージキャンペーンを設定します。
3. アプリケーションで新しいセッションが発生することを確認します。
4. \[event ユーザー logs]\[troubleshooting_iams_3]を使用して、端末がセッション起動時にアプリ内メッセージを要求していることを確認します。テストユーザーのセッション開始イベントに関連付けられた SDK リクエストを見つけます。
  - トリガーされたアプリ内メッセージをリクエストするためのアプリであれば、\[**レスポンスデータ**] の \[**リクエスト済みレスポンス**] フィールドに `trigger` が表示されます。
  - アプリが元のアプリ内メッセージをリクエストするためのものだった場合、\[**レスポンスデータ］**] の \[**リクエスト済みレスポンス**] フィールドに `in_app` が表示されます。
5. \[event ユーザー logs]\[troubleshooting_iams_3]を使用して、レスポンスデータに正しいアプリ内メッセージsが返されているかどうかを確認します。<br>![]\[troubleshooting_iams_5]

### リクエストされていないメッセージのトラブルシューティング

アプリ内メッセージがリクエストされていない場合、アプリ内メッセージはセッション開始時にリフレッシュされるため、アプリがセッションを正しくトラッキングしていない可能性があります。また、アプリのセッションタイムアウトセマンティクスに基づいて、アプリが実際にセッションを開始していることを確認してください:

![イベントユーザーログで見つかったSDKリクエストは、成功したセッション起動イベントを表示します。]\[troubleshooting_iams_10]

### メッセージが返されない問題のトラブルシューティング

アプリ内メッセージが返されない場合、キャンペーンターゲティングの問題が発生している可能性があります。

- セグメントにユーザーが含まれていない。
  - ユーザーの\[\*\*Engagement**]\[トラブルシューティング_iams_6] タブで、**Segment s** で正しいSegment アプリが取得されているかどうかを確認します。
- ユーザーが以前にアプリ内メッセージを受け取ったことがあり、再度受け取る資格がなかった。
  - **キャンペーンコンポーザー**の**Delivery**ステップにある\[キャンペーン再適格性設定s]\[トラブルシューティング_iams_7]を確認し、再適格性設定がテスト設定に合っていることを確認します。
- ユーザーがキャンペーンのフリークエンシーキャップに達した。
  - キャンペーン \[frequency cap 設定 s]\[troubleshooting_iams_8]] を確認し、テスト設定と一致していることを確認します。
- キャンペーンにコントロールグループが存在した場合、ユーザーがコントロールグループに分類された可能性があります。
  - キャンペーンバリアントが \[**制御**] に設定されている受信キャンペーンバリアントフィルターでセグメントを作成し、ユーザーがそのセグメントに分類されたかどうかを確認することで、これが発生したかどうかを確認できます。
  - 統合テスト目的でキャンペーンを作成する場合は、コントロールグループの追加をオプトアウトしてください。

## アプリ内メッセージ表示 {#troubleshooting-in-app-message-display}

アプリがアプリ内メッセージのリクエストと受信に成功しているのに表示されない場合は、デバイス側のロジックによって表示が妨げられている可能性があります。

- トリガー ed アプリ内メッセージ s は、\[トリガー s]\[トラブルシューティング_iams_9]の最小間隔]に基づいてレート制限されます。これはs から30 秒デフォルトです。
- `braze.subscribeToInAppMessage`または`appboy.subscribeToNewInAppMessages`を使用してカスタムアプリ内メッセージ処理を行う場合は、サブスクリプションがアプリ内メッセージディスプレイに影響を与えないことを確認します。

\[troubleshooting_iams_1]: {{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#adding-test-users
\[troubleshooting_iams_2]: {{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab
\[troubleshooting_iams_3]: {{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab
\[troubleshooting_iams_4]: #session-tracking
\[troubleshooting_iams_5]:  {% image_buster /assets/img_archive/event_user_log_iams.png %}
\[troubleshooting_iams_6]: {{ site.baseurl }}/user_guide/engagement_tools/segments/using_user_search/#engagement-tab
\[troubleshooting_iams_7]: {{ site.baseurl }}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/
\[troubleshooting_iams_8]: {{ site.baseurl }}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping
\[troubleshooting_iams_9]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/in-app_messaging/in-app_message_delivery/#minimum-time-interval-between-triggers
\[troubleshooting_iams_10]: {% image_buster /assets/img_archive/event_user_log_session_start.png %}
\[troubleshooting_iams_11]: #troubleshooting-in-app-message-delivery
\[troubleshooting_iams_12]: #troubleshooting-in-app-message-display
