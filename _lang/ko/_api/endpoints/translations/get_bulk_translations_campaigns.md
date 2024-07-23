---
nav_title: "GET: 캠페인의 번역 보기"
article_title: "GET: 캠페인의 번역 보기"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "이 문서에서는 캠페인 엔드포인트의 보기 번역에 대한 세부 정보를 간략하게 설명합니다."
---

{% api %}
# 캠페인의 번역 보기
{% apimethod get %}
/campaigns/translations
{% endapimethod %}

> 이 엔드포인트를 사용하여 캠페인의 각 메시지 변형에 대한 모든 번역을 볼 수 있습니다.

{% alert important %}
API를 통해 캠페인 메시지의 번역을 보는 것은 현재 얼리 액세스가 가능합니다. 얼리 액세스에 참여하고 싶다면 Braze 계정 관리자에게 문의하세요.
{% endalert %}

## 사전 요구 사항

이 엔드포인트를 사용하려면 `campaigns.translations.get` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key/)가 필요합니다.

## 사용량 제한

이 엔드포인트의 사용량 제한은 시간당 요청 250,000건입니다.

## 경로 매개변수

| 매개변수 | 필수 | 데이터 유형 | 설명 |
| --------- | ---------| --------- | ----------- |
`campaign_id`| | 캠페인 번역에 필요 | 문자열 | 캠페인 ID.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## 예제 요청

```
curl --location --request GET 'https://rest.iad-03.braze.com/campaign/translations' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## 응답

이 엔드포인트에는 `200`, `400`, `404`, `429`라는 네 가지 상태 코드 응답이 있습니다.

## 성공 응답 예시

`200` 상태 코드는 다음 응답 헤더와 본문을 반환할 수 있습니다.

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
	"translations": [
		{
			"locale": {
 				"name": "zh-HK",
 				"country": "Hong Kong",
 				"language": "Chinese (Traditional)",
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

## 오류 응답 예시

`400` 상태 코드는 다음 응답 본문을 반환할 수 있습니다. 발생할 수 있는 오류에 대한 자세한 내용은 [문제 해결을](#troubleshooting) 참조하십시오.

```json
{
	"errors": [
		{
			"message": "This message does not support multi-language."
		}
	]
}
```

## 문제 해결

다음 표에는 반환될 수 있는 오류와 관련 문제 해결 단계가 나와 있습니다.

| 오류 메시지 | 문제 해결 |
|---------------------------------|----------------------------------------------------------------------------|
| `INVALID_CAMPAIGN_ID`                   | 캠페인 ID가 번역 중인 캠페인과 일치하는지 확인합니다.                   |
| `INVALID_MESSAGE_VARIATION_ID` | 메시지 ID가 올바른지 확인하세요.|
| `MESSAGE_NOT_FOUND` | 번역할 메시지가 맞는지 확인하세요.|
| `MULTI_LANGUAGE_NOT_ENABLED`            | 워크스페이스에 다국어 설정이 켜져 있지 않습니다.                       |
| `MULTI_LANGUAGE_NOT_ENABLED_ON_MESSAGE` | 이메일 캠페인 또는 이메일이 포함된 Canvas 메시지만 번역할 수 있습니다.|
| `UNSUPPORTED_CHANNEL` | 이메일 캠페인의 메시지 또는 이메일이 포함된 Canvas 메시지만 번역할 수 있습니다.|
{: .reset-td-br-1 .reset-td-br-2}

{% endapi %}