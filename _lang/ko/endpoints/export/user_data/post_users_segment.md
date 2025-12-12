---
nav_title: "POST: 세그먼트별 고객 프로필 내보내기"
article_title: "POST: 세그먼트별 고객 프로필 내보내기"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "이 문서에서는 브레이즈 엔드포인트 세그먼트별 내보내기 사용자에 대한 자세한 내용을 설명합니다."

---
{% api %}
# 세그먼트별 고객 프로필 내보내기
{% apimethod post %}
/users/export/segment
{% endapimethod %}

> 이 엔드포인트를 사용하여 세그먼트 내의 모든 사용자를 내보냅니다. 

{% alert important %}
이 엔드포인트를 사용할 때 다음 사항을 유의하십시오:<br><br>1\. 이 API 요청의 `fields_to_export` 필드는 **필수**입니다.<br>2\. `custom_events`, `purchases`, `campaigns_received`, `canvases_received` 의 필드에는 지난 90일 동안의 데이터만 포함됩니다.
{% endalert %}

사용자 데이터는 줄 바꿈으로 구분된 열러 사용자 JSON 객체 파일로 내보내집니다(예: 한 줄에 하나의 JSON 객체). 데이터 통합이 이미 설정되어 있는 경우 자동으로 생성된 URL 또는 S3 버킷으로 데이터가 내보내집니다.

한 회사에서 이 엔드포인트를 사용하여 한 번에 세그먼트당 최대 한 번만 내보내기를 실행할 수 있습니다. 내보내기가 완료될 때까지 기다렸다가 다시 시도하세요. 

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#cfa6fa98-632c-4f25-8789-6c3f220b9457 {% endapiref %}

## Prerequisites

이 엔드포인트를 사용하려면 `users.export.segment` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key/)가 필요합니다.

## 사용량 제한

{% multi_lang_include rate_limits.md endpoint='default' %}

## 자격 증명 기반 응답 세부 정보

Braze에 [S3][1], [Azure][2] 또는 [Google 클라우드 스토리지][3] 자격 증명을 추가한 경우, 각 파일은 버킷에 `segment-export/SEGMENT_ID/YYYY-MM-dd/RANDOM_UUID-TIMESTAMP_WHEN_EXPORT_STARTED/filename.zip` 와 같은 키 형식의 ZIP 파일로 업로드됩니다. Azure를 사용하는 경우, Braze의 Azure 파트너 개요 페이지에서 **이것을 기본 데이터 내보내기 대상으로 설정** 확인란이 선택되어 있는지 확인하세요. 일반적으로 처리를 최적화하기 위해 사용자 5,000명당 1개의 파일을 생성합니다. 큰 작업 공간 내에서 작은 세그먼트를 내보내면 여러 개의 파일이 생성될 수 있습니다. 그런 다음 파일을 추출하고 필요한 경우 모든 `json` 파일을 하나의 파일로 연결할 수 있습니다. `gzip`의 `output_format`을 지정하면 파일 확장자가 `.zip` 대신 `.gz`가 됩니다.

{% details Export pathing breakdown for ZIP %}
**ZIP 형식:**
`bucket-name/segment-export/SEGMENT_ID/YYYY-MM-dd/RANDOM_UUID-TIMESTAMP_WHEN_EXPORT_STARTED/filename.zip`

**ZIP 예시:**
`braze.docs.bucket/segment-export/abc56c0c-rd4a-pb0a-870pdf4db07q/2019-04-25/d9696570-dfb7-45ae-baa2-25e302r2da27-1556044807/114f0226319130e1a4770f2602b5639a.zip`

| 등록정보                        | 세부 정보                                                                              | 예제에서는 다음과 같이 표시됩니다.                    |
| ------------------------------- | ------------------------------------------------------------------------------------ |
| `bucket-name`                   | 버킷 이름에 따라 수정되었습니다.                                                     | `braze.docs.bucket`                    |
| `segment-export`                | 수정되었습니다.                                                                               | `segment-export`                       |
| `SEGMENT_ID`                    | 내보내기 요청에 포함됩니다.                                                      | `abc56c0c-rd4a-pb0a-870pdf4db07q`      |
| `YYYY-MM-dd`                    | 성공적인 콜백이 수신된 날짜입니다.                                        | `2019-04-25`                           |
| `RANDOM_UUID`                   | 요청 시점에 Braze에서 생성한 임의의 UUID입니다.                         | `d9696570-dfb7-45ae-baa2-25e302r2da27` |
| `TIMESTAMP_WHEN_EXPORT_STARTED` | 내보내기가 요청된 유닉스 시간(UTC 기준 2017-01-01:00:00:00Z 이후 초)입니다. | `1556044807`                           |
| `filename`                      | 파일당 무작위입니다.                                                                     | `114f0226319130e1a4770f2602b5639a`     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% enddetails %}

