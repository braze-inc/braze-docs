---
nav_title: "SQL 세그먼트 확장"
article_title: SQL 세그먼트 확장
alias: "/sql_segments/"
page_order: 3.2

page_type: reference
description: "이 문서에서는 Snowflake 쿼리를 사용하여 SQL 세그먼트 확장을 만드는 방법에 대해 설명합니다."
tool: Segments
---

# SQL 세그먼트 확장

> [Snowflake]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/) 데이터의 Snowflake SQL 쿼리를 사용하여 세그먼트 확장을 생성할 수 있습니다. SQL은 다른 세그먼트 기능으로는 달성할 수 없는 방식으로 데이터 간의 관계를 설명할 수 있는 유연성을 제공하기 때문에 새로운 세그먼트 사용 사례를 발굴하는 데 도움이 될 수 있습니다.

표준 세그먼트 확장과 마찬가지로 SQL 세그먼트 확장 프로그램에서 최대 2년(730일)까지의 이벤트를 쿼리할 수 있습니다.

## SQL 세그먼트 확장 유형

SQL 세그먼트 확장을 만들 때 선택할 수 있는 SQL 편집기에는 SQL 편집기와 증분 SQL 편집기의 두 가지 유형이 있습니다.

- **SQL 편집기로 확장 프로그램 만들기(전체 새로 고침):** 세그먼트가 새로고침될 때마다 Braze는 사용 가능한 모든 데이터를 쿼리하여 세그먼트를 업데이트하며, 이때 점진적 새로고침보다 더 많은 크레딧이 사용됩니다. 전체 새로 고침 연장은 멤버십을 매일 자동으로 갱신할 수 있지만 증분 새로고침으로는 갱신할 수 없습니다.
- **증분 SQL 편집기(증분 새로 고침)로 확장 만들기:** 증분 새로고침은 지난 이틀간의 데이터만 계산하므로 비용 효율성이 높고 매번 크레딧을 덜 소모합니다. 증분 새로고침 SQL 세그먼트를 생성할 때 멤버십을 매일 자동으로 재생성하도록 설정할 수 있습니다. <br><br>증분 새로고침 기능이 있는 확장 기능의 주요 이점은 세그먼트가 매일 멤버십을 자동으로 새로 고치도록 설정할 수 있다는 것입니다. 일반 SQL 편집기로 생성한 세그먼트는 멤버십을 수동으로만 새로 고칠 수 있습니다. 이렇게 하면 SQL 세그먼트 확장을 위한 일일 데이터 새로고침 비용을 줄일 수 있습니다.

{% alert tip %}
두 SQL 편집기에서 생성된 모든 SQL 세그먼트에 대해 수동으로 전체 새로고침을 수행할 수 있습니다.
{% endalert %}

## SQL 세그먼트 확장 만들기

{% tabs 로컬 %}
{% tab 전체 새로 고침 %}

전체 새로 고침 SQL 세그먼트 확장을 만들려면 다음과 같이 하세요:

1. **대상** > **세그먼트 확장으로** 이동합니다.
2. **새 확장 프로그램 만들기**를 클릭하고 **전체 새로고침**을 선택합니다.<br><br>
   ![]({% image_buster /assets/img/segment/segment_extension_modal.png %}){: style="max-width:50%" }<br><br>
