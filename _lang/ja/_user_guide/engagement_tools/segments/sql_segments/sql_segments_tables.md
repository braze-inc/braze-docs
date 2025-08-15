---
nav_title: "SQL テーブルリファレンス"
article_title: SQL テーブルリファレンス
page_order: 3
page_type: reference
toc_headers: h2
description: "この記事では、クエリビルダやSQL Segment Extensionsの生成時にクエリ可能なテーブルと列を紹介します。"
tool: Segments
---

<style>
table td {
   word-break: keep-all;
}
</style>

# SQL テーブルリファレンス

このページは、[クエリビルダや]({{site.baseurl}}/user_guide/analytics/query_builder/) [SQL セグメントエクステンションの]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/)生成時に照会可能なテーブルと列の参照です。 

## 目次

テーブル | 説明
------|------------
[USERS_BEHAVIORS_CUSTOMEVENT_SHARED](#USERS_BEHAVIORS_CUSTOMEVENT_SHARED) | ユーザーがカスタムイベントを実行したとき
[USERS_BEHAVIORS_INSTALLATTRIBUTION_SHARED](#USERS_BEHAVIORS_INSTALLATTRIBUTION_SHARED) | ユーザーがアプリをインストールし、それをパートナーに帰属させる場合
[USERS_BEHAVIORS_LOCATION_SHARED](#USERS_BEHAVIORS_LOCATION_SHARED) | ユーザーが位置情報を記録する
[USERS_BEHAVIORS_PURCHASE_SHARED](#USERS_BEHAVIORS_PURCHASE_SHARED) | ユーザーが購入を行ったとき
[USERS_BEHAVIORS_UNINSTALL_SHARED](#USERS_BEHAVIORS_UNINSTALL_SHARED) | ユーザーがアプリをアンインストールする
[USERS_BEHAVIORS_UPGRADEDAPP_SHARED](#USERS_BEHAVIORS_UPGRADEDAPP_SHARED) | ユーザーがアプリをアップグレードした場合
[USERS_BEHAVIORS_APP_FIRSTSESSION_SHARED](#USERS_BEHAVIORS_APP_FIRSTSESSION_SHARED) | ユーザーが初回セッションを開始したとき
[USERS_BEHAVIORS_APP_NEWSFEEDIMPRESSION_SHARED](#USERS_BEHAVIORS_APP_NEWSFEEDIMPRESSION_SHARED) | ユーザーがニュースフィードを見るとき
[USERS_BEHAVIORS_APP_SESSIONEND_SHARED](#USERS_BEHAVIORS_APP_SESSIONEND_SHARED) | ユーザーがアプリのセッションを終了するとき
[USERS_BEHAVIORS_APP_SESSIONSTART_SHARED](#USERS_BEHAVIORS_APP_SESSIONSTART_SHARED) | ユーザーがアプリでセッションを開始するとき
[USERS_BEHAVIORS_GEOFENCE_DATAEVENT_SHARED](#USERS_BEHAVIORS_GEOFENCE_DATAEVENT_SHARED) | ユーザーがジオフェンスされた領域をトリガーしたとき (例えば、ジオフェンスに出入りしたとき)。このイベントは、他のイベントとともにバッチ化され、標準的なイベントエンドポイントを通じて受信されたため、リアルタイムでエンドポイントによって受信されなかった可能性があります。
[USERS_BEHAVIORS_GEOFENCE_RECORDEVENT_SHARED](#USERS_BEHAVIORS_GEOFENCE_RECORDEVENT_SHARED) | ユーザーがジオフェンスされた領域をトリガーしたとき (例えば、ジオフェンスに出入りしたとき)。このイベントは専用のジオフェンスエンドポイントを通じて受信されたため、ユーザーのデバイスがジオフェンスをトリガーしたことを検知するとすぐにリアルタイムで受信されます。<br><br>また、ジオフェンスエンドポイントのレート制限により、一部のジオフェンスイベントが RecordEvent として反映されない可能性があります。ただし、すべてのジオフェンスイベントは、DataEvent によって表現されます (ただし、バッチ処理によって遅延が発生する可能性があります)。
[USERS_BEHAVIORS_SUBSCRIPTION_GLOBALSTATECHANGE_SHARED](#USERS_BEHAVIORS_SUBSCRIPTION_GLOBALSTATECHANGE_SHARED) | ユーザーが電子メールなどのチャネルからグローバルに購読または購読解除された場合
[USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED](#USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED) | ユーザーがサブスクリプショングループに登録されたとき、またはサブスクリプショングループから登録解除されたとき
[USERS_CAMPAIGNS_CONVERSION_SHARED](#USERS_CAMPAIGNS_CONVERSION_SHARED) | ユーザーがキャンペーンにコンバージョンした場合
[USERS_CAMPAIGNS_ENROLLINCONTROL_SHARED](#USERS_CAMPAIGNS_ENROLLINCONTROL_SHARED) | ユーザーがキャンペーンのコントロールグループに登録された場合
[USERS_CAMPAIGNS_FREQUENCYCAP_SHARED](#USERS_CAMPAIGNS_FREQUENCYCAP_SHARED) | ユーザーがキャンペーンで回数制限を受けた場合
[USERS_CAMPAIGNS_REVENUE_SHARED](#USERS_CAMPAIGNS_REVENUE_SHARED) | ユーザーが一次コンバージョン期間内に収益を上げた場合
[USERS_CANVASSTEP_PROGRESSION_SHARED](#USERS_CANVASSTEP_PROGRESSION_SHARED) | ユーザーがキャンバスステップに進むとき
[USERS_CANVAS_CONVERSION_SHARED](#USERS_CANVAS_CONVERSION_SHARED) | キャンバスのコンバージョンイベントでユーザーがコンバージョンした場合
[USERS_CANVAS_ENTRY_SHARED](#USERS_CANVAS_ENTRY_SHARED) | ユーザーがキャンバスに入るとき
[USERS_CANVAS_EXIT_MATCHEDAUDIENCE_SHARED](#USERS_CANVAS_EXIT_MATCHEDAUDIENCE_SHARED) | ユーザーがオーディエンスの終了条件に一致してキャンバスを出たとき
[USERS_CANVAS_EXIT_PERFORMEDEVENT_SHARED](#USERS_CANVAS_EXIT_PERFORMEDEVENT_SHARED) | ユーザーが例外イベントを実行してキャンバスを終了した場合
[USERS_CANVAS_EXPERIMENTSTEP_CONVERSION_SHARED](#USERS_CANVAS_EXPERIMENTSTEP_CONVERSION_SHARED) | キャンバス実験のステップでユーザーがコンバージョンした場合
[USERS_CANVAS_EXPERIMENTSTEP_SPLITENTRY_SHARED](#USERS_CANVAS_EXPERIMENTSTEP_SPLITENTRY_SHARED) | ユーザーが実験ステップパスに入ったとき
[USERS_CANVAS_FREQUENCYCAP_SHARED](#USERS_CANVAS_FREQUENCYCAP_SHARED) | キャンバスのステップでユーザーが回数制限を受けた場合
[USERS_CANVAS_REVENUE_SHARED](#USERS_CANVAS_REVENUE_SHARED) | 一次コンバージョンイベント期間内にユーザーが収益を上げた場合
[USERS_MESSAGES_CONTENTCARD_ABORT_SHARED](#USERS_MESSAGES_CONTENTCARD_ABORT_SHARED) | 当初予定されていたコンテンツカードメッセージが、何らかの理由で中止された。
[USERS_MESSAGES_CONTENTCARD_CLICK_SHARED](#USERS_MESSAGES_CONTENTCARD_CLICK_SHARED) | ユーザーがコンテンツカードをクリックすると
[USERS_MESSAGES_CONTENTCARD_DISMISS_SHARED](#USERS_MESSAGES_CONTENTCARD_DISMISS_SHARED) | ユーザーがコンテンツカードを却下したとき
[USERS_MESSAGES_CONTENTCARD_IMPRESSION_SHARED](#USERS_MESSAGES_CONTENTCARD_IMPRESSION_SHARED) | ユーザーがコンテンツ・カードを見るとき
[USERS_MESSAGES_CONTENTCARD_SEND_SHARED](#USERS_MESSAGES_CONTENTCARD_SEND_SHARED) | コンテンツ・カードをユーザーに送る場合
[USERS_MESSAGES_EMAIL_ABORT_SHARED](#USERS_MESSAGES_EMAIL_ABORT_SHARED) | 当初予定されていたメールメッセージが、何らかの理由で中止された。
[USERS_MESSAGES_EMAIL_BOUNCE_SHARED](#USERS_MESSAGES_EMAIL_BOUNCE_SHARED) | メールサービスプロバイダーがハードバウンスを返した。ハードバウンスとは、永続的な配信の失敗です。
[USERS_MESSAGES_EMAIL_CLICK_SHARED](#USERS_MESSAGES_EMAIL_CLICK_SHARED) | ユーザーが電子メールのリンクをクリックした場合
[USERS_MESSAGES_EMAIL_DELIVERY_SHARED](#USERS_MESSAGES_EMAIL_DELIVERY_SHARED) | 電子メールが配信された場合
[USERS_MESSAGES_EMAIL_MARKASSPAM_SHARED](#USERS_MESSAGES_EMAIL_MARKASSPAM_SHARED) | メールがスパムとしてマークされた場合
[USERS_MESSAGES_EMAIL_OPEN_SHARED](#USERS_MESSAGES_EMAIL_OPEN_SHARED) | ユーザーがメールを開く
[USERS_MESSAGES_EMAIL_SEND_SHARED](#USERS_MESSAGES_EMAIL_SEND_SHARED) | ユーザーに電子メールを送信する場合
[USERS_MESSAGES_EMAIL_SOFTBOUNCE_SHARED](#USERS_MESSAGES_EMAIL_SOFTBOUNCE_SHARED) | メールがソフトバウンスしたとき
[USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED](#USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED) | ユーザーがメールを配信停止したとき
[USERS_MESSAGES_INAPPMESSAGE_ABORT_SHARED](#USERS_MESSAGES_INAPPMESSAGE_ABORT_SHARED) | 当初予定されていたアプリ内メッセージが何らかの理由で中止された。
[USERS_MESSAGES_INAPPMESSAGE_CLICK_SHARED](#USERS_MESSAGES_INAPPMESSAGE_CLICK_SHARED) | ユーザーがアプリ内メッセージをクリックした場合
[USERS_MESSAGES_INAPPMESSAGE_IMPRESSION_SHARED](#USERS_MESSAGES_INAPPMESSAGE_IMPRESSION_SHARED) | ユーザーがアプリ内メッセージを閲覧した場合
[USERS_MESSAGES_NEWSFEEDCARD_ABORT_SHARED](#USERS_MESSAGES_NEWSFEEDCARD_ABORT_SHARED) | 当初予定されていたニュースフィードカードメッセージが何らかの理由で中止された。
[USERS_MESSAGES_NEWSFEEDCARD_CLICK_SHARED](#USERS_MESSAGES_NEWSFEEDCARD_CLICK_SHARED) | ユーザーがニュースフィードカードをクリックすると
[USERS_MESSAGES_NEWSFEEDCARD_IMPRESSION_SHARED](#USERS_MESSAGES_NEWSFEEDCARD_IMPRESSION_SHARED) | ユーザーがニュースフィードカードを閲覧する
[USERS_MESSAGES_PUSHNOTIFICATION_ABORT_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_ABORT_SHARED) | 当初予定されていたプッシュ通知メッセージが、何らかの理由で中止された。
[USERS_MESSAGES_PUSHNOTIFICATION_BOUNCE_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_BOUNCE_SHARED) | プッシュ通知がバウンスしたとき
[USERS_MESSAGES_PUSHNOTIFICATION_INFLUENCEDOPEN_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_INFLUENCEDOPEN_SHARED) | ユーザーが通知を受け取った後、通知をクリックせずにアプリを開いた場合
[USERS_MESSAGES_PUSHNOTIFICATION_IOSFOREGROUND_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_IOSFOREGROUND_SHARED) | アプリを開いているときにプッシュ通知を受け取った場合
[USERS_MESSAGES_PUSHNOTIFICATION_OPEN_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_OPEN_SHARED) | ユーザーがプッシュ通知を開いたとき、またはプッシュ通知ボタン（アプリを開かないCLOSEボタンを含む）をクリックしたとき。<br><br> プッシュボタンの操作には複数の結果があります。「No」、「Decline」、「Cancel」アクションは 「クリック数」、Accept アクションは「開封数」です。両方ともこの表に表示されていますが、**BUTTON_ACTION_TYPE**列で区別できます。たとえば、「No」、「Decline」、「Cancel」でない`BUTTON_ACTION_TYPE`でグループ化するためにクエリを使用できます。
[USERS_MESSAGES_PUSHNOTIFICATION_SEND_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_SEND_SHARED) | ユーザーにプッシュ通知を送るとき
[USERS_MESSAGES_SMS_ABORT_SHARED](#USERS_MESSAGES_SMS_ABORT_SHARED) | 当初予定されていたSMSメッセージが何らかの理由で中止された。
[USERS_MESSAGES_SMS_CARRIERSEND_SHARED](#USERS_MESSAGES_SMS_CARRIERSEND_SHARED) | SMSメッセージがキャリアに送信されるとき
[USERS_MESSAGES_SMS_DELIVERY_SHARED](#USERS_MESSAGES_SMS_DELIVERY_SHARED) | SMSメッセージが配信された場合
[USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED](#USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED) | BrazeがSMSサービスプロバイダにSMSメッセージを配信できない場合
[USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED](#USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED) | ユーザーからSMSメッセージを受信した場合
[USERS_MESSAGES_SMS_REJECTION_SHARED](#USERS_MESSAGES_SMS_REJECTION_SHARED) | SMSメッセージがユーザーに届かない場合
[USERS_MESSAGES_SMS_SEND_SHARED](#USERS_MESSAGES_SMS_SEND_SHARED) | SMSメッセージが送信された場合
[USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED](#USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED) | ユーザーがSMSメッセージに含まれるBrazeの短縮URLをクリックした場合
[USERS_MESSAGES_WEBHOOK_ABORT_SHARED](#USERS_MESSAGES_WEBHOOK_ABORT_SHARED) | 当初予定されていたウェブフック・メッセージが何らかの理由で中止された
[USERS_MESSAGES_WEBHOOK_SEND_SHARED](#USERS_MESSAGES_WEBHOOK_SEND_SHARED) | ユーザーに対してウェブフックを送信する場合
[USERS_MESSAGES_WHATSAPP_ABORT_SHARED](#USERS_MESSAGES_WHATSAPP_ABORT_SHARED) | 予定されていたWhatsAppメッセージが何らかの理由で中断された
[USERS_MESSAGES_WHATSAPP_DELIVERY_SHARED](#USERS_MESSAGES_WHATSAPP_DELIVERY_SHARED) |WhatsAppメッセージが配信された場合
[USERS_MESSAGES_WHATSAPP_FAILURE_SHARED](#USERS_MESSAGES_WHATSAPP_FAILURE_SHARED) | WhatsAppメッセージがユーザーに届かない場合
[USERS_MESSAGES_WHATSAPP_INBOUNDRECEIVE_SHARED](#USERS_MESSAGES_WHATSAPP_INBOUNDRECEIVE_SHARED) | ユーザーからWhatsAppメッセージを受信した場合
[USERS_MESSAGES_WHATSAPP_READ_SHARED](#USERS_MESSAGES_WHATSAPP_READ_SHARED) | ユーザーがWhatsAppメッセージを開く
[USERS_MESSAGES_WHATSAPP_SEND_SHARED](#USERS_MESSAGES_WHATSAPP_SEND_SHARED) | あるユーザーに対してWhatsAppメッセージを送信する場合
[USERS_RANDOMBUCKETNUMBERUPDATE_SHARED](#USERS_RANDOMBUCKETNUMBERUPDATE_SHARED) | ユーザーのランダムバケット番号が変更された場合
[USERS_USERDELETEREQUEST_SHARED](#USERS_USERDELETEREQUEST_SHARED) | 顧客からのリクエストによりユーザーが削除された場合
[USERS_USERORPHAN_SHARED](#USERS_USERORPHAN_SHARED) | ユーザーが他のユーザーのプロファイルと統合され、元のプロファイルが孤児になった場合


## 行動

### USERS_BEHAVIORS_CUSTOMEVENT_SHARED {#USERS_BEHAVIORS_CUSTOMEVENT_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | イベントを実行したユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザーID
`app_group_api_id` | `null,` `string` | このユーザーが所属するワークスペースのAPI ID
`app_api_id` | `null,` `string` | このアクションが発生したアプリのAPI ID
`time` | `int` | ユーザーがイベントを実行したUnixタイムスタンプ
`gender` | `null,` `string` | [PII] ユーザーの性別
`country` | `null,` `string` | [PII] ユーザーの国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
`device_id` | `null,` `string` | カスタムイベントが発生したデバイスのID
`sdk_version` | `null,` `string` | イベント中に使用されたBraze SDKのバージョン
`platform` | `null,` `string` | デバイスのプラットフォーム
`os_version` | `null,` `string` | デバイスのオペレーティング・システムのバージョン
`device_model` | `null,` `string` | デバイスのモデル
`name` | `string` | カスタムイベントの名前
`properties` | `string` | JSONエンコードされた文字列として保存されたイベントのカスタムプロパティ
`ad_id` | `null,` `string` | [PII] 広告識別子
`ad_id_type` | `null,` `string` | `ios_idfa`、`google_ad_id`、`windows_ad_id`、`roku_ad_id` のいずれか
`ad_tracking_enabled` | `null, boolean` | デバイスの広告トラッキングが有効かどうか
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_INSTALLATTRIBUTION_SHARED {#USERS_BEHAVIORS_INSTALLATTRIBUTION_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | インストールしたユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザーID
`device_id` | `null,` `string` | ユーザーが匿名の場合、このユーザーに関連付けられる `device_id`
`app_group_api_id` | `null,` `string` | このユーザーが所属するワークスペースのAPI ID
`time` | `int` | ユーザーがインストールしたUnixのタイムスタンプ
`source` | `string` | アトリビューション元
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_LOCATION_SHARED {#USERS_BEHAVIORS_LOCATION_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | 位置を記録したユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザーID
`app_group_api_id` | `null,` `string` | このユーザーが所属するワークスペースのAPI ID
`app_api_id` | `null,` `string` | この位置情報が記録されたアプリのAPI ID
`time` | `int` | ロケーションが記録されたUnixタイムスタンプ
`latitude` | `float` | [PII] 記録された場所の緯度
`longitude` | `float` | [PII] 記録された場所の経度
`altitude` | `null, float` | [PII] 記録された位置の高度
`ll_accuracy` | `null, float` | 記録された位置の緯度経度の精度
`alt_accuracy` | `null, float` | 記録された位置の高度の精度
`device_id` | `null,` `string` | 位置情報が記録されたデバイスのID
`sdk_version` | `null,` `string` | その場所が記録されたときに使用されていたBraze SDKのバージョン
`platform` | `null,` `string` | デバイスのプラットフォーム
`os_version` | `null,` `string` | デバイスのオペレーティング・システムのバージョン
`device_model` | `null,` `string` | デバイスのモデル
`ad_id` | `null,` `string` | [PII] 広告識別子
`ad_id_type` | `null,` `string` | `ios_idfa`、`google_ad_id`、`windows_ad_id`、`roku_ad_id` のいずれか
`ad_tracking_enabled` | `null, boolean` | デバイスの広告トラッキングが有効かどうか
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_PURCHASE_SHARED {#USERS_BEHAVIORS_PURCHASE_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | 購入したユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザーID
`app_group_api_id` | `null,` `string` | このユーザーが所属するワークスペースのAPI ID
`app_api_id` | `null,` `string` | 購入が発生したアプリの API ID
`time` | `int` | ユーザーが購入した時点の Unix タイムスタンプ
`device_id` | `null,` `string` | 購入が発生したデバイスの ID
`sdk_version` | `null,` `string` | 購入時に使用していたBraze SDKのバージョン
`platform` | `null,` `string` | デバイスのプラットフォーム
`os_version` | `null,` `string` | デバイスのオペレーティング・システムのバージョン
`device_model` | `null,` `string` | デバイスのモデル
`product_id` | `string` | 購入した製品のID
`price` | `float` | 購入価格
`currency` | `string` | 購入通貨
`properties` | `string` | JSONエンコードされた文字列として保存された購入のカスタムプロパティ
`ad_id` | `null,` `string` | [PII] 広告識別子
`ad_id_type` | `null,` `string` | `ios_idfa`、`google_ad_id`、`windows_ad_id`、`roku_ad_id` のいずれか
`ad_tracking_enabled` | `null, boolean` | デバイスの広告トラッキングが有効かどうか
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_UNINSTALL_SHARED {#USERS_BEHAVIORS_UNINSTALL_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | アンインストールしたユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザーID
`device_id` | `null,` `string` | ユーザーが匿名の場合、このユーザーに関連付けられる `device_id`
`app_group_api_id` | `null,` `string` | このユーザーが所属するワークスペースのAPI ID
`app_api_id` | `null,` `string` | アンインストールされたアプリのAPI ID
`time` | `int` | ユーザーがアンインストールしたUnixタイムスタンプ
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_UPGRADEDAPP_SHARED {#USERS_BEHAVIORS_UPGRADEDAPP_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | アプリをアップグレードしたユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザーID
`app_group_api_id` | `null,` `string` | このユーザーが所属するワークスペースのAPI ID
`app_api_id` | `null,` `string` | ユーザーがアップグレードしたアプリのAPI ID
`time` | `int` | ユーザーがアプリをアップグレードしたUnixタイムスタンプ
`device_id` | `null,` `string` | ユーザーがアプリをアップグレードしたデバイスのID
`sdk_version` | `null,` `string` | 使用中のBraze SDKのバージョン
`platform` | `null,` `string` | デバイスのプラットフォーム
`os_version` | `null,` `string` | デバイスのオペレーティング・システムのバージョン
`device_model` | `null,` `string` | デバイスのモデル
`old_app_version` | `null,` `string` | 旧バージョンのアプリ
`new_app_version` | `null,` `string` | アプリの新バージョン
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_APP_FIRSTSESSION_SHARED {#USERS_BEHAVIORS_APP_FIRSTSESSION_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このアクションを実行するユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザーID
`app_group_api_id` | `null,` `string` | このユーザーが所属するワークスペースのAPI ID
`app_api_id` | `null,` `string` | このセッションが発生したアプリのAPI ID
`time` | `int` | セッションが開始されたUnixタイムスタンプ
`session_id` | `string` | セッションのUUID
`gender` | `null,` `string` | [PII] ユーザーの性別
`country` | `null,` `string` | [PII] ユーザーの国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
`device_id` | `null,` `string` | セッションが発生したデバイスの ID
`sdk_version` | `null,` `string` | セッション中に使用されたBraze SDKのバージョン
`platform` | `null,` `string` | デバイスのプラットフォーム
`os_version` | `null,` `string` | デバイスのオペレーティング・システムのバージョン
`device_model` | `null,` `string` | デバイスのモデル
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_APP_NEWSFEEDIMPRESSION_SHARED {#USERS_BEHAVIORS_APP_NEWSFEEDIMPRESSION_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | ニュースフィードを閲覧したユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザーID
`app_group_api_id` | `null,` `string` | このユーザーが所属するワークスペースのAPI ID
`app_api_id` | `null,` `string` | ユーザーがニュースフィードを閲覧したアプリのAPI ID
`time` | `int` | ユーザーがニュースフィードを閲覧したUnixタイムスタンプ
`device_id` | `null,` `string` | インプレッションが発生したデバイスの ID
`sdk_version` | `null,` `string` | インプレッションで使用したBraze SDKのバージョン
`platform` | `null,` `string` | デバイスのプラットフォーム
`os_version` | `null,` `string` | デバイスのオペレーティング・システムのバージョン
`device_model` | `null,` `string` | デバイスのモデル
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_APP_SESSIONEND_SHARED {#USERS_BEHAVIORS_APP_SESSIONEND_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このアクションを実行するユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザーID
`app_group_api_id` | `null,` `string` | このユーザーが所属するワークスペースのAPI ID
`app_api_id` | `null,` `string` | このセッションが発生したアプリのAPI ID
`time` | `int` | セッションが終了したUnixタイムスタンプ
`duration` | `null, float` | セッション期間
`session_id` | `string` | セッションのUUID
`device_id` | `null,` `string` | セッションが発生したデバイスの ID
`sdk_version` | `null,` `string` | セッション中に使用されたBraze SDKのバージョン
`platform` | `null,` `string` | デバイスのプラットフォーム
`os_version` | `null,` `string` | デバイスのオペレーティング・システムのバージョン
`device_model` | `null,` `string` | デバイスのモデル
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_APP_SESSIONSTART_SHARED {#USERS_BEHAVIORS_APP_SESSIONSTART_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このアクションを実行するユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザーID
`app_api_id` | `null,` `string` | このセッションが発生したアプリのAPI ID
`app_group_api_id` | `null,` `string` | このユーザーが所属するワークスペースのAPI ID
`time` | `int` | セッションが開始されたUnixタイムスタンプ
`session_id` | `string` | セッションのUUID
`device_id` | `null,` `string` | セッションが発生したデバイスの ID
`sdk_version` | `null,` `string` | セッション中に使用されたBraze SDKのバージョン
`platform` | `null,` `string` | デバイスのプラットフォーム
`os_version` | `null,` `string` | デバイスのオペレーティング・システムのバージョン
`device_model` | `null,` `string` | デバイスのモデル
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_GEOFENCE_DATAEVENT_SHARED {#USERS_BEHAVIORS_GEOFENCE_DATAEVENT_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | イベントを実行したユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザーID
`app_group_api_id` | `null,` `string` | このユーザーが所属するワークスペースのAPI ID
`app_api_id` | `null,` `string` | このアクションが発生したアプリのAPI ID
`time` | `int` | ユーザーがイベントを実行したUnixタイムスタンプ
`device_id` | `null,` `string` | カスタムイベントが発生したデバイスのID
`sdk_version` | `null,` `string` | イベント中に使用されたBraze SDKのバージョン
`platform` | `null,` `string` | デバイスのプラットフォーム
`os_version` | `null,` `string` | デバイスのオペレーティング・システムのバージョン
`device_model` | `null,` `string` | デバイスのモデル
`event_type` | `string` | トリガーされたジオフェンスイベントの種類 (例: 「入る」または「出る」)
`location_set_id` | `string` | トリガーされたジオフェンスのロケーションセットのID
`geofence_id` | `string` | トリガーされたジオフェンスの ID
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_GEOFENCE_RECORDEVENT_SHARED {#USERS_BEHAVIORS_GEOFENCE_RECORDEVENT_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | イベントを実行したユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザーID
`app_group_api_id` | `null,` `string` | このユーザーが所属するワークスペースのAPI ID
`app_api_id` | `null,` `string` | このアクションが発生したアプリのAPI ID
`time` | `int` | ユーザーがイベントを実行したUnixタイムスタンプ
`device_id` | `null,` `string` | カスタムイベントが発生したデバイスのID
`sdk_version` | `null,` `string` | イベント中に使用されたBraze SDKのバージョン
`platform` | `null,` `string` | デバイスのプラットフォーム
`os_version` | `null,` `string` | デバイスのオペレーティング・システムのバージョン
`device_model` | `null,` `string` | デバイスのモデル
`event_type` | `string` | トリガーされたジオフェンスイベントの種類 (例: 「入る」または「出る」)
`location_set_id` | `string` | トリガーされたジオフェンスのロケーションセットのID
`geofence_id` | `string` | トリガーされたジオフェンスの ID
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_SUBSCRIPTION_GLOBALSTATECHANGE_SHARED {#USERS_BEHAVIORS_SUBSCRIPTION_GLOBALSTATECHANGE_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | 影響を受けたユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザーID
`email_address` | `null,` `string` | [PII] ユーザーのメールアドレス
`state_change_source` | `null,` `string` | 状態変更のソース（REST、SDK、ダッシュボードなど）
`subscription_status` | `string` | サブスクリプションステータス: 「配信登録済み」または「配信停止済み」
`channel` | `null,` `string` | メールなど、グローバルサブスクリプション状態のチャネル
`time` | `int` | サブスクリプションの状態が変更されたUnixタイムスタンプ
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`app_group_api_id` | `null,` `string` | このユーザーが所属するワークスペースのAPI ID
`app_api_id` | `null,` `string` | イベントが属するアプリのAPI ID
`campaign_id` | `null,` `string` | このイベントが属するキャンペーンの内部用Braze ID
`campaign_api_id` | `null,` `string` | このイベントが属するキャンペーンのAPI ID
`message_variation_api_id` | `null,` `string` | このイベントが属するメッセージバリエーションのAPI ID
`canvas_id` | `null,` `string` | このイベントが属するキャンバスの内部使用Braze ID
`canvas_api_id` | `null,` `string` | このイベントが属するキャンバスのAPI ID
`canvas_variation_api_id` | `null,` `string` | このイベントが属するキャンバスのバリエーションのAPI ID
`canvas_step_api_id` | `null,` `string` | このイベントが属するキャンバスステップのAPI ID
`send_id` | `null,` `string` | このサブスクリプション状態変更アクションが発信したメッセージ送信ID
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED {#USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | 影響を受けたユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザーID
`device_id` | `null,` `string` | ユーザーが匿名の場合、このユーザーに関連付けられる `device_id`
`app_group_api_id` | `null,` `string` | このユーザーが所属するワークスペースのAPI ID
`email_address` | `null,` `string` | [PII] ユーザーのメールアドレス
`phone_number` | `null,` `string` | [PII] e164 形式のユーザーの電話番号
`app_api_id` | `null,` `string` | イベントが属するアプリのAPI ID
`campaign_id` | `null,` `string` | このイベントが属するキャンペーンの内部用Braze ID
`campaign_api_id` | `null,` `string` | このイベントが属するキャンペーンのAPI ID
`message_variation_api_id` | `null,` `string` | このイベントが属するメッセージバリエーションのAPI ID
`canvas_id` | `null,` `string` | このイベントが属するキャンバスの内部使用Braze ID
`canvas_api_id` | `null,` `string` | このイベントが属するキャンバスのAPI ID
`canvas_variation_api_id` | `null,` `string` | このイベントが属するキャンバスのバリエーションのAPI ID
`canvas_step_api_id` | `null,` `string` | このイベントが属するキャンバスステップのAPI ID
`subscription_group_api_id` | `string` | サブスクリプショングループAPI ID
`channel` | `null,` `string` | チャンネル：「Eメール」または「SMS」、購読グループのチャンネルタイプによる
`subscription_status` | `string` | サブスクリプションステータス: 「配信登録済み」または「配信停止済み」
`time` | `int` | サブスクリプションの状態が変更されたUnixタイムスタンプ
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`send_id` | `null,` `string` | このサブスクリプション状態変更アクションが発信したメッセージ送信ID
`state_change_source` | `null,` `string` | 状態変更のソース（REST、SDK、ダッシュボードなど）
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## キャンペーン

### USERS_CAMPAIGNS_CONVERSION_SHARED {#USERS_CAMPAIGNS_CONVERSION_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザーID
`device_id` | `null,` `string` | ユーザーが匿名の場合、このユーザーに関連付けられる `device_id`
`app_group_api_id` | `null,` `string` | このユーザーが所属するワークスペースのAPI ID
`time` | `int` | イベントが発生したUnixタイムスタンプ
`app_api_id` | `null,` `string` | このイベントが発生したアプリのAPI ID
`dispatch_id` | `null,` `string` | このメッセージが属するディスパッチの ID
`send_id` | `null,` `string` | このメッセージが属するメッセージ送信ID
`campaign_id` | `string` | このイベントが属するキャンペーンの内部用Braze ID
`campaign_api_id` | `null,` `string` | このイベントが属するキャンペーンのAPI ID
`message_variation_api_id` | `null,` `string` | このユーザーが受信したメッセージバリエーションのAPI ID
`conversion_behavior_index` | `null, int` | 変換動作のインデックス
`gender` | `null,` `string` | [PII] ユーザーの性別
`country` | `null,` `string` | [PII] ユーザーの国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CAMPAIGNS_ENROLLINCONTROL_SHARED {#USERS_CAMPAIGNS_ENROLLINCONTROL_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザーID
`device_id` | `null,` `string` | ユーザーが匿名の場合、このユーザーに関連付けられる `device_id`
`app_group_api_id` | `null,` `string` | このユーザーが所属するワークスペースのAPI ID
`time` | `int` | イベントが発生したUnixタイムスタンプ
`app_api_id` | `null,` `string` | このイベントが発生したアプリのAPI ID
`dispatch_id` | `null,` `string` | このメッセージが属するディスパッチの ID
`send_id` | `null,` `string` | このメッセージが属するメッセージ送信ID
`campaign_id` | `string` | このイベントが属するキャンペーンの内部用Braze ID
`campaign_api_id` | `null,` `string` | このイベントが属するキャンペーンのAPI ID
`message_variation_api_id` | `null,` `string` | このユーザーが受信したメッセージバリエーションのAPI ID
`gender` | `null,` `string` | [PII] ユーザーの性別
`country` | `null,` `string` | [PII] ユーザーの国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CAMPAIGNS_FREQUENCYCAP_SHARED {#USERS_CAMPAIGNS_FREQUENCYCAP_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザーID
`device_id` | `null,` `string` | ユーザーが匿名の場合、このユーザーに関連付けられる `device_id`
`app_group_api_id` | `null,` `string` | このユーザーが所属するワークスペースのAPI ID
`time` | `int` | イベントが発生したUnixタイムスタンプ
`dispatch_id` | `null,` `string` | このメッセージが属するディスパッチの ID
`send_id` | `null,` `string` | このメッセージが属するメッセージ送信ID
`campaign_id` | `string` | このイベントが属するキャンペーンの内部用Braze ID
`campaign_api_id` | `null,` `string` | このイベントが属するキャンペーンのAPI ID
`message_variation_api_id` | `null,` `string` | このユーザーが受信したメッセージバリエーションのAPI ID
`channel` | `null,` `string` | このイベントが属するチャンネル
`gender` | `null,` `string` | [PII] ユーザーの性別
`country` | `null,` `string` | [PII] ユーザーの国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CAMPAIGNS_REVENUE_SHARED {#USERS_CAMPAIGNS_REVENUE_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザーID
`device_id` | `null,` `string` | ユーザーが匿名の場合、このユーザーに関連付けられる `device_id`
`app_group_api_id` | `null,` `string` | このユーザーが所属するワークスペースのAPI ID
`time` | `int` | イベントが発生したUnixタイムスタンプ
`app_api_id` | `null,` `string` | このイベントが発生したアプリのAPI ID
`dispatch_id` | `null,` `string` | このメッセージが属するディスパッチの ID
`send_id` | `null,` `string` | このメッセージが属するメッセージ送信ID
`campaign_id` | `string` | このイベントが属するキャンペーンの内部用Braze ID
`campaign_api_id` | `null,` `string` | このイベントが属するキャンペーンのAPI ID
`message_variation_api_id` | `null,` `string` | このユーザーが受信したメッセージバリエーションのAPI ID
`gender` | `null,` `string` | [PII] ユーザーの性別
`country` | `null,` `string` | [PII] ユーザーの国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
`revenue` | `long` | 発生したセント単位の米ドル収益額
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## キャンバス

### USERS_CANVASSTEP_PROGRESSION_SHARED {#USERS_CANVASSTEP_PROGRESSION_SHARED}

| フィールド                                  | タイプ                     | 説明                                                                                                     |
| -------------------------------------- | ------------------------ | --------------------------------------------------------------------------------------------------------------- |
| `id`                                   | `string`, `null`    | このイベントのグローバルな一意の ID                                                                               |
| `user_id`                              | `string`, `null`    | このイベントを実行したユーザーのBraze ID                                                                   |
| `external_user_id`                     | `string`, `null`    | [PII] ユーザーの外部ユーザーID                                                                              |
| `device_id`                            | `string`, `null`    | ユーザーが匿名の場合、このユーザーに紐づくデバイスのID                                            |
| `app_group_id`                         | `string`, `null`    | このユーザーが所属するワークスペースのBraze ID                                                                   |
| `app_group_api_id`                     | `string`, `null`    | このユーザーが所属するワークスペースのAPI ID                                                                    |
| `time`                                 | `int`, `null`       | イベントが発生したUnixタイムスタンプ                                                                      |
| `canvas_id`                            | `string`, `null`    | (Braze専用）このイベントが属するキャンバスのID                                                     |
| `canvas_api_id`                        | `string`, `null`    | このイベントが属するキャンバスのAPI ID        |         
| `canvas_variation_api_id`              | `string`, `null`    | このイベントが属するキャンバスのバリエーションのAPI ID                                                            |
| `canvas_step_api_id`                   | `string`, `null`    | このイベントが属するキャンバスステップのAPI ID                                                                 |
| `progression_type`                     | `string`, `null`    | ステップ進行イベントのタイプ |
| `is_canvas_entry`                      | `boolean`, `null`   | これがキャンバスの最初のステップへのエントリーであるかどうか        |
| `exit_reason`                          | `string`, `null`    | これが離脱である場合、ステップ中にユーザーがキャンバスを離脱した理由                  |
| `canvas_entry_id`                      | `string`, `null`    | キャンバス内のこのユーザーインスタンスの一意の識別子  |
| `next_step_id`                         | `string`, `null`    | キャンバスの次のステップの BSON ID |
| `next_step_api_id`                     | `string`, `null`    | キャンバスの次のステップの API ID |
| `sf_created_at`                        | `timestamp`, `null` | このイベントが Snowpipe に検出されたとき                                                                   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_CONVERSION_SHARED {#USERS_CANVAS_CONVERSION_SHARED}

| フィールド                                  | タイプ                     | 説明                                                                                                     |
| -------------------------------------- | ------------------------ | --------------------------------------------------------------------------------------------------------------- |
| `id`                                   | `string`, `null`    | このイベントのグローバルな一意の ID                                                                               |
| `user_id`                              | `string`, `null`    | このイベントを実行したユーザーのBraze ID                                                                   |
| `external_user_id`                     | `string`, `null`    | [PII] ユーザーの外部ユーザーID                                                                              |
| `device_id`                            | `string`, `null`    | ユーザーが匿名の場合、このユーザーに紐づくデバイスのID                                            |
| `app_group_id`                         | `string`, `null`    | このユーザーが所属するワークスペースのBraze ID                                                                   |
| `app_group_api_id`                     | `string`, `null`    | このユーザーが所属するワークスペースのAPI ID                                                                    |
| `time`                                 | `int`, `null`       | イベントが発生したUnixタイムスタンプ                                                                      |
| `app_api_id`                           | `string`, `null`    | このイベントが発生したアプリのAPI ID                                                                  |
| `canvas_id`                            | `string`, `null`    | (Braze専用）このイベントが属するキャンバスのID                                                     |
| `canvas_api_id`                        | `string`, `null`    | このイベントが属するキャンバスのAPI ID                                                                      |
| `canvas_variation_api_id`              | `string`, `null`    | このイベントが属するキャンバスのバリエーションのAPI ID                                                            |
| `canvas_step_api_id`                   | `string`, `null`    | このイベントが属するキャンバスステップのAPI ID                                                                 |
| `canvas_step_message_variation_api_id` | `string`, `null`    | このユーザーが受け取ったキャンバスステップメッセージのバリエーションのAPI ID                                                  |
| `conversion_behavior_index`            | `int`, `null`       | ユーザーが行ったコンバージョンイベントのタイプ。"0 "は一次コンバージョン、"1 "は二次コンバージョンである。 |
| `gender`                               | `string`, `null`    | [PII] ユーザーの性別                                                                                        |
| `country`                              | `string`, `null`    | [PII] ユーザーの国                                                                                       |
| `timezone`                             | `string`, `null`    | ユーザーのタイムゾーン                                                                                            |
| `language`                             | `string`, `null`    | [PII] ユーザーの言語                                                                                      |
| `sf_created_at`                        | `timestamp`, `null` | このイベントが Snowpipe に検出されたとき                                                                   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_ENTRY_SHARED {#USERS_CANVAS_ENTRY_SHARED}

| フィールド                     | タイプ                     | 説明                                                          |
| ------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                      | `string`, `null`    | このイベントのグローバルな一意の ID                                    |
| `user_id`                 | `string`, `null`    | このイベントを実行したユーザーのBraze ID                        |
| `external_user_id`        | `string`, `null`    | [PII] ユーザーの外部ユーザーID                                   |
| `device_id`               | `string`, `null`    | ユーザーが匿名の場合、このユーザーに紐づくデバイスのID |
| `app_group_id`            | `string`, `null`    | このユーザーが所属するワークスペースのBraze ID                        |
| `app_group_api_id`        | `string`, `null`    | このユーザーが所属するワークスペースのAPI ID                         |
| `time`                    | `int`, `null`       | イベントが発生したUnixタイムスタンプ                           |
| `canvas_id`               | `string`, `null`    | (Braze専用）このイベントが属するキャンバスのID          |
| `canvas_api_id`           | `string`, `null`    | このイベントが属するキャンバスのAPI ID                           |
| `canvas_variation_api_id` | `string`, `null`    | このイベントが属するキャンバスのバリエーションのAPI ID                 |
| `canvas_step_api_id`      | `string`, `null`    | [非推奨] このイベントが属するキャンバスステップのAPI ID         |
| `gender`                  | `string`, `null`    | [PII] ユーザーの性別                                             |
| `country`                 | `string`, `null`    | [PII] ユーザーの国                                            |
| `timezone`                | `string`, `null`    | ユーザーのタイムゾーン                                                 |
| `language`                | `string`, `null`    | [PII] ユーザーの言語                                           |
| `in_control_group`        | `boolean`, `null`   | ユーザーがコントロール・グループに登録されていた場合、真となる                   |
| `sf_created_at`           | `timestamp`, `null` | このイベントが Snowpipe に検出されたとき                        |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_EXIT_MATCHEDAUDIENCE_SHARED {#USERS_CANVAS_EXIT_MATCHEDAUDIENCE_SHARED}

| フィールド                     | タイプ                     | 説明                                                          |
| ------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                      | `string`, `null`    | このイベントのグローバルな一意の ID                                    |
| `user_id`                 | `string`, `null`    | このイベントを実行したユーザーのBraze ID                        |
| `external_user_id`        | `string`, `null`    | [PII] ユーザーの外部ユーザーID                                   |
| `device_id`               | `string`, `null`    | ユーザーが匿名の場合、このユーザーに紐づくデバイスのID |
| `app_group_id`            | `string`, `null`    | このユーザーが所属するワークスペースのBraze ID                        |
| `app_group_api_id`        | `string`, `null`    | このユーザーが所属するワークスペースのAPI ID                         |
| `time`                    | `int`, `null`       | イベントが発生したUnixタイムスタンプ                           |
| `canvas_id`               | `string`, `null`    | (Braze専用）このイベントが属するキャンバスのID          |
| `canvas_api_id`           | `string`, `null`    | このイベントが属するキャンバスのAPI ID                           |
| `canvas_variation_api_id` | `string`, `null`    | このイベントが属するキャンバスのバリエーションのAPI ID                 |
| `canvas_step_api_id`      | `string`, `null`    | このイベントが属するキャンバスステップのAPI ID                      |
| `sf_created_at`           | `timestamp`, `null` | このイベントが Snowpipe に検出されたとき                        |

{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_EXIT_PERFORMEDEVENT_SHARED {#USERS_CANVAS_EXIT_PERFORMEDEVENT_SHARED}

| フィールド                     | タイプ                     | 説明                                                          |
| ------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                      | `string`, `null`    | このイベントのグローバルな一意の ID                                    |
| `user_id`                 | `string`, `null`    | このイベントを実行したユーザーのBraze ID                        |
| `external_user_id`        | `string`, `null`    | [PII] ユーザーの外部ユーザーID                                   |
| `device_id`               | `string`, `null`    | ユーザーが匿名の場合、このユーザーに紐づくデバイスのID |
| `app_group_id`            | `string`, `null`    | このユーザーが所属するワークスペースのBraze ID                        |
| `app_group_api_id`        | `string`, `null`    | このユーザーが所属するワークスペースのAPI ID                         |
| `time`                    | `int`, `null`       | イベントが発生したUnixタイムスタンプ                           |
| `canvas_id`               | `string`, `null`    | (Braze専用）このイベントが属するキャンバスのID          |
| `canvas_api_id`           | `string`, `null`    | このイベントが属するキャンバスのAPI ID                           |
| `canvas_variation_api_id` | `string`, `null`    | このイベントが属するキャンバスのバリエーションのAPI ID                 |
| `canvas_step_api_id`      | `string`, `null`    | このイベントが属するキャンバスステップのAPI ID                      |
| `sf_created_at`           | `timestamp`, `null` | このイベントが Snowpipe に検出されたとき                        |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_EXPERIMENTSTEP_CONVERSION_SHARED {#USERS_CANVAS_EXPERIMENTSTEP_CONVERSION_SHARED}

| フィールド                       | タイプ                     | 説明                                                                                                     |
| --------------------------- | ------------------------ | --------------------------------------------------------------------------------------------------------------- |
| `id`                        | `string`, `null`    | このイベントのグローバルな一意の ID                                                                               |
| `user_id`                   | `string`, `null`    | このイベントを実行したユーザーのBraze ID                                                                   |
| `external_user_id`          | `string`, `null`    | [PII] ユーザーの外部ユーザーID                                                                              |
| `device_id`                 | `string`, `null`    | ユーザーが匿名の場合、このユーザーに紐づくデバイスのID                                            |
| `app_group_id`              | `string`, `null`    | このユーザーが所属するワークスペースのBraze ID                                                                   |
| `time`                      | `int`, `null`       | イベントが発生したUnixタイムスタンプ                                                                      |
| `app_api_id`                | `string`, `null`    | このイベントが発生したアプリのAPI ID                                                                  |
| `canvas_id`                 | `string`, `null`    | (Braze専用）このイベントが属するキャンバスのID                                                     |
| `canvas_api_id`             | `string`, `null`    | このイベントが属するキャンバスのAPI ID                                                                      |
| `canvas_variation_api_id`   | `string`, `null`    | このイベントが属するキャンバスのバリエーションのAPI ID                                                            |
| `canvas_step_api_id`        | `string`, `null`    | このイベントが属するキャンバスステップのAPI ID                                                                 |
| `experiment_step_api_id`    | `string`, `null`    | このイベントが属する実験ステップのAPI ID                                                             |
| `conversion_behavior_index` | `int`, `null`       | ユーザーが行ったコンバージョンイベントのタイプ。"0 "は一次コンバージョン、"1 "は二次コンバージョンである。 |
| `sf_created_at`             | `timestamp`, `null` | このイベントが Snowpipe に検出されたとき                                                                   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_EXPERIMENTSTEP_SPLITENTRY_SHARED {#USERS_CANVAS_EXPERIMENTSTEP_SPLITENTRY_SHARED}

| フィールド                     | タイプ                     | 説明                                                          |
| ------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                      | `string`, `null`    | このイベントのグローバルな一意の ID                                    |
| `user_id`                 | `string`, `null`    | このイベントを実行したユーザーのBraze ID                        |
| `external_user_id`        | `string`, `null`    | [PII] ユーザーの外部ユーザーID                                   |
| `device_id`               | `string`, `null`    | ユーザーが匿名の場合、このユーザーに紐づくデバイスのID |
| `app_group_id`            | `string`, `null`    | このユーザーが所属するワークスペースのBraze ID                        |
| `time`                    | `int`, `null`       | イベントが発生したUnixタイムスタンプ                           |
| `canvas_id`               | `string`, `null`    | (Braze専用）このイベントが属するキャンバスのID          |
| `canvas_api_id`           | `string`, `null`    | このイベントが属するキャンバスのAPI ID                           |
| `canvas_variation_api_id` | `string`, `null`    | このイベントが属するキャンバスのバリエーションのAPI ID                 |
| `canvas_step_api_id`      | `string`, `null`    | このイベントが属するキャンバスステップのAPI ID                      |
| `experiment_step_api_id`  | `string`, `null`    | このイベントが属する実験ステップのAPI ID                  |
| `in_control_group`        | `boolean`, `null`   | ユーザーがコントロール・グループに登録されていた場合、真となる                   |
| `sf_created_at`           | `timestamp`, `null` | このイベントが Snowpipe に検出されたとき                        |

{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_FREQUENCYCAP_SHARED {#USERS_CANVAS_FREQUENCYCAP_SHARED}

| フィールド                                  | タイプ                     | 説明                                                          |
| -------------------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                                   | `string`, `null`    | このイベントのグローバルな一意の ID                                    |
| `user_id`                              | `string`, `null`    | このイベントを実行したユーザーのBraze ID                        |
| `external_user_id`                     | `string`, `null`    | [PII] ユーザーの外部ユーザーID                                   |
| `device_id`                            | `string`, `null`    | ユーザーが匿名の場合、このユーザーに紐づくデバイスのID |
| `app_group_id`                         | `string`, `null`    | このユーザーが所属するワークスペースのBraze ID                        |
| `app_group_api_id`                     | `string`, `null`    | このユーザーが所属するワークスペースのAPI ID                         |
| `time`                                 | `int`, `null`       | イベントが発生したUnixタイムスタンプ                           |
| `canvas_id`                            | `string`, `null`    | (Braze専用）このイベントが属するキャンバスのID          |
| `canvas_api_id`                        | `string`, `null`    | このイベントが属するキャンバスのAPI ID                           |
| `canvas_variation_api_id`              | `string`, `null`    | このイベントが属するキャンバスのバリエーションのAPI ID                 |
| `canvas_step_api_id`                   | `string`, `null`    | このイベントが属するキャンバスステップのAPI ID                      |
| `canvas_step_message_variation_api_id` | `string`, `null`    | このユーザーが受け取ったキャンバスステップメッセージのバリエーションのAPI ID       |
| `channel`                              | `string`, `null`    | このイベントが属するメッセージング・チャンネル（Eメール、プッシュなど）          |
| `gender`                               | `string`, `null`    | [PII] ユーザーの性別                                             |
| `country`                              | `string`, `null`    | [PII] ユーザーの国                                            |
| `timezone`                             | `string`, `null`    | ユーザーのタイムゾーン                                                 |
| `language`                             | `string`, `null`    | [PII] ユーザーの言語                                           |
| `sf_created_at`                        | `timestamp`, `null` | このイベントが Snowpipe に検出されたとき                        |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_REVENUE_SHARED {#USERS_CANVAS_REVENUE_SHARED}

| フィールド                                  | タイプ                     | 説明                                                          |
| -------------------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                                   | `string`, `null`    | このイベントのグローバルな一意の ID                                    |
| `user_id`                              | `string`, `null`    | このイベントを実行したユーザーのBraze ID                        |
| `external_user_id`                     | `string`, `null`    | [PII] ユーザーの外部ユーザーID                                   |
| `device_id`                            | `string`, `null`    | ユーザーが匿名の場合、このユーザーに紐づくデバイスのID |
| `app_group_id`                         | `string`, `null`    | このユーザーが所属するワークスペースのBraze ID                        |
| `app_group_api_id`                     | `string`, `null`    | このユーザーが所属するワークスペースのAPI ID                         |
| `time`                                 | `int`, `null`       | イベントが発生したUnixタイムスタンプ                           |
| `canvas_id`                            | `string`, `null`    | (Braze専用）このイベントが属するキャンバスのID          |
| `canvas_api_id`                        | `string`, `null`    | このイベントが属するキャンバスのAPI ID                           |
| `canvas_variation_api_id`              | `string`, `null`    | このイベントが属するキャンバスのバリエーションのAPI ID                 |
| `canvas_step_api_id`                   | `string`, `null`    | このイベントが属するキャンバスステップのAPI ID                      |
| `canvas_step_message_variation_api_id` | `string`, `null`    | このユーザーが受け取ったキャンバスステップメッセージのバリエーションのAPI ID       |
| `gender`                               | `string`, `null`    | [PII] ユーザーの性別                                             |
| `country`                              | `string`, `null`    | [PII] ユーザーの国                                            |
| `timezone`                             | `string`, `null`    | ユーザーのタイムゾーン                                                 |
| `language`                             | `string`, `null`    | [PII] ユーザーの言語                                           |
| `revenue`                              | `int`, `null`       | 米ドル建てで発生した収益額（セント表示               |
| `sf_created_at`                        | `timestamp`, `null` | このイベントが Snowpipe に検出されたとき                        |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## メッセージ

### USERS_MESSAGES_CONTENTCARD_ABORT_SHARED {#USERS_MESSAGES_CONTENTCARD_ABORT_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザーID
`device_id` | `null,` `string` | ユーザーが匿名の場合、このユーザーに関連付けられる `device_id`
`app_group_api_id` | `null,` `string` | このユーザーが所属するワークスペースのAPI ID
`time` | `int` | イベントが発生したUnixタイムスタンプ
`dispatch_id` | `null,` `string` | このメッセージが属するディスパッチの ID
`send_id` | `null,` `string` | このメッセージが属するメッセージ送信ID
`campaign_id` | `null,` `string` | このイベントが属するキャンペーンの内部用Braze ID
`campaign_api_id` | `null,` `string` | このイベントが属するキャンペーンのAPI ID
`message_variation_api_id` | `null,` `string` | このユーザーが受信したメッセージバリエーションのAPI ID
`canvas_id` | `null,` `string` | このイベントが属するキャンバスの内部使用Braze ID
`canvas_api_id` | `null,` `string` | このイベントが属するキャンバスのAPI ID
`canvas_variation_api_id` | `null,` `string` | このイベントが属するキャンバスのバリエーションのAPI ID
`canvas_step_api_id` | `null,` `string` | このイベントが属するキャンバスステップのAPI ID
`canvas_step_message_variation_api_id` | `null,` `string` | このユーザーが受け取ったキャンバスステップメッセージのバリエーションのAPI ID
`gender` | `null,` `string` | [PII] ユーザーの性別
`country` | `null,` `string` | [PII] ユーザーの国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
`abort_type` | `null,` `string` | 中止のタイプ。`liquid_abort_message` または `rate_limit` のいずれか
`abort_log` | `null,` `string` | [PII] 中止の詳細を記述するログメッセージ (最大 128 文字)
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_CONTENTCARD_CLICK_SHARED {#USERS_MESSAGES_CONTENTCARD_CLICK_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーのBraze ID
`content_card_id` | `string` | このイベントを発生させたカードのID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザーID
`app_group_api_id` | `null,` `string` | このユーザーが所属するワークスペースのAPI ID
`time` | `int` | イベントが発生したUnixタイムスタンプ
`app_api_id` | `null,` `string` | このイベントが発生したアプリのAPI ID
`dispatch_id` | `null,` `string` | このメッセージが属するディスパッチの ID
`send_id` | `null,` `string` | このメッセージが属するメッセージ送信ID
`campaign_id` | `null,` `string` | このイベントが属するキャンペーンの内部用Braze ID
`campaign_api_id` | `null,` `string` | このイベントが属するキャンペーンのAPI ID
`message_variation_api_id` | `null,` `string` | このユーザーが受信したメッセージバリエーションのAPI ID
`canvas_id` | `null,` `string` | このイベントが属するキャンバスの内部使用Braze ID
`canvas_api_id` | `null,` `string` | このイベントが属するキャンバスのAPI ID
`canvas_variation_api_id` | `null,` `string` | このイベントが属するキャンバスのバリエーションのAPI ID
`canvas_step_api_id` | `null,` `string` | このイベントが属するキャンバスステップのAPI ID
`canvas_step_message_variation_api_id` | `null,` `string` | このユーザーが受け取ったキャンバスステップメッセージのバリエーションのAPI ID
`gender` | `null,` `string` | [PII] ユーザーの性別
`country` | `null,` `string` | [PII] ユーザーの国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
`device_id` | `null,` `string` | イベントが発生したデバイスの ID
`sdk_version` | `null,` `string` | イベント中に使用されたBraze SDKのバージョン
`platform` | `null,` `string` | デバイスのプラットフォーム
`os_version` | `null,` `string` | デバイスのオペレーティング・システムのバージョン
`device_model` | `null,` `string` | デバイスのモデル
`resolution` | `null,` `string` | デバイスの解像度
`carrier` | `null,` `string` | デバイスの通信事業者
`browser` | `null,` `string` | デバイスのブラウザ
`ad_id` | `null,` `string` | [PII] 広告識別子
`ad_id_type` | `null,` `string` | `ios_idfa`、`google_ad_id`、`windows_ad_id`、`roku_ad_id` のいずれか
`ad_tracking_enabled` | `null, boolean` | デバイスの広告トラッキングが有効かどうか
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_CONTENTCARD_DISMISS_SHARED {#USERS_MESSAGES_CONTENTCARD_DISMISS_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーのBraze ID
`content_card_id` | `string` | このイベントを発生させたカードのID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザーID
`app_group_api_id` | `null,` `string` | このユーザーが所属するワークスペースのAPI ID
`time` | `int` | イベントが発生したUnixタイムスタンプ
`app_api_id` | `null,` `string` | このイベントが発生したアプリのAPI ID
`dispatch_id` | `null,` `string` | このメッセージが属するディスパッチの ID
`send_id` | `null,` `string` | このメッセージが属するメッセージ送信ID
`campaign_id` | `null,` `string` | このイベントが属するキャンペーンの内部用Braze ID
`campaign_api_id` | `null,` `string` | このイベントが属するキャンペーンのAPI ID
`message_variation_api_id` | `null,` `string` | このユーザーが受信したメッセージバリエーションのAPI ID
`canvas_id` | `null,` `string` | このイベントが属するキャンバスの内部使用Braze ID
`canvas_api_id` | `null,` `string` | このイベントが属するキャンバスのAPI ID
`canvas_variation_api_id` | `null,` `string` | このイベントが属するキャンバスのバリエーションのAPI ID
`canvas_step_api_id` | `null,` `string` | このイベントが属するキャンバスステップのAPI ID
`canvas_step_message_variation_api_id` | `null,` `string` | このユーザーが受け取ったキャンバスステップメッセージのバリエーションのAPI ID
`gender` | `null,` `string` | [PII] ユーザーの性別
`country` | `null,` `string` | [PII] ユーザーの国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
`device_id` | `null,` `string` | イベントが発生したデバイスの ID
`sdk_version` | `null,` `string` | イベント中に使用されたBraze SDKのバージョン
`platform` | `null,` `string` | デバイスのプラットフォーム
`os_version` | `null,` `string` | デバイスのオペレーティング・システムのバージョン
`device_model` | `null,` `string` | デバイスのモデル
`resolution` | `null,` `string` | デバイスの解像度
`carrier` | `null,` `string` | デバイスの通信事業者
`browser` | `null,` `string` | デバイスのブラウザ
`ad_id` | `null,` `string` | [PII] 広告識別子
`ad_id_type` | `null,` `string` | `ios_idfa`、`google_ad_id`、`windows_ad_id`、`roku_ad_id` のいずれか
`ad_tracking_enabled` | `null, boolean` | デバイスの広告トラッキングが有効かどうか
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_CONTENTCARD_IMPRESSION_SHARED {#USERS_MESSAGES_CONTENTCARD_IMPRESSION_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーのBraze ID
`content_card_id` | `string` | このイベントを発生させたカードのID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザーID
`app_group_api_id` | `null,` `string` | このユーザーが所属するワークスペースのAPI ID
`time` | `int` | イベントが発生したUnixタイムスタンプ
`app_api_id` | `null,` `string` | このイベントが発生したアプリのAPI ID
`dispatch_id` | `null,` `string` | このメッセージが属するディスパッチの ID
`send_id` | `null,` `string` | このメッセージが属するメッセージ送信ID
`campaign_id` | `null,` `string` | このイベントが属するキャンペーンの内部用Braze ID
`campaign_api_id` | `null,` `string` | このイベントが属するキャンペーンのAPI ID
`message_variation_api_id` | `null,` `string` | このユーザーが受信したメッセージバリエーションのAPI ID
`canvas_id` | `null,` `string` | このイベントが属するキャンバスの内部使用Braze ID
`canvas_api_id` | `null,` `string` | このイベントが属するキャンバスのAPI ID
`canvas_variation_api_id` | `null,` `string` | このイベントが属するキャンバスのバリエーションのAPI ID
`canvas_step_api_id` | `null,` `string` | このイベントが属するキャンバスステップのAPI ID
`canvas_step_message_variation_api_id` | `null,` `string` | このユーザーが受け取ったキャンバスステップメッセージのバリエーションのAPI ID
`gender` | `null,` `string` | [PII] ユーザーの性別
`country` | `null,` `string` | [PII] ユーザーの国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
`device_id` | `null,` `string` | イベントが発生したデバイスの ID
`sdk_version` | `null,` `string` | イベント中に使用されたBraze SDKのバージョン
`platform` | `null,` `string` | デバイスのプラットフォーム
`os_version` | `null,` `string` | デバイスのオペレーティング・システムのバージョン
`device_model` | `null,` `string` | デバイスのモデル
`resolution` | `null,` `string` | デバイスの解像度
`carrier` | `null,` `string` | デバイスの通信事業者
`browser` | `null,` `string` | デバイスのブラウザ
`ad_id` | `null,` `string` | [PII] 広告識別子
`ad_id_type` | `null,` `string` | `ios_idfa`、`google_ad_id`、`windows_ad_id`、`roku_ad_id` のいずれか
`ad_tracking_enabled` | `null, boolean` | デバイスの広告トラッキングが有効かどうか
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_CONTENTCARD_SEND_SHARED {#USERS_MESSAGES_CONTENTCARD_SEND_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザーID
`device_id` | `null,` `string` | ユーザーが匿名の場合、このユーザーに関連付けられる `device_id`
`app_group_api_id` | `null,` `string` | このユーザーが所属するワークスペースのAPI ID
`time` | `int` | イベントが発生したUnixタイムスタンプ
`dispatch_id` | `null,` `string` | このメッセージが属するディスパッチの ID
`send_id` | `null,` `string` | このメッセージが属するメッセージ送信ID
`campaign_id` | `null,` `string` | このイベントが属するキャンペーンの内部用Braze ID
`campaign_api_id` | `null,` `string` | このイベントが属するキャンペーンのAPI ID
`message_variation_api_id` | `null,` `string` | このユーザーが受信したメッセージバリエーションのAPI ID
`canvas_id` | `null,` `string` | このイベントが属するキャンバスの内部使用Braze ID
`canvas_api_id` | `null,` `string` | このイベントが属するキャンバスのAPI ID
`canvas_variation_api_id` | `null,` `string` | このイベントが属するキャンバスのバリエーションのAPI ID
`canvas_step_api_id` | `null,` `string` | このイベントが属するキャンバスステップのAPI ID
`canvas_step_message_variation_api_id` | `null,` `string` | このユーザーが受け取ったキャンバスステップメッセージのバリエーションのAPI ID
`gender` | `null,` `string` | [PII] ユーザーの性別
`country` | `null,` `string` | [PII] ユーザーの国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
`content_card_id` | `string` | このイベントを発生させたカードのID
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_ABORT_SHARED {#USERS_MESSAGES_EMAIL_ABORT_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザーID
`device_id` | `null,` `string` | ユーザーが匿名の場合、このユーザーに関連付けられる `device_id`
`app_group_api_id` | `null,` `string` | このユーザーが所属するワークスペースのAPI ID
`time` | `int` | イベントが発生したUnixタイムスタンプ
`dispatch_id` | `null,` `string` | このメッセージが属するディスパッチの ID
`send_id` | `null,` `string` | このメッセージが属するメッセージ送信ID
`campaign_id` | `null,` `string` | このイベントが属するキャンペーンの内部用Braze ID
`campaign_api_id` | `null,` `string` | このイベントが属するキャンペーンのAPI ID
`message_variation_api_id` | `null,` `string` | このユーザーが受信したメッセージバリエーションのAPI ID
`canvas_id` | `null,` `string` | このイベントが属するキャンバスの内部使用Braze ID
`canvas_api_id` | `null,` `string` | このイベントが属するキャンバスのAPI ID
`canvas_variation_api_id` | `null,` `string` | このイベントが属するキャンバスのバリエーションのAPI ID
`canvas_step_api_id` | `null,` `string` | このイベントが属するキャンバスステップのAPI ID
`canvas_step_message_variation_api_id` | `null,` `string` | このユーザーが受け取ったキャンバスステップメッセージのバリエーションのAPI ID
`gender` | `null,` `string` | [PII] ユーザーの性別
`country` | `null,` `string` | [PII] ユーザーの国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
`email_address` | `string` | [PII] ユーザーのメールアドレス
`ip_pool` | `null,` `string` | メール送信元のIPプール
`abort_type` | `null,` `string` | 中止のタイプ。`liquid_abort_message` または `rate_limit` のいずれか
`abort_log` | `null,` `string` | [PII] 中止の詳細を記述するログメッセージ (最大 128 文字)
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_BOUNCE_SHARED {#USERS_MESSAGES_EMAIL_BOUNCE_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザーID
`device_id` | `null,` `string` | ユーザーが匿名の場合、このユーザーに関連付けられる `device_id`
`app_group_api_id` | `null,` `string` | このユーザーが所属するワークスペースのAPI ID
`time` | `int` | イベントが発生したUnixタイムスタンプ
`dispatch_id` | `null,` `string` | このメッセージが属するディスパッチの ID
`send_id` | `null,` `string` | このメッセージが属するメッセージ送信ID
`campaign_id` | `null,` `string` | このイベントが属するキャンペーンの内部用Braze ID
`campaign_api_id` | `null,` `string` | このイベントが属するキャンペーンのAPI ID
`message_variation_api_id` | `null,` `string` | このユーザーが受信したメッセージバリエーションのAPI ID
`canvas_id` | `null,` `string` | このイベントが属するキャンバスの内部使用Braze ID
`canvas_api_id` | `null,` `string` | このイベントが属するキャンバスのAPI ID
`canvas_variation_api_id` | `null,` `string` | このイベントが属するキャンバスのバリエーションのAPI ID
`canvas_step_api_id` | `null,` `string` | このイベントが属するキャンバスステップのAPI ID
`canvas_step_message_variation_api_id` | `null,` `string` | このユーザーが受け取ったキャンバスステップメッセージのバリエーションのAPI ID
`gender` | `null,` `string` | [PII] ユーザーの性別
`country` | `null,` `string` | [PII] ユーザーの国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
`email_address` | `string` | [PII] ユーザーのメールアドレス
`sending_ip` | `null,` `string` | メール送信元のIPアドレス
`ip_pool` | `null,` `string` | メール送信元のIPプール
`bounce_reason` | `null,` `string` | [PII] このバウンスイベントで受信したSMTP理由コードとユーザーフレンドリーメッセージ
`esp` | `null,` `string` | イベントに関連する ESP (SparkPost、SendGrid、または Amazon SES)
`from_domain` | `null,` `string` | メールの送信ドメイン
`is_drop` | `null, boolean` | このイベントがドロップイベントとしてカウントされることを示す。
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_CLICK_SHARED {#USERS_MESSAGES_EMAIL_CLICK_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザーID
`device_id` | `null,` `string` | ユーザーが匿名の場合、このユーザーに関連付けられる `device_id`
`app_group_api_id` | `null,` `string` | このユーザーが所属するワークスペースのAPI ID
`time` | `int` | イベントが発生したUnixタイムスタンプ
`dispatch_id` | `null,` `string` | このメッセージが属するディスパッチの ID
`send_id` | `null,` `string` | このメッセージが属するメッセージ送信ID
`campaign_id` | `null,` `string` | このイベントが属するキャンペーンの内部用Braze ID
`campaign_api_id` | `null,` `string` | このイベントが属するキャンペーンのAPI ID
`message_variation_api_id` | `null,` `string` | このユーザーが受信したメッセージバリエーションのAPI ID
`canvas_id` | `null,` `string` | このイベントが属するキャンバスの内部使用Braze ID
`canvas_api_id` | `null,` `string` | このイベントが属するキャンバスのAPI ID
`canvas_variation_api_id` | `null,` `string` | このイベントが属するキャンバスのバリエーションのAPI ID
`canvas_step_api_id` | `null,` `string` | このイベントが属するキャンバスステップのAPI ID
`canvas_step_message_variation_api_id` | `null,` `string` | このユーザーが受け取ったキャンバスステップメッセージのバリエーションのAPI ID
`gender` | `null,` `string` | [PII] ユーザーの性別
`country` | `null,` `string` | [PII] ユーザーの国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
`email_address` | `string` | [PII] ユーザーのメールアドレス
`url` | `null,` `string` | ユーザーがクリックしたURL
`user_agent` | `null,` `string` | クリックが発生したユーザーエージェント
`ip_pool` | `null,` `string` | メール送信元のIPプール
`link_id` | `null,` `string` | Brazeが作成した、クリックされたリンクのユニークID。
`link_alias` | `null,` `string` | このリンクIDに関連するエイリアス
`esp` | `null,` `string` | イベントに関連する ESP (SparkPost、SendGrid、または Amazon SES)
`from_domain` | `null,` `string` | メールの送信ドメイン
`is_amp` | `null, boolean` | AMPイベントであることを示す
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_DELIVERY_SHARED {#USERS_MESSAGES_EMAIL_DELIVERY_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザーID
`device_id` | `null,` `string` | ユーザーが匿名の場合、このユーザーに関連付けられる `device_id`
`app_group_api_id` | `null,` `string` | このユーザーが所属するワークスペースのAPI ID
`time` | `int` | イベントが発生したUnixタイムスタンプ
`dispatch_id` | `null,` `string` | このメッセージが属するディスパッチの ID
`send_id` | `null,` `string` | このメッセージが属するメッセージ送信ID
`campaign_id` | `null,` `string` | このイベントが属するキャンペーンの内部用Braze ID
`campaign_api_id` | `null,` `string` | このイベントが属するキャンペーンのAPI ID
`message_variation_api_id` | `null,` `string` | このユーザーが受信したメッセージバリエーションのAPI ID
`canvas_id` | `null,` `string` | このイベントが属するキャンバスの内部使用Braze ID
`canvas_api_id` | `null,` `string` | このイベントが属するキャンバスのAPI ID
`canvas_variation_api_id` | `null,` `string` | このイベントが属するキャンバスのバリエーションのAPI ID
`canvas_step_api_id` | `null,` `string` | このイベントが属するキャンバスステップのAPI ID
`canvas_step_message_variation_api_id` | `null,` `string` | このユーザーが受け取ったキャンバスステップメッセージのバリエーションのAPI ID
`gender` | `null,` `string` | [PII] ユーザーの性別
`country` | `null,` `string` | [PII] ユーザーの国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
`email_address` | `string` | [PII] ユーザーのメールアドレス
`sending_ip` | `null,` `string` | メールの送信元IPアドレス
`ip_pool` | `null,` `string` | メール送信元のIPプール
`esp` | `null,` `string` | イベントに関連する ESP (SparkPost、SendGrid、または Amazon SES)
`from_domain` | `null,` `string` | メールの送信ドメイン
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_MARKASSPAM_SHARED {#USERS_MESSAGES_EMAIL_MARKASSPAM_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザーID
`device_id` | `null,` `string` | ユーザーが匿名の場合、このユーザーに関連付けられる `device_id`
`app_group_api_id` | `null,` `string` | このユーザーが所属するワークスペースのAPI ID
`time` | `int` | イベントが発生したUnixタイムスタンプ
`dispatch_id` | `null,` `string` | このメッセージが属するディスパッチの ID
`send_id` | `null,` `string` | このメッセージが属するメッセージ送信ID
`campaign_id` | `null,` `string` | このイベントが属するキャンペーンの内部用Braze ID
`campaign_api_id` | `null,` `string` | このイベントが属するキャンペーンのAPI ID
`message_variation_api_id` | `null,` `string` | このユーザーが受信したメッセージバリエーションのAPI ID
`canvas_id` | `null,` `string` | このイベントが属するキャンバスの内部使用Braze ID
`canvas_api_id` | `null,` `string` | このイベントが属するキャンバスのAPI ID
`canvas_variation_api_id` | `null,` `string` | このイベントが属するキャンバスのバリエーションのAPI ID
`canvas_step_api_id` | `null,` `string` | このイベントが属するキャンバスステップのAPI ID
`canvas_step_message_variation_api_id` | `null,` `string` | このユーザーが受け取ったキャンバスステップメッセージのバリエーションのAPI ID
`gender` | `null,` `string` | [PII] ユーザーの性別
`country` | `null,` `string` | [PII] ユーザーの国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
`email_address` | `string` | [PII] ユーザーのメールアドレス
`user_agent` | `null,` `string` | スパム報告が発生したユーザーエージェント
`ip_pool` | `null,` `string` | メール送信元のIPプール
`esp` | `null,` `string` | イベントに関連する ESP (SparkPost、SendGrid、または Amazon SES)
`from_domain` | `null,` `string` | メールの送信ドメイン
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_OPEN_SHARED {#USERS_MESSAGES_EMAIL_OPEN_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザーID
`device_id` | `null,` `string` | ユーザーが匿名の場合、このユーザーに関連付けられる `device_id`
`app_group_api_id` | `null,` `string` | このユーザーが所属するワークスペースのAPI ID
`time` | `int` | イベントが発生したUnixタイムスタンプ
`dispatch_id` | `null,` `string` | このメッセージが属するディスパッチの ID
`send_id` | `null,` `string` | このメッセージが属するメッセージ送信ID
`campaign_id` | `null,` `string` | このイベントが属するキャンペーンの内部用Braze ID
`campaign_api_id` | `null,` `string` | このイベントが属するキャンペーンのAPI ID
`message_variation_api_id` | `null,` `string` | このユーザーが受信したメッセージバリエーションのAPI ID
`canvas_id` | `null,` `string` | このイベントが属するキャンバスの内部使用Braze ID
`canvas_api_id` | `null,` `string` | このイベントが属するキャンバスのAPI ID
`canvas_variation_api_id` | `null,` `string` | このイベントが属するキャンバスのバリエーションのAPI ID
`canvas_step_api_id` | `null,` `string` | このイベントが属するキャンバスステップのAPI ID
`canvas_step_message_variation_api_id` | `null,` `string` | このユーザーが受け取ったキャンバスステップメッセージのバリエーションのAPI ID
`gender` | `null,` `string` | [PII] ユーザーの性別
`country` | `null,` `string` | [PII] ユーザーの国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
`email_address` | `string` | [PII] ユーザーのメールアドレス
`user_agent` | `null,` `string` | オープンが発生したユーザーエージェント
`ip_pool` | `null,` `string` | メール送信元のIPプール
`machine_open` | `null,` `string` | 例えば、メールのプライバシー保護が有効になっているAppleデバイスによって、ユーザーの関与なしに開封イベントがトリガーされた場合、'true'が入力される。値は、より詳細な情報を提供するために、時間の経過とともに変化する可能性があります。
`esp` | `null,` `string` | イベントに関連する ESP (SparkPost、SendGrid、または Amazon SES)
`from_domain` | `null,` `string` | メールの送信ドメイン
`is_amp` | `null, boolean` | AMPイベントであることを示す
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_SEND_SHARED {#USERS_MESSAGES_EMAIL_SEND_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザーID
`device_id` | `null,` `string` | ユーザーが匿名の場合、このユーザーに関連付けられる `device_id`
`app_group_api_id` | `null,` `string` | このユーザーが所属するワークスペースのAPI ID
`time` | `int` | イベントが発生したUnixタイムスタンプ
`dispatch_id` | `null,` `string` | このメッセージが属するディスパッチの ID
`send_id` | `null,` `string` | このメッセージが属するメッセージ送信ID
`campaign_id` | `null,` `string` | このイベントが属するキャンペーンの内部用Braze ID
`campaign_api_id` | `null,` `string` | このイベントが属するキャンペーンのAPI ID
`message_variation_api_id` | `null,` `string` | このユーザーが受信したメッセージバリエーションのAPI ID
`canvas_id` | `null,` `string` | このイベントが属するキャンバスの内部使用Braze ID
`canvas_api_id` | `null,` `string` | このイベントが属するキャンバスのAPI ID
`canvas_variation_api_id` | `null,` `string` | このイベントが属するキャンバスのバリエーションのAPI ID
`canvas_step_api_id` | `null,` `string` | このイベントが属するキャンバスステップのAPI ID
`canvas_step_message_variation_api_id` | `null,` `string` | このユーザーが受け取ったキャンバスステップメッセージのバリエーションのAPI ID
`gender` | `null,` `string` | [PII] ユーザーの性別
`country` | `null,` `string` | [PII] ユーザーの国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
`email_address` | `string` | [PII] ユーザーのメールアドレス
`ip_pool` | `null,` `string` | メール送信元のIPプール
`message_extras` | `null,` `string` | [PII] リキッドレンダリング時にタグ付けされたキーと値のペアのJSON文字列
`esp` | `null,` `string` | イベントに関連する ESP (SparkPost、SendGrid、または Amazon SES)
`from_domain` | `null,` `string` | メールの送信ドメイン
`sf_created_at` | `timestamp`, `null` | このイベントが Snowpipe に検出されたとき
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_SOFTBOUNCE_SHARED {#USERS_MESSAGES_EMAIL_SOFTBOUNCE_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザーID
`device_id` | `null,` `string` | ユーザーが匿名の場合、このユーザーに関連付けられる `device_id`
`app_group_api_id` | `null,` `string` | このユーザーが所属するワークスペースのAPI ID
`time` | `int` | イベントが発生したUnixタイムスタンプ
`dispatch_id` | `null,` `string` | このメッセージが属するディスパッチの ID
`send_id` | `null,` `string` | このメッセージが属するメッセージ送信ID
`campaign_id` | `null,` `string` | このイベントが属するキャンペーンの内部用Braze ID
`campaign_api_id` | `null,` `string` | このイベントが属するキャンペーンのAPI ID
`message_variation_api_id` | `null,` `string` | このユーザーが受信したメッセージバリエーションのAPI ID
`canvas_id` | `null,` `string` | このイベントが属するキャンバスの内部使用Braze ID
`canvas_api_id` | `null,` `string` | このイベントが属するキャンバスのAPI ID
`canvas_variation_api_id` | `null,` `string` | このイベントが属するキャンバスのバリエーションのAPI ID
`canvas_step_api_id` | `null,` `string` | このイベントが属するキャンバスステップのAPI ID
`canvas_step_message_variation_api_id` | `null,` `string` | このユーザーが受け取ったキャンバスステップメッセージのバリエーションのAPI ID
`gender` | `null,` `string` | [PII] ユーザーの性別
`country` | `null,` `string` | [PII] ユーザーの国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
`email_address` | `string` | [PII] ユーザーのメールアドレス
`sending_ip` | `null,` `string` | メール送信元のIPアドレス
`ip_pool` | `null,` `string` | メール送信元のIPプール
`bounce_reason` | `null,` `string` | [PII] このバウンスイベントで受信したSMTP理由コードとユーザーフレンドリーメッセージ
`esp` | `null,` `string` | イベントに関連する ESP (SparkPost、SendGrid、または Amazon SES)
`from_domain` | `null,` `string` | メールの送信ドメイン
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED {#USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザーID
`device_id` | `null,` `string` | ユーザーが匿名の場合、このユーザーに関連付けられる `device_id`
`app_group_api_id` | `null,` `string` | このユーザーが所属するワークスペースのAPI ID
`time` | `int` | イベントが発生したUnixタイムスタンプ
`dispatch_id` | `null,` `string` | このメッセージが属するディスパッチの ID
`send_id` | `null,` `string` | このメッセージが属するメッセージ送信ID
`campaign_id` | `null,` `string` | このイベントが属するキャンペーンの内部用Braze ID
`campaign_api_id` | `null,` `string` | このイベントが属するキャンペーンのAPI ID
`message_variation_api_id` | `null,` `string` | このユーザーが受信したメッセージバリエーションのAPI ID
`canvas_id` | `null,` `string` | このイベントが属するキャンバスの内部使用Braze ID
`canvas_api_id` | `null,` `string` | このイベントが属するキャンバスのAPI ID
`canvas_variation_api_id` | `null,` `string` | このイベントが属するキャンバスのバリエーションのAPI ID
`canvas_step_api_id` | `null,` `string` | このイベントが属するキャンバスステップのAPI ID
`canvas_step_message_variation_api_id` | `null,` `string` | このユーザーが受け取ったキャンバスステップメッセージのバリエーションのAPI ID
`gender` | `null,` `string` | [PII] ユーザーの性別
`country` | `null,` `string` | [PII] ユーザーの国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
`email_address` | `string` | [PII] ユーザーのメールアドレス
`ip_pool` | `null,` `string` | メール送信元のIPプール
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_INAPPMESSAGE_ABORT_SHARED {#USERS_MESSAGES_INAPPMESSAGE_ABORT_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザーID
`app_group_api_id` | `null,` `string` | このユーザーが所属するワークスペースのAPI ID
`time` | `int` | イベントが発生したUnixタイムスタンプ
`app_api_id` | `null,` `string` | このイベントが発生したアプリのAPI ID
`card_api_id` | `null,` `string` | カードのAPI ID
`dispatch_id` | `null,` `string` | このメッセージが属するディスパッチの ID
`send_id` | `null,` `string` | このメッセージが属するメッセージ送信ID
`campaign_id` | `null,` `string` | このイベントが属するキャンペーンの内部用Braze ID
`campaign_api_id` | `null,` `string` | このイベントが属するキャンペーンのAPI ID
`message_variation_api_id` | `null,` `string` | このユーザーが受信したメッセージバリエーションのAPI ID
`canvas_id` | `null,` `string` | このイベントが属するキャンバスの内部使用Braze ID
`canvas_api_id` | `null,` `string` | このイベントが属するキャンバスのAPI ID
`canvas_variation_api_id` | `null,` `string` | このイベントが属するキャンバスのバリエーションのAPI ID
`canvas_step_api_id` | `null,` `string` | このイベントが属するキャンバスステップのAPI ID
`canvas_step_message_variation_api_id` | `null,` `string` | このユーザーが受け取ったキャンバスステップメッセージのバリエーションのAPI ID
`gender` | `null,` `string` | [PII] ユーザーの性別
`country` | `null,` `string` | [PII] ユーザーの国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
`device_id` | `null,` `string` | イベントが発生したデバイスの ID
`sdk_version` | `null,` `string` | イベント中に使用されたBraze SDKのバージョン
`platform` | `null,` `string` | デバイスのプラットフォーム
`os_version` | `null,` `string` | デバイスのオペレーティング・システムのバージョン
`device_model` | `null,` `string` | デバイスのモデル
`resolution` | `null,` `string` | デバイスの解像度
`carrier` | `null,` `string` | デバイスの通信事業者
`browser` | `null,` `string` | デバイスのブラウザ
`version` | `string` | アプリ内メッセージのバージョン、レガシーまたはトリガー済み
`ad_id` | `null,` `string` | [PII] 広告識別子
`ad_id_type` | `null,` `string` | `ios_idfa`、`google_ad_id`、`windows_ad_id`、`roku_ad_id` のいずれか
`ad_tracking_enabled` | `null, boolean` | デバイスの広告トラッキングが有効かどうか
`abort_type` | `null,` `string` | 中止のタイプ。`liquid_abort_message` または `rate_limit` のいずれか
`abort_log` | `null,` `string` | [PII] 中止の詳細を記述するログメッセージ (最大 128 文字)
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_INAPPMESSAGE_CLICK_SHARED {#USERS_MESSAGES_INAPPMESSAGE_CLICK_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザーID
`app_group_api_id` | `null,` `string` | このユーザーが所属するワークスペースのAPI ID
`time` | `int` | イベントが発生したUnixタイムスタンプ
`app_api_id` | `null,` `string` | このイベントが発生したアプリのAPI ID
`card_api_id` | `null,` `string` | カードのAPI ID
`dispatch_id` | `null,` `string` | このメッセージが属するディスパッチの ID
`send_id` | `null,` `string` | このメッセージが属するメッセージ送信ID
`campaign_id` | `null,` `string` | このイベントが属するキャンペーンの内部用Braze ID
`campaign_api_id` | `null,` `string` | このイベントが属するキャンペーンのAPI ID
`message_variation_api_id` | `null,` `string` | このユーザーが受信したメッセージバリエーションのAPI ID
`canvas_id` | `null,` `string` | このイベントが属するキャンバスの内部使用Braze ID
`canvas_api_id` | `null,` `string` | このイベントが属するキャンバスのAPI ID
`canvas_variation_api_id` | `null,` `string` | このイベントが属するキャンバスのバリエーションのAPI ID
`canvas_step_api_id` | `null,` `string` | このイベントが属するキャンバスステップのAPI ID
`canvas_step_message_variation_api_id` | `null,` `string` | このユーザーが受け取ったキャンバスステップメッセージのバリエーションのAPI ID
`gender` | `null,` `string` | [PII] ユーザーの性別
`country` | `null,` `string` | [PII] ユーザーの国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
`device_id` | `null,` `string` | イベントが発生したデバイスの ID
`sdk_version` | `null,` `string` | イベント中に使用されたBraze SDKのバージョン
`platform` | `null,` `string` | デバイスのプラットフォーム
`os_version` | `null,` `string` | デバイスのオペレーティング・システムのバージョン
`device_model` | `null,` `string` | デバイスのモデル
`resolution` | `null,` `string` | デバイスの解像度
`carrier` | `null,` `string` | デバイスの通信事業者
`browser` | `null,` `string` | デバイスのブラウザ
`version` | `string` | アプリ内メッセージのバージョン、レガシーまたはトリガー済み
`button_id` | `null,` `string` | クリックされたボタンの ID (このクリックがボタンのクリックを表す場合)
`ad_id` | `null,` `string` | [PII] 広告識別子
`ad_id_type` | `null,` `string` | `ios_idfa`、`google_ad_id`、`windows_ad_id`、`roku_ad_id` のいずれか
`ad_tracking_enabled` | `null, boolean` | デバイスの広告トラッキングが有効かどうか
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_INAPPMESSAGE_IMPRESSION_SHARED {#USERS_MESSAGES_INAPPMESSAGE_IMPRESSION_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザーID
`app_group_api_id` | `null,` `string` | このユーザーが所属するワークスペースのAPI ID
`time` | `int` | イベントが発生したUnixタイムスタンプ
`app_api_id` | `null,` `string` | このイベントが発生したアプリのAPI ID
`card_api_id` | `null,` `string` | カードのAPI ID
`dispatch_id` | `null,` `string` | このメッセージが属するディスパッチの ID
`send_id` | `null,` `string` | このメッセージが属するメッセージ送信ID
`campaign_id` | `null,` `string` | このイベントが属するキャンペーンの内部用Braze ID
`campaign_api_id` | `null,` `string` | このイベントが属するキャンペーンのAPI ID
`message_variation_api_id` | `null,` `string` | このユーザーが受信したメッセージバリエーションのAPI ID
`canvas_id` | `null,` `string` | このイベントが属するキャンバスの内部使用Braze ID
`canvas_api_id` | `null,` `string` | このイベントが属するキャンバスのAPI ID
`canvas_variation_api_id` | `null,` `string` | このイベントが属するキャンバスのバリエーションのAPI ID
`canvas_step_api_id` | `null,` `string` | このイベントが属するキャンバスステップのAPI ID
`canvas_step_message_variation_api_id` | `null,` `string` | このユーザーが受け取ったキャンバスステップメッセージのバリエーションのAPI ID
`gender` | `null,` `string` | [PII] ユーザーの性別
`country` | `null,` `string` | [PII] ユーザーの国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
`device_id` | `null,` `string` | イベントが発生したデバイスの ID
`sdk_version` | `null,` `string` | イベント中に使用されたBraze SDKのバージョン
`platform` | `null,` `string` | デバイスのプラットフォーム
`os_version` | `null,` `string` | デバイスのオペレーティング・システムのバージョン
`device_model` | `null,` `string` | デバイスのモデル
`resolution` | `null,` `string` | デバイスの解像度
`carrier` | `null,` `string` | デバイスの通信事業者
`browser` | `null,` `string` | デバイスのブラウザ
`version` | `string` | アプリ内メッセージのバージョン、レガシーまたはトリガー済み
`ad_id` | `null,` `string` | [PII] 広告識別子
`ad_id_type` | `null,` `string` | `ios_idfa`、`google_ad_id`、`windows_ad_id`、`roku_ad_id` のいずれか
`ad_tracking_enabled` | `null, boolean` | デバイスの広告トラッキングが有効かどうか
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_NEWSFEEDCARD_ABORT_SHARED {#USERS_MESSAGES_NEWSFEEDCARD_ABORT_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザーID
`app_group_api_id` | `null,` `string` | このユーザーが所属するワークスペースのAPI ID
`time` | `int` | イベントが発生したUnixタイムスタンプ
`app_api_id` | `null,` `string` | このイベントが発生したアプリのAPI ID
`card_api_id` | `null,` `string` | カードのAPI ID
`gender` | `null,` `string` | [PII] ユーザーの性別
`country` | `null,` `string` | [PII] ユーザーの国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
`device_id` | `null,` `string` | イベントが発生したデバイスの ID
`sdk_version` | `null,` `string` | イベント中に使用されたBraze SDKのバージョン
`platform` | `null,` `string` | デバイスのプラットフォーム
`os_version` | `null,` `string` | デバイスのオペレーティング・システムのバージョン
`device_model` | `null,` `string` | デバイスのモデル
`resolution` | `null,` `string` | デバイスの解像度
`carrier` | `null,` `string` | デバイスの通信事業者
`browser` | `null,` `string` | デバイスのブラウザ
`abort_type` | `null,` `string` | 中止のタイプ。`liquid_abort_message` または `rate_limit` のいずれか
`abort_log` | `null,` `string` | [PII] 中止の詳細を記述するログメッセージ (最大 128 文字)
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_NEWSFEEDCARD_CLICK_SHARED {#USERS_MESSAGES_NEWSFEEDCARD_CLICK_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザーID
`app_group_api_id` | `null,` `string` | このユーザーが所属するワークスペースのAPI ID
`time` | `int` | イベントが発生したUnixタイムスタンプ
`app_api_id` | `null,` `string` | このイベントが発生したアプリのAPI ID
`card_api_id` | `null,` `string` | カードのAPI ID
`gender` | `null,` `string` | [PII] ユーザーの性別
`country` | `null,` `string` | [PII] ユーザーの国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
`device_id` | `null,` `string` | イベントが発生したデバイスの ID
`sdk_version` | `null,` `string` | イベント中に使用されたBraze SDKのバージョン
`platform` | `null,` `string` | デバイスのプラットフォーム
`os_version` | `null,` `string` | デバイスのオペレーティング・システムのバージョン
`device_model` | `null,` `string` | デバイスのモデル
`resolution` | `null,` `string` | デバイスの解像度
`carrier` | `null,` `string` | デバイスの通信事業者
`browser` | `null,` `string` | デバイスのブラウザ
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_NEWSFEEDCARD_IMPRESSION_SHARED {#USERS_MESSAGES_NEWSFEEDCARD_IMPRESSION_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザーID
`app_group_api_id` | `null,` `string` | このユーザーが所属するワークスペースのAPI ID
`time` | `int` | イベントが発生したUnixタイムスタンプ
`app_api_id` | `null,` `string` | このイベントが発生したアプリのAPI ID
`card_api_id` | `null,` `string` | カードのAPI ID
`gender` | `null,` `string` | [PII] ユーザーの性別
`country` | `null,` `string` | [PII] ユーザーの国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
`device_id` | `null,` `string` | イベントが発生したデバイスの ID
`sdk_version` | `null,` `string` | イベント中に使用されたBraze SDKのバージョン
`platform` | `null,` `string` | デバイスのプラットフォーム
`os_version` | `null,` `string` | デバイスのオペレーティング・システムのバージョン
`device_model` | `null,` `string` | デバイスのモデル
`resolution` | `null,` `string` | デバイスの解像度
`carrier` | `null,` `string` | デバイスの通信事業者
`browser` | `null,` `string` | デバイスのブラウザ
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_PUSHNOTIFICATION_ABORT_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_ABORT_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザーID
`device_id` | `null,` `string` | 配信を試みた `device_id`
`app_group_api_id` | `null,` `string` | このユーザーが所属するワークスペースのAPI ID
`time` | `int` | イベントが発生したUnixタイムスタンプ
`app_api_id` | `null,` `string` | このイベントが発生したアプリのAPI ID
`dispatch_id` | `null,` `string` | このメッセージが属するディスパッチの ID
`send_id` | `null,` `string` | このメッセージが属するメッセージ送信ID
`campaign_id` | `null,` `string` | このイベントが属するキャンペーンの内部用Braze ID
`campaign_api_id` | `null,` `string` | このイベントが属するキャンペーンのAPI ID
`message_variation_api_id` | `null,` `string` | このユーザーが受信したメッセージバリエーションのAPI ID
`canvas_id` | `null,` `string` | このイベントが属するキャンバスの内部使用Braze ID
`canvas_api_id` | `null,` `string` | このイベントが属するキャンバスのAPI ID
`canvas_variation_api_id` | `null,` `string` | このイベントが属するキャンバスのバリエーションのAPI ID
`canvas_step_api_id` | `null,` `string` | このイベントが属するキャンバスステップのAPI ID
`canvas_step_message_variation_api_id` | `null,` `string` | このユーザーが受け取ったキャンバスステップメッセージのバリエーションのAPI ID
`gender` | `null,` `string` | [PII] ユーザーの性別
`country` | `null,` `string` | [PII] ユーザーの国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
`platform` | `string` | デバイスのプラットフォーム
`abort_type` | `null,` `string` | 中止のタイプ。`liquid_abort_message` または `rate_limit` のいずれか
`abort_log` | `null,` `string` | [PII] 中止の詳細を記述するログメッセージ (最大 128 文字)
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_PUSHNOTIFICATION_BOUNCE_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_BOUNCE_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザーID
`push_token` | `null,` `string` | バウンスしたプッシュ・トークン
`device_id` | `null,` `string` | 配信を試みたがバウンスした `device_id`
`app_group_api_id` | `null,` `string` | このユーザーが所属するワークスペースのAPI ID
`time` | `int` | イベントが発生したUnixタイムスタンプ
`app_api_id` | `null,` `string` | このイベントが発生したアプリのAPI ID
`dispatch_id` | `null,` `string` | このメッセージが属するディスパッチの ID
`send_id` | `null,` `string` | このメッセージが属するメッセージ送信ID
`campaign_id` | `null,` `string` | このイベントが属するキャンペーンの内部用Braze ID
`campaign_api_id` | `null,` `string` | このイベントが属するキャンペーンのAPI ID
`message_variation_api_id` | `null,` `string` | このユーザーが受信したメッセージバリエーションのAPI ID
`canvas_id` | `null,` `string` | このイベントが属するキャンバスの内部使用Braze ID
`canvas_api_id` | `null,` `string` | このイベントが属するキャンバスのAPI ID
`canvas_variation_api_id` | `null,` `string` | このイベントが属するキャンバスのバリエーションのAPI ID
`canvas_step_api_id` | `null,` `string` | このイベントが属するキャンバスステップのAPI ID
`canvas_step_message_variation_api_id` | `null,` `string` | このユーザーが受け取ったキャンバスステップメッセージのバリエーションのAPI ID
`gender` | `null,` `string` | [PII] ユーザーの性別
`country` | `null,` `string` | [PII] ユーザーの国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
`platform` | `null,` `string` | デバイスのプラットフォーム
`ad_id` | `null,` `string` | [PII] 配信を試みたデバイスの広告 ID
`ad_id_type` | `null,` `string` | 広告 ID のタイプ
`ad_tracking_enabled` | `null, boolean` | 広告のトラッキングを有効にしているかどうか
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_PUSHNOTIFICATION_INFLUENCEDOPEN_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_INFLUENCEDOPEN_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザーID
`app_group_api_id` | `null,` `string` | このユーザーが所属するワークスペースのAPI ID
`time` | `int` | イベントが発生したUnixタイムスタンプ
`app_api_id` | `null,` `string` | このイベントが発生したアプリのAPI ID
`dispatch_id` | `null,` `string` | このメッセージが属するディスパッチの ID
`send_id` | `null,` `string` | このメッセージが属するメッセージ送信ID
`campaign_id` | `null,` `string` | このイベントが属するキャンペーンの内部用Braze ID
`campaign_api_id` | `null,` `string` | このイベントが属するキャンペーンのAPI ID
`message_variation_api_id` | `null,` `string` | このユーザーが受信したメッセージバリエーションのAPI ID
`canvas_id` | `null,` `string` | このイベントが属するキャンバスの内部使用Braze ID
`canvas_api_id` | `null,` `string` | このイベントが属するキャンバスのAPI ID
`canvas_variation_api_id` | `null,` `string` | このイベントが属するキャンバスのバリエーションのAPI ID
`canvas_step_api_id` | `null,` `string` | このイベントが属するキャンバスステップのAPI ID
`canvas_step_message_variation_api_id` | `null,` `string` | このユーザーが受け取ったキャンバスステップメッセージのバリエーションのAPI ID
`gender` | `null,` `string` | [PII] ユーザーの性別
`country` | `null,` `string` | [PII] ユーザーの国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
`device_id` | `null,` `string` | イベントが発生したデバイスの ID
`sdk_version` | `null,` `string` | イベント中に使用されたBraze SDKのバージョン
`platform` | `null,` `string` | デバイスのプラットフォーム
`os_version` | `null,` `string` | デバイスのオペレーティング・システムのバージョン
`device_model` | `null,` `string` | デバイスのモデル
`resolution` | `null,` `string` | デバイスの解像度
`carrier` | `null,` `string` | デバイスの通信事業者
`browser` | `null,` `string` | デバイスのブラウザ
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_PUSHNOTIFICATION_IOSFOREGROUND_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_IOSFOREGROUND_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザーID
`app_group_api_id` | `null,` `string` | このユーザーが所属するワークスペースのAPI ID
`time` | `int` | イベントが発生したUnixタイムスタンプ
`app_api_id` | `null,` `string` | このイベントが発生したアプリのAPI ID
`dispatch_id` | `null,` `string` | このメッセージが属するディスパッチの ID
`send_id` | `null,` `string` | このメッセージが属するメッセージ送信ID
`campaign_id` | `null,` `string` | このイベントが属するキャンペーンの内部用Braze ID
`campaign_api_id` | `null,` `string` | このイベントが属するキャンペーンのAPI ID
`message_variation_api_id` | `null,` `string` | このユーザーが受信したメッセージバリエーションのAPI ID
`canvas_id` | `null,` `string` | このイベントが属するキャンバスの内部使用Braze ID
`canvas_api_id` | `null,` `string` | このイベントが属するキャンバスのAPI ID
`canvas_variation_api_id` | `null,` `string` | このイベントが属するキャンバスのバリエーションのAPI ID
`canvas_step_api_id` | `null,` `string` | このイベントが属するキャンバスステップのAPI ID
`canvas_step_message_variation_api_id` | `null,` `string` | このユーザーが受け取ったキャンバスステップメッセージのバリエーションのAPI ID
`gender` | `null,` `string` | [PII] ユーザーの性別
`country` | `null,` `string` | [PII] ユーザーの国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
`device_id` | `null,` `string` | イベントが発生したデバイスの ID
`sdk_version` | `null,` `string` | イベント中に使用されたBraze SDKのバージョン
`platform` | `null,` `string` | デバイスのプラットフォーム
`os_version` | `null,` `string` | デバイスのオペレーティング・システムのバージョン
`device_model` | `null,` `string` | デバイスのモデル
`resolution` | `null,` `string` | デバイスの解像度
`carrier` | `null,` `string` | デバイスの通信事業者
`browser` | `null,` `string` | デバイスのブラウザ
`ad_id` | `null,` `string` | [PII] 配信を試みたデバイスの広告 ID
`ad_id_type` | `null,` `string` | 広告 ID のタイプ
`ad_tracking_enabled` | `null, boolean` | 広告のトラッキングを有効にしているかどうか
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_PUSHNOTIFICATION_OPEN_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_OPEN_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザーID
`app_group_api_id` | `null,` `string` | このユーザーが所属するワークスペースのAPI ID
`time` | `int` | イベントが発生したUnixタイムスタンプ
`app_api_id` | `null,` `string` | このイベントが発生したアプリのAPI ID
`dispatch_id` | `null,` `string` | このメッセージが属するディスパッチの ID
`send_id` | `null,` `string` | このメッセージが属するメッセージ送信ID
`campaign_id` | `null,` `string` | このイベントが属するキャンペーンの内部用Braze ID
`campaign_api_id` | `null,` `string` | このイベントが属するキャンペーンのAPI ID
`message_variation_api_id` | `null,` `string` | このユーザーが受信したメッセージバリエーションのAPI ID
`canvas_id` | `null,` `string` | このイベントが属するキャンバスの内部使用Braze ID
`canvas_api_id` | `null,` `string` | このイベントが属するキャンバスのAPI ID
`canvas_variation_api_id` | `null,` `string` | このイベントが属するキャンバスのバリエーションのAPI ID
`canvas_step_api_id` | `null,` `string` | このイベントが属するキャンバスステップのAPI ID
`canvas_step_message_variation_api_id` | `null,` `string` | このユーザーが受け取ったキャンバスステップメッセージのバリエーションのAPI ID
`gender` | `null,` `string` | [PII] ユーザーの性別
`country` | `null,` `string` | [PII] ユーザーの国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
`device_id` | `null,` `string` | イベントが発生したデバイスの ID
`sdk_version` | `null,` `string` | イベント中に使用されたBraze SDKのバージョン
`platform` | `null,` `string` | デバイスのプラットフォーム
`os_version` | `null,` `string` | デバイスのオペレーティング・システムのバージョン
`device_model` | `null,` `string` | デバイスのモデル
`resolution` | `null,` `string` | デバイスの解像度
`carrier` | `null,` `string` | デバイスの通信事業者
`browser` | `null,` `string` | デバイスのブラウザ
`button_string` | `null,` `string` | クリックされたプッシュ通知ボタンの識別子 (button_string)。ボタンのクリックでない場合は null
`button_action_type` | `null,` `string` | プッシュ通知ボタンのアクションタイプ。URI, DEEP_LINK, NONE, CLOSE] のいずれか。 ボタンクリックによるものでない場合はNULLとなる。
`slide_id` | `null,` `string` | ユーザがクリックしたプッシュカルーセルスライドのスライド識別子
`slide_action_type` | `null,` `string` | プッシュカルーセルスライドのアクションタイプ
`ad_id` | `null,` `string` | [PII] 配信を試みたデバイスの広告 ID
`ad_id_type` | `null,` `string` | 広告 ID のタイプ
`ad_tracking_enabled` | `null, boolean` | 広告のトラッキングを有効にしているかどうか
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_PUSHNOTIFICATION_SEND_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_SEND_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザーID
`push_token` | `null,` `string` | 配信を試みたプッシュトークン
`device_id` | `null,` `string` | 配信を試みた `device_id`
`app_group_api_id` | `null,` `string` | このユーザーが所属するワークスペースのAPI ID
`time` | `int` | イベントが発生したUnixタイムスタンプ
`app_api_id` | `null,` `string` | このイベントが発生したアプリのAPI ID
`dispatch_id` | `null,` `string` | このメッセージが属するディスパッチの ID
`send_id` | `null,` `string` | このメッセージが属するメッセージ送信ID
`campaign_id` | `null,` `string` | このイベントが属するキャンペーンの内部用Braze ID
`campaign_api_id` | `null,` `string` | このイベントが属するキャンペーンのAPI ID
`message_variation_api_id` | `null,` `string` | このユーザーが受信したメッセージバリエーションのAPI ID
`canvas_id` | `null,` `string` | このイベントが属するキャンバスの内部使用Braze ID
`canvas_api_id` | `null,` `string` | このイベントが属するキャンバスのAPI ID
`canvas_variation_api_id` | `null,` `string` | このイベントが属するキャンバスのバリエーションのAPI ID
`canvas_step_api_id` | `null,` `string` | このイベントが属するキャンバスステップのAPI ID
`canvas_step_message_variation_api_id` | `null,` `string` | このユーザーが受け取ったキャンバスステップメッセージのバリエーションのAPI ID
`gender` | `null,` `string` | [PII] ユーザーの性別
`country` | `null,` `string` | [PII] ユーザーの国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
`platform` | `string` | デバイスのプラットフォーム
`ad_id` | `null,` `string` | [PII] 配信を試みたデバイスの広告 ID
`ad_id_type` | `null,` `string` | 広告 ID のタイプ
`ad_tracking_enabled` | `null, boolean` | 広告のトラッキングを有効にしているかどうか
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_ABORT_SHARED {#USERS_MESSAGES_SMS_ABORT_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザーID
`app_group_api_id` | `null,` `string` | このユーザーが所属するワークスペースのAPI ID
`time` | `int` | イベントが発生したUnixタイムスタンプ
`campaign_id` | `null,` `string` | このイベントが属するキャンペーンの内部用Braze ID
`campaign_api_id` | `null,` `string` | このイベントが属するキャンペーンのAPI ID
`message_variation_api_id` | `null,` `string` | このユーザーが受信したメッセージバリエーションのAPI ID
`canvas_id` | `null,` `string` | このイベントが属するキャンバスの内部使用Braze ID
`canvas_api_id` | `null,` `string` | このイベントが属するキャンバスのAPI ID
`canvas_variation_api_id` | `null,` `string` | このイベントが属するキャンバスのバリエーションのAPI ID
`canvas_step_api_id` | `null,` `string` | このイベントが属するキャンバスステップのAPI ID
`canvas_step_message_variation_api_id` | `null,` `string` | このユーザーが受け取ったキャンバスステップメッセージのバリエーションのAPI ID
`subscription_group_api_id` | `null,` `string` | サブスクリプショングループの外部 ID
`abort_type` | `null,` `string` | 中止のタイプ。`liquid_abort_message` または `rate_limit` のいずれか
`abort_log` | `null,` `string` | [PII] 中止の詳細を記述するログメッセージ (最大 128 文字)
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_CARRIERSEND_SHARED {#USERS_MESSAGES_SMS_CARRIERSEND_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザーID
`device_id` | `null,` `string` | ユーザーが匿名の場合、このユーザーに関連付けられる `device_id`
`app_group_api_id` | `null,` `string` | このユーザーが所属するワークスペースのAPI ID
`time` | `int` | イベントが発生したUnixタイムスタンプ
`dispatch_id` | `null,` `string` | このメッセージが属するディスパッチの ID
`send_id` | `null,` `string` | このメッセージが属するメッセージ送信ID
`campaign_id` | `null,` `string` | このイベントが属するキャンペーンの内部用Braze ID
`campaign_api_id` | `null,` `string` | このイベントが属するキャンペーンのAPI ID
`message_variation_api_id` | `null,` `string` | このユーザーが受信したメッセージバリエーションのAPI ID
`canvas_id` | `null,` `string` | このイベントが属するキャンバスの内部使用Braze ID
`canvas_api_id` | `null,` `string` | このイベントが属するキャンバスのAPI ID
`canvas_variation_api_id` | `null,` `string` | このイベントが属するキャンバスのバリエーションのAPI ID
`canvas_step_api_id` | `null,` `string` | このイベントが属するキャンバスステップのAPI ID
`canvas_step_message_variation_api_id` | `null,` `string` | このユーザーが受け取ったキャンバスステップメッセージのバリエーションのAPI ID
`gender` | `null,` `string` | [PII] ユーザーの性別
`country` | `null,` `string` | [PII] ユーザーの国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
`to_phone_number` | `null,` `string` | [PII] 受信者の電話番号
`from_phone_number` | `null,` `string` | SMSメッセージの送信元電話番号
`subscription_group_api_id` | `null,` `string` | サブスクリプショングループの外部 ID
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_DELIVERY_SHARED {#USERS_MESSAGES_SMS_DELIVERY_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザーID
`device_id` | `null,` `string` | ユーザーが匿名の場合、このユーザーに関連付けられる `device_id`
`app_group_api_id` | `null,` `string` | このユーザーが所属するワークスペースのAPI ID
`time` | `int` | イベントが発生したUnixタイムスタンプ
`dispatch_id` | `null,` `string` | このメッセージが属するディスパッチの ID
`send_id` | `null,` `string` | このメッセージが属するメッセージ送信ID
`campaign_id` | `null,` `string` | このイベントが属するキャンペーンの内部用Braze ID
`campaign_api_id` | `null,` `string` | このイベントが属するキャンペーンのAPI ID
`message_variation_api_id` | `null,` `string` | このユーザーが受信したメッセージバリエーションのAPI ID
`canvas_id` | `null,` `string` | このイベントが属するキャンバスの内部使用Braze ID
`canvas_api_id` | `null,` `string` | このイベントが属するキャンバスのAPI ID
`canvas_variation_api_id` | `null,` `string` | このイベントが属するキャンバスのバリエーションのAPI ID
`canvas_step_api_id` | `null,` `string` | このイベントが属するキャンバスステップのAPI ID
`canvas_step_message_variation_api_id` | `null,` `string` | このユーザーが受け取ったキャンバスステップメッセージのバリエーションのAPI ID
`gender` | `null,` `string` | [PII] ユーザーの性別
`country` | `null,` `string` | [PII] ユーザーの国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
`to_phone_number` | `null,` `string` | [PII] 受信者の電話番号
`from_phone_number` | `null,` `string` | SMSメッセージが送信された電話番号
`subscription_group_api_id` | `null,` `string` | サブスクリプショングループの外部 ID
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED {#USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザーID
`device_id` | `null,` `string` | ユーザーが匿名の場合、このユーザーに関連付けられる `device_id`
`app_group_api_id` | `null,` `string` | このユーザーが所属するワークスペースのAPI ID
`time` | `int` | イベントが発生したUnixタイムスタンプ
`dispatch_id` | `null,` `string` | このメッセージが属するディスパッチの ID
`send_id` | `null,` `string` | このメッセージが属するメッセージ送信ID
`campaign_id` | `null,` `string` | このイベントが属するキャンペーンの内部用Braze ID
`campaign_api_id` | `null,` `string` | このイベントが属するキャンペーンのAPI ID
`message_variation_api_id` | `null,` `string` | このユーザーが受信したメッセージバリエーションのAPI ID
`canvas_id` | `null,` `string` | このイベントが属するキャンバスの内部使用Braze ID
`canvas_api_id` | `null,` `string` | このイベントが属するキャンバスのAPI ID
`canvas_variation_api_id` | `null,` `string` | このイベントが属するキャンバスのバリエーションのAPI ID
`canvas_step_api_id` | `null,` `string` | このイベントが属するキャンバスステップのAPI ID
`canvas_step_message_variation_api_id` | `null,` `string` | このユーザーが受け取ったキャンバスステップメッセージのバリエーションのAPI ID
`gender` | `null,` `string` | [PII] ユーザーの性別
`country` | `null,` `string` | [PII] ユーザーの国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
`to_phone_number` | `null,` `string` | [PII] 受信者の電話番号
`subscription_group_api_id` | `null,` `string` | サブスクリプショングループの外部 ID
`error` | `null,` `string` | エラー名
`provider_error_code` | `null,` `string` | SMSサービスプロバイダからのエラーコード
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED {#USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `null,` `string` | このイベントを実行したユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザーID
`app_group_api_id` | `null,` `string` | 受信電話番号に関連するワークスペースのAPI ID
`time` | `int` | イベントが発生したUnixタイムスタンプ
`user_phone_number` | `string` | [PII] メッセージを受信したユーザーの電話番号
`subscription_group_id` | `null,` `string` | このSMSメッセージの対象となる購読グループのID
`subscription_group_api_id` | `null,` `string` | このSMSメッセージの対象となる購読グループのAPI ID
`inbound_phone_number` | `string` | メッセージが送信された受信番号
`action` | `string` | このメッセージに対して実行されたアクション。`Subscribed`、`Unsubscribed`、`None` などがあります。
`message_body` | `string` | ユーザーからの応答
`media_urls` | `null, {"type"=>"array", "items"=>["null", "string"]}` | ユーザーからのメディアURL
`campaign_id` | `null,` `string` | このイベントが属するキャンペーンの内部用Braze ID
`campaign_api_id` | `null,` `string` | このイベントが属するキャンペーンのAPI ID
`message_variation_api_id` | `null,` `string` | このイベントが属するメッセージバリエーションのAPI ID
`canvas_id` | `null,` `string` | このイベントが属するキャンバスの内部使用Braze ID
`canvas_api_id` | `null,` `string` | このイベントが属するキャンバスのAPI ID
`canvas_variation_api_id` | `null,` `string` | このイベントが属するキャンバスのバリエーションのAPI ID
`canvas_step_api_id` | `null,` `string` | このイベントが属するキャンバスステップのAPI ID
`canvas_step_message_variation_api_id` | `null,` `string` | このイベントが属するキャンバスステップメッセージバリエーションのAPI ID
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_REJECTION_SHARED {#USERS_MESSAGES_SMS_REJECTION_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザーID
`device_id` | `null,` `string` | ユーザーが匿名の場合、このユーザーに関連付けられる `device_id`
`app_group_api_id` | `null,` `string` | このユーザーが所属するワークスペースのAPI ID
`time` | `int` | イベントが発生したUnixタイムスタンプ
`dispatch_id` | `null,` `string` | このメッセージが属するディスパッチの ID
`send_id` | `null,` `string` | このメッセージが属するメッセージ送信ID
`campaign_id` | `null,` `string` | このイベントが属するキャンペーンの内部用Braze ID
`campaign_api_id` | `null,` `string` | このイベントが属するキャンペーンのAPI ID
`message_variation_api_id` | `null,` `string` | このユーザーが受信したメッセージバリエーションのAPI ID
`canvas_id` | `null,` `string` | このイベントが属するキャンバスの内部使用Braze ID
`canvas_api_id` | `null,` `string` | このイベントが属するキャンバスのAPI ID
`canvas_variation_api_id` | `null,` `string` | このイベントが属するキャンバスのバリエーションのAPI ID
`canvas_step_api_id` | `null,` `string` | このイベントが属するキャンバスステップのAPI ID
`canvas_step_message_variation_api_id` | `null,` `string` | このユーザーが受け取ったキャンバスステップメッセージのバリエーションのAPI ID
`gender` | `null,` `string` | [PII] ユーザーの性別
`country` | `null,` `string` | [PII] ユーザーの国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
`to_phone_number` | `null,` `string` | [PII] 受信者の電話番号
`from_phone_number` | `null,` `string` | SMSメッセージの送信元電話番号
`subscription_group_api_id` | `null,` `string` | サブスクリプショングループの外部 ID
`error` | `null,` `string` | エラー名
`provider_error_code` | `null,` `string` | SMSサービスプロバイダからのエラーコード
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_SEND_SHARED {#USERS_MESSAGES_SMS_SEND_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザーID
`device_id` | `null,` `string` | ユーザーが匿名の場合、このユーザーに関連付けられる `device_id`
`app_group_api_id` | `null,` `string` | このユーザーが所属するワークスペースのAPI ID
`time` | `int` | イベントが発生したUnixタイムスタンプ
`dispatch_id` | `null,` `string` | このメッセージが属するディスパッチの ID
`send_id` | `null,` `string` | このメッセージが属するメッセージ送信ID
`campaign_id` | `null,` `string` | このイベントが属するキャンペーンの内部用Braze ID
`campaign_api_id` | `null,` `string` | このイベントが属するキャンペーンのAPI ID
`message_variation_api_id` | `null,` `string` | このユーザーが受信したメッセージバリエーションのAPI ID
`canvas_id` | `null,` `string` | このイベントが属するキャンバスの内部使用Braze ID
`canvas_api_id` | `null,` `string` | このイベントが属するキャンバスのAPI ID
`canvas_variation_api_id` | `null,` `string` | このイベントが属するキャンバスのバリエーションのAPI ID
`canvas_step_api_id` | `null,` `string` | このイベントが属するキャンバスステップのAPI ID
`canvas_step_message_variation_api_id` | `null,` `string` | このユーザーが受け取ったキャンバスステップメッセージのバリエーションのAPI ID
`gender` | `null,` `string` | [PII] ユーザーの性別
`country` | `null,` `string` | [PII] ユーザーの国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
`to_phone_number` | `null,` `string` | [PII] 受信者の電話番号
`subscription_group_api_id` | `null,` `string` | サブスクリプショングループの外部 ID
`category` | `null,` `string` | キーワードカテゴリ名。自動返信メッセージにのみ入力されます。「オプトイン」、「オプトアウト」、「ヘルプ」、またはカスタム値
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED {#USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `null,` `string` | short_urlが対象としたユーザーのBraze ID。short_urlがユーザーのクリックトラッキングを使用していない場合はNULLとなる。
`external_user_id` | `null,` `string` | [PII] Short_url がターゲットとしたユーザーの外部 ID が存在する場合はその ID、Short_url がユーザーのクリックトラッキングを使用していない場合は null となる。
`app_group_api_id` | `null,` `string` | short_urlの生成に使用したワークスペースのAPI ID
`time` | `int` | short_urlがクリックされたUnixタイムスタンプ
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`campaign_id` | `null,` `string` | short_url が生成されたキャンペーンの Braze ID。キャンペーンからのものでない場合は null
`campaign_api_id` | `null,` `string` | short_urlが生成されたキャンペーンのAPI ID。
`message_variation_api_id` | `null,` `string` | メッセージバリエーションshort_urlが生成されたAPI ID、キャンペーンからのものでない場合はNULL
`canvas_id` | `null,` `string` | short_url が生成されたキャンバスの Braze ID。キャンバスからのものでない場合は null
`canvas_api_id` | `null,` `string` | short_url が生成されたキャンバスの API ID。キャンバスからのものでない場合は null
`canvas_variation_api_id` | `null,` `string` | short_url が生成されたキャンバスバリエーションの API ID。キャンバスからのものでない場合は null
`canvas_step_api_id` | `null,` `string` | short_url が生成されたキャンバスステップの API ID。キャンバスからのものでない場合は null
`canvas_step_message_variation_api_id` | `null,` `string` | short_url が生成されたキャンバスステップのメッセージバリエーションの API ID。キャンバスからのものでない場合は null
`url` | `string` | short_urlによってリダイレクトされるメッセージに含まれる元のURL
`short_url` | `string` | クリックされた短縮URL
`user_agent` | `null,` `string` | ユーザーエージェントがshort_urlを要求する
`user_phone_number` | `string` | [PII] ユーザーの電話番号
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WEBHOOK_ABORT_SHARED {#USERS_MESSAGES_WEBHOOK_ABORT_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザーID
`device_id` | `null,` `string` | ユーザーが匿名の場合、このユーザーに関連付けられる `device_id`
`app_group_api_id` | `null,` `string` | このユーザーが所属するワークスペースのAPI ID
`time` | `int` | イベントが発生したUnixタイムスタンプ
`dispatch_id` | `null,` `string` | このメッセージが属するディスパッチの ID
`send_id` | `null,` `string` | このメッセージが属するメッセージ送信ID
`campaign_id` | `null,` `string` | このイベントが属するキャンペーンの内部用Braze ID
`campaign_api_id` | `null,` `string` | このイベントが属するキャンペーンのAPI ID
`message_variation_api_id` | `null,` `string` | このユーザーが受信したメッセージバリエーションのAPI ID
`canvas_id` | `null,` `string` | このイベントが属するキャンバスの内部使用Braze ID
`canvas_api_id` | `null,` `string` | このイベントが属するキャンバスのAPI ID
`canvas_variation_api_id` | `null,` `string` | このイベントが属するキャンバスのバリエーションのAPI ID
`canvas_step_api_id` | `null,` `string` | このイベントが属するキャンバスステップのAPI ID
`canvas_step_message_variation_api_id` | `null,` `string` | このユーザーが受け取ったキャンバスステップメッセージのバリエーションのAPI ID
`gender` | `null,` `string` | [PII] ユーザーの性別
`country` | `null,` `string` | [PII] ユーザーの国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
`abort_type` | `null,` `string` | 中止のタイプ。`liquid_abort_message` または `rate_limit` のいずれか
`abort_log` | `null,` `string` | [PII] 中止の詳細を記述するログメッセージ (最大 128 文字)
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WEBHOOK_SEND_SHARED {#USERS_MESSAGES_WEBHOOK_SEND_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザーID
`device_id` | `null,` `string` | ユーザーが匿名の場合、このユーザーに関連付けられる `device_id`
`app_group_api_id` | `null,` `string` | このユーザーが所属するワークスペースのAPI ID
`time` | `int` | イベントが発生したUnixタイムスタンプ
`dispatch_id` | `null,` `string` | このメッセージが属するディスパッチの ID
`send_id` | `null,` `string` | このメッセージが属するメッセージ送信ID
`campaign_id` | `null,` `string` | このイベントが属するキャンペーンの内部用Braze ID
`campaign_api_id` | `null,` `string` | このイベントが属するキャンペーンのAPI ID
`message_variation_api_id` | `null,` `string` | このユーザーが受信したメッセージバリエーションのAPI ID
`canvas_id` | `null,` `string` | このイベントが属するキャンバスの内部使用Braze ID
`canvas_api_id` | `null,` `string` | このイベントが属するキャンバスのAPI ID
`canvas_variation_api_id` | `null,` `string` | このイベントが属するキャンバスのバリエーションのAPI ID
`canvas_step_api_id` | `null,` `string` | このイベントが属するキャンバスステップのAPI ID
`canvas_step_message_variation_api_id` | `null,` `string` | このユーザーが受け取ったキャンバスステップメッセージのバリエーションのAPI ID
`gender` | `null,` `string` | [PII] ユーザーの性別
`country` | `null,` `string` | [PII] ユーザーの国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WHATSAPP_ABORT_SHARED {#USERS_MESSAGES_WHATSAPP_ABORT_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`time` | `int` | イベントが発生したUnixタイムスタンプ
`to_phone_number` | 	`null,` `string` | [PII] 受信者の電話番号
`user_id` | `string` | このイベントを実行したユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザーID
`device_id` | `null,` `string` | ユーザーが匿名の場合、このユーザーに関連付けられる `device_id`
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`app_group_id` | `null,` `string` | このユーザーが所属するワークスペースのID
`app_group_api_id` | `null,` `string` | このユーザーが所属するワークスペースのAPI ID
`subscription_group_api_id` | `string` | サブスクリプショングループAPI ID
`campaign_id` | `null,` `string` | このイベントが属するキャンペーンの内部用Braze ID
`campaign_api_id` | `null,` `string` | このイベントが属するキャンペーンのAPI ID
`message_variation_api_id` | `null,` `string` | このユーザーが受信したメッセージバリエーションのAPI ID
`canvas_id` | `null,` `string` | このイベントが属するキャンバスの内部使用Braze ID
`canvas_api_id` | `null,` `string` | このイベントが属するキャンバスのAPI ID
`canvas_variation_api_id` | `null,` `string` | このイベントが属するキャンバスのバリエーションのAPI ID
`canvas_step_api_id` | `null,` `string` | このイベントが属するキャンバスステップのAPI ID
`canvas_step_message_variation_api_id` | `null,` `string` | このユーザーが受け取ったキャンバスステップメッセージのバリエーションのAPI ID
`dispatch_id` | `null,` `string` | このメッセージが属するディスパッチの ID
`abort_type` | `null,` `string` | 中止のタイプ。`liquid_abort_message` または `rate_limit` のいずれか
`abort_log` | `null,` `string` | [PII] 中止の詳細を記述するログメッセージ (最大 128 文字)
`sf_created_at` | `timestamp`, `null` | このイベントが Snowpipe に検出されたとき      
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WHATSAPP_DELIVERY_SHARED {#USERS_MESSAGES_WHATSAPP_DELIVERY_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`time` | `int` | イベントが発生したUnixタイムスタンプ
`to_phone_number` | `null,` `string` | [PII] 受信者の電話番号
`user_id` | `string` | このイベントを実行したユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザーID
`device_id` | `null,` `string` | ユーザーが匿名の場合、このユーザーに関連付けられる `device_id`
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`from_phone_number` | `null,` `string` | WhatsAppメッセージの送信元電話番号
`app_group_id` | `null,` `string` | このユーザーが所属するワークスペースのID
`app_group_api_id` | `null,` `string` | このユーザーが所属するワークスペースのAPI ID
`subscription_group_api_id` | `string` | サブスクリプショングループAPI ID
`campaign_id` | `null,` `string` | このイベントが属するキャンペーンの内部用Braze ID
`campaign_api_id` | `null,` `string` | このイベントが属するキャンペーンのAPI ID
`message_variation_api_id` | `null,` `string` | このユーザーが受信したメッセージバリエーションのAPI ID
`canvas_id` | `null,` `string` | このイベントが属するキャンバスの内部使用Braze ID
`canvas_api_id` | `null,` `string` | このイベントが属するキャンバスのAPI ID
`canvas_variation_api_id` | `null,` `string` | このイベントが属するキャンバスのバリエーションのAPI ID
`canvas_step_api_id` | `null,` `string` | このイベントが属するキャンバスステップのAPI ID
`canvas_step_message_variation_api_id` | `null,` `string` | このユーザーが受け取ったキャンバスステップメッセージのバリエーションのAPI ID
`dispatch_id` | `null,` `string` | このメッセージが属するディスパッチの ID
`sf_created_at` | `timestamp`, `null` | このイベントが Snowpipe に検出されたとき      
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WHATSAPP_FAILURE_SHARED {#USERS_MESSAGES_WHATSAPP_FAILURE_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`time` | `int` | イベントが発生したUnixタイムスタンプ
`to_phone_number` | `null,` `string` | [PII] 受信者の電話番号
`user_id` | `string` | このイベントを実行したユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザーID
`device_id` | `null,` `string` | ユーザーが匿名の場合、このユーザーに関連付けられる `device_id`
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`from_phone_number` | `null,` `string` | WhatsAppメッセージの送信元電話番号
`app_group_id` | `null,` `string` | このユーザーが所属するワークスペースのID
`app_group_api_id` | `null,` `string` | このユーザーが所属するワークスペースのAPI ID
`subscription_group_api_id` | `string` | サブスクリプショングループAPI ID
`campaign_id` | `null,` `string` | このイベントが属するキャンペーンの内部用Braze ID
`campaign_api_id` | `null,` `string` | このイベントが属するキャンペーンのAPI ID
`message_variation_api_id` | `null,` `string` | このユーザーが受信したメッセージバリエーションのAPI ID
`canvas_id` | `null,` `string` | このイベントが属するキャンバスの内部使用Braze ID
`canvas_api_id` | `null,` `string` | このイベントが属するキャンバスのAPI ID
`canvas_variation_api_id` | `null,` `string` | このイベントが属するキャンバスのバリエーションのAPI ID
`canvas_step_api_id` | `null,` `string` | このイベントが属するキャンバスステップのAPI ID
`canvas_step_message_variation_api_id` | `null,` `string` | このユーザーが受け取ったキャンバスステップメッセージのバリエーションのAPI ID
`dispatch_id` | `null,` `string` | このメッセージが属するディスパッチの ID
`provider_error_code` | `null,` `string` | WhatsAppのエラーコード
`provider_error_title` | `null, ` `string` | WhatsAppのエラータイトル
`sf_created_at` | `timestamp`, `null` | このイベントが Snowpipe に検出されたとき      
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WHATSAPP_INBOUNDRECEIVE_SHARED {#USERS_MESSAGES_WHATSAPP_INBOUNDRECEIVE_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`time` | `int` | イベントが発生したUnixタイムスタンプ
`user_phone_number` | `string` | [PII] メッセージを受信したユーザーの電話番号
`user_id` | `string` | このイベントを実行したユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザーID
`inbound_phone_number` | `string` | メッセージが送信された受信番号
`device_id` | `null,` `string` | ユーザーが匿名の場合、このユーザーに関連付けられる `device_id`
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`app_group_id` | `null,` `string` | このユーザーが所属するワークスペースのID
`app_group_api_id` | `null,` `string` | このユーザーが所属するワークスペースのAPI ID
`subscription_group_api_id` | `string` | サブスクリプショングループAPI ID
`campaign_id` | `null,` `string` | このイベントが属するキャンペーンの内部用Braze ID
`campaign_api_id` | `null,` `string` | このイベントが属するキャンペーンのAPI ID
`message_variation_api_id` | `null,` `string` | このユーザーが受信したメッセージバリエーションのAPI ID
`canvas_id` | `null,` `string` | このイベントが属するキャンバスの内部使用Braze ID
`canvas_api_id` | `null,` `string` | このイベントが属するキャンバスのAPI ID
`canvas_variation_api_id` | `null,` `string` | このイベントが属するキャンバスのバリエーションのAPI ID
`canvas_step_api_id` | `null,` `string` | このイベントが属するキャンバスステップのAPI ID
`canvas_step_message_variation_api_id` | `null,` `string` | このユーザーが受け取ったキャンバスステップメッセージのバリエーションのAPI ID
`message_body` | `string` | ユーザーからの応答
`quick_reply_text` | `string` | ユーザーが押したボタンのテキスト
`media_urls` | `null, {"type"=>"array", "items"=>["null", "string"]}` | ユーザーからのメディアURL
`action` | `string` | このメッセージに対して実行されたアクション。`Subscribed`、`Unsubscribed`、`None` などがあります。
`sf_created_at` | `timestamp`, `null` | このイベントが Snowpipe に検出されたとき      
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WHATSAPP_READ_SHARED {#USERS_MESSAGES_WHATSAPP_READ_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`time` | `int` | イベントが発生したUnixタイムスタンプ
`to_phone_number` | `null,` `string` | [PII] 受信者の電話番号
`user_id` | `string` | このイベントを実行したユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザーID
`device_id` | `null,` `string` | ユーザーが匿名の場合、このユーザーに関連付けられる `device_id`
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`from_phone_number` | `null,` `string` | WhatsAppメッセージの送信元電話番号
`app_group_id` | `null,` `string` | このユーザーが所属するワークスペースのID
`app_group_api_id` | `null,` `string` | このユーザーが所属するワークスペースのAPI ID
`subscription_group_api_id` | `string` | サブスクリプショングループAPI ID
`campaign_id` | `null,` `string` | このイベントが属するキャンペーンの内部用Braze ID
`campaign_api_id` | `null,` `string` | このイベントが属するキャンペーンのAPI ID
`message_variation_api_id` | `null,` `string` | このユーザーが受信したメッセージバリエーションのAPI ID
`canvas_id` | `null,` `string` | このイベントが属するキャンバスの内部使用Braze ID
`canvas_api_id` | `null,` `string` | このイベントが属するキャンバスのAPI ID
`canvas_variation_api_id` | `null,` `string` | このイベントが属するキャンバスのバリエーションのAPI ID
`canvas_step_api_id` | `null,` `string` | このイベントが属するキャンバスステップのAPI ID
`canvas_step_message_variation_api_id` | `null,` `string` | このユーザーが受け取ったキャンバスステップメッセージのバリエーションのAPI ID
`dispatch_id` | `null,` `string` | このメッセージが属するディスパッチの ID
`sf_created_at` | `timestamp`, `null` | このイベントが Snowpipe に検出されたとき      
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WHATSAPP_SEND_SHARED {#USERS_MESSAGES_WHATSAPP_SEND_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`time` | `int` | イベントが発生したUnixタイムスタンプ
`to_phone_number` | `null,` `string`	| [PII] 受信者の電話番号
`user_id` | `string` | このイベントを実行したユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザーID
`device_id` | `null,` `string` | ユーザーが匿名の場合、このユーザーに関連付けられる `device_id`
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`from_phone_number` | `null,` `string` | WhatsAppメッセージの送信元電話番号
`app_group_id` | `null,` `string` | このユーザーが所属するワークスペースのID
`app_group_api_id` | `null,` `string` | このユーザーが所属するワークスペースのAPI ID
`subscription_group_api_id` | `string` | サブスクリプショングループAPI ID
`campaign_id` | `null,` `string` | このイベントが属するキャンペーンの内部用Braze ID
`campaign_api_id` | `null,` `string` | このイベントが属するキャンペーンのAPI ID
`message_variation_api_id` | `null,` `string` | このユーザーが受信したメッセージバリエーションのAPI ID
`canvas_id` | `null,` `string` | このイベントが属するキャンバスの内部使用Braze ID
`canvas_api_id` | `null,` `string` | このイベントが属するキャンバスのAPI ID
`canvas_variation_api_id` | `null,` `string` | このイベントが属するキャンバスのバリエーションのAPI ID
`canvas_step_api_id` | `null,` `string` | このイベントが属するキャンバスステップのAPI ID
`canvas_step_message_variation_api_id` | `null,` `string` | このユーザーが受け取ったキャンバスステップメッセージのバリエーションのAPI ID
`dispatch_id` | `null,` `string` | このメッセージが属するディスパッチの ID
`message_extras` | `null,` `string` | [PII] リキッドレンダリング時にタグ付けされたキーと値のペアのJSON文字列
`sf_created_at` | `timestamp`, `null` | このイベントが Snowpipe に検出されたとき      
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## ユーザー

### USERS_RANDOMBUCKETNUMBERUPDATE_SHARED {#USERS_RANDOMBUCKETNUMBERUPDATE_SHARED}

| フィールド                       | タイプ                     | 説明                                        |
| --------------------------- | ------------------------ | -------------------------------------------------- |
| `id`                        | `string`, `null`    | このイベントのグローバルな一意の ID                  |
| `app_group_id`              | `string`, `null`    | このユーザーが所属するワークスペースのBraze ID      |
| `app_group_api_id`          | `string`, `null`    | このユーザーが所属するワークスペースのAPI ID       |
| `user_id`                   | `string`, `null`    | このイベントを実行したユーザーのBraze ID      |
| `external_user_id`          | `string`, `null`    | [PII] ユーザーの外部ユーザーID                 |
| `time`                      | `int`, `null`       | イベントが発生したUnixタイムスタンプ         |
| `random_bucket_number`      | `int`, `null`       | ユーザーに割り当てられている現在のランダムバケット番号  |
| `prev_random_bucket_number` | `int`, `null`       | ユーザーに割り当てられた以前のランダムなバケット番号 |
| `sf_created_at`             | `timestamp`, `null` | このイベントが Snowpipe に検出されたとき      |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_USERDELETEREQUEST_SHARED {#USERS_USERDELETEREQUEST_SHARED}

| フィールド              | タイプ                     | 説明                                                   |
| ------------------ | ------------------------ | ------------------------------------------------------------- |
| `id`               | `string`, `null`    | このイベントのグローバルな一意の ID                             |
| `user_id`          | `string`, `null`    | 削除されたユーザーのBraze ID                          |
| `app_group_id`     | `string`, `null`    | このユーザーが所属するワークスペースのBraze ID                 |
| `app_group_api_id` | `string`, `null`    | このユーザーが所属するワークスペースのAPI ID                  |
| `time`             | `int`, `null`       | ユーザー削除リクエストが処理されたUnixタイムスタンプ |
| `sf_created_at`    | `timestamp`, `null` | このイベントが Snowpipe に検出されたとき                 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_USERORPHAN_SHARED {#USERS_USERORPHAN_SHARED}

| フィールド              | タイプ                     | 説明                                                                   |
| ------------------ | ------------------------ | ----------------------------------------------------------------------------- |
| `id`               | `string`, `null`    | このイベントのグローバルな一意の ID                                             |
| `user_id`          | `string`, `null`    | 孤児となったユーザーのBraze ID                                         |
| `external_user_id` | `string`, `null`    | [PII] ユーザーの外部ユーザーID                                            |
| `device_id`        | `string`, `null`    | ユーザーが匿名の場合、このユーザーに紐づくデバイスのID          |
| `app_group_id`     | `string`, `null`    | このユーザーが所属するワークスペースのBraze ID                                 |
| `app_group_api_id` | `string`, `null`    | このユーザーが所属するワークスペースのAPI ID                                  |
| `app_api_id`       | `string`, `null`    | 孤児となったユーザーが所属していたアプリのAPI ID                               |
| `time`             | `int`, `null`       | ユーザーが孤児となったUnixタイムスタンプ                                 |
| `orphaned_by_id`   | `string`, `null`    | 孤児となったユーザーのプロファイルとマージされたユーザーのBraze ID |
| `sf_created_at`    | `timestamp`, `null` | このイベントが Snowpipe に検出されたとき                                 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }
