---
nav_title: 침묵 푸시 알림
article_title: FireOS용 무음 푸시 알림
platform: FireOS
page_order: 3

page_type: reference
description: "이 참조 문서에서는 무음 FireOS 푸시 알림을 보내는 방법과 무음 푸시 알림이 더 나을 수 있는 잠재적 사용 사례에 대해 설명합니다."
channel: push

---

# 조용한 푸시 알림

> 무음 알림을 사용하면 중요한 이벤트가 발생할 때 백그라운드에서 앱에 알림을 보낼 수 있습니다. 새로운 인스턴트 메시지를 전달하거나, 잡지의 새로운 호를 발행하거나, 속보 알림을 보내거나, 사용자가 좋아하는 TV 프로그램의 최신 에피소드를 오프라인 시청을 위해 다운로드할 준비가 되어 있을 수 있습니다. 조용한 알림은 배경 가져오기 간의 지연이 허용되지 않을 수 있는 산발적이지만 즉시 중요한 콘텐츠에 적합합니다.

Silent notifications are available through the Braze [메시징 API][2]. 그들을 활용하려면 `send_to_sync` 플래그를 `true`로 설정하고 [Android 푸시 객체][3] 내에서 `title` 또는 `alert` 필드가 설정되지 않도록 해야 합니다. 그렇지 않으면 `send_to_sync`와 함께 사용할 때 오류가 발생합니다. 그러나 객체 내에 데이터 `extras`를 포함할 수 있습니다.

무음 알림은 대시보드 내에서도 사용할 수 있습니다. 조용한 알림을 보내려면 알림의 제목 및 본문 필드가 비어 있는지 확인하십시오. 그림과 같이:

![][6]

[2]: {{site.baseurl}}/api/endpoints/messaging/
[3]: {{site.baseurl}}/api/objects_filters/messaging/android_object/
[6]: {% image_buster /assets/img_archive/SilentPushExample.png %} "무음 푸시 알림 예제 -- Android"
