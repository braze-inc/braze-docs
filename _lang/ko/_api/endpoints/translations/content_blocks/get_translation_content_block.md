---
nav_title: "GET: 콘텐츠 블록에 대한 모든 번역 보기"
article_title: "GET: 콘텐츠 블록에 대한 모든 번역 보기"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "이 문서에서는 콘텐츠 블록에 대한 모든 번역 보기 엔드포인트에 대한 세부 정보를 설명합니다."
---

{% api %}
# 콘텐츠 블록에 대한 모든 번역 보기
{% apimethod get %}
/content_blocks/translations
{% endapimethod %}

> 이 엔드포인트를 사용하여 [콘텐츠 블록]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/)에 대한 모든 번역을 볼 수 있습니다. 번역 기능에 대한 자세한 내용은 [메시지의 로케일]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/)를 참조하십시오.

{% include early_access_beta_alert.md feature='This endpoint' %}

## Prerequisites

이 엔드포인트를 사용하려면 `content_blocks.translations.get` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key/)가 필요합니다.

## 사용량 제한

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## 쿼리 매개변수

| 매개변수 | 필수 | 데이터 유형 | 설명 |
| --------- | ---------| --------- | ----------- |
|`content_block_id`| Required | 문자열 | 귀하의 콘텐츠 블록의 ID입니다. |
|`locale_id`| Optional | 문자열 | 응답을 필터링할 로케일 UUID입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert note %}
모든 번역 ID는 보편적 고유 식별자(UUID)로 간주되며, GET 엔드포인트의 응답에서 찾을 수 있습니다.
{% endalert %}

## 예시 요청

```
curl --location --request GET 'https://rest.iad-03.braze.com/content_blocks/translations?content_block_id={content_block_id}&locale_id={locale_uuid}' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## 응답

이 엔드포인트에 대한 상태 코드 응답은 `200`, `400`, `404`, `429` 의 네 가지가 있습니다.

### 성공 응답의 예

`200` 상태 코드는 다음과 같은 응답 헤더와 본문을 반환할 수 있습니다.

```json
{
    "translations": [
        {
            "translation_map": {
                "id_0": "¡Hola!",
                "id_1": "Me llamo Jacky",
                "id_2": "¿Dónde está la biblioteca?"
            },
            "locale": {
                "uuid": "c7c12345-te35-1234-5678-abcdefa99r3f",
                "name": "es-MX",
                "country": "MX",
                "language": "es",
                "locale_key": "es-mx"
            }
        },
        {
            "translation_map": {
                "id_0": "你好",
                "id_1": "我的名字是 Jacky",
                "id_2": "圖書館在哪裡?"
            },
            "locale": {
                "uuid": "a1b12345-cd35-1234-5678-abcdefa99r3f",
                "name": "zh-HK",
                "country": "HK",
                "language": "zh",
                "locale_key": "zh-hk"
            }
        }
    ]
}
```

### 오류 응답의 예

`400` 상태 코드는 다음과 같은 응답 본문을 반환할 수 있습니다.

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
