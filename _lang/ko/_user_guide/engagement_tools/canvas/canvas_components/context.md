---
nav_title: 컨텍스트 
article_title: 컨텍스트 
alias: /context/
page_order: 1.5
page_type: reference
description: "이 참조 문서에서는 캔버스에서 컨텍스트 단계를 만들고 사용하는 방법에 대해 설명합니다."
tool: Canvas

---

# 컨텍스트

> 컨텍스트 단계를 사용하면 사용자가 캔버스를 이동할 때 하나 이상의 변수를 생성하고 업데이트할 수 있습니다. 예를 들어, 시즌별 할인을 관리하는 캔버스가 있는 경우 컨텍스트 변수를 사용하여 사용자가 캔버스에 들어갈 때마다 다른 할인 코드를 저장할 수 있습니다.

{% alert important %}
컨텍스트 단계는 현재 얼리 액세스 중입니다. Contact your Braze account manager if you're interested in participating in this early access.
{% endalert %}

## How it works

![캔버스의 첫 번째 단계인 컨텍스트 단계]({% image_buster /assets/img/context_step3.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

컨텍스트 단계를 사용하면 사용자가 특정 캔버스를 통과하는 동안 임시 데이터를 생성하고 사용할 수 있습니다. 이 데이터는 해당 캔버스 여정 내에서만 존재하며 다른 캔버스나 세션 외부에 지속되지 않습니다.

이 프레임워크 내에서 각 컨텍스트 단계는 사용자의 프로필 정보를 영구적으로 변경하지 않고도 지연을 개인화하고, 사용자를 동적으로 분류하고, 메시지를 보강할 수 있는 임시 데이터 조각인 여러 컨텍스트 변수를 정의할 수 있습니다.

예를 들어 항공편 예약을 관리하는 경우 각 사용자의 예정된 비행 시간에 대한 컨텍스트 변수를 만들 수 있습니다. 그런 다음 각 사용자의 비행 시간을 기준으로 지연을 설정하고 동일한 캔버스에서 개인화된 알림을 보낼 수 있습니다.

컨텍스트 변수는 두 가지 방법으로 설정할 수 있습니다:

- **캔버스 항목에서:** 사용자가 캔버스에 들어가면 이벤트 또는 API 트리거의 데이터가 컨텍스트 변수를 자동으로 채울 수 있습니다.
- **컨텍스트에서 단계:** 컨텍스트 단계를 추가하여 캔버스 내에서 컨텍스트 변수를 수동으로 정의하거나 업데이트할 수 있습니다.

각 컨텍스트 변수에는 다음이 포함됩니다:

- 이름(예: `flight_time` 또는 `subscription_renewal_date`)
- [데이터 유형](#context-variable-types) (숫자, 문자열, 시간, 배열 등)
- [Liquid를]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) 사용하거나 **개인화 추가** 도구를 통해 할당하는 값입니다.

정의된 컨텍스트 변수는 다음 형식으로 참조하여 캔버스 전체에서 사용할 수 있습니다: {% raw %}`{{context.${example_variable_name}}}`{% endraw %}.

예를 들어
{% raw %}`{{context.${flight_time}}}{% endraw %}` 는 사용자의 예정된 비행 시간을 반환할 수 있습니다.

사용자가 캔버스를 입력할 때마다(이전에 입력한 적이 있더라도) 최신 입력 데이터와 캔버스 설정을 기반으로 컨텍스트 변수가 재정의됩니다. 이를 통해 여러 항목을 입력한 사용자도 개인화되고 정확한 여정을 유지할 수 있습니다.

## 컨텍스트 만들기 단계

### 1단계: 단계 추가

캔버스에 단계를 추가한 다음 사이드바에서 구성 요소를 끌어다 놓거나 <i class="fas fa-plus-circle"></i> 더하기 버튼을 선택하고 **컨텍스트를** 선택합니다.

### 2단계: 변수 정의

{% alert note %}
각 컨텍스트 단계에 대해 최대 10개의 컨텍스트 변수를 정의할 수 있습니다.
{% endalert %}

컨텍스트 변수를 정의합니다:

1. 컨텍스트 변수에 **이름을** 지정합니다.
2. [데이터 유형을](#context-variable-types) 선택합니다.
3. Liquid 표현식을 수동으로 작성하거나 **개인화 추가를** 사용하여 기존 속성에서 Liquid 스니펫을 만듭니다.
4. **미리 보기를** 선택하여 컨텍스트 변수 값을 확인합니다.
5. (선택 사항) 변수를 추가하려면 **컨텍스트 변수 추가를** 선택하고 1~4단계를 반복합니다.
6. 완료했으면 **완료**를 선택합니다.

이제 메시지 및 사용자 업데이트 단계 등 Liquid를 사용하는 모든 곳에서 **개인화 추가를** 선택하여 컨텍스트 변수를 사용할 수 있습니다. 전체 안내는 [컨텍스트 변수 사용하기를](#using-context-variables) 참조하세요.

### 3단계: 사용자 경로 테스트(선택 사항)

컨텍스트 변수가 유효하면 캔버스 전체에서 해당 변수를 참조할 수 있습니다. 그러나 컨텍스트 변수가 올바르게 생성되지 않은 경우 캔버스의 향후 단계도 올바르게 수행되지 않습니다. [사용자 경로를 테스트하고 미리 확인하여]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/preview_user_paths) 메시지가 올바른 대상에게 전송되는지 확인하는 것이 좋습니다. [유효하지 않은 컨텍스트 변수를](#troubleshooting) 생성하는 일반적인 시나리오를 주의하세요.

예를 들어 사용자에게 약속 시간을 할당하는 컨텍스트 단계를 만들지만 약속 시간의 값을 과거 날짜로 설정하면 메시지 단계에서 만든 미리 알림 이메일은 절대로 전송되지 않습니다. 

## 컨텍스트 변수 데이터 유형 {#context-variable-types}

이 단계에서 생성되거나 업데이트되는 컨텍스트 변수에는 다음과 같은 데이터 유형을 할당할 수 있습니다.

{% alert note %}
컨텍스트 변수는 데이터 유형에 대한 예상 형식이 [사용자 지정 이벤트와]({{site.baseurl}}/user_guide/data/custom_data/custom_events/#expected-format) 동일하지만, 컨텍스트 변수는 중첩된 개체를 지원하지 않습니다.
{% endalert %}

| 데이터 유형 | 변수 이름 예시 | 예제 값 |
|---|---|---|
|부울| 충성도_프로그램 |{% raw %}<code>true</code>{% endraw %}| 
|숫자| credit_score |{% raw %}<code>740{% endraw %}|
|문자열| product_name |{% raw %}<code>green_tea</code>{% endraw %} |
|배열| 즐겨찾는_제품|{% raw %}<code>["wireless_headphones", "smart_homehub", "fitness_tracker_swatch"]</code>{% endraw %}|
|Time| 마지막_구매_날짜|{% raw %}<code>2025-12-25T08:15:30:250-0800</code>{% endraw %}|
|개체(평면) | 사용자_프로필|{% raw %}<code>{<br>&emsp;"first_name": "{{user.first_name}}",<br>&emsp;"last_name": "{{user.last_name}}",<br>&emsp;"email": "{{user.email}}",<br>&emsp;"loyalty_points": {{user.loyalty_points}},<br>&emsp;"preferred_categories": {{user.preferred_categories}}<br>}</code>{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 컨텍스트 변수 사용 {#using-context-variables}

예를 들어, 승객에게 다가오는 항공편 전에 VIP 라운지 이용에 대해 알리고 싶다고 가정해 보겠습니다. 이 메시지는 일등석 항공권을 구매한 승객에게만 전송해야 합니다. 컨텍스트 변수는 이러한 정보를 유연하게 추적하는 방법입니다.

사용자는 비행기 티켓을 구매할 때 캔버스에 입장하게 됩니다. 라운지 이용 자격을 결정하기 위해 컨텍스트 단계에서 `lounge_access_granted` 이라는 컨텍스트 변수를 만든 다음, 사용자 여정의 후속 단계에서 해당 컨텍스트 변수를 참조합니다.

![승객이 VIP 라운지 이용 자격이 있는지 추적하도록 컨텍스트 변수를 설정합니다.]({% image_buster /assets/img/context_example4.png %}){: style="max-width:90%"}

이 컨텍스트 단계에서는 {% raw %}`{{custom_attribute.${purchased_flight}}}`{% endraw %} 을 사용하여 구매한 항공편 유형이 `first_class` 인지 확인합니다.

다음으로 {% raw %}`{{context.${lounge_access_granted}}}`{% endraw %} 이 `true` 인 사용자를 타겟팅하는 메시지 단계를 만들겠습니다. 이 메시지는 개인화된 라운지 정보가 포함된 푸시 알림이 됩니다. 이 컨텍스트 변수에 따라 해당 승객은 비행 전에 관련 메시지를 받게 됩니다.

- 일등석 항공권 승객에게는 다음과 같은 혜택이 제공됩니다: "VIP 전용 라운지를 이용하세요!"
- 비즈니스 및 이코노미 항공권 승객에게 제공됩니다: "항공편을 업그레이드하여 VIP 전용 라운지를 이용하세요."

![구매한 항공권 유형에 따라 전송할 메시지가 다른 메시지 단계입니다.]({% image_buster /assets/img/context_example3.png %}){: style="max-width:90%"}

{% alert tip %}
컨텍스트 단계의 정보로 [개인화된 지연 옵션을]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/#personalized-delays) 추가할 수 있습니다. 즉, 사용자를 지연시키는 변수를 선택할 수 있습니다.
{% endalert %}

## 연결된 콘텐츠 문자열을 JSON으로 변환하기

컨텍스트 단계에서 [커넥티드 콘텐츠를 호출할]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call) 때 일관성 및 오류 방지를 위해 호출에서 반환되는 JSON은 문자열 데이터 유형으로 평가됩니다. 이 문자열을 JSON으로 변환하려면 `as_json_string` 을 사용하여 변환합니다. For example:

{%raw%}
```liquid
{% connected_content http://example.com :save product %}
{{ product | as_json_string }}
```
{%endraw%}

## 문제 해결 {#troubleshooting}

### 잘못된 컨텍스트 변수

컨텍스트 변수는 다음과 같은 경우 유효하지 않은 것으로 간주됩니다:
- 임베디드 커넥티드 콘텐츠에 대한 호출이 실패합니다.
- 런타임에 Liquid 표현식은 데이터 유형과 일치하지 않거나 비어 있는 값(null)을 반환합니다.

예를 들어 컨텍스트 변수 데이터 유형이 **숫자이지만** Liquid 표현식이 문자열을 반환하는 경우 유효하지 않습니다.

이런 상황에서는 
- 사용자가 다음 단계로 진행합니다. 
- 캔버스 단계 분석에서는 이를 _업데이트되지 않은_ 것으로 간주합니다.

문제를 해결할 때 _업데이트되지 않음_ 메트릭을 모니터링하여 컨텍스트 변수가 올바르게 업데이트되고 있는지 확인하세요. 컨텍스트 변수가 유효하지 않은 경우 사용자는 컨텍스트 단계를 지나 캔버스에서 계속 진행할 수 있지만 이후 단계에서는 자격을 얻지 못할 수 있습니다.

각 데이터 유형에 대한 설정 예는 [컨텍스트 변수 데이터 유형을](#context-variable-types) 참조하세요.

## Frequently asked questions

### 컨텍스트 변수는 캔버스 항목 속성과 어떻게 다릅니까?

컨텍스트 단계 얼리 액세스에 참여 중인 경우 이제 캔버스 항목 속성이 캔버스 컨텍스트 변수로 포함됩니다. 즉, Liquid 스니펫에서 컨텍스트 변수를 사용하는 것과 유사하게 Braze API를 사용하여 캔버스 항목 속성을 전송하고 다른 단계에서 참조할 수 있습니다.

### 단일 컨텍스트 단계에서 변수가 서로를 참조할 수 있나요?

예. 컨텍스트 단계의 모든 변수는 순서대로 평가되므로 다음과 같은 컨텍스트 변수를 설정할 수 있습니다:

| 컨텍스트 변수 | 값 | 설명 |
|---|---|---|
|`favorite_cuisine`| {% raw %}`{{custom_attribute.${Favorite Cuisine}}}`{% endraw %} | 사용자가 가장 좋아하는 요리 유형입니다. |
|`promo_code`| {% raw %}`EATFRESH`{% endraw %} | 사용자에게 사용 가능한 할인 코드입니다. |
|`personalized_message`|  {% raw %}`"Enjoy a discount of" {{promo_code}} "on delivery from your favorite" {{favorite_cuisine}} restaurants!"`{% endraw %} | 이전 변수를 결합한 개인화된 메시지입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

메시지 단계에서 Liquid 스니펫 {% raw %}`{{context.${personalized_message}}}`{% endraw %} 을 사용하여 컨텍스트 변수를 참조하여 각 사용자에게 개인화된 메시지를 전달할 수 있습니다.

이는 여러 컨텍스트 단계에도 적용됩니다. 예를 들어 다음 시퀀스를 상상해 보세요:
1. 초기 컨텍스트 단계는 `job_title` 값으로 `JobInfo` 라는 변수를 만듭니다.
2. 메시지 단계는 {% raw %}`{{context.${JobInfo}}}`{% endraw %} 을 참조하고 사용자에게 `job_title` 을 표시합니다.
3. 나중에 컨텍스트 단계에서 컨텍스트 변수를 업데이트하여 `JobInfo` 의 값을 `job_description` 으로 변경합니다.
4. `JobInfo` 을 참조하는 모든 후속 단계는 이제 업데이트된 값 `job_description` 을 사용합니다.

컨텍스트 변수는 캔버스 전체에서 가장 최근 값을 사용하며, 업데이트할 때마다 해당 변수를 참조하는 모든 다음 단계에 영향을 줍니다.


