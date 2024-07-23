---
nav_title: "GET: 캔버스에 대한 번역 보기"
article_title: "GET: 캔버스에 대한 번역 보기"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "이 문서에서는 캔버스 엔드포인트의 목록 번역에 대한 자세한 내용을 설명합니다."
---

{% api %}
# 캔버스에 대한 번역 목록
{% apimethod get %}
/canvases/translations
{% endapimethod %}

> 이 엔드포인트를 사용하여 캔버스에 대한 모든 번역을 볼 수 있습니다.

{% alert important %}
API를 통해 캔버스에 대한 번역 보기는 현재 얼리 액세스 중입니다. 얼리 액세스에 참여하려면 Braze 계정 매니저에게 문의하세요.
{% endalert %}

## 전제 조건

이 엔드포인트를 사용하려면 `canvas.translations.get` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key/)가 필요합니다.

## 요금 제한

이 엔드포인트의 사용량 제한은 시간당 250,000건의 요청입니다.

## 경로 매개변수

| 매개변수 | 필수 | 데이터 유형 | 설명 | 설명
| --------- | ---------| --------- | ----------- |
|`canvas_id`| 필수 | 문자열 | 캔버스의 ID입니다. |
|`step_id`| 필수 | 문자열 | 캔버스 단계의 ID입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## 요청 예시

```
curl --location --request GET 'https://rest.iad-03.braze.com/canvas/translations' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## 응답

이 엔드포인트에 대한 상태 코드 응답은 `200`, `400`, `404`, `429` 등 네 가지가 있습니다.

## 성공 응답 예시

`200` 상태 코드는 다음과 같은 응답 헤더와 본문을 반환할 수 있습니다.

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

`400` 상태 코드는 다음과 같은 응답 본문을 반환할 수 있습니다. 발생할 수 있는 오류에 대한 자세한 내용은 [문제 해결을](#troubleshooting) 참조하세요.

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

| 오류 메시지 | 문제 해결 | 도움말
|-----------------------------------------|------------------------------------------------------------------------------------|
| `INVALID_CAMPAIGN_ID`                   | 캠페인 ID가 번역 중인 캠페인과 일치하는지 확인합니다.                   |
| `INVALID_MESSAGE_VARIATION_ID` | 메시지 ID가 올바른지 확인합니다.                                                |
| `MESSAGE_NOT_FOUND` | 번역할 메시지를 확인합니다.                                           |
| `MULTI_LANGUAGE_NOT_ENABLED`            | 워크스페이스에 대한 다국어 설정이 켜져 있지 않습니다.                       |
| `MULTI_LANGUAGE_NOT_ENABLED_ON_MESSAGE` | 이메일 캠페인 또는 이메일이 포함된 캔버스 메시지만 번역할 수 있습니다.             |
| `UNSUPPORTED_CHANNEL` | 이메일 캠페인의 메시지 또는 이메일이 포함된 캔버스 메시지만 번역할 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2}

{% endapi %}