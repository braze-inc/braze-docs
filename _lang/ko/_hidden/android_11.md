---
nav_title: Android 11 업그레이드 가이드
article_title: Android 11 업그레이드 가이드
page_order: 9
platform: 
  - Android
  - FireOS
description: "이 참조 문서는 Android 11 SDK 업데이트를 다루며, 딥링킹, SDK 호환성 등과 같은 변경 사항을 강조합니다."
hidden: true
---

# Android 11 SDK 업그레이드 가이드

이 가이드는 Android 11(2020년 9월 8일 출시)에서 도입된 관련 변경 사항과 Braze Android SDK 통합을 위한 필수 업그레이드 단계를 설명합니다.

Android 11의 전체 마이그레이션 가이드는 [Android 개발자 설명서](https://developer.android.com/preview/migration)를 참조하세요.

## Braze SDK 호환성

Android 11(API 30)을 _대상으로 하는_ 모든 앱은 Braze 메시징 기능을 계속 사용하려면 [Braze Android SDK v8.1.0+][1]로 업그레이드해야 합니다.

{% alert important %}
Android 11의 API 변경으로 인해 Android 11을 타겟팅하는 앱이 Braze Android SDK v8.1.0+로 업그레이드되지 않으면 Braze UI 구성 요소에서 딥링킹 문제가 발생하고 커스텀 HTML 인앱 메시지가 제대로 표시되지 않습니다.
{% endalert %}

### 딥 링크

Android 11 이상(API 버전 30+)을 타겟팅하는 앱은 Braze 메시지 내에서 딥 링크를 계속 사용하려면 [Braze Android SDK v8.1.0][1]으로 업그레이드해야 합니다. Android 11 API 변경으로 인해 Android SDK v8.1.0 이상으로 업그레이드하지 않은 앱은 Braze 메시지(인앱 메시지 또는 콘텐츠 카드) 내에서 딥링크 문제를 겪게 됩니다.

### HTML 인-앱 메시지

Android 11 이상(API 버전 30+)을 타겟팅하는 앱은 커스텀 HTML 인앱 메시지를 계속 사용하려면 Braze Android SDK v8.1.0으로 업그레이드해야 합니다. Android 11 WebView 설정 변경으로 인해 Android 11 타겟 앱에서는 [Braze Android SDK v8.1.0][1]으로 업그레이드할 때까지 HTML 인앱 메시지가 제대로 표시되지 않습니다. 

### 위치 권한

위치 권한을 사용하는 앱은 위치 액세스를 요청할 때 Android의 [모범 사례](https://developer.android.com/preview/privacy/location#change-details)를 따라야 합니다. 이러한 위치 업데이트를 위해 Braze 통합에 대한 변경 사항이 필요하지 않습니다.

## Android 11 동작 변경 사항

### 한 번 허용 권한

사용자는 이제 위치 수집과 같은 권한을 일회성으로 부여할 수 있습니다(자세한 내용은 [Android 문서](https://developer.android.com/preview/privacy/location#one-time-access)를 참조하세요). 앱이 종료되거나 백그라운드에서 충분히 오래 있으면 해당 권한이 자동으로 취소됩니다. 앱은 향후 필요할 때 이 권한을 다시 요청해야 합니다. 위치 권한 요청을 위한 권장 흐름을 이미 따르는 앱은 일회성 권한을 지원합니다.

![][3]{: height="230px" }

### 백그라운드 위치 권한

Android 11은 앱이 먼저 포그라운드 위치 권한을 요청한 후, 앱이 백그라운드에 있을 때 다시 사용자에게 백그라운드 위치 권한을 요청할 수 있습니다.
지오펜스를 사용하는 고객은 앱이 Android의 백그라운드 위치 권한 수집 권장 사항을 따르는지 확인해야 합니다. 자세한 내용은 [Android 문서](https://developer.android.com/preview/privacy/location#background-location)를 참조하십시오.

[1]: https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#810
[3]: {% image_buster /assets/img/android/android-11-one-time-permission.svg %}
