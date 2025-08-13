---
nav_title: 채널별 메시지 작성
article_title: 채널별 메시지 작성
page_order: 5
layout: dev_guide

guide_top_header: "채널별 메시지 작성"
guide_top_text: "메시징 채널은 휴대폰이나 웹 브라우저의 푸시 알림, 이메일, 인앱 메시지 등을 통해 고객과 가상으로 소통할 수 있는 방법입니다! 이러한 채널에 대해 자세히 알아보고 Braze에서 해당 채널을 활용하는 방법을 알아보려면 다음 섹션을 참조하세요. 또는 <a href='https://learning.braze.com/series/messaging-channels' target='_blank'>메시징 채널에서</a> Braze 학습 과정을 확인해 보세요!<br><br>Braze를 사용하여 각 채널에서 접근성 높은 메시지 캠페인을 만들 수 있습니다. 엔지니어와 협력하여 구현 시 접근성 표준을 충족하는지 확인하세요."
description: "이 랜딩 페이지는 Braze 메시징 채널을 다룹니다. 메시징 채널은 휴대폰이나 웹 브라우저의 푸시 알림, 이메일, 인앱 메시지 등을 통해 고객과 가상으로 소통할 수 있는 방법입니다!"

guide_featured_title: "사용 가능한 채널"
guide_featured_list:
- name: Banners
  link: /docs/user_guide/message_building_by_channel/banners/
  image: /assets/img/braze_icons/table.svg
- name: 콘텐츠 카드
  link: /docs/user_guide/message_building_by_channel/content_cards/
  image: /assets/img/braze_icons/table.svg
- name: 이메일 메시징
  link: /docs/user_guide/message_building_by_channel/email/
  image: /assets/img/braze_icons/mail-01.svg
- name: "인앱 메시징"
  link: /docs/user_guide/message_building_by_channel/in-app_messages/
  image: /assets/img/braze_icons/annotation-dots.svg
- name: 푸시 메시징
  link: /docs/user_guide/message_building_by_channel/push/
  image: /assets/img/braze_icons/marker-pin-01.svg
- name: "SMS, MMS, and RCS"
  link: /docs/user_guide/message_building_by_channel/sms_mms_rcs/
  image: /assets/img/braze_icons/message-text-circle-01.svg
- name: 웹훅
  link: /docs/user_guide/message_building_by_channel/webhooks/
  image: /assets/img/braze_icons/brackets.svg
- name: WhatsApp
  link: /docs/user_guide/message_building_by_channel/whatsapp/
  image: /assets/img/braze_icons/whatsapp.svg
---

## Accessibility resources

Braze를 사용하여 각 채널에서 접근성 높은 메시지 캠페인을 만들 수 있습니다. 엔지니어와 협력하여 구현 시 접근성 표준을 충족하는지 확인하세요. If you’d like additional guidance, we recommend:

- [Accessible Messaging Foundations](https://learning.braze.com/accessible-messaging-foundations): Learn fundamental accessibility principles that apply to brand communications in this Braze Learning course.
- [Building Accessible Messages]({{site.baseurl}}/help/accessibility/): Learn how to add alt text and structure your content for assistive technologies directly within Braze.

{% multi_lang_include accessibility/feedback.md %}

## 메시지 채널 선택하기

캠페인과 캔버스에 가장 적합한 메시지 채널을 결정할 때는 항상 메시지의 콘텐츠와 긴급성을 고려하세요:

- **콘텐츠**는 메시지가 시각적으로 얼마나 매력적인지를 나타냅니다. 사본에 멀티미디어 및 기타 자산을 추가하여 콘텐츠를 더욱 풍성하게 만들 수 있습니다.
- **긴급성**은 메시지가 얼마나 빨리 사용자에게 알리고 관심을 끌 수 있는지를 측정하는 척도입니다. 사용자가 즉시 확인할 수 있는 알림은 긴급성이 높은 반면, 사용자가 앱에 로그인해야 하는 메시지는 긴급성이 낮습니다.

다음 표는 콘텐츠 및 긴급성 측면에서 주요 메시징 채널의 강점과 약점을 보여줍니다. 메시지가 얼마나 긴급하고 콘텐츠가 풍부해야 하는지 항상 고려한 다음 캠페인에 적합한 채널을 선택하세요.

![모바일/웹 푸시는 단순 콘텐츠, 높은 긴급성, 이메일은 리치 콘텐츠, 높은 긴급성, 인앱/브라우저 메시지는 단순 콘텐츠, 낮은 긴급성, 콘텐츠 카드는 낮은 긴급성, 리치 콘텐츠]({% image_buster /assets/img_archive/messaging_matrix.png %})

이 매트릭스를 활용하는 방법에 대해 자세히 알아보려면 [메시징 매트릭스 이해에](https://learning.braze.com/understand-the-messaging-matrix) 대한 Braze 학습 과정을 확인하세요.

<br><br>
