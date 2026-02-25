---
nav_title: Liquid 사용 사례 라이브러리
article_title: Liquid 사용 사례 라이브러리
page_order: 10
search_rank: 2
excerpt_separator: ""
page_type: glossary
layout: liquid_use_case_glossary
description: "이 랜딩 페이지에서는 기념일, 앱 사용량, 카운트다운 등 카테고리별로 정리된 Liquid 사용 사례 샘플을 확인할 수 있습니다."

---

{% api %}

## 기념일 및 공휴일

{% apitags %}
기념일 및 공휴일
{% endapitags %}

- [사용자의 기념일 연도에 따라 메시지 개인화하기](#anniversary-year)
- [사용자의 생일 주를 기준으로 메시지 개인화하기](#birthday-week)
- [생일이 있는 달에 사용자에게 캠페인 보내기](#birthday-month)
- [주요 공휴일에는 메시지 보내지 않기](#holiday-avoid)

### 사용자의 기념일 연도에 따라 메시지 개인화하기 {#anniversary-year}

이 사용 사례는 사용자의 최초 가입 날짜를 기준으로 앱 기념일을 계산하고 기념 연수에 따라 다른 메시지를 표시하는 방법을 보여줍니다.

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

**설명:** 여기서는 예약 변수 `now`를 사용하여 현재 날짜와 시간을 [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601) 형식으로 템플릿화합니다. 필터 `%B`("May"와 같은 월)와 `%d`("18"과 같은 일)는 현재 월과 일의 형식을 지정합니다. 그런 다음 `signup_date` 값에 동일한 날짜 및 시간 필터를 사용하여 조건부 태그와 로직을 통해 두 값을 비교할 수 있도록 합니다.

그런 다음 변수 문을 세 개 더 반복하여 `signup_date`에 대해 `%B` 및 `%d`를 구하고 `%Y`("2021"과 같은 연도)도 추가합니다. 이렇게 하면 `signup_date`의 날짜와 시간이 연도만으로 구성됩니다. 일과 월을 알면 사용자의 기념일이 오늘인지 확인할 수 있고, 연도를 알면 몇 년이 지났는지 알 수 있으므로 축하 메시지를 보낼 수 있습니다!

{% alert tip %} 가입 날짜를 수집한 연수만큼 조건을 만들 수 있습니다. {% endalert %}  

### 사용자의 생일 주를 기준으로 메시지 개인화하기 {#birthday-week}

이 사용 사례에서는 사용자의 생일을 찾아 현재 날짜와 비교한 다음 생일 주간 전, 중, 후에 특별한 생일 메시지를 표시하는 방법을 보여줍니다.

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

**설명:** [기념일 연도](#anniversary-year) 사용 사례와 마찬가지로 여기서는 예약 변수 `now`를 사용하고 `%W` 필터(1년 52주 중 12주와 같은 주 번호)를 사용하여 사용자의 생일이 속한 연도의 주 번호를 가져옵니다. 사용자의 생일 주간이 현재 주와 일치하면 축하 메시지를 보냅니다! 

또한 `last_week` 및 `next_week`에 대한 문구를 포함하여 메시징을 더욱 개인화할 수 있습니다.

### 생일이 있는 달에 사용자에게 캠페인 보내기 {#birthday-month}

이 사용 사례에서는 사용자의 생일 월을 계산하여 현재 월에 생일이 있는지 확인하고, 생일이 있는 경우 특별 메시지를 보내는 방법을 보여줍니다.

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

**설명:** [생일 주](#birthday-week) 사용 사례와 유사하지만 여기서는 `%B` 필터("May"와 같은 월)를 사용하여 이번 달에 생일이 있는 사용자를 계산한다는 점이 다릅니다. 생일이 있는 사용자에게 매달 이메일을 보내는 것도 하나의 활용 방안이 될 수 있습니다.

### 주요 공휴일에는 메시지 보내지 않기 {#holiday-avoid}

이 사용 사례는 참여도가 낮을 수 있는 주요 공휴일을 피하면서 연휴 기간에 메시지를 보내는 방법을 보여줍니다.

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

**설명:** 여기서는 예약 변수 `now`(현재 날짜 및 시간)에 `%Y`("2023"과 같은 연도), `%m`("12"와 같은 월), `%d`("25"와 같은 일) 필터를 사용하여 `today`라는 용어를 할당하고 날짜 형식을 지정합니다. 그런 다음 조건문을 실행하여 `today` 변수가 선택한 공휴일과 일치하면 메시지가 중단되도록 합니다. 

제공된 예제에서는 크리스마스 이브, 크리스마스 당일 및 박싱데이(크리스마스 다음 날)를 사용했습니다.

{% endapi %}

{% api %}

## 앱 사용

{% apitags %}
앱 사용
{% endapitags %}

- [사용자가 세션을 기록한 경우 해당 사용자의 언어로 메시지 보내기](#app-session-language)
- [사용자가 마지막으로 앱을 연 시간에 따라 메시지 개인화하기](#app-last-opened)
- [사용자가 마지막으로 앱을 사용한 지 3일이 지나지 않은 경우 다른 메시지 표시하기](#app-last-opened-less-than)

### 사용자가 세션을 기록하지 않은 경우 해당 사용자의 언어로 메시지 보내기 {#app-session-language}

이 사용 사례는 사용자가 세션을 기록했는지 확인하고, 기록하지 않은 경우 커스텀 속성을 통해 수동으로 수집한 언어(있는 경우)를 기반으로 메시지를 표시하는 로직을 포함합니다. 계정에 연결된 언어 정보가 없는 경우 기본 언어로 메시지가 표시됩니다. 사용자가 세션을 기록한 경우 사용자와 연결된 모든 언어 정보를 가져와서 적절한 메시지를 표시합니다. 

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
**설명:** 여기에서는 그룹화된 `if` 문 두 개를 중첩하여 사용하고 있습니다. 첫 번째 `if` 문은 `last_used_app_date`가 `nil`인지 확인하여 사용자가 세션을 시작했는지 확인합니다. 이는 사용자가 세션을 기록할 때 소프트웨어 개발 키트가 `{{${language}}}`를 자동으로 수집하기 때문입니다. 사용자가 세션을 기록하지 않은 경우 아직 해당 언어가 없으므로 언어 관련 커스텀 속성이 저장되어 있는지 확인하고 해당 정보를 바탕으로 가능한 경우 해당 언어로 메시지를 표시합니다.
{% endraw %}

두 번째 `if` 문은 사용자에게 `last_used_app_date`에 대한 `nil`이 없기 때문에 표준(기본값) 속성만 확인하며, 이는 사용자가 세션을 기록했고 해당 언어를 가지고 있다는 의미입니다.

{% alert note %}
[`Nil`](https://shopify.github.io/liquid/basics/types/#nil)은 Liquid 코드에 결과가 없을 때 반환되는 예약 변수입니다. `Nil`은 `if` 블록에서 `false`로 취급됩니다.
{% endalert %}

### 사용자가 마지막으로 앱을 연 시간에 따라 메시지 개인화하기 {#app-last-opened}

이 사용 사례는 사용자가 마지막으로 앱을 연 시간을 계산하여 경과 시간에 따라 다른 개인화된 메시지를 표시합니다.

{% raw %}
```liquid
{% assign last_used_date = {{${last_used_app_date}}} | date: "%s" %}
{% assign now = 'now' | date: "%s" %}
{% assign difference_in_days = {{now}} | minus: {{last_used_date}} | divided_by: 86400 %}
{% if {{difference_in_days}} < 3 %}
Happy to see you again!
{% else %}
It's been a while; here are some of our latest updates.
{% endif %}
```
{% endraw %}

### 사용자가 마지막으로 앱을 사용한 지 3일이 지나지 않은 경우 다른 메시지 표시하기 {#app-last-opened-less-than}

이 사용 사례는 사용자가 앱을 사용한 지 얼마나 되었는지 계산하고, 경과 시간에 따라 다른 개인화된 메시지를 표시합니다.

{% raw %}
```liquid
{% assign last_used_date = {{${last_used_app_date}}} | date: "%s" %}
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
- [설정된 시점부터 카운트다운 계산하기](#countdown-difference-days)
- [특정 배송 날짜 및 우선순위에 대한 카운트다운 만들기](#countdown-shipping-options)
- [일 단위로 카운트다운 만들기](#countdown-days)
- [일에서 시간, 분 단위로 카운트다운 만들기](#countdown-dynamic)
- [특정 날짜까지 남은 일수 표시](#countdown-future-date)
- [커스텀 날짜 속성이 도래할 때까지 남은 일수 표시](#countdown-custom-date-attribute)
- [남은 시간을 표시하고, 남은 시간이 X시간밖에 남지 않은 경우 메시지 중단하기](#countdown-abort-window)
- [사용자의 멤버십이 종료되기 X일 전에 보내는 인앱 메시지](#countdown-membership-expiry)
- [사용자의 날짜와 언어를 기반으로 인앱 메시지 개인화하기](#countdown-personalize-language)
- [지금부터 30일 후 날짜를 월과 일 형식으로 템플릿화하기](#countdown-template-date)

### 오늘 날짜에 x일 추가 {#countdown-add-x-days}

이 사용 사례는 현재 날짜에 특정 일수를 추가하여 메시지에서 참조하고 활용합니다. 예를 들어 주말에 해당 지역에서 열리는 이벤트를 보여주는 주중 메시지를 보낼 수 있습니다.

{% raw %}
```liquid
Here are the movies we're showing on {{ "now" | date:'%s' | plus:259200 | date:"%F" }}!
```
{% endraw %}

`plus` 값은 항상 초 단위이므로 초를 일 단위로 변환하기 위해 `%F` 필터로 마무리합니다.

{% alert important %}
메시지에 이벤트 목록에 대한 URL 또는 딥링크를 포함하면 사용자에게 향후 발생할 이벤트 목록으로 안내할 수 있습니다.
{% endalert %}

### 설정된 시점부터 카운트다운 계산하기 {#countdown-difference-days}

이 사용 사례는 특정 날짜와 현재 날짜 사이의 일수 차이를 계산합니다. 이 차이를 사용하여 사용자에게 카운트다운을 표시할 수 있습니다.

{% raw %}
```liquid
{% assign event_date = '2023-12-31' | date: "%s" %}
{% assign today = 'now' | date: "%s" %}
{% assign difference = event_date | minus: today %}
{% assign difference_days = difference | divided_by: 86400 %}
you have {{ difference_days }} days left!
```
{% endraw %}

### 특정 배송 날짜 및 우선순위에 대한 카운트다운 만들기 {#countdown-shipping-options}

이 사용 사례는 다양한 배송 옵션을 캡처하고, 수령까지 걸리는 시간을 계산하고, 특정 날짜까지 패키지를 수령할 수 있도록 사용자에게 구매를 권장하는 메시지를 표시합니다.

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

이 사용 사례는 특정 이벤트와 현재 날짜 사이에 남은 시간을 계산하고 이벤트까지 남은 일수를 표시합니다.

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
`date` 값이 있는 커스텀 속성 필드가 필요합니다.
{% endalert %}

### 일에서 시간, 분 단위로 카운트다운 만들기 {#countdown-dynamic}

이 사용 사례는 특정 이벤트와 현재 날짜 사이에 남은 시간을 계산합니다. 이벤트까지 남은 시간에 따라 시간 값(일, 시간, 분)을 변경하여 다양한 개인화된 메시지를 표시합니다.

예를 들어 고객의 주문이 도착할 때까지 이틀이 남았다면 "주문이 2일 후에 도착할 예정입니다."라고 말할 수 있습니다. 반면 하루 미만인 경우에는 "주문이 17시간 후에 도착합니다."로 변경할 수 있습니다.

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
`date` 값이 있는 커스텀 속성 필드가 필요합니다. 또한 시간을 일, 시간, 분 단위로 표시할 시간 임계값을 설정해야 합니다.
{% endalert %}

### 특정 날짜까지 남은 일수 표시 {#countdown-future-date}

이 사용 사례는 현재 날짜와 미래 이벤트 날짜의 차이를 계산하여 이벤트까지 며칠이 남았는지 알려주는 메시지를 표시합니다.

{% raw %}
```liquid
{% assign event_date = '2024-01-15' | date: "%s" %}
{% assign today = 'now' | date: "%s" %}
{% assign difference = event_date | minus: today %}
{% assign difference_days = difference | divided_by: 86400 %}
There are {{difference_days}} days until your birthday!
```
{% endraw %}

### 커스텀 날짜 속성이 도래할 때까지 남은 일수 표시 {#countdown-custom-date-attribute}

이 사용 사례는 현재 날짜와 미래 날짜 사이의 일수 차이를 계산하고 그 차이가 설정된 숫자와 일치하는 경우 메시지를 표시합니다.

이 예에서 사용자는 커스텀 날짜 속성으로부터 2일 이내에 메시지를 받게 됩니다. 그렇지 않으면 메시지가 전송되지 않습니다.

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

### 남은 시간을 표시하고 남은 시간이 X시간만 남은 경우 메시지 중단하기 {#countdown-abort-window}

이 사용 사례는 특정 날짜까지 남은 기간을 계산하고 그 기간에 따라(날짜가 너무 가까우면 메시징 건너뛰기) 다른 개인화된 메시지를 표시합니다. 

예를 들어, "런던행 티켓을 구매하려면 X시간이 남았습니다"라는 메시지를 보내되, 런던행 비행 시간까지 2시간 이내인 경우에는 메시지를 보내지 않습니다.

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

{% alert important %} 커스텀 이벤트 속성정보가 필요합니다. {% endalert %}

### 사용자 멤버십이 종료되기 x일 전에 보내는 인앱 메시지 {#countdown-membership-expiry}

이 사용 사례는 멤버십 만료 날짜를 캡처하고, 만료까지 남은 기간을 계산하며, 멤버십 만료까지 남은 기간에 따라 다른 메시지를 표시합니다.

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

### 사용자의 날짜와 언어를 기반으로 인앱 메시지 개인화하기 {#countdown-personalize-language}

이 사용 사례는 이벤트 카운트다운을 계산하고 사용자의 언어 설정에 따라 해당 언어로 카운트다운을 표시합니다.

예를 들어, 한 달에 한 번씩 사용자에게 업셀 메시지를 보내 오퍼의 유효 기간을 알려주는 인앱 메시지를 네 개 보낼 수 있습니다:

- 초기
- 2일 남음
- 1일 남음
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
`date` 값을 할당하고 지정된 날짜가 날짜 범위를 벗어나는 경우 중단 로직을 포함해야 합니다. 정확한 날짜 계산을 위해 할당된 종료 날짜에 23:59:59가 포함되어야 합니다.
{% endalert %}

### 지금부터 30일 후 날짜를 월과 일 형식으로 템플릿화하기 {#countdown-template-date}

이 사용 사례는 메시징에 사용할 30일 후 날짜를 표시합니다.

{% raw %}
```liquid
{% assign today = 'now' | date: "%s" %}
{% assign thirty_days = today | plus: 2592000 | date: "%B %d" %}
```
{% endraw %}

{% endapi %}

{% api %}

## 커스텀 속성

{% apitags %}
커스텀 속성
{% endapitags %}

- [일치하는 커스텀 속성을 기반으로 메시지 개인화하기](#attribute-matching)
- [두 개의 커스텀 속성을 빼서 차액을 금전적 가치로 표시하기](#attribute-monetary-difference)
- [사용자의 전체 이름이 first_name 필드에 저장되어 있는 경우 사용자의 이름 참조하기](#attribute-first-name)

### 일치하는 커스텀 속성을 기반으로 메시지 개인화하기 {#attribute-matching}

이 사용 사례는 사용자에게 특정 커스텀 속성이 있는지 확인하고, 있다면 다른 개인화된 메시지를 표시합니다. 

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

### 두 개의 커스텀 속성을 빼서 차액을 금전적 가치로 표시하기 {#attribute-monetary-difference}

이 사용 사례는 두 개의 화폐 커스텀 속성을 캡처한 다음 그 차이를 계산하고 표시하여 사용자에게 목표에 도달하기까지 얼마나 남았는지 알려줍니다.

{% raw %}
```liquid
{% assign event_goal = {{custom_attribute.${last_selected_event_personal_goal}}} %}
{% assign current_raised =  {{custom_attribute.${last_selected_event_personal_amount_raised}}} %}
{% assign difference =  event_goal | minus: current_raised %}
You only have ${{ difference | round: 0 | number_with_delimiter }} left to raise!
```
{% endraw %}

### 사용자의 전체 이름이 first_name 필드에 저장되어 있는 경우 사용자의 이름 참조하기 {#attribute-first-name}

이 사용 사례는 사용자의 이름(이름과 성이 모두 단일 필드에 저장되어 있는 경우)을 캡처한 다음 이 이름을 사용하여 환영 메시지를 표시합니다.

{% raw %}
```liquid
{{${first_name} | truncatewords: 1, "" | default: 'hi'}}
{% assign name = {{${first_name}}} | split: ' ' %}
Hi {{name[0]}}, here's your message!
```

**설명:** `split` 필터는 `{{${first_name}}}`에 있는 문자열을 배열로 변환합니다. `{{name[0]}}`을 사용하면 배열의 첫 번째 항목, 즉 사용자의 이름만 참조합니다. 

{% endraw %}
{% endapi %}

{% api %}

## 커스텀 이벤트

{% apitags %}
커스텀 이벤트
{% endapitags %}

- [커스텀 이벤트가 현재로부터 2시간 이내인 경우 푸시 알림 중단하기](#event-abort-push)
- [사용자가 커스텀 이벤트를 세 번 수행할 때마다 캠페인 보내기](#event-three-times)
- [한 카테고리에서만 구매한 사용자에게 메시지 보내기](#event-purchased-one-category)
- [지난 한 달 동안 커스텀 이벤트가 발생한 횟수 추적하기](#track)


### 커스텀 이벤트가 현재로부터 2시간 이내인 경우 푸시 알림 중단하기 {#event-abort-push}

이 사용 사례는 이벤트까지 남은 시간을 계산하고 남은 시간에 따라 다양한 개인화된 메시지를 표시합니다.

예를 들어 커스텀 이벤트 속성정보가 향후 2시간 이내에 도래하면 푸시가 발송되지 않도록 설정할 수 있습니다. 이 예제에서는 기차표에 대한 유기한 장바구니 시나리오를 사용합니다.

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

### 사용자가 커스텀 이벤트를 세 번 수행할 때마다 캠페인 보내기 {#event-three-times}

이 사용 사례는 사용자가 커스텀 이벤트를 세 번 수행했는지 확인하고, 수행한 경우 메시지를 표시하거나 캠페인을 전송합니다. 

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

{% alert important %} 커스텀 이벤트 수의 이벤트 속성정보가 있거나 Braze 엔드포인트에 대한 웹훅을 사용해야 합니다. 이는 사용자가 이벤트를 수행할 때마다 커스텀 속성(`example_event_count`)을 증가시키기 위한 것입니다. 이 예에서는 3의 케이던스(1, 4, 7, 10 등)를 사용합니다. 케이던스를 0(0, 3, 6, 9 등)에서 시작하려면 `minus: 1`을 제거합니다.
{% endalert %}

### 한 카테고리에서만 구매한 사용자에게 메시지 보내기 {#event-purchased-one-category}

이 사용 사례는 사용자가 구매한 카테고리의 목록을 캡처하며, 구매 카테고리가 하나만 존재하는 경우 메시지를 표시합니다.

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

### 지난 한 달 동안 커스텀 이벤트가 발생한 횟수 추적하기 {#track}

이 사용 사례는 현재 월 1일부터 전월 사이에 커스텀 이벤트가 기록된 횟수를 계산합니다. 그런 다음 users/track 호출을 실행하여 이 값을 커스텀 속성으로 업데이트하고 저장할 수 있습니다. 이 캠페인은 두 달 연속으로 실행되어야 월별 데이터를 사용할 수 있습니다.

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

- [다른 언어로 월 이름 표시하기](#language-display-month)
- [사용자의 언어에 따라 이미지 표시하기](#language-image-display)
- [요일 및 사용자 언어에 따라 메시징 개인화하기](#language-personalize-message)

### 다른 언어로 월 이름 표시하기 {#language-display-month}

이 사용 사례는 현재 날짜, 월, 연도를 표시하며 월은 다른 언어로 표시됩니다. 제공된 예는 스웨덴어를 사용합니다.

{% raw %}
```liquid
{% assign day = 'now' | date: "%e" %}
{% assign year =  'now' | date: "%Y" %}
{% assign month =  'now' | date: "%B" %}

{% if {{month}} == 'January' %}
{{day}} Januari {{year}}
{% elsif {{month}} == 'February' %}
{{day}} Februari {{year}}
{% elsif {{month}} == 'March' %}
{{day}} Mars {{year}}
{% elsif {{month}} == 'April' %}
{{day}} April {{year}}
{% elsif {{month}} == 'May' %}
{{day}} Maj {{year}}
{% elsif {{month}} == 'June' %}
{{day}} Juni {{year}}
{% elsif {{month}} == 'July' %}
{{day}} Juli {{year}}
{% elsif {{month}} == 'August' %}
{{day}} Augusti {{year}}
{% elsif {{month}} == 'September' %}
{{day}} September {{year}}
{% elsif {{month}} == 'October' %}
{{day}} Oktober {{year}}
{% elsif {{month}} == 'November' %}
{{day}} November {{year}}
{% elsif {{month}} == 'December' %}
{{day}} December {{year}}
{% endif %}
```
{% endraw %}

### 사용자의 언어에 따라 이미지 표시하기 {#language-image-display}

이 사용 사례는 사용자의 언어를 기반으로 이미지를 표시합니다. 이 사용 사례는 Braze 미디어 라이브러리에 업로드된 이미지로만 테스트되었습니다.

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

### 요일 및 사용자 언어에 따라 메시징 개인화하기 {#language-personalize-message}

이 사용 사례는 현재 요일을 확인하고, 요일에 따라 사용자의 언어가 제공된 언어 옵션 중 하나로 설정되어 있는 경우 해당 언어로 특정 메시지를 표시합니다.

제공된 예는 화요일까지만 포함되어 있지만 각 요일에 대해 반복할 수 있습니다.

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

- [마케팅 이메일을 차단한 고객에게 이메일 보내지 않기](#misc-avoid-blocked-emails)
- [고객의 구독 상태를 사용하여 메시지 콘텐츠 개인화하기](#misc-personalize-content)
- [문자열에 있는 모든 단어의 첫 글자를 대문자로 표기하기](#misc-capitalize-words-string)
- [커스텀 속성 값을 배열과 비교하기](#misc-compare-array)
- [예정된 이벤트 미리 알림 만들기](#misc-event-reminder)
- [배열 내에서 문자열 찾기](#misc-string-in-array)
- [배열에서 가장 큰 값 찾기](#misc-largest-value)
- [배열에서 가장 작은 값 찾기](#misc-smallest-value)
- [문자열의 끝 부분 쿼리하기](#misc-query-end-of-string)
- [여러 조합으로 커스텀 속성에서 배열의 값 쿼리하기](#misc-query-array-values)
- [문자열을 전화번호 형식으로 지정하기](#phone-number)

### 마케팅 이메일을 차단한 고객에게 이메일 보내지 않기 {#misc-avoid-blocked-emails}

이 사용 사례는 콘텐츠 블록에 저장된 차단된 사용자 목록을 가져와 차단된 사용자가 향후 캠페인이나 캔버스에서 커뮤니케이션을 받거나 타겟팅되지 않도록 합니다.

{% alert important %}
이 Liquid를 사용하려면 먼저 차단된 이메일 목록을 콘텐츠 블록에 저장하세요. 목록에는 이메일 주소 사이에 추가 공백이나 문자가 삽입되지 않아야 합니다(예: `test@braze.com,abc@braze.com`).
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

**설명:** 여기에서 차단된 이메일의 콘텐츠 블록을 참조하여 잠재적 수신자의 이메일이 이 목록에 있는지 확인합니다. 이메일이 발견되면 메시지가 전송되지 않습니다.

{% alert note %}
콘텐츠 블록의 크기 제한은 5MB입니다.
{% endalert %}

### 고객의 구독 상태를 사용하여 메시지 콘텐츠 개인화하기 {#misc-personalize-content}

이 사용 사례는 고객의 구독 상태를 사용하여 개인화된 콘텐츠를 전송합니다. 특정 구독 그룹에 가입한 고객에게는 이메일 구독 그룹 전용 메시지가 전송됩니다.

{% raw %}
```liquid
{% if {{subscribed_state.${subscription_group_id}}} == 'subscribed' %}
This is an exclusive message for subscribed users!
{% else %} This is the default message for other users.
{% endif %}
```
{% endraw %}

### 문자열에 있는 모든 단어의 첫 글자를 대문자로 표기하기 {#misc-capitalize-words-string}

이 사용 사례는 단어 문자열을 가져와 배열로 분할하고 각 단어의 첫 글자를 대문자로 표시합니다.

{% raw %}
```liquid
{% assign words_array = {{custom_attribute.${address}}} | split: ' ' %}
{% for words in {{words_array}} %}
{{ words | capitalize | append: ' ' }}
{% endfor %} 
```
{% endraw %}

**설명:** 여기서는 선택한 문자열 속성에 변수를 할당하고 `split` 필터를 사용하여 문자열을 배열로 분할했습니다. 그런 다음 `for` 태그를 사용하여 새로 만든 배열의 각 항목에 `words` 변수를 할당하고 `capitalize` 필터와 `append` 필터를 사용하여 각 용어 사이에 공백을 추가하여 해당 단어를 표시했습니다.

### 커스텀 속성 값을 배열과 비교하기 {#misc-compare-array}

이 사용 사례는 즐겨찾는 스토어 목록을 가져와서 사용자가 즐겨찾는 스토어가 목록에 있는지 확인하고, 있다면 해당 스토어에서 제공하는 특별 행사를 표시합니다.

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

{% alert important %} 이 시퀀스에는 기본 조건문에 `break` 태그가 있습니다. 이렇게 하면 일치하는 항목이 발견되면 루프가 중지됩니다. 일치하는 항목을 많이 또는 모두 표시하려면 `break` 태그를 제거하세요. {% endalert %}

### 예정된 이벤트 미리 알림 만들기 {#misc-event-reminder}

이 사용 사례를 통해 사용자는 커스텀 이벤트를 기반으로 예정된 미리 알림을 설정할 수 있습니다. 예시 시나리오에서는 사용자가 26일 이상 남은 보험 갱신 날짜에 대한 미리 알림을 설정하여 보험 갱신 날짜 26일, 13일, 7일 또는 2일 전에 미리 알림을 보낼 수 있습니다.

이 사용 사례에서는 [웹훅 캠페인]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) 또는 캔버스 단계의 본문에 다음이 포함되어야 합니다.

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