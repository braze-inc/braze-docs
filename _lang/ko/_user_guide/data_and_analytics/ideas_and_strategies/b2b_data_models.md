---
nav_title: B2B 데이터 모델
article_title: B2B 데이터 모델 만들기
page_order: 0
page_type: reference
description: "Braze 데이터 도구를 사용하여 B2B 모델을 만드는 방법을 알아보세요."
---

# B2B 데이터 모델 만들기

> 이 사용 사례는 Braze 데이터 도구를 사용하여 비즈니스 사용자를 타겟팅, 트리거, 개인화 및 메시지를 전송하는 데 도움이 되는 효과적이고 효율적인 B2B 데이터 모델을 만드는 방법을 보여줍니다. 

{% alert note %}
이러한 권장 사항은 시간이 지남에 따라 Braze가 B2B 기능을 구축함에 따라 변경될 수 있습니다.
{% endalert %}

B2B 데이터 모델을 설정하는 방법을 살펴보기 전에 알아야 할 몇 가지 개념과 용어에 대해 살펴보겠습니다.

B2B 캠페인을 실행하는 데 필요한 네 가지 주요 B2B 개체가 있습니다.

| 객체 | 설명 |
| --- | --- |
| 리드 | 제품이나 서비스에 관심을 보였지만 아직 기회로 전환되지 않은 잠재 고객에 대한 기록입니다. |
| 연락처 | 일반적으로 자격을 갖추고 리드에서 연락처로 전환된 개인은 영업 기회를 추구할 수 있습니다. |
| 기회 | 진행 중인 잠재적 판매 또는 거래의 세부 정보를 추적하는 기록
| 계좌 | 자격을 갖춘 잠재 고객, 기존 고객, 파트너 또는 이와 유사한 중요한 관계를 맺고 있는 경쟁사 조직에 대한 기록입니다. |
{: .reset-td-br-1 .reset-td-br-2 }

Braze 내에서 이 네 가지 개체는 사용자 프로필과 비즈니스 개체라는 두 가지 개체로 결합 및 축소됩니다.

| 브레이즈 B2B 개체 | 설명 | 원본 B2B 개체  |
| --- | --- | --- |
| 사용자 프로필 | 영업 CRM 시스템의 리드와 연락처에 직접 매핑됩니다. 리드는 Braze에서 캡처되므로 영업 CRM 시스템에서 자동으로 리드로 생성됩니다. 연락처로 변환되면 연락처 ID와 세부 정보가 다시 Braze에 동기화됩니다. |리드<br> 연락처 |
| 비즈니스 개체 | 이는 영업 CRM 시스템의 모든 비사용자 개체에 매핑됩니다. 여기에는 계정 개체 및 기회 개체와 같은 영업 관련 개체가 포함됩니다. | 계좌<br> 기회 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## 1단계: Braze에서 비즈니스 개체 만들기

비즈니스 개체는 사용자 중심이 아닌 모든 데이터 집합입니다. B2B 맥락에서 이러한 데이터에는 계정 및 기회 데이터와 회사가 추적하는 기타 관련 비사용자 중심 데이터 세트가 포함됩니다.

Braze에서 비즈니스 개체를 만들고 관리하는 방법에는 카탈로그와 연결된 소스 두 가지가 있습니다. 

| 방법 | 설명 |
| --- | --- |
| [카탈로그]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs) | 이들은 Braze의 기본 사용자 프로필에 있는 독립적인 데이터 객체(보조 데이터 객체)입니다. B2B 환경에서는 계정과 기회에 대한 카탈로그가 있을 것입니다. |
| [연결된 소스]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/connected_sources/) | 이를 통해 Braze는 데이터 웨어하우스에 직접 쿼리할 수 있습니다. 이미 리드, 연락처, 기회, 계정 개체를 데이터 웨어하우스에 정기적으로 동기화하고 있을 가능성이 높으므로 Braze 세분화를 해당 웨어하우스에 직접 지정하고 복사본이 없는 환경에서 활성화할 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 }

### 옵션 1: 계정 및 기회에 카탈로그 사용

카탈로그는 Braze에서 호스팅 및 관리되는 데이터 테이블입니다. 계정 및 기회 데이터는 선택한 영업 CRM 시스템에서 생성되지만, 계정 기반 세분화, 계정 기반 마케팅, 리드 관리 등 마케팅 목적으로 사용하기 위해 Braze에서 이를 복제하게 됩니다.

