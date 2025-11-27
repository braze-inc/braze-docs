---
nav_title: "メールオブジェクト"
article_title: 電子メール・メッセージング・オブジェクト
page_order: 5
page_type: reference
channel: email
description: "この参考記事では、Braze メールオブジェクトのさまざまなコンポーネントについて説明します。"

---

# メールオブジェクト

> `email` オブジェクトを使うと、[メッセージング・エンドポイントを通じて]({{site.baseurl}}/api/endpoints/messaging)電子メールを修正したり作成したりすることができる。

## メールオブジェクト

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
  "email_template_id": (optional, string) if provided, Braze uses the subject/body/should_inline_css values from the given email template UNLESS they are specified here, in which case Braze overrides the provided template,
  "message_variation_id": (optional, string) used when providing a campaign_id to specify which message variation this message should be tracked under,
  "extras": (optional, valid Key-Value Hash) extra hash - for SendGrid users, this is passed to SendGrid as Unique Arguments,
  "headers": (optional, valid Key-Value Hash) hash of custom extensions headers (available for SparkPost, SendGrid, or Amazon SES),
  "should_inline_css": (optional, boolean) whether to inline CSS on the body. If not provided, falls back to the default CSS inlining value for the workspace,
  "attachments": (optional, array) array of JSON objects that define the files you need attached, defined by "file_name" and "url",
    "file_name": (required, string) the name of the file you want to attach to your email, excluding the extension (for example, ".pdf"). Attach files up to 2 MB. This is required if you use "attachments",
    "url": (required, string) the corresponding URL of the file you want to attach to your email. The file name's extension is detected automatically from the URL defined, which should return the appropriate "Content-Type" as a response header. This is required if you use "attachments",
}
```

- [アプリ識別子]({{site.baseurl}}/api/identifier_types/)
  - ワークスペースに設定されたアプリの有効な`app_id` は、ユーザーがプロファイルに特定のアプリを持っているかどうかに関係なく、ワークスペース内のすべてのユーザーに対して動作します。
- プリヘッダーの詳細とベストプラクティスについては、[メール本文のスタイル]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/guidelines_and_tips/#body-styling)に関するヘルプ記事を参照してください。

{% alert warning %}
Braze では、添付ファイルの `url` に Google Drive のリンクを使用しないことを推奨しています。これにより、ファイルを取得するためのサーバー呼び出しがブロックされる可能性があり、それによってメールメッセージが送信されなくなる可能性があるからです。
{% endalert %}

有効な添付ファイルの種類には次が含まれます: `txt`、`csv`、`log`、`css`、`ics`、`jpg`、`jpe`、`jpeg`、`gif`、`png`、`bmp`、`psd`、`tif`、`tiff`、`svg`、`indd`、`ai`、`eps`、`doc`、`docx`、`rtf`、`odt`、`ott`、`pdf`、`pub`、`pages`、`mobi`、`epub`、`mp3`、`m4a`、`m4v`、`wma`、`ogg`、`flac`、`wav`、`aif`、`aifc`、`aiff`、`mp4`、`mov`、`avi`、`mkv`、`mpeg`、`mpg`、`wmv`、`xls`、`xlsx`、`ods`、`numbers`、`odp`、`ppt`、`pptx`、`pps`、`key`、`zip`、`vcf`、`pkpass`。

`email_template_id` は、HTML エディターで作成されたメールテンプレートの下部から取得できます。以下は、このIDがどのように見えるかの例である：

![HTMLメールテンプレートのAPI識別子セクション]({% image_buster /assets/img_archive/email_template_id.png %})({: style="max-width:70%;"})

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

1. **設定]>**[**接続コンテンツ]**に移動し、**[認証情報の追加]**をクリックして認証情報を追加する。
2. 名前を入力し、ユーザー名とパスワードを追加する。
3. `/messages/send` エンドポイントの電子メール・オブジェクトに、添付ファイルの詳細でクレデンシャル名を指定する`basic_auth_credential` プロパティを含める。クレデンシャル名を`company_basic_auth_credential_name` とした、以下の例を参照のこと：

```json
{
  "external_user_ids": ["recipient_user_id"],
  "messages":{
    "email":{
      "app_id": "153e8a29-fd6d-4f77-ade7-1a4ca08d457a",
      "subject": "Basis auth attachment test",
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

