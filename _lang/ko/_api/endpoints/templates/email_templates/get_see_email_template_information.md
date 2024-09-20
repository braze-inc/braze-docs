---
nav_title: "GET: 이메일 템플릿 정보 보기"
article_title: "GET: 이메일 템플릿 정보 보기"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "이 문서에서는 이메일 템플릿 Braze 엔드포인트 참조에 대한 세부 정보를 간략하게 설명합니다."

---
{% api %}
# 이메일 템플릿 정보 보기
{% apimethod get %}
/templates/email/info
{% endapimethod %}

> 이 엔드포인트를 사용하여 이메일 템플릿에 대한 정보를 가져옵니다.

{% alert important %}
이메일용 드래그 앤 드롭 편집기를 사용하여 작성된 템플릿은 허용되지 않습니다.
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#e98d2d5b-62fe-4358-b391-9fe9e460d0ac {% endapiref %}

## 필수 구성 요소
이 엔드포인트를 사용하려면 `templates.email.info` 권한이 있는 [API 키]({{site.baseurl}}/api/api_key/)가 필요합니다.

## 사용량 제한

{% multi_lang_include rate_limits.md endpoint='default' %}

## 요청 매개 변수

| 매개 변수 | 필수 | 데이터형 | 설명 |
|---|---|---|---|
| `email_template_id`  | 필수 | 문자열 | [이메일 템플릿 API 식별자]({{site.baseurl}}/api/identifier_types/)를 참조하십시오. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## 요청 예시
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/templates/email/info?email_template_id={{email_template_id}}' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'
```
{% endraw %}

## 응답 

```json
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
{
  "email_template_id": (string) Your email template's API Identifier,
  "template_name": (string) The name of your email template,
  "description": (string) The email template description,
  "subject": (string) The email template subject line,
  "preheader": (optional, string) The email preheader used to generate previews in some clients),
  "body": (optional, string) The email template body that may include HTML,
  "plaintext_body": (optional, string) A plaintext version of the email template body,
  "should_inline_css": (optional, boolean) Whether there is inline CSS in the body of the template - defaults to the css inlining value for the workspace,
  "tags": (string) Tag names,
  "created_at": (string) The time the email was created at in ISO 8601,
  "updated_at": (string) The time the email was updated in ISO 8601
}
```

이 응답의 이미지는 `body` 변수에 HTML로 표시됩니다.

{% endapi %}
