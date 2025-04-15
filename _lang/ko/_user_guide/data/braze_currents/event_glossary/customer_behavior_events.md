---
nav_title: 고객 행동 및 사용자 이벤트
layout: customer_behavior_events_glossary
page_order: 4
excerpt_separator: ""
page_type: glossary
description: "이 용어집에는 Braze가 커런트를 사용하여 추적하고 선택한 데이터 웨어하우스로 전송할 수 있는 다양한 고객 행동 및 사용자 이벤트가 나열되어 있습니다."
tool: Currents
search_rank: 7
---

추가 이벤트 자격에 대한 액세스가 필요한 경우 Braze 담당자에게 문의하거나 [지원 티켓을]({{site.baseurl}}/braze_support/) 개설하세요. 이 페이지에서 필요한 정보를 찾을 수 없다면 [메시지 참여 이벤트 라이브러리]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) 또는 [커런츠 샘플 데이터 예시를](https://github.com/Appboy/currents-examples/tree/master/sample-data) 확인하세요.

{% details 고객 행동 및 사용자 이벤트 구조와 플랫폼 가치에 대한 설명 %}

### 이벤트 구조

이 고객 행동 및 사용자 이벤트 분석은 일반적으로 고객 행동 또는 사용자 이벤트에 어떤 유형의 정보가 포함되는지 보여줍니다. 구성 요소에 대한 확실한 이해를 바탕으로 개발자와 비즈니스 인텔리전스 전략 팀은 수신되는 Currents 이벤트 데이터를 사용하여 데이터 기반 보고서와 차트를 만들고 다른 유용한 데이터 메트릭을 활용할 수 있습니다.

![사용자별 속성, 행동별 속성, 기기별 속성별로 그룹화된 구매 이벤트를 보여주는 사용자 이벤트 분석]({% image_buster /assets/img/customer_engagement_event.png %})

고객 행동 및 사용자 이벤트는 **사용자별** 속성, **행동별** 속성, **기기별** 속성으로 구성됩니다.

### 플랫폼 가치

특정 이벤트는 사용자 기기의 플랫폼을 지정하는 `platform` 값을 반환합니다.
<br>다음 표에서는 반환 가능한 값을 자세히 설명합니다:

| 사용자 디바이스 | 플랫폼 가치 |
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
저장 스키마는 우리가 데이터 웨어하우스 저장 파트너(예: Google Cloud Storage, Amazon S3 및 Microsoft Azure Blob Storage)로 보내는 평면 파일 이벤트 데이터에 적용됩니다. 여기에 나열된 일부 이벤트와 목적지 조합은 아직 일반적으로 사용할 수 없습니다. 다양한 파트너가 지원하는 이벤트에 대한 자세한 내용은 [사용 가능한 파트너]({{site.baseurl}}/user_guide/data/braze_currents/available_partners/) 목록을 참조하여 각 페이지를 확인하세요.<br><br>또한, 커런츠는 페이로드가 900KB를 초과하는 지나치게 큰 이벤트는 삭제한다는 점에 유의하세요.
{% endalert %}
{% api %}

## 사용자 지정 이벤트

{% apitags %}
사용자 지정 이벤트
{% endapitags %}

이 이벤트는 특정 사용자 지정 이벤트가 트리거될 때 발생합니다. 이를 사용하여 사용자가 애플리케이션에서 커스텀 이벤트를 수행하는 시기를 추적할 수 있습니다.

{% tabs %}
{% tab Mixpanel %}
```json
// [Braze Custom Event] custom event name: users.behaviors.CustomEvent

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "ad_id" : "(optional, string) Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "$device" : "(optional, string) Model of the device",
    "distinct_id" : "(required, string) External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "$os" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab 클라우드 스토리지 %}
```json
// [Braze Custom Event] custom event name: users.behaviors.CustomEvent

{
  "ad_id" : "(optional, string) Advertising identifier",
  "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
  "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "device_model" : "(optional, string) Model of the device",
  "external_user_id" : "(optional, string) External ID of the user",
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

{% tab 진폭 %}
```json
// [Braze Custom Event] custom event name: users.behaviors.CustomEvent

{
  "adid" : "(optional, string) Advertising identifier",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "ad_id" : "(optional, string) Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "device_model" : "(optional, string) Model of the device",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "idfa" : "(optional, string) Advertising identifier",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) External ID of the user"
}
```
{% endtab %}
{% endtabs %}

#### 부동산 세부 정보
- `ad_id`, `ad_id_type` 및 `ad_tracking_enabled`의 경우 네이티브 SDK를 통해 iOS IDFA 및 Android Google 광고 ID를 명시적으로 수집해야 합니다. Learn more about them here: [iOS]({{site.baseurl}}/developer_guide/platforms/swift/analytics/swift_idfv/), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id).
- 고객 성공 매니저 또는 계정 매니저에게 문의하여 `ad_id`로 보내기 위한 기능 플리퍼를 사용하도록 설정하고, Kafka를 사용하여 [커런츠]({{site.baseurl}}/user_guide/data/braze_currents/) 데이터를 수집하는 경우에는 고객 성공 매니저 또는 계정 매니저에게 문의하세요.

{% endapi %}
{% api %}

## 구매 이벤트

{% apitags %}
구매
{% endapitags %}

이 이벤트는 사용자가 구매할 때 발생합니다. 이 데이터를 사용하여 사용자가 애플리케이션에서 상품을 구매한 시점을 추적합니다.

{% alert tip %}
구매는 특별한 사용자 지정 이벤트이며, 사용자 지정 이벤트와 동일한 방식으로 JSON으로 인코딩된 사용자 지정 이벤트 속성 문자열이 함께 제공됩니다.
{% endalert %}

{% tabs %}
{% tab Mixpanel %}
```json
// Purchase: users.behaviors.Purchase

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "ad_id" : "(optional, string) Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "currency" : "(required, string) Currency of the purchase",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "$device" : "(optional, string) Model of the device",
    "distinct_id" : "(required, string) External ID of the user",
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

{% tab 클라우드 스토리지 %}
```json
// Purchase: users.behaviors.Purchase

{
  "ad_id" : "(optional, string) Advertising identifier",
  "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
  "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "currency" : "(required, string) Currency of the purchase",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "device_model" : "(optional, string) Model of the device",
  "external_user_id" : "(optional, string) External ID of the user",
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

{% tab 진폭 %}
```json
// Purchase: users.behaviors.Purchase

{
  "adid" : "(optional, string) Advertising identifier",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "ad_id" : "(optional, string) Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "currency" : "(required, string) Currency of the purchase",
    "device_model" : "(optional, string) Model of the device",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "idfa" : "(optional, string) Advertising identifier",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "price" : "(required, float) Price of the purchase",
  "productId" : "(required, string) ID of the product purchased",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) External ID of the user"
}
```
{% endtab %}
{% endtabs %}

#### 부동산 세부 정보
- `ad_id`, `ad_id_type` 및 `ad_tracking_enabled` 의 경우 네이티브 SDK를 통해 iOS IDFA 및 Android Google 광고 ID를 명시적으로 수집해야 합니다. Learn more about them here: [iOS]({{site.baseurl}}/developer_guide/platforms/swift/analytics/swift_idfv/), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id).
- 고객 성공 관리자 또는 계정 관리자에게 문의하여 `ad_id` 으로 보내기 위한 기능 플리퍼를 사용하도록 설정하고, Kafka를 사용하여 [Currents]({{site.baseurl}}/user_guide/data/braze_currents/) 데이터를 수집하는 경우에는 고객 성공 관리자 또는 계정 관리자에게 문의하세요.
{% endapi %}


{% api %}

## 최초 세션 이벤트

{% apitags %}
세션
{% endapitags %}

이 이벤트는 사용자가 애플리케이션에서 첫 세션을 시작할 때 발생합니다. 이 데이터를 사용하여 사용자가 세션을 시작하는 시점을 추적합니다.

{% alert tip %}
사용자가 첫 세션을 시작하면 `FirstSession` 이벤트와 `SessionStart` 이벤트가 모두 발생합니다.
{% endalert %}

{% tabs %}
{% tab Mixpanel %}
```json
// First Session: users.behaviors.app.FirstSession

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "$device" : "(optional, string) Model of the device",
    "distinct_id" : "(required, string) External ID of the user",
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

{% tab 클라우드 스토리지 %}
```json
// First Session: users.behaviors.app.FirstSession

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(required, string) API ID of the app on which this event occurred",
  "country" : "(optional, string) Country of the user",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "device_model" : "(optional, string) Model of the device",
  "external_user_id" : "(optional, string) External ID of the user",
  "gender" : "(optional, string) Gender of the user, one of ['M', 'F', 'O', 'N', 'P']",
  "id" : "(required, string) Globally unique ID for this event",
  "language" : "(optional, string) Language of the user",
  "os_version" : "(optional, string) Version of the operating system of the device",
  "platform" : "(optional, string) Platform of the device",
  "sdk_version" : "(optional, string) Version of the Braze SDK in use during the event",
  "session_id" : "(required, string) UUID of the session",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}

