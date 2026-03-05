---
nav_title: 사용자 메시징하기
article_title: 메시지 사용자
description: "이 참조 문서는 Braze가 사용자 메시지를 처리하는 방법을 다룹니다."
page_type: reference
channel:
  - WhatsApp
page_order: 5.1
alias: /whatsapp_quick_replies/

---

# 사용자 메시지

> WhatsApp은 양방향 소통 채널입니다. 귀하의 브랜드는 사용자에게 메시지를 보낼 수 있을 뿐만 아니라 템플릿 캠페인 및 캔버스를 사용하여 대화에 참여할 수 있습니다. There are various ways to do this, including WhatsApp quick replies, list messages, and trigger words. Quick reply and list message calls-to-action (CTAs) are a great way to encourage user engagement with your WhatsApp messaging.

## 동작 기반 트리거 

Both campaigns and Canvases can start, branch, and have mid-journey changes from an inbound WhatsApp message (a user messaging your WhatsApp), such as a trigger word. 

사용자가 기대하는 트리거 단어와 일치하는지 확인하세요.

**알아야 할 사항:**
- 트리거 단어의 각 글자는 구성할 때 대문자로 작성해야 합니다. Braze는 사용자가 보낸 인바운드 트리거 단어가 대문자로 작성될 필요가 없습니다. 예를 들어, 메시징 "jOin2023"은 여전히 캔버스 또는 캠페인을 트리거합니다.
- 입력 일정 작업 기반 트리거에 트리거 단어가 지정되지 않은 경우 캠페인 또는 캔버스는 모든 수신 WhatsApp 메시지에 대해 실행됩니다. 이것은 활성 캠페인 및 캔버스 전반에 걸쳐 일치하는 구문이 있는 메시지를 포함하며, 이 경우 사용자는 두 개의 WhatsApp 메시지를 받게 됩니다.

{% tabs %}
{% tab Campaign %}

![액션 기반 캠페인 예약 옵션.]({% image_buster /assets/img/whatsapp/whatsapp27.png %})

{% endtab %}
{% tab Canvas %}

![작업 기반 캔버스 예약 옵션.]({% image_buster /assets/img/whatsapp/whatsapp25.png %})

{% endtab %}
{% endtabs %}

## 인식되지 않는 응답

대화형 캔버스에서 인식되지 않는 응답에 대한 옵션을 포함할 것을 권장합니다. 이 가이드는 사용자가 사용할 수 있는 프롬프트와 채널에 대한 기대치를 이해하도록 돕습니다. 기대 관리는 라이브 에이전트 채팅이 있는 WhatsApp 채널이 있는 경우 특히 유용할 수 있습니다. 
- 작업 단계에서 커스텀 필터 구문에 대한 작업 그룹을 만든 후 "WhatsApp 메시지 보내기"에 대한 추가 작업 그룹을 추가하지만 **메시지 본문을 확인하지 마세요**. 이것은 "else" 절과 유사하게 인식되지 않은 모든 사용자 응답을 포착합니다. 
- 이 채널은 관리되지 않으며 필요시 지원 채널로 안내하는 WhatsApp 메시지를 사용자에게 보내는 것을 권장합니다. 

## 빠른 답장 

![전화 화면에 표시된 실행 버튼이 클릭된 버튼의 텍스트에 응답합니다.]({% image_buster /assets/img/whatsapp/whatsapp11.png %}){: style="float:right;max-width:25%;margin-left:15px;border: 0;"}

빠른 답장은 대화 내에서 클릭 가능한 버튼 옵션으로 나타나지만 사용자가 텍스트로 응답한 것처럼 작동합니다. Braze는 이러한 메시지를 수신 메시지로 처리한 다음 클릭된 버튼에 따라 설정된 응답을 보낼 수 있습니다. 사용자의 응답을 만들고 필터링할 때 "인바운드 WhatsApp 메시지 작업" 단계를 사용하세요.

![WhatsApp 메시지가 텍스트와 세 개의 실행 버튼을 보여줍니다.]({% image_buster /assets/img/whatsapp/whatsapp13.png %}){: style="max-width:50%;"}

### Configure the quick reply experience in Canvas

#### 1단계: CTA 빌드

