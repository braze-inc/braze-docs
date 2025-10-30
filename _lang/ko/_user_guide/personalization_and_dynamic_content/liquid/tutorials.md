---
nav_title: 튜토리얼
article_title: "튜토리얼: Liquid 코드 작성하기"
page_order: 11
description: "이 참조 페이지에는 Liquid 코드 시작하는 데 도움이 되는 초보자 친화적인 튜토리얼이 포함되어 있습니다."
page_type: tutorial
---

# 튜토리얼: Liquid 코드 작성하기

> Liquid에 처음이신가요? 이 튜토리얼은 초보자 친화적인 사용 사례를 위해 Liquid 코드 작성 시작하는 데 도움이 될 것입니다. 각 튜토리얼은 조건 논리 및 연산자와 같은 다양한 학습 목표의 조합을 다룹니다.

이 튜토리얼을 마치면 다음을 할 수 있습니다:

- 일반적인 사용 사례에 대한 Liquid 코드 작성하기
- 사용자 데이터에 따라 메시지를 개인화하기 위해 Liquid 조건 논리 연결하기
- 변수와 필터를 사용하여 속성의 값을 사용하는 방정식 작성하기
- Liquid 코드의 기본 명령을 인식하고 코드가 수행하는 작업에 대한 일반적인 이해 형성하기

