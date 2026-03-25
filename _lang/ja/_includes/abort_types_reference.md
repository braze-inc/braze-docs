以下の表は、使用可能な `abort_type` の値を一覧にしたものです。中止タイプは、メッセージが送信されなかった具体的な理由を示します。

{% if include.channel %}
{% assign ch = include.channel %}
{% else %}
{% assign ch = "all" %}
{% endif %}

### 一般

これらの中止タイプは、すべてのメッセージングチャネルで発生する可能性があります。

| `abort_type` の値 | 説明 |
| --- | --- |
| `liquid_abort_message` | [abort_message]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/) Liquid タグが呼び出されたため、送信がキャンセルされました。 |
| `template_parse_error` | 構文またはレンダリングエラーによりメッセージテンプレートを解析できなかったため、送信がキャンセルされました。 |
| `rate_limit` | 設定された[レート制限]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/)を超えたため、メッセージが中止されました。 |
| `campaign_disabled` | メッセージが送信される前にキャンペーンが無効化されました。 |
| `campaign_does_not_exist` | このメッセージに関連付けられたキャンペーンが存在しなくなりました。 |
| `campaign_action_does_not_exist` | このメッセージに関連付けられたキャンペーンアクションが存在しなくなりました。 |
| `message_variation_does_not_exist` | このユーザーに割り当てられたメッセージバリエーションが存在しなくなりました。 |
| `user_not_in_segment` | ユーザーがターゲット Segment に含まれていないため、メッセージは送信されませんでした。 |
| `trigger_event_blacklisted` | トリガーイベントがブロックリストに登録されているため、メッセージは送信されませんでした。 |
| `exhausted_retries` | 最大リトライ回数を超えてもメッセージを送信できませんでした。 |
| `frequency_capped` | ワークスペースの[フリークエンシーキャップ]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#about-frequency-capping)ルールで許可されたメッセージの最大数をユーザーがすでに受信しています。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% unless ch == "newsfeedcard" or ch == "rcs" %}

### コンテンツとレンダリング

| `abort_type` の値 | 説明 |
| --- | --- |
| `exhausted_cc_retries` | コネクテッドコンテンツが最大リトライ回数を超えて失敗したため、メッセージが中止されました。 |
| `connected_content_not_supported` | このコンテキストでは[コネクテッドコンテンツ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/)がサポートされていないため、メッセージが中止されました。 |
| `promo_codes_not_supported` | このコンテキストではプロモーションコードがサポートされていないため、メッセージが中止されました。 |
| `catalog_items_rerender_not_supported` | このコンテキストではカタログアイテムの再レンダリングがサポートされていないため、メッセージが中止されました。 |
{% if ch == "all" or ch == "email" or ch == "push" or ch == "inappmessage" or ch == "contentcard" or ch == "webhook" or ch == "banner" %}| `blacklisted_media_url` | メディア URL がブロックリストに登録されており、メッセージで使用できません。 |
| `blocked_media_url` | メディア URL がセキュリティポリシーによりブロックされました。 |
| `invalid_media_url` | メディア URL が無効であるか、解決できませんでした。 |{% endif %}
{% if ch == "all" or ch == "email" or ch == "webhook" %}| `ssl_error` | リクエスト中に SSL エラーが発生しました。 |
| `invalid_http_status` | HTTP リクエストが失敗のステータスコードを返しました。 |
| `http_timeout` | HTTP リクエストが応答を受信する前にタイムアウトしました。 |
| `missing_hostname` | リクエスト URL にホスト名がありません。 |{% endif %}
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endunless %}

{% if ch == "all" or ch == "email" %}

### メール

| `abort_type` の値 | 説明 |
| --- | --- |
| `exhausted_link_shortening_retries` | リンク短縮が最大リトライ回数を超えて失敗しました。 |
| `missing_email` | ユーザーのプロファイルにメールアドレスがありません。 |
| `invalid_domain` | メールアドレスのドメインが無効です。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endif %}

