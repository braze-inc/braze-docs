---
nav_title: WhatsApp 설정
article_title: WhatsApp 설정
alias: /partners/whatsapp/
description: "이 문서에서는 사전 요구 사항 및 제안된 다음 단계를 포함하여 Braze WhatsApp 채널을 설정하는 방법에 대해 설명합니다."
page_type: partner
search_tag: Partner
page_order: 1
channel:
  - WhatsApp
search_rank: 2
---

# WhatsApp 설정

> [WhatsApp](https://www.whatsapp.com/) 비즈니스 메시징은 전 세계에서 널리 사용되는 P2P 메시징 플랫폼으로, 기업용 대화 기반 메시징을 제공합니다.	

## 필수 조건

통합을 진행하기 전에 다음 사항을 확인하시기 바랍니다:

- **옵트인 정책:** WhatsApp은 고객이 메시징에 옵트인하도록 요구합니다.
- **WhatsApp 콘텐츠 규칙:** WhatsApp에는 준수해야 하는 몇 가지 [콘텐츠 규칙이](https://www.whatsapp.com/legal/commerce-policy?l=en) 있습니다.
- **규정 준수:** 모든 해당 Braze 및 메타 설명서와 해당 [메타 정책](https://www.whatsapp.com/legal/?lang=en)을 준수하세요.
- **24시간 대화 제한:** 비즈니스가 초기 템플릿 메시지를 보내거나 사용자가 메시지를 보내면 24시간 동안 두 당사자가 메시지를 주고받을 수 있는 창이 열립니다. 
- **대화 시작하기:** 사용자는 언제든지 대화를 시작할 수 있습니다. 기업은 승인된 메시지 템플릿을 통해서만 대화를 시작할 수 있습니다.
<br><br>

| 요구 사항| 설명|
| ---| --- |
| 메타 비즈니스 매니저 계정 | 이 메시징 채널을 활용하려면 메타 비즈니스 계정이 필요합니다. |
| WhatsApp Business 계정 | 이 메시징 채널을 활용하려면 WhatsApp 비즈니스 계정이 필요합니다. |
| WhatsApp 전화번호 | 메시징 채널을 사용하려면 WhatsApp의 [클라우드 API](https://developers.facebook.com/docs/whatsapp/cloud-api/phone-numbers) 또는 [온프레미스 API에](https://developers.facebook.com/docs/whatsapp/on-premises/phone-numbers) 대한 요구 사항을 충족하는 전화번호를 확보해야 합니다.  | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 통합

### 1단계: WhatsApp 메신저를 Braze에 연결

Braze에서 **파트너 통합** > **기술 파트너**로 이동하여 **WhatsApp**을 검색합니다.

WhatsApp 파트너 페이지에서 **연동 시작**을 선택합니다.

![][1]

열린 창에서 **통합 시작** 버튼이 나타날 때까지 **다음**을 선택합니다. 버튼을 선택하여 통합 프로세스를 시작합니다.

![Braze를 WhatsApp에 연결하는 방법에 대한 안내입니다.][7]

### 2단계: WhatsApp 설정

다음으로 Braze 설정 워크플로에 대한 메시지가 표시됩니다. 단계별 안내는 [WhatsApp 임베디드 가입]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/embedded_signup/)을 참조하세요. 

이 흐름 안에서 여러분은 그렇게 할 것입니다.
1. 메타 및 WhatsApp 비즈니스 계정을 만들거나 선택합니다. [WhatsApp 표시 이름 가이드라인](https://www.facebook.com/business/help/757569725593362)을 검토하세요. <br><br>회사에 이미 하나 이상의 기존 메타 비즈니스 계정이 있을 가능성이 높습니다. 이 경우 WhatsApp 비즈니스 계정이 어디에 위치할지 선택하세요. WhatsApp에 대한 사용자 권한 및 비즈니스 인증은 메타 비즈니스 계정에서 중앙에서 제어됩니다.<br><br>
2. WhatsApp 비즈니스 프로필을 만듭니다.
3. WhatsApp 비즈니스 번호를 인증합니다.<br><br>

설정이 완료되면 사용자를 위한 전용 WhatsApp 구독 그룹이 생성됩니다.

### 3단계: WhatsApp 템플릿 만들기

승인된 WhatsApp 메시지 템플릿만 고객과의 대화를 시작하는 데 사용할 수 있습니다. WhatsApp 템플릿은 [메타 비즈니스 관리자](https://www.facebook.com/business/help/2055875911147364?id=2129163877102343)에서 만들 수 있습니다. Braze에서 지원하는 WhatsApp 메시징 기능 목록은 [지원되는 WhatsApp 기능]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create#supported-whatsapp-features)에서 확인하세요.

1. **[템플릿 관리자로](https://business.facebook.com/wa/manage/message-templates) 이동합니다.**<br>
메타 비즈니스 매니저의 **계정 도구**에서 **메시지 템플릿**을 선택합니다.
다음으로 **템플릿 만들기**를 선택합니다.<br><br>![][3]{: style="max-width:100%;"}<br><br>
2. **메시지 설정**<br>
새 메시지 템플릿 작성기에서 메시지의 카테고리를 선택하고 템플릿 이름을 지정한 다음 지원할 언어를 선택합니다. 나중에 언어를 삭제하거나 추가할 수 있습니다.<br><br> 
	사용 가능한 메시지 템플릿 카테고리는 다음과 같습니다:
	- 마케팅: 프로모션 혜택, 제품 공지 등을 전송하여 인지도와 인게이지먼트를 높이세요.
	- 유틸리티: 계정 업데이트, 주문 업데이트, 알림 등을 전송하여 중요한 정보를 공유하세요.
	- 인증: 고객이 계정에 액세스할 수 있는 코드를 보내세요.<br><br> 
	![][4]{: style="max-width:100%;"}<br><br>
3. **템플릿 편집**<br>
다음으로 메시지 템플릿을 만들라는 메시지가 표시됩니다. <br><br>여기에서 텍스트 또는 미디어 헤더, 텍스트 본문, 메시지 바닥글 및 버튼을 제공할 수 있습니다. 현재 동영상 및 문서 헤더는 사용할 수 없으며, 헤더는 텍스트 또는 이미지 유형이어야 합니다. 오른쪽에 메시지 미리보기가 표시됩니다. <br><br>메타는 Liquid를 지원하지 않지만, 나중에 Braze에서 Liquid 변수로 대체할 수 있는 변수를 템플릿에 넣을 수 있습니다. **변수 추가** 버튼을 선택하면 됩니다.<br><br>![][5]{: style="max-width:100%;"}<br><br>템플릿을 완성했으면 **제출을** 누릅니다. 

#### 템플릿 승인 시간

메시지 템플릿의 승인 상태는 메타 비즈니스 매니저의 **메시지 템플릿** 페이지에서 확인하거나 Braze에서 캠페인 또는 캔버스를 만들 때 확인할 수 있습니다. 또한 알림 권한에 따라 WhatsApp 팀으로부터 이메일로 알림을 받을 수도 있습니다. 

{% alert note %}
승인된 템플릿은 원하는 만큼 많은 캠페인과 캔버스에서 사용할 수 있습니다. 또한 원하는 수만큼 옵트인한 사용자에게 보낼 수도 있습니다. 템플릿의 품질이 저하되지 않는 한 마찬가지입니다.
{% endalert %}

### 4단계: WhatsApp 캠페인 만들기

WhatsApp 템플릿이 승인되면 대시보드로 이동하여 [WhatsApp 캔버스 또는 캠페인]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create/)을 구축할 수 있습니다. 

{% alert note %}
WhatsApp 비즈니스 계정이 생성되면 메타에서 시작 메시징 한도를 결정합니다. 자세히 알아보려면 [처리량을]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/10dlc/#throughput) 확인하세요.
{% endalert %}

## 다음 단계

통합을 완료한 후에는 다음 두 가지 메타 프로세스를 완료하는 것이 좋습니다:
- [비즈니스 확인](https://www.facebook.com/business/help/2058515294227817?id=180505742745347)
	- 기존 메타 비즈니스 매니저를 사용했다면 이미 비즈니스 인증이 되어 있을 수 있습니다. 
- [공식 비즈니스 계정](https://www.facebook.com/business/help/604726921052590?ref=search_new_0)

또한 [사용자 전화번호]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_phone_numbers/)에 대해 알아보고 [조직에서 메시지 템플릿](https://www.facebook.com/business/help/2169003770027706?id=2190812977867143)을 만들기 위해 액세스 권한이 필요한 사용자를 추가하는 것이 좋습니다.

### WhatsApp 클라우드 API 로컬 스토리지

Braze는 WhatsApp의 [클라우드 API 로컬 스토리지를](https://developers.facebook.com/docs/whatsapp/cloud-api/overview/local-storage?content_id=ka6F9gESPqhQpm5) 지원합니다. 이 기능을 사용하려면 Braze 고객 지원 관리자에게 문의하세요.

[1]: {% image_buster /assets/img/whatsapp/whatsapp1.png %}
[2]: {% image_buster /assets/img/whatsapp/whatsapp10.png %}
[3]: {% image_buster /assets/img/whatsapp/whatsapp2.png %}
[4]: {% image_buster /assets/img/whatsapp/whatsapp3.png %}
[5]: {% image_buster /assets/img/whatsapp/whatsapp4.png %}
[6]: {% image_buster /assets/img/whatsapp/whatsapp5.png %}
[7]: {% image_buster /assets/img/whatsapp/instructions.png %} 
