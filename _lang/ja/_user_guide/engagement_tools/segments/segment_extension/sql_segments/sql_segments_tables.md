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
[CATALOGS_ITEMS_SHARED](#CATALOGS_ITEMS_SHARED) | 削除されていないカタログ項目
[CHANGELOGS_GLOBALCONTROLGROUP_SHARED](#CHANGELOGS_GLOBALCONTROLGROUP_SHARED) | グローバルコントロールグループが変更されたとき
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
[USERS_BEHAVIORS_LIVEACTIVITY_PUSHTOSTARTTOKENCHANGE_SHARED](#USERS_BEHAVIORS_LIVEACTIVITY_PUSHTOSTARTTOKENCHANGE_SHARED) | ライブアクティビティのプッシュトークンが変更されたとき
[USERS_BEHAVIORS_LIVEACTIVITY_UPDATETOKENCHANGE_SHARED](#USERS_BEHAVIORS_LIVEACTIVITY_UPDATETOKENCHANGE_SHARED) | ライブアクティビティの更新トークンが変更されたとき
[USERS_BEHAVIORS_PUSHNOTIFICATION_TOKENSTATECHANGE_SHARED](#USERS_BEHAVIORS_PUSHNOTIFICATION_TOKENSTATECHANGE_SHARED) | プッシュ通知トークンの状態が変わった時
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
[USERS_MESSAGES_BANNER_ABORT_SHARED](#USERS_MESSAGES_BANNER_ABORT_SHARED) | 当初スケジュールされていたバナーメッセージが何らかの理由で中止された。
[USERS_MESSAGES_BANNER_CLICK_SHARED](#USERS_MESSAGES_BANNER_CLICK_SHARED) | ユーザーがバナーをクリックした時
[USERS_MESSAGES_BANNER_IMPRESSION_SHARED](#USERS_MESSAGES_BANNER_IMPRESSION_SHARED) | ユーザーがバナーを表示するとき
[USERS_MESSAGES_CONTENTCARD_ABORT_SHARED](#USERS_MESSAGES_CONTENTCARD_ABORT_SHARED) | 当初予定されていたコンテンツカードメッセージが、何らかの理由で中止された。
[USERS_MESSAGES_CONTENTCARD_CLICK_SHARED](#USERS_MESSAGES_CONTENTCARD_CLICK_SHARED) | ユーザーがコンテンツカードをクリックすると
[USERS_MESSAGES_CONTENTCARD_DISMISS_SHARED](#USERS_MESSAGES_CONTENTCARD_DISMISS_SHARED) | ユーザーがコンテンツカードを却下したとき
[USERS_MESSAGES_CONTENTCARD_IMPRESSION_SHARED](#USERS_MESSAGES_CONTENTCARD_IMPRESSION_SHARED) | ユーザーがコンテンツ・カードを見るとき
[USERS_MESSAGES_CONTENTCARD_SEND_SHARED](#USERS_MESSAGES_CONTENTCARD_SEND_SHARED) | コンテンツ・カードをユーザーに送る場合
[USERS_MESSAGES_EMAIL_ABORT_SHARED](#USERS_MESSAGES_EMAIL_ABORT_SHARED) | 当初予定されていたメールメッセージが、何らかの理由で中止された。
[USERS_MESSAGES_EMAIL_BOUNCE_SHARED](#USERS_MESSAGES_EMAIL_BOUNCE_SHARED) | メールサービスプロバイダーがハードバウンスを返した。ハードバウンスとは、永続的な配信の失敗です。
[USERS_MESSAGES_EMAIL_CLICK_SHARED](#USERS_MESSAGES_EMAIL_CLICK_SHARED) | ユーザーが電子メールのリンクをクリックした場合
[USERS_MESSAGES_EMAIL_DEFERRAL_SHARED](#USERS_MESSAGES_EMAIL_DEFERRAL_SHARED) | メールが保留される時
[USERS_MESSAGES_EMAIL_DELIVERY_SHARED](#USERS_MESSAGES_EMAIL_DELIVERY_SHARED) | 電子メールが配信された場合
[USERS_MESSAGES_EMAIL_MARKASSPAM_SHARED](#USERS_MESSAGES_EMAIL_MARKASSPAM_SHARED) | メールがスパムとしてマークされた場合
[USERS_MESSAGES_EMAIL_OPEN_SHARED](#USERS_MESSAGES_EMAIL_OPEN_SHARED) | ユーザーがメールを開く
[USERS_MESSAGES_EMAIL_SEND_SHARED](#USERS_MESSAGES_EMAIL_SEND_SHARED) | ユーザーに電子メールを送信する場合
[USERS_MESSAGES_EMAIL_SOFTBOUNCE_SHARED](#USERS_MESSAGES_EMAIL_SOFTBOUNCE_SHARED) | メールがソフトバウンスしたとき
[USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED](#USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED) | ユーザーがメールを配信停止したとき
[USERS_MESSAGES_FEATUREFLAG_IMPRESSION_SHARED](#USERS_MESSAGES_FEATUREFLAG_IMPRESSION_SHARED) | ユーザーがフィーチャーフラグを表示するとき
[USERS_MESSAGES_INAPPMESSAGE_ABORT_SHARED](#USERS_MESSAGES_INAPPMESSAGE_ABORT_SHARED) | 当初予定されていたアプリ内メッセージが何らかの理由で中止された。
[USERS_MESSAGES_INAPPMESSAGE_CLICK_SHARED](#USERS_MESSAGES_INAPPMESSAGE_CLICK_SHARED) | ユーザーがアプリ内メッセージをクリックした場合
[USERS_MESSAGES_INAPPMESSAGE_IMPRESSION_SHARED](#USERS_MESSAGES_INAPPMESSAGE_IMPRESSION_SHARED) | ユーザーがアプリ内メッセージを閲覧した場合
[USERS_MESSAGES_LINE_ABORT_SHARED](#USERS_MESSAGES_LINE_ABORT_SHARED) | スケジュールされたLINEメッセージが配信できない場合、LINEに送信する前に
[USERS_MESSAGES_LINE_CLICK_SHARED](#USERS_MESSAGES_LINE_CLICK_SHARED) | ユーザーがLINEメッセージ内のリンクをクリックした時
[USERS_MESSAGES_LINE_INBOUNDRECEIVE_SHARED](#USERS_MESSAGES_LINE_INBOUNDRECEIVE_SHARED) | ユーザーからLINEメッセージが届いた時
[USERS_MESSAGES_LINE_SEND_SHARED](#USERS_MESSAGES_LINE_SEND_SHARED) | LINEメッセージがLINEに送信されるとき
[USERS_MESSAGES_LIVEACTIVITY_OUTCOME_SHARED](#USERS_MESSAGES_LIVEACTIVITY_OUTCOME_SHARED) | ライブアクティビティに結果イベントがある場合
[USERS_MESSAGES_LIVEACTIVITY_SEND_SHARED](#USERS_MESSAGES_LIVEACTIVITY_SEND_SHARED) | ライブアクティビティのメッセージが送信されるとき
[USERS_MESSAGES_NEWSFEEDCARD_ABORT_SHARED](#USERS_MESSAGES_NEWSFEEDCARD_ABORT_SHARED) | 当初スケジュールされていたニュースフィードのカードメッセージが何らかの理由で中止された。
[USERS_MESSAGES_NEWSFEEDCARD_CLICK_SHARED](#USERS_MESSAGES_NEWSFEEDCARD_CLICK_SHARED) | ユーザーがニュースフィードカードをクリックすると
[USERS_MESSAGES_NEWSFEEDCARD_IMPRESSION_SHARED](#USERS_MESSAGES_NEWSFEEDCARD_IMPRESSION_SHARED) | ユーザーがニュースフィードカードを閲覧する
[USERS_MESSAGES_PUSHNOTIFICATION_ABORT_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_ABORT_SHARED) | 当初予定されていたプッシュ通知メッセージが、何らかの理由で中止された。
[USERS_MESSAGES_PUSHNOTIFICATION_BOUNCE_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_BOUNCE_SHARED) | プッシュ通知がバウンスしたとき
[USERS_MESSAGES_PUSHNOTIFICATION_INFLUENCEDOPEN_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_INFLUENCEDOPEN_SHARED) | ユーザーが通知を受け取った後、通知をクリックせずにアプリを開いた場合
[USERS_MESSAGES_PUSHNOTIFICATION_IOSFOREGROUND_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_IOSFOREGROUND_SHARED) | ユーザーがアプリを開封している状態でプッシュ通知を受信した時。<br><br>このイベントは[SWIFT SDK](https://github.com/braze-inc/braze-swift-sdk)ではサポートされておらず、[Objective-C SDK](https://github.com/Appboy/appboy-ios-sdk)では非推奨となっている。
[USERS_MESSAGES_PUSHNOTIFICATION_OPEN_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_OPEN_SHARED) | ユーザーがプッシュ通知を開いたとき、またはプッシュ通知ボタン（アプリを開かないCLOSEボタンを含む）をクリックしたとき。<br><br> プッシュボタンの操作には複数の結果があります。「No」、「Decline」、「Cancel」アクションは 「クリック数」、Accept アクションは「開封数」です。両者はこの表に示されているが、列**BUTTON_ACTION_TYPE**で区別できる。たとえば、「No」、「Decline」、「Cancel」でない`BUTTON_ACTION_TYPE`でグループ化するためにクエリを使用できます。
[USERS_MESSAGES_PUSHNOTIFICATION_SEND_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_SEND_SHARED) | ユーザーにプッシュ通知を送るとき
[USERS_MESSAGES_RCS_ABORT_SHARED](#USERS_MESSAGES_RCS_ABORT_SHARED) | Braze内でエラーが検出されたためRCS送信が中断され、メッセージが破棄された場合
[USERS_MESSAGES_RCS_CLICK_SHARED](#USERS_MESSAGES_RCS_CLICK_SHARED) | エンドユーザーがUI要素をタップまたはクリックしてRCSメッセージとやり取りするとき
[USERS_MESSAGES_RCS_DELIVERY_SHARED](#USERS_MESSAGES_RCS_DELIVERY_SHARED) | RCSメッセージがエンドユーザーのモバイル端末に正常に配信されたとき
[USERS_MESSAGES_RCS_INBOUNDRECEIVE_SHARED](#USERS_MESSAGES_RCS_INBOUNDRECEIVE_SHARED) | エンドユーザーから発信されたRCSメッセージをBrazeが受信したとき
[USERS_MESSAGES_RCS_READ_SHARED](#USERS_MESSAGES_RCS_READ_SHARED) | ユーザーが自身の端末でRCSメッセージを開封するとき
[USERS_MESSAGES_RCS_REJECTION_SHARED](#USERS_MESSAGES_RCS_REJECTION_SHARED) | 通信事業者の介入によりRCSメッセージの配信が失敗した場合
[USERS_MESSAGES_RCS_SEND_SHARED](#USERS_MESSAGES_RCS_SEND_SHARED) | RCSメッセージがBrazeのシステムからラストマイル配信パートナーに送信される時
[USERS_MESSAGES_SMS_ABORT_SHARED](#USERS_MESSAGES_SMS_ABORT_SHARED) | 当初予定されていたSMSメッセージが何らかの理由で中止された。
[USERS_MESSAGES_SMS_CARRIERSEND_SHARED](#USERS_MESSAGES_SMS_CARRIERSEND_SHARED) | SMSメッセージがキャリアに送信されるとき
[USERS_MESSAGES_SMS_DELIVERY_SHARED](#USERS_MESSAGES_SMS_DELIVERY_SHARED) | SMSメッセージが配信された場合
[USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED](#USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED) | BrazeがSMSサービスプロバイダにSMSメッセージを配信できない場合
[USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED](#USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED) | ユーザーからSMSメッセージを受信した場合
[USERS_MESSAGES_SMS_REJECTION_SHARED](#USERS_MESSAGES_SMS_REJECTION_SHARED) | SMSメッセージがユーザーに届かない場合
[USERS_MESSAGES_SMS_SEND_SHARED](#USERS_MESSAGES_SMS_SEND_SHARED) | SMSメッセージが送信された場合
[USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED](#USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED) | ユーザーがSMSメッセージに含まれるBrazeの短縮URLをクリックした場合
[USERS_MESSAGES_WEBHOOK_ABORT_SHARED](#USERS_MESSAGES_WEBHOOK_ABORT_SHARED) | 当初予定されていたウェブフック・メッセージが何らかの理由で中止された
[USERS_MESSAGES_WEBHOOK_FAILURE_SHARED](#USERS_MESSAGES_WEBHOOK_FAILURE_SHARED) | Webhookメッセージが配信されたが、エンドポイントからのエラー応答で失敗した場合
[USERS_MESSAGES_WEBHOOK_SEND_SHARED](#USERS_MESSAGES_WEBHOOK_SEND_SHARED) | ユーザーに対してウェブフックを送信する場合
[USERS_MESSAGES_WHATSAPP_ABORT_SHARED](#USERS_MESSAGES_WHATSAPP_ABORT_SHARED) | 予定されていたWhatsAppメッセージが何らかの理由で中断された
[USERS_MESSAGES_WHATSAPP_CLICK_SHARED](#USERS_MESSAGES_WHATSAPP_CLICK_SHARED) | ユーザーがWhatsAppメッセージ内のリンクやボタンをクリックした時
[USERS_MESSAGES_WHATSAPP_DELIVERY_SHARED](#USERS_MESSAGES_WHATSAPP_DELIVERY_SHARED) |WhatsAppメッセージが配信された場合
[USERS_MESSAGES_WHATSAPP_FAILURE_SHARED](#USERS_MESSAGES_WHATSAPP_FAILURE_SHARED) | WhatsAppメッセージがユーザーに届かない場合
[USERS_MESSAGES_WHATSAPP_INBOUNDRECEIVE_SHARED](#USERS_MESSAGES_WHATSAPP_INBOUNDRECEIVE_SHARED) | ユーザーからWhatsAppメッセージを受信した場合
[USERS_MESSAGES_WHATSAPP_READ_SHARED](#USERS_MESSAGES_WHATSAPP_READ_SHARED) | ユーザーがWhatsAppメッセージを開く
[USERS_MESSAGES_WHATSAPP_SEND_SHARED](#USERS_MESSAGES_WHATSAPP_SEND_SHARED) | あるユーザーに対してWhatsAppメッセージを送信する場合
[USERS_RANDOMBUCKETNUMBERUPDATE_SHARED](#USERS_RANDOMBUCKETNUMBERUPDATE_SHARED) | ユーザーのランダムバケット番号が変更された場合
[USERS_USERDELETEREQUEST_SHARED](#USERS_USERDELETEREQUEST_SHARED) | 顧客からのリクエストによりユーザーが削除された場合
[USERS_USERORPHAN_SHARED](#USERS_USERORPHAN_SHARED) | ユーザーが他のユーザーのプロファイルと統合され、元のプロファイルが孤児になった場合


## カタログ

### CATALOGS_ITEMS_SHARED {#CATALOGS_ITEMS_SHARED}

フィールド | タイプ | 説明
------|------|------------
`catalog_id` | `string` | カタログのBSON ID
`item_id` | `string` | カタログ項目のBSON ID
`app_group_id` | `null,` `string` | アプリグループのBSON ID
`app_group_api_id` | `null,` `string` | アプリグループのAPI ID
`field_name` | `null,` `string` | フィールド名
`field_value` | `null,` `string` | フィールドの値
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## 変更ログ

### CHANGELOGS_GLOBALCONTROLGROUP_SHARED {#CHANGELOGS_GLOBALCONTROLGROUP_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`app_group_id` | `null,` `string` | このユーザーが所属するアプリグループのBSON ID
`app_group_api_id` | `null,` `string` | このユーザーが所属するアプリグループのAPI ID
`time` | `int` | イベントが発生したUNIXタイムスタンプ
`random_bucket_number` | `null, int` | 新しいランダムなバケット番号
`global_control_group` | `null, boolean` | この変更により、バケット番号はグローバルコントロールグループに含まれる。
`previous_global_control_group` | `null, boolean` | この変更前はバケット番号がグローバルコントロールグループに含まれていたが、現在は含まれていない。
`sf_created_at` | `timestamp`, `null` | この出来事がスノーパイプによって拾われた時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


## 行動

### USERS_BEHAVIORS_CUSTOMEVENT_SHARED {#USERS_BEHAVIORS_CUSTOMEVENT_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | イベントを実行したユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
`app_group_api_id` | `null,` `string` | このユーザーが所属するワークスペースのAPI ID
`app_api_id` | `null,` `string` | このアクションが発生したアプリのAPI ID
`time` | `int` | ユーザーがイベントを実行したUnixタイムスタンプ
`gender` | `null,` `string` | [PII] ユーザーの性別
`country` | `null,` `string` | [PII] ユーザーの居住国
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
`app_group_id` | `null,` `string` | このユーザーが所属するアプリグループのBSON ID
`sf_created_at` | `timestamp`, `null` | この出来事がスノーパイプによって拾われた時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_INSTALLATTRIBUTION_SHARED {#USERS_BEHAVIORS_INSTALLATTRIBUTION_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | インストールしたユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
`device_id` | `null,` `string` | ユーザーが匿名の場合、このユーザーに関連付けられる `device_id`
`app_group_api_id` | `null,` `string` | このユーザーが所属するワークスペースのAPI ID
`time` | `int` | ユーザーがインストールしたUnixのタイムスタンプ
`source` | `string` | アトリビューション元
`app_group_id` | `null,` `string` | このユーザーが所属するアプリグループのBSON ID
`sf_created_at` | `timestamp`, `null` | この出来事がスノーパイプによって拾われた時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_LOCATION_SHARED {#USERS_BEHAVIORS_LOCATION_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | 位置を記録したユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
`app_group_api_id` | `null,` `string` | このユーザーが所属するワークスペースのAPI ID
`app_api_id` | `null,` `string` | この位置情報が記録されたアプリのAPI ID
`time` | `int` | ロケーションが記録されたUnixタイムスタンプ
`latitude` | `float` | [PII] 記録された位置の緯度
`longitude` | `float` | [PII] 記録された位置の経度
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
`app_group_id` | `null,` `string` | このユーザーが所属するアプリグループのBSON ID
`sf_created_at` | `timestamp`, `null` | この出来事がスノーパイプによって拾われた時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_PURCHASE_SHARED {#USERS_BEHAVIORS_PURCHASE_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | 購入したユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
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
`app_group_id` | `null,` `string` | このユーザーが所属するアプリグループのBSON ID
`sf_created_at` | `timestamp`, `null` | この出来事がスノーパイプによって拾われた時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_UNINSTALL_SHARED {#USERS_BEHAVIORS_UNINSTALL_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | アンインストールしたユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
`device_id` | `null,` `string` | ユーザーが匿名の場合、このユーザーに関連付けられる `device_id`
`app_group_api_id` | `null,` `string` | このユーザーが所属するワークスペースのAPI ID
`app_api_id` | `null,` `string` | アンインストールされたアプリのAPI ID
`time` | `int` | ユーザーがアンインストールしたUnixタイムスタンプ
`app_group_id` | `null,` `string` | このユーザーが所属するアプリグループのBSON ID
`sf_created_at` | `timestamp`, `null` | この出来事がスノーパイプによって拾われた時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_UPGRADEDAPP_SHARED {#USERS_BEHAVIORS_UPGRADEDAPP_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | アプリをアップグレードしたユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
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
`app_group_id` | `null,` `string` | このユーザーが所属するアプリグループのBSON ID
`sf_created_at` | `timestamp`, `null` | この出来事がスノーパイプによって拾われた時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_APP_FIRSTSESSION_SHARED {#USERS_BEHAVIORS_APP_FIRSTSESSION_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このアクションを実行するユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
`app_group_api_id` | `null,` `string` | このユーザーが所属するワークスペースのAPI ID
`app_api_id` | `null,` `string` | このセッションが発生したアプリのAPI ID
`time` | `int` | セッションが開始されたUnixタイムスタンプ
`session_id` | `string` | セッションのUUID
`gender` | `null,` `string` | [PII] ユーザーの性別
`country` | `null,` `string` | [PII] ユーザーの居住国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
`device_id` | `null,` `string` | セッションが発生したデバイスの ID
`sdk_version` | `null,` `string` | セッション中に使用されたBraze SDKのバージョン
`platform` | `null,` `string` | デバイスのプラットフォーム
`os_version` | `null,` `string` | デバイスのオペレーティング・システムのバージョン
`device_model` | `null,` `string` | デバイスのモデル
`app_group_id` | `null,` `string` | このユーザーが所属するアプリグループのBSON ID
`sf_created_at` | `timestamp`, `null` | この出来事がスノーパイプによって拾われた時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_BEHAVIORS_APP_NEWSFEEDIMPRESSION_SHARED {#USERS_BEHAVIORS_APP_NEWSFEEDIMPRESSION_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーのBrazeユーザー ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部 ID
`app_group_id` | `null,` `string` | このユーザーが所属するアプリグループのBSON ID
`app_group_api_id` | `null,` `string` | このユーザーが所属するアプリグループのAPI ID
`app_api_id` | `null,` `string` | このイベントが発生したアプリのAPI ID
`time` | `int` | イベントが発生したUNIXタイムスタンプ
`device_id` | `null,` `string` | イベントが発生したデバイスの ID
`sdk_version` | `null,` `string` | イベント中に使用されたBraze SDKのバージョン
`platform` | `null,` `string` | デバイスのプラットフォーム
`os_version` | `null,` `string` | デバイスのオペレーティング・システムのバージョン
`device_model` | `null,` `string` | デバイスのモデル
`sf_created_at` | `timestamp`, `null` | この出来事がスノーパイプによって拾われた時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_APP_SESSIONEND_SHARED {#USERS_BEHAVIORS_APP_SESSIONEND_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このアクションを実行するユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
`app_group_api_id` | `null,` `string` | このユーザーが所属するワークスペースのAPI ID
`app_api_id` | `null,` `string` | このセッションが発生したアプリのAPI ID
`time` | `int` | セッションが終了したUnixタイムスタンプ
`duration` | `null, float` | セッションの継続時間（秒単位）
`session_id` | `string` | セッションのUUID
`device_id` | `null,` `string` | セッションが発生したデバイスの ID
`sdk_version` | `null,` `string` | セッション中に使用されたBraze SDKのバージョン
`platform` | `null,` `string` | デバイスのプラットフォーム
`os_version` | `null,` `string` | デバイスのオペレーティング・システムのバージョン
`device_model` | `null,` `string` | デバイスのモデル
`app_group_id` | `null,` `string` | このユーザーが所属するアプリグループのBSON ID
`sf_created_at` | `timestamp`, `null` | この出来事がスノーパイプによって拾われた時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_APP_SESSIONSTART_SHARED {#USERS_BEHAVIORS_APP_SESSIONSTART_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このアクションを実行するユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
`app_api_id` | `null,` `string` | このセッションが発生したアプリのAPI ID
`app_group_api_id` | `null,` `string` | このユーザーが所属するワークスペースのAPI ID
`time` | `int` | セッションが開始されたUnixタイムスタンプ
`session_id` | `string` | セッションのUUID
`device_id` | `null,` `string` | セッションが発生したデバイスの ID
`sdk_version` | `null,` `string` | セッション中に使用されたBraze SDKのバージョン
`platform` | `null,` `string` | デバイスのプラットフォーム
`os_version` | `null,` `string` | デバイスのオペレーティング・システムのバージョン
`device_model` | `null,` `string` | デバイスのモデル
`app_group_id` | `null,` `string` | このユーザーが所属するアプリグループのBSON ID
`sf_created_at` | `timestamp`, `null` | この出来事がスノーパイプによって拾われた時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_GEOFENCE_DATAEVENT_SHARED {#USERS_BEHAVIORS_GEOFENCE_DATAEVENT_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | イベントを実行したユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
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
`app_group_id` | `null,` `string` | このユーザーが所属するアプリグループのBSON ID
`sf_created_at` | `timestamp`, `null` | この出来事がスノーパイプによって拾われた時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_GEOFENCE_RECORDEVENT_SHARED {#USERS_BEHAVIORS_GEOFENCE_RECORDEVENT_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | イベントを実行したユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
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
`app_group_id` | `null,` `string` | このユーザーが所属するアプリグループのBSON ID
`sf_created_at` | `timestamp`, `null` | この出来事がスノーパイプによって拾われた時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_BEHAVIORS_LIVEACTIVITY_PUSHTOSTARTTOKENCHANGE_SHARED {#USERS_BEHAVIORS_LIVEACTIVITY_PUSHTOSTARTTOKENCHANGE_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーのBrazeユーザー ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部 ID
`time` | `int` | イベントが発生したUNIXタイムスタンプ
`app_group_id` | `null,` `string` | このユーザーが所属するアプリグループのBSON ID
`activity_attributes_type` | `null,` `string` | ライブアクティビティ属性タイプ
`push_to_start_token` | `null,` `string` | ライブアクティビティの開始トークンをプッシュする
`device_id` | `null,` `string` | イベントが発生したデバイスの ID
`sdk_version` | `null,` `string` | イベント中に使用されたBraze SDKのバージョン
`ios_push_token_apns_gateway` | `null, int` | プッシュトークンのAPNゲートウェイは、iOSプッシュトークンのみに適用される。開発環境は1、本番環境は2である。
`push_token_state_change_type` | `null,` `string` | プッシュトークンの状態変化タイプの説明
`app_group_api_id` | `null,` `string` | このユーザーが所属するアプリグループのAPI ID
`app_api_id` | `null,` `string` | このイベントが発生したアプリのAPI ID
`sf_created_at` | `timestamp`, `null` | この出来事がスノーパイプによって拾われた時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_BEHAVIORS_LIVEACTIVITY_UPDATETOKENCHANGE_SHARED {#USERS_BEHAVIORS_LIVEACTIVITY_UPDATETOKENCHANGE_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーのBrazeユーザー ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部 ID
`time` | `int` | イベントが発生したUNIXタイムスタンプ
`app_group_id` | `null,` `string` | このユーザーが所属するアプリグループのBSON ID
`activity_id` | `null,` `string` | ライブアクティビティ識別子
`update_token` | `null,` `string` | ライブアクティビティ更新トークン
`device_id` | `null,` `string` | イベントが発生したデバイスの ID
`sdk_version` | `null,` `string` | イベント中に使用されたBraze SDKのバージョン
`ios_push_token_apns_gateway` | `null, int` | プッシュトークンのAPNゲートウェイは、iOSプッシュトークンのみに適用される。開発環境は1、本番環境は2である。
`push_token_state_change_type` | `null,` `string` | プッシュトークンの状態変化タイプの説明
`app_group_api_id` | `null,` `string` | このユーザーが所属するアプリグループのAPI ID
`app_api_id` | `null,` `string` | このイベントが発生したアプリのAPI ID
`sf_created_at` | `timestamp`, `null` | この出来事がスノーパイプによって拾われた時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_BEHAVIORS_PUSHNOTIFICATION_TOKENSTATECHANGE_SHARED {#USERS_BEHAVIORS_PUSHNOTIFICATION_TOKENSTATECHANGE_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`time` | `int` | イベントが発生したUNIXタイムスタンプ
`user_id` | `string` | このイベントを実行したユーザーのBrazeユーザー ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部 ID
`sdk_version` | `null,` `string` | イベント中に使用されたBraze SDKのバージョン
`platform` | `null,` `string` | デバイスのプラットフォーム
`app_group_id` | `null,` `string` | このユーザーが所属するアプリグループのBSON ID
`push_token` | `null,` `string` | イベントのプッシュトークン
`push_token_created_at` | `null, int` | プッシュトークンが作成されたUNIXタイムスタンプ
`push_token_updated_at` | `null, int` | プッシュトークンが最後に更新されたUNIXタイムスタンプ
`push_token_foreground_push_disabled` | `null, boolean` | プッシュトークンのフォアグラウンドプッシュ無効フラグ
`push_token_device_id` | `null,` `string` | プッシュトークンのデバイスID
`push_token_provisionally_opted_in` | `null, boolean` | プッシュトークンの仮オプトインフラグ
`ios_push_token_apns_gateway` | `null, int` | プッシュトークンのAPNゲートウェイは、iOSプッシュトークンのみに適用される。開発環境は1、本番環境は2である。
`web_push_token_public_key` | `null,` `string` | プッシュトークンの公開キー。Web プッシュトークンにのみ適用される。
`web_push_token_user_auth` | `null,` `string` | プッシュトークンのユーザー認証は、Web プッシュトークンにのみ適用される。
`web_push_token_vapid_public_key` | `null,` `string` | プッシュトークンのVAPID公開キー。Web プッシュトークンのみに適用される。
`push_token_state_change_type` | `null,` `string` | プッシュトークンの状態変化タイプの説明
`app_group_api_id` | `null,` `string` | このユーザーが所属するアプリグループのAPI ID
`app_api_id` | `null,` `string` | このイベントが発生したアプリのAPI ID
`sf_created_at` | `timestamp`, `null` | この出来事がスノーパイプによって拾われた時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_SUBSCRIPTION_GLOBALSTATECHANGE_SHARED {#USERS_BEHAVIORS_SUBSCRIPTION_GLOBALSTATECHANGE_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | 影響を受けたユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
`email_address` | `null,` `string` | [PII] ユーザーのメールアドレス
`state_change_source` | `null,` `string` | 状態変更のソース（REST、SDK、ダッシュボードなど）
`subscription_status` | `string` | サブスクリプションステータス: 「サブスクライバー」「配信停止」「オプトイン」
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
`app_group_id` | `null,` `string` | このユーザーが所属するアプリグループのBSON ID
`channel_identifier` | `null,` `string` | [PII] イベントの対象となるチャネルにおけるユーザーの識別子。
`sf_created_at` | `timestamp`, `null` | この出来事がスノーパイプによって拾われた時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED {#USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | 影響を受けたユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
`device_id` | `null,` `string` | ユーザーが匿名の場合、このユーザーに関連付けられる `device_id`
`app_group_api_id` | `null,` `string` | このユーザーが所属するワークスペースのAPI ID
`email_address` | `null,` `string` | [PII] ユーザーのメールアドレス
`phone_number` | `null,` `string` | [PII] ユーザーの電話番号（E164形式）
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
`subscription_status` | `string` | サブスクリプションステータス: 「サブスクライバー」「配信停止」「オプトイン」
`time` | `int` | サブスクリプションの状態が変更されたUnixタイムスタンプ
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`send_id` | `null,` `string` | このサブスクリプション状態変更アクションが発信したメッセージ送信ID
`state_change_source` | `null,` `string` | 状態変更のソース（REST、SDK、ダッシュボードなど）
`app_group_id` | `null,` `string` | このユーザーが所属するアプリグループのBSON ID
`dispatch_id` | `null,` `string` | このメッセージが属するディスパッチの ID
`channel_identifier` | `null,` `string` | [PII] イベントの対象となるチャネルにおけるユーザーの識別子。
`sf_created_at` | `timestamp`, `null` | この出来事がスノーパイプによって拾われた時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## キャンペーン

### USERS_CAMPAIGNS_CONVERSION_SHARED {#USERS_CAMPAIGNS_CONVERSION_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
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
`country` | `null,` `string` | [PII] ユーザーの居住国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
`app_group_id` | `null,` `string` | このユーザーが所属するアプリグループのBSON ID
`sf_created_at` | `timestamp`, `null` | この出来事がスノーパイプによって拾われた時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CAMPAIGNS_ENROLLINCONTROL_SHARED {#USERS_CAMPAIGNS_ENROLLINCONTROL_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
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
`country` | `null,` `string` | [PII] ユーザーの居住国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
`app_group_id` | `null,` `string` | このユーザーが所属するアプリグループのBSON ID
`sf_created_at` | `timestamp`, `null` | この出来事がスノーパイプによって拾われた時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CAMPAIGNS_FREQUENCYCAP_SHARED {#USERS_CAMPAIGNS_FREQUENCYCAP_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
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
`country` | `null,` `string` | [PII] ユーザーの居住国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
`app_group_id` | `null,` `string` | このユーザーが所属するアプリグループのBSON ID
`sf_created_at` | `timestamp`, `null` | この出来事がスノーパイプによって拾われた時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CAMPAIGNS_REVENUE_SHARED {#USERS_CAMPAIGNS_REVENUE_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
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
`country` | `null,` `string` | [PII] ユーザーの居住国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
`revenue` | `long` | 発生したセント単位の米ドル収益額
`app_group_id` | `null,` `string` | このユーザーが所属するアプリグループのBSON ID
`sf_created_at` | `timestamp`, `null` | この出来事がスノーパイプによって拾われた時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## キャンバス

### USERS_CANVASSTEP_PROGRESSION_SHARED {#USERS_CANVASSTEP_PROGRESSION_SHARED}

| フィールド                                  | タイプ                     | 説明                                                                                                     |
| -------------------------------------- | ------------------------ | --------------------------------------------------------------------------------------------------------------- |
| `id`                                   | `string`, `null`    | このイベントのグローバルな一意の ID                                                                               |
| `user_id`                              | `string`, `null`    | このイベントを実行したユーザーのBraze ID                                                                   |
| `external_user_id`                     | `string`, `null`    | [PII] ユーザーの外部ユーザー ID                                                                              |
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
| `external_user_id`                     | `string`, `null`    | [PII] ユーザーの外部ユーザー ID                                                                              |
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
| `country`                              | `string`, `null`    | [PII] ユーザーの居住国                                                                                       |
| `timezone`                             | `string`, `null`    | ユーザーのタイムゾーン                                                                                            |
| `language`                             | `string`, `null`    | [PII] ユーザーの言語                                                                                      |
| `sf_created_at`                        | `timestamp`, `null` | このイベントが Snowpipe に検出されたとき                                                                   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_ENTRY_SHARED {#USERS_CANVAS_ENTRY_SHARED}

| フィールド                     | タイプ                     | 説明                                                          |
| ------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                      | `string`, `null`    | このイベントのグローバルな一意の ID                                    |
| `user_id`                 | `string`, `null`    | このイベントを実行したユーザーのBraze ID                        |
| `external_user_id`        | `string`, `null`    | [PII] ユーザーの外部ユーザー ID                                   |
| `device_id`               | `string`, `null`    | ユーザーが匿名の場合、このユーザーに紐づくデバイスのID |
| `app_group_id`            | `string`, `null`    | このユーザーが所属するワークスペースのBraze ID                        |
| `app_group_api_id`        | `string`, `null`    | このユーザーが所属するワークスペースのAPI ID                         |
| `time`                    | `int`, `null`       | イベントが発生したUnixタイムスタンプ                           |
| `canvas_id`               | `string`, `null`    | (Braze専用）このイベントが属するキャンバスのID          |
| `canvas_api_id`           | `string`, `null`    | このイベントが属するキャンバスのAPI ID                           |
| `canvas_variation_api_id` | `string`, `null`    | このイベントが属するキャンバスのバリエーションのAPI ID                 |
| `canvas_step_api_id`      | `string`, `null`    | [非推奨] このイベントが属するキャンバスステップのAPI ID         |
| `gender`                  | `string`, `null`    | [PII] ユーザーの性別                                             |
| `country`                 | `string`, `null`    | [PII] ユーザーの居住国                                            |
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
| `external_user_id`        | `string`, `null`    | [PII] ユーザーの外部ユーザー ID                                   |
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
| `external_user_id`        | `string`, `null`    | [PII] ユーザーの外部ユーザー ID                                   |
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
| `external_user_id`          | `string`, `null`    | [PII] ユーザーの外部ユーザー ID                                                                              |
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
| `experiment_split_api_id` | `string`, `null` | ユーザーが登録された実験のAPI ID |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_EXPERIMENTSTEP_SPLITENTRY_SHARED {#USERS_CANVAS_EXPERIMENTSTEP_SPLITENTRY_SHARED}

| フィールド                     | タイプ                     | 説明                                                          |
| ------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                      | `string`, `null`    | このイベントのグローバルな一意の ID                                    |
| `user_id`                 | `string`, `null`    | このイベントを実行したユーザーのBraze ID                        |
| `external_user_id`        | `string`, `null`    | [PII] ユーザーの外部ユーザー ID                                   |
| `app_group_id`            | `string`, `null`    | このユーザーが所属するワークスペースのBraze ID                        |
| `time`                    | `int`, `null`       | イベントが発生したUnixタイムスタンプ                           |
| `canvas_id`               | `string`, `null`    | (Braze専用）このイベントが属するキャンバスのID          |
| `canvas_api_id`           | `string`, `null`    | このイベントが属するキャンバスのAPI ID                           |
| `canvas_variation_api_id` | `string`, `null`    | このイベントが属するキャンバスのバリエーションのAPI ID                 |
| `canvas_step_api_id`      | `string`, `null`    | このイベントが属するキャンバスステップのAPI ID                      |
| `experiment_step_api_id`  | `string`, `null`    | このイベントが属する実験ステップのAPI ID                  |
| `in_control_group`        | `boolean`, `null`   | ユーザーがコントロール・グループに登録されていた場合、真となる                   |
| `sf_created_at`           | `timestamp`, `null` | このイベントが Snowpipe に検出されたとき                        |

\|`experiment_split_api_id`  | `string`,`null`  | ユーザーが登録された実験分割のAPI ID |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_FREQUENCYCAP_SHARED {#USERS_CANVAS_FREQUENCYCAP_SHARED}

| フィールド                                  | タイプ                     | 説明                                                          |
| -------------------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                                   | `string`, `null`    | このイベントのグローバルな一意の ID                                    |
| `user_id`                              | `string`, `null`    | このイベントを実行したユーザーのBraze ID                        |
| `external_user_id`                     | `string`, `null`    | [PII] ユーザーの外部ユーザー ID                                   |
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
| `country`                              | `string`, `null`    | [PII] ユーザーの居住国                                            |
| `timezone`                             | `string`, `null`    | ユーザーのタイムゾーン                                                 |
| `language`                             | `string`, `null`    | [PII] ユーザーの言語                                           |
| `sf_created_at`                        | `timestamp`, `null` | このイベントが Snowpipe に検出されたとき                        |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_REVENUE_SHARED {#USERS_CANVAS_REVENUE_SHARED}

| フィールド                                  | タイプ                     | 説明                                                          |
| -------------------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                                   | `string`, `null`    | このイベントのグローバルな一意の ID                                    |
| `user_id`                              | `string`, `null`    | このイベントを実行したユーザーのBraze ID                        |
| `external_user_id`                     | `string`, `null`    | [PII] ユーザーの外部ユーザー ID                                   |
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
| `country`                              | `string`, `null`    | [PII] ユーザーの居住国                                            |
| `timezone`                             | `string`, `null`    | ユーザーのタイムゾーン                                                 |
| `language`                             | `string`, `null`    | [PII] ユーザーの言語                                           |
| `revenue`                              | `int`, `null`       | 米ドル建てで発生した収益額（セント表示               |
| `sf_created_at`                        | `timestamp`, `null` | このイベントが Snowpipe に検出されたとき                        |
| `app_api_id` | `string`, `null` | このイベントが発生したアプリのAPI ID |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## メッセージ


### USERS_MESSAGES_BANNER_ABORT_SHARED {#USERS_MESSAGES_BANNER_ABORT_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーのBrazeユーザー ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部 ID
`app_group_id` | `null,` `string` | このユーザーが所属するアプリグループのBSON ID
`app_group_api_id` | `null,` `string` | このユーザーが所属するアプリグループのAPI ID
`time` | `int` | イベントが発生したUNIXタイムスタンプ
`app_api_id` | `null,` `string` | このイベントが発生したアプリのAPI ID
`campaign_id` | `null,` `string` | このイベントが属するキャンペーンのBSON ID
`campaign_api_id` | `null,` `string` | このイベントが属するキャンペーンのAPI ID
`message_variation_api_id` | `null,` `string` | このユーザーが受信したメッセージバリエーションのAPI ID
`gender` | `null,` `string` | [PII] ユーザーの性別
`country` | `null,` `string` | [PII] ユーザーの居住国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
`device_id` | `null,` `string` | イベントが発生したデバイスの ID
`sdk_version` | `null,` `string` | イベント中に使用されたBraze SDKのバージョン
`platform` | `null,` `string` | デバイスのプラットフォーム
`os_version` | `null,` `string` | デバイスのオペレーティング・システムのバージョン
`device_model` | `null,` `string` | デバイスのモデル
`resolution` | `null,` `string` | デバイスの解像度
`carrier` | `null,` `string` | デバイスの通信事業者
`browser` | `null,` `string` | デバイスブラウザ - 抽出元user_agent\- 開封された場所
`ad_id` | `null,` `string` | [PII] 広告識別子
`ad_id_type` | `null,` `string` | 一つ ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']
`ad_tracking_enabled` | `null, boolean` | デバイスの広告トラッキングが有効かどうか
`abort_type` | `null,` `string` | 中絶の種類の一つ ['liquid_abort_message', 'quiet_hours', 'rate_limit']
`abort_log` | `null,` `string` | [PII] 中止の詳細を説明するログメッセージ（最大128文字）
`banner_placement_id` | `null,` `string` | 顧客指定のバナー配置ID
`sf_created_at` | `timestamp`, `null` | この出来事がスノーパイプによって拾われた時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_BANNER_CLICK_SHARED {#USERS_MESSAGES_BANNER_CLICK_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーのBrazeユーザー ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部 ID
`app_group_id` | `null,` `string` | このユーザーが所属するアプリグループのBSON ID
`app_group_api_id` | `null,` `string` | このユーザーが所属するアプリグループのAPI ID
`time` | `int` | イベントが発生したUNIXタイムスタンプ
`app_api_id` | `null,` `string` | このイベントが発生したアプリのAPI ID
`campaign_id` | `null,` `string` | このイベントが属するキャンペーンのBSON ID
`campaign_api_id` | `null,` `string` | このイベントが属するキャンペーンのAPI ID
`message_variation_api_id` | `null,` `string` | このユーザーが受信したメッセージバリエーションのAPI ID
`gender` | `null,` `string` | [PII] ユーザーの性別
`country` | `null,` `string` | [PII] ユーザーの居住国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
`device_id` | `null,` `string` | イベントが発生したデバイスの ID
`sdk_version` | `null,` `string` | イベント中に使用されたBraze SDKのバージョン
`platform` | `null,` `string` | デバイスのプラットフォーム
`os_version` | `null,` `string` | デバイスのオペレーティング・システムのバージョン
`device_model` | `null,` `string` | デバイスのモデル
`resolution` | `null,` `string` | デバイスの解像度
`carrier` | `null,` `string` | デバイスの通信事業者
`browser` | `null,` `string` | デバイスブラウザ - 抽出元user_agent\- 開封された場所
`button_id` | `null,` `string` | クリックされたボタンの ID (このクリックがボタンのクリックを表す場合)
`ad_id` | `null,` `string` | [PII] 広告識別子
`ad_id_type` | `null,` `string` | 一つ ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']
`ad_tracking_enabled` | `null, boolean` | デバイスの広告トラッキングが有効かどうか
`banner_placement_id` | `null,` `string` | 顧客指定のバナー配置ID
`sf_created_at` | `timestamp`, `null` | この出来事がスノーパイプによって拾われた時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_BANNER_IMPRESSION_SHARED {#USERS_MESSAGES_BANNER_IMPRESSION_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーのBrazeユーザー ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部 ID
`app_group_id` | `null,` `string` | このユーザーが所属するアプリグループのBSON ID
`app_group_api_id` | `null,` `string` | このユーザーが所属するアプリグループのAPI ID
`time` | `int` | イベントが発生したUNIXタイムスタンプ
`app_api_id` | `null,` `string` | このイベントが発生したアプリのAPI ID
`campaign_id` | `null,` `string` | このイベントが属するキャンペーンのBSON ID
`campaign_api_id` | `null,` `string` | このイベントが属するキャンペーンのAPI ID
`message_variation_api_id` | `null,` `string` | このユーザーが受信したメッセージバリエーションのAPI ID
`gender` | `null,` `string` | [PII] ユーザーの性別
`country` | `null,` `string` | [PII] ユーザーの居住国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
`device_id` | `null,` `string` | イベントが発生したデバイスの ID
`sdk_version` | `null,` `string` | イベント中に使用されたBraze SDKのバージョン
`platform` | `null,` `string` | デバイスのプラットフォーム
`os_version` | `null,` `string` | デバイスのオペレーティング・システムのバージョン
`device_model` | `null,` `string` | デバイスのモデル
`resolution` | `null,` `string` | デバイスの解像度
`carrier` | `null,` `string` | デバイスの通信事業者
`browser` | `null,` `string` | デバイスブラウザ - 抽出元user_agent\- 開封された場所
`ad_id` | `null,` `string` | [PII] 広告識別子
`ad_id_type` | `null,` `string` | 一つ ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']
`ad_tracking_enabled` | `null, boolean` | デバイスの広告トラッキングが有効かどうか
`banner_placement_id` | `null,` `string` | 顧客指定のバナー配置ID
`sf_created_at` | `timestamp`, `null` | この出来事がスノーパイプによって拾われた時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_CONTENTCARD_ABORT_SHARED {#USERS_MESSAGES_CONTENTCARD_ABORT_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
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
`country` | `null,` `string` | [PII] ユーザーの居住国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
`abort_type` | `null,` `string` | 中絶の種類の一つ ['liquid_abort_message', 'quiet_hours', 'rate_limit']
`abort_log` | `null,` `string` | [PII] 中止の詳細を説明するログメッセージ（最大2,000文字）
`app_group_id` | `null,` `string` | このユーザーが所属するアプリグループのBSON ID
`sf_created_at` | `timestamp`, `null` | この出来事がスノーパイプによって拾われた時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_CONTENTCARD_CLICK_SHARED {#USERS_MESSAGES_CONTENTCARD_CLICK_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーのBraze ID
`content_card_id` | `string` | このイベントを発生させたカードのID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
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
`country` | `null,` `string` | [PII] ユーザーの居住国
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
`app_group_id` | `null,` `string` | このユーザーが所属するアプリグループのBSON ID
`sf_created_at` | `timestamp`, `null` | この出来事がスノーパイプによって拾われた時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_CONTENTCARD_DISMISS_SHARED {#USERS_MESSAGES_CONTENTCARD_DISMISS_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーのBraze ID
`content_card_id` | `string` | このイベントを発生させたカードのID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
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
`country` | `null,` `string` | [PII] ユーザーの居住国
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
`app_group_id` | `null,` `string` | このユーザーが所属するアプリグループのBSON ID
`sf_created_at` | `timestamp`, `null` | この出来事がスノーパイプによって拾われた時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_CONTENTCARD_IMPRESSION_SHARED {#USERS_MESSAGES_CONTENTCARD_IMPRESSION_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーのBraze ID
`content_card_id` | `string` | このイベントを発生させたカードのID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
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
`country` | `null,` `string` | [PII] ユーザーの居住国
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
`app_group_id` | `null,` `string` | このユーザーが所属するアプリグループのBSON ID
`sf_created_at` | `timestamp`, `null` | この出来事がスノーパイプによって拾われた時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_CONTENTCARD_SEND_SHARED {#USERS_MESSAGES_CONTENTCARD_SEND_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
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
`country` | `null,` `string` | [PII] ユーザーの居住国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
`content_card_id` | `string` | このイベントを発生させたカードのID
`app_group_id` | `null,` `string` | このユーザーが所属するアプリグループのBSON ID
`message_extras` | `null,` `string` | [PII] 液体レンダリング中のタグ付きキーと値のペアを格納したJSON文字列
`sf_created_at` | `timestamp`, `null` | この出来事がスノーパイプによって拾われた時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_ABORT_SHARED {#USERS_MESSAGES_EMAIL_ABORT_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
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
`country` | `null,` `string` | [PII] ユーザーの居住国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
`email_address` | `string` | [PII] ユーザーのメールアドレス
`ip_pool` | `null,` `string` | メール送信元のIPプール
`abort_type` | `null,` `string` | 中絶の種類の一つ ['liquid_abort_message', 'quiet_hours', 'rate_limit']
`abort_log` | `null,` `string` | [PII] 中止の詳細を説明するログメッセージ（最大2,000文字）
`app_group_id` | `null,` `string` | このユーザーが所属するアプリグループのBSON ID
`sf_created_at` | `timestamp`, `null` | この出来事がスノーパイプによって拾われた時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_BOUNCE_SHARED {#USERS_MESSAGES_EMAIL_BOUNCE_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
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
`country` | `null,` `string` | [PII] ユーザーの居住国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
`email_address` | `string` | [PII] ユーザーのメールアドレス
`sending_ip` | `null,` `string` | メール送信元のIPアドレス
`ip_pool` | `null,` `string` | メール送信元のIPプール
`bounce_reason` | `null,` `string` | [PII] このバウンスイベントで受信したSMTP理由コードとユーザーフレンドリーなメッセージ
`esp` | `null,` `string` | イベントに関連する ESP (SparkPost、SendGrid、または Amazon SES)
`from_domain` | `null,` `string` | メールの送信ドメイン
`is_drop` | `null, boolean` | このイベントがドロップイベントとしてカウントされることを示す。
`app_group_id` | `null,` `string` | このユーザーが所属するアプリグループのBSON ID
`sf_created_at` | `timestamp`, `null` | この出来事がスノーパイプによって拾われた時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_CLICK_SHARED {#USERS_MESSAGES_EMAIL_CLICK_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
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
`country` | `null,` `string` | [PII] ユーザーの居住国
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
`app_group_id` | `null,` `string` | このユーザーが所属するアプリグループのBSON ID
`is_suspected_bot_click` | `null, boolean` | このイベントがボットイベントとして処理されたかどうか
`suspected_bot_click_reason` | `null, object` | なぜこのイベントがボットとして分類されたのか
`sf_created_at` | `timestamp`, `null` | この出来事がスノーパイプによって拾われた時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_EMAIL_DEFERRAL_SHARED {#USERS_MESSAGES_EMAIL_DEFERRAL_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`time` | `int` | イベントが発生したUNIXタイムスタンプ
`user_id` | `string` | このイベントを実行したユーザーのBrazeユーザー ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部 ID
`app_group_id` | `null,` `string` | このユーザーが所属するアプリグループのBSON ID
`app_group_api_id` | `null,` `string` | このユーザーが所属するアプリグループのAPI ID
`send_id` | `null,` `string` | このメッセージが属するメッセージ送信ID
`campaign_id` | `null,` `string` | このイベントが属するキャンペーンのBSON ID
`campaign_api_id` | `null,` `string` | このイベントが属するキャンペーンのAPI ID
`message_variation_api_id` | `null,` `string` | このユーザーが受信したメッセージバリエーションのAPI ID
`canvas_id` | `null,` `string` | このイベントが属するキャンバスのBSON ID
`canvas_api_id` | `null,` `string` | このイベントが属するキャンバスのAPI ID
`canvas_variation_api_id` | `null,` `string` | このイベントが属するキャンバスのバリエーションのAPI ID
`canvas_step_api_id` | `null,` `string` | このイベントが属するキャンバスステップのAPI ID
`canvas_step_message_variation_api_id` | `null,` `string` | このユーザーが受け取ったキャンバスステップメッセージのバリエーションのAPI ID
`dispatch_id` | `null,` `string` | このメッセージが属するディスパッチの ID
`email_address` | `null,` `string` | [PII] ユーザーのメールアドレス
`recipient_domain` | `null,` `string` | 受信者のメールドメイン
`esp` | `null,` `string` | イベントに関連するメールサービスプロバイダー (ESP)（SparkPostやSendGrid、あるいはAmazon SES）
`from_domain` | `null,` `string` | メールの送信ドメイン
`ip_pool` | `null,` `string` | メール送信元となったIPプール
`sending_ip` | `null,` `string` | メール送信元のIPアドレス
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`deferral_reason` | `null,` `string` | [PII] この遅延イベントで受信したSMTPコードとユーザーフレンドリーなメッセージ
`attempt_count` | `null, int` | メッセージングでメッセージを送信しようとした試行回数
`sf_created_at` | `timestamp`, `null` | この出来事がスノーパイプによって拾われた時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_DELIVERY_SHARED {#USERS_MESSAGES_EMAIL_DELIVERY_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
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
`country` | `null,` `string` | [PII] ユーザーの居住国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
`email_address` | `string` | [PII] ユーザーのメールアドレス
`sending_ip` | `null,` `string` | メールの送信元IPアドレス
`ip_pool` | `null,` `string` | メール送信元のIPプール
`esp` | `null,` `string` | イベントに関連する ESP (SparkPost、SendGrid、または Amazon SES)
`from_domain` | `null,` `string` | メールの送信ドメイン
`app_group_id` | `null,` `string` | このユーザーが所属するアプリグループのBSON ID
`sf_created_at` | `timestamp`, `null` | この出来事がスノーパイプによって拾われた時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_MARKASSPAM_SHARED {#USERS_MESSAGES_EMAIL_MARKASSPAM_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
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
`country` | `null,` `string` | [PII] ユーザーの居住国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
`email_address` | `string` | [PII] ユーザーのメールアドレス
`user_agent` | `null,` `string` | スパム報告が発生したユーザーエージェント
`ip_pool` | `null,` `string` | メール送信元のIPプール
`esp` | `null,` `string` | イベントに関連する ESP (SparkPost、SendGrid、または Amazon SES)
`from_domain` | `null,` `string` | メールの送信ドメイン
`app_group_id` | `null,` `string` | このユーザーが所属するアプリグループのBSON ID
`sf_created_at` | `timestamp`, `null` | この出来事がスノーパイプによって拾われた時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_OPEN_SHARED {#USERS_MESSAGES_EMAIL_OPEN_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
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
`country` | `null,` `string` | [PII] ユーザーの居住国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
`email_address` | `string` | [PII] ユーザーのメールアドレス
`user_agent` | `null,` `string` | オープンが発生したユーザーエージェント
`ip_pool` | `null,` `string` | メール送信元のIPプール
`machine_open` | `null,` `string` | 例えば、メールのプライバシー保護が有効になっているAppleデバイスによって、ユーザーの関与なしに開封イベントがトリガーされた場合、'true'が入力される。値は、より詳細な情報を提供するために、時間の経過とともに変化する可能性があります。
`esp` | `null,` `string` | イベントに関連する ESP (SparkPost、SendGrid、または Amazon SES)
`from_domain` | `null,` `string` | メールの送信ドメイン
`is_amp` | `null, boolean` | AMPイベントであることを示す
`app_group_id` | `null,` `string` | このユーザーが所属するアプリグループのBSON ID
`sf_created_at` | `timestamp`, `null` | この出来事がスノーパイプによって拾われた時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_SEND_SHARED {#USERS_MESSAGES_EMAIL_SEND_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
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
`country` | `null,` `string` | [PII] ユーザーの居住国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
`email_address` | `string` | [PII] ユーザーのメールアドレス
`ip_pool` | `null,` `string` | メール送信元のIPプール
`message_extras` | `null,` `string` | [PII] Liquidレンダリング時のタグ付きキーと値のペアのJSON文字列
`esp` | `null,` `string` | イベントに関連する ESP (SparkPost、SendGrid、または Amazon SES)
`from_domain` | `null,` `string` | メールの送信ドメイン
`sf_created_at` | `timestamp`, `null` | このイベントが Snowpipe に検出されたとき
`app_group_id` | `null,` `string` | このユーザーが所属するアプリグループのBSON ID
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_SOFTBOUNCE_SHARED {#USERS_MESSAGES_EMAIL_SOFTBOUNCE_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
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
`country` | `null,` `string` | [PII] ユーザーの居住国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
`email_address` | `string` | [PII] ユーザーのメールアドレス
`sending_ip` | `null,` `string` | メール送信元のIPアドレス
`ip_pool` | `null,` `string` | メール送信元のIPプール
`bounce_reason` | `null,` `string` | [PII] このバウンスイベントで受信したSMTP理由コードとユーザーフレンドリーなメッセージ
`esp` | `null,` `string` | イベントに関連する ESP (SparkPost、SendGrid、または Amazon SES)
`from_domain` | `null,` `string` | メールの送信ドメイン
`app_group_id` | `null,` `string` | このユーザーが所属するアプリグループのBSON ID
`sf_created_at` | `timestamp`, `null` | この出来事がスノーパイプによって拾われた時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED {#USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
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
`country` | `null,` `string` | [PII] ユーザーの居住国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
`email_address` | `string` | [PII] ユーザーのメールアドレス
`ip_pool` | `null,` `string` | メール送信元のIPプール
`app_group_id` | `null,` `string` | このユーザーが所属するアプリグループのBSON ID
`sf_created_at` | `timestamp`, `null` | この出来事がスノーパイプによって拾われた時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_FEATUREFLAG_IMPRESSION_SHARED {#USERS_MESSAGES_FEATUREFLAG_IMPRESSION_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`app_api_id` | `null,` `string` | このイベントが発生したアプリのAPI ID
`app_group_id` | `null,` `string` | このユーザーが所属するアプリグループのBSON ID
`app_group_api_id` | `null,` `string` | このユーザーが所属するアプリグループのAPI ID
`campaign_api_id` | `null,` `string` | このイベントが属するキャンペーンのAPI ID
`campaign_id` | `null,` `string` | このイベントが属するキャンペーンのBSON ID
`canvas_api_id` | `null,` `string` | このイベントが属するキャンバスのAPI ID
`canvas_id` | `null,` `string` | このイベントが属するキャンバスのBSON ID
`canvas_step_api_id` | `null,` `string` | このイベントが属するキャンバスステップのAPI ID
`canvas_step_message_variation_api_id` | `null,` `string` | このユーザーが受け取ったキャンバスステップメッセージのバリエーションのAPI ID
`canvas_variation_api_id` | `null,` `string` | このイベントが属するキャンバスのバリエーションのAPI ID
`feature_flag_id_name` | `null,` `string` | フィーチャーフラグのロールアウト識別子
`message_variation_api_id` | `null,` `string` | このユーザーが受信したメッセージバリエーションのAPI ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部 ID
`device_id` | `null,` `string` | イベントが発生したデバイスの ID
`time` | `int` | イベントが発生したUNIXタイムスタンプ
`gender` | `null,` `string` | [PII] ユーザーの性別
`browser` | `null,` `string` | デバイスブラウザ - 抽出元user_agent\- 開封された場所
`carrier` | `null,` `string` | デバイスの通信事業者
`country` | `null,` `string` | [PII] ユーザーの居住国
`device_model` | `null,` `string` | デバイスのモデル
`language` | `null,` `string` | [PII] ユーザーの言語
`os_version` | `null,` `string` | デバイスのオペレーティング・システムのバージョン
`platform` | `null,` `string` | デバイスのプラットフォーム
`resolution` | `null,` `string` | デバイスの解像度
`sdk_version` | `null,` `string` | イベント中に使用されたBraze SDKのバージョン
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`user_id` | `string` | このイベントを実行したユーザーのBrazeユーザー ID
`sf_created_at` | `timestamp`, `null` | この出来事がスノーパイプによって拾われた時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_INAPPMESSAGE_ABORT_SHARED {#USERS_MESSAGES_INAPPMESSAGE_ABORT_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
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
`country` | `null,` `string` | [PII] ユーザーの居住国
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
`abort_type` | `null,` `string` | 中絶の種類の一つ ['liquid_abort_message', 'quiet_hours', 'rate_limit']
`abort_log` | `null,` `string` | [PII] 中止の詳細を説明するログメッセージ（最大2,000文字）
`app_group_id` | `null,` `string` | このユーザーが所属するアプリグループのBSON ID
`sf_created_at` | `timestamp`, `null` | この出来事がスノーパイプによって拾われた時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_INAPPMESSAGE_CLICK_SHARED {#USERS_MESSAGES_INAPPMESSAGE_CLICK_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
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
`country` | `null,` `string` | [PII] ユーザーの居住国
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
`app_group_id` | `null,` `string` | このユーザーが所属するアプリグループのBSON ID
`sf_created_at` | `timestamp`, `null` | この出来事がスノーパイプによって拾われた時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_INAPPMESSAGE_IMPRESSION_SHARED {#USERS_MESSAGES_INAPPMESSAGE_IMPRESSION_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
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
`country` | `null,` `string` | [PII] ユーザーの居住国
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
`app_group_id` | `null,` `string` | このユーザーが所属するアプリグループのBSON ID
`message_extras` | `null,` `string` | [PII] 液体レンダリング中のタグ付きキーと値のペアを格納したJSON文字列
`locale_key` | `null,` `string` | [PII] このメッセージの作成に使用された翻訳に対応するキー（例：'en-us'）。デフォルトの場合はnull。
`sf_created_at` | `timestamp`, `null` | この出来事がスノーパイプによって拾われた時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_LINE_ABORT_SHARED {#USERS_MESSAGES_LINE_ABORT_SHARED}

フィールド | タイプ | 説明
------|------|------------
`app_group_api_id` | `null,` `string` | このユーザーが所属するアプリグループのAPI ID
`app_group_id` | `null,` `string` | このユーザーが所属するアプリグループのBSON ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部 ID
`id` | `string` | このイベントのグローバルな一意の ID
`time` | `int` | イベントが発生したUNIXタイムスタンプ
`user_id` | `string` | このイベントを実行したユーザーのBrazeユーザー ID
`abort_log` | `null,` `string` | [PII] 中止の詳細を説明するログメッセージ（最大128文字）
`abort_type` | `null,` `string` | 中絶の種類の一つ ['liquid_abort_message', 'quiet_hours', 'rate_limit']
`campaign_api_id` | `null,` `string` | このイベントが属するキャンペーンのAPI ID
`canvas_step_api_id` | `null,` `string` | このイベントが属するキャンバスステップのAPI ID
`canvas_step_message_variation_api_id` | `null,` `string` | このユーザーが受け取ったキャンバスステップメッセージのバリエーションのAPI ID
`device_id` | `null,` `string` | イベントが発生したデバイスの ID
`dispatch_id` | `null,` `string` | このメッセージが属するディスパッチの ID
`line_channel_id` | `null,` `string` | メッセージが送信された、または受信されたLINEチャネルID
`line_channel_name` | `null,` `string` | メッセージが送信された、または受信されたLINEチャネル名
`message_variation_api_id` | `null,` `string` | このユーザーが受信したメッセージバリエーションのAPI ID
`native_line_id` | `null,` `string` | [PII] メッセージの送信元または受信元のユーザーのLINE ID
`send_id` | `null,` `string` | このメッセージが属するメッセージ送信ID
`subscription_group_api_id` | `string` | サブスクリプショングループAPI ID
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`campaign_name` | `null,` `string` | キャンペーン名
`canvas_step_name` | `null,` `string` | キャンバスステップの名前
`canvas_variation_api_id` | `null,` `string` | このイベントが属するキャンバスのバリエーションのAPI ID
`canvas_api_id` | `null,` `string` | このイベントが属するキャンバスのAPI ID
`sf_created_at` | `timestamp`, `null` | この出来事がスノーパイプによって拾われた時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_LINE_CLICK_SHARED {#USERS_MESSAGES_LINE_CLICK_SHARED}

フィールド | タイプ | 説明
------|------|------------
`app_group_api_id` | `null,` `string` | このユーザーが所属するアプリグループのAPI ID
`app_group_id` | `null,` `string` | このユーザーが所属するアプリグループのBSON ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部 ID
`id` | `string` | このイベントのグローバルな一意の ID
`time` | `int` | イベントが発生したUNIXタイムスタンプ
`user_id` | `string` | このイベントを実行したユーザーのBrazeユーザー ID
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`native_line_id` | `null,` `string` | [PII] メッセージの送信元または受信元のユーザーのLINE ID
`line_channel_id` | `null,` `string` | メッセージが送信された、または受信されたLINEチャネルID
`line_channel_name` | `null,` `string` | メッセージが送信された、または受信されたLINEチャネル名
`subscription_group_api_id` | `string` | サブスクリプショングループAPI ID
`campaign_api_id` | `null,` `string` | このイベントが属するキャンペーンのAPI ID
`campaign_name` | `null,` `string` | キャンペーン名
`message_variation_api_id` | `null,` `string` | このユーザーが受信したメッセージバリエーションのAPI ID
`canvas_api_id` | `null,` `string` | このイベントが属するキャンバスのAPI ID
`canvas_variation_api_id` | `null,` `string` | このイベントが属するキャンバスのバリエーションのAPI ID
`canvas_step_api_id` | `null,` `string` | このイベントが属するキャンバスステップのAPI ID
`canvas_step_message_variation_api_id` | `null,` `string` | このユーザーが受け取ったキャンバスステップメッセージのバリエーションのAPI ID
`canvas_step_name` | `null,` `string` | キャンバスステップの名前
`dispatch_id` | `null,` `string` | このメッセージが属するディスパッチの ID
`device_id` | `null,` `string` | イベントが発生したデバイスの ID
`send_id` | `null,` `string` | このメッセージが属するメッセージ送信ID
`is_suspected_bot_click` | `null, boolean` | このイベントがボットイベントとして処理されたかどうか
`short_url` | `null,` `string` | クリックされた短縮URL
`url` | `null,` `string` | ユーザーがクリックしたURL
`user_agent` | `null,` `string` | スパム報告が発生したユーザーエージェント
`sf_created_at` | `timestamp`, `null` | この出来事がスノーパイプによって拾われた時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_LINE_INBOUNDRECEIVE_SHARED {#USERS_MESSAGES_LINE_INBOUNDRECEIVE_SHARED}

フィールド | タイプ | 説明
------|------|------------
`app_group_api_id` | `null,` `string` | このユーザーが所属するアプリグループのAPI ID
`app_group_id` | `null,` `string` | このユーザーが所属するアプリグループのBSON ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部 ID
`id` | `string` | このイベントのグローバルな一意の ID
`time` | `int` | イベントが発生したUNIXタイムスタンプ
`user_id` | `string` | このイベントを実行したユーザーのBrazeユーザー ID
`campaign_api_id` | `null,` `string` | このイベントが属するキャンペーンのAPI ID
`campaign_name` | `null,` `string` | キャンペーン名
`canvas_api_id` | `null,` `string` | このイベントが属するキャンバスのAPI ID
`canvas_step_api_id` | `null,` `string` | このイベントが属するキャンバスステップのAPI ID
`canvas_step_message_variation_api_id` | `null,` `string` | このユーザーが受け取ったキャンバスステップメッセージのバリエーションのAPI ID
`canvas_step_name` | `null,` `string` | キャンバスステップの名前
`canvas_variation_api_id` | `null,` `string` | このイベントが属するキャンバスのバリエーションのAPI ID
`device_id` | `null,` `string` | イベントが発生したデバイスの ID
`dispatch_id` | `null,` `string` | このメッセージが属するディスパッチの ID
`line_channel_id` | `null,` `string` | メッセージが送信された、または受信されたLINEチャネルID
`line_channel_name` | `null,` `string` | メッセージが送信された、または受信されたLINEチャネル名
`media_id` | `null,` `string` | LINEが生成したIDで、LINEから受信したメディアを取得するのに使える。
`message_body` | `null,` `string` | ユーザーからの入力された応答
`message_variation_api_id` | `null,` `string` | このユーザーが受信したメッセージバリエーションのAPI ID
`native_line_id` | `null,` `string` | [PII] メッセージの送信元または受信元のユーザーのLINE ID
`send_id` | `null,` `string` | このメッセージが属するメッセージ送信ID
`subscription_group_api_id` | `string` | サブスクリプショングループAPI ID
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`sf_created_at` | `timestamp`, `null` | この出来事がスノーパイプによって拾われた時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_LINE_SEND_SHARED {#USERS_MESSAGES_LINE_SEND_SHARED}

フィールド | タイプ | 説明
------|------|------------
`app_group_api_id` | `null,` `string` | このユーザーが所属するアプリグループのAPI ID
`app_group_id` | `null,` `string` | このユーザーが所属するアプリグループのBSON ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部 ID
`id` | `string` | このイベントのグローバルな一意の ID
`time` | `int` | イベントが発生したUNIXタイムスタンプ
`user_id` | `string` | このイベントを実行したユーザーのBrazeユーザー ID
`campaign_api_id` | `null,` `string` | このイベントが属するキャンペーンのAPI ID
`campaign_name` | `null,` `string` | キャンペーン名
`canvas_api_id` | `null,` `string` | このイベントが属するキャンバスのAPI ID
`canvas_step_api_id` | `null,` `string` | このイベントが属するキャンバスステップのAPI ID
`canvas_step_message_variation_api_id` | `null,` `string` | このユーザーが受け取ったキャンバスステップメッセージのバリエーションのAPI ID
`canvas_step_name` | `null,` `string` | キャンバスステップの名前
`canvas_variation_api_id` | `null,` `string` | このイベントが属するキャンバスのバリエーションのAPI ID
`device_id` | `null,` `string` | イベントが発生したデバイスの ID
`dispatch_id` | `null,` `string` | このメッセージが属するディスパッチの ID
`line_channel_id` | `null,` `string` | メッセージが送信された、または受信されたLINEチャネルID
`line_channel_name` | `null,` `string` | メッセージが送信された、または受信されたLINEチャネル名
`message_extras` | `null,` `string` | [PII] 液体レンダリング中のタグ付きキーと値のペアを格納したJSON文字列
`message_variation_api_id` | `null,` `string` | このユーザーが受信したメッセージバリエーションのAPI ID
`native_line_id` | `null,` `string` | [PII] メッセージの送信元または受信元のユーザーのLINE ID
`send_id` | `null,` `string` | このメッセージが属するメッセージ送信ID
`subscription_group_api_id` | `string` | サブスクリプショングループAPI ID
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`sf_created_at` | `timestamp`, `null` | この出来事がスノーパイプによって拾われた時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_LIVEACTIVITY_OUTCOME_SHARED {#USERS_MESSAGES_LIVEACTIVITY_OUTCOME_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーのBrazeユーザー ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部 ID
`time` | `int` | イベントが発生したUNIXタイムスタンプ
`app_group_id` | `null,` `string` | このユーザーが所属するアプリグループのBSON ID
`activity_id` | `null,` `string` | ライブアクティビティ識別子
`activity_attributes_type` | `null,` `string` | ライブアクティビティ属性タイプ
`push_to_start_token` | `null,` `string` | ライブアクティビティの開始トークンをプッシュする
`update_token` | `null,` `string` | ライブアクティビティ更新トークン
`live_activity_event_type` | `null,` `string` | ライブアクティビティのイベントタイプ。['開始', '更新', '終了'] のいずれか
`live_activity_event_outcome` | `null,` `string` | ライブ活動イベントの結果
`app_group_api_id` | `null,` `string` | このユーザーが所属するアプリグループのAPI ID
`app_api_id` | `null,` `string` | このイベントが発生したアプリのAPI ID
`sf_created_at` | `timestamp`, `null` | この出来事がスノーパイプによって拾われた時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_LIVEACTIVITY_SEND_SHARED {#USERS_MESSAGES_LIVEACTIVITY_SEND_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーのBrazeユーザー ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部 ID
`time` | `int` | イベントが発生したUNIXタイムスタンプ
`app_group_id` | `null,` `string` | このユーザーが所属するアプリグループのBSON ID
`activity_id` | `null,` `string` | ライブアクティビティ識別子
`activity_attributes_type` | `null,` `string` | ライブアクティビティ属性タイプ
`push_to_start_token` | `null,` `string` | ライブアクティビティの開始トークンをプッシュする
`update_token` | `null,` `string` | ライブアクティビティ更新トークン
`live_activity_event_type` | `null,` `string` | ライブアクティビティのイベントタイプ。['開始', '更新', '終了'] のいずれか
`app_group_api_id` | `null,` `string` | このユーザーが所属するアプリグループのAPI ID
`app_api_id` | `null,` `string` | このイベントが発生したアプリのAPI ID
`sf_created_at` | `timestamp`, `null` | この出来事がスノーパイプによって拾われた時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_NEWSFEEDCARD_ABORT_SHARED {#USERS_MESSAGES_NEWSFEEDCARD_ABORT_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーのBrazeユーザー ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部 ID
`app_group_id` | `null,` `string` | このユーザーが所属するアプリグループのBSON ID
`app_group_api_id` | `null,` `string` | このユーザーが所属するアプリグループのAPI ID
`time` | `int` | イベントが発生したUNIXタイムスタンプ
`app_api_id` | `null,` `string` | このイベントが発生したアプリのAPI ID
`card_api_id` | `null,` `string` | カードのAPI ID
`gender` | `null,` `string` | [PII] ユーザーの性別
`country` | `null,` `string` | [PII] ユーザーの居住国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
`device_id` | `null,` `string` | イベントが発生したデバイスの ID
`sdk_version` | `null,` `string` | イベント中に使用されたBraze SDKのバージョン
`platform` | `null,` `string` | デバイスのプラットフォーム
`os_version` | `null,` `string` | デバイスのオペレーティング・システムのバージョン
`device_model` | `null,` `string` | デバイスのモデル
`resolution` | `null,` `string` | デバイスの解像度
`carrier` | `null,` `string` | デバイスの通信事業者
`browser` | `null,` `string` | デバイスブラウザ - 抽出元user_agent\- 開封された場所
`abort_type` | `null,` `string` | 中絶の種類の一つ ['liquid_abort_message', 'quiet_hours', 'rate_limit']
`abort_log` | `null,` `string` | [PII] 中止の詳細を説明するログメッセージ（最大128文字）
`sf_created_at` | `timestamp`, `null` | この出来事がスノーパイプによって拾われた時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_NEWSFEEDCARD_CLICK_SHARED {#USERS_MESSAGES_NEWSFEEDCARD_CLICK_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーのBrazeユーザー ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部 ID
`app_group_id` | `null,` `string` | このユーザーが所属するアプリグループのBSON ID
`app_group_api_id` | `null,` `string` | このユーザーが所属するアプリグループのAPI ID
`time` | `int` | イベントが発生したUNIXタイムスタンプ
`app_api_id` | `null,` `string` | このイベントが発生したアプリのAPI ID
`card_api_id` | `null,` `string` | カードのAPI ID
`gender` | `null,` `string` | [PII] ユーザーの性別
`country` | `null,` `string` | [PII] ユーザーの居住国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
`device_id` | `null,` `string` | イベントが発生したデバイスの ID
`sdk_version` | `null,` `string` | イベント中に使用されたBraze SDKのバージョン
`platform` | `null,` `string` | デバイスのプラットフォーム
`os_version` | `null,` `string` | デバイスのオペレーティング・システムのバージョン
`device_model` | `null,` `string` | デバイスのモデル
`resolution` | `null,` `string` | デバイスの解像度
`carrier` | `null,` `string` | デバイスの通信事業者
`browser` | `null,` `string` | デバイスブラウザ - 抽出元user_agent\- 開封された場所
`sf_created_at` | `timestamp`, `null` | この出来事がスノーパイプによって拾われた時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_NEWSFEEDCARD_IMPRESSION_SHARED {#USERS_MESSAGES_NEWSFEEDCARD_IMPRESSION_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーのBrazeユーザー ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部 ID
`app_group_id` | `null,` `string` | このユーザーが所属するアプリグループのBSON ID
`app_group_api_id` | `null,` `string` | このユーザーが所属するアプリグループのAPI ID
`time` | `int` | イベントが発生したUNIXタイムスタンプ
`app_api_id` | `null,` `string` | このイベントが発生したアプリのAPI ID
`card_api_id` | `null,` `string` | カードのAPI ID
`gender` | `null,` `string` | [PII] ユーザーの性別
`country` | `null,` `string` | [PII] ユーザーの居住国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
`device_id` | `null,` `string` | イベントが発生したデバイスの ID
`sdk_version` | `null,` `string` | イベント中に使用されたBraze SDKのバージョン
`platform` | `null,` `string` | デバイスのプラットフォーム
`os_version` | `null,` `string` | デバイスのオペレーティング・システムのバージョン
`device_model` | `null,` `string` | デバイスのモデル
`resolution` | `null,` `string` | デバイスの解像度
`carrier` | `null,` `string` | デバイスの通信事業者
`browser` | `null,` `string` | デバイスブラウザ - 抽出元user_agent\- 開封された場所
`sf_created_at` | `timestamp`, `null` | この出来事がスノーパイプによって拾われた時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_PUSHNOTIFICATION_ABORT_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_ABORT_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
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
`country` | `null,` `string` | [PII] ユーザーの居住国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
`platform` | `string` | デバイスのプラットフォーム
`abort_type` | `null,` `string` | 中絶の種類の一つ ['liquid_abort_message', 'quiet_hours', 'rate_limit']
`abort_log` | `null,` `string` | [PII] 中止の詳細を説明するログメッセージ（最大2,000文字）
`app_group_id` | `null,` `string` | このユーザーが所属するアプリグループのBSON ID
`sf_created_at` | `timestamp`, `null` | この出来事がスノーパイプによって拾われた時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_PUSHNOTIFICATION_BOUNCE_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_BOUNCE_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
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
`country` | `null,` `string` | [PII] ユーザーの居住国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
`platform` | `null,` `string` | デバイスのプラットフォーム
`ad_id` | `null,` `string` | [PII] 配信を試みた端末の広告ID
`ad_id_type` | `null,` `string` | 広告 ID のタイプ
`ad_tracking_enabled` | `null, boolean` | 広告のトラッキングを有効にしているかどうか
`app_group_id` | `null,` `string` | このユーザーが所属するアプリグループのBSON ID
`sf_created_at` | `timestamp`, `null` | この出来事がスノーパイプによって拾われた時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_PUSHNOTIFICATION_INFLUENCEDOPEN_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_INFLUENCEDOPEN_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
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
`country` | `null,` `string` | [PII] ユーザーの居住国
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
`app_group_id` | `null,` `string` | このユーザーが所属するアプリグループのBSON ID
`sf_created_at` | `timestamp`, `null` | この出来事がスノーパイプによって拾われた時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_PUSHNOTIFICATION_IOSFOREGROUND_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_IOSFOREGROUND_SHARED}

{% alert important %}
このイベントは[SWIFT SDK](https://github.com/braze-inc/braze-swift-sdk)ではサポートされておらず、[Objective-C SDK](https://github.com/Appboy/appboy-ios-sdk)では非推奨となっている。
{% endalert %}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
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
`country` | `null,` `string` | [PII] ユーザーの居住国
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
`ad_id` | `null,` `string` | [PII] 配信を試みた端末の広告ID
`ad_id_type` | `null,` `string` | 広告 ID のタイプ
`ad_tracking_enabled` | `null, boolean` | 広告のトラッキングを有効にしているかどうか
`app_group_id` | `null,` `string` | このユーザーが所属するアプリグループのBSON ID
`sf_created_at` | `timestamp`, `null` | この出来事がスノーパイプによって拾われた時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_PUSHNOTIFICATION_OPEN_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_OPEN_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
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
`country` | `null,` `string` | [PII] ユーザーの居住国
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
`button_string` | `null,` `string` | 押されたプッシュ通知ボタ(button_string)ンの識別子。ボタンクリック以外の場合にはnullとなる。
`button_action_type` | `null,` `string` | プッシュ通知ボタンのアクションタイプ。[URI,DEEP_LINK,NONE, CLOSE]のいずれか。ボタンクリック以外の場合にはnull
`slide_id` | `null,` `string` | ユーザがクリックしたプッシュカルーセルスライドのスライド識別子
`slide_action_type` | `null,` `string` | プッシュカルーセルスライドのアクションタイプ
`ad_id` | `null,` `string` | [PII] 配信を試みた端末の広告ID
`ad_id_type` | `null,` `string` | 広告 ID のタイプ
`ad_tracking_enabled` | `null, boolean` | 広告のトラッキングを有効にしているかどうか
`app_group_id` | `null,` `string` | このユーザーが所属するアプリグループのBSON ID
`sf_created_at` | `timestamp`, `null` | この出来事がスノーパイプによって拾われた時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_PUSHNOTIFICATION_SEND_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_SEND_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
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
`country` | `null,` `string` | [PII] ユーザーの居住国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
`platform` | `string` | デバイスのプラットフォーム
`ad_id` | `null,` `string` | [PII] 配信を試みた端末の広告ID
`ad_id_type` | `null,` `string` | 広告 ID のタイプ
`ad_tracking_enabled` | `null, boolean` | 広告のトラッキングを有効にしているかどうか
`app_group_id` | `null,` `string` | このユーザーが所属するアプリグループのBSON ID
`message_extras` | `null,` `string` | [PII] 液体レンダリング中のタグ付きキーと値のペアを格納したJSON文字列
`is_sampled` | `null,` `string` | プッシュ送信がサンプリングされ、配信イベントを期待したかどうかを示す
`locale_key` | `null,` `string` | [PII] このメッセージの作成に使用された翻訳に対応するキー（例：'en-us'）。デフォルトの場合はnull。
`sf_created_at` | `timestamp`, `null` | この出来事がスノーパイプによって拾われた時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_RCS_ABORT_SHARED {#USERS_MESSAGES_RCS_ABORT_SHARED}

フィールド | タイプ | 説明
------|------|------------
`app_group_api_id` | `null,` `string` | このユーザーが所属するアプリグループのAPI ID
`app_group_id` | `null,` `string` | このユーザーが所属するアプリグループのBSON ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部 ID
`id` | `string` | このイベントのグローバルな一意の ID
`time` | `int` | イベントが発生したUNIXタイムスタンプ
`user_id` | `string` | このイベントを実行したユーザーのBrazeユーザー ID
`abort_log` | `null,` `string` | [PII] 中止の詳細を説明するログメッセージ（最大128文字）
`abort_type` | `null,` `string` | 中絶の種類の一つ ['liquid_abort_message', 'quiet_hours', 'rate_limit']
`campaign_name` | `null,` `string` | キャンペーン名
`canvas_id` | `null,` `string` | このイベントが属するキャンバスのBSON ID
`canvas_name` | `null,` `string` | キャンバスの名前
`canvas_step_name` | `null,` `string` | キャンバスステップの名前
`canvas_variation_name` | `null,` `string` | このユーザーが受け取ったキャンバスのバリエーション名
`message_variation_name` | `null,` `string` | メッセージのバリエーション名
`subscription_group_api_id` | `string` | サブスクリプショングループAPI ID
`message_variation_api_id` | `null,` `string` | このユーザーが受信したメッセージバリエーションのAPI ID
`canvas_variation_api_id` | `null,` `string` | このイベントが属するキャンバスのバリエーションのAPI ID
`canvas_step_api_id` | `null,` `string` | このイベントが属するキャンバスステップのAPI ID
`canvas_step_message_variation_api_id` | `null,` `string` | このユーザーが受け取ったキャンバスステップメッセージのバリエーションのAPI ID
`campaign_api_id` | `null,` `string` | このイベントが属するキャンペーンのAPI ID
`sf_created_at` | `timestamp`, `null` | この出来事がスノーパイプによって拾われた時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_RCS_CLICK_SHARED {#USERS_MESSAGES_RCS_CLICK_SHARED}

フィールド | タイプ | 説明
------|------|------------
`app_group_api_id` | `null,` `string` | このユーザーが所属するアプリグループのAPI ID
`app_group_id` | `null,` `string` | このユーザーが所属するアプリグループのBSON ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部 ID
`id` | `string` | このイベントのグローバルな一意の ID
`time` | `int` | イベントが発生したUNIXタイムスタンプ
`user_id` | `string` | このイベントを実行したユーザーのBrazeユーザー ID
`campaign_name` | `null,` `string` | キャンペーン名
`canvas_id` | `null,` `string` | このイベントが属するキャンバスのBSON ID
`canvas_name` | `null,` `string` | キャンバスの名前
`canvas_step_name` | `null,` `string` | キャンバスステップの名前
`device_id` | `null,` `string` | イベントが発生したデバイスの ID
`is_suspected_bot_click` | `null, boolean` | このイベントがボットイベントとして処理されたかどうか
`message_variation_name` | `null,` `string` | メッセージのバリエーション名
`send_id` | `null,` `string` | このメッセージが属するメッセージ送信ID
`short_url` | `null,` `string` | クリックされた短縮URL
`suspected_bot_click_reason` | `null,` `string` | なぜこのイベントがボットとして分類されたのか
`user_agent` | `null,` `string` | スパム報告が発生したユーザーエージェント
`user_phone_number` | `null,` `string` | [PII] メッセージを受信したユーザーの電話番号
`message_variation_api_id` | `null,` `string` | このユーザーが受信したメッセージバリエーションのAPI ID
`canvas_variation_api_id` | `null,` `string` | このイベントが属するキャンバスのバリエーションのAPI ID
`canvas_step_api_id` | `null,` `string` | このイベントが属するキャンバスステップのAPI ID
`canvas_step_message_variation_api_id` | `null,` `string` | このユーザーが受け取ったキャンバスステップメッセージのバリエーションのAPI ID
`interaction_type` | `null,` `string` | クリックを生んだ相互作用の種類。例として文字列の値：テキストURL、返信、URLを開く
`element_label` | `null,` `string` | クリックされた要素に関するオプションの詳細情報。例えば、提案された返信やボタンのテキストなど。
`element_type` | `null,` `string` | 提案とボタンに共通するinteraction_type要素が、提案から来たものかボタンから来たものかを指定する。例:提案、ボタン
`campaign_api_id` | `null,` `string` | このイベントが属するキャンペーンのAPI ID
`url` | `null,` `string` | ユーザーがクリックしたURL
`subscription_group_api_id` | `string` | サブスクリプショングループAPI ID
`canvas_variation_name` | `null,` `string` | このユーザーが受け取ったキャンバスのバリエーション名
`sf_created_at` | `timestamp`, `null` | この出来事がスノーパイプによって拾われた時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_RCS_DELIVERY_SHARED {#USERS_MESSAGES_RCS_DELIVERY_SHARED}

フィールド | タイプ | 説明
------|------|------------
`app_group_api_id` | `null,` `string` | このユーザーが所属するアプリグループのAPI ID
`app_group_id` | `null,` `string` | このユーザーが所属するアプリグループのBSON ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部 ID
`id` | `string` | このイベントのグローバルな一意の ID
`time` | `int` | イベントが発生したUNIXタイムスタンプ
`user_id` | `string` | このイベントを実行したユーザーのBrazeユーザー ID
`campaign_name` | `null,` `string` | キャンペーン名
`canvas_id` | `null,` `string` | このイベントが属するキャンバスのBSON ID
`canvas_name` | `null,` `string` | キャンバスの名前
`canvas_step_name` | `null,` `string` | キャンバスステップの名前
`canvas_variation_name` | `null,` `string` | このユーザーが受け取ったキャンバスのバリエーション名
`device_id` | `null,` `string` | イベントが発生したデバイスの ID
`dispatch_id` | `null,` `string` | このメッセージが属するディスパッチの ID
`message_variation_name` | `null,` `string` | メッセージのバリエーション名
`send_id` | `null,` `string` | このメッセージが属するメッセージ送信ID
`subscription_group_api_id` | `string` | サブスクリプショングループAPI ID
`to_phone_number` | `null,` `string` | [PII] メッセージを受信するユーザーの電話番号は、+14155552671 のようなe.164形式で記載する。
`message_variation_api_id` | `null,` `string` | このユーザーが受信したメッセージバリエーションのAPI ID
`canvas_variation_api_id` | `null,` `string` | このイベントが属するキャンバスのバリエーションのAPI ID
`canvas_step_api_id` | `null,` `string` | このイベントが属するキャンバスステップのAPI ID
`canvas_step_message_variation_api_id` | `null,` `string` | このユーザーが受け取ったキャンバスステップメッセージのバリエーションのAPI ID
`campaign_api_id` | `null,` `string` | このイベントが属するキャンペーンのAPI ID
`from_rcs_sender` | `null,` `string` | メッセージを送信するために使用されたRCS送信者IDまたはエージェント名
`sf_created_at` | `timestamp`, `null` | この出来事がスノーパイプによって拾われた時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_RCS_INBOUNDRECEIVE_SHARED {#USERS_MESSAGES_RCS_INBOUNDRECEIVE_SHARED}

フィールド | タイプ | 説明
------|------|------------
`app_group_api_id` | `null,` `string` | このユーザーが所属するアプリグループのAPI ID
`app_group_id` | `null,` `string` | このユーザーが所属するアプリグループのBSON ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部 ID
`id` | `string` | このイベントのグローバルな一意の ID
`time` | `int` | イベントが発生したUNIXタイムスタンプ
`user_id` | `string` | このイベントを実行したユーザーのBrazeユーザー ID
`action` | `null,` `string` | このメッセージに対するアクション（例：購読、配信停止、またはなし）。
`campaign_name` | `null,` `string` | キャンペーン名
`canvas_id` | `null,` `string` | このイベントが属するキャンバスのBSON ID
`canvas_name` | `null,` `string` | キャンバスの名前
`canvas_step_name` | `null,` `string` | キャンバスステップの名前
`media_urls` | `null,` `string` | ユーザーからのメディアURL
`message_variation_name` | `null,` `string` | メッセージのバリエーション名
`send_id` | `null,` `string` | このメッセージが属するメッセージ送信ID
`user_phone_number` | `null,` `string` | [PII] メッセージを受信したユーザーの電話番号
`subscription_group_api_id` | `string` | サブスクリプショングループAPI ID
`message_body` | `null,` `string` | ユーザーからの入力された応答
`to_rcs_sender` | `null,` `string` | メッセージが送信された受信側のRCS送信者
`message_variation_api_id` | `null,` `string` | このユーザーが受信したメッセージバリエーションのAPI ID
`canvas_step_api_id` | `null,` `string` | このイベントが属するキャンバスステップのAPI ID
`canvas_variation_api_id` | `null,` `string` | このイベントが属するキャンバスのバリエーションのAPI ID
`canvas_step_message_variation_api_id` | `null,` `string` | このユーザーが受け取ったキャンバスステップメッセージのバリエーションのAPI ID
`campaign_api_id` | `null,` `string` | このイベントが属するキャンペーンのAPI ID
`campaign_id` | `null,` `string` | このイベントが属するキャンペーンのBSON ID
`sf_created_at` | `timestamp`, `null` | この出来事がスノーパイプによって拾われた時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_RCS_READ_SHARED {#USERS_MESSAGES_RCS_READ_SHARED}

フィールド | タイプ | 説明
------|------|------------
`app_group_api_id` | `null,` `string` | このユーザーが所属するアプリグループのAPI ID
`app_group_id` | `null,` `string` | このユーザーが所属するアプリグループのBSON ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部 ID
`id` | `string` | このイベントのグローバルな一意の ID
`time` | `int` | イベントが発生したUNIXタイムスタンプ
`user_id` | `string` | このイベントを実行したユーザーのBrazeユーザー ID
`campaign_name` | `null,` `string` | キャンペーン名
`canvas_id` | `null,` `string` | このイベントが属するキャンバスのBSON ID
`canvas_name` | `null,` `string` | キャンバスの名前
`canvas_step_name` | `null,` `string` | キャンバスステップの名前
`canvas_variation_name` | `null,` `string` | このユーザーが受け取ったキャンバスのバリエーション名
`message_variation_name` | `null,` `string` | メッセージのバリエーション名
`to_phone_number` | `null,` `string` | [PII] メッセージを受信するユーザーの電話番号は、+14155552671 のようなe.164形式で記載する。
`message_variation_api_id` | `null,` `string` | このユーザーが受信したメッセージバリエーションのAPI ID
`canvas_variation_api_id` | `null,` `string` | このイベントが属するキャンバスのバリエーションのAPI ID
`canvas_step_api_id` | `null,` `string` | このイベントが属するキャンバスステップのAPI ID
`canvas_step_message_variation_api_id` | `null,` `string` | このユーザーが受け取ったキャンバスステップメッセージのバリエーションのAPI ID
`campaign_api_id` | `null,` `string` | このイベントが属するキャンペーンのAPI ID
`sf_created_at` | `timestamp`, `null` | この出来事がスノーパイプによって拾われた時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_RCS_REJECTION_SHARED {#USERS_MESSAGES_RCS_REJECTION_SHARED}

フィールド | タイプ | 説明
------|------|------------
`app_group_api_id` | `null,` `string` | このユーザーが所属するアプリグループのAPI ID
`app_group_id` | `null,` `string` | このユーザーが所属するアプリグループのBSON ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部 ID
`id` | `string` | このイベントのグローバルな一意の ID
`time` | `int` | イベントが発生したUNIXタイムスタンプ
`user_id` | `string` | このイベントを実行したユーザーのBrazeユーザー ID
`campaign_name` | `null,` `string` | キャンペーン名
`canvas_id` | `null,` `string` | このイベントが属するキャンバスのBSON ID
`canvas_name` | `null,` `string` | キャンバスの名前
`canvas_step_name` | `null,` `string` | キャンバスステップの名前
`canvas_variation_name` | `null,` `string` | このユーザーが受け取ったキャンバスのバリエーション名
`device_id` | `null,` `string` | イベントが発生したデバイスの ID
`dispatch_id` | `null,` `string` | このメッセージが属するディスパッチの ID
`error` | `null,` `string` | エラー名
`from_rcs_sender` | `null,` `string` | メッセージを送信するために使用されたRCS送信者IDまたはエージェント名
`is_sms_fallback` | `null, boolean` | この拒否されたRCSメッセージに対してSMSフォールバックが試行されたかどうかを示す。SMS配信イベントと連動している。
`message_variation_name` | `null,` `string` | メッセージのバリエーション名
`provider_error_code` | `null,` `string` | プロバイダーからのエラーコード
`send_id` | `null,` `string` | このメッセージが属するメッセージ送信ID
`subscription_group_api_id` | `string` | サブスクリプショングループAPI ID
`message_variation_api_id` | `null,` `string` | このユーザーが受信したメッセージバリエーションのAPI ID
`canvas_variation_api_id` | `null,` `string` | このイベントが属するキャンバスのバリエーションのAPI ID
`canvas_step_api_id` | `null,` `string` | このイベントが属するキャンバスステップのAPI ID
`to_phone_number` | `null,` `string` | [PII] メッセージを受信するユーザーの電話番号は、+14155552671 のようなe.164形式で記載する。
`campaign_api_id` | `null,` `string` | このイベントが属するキャンペーンのAPI ID
`canvas_step_message_variation_api_id` | `null,` `string` | このユーザーが受け取ったキャンバスステップメッセージのバリエーションのAPI ID
`sf_created_at` | `timestamp`, `null` | この出来事がスノーパイプによって拾われた時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_RCS_SEND_SHARED {#USERS_MESSAGES_RCS_SEND_SHARED}

フィールド | タイプ | 説明
------|------|------------
`app_group_api_id` | `null,` `string` | このユーザーが所属するアプリグループのAPI ID
`app_group_id` | `null,` `string` | このユーザーが所属するアプリグループのBSON ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部 ID
`id` | `string` | このイベントのグローバルな一意の ID
`time` | `int` | イベントが発生したUNIXタイムスタンプ
`user_id` | `string` | このイベントを実行したユーザーのBrazeユーザー ID
`campaign_name` | `null,` `string` | キャンペーン名
`canvas_id` | `null,` `string` | このイベントが属するキャンバスのBSON ID
`canvas_name` | `null,` `string` | キャンバスの名前
`canvas_step_name` | `null,` `string` | キャンバスステップの名前
`canvas_variation_name` | `null,` `string` | このユーザーが受け取ったキャンバスのバリエーション名
`category` | `null,` `string` | キーワードカテゴリ名。自動返信メッセージでのみ設定される：'opt-in'、'opt-out'、'help'、またはカスタム値
`device_id` | `null,` `string` | イベントが発生したデバイスの ID
`dispatch_id` | `null,` `string` | このメッセージが属するディスパッチの ID
`from_rcs_sender` | `null,` `string` | メッセージを送信するために使用されたRCS送信者IDまたはエージェント名
`message_extras` | `null,` `string` | リキッドレンダリング中のタグ付きキーと値のペアのJSON文字列
`message_variation_name` | `null,` `string` | メッセージのバリエーション名
`send_id` | `null,` `string` | このメッセージが属するメッセージ送信ID
`subscription_group_api_id` | `string` | サブスクリプショングループAPI ID
`to_phone_number` | `null,` `string` | [PII] メッセージを受信するユーザーの電話番号は、+14155552671 のようなe.164形式で記載する。
`message_variation_api_id` | `null,` `string` | このユーザーが受信したメッセージバリエーションのAPI ID
`canvas_variation_api_id` | `null,` `string` | このイベントが属するキャンバスのバリエーションのAPI ID
`canvas_step_message_variation_api_id` | `null,` `string` | このユーザーが受け取ったキャンバスステップメッセージのバリエーションのAPI ID
`canvas_step_api_id` | `null,` `string` | このイベントが属するキャンバスステップのAPI ID
`campaign_api_id` | `null,` `string` | このイベントが属するキャンペーンのAPI ID
`sf_created_at` | `timestamp`, `null` | この出来事がスノーパイプによって拾われた時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_ABORT_SHARED {#USERS_MESSAGES_SMS_ABORT_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
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
`abort_type` | `null,` `string` | 中絶の種類の一つ ['liquid_abort_message', 'quiet_hours', 'rate_limit']
`abort_log` | `null,` `string` | [PII] 中止の詳細を説明するログメッセージ（最大2,000文字）
`app_group_id` | `null,` `string` | このユーザーが所属するアプリグループのBSON ID
`sf_created_at` | `timestamp`, `null` | この出来事がスノーパイプによって拾われた時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_CARRIERSEND_SHARED {#USERS_MESSAGES_SMS_CARRIERSEND_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
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
`country` | `null,` `string` | [PII] ユーザーの居住国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
`to_phone_number` | `null,` `string` | [PII] 受信者の電話番号
`from_phone_number` | `null,` `string` | SMSメッセージの送信元電話番号
`subscription_group_api_id` | `null,` `string` | サブスクリプショングループの外部 ID
`app_group_id` | `null,` `string` | このユーザーが所属するアプリグループのBSON ID
`sf_created_at` | `timestamp`, `null` | この出来事がスノーパイプによって拾われた時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_DELIVERY_SHARED {#USERS_MESSAGES_SMS_DELIVERY_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
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
`country` | `null,` `string` | [PII] ユーザーの居住国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
`to_phone_number` | `null,` `string` | [PII] 受信者の電話番号
`from_phone_number` | `null,` `string` | SMSメッセージが送信された電話番号
`subscription_group_api_id` | `null,` `string` | サブスクリプショングループの外部 ID
`app_group_id` | `null,` `string` | このユーザーが所属するアプリグループのBSON ID
`is_sms_fallback` | `null, boolean` | この拒否されたRCSメッセージに対してSMSフォールバックが試行されたかどうかを示す。SMS配信イベントと連動している。
`sf_created_at` | `timestamp`, `null` | この出来事がスノーパイプによって拾われた時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED {#USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
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
`country` | `null,` `string` | [PII] ユーザーの居住国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
`to_phone_number` | `null,` `string` | [PII] 受信者の電話番号
`subscription_group_api_id` | `null,` `string` | サブスクリプショングループの外部 ID
`error` | `null,` `string` | エラー名
`provider_error_code` | `null,` `string` | SMSサービスプロバイダからのエラーコード
`app_group_id` | `null,` `string` | このユーザーが所属するアプリグループのBSON ID
`is_sms_fallback` | `null, boolean` | この拒否されたRCSメッセージに対してSMSフォールバックが試行されたかどうかを示す。SMS配信イベントと連動している。
`sf_created_at` | `timestamp`, `null` | この出来事がスノーパイプによって拾われた時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED {#USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `null,` `string` | このイベントを実行したユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
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
`app_group_id` | `null,` `string` | このユーザーが所属するアプリグループのBSON ID
`sf_created_at` | `timestamp`, `null` | この出来事がスノーパイプによって拾われた時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_REJECTION_SHARED {#USERS_MESSAGES_SMS_REJECTION_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
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
`country` | `null,` `string` | [PII] ユーザーの居住国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
`to_phone_number` | `null,` `string` | [PII] 受信者の電話番号
`from_phone_number` | `null,` `string` | SMSメッセージの送信元電話番号
`subscription_group_api_id` | `null,` `string` | サブスクリプショングループの外部 ID
`error` | `null,` `string` | エラー名
`provider_error_code` | `null,` `string` | SMSサービスプロバイダからのエラーコード
`app_group_id` | `null,` `string` | このユーザーが所属するアプリグループのBSON ID
`is_sms_fallback` | `null, boolean` | この拒否されたRCSメッセージに対してSMSフォールバックが試行されたかどうかを示す。SMS配信イベントと連動している。
`sf_created_at` | `timestamp`, `null` | この出来事がスノーパイプによって拾われた時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_SEND_SHARED {#USERS_MESSAGES_SMS_SEND_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
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
`country` | `null,` `string` | [PII] ユーザーの居住国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
`to_phone_number` | `null,` `string` | [PII] 受信者の電話番号
`subscription_group_api_id` | `null,` `string` | サブスクリプショングループの外部 ID
`category` | `null,` `string` | キーワードカテゴリ名。自動返信メッセージにのみ入力されます。「オプトイン」、「オプトアウト」、「ヘルプ」、またはカスタム値
`app_group_id` | `null,` `string` | このユーザーが所属するアプリグループのBSON ID
`message_extras` | `null,` `string` | [PII] 液体レンダリング中のタグ付きキーと値のペアを格納したJSON文字列
`sf_created_at` | `timestamp`, `null` | この出来事がスノーパイプによって拾われた時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED {#USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `null,` `string` | 対象ユーザーのBraze IDは、ユーザークリックトラッキングを使用short_urlしていない場合short_url,nullとなる。
`external_user_id` | `null,` `string` | [PII] 対象ユーザーの外部ID（short_url存在する場合）。ユーザークリックトラッキングを使用short_urlしていない場合はnull。
`app_group_api_id` | `null,` `string` | 生成に使用されたワークスペースのAPI ID short_url
`time` | `int` | クリックされたshort_url時点のUnixタイムスタンプ
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`campaign_id` | `null,` `string` | キャンペーンのBrazeshort_url IDが生成された。キャンペーンからではない場合はnull。
`campaign_api_id` | `null,` `string` | キャンペーンのAPI IDは、short_urlキャンペーンから生成されたものである。キャンペーンからではない場合はnullである。
`message_variation_api_id` | `null,` `string` | メッセージバリエーションがshort_url生成されたAPI ID。キャンペーン由来でない場合はnull。
`canvas_id` | `null,` `string` | キャンバスに対してshort_url生成されたBraze ID。キャンバスからではない場合はnull。
`canvas_api_id` | `null,` `string` | キャンバス の API ID は生成された。キャンバスshort_url からのものではない場合は null である。
`canvas_variation_api_id` | `null,` `string` | キャンバスのバリエーション用にshort_url生成されたAPI ID。キャンバス以外からの場合はnull。
`canvas_step_api_id` | `null,` `string` | キャンバスステップのAPI short_urlIDは生成された。キャンバス以外からの場合はnullである。
`canvas_step_message_variation_api_id` | `null,` `string` | キャンバスステップメッセージのバリエーションshort_urlが生成されたAPI ID。キャンバスからのものではない場合はnull。
`url` | `string` | メッセージに含まれる元のURLは、リダイレクト先のURLである。 short_url
`short_url` | `string` | クリックされた短縮URL
`user_agent` | `null,` `string` | リクエストしているユーザーエージェント short_url
`user_phone_number` | `string` | [PII] ユーザーの電話番号
`device_id` | `null,` `string` | イベントが発生したデバイスの ID
`app_group_id` | `null,` `string` | このユーザーが所属するアプリグループのBSON ID
`is_suspected_bot_click` | `null, boolean` | このイベントがボットイベントとして処理されたかどうか
`suspected_bot_click_reason` | `null, object` | なぜこのイベントがボットとして分類されたのか
`sf_created_at` | `timestamp`, `null` | この出来事がスノーパイプによって拾われた時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WEBHOOK_ABORT_SHARED {#USERS_MESSAGES_WEBHOOK_ABORT_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
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
`country` | `null,` `string` | [PII] ユーザーの居住国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
`abort_type` | `null,` `string` | 中絶の種類の一つ ['liquid_abort_message', 'quiet_hours', 'rate_limit']
`abort_log` | `null,` `string` | [PII] 中止の詳細を説明するログメッセージ（最大2,000文字）
`app_group_id` | `null,` `string` | このユーザーが所属するアプリグループのBSON ID
`sf_created_at` | `timestamp`, `null` | この出来事がスノーパイプによって拾われた時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_WEBHOOK_FAILURE_SHARED {#USERS_MESSAGES_WEBHOOK_FAILURE_SHARED}

フィールド | タイプ | 説明
------|------|------------
`http_status_code` | `null, int` | 応答のHTTPステータスコード
`endpoint_url` | `null,` `string` | リクエストされているエンドポイントURL
`app_group_api_id` | `null,` `string` | このユーザーが所属するアプリグループのAPI ID
`app_group_id` | `null,` `string` | このユーザーが所属するアプリグループのBSON ID
`campaign_api_id` | `null,` `string` | このイベントが属するキャンペーンのAPI ID
`campaign_id` | `null,` `string` | このイベントが属するキャンペーンのBSON ID
`canvas_api_id` | `null,` `string` | このイベントが属するキャンバスのAPI ID
`canvas_id` | `null,` `string` | このイベントが属するキャンバスのBSON ID
`canvas_step_api_id` | `null,` `string` | このイベントが属するキャンバスステップのAPI ID
`canvas_step_message_variation_api_id` | `null,` `string` | このユーザーが受け取ったキャンバスステップメッセージのバリエーションのAPI ID
`canvas_variation_api_id` | `null,` `string` | このイベントが属するキャンバスのバリエーションのAPI ID
`content_length` | `null, int` | 応答の内容の長さ
`dispatch_id` | `null,` `string` | このメッセージが属するディスパッチの ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部 ID
`host` | `null,` `string` | リクエストのホスト
`id` | `string` | このイベントのグローバルな一意の ID
`message_variation_api_id` | `null,` `string` | このユーザーが受信したメッセージバリエーションのAPI ID
`raw_response` | `null,` `string` | エンドポイントからの切り詰められた生の応答
`retry_count` | `null, int` | 試行された再試行の回数
`send_id` | `null,` `string` | このメッセージが属するメッセージ送信ID
`time` | `int` | イベントが発生したUNIXタイムスタンプ
`url_path` | `null,` `string` | リクエストされているURLのパス
`user_id` | `string` | このイベントを実行したユーザーのBrazeユーザー ID
`webhook_duration` | `null, int` | このリクエストの総所要時間（ミリ秒単位）
`webhook_failure_source` | `null,` `string` | エラーがBrazeによって発生したのか、それともエンドポイント自体によって発生したのかを判断するためだ。ソースフィールドは外部エンドポイントである可能性がある。ステータスコードを無視してホストに到達不能とする。
`is_terminal` | `null, boolean` | この出来事が送信の最終的な試みであったかどうか
`sf_created_at` | `timestamp`, `null` | この出来事がスノーパイプによって拾われた時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WEBHOOK_SEND_SHARED {#USERS_MESSAGES_WEBHOOK_SEND_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
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
`country` | `null,` `string` | [PII] ユーザーの居住国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
`app_group_id` | `null,` `string` | このユーザーが所属するアプリグループのBSON ID
`message_extras` | `null,` `string` | [PII] 液体レンダリング中のタグ付きキーと値のペアを格納したJSON文字列
`sf_created_at` | `timestamp`, `null` | この出来事がスノーパイプによって拾われた時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WHATSAPP_ABORT_SHARED {#USERS_MESSAGES_WHATSAPP_ABORT_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`time` | `int` | イベントが発生したUnixタイムスタンプ
`to_phone_number` | 	`null,` `string` | [PII] 受信者の電話番号
`user_id` | `string` | このイベントを実行したユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
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
`abort_type` | `null,` `string` | 中絶の種類の一つ ['liquid_abort_message', 'quiet_hours', 'rate_limit']
`abort_log` | `null,` `string` | [PII] 中止の詳細を説明するログメッセージ（最大2,000文字）
`sf_created_at` | `timestamp`, `null` | このイベントが Snowpipe に検出されたとき      
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_WHATSAPP_CLICK_SHARED {#USERS_MESSAGES_WHATSAPP_CLICK_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーのBrazeユーザー ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部 ID
`device_id` | `null,` `string` | イベントが発生したデバイスの ID
`app_group_id` | `null,` `string` | このユーザーが所属するアプリグループのBSON ID
`app_group_api_id` | `null,` `string` | このユーザーが所属するアプリグループのAPI ID
`time` | `int` | イベントが発生したUNIXタイムスタンプ
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`campaign_id` | `null,` `string` | このイベントが属するキャンペーンのBSON ID
`campaign_api_id` | `null,` `string` | このイベントが属するキャンペーンのAPI ID
`message_variation_api_id` | `null,` `string` | このユーザーが受信したメッセージバリエーションのAPI ID
`canvas_id` | `null,` `string` | このイベントが属するキャンバスのBSON ID
`canvas_api_id` | `null,` `string` | このイベントが属するキャンバスのAPI ID
`canvas_variation_api_id` | `null,` `string` | このイベントが属するキャンバスのバリエーションのAPI ID
`canvas_step_api_id` | `null,` `string` | このイベントが属するキャンバスステップのAPI ID
`canvas_step_message_variation_api_id` | `null,` `string` | このユーザーが受け取ったキャンバスステップメッセージのバリエーションのAPI ID
`url` | `null,` `string` | ユーザーがクリックしたURL
`short_url` | `null,` `string` | クリックされた短縮URL
`user_agent` | `null,` `string` | スパム報告が発生したユーザーエージェント
`user_phone_number` | `null,` `string` | [PII] メッセージを受信したユーザーの電話番号
`sf_created_at` | `timestamp`, `null` | この出来事がスノーパイプによって拾われた時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WHATSAPP_DELIVERY_SHARED {#USERS_MESSAGES_WHATSAPP_DELIVERY_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`time` | `int` | イベントが発生したUnixタイムスタンプ
`to_phone_number` | `null,` `string` | [PII] 受信者の電話番号
`user_id` | `string` | このイベントを実行したユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
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
`send_id` | `null,` `string` | このメッセージが属するメッセージ送信ID
`flow_id` | `null,` `string` | WhatsAppマネージャーにおけるフローの固有ID。ユーザーがWhatsApp Flowに応答している場合、この条件が成立する。
`template_name` | `null,` `string` | [PII] WhatsAppマネージャー内のテンプレートの名前。テンプレートメッセージを送信する場合に存在させる
`message_id` | `null,` `string` | このメッセージに対してMetaが生成した固有ID
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WHATSAPP_FAILURE_SHARED {#USERS_MESSAGES_WHATSAPP_FAILURE_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`time` | `int` | イベントが発生したUnixタイムスタンプ
`to_phone_number` | `null,` `string` | [PII] 受信者の電話番号
`user_id` | `string` | このイベントを実行したユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
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
`send_id` | `null,` `string` | このメッセージが属するメッセージ送信ID
`message_id` | `null,` `string` | このメッセージに対してMetaが生成した固有ID
`template_name` | `null,` `string` | [PII] WhatsAppマネージャー内のテンプレートの名前。テンプレートメッセージを送信する場合に存在させる
`flow_id` | `null,` `string` | WhatsAppマネージャーにおけるフローの固有ID。ユーザーがWhatsApp Flowに応答している場合、この条件が成立する。
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WHATSAPP_INBOUNDRECEIVE_SHARED {#USERS_MESSAGES_WHATSAPP_INBOUNDRECEIVE_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`time` | `int` | イベントが発生したUnixタイムスタンプ
`user_phone_number` | `string` | [PII] メッセージを受信したユーザーの電話番号
`user_id` | `string` | このイベントを実行したユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
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
`catalog_id` | `null,` `string` | 製品がインバウンドメッセージで参照されている場合の製品のカタログ ID。それ以外の場合は、空です。
`product_id` | `null,` `string` | 購入した製品のID
`flow_id` | `null,` `string` | WhatsAppマネージャーにおけるフローの固有ID。ユーザーがWhatsApp Flowに応答している場合、この条件が成立する。
`flow_response_json` | `null,` `string` | [PII] ユーザーが入力したフォームの値。ユーザーがWhatsApp Flowに応答している場合、この条件が成立する。
`message_id` | `null,` `string` | このメッセージに対してMetaが生成した固有ID
`in_reply_to` | `null,` `string` | このメッセージが返信した返信message_id先のメッセージの件名
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WHATSAPP_READ_SHARED {#USERS_MESSAGES_WHATSAPP_READ_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`time` | `int` | イベントが発生したUnixタイムスタンプ
`to_phone_number` | `null,` `string` | [PII] 受信者の電話番号
`user_id` | `string` | このイベントを実行したユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
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
`send_id` | `null,` `string` | このメッセージが属するメッセージ送信ID
`template_name` | `null,` `string` | [PII] WhatsAppマネージャー内のテンプレートの名前。テンプレートメッセージを送信する場合に存在させる
`message_id` | `null,` `string` | このメッセージに対してMetaが生成した固有ID
`flow_id` | `null,` `string` | WhatsAppマネージャーにおけるフローの固有ID。ユーザーがWhatsApp Flowに応答している場合、この条件が成立する。
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WHATSAPP_SEND_SHARED {#USERS_MESSAGES_WHATSAPP_SEND_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`time` | `int` | イベントが発生したUnixタイムスタンプ
`to_phone_number` | `null,` `string`	| [PII] 受信者の電話番号
`user_id` | `string` | このイベントを実行したユーザーのBraze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
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
`message_extras` | `null,` `string` | [PII] Liquidレンダリング時のタグ付きキーと値のペアのJSON文字列
`sf_created_at` | `timestamp`, `null` | このイベントが Snowpipe に検出されたとき      
`send_id` | `null,` `string` | このメッセージが属するメッセージ送信ID
`flow_id` | `null,` `string` | WhatsAppマネージャーにおけるフローの固有ID。ユーザーがWhatsApp Flowに応答している場合、この条件が成立する。
`template_name` | `null,` `string` | [PII] WhatsAppマネージャー内のテンプレートの名前。テンプレートメッセージを送信する場合に存在させる
`message_id` | `null,` `string` | このメッセージに対してMetaが生成した固有ID
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## ユーザー

### USERS_RANDOMBUCKETNUMBERUPDATE_SHARED {#USERS_RANDOMBUCKETNUMBERUPDATE_SHARED}

| フィールド                       | タイプ                     | 説明                                        |
| --------------------------- | ------------------------ | -------------------------------------------------- |
| `id`                        | `string`, `null`    | このイベントのグローバルな一意の ID                  |
| `app_group_id`              | `string`, `null`    | このユーザーが所属するワークスペースのBraze ID      |
| `app_group_api_id`          | `string`, `null`    | このユーザーが所属するワークスペースのAPI ID       |
| `user_id`                   | `string`, `null`    | このイベントを実行したユーザーのBraze ID      |
| `external_user_id`          | `string`, `null`    | [PII] ユーザーの外部ユーザー ID                 |
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
| `external_user_id` | `string`, `null`    | [PII] ユーザーの外部ユーザー ID                                            |
| `device_id`        | `string`, `null`    | ユーザーが匿名の場合、このユーザーに紐づくデバイスのID          |
| `app_group_id`     | `string`, `null`    | このユーザーが所属するワークスペースのBraze ID                                 |
| `app_group_api_id` | `string`, `null`    | このユーザーが所属するワークスペースのAPI ID                                  |
| `app_api_id`       | `string`, `null`    | 孤児となったユーザーが所属していたアプリのAPI ID                               |
| `time`             | `int`, `null`       | ユーザーが孤児となったUnixタイムスタンプ                                 |
| `orphaned_by_id`   | `string`, `null`    | 孤児となったユーザーのプロファイルとマージされたユーザーのBraze ID |
| `sf_created_at`    | `timestamp`, `null` | このイベントが Snowpipe に検出されたとき                                 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }
