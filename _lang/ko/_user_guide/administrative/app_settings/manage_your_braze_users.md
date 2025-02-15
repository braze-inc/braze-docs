---
nav_title: 회사 사용자
article_title: 회사 사용자
page_order: 23
layout: dev_guide
guide_top_header: "회사 사용자"
guide_top_text: "회사의 Braze 계정 관리자는 사용자를 보다 세분화하거나 사례별로 관리해야 할 필요가 있을 수 있습니다. Braze는 팀을 만들고 사용자 권한 및 회사 전체 설정을 관리하여 이를 지원합니다."

page_type: landing
description: "이 랜딩 페이지에는 사용자 추가 및 삭제, 사용자 권한 설정, 팀 만들기, 회사 설정 관리 등 Braze 사용자 관리에 대한 문서가 나열되어 있습니다."

guide_featured_title: "섹션 기사"
guide_featured_list:
- name: Braze 사용자 관리
  link: /docs/user_guide/administrative/app_settings/manage_your_braze_users/adding_users_to_your_dashboard/
  image: /assets/img/braze_icons/user-plus-01.svg
- name: 사용자 권한 설정
  link: /docs/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/
  image: /assets/img/braze_icons/user-square.svg
- name: Teams
  link: /docs/user_guide/administrative/app_settings/manage_your_braze_users/teams/
  image: /assets/img/braze_icons/users-01.svg
---

## 팀, 권한 집합 및 역할 간의 차이점은 무엇인가요? 

팀, 권한 세트 및 사용자 역할을 사용하여 Braze 내에서 대시보드 사용자 액세스 및 책임을 관리할 수 있습니다. 각 기능에는 서로 다른 권한 및 액세스 제어 컬렉션이 포함되어 있습니다.

### 주요 차이점

크게 보면 각 기능의 범위가 다릅니다:
- 권한 집합은 대시보드 사용자가 모든 워크스페이스에서 수행할 수 있는 작업을 제어합니다.
- 역할은 대시보드 사용자가 특정 작업 영역에서 수행할 수 있는 작업을 제어합니다.
- 팀은 대시보드 사용자가 메시지를 보낼 수 있는 오디언스를 제어합니다.

| 기능 | 할 수 있는 일
| - | - |
| [권한 집합]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#creating-a-permission-set) > 특정 주제 영역 또는 작업과 관련된 권한("개발자" 및 "마케팅 담당자" 등)을 묶은 다음, 여러 워크스페이스에서 동일한 권한이 필요한 대시보드 사용자에게 해당 권한을 적용합니다. |
| [역할]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#creating-a-role) > 개별 사용자 지정 권한 및 작업 영역 액세스 제어를 미리 정의된 역할(예: '마케팅 담당자 - 패션 브랜드' 및 '마케팅 담당자 - 스킨케어 브랜드')에 묶은 다음 대시보드 사용자에게 역할을 할당하여 관련 작업 영역 액세스 및 권한을 직접 부여할 수 있습니다. |
| [팀]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) > 대상(예: 고객 기반 위치, 언어 및 사용자 지정 속성)에 따라 대시보드 사용자의 리소스 액세스를 제한하세요. |
{: .reset-td-br-1 .reset-td-br-2 }