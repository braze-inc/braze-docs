---
nav_title: メッセージのアーカイブ
article_title: メッセージのアーカイブ
alias: "/message_archiving/"
page_order: 0
page_type: reference
description: "このリファレンス記事では、ユーザーに送信するメッセージのコピーを保存できる機能であるメッセージアーカイブについて説明します。"

---

# メッセージのアーカイブ

> メッセージのアーカイブ機能により、ユーザーに送信されたメッセージのコピーを、保存やコンプライアンス目的で AWS S3 バケット、Azure Blob Storage コンテナ、または Google Cloud Storage バケットに保存できます。<br><br> この記事では、メッセージのアーカイブ設定、JSON ペイロード参照、およびよくある質問について説明します。

メッセージのアーカイブはアドオン機能として利用できます。メッセージのアーカイブを開始するには、Braze のカスタマーサクセスマネージャーにお問い合わせください。

## 仕組み

この機能をオンにすると、Braze は選択したチャネル（メール、SMS/MMS、またはプッシュ）を通じてユーザーに送信された各メッセージについて、gzip 圧縮された JSON ファイルを書き込みます。Braze はこれらのファイルをデフォルトのデータエクスポート先に書き込みます。これには、[トランザクションメール API]({{site.baseurl}}/user_guide/message_building_by_channel/email/transactional_message_api_campaign) を通じて送信されるトランザクションメールキャンペーンなど、各チャネルのすべてのキャンペーンタイプが含まれます。