{% tab 진폭 %}
```json
// First Session: users.behaviors.app.FirstSession

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "device_model" : "(optional, string) Model of the device",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "session_id" : "(optional, string) UUID of the session"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) External ID of the user"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}

## 세션 시작 이벤트

{% apitags %}
세션
{% endapitags %}

이 이벤트는 사용자가 세션을 시작할 때 발생합니다. 이 데이터를 사용하여 사용자가 세션을 시작하는 시점을 추적합니다.

{% alert tip %}
사용자가 첫 세션을 시작하면 `FirstSession` 이벤트와 `SessionStart` 이벤트가 모두 발생합니다.
{% endalert %}

{% tabs %}
{% tab Mixpanel %}
```json
// Session Start: users.behaviors.app.SessionStart

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "$device" : "(optional, string) Model of the device",
    "distinct_id" : "(required, string) External ID of the user",
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

{% tab 클라우드 스토리지 %}
```json
// Session Start: users.behaviors.app.SessionStart

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(required, string) API ID of the app on which this event occurred",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "device_model" : "(optional, string) Model of the device",
  "external_user_id" : "(optional, string) External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "os_version" : "(optional, string) Version of the operating system of the device",
  "platform" : "(optional, string) Platform of the device",
  "session_id" : "(required, string) UUID of the session",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}

{% tab 진폭 %}
```json
// Session Start: users.behaviors.app.SessionStart

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "device_model" : "(optional, string) Model of the device",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "session_id" : "(optional, string) UUID of the session"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) External ID of the user"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}

