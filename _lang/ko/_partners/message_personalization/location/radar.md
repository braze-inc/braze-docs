---
nav_title: Radar
article_title: Radar
alias: /partners/radar/
description: "이 참조 문서에서는 iOS 및 Android 앱에 위치 컨텍스트 및 추적 기능을 추가하기 위한 Braze와 지오펜싱 플랫폼인 Radar 간의 파트너십에 대해 설명합니다."
page_type: partner
search_tag: Partner

---

# Radar

> [Radar](https://www.onradar.com/)는 선도적인 지오펜싱 및 위치 추적 플랫폼입니다. Radar 플랫폼에는 세 가지 핵심 제품이 있습니다. [지오펜스](https://radar.io/product/geofencing), [여행 추적](https://radar.io/product/trip-tracking) 및 [지리적 API](https://radar.io/product/api)가 이에 해당합니다. Combining the Braze industry-leading engagement platform and Radar's industry-leading geofencing capabilities allows you to drive revenue and loyalty through a wide range of location-based product and service experiences. 여기에는 픽업 및 배송 추적, 위치 트리거 알림, 상황에 맞는 개인화, 위치 확인, 매장 찾기, 주소 자동 완성 등이 포함됩니다.

_This integration is maintained by Radar._

## 통합 정보

Braze와 Radar의 통합을 통해 풍부한 퍼스트파티 위치 데이터로 정교한 위치 기반 캠페인 트리거를 활용하고 고객 프로필을 보강할 수 있습니다. 레이더 지오펜스 또는 여행 추적 이벤트가 생성되면 사용자 지정 이벤트와 사용자 속성이 실시간으로 Braze로 전송됩니다. 이러한 이벤트와 속성을 사용하여 위치 기반 캠페인을 트리거하고, 라스트 마일 픽업 및 배송 작업을 강화하고, 차량 및 배송 물류를 모니터링하거나, 위치 패턴을 기반으로 사용자 세그먼트를 구축할 수 있습니다. 

또한, Radar 지리적 API를 활용하여 [연결된 콘텐츠]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/)를 통해 마케팅 캠페인을 강화하거나 개인화할 수 있습니다. 

## 필수 조건

| 요구 사항 | 설명 |
|---|---|
| 레이더 계정 | 이 파트너십을 이용하려면 Radar 계정이 필요합니다. |
| Braze REST API 키 | `users.track` 권한이 있는 Braze REST API 키. <br><br> Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다. |
| 앱 식별자 | [앱 식별자]({{site.baseurl}}/api/identifier_types/?tab=app%20ids)는 Braze 대시보드의 **설정** > **API 키**에서 찾을 수 있습니다. |
| iOS API 키<br>Android API 키 | 이러한 API 키는 Braze 대시보드의 **설정** > **앱 설정**에서 찾을 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 통합

Braze와 Radar SDK 간에 데이터를 매핑하려면 두 시스템에서 동일한 사용자 ID 또는 사용자 별칭을 설정해야 합니다. 이 작업은 Braze SDK의 `changeUser()` 메서드와 Radar SDK의 `setUserId()` 메서드를 사용하여 수행할 수 있습니다.

통합을 활성화하려면 다음과 같이 하세요:

