---
nav_title: 전화번호 획득
article_title: 전화번호 획득
page_order: 3
description: "이 참조 문서에서는 Twilio와 Infobip에서 전화번호를 획득하는 방법을 다룹니다."
page_type: reference
channel:
  - WhatsApp
---

# 전화번호 획득

> WhatsApp 메시징 채널을 사용하려면 WhatsApp의 [클라우드 API](https://developers.facebook.com/docs/whatsapp/cloud-api/phone-numbers) 또는 [온프레미스 API](https://developers.facebook.com/docs/whatsapp/on-premises/phone-numbers) 요구 사항을 충족하는 전화번호가 필요합니다.

전화번호는 직접 획득해야 하며, Braze가 번호를 제공하지 않습니다. 비즈니스 전화 제공업체를 통해 SIM 카드가 장착된 실제 전화를 구매하거나 파트너 중 한 곳을 사용할 수 있습니다: Twilio 또는 Infoblip. **자신의 Twilio 또는 Infobip 계정이 있어야 하며, 이는 Braze를 통해 수행할 수 없습니다.**

## WhatsApp API 요구 사항

전화번호는 다음 WhatsApp API 요구 사항을 충족해야 합니다:

- 귀하의 비즈니스 소유 
- 국가 및 지역 코드가 있어야 함(예: 유선 및 휴대전화 번호)
- 음성 통화 또는 SMS를 받을 수 있어야 함
- 계정 설정 중에 접근 가능해야 함(인증 코드를 받기 위해)
- 단축 코드가 아님
- WhatsApp 비즈니스 플랫폼에서 이전에 사용되지 않음
- 개인 WhatsApp 계정에 연결되지 않음

## Twilio 전화번호 획득

### 1단계: Twilio 콘솔 또는 API에서 전화번호를 구매하세요.

1. Twilio 콘솔에서 **개발** > **전화번호** > **관리** > **번호 구매**로 이동합니다. 이 옵션이 보이지 않으면 **제품 탐색**을 선택하고 **슈퍼 네트워크**로 스크롤한 다음 **전화번호** > **번호 구매**를 선택합니다. <br><br>\!["개발" 탭이 열리고 "번호 구매" 옵션이 있는 Twilio 콘솔.]({% image_buster /assets/img/whatsapp/develop_buy_number.png %}){: style="max-width:20%;"}<br><br>

2. 원하는 지역 코드 또는 지역을 입력하세요(있는 경우). 번호를 찾은 후 **구매**를 선택합니다. <br><br> \![나열된 전화번호를 구매하는 버튼.]({% image_buster /assets/img/whatsapp/buy.png %})<br><br>

3. 전화번호를 구매한 후 **활성 번호**로 이동하여 방금 구매한 전화번호를 선택합니다. <br><br>\![구매한 전화번호가 표시된 "활성 번호".]({% image_buster /assets/img/whatsapp/active_numbers.png %}){: style="max-width:70%;"}<br><br>

### 2단계: 전화번호 구성하기

Twilio의 지침에 따라 [Twilio 전화번호를 설정하여 이메일을 통해 인증 코드를 받도록 설정하세요.](https://www.twilio.com/docs/whatsapp/self-sign-up#verify-your-whatsapp-sender) **다른 단계의 지침을 따르지 마세요. 그렇게 하면 전화번호가 Braze가 아닌 Twilio에 연결됩니다.**

{% alert warning %}
**인증 코드를 받기 위해 Twilio의 지침만 따르세요.**

Twilio의 지침에서 다음 단계를 따르면 전화번호가 Twilio에 연결됩니다. 그것은 당신이 마이그레이션을 하거나 다른 번호를 구매하지 않는 한 그 번호를 Braze에 연결할 수 없다는 것을 의미합니다.
{% endalert %}

### 3단계: 임베디드 가입 워크플로우 완료하기

1. Twilio가 구성된 후 Braze 대시보드로 이동하여 > **기술 파트너** > **WhatsApp**를 선택하고 **통합 시작** 또는 **WhatsApp 비즈니스 계정 추가**를 선택하여 [임베디드 가입 워크플로우]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/embedded_signup/)를 트리거합니다.<br><br>**WhatsApp** 단계에서 전화번호를 확인하는 방법으로 **전화 통화**를 선택합니다. <br><br>\![전화번호를 문자 메시지 또는 전화 통화로 확인하는 옵션이 있는 섹션.]({% image_buster /assets/img/whatsapp/verify.png %}){: style="max-width:50%;"}<br><br>

2. 인증 코드가 이메일 수신함으로 전송될 때까지 몇 분 기다린 후, 인증 코드를 입력하고 설정을 완료하세요.

## Infobip 전화번호 획득하기 

1. Infobip 콘솔에서 **채널 및 번호**로 이동하여 **번호**를 선택하세요.<br><br>\!["번호"가 아래에 나열된 Infoblip "채널 및 번호" 섹션.]({% image_buster /assets/img/whatsapp/infoblip_numbers.png %}){: style="max-width:30%;"}<br><br>

2. **번호 구매** > 메시지를 보내고 싶은 국가 > **SMS**를 선택하세요.<br><br>\![번호를 구매하는 버튼.]({% image_buster /assets/img/whatsapp/infoblip_buy.png %})<br><br>

3. 선택한 국가에 따라 추가 등록 프로세스를 완료해야 할 수 있습니다(예: 미국 전화번호의 경우 10 DLC 또는 무료 전화 옵션 선택). 사용 가능한 옵션을 선택해야 합니다.<br><br>\![번호 유형을 선택하라는 페이지: 10 DLC 또는 무료 전화.]({% image_buster /assets/img/whatsapp/infoblip_10dlc.png %}){: style="max-width:70%;"}<br><br>

4. 사용 가능한 제안을 선택한 후 나머지 단계를 진행하고 요청이 처리될 때까지 기다리세요. 상태를 확인하려면 **번호** > **내 요청**로 이동하세요. <br><br>\![수수료 및 범위 정보를 포함한 제안.]({% image_buster /assets/img/whatsapp/infoblip_offer.png %}){: style="max-width:70%;"}<br><br>

5. 선택한 국가에 따라 Infobip 팀이 등록 세부정보를 위해 연락할 때까지 기다리세요(예: 미국의 10DLC).<br><br>

6. Infobip에서 전화번호가 준비되면 Braze 대시보드로 이동하여 > **기술 파트너** > **WhatsApp**를 선택하고 **통합 시작** 또는 **WhatsApp 비즈니스 계정 추가**를 선택하여 [내장된 가입 워크플로우]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/embedded_signup/)를 트리거하세요.<br><br> **WhatsApp에 대한 전화번호 추가** 단계에서 전화번호를 확인하는 방법으로 **문자 메시지**를 선택하세요.<br><br>\![전화번호를 문자 메시지 또는 전화 통화로 확인하는 옵션이 있는 섹션.]({% image_buster /assets/img/whatsapp/infoblip_verify.png %})<br><br>

7. Infobip의 [로그 분석](https://www.infobip.com/docs/analyze/analyze-logs)을 고객 포털에서 확인하여 인증 코드를 찾으세요. 인증 코드가 나타나는 데 몇 분이 걸릴 수 있습니다. 그런 다음 인증 코드를 입력하고 설정을 완료하세요.




