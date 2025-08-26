---
nav_title: "GET: 캔버스에 대한 번역 보기"
article_title: "GET: 캔버스에 대한 번역 보기"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "이 문서에서는 캔버스 엔드포인트의 보기 번역에 대한 자세한 내용을 설명합니다."
---

{% api %}
# 캔버스에 대한 번역 보기
{% apimethod get %}
/canvas/translations/?locale_id={locale_id}
{% endapimethod %}

> 이 엔드포인트를 사용하여 번역된 메시지를 보고 이 메시지가 사용자에게 어떻게 보이는지 확인할 수 있습니다.

{% alert important %}
API를 통해 캔버스에 대한 번역된 메시지를 보는 기능은 현재 얼리 액세스 중입니다. 얼리 액세스에 참여하려면 Braze 계정 매니저에게 문의하세요.
{% endalert %}

## 필수 구성 요소

이 엔드포인트를 사용하려면 `canvas.translations.get` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key/)가 필요합니다.

## 사용량 제한

이 엔드포인트는 시간당 250,000개의 요청에 대한 속도 제한이 있습니다.

## 경로 매개변수

| 매개변수 | 필수 | 데이터 유형 | 설명 |
| --------- | ---------| --------- | ----------- |
|`step_id`| 필수 | 문자열 | 캔버스 단계의 ID입니다. |
|`message_variation_id`| 필수 | 문자열 | 메시지 변형을 위한 ID입니다. |
|`locale_id`| 필수 | 문자열 | 로캘의 ID입니다. |
|`workflow_id` | 필수 | 문자열 | 캔버스의 ID입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

모든 번역 ID는 **다국어 지원** 설정이나 요청 응답에서 찾을 수 있는 UUID(범용 고유 식별자)로 간주된다는 점에 유의하세요.

## 요청 예시

```
curl --location --request GET 'https://rest.iad-03.braze.com/canvas/translations/?locale_id={locale_id}' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## 응답

이 엔드포인트에 대한 상태 코드 응답은 `200`, `400`, `404`, `429` 의 네 가지가 있습니다.

## 성공 응답의 예

`200` 상태 코드는 다음과 같은 응답 헤더와 본문을 반환할 수 있습니다.

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
	"translations": [
		{
			"locale": {
 				"name": "es-MX",
 				"country": "Mexico",
 				"language": "Spanish",
			},
			"translation_map": {
				"id_0": "Hello",
				"id_1": "My name is Jacky",
				"id_2": "Where is the library?"
			}
		}
	]
}
```

### 오류 응답의 예

`400` 상태 코드는 다음과 같은 응답 본문을 반환할 수 있습니다. 발생할 수 있는 오류에 대한 자세한 내용은 [문제 해결을](#troubleshooting) 참조하세요.

```json
{
	"errors": [
		{
			"message": "Invalid locale ID"
		}
	]
}
```

## 문제 해결

다음 표에는 반환될 수 있는 오류와 관련 문제 해결 단계가 나와 있습니다.

| 오류 메시지                           | 문제 해결                                                                    |
|-----------------------------------------|------------------------------------------------------------------------------------|
| `INVALID_CAMPAIGN_ID`                   | 캠페인 ID가 번역 중인 캠페인과 일치하는지 확인합니다.                   |
| `INVALID_LOCALE_ID`                     | 메시지 번역에 로캘 ID가 있는지 확인합니다.                         |
| `INVALID_MESSAGE_VARIATION_ID`          | 메시지 ID가 올바른지 확인합니다.                                                |
| `MESSAGE_NOT_FOUND`                     | 번역할 메시지를 확인합니다.                                           |
| `LOCALE_NOT_FOUND`                      | 다국어 설정에 로캘이 있는지 확인합니다.                         |
| `MULTI_LANGUAGE_NOT_ENABLED`            | 작업 공간에 대한 다국어 설정이 켜져 있지 않습니다.                       |
| `MULTI_LANGUAGE_NOT_ENABLED_ON_MESSAGE` | 이메일 캠페인 또는 이메일이 포함된 캔버스 메시지만 번역할 수 있습니다.             |
| `UNSUPPORTED_CHANNEL`                   | 이메일 캠페인의 메시지 또는 이메일이 포함된 캔버스 메시지만 번역할 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
