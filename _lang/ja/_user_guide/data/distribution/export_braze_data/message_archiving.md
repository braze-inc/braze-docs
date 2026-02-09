---
nav_title: メッセージのアーカイブ
article_title: メッセージのアーカイブ
alias: "/message_archiving/"
page_order: 0
page_type: reference
description: "このリファレンス記事では、ユーザーに送信するメッセージのコピーを保存できる機能であるメッセージアーカイブについて説明します。"

---

# メッセージのアーカイブ

> メッセージアーカイブを使用すると、アーカイブまたは準拠のためにユーザーに送信されたメッセージのコピーを、AWS S3 バケット、Azure Blob ストレージコンテナ、またはGoogle Cloud Storage バケットに保存できます。<br><br> この記事では、メッセージアーカイブの設定方法、JSON 有料読み込むリファレンス、よくある質問について説明します。

メッセージのアーカイブはアドオン機能として利用できます。メッセージアーカイブの使用を開始するには、Braze 顧客のサクセスマネージャーにお問い合わせください。

## 仕組み

この機能をオンにすると、クラウドストレージバケットをBrazeに接続し、デフォルトのデータ送信先としてマークしている場合、Brazeは、選択したチャネル（メール、SMS/MMS、またはプッシュ）を通じてユーザーに送信された各メッセージについて、gzip圧縮されたJSONファイルをクラウドストレージバケットに書き込む。 

