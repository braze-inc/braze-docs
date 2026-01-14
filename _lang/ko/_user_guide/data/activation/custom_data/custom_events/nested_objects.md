---
nav_title: 중첩된 개체
article_title: 커스텀 이벤트의 중첩된 오브젝트
page_order: 1
page_type: reference
description: "이 문서에서는 중첩된 JSON 데이터를 커스텀 이벤트 및 구매 속성정보로 전송하는 방법과 메시징에서 이러한 중첩된 오브젝트를 사용하는 방법에 대해 설명합니다."
---

# 커스텀 이벤트의 중첩된 오브젝트

> 이 페이지에서는 중첩된 JSON 데이터를 커스텀 이벤트 및 구매 속성정보로 전송하는 방법과 메시징에서 이러한 중첩된 오브젝트를 사용하는 방법에 대해 설명합니다.

다른 객체 안에 있는 객체인 커스텀 오브젝트를 사용하여 중첩된 JSON 데이터를 커스텀 이벤트 및 구매 속성정보로 전송할 수 있습니다. 이 중첩된 데이터는 메시지에서 개인화된 정보를 템플릿화하고, 메시지 전송을 트리거하고, 사용자를 세분화하는 데 사용할 수 있습니다.

## 제한 사항

- 중첩된 데이터는 [커스텀 이벤트]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) 와 [구매 이벤트]({{site.baseurl}}/user_guide/data/custom_data/purchase_events/) 모두에 지원되지만 다른 이벤트 유형에는 지원되지 않습니다.
- 배열 또는 오브젝트 값을 포함하는 이벤트 속성정보 객체는 최대 100KB의 이벤트 속성 페이로드를 가질 수 있습니다.
- 구매 이벤트에 대한 이벤트 속성정보 스키마는 생성할 수 없습니다.
- 이벤트 속성정보 스키마는 지난 24시간 동안의 커스텀 이벤트를 샘플링하여 생성됩니다.

### 최소 소프트웨어 개발 키트 버전

다음 소프트웨어 개발 키트 버전은 중첩 개체를 지원합니다:

{% sdk_min_versions swift:5.0.0 android:1.0.0 web:3.3.0 %}

## 1단계: 스키마 생성

중첩된 이벤트 속성정보가 있는 각 이벤트에 대한 스키마를 생성하여 커스텀 이벤트의 중첩된 데이터에 액세스할 수 있습니다. 스키마를 생성합니다:

1. **데이터 설정** > 커스텀 이벤트로 이동합니다.
2. 중첩된 이벤트 속성정보가 있는 이벤트의 **속성 관리를** 선택합니다.
3. <i class="fas fa-arrows-rotate"></i> 버튼을 선택하여 스키마를 생성합니다. 스키마를 보려면 <i class="fas fa-plus"></i> 더하기 버튼을 선택합니다.

\![]({% image_buster /assets/img_archive/schema_generation_example.png %}){: style="max-width:80%;"}

나중에 새 속성이 전송되면 스키마가 다시 생성될 때까지 해당 속성은 스키마에 포함되지 않습니다. 스키마는 24시간마다 재생성할 수 있습니다.

## 2단계: 중첩된 개체 사용

세분화 및 개인화 중에 중첩된 데이터를 참조할 수 있습니다. 스키마는 필요하지 않습니다. 사용 예는 다음 섹션을 참조하세요:

