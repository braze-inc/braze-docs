> 쿼리 빌더를 사용하는 방법을 알아보고 Snowflake에서 Braze 데이터를 사용하여 보고서를 생성할 수 있습니다. 쿼리 빌더는 시작할 수 있도록 미리 작성된 SQL [쿼리 템플릿]({{site.baseurl}}/user_guide/analytics/query_builder/query_templates/)과 함께 제공되며, 직접 커스텀 SQL 쿼리를 작성하여 더 많은 인사이트를 얻을 수 있습니다.

## 필수 조건

쿼리 빌더를 사용하려면 일부 고객 데이터에 직접 액세스할 수 있는 ['PII 보기' 권한이]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/) 필요합니다.

## 쿼리 작성기 사용

### 1단계: SQL 쿼리 만들기

새 쿼리를 만들려면 **분석** > **쿼리 빌더로** 이동한 다음 **SQL 쿼리 만들기를** 선택합니다.

!["SQL 쿼리 만들기" 드롭다운에 있는 "쿼리 템플릿" 및 "SQL 편집기" 옵션]({% image_buster /assets/img_archive/create_sql_query_button.png %}){: style="max-width:60%;"}

쿼리를 작성하는 데 영감이나 도움이 필요하다면 **쿼리 템플릿을** 선택하고 [미리 만들어진 템플릿을]({{site.baseurl}}/user_guide/analytics/query_builder/query_templates/) 선택하세요. 빈 쿼리로 시작하려면 **SQL 편집기를** 선택합니다.

보고서는 현재 날짜와 시간으로 자동으로 이름이 지정됩니다. 이름 위에 마우스를 올리고 <i class="fas fa-pencil" alt="Edit"></i>을 선택하여 SQL 쿼리에 의미 있는 이름을 지정하세요.

![보고서 이름 예시: "2025년 5월 채널 참여도"]({% image_buster /assets/img_archive/report_name_example.png %}){: style="max-width:80%;"}

### 2단계: 쿼리 구축

쿼리를 구축할 때 AI의 도움을 받거나 직접 구축할 수 있습니다.

