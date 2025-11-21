---
nav_title: 메시지 
article_title: 메시지 
alias: "/message_step/"
page_order: 5
page_type: reference
description: "이 참고 문서에서는 메시지 단계를 사용하여 독립형 메시지를 만드는 방법에 대해 설명합니다."
tool: Canvas

---

# 메시지 

> 메시지 단계를 사용하면 캔버스에서 원하는 위치에 독립형 메시지를 추가할 수 있습니다.

푸시 채널을 사용하여 "점심 프로모션"이라는 이름의 메시지 단계.]({% image_buster /assets/img/canvas_components/message_step1.png %}){: style="float:right;max-width:25%;margin-left:15px;"}

## 메시지 작성하기

메시지 컴포넌트를 만들려면 먼저 캔버스에 단계를 추가합니다. 사이드바에서 컴포넌트를 드래그 앤 드롭하거나 단계 하단에 있는 <i class="fas fa-plus-circle"></i> 더하기 버튼을 선택하고 **메시지를** 선택합니다. 

### 1단계: 메시징 채널 선택하기

다음 메시징 채널 중에서 선택할 수 있습니다: 
- 콘텐츠 카드
- 이메일
- LINE
- 푸시 알림
- SMS/MMS/RCS
- 인앱 메시지 
- 웹훅
- WhatsApp

메시지 단계에 선택할 수 있는 메시징 채널 목록입니다.]({% image_buster /assets/img/canvas_components/message_step2.png %})

### 2단계: 전달 설정 편집하기

다음으로 지능형 전달, 방해금지 시간 재정의 및 전달 유효성 검사에 대한 설정을 편집할 수 있습니다.

#### Intelligent Timing

사용자 프로필에 최적의 시간을 계산할 수 있는 데이터가 충분하지 않은 경우 대체 옵션으로 [Intelligent Timing을]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/) 인에이블먼트할 수 있습니다. 사용자가 메시지 단계에 진입한 후 실제 메시지 전송까지 지연이 발생하는지 추가로 확인하기 위해 Intelligent Timing 및 [속도 제한을]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#rate-limiting-and-frequency-capping/) 인에이블먼트하는 것이 좋습니다.

**전달 설정** 탭에서 **Intelligent Timing 사용을** 선택합니다. 여기에서 가장 인기 있는 시간 또는 특정 대체 시간을 선택할 수 있습니다. 방해금지 시간이 인에이블먼트된 경우 메시지 단계에서도 이 설정을 재정의할 수 있습니다.

#### 전달 유효성 검사

전달 유효성 검사는 메시지 전송 시 오디언스가 전달 기준을 충족하는지 확인하기 위한 추가 확인 기능을 제공합니다. 이 설정은 조용한 시간, Intelligent Timing 또는 속도 제한이 활성화된 경우에 권장됩니다. 메시지 세그먼트 또는 추가 필터를 추가하여 메시지 전송 시 유효성을 검사할 수 있습니다. 사용자가 메시지 단계에 대해 설정된 전달 유효성 검사를 충족하지 않으면 해당 단계에서 캔버스를 종료합니다.

메시지 컴포넌트 설정을 위한 전달 설정 탭입니다. 조용한 시간을 인에이블먼트하고, 최적의 시간에 메시지를 전달하기 위해 지능형 타이밍 사용 확인란을 선택합니다. 메시지 전송 시 오디언스의 유효성을 검사하기 위해 전달 유효성 검사를 인에이블먼트합니다.]({% image_buster /assets/img/canvas_components/message_step4.png %}){: style="max-width:90%;"}

## 사용자 진행 방법

메시지 단계에 진입한 모든 사용자는 다음 조건 중 하나라도 충족되면 다음 단계로 진행됩니다:

- 모든 메시징이 전송됩니다.
- 메시지가 최대 게재빈도 설정되어 전송되지 않습니다.
- 메시징이 중단되었습니다.
- 채널로 사용자에게 연결할 수 없으므로 메시지가 전송되지 않습니다.

{% raw %}
작업 기반 캔버스가 인바운드 SMS 메시지에 의해 트리거되는 경우 첫 번째 단계(메시지 단계) 또는 작업 경로 단계 아래에 중첩된 메시지 단계에서 SMS 속성을 참조할 수 있습니다. 예를 들어 메시지 단계에서 `{{sms.${inbound_message_body}}}` 또는 `{{sms.${inbound_media_urls}}}` 을 사용할 수 있습니다.
{% endraw %}

## 캔버스 항목 속성 참조하기

캔버스 입력 속성은 캔버스 생성의 **입력 일정** 단계에서 구성되며 사용자를 캔버스에 입력하는 트리거를 나타냅니다. 이러한 속성은 API 트리거 캔버스에 있는 항목 페이로드의 속성에도 액세스할 수 있습니다. `canvas_entry_properties` 객체의 최대 크기 제한은 50KB입니다. 

