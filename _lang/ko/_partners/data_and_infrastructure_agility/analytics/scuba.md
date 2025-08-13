---
nav_title: 스쿠버
article_title: Scuba Analytics
description: "Scuba 및 Braze의 이 기술 참조 문서에서는 Braze 세그먼트를 사용하여 Scuba의 실시간 데이터 인사이트를 활성화하는 방법을 설명합니다."
alias: /partners/scuba/
page_type: partner
search_tag: Partner
---

# Scuba Analytics

>[Scuba Analytics][1]는 고속 시계열 데이터를 위해 설계된 풀스택 머신 러닝 기반 데이터 협업 플랫폼입니다. Scuba를 사용하면 사용자(액터라고도 함)를 선택적으로 내보내고 Braze 플랫폼에 로드할 수 있습니다. Scuba에서는 커스텀 액터 속성을 사용하여 행동 추세를 분석하고, 다양한 플랫폼에서 데이터를 활성화하며, 머신 러닝을 사용하여 예측 모델링을 수행합니다.

_이 통합은 스쿠버 애널리틱스에서 유지 관리합니다._

## 전제 조건

Braze에서 Scuba Analytics를 사용하려면 다음이 필요합니다.

| 요구 사항 | 설명 |
|---|---|
|스쿠버 API 토큰 | `https://{scuba_hostname}/api/create_token` 엔드포인트에서 검색할 수 있는 Scuba API 토큰. |
| Braze REST API 키 | `users.track` 권한이 있는 Braze REST API 키. <br><br> 이는 **설정** > **API 키**에서 Braze 대시보드에서 생성할 수 있습니다. |
| Braze REST 엔드포인트  | REST 엔드포인트 URL. 엔드포인트는 [인스턴스의 Braze URL에][1] 따라 달라집니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Braze에 스쿠버 데이터 업로드하기

{% alert important %}
다음 요청은 curl을 사용합니다. 더 나은 API 요청 관리를 위해 Postman과 같은 API 클라이언트를 사용하는 것이 좋습니다.
{% endalert %}

Braze에 Scuba 데이터를 업로드하려면 `application/json` 콘텐츠 유형을 사용하여 `https://scuba.pliant.io/a/scuba-connectors/prod/braze-activation`에 대한 POST 요청을 수행합니다.

```bash
curl -X POST "https://scuba.pliant.io/a/scuba-connectors/prod/braze-activation" \
-H "content-type: application/json" \
-d '{"braze_host":"BRAZE_API_ENDPOINT", \
"braze_api_key":"BRAZE_API_KEY", \
"scuba_host":"HOSTNAME", \
"scuba_token":"SCUBA_API_TOKEN", \
"scuba_table_name":"TABLE_NAME", \
"scuba_actor_property_name":"ACTOR_PROPERTY_NAME", \
"scuba_actor_property_value_filter":"ACTOR_PROPERTY_FILTER" \
"scuba_actor_id":"ACTOR_ID", \
"scuba_period_start":"PERIOD_START", \
"scuba_period_end":"PERIOD_END", \
"scuba_record_limit":"RECORD_LIMIT"}'
```

다음을 교체합니다:

