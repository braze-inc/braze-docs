---
nav_title: 사용자 리타겟팅
article_title: 사용자 리타겟팅
page_order: 3
description: "이 참조 문서는 사용자가 WhatsApp 상호 작용을 통해 메시지를 리타겟하는 방법을 다룹니다."
page_type: reference
channel:
  - WhatsApp
---

# 사용자 리타겟팅 

> 사용자의 구독 상태를 변경하는 것 외에도, Braze는 메시지 필터링 및 트리거를 위해 고객 프로필과의 상호 작용을 기록합니다.<br><br>이 필터 및 트리거를 사용하면 WhatsApp 메시지를 받았거나 특정 WhatsApp 캠페인 또는 캔버스 단계에서 WhatsApp 메시지를 받은 사용자를 필터링할 수 있습니다.

## 리타겟팅 옵션

{% alert note %}
사용자 리타겟팅으로 오디언스를 구축할 때, 특정 사용자를 포함하거나 제외하려면 사용자의 선호도에 따라 결정할 수 있으며, CCPA(캘리포니아 소비자 개인정보 보호법) 하의 '판매 또는 공유 금지' 권리와 같은 개인정보 보호법을 준수해야 합니다. 마케터는 사용자의 적격성에 대한 관련 필터를 캔버스 및/또는 캠페인 진입 기준 내에서 구현해야 합니다.
{% endalert %}

### 사용자를 WhatsApp으로 필터링

사용자는 마지막으로 WhatsApp을 받았을 때 또는 특정 WhatsApp 캠페인에서 WhatsApp을 받았는지 여부에 따라 필터링할 수 있습니다. 필터는 캠페인 빌더의 타겟 사용자 단계에서 설정할 수 있습니다.

**마지막으로 수신한 WhatsApp으로 필터**<br>
![Filter for last receiving a WhatsApp message on April 22, 2025.]({% image_buster /assets/img/whatsapp/whatsapp23.png %}){: style="max-width:75%"}

**받은 메시지로 필터링 WhatsApp 캠페인**<br>
특정 WhatsApp 캠페인에서 메시지를 받은 사용자를 필터링합니다. 이 필터를 사용하면 WhatsApp 캠페인에서 메시지를 받지 않은 사람들을 필터링할 수도 있습니다.<br>
![Filter for receiving a WhatsApp campaign.]({% image_buster /assets/img/whatsapp/whatsapp22.png %}){: style="max-width:75%"}

### 인게이지먼트로 필터
리타겟 사용자가 WhatsApp 캠페인 또는 캔버스 단계를 읽었거나 읽지 않은 경우. 

**리타겟 사용자가 특정 WhatsApp 캠페인을 열거나 읽은 경우**
1. **클릭됨/열림 캠페인** 필터를 사용하여 세그먼트를 만드십시오.
2. **WhatsApp 메시지 읽기**을 선택하십시오.
3. 원하는 캠페인을 선택하세요.<br>

![Filter for having read a WhatsApp message.]({% image_buster /assets/img/whatsapp/whatsapp21.png %}){: style="max-width:75%"}

**리타겟 사용자가 특정 캔버스 단계를 열거나 읽은 경우**
1. **클릭됨/열림 단계** 필터를 사용하여 세그먼트를 만듭니다.
2. **WhatsApp 메시지 읽기**을 선택하십시오.
3. 원하는 캔버스 및 캔버스 단계를 선택하십시오.<br>

![Filter for reading a WhatsApp step.]({% image_buster /assets/img/whatsapp/whatsapp20.png %}){: style="max-width:75%"}

**캠페인 또는 캔버스 기여도로 필터**<br>
사용자가 특정 WhatsApp 캠페인 또는 캔버스 구성 요소 또는 태그를 열거나 읽은 경우 필터링합니다.

![Filter for opening a specific WhatsApp message.]({% image_buster /assets/img/whatsapp/whatsapp19.png %}){: style="max-width:75%"}

