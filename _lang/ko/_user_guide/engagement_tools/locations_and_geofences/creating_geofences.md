---
nav_title: 지오펜스 생성
article_title: 지오펜스 생성
page_order: 1
page_type: reference
toc_headers: h2
description: "이 참조 문서에서는 지오펜스가 무엇인지, 지오펜스 이벤트를 생성하고 구성하는 방법을 다룹니다."
tool: 
  - Location
search_rank: 9
---

# 지오펜스

> 실시간 위치 제공의 핵심은 지오펜스 개념입니다. 지오펜스는 특정 글로벌 위치를 중심으로 반경을 결합한 위도와 경도로 표현되는 가상 지리적 영역입니다. 지오펜스는 건물 크기에서 전체 도시 크기까지 다양할 수 있습니다.

## How it works

Geofences can be used to trigger campaigns in real-time as users enter and exit their borders, or send follow-up campaigns hours or days later. 지오펜스에 들어오거나 나가는 사용자는 세분화 및 리타겟팅에 사용할 수 있는 새로운 사용자 데이터 레이어를 추가합니다.

지오펜스는 지오펜스 세트로 구성됩니다. 지오펜스 세트는 플랫폼 전반에서 사용자를 세그먼트하거나 참여시키는 데 사용할 수 있는 지오펜스 그룹입니다. 각 지오펜스 세트는 최대 10,000개의 지오펜스를 보유할 수 있습니다.

You can create or upload an unlimited number of geofences.

- Android 앱은 한 번에 최대 100개의 지오펜스를 로컬에 저장할 수 있습니다. Braze는 앱당 로컬에 최대 20개의 지오펜스만 저장하도록 구성됩니다.
- iOS 기기는 앱당 한 번에 최대 20개의 지오펜스를 모니터링할 수 있습니다. Braze는 공간이 허용되는 경우 최대 20개의 위치를 모니터링합니다. 
- If the user is eligible to receive more than 20 geofences, Braze will download the maximum amount of locations based on proximity to the user at the point of session start.
- 지오펜스가 올바르게 작동하려면 앱이 사용 가능한 모든 지오펜스 위치를 사용하지 않도록 해야 합니다.

Refer to the following table for common geofence terms and their descriptions.

| Term | Description |
|---|---|
| Latitude and longitude | The geographic center of the geofence. |
| Radius | The radius of the geofence in meters, measured from the geographic center. We recommend setting a minimum radius of 100–150 meters for all geofences. |
| Cooldown | Users receive geofence-triggered notifications after performing enter or exit transitions on individual geofences. After a transition occurs, there is a pre-defined time during which that user may not perform the same transition on that individual geofence again. This time is called the "cooldown" and is pre-defined by Braze, and its main purpose is to prevent unnecessary network requests. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Manually create geofences

### Step 1: Create a geofence set

To create a geofence, you'll need to create a geofence set first.

1. Go to **Audience** > **Locations** in the Braze dashboard.
2. Select **Create Geofence Set**.
3. For **Set name**, enter a name for your geofence set.
4. (Optional) Add tags to filter your set.

### Step 2: Add the geofences

Next, you can add geofences to your geofence set.

1. Select **Draw Geofence** to click and drag the circle on the map. Repeat to add more geofences to your set as needed.
2. (Optional) You can select **Edit** and replace the geofence description with a name.
3. Select **Save Geofence Set** to save.

