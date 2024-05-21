---
nav_title: メッセージのアーカイブ
article_title: メッセージのアーカイブ
alias: "/message_archiving/"
page_order: 0
page_type: reference
description: "このリファレンス記事では、ユーザーに送信するメッセージのコピーを保存できる機能であるメッセージアーカイブについて説明します。"

---

# メッセージのアーカイブ

> メッセージのアーカイブを使用すると、アーカイブやコンプライアンスの目的で、ユーザーに送信したメッセージのコピーを AWS S3 バケット、Azure Blob Storage コンテナー、または Google Cloud Storage バケットに保存できます。

メッセージのアーカイブはアドオン機能として利用できます。メッセージのアーカイブを開始するには、Braze カスタマーサクセスマネージャーにお問い合わせください。

## 概要

この機能がオンになっている場合、クラウドストレージバケットを Braze に接続し、それをデフォルトのデータエクスポート先としてマークすると、Braze は、選択したチャネルを通じてユーザーに送信されるメッセージ (メール、SMS、またはプッシュ) ごとに gzip 圧縮された JSON ファイルをクラウドストレージバケットに書き込みます。 

このファイルには、[[ファイル参照](#file-references)] で定義されたフィールドが含まれており、ユーザーに送信されるテンプレート化された最終的なメッセージが反映されます。キャンペーンで定義されたテンプレートの値 ({% raw %}`{{${first_name}}}`{% endraw %} など) が、プロファイル情報に基づいてユーザーが受け取った最終的な値を示します。これにより、送信したメッセージのコピーを保持して、コンプライアンス、監査、またはカスタマーサポートの要件を満たすことができます。

複数のクラウドストレージプロバイダーの認証情報を設定した場合、メッセージのアーカイブ機能では、デフォルトのデータエクスポート先として明示的にマークされたプロバイダーにのみエクスポートします。明示的なデフォルトが指定されておらず、AWS S3 バケットが接続されている場合、メッセージのアーカイブ機能によりそのバケットにアップロードされます。

{% alert important %}
この機能をオンにすると、正確性を確保するためにメッセージの送信直前にファイルのアップロードが実行されるため、メッセージの配信速度に影響します。これにより、Braze 送信パイプラインに追加の遅延が発生し、送信速度に影響します。
{% endalert %}

JSON は、次のキー構造を使用してストレージバケットに保存されます。

`sent_messages/channel/(one of: md5, e164 phone number, email, or push token)/(campaign_id OR canvas_step_id)/DispatchId.json.gz`

ファイルの例を以下に示します。

`sent_messages/email/819baa08d8d7e77e19d4666f5fc6050b/ee965cb2-8934-4b0a-acf1-91c899c2f915/651fd10b282850b39e1169c13975234b.json.gz`

{% alert note %}
**バケット内でのプッシュトークンの検出に苦労している場合のヒント**<br>
Braze は、プッシュトークンをハッシュする前にその大文字を小文字にします。これにより、プッシュトークン `Test_Push_Token12345` はキーパス内で小文字の `test_push_token12345` になり、ハッシュは `32b802170652af2b5624b695f34de089` です。
{% endalert %}

## メッセージのアーカイブの設定

このセクションでは、ワークスペースのメッセージ アーカイブを設定する方法について説明します。先に進む前に、会社でメッセージアーカイブを購入し、有効にしていることを確認してください。

### ステップ 1: クラウドストレージバケットの接続

まだクラウドストレージバケットを接続していない場合は、Braze に接続します。手順については、[Amazon S3]({{site.baseurl}}/partners/data_and_infrastructure_agility/cloud_storage/amazon_s3/)、[Azure Blob Storage]({{site.baseurl}}/partners/data_and_infrastructure_agility/cloud_storage/microsoft_azure_blob_storage_for_currents/) または [Google Cloud Storage]({{site.baseurl}}/partners/data_and_infrastructure_agility/cloud_storage/google_cloud_storage_for_currents/) に関するパートナーのドキュメントを参照してください。

### ステップ 2: メッセージをアーカイブするチャネルの選択

[**メッセージのアーカイブ**] の設定ページで、送信するメッセージのコピーをクラウドストレージバケットに保存するチャネルを制御します。

チャネルを選択するには次のステップに従います。

1. [**設定**] > [**メッセージのアーカイブ**] に移動します。
2. チャネルを選択します。
3. [**変更内容を保存**] をクリックします。

![[メッセージのアーカイブ] ページには、選択できるチャネルとして、メール、プッシュ、SMS の 3 つがあります。][1]

{% alert note %}
[**設定**] に [**メッセージのアーカイブ**] が表示されない場合は、会社がメッセージのアーカイブ機能を購入して有効にしていることを確認してください。
{% endalert %}

## ファイル参照

以下に、メッセージが送信されるたびにクラウドストレージバケットに配信される JSON ペイロードの参照を示します。[メッセージのアーカイブのサンプル ファイル](https://github.com/braze-inc/braze-examples/tree/main/message-archiving)については、コード例リポジトリを参照してください。

{% tabs %}
{% tab Email %}

```json
{
  "version" : 1, //numerical version of the json structure
  "to": ToAddress, ("customer@example.com")
  "subject": SubjectLine ("20% off coupon inside!"),
  "from_name": DisplayName ("Braze"),
  "from_address": FromAddress ("no-reply@braze.com"),
  "html_body": HtmlBody,
  "plaintext_body": PlainTextBody,
  "amp_body": AMPEmailBody,
  "extras": Extra hash—for SendGrid users, this will be passed to SendGrid as Unique Arguments,
  "headers": HashOfHeaders,
  "sent_at": UnixTimestamp,
  "dispatch_id": DispatchIdFromBraze,
  "campaign_id": CampaignApiKey, // may not be available
  "canvas_id": CanvasApiKey, // may not be available
  "canvas_step_id": CanvasStepID, // may not be available
  "canvas_variation_id" : CanvasVariationId, // may not be available
  "message_variation_id": MessageVariationId, // may not be available,
  "attachments": Array of JSON Objects containing 'bytes' and 'file_name', // may not be available
  "user_id": String,
  "campaign_name": String, // will only be available if the message is from a campaign
  "canvas_name": String, // will only be available if the message is a from Canvas
  "canvas_step_name": String, // will only be available if the message is from a Canvas
  "external_id": String
}
```

このペイロードの `extras` フィールドは、メールの作成時に [**メールエクストラ**] フィールドに追加されたキーと値のペアを表します。Currents にデータを送り返す方法については、[メッセージエクストラ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/message_extras/)を参照してください。

![\]({% image_buster /assets/img_archive/email_extras.png %}){: style="max-width:60%" }

{% endtab %}
{% tab SMS %}

```json
{
  "version" : 1 //numerical version of the json structure
  "to": PhoneNumber, ("+15555555555"),
  "body": Body ("Hi there!"),
  "subscription_group": SubscriptionGroupExternalId,
  "provider": StringOfProviderName,
  "media_urls": ArrayOfString,
  "sent_at": UnixTimestamp,
  "dispatch_id": DispatchIdFromBraze,
  "campaign_id": CampaignApiKey, // may not be available
  "canvas_id": CanvasApiKey, // may not be available
  "canvas_step_id": CanvasStepID, // may not be available
  "canvas_variation_id" : CanvasVariationId, // may not be available
  "message_variation_id": MessagVariationId, // may not be available
  "user_id": String,
  "campaign_name": String, // will only be available if the message is from a campaign
  "canvas_name": String, // will only be available if the message is a from Canvas
  "canvas_step_name": String, // will only be available if the message is from a Canvas
  "external_id": String
}
```

{% endtab %}
{% tab Push %}

```json
{
  "version" : 1, //numerical version of the json structure
  "to": PushToken,
  "payload": JsonOfEntirePushPayload,
  "platform": ios/android/web/kindle,
  "app_id": ApiKeyOfApp,
  "sent_at": UnixTimestamp,
  "dispatch_id": DispatchIdFromBraze,
  "campaign_id": CampaignApiKey, // may not be available
  "canvas_id": CanvasApiKey, // may not be available
  "canvas_step_id": CanvasStepID, // may not be available
  "canvas_variation_id" : CanvasVariationId, // may not be available
  "message_variation_id": MessagVariationId, // may not be available
  "user_id": String,
  "campaign_name": String, // will only be available if the message is from a campaign
  "canvas_name": String, // will only be available if the message is a from Canvas
  "canvas_step_name": String, // will only be available if the message is from a Canvas
  "external_id": String
}
```

{% endtab %}
{% endtabs %}

## よくある質問

### ペイロードに含まれていないテンプレートは何ですか?

メッセージが Braze から送信された後に行われた変更は、クラウドストレージバケットに保存されるファイルに反映されません。これには、メール配信パートナーが行う変更が含まれ、クリック追跡のためのリンクのラッピングや追跡ピクセルの挿入などがあります。

### キャンペーンパスの「unassociated」の値の下にあるメッセージは何ですか?

メッセージがキャンペーンまたはキャンバス以外で送信される場合、ファイル名のキャンペーン ID は「unassociated」になります。これは、ダッシュボードからテストメッセージを送信する場合、Braze が SMS 自動応答を送信する場合、または API 経由で送信されるメッセージにキャンペーン ID が指定されていない場合に発生します。

### この送信に関する詳細情報を見つけるにはどうすればよいですか?

`external_id` または `dispatch_id` のいずれかと `user_id` を組み合わせて、テンプレート化されたメッセージと Currents データを相互参照することにより、メッセージが配信されたタイムスタンプ、ユーザーがメッセージを開封したかクリックしたかなどの詳細情報が得られます。

### 再試行はどのように処理されますか?

クラウドストレージバケットに到達できない場合、Braze では [バックオフジッター](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/#Jitter)を使用して最大 3 回再試行されます。AWS S3 のレート制限の再試行は Braze によって自動的に処理されます。

### 認証情報が無効の場合、どうなりますか?

クラウドストレージの認証情報がいずれかの時点で無効になった場合、その後 Braze はクラウドストレージバケットにメッセージを保存できなくなり、それらのメッセージは失われます。認証情報の問題に関するアラートを確実に受信できるように、[[AWS 認証エラー通知]({{site.baseurl}}/user_guide/administrative/company_settings/notification_preferences)] 設定をを行うことをお勧めします。

### アーカイブファイルの「sent\_at」タイムスタンプが Currents の送信タイムスタンプとわずかに異なるのはなぜですか?

レンダリングされたコピーは、メッセージをエンドユーザーに送信する直前にアップロードされます。クラウドストレージのアップロード時刻により、レンダリングされたコピーの「sent\_at」タイムスタンプと実際の送信時刻との間には、数秒の遅延が発生する可能性があります。

[1]: {% image_buster /assets/img/message_archiving_settings.png %}
