---
nav_title: 채널 필터
article_title: Intelligent Channel 필터
page_order: 1.5
description: "이 문서는 선택한 메시지 채널이 해당 사용자에게 '최고' 채널인 오디언스 일부를 선택하는 Intelligent Channel 필터를 설명합니다. 여기서 '최고'는 사용자 이력 기준 상호작용 가능성이 가장 높은 채널을 의미합니다."
search_rank: 11
---

# [![Braze Learning 과정]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/most-engaged-channel){: style="float:right;width:120px;border:0;" class="noimgborder"}Intelligent Channel 필터

> **Intelligent Channel** 필터(이전 **Most Engaged**)는 선택한 메시지 채널이 해당 사용자에게 "최고" 채널인 오디언스 일부를 선택합니다.

## 채널 필터 정보

![선택 가능한 다양한 채널이 있는 Intelligent Channel 필터 드롭다운.]({% image_buster /assets/img/intelligent_channel_filter.png %}){: style="float:right;max-width:40%;margin-left:10px;margin-top:10px;border:0"}

여기서 "최고"는 사용자 이력 기준 상호작용 가능성이 가장 높은 채널을 의미합니다. 이메일, SMS, WhatsApp, 웹 푸시 또는 모바일 푸시(사용 가능한 모든 모바일 OS/기기 포함)를 채널로 선택할 수 있습니다.

Intelligent Channel은 최근 6개월 동안 메시지 상호작용(열기 또는 클릭) 수를 수신한 메시지 수로 나눈 비율로 사용자·채널별 상호작용률을 계산합니다. 채널은 상호작용률로 순위가 매겨지며, 가장 높은 비율의 채널이 해당 사용자의 "Most Engaged"입니다.

사용자에게 메시지가 전송되거나 사용자가 메시지와 상호작용할 때마다 상호작용률이 몇 초 내에 재계산됩니다. 한 메시지에 대한 상호작용은 한 번만 집계됩니다(예: 같은 이메일 열기 및 클릭은 한 번의 상호작용).

Intelligent Channel 필터를 사용하려면 이메일, 웹 푸시 또는 모바일 푸시 캠페인 생성 시 **대상 오디언스** 페이지에서 **Intelligent Channel** 필터를 선택합니다.

{% alert important %}
SMS 채널 상호작용률 계산을 위해 [SMS 링크 단축]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/link_shortening/)과 고급 추적 및 클릭 추적을 활성화하세요. 이 추적 없이는 [동점 처리 동작]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_channel/#tie-breaking) 때문에 SMS가 0% 상호작용률로 Intelligent Channel로 선택될 수 있습니다.
{% endalert %}

## "데이터 부족" 옵션

Braze가 "최고" 채널을 판단하려면 충분한 데이터가 필요합니다. 사용자는 사용 가능한 세 채널 중 최소 두 채널에서 채널당 최소 3통의 메시지를 받아야 합니다(열기 여부는 불필요).

채널별로 충분한 메시지를 받지 못한 사용자는 이 필터의 "데이터 부족" 옵션에 포함됩니다. 이러한 사용자에게는 세 채널 중 아무 채널이나 사용할 수 있습니다.

예: 푸시를 선호하는 사용자에게 푸시를 보내고, 데이터가 부족한 사용자에게도 같은 푸시를 보내려면 Intelligent Channel 필터를 **모바일 푸시** 로 설정하고 **OR** 로 **데이터 부족** 이 설정된 두 번째 Intelligent Channel 필터를 추가합니다. Intelligent Channel 필터가 **이메일** 로 설정된 별도 캠페인으로 이메일을 선호하는 사용자에게 도달할 수 있습니다.

![모바일 푸시 또는 데이터 부족용 Intelligent Channel 필터.]({% image_buster /assets/img/intelligent_example.png %}){:style="border:none"}

{% alert note %}
[최대 게재빈도 설정]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#delivery-rules)을 무시하는 캠페인 및 Canvas 단계는 Intelligent Channel에서 제외되며 데이터 요건을 충족하지 않습니다.
{% endalert %}

동점 처리, 도달 불가 채널, 오디언스 크기에 대한 모범 사례는 왼쪽 목차 또는 Braze 대시보드 도움말의 전체 문서를 참조하세요.
