---
nav_title: 사용자에게 메시지 전송
article_title: 사용자에게 메시지 전송
description: "이 참조 문서에서는 Braze가 사용자 메시지를 처리하는 방법에 대해 설명합니다."
page_type: reference
channel:
  - WhatsApp
page_order: 5.1
alias: /whatsapp_quick_replies/

---

# 사용자 메시지

> WhatsApp은 양방향 통신 채널입니다. 브랜드는 사용자에게 메시지를 보낼 수 있을 뿐만 아니라 템플릿 캠페인과 캔버스를 사용하여 대화에 참여할 수 있습니다. WhatsApp 빠른 답장, 목록 메시지 및 트리거 단어를 포함하여 이를 수행하는 다양한 방법이 있습니다. 빠른 답장 및 목록 메시지의 행동 유도(CTA)는 WhatsApp 메시징에서 사용자 참여를 유도하는 훌륭한 방법입니다.

## 행동 기반 트리거 

캠페인과 캔버스 모두 인바운드 WhatsApp 메시지(사용자가 WhatsApp에 메시지를 보낸 경우)에서 시작하고 분기하며 중간 여정 변경을 할 수 있습니다. 예를 들어 트리거 단어가 있습니다. 

트리거 단어가 사용자가 기대하는 것과 일치하는지 확인하십시오.

**알아야 할 사항:**
- 트리거 단어의 각 문자는 구성할 때 대문자로 작성해야 합니다. Braze는 사용자가 보낸 인바운드 트리거 단어가 대문자로 작성될 필요는 없습니다. 예를 들어, "jOin2023" 메시지는 여전히 캔버스나 캠페인을 트리거합니다.
- 입장 일정의 행동 기반 트리거에 트리거 단어가 지정되지 않은 경우, 캠페인이나 캔버스는 모든 인바운드 WhatsApp 메시지에 대해 실행됩니다. 여기에는 활성 캠페인과 캔버스에서 일치하는 구문이 포함된 메시지가 포함되며, 이 경우 사용자는 두 개의 WhatsApp 메시지를 받게 됩니다.

{% tabs %}
{% tab Campaign %}

\![행동 기반 캠페인 일정 옵션.]({% image_buster /assets/img/whatsapp/whatsapp27.png %})

{% endtab %}
{% tab Canvas %}

\![액션 기반 캔버스 일정 옵션.]({% image_buster /assets/img/whatsapp/whatsapp25.png %})

{% endtab %}
{% endtabs %}

## 인식되지 않은 응답

인터랙티브 캔버스에서 인식되지 않은 응답 옵션을 포함하는 것을 권장합니다. 이것은 사용자가 사용 가능한 프롬프트를 이해하도록 안내하고 채널에 대한 기대치를 설정합니다. 기대 관리가 특히 유용할 수 있는 경우는 라이브 에이전트 채팅이 있는 WhatsApp 채널이 있는 경우입니다. 
- 액션 단계에서 사용자 정의 필터 구문에 대한 액션 그룹을 생성한 후, "WhatsApp 메시지 전송"에 대한 추가 액션 그룹을 추가하되 **메시지 본문이 어디인지 확인하지 마십시오.** 이것은 모든 인식되지 않은 사용자 응답을 포착하며, "else" 절과 유사합니다. 
- WhatsApp 메시지로 후속 조치를 취하여 이 채널이 관리되지 않음을 사용자에게 알리고 필요할 경우 지원 채널로 안내하는 것을 권장합니다. 

## 빠른 응답 

\![전화 화면에 클릭한 버튼의 텍스트에 응답할 호출 버튼이 표시됩니다.]({% image_buster /assets/img/whatsapp/whatsapp11.png %}){: style="float:right;max-width:25%;margin-left:15px;border: 0;"}

빠른 응답은 대화 내에서 클릭 가능한 버튼 옵션으로 나타나지만 사용자가 텍스트로 응답한 것처럼 작동합니다. Braze는 이러한 응답을 수신 메시지로 처리하고 클릭한 버튼에 따라 설정된 응답을 다시 보낼 수 있습니다. 사용자로부터 응답을 생성하고 필터링할 때 "수신 WhatsApp 메시지 액션" 단계를 사용하십시오.

\![텍스트와 세 개의 호출 버튼이 있는 WhatsApp 메시지.]({% image_buster /assets/img/whatsapp/whatsapp13.png %}){: style="max-width:50%;"}

### 캔버스에서 빠른 응답 경험을 구성하십시오.

#### 1단계: CTA 구축하기

먼저, 메시지 템플릿 내의 [WhatsApp 메시지 템플릿 관리자](https://business.facebook.com/wa/manage/message-templates/)에서 빠른 응답 CTA를 구축하십시오. 

\![CTA 버튼을 생성하는 방법을 보여주는 WhatsApp 메시지 템플릿 관리자 UI, 버튼 유형(사용자 정의) 및 버튼 텍스트를 제공합니다.]({% image_buster /assets/img/whatsapp/whatsapp12.png %}){: style="max-width:80%;"}

템플릿이 제출되고 WhatsApp에 의해 승인되면 Braze 내에서 캔버스를 구축하는 데 사용할 수 있습니다. 

{% alert tip %}
메시지 템플릿에 대한 승인을 받기 전에 캔버스를 구축할 수 있습니다.
{% endalert %}

#### 2단계: 캔버스를 구축하세요

다음으로, 생성한 템플릿을 포함하는 메시지 단계로 캔버스를 구축하세요. 

\![빠른 응답 템플릿이 채워진 WhatsApp 단계 메시지 작성기.]({% image_buster /assets/img/whatsapp/whatsapp14.png %})

메시지 단계 다음에 오는 작업 단계를 만드세요. 이 작업 단계에서 빠른 응답 옵션당 하나의 그룹을 만드세요.

\![평가 작업이 "WhatsApp 수신 메시지 전송"으로 설정된 캔버스.]({% image_buster /assets/img/whatsapp/whatsapp15.png %})

각 빠른 응답 옵션 그룹에 대해 일치하는 버튼으로 정확한 텍스트를 지정하세요. 키워드는 대문자로 작성해야 합니다. 

\![특정 메시지 본문이 수신될 때 "WhatsApp 수신 메시지 전송" 작업이 설정된 캔버스 단계.]({% image_buster /assets/img/whatsapp/whatsapp16.png %})

사용자가 빠른 응답 대신 텍스트로 메시지에 응답할 경우 기본 응답을 원하시면, 일치하는 메시지 본문이 없는 추가 그룹을 만드세요.

이 시점부터는 계속해서 캔버스를 구축하세요.

### 응답

각 응답에 대한 회신 메시지가 필요할 것입니다. 빠른 응답의 범위를 벗어난 응답에 대한 모든 옵션을 갖는 것을 권장합니다(예: 미리 정해진 프롬프트 대신 일반 메시지로 응답하는 고객을 위한). 예를 들어, "죄송합니다, 귀하의 응답을 인식하지 못했습니다." 지원 문제의 경우, <support channel>에 메시지를 보내주세요."

\![각 클릭 유도 버튼에 대한 응답을 보여주는 캔버스.]({% image_buster /assets/img/whatsapp/whatsapp18.png %})

Braze Canvas가 제공하는 후속 작업(응답 메시지, 사용자 프로필 업데이트 또는 Braze-to-Braze 웹후크 등)을 사용할 수 있습니다. 

## 메시지 목록

메시지 목록은 클릭 가능한 옵션 목록과 함께 본문 메시지로 표시됩니다. 각 목록은 여러 섹션을 가질 수 있으며, 각 목록은 최대 10개의 행을 가질 수 있습니다.

\![다양한 패션 스타일에 대한 행이 있는 WhatsApp 목록 메시지의 예.]({% image_buster /assets/img/whatsapp/list_message_example.png %}){: style="max-width:40%;"}

### Canvas에서 목록 메시지 경험 구성하기

#### 1단계: 기존의 작업 기반 Canvas를 생성하거나 편집하기

WhatsApp 목록 메시지는 사용자 메시지에 대한 응답으로 있어야 하므로 작업 기반 Canvas에만 추가할 수 있습니다.

#### 2단계: WhatsApp 메시지 단계 만들기

WhatsApp [메시지 단계]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/)를 추가한 다음, **목록 메시지**의 응답 메시지 레이아웃을 선택합니다.

\![생성할 수 있는 다양한 유형의 WhatsApp 응답 메시지의 선택 가능한 컬렉션, "목록 메시지" 포함.]({% image_buster /assets/img/whatsapp/list_message_option.png %}){: style="max-width:70%;"}

사용자가 목록을 표시하기 위해 선택할 **목록 버튼** 이름을 추가합니다. 그런 다음 **목록 내용**의 필드를 사용하여 목록을 만듭니다:

- **섹션:** 목록 항목을 그룹화하고 정리하기 위해 최대 10개의 섹션을 추가합니다. 예를 들어, 의류 소매업체는 섹션을 사용하여 계절 스타일(봄, 여름, 가을, 겨울) 또는 의류 항목(상의, 하의, 신발)으로 정리할 수 있습니다.
- **행:** 모든 섹션에 걸쳐 최대 10개의 행 또는 목록 항목을 추가합니다.
- **행 설명(선택 사항):** 모든 행(목록 항목)에 선택적 설명을 추가합니다.

\![두 개의 섹션과 여러 행 및 행 설명으로 채워진 "목록 내용" 섹션.]({% image_buster /assets/img/whatsapp/list_content.png %}){: style="max-width:60%;"}

섹션과 행의 순서를 이름 옆에 있는 아이콘을 선택하고 드래그하여 변경합니다.

\![새 위치로 목록 섹션 드래그하기.]({% image_buster /assets/img/whatsapp/drag_list_order.png %}){: style="max-width:60%;"}

캔버스 작곡기로 돌아가서 각 목록 응답에 대한 그룹이 있는 메시지 단계 뒤에 [작업 경로]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/)를 추가합니다. 각 그룹에서:

1. **수신된 WhatsApp 구독 그룹**에 대한 트리거를 추가하고 해당 WhatsApp 구독 그룹을 선택합니다.
2. **메시지 본문이 있는 위치** 체크박스를 확인합니다.
3. 하나의 행(또는 목록 항목)에 대한 내용을 지정합니다.

\![다양한 의류 스타일을 위한 그룹이 있는 작업 경로의 작곡기.]({% image_buster /assets/img/whatsapp/action_path_list_message.png %})

캔버스를 계속 구축합니다.

### 긴 설명을 위한 작업 경로 만들기

행 설명이 있는 경우 **정규 표현식 일치**를 사용하여 행을 지정해야 합니다. 예를 들어, "당신의 좋아하는 앵클 부츠 위에 맞는 새로운 스타일"이라는 설명이 있는 행을 지정하려면 "앵클 부츠"와 함께 [정규 표현식]({{site.baseurl}}/user_guide/engagement_tools/segments/regex/)를 사용할 수 있습니다.

\!["정규 표현식 일치" 필터를 사용하여 "앵클 부츠"가 포함된 응답 메시지를 캡처하는 WhatsApp 트리거.]({% image_buster /assets/img/whatsapp/regex_list_message.png %})

## 응답 메시지에 대한 고려 사항

응답 메시지는 사용자의 메시지를 수신한 후 24시간 이내에 전송되어야 합니다. 성공적인 경험을 구축하기 위해 Braze는 메시지 논리를 확인하여 응답 메시지를 차단 해제하는 상류 수신 사용자 메시지가 있는지 확인합니다. 

다음 이벤트가 응답 메시지의 차단을 해제합니다: 

- 수신 메시지 
  - [작업 경로]({{site.baseurl}}/action_paths/) 또는 [작업 기반 진입]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/)과 트리거 **WhatsApp 수신 메시지 전송**.

\!["WhatsApp 수신 메시지 전송" 트리거가 있는 작업 기반 진입 단계.]({% image_buster /assets/img/whatsapp/whatsapp_inbound_message_trigger.png %})

- [API 트리거된 항목]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/)
- 수신된 제품 메시지 
  - [`ecommerce.cart_updated`]({{site.baseurl}}/user_guide/data/custom_data/recommended_events/ecommerce_events/?tab=ecommerce.cart_updated#types-of-ecommerce-recommended-events) 이벤트

\![사용자 정의 이벤트 `ecommerce.cart_updated`.]({% image_buster /assets/img/whatsapp/ecommerce_cart_updated.png %}의 트리거가 있는 작업 경로

