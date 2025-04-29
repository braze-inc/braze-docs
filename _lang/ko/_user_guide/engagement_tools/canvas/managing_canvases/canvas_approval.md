---
nav_title: 캔버스 승인 및 권한
article_title: 캔버스 승인 및 권한 
page_order: 0.5
alias: "/canvas_approval/"
description: "이 참조 문서는 캔버스를 출시 전에 승인하는 방법과 관련 사용자 권한에 대해 설명합니다."
tool: Canvas
---

# 캔버스 승인 및 권한

> 캔버스 승인으로 출시 전에 워크플로우에 검토 프로세스가 추가됩니다. 이 방법으로 각 확인이 캔버스를 시작하기 위해 승인되었는지 확인할 수 있습니다.

## 캔버스 승인 켜기

캔버스에 대한 승인 워크플로를 켜려면 **설정** > **승인 워크플로**에서 **워크플레이스 설정**으로 이동하십시오. 기본값으로, 이 기능은 꺼져 있습니다.

![캠페인 및 캔버스에 대한 승인 워크플로우를 사용할 수 있는 옵션이 활성화된 승인 워크플로우 설정입니다.][1]

{% alert tip %}
Canvases를 승인하려면 적절한 [사용자 권한]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#managing-limited-and-team-role-permissions)이 있는지 확인하십시오.
{% endalert %}

### 사용자 권한 설정

Canvas에 대한 승인 워크플로우가 활성화된 후, **설정** > **회사 사용자**로 이동하여 특정 사용자가 캔버스를 즉시 승인하고 거부할 수 있도록 **캔버스 승인 및 거부**를 선택합니다. 이 권한은 작업 공간 또는 [Teams]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/)에 적용하거나 [권한 세트]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#permission-sets)에 추가할 수도 있습니다.

이 권한을 가진 사용자는 캔버스 워크플로우에서 다음 작업을 수행할 수 있습니다:
- 승인하지만 캔버스를 시작하지 마십시오
- 출시하지만 캔버스를 승인하지 마십시오
- 승인하고 캔버스를 시작하세요
- 캔버스를 승인하거나 시작하지 마십시오

![승인 및 거부 캔버스 권한에 대한 선택되지 않은 체크박스의 예로, 이 사용자는 캔버스를 승인하거나 거부할 권한이 없습니다.][3]{: style="max-width:70%" }

{% alert important %}
라이브 캠페인을 편집하려면 "캠페인 승인 및 거부" 권한이 필요합니다. 사용자는 캠페인의 초안 버전이 아직 제공되지 않기 때문에 변경 사항을 승인해야 합니다. 이것은 캔버스의 경우가 아닙니다. 사용자가 변경을 하고 초안으로 저장할 수 있으며, 다른 사용자가 캔버스를 승인하고 시작할 수 있습니다.
{% endalert %}

## 승인 사용

"캔버스 승인 및 거부" 권한이 있으면 캔버스 빌더의 **요약** 단계에 접근할 수 있습니다. 이 페이지는 전환 이벤트, 입력 일정 및 캔버스의 구성 요소 유형 및 수량을 포함하여 이러한 세부 정보를 승인하거나 거부할 수 있는 옵션과 함께 주요 캔버스 세부 정보 요약을 제공합니다. Canvas 승인에 대한 기본 상태는 **승인 대기 중**임을 유의하십시오.

**요약** 단계에서 승인 상태가 설정되면, 캔버스에 대한 이후의 모든 변경 사항은 저장될 때 모든 승인 상태를 재설정합니다. 이것은 초안 캔버스 또는 출시 후 캔버스에서 이루어진 모든 변경 사항에 적용됩니다. 예를 들어, 대상 오디언스에만 변경 사항을 적용하면 **요약** 단계에서 모든 섹션의 승인 상태가 기본값 상태인 보류 중으로 되돌아갑니다.

![승인된 것으로 표시된 전환 이벤트 및 입력 일정 세부 정보가 포함된 캔버스 승인 워크플로의 예입니다.][2]{: style="max-width:85%" }

각 섹션이 승인되면 **Launch** 버튼을 사용할 수 있으며, 캔버스를 시작할 수 있습니다.

[1]: {% image_buster /assets/img_archive/canvas_approval.png %}
[2]: {% image_buster /assets/img_archive/canvas_approval_summary.png %}
[3]: {% image_buster /assets/img_archive/canvas_approval_user_permissions.png %}