| 튜토리얼 | 학습 목표 |
| --- | --- |
| [사용자 세그먼트에 대한 메시지 개인화](#segments) | 기본값, 조건 논리 |
| [버려진 장바구니 알림](#reminders) | 연산자, 조건 논리 |
| [이벤트 카운트다운](#countdown) | 변수, 날짜 필터 |
| [매월 생일 메시지](#birthday) | 변수, 날짜 필터, 연산자 |
| [좋아하는 제품 홍보](#favorite-product) | 변수, 날짜 필터, 방정식, 연산자 |
{: .reset-br-td-1 .reset-br-td-2}

## 사용자 세그먼트 {#segments}에 대한 개인화된 메시지

VIP 고객 및 신규 구독자와 같은 다양한 사용자 세그먼트에 맞게 메시지를 사용자 정의해 보겠습니다.

1. 사용자의 이름이 있을 때와 없을 때 보낼 개인화된 인사말로 메시지를 열어보세요. 이를 위해 `first_name` 속성을 포함하고 `first_name`가 비어 있을 경우 사용할 기본값을 포함하는 Liquid 태그를 생성합니다. 이 시나리오에서는 기본값으로 "여행자"를 사용해 보겠습니다.

{% raw %}
```liquid
Happy summer, {{${first_name} | default: "traveler"}}!
```
{% endraw %}

{: start="2"}
2\. 이제 사용자가 VIP 고객인 경우 보낼 메시지를 제공하겠습니다. 이를 위해 조건부 논리 태그 `if`를 사용해야 합니다. 이 태그는 `vip_status` 사용자 정의 속성이 `VIP`와 같으면 다음 Liquid가 수행된다고 말합니다. 이 경우 특정 메시지가 전송됩니다.

{% raw %}
```liquid
{% if {{custom_attribute.${vip_status}}} == 'VIP' %}
Thank you for being a VIP customer! Enjoy your exclusive discount code: VIPSUMMR464.
```
{% endraw %}

{: start="3"}
3\. 신규 구독자에게 맞춤형 메시지를 보내보겠습니다. 사용자의 `vip_status`가 `new`인 경우 다음 메시지를 전송하도록 조건부 논리 태그 `elsif`를 사용하겠습니다.

{% raw %}
```liquid
{% elsif {{custom_attribute.${vip_status}}} == 'new' %}
Thank you for subscribing! Enjoy your welcome discount code: NEWTRAVEL257.
```
{% endraw %}

{: start="4"}
4\. VIP 또는 신규가 아닌 사용자들은 어떻게 하나요? 우리는 `else` 태그를 사용하여 모든 다른 사용자에게 메시지를 보낼 수 있습니다. 이 태그는 이전 조건이 충족되지 않을 경우 다음 메시지를 보내야 함을 지정합니다. 그런 다음 `endif` 태그로 조건부 논리를 닫을 수 있습니다. 더 이상 고려할 VIP 상태가 없기 때문입니다.

{% raw %}
```liquid
{% else %}
Thanks for traveling with us! Enjoy your unique discount code: SUMMRTRVLS240.
{% endif %}
```
{% endraw %}

{% details Full Liquid code %}
{% raw %}
```liquid
Happy summer, {{${first_name} | default: "traveler"}}!
{% if {{custom_attribute.${vip_status}}} == 'VIP' %}
Thank you for being a VIP customer! Enjoy your exclusive discount code: VIPSUMMR464.
{% elsif {{custom_attribute.${vip_status}}} == 'new' %}
Thank you for subscribing! Enjoy your welcome discount code: NEWTRAVEL257.
{% else %}
Thanks for traveling with us! Enjoy your unique discount code: SUMMRTRVLS240.
{% endif %}
```
{% endraw %}
{% enddetails %}

## 버려진 장바구니 알림 {#reminders}

사용자에게 장바구니에 남아 있는 항목을 상기시키기 위해 개인화된 메시지를 보내봅시다. 장바구니에 있는 항목 수에 따라 추가로 사용자화하여, 항목이 세 개 이하인 경우 모든 항목을 나열합니다. 항목이 세 개를 초과하는 경우, 더 간결한 메시지를 보낼 것입니다.

1. 사용자의 장바구니가 비어 있는지 확인하기 위해 `!=` 연산자를 사용하여 Liquid 조건부 논리를 열어봅시다. 이는 "같지 않다"는 의미입니다. 이 경우, 우리는 사용자 정의 속성 `cart_items`가 빈 값과 같지 않도록 조건을 설정할 것입니다.

{% raw %}
```liquid
{% if {{custom_attribute.${cart_items}}} != blank %}
```
{% endraw %}

{: start="2"}
2\. 그런 다음, 장바구니에 세 개 이상의 항목이 있는지 확인하기 위해 \`>\` 연산자를 사용하여 초점을 좁혀야 합니다. 이는 "보다 크다"는 의미입니다.

{% raw %}
```liquid
{% if {{custom_attribute.${cart_items}}} | size > 3 %}
```
{% endraw %}

{: start="3"}
3\. 사용자를 이름으로 인사하는 메시지를 작성하거나, 이름이 없을 경우 기본값으로 "거기"를 사용합니다. 장바구니에 세 개 이상의 항목이 있을 경우 명시해야 할 내용을 포함합니다. 사용자를 압도하지 않기 위해 전체 목록을 나열하고 싶지 않으므로, 처음 세 개의 `cart_items`를 나열합시다.

{% raw %}
```liquid
Hi {{${first_name} | default: 'there'}}, don't forget to complete your purchase! Your items {{custom_attribute.${cart_items[0]}}}, {{custom_attribute.${cart_items[1]}}}, {{custom_attribute.${cart_items[2]}}}, and others are waiting for you.
```
{% endraw %}

{: start="4"}
4\. 이전 조건이 충족되지 않을 경우(즉, `cart_items`가 비어 있거나 세 개 미만인 경우) 발생해야 할 일을 지정하기 위해 `else` 태그를 사용하고, 보낼 메시지를 제공합니다. 세 개의 항목은 많은 공간을 차지하지 않기 때문에, 우리는 모두 나열할 수 있습니다. 우리는 Liquid 연산자 `join`와 `,`를 사용하여 항목이 쉼표로 구분되어 나열되도록 지정할 것입니다. 논리를 `endif`로 닫습니다.

{% raw %}
```liquid
{% else %}
Hi {{${first_name} | default: 'there'}}, don't forget to complete your purchase! Your items: {{{custom_attribute.${cart_items}}} | join: ', '}  are waiting for you. 
{% endif %}
```
{% endraw %}

{: start="5"}
5\. `else`를 사용한 다음 `abort_message`를 사용하여 장바구니가 이전 조건을 충족하지 않을 경우 메시지를 보내지 않도록 Liquid 코드에 지시합니다. 다시 말해, 장바구니가 비어 있는 경우입니다. 논리를 `endif`로 닫습니다.

{% raw %}
```liquid
{% else %}
{% abort_message('No items in cart') %}
{% endif %}
```
{% endraw %}

{% details Full Liquid code %}
{% raw %}
```liquid
{% if {{custom_attribute.${cart_items}}} != blank %}
{% if {{custom_attribute.${cart_items}}} | size > 3 %}
Hi {{${first_name} | default: 'there'}}, don't forget to complete your purchase! Your items {{custom_attribute.${cart_items[0]}}}, {{custom_attribute.${cart_items[1]}}}, {{custom_attribute.${cart_items[2]}}}, and others are waiting for you.
{% else %}
Hi {{${first_name} | default: 'there'}}, don't forget to complete your purchase! Your items: {{{custom_attribute.${cart_items}}} | join: ', '}  are waiting for you.
{% endif %}
{% else %}
{% abort_message('No items in cart') %}
{% endif %}
```
{% endraw %}
{% enddetails %}

## 이벤트 카운트다운 {#countdown}

기념일 세일까지 남은 일수를 사용자에게 알리는 메시지를 보내겠습니다. 이를 위해 변수들을 사용하여 속성 값들을 조작하는 방정식을 만들겠습니다.

1. 먼저, 변수 `sale_date`을 사용자 정의 속성 `anniversary_date`에 할당하고 `date: "s"` 필터를 적용하겠습니다. 이것은 `anniversary_date`를 초 단위로 표현된 타임스탬프 형식으로 변환한 후, 그 값을 `sale_date`에 할당합니다.

{% raw %}
```liquid
{% assign sale_date = {{custom_attribute.${anniversary_date}}} | date: "%s" %}
```
{% endraw %}

{: start="2"}
2\. 오늘의 타임스탬프를 캡처할 변수를 할당해야 합니다. 변수 `today`를 `now` (현재 날짜 및 시간)에 할당한 후, `date: "%s"` 필터를 적용하겠습니다.

{% raw %}
```liquid
{% assign today =  'now' | date: "%s"  %}
```
{% endraw %}

{: start="3"}
3\. 이제 현재 (`today`)와 기념일 세일 (`sale_date`) 사이의 초 수를 계산해 보겠습니다. 이를 위해 변수 `difference`를 `sale_date`에서 `today`을 뺀 값으로 설정합니다.

{% raw %}
```liquid
{% assign difference =  event_date | minus: today %}
```
{% endraw %}

{: start="4"}
4\. 이제 `difference`를 메시지에서 참조할 수 있는 값으로 변환해야 합니다. 세일까지 남은 초 수를 사용자에게 알려주는 것은 이상적이지 않습니다. 변수 `difference_days`을 `event_date`에 할당하고 `86400`로 나누어 일 수를 구하겠습니다.

{% raw %}
```liquid
{% assign difference_days = difference | divided_by: 86400 %}
```
{% endraw %}

{: start="5"}
5\. 마지막으로, 보낼 메시지를 생성하겠습니다.

{% raw %}
```liquid
Get ready! Our Anniversary Sale is in {{ difference_days }} days!
```
{% endraw %}

{% details Full Liquid code %}
{% raw %}
```liquid
{% assign sale_date = {{custom_attribute.${anniversary_date}}} | date: "%s" %}
{% assign today =  'now' | date: "%s"  %}
{% assign difference =  event_date | minus: today %}
{% assign difference_days = difference | divided_by: 86400 %}
Get ready! Our Anniversary Sale is in {{ difference_days }} days!
```
{% endraw %}
{% enddetails %}

## 월별 생일 메시지 {#birthday}

오늘의 월에 생일이 있는 모든 사용자에게 특별 프로모션을 보내겠습니다. 이번 달에 생일이 없는 사용자에게는 메시지가 전송되지 않습니다.

1. 먼저, 오늘의 월을 가져오겠습니다. 변수 `this_month`을 `now` (현재 날짜 및 시간)에 할당한 후, `date: "%B"` 필터를 사용하여 변수가 월과 같도록 지정하겠습니다.

{% raw %}
```liquid
{% assign this_month = 'now' | date: "%B" %}
```
{% endraw %}

{: start="2"}
2\. 이제 사용자의 `date_of_birth`에서 생일 월을 가져오겠습니다. 변수 `birth_month`을 `date_of_birth`에 할당한 후, `date: "%B"` 필터를 사용하겠습니다.

{% raw %}
```liquid
{% assign birth_month = {{${date_of_birth}}} | date: "%B" %}
```
{% endraw %}

{: start="3"}
3\. 이제 두 개의 변수가 값으로 월을 가지고 있으므로 조건 논리로 비교할 수 있습니다. 조건을 사용자의 `birth_month`와 `date_of_birth`가 같도록 설정합시다.

{% raw %}
```liquid
{% if {{this_month}} == {{birth_month}} %}
```
{% endraw %}

{: start="4"}
4\. 이번 달이 사용자의 생일 달이라면 보낼 메시지를 만들어 봅시다.

{% raw %}
```liquid
We heard {{this_month}} is a special month! Enjoy a 50% discount on your purchase with code BIRTHDAY50 until the end of {{this_month}}.
```
{% endraw %}

{: start="5"}
5\. 조건이 충족되지 않을 경우(이번 달이 사용자의 생일 달이 아니기 때문에) 발생하는 일을 지정하기 위해 `else` 태그를 사용하세요.

{% raw %}
```liquid
{% else %} 
```
{% endraw %}

{: start="6"}
6\. 사용자의 생일 달이 이번 달이 아닐 경우 메시지를 보내고 싶지 않으므로, `abort_message`를 사용하여 메시지를 취소한 다음 `endif`으로 조건 논리를 닫습니다.

{% raw %}
```liquid
{% abort_message("Not their birthday month") %}
{% endif %}
```
{% endraw %}

{% details Full Liquid code %}
{% raw %}
```liquid
{% assign this_month = 'now' | date: "%B" %}
{% assign birth_month = {{${date_of_birth}}} | date: "%B" %}
{% if {{this_month}} == {{birth_month}} %}
We heard {{this_month}} is a special month! Enjoy a 50% discount on your purchase with code BIRTHDAY50 until the end of {{this_month}}.
{% else %} 
{% abort_message("Not their birthday month") %}
{% endif %}
```
{% endraw %}
{% enddetails %}

## 좋아하는 제품 프로모션 {#favorite-product}

사용자의 마지막 구매 날짜가 6개월 이상 지났다면 사용자의 좋아하는 제품을 홍보합시다.

1. 먼저, 사용자의 좋아하는 제품과 마지막 구매 날짜가 있는지 조건 논리를 사용하여 확인합니다.

{% raw %}
```liquid
{% if {{custom_attribute.${favorite_product}}} == blank or {{custom_attribute.${last_purchase_date}}} == blank %}
```
{% endraw %}

{: start="2"}
2\. 그런 다음 사용자의 좋아하는 제품이나 마지막 구매 날짜가 없으면 메시지를 보내지 않도록 명시합니다.

{% raw %}
```liquid
{% abort_message("No favorite product or last purchase date") %}
```
{% endraw %}

{: start="3"}
3\. 위의 조건이 충족되지 않을 경우(우리가 _가지고_ 있는 사용자의 좋아하는 제품과 마지막 구매 날짜가 있기 때문에) 발생해야 할 일을 지정하기 위해 `else`를 사용합니다.

{% raw %}
```liquid
{% else %}
```
{% endraw %}

{: start="4"}
4\. 구매 날짜가 있다면, 오늘 날짜와 비교할 수 있도록 변수를 할당해야 합니다. 먼저, 변수 `today`를 `now` (현재 날짜 및 시간)으로 할당하여 오늘 날짜의 값을 만들고, `date: "%s"` 필터를 사용하여 값을 초 단위의 타임스탬프 형식으로 변환합니다. 타임스탬프에 "0"을 추가하기 위해 `plus: 0` 필터를 추가합니다. 이것은 타임스탬프의 값을 변경하지 않지만, 향후 방정식에서 타임스탬프를 사용하는 데 유용합니다.


{% raw %}
```liquid
{% assign today = 'now' | date: "%s" | plus: 0 %}
```
{% endraw %}

{: start="5"}
5\. 이제 변수를 `last_purchase_date`로 할당하여 마지막 구매 날짜를 초 단위로 캡처하고 `date: "s"` 필터를 사용합니다. 다시 `plus: 0` 필터를 추가합니다.

{% raw %}
```liquid
{% assign last_purchase_date = {{custom_attribute.${last_purchase_date}}} | date: "%s" | plus: 0 %}
```
{% endraw %}

{: start="6"}
6\. 마지막 구매 날짜와 오늘 날짜가 초 단위이므로, 6개월이 몇 초인지 계산해야 합니다. 방정식을 만들어 봅시다(약 6개월 * 30.44일 * 24시간 * 60분 * 60초) 그리고 이를 변수 `six_months`에 할당합니다. 시간 단위의 곱셈을 지정하기 위해 `times`을 사용합니다.

{% raw %}
```liquid
{% assign six_months = 6 | times: 30.44 | times: 24 | times: 60 | times: 60 %}
```
{% endraw %}

{: start="7"}
7\. 이제 모든 시간 값이 초 단위로 되어 있으므로, 우리는 그 값을 방정식에 사용할 수 있습니다. 오늘의 값을 가져와서 `last_purchase_date`을 빼는 `today_minus_last_purchase_date`라는 변수를 할당해 보겠습니다. 이것은 마지막 구매 이후로 얼마나 많은 초가 지났는지를 알려줍니다.

{% raw %}
```liquid
{% assign today_minus_last_purchase_date = {{today | minus: last_purchase_date}} %}
```
{% endraw %}

{: start="8"}
8\. 이제 조건 논리에서 우리의 시간 값을 직접 비교해 보겠습니다. 조건을 `today_minus_last_purchase_date`가 여섯 개월 이상 (`>=`)인 것으로 정의해 보겠습니다. 다시 말해, 마지막 구매 날짜는 최소한 여섯 개월 전이었습니다.

{% raw %}
```liquid
{% if today_minus_last_purchase_date >= six_months %}
```
{% endraw %}

{: start="9"}
9\. 마지막 구매가 최소한 여섯 개월 전이었다면 보낼 메시지를 만들어 보겠습니다.

{% raw %}
```liquid
We noticed it’s been a while since you last purchased {{custom_attribute.${favorite_product}}}. Have you checked out our latest offerings?
```
{% endraw %}

{: start="10"}
10\. 조건이 충족되지 않을 경우(구매가 최소한 여섯 개월 전이 아니었기 때문에) 어떤 일이 일어날지를 지정하기 위해 `else` 태그를 사용할 것입니다.

{% raw %}
```liquid
{% else %}
```
{% endraw %}

{: start="11"}
11\. 메시지를 취소하기 위해 `abort_message`를 포함할 것입니다.

{% raw %}
```liquid
{% abort_message("No favorite product or last purchase date") %}
```
{% endraw %}

{: start="12"}
12\. 마무리하기 위해, 두 개의 `endif` 태그로 Liquid를 끝낼 것입니다. 첫 번째 `endif`는 좋아하는 제품 또는 마지막 구매 날짜에 대한 조건 검사를 닫고, 두 번째 `endif`는 마지막 구매 날짜가 최소한 여섯 개월 전이라는 조건 검사를 닫습니다.

{% raw %}
```liquid
{% endif %}
{% endif %}
```
{% endraw %}

{% details Full Liquid code %}
{% raw %}
```liquid
{% if {{custom_attribute.${favorite_product}}} == blank or {{custom_attribute.${last_purchase_date}}} == blank %}
{% abort_message("No favorite product or last purchase date") %}
{% else %}
{% assign today = 'now' | date: "%s" | plus: 0 %}
{% assign last_purchase_date = {{custom_attribute.${last_purchase_date}}} | date: "%s" | plus: 0 %}
{% assign six_months = 6 | times: 30.44 | times: 24 | times: 60 | times: 60 %}
{% assign today_minus_last_purchase_date = {{today | minus: last_purchase_date}} %}
{% if today_minus_last_purchase_date >= six_months %}
We noticed it’s been a while since you last purchased {{custom_attribute.${favorite_product}}}. Have you checked out our latest offerings?
{% else %}
{% abort_message("Last purchase was less than six months ago") %}
{% endif %}
{% endif %}
```
{% endraw %}
{% enddetails %}
