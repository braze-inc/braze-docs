---
nav_title: 사용 중단
article_title: 사용 중단
page_order: 9
page_type: reference
description: "이 페이지에는 더 이상 사용되지 않는 문서에 대한 참조가 포함되어 있으며 더 이상 사용되지 않는 기능 및 지원되지 않는 기능의 목록이 제공됩니다."
---

# 사용 중단

기술은 항상 Braze 내부와 외부에서 움직이고 있습니다! 그리고 Braze는 이에 발맞추기 위해 최선을 다하고 있습니다. 이 문서에서는 Braze의 기원과 기술, 즉 "지난 시대"에 사람들을 어떻게 지원했는지 살펴볼 수 있습니다.

더 이상 존재하지 않는 연동 서비스나 기능에 대한 용어를 검색하다가 이 페이지에 오셨을 수도 있습니다. 이는 기술 업계의 진행 상황과 움직임에 대한 정보를 제공하기 위한 시도입니다. 다음 링크를 방문하여 더 이상 사용되지 않는 기능 및 지원되지 않는 기능 목록을 확인하고 사용되지 않는 도움말을 읽을 수 있습니다.

## 더 이상 사용되지 않는 문서

- [Android용 맞춤형 푸시 브로드캐스트 수신기]({{site.baseurl}}/help/release_notes/deprecations/custom_broadcast_receiver/)
- [Eclipse SDK 설정]({{site.baseurl}}/help/release_notes/deprecations/eclipse_setup_deprecated/)
- [TLS 1.0 및 1.1 사용 중단]({{site.baseurl}}/help/release_notes/deprecations/tls_deprecation/)
- [Twilio 웹훅 통합]({{site.baseurl}}/help/release_notes/deprecations/twilio/)
- [파트너십 최적화]({{site.baseurl}}/help/release_notes/deprecations/apptimize/)
- [Grouparoo 파트너십]({{site.baseurl}}/help/release_notes/deprecations/grouparoo)
- [Shopify `checkout.liquid` 사용 중단]({{site.baseurl}}/help/release_notes/deprecations/shopify_checkout/)

## 사용 중단 로그

### Shopify `checkout.liquid`

**지원 철회**: 2024년 8월(1단계), 2025년 8월(2단계)

