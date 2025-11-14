---
nav_title: 푸시
article_title: 푸시
page_order: 4
layout: dev_guide
guide_top_header: "푸시"
guide_top_text: "푸시 알림은 모바일 또는 웹을 통해 시간에 민감한 행동 유도 메시지를 전송하고, 한동안 앱에 들어오지 않은 사용자를 다시 참여시키는 검증된 방법입니다. 사용자를 콘텐츠로 직접 안내하고 애플리케이션의 가치를 보여줍니다. 푸시 알림은 사용자를 특정 장소로 유도하는 데 유용하지만, 현명하게 사용해야 합니다. <br><br> 다음 기사 중 하나를 읽거나 [Push Braze Learning course](https://learning.braze.com/messaging-channels-push)를 확인하여 푸시를 보낼 수 있는 대상, 전송 방법 및 Braze가 제공하는 고급 푸시 기능에 대해 알아보세요. 푸시 알림의 예시는 [고객 사례](https://www.braze.com/customers)를 확인하세요."
description: "이 랜딩 페이지는 푸시 메시지의 홈입니다. 여기에서 푸시 유형, 푸시 등록, 푸시 활성화, 푸시 기초, 푸시 보고서 등에 대한 기사를 찾을 수 있습니다."
channel:
  - push

guide_featured_title: "인기 기사"
guide_featured_list:
- name: 푸시 유형
  link: /docs/user_guide/message_building_by_channel/push/types/
  image: /assets/img/braze_icons/list.svg
- name: 푸시 등록
  link: /docs/user_guide/message_building_by_channel/push/push_registration/
  image: /assets/img/braze_icons/check-square-broken.svg
- name: 푸시 활성화 및 구독
  link: /docs/user_guide/message_building_by_channel/push/users_and_subscriptions/
  image: /assets/img/braze_icons/users-01.svg
- name: 푸시 메시지 만들기
  link: /docs/user_guide/message_building_by_channel/push/creating_a_push_message/
  image: /assets/img/braze_icons/edit-05.svg

guide_menu_title: "More articles"
guide_menu_list:
- name: 고급 옵션
  link: /docs/user_guide/message_building_by_channel/push/advanced_push_options/
  image: /assets/img/braze_icons/settings-01.svg
- name: 푸시 기초
  link: /docs/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/
  image: /assets/img/braze_icons/phone-02.svg
- name: 보고서
  link: /docs/user_guide/message_building_by_channel/push/push_reporting/
  image: /assets/img/braze_icons/bar-chart-01.svg
- name: 안드로이드 옵션
  link: /docs/user_guide/message_building_by_channel/push/android/
  image: /assets/img/braze_icons/android.svg
- name: iOS 옵션
  link: /docs/user_guide/message_building_by_channel/push/ios/
  image: /assets/img/braze_icons/apple.svg
- name: 웹 푸시
  link: /docs/user_guide/message_building_by_channel/push/web/
  image: /assets/img/braze_icons/monitor-01.svg
- name: 모범 사례
  link: /docs/user_guide/message_building_by_channel/push/best_practices/
  image: /assets/img/braze_icons/check-square-broken.svg
- name: 메시지의 로케일
  link: /docs/locales_in_messages/
  image: /assets/img/braze_icons/translate-01.svg
- name: 일반 푸시 오류 메시지
  link: /docs/user_guide/message_building_by_channel/push/push_error_codes/
  image: /assets/img/braze_icons/alert-triangle.svg
- name: 문제 해결
  link: /docs/user_guide/message_building_by_channel/push/troubleshooting/
  image: /assets/img/braze_icons/annotation-question.svg
- name: 자주 묻는 질문
  link: /docs/user_guide/message_building_by_channel/push/faq/
  image: /assets/img/braze_icons/annotation-question.svg
---

## [![브레이즈 학습 과정]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/path/push-fundamentals){: style="float:right;width:120px;border:0;" class="noimgborder"}사용 사례

