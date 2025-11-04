---
nav_title: 쿼리 빌더
article_title: 쿼리 빌더
page_order: 15
description: "이 참조 문서에서는 쿼리 빌더에서 Snowflake의 Braze 데이터를 사용하여 보고서를 구축하는 방법에 대해 설명합니다."
tool: Reports
alias: /query_builder/
---

# 쿼리 빌더

> 쿼리 빌더는 Snowflake의 Braze 데이터를 사용하여 보고서를 생성합니다. 쿼리 빌더에는 미리 구축된 SQL [쿼리 템플릿이]({{site.baseurl}}/user_guide/analytics/query_builder/query_templates/) 제공되므로 바로 시작하거나, 더 많은 인사이트를 얻을 수 있는 커스텀 SQL 쿼리를 직접 작성할 수도 있습니다.

쿼리 빌더는 일부 고객 데이터에 직접 액세스할 수 있도록 허용하므로 'PII 보기' 권한이 있는 경우에만 쿼리 빌더에 액세스할 수 있습니다.

## 쿼리 빌더에서 리포트 실행하기

쿼리 빌더 리포트를 실행하려면 다음과 같이 하세요:

1. **분석** > **쿼리 빌더로** 이동합니다.
2. **SQL 쿼리 만들기를** 선택합니다. 쿼리를 작성하는 데 영감이나 도움이 필요하다면 **쿼리 템플릿을** 선택하고 목록에서 템플릿을 선택하세요. 그렇지 않으면 **SQL 편집기를** 선택하여 편집기로 바로 이동합니다.
3. 보고서에는 현재 날짜와 시간이 포함된 이름이 자동으로 지정됩니다. 이름 위로 마우스를 가져가 <i class="fas fa-pencil" alt="Edit"></i> 을 선택하여 SQL 쿼리에 의미 있는 이름을 지정합니다.
4. 편집기에서 SQL 쿼리를 작성하거나 **AI 쿼리 빌더** 탭에서 AI의 [도움을 받으세요](#ai-query-builder). 직접 SQL을 작성하는 경우에는 요구 사항 및 리소스에 대한 [커스텀 SQL 쿼리 작성을](#custom-sql) 참조하세요.
5. **쿼리 실행을** 선택합니다.
6. 쿼리를 저장합니다.
7. 보고서의 CSV를 다운로드하려면 **내보내기를** 선택합니다.

템플릿 쿼리 "지난 30일 동안의 채널 참여도 및 매출"에 대한 결과를 보여주는 쿼리 빌더.]({% image_buster /assets/img_archive/query_builder.png %})

각 보고서의 결과는 하루에 한 번 생성할 수 있습니다. 같은 리포트를 하루에 두 번 이상 캘린더에 실행하면 두 보고서에서 동일한 결과를 볼 수 있습니다.

### 쿼리 템플릿

보고서를 처음 만들 때 **SQL 쿼리 만들기** > **쿼리 템플릿을** 선택하여 쿼리 템플릿에 액세스합니다.

사용 가능한 템플릿 목록은 [쿼리 템플릿을]({{site.baseurl}}/user_guide/analytics/query_builder/query_templates/) 참조하세요.

### 데이터 기간

모든 쿼리는 지난 60일 동안의 데이터를 표시합니다.

### 쿼리 빌더 시간대

Snowflake 데이터베이스 쿼리의 기본값은 UTC입니다. 따라서 **이메일 채널 참여** 페이지(회사 표준 시간대를 따름)와 쿼리 작성기 결과 사이에 일부 데이터 불일치가 있을 수 있습니다.

쿼리 결과에서 표준 시간대를 변환하려면 쿼리에 다음 SQL을 추가하고 회사의 표준 시간대에 맞게 커스텀하세요:

