---
nav_title: 컨텍스트 
article_title: 컨텍스트 
alias: /context/
page_order: 1.5
page_type: reference
toc_headers: "h2"
description: "이 참조 문서에서는 캔버스에서 컨텍스트 단계를 만들고 사용하는 방법에 대해 설명합니다."
tool: Canvas

---

# 컨텍스트

> 컨텍스트 단계를 사용하면 사용자가 캔버스를 이동할 때 하나 이상의 변수를 생성하고 업데이트할 수 있습니다. 예를 들어 시즌별 할인을 관리하는 캔버스가 있는 경우 컨텍스트 변수를 사용하여 사용자가 캔버스에 들어올 때마다 다른 할인 코드를 저장할 수 있습니다.

{% alert important %}
컨텍스트 단계는 현재 얼리 액세스 중입니다. 이번 얼리 액세스에 참여하려면 Braze 계정 매니저에게 문의하세요.<br><br>캔버스 컨텍스트 단계 미리 보기를 옵트인하면 모든 캔버스에서 타임스탬프가 처리되는 방식이 변경된다는 점에 유의하세요. 이에 대한 자세한 내용은 [시간대 일관성 표준화를](#time-zone-consistency-standardization) 참조하세요.
{% endalert %}

## 작동 방식

캔버스의 첫 번째 단계인 컨텍스트 단계.]({% image_buster /assets/img/context_step3.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

컨텍스트 단계를 사용하면 사용자가 특정 캔버스를 통과하는 동안 임시 데이터를 생성하고 사용할 수 있습니다. 이 데이터는 해당 캔버스 여정 내에서만 존재하며 다른 캔버스나 세션 외부에 지속되지 않습니다.

이 프레임워크 내에서 각 컨텍스트 단계는 사용자의 프로필 정보를 영구적으로 변경하지 않고도 지연을 개인화하고, 사용자를 동적으로 세분화하고, 메시징을 강화할 수 있는 임시 데이터 조각인 여러 컨텍스트 변수를 정의할 수 있습니다.

예를 들어 항공편 예약을 관리하는 경우 각 사용자의 예정된 비행 시간에 대한 컨텍스트 변수를 만들 수 있습니다. 그런 다음 각 사용자의 비행 시간을 기준으로 지연을 설정하고 동일한 캔버스에서 개인화된 알림을 보낼 수 있습니다.

컨텍스트 변수는 두 가지 방법으로 설정할 수 있습니다:

- **캔버스 항목에서:** 사용자가 캔버스에 들어가면 이벤트 또는 API 트리거의 데이터가 컨텍스트 변수를 자동으로 채울 수 있습니다.
- **컨텍스트에서 단계:** 컨텍스트 단계를 추가하여 캔버스 내에서 컨텍스트 변수를 수동으로 정의하거나 업데이트할 수 있습니다.

각 컨텍스트 변수에는 다음이 포함됩니다:

- 이름(예: `flight_time` 또는 `subscription_renewal_date`)
- [데이터 유형](#context-variable-types) (예: 숫자, 문자열, 시간 또는 배열)
- [Liquid를]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) 사용하거나 **개인화 추가** 도구를 통해 지정한 값입니다.

정의된 컨텍스트 변수는 다음 형식으로 참조하여 캔버스 전체에서 사용할 수 있습니다: {% raw %}`{{context.${example_variable_name}}}`{% endraw %}.

예를 들어 {% raw %}`{{context.${flight_time}}}`{% endraw %} 은 사용자의 예정된 비행 시간을 반환할 수 있습니다.

사용자가 캔버스를 입력할 때마다(이전에 입력한 적이 있더라도) 최신 입력 데이터와 캔버스 설정을 기반으로 컨텍스트 변수가 재정의됩니다. 이러한 상태 저장 접근 방식을 사용하면 각 캔버스 항목이 독립적인 컨텍스트를 유지할 수 있으므로 사용자는 각 상태에 대한 특정 컨텍스트를 유지하면서 동일한 여정 내에서 여러 개의 활성 상태를 가질 수 있습니다.

예를 들어, 고객에게 예정된 항공편이 두 개 있는 경우 출발 시간 및 대상과 같은 항공편별 컨텍스트 변수가 있는 두 개의 개별 여정 상태를 동시에 실행할 수 있습니다. 이를 통해 오후 2시 뉴욕행 항공편에 대한 개인화된 알림을 보내는 동시에 내일 오전 8시 로스앤젤레스행 항공편에 대한 다른 업데이트를 전송하여 각 메시지가 특정 예약과 관련성을 유지하도록 할 수 있습니다.

## 고려 사항

- 컨텍스트 단계당 최대 10개의 컨텍스트 변수를 가질 수 있습니다.
- 각 컨텍스트 변수 이름은 최대 100자까지 입력할 수 있습니다.
- 컨텍스트 변수 이름은 유효한 식별자(문자, 숫자, 밑줄만 가능)여야 합니다.
- 컨텍스트 변수 정의는 최대 10,240자까지 입력할 수 있습니다. 
- API 트리거된 캔버스에 전달된 컨텍스트 변수는 캔버스의 컨텍스트 단계에서 생성된 컨텍스트 변수와 동일한 네임스페이스를 공유합니다. 즉, `/canvas/trigger/send` 엔드포인트 [컨텍스트 객체에서]({{site.baseurl}}/api/objects_filters/context_object) `purchased_item` 변수를 보내면 {% raw %}`{context.${purchased_item}}`{% endraw %} 로 참조할 수 있으며, 캔버스의 컨텍스트 단계에서 해당 변수를 다시 선언하면 이전에 보낸 내용을 재정의할 수 있습니다.
- 컨텍스트 단계당 최대 50KB까지 저장할 수 있으며, 단계당 최대 10개의 변수를 분산하여 저장할 수 있습니다. 한 단계에서 50KB를 초과하는 변수 크기는 사용자를 위해 평가되거나 저장되지 않습니다. 이러한 크기는 순차적으로 계산됩니다. 예를 들어 컨텍스트 단계에 3개의 변수가 있는 경우입니다:
  - 변수 1: 30 KB
  - 변수 2: 19 KB
  - 변수 3: 2 KB
  - 즉, 변수 3은 다른 모든 컨텍스트 변수의 합이 50KB를 초과하기 때문에 평가되거나 저장되지 않습니다.

## 컨텍스트 만들기 단계

### 1단계: 단계 추가

캔버스에 단계를 추가한 다음 사이드바에서 컴포넌트를 드래그 앤 드롭하거나 <i class="fas fa-plus-circle"></i> 더하기 버튼을 선택하고 **컨텍스트를** 선택합니다.

### 2단계: 변수 정의

{% alert note %}
각 컨텍스트 단계에 대해 최대 10개의 컨텍스트 변수를 정의할 수 있습니다.
{% endalert %}

컨텍스트 변수를 정의합니다:

1. 컨텍스트 변수에 **이름을** 지정합니다.
2. [데이터 유형을](#context-variable-types) 선택합니다.
3. Liquid 표현식을 직접 작성하거나 **개인화 추가를** 사용하여 기존 속성에서 Liquid 스니펫을 생성하세요.
4. **미리 보기를** 선택하여 컨텍스트 변수 값을 확인합니다.
5. (선택 사항) 변수를 추가하려면 **컨텍스트 변수 추가를** 선택하고 1~4단계를 반복합니다.
6. 완료했으면 **완료를** 선택합니다.

이제 메시지 및 사용자 업데이트 단계 등 Liquid를 사용하는 모든 곳에서 **개인화 추가를** 선택하여 컨텍스트 변수를 사용할 수 있습니다. 전체 안내는 [컨텍스트 변수 사용하기를](#using-context-variables) 참조하세요.

## 컨텍스트 변수 데이터 유형 {#context-variable-types}

이 단계에서 생성되거나 업데이트되는 컨텍스트 변수에는 다음과 같은 데이터 유형을 할당할 수 있습니다.

{% alert note %}
컨텍스트 변수는 데이터 유형에 대해 [커스텀 이벤트와]({{site.baseurl}}/user_guide/data/custom_data/custom_events/#expected-format) 동일한 예상 형식을 갖습니다. <br><br>중첩된 객체 및 객체 배열의 경우 [`as_json_string` Liquid 필터를](#converting-connected-content-strings-to-json) 사용하세요. 컨텍스트 단계에서 동일한 오브젝트를 생성하는 경우, 다음과 같이 `as_json_string` 을 사용하여 오브젝트를 렌더링해야 합니다. {%raw%}```{{context.${object_array} | as_json_string }}```{%endraw%}
{% endalert %}

| 데이터 유형 | 변수 이름 예시 | 예제 값 |
|---|---|---|
|부울| loyalty_program |{% raw %}<code>true</code>{% endraw %}| 
|번호| credit_score |{% raw %}<code>740{% endraw %}|
|문자열| product_name |{% raw %}<code>green_tea</code>{% endraw %} |
|배열| favorite_products|{% raw %}<code>["wireless_headphones", "smart_homehub", "fitness_tracker_swatch"]</code>{% endraw %}|
|시간(UTC 기준) | last_purchase_date|{% raw %}<code>2025-12-25T08:15:30:250-0800</code>{% endraw %}|
|개체(평면) | user_profile|{% raw %}<code>{<br> "first_name": "{{user.first_name}}",<br> "last_name": "{{user.last_name}}",<br> "이메일": "{{user.email}}",<br> "loyalty_points": {{user.loyalty_points}},<br> "preferred_categories": {{user.preferred_categories}}<br>}</code>{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

기본값으로 시간 데이터 유형은 UTC입니다. 문자열 데이터 유형을 사용하여 시간 값을 저장하는 경우 PST와 같은 다른 표준 시간대로 시간을 정의할 수 있습니다. 

예를 들어 생일 전날 사용자에게 메시지를 보내는 경우, 전날 전송과 관련된 Liquid 로직이 있으므로 컨텍스트 변수를 시간 데이터 유형으로 저장할 수 있습니다. 그러나 크리스마스(12월 25일)에 휴일 메시지를 보내는 경우 시간을 동적 변수로 참조할 필요가 없으므로 문자열 데이터 유형을 사용하는 것이 좋습니다.

## 컨텍스트 변수 사용 {#using-context-variables}

예를 들어, 승객에게 다가오는 항공편 전에 VIP 라운지 이용에 대해 알리고 싶다고 가정해 보겠습니다. 이 메시지는 일등석 항공권을 구매한 승객에게만 전송해야 합니다. 컨텍스트 변수는 이 정보를 추적하는 유연한 방법입니다.

사용자는 비행기 티켓을 구매할 때 캔버스에 입장하게 됩니다. 라운지 이용 자격을 결정하기 위해 컨텍스트 단계에서 `lounge_access_granted` 이라는 컨텍스트 변수를 만든 다음, 사용자 여정의 후속 단계에서 해당 컨텍스트 변수를 참조합니다.

\![승객이 VIP 라운지 이용 자격이 있는지 추적하도록 설정된 컨텍스트 변수입니다.]({% image_buster /assets/img/context_example4.png %}){: style="max-width:90%"}

이 컨텍스트 단계에서는 {% raw %}`{{custom_attribute.${purchased_flight}}}`{% endraw %} 을 사용하여 구매한 항공편 유형이 `first_class` 인지 확인합니다.

다음으로 {% raw %}`{{context.${lounge_access_granted}}}`{% endraw %} 이 `true` 인 사용자를 타겟팅하는 메시지 단계를 만들어 보겠습니다. 이 메시지는 개인화된 라운지 정보가 포함된 푸시 알림으로 전송됩니다. 이 컨텍스트 변수를 기반으로 해당 승객은 비행 전에 관련 메시지를 받게 됩니다.

- 일등석 항공권 승객에게는 다음과 같은 혜택이 제공됩니다: "VIP 전용 라운지를 이용하세요!"
- 비즈니스 및 이코노미 항공권 승객에게 제공됩니다: "항공편을 업그레이드하여 VIP 전용 라운지를 이용하세요."

구매한 항공권 유형에 따라 전송할 메시징이 다른 메시지 단계입니다.]({% image_buster /assets/img/context_example3.png %}){: style="max-width:90%"}

{% alert tip %}
컨텍스트 단계의 정보로 [개인화된 지연 옵션을]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/#personalized-delays) 추가할 수 있습니다. 즉, 사용자를 지연시키는 변수를 선택할 수 있습니다.
{% endalert %}

### 행동 경로 및 종료 기준의 경우

이러한 트리거 동작에서 컨텍스트 변수 또는 커스텀 속성과 속성 필터를 비교하여 활용할 수 있습니다: **커스텀 이벤트 진행** 및 **구매하기**. 이러한 동작 트리거는 기본 및 중첩 프로퍼티 모두에 대한 프로퍼티 필터도 지원합니다. 

- 기본 속성과 비교할 때 사용 가능한 비교는 커스텀 이벤트에 정의된 속성 유형과 일치합니다. 예를 들어 문자열 속성은 정확히 동일한 정규식 일치를 갖습니다. 부울 속성은 참 또는 거짓입니다. 
- 중첩된 속성을 비교할 때는 유형이 미리 정의되지 않으므로 중첩된 고객 속성을 비교할 때와 마찬가지로 부울, 숫자, 문자열, 시간 및 요일에 대해 여러 데이터 유형에 걸쳐 비교를 선택할 수 있습니다. 비교 시점에 중첩된 속성의 실제 데이터 유형과 일치하지 않는 데이터 유형을 선택하면 사용자는 행동 경로 또는 종료 기준과 일치하지 않게 됩니다.

#### 행동 경로 예시

{% alert important %}
커스텀 속성 비교의 경우 작업이 수행되는 시점의 커스텀 속성 값을 사용합니다. 즉, 비교 시점에 사용자에게 이 커스텀 속성이 채워져 있지 않거나 커스텀 속성 값이 정의된 속성 비교와 일치하지 않는 경우 사용자가 행동 경로 그룹과 일치하지 않습니다. 이는 사용자가 행동 경로 단계에 진입했을 때 일치하는 경우에도 마찬가지입니다.
{% endalert %}

{% tabs %}
{% tab Perform custom event %}

다음 행동 경로는 기본 속성 `source` 을 가진 커스텀 이벤트 `Account_Created` 를 수행한 사용자를 컨텍스트 변수 `app_source_variable` 로 정렬하도록 설정되어 있습니다.

커스텀 이벤트를 수행할 때 컨텍스트 변수를 참조하는 행동 경로 예시입니다.]({% image_buster /assets/img/context_action_path1.png %})

{% endtab %}
{% tab Make purchase %}

다음 행동 경로는 특정 제품 이름 `shoes` 에 대한 기본 속성 `brand` 을 컨텍스트 변수 `promoted_shoe_brand` 와 일치하도록 설정됩니다.

구매 시 컨텍스트 변수를 참조하는 행동 경로의 예시입니다.]({% image_buster /assets/img/context_action_path2.png %})

{% endtab %}
{% endtabs %}

#### 종료 기준 예시

{% tabs %}
{% tab Perform custom event %}

종료 기준은 사용자가 캔버스 내 여정의 어느 시점에서든 다음과 같은 경우 캔버스를 종료한다고 명시합니다:

- 커스텀 이벤트 **장바구니 유기**, 그리고
- 기본 속성 **Item in Cart는** 컨텍스트 변수 `cart_item_threshold` 의 문자열 값과 일치합니다.

컨텍스트 변수를 기반으로 커스텀 이벤트를 수행하면 사용자를 종료하도록 설정한 종료 기준입니다.]({% image_buster /assets/img/context_exit_criteria1.png %})

{% endtab %}
{% tab Make purchase %}

종료 기준은 사용자가 캔버스 내 여정의 어느 시점에서든 다음과 같은 경우 캔버스를 종료한다고 명시합니다:

- '책' 제품명으로 특정 제품을 구매하고
- 해당 구매의 중첩 고객 속성 "loyalty_program" 은 사용자의 커스텀 속성 "VIP"와 동일합니다.

!!! 사용자가 구매를 하면 종료하도록 종료 기준을 설정합니다.]({% image_buster /assets/img/context_exit_criteria2.png %})

{% endtab %}
{% endtabs %}

### 컨텍스트 변수 필터

[오디언스 경로]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths) 및 [결정 분할]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split) 단계에서 이전에 선언한 컨텍스트 변수를 사용하는 필터를 만들 수 있습니다.

