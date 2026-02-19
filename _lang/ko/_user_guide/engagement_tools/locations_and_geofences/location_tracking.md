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

일반적으로 모바일 앱은 기기의 GPS 칩과 기타 시스템(예: Wi-Fi 스캔)을 사용하여 사용자의 위치를 추적합니다. 웹 앱은 WPS(Wi-Fi 포지셔닝 시스템)를 사용하여 사용자의 위치를 추적합니다. 이러한 모든 플랫폼은 사용자가 위치 추적에 옵트인해야 합니다. 사용자의 장치에서 Wi-Fi가 활성화되어 있는지 여부에 따라 위치 추적 데이터의 정확성이 영향을 받을 수 있습니다. Android 사용자는 다른 위치 모드를 선택할 수도 있습니다. '배터리 절약' 또는 '기기 전용' 모드를 사용하는 사용자는 부정확한 데이터를 가질 수 있습니다.

### IP 주소별 SDK 사용자 위치

Braze는 첫 번째 소프트웨어 개발 키트 세션이 시작될 때의 IP 주소를 사용하여 지리적으로 위치한 국가의 사용자 위치를 감지합니다. 

이전에는 Braze에서 소프트웨어 개발 키트 사용자를 생성하는 동안과 첫 번째 세션이 진행되는 동안 기기 로캘의 국가 코드를 사용했습니다. 첫 번째 세션 시작을 처리한 후에만 IP 주소가 사용되어 사용자의 더 신뢰할 수 있는 국가를 설정합니다. 즉, 첫 번째 세션 시작이 처리된 후 두 번째 세션부터 사용자 국가가 더 정확하게 설정되었습니다.

이제 Braze는 IP 주소를 사용하여 소프트웨어 개발 키트를 통해 생성된 고객 프로필의 국가 값을 설정하며, IP 기반 국가 설정은 첫 번째 세션 중 및 이후에 사용할 수 있습니다.

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

## 비콘 및 지오펜스에 대한 파트너십 지원

기존의 비콘 또는 지오펜스 지원과 타겟팅 및 메시징 기능을 결합하면 사용자의 물리적 행동에 대한 더 많은 정보를 얻을 수 있으므로 그에 맞는 메시지를 보낼 수 있습니다. 일부 파트너와 함께 위치 추적 기능을 활용할 수 있습니다: 

- [Radar]({{site.baseurl}}/partners/message_personalization/location/radar/)
- [Infillion]({{site.baseurl}}/partners/message_personalization/location/infillion/)
- [Foursquare]({{site.baseurl}}/partners/message_personalization/location/foursquare/)

## Frequently asked questions

### When does Braze collect location data?

Braze only collects location when the application is open in the foreground. As a result, our `Most Recent Location` filter targets users based upon where they last opened the application (also referred to as session start).

You should also keep the following nuances in mind:

- 위치가 비활성화되어 있으면 `Most Recent Location` 필터에 마지막으로 기록된 위치가 표시됩니다.
- 프로필에 위치가 저장된 적이 있는 사용자는 그 이후 위치 추적을 옵트아웃했더라도 `Location Available` 필터를 사용할 수 있습니다.

### What's the difference between the Most Recent Device Locale and Most Recent Location filters?

The `Most Recent Device Locale` comes from the user's device settings. 예를 들어 iPhone 사용자의 경우 기기의 **설정** > **일반** > **언어 & 지역에** 표시됩니다. This filter is used to capture language and regional formatting, such as dates and addresses, and is independent of the `Most Recent Location` filter.

The `Most Recent Location` is the last known GPS location of the device. This is updated on session start and is stored on the user's profile.

### 사용자가 위치 추적을 옵트인하면 이전 위치 데이터가 Braze에서 삭제되나요?

아니요. 사용자가 프로필에 위치를 저장한 적이 있는 경우 나중에 위치 추적을 옵트아웃해도 해당 데이터는 자동으로 삭제되지 않습니다.

## 문제 해결

### 사용 가능한 위치가 없는 사용자

Braze는 소프트웨어 개발 키트를 통해 기본값으로 사용자의 가장 최근 위치를 캡처합니다. 일반적으로 "최근 위치"는 사용자가 가장 최근에 앱을 사용한 위치를 의미합니다. Braze 백그라운드 위치 데이터를 전송하면 더 세분화된 데이터를 사용할 수 있습니다.

사용 가능한 위치가 없는 경우 두 가지 빠른 확인을 통해 데이터 수집 및 날짜 전송을 확인할 수 있습니다.

#### 데이터 수집

앱이 위치 데이터를 수집하고 있는지 확인합니다:

- iOS의 경우, 이는 사용자가 사용자 여정의 어느 시점에서 메시지를 통해 위치 데이터 공유에 옵트인한다는 의미입니다. 
- Android의 경우 앱 설치 시 앱이 미세 또는 거친 위치 권한을 요청하는지 확인합니다.

사용자 위치 데이터가 Braze로 전송되고 있는지 확인하려면 **위치 사용 가능** 필터를 사용하세요. 이 필터를 사용하면 '가장 최근 위치'를 가진 사용자의 비율을 확인할 수 있습니다.

!['사용 가능한 위치' 필터를 사용하는 '테스트 위치' 세그먼트입니다.]({% image_buster /assets/img_archive/trouble7.png %})

#### 데이터 전송

개발자가 위치 데이터를 Braze에 전달하고 있는지 확인하세요. 일반적으로 위치 데이터 전달은 사용자가 권한을 부여한 후 SDK에서 자동으로 처리되지만, 개발자가 Braze에서 위치 추적을 비활성화했을 수 있습니다. 위치 추적에 대한 자세한 내용은 다음에서 확인할 수 있습니다:
- [Android]({{site.baseurl}}/developer_guide/analytics/tracking_location?sdktab=android)
- [iOS]({{site.baseurl}}/developer_guide/analytics/tracking_location?sdktab=swift)
- [Web]({{site.baseurl}}/developer_guide/analytics/tracking_location?sdktab=web)