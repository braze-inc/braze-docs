---
nav_title: 컨텍스트 변수
article_title: 컨텍스트 변수
page_type: reference
description: "이 참조 문서에서는 Braze 캔버스에서의 컨텍스트 변수, 그 유형, 사용법 및 모범 사례를 설명합니다."
---

# 컨텍스트 변수

> 컨텍스트 변수는 특정 캔버스를 통해 사용자의 여정 내에서 생성하고 사용할 수 있는 임시 데이터 조각입니다. 이들은 지연을 개인화하고, 사용자를 동적으로 세그먼트화하며, 사용자의 프로필 정보를 영구적으로 변경하지 않고도 메시징을 풍부하게 할 수 있게 해줍니다. 컨텍스트 변수는 캔버스 세션 내에서만 존재하며, 서로 다른 캔버스나 세션 외부에서는 지속되지 않습니다.

## 컨텍스트 변수가 작동하는 방식

컨텍스트 변수는 두 가지 방법으로 설정할 수 있습니다:

- **캔버스 항목에서:** 사용자가 캔버스에 들어가면 이벤트 또는 API 트리거의 데이터가 컨텍스트 변수를 자동으로 채울 수 있습니다.
- **컨텍스트에서 단계:** 캔버스 내에서 [컨텍스트 단계]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context)를 추가하여 수동으로 컨텍스트 변수를 정의하거나 업데이트할 수 있습니다.

각 컨텍스트 변수에는 다음이 포함됩니다:

- 이름(예: `flight_time` 또는 `subscription_renewal_date`)
- 데이터 유형(예: 숫자, 문자열, 시간 또는 배열)
- [Liquid를]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) 사용하거나 **개인화 추가** 도구를 통해 할당하는 값입니다.

정의된 컨텍스트 변수는 다음 형식으로 참조하여 캔버스 전체에서 사용할 수 있습니다: {% raw %}`{{context.${example_variable_name}}}`{% endraw %}.

예를 들어, {% raw %}`{{context.${flight_time}}}`{% endraw %}은 사용자의 예정된 비행 시간을 반환할 수 있습니다.

사용자가 캔버스를 입력할 때마다(이전에 입력한 적이 있더라도) 최신 입력 데이터와 캔버스 설정을 기반으로 컨텍스트 변수가 재정의됩니다. 이 상태 유지 접근 방식은 각 캔버스 항목이 고유한 독립적인 컨텍스트를 유지할 수 있게 하여, 사용자가 동일한 여정 내에서 여러 활성 상태를 가지면서 각 상태에 대한 특정 컨텍스트를 유지할 수 있게 합니다.

예를 들어, 고객이 두 개의 예정된 비행이 있는 경우, 그들은 동시에 실행되는 두 개의 별도의 여정 상태를 가지게 됩니다. 각 상태는 출발 시간 및 목적지와 같은 비행 특정 컨텍스트 변수를 가집니다. 이렇게 하면 고객의 오후 2시 뉴욕행 비행에 대한 개인화된 알림을 보내면서 내일 오전 8시 로스앤젤레스행 비행에 대한 다른 업데이트를 보낼 수 있어, 각 메시지가 특정 예약과 관련성을 유지합니다.

## 고려 사항

각 [컨텍스트 단계]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/)당 최대 10개의 컨텍스트 변수를 정의할 수 있습니다. 각 변수 이름은 최대 100자까지 가능하며, 문자, 숫자 또는 밑줄만 사용할 수 있습니다.

컨텍스트 변수 정의는 최대 10,240자까지 가능합니다. API 트리거 캔버스로 컨텍스트 변수를 전달하면, 이들은 컨텍스트 단계에서 생성된 변수와 동일한 네임스페이스를 공유합니다. 예를 들어, [`/canvas/trigger/send` 엔드포인트]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/) 컨텍스트 객체에서 변수를 `purchased_item`로 보내면, 이를 {% raw %}`{{context.${purchased_item}}}`{% endraw %}으로 참조할 수 있습니다. 컨텍스트 단계에서 해당 변수를 재정의하면, 새로운 값이 해당 사용자의 여정에 대한 API 값을 덮어쓰게 됩니다.

