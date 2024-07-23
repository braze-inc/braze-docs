---
nav_title: "PUT: 캠페인에서 번역 업데이트"
article_title: "PUT: 캠페인에서 번역 업데이트"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "이 문서에서는 캠페인 엔드포인트의 업데이트 번역에 대한 세부 정보를 간략하게 설명합니다."
---

{% api %}
# 캠페인에서 번역 업데이트
{% apimethod put %}
/campaigns/translations
{% endapimethod %}

> 이 엔드포인트를 사용하여 캠페인의 여러 번역을 업데이트합니다.

{% alert important %}
API를 통한 캠페인 번역 업데이트는 현재 얼리 액세스가 가능합니다. 얼리 액세스에 참여하고 싶다면 Braze 계정 관리자에게 문의하세요.
{% endalert %}

## 사전 요구 사항

이 엔드포인트를 사용하려면 `campaigns.translations.update` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key/)가 필요합니다.

## 사용량 제한

이 엔드포인트의 사용량 제한은 시간당 요청 250,000건입니다.

## 경로 매개변수

이 엔드포인트에는 경로 매개변수가 없습니다.

## 요청 매개변수

| 매개변수 | 필수 | 데이터 유형 | 설명 |
| --------- | ---------| --------- | ----------- |
| `locale_id` | 필수 | 문자열 | 로캘의 ID입니다.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## 예제 요청

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "campaign_id": "9a0ba932-11c0-4c33-b529-e79aafc12409",
    "message_variation_id": "f5896eec-847d-4c0d-a4b6-7695e67520d7",
    "locale_id": "3fa10d31-83ae-4ff4-9631-f52cea9ec8fa",
    "translation_map": {
        "id_4": "¿Dónde está la biblioteca? Me llamo T-Bone, La araña discoteca.",
        "subject_1": "¿Dónde está la biblioteca? Me llamo T-Bone, La araña discoteca.",
        "id_1": "¿Dónde está la biblioteca? Me llamo T-Bone, La araña discoteca.",
        "image": "¿Dónde está la biblioteca? Me llamo T-Bone, La araña discoteca."
    }
}
```

## 성공 응답 예시

```json
{
	"message": "success"
}
```

### 오류 응답 예시

`400` 상태 코드는 다음 응답 본문을 반환할 수 있습니다. 발생할 수 있는 오류에 대한 자세한 내용은 [문제 해결을](#troubleshooting) 참조하십시오.

```json
{
	"errors": [
		{
			"message": "Something went wrong. Translation IDs are mismatched or translated text exceeds limits."
		}
	]
}
```


## 문제 해결

다음 표에는 반환될 수 있는 오류와 관련 문제 해결 단계가 나와 있습니다.

| 오류 메시지 | 문제 해결 |
|---------------------------------|----------------------------------------------------------------------------|
| `INVALID_CAMPAIGN_ID`                   | 캠페인 ID가 번역 중인 캠페인과 일치하는지 확인합니다.                   |
| `INVALID_LOCALE_ID`                     | 메시지 번역에 로캘 ID가 있는지 확인합니다.                         |
| `INVALID_MESSAGE_VARIATION_ID` | 메시지 ID가 올바른지 확인하세요.|
| `INVALID_TRANSLATION_OBJECT` | 번역 ID가 일치하지 않거나 번역된 텍스트가 한도를 초과합니다.|
| `MESSAGE_NOT_FOUND` | 번역할 메시지가 맞는지 확인하세요.|
| `LOCALE_NOT_FOUND`                      | 다국어 설정에 로캘이 있는지 확인합니다.                         |
| `MISSING_TRANSLATIONS` | 번역 ID는 메시지와 일치해야 합니다.|
| `MULTI_LANGUAGE_NOT_ENABLED`            | 워크스페이스에 다국어 설정이 켜져 있지 않습니다.                       |
| `MULTI_LANGUAGE_NOT_ENABLED_ON_MESSAGE` | 이메일 캠페인 또는 이메일이 포함된 Canvas 메시지만 번역할 수 있습니다.|
| `UNSUPPORTED_CHANNEL` | 이메일 캠페인의 메시지 또는 이메일이 포함된 Canvas 메시지만 번역할 수 있습니다.|
{: .reset-td-br-1 .reset-td-br-2}

{% endapi %}