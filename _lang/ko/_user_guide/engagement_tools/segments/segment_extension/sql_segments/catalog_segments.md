---
nav_title: "카탈로그 세그먼트"
article_title: 카탈로그 세그먼트 세분화
page_order: 1
page_type: reference
alias: "/catalog_segments/"
description: "이 문서에서는 SQL 세그먼트 확장에서 카탈로그 데이터를 사용하여 사용자 오디언스를 구축하는 카탈로그 세그먼트를 만드는 방법에 대해 설명합니다."
tool: Segments
---

# 카탈로그 세그먼트

> 카탈로그 세그먼트는 카탈로그 데이터를 커스텀 이벤트 또는 구매 데이터와 결합하여 생성되는 SQL 세그먼트 확장의 한 유형입니다. 세그먼트에서 참조한 다음 캠페인과 캔버스를 통해 타겟팅할 수 있습니다. 

{% alert important %}
카탈로그 세그먼트는 현재 얼리 액세스 중입니다. 이번 얼리 액세스에 참여하려면 고객 성공 매니저에게 문의하세요.
{% endalert %}

카탈로그 세그먼트는 SQL을 사용하여 카탈로그의 데이터와 커스텀 이벤트 또는 구매의 데이터를 조인합니다. 이렇게 하려면 카탈로그와 커스텀 이벤트 또는 구매 전반에 걸쳐 공통 식별자 필드가 있어야 합니다. 예를 들어 카탈로그의 아이템 ID 값은 커스텀 이벤트의 속성 값과 일치해야 합니다.

## 카탈로그 세그먼트 만들기

1. **세그먼트 확장** > **새 확장 프로그램 만들기** > **템플릿으로 시작으로** 이동하여 템플릿을 선택합니다. <br>이벤트 또는 구매를 위한 카탈로그 세그먼트를 생성하는 옵션이 있는 모달입니다.]({% image_buster /assets/img/catalog-segments-template.png %}){: style="max-width:80%" }

{: start="2"}
2\. SQL 편집기는 자동으로 템플릿으로 채워집니다. <br>미리 생성된 템플릿이 있는 SQL 편집기.]({% image_buster /assets/img/catalog-segments-editor.png %}){: style="max-width:80%" }<br>이 템플릿은 사용자 이벤트 데이터를 카탈로그 데이터와 조인하여 특정 카탈로그 항목에 참여한 사용자를 세그먼트화합니다.

3. 세그먼트를 생성하기 전에 **변수** 탭을 사용하여 템플릿에 필요한 필드를 입력하세요. <br>Braze에서 카탈로그 항목에 대한 참여도를 기반으로 사용자를 식별하려면 다음을 수행해야 합니다: <br> \- 카탈로그 필드가 포함된 카탈로그를 선택합니다. <br> \- 이벤트 속성정보가 포함된 커스텀 이벤트를 선택합니다. <br> \- 카탈로그 필드와 이벤트 속성정보 값 일치시키기

변수를 선택하기 위한 가이드라인은 다음과 같습니다:

| 변수 필드 | 설명 |
| --- | --- |
| `Catalog` | 사용자를 타겟팅하는 데 사용하는 카탈로그의 이름입니다. |
| `Catalog field`| 카탈로그에서 `Custom event property` 과 동일한 값을 포함하는 필드입니다. 이는 일종의 ID인 경우가 많습니다. 이커머스 사용 사례에서는 `shopify_id` 이 됩니다. |
| `Custom event` | `Catalog field` 과 일치하는 값을 가진 속성을 포함하는 동일한 이벤트인 커스텀 이벤트의 이름입니다. 이커머스 사용 사례에서는 `Made Order` 이 됩니다. |
| `Custom event property` | `Catalog field` 와 값을 일치시키는 커스텀 이벤트 속성정보의 이름입니다. 전자 상거래 예제 사용 사례에서는 다음과 같습니다. `Shopify_ID.`|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{: start="4"}
4\. 필요한 경우 사용 사례에 대한 추가 선택 필드를 입력하여 카탈로그 내의 특정 필드 값으로 세그먼트화할 수 있습니다:
- `Catalog field`: 이 카탈로그 내의 특정 필드(열 이름)
- `Value`: 해당 필드 또는 열 내의 특정 값 <br><br> 건강 앱을 예로 들어 예약할 수 있는 각 의사의 카탈로그에 `vision` 또는 `dental` 와 같은 값을 포함하는 `specialty` 라는 필드가 있다고 가정해 보겠습니다. `dental` 값으로 의사를 방문한 적이 있는 사용자를 세분화하려면 `specialty` 을 `Catalog field` 으로 선택하고 `dental` 을 `Value` 으로 선택하면 됩니다.

5. SQL 세그먼트를 만든 후에는 **미리 보기 실행을** 클릭하여 쿼리가 사용자를 반환하는지 또는 오류가 있는지 확인하는 것이 좋습니다. [쿼리 결과 미리 보기]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/#previewing-results), [SQL 세그먼트 확장]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/#managing-sql-segment-extensions) 관리 등에 대한 자세한 내용은 [SQL 세그먼트 확장을]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/) 참조하세요. 

{% alert note %}
`CATALOGS_ITEMS_SHARED` 테이블을 사용하는 SQL 세그먼트를 생성하는 경우 카탈로그 ID를 지정해야 합니다. 예를 들어