このファイルには、[ファイル参照](#file-references)で定義されたフィールドが含まれており、ユーザーに送信されるテンプレート化された最終的なメッセージが反映されます。キャンペーンで定義されたテンプレートの値（{% raw %}`{{${first_name}}}`{% endraw %} など）には、プロファイル情報に基づいてユーザーが受け取った最終的な値が表示されます。これにより、送信したメッセージのコピーを保持して、コンプライアンス、監査、またはカスタマーサポートの要件を満たすことができます。

複数のクラウドストレージプロバイダーの認証情報を設定した場合、メッセージのアーカイブ機能では、デフォルトのデータエクスポート先としてマークされたプロバイダーにのみエクスポートされます。明示的なデフォルトが設定されておらず、AWS S3 バケットが接続されている場合、メッセージアーカイブはそのバケットにアップロードされます。

{% alert important %}
この機能をオンにすると、メッセージの配信速度に影響が出ます。正確性を保つため、ファイルのアップロードはメッセージ送信の直前に行われるためです。メッセージのアーカイブによって生じる遅延は、クラウドストレージプロバイダーと、保存されるドキュメントのスループットおよびサイズに応じて異なります。
{% endalert %}

JSON は、次のキー構造を使用してストレージバケットに保存されます。

`sent_messages/{channel, one of: email, push, sms}/{MD5 digest of downcased: email address, push token, or E.164 phone number}/{campaign or Canvas step API ID}/{dispatch ID}.json.gz`

ファイルの例を以下に示します。

`sent_messages/email/819baa08d8d7e77e19d4666f5fc6050b/ee965cb2-8934-4b0a-acf1-91c899c2f915/651fd10b282850b39e1169c13975234b.json.gz`

{% alert note %}
MD5 ダイジェストは、既知の小文字化されたメールアドレス、プッシュトークン、または E.164 電話番号を使ってのみ計算できます。既知の MD5 ダイジェストを逆にして、小文字のメールアドレス、プッシュトークン、または E.164 電話番号を取得することはできません。
{% endalert %}

{% alert tip %}
**バケット内でプッシュトークンが見つからない場合**<br>
Braze は、プッシュトークンをハッシュする前に小文字に変換します。これにより、プッシュトークン `Test_Push_Token12345` はキーパス内で `test_push_token12345` に小文字化され、ハッシュは `32b802170652af2b5624b695f34de089` になります。
{% endalert %}

## メッセージのアーカイブの設定

このセクションでは、ワークスペースのメッセージアーカイブの設定について説明します。先に進む前に、会社でメッセージアーカイブを購入し、有効にしていることを確認してください。

### ステップ 1: クラウドストレージバケットの接続

まだクラウドストレージバケットを接続していない場合は、Braze に接続します。手順については、[Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3/)、[Azure Blob Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents/)、または [Google Cloud Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/google_cloud_storage_for_currents/) に関するパートナーのドキュメントを参照してください。

{% alert note %}
メッセージのアーカイブには Currents の設定は不要です。パートナー向けドキュメントに記載されているその前提条件はスキップして構いません。
{% endalert %}

### ステップ 2: メッセージをアーカイブするチャネルの選択

[**メッセージのアーカイブ**] の設定ページで、送信するメッセージのコピーをクラウドストレージバケットに保存するチャネルを制御します。

チャネルを選択するには次のステップに従います。

1. [**設定**] > [**メッセージのアーカイブ**] に移動します。
2. チャネルを選択します。
3. [**変更の保存**] を選択します。

![[メッセージのアーカイブ] ページには、選択できるチャネルとして、メール、プッシュ、SMS の 3 つがあります。]({% image_buster /assets/img/message_archiving_settings.png %})

{% alert note %}
[**設定**] に [**メッセージのアーカイブ**] が表示されない場合は、会社がメッセージのアーカイブ機能を購入して有効にしていることを確認してください。
{% endalert %}

## ファイル参照

以下は、メッセージが送信されるたびにクラウドストレージバケットに配信される JSON ペイロードへの参照です。[メッセージのアーカイブのサンプルファイル](https://github.com/braze-inc/braze-examples/tree/main/message-archiving)については、コード例リポジトリを参照してください。

{% tabs %}
{% tab Email %}

```json
{
  "version": 1, //numerical version of the JSON structure
  "to": ToAddress, ("customer@example.com")
  "subject": SubjectLine ("20% off coupon inside!"),
  "from_name": DisplayName ("Braze"),
  "from_address": FromAddress ("no-reply@braze.com"),
  "html_body": HtmlBody,
  "plaintext_body": PlainTextBody,
  "amp_body": AMPEmailBody,
  "extras": Hash of key-value pairs from Email Extras configured in the email editor,
  "headers": HashOfHeaders,
  "sent_at": UnixTimestamp,
  "dispatch_id": DispatchIdFromBraze,
  "campaign_id": CampaignApiId, // may not be available
  "canvas_id": CanvasApiId, // may not be available
  "canvas_step_id": CanvasStepApiId, // may not be available
  "canvas_variation_id" : CanvasVariationApiId, // may not be available
  "message_variation_id": MessageVariationApiId, // may not be available,
  "attachments": Array of JSON Objects containing 'bytes' and 'file_name', // may not be available
  "user_id": String,
  "campaign_name": String, // will only be available if the message is from a campaign
  "canvas_name": String, // will only be available if the message is from Canvas
  "canvas_step_name": String, // will only be available if the message is from a Canvas
  "external_id": String
}
```

`extras` フィールドには、HTML エディターでメールを作成する際に **メールの追加情報** フィールドで設定したキーと値のペアが含まれます。メールエクストラ機能はすべてのメールサービスプロバイダー（SendGrid や SparkPost を含む）で動作し、どのプロバイダーを使用しているかに関わらず、アーカイブされたメッセージにも含まれます。メールエクストラの設定に関する詳細は、[メールキャンペーンの作成]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/creating_an_email_campaign/#adding-email-extras)を参照してください。Currents にデータを送り返す方法については、[メッセージエクストラ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/message_extras/)を参照してください。

![]({% image_buster /assets/img_archive/email_extras.png %}){: style="max-width:60%" }

{% endtab %}
{% tab SMS/MMS %}

```json
{
  "version": 1 //numerical version of the JSON structure
  "to": PhoneNumber, ("+15555555555"),
  "body": Body ("Hi there!"),
  "subscription_group": SubscriptionGroupExternalId,
  "provider": StringOfProviderName,
  "media_urls": ArrayOfString, // indicates a message is MMS
  "sent_at": UnixTimestamp,
  "dispatch_id": DispatchIdFromBraze,
  "campaign_id": CampaignApiId, // may not be available
  "canvas_id": CanvasApiId, // may not be available
  "canvas_step_id": CanvasStepApiId, // may not be available
  "canvas_variation_id" : CanvasVariationApiId, // may not be available
  "message_variation_id": MessagVariationApiId, // may not be available
  "user_id": String,
  "campaign_name": String, // will only be available if the message is from a campaign
  "canvas_name": String, // will only be available if the message is from Canvas
  "canvas_step_name": String, // will only be available if the message is from a Canvas
  "external_id": String
}
```

{% endtab %}
{% tab Push %}

```json
{
  "version": 1, //numerical version of the JSON structure
  "to": PushToken,
  "payload": JsonOfEntirePushPayload,
  "platform": one of "android_push" | "ios_push" | "kindle_push" | "web_push",
  "app_id": ApiKeyOfApp,
  "sent_at": UnixTimestamp,
  "dispatch_id": DispatchIdFromBraze,
  "campaign_id": CampaignApiId, // may not be available
  "canvas_id": CanvasApiApiId, // may not be available
  "canvas_step_id": CanvasStepApiId, // may not be available
  "canvas_variation_id" : CanvasVariationApiId, // may not be available
  "message_variation_id": MessagVariationApiId, // may not be available
  "user_id": String,
  "campaign_name": String, // will only be available if the message is from a campaign
  "canvas_name": String, // will only be available if the message is from a Canvas
  "canvas_step_name": String, // will only be available if the message is from a Canvas
  "external_id": String
}
```

### プッシュペイロード構造のバリエーション

{% alert important %}
プッシュ通知アーカイブの最上位 `payload` フィールドには、デバイスに送信されたプロバイダーのペイロード全体が含まれます。この JSON 内では、APNs 用の `aps` や、FCM 用の `notification` および `data` といったキーは、メッセージの種類、プラットフォーム、設定によって大きく異なる場合があります。
{% endalert %}

メッセージのアーカイブはメッセージペイロード自体をキャプチャしますが、FCM や APNs に送信される配信メタデータは含まれません。配信メタデータには以下が含まれます。

- デバイストークン
- 優先度設定
- 有効期限（TTL）
- 折りたたみ ID
- APNs ヘッダー
- 有効期限のタイムスタンプ
- その他の配信設定フィールド

これらのフィールドは、プッシュプロバイダーへの配信指示として機能します。通常、メッセージコンテンツの一部とは見なされません。

以下に例を示します。

- **iOS のプッシュ通知**は、リッチプッシュ通知（`aps.alert` が `title` や `body` などのフィールドを含むオブジェクトである場合）と簡易通知（`aps.alert` が文字列である場合）で構造が異なることがあります。
- **Android のプッシュ通知**（例: FCM）は、カスタムキーを持つデータメッセージを使用します。ペイロード構造は、メッセージの設定に応じて異なるオプションフィールドを含む場合があります。例えば、プッシュボタン、カルーセル、追加のメタデータなどです。

さらに、ダッシュボードからのテスト送信は、本番メッセージとは異なるペイロード構造を生成する可能性があります。

JSON ペイロードの形式はメッセージごとに異なり、時間の経過とともに変更される可能性があります。アーカイブされたプッシュペイロードを解析する際は、固定された構造を前提にしたり、同じフィールドが常に存在すると期待したりしないでください。さまざまなペイロード形式を処理する柔軟な解析ロジックを実装してください。

{% endtab %}
{% endtabs %}

## よくある質問

### ペイロードに含まれないテンプレートは何ですか？

メッセージが Braze を離れた後に行われた変更は、クラウドストレージバケットに保存されたファイルには反映されません。これには、クリックトラッキングのためのリンクのラッピングやトラッキングピクセルの挿入など、メール配信パートナーが行う変更も含まれます。

### キャンペーンパスの「unassociated」の値の下にあるメッセージは何ですか？

メッセージがキャンペーンまたは Canvas 以外で送信される場合、ファイル名のキャンペーン ID は「unassociated」になります。これは、ダッシュボードからテストメッセージを送信した場合、Braze が SMS/MMS 自動レスポンスを送信した場合、または API 経由で送信したメッセージにキャンペーン ID が指定されていない場合に発生します。

### この送信に関する詳細情報を見つけるにはどうすればよいですか？

`external_id` または `dispatch_id` を `user_id` と組み合わせて使用することで、テンプレート化されたメッセージを Currents データと照合し、配信時刻やユーザーが開封・クリックしたかといった詳細情報を確認できます。

### 再試行はどのように処理されますか？

クラウドストレージバケットに到達できない場合、Braze は[バックオフジッター](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/#Jitter)を使用して最大 3 回再試行します。AWS S3 のレート制限の再試行は Braze によって自動的に処理されます。

### 認証情報が無効の場合、どうなりますか？

クラウドストレージの認証情報がいずれかの時点で無効になった場合、Braze はクラウドストレージバケットにメッセージを保存できなくなり、それらのメッセージは失われます。Amazon Web Services、Google Cloud Services、または Azure（Microsoft Cloud Services）の[通知設定]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/notification_preferences/)を構成することを推奨します。これにより、認証情報の問題が発生した場合にアラートを受け取れるようになります。

### アーカイブファイルの `sent_at` タイムスタンプが Currents の送信タイムスタンプと若干異なるのはなぜですか？

レンダリングされたコピーは、ユーザーにメッセージを送信する直前にアップロードされます。クラウドストレージのアップロード時間により、レンダリングされたコピーの `sent_at` タイムスタンプと実際の送信時刻との間に、数秒の遅延が発生する可能性があります。

### 現在の Currents データ用バケットはそのまま使用して、メッセージアーカイブ専用に新しいバケットを作成できますか？

いいえ、できません。このような専用バケットの作成に関心がある場合は、[製品フィードバック]({{site.baseurl}}/user_guide/administrative/access_braze/portal/)をお送りください。

### Currents データエクスポートの仕組みと同様に、アーカイブされたデータは既存のバケット内の専用フォルダーに書き込まれますか？

データはバケットの `sent_messages` セクションに書き込まれます。詳しくは[仕組み](#how-it-works)を参照してください。

### メッセージアーカイブを使って、ファイルを異なるワークスペースにグループ分けできますか？

いいえ、できません。メッセージのアーカイブ機能は、ワークスペースに基づくファイルのグループ化をサポートしていません。代わりに、キャンペーンやキャンバスステップの API ID がどのワークスペースに属するかを特定し、その情報に基づいてグループ化できます。