{% multi_lang_include developer_guide/prerequisites/android.md %} [푸시 알림도 설정해야]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android) 합니다.

## 무음 푸시 알림 설정하기

무음 알림은 Braze [메시징 API]({{site.baseurl}}/api/endpoints/messaging/)를 통해 사용할 수 있습니다. 이를 활용하려면 [Android 푸시 객체]({{site.baseurl}}/api/objects_filters/messaging/android_object/) 내에서 `send_to_sync` 플래그를 `true` 으로 설정하고 `title` 또는 `alert` 필드가 설정되어 있지 않은지 확인해야 하며, `send_to_sync` 과 함께 사용하면 오류가 발생할 수 있습니다. 그러나 오브젝트에 데이터 `extras`를 포함할 수 있습니다.

무음 알림은 대시보드 내에서도 사용할 수 있습니다. 무음 알림을 보내려면 표시된 대로 알림의 제목 및 본문 필드가 비어 있는지 확인합니다.

![]({% image_buster /assets/img_archive/SilentPushExample.png %} "Silent Push Notification Example -- Android")
