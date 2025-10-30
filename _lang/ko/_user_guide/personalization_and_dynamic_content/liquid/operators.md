---
nav_title: 연산자
article_title: 액체 연산자
page_order: 2
description: "이 참조 페이지는 Liquid가 지원하는 연산자와 관련된 예제를 설명합니다."

---

# 연산자

> Liquid는 조건문에서 사용할 수 있는 많은 [연산자](https://docs.shopify.com/themes/liquid/basics/operators)를 지원합니다. 이 페이지는 Liquid가 지원하는 연산자를 다루고 있으며, 메시지에서 이를 사용하는 방법에 대한 사용 사례를 제공합니다.

이 표는 지원되는 연산자를 나열합니다. 괄호는 Liquid에서 유효하지 않은 문자이며 태그가 작동하지 않도록 방지합니다.

|   구문| 연산자 설명|
|---------|-----------|
| ==  | 같음        |
| !=  | 같지 않음|
|  >  | 보다 큼  |
| <   | 보다 작음     |
| >=| 보다 크거나 같음|
| <= | 보다 작거나 같음 |
| 또는 | 조건 A 또는 조건 B|
| 그리고 | 조건 A 그리고 조건 B|
| 포함 | 문자열 또는 문자열 배열이 문자열을 포함하는지 확인합니다.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 튜토리얼

마케팅 캠페인에서 이러한 연산자를 사용하는 방법을 배우기 위해 몇 가지 튜토리얼을 살펴보겠습니다:

### 정수 사용자 정의 속성이 있는 메시지 선택

구매를 한 사용자와 하지 않은 사용자에게 개인화된 프로모션 할인으로 푸시 알림을 보내겠습니다. 푸시 알림은 사용자의 총 지출을 확인하기 위해 `total_spend`이라는 정수 사용자 정의 속성을 사용할 것입니다.

1. 사용자의 총 지출이 `0`보다 큰지 확인하기 위해 더 큰 (`>`) 연산자를 사용하여 조건문을 작성하세요. 이는 사용자가 구매를 했음을 나타냅니다. 그런 다음, 해당 사용자에게 보낼 메시지를 만듭니다.

{% raw %}
```liquid
{% if {{custom_attribute.${total_spend}}} >0 %}
Surprise! We added a 15% discount code to your account that automatically applies to your next order.
```
{% endraw %}

{: start="2"}
2\. 사용자의 총 지출이 `0`와 같거나 존재하지 않는 경우를 포착하기 위해 {% raw %}`{% else %}`{% endraw %} 태그를 추가합니다. 그런 다음, 해당 사용자에게 보낼 메시지를 만듭니다.

{% raw %}
```liquid
{% else %}
Need a sign to update your wardrobe? We added a 15% discount code to your account that will automatically apply to your first order.
```
{% endraw %}

{: start="3"}
3\. {% raw %}`{% endif %}`{% endraw %} 태그로 조건 논리를 닫습니다.

{% raw %}
```liquid
{% endif %}
```
{% endraw %}

\![튜토리얼의 전체 Liquid 코드가 포함된 푸시 알림 작성기.]({% image_buster /assets/img/liquid-if-totalspend.png %}){: width="100%"}

{% details Full Liquid code %}
{% raw %}
```liquid
{% if {{custom_attribute.${total_spend}}} >0 %}
Surprise! We added a 15% discount code to your account that automatically applies to your next order.
{% else %}
Need a sign to update your wardrobe? We added a 15% discount code to your account that will automatically apply to your first order.
{% endif %}
```
{% endraw %}
{% enddetails %}

이제 사용자의 "총 지출" 사용자 정의 속성이 `0`보다 크면 메시지를 받게 됩니다:

```
Surprise! We added a 15% discount code to your account that automatically applies to your next order.
```
사용자의 "총 지출" 사용자 정의 속성이 존재하지 않거나 `0`과 같으면 다음 메시지를 받게 됩니다:

```
Need a sign to update your wardrobe? We added a 15% discount code to your account that will automatically apply to your first order.
```

### 문자열 사용자 정의 속성이 있는 메시지를 선택하세요

사용자에게 푸시 알림을 보내고 각 사용자가 가장 최근에 플레이한 게임에 따라 메시지를 개인화합시다. 이는 사용자가 마지막으로 플레이한 게임을 확인하기 위해 `recent_game`이라는 문자열 사용자 정의 속성을 사용합니다.

1. 사용자의 가장 최근 게임이 *Awkward Dinner Party*인지 확인하기 위해 같음 (`==`) 연산자를 사용하여 조건문을 작성하세요. 그런 다음, 해당 사용자에게 보낼 메시지를 만듭니다.

{% raw %}
```liquid
{% if {{custom_attribute.${recent_game}}} == 'Awkward Dinner Party' %}
You are formally invited to our next dinner party. Log on next week for another round of delectable dishes and curious conversations.
```
{% endraw %}

{: start="2"}
2\. 사용자의 가장 최근 게임이 *Proxy War 3:인지 확인하기 위해 같음 (`==`) 연산자와 함께 `elsif` 태그를 사용하세요. Thirst* 전쟁입니다. 그런 다음, 해당 사용자에게 보낼 메시지를 만듭니다.

{% raw %}
```liquid
{% elsif {{custom_attribute.${recent_game}}} == 'Proxy War 3: War of Thirst' %}
Your fleet awaits your next orders. Log on when you're ready to rejoin the war for hydration.
```
{% endraw %}

{: start="3"}
3\. 사용자가 최근 게임이 있는지(값이 비어 있지 않음을 의미) 확인하기 위해 같지 않음 (`!=`) 및 "그리고" (`&&`) 연산자와 함께 `elsif` 태그를 사용하여 게임이 *Awkward Dinner Party* 또는 *Proxy War 3:가 아닌지 확인하세요. Thirst* 전쟁입니다. 그런 다음, 해당 사용자에게 보낼 메시지를 만듭니다.

{% raw %}
```liquid
{% elsif {{custom_attribute.${recent_game}}} != blank && 'Awkward Dinner Party' or 'Proxy War 3: War of Thirst' %}
Limited Time Deal! Get 15% off our best-selling classics!
```
{% endraw %}

{: start="4"}
4\. 최근 게임이 없는 사용자를 포착하기 위해 {% raw %}`{% else %}`{% endraw %} 태그를 추가하세요. 그런 다음, 해당 사용자에게 보낼 메시지를 만듭니다.

{% raw %}
```liquid
{% else %}
Hey! I've got a deal for you. Buy 2 of our newest releases and get 10% off!
```
{% endraw %}

{: start="5"}
5\. {% raw %}`{% endif %}`{% endraw %} 태그로 조건 논리를 닫습니다.

{% raw %}
```liquid
{% endif %}
```
{% endraw %}

{% details Full Liquid code %}
{% raw %}
```liquid
{% if {{custom_attribute.${recent_game}}} == 'Awkward Dinner Party' %}
You are formally invited to our next dinner party. Log on next week for another round of delectable dishes and curious conversations.
{% elsif {{custom_attribute.${recent_game}}} == 'Proxy War 3: War of Thirst' %}
Your fleet awaits your next orders. Log on when you're ready to rejoin the war for hydration.
{% elsif {{custom_attribute.${recent_game}}} != blank && 'Awkward Dinner Party' or 'Proxy War 3: War of Thirst' %}
Limited Time Deal! Get 15% off our best-selling classics!
{% else %}
Hey! I've got a deal for you. Buy 2 of our newest releases and get 10% off!
{% endif %}
```
{% endraw %}
{% enddetails %}

\![튜토리얼의 전체 Liquid 코드가 포함된 푸시 알림 작성기.]({% image_buster /assets/img/liquid-if-elsif-games.png %})

이제 사용자가 마지막으로 *Awkward Dinner Party*를 플레이했다면, 이 메시지를 받게 됩니다:

```
You are formally invited to our next dinner party. Log on next week for another round of delectable dishes and curious conversations.
```

사용자의 가장 최근 게임이 *Proxy War 3:인 경우 Thirst* 전쟁입니다. 이 경우 이 메시지를 받게 됩니다:

```
Your fleet awaits your next orders. Log on when you're ready to rejoin the war for hydration.
```

사용자가 최근에 *Awkward Dinner Party* 또는 *Proxy War 3:가 아닌 게임을 플레이했다면 Thirst* 전쟁입니다. 이 경우 이 메시지를 받게 됩니다:

```
Limited Time Deal! Get 15% off our best-selling classics!
```

사용자가 게임을 플레이하지 않았거나 해당 사용자 정의 속성이 프로필에 존재하지 않는 경우, 이 메시지를 받게 됩니다:

```
Hey! I've got a deal for you. Buy 2 of our newest releases and get 10% off!
```

### 위치에 따라 메시지를 중단합니다.

메시지는 거의 모든 것에 따라 중단할 수 있습니다. 사용자가 지정된 지역에 기반하지 않는 경우 메시지를 중단합시다. 그들은 프로모션, 쇼 또는 배달 자격이 없을 수 있습니다.

1. 사용자의 시간대가 `America/Los_Angeles`인지 확인하기 위해 equals (`==`) 연산자를 사용하여 조건문을 작성한 다음, 해당 사용자에게 보낼 메시지를 만듭니다. 

{% raw %}
```liquid
{% if {{${time_zone}}} == 'America/Los_Angeles' %}
Stream now!
```
{% endraw %}

{: start="2"}
2\. `America/Los_Angeles` 시간대 외부의 사용자에게 메시지를 보내지 않으려면 {% raw %}`{% else %}`{% endraw %} 및 {% raw %}`{% endif %}`{% endraw %} 태그를 {% raw %}`{% abort_message () %}`{% endraw %} 태그 주위에 감쌉니다.

{% raw %}
```liquid
{% else %}
{% abort_message () %}
{% endif %}
```
{% endraw %}

{% details Full Liquid code %}
{% raw %}
```liquid
{% if {{${time_zone}}} =='America/Los_Angeles' %}
Stream now!
{% else %}
{% abort_message () %}
{% endif %}
```
{% endraw %}
{% enddetails %}

\![튜토리얼의 전체 Liquid 코드가 포함된 푸시 알림 작성기.]({% image_buster /assets/img/abort-if.png %})

연결된 콘텐츠에 따라 메시지를 [중단할 수도 있습니다]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/aborting_connected_content/).


