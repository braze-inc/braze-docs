---
nav_title: 인라인 이미지 푸시
article_title: Android용 인라인 이미지 푸시
platform: Android
page_order: 5.9
description: "이 참조 문서에서는 Android 애플리케이션에서 인라인 이미지 푸시를 구현하는 방법을 다룹니다."
channel:
  - push

---

# 인라인 이미지 푸시

![]({% image_buster /assets/img/android/push/inline_image_push_android_1.png %}){: style="float:right;max-width:30%;margin-left:15px;border: 0;"}

> 인라인 이미지 푸시를 사용하여 Android 푸시 알림에 더 큰 이미지를 표시하세요. 이 디자인을 사용하면 사용자가 이미지를 확대하기 위해 수동으로 푸시를 확장할 필요가 없습니다. 

이 기능을 사용하기 위해 추가적인 통합이나 SDK 변경이 필요하지 않습니다. 대신, 최소 버전 요구 사항을 충족하지 않는 기기 또는 SDK는 표준 큰 이미지 푸시 알림을 표시합니다.

## 사용 요구 사항

- 이 알림 유형에는 Braze Android SDK v10.0.0 이상 및 Android M 이상 기기가 필요합니다. 
- 지원되지 않는 기기 또는 SDK는 표준 큰 이미지 푸시 알림으로 대체됩니다.
- 일반 Android 푸시 알림과 달리 인라인 이미지 푸시 이미지는 3:2 화면 비율로 제공됩니다.

{% alert note %}
Android 12를 실행하는 기기는 커스텀 푸시 알림 스타일의 변경으로 인해 다르게 렌더링됩니다.
{% endalert %}

## 대시보드 설정

Android 푸시 메시지를 작성할 때 **알림 유형** 드롭다운에서 이 기능을 사용할 수 있습니다.

![푸시 캠페인 에디터에서 '알림 유형' 드롭다운의 위치(표준 푸시 미리보기 위)를 표시합니다.]({% image_buster /assets/img/android/push/android_inline_image_notification_type.png %})
