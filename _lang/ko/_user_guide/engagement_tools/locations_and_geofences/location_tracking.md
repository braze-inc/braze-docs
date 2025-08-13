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

- [iOS]({{site.baseurl}}/developer_guide/analytics/tracking_location/?sdktab=swift)
- [Android]({{site.baseurl}}/developer_guide/analytics/tracking_location/?sdktab=android)
- [Web]({{site.baseurl}}/developer_guide/analytics/tracking_location/?sdktab=web)

일반적으로 모바일 앱은 디바이스의 GPS 칩 및 기타 시스템(예: Wi-Fi 스캔)을 사용하여 사용자의 위치를 추적합니다. 웹 앱은 사용자의 위치를 추적하기 위해 WPS(와이파이 위치 시스템)를 사용할 것입니다. 이 모든 플랫폼은 사용자가 위치 추적에 옵트인해야 합니다. 사용자의 장치에서 Wi-Fi가 활성화되어 있는지 여부에 따라 위치 추적 데이터의 정확성이 영향을 받을 수 있습니다. Android 사용자는 다른 위치 모드를 선택할 수도 있습니다. '배터리 절약' 또는 '기기 전용' 모드를 사용하는 사용자는 부정확한 데이터를 가질 수 있습니다.

### IP 주소별 SDK 사용자 위치

2024년 11월 26일부터 Braze는 첫 번째 SDK 세션이 시작될 때부터 IP 주소를 사용하여 지리적으로 위치한 국가의 사용자 위치를 감지합니다. 

이전에 Braze는 SDK 사용자 생성 시 및 첫 세션 동안 기기 로케일에서 국가 코드를 사용했습니다. 첫 번째 세션 시작을 처리한 후에만 IP 주소가 사용되어 사용자의 더 신뢰할 수 있는 국가를 설정합니다. 이것은 사용자 국가가 첫 번째 세션 시작이 처리된 후 두 번째 세션부터 더 높은 정확도로 설정되었음을 의미했습니다.

이제 Braze는 SDK를 통해 생성된 사용자 프로필의 국가 값을 설정하기 위해 IP 주소를 사용할 것이며, 이 IP 기반 국가 설정은 첫 번째 세션 중 및 이후에 사용할 수 있습니다.

## 위치 타겟팅

위치 추적 데이터와 세그먼트를 사용하여 위치 기반 캠페인과 전략을 설정할 수 있습니다. 예를 들어, 특정 지역에 거주하는 사용자들을 위한 프로모션 캠페인을 진행하거나 더 엄격한 규제가 있는 지역의 사용자를 제외할 수 있습니다.

Refer to [Location targeting]({{site.baseurl}}/user_guide/engagement_tools/segments/location_targeting/) for more information on creating a location segment.

## 기본 위치 속성 하드 설정

You can also use the [`users/track` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) in our API to update the [`current_location`]({{site.baseurl}}/api/objects_filters/user_attributes_object/) standard attribute. 예를 들면 다음과 같습니다:

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

- [Radar]({{site.baseurl}}/partners/message_personalization/location/radar/)
- [Infillion]({{site.baseurl}}/partners/message_personalization/location/infillion/)
- [Foursquare]({{site.baseurl}}/partners/message_personalization/location/foursquare/)

## 자주 묻는 질문

### When does Braze collect location data?

Braze only collects location when the application is open in the foreground. As a result, our `Most Recent Location` filter targets users based upon where they last opened the application (also referred to as session start).

You should also keep the following nuances in mind:

- If location is disabled, the `Most Recent Location` filter will show the last location recorded.
- If a user has ever had a location stored on their profile, they will qualify for the `Location Available` filter, even if they've opted out of location tracking since then.

### What's the difference between the Most Recent Device Locale and Most Recent Location filters?

The `Most Recent Device Locale` comes from the user's device settings. For example, this appears for iPhone users in their device at **Settings** > **General** > **Language & Region**. This filter is used to capture language and regional formatting, such as dates and addresses, and is independent of the `Most Recent Location` filter.

The `Most Recent Location` is the last known GPS location of the device. This is updated on session start and is stored on the user's profile.

### If a user opts out of location tracking, will their old location data be removed from Braze?

No. If a user has ever had a location stored on their profile, that data will not be automatically removed if they later opt out of location tracking.

