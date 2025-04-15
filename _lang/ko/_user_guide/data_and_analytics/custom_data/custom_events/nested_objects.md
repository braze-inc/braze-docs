---
nav_title: 중첩된 개체
article_title: 사용자 지정 이벤트의 중첩된 개체
page_order: 1
page_type: reference
description: "이 문서에서는 중첩된 JSON 데이터를 사용자 지정 이벤트 및 구매의 속성으로 전송하는 방법과 메시징에서 이러한 중첩된 개체를 사용하는 방법에 대해 설명합니다."
---

# 사용자 지정 이벤트의 중첩된 개체

> 이 문서에서는 중첩된 JSON 데이터를 사용자 지정 이벤트 및 구매의 속성으로 전송하는 방법과 메시징에서 이러한 중첩된 개체를 사용하는 방법에 대해 설명합니다.

중첩 개체(다른 개체 안에 있는 개체)를 사용하여 사용자 지정 이벤트 및 구매의 속성으로 중첩된 JSON 데이터를 전송할 수 있습니다. 이 중첩된 데이터는 메시지에서 개인화된 정보를 템플릿화하고, 메시지 전송을 트리거하고, 세분화하는 데 사용할 수 있습니다.

## 제한 사항

- 중첩된 데이터는 [사용자 지정 이벤트]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/) 와 [구매 이벤트]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/purchase_events/) 모두에 지원되지만 다른 이벤트 유형은 지원되지 않습니다.
- 배열 또는 개체 값을 포함하는 이벤트 속성 개체는 최대 100KB의 이벤트 속성 페이로드를 가질 수 있습니다.
- 구매 이벤트에 대해서는 이벤트 속성 스키마를 생성할 수 없습니다.
- 이벤트 속성정보 스키마는 지난 24시간 동안의 커스텀 이벤트를 샘플링하여 생성됩니다.

### 최소 SDK 버전

다음 SDK 버전은 중첩된 개체를 지원합니다:

{% sdk_min_versions swift:5.0.0 android:1.0.0 web:3.3.0 %}

## 1단계: 스키마 생성

사용자 지정 이벤트의 중첩된 데이터에 액세스하려면 중첩된 이벤트 속성을 사용하여 각 이벤트에 대한 스키마를 생성합니다. 스키마를 생성하려면 다음 단계를 따르세요:

1. **데이터 설정** > **사용자 지정 이벤트로** 이동합니다.
2. 중첩된 속성정보 가 있는 이벤트의 **속성정보 관리**를 선택합니다.
3. <i class="fas fa-arrows-rotate"></i> 버튼을 선택하여 스키마를 생성합니다. 스키마를 보려면 <i class="fas fa-plus"></i> 더하기 버튼을 선택합니다.

![][6]{: style="max-width:80%;"}

## 2단계: 중첩된 개체 사용

스키마를 생성한 후에는 세분화 및 개인화 중에 중첩된 데이터를 참조할 수 있습니다. 사용 예는 다음 섹션을 참조하세요:

