---
nav_title: "POST: 이메일 템플릿 업데이트"
article_title: "POST: 이메일 템플릿 업데이트"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "이 문서에서는 업데이트 이메일 템플릿 Braze 엔드포인트에 대한 자세한 내용을 설명합니다."

---
{% api %}
# 기존 이메일 템플릿 업데이트
{% apimethod post %}
/templates/email/update
{% endapimethod %}

> 이 엔드포인트를 사용하여 Braze 대시보드에서 이메일 템플릿을 업데이트하세요.

**템플릿 & 미디어** 페이지에서 이메일 템플릿의 `email_template_id` 으로 이동하여 액세스할 수 있습니다. [이메일 템플릿 만들기 엔드포인트는]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template/) `email_template_id` 참조도 반환합니다.

`email_template_id` 이외의 모든 필드는 선택 사항이지만 업데이트할 필드를 하나 이상 지정해야 합니다.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#afb25494-3350-458d-932d-5bf4220049fa {% endapiref %}

## Prerequisites
이 엔드포인트를 사용하려면 `templates.email.update` 권한이 있는 [API 키]({{site.baseurl}}/api/api_key/)가 필요합니다.

## 사용량 제한

{% multi_lang_include rate_limits.md endpoint='default' %}

## 요청 본문

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "email_template_id": (required, string) Your email template's API Identifier,
  "template_name": (optional, string) The name of your email template,
  "subject": (optional, string) The email template subject line,
  "body": (optional, string) The email template body that may include HTML,
  "plaintext_body": (optional, string) A plaintext version of the email template body,
  "preheader": (optional, string) The email preheader used to generate previews in some clients,
  "tags": (optional, array of Strings) Tags must already exist,
  "should_inline_css": (optional, Boolean) If `true`, the `inline_css` feature will be applied to the template.
}
```

## 요청 매개변수

| 매개변수 | 필수 | 데이터 유형 | 설명 |
| --------- | ---------| --------- | ----------- |
|`email_template_id`| Required |문자열|[이메일 템플릿의 API 식별자입니다]({{site.baseurl}}/api/identifier_types/).|
|`template_name`|Optional|문자열|이메일 템플릿의 이름입니다.|
|`subject`|Optional|문자열|이메일 템플릿 제목.|
|`body`|Optional|문자열|HTML을 포함할 수 있는 이메일 템플릿 본문입니다.|
|`plaintext_body`|Optional|문자열|이메일 템플릿 본문의 일반 텍스트 버전입니다.|
|`preheader`|Optional|문자열|일부 클라이언트에서 미리보기를 생성하는 데 사용되는 이메일 프리헤더입니다.|
|`tags`|Optional|문자열|[태그가]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) 이미 존재해야 합니다.|
|`should_inline_css`|선택 사항|부울|템플릿별로 `inline_css` 기능을 사용하거나 사용하지 않도록 설정합니다. 제공하지 않으면 Braze는 앱그룹에 대한 기본 설정을 사용합니다. `true` 또는 `false` 중 하나가 예상됩니다.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 예시 요청
```
curl --location --request POST 'https://rest.iad-01.braze.com/templates/email/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "email_template_id": "email_template_id",
  "template_name": "Weekly Newsletter",
  "subject": "This Week'\''s Styles",
  "body": "Check out this week'\''s digital lookbook to inspire your outfits. Take a look at https://www.braze.com/",
  "plaintext_body": "This is the updated text within my email body and here is a link to https://www.braze.com/.",
  "preheader": "We want you to have the best looks this summer",
  "tags": ["Tag1", "Tag2"]
}'
```

## 문제 해결

다음 표에는 해당하는 경우 반환될 수 있는 오류 및 관련 문제 해결 단계가 나와 있습니다.

| 오류 | 문제 해결 |
| --- | --- |
| 템플릿 이름은 필수 항목입니다. | 템플릿 이름을 입력합니다. |
| 태그는 배열이어야 합니다. | 태그의 형식은 문자열 배열로 지정해야 합니다(예: `["marketing", "promotional", "transactional"]`). |
| 모든 태그는 문자열이어야 합니다. | 태그가 따옴표로 묶여 있는지 확인합니다(`""`). |
| 일부 태그를 찾을 수 없습니다. | 이메일 템플릿을 만들 때 태그를 추가하려면 해당 태그가 이미 Braze에 존재해야 합니다. |
| `should_inline_css` 에 대한 잘못된 값입니다. `true` 또는 `false` 중 하나가 예상되었습니다. | 이 매개변수는 부울 값(참 또는 거짓)만 허용합니다. `should_inline_css` 값이 따옴표(`""`)로 묶이지 않았는지 확인하여 값이 문자열로 대신 전송되도록 합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