このファイルには、[[ファイル参照](#file-references)] で定義されたフィールドが含まれており、ユーザーに送信されるテンプレート化された最終的なメッセージが反映されます。キャンペーンで定義されたテンプレートの値 ({% raw %}`{{${first_name}}}`{% endraw %} など) が、プロファイル情報に基づいてユーザーが受け取った最終的な値を示します。これにより、送信したメッセージのコピーを保持して、コンプライアンス、監査、またはカスタマーサポートの要件を満たすことができます。

複数のクラウドストレージプロバイダーの認証情報を設定した場合、メッセージのアーカイブ機能では、デフォルトのデータエクスポート先として明示的にマークされたプロバイダーにのみエクスポートされます。明示的なデフォルトが提供されておらず、AWS S3バケットが接続されている場合、メッセージアーカイブはそのバケットにアップロードされます。

{% alert important %}
この機能をオンにすると、メッセージの配信速度に影響が出る。正確性を保つため、アップロードはメッセージ送信の直前に行われるからだ。メッセージのアーカイブによって生じる遅延は、クラウドストレージプロバイダーと、保存されているドキュメントのスループットとサイズに応じて異なります。
{% endalert %}

JSON は、次のキー構造を使用してストレージバケットに保存されます。

`sent_messages/{channel, one of: email, push, sms}/{MD5 digest of downcased: email address, push token, or E.164 phone number}/{campaign or Canvas step API ID}/{dispatch ID}.json.gz`

ファイルの例を以下に示します。

`sent_messages/email/819baa08d8d7e77e19d4666f5fc6050b/ee965cb2-8934-4b0a-acf1-91c899c2f915/651fd10b282850b39e1169c13975234b.json.gz`

{% alert note %}
MD5 ダイジェストは、既知のダウンケースメールアドレス、プッシュトークン、E.164 電話番号を使ってのみ計算できます。既知の MD5 ダイジェストを逆にして、小文字のメールアドレス、プッシュトークン、または E.164 電話番号を取得することはできません。
{% endalert %}

{% alert tip %}
**バケット内でのプッシュトークンの検出に苦労している場合のヒント**<br>
Braze は、プッシュトークンをハッシュする前にその大文字を小文字にします。これにより、プッシュトークン `Test_Push_Token12345` はキーパス内で小文字の `test_push_token12345` になり、ハッシュは `32b802170652af2b5624b695f34de089` です。
{% endalert %}

## メッセージのアーカイブの設定

このセクションでは、ワークスペースのメッセージアーカイブの設定について説明する。先に進む前に、会社でメッセージアーカイブを購入し、有効にしていることを確認してください。

### ステップ 1: クラウドストレージバケットの接続

まだクラウドストレージバケットを接続していない場合は、Braze に接続します。手順については、[Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3/)、[Azure Blob Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents/) または [Google Cloud Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/google_cloud_storage_for_currents/) に関するパートナーのドキュメントを参照してください。

{% alert note %}
メッセージアーカイブのCurrentsを設定する必要はありません。そのため、パートナードキュメントでその前提条件を省略できます。
{% endalert %}

### ステップ 2:メッセージをアーカイブするチャネルの選択

[**メッセージのアーカイブ**] の設定ページで、送信するメッセージのコピーをクラウドストレージバケットに保存するチャネルを制御します。

チャネルを選択するには次のステップに従います。

1. [**設定**] > [**メッセージのアーカイブ**] に移動します。
2. チャネルを選択します。
3. **変更の保存**を選択します。

![[メッセージのアーカイブ] ページには、選択できるチャネルとして、メール、プッシュ、SMS の 3 つがあります。]({% image_buster /assets/img/message_archiving_settings.png %})

{% alert note %}
[**設定**] に [**メッセージのアーカイブ**] が表示されない場合は、会社がメッセージのアーカイブ機能を購入して有効にしていることを確認してください。
{% endalert %}

## ファイル参照

以下は、メッセージが送信されるたびにクラウドストレージバケットに配信されるJSON 有料読み込むのリファレンスです。[メッセージのアーカイブのサンプル ファイル](https://github.com/braze-inc/braze-examples/tree/main/message-archiving)については、コード例リポジトリを参照してください。

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

`extras` フィールドには、HTML エディタでメールを作成するときに** メール Extras** フィールドで設定されたキーと値のペアが含まれます。メールの追加機能は、すべてのメールサービスプロバイダ(SendGridおよびSparkpostを含む)に適用され、どのプロバイダが使用されているかに関係なく、アーカイブメッセージに含まれます。メールエクストラの設定の詳細については、[メール キャンペーンの作成]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/creating_an_email_campaign/#adding-email-extras)を参照してください。Currents にデータを送り返す方法については、[メッセージエクストラ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/message_extras/)を参照してください。

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

{% endtab %}
{% endtabs %}

## よくある質問

### ペイロードに含まれていないテンプレートは何ですか?

メッセージがBrazeを離れた後に行われた修正は、クラウドストレージバケットに保存されたファイルには反映されない。これには、クリック追跡のためのリンクのラッピングやトラッキングピクセルの挿入など、メール配信パートナーが行う修正も含まれる。

### キャンペーンパスの「unassociated」の値の下にあるメッセージは何ですか?

メッセージがキャンペーンまたはキャンバス以外で送信される場合、ファイル名のキャンペーン ID は「unassociated」になります。ダッシュボードからテストメッセージを送信した場合、BrazeがSMS/MMS自動レスポンスを送信した場合、またはAPI経由で送信したメッセージにキャンペーンIDが指定されていない場合に発生する。

### この送信に関する詳細情報を見つけるにはどうすればよいですか?

`external_id` または`dispatch_id` を`user_id` と組み合わせて使用すると、テンプレートd メッセージとCurrentsデータを相互参照して、配信されたタイムスタンプ、ユーザー 開封がメッセージをクリックしたかどうかなどの詳細情報を確認できます。

### 再試行はどのように処理されますか?

クラウドストレージバケットに到達できない場合、Braze では [バックオフジッター](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/#Jitter)を使用して最大 3 回再試行されます。AWS S3 のレート制限の再試行は Braze によって自動的に処理されます。

### 認証情報が無効の場合、どうなりますか?

クラウドストレージの認証情報がいずれかの時点で無効になった場合、その後 Braze はクラウドストレージバケットにメッセージを保存できなくなり、それらのメッセージは失われます。Amazon Web Services、Google Cloud Services、またはAzure (Microsoft Cloud Services) の[通知設定]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/notification_preferences/) を設定して、認証情報の問題に関する警告を受け取るようにすることをお勧めします。

### アーカイブファイルの`sent_at` タイムスタンプが Currents の送信タイムスタンプと若干異なるのはなぜか？

レンダリングされたコピーは、ユーザーにメッセージを送る直前にアップロードされる。クラウドストレージのアップロード時刻により、レンダリングされたコピーの `sent_at` タイムスタンプと実際の送信時刻との間には、数秒の遅延が発生する可能性があります。

### 現在のバケットを引き続き Currents データ用に使用して、メッセージアーカイブ専用に新しいバケットを作成できますか？

できません。このような特定のバケットの作成に関心がある場合には、[製品フィードバック]({{site.baseurl}}/user_guide/administrative/access_braze/portal/)をお送りください。

### Currents データエクスポートの仕組みと同様に、アーカイブされたデータは既存のバケット内の専用フォルダーに書き込まれるのですか?

データはバケットの`sent_messages` セクションに書き込まれます。詳しくは「[仕組み](#how-it-works)」を参照のこと。

### メッセージアーカイブを使用して、ファイルを別のワークスペースにグループ化できますか?

いいえ。メッセージアーカイブでは、ワークスペースs に基づくグループ化はできません。代わりに、キャンペーン またはキャンバスステップ API ID がどのワークスペースに属しているかを判断し、その情報に基づいてグループ化できます。
