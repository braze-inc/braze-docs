---
nav_title: 튜토리얼
article_title: "자습서: Writing Liquid 코드"
page_order: 11
description: "이 참조 페이지에는 Liquid 코드로 시작하는 데 도움이 되는 초보자 친화적인 튜토리얼이 포함되어 있습니다."
page_type: tutorial
---

# 자습서: Writing Liquid 코드

> New to Liquid? 이 튜토리얼은 초보자 친화적인 사용 사례를 위해 Liquid 코드를 작성하는 데 도움이 될 것입니다. 각 튜토리얼은 조건 로직 및 연산자와 같은 학습 목표의 다양한 조합을 다룹니다.

이 튜토리얼을 마치면 다음을 할 수 있습니다:

- 일반적인 사용 사례를 위한 Liquid 코드 작성
- 문자열과 액체 조건 로직을 결합하여 사용자 데이터에 기반한 메시지를 개인화합니다.
- 속성의 값을 사용하는 방정식을 작성하기 위해 변수와 필터를 사용하십시오.
- Liquid 코드의 기본 명령을 인식하고 코드가 무엇을 하는지에 대한 일반적인 이해 형성하기

| 튜토리얼 | 학습 목표 |
| --- | --- |
| [사용자 세그먼트에 맞게 메시지를 개인화하세요.](#segments) | 기본값, 조건 로직 |
| [유기한 장바구니 알림](#reminders) | 연산자, 조건 로직 |
| [이벤트 카운트다운](#countdown) | 변수, 날짜 필터 |
| [월간 생일 메시지](#birthday) | 변수, 날짜 필터, 연산자 |
| [좋아하는 제품을 홍보하다](#favorite-product) | 변수, 날짜 필터, 방정식, 연산자 |
{: .reset-br-td-1 .reset-br-td-2}

## 사용자 세그먼트에 대한 개인화된 메시지 {#segments}

다양한 사용자 세그먼트, 예를 들어 VIP 고객과 신규 구독자를 위한 메시지를 맞춤 설정해 보겠습니다.

1. 사용자의 이름이 있을 때와 없을 때 보내는 개인화된 인사말로 메시지를 열어보세요. 이 작업을 수행하려면, 속성 `first_name`을 포함하고 `first_name`가 비어 있을 경우 사용할 기본값을 포함하는 Liquid 태그를 생성하십시오. 이 시나리오에서는 "여행자"를 기본값으로 사용합시다.

{% raw %}
```liquid
Happy summer, {{${first_name} | default: "traveler"}}!
```
{% endraw %}

{: start="2"}
2\. 이제 사용자가 VIP 고객인 경우 보낼 메시지를 제공합시다. 이것을 위해 조건 로직 태그를 사용해야 합니다: `if`. 이 태그는 `vip_status` 커스텀 속성이 `VIP`와 같으면 다음 Liquid가 실행된다고 말합니다. 이 경우, 특정 메시지가 전송됩니다.

{% raw %}
```liquid
{% if {{custom_attribute.${vip_status}}} == 'VIP' %}
Thank you for being a VIP customer! Enjoy your exclusive discount code: VIPSUMMR464.
```
{% endraw %}

{: start="3"}
3\. 새로운 구독자인 사용자에게 맞춤형 메시지를 보내봅시다. 우리는 조건 로직 태그 `elsif`를 사용하여 사용자의 `vip_status`가 `new`일 경우 다음 메시지가 전송되도록 지정할 것입니다.

{% raw %}
```liquid
{% elsif {{custom_attribute.${vip_status}}} == 'new' %}
Thank you for subscribing! Enjoy your welcome discount code: NEWTRAVEL257.
```
{% endraw %}

{: start="4"}
4\. VIP가 아니거나 새로운 사용자는 어떻게 되나요? 우리는 `else` 태그가 있는 모든 다른 사용자에게 메시지를 보낼 수 있으며, 이는 이전 조건이 충족되지 않을 경우 다음 메시지를 보내야 함을 지정합니다. 그럼 `endif` 태그로 조건 로직을 닫을 수 있습니다. 더 이상 고려할 VIP 상태가 없습니다.

{% raw %}
```liquid
{% else %}
Thanks for traveling with us! Enjoy your unique discount code: SUMMRTRVLS240.
{% endif %}
```
{% endraw %}

{% details 전체 액체 코드 %}
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

## 유기한 장바구니 알림 {#reminders}

장바구니에 남겨진 항목을 사용자에게 상기시키기 위해 개인화된 메시지를 보내자. 장바구니에 있는 항목 수에 따라 추가로 맞춤 설정하여, 항목이 세 개 이하인 경우 모든 항목을 나열합니다. 세 개 이상의 항목이 있는 경우, 더 간결한 메시지를 보낼 것입니다.

1. 사용자의 장바구니가 비어 있는지 확인하기 위해 연산자 `!=`와 함께 Liquid 조건 로직을 열어보겠습니다. 이는 "같지 않다"는 의미입니다. 이 경우, 우리는 조건을 커스텀 속성 `cart_items`이(가) 빈 값과 같지 않도록 설정할 것입니다.

{% raw %}
```liquid
{% if {{custom_attribute.${cart_items}}} != blank %}
```
{% endraw %}

{: start="2"}
2\. 그런 다음 우리는 초점을 좁히고 장바구니에 세 개 이상의 항목이 있는지 확인해야 합니다. 이를 위해 \`>\` 연산자를 사용합니다. 이는 "보다 큼"을 의미합니다.

{% raw %}
```liquid
{% if {{custom_attribute.${cart_items}}} | size > 3 %}
```
{% endraw %}

{: start="3"}
3\. 사용자의 이름으로 인사하는 메시지를 작성하세요. 이름이 없으면 "거기"를 기본값으로 사용하세요. 장바구니에 3개 이상의 항목이 있는 경우 명시해야 할 내용을 포함하세요. 사용자에게 전체 목록으로 압도하고 싶지 않기 때문에 처음 세 개 `cart_items`를 나열합시다.

{% raw %}
```liquid
Hi {{${first_name} | default: 'there'}}, don't forget to complete your purchase! Your items {{custom_attribute.${cart_items[0]}}}, {{custom_attribute.${cart_items[1]}}}, {{custom_attribute.${cart_items[2]}}}, and others are waiting for you.
```
{% endraw %}

{: start="4"}
4\. 이전 조건이 충족되지 않을 경우(즉, `cart_items`이 비어 있거나 세 개 미만인 경우) `else` 태그를 사용하여 어떤 일이 발생해야 하는지 지정한 다음, 전송할 메시지를 제공하십시오. 세 개의 항목이 많은 공간을 차지하지 않기 때문에, 우리는 그것들을 모두 나열할 수 있습니다. 우리는 Liquid 연산자 `join` 및 `,`를 사용하여 항목이 쉼표로 구분되어 나열되어야 함을 지정할 것입니다. 논리를 `endif`로 닫습니다.

{% raw %}
```liquid
{% else %}
Hi {{${first_name} | default: 'there'}}, don't forget to complete your purchase! Your items: {{{custom_attribute.${cart_items}}} | join: ', '}  are waiting for you. 
{% endif %}
```
{% endraw %}

{: start="5"}
5\. `else`를 사용한 다음 `abort_message`을(를) 사용하여 Liquid 코드가 장바구니가 이전 조건을 충족하지 않을 경우 메시지를 보내지 않도록 합니다. 장바구니가 비어 있다면. 논리를 `endif`로 닫습니다.

{% raw %}
```liquid
{% else %}
{% abort_message('No items in cart') %}
{% endif %}
```
{% endraw %}

{% details 전체 액체 코드 %}
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

기념일 세일까지 남은 일수를 사용자에게 알리는 메시지를 보내자. 이 작업을 수행하기 위해 우리는 변수를 사용하여 속성 값의 조작을 위한 방정식을 만들 수 있습니다.

1. 먼저, 변수 `sale_date`를 커스텀 속성 `anniversary_date`에 할당하고 `date: "s"` 필터를 적용합시다. 이것은 `anniversary_date`를 초로 표현된 타임스탬프 형식으로 변환한 다음, 해당 값을 `sale_date`에 할당합니다.

{% raw %}
```liquid
{% assign sale_date = {{custom_attribute.${anniversary_date}}} | date: "%s" %}
```
{% endraw %}

{: start="2"}
2\. 오늘의 타임스탬프를 캡처할 변수를 할당해야 합니다. 변수 `today`를 `now` (현재 날짜와 시간)으로 할당한 다음, `date: "%s"` 필터를 적용합시다.

{% raw %}
```liquid
{% assign today =  'now' | date: "%s"  %}
```
{% endraw %}

{: start="3"}
3\. 이제 지금 (`today`)과 기념일 세일 (`sale_date`) 사이에 몇 초가 있는지 계산해 봅시다. 이 작업을 수행하려면 변수 `difference`에 `sale_date`에서 `today`을(를) 뺀 값을 할당합니다.

{% raw %}
```liquid
{% assign difference =  event_date | minus: today %}
```
{% endraw %}

{: start="4"}
4\. 이제 `difference`를 메시지에서 참조할 수 있는 값으로 변환해야 합니다. 판매까지 몇 초가 남았는지 사용자에게 알려주는 것은 이상적이지 않습니다. `difference_days`를 `event_date`에 할당하고 `86400`로 나누어 일 수를 구해봅시다.

{% raw %}
```liquid
{% assign difference_days = difference | divided_by: 86400 %}
```
{% endraw %}

{: start="5"}
5\. 마지막으로, 보낼 메시지를 만들어 봅시다.

{% raw %}
```liquid
Get ready! Our Anniversary Sale is in {{ difference_days }} days!
```
{% endraw %}

{% details 전체 액체 코드 %}
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

## 매월 생일 메시지 {#birthday}

오늘 생일인 모든 사용자에게 특별 프로모션을 보내자. 이번 달 생일이 없는 사용자에게는 메시지가 전송되지 않습니다.

1. 먼저, 오늘의 월을 뽑아봅시다. 우리는 변수 `this_month`를 `now` (현재 날짜와 시간)로 할당한 다음, `date: "%B"` 필터를 사용하여 변수가 월과 같아야 함을 지정합니다.

{% raw %}
```liquid
{% assign this_month = 'now' | date: "%B" %}
```
{% endraw %}

{: start="2"}
2\. 이제 사용자의 `date_of_birth`에서 생월을 가져옵시다. 우리는 변수 `birth_month`를 `date_of_birth`에 할당한 다음 `date: "%B"` 필터를 사용할 것입니다.

{% raw %}
```liquid
{% assign birth_month = {{${date_of_birth}}} | date: "%B" %}
```
{% endraw %}

{: start="3"}
3\. 이제 두 개의 변수가 값으로 월을 가지고 있으므로, 조건 로직을 사용하여 비교할 수 있습니다. 사용자의 `birth_month`와 같도록 조건을 `date_of_birth`로 설정합시다.

{% raw %}
```liquid
{% if {{this_month}} == {{birth_month}} %}
```
{% endraw %}

{: start="4"}
4\. 사용자의 생일이 이 달인 경우에 보낼 메시지를 만들어 봅시다.

{% raw %}
```liquid
We heard {{this_month}} is a special month! Enjoy a 50% discount on your purchase with code BIRTHDAY50 until the end of {{this_month}}.
```
{% endraw %}

{: start="5"}
5\. 조건이 충족되지 않을 경우(이번 달이 사용자의 생일 달이 아니기 때문에) `else` 태그를 사용하여 발생하는 일을 지정하십시오.

{% raw %}
```liquid
{% else %} 
```
{% endraw %}

{: start="6"}
6\. 사용자의 생일이 이 달이 아닐 경우 메시지를 보내고 싶지 않으므로, `abort_message`를 사용하여 메시지를 취소한 다음 `endif`으로 조건 로직을 닫겠습니다.

{% raw %}
```liquid
{% abort_message("Not their birthday month") %}
{% endif %}
```
{% endraw %}

{% details 전체 액체 코드 %}
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

사용자의 마지막 구매 날짜가 6개월 이상 지났다면 사용자가 좋아하는 제품을 홍보합시다.

1. 먼저, 우리는 조건 로직을 사용하여 사용자의 좋아하는 제품과 마지막 구매 날짜가 있는지 확인할 것입니다.

{% raw %}
```liquid
{% if {{custom_attribute.${favorite_product}}} == blank or {{custom_attribute.${last_purchase_date}}} == blank %}
```
{% endraw %}

{: start="2"}
2\. 그렇다면 사용자의 좋아하는 제품이나 마지막 구매 날짜가 없으면 메시지를 보내지 않도록 하겠습니다.

{% raw %}
```liquid
{% abort_message("No favorite product or last purchase date") %}
```
{% endraw %}

{: start="3"}
3\. 우리는 `else`를 사용하여 위의 조건이 충족되지 않을 경우 어떤 일이 발생해야 하는지 지정합니다 (왜냐하면 우리는 _하고_ 사용자의 좋아하는 제품과 마지막 구매 날짜를 가지고 있습니다).

{% raw %}
```liquid
{% else %}
```
{% endraw %}

{: start="4"}
4\. 구매 날짜가 있다면, 이를 변수에 할당하여 오늘 날짜와 비교할 수 있어야 합니다. 먼저, 변수 `today`를 `now` (현재 날짜 및 시간)에 할당하여 오늘 날짜의 값을 생성하고 `date: "%s"` 필터를 사용하여 값을 초 단위로 표현된 타임스탬프 형식으로 변환합시다. 우리는 `plus: 0` 필터를 추가하여 타임스탬프에 "0"을 추가할 것입니다. 이것은 타임스탬프의 값을 변경하지 않지만, 미래의 방정식에서 타임스탬프를 사용하는 데 유용합니다.


{% raw %}
```liquid
{% assign today = 'now' | date: "%s" | plus: 0 %}
```
{% endraw %}

{: start="5"}
5\. 이제 변수를 `last_purchase_date`를 커스텀 속성 `last_purchase_date`에 할당하고 `date: "s"` 필터를 사용하여 마지막 구매 날짜를 초 단위로 캡처해 보겠습니다. 우리는 다시 `plus: 0` 필터를 추가할 것입니다.

{% raw %}
```liquid
{% assign last_purchase_date = {{custom_attribute.${last_purchase_date}}} | date: "%s" | plus: 0 %}
```
{% endraw %}

{: start="6"}
6\. 마지막 구매 날짜와 오늘 날짜가 초 단위이므로, 6개월이 몇 초인지 계산해야 합니다. 우리가 방정식을 만들어 보자 (대략 6개월 * 30.44일 * 24시간 * 60분 * 60초) 그리고 그것을 변수 `six_months`에 할당하자. 우리는 `times`을 사용하여 시간 단위의 곱셈을 지정할 것입니다.

{% raw %}
```liquid
{% assign six_months = 6 | times: 30.44 | times: 24 | times: 60 | times: 60 %}
```
{% endraw %}

{: start="7"}
7\. 이제 모든 시간 값이 초로 변환되었으므로, 우리는 방정식에서 그 값을 사용할 수 있습니다. 오늘의 값을 가져와서 `last_purchase_date`을(를) 빼는 `today_minus_last_purchase_date`라는 변수를 할당합시다. 이것은 마지막 구매 이후로 얼마나 많은 초가 지났는지를 알려줍니다.

{% raw %}
```liquid
{% assign today_minus_last_purchase_date = {{today | minus: last_purchase_date}} %}
```
{% endraw %}

{: start="8"}
8\. 이제 조건 로직에서 우리의 시간 값을 직접 비교해 봅시다. 조건을 `today_minus_last_purchase_date`가 여섯 달 이상 (`>=`)인 것으로 정의합시다. 다시 말해, 마지막 구매 날짜는 최소 6개월 전이었습니다.

{% raw %}
```liquid
{% if today_minus_last_purchase_date >= six_months %}
```
{% endraw %}

{: start="9"}
9\. 마지막 구매가 최소 6개월 전이었다면 보낼 메시지를 만들어 봅시다.

{% raw %}
```liquid
We noticed it’s been a while since you last purchased {{custom_attribute.${favorite_product}}}. Have you checked out our latest offerings?
```
{% endraw %}

{: start="10"}
10\. 우리는 `else` 태그를 사용하여 조건이 충족되지 않을 경우(구매가 최소 6개월 전이 아니기 때문에) 어떤 일이 발생해야 하는지를 지정할 것입니다.

{% raw %}
```liquid
{% else %}
```
{% endraw %}

{: start="11"}
11\. 우리는 메시지를 취소하기 위해 `abort_message`를 포함할 것입니다.

{% raw %}
```liquid
{% abort_message("No favorite product or last purchase date") %}
```
{% endraw %}

{: start="12"}
12\. 마무리하자면, 우리는 두 개의 `endif` 태그로 Liquid를 끝낼 것입니다. 첫 번째 `endif`는 즐겨 찾는 제품 또는 마지막 구매 날짜에 대한 조건 검사를 종료하고, 두 번째 `endif`는 마지막 구매 날짜가 최소 6개월 전임을 확인하는 조건 검사를 종료합니다.

{% raw %}
```liquid
{% endif %}
{% endif %}
```
{% endraw %}

{% details 전체 액체 코드 %}
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