\![Apple 제품 간의 푸시 메시지 예시.]({% image_buster /assets/img/red-dress.gif %}){: height="400px"}  \![iPhone 홈 화면의 스톱워치에서 읽는 푸시 메시지 예시: "안녕하세요!" 이것은 iOS 푸시입니다".]({% image_buster /assets/img/ios_push.png %}){: height="400px"}

푸시 알림은 새로운 사용자를 유치하고 재참여 캠페인을 만드는 데 훌륭한 도구입니다. 여기 일반적인 푸시 메시지 사용 사례의 몇 가지 예가 있습니다.

| 사용 사례 | 설명 |
| -------- | ----------- |
| 초기 온보딩 | 사용자가 앱을 사용하기 위한 초기 단계를 밟기 전(예: 계정 등록)까지 그들의 가치는 심각하게 제한됩니다. 푸시 알림을 사용하여 사용자가 이러한 단계를 완료하도록 촉구하여 앱을 완전히 사용할 수 있도록 하세요. |
| 첫 구매 | 사용자가 앱 사용에 익숙해지면, 푸시 알림을 사용하여 그들을 인앱 구매자로 전환하는 데 도움을 줄 수 있습니다. |
| 새로운 기능 | 푸시 알림은 이탈한 사용자에게 새로운 기능을 알리는 데 효과적일 수 있으며, 이로 인해 그들이 다시 앱으로 돌아올 수 있습니다. |
| 시간 민감한 제안 | 제안에 대한 시계가 똑딱거리고 있다면, 때때로 푸시는 사용자가 만료되기 전에 이를 알리는 좋은 방법입니다. 이 메시지는 일반적으로 높은 긴급성을 가지고 있으며, 최근에 사용을 중단한 사용자에게 앱을 상기시키는 데 최적입니다.<br><br> 예를 들어, 귀하의 앱이 게임이고 사용자가 매일 게임을 플레이하는 연속성을 유지하면 게임 내 통화 보너스를 제공한다고 가정해 보겠습니다. 사용자에게 그 연속성이 깨질 위험이 있다는 것을 알리는 것은 특정 일수를 초과한 경우 합리적인 푸시가 될 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

중단된 사용자를 다시 참여시키는 방법에 대한 자세한 정보는 [빠른 승리]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/capturing_lapsing_users/#capturing-lapsing-users) 페이지를 참조하세요.

## 푸시 사용을 위한 전제 조건

Braze를 사용하여 푸시 메시지를 생성하고 전송하기 전에 개발자와 협력하여 웹사이트나 앱에 푸시를 통합해야 합니다. 자세한 단계는 각 플랫폼에 대한 통합 가이드를 참조하세요:

- [iOS]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift)
- [안드로이드]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/?tab=android)
- [웹]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=web)

## 푸시 프라이밍

사용자가 메시지를 받기 위해 푸시에 옵트인해야 한다는 점을 염두에 두세요. 이는 고객에게 푸시 알림을 보내고자 하는 이유와 푸시를 활성화하면 어떤 이점이 있는지를 설명하기 위해 인앱 메시지를 사용하는 것이 좋습니다. 이 과정은 [푸시 프라이밍]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/)이라고 합니다.

## 푸시 메시지 규정

푸시 메시지는 고객의 전화나 브라우저로 직접 전송되는 침입적인 유형의 메시지이기 때문에 앱과 사이트를 통해 푸시 메시지를 전송하는 데 대한 지침이 있습니다.

### 앱에 대한 모바일 푸시 규정

{% alert important %}
귀하의 푸시 메시지는 Apple App Store 및 Google Play Store 정책의 지침 내에 있어야 하며, 특히 푸시 메시지를 광고, 스팸, 프로모션 등으로 사용하는 것과 관련하여 그렇습니다.
{% endalert %}

|애플 앱 스토어 정책|
|---|
|[3.2.2](https://developer.apple.com/app-store/review/guidelines/#unacceptable) 허용되지 않음: (i) 앱 스토어와 유사한 제3자 앱, 확장 프로그램 또는 플러그인을 표시하는 인터페이스를 생성하거나 일반 관심 컬렉션으로 사용하는 것.| 
|[4.5.4](https://developer.apple.com/app-store/review/guidelines/#apple-sites-and-services) 푸시 알림은 앱이 작동하는 데 필요하지 않으며, 민감한 개인 정보나 기밀 정보를 전송하는 데 사용되어서는 안 됩니다. 푸시 알림은 고객이 앱의 UI에 표시된 동의 언어를 통해 수신하기로 명시적으로 동의하지 않는 한, 프로모션이나 직접 마케팅 목적으로 사용되어서는 안 됩니다. 또한 사용자가 이러한 메시지를 수신하지 않도록 선택할 수 있는 방법을 앱에 제공해야 합니다.|
|[4.10](https://developer.apple.com/app-store/review/guidelines/#monetizing-built-in-capabilities) 푸시 알림, 카메라 또는 자이로스코프와 같은 하드웨어 또는 운영 체제에서 제공하는 내장 기능을 수익화할 수 없습니다. 또한 Apple Music 접근, iCloud 저장소 또는 Screen Time API와 같은 Apple 서비스 및 기술도 포함됩니다.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

|구글 플레이 스토어 정책|
|---|
|[시스템 기능의 무단 사용 또는 모방](https://developers.google.com/android/play-protect/mobile-unwanted-software#muws-categories) 우리는 알림이나 경고와 같은 시스템 기능을 모방하거나 방해하는 앱이나 광고를 허용하지 않습니다. 시스템 수준의 알림은 항공사 앱이 사용자에게 특별 거래를 알리거나 게임이 사용자에게 게임 내 프로모션을 알리는 것과 같은 앱의 필수 기능에만 사용될 수 있습니다.|
{: .reset-td-br-1 role="presentation" }