각 컨텍스트 단계당 최대 50KB를 저장할 수 있으며, 최대 10개의 변수에 분산됩니다. 단계의 모든 변수의 총 크기가 50 KB를 초과하면, 한도를 초과하는 변수는 평가되거나 저장되지 않습니다. 예를 들어, Context 단계에 세 개의 변수가 있는 경우:

- 변수 1: 30 KB
- 변수 2: 19 KB
- 변수 3: 2 KB

변수 3은 이전 변수의 합이 50 KB를 초과하므로 평가되거나 저장되지 않습니다.

## Data types

이 단계에서 생성되거나 업데이트되는 컨텍스트 변수에는 다음과 같은 데이터 유형을 할당할 수 있습니다.

{% alert note %}
Context 변수는 [커스텀 이벤트]({{site.baseurl}}/user_guide/data/custom_data/custom_events/#expected-format)와 동일한 데이터 유형의 예상 형식을 가집니다. <br><br>배열 유형을 사용할 때, Braze는 값을 JSON으로 구문 분석하려고 시도하며, 이는 객체 배열이 성공적으로 생성될 수 있도록 합니다. 배열 내의 객체가 유효한 JSON이 아닌 경우, 결과는 단순한 문자열 배열이 됩니다. <br><br>중첩된 객체 및 객체 배열의 경우, [`as_json_string` Liquid 필터](#converting-connected-content-strings-to-json)를 사용하십시오. Context 단계에서 동일한 객체를 생성하는 경우, `as_json_string`을 사용하여 객체를 렌더링해야 합니다. 예: {%raw%}```{{context.${object_array} | as_json_string }}```{%endraw%}
{% endalert %}

| 데이터 유형 | 변수 이름 예시 | 예제 값 |
|---|---|---|
|부울| loyalty_program |{% raw %}<code>true</code>{% endraw %}| 
|숫자| credit_score |{% raw %}<code>740</code>{% endraw %}|
|문자열| product_name |{% raw %}<code>green_tea</code>{% endraw %} |
|배열| favorite_products|{% raw %}<code>["wireless_headphones", "smart_homehub", "fitness_tracker_swatch"]</code>{% endraw %}|
|객체의 배열| pet_details |{% raw %}<code>[_mem_lt_br>_mem_amp_emsp;{ "id": 1, "type": "dog", "breed": "beagle", "name": "Gus" }_mem_lt_br>_mem_amp_emsp;,_mem_lt_br>_mem_amp_emsp;{ "id": 2, "type": "cat", "breed": "calico", "name": "Gerald" }_mem_lt_br>]</code>{% endraw %}|
|시간 (UTC 기준) | last_purchase_date|{% raw %}<code>2025-12-25T08:15:30:250-0800</code>{% endraw %}|
|개체(평면) | user_profile|{% raw %}<code>{<br>&emsp;"first_name": "{{user.first_name}}",<br>&emsp;"last_name": "{{user.last_name}}",<br>&emsp;"email": "{{user.email}}",<br>&emsp;"loyalty_points": {{user.loyalty_points}},<br>&emsp;"preferred_categories": {{user.preferred_categories}}<br>}</code>{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

기본적으로, 시간 데이터 유형은 UTC입니다. 시간 값을 저장하기 위해 문자열 데이터 유형을 사용하는 경우, PST와 같은 다른 시간대의 시간으로 정의할 수 있습니다. 

예를 들어, 생일 전날 사용자에게 메시지를 보내는 경우, Liquid 논리가 생일 전날 보내는 것과 관련이 있으므로 Context 변수를 시간 데이터 유형으로 저장해야 합니다. 그러나 크리스마스 날(12월 25일)에 휴일 메시지를 보내는 경우, 시간을 동적 변수로 참조할 필요가 없으므로 문자열 데이터 유형을 사용하는 것이 바람직합니다.

## Context 변수 사용

컨텍스트 변수를 캔버스에서 Liquid를 사용하는 모든 곳에서 사용할 수 있습니다. 예를 들어 [메시지]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step) 및 [사용자 업데이트]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update) 단계에서 **개인화 추가**를 선택하여 사용할 수 있습니다.

