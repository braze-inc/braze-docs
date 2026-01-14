---
nav_title: 고객 행동 및 사용자 이벤트
layout: customer_behavior_events_glossary
page_order: 4
excerpt_separator: ""
page_type: glossary
description: "이 용어집에는 Braze가 커런츠를 사용하여 추적하고 선택한 데이터 웨어하우스로 전송할 수 있는 다양한 고객 행동 및 사용자 이벤트가 나열되어 있습니다."
tool: Currents
search_rank: 7
---

추가 이벤트 자격에 대한 액세스가 필요한 경우 Braze 담당자에게 문의하거나 [지원 티켓을]({{site.baseurl}}/braze_support/) 개설하세요. 이 페이지에서 필요한 것을 찾을 수 없다면 [메시지 참여 이벤트 라이브러리]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) 또는 [커런츠 샘플 데이터 예시를](https://github.com/Appboy/currents-examples/tree/master/sample-data) 확인하세요.

{% details Explanation of customer behavior and user event structure and platform values %}

### 이벤트 구조

이 고객 행동 및 사용자 이벤트 분석은 일반적으로 고객 행동 또는 사용자 이벤트에 어떤 유형의 정보가 포함되는지 보여줍니다. 구성 요소에 대한 확실한 이해를 바탕으로 개발자와 비즈니스 인텔리전스 전략 팀은 수신되는 커런츠 이벤트 데이터를 사용하여 데이터 중심 보고서와 차트를 작성하고 다른 중요한 데이터 측정기준을 활용할 수 있습니다.

\![사용자별 속성, 행동별 속성, 기기별 속성별로 그룹화된 구매 이벤트를 보여주는 사용자 이벤트 내역]({% image_buster /assets/img/customer_engagement_event.png %})

고객 행동 및 사용자 이벤트는 **사용자별** 속성, **행동별** 속성, **기기별** 속성으로 구성됩니다.

### 플랫폼 가치

특정 이벤트는 사용자 기기의 플랫폼을 지정하는 `platform` 값을 반환합니다.
<br>다음 표에서는 반환 가능한 값을 자세히 설명합니다:

| 사용자 기기 | 플랫폼 가치 |
| --- | --- |
| iOS | `ios` |
| Android | `android` |
| FireTV | `kindle` |
| Kindle | `kindle` |
| 웹 | `web` |
| tvOS | `tvos` |
| Roku | `roku` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% enddetails %}

{% alert important %}
스토리지 스키마는 데이터 웨어하우스 스토리지 파트너(예: Google Cloud Storage, Amazon S3, Microsoft Azure Blob Storage)로 전송하는 플랫 파일 이벤트 데이터에 적용됩니다. 여기에 나열된 일부 이벤트와 대상 조합은 아직 일반적으로 사용할 수 없습니다. 다양한 파트너가 지원하는 이벤트에 대한 자세한 내용은 [사용 가능한 파트너]({{site.baseurl}}/user_guide/data/braze_currents/available_partners/) 목록을 참조하여 각 파트너 페이지를 확인하세요.<br><br>또한 커런츠는 페이로드가 900KB를 초과하는 지나치게 큰 이벤트는 삭제한다는 점에 유의하세요.
{% endalert %}

{% api %}
## 무작위 버킷 번호 업데이트 이벤트 {#random-bucket-number-update-events}

{% apitags %}
무작위 버킷 번호
{% endapitags %}

이 사용자 이벤트는 워크스페이스 내에서 새 사용자가 생성될 때마다 발생합니다. 이 이벤트 기간 동안 각 신규 사용자에게는 무작위 버킷 번호가 할당되며, 이를 사용하여 균일하게 분포된 무작위 사용자 세그먼트를 생성할 수 있습니다. 이를 사용하여 다양한 무작위 버킷 번호 값을 그룹화하고 캠페인 및 캠페인 배리언트 전반의 성능/성과를 비교할 수 있습니다.