{% alert tip %}
최적의 기능을 위해 반경 최소 200미터의 지오펜스를 만드는 것을 권장합니다. For more information on configurable options, refer to [Mobile integrations](#mobile-integrations).
{% endalert %}

![A geofence set with two geofences "EastCoastGreaterNY" and "WesternRegion" with two circles on the map.]({% image_buster /assets/img/geofence_example.png %})

## Bulk upload geofences {#creating-geofence-sets-via-bulk-upload}

지오펜스는 `FeatureCollection` 유형의 GeoJSON 객체로 일괄 업로드할 수 있습니다. Each geofence is a `Point` geometry type in the feature collection. The properties for each feature require a `radius` key, and an optional `name` key for each geofence. 

To upload your GeoJSON, select **More** > **Upload GeoJSON**.

When creating your geofences, consider the following details:

- The `coordinates` value in the GeoJSON is formatted as `[Longitude, Latitude]`.
- The maximum geofence radius that may be uploaded is 10,000 meters (about 100 kilometers or 62 miles).

### Example

The following example represents the correct GeoJSON for specifying two geofences: one for Braze headquarters in NYC, and one for the Statue of Liberty south of Manhattan.

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

## 지오펜스 이벤트 사용

After geofences have been configured, you can use them to enhance and enrich how you communicate with your users.

### Triggering campaigns and Canvases

캠페인 및 캔버스 트리거의 일부로 지오펜스 데이터를 사용하려면 전달 방법으로 **실행 기반 전달**을 선택하세요. 다음으로, `Trigger a Geofence`의 트리거 동작을 추가합니다. 마지막으로, 메시지에 대한 지오펜스 세트 및 지오펜스 전환 이벤트 유형을 선택하세요. 지오펜스 이벤트를 사용하여 캔버스를 통해 사용자들을 진전시킬 수도 있습니다.

![An action-based campaign with a geofence that will trigger when a user enters German airports.]({% image_buster /assets/img_archive/action_based_geofence_trigger.png %})

### Personalizing messages

지오펜스 데이터를 사용하여 메시지를 개인화하려면 다음 Liquid 개인화 구문을 사용할 수 있습니다:

{% raw %}
* `{{event_properties.${geofence_name}}}`
* `{{event_properties.${geofence_set_name}}}`
{% endraw %}

## 지오펜스 세트 업데이트

활성 사용자에게 Braze 소프트웨어 개발 키트는 세션 시작 시 하루에 한 번만 지오펜스를 요청합니다. 즉, 세션이 시작된 후 지오펜스 세트에 변경이 발생하면 세트가 처음 내려받아진 시점부터 24시간이 지나야 업데이트된 세트를 받을 수 있습니다.

{% alert note %}
지오펜스가 기기에 로드되지 않으면 사용자가 해당 지역에 들어가도 지오펜스를 트리거할 수 없습니다.
{% endalert %}

## Mobile integrations {#mobile-integrations}

### Cross-platform requirements

Geofence-triggered campaigns are available on iOS and Android. To support geofences, the following must be in place:

1. Your integration must support background push notifications.
2. Braze geofences or location collection must be enabled.
3. For devices on iOS version 11 and up, the user must allow location access always for geofencing to work.

{% alert important %}
Starting with Braze SDK version 3.6.0, Braze location collection is disabled by default. To verify that it's enabled on Android, confirm that `com_braze_enable_location_collection` is set to `true` in your `braze.xml`.
{% endalert %}

Refer to [Android](https://developer.android.com/develop/sensors-and-location/location/geofencing#choose-the-optimal-radius-for-your-geofence) or [iOS](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/LocationAwarenessPG/RegionMonitoring/RegionMonitoring.html#//apple_ref/doc/uid/TP40009497-CH9-SW5) documentation for more guidance based on your platform.

{% alert tip %}
You can also leverage geofences with our Technology Partners, such as [Radar]({{site.baseurl}}/partners/message_personalization/location/radar/) and [Foursquare]({{site.baseurl}}/partners/message_personalization/location/foursquare/)
{% endalert %}

## 자주 묻는 질문

### What's the difference between geofences and location tracking?

In Braze, a geofence is a different concept from location tracking. Geofences are used as triggers for certain actions. A geofence is a virtual boundary set up around a geographical location. When a user enters or exits this boundary, it can trigger a specific action, such as sending a message.

Location tracking is used to collect and store a user's most recent location data. This data can be used to segment users based on the `Most Recent Location` filter. For example, you could use the `Most Recent Location` filter to target a specific region of your audience, such as sending a message to users located in New York.

### How accurate are Braze geofences?

Braze geofences use a combination of all location providers available to a device to triangulate the user's location. These include Wi-Fi, GPS, and cellular towers.

Typical accuracy is in 20–50m range and best-case accuracy will be in the 5-10m range. In rural areas, accuracy may degrade significantly, potentially going up to several kilometers. Braze recommends creating geofences with larger radii in rural locations.

For more information on the accuracy of geofences, refer to [Android](https://developer.android.com/develop/sensors-and-location/location/geofencing) and [iOS](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/LocationAwarenessPG/RegionMonitoring/RegionMonitoring.html#//apple_ref/doc/uid/TP40009497-CH9-SW1) documentation.

### How do geofences affect battery life?

Our geofencing solution uses the native geofence system service on iOS and Android and is tuned to intelligently trade off accuracy and power, saving battery life and improving performance as the underlying service improves.

### When are geofences active?

Braze geofences work at all hours of the day, even when your app is closed. They become active as soon as they are defined and uploaded to the Braze dashboard. However, geofences can't function if a user has disabled location tracking.

For geofences to work, users must have location services enabled on their device and must have granted your app permission to access their location. If a user has disabled location tracking, your app won't be able to detect when they enter or exit a geofence.

### Is geofence data stored in user profiles?

No, Braze doesn't store geofence data on user profiles. Geofences are monitored by Apple and Google location services, and Braze only gets notified when a user triggers a geofence. At that point, we process any associated trigger campaigns.

### Can I set up a geofence within a geofence?

As a best practice, avoid setting up geofences inside each other as this may cause issues with triggering notifications.

