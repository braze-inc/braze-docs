---
nav_title: BYO WhatsApp 커넥터
article_title: 내 WhatsApp 커넥터 가져오기
page_order: 0
description: "이 참조 문서는 Braze가 Infobip WhatsApp 비즈니스 관리자에 접근할 수 있도록 하는 Bring Your Own WhatsApp 커넥터 설정을 위한 단계별 안내를 제공합니다."
page_type: reference
channel:
  - WhatsApp
---

# 내 WhatsApp 커넥터 가져오기

> Bring Your Own (BYO) WhatsApp 커넥터는 Braze와 Infobip 간의 파트너십을 제공하며, Infobip WhatsApp 비즈니스 관리자(WABA)에 대한 Braze의 접근을 허용합니다. 이를 통해 Braze를 사용하여 세분화, 개인화 및 캠페인 오케스트레이션을 하면서 Infobip과 직접 메시징 비용을 관리하고 지불할 수 있습니다. Braze는 아웃바운드 메시지, 인바운드 메시지 처리, WhatsApp 흐름 및 분석과 같은 WhatsApp 채널이 제공하는 모든 기존 기능을 유지합니다.

## 요구 사항 

| Requirement | 설명 |
| --- | --- |
| Infobip 계정 | BYO WhatsApp 커넥터를 사용하려면 Infobip 계정이 필요합니다.
| 메시징 크레딧 | WhatsApp 메시지를 보낼 때 Braze 메시징 크레딧을 소모합니다. |
| WhatsApp 요구 사항 | 모든 [WhatsApp 요구 사항]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/#prerequisites)을 완료하십시오. |
| Phone number | 편의를 위해 [Infobip을 통해 전화번호를 확보하는 것을 권장합니다.](https://www.infobip.com/docs/numbers/getting-started) |
{: .reset-td-br-1 .reset-td-br-2 role=”presentation” }

## 설정하기 

BYO WhatsApp 커넥터를 설정하기 전에 WhatsApp 비즈니스 계정의 이전 발송이 Infobip을 통해 이루어지지 않았는지 확인하십시오.

### 지원되는 사례

- WhatsApp 비즈니스 계정과 전화번호가 이전에 파트너와 연결된 적이 없음
- WhatsApp 비즈니스 계정이 네이티브 통합을 통해 Braze에 직접 연결되어 있음.
    - 전화번호를 한 번에 하나씩 새로운 WhatsApp 비즈니스 계정으로 마이그레이션하려면 [WhatsApp 전화번호 마이그레이션]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/phone_number_migration/)의 단계를 따르십시오.
- WhatsApp 비즈니스 계정이 Braze 및 Infobip과 다른 솔루션 제공업체에 연결되어 있음
    - 전화번호를 한 번에 하나씩 새로운 WhatsApp 비즈니스 계정으로 마이그레이션하려면 [WhatsApp 전화번호 마이그레이션]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/phone_number_migration/)의 단계를 따르십시오.

## 1단계: Infobip 계정 정보를 {#step-1} 가져옵니다.

1. Infobip에서 WhatsApp 비즈니스 계정과 함께 사용할 계정을 식별합니다. 
2. **개발자 도구** > **API 키**로 이동하여 **API 키 생성**을 선택합니다.

!["API 키 생성" 페이지는 생성 날짜가 "16/12/2025"이고 만료 날짜가 "16/12/36"입니다.]({% image_buster /assets/img/whatsapp/byo_connector/create_api_key.png %})

{: start="3"}
3\. 키에 "Braze - 내 작업 공간 이름 - 내 WABA 이름"과 같은 의미 있는 이름을 부여합니다.
4\. 토큰 만료 문제를 피하기 위해 먼 미래의 만료 날짜를 추가합니다.
    \- 만료 날짜 전에 새 API 키를 생성하고 WABA를 다시 연결해야 한다는 메모를 남깁니다.
5\. 다음 범위를 선택합니다:
- `Message:send`
- `Whatsapp:manage`
- `Whatsapp:message:send`
- `Account-management:manage`
- `Subscriptions:manage`
- `Metrics:manage`
6. 키를 생성한 후 API 키를 복사합니다.
    - 키는 생성 후 제한된 시간 동안만 복사할 수 있습니다. 미래에 다른 WhatsApp 비즈니스 계정을 연결해야 하는 경우 이러한 단계를 반복하여 새 키를 생성할 수 있습니다.

