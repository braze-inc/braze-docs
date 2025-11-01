---
nav_title: 푸시 설정
article_title: 푸시 설정
page_order: 16
page_type: reference
description: "이 문서에서는 Braze 대시보드의 푸시 설정에 대한 개요를 제공합니다."
channel: push

---

# 푸시 설정

> **푸시 설정** 페이지에서는 푸시 TTL(푸시 유지 시간), Android 캠페인의 기본값 FCM 우선순위 등 푸시 알림에 대한 주요 설정을 구성할 수 있습니다. 이러한 설정은 푸시 알림의 전달과 효과를 최적화하여 사용자에게 더 나은 경험을 제공하는 데 도움이 됩니다.

## 푸시 TTL이란 무엇인가요?

푸시 TTL(유지 시간)은 캠페인이 전송될 때 오프라인 상태인 기기에 푸시 알림을 전달하려고 시도하는 시간을 제어합니다. TTL이 만료된 후 기기가 다시 연결되면 메시징이 전달되지 않습니다. 이 설정은 사용자의 기기가 이미 알림을 수신한 경우에는 알림을 제거하지 않으며 푸시 제공업체가 알림을 전달하려고 시도하는 시간만 제어합니다.

## 기본값 푸시 TTL 값 설정하기

기본적으로 Braze는 각 푸시 메시징 서비스에 대해 푸시 TTL을 최대값으로 설정합니다. 

| 푸시 메시징 서비스 | 최대 TTL |
| --- | --- |
| 웹(FCM 또는 웹 푸시 서비스를 통해) | 28일 |
| Firebase 클라우드 메시징(FCM) | 28일 |
| Kindle (ADM) | 31일 |
| Huawei(HMS) | 15일 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

이러한 설정은 특정 메시지에 대해 다른 TTL을 설정하지 않는 한 모든 푸시 캠페인에 전역적으로 적용됩니다. 메시지의 TTL을 조정하려면 [고급 캠페인 설정을]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/advanced_campaign_settings/#ttl) 참조하세요.

다른 기본값 푸시 TTL을 설정하려면:

1. **설정** > **설정 관리** > **푸시 설정으로** 이동합니다.
2. 각 Android 플랫폼에 대해 기본값인 유지 시간을 정의합니다. 시간 또는 초와 같이 더 작은 단위로 설정하여 보다 정밀하게 제어할 수 있습니다.
3. **저장을** 선택하여 변경 사항을 적용합니다.

\![Firebase, 웹, 킨들, 화웨이 기기에 대한 푸시 TTL 설정.]({% image_buster /assets/img/push_ttl.png %})

## Android 캠페인의 기본값 FCM 우선 순위

모든 Android 푸시 캠페인에 대한 기본값 FCM(Firebase 클라우드 메시징) 우선 순위를 설정할 수 있습니다. 이 우선순위에 따라 푸시 알림이 사용자의 기기에 전달되는 방식이 결정됩니다.

FCM 우선 순위 옵션은 다음과 같습니다:

| 우선순위 | 설명 | 사용 사례 |
| --- | --- | --- |
| 보통 | 배터리 사용량을 최적화하는 표준 전달 우선 순위 | 즉각적인 주의가 필요하지 않은 콘텐츠 |
| 높음 | 메시징이 즉시 전송됩니다. | 신속한 전달이 필요한 시간에 민감한 알림 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

기본값 FCM 우선순위를 설정합니다:

1. **설정** > **설정 관리** > **푸시 설정으로** 이동합니다.
2. FCM 우선순위 섹션에서 기본값으로 '보통' 또는 '높음'을 선택합니다.
3. **저장을** 선택하여 변경 사항을 적용합니다.

\![Android 전달 우선순위 설정.]({% image_buster /assets/img/push_fcm_priority_settings.png %})

이 설정은 특정 캠페인을 만들 때 다른 우선순위를 선택하지 않는 한 모든 새 Android 푸시 캠페인에 전역적으로 적용됩니다. 

{% alert note %}
앱에서 사용자에게 표시되는 알림이나 사용자 참여를 유도하지 않는 우선순위가 높은 메시지를 자주 보내는 것을 FCM이 감지하면 해당 메시지의 우선순위가 자동으로 일반 우선순위로 내려갈 수 있습니다.
{% endalert %}

FCM 우선순위 수준 및 우선순위 해제에 대한 자세한 내용은 [고급 캠페인 설정을]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/advanced_campaign_settings/#fcm-priority) 참조하세요.

