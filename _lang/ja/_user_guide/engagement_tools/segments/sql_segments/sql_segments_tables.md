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

このページは、[クエリビルダや]({{site.baseurl}}/user_guide/data_and_analytics/query_builder/) [SQL セグメントエクステンションの]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/)生成時に照会可能なテーブルと列の参照です。 

## 目次

テーブル | 説明
------|------------
[USERS\_BEHAVIORS\_CUSTOMEVENT\_SHARED](#USERS_BEHAVIORS_CUSTOMEVENT_SHARED) | ユーザーがカスタムイベントを実行するとき
[USERS\_BEHAVIORS\_INSTALLATTRIBUTION\_SHARED](#USERS_BEHAVIORS_INSTALLATTRIBUTION_SHARED) | ユーザーがアプリをインストールし、それをパートナーに帰属させるとき
[USERS\_BEHAVIORS\_LOCATION\_SHARED](#USERS_BEHAVIORS_LOCATION_SHARED) | ユーザーが位置情報を記録するとき
[USERS\_BEHAVIORS\_PURCHASE\_SHARED](#USERS_BEHAVIORS_PURCHASE_SHARED) | ユーザーが購入したとき
[USERS\_BEHAVIORS\_UNINSTALL\_SHARED](#USERS_BEHAVIORS_UNINSTALL_SHARED) | ユーザーがアプリをアンインストールするとき
[USERS\_BEHAVIORS\_UPGRADEDAPP\_SHARED](#USERS_BEHAVIORS_UPGRADEDAPP_SHARED) | ユーザーがアプリをアップグレードしたとき
[USERS\_BEHAVIORS\_APP\_FIRSTSESSION\_SHARED](#USERS_BEHAVIORS_APP_FIRSTSESSION_SHARED) | ユーザーが最初のセッションを行ったとき
[USERS\_BEHAVIORS\_APP\_NEWSFEEDIMPRESSION\_SHARED](#USERS_BEHAVIORS_APP_NEWSFEEDIMPRESSION_SHARED) | ユーザーがニュースフィードを閲覧するとき
[USERS\_BEHAVIORS\_APP\_SESSIONEND\_SHARED](#USERS_BEHAVIORS_APP_SESSIONEND_SHARED) | ユーザーがアプリのセッションを終了するとき
[USERS\_BEHAVIORS\_APP\_SESSIONSTART\_SHARED](#USERS_BEHAVIORS_APP_SESSIONSTART_SHARED) | ユーザーがアプリでセッションを開始するとき
[USERS\_BEHAVIORS\_GEOFENCE\_DATAEVENT\_SHARED](#USERS_BEHAVIORS_GEOFENCE_DATAEVENT_SHARED) | ユーザーがジオフェンスされた領域をトリガーしたとき (たとえば、ジオフェンスに出入りしたとき)。このイベントは、他のイベントとバッティングされ、標準的なイベントエンドポイントを通じて受信されたため、リアルタイムでエンドポイントによって受信されなかった可能性があります。
[USERS\_BEHAVIORS\_GEOFENCE\_RECORDEVENT\_SHARED | ](#USERS_BEHAVIORS_GEOFENCE_RECORDEVENT_SHARED)ユーザーがジオフェンスされた領域をトリガーしたとき (例: ジオフェンスに出入りしたとき)。このイベントは専用のジオフェンスエンドポイントを通じて受信されたため、ユーザーのデバイスがジオフェンスをトリガーしたことを検知するとすぐにリアルタイムで受信されます。<br><br>また、ジオフェンスエンドポイントのレート制限により、一部のジオフェンスイベントが RecordEvent として反映されない可能性があります。ただし、すべてのジオフェンスイベントは、DataEvent によって表現されます (ただし、バッチ処理によって遅延が発生する可能性があります)。
[USERS\_BEHAVIORS\_SUBSCRIPTION\_GLOBALSTATECHANGE\_SHARED](#USERS_BEHAVIORS_SUBSCRIPTION_GLOBALSTATECHANGE_SHARED) | ユーザーがメールなどのチャネルからグローバルにサブスクリプションされた、またはサブスクリプションが解除されたとき
[USERS\_BEHAVIORS\_SUBSCRIPTIONGROUP\_STATECHANGE\_SHARED](#USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED) | ユーザーがサブスクリプショングループに登録されたとき、またはサブスクリプショングループから登録解除されたとき。
[USERS\_CAMPAIGNS\_ABORT\_SHARED](#USERS_CAMPAIGNS_ABORT_SHARED) | 当初予定されていたキャンペーンメッセージが何らかの理由で中止されたとき。
[USERS\_CAMPAIGNS\_CONVERSION\_SHARED](#USERS_CAMPAIGNS_CONVERSION_SHARED) | キャンペーンでユーザーがコンバージョンしたとき
[USERS\_CAMPAIGNS\_ENROLLINCONTROL\_SHARED](#USERS_CAMPAIGNS_ENROLLINCONTROL_SHARED) | ユーザーがキャンペーンのコントロールグループに登録されたとき
[USERS\_CAMPAIGNS\_FREQUENCYCAP\_SHARED](#USERS_CAMPAIGNS_FREQUENCYCAP_SHARED) | ユーザーがキャンペーンで回数制限を受けたとき
[USERS\_CAMPAIGNS\_REVENUE\_SHARED](#USERS_CAMPAIGNS_REVENUE_SHARED) | ユーザーが 1 次コンバージョン期間内に収益を上げたとき
[USERS\_CANVAS\_ABORT\_SHARED](#USERS_CANVAS_ABORT_SHARED) | 当初スケジュールされていたキャンバスステップメッセージが何らかの理由で中止されたとき
[USERS\_CANVAS\_CONVERSION\_SHARED](#USERS_CANVAS_CONVERSION_SHARED) | キャンバスのコンバージョンイベントでユーザーがコンバージョンしたとき
[USERS\_CANVAS\_ENTRY\_SHARED](#USERS_CANVAS_ENTRY_SHARED) | ユーザーがキャンバスに入るとき
[USERS\_CANVAS\_EXIT\_MATCHEDAUDIENCE\_SHARED](#USERS_CANVAS_EXIT_MATCHEDAUDIENCE_SHARED) | ユーザーが視聴終了条件に一致してキャンバスを終了したとき
[USERS\_CANVAS\_EXIT\_PERFORMEDEVENT\_SHARED](#USERS_CANVAS_EXIT_PERFORMEDEVENT_SHARED) | ユーザーが例外イベントを実行してキャンバスを終了したとき
[USERS\_CANVAS\_EXPERIMENTSTEP\_CONVERSION\_SHARED](#USERS_CANVAS_EXPERIMENTSTEP_CONVERSION_SHARED) | キャンバス実験ステップでユーザーがコンバージョンしたとき
[USERS\_CANVAS\_EXPERIMENTSTEP\_SPLITENTRY\_SHARED](#USERS_CANVAS_EXPERIMENTSTEP_SPLITENTRY_SHARED) | ユーザーが実験ステップのパスを入力したとき
[USERS\_CANVAS\_FREQUENCYCAP\_SHARED](#USERS_CANVAS_FREQUENCYCAP_SHARED) | キャンバスのステップでユーザーが回数制限を受けたとき
[USERS\_CANVAS\_REVENUE\_SHARED](#USERS_CANVAS_REVENUE_SHARED) | ユーザーが 1 次コンバージョンイベント期間内に収益を上げたとき
[USERS\_MESSAGES\_CONTENTCARD\_ABORT\_SHARED](#USERS_MESSAGES_CONTENTCARD_ABORT_SHARED) | 当初スケジュールされていたコンテンツカードメッセージが、何らかの理由で中止されたとき
[USERS\_MESSAGES\_CONTENTCARD\_CLICK\_SHARED](#USERS_MESSAGES_CONTENTCARD_CLICK_SHARED) | ユーザーがコンテンツカードをクリックしたとき
[USERS\_MESSAGES\_CONTENTCARD\_DISMISS\_SHARED](#USERS_MESSAGES_CONTENTCARD_DISMISS_SHARED) | ユーザーがコンテンツカードを破棄したとき
[USERS\_MESSAGES\_CONTENTCARD\_IMPRESSION\_SHARED](#USERS_MESSAGES_CONTENTCARD_IMPRESSION_SHARED) | ユーザーがコンテンツカードを見るとき
[USERS\_MESSAGES\_CONTENTCARD\_SEND\_SHARED](#USERS_MESSAGES_CONTENTCARD_SEND_SHARED) | コンテンツカードをユーザーに送信するとき
[USERS\_MESSAGES\_EMAIL\_ABORT\_SHARED](#USERS_MESSAGES_EMAIL_ABORT_SHARED) | 当初予定されていたメールメッセージが何らかの理由で中止されたとき。
[USERS\_MESSAGES\_EMAIL\_BOUNCE\_SHARED](#USERS_MESSAGES_EMAIL_BOUNCE_SHARED) | メールサービスプロバイダー (ESP) がハードバウンスを返した。ハードバウンスとは、永続的な配信の失敗です。
[USERS\_MESSAGES\_EMAIL\_CLICK\_SHARED | ](#USERS_MESSAGES_EMAIL_CLICK_SHARED)ユーザーがメールのリンクをクリックした場合
[USERS\_MESSAGES\_EMAIL\_DELIVERY\_SHARED](#USERS_MESSAGES_EMAIL_DELIVERY_SHARED) | メールが配信されたとき
[USERS\_MESSAGES\_EMAIL\_MARKASSPAM\_SHARED](#USERS_MESSAGES_EMAIL_MARKASSPAM_SHARED) | メールがスパムとしてマークされたとき
[USERS\_MESSAGES\_EMAIL\_OPEN\_SHARED](#USERS_MESSAGES_EMAIL_OPEN_SHARED) | ユーザーがメールを開いたとき
[USERS\_MESSAGES\_EMAIL\_SEND\_SHARED](#USERS_MESSAGES_EMAIL_SEND_SHARED) | ユーザーにメールを送信するとき
[USERS\_MESSAGES\_EMAIL\_SOFTBOUNCE\_SHARED](#USERS_MESSAGES_EMAIL_SOFTBOUNCE_SHARED) | メールがソフトバウンスしたとき
[USERS\_MESSAGES\_EMAIL\_UNSUBSCRIBE\_SHARED](#USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED) | ユーザーがメールの配信を停止したとき
[USERS\_MESSAGES\_INAPPMESSAGE\_ABORT\_SHARED](#USERS_MESSAGES_INAPPMESSAGE_ABORT_SHARED) | 当初予定されていたアプリ内メッセージが何らかの理由で中止されたとき。
[USERS\_MESSAGES\_INAPPMESSAGE\_CLICK\_SHARED](#USERS_MESSAGES_INAPPMESSAGE_CLICK_SHARED) | ユーザーがアプリ内メッセージをクリックしたとき
[USERS\_MESSAGES\_INAPPMESSAGE\_IMPRESSION\_SHARED](#USERS_MESSAGES_INAPPMESSAGE_IMPRESSION_SHARED) | ユーザーがアプリ内メッセージを閲覧したとき
[USERS\_MESSAGES\_NEWSFEEDCARD\_ABORT\_SHARED](#USERS_MESSAGES_NEWSFEEDCARD_ABORT_SHARED) | 当初予定されていたニュースフィードカードのメッセージが何らかの理由で中止されたとき。
[USERS\_MESSAGES\_NEWSFEEDCARD\_CLICK\_SHARED](#USERS_MESSAGES_NEWSFEEDCARD_CLICK_SHARED) | ユーザーがニュースフィードカードをクリックしたとき
[USERS\_MESSAGES\_NEWSFEEDCARD\_IMPRESSION\_SHARED](#USERS_MESSAGES_NEWSFEEDCARD_IMPRESSION_SHARED) | ユーザーがニュースフィードカードを閲覧したとき
[USERS\_MESSAGES\_PUSHNOTIFICATION\_ABORT\_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_ABORT_SHARED) | 当初予定されていたプッシュ通知メッセージが何らかの理由で中止されたとき
[USERS\_MESSAGES\_PUSHNOTIFICATION\_BOUNCE\_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_BOUNCE_SHARED) | プッシュ通知がバウンスしたとき
[USERS\_MESSAGES\_PUSHNOTIFICATION\_INFLUENCEDOPEN\_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_INFLUENCEDOPEN_SHARED) | ユーザーが通知を受信した後、通知をクリックせずにアプリを開いたとき
[USERS\_MESSAGES\_PUSHNOTIFICATION\_IOSFOREGROUND\_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_IOSFOREGROUND_SHARED) | アプリを開く際にプッシュ通知を受信したとき
[USERS\_MESSAGES\_PUSHNOTIFICATION\_OPEN\_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_OPEN_SHARED) | ユーザーがプッシュ通知を開いたとき、またはプッシュ通知ボタン (アプリを開かない [閉じる] ボタンを含む) をクリックしたとき。<br><br> プッシュボタンの操作には複数の結果があります。「No」、「Decline」、「Cancel」アクションは 「クリック数」、Accept アクションは「開封数」です。このテーブルではどちらも表現されていますが、**BUTTON\_ACTION\_TYPE** 列で区別できます。たとえば、「No」、「Decline」、「Cancel」でない`BUTTON_ACTION_TYPE`でグループ化するためにクエリを使用できます。
[USERS\_MESSAGES\_PUSHNOTIFICATION\_SEND\_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_SEND_SHARED) | ユーザーにプッシュ通知を送るとき
[USERS\_MESSAGES\_SMS\_ABORT\_SHARED](#USERS_MESSAGES_SMS_ABORT_SHARED) | 当初予定されていた SMS メッセージが何らかの理由で中止されたとき。
[USERS\_MESSAGES\_SMS\_CARRIERSEND\_SHARED](#USERS_MESSAGES_SMS_CARRIERSEND_SHARED) | SMS メッセージが通信業者に送信されたとき
[USERS\_MESSAGES\_SMS\_DELIVERY\_SHARED](#USERS_MESSAGES_SMS_DELIVERY_SHARED) | SMS メッセージが配信されたとき
[USERS\_MESSAGES\_SMS\_DELIVERYFAILURE\_SHARED](#USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED) | Braze が SMS サービスプロバイダーに SMS メッセージを配信できなかったとき
[USERS\_MESSAGES\_SMS\_INBOUNDRECEIVE\_SHARED](#USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED) | ユーザーから SMS メッセージを受信したとき
[USERS\_MESSAGES\_SMS\_REJECTION\_SHARED](#USERS_MESSAGES_SMS_REJECTION_SHARED) | SMSメッセージがユーザーに届かなかった場合
[USERS\_MESSAGES\_SMS\_SEND\_SHARED](#USERS_MESSAGES_SMS_SEND_SHARED) | SMS メッセージが送信されたとき
[USERS\_MESSAGES\_SMS\_SHORTLINKCLICK\_SHARED](#USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED) | SMS メッセージに含まれる Braze 短縮 URL をクリックしたとき
[USERS\_MESSAGES\_WEBHOOK\_ABORT\_SHARED](#USERS_MESSAGES_WEBHOOK_ABORT_SHARED) | 当初スケジュールされていた Webhook メッセージが何らかの理由で中止されたとき。
[USERS\_MESSAGES\_WEBHOOK\_SEND\_SHARED](#USERS_MESSAGES_WEBHOOK_SEND_SHARED) | ユーザーの Webhook を送信するとき
[USERS\_RANDOMBUCKETNUMBERUPDATE\_SHARED](#USERS_RANDOMBUCKETNUMBERUPDATE_SHARED) | ユーザーのランダムバケット番号が変更されたとき
[USERS\_USERDELETEREQUEST\_SHARED](#USERS_USERDELETEREQUEST_SHARED) | 顧客からのリクエストによりユーザーを削除したとき
[USERS\_USERORPHAN\_SHARED](#USERS_USERORPHAN_SHARED) | ユーザーが他のユーザーのプロファイルとマージされ、元のプロファイルが孤立したとき


## 行動

### USERS\_BEHAVIORS\_CUSTOMEVENT\_SHARED {#USERS_BEHAVIORS_CUSTOMEVENT_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | イベントを実行したユーザーの Braze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
`app_group_api_id` | `null,` `string` | このユーザーが属するワークスペースの API ID
`app_api_id` | `null,` `string` | このアクションが発生したアプリの API ID
`time` | `int` | ユーザーがイベントを実行した Unix タイムスタンプ
`gender` | `null,` `string` | [PII] ユーザーの性別
`country` | `null,` `string` | [PII] ユーザーの国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
`device_id` | `null,` `string` | カスタムイベントが発生したデバイスの ID
`sdk_version` | `null,` `string` | イベント中に使用された Braze SDK のバージョン
`platform` | `null,` `string` | デバイスのプラットフォーム
`os_version` | `null,` `string` | デバイスのオペレーティングシステムのバージョン
`device_model` | `null,` `string` | デバイスのモデル
`name` | `string` | カスタムイベントの名前
`properties` | `string` | JSON エンコードされた文字列として保存されたイベントのカスタムプロパティ
`ad_id` | `null,` `string` | [PII] 広告識別子
`ad_id_type` | `null,` `string` | `ios_idfa`、`google_ad_id`、`windows_ad_id`、または `roku_ad_id` のいずれか
`ad_tracking_enabled` | `null, boolean` | デバイスの広告追跡が有効かどうか
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS\_BEHAVIORS\_INSTALLATTRIBUTION\_SHARED {#USERS_BEHAVIORS_INSTALLATTRIBUTION_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | インストールしたユーザーの Braze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
`device_id` | `null,` `string` | `device_id`、ユーザーが匿名の場合、このユーザーに関連付けられる
`app_group_api_id` | `null,` `string` | このユーザーが属するワークスペースの API ID
`time` |`int` | ユーザーがインストールした Unix タイムスタンプ
`source` |`string` | アトリビューション元
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS\_BEHAVIORS\_LOCATION\_SHARED {#USERS_BEHAVIORS_LOCATION_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` |`string` | 位置情報を記録したユーザーの Braze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
`app_group_api_id` | `null,` `string` | このユーザーが属するワークスペースの API ID
`app_api_id` | `null,` `string` | この位置情報が記録されたアプリの API ID
`time` | `int` | 位置情報が記録された Unix タイムスタンプ
`latitude` | `float` | [PII] 記録された位置の緯度
`longitude` | `float` | [PII] 記録された位置の経度
`altitude` | `null, float` | [PII] 記録された位置の高度
`ll_accuracy` | `null, float` | 記録された位置の緯度経度の精度
`alt_accuracy` | `null, float` | 記録された位置の高度の精度
`device_id` |`null,` `string` | 位置情報が記録されたデバイスの ID
`sdk_version` |`null,` `string` | 位置情報が記録されたときに使用されていた Braze SDK のバージョン
`platform` | `null,` `string` | デバイスのプラットフォーム
`os_version` | `null,` `string` | デバイスのオペレーティングシステムのバージョン
`device_model` | `null,` `string` | デバイスのモデル
`ad_id` | `null,` `string` | [PII] 広告識別子
`ad_id_type` | `null,` `string` | `ios_idfa`、`google_ad_id`、`windows_ad_id`、または `roku_ad_id` のいずれか
`ad_tracking_enabled` | `null, boolean` | デバイスの広告追跡が有効かどうか
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS\_BEHAVIORS\_PURCHASE\_SHARED {#USERS_BEHAVIORS_PURCHASE_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | 購入したユーザーの Braze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
`app_group_api_id` | `null,` `string` | このユーザーが属するワークスペースの API ID
`app_api_id` | `null,` `string` | 購入が発生したアプリの API ID
`time` | `int` | ユーザーが購入した Unix タイムスタンプ
`device_id` | `null,` `string` | 購入した端末の ID
`sdk_version` | `null,` `string` | 購入時に使用していた Braze SDK のバージョン
`platform` | `null,` `string` | デバイスのプラットフォーム
`os_version` | `null,` `string` | デバイスのオペレーティングシステムのバージョン
`device_model` | `null,` `string` | デバイスのモデル
`product_id` | `string` | 購入した製品の ID
`price` | `float` | 購入価格
`currency` | `string` | 購入通貨
`properties` | `string` | JSON エンコードされた文字列として保存された購入のカスタムプロパティ
`ad_id` | `null,` `string` | [PII] 広告識別子
`ad_id_type` | `null,` `string` | `ios_idfa`、`google_ad_id`、`windows_ad_id`、または `roku_ad_id` のいずれか
`ad_tracking_enabled` | `null, boolean` | デバイスの広告追跡が有効かどうか
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS\_BEHAVIORS\_UNINSTALL\_SHARED {#USERS_BEHAVIORS_UNINSTALL_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | アンインストールしたユーザーの Braze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
`device_id` | `null,` `string` | `device_id`、ユーザーが匿名の場合、このユーザーに関連付けられる
`app_group_api_id` | `null,` `string` | このユーザーが属するワークスペースの API ID
`app_api_id` |`null,` `string` | アンインストールされたアプリの API ID
`time` |`int` | ユーザーがアンインストールした Unix タイムスタンプ
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS\_BEHAVIORS\_UPGRADEDAPP\_SHARED {#USERS_BEHAVIORS_UPGRADEDAPP_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | アプリをアップグレードしたユーザーの Braze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
`app_group_api_id` | `null,` `string` | このユーザーが属するワークスペースの API ID
`app_api_id` | `null,` `string` | ユーザーがアップグレードしたアプリの API ID
`time` | `int` | ユーザーがアプリをアップグレードした Unix タイムスタンプ
`device_id` | `null,` `string` | ユーザーがアプリをアップグレードしたデバイスの ID
`sdk_version` | `null,` `string` | 使用している Braze SDK のバージョン
`platform` | `null,` `string` | デバイスのプラットフォーム
`os_version` | `null,` `string` | デバイスのオペレーティングシステムのバージョン
`device_model` | `null,` `string` | デバイスのモデル
`old_app_version` | `null,` `string` | アプリの古いバージョン
`new_app_version` | `null,` `string` | アプリの新しいバージョン
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS\_BEHAVIORS\_APP\_FIRSTSESSION\_SHARED {#USERS_BEHAVIORS_APP_FIRSTSESSION_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このアクションを実行するユーザーの Braze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
`app_group_api_id` | `null,` `string` | このユーザーが属するワークスペースの API ID
`app_api_id` | `null,` `string` | このセッションが発生したアプリの API ID
`time` | `int` | セッションが開始された Unix タイムスタンプ
`session_id` | `string` | セッションの UUID
`gender` | `null,` `string` | [PII] ユーザーの性別
`country` | `null,` `string` | [PII] ユーザーの国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
`device_id` | `null,` `string` | セッションが発生したデバイスの ID
`sdk_version` | `null,` `string` | セッション中に使用している Braze SDK のバージョン
`platform` | `null,` `string` | デバイスのプラットフォーム
`os_version` | `null,` `string` | デバイスのオペレーティングシステムのバージョン
`device_model` | `null,` `string` | デバイスのモデル
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS\_BEHAVIORS\_APP\_NEWSFEEDIMPRESSION\_SHARED {#USERS_BEHAVIORS_APP_NEWSFEEDIMPRESSION_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | ニュースフィードを閲覧したユーザーの Braze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
`app_group_api_id` | `null,` `string` | このユーザーが属するワークスペースの API ID
`app_api_id` | `null,` `string` | ユーザーがニュースフィードを閲覧したアプリの API ID
`time` | `int` | ユーザーがニュースフィードを閲覧した Unix タイムスタンプ
`device_id` | `null,` `string` | インプレッションが発生したデバイスの ID
`sdk_version` | `null,` `string` | インプレッション中に使用された Braze SDK のバージョン
`platform` | `null,` `string` | デバイスのプラットフォーム
`os_version` | `null,` `string` | デバイスのオペレーティングシステムのバージョン
`device_model` | `null,` `string` | デバイスのモデル
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS\_BEHAVIORS\_APP\_SESSIONEND\_SHARED {#USERS_BEHAVIORS_APP_SESSIONEND_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このアクションを実行するユーザーの Braze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
`app_group_api_id` | `null,` `string` | このユーザーが属するワークスペースの API ID
`app_api_id` | `null,` `string` | このセッションが発生したアプリの API ID
`time` | `int` | セッションが終了した Unix タイムスタンプ
`duration` |`null, float` | セッション期間
`session_id` | `string` | セッションの UUID
`device_id` | `null,` `string` | セッションが発生したデバイスの ID
`sdk_version` | `null,` `string` | セッション中に使用している Braze SDK のバージョン
`platform` | `null,` `string` | デバイスのプラットフォーム
`os_version` | `null,` `string` | デバイスのオペレーティングシステムのバージョン
`device_model` | `null,` `string` | デバイスのモデル
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS\_BEHAVIORS\_APP\_SESSIONSTART\_SHARED {#USERS_BEHAVIORS_APP_SESSIONSTART_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このアクションを実行するユーザーの Braze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
`app_api_id` | `null,` `string` | このセッションが発生したアプリの API ID
`app_group_api_id` | `null,` `string` | このユーザーが属するワークスペースの API ID
`time` | `int` | セッションが開始された Unix タイムスタンプ
`session_id` | `string` | セッションの UUID
`device_id` | `null,` `string` | セッションが発生したデバイスの ID
`sdk_version` | `null,` `string` | セッション中に使用している Braze SDK のバージョン
`platform` | `null,` `string` | デバイスのプラットフォーム
`os_version` | `null,` `string` | デバイスのオペレーティングシステムのバージョン
`device_model` | `null,` `string` | デバイスのモデル
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS\_BEHAVIORS\_GEOFENCE\_DATAEVENT\_SHARED {#USERS_BEHAVIORS_GEOFENCE_DATAEVENT_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | イベントを実行したユーザーの Braze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
`app_group_api_id` | `null,` `string` | このユーザーが属するワークスペースの API ID
`app_api_id` | `null,` `string` | このアクションが発生したアプリの API ID
`time` | `int` | ユーザーがイベントを実行した Unix タイムスタンプ
`device_id` | `null,` `string` | カスタムイベントが発生したデバイスの ID
`sdk_version` | `null,` `string` | イベント中に使用された Braze SDK のバージョン
`platform` | `null,` `string` | デバイスのプラットフォーム
`os_version` | `null,` `string` | デバイスのオペレーティングシステムのバージョン
`device_model` | `null,` `string` | デバイスのモデル
`event_type` | `string` | トリガーされたジオフェンスイベントの種類。(例: 「入る」または「出る」)。
`location_set_id` | `string` | トリガーされたジオフェンスの位置情報セットの ID
`geofence_id` | `string` | トリガーされたジオフェンスの ID
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS\_BEHAVIORS\_GEOFENCE\_RECORDEVENT\_SHARED {#USERS_BEHAVIORS_GEOFENCE_RECORDEVENT_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | イベントを実行したユーザーの Braze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
`app_group_api_id` | `null,` `string` | このユーザーが属するワークスペースの API ID
`app_api_id` | `null,` `string` | このアクションが発生したアプリの API ID
`time` | `int` | ユーザーがイベントを実行した Unix タイムスタンプ
`device_id` | `null,` `string` | カスタムイベントが発生したデバイスの ID
`sdk_version` | `null,` `string` | イベント中に使用された Braze SDK のバージョン
`platform` | `null,` `string` | デバイスのプラットフォーム
`os_version` | `null,` `string` | デバイスのオペレーティングシステムのバージョン
`device_model` | `null,` `string` | デバイスのモデル
`event_type` | `string` | トリガーされたジオフェンスイベントの種類。(例: 「入る」または「出る」)。
`location_set_id` | `string` | トリガーされたジオフェンスの位置情報セットの ID
`geofence_id` | `string` | トリガーされたジオフェンスの ID
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS\_BEHAVIORS\_SUBSCRIPTION\_GLOBALSTATECHANGE\_SHARED {#USERS_BEHAVIORS_SUBSCRIPTION_GLOBALSTATECHANGE_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | 影響を受けたユーザーの Braze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
`email_address` | `null,` `string` | [PII] ユーザーのメールアドレス
`state_change_source` | `null,` `string` | 状態変化のソース (REST、SDK、ダッシュボードなど)
`subscription_status` | `string` | サブスクリプションステータス:「配信登録済み」または「配信停止済み」
`channel` | `null,` `string` | メールのようなグローバルサブスクリプション状態のチャネル
`time` | `int` | サブスクリプションの状態が変更された Unix タイムスタンプ
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`app_group_api_id` | `null,` `string` | このユーザーが属するワークスペースの API ID
`app_api_id` | `null,` `string` | イベントが属するアプリの API ID
`campaign_id` | `null,` `string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,` `string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,` `string` | このイベントが属するメッセージバリエーションの API ID
`canvas_id` | `null,` `string` | このイベントが属するキャンバスの内部使用 Braze ID
`canvas_api_id` | `null,` `string` | このイベントが属するキャンバスの API ID
`canvas_variation_api_id` | `null,` `string` | このイベントが属するキャンバスバリエーションの API ID
`canvas_step_api_id` | `null,` `string` | このイベントが属するキャンバスステップの API ID
`send_id` | `null,` `string` | このサブスクリプション状態変更アクションの発信元となったメッセージ送信 ID
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS\_BEHAVIORS\_SUBSCRIPTIONGROUP\_STATECHANGE\_SHARED {#USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | 影響を受けたユーザーの Braze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
`device_id` | `null,` `string` | `device_id`、ユーザーが匿名の場合、このユーザーに関連付けられる
`app_group_api_id` | `null,` `string` | このユーザーが属するワークスペースの API ID
`email_address` | `null,` `string` | [PII] ユーザーのメールアドレス
`phone_number` | `null,` `string` | [PII] e164 形式のユーザーの電話番号
`app_api_id` | `null,` `string` | イベントが属するアプリの API ID
`campaign_id` | `null,` `string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,` `string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,` `string` | このイベントが属するメッセージバリエーションの API ID
`canvas_id` | `null,` `string` | このイベントが属するキャンバスの内部使用 Braze ID
`canvas_api_id` | `null,` `string` | このイベントが属するキャンバスの API ID
`canvas_variation_api_id` | `null,` `string` | このイベントが属するキャンバスバリエーションの API ID
`canvas_step_api_id` | `null,` `string` | このイベントが属するキャンバスステップの API ID
`subscription_group_api_id` | `string` | サブスクリプショングループの API ID
`channel` | `null,` `string` | チャネル: サブスクリプショングループのチャネルタイプに応じて 'email' または 'sms'
`subscription_status` | `string` | サブスクリプションステータス:「配信登録済み」または「配信停止済み」
`time` | `int` | サブスクリプションの状態が変更された Unix タイムスタンプ
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`send_id` | `null,` `string` | このサブスクリプション状態変更アクションの発信元となったメッセージ送信 ID
`state_change_source` | `null,` `string` | 状態変化のソース (REST、SDK、ダッシュボードなど)
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## キャンペーン

### USERS\_CAMPAIGNS\_ABORT\_SHARED {#USERS_CAMPAIGNS_ABORT_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` |`string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
`device_id` | `null,` `string` | `device_id`、ユーザーが匿名の場合、このユーザーに関連付けられる
`app_group_api_id` | `null,` `string` | このユーザーが属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`dispatch_id` | `null,` `string` | このメッセージが属するディスパッチの ID
`send_id` | `null,` `string` | このメッセージが属するメッセージ送信 ID
`campaign_id` |`string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,` `string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,` `string` | このユーザーが受け取ったメッセージバリエーションの API ID
`channel` | `null,` `string` | このイベントが属するチャネル
`gender` | `null,` `string` | [PII] ユーザーの性別
`country` | `null,` `string` | [PII] ユーザーの国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
`abort_type` | `null,` `string` | 中止のタイプ。`liquid_abort_message`、`quiet_hours`、`rate_limit` のいずれか
`abort_log` | `null,` `string` | [PII] 中止の詳細を記述するログメッセージ (最大 128 文字)
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS\_CAMPAIGNS\_CONVERSION\_SHARED {#USERS_CAMPAIGNS_CONVERSION_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` |`string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
`device_id` | `null,` `string` | `device_id`、ユーザーが匿名の場合、このユーザーに関連付けられる
`app_group_api_id` | `null,` `string` | このユーザーが属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`app_api_id` | `null,` `string` | このイベントが発生したアプリの API ID
`dispatch_id` | `null,` `string` | このメッセージが属するディスパッチの ID
`send_id` | `null,` `string` | このメッセージが属するメッセージ送信 ID
`campaign_id` |`string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,` `string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,` `string` | このユーザーが受け取ったメッセージバリエーションの API ID
`conversion_behavior_index` | `null, int` | 変換動作のインデックス
`gender` | `null,` `string` | [PII] ユーザーの性別
`country` | `null,` `string` | [PII] ユーザーの国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS\_CAMPAIGNS\_ENROLLINCONTROL\_SHARED {#USERS_CAMPAIGNS_ENROLLINCONTROL_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` |`string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
`device_id` | `null,` `string` | `device_id`、ユーザーが匿名の場合、このユーザーに関連付けられる
`app_group_api_id` | `null,` `string` | このユーザーが属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`app_api_id` | `null,` `string` | このイベントが発生したアプリの API ID
`dispatch_id` | `null,` `string` | このメッセージが属するディスパッチの ID
`send_id` | `null,` `string` | このメッセージが属するメッセージ送信 ID
`campaign_id` |`string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,` `string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,` `string` | このユーザーが受け取ったメッセージバリエーションの API ID
`gender` | `null,` `string` | [PII] ユーザーの性別
`country` | `null,` `string` | [PII] ユーザーの国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS\_CAMPAIGNS\_FREQUENCYCAP\_SHARED {#USERS_CAMPAIGNS_FREQUENCYCAP_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` |`string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
`device_id` | `null,` `string` | `device_id`、ユーザーが匿名の場合、このユーザーに関連付けられる
`app_group_api_id` | `null,` `string` | このユーザーが属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`dispatch_id` | `null,` `string` | このメッセージが属するディスパッチの ID
`send_id` | `null,` `string` | このメッセージが属するメッセージ送信 ID
`campaign_id` |`string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,` `string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,` `string` | このユーザーが受け取ったメッセージバリエーションの API ID
`channel` | `null,` `string` | このイベントが属するチャネル
`gender` | `null,` `string` | [PII] ユーザーの性別
`country` | `null,` `string` | [PII] ユーザーの国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS\_CAMPAIGNS\_REVENUE\_SHARED {#USERS_CAMPAIGNS_REVENUE_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` |`string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
`device_id` | `null,` `string` | `device_id`、ユーザーが匿名の場合、このユーザーに関連付けられる
`app_group_api_id` | `null,` `string` | このユーザーが属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`app_api_id` | `null,` `string` | このイベントが発生したアプリの API ID
`dispatch_id` | `null,` `string` | このメッセージが属するディスパッチの ID
`send_id` | `null,` `string` | このメッセージが属するメッセージ送信 ID
`campaign_id` |`string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,` `string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,` `string` | このユーザーが受け取ったメッセージバリエーションの API ID
`gender` | `null,` `string` | [PII] ユーザーの性別
`country` | `null,` `string` | [PII] ユーザーの国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
`revenue` | `long` | 発生したセント単位の米ドル収益額
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## キャンバス

### USERS\_CANVAS\_ABORT\_SHARED {#USERS_CANVAS_ABORT_SHARED}

| フィールド                                  | タイプ                     | 説明                                                                |
| -------------------------------------- | ------------------------ | -------------------------------------------------------------------------- |
| `id`                                   | `string`、`null`    | このイベントのグローバルな一意の ID                                          |
| `user_id`                              | `string`、`null`    | このイベントを実行したユーザーの Braze ID                              |
| `external_user_id`                     | `string`、`null`    | [PII] ユーザーの外部ユーザー ID                                         |
| `device_id`                            | `string`、`null`    | 匿名の場合、このユーザーに関連付けられているデバイスの ID       |
| `app_group_id`                         | `string`、`null`    | このユーザーが属するワークスペースの Braze ID                              |
| `app_group_api_id`                     | `string`、`null`    | このユーザーが属するワークスペースの API ID                               |
| `time`                                 | `int`、`null`       | イベントが発生した Unix タイムスタンプ                                 |
| `canvas_id`                            | `string`、`null`    | (Braze の使用のみ) キャンバスのID                |
| `canvas_api_id`                        | `string`、`null`    | このイベントが属するキャンバスの API ID                                 |
| `canvas_variation_api_id`              | `string`、`null`    | このイベントが属するキャンバスバリエーションの API ID                       |
| `canvas_step_api_id`                   | `string`、`null`    | このイベントが属するキャンバスステップの API ID                            |
| `canvas_step_message_variation_api_id` | `string`、`null`    | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID             |
| `channel`                              | `string`、`null`    | このイベントが属するメッセージングチャネル (メール、プッシュ通知など)                |
| `gender`                               | `string`、`null`    | [PII] ユーザーの性別                                                   |
| `country`                              | `string`、`null`    | [PII] ユーザーの国                                                 |
| `timezone`                             | `string`、`null`    | ユーザーのタイムゾーン                                                       |
| `language`                             | `string`、`null`    | [PII] ユーザーの言語                                                 |
| `abort_type`                           | `string`、`null`    | 中止のタイプ。"liquid_abort_message"、"quiet_hours"、"rate_limit"のいずれか |
| `abort_log`                            | `string`、`null`    | [PII] 中止の詳細を記述するログメッセージ (最大 128 文字)         |
| `sf_created_at`                        | `timestamp`、`null` | このイベントが Snowpipe に検出されたとき                              |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS\_CANVAS\_CONVERSION\_SHARED {#USERS_CANVAS_CONVERSION_SHARED}

| フィールド                                  | タイプ                     | 説明                                                                                                     |
| -------------------------------------- | ------------------------ | --------------------------------------------------------------------------------------------------------------- |
| `id`                                   | `string`、`null`    | このイベントのグローバルな一意の ID                                                                               |
| `user_id`                              | `string`、`null`    | このイベントを実行したユーザーの Braze ID                                                                   |
| `external_user_id`                     | `string`、`null`    | [PII] ユーザーの外部ユーザー ID                                                                              |
| `device_id`                            | `string`、`null`    | 匿名の場合、このユーザーに関連付けられているデバイスの ID                                            |
| `app_group_id`                         | `string`、`null`    | このユーザーが属するワークスペースの Braze ID                                                                   |
| `app_group_api_id`                     | `string`、`null`    | このユーザーが属するワークスペースの API ID                                                                    |
| `time`                                 | `int`、`null`       | イベントが発生した Unix タイムスタンプ                                                                      |
| `app_api_id`                           | `string`、`null`    | このイベントが発生したアプリの API ID                                                                  |
| `canvas_id`                            | `string`、`null`    | (Braze の使用のみ) キャンバスのID                                                     |
| `canvas_api_id`                        | `string`、`null`    | このイベントが属するキャンバスの API ID                                                                      |
| `canvas_variation_api_id`              | `string`、`null`    | このイベントが属するキャンバスバリエーションの API ID                                                            |
| `canvas_step_api_id`                   | `string`、`null`    | このイベントが属するキャンバスステップの API ID                                                                 |
| `canvas_step_message_variation_api_id` | `string`、`null`    | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID                                                  |
| `conversion_behavior_index`            | `int`、`null`       | ユーザーが行ったコンバージョンイベントのタイプ。"0"は 1 次コンバージョン、"1"は 2 次コンバージョン |
| `gender`                               | `string`、`null`    | [PII] ユーザーの性別                                                                                        |
| `country`                              | `string`、`null`    | [PII] ユーザーの国                                                                                       |
| `timezone`                             | `string`、`null`    | ユーザーのタイムゾーン                                                                                             |
| `language`                             | `string`、`null`    | [PII] ユーザーの言語                                                                                      |
| `sf_created_at`                        | `timestamp`、`null` | このイベントが Snowpipe に検出されたとき                                                                   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS\_CANVAS\_ENTRY\_SHARED {#USERS_CANVAS_ENTRY_SHARED}

| フィールド                     | タイプ                     | 説明                                                          |
| ------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                      | `string`、`null`    | このイベントのグローバルな一意の ID                                    |
| `user_id`                 | `string`、`null`    | このイベントを実行したユーザーの Braze ID                        |
| `external_user_id`        | `string`、`null`    | [PII] ユーザーの外部ユーザー ID                                   |
| `device_id`               | `string`、`null`    | 匿名の場合、このユーザーに関連付けられているデバイスの ID |
| `app_group_id`            | `string`、`null`    | このユーザーが属するワークスペースの Braze ID                        |
| `app_group_api_id`        | `string`、`null`    | このユーザーが属するワークスペースの API ID                         |
| `time`                    | `int`、`null`       | イベントが発生した Unix タイムスタンプ                           |
| `canvas_id`               | `string`、`null`    | (Braze の使用のみ) キャンバスのID          |
| `canvas_api_id`           | `string`、`null`    | このイベントが属するキャンバスの API ID                           |
| `canvas_variation_api_id` | `string`、`null`    | このイベントが属するキャンバスバリエーションの API ID                 |
| `canvas_step_api_id`      | `string`、`null`    | [非推奨] このイベントが属するキャンバスステップの API ID         |
| `gender`                  | `string`、`null`    | [PII] ユーザーの性別                                             |
| `country`                 | `string`、`null`    | [PII] ユーザーの国                                            |
| `timezone`                | `string`、`null`    | ユーザーのタイムゾーン                                                  |
| `language`                | `string`、`null`    | [PII] ユーザーの言語                                           |
| `in_control_group`        | `boolean`、`null`   | ユーザーがコントロールグループに登録されている場合は真                   |
| `sf_created_at`           | `timestamp`、`null` | このイベントが Snowpipe に検出されたとき                        |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS\_CANVAS\_EXIT\_MATCHEDAUDIENCE\_SHARED {#USERS_CANVAS_EXIT_MATCHEDAUDIENCE_SHARED}

| フィールド                     | タイプ                     | 説明                                                          |
| ------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                      | `string`、`null`    | このイベントのグローバルな一意の ID                                    |
| `user_id`                 | `string`、`null`    | このイベントを実行したユーザーの Braze ID                        |
| `external_user_id`        | `string`、`null`    | [PII] ユーザーの外部ユーザー ID                                   |
| `device_id`               | `string`、`null`    | 匿名の場合、このユーザーに関連付けられているデバイスの ID |
| `app_group_id`            | `string`、`null`    | このユーザーが属するワークスペースの Braze ID                        |
| `app_group_api_id`        | `string`、`null`    | このユーザーが属するワークスペースの API ID                         |
| `time`                    | `int`、`null`       | イベントが発生した Unix タイムスタンプ                           |
| `canvas_id`               | `string`、`null`    | (Braze の使用のみ) キャンバスのID          |
| `canvas_api_id`           | `string`、`null`    | このイベントが属するキャンバスの API ID                           |
| `canvas_variation_api_id` | `string`、`null`    | このイベントが属するキャンバスバリエーションの API ID                 |
| `canvas_step_api_id`      | `string`、`null`    | このイベントが属するキャンバスステップの API ID                      |
| `sf_created_at`           | `timestamp`、`null` | このイベントが Snowpipe に検出されたとき                        |

{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS\_CANVAS\_EXIT\_PERFORMEDEVENT\_SHARED {#USERS_CANVAS_EXIT_PERFORMEDEVENT_SHARED}

| フィールド                     | タイプ                     | 説明                                                          |
| ------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                      | `string`、`null`    | このイベントのグローバルな一意の ID                                    |
| `user_id`                 | `string`、`null`    | このイベントを実行したユーザーの Braze ID                        |
| `external_user_id`        | `string`、`null`    | [PII] ユーザーの外部ユーザー ID                                   |
| `device_id`               | `string`、`null`    | 匿名の場合、このユーザーに関連付けられているデバイスの ID |
| `app_group_id`            | `string`、`null`    | このユーザーが属するワークスペースの Braze ID                        |
| `app_group_api_id`        | `string`、`null`    | このユーザーが属するワークスペースの API ID                         |
| `time`                    | `int`、`null`       | イベントが発生した Unix タイムスタンプ                           |
| `canvas_id`               | `string`、`null`    | (Braze の使用のみ) キャンバスのID          |
| `canvas_api_id`           | `string`、`null`    | このイベントが属するキャンバスの API ID                           |
| `canvas_variation_api_id` | `string`、`null`    | このイベントが属するキャンバスバリエーションの API ID                 |
| `canvas_step_api_id`      | `string`、`null`    | このイベントが属するキャンバスステップの API ID                      |
| `sf_created_at`           | `timestamp`、`null` | このイベントが Snowpipe に検出されたとき                        |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS\_CANVAS\_EXPERIMENTSTEP\_CONVERSION\_SHARED {#USERS_CANVAS_EXPERIMENTSTEP_CONVERSION_SHARED}

| フィールド                       | タイプ                     | 説明                                                                                                     |
| --------------------------- | ------------------------ | --------------------------------------------------------------------------------------------------------------- |
| `id`                        | `string`、`null`    | のイベントのグローバルな一意の ID                                                                               |
| `user_id`                   | `string`、`null`    | このイベントを実行したユーザーの Braze ID                                                                   |
| `external_user_id`          | `string`、`null`    | [PII] ユーザーの外部ユーザー ID                                                                              |
| `device_id`                 | `string`、`null`    | 匿名の場合、このユーザーに関連付けられているデバイスの ID                                            |
| `app_group_id`              | `string`、`null`    | このユーザーが属するワークスペースの Braze ID                                                                   |
| `time`                      | `int`、`null`       | イベントが発生した Unix タイムスタンプ                                                                      |
| `app_api_id`                | `string`、`null`    | このイベントが発生したアプリの API ID                                                                  |
| `canvas_id`                 | `string`、`null`    | (Braze の使用のみ) キャンバスのID                                                     |
| `canvas_api_id`             | `string`、`null`    | このイベントが属するキャンバスの API ID                                                                      |
| `canvas_variation_api_id`   | `string`、`null`    | このイベントが属するキャンバスバリエーションの API ID                                                            |
| `canvas_step_api_id`        | `string`、`null`    | このイベントが属するキャンバスステップの API ID                                                                 |
| `experiment_step_api_id`    | `string`、`null`    | このイベントが属する実験ステップの API ID                                                             |
| `conversion_behavior_index` | `int`、`null`       | ユーザーが行ったコンバージョンイベントのタイプ。"0"は 1 次コンバージョン、"1"は 2 次コンバージョン |
| `sf_created_at`             | `timestamp`、`null` | このイベントが Snowpipe に検出されたとき                                                                   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS\_CANVAS\_EXPERIMENTSTEP\_SPLITENTRY\_SHARED {#USERS_CANVAS_EXPERIMENTSTEP_SPLITENTRY_SHARED}

| フィールド                     | タイプ                     | 説明                                                          |
| ------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                      | `string`、`null`    | このイベントのグローバルな一意の ID                                    |
| `user_id`                 | `string`、`null`    | このイベントを実行したユーザーの Braze ID                        |
| `external_user_id`        | `string`、`null`    | [PII] ユーザーの外部ユーザー ID                                   |
| `device_id`               | `string`、`null`    | 匿名の場合、このユーザーに関連付けられているデバイスの ID |
| `app_group_id`            | `string`、`null`    | このユーザーが属するワークスペースの Braze ID                        |
| `time`                    | `int`、`null`       | イベントが発生した Unix タイムスタンプ                           |
| `canvas_id`               | `string`、`null`    | (Braze の使用のみ) キャンバスのID          |
| `canvas_api_id`           | `string`、`null`    | このイベントが属するキャンバスの API ID                           |
| `canvas_variation_api_id` | `string`、`null`    | このイベントが属するキャンバスバリエーションの API ID                 |
| `canvas_step_api_id`      | `string`、`null`    | このイベントが属するキャンバスステップの API ID                      |
| `experiment_step_api_id`  | `string`、`null`    | このイベントが属する実験ステップの API ID                  |
| `in_control_group`        | `boolean`、`null`   | ユーザーがコントロールグループに登録されている場合は真                   |
| `sf_created_at`           | `timestamp`、`null` | このイベントが Snowpipe に検出されたとき                        |

{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS\_CANVAS\_FREQUENCYCAP\_SHARED {#USERS_CANVAS_FREQUENCYCAP_SHARED}

| フィールド                                  | タイプ                     | 説明                                                          |
| -------------------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                                   | `string`、`null`    | このイベントのグローバルな一意の ID                                    |
| `user_id`                              | `string`、`null`    | このイベントを実行したユーザーの Braze ID                        |
| `external_user_id`                     | `string`、`null`    | [PII] ユーザーの外部ユーザー ID                                   |
| `device_id`                            | `string`、`null`    | 匿名の場合、このユーザーに関連付けられているデバイスの ID |
| `app_group_id`                         | `string`、`null`    | このユーザーが属するワークスペースの Braze ID                        |
| `app_group_api_id`                     | `string`、`null`    | このユーザーが属するワークスペースの API ID                         |
| `time`                                 | `int`、`null`       | イベントが発生した Unix タイムスタンプ                           |
| `canvas_id`                            | `string`、`null`    | (Braze の使用のみ) キャンバスのID          |
| `canvas_api_id`                        | `string`、`null`    | このイベントが属するキャンバスの API ID                           |
| `canvas_variation_api_id`              | `string`、`null`    | このイベントが属するキャンバスバリエーションの API ID                 |
| `canvas_step_api_id`                   | `string`、`null`    | このイベントが属するキャンバスステップの API ID                      |
| `canvas_step_message_variation_api_id` | `string`、`null`    | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID       |
| `channel`                              | `string`、`null`    | このイベントが属するメッセージングチャネル (メール、プッシュ通知など)          |
| `gender`                               | `string`、`null`    | [PII] ユーザーの性別                                             |
| `country`                              | `string`、`null`    | [PII] ユーザーの国                                            |
| `timezone`                             | `string`、`null`    | ユーザーのタイムゾーン                                                  |
| `language`                             | `string`、`null`    | [PII] ユーザーの言語                                           |
| `sf_created_at`                        | `timestamp`、`null` | このイベントが Snowpipe に検出されたとき                        |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS\_CANVAS\_REVENUE\_SHARED {#USERS_CANVAS_REVENUE_SHARED}

| フィールド                                  | タイプ                     | 説明                                                          |
| -------------------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                                   | `string`、`null`    | このイベントのグローバルな一意の ID                                    |
| `user_id`                              | `string`、`null`    | このイベントを実行したユーザーの Braze ID                        |
| `external_user_id`                     | `string`、`null`    | [PII] ユーザーの外部ユーザー ID                                   |
| `device_id`                            | `string`、`null`    | 匿名の場合、このユーザーに関連付けられているデバイスの ID |
| `app_group_id`                         | `string`、`null`    | このユーザーが属するワークスペースの Braze ID                        |
| `app_group_api_id`                     | `string`、`null`    | このユーザーが属するワークスペースの API ID                         |
| `time`                                 | `int`、`null`       | イベントが発生した Unix タイムスタンプ                           |
| `canvas_id`                            | `string`、`null`    | (Braze の使用のみ) キャンバスのID          |
| `canvas_api_id`                        | `string`、`null`    | このイベントが属するキャンバスの API ID                           |
| `canvas_variation_api_id`              | `string`、`null`    | このイベントが属するキャンバスバリエーションの API ID                 |
| `canvas_step_api_id`                   | `string`、`null`    | このイベントが属するキャンバスステップの API ID                      |
| `canvas_step_message_variation_api_id` | `string`、`null`    | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID       |
| `gender`                               | `string`、`null`    | [PII] ユーザーの性別                                             |
| `country`                              | `string`、`null`    | [PII] ユーザーの国                                            |
| `timezone`                             | `string`、`null`    | ユーザーのタイムゾーン                                                  |
| `language`                             | `string`、`null`    | [PII] ユーザーの言語                                           |
| `revenue`                              | `int`、`null`       | 発生した米ドル収益額、セント単位で表示               |
| `sf_created_at`                        | `timestamp`、`null` | このイベントが Snowpipe に検出されたとき                        |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## メッセージ

### USERS\_MESSAGES\_CONTENTCARD\_ABORT\_SHARED {#USERS_MESSAGES_CONTENTCARD_ABORT_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` |`string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
`device_id` | `null,` `string` | `device_id`、ユーザーが匿名の場合、このユーザーに関連付けられる
`app_group_api_id` | `null,` `string` | このユーザーが属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`dispatch_id` | `null,` `string` | このメッセージが属するディスパッチの ID
`send_id` | `null,` `string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `null,` `string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,` `string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,` `string` | このユーザーが受け取ったメッセージバリエーションの API ID
`canvas_id` | `null,` `string` | このイベントが属するキャンバスの内部使用 Braze ID
`canvas_api_id` | `null,` `string` | このイベントが属するキャンバスの API ID
`canvas_variation_api_id` | `null,` `string` | このイベントが属するキャンバスバリエーションの API ID
`canvas_step_api_id` | `null,` `string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,` `string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,` `string` | [PII] ユーザーの性別
`country` | `null,` `string` | [PII] ユーザーの国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
`abort_type` | `null,` `string` | 中止のタイプ。`liquid_abort_message`、`quiet_hours`、`rate_limit` のいずれか
`abort_log` | `null,` `string` | [PII] 中止の詳細を記述するログメッセージ (最大 128 文字)
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS\_MESSAGES\_CONTENTCARD\_CLICK\_SHARED {#USERS_MESSAGES_CONTENTCARD_CLICK_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` |`string` | このイベントを実行したユーザーの Braze ID
`content_card_id` | `string` | このイベントを発生させたカードの ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
`app_group_api_id` | `null,` `string` | このユーザーが属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`app_api_id` | `null,` `string` | このイベントが発生したアプリの API ID
`dispatch_id` | `null,` `string` | このメッセージが属するディスパッチの ID
`send_id` | `null,` `string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `null,` `string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,` `string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,` `string` | このユーザーが受け取ったメッセージバリエーションの API ID
`canvas_id` | `null,` `string` | このイベントが属するキャンバスの内部使用 Braze ID
`canvas_api_id` | `null,` `string` | このイベントが属するキャンバスの API ID
`canvas_variation_api_id` | `null,` `string` | このイベントが属するキャンバスバリエーションの API ID
`canvas_step_api_id` | `null,` `string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,` `string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,` `string` | [PII] ユーザーの性別
`country` | `null,` `string` | [PII] ユーザーの国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
`device_id` | `null,` `string` ｜イベントが発生したデバイスの ID
`sdk_version` | `null,` `string` | イベント中に使用された Braze SDK のバージョン
`platform` | `null,` `string` | デバイスのプラットフォーム
`os_version` | `null,` `string` | デバイスのオペレーティングシステムのバージョン
`device_model` | `null,` `string` | デバイスのモデル
`resolution` | `null,` `string` | デバイスの解像度
`carrier` | `null,` `string` | デバイスの通信業者
`browser` | `null,` `string` | デバイスのブラウザー
`ad_id` | `null,` `string` | [PII] 広告識別子
`ad_id_type` | `null,` `string` | `ios_idfa`、`google_ad_id`、`windows_ad_id`、または `roku_ad_id` のいずれか
`ad_tracking_enabled` | `null, boolean` | デバイスの広告追跡が有効かどうか
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS\_MESSAGES\_CONTENTCARD\_DISMISS\_SHARED {#USERS_MESSAGES_CONTENTCARD_DISMISS_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` |`string` | このイベントを実行したユーザーの Braze ID
`content_card_id` | `string` | このイベントを発生させたカードの ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
`app_group_api_id` | `null,` `string` | このユーザーが属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`app_api_id` | `null,` `string` | このイベントが発生したアプリの API ID
`dispatch_id` | `null,` `string` | このメッセージが属するディスパッチの ID
`send_id` | `null,` `string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `null,` `string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,` `string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,` `string` | このユーザーが受け取ったメッセージバリエーションの API ID
`canvas_id` | `null,` `string` | このイベントが属するキャンバスの内部使用 Braze ID
`canvas_api_id` | `null,` `string` | このイベントが属するキャンバスの API ID
`canvas_variation_api_id` | `null,` `string` | このイベントが属するキャンバスバリエーションの API ID
`canvas_step_api_id` | `null,` `string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,` `string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,` `string` | [PII] ユーザーの性別
`country` | `null,` `string` | [PII] ユーザーの国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
`device_id` | `null,` `string` ｜イベントが発生したデバイスの ID
`sdk_version` | `null,` `string` | イベント中に使用された Braze SDK のバージョン
`platform` | `null,` `string` | デバイスのプラットフォーム
`os_version` | `null,` `string` | デバイスのオペレーティングシステムのバージョン
`device_model` | `null,` `string` | デバイスのモデル
`resolution` | `null,` `string` | デバイスの解像度
`carrier` | `null,` `string` | デバイスの通信業者
`browser` | `null,` `string` | デバイスのブラウザー
`ad_id` | `null,` `string` | [PII] 広告識別子
`ad_id_type` | `null,` `string` | `ios_idfa`、`google_ad_id`、`windows_ad_id`、または `roku_ad_id` のいずれか
`ad_tracking_enabled` | `null, boolean` | デバイスの広告追跡が有効かどうか
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS\_MESSAGES\_CONTENTCARD\_IMPRESSION\_SHARED {#USERS_MESSAGES_CONTENTCARD_IMPRESSION_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` |`string` | このイベントを実行したユーザーの Braze ID
`content_card_id` | `string` | このイベントを発生させたカードの ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
`app_group_api_id` | `null,` `string` | このユーザーが属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`app_api_id` | `null,` `string` | このイベントが発生したアプリの API ID
`dispatch_id` | `null,` `string` | このメッセージが属するディスパッチの ID
`send_id` | `null,` `string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `null,` `string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,` `string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,` `string` | このユーザーが受け取ったメッセージバリエーションの API ID
`canvas_id` | `null,` `string` | このイベントが属するキャンバスの内部使用 Braze ID
`canvas_api_id` | `null,` `string` | このイベントが属するキャンバスの API ID
`canvas_variation_api_id` | `null,` `string` | このイベントが属するキャンバスバリエーションの API ID
`canvas_step_api_id` | `null,` `string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,` `string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,` `string` | [PII] ユーザーの性別
`country` | `null,` `string` | [PII] ユーザーの国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
`device_id` | `null,` `string` ｜イベントが発生したデバイスの ID
`sdk_version` | `null,` `string` | イベント中に使用された Braze SDK のバージョン
`platform` | `null,` `string` | デバイスのプラットフォーム
`os_version` | `null,` `string` | デバイスのオペレーティングシステムのバージョン
`device_model` | `null,` `string` | デバイスのモデル
`resolution` | `null,` `string` | デバイスの解像度
`carrier` | `null,` `string` | デバイスの通信業者
`browser` | `null,` `string` | デバイスのブラウザー
`ad_id` | `null,` `string` | [PII] 広告識別子
`ad_id_type` | `null,` `string` | `ios_idfa`、`google_ad_id`、`windows_ad_id`、または `roku_ad_id` のいずれか
`ad_tracking_enabled` | `null, boolean` | デバイスの広告追跡が有効かどうか
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS\_MESSAGES\_CONTENTCARD\_SEND\_SHARED {#USERS_MESSAGES_CONTENTCARD_SEND_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` |`string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
`device_id` | `null,` `string` | `device_id`、ユーザーが匿名の場合、このユーザーに関連付けられる
`app_group_api_id` | `null,` `string` | このユーザーが属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`dispatch_id` | `null,` `string` | このメッセージが属するディスパッチの ID
`send_id` | `null,` `string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `null,` `string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,` `string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,` `string` | このユーザーが受け取ったメッセージバリエーションの API ID
`canvas_id` | `null,` `string` | このイベントが属するキャンバスの内部使用 Braze ID
`canvas_api_id` | `null,` `string` | このイベントが属するキャンバスの API ID
`canvas_variation_api_id` | `null,` `string` | このイベントが属するキャンバスバリエーションの API ID
`canvas_step_api_id` | `null,` `string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,` `string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,` `string` | [PII] ユーザーの性別
`country` | `null,` `string` | [PII] ユーザーの国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
`content_card_id` | `string` | このイベントを発生させたカードの ID
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS\_MESSAGES\_EMAIL\_ABORT\_SHARED {#USERS_MESSAGES_EMAIL_ABORT_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` |`string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
`device_id` | `null,` `string` | `device_id`、ユーザーが匿名の場合、このユーザーに関連付けられる
`app_group_api_id` | `null,` `string` | このユーザーが属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`dispatch_id` | `null,` `string` | このメッセージが属するディスパッチの ID
`send_id` | `null,` `string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `null,` `string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,` `string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,` `string` | このユーザーが受け取ったメッセージバリエーションの API ID
`canvas_id` | `null,` `string` | このイベントが属するキャンバスの内部使用 Braze ID
`canvas_api_id` | `null,` `string` | このイベントが属するキャンバスの API ID
`canvas_variation_api_id` | `null,` `string` | このイベントが属するキャンバスバリエーションの API ID
`canvas_step_api_id` | `null,` `string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,` `string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,` `string` | [PII] ユーザーの性別
`country` | `null,` `string` | [PII] ユーザーの国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
`email_address` | `string` | [PII] ユーザーのメールアドレス
`ip_pool` | `null,` `string` | メール送信元の IP プール
`abort_type` | `null,` `string` | 中止のタイプ。`liquid_abort_message`、`quiet_hours`、`rate_limit` のいずれか
`abort_log` | `null,` `string` | [PII] 中止の詳細を記述するログメッセージ (最大 128 文字)
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS\_MESSAGES\_EMAIL\_BOUNCE\_SHARED {#USERS_MESSAGES_EMAIL_BOUNCE_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` |`string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
`device_id` | `null,` `string` | `device_id`、ユーザーが匿名の場合、このユーザーに関連付けられる
`app_group_api_id` | `null,` `string` | このユーザーが属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`dispatch_id` | `null,` `string` | このメッセージが属するディスパッチの ID
`send_id` | `null,` `string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `null,` `string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,` `string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,` `string` | このユーザーが受け取ったメッセージバリエーションの API ID
`canvas_id` | `null,` `string` | このイベントが属するキャンバスの内部使用 Braze ID
`canvas_api_id` | `null,` `string` | このイベントが属するキャンバスの API ID
`canvas_variation_api_id` | `null,` `string` | このイベントが属するキャンバスバリエーションの API ID
`canvas_step_api_id` | `null,` `string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,` `string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,` `string` | [PII] ユーザーの性別
`country` | `null,` `string` | [PII] ユーザーの国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
`email_address` | `string` | [PII] ユーザーのメールアドレス
`sending_ip` | `null,` `string` | メール送信元のIPアドレス
`ip_pool` | `null,` `string` | メール送信元の IP プール
`bounce_reason` | `null,` `string` | [PII] このバウンスイベントで受信した SMTP 理由コードとユーザーフレンドリーメッセージ
`esp` | `null,` `string` | イベントに関連する ESP (SparkPost または SendGrid)
`from_domain` | `null,` `string` | メール送信ドメイン
`is_drop` | `null, boolean` | このイベントがドロップイベントとしてカウントされることを示す
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS\_MESSAGES\_EMAIL\_CLICK\_SHARED {#USERS_MESSAGES_EMAIL_CLICK_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` |`string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
`device_id` | `null,` `string` | `device_id`、ユーザーが匿名の場合、このユーザーに関連付けられる
`app_group_api_id` | `null,` `string` | このユーザーが属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`dispatch_id` | `null,` `string` | このメッセージが属するディスパッチの ID
`send_id` | `null,` `string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `null,` `string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,` `string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,` `string` | このユーザーが受け取ったメッセージバリエーションの API ID
`canvas_id` | `null,` `string` | このイベントが属するキャンバスの内部使用 Braze ID
`canvas_api_id` | `null,` `string` | このイベントが属するキャンバスの API ID
`canvas_variation_api_id` | `null,` `string` | このイベントが属するキャンバスバリエーションの API ID
`canvas_step_api_id` | `null,` `string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,` `string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,` `string` | [PII] ユーザーの性別
`country` | `null,` `string` | [PII] ユーザーの国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
`email_address` | `string` | [PII] ユーザーのメールアドレス
`url` | `null,` `string` | ユーザーがクリックした URL
`user_agent` | `null,` `string` | クリックが発生したユーザーエージェント
`ip_pool` | `null,` `string` | メール送信元の IP プール
`link_id` | `null,` `string` | Braze が作成した、クリックされたリンクの一意の ID
`link_alias` | `null,` `string` | このリンク ID に関連するエイリアス
`esp` | `null,` `string` | イベントに関連する ESP (SparkPost または SendGrid)
`from_domain` | `null,` `string` | メール送信ドメイン
`is_amp` | `null, boolean` | これが AMP イベントであることを示す
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS\_MESSAGES\_EMAIL\_DELIVERY\_SHARED {#USERS_MESSAGES_EMAIL_DELIVERY_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` |`string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
`device_id` | `null,` `string` | `device_id`、ユーザーが匿名の場合、このユーザーに関連付けられる
`app_group_api_id` | `null,` `string` | このユーザーが属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`dispatch_id` | `null,` `string` | このメッセージが属するディスパッチの ID
`send_id` | `null,` `string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `null,` `string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,` `string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,` `string` | このユーザーが受け取ったメッセージバリエーションの API ID
`canvas_id` | `null,` `string` | このイベントが属するキャンバスの内部使用 Braze ID
`canvas_api_id` | `null,` `string` | このイベントが属するキャンバスの API ID
`canvas_variation_api_id` | `null,` `string` | このイベントが属するキャンバスバリエーションの API ID
`canvas_step_api_id` | `null,` `string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,` `string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,` `string` | [PII] ユーザーの性別
`country` | `null,` `string` | [PII] ユーザーの国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
`email_address` | `string` | [PII] ユーザーのメールアドレス
`sending_ip` | `null,` `string` | メール送信元のIPアドレス
`ip_pool` | `null,` `string` | メール送信元の IP プール
`esp` | `null,` `string` | イベントに関連する ESP (SparkPost または SendGrid)
`from_domain` | `null,` `string` | メール送信ドメイン
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS\_MESSAGES\_EMAIL\_MARKASSPAM\_SHARED {#USERS_MESSAGES_EMAIL_MARKASSPAM_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` |`string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
`device_id` | `null,` `string` | `device_id`、ユーザーが匿名の場合、このユーザーに関連付けられる
`app_group_api_id` | `null,` `string` | このユーザーが属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`dispatch_id` | `null,` `string` | このメッセージが属するディスパッチの ID
`send_id` | `null,` `string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `null,` `string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,` `string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,` `string` | このユーザーが受け取ったメッセージバリエーションの API ID
`canvas_id` | `null,` `string` | このイベントが属するキャンバスの内部使用 Braze ID
`canvas_api_id` | `null,` `string` | このイベントが属するキャンバスの API ID
`canvas_variation_api_id` | `null,` `string` | このイベントが属するキャンバスバリエーションの API ID
`canvas_step_api_id` | `null,` `string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,` `string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,` `string` | [PII] ユーザーの性別
`country` | `null,` `string` | [PII] ユーザーの国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
`email_address` | `string` | [PII] ユーザーのメールアドレス
`user_agent` | `null,` `string` | スパム報告が発生したユーザーエージェント
`ip_pool` | `null,` `string` | メール送信元の IP プール
`esp` | `null,` `string` | イベントに関連する ESP (SparkPost または SendGrid)
`from_domain` | `null,` `string` | メール送信ドメイン
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS\_MESSAGES\_EMAIL\_OPEN\_SHARED {#USERS_MESSAGES_EMAIL_OPEN_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` |`string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
`device_id` | `null,` `string` | `device_id`、ユーザーが匿名の場合、このユーザーに関連付けられる
`app_group_api_id` | `null,` `string` | このユーザーが属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`dispatch_id` | `null,` `string` | このメッセージが属するディスパッチの ID
`send_id` | `null,` `string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `null,` `string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,` `string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,` `string` | このユーザーが受け取ったメッセージバリエーションの API ID
`canvas_id` | `null,` `string` | このイベントが属するキャンバスの内部使用 Braze ID
`canvas_api_id` | `null,` `string` | このイベントが属するキャンバスの API ID
`canvas_variation_api_id` | `null,` `string` | このイベントが属するキャンバスバリエーションの API ID
`canvas_step_api_id` | `null,` `string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,` `string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,` `string` | [PII] ユーザーの性別
`country` | `null,` `string` | [PII] ユーザーの国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
`email_address` | `string` | [PII] ユーザーのメールアドレス
`user_agent` | `null,` `string` | 開封が発生したユーザーエージェント
`ip_pool` | `null,` `string` | メール送信元の IP プール
`machine_open` | `null,` `string` | たとえば、プライバシー保護が有効になっている Apple デバイスなどで、ユーザーがエンゲージせずに開封イベントがトリガーされた場合は、「true」に設定されます。値は、より詳細な情報を提供するために、時間の経過とともに変化する可能性があります。
`esp` | `null,` `string` | イベントに関連する ESP (SparkPost または SendGrid)
`from_domain` | `null,` `string` | メール送信ドメイン
`is_amp` | `null, boolean` | これが AMP イベントであることを示す
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS\_MESSAGES\_EMAIL\_SEND\_SHARED {#USERS_MESSAGES_EMAIL_SEND_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` |`string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
`device_id` | `null,` `string` | `device_id`、ユーザーが匿名の場合、このユーザーに関連付けられる
`app_group_api_id` | `null,` `string` | このユーザーが属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`dispatch_id` | `null,` `string` | このメッセージが属するディスパッチの ID
`send_id` | `null,` `string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `null,` `string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,` `string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,` `string` | このユーザーが受け取ったメッセージバリエーションの API ID
`canvas_id` | `null,` `string` | このイベントが属するキャンバスの内部使用 Braze ID
`canvas_api_id` | `null,` `string` | このイベントが属するキャンバスの API ID
`canvas_variation_api_id` | `null,` `string` | このイベントが属するキャンバスバリエーションの API ID
`canvas_step_api_id` | `null,` `string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,` `string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,` `string` | [PII] ユーザーの性別
`country` | `null,` `string` | [PII] ユーザーの国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
`email_address` | `string` | [PII] ユーザーのメールアドレス
`ip_pool` | `null,` `string` | メール送信元の IP プール
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS\_MESSAGES\_EMAIL\_SOFTBOUNCE\_SHARED {#USERS_MESSAGES_EMAIL_SOFTBOUNCE_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` |`string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
`device_id` | `null,` `string` | `device_id`、ユーザーが匿名の場合、このユーザーに関連付けられる
`app_group_api_id` | `null,` `string` | このユーザーが属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`dispatch_id` | `null,` `string` | このメッセージが属するディスパッチの ID
`send_id` | `null,` `string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `null,` `string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,` `string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,` `string` | このユーザーが受け取ったメッセージバリエーションの API ID
`canvas_id` | `null,` `string` | このイベントが属するキャンバスの内部使用 Braze ID
`canvas_api_id` | `null,` `string` | このイベントが属するキャンバスの API ID
`canvas_variation_api_id` | `null,` `string` | このイベントが属するキャンバスバリエーションの API ID
`canvas_step_api_id` | `null,` `string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,` `string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,` `string` | [PII] ユーザーの性別
`country` | `null,` `string` | [PII] ユーザーの国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
`email_address` | `string` | [PII] ユーザーのメールアドレス
`sending_ip` | `null,` `string` | メール送信元のIPアドレス
`ip_pool` | `null,` `string` | メール送信元の IP プール
`bounce_reason` | `null,` `string` | [PII] このバウンスイベントで受信した SMTP 理由コードとユーザーフレンドリーメッセージ
`esp` | `null,` `string` | イベントに関連する ESP (SparkPost または SendGrid)
`from_domain` | `null,` `string` | メール送信ドメイン
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS\_MESSAGES\_EMAIL\_UNSUBSCRIBE\_SHARED {#USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` |`string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
`device_id` | `null,` `string` | `device_id`、ユーザーが匿名の場合、このユーザーに関連付けられる
`app_group_api_id` | `null,` `string` | このユーザーが属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`dispatch_id` | `null,` `string` | このメッセージが属するディスパッチの ID
`send_id` | `null,` `string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `null,` `string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,` `string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,` `string` | このユーザーが受け取ったメッセージバリエーションの API ID
`canvas_id` | `null,` `string` | このイベントが属するキャンバスの内部使用 Braze ID
`canvas_api_id` | `null,` `string` | このイベントが属するキャンバスの API ID
`canvas_variation_api_id` | `null,` `string` | このイベントが属するキャンバスバリエーションの API ID
`canvas_step_api_id` | `null,` `string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,` `string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,` `string` | [PII] ユーザーの性別
`country` | `null,` `string` | [PII] ユーザーの国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
`email_address` | `string` | [PII] ユーザーのメールアドレス
`ip_pool` | `null,` `string` | メール送信元の IP プール
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS\_MESSAGES\_INAPPMESSAGE\_ABORT\_SHARED {#USERS_MESSAGES_INAPPMESSAGE_ABORT_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` |`string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
`app_group_api_id` | `null,` `string` | このユーザーが属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`app_api_id` | `null,` `string` | このイベントが発生したアプリの API ID
`card_api_id` | `null,` `string` | カードの API ID
`dispatch_id` | `null,` `string` | このメッセージが属するディスパッチの ID
`send_id` | `null,` `string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `null,` `string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,` `string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,` `string` | このユーザーが受け取ったメッセージバリエーションの API ID
`canvas_id` | `null,` `string` | このイベントが属するキャンバスの内部使用 Braze ID
`canvas_api_id` | `null,` `string` | このイベントが属するキャンバスの API ID
`canvas_variation_api_id` | `null,` `string` | このイベントが属するキャンバスバリエーションの API ID
`canvas_step_api_id` | `null,` `string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,` `string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,` `string` | [PII] ユーザーの性別
`country` | `null,` `string` | [PII] ユーザーの国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
`device_id` | `null,` `string` ｜イベントが発生したデバイスの ID
`sdk_version` | `null,` `string` | イベント中に使用された Braze SDK のバージョン
`platform` | `null,` `string` | デバイスのプラットフォーム
`os_version` | `null,` `string` | デバイスのオペレーティングシステムのバージョン
`device_model` | `null,` `string` | デバイスのモデル
`resolution` | `null,` `string` | デバイスの解像度
`carrier` | `null,` `string` | デバイスの通信業者
`browser` | `null,` `string` | デバイスのブラウザー
`version` | `string` | アプリ内メッセージのバージョン、レガシーまたはトリガー済み
`ad_id` | `null,` `string` | [PII] 広告識別子
`ad_id_type` | `null,` `string` | `ios_idfa`、`google_ad_id`、`windows_ad_id`、または `roku_ad_id` のいずれか
`ad_tracking_enabled` | `null, boolean` | デバイスの広告追跡が有効かどうか
`abort_type` | `null,` `string` | 中止のタイプ。`liquid_abort_message`、`quiet_hours`、`rate_limit` のいずれか
`abort_log` | `null,` `string` | [PII] 中止の詳細を記述するログメッセージ (最大 128 文字)
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS\_MESSAGES\_INAPPMESSAGE\_CLICK\_SHARED {#USERS_MESSAGES_INAPPMESSAGE_CLICK_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` |`string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
`app_group_api_id` | `null,` `string` | このユーザーが属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`app_api_id` | `null,` `string` | このイベントが発生したアプリの API ID
`card_api_id` | `null,` `string` | カードの API ID
`dispatch_id` | `null,` `string` | このメッセージが属するディスパッチの ID
`send_id` | `null,` `string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `null,` `string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,` `string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,` `string` | このユーザーが受け取ったメッセージバリエーションの API ID
`canvas_id` | `null,` `string` | このイベントが属するキャンバスの内部使用 Braze ID
`canvas_api_id` | `null,` `string` | このイベントが属するキャンバスの API ID
`canvas_variation_api_id` | `null,` `string` | このイベントが属するキャンバスバリエーションの API ID
`canvas_step_api_id` | `null,` `string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,` `string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,` `string` | [PII] ユーザーの性別
`country` | `null,` `string` | [PII] ユーザーの国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
`device_id` | `null,` `string` ｜イベントが発生したデバイスの ID
`sdk_version` | `null,` `string` | イベント中に使用された Braze SDK のバージョン
`platform` | `null,` `string` | デバイスのプラットフォーム
`os_version` | `null,` `string` | デバイスのオペレーティングシステムのバージョン
`device_model` | `null,` `string` | デバイスのモデル
`resolution` | `null,` `string` | デバイスの解像度
`carrier` | `null,` `string` | デバイスの通信業者
`browser` | `null,` `string` | デバイスのブラウザー
`version` | `string` | アプリ内メッセージのバージョン、レガシーまたはトリガー済み
`button_id` | `null,` `string` | クリックされたボタンの ID (このクリックがボタンのクリックを表す場合)
`ad_id` | `null,` `string` | [PII] 広告識別子
`ad_id_type` | `null,` `string` | `ios_idfa`、`google_ad_id`、`windows_ad_id`、または `roku_ad_id` のいずれか
`ad_tracking_enabled` | `null, boolean` | デバイスの広告追跡が有効かどうか
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS\_MESSAGES\_INAPPMESSAGE\_IMPRESSION\_SHARED {#USERS_MESSAGES_INAPPMESSAGE_IMPRESSION_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` |`string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
`app_group_api_id` | `null,` `string` | このユーザーが属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`app_api_id` | `null,` `string` | このイベントが発生したアプリの API ID
`card_api_id` | `null,` `string` | カードの API ID
`dispatch_id` | `null,` `string` | このメッセージが属するディスパッチの ID
`send_id` | `null,` `string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `null,` `string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,` `string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,` `string` | このユーザーが受け取ったメッセージバリエーションの API ID
`canvas_id` | `null,` `string` | このイベントが属するキャンバスの内部使用 Braze ID
`canvas_api_id` | `null,` `string` | このイベントが属するキャンバスの API ID
`canvas_variation_api_id` | `null,` `string` | このイベントが属するキャンバスバリエーションの API ID
`canvas_step_api_id` | `null,` `string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,` `string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,` `string` | [PII] ユーザーの性別
`country` | `null,` `string` | [PII] ユーザーの国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
`device_id` | `null,` `string` ｜イベントが発生したデバイスの ID
`sdk_version` | `null,` `string` | イベント中に使用された Braze SDK のバージョン
`platform` | `null,` `string` | デバイスのプラットフォーム
`os_version` | `null,` `string` | デバイスのオペレーティングシステムのバージョン
`device_model` | `null,` `string` | デバイスのモデル
`resolution` | `null,` `string` | デバイスの解像度
`carrier` | `null,` `string` | デバイスの通信業者
`browser` | `null,` `string` | デバイスのブラウザー
`version` | `string` | アプリ内メッセージのバージョン、レガシーまたはトリガー済み
`ad_id` | `null,` `string` | [PII] 広告識別子
`ad_id_type` | `null,` `string` | `ios_idfa`、`google_ad_id`、`windows_ad_id`、または `roku_ad_id` のいずれか
`ad_tracking_enabled` | `null, boolean` | デバイスの広告追跡が有効かどうか
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS\_MESSAGES\_NEWSFEEDCARD\_ABORT\_SHARED {#USERS_MESSAGES_NEWSFEEDCARD_ABORT_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` |`string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
`app_group_api_id` | `null,` `string` | このユーザーが属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`app_api_id` | `null,` `string` | このイベントが発生したアプリの API ID
`card_api_id` | `null,` `string` | カードの API ID
`gender` | `null,` `string` | [PII] ユーザーの性別
`country` | `null,` `string` | [PII] ユーザーの国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
`device_id` | `null,` `string` ｜イベントが発生したデバイスの ID
`sdk_version` | `null,` `string` | イベント中に使用された Braze SDK のバージョン
`platform` | `null,` `string` | デバイスのプラットフォーム
`os_version` | `null,` `string` | デバイスのオペレーティングシステムのバージョン
`device_model` | `null,` `string` | デバイスのモデル
`resolution` | `null,` `string` | デバイスの解像度
`carrier` | `null,` `string` | デバイスの通信業者
`browser` | `null,` `string` | デバイスのブラウザー
`abort_type` | `null,` `string` | 中止のタイプ。`liquid_abort_message`、`quiet_hours`、`rate_limit` のいずれか
`abort_log` | `null,` `string` | [PII] 中止の詳細を記述するログメッセージ (最大 128 文字)
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS\_MESSAGES\_NEWSFEEDCARD\_CLICK\_SHARED {#USERS_MESSAGES_NEWSFEEDCARD_CLICK_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` |`string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
`app_group_api_id` | `null,` `string` | このユーザーが属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`app_api_id` | `null,` `string` | このイベントが発生したアプリの API ID
`card_api_id` | `null,` `string` | カードの API ID
`gender` | `null,` `string` | [PII] ユーザーの性別
`country` | `null,` `string` | [PII] ユーザーの国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
`device_id` | `null,` `string` ｜イベントが発生したデバイスの ID
`sdk_version` | `null,` `string` | イベント中に使用された Braze SDK のバージョン
`platform` | `null,` `string` | デバイスのプラットフォーム
`os_version` | `null,` `string` | デバイスのオペレーティングシステムのバージョン
`device_model` | `null,` `string` | デバイスのモデル
`resolution` | `null,` `string` | デバイスの解像度
`carrier` | `null,` `string` | デバイスの通信業者
`browser` | `null,` `string` | デバイスのブラウザー
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS\_MESSAGES\_NEWSFEEDCARD\_IMPRESSION\_SHARED {#USERS_MESSAGES_NEWSFEEDCARD_IMPRESSION_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` |`string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
`app_group_api_id` | `null,` `string` | このユーザーが属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`app_api_id` | `null,` `string` | このイベントが発生したアプリの API ID
`card_api_id` | `null,` `string` | カードの API ID
`gender` | `null,` `string` | [PII] ユーザーの性別
`country` | `null,` `string` | [PII] ユーザーの国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
`device_id` | `null,` `string` ｜イベントが発生したデバイスの ID
`sdk_version` | `null,` `string` | イベント中に使用された Braze SDK のバージョン
`platform` | `null,` `string` | デバイスのプラットフォーム
`os_version` | `null,` `string` | デバイスのオペレーティングシステムのバージョン
`device_model` | `null,` `string` | デバイスのモデル
`resolution` | `null,` `string` | デバイスの解像度
`carrier` | `null,` `string` | デバイスの通信業者
`browser` | `null,` `string` | デバイスのブラウザー
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS\_MESSAGES\_PUSHNOTIFICATION\_ABORT\_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_ABORT_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` |`string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
`device_id` | `null,` `string` | 配信を試みた `device_id`
`app_group_api_id` | `null,` `string` | このユーザーが属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`app_api_id` | `null,` `string` | このイベントが発生したアプリの API ID
`dispatch_id` | `null,` `string` | このメッセージが属するディスパッチの ID
`send_id` | `null,` `string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `null,` `string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,` `string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,` `string` | このユーザーが受け取ったメッセージバリエーションの API ID
`canvas_id` | `null,` `string` | このイベントが属するキャンバスの内部使用 Braze ID
`canvas_api_id` | `null,` `string` | このイベントが属するキャンバスの API ID
`canvas_variation_api_id` | `null,` `string` | このイベントが属するキャンバスバリエーションの API ID
`canvas_step_api_id` | `null,` `string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,` `string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,` `string` | [PII] ユーザーの性別
`country` | `null,` `string` | [PII] ユーザーの国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
`platform` | `string` | デバイスのプラットフォーム
`abort_type` | `null,` `string` | 中止のタイプ。`liquid_abort_message`、`quiet_hours`、`rate_limit` のいずれか
`abort_log` | `null,` `string` | [PII] 中止の詳細を記述するログメッセージ (最大 128 文字)
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS\_MESSAGES\_PUSHNOTIFICATION\_BOUNCE\_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_BOUNCE_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` |`string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
`push_token` | `null,` `string` | バウンスしたトークンをプッシュする
`device_id` | `null,` `string` | 配信を試みたがバウンスした `device_id`
`app_group_api_id` | `null,` `string` | このユーザーが属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`app_api_id` | `null,` `string` | このイベントが発生したアプリの API ID
`dispatch_id` | `null,` `string` | このメッセージが属するディスパッチの ID
`send_id` | `null,` `string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `null,` `string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,` `string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,` `string` | このユーザーが受け取ったメッセージバリエーションの API ID
`canvas_id` | `null,` `string` | このイベントが属するキャンバスの内部使用 Braze ID
`canvas_api_id` | `null,` `string` | このイベントが属するキャンバスの API ID
`canvas_variation_api_id` | `null,` `string` | このイベントが属するキャンバスバリエーションの API ID
`canvas_step_api_id` | `null,` `string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,` `string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,` `string` | [PII] ユーザーの性別
`country` | `null,` `string` | [PII] ユーザーの国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
`platform` | `null,` `string` | デバイスのプラットフォーム
`ad_id` | `null,` `string` | [PII] 配信を試みたデバイスの広告 ID
`ad_id_type` | `null,` `string` | 広告 ID のタイプ
`ad_tracking_enabled` | `null, boolean` | 広告の追跡を有効にするかどうか
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS\_MESSAGES\_PUSHNOTIFICATION\_INFLUENCEDOPEN\_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_INFLUENCEDOPEN_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` |`string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
`app_group_api_id` | `null,` `string` | このユーザーが属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`app_api_id` | `null,` `string` | このイベントが発生したアプリの API ID
`dispatch_id` | `null,` `string` | このメッセージが属するディスパッチの ID
`send_id` | `null,` `string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `null,` `string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,` `string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,` `string` | このユーザーが受け取ったメッセージバリエーションの API ID
`canvas_id` | `null,` `string` | このイベントが属するキャンバスの内部使用 Braze ID
`canvas_api_id` | `null,` `string` | このイベントが属するキャンバスの API ID
`canvas_variation_api_id` | `null,` `string` | このイベントが属するキャンバスバリエーションの API ID
`canvas_step_api_id` | `null,` `string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,` `string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,` `string` | [PII] ユーザーの性別
`country` | `null,` `string` | [PII] ユーザーの国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
`device_id` | `null,` `string` ｜イベントが発生したデバイスの ID
`sdk_version` | `null,` `string` | イベント中に使用された Braze SDK のバージョン
`platform` | `null,` `string` | デバイスのプラットフォーム
`os_version` | `null,` `string` | デバイスのオペレーティングシステムのバージョン
`device_model` | `null,` `string` | デバイスのモデル
`resolution` | `null,` `string` | デバイスの解像度
`carrier` | `null,` `string` | デバイスの通信業者
`browser` | `null,` `string` | デバイスのブラウザー
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS\_MESSAGES\_PUSHNOTIFICATION\_IOSFOREGROUND\_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_IOSFOREGROUND_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` |`string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
`app_group_api_id` | `null,` `string` | このユーザーが属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`app_api_id` | `null,` `string` | このイベントが発生したアプリの API ID
`dispatch_id` | `null,` `string` | このメッセージが属するディスパッチの ID
`send_id` | `null,` `string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `null,` `string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,` `string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,` `string` | このユーザーが受け取ったメッセージバリエーションの API ID
`canvas_id` | `null,` `string` | このイベントが属するキャンバスの内部使用 Braze ID
`canvas_api_id` | `null,` `string` | このイベントが属するキャンバスの API ID
`canvas_variation_api_id` | `null,` `string` | このイベントが属するキャンバスバリエーションの API ID
`canvas_step_api_id` | `null,` `string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,` `string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,` `string` | [PII] ユーザーの性別
`country` | `null,` `string` | [PII] ユーザーの国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
`device_id` | `null,` `string` ｜イベントが発生したデバイスの ID
`sdk_version` | `null,` `string` | イベント中に使用された Braze SDK のバージョン
`platform` | `null,` `string` | デバイスのプラットフォーム
`os_version` | `null,` `string` | デバイスのオペレーティングシステムのバージョン
`device_model` | `null,` `string` | デバイスのモデル
`resolution` | `null,` `string` | デバイスの解像度
`carrier` | `null,` `string` | デバイスの通信業者
`browser` | `null,` `string` | デバイスのブラウザー
`ad_id` | `null,` `string` | [PII] 配信を試みたデバイスの広告 ID
`ad_id_type` | `null,` `string` | 広告 ID のタイプ
`ad_tracking_enabled` | `null, boolean` | 広告の追跡を有効にするかどうか
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS\_MESSAGES\_PUSHNOTIFICATION\_OPEN\_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_OPEN_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` |`string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
`app_group_api_id` | `null,` `string` | このユーザーが属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`app_api_id` | `null,` `string` | このイベントが発生したアプリの API ID
`dispatch_id` | `null,` `string` | このメッセージが属するディスパッチの ID
`send_id` | `null,` `string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `null,` `string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,` `string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,` `string` | このユーザーが受け取ったメッセージバリエーションの API ID
`canvas_id` | `null,` `string` | このイベントが属するキャンバスの内部使用 Braze ID
`canvas_api_id` | `null,` `string` | このイベントが属するキャンバスの API ID
`canvas_variation_api_id` | `null,` `string` | このイベントが属するキャンバスバリエーションの API ID
`canvas_step_api_id` | `null,` `string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,` `string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,` `string` | [PII] ユーザーの性別
`country` | `null,` `string` | [PII] ユーザーの国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
`device_id` | `null,` `string` ｜イベントが発生したデバイスの ID
`sdk_version` | `null,` `string` | イベント中に使用された Braze SDK のバージョン
`platform` | `null,` `string` | デバイスのプラットフォーム
`os_version` | `null,` `string` | デバイスのオペレーティングシステムのバージョン
`device_model` | `null,` `string` | デバイスのモデル
`resolution` | `null,` `string` | デバイスの解像度
`carrier` | `null,` `string` | デバイスの通信業者
`browser` | `null,` `string` | デバイスのブラウザー
`button_string` | `null,` `string` | クリックされたプッシュ通知ボタンの識別子 (button_string)。ボタンのクリックでない場合は null
`button_action_type` | `null,` `string` | プッシュ通知ボタンのアクションタイプ。[URI、DEEP\_LINK、NONE、CLOSE] のいずれか。ボタンのクリックでない場合は null
`slide_id` | `null,` `string` | ユーザがクリックしたプッシュ通知カルーセルスライドのスライド識別子
`slide_action_type` | `null,` `string` | プッシュ通知カルーセルスライドのアクションタイプ
`ad_id` | `null,` `string` | [PII] 配信を試みたデバイスの広告 ID
`ad_id_type` | `null,` `string` | 広告 ID のタイプ
`ad_tracking_enabled` | `null, boolean` | 広告の追跡を有効にするかどうか
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS\_MESSAGES\_PUSHNOTIFICATION\_SEND\_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_SEND_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` |`string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
`push_token` | `null,` `string` | 配信を試みたプッシュトークン
`device_id` | `null,` `string` | 配信を試みた `device_id`
`app_group_api_id` | `null,` `string` | このユーザーが属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`app_api_id` | `null,` `string` | このイベントが発生したアプリの API ID
`dispatch_id` | `null,` `string` | このメッセージが属するディスパッチの ID
`send_id` | `null,` `string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `null,` `string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,` `string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,` `string` | このユーザーが受け取ったメッセージバリエーションの API ID
`canvas_id` | `null,` `string` | このイベントが属するキャンバスの内部使用 Braze ID
`canvas_api_id` | `null,` `string` | このイベントが属するキャンバスの API ID
`canvas_variation_api_id` | `null,` `string` | このイベントが属するキャンバスバリエーションの API ID
`canvas_step_api_id` | `null,` `string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,` `string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,` `string` | [PII] ユーザーの性別
`country` | `null,` `string` | [PII] ユーザーの国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
`platform` | `string` | デバイスのプラットフォーム
`ad_id` | `null,` `string` | [PII] 配信を試みたデバイスの広告 ID
`ad_id_type` | `null,` `string` | 広告 ID のタイプ
`ad_tracking_enabled` | `null, boolean` | 広告の追跡を有効にするかどうか
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS\_MESSAGES\_SMS\_ABORT\_SHARED {#USERS_MESSAGES_SMS_ABORT_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` |`string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
`app_group_api_id` | `null,` `string` | このユーザーが属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`campaign_id` | `null,` `string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,` `string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,` `string` | このユーザーが受け取ったメッセージバリエーションの API ID
`canvas_id` | `null,` `string` | このイベントが属するキャンバスの内部使用 Braze ID
`canvas_api_id` | `null,` `string` | このイベントが属するキャンバスの API ID
`canvas_variation_api_id` | `null,` `string` | このイベントが属するキャンバスバリエーションの API ID
`canvas_step_api_id` | `null,` `string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,` `string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`subscription_group_api_id` | `null,` `string` | サブスクリプショングループの外部 ID
`abort_type` | `null,` `string` | 中止のタイプ。`liquid_abort_message`、`quiet_hours`、`rate_limit` のいずれか
`abort_log` | `null,` `string` | [PII] 中止の詳細を記述するログメッセージ (最大 128 文字)
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS\_MESSAGES\_SMS\_CARRIERSEND\_SHARED {#USERS_MESSAGES_SMS_CARRIERSEND_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` |`string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
`device_id` | `null,` `string` | `device_id`、ユーザーが匿名の場合、このユーザーに関連付けられる
`app_group_api_id` | `null,` `string` | このユーザーが属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`dispatch_id` | `null,` `string` | このメッセージが属するディスパッチの ID
`send_id` | `null,` `string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `null,` `string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,` `string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,` `string` | このユーザーが受け取ったメッセージバリエーションの API ID
`canvas_id` | `null,` `string` | このイベントが属するキャンバスの内部使用 Braze ID
`canvas_api_id` | `null,` `string` | このイベントが属するキャンバスの API ID
`canvas_variation_api_id` | `null,` `string` | このイベントが属するキャンバスバリエーションの API ID
`canvas_step_api_id` | `null,` `string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,` `string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,` `string` | [PII] ユーザーの性別
`country` | `null,` `string` | [PII] ユーザーの国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
`to_phone_number` | `null,` `string` | [PII] 受信者の電話番号
`from_phone_number` | `null,` `string` | SMS メッセージの送信元電話番号
`subscription_group_api_id` | `null,` `string` | サブスクリプショングループの外部 ID
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS\_MESSAGES\_SMS\_DELIVERY\_SHARED {#USERS_MESSAGES_SMS_DELIVERY_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` |`string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
`device_id` | `null,` `string` | `device_id`、ユーザーが匿名の場合、このユーザーに関連付けられる
`app_group_api_id` | `null,` `string` | このユーザーが属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`dispatch_id` | `null,` `string` | このメッセージが属するディスパッチの ID
`send_id` | `null,` `string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `null,` `string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,` `string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,` `string` | このユーザーが受け取ったメッセージバリエーションの API ID
`canvas_id` | `null,` `string` | このイベントが属するキャンバスの内部使用 Braze ID
`canvas_api_id` | `null,` `string` | このイベントが属するキャンバスの API ID
`canvas_variation_api_id` | `null,` `string` | このイベントが属するキャンバスバリエーションの API ID
`canvas_step_api_id` | `null,` `string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,` `string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,` `string` | [PII] ユーザーの性別
`country` | `null,` `string` | [PII] ユーザーの国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
`to_phone_number` | `null,` `string` | [PII] 受信者の電話番号
`from_phone_number` | `null,` `string` | SMS メッセージの送信元電話番号
`subscription_group_api_id` | `null,` `string` | サブスクリプショングループの外部 ID
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS\_MESSAGES\_SMS\_DELIVERYFAILURE\_SHARED {#USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` |`string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
`device_id` | `null,` `string` | `device_id`、ユーザーが匿名の場合、このユーザーに関連付けられる
`app_group_api_id` | `null,` `string` | このユーザーが属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`dispatch_id` | `null,` `string` | このメッセージが属するディスパッチの ID
`send_id` | `null,` `string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `null,` `string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,` `string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,` `string` | このユーザーが受け取ったメッセージバリエーションの API ID
`canvas_id` | `null,` `string` | このイベントが属するキャンバスの内部使用 Braze ID
`canvas_api_id` | `null,` `string` | このイベントが属するキャンバスの API ID
`canvas_variation_api_id` | `null,` `string` | このイベントが属するキャンバスバリエーションの API ID
`canvas_step_api_id` | `null,` `string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,` `string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,` `string` | [PII] ユーザーの性別
`country` | `null,` `string` | [PII] ユーザーの国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
`to_phone_number` | `null,` `string` | [PII] 受信者の電話番号
`subscription_group_api_id` | `null,` `string` | サブスクリプショングループの外部 ID
`error` | `null,` `string` | エラー名
`provider_error_code` |`null,` `string` | SMS サービスプロバイダーからのエラーコード
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS\_MESSAGES\_SMS\_INBOUNDRECEIVE\_SHARED {#USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `null,` `string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
`app_group_api_id` | `null,` `string` | 受信電話番号に関連するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`user_phone_number` | `string` | [PII] メッセージを受信したユーザーの電話番号
`subscription_group_id` | `null,` `string` ｜この SMS メッセージの対象となるサブスクリプショングループの ID
`subscription_group_api_id` | `null,` `string` | この SMS メッセージの対象となるサブスクリプショングループの ID
`inbound_phone_number` | `string` | メッセージが送られた受信番号
`action` | `string` | このメッセージに対するアクション。(例: 「配信登録済み」、配信停止、「なし」)。
`message_body` | `string` | ユーザーからの応答
`media_urls` | `null, {"type"=>"array", "items"=>["null", "string"]}` | ユーザーからのメディア URL
`campaign_id` | `null,` `string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,` `string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,` `string` | このイベントが属するメッセージバリエーションの API ID
`canvas_id` | `null,` `string` | このイベントが属するキャンバスの内部使用 Braze ID
`canvas_api_id` | `null,` `string` | このイベントが属するキャンバスの API ID
`canvas_variation_api_id` | `null,` `string` | このイベントが属するキャンバスバリエーションの API ID
`canvas_step_api_id` | `null,` `string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,` `string` | このイベントが属するキャンバスステップメッセージバリエーションの API ID
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS\_MESSAGES\_SMS\_REJECTION\_SHARED {#USERS_MESSAGES_SMS_REJECTION_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` |`string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
`device_id` | `null,` `string` | `device_id`、ユーザーが匿名の場合、このユーザーに関連付けられる
`app_group_api_id` | `null,` `string` | このユーザーが属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`dispatch_id` | `null,` `string` | このメッセージが属するディスパッチの ID
`send_id` | `null,` `string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `null,` `string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,` `string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,` `string` | このユーザーが受け取ったメッセージバリエーションの API ID
`canvas_id` | `null,` `string` | このイベントが属するキャンバスの内部使用 Braze ID
`canvas_api_id` | `null,` `string` | このイベントが属するキャンバスの API ID
`canvas_variation_api_id` | `null,` `string` | このイベントが属するキャンバスバリエーションの API ID
`canvas_step_api_id` | `null,` `string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,` `string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,` `string` | [PII] ユーザーの性別
`country` | `null,` `string` | [PII] ユーザーの国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
`to_phone_number` | `null,` `string` | [PII] 受信者の電話番号
`from_phone_number` | `null,` `string` | SMS メッセージの送信元電話番号
`subscription_group_api_id` | `null,` `string` | サブスクリプショングループの外部 ID
`error` | `null,` `string` | エラー名
`provider_error_code` |`null,` `string` | SMS サービスプロバイダーからのエラーコード
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS\_MESSAGES\_SMS\_SEND\_SHARED {#USERS_MESSAGES_SMS_SEND_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` |`string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
`device_id` | `null,` `string` | `device_id`、ユーザーが匿名の場合、このユーザーに関連付けられる
`app_group_api_id` | `null,` `string` | このユーザーが属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`dispatch_id` | `null,` `string` | このメッセージが属するディスパッチの ID
`send_id` | `null,` `string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `null,` `string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,` `string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,` `string` | このユーザーが受け取ったメッセージバリエーションの API ID
`canvas_id` | `null,` `string` | このイベントが属するキャンバスの内部使用 Braze ID
`canvas_api_id` | `null,` `string` | このイベントが属するキャンバスの API ID
`canvas_variation_api_id` | `null,` `string` | このイベントが属するキャンバスバリエーションの API ID
`canvas_step_api_id` | `null,` `string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,` `string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,` `string` | [PII] ユーザーの性別
`country` | `null,` `string` | [PII] ユーザーの国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
`to_phone_number` | `null,` `string` | [PII] 受信者の電話番号
`subscription_group_api_id` | `null,` `string` | サブスクリプショングループの外部 ID
`category` | `null,` `string` | キーワードカテゴリ名、自動返信メッセージにのみ入力される:「オプトイン」、「オプトアウト」、「ヘルプ」、またはカスタム値
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS\_MESSAGES\_SMS\_SHORTLINKCLICK\_SHARED {#USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `null,` `string` | short_url がターゲットとしたユーザーの Braze ID。short_url がユーザーのクリック追跡を使用していない場合は null
`external_user_id` | `null,` `string` | [PII] short_url が存在する場合は、short_url がターゲットとしたユーザーの外部 ID、short_url がユーザーのクリック追跡を使用していない場合は null
`app_group_api_id` | `null,` `string` | short_url の生成に使用したワークスペースの API ID
`time` | `int` | short\_url がクリックされた Unix タイムスタンプ
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`campaign_id` | `null,` `string` | short_url が生成されたキャンペーンの Braze ID、キャンペーンからのものでない場合は null
`campaign_api_id` | `null,` `string` | short_url が生成されたキャンペーンの API ID、キャンペーンからのものでない場合は null
`message_variation_api_id` | `null,` `string` | short_url が生成されたメッセージ バリエーションの API ID、キャンペーンからのものでない場合は null
`canvas_id` | `null,` `string` | short_url が生成されたキャンバスの Braze ID、キャンバスからのものでない場合は null
`canvas_api_id` | `null,` `string` | short_url が生成されたキャンバスの API ID、キャンバスからのものでない場合は null
`canvas_variation_api_id` | `null,` `string` | short_url が生成されたキャンバスバリエーションの API ID、キャンバスからのものでない場合は null
`canvas_step_api_id` | `null,` `string` | short_url が生成されたキャンバスステップの API ID、キャンバスからのものでない場合は null
`canvas_step_message_variation_api_id` | `null,` `string` | short_url が生成されたキャンバスステップメッセージの API ID、キャンバスからのものでない場合は null
`url` | `string` | short\_url によってリダイレクトされるメッセージに含まれる元の URL
`short_url` | `string` | クリックされた短縮 URL
`user_agent` | `null,` `string` | short_url を要求するユーザーエージェント
`user_phone_number` | `string` | [PII] ユーザーの電話番号
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS\_MESSAGES\_WEBHOOK\_ABORT\_SHARED {#USERS_MESSAGES_WEBHOOK_ABORT_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` |`string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
`device_id` | `null,` `string` | `device_id`、ユーザーが匿名の場合、このユーザーに関連付けられる
`app_group_api_id` | `null,` `string` | このユーザーが属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`dispatch_id` | `null,` `string` | このメッセージが属するディスパッチの ID
`send_id` | `null,` `string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `null,` `string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,` `string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,` `string` | このユーザーが受け取ったメッセージバリエーションの API ID
`canvas_id` | `null,` `string` | このイベントが属するキャンバスの内部使用 Braze ID
`canvas_api_id` | `null,` `string` | このイベントが属するキャンバスの API ID
`canvas_variation_api_id` | `null,` `string` | このイベントが属するキャンバスバリエーションの API ID
`canvas_step_api_id` | `null,` `string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,` `string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,` `string` | [PII] ユーザーの性別
`country` | `null,` `string` | [PII] ユーザーの国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
`abort_type` | `null,` `string` | 中止のタイプ。`liquid_abort_message`、`quiet_hours`、`rate_limit` のいずれか
`abort_log` | `null,` `string` | [PII] 中止の詳細を記述するログメッセージ (最大 128 文字)
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS\_MESSAGES\_WEBHOOK\_SEND\_SHARED {#USERS_MESSAGES_WEBHOOK_SEND_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` |`string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,` `string` | [PII] ユーザーの外部ユーザー ID
`device_id` | `null,` `string` | `device_id`、ユーザーが匿名の場合、このユーザーに関連付けられる
`app_group_api_id` | `null,` `string` | このユーザーが属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`dispatch_id` | `null,` `string` | このメッセージが属するディスパッチの ID
`send_id` | `null,` `string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `null,` `string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,` `string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,` `string` | このユーザーが受け取ったメッセージバリエーションの API ID
`canvas_id` | `null,` `string` | このイベントが属するキャンバスの内部使用 Braze ID
`canvas_api_id` | `null,` `string` | このイベントが属するキャンバスの API ID
`canvas_variation_api_id` | `null,` `string` | このイベントが属するキャンバスバリエーションの API ID
`canvas_step_api_id` | `null,` `string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,` `string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,` `string` | [PII] ユーザーの性別
`country` | `null,` `string` | [PII] ユーザーの国
`timezone` | `null,` `string` | ユーザーのタイムゾーン
`language` | `null,` `string` | [PII] ユーザーの言語
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## ユーザー

### USERS\_RANDOMBUCKETNUMBERUPDATE\_SHARED {#USERS_RANDOMBUCKETNUMBERUPDATE_SHARED}

| フィールド                       | タイプ                     | 説明                                        |
| --------------------------- | ------------------------ | -------------------------------------------------- |
| `id`                        | `string`、`null`    | このイベントのグローバルな一意の ID                  |
| `app_group_id`              | `string`、`null`    | このユーザーが属するワークスペースの Braze ID      |
| `app_group_api_id`          | `string`、`null`    | このユーザーが属するワークスペースの API ID       |
| `user_id`                   | `string`、`null`    | このイベントを実行したユーザーの Braze ID      |
| `external_user_id`          | `string`、`null`    | [PII] ユーザーの外部ユーザー ID                 |
| `time`                      | `int`、`null`       | イベントが発生した Unix タイムスタンプ         |
| `random_bucket_number`      | `int`、`null`       | ユーザーに割り当てられた現在のランダムバケット番号  |
| `prev_random_bucket_number` | `int`、`null`       | ユーザーに割り当てられた以前のランダムバケット番号 |
| `sf_created_at`             | `timestamp`、`null` | このイベントが Snowpipe に検出されたとき      |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS\_USERDELETEREQUEST\_SHARED {#USERS_USERDELETEREQUEST_SHARED}

| フィールド              | タイプ                     | 説明                                                   |
| ------------------ | ------------------------ | ------------------------------------------------------------- |
| `id`               | `string`、`null`    | このイベントのグローバルな一意の ID                             |
| `user_id`          | `string`、`null`    | 削除されたユーザーの Braze ID                          |
| `app_group_id`     | `string`、`null`    | このユーザーが属するワークスペースの Braze ID                 |
| `app_group_api_id` | `string`、`null`    | このユーザーが属するワークスペースの API ID                  |
| `time`             | `int`、`null`       | ユーザー削除リクエストが処理された Unix タイムスタンプ |
| `sf_created_at`    | `timestamp`、`null` | このイベントが Snowpipe に検出されたとき                 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS\_USERORPHAN\_SHARED {#USERS_USERORPHAN_SHARED}

| フィールド              | タイプ                     | 説明                                                                   |
| ------------------ | ------------------------ | ----------------------------------------------------------------------------- |
| `id`               | `string`、`null`    | このイベントのグローバルな一意の ID                                             |
| `user_id`          | `string`、`null`    | 孤立したユーザーの Braze ID                                         |
| `external_user_id` | `string`、`null`    | [PII] ユーザーの外部ユーザー ID                                            |
| `device_id`        | `string`、`null`    | 匿名の場合、このユーザーに関連付けられているデバイスの ID          |
| `app_group_id`     | `string`、`null`    | このユーザーが属するワークスペースの Braze ID                                 |
| `app_group_api_id` | `string`、`null`    | このユーザーが属するワークスペースの API ID                                  |
| `app_api_id`       | `string`、`null`    | 孤立したユーザーが属するアプリの API ID                               |
| `time`             | `int`、`null`       | ユーザーが孤立した Unix タイムスタンプ                                 |
| `orphaned_by_id`   | `string`、`null`    | プロファイルが孤立したユーザーのプロフィールとマージされたユーザーの Braze ID |
| `sf_created_at`    | `timestamp`、`null` | このイベントが Snowpipe に検出されたとき                                 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}
