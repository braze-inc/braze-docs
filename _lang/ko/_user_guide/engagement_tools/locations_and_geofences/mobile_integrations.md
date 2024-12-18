---
nav_title: 모바일 통합
article_title: 지오펜스 모바일 통합
page_order: 2
page_type: reference
description: "이 참조 문서에서는 지오펜스 사용과 관련된 필수 모바일 통합에 대해 설명합니다."
tool: Location

---

# 모바일 통합

> 이 참조 문서에서는 지오펜스 사용과 관련된 필수 모바일 통합에 대해 설명합니다.

## 크로스 플랫폼 요구 사항

지오펜스 트리거 캠페인은 iOS와 Android에서 사용할 수 있습니다. 지오펜스를 지원하려면 다음 사항이 갖추어져 있어야 합니다:

1. 통합은 백그라운드 푸시 알림을 지원해야 합니다.
2. Braze 지오펜스 또는 위치 수집을 활성화해야 합니다.
3. iOS 버전 11 이상 기기의 경우 지오펜싱이 작동하려면 사용자가 항상 위치 액세스를 허용해야 합니다.

{% alert important %}
Braze SDK 버전 3.6.0부터는 기본적으로 Braze 위치 수집이 비활성화되어 있습니다. Android에서 활성화되어 있는지 확인하려면 `braze.xml` 에서 `com_braze_enable_location_collection` 가 `true` 로 설정되어 있는지 확인하세요.
{% endalert %}

## 지오펜스 구성

### 위도 및 경도

지오펜스의 지리적 중심입니다.

### 반경

지리적 중심에서 측정한 지오펜스의 반경(미터)입니다. 모든 지오펜스에 대해 최소 반경을 100~150미터로 설정하는 것이 좋습니다.

플랫폼에 따른 자세한 안내는 이 가이드를 참조하세요:
- [Android](https://developer.android.com/develop/sensors-and-location/location/geofencing#choose-the-optimal-radius-for-your-geofence)
- [iOS](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/LocationAwarenessPG/RegionMonitoring/RegionMonitoring.html#//apple_ref/doc/uid/TP40009497-CH9-SW5)

### 쿨다운

사용자는 개별 지오펜스에서 진입 또는 퇴장 전환을 수행한 후 지오펜스 트리거 알림을 받습니다. 전환이 발생한 후에는 해당 사용자가 해당 개별 지오펜스에서 동일한 전환을 다시 수행할 수 없는 사전 정의된 시간이 있습니다. 이 시간을 "쿨다운"이라고 하며 Braze에서 미리 정의합니다. 주요 목적은 불필요한 네트워크 요청을 방지하는 것입니다.

### 기술 파트너

예를 들어 일부 파트너와 함께 지오펜스를 활용할 수도 있습니다. 

- [Radar][12]
- [Foursquare][13]

## 자주 묻는 질문

지오펜스에 대해 자주 묻는 질문에 대한 답변은 지오펜스 [FAQ][5]를 참조하세요.

[3]: https://developers.google.com/android/reference/com/google/android/gms/location/package-summary
[4]: https://developer.apple.com/library/content/documentation/UserExperience/Conceptual/LocationAwarenessPG/RegionMonitoring/RegionMonitoring.html
[5]: {{site.baseurl}}/user_guide/engagement_tools/locations_and_geofences/faqs/#geofences
[12]: {{site.baseurl}}/partners/data_augmentation/contextual_location/radar/
[13]: {{site.baseurl}}/partners/data_augmentation/contextual_location/foursquare/

