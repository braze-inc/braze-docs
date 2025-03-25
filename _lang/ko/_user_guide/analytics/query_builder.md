---
nav_title: 퀴리 빌더
article_title: 퀴리 빌더
page_order: 15
page_type: reference
description: "이 참조 문서에서는 Query Builder에서 Snowflake의 Braze 데이터를 사용하여 보고서를 구축하는 방법을 설명합니다."
tool: Reports
---

# 퀴리 빌더

> 쿼리 빌더는 Snowflake의 Braze 데이터를 사용하여 보고서를 생성합니다. 쿼리 빌더는 시작할 수 있도록 미리 작성된 SQL [쿼리 템플릿]({{site.baseurl}}/user_guide/analytics/query_builder/query_templates/)과 함께 제공되며, 직접 커스텀 SQL 쿼리를 작성하여 더 많은 인사이트를 얻을 수 있습니다.

쿼리 빌더는 일부 고객 데이터에 직접 액세스할 수 있으므로 "PII 보기" [권한]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/)이 있는 경우에만 쿼리 빌더에 액세스할 수 있습니다.

## 쿼리 빌더에서 보고서 실행

쿼리 빌더 보고서를 실행하는 방법:

1. **분석** > **쿼리 빌더**로 이동합니다.

{% alert note %}
[이전 탐색]({{site.baseurl}}/navigation)을 사용하는 경우 **쿼리 빌더**를 **데이터** 아래에서 찾을 수 있습니다.
{% endalert %}