이 옵션의 경우, 계정용 카탈로그와 기회용 카탈로그를 각각 하나씩 생성하고 [카탈로그 API]({{site.baseurl}}/api/endpoints/catalogs/) 또는 [카탈로그 클라우드 데이터 수집(CDI)]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/sync_catalogs_data/)을 통해 Braze 업데이트를 전송하여 자주 업데이트하는 것을 권장합니다. 이러한 카탈로그를 생성할 때 카탈로그의 `id` (첫 번째 열)이 영업 CRM 시스템의 `id` 과 일치하는지 확인하세요.

#### CRM 필드 위에 매핑

아래 표에는 CRM의 계정 및 기회 개체에서 매핑할 수 있는 몇 가지 필드의 예가 나와 있습니다.

{% tabs %}
{% tab 계정 카탈로그 %}

이 사용 사례에서는 Salesforce를 예로 들어 CRM 시스템을 설명합니다. CRM의 개체에 포함된 모든 필드에 매핑할 수 있습니다.

<table border="1">
  <tr>
    <th><b>브레이즈 개체</b></th>
    <th><b>브레이즈 필드</b></th>
    <th><b>CRM 개체(Salesforce)</b></th>
    <th><b>CRM 분야(Salesforce)</b></th>
  </tr>
  <tr>
    <td rowspan="4">카탈로그 > 계정 카탈로그</td>
    <td><code>id</code></td>
    <td><code>account</code></td>
    <td><code>id</code></td>
  </tr>
  <tr>
    <td><code>AccountName</code></td>
    <td><code>account</code></td>
    <td><code>Account Name</code></td>
  </tr>
  <tr>
    <td><code>Type</code></td>
    <td><code>account</code></td>
    <td><code>Type</code></td>
  </tr>
  <tr>
    <td><code>OTHER_FIELDS</code></td>
    <td><code>account</code></td>
    <td><code>OTHER_FIELDS</code></td>
  </tr>
</table>

##### 매핑된 계정 필드의 예시 테이블

![청구 주소 및 계정 소유자와 같은 각 정보가 포함된 Salesforce 계정 표.]({% image_buster /assets/img/b2b/sf_accounts.png %})

{% endtab %}
{% tab 기회 카탈로그 %}

이 사용 사례에서는 Salesforce를 예로 들어 CRM 시스템을 설명합니다. CRM의 개체에 포함된 모든 필드에 매핑할 수 있습니다.

<table border="1">
  <tr>
    <th><b>브레이즈 개체</b></th>
    <th><b>브레이즈 필드</b></th>
    <th><b>CRM 개체(Salesforce)</b></th>
    <th><b>CRM 분야(Salesforce)</b></th>
  </tr>
  <tr>
    <td rowspan="4">카탈로그 > 기회 카탈로그</td>
    <td><code>id</code></td>
    <td><code>opportunity</code></td>
    <td><code>id</code></td>
  </tr>
  <tr>
    <td><code>OpportunityName</code></td>
    <td><code>opportunity</code></td>
    <td><code>Opportunity Name</code></td>
  </tr>
  <tr>
    <td><code>Territory</code></td>
    <td><code>opportunity</code></td>
    <td><code>Territory</code></td>
  <tr>
    <td><code>OTHER_FIELDS</code></td>
    <td><code>opportunity</code></td>
    <td><code>OTHER_FIELDS</code></td>
  </tr>
  </tr>
</table>

##### 매핑된 기회 필드의 예시 테이블

![청구 주소 및 계정 소유자와 같은 각 정보가 포함된 Salesforce 기회 표.]({% image_buster /assets/img/b2b/sf_opportunities.png %})

{% endtab %}
{% endtabs %}

### 옵션 2: 계정 및 기회에 연결된 소스 사용

연결된 소스는 자체 데이터 웨어하우스에서 사용자가 호스팅하고 Braze [CDI 세그먼트에서]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/cdi_segments/) 쿼리하는 데이터 테이블입니다. 카탈로그와 달리, 비즈니스 개체(계정 및 기회)를 Braze에 복제하는 대신 데이터 웨어하우스에 보관하고 데이터 웨어하우스를 진실의 소스로 사용하게 됩니다.

연결된 소스를 설정하려면 [연결된 소스 통합하기를]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/connected_sources#integrating-connected-sources) 참조하세요.