- [API 요청 본문](#api-request-body)
- [Liquid 템플릿](#liquid-templating)
- [메시지 트리거링](#message-triggering)
- [세분화](#segmentation)
- [개인화](#personalization)

### API 요청 본문

{% tabs %}
{% tab 음악 예제 %}

다음은 "생성된 재생 목록" 커스텀 이벤트가 포함된 `/users/track` 예시입니다. 재생 목록이 생성된 후 재생 목록의 속성을 캡처하기 위해 "노래"를 속성으로 나열하는 API 요청과 노래의 중첩된 속성의 배열을 전송합니다.

```
...
"properties": {
  "songs": [
    {
      "title": "Smells Like Teen Spirit",
      "artist": "Nirvana",
      "album": {
        "name": "Nevermind",
        "yearReleased": "1991"
      }
    },
    {
      "title": "While My Guitar Gently Weeps",
      "artist": "the Beatles",
      "album": {
        "name": "The Beatles",
        "yearReleased": "1968"
      }
    }
  ]
}
...
```
{% endtab %}
{% tab 레스토랑 예제%}

다음은 '주문됨' 사용자 지정 이벤트가 포함된 `/users/track` 예제입니다. 주문이 완료되면 해당 주문의 속성을 캡처하기 위해 "r_details"를 속성으로 나열하고 해당 주문의 중첩된 속성을 나열하는 API 요청을 보냅니다.

```
...
"properties": {
  "r_details": {
    "name": "McDonalds",
    "identifier": "12345678",
    "location" : {
      "city": "Montclair",
      "state": "NJ"
    }
  }
}
...
```
{% endtab %}
{% endtabs %}

### Liquid 템플릿

다음 Liquid 템플릿 예제는 앞의 API 요청에서 저장된 중첩된 속성정보를 참조하여 Liquid 메시징에 사용하는 방법을 보여줍니다. Liquid 및 점 표기법을 사용하여 중첩된 데이터를 탐색하여 메시지에 포함할 특정 노드를 찾습니다.

{% tabs %}
{% tab 음악 예제 %}
"생성된 재생 목록" 이벤트에 의해 트리거된 메시지에서 Liquid에서 템플릿을 지정합니다.

{% raw %}
`{{event_properties.${songs}[0].album.name}}`: "신경 쓰지 마"<br>
`{{event_properties.${songs}[1].title}}`: "내 기타가 부드럽게 우는 동안"
{% endraw %}

{% endtab %}
{% tab 레스토랑 예시 %}
"주문됨" 이벤트에 의해 트리거된 메시지에서 Liquid의 템플릿을 생성합니다.

{% raw %}
`{{event_properties.${r_details}.location.city}}`: "몽클레어"
{% endraw %}

{% endtab %}
{% endtabs %}

### 메시지 트리거링

이러한 속성을 사용하여 캠페인을 트리거하려면 사용자 지정 이벤트 또는 구매를 선택하고 **중첩된 속성** 필터를 추가합니다. 인앱 메시지에는 아직 메시지 트리거링이 지원되지 않지만, 메시지의 Liquid 개인 설정에서 중첩된 속성은 계속 표시됩니다.

{% tabs %}
{% tab 음악 예제 %}

'생성된 재생 목록' 이벤트에서 중첩된 속성이 있는 캠페인을 트리거합니다:

![사용자 지정 이벤트에서 속성 필터를 위해 중첩된 속성을 선택하는 사용자.]({% image_buster /assets/img/nested_object2.png %})

트리거 조건 `songs[].album.yearReleased` "is" "1968"은 1968년에 발매된 앨범이 있는 노래가 있는 이벤트와 일치합니다. 배열을 트래버스할 때는 괄호 표기법 `[]`를 사용하고, 트래버스된 배열의 **항목**이 이벤트 속성정보와 일치하는 경우 일치시킵니다.

{% alert important %}
**does not equal** 필터는 배열의 속성이 제공된 값과 같지 않을 때만 일치합니다. <br><br>예를 들어, 캔버스 A에 액션 기반 커스텀 이벤트 중첩 속성 필터 **equals** "스마트워치"가 있고, 캔버스 B에 액션 기반 커스텀 이벤트 중첩 속성 필터 **does not equal** "심폰"이 있다고 가정해 보겠습니다. 당신의 속성에 "스마트워치"와 "심폰"이 있다면, 두 개의 캔버스가 트리거됩니다. 그러나 속성에 "simphone" 또는 "sim only"가 있는 경우, 캔버스는 트리거되지 않습니다.
{% endalert %}

{% endtab %}
{% tab 레스토랑 예시 %}

'주문됨' 이벤트에서 중첩된 속성이 있는 캠페인을 트리거합니다:

![커스텀 이벤트에 대해 속성 필터 r_details.name을 McDonalds로 추가하는 사용자.]({% image_buster /assets/img/nested_object1.png %})

`r_details.name`: "맥도날드"<br>
`r_details.location.city`: "몽클레어"
{% endtab %}
{% endtabs %}

{% alert note %}
이벤트 속성에 `[]` 또는 `.` 문자가 포함된 경우 큰따옴표로 묶어 이스케이프 처리하세요. 예를 들어 `"songs[].album".yearReleased`는 이벤트와 리터럴 속성정보 `"songs[].album"`을 일치시킵니다.
{% endalert %}

### 세분화

중첩된 이벤트 속성정보를 기반으로 사용자를 세분화하려면 [세그먼트 확장]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/)을 사용해야 합니다. 스키마를 생성한 후에는 중첩된 개체 탐색기가 세분화 섹션에 표시됩니다. 

![][4]

세분화는 트리거링과 동일한 표기법을 사용합니다( [메시지 트리거링](#message-triggering) 참조).

### 개인화

**개인화 추가** 모달을 사용하여 개인화 유형으로 **고급 이벤트 속성을** 선택합니다. 이 옵션을 사용하면 스키마가 생성된 후 중첩된 이벤트 속성정보를 추가할 수 있습니다.

![][5]{: style="max-width:70%;"}

## 자주 묻는 질문

### 중첩된 개체를 사용하면 추가 데이터 포인트가 소모되나요?

이 기능을 추가해도 데이터 포인트 과금 방식에는 변화가 없습니다. 중첩된 개체를 기반으로 세그먼트를 분할하는 경우 세그먼트 확장을 사용하므로 추가 데이터 포인트 사용량이 발생하지 않습니다.

### 중첩된 데이터는 얼마나 많이 전송할 수 있나요?

이벤트의 속성 중 하나 이상에 중첩된 데이터가 포함된 경우, 이벤트의 모든 결합된 속성에 대한 최대 페이로드는 100KB입니다. 이 크기 제한을 초과하는 요청은 거부됩니다.

[4]: {% image_buster /assets/img_archive/nested_event_properties_segmentation.png %}
[5]: {% image_buster /assets/img_archive/nested_event_properties_personalization.png %}
[6]: {% image_buster /assets/img_archive/schema_generation_example.png %}