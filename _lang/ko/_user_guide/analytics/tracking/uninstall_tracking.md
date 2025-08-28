---
nav_title: 설치 제거 추적
article_title: 설치 제거 추적
page_order: 6
page_type: reference
description: "이 참조 문서에서는 캠페인 수준 및 앱 수준 통계에 대한 제거 추적 구현에 대해 설명합니다."
tool: Reports

---

# 추적 제거

> 이 문서에서는 시간 경과에 따른 집계된 앱 제거를 확인하여 추세와 이상 징후를 파악하고 캠페인 수준의 제거를 추적하여 특정 캠페인이 앱 설치를 유도하는지 또는 방해하는지 확인하는 방법을 설명합니다.

Braze의 제거 추적은 다음과 같은 세부 정보를 제공합니다:

1. **홈** 페이지의 시계열 그래프에서 일일 앱 수준 제거 통계를 확인할 수 있습니다.
2. 특정 캠페인의 **캠페인 세부 정보** 페이지에서 캠페인 수준 제거 통계를 시계열 그래프로 확인할 수 있습니다. 이 통계는 매일 삭제하는 캠페인 수신자 수를 지정합니다.

{% alert note %}
Braze 대시보드에서 추적 기능을 제거하려면 옵트인해야 합니다. 이 기능은 현재 iOS, Android 및 Fire OS의 앱에서 사용할 수 있습니다.
{% endalert %}

## 작동 방식

Braze는 정기적인 푸시 캠페인에서 기본 수준의 제거 정보를 자동으로 수집합니다. 그러나 사용자마다 푸시 캠페인을 수신하는 빈도가 다를 수 있으므로, 삭제 추적 기능을 제공하여 사용자들의 삭제 활동에 대한 보다 정확한 스냅샷을 제공합니다.

## 제거 추적 켜기

추적하려는 각 앱의 **앱 설정** 페이지의 **설정** 아래에서 제거 추적을 사용 설정할 수 있습니다.

앱에 대해 제거 추적이 켜져 있으면 24시간 동안 세션을 녹화하거나 푸시를 받지 않은 사용자에게 매일 밤 백그라운드 푸시 메시지가 전송됩니다.

### 구성

To configure uninstall tracking for your iOS application, use a [utility method]({{site.baseurl}}/developer_guide/analytics/tracking_uninstalls/?sdktab=swift). For your Android application, use [`isUninstallTrackingPush()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.push/-braze-notification-payload/is-uninstall-tracking-push.html). 제거 추적 또는 일반 푸시 캠페인 전송을 통해 제거가 감지되면, Braze는 사용자의 제거 예상 시간을 기록합니다. 이 시간은 사용자 프로필에 표준 속성으로 저장되며 윈백 캠페인의 사용자 세그먼트를 정의하는 데 사용할 수 있습니다.

## 제거를 기준으로 세그먼트 필터링

The **Uninstalled** filter selects users who uninstalled your app within a time range. 제거 시점을 정확히 파악하기 어렵기 때문에 제거 필터의 시간 범위를 넓게 설정하여 제거한 모든 사람이 어느 시점에 해당 세그먼트에 속하도록 하는 것이 좋습니다.

제거에 대한 일일 통계는 **홈** 페이지에서 확인할 수 있습니다. 

![Uninstall segment.]({% image_buster /assets/img_archive/Uninstall_Segment.png %} "Uninstall Segment")

그래프는 Braze가 제공하는 다른 통계와 마찬가지로 앱과 세그먼트별로 세분화할 수 있습니다. In the **Performance overview** section, select your date range and, if desired, an app. Then, scroll down to the **Performance Over Time** graph and do the following:

1. **통계 대상** 드롭다운에서 **제거**를 선택합니다.
2. **분류** 드롭다운에서 **세그먼트별을** 선택합니다.
3. 분석 **값** 드롭다운에서 그래프에 포함할 세그먼트를 선택합니다.

{% alert note %}
제거 추적이 활성화되지 않은 앱은 일부 사용자(푸시 알림이 타겟팅된 사용자)의 제거만 보고하므로 일일 제거 총계가 표시된 것보다 높을 수 있습니다.
{% endalert %}

## 캠페인 추적 제거

캠페인 제거 추적은 특정 캠페인을 수신한 후 선택한 기간 내에 앱을 삭제한 사용자 수를 표시합니다. 이 도구는 캠페인이 의도하지 않은 부정적인 사용자 행동을 조장할 수 있는 방법에 대한 인사이트를 제공하고 전반적인 캠페인 효과를 측정하는 데 도움이 됩니다.

캠페인의 제거 통계는 특정 캠페인의 **캠페인 분석** 페이지에 있습니다. 멀티채널 및 다변량 캠페인의 경우, 설치 제거를 각각 채널 및 배리언트별로 세분화할 수 있습니다.

![Uninstall at the campaign-level.]({% image_buster /assets/img_archive/campaign_level_uninstall_tracking.png %})

### 작동 방식

Braze는 사용자의 디바이스로 전송된 푸시 메시지가 Firebase 클라우드 메시징(FCM) 또는 Apple 푸시 알림 서비스(APN)로부터 앱이 더 이상 설치되지 않았다는 신호를 반환하는 시점을 관찰하여 제거를 추적합니다. 특정 앱에 대해 글로벌 제거 추적이 켜져 있으면 사용자가 앱을 제거했는지 여부를 감지하기 위해 매일 사용자에게 무음 푸시 메시지를 보냅니다. 이 '무음' 푸시는 모든 사용자에게 전송되지만(사용자가 앱 설정에서 무음 푸시를 비활성화하지 않은 경우), 사용자에게 푸시가 표시되지는 않습니다. 사용자가 삭제한 것이 감지되면 삭제합니다:

* 앱의 총 제거 횟수를 1씩 늘립니다.
* 지난 24시간 동안 사용자가 성공적으로 수신한 모든 캠페인의 제거 횟수를 하나씩 늘립니다.
* 사용자가 24시간 동안 세 개의 캠페인을 수신한 후 삭제하면 세 개의 캠페인 모두에 대한 '삭제' 횟수가 증가합니다.

제거 추적은 FCM 및 APN에 의해 이 정보에 대한 제한이 적용될 수 있습니다. Braze는 FCM 또는 APN이 사용자가 제거했다고 알려줄 때만 제거 횟수를 늘리지만, 이러한 타사 시스템은 언제든 제거 사실을 알릴 수 있는 권한을 보유합니다. 따라서 제거 추적은 정확한 통계가 아닌 방향성 추세를 감지하는 데 사용해야 합니다.

For more on using uninstall tracking, see our blog post [Uninstall Tracking: An Industry Look at its Strengths and Limitations](https://www.braze.com/blog/uninstall-tracking-an-industry-look-at-its-strengths-and-limitations/).

## 문제 해결

### 갑자기 삭제가 급증하는 이유는 무엇인가요?

앱 제거가 급증하는 경우, Firebase 클라우드 메시징(FCM)과 Apple 푸시 알림 서비스(APNS)가 이전 토큰을 다른 주기로 해지하기 때문일 수 있습니다.

### Why are the number of app uninstalls different from what's in APNs?

차이가 예상됩니다. 

Apple uses a randomized schedule to delay reporting when a push token becomes invalid, meaning that even after a user uninstalls an app, APNs may continue to return successful responses to push notifications for a period of time. This delay is intentional and designed to protect user privacy. No bounce or failure will be reported until APNs returns a `410` status for an invalid token.

