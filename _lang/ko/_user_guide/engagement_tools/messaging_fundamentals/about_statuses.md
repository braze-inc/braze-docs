---
nav_title: 상태
article_title: 캠페인 및 캔버스 상태
page_order: 1
description: "캠페인 및 캔버스의 상태와 대시보드에서 캔버스를 사용하는 방법에 대해 알아보세요."
tool:
    - Campaigns
    - Canvas
---

# 캠페인 및 캔버스 상태

> 캠페인 및 캔버스의 상태와 대시보드에서 캔버스를 사용하는 방법에 대해 알아보세요.

## 상태별 필터링

캠페인 또는 캔버스를 상태별로 필터링하려면 **모든 상태를** 선택한 다음 상태를 선택합니다.

![Braze 대시보드의 '모든 상태' 드롭다운.]({% image_buster /assets/img/messaging_fundamentals/filter-by-status.png %}){: style="max-width:70%;"}

## 상태 변경하기

캠페인 또는 캔버스의 상태를 변경하려면 <i class="fas fa-ellipsis-vertical"></i> 메뉴를 선택한 다음 상태를 선택합니다.

![Braze 대시보드의 캔버스 목록과 캔버스 중 하나에 대한 메뉴가 열려 있습니다.]({% image_buster /assets/img/messaging_fundamentals/change-status.png %})

## 사용 가능한 상태

캠페인 및 캔버스에 사용할 수 있는 상태입니다:

| 상태 | 설명 |
| --- | --- |
| 활성 | 활성 캠페인과 캔버스가 전송 중입니다. 기본적으로 각 페이지에는 활성 캠페인과 캔버스가 표시됩니다. |
| 임시저장본 | 캠페인 및 캔버스의 초안은 저장되지만 실행되지는 않습니다. 편집을 계속하고 전송을 시작하려면 Braze 대시보드에서 **메시징으로** 이동하여 초안을 선택하고 **캔버스** 또는 **캠페인을** 선택하면 됩니다. |
| 아카이브됨 | 보관된 캠페인 및 캔버스는 더 이상 전송되지 않는 메시지입니다. 이러한 캠페인과 캔버스는 통계 그래프에서도 제거됩니다. [**홈**]({{site.baseurl}}/user_guide/analytics/dashboard/home_dashboard) 및 [**Revenue**]({{site.baseurl}}/user_guide/analytics/reporting/revenue_report) 페이지의 통계 그래프에서도 제거됩니다.|
| 중지됨 | 중지된 캠페인과 캔버스는 일시 중지되지만 계속 편집할 수 있습니다. 다시 시작하려면 <i class="fas fa-ellipsis-vertical"></i> 메뉴를 선택한 다음 **다시 시작을** 선택합니다. 자세한 내용은 [중지된 캔버스 동작을](#stopped-canvas-behavior) 참조하세요. |
| 유휴상태 | 캠페인이나 캔버스가 더 이상 메시지를 보내지 않는 경우, Braze는 캠페인과 캔버스 목록을 정렬하고 관리하는 데 도움이 되도록 유휴 상태로 지정합니다. 자동으로 중지되는 캠페인 또는 캔버스와 관련 중지 날짜를 확인할 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 중지된 캔버스 동작 {#stopped-canvas-behavior}

캔버스가 중지되면 다음과 같은 일이 발생합니다:

- **예약된 메시지:** 예약된 메시지는 캔버스에서 사용자의 위치와 관계없이 전송되지 않습니다. 여기에는 속도 제한으로 인해 대기열에 오른 사용자도 포함됩니다.
- **이메일 전송:** 이메일 서비스 제공업체(ESP)가 기존 요청을 계속 처리할 수 있으므로 이메일 전송이 즉시 중단되지 않을 수 있습니다.
- **지연 단계:** [지연 단계에]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/) 있는 사용자는 정상적으로 캔버스에 남아 있지만 설정된 기간이 끝나면 캔버스를 종료합니다.

캔버스를 다시 시작하려면 <i class="fas fa-ellipsis-vertical"></i> 메뉴를 선택한 다음 **다시 시작을** 선택합니다. 다시 활성화하면 예약된 시간이 아직 지나지 않았다면 이전에 중지된 모든 메시지가 예약된 대로 전송됩니다.

## Best practices

### 상태별 메시지 모니터링

상태별로 메시지를 모니터링하여 성과 세부 정보를 검토할 수 있습니다. 예를 들어 일련의 활성 캠페인이 있는 경우 참여 지표를 통해 각 캠페인의 성과를 평가하고 필요에 따라 조정할 수 있습니다. 대신 중지된 캔버스가 몇 개 있는 경우 메시징을 위해 캔버스를 재개할지 아니면 완전히 보관할지 고려할 수 있습니다.

{% alert tip %}
정리 정돈을 위한 더 많은 방법을 찾고 계신가요? [팀과]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams) [태그를]({{site.baseurl}}/user_guide/administrative/app_settings/tags) 추가하여 더 많은 컨텍스트를 한 눈에 파악할 수 있습니다.
{% endalert %}

### 활성 메시지 감사

활성 캠페인 및 캔버스에 대한 감사를 수행하여 관련성 및 성과를 평가하고 오래된 캠페인 및 캔버스를 제거하거나 업데이트하여 메시지를 최신 상태로 유지할 수 있습니다.
