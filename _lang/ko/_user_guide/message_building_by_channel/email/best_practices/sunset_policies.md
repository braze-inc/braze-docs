---
nav_title: 일몰 정책
article_title: 이메일 일몰 정책
page_order: 8
page_type: reference
description: "이 도움말에서는 일몰 정책과 관련된 모범 사례와 참여하지 않는 사용자에게 메시지를 중단하는 것이 더 나은 상황을 이해하는 방법에 대해 설명합니다."
channel: email

---

# 일몰 정책

> 최대한 많은 사용자에게 캠페인을 보내고 싶을 수도 있지만, 실제로는 참여하지 않는 사용자에게 메시지를 보내는 것을 중단하는 것이 유리한 경우가 있습니다. 

이메일의 경우 발신 IP에는 참여도, 스팸 신고, 차단 목록 등을 고려한 평판 점수가 있습니다. You can use tools like [Sender Score](https://www.senderscore.org/) or [Outlook's Smart Network Data Service](https://postmaster.live.com/snds/) to monitor your reputation score. 평판 점수가 지속적으로 낮으면 ISP 및 사서함 필터가 참여 중인 수신자를 포함하여 모든 수신자에 대해 자동으로 이메일을 스팸 또는 우선순위가 낮은 폴더로 분류할 수 있습니다. 일몰 정책을 만들면 활성 수신자에게만 이메일을 전송하는 데 도움이 됩니다. 

세분화 필터를 사용하면 이메일, 푸시 및 인앱 알림에 대한 일몰 정책을 쉽게 구현하여 메시지가 스팸으로 표시되는 것을 방지할 수 있습니다. 다음은 일몰 정책을 만들 때 고려해야 할 몇 가지 사항입니다:

- 무엇이 '참여하지 않는' 사용자로 간주되나요? 
- 인게이지먼트는 클릭, 구매, 앱 사용 또는 이러한 행동의 조합으로 정의되나요? 
- 메시지 전송을 중단하려면 얼마나 오래 참여하지 않아야 하나요?
- 세그먼트에서 제외하기 전에 사용자에게 특별한 캠페인을 제공하나요?
- 어떤 메시징 채널에 일몰 정책이 적용되나요? 

For example, if you have users who opt in to [Apple's Mail Privacy Protection (MPP)]({{site.baseurl}}/user_guide/message_building_by_channel/email/apple_mail/mpp/), consider how this may impact your email campaigns and deliverability metrics and determine how to best structure your sunset policy.

To incorporate sunset policies into your campaigns, create a [segment]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#creating-a-segment) that automatically excludes users who have marked your emails as spam or have not interacted with a your messages for a certain period of time.  

To set up these segments, choose the `Has Marked You As Spam` and `Last Engaged With Message` filters located under the **Retargeting** section in the filter dropdown. 

`Last Engaged With Message` 필터를 적용할 때는 사용자가 상호 작용했거나 하지 않은 메시징 유형(푸시, 이메일 또는 인앱 알림)과 사용자가 마지막으로 상호 작용한 후 경과한 일수를 지정합니다. 세그먼트를 만든 후 이 세그먼트를 [메시징 채널]({{site.baseurl}}/user_guide/message_building_by_channel/)로 타겟팅하도록 선택합니다.

![Segment Details page with the filter "Last Engaged with Message" selected.]({% image_buster /assets/img_archive/email_sunset_policies_new.png %})

Braze는 스팸으로 표시한 사용자에게 자동으로 이메일 전송을 중지하지만, `Has Marked You As Spam` 필터를 사용하면 이러한 사용자에게 타겟팅된 푸시 메시지와 인앱 알림을 보낼 수도 있습니다. This filter is useful for [retargeting campaigns]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/retargeting_campaigns/#retargeting-campaigns). 예를 들어, 참여하지 않는 사용자에게 이메일을 열람하지 않을 때 놓치고 있는 기능 및 할인을 상기시키는 메시지를 보낼 수 있습니다.

일몰 정책은 휴면 사용자를 대상으로 하는 이메일 캠페인에 특히 유용할 수 있습니다. 이러한 캠페인은 일정 기간 동안 앱과 상호 작용하지 않은 세그먼트에 초점을 맞추지만, 참여하지 않은 수신자를 반복적으로 포함할 경우 이메일의 전달 가능성을 위험에 빠뜨릴 수 있습니다. 일몰 정책을 사용하면 휴면 사용자를 스팸 폴더에 넣지 않고 타겟팅할 수 있습니다.

