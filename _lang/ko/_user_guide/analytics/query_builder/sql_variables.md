---
nav_title: SQL 변수
article_title: 쿼리 빌더 SQL 변수
page_order: 2
page_type: reference
description: "쿼리 빌더에서 변수를 사용하는 방법을 알아두면 쿼리를 재사용하고 코드에 데이터를 하드코딩하지 않아도 됩니다."
tool: Reports
---

# 쿼리 빌더 SQL 변수

> 쿼리 빌더에서 SQL 변수를 사용하는 방법을 알아두면 쿼리를 재사용하고 코드에 데이터를 하드코딩하는 일을 피할 수 있습니다.

## SQL 변수를 사용하는 이유는 무엇인가요?

SQL 변수를 사용하면 다음과 같은 이점이 있습니다:

- 보고서를 작성할 때 캠페인 ID를 붙여넣는 대신 목록에서 선택할 수 있는 캠페인 변수를 생성하여 시간을 절약하세요.
- 나중에 약간 다른 사용 사례(예: 다른 커스텀 이벤트)에 보고서를 재사용할 수 있도록 변수를 추가하여 값을 교체할 수 있습니다.
- 각 보고서마다 필요한 편집 양을 줄여 SQL을 편집할 때 사용자 오류를 줄이세요. SQL에 더 익숙한 팀원은 기술 수준이 낮은 팀원이 사용할 수 있는 보고서를 만들 수 있습니다.

## 변수 사용

### 1단계: 변수 추가

쿼리에 변수를 추가하려면 다음 구문을 사용합니다:

{% raw %}
```sql
{{variable_type.${custom_label}}}
```
{% endraw %}

다음을 교체합니다:

