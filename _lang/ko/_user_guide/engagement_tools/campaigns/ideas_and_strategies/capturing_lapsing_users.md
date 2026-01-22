---
nav_title: 소멸하는 사용자를 포착하기
article_title: 소멸하는 사용자 포착하기
page_order: 1
page_type: tutorial
description: "이 사용법 기사는 소멸하는 사용자 문제와 이러한 사용자를 다시 참여시키기 위해 Braze 캠페인을 효과적으로 사용하는 방법을 다룹니다."
tool:
  - Segments
  - Campaigns

---

# 소멸하는 사용자를 포착하기

> 청중이 줄어들고 있다면, 그들을 다시 유혹하는 것이 중요합니다. Braze를 사용하면 소멸하는 사용자를 포착하기 위해 자동화된 반복 재참여 캠페인을 설정할 수 있습니다. 재참여 시간대와 반복 주기를 앱에 가장 적합한 것으로 선택할 수 있지만, 시연을 위해 14일 재참여 계획으로 시작하겠습니다.

사용자 타겟팅에 대한 자세한 내용은 캠페인 설정에 대한 [Braze 학습 과정](https://learning.braze.com/campaign-setup-delivery-targeting-conversions)을 확인하세요!

## 1단계: 사용자 세분화

먼저, 지난 2주 동안 앱을 사용하지 않은 사용자를 타겟팅하기 위해 다음 필터를 사용하여 세그먼트를 생성하겠습니다:

- **마지막 사용 앱** 2주 이상 전
- **마지막 사용 앱** 3주 미만 전

\![]({% image_buster /assets/img_archive/2weeklapse1.png %}){: style="max-width:70%;"}

세그먼트에 "소멸된 사용자 - 2주"와 같은 기억하기 쉬운 이름을 붙입니다. 우리가 캠페인을 주간으로 반복하도록 설정하고 있기 때문에, 세그먼트에 최소한 1주일의 사용자가 포함되어 있는지 확인하고 싶습니다. 그래서 우리는 2주에서 3주 사이에 마지막으로 앱을 사용한 사용자를 선택했습니다.

## 2단계: 캠페인 만들기

다음으로, **캠페인 만들기**를 클릭하고 이 세그먼트에 보낼 캠페인 유형을 선택합니다. 이 예에서는 새로운 [푸시 캠페인]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message)을 만들겠습니다.

\![]({% image_buster /assets/img_archive/2weeklapse2.png %}){: style="max-width:70%;"}

캠페인 이름을 "소멸된 사용자에게 보내는 메시지 - 2주"로 정하고 메시지 내용을 생성하겠습니다. 이 예제에서는 iOS 사용자만 타겟팅할 것이지만, Android 및 iOS 푸시 알림에 Braze를 사용할 수 있습니다. 

사용자가 앱에 마지막으로 있었던 시간에 가까울수록 주제와 관련성이 중요해집니다. 사용자가 앱을 사용하지 않은 지 2주 후에 메시지를 보낼 때는 관련 콘텐츠를 제공하고 앱 사용의 이점을 강조하는 것이 중요합니다.

\![]({% image_buster /assets/img_archive/2weeklapse3.png %}){: style="max-width:70%;"}

다음으로, [현지 시간대 배달]({{site.baseurl}}/help/faqs/#what-does-local-time-zone-delivery-offer)을 사용하여 매주 목요일 오후 5시 45분에 메시지를 보내는 반복 일정을 생성할 것입니다 **시간 기반 예약 옵션** . 사용자가 사용량이 많은 기간 직전에 타겟팅할 수 있도록 세션 그래프를 확인하는 것이 좋습니다. 이것은 사람들이 앱을 사용할 가능성이 가장 높은 시점에 재참여를 시도하도록 보장합니다. 이것은 나중에 변경할 수 있으며 초기 가설을 테스트할 수 있습니다.

\![]({% image_buster /assets/img_archive/2weeklapse4.png %}){: style="max-width:70%;"}

## 3단계: 캠페인 시작

이제 캠페인을 보낼 준비가 되었습니다. 작곡가의 마지막 페이지에서 설정을 확인하고 **캠페인 시작**을 클릭하세요!

