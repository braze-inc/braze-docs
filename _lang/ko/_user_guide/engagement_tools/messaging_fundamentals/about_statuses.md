---
nav_title: 상태
article_title: 캠페인 및 캔버스 상태
page_order: 1
description: "캠페인 및 캔버스의 상태와 대시보드에서 이를 사용하는 방법에 대해 알아보세요."
tool:
    - Campaigns
    - Canvas
---

# 캠페인 및 캔버스 상태

> 캠페인 및 캔버스의 상태와 대시보드에서 이를 사용하는 방법에 대해 알아보세요.

## 상태별 필터링

캠페인이나 캔버스를 상태별로 필터링하려면 **모든 상태**을 선택한 다음 상태를 선택하세요.

\![Braze 대시보드의 '모든 상태' 드롭다운.]({% image_buster /assets/img/messaging_fundamentals/filter-by-status.png %}){: style="max-width:70%;"}

## 상태 변경

캠페인이나 캔버스의 상태를 변경하려면 <i class="fas fa-ellipsis-vertical"></i> 메뉴를 선택한 다음 상태를 선택하세요.

\![Braze 대시보드의 캔버스 목록, 하나의 캔버스에 대한 메뉴가 열려 있습니다.]({% image_buster /assets/img/messaging_fundamentals/change-status.png %})

## 사용 가능한 상태

다음은 캠페인 및 캔버스에 대한 사용 가능한 상태입니다:

| 상태 | 설명 |
| --- | --- |
| 활성 | 활성 캠페인 및 캔버스는 전송 중입니다. 기본적으로 활성 캠페인 및 캔버스가 해당 페이지에 표시됩니다. |
| 초안 | 캠페인 및 캔버스의 초안은 저장되지만 시작되지 않았습니다. 편집을 계속하고 전송을 시작하려면 Braze 대시보드에서 **메시징**으로 이동하여 초안을 선택하거나 **캔버스** 또는 **캠페인**을 선택할 수 있습니다. |
| 보관됨 | 보관된 캠페인과 캔버스는 더 이상 전송되지 않는 메시지입니다. 이 캠페인과 캔버스는 [**홈**]({{site.baseurl}}/user_guide/analytics/dashboard/home_dashboard) 및 [**수익**]({{site.baseurl}}/user_guide/analytics/reporting/revenue_report) 페이지의 통계 그래프에서 제거됩니다.|
| 중지됨 | 중지된 캠페인과 캔버스는 일시 중지되지만 여전히 편집할 수 있습니다. 재개하려면 <i class="fas fa-ellipsis-vertical"></i> 메뉴를 선택한 다음 **재개**를 선택하세요. 자세한 정보는 [중지된 캔버스 동작](#stopped-canvas-behavior)을 참조하세요. |
| 대기 중 | 캠페인이나 캔버스가 더 이상 메시지를 전송하지 않을 때, Braze는 캠페인과 캔버스 목록을 정리하고 관리하는 데 도움이 되도록 대기 상태를 할당합니다. 어떤 캠페인이나 캔버스가 자동으로 중지될 것인지와 관련된 중지 날짜를 볼 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 중지된 캔버스 동작 {#stopped-canvas-behavior}

캔버스가 중지되면 다음과 같은 일이 발생합니다:

- **예약된 메시지:** 사용자의 캔버스 내 위치와 관계없이 예약된 메시지는 전송되지 않습니다. 이것은 비율 제한으로 인해 대기 중인 사용자도 포함됩니다.
- **이메일 전송:** 이메일 전송은 즉시 중지되지 않을 수 있으며, 이메일 서비스 제공업체(ESP)가 기존 요청을 계속 처리할 수 있습니다.
- **지연 단계:** [지연 단계]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/)에 있는 사용자는 정상적으로 그곳에 남아 있지만 설정된 기간이 끝나면 캔버스를 종료합니다.

캔버스를 재개하려면 <i class="fas fa-ellipsis-vertical"></i> 메뉴를 선택한 다음 **재개**를 선택하세요. 재활성화되면, 이전에 중지된 모든 메시지가 예정된 대로 전송됩니다. 예정된 시간이 이미 지나지 않은 한.

## 모범 사례

### 상태별로 메시지 모니터링

상태별로 메시지를 모니터링하여 성과 세부정보를 검토할 수 있습니다. 예를 들어, 활성 캠페인 시리즈가 있는 경우 각 캠페인의 참여 지표를 통해 성과를 평가하고 필요에 따라 조정할 수 있습니다. 대신 중지된 캔버스가 몇 개 있다면, 메시징을 위해 재개해야 할지 아니면 완전히 아카이브해야 할지를 고려할 수 있습니다.

{% alert tip %}
조직을 유지할 수 있는 더 많은 방법을 찾고 있나요? [팀]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams) 및 [태그]({{site.baseurl}}/user_guide/administrative/app_settings/tags)를 추가하여 한눈에 더 많은 맥락을 제공하세요.
{% endalert %}

### 활성 메시지 감사

활성 캠페인 및 캔버스에 대한 감사를 수행함으로써 관련성과 성과를 평가하고, 구식 캠페인 및 캔버스를 제거하거나 업데이트하여 메시지를 신선하게 유지할 수 있습니다.
