---
nav_title: 무음 푸시 알림
article_title: Android용 무음 푸시 알림
platform: Android
page_order: 3
description: "이 문서에서는 Android 애플리케이션에서 무음 푸시 알림을 구현하는 방법에 대해 설명합니다."
channel:
  - push

---

# Android용 무음 푸시 알림

> 무음 알림을 사용하면 중요한 이벤트가 발생할 때 백그라운드에서 앱에 알림을 보낼 수 있습니다. 전달할 새 인스턴트 메시지, 발행할 잡지 신간, 송출할 뉴스 속보 알림 또는 오프라인으로 시청할 수 있도록 다운로드할 준비가 된 사용자가 좋아하는 TV 프로그램의 최신 에피소드를 확인할 수 있습니다. 무음 알림은 백그라운드 가져오기 사이의 지연이 허용되지 않을 수도 있는 산발적이지만 바로 중요한 콘텐츠에 적합합니다.

## 무음 푸시 알림 설정하기

무음 알림은 Braze [메시징 API]({{site.baseurl}}/api/endpoints/messaging/)를 통해 사용할 수 있습니다. 이를 활용하려면 [Android 푸시 개체]({{site.baseurl}}/api/objects_filters/messaging/android_object/) 내에서 `send_to_sync` 플래그를 `true` 로 설정하고 `title` 또는 `alert` 필드가 설정되어 있지 않은지 확인해야 합니다( `send_to_sync`와 함께 사용하면 오류가 발생할 수 있으므로, 개체 내에 `extras` 데이터를 포함할 수 있음).

{% alert tip %}
[푸시 알림 메시지를 작성할]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message//?tab=android#step-4-compose-your-push-message) 때 공백 하나만 있는 메시지를 보내면 무음 Android 푸시 알림을 보낼 수 있습니다. 이 방법은 푸시 알림을 보내는 데 권장되는 방법은 **아니지만** 경우에 따라 유용할 수 있습니다.
{% endalert %}

