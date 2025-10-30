---
nav_title: 액체 사용 사례 라이브러리
article_title: 액체 사용 사례 라이브러리
page_order: 10
search_rank: 2
excerpt_separator: ""
page_type: glossary
layout: liquid_use_case_glossary
description: "이 랜딩 페이지는 기념일, 앱 사용, 카운트다운 등과 같은 카테고리별로 정리된 샘플 액체 사용 사례의 홈입니다."

---

{% api %}

## 기념일 및 휴일

{% apitags %}
기념일 및 휴일
{% endapitags %}

- [사용자의 기념일 연도에 따라 메시지를 개인화합니다.](#anniversary-year)
- [사용자의 생일 주에 따라 메시지를 개인화합니다.](#birthday-week)
- [사용자의 생일 달에 캠페인을 보냅니다.](#birthday-month)
- [주요 휴일에 메시지를 보내지 않도록 합니다.](#holiday-avoid)

### 사용자의 기념일 연도에 따라 메시지를 개인화합니다. {#anniversary-year}

이 사용 사례는 사용자의 초기 가입 날짜를 기준으로 사용자의 앱 기념일을 계산하고, 그들이 축하하는 연도에 따라 다른 메시지를 표시하는 방법을 보여줍니다.

{% raw %}
```liquid
{% assign this_month = 'now' | date: "%B" %} 
{% assign this_day = 'now' | date: "%d" %}
{% assign anniversary_month = {{custom_attribute.${registration_date}}} | date: "%B" %}
{% assign anniversary_day = {{custom_attribute.${registration_date}}} | date: "%d" %}
{% assign anniversary_year = {{custom_attribute.${registration_date}}} | date: "%Y" %}

{% if this_month == anniversary_month %} 
{% if this_day == anniversary_day %} 
{% if anniversary_year == '2021' %}
Exactly one year ago today we met for the first time!

{% elsif anniversary_year == '2020' %}
Exactly two years ago today we met for the first time!

{% elsif anniversary_year == '2019' %}
Exactly three years ago today we met for the first time!

{% else %}
{% abort_message("Not same year") %}
{% endif %}

{% else %} 
{% abort_message("Not same day") %} 
{% endif %}

{% else %}
{% abort_message("Not same month") %}
{% endif %}
```
{% endraw %}

**설명:** 여기서는 예약된 변수 `now`를 사용하여 현재 날짜와 시간을 [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601) 형식으로 템플릿합니다. 필터 `%B` (월이 "5월"과 같은) 및 `%d` (일이 "18일"과 같은)는 현재 월과 일을 형식화합니다. 그런 다음 동일한 날짜 및 시간 필터를 `signup_date` 값에 적용하여 조건 태그 및 논리를 사용하여 두 값을 비교할 수 있도록 합니다.

그런 다음 `signup_date`에 대한 `%B` 및 `%d`를 얻기 위해 세 개의 변수 문을 더 반복하지만 `%Y` (연도가 "2021년"과 같은)를 추가합니다. 이것은 `signup_date`의 날짜와 시간을 단지 연도로 형성합니다. 일과 월을 알면 사용자의 기념일이 오늘인지 확인할 수 있고, 연도를 알면 몇 년이 지났는지 알 수 있습니다. 이는 그들에게 축하해야 할 몇 년인지 알 수 있게 해줍니다!

{% alert tip %} 가입 날짜를 수집한 연도만큼 많은 조건을 만들 수 있습니다. {% endalert %}  

### 사용자의 생일 주 {#birthday-week}에 따라 메시지를 개인화합니다.

이 사용 사례는 사용자의 생일을 찾고, 현재 날짜와 비교한 다음, 생일 주 전후에 특별한 생일 메시지를 표시하는 방법을 보여줍니다.

{% raw %}
```liquid
{% assign this_week = 'now' | date: '%W' %}
{% assign birthday_week = ${date_of_birth}  | date: '%W' %}
{% assign last_week = {{this_week}} | minus: 1 %}
{% assign next_week = {{this_week}} | plus: 1 %}
{% assign birthday_week_conversion = {{birthday_week}} | plus: 0 %}
{% if {{last_week}} == {{birthday_week_conversion}} %}
Happy birthday for last week!
{% elsif {{birthday_week}} == {{this_week}} %}
Happy birthday for this week!
{% elsif {{next_week}} == {{birthday_week_conversion}} %}
Happy birthday for next week!
{% else %}
No birthday for you!
{% endif %}
```
{% endraw %}

**설명:** [기념일 연도](#anniversary-year) 사용 사례와 유사하게, 여기서는 예약된 변수 `now`를 가져와서 `%W` 필터(1년 중 52주 중 12주와 같은 주)를 사용하여 사용자의 생일이 포함된 주의 주 번호를 가져옵니다. 사용자의 생일 주가 현재 주와 일치하면, 우리는 그들에게 축하 메시지를 보냅니다! 

우리는 또한 `last_week` 및 `next_week`에 대한 문구를 포함하여 메시지를 더욱 개인화합니다.

### 사용자의 생일 월 {#birthday-month}에 캠페인을 보냅니다.

이 사용 사례는 사용자의 생일 월을 계산하고, 생일이 현재 월에 해당하는지 확인한 다음, 그렇다면 특별한 메시지를 보내는 방법을 보여줍니다.

{% raw %}
```liquid
{% assign this_month = 'now' | date: "%B" %}
{% assign birth_month = {{${date_of_birth}}} | date: "%B" %}
{% if {{this_month}} == {{birth_month}} %}
Message body 
{% else %} 
{% abort_message("Not their birthday month") %}
{% endif %}
```
{% endraw %}

**설명:** [생일 주](#birthday-week) 사용 사례와 유사하지만, 여기서는 `%B` 필터("5월"과 같은 월)를 사용하여 이번 달에 생일이 있는 사용자를 계산합니다. 잠재적인 응용 프로그램은 월간 이메일에서 생일 사용자에게 다가가는 것입니다.

### 주요 공휴일 {#holiday-avoid}에 메시지 전송을 피하십시오.

이 사용 사례는 참여도가 낮을 가능성이 있는 주요 공휴일의 날을 피하면서 휴일 기간 동안 메시지를 보내는 방법을 보여줍니다.

{% raw %}
```liquid
{% assign today = 'now' | date: '%Y-%m-%d' %}
{% if today == "2023-12-24" or today == "2023-12-25" or today == "2023-12-26" %}
{% abort_message %}
{% else %}
Message if today isn't one of the provided holidays.
{% endif %}
```
{% endraw %}

**설명:** 여기서는 용어 `today`를 예약된 변수 `now`(현재 날짜 및 시간)에 할당하고, 필터 `%Y`("2023"과 같은 연도), `%m`("12"와 같은 월), `%d`("25"와 같은 일)를 사용하여 날짜를 형식화합니다. 그런 다음 변수 `today`가 선택한 공휴일과 일치하면 메시지가 중단된다고 말하는 조건문을 실행합니다. 

제공된 예시는 크리스마스 이브, 크리스마스 날, 그리고 박싱 데이(크리스마스 다음 날)를 사용합니다.

{% endapi %}

{% api %}

## 앱 사용

{% apitags %}
앱 사용
{% endapitags %}

- [사용자가 세션을 기록한 경우 사용자의 언어로 메시지를 보냅니다.](#app-session-language)
- [사용자가 마지막으로 앱을 열었던 시간에 따라 메시지를 개인화합니다.](#app-last-opened)
- [사용자가 마지막으로 앱을 사용한 지 3일이 채 안 된 경우 다른 메시지를 표시합니다.](#app-last-opened-less-than)

### 사용자가 세션을 기록하지 않은 경우 사용자의 언어로 메시지를 보냅니다 {#app-session-language}.

이 사용 사례는 사용자가 세션을 기록했는지 확인하고, 그렇지 않은 경우 수집된 사용자 정의 속성을 통해 수동으로 수집된 언어에 따라 메시지를 표시하는 논리를 포함합니다. 계정에 연결된 언어 정보가 없으면 기본 언어로 메시지가 표시됩니다. 사용자가 세션에 로그인한 경우, 사용자와 연결된 언어 정보를 가져와 적절한 메시지를 표시합니다. 

{% raw %}
```liquid
{% if {{${last_used_app_date}}} == nil %}
{% if {{custom_attribute.${user_language}}} == 'en' %}
Message in English based on custom attribute
{% elsif {{custom_attribute.${user_language}}} == 'fr' %}
Message in French based on custom attribute
{% else %}
Does not have language - Default language
{% endif %}
{% else %}
{% if ${language} == 'en' %}
Message in English based on Language
{% elsif ${language} == 'fr' %}
Message in French based on Language
{% else %}
Has language - Default language
{% endif %}
{% endif %}
```
{% endraw %}

{% raw %}
**설명:** 여기서는 두 개의 그룹화된 `if` 문장을 중첩하여 사용하고 있습니다. 첫 번째 `if` 문장은 사용자가 `last_used_app_date`가 `nil`인지 확인하여 세션을 시작했는지 확인합니다. 이는 사용자가 세션에 로그인할 때 SDK에 의해 `{{${language}}}`가 자동으로 수집되기 때문입니다. 사용자가 세션에 로그인하지 않은 경우, 언어 정보를 아직 갖고 있지 않으므로, 저장된 언어 관련 사용자 정의 속성이 있는지 확인하고, 그 정보를 바탕으로 가능한 경우 해당 언어로 메시지를 표시합니다.
{% endraw %}

두 번째 `if` 문장은 사용자가 `last_used_app_date`에 대한 `nil`가 없기 때문에 표준(기본) 속성을 확인합니다. 이는 사용자가 세션에 로그인했음을 의미하며, 우리는 그들의 언어를 가지고 있습니다.

{% alert note %}
[`Nil`](https://shopify.github.io/liquid/basics/types/#nil)는 Liquid 코드에 결과가 없을 때 반환되는 예약 변수입니다. `Nil`는 `if` 블록에서 `false`로 처리됩니다.
{% endalert %}

### 사용자가 마지막으로 앱을 열었던 시점에 따라 메시지를 개인화합니다 {#app-last-opened}

이 사용 사례는 사용자가 앱을 마지막으로 열었던 시간을 계산하고, 시간의 길이에 따라 다른 개인화된 메시지를 표시합니다.

{% raw %}
```liquid
{% assign last_used_date = {{${last_used_app_date}} | date: "%s" %}
{% assign now = 'now' | date: "%s" %}
{% assign difference_in_days = {{now}} | minus: {{last_used_date}} | divided_by: 86400 %}
{% if {{difference_in_days}} < 3 %}
Happy to see you again!
{% else %}
It's been a while; here are some of our latest updates.
{% endif %}
```
{% endraw %}

### 사용자가 마지막으로 앱을 사용한 지 3일이 채 안 된 경우 다른 메시지를 표시합니다 {#app-last-opened-less-than}

이 사용 사례는 사용자가 앱을 사용한 지 얼마나 되었는지를 계산하고, 시간의 길이에 따라 다른 개인화된 메시지를 표시합니다.

{% raw %}
```liquid
{% assign last_used_date = {{${last_used_app_date}} | date: "%s" %}
{% assign now = 'now' | date: "%s" %}
{% assign difference_in_days = {{now}} | minus: {{last_used_date}} | divided_by: 86400 %}
{% if {{difference_in_days}} < 3 %}
Message for a recently active user
{% else %}
Message for a less active user
{% endif %}
```
{% endraw %}

{% endapi %}

{% api %}

## 카운트다운

{% apitags %}
카운트다운
{% endapitags %}

- [오늘 날짜에 X일 추가](#countdown-add-x-days)
- [특정 시점에서 카운트다운 계산](#countdown-difference-days)
- [특정 배송 날짜 및 우선 순위에 대한 카운트다운 생성](#countdown-shipping-options)
- [일 단위로 카운트다운 생성](#countdown-days)
- [일에서 시간, 시간에서 분으로 카운트다운 만들기](#countdown-dynamic)
- [특정 날짜까지 남은 일 수 표시하기](#countdown-future-date)
- [사용자 정의 날짜 속성이 도착할 때까지 남은 일 수 표시하기](#countdown-custom-date-attribute)
- [남은 시간을 표시하고, 남은 시간이 X 시간뿐일 경우 메시지를 중단하기](#countdown-abort-window)
- [사용자의 멤버십 종료 X일 전에 전송할 인앱 메시지](#countdown-membership-expiry)
- [사용자의 날짜와 언어에 따라 인앱 메시지 개인화하기](#countdown-personalize-language)
- [현재로부터 30일 후의 날짜를 월과 일 형식으로 템플릿화하기](#countdown-template-date)

### 오늘 날짜에 x일 추가하기 {#countdown-add-x-days}

이 사용 사례는 현재 날짜에 특정 일 수를 추가하여 메시지에 참조하고 추가합니다. 예를 들어, 주중에 주말의 지역 이벤트를 보여주는 메시지를 전송하고 싶을 수 있습니다.

{% raw %}
```liquid
Here are the movies we're showing on {{ "now" | date:'%s' | plus:259200 | date:"%F" }}!
```
{% endraw %}

`plus` 값은 항상 초 단위이므로, 초를 일로 변환하기 위해 필터 `%F`로 끝납니다.

{% alert important %}
메시지에 이벤트 목록으로의 URL 또는 딥 링크를 포함하여 사용자를 미래에 발생하는 행동 목록으로 보낼 수 있습니다.
{% endalert %}

### 특정 시점에서 카운트다운 계산하기 {#countdown-difference-days}

이 사용 사례는 특정 날짜와 현재 날짜 사이의 일 수 차이를 계산합니다. 이 차이는 사용자에게 카운트다운을 표시하는 데 사용될 수 있습니다.

{% raw %}
```liquid
{% assign event_date = '2023-12-31' | date: "%s" %}
{% assign today = 'now' | date: "%s" %}
{% assign difference = event_date | minus: today %}
{% assign difference_days = difference | divided_by: 86400 %}
you have {{ difference_days }} days left!
```
{% endraw %}

### 특정 배송 날짜와 우선 순위에 대한 카운트다운 만들기 {#countdown-shipping-options}

이 사용 사례는 다양한 배송 옵션을 캡처하고, 수령하는 데 걸리는 시간을 계산하며, 사용자가 특정 날짜까지 패키지를 받을 수 있도록 구매를 유도하는 메시지를 표시합니다.

{% raw %}
```liquid
{% assign standard_shipping_start = "2023-12-10T00:00-05:00" | date: "%s" %}
{% assign standard_shipping_end = "2023-12-20T13:00-05:00" | date: "%s" %}
{% assign express_shipping_end = "2023-12-22T24:00-05:00" | date: "%s" %}
{% assign overnight_shipping_end = "2023-12-23T24:00-05:00" | date: "%s" %}
{% assign today = 'now' | date: "%s" %}

{% assign difference_s = standard_shipping_end | minus: today %}
{% assign difference_s_days = difference_s | divided_by: 86400.00 | round %}
{% assign difference_e = express_shipping_end | minus: today %}
{% assign difference_e_days = difference_e | divided_by: 86400.00 | round %}
{% assign difference_o = overnight_shipping_end | minus: today %}
{% assign difference_o_days = difference | divided_by: 86400.00 | round %}

{% if today >= standard_shipping_start and today <= standard_shipping_end %}
{% if difference_s_days == 0 %}
This is the last day to order with standard shipping, so your order gets here on time for Christmas Eve!
{% elsif difference_s_days == 1 %}
There is {{difference_s_days}} day left to order with standard shipping, so your order gets here on time for Christmas Eve!

{% else %}
There are {{difference_s_days}} days left to order with standard shipping so your order gets here on time for Christmas Eve!
{% endif %}
{% elsif today > standard_shipping_end and today < express_shipping_end %}
{% if difference_e_days == 1 %}
There is {{difference_e_days}} day left to order with express shipping, so your order gets here on time for Christmas Eve!
{% else %}
There are {{difference_e_days}} days left to order with express shipping so your order gets here on time for Christmas Eve!
{% endif %}
{% elsif today >= express_shipping_end and today < overnight_shipping_end %}
This is the last day for overnight shipping so your order gets here on time for Christmas Eve!
{% else %}
{% abort_message("Unable to order and ship in time") %}
{% endif %}
```
{% endraw %}

### 일 단위로 카운트다운 만들기 {#countdown-days}

이 사용 사례는 특정 이벤트와 현재 날짜 사이의 남은 시간을 계산하고 이벤트까지 남은 일 수를 표시합니다.

{% raw %}
```liquid
{% assign event_date = {{custom_attribute.${last_selected_event_date}}} | date: "%s" %}
{% assign today =  'now' | date: "%s"  %}
{% assign difference =  event_date | minus: today %}
{% assign difference_days = difference | divided_by: 86400 %}
Your order will arrive in {{ difference_days }} days!
```
{% endraw %}

{% alert important %}
`date` 값이 있는 사용자 정의 속성 필드가 필요합니다.
{% endalert %}

### 일에서 시간, 분으로 카운트다운을 만드세요 {#countdown-dynamic}

이 사용 사례는 특정 이벤트와 현재 날짜 사이의 남은 시간을 계산합니다. 이벤트까지 남은 시간에 따라 시간 값(일, 시간, 분)을 변경하여 다양한 개인화된 메시지를 표시합니다.

예를 들어, 고객의 주문이 도착하는 데 이틀이 남았다면 "주문이 2일 후에 도착합니다."라고 말할 수 있습니다. 하루가 남지 않았다면 "주문이 17시간 후에 도착합니다."로 변경할 수 있습니다.

{% raw %}
```liquid
{% assign today =  'now' | date: "%s"  %}
{% assign scheme_finish = "2017-10-13T10:30:30" | date: "%s" %}
{% assign difference_seconds =  scheme_finish | minus: today %}
{% assign difference_minutes = difference_seconds | divided_by: 60 %}
{% assign difference_hours = difference_seconds | divided_by: 3600 %}
{% assign difference_days = difference_seconds | divided_by: 86400 %}
{% if {{difference_minutes}} > 59 and {{difference_minutes}} < 1440 %}
You have {{difference_hours}} hours left till your order arrives!
{% elsif {{difference_minutes}} < 59 %}
You have {{difference_minutes}} minutes left till your order arrives!
{% else %}
You have {{difference_days}} days left till your order arrives!
{% endif %}
```
{% endraw %}

{% alert important %}
`date` 값이 있는 사용자 정의 속성 필드가 필요합니다. 일, 시간 및 분으로 표시할 시간을 설정할 임계값을 설정해야 합니다.
{% endalert %}

### 특정 날짜까지 남은 일수를 표시하세요 {#countdown-future-date}

이 사용 사례는 현재 날짜와 미래 이벤트 날짜 사이의 차이를 계산하고 이벤트까지 남은 일수를 알리는 메시지를 표시합니다.

{% raw %}
```liquid
{% assign event_date = '2024-01-15' | date: "%s" %}
{% assign today = 'now' | date: "%s" %}
{% assign difference = event_date | minus: today %}
{% assign difference_days = difference | divided_by: 86400 %}
There are {{difference_days}} days until your birthday!
```
{% endraw %}

### 사용자 정의 날짜 속성이 도착할 때까지 남은 일수를 표시하세요 {#countdown-custom-date-attribute}

이 사용 사례는 현재 날짜와 미래 날짜 사이의 일수 차이를 계산하고 차이가 설정된 숫자와 일치할 경우 메시지를 표시합니다.

이 예에서는 사용자가 사용자 정의 날짜 속성의 이틀 이내에 메시지를 받게 됩니다. 그렇지 않으면 메시지가 전송되지 않습니다.

{% raw %}
```liquid
{% assign today = 'now' | date: '%j' | plus: 0 %}
{% assign surgery_date = {{custom_attribute.${surgery_date}}} | date: '%j' | plus: 0 %}

{% assign difference_days = {{surgery_date}} | minus: {{today}} %}
{% if difference_days == 2 %}
Your surgery is in 2 days on {{custom_attribute.${surgery_date}}}
{% else %}
{% abort_message %}
{% endif %}
```
{% endraw %}

### 남은 시간을 표시하고 남은 시간이 x 시간뿐일 경우 메시지를 중단하세요 {#countdown-abort-window}

이 사용 사례는 특정 날짜까지 남은 시간을 계산하고, 길이에 따라(날짜가 너무 가까운 경우 메시지를 건너뛰고) 다양한 개인화된 메시지를 표시합니다. 

예를 들어, "런던행 비행기 티켓을 구매할 시간이 x시간 남았습니다."라고 하지만, 런던행 비행기 출발 2시간 이내에는 메시지를 보내지 않습니다.

{% raw %}
```liquid
{% assign today =  'now' | date: "%s"  %}
{% assign dep_time = {{event_properties.${outboundDate}}} | date: "%s" %}
{% assign time_to_dep = dep_time | minus: today %}
{% if {{time_to_dep}} < 7200 %}
{% abort_message("OutboundDate less than 2 hours") %}
{% elsif {{time_to_dep}} > 7200 and {{time_to_dep}} < 86400 %}
Don't forget to buy your ticket to {{event_properties.${toStation}}} within next 24 hours!
{% else %}
Still traveling to {{event_properties.${toStation}}} in more than 24 hours? Book now!
{% endif %}
```
{% endraw %}

{% alert important %} 사용자 정의 이벤트 속성이 필요합니다. {% endalert %}

### 사용자의 멤버십이 종료되기 x일 전에 전송할 인앱 메시지 {#countdown-membership-expiry}

이 사용 사례는 멤버십 만료 날짜를 캡처하고, 만료까지 남은 시간을 계산하며, 멤버십 만료까지 남은 시간에 따라 다양한 메시지를 표시합니다.

{% raw %}
```liquid
{% assign membership_expiry = {{custom_attribute.${membership_expiry_date}}} | date: "%s" %}
{% assign today = 'now' | date: "%s" %}
{% assign difference = membership_expiry | minus: today %}
{% assign difference_days = difference | divided_by: 86400 %}

{% if difference_days > 4 and difference_days <= 7 %}
You have {{difference_days}} days left in your trial, make sure you upgrade!

{% elsif difference_days > 2 and difference_days <= 4 %}
HURRY! You have {{difference_days}} days left in your trial, make sure you upgrade!

{% elsif difference_days == 2 %}
LAST CHANCE! You have {{difference_days}} days left in your trial. Make sure you upgrade!

{% else %}
You have few days left in your trial. Make sure to upgrade!
{% endif %}
```
{% endraw %}

### 사용자의 날짜와 언어에 따라 인앱 메시지를 개인화하세요 {#countdown-personalize-language}

이 사용 사례는 이벤트에 대한 카운트다운을 계산하며, 사용자의 언어 설정에 따라 카운트다운을 해당 언어로 표시합니다.

예를 들어, 사용자가 제안이 유효한 기간을 알 수 있도록 매달 일련의 업셀 메시지를 보낼 수 있습니다.

- 초기
- 남은 2일
- 남은 1일
- 마지막 날

{% raw %}
```liquid
{% assign today = 'now' | date: "%s" %}
{% assign end_date = "2021-04-16T23:59:59" | date: "%s" %}
{% assign difference = end_date | minus: today %}
{% assign difference_days = difference | divided_by: 86400 %}
{% if {{difference_days}} >= 3 %}
{% if ${language} == 'de' %}

Hallo, das Angebot gilt bis zum 16.04.

{% elsif ${language} == 'ch' %}
Grüezi, das Angebot gilt bis zum 16.04.

{% elsif ${language} == 'en' %}
The offer is valid until 16.04.

{% else %}
The offer is valid until 16.04.

{% endif %}
{% elsif {{difference_days}} == 2 %}
{% if ${language} == 'de' %}
INSERT MESSAGE

{% elsif ${language} == 'ch' %}
INSERT MESSAGE

{% elsif ${language} == 'en' %}
INSERT MESSAGE

{% else %}
INSERT MESSAGE
{% endif %}

{% elsif {{difference_days}} == 1 %}
{% if ${language} == 'de' %}
INSERT MESSAGE

{% elsif ${language} == 'ch' %}
INSERT MESSAGE

{% elsif ${language} == 'en' %}
INSERT MESSAGE

{% else %}
INSERT MESSAGE
{% endif %}

{% elsif {{difference_days}} == 0 %}
{% if ${language} == 'de' %}
Hallo, das Angebot gilt noch heute.

{% elsif ${language} == 'ch' %}
Hallo, das Angebot gilt noch heute.

{% elsif ${language} == 'en' %}
Grüezi, das Angebot gilt noch heute.

{% else %}
Hi, the offer is only valid today.
{% endif %}

{% else %}
{% abort_message("Calculation failed") %}
{% endif %}
```
{% endraw %}

{% alert important %}
`date` 값을 할당하고 주어진 날짜가 날짜 범위를 벗어날 경우 중단 로직을 포함해야 합니다. 정확한 날짜 계산을 위해 할당된 종료 날짜는 23:59:59를 포함해야 합니다.
{% endalert %}

### 30일 후의 날짜를 월과 일 형식으로 {#countdown-template-date}에 맞춰 템플릿화합니다.

이 사용 사례는 메시지에 사용할 30일 후의 날짜를 표시합니다.

{% raw %}
```liquid
{% assign today = 'now' | date: "%s" %}
{% assign thirty_days = today | plus: 2592000 | date: "%B %d" %}
```
{% endraw %}

{% endapi %}

{% api %}

## 사용자 정의 속성

{% apitags %}
사용자 정의 속성
{% endapitags %}

- [사용자 정의 속성에 따라 메시지를 개인화합니다.](#attribute-matching)
- [두 개의 사용자 정의 속성을 빼서 차이를 금전적 가치로 표시합니다.](#attribute-monetary-difference)
- [사용자의 전체 이름이 first_name 필드에 저장되어 있는 경우 사용자의 이름을 참조합니다.](#attribute-first-name)

### 사용자 정의 속성에 따라 메시지를 개인화합니다 {#attribute-matching}

이 사용 사례는 사용자가 특정 사용자 정의 속성을 가지고 있는지 확인하고, 그렇다면 서로 다른 개인화된 메시지를 표시합니다. 

{% raw %}
```liquid
{% if custom_attribute.${hasShovel} == true and custom_attribute.${VisitToGroundTooTough} > 0 %}
The ground is very hard. The dirt road goes East.
{% elsif custom_attribute.${hasShovel} == true %}
The dirt road goes East.
{% elsif custom_attribute.${VisitToStart} > 0 %}
The dirt road goes East.
The shovel here.
{% else %}
You are at a dead-end of a dirt road. The road goes to the east. In the distance, you can see that it will eventually fork off. The trees here are very tall royal palms, and they are spaced equidistant from each other.
There is a shovel here.
{% endif %}
```
{% endraw %}

### 두 개의 사용자 정의 속성을 빼서 차이를 금전적 가치로 표시합니다 {#attribute-monetary-difference}

이 사용 사례는 두 개의 금전적 사용자 정의 속성을 캡처한 다음, 차이를 계산하고 표시하여 사용자가 목표에 도달하기 위해 얼마나 더 필요한지 알 수 있도록 합니다.

{% raw %}
```liquid
{% assign event_goal = {{custom_attribute.${last_selected_event_personal_goal}}} %}
{% assign current_raised =  {{custom_attribute.${last_selected_event_personal_amount_raised}}} %}
{% assign difference =  event_goal | minus: current_raised %}
You only have ${{ difference | round: 0 | number_with_delimiter }} left to raise!
```
{% endraw %}

### 사용자의 전체 이름이 first_name 필드에 저장되어 있는 경우 사용자의 이름을 참조합니다 {#attribute-first-name}

이 사용 사례는 사용자의 이름(이름과 성이 단일 필드에 저장된 경우)을 캡처한 다음, 이 이름을 사용하여 환영 메시지를 표시합니다.

{% raw %}
```liquid
{{${first_name} | truncatewords: 1, "" | default: 'hi'}}
{% assign name = {{${first_name}}} | split: ' ' %}
Hi {{name[0]}}, here's your message!
```

**설명:** `split` 필터는 `{{${first_name}}}`에 저장된 문자열을 배열로 변환합니다. `{{name[0]}}`를 사용하여 배열의 첫 번째 항목, 즉 사용자의 이름만 참조합니다. 

{% endraw %}
{% endapi %}

{% api %}

## 사용자 정의 이벤트

{% apitags %}
사용자 정의 이벤트
{% endapitags %}

- [현재로부터 두 시간 이내에 사용자 정의 이벤트가 있는 경우 푸시 알림을 중단합니다](#event-abort-push)
- [사용자가 사용자 정의 이벤트를 세 번 수행할 때마다 캠페인을 전송합니다](#event-three-times)
- [한 카테고리에서만 구매한 사용자에게 메시지를 전송합니다](#event-purchased-one-category)
- [지난 한 달 동안 사용자 정의 이벤트가 발생한 횟수를 추적합니다](#track)


### 현재로부터 두 시간 이내에 사용자 정의 이벤트가 있는 경우 푸시 알림을 중단합니다 {#event-abort-push}

이 사용 사례는 이벤트까지의 시간을 계산하고 남은 시간에 따라 다양한 개인화된 메시지를 표시합니다.

예를 들어, 사용자 정의 이벤트 속성이 다음 두 시간 이내에 통과할 경우 푸시 알림이 전송되지 않도록 할 수 있습니다. 이 예시는 기차 티켓의 장바구니 방치 시나리오를 사용합니다.

{% raw %}
```liquid
{% assign today =  'now' | date: "%s"  %}
{% assign dep_time = {{event_properties.${outboundDate_Time}}} | date: "%s" %}
{% assign time_to_dep = dep_time | minus: today %}
{% if {{time_to_dep}} <= 7200 %}
{% abort_message("OutboundDate less than 2 hours") %}
{% elsif {{time_to_dep}} > 7200 and {{time_to_dep}} < 86400 %}
Don't forget to buy your ticket to {{event_properties.${toStation}}} within next 24 hours
{% else %}
Still traveling to {{event_properties.${toStation}}} in more than 24 hours? Book now
{% endif %}
```
{% endraw %}

### 사용자가 사용자 정의 이벤트를 세 번 수행할 때마다 캠페인을 전송합니다 {#event-three-times}

이 사용 사례는 사용자가 사용자 정의 이벤트를 세 번 수행했는지 확인하고, 그렇다면 메시지를 표시하거나 캠페인을 전송합니다. 

{% raw %}
```liquid
{% assign cadence = custom_attribute.${example} | minus: 1 | modulo: 3 %}
{% if custom_attribute.${example} == blank %}
{% abort_message("Error calculating cadence") %}
{% elsif cadence != 0 %}
{% abort_message("Skip message") %}
{% endif %}
Did you forget something in your shopping cart?
```
{% endraw %}

{% alert important %} 사용자 정의 이벤트 수의 이벤트 속성이 있거나 Braze 엔드포인트에 웹후크를 사용해야 합니다. 이는 사용자가 이벤트를 수행할 때마다 사용자 정의 속성 (`example_event_count`)을 증가시키기 위한 것입니다. 이 예시는 3의 주기를 사용합니다 (1, 4, 7, 10 등). 주기를 0 (0, 3, 6, 9 등)에서 시작하려면 `minus: 1`을 제거하십시오.
{% endalert %}

### 한 카테고리에서만 구매한 사용자에게 메시지를 전송합니다 {#event-purchased-one-category}

이 사용 사례는 사용자가 구매한 카테고리 목록을 캡처하고, 하나의 구매 카테고리만 존재하는 경우 메시지를 표시합니다.

{% raw %}
```liquid
{% assign category = {{custom_attribute.${categories_purchased}}} %}
{% assign uniq_cat = {{category | uniq }} %}
{% if {{uniq_cat | size}} == 1%}
{{uniq_cat}}
{% else %}
{% abort_message("Purchase category doesn't exist") %}
{% endif %}
```
{% endraw %}

### 지난 한 달 동안 사용자 정의 이벤트가 발생한 횟수를 추적합니다 {#track}

이 사용 사례는 현재 월의 1일과 이전 월 사이에 기록된 사용자 정의 이벤트의 횟수를 계산합니다. 그런 다음 users/track 호출을 실행하여 이 값을 사용자 정의 속성으로 저장할 수 있습니다. 이 캠페인은 월별 데이터를 사용할 수 있기 전에 두 개의 연속 월 동안 실행되어야 합니다.

{% raw %}
```liquid

{% capture body %}
{
 "braze_id": "{{${braze_id}}}",
 "fields_to_export": ["custom_events"]
}

{% endcapture %}

{% connected_content YOUR_BRAZE_ENDPOINT/users/export/ids
 :method post
  :headers { "Authorization": "Bearer YOUR_API_KEY" }
  :body {{body}}
 :content_type application/json
 :save response
  :retry %}

{% for custom_event in response.users[0].custom_events %}
{% assign ce_name = custom_event.name %}
{% comment %} The following custom event name will need to be amended for the target custom event. {% endcomment %}

{% if ce_name == "Project Exported" %}
{% comment %}{{custom_event.name}}: {{custom_event.count}}{% endcomment %}
{% assign current_count = custom_event.count %}
{% endif %}
{% endfor %}

{% assign prev_month_count = {{custom_attribute.${projects_exported_prev_month}}} %}
{% assign latest_count = current_count | minus: prev_month_count %}
{% assign now = "now" | date: "%s" %}
{% assign yesterday = {{now}} | minus: 86400 %}
{% assign previous_month = {{yesterday}} | date: "%B" %}
{% assign previous_year = {{yesterday}} | date: "%y" %}
{% assign formatted_month = previous_month | downcase %}
{% comment %}The Custom Event name that is being tracked will be needed to be amended for the target Custom Event in the Attribute Name below. {% endcomment %}
```

```json
"attributes": [
  {
    "external_id":"{{${user_id}}}",
       "projects_exported_{{formatted_month}}_{{previous_year}}": "{{latest_count}}"
  }
]
```

{% endraw %}

{% endapi %}

{% api %}

## 언어

{% apitags %}
언어
{% endapitags %}

- [다른 언어로 월 이름 표시](#language-display-month)
- [사용자의 언어에 따라 이미지 표시](#language-image-display)
- [요일 및 사용자의 언어에 따라 메시지 개인화](#language-personalize-message)

### 다른 언어로 월 이름 표시 {#language-display-month}

이 사용 사례는 현재 날짜, 월 및 연도를 표시하며, 월은 다른 언어로 표시됩니다. 제공된 예제는 스웨덴어를 사용합니다.

{% raw %}
```liquid
{% assign day = 'now' | date: "%e" %}
{% assign year =  'now' | date: "%Y" %}
{% assign month =  'now' | date: "%B" %}

{% if {{month}} == 'January' %}
{{day}} Januari {{year}}
{% elsif {{month)) == 'February' %}
{{day}} Februari {{year}}
{% elsif {{month)) == 'March' %}
{{day}} Mars {{year}}
{% elsif {{month)) == 'April' %}
{{day}} April {{year}}
{% elsif {{month)) == 'May' %}
{{day}} Maj {{year}}
{% elsif {{month)) == 'June' %}
{{day}} Juni {{year}}
{% elsif {{month)) == 'July' %}
{{day}} Juli {{year}}
{% elsif {{month)) == 'August' %}
{{day}} Augusti {{year}}
{% elsif {{month)) == 'September' %}
{{day}} September {{year}}
{% elsif {{month)) == 'October' %}
{{day}} Oktober {{year}}
{% elsif {{month)) == 'November' %}
{{day}} November {{year}}
{% elsif {{month)) == 'December' %}
{{day}} December {{year}}
{% endif %}
```
{% endraw %}

### {#language-image-display}사용자의 언어에 따라 이미지 표시{#language-image-display}

이 사용 사례는 사용자의 언어에 따라 이미지를 표시합니다. 이 사용 사례는 Braze 미디어 라이브러리에 업로드된 이미지로만 테스트되었습니다.

{% raw %}
```liquid
{% if ${language} == 'en' %}
English image URL (for example, https://cdn-staging.braze.com/appboy/communication/assets/image_assets/images/60aecba96a93150c749b4d57/original.png?1622068137)
{% elsif ${language} == 'ru' %}
Russian image URL
{% elsif ${language} == 'es' %}
Spanish image URL
{% else %}
Fallback image URL
{% endif %}
```
{% endraw %}

### 요일 및 사용자의 언어에 따라 메시지 개인화 {#language-personalize-message}

이 사용 사례는 현재 요일을 확인하고, 요일에 따라 사용자의 언어가 제공된 언어 옵션 중 하나로 설정되어 있으면 해당 언어로 특정 메시지를 표시합니다.

제공된 예제는 화요일에 멈추지만, 주의 각 요일에 대해 반복할 수 있습니다.

{% raw %}
```liquid
{% assign today  = 'now' | date: '%A' %}

{% if today == 'Monday' %}
{% if ${language} == 'es' %}
Compra hoy y lleva tu aprendizaje de idiomas a niveles más altos. 🚀

{% elsif ${language} == 'en' %}
Purchase today and take your language learning to the next level. 🚀

{% elsif ${language} == 'zh' %}
今天就购买并将您的语言提高到一个新水平吧。🚀

{% else %}
It's Monday, but the language doesn't match 
{% endif %}

{% elsif today == 'Tuesday' %}

{% if ${language} == 'zh' %}
不要忘记解锁以获取完整版本哦。🔓

{% elsif ${language} == 'en' %}
Don't forget to unlock the full version of your language. 🔓

{% elsif ${language} == 'ja' %}
すべての機能を使ってみませんか 🔓

{% elsif ${language} == 'es' %}
No te olivides de desbloquear la versión completa del programa de idiomas. 🔓

{% else %}
tuesday default
{% endif %}
{% endif %}
```
{% endraw %}

{% endapi %}

{% api %}

## 기타

{% apitags %}
기타
{% endapitags %}

- [마케팅 이메일을 차단한 고객에게 이메일을 보내지 않도록 하세요](#misc-avoid-blocked-emails)
- [고객의 구독 상태를 사용하여 메시지의 콘텐츠를 개인화하세요](#misc-personalize-content)
- [문자열의 모든 단어의 첫 글자를 대문자로 바꾸기](#misc-capitalize-words-string)
- [사용자 정의 속성 값을 배열과 비교하기](#misc-compare-array)
- [다가오는 이벤트 알림 만들기](#misc-event-reminder)
- [배열 내에서 문자열 찾기](#misc-string-in-array)
- [배열에서 가장 큰 값 찾기](#misc-largest-value)
- [배열에서 가장 작은 값 찾기](#misc-smallest-value)
- [문자열의 끝 쿼리하기](#misc-query-end-of-string)
- [여러 조합을 가진 사용자 정의 속성에서 배열의 값 쿼리하기](#misc-query-array-values)
- [문자열을 전화번호 형식으로 변환하기](#phone-number)

### 마케팅 이메일을 차단한 고객에게 이메일을 보내지 마십시오 {#misc-avoid-blocked-emails}

이 사용 사례는 콘텐츠 블록에 저장된 차단된 사용자 목록을 가져와서 차단된 사용자가 다가오는 캠페인이나 캔버스에서 소통되지 않거나 타겟팅되지 않도록 확인합니다.

{% alert important %}
이 Liquid를 사용하려면 먼저 콘텐츠 블록 내에 차단된 이메일 목록을 저장하십시오. 목록에는 이메일 주소 사이에 추가 공백이나 문자가 삽입되지 않아야 합니다(예: `test@braze.com,abc@braze.com`).
{% endalert %}

{% raw %}
```liquid
{% assign blocked_emails = {{content_blocks.${BlockedEmailList}}} | split: ',' %}
{% for email in blocked_emails %}
    {% if {{${email_address}}} == email %}
    {% abort_message("Email is blocked") %}
    {% break %}
    {% endif %}
{% endfor %} 
Your message here!
```
{% endraw %}

**설명:** 여기에서 차단된 이메일의 콘텐츠 블록을 참조하여 잠재적인 수신자의 이메일이 이 목록에 있는지 확인합니다. 이메일이 발견되면 메시지가 전송되지 않습니다.

{% alert note %}
콘텐츠 블록의 크기 제한은 5MB입니다.
{% endalert %}

### 고객의 구독 상태를 사용하여 메시지의 콘텐츠를 개인화하십시오 {#misc-personalize-content}

이 사용 사례는 고객의 구독 상태를 사용하여 개인화된 콘텐츠를 전송합니다. 특정 구독 그룹에 가입한 고객은 이메일 구독 그룹을 위한 독점 메시지를 받게 됩니다.

{% raw %}
```liquid
{% if {{subscribed_state.${subscription_group_id}}} == 'subscribed' %}
This is an exclusive message for subscribed users!
{% else %} This is the default message for other users.
{% endif %}
```
{% endraw %}

### 문자열의 모든 단어의 첫 글자를 대문자로 바꾸기 {#misc-capitalize-words-string}

이 사용 사례는 단어 문자열을 가져와서 배열로 나누고 각 단어의 첫 글자를 대문자로 만듭니다.

{% raw %}
```liquid
{% assign words_array = {{custom_attribute.${address}}} | split: ' ' %}
{% for words in {{words_array}} %}
{{ words | capitalize | append: ' ' }}
{% endfor %} 
```
{% endraw %}

**설명:** 여기서 우리는 선택한 문자열 속성에 변수를 할당하고 `split` 필터를 사용하여 문자열을 배열로 나누었습니다. 그런 다음 `for` 태그를 사용하여 변수 `words`를 새로 생성된 배열의 각 항목에 할당한 후, `capitalize` 필터와 `append` 필터를 사용하여 각 용어 사이에 공백을 추가하여 해당 단어를 표시합니다.

### 사용자 정의 속성 값을 배열 {#misc-compare-array}과 비교합니다.

이 사용 사례는 좋아하는 상점 목록을 가져와 사용자의 좋아하는 상점이 그 목록에 있는지 확인하고, 그렇다면 해당 상점에서 특별 제안을 표시합니다.

{% raw %}
```liquid
{% assign favorite_stores = 'Target,Walmart,Costco' | split: ',' %}
{% for store in favorite_stores %}
{% if {{custom_attribute.${favorited_stores}}} contains {{store}} %}
Today's offer from {{store}}

{% break %}

{% else %}
{% abort_message("No attribute found") %}
{% endif %}
{% endfor %}
```
{% endraw %}

{% alert important %} 이 시퀀스는 기본 조건문에 `break` 태그가 있습니다. 이로 인해 일치하는 항목이 발견되면 루프가 중지됩니다. 많은 일치 항목이나 모든 일치 항목을 표시하려면 `break` 태그를 제거하십시오. {% endalert %}

### 다가오는 이벤트 알림 만들기 {#misc-event-reminder}

이 사용 사례는 사용자가 사용자 정의 이벤트를 기반으로 다가오는 알림을 설정할 수 있도록 합니다. 예제 시나리오는 사용자가 정책 갱신 날짜에 대한 알림을 설정할 수 있도록 하며, 이 날짜는 26일 이상 남아 있으며, 알림은 정책 갱신 날짜의 26일, 13일, 7일 또는 2일 전에 전송됩니다.

이 사용 사례에서는 다음이 [웹훅 캠페인]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) 또는 캔버스 단계의 본문에 포함되어야 합니다.

{% raw %}
```liquid
{% comment %}
Depending on how the reminder_capture property is passed to Braze, with/without a timestamp, the number of days could impact whether a user falls on either side of the 26/13/7/2-day windows.
Once users have been assigned to a Reminder journey/flow, they are then scheduled to enter a subsequent Canvas.
This 'Event Listener' can be used to split out users into different journeys based on the Custom Event properties sent to Braze.
{% endcomment %}

{% comment %}
When testing, make sure the campaign ID, campaign API endpoint, Canvas ID, Canvas API endpoint are entered correctly. In this example, the Canvas ID and Canvas API endpoint have been set up for sharing with the client. In practice, this can be testing using a campaign ID and Campaign API endpoint.
{% endcomment %}

{% comment %}
The following step calculates how much there is between today's date and the Reminder Date as 'time_to_reminder'.
{% endcomment %}

{% assign today = "now" | date: '%s' %}
{% assign reminder_start_date = {{event_properties.${reminder_date}}} | date: '%s' %}
{% assign time_to_reminder = reminder_start_date | minus: today %}

{% comment %}
The following step checks if the time_to_reminder is more than 26 days away; if this is true, then the user is scheduled to enter the subsequent Canvas 26 days before the reminder_date.
The time is converted from 'seconds from 1970' to the appropriate Reminder Date in the required ISO 8601 format.
N.B. Additional time zones would need to be catered for by adding an additional API Schedule property of "in_local_time"
{% endcomment %}

{% if {{time_to_reminder}} > 2246400 %}
{% assign time_to_first_message = reminder_start_date | plus: 2246400 %}
{{ time_to_first_message | date: '%Y-%m-%dT%H:%M' }}
{
"canvas_id": "954e15bc-af93-9dc8-a863-ad2580f1750e",
"recipients": [
{
"external_user_id": "{{${user_id}}}"
}
],
"trigger_properties" : {
"enquiry_id" : "{{event_properties.${reminder_id}}}",
"reminder_date" : "{{event_properties.${reminder_date} | date: '%Y-%m-%dT%H:%M:%S+0000'}}",
"message_personalisation_X" : "{{event_properties.${property_x}}}",
"message_personalisation_Y" : "{{event_properties.${property_y}}}",
"message_personalisation_Z" : "{{event_properties.${property_z}}}"
},

"schedule": {
"time": "{{ time_to_first_message | date: '%Y-%m-%dT%H:%M:%S+0000' }}"
}
}

{% comment %}
The following step checks if the time_to_reminder is less than 26 days away but more than 13 days away.
Users are scheduled to enter the journey on day 13.
{% endcomment %}

{% elsif 1123200 > {{time_to_reminder}} and {{time_to_reminder}} < 2246399 %}
{% assign time_to_first_message = reminder_start_date | plus: 1123200 %}

{
"canvas_id": "954e15bc-af93-9dc8-a863-ad2580f1750e",
"recipients": [
{
"external_user_id": "{{${user_id}}}"
}
],
"trigger_properties" : {
"enquiry_id" : "{{event_properties.${reminder_id}}}",
"reminder_date" : "{{event_properties.${reminder_date} | date: '%Y-%m-%dT%H:%M:%S+0000'}}",
"message_personalisation_X" : "{{event_properties.${property_x}}}",
"message_personalisation_Y" : "{{event_properties.${property_y}}}",
"message_personalisation_Z" : "{{event_properties.${property_z}}}"
},

"schedule": {
"time": "{{ time_to_first_message | date: '%Y-%m-%dT%H:%M:%S+0000' }}"
}
}

{% comment %}
The following step checks if the time_to_reminder is less than 13 days away but more than seven days away.
Users are scheduled to enter the journey on day 7.
{% endcomment %}

{% elsif 604800 > {{time_to_reminder}} and {{time_to_reminder}} < 1123199 %}
{% assign time_to_first_message = reminder_start_date | plus: 604800 %}

{
"canvas_id": "954e15bc-af93-9dc8-a863-ad2580f1750e",
"recipients": [
{
"external_user_id": "{{${user_id}}}"
}
],
"trigger_properties" : {
"enquiry_id" : "{{event_properties.${reminder_id}}}",
"reminder_date" : "{{event_properties.${reminder_date} | date: '%Y-%m-%dT%H:%M:%S+0000'}}",
"message_personalisation_X" : "{{event_properties.${property_x}}}",
"message_personalisation_Y" : "{{event_properties.${property_y}}}",
"message_personalisation_Z" : "{{event_properties.${property_z}}}"
},

"schedule": {
"time": "{{ time_to_first_message | date: '%Y-%m-%dT%H:%M:%S+0000' }}"
}
}

{% comment %}
The following step checks if the time_to_reminder is less than seven days away but more than two days away.
Users are scheduled to enter the journey on day 2.
{% endcomment %}

{% else {{time_to_reminder}} < 604799 and {{time_to_reminder}} > 172860 %}
{% assign time_to_first_message = reminder_start_date | plus: 172800 %}

{
"canvas_id": "954e15bc-af93-9dc8-a863-ad2580f1750e",
"recipients": [
{
"external_user_id": "{{${user_id}}}"
}
],
"trigger_properties" : {
"enquiry_id" : "{{event_properties.${reminder_id}}}",
"reminder_date" : "{{event_properties.${reminder_date} | date: '%Y-%m-%dT%H:%M:%S+0000'}}",
"message_personalisation_X" : "{{event_properties.${property_x}}}",
"message_personalisation_Y" : "{{event_properties.${property_y}}}",
"message_personalisation_Z" : "{{event_properties.${property_z}}}"
},

"schedule": {
"time": "{{ time_to_first_message | date: '%Y-%m-%dT%H:%M:%S+0000' }}"
}
}
{% endif %}
```
{% endraw %}

{% alert important %} 

사용자 정의 이벤트 `reminder_capture`이 필요하며, 사용자 정의 이벤트 속성에는 최소한 다음이 포함되어야 합니다:

- `reminder-id`: 사용자 정의 이벤트의 식별자
- `reminder_date`: 사용자가 알림이 만료되는 날짜
- `message_personalisation_X`: 전송 시 메시지를 개인화하는 데 필요한 모든 속성

{% endalert %}

### 배열 {#misc-string-in-array} 내에서 문자열 찾기

이 사용 사례는 사용자 정의 속성 배열에 특정 문자열이 포함되어 있는지 확인하고, 존재하는 경우 특정 메시지를 표시합니다.

{% raw %}
```liquid
{% if custom_attribute.${PartnershipProgramsNotLinked} contains 'Hertz' %}
Link your Hertz account to use Hertz Fast Lane.
{% endif %}
```
{% endraw %}

### 배열 {#misc-largest-value}에서 가장 큰 값 찾기

이 사용 사례는 사용자 메시지에 사용할 주어진 사용자 정의 속성 배열에서 가장 높은 값을 계산합니다.

예를 들어, 현재 최고 점수나 항목에 대한 최고 입찰가를 사용자에게 보여주고 싶을 수 있습니다.

{% raw %}
```liquid
{% assign maxValue = 0 %}
{% for attribute in {{custom_attribute.${array_attribute}}} %}
{% assign compareValue = {{attribute | plus: 0}} %}
{% if compareValue > maxValue %}
{% assign maxValue = compareValue %}
{% endif %}
{% endfor %}
{{maxValue}}
```
{% endraw %}

{% alert important %}
정수 값을 가지며 배열(목록)의 일부인 사용자 정의 속성을 사용해야 합니다. {% endalert %}

### 배열에서 가장 작은 값을 찾습니다. {#misc-smallest-value}

이 사용 사례는 사용자 메시지에 사용할 주어진 사용자 정의 속성 배열에서 가장 낮은 값을 계산합니다.

예를 들어, 사용자에게 가장 낮은 점수나 가장 저렴한 항목을 보여주고 싶을 수 있습니다.

{% raw %}
```liquid
{% assign minValue = custom_attribute.${array_attribute}[0] | plus: 0 %}
{% for attribute in {{custom_attribute.${array_attribute}}} %}
{% assign compareValue = {{attribute | plus: 0}} %}
{% if compareValue < minValue %}
{% assign minValue = compareValue %}
{% endif %}
{% endfor %}
{{minValue}}
```
{% endraw %}

{% alert important %} 정수 값을 가지며 배열(목록)의 일부인 사용자 정의 속성을 사용해야 합니다. {% endalert %}

### 문자열의 끝을 쿼리합니다. {#misc-query-end-of-string}

이 사용 사례는 메시지에 사용할 문자열의 끝을 쿼리합니다.

{% raw %}
```liquid
{% assign interest = {{custom_attribute.${Buyer Interest}} | first } %}
{% assign marketplace = {{{{interest}} | split: "" | reverse | join: "" |  truncate: 4, ""}} %}
{% if {{marketplace}} == '3243' %}

Your last marketplace search was on {{custom_attribute.${Last marketplace buyer interest} | date: '%d.%m.%Y'}}. Check out all of our new offers.

{% else %}
{% abort_message() %}
{% endif %}
```
{% endraw %}

### 여러 조합을 가진 사용자 정의 속성에서 배열의 값을 쿼리합니다. {#misc-query-array-values}

이 사용 사례는 곧 만료될 프로그램 목록을 가져와 사용자의 즐겨찾기 프로그램이 그 목록에 있는지 확인하고, 있다면 사용자에게 곧 만료될 것이라는 메시지를 표시합니다.

{% raw %} 
```liquid
{% assign expired_shows = 'Modern Family,The Rookie,Body of Proof,Felicity' | split: ',' %}
{% for show in expired_shows %}
{% if {{custom_attribute.${Favorite Shows}}} contains {{show}} %}
{% assign new_shows = new_shows | append: {{show}} | append: '*' %}
{% endif %}
{% endfor %}
{% assign new_shows_clean = new_shows | split: '*' %}
{% if new_shows_clean.size != 0 %}

All episodes of {{new_shows_clean | join: ', ' }} expire on 9/8 - watch them now before they're gone!

{% else %}
{% abort_message("Not found") %}
{% endif %}
```
{% endraw %}

{% alert important %} 먼저 배열 간의 일치를 찾아야 하며, 그런 다음 일치를 나누기 위한 논리를 구축해야 합니다. {% endalert %}

### 문자열을 전화번호 형식으로 변환합니다. {#phone-number}

이 사용 사례는 `phone_number` 사용자 프로필 필드를 인덱싱하는 방법을 보여주며(기본적으로 정수 문자열로 형식화됨), 지역 전화번호 표준에 따라 재형식화합니다. 예를 들어, 1234567890을 (123)-456-7890으로 변환합니다.

{% raw %} 
```liquid
{% assign phone = {{${phone_number}}} | remove: "-" | split: '' %}

({{ phone[0] }}{{ phone[1] }}{{ phone[2] }})-{{ phone[3] }}{{ phone[4] }}{{ phone[5] }}-{{ phone[6] }}{{ phone[7] }}{{ phone[8] }}{{ phone[9] }}
```
{% endraw %}

{% endapi %}

{% api %}

## 플랫폼 타겟팅

{% apitags %}
플랫폼 타겟팅
{% endapitags %}

- [장치 OS에 따라 복사본을 구분합니다.](#platform-device-os)
- [특정 플랫폼만 타겟팅합니다.](#platform-target)
- [특정 OS 버전이 있는 iOS 장치만 타겟팅합니다.](#platform-target-ios-version)
- [웹 브라우저만 타겟팅합니다.](#platform-target-web)
- [특정 모바일 통신사 타겟](#platform-target-carrier)

### 기기 OS {#platform-device-os}에 따라 복사본을 구분합니다.

이 사용 사례는 사용자가 어떤 플랫폼에 있는지 확인하고, 그들의 플랫폼에 따라 특정 메시지를 표시합니다.

예를 들어, 모바일 사용자에게는 메시지 복사의 짧은 버전을 보여주고, 다른 사용자에게는 일반적인 긴 버전을 보여줄 수 있습니다. 모바일 사용자에게는 그들에게 관련된 특정 메시지를 보여줄 수 있지만, 웹 사용자에게는 관련이 없을 수 있습니다. 예를 들어, iOS 메시지는 Apple Pay에 대해 이야기할 수 있지만, Android 메시지는 Google Pay를 언급해야 합니다.

{% raw %}
```liquid
{% if targeted_device.${platform} == "ios" or targeted_device.${platform} == "android" %}
This is a shorter copy.

{% else %}
This is the regular copy and much longer than the short version. 
{% endif %}
```
{% endraw %}

{% alert note %}
Liquid는 대소문자를 구분하며, `targeted_device.${platform}`는 모든 소문자로 값을 반환합니다.
{% endalert %}

### 특정 플랫폼만 타겟팅합니다 {#platform-target}

이 사용 사례는 사용자의 기기 플랫폼을 캡처하고, 플랫폼에 따라 메시지를 표시합니다.

예를 들어, Android 사용자에게만 메시지를 보내고 싶을 수 있습니다. 이것은 세분화 도구 내에서 앱을 선택하는 대안으로 사용될 수 있습니다.

{% raw %}
```liquid
{% if {{targeted_device.${platform}}} == 'android' %} 

This is a message for an Android user! 

{% else %}  
{% abort_message %} 
{% endif %}
```
{% endraw %}

### 특정 OS 버전 {#platform-target-ios-version}을 가진 기기만 타겟팅합니다.

이 사용 사례는 사용자의 OS 버전이 특정 버전 집합에 해당하는지 확인하고, 그렇다면 특정 메시지를 표시합니다.

사용된 예시는 OS 버전 10.0 이하의 사용자에게 지원 종료 경고를 보냅니다.

{% raw %}
```liquid
{% if {{targeted_device.${os}}} == "10.0" or {{targeted_device.${os}}} == "10.0.1" or {{targeted_device.${os}}} == "10.0.2" or {{targeted_device.${os}}} == "10.0.3" or {{targeted_device.${os}}} == "10.1" or {{targeted_device.${os}}} == "10.2" or {{targeted_device.${os}}} == "10.2.1" or {{targeted_device.${os}}} == "10.3" or {{targeted_device.${os}}} == "10.3.1" or {{targeted_device.${os}}} == "10.3.2" or {{targeted_device.${os}}} == "10.3.3" or {{targeted_device.${os}}} == "10.3.4" or {{targeted_device.${os}}} == "9.3.1" or {{targeted_device.${os}}} == "9.3.2" or {{targeted_device.${os}}} == "9.3.3" or {{targeted_device.${os}}} == "9.3.4" or {{targeted_device.${os}}} == "9.3.5" %}

We are phasing out support for your device's operating system. Be sure to update to the latest software for the best app experience.

{% else %}
{% abort_message %}
{% endif %}
```
{% endraw %}

### 웹 브라우저만 타겟팅합니다 {#platform-target-web}

이 사용 사례는 사용자의 타겟 기기가 Mac 또는 Windows에서 실행되는지 확인하고, 그렇다면 특정 메시지를 표시합니다.

{% raw %}
```liquid
{% if {{targeted_device.${os}}} == 'Mac' or {{targeted_device.${os}}} == 'Windows' %}

This message will display on your desktop web browser.

{% else %}
{% abort_message %}
{% endif %}
```
{% endraw %}

다음 사용 사례는 웹 사용자가 iOS 또는 Android에 있는지 확인하고, 그렇다면 특정 메시지를 표시합니다.

{% raw %}
```liquid
{% if {{targeted_device.${os}}} == 'iOS' and {{targeted_device.${platform}}} == 'web' %}

Content for iOS.

{% elsif {{targeted_device.${os}}} == 'android' and {{targeted_device.${platform}}} == 'web' %}

Content for Android.

{% else %}
{% abort_message %} 
{% endif %}
```
{% endraw %}

### 특정 모바일 통신사 타겟팅 {#platform-target-carrier}

이 사용 사례는 사용자의 기기 통신사가 Verizon인지 확인하고, 그렇다면 특정 메시지를 표시합니다.

푸시 알림 및 인앱 메시지 채널의 경우, Liquid를 사용하여 메시지 본문에 기기 통신사를 지정할 수 있습니다. 수신자의 장치 통신사가 일치하지 않으면 메시지가 전송되지 않습니다.

{% raw %}
```liquid
{% if {targeted_device.${carrier}} contains "verizon" or {targeted_device.${carrier}} contains "Verizon" %}

This is a message for Verizon users!

{% else %}
{% abort_message %}
{% endif %}
```
{% endraw %}

{% endapi %}

{% api %}

## 시간대

{% apitags %}
시간대
{% endapitags %}

- [사용자의 시간대에 따라 메시지를 개인화하세요.](#personalize-timezone)
- [사용자 정의 속성에 CST 시간대를 추가하세요.](#time-append-cst)
- [타임스탬프를 삽입하세요.](#time-insert-timestamp)
- [사용자의 현지 시간대의 시간 창 동안에만 Canvas 푸시를 전송하세요.](#time-canvas-window)
- [사용자의 현지 시간대의 시간 창 사이에 반복적인 인앱 메시지 캠페인을 전송하세요.](#time-reocurring-iam-window)
- [사용자의 현지 시간대에서 평일과 주말에 다른 메시지를 전송하세요.](#time-weekdays-vs-weekends)
- [사용자의 현지 시간대에서 하루 중 시간에 따라 다른 메시지를 전송하세요.](#time-of-day)

### 사용자의 시간대에 따라 메시지를 개인화하세요 {#personalize-timezone}

이 사용 사례는 사용자의 시간대에 따라 다른 메시지를 표시합니다.

{% raw %}
```liquid
{% if {{${time_zone}}} == 'xx' %}
Message for time zone xx.
{% elsif {{$time_zone}}} == 'yy' %}
Message for time zone yy.
{% else %}
{% abort_message("Invalid time zone") %}
{% endif %}
```
{% endraw %}

### 사용자 정의 속성에 CST 시간대를 추가하세요 {#time-append-cst}

이 사용 사례는 주어진 시간대에서 사용자 정의 날짜 속성을 표시합니다.

옵션 1:
{% raw %}
```liquid
{{custom_attribute.${application_expires_date} | time_zone: -0005 | date: '%B, %d %Y' }}
```
{% endraw %}

옵션 2:
{% raw %}
```liquid
{{custom_attribute.${application_expires_date} | time_zone: 'America/Chicago' | date: '%B %d %Y %z' }}
```
{% endraw %}

### 타임스탬프를 삽입하세요 {#time-insert-timestamp}

이 사용 사례는 현재 시간대에 타임스탬프가 포함된 메시지를 표시합니다.

제공된 다음 예시는 날짜를 YYYY-mm-dd HH:MM:SS 형식으로 표시합니다. 예: 2021-05-03 10:41:04.

{% raw %}
```liquid
{{${user_id} | default: 'You'}} received a campaign, rendered at ({{ "now" | time_zone: ${time_zone} | date: "%Y-%m-%d %H:%M:%S" }})
```
{% endraw %}

### 사용자의 현지 시간대의 시간 창 동안에만 Canvas 푸시를 전송하세요 {#time-canvas-window}

이 사용 사례는 사용자의 현지 시간대에서 시간을 확인하고, 설정된 시간 내에 해당하면 특정 메시지를 표시합니다.

{% raw %}
```liquid
{% assign time = 'now' | time_zone: ${time_zone} %}
{% assign hour = time | date: '%H' | plus: 0 %}
{% if hour > 20 or hour < 8 %}
{% abort_message("Outside allowed time window") %}
{% endif %}

Here's a message that will send between 8 am and 8 pm!
```
{% endraw %}

### 사용자의 현지 시간대 {#time-reoccurring-iam-window}에 특정 시간대 사이에 반복되는 인앱 메시지 캠페인을 전송합니다.

이 사용 사례는 사용자의 현재 시간이 설정된 시간대 내에 있는 경우 메시지를 표시합니다.

예를 들어, 다음 시나리오는 사용자가 상점이 닫혀 있음을 알 수 있도록 합니다.

{% raw %}
```liquid
{% assign time = 'now' | time_zone: ${time_zone} %} 
{% assign hour = time | date: '%H' | plus: 0 %}
{% if hour > 21 or hour < 10 %}

Store's closed. Come back between 11 am and 9 pm!

{% else %} 
{% abort_message("Not sent because the store is open") %}
{% endif %}
```
{% endraw %}

### 사용자의 현지 시간대 {#time-weekdays-vs-weekends}에 주중과 주말에 따라 다른 메시지를 전송합니다.

이 사용 사례는 사용자의 현재 요일이 토요일 또는 일요일인지 확인하고, 요일에 따라 다른 메시지를 표시합니다.

{% raw %}
```liquid
{% assign today = 'now' | time_zone: ${time_zone} | date: "%A" %}
{% if {{today}} == 'Saturday' or {{today}} == 'Sunday' %}
It's {{today}}, why don't you open the app for your transactions?

{% else %}
It's {{today}}, why don't you visit the store?
{% endif %}
```
{% endraw %}

### 사용자의 현지 시간대 {#time-of-day}에 시간대에 따라 다른 메시지를 전송합니다.

이 사용 사례는 사용자의 현재 시간이 설정된 시간대 외부에 있는 경우 메시지를 표시합니다.

예를 들어, 시간대에 따라 달라지는 시간 민감한 기회에 대해 사용자에게 알리고 싶을 수 있습니다.

{% raw %}
```liquid
{% assign time = 'now' | time_zone: ${time_zone} %}
{% assign hour = time | date: '%H' | plus: 0 %}
{% if hour > 20 or hour < 8 %}
{% abort_message("Outside allowed time window") %}
{% endif %}

Check out this new bar after work today. HH specials!
```
{% endraw %}

{% alert note %} 이것은 [조용한 시간]({{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/time_based_campaign/#time-based-functionalities-for-campaigns)의 반대입니다. {% endalert %}

{% endapi %}

{% api %}

## 주/일/월

{% apitags %}
주/일/월
{% endapitags %}

- [이전 달의 이름을 메시지에 가져옵니다.](#month-name)
- [매달 마지막에 캠페인을 전송합니다.](#month-end)
- [매달 마지막(주중) 날에 캠페인을 전송합니다.](#day-of-month-last)
- [매일 다른 메시지를 전송합니다.](#day-of-month)
- [매주 다른 메시지를 전송합니다.](#day-of-week)

### 이전 달의 이름을 메시지에 가져옵니다 {#month-name}

이 사용 사례는 현재 달을 가져와서 메시지에 사용될 이전 달을 표시합니다.

{% raw %}
```liquid
{% assign today = 'now' | date: "%m" %}
{% assign last_month = {{today}} | minus: 1 %}
{% if last_month == 1 %}
{% assign month = "January" %}
{% elsif last_month == 2 %}
{% assign month = "February" %}
{% elsif last_month == 3 %}
{% assign month = "March" %}
{% elsif last_month == 4 %}
{% assign month = "April" %}
{% elsif last_month == 5 %}
{% assign month = "May" %}
{% elsif last_month == 6 %}
{% assign month = "June" %}
{% elsif last_month == 7 %}
{% assign month = "July" %}
{% elsif last_month == 8 %}
{% assign month = "August" %}
{% elsif last_month == 9 %}
{% assign month = "September" %}
{% elsif last_month == 10 %}
{% assign month = "October" %}
{% elsif last_month == 11 %}
{% assign month = "November" %}
{% elsif last_month == 0 %}
{% assign month = "December" %}
{% endif %}

Here's an overview of what your spending looked like in {{month}}.
```
{% endraw %}

대신 다음을 사용하여 동일한 결과를 얻을 수 있습니다.

{% raw %}
```liquid
{% assign last_month_name = 'now' | date: "%Y-%m-01" | date: '%s' | minus: 1 | date: "%B" %}

Here's an overview of what your spending looked like in {{month}}.
```
{% endraw %}

### 매달 마지막에 캠페인을 전송합니다 {#month-end}

이 사용 사례는 현재 날짜가 날짜 목록에 포함되어 있는지 확인하고, 날짜에 따라 특정 메시지를 표시합니다.

{% alert note %} 이는 윤년(2월 29일)을 고려하지 않습니다. {% endalert %}

{% raw %}
```liquid
{% assign current_date = 'now' | date: '%b %d' %}

{% if current_date == "Jan 31" or current_date == "Feb 28" or current_date == "Mar 31" or current_date == "Apr 30" or current_date == "May 31" or current_date == "Jun 30" or current_date == "Jul 31" or current_date == "Aug 31" or current_date == "Sep 30" or current_date == "Oct 31" or current_date == "Nov 30" or current_date == "Dec 31" %}

The date is correct

{% else %}
{% abort_message("Date is not listed") %}
{% endif %}
```
{% endraw %}

### 한 달의 마지막(평일) 날에 캠페인을 보내세요 {#day-of-month-last}

이 사용 사례는 현재 월과 일을 캡처하고 현재 일이 한 달의 마지막 평일에 해당하는지 계산합니다.

예를 들어, 한 달의 마지막 수요일에 사용자에게 제품 피드백을 요청하는 설문조사를 보낼 수 있습니다.

{% raw %}
```liquid
{% comment %}Pull the day, day name, month, and year from today's date.{% endcomment %}
{% assign current_day = "now" | date: "%d" %}
{% assign current_day_name = "now" | date: "%a" %}
{% assign current_month = "now" | date: "%b" %}
{% assign current_year = "now" | date: "%Y" %}

{% comment %}Assign the correct number of days for the current month.{% endcomment %}

{% if current_month == "Jan" %}
{% assign last_day_of_month = 31 %}
{% elsif current_month == "Mar" %}
{% assign last_day_of_month = 31 %}
{% elsif current_month == "Apr" %}
{% assign last_day_of_month = 30 %}
{% elsif current_month == "May" %}
{% assign last_day_of_month = 31 %}
{% elsif current_month == "Jun" %}
{% assign last_day_of_month = 30 %}
{% elsif current_month == "Jul" %}
{% assign last_day_of_month = 31 %}
{% elsif current_month == "Aug" %}
{% assign last_day_of_month = 31 %}
{% elsif current_month == "Sep" %}
{% assign last_day_of_month = 30 %}
{% elsif current_month == "Oct" %}
{% assign last_day_of_month = 31 %}
{% elsif current_month == "Nov" %}
{% assign last_day_of_month = 30 %}
{% elsif current_month == "Dec" %}
{% assign last_day_of_month = 31 %}
{% endif %}

{% comment %}Assign the correct number of days if the current month is February, taking into account leap years.{% endcomment %}

{% assign leap_year_remainder = {{current_year | modulo: 4 }} != "0" %}
{% if leap_year_remainder == 0 and current_month == "Feb" %}
{% assign last_day_of_month = 29 %}
{% elsif leap_year_remainder != "0" and current_month == "Feb" %}
{% assign last_day_of_month = 28 %}
{% endif %}

{% comment %}Check that today's date is within a week of the last day of the month. If not, abort the message. If so, check that today is Wednesday. If not, abort the message.{% endcomment %}

{% assign diff_in_days = last_day_of_month | minus: current_day | plus: 1%} 
{% if diff_in_days <= 7 %} 
{% unless current_day_name == "Wed" %} 
{% abort_message("Wrong day of the week") %} 
{% endunless %} 
{% else %} 
{% abort_message("Not the last week of the month") %} 
{% endif %}
```
{% endraw %}

### 한 달의 매일 다른 메시지를 보내세요 {#day-of-month}

이 사용 사례는 현재 날짜가 목록의 날짜와 일치하는지 확인하고, 요일에 따라 별도의 메시지를 표시합니다.

{% raw %}
```liquid
{% assign today = 'now' | time_zone: {{${time_zone}}} | date: "%Y-%m-%d" %}
{% assign day_1 = "2019-12-01" | time_zone: {{${time_zone}}} | date: "%Y-%m-%d" %}
{% assign day_2 = "2019-12-02" | time_zone: {{${time_zone}}} | date: "%Y-%m-%d" %}
{% assign day_3 = "2019-12-03" | time_zone: {{${time_zone}}} | date: "%Y-%m-%d" %}

{% if today == day_1 %}
Message for 2019-12-01

{% elsif today == day_2 %}
Message for 2019-12-02

{% elsif today == day_3%}
Message for 2019-12-03

{% else %}
{% abort_message("Date not listed") %}
{% endif %}
```
{% endraw %}

### 한 주의 매일 다른 메시지를 보내세요 {#day-of-week}

이 사용 사례는 현재 요일을 확인하고, 요일에 따라 별도의 메시지를 표시합니다.

{% raw %}
```liquid
{% assign today = 'now' | date: "%A" %}
{% case today %}
{% when 'Monday' %}
Monday copy

{% when 'Tuesday' %}
Tuesday copy

{% when 'Wednesday' %}
Wednesday copy

{% when  'Thursday' %}
Thursday copy

{% when  'Friday' %}
Friday copy

{% when 'Saturday' %}
Saturday copy

{% when 'Sunday' %}
Sunday copy

{% else %}
Default copy
{% endcase %}
```
{% endraw %}

{% alert note %}
"기본 복사본"이라는 줄을 {% raw %}`{% abort_message() %}`{% endraw %}로 교체하여 요일이 알려지지 않은 경우 메시지가 전송되지 않도록 할 수 있습니다.
{% endalert %}

{% endapi %}