{% raw %}
```sql
SELECT
DATE_TRUNC(
'day',
CONVERT_TIMEZONE('UTC','Australia/Sydney', TO_TIMESTAMP(TIME))
) AS send_date_sydney,
COUNT(ID) AS emails_sent
USERS_MESSAGES_EMAIL_SEND_SHARED
WHERE
-- Apply the date range in Sydney time as well
CONVERT_TIMEZONE('UTC','Australia/Sydney', TO_TIMESTAMP(TIME)) >= '2025-03-25 00:00:00'
AND CONVERT_TIMEZONE('UTC','Australia/Sydney', TO_TIMESTAMP(TIME)) < '2025-03-29 00:00:00'
AND APP_GROUP_ID = 'your app group ID'
GROUP BY
send_date_sydney
ORDER BY
send_date_sydney;
```
{% endraw %}

### 쿼리 기록

쿼리 빌더의 쿼리 **기록** 섹션에는 이전에 실행한 쿼리가 표시되어 작업을 추적하고 재사용할 수 있습니다. 쿼리 기록은 7일 동안 보관되므로 7일이 지난 쿼리는 자동으로 삭제됩니다.

장기간 쿼리 사용을 감사하거나 7일 이상의 기록을 유지해야 하는 경우 중요한 쿼리 결과는 만료되기 전에 내보내거나 저장하는 것이 좋습니다.

## AI 쿼리 빌더로 SQL 생성하기

AI 쿼리 빌더는 OpenAI 기반의 [GPT를](https://openai.com/gpt-4) 활용하여 쿼리에 적합한 SQL을 추천합니다.

SQL AI 쿼리 빌더.]({% image_buster /assets/img_archive/query_builder_ai_tab.png %}){: style="max-width:60%;" }

AI 쿼리 빌더로 SQL을 생성하려면:

1. 쿼리 빌더에서 보고서를 만든 후 **AI 쿼리 빌더** 탭을 선택합니다.
2. 프롬프트를 입력하거나 샘플 프롬프트를 선택한 후 **생성을** 선택하여 프롬프트를 SQL로 번역합니다.
3. 생성된 SQL을 검토하여 올바른지 확인한 다음 **편집기에 삽입을** 선택합니다.

### 팁

