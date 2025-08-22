---
nav_title: 다중 비즈니스 계정 
article_title: 다중 WhatsApp 비즈니스 계정 및 전화번호
page_order: 2
description: "이 참조 문서에서는 WhatsApp 비즈니스 계정 및 전화번호를 추가하는 단계를 다룹니다."
page_type: reference
channel:
  - WhatsApp
---

# 여러 개의 WhatsApp 비즈니스 계정 및 전화번호

> 각 워크스페이스에 여러 개의 WhatsApp 비즈니스 계정과 구독 그룹(및 전화번호)을 추가할 수 있습니다. <br><br>각 구독 그룹은 하나의 고유한 전화번호에 연결되므로 동일한 전화번호를 여러 구독 그룹에 연결하거나 여러 전화번호를 하나의 구독 그룹에 연결할 수 없습니다.

## 여러 WhatsApp 비즈니스 계정 

여러 WhatsApp 비즈니스 계정을 보유하는 것은 여러 브랜드가 있는 Braze 작업 공간에서 사용자에게 WhatsApp 메시지를 보내고자 할 때 유용합니다. 이는 각 비즈니스 계정이 WhatsApp 내에서 별도로 운영되며 고유한 전화번호, 메시지 템플릿 및 품질 등급을 가지고 있기 때문입니다.

동일한 Meta Business 매니저 내에 중첩된 비즈니스 계정도 사용자 액세스 권한 관리 및 카탈로그를 공유합니다(Braze에서는 아직 지원되지 않음).

![Diagram of the Braze and WhatsApp ecosystem, showing how workspaces and WhatsApp Business accounts connect to each other: you can connect one subscription group to one phone number, multiple WhatsApp Business accounts to one workspace, and one workspace to multiple Meta Business Portfolios.]({% image_buster /assets/img/whatsapp/whatsapp_braze_ecosystem.png %}) 

### WhatsApp 비즈니스 계정 추가

워크스페이스당 최대 10개의 WhatsApp 비즈니스 계정을 추가할 수 있습니다. The business accounts can be nested in different Meta Business Managers. 계정을 추가하려면:

1. Go to **Technology Partners** > **WhatsApp** and select **Add WhatsApp Business Account**. 

![WhatsApp Messaging Integration section with options to add a business account or add a subscription group and number.]({% image_buster /assets/img/whatsapp/multiple_wabas.png %})

{: start="2"}
2\. 가입 워크플로를 진행하세요. For a detailed step-by-step walkthrough, refer to [WhatsApp embedded signup]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/embedded_signup/).

{% alert important %}
전화번호는 다른 WhatsApp 계정에 등록되지 않은 것을 포함하여 모든 WhatsApp 전화번호 요구 사항을 충족해야 합니다.
{% endalert %}

## 다중 구독 그룹 및 전화번호

메시지 템플릿은 동일한 WhatsApp 비즈니스 계정의 모든 전화번호에서 공유됩니다. 자세한 내용은 [구독 그룹]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_subscription/)을 참조하세요.

각 WhatsApp 전화번호는 사용자에게 별도의 WhatsApp 채팅으로 표시됩니다. WhatsApp 비즈니스 계정 내의 각 전화번호는 서로 독립적으로 작동하므로 다음에 대해 동일하거나 다른 값을 가질 수 있습니다: 
- 표시 이름 
- 상태 
- 품질 등급 
- 메시징 제한 

### 구독 그룹 및 전화번호 추가

WhatsApp 비즈니스 계정당 최대 20개의 구독 그룹(및 발신 전화번호)을 추가할 수 있습니다. 구독 그룹 및 전화번호를 추가하려면:

1. Go to **Technology Partners** > **WhatsApp** and select **Add Subscription Group and Number**.

![WhatsApp Messaging Integration section with options to add a business account or add a subscription group and number.]({% image_buster /assets/img/whatsapp/multiple_wabas.png %})

{: start="2"}
2\. 가입 워크플로를 진행하세요. <br><br> **WhatsApp 비즈니스 계정 선택** 단계에서 기존 WhatsApp 비즈니스 계정을 선택하고 새 전화번호를 추가하세요. 이 번호는 다른 WhatsApp 계정에 등록되지 않는 것을 포함하여 모든 WhatsApp 전화번호 요구 사항을 충족해야 합니다.

### 구독 그룹 및 전화번호 제거 

1. **오디언스** > **구독** 및 구독 그룹을 보관하세요.
2. Meta Business 매니저로 이동하여 전화번호를 삭제하세요.
