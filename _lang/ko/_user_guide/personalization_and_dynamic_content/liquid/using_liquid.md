---
nav_title: 액체 사용
article_title: 리퀴드 사용 사례 및 개요
page_order: 0
description: "이 참고 문서에서는 일반적인 Liquid 사용 사례에 대한 개요와 메시징에 Liquid 태그를 포함하는 방법에 대해 설명합니다."
search_rank: 2
---

# [![Braze 학습 과정]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/path/dynamic-personalization-with-liquid){: style="float:right;width:120px;border:0;" class="noimgborder"}Liquid 사용하기

> 이 도움말에서는 다양한 사용자 속성을 사용하여 메시징에 개인 정보를 동적으로 삽입하는 방법을 설명합니다.

Liquid는 Shopify에서 개발한 오픈 소스 템플릿 언어이며 Ruby로 작성되었습니다. Braze에서 이를 사용하여 사용자 프로필 데이터를 메시지로 가져오고 해당 데이터를 사용자 지정할 수 있습니다. 예를 들어 Liquid 태그를 사용하여 사용자의 가입 기념일에 따라 다른 오퍼를 보내는 등의 조건부 메시지를 만들 수 있습니다. 또한 필터는 타임스탬프에서 사용자의 등록 날짜를 "2022년 1월 15일"과 같이 더 읽기 쉬운 형식으로 포맷하는 등 데이터를 조작할 수 있습니다. For further details on Liquid syntax and its capabilities, refer to [Supported personalization tags]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/).

## 작동 방식

Liquid 태그는 사용자의 계정에서 동의한 정보를 가져와 개인화 및 관련 메시징 관행을 활성화할 수 있는 메시지 내 입력 안내 역할을 합니다.

다음 블록에서는 사용자의 이름을 부를 때 Liquid 태그를 이중으로 사용하는 것과 사용자가 이름을 등록하지 않은 경우 기본 태그를 사용하는 것을 볼 수 있습니다.

{% raw %}
```liquid
Hi {{ ${first_name} | default: 'Valued User' }}, thanks for using the App!
```
{% endraw %}

신원 미상이라는 사용자에게는 이 메시지가 다음과 같이 표시됩니다.

```
Hi Janet, thanks for using the App!
```

또는

```
Hi Valued User, thanks for using the App!
```

## 대체할 수 있는 지원되는 값

사용 가능 여부에 따라 다음 값을 메시지로 대체할 수 있습니다:

- [Basic user information]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/) (for example, `first_name`, `last_name`, `email_address`)
- [Custom attributes]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/)
    - [Nested custom attributes]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/nested_custom_attribute_support/#liquid-templating)
- [Custom event properties]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)
- [Most recently used device information]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/#most-recently-used-device-information)
- [Target device information]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/#targeted-device-information)

You can also pull content directly from a web server through Braze [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/).

{% alert important %}
Braze는 현재 Shopify의 Liquid 5까지 지원합니다.
{% endalert %}

## Liquid 사용

Using [Liquid tags]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/), you can elevate the quality of your messages by enriching them with a personal touch. 

### 액체 구문

Liquid는 동적 개인화를 제작할 때 염두에 두어야 할 특정 구조 또는 구문을 따릅니다. 다음은 명심해야 할 몇 가지 기본 규칙입니다:

1. **Braze에서는 따옴표를 사용합니다:** 둥근 따옴표('**'**)와 곧은 따옴표('**'**)에는 차이가 있습니다. Braze의 Liquid에서는 따옴표(**" "**)를 사용하세요. 특정 텍스트 편집기에서 복사하여 붙여넣을 때 꼬불꼬불한 따옴표가 표시될 수 있으며, 이는 Liquid에서 문제를 일으킬 수 있습니다. 따옴표를 Braze 대시보드에 직접 입력하는 경우 괜찮을 것입니다!
2. **괄호는 쌍으로 제공됩니다.** 모든 대괄호는 **{ }**를 열고 닫아야 합니다. 중괄호를 사용해야 합니다!
3. **문이 쌍으로 구성된 경우:** 모든 `if`에 대해 `endif`를 추가하여 `if` 문장이 종료되었음을 표시해야 합니다.

#### 기본 속성 및 사용자 지정 속성

{% raw %}

메시지에 다음 텍스트를 포함하는 경우 `{{${first_name}}}`을 포함하면 메시지가 전송될 때 고객 프로필에서 가져온 사용자의 이름이 대체됩니다. 다른 기본 사용자 속성과 동일한 형식을 사용할 수 있습니다.

커스텀 속성 값을 사용하려면 변수에 네임스페이스 "custom_attribute"를 추가해야 합니다. 예를 들어 "우편 번호"라는 커스텀 속성을 사용하려면 메시지에 `{{custom_attribute.${zip code}}}`를 포함하면 됩니다.

### 태그 삽입하기