- 사용 가능한 [Snowflake 데이터 테이블에]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/sql_segments_tables/) 익숙해지세요. 이러한 테이블에 존재하지 않는 데이터를 요청하면 ChatGPT가 가짜 테이블을 구성하게 될 수 있습니다.
- 이 기능에 대한 [SQL 작성 규칙을]({{site.baseurl}}/user_guide/data_and_analytics/query_builder/#custom-sql) 숙지하세요. 이러한 규칙을 따르지 않으면 오류가 발생합니다.
- AI 쿼리 빌더를 사용하면 분당 최대 20개의 프롬프트를 보낼 수 있습니다.

### 내 데이터는 어떻게 사용되어 OpenAI로 전송되나요?
<!-- Contact Legal for changes. -->

SQL을 생성하기 위해 Braze는 OpenAI의 API 플랫폼으로 프롬프트를 전송합니다. 사용자가 제공하는 콘텐츠에 고유 식별자 정보를 포함하지 않는 한, Braze에서 OpenAI로 전송되는 모든 쿼리는 익명으로 처리되므로 OpenAI는 해당 쿼리가 누구로부터 전송되었는지 식별할 수 없습니다. [OpenAI의 API 플랫폼](https://openai.com/policies/api-data-usage-policies) 약관에 자세히 설명된 대로, Braze를 통해 OpenAI의 API로 전송된 데이터는 모델 학습이나 개선에 사용되지 않으며 30일 후에 삭제됩니다. [사용 정책을](https://openai.com/policies/usage-policies) 포함하여 귀하와 관련된 OpenAI의 정책을 준수해야 합니다. Braze는 AI가 생성한 콘텐츠와 관련하여 어떠한 종류의 보증도 하지 않습니다. 

## 커스텀 SQL 쿼리 작성하기 {#custom-sql}

[Snowflake 구문을](https://docs.snowflake.com/en/sql-reference) 사용하여 SQL 쿼리를 작성합니다. 쿼리할 수 있는 테이블 및 열의 전체 목록은 [테이블 참조를]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/sql_segments_tables/) 참조하세요.

쿼리 빌더 내에서 테이블 세부 정보를 보려면 다음과 같이 하세요:

1. **쿼리 빌더** 페이지에서 **참조** 패널을 열고 **사용 가능한 데이터 테이블을** 선택하여 사용 가능한 데이터 테이블과 그 이름을 확인합니다.
3. <i class="fas fa-chevron-down" alt=""></i> **세부정보 보기를** 선택하여 테이블 설명과 데이터 유형 등 테이블 열에 대한 정보를 확인합니다.
4. SQL에 테이블 이름을 삽입하려면 다음을 선택합니다. <i class="fas fa-copy" title="SQL 편집기에 테이블 이름 복사"></i>.

Braze에서 제공하는 미리 작성된 쿼리를 사용하려면 쿼리 빌더에서 보고서를 처음 만들 때 쿼리 **템플릿을** 선택하세요.

쿼리를 특정 기간으로 제한하면 결과를 더 빨리 생성하는 데 도움이 됩니다. 다음은 지난 한 시간 동안 발생한 구매 수와 매출을 가져오는 쿼리 예제입니다.

```sql
SELECT COUNT(*) as Purchases, SUM(price) as Revenue
FROM USERS_BEHAVIORS_PURCHASE_SHARED
WHERE to_date(to_timestamp_ntz(time)) >= DATEADD('hour', -1, date_trunc('day',CURRENT_DATE()));
```

이 쿼리는 지난 달에 보낸 이메일 수를 검색합니다:

```sql
SELECT COUNT(*) as Sends
FROM USERS_MESSAGES_EMAIL_SEND_SHARED
WHERE to_date(to_timestamp_ntz(time)) >= DATEADD('month', -1, date_trunc('day',CURRENT_DATE()));
```

`CANVAS_ID`, `CANVAS_VARIATION_API_ID` 또는 `CAMPAIGN_ID` 에 대해 쿼리하면 관련 이름 열이 자동으로 결과 테이블에 포함됩니다. `SELECT` 쿼리 자체에 포함할 필요는 없습니다.

| ID 이름 | 연관된 이름 열 |
| --- | --- |
| `CANVAS_ID` | 캔버스 이름 |
| `CANVAS_VARIATION_API_ID` | 캔버스 배리언트 이름 |
| `CAMPAIGN_ID` | 캠페인 이름 |
{: .reset-td-br-1 .reset-td-br-2 }

이 쿼리는 최대 100개의 행으로 세 개의 ID와 연결된 이름 열을 모두 검색합니다:

```sql
SELECT CANVAS_ID, CANVAS_VARIATION_API_ID, CAMPAIGN_ID
FROM USERS_MESSAGES_EMAIL_SEND_SHARED 
LIMIT 100
```

### 캠페인 배리언트 이름 자동 채우기

캠페인 배리언트 이름이 자동으로 입력되도록 하려면 이 예제에서처럼 쿼리에 열 이름 `MESSAGE_VARIATION_API_ID` 을 포함하세요:

```sql
SELECT CANVAS_ID, CANVAS_VARIATION_API_ID, CAMPAIGN_ID, MESSAGE_VARIATION_API_ID
FROM USERS_MESSAGES_EMAIL_SEND_SHARED 
LIMIT 100
```

### 문제 해결

다음과 같은 이유로 쿼리가 실패할 수 있습니다:

- SQL 쿼리의 구문 오류
- 처리 시간 초과(6분 후)
    - 실행하는 데 6분 이상 걸리는 리포트는 시간이 초과됩니다.
    - 보고서가 시간 초과되는 경우 데이터를 쿼리하는 시간 범위를 제한하거나 보다 구체적인 데이터 집합을 쿼리해 보세요.

## 변수 사용

변수를 사용하면 값을 수동으로 복사할 필요 없이 SQL에서 미리 정의된 변수 유형을 사용하여 값을 참조할 수 있습니다. 예를 들어 캠페인의 ID를 SQL 편집기에 수동으로 복사하는 대신 {% raw %}`{{campaign.${My campaign}}}`{% endraw %} 을 사용하여 **변수** 탭의 드롭다운에서 캠페인을 직접 선택할 수 있습니다.

변수가 만들어지면 쿼리 빌더 보고서의 **변수** 탭에 변수가 표시됩니다. SQL 변수를 사용하면 다음과 같은 이점이 있습니다:

- 보고서를 작성할 때 캠페인 ID를 붙여넣는 대신 목록에서 선택할 수 있는 캠페인 변수를 생성하여 시간을 절약하세요.
- 나중에 약간 다른 사용 사례(예: 다른 커스텀 이벤트)에 보고서를 재사용할 수 있도록 변수를 추가하여 값을 교체할 수 있습니다.
- 각 보고서마다 필요한 편집 양을 줄여 SQL을 편집할 때 사용자 오류를 줄이세요. SQL에 더 익숙한 팀원은 기술 수준이 낮은 팀원이 사용할 수 있는 보고서를 만들 수 있습니다.

### 가이드라인

변수는 다음 Liquid 구문을 따라야 합니다: {% raw %}`{{ type.${name}}}`{% endraw %} 여기서 `type` 은 허용되는 유형 중 하나여야 하며 `name` 은 사용자가 선택한 모든 유형이 가능합니다. 이러한 변수의 레이블은 기본값이 변수 이름으로 지정됩니다.

기본적으로 값을 제공하지 않으면 기본값이 지난 30일로 설정되는 날짜 범위를 제외한 모든 변수는 필수이며, 변수 값을 선택하지 않으면 보고서가 실행되지 않습니다.

### 변수 유형

허용되는 변수 유형은 다음과 같습니다:

- [번호](#number)
- [날짜 범위](#date-range)
- [메시징](#messaging)
- [제품](#products)
- [커스텀 이벤트](#custom-events)
- [커스텀 이벤트 속성정보](#custom-event-properties)
- [작업 공간](#workspace)
- [카탈로그](#catalogs)
- [카탈로그 필드](#catalog-fields)
- [옵션](#options)
- [세그먼트](#segments)
- [문자열](#string)
- [태그](#tags)

#### 번호

- **대체 가치:** 제공된 값은 다음과 같습니다. `5.5`
- **사용 예시:** {% raw %}`some_number_column < {{number.${some name}}}`{% endraw %}

#### 날짜 범위

`start_date` 과 `end_date` 을 모두 사용하는 경우 날짜 범위로 사용할 수 있도록 이름이 같아야 합니다.

##### 예제 값

날짜 범위 유형은 상대, 시작일, 종료일 또는 날짜 범위일 수 있습니다.

`start_date` 및 `end_date` 모두 같은 이름으로 사용되는 경우 네 가지 유형이 모두 표시됩니다. 하나만 사용하는 경우 관련 유형만 표시됩니다.

| 날짜 범위 유형 | 설명 | 필수 값 |
| --- | --- | --- |
| 상대 | 지난 X일을 지정합니다. | 필요 사항 `start_date` |
| 시작 날짜 | 시작 날짜를 지정합니다. | 필요 사항 `start_date` |
| 종료 날짜 | 종료 날짜를 지정합니다. | 필요 사항 `end_date` |
| 날짜 범위 | 시작 날짜와 종료 날짜를 모두 지정합니다. | `start_date` 및 `end_date` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

- **대체 가치:** `start_date` 및 `end_date` 을 UTC로 지정된 날짜(예: `1696517353`)의 초 단위 Unix 타임스탬프로 바꿉니다.
- **사용 예시:** 모든 상대, 시작 날짜, 종료 날짜 및 날짜 범위 변수에 대해:
    - {% raw %}`time > {{start_date.${some name}}} AND time < {{end_date.${some name}}}` {% endraw %}
        - 날짜 범위를 원하지 않는 경우 `start_date` 또는 `end_date` 을 사용할 수 있습니다.

#### 메시징

모든 메시징 변수의 상태를 하나의 그룹으로 묶으려면 모든 메시징 변수가 동일한 식별자를 공유해야 합니다.

##### 캔버스

하나의 캔버스를 선택합니다. 캠페인과 동일한 이름을 공유하면 **변수** 탭에 캔버스 또는 캠페인을 선택할 수 있는 라디오 버튼이 표시됩니다.

- **대체 가치:** 캔버스 BSON ID
- **사용 예시:** {% raw %}`canvas_id = ‘{{canvas.${some name}}}’`{% endraw %}

##### 캔버스

여러 캔버스를 선택하는 경우. 캠페인과 동일한 이름을 공유하면 **변수** 탭에 캔버스 또는 캠페인을 선택할 수 있는 라디오 버튼이 표시됩니다.

- **대체 가치:** 캔버스 BSON ID
- **사용 예시:** {% raw %}`canvas_id IN ({{canvases.${some name}}})`{% endraw %}

##### 캠페인

하나의 캠페인을 선택합니다. 캔버스와 같은 이름을 공유하면 **변수** 탭에 캔버스 또는 캠페인을 선택할 수 있는 라디오 버튼이 표시됩니다.

- **대체 가치:** 캠페인 BSON ID
- **사용 예시:** {% raw %}`campaign_id = ‘{{campaign.${some name}}}’`{% endraw %}

##### 캠페인

다중 선택 캠페인의 경우. 캔버스와 같은 이름을 공유하면 **변수** 탭에 캔버스 또는 캠페인을 선택할 수 있는 라디오 버튼이 표시됩니다.

- **대체 가치:** 캠페인 BSON ID
- **사용 예시:** {% raw %}`campaign_id IN ({{campaigns.${some name}}})`{% endraw %}

##### 캠페인 배리언트

선택한 캠페인에 속한 캠페인 배리언트를 선택합니다. 캠페인 또는 캠페인 변수와 함께 사용해야 합니다.

- **대체 가치:** 캠페인 배리언트 API ID, 쉼표로 구분된 문자열(예: `api-id1, api-id2`.
- **사용 예시:** {% raw %}`message_variation_api_id IN ({{campaign_variants.${some name}}})`{% endraw %}

##### 캔버스 배리언트

선택한 캔버스에 속한 캔버스 배리언트를 선택합니다. 캔버스 또는 캔버스 변수와 함께 사용해야 합니다.

- **대체 가치:** 캔버스 배리언트 API ID, `api-id1, api-id2` 와 같이 쉼표로 구분된 문자열.
- **사용 예시:** {% raw %}`canvas_variation_api_id IN ({{canvas_variants.${some name}}})`{% endraw %}

##### 캔버스 단계

선택한 캔버스에 속하는 캔버스 단계를 선택합니다. 캔버스 변수와 함께 사용해야 합니다.

- **대체 가치:** 캔버스 단계 API ID
- **사용 예시:** {% raw %}`canvas_step_api_id = ‘{{canvas_step.${some name}}}’`{% endraw %}

##### 캔버스 단계

선택한 캔버스에 속하는 캔버스 단계를 선택합니다. 캔버스 또는 캔버스 변수와 함께 사용해야 합니다.

- **대체 가치:** 캔버스 단계 API ID
- **사용 예시:** {% raw %}`canvas_step_api_id IN ({{canvas_steps.${some name}}})`{% endraw %}
