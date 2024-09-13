---
nav_title: SDK 추적 비활성화하기
article_title: Android 및 FireOS용 데이터 수집 비활성화하기
platform: 
  - Android
  - FireOS
page_order: 8
description: "이 문서에서는 Android 또는 FireOS 애플리케이션의 데이터 수집을 비활성화하는 방법을 설명합니다."

---

# SDK 추적 비활성화하기

> 이 문서에서는 Android 또는 FireOS 애플리케이션의 데이터 수집을 비활성화하는 방법을 설명합니다.

데이터 개인정보 보호 규정을 준수하기 위해 안드로이드 SDK에서 데이터 추적 활동을 완전히 중지할 수 있습니다. [`disableSDK()`][1]. 이 방법을 사용하면 모든 네트워크 연결이 취소되고 Braze SDK가 Braze 서버로 데이터를 전달하지 않습니다. 나중에 데이터 수집을 재개하려면 나중에 데이터 수집을 재개하려면 [`enableSDK()`][2] 메서드를 사용하여 데이터 수집을 재개할 수 있습니다.

또한 메서드 [`wipeData()`][3] 메서드를 사용하여 디바이스에 저장된 모든 클라이언트 측 데이터를 완전히 지울 수도 있습니다.

[1]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/disable-sdk.html
[2]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/enable-sdk.html
[3]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/wipe-data.html
