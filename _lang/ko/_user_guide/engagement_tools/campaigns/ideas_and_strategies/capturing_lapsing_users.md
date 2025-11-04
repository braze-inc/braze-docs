---
nav_title: 휴면 사용자 캡처
article_title: 휴면 사용자 캡처
page_order: 1
page_type: tutorial
description: "이 도움말 문서에서는 휴면 사용자 문제와 이러한 사용자의 재참여를 위해 Braze 캠페인을 효과적으로 사용하는 방법에 대해 설명합니다."
tool:
  - Segments
  - Campaigns

---

# 휴면 사용자 캡처

> 잠재고객이 줄어들고 있다면 이들을 다시 끌어들이는 것이 중요합니다. Braze를 사용하면 자동화된 반복 재참여 캠페인을 설정하여 휴면 사용자를 확보할 수 있습니다. 앱에 가장 적합한 재참여 기간과 반복 횟수를 선택할 수 있지만, 데모를 위해 14일 리인게이지먼트 플랜으로 시작하겠습니다.

사용자 타겟팅에 대한 자세한 내용은 캠페인 설정에 대한 [Braze 학습 과정](https://learning.braze.com/campaign-setup-delivery-targeting-conversions)을 확인하세요!

## 1단계: 사용자 세분화

먼저 다음 필터를 사용하여 지난 2주간 앱을 사용하지 않은 사용자를 타겟팅하는 세그먼트를 생성합니다.

- 2주 이상 전에 **마지막으로 사용한 앱** 
- **마지막으로 사용한 앱이** 3주 미만

![]({% image_buster /assets/img_archive/2weeklapse1.png %}){: style="max-width:70%;"}

세그먼트의 이름은 "경과된 사용자 - 2주"와 같이 기억에 남는 이름을 지정합니다. 매주 반복되도록 캠페인을 설정하고 있으므로 세그먼트에서 최소 1주일 동안 캡처된 사용자가 있는지 확인해야 합니다. 그렇기 때문에 2~3주 전에 마지막으로 앱을 사용한 사용자를 선정했습니다.

## 2단계: 캠페인 만들기

Next, click **Create Campaign** and choose the type of campaign we will be sending to this segment. in this example, we'll create a new [push campaign]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message).

![]({% image_buster /assets/img_archive/2weeklapse2.png %}){: style="max-width:70%;"}

캠페인의 이름을 "휴면 사용자에게 보내는 메시지 - 2주"로 정한 다음 메시지 내용을 작성합니다. 이 예에서는 iOS 사용자만 타겟팅하지만, Android 및 iOS 푸시 알림에 Braze를 사용할 수 있습니다. 

사용자가 앱을 마지막으로 사용한 시간이 가까울수록 화제성과 연관성이 더 중요합니다. 2주 동안 앱을 사용하지 않은 사용자에게 메시지를 보낼 때는 관련 콘텐츠를 노출하고 앱 사용의 이점을 강조하는 것이 중요합니다.

![]({% image_buster /assets/img_archive/2weeklapse3.png %}){: style="max-width:70%;"}

Next, we'll create a recurring schedule to send our weekly message on Thursdays at 5:45 pm using [local time zone delivery]({{site.baseurl}}/help/faqs/#what-does-local-time-zone-delivery-offer) in **Time-Based Scheduling Options**. 사용량이 많은 기간 직전에 세션 그래프를 확인하여 사용자를 타겟팅하는 것이 좋습니다. 이렇게 하면 사람들이 앱을 사용할 가능성이 가장 높을 때 재참여를 유도할 수 있습니다. 나중에 이를 변경하여 초기 가설을 테스트할 수 있습니다.

![]({% image_buster /assets/img_archive/2weeklapse4.png %}){: style="max-width:70%;"}

## 3단계: 캠페인 시작

이제 캠페인을 보낼 준비가 되었습니다. 작성기의 마지막 페이지에서 설정을 확인하고 **캠페인 시작**을 클릭합니다!

