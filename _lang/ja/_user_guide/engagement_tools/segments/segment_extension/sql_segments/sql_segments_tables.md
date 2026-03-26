---
nav_title: "SQL テーブルリファレンス"
article_title: SQL テーブルリファレンス
page_order: 3
page_type: reference
toc_headers: h2
description: "このページは、クエリビルダ、SQL セグメントエクステンション、Snowflake データシェアリングで使用される Snowflake SQL テーブルと列のリファレンスです。"
tool: Segments
---

<style>
table td {
   word-break: keep-all;
}
</style>

# SQL テーブルリファレンス

このページは、以下の Braze ツールで利用可能な Snowflake SQL テーブルと列のリファレンスです。

- [クエリビルダ]({{site.baseurl}}/user_guide/analytics/query_builder/)
- [SQL セグメントエクステンション]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/)
- [Snowflake データシェアリング]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/)

ほとんどのテーブルは3つのツールすべてで利用できます。**Snowflake データシェアリング専用**と記載されたテーブルは Snowflake データシェアリングでのみ利用可能であり、クエリビルダや SQL セグメントエクステンションではアクセスできません。

{% alert tip %}
これらの SQL テーブルは、[Currents イベント用語集]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/)に記載されているイベントに対応しています。たとえば、SQL テーブル `USERS_MESSAGES_EMAIL_SEND_SHARED` は Currents イベント `users.messages.email.Send` に対応しています。JSON イベントスキーマやパートナー固有のフォーマット (Amplitude、Mixpanel、Segment) が必要な場合は、Currents 用語集を参照してください。
{% endalert %}

## 目次