!["Braze 예제 API 키"에 6개의 추가 범위가 있습니다.]({% image_buster /assets/img/whatsapp/byo_connector/api_key.png %})

{: start="7"}
7\. 계정 API 기본 URL을 복사합니다.

!["API 키" 페이지는 강조 표시된 API 기본 URL이 있습니다.]({% image_buster /assets/img/whatsapp/byo_connector/api_base_url.png %})

## 2단계: 임베디드 가입 시작

1. Braze에서 **파트너 통합** > **기술 파트너** > **WhatsApp**로 이동합니다.
2. **BYO 커넥터 - Infobip** 탭을 선택합니다.

![WhatsApp 기술 파트너 페이지입니다.]({% image_buster /assets/img/whatsapp/byo_connector/byo_tab_tech_parners.png %})

{: start="3"}
3\. [1단계](#step-1)에서 API 키와 기본 URL을 입력합니다.
4\. Select **Connect**.
5\. 다음 고려 사항과 함께 [임베디드 가입 워크플로]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/embedded_signup/#whatsapp-embedded-signup-workflow)를 진행합니다:
- 다른 비즈니스 솔루션 제공업체에서 사용 중인 동일한 비즈니스 포트폴리오를 선택할 수 없습니다.
- 다른 비즈니스 솔루션 제공자가 사용 중인 전화번호를 선택할 수 없습니다.
- 새로운 WABA를 생성해야 하며, 기존의 것을 선택해서는 안 됩니다.

{% alert note %}
인증 코드를 받으려면 Infobip 대시보드 > **분석** > **로그**로 이동하여 수신 SMS 메시지에서 코드를 가져오세요.  
{% endalert %}

![인증 코드가 포함된 수신 SMS 메시지를 보여주는 메시지 로그입니다.]({% image_buster /assets/img/whatsapp/byo_connector/verification_code.png %})

설정을 완료한 후, 귀하의 전화번호는 WhatsApp 비즈니스 그룹 아래의 구독 그룹으로 나열됩니다. WhatsApp 비즈니스 그룹에는 연결된 Infobip 계정 이름과 API 기본 URL이 포함되어 있습니다. 네이티브 통합을 통해 연결된 계정은 Infobip 계정 이름이 없습니다.

{% alert note %}
각 WhatsApp 비즈니스 계정을 단일 Infobip 계정에 연결하세요. 추가 전화번호나 구독 그룹을 연결할 때마다, WhatsApp 비즈니스 계정이 이미 Infobip 계정에 연결되어 있다면 기존 계정의 API 자격 증명을 다시 입력해야 합니다.
{% endalert %}

## 3단계: 메시지 전송

네이티브 통합 전송 프로세스를 따르세요, 포함하여:
- [구독 그룹에 사용자 추가]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_subscription/)
- [메시지 만들기]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create/)

## 설정 문제 해결

### WhatsApp 비즈니스 계정 ID를 검색할 수 없습니다.

귀하의 WhatsApp 비즈니스 계정이 다른 Braze 작업 공간에 연결되어 있지 않은지 확인하세요.

### WhatsApp 비즈니스 계정 ID를 Infobip과 공유할 수 없습니다.

1. 귀하의 WhatsApp 비즈니스 계정이 Braze 또는 다른 파트너에 연결되어 있지 않은지 확인하세요.
2. 귀하의 WhatsApp 비즈니스 계정에 있는 전화번호가 다른 Infobip 계정에 연결되어 있지 않은지 확인하세요. 가져온 번호의 경우, Infobip에서 번호를 찾고 **번호 취소**를 선택할 수 있습니다.

![Infobip 번호에 대한 "번호 취소" 버튼입니다.]({% image_buster /assets/img/whatsapp/byo_connector/cancel_number.png %})

## 고려 사항 


현재 Braze의 모든 기존 기능이 지원되지만, 이러한 사용 사례는 현재 지원되지 않습니다.

| Use case | 이유 |
| --- | --- |
| Braze와 Infobip에서 수신 메시지 처리 | 이로 인해 두 시스템 중 하나에 의해 트리거된 논리 열이 방지되어 중복되고 잠재적으로 모순된 메시지 스레드가 생성됩니다. |
| Braze와 Infobip에서 메시지 전송 | Braze에 연결된 WhatsApp 비즈니스 계정의 경우 모든 전송은 Braze에서 시작됩니다. |
{: .reset-td-br-1 .reset-td-br-2 role=“presentation” }

