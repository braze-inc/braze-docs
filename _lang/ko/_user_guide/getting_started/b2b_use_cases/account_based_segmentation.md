---
nav_title: 계정 기반 세분화
article_title: 계정 기반 세분화 설정
page_order: 2
page_type: reference
description: "다양한 Braze 기능을 사용하여 B2B 계정 기반 세분화 사용 사례를 강화하는 방법을 알아보세요."
---

# 계정 기반 세분화 설정

> 이 페이지에서는 B2B 계정 기반 세분화 사용 사례를 강화하기 위해 다양한 Braze 기능을 사용하는 방법을 보여줍니다.

You can do B2B account-based segmentation in two ways, depending on how you set up your [B2B data model]({{site.baseurl}}/user_guide/getting_started/b2b_use_cases/b2b_data_models/):

- [비즈니스 개체에 카탈로그를](#option-1-when-using-catalogs-for-your-business-objects) 사용하는 경우
- [비즈니스 개체에 연결된 소스를](#option-2-when-using-connected-sources-for-your-business-objects) 사용하는 경우

## B2B 계정 기반 세분화 설정

### 옵션 1: 비즈니스 개체에 카탈로그를 사용하는 경우

#### 기본 SQL 템플릿 세분화

시작하는 데 도움을 드리기 위해 간단한 계정 기반 세분화를 위한 기본 SQL 템플릿을 만들었습니다.

대상 기업 계정의 직원인 사용자를 세분화하고자 한다고 가정해 보겠습니다. 

1. **대상** > **세그먼트 확장** > **새 확장 만들기** > **템플릿으로 시작으로** 이동하여 **이벤트용 카탈로그 세그먼트** 템플릿을 선택합니다. <br><br> !["이벤트 또는 구매를 위한 카탈로그 세그먼트 옵션이 있는 '템플릿 선택' 모달을 선택합니다.][1]<br><br>SQL 편집기는 사용자 이벤트 데이터를 카탈로그 데이터와 조인하여 특정 카탈로그 항목에 참여하는 사용자를 세분화하는 템플릿으로 자동으로 채워집니다. <br><br>!['변수' 탭이 열려 있는 새 확장을 위한 SQL 편집기입니다.][2]<br><br>
2. 세그먼트를 생성하기 전에 **변수** 탭을 사용하여 템플릿에 필요한 필드를 입력합니다.<br><br>Braze가 카탈로그 항목에 대한 인게이지먼트를 기반으로 사용자를 식별하려면 다음을 수행해야 합니다.
- 카탈로그 필드가 포함된 카탈로그를 선택합니다.
- 이벤트 속성이 포함된 사용자 지정 이벤트를 선택합니다.
- 카탈로그 필드와 이벤트 속성 값 일치

##### B2B 사용 사례를 위한 변수 가이드라인

B2B 계정 기반 세분화 사용 사례에 대해 다음 변수를 선택합니다:

| 변수 | 등록정보 |
| --- | --- |
| 카탈로그 | 계정 카탈로그 |
| 카탈로그 필드 | ID |
| 사용자 지정 이벤트 | 계정_연결 |
| 사용자 지정 이벤트 등록정보 | 계정_id |
| (SQL 결과 필터링 아래) 카탈로그 필드 | 분류 |
| (SQL 결과 필터링 아래) 값 | 엔터프라이즈 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### 정교한 SQL 세분화

보다 정교하거나 복잡한 세분화는 [SQL 세그먼트 확장을]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/) 참조하세요. 시작하는 데 도움이 되도록 B2B 계정 기반 세분화를 시작하는 데 사용할 수 있는 몇 가지 SQL 템플릿을 소개합니다:

1. 단일 카탈로그에서 두 개의 필터를 비교하는 세그먼트를 만듭니다(예: 엔터프라이즈급 계정의 레스토랑 업계에 종사하는 사용자). 카탈로그 ID와 항목 ID를 포함해야 합니다.

```sql
WITH salesforce_accounts AS (
   SELECT
       ITEM_ID as id,
       MAX(CASE WHEN FIELD_NAME = 'Industry' THEN FIELD_VALUE END) AS Industry,
       MAX(CASE WHEN FIELD_NAME = 'Classification' THEN FIELD_VALUE END) AS Classification,
   FROM CATALOGS_ITEMS_SHARED
   WHERE CATALOG_ID = '6655ef5213ea0f00591816e2' -- salesforce_accounts
   GROUP BY ITEM_ID
)
SELECT DISTINCT events.USER_ID
FROM USERS_BEHAVIORS_CUSTOMEVENT_SHARED as events
JOIN salesforce_accounts
ON TRY_PARSE_JSON(events.properties):account_id::STRING = salesforce_accounts.id
WHERE events.name = 'account_linked'
AND salesforce_accounts.Industry = 'Restaurants'
AND salesforce_accounts.Classification = 'Enterprise'
; 
```

{: start="2"}
2\. 두 개의 개별 카탈로그에서 두 개의 필터를 비교하는 세그먼트를 만듭니다(예: '3단계' 기회가 열려 있는 기업 대상 계정과 연결된 사용자).

```sql
-- Reformat catalog data into a table with columns for each field
WITH salesforce_accounts AS (
   SELECT
       ITEM_ID as id,
       MAX(CASE WHEN FIELD_NAME = 'Industry' THEN FIELD_VALUE END) AS Industry,
       MAX(CASE WHEN FIELD_NAME = 'Classification' THEN FIELD_VALUE END) AS Classification,
   FROM CATALOGS_ITEMS_SHARED
   WHERE CATALOG_ID = '6655ef5213ea0f00591816e2' -- salesforce_accounts
   GROUP BY ITEM_ID
),
salesforce_opportunities AS (
   SELECT
       ITEM_ID as id,
       MAX(CASE WHEN FIELD_NAME = 'Account_ID' THEN FIELD_VALUE END) AS Account_ID,
       MAX(CASE WHEN FIELD_NAME = 'Stage' THEN FIELD_VALUE END) AS Stage,
   FROM CATALOGS_ITEMS_SHARED
   WHERE CATALOG_ID = '6655f84a348f0f0059ad0627' -- salesforce_opportunities
   GROUP BY ITEM_ID
)
SELECT DISTINCT events.USER_ID
FROM USERS_BEHAVIORS_CUSTOMEVENT_SHARED as events
JOIN salesforce_accounts
ON TRY_PARSE_JSON(events.properties):account_id::STRING = salesforce_accounts.id
JOIN salesforce_opportunities
ON salesforce_accounts.id = salesforce_opportunities.Account_ID
WHERE events.name = 'account_linked'
AND salesforce_accounts.Industry = 'Restaurants'
AND salesforce_opportunities.Stage = 'Closed Won'
;
```

### 옵션 2: 비즈니스 개체에 연결된 소스를 사용하는 경우

세분화에서 연결된 소스를 사용하는 방법에 대한 기본 사항은 [CDI 세그먼트를]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/cdi_segments/) 참조하세요. 원하는 방식으로 서식을 지정할 수 있으므로 [카탈로그 사용 시에서](#option-1-when-using-catalogs-for-your-business-objects) 다루는 템플릿을 사용하여 소스 테이블의 서식을 지정하는 방법에 대한 영감을 얻을 수 있습니다.

## 세그먼트에서 계정 기반 확장 프로그램 사용

위 단계에서 계정 수준 세분화를 생성한 후에는 해당 세그먼트 확장을 타겟팅 기준으로 바로 가져올 수 있습니다. 또한 역할, 이전 캠페인 참여도 등과 같은 사용자 인구통계학적 기준을 점진적으로 적용하여 쉽게 레이어링할 수 있습니다. 자세한 내용은 [세그먼트에서 확장 프로그램 사용하기를]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/#step-6-use-your-extension-in-a-segment) 참조하세요.

[1]: {% image_buster /assets/img/b2b/select_a_template.png %}
[2]: {% image_buster /assets/img/b2b/enter_new_name.png %}
