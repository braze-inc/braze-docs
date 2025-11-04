---
nav_title: Channel Filter
article_title: 인텔리전트 채널 필터
page_order: 1.5
description: "이 기사는 인텔리전트 채널 필터에 대해 다루고 있으며, 선택된 메시징 채널이 가장 적합한 채널인 오디언스의 일부를 선택하는 필터입니다. 이 경우, 최선은 사용자의 기록을 고려할 때 인게이지먼트 가능성이 가장 높은 것을 의미합니다."
search_rank: 11
---

# [![Braze 학습 과정]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/most-engaged-channel){: style="float:right;width:120px;border:0;" class="noimgborder"}인텔리전트 채널 필터

> The `Intelligent Channel` filter (previously `Most Engaged`) selects the portion of your audience for whom the selected messaging channel is their "best" channel. 

## About the Channel Filter

![The Intelligent Channel filter with a dropdown for the different channels that can be selected.]({% image_buster /assets/img/intelligent_channel_filter.png %}){: style="float:right;max-width:40%;margin-left:10px;margin-top:10px;border:0"}

이 경우, 최선은 사용자의 기록을 고려할 때 인게이지먼트 가능성이 가장 높은 채널을 의미합니다. 이메일, SMS, WhatsApp, 웹 푸시 또는 모바일 푸시(사용 가능한 모든 모바일 OS 또는 디바이스 포함)를 채널로 선택할 수 있습니다.

인텔리전트 채널은 각 사용자의 참여율을 세 개의 채널 각각에 대해 계산하는데, 이는 메시지 상호작용(열기 또는 클릭)의 비율을 지난 6개월 동안 받은 메시지 수로 나누어 산출됩니다. 사용 가능한 채널은 각각의 인게이지먼트 비율에 따라 순위가 매겨지며, 가장 높은 비율을 가진 채널이 해당 사용자의 "가장 많이 참여한 채널"입니다. 

사용자에게 메시지가 전송되거나 사용자가 메시지와 상호작용할 때마다 인게이지먼트 비율이 몇 초 내에 다시 계산됩니다. 사용자는 메시지와 상호작용한 것으로 한 번만 계산됩니다(예를 들어, 동일한 이메일에서 열기 및 클릭이 발생해도 해당 메시지는 두 번이 아닌 한 번만 상호작용한 것으로 표시됩니다). 

To enable the Intelligent Channel filter, select the **Intelligent Channel** filter on the **Target Audiences** page when creating a email, web push, or mobile push campaign.

{% alert important %}
SMS 채널의 참여율을 계산하려면 고급 추적 및 클릭 추적과 함께 [SMS 링크 단축]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/link_shortening/#overview/)을 켜세요. Without this tracking, SMS may be selected as the Intelligent Channel for a 0% engagement rate because of our [tie-breaking behavior]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_channel/#tie-breaking).
{% endalert %}

## "데이터가 충분하지 않음" 옵션

Braze가 어떤 채널이 "최고"인지 결정하려면 충분한 데이터가 필요합니다. 이는 사용자가 최소한 두 개 이상의 사용 가능한 채널에서 최소 세 개 이상의 메시지를 수신해야 함을 의미합니다. 메시지가 반드시 열려 있을 필요는 없습니다. 

사용자가 채널을 통해 충분한 메시지를 받지 못한 경우, 해당 사용자는 이 필터의 "데이터 부족" 옵션에 속하게 됩니다. 이를 통해 사용자는 세 가지 사용 가능한 메시징 채널 중 하나를 사용하여 이러한 사용자를 타겟팅할 수 있습니다.

예를 들어 푸시 메시지를 선호하는 사용자와 데이터가 충분하지 않은 사용자에게 동일한 푸시 메시지를 수신하도록 하려고 한다고 가정해 보겠습니다. 이 경우 지능형 채널 필터를 **모바일 푸시로** 설정하고 **OR을** 사용하여 **데이터 부족으로** 설정된 두 번째 지능형 채널 필터를 추가할 수 있습니다. 이메일을 선호하는 사용자를 대상으로 하는 별도의 캠페인은 인텔리전트 채널 필터를 이메일로 설정할 수 있습니다.

![Intelligent Channel filters for mobile push or not enough data.]({% image_buster /assets/img/intelligent_example.png %}){:style="border:none"}

{% alert note %}
[최대 게재빈도 설정]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#delivery-rules)을 무시하는 캠페인 및 캔버스 단계는 인텔리전트 채널에 의해 고려되지 않으며 데이터 요구 사항에 기여할 수 없습니다.
{% endalert %}

## "모바일 푸시" 옵션

모바일 푸시는 Android, iOS, Kindle 및 Braze에서 사용할 수 있는 기타 모바일 기기 채널을 통합합니다. 인텔리전트 채널을 계산할 때, Braze는 각 종류의 모바일 기기를 별도로 살펴보고, 이메일 및 웹 푸시와 비교할 때 "모바일 푸시" 카테고리를 나타내기 위해 가장 높은 참여율을 선택합니다. 

예를 들어, 사용자가 여러 대의 모바일 기기를 가지고 있는 경우, 모바일 참여율은 기기들 중 가장 높은 비율로 나타납니다. 그러나 이것이 사용자가 해당 기기에서만 푸시 알림을 받도록 강제하지는 않습니다. 이 비율은 이메일 및 웹 푸시와 비교할 때만 사용됩니다.

## 개별 채널

Braze가 사용자에게 가장 적합한 단일 채널을 선택하도록 하는 대신, 사용자가 선택한 특정 채널에서 메시지를 열 가능성이 있는지 여부에 따라 사용자를 필터링하고 싶을 수도 있습니다. For that you can use the Message Open Likelihood filter in [Segmentation filters]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#message-open-likelihood).

## 모범 사례 및 효과적인 사용 전략

### 동점자 결정

일부 사용자는 수신한 메시지 수가 적기 때문에 특정 사용자에 대해 사용 가능한 채널 전반에 걸쳐 참여율이 동점인 경우가 드물지 않습니다(예: 단일 사용자가 **이메일** 및 모바일 푸시 모두에 대해 0.2 참여율을 가짐). 이러한 경우에는 가장 최근에 열린 이벤트가 있는 채널에 우선 순위를 부여하여 동점을 해결합니다.

### 도달할 수 없는 채널

사용자가 순위를 결정할 수 있는 충분한 데이터를 가지고 있지만 가장 많이 참여한 채널에서 도달할 수 없게 되면, 사용자는 "탈락"하여 메시지를 받지 못하게 됩니다. 특정 채널에서 연락할 수 없는 사용자는 별도로 타겟팅해야 합니다.

### 오디언스 사이징

인텔리전트 채널은 메시지에 참여할 가능성이 나머지 오디언스보다 훨씬 높은 사용자 그룹을 미리 선택적으로 타겟팅할 수 있게 해줍니다. 이것은 일반적인 오디언스에서 대다수 사용자를 나타내지 않을 가능성이 큽니다. 오히려, 이 필터는 특정 채널에서 참여한 기록이 있는 일반적인 오디언스 중 5-20%를 찾을 것으로 기대할 수 있습니다.