이 엔드포인트를 사용하여 내보내기에 대한 자체 버킷 정책을 적용하려면 자체 S3 또는 Azure 자격 증명을 설정할 것을 강력히 권장합니다. 클라우드 저장소 자격 증명이 없는 경우 요청에 대한 응답은 모든 사용자 파일이 포함된 ZIP 파일을 다운로드할 수 있는 URL을 제공합니다. URL은 내보내기가 준비된 후에만 유효한 위치가 됩니다. 

클라우드 스토리지 자격 증명을 제공하지 않으면 이 엔드포인트에서 내보낼 수 있는 데이터의 양에 제한이 있다는 점에 유의하세요. 내보내는 필드와 사용자 수에 따라 파일 크기가 너무 크면 파일 전송이 실패할 수 있습니다. 가장 좋은 방법은 `fields_to_export` 을 사용하여 내보낼 필드를 지정하고 전송 크기를 작게 유지해야 하는 필드만 지정하는 것입니다. 파일 생성 중 오류가 발생하면 사용자 기반을 무작위 버킷 번호를 기준으로 더 많은 세그먼트로 나누는 것을 고려하십시오 (예: 무작위 버킷 번호가 1,000 미만이거나 1,000에서 2,000 사이인 세그먼트를 생성).

두 시나리오 모두 선택적으로 내보내기가 준비되면 알림을 받으려면 `callback_endpoint` 을 입력할 수 있습니다. `callback_endpoint` 주소가 제공된 경우 다운로드가 준비되면 제공된 주소로 우편 요청을 보내드립니다. 게시물의 본문은 "성공":true입니다. Braze에 S3 자격 증명을 추가하지 않은 경우, 게시물 본문에는 다운로드 URL이 값으로 포함된 `url` 속성이 추가로 표시됩니다.

더 큰 사용자 기반은 더 긴 내보내기 시간으로 이어질 것입니다. 예를 들어 사용자가 2천만 명인 앱의 경우 1시간 이상 걸릴 수 있습니다.

## 요청 본문

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "segment_id" : (required, string) identifier for the segment to be exported,
  "callback_endpoint" : (optional, string) endpoint to post a download URL when the export is available,
  "fields_to_export" : (required, array of string) name of user data fields to export, you may also export custom attributes. New accounts must specify specific fields to export,
  "output_format" : (optional, string) when using your own S3 bucket,  specifies file format as 'zip' or 'gzip'. Defaults to ZIP file format
}
```

## 요청 매개변수

| 매개변수                     | 필수  | 데이터 유형        | 설명                                                                                                                                                                                                                                                                                                                                                                                                  |
| ----------------------------- | --------- | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `segment_id`                  | Required  | 문자열           | 내보낼 세그먼트의 식별자. [세그먼트 식별자를]({{site.baseurl}}/api/identifier_types/) 참조하세요.<br><br>지정된 세그먼트의 `segment_id`는 Braze 계정 내 [API 키]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/) 페이지에서 찾을 수 있거나 [세그먼트 목록 엔드포인트]({{site.baseurl}}/api/endpoints/export/segments/get_segment/)를 사용할 수 있습니다. |
| `callback_endpoint`           | Optional  | 문자열           | 내보내기를 사용할 수 있을 때 다운로드 URL을 게시할 엔드포인트를 설정합니다.                                                                                                                                                                                                                                                                                                                                             |
| `fields_to_export`            | 필수* | 문자열 배열 | 내보낼 사용자 데이터 필드의 이름입니다. 이 매개 변수에 `custom_attributes`를 포함하여 모든 커스텀 속성을 내보낼 수도 있습니다. <br><br>2021년 4월부터 새 계정은 내보낼 특정 필드를 지정해야 합니다.                                                                                                                                                                                        |
| `custom_attributes_to_export` | 선택 사항  | 문자열 배열 | 내보낼 특정 커스텀 속성의 이름. 최대 500개의 커스텀 속성을 내보낼 수 있습니다. 대시보드에서 커스텀 속성을 만들고 관리하려면 **데이터 설정** > **커스텀 속성**으로 이동하십시오.                                                                                                                                                                                                          |
| `output_format`               | Optional  | 문자열           | 파일의 출력 형식. 기본값은 `zip` 파일 형식입니다. 자신의 S3 버킷을 사용하는 경우 `zip` 또는 `gzip`을 지정할 수 있습니다.                                                                                                                                                                                                                                                                         |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert note %}
`fields_to_export` 매개 변수에 `custom_attributes` 이 포함되어 있으면 `custom_attributes_to_export` 에 있는 내용에 관계없이 모든 사용자 정의 속성이 내보내집니다. 특정 속성을 내보내는 것이 목표인 경우 `fields_to_export` 매개변수에 `custom_attributes` 을 포함하지 않아야 합니다. 대신 `custom_attributes_to_export` 매개 변수를 사용합니다.
{% endalert %}

## 모든 커스텀 속성을 내보내기 위한 예시 요청
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/export/segment' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "segment_id" : "segment_identifier",
  "callback_endpoint" : "example_endpoint",
  "fields_to_export" : ["first_name", "email", "purchases", "custom_attributes"],
  "output_format" : "zip"
}'
```

