---
nav_title: "인앱 메시지"
article_title: 인앱 메시지
page_order: 2
alias: /in-app_messages/
description: "이 랜딩 페이지에서는 인앱 메시지의 모든 것을 확인할 수 있습니다. 여기에서 인앱 메시지 작성 방법, 드래그 앤 드롭 편집기, 메시지 커스텀 방법, 리포팅 등에 대한 도움말을 확인할 수 있습니다."
channel:
  - in-app messages
search_rank: 5
---

# [![Braze 학습 과정]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/messaging-channels-in-app-in-browser){: style="float:right;width:120px;border:0;" class="noimgborder"} 인앱 메시지

> 인앱 메시지는 푸시 알림으로 사용자의 하루를 방해하지 않고 콘텐츠를 사용자에게 전달하는 데 도움을 줍니다. 이러한 메시지는 사용자의 앱 외부에서 전달되지 않으며 홈 화면을 침범하지 않습니다. 

커스텀 인앱 메시지는 사용자 경험을 향상시키고 오디언스가 앱에서 최대한의 가치를 얻을 수 있도록 도와줍니다. 다양한 레이아웃과 사용자 지정 도구를 선택할 수 있는 인앱 메시지는 그 어느 때보다 사용자의 참여를 유도할 수 있습니다. 이들은 맥락을 가지고 있으며 긴급성이 낮고 사용자가 앱 내에서 활동할 때 전달됩니다. 인앱 메시지의 예시는 [고객 사례](https://www.braze.com/customers/)를 확인하세요.

## 사용 사례

인앱 메시지에서 제공하는 풍부한 수준의 콘텐츠를 통해 이 채널을 다양한 사용 사례에 활용할 수 있습니다.

| 사용 사례 | 설명 |
| --- | --- |
| 푸시 프라이밍 | Run a [push priming]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/) campaign using a rich in-app message to show your customers the benefit of opting into push for your app or site, and present them with a prompt to grant push permission.
| 영업 및 프로모션 | 모달 인앱 메시지를 사용하여 정적 프로모션 코드 또는 오퍼가 포함된 시각적으로 매력적인 미디어로 고객을 맞이하세요. 그렇지 않았다면 구매나 전환을 하지 않았을 고객이 구매나 전환을 하도록 인센티브를 제공하세요. |
| 기능 채택 장려 | 고객이 앱의 다른 부분을 사용하거나 서비스를 이용하도록 유도하세요. |
| 고도로 개인화된 캠페인 | 고객이 앱이나 사이트에 들어왔을 때 가장 먼저 보게 되는 인앱 메시지를 배치하세요. Add in some Braze personalization features, such as [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/), to compel users to take action and therefore make your outreach more effective.
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

고려해야 할 다른 사용 사례는 다음과 같습니다:

- 새로운 앱 기능
- 앱 관리
- 리뷰
- 앱 업그레이드 또는 업데이트
- 경품 및 경품 행사

## 표준 메시지 유형

다음 탭은 사용자가 슬라이드업, 모달, 전체 화면 인앱 메시지 등 표준 인앱 메시지 유형 중 하나를 열었을 때 어떤 모습인지 보여줍니다.

{% tabs %}
{% tab Slideup %}

슬라이드업 메시지는 일반적으로 앱 화면의 상단과 하단에 표시됩니다(메시지를 작성할 때 설정할 수 있음). 새로운 서비스 약관, 쿠키 및 기타 정보 스니펫에 대해 사용자에게 알리는 데 유용합니다.