- [API 요청 본문](#api-request-body)
- [Liquid 템플레이트](#liquid-templating)
- [메시지 트리거된 메시지](#message-triggering)
- [세그먼트 세분화](#segmentation)
- [개인화](#personalization)

### API 요청 본문

{% tabs %}
{% tab Music Example %}

다음은 '생성된 재생 목록' 커스텀 이벤트가 포함된 `/users/track` 예시입니다. 재생목록이 생성되면 전송을 통해 재생목록의 속성을 캡처합니다:
- "노래"를 속성으로 나열하는 API 요청
- 노래의 중첩된 속성 배열

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
{% tab Restaurant Example%}

다음은 '주문됨' 커스텀 이벤트가 포함된 `/users/track` 예시입니다. 주문이 완료된 후에는 전송을 통해 해당 주문의 속성을 캡처합니다:
- "r_details" 을 속성으로 나열하는 API 요청
- 해당 주문의 중첩된 속성

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

{% alert note %}
중첩된 커스텀 이벤트 속성정보의 경우 연도가 0보다 작거나 3000보다 크면 Braze는 사용자에게 이 값을 저장하지 않습니다.
{% endalert %}

### Liquid 템플레이트

다음은 [이전 API 요청](#api-request-body)에서 요청한 중첩된 프로퍼티를 참조하는 Liquid 템플릿을 만드는 방법을 보여줍니다.

{% tabs %}
{% tab Music Example %}
"생성된 재생 목록" 이벤트에 의해 트리거된 메시지에서 Liquid에서 템플릿을 지정합니다:

{% raw %}
`{{event_properties.${songs}[0].album.name}}`: "네버마인드"<br>
`{{event_properties.${songs}[1].title}}`: "내 기타가 부드럽게 우는 동안"
{% endraw %}

{% endtab %}
{% tab Restaurant Example %}
"주문됨" 이벤트에 의해 트리거된 메시지를 Liquid에서 템플릿화합니다:

{% raw %}
`{{event_properties.${r_details}.location.city}}`: "몽클레어"
{% endraw %}

{% endtab %}
{% endtabs %}

### 메시지 트리거된 메시지

이러한 속성을 사용하여 캠페인을 트리거하려면 커스텀 이벤트 또는 구매를 선택한 다음 **중첩된** 이벤트 속성정보 필터를 추가합니다. 인앱 메시지에는 아직 메시지 트리거가 지원되지 않지만 메시지의 Liquid 개인화에서 중첩된 속성은 계속 표시됩니다.

{% tabs %}
{% tab Music Example %}

'생성된 재생목록' 이벤트에서 중첩된 이벤트 속성정보로 캠페인을 트리거합니다:

\![커스텀 이벤트에서 속성 필터를 위해 중첩된 이벤트 속성정보를 선택하는 사용자.]({% image_buster /assets/img/nested_object2.png %})

트리거 조건 `songs[].album.yearReleased` "is" "1968"은 노래 중 1968년에 발매된 앨범이 있는 이벤트와 일치합니다. 배열을 트래버스할 때는 괄호 표기법 `[]` 을 사용하고, 트래버스된 배열의 **항목이** 이벤트 속성정보와 일치하는 경우 일치시킵니다.

{% alert important %}
**같지 않음** 필터는 배열의 속성 중 제공된 값과 동일한 속성이 없는 경우에만 일치합니다. <br><br>예를 들어 캔버스 A의 액션 기반 커스텀 이벤트 중첩된 **속성정보** 필터가 '스마트워치'이고 캔버스 B의 액션 기반 커스텀 이벤트 중첩된 속성정보 필터가 '스마트폰' **이 아니라고** 가정해 보겠습니다. 속성에 "스마트워치"와 "스마트폰"이 있는 경우 두 캔버스 모두 트리거됩니다. 그러나 어떤 속성에 '심폰' 또는 '심 전용'이 있는 경우 어느 캔버스도 트리거되지 않습니다.
{% endalert %}

{% endtab %}
{% tab Restaurant Example %}

'주문됨' 이벤트에서 중첩된 이벤트 속성정보로 캠페인을 트리거합니다:

\![커스텀 이벤트를 위해 속성 필터 r_details.name 를 추가하는 사용자는 맥도날드입니다.]({% image_buster /assets/img/nested_object1.png %})

`r_details.name`: "맥도날드"<br>
`r_details.location.city`: "몽클레어"
{% endtab %}
{% endtabs %}

{% alert note %}
이벤트 속성정보에 `[]` 또는 `.` 문자가 포함된 경우 큰따옴표로 묶어 이스케이프 처리하세요. 예를 들어 `"songs[].album".yearReleased` 은 이벤트와 리터럴 속성정보 `"songs[].album"` 를 일치시킵니다.
{% endalert %}

### 세그먼트 세분화

중첩된 이벤트 속성정보를 기반으로 사용자를 세분화하려면 [세그먼트 확장을]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/) 사용해야 합니다. 스키마를 생성한 후에는 중첩된 개체 탐색기가 세그먼트 섹션에 표시됩니다. 

\![]({% image_buster /assets/img_archive/nested_event_properties_segmentation.png %})

세분화는 트리거링과 동일한 표기법을 사용합니다( [메시지 트리거링](#message-triggering) 참조).

세그먼트 확장을 편집하거나 만들려면 '세그먼트 편집' 권한이 필요합니다.

### 개인화

**개인화 추가** 모달을 사용하여 개인화 유형으로 **고급 이벤트 속성정보를** 선택합니다. 이 옵션을 사용하면 스키마가 생성된 후 중첩된 이벤트 속성정보를 추가할 수 있습니다.

\![]({% image_buster /assets/img_archive/nested_event_properties_personalization.png %}){: style="max-width:70%;"}

## 자주 묻는 질문

### 중첩된 개체를 사용하면 추가 데이터 포인트가 기록되나요?

이 기능을 추가해도 데이터 포인트를 기록하는 방식에는 아무런 변화가 없습니다. 중첩된 개체를 기반으로 세분화할 때는 추가 데이터 포인트를 사용하지 않는 세그먼트 확장을 사용합니다.

### 중첩된 데이터를 얼마나 많이 전송할 수 있나요?

이벤트 속성정보 중 하나 이상에 중첩된 데이터가 포함된 경우, 이벤트에 결합된 모든 속성의 최대 페이로드는 100KB입니다. 이 크기 제한을 초과하는 요청은 거부됩니다.