## 특정 커스텀 속성을 내보내기 위한 예시 요청
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/export/segment' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "segment_id" : "segment_identifier",
  "callback_endpoint" : "example_endpoint",
  "fields_to_export" : ["first_name", "email", "purchases"],
  "custom_attributes_to_export" : ["allergies", "favorite_food"],
  "output_format" : "zip"
}'
```

## 내보낼 필드

다음은 유효한 `fields_to_export` 목록입니다. `fields_to_export`를 사용하여 반환되는 데이터를 최소화하면 이 API 엔드포인트의 응답 시간을 개선할 수 있습니다.

| 내보낼 필드       | 데이터 유형       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| --------------------- | --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `apps`                | 배열           | 이 사용자가 세션에 로그인한 앱(필드 포함)입니다:<br><br>- `name`: 앱 이름<br>- `platform`: iOS, Android 또는 웹과 같은 앱 플랫폼<br>- `version`: 앱 버전 번호 또는 이름 <br>- `sessions`: 이 앱의 총 세션 수<br>- `first_used`: 첫 세션 날짜<br>- `last_used`: 마지막 세션 날짜<br><br>모든 필드는 문자열입니다.                                                                                                                                                                                                                                                                                       |
| `attributed_campaign` | 문자열          | [어트리뷰션 통합의]({{site.baseurl}}/partners/message_orchestration/) 데이터(설정된 경우). 특정 광고 캠페인의 식별자입니다.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `attributed_source`   | 문자열          | [어트리뷰션 통합의]({{site.baseurl}}/partners/message_orchestration/) 데이터(설정된 경우). 광고가 게재된 플랫폼의 식별자입니다.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `attributed_adgroup`  | 문자열          | [어트리뷰션 통합의]({{site.baseurl}}/partners/message_orchestration/) 데이터(설정된 경우). 캠페인 아래의 선택적 하위 그룹을 위한 식별자입니다.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `attributed_ad`       | 문자열          | [어트리뷰션 통합의]({{site.baseurl}}/partners/message_orchestration/) 데이터(설정된 경우). 캠페인 및 광고 그룹 아래의 선택적 하위 그룹에 대한 식별자입니다.                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `push_subscribe`      | 문자열          | 사용자의 푸시 구독 상태.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `email_subscribe`     | 문자열          | 사용자의 이메일 구독 상태.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `braze_id`            | 문자열          | 이 사용자에 대해 Braze가 설정한 기기별 고유 사용자 식별자입니다.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `country`             | 문자열          | [ISO 3166-1 알파-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) 표준을 사용하는 사용자의 국가.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `created_at`          | 문자열          | 사용자 프로필이 생성된 날짜와 시간(ISO 8601 형식)입니다.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `custom_attributes`   | 객체          | 이 사용자에 대한 사용자 지정 속성 키-값 쌍입니다.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `custom_events`       | 배열           | 지난 90일 동안 이 사용자에 의해 발생한 사용자 지정 이벤트입니다.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `devices`             | 배열           | 플랫폼에 따라 다음을 포함할 수 있는 사용자 디바이스에 대한 정보입니다:<br><br>- `model`: 디바이스 모델명<br>- `os`: 디바이스의 운영 체제<br>- `carrier`: 디바이스의 서비스 통신사(가능한 경우)<br>- `idfv`: (iOS) Braze 장치 식별자, 공급업체용 Apple 식별자(있는 경우)<br>- `idfa`: (iOS) 광고용 식별자(있는 경우)<br>- `device_id`: (Android) Braze 디바이스 식별자<br>- `google_ad_id`: (Android) Google Play 광고 식별자(있는 경우)<br>- `roku_ad_id`: (로쿠) 로쿠 광고 식별자<br>- `ad_tracking_enabled`: 기기에서 광고 추적이 활성화된 경우 참 또는 거짓일 수 있습니다. |
| `dob`                 | 문자열          | 사용자의 생년월일 형식 `YYYY-MM-DD`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `email`               | 문자열          | 사용자의 이메일 주소.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `external_id`         | 문자열          | 식별된 사용자를 위한 고유 사용자 식별자입니다.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `first_name`          | 문자열          | 사용자의 이름입니다.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `gender`              | 문자열          | 사용자의 성별. 가능한 값은 다음과 같습니다:<br><br>- `M`: 남성<br>- `F`: 여성<br>- `O`: 기타<br>- `N`: 해당 없음<br>- `P`: 말하지 않는 것을 선호합니다.<br>- `nil`: 알 수 없음                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `home_city`           | 문자열          | 사용자의 거주 도시.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `language`            | 문자열          | ISO-639-1 표준의 사용자 언어.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `last_coordinates`    | 플로트 배열 | 사용자의 가장 최근 디바이스 위치, 형식은 `[longitude, latitude]` 입니다.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `last_name`           | 문자열          | 사용자의 성입니다.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `phone`               | 문자열          | E.164 형식의 사용자 전화번호.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `purchases`           | 배열           | 이 사용자가 지난 90일 동안 구매한 구매 건수입니다.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `push_tokens`         | 배열           | 사용자의 푸시 토큰에 대한 정보.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `random_bucket`       | 정수         | 무작위 사용자 세그먼트를 균일하게 분산시키는 데 사용되는 사용자의 [무작위 버킷 번호입니다]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/customer_behavior_events#random-bucket-number-event).                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `time_zone`           | 문자열          | 사용자의 표준 시간대를 IANA 표준 시간대 데이터베이스와 동일한 형식으로 입력합니다.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `total_revenue`       | Float           | 이 사용자에게 귀속된 총 수익입니다. 총 수익은 사용자가 받은 캠페인 및 캔버스에 대한 전환 기간 동안 구매한 금액을 기준으로 계산됩니다.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `uninstalled_at`      | 타임스탬프       | 사용자가 앱을 삭제한 날짜와 시간입니다. 앱이 제거되지 않은 경우 생략됩니다.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `user_aliases`        | 객체          | `alias_name` 및 `alias_label` 을 포함하는 [사용자 별칭 개체가]({{site.baseurl}}/api/objects_filters/user_alias_object#user-alias-object-specification) 있는 경우.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## 중요한 알림

- `custom_events`, `purchases`, `campaigns_received`, `canvases_received` 의 필드에는 지난 90일 동안의 데이터만 포함됩니다.
- `custom_events` 와 `purchases` 모두 `first` 와 `count` 에 대한 필드가 포함되어 있습니다. 이 두 필드에는 모든 시간의 정보를 반영하며 지난 90일 동안의 데이터에만 국한되지 않습니다. 예를 들어, 특정 사용자가 90일 전에 이벤트를 처음 수행한 경우, 이는 `first` 필드에 정확하게 반영되며, `count` 필드는 지난 90일 이전에 발생한 이벤트도 고려합니다.
- 회사가 엔드포인트 수준에서 실행할 수 있는 동시 세그먼트 내보내기 수는 100개로 제한됩니다. 이 제한을 초과하는 시도는 오류가 발생합니다.
- 첫 번째 내보내기 작업이 실행 중인 상태에서 세그먼트를 두 번째로 내보내려고 하면 429 오류가 발생합니다.

## 응답

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "object_prefix": (required, string) the filename prefix that will be used for the JSON file produced by this export, for example, 'bb8e2a91-c4aa-478b-b3f2-a4ee91731ad1-1464728599',
    "url" : (optional, string) the URL where the segment export data can be downloaded if you do not have your own S3 credentials
}
```