예를 들어, 승객에게 다가오는 항공편 전에 VIP 라운지 이용에 대해 알리고 싶다고 가정해 보겠습니다. 이 메시지는 일등석 항공권을 구매한 승객에게만 전송해야 합니다. 컨텍스트 변수는 이러한 정보를 유연하게 추적하는 방법입니다.

사용자는 비행기 티켓을 구매할 때 캔버스에 입장하게 됩니다. 라운지 이용 자격을 결정하기 위해 컨텍스트 단계에서 `lounge_access_granted` 이라는 컨텍스트 변수를 만든 다음, 사용자 여정의 후속 단계에서 해당 컨텍스트 변수를 참조합니다.

![승객이 VIP 라운지 접근 자격이 있는지 추적하기 위해 설정된 컨텍스트 변수입니다.]({% image_buster /assets/img/context_example4.png %}){: style="max-width:90%"}

이 컨텍스트 단계에서는 {% raw %}`{{custom_attribute.${purchased_flight}}}`{% endraw %} 을 사용하여 구매한 항공편 유형이 `first_class` 인지 확인합니다.

다음으로 {% raw %}`{{context.${lounge_access_granted}}}`{% endraw %} 이 `true` 인 사용자를 타겟팅하는 메시지 단계를 만들겠습니다. 이 메시지는 개인화된 라운지 정보를 포함하는 푸시 알림이 될 것입니다. 이 컨텍스트 변수에 따라 해당 승객은 비행 전에 관련 메시지를 받게 됩니다.

- 일등석 항공권 승객에게는 다음과 같은 혜택이 제공됩니다: "VIP 전용 라운지를 이용하세요!"
- 비즈니스 및 이코노미 항공권 승객에게 제공됩니다: "항공편을 업그레이드하여 VIP 전용 라운지를 이용하세요."

![구매한 항공권 유형에 따라 전송할 서로 다른 메시지를 가진 메시지 단계입니다.]({% image_buster /assets/img/context_example3.png %}){: style="max-width:90%"}

{% alert tip %}
컨텍스트 단계의 정보로 [개인화된 지연 옵션을]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/#personalized-delays) 추가할 수 있습니다. 즉, 사용자를 지연시키는 변수를 선택할 수 있습니다.
{% endalert %}

### 액션 경로 및 종료 기준에 대해

이 트리거 작업에서 컨텍스트 변수 또는 커스텀 속성과 비교 속성 필터를 활용할 수 있습니다: **Perform Custom Event** and **Make Purchase**. 이 작업 트리거는 기본 및 중첩 속성 모두에 대한 속성 필터를 지원합니다. 

- 기본 속성과 비교할 때 사용 가능한 비교는 커스텀 이벤트에 의해 정의된 속성의 유형과 일치합니다. 예를 들어, 문자열 속성은 정확히 일치하거나 정규식과 일치합니다. 부울 속성은 true 또는 false입니다. 
- 중첩 속성과 비교할 때, 유형이 미리 정의되어 있지 않으므로 부울, 숫자, 문자열, 시간 및 연중일에 대해 여러 데이터 유형 간의 비교를 선택할 수 있습니다. 이는 중첩 커스텀 속성에 대한 비교와 유사합니다. 비교 시 중첩 속성의 실제 데이터 유형과 일치하지 않는 데이터 유형을 선택하면 사용자가 액션 경로 또는 종료 기준과 일치하지 않습니다.

#### 액션 경로 예시

{% alert important %}
커스텀 속성 비교의 경우, 작업이 수행될 때 커스텀 속성 값을 사용합니다. 이는 사용자가 비교 시점에 이 커스텀 속성이 채워져 있지 않거나 커스텀 속성 값이 정의된 속성 비교와 일치하지 않으면 액션 경로 그룹과 일치하지 않음을 의미합니다. 이는 사용자가 액션 경로 단계에 들어갔을 때 일치했더라도 마찬가지입니다.
{% endalert %}

