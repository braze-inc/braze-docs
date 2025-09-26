---
nav_title: 메시지 추가 태그
article_title: 메시지 추가 태그
page_order: 1
description: "이 문서는 메시지 추가 Liquid 태그를 사용하는 방법과 구문을 확인하는 방법을 설명합니다."
alias: "/message_extras_tag/"
---

# 메시지 추가 기능 Liquid 태그

> 전송 이벤트에 Liquid 태그를 사용하여 연결된 콘텐츠, 카탈로그, 커스텀 속성(예: 언어, 국가), 캔버스 항목 속성 또는 기타 데이터 소스의 동적 데이터로 주석을 달 수 있습니다.

`message_extras` Liquid 태그는 커런츠 및 Snowflake 데이터 공유의 해당 전송 이벤트에 키-값 페어를 추가합니다. 

동적 또는 추가 데이터를 커런츠 또는 Snowflake 데이터 공유 전송 이벤트로 다시 보내려면 메시지 본문에 적절한 Liquid 태그를 삽입하세요. 

다음은 표준 Liquid 태그 형식의 예입니다 :

{% raw %}
```liquid
{% message_extras :key test :value 123 %}
```
{% endraw %}

메시지 본문에 키-값 페어를 위해 필요한 태그를 추가할 수 있습니다. 그러나 모든 키와 값의 길이는 1KB를 초과해서는 안 됩니다. 커런츠 및 Snowflake 데이터 공유에서 전송 이벤트에 대해 `message_extras`라는 새 이벤트 필드를 볼 수 있습니다. 이것은 하나의 필드에 JSON 직렬화된 문자열을 생성합니다.

## 지원 채널

`message_extras` 태그는 모든 메시지 유형에 대해 전송 이벤트와 함께 인앱 메시지 노출 횟수 이벤트를 지원합니다. 인앱 메시지에서 `message_extras`를 사용하려면 특정 [최소 SDK 버전](#iam-sdk)을 충족해야 합니다.

## 태그를 사용하는 방법

1. 채널의 메시지 본문에 Liquid 태그를 입력하세요. 또는 **개인화 추가** 모달을 사용하고 개인화 유형에 대해 **메시지 추가 기능**을 선택할 수 있습니다. 

![The Add Personalization modal with Message Extras selected as the personalization type.]({% image_buster /assets/img_archive/message_extras1.png %}){: style="max-width:35%;"}

{: start="2"}

2. 각 `message_extras` 태그에 대한 [키-값 페어]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/key_value_pairs/)를 입력하세요. 

![메시지 엑스트라 태그에 대한 키-값 쌍의 예입니다. 제목 필드에는 "Your New Favorites."라고 적혀 있습니다. 메시지는 메시지 추가 태그의 키-값 페어를 읽고 다음 문장을 읽습니다. "We're excited to bring you a side selection of fresh and exciting products that are sure to become your new go-to favorites"]({% image_buster /assets/img_archive/message_extras2.png %}){: style="max-width:70%;"}

{: start="3"}

3. 캠페인 또는 캔버스가 발송된 후, Braze는 발송 시간에 동적 데이터를 커런츠 또는 Snowflake 데이터 공유 발송 이벤트를 통해 `message_extras` 필드에 첨부합니다.

## 구문 검사

태그 외의 다른 입력은 Currents 또는 Snowflake로 전달되지 않을 수 있습니다. 다음 중 어느 것도 포함하지 않도록 구문이나 형식을 확인하십시오:

- 존재하지 않거나 비어 있거나 잘못 입력된 구분 기호
- 중복 키(Braze는 처음으로 발견된 키-값 페어를 보내는 기본값을 사용합니다)
- 키 또는 값이 정의되기 전에 추가 텍스트
- 순서가 맞지 않는 키와 값 
  - {% raw %}예를 들어, ```{% message_extras :value 123 :key test %}```{% endraw %}

## 고려사항

- 키-값이 1KB를 초과하면 잘립니다. 
- 공백은 문자 수에 포함됩니다. Braze는 앞뒤 공백을 생략합니다.
- 결과 JSON은 문자열 값만 출력합니다.
- Liquid 변수를 키 또는 값으로 포함할 수 있지만, 다른 Liquid 태그는 사용할 수 없습니다.
  - 예를 들어, 다음 Liquid를 사용할 수 있습니다:

## 자주 묻는 질문

#### 내 참여 이벤트(열기 및 클릭)와 같은 전송 이벤트에서 message_extras 필드를 어떻게 연결할 수 있습니까? 

`dispatch_id`가 생성되어 전송 이벤트에 제공되며, 특정 클릭, 열람 또는 전달된 이벤트와 연결할 수 있는 고유 식별자로 사용할 수 있습니다. 이 필드를 Currents 또는 Snowflake에서 사용하고 쿼리할 수 있습니다. [`dispatch_id`동작]({{site.baseurl}}/help/help_articles/data/dispatch_id/)에 대해 자세히 알아보세요.

#### 앱 내 메시지에서 message_extras를 사용할 수 있나요? {#iam-sdk}

네, 사용자의 기기가 다음 최소 SDK 버전에서 실행되는 한 `message_extras`를 인앱 메시지에서 사용할 수 있습니다.

{% sdk_min_versions web:5.2.0 android:30.4.0 swift:8.4.0 %}