URL을 사용할 수 있게 된 후에는 몇 시간 동안만 유효합니다. 따라서 Braze에 자신의 S3 자격 증명을 추가하는 것을 적극 권장합니다.

API 응답에 `object_prefix` 이 표시되고 데이터를 다운로드할 수 있는 URL이 없다면 이 엔드포인트에 대해 이미 Amazon S3 버킷이 설정되어 있다는 뜻입니다. 이 엔드포인트를 사용하여 내보낸 모든 데이터는 S3 버킷으로 바로 이동합니다.

## 사용자 내보내기 파일 출력 예시

사용자 내보내기 개체(가능한 최소한의 데이터만 포함 - 개체에서 필드가 누락된 경우 null 또는 비어있는 것으로 가정해야 함):

{% tabs %}
{% tab All fields %}

```json
{
    "created_at": (string),
    "external_id" : (string),
    "user_aliases" : [
      {
        "alias_name" : (string),
        "alias_label" : (string)
      }
    ],
    "braze_id": (string),
    "first_name" : (string),
    "last_name" : (string),
    "email" : (string),
    "dob" : (string) date for the user's date of birth,
    "home_city" : (string),
    "country" : (string) ISO-3166-1 alpha-2 standard,
    "phone" : (string),
    "language" : (string) ISO-639-1 standard,
    "time_zone" : (string),
    "last_coordinates" : (array of float) [lon, lat],
    "gender" : (string) "M" | "F",
    "total_revenue" : (float),
    "attributed_campaign" : (string),
    "attributed_source" : (string),
    "attributed_adgroup" : (string),
    "attributed_ad" : (string),
    "push_subscribe" : (string) "opted_in" | "subscribed" | "unsubscribed",
    "email_subscribe" : (string) "opted_in" | "subscribed" | "unsubscribed",
    "custom_attributes" : (object) custom attribute key-value pairs,
    "custom_events" : [
      {
        "name" : (string),
        "first" : (string) date,
        "last" : (string) date,
        "count" : (int)
      },
      ...
    ],
    "purchases" : [
      {
        "name" : (string),
        "first" : (string) date,
        "last" : (string) date,
        "count" : (int)
      },
      ...
    ],
    "devices" : [
      {
        "model" : (string),
        "os" : (string),
        "carrier" : (string),
        "idfv" : (string) only included for iOS devices when IDFV collection is enabled,
        "idfa" : (string) only included for iOS devices when IDFA collection is enabled,
        "google_ad_id" : (string) only included for Android devices when Google Play Advertising Identifier collection is enabled,
        "roku_ad_id" : (string) only included for Roku devices,
        "ad_tracking_enabled" : (boolean)
      },
      ...
    ],
    "push_tokens" : [
      {
        "app" : (string) app name,
        "platform" : (string),
        "token" : (string),
        "device_id": (string),
        "notifications_enabled": (boolean) whether the user's push notifications are turned on or turned off
      },
      ...
    ],
    "apps" : [
      {
        "name" : (string),
        "platform" : (string),
        "version" : (string),
        "sessions" : (integer),
        "first_used" : (string) date,
        "last_used" : (string) date
      },
      ...
    ],
    "campaigns_received" : [
      {
        "name" : (string),
        "last_received" : (string) date,
        "engaged" : 
         {
           "opened_email" : (boolean),
           "opened_push" : (boolean),
           "clicked_email" : (boolean),
           "clicked_triggered_in_app_message" : (boolean)
          },
          "converted" : (boolean),
          "api_campaign_id" : (string),
          "variation_name" : (optional, string) exists only if it is a multivariate campaign,
          "variation_api_id" : (optional, string) exists only if it is a multivariate campaign,
          "in_control" : (optional, boolean) exists only if it is a multivariate campaign
        },
      ...
    ],
    "canvases_received": [
      {
        "name": (string),
        "api_canvas_id": (string),
        "last_received_message": (string) date,
        "last_entered": (string) date,
        "variation_name": (string),
        "in_control": (boolean),
        "last_exited": (string) date,
        "steps_received": [
          {
            "name": (string),
            "api_canvas_step_id": (string),
            "last_received": (string) date
          },
          {
            "name": (string),
            "api_canvas_step_id": (string),
            "last_received": (string) date
          },
          {
            "name": (string),
            "api_canvas_step_id": (string),
            "last_received": (string) date
          }
        ]
      },
      ...
    ],
    "cards_clicked" : [
      {
        "name" : (string)
      },
      ...
    ]
}
```