모든 메시지에 열린 중괄호 `{{` 두 개를 입력하여 태그를 삽입하면 입력하는 동안 계속 업데이트되는 자동 완성 기능이 트리거됩니다. 입력할 때 표시되는 옵션에서 변수를 선택할 수도 있습니다.

사용자 지정 태그를 사용하는 경우 원하는 메시지에 태그를 복사하여 붙여넣을 수 있습니다.

{% endraw %}

{% alert note %}

이메일 메시지에 Liquid를 사용하는 경우 반드시 사용해야 합니다:

1. 기존 편집기가 아닌 HTML 편집기를 사용하여 삽입합니다. 클래식 편집기는 리퀴드를 일반 텍스트로 구문 분석할 수 있습니다. 예를 들어, Liquid는 사용자의 이름으로 템플릿을 지정하는 대신 {% raw %}`Hi {{ ${first_name} }}, thanks for using our service!`{% endraw %} 로 구문 분석합니다.
2. Liquid 코드는 `<body>` 태그 안에만 배치하세요. 이 태그 외부에 배치하면 전달 시 렌더링이 일관되지 않을 수 있습니다.

{% endalert %}

### 미리 포맷된 변수 삽입하기

You can insert pre-formatted variables with defaults through the **Add Personalization** modal located near any templated text field.

![개인화 삽입을 선택한 후 표시되는 개인화 추가 모달입니다. The modal has fields for personalization type, attribute, optional default value, and displays a preview of the Liquid syntax.]({% image_buster /assets/img_archive/insert_liquid_var_arrow.png %}){: style="max-width:90%;"}

The modal will insert Liquid with your specified default value at the point where your cursor was. 삽입 지점은 앞뒤 텍스트가 있는 미리보기 상자로도 지정할 수 있습니다. 텍스트 블록이 강조 표시된 경우 강조 표시된 텍스트가 바뀝니다.

![A GIF of the Add Personalization modal that shows the user inserting "fellow traveler" as a default value, and the modal replacing the highlighted text "name" in the composer with the Liquid snippet.]({% image_buster /assets/img_archive/insert_var_shot.gif %})

### 변수 할당

{% raw %}
Liquid의 일부 작업에서는 조작하려는 값을 변수로 저장해야 합니다. Liquid 문에 여러 속성, 이벤트 속성정보 또는 필터가 포함된 경우 이러한 경우가 많습니다.

예를 들어 두 개의 사용자 지정 데이터 정수를 함께 추가하고 싶다고 가정해 보겠습니다. 

#### 잘못된 액체 예제

사용할 수 없습니다:

```liquid
{{custom_attribute.${one}}} | plus: {{custom_attribute.${two}}}
```

이 Liquid는 한 줄에 여러 속성을 참조할 수 없기 때문에 작동하지 않으며, 연산 함수가 수행되기 전에 이러한 값 중 하나 이상에 변수를 할당해야 합니다. 두 개의 커스텀 속성을 추가하려면 두 줄의 Liquid가 필요합니다. 하나는 변수에 커스텀 속성을 할당하는 데, 다른 하나는 추가를 수행하는 데 사용됩니다.

#### 올바른 액체 예제

사용할 수 있습니다:

```liquid
{% assign value_one = {{custom_attribute.${one}}} %}
{% assign result = value_one | plus: {{custom_attribute.${two}}} %}
```

#### 튜토리얼: 변수를 사용하여 잔액 계산하기

기프트 카드 잔액과 리워드 잔액을 더하여 사용자의 현재 잔액을 계산해 보겠습니다:

먼저 `assign` 태그를 사용하여 `current_rewards_balance` 의 사용자 지정 속성을 "balance"라는 용어로 대체합니다. 즉, 이제 조작할 수 있는 `balance`라는 변수가 생겼습니다.

```liquid
{% assign balance = {{custom_attribute.${current_rewards_balance}}} %}
```

다음으로 `plus` 필터를 사용하여 각 사용자의 기프트 카드 잔액을 `{{balance}}`로 표시되는 리워드 잔액과 결합합니다.

```liquid
{% assign balance = {{custom_attribute.${current_rewards_balance}}} %}
You have ${{custom_attribute.${giftcard_balance} | plus: {{balance}}}} to spend!
```
{% endraw %}

{% alert tip %}
모든 메시지에 동일한 변수를 할당하고 계신가요? `assign` 태그를 반복해서 작성하는 대신 해당 태그를 콘텐츠 블록으로 저장하여 메시지 상단에 넣을 수 있습니다.

1. [콘텐츠 블록을 생성합니다]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/#create-a-content-block).
2. 콘텐츠 블록에 이름을 지정합니다(공백이나 특수 문자 제외).
3. 페이지 하단에서 **수정을** 선택합니다.
4. `assign` 태그를 입력합니다.

콘텐츠 블록이 메시지 상단에 있는 한, 변수가 객체로 메시지에 삽입될 때마다 선택한 커스텀 속성을 참조합니다!
{% endalert %}

