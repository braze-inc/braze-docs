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

> 위치 수집은 GPS 위치 데이터를 사용하여 앱을 열었을 때 사용자의 가장 최근 위치를 캡처합니다. 이 정보를 사용하여 정의된 위치에 있었던 사용자를 기준으로 데이터를 세그먼트화할 수 있습니다.

## 위치 추적 인에이블먼트하기

앱에서 위치 수집을 인에이블먼트하려면 사용 중인 플랫폼의 개발자 가이드를 참조하세요:

- [iOS]({{site.baseurl}}/developer_guide/analytics/tracking_location/?sdktab=swift)
- [Android]({{site.baseurl}}/developer_guide/analytics/tracking_location/?sdktab=android)
- [웹]({{site.baseurl}}/developer_guide/analytics/tracking_location/?sdktab=web)

일반적으로 모바일 앱은 기기의 GPS 칩과 기타 시스템(예: Wi-Fi 스캔)을 사용하여 사용자의 위치를 추적합니다. 웹 앱은 WPS(Wi-Fi 포지셔닝 시스템)를 사용하여 사용자의 위치를 추적합니다. 이러한 모든 플랫폼에서는 사용자가 위치 추적에 옵트인해야 합니다. 위치 추적 데이터의 정확도는 사용자의 기기에 Wi-Fi가 인에이블먼트되어 있는지 여부에 따라 영향을 받을 수 있습니다. Android 사용자는 다른 위치 모드를 선택할 수도 있습니다. '배터리 저장' 또는 '기기 전용' 모드에 있는 사용자는 부정확한 데이터를 얻을 수 있습니다.

### IP 주소별 소프트웨어 개발 키트 사용자 위치

2024년 11월 26일부터 Braze는 첫 번째 소프트웨어 개발 키트 세션이 시작될 때부터 IP 주소를 사용하여 지리적으로 위치한 국가의 사용자 위치를 감지합니다. 

그 전에는 소프트웨어 개발 키트 사용자를 생성하는 동안과 첫 번째 세션이 진행되는 동안 Braze는 기기 로캘의 국가 코드를 사용했습니다. 첫 번째 세션 시작을 처리한 후에만 사용자에게 더 안정적인 국가를 설정하는 데 IP 주소가 사용됩니다. 즉, 첫 번째 세션 시작이 처리된 후 두 번째 세션부터 사용자 국가가 더 정확하게 설정되었습니다.

이제 Braze는 IP 주소를 사용하여 소프트웨어 개발 키트를 통해 생성된 고객 프로필의 국가 값을 설정하며, IP 기반 국가 설정은 첫 번째 세션 중과 이후에도 사용할 수 있습니다.

## 위치 타겟팅

위치 추적 데이터와 세그먼트를 사용하여 위치 기반 캠페인과 전략을 설정할 수 있습니다. 예를 들어 특정 지역에 거주하는 사용자를 대상으로 프로모션 캠페인을 진행하거나 규제가 더 엄격한 지역의 사용자를 제외할 수 있습니다.

위치 세그먼트 생성에 대한 자세한 내용은 위치 [타겟팅을]({{site.baseurl}}/user_guide/engagement_tools/segments/location_targeting/) 참조하세요.

## 기본 위치 속성 하드 설정하기

API의 [`users/track` 엔드포인트를]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) 사용하여 표준 속성을 업데이트할 수도 있습니다. [`current_location`]({{site.baseurl}}/api/objects_filters/user_attributes_object/) 표준 속성을 업데이트할 수도 있습니다. 예를 들면 다음과 같습니다:

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

## 자주 묻는 질문

### Braze는 언제 위치 데이터를 수집하나요?

Braze는 애플리케이션이 포그라운드에서 열려 있을 때만 위치를 수집합니다. 결과적으로 `Most Recent Location` 필터는 사용자가 마지막으로 애플리케이션을 연 위치(세션 시작이라고도 함)를 기준으로 사용자를 타겟팅합니다.

또한 다음과 같은 뉘앙스도 염두에 두어야 합니다:

- 위치가 비활성화되어 있으면 `Most Recent Location` 필터에 마지막으로 기록된 위치가 표시됩니다.
- 프로필에 위치가 저장된 적이 있는 사용자는 그 이후 위치 추적을 옵트아웃했더라도 `Location Available` 필터를 사용할 수 있습니다.

### 가장 최근 기기 로캘과 가장 최근 위치 필터의 차이점은 무엇인가요?

`Most Recent Device Locale` 은 사용자의 기기 설정에서 제공됩니다. 예를 들어 iPhone 사용자의 경우 기기의 **설정** > **일반** > **언어 & 지역에** 표시됩니다. 이 필터는 날짜 및 주소와 같은 언어 및 지역 서식을 캡처하는 데 사용되며 `Most Recent Location` 필터와는 독립적입니다.

`Most Recent Location` 은 기기의 마지막으로 알려진 GPS 위치입니다. 세션 시작 시 업데이트되며 사용자 프로필에 저장됩니다.

### 사용자가 위치 추적을 옵트인하면 이전 위치 데이터가 Braze에서 삭제되나요?

아니요. 사용자가 프로필에 위치를 저장한 적이 있는 경우 나중에 위치 추적을 옵트아웃하더라도 해당 데이터는 자동으로 삭제되지 않습니다.