{% alert important %}
컨텍스트 변수 필터는 오디언스 경로 및 결정 분할 단계에서만 사용할 수 있습니다.
{% endalert %}

컨텍스트 변수는 캔버스의 범위 내에서만 선언되고 액세스 가능하므로 세그먼트에서 참조할 수 없습니다. 컨텍스트 변수 필터는 오디언스 경로 및 결정 분할 단계에서 유사하게 작동합니다. 오디언스 경로 단계는 여러 그룹을 나타내며, 결정 분할 단계는 이진 결정을 나타냅니다.

컨텍스트 변수가 있는 필터를 만드는 옵션이 있는 결정 분할 단계 예제입니다.]({% image_buster /assets/img/context_decision_split.png %}){: style="max-width:90%;"}

캔버스 컨텍스트 변수에 사전 정의된 유형이 있는 것과 마찬가지로, 컨텍스트 변수와 정적 값 간의 비교에는 [일치하는 데이터 유형이]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes/nested_custom_attribute_support/#supported-data-types) 있어야 합니다. 컨텍스트 변수 필터를 사용하면 [중첩된 고객 속성의]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes/nested_custom_attribute_support/) 비교와 마찬가지로 부울, 숫자, 문자열, 시간, 요일 등 여러 데이터 유형에 대한 비교를 수행할 수 있습니다.

