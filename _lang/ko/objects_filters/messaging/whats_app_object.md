---
nav_title: "WhatsApp 개체"
article_title: WhatsApp 메시징 개체
page_order: 15
page_type: reference
channel: WhatsApp
description: "이 참고 문서에서는 Braze WhatsApp 객체의 다양한 구성요소에 대해 설명합니다."

---

# WhatsApp 개체

> `whats_app` 개체를 사용하면 [메시징 엔드포인트를]({{site.baseurl}}/api/endpoints/messaging) 통해 WhatsApp 메시지를 수정하거나 생성할 수 있습니다.

## WhatsApp 개체

```json
{
  "app_id": (required, string) see App Identifier,
  "subscription_group_id": (required, string) the ID of your subscription group,
  "message_variation_id": (optional, string) used when providing a campaign_id to specify which message variation this message should be tracked under,
  "message_type": (required, string) the type of WhatsApp message being sent under the `message` key (template_message | text_response_message | text_image_response_message | quick_reply_response_message | list_response_message | flow_response_message),
  "message": (required, object) The message object that must include the required fields based on the selected `message_type`. Below are the specific message structures for each type. Refer to the relevant message type for the required fields and their format.
}
```

- [앱 식별자]({{site.baseurl}}/api/identifier_types/)

### 메시지 유형

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

##### 헤더 변수 객체

`header_variables` 개체를 사용하면 WhatsApp 템플릿에서 헤더 변수의 값을 지정할 수 있습니다. 각 키는 지정된 값으로 대체할 WhatsApp 템플릿 변수 인덱스(인덱되지 않음)입니다.

```json
{
  "$TEMPLATE_VARIABLE_INDEX_0": "$TEMPLATE_VARIABLE_VALUE_0"
}
```
현재 헤더 변수는 0 또는 하나만 지정할 수 있습니다.


###### 예시

```json
{
  "0": "Check it out!"
}
```

##### 본문 변수 개체

`body_variables` 개체를 사용하면 WhatsApp 템플릿에서 본문 변수의 값을 지정할 수 있습니다. 각 키는 지정된 값으로 대체할 WhatsApp 템플릿 변수 인덱스(인덱되지 않음)입니다.
```json
{
  "$TEMPLATE_VARIABLE_INDEX_0": "$TEMPLATE_VARIABLE_VALUE_0",
  "$TEMPLATE_VARIABLE_INDEX_1": "$TEMPLATE_VARIABLE_VALUE_1"
}
```

###### 예시

```json
{
  "0": "Check it out!",
  "1": "It's pretty neat."
}
```

##### 버튼 변수 개체

`button_variables` 개체를 사용하면 WhatsApp 템플릿에서 버튼 변수에 대한 값을 지정할 수 있습니다. 각 키는 지정된 값으로 대체할 WhatsApp 템플릿 변수 인덱스(인덱되지 않음)입니다.

```json
{
  "$TEMPLATE_VARIABLE_INDEX_1": "$TEMPLATE_VARIABLE_VALUE_1",
}
```

현재 버튼 변수는 콜투액션 URL의 경로 구성 요소인 버튼 변수 하나만 지정할 수 있습니다. 변수 인덱스는 템플릿의 CTA URL 버튼 인덱스와 일치해야 합니다. 예를 들어 CTA 버튼이 템플릿의 두 번째 버튼인 경우 가변 인덱스 "1"을 사용합니다.

###### 예시

```json
{
  "1": "/marketing/promotion123"
}
```

### 응답 메시지

#### text_response_message

```json
{
  "body": (required, string) the body of the message to send,
  "preview_url": (optional, boolean) whether WhatsApp should render a preview of links included in body
}
```

###### 예시

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

###### 예시

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

##### 버튼 개체

```json
{
  "text": (required, string) the text of the button
}
```

###### 예시

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

#### list_response_message

`list_response_message` 유형은 WhatsApp에서 목록 기반 메시지를 보낼 수 있습니다. 이 메시지 유형에는 수신자가 상호 작용할 수 있는 항목 목록이 포함되어 있습니다.

```json
{
  "header": (optional, string) the header of the message to send,
  "body": (required, string) the body of the message to send,
  "footer": (optional, string) the footer of the message to send,
  "list": (required, object) the list object that contains:
    "list_button_text": (required, string) the text that will appear on the list button,
    "list_sections": (required, array) an array of List Section Objects
}
```

#### 섹션 개체 나열

```json
{
  "section_title": (required, string) The title of the section,
  "list_rows": (required, array) An array of List Row Objects
}
```

#### 행 개체 나열

```json
{
  "row_title": (required, string) The title of the row,
  "row_description": (optional, string) The description for the row
}
```

##### 제약 조건

- **list_sections**: 섹션이 하나 이상 있어야 합니다.
- **list_rows**: 모든 섹션에 최대 10개의 행을 포함할 수 있습니다.
- **row_description**: 각 행에 대해 선택 사항입니다.

##### 예시

```json
{
  "body": "Here is a list of options to choose from:",
  "list": {
    "list_button_text": "Choose an option",
    "list_sections": [
      {
        "section_title": "Section 1",
        "list_rows": [
          {
            "row_title": "Option 1"
          },
          {
            "row_title": "Option 2",
            "row_description": "Description for Option 2"
          }
        ]
      },
      {
        "section_title": "Section 2",
        "list_rows": [
          {
            "row_title": "Option 3"
          },
          {
            "row_title": "Option 4"
          },
          {
            "row_title": "Option 5"
          }
        ]
      }
    ]
  }
}
```

#### flow_response_message

`flow_response_message` 유형을 사용하면 WhatsApp에서 플로우 기반 메시지를 보낼 수 있습니다. 이 메시지 유형에는 수신자가 완료할 수 있는 대화형 흐름이 포함됩니다.

```json
{
  "header_text": (optional, string) the header text of the message to send,
  "body": (required, string) the body of the message to send,
  "footer": (optional, string) the footer of the message to send,
  "flow_button": (required, object) the flow button object that contains:
    "caption": (required, string) the text that will appear on the flow button,
    "flow_id": (required, string) the unique identifier of the WhatsApp Flow,
  "generate_custom_attribute": (optional, boolean) whether to save flow response on the user profile and generate a custom attribute upon responding to this flow message
}
```

##### 흐름 버튼 개체

```json
{
  "caption": (required, string) The text displayed on the button,
  "flow_id": (required, string) The ID of the flow
}
```

##### 제약 조건

- **flow_button**: 캡션과 `flow_id` 를 모두 포함해야 합니다.
- **캡션**: 최대 20자까지 입력할 수 있습니다.
- **flow_id**: 유효한 게시된 Flow ID여야 합니다.

##### 예시

```json
{
  "body": "Please complete your order details",
  "flow_button": {
    "caption": "Start Order",
    "flow_id": "594425479261596"
  },
  "generate_custom_attribute": true
}
```