| 입력 안내             | 설명                                                                                                                                                                                     |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `BRAZE_API_ENDPOINT`    | 현재 Braze 인스턴스의 Braze REST 엔드포인트 URL. 자세한 내용은 [Rest API 키]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/#rest-api-keys)를 참조하세요. |
| `BRAZE_API_KEY`         | `users.track` 권한이 있는 Braze REST API 키입니다.                                                                                                                                      |
| `HOSTNAME`              | 현재 Scuba 인스턴스의 호스트 이름.                                                                                                                                                    |
| `SCUBA_API_TOKEN`       | Scuba API 토큰.                                                                                                                                                                           |
| `TABLE_NAME`            | 데이터 집합이 속한 테이블입니다. 자세한 내용은 [용어집을 참조하세요: 데이터 집합 테이블][3].                                                                                                      |
| `ACTOR_PROPERTY_NAME`   | 데이터 세트가 속한 액터 속성입니다. 이 이름과 일치하는 데이터만 반환됩니다. 자세한 내용은 [용어집을 참조하세요: 액터 속성][4].                                             |
| `ACTOR_PROPERTY_FILTER` | 배우 속성에 대한 오디언스 검색 필터입니다.                                                                                                                                             |
| `ACTOR_ID`              | 데이터 세트가 속한 액터 프로퍼티의 ID입니다. 이 ID는 Braze의 `external_id` 계정과 일치합니다. 자세한 내용은 [용어집을 참조하세요: 액터][5].                                              |
| `PERIOD_START`          | BQL 호환 날짜로 설정된 시작 기간. 자세한 내용은 [BQL 구문 및 사용법을][6] 참조하세요.                                                                                                 |
| `PERIOD_END`            | BQL 호환 날짜로 설정된 종료 기간. 자세한 내용은 [BQL 구문 및 사용법을][6] 참조하세요.                                                                                                   |
| `RECORD_LIMIT`          | **선택 사항**: 반환할 최대 레코드 수입니다. `scuba_record_limit`를 생략하면 Scuba는 최대 100개의 레코드를 반환합니다. 이를 변경하려면 `scuba_record_limit` 에 음수가 아닌 숫자를 지정합니다.    |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 기본 동작

기본적으로 `update_existing_only`는 `false`로 설정되어 있으며, 이는 Braze의 기존 레코드를 업데이트하고 존재하지 않는 항목에 대해 새 레코드를 생성합니다. Scuba가 새 레코드를 생성하지 못하게 하려면 `update_existing_only`를 `true`로 설정합니다.

### 사용량 제한

Scuba는 이 엔드포인트에 분당 50,000건의 사용량 제한을 적용합니다.

## Scuba의 행동 데이터를 사용하여 세그먼트 만들기

[데이터를 업로드한](#uploading-your-scuba-data-to-braze) 후, Scuba의 행동 데이터를 사용하여 Braze에서 사용자 세그먼트를 생성할 수 있습니다.

### 1단계: 새 세그먼트 만들기

Braze에서 **오디언스** > **세그먼트로** 이동한 다음 **세그먼트 생성을** 선택하고 세그먼트의 이름을 입력합니다.

![Braze에서 새 세그먼트 만들기.][501]

### 2단계: Scuba 속성을 찾아서 선택

**세그먼트 세부 정보** > **필터에서** **사용자 지정 속성을** 선택합니다.

!['세그먼트 세부 정보'에서 '사용자 지정 속성' 필터를 선택합니다.][502]

**커스텀 속성 검색**을 선택한 다음, 이전 POST 요청에서 사용한 액터 속성정보 이름을 선택합니다.

![액터 프로퍼티를 커스텀 어트리뷰트로 선택합니다.][503]

### 3단계: 속성 구성

액터 프로퍼티 이름 옆에서 연산자와 값(해당되는 경우)을 선택합니다. 이러한 값은 Scuba에서 정의한 액터 속성정보에 따라 결정됩니다. 완료했으면 **저장을** 선택합니다.

![선택한 항목에 대한 작업 및 값 선택 ][504]


[1]: https://scuba.io
[3]: https://docs.scuba.io/glossary/dataset-table
[4]: https://docs.scuba.io/glossary/actor-property
[5]: https://docs.scuba.io/glossary/actor
[6]: https://docs.scuba.io/guides/bql-syntax-and-usage
[501]: {% image_buster /assets/img/scuba/analytics/segment_name.png %}
[502]: {% image_buster /assets/img/scuba/analytics/filter_attribute.png %}
[503]: {% image_buster /assets/img/scuba/analytics/select_property.png %}
[504]: {% image_buster /assets/img/scuba/analytics/operator_end.png %}