{% alert note %}
컨텍스트 변수와 비교에 동일한 데이터 유형을 사용하세요. 예를 들어 컨텍스트 변수가 시간 데이터 유형인 경우 시간 비교(예: "전" 또는 "후")를 사용합니다. 일치하지 않는 데이터 유형(예: 시간 컨텍스트 변수와 문자열 비교)을 사용하면 예기치 않은 동작이 발생할 수 있습니다.
{% endalert %}

다음은 컨텍스트 변수 `product_name` 와 정규식 `/braze/` 을 비교하는 컨텍스트 변수 필터의 예입니다.

컨텍스트 변수 "product_name" 에 대한 필터 설정이 정규식 "/braze/"와 일치하도록 합니다.]({% image_buster /assets/img/context_variable_filter1.png %}){: style="max-width:90%;"}

#### 컨텍스트 변수 또는 커스텀 속성과 비교하기

**컨텍스트 변수 또는 커스텀 속성과 비교** 토글을 선택하면 이전에 정의한 컨텍스트 변수 또는 사용자 커스텀 속성과 비교하는 컨텍스트 변수 필터를 구성할 수 있습니다. 이는 API 트리거된 `context` 과 같이 사용자별로 동적인 비교를 수행하거나 컨텍스트 변수에 걸쳐 정의된 복잡한 비교 로직을 압축하는 데 유용할 수 있습니다.

