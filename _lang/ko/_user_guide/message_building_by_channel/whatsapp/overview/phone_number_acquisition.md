---
nav_title: 전화번호 획득
article_title: 전화번호 획득
page_order: 4
description: "이 참조 문서에서는 Twilio 및 Infobip에서 전화번호를 획득하는 방법을 다룹니다."
page_type: reference
channel:
  - WhatsApp
---

# 전화번호 획득

> WhatsApp 메시징 채널을 사용하려면 [Cloud API](https://developers.facebook.com/docs/whatsapp/cloud-api/phone-numbers) 또는 [On-Premises API](https://developers.facebook.com/docs/whatsapp/on-premises/phone-numbers)에 대한 WhatsApp의 요구 사항을 충족하는 전화번호가 필요합니다.

전화번호는 직접 획득해야 하며, Braze에서 번호를 제공하지 않습니다. 비즈니스 전화 제공업체를 통해 SIM 카드가 있는 물리적 전화를 구입하거나 파트너인 Twilio 또는 Infobip을 사용할 수 있습니다. **Braze를 통해서는 이 작업을 수행할 수 없으므로 Twilio 또는 Infobip 계정을 직접 보유하고 있어야 합니다.**

## WhatsApp API 요구 사항

전화번호는 다음 WhatsApp API 요구 사항을 충족해야 합니다:

- 비즈니스가 소유한 번호일 것
- 국가 코드 및 지역 코드가 있을 것(유선 전화 및 휴대폰 번호 등)
- 음성 통화 또는 SMS 수신이 가능할 것
- 계정 설정 중 접근 가능할 것(인증 코드 수신을 위해)
- 짧은 코드가 아닐 것
- 이전에 WhatsApp 비즈니스 플랫폼에서 사용된 적이 없을 것
- 개인 WhatsApp 계정에 연결되어 있지 않을 것

## Twilio 전화번호 획득

### 1단계: Twilio 콘솔 또는 API에서 전화번호 구매

1. Twilio 콘솔에서 **Develop** > **Phone Numbers** > **Manage** > **Buy a number**로 이동합니다. 이 옵션이 보이지 않으면 **Explore Products**를 선택하고 **Super Networks**로 스크롤한 다음 **Phone Number** > **Buy a number**를 선택하세요. <br><br>![Twilio 콘솔에서 "Develop" 탭을 열고 "Buy a number" 옵션을 선택합니다.]({% image_buster /assets/img/whatsapp/develop_buy_number.png %}){: style="max-width:20%;"}<br><br>

2. 원하는 지역 코드 또는 지역(있는 경우)을 입력하세요. 번호를 찾은 다음 **Buy**를 선택하세요. <br><br> ![목록에 있는 전화번호를 구매하는 버튼입니다.]({% image_buster /assets/img/whatsapp/buy.png %})<br><br>

3. 전화번호를 구입한 후 **Active Numbers**로 이동하여 방금 구입한 전화번호를 선택하세요. <br><br>!["Active Numbers"에서 구매한 전화번호를 표시합니다.]({% image_buster /assets/img/whatsapp/active_numbers.png %}){: style="max-width:70%;"}<br><br>

### 2단계: 전화번호 구성

Twilio의 지침에 따라 [Twilio Voice](https://www.twilio.com/docs/whatsapp/self-sign-up#add-your-whatsapp-phone-number)**만** 사용하여 이메일을 통해 인증 코드를 받을 수 있도록 Twilio 전화번호를 설정하세요. **다른 단계의 지침은 따르지 마세요.**

{% alert warning %}
Twilio의 지침은 인증 코드를 받기 위한 용도로만 따르세요.
다음 단계까지 따르면 전화번호가 Twilio에 연결되며, 마이그레이션을 하거나 다른 번호를 구매하지 않는 한 해당 번호를 Braze에 연결할 수 없습니다.
{% endalert %}

1. Twilio 콘솔에서 [Active Numbers 페이지](https://www.twilio.com/console/phone-numbers/incoming)로 이동하여 구매한 전화번호를 선택합니다.
2. **Voice Configuration** 섹션으로 이동하여 **Configure with** 드롭다운에서 **Webhook, TwiML Bin, Function, Studio Flow, Proxy Service**를 선택합니다.
3. **A call comes in** 행에서 **Webhook**을 선택하고 URL을 `https://twimlets.com/voicemail?Email=YOUR_EMAIL_ADDRESS`로 설정합니다. `YOUR_EMAIL_ADDRESS`를 본인의 이메일 주소로 바꾸세요.
4. Twilio 콘솔에서 **2. Link WhatsApp Business Account with your number** > **2. Copy the phone number you register**로 이동하여 전화번호 옆의 **Copy**를 선택합니다.
5. **Self Sign-up** 창의 **Add your WhatsApp phone number** 페이지에서 **Add a new phone number**를 선택하고 전화번호를 붙여넣습니다.
6. 인증 방법으로 **Phone call**을 선택한 다음 **Next**를 선택합니다.
7. 10분 이내에 이메일로 인증 코드를 받게 됩니다.

### 3단계: 임베디드 가입 워크플로 완료

1. Twilio 구성이 완료되면 Braze 대시보드 > **기술 파트너** > **WhatsApp**로 이동하여 **Begin integration** 또는 **Add WhatsApp Business Account** 중 표시되는 항목을 선택하여 [임베디드 가입 워크플로]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/embedded_signup/)를 트리거합니다.<br><br>**Add a phone number for WhatsApp** 단계에서 전화번호 인증 방법으로 **Phone call**을 선택하세요. <br><br>![문자 메시지 또는 전화 통화를 통해 전화번호를 인증할 수 있는 옵션이 있는 섹션입니다.]({% image_buster /assets/img/whatsapp/verify.png %}){: style="max-width:50%;"}<br><br>

2. 인증 코드가 이메일 받은편지함으로 전송될 때까지 몇 분 기다린 후, 인증 코드를 입력하고 설정을 완료하세요.

## Infobip 전화번호 획득

1. Infobip 콘솔에서 **Channels and Numbers**로 이동하여 **Numbers**를 선택합니다.<br><br>![Infobip "Channels and Numbers" 섹션에 "Numbers"가 아래에 나열되어 있습니다.]({% image_buster /assets/img/whatsapp/infoblip_numbers.png %}){: style="max-width:30%;"}<br><br>

2. **Buy Number** > 메시지를 보내려는 국가 선택 > **SMS**를 선택합니다.<br><br>![번호 구매 버튼입니다.]({% image_buster /assets/img/whatsapp/infoblip_buy.png %})<br><br>

3. 선택한 국가에 따라 추가 등록 절차(미국 전화번호의 경우 10DLC 또는 수신자 부담 번호 옵션 선택 등)를 완료해야 할 수 있습니다. 사용 가능한 옵션을 선택하세요.<br><br>![번호 유형을 선택하라는 페이지입니다: 10DLC 또는 수신자 부담 번호 중 하나를 선택하세요.]({% image_buster /assets/img/whatsapp/infoblip_10dlc.png %}){: style="max-width:70%;"}<br><br>

4. 사용 가능한 제안을 선택한 다음 나머지 단계를 진행하고 요청이 처리될 때까지 기다리세요. 상태를 확인하려면 **Numbers** > **My Request**로 이동하세요. <br><br>![요금 및 커버리지 정보가 포함된 제안입니다.]({% image_buster /assets/img/whatsapp/infoblip_offer.png %}){: style="max-width:70%;"}<br><br>

5. 선택한 국가에 따라 Infobip 팀이 등록 세부 정보(예: 미국의 10DLC)에 대해 연락할 때까지 기다리세요.<br><br>

6. Infobip에서 전화번호가 준비되면 Braze 대시보드 > **기술 파트너** > **WhatsApp**로 이동하여 **Begin integration** 또는 **Add WhatsApp Business Account** 중 표시되는 항목을 선택하여 [임베디드 가입 워크플로]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/embedded_signup/)를 트리거합니다.<br><br> **Add a phone number for WhatsApp** 단계에서 전화번호 인증 방법으로 **Text message**를 선택하세요.<br><br>![문자 메시지 또는 전화 통화를 통해 전화번호를 인증할 수 있는 옵션이 있는 섹션입니다.]({% image_buster /assets/img/whatsapp/infoblip_verify.png %})<br><br>

7. Infobip 고객 포털에서 [로그 분석](https://www.infobip.com/docs/analyze/analyze-logs)을 확인하여 인증 코드를 찾으세요. 표시되기까지 몇 분 정도 소요될 수 있습니다. 인증 코드를 입력하고 설정을 완료하세요.