![앱 화면 하단에서 슬라이드업 인앱 메시지가 나타납니다. 슬라이드업에는 아이콘 이미지와 간단한 메시지가 포함됩니다.]({% image_buster /assets/img/slideup-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab Modal %}

모달은 기기의 화면 중앙에 나타나며 화면 오버레이가 있어 배경의 앱과 구분됩니다. 사용자에게 세일이나 경품 행사를 이용하도록 은근히 제안하는 데 적합합니다.

![앱 및 웹사이트의 중앙에 대화 상자로 표시되는 모달 인앱 메시지. 모달에는 이미지, 헤더, 메시지 본문 및 두 개의 버튼이 포함됩니다.]({% image_buster /assets/img/modal-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab Fullscreen %}

전체 화면 메시지는 기기의 전체 화면을 차지하는, 여러분이 기대하는 바로 그 메시지입니다! 이 메시지 유형은 필수 앱 업데이트와 같이 사용자의 주의가 정말 필요한 경우에 유용합니다.

![앱 화면을 차지하는 전체 화면 인앱 메시지. 전체 화면 메시지에는 큰 이미지, 헤더, 메시지 본문 및 두 개의 버튼이 포함됩니다.]({% image_buster /assets/img/full-screen-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% endtabs %}

이러한 기본 메시지 템플릿 외에도, 커스텀 HTML 인앱 메시지, CSS가 포함된 웹 모달 또는 웹 이메일 캡처 양식을 사용하여 메시징을 추가로 사용자화할 수 있습니다. For more information, refer to [Customization]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/).

## 템플릿 인앱 메시지

인앱 메시지는 **캠페인 적격성 재평가 후 표시**가 선택되거나 메시지에 다음 Liquid 태그가 존재하는 경우 템플릿 인앱 메시지로 전달됩니다:

- `canvas_entry_properties`
- `connected_content`
- {% raw %}`{sms.${*}}`{% endraw %}와 같은 SMS 변수
- `catalog_items`
- `catalog_selection_items`
- `event_properties`

이는 세션 시작 중에 장치가 전체 메시지 대신 해당 인앱 메시지의 트리거를 수신함을 의미합니다. 사용자가 인앱 메시지를 트리거하면 사용자의 기기가 실제 메시지를 가져오기 위해 네트워크 요청을 보냅니다.

{% alert note %}
장치가 인터넷에 접근할 수 없는 경우 메시지는 전달되지 않습니다. Liquid 로직이 해결되는 데 너무 오랜 시간이 걸리면 메시지가 전달되지 않을 수 있습니다.
{% endalert %}

## 중단 동작

Braze에서는 사용자가 메시지를 받을 자격이 있는 행동을 취했지만 Liquid 로직이 그들을 자격이 없다고 표시하여 메시지를 받지 못할 때 중단이 발생합니다. For example:

1. 샘은 이메일 캠페인을 트리거해야 하는 행동을 수행합니다.
2. 이메일 본문에는 커스텀 속성 점수가 50 미만일 경우 이 이메일을 보내지 말라는 Liquid 로직이 포함되어 있습니다.
3. 샘의 커스텀 속성 점수는 20입니다.
4. Braze는 샘이 이 이메일을 받지 않아야 한다고 인식하고 이메일이 중단됩니다.
5. 중단 이벤트가 기록됩니다.

그러나 인앱 메시지는 풀 채널이기 때문에 중단 방식이 약간 다르게 작동합니다.

### 인앱 메시지 중단 동작

인앱 메시지는 세션 시작 시 기기에 의해 가져오고 기기에 캐시되므로 인터넷 연결 품질에 관계없이 메시지가 사용자에게 즉시 전달될 수 있습니다. 예를 들어, 사용자가 세션 내에서 다섯 개의 인앱 메시지를 받으면 세션 시작 시 다섯 개 모두를 받게 됩니다. 메시지는 로컬에 캐시되며 정의된 트리거 이벤트가 발생할 때 나타납니다(세션 시작, 사용자가 커스텀 이벤트를 기록하는 버튼 클릭 등).

다시 말해, 인앱 메시지를 중단해야 하는지 여부를 결정하는 논리는 트리거가 발생하기 **전에** 발생합니다. 이를 보여주기 위해 이메일 예제의 샘이 푸시 알림을 구독하고 있다고 가정해 보겠습니다.

1. 샘은 전화에서 Braze 기반 앱을 실행하여 세션을 시작합니다.
2. 작업 공간의 활성 캠페인에 대한 오디언스 기준에 따라 샘은 다섯 가지 다른 캠페인에 적합할 수 있습니다. 모든 다섯 개가 그의 전화로 가져와지고 캐시됩니다.
3. 샘은 이러한 메시지를 트리거할 수 있는 어떤 행동도 **하지 않았습니다**, 하지만 세션에서 해당 메시지를 받을 수 있습니다.
4. 두 개의 인앱 메시지에 있는 Liquid는 샘이 메시지를 받지 못하도록 하는 규칙이 있습니다(예: 점수 커스텀 속성이 충분히 높지 않음).
5. 샘은 그들을 제외하는 두 개의 인앱 메시지를 받지 않지만, 나머지 세 개의 메시지는 받습니다.
6. 중단 이벤트는 기록되지 않습니다.

Braze는 샘의 경우 중단 이벤트를 기록하지 않는데, 이는 중단의 정의를 충족하지 않기 때문입니다; 샘은 메시지를 트리거할 수 있는 어떤 행동도 **하지 않았습니다**. 인앱 메시지의 경우, 사용자는 Braze가 메시지를 보여주지 않아야 한다고 판단하기 전에 실제로 트리거를 수행하지 않습니다.

#### 템플릿 인앱 메시지 중단 동작

[템플릿 인앱 메시지](#templated-in-app-messages)는 트리거 이벤트가 발생할 때 메시지를 표시해야 하는지 SDK가 재평가하도록 강제합니다. 이는 다른 중단 동작을 가집니다. 이를 보여주기 위해 이 예제를 고려해 보겠습니다:

1. 샘은 자신의 전화에서 Braze 기반 앱을 실행하여 Braze 세션을 시작합니다.
2. 활성 캠페인의 청중 기준에 따르면 샘은 템플릿 인앱 메시지의 자격이 있을 수 있으므로 트리거 정보가 메시지 페이로드 없이 그의 기기로 전송됩니다.
3. 샘은 커스텀 이벤트를 기록하는 버튼을 선택하여 템플릿 인앱 메시지를 트리거합니다.
4. 샘의 기기는 인앱 메시지를 가져오기 위해 네트워크 요청을 합니다.
5. 메시지의 Liquid 논리로 인해 중단이 발생하므로 Braze는 이를 중단으로 기록합니다. 샘은 이 평가 이전에 트리거 동작을 수행했습니다.

##### 인앱 메시지 중단 동작 비교

이 표는 샘이 경험한 인앱 메시지 흐름을 비교합니다:

| In-app message | 중단 동작 |
| --- | --- |
| Standard | 샘이 메시지를 트리거할 수 있는 동작을 수행하지 않았기 때문에 중단 이벤트가 기록되지 않았습니다.<br><br>표준 인앱 메시지는 중단을 기록하지 않는데, 중단의 정의는 "트리거 동작을 수행했음에도 메시지를 보지 못했다"입니다. 인앱 메시지는 트리거 동작이 발생하기 전에 기기로 전달되므로 Liquid 논리로 인해 인앱 메시지가 생략되었다고 간주하는 것은 의미가 없습니다. |
| 템플릿 | 샘이 템플릿 인앱 메시지를 트리거하기 위해 트리거 동작을 수행했지만 Liquid 템플릿에서 중단을 받았기 때문에 중단 이벤트가 기록되었습니다. <br><br>템플릿 인앱 메시지는 Liquid 평가가 트리거 동작이 수행된 후에 발생하기 때문에 중단을 기록합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 추가 자료

Before you get started with creating your own in-app message campaigns—or using in-app messages in a multi-channel campaign—we highly recommend that you check out our [In-app message prep guide]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/best_practices/prep_guide/). 이 가이드에서는 인앱 메시지를 작성할 때 고려해야 할 타겟팅, 콘텐츠 및 전환 관련 질문에 대해 설명합니다.