{:start="2"}
2\. **SQL 쿼리 만들기**을 선택하십시오. 영감이나 도움을 받아 쿼리를 작성하려면 **쿼리 템플릿**을 선택하고 목록에서 템플릿을 선택하세요. 그렇지 않으면 편집기로 바로 이동하려면 **SQL Editor**를 선택하십시오.
3\. 보고서는 현재 날짜와 시간으로 자동으로 이름이 지정됩니다. 이름 위에 마우스를 올리고 <i class="fas fa-pencil" alt="Edit"></i>을 선택하여 SQL 쿼리에 의미 있는 이름을 지정하세요.
4\. 편집기에서 SQL 쿼리를 작성하거나 **AI 쿼리 빌더** 탭에서 [AI](#ai-query-builder)의 도움을 받으세요. 자체 SQL을 작성하는 경우, 요구 사항 및 리소스에 대해서는 [커스텀 SQL 쿼리 작성](#custom-sql)을 참조하세요.
5\. **쿼리 실행**을 선택합니다.
6\. 쿼리를 저장합니다.
7\. 보고서의 CSV를 다운로드하려면 **내보내기**를 선택하세요.

![쿼리 빌더가 템플릿 쿼리 "채널 인게이지먼트 및 매출 지난 30일 동안"에 대한 결과를 보여줍니다.]({% image_buster /assets/img_archive/query_builder.png %})

각 보고서의 결과는 하루에 한 번 생성할 수 있습니다. 하루에 같은 보고서를 한 번 이상 실행하면 두 보고서에서 동일한 결과를 볼 수 있습니다.

### 쿼리 템플릿

보고서를 처음 만들 때 **SQL 쿼리 만들기** > **쿼리 템플릿을** 선택하여 쿼리 템플릿에 액세스합니다.

[쿼리 템플릿]({{site.baseurl}}/user_guide/analytics/query_builder/query_templates/)을 참조하여 사용 가능한 템플릿 목록을 확인하세요.

### 데이터 기간

모든 쿼리는 지난 60일 동안의 데이터를 표시합니다. 

## AI 쿼리 빌더로 SQL 생성

AI 쿼리 빌더는 [GPT](https://openai.com/gpt-4)를 활용하여 OpenAI에서 제공하는 SQL을 추천합니다.

![][2]{: style="max-width:60%;" }

AI 쿼리 빌더를 사용하여 SQL을 생성하는 방법:

1. 쿼리 빌더에서 보고서를 만든 후 **AI 쿼리 빌더** 탭을 선택합니다.
2. 프롬프트를 입력하거나 샘플 프롬프트를 선택하고 **생성**을 선택하여 프롬프트를 SQL로 번역하십시오.
3. 생성된 SQL을 검토하여 올바른지 확인한 다음 **편집기에 삽입**을 선택합니다.

### 팁

- 사용 가능한 [Snowflake 데이터 테이블]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/sql_segments_tables/)에 익숙해집니다. 이러한 테이블에 존재하지 않는 데이터를 요청하면 ChatGPT가 가짜 테이블을 구성하게 될 수 있습니다.
- 이 기능에 대한 [SQL 작성 규칙을]({{site.baseurl}}/user_guide/data_and_analytics/query_builder/#custom-sql) 숙지하세요. 이 규칙을 따르지 않으면 오류가 발생합니다.
- AI 쿼리 빌더를 사용하여 분당 최대 20개의 프롬프트를 보낼 수 있습니다.

### 내 데이터는 어떻게 사용되고 OpenAI로 전송되나요?
<!-- Contact Legal for changes. -->

SQL을 생성하기 위해 Braze는 사용자의 프롬프트를 OpenAI의 API 플랫폼으로 전송합니다. Braze에서 OpenAI로 전송되는 모든 쿼리는 익명으로 처리되므로, 사용자가 제공하는 콘텐츠에 고유 식별 정보를 포함하지 않는 한 OpenAI는 해당 쿼리가 누구로부터 전송되었는지 확인할 수 없습니다. [OpenAI의 API 플랫폼](https://openai.com/policies/api-data-usage-policies) 약관에 명시된 바와 같이, Braze를 통해 OpenAI의 API로 전송된 데이터는 모델을 학습하거나 개선하는 데 사용되지 않으며 30일 후에 삭제됩니다. [사용 정책](https://openai.com/policies/usage-policies)을 포함하여 사용자와 관련된 OpenAI의 정책을 준수해야 합니다. Braze는 AI 생성 콘텐츠에 대해 어떠한 종류의 보증도 하지 않습니다. 

## 커스텀 SQL 쿼리 작성 {#custom-sql}

[Snowflake syntax](https://docs.snowflake.com/en/sql-reference)를 사용하여 SQL 쿼리를 작성하십시오. 전체 테이블 및 쿼리할 수 있는 열 목록은 [테이블 참조]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/sql_segments_tables/)를 참조하십시오.

쿼리 빌더 내에서 테이블 세부 정보를 보려면:

1. **쿼리 빌더** 페이지에서 **참조** 패널을 열고 **사용 가능한 데이터 테이블**을 선택하여 사용 가능한 데이터 테이블과 그 이름을 확인합니다.
3. <i class="fas fa-chevron-down" alt=""></i> **자세히 보기**를 선택하여 테이블 설명 및 데이터 유형과 같은 테이블 열에 대한 정보를 확인하십시오.
4. SQL에 테이블 이름을 삽입하려면 <i class="fas fa-copy" title="SQL 편집기에 테이블 이름 복사"></i>을 선택하십시오.

Braze에서 제공하는 미리 작성된 쿼리를 사용하려면 Query Builder에서 보고서를 처음 만들 때 **쿼리 템플릿**을 선택하세요.

특정 기간으로 쿼리를 제한하면 더 빠르게 결과를 생성할 수 있습니다. 다음은 지난 한 시간 동안 발생한 구매 수와 매출을 가져오는 예제 쿼리입니다.

```sql
SELECT COUNT(*) as Purchases, SUM(price) as Revenue
FROM USERS_BEHAVIORS_PURCHASE_SHARED
WHERE to_date(to_timestamp_ntz(time)) >= DATEADD('hour', -1, date_trunc('day',CURRENT_DATE()));
```

이 쿼리는 지난 달에 보낸 이메일 수를 검색합니다.

```sql
SELECT COUNT(*) as Sends
FROM USERS_MESSAGES_EMAIL_SEND_SHARED
WHERE to_date(to_timestamp_ntz(time)) >= DATEADD('month', -1, date_trunc('day',CURRENT_DATE()));
```

`CANVAS_ID`, `CANVAS_VARIATION_API_ID` 또는 `CAMPAIGN_ID` 에 대해 쿼리하는 경우 관련 이름 열이 자동으로 결과 테이블에 포함됩니다. `SELECT` 쿼리 자체에 포함할 필요는 없습니다.

| ID 이름 | 연관된 이름 열 |
| --- | --- |
| `CANVAS_ID` | 캔버스 이름 |
| `CANVAS_VARIATION_API_ID` | 캔버스 변형 이름 |
| `CAMPAIGN_ID` | 캠페인 이름 |
{: .reset-td-br-1 .reset-td-br-2 }

이 쿼리는 최대 100개의 행으로 세 개의 ID와 연결된 이름 열을 모두 검색합니다:

```sql
SELECT CANVAS_ID, CANVAS_VARIATION_API_ID, CAMPAIGN_ID
FROM USERS_MESSAGES_EMAIL_SEND_SHARED 
LIMIT 100
```

### 문제 해결

다음과 같은 이유로 쿼리가 실패할 수 있습니다:

- SQL 쿼리의 구문 오류
- 처리 시간 초과 (6분 후)
    - 6분 이상 실행되는 보고서는 시간 초과됩니다.
    - 보고서가 시간 초과되면 쿼리하는 데이터의 시간 범위를 제한하거나 더 구체적인 데이터 세트를 쿼리해 봅니다.

## 변수 사용

변수를 사용하여 SQL에서 미리 정의된 변수 유형을 사용하여 값을 참조하고 값을 수동으로 복사할 필요가 없습니다. 예를 들어, 캠페인의 ID를 SQL 편집기에 수동으로 복사하는 대신, {% raw %}`{{campaign.${My campaign}}}`{% endraw %}을 사용하여 **변수** 탭의 드롭다운에서 캠페인을 직접 선택할 수 있습니다.

![][3]

변수가 생성된 후에는 쿼리 빌더 보고서의 **변수** 탭에 나타납니다. SQL 변수를 사용하는 이점은 다음과 같습니다:

- 캠페인 ID를 붙여넣는 대신 보고서를 작성할 때 목록에서 선택할 수 있는 캠페인 변수를 만들어 시간을 저장하세요.
- 변수를 추가하여 값을 교체하면 나중에 약간 다른 사용 사례(예: 다른 커스텀 이벤트)에 대해 보고서를 재사용할 수 있습니다.
- 각 보고서에 필요한 편집 양을 줄여 SQL을 편집할 때 사용자 오류를 줄입니다. SQL에 더 익숙한 팀원들은 기술적이지 않은 팀원들이 사용할 수 있는 보고서를 만들 수 있습니다.

### 지침

변수가 준수해야 하는 Liquid 구문: {% raw %}`{{ type.${name}}}`{% endraw %}, 여기서 `type`은 허용된 유형 중 하나여야 하며 `name`은 선택할 수 있는 아무 것이나 될 수 있습니다. 이 변수들의 레이블은 기본값으로 변수 이름이 됩니다.

기본값으로, 모든 변수는 필수입니다 (변수 값이 선택되지 않으면 보고서가 실행되지 않습니다) 날짜 범위를 제외하고, 값이 제공되지 않으면 기본값은 지난 30일입니다.

### 변수 유형

다음 변수 유형이 허용됩니다:

- [숫자](#number)
- [날짜 범위](#date-range)
- [메시징](#messaging)
- [제품](#products)
- [사용자 지정 이벤트](#custom-events)
- [커스텀 이벤트 속성](#custom-event-properties)
- [워크스페이스](#workspace)
- [카탈로그](#catalogs)
- [카탈로그 필드](#catalog-fields)
- [옵션](#options)
- [세그먼트](#segments)
- [문자열](#string)
- [태그](#tags)

#### 숫자

- **대체 값:** 제공된 값, 예를 들어 `5.5`
- **사용 예:** {% raw %}`some_number_column < {{number.${some name}}}`{% endraw %}

#### 날짜 범위

![][4]{: style="max-width:50%;"}

둘 다 `start_date` 및 `end_date`를 사용하는 경우 날짜 범위로 사용할 수 있도록 동일한 이름을 가져야 합니다.

##### 예시 값

날짜 범위 유형은 상대적일 수 있으며, 시작 날짜, 종료 날짜 또는 날짜 범위일 수 있습니다.

두 가지 모두 `start_date` 및 `end_date`가 동일한 이름으로 사용되는 경우 네 가지 유형이 모두 표시됩니다. 하나만 사용되는 경우 관련 유형만 표시됩니다.

| 날짜 범위 유형 | 설명 | 필수 값 |
| --- | --- | --- |
| 상대 | 지정된 지난 X일 | `start_date` 필요 |
| 시작일 | 시작 날짜를 지정합니다 | `start_date` 필요 |
| 종료일 | 종료 날짜를 지정합니다 | `end_date` 필요 |
| 날짜 범위 | 시작 날짜와 종료 날짜를 모두 지정합니다 | `start_date` 및 `end_date` 모두 필요합니다 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

- **대체 값:** `start_date` 및 `end_date`를 UTC의 지정된 날짜에 대한 초 단위의 Unix 타임스탬프로 대체합니다. 예: `1696517353`.
- **사용 예:** 모든 상대, 시작 날짜, 종료 날짜 및 날짜 범위 변수에 대해:
    - {% raw %}`time > {{start_date.${some name}}} AND time < {{end_date.${some name}}}` {% endraw %}
        - 날짜 범위를 원하지 않는 경우 `start_date` 또는 `end_date`를 사용할 수 있습니다.

#### 메시징

모든 메시징 변수는 하나의 그룹에서 상태를 결합하려면 동일한 식별자를 공유해야 합니다.

![][5]{: style="max-width:50%;"}

##### 캔버스

하나의 캔버스를 선택하기 위해서. 캠페인과 동일한 이름을 공유하면 **변수** 탭 내에서 라디오 버튼이 생성되어 캔버스 또는 캠페인을 선택할 수 있습니다.

- **대체 값:** 캔버스 BSON ID
- **사용 예:** {% raw %}`canvas_id = ‘{{canvas.${some name}}}’`{% endraw %}

##### 캔버스

여러 캔버스를 선택하려면. 캠페인과 동일한 이름을 공유하면 **변수** 탭 내에서 캔버스 또는 캠페인을 선택할 수 있는 라디오 버튼이 생성됩니다.

- **대체 값:** 캔버스 BSON ID
- **사용 예:** {% raw %}`canvas_id IN ({{canvases.${some name}}})`{% endraw %}

##### 캠페인

하나의 캠페인을 선택하기 위해. Canvas와 동일한 이름을 공유하면 **변수** 탭 내에서 Canvas 또는 캠페인을 선택하기 위한 라디오 버튼이 생성됩니다.

- **대체 값:** 캠페인 BSON ID
- **사용 예:** {% raw %}`campaign_id = ‘{{campaign.${some name}}}’`{% endraw %}

##### 캠페인

캠페인을 다중 선택하기 위해. Canvas와 동일한 이름을 공유하면 **변수** 탭 내에서 Canvas 또는 캠페인을 선택할 수 있는 라디오 버튼이 생성됩니다.

- **대체 값:** 캠페인 BSON ID
- **사용 예:** {% raw %}`campaign_id IN ({{campaigns.${some name}}})`{% endraw %}

##### 캠페인 변형

선택한 캠페인에 속하는 캠페인 변형을 선택하기 위해. 캠페인 또는 캠페인 변수와 함께 사용해야 합니다.

- **대체 값:** 캠페인 변형 API ID, 쉼표로 구분된 문자열 예: `api-id1, api-id2`.
- **사용 예:** {% raw %}`message_variation_api_id IN ({{campaign_variants.${some name}}})`{% endraw %}

##### 캔버스 변형

선택한 캔버스에 속하는 캔버스 변형을 선택하기 위해. 캔버스 또는 캔버스 변수를 사용해야 합니다.

- **대체 값:** 캔버스 배리언트 API ID, `api-id1, api-id2`와 같이 쉼표로 구분된 문자열.
- **사용 예:** {% raw %}`canvas_variation_api_id IN ({{canvas_variants.${some name}}})`{% endraw %}

##### 캔버스 단계

선택한 캔버스에 속하는 캔버스 단계를 선택하기 위해서. 캔버스 변수와 함께 사용해야 합니다.

- **대체 값:** 캔버스 단계 API ID
- **사용 예:** {% raw %}`canvas_step_api_id = ‘{{canvas_step.${some name}}}’`{% endraw %}

##### 캔버스 단계 수

선택한 캔버스에 속하는 캔버스 단계를 선택하기 위해. 캔버스 또는 캔버스 변수를 사용해야 합니다.

- **대체 값:** 캔버스 단계 API ID
- **사용 예:** {% raw %}`canvas_step_api_id IN ({{canvas_steps.${some name}}})`{% endraw %}

#### 제품

제품 이름 목록을 선택하기 위해.

- **대체 값:** 제품 names are surrounded by single quotes and separated by commas, such as in `product1, product2`
- **사용 예:** {% raw %}`product_id IN ({{products.${product name (optional)}}})`{% endraw %}

#### 사용자 지정 이벤트

커스텀 이벤트 목록을 선택하기 위해.

- **대체 값:** 커스텀 이벤트 속성정보 이름은 `event1, event2`와 같이 쉼표로 구분됩니다.
- **사용 예:** {% raw %}`name = ‘{{custom_events.${event names)}}}’`{% endraw %}

#### 커스텀 이벤트 속성

커스텀 이벤트 속성정보 이름 목록을 선택하기 위해. 커스텀 이벤트 변수와 함께 사용해야 합니다.

- **대체 값:** 커스텀 이벤트 속성정보 이름은 `property1, property2`와 같이 쉼표로 구분됩니다.
- **사용 예:** {% raw %}`name = ‘{{custom_event_properties.${property names)}}}’`{% endraw %}

#### 워크스페이스

워크스페이스를 선택하기 위해서.

- **대체 값:** 워크스페이스 BSON ID
- **사용 예:** {% raw %}`workspace_id = ‘{{workspace.${app_group_id}}}’`{% endraw %}

#### 카탈로그

카탈로그 선택을 위해.

- **대체 값:** 카탈로그 BSON ID
- **사용 예:** {% raw %}`catalog_id = ‘{{catalogs.${catalog}}}’`{% endraw %}

#### 카탈로그 필드

카탈로그 필드를 선택하기 위해서. 카탈로그 변수와 함께 사용해야 합니다.

- **대체 값:** 카탈로그 필드 이름
- **사용 예:** {% raw %}`field_name = '{{catalog_fields.${some name}}}’`{% endraw %}

#### 옵션 {#options}

옵션 목록에서 선택하기 위해.

- **대체 값:** 선택한 옵션의 값
- **사용 예:**
    - 선택 드롭다운의 경우: {% raw %}`{{options.${metrics} | is_multi_select: 'true' | options: '[{"label": "test", "value": "test_value"}, {"label": "test2", "value": "test_value2"}]'}}`{% endraw %}
        - `is_multi_select`를 이용하면여러 옵션을 선택할 수 있는지 여부를 지정할 수 있습니다
    - 라디오 버튼의 경우: {% raw %}`{{options.${metrics} | is_radio_button: 'true' | options: '[{"label": "test", "value": "test_value"}, {"label": "test2", "value": "test_value2"}]'}}`{% endraw %}

#### 세그먼트

세그먼트를 선택하려면 [분석 추적]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking/)이(가) 켜져 있어야 합니다.

- **대체 값:** 세그먼트 분석 ID, 이는 이 열이 사용 가능한 테이블의 `user_segment_membership_ids` 열에 저장된 ID에 해당합니다.
- **사용 예:** {% raw %}`{{segments.${analytics_segments}}}`{% endraw %}

#### 문자열

보고서 실행 간 반복적인 문자열 값을 변경하기 위해. 이 변수를 사용하여 SQL에서 값을 여러 번 하드코딩하는 것을 피하십시오.

- **대체 값:** 문자열 그대로 따옴표 없이
- **사용 예:** {% raw %}`{{string.${some name}}}`{% endraw %}

#### 태그

캠페인 및 캔버스를 위한 태그 선택.

- **대체 값:** 선택한 태그와 연관된 단일 인용 부호로 묶인 쉼표로 구분된 BSON ID를 가진 캠페인 및 캔버스
- **사용 예:** {% raw %}`{{tags.${some tags}}}`{% endraw %}

### 변수 메타데이터

메타데이터는 변수 이름 뒤에 파이프( | ) 문자를 추가하여 변수에 메타데이터를 첨부하여 동작을 변경할 수 있습니다. 메타데이터의 순서는 중요하지 않으며 원하는 만큼 추가할 수 있습니다. 또한 모든 유형의 메타데이터는 특정 변수에만 해당하는 특수 메타데이터를 제외하고는 모든 변수에 사용할 수 있습니다(이 경우에는 해당 사항이 표시됩니다). 모든 메타데이터의 사용은 선택 사항이며 기본값의 변수 동작을 변경하는 데 사용됩니다.

**사용 예:** {% raw %}`{{string.${my var}| is_required: ‘false’ | description: ‘My optional string var’}}`{% endraw %}

#### 표시 여부

변수가 보이는지 여부에 따라. 모든 변수는 **변수** 탭에서 기본값으로 표시되며, 값을 입력할 수 있습니다.

다른 변수가 값을 가지고 있는지 여부와 같은 다른 변수에 따라 값이 달라지는 여러 특수 변수가 있습니다. 이 특수 변수는 표시되지 않도록 표시되어 **변수** 탭에 표시되지 않습니다.

**사용 예:** `visible: ‘false’`

#### 필수

변수가 기본값으로 필요한지 여부에 대해. 변수의 값이 비어 있으면 일반적으로 잘못된 쿼리가 발생합니다.

**사용 예:** `required: ‘false’`

#### 주문

**변수** 탭에서 변수의 위치를 선택합니다.

**사용 예:** `order: ‘1’`

#### 작은따옴표 포함

변수의 값을 작은따옴표로 둘러싸기 위해서입니다.

**사용 예:** `include_quotes: ‘true’`

#### Include double quotes

변수의 값을 큰따옴표로 둘러싸기 위해서입니다.

**사용 예:** `include_double_quotes: ‘true’`

#### 다중 선택

선택 드롭다운이 단일 선택 또는 다중 선택을 허용하는지 여부에 따라 다릅니다. 지금은 [옵션](#options) 변수를 사용하는 경우에만 이 메타데이터를 포함할 수 있습니다.

**사용 예:** `is_multi_select: ‘true’`

![][7]{: style="max-width:50%;"}

#### 라디오 버튼

**변수** 탭에서 드롭다운을 선택하는 대신 라디오 버튼으로 옵션을 표시합니다. 이 메타데이터는 [옵션](#options) 변수를 사용하는 경우에만 포함할 수 있습니다.

**사용 예:** `is_radio_button: ‘true’`

![][6]{: style="max-width:50%;"}

#### 옵션 

레이블과 값의 형태로 선택 가능한 옵션 목록을 제공하기 위해. 레이블은 표시되는 것이고 값은 옵션이 선택될 때 변수로 대체되는 것입니다. 이 메타데이터는 [옵션](#options) 변수를 사용하는 경우에만 포함할 수 있습니다.

**사용 예:** `options: '[{"label": "test", "value": "test_value"}, {"label": "test2", "value": "test_value2"}]'`

#### 입력 안내

변수의 입력 필드에 표시되는 입력 안내 텍스트를 지정하기 위해서입니다.

**사용 예:** `placeholder: ‘enter some value’`

#### 설명

변수의 입력 필드 아래에 표시되는 설명 텍스트를 지정하기 위해.

**사용 예:** `description: ‘some description’`

#### 기본값

변수에 값이 지정되지 않았을 때 기본값을 지정하기 위해서입니다.

**사용 예:** `default_value: ‘5’`

#### 레이블 숨기기

변수 이름 레이블을 숨기기 위해. 변수의 이름은 기본값 레이블로 사용됩니다.

**사용 예:** `hide_label: ‘true’`

### 특수 변수

다음 변수는 다른 변수와 함께 사용할 수 있습니다:

#### 다른 변수의 값의 존재 여부

변수의 값이 채워져 있는지 여부를 알기 위해서. 이것은 변수가 채워지지 않은 경우 조건을 단락하고자 할 때 선택적 변수에 유용합니다.

- **대체 값:** `true` 또는 `false` 다른 변수의 값에 따라 다릅니다
- **사용 예:** {% raw %}`{{string.${type_name_has_no_value} | visible: 'false'}} or {{string.${type_name_has_value} | visible: 'false'}}`{% endraw %}

`type` 및 `name`는 참조된 변수를 나타냅니다. 예를 들어, 다음 선택적 변수를 단축하려면 {% raw %}`{{campaigns.${messaging}}`, 다음을 사용할 수 있습니다.
`{{string.${campaigns_messaging_has_no_value}  | visible: 'false'}} OR campaign_id IN ({{campaigns.${messaging} | is_required: ‘false’}})`{% endraw %}

## 보고서 시간 초과

6분 이상 실행되는 보고서는 시간 초과됩니다. 이것이 오랜만에 실행하는 첫 번째 쿼리라면 처리하는 데 시간이 더 걸릴 수 있으며, 따라서 시간 초과될 가능성이 더 높습니다. 이런 일이 발생하면 보고서를 다시 실행해 보십시오.

보고서가 시간 초과되거나 다시 시도한 후에도 오류가 발생하면 [지원]({{site.baseurl}}/help/support#braze-support)에 문의하십시오.

## 데이터 및 결과

결과 및 결과 내보내기는 최대 1,000개의 행을 포함할 수 있는 테이블입니다. 더 많은 양의 데이터를 필요로 하는 보고서의 경우, [커런츠]({{site.baseurl}}/user_guide/data/braze_currents/) 또는 Braze의 [export APIs]({{site.baseurl}}/api/endpoints/export)와 같은 다른 도구를 사용하십시오.

## 쿼리 빌더 사용 모니터링

각 Braze 워크스페이스에는 매월 5개의 Snowflake 크레딧이 제공됩니다. 쿼리를 실행하거나 테이블을 미리 볼 때마다 Snowflake 크레딧의 작은 부분이 사용됩니다.

{% alert note %}
Snowflake 크레딧은 기능 간에 공유되지 않습니다. 예를 들어 SQL 세그먼트 확장 프로그램과 쿼리 빌더의 크레딧은 서로 독립적입니다.
{% endalert %}

크레딧 사용량은 SQL 쿼리의 실행 시간과 상관관계가 있습니다. 실행 시간이 길수록 쿼리에 소요되는 Snowflake 크레딧의 비율이 높아집니다. 실행 시간은 시간이 지남에 따라 쿼리의 복잡성과 크기에 따라 달라질 수 있습니다. 더 복잡하고 빈번한 쿼리를 실행할수록 리소스 할당이 커지고 실행 시간이 빨라집니다.

크레딧은 Braze SQL 편집기에서 보고서를 작성, 편집 또는 저장할 때 사용되지 않습니다. 크레딧은 매월 1일 한국 시간 09:00에 5로 초기화됩니다. 쿼리 빌더 페이지 상단에서 월간 크레딧 사용량을 모니터링할 수 있습니다.

![쿼리 빌더는 이번 달에 사용된 크레딧 양을 보여줍니다.][1]{: style="max-width:60%;"}

크레딧 한도에 도달하면 쿼리를 실행할 수 없지만 SQL 보고서를 생성, 편집 및 저장할 수 있습니다. 쿼리 빌더 크레딧을 더 구매하려면 계정 매니저에게 문의하세요.

[1]: {% image_buster /assets/img_archive/query_builder_credits.png %}
[2]: {% image_buster /assets/img_archive/query_builder_ai_tab.png %}
[3]: {% image_buster /assets/img_archive/sql_variables_panel.png %}
[4]: {% image_buster /assets/img_archive/query_builder_time_range.png %}
[5]: {% image_buster /assets/img_archive/sql_variables_canvases.png %}
[6]: {% image_buster /assets/img_archive/sql_variables_campaigns.png %}
[7]: {% image_buster /assets/img_archive/sql_variables_productname.png %}