Shopify 에 대한 지원`checkout.liquid` 은 2024년 8월에 중단되기 시작하여 2025년 8월에 종료됩니다. Shopify는 더 안전하고 성능이 뛰어나며 사용자 지정이 가능한 [Checkout 확장성으로](https://www.shopify.com/enterprise/blog/checkout-extensibility-winter-editions) 전환할 예정입니다.

### Android용 맞춤형 푸시 브로드캐스트 수신기

**지원 철회**: 2022년 10월

푸시 알림에 사용자 지정 `BroadcastReceiver` 사용은 더 이상 사용되지 않습니다. 대신 [` subscribeToPushNotificationEvents()`]({{site.baseurl}}/developer_guide/push_notifications/customization/?sdktab=android#android_using-a-callback-for-push-events) 대신 사용하세요.

### Grouparoo 파트너십

**지원 철회**: 2022년 4월

Grouparoo에 대한 지원은 2022년 4월부터 중단되었습니다.

### Braze Windows SDK

**2022년 3월 24일**: Braze Windows SDK는 더 이상 사용되지 않으며, Braze 대시보드에서 새로운 Windows 앱을 만들 수 없습니다.<br>
**2022년 9월 15일**: Windows 앱에 새 메시지를 보낼 수 없습니다. 기존 메시지 및 데이터 수집은 영향을 받지 않습니다.<br>
**2024년 1월 11일**: Braze는 더 이상 Windows 앱에서 메시지를 제공하거나 데이터를 수집하지 않습니다.

### Baidu 푸시 통합

**2022년 3월 24일**: Braze 바이두 푸시 통합은 더 이상 사용되지 않으며, Braze 대시보드에서 새로운 바이두 앱을 만들 수 없습니다. <br>
**2022년 9월 15일**: 새로운 Baidu 푸시 메시지를 만들 수 없습니다. 기존 메시지 및 데이터 수집은 영향을 받지 않습니다.<br>
**2024년 1월 11일**: Braze는 더 이상 Baidu 앱에서 메시지를 제공하거나 데이터를 수집하지 않습니다.

### appboyBridge 전역 변수

**지원 철회**: 2021년 5월<br>
**대체됨**: `brazeBridge`

`appboyBridge` 글로벌 변수는 더 이상 사용되지 않으며 `brazeBridge` 로 대체됩니다. `appboyBridge`는 기존 고객에게는 계속 작동하지만 `appboyBridge`를 사용 중인 경우 `brazeBridge`로 마이그레이션하는 것이 좋습니다.

### Amazon Moments 파트너십

**지원 철회**: 2020년 6월

Amazon Moments에 대한 지원은 2020년 6월부터 중단되었습니다. Amazon Moments가 Amazon Advertising에 통합되어 해당 API와 연동이 더 이상 사용되지 않습니다.

### 사실적인 파트너십

**지원 철회**: 2020년 6월

Factual에 대한 지원은 2020년 6월부로 중단되었습니다. 최근 Foursquare가 인수한 Factual은 더 이상 Braze 플랫폼과 통합되지 않습니다.

### Twilio 웹훅 통합

**지원 철회**: 2020년 1월

2020년 1월 31일부로 [Twilio 웹훅 통합]({{site.baseurl}}/partners/twilio/)에 대한 지원이 중단되었습니다. Braze에서 여전히 SMS 서비스에 액세스하려면 [SMS 문서를]({{site.baseurl}}/user_guide/message_building_by_channel/sms/) 참조하세요.

### 파트너십 최적화

**지원 철회**: 2019년 8월

현재 [Braze와 함께 Apptimize]({{site.baseurl}}/help/release_notes/deprecations/apptimize)를 사용 중인 경우 서비스 중단은 발생하지 않습니다. 여전히 Apptimize 커스텀 속성을 Braze 고객 프로필에 설정할 수 있습니다. 그러나 파트너와의 공식적인 에스컬레이션 지원은 제공되지 않습니다.

### 인앱 메시지 원본

**지원 철회:** 2019년 2월<br>
**대체됨**: [인앱 메시징]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/create/)

Braze는 최신 UX 및 UI 모범 사례를 준수하도록 인앱 메시지의 모양과 느낌을 개선했으며, 더 이상 기존 인앱 메시지를 지원하지 않습니다.

Braze는 다음 SDK 릴리스에서 새로운 형태의 인앱 메시지로 전환했습니다.
- iOS: `2.19.0`
- Android: `1.13.0`
- 웹: `1.3.0`

이번 릴리스 이전에는 Braze에서 "원본 인앱 메시지"를 지원했습니다. 이전에는 새 릴리스 이전에 인앱 캠페인을 실행한 모든 고객에게 오리지널 인앱 메시지에 대한 지원이 제공되었습니다. 모든 캠페인 통계는 변경 사항의 영향을 받지 않았으며, 기존 인앱 메시지를 보낸 사람들은 **캠페인** 페이지의 **캠페인 만들기** 버튼을 통해 다른 사람들에게 메시지를 보낼 수 있었습니다.

### 피드백 위젯

**지원 철회**: 2019년 7월 1일.

Braze SDK는 앱에 추가할 수 있는 피드백 위젯을 제공하여 사용자가 `submitfeedback` 메서드를 사용하여 피드백을 남기고 Desk.com 또는 Zendesk로 전달할 수 있도록 하며 대시보드에서 관리합니다.

### Google 클라우드 메시징(GCM)

**지원 철회**: Braze 지원 중단: 2018년 7월, Google 지원 중단: 2019년 5월 29일<br>
**대체됨**: [Firebase 클라우드 메시징(FCM)]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/#step-1-enable-firebase)

Google은 2019년 5월 29일부로 [GCM에 대한 지원을 중단했습니다](https://developers.googleblog.com/2018/04/time-to-upgrade-from-gcm-to-fcm.html). Braze는 2018년 7월에 Android SDK에서 GCM에 대한 지원을 중단했으며, 이는 [Android SDK 체인지로그](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md)에 명시되어 있습니다. 즉, 기존 GCM 토큰은 계속 작동하며 기존 사용자에게 메시지를 보낼 수 있습니다. 그러나 새 사용자에게는 메시지를 보낼 수 없습니다.

아직 [FCM(Firebase Cloud Messaging)]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/#step-1-enable-firebase) 으로 마이그레이션하지 않은 고객은 이 변경 사항의 영향을 받을 수 있습니다.

FCM으로 전환하지 않은 경우 모든 GCM 푸시 토큰 등록이 실패합니다. 현재 앱이 GCM을 지원하는 경우 개발팀과 협력하여 [GCM에서 FCM(파이어베이스 클라우드 메시징)으로 전환](https://developers.google.com/cloud-messaging/android/android-migrate-fcm)해야 합니다.

### Eclipse

**지원 철회**: 2014-2015<br>
**대체됨**: [Android 스튜디오]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#using-android-studio)

Braze는 Eclipse Android 개발자 도구(ADT) 플러그인에 대한 Google의 [서비스 종료](http://android-developers.blogspot.com/2015/06/an-update-on-eclipse-android-developer.html)로 인해 Eclipse IDE에 대한 지원을 중단했습니다. 

마이그레이션 전에 Eclipse 통합에 대한 도움이 필요한 경우 [지원팀]({{site.baseurl}}/support_contact/)에 문의하여 도움을 받으세요.

### 원시 이벤트 스트림(RES)

**지원 철회**: 2018년 7월<br>
**대체됨**: [커런츠]({{site.baseurl}}/user_guide/data/braze_currents/)

원시 이벤트 스트림은 [커런츠]({{site.baseurl}}/user_guide/data/braze_currents/)의 전신으로, 향후 Braze 데이터를 위한 공간을 마련하기 위해 더 이상 사용되지 않습니다.

### 유휴 상태에서의 지연 - GCM 기능

**지원 철회**: 2016년 11월

유휴 상태 동안 지연 매개변수는 이전에는 [GCM 푸시 옵션](https://developers.google.com/cloud-messaging/http-server-ref)의 일부였습니다. Google은 2016년 11월 15일에 이 옵션에 대한 지원을 철회했습니다. 이전에는 **true**로 설정하면 기기가 활성화될 때까지 메시지를 보내지 않아야 함을 나타냅니다.

### 사용자 지정 엔드포인트

**지원 철회**: 2019년 12월

사용자 지정 엔드포인트 제거. 사용자 지정 엔드포인트가 있는 경우 계속 사용할 수 있지만 Braze에서는 더 이상 제공하지 않습니다.


