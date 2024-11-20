---
nav_title: 무음 푸시 알림
article_title: FireOS용 무음 푸시 알림
platform: FireOS
page_order: 3

page_type: reference
description: "이 참조 문서에서는 무음 FireOS 푸시 알림을 보내는 방법과 무음 푸시 알림이 더 유용한 잠재적 사용 사례를 설명합니다."
channel: push

---

# 조용한 푸시 알림

> 무음 알림을 사용하면 중요한 이벤트가 발생할 때 백그라운드에서 앱에 알림을 보낼 수 있습니다. 전달할 새 인스턴트 메시지, 발행할 잡지 신간, 송출할 뉴스 속보 알림 또는 오프라인으로 시청할 수 있도록 다운로드할 준비가 된 사용자가 좋아하는 TV 프로그램의 최신 에피소드를 확인할 수 있습니다. 무음 알림은 백그라운드 가져오기 사이의 지연이 허용되지 않을 수도 있는 산발적이지만 바로 중요한 콘텐츠에 적합합니다.

무음 알림은 Braze [메시징 API]({{site.baseurl}}/api/endpoints/messaging/)를 통해 사용할 수 있습니다. 이를 활용하려면 [Android 푸시 객체]({{site.baseurl}}/api/objects_filters/messaging/android_object/) 내에서 `send_to_sync` 플래그를 `true` 으로 설정하고 `title` 또는 `alert` 필드가 설정되어 있지 않은지 확인해야 하며, `send_to_sync` 과 함께 사용하면 오류가 발생할 수 있습니다. 그러나 오브젝트에 데이터 `extras`를 포함할 수 있습니다.

무음 알림은 대시보드 내에서도 사용할 수 있습니다. 무음 알림을 보내려면 표시된 대로 알림의 제목 및 본문 필드가 비어 있는지 확인합니다.

![]({% image_buster /assets/img_archive/SilentPushExample.png %} "무음 푸시 알림 예시 - 안드로이드")

