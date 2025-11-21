---
nav_title: 메시지 추가 태그
article_title: 메시지 추가 태그
page_order: 1
description: "이 문서에서는 메시지 추가 기능인 Liquid 태그를 사용하는 방법과 구문을 확인하는 방법에 대해 설명합니다."
alias: "/message_extras_tag/"
---

# 메시지 추가 Liquid 태그

> `message_extras` Liquid 태그를 사용하여 연결된 콘텐츠, 카탈로그, 커스텀 속성(예: 언어, 국가), 캔버스 항목 속성 또는 기타 데이터 소스의 동적 데이터로 보내기 이벤트에 주석을 달 수 있습니다.

`message_extras` Liquid 태그는 커런츠 및 Snowflake 데이터 공유에서 해당 전송 이벤트에 키-값 페어를 추가합니다. 

커런츠 또는 Snowflake 데이터 공유 보내기 이벤트에 동적 데이터 또는 추가 데이터를 다시 보내려면 메시지 본문에 적절한 Liquid 태그를 삽입하세요. 

다음은 `message_extras` 에 대한 표준 Liquid 태그 형식의 예시입니다:

{% raw %}
```liquid
{% message_extras :key test :value 123 %}
```
{% endraw %}

메시지 본문의 키-값 페어에 필요에 따라 이러한 태그를 추가할 수 있습니다. 그러나 모든 키와 값의 길이는 1KB를 초과해서는 안 됩니다. 커런츠 및 Snowflake 데이터 공유에서 이벤트 전송을 위한 `message_extras` 이라는 새로운 이벤트 필드가 표시됩니다. 이렇게 하면 하나의 필드에 JSON 직렬화된 문자열이 생성됩니다.

## 지원되는 채널

`message_extras` 태그는 인앱 메시지 노출 횟수 이벤트와 함께 전송 이벤트가 있는 모든 메시지 유형에 대해 지원됩니다. `message_extras` 을 인앱 메시지와 함께 사용하려면 특정 [최소 소프트웨어 개발 키트 버전을](#iam-sdk) 충족해야 합니다.

## `message_extras` 태그 사용 방법

1. 채널의 메시지 본문에 `message_extras` Liquid 태그를 입력합니다. 또는 개인화 **추가** 모달을 사용하고 개인화 유형으로 **메시지 추가를** 선택할 수 있습니다. 

메시지 추가를 개인화 유형으로 선택한 개인화 추가 모달.]({% image_buster /assets/img_archive/message_extras1.png %}){: style="max-width:35%;"}

{: start="2"}

2. 각 `message_extras` 태그에 [키-값 페어를]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/key_value_pairs/) 입력합니다. 

\![메시지 추가 태그의 키-값 페어 예시입니다. 제목 필드에는 "새 즐겨찾기가 표시됩니다."라고 표시됩니다. 메시지는 메시지 추가 태그의 키-값 페어와 다음 문장을 읽습니다: "새로운 인기 제품이 될 신선하고 흥미로운 제품들을 선보이게 되어 기쁘게 생각합니다."]({% image_buster /assets/img_archive/message_extras2.png %}){: style="max-width:70%;"}

{: start="3"}

3. 캠페인 또는 캔버스를 전송한 후, Braze는 전송 시점에 커런츠 또는 Snowflake 데이터 공유 전송 이벤트를 통해 `message_extras` 필드에 동적 데이터를 첨부합니다.

## 구문 확인

위에서 설명한 태그 표준과 일치하지 않는 다른 입력은 커런츠 또는 Snowflake에 전달되지 않을 수 있습니다. 구문이나 서식에 다음 사항이 포함되어 있지 않은지 확인하세요:

- 존재하지 않거나, 비어 있거나, 잘못 입력된 구분 기호
- 중복 키(Braze는 기본값으로 먼저 발견되는 키-값 페어 전송)
- 키 또는 값이 정의되기 전의 추가 텍스트
- 순서가 맞지 않는 키 및 값 
  - {% raw %}예를 들어 ```{% message_extras :value 123 :key test %}```{% endraw %}

## 커런츠에 프로모션 코드 정보 보내기

{% multi_lang_include shopify.md section='Liquid promotion codes with Currents' %}

## 고려 사항

- 키 값이 1KB를 초과하면 잘립니다. 
- 공백은 글자 수에 포함됩니다. Braze는 선행 공백과 후행 공백을 생략합니다.
- 결과 JSON은 문자열 값만 출력합니다.
- Liquid 변수를 키 또는 값으로 포함할 수는 있지만 `message_extras` 내에 다른 Liquid 태그를 사용할 수는 없습니다.
  - 예를 들어 다음과 같은 Liquid를 사용할 수 있습니다: {% raw %}```{% assign value = '123' %} {% assign key = 'test' %} {% message_extras :key {{key}} :value {{value}} %}```{% endraw %}

## 자주 묻는 질문

#### 이벤트 보내기에서 message_extras 필드를 열기 및 클릭과 같은 참여 이벤트에 연결하려면 어떻게 해야 하나요? 

`dispatch_id` 이 생성되어 전송 이벤트에 제공되며, 특정 클릭, 열기 또는 전달 이벤트에 연결하기 위한 고유 식별자로 사용할 수 있습니다. 이 필드는 커런츠 또는 Snowflake에서 사용하고 쿼리할 수 있습니다. [`dispatch_id` 동작에]({{site.baseurl}}/help/help_articles/data/dispatch_id/) 대해 자세히 알아보세요.

#### message_extras 을 인앱 메시지와 함께 사용할 수 있나요? {#iam-sdk}

예, 사용자의 기기가 다음 최소 소프트웨어 개발 키트 버전을 사용하는 경우 인앱 메시징에 `message_extras` 을 사용할 수 있습니다:

{% sdk_min_versions web:5.2.0 android:30.4.0 swift:8.4.0 %}

