---
nav_title: IDFV 수집
article_title: IDFV 수집
platform: Swift
page_type: reference
description: "이 참조 문서에서는 Swift SDK의 선택적 IDFV 필드를 수집하는 방법을 설명합니다."
page_order: 4

---

# IDFV 수집 

## 배경

이전 버전의 Braze iOS SDK에서는 공급업체 식별자(IDFV) 필드가 사용자의 기기 ID로 자동 수집됩니다. Swift SDK v5.7.0부터는 IDFV 필드를 선택적으로 비활성화하며, 대신 Braze에서 임의의 UUID를 기기 ID로 설정합니다. Swift SDK v7.0.0부터는 IDFV 필드가 기본적으로 수집되지 않으며, 대신 UUID가 기기 ID로 설정됩니다.

`useUUIDAsDeviceId` 기능은 기기 ID를 UUID로 설정하도록 [Swift SDK](https://github.com/braze-inc/braze-swift-sdk)를 구성합니다. 기존에는 iOS SDK가 Apple에서 생성한 IDFV 값과 동일한 기기 ID를 할당했습니다. iOS 앱에서 이 기능을 기본적으로 활성화하면 SDK를 통해 생성된 모든 새 사용자에게 UUID와 동일한 기기 ID가 할당됩니다.

여전히 IDFV를 별도로 수집하고 싶다면 [여기](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(identifierforvendor:))에서 설명한 대로 Swift SDK를 통해 수집할 수 있습니다.

## 고려 사항

### SDK 버전

Swift SDK v7.0.0 이상에서 `useUUIDAsDeviceId`를 활성화하면(기본값) 새로 생성되는 모든 사용자에게 임의의 기기 ID가 할당됩니다. 기존의 모든 사용자는 동일한 기기 ID 값을 유지하며, 이 값은 IDFV일 수 있습니다.

이 기능을 활성화하지 않으면 생성 시 계속해서 기기에 IDFV가 할당됩니다.

### 다운스트림 

**기술 파트너**: 이 기능을 활성화하면 Braze 기기 ID에서 IDFV 값을 파생하는 모든 기술 파트너는 더 이상 이 데이터에 액세스할 수 없습니다. 파트너 통합을 위해 기기에서 파생된 IDFV 값이 필요한 경우 이 기능을 true로 설정하는 것이 좋습니다.

**커런츠**: `useUUIDAsDeviceId`를 true로 설정하면 커런츠에서 전송된 기기 ID가 더 이상 IDFV 값과 같지 않습니다.

## 자주 묻는 질문

#### 이 변경 사항이 Braze의 기존 사용자에게 영향을 주나요?
아니요. 이 기능을 활성화하면 Braze의 사용자 데이터를 덮어쓰지 않습니다. 새로 생성한 기기 또는 `wipedata()`를 호출한 후에만 새 UUID 기기 ID가 생성됩니다.

#### 이 기능을 켠 후에 끌 수 있나요?
예. 이 기능은 사용자 재량으로 켜고 끌 수 있습니다. 이전에 저장된 장치 ID는 덮어쓰지 않습니다.

#### 다른 곳에서도 Braze를 통해 IDFV 값을 캡처할 수 있나요?
예. 선택적으로 Swift SDK를 통해 IDFV를 수집할 수 있습니다(기본적으로 수집은 비활성화됨). 
