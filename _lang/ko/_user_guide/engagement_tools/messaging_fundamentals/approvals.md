---
nav_title: 승인
article_title: 승인
page_order: 2
page_type: reference
description: "이 참고 문서에서는 캠페인과 캔버스가 가질 수 있는 다양한 상태와 그 의미에 대한 개요를 설명합니다."
tool:
    - Campaigns
    - Canvas
---

# 캠페인 및 캔버스 승인

> 캠페인 및 캔버스에 대한 승인 프로세스는 출시 전 워크플로에 검토 프로세스를 추가합니다. 이렇게 하면 캠페인 또는 캔버스 에디터의 각 섹션이 승인되었는지 확인하여 실행할 수 있습니다.

## 작동 방식

에디터의 마지막 단계에서 캠페인 또는 캔버스의 세부 정보를 검토할 수 있습니다. 캠페인의 경우 **검토 요약**, 캔버스의 경우 **요약입니다**. 

관리자가 승인 워크플로우를 켠 경우 요약의 각 섹션은 적절한 권한을 가진 사용자가 승인해야 메시징을 시작할 수 있습니다. 각 섹션의 기본값은 **승인 보류 중입니다**.

{% tabs %}
{% tab campaign %}
캠페인을 시작하려면 이러한 주요 구성 요소를 승인해야 합니다:

- **메시지:** 이것이 캠페인 메시지입니다.
- **전달:** 전달 유형이며 사용자가 캠페인을 수신할 시기를 결정합니다.
- **타겟 오디언스:** 이에 따라 캠페인을 수신할 대상자가 결정됩니다.
- **전환 이벤트:** 참여 및 보고 목적으로 추적하는 측정기준입니다.
{% endtab %}

{% tab canvas %}
캔버스를 시작하려면 이러한 주요 구성 요소를 승인해야 합니다:

- **전환 이벤트:** 참여 및 보고 목적으로 추적하는 측정기준입니다.
- **참가 일정:** 여기에는 입력 일정의 유형과 사용자가 캔버스에 입력해야 하는 시기가 포함됩니다.
- **타겟 오디언스:** 이 캔버스에 누가 입장할지 결정됩니다.
- **설정 보내기:** 다음은 캔버스의 모든 단계에 대한 전송 옵션입니다. 
- **캔버스를 구축합니다:** 이것이 캔버스 사용자 여정입니다.
{% endtab %}
{% endtabs %}

## 승인 워크플로 켜기

기본적으로 캠페인 및 캔버스에 대한 승인 워크플로 설정은 꺼져 있습니다. 이 기능을 사용 **설정하려면 설정** > **승인 워크플로로** 이동하여 해당 토글을 선택합니다:
- **내 워크스페이스]의 모든 캠페인에 승인 워크플로우 사용**
- **내 작업 공간]의 모든 캔버스에 승인 워크플로우 사용**

{% alert important %}
[API 캠페인]({{site.baseurl}}/api/api_campaigns) 및 [트랜잭션 이메일 캠페인에]({{site.baseurl}}/user_guide/message_building_by_channel/email/transactional_message_api_campaign) 대한 구축 워크플로에서는 캠페인 승인이 지원되지 않습니다.
{% endalert %}

## 사용자 권한 설정

승인 워크플로우가 켜진 후에는 대시보드 사용자가 캠페인과 캔버스를 즉시 승인하거나 거부할 수 있도록 사용자 권한을 설정해야 합니다. 두 권한 모두 워크스페이스 또는 [Teams에]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) 적용하거나 [권한 집합에]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#permission-sets) 추가할 수도 있습니다.

{% tabs %}
{% tab campaign %}
['캠페인 승인 및 거부' 권한이]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#managing-limited-and-team-role-permissions) 있어야 합니다. 이 권한은 캠페인의 승인 상태를 업데이트할 수 있는 사용자를 제어합니다. 캠페인의 구성 요소를 자체 승인할 수 있습니다.
{% endtab %}

{% tab canvas %}
["캔버스 승인 및 거부" 권한이]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#managing-limited-and-team-role-permissions) 있어야 합니다. 이 권한이 있는 사용자는 캔버스 워크플로에서 다음 작업을 수행할 수 있습니다:

- 캔버스를 승인하지만 실행하지 않음
- 캔버스를 시작하지만 승인하지 않음
- 캔버스 승인 및 실행
- 캔버스를 승인하거나 실행하지 않습니다.

**요약** 단계에서 승인 상태를 설정한 후 이후에 캔버스를 변경하면 저장 시 모든 승인 상태가 초기화됩니다. 이는 초안 캔버스 또는 출시 후 캔버스에서 변경한 모든 사항에 적용됩니다. 예를 들어 타겟 오디언스만 변경하는 경우 **요약** 단계에서는 모든 섹션의 승인 상태가 기본값인 보류 중 상태로 되돌아갑니다.
{% endtab %}
{% endtabs %}

{% alert important %}
실시간 캠페인을 편집하려면 '캠페인 승인 및 거부' 권한이 필요합니다. 캠페인 초안 버전은 아직 사용할 수 없으므로 사용자가 변경 사항을 승인해야 합니다. 캔버스는 사용자가 변경하여 초안으로 저장하고 다른 사용자가 승인하고 캔버스를 실행할 수 있으므로 그렇지 않습니다.
{% endalert %}
