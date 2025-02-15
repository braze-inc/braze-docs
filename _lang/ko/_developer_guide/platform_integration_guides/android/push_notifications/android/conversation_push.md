---
nav_title: 대화 푸시
article_title: 대화 푸시 for Android
platform: Android
page_order: 5.92
description: "이 애플리케이션은 Android 애플리케이션에서 Android 대화 푸시를 구현하는 방법을 다룹니다."
channel:
  - push

---

# 대화 푸시

> 이 애플리케이션은 Android 애플리케이션에서 Android 대화 푸시를 구현하는 방법을 다룹니다.

![]({% image_buster /assets/img/android/push/conversations_android.png %}){: style="float:right;max-width:35%;margin-left:15px;border: 0;"}

[사람과 대화 이니셔티브](https://developer.android.com/guide/topics/ui/conversations)는 휴대폰의 시스템 표면에서 사람과 대화의 개선을 목표로 하는 다년간의 Android 이니셔티브입니다. 이 우선순위는 모든 인구 통계학적 특성에 걸쳐 대부분의 Android 사용자에게 있어 다른 사람들과의 의사소통 및 상호작용이 여전히 가장 가치 있고 중요한 기능 영역이라는 사실에 기반합니다.

이 기능을 사용하기 위해 추가적인 통합이나 SDK 변경은 필요하지 않습니다. 대신, 최소 버전 요구 사항을 충족하지 않는 기기 또는 SDK는 표준 푸시 알림을 표시합니다.

## 사용 요구 사항

- 이 알림 유형에는 Braze Android SDK v15.0.0 이상 및 Android 11 이상 기기가 필요합니다. 
- 지원되지 않는 기기 또는 SDK에서는 표준 푸시 알림으로 대체됩니다.

이 기능은 Braze REST API를 통해서만 사용할 수 있습니다. 자세한 내용은 [Android 푸시 개체]({{site.baseurl}}/api/objects_filters/messaging/android_object#android-conversation-push-object)를 참조하세요.