1. Radar의 [통합](https://radar.com/documentation/integrations) 페이지에서 Braze를 찾습니다.
1. **활성화됨**을 **예**로 설정합니다.
3. 앱 식별자와 API 키를 붙여넣습니다.

{% alert note %}
테스트 환경과 라이브 환경에 대해 별도의 API 키를 설정할 수 있습니다.
{% endalert %}

{:start="4"}
4\. Braze 엔드포인트를 선택합니다.
5\. 이벤트 또는 이벤트 속성 필터링을 입력하여 관련 데이터만 참여 마케팅을 위해 Braze로 전송되도록 합니다. Radar 이벤트가 생성될 때마다 Radar는 커스텀 이벤트와 사용자 속성을 Braze로 전송합니다. iOS 기기의 이벤트는 iOS API 키를 사용하여 전송되며, Android 기기의 이벤트 및 사용자 속성은 Android API 키를 사용하여 전송됩니다.

{% alert note %}
기본적으로 Radar `userId`는 로그인한 사용자의 경우 Braze `external_id`로 매핑됩니다. 그러나 Radar `metadata.brazeAlias` 또는 `metadata.brazeExternalId`를 설정하여 로그아웃한 사용자를 추적하거나 커스텀 매핑을 지정할 수 있습니다. `metadata.brazeAlias`를 설정한 경우, Braze에 라벨 `radarAlias`와 함께 일치하는 별칭도 추가해야 합니다.
{% endalert %}

## 이벤트 및 속성 기반 사용 사례

사용자 지정 이벤트와 사용자 속성을 사용하여 위치 기반 세그먼트를 구축하거나 위치 기반 캠페인을 트리거할 수 있습니다.

### 도로변 픽업에 대한 스토어 도착 알림 트리거 

사용자가 도로변 픽업을 위해 스토어에 도착하면 도착 안내와 함께 푸시 알림을 보냅니다.

!["도착_at_trip_destination" 사용자 지정 이벤트가 발생하고 "trip_metadata"가 "curbside"와 같을 때 캠페인이 전달된다는 것을 보여주는 액션 기반 배달 캠페인입니다.]({% image_buster /assets/img_archive/radar-campaign.png %})

### 최근 스토어 방문자의 잠재 고객 세그먼트 구축

예를 들어, 구매 여부에 관계없이 지난 7일 이내에 스토어를 방문한 모든 사용자를 타겟팅할 수 있습니다.

!['radar_geofence_tags'에 my_store 값이 포함되어 있고 'radar_updated_at;이 7일 이전인 세그먼트.]({% image_buster /assets/img_archive/radar-segment.png %})

## 연결된 콘텐츠

다음 예는 디지털 오퍼로 주변 사용자를 매장으로 유도하는 프로모션을 실행하는 방법을 보여줍니다. 

![An Android image of a Connected Content push message that displays "New In Store Deals, Walmart and target near you".]({% image_buster /assets/img/radar_example.png %}){: style="float:right;max-width:30%;border:0;"}

시작하려면 요청 URL 내에서 사용할 수 있는 Radar의 게시 가능한 API 키가 준비되어 있어야 합니다.

그런 다음, `connected_content` 태그 내에서 [장소 검색 API](https://radar.io/documentation/api#search-places)에 대한 GET 요청을 수행합니다. 장소 검색 API는 장소, 체인점, 카테고리에 대한 위치 데이터베이스로 전 세계에 대한 종합적인 시각을 제공하는 [레이더 장소](https://radar.io/documentation/places) 데이터베이스를 기반으로 주변 위치를 반환합니다.

다음 코드 스니펫은 API 호출에서 Radar가 JSON 오브젝트로 반환하는 내용의 예제입니다.

```json
{
  "meta": {
    "code": 200
  },
  "places": [
    {
      "_id": "5dc9b0fd2004860034bf2b06",
      "name": "Target",
      "location": {
        "type": "Point",
        "coordinates": [
          -74.42653983613333,
          40.548302893822985
        ]
      },
      "categories": [
        "shopping-retail",
        "department-store"
      ],
      "chain": {
        "slug": "target",
        "name": "Target",
        "domain": "target.com"
      }
    },
    {
      "_id": "5dc9b3d82004860034bfec54",
      "name": "Walmart",
      "location": {
        "type": "Point",
        "coordinates": [
          -74.44121885326864,
          40.554603296187224
        ]
      },
      "categories": [
        "shopping-retail"
      ],
      "chain": {
        "slug": "walmart",
        "name": "Walmart",
        "domain": "walmart.com"
      }
    }
  ]
}
```

연결된 콘텐츠 타겟팅 및 개인화된 Braze 메시지를 구성하려면 API 요청 URL의 `near` 매개변수에 대한 입력으로 Braze `most_recent_location` 속성을 활용할 수 있습니다. `most_recent_location` 속성은 Radar 이벤트 통합을 통해 또는 Braze SDK를 통해 직접 수집됩니다.

다음 예제에서는 Target 및 Walmart 위치에 대해 레이더 체인 필터링이 적용되고 주변 위치의 검색 반경이 2km로 설정되어 있습니다.

{% raw %}
```
{% connected_content https://api.radar.io/v1/search/places?radius=2000&near={{${most_recent_location}.latitude}},{{${most_recent_location}.longitude}}&chains=target,walmart&limit=5 :method get :headers {"Authorization": "<yourRadarPublishableKey>"} :content_type application/json :save nearbyplaces %}
```
{% endraw %}

`connect_content` 태그에서 볼 수 있듯이 JSON 오브젝트는 URL 뒤에 `:save nearbyplaces`를 추가하여 로컬 변수 `nearbyplaces`에 저장됩니다.
{% raw %}`{{nearbyplaces.places}}`{% endraw%}를 참조하여 출력의 형태를 테스트할 수 있습니다.

사용 사례를 종합하면 캠페인의 구문은 다음과 같습니다. 다음 코드는 `nearbyplaces.places` 오브젝트를 반복하여 고유 값을 추출하고 사람이 읽을 수 있는 적절한 구분 기호를 사용하여 메시지를 연결합니다.

{% raw %}
```
{% connected_content https://api.radar.io/v1/search/places?radius=2000&near={{${most_recent_location}.latitude}},{{${most_recent_location}.longitude}}&chains=target,walmart&limit=5 :method get :headers {"Authorization": "<yourRadarPublishableKey>"} :content_type application/json :save nearbyplaces %}
{% if nearbyplaces.**http_status_code** != 200 %}
{% abort_message('Connected Content returned a non-200 http status code') %}
{% endif %}
{% if nearbyplaces.meta.code != 200 %}
{% abort_message('Connected Content returned a non-200 meta code') %}
{% endif %}
{% if nearbyplaces.places.size == 0 %}
{% abort_message('Connected Content returned no nearby places') %}
{% else %}
{% assign delimiter = ", " %}
{% assign names = nearbyplaces.places | map: 'name' | uniq %}
{% if names.size == 2 %}
{{ names | join: ' and ' }} 
{% elsif names.size > 2 %}
{% assign names_final_str = "" %}
{% for name in names %}
{% if forloop.first == true %}
{% assign names_final_str = names_final_str  | append: name %}
{% elsif forloop.last == true %}
{% assign names_final_str = names_final_str | append: ", and "  | append: name %}
{% else %}
{% assign names_final_str = names_final_str | append: delimiter  | append: name %}
{% endif %}
{% endfor %}
{{ names_final_str }}
{% else %}
{{ names }} 
{% endif %}
near you!
```
{% endraw %}

{% alert tip %}
연결된 콘텐츠에서 활용할 수 있는 모든 Radar API는 [Radar 설명서](https://radar.io/documentation/api)를 참조하세요.
{% endalert %}


