---
nav_title: 지오펜스 생성
article_title: 지오펜스 생성
page_order: 1
page_type: reference
description: "이 참조 문서에서는 지오펜스가 무엇인지, 지오펜스 이벤트를 생성하고 구성하는 방법을 다룹니다."
tool: 
  - Location
search_rank: 9
---

# 지오펜스

> 실시간 위치 제공의 핵심은 지오펜스 개념입니다. 지오펜스는 특정 글로벌 위치를 중심으로 반경을 결합한 위도와 경도로 표현되는 가상 지리적 영역입니다. 지오펜스는 건물 크기에서 전체 도시 크기까지 다양할 수 있습니다.

Braze 대시보드에서 지오펜스를 정의하고 사용자가 경계를 출입할 때 실시간으로 캠페인을 트리거하거나 몇 시간 또는 며칠 후에 후속 캠페인을 보낼 수 있습니다. 지오펜스에 들어오거나 나가는 사용자는 세분화 및 리타겟팅에 사용할 수 있는 새로운 사용자 데이터 레이어를 추가합니다.

## 개요

**오디언스** > **위치**에서 지오펜스를 관리합니다.

{% alert note %}
[이전 탐색]({{site.baseurl}}/navigation)을 사용하는 경우 **위치**를 **참여** 아래에서 찾을 수 있습니다.
{% endalert %}

지오펜스는 지오펜스 세트로 구성됩니다. 지오펜스 세트는 플랫폼 전반에서 사용자를 세그먼트하거나 참여시키는 데 사용할 수 있는 지오펜스 그룹입니다. 각 지오펜스 세트는 최대 10,000개의 지오펜스를 보유할 수 있습니다.

대시보드에서 무제한의 지오펜스를 생성하거나 업로드할 수 있으므로 마케팅 팀이 지오펜스 세트 및 캠페인을 설정할 때 지오펜스 수를 계산할 필요가 없습니다. Braze는 각 사용자를 위해 추적하는 지오펜스를 동적으로 다시 동기화하여 사용자에게 가장 관련성이 높은 지오펜스가 항상 사용 가능하도록 합니다.

- Android 앱은 한 번에 최대 100개의 지오펜스를 로컬에 저장할 수 있습니다. Braze는 앱당 로컬에 최대 20개의 지오펜스만 저장하도록 구성됩니다.
- iOS 기기는 앱당 한 번에 최대 20개의 지오펜스를 모니터링할 수 있습니다. Braze는 공간이 허용되는 경우 최대 20개의 위치를 모니터링합니다. 
- 사용자가 20개 이상의 지오펜스를 받을 자격이 있는 경우, Braze는 세션 시작/푸시 새로고침 시점에서 사용자와의 근접성을 기준으로 최대 위치를 다운로드합니다.
- 지오펜스가 올바르게 작동하려면 앱이 사용 가능한 모든 지오펜스 위치를 사용하지 않도록 해야 합니다.

## 지오펜스 세트 생성

### 세트를 수동으로 생성

**위치** 페이지에서 **\+ 지오펜스 세트 만들기**를 클릭하세요.

![사용자가 함부르크 공항의 지도에 반경 2,000미터를 그려 설정한 독일 공항의 지오펜스 세트.][1]

지오펜스 세트를 생성한 후에는 지도에 지오펜스를 그려서 수동으로 추가할 수 있습니다. 최적의 기능을 위해 반경 최소 200미터의 지오펜스를 만드는 것을 권장합니다. For more information on configurable options, refer to [Geofence configuration]({{site.baseurl}}/user_guide/engagement_tools/locations_and_geofences/mobile_integrations/).

### 대량 업로드를 통해 세트 생성 {#creating-geofence-sets-via-bulk-upload}