テーブル | 説明
------|------------
[AGENTCONSOLE_AGENTEXECUTED_SHARED](#AGENTCONSOLE_AGENTEXECUTED_SHARED) | Agent Console エージェントが実行されたとき（**Snowflake Data Sharing のみ**）
[AGENTCONSOLE_TOOLINVOCATION_SHARED](#AGENTCONSOLE_TOOLINVOCATION_SHARED) | ツールが実行されたとき（**Snowflake Data Sharing のみ**）
[CATALOGS_ITEMS_SHARED](#CATALOGS_ITEMS_SHARED) | 削除されていないカタログアイテム
[CHANGELOGS_CAMPAIGN_SHARED](#CHANGELOGS_CAMPAIGN_SHARED) | キャンペーンが変更されたとき（**Snowflake Data Sharing のみ**）
[CHANGELOGS_CANVAS_SHARED](#CHANGELOGS_CANVAS_SHARED) | Canvas が変更されたとき（**Snowflake Data Sharing のみ**）
[CHANGELOGS_GLOBALCONTROLGROUP_SHARED](#CHANGELOGS_GLOBALCONTROLGROUP_SHARED) | グローバルコントロールグループが変更されたとき
[USERS_BEHAVIORS_CUSTOMEVENT_SHARED](#USERS_BEHAVIORS_CUSTOMEVENT_SHARED) | ユーザーがカスタムイベントを実行したとき
[USERS_BEHAVIORS_INSTALLATTRIBUTION_SHARED](#USERS_BEHAVIORS_INSTALLATTRIBUTION_SHARED) | ユーザーがアプリをインストールし、パートナーにアトリビューションされたとき
[USERS_BEHAVIORS_LOCATION_SHARED](#USERS_BEHAVIORS_LOCATION_SHARED) | ユーザーがロケーションを記録したとき
[USERS_BEHAVIORS_PURCHASE_SHARED](#USERS_BEHAVIORS_PURCHASE_SHARED) | ユーザーが購入を行ったとき
[USERS_BEHAVIORS_UNINSTALL_SHARED](#USERS_BEHAVIORS_UNINSTALL_SHARED) | ユーザーがアプリをアンインストールしたとき
[USERS_BEHAVIORS_UPGRADEDAPP_SHARED](#USERS_BEHAVIORS_UPGRADEDAPP_SHARED) | ユーザーがアプリをアップグレードしたとき
[USERS_BEHAVIORS_APP_FIRSTSESSION_SHARED](#USERS_BEHAVIORS_APP_FIRSTSESSION_SHARED) | ユーザーが初回セッションを行ったとき
[USERS_BEHAVIORS_APP_NEWSFEEDIMPRESSION_SHARED](#USERS_BEHAVIORS_APP_NEWSFEEDIMPRESSION_SHARED) | ユーザーが News Feed を閲覧したとき
[USERS_BEHAVIORS_APP_SESSIONEND_SHARED](#USERS_BEHAVIORS_APP_SESSIONEND_SHARED) | ユーザーがアプリでセッションを終了したとき
[USERS_BEHAVIORS_APP_SESSIONSTART_SHARED](#USERS_BEHAVIORS_APP_SESSIONSTART_SHARED) | ユーザーがアプリでセッションを開始したとき
[USERS_BEHAVIORS_GEOFENCE_DATAEVENT_SHARED](#USERS_BEHAVIORS_GEOFENCE_DATAEVENT_SHARED) | ユーザーがジオフェンスエリアをトリガーしたとき（例: ジオフェンスに入った、または出たとき）。このイベントは他のイベントとバッチ処理され、標準イベントエンドポイント経由で受信されたため、リアルタイムで受信されていない場合があります。
[USERS_BEHAVIORS_GEOFENCE_RECORDEVENT_SHARED](#USERS_BEHAVIORS_GEOFENCE_RECORDEVENT_SHARED) | ユーザーがジオフェンスエリアをトリガーしたとき（例: ジオフェンスに入った、または出たとき）。このイベントは専用のジオフェンスエンドポイント経由で受信されるため、ユーザーのデバイスがジオフェンスのトリガーを検出するとすぐにリアルタイムで受信されます。<br><br>また、ジオフェンスエンドポイントのレート制限により、一部のジオフェンスイベントが RecordEvent として反映されない場合があります。ただし、すべてのジオフェンスイベントは DataEvent として表現されます（バッチ処理による遅延が発生する可能性があります）。
[USERS_BEHAVIORS_LIVEACTIVITY_PUSHTOSTARTTOKENCHANGE_SHARED](#USERS_BEHAVIORS_LIVEACTIVITY_PUSHTOSTARTTOKENCHANGE_SHARED) | Live Activity の push-to-start トークンが変更されたとき
[USERS_BEHAVIORS_LIVEACTIVITY_UPDATETOKENCHANGE_SHARED](#USERS_BEHAVIORS_LIVEACTIVITY_UPDATETOKENCHANGE_SHARED) | Live Activity の更新トークンが変更されたとき
[USERS_BEHAVIORS_PUSHNOTIFICATION_TOKENSTATECHANGE_SHARED](#USERS_BEHAVIORS_PUSHNOTIFICATION_TOKENSTATECHANGE_SHARED) | プッシュ通知トークンの状態が変更されたとき
[USERS_BEHAVIORS_SUBSCRIPTION_GLOBALSTATECHANGE_SHARED](#USERS_BEHAVIORS_SUBSCRIPTION_GLOBALSTATECHANGE_SHARED) | ユーザーがメールなどのチャネルでグローバルに購読または配信停止されたとき
[USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED](#USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED) | ユーザーがサブスクリプショングループに購読または配信停止されたとき
[USERS_CAMPAIGNS_CONVERSION_SHARED](#USERS_CAMPAIGNS_CONVERSION_SHARED) | ユーザーがキャンペーンでコンバージョンしたとき
[USERS_CAMPAIGNS_ENROLLINCONTROL_SHARED](#USERS_CAMPAIGNS_ENROLLINCONTROL_SHARED) | ユーザーがキャンペーンのコントロールグループに登録されたとき
[USERS_CAMPAIGNS_FREQUENCYCAP_SHARED](#USERS_CAMPAIGNS_FREQUENCYCAP_SHARED) | ユーザーがキャンペーンでフリークエンシーキャップに達したとき
[USERS_CAMPAIGNS_REVENUE_SHARED](#USERS_CAMPAIGNS_REVENUE_SHARED) | ユーザーが1次コンバージョン期間内に収益を生成したとき
[USERS_CANVASSTEP_PROGRESSION_SHARED](#USERS_CANVASSTEP_PROGRESSION_SHARED) | ユーザーがキャンバスステップに進んだとき
[USERS_CANVAS_CONVERSION_SHARED](#USERS_CANVAS_CONVERSION_SHARED) | ユーザーが Canvas のコンバージョンイベントでコンバージョンしたとき
[USERS_CANVAS_ENTRY_SHARED](#USERS_CANVAS_ENTRY_SHARED) | ユーザーが Canvas に入ったとき
[USERS_CANVAS_EXIT_MATCHEDAUDIENCE_SHARED](#USERS_CANVAS_EXIT_MATCHEDAUDIENCE_SHARED) | ユーザーがオーディエンス離脱条件に一致して Canvas を離脱したとき
[USERS_CANVAS_EXIT_PERFORMEDEVENT_SHARED](#USERS_CANVAS_EXIT_PERFORMEDEVENT_SHARED) | ユーザーが例外イベントを実行して Canvas を離脱したとき
[USERS_CANVAS_EXPERIMENTSTEP_CONVERSION_SHARED](#USERS_CANVAS_EXPERIMENTSTEP_CONVERSION_SHARED) | ユーザーが Canvas の実験ステップでコンバージョンしたとき
[USERS_CANVAS_EXPERIMENTSTEP_SPLITENTRY_SHARED](#USERS_CANVAS_EXPERIMENTSTEP_SPLITENTRY_SHARED) | ユーザーが実験ステップのパスに入ったとき
[USERS_CANVAS_FREQUENCYCAP_SHARED](#USERS_CANVAS_FREQUENCYCAP_SHARED) | ユーザーがキャンバスステップでフリークエンシーキャップに達したとき
[USERS_CANVAS_REVENUE_SHARED](#USERS_CANVAS_REVENUE_SHARED) | ユーザーが1次コンバージョンイベント期間内に収益を生成したとき
[USERS_MESSAGES_BANNER_ABORT_SHARED](#USERS_MESSAGES_BANNER_ABORT_SHARED) | 元々スケジュールされたバナーメッセージが何らかの理由で中止されたとき
[USERS_MESSAGES_BANNER_CLICK_SHARED](#USERS_MESSAGES_BANNER_CLICK_SHARED) | ユーザーがバナーをクリックしたとき
[USERS_MESSAGES_BANNER_IMPRESSION_SHARED](#USERS_MESSAGES_BANNER_IMPRESSION_SHARED) | ユーザーがバナーを閲覧したとき
[USERS_MESSAGES_CONTENTCARD_ABORT_SHARED](#USERS_MESSAGES_CONTENTCARD_ABORT_SHARED) | 元々スケジュールされたコンテンツカードメッセージが何らかの理由で中止されたとき
[USERS_MESSAGES_CONTENTCARD_CLICK_SHARED](#USERS_MESSAGES_CONTENTCARD_CLICK_SHARED) | ユーザーがコンテンツカードをクリックしたとき
[USERS_MESSAGES_CONTENTCARD_DISMISS_SHARED](#USERS_MESSAGES_CONTENTCARD_DISMISS_SHARED) | ユーザーがコンテンツカードを閉じたとき
[USERS_MESSAGES_CONTENTCARD_IMPRESSION_SHARED](#USERS_MESSAGES_CONTENTCARD_IMPRESSION_SHARED) | ユーザーがコンテンツカードを閲覧したとき
[USERS_MESSAGES_CONTENTCARD_SEND_SHARED](#USERS_MESSAGES_CONTENTCARD_SEND_SHARED) | ユーザーにコンテンツカードを送信したとき
[USERS_MESSAGES_EMAIL_ABORT_SHARED](#USERS_MESSAGES_EMAIL_ABORT_SHARED) | 元々スケジュールされたメールメッセージが何らかの理由で中止されたとき
[USERS_MESSAGES_EMAIL_BOUNCE_SHARED](#USERS_MESSAGES_EMAIL_BOUNCE_SHARED) | メールサービスプロバイダー (ESP) がハードバウンスを返したとき。ハードバウンスは永続的な配信失敗を示します。
[USERS_MESSAGES_EMAIL_CLICK_SHARED](#USERS_MESSAGES_EMAIL_CLICK_SHARED) | ユーザーがメール内のリンクをクリックしたとき
[USERS_MESSAGES_EMAIL_DEFERRAL_SHARED](#USERS_MESSAGES_EMAIL_DEFERRAL_SHARED) | メールが遅延されたとき
[USERS_MESSAGES_EMAIL_DELIVERY_SHARED](#USERS_MESSAGES_EMAIL_DELIVERY_SHARED) | メールが配信されたとき
[USERS_MESSAGES_EMAIL_MARKASSPAM_SHARED](#USERS_MESSAGES_EMAIL_MARKASSPAM_SHARED) | メールがスパムとしてマークされたとき
[USERS_MESSAGES_EMAIL_OPEN_SHARED](#USERS_MESSAGES_EMAIL_OPEN_SHARED) | ユーザーがメールを開封したとき
[USERS_MESSAGES_EMAIL_SEND_SHARED](#USERS_MESSAGES_EMAIL_SEND_SHARED) | ユーザーにメールを送信したとき
[USERS_MESSAGES_EMAIL_SOFTBOUNCE_SHARED](#USERS_MESSAGES_EMAIL_SOFTBOUNCE_SHARED) | メールがソフトバウンスしたとき
[USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED](#USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED) | ユーザーがメールを配信停止したとき
[USERS_MESSAGES_EMAIL_RETRY_SHARED](#USERS_MESSAGES_EMAIL_RETRY_SHARED) | メールメッセージが優先度の引き下げまたはフリークエンシーキャップ後にリトライされたとき（**Snowflake Data Sharing のみ**）
[USERS_MESSAGES_FEATUREFLAG_IMPRESSION_SHARED](#USERS_MESSAGES_FEATUREFLAG_IMPRESSION_SHARED) | ユーザーがフィーチャーフラグを閲覧したとき
[USERS_MESSAGES_INAPPMESSAGE_ABORT_SHARED](#USERS_MESSAGES_INAPPMESSAGE_ABORT_SHARED) | 元々スケジュールされたアプリ内メッセージが何らかの理由で中止されたとき
[USERS_MESSAGES_INAPPMESSAGE_CLICK_SHARED](#USERS_MESSAGES_INAPPMESSAGE_CLICK_SHARED) | ユーザーがアプリ内メッセージをクリックしたとき
[USERS_MESSAGES_INAPPMESSAGE_IMPRESSION_SHARED](#USERS_MESSAGES_INAPPMESSAGE_IMPRESSION_SHARED) | ユーザーがアプリ内メッセージを閲覧したとき
[USERS_MESSAGES_LINE_ABORT_SHARED](#USERS_MESSAGES_LINE_ABORT_SHARED) | スケジュールされた LINE メッセージが LINE への送信前に配信できなかったとき
[USERS_MESSAGES_LINE_CLICK_SHARED](#USERS_MESSAGES_LINE_CLICK_SHARED) | ユーザーが LINE メッセージ内のリンクをクリックしたとき
[USERS_MESSAGES_LINE_INBOUNDRECEIVE_SHARED](#USERS_MESSAGES_LINE_INBOUNDRECEIVE_SHARED) | ユーザーから LINE メッセージを受信したとき
[USERS_MESSAGES_LINE_SEND_SHARED](#USERS_MESSAGES_LINE_SEND_SHARED) | LINE メッセージが LINE に送信されたとき
[USERS_MESSAGES_LINE_RETRY_SHARED](#USERS_MESSAGES_LINE_RETRY_SHARED) | LINE メッセージが優先度の引き下げまたはフリークエンシーキャップ後にリトライされたとき（**Snowflake Data Sharing のみ**）
[USERS_MESSAGES_LIVEACTIVITY_OUTCOME_SHARED](#USERS_MESSAGES_LIVEACTIVITY_OUTCOME_SHARED) | Live Activity にアウトカムイベントが発生したとき
[USERS_MESSAGES_LIVEACTIVITY_SEND_SHARED](#USERS_MESSAGES_LIVEACTIVITY_SEND_SHARED) | Live Activity メッセージが送信されたとき
[USERS_MESSAGES_NEWSFEEDCARD_ABORT_SHARED](#USERS_MESSAGES_NEWSFEEDCARD_ABORT_SHARED) | 元々スケジュールされた News Feed カードメッセージが何らかの理由で中止されたとき
[USERS_MESSAGES_NEWSFEEDCARD_CLICK_SHARED](#USERS_MESSAGES_NEWSFEEDCARD_CLICK_SHARED) | ユーザーが News Feed カードをクリックしたとき
[USERS_MESSAGES_NEWSFEEDCARD_IMPRESSION_SHARED](#USERS_MESSAGES_NEWSFEEDCARD_IMPRESSION_SHARED) | ユーザーが News Feed カードを閲覧したとき
[USERS_MESSAGES_PUSHNOTIFICATION_ABORT_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_ABORT_SHARED) | 元々スケジュールされたプッシュ通知メッセージが何らかの理由で中止されたとき
[USERS_MESSAGES_PUSHNOTIFICATION_BOUNCE_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_BOUNCE_SHARED) | プッシュ通知がバウンスしたとき
[USERS_MESSAGES_PUSHNOTIFICATION_INFLUENCEDOPEN_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_INFLUENCEDOPEN_SHARED) | ユーザーが通知を受信した後、通知をクリックせずにアプリを開いたとき
[USERS_MESSAGES_PUSHNOTIFICATION_IOSFOREGROUND_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_IOSFOREGROUND_SHARED) | アプリが開いている状態でユーザーがプッシュ通知を受信したとき。<br><br>このイベントは [Swift SDK](https://github.com/braze-inc/braze-swift-sdk) ではサポートされておらず、[Obj-C SDK](https://github.com/Appboy/appboy-ios-sdk) では非推奨です。
[USERS_MESSAGES_PUSHNOTIFICATION_OPEN_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_OPEN_SHARED) | ユーザーがプッシュ通知を開いた、またはプッシュ通知ボタン（アプリを開かない「閉じる」ボタンを含む）をクリックしたとき。<br><br>プッシュボタンアクションには複数の結果があります。「いいえ」、「拒否」、「キャンセル」のアクションは「クリック」であり、「承認」のアクションは「開封」です。両方ともこのテーブルに表示されますが、**BUTTON_ACTION_TYPE** 列で区別できます。例えば、「いいえ」、「拒否」、「キャンセル」以外の `BUTTON_ACTION_TYPE` でグループ化するクエリを使用できます。
[USERS_MESSAGES_PUSHNOTIFICATION_SEND_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_SEND_SHARED) | ユーザーにプッシュ通知を送信したとき
[USERS_MESSAGES_RCS_ABORT_SHARED](#USERS_MESSAGES_RCS_ABORT_SHARED) | Braze 内でエラーが検出されて RCS 送信が中断され、メッセージが破棄されたとき
[USERS_MESSAGES_RCS_CLICK_SHARED](#USERS_MESSAGES_RCS_CLICK_SHARED) | エンドユーザーが RCS メッセージの UI 要素をタップまたはクリックして操作したとき
[USERS_MESSAGES_RCS_DELIVERY_SHARED](#USERS_MESSAGES_RCS_DELIVERY_SHARED) | RCS メッセージがエンドユーザーのモバイルデバイスに正常に配信されたとき
[USERS_MESSAGES_RCS_INBOUNDRECEIVE_SHARED](#USERS_MESSAGES_RCS_INBOUNDRECEIVE_SHARED) | Braze がエンドユーザーからの RCS メッセージを受信したとき
[USERS_MESSAGES_RCS_READ_SHARED](#USERS_MESSAGES_RCS_READ_SHARED) | エンドユーザーがデバイスで RCS メッセージを開いたとき
[USERS_MESSAGES_RCS_REJECTION_SHARED](#USERS_MESSAGES_RCS_REJECTION_SHARED) | キャリアの介入により RCS メッセージの配信に失敗したとき
[USERS_MESSAGES_RCS_SEND_SHARED](#USERS_MESSAGES_RCS_SEND_SHARED) | RCS メッセージが Braze のシステムからラストマイル配信パートナーに送信されたとき
[USERS_MESSAGES_SMS_ABORT_SHARED](#USERS_MESSAGES_SMS_ABORT_SHARED) | 元々スケジュールされた SMS メッセージが何らかの理由で中止されたとき
[USERS_MESSAGES_SMS_CARRIERSEND_SHARED](#USERS_MESSAGES_SMS_CARRIERSEND_SHARED) | SMS メッセージがキャリアに送信されたとき
[USERS_MESSAGES_SMS_DELIVERY_SHARED](#USERS_MESSAGES_SMS_DELIVERY_SHARED) | SMS メッセージが配信されたとき
[USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED](#USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED) | Braze が SMS メッセージを SMS サービスプロバイダーに配信できなかったとき
[USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED](#USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED) | ユーザーから SMS メッセージを受信したとき
[USERS_MESSAGES_SMS_REJECTION_SHARED](#USERS_MESSAGES_SMS_REJECTION_SHARED) | SMS メッセージがユーザーに配信されなかったとき
[USERS_MESSAGES_SMS_SEND_SHARED](#USERS_MESSAGES_SMS_SEND_SHARED) | SMS メッセージが送信されたとき
[USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED](#USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED) | ユーザーが SMS メッセージに含まれる Braze 短縮 URL をクリックしたとき
[USERS_MESSAGES_SMS_RETRY_SHARED](#USERS_MESSAGES_SMS_RETRY_SHARED) | SMS メッセージが優先度の引き下げまたはフリークエンシーキャップ後にリトライされたとき（**Snowflake Data Sharing のみ**）
[USERS_MESSAGES_WEBHOOK_ABORT_SHARED](#USERS_MESSAGES_WEBHOOK_ABORT_SHARED) | 元々スケジュールされた Webhook メッセージが何らかの理由で中止されたとき
[USERS_MESSAGES_WEBHOOK_FAILURE_SHARED](#USERS_MESSAGES_WEBHOOK_FAILURE_SHARED) | Webhook メッセージが配信されたが、エンドポイントからエラーレスポンスが返されたとき
[USERS_MESSAGES_WEBHOOK_SEND_SHARED](#USERS_MESSAGES_WEBHOOK_SEND_SHARED) | ユーザーに Webhook を送信したとき
[USERS_MESSAGES_WEBHOOK_RETRY_SHARED](#USERS_MESSAGES_WEBHOOK_RETRY_SHARED) | Webhook メッセージが優先度の引き下げまたはフリークエンシーキャップ後にリトライされたとき（**Snowflake Data Sharing のみ**）
[USERS_MESSAGES_WHATSAPP_ABORT_SHARED](#USERS_MESSAGES_WHATSAPP_ABORT_SHARED) | 元々スケジュールされた WhatsApp メッセージが何らかの理由で中止されたとき
[USERS_MESSAGES_WHATSAPP_CLICK_SHARED](#USERS_MESSAGES_WHATSAPP_CLICK_SHARED) | ユーザーが WhatsApp メッセージ内のリンクまたはボタンをクリックしたとき
[USERS_MESSAGES_WHATSAPP_DELIVERY_SHARED](#USERS_MESSAGES_WHATSAPP_DELIVERY_SHARED) | WhatsApp メッセージが配信されたとき
[USERS_MESSAGES_WHATSAPP_FAILURE_SHARED](#USERS_MESSAGES_WHATSAPP_FAILURE_SHARED) | WhatsApp メッセージがユーザーに配信されなかったとき
[USERS_MESSAGES_WHATSAPP_INBOUNDRECEIVE_SHARED](#USERS_MESSAGES_WHATSAPP_INBOUNDRECEIVE_SHARED) | ユーザーから WhatsApp メッセージを受信したとき
[USERS_MESSAGES_WHATSAPP_READ_SHARED](#USERS_MESSAGES_WHATSAPP_READ_SHARED) | ユーザーが WhatsApp メッセージを開いたとき
[USERS_MESSAGES_WHATSAPP_SEND_SHARED](#USERS_MESSAGES_WHATSAPP_SEND_SHARED) | ユーザーに WhatsApp メッセージを送信したとき
[USERS_MESSAGES_WHATSAPP_RETRY_SHARED](#USERS_MESSAGES_WHATSAPP_RETRY_SHARED) | WhatsApp メッセージが優先度の引き下げまたはフリークエンシーキャップ後にリトライされたとき（**Snowflake Data Sharing のみ**）
[USERS_RANDOMBUCKETNUMBERUPDATE_SHARED](#USERS_RANDOMBUCKETNUMBERUPDATE_SHARED) | ユーザーのランダムバケット番号が変更されたとき
[USERS_USERDELETEREQUEST_SHARED](#USERS_USERDELETEREQUEST_SHARED) | 顧客のリクエストによりユーザーが削除されたとき
[USERS_USERORPHAN_SHARED](#USERS_USERORPHAN_SHARED) | ユーザーが別のユーザーのプロファイルとマージされ、元のプロファイルが孤立したとき
[SNAPSHOTS_APP_SHARED](#SNAPSHOTS_APP_SHARED) | アプリスナップショット（**Snowflake Data Sharing のみ**）
[SNAPSHOTS_CAMPAIGN_MESSAGE_VARIATION_SHARED](#SNAPSHOTS_CAMPAIGN_MESSAGE_VARIATION_SHARED) | キャンペーンメッセージバリエーションスナップショット（**Snowflake Data Sharing のみ**）
[SNAPSHOTS_CANVAS_FLOW_STEP_SHARED](#SNAPSHOTS_CANVAS_FLOW_STEP_SHARED) | キャンバスフローステップスナップショット（**Snowflake Data Sharing のみ**）
[SNAPSHOTS_CANVAS_STEP_SHARED](#SNAPSHOTS_CANVAS_STEP_SHARED) | キャンバスステップスナップショット（**Snowflake Data Sharing のみ**）
[SNAPSHOTS_CANVAS_VARIATION_SHARED](#SNAPSHOTS_CANVAS_VARIATION_SHARED) | Canvas バリエーションスナップショット（**Snowflake Data Sharing のみ**）
[SNAPSHOTS_EXPERIMENT_STEP_SHARED](#SNAPSHOTS_EXPERIMENT_STEP_SHARED) | 実験ステップスナップショット（**Snowflake Data Sharing のみ**）


## Agent Console {#agent-console}

{% alert note %}
Agent Console テーブルは Snowflake Data Sharing でのみ利用可能です。
{% endalert %}

### AGENTCONSOLE_AGENTEXECUTED_SHARED {#AGENTCONSOLE_AGENTEXECUTED_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバル一意 ID
`invocation_id` | `string` | このメッセージのグローバル一意 ID
`request_id` | `string` | この LLM リクエスト全体と完全な実行の一意 ID
`duration` | `int` | セッションの継続時間（秒）
`prompt_tokens` | `int` | このリクエストで使用されたプロンプトトークン数
`completion_tokens` | `int` | このリクエストで使用された補完トークン数
`total_tokens` | `int` | このリクエストで使用された合計トークン数
`cache_tokens` | `int` | このリクエストで使用されたキャッシュトークン数
`reasoning_tokens` | `int` | このリクエストで使用された推論トークン数
`time` | `int` | イベントが発生した UNIX タイムスタンプ
`app_group_id` | `string` | このユーザーが属するアプリグループの BSON ID
`agent_id` | `string` | CustomerDefinedAgent の BSON ID
`agent_name` | `string` | CustomerDefinedAgent の名前
`model_provider` | `string` | LLM モデルプロバイダーの名前
`model_name` | `string` | このリクエストで使用された LLM モデルの名前
`provider_request_id` | `string` | API コールに対してモデルプロバイダーから提供されたリクエスト ID
`cache_hit` | `boolean` | このリクエストがキャッシュにヒットしてレスポンスを返したかどうか
`llm_owned_by_customer` | `boolean` | true の場合、顧客の API キーが使用されました。false の場合、Braze のキーが使用されました
`is_error` | `boolean` | このリクエストがエラーになったかどうか
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`user_id` | `string` | [PII] このイベントを実行したユーザーの Braze ユーザー ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの external ID
`input` | `null,`&nbsp;`string` | [PII] LLM への入力
`output` | `null,`&nbsp;`string` | [PII] LLM からのレスポンス
`invocation_source` | `null,`&nbsp;`string` | LLM リクエストを呼び出した Ruby オブジェクト
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### AGENTCONSOLE_TOOLINVOCATION_SHARED {#AGENTCONSOLE_TOOLINVOCATION_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバル一意 ID
`tool_call_id` | `string` | このツールコールのグローバル一意 ID
`duration` | `int` | セッションの継続時間（秒）
`time` | `int` | イベントが発生した UNIX タイムスタンプ
`app_group_id` | `string` | このユーザーが属するアプリグループの BSON ID
`agent_id` | `string` | CustomerDefinedAgent の BSON ID
`agent_name` | `string` | CustomerDefinedAgent の名前
`is_error` | `boolean` | このリクエストがエラーになったかどうか
`tool_name` | `string` | ツールの名前
`tool_arguments` | `null,`&nbsp;`string` | [PII] ツール引数の JSON
`invocation_source` | `null,`&nbsp;`string` | LLM リクエストを呼び出した Ruby オブジェクト
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## カタログ

### CATALOGS_ITEMS_SHARED {#CATALOGS_ITEMS_SHARED}

フィールド | タイプ | 説明
------|------|------------
`catalog_id` | `string` | カタログの BSON ID
`item_id` | `string` | カタログアイテムの BSON ID
`app_group_id` | `null,`&nbsp;`string` | アプリグループの BSON ID
`app_group_api_id` | `null,`&nbsp;`string` | アプリグループの API ID
`field_name` | `null,`&nbsp;`string` | フィールドの名前
`field_value` | `null,`&nbsp;`string` | フィールドの値
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## 変更ログ

### CHANGELOGS_GLOBALCONTROLGROUP_SHARED {#CHANGELOGS_GLOBALCONTROLGROUP_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバル一意 ID
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの API ID
`time` | `int` | イベントが発生した UNIX タイムスタンプ
`random_bucket_number` | `null, int` | 新しいランダムバケット番号
`global_control_group` | `null, boolean` | この変更により、バケット番号がグローバルコントロールグループに含まれます
`previous_global_control_group` | `null, boolean` | この変更前はバケット番号がグローバルコントロールグループに含まれていましたが、現在は含まれていません
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### CHANGELOGS_CAMPAIGN_SHARED {#CHANGELOGS_CAMPAIGN_SHARED}

{% alert note %}
このテーブルは Snowflake Data Sharing でのみ利用可能です。
{% endalert %}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバル一意 ID
`time` | `int` | イベントが発生した UNIX タイムスタンプ
`app_group_id` | `string` | このユーザーが属するアプリグループの BSON ID
`api_id` | `string` | キャンペーンの API ID
`name` | `null,`&nbsp;`string` | キャンペーンの名前
`conversion_behaviors` | `null,`&nbsp;`string` | キャンペーンのコンバージョン動作
`actions` | `null,`&nbsp;`string` | キャンペーンのアクション
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### CHANGELOGS_CANVAS_SHARED {#CHANGELOGS_CANVAS_SHARED}

{% alert note %}
このテーブルは Snowflake Data Sharing でのみ利用可能です。
{% endalert %}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバル一意 ID
`time` | `int` | イベントが発生した UNIX タイムスタンプ
`app_group_id` | `string` | このユーザーが属するアプリグループの BSON ID
`api_id` | `string` | Canvas の API ID
`name` | `null,`&nbsp;`string` | Canvas の名前
`conversion_behaviors` | `null,`&nbsp;`string` | Canvas のコンバージョン動作
`variations` | `null,`&nbsp;`string` | Canvas のバリエーション
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


## 動作

### USERS_BEHAVIORS_CUSTOMEVENT_SHARED {#USERS_BEHAVIORS_CUSTOMEVENT_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバル一意 ID
`user_id` | `string` | イベントを実行したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの external user ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するワークスペースの API ID
`app_api_id` | `null,`&nbsp;`string` | このアクションが発生したアプリの API ID
`time` | `int` | ユーザーがイベントを実行した Unix タイムスタンプ
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`device_id` | `null,`&nbsp;`string` | カスタムイベントが発生したデバイスの ID
`sdk_version` | `null,`&nbsp;`string` | イベント時に使用されていた Braze SDK のバージョン
`platform` | `null,`&nbsp;`string` | デバイスのプラットフォーム
`os_version` | `null,`&nbsp;`string` | デバイスのオペレーティングシステムのバージョン
`device_model` | `null,`&nbsp;`string` | デバイスのモデル
`name` | `string` | カスタムイベントの名前
`properties` | `string` | JSON エンコードされた文字列として保存されたイベントのカスタムプロパティ
`ad_id` | `null,`&nbsp;`string` | [PII] 広告識別子
`ad_id_type` | `null,`&nbsp;`string` | `ios_idfa`、`google_ad_id`、`windows_ad_id`、または `roku_ad_id` のいずれか
`ad_tracking_enabled` | `null, boolean` | デバイスで広告トラッキングが有効かどうか
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_INSTALLATTRIBUTION_SHARED {#USERS_BEHAVIORS_INSTALLATTRIBUTION_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバル一意 ID
`user_id` | `string` | インストールしたユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの external user ID
`device_id` | `null,`&nbsp;`string` | ユーザーが匿名の場合、このユーザーに紐づく `device_id`
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するワークスペースの API ID
`time` | `int` | ユーザーがインストールした Unix タイムスタンプ
`source` | `string` | アトリビューションのソース
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_LOCATION_SHARED {#USERS_BEHAVIORS_LOCATION_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバル一意 ID
`user_id` | `string` | ロケーションを記録したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの external user ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するワークスペースの API ID
`app_api_id` | `null,`&nbsp;`string` | このロケーションが記録されたアプリの API ID
`time` | `int` | ロケーションが記録された Unix タイムスタンプ
`latitude` | `float` | [PII] 記録されたロケーションの緯度
`longitude` | `float` | [PII] 記録されたロケーションの経度
`altitude` | `null, float` | [PII] 記録されたロケーションの高度
`ll_accuracy` | `null, float` | 記録されたロケーションの緯度・経度の精度
`alt_accuracy` | `null, float` | 記録されたロケーションの高度の精度
`device_id` | `null,`&nbsp;`string` | ロケーションが記録されたデバイスの ID
`sdk_version` | `null,`&nbsp;`string` | ロケーション記録時に使用されていた Braze SDK のバージョン
`platform` | `null,`&nbsp;`string` | デバイスのプラットフォーム
`os_version` | `null,`&nbsp;`string` | デバイスのオペレーティングシステムのバージョン
`device_model` | `null,`&nbsp;`string` | デバイスのモデル
`ad_id` | `null,`&nbsp;`string` | [PII] 広告識別子
`ad_id_type` | `null,`&nbsp;`string` | `ios_idfa`、`google_ad_id`、`windows_ad_id`、または `roku_ad_id` のいずれか
`ad_tracking_enabled` | `null, boolean` | デバイスで広告トラッキングが有効かどうか
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_PURCHASE_SHARED {#USERS_BEHAVIORS_PURCHASE_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバル一意 ID
`user_id` | `string` | 購入を行ったユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの external user ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するワークスペースの API ID
`app_api_id` | `null,`&nbsp;`string` | 購入が発生したアプリの API ID
`time` | `int` | ユーザーが購入を行った Unix タイムスタンプ
`device_id` | `null,`&nbsp;`string` | 購入が発生したデバイスの ID
`sdk_version` | `null,`&nbsp;`string` | 購入時に使用されていた Braze SDK のバージョン
`platform` | `null,`&nbsp;`string` | デバイスのプラットフォーム
`os_version` | `null,`&nbsp;`string` | デバイスのオペレーティングシステムのバージョン
`device_model` | `null,`&nbsp;`string` | デバイスのモデル
`product_id` | `string` | 購入された製品の ID
`price` | `float` | 購入の価格
`currency` | `string` | 購入の通貨
`properties` | `string` | JSON エンコードされた文字列として保存された購入のカスタムプロパティ
`ad_id` | `null,`&nbsp;`string` | [PII] 広告識別子
`ad_id_type` | `null,`&nbsp;`string` | `ios_idfa`、`google_ad_id`、`windows_ad_id`、または `roku_ad_id` のいずれか
`ad_tracking_enabled` | `null, boolean` | デバイスで広告トラッキングが有効かどうか
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_UNINSTALL_SHARED {#USERS_BEHAVIORS_UNINSTALL_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバル一意 ID
`user_id` | `string` | アンインストールしたユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの external user ID
`device_id` | `null,`&nbsp;`string` | ユーザーが匿名の場合、このユーザーに紐づく `device_id`
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するワークスペースの API ID
`app_api_id` | `null,`&nbsp;`string` | アンインストールされたアプリの API ID
`time` | `int` | ユーザーがアンインストールした Unix タイムスタンプ
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_UPGRADEDAPP_SHARED {#USERS_BEHAVIORS_UPGRADEDAPP_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバル一意 ID
`user_id` | `string` | アプリをアップグレードしたユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの external user ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するワークスペースの API ID
`app_api_id` | `null,`&nbsp;`string` | ユーザーがアップグレードしたアプリの API ID
`time` | `int` | ユーザーがアプリをアップグレードした Unix タイムスタンプ
`device_id` | `null,`&nbsp;`string` | ユーザーがアプリをアップグレードしたデバイスの ID
`sdk_version` | `null,`&nbsp;`string` | 使用されていた Braze SDK のバージョン
`platform` | `null,`&nbsp;`string` | デバイスのプラットフォーム
`os_version` | `null,`&nbsp;`string` | デバイスのオペレーティングシステムのバージョン
`device_model` | `null,`&nbsp;`string` | デバイスのモデル
`old_app_version` | `null,`&nbsp;`string` | アプリの旧バージョン
`new_app_version` | `null,`&nbsp;`string` | アプリの新バージョン
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_APP_FIRSTSESSION_SHARED {#USERS_BEHAVIORS_APP_FIRSTSESSION_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバル一意 ID
`user_id` | `string` | このアクションを実行したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの external user ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するワークスペースの API ID
`app_api_id` | `null,`&nbsp;`string` | このセッションが発生したアプリの API ID
`time` | `int` | セッションが開始された Unix タイムスタンプ
`session_id` | `string` | セッションの UUID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`device_id` | `null,`&nbsp;`string` | セッションが発生したデバイスの ID
`sdk_version` | `null,`&nbsp;`string` | セッション中に使用されていた Braze SDK のバージョン
`platform` | `null,`&nbsp;`string` | デバイスのプラットフォーム
`os_version` | `null,`&nbsp;`string` | デバイスのオペレーティングシステムのバージョン
`device_model` | `null,`&nbsp;`string` | デバイスのモデル
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_BEHAVIORS_APP_NEWSFEEDIMPRESSION_SHARED {#USERS_BEHAVIORS_APP_NEWSFEEDIMPRESSION_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバル一意 ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ユーザー ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの external ID
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの API ID
`app_api_id` | `null,`&nbsp;`string` | このイベントが発生したアプリの API ID
`time` | `int` | イベントが発生した UNIX タイムスタンプ
`device_id` | `null,`&nbsp;`string` | イベントが発生したデバイスの ID
`sdk_version` | `null,`&nbsp;`string` | イベント時に使用されていた Braze SDK のバージョン
`platform` | `null,`&nbsp;`string` | デバイスのプラットフォーム
`os_version` | `null,`&nbsp;`string` | デバイスのオペレーティングシステムのバージョン
`device_model` | `null,`&nbsp;`string` | デバイスのモデル
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_APP_SESSIONEND_SHARED {#USERS_BEHAVIORS_APP_SESSIONEND_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバル一意 ID
`user_id` | `string` | このアクションを実行したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの external user ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するワークスペースの API ID
`app_api_id` | `null,`&nbsp;`string` | このセッションが発生したアプリの API ID
`time` | `int` | セッションが終了した Unix タイムスタンプ
`duration` | `null, float` | セッションの継続時間（秒）
`session_id` | `string` | セッションの UUID
`device_id` | `null,`&nbsp;`string` | セッションが発生したデバイスの ID
`sdk_version` | `null,`&nbsp;`string` | セッション中に使用されていた Braze SDK のバージョン
`platform` | `null,`&nbsp;`string` | デバイスのプラットフォーム
`os_version` | `null,`&nbsp;`string` | デバイスのオペレーティングシステムのバージョン
`device_model` | `null,`&nbsp;`string` | デバイスのモデル
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_APP_SESSIONSTART_SHARED {#USERS_BEHAVIORS_APP_SESSIONSTART_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバル一意 ID
`user_id` | `string` | このアクションを実行したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの external user ID
`app_api_id` | `null,`&nbsp;`string` | このセッションが発生したアプリの API ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するワークスペースの API ID
`time` | `int` | セッションが開始された Unix タイムスタンプ
`session_id` | `string` | セッションの UUID
`device_id` | `null,`&nbsp;`string` | セッションが発生したデバイスの ID
`sdk_version` | `null,`&nbsp;`string` | セッション中に使用されていた Braze SDK のバージョン
`platform` | `null,`&nbsp;`string` | デバイスのプラットフォーム
`os_version` | `null,`&nbsp;`string` | デバイスのオペレーティングシステムのバージョン
`device_model` | `null,`&nbsp;`string` | デバイスのモデル
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_GEOFENCE_DATAEVENT_SHARED {#USERS_BEHAVIORS_GEOFENCE_DATAEVENT_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバル一意 ID
`user_id` | `string` | イベントを実行したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの external user ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するワークスペースの API ID
`app_api_id` | `null,`&nbsp;`string` | このアクションが発生したアプリの API ID
`time` | `int` | ユーザーがイベントを実行した Unix タイムスタンプ
`device_id` | `null,`&nbsp;`string` | カスタムイベントが発生したデバイスの ID
`sdk_version` | `null,`&nbsp;`string` | イベント時に使用されていた Braze SDK のバージョン
`platform` | `null,`&nbsp;`string` | デバイスのプラットフォーム
`os_version` | `null,`&nbsp;`string` | デバイスのオペレーティングシステムのバージョン
`device_model` | `null,`&nbsp;`string` | デバイスのモデル
`event_type` | `string` | トリガーされたジオフェンスイベントの種類（例: 'enter' または 'exit'）
`location_set_id` | `string` | トリガーされたジオフェンスのロケーションセットの ID
`geofence_id` | `string` | トリガーされたジオフェンスの ID
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_GEOFENCE_RECORDEVENT_SHARED {#USERS_BEHAVIORS_GEOFENCE_RECORDEVENT_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバル一意 ID
`user_id` | `string` | イベントを実行したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの external user ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するワークスペースの API ID
`app_api_id` | `null,`&nbsp;`string` | このアクションが発生したアプリの API ID
`time` | `int` | ユーザーがイベントを実行した Unix タイムスタンプ
`device_id` | `null,`&nbsp;`string` | カスタムイベントが発生したデバイスの ID
`sdk_version` | `null,`&nbsp;`string` | イベント時に使用されていた Braze SDK のバージョン
`platform` | `null,`&nbsp;`string` | デバイスのプラットフォーム
`os_version` | `null,`&nbsp;`string` | デバイスのオペレーティングシステムのバージョン
`device_model` | `null,`&nbsp;`string` | デバイスのモデル
`event_type` | `string` | トリガーされたジオフェンスイベントの種類（例: 'enter' または 'exit'）
`location_set_id` | `string` | トリガーされたジオフェンスのロケーションセットの ID
`geofence_id` | `string` | トリガーされたジオフェンスの ID
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_BEHAVIORS_LIVEACTIVITY_PUSHTOSTARTTOKENCHANGE_SHARED {#USERS_BEHAVIORS_LIVEACTIVITY_PUSHTOSTARTTOKENCHANGE_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバル一意 ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ユーザー ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの external ID
`time` | `int` | イベントが発生した UNIX タイムスタンプ
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`activity_attributes_type` | `null,`&nbsp;`string` | Live Activity の属性タイプ
`push_to_start_token` | `null,`&nbsp;`string` | Live Activity の push to start トークン
`device_id` | `null,`&nbsp;`string` | イベントが発生したデバイスの ID
`sdk_version` | `null,`&nbsp;`string` | イベント時に使用されていた Braze SDK のバージョン
`ios_push_token_apns_gateway` | `null, int` | プッシュトークンの APN ゲートウェイ。iOS プッシュトークンにのみ適用されます。1 は開発用、2 は本番用
`push_token_state_change_type` | `null,`&nbsp;`string` | プッシュトークンの状態変更タイプの説明
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの API ID
`app_api_id` | `null,`&nbsp;`string` | このイベントが発生したアプリの API ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_BEHAVIORS_LIVEACTIVITY_UPDATETOKENCHANGE_SHARED {#USERS_BEHAVIORS_LIVEACTIVITY_UPDATETOKENCHANGE_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバル一意 ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ユーザー ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの external ID
`time` | `int` | イベントが発生した UNIX タイムスタンプ
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`activity_id` | `null,`&nbsp;`string` | Live Activity の識別子
`update_token` | `null,`&nbsp;`string` | Live Activity の更新トークン
`device_id` | `null,`&nbsp;`string` | イベントが発生したデバイスの ID
`sdk_version` | `null,`&nbsp;`string` | イベント時に使用されていた Braze SDK のバージョン
`ios_push_token_apns_gateway` | `null, int` | プッシュトークンの APN ゲートウェイ。iOS プッシュトークンにのみ適用されます。1 は開発用、2 は本番用
`push_token_state_change_type` | `null,`&nbsp;`string` | プッシュトークンの状態変更タイプの説明
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの API ID
`app_api_id` | `null,`&nbsp;`string` | このイベントが発生したアプリの API ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_BEHAVIORS_PUSHNOTIFICATION_TOKENSTATECHANGE_SHARED {#USERS_BEHAVIORS_PUSHNOTIFICATION_TOKENSTATECHANGE_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバル一意 ID
`time` | `int` | イベントが発生した UNIX タイムスタンプ
`time_ms` | `int` | イベントが発生した時刻（ミリ秒）
`user_id` | `string` | このイベントを実行したユーザーの Braze ユーザー ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの external ID
`sdk_version` | `null,`&nbsp;`string` | イベント時に使用されていた Braze SDK のバージョン
`platform` | `null,`&nbsp;`string` | デバイスのプラットフォーム
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`push_token` | `null,`&nbsp;`string` | イベントのプッシュトークン
`push_token_created_at` | `null, int` | プッシュトークンが作成された UNIX タイムスタンプ
`push_token_updated_at` | `null, int` | プッシュトークンが最後に更新された UNIX タイムスタンプ
`push_token_foreground_push_disabled` | `null, boolean` | プッシュトークンのフォアグラウンドプッシュ無効フラグ
`push_token_device_id` | `null,`&nbsp;`string` | プッシュトークンのデバイス ID
`push_token_provisionally_opted_in` | `null, boolean` | プッシュトークンの仮オプトインフラグ
`ios_push_token_apns_gateway` | `null, int` | プッシュトークンの APN ゲートウェイ。iOS プッシュトークンにのみ適用されます。1 は開発用、2 は本番用
`web_push_token_public_key` | `null,`&nbsp;`string` | プッシュトークンの公開キー。Web プッシュトークンにのみ適用されます
`web_push_token_user_auth` | `null,`&nbsp;`string` | プッシュトークンのユーザー認証。Web プッシュトークンにのみ適用されます
`web_push_token_vapid_public_key` | `null,`&nbsp;`string` | プッシュトークンの VAPID 公開キー。Web プッシュトークンにのみ適用されます
`push_token_state_change_type` | `null,`&nbsp;`string` | プッシュトークンの状態変更タイプの説明
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの API ID
`app_api_id` | `null,`&nbsp;`string` | このイベントが発生したアプリの API ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_SUBSCRIPTION_GLOBALSTATECHANGE_SHARED {#USERS_BEHAVIORS_SUBSCRIPTION_GLOBALSTATECHANGE_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバル一意 ID
`user_id` | `string` | 影響を受けたユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの external user ID
`email_address` | `null,`&nbsp;`string` | [PII] ユーザーのメールアドレス
`state_change_source` | `null,`&nbsp;`string` | 状態変更のソース（REST、SDK、ダッシュボードなど）
`subscription_status` | `string` | サブスクリプションステータス: 'Subscribed'、'Unsubscribed'、または 'Opted In'
`channel` | `null,`&nbsp;`string` | メールなどのグローバルサブスクリプション状態のチャネル
`time` | `int` | サブスクリプション状態が変更された Unix タイムスタンプ
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するワークスペースの API ID
`app_api_id` | `null,`&nbsp;`string` | イベントが属するアプリの API ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このイベントが属するメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`send_id` | `null,`&nbsp;`string` | このサブスクリプション状態変更アクションの発生元であるメッセージ送信 ID
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`channel_identifier` | `null,`&nbsp;`string` | [PII] イベント対象チャネルにおけるユーザーの識別子
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED {#USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバル一意 ID
`user_id` | `string` | 影響を受けたユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの external user ID
`device_id` | `null,`&nbsp;`string` | ユーザーが匿名の場合、このユーザーに紐づく `device_id`
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するワークスペースの API ID
`email_address` | `null,`&nbsp;`string` | [PII] ユーザーのメールアドレス
`phone_number` | `null,`&nbsp;`string` | [PII] e164 形式のユーザーの電話番号
`app_api_id` | `null,`&nbsp;`string` | イベントが属するアプリの API ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このイベントが属するメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`subscription_group_api_id` | `string` | サブスクリプショングループの API ID
`channel` | `null,`&nbsp;`string` | チャネル: サブスクリプショングループのチャネルタイプに応じて 'email' または 'sms'
`subscription_status` | `string` | サブスクリプションステータス: 'Subscribed'、'Unsubscribed'、または 'Opted In'
`time` | `int` | サブスクリプション状態が変更された Unix タイムスタンプ
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`send_id` | `null,`&nbsp;`string` | このサブスクリプション状態変更アクションの発生元であるメッセージ送信 ID
`state_change_source` | `null,`&nbsp;`string` | 状態変更のソース（REST、SDK、ダッシュボードなど）
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`channel_identifier` | `null,`&nbsp;`string` | [PII] イベント対象チャネルにおけるユーザーの識別子
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## キャンペーン

### USERS_CAMPAIGNS_CONVERSION_SHARED {#USERS_CAMPAIGNS_CONVERSION_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの external ID
`device_id` | `null,`&nbsp;`string` | ユーザーが匿名の場合、このユーザーに紐づけられた `device_id`
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが所属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`app_api_id` | `null,`&nbsp;`string` | このイベントが発生したアプリの API ID
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`conversion_behavior_index` | `null, int` | コンバージョン動作のインデックス
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`app_group_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CAMPAIGNS_ENROLLINCONTROL_SHARED {#USERS_CAMPAIGNS_ENROLLINCONTROL_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの external ID
`device_id` | `null,`&nbsp;`string` | ユーザーが匿名の場合、このユーザーに紐づけられた `device_id`
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが所属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`app_api_id` | `null,`&nbsp;`string` | このイベントが発生したアプリの API ID
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`app_group_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CAMPAIGNS_FREQUENCYCAP_SHARED {#USERS_CAMPAIGNS_FREQUENCYCAP_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの external ID
`device_id` | `null,`&nbsp;`string` | ユーザーが匿名の場合、このユーザーに紐づけられた `device_id`
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが所属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`channel` | `null,`&nbsp;`string` | このイベントが属するチャネル
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`app_group_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CAMPAIGNS_REVENUE_SHARED {#USERS_CAMPAIGNS_REVENUE_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの external ID
`device_id` | `null,`&nbsp;`string` | ユーザーが匿名の場合、このユーザーに紐づけられた `device_id`
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが所属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`app_api_id` | `null,`&nbsp;`string` | このイベントが発生したアプリの API ID
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`revenue` | `long` | 生成された USD 収益額 (セント単位)
`app_group_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Canvas

### USERS_CANVASSTEP_PROGRESSION_SHARED {#USERS_CANVASSTEP_PROGRESSION_SHARED}

| フィールド                                  | タイプ                     | 説明                                                                                                     |
| -------------------------------------- | ------------------------ | --------------------------------------------------------------------------------------------------------------- |
| `id`                                   | `string`,&nbsp;`null`    | このイベントのグローバルな一意の ID                                                                               |
| `user_id`                              | `string`,&nbsp;`null`    | このイベントを実行したユーザーの Braze ID                                                                   |
| `external_user_id`                     | `string`,&nbsp;`null`    | [PII] ユーザーの external ID                                                                              |
| `device_id`                            | `string`,&nbsp;`null`    | ユーザーが匿名の場合、このユーザーに紐づけられたデバイスの ID                                            |
| `app_group_id`                         | `string`,&nbsp;`null`    | このユーザーが所属するワークスペースの Braze ID                                                                   |
| `app_group_api_id`                     | `string`,&nbsp;`null`    | このユーザーが所属するワークスペースの API ID                                                                    |
| `time`                                 | `int`,&nbsp;`null`       | イベントが発生した Unix タイムスタンプ                                                                      |
| `canvas_id`                            | `string`,&nbsp;`null`    | (Braze 内部使用のみ) このイベントが属する Canvas の ID                                                     |
| `canvas_api_id`                        | `string`,&nbsp;`null`    | このイベントが属する Canvas の API ID        |         
| `canvas_variation_api_id`              | `string`,&nbsp;`null`    | このイベントが属する Canvas バリエーションの API ID                                                            |
| `canvas_step_api_id`                   | `string`,&nbsp;`null`    | このイベントが属するキャンバスステップの API ID                                                                 |
| `progression_type`                     | `string`,&nbsp;`null`    | ステップ進行イベントのタイプ |
| `is_canvas_entry`                      | `boolean`,&nbsp;`null`   | Canvas の最初のステップへのエントリかどうか        |
| `exit_reason`                          | `string`,&nbsp;`null`    | 離脱の場合、ユーザーがそのステップで Canvas を離脱した理由                  |
| `canvas_entry_id`                      | `string`,&nbsp;`null`    | Canvas 内のこのユーザーインスタンスの一意の識別子  |
| `next_step_id`                         | `string`,&nbsp;`null`    | Canvas の次のステップの BSON ID |
| `next_step_api_id`                     | `string`,&nbsp;`null`    | Canvas の次のステップの API ID |
| `sf_created_at`                        | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時                                                                   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_CONVERSION_SHARED {#USERS_CANVAS_CONVERSION_SHARED}

| フィールド                                  | タイプ                     | 説明                                                                                                     |
| -------------------------------------- | ------------------------ | --------------------------------------------------------------------------------------------------------------- |
| `id`                                   | `string`,&nbsp;`null`    | このイベントのグローバルな一意の ID                                                                               |
| `user_id`                              | `string`,&nbsp;`null`    | このイベントを実行したユーザーの Braze ID                                                                   |
| `external_user_id`                     | `string`,&nbsp;`null`    | [PII] ユーザーの external ID                                                                              |
| `device_id`                            | `string`,&nbsp;`null`    | ユーザーが匿名の場合、このユーザーに紐づけられたデバイスの ID                                            |
| `app_group_id`                         | `string`,&nbsp;`null`    | このユーザーが所属するワークスペースの Braze ID                                                                   |
| `app_group_api_id`                     | `string`,&nbsp;`null`    | このユーザーが所属するワークスペースの API ID                                                                    |
| `time`                                 | `int`,&nbsp;`null`       | イベントが発生した Unix タイムスタンプ                                                                      |
| `app_api_id`                           | `string`,&nbsp;`null`    | このイベントが発生したアプリの API ID                                                                  |
| `canvas_id`                            | `string`,&nbsp;`null`    | (Braze 内部使用のみ) このイベントが属する Canvas の ID                                                     |
| `canvas_api_id`                        | `string`,&nbsp;`null`    | このイベントが属する Canvas の API ID                                                                      |
| `canvas_variation_api_id`              | `string`,&nbsp;`null`    | このイベントが属する Canvas バリエーションの API ID                                                            |
| `canvas_step_api_id`                   | `string`,&nbsp;`null`    | このイベントが属するキャンバスステップの API ID                                                                 |
| `canvas_step_message_variation_api_id` | `string`,&nbsp;`null`    | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID                                                  |
| `conversion_behavior_index`            | `int`,&nbsp;`null`       | ユーザーが実行したコンバージョンイベントのタイプ。「0」は1次コンバージョン、「1」は2次コンバージョンです |
| `gender`                               | `string`,&nbsp;`null`    | [PII] ユーザーの性別                                                                                        |
| `country`                              | `string`,&nbsp;`null`    | [PII] ユーザーの国                                                                                       |
| `timezone`                             | `string`,&nbsp;`null`    | ユーザーのタイムゾーン                                                                                            |
| `language`                             | `string`,&nbsp;`null`    | [PII] ユーザーの言語                                                                                      |
| `sf_created_at`                        | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時                                                                   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_ENTRY_SHARED {#USERS_CANVAS_ENTRY_SHARED}

| フィールド                     | タイプ                     | 説明                                                          |
| ------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                      | `string`,&nbsp;`null`    | このイベントのグローバルな一意の ID                                    |
| `user_id`                 | `string`,&nbsp;`null`    | このイベントを実行したユーザーの Braze ID                        |
| `external_user_id`        | `string`,&nbsp;`null`    | [PII] ユーザーの external ID                                   |
| `device_id`               | `string`,&nbsp;`null`    | ユーザーが匿名の場合、このユーザーに紐づけられたデバイスの ID |
| `app_group_id`            | `string`,&nbsp;`null`    | このユーザーが所属するワークスペースの Braze ID                        |
| `app_group_api_id`        | `string`,&nbsp;`null`    | このユーザーが所属するワークスペースの API ID                         |
| `time`                    | `int`,&nbsp;`null`       | イベントが発生した Unix タイムスタンプ                           |
| `canvas_id`               | `string`,&nbsp;`null`    | (Braze 内部使用のみ) このイベントが属する Canvas の ID          |
| `canvas_api_id`           | `string`,&nbsp;`null`    | このイベントが属する Canvas の API ID                           |
| `canvas_variation_api_id` | `string`,&nbsp;`null`    | このイベントが属する Canvas バリエーションの API ID                 |
| `canvas_step_api_id`      | `string`,&nbsp;`null`    | [非推奨] このイベントが属するキャンバスステップの API ID         |
| `gender`                  | `string`,&nbsp;`null`    | [PII] ユーザーの性別                                             |
| `country`                 | `string`,&nbsp;`null`    | [PII] ユーザーの国                                            |
| `timezone`                | `string`,&nbsp;`null`    | ユーザーのタイムゾーン                                                 |
| `language`                | `string`,&nbsp;`null`    | [PII] ユーザーの言語                                           |
| `in_control_group`        | `boolean`,&nbsp;`null`   | ユーザーがコントロールグループに登録されたかどうか                   |
| `sf_created_at`           | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時                        |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_EXIT_MATCHEDAUDIENCE_SHARED {#USERS_CANVAS_EXIT_MATCHEDAUDIENCE_SHARED}

| フィールド                     | タイプ                     | 説明                                                          |
| ------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                      | `string`,&nbsp;`null`    | このイベントのグローバルな一意の ID                                    |
| `user_id`                 | `string`,&nbsp;`null`    | このイベントを実行したユーザーの Braze ID                        |
| `external_user_id`        | `string`,&nbsp;`null`    | [PII] ユーザーの external ID                                   |
| `app_group_id`            | `string`,&nbsp;`null`    | このユーザーが所属するワークスペースの Braze ID                        |
| `app_group_api_id`        | `string`,&nbsp;`null`    | このユーザーが所属するワークスペースの API ID                         |
| `time`                    | `int`,&nbsp;`null`       | イベントが発生した Unix タイムスタンプ                           |
| `canvas_id`               | `string`,&nbsp;`null`    | (Braze 内部使用のみ) このイベントが属する Canvas の ID          |
| `canvas_api_id`           | `string`,&nbsp;`null`    | このイベントが属する Canvas の API ID                           |
| `canvas_variation_api_id` | `string`,&nbsp;`null`    | このイベントが属する Canvas バリエーションの API ID                 |
| `canvas_step_api_id`      | `string`,&nbsp;`null`    | このイベントが属するキャンバスステップの API ID                      |
| `sf_created_at`           | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時                        |

{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_EXIT_PERFORMEDEVENT_SHARED {#USERS_CANVAS_EXIT_PERFORMEDEVENT_SHARED}

| フィールド                     | タイプ                     | 説明                                                          |
| ------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                      | `string`,&nbsp;`null`    | このイベントのグローバルな一意の ID                                    |
| `user_id`                 | `string`,&nbsp;`null`    | このイベントを実行したユーザーの Braze ID                        |
| `external_user_id`        | `string`,&nbsp;`null`    | [PII] ユーザーの external ID                                   |
| `app_group_id`            | `string`,&nbsp;`null`    | このユーザーが所属するワークスペースの Braze ID                        |
| `app_group_api_id`        | `string`,&nbsp;`null`    | このユーザーが所属するワークスペースの API ID                         |
| `time`                    | `int`,&nbsp;`null`       | イベントが発生した Unix タイムスタンプ                           |
| `canvas_id`               | `string`,&nbsp;`null`    | (Braze 内部使用のみ) このイベントが属する Canvas の ID          |
| `canvas_api_id`           | `string`,&nbsp;`null`    | このイベントが属する Canvas の API ID                           |
| `canvas_variation_api_id` | `string`,&nbsp;`null`    | このイベントが属する Canvas バリエーションの API ID                 |
| `canvas_step_api_id`      | `string`,&nbsp;`null`    | このイベントが属するキャンバスステップの API ID                      |
| `sf_created_at`           | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時                        |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_EXPERIMENTSTEP_CONVERSION_SHARED {#USERS_CANVAS_EXPERIMENTSTEP_CONVERSION_SHARED}

| フィールド                       | タイプ                     | 説明                                                                                                     |
| --------------------------- | ------------------------ | --------------------------------------------------------------------------------------------------------------- |
| `id`                        | `string`,&nbsp;`null`    | このイベントのグローバルな一意の ID                                                                               |
| `user_id`                   | `string`,&nbsp;`null`    | このイベントを実行したユーザーの Braze ID                                                                   |
| `external_user_id`          | `string`,&nbsp;`null`    | [PII] ユーザーの external ID                                                                              |
| `app_group_id`              | `string`,&nbsp;`null`    | このユーザーが所属するワークスペースの Braze ID                                                                   |
| `time`                      | `int`,&nbsp;`null`       | イベントが発生した Unix タイムスタンプ                                                                      |
| `app_api_id`                | `string`,&nbsp;`null`    | このイベントが発生したアプリの API ID                                                                  |
| `canvas_id`                 | `string`,&nbsp;`null`    | (Braze 内部使用のみ) このイベントが属する Canvas の ID                                                     |
| `canvas_api_id`             | `string`,&nbsp;`null`    | このイベントが属する Canvas の API ID                                                                      |
| `canvas_variation_api_id`   | `string`,&nbsp;`null`    | このイベントが属する Canvas バリエーションの API ID                                                            |
| `canvas_step_api_id`        | `string`,&nbsp;`null`    | このイベントが属するキャンバスステップの API ID                                                                 |
| `experiment_step_api_id`    | `string`,&nbsp;`null`    | このイベントが属する実験ステップの API ID                                                             |
| `conversion_behavior_index` | `int`,&nbsp;`null`       | ユーザーが実行したコンバージョンイベントのタイプ。「0」は1次コンバージョン、「1」は2次コンバージョンです |
| `sf_created_at`             | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時                                                                   |
| `experiment_split_api_id` | `string`,&nbsp;`null` | ユーザーが登録された実験スプリットの API ID |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_EXPERIMENTSTEP_SPLITENTRY_SHARED {#USERS_CANVAS_EXPERIMENTSTEP_SPLITENTRY_SHARED}

| フィールド                     | タイプ                     | 説明                                                          |
| ------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                      | `string`,&nbsp;`null`    | このイベントのグローバルな一意の ID                                    |
| `user_id`                 | `string`,&nbsp;`null`    | このイベントを実行したユーザーの Braze ID                        |
| `external_user_id`        | `string`,&nbsp;`null`    | [PII] ユーザーの external ID                                   |
| `app_group_id`            | `string`,&nbsp;`null`    | このユーザーが所属するワークスペースの Braze ID                        |
| `time`                    | `int`,&nbsp;`null`       | イベントが発生した Unix タイムスタンプ                           |
| `canvas_id`               | `string`,&nbsp;`null`    | (Braze 内部使用のみ) このイベントが属する Canvas の ID          |
| `canvas_api_id`           | `string`,&nbsp;`null`    | このイベントが属する Canvas の API ID                           |
| `canvas_variation_api_id` | `string`,&nbsp;`null`    | このイベントが属する Canvas バリエーションの API ID                 |
| `canvas_step_api_id`      | `string`,&nbsp;`null`    | このイベントが属するキャンバスステップの API ID                      |
| `experiment_step_api_id`  | `string`,&nbsp;`null`    | このイベントが属する実験ステップの API ID                  |
| `in_control_group`        | `boolean`,&nbsp;`null`   | ユーザーがコントロールグループに登録されたかどうか                   |
| `sf_created_at`           | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時                        |

| `experiment_split_api_id` | `string`,&nbsp;`null` | ユーザーが登録された実験スプリットの API ID |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_FREQUENCYCAP_SHARED {#USERS_CANVAS_FREQUENCYCAP_SHARED}

| フィールド                                  | タイプ                     | 説明                                                          |
| -------------------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                                   | `string`,&nbsp;`null`    | このイベントのグローバルな一意の ID                                    |
| `user_id`                              | `string`,&nbsp;`null`    | このイベントを実行したユーザーの Braze ID                        |
| `external_user_id`                     | `string`,&nbsp;`null`    | [PII] ユーザーの external ID                                   |
| `device_id`                            | `string`,&nbsp;`null`    | ユーザーが匿名の場合、このユーザーに紐づけられたデバイスの ID |
| `app_group_id`                         | `string`,&nbsp;`null`    | このユーザーが所属するワークスペースの Braze ID                        |
| `app_group_api_id`                     | `string`,&nbsp;`null`    | このユーザーが所属するワークスペースの API ID                         |
| `time`                                 | `int`,&nbsp;`null`       | イベントが発生した Unix タイムスタンプ                           |
| `canvas_id`                            | `string`,&nbsp;`null`    | (Braze 内部使用のみ) このイベントが属する Canvas の ID          |
| `canvas_api_id`                        | `string`,&nbsp;`null`    | このイベントが属する Canvas の API ID                           |
| `canvas_variation_api_id`              | `string`,&nbsp;`null`    | このイベントが属する Canvas バリエーションの API ID                 |
| `canvas_step_api_id`                   | `string`,&nbsp;`null`    | このイベントが属するキャンバスステップの API ID                      |
| `canvas_step_message_variation_api_id` | `string`,&nbsp;`null`    | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID       |
| `channel`                              | `string`,&nbsp;`null`    | このイベントが属するメッセージングチャネル (メール、プッシュなど)          |
| `gender`                               | `string`,&nbsp;`null`    | [PII] ユーザーの性別                                             |
| `country`                              | `string`,&nbsp;`null`    | [PII] ユーザーの国                                            |
| `timezone`                             | `string`,&nbsp;`null`    | ユーザーのタイムゾーン                                                 |
| `language`                             | `string`,&nbsp;`null`    | [PII] ユーザーの言語                                           |
| `sf_created_at`                        | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時                        |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_REVENUE_SHARED {#USERS_CANVAS_REVENUE_SHARED}

| フィールド                                  | タイプ                     | 説明                                                          |
| -------------------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                                   | `string`,&nbsp;`null`    | このイベントのグローバルな一意の ID                                    |
| `user_id`                              | `string`,&nbsp;`null`    | このイベントを実行したユーザーの Braze ID                        |
| `external_user_id`                     | `string`,&nbsp;`null`    | [PII] ユーザーの external ID                                   |
| `device_id`                            | `string`,&nbsp;`null`    | ユーザーが匿名の場合、このユーザーに紐づけられたデバイスの ID |
| `app_group_id`                         | `string`,&nbsp;`null`    | このユーザーが所属するワークスペースの Braze ID                        |
| `app_group_api_id`                     | `string`,&nbsp;`null`    | このユーザーが所属するワークスペースの API ID                         |
| `time`                                 | `int`,&nbsp;`null`       | イベントが発生した Unix タイムスタンプ                           |
| `canvas_id`                            | `string`,&nbsp;`null`    | (Braze 内部使用のみ) このイベントが属する Canvas の ID          |
| `canvas_api_id`                        | `string`,&nbsp;`null`    | このイベントが属する Canvas の API ID                           |
| `canvas_variation_api_id`              | `string`,&nbsp;`null`    | このイベントが属する Canvas バリエーションの API ID                 |
| `canvas_step_api_id`                   | `string`,&nbsp;`null`    | このイベントが属するキャンバスステップの API ID                      |
| `canvas_step_message_variation_api_id` | `string`,&nbsp;`null`    | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID       |
| `gender`                               | `string`,&nbsp;`null`    | [PII] ユーザーの性別                                             |
| `country`                              | `string`,&nbsp;`null`    | [PII] ユーザーの国                                            |
| `timezone`                             | `string`,&nbsp;`null`    | ユーザーのタイムゾーン                                                 |
| `language`                             | `string`,&nbsp;`null`    | [PII] ユーザーの言語                                           |
| `revenue`                              | `int`,&nbsp;`null`       | 生成された USD 収益額 (セント単位で表示)               |
| `sf_created_at`                        | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時                        |
| `app_api_id` | `string`,&nbsp;`null` | このイベントが発生したアプリの API ID |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## メッセージ


### USERS_MESSAGES_BANNER_ABORT_SHARED {#USERS_MESSAGES_BANNER_ABORT_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ユーザー ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`app_group_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの BSON ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの API ID
`time` | `int` | イベントが発生した UNIX タイムスタンプ
`app_api_id` | `null,`&nbsp;`string` | このイベントが発生したアプリの API ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの BSON ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`device_id` | `null,`&nbsp;`string` | イベントが発生したデバイスの ID
`sdk_version` | `null,`&nbsp;`string` | イベント中に使用されていた Braze SDK のバージョン
`platform` | `null,`&nbsp;`string` | デバイスのプラットフォーム
`os_version` | `null,`&nbsp;`string` | デバイスのオペレーティングシステムのバージョン
`device_model` | `null,`&nbsp;`string` | デバイスのモデル
`resolution` | `null,`&nbsp;`string` | デバイスの解像度
`carrier` | `null,`&nbsp;`string` | デバイスの通信キャリア
`browser` | `null,`&nbsp;`string` | 開封が発生したデバイスのブラウザー（user_agent から抽出）
`ad_id` | `null,`&nbsp;`string` | [PII] 広告識別子
`ad_id_type` | `null,`&nbsp;`string` | ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id'] のいずれか
`ad_tracking_enabled` | `null, boolean` | デバイスで広告トラッキングが有効かどうか
`abort_type` | `null,`&nbsp;`string` | 中止のタイプ。['liquid_abort_message', 'quiet_hours', 'rate_limit'] のいずれか
`abort_log` | `null,`&nbsp;`string` | [PII] 中止の詳細を記述するログメッセージ（最大128文字）
`banner_placement_id` | `null,`&nbsp;`string` | 顧客が指定したバナー配置 ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_BANNER_CLICK_SHARED {#USERS_MESSAGES_BANNER_CLICK_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ユーザー ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`app_group_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの BSON ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの API ID
`time` | `int` | イベントが発生した UNIX タイムスタンプ
`app_api_id` | `null,`&nbsp;`string` | このイベントが発生したアプリの API ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの BSON ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`device_id` | `null,`&nbsp;`string` | イベントが発生したデバイスの ID
`sdk_version` | `null,`&nbsp;`string` | イベント中に使用されていた Braze SDK のバージョン
`platform` | `null,`&nbsp;`string` | デバイスのプラットフォーム
`os_version` | `null,`&nbsp;`string` | デバイスのオペレーティングシステムのバージョン
`device_model` | `null,`&nbsp;`string` | デバイスのモデル
`resolution` | `null,`&nbsp;`string` | デバイスの解像度
`carrier` | `null,`&nbsp;`string` | デバイスの通信キャリア
`browser` | `null,`&nbsp;`string` | 開封が発生したデバイスのブラウザー（user_agent から抽出）
`button_id` | `null,`&nbsp;`string` | クリックされたボタンの ID（このクリックがボタンのクリックを表す場合）
`ad_id` | `null,`&nbsp;`string` | [PII] 広告識別子
`ad_id_type` | `null,`&nbsp;`string` | ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id'] のいずれか
`ad_tracking_enabled` | `null, boolean` | デバイスで広告トラッキングが有効かどうか
`banner_placement_id` | `null,`&nbsp;`string` | 顧客が指定したバナー配置 ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_BANNER_IMPRESSION_SHARED {#USERS_MESSAGES_BANNER_IMPRESSION_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ユーザー ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`app_group_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの BSON ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの API ID
`time` | `int` | イベントが発生した UNIX タイムスタンプ
`app_api_id` | `null,`&nbsp;`string` | このイベントが発生したアプリの API ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの BSON ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`device_id` | `null,`&nbsp;`string` | イベントが発生したデバイスの ID
`sdk_version` | `null,`&nbsp;`string` | イベント中に使用されていた Braze SDK のバージョン
`platform` | `null,`&nbsp;`string` | デバイスのプラットフォーム
`os_version` | `null,`&nbsp;`string` | デバイスのオペレーティングシステムのバージョン
`device_model` | `null,`&nbsp;`string` | デバイスのモデル
`resolution` | `null,`&nbsp;`string` | デバイスの解像度
`carrier` | `null,`&nbsp;`string` | デバイスの通信キャリア
`browser` | `null,`&nbsp;`string` | 開封が発生したデバイスのブラウザー（user_agent から抽出）
`ad_id` | `null,`&nbsp;`string` | [PII] 広告識別子
`ad_id_type` | `null,`&nbsp;`string` | ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id'] のいずれか
`ad_tracking_enabled` | `null, boolean` | デバイスで広告トラッキングが有効かどうか
`banner_placement_id` | `null,`&nbsp;`string` | 顧客が指定したバナー配置 ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_CONTENTCARD_ABORT_SHARED {#USERS_MESSAGES_CONTENTCARD_ABORT_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`device_id` | `null,`&nbsp;`string` | ユーザーが匿名の場合、このユーザーに紐づけられた `device_id`
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが所属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`abort_type` | `null,`&nbsp;`string` | 中止のタイプ。['liquid_abort_message', 'quiet_hours', 'rate_limit'] のいずれか
`abort_log` | `null,`&nbsp;`string` | [PII] 中止の詳細を記述するログメッセージ（最大2,000文字）
`app_group_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_CONTENTCARD_CLICK_SHARED {#USERS_MESSAGES_CONTENTCARD_CLICK_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ID
`content_card_id` | `string` | このイベントを生成したカードの ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが所属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`app_api_id` | `null,`&nbsp;`string` | このイベントが発生したアプリの API ID
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`device_id` | `null,`&nbsp;`string` | イベントが発生したデバイスの ID
`sdk_version` | `null,`&nbsp;`string` | イベント中に使用されていた Braze SDK のバージョン
`platform` | `null,`&nbsp;`string` | デバイスのプラットフォーム
`os_version` | `null,`&nbsp;`string` | デバイスのオペレーティングシステムのバージョン
`device_model` | `null,`&nbsp;`string` | デバイスのモデル
`resolution` | `null,`&nbsp;`string` | デバイスの解像度
`carrier` | `null,`&nbsp;`string` | デバイスの通信キャリア
`browser` | `null,`&nbsp;`string` | デバイスのブラウザー
`ad_id` | `null,`&nbsp;`string` | [PII] 広告識別子
`ad_id_type` | `null,`&nbsp;`string` | `ios_idfa`、`google_ad_id`、`windows_ad_id`、または `roku_ad_id` のいずれか
`ad_tracking_enabled` | `null, boolean` | デバイスで広告トラッキングが有効かどうか
`app_group_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_CONTENTCARD_DISMISS_SHARED {#USERS_MESSAGES_CONTENTCARD_DISMISS_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ID
`content_card_id` | `string` | このイベントを生成したカードの ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが所属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`app_api_id` | `null,`&nbsp;`string` | このイベントが発生したアプリの API ID
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`device_id` | `null,`&nbsp;`string` | イベントが発生したデバイスの ID
`sdk_version` | `null,`&nbsp;`string` | イベント中に使用されていた Braze SDK のバージョン
`platform` | `null,`&nbsp;`string` | デバイスのプラットフォーム
`os_version` | `null,`&nbsp;`string` | デバイスのオペレーティングシステムのバージョン
`device_model` | `null,`&nbsp;`string` | デバイスのモデル
`resolution` | `null,`&nbsp;`string` | デバイスの解像度
`carrier` | `null,`&nbsp;`string` | デバイスの通信キャリア
`browser` | `null,`&nbsp;`string` | デバイスのブラウザー
`ad_id` | `null,`&nbsp;`string` | [PII] 広告識別子
`ad_id_type` | `null,`&nbsp;`string` | `ios_idfa`、`google_ad_id`、`windows_ad_id`、または `roku_ad_id` のいずれか
`ad_tracking_enabled` | `null, boolean` | デバイスで広告トラッキングが有効かどうか
`app_group_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_CONTENTCARD_IMPRESSION_SHARED {#USERS_MESSAGES_CONTENTCARD_IMPRESSION_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ID
`content_card_id` | `string` | このイベントを生成したカードの ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが所属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`app_api_id` | `null,`&nbsp;`string` | このイベントが発生したアプリの API ID
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`device_id` | `null,`&nbsp;`string` | イベントが発生したデバイスの ID
`sdk_version` | `null,`&nbsp;`string` | イベント中に使用されていた Braze SDK のバージョン
`platform` | `null,`&nbsp;`string` | デバイスのプラットフォーム
`os_version` | `null,`&nbsp;`string` | デバイスのオペレーティングシステムのバージョン
`device_model` | `null,`&nbsp;`string` | デバイスのモデル
`resolution` | `null,`&nbsp;`string` | デバイスの解像度
`carrier` | `null,`&nbsp;`string` | デバイスの通信キャリア
`browser` | `null,`&nbsp;`string` | デバイスのブラウザー
`ad_id` | `null,`&nbsp;`string` | [PII] 広告識別子
`ad_id_type` | `null,`&nbsp;`string` | `ios_idfa`、`google_ad_id`、`windows_ad_id`、または `roku_ad_id` のいずれか
`ad_tracking_enabled` | `null, boolean` | デバイスで広告トラッキングが有効かどうか
`app_group_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_CONTENTCARD_SEND_SHARED {#USERS_MESSAGES_CONTENTCARD_SEND_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`device_id` | `null,`&nbsp;`string` | ユーザーが匿名の場合、このユーザーに紐づけられた `device_id`
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが所属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`content_card_id` | `string` | このイベントを生成したカードの ID
`app_group_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの BSON ID
`message_extras` | `null,`&nbsp;`string` | [PII] Liquid レンダリング中にタグ付けされたキーと値のペアの JSON 文字列
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_ABORT_SHARED {#USERS_MESSAGES_EMAIL_ABORT_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`device_id` | `null,`&nbsp;`string` | ユーザーが匿名の場合、このユーザーに紐づけられた `device_id`
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが所属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`email_address` | `string` | [PII] ユーザーのメールアドレス
`ip_pool` | `null,`&nbsp;`string` | メール送信に使用された IP プール
`abort_type` | `null,`&nbsp;`string` | 中止のタイプ。['liquid_abort_message', 'quiet_hours', 'rate_limit'] のいずれか
`abort_log` | `null,`&nbsp;`string` | [PII] 中止の詳細を記述するログメッセージ（最大2,000文字）
`app_group_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_BOUNCE_SHARED {#USERS_MESSAGES_EMAIL_BOUNCE_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`device_id` | `null,`&nbsp;`string` | ユーザーが匿名の場合、このユーザーに紐づけられた `device_id`
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが所属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`email_address` | `string` | [PII] ユーザーのメールアドレス
`sending_ip` | `null,`&nbsp;`string` | メール送信に使用された IP アドレス
`ip_pool` | `null,`&nbsp;`string` | メール送信に使用された IP プール
`bounce_reason` | `null,`&nbsp;`string` | [PII] このバウンスイベントで受信した SMTP 理由コードとユーザーフレンドリーなメッセージ
`esp` | `null,`&nbsp;`string` | イベントに関連するメールサービスプロバイダー (ESP)（SparkPost、SendGrid、または Amazon SES）
`from_domain` | `null,`&nbsp;`string` | メールの送信ドメイン
`is_drop` | `null, boolean` | このイベントがドロップイベントとしてカウントされることを示します
`app_group_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_CLICK_SHARED {#USERS_MESSAGES_EMAIL_CLICK_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`device_id` | `null,`&nbsp;`string` | ユーザーが匿名の場合、このユーザーに紐づけられた `device_id`
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが所属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`email_address` | `string` | [PII] ユーザーのメールアドレス
`url` | `null,`&nbsp;`string` | ユーザーがクリックした URL
`user_agent` | `null,`&nbsp;`string` | クリックが発生したユーザーエージェント
`ip_pool` | `null,`&nbsp;`string` | メール送信に使用された IP プール
`link_id` | `null,`&nbsp;`string` | Braze が作成した、クリックされたリンクの一意の ID
`link_alias` | `null,`&nbsp;`string` | このリンク ID に関連付けられたエイリアス
`esp` | `null,`&nbsp;`string` | イベントに関連するメールサービスプロバイダー (ESP)（SparkPost、SendGrid、または Amazon SES）
`from_domain` | `null,`&nbsp;`string` | メールの送信ドメイン
`is_amp` | `null, boolean` | これが AMP イベントであることを示します
`app_group_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの BSON ID
`is_suspected_bot_click` | `null, boolean` | このイベントがボットイベントとして処理されたかどうか
`suspected_bot_click_reason` | `null, object` | このイベントがボットとして分類された理由
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_EMAIL_DEFERRAL_SHARED {#USERS_MESSAGES_EMAIL_DEFERRAL_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`time` | `int` | イベントが発生した UNIX タイムスタンプ
`user_id` | `string` | このイベントを実行したユーザーの Braze ユーザー ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`app_group_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの BSON ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの API ID
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの BSON ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の BSON ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`email_address` | `null,`&nbsp;`string` | [PII] ユーザーのメールアドレス
`recipient_domain` | `null,`&nbsp;`string` | 受信者のメールドメイン
`esp` | `null,`&nbsp;`string` | イベントに関連するメールサービスプロバイダー (ESP)（Sparkpost、Sendgrid、または Amazon SES）
`from_domain` | `null,`&nbsp;`string` | メールの送信ドメイン
`ip_pool` | `null,`&nbsp;`string` | メール送信に使用された IP プール
`sending_ip` | `null,`&nbsp;`string` | メール送信に使用された IP アドレス
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`deferral_reason` | `null,`&nbsp;`string` | [PII] この遅延イベントで受信した SMTP 理由コードとユーザーフレンドリーなメッセージ
`attempt_count` | `null, int` | メッセージの送信試行回数
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_DELIVERY_SHARED {#USERS_MESSAGES_EMAIL_DELIVERY_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`device_id` | `null,`&nbsp;`string` | ユーザーが匿名の場合、このユーザーに紐づけられた `device_id`
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが所属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`email_address` | `string` | [PII] ユーザーのメールアドレス
`sending_ip` | `null,`&nbsp;`string` | メール送信に使用された IP アドレス
`ip_pool` | `null,`&nbsp;`string` | メール送信に使用された IP プール
`esp` | `null,`&nbsp;`string` | イベントに関連するメールサービスプロバイダー (ESP)（SparkPost、SendGrid、または Amazon SES）
`from_domain` | `null,`&nbsp;`string` | メールの送信ドメイン
`app_group_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_MARKASSPAM_SHARED {#USERS_MESSAGES_EMAIL_MARKASSPAM_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`device_id` | `null,`&nbsp;`string` | ユーザーが匿名の場合、このユーザーに紐づけられた `device_id`
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが所属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`email_address` | `string` | [PII] ユーザーのメールアドレス
`user_agent` | `null,`&nbsp;`string` | スパム報告が発生したユーザーエージェント
`ip_pool` | `null,`&nbsp;`string` | メール送信に使用された IP プール
`esp` | `null,`&nbsp;`string` | イベントに関連するメールサービスプロバイダー (ESP)（SparkPost、SendGrid、または Amazon SES）
`from_domain` | `null,`&nbsp;`string` | メールの送信ドメイン
`app_group_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_OPEN_SHARED {#USERS_MESSAGES_EMAIL_OPEN_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`device_id` | `null,`&nbsp;`string` | ユーザーが匿名の場合、このユーザーに紐づけられた `device_id`
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが所属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`email_address` | `string` | [PII] ユーザーのメールアドレス
`user_agent` | `null,`&nbsp;`string` | 開封が発生したユーザーエージェント
`ip_pool` | `null,`&nbsp;`string` | メール送信に使用された IP プール
`machine_open` | `null,`&nbsp;`string` | ユーザーの操作なしに開封イベントがトリガーされた場合（例：メールプライバシー保護が有効な Apple デバイスなど）に 'true' が設定されます。値はより詳細な情報を提供するために変更される場合があります。
`esp` | `null,`&nbsp;`string` | イベントに関連するメールサービスプロバイダー (ESP)（SparkPost、SendGrid、または Amazon SES）
`from_domain` | `null,`&nbsp;`string` | メールの送信ドメイン
`is_amp` | `null, boolean` | これが AMP イベントであることを示します
`app_group_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_SEND_SHARED {#USERS_MESSAGES_EMAIL_SEND_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`device_id` | `null,`&nbsp;`string` | ユーザーが匿名の場合、このユーザーに紐づけられた `device_id`
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが所属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`email_address` | `string` | [PII] ユーザーのメールアドレス
`ip_pool` | `null,`&nbsp;`string` | メール送信に使用された IP プール
`message_extras` | `null,`&nbsp;`string` | [PII] Liquid レンダリング中にタグ付けされたキーと値のペアの JSON 文字列
`esp` | `null,`&nbsp;`string` | イベントに関連するメールサービスプロバイダー (ESP)（SparkPost、SendGrid、または Amazon SES）
`from_domain` | `null,`&nbsp;`string` | メールの送信ドメイン
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
`app_group_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの BSON ID
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_SOFTBOUNCE_SHARED {#USERS_MESSAGES_EMAIL_SOFTBOUNCE_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`device_id` | `null,`&nbsp;`string` | ユーザーが匿名の場合、このユーザーに紐づけられた `device_id`
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが所属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`email_address` | `string` | [PII] ユーザーのメールアドレス
`sending_ip` | `null,`&nbsp;`string` | メール送信に使用された IP アドレス
`ip_pool` | `null,`&nbsp;`string` | メール送信に使用された IP プール
`bounce_reason` | `null,`&nbsp;`string` | [PII] このバウンスイベントで受信した SMTP 理由コードとユーザーフレンドリーなメッセージ
`esp` | `null,`&nbsp;`string` | イベントに関連するメールサービスプロバイダー (ESP)（SparkPost、SendGrid、または Amazon SES）
`from_domain` | `null,`&nbsp;`string` | メールの送信ドメイン
`app_group_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED {#USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`device_id` | `null,`&nbsp;`string` | ユーザーが匿名の場合、このユーザーに紐づけられた `device_id`
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが所属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`email_address` | `string` | [PII] ユーザーのメールアドレス
`ip_pool` | `null,`&nbsp;`string` | メール送信に使用された IP プール
`app_group_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_RETRY_SHARED {#USERS_MESSAGES_EMAIL_RETRY_SHARED}

{% alert note %}
このテーブルは Snowflake データシェアリングでのみ利用可能です。
{% endalert %}

このイベントは、メッセージの優先度が下げられたりフリークエンシーキャップが適用されたりして、設定されたリトライ時間枠内で後から再試行された場合に発生します。

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | [PII] このイベントを実行したユーザーの Braze ユーザー ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`app_group_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの BSON ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの API ID
`time` | `int` | イベントが発生した UNIX タイムスタンプ
`retry_type` | `null,`&nbsp;`string` | リトライのタイプ
`retry_log` | `null,`&nbsp;`string` | リトライの詳細を記述するログメッセージ
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの BSON ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の BSON ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`email_address` | `null,`&nbsp;`string` | [PII] ユーザーのメールアドレス
`ip_pool` | `null,`&nbsp;`string` | メール送信に使用された IP プール
`device_id` | `null,`&nbsp;`string` | イベントが発生したデバイスの ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_FEATUREFLAG_IMPRESSION_SHARED {#USERS_MESSAGES_FEATUREFLAG_IMPRESSION_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`app_api_id` | `null,`&nbsp;`string` | このイベントが発生したアプリの API ID
`app_group_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの BSON ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの API ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの BSON ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の BSON ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`feature_flag_id_name` | `null,`&nbsp;`string` | フィーチャーフラグのロールアウト識別子
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`device_id` | `null,`&nbsp;`string` | イベントが発生したデバイスの ID
`time` | `int` | イベントが発生した UNIX タイムスタンプ
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`browser` | `null,`&nbsp;`string` | 開封が発生したデバイスのブラウザー（user_agent から抽出）
`carrier` | `null,`&nbsp;`string` | デバイスの通信キャリア
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`device_model` | `null,`&nbsp;`string` | デバイスのモデル
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`os_version` | `null,`&nbsp;`string` | デバイスのオペレーティングシステムのバージョン
`platform` | `null,`&nbsp;`string` | デバイスのプラットフォーム
`resolution` | `null,`&nbsp;`string` | デバイスの解像度
`sdk_version` | `null,`&nbsp;`string` | イベント中に使用されていた Braze SDK のバージョン
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`user_id` | `string` | このイベントを実行したユーザーの Braze ユーザー ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_INAPPMESSAGE_ABORT_SHARED {#USERS_MESSAGES_INAPPMESSAGE_ABORT_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが所属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`app_api_id` | `null,`&nbsp;`string` | このイベントが発生したアプリの API ID
`card_api_id` | `null,`&nbsp;`string` | カードの API ID
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`device_id` | `null,`&nbsp;`string` | イベントが発生したデバイスの ID
`sdk_version` | `null,`&nbsp;`string` | イベント中に使用されていた Braze SDK のバージョン
`platform` | `null,`&nbsp;`string` | デバイスのプラットフォーム
`os_version` | `null,`&nbsp;`string` | デバイスのオペレーティングシステムのバージョン
`device_model` | `null,`&nbsp;`string` | デバイスのモデル
`resolution` | `null,`&nbsp;`string` | デバイスの解像度
`carrier` | `null,`&nbsp;`string` | デバイスの通信キャリア
`browser` | `null,`&nbsp;`string` | デバイスのブラウザー
`version` | `string` | アプリ内メッセージのバージョン（レガシーまたはトリガー）
`ad_id` | `null,`&nbsp;`string` | [PII] 広告識別子
`ad_id_type` | `null,`&nbsp;`string` | `ios_idfa`、`google_ad_id`、`windows_ad_id`、または `roku_ad_id` のいずれか
`ad_tracking_enabled` | `null, boolean` | デバイスで広告トラッキングが有効かどうか
`abort_type` | `null,`&nbsp;`string` | 中止のタイプ。['liquid_abort_message', 'quiet_hours', 'rate_limit'] のいずれか
`abort_log` | `null,`&nbsp;`string` | [PII] 中止の詳細を記述するログメッセージ（最大2,000文字）
`app_group_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_INAPPMESSAGE_CLICK_SHARED {#USERS_MESSAGES_INAPPMESSAGE_CLICK_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが所属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`app_api_id` | `null,`&nbsp;`string` | このイベントが発生したアプリの API ID
`card_api_id` | `null,`&nbsp;`string` | カードの API ID
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`device_id` | `null,`&nbsp;`string` | イベントが発生したデバイスの ID
`sdk_version` | `null,`&nbsp;`string` | イベント中に使用されていた Braze SDK のバージョン
`platform` | `null,`&nbsp;`string` | デバイスのプラットフォーム
`os_version` | `null,`&nbsp;`string` | デバイスのオペレーティングシステムのバージョン
`device_model` | `null,`&nbsp;`string` | デバイスのモデル
`resolution` | `null,`&nbsp;`string` | デバイスの解像度
`carrier` | `null,`&nbsp;`string` | デバイスの通信キャリア
`browser` | `null,`&nbsp;`string` | デバイスのブラウザー
`version` | `string` | アプリ内メッセージのバージョン（レガシーまたはトリガー）
`button_id` | `null,`&nbsp;`string` | クリックされたボタンの ID（このクリックがボタンのクリックを表す場合）
`ad_id` | `null,`&nbsp;`string` | [PII] 広告識別子
`ad_id_type` | `null,`&nbsp;`string` | `ios_idfa`、`google_ad_id`、`windows_ad_id`、または `roku_ad_id` のいずれか
`ad_tracking_enabled` | `null, boolean` | デバイスで広告トラッキングが有効かどうか
`app_group_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_INAPPMESSAGE_IMPRESSION_SHARED {#USERS_MESSAGES_INAPPMESSAGE_IMPRESSION_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが所属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`app_api_id` | `null,`&nbsp;`string` | このイベントが発生したアプリの API ID
`card_api_id` | `null,`&nbsp;`string` | カードの API ID
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`device_id` | `null,`&nbsp;`string` | イベントが発生したデバイスの ID
`sdk_version` | `null,`&nbsp;`string` | イベント中に使用されていた Braze SDK のバージョン
`platform` | `null,`&nbsp;`string` | デバイスのプラットフォーム
`os_version` | `null,`&nbsp;`string` | デバイスのオペレーティングシステムのバージョン
`device_model` | `null,`&nbsp;`string` | デバイスのモデル
`resolution` | `null,`&nbsp;`string` | デバイスの解像度
`carrier` | `null,`&nbsp;`string` | デバイスの通信キャリア
`browser` | `null,`&nbsp;`string` | デバイスのブラウザー
`version` | `string` | アプリ内メッセージのバージョン（レガシーまたはトリガー）
`ad_id` | `null,`&nbsp;`string` | [PII] 広告識別子
`ad_id_type` | `null,`&nbsp;`string` | `ios_idfa`、`google_ad_id`、`windows_ad_id`、または `roku_ad_id` のいずれか
`ad_tracking_enabled` | `null, boolean` | デバイスで広告トラッキングが有効かどうか
`app_group_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの BSON ID
`message_extras` | `null,`&nbsp;`string` | [PII] Liquid レンダリング中にタグ付けされたキーと値のペアの JSON 文字列
`locale_key` | `null,`&nbsp;`string` | [PII] このメッセージの作成に使用された翻訳に対応するキー（例：'en-us'）（デフォルトの場合は null）
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_LINE_ABORT_SHARED {#USERS_MESSAGES_LINE_ABORT_SHARED}

フィールド | タイプ | 説明
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの API ID
`app_group_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの BSON ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`id` | `string` | このイベントのグローバルな一意の ID
`time` | `int` | イベントが発生した UNIX タイムスタンプ
`user_id` | `string` | このイベントを実行したユーザーの Braze ユーザー ID
`abort_log` | `null,`&nbsp;`string` | [PII] 中止の詳細を記述するログメッセージ（最大128文字）
`abort_type` | `null,`&nbsp;`string` | 中止のタイプ。['liquid_abort_message', 'quiet_hours', 'rate_limit'] のいずれか
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`device_id` | `null,`&nbsp;`string` | イベントが発生したデバイスの ID
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`line_channel_id` | `null,`&nbsp;`string` | メッセージの送受信先の LINE チャネル ID
`line_channel_name` | `null,`&nbsp;`string` | メッセージの送受信先の LINE チャネル名
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`native_line_id` | `null,`&nbsp;`string` | [PII] メッセージの送受信元のユーザーの LINE ID
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`subscription_group_api_id` | `string` | サブスクリプショングループの API ID
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`campaign_name` | `null,`&nbsp;`string` | キャンペーンの名前
`canvas_step_name` | `null,`&nbsp;`string` | キャンバスステップの名前
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の API ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_LINE_CLICK_SHARED {#USERS_MESSAGES_LINE_CLICK_SHARED}

フィールド | タイプ | 説明
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの API ID
`app_group_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの BSON ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`id` | `string` | このイベントのグローバルな一意の ID
`time` | `int` | イベントが発生した UNIX タイムスタンプ
`user_id` | `string` | このイベントを実行したユーザーの Braze ユーザー ID
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`native_line_id` | `null,`&nbsp;`string` | [PII] メッセージの送受信元のユーザーの LINE ID
`line_channel_id` | `null,`&nbsp;`string` | メッセージの送受信先の LINE チャネル ID
`line_channel_name` | `null,`&nbsp;`string` | メッセージの送受信先の LINE チャネル名
`subscription_group_api_id` | `string` | サブスクリプショングループの API ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`campaign_name` | `null,`&nbsp;`string` | キャンペーンの名前
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`canvas_step_name` | `null,`&nbsp;`string` | キャンバスステップの名前
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`device_id` | `null,`&nbsp;`string` | イベントが発生したデバイスの ID
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`is_suspected_bot_click` | `null, boolean` | このイベントがボットイベントとして処理されたかどうか
`short_url` | `null,`&nbsp;`string` | クリックされた短縮 URL
`url` | `null,`&nbsp;`string` | ユーザーがクリックした URL
`user_agent` | `null,`&nbsp;`string` | スパム報告が発生したユーザーエージェント
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_LINE_INBOUNDRECEIVE_SHARED {#USERS_MESSAGES_LINE_INBOUNDRECEIVE_SHARED}

フィールド | タイプ | 説明
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの API ID
`app_group_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの BSON ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`id` | `string` | このイベントのグローバルな一意の ID
`time` | `int` | イベントが発生した UNIX タイムスタンプ
`user_id` | `string` | このイベントを実行したユーザーの Braze ユーザー ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`campaign_name` | `null,`&nbsp;`string` | キャンペーンの名前
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`canvas_step_name` | `null,`&nbsp;`string` | キャンバスステップの名前
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`device_id` | `null,`&nbsp;`string` | イベントが発生したデバイスの ID
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`line_channel_id` | `null,`&nbsp;`string` | メッセージの送受信先の LINE チャネル ID
`line_channel_name` | `null,`&nbsp;`string` | メッセージの送受信先の LINE チャネル名
`media_id` | `null,`&nbsp;`string` | LINE から受信メディアを取得するために使用できる LINE 生成 ID
`message_body` | `null,`&nbsp;`string` | ユーザーからの入力応答
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`native_line_id` | `null,`&nbsp;`string` | [PII] メッセージの送受信元のユーザーの LINE ID
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`subscription_group_api_id` | `string` | サブスクリプショングループの API ID
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_LINE_SEND_SHARED {#USERS_MESSAGES_LINE_SEND_SHARED}

フィールド | タイプ | 説明
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの API ID
`app_group_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの BSON ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`id` | `string` | このイベントのグローバルな一意の ID
`time` | `int` | イベントが発生した UNIX タイムスタンプ
`user_id` | `string` | このイベントを実行したユーザーの Braze ユーザー ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`campaign_name` | `null,`&nbsp;`string` | キャンペーンの名前
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`canvas_step_name` | `null,`&nbsp;`string` | キャンバスステップの名前
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`device_id` | `null,`&nbsp;`string` | イベントが発生したデバイスの ID
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`line_channel_id` | `null,`&nbsp;`string` | メッセージの送受信先の LINE チャネル ID
`line_channel_name` | `null,`&nbsp;`string` | メッセージの送受信先の LINE チャネル名
`message_extras` | `null,`&nbsp;`string` | [PII] Liquid レンダリング中にタグ付けされたキーと値のペアの JSON 文字列
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`native_line_id` | `null,`&nbsp;`string` | [PII] メッセージの送受信元のユーザーの LINE ID
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`subscription_group_api_id` | `string` | サブスクリプショングループの API ID
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_LINE_RETRY_SHARED {#USERS_MESSAGES_LINE_RETRY_SHARED}

{% alert note %}
このテーブルは Snowflake データシェアリングでのみ利用可能です。
{% endalert %}

このイベントは、メッセージの優先度が下げられたりフリークエンシーキャップが適用されたりして、設定されたリトライ時間枠内で後から再試行された場合に発生します。

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | [PII] このイベントを実行したユーザーの Braze ユーザー ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`app_group_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの BSON ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの API ID
`time` | `int` | イベントが発生した UNIX タイムスタンプ
`retry_type` | `null,`&nbsp;`string` | リトライのタイプ
`retry_log` | `null,`&nbsp;`string` | リトライの詳細を記述するログメッセージ
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの BSON ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の BSON ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`device_id` | `null,`&nbsp;`string` | イベントが発生したデバイスの ID
`line_channel_id` | `null,`&nbsp;`string` | メッセージの送受信先の LINE チャネル ID
`line_channel_name` | `null,`&nbsp;`string` | メッセージの送受信先の LINE チャネル名
`native_line_id` | `null,`&nbsp;`string` | [PII] メッセージの送受信元のユーザーの LINE ID
`subscription_group_api_id` | `null,`&nbsp;`string` | サブスクリプショングループの API ID
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_LIVEACTIVITY_OUTCOME_SHARED {#USERS_MESSAGES_LIVEACTIVITY_OUTCOME_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ユーザー ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`time` | `int` | イベントが発生した UNIX タイムスタンプ
`app_group_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの BSON ID
`activity_id` | `null,`&nbsp;`string` | Live Activity の識別子
`activity_attributes_type` | `null,`&nbsp;`string` | Live Activity の属性タイプ
`push_to_start_token` | `null,`&nbsp;`string` | Live Activity の push to start トークン
`update_token` | `null,`&nbsp;`string` | Live Activity の更新トークン
`live_activity_event_type` | `null,`&nbsp;`string` | Live Activity のイベントタイプ。['start', 'update', 'end'] のいずれか
`live_activity_event_outcome` | `null,`&nbsp;`string` | Live Activity イベントの結果
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの API ID
`app_api_id` | `null,`&nbsp;`string` | このイベントが発生したアプリの API ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_LIVEACTIVITY_SEND_SHARED {#USERS_MESSAGES_LIVEACTIVITY_SEND_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ユーザー ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`time` | `int` | イベントが発生した UNIX タイムスタンプ
`app_group_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの BSON ID
`activity_id` | `null,`&nbsp;`string` | Live Activity の識別子
`activity_attributes_type` | `null,`&nbsp;`string` | Live Activity の属性タイプ
`push_to_start_token` | `null,`&nbsp;`string` | Live Activity の push to start トークン
`update_token` | `null,`&nbsp;`string` | Live Activity の更新トークン
`live_activity_event_type` | `null,`&nbsp;`string` | Live Activity のイベントタイプ。['start', 'update', 'end'] のいずれか
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの API ID
`app_api_id` | `null,`&nbsp;`string` | このイベントが発生したアプリの API ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_NEWSFEEDCARD_ABORT_SHARED {#USERS_MESSAGES_NEWSFEEDCARD_ABORT_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ユーザー ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`app_group_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの BSON ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの API ID
`time` | `int` | イベントが発生した UNIX タイムスタンプ
`app_api_id` | `null,`&nbsp;`string` | このイベントが発生したアプリの API ID
`card_api_id` | `null,`&nbsp;`string` | カードの API ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`device_id` | `null,`&nbsp;`string` | イベントが発生したデバイスの ID
`sdk_version` | `null,`&nbsp;`string` | イベント中に使用されていた Braze SDK のバージョン
`platform` | `null,`&nbsp;`string` | デバイスのプラットフォーム
`os_version` | `null,`&nbsp;`string` | デバイスのオペレーティングシステムのバージョン
`device_model` | `null,`&nbsp;`string` | デバイスのモデル
`resolution` | `null,`&nbsp;`string` | デバイスの解像度
`carrier` | `null,`&nbsp;`string` | デバイスの通信キャリア
`browser` | `null,`&nbsp;`string` | 開封が発生したデバイスのブラウザー（user_agent から抽出）
`abort_type` | `null,`&nbsp;`string` | 中止のタイプ。['liquid_abort_message', 'quiet_hours', 'rate_limit'] のいずれか
`abort_log` | `null,`&nbsp;`string` | [PII] 中止の詳細を記述するログメッセージ（最大128文字）
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_NEWSFEEDCARD_CLICK_SHARED {#USERS_MESSAGES_NEWSFEEDCARD_CLICK_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ユーザー ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`app_group_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの BSON ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの API ID
`time` | `int` | イベントが発生した UNIX タイムスタンプ
`app_api_id` | `null,`&nbsp;`string` | このイベントが発生したアプリの API ID
`card_api_id` | `null,`&nbsp;`string` | カードの API ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`device_id` | `null,`&nbsp;`string` | イベントが発生したデバイスの ID
`sdk_version` | `null,`&nbsp;`string` | イベント中に使用されていた Braze SDK のバージョン
`platform` | `null,`&nbsp;`string` | デバイスのプラットフォーム
`os_version` | `null,`&nbsp;`string` | デバイスのオペレーティングシステムのバージョン
`device_model` | `null,`&nbsp;`string` | デバイスのモデル
`resolution` | `null,`&nbsp;`string` | デバイスの解像度
`carrier` | `null,`&nbsp;`string` | デバイスの通信キャリア
`browser` | `null,`&nbsp;`string` | 開封が発生したデバイスのブラウザー（user_agent から抽出）
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_NEWSFEEDCARD_IMPRESSION_SHARED {#USERS_MESSAGES_NEWSFEEDCARD_IMPRESSION_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ユーザー ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`app_group_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの BSON ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの API ID
`time` | `int` | イベントが発生した UNIX タイムスタンプ
`app_api_id` | `null,`&nbsp;`string` | このイベントが発生したアプリの API ID
`card_api_id` | `null,`&nbsp;`string` | カードの API ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`device_id` | `null,`&nbsp;`string` | イベントが発生したデバイスの ID
`sdk_version` | `null,`&nbsp;`string` | イベント中に使用されていた Braze SDK のバージョン
`platform` | `null,`&nbsp;`string` | デバイスのプラットフォーム
`os_version` | `null,`&nbsp;`string` | デバイスのオペレーティングシステムのバージョン
`device_model` | `null,`&nbsp;`string` | デバイスのモデル
`resolution` | `null,`&nbsp;`string` | デバイスの解像度
`carrier` | `null,`&nbsp;`string` | デバイスの通信キャリア
`browser` | `null,`&nbsp;`string` | 開封が発生したデバイスのブラウザー（user_agent から抽出）
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_PUSHNOTIFICATION_ABORT_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_ABORT_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`device_id` | `null,`&nbsp;`string` | 配信を試みた `device_id`
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが所属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`app_api_id` | `null,`&nbsp;`string` | このイベントが発生したアプリの API ID
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`platform` | `string` | デバイスのプラットフォーム
`abort_type` | `null,`&nbsp;`string` | 中止のタイプ。['liquid_abort_message', 'quiet_hours', 'rate_limit'] のいずれか
`abort_log` | `null,`&nbsp;`string` | [PII] 中止の詳細を記述するログメッセージ（最大2,000文字）
`app_group_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_PUSHNOTIFICATION_BOUNCE_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_BOUNCE_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`push_token` | `null,`&nbsp;`string` | バウンスしたプッシュトークン
`device_id` | `null,`&nbsp;`string` | 配信を試みてバウンスした `device_id`
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが所属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`app_api_id` | `null,`&nbsp;`string` | このイベントが発生したアプリの API ID
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`platform` | `null,`&nbsp;`string` | デバイスのプラットフォーム
`ad_id` | `null,`&nbsp;`string` | [PII] 配信を試みたデバイスの広告 ID
`ad_id_type` | `null,`&nbsp;`string` | 広告 ID のタイプ
`ad_tracking_enabled` | `null, boolean` | 広告のトラッキングが有効かどうか
`app_group_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_PUSHNOTIFICATION_INFLUENCEDOPEN_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_INFLUENCEDOPEN_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが所属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`app_api_id` | `null,`&nbsp;`string` | このイベントが発生したアプリの API ID
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`device_id` | `null,`&nbsp;`string` | イベントが発生したデバイスの ID
`sdk_version` | `null,`&nbsp;`string` | イベント中に使用されていた Braze SDK のバージョン
`platform` | `null,`&nbsp;`string` | デバイスのプラットフォーム
`os_version` | `null,`&nbsp;`string` | デバイスのオペレーティングシステムのバージョン
`device_model` | `null,`&nbsp;`string` | デバイスのモデル
`resolution` | `null,`&nbsp;`string` | デバイスの解像度
`carrier` | `null,`&nbsp;`string` | デバイスの通信キャリア
`browser` | `null,`&nbsp;`string` | デバイスのブラウザー
`app_group_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_PUSHNOTIFICATION_IOSFOREGROUND_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_IOSFOREGROUND_SHARED}

{% alert important %}
このイベントは [Swift SDK](https://github.com/braze-inc/braze-swift-sdk) ではサポートされておらず、[Obj-C SDK](https://github.com/Appboy/appboy-ios-sdk) では非推奨です。
{% endalert %}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが所属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`app_api_id` | `null,`&nbsp;`string` | このイベントが発生したアプリの API ID
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`device_id` | `null,`&nbsp;`string` | イベントが発生したデバイスの ID
`sdk_version` | `null,`&nbsp;`string` | イベント中に使用されていた Braze SDK のバージョン
`platform` | `null,`&nbsp;`string` | デバイスのプラットフォーム
`os_version` | `null,`&nbsp;`string` | デバイスのオペレーティングシステムのバージョン
`device_model` | `null,`&nbsp;`string` | デバイスのモデル
`resolution` | `null,`&nbsp;`string` | デバイスの解像度
`carrier` | `null,`&nbsp;`string` | デバイスの通信キャリア
`browser` | `null,`&nbsp;`string` | デバイスのブラウザー
`ad_id` | `null,`&nbsp;`string` | [PII] 配信を試みたデバイスの広告 ID
`ad_id_type` | `null,`&nbsp;`string` | 広告 ID のタイプ
`ad_tracking_enabled` | `null, boolean` | 広告のトラッキングが有効かどうか
`app_group_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_PUSHNOTIFICATION_OPEN_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_OPEN_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが所属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`app_api_id` | `null,`&nbsp;`string` | このイベントが発生したアプリの API ID
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`device_id` | `null,`&nbsp;`string` | イベントが発生したデバイスの ID
`sdk_version` | `null,`&nbsp;`string` | イベント中に使用されていた Braze SDK のバージョン
`platform` | `null,`&nbsp;`string` | デバイスのプラットフォーム
`os_version` | `null,`&nbsp;`string` | デバイスのオペレーティングシステムのバージョン
`device_model` | `null,`&nbsp;`string` | デバイスのモデル
`resolution` | `null,`&nbsp;`string` | デバイスの解像度
`carrier` | `null,`&nbsp;`string` | デバイスの通信キャリア
`browser` | `null,`&nbsp;`string` | デバイスのブラウザー
`button_string` | `null,`&nbsp;`string` | クリックされたプッシュ通知ボタンの識別子（button_string）。ボタンクリックでない場合は null
`button_action_type` | `null,`&nbsp;`string` | プッシュ通知ボタンのアクションタイプ。[URI, DEEP_LINK, NONE, CLOSE] のいずれか。ボタンクリックでない場合は null
`slide_id` | `null,`&nbsp;`string` | ユーザーがクリックしたプッシュカルーセルスライドのスライド識別子
`slide_action_type` | `null,`&nbsp;`string` | プッシュカルーセルスライドのアクションタイプ
`ad_id` | `null,`&nbsp;`string` | [PII] 配信を試みたデバイスの広告 ID
`ad_id_type` | `null,`&nbsp;`string` | 広告 ID のタイプ
`ad_tracking_enabled` | `null, boolean` | 広告のトラッキングが有効かどうか
`app_group_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_PUSHNOTIFICATION_SEND_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_SEND_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`push_token` | `null,`&nbsp;`string` | 配信を試みたプッシュトークン
`device_id` | `null,`&nbsp;`string` | 配信を試みた `device_id`
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが所属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`app_api_id` | `null,`&nbsp;`string` | このイベントが発生したアプリの API ID
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`platform` | `string` | デバイスのプラットフォーム
`ad_id` | `null,`&nbsp;`string` | [PII] 配信を試みたデバイスの広告 ID
`ad_id_type` | `null,`&nbsp;`string` | 広告 ID のタイプ
`ad_tracking_enabled` | `null, boolean` | 広告のトラッキングが有効かどうか
`app_group_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの BSON ID
`message_extras` | `null,`&nbsp;`string` | [PII] Liquid レンダリング中にタグ付けされたキーと値のペアの JSON 文字列
`is_sampled` | `null,`&nbsp;`string` | プッシュ送信がサンプリングされ、配信イベントが期待されるかどうかを示します
`locale_key` | `null,`&nbsp;`string` | [PII] このメッセージの作成に使用された翻訳に対応するキー（例：'en-us'）（デフォルトの場合は null）
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_RCS_ABORT_SHARED {#USERS_MESSAGES_RCS_ABORT_SHARED}

フィールド | タイプ | 説明
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの API ID
`app_group_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの BSON ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`id` | `string` | このイベントのグローバルな一意の ID
`time` | `int` | イベントが発生した UNIX タイムスタンプ
`user_id` | `string` | このイベントを実行したユーザーの Braze ユーザー ID
`abort_log` | `null,`&nbsp;`string` | [PII] 中止の詳細を記述するログメッセージ（最大128文字）
`abort_type` | `null,`&nbsp;`string` | 中止のタイプ。['liquid_abort_message', 'quiet_hours', 'rate_limit'] のいずれか
`campaign_name` | `null,`&nbsp;`string` | キャンペーンの名前
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の BSON ID
`canvas_name` | `null,`&nbsp;`string` | Canvas の名前
`canvas_step_name` | `null,`&nbsp;`string` | キャンバスステップの名前
`canvas_variation_name` | `null,`&nbsp;`string` | このユーザーが受信した Canvas バリエーションの名前
`message_variation_name` | `null,`&nbsp;`string` | メッセージバリエーションの名前
`subscription_group_api_id` | `string` | サブスクリプショングループの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_RCS_CLICK_SHARED {#USERS_MESSAGES_RCS_CLICK_SHARED}

フィールド | タイプ | 説明
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの API ID
`app_group_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの BSON ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`id` | `string` | このイベントのグローバルな一意の ID
`time` | `int` | イベントが発生した UNIX タイムスタンプ
`user_id` | `string` | このイベントを実行したユーザーの Braze ユーザー ID
`campaign_name` | `null,`&nbsp;`string` | キャンペーンの名前
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の BSON ID
`canvas_name` | `null,`&nbsp;`string` | Canvas の名前
`canvas_step_name` | `null,`&nbsp;`string` | キャンバスステップの名前
`device_id` | `null,`&nbsp;`string` | イベントが発生したデバイスの ID
`is_suspected_bot_click` | `null, boolean` | このイベントがボットイベントとして処理されたかどうか
`message_variation_name` | `null,`&nbsp;`string` | メッセージバリエーションの名前
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`short_url` | `null,`&nbsp;`string` | クリックされた短縮 URL
`suspected_bot_click_reason` | `null,`&nbsp;`string` | このイベントがボットとして分類された理由
`user_agent` | `null,`&nbsp;`string` | スパム報告が発生したユーザーエージェント
`user_phone_number` | `null,`&nbsp;`string` | [PII] メッセージを受信したユーザーの電話番号
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`interaction_type` | `null,`&nbsp;`string` | クリックを生成したインタラクションのタイプ。文字列値の例：Text URL、Reply、OpenURL
`element_label` | `null,`&nbsp;`string` | クリックされた要素に関するオプションの詳細（候補返信やボタンのテキストなど）
`element_type` | `null,`&nbsp;`string` | 候補とボタンに共通する interaction_type が候補由来かボタン由来かを指定します。例：Suggestion、Button
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`url` | `null,`&nbsp;`string` | ユーザーがクリックした URL
`subscription_group_api_id` | `string` | サブスクリプショングループの API ID
`canvas_variation_name` | `null,`&nbsp;`string` | このユーザーが受信した Canvas バリエーションの名前
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_RCS_DELIVERY_SHARED {#USERS_MESSAGES_RCS_DELIVERY_SHARED}

フィールド | タイプ | 説明
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの API ID
`app_group_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの BSON ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`id` | `string` | このイベントのグローバルな一意の ID
`time` | `int` | イベントが発生した UNIX タイムスタンプ
`user_id` | `string` | このイベントを実行したユーザーの Braze ユーザー ID
`campaign_name` | `null,`&nbsp;`string` | キャンペーンの名前
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の BSON ID
`canvas_name` | `null,`&nbsp;`string` | Canvas の名前
`canvas_step_name` | `null,`&nbsp;`string` | キャンバスステップの名前
`canvas_variation_name` | `null,`&nbsp;`string` | このユーザーが受信した Canvas バリエーションの名前
`device_id` | `null,`&nbsp;`string` | イベントが発生したデバイスの ID
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`message_variation_name` | `null,`&nbsp;`string` | メッセージバリエーションの名前
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`subscription_group_api_id` | `string` | サブスクリプショングループの API ID
`to_phone_number` | `null,`&nbsp;`string` | [PII] メッセージを受信するユーザーの電話番号（e.164 形式、例：+14155552671）
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`from_rcs_sender` | `null,`&nbsp;`string` | メッセージの送信に使用された RCS 送信者 ID またはエージェント名
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_RCS_INBOUNDRECEIVE_SHARED {#USERS_MESSAGES_RCS_INBOUNDRECEIVE_SHARED}

フィールド | タイプ | 説明
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの API ID
`app_group_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの BSON ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`id` | `string` | このイベントのグローバルな一意の ID
`time` | `int` | イベントが発生した UNIX タイムスタンプ
`user_id` | `string` | このイベントを実行したユーザーの Braze ユーザー ID
`action` | `null,`&nbsp;`string` | このメッセージに対して実行されたアクション（例：Subscribed、Unsubscribed、None）
`campaign_name` | `null,`&nbsp;`string` | キャンペーンの名前
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の BSON ID
`canvas_name` | `null,`&nbsp;`string` | Canvas の名前
`canvas_step_name` | `null,`&nbsp;`string` | キャンバスステップの名前
`media_urls` | `null,`&nbsp;`string` | ユーザーからのメディア URL
`message_variation_name` | `null,`&nbsp;`string` | メッセージバリエーションの名前
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`user_phone_number` | `null,`&nbsp;`string` | [PII] メッセージを受信したユーザーの電話番号
`subscription_group_api_id` | `string` | サブスクリプショングループの API ID
`message_body` | `null,`&nbsp;`string` | ユーザーからの入力応答
`to_rcs_sender` | `null,`&nbsp;`string` | メッセージの送信先の受信 RCS 送信者
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_RCS_READ_SHARED {#USERS_MESSAGES_RCS_READ_SHARED}

フィールド | タイプ | 説明
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの API ID
`app_group_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの BSON ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`id` | `string` | このイベントのグローバルな一意の ID
`time` | `int` | イベントが発生した UNIX タイムスタンプ
`user_id` | `string` | このイベントを実行したユーザーの Braze ユーザー ID
`campaign_name` | `null,`&nbsp;`string` | キャンペーンの名前
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の BSON ID
`canvas_name` | `null,`&nbsp;`string` | Canvas の名前
`canvas_step_name` | `null,`&nbsp;`string` | キャンバスステップの名前
`canvas_variation_name` | `null,`&nbsp;`string` | このユーザーが受信した Canvas バリエーションの名前
`message_variation_name` | `null,`&nbsp;`string` | メッセージバリエーションの名前
`to_phone_number` | `null,`&nbsp;`string` | [PII] メッセージを受信するユーザーの電話番号（e.164 形式、例：+14155552671）
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_RCS_REJECTION_SHARED {#USERS_MESSAGES_RCS_REJECTION_SHARED}

フィールド | タイプ | 説明
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの API ID
`app_group_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの BSON ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`id` | `string` | このイベントのグローバルな一意の ID
`time` | `int` | イベントが発生した UNIX タイムスタンプ
`user_id` | `string` | このイベントを実行したユーザーの Braze ユーザー ID
`campaign_name` | `null,`&nbsp;`string` | キャンペーンの名前
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の BSON ID
`canvas_name` | `null,`&nbsp;`string` | Canvas の名前
`canvas_step_name` | `null,`&nbsp;`string` | キャンバスステップの名前
`canvas_variation_name` | `null,`&nbsp;`string` | このユーザーが受信した Canvas バリエーションの名前
`device_id` | `null,`&nbsp;`string` | イベントが発生したデバイスの ID
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`error` | `null,`&nbsp;`string` | エラー名
`from_rcs_sender` | `null,`&nbsp;`string` | メッセージの送信に使用された RCS 送信者 ID またはエージェント名
`is_sms_fallback` | `null, boolean` | この拒否された RCS メッセージに対して SMS フォールバックが試行されたかどうかを示します。SMS 配信イベントとリンク/ペアになっています
`message_variation_name` | `null,`&nbsp;`string` | メッセージバリエーションの名前
`provider_error_code` | `null,`&nbsp;`string` | プロバイダーからのエラーコード
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`subscription_group_api_id` | `string` | サブスクリプショングループの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`to_phone_number` | `null,`&nbsp;`string` | [PII] メッセージを受信するユーザーの電話番号（e.164 形式、例：+14155552671）
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_RCS_SEND_SHARED {#USERS_MESSAGES_RCS_SEND_SHARED}

フィールド | タイプ | 説明
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの API ID
`app_group_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの BSON ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`id` | `string` | このイベントのグローバルな一意の ID
`time` | `int` | イベントが発生した UNIX タイムスタンプ
`user_id` | `string` | このイベントを実行したユーザーの Braze ユーザー ID
`campaign_name` | `null,`&nbsp;`string` | キャンペーンの名前
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の BSON ID
`canvas_name` | `null,`&nbsp;`string` | Canvas の名前
`canvas_step_name` | `null,`&nbsp;`string` | キャンバスステップの名前
`canvas_variation_name` | `null,`&nbsp;`string` | このユーザーが受信した Canvas バリエーションの名前
`category` | `null,`&nbsp;`string` | キーワードカテゴリ名。自動返信メッセージの場合のみ設定されます：'opt-in'、'opt-out'、'help'、またはカスタム値
`device_id` | `null,`&nbsp;`string` | イベントが発生したデバイスの ID
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`from_rcs_sender` | `null,`&nbsp;`string` | メッセージの送信に使用された RCS 送信者 ID またはエージェント名
`message_extras` | `null,`&nbsp;`string` | Liquid レンダリング中にタグ付けされたキーと値のペアの JSON 文字列
`message_variation_name` | `null,`&nbsp;`string` | メッセージバリエーションの名前
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`subscription_group_api_id` | `string` | サブスクリプショングループの API ID
`to_phone_number` | `null,`&nbsp;`string` | [PII] メッセージを受信するユーザーの電話番号（e.164 形式、例：+14155552671）
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_ABORT_SHARED {#USERS_MESSAGES_SMS_ABORT_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが所属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`subscription_group_api_id` | `null,`&nbsp;`string` | サブスクリプショングループの外部 ID
`abort_type` | `null,`&nbsp;`string` | 中止のタイプ。['liquid_abort_message', 'quiet_hours', 'rate_limit'] のいずれか
`abort_log` | `null,`&nbsp;`string` | [PII] 中止の詳細を記述するログメッセージ（最大2,000文字）
`app_group_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_CARRIERSEND_SHARED {#USERS_MESSAGES_SMS_CARRIERSEND_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`device_id` | `null,`&nbsp;`string` | ユーザーが匿名の場合、このユーザーに紐づけられた `device_id`
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが所属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`to_phone_number` | `null,`&nbsp;`string` | [PII] 受信者の電話番号
`from_phone_number` | `null,`&nbsp;`string` | SMS メッセージの送信元電話番号
`subscription_group_api_id` | `null,`&nbsp;`string` | サブスクリプショングループの外部 ID
`app_group_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_DELIVERY_SHARED {#USERS_MESSAGES_SMS_DELIVERY_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`device_id` | `null,`&nbsp;`string` | ユーザーが匿名の場合、このユーザーに紐づけられた `device_id`
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが所属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`to_phone_number` | `null,`&nbsp;`string` | [PII] 受信者の電話番号
`from_phone_number` | `null,`&nbsp;`string` | SMS メッセージの送信元電話番号
`subscription_group_api_id` | `null,`&nbsp;`string` | サブスクリプショングループの外部 ID
`app_group_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの BSON ID
`is_sms_fallback` | `null, boolean` | この拒否された RCS メッセージに対して SMS フォールバックが試行されたかどうかを示します。SMS 配信イベントとリンク/ペアになっています
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED {#USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`device_id` | `null,`&nbsp;`string` | ユーザーが匿名の場合、このユーザーに紐づけられた `device_id`
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが所属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`to_phone_number` | `null,`&nbsp;`string` | [PII] 受信者の電話番号
`subscription_group_api_id` | `null,`&nbsp;`string` | サブスクリプショングループの外部 ID
`error` | `null,`&nbsp;`string` | エラー名
`provider_error_code` | `null,`&nbsp;`string` | SMS サービスプロバイダーからのエラーコード
`app_group_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの BSON ID
`is_sms_fallback` | `null, boolean` | この拒否された RCS メッセージに対して SMS フォールバックが試行されたかどうかを示します。SMS 配信イベントとリンク/ペアになっています
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED {#USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `null,`&nbsp;`string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`app_group_api_id` | `null,`&nbsp;`string` | 受信電話番号に関連付けられたワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`user_phone_number` | `string` | [PII] メッセージを受信したユーザーの電話番号
`subscription_group_id` | `null,`&nbsp;`string` | この SMS メッセージの対象となるサブスクリプショングループの ID
`subscription_group_api_id` | `null,`&nbsp;`string` | この SMS メッセージの対象となるサブスクリプショングループの API ID
`inbound_phone_number` | `string` | メッセージの送信先の受信番号
`action` | `string` | このメッセージに対して実行されたアクション。例：`Subscribed`、`Unsubscribed`、`None`
`message_body` | `string` | ユーザーからの応答
`media_urls` | `null, {"type"=>"array", "items"=>["null", "string"]}` | ユーザーからのメディア URL
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このイベントが属するメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップメッセージバリエーションの API ID
`app_group_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_REJECTION_SHARED {#USERS_MESSAGES_SMS_REJECTION_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`device_id` | `null,`&nbsp;`string` | ユーザーが匿名の場合、このユーザーに紐づけられた `device_id`
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが所属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`to_phone_number` | `null,`&nbsp;`string` | [PII] 受信者の電話番号
`from_phone_number` | `null,`&nbsp;`string` | SMS メッセージの送信元電話番号
`subscription_group_api_id` | `null,`&nbsp;`string` | サブスクリプショングループの外部 ID
`error` | `null,`&nbsp;`string` | エラー名
`provider_error_code` | `null,`&nbsp;`string` | SMS サービスプロバイダーからのエラーコード
`app_group_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの BSON ID
`is_sms_fallback` | `null, boolean` | この拒否された RCS メッセージに対して SMS フォールバックが試行されたかどうかを示します。SMS 配信イベントとリンク/ペアになっています
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_SEND_SHARED {#USERS_MESSAGES_SMS_SEND_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`device_id` | `null,`&nbsp;`string` | ユーザーが匿名の場合、このユーザーに紐づけられた `device_id`
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが所属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`to_phone_number` | `null,`&nbsp;`string` | [PII] 受信者の電話番号
`subscription_group_api_id` | `null,`&nbsp;`string` | サブスクリプショングループの外部 ID
`category` | `null,`&nbsp;`string` | キーワードカテゴリ名。自動返信メッセージの場合のみ設定されます：'Opt-in'、'Opt-out'、'Help'、またはカスタム値
`app_group_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの BSON ID
`message_extras` | `null,`&nbsp;`string` | [PII] Liquid レンダリング中にタグ付けされたキーと値のペアの JSON 文字列
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED {#USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `null,`&nbsp;`string` | short_url の対象ユーザーの Braze ID。short_url がユーザークリックトラッキングを使用していない場合は null
`external_user_id` | `null,`&nbsp;`string` | [PII] short_url の対象ユーザーの外部 ID（存在する場合）。short_url がユーザークリックトラッキングを使用していない場合は null
`app_group_api_id` | `null,`&nbsp;`string` | short_url の生成に使用されたワークスペースの API ID
`time` | `int` | short_url がクリックされた Unix タイムスタンプ
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`campaign_id` | `null,`&nbsp;`string` | short_url が生成されたキャンペーンの Braze ID。キャンペーンからでない場合は null
`campaign_api_id` | `null,`&nbsp;`string` | short_url が生成されたキャンペーンの API ID。キャンペーンからでない場合は null
`message_variation_api_id` | `null,`&nbsp;`string` | short_url が生成されたメッセージバリエーションの API ID。キャンペーンからでない場合は null
`canvas_id` | `null,`&nbsp;`string` | short_url が生成された Canvas の Braze ID。Canvas からでない場合は null
`canvas_api_id` | `null,`&nbsp;`string` | short_url が生成された Canvas の API ID。Canvas からでない場合は null
`canvas_variation_api_id` | `null,`&nbsp;`string` | short_url が生成された Canvas バリエーションの API ID。Canvas からでない場合は null
`canvas_step_api_id` | `null,`&nbsp;`string` | short_url が生成されたキャンバスステップの API ID。Canvas からでない場合は null
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | short_url が生成されたキャンバスステップメッセージバリエーションの API ID。Canvas からでない場合は null
`url` | `string` | short_url がリダイレクトする、メッセージに含まれる元の URL
`short_url` | `string` | クリックされた短縮 URL
`user_agent` | `null,`&nbsp;`string` | short_url をリクエストしたユーザーエージェント
`user_phone_number` | `string` | [PII] ユーザーの電話番号
`device_id` | `null,`&nbsp;`string` | イベントが発生したデバイスの ID
`app_group_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの BSON ID
`is_suspected_bot_click` | `null, boolean` | このイベントがボットイベントとして処理されたかどうか
`suspected_bot_click_reason` | `null, object` | このイベントがボットとして分類された理由
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_RETRY_SHARED {#USERS_MESSAGES_SMS_RETRY_SHARED}

{% alert note %}
このテーブルは Snowflake データシェアリングでのみ利用可能です。
{% endalert %}

このイベントは、メッセージの優先度が下げられたりフリークエンシーキャップが適用されたりして、設定されたリトライ時間枠内で後から再試行された場合に発生します。

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | [PII] このイベントを実行したユーザーの Braze ユーザー ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`app_group_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの BSON ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの API ID
`time` | `int` | イベントが発生した UNIX タイムスタンプ
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの BSON ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の BSON ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`subscription_group_api_id` | `null,`&nbsp;`string` | サブスクリプショングループの API ID
`retry_type` | `null,`&nbsp;`string` | リトライのタイプ
`retry_log` | `null,`&nbsp;`string` | リトライの詳細を記述するログメッセージ
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WEBHOOK_ABORT_SHARED {#USERS_MESSAGES_WEBHOOK_ABORT_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`device_id` | `null,`&nbsp;`string` | ユーザーが匿名の場合、このユーザーに紐づけられた `device_id`
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが所属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`abort_type` | `null,`&nbsp;`string` | 中止のタイプ。['liquid_abort_message', 'quiet_hours', 'rate_limit'] のいずれか
`abort_log` | `null,`&nbsp;`string` | [PII] 中止の詳細を記述するログメッセージ（最大2,000文字）
`app_group_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_WEBHOOK_FAILURE_SHARED {#USERS_MESSAGES_WEBHOOK_FAILURE_SHARED}

フィールド | タイプ | 説明
------|------|------------
`http_status_code` | `null, int` | レスポンスの HTTP ステータスコード
`endpoint_url` | `null,`&nbsp;`string` | リクエスト先のエンドポイント URL
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの API ID
`app_group_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの BSON ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの BSON ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の BSON ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`content_length` | `null, int` | レスポンスのコンテンツ長
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`host` | `null,`&nbsp;`string` | リクエストのホスト
`id` | `string` | このイベントのグローバルな一意の ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`raw_response` | `null,`&nbsp;`string` | エンドポイントからの切り詰められた生レスポンス
`retry_count` | `null, int` | 試行されたリトライ回数
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`time` | `int` | イベントが発生した UNIX タイムスタンプ
`url_path` | `null,`&nbsp;`string` | リクエスト先 URL のパス
`user_id` | `string` | このイベントを実行したユーザーの Braze ユーザー ID
`webhook_duration` | `null, int` | このリクエストの合計所要時間（ミリ秒）
`webhook_failure_source` | `null,`&nbsp;`string` | エラーが Braze によって作成されたか、エンドポイント自体によって作成されたかを示します。ソースフィールドは External Endpoint、Treat no status code to host unreachable のいずれかです
`is_terminal` | `null, boolean` | このイベントが送信における最終試行であったかどうか
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WEBHOOK_SEND_SHARED {#USERS_MESSAGES_WEBHOOK_SEND_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`device_id` | `null,`&nbsp;`string` | ユーザーが匿名の場合、このユーザーに紐づけられた `device_id`
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが所属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`campaign_name` | `null,`&nbsp;`string` | キャンペーンの名前
`message_variation_name` | `null,`&nbsp;`string` | メッセージバリエーションの名前
`canvas_name` | `null,`&nbsp;`string` | Canvas の名前
`canvas_variation_name` | `null,`&nbsp;`string` | このユーザーが受信した Canvas バリエーションの名前
`canvas_step_name` | `null,`&nbsp;`string` | キャンバスステップの名前
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`app_group_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの BSON ID
`message_extras` | `null,`&nbsp;`string` | [PII] Liquid レンダリング中にタグ付けされたキーと値のペアの JSON 文字列
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WEBHOOK_RETRY_SHARED {#USERS_MESSAGES_WEBHOOK_RETRY_SHARED}

{% alert note %}
このテーブルは Snowflake データシェアリングでのみ利用可能です。
{% endalert %}

このイベントは、メッセージの優先度が下げられたりフリークエンシーキャップが適用されたりして、設定されたリトライ時間枠内で後から再試行された場合に発生します。

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | [PII] このイベントを実行したユーザーの Braze ユーザー ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`app_group_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの BSON ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの API ID
`time` | `int` | イベントが発生した UNIX タイムスタンプ
`device_id` | `null,`&nbsp;`string` | イベントが発生したデバイスの ID
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの BSON ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の BSON ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`retry_type` | `null,`&nbsp;`string` | リトライのタイプ
`retry_log` | `null,`&nbsp;`string` | リトライの詳細を記述するログメッセージ
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WHATSAPP_ABORT_SHARED {#USERS_MESSAGES_WHATSAPP_ABORT_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`to_phone_number` | 	`null,`&nbsp;`string` | [PII] 受信者の電話番号
`user_id` | `string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`device_id` | `null,`&nbsp;`string` | ユーザーが匿名の場合、このユーザーに紐づけられた `device_id`
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`app_group_id` | `null,`&nbsp;`string` | このユーザーが所属するワークスペースの ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが所属するワークスペースの API ID
`subscription_group_api_id` | `string` | サブスクリプショングループの API ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`abort_type` | `null,`&nbsp;`string` | 中止のタイプ。['liquid_abort_message', 'quiet_hours', 'rate_limit'] のいずれか
`abort_log` | `null,`&nbsp;`string` | [PII] 中止の詳細を記述するログメッセージ（最大2,000文字）
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_WHATSAPP_CLICK_SHARED {#USERS_MESSAGES_WHATSAPP_CLICK_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ユーザー ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`device_id` | `null,`&nbsp;`string` | イベントが発生したデバイスの ID
`app_group_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの BSON ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの API ID
`time` | `int` | イベントが発生した UNIX タイムスタンプ
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの BSON ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の BSON ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`url` | `null,`&nbsp;`string` | ユーザーがクリックした URL
`short_url` | `null,`&nbsp;`string` | クリックされた短縮 URL
`user_agent` | `null,`&nbsp;`string` | スパム報告が発生したユーザーエージェント
`user_phone_number` | `null,`&nbsp;`string` | [PII] メッセージを受信したユーザーの電話番号
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WHATSAPP_DELIVERY_SHARED {#USERS_MESSAGES_WHATSAPP_DELIVERY_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`to_phone_number` | `null,`&nbsp;`string` | [PII] 受信者の電話番号
`user_id` | `string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`device_id` | `null,`&nbsp;`string` | ユーザーが匿名の場合、このユーザーに紐づけられた `device_id`
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`from_phone_number` | `null,`&nbsp;`string` | WhatsApp メッセージの送信元電話番号
`app_group_id` | `null,`&nbsp;`string` | このユーザーが所属するワークスペースの ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが所属するワークスペースの API ID
`subscription_group_api_id` | `string` | サブスクリプショングループの API ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`flow_id` | `null,`&nbsp;`string` | WhatsApp Manager 内の Flow の一意の ID。ユーザーが WhatsApp Flow に応答している場合に存在します。
`template_name` | `null,`&nbsp;`string` | [PII] WhatsApp Manager 内のテンプレート名。テンプレートメッセージを送信する場合に存在します
`message_id` | `null,`&nbsp;`string` | Meta が生成したこのメッセージの一意の ID
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WHATSAPP_FAILURE_SHARED {#USERS_MESSAGES_WHATSAPP_FAILURE_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`to_phone_number` | `null,`&nbsp;`string` | [PII] 受信者の電話番号
`user_id` | `string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`device_id` | `null,`&nbsp;`string` | ユーザーが匿名の場合、このユーザーに紐づけられた `device_id`
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`from_phone_number` | `null,`&nbsp;`string` | WhatsApp メッセージの送信元電話番号
`app_group_id` | `null,`&nbsp;`string` | このユーザーが所属するワークスペースの ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが所属するワークスペースの API ID
`subscription_group_api_id` | `string` | サブスクリプショングループの API ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`provider_error_code` | `null,`&nbsp;`string` | WhatsApp からのエラーコード
`provider_error_title` | `null, `&nbsp;`string` | WhatsApp からのエラータイトル
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`message_id` | `null,`&nbsp;`string` | Meta が生成したこのメッセージの一意の ID
`template_name` | `null,`&nbsp;`string` | [PII] WhatsApp Manager 内のテンプレート名。テンプレートメッセージを送信する場合に存在します
`flow_id` | `null,`&nbsp;`string` | WhatsApp Manager 内の Flow の一意の ID。ユーザーが WhatsApp Flow に応答している場合に存在します。
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WHATSAPP_INBOUNDRECEIVE_SHARED {#USERS_MESSAGES_WHATSAPP_INBOUNDRECEIVE_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`user_phone_number` | `string` | [PII] メッセージを受信したユーザーの電話番号
`user_id` | `string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`inbound_phone_number` | `string` | メッセージの送信先の受信番号
`device_id` | `null,`&nbsp;`string` | ユーザーが匿名の場合、このユーザーに紐づけられた `device_id`
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`app_group_id` | `null,`&nbsp;`string` | このユーザーが所属するワークスペースの ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが所属するワークスペースの API ID
`subscription_group_api_id` | `string` | サブスクリプショングループの API ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`message_body` | `string` | ユーザーからの応答
`quick_reply_text` | `string` | ユーザーが押したボタンのテキスト
`media_urls` | `null, {"type"=>"array", "items"=>["null", "string"]}` | ユーザーからのメディア URL
`action` | `string` | このメッセージに対して実行されたアクション。例：`Subscribed`、`Unsubscribed`、`None`
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
`catalog_id` | `null,`&nbsp;`string` | 受信メッセージで製品が参照されている場合のカタログ ID。それ以外の場合は空
`product_id` | `null,`&nbsp;`string` | 購入された製品の ID
`flow_id` | `null,`&nbsp;`string` | WhatsApp Manager 内の Flow の一意の ID。ユーザーが WhatsApp Flow に応答している場合に存在します。
`flow_response_json` | `null,`&nbsp;`string` | [PII] ユーザーが応答したフォームの値。ユーザーが WhatsApp Flow に応答している場合に存在します。
`message_id` | `null,`&nbsp;`string` | Meta が生成したこのメッセージの一意の ID
`in_reply_to` | `null,`&nbsp;`string` | このメッセージが返信した元メッセージの message_id
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WHATSAPP_READ_SHARED {#USERS_MESSAGES_WHATSAPP_READ_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`to_phone_number` | `null,`&nbsp;`string` | [PII] 受信者の電話番号
`user_id` | `string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`device_id` | `null,`&nbsp;`string` | ユーザーが匿名の場合、このユーザーに紐づけられた `device_id`
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`from_phone_number` | `null,`&nbsp;`string` | WhatsApp メッセージの送信元電話番号
`app_group_id` | `null,`&nbsp;`string` | このユーザーが所属するワークスペースの ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが所属するワークスペースの API ID
`subscription_group_api_id` | `string` | サブスクリプショングループの API ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`template_name` | `null,`&nbsp;`string` | [PII] WhatsApp Manager 内のテンプレート名。テンプレートメッセージを送信する場合に存在します
`message_id` | `null,`&nbsp;`string` | Meta が生成したこのメッセージの一意の ID
`flow_id` | `null,`&nbsp;`string` | WhatsApp Manager 内の Flow の一意の ID。ユーザーが WhatsApp Flow に応答している場合に存在します。
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WHATSAPP_SEND_SHARED {#USERS_MESSAGES_WHATSAPP_SEND_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`to_phone_number` | `null,`&nbsp;`string`	| [PII] 受信者の電話番号
`user_id` | `string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`device_id` | `null,`&nbsp;`string` | ユーザーが匿名の場合、このユーザーに紐づけられた `device_id`
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`from_phone_number` | `null,`&nbsp;`string` | WhatsApp メッセージの送信元電話番号
`app_group_id` | `null,`&nbsp;`string` | このユーザーが所属するワークスペースの ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが所属するワークスペースの API ID
`subscription_group_api_id` | `string` | サブスクリプショングループの API ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`message_extras` | `null,`&nbsp;`string` | [PII] Liquid レンダリング中にタグ付けされたキーと値のペアの JSON 文字列
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`flow_id` | `null,`&nbsp;`string` | WhatsApp Manager 内の Flow の一意の ID。ユーザーが WhatsApp Flow に応答している場合に存在します。
`template_name` | `null,`&nbsp;`string` | [PII] WhatsApp Manager 内のテンプレート名。テンプレートメッセージを送信する場合に存在します
`message_id` | `null,`&nbsp;`string` | Meta が生成したこのメッセージの一意の ID
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WHATSAPP_RETRY_SHARED {#USERS_MESSAGES_WHATSAPP_RETRY_SHARED}

{% alert note %}
このテーブルは Snowflake データシェアリングでのみ利用可能です。
{% endalert %}

このイベントは、メッセージの優先度が下げられたりフリークエンシーキャップが適用されたりして、設定されたリトライ時間枠内で後から再試行された場合に発生します。

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | [PII] このイベントを実行したユーザーの Braze ユーザー ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`app_group_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの BSON ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの API ID
`time` | `int` | イベントが発生した UNIX タイムスタンプ
`to_phone_number` | `null,`&nbsp;`string` | [PII] メッセージを受信するユーザーの電話番号（e.164 形式）
`device_id` | `null,`&nbsp;`string` | イベントが発生したデバイスの ID
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`subscription_group_api_id` | `null,`&nbsp;`string` | サブスクリプショングループの API ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの BSON ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の BSON ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas の API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`retry_type` | `null,`&nbsp;`string` | リトライのタイプ
`retry_log` | `null,`&nbsp;`string` | リトライの詳細を記述するログメッセージ
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## ユーザー

### USERS_RANDOMBUCKETNUMBERUPDATE_SHARED {#USERS_RANDOMBUCKETNUMBERUPDATE_SHARED}

| フィールド                       | タイプ                     | 説明                                        |
| --------------------------- | ------------------------ | -------------------------------------------------- |
| `id`                        | `string`,&nbsp;`null`    | このイベントのグローバルな一意の ID                  |
| `app_group_id`              | `string`,&nbsp;`null`    | このユーザーが属するワークスペースの Braze ID      |
| `app_group_api_id`          | `string`,&nbsp;`null`    | このユーザーが属するワークスペースの API ID       |
| `user_id`                   | `string`,&nbsp;`null`    | このイベントを実行したユーザーの Braze ID      |
| `external_user_id`          | `string`,&nbsp;`null`    | [PII] ユーザーの外部ユーザー ID                 |
| `time`                      | `int`,&nbsp;`null`       | イベントが発生した Unix タイムスタンプ         |
| `random_bucket_number`      | `int`,&nbsp;`null`       | ユーザーに割り当てられた現在のランダムバケット番号  |
| `prev_random_bucket_number` | `int`,&nbsp;`null`       | ユーザーに割り当てられていた以前のランダムバケット番号 |
| `sf_created_at`             | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時      |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_USERDELETEREQUEST_SHARED {#USERS_USERDELETEREQUEST_SHARED}

| フィールド              | タイプ                     | 説明                                                   |
| ------------------ | ------------------------ | ------------------------------------------------------------- |
| `id`               | `string`,&nbsp;`null`    | このイベントのグローバルな一意の ID                             |
| `user_id`          | `string`,&nbsp;`null`    | 削除されたユーザーの Braze ID                          |
| `app_group_id`     | `string`,&nbsp;`null`    | このユーザーが属するワークスペースの Braze ID                 |
| `app_group_api_id` | `string`,&nbsp;`null`    | このユーザーが属するワークスペースの API ID                  |
| `time`             | `int`,&nbsp;`null`       | ユーザー削除リクエストが処理された Unix タイムスタンプ |
| `sf_created_at`    | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時                 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_USERORPHAN_SHARED {#USERS_USERORPHAN_SHARED}

| フィールド              | タイプ                     | 説明                                                                   |
| ------------------ | ------------------------ | ----------------------------------------------------------------------------- |
| `id`               | `string`,&nbsp;`null`    | このイベントのグローバルな一意の ID                                             |
| `user_id`          | `string`,&nbsp;`null`    | 孤立したユーザーの Braze ID                                         |
| `external_user_id` | `string`,&nbsp;`null`    | [PII] ユーザーの外部ユーザー ID                                            |
| `device_id`        | `string`,&nbsp;`null`    | このユーザーに紐づけられたデバイスの ID（ユーザーが匿名の場合）          |
| `app_group_id`     | `string`,&nbsp;`null`    | このユーザーが属するワークスペースの Braze ID                                 |
| `app_group_api_id` | `string`,&nbsp;`null`    | このユーザーが属するワークスペースの API ID                                  |
| `app_api_id`       | `string`,&nbsp;`null`    | 孤立したユーザーが属していたアプリの API ID                               |
| `time`             | `int`,&nbsp;`null`       | ユーザーが孤立した Unix タイムスタンプ                                 |
| `orphaned_by_id`   | `string`,&nbsp;`null`    | 孤立したユーザーのプロファイルとマージされたユーザーの Braze ID |
| `sf_created_at`    | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時                                 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## スナップショット {#snapshots}

{% alert note %}
スナップショットテーブルは Snowflake データ共有でのみ利用できます。
{% endalert %}

### SNAPSHOTS_APP_SHARED {#SNAPSHOTS_APP_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`time` | `int` | イベントが発生した UNIX タイムスタンプ
`app_group_id` | `string` | このユーザーが属するアプリグループの BSON ID
`api_id` | `string` | アプリの API ID
`name` | `null,`&nbsp;`string` | アプリの名前
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### SNAPSHOTS_CAMPAIGN_MESSAGE_VARIATION_SHARED {#SNAPSHOTS_CAMPAIGN_MESSAGE_VARIATION_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`time` | `int` | イベントが発生した UNIX タイムスタンプ
`app_group_id` | `string` | このユーザーが属するアプリグループの BSON ID
`api_id` | `string` | キャンペーンメッセージバリエーションの API ID
`name` | `null,`&nbsp;`string` | キャンペーンメッセージバリエーションの名前
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### SNAPSHOTS_CANVAS_FLOW_STEP_SHARED {#SNAPSHOTS_CANVAS_FLOW_STEP_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`time` | `int` | イベントが発生した UNIX タイムスタンプ
`app_group_id` | `string` | このユーザーが属するアプリグループの BSON ID
`type` | `null,`&nbsp;`string` | キャンバスフローステップのタイプ
`api_step_id` | `string` | キャンバスステップの API ID
`experiment_splits` | `null,`&nbsp;`string` | ステップの実験分割
`conversion_behaviors` | `null,`&nbsp;`string` | ステップのコンバージョン動作
`name` | `null,`&nbsp;`string` | キャンバスフローステップの名前
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### SNAPSHOTS_CANVAS_STEP_SHARED {#SNAPSHOTS_CANVAS_STEP_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`time` | `int` | イベントが発生した UNIX タイムスタンプ
`app_group_id` | `string` | このユーザーが属するアプリグループの BSON ID
`api_id` | `string` | キャンバスステップの API ID
`name` | `null,`&nbsp;`string` | キャンバスステップの名前
`actions` | `null,`&nbsp;`string` | キャンバスステップのアクション
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### SNAPSHOTS_CANVAS_VARIATION_SHARED {#SNAPSHOTS_CANVAS_VARIATION_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`time` | `int` | イベントが発生した UNIX タイムスタンプ
`app_group_id` | `string` | このユーザーが属するアプリグループの BSON ID
`api_id` | `string` | Canvas バリエーションの API ID
`name` | `null,`&nbsp;`string` | Canvas バリエーションの名前
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### SNAPSHOTS_EXPERIMENT_STEP_SHARED {#SNAPSHOTS_EXPERIMENT_STEP_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`time` | `int` | イベントが発生した UNIX タイムスタンプ
`app_group_id` | `string` | このユーザーが属するアプリグループの BSON ID
`type` | `null,`&nbsp;`string` | 実験ステップのタイプ
`api_step_id` | `string` | 実験ステップの API ID
`experiment_splits` | `null,`&nbsp;`string` | ステップの実験分割
`conversion_behaviors` | `null,`&nbsp;`string` | ステップのコンバージョン動作
`name` | `null,`&nbsp;`string` | 実験ステップの名前
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }