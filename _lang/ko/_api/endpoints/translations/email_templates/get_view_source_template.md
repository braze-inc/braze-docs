---
nav_title: "GET: 이메일 템플릿에 대한 소스 번역 보기"
article_title: "GET: 이메일 템플릿에 대한 소스 번역 보기"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "이 문서에서는 이메일 템플릿 엔드포인트에 대한 소스 번역 보기의 세부 정보를 설명합니다."
---

{% api %}
# 이메일 템플릿에 대한 소스 번역 보기
{% apimethod get %}
/templates/email/translations/source
{% endapimethod %}

> 이 엔드포인트를 사용하여 [이메일 템플릿]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates)에 대한 소스 번역을 볼 수 있습니다.

{% alert important %}
이 엔드포인트는 현재 얼리 액세스 중입니다. Contact your Braze account manager if you're interested in participating in the early access.
{% endalert %}

## Prerequisites

이 엔드포인트를 사용하려면 `templates.email.info` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key/)가 필요합니다.

## 사용량 제한

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## 쿼리 매개변수

| 매개변수     | 필수 | 데이터 유형 | 설명                     |
|---------------|----------|-----------|---------------------------------|
| `template_id` | 필수 | 문자열    | 이메일 템플릿의 ID입니다. |
| `locale_id`   | 필수 | 문자열    | 로캘의 ID입니다.           |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

모든 번역 ID는 **다국어 지원** 설정이나 요청 응답에서 찾을 수 있는 UUID(범용 고유 식별자)로 간주된다는 점에 유의하세요.

## 예시 요청

```
curl --location --request GET 'https://rest.iad-03.braze.com/templates/email/translations/source' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## 응답

이 엔드포인트에 대한 상태 코드 응답은 `200`, `400`, `404`, `429` 의 네 가지가 있습니다.

### 성공 응답의 예

`200` 상태 코드는 다음과 같은 응답 헤더와 본문을 반환할 수 있습니다.

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "translations": {
        "translation_map": {
            "id_0": "Here's a limited time offer for your membership tier!",
            "id_1": "Welcome to a new fashion-forward season!"
        }
    },
    "message": "success"
}
```

### 오류 응답의 예

`400` 상태 코드는 다음과 같은 응답 본문을 반환할 수 있습니다. 발생할 수 있는 오류에 대한 자세한 내용은 [문제 해결을](#troubleshooting) 참조하세요.

```json
{
    "errors": [
        {
            "message": "The provided locale code does not exist."
        }
    ]
}
```

## 문제 해결

다음 표에는 반환될 수 있는 오류와 관련 문제 해결 단계가 나와 있습니다.

| 오류 메시지                           | 문제 해결                                                                    |
|-----------------------------------------|------------------------------------------------------------------------------------|
| `INVALID_LOCALE_ID`                     | 메시지 번역에 로캘 ID가 있는지 확인합니다.                         |
| `LOCALE_NOT_FOUND`                      | 다국어 설정에 로캘이 있는지 확인합니다.                         |
| `MULTI_LANGUAGE_NOT_ENABLED`            | 작업 공간에 대한 다국어 설정이 켜져 있지 않습니다.                       |
| `MULTI_LANGUAGE_NOT_ENABLED_ON_MESSAGE` | 이메일 템플릿과 이메일, 푸시, 인앱 메시지 캠페인 또는 이메일이 포함된 캔버스 메시지만 번역할 수 있습니다.             |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
