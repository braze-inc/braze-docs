---
nav_title: 연산자
article_title: 리퀴드 오퍼레이터
page_order: 2
description: "이 참조 페이지에는 Liquid가 지원하는 연산자와 관련 예시가 나와 있습니다."

---

# 연산자

> Liquid supports many [operators](https://docs.shopify.com/themes/liquid/basics/operators) that can be used in your conditional statements. 이 페이지에서는 Liquid가 지원하는 연산자를 다루고, 메시지에서 어떻게 사용할 수 있는지에 대한 사용 사례를 제공합니다.

이 표에는 지원되는 연산자가 나열되어 있습니다. 괄호는 Liquid에서 유효하지 않은 문자이며 태그가 작동하지 않도록 합니다.

|   구문| 연산자 설명|
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

## 튜토리얼

Let's go through a few tutorials to learn how to use these operators for your marketing campaigns:

### 정수 사용자 지정 속성이 있는 메시지 선택하기

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

Now if a user's "Total Spend" custom attribute is greater than `0`, they will get the message:

```
Surprise! We added a 15% discount code to your account that automatically applies to your next order.
```
If a user's "Total Spend" custom attribute does not exist or is equal to `0`, they will get the following message:

```
Need a sign to update your wardrobe? We added a 15% discount code to your account that will automatically apply to your first order.
```

### 문자열 사용자 지정 속성이 있는 메시지 선택

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
3\. Use the `elsif` tag with the does not equal (`!=`) and "and" (`&&`) operators to check if the user has a recent game (meaning the value isn't blank), and that the game isn't *Awkward Dinner Party* or *Proxy War 3: War of Thirst*. Then, create a message to send to those users.

{% raw %}
```liquid
{% elsif {{custom_attribute.${recent_game}}} != blank && 'Awkward Dinner Party' or 'Proxy War 3: War of Thirst' %}
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
{% elsif {{custom_attribute.${recent_game}}} != blank && 'Awkward Dinner Party' or 'Proxy War 3: War of Thirst' %}
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