## 세션 종료 이벤트

{% apitags %}
세션
{% endapitags %}

이는 사용자가 애플리케이션을 종료하여 현재 세션이 종료될 때 발생합니다. 이 데이터를 사용하여 세션이 종료되는 시점을 추적하고 적절한 세션 시작 이벤트와 함께 세션의 지속 시간을 계산합니다.

{% alert tip %}
사용자가 첫 세션을 시작하면 `FirstSession` 이벤트와 `SessionStart` 이벤트가 모두 발생합니다.
{% endalert %}

{% tabs %}
{% tab Mixpanel %}
```json
// Session End: users.behaviors.app.SessionEnd

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "$device" : "(optional, string) Model of the device",
    "duration" : "(optional, float) Duration of the session in seconds",
    "distinct_id" : "(required, string) External ID of the user",
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

{% tab 클라우드 스토리지 %}
```json
// Session End: users.behaviors.app.SessionEnd

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(required, string) API ID of the app on which this event occurred",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "device_model" : "(optional, string) Model of the device",
  "duration" : "(optional, float) Duration of the session in seconds",
  "external_user_id" : "(optional, string) External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "os_version" : "(optional, string) Version of the operating system of the device",
  "platform" : "(optional, string) Platform of the device",
  "session_id" : "(required, string) UUID of the session",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}

{% tab 진폭 %}
```json
// Session End: users.behaviors.app.SessionEnd

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
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
  "user_id" : "(optional, string) External ID of the user"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}

## 위치 이벤트

{% apitags %}
위치
{% endapitags %}

이 이벤트는 사용자가 지정된 위치를 방문할 때 트리거됩니다. 이를 사용하여 앱에서 위치 이벤트를 트리거하는 사용자를 추적할 수 있습니다.

{% tabs %}
{% tab Mixpanel %}
```json
// Location: users.behaviors.Location

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "ad_id" : "(optional, string) Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "alt_accuracy" : "(optional, float) Altitude accuracy of recorded location",
    "altitude" : "(optional, float) Altitude of recorded location",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "$device" : "(optional, string) Model of the device",
    "distinct_id" : "(required, string) External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "latitude" : "(required, float) Latitude of recorded location",
    "ll_accuracy" : "(optional, float) Accuracy of the latitude and longitude of recorded location",
    "longitude" : "(required, float) Longitude of recorded location",
    "$os" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab 클라우드 스토리지 %}
