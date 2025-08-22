---
nav_title: "카탈로그 세그먼트"
article_title: 카탈로그 세그먼트
page_order: 1
page_type: reference
alias: "/catalog_segments/"
description: "이 문서에서는 SQL 세그먼트 확장에서 카탈로그 데이터를 사용하여 사용자 오디언스를 구축하는 카탈로그 세그먼트를 만드는 방법에 대해 설명합니다."
tool: Segments
---

# 카탈로그 세그먼트

> 카탈로그 세그먼트는 카탈로그 데이터를 사용자 지정 이벤트 또는 구매의 데이터와 결합하여 생성되는 SQL 세그먼트 확장의 한 유형입니다. 세그먼트에서 참조한 다음 캠페인 및 캔버스에서 타겟팅할 수 있습니다. 

{% alert important %}
카탈로그 세그먼트는 현재 얼리 액세스 중입니다. 이 얼리 액세스에 참여하려면 고객 성공 매니저에게 문의하세요.
{% endalert %}

카탈로그 세그먼트는 SQL을 사용하여 카탈로그의 데이터와 사용자 지정 이벤트 또는 구매의 데이터를 조인합니다. 이렇게 하려면 카탈로그와 커스텀 이벤트 또는 구매에 공통 식별자 필드가 있어야 합니다. 예를 들어 카탈로그의 항목 ID 값은 커스텀 이벤트의 속성 값과 일치해야 합니다.

## 카탈로그 세그먼트 만들기

1. Go to **Segment Extensions** > **Create New Extension** > **Start With Template** and select a template. <br>![Modal with the option to create a catalog segment for events or purchases.]({% image_buster /assets/img/catalog-segments-template.png %}){: style="max-width:80%" }

{: start="2"}
2\. SQL 편집기에 템플릿이 자동으로 채워집니다. <br>![SQL editor with a pregenerated template.]({% image_buster /assets/img/catalog-segments-editor.png %}){: style="max-width:80%" }<br>이 템플릿은 사용자 이벤트 데이터를 카탈로그 데이터와 조인하여 특정 카탈로그 항목에 참여한 사용자를 세분화합니다.

3. 세그먼트를 생성하기 전에 **변수** 탭을 사용하여 템플릿에 필요한 필드를 입력합니다. <br>Braze가 카탈로그 항목에 대한 인게이지먼트를 기반으로 사용자를 식별하려면 다음을 수행해야 합니다. <br> \- 카탈로그 필드가 포함된 카탈로그를 선택합니다. <br> \- 이벤트 속성이 포함된 사용자 지정 이벤트를 선택합니다. <br> \- 카탈로그 필드와 이벤트 속성 값 일치

변수를 선택하기 위한 가이드라인은 다음과 같습니다:

| 가변 필드 | 설명 |
| --- | --- |
| `Catalog` | 사용자를 타깃팅하는 데 사용하는 카탈로그의 이름입니다. |
| `Catalog field`| 카탈로그에서 `Custom event property` 과 동일한 값을 포함하는 필드입니다. 이것은 종종 ID의 한 유형입니다. In the eCommerce use case, this would be `shopify_id`. |
| `Custom event` | `Catalog field` 과 일치하는 값을 가진 속성을 포함하는 동일한 이벤트인 사용자 지정 이벤트의 이름입니다. In the eCommerce use case, this would be `Made Order`. |
| `Custom event property` | `Catalog field` 와 값을 일치시키는 사용자 지정 이벤트 속성의 이름입니다. In the eCommerce example use case, this would be `Shopify_ID.`|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{: start="4"}
4\. 필요한 경우 사용 사례에 대한 추가 선택 필드를 입력하여 카탈로그 내의 특정 필드 값으로 세분화할 수 있습니다:
- `Catalog field`: 이 카탈로그 내의 특정 필드(열 이름)
- `Value`: 해당 필드 또는 열 내의 특정 값 <br><br> 건강 앱을 예로 들어 예약할 수 있는 각 의사의 카탈로그에 `vision` 또는 `dental` 와 같은 값을 포함하는 `specialty` 라는 필드가 있다고 가정해 보겠습니다. `dental` 값을 가진 의사를 방문한 사용자를 세분화하려면 `specialty`를 `Catalog field`로 선택하고 `dental`을 `Value`로 선택하면 됩니다.

