---
nav_title: "알림 옵션"
article_title: 안드로이드 알림 옵션
page_order: 2
page_type: reference
description: "이 참조 문서에서는 여러 안드로이드 알림 옵션과 이를 Braze 캠페인 내에서 최적으로 사용하는 방법을 다룹니다."

platform: Android
channel:
  - Push

---

# 알림 옵션

> 이것은 Braze를 통해 사용할 수 있는 일부 안드로이드 전용 푸시 알림 옵션입니다.

## 무음 알림

푸시 알림 메시지를 [작성할 때]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/?tab=android#step-4-compose-your-push-message), 제목 없이 안드로이드 푸시 메시지를 보낼 수 **없습니다**—하지만 대신 단일 공백을 입력할 수 있습니다. 메시지가 단일 공백만 포함하는 경우, 무음 푸시 알림으로 전송됩니다. 자세한 내용은 [무음 푸시 알림]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=android)을 참조하세요.

## 알림 그룹

메시지를 분류하고 사용자의 알림 트레이에 그룹화하려면 Braze를 통해 안드로이드의 알림 채널 기능을 활용할 수 있습니다.

먼저 안드로이드 푸시 캠페인을 생성한 후, **작성** 탭의 상단에서 **알림 채널** 드롭다운을 확인하세요.

\![]({% image_buster /assets/img_archive/notification_channel_dropdown.png %}){: style="max-width:60%;"}

드롭다운에서 알림 채널을 선택하세요. 알림 채널 설정이 작동하지 않을 경우를 대비하여 대체 채널도 선택해야 합니다.

여기에 나열된 [알림 채널]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/notification_channels/)이 없으면 알림 채널 ID를 사용하여 추가할 수 있습니다. 개발자에게 연락하여 알림 채널 ID가 무엇인지 확인하거나 필요에 따라 새 ID를 생성하도록 요청하세요. 

알림 채널에 알림 ID를 추가하려면 **알림 채널 관리**을 클릭하고 **알림 채널** 드롭다운 메뉴에서 필수 필드를 작성하세요. 알림 채널은 Braze 플랫폼에서 사용되기 전에 앱에서 정의되어야 합니다.

\![]({% image_buster /assets/img_archive/notification_channels.png %}){: style="max-width:80%;" }


