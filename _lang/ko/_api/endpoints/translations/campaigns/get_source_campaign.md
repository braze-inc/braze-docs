---
nav_title: "GET: 캠페인 번역 태그의 기본값 보기"
article_title: "GET: 캠페인 번역 태그의 기본값 보기"
search_tag: Endpoint
page_order: 3

layout: api_page
page_type: reference
description: "이 문서에서는 캠페인 번역 소스 엔드포인트에 대한 자세한 내용을 설명합니다."
---

{% api %}
# 캠페인 번역 태그의 기본값 보기
{% apimethod get %}
/캠페인/번역/소스
{% endapimethod %}

> 이 엔드포인트를 사용하여 캠페인의 번역 태그에 대한 모든 기본값 번역 소스를 볼 수 있습니다. 다음은 {% raw %}`{% translation id %} source {% endtranslation %}`{% endraw %} 내의 값입니다. 번역 기능에 대한 자세한 내용은 [메시징의 로캘을]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/) 참조하세요.

{% alert important %}
이 엔드포인트는 현재 얼리 액세스 중입니다. Contact your Braze account manager if you're interested in participating in the early access.
{% endalert %}

## Prerequisites

이 엔드포인트를 사용하려면 `campaigns.translations.get` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key/)가 필요합니다.

## 사용량 제한

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## 쿼리 매개변수

| 매개변수 | 필수 | 데이터 유형 | 설명 |
| --------- | ---------| --------- | ----------- |
|`campaign_id`| Required | 문자열 | 캠페인의 ID입니다. |
|`message_variation_id`| Required | 문자열 | 메시지 변형의 ID입니다. |
|`locale_id`| Optional | 문자열 | 응답을 필터링할 로캘 UUID입니다. |
|`post_launch_draft_version`| 선택 사항 | 부울 | `true` 이 최신 라이브 게시 버전 대신 최신 초안 버전을 반환하는 경우. 기본값은 `false` 최신 라이브 버전을 반환합니다.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert note %}
모든 번역 ID는 GET 엔드포인트의 응답에서 찾을 수 있는 UUID(범용 고유 식별자)로 간주됩니다.
{% endalert %}

## 예시 요청

```
curl --location --request GET 'https://rest.iad-03.braze.com/campaigns/translations/source?campaign_id={campaign_id}&message_variation_id={message_variation_id}&locale_id={locale_uuid}&post_launch_draft_version=true' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## 응답

이 엔드포인트에 대한 상태 코드 응답은 `200`, `400`, `404`, `429` 의 네 가지가 있습니다.

### 성공 응답의 예

`200` 상태 코드는 다음과 같은 응답 헤더와 본문을 반환할 수 있습니다.

```json
{
   "translations": {
       "translation_map": {
           "id_0": "Here's a Million Dollars",
           "id_1": "Hello World!"
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
			"message": "This message does not support multi-language."
		}
	]
}
```

{% endapi %}