항목 속성은 Liquid에서 모든 메시지 단계에서 사용할 수 있습니다. 이러한 항목 속성을 참조할 때 다음 Liquid를 사용하십시오: {% raw %}``canvas_entry_properties${property_name}``{% endraw %}. 이 방법을 사용하려면 이벤트가 커스텀 이벤트 또는 구매 이벤트여야 합니다.

{% alert note %}
특히 인앱 메시지 채널의 경우 `canvas_entry_properties` 은 캔버스에서만 참조할 수 있습니다.
{% endalert %}

이러한 항목 속성을 참조할 때 다음 Liquid를 사용하십시오: {% raw %}``canvas_entry_properties${property_name}``{% endraw %}. 이 방법을 사용하려면 이벤트가 커스텀 이벤트 또는 구매 이벤트여야 합니다.

{% raw %}
예를 들어 다음 요청을 고려해 보세요: `\"canvas_entry_properties\" : {\"product_name\" : \"shoes\", \"product_price\" : 79.99}`. Liquid `{{canvas_entry_properties.${product_name}}}` 를 사용하여 메시징에 "신발"이라는 단어를 추가할 수 있습니다.
{% endraw %}

또한 메시지 단계의 [지속성 항목 속성정보를]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/canvas_persistent_entry_properties/) 활용하여 캔버스 워크플로 전체에서 개인화된 단계를 통해 사용자를 안내할 수 있습니다.

### 이벤트 속성정보

이벤트 속성은 커스텀 이벤트 및 구매 이벤트에 대해 설정하는 속성을 말합니다. 이러한 이벤트 속성정보는 캔버스뿐만 아니라 실행 기반 전달이 있는 캠페인에서도 사용할 수 있습니다. 

캔버스에서 커스텀 이벤트 및 구매 이벤트 속성정보는 [행동 경로]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/) 단계를 따르는 모든 메시지 단계에서 Liquid에서 사용할 수 있습니다. 예를 들어 `event_properties` 을 참조할 때는 이 Liquid 스니펫을 사용합니다: {% raw %}``{{event_properties.${property_name}}}``{% endraw %} 

{% alert important %}
`event_properties` 는 행동 경로 단계와 독립적으로 사용할 수 없습니다.
{% endalert %}

행동 경로 다음의 첫 번째 메시지 단계에서 해당 행동 경로에 참조된 이벤트와 관련된 `event_properties` 을 사용할 수 있습니다. 이 행동 경로 단계와 메시지 단계 사이에 다른 단계(다른 행동 경로나 메시지 단계가 아닌)를 가질 수 있습니다. 메시지 단계가 행동 경로 단계의 모든 사람이 아닌 경로로 추적할 수 있는 경우에만 `event_properties` 에 액세스할 수 있습니다.

{% alert important %}
리드 메시지 단계에서는 `event_properties` 을 사용할 수 없습니다. 대신 `canvas_entry_properties` 을 사용하거나 `event_properties` 을 포함하는 메시지 단계 앞에 해당 이벤트가 있는 행동 경로 단계를 추가해야 합니다.
{% endalert %}

{% details Expand for original Canvas editor %}

더 이상 원본 편집기를 사용하여 캔버스를 만들거나 복제할 수 없습니다. 이 섹션은 참고용으로만 제공됩니다.

- `event_properties` 는 예약된 전체 단계에서 사용할 수 없습니다. 그러나 전체 단계가 예약되어 있더라도 액션 기반 캔버스의 첫 번째 전체 단계에서는 `event_properties` 을 사용할 수 있습니다.
- `canvas_entry_properties` 는 캔버스의 첫 번째 전체 단계에서만 참조할 수 있습니다.
- 특히 인앱 메시지 채널의 경우, 이전 얼리 액세스에서 지속성 항목 속성정보를 인에이블먼트한 경우 원래 캔버스 에디터에서 `canvas_entry_properties` 을 참조할 수 있습니다.

{% enddetails %}

## 분석

메시지 컴포넌트 측정기준의 정의는 다음 표를 참조하세요: 

| 측정기준 | 설명 |
| --- | --- |
| _항목_ | 단계를 입력한 횟수입니다. 캔버스에 재인증 자격이 있는 사용자가 메시지 단계를 두 번 입력하면 두 개의 항목이 기록됩니다. |
| _다음 단계로 진행_ | 캔버스에서 다음 단계로 진행된 항목 수입니다. |
| _전송_ | 스텝이 보낸 총 메시지 수입니다. 캔버스 자격이 다시 부여되고 사용자가 메시지 단계를 두 번 입력하면 두 개의 항목이 기록됩니다. |
| _고유 수신자_ | 이 단계에서 메시지를 받은 사용자 수입니다. |
| _주요 전환 이벤트_ | Braze 캠페인에서 수신한 메시지를 상호 작용하거나 본 후 정의된 이벤트가 발생한 횟수입니다. 캠페인을 구축할 때 이 이벤트를 정의합니다. |
| _매출_ | 설정된 기본 전환 기간 내에 캠페인 수신자로부터 발생한 총 매출(달러)입니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }


