---
nav_title: "WhatsApp로 클릭하는 광고"
article_title: WhatsApp로 클릭하는 광고
page_order: 1
description: "이 참조 기사는 WhatsApp로 클릭하는 광고를 설정하고 사용하는 단계별 가이드를 제공합니다."
page_type: reference
alias: /whatsapp_use_cases/
channel:
  - WhatsApp
---

# WhatsApp로 클릭하는 광고

> 이 페이지는 WhatsApp로 클릭하는 광고를 설정하고 사용하는 단계별 가이드를 제공하여 귀하와 귀하의 팀이 WhatsApp 프로그램을 향상시킬 수 있도록 합니다.

WhatsApp로 클릭하는 광고는 Facebook, Instagram 또는 기타 플랫폼의 Meta 광고에서 신규 및 기존 고객을 유치하는 효율적인 방법입니다. 이 광고를 사용하여 제품과 서비스를 홍보하고 사용자가 WhatsApp 존재를 인식하도록 합니다.

\![Calorie Rocket의 무료 배송을 광고하는 Facebook 광고와 사용자가 광고 버튼을 선택할 때 발생하는 WhatsApp 대화.]({% image_buster /assets/img/whatsapp/ads_that_click_whatsapp.png %}){: style="max-width:70%;"}

## WhatsApp로 클릭하는 광고 설정하기

1. Meta Ads Manager에서 Facebook, Instagram 또는 기타 플랫폼에 광고를 만들려면 단계별 가이드를 따르세요 [WhatsApp로 클릭하는 광고 만들기](https://business.whatsapp.com/products/create-ads-that-click-to-whatsapp). **자동 응답을 설정하지 마세요**; 대신 Braze에서 응답을 설정합니다.

\![참여 광고를 만들기 위한 작곡기가 있는 광고 관리자.]({% image_buster /assets/img/whatsapp/meta_ads_composer.png %})

사용자가 WhatsApp 비즈니스 계정으로 보낼 사전 채워진 메시지를 설정할 때 특정 단어 또는 구문을 포함하여 특정 광고에 대한 응답을 트리거하는 데 사용할 것입니다. 이 예에서 음식 배달 앱은 광고에서 홍보되는 "무료 배송"을 사용하고 있습니다. 

\!["무료 배송을 원합니다"라는 사전 채워진 메시지가 있는 광고 관리자 템플릿 작곡기.]({% image_buster /assets/img/whatsapp/pre_filled_message.png %})

{% alert tip %}
광고 설명에서 광고를 클릭하면 브랜드와 대화가 시작된다는 것을 분명히 하여 "WhatsApp에서 지금 채팅하기"와 같은 문구를 사용하세요.
{% endalert %}

{: start="2"}
2\. Braze에서 작업 기반 옵션이 **WhatsApp 수신 메시지 전송**이고 메시지 본문이 “YOUR_TRIGGER_WORD”.인 작업 기반 캔버스를 설정합니다. 이 예에서 음식 배달 앱은 "무료 배송"을 사용하고 있습니다.

\!["WhatsApp 수신 메시지 전송"의 트리거 이벤트와 "무료 배송"의 정규 표현식과 일치하는 메시지 본문이 있는 작업 기반 Braze 캔버스의 진입 일정.]({% image_buster /assets/img/whatsapp/action_based_free_delivery.png %})

{: start="3"}
3\. 고객이 캔버스에 들어간 직후(예: 지연 없이) 즉시 전송되는 응답 메시지를 캔버스에 설정하세요. 광고를 클릭하는 것이 기술적으로 옵트인으로 간주되지만, 사용자가 WhatsApp에서 향후 마케팅 메시지를 수신하고 싶어하는지 묻는 응답 메시지를 설정하는 것이 좋습니다. 

{% alert tip %}
사용자가 옵트인 여부를 빠르게 표시할 수 있도록 "예" 또는 "아니요"와 같은 빠른 응답으로 응답 메시지를 설정하세요.
{% endalert %}

광고에서 약속한 할인 코드, 제안 또는 기타 정보를 제공하는 것을 잊지 마세요!

\!["예" 및 "아니요" 버튼 응답이 있는 WhatsApp 메시지 작성기.]({% image_buster /assets/img/whatsapp/quick_replies.png %})

\!["구독 그룹에 인바운드 WhatsApp 전송"의 트리거 이벤트와 "YES"의 트리거 단어가 있는 "옵트인" 그룹이 있는 캔버스 단계.]({% image_buster /assets/img/whatsapp/opting_in_step.png %})

{: start="4"}
4\. 다음 업데이트 방법 중 하나로 사용자 프로필의 구독 상태를 업데이트하여 옵트인 사용자로 만드세요:
    \- REST API를 통해 구독 상태를 업데이트하는 Braze-to-Braze 웹후크를 만드세요.  
    \- 고급 JSON 편집기를 사용하여 [사용자의 구독 상태를 WhatsApp 캔버스로 업데이트]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_subscription/#whatsapp-opt-in-and-opt-out-process)하는 템플릿으로 사용자 프로필을 업데이트하세요.

\![고급 JSON 편집기를 사용하여 사용자 프로필을 업데이트하는 사용자 업데이트 캔버스 단계.]({% image_buster /assets/img/whatsapp/user_update_step_json.png %})

\![WhatsApp으로 Ads That Click을 전송하는 워크플로우를 보여주는 캔버스, 세 가지 작업 경로 포함: 옵트인, 옵트아웃 및 기타 모든 사용자.]({% image_buster /assets/img/whatsapp/ads_that_click_canvas.png %})

## 고려사항

WhatsApp으로 클릭하는 광고에서 시작된 대화는 다음 조건이 충족되면 무료입니다:

- 사용자가 [무료 진입점](https://developers.facebook.com/docs/whatsapp/pricing#free-entry-point-conversations)을 통해 메시지를 보내면, 광고가 WhatsApp으로 클릭되는 경우 24시간 [고객 서비스 창](https://developers.facebook.com/docs/whatsapp/cloud-api/guides/send-messages#customer-service-windows)이 열리며, 이 기간 동안 해당 사용자에게 모든 유형의 메시지를 보낼 수 있습니다.
- 고객 서비스 창(24시간 이내) 내에 응답하면 72시간 동안 무료 진입점이 열리며, 72시간 창 내의 모든 메시지는 무료입니다.
- 응답 메시지는 무료입니다.