{% tabs %}
{% tab Example 1 %}

지난 3일 동안 앱에 로그인하지 않은 사용자를 포함하여 일정 기간 동안 활동이 없는 사용자에게 개인화된 알림 메시지를 보내고 싶다고 가정해 보겠습니다.

{% raw %}`{{now | minus: 3 | append: ' days'}}`{% endraw %} 으로 정의된 컨텍스트 변수 `re_engagement_date` 가 있습니다. `3 days` 은 사용자의 커스텀 속성으로 저장되는 가변 금액일 수도 있습니다. 따라서 `last_login_date` (고객 프로필에 커스텀 속성으로 저장됨) 뒤에 `re_engagement_date` 이 오면 메시지가 전송됩니다.

\![커스텀 속성 "last_login_date".]({% image_buster /assets/img/context_variable_filter2.png %} 뒤에 컨텍스트 변수 "re_engagement_date" 에 대한 개인화 유형으로 커스텀 속성을 사용하는 필터 설정입니다.)

{% endtab %}
{% tab Example 2 %}

다음 필터는 컨텍스트 변수 `reminder_date` 가 컨텍스트 변수 `appointment_deadline` 보다 앞에 있는지 비교합니다. 이를 통해 오디언스 경로 단계의 사용자를 그룹화하여 약속 마감일 전에 추가 알림을 받아야 하는지 여부를 결정할 수 있습니다.

