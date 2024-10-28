---
nav_title: Android 12 업그레이드 가이드
article_title: Android 12 업그레이드 가이드
page_order: 9
permalink: "/android_12/"
layout: "dev_guide"
hidden: true
platform: 
  - Android
  - FireOS
description: "이 참조 문서는 Android 12 SDK 업데이트를 다루며, 딥링킹, SDK 호환성 등과 같은 변경 사항을 강조합니다."
---

# 안드로이드 12 SDK 업그레이드 가이드

이 가이드에서는 Android 12(2021)에 도입된 관련 변경 사항과 Braze Android SDK 통합에 필요한 업그레이드 단계에 대해 설명합니다.

Android 12 마이그레이션 가이드 전문은 [Android 개발자 설명서](https://developer.android.com/about/versions/12)를 참조하세요.

## Braze SDK 호환성

안드로이드 12를 타겟팅하는 경우, [Braze Android SDK v13.1.2 이상][1]을 사용해야 합니다. 아직 Android 12를 대상으로 하지 않는 경우에도 업그레이드를 권장합니다.

**Braze Android SDK를 업그레이드하지 않으면 어떻게 되나요?**

* Android의 [시스템 종료 대화 상자](https://developer.android.com/about/versions/12/behavior-changes-all#close-system-dialogs) 변경으로 인해 이전 버전의 Braze Android SDK는 Android 12를 실행하는 기기에서 푸시 알림을 수신할 때 경고를 기록합니다. 이 동작은 앱이 Android 12를 대상으로 하지 않는 경우에도 발생합니다.
* [구성 요소 내보내기](https://developer.android.com/about/versions/12/behavior-changes-12#exported), [보류 중인 의도](https://developer.android.com/about/versions/12/behavior-changes-12#pending-intent-mutability) 및 [알림 트램폴린](https://developer.android.com/about/versions/12/behavior-changes-12#notification-trampolines)의 변경 사항은 앱 컴파일 기능에 영향을 미치거나 Braze SDK가 초기화되지 않을 수 있습니다. 이 동작은 Android 12를 타겟팅하는 앱에서만 발생합니다.
* [사용자 지정 푸시 알림의](https://developer.android.com/about/versions/12/behavior-changes-12#custom-notifications) 변경으로 인해 새로운 [Android 인라인 이미지 푸시]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/inline_image_push/) 기능의 레이아웃이 변경되었습니다. 이 동작은 Android 12를 타겟팅하는 앱에서만 발생합니다.

[1]: https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#1312