{% if ch == "all" or ch == "push" %}

### プッシュ

| `abort_type` の値 | 説明 |
| --- | --- |
| `invalid_push_payload` | プッシュ通知のペイロードが無効または不正な形式です。 |
| `sdk_not_supported` | ユーザーのデバイスの SDK バージョンがこのタイプのプッシュ通知をサポートしていません。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endif %}

{% if ch == "all" or ch == "sms" %}

### SMS/MMS

| `abort_type` の値 | 説明 |
| --- | --- |
| `exhausted_link_shortening_retries` | リンク短縮が最大リトライ回数を超えて失敗しました。 |
| `sms_empty_payload` | SMS メッセージの本文が空です。 |
| `sms_no_sending_numbers` | このサブスクリプショングループで利用可能な送信用電話番号がありません。 |
| `sms_fatal_provider_error` | SMS プロバイダーで致命的なエラーが発生し、メッセージを配信できませんでした。 |
| `sms_gateway_domain_not_allowed` | SMS ゲートウェイドメインが許可リストに含まれていません。 |
| `blocked_recipient_country` | 受信者の電話番号が[地理的権限]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_geographic_permissions/)によりブロックされている国のものです。 |
| `mms_not_supported` | この受信者または送信番号では MMS がサポートされていません。 |
| `no_current_messaging_service` | このサブスクリプショングループにアクティブなメッセージングサービスが設定されていません。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endif %}

{% if ch == "all" or ch == "whatsapp" %}

### WhatsApp

| `abort_type` の値 | 説明 |
| --- | --- |
| `whats_app_no_sending_numbers` | この WhatsApp サブスクリプショングループで利用可能な送信用電話番号がありません。 |
| `whats_app_invalid_template_message` | WhatsApp テンプレートメッセージが無効であるか、承認されていません。 |
| `whats_app_invalid_response_message` | WhatsApp 応答メッセージが無効です。 |
| `whats_app_fatal_provider_error` | WhatsApp プロバイダーで致命的なエラーが発生し、メッセージを配信できませんでした。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endif %}

{% if ch == "all" or ch == "line" %}

### LINE

| `abort_type` の値 | 説明 |
| --- | --- |
| `line_fatal_provider_error` | LINE プロバイダーで致命的なエラーが発生し、メッセージを配信できませんでした。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endif %}

{% if ch == "all" or ch == "kakao" %}

### Kakao

| `abort_type` の値 | 説明 |
| --- | --- |
| `kakao_fatal_provider_error` | Kakao プロバイダーで致命的なエラーが発生し、メッセージを配信できませんでした。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endif %}

{% if ch == "all" or ch == "contentcard" %}

### コンテンツカード

| `abort_type` の値 | 説明 |
| --- | --- |
| `content_card_size_exceeded` | コンテンツカードのペイロードが最大サイズ制限 (2 KB) を超えています。 |
| `content_card_content_invalid` | コンテンツカードのコンテンツが無効であるか、サポートされていない文字が含まれています。 |
| `content_card_expiration_invalid` | コンテンツカードの有効期限が無効です。 |
| `content_card_general` | 一般的なエラーによりコンテンツカードを作成できませんでした。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endif %}

{% if ch == "all" or ch == "inappmessage" %}

### アプリ内メッセージ

| `abort_type` の値 | 説明 |
| --- | --- |
| `no_longer_in_availability_window` | 設定された利用可能時間枠内にメッセージを送信できなかったため、中止されました。 |
| `maximum_impressions_reached` | アプリ内メッセージはすでに最大インプレッション数に達しています。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endif %}

{% if ch == "all" or ch == "webhook" %}

### Webhook

| `abort_type` の値 | 説明 |
| --- | --- |
| `blocked_webhook_url` | Webhook URL がセキュリティポリシーによりブロックされました。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endif %}