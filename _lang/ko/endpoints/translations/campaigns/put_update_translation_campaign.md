---
nav_title: "PUT: 캠페인에서 번역 업데이트"
article_title: "PUT: 캠페인에서 번역 업데이트"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "이 기사는 캠페인 엔드포인트에서 업데이트 번역에 대한 세부 정보를 설명합니다."
---

{% api %}
# 캠페인에서 번역 업데이트
{% apimethod put %}
/campaigns/translations
{% endapimethod %}

> 이 엔드포인트를 사용하여 캠페인의 여러 번역을 업데이트할 수 있습니다.

캠페인이 시작된 후 번역을 업데이트하려면 먼저 [메시지를 초안으로 저장]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/change_your_campaign_after_launch/)해야 합니다.

{% alert important %}
이 엔드포인트는 현재 얼리 액세스 중입니다. Contact your Braze account manager if you're interested in participating in the early access.
{% endalert %}

## Prerequisites

이 엔드포인트를 사용하려면 `campaigns.translations.update` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key/)가 필요합니다.

## 사용량 제한

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## 경로 매개변수

이 엔드포인트에는 경로 매개 변수가 없습니다.

## 요청 매개변수

| 매개변수 | 필수 | 데이터 유형 | 설명 |
| --------- | ---------| --------- | ----------- |
| `campaign_id` | Required | 문자열 | 캠페인의 ID입니다. |
| `message_variation_id` | Required | 문자열 | 메시지 변형의 ID입니다. |
| `locale_name` | Required | 문자열 | 로캘의 이름입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

모든 번역 ID는 보편적인 고유 식별자(UUID)로 간주되며, 이는 **다국어 지원** 설정 또는 GET 요청 응답에서 찾을 수 있습니다.

## 예시 요청

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "campaign_id": "e24404b3-3626-4de0-bdec-06935f3aa0ab", // CAMPAIGNS ONLY
    "message_variation_id": "f14404b3-3626-4de0-bdec-06935f3aa0ad",
    "locale_id": "h94404b3-3626-4de0-bdec-06935f3aa0ad",
    "translation_map": {
        "id_3": "Ein Absatz ohne Formatierung"
    }
}
```

## 응답

이 엔드포인트에 대한 상태 코드 응답은 `200`, `400`, `404`, `429` 의 네 가지가 있습니다.

### 성공 응답의 예

```json
{
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

| 오류 메시지  | 문제 해결 |
|----|----------|
| `The provided translations yielded errors when parsing. Please contact Braze for more information.` | 타사 번역가가 Liquid 오류를 생성하는 예외가 있는 번역을 제공할 때 발생합니다. 추가 지원이 필요하면 Braze 지원팀에 문의하세요. |
| `The provided translations are missing 'id_1', 'id_2'` | 번역 ID가 일치하지 않거나 번역된 텍스트가 한도를 초과합니다. 예를 들어, 이는 페이로드 모양에 번역 객체의 필드가 누락되었음을 의미할 수 있습니다. 모든 메시지(다국어 사용 설정 시)에는 ID가 연결된 특정 수의 '번역 블록'이 있어야 합니다. 제공된 페이로드에 ID가 하나라도 누락된 경우 불완전한 객체로 간주되어 오류가 발생합니다. |
| `The provided locale code does not exist.` | 타사 번역기의 페이로드에는 Braze에 존재하지 않는 로캘 코드가 포함되어 있습니다. |
| `The provided translations have exceeded the maximum of 20MB.` | 제공된 페이로드가 크기 제한을 초과합니다. |
| `You have exceeded the maximum number of requests. Please try again later.` | 모든 Braze API에는 속도 제한 기능이 내장되어 있으며, 이 오류는 이 인증 토큰에 할당된 양을 초과하면 자동으로 반환됩니다. |
| `This message does not support multi-language.` | 메시지 ID가 아직 다국어 메시지를 지원하지 않는 경우 이 문제가 발생할 수 있습니다. 푸시, 인앱 메시지, 이메일 등 다음 채널의 메시지만 번역할 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
