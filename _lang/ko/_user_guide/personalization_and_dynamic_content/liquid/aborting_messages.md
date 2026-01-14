---
nav_title: 메시지 중단하기
article_title: Liquid 메시지 중단하기
page_order: 7
description: "이 참고 문서에서는 Liquid 메시지 중단과 몇 가지 사용 사례에 대해 설명합니다."

---

# 메시지 중단하기

> 선택적으로 조건부 내에서 `abort_message("optional reason for aborting")` Liquid 메시지 태그를 사용하여 사용자에게 메시지를 보내지 않도록 할 수 있습니다. 이 참고 문서에는 이 기능을 마케팅 캠페인에 사용할 수 있는 몇 가지 예가 나와 있습니다.

{% alert note %}
캔버스에서 메시지 단계가 중단되면 사용자는 캔버스를 **종료하지 않고** 다음 단계로 **진행합니다**.
{% endalert %}

## "참석한 게임 수"가 0이면 메시지 중단

예를 들어 게임에 참여하지 않은 고객에게 메시지를 보내고 싶지 않다고 가정해 보겠습니다:

{% raw %}
```liquid
{% if custom_attribute.${Number_Game_Attended} == 1 %}
Loved the game? Get 10% off your second one with code SAVE10.
{% elsif custom_attribute.${Number_Game Attended} > 1 %}
Love the games? Get 10% off your next one with code SAVE10.
{% else %}
{% abort_message() %}
{% endif %}
```
{% endraw %}

이 메시지는 게임에 참여한 것으로 확인된 고객에게만 전송됩니다.

## 영어를 사용하는 고객에게만 메시지 보내기

고객의 언어가 영어일 때 일치하는 "if" 문과 영어를 사용하지 않거나 프로필에 해당 언어가 없는 경우 메시지를 중단하는 "else" 문을 생성하여 영어를 사용하는 고객에게만 메시지를 보낼 수 있습니다.

{% raw %}
```liquid

{% if ${language} == 'en' %}
Send this message in English!
{% else %}
{% abort_message() %}
{% endif %}
```

기본값으로 Braze는 일반 오류 메시지를 메시지 활동 로그에 기록합니다:

```text
{% abort_message %} called
```

괄호 안에 문자열을 포함하여 메시지 중단이 메시지 활동 로그에 무언가를 기록하도록 할 수도 있습니다:

```liquid
{% abort_message('language was nil') %}
```
{% endraw %}

개발자 콘솔의 메시지 오류 로그에 "언어가 없음"이라는 중단 메시지가 표시됩니다.]({% image_buster /assets/img_archive/developer_console.png %})

## 중단 메시지 쿼리하기

[쿼리 빌더]({{site.baseurl}}/user_guide/analytics/query_builder/) 또는 자체 데이터 웨어하우스(Braze에 연결되어 있는 경우)를 사용하여 Liquid 로직으로 인해 메시징이 중단될 때 트리거되는 특정 중단 메시지를 쿼리할 수 있습니다.

## 고려 사항

`abort_message()` Liquid 메시지 태그를 사용하면 메시징이 사용자에게 전송되지 않으므로 메시지가 사용자 프로필에 표시되지 않으며 전달 또는 최대 게재빈도 설정에 포함되지 않습니다.