{% endtab %}
{% tab Sample output %}

```json
{
    "created_at" : "2020-07-10 15:00:00.000 UTC",
    "external_id" : "A8i3mkd99",
    "user_aliases" : [
      {
        "alias_name" : "user_123",
        "alias_label" : "amplitude_id"
      }
    ],
    "braze_id": "5fbd99bac125ca40511f2cb1",
    "random_bucket" : 2365,
    "first_name" : "Jane",
    "last_name" : "Doe",
    "email" : "example@braze.com",
    "dob" : "1980-12-21",
    "home_city" : "Chicago",
    "country" : "US",
    "phone" : "+442071838750",
    "language" : "en",
    "time_zone" : "Eastern Time (US & Canada)",
    "last_coordinates" : [41.84157636433568, -87.83520818508256],
    "gender" : "F",
    "total_revenue" : 65,
    "attributed_campaign" : "braze_test_campaign_072219",
    "attributed_source" : "braze_test_source_072219",
    "attributed_adgroup" : "braze_test_adgroup_072219",
    "attributed_ad" : "braze_test_ad_072219",
    "push_subscribe" : "opted_in", 
    "push_opted_in_at": "2020-01-26T22:45:53.953Z",
    "email_subscribe" : "subscribed",
    "custom_attributes": 
    {
      "loyaltyId": "37c98b9d-9a7f-4b2f-a125-d873c5152856",
      "loyaltyPoints": "321",
       "loyaltyPointsNumber": 107
    },
    "custom_events": [
      {
        "name": "Loyalty Acknowledgement",
        "first": "2021-06-28T17:02:43.032Z",
        "last": "2021-06-28T17:02:43.032Z",
        "count": 1
      },
      ...
    ],
    "purchases": [
      {
        "name": "item_40834",
        "first": "2021-09-05T03:45:50.540Z",
        "last": "2022-06-03T17:30:41.201Z",
        "count": 10
      },
      ...
    ],
    "devices": [
      {
        "model": "Pixel XL",
        "os": "Android (Q)",
        "carrier": null,
        "device_id": "312ef2c1-83db-4789-967-554545a1bf7a",
        "ad_tracking_enabled": true
      },
      ...
    ],
    "push_tokens": [
      {
        "app": "MovieCanon",
        "platform": "Android",
        "token": "12345abcd",
        "device_id": "312ef2c1-83db-4789-967-554545a1bf7a",
        "notifications_enabled": true
      },
      ...
    ],
    "apps": [
      {
        "name": "MovieCannon",
        "platform": "Android",
        "version": "3.29.0",
        "sessions": 1129,
        "first_used": "2020-02-02T19:56:19.142Z",
        "last_used": "2021-11-11T00:25:19.201Z"
      },
      ...
    ],
    "campaigns_received": [
      {
        "name": "Email Unsubscribe",
        "api_campaign_id": "d72fdc84-ddda-44f1-a0d5-0e79f47ef942",
        "last_received": "2022-06-02T03:07:38.105Z",
        "engaged": 
        {
           "opened_email": true
        },
        "converted": true,
        "multiple_converted": 
        {
          "Primary Conversion Event - A": true
        },
        "in_control": false,
        "variation_name": "Variant 1",
        "variation_api_id": "1bddc73a-a134-4784-9134-5b5574a9e0b8"
      },
      ...
    ],
    "canvases_received": [
      {
        "name": "Non Global  Holdout Group 4/21/21",
        "api_canvas_id": "46972a9d-dc81-473f-aa03-e3473b4ed781",
        "last_received_message": "2021-07-07T20:46:24.136Z",
        "last_entered": "2021-07-07T20:45:24.000+00:00",
        "variation_name": "Variant 1",
        "in_control": false,
        "last_entered_control_at": null,
        "last_exited": "2021-07-07T20:46:24.136Z",
        "steps_received": [
          {
            "name": "Step",
            "api_canvas_step_id": "43d1a349-c3c8-4be1-9fbe-ce708e4d1c39",
            "last_received": "2021-07-07T20:46:24.136Z"
          },
          ...
        ]
      }
      ...
    ],    
    "cards_clicked" : [
      {
        "name" : "Loyalty Promo"
      },
      ...
    ]
}
```

{% endtab %}
{% endtabs %}

{% alert tip %}
CSV 및 API 내보내기 문제 해결에 대한 도움은 [내보내기 문제 해결]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/)를 방문하세요.
{% endalert %}

[1]: {{site.baseurl}}/partners/data_and_infrastructure_agility/cloud_storage/amazon_s3
[2]: {{site.baseurl}}/partners/data_and_infrastructure_agility/cloud_storage/microsoft_azure_blob_storage_for_currents/
[3]: {{site.baseurl}}/partners/data_and_infrastructure_agility/cloud_storage/google_cloud_storage_for_currents/

{% endapi %}
