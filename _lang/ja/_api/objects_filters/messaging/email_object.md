---
nav_title: "電子メールオブジェクト"
article_title: 電子メール・メッセージング・オブジェクト
page_order: 5
page_type: reference
channel: email
description: "このリファレンス記事では、Brazeメールオブジェクトのさまざまなコンポーネントについて説明します。"

---

# 電子メールオブジェクト

> `email` オブジェクトを使用すると、当社の[メッセージングエンドポイントを介して]({{site.baseurl}}/api/endpoints/messaging)電子メールを変更または作成できます。

## 電子メールオブジェクト

```json
{
  "app_id": (required, string), see App Identifier,
  "subject": (optional, string),
  "from": (required, valid email address in the format "Display Name <email@address.com>"),
  "reply_to": (optional, valid email address in the format "email@address.com" - defaults to your workspace's default reply to if not set) - use "NO_REPLY_TO" to set reply-to address to null,
  "bcc": (optional, one of the BCC addresses defined in your workspace's email settings) if provided and the BCC feature is enabled for your account, this address will get added to your outbound message as a BCC address,
  "body": (required unless email_template_id is given, valid HTML),
  "plaintext_body": (optional, valid plaintext, defaults to autogenerating plaintext from "body" when this is not set),
  "preheader": (optional*, string) recommended length 50-100 characters,
  "email_template_id": (optional, string) if provided, we will use the subject/body/should_inline_css values from the given email template UNLESS they are specified here, in which case we will override the provided template,
  "message_variation_id": (optional, string) used when providing a campaign_id to specify which message variation this message should be tracked under,
  "extras": (optional, valid Key-Value Hash) extra hash - for SendGrid users, this will be passed to SendGrid as Unique Arguments,
  "headers": (optional, valid Key-Value Hash) hash of custom extensions headers (available for SparkPost and SendGrid),
  "should_inline_css": (optional, boolean) whether to inline CSS on the body. If not provided, falls back to the default CSS inlining value for the workspace,
  "attachments": (optional, array) array of JSON objects that define the files you need attached, defined by "file_name" and "url",
    "file_name": (required, string) the name of the file you want to attach to your email, excluding the extension (for example, ".pdf"). Attach files up to 2 MB. This is required if you use "attachments",
    "url": (required, string) the corresponding URL of the file you want to attach to your email. The file name's extension will be detected automatically from the URL defined, which should return the appropriate "Content-Type" as a response header. This is required if you use "attachments",
}
```

- [アプリ識別子]({{site.baseurl}}/api/identifier_types/)
- プリヘッダーに関するより詳しい情報とベストプラクティスについては、[email body styling][46]のヘルプ記事を参照してください。

{% alert warning %}
Brazeでは、添付ファイルの`url` にGoogle Driveのリンクを使用しないことを推奨しています。これは、ファイルを取得するための当社のサーバーの呼び出しがブロックされ、電子メールメッセージが送信されなくなる可能性があるためです。
{% endalert %}

有効な添付ファイルのタイプは以下の通りです：`txt` `csv`,`log`,`css`,`ics`,`jpg`,`jpe`,`jpeg`,`gif`,`png`,`bmp`,`psd`,`tif`,`tiff`,`svg`,`indd`,`ai`,`eps`,`doc`,`docx`,`rtf`,`odt`,`ott`,`pdf`,`pub`,`pages`,`mobi`,`epub`,`mp3` 、`m4a` `m4v`,`wma`,`ogg`,`flac`,`wav`,`aif`,`aifc`,`aiff`,`mp4`,`mov`,`avi`,`mkv`,`mpeg`,`mpg`,`wmv`,`xls`,`xlsx`,`ods`,`numbers`,`odp`,`ppt`,`pptx`,`pps`,`key`,`zip`,`vcf`, および`pkpass` 。

`email_template_id` は、HTMLエディタで作成されたメールテンプレートの下部から取得できます。以下は、このIDがどのように見えるかの例である：

HTMLメールテンプレートのAPI識別子セクション][31]。

## 添付ファイル付き電子メールオブジェクトの例

```json
{
  "external_user_ids": ["YOUR_EXTERNAL_USER_ID"],
  "messages":{
     "email":{
        "app_id":"YOUR_APP_ID",
        "attachments":[{
            "file_name":"YourFileName",
            "url":"https://exampleurl.com/YourFileName.pdf"
         }]
     }
  }
}
```

## 電子メール添付ファイルの認証

{% alert important %}
このエンドポイントにおける電子メール添付ファイルの認証は、現在、早期アクセス中である。早期アクセスにご興味のある方は、Brazeのアカウントマネージャーにお問い合わせください。
{% endalert %}

1. **設定]>**[**接続コンテンツ**]に移動し、[**認証情報の追加**]をクリックして認証情報を追加します。
2. 名前を入力し、ユーザー名とパスワードを追加する。
3. `/messages/send` エンドポイントの電子メール・オブジェクトに、添付ファイルの詳細にクレデンシャル名を指定する`basic_auth_credential` プロパティを含める。以下の例を参照のこと。クレデンシャル名は`company_basic_auth_credential_name` ：

```json
{
  "external_user_ids": ["recipient_user_id"],
  "messages":{
    "email":{
      "app_id": "153e8a29-fd6d-4f77-ade7-1a4ca08d457a",
      "subject": "Basis auth attachement test",
      "from": "mail <mail@e.company.com>",
      "body": "my attachment test",
      "attachments":[
        { "file_name":"checkout_receipt.pdf",
        "url":"https://fileserver.company.com/user123-checkout_receipt.pdf",
        "basic_auth_credential": "company_basic_auth_credential_name" }
      ]
    }
  }
}
```

[31]: {% image_buster /assets/img_archive/email_template_id.png %}
[46]:{{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/guidelines_and_tips/#body-styling
