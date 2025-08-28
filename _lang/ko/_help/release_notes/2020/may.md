---
nav_title: 5월
page_order: 8
noindex: true
page_type: update
description: "이 문서에는 2020년 5월 릴리스 노트가 포함되어 있습니다."
---
# 2020년 5월

## Google Tag Manager

[Google Tag Manager]({{site.baseurl}}/developer_guide/sdk_initalization/?sdktab=android)를 사용하여 Braze의 Android 소프트웨어 개발 키트를 배포하고 관리하는 방법에 대한 설명서 및 예제가 추가되었습니다.

## 새로운 블랙리스트 이메일 API 엔드포인트

이제 Braze API를 통해 이메일 주소를 [블랙리스트에 추가]({{site.baseurl}}/api/endpoints/email/post_blacklist/)할 수 있습니다. 이메일 주소를 블랙리스트에 추가하면 사용자가 이메일에서 탈퇴하고 하드바운스로 표시됩니다.

## Braze API 엔드포인트에 대한 API 키 변경

2020년 5월부터 Braze는 API 키를 읽는 방식을 더 안전하게 변경했습니다. 이제 API 키는 요청 헤더로 전달되어야 합니다. 예제는 **예제 요청** 아래의 개별 엔드포인트 페이지와 **API 키 설명**에서 찾을 수 있습니다.

Braze는 요청 본문과 URL 매개변수를 통해 전달되는 `api_key`를 계속 지원할 것이지만, 결국에는 중단될 예정입니다(TBD). **API 호출을 적절히 업데이트하세요.** 이러한 변경 사항은 [Postman](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#intro) 내에서 업데이트되었습니다.
{% details API 키 설명 %}
{% tabs %}
{% tab GET 요청 %}
이 예제는 `/email/hard_bounces` 엔드포인트를 사용합니다.

**이전: 요청 본문의 API 키**
```
curl --location --request GET 'https://rest.iad-01.braze.com/email/hard_bounces?api_key={YOUR_REST_API_KEY}&start_date=2019-01-01&end_date=2019-02-01&limit=100&offset=1&email=foo@braze.com' \
```
**지금: 헤더의 API 키**
```
curl --location --request GET 'https://rest.iad-01.braze.com/email/hard_bounces?start_date=2019-01-01&end_date=2019-02-01&limit=100&offset=1&email=foo@braze.com' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endtab %}
{% tab POST 요청 %}
이 예제는 `/user/track` 엔드포인트를 사용합니다.

**이전: 요청 본문의 API 키**
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--data-raw '{
	"api_key": YOUR-API-KEY-HERE ,
	"attributes": [ 
 	{
 	  "external_id":"user_id",
      "string_attribute": "sherman",
      "boolean_attribute_1": true,
      "integer_attribute": 25,
      "array_attribute": ["banana", "apple"]
    }
    ]
}'
```
**지금: 헤더의 API 키**
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
	"attributes": [ 
 	{
	  "external_id":"user_id",
      "string_attribute": "sherman",
      "boolean_attribute_1": true,
      "integer_attribute": 25,
      "array_attribute": ["banana", "apple"]
    }
    ]
}'
```
{% endtab %}
{% endtabs %}
{% enddetails %}