{% tabs %}
{% tab Perform custom event %}

다음 액션 경로는 기본 속성 `source`와 함께 커스텀 이벤트 `Account_Created`을 수행한 사용자를 정렬하도록 설정되어 있습니다. `app_source_variable`에 대한 컨텍스트 변수로.

![커스텀 이벤트를 수행할 때 컨텍스트 변수를 참조하는 액션 경로의 예입니다.]({% image_buster /assets/img/context_action_path1.png %})

{% endtab %}
{% tab Make purchase %}

다음 액션 경로는 특정 제품 이름 `shoes`에 대한 기본 속성 `brand`과 컨텍스트 변수 `promoted_shoe_brand`를 일치시키도록 설정되어 있습니다.

![구매할 때 컨텍스트 변수를 참조하는 액션 경로의 예입니다.]({% image_buster /assets/img/context_action_path2.png %})

{% endtab %}
{% endtabs %}

#### 종료 기준 예시

{% tabs %}
{% tab Perform custom event %}

종료 기준은 사용자가 캔버스에서의 여정 중 언제든지 다음과 같은 경우 캔버스를 종료한다고 명시합니다:

- 사용자가 커스텀 이벤트 **장바구니 포기**를 수행하고,
- 기본 속성 **장바구니의 항목**이 컨텍스트 변수 `cart_item_threshold`의 문자열 값과 일치하는 경우.

![컨텍스트 변수를 기반으로 커스텀 이벤트를 수행하는 경우 사용자를 종료하도록 설정된 종료 기준입니다.]({% image_buster /assets/img/context_exit_criteria1.png %})

{% endtab %}
{% tab Make purchase %}

종료 기준은 사용자가 캔버스에서의 여정 중 언제든지 다음과 같은 경우 캔버스를 종료한다고 명시합니다:

- 사용자가 "책" 제품 이름에 대한 특정 구매를 하고,
- 그 구매의 중첩 속성 "loyalty_program"이 사용자의 커스텀 속성 "VIP"와 같을 때.

![구매를 수행하는 경우 사용자를 종료하도록 설정된 종료 기준입니다.]({% image_buster /assets/img/context_exit_criteria2.png %})

{% endtab %}
{% endtabs %}

### 컨텍스트 변수 필터

이전 선언된 컨텍스트 변수를 [오디언스 경로]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths) 및 [결정 분할]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split) 단계에서 사용하는 필터를 생성할 수 있습니다.

{% alert note %}
컨텍스트 변수 필터는 오디언스 경로 및 결정 분할 단계에서만 사용할 수 있습니다.
{% endalert %}

컨텍스트 변수는 선언되며 캔버스의 범위 내에서만 접근할 수 있으므로 세그먼트에서 참조할 수 없습니다. 컨텍스트 변수 필터는 오디언스 경로와 결정 분할 단계에서 유사하게 작동합니다. 오디언스 경로 단계는 여러 그룹을 나타내고, 결정 분할 단계는 이진 결정을 나타냅니다.

![컨텍스트 변수를 사용하여 필터를 생성할 수 있는 결정 분할 단계 예시입니다.]({% image_buster /assets/img/context_decision_split.png %}){: style="max-width:90%;"}

캔버스의 컨텍스트 변수에 미리 정의된 유형이 있는 것처럼, 컨텍스트 변수와 정적 값 간의 비교는 [일치하는 데이터 유형]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes/nested_custom_attribute_support/#supported-data-types)을 가져야 합니다. 컨텍스트 변수 필터는 부울, 숫자, 문자열, 시간 및 연중일에 대한 여러 데이터 유형 간의 비교를 허용하며, [중첩 커스텀 속성]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes/nested_custom_attribute_support/)에 대한 비교와 유사합니다.

{% alert note %}
컨텍스트 변수와 비교에 동일한 데이터 유형을 사용하십시오. 예를 들어, 컨텍스트 변수가 시간 데이터 유형인 경우 시간 비교(예: "이전" 또는 "이후")를 사용하십시오. 데이터 유형이 일치하지 않는 경우(예: 시간 컨텍스트 변수와 문자열 비교) 예기치 않은 동작이 발생할 수 있습니다.
{% endalert %}

