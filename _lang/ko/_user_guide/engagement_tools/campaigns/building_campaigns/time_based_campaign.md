---
nav_title: 캠페인을 위한 시간 기반 기능
article_title: 캠페인을 위한 시간 기반 기능
page_order: 2
tool: Campaigns
page_type: reference
description: "이 참조 문서에서는 예약 전송, Intelligent Timing 및 실행 기반 전달과 같은 캠페인의 시간 기반 기능에 대해 설명합니다."

---
# 캠페인을 위한 시간 기반 기능

> 캠페인을 사용할 때 시간 기반 예약 옵션을 사용하여 오디언스에게 도달할 수 있습니다. 이러한 시간 기반 기능에는 예약 전송으로 설정된 캠페인과 액션 기반 전송이 포함됩니다.

{% alert tip %}
캠페인 전달에 대한 자세한 내용은 [캠페인 설정](https://learning.braze.com/campaign-setup-delivery-targeting-conversions) 브레이즈 학습 과정을 확인하세요.
{% endalert %}

## 예약 배송

이 섹션에서는 [예약된 배달]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/scheduled_delivery/) 캠페인의 시간 기반 예약 및 배달 옵션에 대해 설명합니다.

### 지정한 시간에 발송

| 정의 | 시간대 |
| ---------- | --------- |
| 특정 달력 날짜에 지정된 시간에 메시지를 보냅니다. | 회사 표준 시간대. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

!["지정된 시간에 보내기" 옵션을 선택한 캠페인은 2021년 7월 13일 오전 9시부터 한 번만 보내도록 설정되어 있습니다.][2]

### Intelligent Timing

| 정의 | 시간대 |
| ---------- | --------- |
| 사용자의 최적 시간. 각 사용자는 참여 가능성이 가장 높은 시간에 캠페인을 받게 됩니다. 자세히 알아보려면 [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/)을 확인하세요. | 특정 시간을 [대체]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/#fallback-options) 시간으로 선택하면 사용자 현지 시간으로 전송됩니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

!["Intelligent Timing" 옵션을 선택한 캠페인은 프로필에 최적의 시간을 계산할 수 있는 데이터가 충분하지 않은 사용자를 위해 2021년 7월 13일 오전 9시를 사용자 지정 대체 시간으로 설정하여 최적의 시간에 한 번 전송하도록 설정했습니다.][3]

### 현지 시간대의 사용자에게 캠페인 보내기

| 정의 | 시간대 |
| ---------- | --------- |
| 사용자의 [개별 시간대]({{site.baseurl}}/user_guide/engagement_tools/campaigns/faq/#when-does-braze-evaluate-users-for-local-time-zone-delivery)를 기준으로 세그먼트에 메시지를 전달할 수 있습니다. | 사용자 현지 시간입니다. 사용자의 표준 시간대가 설정되어 있지 않으면 회사 표준 시간대로 되돌아갑니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

!["지정된 시간에 보내기" 옵션이 선택된 캠페인은 2021년 7월 13일 오전 9시부터 "현지 시간대의 사용자에게 캠페인 보내기" 확인란을 선택하여 한 번 전송합니다.][4]

### 사용자에게 캠페인을 수신할 수 있는 자격을 다시 부여

| 정의 | 시간대 |
| ---------- | --------- |
| 사용자가 이 캠페인에서 메시지를 받은 후 언제 다시 캠페인을 받을 수 있는 자격이 주어질지 지정합니다. [자세히 알아보기]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/). | N/A |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![일주일 후 "사용자가 캠페인을 다시 받을 수 있도록 허용" 확인란이 선택된 캠페인입니다.][5]

## 액션 기반 전달

이 섹션에서는 [액션 기반 배달]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/) 캠페인의 일정 지연 및 배달 옵션에 대해 설명합니다.

### 일정 지연

{% alert important %}
지연 시간을 선택할 때 [캠페인 기간보다]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/#step-4-assign-duration) 긴 지연 시간을 설정하면 사용자가 캠페인을 수신하지 못한다는 점에 유의하세요.
{% endalert %}

#### 즉시 캠페인 보내기

| 정의 | 시간대 |
| ---------- | --------- |
| 사용자가 트리거 동작을 수행한 후 즉시 메시지를 보냅니다. | N/A |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![트리거 이벤트 발생 후 즉시 캠페인을 전송하도록 설정한 일정 지연입니다.][6]

#### X일 후 캠페인 보내기

| 정의 | 시간대 |
| ---------- | --------- |
| 잠시 후 메시지를 보냅니다. 지연 시간을 초, 분, 시간, 일 또는 주 단위로 지정할 수 있습니다. [인앱 메시지 캠페인의]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/about) 경우 최대 2시간까지만 지연을 설정할 수 있습니다. | N/A |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![트리거 이벤트 발생 후 하루 후에 캠페인을 보내도록 설정한 일정 지연입니다.][7]