| 입력 안내      | 설명                                                                                                                              |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| `variable_type`   | 사용하려는 미리 정의된 변수 유형(예: `campaign` 또는 `catalog_fields`). 전체 목록은 [지원되는 변수 유형을](#variable-types) 참조하세요. |
| `custom_label` | 쿼리 빌더의 **변수** 탭에서 변수를 식별하는 데 사용되는 레이블입니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

다음 예에서는 한 달의 첫날과 마지막 날 사이의 총 사용자 수를 캠페인에 대해 쿼리합니다. 각 변수에는 다음 단계에서 값이 할당됩니다.

{% raw %}
```sql
SELECT COUNT(*) AS total_users
FROM USERS_CAMPAIGNS_REVENUE_SHARED
WHERE campaign_id = '{{campaign.${Campaign}}}'
  AND TIME > '{{start_date.${Month First Day}}}'
  AND TIME < '{{end_date.${Month Last Day}}}';
```
{% endraw %}

### 2단계: 값 지정

기본적으로 **변수** 탭은 쿼리 빌더에 표시되지 않습니다. 쿼리에 첫 번째 변수를 추가한 후에만 표시됩니다. 여기에서 값을 할당할 수 있습니다. 선택할 수 있는 특정 값은 특정 변수의 [유형에](#variable-types) 따라 달라집니다.

다음 예에서는 2025년 6월의 첫날과 마지막 날과 함께 '여름 기능 출시' 캠페인이 값으로 할당되어 있습니다.

쿼리 빌더의 '변수' 탭에 주어진 예제가 표시됩니다.]({% image_buster /assets/img/query_builder_example.png %})

## 일반 변수 유형 {#variable-types}

### 번호

`number` 는 문자열이 아닌 다른 변수와 함께 사용할 수 있습니다. `5.5` 과 같은 10진수를 포함한 모든 양수 또는 음수를 허용합니다.

{% tabs %}
{% tab usage %}
{% raw %}
```sql
some_number_column < {{number.${custom_label}}}
```
{% endraw %}
{% endtab %}
{% endtabs %}

### 문자열

리포트 실행 간에 반복적인 문자열 값을 변경하는 경우. 이 변수를 사용하면 SQL에서 값을 여러 번 하드코딩하는 것을 방지할 수 있습니다.

{% tabs %}
{% tab usage %}
{% raw %}
```sql
'{{string.${add a string here.}}}'
```
{% endraw %}
{% endtab %}
{% endtabs %}

### 목록 {#list}

옵션 목록에서 선택합니다.

{% tabs local %}
{% tab choose one %}
{% subtabs %}
{% subtab usage %}
{% raw %}
```sql
{{options.${metrics} | is_radio_button: 'true' | options: '[{"label": "test", "value": "test_value"}, {"label": "test2", "value": "test_value2"}]'}}
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab choose multiple %}
{% subtabs %}
{% subtab usage %}
{% raw %}
```sql
{{options.${metrics} | is_multi_select: 'true' | options: '[{"label": "test", "value": "test_value"}, {"label": "test2", "value": "test_value2"}]'}}
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

#### 라디오 버튼

**변수** 탭에서 옵션을 선택 드롭다운 대신 라디오 버튼으로 표시하는 경우. 이 기능은 단독으로 사용할 수 없으며 [목록과](#list) 함께 사용해야 합니다.

{% tabs %}
{% tab usage %}
```sql
is_radio_button: 'true'
```
{% endtab %}
{% endtabs %}

Braze에서 렌더링된 라디오 버튼 예시.]({% image_buster /assets/img_archive/sql_variables_campaigns.png %}){: style="max-width:50%;"}

#### 다중 선택

선택 드롭다운에서 단일 또는 다중 선택을 허용할지 여부에 대해 설명합니다. 이 기능은 단독으로 사용할 수 없으며 [목록과](#list) 함께 사용해야 합니다.

{% tabs %}
{% tab usage %}
```sql
is_multi_select: 'true'
```
{% endtab %}
{% endtabs %}

Braze에서 렌더링된 다중 선택 목록 예시.]({% image_buster /assets/img_archive/sql_variables_productname.png %}){: style="max-width:50%;"}

#### 옵션 

선택 가능한 옵션 목록을 레이블 및 값 형태로 제공합니다. 레이블은 표시되는 내용이고 값은 옵션을 선택할 때 변수가 대체되는 내용입니다. 이 기능은 단독으로 사용할 수 없으며 [목록과](#list) 함께 사용해야 합니다.

{% tabs %}
{% tab usage %}
```sql
options: '[{"label": "test", "value": "test_value"}, {"label": "test2", "value": "test_value2"}]'
```
{% endtab %}
{% endtabs %}

## Braze 관련 변수 유형

### 날짜 범위

날짜를 선택할 수 있는 캘린더를 표시합니다. `start_date` 및 `end_date` 을 UTC로 지정된 날짜에 대한 초 단위의 Unix 타임스탬프(예: `1696517353`)로 바꿉니다. 선택적으로 `start_date` 또는 `end_date` 만 설정하여 캘린더에 단일 날짜만 표시할 수 있습니다. `start_date` 과 `end_date` 의 레이블이 일치하지 않으면 날짜 범위가 아닌 두 개의 개별 날짜로 취급됩니다.

{% tabs %}
{% tab usage %}
{% raw %}
```
time > {{start_date.${custom_label}}} AND time < {{end_date.${custom_label}}}
```
{% endraw %}
{% endtab %}
{% endtabs %}

날짜 범위를 다음 옵션 중 하나로 설정할 수 있습니다. `start_date` 및 `end_date` 을 모두 사용하고 동일한 레이블을 공유하는 경우 모든 옵션이 표시됩니다. 그렇지 않고 하나만 사용하면 지정된 옵션만 표시됩니다.

| 옵션 | 설명 | 필수 값 |
| --- | --- | --- |
| 상대 | 지난 X일을 지정합니다. | 필요 사항 `start_date` |
| 시작 날짜 | 시작 날짜를 지정합니다. | 필요 사항 `start_date` |
| 종료 날짜 | 종료 날짜를 지정합니다. | 필요 사항 `end_date` |
| 날짜 범위 | 시작 날짜와 종료 날짜를 모두 지정합니다. | `start_date` 및 `end_date` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Liquid는 지정된 날짜 범위 내에서 캘린더를 표시하는 데 사용됩니다:

Braze로 렌더링된 캘린더 예시.]({% image_buster /assets/img_archive/query_builder_time_range.png %}){: style="max-width:50%;"}

### 캠페인

{% tabs local %}
{% tab one campaign %}
하나의 캠페인을 선택합니다. 캔버스와 동일한 레이블을 공유하면 **변수** 탭에 캔버스 또는 캠페인을 선택할 수 있는 라디오 버튼이 표시됩니다.

{% subtabs %}
{% subtab usage %}
{% raw %}
```sql
campaign_id = '{{campaign.${custom_label}}}'
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab multiple campaigns %}
다중 선택 캠페인의 경우. 캔버스와 동일한 레이블을 공유하면 **변수** 탭에 캔버스 또는 캠페인을 선택할 수 있는 라디오 버튼이 표시됩니다.

- **대체 가치:** 캠페인 BSON ID

{% subtabs %}
{% subtab usage %}
{% raw %}
```sql
campaign_id IN ({{campaigns.${custom_label}}})
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab campaign variants %}
선택한 캠페인에 속한 캠페인 배리언트를 선택합니다. 캠페인 또는 캠페인 변수와 함께 사용해야 합니다.

