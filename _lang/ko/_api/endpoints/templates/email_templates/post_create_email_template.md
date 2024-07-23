---
nav_title: "POST: 이메일 템플릿 생성"
article_title: "POST: 이메일 템플릿 만들기"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "이 문서에서는 이메일 템플릿 만들기 Braze 엔드포인트에 대해 자세히 설명합니다."
---
{% api %}
# 이메일 템플릿 생성
{% apimethod post %}
/templates/email/create
{% endapimethod %}

> 이 엔드포인트를 사용하여 Braze 대시보드에서 이메일 템플릿을 만듭니다. 

이 템플릿은 **템플릿 및 미디어** 페이지에서 사용할 수 있습니다. 이 엔드포인트의 응답에는 후속 API 호출에서 템플릿을 업데이트하는 데 사용할 수 있는 필드에 대한 `email_template_id`필드가 포함됩니다.

사용자의 이메일 구독 상태는 RESTful API를 사용하여 Braze를 통해 업데이트하고 검색할 수 있습니다. API를 사용하여 Braze와 다른 이메일 시스템 또는 자체 데이터베이스 간의 양방향 동기화를 설정할 수 있습니다. 모든 API 요청은 HTTPS를 통해 이루어집니다.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5eb1fe0d-2795-474d-aaf2-c4e2977dc94b {% endapiref %}

## 필수 구성 요소
이 엔드포인트를 사용하려면 `templates.email.create` 권한이 있는 [API 키]({{site.baseurl}}/api/api_key/)가 필요합니다.

## 사용량 제한

{% multi_lang_include rate_limits.md endpoint='default' %}

## 요청 본문

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
   "template_name": (required, string) The name of your email template,
   "subject": (required, string) The email template subject line,
   "body": (required, string) The email template body that may include HTML,
   "plaintext_body": (optional, string) A plaintext version of the email template body,
   "preheader": (optional, string) The email preheader used to generate previews in some clients,
   "tags": (optional, Array of Strings) Tags must already exist,
   "should_inline_css": (optional, Boolean) If `true`, the `inline_css` feature is used on this template.
 }
```

## 요청 매개 변수

| 매개 변수 | 필수 | 데이터형 | 설명 |
| --------- | ---------| --------- | ----------- |
|`template_name`|필수|문자열|이메일 템플릿의 이름입니다.|
|`subject`|필수|문자열|이메일 템플릿 제목입니다.|
|`body`|필수|문자열|HTML을 포함할 수 있는 이메일 템플릿 본문입니다.|
|`plaintext_body`|선택 사항|문자열|이메일 템플릿 본문의 일반 텍스트 버전입니다.|
|`preheader`|선택 사항|문자열|일부 클라이언트에서 미리보기를 생성하는 데 사용되는 이메일 프리헤더.|
|`tags`|선택 사항|문자열|[태그]({{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/tags/) 가 이미 있어야 합니다.|
|`should_inline_css`|선택 사항|부울 |템플릿당 `inline_css` 기능을 사용하거나 사용하지 않도록 설정합니다. 제공되지 않은 경우 Braze는 앱 그룹의 기본 설정을 사용합니다. `true` 또는 `false` 중 하나가 예상됩니다.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}


## 요청 예시
```
curl --location --request POST 'https://rest.iad-01.braze.com/templates/email/create' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "template_name": "email_template_name",
  "subject": "Welcome to my email template!",
  "body": "This is the text within my email body and https://www.braze.com/ here is a link to Braze.com.",
  "plaintext_body": "This is the text within my email body and here is a link to https://www.braze.com/.",
  "preheader": "My preheader is pretty cool.",
  "tags": ["Tag1", "Tag2"]
}'
```

## 가능한 오류

다음 표에는 반환될 수 있는 오류 및 관련 문제 해결 단계(해당하는 경우)가 나와 있습니다.

| 오류 | 문제 해결 |
| --- | --- |
| 템플릿 이름은 필수입니다 | 템플릿 이름을 입력합니다. |
| 태그는 배열이어야 합니다. 태그는 문자열 배열로 형식이 지정되어야 합니다(예: `["marketing", "promotional", "transactional"]`. |
| 모든 태그는 문자열이어야 합니다. 태그가 따옴표(`""`)로 캡슐화되어 있는지 확인합니다. |
| 일부 태그를 찾을 수 없습니다 | 이메일 템플릿을 만들 때 태그를 추가하려면 태그가 이미 Braze에 존재해야 합니다. |
| 이메일에는 유효한 콘텐츠 블록 이름이 있어야 합니다. 이메일에는 이 환경에 존재하지 않는 콘텐츠 블록이 포함될 수 있습니다. |
| `should_inline_css`의 값이 잘못되었습니다. `true` 또는 `false` 중 하나가 예상됨 | 이 매개 변수는 부울 값(true 또는 false)만 허용합니다. `should_inline_css` 값이 따옴표(`""`)로 캡슐화되지 않았는지 확인하여 값이 대신 문자열로 전송되도록 합니다.|
{: .reset-td-br-1 .reset-td-br-2}

{% endapi %}
