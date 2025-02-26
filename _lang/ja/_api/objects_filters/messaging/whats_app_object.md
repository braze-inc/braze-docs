---
nav_title: "WhatsAppオブジェクト"
article_title: WhatsAppメッセージングオブジェクト
page_order: 15
page_type: reference
channel: WhatsApp
description: "この参考記事では、Braze WhatsApp オブジェクトのさまざまなコンポーネントについて説明します。"

---

# WhatsAppオブジェクト

> `whats_app` オブジェクトを使用すると、[メッセージングエンドポイント]({{site.baseurl}}/api/endpoints/messaging)経由でWhatsAppメッセージを変更または作成できる。

## WhatsAppオブジェクト

```json
{
  "app_id": (required, string) see App Identifier,
  "subscription_group_id": (required, string) the ID of your subscription group,
  "message_variation_id": (optional, string) used when providing a campaign_id to specify which message variation this message should be tracked under,
  "message_type": (required, string) the type of WhatsApp message being sent under the `message` key (template_message | text_response_message | text_image_response_message | quick_reply_response_message),
  "message": (required, object) message object specifying fields the required fields based on the specified message_type. See Message Types for field specifications.
}
```

- [アプリ識別子]({{site.baseurl}}/api/identifier_types/)

### メッセージの種類

#### template_message

```json
{
  "template_name": (required, string) the WhatsApp template name for the message,
  "template_language_code": (required, string) the language code of the WhatsApp template for the message,
  "header_variables": (optional, header variables object) an object to specify header variable values for specified template_name, required if the header has variables; see object specification below,
  "body_variables": (optional, body variable object) an object to specify body variable values for specified template_name, required if the body has variables; see object specification below,
  "button_variables": (optional, button variables object) an object to specify button variable values for specified template_name, required if buttons have variables; see object specification below,
  "header_image_uri" :(optional, string) URI to the header image, if the header is of type IMAGE in specified template_name
}
```

##### ヘッダー変数オブジェクト

`header_variables` オブジェクトを使用すると、WhatsApp テンプレートのヘッダー変数の値を指定することができる。各キーは、指定された値で置換するWhatsAppテンプレート変数のインデックス（ゼロインデックス）である。

```json
{
  "$TEMPLATE_VARIABLE_INDEX_0": "$TEMPLATE_VARIABLE_VALUE_0"
}
```
現在、指定できるヘッダー変数は0個か1個だけである。


###### 例

```json
{
  "0": "Check it out!"
}
```

##### ボディ変数オブジェクト

`body_variables` オブジェクトを使用すると、WhatsApp テンプレートのボディ変数の値を指定することができる。各キーは、指定された値で置換するWhatsAppテンプレート変数のインデックス（ゼロインデックス）である。
```json
{
  "$TEMPLATE_VARIABLE_INDEX_0": "$TEMPLATE_VARIABLE_VALUE_0",
  "$TEMPLATE_VARIABLE_INDEX_1": "$TEMPLATE_VARIABLE_VALUE_1"
}
```

###### 例

```json
{
  "0": "Check it out!",
  "1": "It's pretty neat."
}
```

##### ボタン変数オブジェクト

`button_variables` オブジェクトを使用すると、WhatsApp テンプレートのボタン変数の値を指定することができる。各キーは、指定された値で置換するWhatsAppテンプレート変数のインデックス（ゼロインデックス）である。

```json
{
  "$TEMPLATE_VARIABLE_INDEX_1": "$TEMPLATE_VARIABLE_VALUE_1",
}
```

現在、指定できるボタン変数は 1 つだけで、CTA URL のパスコンポーネントです。変数のインデックスは、テンプレート内のCTA URLボタンのインデックスと一致しなければならない。例えば、CTAボタンがテンプレートの2番目のボタンであれば、変数インデックス「1」を使う。

###### 例

```json
{
  "1": "/marketing/promotion123"
}
```

#### text_response_message

```json
{
  "body": (required, string) the body of the message to send,
  "preview_url": (optional, boolean) whether WhatsApp should render a preview of links included in body
}
```

###### 例

```json
{
  "body": "Check out our new deals at https://braze.com",
  "preview_url": true
}
```

#### text_image_response_message

```json
{
  "image_uri": (required, string) the uri of the image to send,
  "caption": (optional, string) the caption for the image being sent
}
```

###### 例

```json
{
  "image_uri": "https://braze.com/promotion.jpg",
  "caption": "This won't last for long, check it out!"
}
```

#### quick_reply_response_message

```json
{
  "body": (required, string) the body of the message to send,
  "header_image_uri": (optional, string) the URI of the image to send as the message header (only valid if header_text not present),
  "header_text": (optional, string) the text to send as the message header (only valid if header_image_uri not present),
  "footer": (optional, string) the footer of the message to send,
  "buttons": (required, array) array of Button objects. Will render in message based on order in array.
}
```

##### ボタン・オブジェクト

```json
{
  "text": (required, string) the text of the button
}
```

###### 例

```json
{
  "body": "Want to keep hearing from us?",
  "buttons": [
    {
      "text": "Yes!"
    },
    {
      "text": "No thanks"
    }
  ]
}
```