- **대체 가치:** 캠페인 배리언트 API ID, 쉼표로 구분된 문자열(예: `api-id1, api-id2`.

{% subtabs %}
{% subtab usage %}
{% raw %}
```sql
message_variation_api_id IN ({{campaign_variants.${custom_label}}})
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

{% alert important %}
단일 그룹 내에서 상태를 동기화하려면 모든 캠페인 및 캔버스 변수가 동일한 식별자를 사용해야 합니다.
{% endalert %}

### 캔버스

{% tabs local %}
{% tab one canvas %}
하나의 캔버스를 선택합니다. 캠페인과 동일한 레이블을 공유하면 **변수** 탭에 캔버스 또는 캠페인을 선택할 수 있는 라디오 버튼이 표시됩니다.

- **대체 가치:** 캔버스 BSON ID

{% subtabs %}
{% subtab usage %}
{% raw %}
```sql
canvas_id = '{{canvas.${custom_label}}}'
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab multiple canvases %}
여러 캔버스를 선택하는 경우. 캠페인과 동일한 레이블을 공유하면 **변수** 탭에 캔버스 또는 캠페인을 선택할 수 있는 라디오 버튼이 표시됩니다.

- **대체 가치:** 캔버스 BSON ID

{% subtabs %}
{% subtab usage %}
{% raw %}
```sql
canvas_id IN ({{canvases.${custom_label}}})
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab canvas variants %}
선택한 캔버스에 속한 캔버스 배리언트를 선택합니다. 캔버스 또는 캔버스 변수와 함께 사용해야 합니다. 하나 이상의 캔버스 배리언트 API ID를 쉼표로 구분된 문자열로 설정합니다(예: `api-id1, api-id2`).

{% subtabs %}
{% subtab usage %}
{% raw %}
```sql
canvas_variation_api_id IN ({{canvas_variants.${custom_label}}})
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab one canvas step %}
선택한 캔버스에 속하는 캔버스 단계를 선택합니다. 캔버스 변수와 함께 사용해야 합니다.

{% subtabs %}
{% subtab usage %}
{% raw %}
```sql
canvas_step_api_id = '{{canvas_step.${custom_label}}}'
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab multiple canvas steps %}
선택한 캔버스에 속하는 캔버스 단계를 선택합니다. 캔버스 또는 캔버스 변수와 함께 사용해야 합니다.

{% subtabs %}
{% subtab usage %}
{% raw %}
```sql
canvas_step_api_id IN ({{canvas_steps.${custom_label}}})
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

