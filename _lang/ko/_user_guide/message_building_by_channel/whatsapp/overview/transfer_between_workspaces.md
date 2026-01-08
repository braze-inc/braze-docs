---
nav_title: 작업 공간 간 전송
article_title: 작업 공간 간 전화번호 및 구독 그룹 전송
page_order: 4
description: "이 참조 문서에서는 WhatsApp 전화번호와 구독 그룹을 작업 공간 간에 전송하는 방법을 다룹니다."
page_type: reference
channel:
  - WhatsApp
---

# 작업 공간 간 WhatsApp 전화번호 및 구독 그룹 전송

> 이 페이지에서는 Braze 내에서 WhatsApp 비즈니스 계정(WABA) 전화번호와 관련된 구독 그룹을 한 작업 공간에서 다른 작업 공간으로 이동하는 방법을 다룹니다. 이 프로세스는 Braze와 함께 WhatsApp을 사용하는 경험을 간소화하고 엔지니어링 지원의 필요성을 줄입니다.

## 전제 조건

- 원래 작업 공간과 새 작업 공간 모두에서 [사용자 권한]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#list-of-permissions) "구독 그룹 관리"가 있는지 확인하십시오.
- WABA는 여러 [Braze 클러스터]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints)를 넘을 수 없습니다. 한 회사 내에서 작업하는 경우 이는 발생할 가능성이 낮습니다. 

## 전화번호 및 구독 그룹 전송

### 1단계: 구독 그룹 보관

WhatsApp 구독 그룹을 보관하려면 다음 단계를 따르십시오:

1. 구독 그룹이 현재 존재하는 작업 공간으로 이동합니다.
2. **청중** > **구독 그룹 관리**로 이동하여 이동하려는 WhatsApp 전화번호와 관련된 구독 그룹을 찾습니다.
3. 구독 그룹의 상태 위에 마우스를 올리고 <i class="fa-solid fa-box-archive"></i> **보관**를 선택하면 구독 그룹이 비활성으로 표시되지만 삭제되지는 않습니다.

\!["보관" 버튼이 구독 그룹의 "활성" 상태 위에 마우스를 올릴 때 나타납니다.]({% image_buster /assets/img/whatsapp/archive_subscription_group.png %}){: style="max-width:70%;"}

### 2단계: WhatsApp 전화번호를 새 작업 공간에 통합합니다.

1. WhatsApp 전화번호를 이동할 작업 공간으로 이동합니다.
2. **파트너 통합** > **기술 파트너** > **WhatsApp**으로 이동한 다음, **WhatsApp 메시징 통합** 섹션으로 스크롤합니다. 
3. **새 구독 그룹 및 전화번호 만들기** 옵션을 선택합니다.
4. 통합 프로세스를 시작하며, 이 과정에서 보관된 구독 그룹에서 전화번호를 선택할 수 있습니다.

### 3단계: 통합을 확인합니다.

1. 통합을 완료한 후, WhatsApp 전화번호가 이제 새 작업 공간의 구독 그룹과 연결되어 있는지 확인합니다.
2. 해당 WhatsApp 전화번호를 통해 메시지를 보낼 수 있고 받을 수 있는지 테스트합니다.

## 고려사항

- WhatsApp 전화번호를 원래 작업 공간으로 다시 전송해야 하는 경우, 단계를 반복합니다. 대상 작업 공간에서 구독 그룹을 보관한 다음, 원래 작업 공간에 통합합니다.
- 전송 중에 Meta Business Manager에서 WhatsApp 전화번호를 제거할 필요가 없습니다.