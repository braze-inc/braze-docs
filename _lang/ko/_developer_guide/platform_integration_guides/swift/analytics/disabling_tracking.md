---
nav_title: iOS SDK 추적 비활성화하기
article_title: iOS용 SDK 추적 비활성화하기
platform: Swift
page_order: 8
description: "이 문서는 Swift SDK에 대한 데이터 수집을 비활성화하는 방법을 보여줍니다."

---

# iOS SDK 추적 비활성화하기

> 데이터 프라이버시 규정을 준수하기 위해 Braze 인스턴스에서 [`enabled`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/enabled) 속성정보를 `false`로 설정하여 iOS SDK에서 데이터 추적 활동을 완전히 중지할 수 있습니다. 

`enabled`가 `false`로 설정되면 Braze SDK는 공용 API에 대한 모든 호출을 무시합니다. 또한 SDK는 네트워크 요청, 이벤트 처리 등과 같은 모든 진행 중인 작업을 취소합니다. 데이터 수집을 다시 시작하려면 [`enabled`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/enabled/)를 `true`로 설정합니다.

[`wipeData()`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/wipedata()) 메서드를 사용하여 사용자 기기에 로컬로 저장된 SDK 데이터를 완전히 지울 수도 있습니다. Swift SDK 버전 5.7.0 이하를 사용하거나 `useUUIDAsDeviceId`가 `false`로 설정되어 있는 경우 [`/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/)로 게시 요청을 수행해야 합니다. 공급업체 식별자(IDFV)가 기기 ID로 사용되기 때문입니다. Braze Swift 버전 7.0.0 이상에서는 SDK 및 `wipeData()` 메서드가 기기 ID에 대한 UUID를 무작위로 생성합니다.
