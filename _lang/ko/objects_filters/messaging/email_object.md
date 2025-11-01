---
nav_title: "이메일 개체"
article_title: 이메일 메시징 개체
page_order: 5
page_type: reference
channel: email
description: "이 참조 문서에서는 Braze 이메일 객체의 다양한 구성 요소에 대해 설명합니다."

---

# 이메일 개체

> `email` 개체를 사용하면 [메시징 엔드포인트를]({{site.baseurl}}/api/endpoints/messaging) 통해 이메일을 수정하거나 생성할 수 있습니다.

## 이메일 개체

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
  "headers": (optional, valid Key-Value Hash) hash of custom extensions headers (available for SparkPost, SendGrid, or Amazon SES),
  "should_inline_css": (optional, boolean) whether to inline CSS on the body. If not provided, falls back to the default CSS inlining value for the workspace,
  "attachments": (optional, array) array of JSON objects that define the files you need attached, defined by "file_name" and "url",
    "file_name": (required, string) the name of the file you want to attach to your email, excluding the extension (for example, ".pdf"). Attach files up to 2 MB. This is required if you use "attachments",
    "url": (required, string) the corresponding URL of the file you want to attach to your email. The file name's extension will be detected automatically from the URL defined, which should return the appropriate "Content-Type" as a response header. This is required if you use "attachments",
}
```

- [App identifier]({{site.baseurl}}/api/identifier_types/)
  - 워크스페이스에 구성된 앱의 유효한 `app_id` 은 사용자의 프로필에 특정 앱이 있는지 여부에 관계없이 워크스페이스의 모든 사용자에게 적용됩니다.
- 프리헤더에 대한 자세한 정보와 모범 사례는 [이메일 본문 스타일]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/guidelines_and_tips/#body-styling) 지정에 대한 도움말 문서를 참조하세요.

{% alert warning %}
첨부파일의 `url` 에 Google 드라이브 링크를 사용하면 파일을 가져오기 위한 서버의 호출이 차단되어 이메일 메시지가 전송되지 않을 수 있으므로 사용하지 않는 것이 좋습니다.
{% endalert %}

유효한 첨부 파일 유형은 다음과 같습니다: `txt`, `csv`, `log`, `css`, `ics`, `jpg`, `jpe`, `jpeg`, `gif`, `png`, `bmp`, `psd`, `tif`, `tiff`, `svg`, `indd`, `ai`, `eps`, `doc`, `docx`, `rtf`, `odt`, `ott`, `pdf`, `pub`, `pages`, `mobi`, `epub`, `mp3`, `m4a`, `m4v`, `wma`, `ogg`, `flac`, `wav`, `aif`, `aifc`, `aiff`, `mp4`, `mov`, `avi`, `mkv`, `mpeg`, `mpg`, `wmv`, `xls`, `xlsx`, `ods`, `numbers`, `odp`, `ppt`, `pptx`, `pps`, `key`, `zip`, `vcf`, `pkpass`, 그리고 .

`email_template_id` 은 HTML 편집기로 만든 이메일 템플릿의 하단에서 검색할 수 있습니다. 다음은 이 ID가 어떻게 보이는지 보여주는 예입니다:

![HTML 이메일 템플릿의 API 식별자 섹션입니다.]({% image_buster /assets/img_archive/email_template_id.png %}){: style="max-width:70%;"} 

## 첨부 파일이 있는 이메일 개체 예시

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

## 이메일 첨부 파일에 대한 인증

1. **설정** > **연결된 콘텐츠로** 이동하고 **자격 증명 추가를** 클릭하여 인증 자격 증명을 추가합니다.
2. 이름을 입력하고 사용자 아이디와 비밀번호를 추가합니다.
3. `/messages/send` 엔드포인트의 이메일 개체에 첨부 파일 세부 정보에 자격 증명 이름을 지정하는 `basic_auth_credential` 속성을 포함하세요. 자격증명 이름이 `company_basic_auth_credential_name` 인 다음 예시를 참조하세요:

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