{% alert important %}
단일 그룹 내에서 상태를 동기화하려면 모든 캠페인 및 캔버스 변수가 동일한 식별자를 사용해야 합니다.
{% endalert %}

### 제품

`products` 는 Braze 대시보드에서 하나 이상의 제품을 선택하는 데 사용됩니다.

{% tabs %}
{% tab usage %}
{% raw %}
```sql
({{products.${custom_label}}})
```
{% endraw %}
{% endtab %}

{% tab example %}
{% raw %}
```sql
SELECT product_name
FROM FULL_GAME_AND_DLC
WHERE product_id IN ({{products.${Games with DLC}}});
```
{% endraw %}
{% endtab %}
{% endtabs %}

### 커스텀 이벤트

목록에서 하나 이상의 커스텀 이벤트 또는 커스텀 이벤트 속성정보를 선택합니다.

{% tabs local %}
{% tab event %}
`custom_events` 는 Braze 대시보드에서 하나 이상의 커스텀 이벤트를 선택하는 데 사용됩니다.

{% subtabs %}
{% subtab usage %}
{% raw %}
```sql
'{{custom_events.${custom_label}}}'
```
{% endraw %}
{% endsubtab %}

{% subtab example %}
{% raw %}
```sql
SELECT event_name
FROM CUSTOM_EVENTS_TABLE
WHERE event_name IN ({{custom_events.${Purchased Game}}}); 
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab properties %}
`custom_event_properties` 는 현재 선택된 커스텀 이벤트에서 하나 이상의 속성을 선택하는 데 사용됩니다.  `custom_events` 변수를 설정해야 합니다.

{% subtabs %}
{% subtab usage %}
{% raw %}
```sql
name = '{{custom_event_properties.${property names)}}}'
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### 작업 공간

`workspace` 은 Braze 대시보드에서 단일 워크스페이스를 선택하는 데 사용됩니다.

{% tabs %}
{% tab usage %}
{% raw %}
```sql
workspace_id = '{{workspace.${app_group_id}}}'
```
{% endraw %}
{% endtab %}
{% endtabs %}

### 카탈로그

목록에서 하나 이상의 카탈로그 또는 카탈로그 필드를 선택합니다.

{% tabs local %}
{% tab catologs %}
`catalogs` 은 Braze 대시보드에서 하나 이상의 카탈로그를 선택하는 데 사용됩니다.

{% subtabs %}
{% subtab usage %}
{% raw %}
```sql
catalog_id = '{{catalogs.${catalog}}}'
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab catolog fields %}
`catalog_fields` 는 현재 선택된 카탈로그에서 하나 이상의 필드를 설정하는 데 사용됩니다. `catalogs` 변수를 설정해야 합니다.

{% subtabs %}
{% subtab usage %}
{% raw %}
```sql
field_name = '{{catalog_fields.${custom_label}}}'
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### 세그먼트

[분석 추적이]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking/) 켜져 있는 세그먼트를 선택합니다. 이 열을 사용할 수 있는 테이블의 `user_segment_membership_ids` 열에 저장된 ID에 해당하는 세그먼트 분석 ID로 설정합니다.

{% tabs %}
{% tab usage %}
{% raw %}
```sql
{{segments.${analytics_segments}}}
```
{% endraw %}
{% endtab %}
{% endtabs %}

### 태그

캠페인 및 캔버스에 사용할 태그를 선택합니다. 선택한 태그와 연결된 작은따옴표로 쉼표로 구분된 BSON ID가 있는 캠페인 및 캔버스로 설정합니다.

{% tabs %}
{% tab usage %}
{% raw %}
```sql
{{tags.${some tags}}}
```
{% endraw %}
{% endtab %}
{% endtabs %}

## 가변 메타데이터

