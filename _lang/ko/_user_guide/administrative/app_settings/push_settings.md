---
nav_title: 푸시 설정
article_title: 푸시 설정
page_order: 16
page_type: reference
description: "이 문서에서는 Braze 대시보드의 푸시 설정에 대한 개요를 설명합니다."
channel: push

---

# 푸시 설정

> 푸시 **설정** 페이지에서는 푸시 알림에 대한 주요 설정(예: 푸시 실행 시간(TTL) 및 Android 캠페인의 기본 FCM 우선순위 등)을 구성할 수 있습니다. 이러한 설정은 푸시 알림의 전달과 효과를 최적화하여 사용자에게 더 나은 경험을 제공하는 데 도움이 됩니다.

## What is Push TTL?

Push Time to Live (TTL) controls how long Braze will attempt to deliver a push notification to devices that are offline at the time the campaign is sent. TTL이 만료된 후 디바이스가 다시 연결되면 메시지가 전달되지 않습니다. This setting will not remove a notification if it has already been received by the user's device—it only controls how long the push provider attempts to deliver a notification.

## Setting default Push TTL values

By default, Braze sets the Push TTL to the maximum for each push messaging service. 

| Push messaging service | Maximum TTL |
| --- | --- |
| Web (through FCM or Web Push services) | 28 days |
| Firebase Cloud Messaging (FCM) | 28 days |
| Kindle (ADM) | 31 days |
| Huawei (HMS) | 15 days |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

These settings apply globally to all push campaigns unless a different TTL is set for a specific message. To adjust a message's TTL, see [Advanced campaign settings]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/advanced_campaign_settings/#ttl).

To set a different default Push TTL:

1. **설정** > **설정 관리** > **푸시 설정으로** 이동합니다.
2. For each Android platform, define a default time to live value. You can set smaller increments like hours or seconds for more precise control.
3. Select **Save** to apply your changes.

![Firebase, 웹, Kindle 및 Huawei 디바이스에 대한 푸시 TTL 설정.]({% image_buster /assets/img/push_ttl.png %})

## 안드로이드 캠페인의 기본 FCM 우선 순위

모든 Android 푸시 캠페인에 대해 기본 Firebase 클라우드 메시징(FCM) 우선순위를 설정할 수 있습니다. 이 우선순위에 따라 푸시 알림이 사용자의 디바이스에 전달되는 방식이 결정됩니다.

FCM 우선 순위 옵션에는 다음이 포함됩니다:

| 우선순위 | 설명 | 사용 사례 |
| --- | --- | --- |
| 보통 | 배터리 사용량에 최적화된 표준 배달 우선 순위 | 즉각적인 주의가 필요하지 않은 콘텐츠 |
| 높음 | 메시지가 즉시 전송됩니다. | 신속한 전달이 필요한 시간에 민감한 알림 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

기본 FCM 우선순위를 설정하려면 다음과 같이 하세요:

1. **설정** > **설정 관리** > **푸시 설정으로** 이동합니다.
2. FCM 우선순위 섹션에서 기본 설정으로 '보통' 또는 '높음'을 선택합니다.
3. Select **Save** to apply your changes.

![Android 배달 우선순위 설정]({% image_buster /assets/img/push_fcm_priority_settings.png %})

이 설정은 특정 캠페인을 만들 때 다른 우선순위를 선택하지 않는 한 모든 새 Android 푸시 캠페인에 전역적으로 적용됩니다. 

{% alert note %}
앱에서 사용자에게 표시되는 알림이나 사용자 참여를 유도하지 않는 우선순위가 높은 메시지를 자주 보내는 것을 FCM이 감지하면 해당 메시지의 우선순위가 자동으로 일반 우선순위로 내려갈 수 있습니다.
{% endalert %}

FCM 우선순위 수준 및 우선순위 해제에 대한 자세한 내용은 [고급 캠페인 설정을]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/advanced_campaign_settings/#fcm-priority) 참조하세요.

