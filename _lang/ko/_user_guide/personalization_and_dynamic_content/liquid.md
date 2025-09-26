---
nav_title: Liquid
article_title: Liquid
page_order: 0
layout: dev_guide
search_rank: 3
guide_top_header: "리퀴드 태그를 사용한 개인화"
guide_top_text: "Braze는 지정된 사용자의 값을 자동으로 메시지로 대체할 수 있습니다. 표현식을 두 개의 괄호 안에 넣어 보간된 값을 사용할 것임을 Braze에 알립니다. 이 괄호 안에는 대체하려는 모든 사용자 값을 앞에 달러 기호가 있는 추가 괄호로 둘러싸야 합니다.<br><br>Liquid에 대한 자세한 내용은 Braze 학습 경로와 함께하는 <b><a href='https://learning.braze.com/path/dynamic-personalization-with-liquid'>Liquid를 사용한 동적 개인화</a></b> 가이드를 확인하세요!"
description: "이 랜딩 페이지에서는 지원되는 개인화 태그, 필터, 기본값 설정 등 Liquid의 모든 것을 다룹니다."

guide_featured_title: "섹션 기사"
guide_featured_list:
- name: 액체 사용
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/using_liquid/
  image: /assets/img/braze_icons/beaker-02.svg
- name: 지원되는 개인화 태그
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/
  image: /assets/img/braze_icons/tag-01.svg
- name: 연산자
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/operators/
  image: /assets/img/braze_icons/code-02.svg
- name: 필터
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/filters/
  image: /assets/img/braze_icons/flag-02.svg
- name: 고급 필터
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/
  image: /assets/img/braze_icons/settings-01.svg
- name: 기본값 설정
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/setting_default_values/
  image: /assets/img/braze_icons/table.svg
- name: 조건부 메시징 로직
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/
  image: /assets/img/braze_icons/columns-01.svg
- name: 메시지 중단하기
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/
  image: /assets/img/braze_icons/refresh-ccw-01.svg
- name: Liquid 사용 사례
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/liquid_use_cases/
  image: /assets/img/braze_icons/list.svg
- name: 튜토리얼
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/tutorials/
  image: /assets/img/braze_icons/book-open-01.svg
- name: 자주 묻는 질문
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/faq/
  image: /assets/img/braze_icons/annotation-question.svg
  
---

## Liquid 소개

> Liquid는 Shopify에서 개발한 오픈 소스 템플릿 언어이며 Ruby로 작성되었습니다. Braze에서 Liquid는 사용자 프로필의 데이터를 메시지로 템플릿화하는 데 사용됩니다. 

예를 들어 정수 데이터 유형인 고객 프로필에서 커스텀 속성을 검색하고 해당 값을 가장 가까운 정수로 반올림할 수 있습니다. For more on Liquid syntax and usage, refer to [**Supported personalization tags**]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/).

Liquid 템플릿 언어는 개체, 태그 및 필터 사용을 지원합니다.

- [**객체**]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) 를 사용하면 메시지에 개인화된 속성을 삽입할 수 있습니다.
- [**태그**]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/) 를 사용하면 메시징에 데이터를 삽입하고 조건부 논리를 사용하여 특정 조건이 충족되면 메시지를 보낼 수 있습니다. 예를 들어, 태그를 사용하여 캠페인에 "if" 문과 같은 지능형 로직을 포함할 수 있습니다.
- [**필터**]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/filters/) 를 사용하면 개인화된 속성 및 동적 콘텐츠의 형식을 다시 지정할 수 있습니다. 예를 들어 [`date` 필터를]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/filters/#date-filter) 사용하여 *2016-09-07 08:43:50 UTC와* 같은 타임스탬프를 *2016년 9월 7일과* 같은 날짜로 변환할 수 있습니다.

{% alert warning %}
Braze는 현재 Shopify Liquid의 100%를 지원하지 않으며, 문서에서 설명한 특정 부분만 지원합니다. 오류나 지원되지 않는 Liquid를 사용할 위험을 줄이기 위해 모든 메시지를 보내기 전에 Liquid를 사용하여 테스트하는 것을 적극 권장합니다.
{% endalert %}

### Liquid 5 지원

Braze는 **Shopify의 Liquid 5까지** Liquid를 지원합니다. Liquid 구현은 구문 개인화 태그 유형과 공백 제어를 지원합니다. 특정 태그에 대한 자세한 내용은 [구문 태그]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/#syntax-tags)를 참조하세요.

다음과 같은 새로운 배열 및 수학 필터를 Liquid에서 메시징을 작성할 때 사용할 수 있습니다.
- `at_least`
- `at_most`
- `compact`
- `concat`
- `sort_natural`
- `where`

정의는 [필터를]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/filters/) 참조하세요.

### 리퀴드 업데이트

#### 색상 레이블

각 Liquid 요소는 색상에 해당하므로 Liquid 에디터에서 한눈에 Liquid를 구분할 수 있습니다.

![]({% image_buster /assets/img/liquid_color_code.png %})

#### 예측 액체

또한 개인화된 메시지를 작성할 때 사용자 지정 속성, 속성 이름 등에 예측 리퀴드를 활용할 수도 있습니다.

![]({% image_buster /assets/img/liquid_auto_complete.gif %}){: style="max-width:70%;"}

## 알아두어야 할 용어

이 용어는 다음에서 재해석한 것입니다. [**Shopify 설명서**](https://shopify.github.io/liquid/basics/introduction/)의 지원 수준을 기반으로 재해석되었습니다.

{% raw %}

| 기간 | 정의 | 예시 |  
|---|---|---|
| Liquid | 일반적으로 사용되는 고객용 템플릿 언어로, 동적 콘텐츠를 로드하고 가져오는 데 사용되는 Shopify에서 생성하고 Ruby로 작성되었습니다. | `{{${first_name}}}`을 누르면 사용자의 이름이 메시지에 삽입됩니다. |
| 객체 | 메시지에서 콘텐츠를 표시할 위치를 Liquid에 알려주는 변수 및 의도된 변수 이름의 위치 표시입니다. | `{{${city}}}` 는 사용자의 도시를 메시지에 삽입합니다. |
| 조건부 논리 태그 | 로직을 생성하고 메시지 콘텐츠의 흐름을 제어하는 데 사용됩니다. Braze에서 조건 로직 태그는 미리 정의된 특정 기준에 따라 메시지의 예외 및 변형을 만드는 데 사용됩니다. | ```{% if ${language} == 'en' %}```는 사용자가 "영어"를 언어로 지정한 경우 지정된 방식으로 메시지를 트리거합니다. |
| 필터 | Liquid 오브젝트의 출력을 변경, 축소 또는 재포맷하는 데 사용됩니다. 수학적 연산을 만드는 데 자주 사용됩니다. | ```{{"Big Sale" | upcase}}```를 입력하면 메시지에서 "빅 세일"이라는 단어가 "빅 세일"로 표시됩니다. |
| 연산자 | 메시지에서 사용자가 수신하는 메시지에 영향을 줄 수 있는 종속성 또는 기준을 만드는 데 사용됩니다. | 사용자가 `{% custom_attribute.${Total_Revenue} > 0%}` 으로 태그된 메시지에서 정의된 기준을 충족하면 해당 메시지를 받게 됩니다. 그렇지 않은 경우 설정한 내용에 따라 다른 지정된 메시지를 받거나 받지 않습니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endraw %}

<br>

