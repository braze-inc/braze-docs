---
nav_title: 조건부 메시징 로직
article_title: 조건부 리퀴드 메시징 로직
page_order: 6
description: "이 참조 문서에서는 캠페인에서 태그를 사용할 수 있는 방법과 사용해야 하는 방법에 대해 설명합니다."

---

# 조건부 메시징 로직

> [태그][7]를 사용하면 메시징 캠페인에 프로그래밍 로직을 포함할 수 있습니다. 태그는 조건문을 실행하는 데 사용할 수 있을 뿐만 아니라 변수 할당이나 코드 블록을 반복하는 등의 고급 사용 사례에도 사용할 수 있습니다. <br><br>이 페이지에서는 null, nil 및 빈 속성 값을 처리하는 방법, 사용자 정의 속성을 참조하는 방법 등 태그를 사용할 수 있는 방법과 사용해야 하는 방법에 대해 설명합니다.

## 태그 서식 지정

{% raw %}
태그는 `{% %}`로 묶어야 합니다.
{% endraw %}

{% alert tip %}
조금 더 쉽게 사용할 수 있도록 Braze에는 Liquid 구문을 올바르게 포맷한 경우 녹색과 보라색으로 활성화되는 색상 포맷이 포함되어 있습니다. 녹색 서식은 태그를 식별하는 데 도움이 되며 보라색 서식은 개인화가 포함된 영역을 강조 표시합니다.
<br><br>
조건부 메시징을 사용하는 데 어려움이 있다면 사용자 지정 속성 및 기타 Liquid 요소를 삽입하기 전에 조건부 구문을 작성해 보세요.
<br><br>
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
{% endalert %}

## 조건부 논리

조건문과 같은 다양한 유형의 [메시지 내 지능형 논리][1]를 포함할 수 있습니다. [조건문][8]을 사용하여 캠페인을 글로벌화하는 다음 예시를 참조하세요.
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

### 단계별 예시

이 예에서는 "if", "elsif" 및 "else" 문이 포함된 태그를 사용하여 국제화된 콘텐츠를 전달합니다.

```liquid
{% if ${language} == 'en' %}
This is a message in English from Braze!
```
사용자의 언어가 영어인 경우 첫 번째 조건이 충족되며 사용자는 영어로 된 메시지를 받게 됩니다.

```liquid
{% elsif ${language} == 'es' %}
Este es un mensaje en español de Braze !
{% elsif ${language} == 'zh' %}
这是一条来自Braze的中文消息。
```

조건문을 원하는 만큼 지정할 수 있습니다. 이전 조건이 충족되지 않으면 후속 조건이 확인됩니다. 이 예제에서는 사용자의 디바이스가 영어로 설정되어 있지 않은 경우 이 코드가 사용자의 디바이스가 스페인어 또는 중국어로 설정되어 있는지 확인합니다. 사용자의 디바이스가 이러한 조건 중 하나를 충족하면 해당 언어로 된 메시지를 받게 됩니다.

```liquid
{% else %}
This is a message from Braze! This is going to go to anyone who didn't match the other specified languages!
```

조건부 논리에 `{% else %}` 문을 포함할 수 있습니다. 설정한 조건 중 어느 것도 충족되지 않으면 `{% else %}` 문이 전송할 메시지를 지정합니다. 이 경우 사용자의 언어가 영어, 스페인어 또는 중국어가 아닌 경우 기본값은 영어로 설정됩니다.

```liquid
{% endif %}
```

`{% endif %}` 태그는 조건부 로직이 완료되었음을 알립니다. 조건부 논리가 포함된 모든 메시지에는 `{% endif %}` 태그를 포함해야 합니다. 조건부 로직에 `{% endif %}` 태그를 포함하지 않으면 Braze가 메시지를 구문 분석할 수 없으므로 오류가 발생합니다.

{% endraw %}

## null, nil 및 빈 속성 값에 대한 설명

조건 로직은 고객 프로필에 설정되지 않은 속성 값을 설명하는 데 유용한 방법입니다.

### Null 및 nil 속성 값

사용자 지정 속성의 값이 설정되지 않은 경우 null 또는 nil 값이 발생합니다. 예를 들어, 아직 이름을 설정하지 않은 사용자는 Braze에 로그인할 수 없습니다.

경우에 따라 이름 설정이 있는 사용자와 이름 설정이 없는 사용자에게 완전히 다른 메시지를 보내야 할 수도 있습니다.

