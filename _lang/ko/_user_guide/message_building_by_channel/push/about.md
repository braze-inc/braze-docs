---
nav_title: "푸시 알림 정보"
article_title: 푸시 알림 정보
page_order: 0
page_type: reference
description: "이 참고 문서에서는 푸시에 대한 간략한 개요와 푸시 메시지 시작을 위한 리소스, 몇 가지 규정 사항을 제공합니다."
channel:
  - Push

---

# [![Braze 학습 과정]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/messaging-channels-push){: style="float:right;width:120px;border:0;" class="noimgborder"}푸시 알림 정보

> 푸시 알림은 시간에 민감한 클릭 유도 문안과 한동안 앱에 접속하지 않았던 사용자의 재참여를 유도하는 데 유용합니다. 성공적인 푸시 캠페인은 사용자를 콘텐츠로 직접 유도하고 앱의 가치를 입증합니다.

사용자가 메시지를 받으려면 푸시 수신에 동의해야 하므로 인앱 메시지를 사용하여 고객에게 푸시 알림을 보내려는 이유와 푸시를 사용 설정하면 어떤 이점이 있는지 설명하는 것이 좋습니다. This process is called [push priming]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/).

![Apple 제품에서 푸시 메시지 예시.][1]{: height="400px"}  ![iPhone 홈 화면의 스톱워치에서 푸시 메시지 예시는 다음과 같습니다: "안녕하세요! iOS 푸시입니다."][2]{: height="400px"}

푸시 알림의 더 많은 예시를 보려면 [사례 연구][8]에서 확인하세요.

## 잠재적 사용 사례

푸시 알림은 신규 사용자를 유치하고 재참여 캠페인을 진행하기 위한 훌륭한 도구입니다. 다음은 일반적인 푸시 메시지 사용 사례의 몇 가지 예입니다.

| 사용 사례 | 설명 |
| -------- | ----------- |
| 초기 온보딩 | 사용자가 계정을 등록하는 등 앱 사용을 위한 초기 단계를 밟기 전까지는 앱의 가치가 심각하게 제한됩니다. 푸시 알림을 사용하여 사용자가 이 단계를 완료하도록 유도하여 앱을 완전히 사용할 수 있도록 합니다. |
| 첫 구매 | 사용자가 앱 사용에 익숙해지면 푸시 알림을 사용하여 인앱 구매자로 전환하는 데 도움을 줄 수 있습니다. |
| 새로운 기능 | 푸시 알림은 이탈한 사용자에게 앱으로 다시 돌아올 수 있는 새로운 기능을 알리는 데 효과적일 수 있습니다. |
| 시간에 민감한 오퍼 | 오퍼에 시간이 촉박하다면, 오퍼가 만료되기 전에 사용자에게 이를 알리는 데 푸시가 좋은 방법이 될 수 있습니다. 이러한 메시지는 일반적으로 긴박감이 높으며 최근에 앱이 만료된 사용자에게 앱에 대해 상기시키는 데 최적입니다.<br><br> 예를 들어, 앱이 게임이고 사용자가 매일 게임을 플레이하는 연속 기록을 유지하면 인게임 화폐 보너스를 제공한다고 가정해 보겠습니다. 특정 일수를 초과한 경우 사용자에게 연승이 깨질 위험이 있다는 알림을 보내는 것이 적절할 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

휴면 사용자 재참여에 대한 자세한 내용은 [빠른 성공 사례][23] 주제 페이지를 참조하세요.

## 푸시 사용을 위한 전제 조건

Braze를 사용하여 푸시 메시지를 생성하고 전송하려면 먼저 개발자와 협력하여 웹사이트 또는 앱에 푸시를 통합해야 합니다. 자세한 단계는 각 플랫폼별 통합 가이드를 참조하세요:

- [iOS]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift)
- [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/?tab=android)
- [Web]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=web)

## 푸시 메시지 규정

푸시 메시지는 고객의 휴대폰이나 브라우저로 직접 전달되는 침입형 메시징 유형이므로 앱과 사이트를 통해 푸시 메시지를 보내는 가이드라인이 있습니다.

### 앱에 대한 모바일 푸시 규정

{% alert important %}
푸시 메시지는 광고, 스팸, 프로모션 등으로 푸시 메시지를 사용하는 것과 관련된 Apple App Store 및 Google Play 스토어 정책의 가이드라인을 준수해야 합니다.
{% endalert %}

|Apple 앱 스토어 정책|
|---|
|[3.2.2][9] 허용되지 않음: (i) 앱스토어와 유사하거나 일반 관심사 컬렉션으로 타사 앱, 확장 프로그램 또는 플러그인을 표시하기 위한 인터페이스를 만드는 행위.| 
|[4.5.4][7] 푸시 알림은 앱이 작동하는 데 필요하지 않아야 하며 민감한 개인 정보나 기밀 정보를 전송하는 데 사용해서는 안 됩니다. 고객이 앱 UI에 표시된 동의 문구를 통해 명시적으로 수신에 동의하고 사용자가 메시지 수신을 거부할 수 있는 방법을 앱에 제공하지 않는 한, 푸시 알림을 프로모션이나 직접 마케팅 목적으로 사용해서는 안 됩니다.|
|[4.10](https://developer.apple.com/app-store/review/guidelines/#monetizing-built-in-capabilities) 회원님은 푸시 알림, 카메라 또는 자이로스코프와 같은 하드웨어 또는 운영 체제에서 제공하는 내장 기능이나 Apple 음악 액세스, iCloud 저장소 또는 스크린 타임 API와 같은 Apple 서비스 및 기술을 수익화할 수 없습니다.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

|Google Play 스토어 정책|
|---|
|[시스템 기능의 무단 사용 또는 모방][10] 알림이나 경고와 같은 시스템 기능을 모방하거나 방해하는 앱이나 광고는 허용되지 않습니다. 시스템 수준 알림은 사용자에게 특가 상품을 알려주는 항공사 앱이나 게임 내 프로모션을 알려주는 게임과 같이 앱의 필수 기능에만 사용할 수 있습니다.|
{: .reset-td-br-1 role="presentation" }

[1]: {% image_buster /assets/img/red-dress.gif %}
[2]: {% image_buster /assets/img/ios_push.png %}
[3]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#deep-linking-to-in-app-content
[8]:https://www.braze.com/customers
[7]:https://developer.apple.com/app-store/review/guidelines/#apple-sites-and-services
[9]:https://developer.apple.com/app-store/review/guidelines/#unacceptable
[10]:https://developers.google.com/android/play-protect/mobile-unwanted-software#muws-categories
[23]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/capturing_lapsing_users/#capturing-lapsing-users