지오펜스는 `FeatureCollection` 유형의 GeoJSON 객체로 일괄 업로드할 수 있습니다. 각 개별 지오펜스는 기능 모음에서 `Point` 형식의 기하학 유형입니다. 각 기능의 속성에는 `"radius"` 키가 필요하며 각 지오펜스에 대해 선택적 `"name"` 키가 필요합니다. GeoJSON을 업로드하려면 **\+ 지오펜스 세트 만들기**를 클릭한 다음 **GeoJSON 업로드**를 클릭합니다.

다음 샘플은 NYC에 있는 Braze 본사와 맨해튼 남쪽에 있는 자유의 여신상을 지정하기 위한 두 개의 지오펜스를 지정하는 올바른 GeoJSON을 나타냅니다. 최적의 기능을 위해 반경이 최소 100미터인 지오펜스를 업로드하는 것을 권장합니다.

```
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [-73.992473, 40.755669]
      },
      "properties": {
        "radius": 200,
        "name": "Braze HQ"
      }
    },
    {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [-74.044468, 40.689225]
       },
      "properties": {
        "radius": 100,
        "name": "Statue of Liberty"
      }
    }
  ]
}
```

지오펜스를 만들 때 다음 사항을 염두에 두세요.

- GeoJSON의 `coordinates` 값은 [경도, 위도] 형식으로 작성됩니다.
- 업로드할 수 있는 최대 지오펜스 반경은 10,0000미터(약 100킬로미터 또는 62마일)입니다.

## 지오펜스 세트 업데이트

활성 사용자에게 Braze 소프트웨어 개발 키트는 세션 시작 시 하루에 한 번만 지오펜스를 요청합니다. 즉, 세션이 시작된 후 지오펜스 세트에 변경이 발생하면 세트가 처음 내려받아진 시점부터 24시간이 지나야 업데이트된 세트를 받을 수 있습니다.

비활성 사용자에게 사용자가 백그라운드 푸시를 활성화한 경우, Braze는 최신 위치를 기기로 가져오기 위해 24시간마다 한 번씩 무음 푸시를 보냅니다.

{% alert note %}
지오펜스가 기기에 로드되지 않으면 사용자가 해당 지역에 들어가도 지오펜스를 트리거할 수 없습니다.
{% endalert %}

### 개별 사용자 업데이트

개별 사용자의 지오펜스를 업데이트하는 것은 테스트할 때 유용할 수 있습니다. 지오펜스 세트를 업데이트하려면 **위치** 페이지 하단으로 이동하여 **지오펜스 다시 동기화**를 클릭하십시오. 그런 다음 업데이트하려는 사용자 `external_id` 또는 `email`을 입력하라는 메시지가 표시됩니다.

## 지오펜스 이벤트 사용

지오펜스가 구성되면 이를 사용하여 사용자와의 커뮤니케이션을 향상시키고 풍부하게 할 수 있습니다.

### 트리거링

캠페인 및 캔버스 트리거의 일부로 지오펜스 데이터를 사용하려면 전달 방법으로 **실행 기반 전달**을 선택하세요. 다음으로, `Trigger a Geofence`의 트리거 동작을 추가합니다. 마지막으로, 메시지에 대한 지오펜스 세트 및 지오펜스 전환 이벤트 유형을 선택하세요. 지오펜스 이벤트를 사용하여 캔버스를 통해 사용자들을 진전시킬 수도 있습니다.

![][2]

### 개인화

지오펜스 데이터를 사용하여 메시지를 개인화하려면 다음 Liquid 개인화 구문을 사용할 수 있습니다:

{% raw %}
* `{{event_properties.${geofence_name}}}`
* `{{event_properties.${geofence_set_name}}}`
{% endraw %}

## 자주 묻는 질문

[지오펜스 FAQ][3]를 방문하여 지오펜스에 대한 자주 묻는 질문에 대한 답변을 확인하세요.


[1]: {% image_buster /assets/img_archive/locations_main_screen.png %}
[2]: {% image_buster /assets/img_archive/action_based_geofence_trigger.png %}
[3]: {{site.baseurl}}/user_guide/engagement_tools/locations_and_geofences/faqs/#geofences