먼저, 메시지 템플릿 내 [WhatsApp 메시지 템플릿 매니저](https://business.facebook.com/wa/manage/message-templates/)에서 빠른 응답 CTA를 구축하세요. 

![WhatsApp 메시지 템플릿 매니저 UI가 CTA 버튼을 생성하는 방법을 보여주며, 버튼 유형(커스텀)과 버튼 텍스트를 제공합니다.]({% image_buster /assets/img/whatsapp/whatsapp12.png %}){: style="max-width:80%;"}

템플릿이 제출되고 WhatsApp에서 승인되면 Braze 내에서 캔버스를 구축하는 데 사용할 수 있습니다. 

{% alert tip %}
메시지 템플릿에서 승인을 받기 전에 캔버스를 빌드할 수 있습니다.
{% endalert %}

#### 2단계: 캔버스 비드

그 다음 생성한 템플릿이 포함된 메시지 단계로 캔버스를 빌드합니다. 

![빠른 답장 템플릿이 채워진 WhatsApp 단계별 메시지 작성기.]({% image_buster /assets/img/whatsapp/whatsapp14.png %})

메시지 단계에 따르는 작업 단계를 만듭니다. 이 작업 단계에서 빠른 응답 옵션당 하나의 그룹을 만드세요.

![평가 작업이 "whatsapp 수신 메시지 보내기"인 캔버스입니다.]({% image_buster /assets/img/whatsapp/whatsapp15.png %})

각 빠른 응답 옵션 그룹에 대해 일치하는 버튼과 동일한 텍스트를 지정하세요. 키워드는 대문자로 작성해야 합니다. 

![특정 메시지 본문이 수신될 때 "whatsapp 수신 메시지 보내기" 작업이 전송되도록 설정된 캔버스 단계입니다.]({% image_buster /assets/img/whatsapp/whatsapp16.png %})

사용자가 빠른 응답 대신 텍스트로 메시지에 응답하는 경우 기본 응답을 원하시면 일치하는 메시지 본문이 없는 추가 그룹을 만드십시오.

이 시점부터 계속해서 캔버스를 계속 구축하세요.

### 응답

대부분의 응답에 대해 답장 메시지를 원할 것입니다. 고객이 미리 정해진 프롬프트가 아닌 일반 메시지로 응답하는 경우와 같이 빠른 응답의 범위를 벗어난 응답에 대한 포괄적인 옵션을 권장합니다. 예를 들어, "죄송합니다. 응답을 인식하지 못했습니다." 지원 문제의 경우 <support channel>에게 메시지를 보내주세요."라고 할 수 있습니다

![각 클릭 유도 실행 버튼에 대한 응답을 보여주는 캔버스가 구축되었습니다.]({% image_buster /assets/img/whatsapp/whatsapp18.png %})

Braze 캔버스가 제공하는 후속 작업(예: 응답 메시지, 고객 프로필 업데이트 또는 Braze 간 웹훅)을 사용할 수 있습니다. 

## List messages

List messages appear as a body message with a list of clickable options. 각 목록은 여러 섹션을 가질 수 있으며, 각 목록은 최대 10개의 행을 가질 수 있습니다.

![다양한 패션 스타일에 대한 행이 포함된 WhatsApp 리스트 메시지의 예시입니다.]({% image_buster /assets/img/whatsapp/list_message_example.png %}){: style="max-width:40%;"}

### Configure the list message experience in Canvas

#### 1단계: Create or edit an existing action-based Canvases

You can only add WhatsApp list messages to Canvases that are action-based, as they need to be in response to a user message.

#### 2단계: Create a WhatsApp Message step

Add a WhatsApp [Message step]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/), and then select the response message layout of **List Message**.

!["목록 메시지"를 포함하여 만들 수 있는 다양한 유형의 WhatsApp 응답 메시지 모음입니다.]({% image_buster /assets/img/whatsapp/list_message_option.png %}){: style="max-width:70%;"}

Add a **List button** name that users will select to display your list. Then, use the fields in **List content** to create your list:

- **Section:** Add up to 10 sections to group and organize your list items. For example, a clothing retailer could use sections to organize by seasonal styles (like spring, summer, autumn, and winter) or clothing items (like tops, bottoms, and shoes).
- **Row:** Add up to 10 rows, or list items, across all sections.
- **Row description (optional):** Add an optional description to all rows (list items).

!['콘텐츠 목록' 섹션은 두 개의 섹션과 여러 행 및 행 설명으로 채워집니다.]({% image_buster /assets/img/whatsapp/list_content.png %}){: style="max-width:60%;"}

Change the order of sections and rows by selecting and dragging the icon next to their names.

![목록 섹션을 새 위치로 드래그합니다.]({% image_buster /assets/img/whatsapp/drag_list_order.png %}){: style="max-width:60%;"}

Back in the Canvas composer, add an [Action path]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/) after the Message step that has a group for each list response. In each group:

1. Add a trigger for **Sent inbound WhatsApp subscription group** and select the respective WhatsApp subscription group.
2. Check the **Where the message body** checkbox.
3. Specify the content for one row (or list item).

![다양한 의상 스타일에 대한 그룹이 있는 행동 경로에 대한 컴포저입니다.]({% image_buster /assets/img/whatsapp/action_path_list_message.png %})

Continue to build out your Canvas.

### Creating actions paths for long descriptions

If you have row descriptions, you must use **Matches regex** to specify a row. For example, if you want to specify a row with the description, "Our new style that fits over your favorite pair of ankle boots", you could use [regex]({{site.baseurl}}/user_guide/engagement_tools/segments/regex/) with "ankle boots".

!["정규식과 일치" 필터를 사용하여 '발목 부츠'가 포함된 응답 메시지를 캡처하는 WhatsApp 트리거입니다.]({% image_buster /assets/img/whatsapp/regex_list_message.png %})

## Considerations for response messages

Response messages need to be sent within 24 hours of receiving a user's message. To help build successful experiences, Braze checks the message logic to confirm there is an upstream inbound user message that unblocks the response message. 

The following events unblock response messages: 

- Inbound message 
  - [Action Path]({{site.baseurl}}/action_paths/) or [action-based entry]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/) with the trigger **Send a WhatsApp inbound message**.

!["WhatsApp 인바운드 메시지 보내기"라는 트리거가 있는 액션 기반 입력 단계입니다.]({% image_buster /assets/img/whatsapp/whatsapp_inbound_message_trigger.png %})

- [API-triggered entry]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/)
- Inbound product message 
  - [`ecommerce.cart_updated`]({{site.baseurl}}/user_guide/data/custom_data/recommended_events/ecommerce_events/?tab=ecommerce.cart_updated#types-of-ecommerce-recommended-events) event

![수행된 커스텀 이벤트의 트리거가 있는 행동 경로 `ecommerce.cart_updated`.]({% image_buster /assets/img/whatsapp/ecommerce_cart_updated.png %})

