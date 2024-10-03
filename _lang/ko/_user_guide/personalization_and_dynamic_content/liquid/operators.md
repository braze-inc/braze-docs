---
nav_title: 연산자
article_title: 리퀴드 오퍼레이터
page_order: 2
description: "이 참조 페이지에는 Liquid가 지원하는 연산자와 관련 예시가 나와 있습니다."

---

# 연산자

Liquid는 조건문에 사용할 수 있는 다양한 \[연산자][25] ]를 지원합니다.

|   구문| 운영자 설명|
|---------|-----------|
| ==  | 동등함        |
| !=  | 동등하지 않음|
|  >  | 큼  |
| <   | 미만     |
| >=| 보다 크거나 같은|
| <= | 다음보다 작거나 같아야 합니다. |
| 또는 | 조건 A 또는 조건 B|
| 그리고 | 조건 A 및 조건 B|
| 포함 | 문자열 또는 문자열 배열에 문자열이 포함되어 있는지 확인합니다.|
{: .reset-td-br-1 .reset-td-br-2}

## 연산자 예제

다음은 이러한 운영자가 마케팅 캠페인에 어떻게 도움이 될 수 있는지에 대한 몇 가지 예시입니다:

### 정수 사용자 지정 속성을 통해 메시지 선택

{% raw %}
```liquid
{% if {{custom_attribute.${total_spend}}} >0 %}
Thanks for purchasing! Here's another 10% off!
{% else %}
Buy now! Would 5% off convince you?
{% endif %}
```
{% endraw %}

![][13]{: width="100%"}

이 예제에서 고객의 '총 지출' 사용자 지정 속성이 `0` 보다 크면 메시지가 표시됩니다:

```
Thanks for purchasing! Here's another 10% off!
```
고객의 '총 지출' 사용자 지정 속성이 존재하지 않거나 `0` 와 같으면 다음과 같은 메시지가 표시됩니다:

```
Buy now! Would 5% off convince you?
```

### 문자열 사용자 지정 속성을 통해 메시지 선택

{% raw %}

```liquid
{% if {{custom_attribute.${Game}}} == 'Game1' %}
You played our Game! We're so happy!
{% elsif{{custom_attribute.${Game}}} == 'Game2' %}
You played our other Game! Woop!{% else %}
Hey! Get in here and play this Game!
{% endif %}
```
{% endraw %}

![][14]

이 예제에서는 특정 게임을 플레이한 경우 다음과 같은 메시지가 표시됩니다:

```
You played our Game! We're so happy!
```

다른 지정된 게임을 플레이한 경우:

```
You played our other Game! Woop!
```

게임을 플레이한 적이 없거나 프로필에 해당 사용자 지정 속성이 존재하지 않는 경우 다음과 같은 메시지가 표시됩니다:

```
Hey! Get in here and play this Game!
```

### 위치에 따른 메시지 중단

거의 모든 것을 기준으로 메시지를 중단할 수 있습니다. 다음 예는 사용자가 특정 지역에 거주하지 않는 경우 프로모션, 쇼 또는 배달 자격이 없을 수 있으므로 메시지를 중단하는 방법을 보여줍니다.

{% raw %}
```liquid
{% if {{${time_zone.$}}} =='America/Los_Angeles' %}
Stream now!
{% else %}
{% abort_message () %}
{% endif %}
```
{% endraw %}

![][26]

연결된 콘텐츠를 기반으로 [메시지를 중단할][1] 수도 있습니다.


[1]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/aborting_connected_content/
[13]: {% image_buster /assets/img/liquid-if-totalspend.png %}
[14]: {% image_buster /assets/img/liquid-if-elsif-games.png %}
[25]:https://docs.shopify.com/themes/liquid/basics/operators
[26]: {% image_buster /assets/img/abort-if.png %}
