---
nav_title: 채널별 메시지 작성
article_title: 채널별 메시지 작성
page_order: 5
layout: dev_guide

guide_top_header: "채널별 메시지 작성"
guide_top_text: "메시징 채널은 푸시 알림, 이메일, 앱 내 메시지 등을 통해 고객과 가상으로 소통할 수 있는 방법입니다. 이 채널에 대해 더 배우고 Braze와 함께 활용하는 방법을 알고 싶다면, 아래 나열된 섹션을 확인하세요. 또는 <a href='https://learning.braze.com/series/messaging-channels' target='_blank'>메시징 채널</a>에 대한 Braze 학습 과정을 확인하세요!<br><br>Braze를 사용하여 각 채널에서 접근 가능한 메시징 캠페인을 만들 수 있습니다. 엔지니어와 협력하여 구현에서 접근성 기준을 충족하는지 확인하세요."
description: "이 랜딩 페이지는 Braze 메시징 채널을 다룹니다. 메시징 채널은 푸시 알림, 이메일, 앱 내 메시지 등을 통해 고객과 가상으로 소통할 수 있는 방법입니다."

guide_featured_title: "사용 가능한 채널"
guide_featured_list:
- name: 배너
  link: /docs/user_guide/message_building_by_channel/banners/
  image: /assets/img/braze_icons/table.svg
- name: 콘텐츠 카드
  link: /docs/user_guide/message_building_by_channel/content_cards/
  image: /assets/img/braze_icons/table.svg
- name: 이메일 메시징
  link: /docs/user_guide/message_building_by_channel/email/
  image: /assets/img/braze_icons/mail-01.svg
- name: "앱 내 메시징"
  link: /docs/user_guide/message_building_by_channel/in-app_messages/
  image: /assets/img/braze_icons/annotation-dots.svg
- name: 푸시 메시징
  link: /docs/user_guide/message_building_by_channel/push/
  image: /assets/img/braze_icons/marker-pin-01.svg
- name: "SMS, MMS 및 RCS"
  link: /docs/user_guide/message_building_by_channel/sms_mms_rcs/
  image: /assets/img/braze_icons/message-text-circle-01.svg
- name: 웹훅
  link: /docs/user_guide/message_building_by_channel/webhooks/
  image: /assets/img/braze_icons/brackets.svg
- name: WhatsApp
  link: /docs/user_guide/message_building_by_channel/whatsapp/
  image: /assets/img/braze_icons/whatsapp.svg
---

## 접근성 리소스

Braze를 사용하여 각 채널에서 접근 가능한 메시징 캠페인을 만들 수 있습니다. 엔지니어와 협력하여 구현에서 접근성 기준을 충족하는지 확인하세요. 추가 지침이 필요하시면, 다음을 추천합니다:

- [접근 가능한 메시징 기초](https://learning.braze.com/accessible-messaging-foundations): 브레이즈 학습 과정에서 브랜드 커뮤니케이션에 적용되는 기본 접근성 원칙을 배우십시오.
- [접근 가능한 메시지 구축]({{site.baseurl}}/help/accessibility/): 브레이즈 내에서 보조 기술을 위해 콘텐츠에 대체 텍스트를 추가하고 구조화하는 방법을 배우십시오.

{% multi_lang_include accessibility/feedback.md %}

## 메시지 채널 선택

캠페인과 캔버스에 가장 적합한 메시지 채널을 결정할 때 항상 메시지의 내용과 긴급성을 고려하십시오:

- **내용**은 메시지가 시각적으로 얼마나 매력적인지를 나타냅니다. 귀하의 콘텐츠를 더욱 풍부하게 만들기 위해 복사본에 멀티미디어 및 기타 자산을 추가할 수 있습니다.
- **긴급성**은 메시지가 사용자에게 얼마나 빨리 알리고 주의를 끌 수 있는지를 측정한 것입니다. 사용자가 즉시 볼 수 있는 알림은 높은 긴급성을 가지며, 사용자가 앱에 로그인해야 하는 메시지는 낮은 긴급성을 가집니다.

다음 매트릭스는 콘텐츠와 긴급성 측면에서 주요 메시징 채널의 강점과 약점을 보여줍니다. 메시지가 얼마나 긴급하고 내용이 풍부해야 하는지 항상 고려한 후 캠페인에 적합한 채널을 선택하십시오.

\![모바일/웹 푸시는 간단한 콘텐츠, 높은 긴급성; 이메일은 풍부한 콘텐츠, 높은 긴급성; 인앱/브라우저 메시지는 간단한 콘텐츠, 낮은 긴급성; 콘텐츠 카드는 낮은 긴급성, 풍부한 콘텐츠]({% image_buster /assets/img_archive/messaging_matrix.png %})

이 매트릭스를 활용하는 방법에 대해 더 알아보려면 [메시징 매트릭스 이해하기](https://learning.braze.com/understand-the-messaging-matrix)에 대한 브레이즈 학습 과정을 확인하십시오.

<br><br>
