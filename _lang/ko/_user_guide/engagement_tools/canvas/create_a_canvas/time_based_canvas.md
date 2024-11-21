---
nav_title: 시간 기반 기능
article_title: 캔버스를 위한 시간 기반 기능
page_order: 1
tools: Canvas
page_type: reference
description: "이 참조 문서에서는 캔버스의 정의, 표준 시간대 및 시간 기반 기능의 예시를 다룹니다."

---

# 캔버스를 위한 시간 기반 기능

> 이 참조 문서에서는 전략, 문제 해결 및 일반적인 질문에 대한 답변을 지원하기 위한 캔버스의 시간 기반 기능에 대해 설명합니다. 

## 일정 지연

{% alert important %}
2023년 2월 28일부터 더 이상 원본 편집기를 사용하여 캔버스를 만들거나 복제할 수 없습니다. 이 섹션은 원래 캔버스 워크플로를 사용하여 만든 기존 캔버스의 일정을 편집할 때 참조할 수 있습니다. 캔버스 플로우 워크플로우의 시간 기반 기능은 [지연 구성 요소]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/)를 확인하세요.
{% endalert %}

### 즉시 발송

| 정의 |  시간대 |
| --- | --- |
| 사용자가 이전 단계를 수신한 직후 또는 첫 번째 단계인 경우 사용자가 캔버스에 입장한 직후 메시지를 보냅니다. | N/A |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![][1]

### X일 후 전송

| 정의 |  시간대 |
| --- | --- |
| 잠시 후 메시지를 보냅니다. 지연 시간을 초, 분, 시간, 일 또는 주 단위로 지정할 수 있습니다.  | N/A |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![][2]

### 다음 [요일]에 X 시간에 보내기

| 정의 |  시간대 |
| --- | --- |
| 다음 지정 요일, 선택한 시간대에 메시지를 보냅니다.  | **사용자 현지** **시간** 또는 **회사 시간** 중에서 선택 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

예를 들어 '다음 주 토요일 오후 3시 15분에 보내기'를 선택한다고 가정해 보겠습니다. 사용자가 토요일에 캔버스에 들어가면 7일 후인 다음 토요일에 해당 메시지를 받게 됩니다. 금요일에 입장하면 다음 토요일은 하루 만에 입장할 수 있습니다.

![][3]

### X일 Y시간에 보내기

| 정의 |  시간대 |
| --- | --- |
| 특정 일수에 지정된 시간에 메시지를 보냅니다. | **사용자 현지** **시간** 또는 **회사 시간** 중에서 선택 |

캔버스는 지연을 `day of the week` + `calendar days`로 계산한 다음 `time`을 추가합니다. 예를 들어 월요일 오후 9시에 캔버스 구성 요소를 보내고 다음 단계가 "1일 오전 9시에 보내기"로 예약되어 있다고 가정해 보겠습니다. 캔버스가 지연 시간을 `Monday` + `1 calendar day`로 계산한 다음 `9 am`으로 추가하기 때문에 이 메시지는 화요일 오전 9시에 전달됩니다.

![][4]

### Intelligent Timing

| 정의 | 시간대 |
| ---------- | ----- |
| [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/)은 사용자의 과거 메시지 및 앱과의 상호작용(채널별 기준)에 대한 통계 분석을 기반으로 최적의 전송 시간을 계산합니다. | **특정 시간**을 [대체]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/#fallback-options) 시간으로 선택하면 사용자 현지 시간으로 전송됩니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![][5]

## 글로벌 주파수 제한

| 정의 | 시간대 |
| --- | --- |
| 분, 일, 주(7일), 월 단위로 측정할 수 있는 특정 기간 내에 각 사용자가 캔버스를 받을 수 있는 횟수를 제한할 수 있습니다. | 사용자 현지 시간입니다. 사용자의 표준 시간대가 설정되어 있지 않으면 회사 표준 시간대로 되돌아갑니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

[빈도 제한은]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#frequency-capping) 24시간이 아닌 달력 일수를 기준으로 합니다. 즉, 하루에 한 번만 캠페인을 보내도록 빈도 제한 규칙을 설정할 수 있지만 사용자가 현지 시간으로 오후 11시에 메시지를 받더라도 한 시간 후(다음 날 자정)에 또 다른 메시지를 받을 수 있습니다.

![][6]

{% alert note %}
캔버스를 승인할 수 있는 적절한 [사용자 권한]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#managing-limited-and-team-role-permissions)이 있는 경우 워크플로에 [**요약** 단계]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/canvas_approval/#using-approvals)가 표시됩니다.
{% endalert %}


[1]: {% image_buster /assets/img_archive/schedule_delay_immediately.png %}
[2]: {% image_buster /assets/img_archive/schedule_delay_after.png %}
[3]: {% image_buster /assets/img_archive/schedule_delay_next.png %}
[4]: {% image_buster /assets/img_archive/schedule_delay_in.png %}
[5]: {% image_buster /assets/img_archive/schedule_delay_intelligent.png %}
[6]: {% image_buster /assets/img_archive/schedule_frequency_capping.png %}