#### 다음 [요일] X 시간에 캠페인 보내기

| 정의 | 시간대 |
| ---------- | --------- |
| 다음 지정 요일, 선택한 시간대에 메시지를 보냅니다. | **사용자 현지** **시간** 또는 **회사 시간** 중에서 선택 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

예를 들어 '다음 주 토요일 오후 3시 15분에 보내기'를 선택한다고 가정해 보겠습니다. 사용자가 토요일에 트리거 이벤트를 수행하면 7일 후인 다음 토요일에 해당 메시지를 받게 됩니다. 금요일에 입장하면 다음 토요일은 하루 만에 입장할 수 있습니다.

![][8]

#### X일 Y시간에 보내기

| 정의 | 시간대 |
| ---------- | --------- |
| 특정 일수에 지정된 시간에 메시지를 보냅니다. | **사용자 현지** 시간 또는 **회사 시간** 중에서 선택 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Braze는 지연을 `day of the week` + `calendar days`로 계산한 다음 `time`을 추가합니다. 예를 들어 사용자가 월요일 오후 9시에 트리거 이벤트를 수행하고 일정 지연이 "1일 후 오전 9시에 캠페인 보내기"로 설정되어 있다고 가정해 보겠습니다. Braze는 지연 시간을 `Monday` + `1 calendar day`로 계산한 다음 `9 am`으로 추가하기 때문에 이 메시지는 화요일 오전 9시에 전달됩니다.

![][9]

### 방해금지 시간

| 정의 | 시간대 |
| ---------- | --------- |
| 지정된 시간 동안 메시지가 전송되지 않도록 설정합니다. 방해금지 시간 동안 메시지가 트리거되는 경우, 메시지를 취소하거나 다음 사용 가능한 시간(예: 방해금지 시간이 끝날 때 보내는 것)에 보낼지 선택할 수 있습니다. | 사용자 현지 시간입니다. 사용자의 표준 시간대가 설정되어 있지 않으면 회사 표준 시간대로 되돌아갑니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![방해금지 시간을 활성화한 캠페인입니다. 이 예에서는 사용자 현지 시간으로 밤 12시부터 오전 8시 사이에는 메시지가 전송되지 않습니다. 방해금지 시간 중에 메시지가 트리거되면 다음 사용 가능한 시간에 메시지가 전송됩니다.][10]

### 사용자가 캠페인을 다시 받을 수 있도록 허용하기

| 정의 | 시간대 |
| ---------- | --------- |
| 사용자가 이 캠페인에서 메시지를 받은 후 언제 다시 캠페인을 받을 수 있는 [자격]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/#campaigns)이 주어질지 지정합니다. | N/A |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![일주일 후 "사용자가 캠페인을 다시 받을 수 있도록 허용" 확인란이 선택된 캠페인입니다.][5]

### 글로벌 주파수 제한

| 정의 | 시간대 |
| ---------- | --------- |
| 분, 일, 주(7일), 월 단위로 측정할 수 있는 특정 기간 내에 각 사용자가 캠페인을 수신할 수 있는 횟수를 제한합니다. 자세한 내용은 [최대 게재빈도 설정]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#frequency-capping)을 참조하세요. | 사용자 현지 시간입니다. 사용자의 표준 시간대가 설정되어 있지 않으면 회사 표준 시간대로 되돌아갑니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

기본적으로 새 캔버스의 경우 최대 게재빈도 설정은 꺼져 있습니다. 주파수 제한은 캔버스 엔트리 레벨이 아닌 스텝 레벨에서 적용됩니다.

빈도 제한은 24시간이 아닌 달력 일수를 기준으로 합니다. 즉, 하루에 한 번만 캠페인을 보내도록 빈도 제한 규칙을 설정할 수 있지만 사용자가 현지 시간으로 오후 11시에 메시지를 받더라도 한 시간 후(다음 날 자정)에 또 다른 메시지를 받을 수 있습니다. 

## 전환 기한

| 정의 | 시간대 |
| ---------- | --------- |
| 사용자의 전환 여부를 판정함에 있어 사용자가 캠페인을 수신한 시점과 할당된 행동을 수행한 시점 사이에 최대 경과 시간입니다. For more information, refer to [conversion events]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events/). | N/A |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }



[2]: {% image_buster /assets/img_archive/time_designated.png %}
[3]: {% image_buster /assets/img_archive/time_intelligent_timing.png %}
[4]: {% image_buster /assets/img_archive/time_local.png %}
[5]: {% image_buster /assets/img_archive/time_reeligibility.png %}
[6]: {% image_buster /assets/img_archive/time_delay_immediately.png %}
[7]: {% image_buster /assets/img_archive/time_delay_after.png %}
[8]: {% image_buster /assets/img_archive/time_delay_on_the_next.png %}
[9]: {% image_buster /assets/img_archive/time_delay_in.png %}
[10]: {% image_buster /assets/img_archive/time_quiet_hours.png %}
