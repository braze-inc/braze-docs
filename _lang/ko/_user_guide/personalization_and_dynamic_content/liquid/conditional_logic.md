---
nav_title: 조건부 메시징 로직
article_title: 조건부 Liquid 메시징 로직
page_order: 6
description: "이 참조 문서에서는 태그를 캠페인에서 어떻게 사용하고 사용해야 하는지에 대해 다룹니다."

---

# 조건부 메시징 로직

> [태그](https://docs.shopify.com/themes/liquid-documentation/tags)는 메시징 캠페인에 프로그래밍 로직을 포함할 수 있게 해줍니다. 태그는 조건문을 실행하는 데 사용될 수 있으며, 변수 할당이나 코드 블록 반복과 같은 고급 사용 사례에도 사용될 수 있습니다. <br><br>이 페이지에서는 태그를 어떻게 사용하고 사용해야 하는지, null, nil 및 빈 속성 값을 어떻게 처리하는지, 사용자 정의 속성을 참조하는 방법에 대해 다룹니다.

## 태그 형식 지정

{% raw %}
태그는 `{% %}`로 감싸야 합니다.
{% endraw %}

당신의 삶을 조금 더 쉽게 만들기 위해, Braze는 Liquid 구문을 올바르게 형식화했을 경우 초록색과 보라색으로 활성화되는 색상 형식을 포함했습니다. 초록색 형식은 태그를 식별하는 데 도움이 되며, 보라색 형식은 개인화가 포함된 영역을 강조합니다.

조건부 메시징을 사용하는 데 어려움이 있다면, 사용자 정의 속성과 다른 Liquid 요소를 삽입하기 전에 조건부 구문을 작성해 보세요.

예를 들어, 먼저 메시지 필드에 다음을 추가하세요:  
{% raw %}
```liquid
{% if X >0 %}
{% else %}
{% endif %}
```

초록색으로 강조 표시되는지 확인한 후, 메시지 필드 모서리의 파란색 `+`를 사용하여 `X`을 선택한 Liquid 또는 연결된 콘텐츠로 교체하고, `0`을 원하는 값으로 교체하세요.
<br><br>
그런 다음, 필요에 따라 `else` 조건부 사이에 메시지 변형을 추가하세요:
```liquid
{% if {{custom_attribute.${total_spend}}} >0 %}
Thanks for purchasing! Here's another 10% off!
{% else %}
Buy now! Would 5% off convince you?
{% endif %}
```
{% endraw %}

## 조건부 로직

메시지 내에 많은 유형의 [지능형 로직](http://docs.shopify.com/themes/liquid-documentation/basics)을 포함할 수 있으며, 조건문과 같은 것입니다. 다음 예제는 캠페인을 국제화하기 위해 [조건부](http://docs.shopify.com/themes/liquid-documentation/tags/control-flow-tags)를 사용합니다:
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

### 조건부 태그

#### `if`과 `elsif`

조건 논리는 첫 번째 조건을 확인하는 `if` 태그로 시작됩니다. 후속 조건은 `elsif` 태그를 사용하며 이전 조건이 충족되지 않을 경우 확인됩니다. 이 예제에서 사용자의 장치가 영어로 설정되어 있지 않으면 이 코드는 사용자의 장치가 스페인어로 설정되어 있는지 확인하고, 실패할 경우 장치가 설정되어 있는지 확인합니다. 사용자의 장치가 이러한 조건 중 하나를 충족하면 사용자는 관련 언어로 메시지를 받게 됩니다.

#### `else`

조건 논리에 `{% else %}` 문을 포함할 수 있는 옵션이 있습니다. 설정한 조건이 충족되지 않으면 `{% else %}` 문이 전송해야 할 메시지를 지정합니다. 이 예제에서는 사용자의 언어가 영어, 스페인어 또는 중국어가 아닐 경우 기본적으로 영어로 설정됩니다.

#### `endif`

`{% endif %}` 태그는 조건 논리를 마쳤음을 알립니다. 조건 논리가 있는 모든 메시지에 `{% endif %}` 태그를 포함해야 합니다. 조건 논리에 `{% endif %}` 태그를 포함하지 않으면 Braze가 메시지를 구문 분석할 수 없으므로 오류가 발생합니다.

### 튜토리얼: 위치 기반 콘텐츠 제공

이 튜토리얼을 마치면 사용자의 위치에 따라 "if", "elsif" 및 "else" 문을 사용하여 태그를 사용할 수 있게 됩니다.

1. 사용자의 도시가 뉴욕에 있을 때 어떤 메시지를 전송해야 하는지 설정하기 위해 `if` 태그로 시작합니다. 사용자의 도시가 뉴욕이면 이 첫 번째 조건이 충족되고 사용자는 뉴요커 정체성을 지정하는 메시지를 받게 됩니다.

```liquid
{% if ${city} == "New York" %}
  🎉 Hey there, New Yorker! We're excited to offer you a special deal! 
  Get 20% off your next sandwich at your local Sandwich Emperor. 
  Just show this message at the counter to redeem your offer!
```

{: start="2"}
2\. 다음으로, 사용자의 도시가 로스앤젤레스에 있을 때 어떤 메시지를 전송해야 하는지 설정하기 위해 `elseif` 태그를 사용합니다.

```liquid
{% elsif ${city} == "Los Angeles" %}
  🌞 Hello, Los Angeles! Enjoy a sunny day with a delicious sandwich! 
  Present this message at our LA restaurant for a 20% discount on your next order!
```

{: start="3"}
3\. 사용자의 도시가 시카고에 있을 때 어떤 메시지를 전송해야 하는지 설정하기 위해 또 다른 `elseif` 태그를 사용해 보겠습니다.

```liquid
{% elsif ${city} == "Chicago" %}
  🍕 Chicago, we have a treat for you! 
  Swing by our restaurant and get 20% off your favorite sandwich. 
  Just show this message to our staff!
```

{: start="4"}
4\. 이제 `{% else %}` 태그를 사용하여 사용자의 도시가 샌프란시스코, 뉴욕 또는 시카고에 없을 경우 어떤 메시지를 보낼지 지정해 보겠습니다.

```liquid
{% else %}
 🥪 Craving a sandwich? Visit us at any of our locations for a delicious meal! 
  Check our website for the nearest restaurant to you!
```

{: start="5"}
5\. 마지막으로, `{% endif %}` 태그를 사용하여 우리의 조건 논리가 완료되었음을 지정하겠습니다.

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

## null, nil 및 빈 속성 값 고려하기

조건 논리는 사용자 프로필에 설정되지 않은 속성 값을 고려하는 유용한 방법입니다.

### null 및 nil 속성 값

null 또는 nil 값은 사용자 정의 속성의 값이 설정되지 않았을 때 발생합니다. 예를 들어, 아직 이름을 설정하지 않은 사용자는 Braze에 이름이 기록되지 않습니다.

일부 상황에서는 이름이 설정된 사용자와 이름이 설정되지 않은 사용자에게 완전히 다른 메시지를 보내고 싶을 수 있습니다.

다음 태그를 사용하면 null "이름" 속성을 가진 사용자에게 메시지를 지정할 수 있습니다:

{% raw %}
```liquid
{% if ${first_name} == null %}
  ....
{% endif %}
```
{% endraw %} 

\![null '이름' 속성을 사용한 Braze 대시보드의 예시 메시지.]({% image_buster /assets/img/value_null.png %}){: style="max-width:60%;"}

{% raw %}
```liquid
{% if ${first_name} == null %}
We're having a sale! Hurry up and get 10% off all items today only!
{% else %}
Hey {{${first_name} | default: 'there'}}, we're having a sale! Hurry up and get 10% off all items today only!
{% endif %}
```

null 속성 값은 값 유형과 엄격하게 연관되어 있지 않음을 유의하십시오(예: "null" 문자열은 "null" 배열과 동일함). 따라서 위의 예에서 null 속성 값은 설정되지 않은 이름을 참조하며, 이는 문자열이 됩니다.

{% endraw %}

### 빈 속성 값

빈 값은 사용자 프로필의 속성이 설정되지 않았거나, 공백 문자열(` `)로 설정되었거나, `false`로 설정되었을 때 발생합니다. 빈 값은 Liquid 처리 오류를 피하기 위해 다른 변수보다 먼저 확인해야 합니다.

다음 태그를 사용하면 빈 "이름" 속성을 가진 사용자에게 메시지를 지정할 수 있습니다.

{% raw %}
```liquid
{% if ${first_name} == blank %}
  ....
{% endif %}
```
{% endraw %} 

## 사용자 정의 속성 참조하기

[사용자 정의 속성을 생성한 후]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#managing-custom-attributes), 이러한 사용자 정의 속성을 Liquid 메시지에서 참조할 수 있습니다.

조건 논리를 사용할 때는 올바른 구문을 사용하기 위해 사용자 정의 속성의 데이터 유형을 알아야 합니다. 대시보드의 **사용자 정의 속성** 페이지에서 사용자 정의 속성과 관련된 데이터 유형을 찾고, 각 데이터 유형에 대해 나열된 다음 예제를 참조하십시오.

\![사용자 정의 속성을 위한 데이터 유형 선택하기. 제공된 예제는 문자열 데이터 유형을 가진 Favorite_Category 속성을 보여줍니다.]({% image_buster /assets/img_archive/custom_attribute_data_type.png %}){: style="max-width:80%;"}

{% alert tip %}
문자열과 배열은 그 주위에 직선 아포스트로프가 필요하지만, 불리언과 정수는 아포스트로프가 없습니다.
{% endalert %}

#### 불리언

[불리언]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#booleans)은 이진 값이며, `true` 또는 `false`으로 설정할 수 있습니다. 예를 들어 `registration_complete: true`와 같습니다. 불리언 값은 그 주위에 아포스트로프가 없습니다.

{% raw %}

```liquid
{% if {{custom_attribute.${registration_complete}}} == true %}
```

{% endraw %}

#### 숫자

[숫자]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#numbers)는 정수 또는 부동 소수점일 수 있는 숫자 값입니다. 예를 들어, 사용자는 `shoe_size: 10` 또는 `levels_completed: 287`을 가질 수 있습니다. 숫자 값은 그 주위에 아포스트로프가 없습니다.

{% raw %}

```liquid
{% if {{custom_attribute.${shoe_size}}} == 10 %}
```

{% endraw %}

또한 정수에 대해 [기본 연산자](https://shopify.dev/docs/themes/liquid/reference/basics/operators)와 같은 다른 (<) 또는 (>)를 사용할 수 있습니다:

{% raw %}

```liquid
{% if {{custom_attribute.${flyer_miles}}} >= 500 %}
```

{% endraw %}

#### 문자열

[문자열]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#strings)은 알파벳 숫자 문자로 구성되며 사용자에 대한 데이터를 저장합니다. 예를 들어, `favorite_color: red` 또는 `phone_number: 3025981329`을 가질 수 있습니다. 문자열 값은 그 주위에 아포스트로프가 있어야 합니다.

{% raw %}

```liquid
{% if {{custom_attribute.${favorite_color}}} == 'blue' %}
```

{% endraw %}

문자열의 경우 Liquid에서 "==" 또는 "contains"를 모두 사용할 수 있습니다.

#### 배열

[배열]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#arrays)은 사용자에 대한 정보 목록입니다. 예를 들어, 사용자는 `last_viewed_shows: stranger things, planet earth, westworld`를 가질 수 있습니다. 배열 값은 작은따옴표로 둘러싸여야 합니다.

{% raw %}

```liquid
{% if {{custom_attribute.${last_viewed_shows}}} contains 'homeland' %}
```

{% endraw %}

배열의 경우 "contains"를 사용해야 하며 "=="를 사용할 수 없습니다. 

#### 시간

이벤트가 발생한 시간의 타임스탬프입니다. [시간]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#time) 값은 조건 논리에서 사용되기 위해 [수학 필터]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/filters/#math-filters)가 있어야 합니다.

{% raw %}

```liquid
{% assign expire = {{custom_attribute.${subscription_end_date}}} | plus: 0 %} 
```

{% endraw %}


