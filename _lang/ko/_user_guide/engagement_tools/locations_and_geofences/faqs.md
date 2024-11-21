---
nav_title: FAQ
article_title: 위치 및 지오펜스 FAQ
page_order: 4
page_type: FAQ
description: "이 참조 문서에서는 위치 추적 및 지오펜스 사용과 관련하여 자주 묻는 몇 가지 질문에 대해 설명합니다."
tool: Location

---

# 자주 묻는 질문

> 이 페이지에서는 위치 및 지오펜스에 대해 자주 묻는 질문에 대한 답변을 제공합니다.

## 위치 추적

### Braze는 언제 위치 데이터를 수집하나요?

Braze는 애플리케이션이 포그라운드에서 열려 있을 때만 위치를 수집합니다. 따라서 `Most Recent Location` 필터는 사용자가 마지막으로 애플리케이션을 연 위치(세션 시작이라고도 함)를 기준으로 사용자를 타겟팅합니다.

또한 다음과 같은 뉘앙스도 염두에 두어야 합니다:

- 위치를 비활성화하면 `Most Recent Location` 필터에 마지막으로 기록된 위치가 표시됩니다.
- 사용자가 프로필에 위치를 저장한 적이 있는 경우, 그 이후 위치 추적을 옵트아웃했더라도 `Location Available` 필터를 사용할 수 있습니다.

### 가장 최근 기기 로캘과 가장 최근 위치 필터의 차이점은 무엇인가요?

`Most Recent Device Locale` 은 사용자의 디바이스 설정에서 제공됩니다. 예를 들어 iPhone 사용자의 경우 **설정** > **일반** > **언어 및 지역** 아래에 표시됩니다. 이 필터는 날짜 및 주소와 같은 언어 및 지역 서식을 캡처하는 데 사용되며 `Most Recent Location` 필터와는 독립적입니다.

`Most Recent Location` 은 기기의 마지막으로 알려진 GPS 위치입니다. 세션 시작 시 업데이트되며 사용자의 프로필에 저장됩니다.

### 사용자가 위치 추적을 거부하면 이전 위치 데이터가 Braze에서 삭제되나요?

아니요! 사용자가 프로필에 위치를 저장한 적이 있는 경우, 나중에 위치 추적을 해제하더라도 해당 데이터는 자동으로 삭제되지 않습니다.

## 지오펜스

### 지오펜스와 위치 추적의 차이점은 무엇인가요?

Braze에서 지오펜스는 위치 추적과는 다른 개념입니다. 지오펜스는 특정 동작의 트리거로 사용됩니다. 지오펜스는 지리적 위치를 중심으로 설정된 가상의 경계입니다. 사용자가 이 경계에 들어오거나 나가면 메시지 전송과 같은 특정 작업을 트리거할 수 있습니다.

위치 추적은 사용자의 가장 최근 위치 데이터를 수집하고 저장하는 데 사용됩니다. 이 데이터는 `Most Recent Location` 필터를 기반으로 사용자를 세분화하는 데 사용할 수 있습니다. 예를 들어 `Most Recent Location` 필터를 사용하여 뉴욕에 있는 사용자에게 메시지를 보내는 등 특정 지역의 오디언스를 타겟팅할 수 있습니다.

### Braze 지오펜스는 얼마나 정확하나요?

Braze 지오펜스는 기기에서 사용할 수 있는 모든 위치 제공업체의 조합을 사용하여 사용자의 위치를 삼각 측량합니다. 여기에는 Wi-Fi, GPS, 셀룰러 타워가 포함됩니다.

일반적인 정확도는 20~50m 범위이며 최상의 정확도는 5~10m 범위입니다. 시골 지역에서는 정확도가 크게 저하되어 몇 킬로미터까지 올라갈 수 있습니다. Braze는 시골 지역에서는 반경이 더 큰 지오펜스를 만들 것을 권장합니다.

지오펜스의 정확도에 대한 자세한 내용은 [Android](https://developer.android.com/develop/sensors-and-location/location/geofencing) 및 [iOS](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/LocationAwarenessPG/RegionMonitoring/RegionMonitoring.html#//apple_ref/doc/uid/TP40009497-CH9-SW1) 설명서를 참조하세요.

### 지오펜스는 배터리 수명에 어떤 영향을 미치나요?

저희 지오펜싱 솔루션은 iOS 및 Android의 기본 지오펜스 시스템 서비스를 사용하며 정확도와 전력의 균형을 지능적으로 조정하여 동급 최고의 배터리 수명을 보장하고 기본 서비스가 개선됨에 따라 성능을 향상시킵니다.

### 지오펜스는 언제 활성화되나요?

Braze 지오펜스는 앱이 종료된 상태에서도 하루 종일 작동합니다. 정의되고 Braze 대시보드에 업로드되는 즉시 활성화됩니다. 그러나 사용자가 위치 추적을 사용 중지한 경우에는 지오펜스가 작동하지 않습니다.

지오펜스가 작동하려면 사용자가 기기에서 위치 서비스를 사용하도록 설정하고 앱에 자신의 위치에 액세스할 수 있는 권한을 부여해야 합니다. 사용자가 위치 추적을 비활성화하면 앱에서 사용자가 지오펜스에 들어오고 나갈 때를 감지할 수 없습니다.

### 지오펜스 데이터가 사용자 프로필에 저장되나요?

아니요, Braze는 사용자 프로필에 지오펜스 데이터를 저장하지 않습니다. 지오펜스는 Apple 및 Google 위치 서비스에 의해 모니터링되며, 사용자가 지오펜스를 트리거할 때만 Braze가 알림을 받습니다. 이 시점에서 관련된 모든 트리거 캠페인을 처리합니다.

### 지오펜스 내에 지오펜스를 설정할 수 있나요?

알림을 트리거하는 데 문제가 발생할 수 있으므로 서로 내부에 지오펜스를 설정하는 것은 피하는 것이 좋습니다.

[3]: https://developers.google.com/android/reference/com/google/android/gms/location/package-summary
[4]: https://developer.apple.com/library/content/documentation/UserExperience/Conceptual/LocationAwarenessPG/RegionMonitoring/RegionMonitoring.html
