---
nav_title: 연산자
article_title: 리퀴드 오퍼레이터
page_order: 2
description: "이 참조 페이지에는 Liquid가 지원하는 연산자와 관련 예시가 나와 있습니다."

---

# 연산자

> Liquid supports many [operators](https://docs.shopify.com/themes/liquid/basics/operators) that can be used in your conditional statements. 이 페이지는 Liquid가 지원하는 연산자와 이를 메시지에서 사용하는 방법에 대한 사용 사례를 다룹니다.

이 표는 지원되는 연산자를 나열합니다. 괄호는 Liquid에서 유효하지 않은 문자이며 태그가 작동하지 않도록 방지합니다.

|   Syntax| 연산자 설명|
|---------|-----------|
| ==  | 동등함        |
| !=  | 동등하지 않음|
|  >  | 큼  |
| <   | 미만     |
| >=| 다음 이상|
| <= | 다음 이하 |
| 또는 | 조건 A 또는 조건 B|
| 그리고 | 조건 A 및 조건 B|
| 포함 | 문자열 또는 문자열 배열에 문자열이 포함되어 있는지 확인합니다.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
연산자는 조건문(`if`, `elsif`, `unless`)에서 사용할 수 있지만 `assign` 문, `for` 루프, `case`/`when` 문 또는 배열 접근 괄호에서는 사용할 수 없습니다. 전체 분석은 [연산자 및 필터 사용 위치]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#where-to-use-operators-and-filters)를 참조하십시오.
{% endalert %}

### 괄호 없이 조건 그룹화

Liquid는 표현식을 그룹화하기 위해 괄호를 지원하지 않습니다. 복잡한 불리언 논리를 평가하려면 `(a and b) or c`과 같은 중첩 `if` 문 또는 중간 변수를 사용하십시오.

예를 들어, 값이 복합 조건을 만족하는지 확인하려면 중간 변수를 할당하십시오:

{% raw %}
```liquid
{% assign qualifies = false %}
{% if points > 100 %}
{% assign qualifies = true %}
{% elsif points == 100 and member_level == 'gold' %}
{% assign qualifies = true %}
{% endif %}

{% if qualifies %}
You qualify for a reward!
{% endif %}
```
{% endraw %}

## 튜토리얼

Let's go through a few tutorials to learn how to use these operators for your marketing campaigns:

### 정수 커스텀 속성이 있는 메시지를 선택하십시오.

Let's send push notifications with personalized promotional discounts to users who have or haven't made purchases. The push notification will use an integer custom attribute called `total_spend` to check a user's total spend.

1. Write a conditional statement using the greater than (`>`) operator to check if a user's total spend is greater than `0`, indicating they've made a purchase. Then, create a message to send to those users.

{% raw %}
```liquid
{% if {{custom_attribute.${total_spend}}} >0 %}
Surprise! We added a 15% discount code to your account that automatically applies to your next order.
```
{% endraw %}

{: start="2"}
2\. Add the {% raw %}`{% else %}`{% endraw %} tag to capture users whose total spend equals `0` or doesn't exist. Then, create a message to send to those users.

{% raw %}
```liquid
{% else %}
Need a sign to update your wardrobe? We added a 15% discount code to your account that will automatically apply to your first order.
```
{% endraw %}

{: start="3"}
3\. Close the conditional logic with the {% raw %}`{% endif %}`{% endraw %} tag.

{% raw %}
```liquid
{% endif %}
```
{% endraw %}

![A push notification composer with the full Liquid code from the tutorial.]({% image_buster /assets/img/liquid-if-totalspend.png %}){: width="100%"}

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

이제 사용자의 "총 지출" 커스텀 속성이 `0`보다 크면 다음 메시지를 받게 됩니다:

```
Surprise! We added a 15% discount code to your account that automatically applies to your next order.
```
If a user's "Total Spend" custom attribute does not exist or is equal to `0`, they will get the following message:

```
Need a sign to update your wardrobe? We added a 15% discount code to your account that will automatically apply to your first order.
```

### 문자열 커스텀 속성이 있는 메시지를 선택하십시오.

Let's send push notifications to users, and personalize the message based on each user's most recently played game. This will use a string custom attribute called `recent_game` to check which game a user has last played.

1. Write a conditional statement using the equals (`==`) operator to check if a user's most recent game is *Awkward Dinner Party*. Then, create a message to send to those users.

{% raw %}
```liquid
{% if {{custom_attribute.${recent_game}}} == 'Awkward Dinner Party' %}
You are formally invited to our next dinner party. Log on next week for another round of delectable dishes and curious conversations.
```
{% endraw %}

{: start="2"}
2\. Use the `elsif` tag with the equals (`==`) operator to check if user's most recent game is *Proxy War 3: War of Thirst*. Then, create a message to send to those users.

{% raw %}
```liquid
{% elsif {{custom_attribute.${recent_game}}} == 'Proxy War 3: War of Thirst' %}
Your fleet awaits your next orders. Log on when you're ready to rejoin the war for hydration.
```
{% endraw %}

{: start="3"}
3\. 사용자가 최근 게임이 있는지 확인하려면 `elsif` 태그를 사용하고 "같지 않음" (`!=`) 및 "그리고" (`and`) 연산자를 사용하여 값이 비어 있지 않고 게임이 *어색한 저녁 파티* 또는 *프록시 전쟁 3이 아님을 확인하십시오: War of Thirst*. Then, create a message to send to those users.

{% raw %}
```liquid
{% elsif {{custom_attribute.${recent_game}}} != blank and {{custom_attribute.${recent_game}}} != 'Awkward Dinner Party' and {{custom_attribute.${recent_game}}} != 'Proxy War 3: War of Thirst' %}
Limited Time Deal! Get 15% off our best-selling classics!
```
{% endraw %}

{: start="4"}
4\. Add the {% raw %}`{% else %}`{% endraw %} tag to capture users who don't have a recent game. Then, create a message to send to those users.

{% raw %}
```liquid
{% else %}
Hey! I've got a deal for you. Buy 2 of our newest releases and get 10% off!
```
{% endraw %}

{: start="5"}
5\. Close the conditional logic with the {% raw %}`{% endif %}`{% endraw %} tag.

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
{% elsif {{custom_attribute.${recent_game}}} != blank and {{custom_attribute.${recent_game}}} != 'Awkward Dinner Party' and {{custom_attribute.${recent_game}}} != 'Proxy War 3: War of Thirst' %}
Limited Time Deal! Get 15% off our best-selling classics!
{% else %}
Hey! I've got a deal for you. Buy 2 of our newest releases and get 10% off!
{% endif %}
```
{% endraw %}
{% enddetails %}

![A push notification composer with the full Liquid code from the tutorial.]({% image_buster /assets/img/liquid-if-elsif-games.png %})

Now, if a user last played *Awkward Dinner Party*, they'll receive this message:

```
You are formally invited to our next dinner party. Log on next week for another round of delectable dishes and curious conversations.
```

If a user's most recent game is *Proxy War 3: War of Thirst*, they will receive this message:

```
Your fleet awaits your next orders. Log on when you're ready to rejoin the war for hydration.
```

If a user has recently played a game that wasn't *Awkward Dinner Party* or *Proxy War 3: War of Thirst*, they'll get this message:

```
Limited Time Deal! Get 15% off our best-selling classics!
```

If a user hasn't played any games or that custom attribute doesn't exist on their profile, they'll get this message:

```
Hey! I've got a deal for you. Buy 2 of our newest releases and get 10% off!
```

### 위치에 따른 메시지 중단

거의 모든 것을 기준으로 메시지를 중단할 수 있습니다. Let's abort a message if a user isn't based in a specified area, as they might not qualify for the promotion, show, or delivery.

1. Write a conditional statement using the equals (`==`) operator to check if the user's time zone is `America/Los_Angeles`, then create a message to send to those users. 

{% raw %}
```liquid
{% if {{${time_zone}}} == 'America/Los_Angeles' %}
Stream now!
```
{% endraw %}

{: start="2"}
2\. To avoid sending messages to users outside the `America/Los_Angeles` time zone, wrap {% raw %}`{% else %}`{% endraw %} and {% raw %}`{% endif %}`{% endraw %} tags around an {% raw %}`{% abort_message () %}`{% endraw %} tag.

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

![A push notification composer with the full Liquid code from the tutorial.]({% image_buster /assets/img/abort-if.png %})

You can also [abort messages]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/aborting_connected_content/) based on Connected Content.

## 문제 해결

### 미리보기가 속성 유형을 잘못 강제 변환할 수 있습니다. 

대시보드에서 메시지를 미리 볼 때 대부분의 변수(예: 커스텀 속성)는 올바른 유형으로 강제 변환됩니다. 그러나 일부 변수는 미리보기에서 조회할 수 있는 정의된 유형이 없습니다:

- `api_trigger_properties`
- `canvas_entry_properties`
- `context`

이러한 속성에 대해 미리보기는 값에서 유형을 유추하려고 시도합니다. 이는 당신이 **문자열**로 의도한 값이 **숫자**로 잘못 해석될 수 있음을 의미합니다. 예를 들어, 속성 값이 문자열 `"3"`인 경우 미리보기가 이를 정수 `3`로 강제 변환할 수 있으며, 이는 `contains` 또는 `split`과 같은 문자열 작업에서 예기치 않은 동작을 초래할 수 있습니다.

이러한 속성 유형을 사용할 때 예기치 않은 미리보기 결과가 나타나면 미리보기의 유형 유추가 전송 시 발생하는 것과 일치하지 않을 수 있음을 명심하십시오. 전송 시, 트리거 이벤트 또는 API 호출에서 실제 데이터 유형이 보존됩니다.

미리보기에서 특정 유형을 강제로 지정하려면, 값을 명시적으로 캐스팅할 수 있습니다:

{% raw %}
```liquid
{% comment %} Force a value to be treated as a number {% endcomment %}
{% assign orders = {{canvas_entry_properties.${number_of_orders}}} | plus: 0 %}

{% comment %} Force a value to be treated as a string {% endcomment %}
{% assign code = {{api_trigger_properties.${promo_code}}} | append: "" %}
```
{% endraw %}