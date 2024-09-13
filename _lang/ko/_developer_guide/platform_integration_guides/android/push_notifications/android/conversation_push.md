---
nav_title: 대화 푸시
article_title: 대화 푸시 for Android
platform: Android
page_order: 5.92
description: "이 응용 프로그램은 Android 응용 프로그램에서 android 대화 푸시를 구현하는 방법을 다룹니다."
channel:
  - push

---

# 대화 푸시

> 이 응용 프로그램은 Android 응용 프로그램에서 android 대화 푸시를 구현하는 방법을 다룹니다.

![]({% image_buster /assets/img/android/push/conversations_android.png %}){: style="float:right;max-width:35%;margin-left:15px;border: 0;"}

[사람과 대화 이니셔티브][2]는 휴대폰의 시스템 표면에서 사람과 대화를 향상시키는 것을 목표로 하는 다년간의 Android 이니셔티브입니다. 이 우선순위는 모든 인구 통계학적 특성에 걸쳐 대부분의 Android 사용자에게 있어 다른 사람들과의 의사소통 및 상호작용이 여전히 가장 가치 있고 중요한 기능 영역이라는 사실에 기반합니다.

이 기능을 사용하기 위해 추가적인 통합 또는 소프트웨어 개발 키트 변경이 필요하지 않습니다. 최소 버전 요구 사항을 충족하지 않는 디바이스 또는 SDK는 대신 표준 푸시 알림을 표시합니다.

## 사용 요구 사항

- 이 알림 유형에는 Braze Android 소프트웨어 개발 키트 v15.0.0+ 및 Android 11+ 장치가 필요합니다. 
- 지원되지 않는 장치 또는 SDK는 표준 푸시 알림으로 대체됩니다.

이 기능은 Braze REST API를 통해서만 사용할 수 있습니다. 자세한 내용은 [Android 푸시 개체][1]를 참조하세요.

[1]: {{site.baseurl}}/api/objects_filters/messaging/android_object#android-conversation-push-object
[2]: https://developer.android.com/guide/topics/ui/conversations
