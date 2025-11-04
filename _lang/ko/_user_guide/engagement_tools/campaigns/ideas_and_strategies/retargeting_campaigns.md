---
nav_title: 리타겟팅 캠페인
article_title: 리타겟팅 캠페인
page_order: 2
page_type: reference
description: "이 참조 문서에서는 사용자가 수신한 메시지를 기반으로 캠페인을 리타겟팅하는 방법과 그 이유를 설명합니다."
tool:
  - Campaigns
  
---

# 리타겟팅 캠페인

> 이메일 열람 여부와 같은 사용자의 이전 행동을 기반으로 캠페인을 리타겟팅하면 사용자를 재분류하여 효과적인 데이터 기반 마케팅 접근 방식의 문을 열 수 있습니다.

Braze는 사용자가 수신한 메시지를 기반으로 리타겟팅하는 기능을 지원합니다. You can retarget users based upon their interactions with your campaigns and Canvases. 

이러한 각 리타겟팅 필터는 추가한 후 몇 가지 옵션을 제공합니다. 사용자 타겟팅에 대한 자세한 내용은 캠페인 설정에 대한 [Braze 학습 과정](https://learning.braze.com/campaign-setup-delivery-targeting-conversions)을 확인하세요!

![Segment Details section with the dropdown menu for the available filters.]({% image_buster /assets/img_archive/retarget.png %}){: style="max-width:80%;"}

## 리타겟팅 필터

You can use the retargeting filters in this section for your users within your campaigns and Canvases.

### 캠페인 클릭/열람

이 필터를 사용하여 사용자와 그렇지 않은 사용자를 찾을 수 있습니다.

- 이메일 클릭
- 인앱 메시지 클릭
- 푸시 알림 바로 열기
- 이메일 열람함
- 인앱 메시지 보기

![]({% image_buster /assets/img_archive/clickedopened.png %})

리타겟팅할 캠페인을 선택하여 추가로 지정할 수 있습니다.

### 태그가 있는 캠페인 또는 캔버스를 클릭하거나 열었습니다.

이 필터를 사용하여 특정 태그가 있는 캠페인 또는 캔버스와 상호작용한 적이 있거나 그렇지 않은 사용자를 찾을 수 있습니다:

- 이메일 클릭
- 인앱 메시지 클릭
- 푸시 알림 바로 열기
- 이메일 열람함
- 인앱 메시지 보기

![]({% image_buster /assets/img_archive/retarget_tag_filter.png %})

### 캠페인에서 전환됨 

이 필터를 사용하여 타겟 캠페인에서 전환한 사용자와 전환하지 않은 사용자(주요 전환 기준)를 찾을 수 있습니다. 

반복 캠페인의 경우, 이 필터는 사용자가 캠페인의 가장 최근 메시지에서 전환했는지 여부를 나타냅니다.

![]({% image_buster /assets/img_archive/converted_from_campaign.png %})

### 캔버스에서 전환됨 

이 필터를 사용하여 대상 캔버스에서 전환한 사용자와 전환하지 않은 사용자(주요 전환 기준)를 찾을 수 있습니다.

반복 캔버스의 경우 이 필터는 사용자가 캔버스를 통과할 때마다 전환한 적이 있는지 여부를 나타냅니다.

![]({% image_buster /assets/img_archive/converted_from_canvas.png %})

### 캠페인 대조군에 속함 

이 필터를 사용하여 타겟 캠페인의 제어 그룹에 속하거나 속하지 않은 사용자를 찾을 수 있습니다.

![]({% image_buster /assets/img_archive/campaign_control_group.png %})

### 캔버스 대조군에 속함 

이 필터를 사용하여 드롭다운에서 선택할 수 있는 대상 캔버스의 제어 그룹에 속하거나 속하지 않은 사용자를 찾을 수 있습니다.

![]({% image_buster /assets/img_archive/canvas_control_group.png %})

### 특정 캠페인에서 마지막으로 수신한 메시지 

이 필터를 사용하여 지정된 날짜 또는 일수 전후에 특정 캠페인을 마지막으로 수신한 사용자를 찾을 수 있습니다. 이 필터는 사용자가 다른 캠페인을 수신한 시기는 고려하지 않습니다.

![]({% image_buster /assets/img_archive/last_received_specific_campaign.png %})

### 특정 캠페인 또는 태그가 포함된 캔버스에서 마지막으로 수신한 메시지 

이 필터를 사용하면 지정된 날짜 또는 일수 전후에 특정 캠페인이나 특정 태그가 포함된 캔버스를 마지막으로 수신한 사용자를 찾을 수 있습니다. 이 필터는 사용자가 다른 캠페인이나 캔버스를 수신한 시기는 고려하지 않습니다.

![]({% image_buster /assets/img_archive/last_received_campaign_with_tag.png %})

### 캠페인에서 메시지 수신 

이 필터를 사용하여 타겟 캠페인을 수신했거나 수신하지 않은 사용자를 찾을 수 있습니다.

![]({% image_buster /assets/img_archive/receivedcamp.png %})

### 캠페인 또는 캔버스에서 태그가 포함된 메시지 수신 

이 필터를 사용하여 타겟 태그가 있는 캠페인이나 캔버스를 수신했거나 수신하지 않은 사용자를 찾을 수 있습니다.

![]({% image_buster /assets/img_archive/received_campaign_with_tag.png %})

## 리타겟팅 캠페인의 장점

리타겟팅은 원래 세그먼트에 사용자가 수행하기를 원하는 특정 액션이 포함되어 있는 경우 특히 효과적입니다. 예를 들어 구매 경험이 없는 사용자를 대상으로 하는 카드가 있다고 가정해 보겠습니다. 이 카드는 인앱 구매 할인 프로모션을 광고합니다. 초기 세그먼트는 다음과 같습니다:

- 앱에서 지출한 금액은 정확히 0원
- 마지막으로 사용한 앱이 14일 미만

The total number of users in the segment is 100,000 and you know from the Content Card stats that 60,000 unique users viewed the card and 20,000 unique users clicked the card. 세그먼트 분석기를 통해 카드를 클릭한 사용자 중 실제로 구매를 한 사용자 수를 확인할 수 있습니다:

- 앱에서 지출한 금액이 0보다 큼
- 클릭한 카드가 카드 이름입니다.

이러한 통계를 검토한 후 카드를 클릭했지만 구매를 하지 않은 사용자 세그먼트를 만들 수 있습니다:

- 앱에서 지출한 금액이 정확히 0보다 작습니다
- 클릭한 카드가 카드 이름입니다.

프로모션 또는 다른 인앱 구매에 대한 추가 메시지로 이 세그먼트를 리타겟팅할 수 있습니다. Retargeting can be done with a messaging campaign. 멀티채널 접근 방식을 사용하면 사용자가 가장 반응할 가능성이 높은 곳에 도달할 수 있으므로 캠페인의 효과를 높일 수 있습니다.