여기 컨텍스트 변수 `product_name`를 정규식 `/braze/`와 비교하는 컨텍스트 변수 필터의 예가 있습니다.

![정규식 "/braze/"와 일치하도록 컨텍스트 변수 "product_name"에 대한 필터 설정입니다.]({% image_buster /assets/img/context_variable_filter1.png %}){: style="max-width:90%;"}

#### 컨텍스트 변수 또는 커스텀 속성 비교

**컨텍스트 변수 또는 커스텀 속성에 비교** 토글을 선택하면 이전에 정의된 컨텍스트 변수 또는 사용자 커스텀 속성과 비교하는 컨텍스트 변수 필터를 구성할 수 있습니다. 이는 API 트리거된 `context`와 같이 사용자별로 동적인 비교를 수행하거나, 컨텍스트 변수에 정의된 복잡한 비교 논리를 압축하는 데 유용할 수 있습니다.

{% tabs %}
{% tab Example 1 %}

사용자가 마지막 3일 동안 앱에 로그인하지 않은 경우와 같이 비활성 기간 후 사용자에게 개인화된 알림을 보내고 싶다고 가정해 보겠습니다. 이 경우 메시지를 받아야 합니다.

당신은 {% raw %}`{{now | minus: 3 | append: ' days'}}`{% endraw %}로 정의된 컨텍스트 변수 `re_engagement_date`를 가지고 있습니다. `3 days`는 사용자의 커스텀 속성으로 저장된 가변적인 양일 수 있습니다. 따라서 `re_engagement_date`가 `last_login_date` (사용자 프로필에 커스텀 속성으로 저장됨) 이후인 경우, 그들은 메시지를 받을 것입니다.

![커스텀 속성을 개인화 유형으로 하는 컨텍스트 변수 "re_engagement_date"에 대한 필터 설정입니다. 커스텀 속성 "last_login_date".]({% image_buster /assets/img/context_variable_filter2.png %})

{% endtab %}
{% tab Example 2 %}

다음 필터는 컨텍스트 변수 `reminder_date`가 컨텍스트 변수 `appointment_deadline`보다 이전인지 비교합니다. 이는 사용자를 오디언스 경로 단계에서 그룹화하여 약속 마감일 전에 추가 알림을 받아야 하는지 여부를 결정하는 데 도움이 될 수 있습니다.

![컨텍스트 변수를 개인화 유형으로 하는 컨텍스트 변수 "reminder_date"에 대한 필터 설정입니다. 컨텍스트 변수 "appointment_deadline".]({% image_buster /assets/img/context_variable_filter3.png %})

{% endtab %}
{% endtabs %}

## 시간대 일관성 표준화

대부분의 이벤트 속성이 타임스탬프 유형을 사용하는 경우 이미 캔버스에서 UTC에 있습니다. 그러나 몇 가지 예외가 있습니다. 캔버스 컨텍스트가 추가됨에 따라, 모든 기본 타임스탬프 이벤트 속성은 액션 기반 캔버스에서 일관되게 UTC로 설정됩니다. 이 변경 사항은 캔버스 단계 및 메시지를 편집할 때 보다 예측 가능하고 일관된 경험을 보장하기 위한 더 넓은 노력의 일환입니다. 이 변경 사항은 특정 캔버스가 컨텍스트 단계를 사용하든 사용하지 않든 모든 액션 기반 캔버스에 영향을 미칠 것입니다.

{% alert important %}
모든 경우에 대해, 타임스탬프가 원하는 시간대에 표시되도록 [Liquid time_zone 필터]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/#things-to-know)를 사용하는 것을 강력히 권장합니다. 이 [컨텍스트 단계 기사에서 자주 묻는 질문]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/#faq-example)를 참조하여 예를 확인할 수 있습니다.
{% endalert %}

## 관련 문서

- [컨텍스트 단계]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/)
- [개인화 및 동적 콘텐츠와 Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/)
