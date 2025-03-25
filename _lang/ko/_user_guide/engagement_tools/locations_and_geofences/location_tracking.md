---
nav_title: 위치 추적
article_title: 위치 추적
page_order: 0
page_type: reference
description: "이 참조 문서에서는 앱에서 위치 추적 및 위치 타겟팅을 사용하는 방법과 위치 추적을 지원하는 파트너에 대해 설명합니다."
tool: Location
search_rank: 2
---

# 위치 추적

> 위치 수집은 GPS 위치 데이터를 사용하여 앱을 열었을 때 사용자의 가장 최근 위치를 캡처합니다. 이 정보를 사용하여 정의된 위치에 있던 사용자를 기준으로 데이터를 세분화할 수 있습니다.

## 위치 추적 활성화

앱에서 위치 수집을 사용 설정하려면 사용 중인 플랫폼의 개발자 가이드를 참조하세요.

- [iOS][2]
- [Android][3]
- [웹][4]

일반적으로 모바일 앱은 디바이스의 GPS 칩 및 기타 시스템(예: Wi-Fi 스캔)을 사용하여 사용자의 위치를 추적합니다. 웹 앱은 사용자의 위치를 추적하기 위해 WPS(와이파이 위치 시스템)를 사용할 것입니다. 이 모든 플랫폼은 사용자가 위치 추적에 옵트인해야 합니다. 사용자의 장치에서 Wi-Fi가 활성화되어 있는지 여부에 따라 위치 추적 데이터의 정확성이 영향을 받을 수 있습니다. Android 사용자는 다른 위치 모드를 선택할 수도 있습니다. '배터리 절약' 또는 '기기 전용' 모드를 사용하는 사용자는 부정확한 데이터를 가질 수 있습니다.

### IP 주소별 SDK 사용자 위치

2024년 11월 26일부터 Braze는 첫 번째 SDK 세션이 시작될 때부터 IP 주소를 사용하여 지리적으로 위치한 국가의 사용자 위치를 감지합니다. 

이전에 Braze는 SDK 사용자 생성 시 및 첫 세션 동안 기기 로케일에서 국가 코드를 사용했습니다. 첫 번째 세션 시작을 처리한 후에만 IP 주소가 사용되어 사용자의 더 신뢰할 수 있는 국가를 설정합니다. 이것은 사용자 국가가 첫 번째 세션 시작이 처리된 후 두 번째 세션부터 더 높은 정확도로 설정되었음을 의미했습니다.

이제 Braze는 SDK를 통해 생성된 사용자 프로필의 국가 값을 설정하기 위해 IP 주소를 사용할 것이며, 이 IP 기반 국가 설정은 첫 번째 세션 중 및 이후에 사용할 수 있습니다.

## 위치 타겟팅

위치 추적 데이터와 세그먼트를 사용하여 위치 기반 캠페인과 전략을 설정할 수 있습니다. 예를 들어, 특정 지역에 거주하는 사용자들을 위한 프로모션 캠페인을 진행하거나 더 엄격한 규제가 있는 지역의 사용자를 제외할 수 있습니다.

위치 세그먼트 생성에 대한 자세한 내용은 위치 [타겟팅][1]을 참조하세요.

## 기본 위치 속성 하드 설정

API의 [`users/track` 엔드포인트][8]를 사용하여 표준 속성을 업데이트할 수도 있습니다. [`current_location`][9] 표준 어트리뷰트를 업데이트할 수도 있습니다. 예를 들면 다음과 같습니다:

```
https://[your_braze_rest_endpoint]/users/track
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "attributes": [ 
 	{
 	  "external_id" : "XXX",
 	  "current_location" : {"longitude":-0.118092, "latitude": 51.509865}
      }
   ]
}
```

## 파트너십 지원을 위한 비콘 및 지오펜스

기존의 비콘 또는 지오펜스 지원을 타겟팅 및 메시징 기능과 결합하면 사용자의 물리적 행동에 대한 더 많은 정보를 얻을 수 있어 그에 따라 메시지를 보낼 수 있습니다. 당신은 일부 파트너와 함께 위치 추적을 활용할 수 있습니다: 

- [Radar][6]
- [Infillion][10]
- [Foursquare][7]

## 자주 묻는 질문

위치 관련 자주 묻는 질문에 대한 답변은 위치 [FAQ에서][11] 확인하세요.

[1]: {{site.baseurl}}/user_guide/engagement_tools/segments/location_targeting/
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/location_tracking/
[3]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/location_tracking/
[4]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/location_tracking/
[6]: {{site.baseurl}}/partners/data_augmentation/contextual_location/radar/
[7]: {{site.baseurl}}/partners/data_augmentation/contextual_location/foursquare/
[8]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/
[9]: {{site.baseurl}}/api/objects_filters/user_attributes_object/
[10]: {{site.baseurl}}/partners/message_personalization/location/infillion/
[11]: {{site.baseurl}}/user_guide/engagement_tools/locations_and_geofences/faqs/#locations