\![컨텍스트 변수 "appointment_deadline".]({% image_buster /assets/img/context_variable_filter3.png %}의 컨텍스트 변수 "reminder_date" 에 대한 개인화 유형으로 컨텍스트 변수를 사용하는 필터 설정입니다.)

{% endtab %}
{% endtabs %}

## 사용자 경로 미리보기

[사용자 경로를]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/preview_user_paths) 테스트하고 [미리]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/preview_user_paths) 확인하여 메시지가 올바른 오디언스에게 전송되고 컨텍스트 변수가 예상 결과에 맞게 평가되는지 확인하는 것이 좋습니다.

{% alert note %}
편집기의 **미리보기 & 테스트 보내기** 섹션에서 캔버스를 미리 보는 경우, 이 패널은 미리 보기를 문자열로 생성하므로 테스트 메시지 미리보기의 타임스탬프가 UTC로 **표준화되지** 않습니다. 즉, 캔버스가 `time` 개체를 허용하도록 설정된 경우 메시지 미리보기는 캔버스가 라이브 상태일 때 발생하는 내용을 정확하게 미리 볼 수 없습니다. 캔버스를 가장 정확하게 테스트하려면 대신 사용자 경로를 미리 보는 것이 좋습니다.
{% endalert %}

잘못된 컨텍스트 변수를 생성하는 일반적인 시나리오를 관찰하세요. 사용자 경로를 미리 볼 때 컨텍스트 변수를 사용하여 개인화된 지연 단계의 결과와 사용자를 컨텍스트 변수와 일치시키는 모든 대상, 의사 결정 또는 행동 경로 단계 비교를 볼 수 있습니다.