{% tabs local %}
{% tab BrazeAI 사용하기 %}
AI 쿼리 빌더는 [GPT](https://openai.com/gpt-4)를 활용하여 OpenAI에서 제공하는 SQL을 추천합니다. AI 쿼리 빌더를 사용하여 SQL을 생성하는 방법:

1. 쿼리 빌더에서 보고서를 만든 후 **AI 쿼리 빌더** 탭을 선택합니다.
2. 프롬프트를 입력하거나 샘플 프롬프트를 선택하고 **생성**을 선택하여 프롬프트를 SQL로 번역하십시오.
3. 생성된 SQL을 검토하여 올바른지 확인한 다음 **편집기에 삽입**을 선택합니다.

![The SQL AI query builder.]({% image_buster /assets/img_archive/query_builder_ai_tab.png %}){: style="max-width:60%;" }

#### Tips

- Familiarize yourself with the available [Snowflake data tables]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/sql_segments_tables/). 이러한 테이블에 존재하지 않는 데이터를 요청하면 ChatGPT가 가짜 테이블을 구성하게 될 수 있습니다.
- 이 기능에 대한 [SQL 작성 규칙을]({{site.baseurl}}/user_guide/data_and_analytics/query_builder/#custom-sql) 숙지하세요. 이 규칙을 따르지 않으면 오류가 발생합니다.
- AI 쿼리 빌더를 사용하여 분당 최대 20개의 프롬프트를 보낼 수 있습니다.

\##{% multi_lang_include brazeai/generative_ai/policy.md %}
{% endtab %}

{% tab 혼자서 %}
[Snowflake syntax](https://docs.snowflake.com/en/sql-reference)를 사용하여 SQL 쿼리를 작성하십시오. 전체 테이블 및 쿼리할 수 있는 열 목록은 [테이블 참조]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/sql_segments_tables/)를 참조하십시오.

쿼리 빌더 내에서 테이블 세부 정보를 보려면:

1. **쿼리 빌더** 페이지에서 **참조** 패널을 열고 **사용 가능한 데이터 테이블**을 선택하여 사용 가능한 데이터 테이블과 그 이름을 확인합니다.
3. <i class="fas fa-chevron-down" alt=""></i> **자세히 보기**를 선택하여 테이블 설명 및 데이터 유형과 같은 테이블 열에 대한 정보를 확인하십시오.
4. SQL에 테이블 이름을 삽입하려면 <i class="fas fa-copy" title="SQL 편집기에 테이블 이름 복사"></i>을 선택하십시오.

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

#### 문제 해결

다음과 같은 이유로 쿼리가 실패할 수 있습니다:

- SQL 쿼리의 구문 오류
- 처리 시간 초과 (6분 후)
    - 6분 이상 실행되는 보고서는 시간 초과됩니다.
    - 보고서가 시간 초과되면 쿼리하는 데이터의 시간 범위를 제한하거나 더 구체적인 데이터 세트를 쿼리해 봅니다.
{% endtab %}
{% endtabs %}

### 3단계: 보고서 생성

쿼리 구축을 마쳤으면 **쿼리 실행을** 선택합니다. 오류나 [보고 시간 초과가](#report-timeouts) 없는 경우 쿼리에서 CSV 파일이 생성됩니다.

CSV 보고서를 다운로드하려면 **내보내기를** 선택합니다.

![쿼리 빌더가 템플릿 쿼리 "채널 인게이지먼트 및 매출 지난 30일 동안"에 대한 결과를 보여줍니다.]({% image_buster /assets/img_archive/query_builder.png %})

{% alert important %}
각 보고서는 하루에 한 번만 결과를 생성할 수 있습니다. 같은 리포트를 하루에 여러 번 실행하면 각 보고서에서 동일한 결과를 볼 수 있습니다.
{% endalert %}

## 시간 초과 보고

6분 이상 실행되는 보고서는 시간 초과됩니다. 이것이 오랜만에 실행하는 첫 번째 쿼리라면 처리하는 데 시간이 더 걸릴 수 있으며, 따라서 시간 초과될 가능성이 더 높습니다. 이런 일이 발생하면 보고서를 다시 실행해 보십시오.

여러 번 시도한 후에도 보고서가 계속 시간 초과되는 경우 [지원팀에 문의하세요]({{site.baseurl}}/help/support#braze-support).

## 데이터 및 결과

모든 쿼리는 지난 60일 동안의 데이터를 표시합니다. 결과를 내보낼 때는 최대 1,000개 행까지만 포함됩니다. 더 많은 양의 데이터가 필요한 보고서의 경우 [커런츠]({{site.baseurl}}/user_guide/data/braze_currents/) 또는 [내보내기 API 엔드포인트와]({{site.baseurl}}/api/endpoints/export) 같은 도구를 사용할 수 있습니다.

## Snowflake 크레딧

각 회사는 한 달에 5개의 Snowflake 크레딧을 사용할 수 있으며, 모든 워크스페이스에서 공유할 수 있습니다. 쿼리를 실행하거나 테이블을 미리 볼 때마다 Snowflake 크레딧의 작은 부분이 사용됩니다.

{% alert note %}
Snowflake 크레딧은 기능 간에 공유되지 않습니다. 예를 들어 SQL 세그먼트 확장 프로그램과 쿼리 빌더의 크레딧은 서로 독립적입니다.
{% endalert %}

크레딧 사용량은 SQL 쿼리의 실행 시간과 상관관계가 있습니다. 실행 시간이 길수록 쿼리에 소요되는 Snowflake 크레딧의 비율이 높아집니다. 실행 시간은 시간이 지남에 따라 쿼리의 복잡성과 크기에 따라 달라질 수 있습니다. 더 복잡하고 빈번한 쿼리를 실행할수록 리소스 할당이 커지고 실행 시간이 빨라집니다.

크레딧은 Braze SQL 편집기에서 보고서를 작성, 편집 또는 저장할 때 사용되지 않습니다. 크레딧은 매월 1일 한국 시간 09:00에 5로 초기화됩니다. 쿼리 빌더 페이지 상단에서 월간 크레딧 사용량을 모니터링할 수 있습니다.

![이번 달에 사용한 크레딧 금액을 보여주는 쿼리 빌더]({% image_buster /assets/img_archive/query_builder_credits.png %}){: style="max-width:60%;"}

크레딧 한도에 도달하면 쿼리를 실행할 수 없지만 SQL 보고서를 생성, 편집 및 저장할 수 있습니다. 쿼리 빌더 크레딧을 더 구매하려면 계정 매니저에게 문의하세요.
