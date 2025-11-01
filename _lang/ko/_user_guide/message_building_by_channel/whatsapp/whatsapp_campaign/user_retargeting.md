---
nav_title: 사용자 리타겟팅
article_title: 사용자 리타겟팅
page_order: 4
description: "이 참고 문서에서는 사용자가 WhatsApp 상호작용을 통해 메시지를 리타겟팅하는 방법에 대해 설명합니다."
page_type: reference
channel:
  - WhatsApp
---

# 사용자 리타겟팅 

> 사용자의 구독 상태를 변경하는 것 외에도 Braze는 메시지를 필터링하고 트리거하기 위해 고객 프로필과의 상호 작용도 기록합니다.<br><br>이러한 필터 및 트리거를 사용하면 특정 WhatsApp 캠페인 또는 캔버스 단계에서 WhatsApp 메시지를 수신했거나 수신한 사용자를 필터링할 수 있습니다.

## 리타겟팅 옵션

{% alert note %}
사용자 리타겟팅으로 오디언스를 구축할 때 선호도에 따라 특정 사용자를 포함하거나 제외할 수 있으며, CCPA에 따른 '판매 또는 공유 금지' 권한과 같은 개인정보 보호법을 준수하기 위해 특정 사용자를 포함하거나 제외할 수 있습니다. 마케터는 캔버스 및/또는 캠페인 참가 기준 내에서 사용자 자격을 위한 관련 필터를 구현해야 합니다.
{% endalert %}

### WhatsApp으로 사용자 필터링

사용자는 마지막으로 WhatsApp을 받은 시간 또는 특정 WhatsApp 캠페인에서 WhatsApp을 받은 적이 있는지를 기준으로 필터링할 수 있습니다. 필터는 캠페인 빌더의 타겟팅 사용자 단계에서 설정할 수 있습니다.

**마지막으로 받은 WhatsApp으로 필터링하기**<br>
\![2025년 4월 22일에 마지막으로 받은 WhatsApp 메시지 필터링.]({% image_buster /assets/img/whatsapp/whatsapp23.png %}){: style="max-width:75%"}

**WhatsApp 캠페인에서 받은 메시지를 기준으로 필터링하기**<br>
특정 WhatsApp 캠페인에서 메시지를 받은 사용자를 필터링합니다. 이 필터를 사용하면 WhatsApp 캠페인에서 메시지를 받지 않은 사람들을 필터링할 수도 있습니다.<br>
!!\![WhatsApp 캠페인 수신을 위한 필터.]({% image_buster /assets/img/whatsapp/whatsapp22.png %}){: style="max-width:75%"}

### 참여도별 필터링
WhatsApp 캠페인 또는 캔버스 단계를 읽었거나 읽지 않은 사용자를 리타겟팅하세요. 

**특정 WhatsApp 캠페인을 열거나 읽은 사용자를 리타겟팅하세요.**
1. **클릭/열기 캠페인** 필터를 사용하여 세그먼트를 만듭니다.
2. **WhatsApp 메시지 읽기를** 선택합니다.
3. 원하는 캠페인을 선택합니다.<br>

!!! WhatsApp 메시지를 읽었음을 필터링합니다.]({% image_buster /assets/img/whatsapp/whatsapp21.png %}){: style="max-width:75%"}

**특정 캔버스 단계를 열거나 읽은 사용자를 리타겟팅하세요.**
1. **클릭/열기 단계** 필터를 사용하여 세그먼트를 만듭니다.
2. **WhatsApp 메시지 읽기를** 선택합니다.
3. 원하는 캔버스 및 캔버스 단계를 선택합니다.<br>

!!\![WhatsApp 단계 읽기 필터.]({% image_buster /assets/img/whatsapp/whatsapp20.png %}){: style="max-width:75%"}

**캠페인 또는 캔버스 속성별로 필터링하기**<br>
특정 WhatsApp 캠페인이나 캔버스 구성요소 또는 태그를 열거나 읽은 사용자를 필터링합니다.

\![특정 WhatsApp 메시지를 열기 위한 필터.]({% image_buster /assets/img/whatsapp/whatsapp19.png %}){: style="max-width:75%"}