컨텍스트 변수가 유효하면 캔버스 전체에서 해당 변수를 참조할 수 있습니다. 그러나 컨텍스트 변수가 올바르게 생성되지 않은 경우 캔버스의 향후 단계도 올바르게 수행되지 않습니다. 예를 들어 사용자에게 약속 시간을 할당하는 컨텍스트 단계를 만들지만 약속 시간의 값을 과거 날짜로 설정하면 메시지 단계의 리마인더 이메일이 전송되지 않습니다.

## 연결된 콘텐츠 문자열을 JSON으로 변환하기

컨텍스트 단계에서 [연결된 콘텐츠를 호출할]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call) 때 일관성 및 오류 방지를 위해 호출에서 반환되는 JSON은 문자열 데이터 유형으로 평가됩니다. 이 문자열을 JSON으로 변환하려면 `as_json_string` 을 사용하여 변환합니다. 예를 들어

{%raw%}
```liquid
{% connected_content http://example.com :save product %}
{{ product | as_json_string }}
```
{%endraw%}

## 시간대 일관성 표준화

캔버스 컨텍스트가 추가되면 동작 기반 캔버스의 [트리거 이벤트 속성정보에서]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties) [날짜/시간 유형을]({{site.baseurl}}/user_guide/data/custom_data/custom_events/#custom-event-properties) 가진 모든 타임스탬프가 항상 [UTC로](https://en.wikipedia.org/wiki/Coordinated_Universal_Time) 정규화됩니다. 이전에는 이벤트 속성정보의 타임스탬프가 [일부 예외를 제외하고]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/#things-to-know) UTC로 정규화되었습니다. 이제 캔버스 단계와 메시지를 편집할 때 보다 일관된 경험을 제공할 수 있습니다.

이 변경 사항이 캔버스의 타임스탬프에 어떤 영향을 미치는지 이 예시를 살펴보세요. 캔버스의 첫 번째 단계에서 이벤트 속성정보를 사용하는 액션 기반 캔버스와 다음 메시지 단계가 있다고 가정해 보겠습니다: 

{% raw %}
`Your appointment is scheduled for {{canvas_entry_properties.${appointment_time} | date: "%Y-%m-%d %l:%M %p"}}, we'll see you then!`
{% endraw %}

메시지 단계를 첫 번째 단계로 하는 컨텍스트 여정.]({% image_buster /assets/img/context_timezone_example.png %}){: style="max-width:50%"}