```json
// Location: users.behaviors.Location

{
  "ad_id" : "(optional, string) Advertising identifier",
  "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
  "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
  "alt_accuracy" : "(optional, float) Altitude accuracy of recorded location",
  "altitude" : "(optional, float) Altitude of recorded location",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(required, string) API ID of the app on which this event occurred",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "device_model" : "(optional, string) Model of the device",
  "external_user_id" : "(optional, string) External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "latitude" : "(required, float) Latitude of recorded location",
  "ll_accuracy" : "(optional, float) Accuracy of the latitude and longitude of recorded location",
  "longitude" : "(required, float) Longitude of recorded location",
  "os_version" : "(optional, string) Version of the operating system of the device",
  "platform" : "(optional, string) Platform of the device",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}

{% tab 진폭 %}
```json
// Location: users.behaviors.Location

{
  "adid" : "(optional, string) Advertising identifier",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "ad_id" : "(optional, string) Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "alt_accuracy" : "(optional, float) Altitude accuracy of recorded location",
    "altitude" : "(optional, float) Altitude of recorded location",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "device_model" : "(optional, string) Model of the device",
    "latitude" : "(required, float) Latitude of recorded location",
    "ll_accuracy" : "(optional, float) Accuracy of the latitude and longitude of recorded location",
    "longitude" : "(required, float) Longitude of recorded location",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "idfa" : "(optional, string) Advertising identifier",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) External ID of the user"
}
```
{% endtab %}
{% endtabs %}

#### 부동산 세부 정보
- `ad_id`, `ad_id_type` 및 `ad_tracking_enabled` 의 경우 네이티브 SDK를 통해 iOS IDFA 및 Android Google 광고 ID를 명시적으로 수집해야 합니다. Learn more about them here: [iOS]({{site.baseurl}}/developer_guide/platforms/swift/analytics/swift_idfv/), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id).
- 고객 성공 관리자 또는 계정 관리자에게 문의하여 `ad_id` 으로 보내기 위한 기능 플리퍼를 사용하도록 설정하고, Kafka를 사용하여 [Currents]({{site.baseurl}}/user_guide/data/braze_currents/) 데이터를 수집하는 경우에는 고객 성공 관리자 또는 계정 관리자에게 문의하세요.
{% endapi %}

{% api %}

## 기여도 이벤트

{% apitags %}
기여도
{% endapitags %}

이 이벤트는 앱 설치가 소스에 어트리뷰션될 때 발생합니다. 이를 사용하여 앱 설치의 출처를 추적할 수 있습니다.

{% tabs %}
{% tab Mixpanel %}
```json
// Install Attribution: users.behaviors.InstallAttribution

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "distinct_id" : "(required, string) External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "source" : "(optional, string) The source of the attribution",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab 클라우드 스토리지 %}
```json
// Install Attribution: users.behaviors.InstallAttribution

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "external_user_id" : "(optional, string) External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "source" : "(required, string) The source of the attribution",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}

{% tab 진폭 %}
```json
// Install Attribution: users.behaviors.InstallAttribution

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
  "user_id" : "(optional, string) External ID of the user"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}

## 무작위 버킷 번호 이벤트

{% apitags %}
무작위 버킷 번호
{% endapitags %}

이 사용자 이벤트는 워크스페이스 내에서 새 사용자가 생성될 때마다 발생합니다. 이 이벤트 기간 동안 각 신규 사용자에게는 무작위 버킷 번호가 할당되며, 이를 사용하여 균일하게 분포된 무작위 사용자 세그먼트를 생성할 수 있습니다. 이를 사용하여 다양한 무작위 버킷 번호 값을 그룹화하고 캠페인 및 캠페인 배리언트의 성과를 비교할 수 있습니다.

{% tabs %}
{% tab 클라우드 스토리지 %}
```json
// Random Bucket Number Update: users.RandomBucketNumberUpdate

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "external_user_id" : "(optional, string) External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "prev_random_bucket_number" : "(optional, int) Previous random bucket number",
  "random_bucket_number" : "(required, int) New random bucket number",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% alert important %}
이 Currents 이벤트는 '모든 이벤트 커넥터'를 구매한 고객에게만 제공되며, 스토리지 이벤트 커넥터(Amazon S3, Microsoft Azure 및 Google Cloud Storage)에 대해서만 사용할 수 있습니다.
<br><br>이 이벤트를 활성화하고 워크스페이스에서 기존 사용자의 무작위 버킷 번호에 대한 백필을 예약하려면 고객 성공 관리자에게 문의하세요.
{% endalert %}

{% endapi %}
