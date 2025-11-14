---
nav_title: 기본값 설정하기
article_title: 기본값 Liquid 설정하기
page_order: 5
description: "이 참조 문서에서는 메시징에 사용하는 개인화 속성에 대한 기본 대체 값을 설정하는 방법을 다룹니다."

---

# 기본값 설정하기

{% raw %}

> 메시징에 사용하는 모든 개인화 속성에 대해 기본 대체 값을 설정할 수 있습니다. 이 문서에서는 기본값의 작동 방식, 설정 방법 및 메시징에서 기본값을 사용하는 방법에 대해 설명합니다.

## 작동 방식

기본값은 [Liquid 필터](http://docs.shopify.com/themes/liquid-documentation/filters) (그림과 같이 필터를 인라인으로 구분하려면 `|` 사용)를 "default"라는 이름으로 지정하여 추가할 수 있습니다.

```
| default: 'Insert Your Desired Default Here'
```

기본값이 제공되지 않고 필드가 누락되었거나 사용자에게 설정되지 않은 경우 메시징에서 필드가 비워집니다.

다음 예는 기본값을 추가하는 올바른 구문을 보여줍니다. 이 경우 사용자의 `first_name` 필드가 비어 있거나 사용할 수 없는 경우 "Valued User"라는 단어가 `{{ ${first_name} }}` 속성을 대체합니다.

```liquid
Hi {{ ${first_name} | default: 'Valued User' }}, thanks for using the App!
```

신원 미상의 사용자에게는 이 메시지가 다음과 같이 표시됩니다:

```
Hi Janet, thanks for using the App!
```

아니면...

```
Hi Valued User, thanks for using the App!
```
{% endraw %}

{% alert important %}
빈 값에는 기본값이 표시되지만 빈 값에는 기본값이 표시되지 않습니다. 빈 값은 아무 것도 포함하지 않는 반면, 공백 값은 공백과 같은 공백 문자를 포함하며 다른 문자는 포함하지 않습니다. 예를 들어 빈 문자열은 `""` 처럼 보일 수 있고 빈 문자열은 `" "` 처럼 보일 수 있습니다.
{% endalert %}

## 다양한 데이터 유형에 대한 기본값 설정하기

위의 예는 문자열의 기본값을 설정하는 방법을 보여줍니다. 문자열, 부울 값, 배열, 오브젝트, 숫자 등 `empty`, `nil` (정의되지 않음) 또는 `false` 의 값을 갖는 모든 Liquid 데이터 유형에 대해 기본값을 설정할 수 있습니다.

### 사용 사례: 부울

`premium_user` 이라는 부울 커스텀 속성이 있고 사용자의 프리미엄 상태에 따라 개인화된 메시지를 보내려고 한다고 가정해 보겠습니다. 일부 사용자는 프리미엄 상태가 설정되어 있지 않으므로 이러한 사용자를 캡처하려면 기본값을 설정해야 합니다.

1. 기본값이 `false` 인 `premium_user` 속성에 `is_premium_user` 이라는 변수를 할당합니다. 즉, `premium_user` 가 `nil` 인 경우 `is_premium_user` 의 기본값은 `false` 입니다. 

{% raw %}
```liquid
{% assign is_premium_user = {{custom_attribute.${premium_user}}} | default: false %}
```

{: start="2"}
2\. 그런 다음 조건 로직을 사용하여 `is_premium_user` 가 `true` 일 경우 전송할 메시지를 지정합니다. 즉, `premium_user` 이 `true` 인 경우 전송할 내용입니다. 또한 사용자 이름이 없는 경우를 대비하여 사용자 이름에 기본값을 지정할 수도 있습니다.

```liquid
{% if is_premium_user %}
Hi {{${first_name} | default: 'premium user'}}, thank you for being a premium user!
```

{: start="3"}
3\. 마지막으로 `is_premium_user` 가 `false` 인 경우(즉, `premium_user` 가 `false` 또는 `nil` 인 경우) 어떤 메시지를 보낼지 지정합니다. 그런 다음 조건 로직을 닫습니다.

```liquid
{% else %}
Hi {{${first_name} | default: 'valued user'}}, consider upgrading to premium for more benefits!
{% endif %}
```
{% endraw %}

{% details Full Liquid code %}
{% raw %}
```liquid
{% assign is_premium_user = {{custom_attribute.${premium_user}}} | default: false %}
{% if is_premium_user %}
Hi {{${first_name} | default: 'premium user'}}, thank you for being a premium user!
{% else %}
Hi {{${first_name} | default: 'valued user'}}, consider upgrading to premium for more benefits!
{% endif %}
```
{% endraw %}
{% enddetails %}

### 사용 사례: 숫자

`reward_points` 이라는 숫자 커스텀 속성이 있고 사용자의 리워드 포인트가 포함된 메시지를 보내려고 한다고 가정해 보겠습니다. 일부 사용자는 보상 포인트가 설정되어 있지 않으므로 이러한 사용자를 고려한 기본값을 설정해야 합니다.

1. 사용자의 이름 또는 이름을 모르는 경우 기본값인 `Valued User` 으로 메시지를 시작하세요.

{% raw %}
```liquid
Hi {{${first_name} | default: 'valued user'}},
```
{% endraw %}

{: start="2"}
2\. `reward_points` 라는 커스텀 속성을 사용하고 기본값 `0` 을 사용하여 사용자가 보유한 리워드 포인트 수로 메시지를 끝냅니다. `reward_points` 값이 `nil` 인 모든 사용자는 메시징에 `0` 보상 포인트를 받게 됩니다.

{% raw %}
```liquid
Hi {{${first_name} | default: 'valued user'}}, you have {{custom_attribute.${reward_points} | default: 0}} reward points.
```
{% endraw %}

### 사용 사례: 개체

`city` 및 `state` 속성을 포함하는 `location` 라는 중첩된 고객 속성 오브젝트가 있다고 가정해 보겠습니다. 이러한 속성이 설정되어 있지 않은 경우 사용자에게 속성을 제공하도록 권장할 수 있습니다.

1. 사용자의 이름으로 호칭하고 이름을 모르는 경우 기본값을 입력합니다.

{% raw %}
```liquid
Hi {{${first_name} | default: 'valued user'}},
```
{% endraw %}

{: start="2"}
2\. 사용자의 위치를 확인하겠다는 메시지를 작성합니다.

{% raw %}
```liquid
We'd like to confirm the location associated with your account. We use this location to send you promotions and offers for stores nearest you. You can update your location in your profile settings.
```
{% endraw %}

{: start="3"}
3\. 메시지에 사용자의 위치를 삽입하고 주소 속성이 설정되지 않은 경우에 대한 기본값을 지정합니다.

{% raw %}
```liquid
Your location:
City: {{custom_attribute.${address.city} | default: 'Unknown'}}
State: {{custom_attribute.${address.state} | default: 'Unknown'}}
```
{% endraw %}

{% details Full Liquid code %}
{% raw %}
```liquid
Hi {{${first_name} | default: 'valued user'}}

We'd like to confirm the location associated with your account. We use this location to send you promotions and offers for stores nearest you. You can update your location in your profile settings.

Your location:
City: {{custom_attribute.${address.city} | default: 'Unknown'}}
State: {{custom_attribute.${address.state} | default: 'Unknown'}}
```
{% endraw %}
{% enddetails %}

### 사용 사례: 배열

`destination` 및 `departure_date` 속성을 가진 트립을 포함하는 `upcoming_trips` 이라는 배열 커스텀 속성이 있다고 가정해 보겠습니다. 사용자에게 예약된 여행이 있는지 여부에 따라 개인화된 메시지를 보내려고 합니다.

1. `upcoming_trips` 가 `empty` 인 경우 메시지를 보내지 않도록 지정하는 조건 로직을 작성합니다.

{% raw %}
```liquid
{% if {{custom_attribute.${upcoming_trips}}} == empty %}
{% abort_message('No upcoming trips scheduled') %}
```
{% endraw %}

{: start="2"}
2\. `upcoming_trips` 에 콘텐츠가 있는 경우 전송할 메시지를 지정합니다:<br><br>**2a.** 사용자의 주소를 입력하고 이름을 모르는 경우 기본값을 입력합니다. <br>**2b.** `for` 태그를 사용하여 `upcoming_trips` 에 포함된 각 여행에 대한 속성(또는 정보)을 가져오도록 지정합니다. <br>**2c.** 메시징에 속성을 나열하고 `departure_date` 이 설정되지 않은 경우 기본값을 포함하세요. (예를 들어 여행을 생성하려면 `destination` 이 필요하므로 기본값을 설정할 필요가 없습니다).<br>**2d.** `for` 태그를 닫은 다음 조건 로직을 닫습니다.

{% raw %}
```liquid
{% else %}
Hello {{${first_name} | default: 'fellow traveler'}},
  Here are your upcoming trips:
  <ul>
  {% for trip in {{custom_attribute.${upcoming_trips}}} %}
    <li>
      Destination: {{trip.destination}}
      Departure Date: {{trip.departure_date | default: 'Date not set'}}
    </li>
  {% endfor %}
  </ul>
{% endif %}
```
{% endraw %}

{% details Full Liquid code %}
{% raw %}
```liquid
{% if {{custom_attribute.${upcoming_trips}}} == blank %}
{% abort_message('No upcoming trips scheduled') %}
{% else %}
Hello {{${first_name} | default: 'fellow traveler'}},
  Here are your upcoming trips:
  <ul>
  {% for trip in {{custom_attribute.${upcoming_trips}}} %}
    <li>
      Destination: {{trip.destination}}
      Departure Date: {{trip.departure_date | default: 'Date not set'}}
    </li>
  {% endfor %}
  </ul>
{% endif %}
```
{% endraw %}
{% enddetails %}

[31]:https://docs.shopify.com/themes/liquid/tags/variable-tags
[32]:https://docs.shopify.com/themes/liquid/tags/iteration-tags
[37]:#accounting-for-null-attribute-values
