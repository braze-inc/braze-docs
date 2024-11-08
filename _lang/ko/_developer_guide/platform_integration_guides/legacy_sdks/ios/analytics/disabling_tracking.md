---
nav_title: iOS SDK 추적 비활성화하기
article_title: iOS의 SDK 추적 비활성화
platform: iOS
page_order: 8
description: "이 문서는 iOS 애플리케이션에 대한 데이터 수집을 비활성화하는 방법을 보여줍니다."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# iOS의 데이터 수집 비활성화

데이터 프라이버시 규정을 준수하기 위해 [`disableSDK`](http://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#a8d3b78a98420713d8590ed63c9172733) 메서드를 사용하여 iOS SDK에서 데이터 추적 활동을 완전히 중지할 수 있습니다. 이 방법을 사용하면 모든 네트워크 연결이 취소되고 Braze SDK가 서버로 데이터를 전달하지 않습니다. 나중에 데이터 수집을 재개하려면 향후 [`requestEnableSDKOnNextAppRun`](http://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#a781078a40a3db0de64ac82dcae3b595b) 메서드를 사용하여 데이터 수집을 재개할 수 있습니다.

또한 [`wipeDataAndDisableForAppRun`](http://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#ac8d580f60ec0608cd91240a8a3aa23a3) 메서드를 사용하여 기기에 저장된 모든 클라이언트 측 데이터를 완전히 지울 수도 있습니다.

사용자가 주어진 기기에서 제공업체의 모든 앱을 제거하지 않는 한, `wipeDataAndDisableForAppRun()` 호출 후 다음에 Braze SDK 및 앱을 실행하면 서버가 기기 식별자(IDFV)를 통해 해당 사용자를 다시 식별하게 됩니다. 모든 사용자 데이터를 완전히 제거하려면 `wipeDataAndDisableForAppRun` 호출을 Braze [REST API]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-delete-endpoint)를 통해 서버의 데이터를 삭제하는 요청과 결합해야 합니다.

## iOS SDK v5.7.0 이상
iOS SDK v5.7.0 이상을 사용하는 기기의 경우, [IDFV 수집을 비활성화]({{site.baseurl}}/developer_guide/platform_integration_guides/legacy_sdks/ios/initial_sdk_setup/other_sdk_customizations/#optional-idfv-collection---swift/)할 때 [`wipeData`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/wipedata())를 호출해도 서버가 기기 식별자(IDFV)를 통해 해당 사용자를 다시 식별하지 않습니다.