3. 세그먼트 확장의 이름을 추가하고 SQL을 입력합니다. 요구 사항 및 리소스는 [SQL 작성하기](#writing-sql) 섹션을 참조하세요.<br><br>
   ![SQL 세그먼트 확장 예제를 보여주는 SQL 편집기]({% image_buster /assets/img_archive/sql_segments_editor.png %}){: style="max-width:60%" }<br><br>
4. 세그먼트 확장자를 저장합니다.

{% endtab %}
{% tab 증분 새로 고침 %}

증분 새로고침 SQL 편집기를 사용하면 지정된 시간 프레임 내의 이벤트에 대해 날짜별로 사용자 쿼리 집계를 수행할 수 있습니다. 증분 새로고침 SQL 세그먼트 확장을 만들려면 다음과 같이 하세요:

1. **대상** > **세그먼트 확장으로** 이동합니다.
{% alert note %}

[이전 탐색]({{site.baseurl}}/user_guide/administrative/access_braze/navigation/)을 사용하는 경우 **인게이지먼트** > **세그먼트** > **세그먼트 확장**에서 이 페이지를 찾을 수 있습니다.
{% endalert %}

{:start="2"}
2\. **새 확장 프로그램 만들기**를 클릭하고 **증분 새로고침**을 선택합니다.<br><br>
   ![]({% image_buster /assets/img/segment/segment_extension_modal.png %}){: style="max-width:50%" }<br><br>
3\. 세그먼트 확장의 이름을 추가하고 SQL을 입력합니다. 요구 사항 및 리소스는 [SQL 작성하기](#writing-sql) 섹션을 참조하세요.<br><br>
   ![증분 SQL 세그먼트 확장 예제를 보여주는 SQL 편집기.]({% image_buster /assets/img_archive/sql_segments_editor_incremental.png %}){: style="max-width:60%" }<br><br>
4\. 원하는 경우 **매일 확장 프로그램 재생성**을 선택합니다.<br><br>
   ![확인란을 선택하여 매일 확장 프로그램을 재생성합니다.]({% image_buster /assets/img_archive/sql_segments_regenerate.png %}){: style="max-width:60%" }<br><br>
   이 옵션을 선택하면 Braze가 매일 자동으로 세그먼트 멤버십을 업데이트합니다. 즉, 매일 자정(1시간 정도 지연될 수 있음)에 회사 표준 시간대에 맞춰 Braze가 세그먼트에 새로운 사용자가 있는지 확인하고 세그먼트에 자동으로 추가합니다. 7일 동안 세그먼트 확장을 사용하지 않은 경우, Braze는 자동으로 일일 재생을 일시 중지합니다. 사용하지 않은 세그먼트 확장은 캠페인 또는 캔버스에 포함되지 않은 확장을 말합니다(캠페인 또는 캔버스가 활성화되어 있지 않아도 확장을 "사용 중"으로 간주할 수 있습니다).<br><br>
5\. 세그먼트 확장자를 저장합니다.

{% endtab %}

{% tab AI SQL 생성기 %}

{% alert note %}
AI SQL 생성기는 현재 베타 기능으로 제공되고 있습니다. 이 베타 평가판에 참여하려면 고객 성공 매니저에게 문의하세요.
{% endalert %}

AI SQL 생성기는 OpenAI가 제공하는 [GPT](https://openai.com/gpt-4)를 활용하여 SQL 세그먼트에 맞는 SQL을 추천합니다.

!["지난달에 알림을 받은 사용자" 메시지가 표시되는 AI SQL 생성기]({% image_buster /assets/img/ai_sql_generator.png %}){: style="max-width:70%;"}

AI SQL 생성기를 사용하려면 다음과 같이 하세요:

1. 전체 또는 증분 새로고침을 사용하여 [SQL 세그먼트]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments)를 생성한 후 **AI SQL 생성기 시작**을 클릭합니다.
2. 프롬프트를 입력하고 **생성**을 클릭하여 프롬프트를 SQL로 번역합니다.
3. 생성된 SQL을 검토하여 올바른지 확인한 다음 세그먼트를 저장합니다.

### 프롬프트 예시
- 지난 달에 이메일을 받은 사용자
- 지난 1년간 구매 횟수가 5회 미만인 사용자

### 팁
- Familiarize yourself with the available [Snowflake data tables]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/sql_segments_tables/). 이러한 테이블에 존재하지 않는 데이터를 요청하면 ChatGPT가 가짜 테이블을 구성하게 될 수 있습니다.
- 이 기능에 대한 [SQL 작성 규칙을]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments?tab=sql%20editor#writing-sql) 숙지하세요. 이러한 규칙을 따르지 않으면 오류가 발생합니다. 예를 들어 SQL 코드에서 `user_id` 열을 선택해야 합니다. "사용자 누구"로 프롬프트를 시작하면 도움이 될 수 있습니다.
- AI SQL 생성기를 사용하면 분당 최대 20개의 프롬프트를 보낼 수 있습니다.

### 내 데이터는 어떻게 사용되어 OpenAI로 전송되나요?

SQL을 생성하기 위해 Braze는 사용자의 프롬프트를 OpenAI의 API 플랫폼으로 전송합니다. Braze에서 OpenAI로 전송되는 모든 쿼리는 익명으로 처리되므로, 사용자가 제공하는 콘텐츠에 고유 식별 정보를 포함하지 않는 한 OpenAI는 해당 쿼리가 누구로부터 전송되었는지 확인할 수 없습니다. [OpenAI의 API 플랫폼](https://openai.com/policies/api-data-usage-policies) 약관에 명시된 바와 같이, Braze를 통해 OpenAI의 API로 전송된 데이터는 모델을 학습하거나 개선하는 데 사용되지 않으며 30일 후에 삭제됩니다. [사용 정책](https://openai.com/policies/usage-policies)을 포함하여 사용자와 관련된 OpenAI의 정책을 준수해야 합니다. Braze는 AI가 생성한 콘텐츠와 관련하여 어떠한 종류의 보증도 하지 않습니다.
{% endtab %}
{% endtabs %}

{% alert note %}
실행하는 데 20분 이상 걸리는 SQL 쿼리는 시간 초과됩니다.
{% endalert %}

확장 처리가 완료되면 [세그먼트 확장을 사용하여 세그먼트][4]를 생성하고 캠페인 및 캔버스로 이 새 세그먼트를 타겟팅할 수 있습니다.

## SQL 작성

SQL 쿼리는 [Snowflake 구문](https://docs.snowflake.com/en/sql-reference.html)을 사용하여 작성해야 합니다. Consult the [table reference]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/sql_segments_tables/) for a full list of tables and columns available to be queried.

{% alert important %}
쿼리할 수 있는 테이블에는 이벤트 데이터만 포함되어 있다는 점에 유의하세요. 사용자 속성을 쿼리하려면 SQL 세그먼트와 [기존 세그멘터]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/)의 커스텀 속성 필터를 결합해야 합니다.
{% endalert %} 

{% tabs %}
{% tab SQL 편집기 %}

SQL은 다음 규칙을 추가로 준수해야 합니다:

- 하나의 SQL 문을 작성합니다. 세미콜론을 포함하지 마십시오.
- SQL은 하나의 열, 즉 `user_id` 열만 선택해야 합니다. 즉, SQL에 다음이 포함되어야 합니다:

```sql
SELECT DISTINCT user_id FROM "INSERT TABLE NAME"
```

- 이벤트가 0건인 사용자에 대해서는 쿼리할 수 없으므로 이벤트를 X회 미만 수행한 사용자에 대한 쿼리는 이 해결 방법을 따라야 합니다:
   1. 쿼리를 작성하여 이벤트가 X회 이상 있는 사용자를 선택합니다.
   2. 세그먼트에서 세그먼트 확장을 참조할 때 `doesn't include`를 선택하면 결과가 반전됩니다.

{% endtab %}
{% tab 증분 SQL 편집기 %}

모든 증분 새로고침 쿼리는 쿼리와 스키마 세부 정보의 두 부분으로 구성됩니다.

1. 편집기에서 원하는 테이블에서 `user_id`s를 선택하는 쿼리를 작성합니다.
2. 편집기 위의 필드에서 **연산자**, **횟수**, **기간을** 선택하여 스키마 세부 정보를 추가합니다. 쿼리는 집계 열의 합계가 {% raw %}`{{operator}}` 및 `{{number of times}}`{% endraw %} 입력 안내로 지정된 특정 조건을 충족하는지 확인합니다. 이는 기존 세그먼트 확장을 만드는 워크플로와 유사하게 작동합니다.<br><br>
   - **연산자:** 이벤트가 발생 횟수보다 많거나, 적거나, 같은 횟수로 발생했는지 표시합니다.<br>
   !["초과"가 선택된 연산자 필드]({% image_buster /assets/img_archive/sql_segments_operator.png %})<br><br>
   - **횟수:** 운영자와 관련하여 이벤트를 몇 번 평가하고 싶은지 입력합니다.<br>
   !["5"를 입력한 횟수:]({% image_buster /assets/img_archive/sql_segments_times.png %})<br><br>
   - **기간:** 이벤트의 인스턴스를 확인하려는 1~730일 사이의 일 수입니다. 이 기간은 현재 날짜를 기준으로 지난 날을 나타냅니다. 다음 예는 지난 365일 동안 이벤트를 5회 이상 수행한 사용자에 대한 쿼리를 보여줍니다.<br>
   ![기간 필드에 "365"가 입력되어 있습니다.]({% image_buster /assets/img_archive/sql_segments_period.png %})

다음 예제에서 결과 세그먼트에는 지정된 날짜 이후 지난 30일 동안 `favorited` 이벤트를 3회 이상 수행한 사용자가 포함됩니다.

![증분 SQL 세그먼트 확장 예제를 보여주는 SQL 편집기.]({% image_buster /assets/img_archive/sql_segments_editor_incremental.png %}){: style="max-width:65%" }

![증분 SQL 세그먼트 확장의 SQL 미리 보기]({% image_buster /assets/img_archive/sql_segments_incremental_preview.png %}){: style="max-width:85%" }

### 추가 규칙

증분 새로 고침 쿼리는 다음 규칙을 추가로 준수해야 합니다:

- 하나의 SQL 문을 작성합니다. 세미콜론을 포함하지 마십시오.
- 증분 SQL 세그먼트는 하나의 단일 이벤트만 참조할 수 있습니다. 날짜 및 개수에 대한 드롭다운은 선택한 이벤트를 기준으로 합니다.
- SQL에는 `user_id`, `$start_date` 열과 집계 함수(예: `COUNT`)가 있어야 합니다. 이 세 필드 없이 저장된 SQL은 오류가 발생합니다.

{% alert tip %}
증분 새로고침 세그먼트는 2일 이상 전에 발생한 이벤트인 늦은 이벤트(예: 캡처 시점에 전송되지 않은 SDK 이벤트)를 고려합니다.
{% endalert %}

{% endtab %}
{% endtabs %}

## 결과 미리보기

저장하기 전에 쿼리 미리 보기를 실행할 수 있습니다. 쿼리 미리 보기는 자동으로 100개 행으로 제한되며 60초 후에 시간 초과됩니다. 미리 보기를 실행할 때는 `user_id` 열 요구 사항이 적용되지 않습니다.

증분 SQL 세그먼트 확장의 경우 미리 보기에는 연산자, 횟수 및 기간 필드의 추가 기준이 포함되지 않습니다.

## SQL 세그먼트 확장 관리

**세그먼트 확장** 페이지에서 SQL을 사용하여 생성된 세그먼트는 이름 옆에 <i class="fas fa-code" alt="SQL Segment Extension"></i> 로 표시됩니다.

SQL 세그먼트 확장을 선택하여 확장이 사용 중인 위치를 확인하거나, 확장을 보관하거나, [세그먼트 멤버십](#refreshing-segment-membership)을 수동으로 새로고침할 수 있습니다.

![SQL 편집기의 메시징 사용 섹션에서 SQL 세그먼트가 사용 중인 위치를 표시합니다.][3]

### 세그먼트 멤버십 새로 고침

SQL을 사용하여 생성한 세그먼트 확장의 세그먼트 멤버십을 새로 고치려면 세그먼트 확장을 열고 **새로고침**을 선택합니다. 증분 새로고침 SQL 세그먼트 확장만 자동으로 다시 생성할 수 있습니다(선택한 경우).

{% alert tip %}
사용자가 정기적으로 들어오고 나갈 것으로 예상되는 세그먼트를 만든 경우, 캠페인이나 캔버스에서 해당 세그먼트를 타겟팅하기 전에 사용하는 세그먼트 확장을 수동으로 새로고침하세요.
{% endalert %}

## SQL 세그먼트 사용량 모니터링

각 Braze 작업 공간에는 한 달에 5개의 Snowflake 크레딧이 제공됩니다. 크레딧이 더 필요한 경우 계정 관리자에게 문의하세요. 크레딧은 SQL 세그먼트의 멤버십을 새로 고치거나 저장하고 새로 고칠 때마다 사용됩니다. SQL 세그먼트 내에서 미리 보기를 실행하거나 기존 세그먼트 확장을 저장하거나 새로 고칠 때는 크레딧이 사용되지 않습니다.

{% alert note %}
Snowflake 크레딧은 기능 간에 공유되지 않습니다. 예를 들어 SQL 세그먼트 확장 프로그램과 쿼리 빌더의 크레딧은 서로 독립적입니다.
{% endalert %}

크레딧 사용량은 SQL 쿼리의 실행 시간과 상관관계가 있습니다. 실행 시간이 길수록 쿼리 비용이 더 많이 듭니다. 실행 시간은 시간이 지남에 따라 쿼리의 복잡성과 크기에 따라 달라질 수 있습니다. 쿼리를 더 복잡하고 자주 실행할수록 리소스 할당이 커지고 실행 시간이 빨라집니다.

크레딧을 절약하려면 SQL 세그먼트 확장을 저장하기 전에 쿼리를 미리 보고 올바른지 확인하세요.

크레딧은 매월 1일 오전 12시(UTC)에 5로 초기화됩니다. 크레딧 사용량 패널에서 한 달 동안의 크레딧 사용량을 모니터링할 수 있습니다. **세그먼트 확장** 페이지에서 <i class="fa-solid fa-chart-column"></i> **SQL 크레딧 사용량 보기를** 클릭합니다.

![SQL 세그먼트 확장 페이지의 SQL 크레딧 사용량 패널][5]{: style="max-width:60%"}

크레딧이 0이 되면 다음과 같은 일이 발생합니다.

- 자동으로 새로고침되도록 설정된 모든 SQL 세그먼트 확장은 새로고침을 중지하여 이러한 세그먼트의 멤버십과 이러한 세그먼트를 타겟팅하는 모든 캠페인 또는 캔버스에 영향을 미칩니다.
- 새 SQL 세그먼트 확장은 남은 한 달 동안만 초안으로 저장할 수 있습니다.

SQL 세그먼트를 생성한 모든 회사 사용자와 회사 관리자는 크레딧의 50%, 80%, 100%를 모두 사용하면 알림 이메일을 받게 됩니다. 다음 달 초에 크레딧이 초기화되면 더 많은 SQL 세그먼트를 만들 수 있으며 자동 새로고침이 다시 시작됩니다.

SQL 세그먼트 크레딧을 더 구매하거나 세그먼트 확장을 추가로 구매하려면 계정 매니저에게 문의하세요.

## 문제 해결

다음과 같은 이유로 쿼리가 실패할 수 있습니다:

- SQL 쿼리의 구문 오류
- SQL이 [SQL 규칙을](#writing-sql) 준수하지 않음
- 처리 시간 초과(20분 후)

[1]: {% image_buster /assets/img_archive/sql_segments_create.png %}
[2]: {% image_buster /assets/img_archive/sql_segments_editor.png %}
[3]: {% image_buster /assets/img_archive/sql_segments_usage.png %}
[4]: {{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension#step-5-use-your-extension-in-a-segment
[5]: {% image_buster /assets/img_archive/sql_segments_credits.png %}
[6]: {% image_buster /assets/img/ai_sql_generator.png %}
