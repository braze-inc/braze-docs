---
nav_title: 조건부 메시징 로직
article_title: 조건부 리퀴드 메시징 로직
page_order: 6
description: "이 참조 문서에서는 캠페인에서 태그를 사용할 수 있는 방법과 사용해야 하는 방법에 대해 설명합니다."

---

# 조건부 메시징 로직

> [태그를](https://docs.shopify.com/themes/liquid-documentation/tags) 사용하면 메시징 캠페인에 프로그래밍 로직을 포함할 수 있습니다. 태그는 조건문을 실행하는 데 사용할 수 있을 뿐만 아니라 변수 할당이나 코드 블록을 반복하는 등의 고급 사용 사례에도 사용할 수 있습니다. <br><br>이 페이지에서는 null, nil 및 빈 속성 값을 처리하는 방법, 커스텀 속성을 참조하는 방법 등 태그를 사용할 수 있는 방법과 사용해야 하는 방법을 설명합니다.

## 태그 서식 지정

{% raw %}
태그는 `{% %}`로 묶어야 합니다.
{% endraw %}

조금 더 쉽게 사용할 수 있도록 Braze에는 Liquid 구문을 올바르게 포맷한 경우 녹색과 보라색으로 활성화되는 색상 포맷이 포함되어 있습니다. 녹색 서식은 태그를 식별하는 데 도움이 되며 보라색 서식은 개인화가 포함된 영역을 강조 표시합니다.

조건부 메시징을 사용하는 데 어려움이 있다면 사용자 지정 속성 및 기타 Liquid 요소를 삽입하기 전에 조건부 구문을 작성해 보세요.

예를 들어 메시지 필드에 먼저 다음을 추가합니다:  
{% raw %}
```liquid
{% if X >0 %}
{% else %}
{% endif %}
```

녹색으로 강조 표시되었는지 확인한 다음 메시지 필드 모서리에 있는 파란색 `+`를 사용하여 `X`를 선택한 Liquid 또는 연결된 콘텐츠로 바꾸고 `0`을 원하는 값으로 바꿉니다.
<br><br>
그런 다음 `else` 조건문 사이에 필요에 따라 메시지 변형을 추가합니다:
```liquid
{% if {{custom_attribute.${total_spend}}} >0 %}
Thanks for purchasing! Here's another 10% off!
{% else %}
Buy now! Would 5% off convince you?
{% endif %}
```
{% endraw %}

## 조건부 논리

조건문과 같은 다양한 유형의 [지능형 로직을 메시지 내에](http://docs.shopify.com/themes/liquid-documentation/basics) 포함할 수 있습니다. 다음 예에서는 [조건문을](http://docs.shopify.com/themes/liquid-documentation/tags/control-flow-tags) 사용하여 캠페인을 국제화합니다:
{% raw %}

```liquid
{% if ${language} == 'en' %}
This is a message in English from Braze!
{% elsif ${language} == 'es' %}
Este es un mensaje en español de Braze !
{% elsif ${language} == 'zh' %}
这是一条来自Braze的中文消息。
{% else %}
This is a message from Braze! This is going to go to anyone who did not match the other specified languages!
{% endif %}
```

### Conditional tags

#### `if` and `elsif`

Conditional logic begins with the `if` tag, which states the first condition to check. Subsequent conditions use the `elsif` tag and will be checked if the previous conditions are not met. In this example, if a user's device isn't set to English, this code will check to see if the user's device is set to Spanish, and if that fails, it will check if the device is set to. 사용자의 기기가 이러한 조건 중 하나를 충족하면 해당 언어로 된 메시징을 받게 됩니다.

#### `else`

조건부 논리에 `{% else %}` 문을 포함할 수 있습니다. If none of the conditions that you set are met, the `{% else %}` statement specifies the message that should be sent. In this example, we default to English if a user’s language is not English, Spanish, or Chinese.

#### `endif`

`{% endif %}` 태그는 조건 로직을 완료했음을 알립니다. 조건 로직이 있는 모든 메시징에는 `{% endif %}` 태그를 포함해야 합니다. 조건 로직에 `{% endif %}` 태그를 포함하지 않으면 Braze가 메시지를 구문 분석할 수 없으므로 오류가 발생합니다.

### Tutorial: Deliver location-based content

When you're finished with this tutorial, you'll be able to use tags with "if", "elsif", and "else" statements to deliver content based on a user's location.

1. Begin with an `if` tag to establish what message should be sent when the user's city is in New York. If the user's city is New York, this first condition is met and the user will receive a message specifying their New Yorker identity.

```liquid
{% if ${city} == "New York" %}
  🎉 Hey there, New Yorker! We're excited to offer you a special deal! 
  Get 20% off your next sandwich at your local Sandwich Emperor. 
  Just show this message at the counter to redeem your offer!
```

{: start="2"}
2\. Next, use the `elseif` tag to establish what message should be sent if the user's city is in Los Angeles.

```liquid
{% elsif ${city} == "Los Angeles" %}
  🌞 Hello, Los Angeles! Enjoy a sunny day with a delicious sandwich! 
  Present this message at our LA restaurant for a 20% discount on your next order!
```

{: start="3"}
3\. Let's use another `elseif` tag to establish what message should be sent if the user's city is in Chicago.

```liquid
{% elsif ${city} == "Chicago" %}
  🍕 Chicago, we have a treat for you! 
  Swing by our restaurant and get 20% off your favorite sandwich. 
  Just show this message to our staff!
```

{: start="4"}
4\. Now, let's use the `{% else %}` tag to specify what message should be sent if the user's city isn't in San Francisco, New York, or Chicago.

```liquid
{% else %}
 🥪 Craving a sandwich? Visit us at any of our locations for a delicious meal! 
  Check our website for the nearest restaurant to you!
```

{: start="5"}
5\. Finally, we'll use the `{% endif %}` tag to specify that our conditional logic is done.

```liquid
{% endif %}
```

{% endraw %}

{% details Full Liquid code %}

{% raw %}
```liquid
{% if ${city} == "New York City" %}
  🎉 Hey there, New Yorker! We're excited to offer you a special deal! 
  Get 20% off your next sandwich at our New York location. 
  Just show this message at the counter to redeem your offer!
{% elsif ${city} == "Los Angeles" %}
  🌞 Hello, Los Angeles! Enjoy a sunny day with a delicious sandwich! 
  Present this message at our LA restaurant for a 20% discount on your next order!
{% elsif ${city} == "Chicago" %}
  🍕 Chicago, we have a treat for you! 
  Swing by our restaurant and get 20% off your favorite sandwich. 
  Just show this message to our staff!
{% else %}
  🥪 Craving a sandwich? Visit us at any of our locations for a delicious meal! 
  Check our website for the nearest restaurant to you!
{% endif %}
```
{% endraw %}

{% enddetails %}

## null, nil 및 빈 속성 값에 대한 설명

조건 로직은 고객 프로필에 설정되지 않은 속성 값을 설명하는 데 유용한 방법입니다.

### Null 및 nil 속성 값

커스텀 속성의 값이 설정되지 않은 경우 null 또는 nil 값이 발생합니다. 예를 들어 아직 이름을 설정하지 않은 사용자는 Braze에 이름이 로그인되지 않습니다.

경우에 따라 이름 설정이 있는 사용자와 이름 설정이 없는 사용자에게 완전히 다른 메시지를 보내야 할 수도 있습니다.

다음 태그를 사용하면 '이름' 속성이 null인 사용자에 대한 메시지를 지정할 수 있습니다:

{% raw %}
```liquid
{% if ${first_name} == null %}
  ....
{% endif %}
```
{% endraw %} 

!['이름' 속성이 널인 Braze 대시보드의 메시지 예시입니다.]({% image_buster /assets/img/value_null.png %}){: style="max-width:60%;"}

{% raw %}
```liquid
{% if ${first_name} == null %}
We're having a sale! Hurry up and get 10% off all items today only!
{% else %}
Hey {{${first_name} | default: 'there'}}, we're having a sale! Hurry up and get 10% off all items today only!
{% endif %}
```

null 속성 값은 값 유형과 엄격하게 연관되지 않으므로(예: "null" 문자열은 "null" 배열과 동일) 위의 예에서 null 속성 값은 설정되지 않은 이름(문자열)을 참조하고 있다는 점에 유의하세요.

{% endraw %}

### 빈 속성 값

빈 값은 고객 프로필의 속성이 설정되어 있지 않거나 공백 문자열(` `)로 설정되어 있거나 `false`로 설정된 경우 발생합니다. 빈 값은 다른 변수보다 먼저 확인하여 리퀴드 처리 오류를 방지해야 합니다.

다음 태그를 사용하면 "이름" 속성이 비어 있는 사용자에 대한 메시지를 지정할 수 있습니다.

{% raw %}
```liquid
{% if ${first_name} == blank %}
  ....
{% endif %}
```
{% endraw %} 

## 사용자 지정 속성 참조

[사용자 지정 속성을 생성한]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#managing-custom-attributes) 후에는 Liquid 메시징에서 이러한 사용자 지정 속성을 참조할 수 있습니다.

조건 로직을 사용할 때는 올바른 구문을 사용하고 있는지 확인하려면 커스텀 속성의 데이터 유형을 알아야 합니다. 대시보드의 **사용자 지정** 속성 페이지에서 사용자 지정 속성과 연결된 데이터 유형을 찾은 다음 각 데이터 유형에 대해 나열된 다음 예제를 참조합니다.

![사용자 지정 속성에 대한 데이터 유형을 선택합니다. 제공된 예는 데이터 유형이 문자열인 Favorite_Category 속성을 보여줍니다.]({% image_buster /assets/img_archive/custom_attribute_data_type.png %}){: style="max-width:80%;"}

{% alert tip %}
문자열과 배열에는 직선 아포스트로피가 필요하지만 부울과 정수에는 아포스트로피가 없습니다.
{% endalert %}

#### 부울

[부울은]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#booleans) 이진 값이며 `true` 또는 `false`, 예: `registration_complete: true` 로 설정할 수 있습니다. 부울 값에는 아포스트로피가 없습니다.

{% raw %}

```liquid
{% if {{custom_attribute.${registration_complete}}} == true %}
```

{% endraw %}

#### 숫자

[숫자는]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#numbers) 정수 또는 실수일 수 있는 숫자 값입니다. 예를 들어, 사용자는 `shoe_size: 10` 또는 `levels_completed: 287`을 가질 수 있습니다. 숫자 값에는 아포스트로피가 없습니다.

{% raw %}

```liquid
{% if {{custom_attribute.${shoe_size}}} == 10 %}
```

{% endraw %}

정수의 경우 (<) 미만 또는 (>)보다 큰 값과 같은 다른 [기본 연산자를](https://shopify.dev/docs/themes/liquid/reference/basics/operators) 사용할 수도 있습니다:

{% raw %}

```liquid
{% if {{custom_attribute.${flyer_miles}}} >= 500 %}
```

{% endraw %}

#### 문자열

[문자열은]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#strings) 영숫자로 구성되며 사용자에 대한 데이터를 저장합니다. 예를 들어 `favorite_color: red` 또는 `phone_number: 3025981329`가 있을 수 있습니다. 문자열 값 주위에 아포스트로피를 붙여야 합니다.

{% raw %}

```liquid
{% if {{custom_attribute.${favorite_color}}} == 'blue' %}
```

{% endraw %}

문자열의 경우 Liquid에서 "==" 또는 "contains"를 모두 사용할 수 있습니다.

#### 배열

[배열은]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#arrays) 사용자에 대한 정보의 목록입니다. 예를 들어 사용자가 `last_viewed_shows: stranger things, planet earth, westworld`를 가질 수 있습니다. 배열 값은 주위에 아포스트로피를 포함해야 합니다.

{% raw %}

```liquid
{% if {{custom_attribute.${last_viewed_shows}}} contains 'homeland' %}
```

{% endraw %}

배열의 경우 "contains"를 사용해야 하며 "=="는 사용할 수 없습니다. 

#### Time

이벤트가 발생한 시점의 타임스탬프입니다. 조건부 논리에 사용하려면 [시간]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#time) 값에 [수학 필터가]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/filters/#math-filters) 있어야 합니다.

{% raw %}

```liquid
{% assign expire = {{custom_attribute.${subscription_end_date}}} | plus: 0 %} 
```

{% endraw %}