이 단계에는 다음과 같은 이벤트 페이로드도 포함됩니다: 

```
{
  "appointment_time": "2025-08-05T08:15:30:250-0800"
}
```

지금까지의 메시지는 다음과 같습니다: `Your appointment is scheduled for 2025-08-05 8:15am, we'll see you then!`

캔버스 컨텍스트 얼리 액세스를 통해 이제 메시징이 제공됩니다: `Your appointment is scheduled for 2025-08-05 4:15pm, we’ll see you then!` 이는 타임스탬프가 태평양 표준시( `-08:00`)로 원래 페이로드에 지정된 시간대보다 8시간 빠른 UTC로 되어 있기 때문입니다.

{% alert important %}
이러한 타임스탬프 변경을 고려하여 모든 상황에서 원하는 시간대의 담당자가 타임스탬프에 [Liquid 필터를 사용할]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/#things-to-know) 것을 강력히 권장합니다.
{% endalert %}

### Liquid를 사용하여 원하는 시간대의 타임스탬프 표시하기

다음 Liquid 스니펫을 고려하세요:

{% raw %}
```
Your appointment is scheduled for {{canvas_entry_properties.${appointment_time} | time_zone: "America/Los_Angeles" | date: "%Y-%m-%d %l:%M %p"}}, we'll see you then!
```
{% endraw %}

이 로직은 다음과 같은 출력을 생성합니다: `Your appointment is scheduled for 2025-08-05 8:15am, we'll see you then!`

선호하는 시간대는 이벤트 속성정보 페이로드에 전송되어 Liquid 로직에서 사용될 수도 있습니다: 

```
{
  "appointment_time": "2025-08-05T08:15:30:250-0800"
  "user_timezone": "America/Los_Angeles"
}
```

Liquid 스니펫의 예시입니다:

{% raw %}
```
Your appointment is scheduled for {{canvas_entry_properties.${appointment_time} | time_zone: canvas_entry_properties.${user_timezone} | date: "%Y-%m-%d %l:%M %p"}}, we'll see you then!
```
{% endraw %}

## 문제 해결 {#troubleshooting}

### 잘못된 컨텍스트 변수

컨텍스트 변수는 다음과 같은 경우 유효하지 않은 것으로 간주됩니다:
- 임베드된 연결된 콘텐츠에 대한 호출이 실패했습니다.
- 런타임에 Liquid 표현식은 데이터 유형과 일치하지 않거나 비어 있는 값(null)을 반환합니다.

예를 들어 컨텍스트 변수 데이터 유형이 **숫자이지만** Liquid 표현식이 문자열을 반환하는 경우 유효하지 않습니다.

이런 상황에서는 
- 사용자는 다음 단계로 진행됩니다. 
- 캔버스 단계 분석에서는 이를 _업데이트되지 않음으로_ 계산합니다.

