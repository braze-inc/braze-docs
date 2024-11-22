---
nav_title: 캠페인 승인
article_title: 캠페인 승인
alias: "/campaign_approval/"
page_order: 0
page_type: reference
description: "이 페이지에서는 캠페인 승인 절차에 대한 개요를 제공합니다."
tool: Campaigns
---

# 캠페인 승인하기

> 캠페인 승인은 캠페인을 시작하기 전에 워크플로에 검토 프로세스를 추가합니다. 이 기능은 캠페인 확인 워크플로 단계에서 사용할 수 있는 상태를 추가합니다. 캠페인 시작을 위해 각 확인이 승인되었는지 확인할 수 있습니다.

{% alert important %}
API 캠페인 및 트랜잭션 이메일 캠페인에 대한 구축 워크플로에서는 캠페인 승인이 지원되지 않습니다.
{% endalert %}

## 캠페인 승인 켜기

기본적으로 캠페인 승인 설정은 꺼져 있습니다. 이 기능을 사용 설정하려면 **설정** > **승인 워크플로**로 이동하세요.

{% alert note %}
[이전 탐색]({{site.baseurl}}/navigation)을 사용하는 경우 **설정 관리** > **승인 워크플로**에서 이 페이지를 찾을 수 있습니다.
{% endalert %}

## 승인 사용

캠페인 승인이 켜진 후에는 '캠페인 승인 및 거부' 권한이 있어야 합니다. 이 권한은 캠페인의 승인 상태를 업데이트할 수 있는 사용자를 제어합니다. 이 권한은 워크스페이스나 [팀]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/)에 적용하거나 [권한 집합]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#permission-sets)에 추가할 수도 있습니다.

캠페인 구축 워크플로우의 **요약 검토** 단계에서 승인 옵션을 사용하여 캠페인의 주요 구성 요소를 승인하거나 거부할 수 있습니다: **메시지**, **배달**, **타겟 인구** 및 **전환 이벤트**. 캠페인 승인의 기본 상태는 **승인 보류 중입니다**. 캠페인의 구성 요소를 자체 승인할 수 있다는 점에 유의하세요.

![][1]

각 섹션이 승인되면 **시작** 버튼이 활성화되고 캠페인을 시작할 수 있습니다! 

[1]: {% image_buster /assets/img_archive/campaign_approval_example.png %} 