변수 레이블 뒤에 파이프( | ) 문자를 추가하여 메타데이터를 변수에 첨부하여 변수의 동작을 변경할 수 있습니다. 메타데이터의 순서는 중요하지 않으며 원하는 개수만큼 추가할 수 있습니다. 또한 특정 변수에 한정된 특수 메타데이터를 제외한 모든 유형의 메타데이터를 모든 변수에 사용할 수 있습니다(이러한 경우 표시됨). 모든 메타데이터의 사용은 선택 사항이며 기본값의 변수 동작을 변경하는 데 사용됩니다.

{% tabs %}
{% tab usage %}
{% raw %}
```sql
{{string.${my var}| is_required: 'false' | description: 'My optional string var'}}
```
{% endraw %}
{% endtab %}
{% endtabs %}

### 부울

변수 값이 채워졌는지 여부를 알 수 있습니다. 이는 변수 값이 채워지지 않은 경우 조건을 단락시키려는 선택적 변수에 유용합니다. 다른 변수의 값에 따라 `true` 또는 `false` 로 설정할 수 있습니다.

{% tabs %}
{% tab usage %}
{% raw %}
```sql
{{string.${type_name_has_no_value} | visible: 'false'}} or {{string.${type_name_has_value} | visible: 'false'}}
```
{% endraw %}
{% endtab %}
{% endtabs %}

`type` 및 `name` 참조 변수를 참조합니다. 예를 들어, 다음 옵션 변수를 단락시키려면 {% raw %}`{{campaigns.${messaging}}`{% endraw %}:

{% raw %}
```sql
{{string.${campaigns_messaging_has_no_value}  | visible: 'false'}} OR campaign_id IN ({{campaigns.${messaging} | is_required: 'false'}})
```
{% endraw %}

### 가시성

변수가 표시되는지 여부입니다. 모든 변수는 기본값을 입력할 수 있는 **변수** 탭에 표시됩니다.

다른 변수의 값에 따라 값이 달라지는 특수 변수가 몇 가지 있습니다(예: 다른 변수에 값이 있는지 여부). 이러한 특수 변수는 보이지 않는 것으로 표시되어 **변수** 탭에 표시되지 않습니다.

{% tabs %}
{% tab usage %}
```sql
visible: 'false'
```
{% endtab %}
{% endtabs %}

### 필수

변수가 기본값으로 필요한지 여부입니다. 변수의 값이 비어 있으면 일반적으로 잘못된 쿼리가 발생합니다.

{% tabs %}
{% tab usage %}
```sql
required: 'false'
```
{% endtab %}
{% endtabs %}

### 주문

**변수** 탭에서 변수 위치를 선택합니다.

{% tabs %}
{% tab usage %}
```sql
order: '1'
```
{% endtab %}
{% endtabs %}

### 따옴표 포함

{% tabs local %}
{% tab single quotes %}
변수 값을 작은따옴표로 묶을 때 사용합니다.

{% subtabs %}
{% subtab usage %}
```sql
include_quotes: 'true'
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab double quotes %}
변수 값을 큰따옴표로 묶을 때 사용합니다.

{% subtabs %}
{% subtab usage %}
```sql
include_double_quotes: 'true'
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### 입력 안내

변수의 입력 필드에 표시되는 입력 안내 텍스트를 지정합니다.

{% tabs %}
{% tab usage %}
```sql
placeholder: 'enter some value'
```
{% endtab %}
{% endtabs %}

### 설명

변수의 입력 필드 아래에 표시되는 설명 텍스트를 지정합니다.

{% tabs %}
{% tab usage %}
```sql
description: 'some description'
```
{% endtab %}
{% endtabs %}

### 기본값

값을 지정하지 않은 경우 변수의 기본값을 지정합니다.

{% tabs %}
{% tab usage %}
```sql
default_value: '5'
```
{% endtab %}
{% endtabs %}

### 레이블 숨기기

변수의 레이블을 숨기는 데 사용합니다.

{% tabs %}
{% tab usage %}
```sql
hide_label: 'true'
```
{% endtab %}
{% endtabs %}