```sql
SELECT * FROM CATALOGS_ITEMS_SHARED
WHERE CATALOG_ID = 'XYZ'
LIMIT 10
```
{% endalert %}

### SQL 반전 필요 여부 결정하기

이벤트가 0건인 사용자를 직접 쿼리할 수는 없지만, **반전 SQL을** 사용하여 이러한 사용자를 타겟팅할 수 있습니다.

예를 들어 구매 횟수가 3개 미만인 사용자를 타겟팅하려면 먼저 구매 횟수가 3개 이상인 사용자를 선택하는 쿼리를 작성합니다. 그런 다음 **SQL 반전을** 선택하여 구매 횟수가 3건 미만인 사용자(구매 횟수가 0건인 사용자 포함)를 타겟팅합니다.

세그먼트 확장의 이름은 "지난 30일 동안 1~4개의 이메일을 클릭함"이며 SQL 반전 옵션이 선택되어 있습니다.]({% image_buster /assets/img_archive/sql_segment_invert_sql.png %}){: style="max-width:70%;"}

{% alert important %}
이벤트가 전혀 없는 사용자를 타겟팅하는 것이 목적이 아니라면 SQL을 반전할 필요가 없습니다. **SQL 반전을** 선택한 경우 해당 기능이 필요한지, 세그먼트가 원하는 오디언스와 일치하는지 확인합니다. 예를 들어, 쿼리가 이벤트가 하나 이상 있는 사용자를 타겟팅하는 경우 반전 시 이벤트가 0인 사용자만 타겟팅합니다.
{% endalert %}

## 세그먼트 멤버십 새로고침

카탈로그 세그먼트의 세그먼트 멤버십을 새로고침하려면 카탈로그 세그먼트를 열고 **작업** > **새로고침** > **예, 새로고침을** 선택합니다.

{% alert tip %}
사용자가 정기적으로 들어오고 나갈 것으로 예상되는 세그먼트를 만든 경우, 캠페인이나 캔버스에서 해당 세그먼트를 타겟팅하기 전에 해당 세그먼트가 사용하는 카탈로그 세그먼트를 수동으로 새로고침하세요.
{% endalert %}

### 새로고침 설정 지정하기

{% multi_lang_include segments.md section='Refresh settings' %}

## 사용 사례

{% tabs local %}
{% tab Health %}

### 건강 앱

건강 앱이 있고 치과 방문을 예약한 사용자를 세그먼트화하고자 한다고 가정해 보겠습니다. 또한 다음 사항도 있습니다:

- 환자가 예약할 수 있는 다양한 의사가 포함된 카탈로그 `Doctors`. `doctor ID`
- 카탈로그의 `doctor ID` 필드와 동일한 값을 공유하는 `doctor ID` 속성을 가진 커스텀 이벤트 `Booked Visit` 
- `dental` 값이 포함된 카탈로그 내 `speciality` 필드

다음 변수를 사용하여 카탈로그 세그먼트를 설정합니다:

| 변수 | 속성 |
| --- | --- |
| `Catalog`| 의사 |
| `Catalog field` | 의사 ID |
| `Custom event`| 방문 예약|
| `Custom event property` | 의사 ID |
| `(Under Filter SQL Results) Catalog field` | 스페셜티 |
| `(Under Filter SQL Results) Value`| 치과 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab SaaS %}

### SaaS 플랫폼

B2B SaaS 플랫폼이 있고 기존 고객의 직원인 사용자를 세그먼트화하고자 한다고 가정해 보겠습니다. 또한 다음 사항도 있습니다:

- 현재 SaaS 플랫폼을 사용 중인 여러 계정이 포함된 카탈로그( `Accounts` )로, 각각에 할당된 `account ID`
- 카탈로그의 "계정 ID" 필드와 동일한 값을 공유하는 "계정 ID" 속성을 가진 커스텀 이벤트 `Event Attendance` 
- `enterprise` 값이 포함된 카탈로그 내 `Classification` 필드

다음 변수를 사용하여 카탈로그 세그먼트를 설정합니다:

| 변수 | 속성 |
| --- | --- |
| `Catalog` | 계정 |
| `Catalog field `| 계정 ID |
| `Custom event` | 이벤트 참석 |
| `Custom event property` | 계정 ID |
| `(Under Filter SQL Results) Catalog field` | 분류 |
| `(Under Filter SQL Results) Value` | 엔터프라이즈 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

## 자주 묻는 질문

### 카탈로그 세그먼트를 실행하면 SQL 세그먼트 확장 크레딧이 소모되나요?

예, 카탈로그 세그먼트는 SQL로 구동되며 SQL 세그먼트 확장 크레딧을 소비합니다. 자세히 알아보려면 [SQL 세그먼트 사용법을]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments#monitoring-your-sql-segments-usage) 확인하세요.

### 카탈로그 세그먼트를 만들면 SQL 세그먼트 확장 할당을 사용하나요?

예. SQL 세그먼트 확장이 세그먼트 확장 할당량에 포함되는 것과 같은 방식으로 카탈로그 세그먼트도 해당 할당량에 포함됩니다.

### 현재 템플릿이 제공하지 않는 카탈로그 세그먼트 사용 사례가 있습니다. 어떻게 설정해야 하나요?

추가 안내가 필요하면 고객 지원 매니저 또는 [Braze 지원팀에]({{site.baseurl}}/user_guide/administrative/access_braze/support/) 문의하세요.