문제 해결 시 _업데이트되지 않음_ 측정기준을 모니터링하여 컨텍스트 변수가 올바르게 업데이트되고 있는지 확인하세요. 컨텍스트 변수가 유효하지 않은 경우 사용자는 컨텍스트 단계를 지나 캔버스에서 계속 진행할 수 있지만 이후 단계에 대한 자격을 얻지 못할 수 있습니다.

각 데이터 유형에 대한 설정 예는 [컨텍스트 변수 데이터 유형을](#context-variable-types) 참조하세요.

## 자주 묻는 질문

### 컨텍스트 변수는 캔버스 항목 프로퍼티와 어떻게 다릅니까?

컨텍스트 단계 얼리 액세스에 참여 중인 경우 이제 캔버스 항목 속성이 캔버스 컨텍스트 변수로 포함됩니다. 즉, Liquid 스니펫에서 컨텍스트 변수를 사용하는 것과 유사하게 Braze API를 사용하여 캔버스 항목 속성을 전송하고 다른 단계에서 이를 참조할 수 있습니다.

### 변수가 Singular Context 단계에서 서로 참조할 수 있나요?

예. 컨텍스트 단계의 모든 변수는 순서대로 평가되므로 다음과 같은 컨텍스트 변수를 설정할 수 있습니다:

| 컨텍스트 변수 | 가치 | 설명 |
|---|---|---|
|`favorite_cuisine`| {% raw %}`{{custom_attribute.${Favorite Cuisine}}}`{% endraw %} | 사용자가 가장 좋아하는 요리 유형입니다. |
|`promo_code`| {% raw %}`EATFRESH`{% endraw %} | 사용자가 사용할 수 있는 할인 코드입니다. |
|`personalized_message`|  {% raw %}`"Enjoy a discount of" {{context.promo_code}} "on delivery from your favorite" {{context.favorite_cuisine}} restaurants!"`{% endraw %} | 이전 변수를 결합한 개인화된 메시지입니다. 메시지 단계에서 Liquid 스니펫 {% raw %}`{{context.${personalized_message}}}`{% endraw %} 을 사용하여 컨텍스트 변수를 참조하여 각 사용자에게 개인화된 메시지를 전달할 수 있습니다. 컨텍스트 단계를 사용하여 [프로모션 코드]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes#creating-a-promotion-code-list) 값을 저장하고 캔버스 전체에서 다른 단계에 템플릿으로 사용할 수도 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

이는 여러 컨텍스트 단계에도 적용됩니다. 예를 들어 다음 시퀀스를 상상해 보세요:
1. 초기 컨텍스트 단계는 `job_title` 값으로 `JobInfo` 라는 변수를 만듭니다.
2. 메시지 단계는 {% raw %}`{{context.${JobInfo}}}`{% endraw %} 을 참조하고 사용자에게 `job_title` 을 표시합니다.
3. 나중에 컨텍스트 단계에서 컨텍스트 변수를 업데이트하여 `JobInfo` 의 값을 `job_description` 으로 변경합니다.
4. `JobInfo` 을 참조하는 모든 후속 단계는 이제 업데이트된 값 `job_description` 을 사용합니다.

컨텍스트 변수는 캔버스 전체에서 가장 최근 값을 사용하며, 각 업데이트는 해당 변수를 참조하는 모든 다음 단계에 영향을 미칩니다.

### 캔버스 컨텍스트 시간대 일관성 표준화가 API 트리거 캔버스에 영향을 주나요?

아니요, 이 변경 사항은 동작이 트리거된 캔버스에만 영향을 줍니다. API 트리거 캔버스로 전송되는 타임스탬프는 시간 유형이 아닌 문자열 유형을 사용하므로 원래 시간대가 항상 유지됩니다.

### 이것은 캔버스 항목 속성 및 이벤트 속성정보에 명시된 예외와 어떤 관련이 있나요?

캔버스 컨텍스트 얼리 액세스에 참여하면 캔버스 컨텍스트 단계를 사용하는지 여부에 관계없이 [이러한 예외가]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/#things-to-know) 제거됩니다.
