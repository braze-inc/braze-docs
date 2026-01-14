---
nav_title: 여러 비즈니스 계정
article_title: 여러 WhatsApp 비즈니스 계정 및 전화번호
page_order: 2
description: "이 참조 문서에서는 WhatsApp 비즈니스 계정 및 전화번호를 추가하는 단계를 다룹니다."
page_type: reference
channel:
  - WhatsApp
---

# 여러 WhatsApp 비즈니스 계정 및 전화번호

> 각 작업 공간에 여러 WhatsApp 비즈니스 계정 및 구독 그룹(및 전화번호)을 추가할 수 있습니다. <br><br>각 구독 그룹은 하나의 고유한 전화번호에 연결되므로 동일한 전화번호를 여러 구독 그룹에 연결하거나 여러 전화번호를 하나의 구독 그룹에 연결할 수 없습니다.

## 여러 WhatsApp 비즈니스 계정 

여러 WhatsApp 비즈니스 계정을 보유하는 것은 여러 브랜드가 있는 Braze 작업 공간에서 사용자에게 WhatsApp 메시지를 보내고자 할 때 유용합니다. 이는 각 비즈니스 계정이 WhatsApp 내에서 독립적으로 운영되며 고유한 전화번호, 메시지 템플릿 및 품질 등급을 갖기 때문입니다.

동일한 Meta Business Manager 내에 중첩된 비즈니스 계정은 사용자 액세스 권한 관리 및 카탈로그를 공유합니다(현재 Braze에서는 지원되지 않음).

\![Braze와 WhatsApp 생태계의 다이어그램으로, 작업 공간과 WhatsApp 비즈니스 계정이 서로 연결되는 방식을 보여줍니다: 하나의 구독 그룹을 하나의 전화번호에 연결하고, 여러 WhatsApp 비즈니스 계정을 하나의 작업 공간에 연결하며, 하나의 작업 공간을 여러 Meta Business 포트폴리오에 연결할 수 있습니다.]({% image_buster /assets/img/whatsapp/whatsapp_braze_ecosystem.png %}) 

### WhatsApp 비즈니스 계정 추가하기

작업 공간당 최대 10개의 WhatsApp 비즈니스 계정을 추가할 수 있습니다. 비즈니스 계정은 서로 다른 Meta Business Manager에 중첩될 수 있습니다. 계정을 추가하려면:

1. **기술 파트너** > **WhatsApp**로 이동하여 **WhatsApp 비즈니스 계정 추가**를 선택합니다. 

\![비즈니스 계정을 추가하거나 구독 그룹 및 번호를 추가할 수 있는 WhatsApp 메시징 통합 섹션.]({% image_buster /assets/img/whatsapp/multiple_wabas.png %})

{: start="2"}
2\. 가입 워크플로를 진행합니다. 자세한 단계별 안내는 [WhatsApp 임베디드 가입]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/embedded_signup/)를 참조하십시오.

{% alert important %}
귀하의 전화번호는 다른 WhatsApp 계정에 등록되지 않아야 하며, 모든 WhatsApp 전화번호의 요구 사항을 따라야 합니다.
{% endalert %}

## 여러 구독 그룹 및 전화번호

메시지 템플릿은 동일한 WhatsApp 비즈니스 계정의 모든 전화번호 간에 공유됩니다. WhatsApp 구독 그룹에 대한 자세한 내용은 [구독 그룹]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_subscription/)을 참조하십시오.

각 WhatsApp 전화번호는 사용자에게 별도의 WhatsApp 채팅으로 표시됩니다. WhatsApp 비즈니스 계정 내의 각 전화번호는 서로 독립적으로 작동하므로 다음에 대해 동일하거나 다른 값을 가질 수 있습니다: 
- 표시 이름 
- 상태 
- 품질 등급 
- 메시징 한도 

### 구독 그룹 및 전화번호 추가

WhatsApp 비즈니스 계정당 최대 20개의 구독 그룹(및 발신 전화번호)을 추가할 수 있습니다. 구독 그룹 및 전화번호를 추가하려면:

1. **기술 파트너** > **WhatsApp**로 이동하여 **구독 그룹 및 번호 추가**를 선택하십시오.

\![비즈니스 계정을 추가하거나 구독 그룹 및 번호를 추가할 수 있는 WhatsApp 메시징 통합 섹션.]({% image_buster /assets/img/whatsapp/multiple_wabas.png %})

{: start="2"}
2\. 가입 워크플로를 진행합니다. <br><br> **WhatsApp 비즈니스 계정 선택** 단계에서 기존 WhatsApp 비즈니스 계정을 선택하고 새 전화번호를 추가하십시오. 이 번호는 다른 WhatsApp 계정에 등록되지 않아야 하며, 모든 WhatsApp 전화번호의 요구 사항을 따라야 합니다.

### 구독 그룹 및 전화번호 제거 

1. **청중** > **구독**로 이동하여 구독 그룹을 보관하십시오.
2. 메타 비즈니스 관리자에 가서 전화번호를 삭제하세요.