5. SQL 세그먼트를 생성한 후에는 **미리 보기 실행**을 클릭하여 쿼리가 사용자를 반환하는지 또는 오류가 있는지 확인하는 것이 좋습니다. [쿼리 결과 미리 보기]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/#previewing-results), [SQL 세그먼트 확장]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/#managing-sql-segment-extensions) 관리 등에 대한 자세한 내용은 [SQL 세그먼트 확장]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/)을 참조하세요. 

{% alert note %}
If you're creating a SQL segment that uses the table `CATALOGS_ITEMS_SHARED`, you must specify a catalog ID. For example:

```sql
SELECT * FROM CATALOGS_ITEMS_SHARED
WHERE CATALOG_ID = 'XYZ'
LIMIT 10
```
{% endalert %}

## Refreshing segment membership

To refresh the segment membership of any catalog segment, open the catalog segment and select **Actions** > **Refresh** > **Yes, Refresh**.

{% alert tip %}
If you created a segment where you expect users to enter and exit regularly, manually refresh the catalog segment it uses before targeting that segment in a campaign or Canvas.
{% endalert %}

### Designating refresh settings

{% multi_lang_include segments.md section='Refresh settings' %}

## 사용 사례

### 건강 앱

건강 앱이 있고 치과 방문을 예약한 사용자를 세분화하고자 한다고 가정해 보겠습니다. 또한 다음 사항도 있습니다:

- 각각 `doctor ID`가 할당되어 있으며 환자가 예약할 수 있는 다양한 의사가 포함된 `Doctors` 카탈로그
- 카탈로그의 `doctor ID` 필드와 동일한 값을 공유하는 `doctor ID` 속성정보를 가진 커스텀 이벤트 `Booked Visit`
- `dental` 값이 포함된 카탈로그 내 `speciality` 필드

다음 변수를 사용하여 카탈로그 세그먼트를 설정할 수 있습니다:

| 변수 | 등록정보 |
| --- | --- |
| `Catalog`| 의사 |
| `Catalog field` | 의사 ID |
| `Custom event`| 방문 예약|
| `Custom event property` | 의사 ID |
| `(Under Filter SQL Results) Catalog field` | 전문 분야 |
| `(Under Filter SQL Results) Value`| 치과 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### SaaS 플랫폼

B2B SaaS 플랫폼이 있고 기존 고객의 직원인 사용자를 세분화하고자 한다고 가정해 보겠습니다. 또한 다음 사항도 있습니다:

- 현재 SaaS 플랫폼을 사용 중인 여러 계정이 포함된 카탈로그 `Accounts`, 각각에 할당된 `account ID`
- 카탈로그의 "계정 ID" 필드와 동일한 값을 공유하는 "계정 ID" 속성정보를 가진 커스텀 이벤트 `Event Attendance`
- `enterprise` 값이 포함된 카탈로그 내 `Classification` 필드

다음 변수를 사용하여 카탈로그 세그먼트를 설정할 수 있습니다:

| 변수 | 등록정보 |
| --- | --- |
| `Catalog` | 계좌 |
| `Catalog field `| 계정 ID |
| `Custom event` | 이벤트 참석 |
| `Custom event property` | 계정 ID |
| `(Under Filter SQL Results) Catalog field` | 분류 |
| `(Under Filter SQL Results) Value` | 엔터프라이즈 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 자주 묻는 질문

### 카탈로그 세그먼트를 실행하면 SQL 세그먼트 확장 크레딧이 소모되나요?

예, 카탈로그 세그먼트는 SQL로 구동되며 SQL 세그먼트 확장 크레딧을 사용합니다. 자세히 알아보려면 [SQL 세그먼트 사용법을]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments#monitoring-your-sql-segments-usage) 확인하세요.

### 카탈로그 세그먼트를 만들면 SQL 세그먼트 확장 할당을 사용하나요?

예. SQL 세그먼트 확장이 세그먼트 확장 할당량에 포함되는 것과 마찬가지로 카탈로그 세그먼트도 해당 할당량에 포함됩니다.

### 현재 템플릿이 지원하지 않는 카탈로그 세그먼트 사용 사례가 있습니다. 어떻게 설정해야 하나요?

추가 안내가 필요하면 고객 지원 관리자 또는 [Braze 지원팀에]({{site.baseurl}}/user_guide/administrative/access_braze/support/) 문의하세요.