다음 태그를 사용하면 '이름' 속성이 null인 사용자에 대한 메시지를 지정할 수 있습니다:

{% raw %}
```liquid
{% if ${first_name} == null %}
  ....
{% endif %}
```
{% endraw %} 

!['이름' 속성이 널인 Braze 대시보드의 메시지 예시입니다.][36]{: style="max-width:60%;"}

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

커스텀 속성][2]을 생성한 후에는 Liquid 메시징에서 이러한 커스텀 속성을 참조할 수 있습니다.

조건 로직을 사용할 때는 올바른 구문을 사용하고 있는지 확인하려면 커스텀 속성의 데이터 유형을 알아야 합니다. 대시보드의 **사용자 지정** 속성 페이지에서 사용자 지정 속성과 연결된 데이터 유형을 찾은 다음 각 데이터 유형에 대해 나열된 다음 예제를 참조합니다.

![사용자 지정 속성에 대한 데이터 유형을 선택합니다. 제공된 예는 데이터 유형이 문자열인 Favorite_Category의 속성을 보여줍니다.][20]{: style="max-width:80%;"}

{% alert tip %}
문자열과 배열에는 직선 아포스트로피가 필요하지만 부울과 정수에는 아포스트로피가 없습니다.
{% endalert %}

#### 부울

[부울][9]은 이진 값이며, `true` 또는 `false`로 설정할 수 있습니다(예: `registration_complete: true`). 부울 값에는 아포스트로피가 없습니다.

{% raw %}

```liquid
{% if {{custom_attribute.${registration_complete}}} == true %}
```

{% endraw %}

#### 숫자

[숫자][10]는 정수 또는 부동 소수점일 수 있는 숫자 값입니다. 예를 들어, 사용자는 `shoe_size: 10` 또는 `levels_completed: 287`을 가질 수 있습니다. 숫자 값에는 아포스트로피가 없습니다.

{% raw %}

```liquid
{% if {{custom_attribute.${shoe_size}}} == 10 %}
```

{% endraw %}

정수에 대해 <보다 작음(<) 또는 >보다 큼(>)과 같은 다른 [기본 연산자를](https://shopify.dev/docs/themes/liquid/reference/basics/operators) 사용할 수도 있습니다:

{% raw %}

```liquid
{% if {{custom_attribute.${flyer_miles}}} >= 500 %}
```

{% endraw %}

#### 문자열

[문자열][11]은 영숫자로 구성되며 사용자에 대한 데이터를 저장합니다. 예를 들어 `favorite_color: red` 또는 `phone_number: 3025981329`가 있을 수 있습니다. 문자열 값 주위에 아포스트로피를 붙여야 합니다.

{% raw %}

```liquid
{% if {{custom_attribute.${favorite_color}}} == 'blue' %}
```

{% endraw %}

문자열의 경우 Liquid에서 "==" 또는 "contains"를 모두 사용할 수 있습니다.

#### 배열

[배열][12]은 사용자에 대한 정보 목록입니다. 예를 들어 사용자가 `last_viewed_shows: stranger things, planet earth, westworld`를 가질 수 있습니다. 배열 값은 주위에 아포스트로피를 포함해야 합니다.

{% raw %}

```liquid
{% if {{custom_attribute.${last_viewed_shows}}} contains 'homeland' %}
```

{% endraw %}

배열의 경우 "contains"를 사용해야 하며 "=="는 사용할 수 없습니다. 

#### 시간

이벤트가 발생한 시점의 타임스탬프입니다. 조건 로직에서 사용하려면 [시간][13] 값에 [수학 필터][5]가 있어야 합니다.

{% raw %}

```liquid
{% assign expire = {{custom_attribute.${subscription_end_date}}} | plus: 0 %} 
```

{% endraw %}


[36]:{% image_buster /assets/img/value_null.png %}
[1]:http://docs.shopify.com/themes/liquid-documentation/basics
[2]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#managing-custom-attributes
[5]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/filters/#math-filters
[7]:https://docs.shopify.com/themes/liquid-documentation/tags
[8]: http://docs.shopify.com/themes/liquid-documentation/tags/control-flow-tags "제어 흐름 태그"
[9]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#booleans
[10]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#numbers
[11]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#strings
[12]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#arrays
[13]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#time
[20]: {% image_buster /assets/img_archive/custom_attribute_data_type.png %}