{% alert important %}
이번 커런츠 이벤트는 '모든 이벤트 커넥터'를 구매한 고객에게만 제공되며, 스토리지 이벤트 커넥터(예: Amazon S3, Microsoft Azure, Google Cloud Storage)에서만 사용할 수 있습니다.
<br><br>이 이벤트를 활성화하고 워크스페이스에서 기존 사용자의 무작위 버킷 번호에 대한 백필을 예약하려면 고객 성공 매니저에게 문의하세요.
{% endalert %}

{% tabs %}
{% tab Cloud Storage %}
```json
// users.RandomBucketNumberUpdate

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "prev_random_bucket_number" : "(optional, int) Previous random bucket number",
  "random_bucket_number" : "(required, int) New random bucket number",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## 커스텀 이벤트 {#custom-events}

{% apitags %}
커스텀 이벤트
{% endapitags %}

이 이벤트는 특정 커스텀 이벤트가 트리거될 때 발생합니다. 이를 사용하여 사용자가 애플리케이션에서 커스텀 이벤트를 수행하는 시기를 추적할 수 있습니다.

{% tabs %}
{% tab Amplitude %}
```json
// [Braze Custom Event] (users.behaviors.CustomEvent)

{
  "adid" : "(optional, string) [PII] Advertising identifier",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "device_model" : "(optional, string) Model of the device",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "idfa" : "(optional, string) [PII] Advertising identifier",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// [Braze Custom Event] (users.behaviors.CustomEvent)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "$device" : "(optional, string) Model of the device",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "$os" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// users.behaviors.CustomEvent

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : {
      "model" : "(optional, string) Model of the device",
      "type" : "(optional, string) Platform of the device"
    },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "name" : "(required, string) Name of the custom event"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.behaviors.CustomEvent

{
  "ad_id" : "(optional, string) [PII] Advertising identifier",
  "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
  "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "device_model" : "(optional, string) Model of the device",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "name" : "(required, string) Name of the custom event",
  "os_version" : "(optional, string) Version of the operating system of the device",
  "platform" : "(optional, string) Platform of the device",
  "properties" : "(required, string) Custom properties stored as a JSON encoded string",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

#### 부동산 세부 정보

- 커스텀 이벤트의 경우 페이로드에 이벤트와 관련된 모든 [커스텀 이벤트 속성정보도]({{site.baseurl}}/user_guide/data/custom_data/custom_events#custom-event-properties) 채워집니다.
- `ad_id`, `ad_id_type`, `ad_tracking_enabled` 의 경우 네이티브 SDK를 통해 iOS IDFA 및 Android Google 광고 ID를 명시적으로 수집해야 합니다. 여기에서 자세히 알아보세요: [iOS]({{site.baseurl}}/developer_guide/analytics/managing_data_collection/?sdktab=swift), [Android]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android#android_google-advertising-id).
- Kafka를 사용하여 [커런츠]({{site.baseurl}}/user_guide/data/braze_currents/) 데이터를 수집하는 경우 고객 성공 관리자 또는 계정 매니저에게 문의하여 `ad_id` 으로 전송하기 위한 기능 플리퍼를 인에이블하세요.
{% endapi %}

{% api %}
## 설치 경로 속성 이벤트 {#install-attribution-events}

{% apitags %}
기여도 속성
{% endapitags %}

이 이벤트는 앱 설치가 소스에 속성이 있는 경우 발생합니다. 이를 사용하여 앱 설치의 출처를 추적할 수 있습니다.

{% tabs %}
{% tab Amplitude %}
```json
// Install Attribution (users.behaviors.InstallAttribution)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "source" : "(optional, string) The source of the attribution"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Install Attribution (users.behaviors.InstallAttribution)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "source" : "(optional, string) The source of the attribution",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Install Attribution (users.behaviors.InstallAttribution)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "source" : "(required, string) The source of the attribution"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.behaviors.InstallAttribution

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "source" : "(required, string) The source of the attribution",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## 위치 이벤트 {#location-events}

{% apitags %}
위치
{% endapitags %}

이 이벤트는 사용자가 지정된 위치를 방문할 때 트리거됩니다. 이를 사용하여 앱에서 위치 이벤트를 트리거하는 사용자를 추적할 수 있습니다.

{% tabs %}
{% tab Amplitude %}
```json
// Location (users.behaviors.Location)

{
  "adid" : "(optional, string) [PII] Advertising identifier",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "alt_accuracy" : "(optional, float) Altitude accuracy of recorded location",
    "altitude" : "(optional, float) [PII] Altitude of recorded location",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "device_model" : "(optional, string) Model of the device",
    "latitude" : "(required, float) [PII] Latitude of recorded location",
    "ll_accuracy" : "(optional, float) Accuracy of the latitude and longitude of recorded location",
    "longitude" : "(required, float) [PII] Longitude of recorded location",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "idfa" : "(optional, string) [PII] Advertising identifier",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Location (users.behaviors.Location)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "alt_accuracy" : "(optional, float) Altitude accuracy of recorded location",
    "altitude" : "(optional, float) [PII] Altitude of recorded location",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "$device" : "(optional, string) Model of the device",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "latitude" : "(required, float) [PII] Latitude of recorded location",
    "ll_accuracy" : "(optional, float) Accuracy of the latitude and longitude of recorded location",
    "longitude" : "(required, float) [PII] Longitude of recorded location",
    "$os" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Location (users.behaviors.Location)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : {
      "model" : "(optional, string) Model of the device",
      "type" : "(optional, string) Platform of the device"
    },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "alt_accuracy" : "(optional, float) Altitude accuracy of recorded location",
    "altitude" : "(optional, float) [PII] Altitude of recorded location",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "latitude" : "(required, float) [PII] Latitude of recorded location",
    "ll_accuracy" : "(optional, float) Accuracy of the latitude and longitude of recorded location",
    "longitude" : "(required, float) [PII] Longitude of recorded location"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.behaviors.Location

{
  "ad_id" : "(optional, string) [PII] Advertising identifier",
  "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
  "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
  "alt_accuracy" : "(optional, float) Altitude accuracy of recorded location",
  "altitude" : "(optional, float) [PII] Altitude of recorded location",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(required, string) API ID of the app on which this event occurred",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "device_model" : "(optional, string) Model of the device",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "latitude" : "(required, float) [PII] Latitude of recorded location",
  "ll_accuracy" : "(optional, float) Accuracy of the latitude and longitude of recorded location",
  "longitude" : "(required, float) [PII] Longitude of recorded location",
  "os_version" : "(optional, string) Version of the operating system of the device",
  "platform" : "(optional, string) Platform of the device",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

#### 부동산 세부 정보

- `ad_id`, `ad_id_type`, `ad_tracking_enabled` 의 경우 네이티브 SDK를 통해 iOS IDFA 및 Android Google 광고 ID를 명시적으로 수집해야 합니다. 여기에서 자세히 알아보세요: [iOS]({{site.baseurl}}/developer_guide/analytics/managing_data_collection/?sdktab=swift), [Android]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android#android_google-advertising-id).
- Kafka를 사용하여 [커런츠]({{site.baseurl}}/user_guide/data/braze_currents/) 데이터를 수집하는 경우 고객 성공 관리자 또는 계정 매니저에게 문의하여 `ad_id` 으로 전송하기 위한 기능 플리퍼를 인에이블하세요.
{% endapi %}

{% api %}
## 구매 이벤트 {#purchase-events}

{% apitags %}
구매
{% endapitags %}

이 이벤트는 사용자가 구매할 때 발생합니다. 이 데이터를 사용하여 사용자가 애플리케이션에서 상품을 구매할 때를 추적합니다.

{% alert tip %}
구매는 특별한 커스텀 이벤트이며 커스텀 이벤트와 같은 방식으로 JSON으로 인코딩된 커스텀 이벤트 속성정보 문자열이 함께 제공됩니다.
{% endalert %}

{% tabs %}
{% tab Amplitude %}
```json
// Purchase (users.behaviors.Purchase)

{
  "adid" : "(optional, string) [PII] Advertising identifier",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "currency" : "(required, string) Currency of the purchase",
    "device_model" : "(optional, string) Model of the device",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "idfa" : "(optional, string) [PII] Advertising identifier",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "price" : "(required, float) Price of the purchase",
  "productId" : "(required, string) ID of the product purchased",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Purchase (users.behaviors.Purchase)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "currency" : "(required, string) Currency of the purchase",
    "$device" : "(optional, string) Model of the device",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "$os" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "price" : "(required, float) Price of the purchase",
    "product_id" : "(required, string) ID of the product purchased",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Purchased (users.behaviors.Purchase)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : {
      "model" : "(optional, string) Model of the device",
      "type" : "(optional, string) Platform of the device"
    },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "currency" : "(required, string) Currency of the purchase",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "price" : "(required, float) Price of the purchase",
    "product_id" : "(required, string) ID of the product purchased"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.behaviors.Purchase

{
  "ad_id" : "(optional, string) [PII] Advertising identifier",
  "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
  "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "currency" : "(required, string) Currency of the purchase",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "device_model" : "(optional, string) Model of the device",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "os_version" : "(optional, string) Version of the operating system of the device",
  "platform" : "(optional, string) Platform of the device",
  "price" : "(required, float) Price of the purchase",
  "product_id" : "(required, string) ID of the product purchased",
  "properties" : "(required, string) Custom properties stored as a JSON encoded string",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

#### 부동산 세부 정보

- 구매 이벤트의 경우 페이로드는 이벤트와 관련된 모든 [구매 이벤트 속성정보로]({{site.baseurl}}/user_guide/data/custom_data/purchase_events/#purchase-properties) 채워집니다.
- `ad_id`, `ad_id_type`, `ad_tracking_enabled` 의 경우 네이티브 SDK를 통해 iOS IDFA 및 Android Google 광고 ID를 명시적으로 수집해야 합니다. 여기에서 자세히 알아보세요: [iOS]({{site.baseurl}}/developer_guide/analytics/managing_data_collection/?sdktab=swift), [Android]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android#android_google-advertising-id).
- Kafka를 사용하여 [커런츠]({{site.baseurl}}/user_guide/data/braze_currents/) 데이터를 수집하는 경우 고객 성공 관리자 또는 계정 매니저에게 문의하여 `ad_id` 으로 전송하기 위한 기능 플리퍼를 인에이블하세요.
{% endapi %}

{% api %}
## 첫 세션 이벤트 {#first-session-events}

{% apitags %}
세션
{% endapitags %}

이 이벤트는 사용자가 애플리케이션에서 첫 세션을 시작할 때 발생합니다. 이 데이터를 사용하여 사용자가 세션을 시작하는 시기를 추적합니다.

{% alert tip %}
사용자가 첫 세션을 시작하면 `FirstSession` 이벤트와 `SessionStart` 이벤트가 모두 발생합니다.
{% endalert %}

{% tabs %}
{% tab Amplitude %}
```json
// First Session (users.behaviors.app.FirstSession)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "device_model" : "(optional, string) Model of the device",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "session_id" : "(optional, string) UUID of the session"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// First Session (users.behaviors.app.FirstSession)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "$device" : "(optional, string) Model of the device",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "$os" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "session_id" : "(optional, string) UUID of the session",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// First Session (users.behaviors.app.FirstSession)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : {
      "model" : "(optional, string) Model of the device",
      "type" : "(optional, string) Platform of the device"
    },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "session_id" : "(required, string) UUID of the session"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.behaviors.app.FirstSession

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(required, string) API ID of the app on which this event occurred",
  "country" : "(optional, string) [DEPRECATED]",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "device_model" : "(optional, string) Model of the device",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "gender" : "(optional, string) [DEPRECATED]",
  "id" : "(required, string) Globally unique ID for this event",
  "language" : "(optional, string) [DEPRECATED]",
  "os_version" : "(optional, string) Version of the operating system of the device",
  "platform" : "(optional, string) Platform of the device",
  "sdk_version" : "(optional, string) [DEPRECATED]",
  "session_id" : "(required, string) UUID of the session",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## 세션 종료 이벤트 {#session-end-events}

{% apitags %}
세션
{% endapitags %}

이는 사용자가 애플리케이션을 종료하여 현재 세션이 종료될 때 발생합니다. 이 데이터를 사용하여 세션이 종료되는 시점을 추적하고 적절한 세션 시작 이벤트와 함께 세션에서 세션이 지속된 시간을 계산합니다.

{% tabs %}
{% tab Amplitude %}
```json
// Session End (users.behaviors.app.SessionEnd)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "device_model" : "(optional, string) Model of the device",
    "duration" : "(optional, float) Duration of the session in seconds",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "session_id" : "(optional, string) UUID of the session"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Session End (users.behaviors.app.SessionEnd)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "$device" : "(optional, string) Model of the device",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "duration" : "(optional, float) Duration of the session in seconds",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "$os" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "session_id" : "(optional, string) UUID of the session",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Session Ended (users.behaviors.app.SessionEnd)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : {
      "model" : "(optional, string) Model of the device",
      "type" : "(optional, string) Platform of the device"
    },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "duration" : "(optional, float) Duration of the session in seconds",
    "session_id" : "(required, string) UUID of the session"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.behaviors.app.SessionEnd

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(required, string) API ID of the app on which this event occurred",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "device_model" : "(optional, string) Model of the device",
  "duration" : "(optional, float) Duration of the session in seconds",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "os_version" : "(optional, string) Version of the operating system of the device",
  "platform" : "(optional, string) Platform of the device",
  "session_id" : "(required, string) UUID of the session",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## 세션 시작 이벤트 {#session-start-events}

{% apitags %}
세션
{% endapitags %}

이 이벤트는 사용자가 세션을 시작할 때 발생합니다. 이 데이터를 사용하여 사용자가 세션을 시작하는 시기를 추적합니다.

{% alert tip %}
사용자가 첫 세션을 시작하면 `FirstSession` 이벤트와 `SessionStart` 이벤트가 모두 발생합니다.
{% endalert %}

{% tabs %}
{% tab Amplitude %}
```json
// Session Start (users.behaviors.app.SessionStart)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "device_model" : "(optional, string) Model of the device",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "session_id" : "(optional, string) UUID of the session"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Session Start (users.behaviors.app.SessionStart)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "$device" : "(optional, string) Model of the device",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "$os" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "session_id" : "(optional, string) UUID of the session",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Session Started (users.behaviors.app.SessionStart)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : {
      "model" : "(optional, string) Model of the device",
      "type" : "(optional, string) Platform of the device"
    },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "session_id" : "(required, string) UUID of the session"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.behaviors.app.SessionStart

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(required, string) API ID of the app on which this event occurred",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "device_model" : "(optional, string) Model of the device",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "os_version" : "(optional, string) Version of the operating system of the device",
  "platform" : "(optional, string) Platform of the device",
  "session_id" : "(required, string) UUID of the session",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## 토큰 변경 이벤트를 시작하기 위한 라이브 활동 푸시 {#live-activity-push-to-start-token-change-events}

{% apitags %}
라이브 활동, 푸시 시작 토큰
{% endapitags %}

이 이벤트는 Braze가 라이브 활동 푸시 시작 토큰을 사용자와 동기화할 때 발생합니다.

{% tabs %}
{% tab Amplitude %}
```json
// Live Activity Push To Start Token Change (users.behaviors.liveactivity.PushToStartTokenChange)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "activity_attributes_type" : "(optional, string) Live Activity attribute type",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "ios_push_token_apns_gateway" : "(optional, int) APNS gateway of the push token, only applies to iOS push tokens, 1 for development, 2 for production",
    "push_to_start_token" : "(optional, string) Live Activity push to start token",
    "push_token_state_change_type" : "(optional, string) A description of the push token state change type"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Live Activity Push To Start Token Change (users.behaviors.liveactivity.PushToStartTokenChange)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "activity_attributes_type" : "(optional, string) Live Activity attribute type",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "ios_push_token_apns_gateway" : "(optional, int) APNS gateway of the push token, only applies to iOS push tokens, 1 for development, 2 for production",
    "push_to_start_token" : "(optional, string) Live Activity push to start token",
    "push_token_state_change_type" : "(optional, string) A description of the push token state change type",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Live Activity Push To Start Token Changed (users.behaviors.liveactivity.PushToStartTokenChange)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "activity_attributes_type" : "(optional, string) Live Activity attribute type",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "ios_push_token_apns_gateway" : "(optional, int) APNS gateway of the push token, only applies to iOS push tokens, 1 for development, 2 for production",
    "push_to_start_token" : "(optional, string) Live Activity push to start token",
    "push_token_state_change_type" : "(optional, string) A description of the push token state change type"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.behaviors.liveactivity.PushToStartTokenChange

{
  "activity_attributes_type" : "(optional, string) Live Activity attribute type",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "ios_push_token_apns_gateway" : "(optional, int) APNS gateway of the push token, only applies to iOS push tokens, 1 for development, 2 for production",
  "push_to_start_token" : "(optional, string) Live Activity push to start token",
  "push_token_state_change_type" : "(optional, string) A description of the push token state change type",
  "sdk_version" : "(optional, string) Version of the Braze SDK in use during the event",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## 실시간 활동 업데이트 토큰 변경 이벤트 {#live-activity-update-token-change-events}

{% apitags %}
라이브 활동, 토큰 업데이트
{% endapitags %}

이 이벤트는 Braze가 라이브 활동 업데이트 토큰을 사용자와 동기화할 때 발생합니다.

{% tabs %}
{% tab Amplitude %}
```json
// Live Activity Update Token Change (users.behaviors.liveactivity.UpdateTokenChange)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "activity_id" : "(optional, string) Live Activity identifier",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "ios_push_token_apns_gateway" : "(optional, int) APNS gateway of the push token, only applies to iOS push tokens, 1 for development, 2 for production",
    "push_token_state_change_type" : "(optional, string) A description of the push token state change type",
    "update_token" : "(optional, string) Live Activity update token"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Live Activity Update Token Change (users.behaviors.liveactivity.UpdateTokenChange)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "activity_id" : "(optional, string) Live Activity identifier",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "ios_push_token_apns_gateway" : "(optional, int) APNS gateway of the push token, only applies to iOS push tokens, 1 for development, 2 for production",
    "push_token_state_change_type" : "(optional, string) A description of the push token state change type",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token",
    "update_token" : "(optional, string) Live Activity update token"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Live Activity Update Token Changed (users.behaviors.liveactivity.UpdateTokenChange)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "activity_id" : "(optional, string) Live Activity identifier",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "ios_push_token_apns_gateway" : "(optional, int) APNS gateway of the push token, only applies to iOS push tokens, 1 for development, 2 for production",
    "push_token_state_change_type" : "(optional, string) A description of the push token state change type",
    "update_token" : "(optional, string) Live Activity update token"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.behaviors.liveactivity.UpdateTokenChange

{
  "activity_id" : "(optional, string) Live Activity identifier",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "ios_push_token_apns_gateway" : "(optional, int) APNS gateway of the push token, only applies to iOS push tokens, 1 for development, 2 for production",
  "push_token_state_change_type" : "(optional, string) A description of the push token state change type",
  "sdk_version" : "(optional, string) Version of the Braze SDK in use during the event",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "update_token" : "(optional, string) Live Activity update token",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## 푸시 알림 토큰 상태 변경 이벤트 {#push-notification-token-state-change-events}

{% apitags %}
푸시, 토큰 상태 변경
{% endapitags %}

이 이벤트는 푸시 토큰이 삽입, 업데이트 또는 제거될 때 발생합니다. 푸시 토큰의 상태를 추적하는 데 사용합니다.

{% tabs %}
{% tab Amplitude %}
```json
// Push Notification Token State Change (users.behaviors.pushnotification.TokenStateChange)

{
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "ios_push_token_apns_gateway" : "(optional, int) APNS gateway of the push token, only applies to iOS push tokens, 1 for development, 2 for production",
    "platform" : "(optional, string) Platform of the device",
    "push_token_created_at" : "(optional, int) UNIX timestamp at which the push token was created",
    "push_token_device_id" : "(optional, string) Device id of the push token",
    "push_token_foreground_push_disabled" : "(optional, boolean) Foreground push disabled flag of the push token",
    "push_token_provisionally_opted_in" : "(optional, boolean) Provisionally opted in flag of the push token",
    "push_token_state_change_type" : "(optional, string) A description of the push token state change type",
    "push_token_updated_at" : "(optional, int) UNIX timestamp at which the push token was last updated",
    "web_push_token_public_key" : "(optional, string) Public key of the push token, only applies to web push tokens",
    "web_push_token_user_auth" : "(optional, string) User auth of the push token, only applies to web push tokens",
    "web_push_token_vapid_public_key" : "(optional, string) VAPID public key of the push token, only applies to web push tokens"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Push Notification Token State Change (users.behaviors.pushnotification.TokenStateChange)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "ios_push_token_apns_gateway" : "(optional, int) APNS gateway of the push token, only applies to iOS push tokens, 1 for development, 2 for production",
    "platform" : "(optional, string) Platform of the device",
    "push_token" : "(optional, string) Push token of the event",
    "push_token_created_at" : "(optional, int) UNIX timestamp at which the push token was created",
    "push_token_device_id" : "(optional, string) Device id of the push token",
    "push_token_foreground_push_disabled" : "(optional, boolean) Foreground push disabled flag of the push token",
    "push_token_provisionally_opted_in" : "(optional, boolean) Provisionally opted in flag of the push token",
    "push_token_state_change_type" : "(optional, string) A description of the push token state change type",
    "push_token_updated_at" : "(optional, int) UNIX timestamp at which the push token was last updated",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token",
    "web_push_token_public_key" : "(optional, string) Public key of the push token, only applies to web push tokens",
    "web_push_token_user_auth" : "(optional, string) User auth of the push token, only applies to web push tokens",
    "web_push_token_vapid_public_key" : "(optional, string) VAPID public key of the push token, only applies to web push tokens"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Push Notification Token State Changed (users.behaviors.pushnotification.TokenStateChange)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "ios_push_token_apns_gateway" : "(optional, int) APNS gateway of the push token, only applies to iOS push tokens, 1 for development, 2 for production",
    "push_token" : "(optional, string) Push token of the event",
    "push_token_created_at" : "(optional, int) UNIX timestamp at which the push token was created",
    "push_token_device_id" : "(optional, string) Device id of the push token",
    "push_token_foreground_push_disabled" : "(optional, boolean) Foreground push disabled flag of the push token",
    "push_token_provisionally_opted_in" : "(optional, boolean) Provisionally opted in flag of the push token",
    "push_token_state_change_type" : "(optional, string) A description of the push token state change type",
    "push_token_updated_at" : "(optional, int) UNIX timestamp at which the push token was last updated",
    "web_push_token_public_key" : "(optional, string) Public key of the push token, only applies to web push tokens",
    "web_push_token_user_auth" : "(optional, string) User auth of the push token, only applies to web push tokens",
    "web_push_token_vapid_public_key" : "(optional, string) VAPID public key of the push token, only applies to web push tokens"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.behaviors.pushnotification.TokenStateChange

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "ios_push_token_apns_gateway" : "(optional, int) APNS gateway of the push token, only applies to iOS push tokens, 1 for development, 2 for production",
  "platform" : "(optional, string) Platform of the device",
  "push_token_created_at" : "(optional, int) UNIX timestamp at which the push token was created",
  "push_token_device_id" : "(optional, string) Device id of the push token",
  "push_token_foreground_push_disabled" : "(optional, boolean) Foreground push disabled flag of the push token",
  "push_token_provisionally_opted_in" : "(optional, boolean) Provisionally opted in flag of the push token",
  "push_token_state_change_type" : "(optional, string) A description of the push token state change type",
  "push_token_updated_at" : "(optional, int) UNIX timestamp at which the push token was last updated",
  "sdk_version" : "(optional, string) Version of the Braze SDK in use during the event",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(required, string) Braze user ID of the user who performed this event",
  "web_push_token_public_key" : "(optional, string) Public key of the push token, only applies to web push tokens",
  "web_push_token_user_auth" : "(optional, string) User auth of the push token, only applies to web push tokens",
  "web_push_token_vapid_public_key" : "(optional, string) VAPID public key of the push token, only applies to web push tokens"
}
```
{% endtab %}
{% endtabs %}

#### 부동산 세부 정보

- `push_token_foreground_push_disabled` 필드는 푸시 토큰이 포그라운드 푸시 또는 백그라운드 푸시를 받을 수 있는지 여부를 나타냅니다.
  - 사용자가 기기에서 푸시 알림 권한을 명시적으로 허용한 경우 `false`, 토큰은 포그라운드 푸시 알림을 수신할 수 있습니다.
  - 사용자가 기기에서 푸시 알림 권한을 명시적으로 거부한 경우 `true` 이며, 이 토큰은 백그라운드 푸시 알림에만 허용됩니다.
  - 푸시 권한을 알 수 없는 경우 비어 있습니다. 기본값으로 Braze는 토큰에 포그라운드 푸시 알림을 보내려고 시도합니다.
- `push_token_provisionally_opted_in` 필드는 iOS 푸시 토큰에만 적용됩니다.
  - [임시 권한]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/#provisional-push) 부여를 설정한 경우 임시 토큰의 이 필드는 `true` 로 설정됩니다. 다른 모든 푸시 토큰은 `false` 입니다.
- 푸시 토큰이 Braze에 들어올 때마다 라이프사이클 이벤트가 기록됩니다. `push_token_state_change_type` 필드에 기록되는 토큰 변경 이벤트에는 세 가지 유형("추가", "업데이트", "제거")이 있습니다. 다음 세부 사항을 참고하세요:
  - 이전에 존재하지 않았던 새로운 토큰의 경우 하나의 "추가" 이벤트를 수집합니다.
  - 동일한 사용자에서 동일한 토큰 문자열로 토큰을 업데이트하는 경우(게이트웨이 또는 `foreground_push_disabled` 또는 기타 "보조" 필드 변경), 동일한 토큰에서 하나의 "업데이트" 이벤트가 수집됩니다.
  - 토큰이 한 사용자에서 다른 사용자로 이동한 경우 이전 사용자에 대한 '제거' 이벤트 1개와 새 사용자에 대한 '추가' 이벤트 1개가 수집됩니다.
  - 동일한 사용자 또는 기기가 새 토큰을 생성하는 경우 이전 토큰에 대한 '제거' 이벤트 1개와 새 토큰에 대한 '추가' 이벤트 1개가 수집됩니다.
  - Braze가 토큰을 제거하는 경우(제거 또는 유효하지 않은 토큰 등의 이유로) 토큰에 대해 하나의 "제거" 이벤트를 수집합니다.
{% endapi %}