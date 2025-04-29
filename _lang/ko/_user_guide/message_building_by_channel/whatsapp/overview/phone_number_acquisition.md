---
nav_title: 전화번호 획득
article_title: 전화번호 획득
page_order: 3
description: "이 참조 문서에서는 Twilio 및 Infobip에서 전화번호를 얻는 방법을 다룹니다."
page_type: reference
channel:
  - WhatsApp
---

# 전화번호 획득

> WhatsApp 메시징 채널을 사용하려면 [Cloud API](https://developers.facebook.com/docs/whatsapp/cloud-api/phone-numbers) 또는 [On-Premises API](https://developers.facebook.com/docs/whatsapp/on-premises/phone-numbers)에 대한 WhatsApp의 요구 사항을 충족하는 전화번호가 필요합니다.

전화번호는 직접 획득해야 하며, Braze는 번호를 제공하지 않습니다. 귀하의 비즈니스 전화 제공업체를 통해 SIM 카드가 있는 물리적 전화를 구입하거나 당사의 파트너 중 한 명을 사용할 수 있습니다: Twilio 또는 Infoblip. **Twilio 또는 Infobip 계정이 있어야 합니다. 이 작업은 Braze를 통해 수행할 수 없습니다.**

## WhatsApp API 요구 사항

귀하의 전화번호는 다음 WhatsApp API 요구 사항을 충족해야 합니다:

- 비즈니스 소유 
- 국가 코드 및 지역 코드(유선 전화 및 휴대폰 번호와 같은)를 보유하십시오.
- 음성 통화 또는 SMS를 받을 수 있습니다
- 계정 설정 중에 접근 가능 (인증 코드를 받기 위해)
- 짧은 코드가 아닙니다
- 이전에 WhatsApp 비즈니스 플랫폼에서 사용되지 않음
- 개인 WhatsApp 계정에 연결되지 않음

## Twilio 전화번호 획득

### 1단계: Twilio 콘솔 또는 API에서 전화번호를 구매하세요

1. Twilio 콘솔에서 **개발** > **전화번호** > **관리** > **번호 구매**로 이동합니다. 이 옵션이 보이지 않으면 **제품 탐색**을 선택하고 **슈퍼 네트워크**로 스크롤한 다음 **전화번호** > **번호 구매**을 선택하세요. <br><br>![Twilio 콘솔에서 "개발" 탭을 열고 "번호 구매" 옵션을 선택합니다.][1]{: style="max-width:20%;"}<br><br>

2. 원하는 지역 코드 또는 지역(있는 경우)을 입력하세요. 숫자를 찾은 다음 **구매**를 선택하세요. <br><br> ![목록에 있는 전화번호를 구매하는 버튼입니다.][2]<br><br>

3. 전화번호를 구입한 후 **Active Numbers**로 이동하여 방금 구입한 전화번호를 선택하십시오. <br><br>!["활성 번호"는 구매한 전화번호를 표시합니다.][3]{: style="max-width:70%;"}<br><br>

### 2단계: 전화번호 구성

Twilio의 지침에 따라 [음성 메일 전사를 사용하여 이메일로 인증 코드를 받을 수 있도록 Twilio 전화번호를 설정하세요](https://www.twilio.com/docs/whatsapp/self-sign-up#setting-up-your-twilio-phone-number-to-receive-the-verification-code-via-email-using-voicemail-transcription). **다른 단계의 지침을 따르지 마세요. 그렇게 하면 Twilio가 아닌 Braze에 전화번호가 연결됩니다.**

{% alert warning %}
**Twilio의 지침만 따라 인증 코드를 받으세요.**

Twilio의 지침에 따라 다음 단계를 따르면 전화번호를 Twilio에 연결할 수 있습니다. 즉, 마이그레이션을 하거나 다른 번호를 구매하지 않으면 해당 번호를 Braze에 연결할 수 없습니다.
{% endalert %}

### 3단계: 내장된 가입 워크플로를 완료하세요

1. Twilio가 구성된 후 Braze 대시보드 > **Technology Partners** > **WhatsApp**로 이동하여 **통합 시작** 또는 **WhatsApp 비즈니스 계정 추가** 중 표시되는 항목을 선택하여 [내장된 가입 워크플로우]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/embedded_signup/)를 트리거합니다.<br><br>**WhatsApp에 전화번호 추가** 단계에서 전화번호를 확인하는 방법으로 **전화 통화**를 선택하세요. <br><br>![텍스트 메시지 또는 전화 통화를 통해 전화번호를 확인할 수 있는 옵션이 있는 섹션입니다.][4]{: style="max-width:50%;"}<br><br>

2. 인증 코드가 이메일 받은편지함으로 전송될 때까지 몇 분 기다린 후, 인증 코드를 입력하고 설정을 완료하세요.

## Infobip 전화번호 획득 

1. Infobip 콘솔에서 **채널 및 번호**로 이동하여 **번호**를 선택합니다.<br><br>![Infoblip "채널 및 번호" 섹션에 "번호"가 아래에 나열되어 있습니다.][5]{: style="max-width:30%;"}<br><br>

2. **구매 번호** > 메시지를 보내고 싶은 국가를 선택 > **SMS**.<br><br>![번호 구매를 위한 버튼.][6]<br><br>

3. 선택한 국가에 따라 추가 등록 절차(미국 전화번호의 경우 10 DLC 또는 무료 전화 옵션 선택 등)를 완료해야 할 수 있습니다. 사용 가능한 옵션을 선택하십시오.<br><br>![번호 유형을 선택하라는 페이지입니다: 10 DLC 또는 수신자 부담 번호 중 하나를 선택하세요.][7]{: style="max-width:70%;"}<br><br>

4. 사용 가능한 제안을 선택한 다음 나머지 단계를 진행하고 요청이 처리될 때까지 기다리세요. 상태를 확인하려면 **숫자** > **내 요청**으로 이동하십시오. <br><br>![요금 및 보장을 포함한 정보가 포함된 제안입니다.][8]{: style="max-width:70%;"}<br><br>

5. 선택한 국가에 따라 Infobip 팀이 등록 세부 정보(미국의 경우 10DLC 등)를 위해 연락할 때까지 기다리세요.<br><br>

6. Infobip에서 전화번호가 준비되면 Braze 대시보드 > **기술 파트너** > **WhatsApp**로 이동하여 **통합 시작** 또는 **WhatsApp 비즈니스 계정 추가** 중 표시되는 항목을 선택하여 [내장된 가입 워크플로우]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/embedded_signup/)를 트리거합니다.<br><br> **WhatsApp에 전화번호 추가** 단계에서 전화번호를 확인하는 방법으로 **문자 메시지**를 선택하세요.<br><br>![텍스트 메시지 또는 전화 통화를 통해 전화번호를 확인할 수 있는 옵션이 있는 섹션입니다.][9]<br><br>

7. Infobip의 [로그 분석](https://www.infobip.com/docs/analyze/analyze-logs)을(를) 고객 포털에서 확인하여 인증 코드를 확인하세요. 인증 코드는 몇 분 정도 소요될 수 있습니다. 그런 다음 인증 코드를 입력하고 설정을 완료하세요.




[1]: {% image_buster /assets/img/whatsapp/develop_buy_number.png %}
[2]: {% image_buster /assets/img/whatsapp/buy.png %}
[3]: {% image_buster /assets/img/whatsapp/active_numbers.png %}
[4]: {% image_buster /assets/img/whatsapp/verify.png %}
[5]: {% image_buster /assets/img/whatsapp/infoblip_numbers.png %}
[6]: {% image_buster /assets/img/whatsapp/infoblip_buy.png %}
[7]: {% image_buster /assets/img/whatsapp/infoblip_10dlc.png %}
[8]: {% image_buster /assets/img/whatsapp/infoblip_offer.png %}
[9]: {% image_buster /assets/img/whatsapp/infoblip_verify.png %}