## 2단계: 비즈니스 개체를 사용자 프로필과 연결

사용자 프로필은 대부분의 인구통계학적 세분화, 트리거링 및 개인화를 지원하는 Braze의 주요 객체입니다. 사용자 프로필에는 속성(인구통계 데이터), 이벤트(행동 데이터) 또는 구매(트랜잭션 데이터)의 형태를 취하는 [사용자 지정 데이터를]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/) 포함하여 SDK 및 기타 소스에서 수집한 [기본 사용자 데이터가]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/) 포함됩니다.

### 2.1 단계: 영업 CRM ID를 Braze에 매핑

먼저, Braze와 선택한 CRM에 데이터를 공유할 수 있는 공통 식별자가 있는지 확인합니다. 다음 표를 사용하여 영업 CRM ID 필드를 Braze 사용자 개체에 다시 매핑하는 것이 좋습니다. 아래 표에는 Salesforce가 CRM 시스템으로 표시되어 있지만 이 작업은 모든 CRM에서 수행할 수 있습니다.

#### 브레이즈 오브젝트: 사용자

| 브레이즈 필드 | CRM 개체(Salesforce) | CRM 분야(Salesforce) | 추가 정보 |
| --- | --- | --- | --- |
| `Aliases.salesforce_lead_id` | Lead | `id` |  \- 사용자 별칭 레이블: `salesforce_lead_id` <br>\- 사용자 별칭 이름입니다: `lead_id`|
| `Aliases.salesforce_contact_id` | 연락처 | `id` | \- 사용자 별칭 레이블: `salesforce_contact_id` <br>\- 사용자 별칭 이름입니다: `contact_id` |
| `AccountId` | 연락처 | `AccountId` | 
| `OpportunityId` (선택 사항, 스칼라) <br>또는<br> `Opportunities` (선택 사항, 배열) | 기회 | `id` | 
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 }

{% alert note %}
`external_id` 대신 [별칭을]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases) 사용하여 Salesforce 리드 및 연락처 식별자를 Braze에 다시 매핑하는 것이 좋습니다. 제품 주도 성장 스타일 이니셔티브를 식별하고 실행할 때 필요한 조회 횟수를 줄일 수 있기 때문입니다.
{% endalert %}

ID를 동기화한 후에는 Braze 사용자 프로필을 비즈니스 개체와 연결해야 합니다. 

### 2.2 단계: 사용자 프로필과 비즈니스 개체 간의 관계 만들기

#### 옵션 1: 비즈니스 개체에 카탈로그를 사용하는 경우

이제 기회 및 계정 세부 정보가 Braze 카탈로그로 설명되었으므로 이러한 카탈로그와 메시지를 보내려는 사용자 프로필 간에 관계를 만들어야 합니다. 현재 이 작업을 수행하려면 두 단계가 필요합니다:

1. 사용자 프로필에 계정(예: `account_id (string)`), 기회 ID(예: `opportunity_ids (array)`) 또는 둘 다를 속성으로 포함시킵니다.
2. 이벤트 속성으로 계정 ID가 포함된 이벤트(예: `account_linked`)를 기록합니다.

```json
{
  "attributes" : [
    {
      "external_id" : "user1",
      "accountId" : "001J7000004K7AF",
      "opportunityIds" : [
"0064J000004EU59",
"0064J000004EU5G"
]
    }
  ],
  "events" : [
    {
      "external_id" : "user1",
      "name" : "account_linked",
      "time" : "2013-07-16T19:20:45+01:00",
      "properties": {
        "account_id": "001J7000004K7AF"
      }
    }
  ]
}
```

#### 옵션 2: 연결된 소스를 사용하는 경우

연결된 소스의 테이블 중 하나에 사용자를 위해 Braze에서 설정한 `external_user_id` 과 일치하는 `user_id` 이 포함되어야 합니다. 위의 사용자 프로필 설정에서는 리드와 `contact_ids` 을 `external_id` 으로 사용하므로 리드/연락처 테이블에 이러한 ID가 포함되어 있는지 확인해야 합니다.

ID가 일치하는지 확인하는 것 외에도 효율적인 세분화 및 개인화를 위해 `account_id`, `opportunity_id` 과 같은 기본 계정 수준 데이터와 `industry` 과 같은 일반적인 기업 속성까지 사용자 프로필에 기록하는 것이 좋습니다.