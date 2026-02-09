---
nav_title: mParticle by Rokt
article_title: mParticle by Rokt
alias: /partners/mparticle/
description: "This reference article outlines the partnership between Braze and mParticle, a customer data platform that collects and routes information between sources in your marketing stack."
page_type: partner
search_tag: Partner

---

# mParticle by Rokt

{% multi_lang_include video.html id="Njhqwd36gZM" align="right" %}

> mParticle's customer data platform empowers you to do more with your data. Sophisticated marketers use mParticle to orchestrate data across their entire growth stack, enabling them to win in key customer journey moments.

The Braze and mParticle integration allows you to seamlessly control the flow of information between the two systems:
- Sync mParticle audiences to Braze for Braze campaign and Canvas segmentation.
- Share data across the two platforms. This can be done through the mParticle kit integration and the server-to-server integration.
- [Send Braze user interaction to mParticle through Currents]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/mparticle/mparticle_for_currents/), making it actionable across the entire growth stack. 

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| mParticle account | An [mParticle account](https://app.mparticle.com/login) is required to take advantage of this partnership. |
| Braze instance | Your Braze instance can be found on the [API overview page]({{site.baseurl}}/api/basics/#endpoints) (for example, `US-01` or `US-02`). |
| Braze app identifier key | Your app identifier key. <br><br>이것은 Braze 대시보드의 **설정 관리** > **API 키**에서 찾을 수 있습니다. |
| Workspace REST API key | (Server-to-server) A Braze REST API key<br><br>이것은 Braze 대시보드의 **개발자 콘솔** > **API 설정** > **API 키**에서 생성할 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Audiences

Use Braze and mParticle's partnership to configure your integration and import mParticle audiences directly into Braze for retargeting, creating a full loop of data from one system to another. 

설정한 모든 통합은 데이터 포인트를 기록합니다. Braze 데이터 포인트의 뉘앙스에 대한 질문이 있는 경우, 귀하의 Braze 계정 매니저가 답변할 수 있습니다.

#### Forwarding Audiences

mParticle offers three ways to set cohort membership attributes, controlled by the "[Send Segments As](#send_settings)" configuration setting. Refer to the following sections for the processing of each option:

- [Single string attribute](#string)
- [Single array attribute](#array)
- [One attribute per segment](#per-segment)
- [Both single array attribute and single string attribute](#both-1)
- [Both single array attribute and one attribute per segment](#both-2)
- [Both single string attribute and one attribute per segment](#both-3)
- [Single array attribute, single string attribute, and one attribute per segment](#multi)

##### Single string attribute {#string}

mParticle will create a single custom attribute called `SegmentMembership`. The value of this attribute is a string of comma-separated mParticle audience IDs that match the user. These audience IDs can be found in the mParticle dashboard under **Audiences**.

For example, if an mParticle audience "Ibiza dreamers" has an audience ID of "11036", you can segment these users with the filter `SegmentMembership` — `matches regex` — `11036`.

While this is the default option in mParticle, most Braze users opt to use [single array attributes](#array) for the filtering experience when creating segments in Braze.

{% alert important %}
This solution is not recommended if you have more than a few audiences because custom attributes can be up to 255 characters long, so you will not be able to store dozens or hundreds of audiences on a user profile using this method. If you have a large number of cohorts per user, we strongly recommend the "one attribute per segment" configuration.
{% endalert %}

![mParticle 세그먼트 membership]({% image_buster /assets/img_archive/mparticle1.png %})

##### 단일 배열 속성 {#array}

mParticle creates a single custom array attribute in Braze for each user, called `SegmentMembershipArray`. The value of this attribute is an array of mParticle audience IDs that match the user.

For example, if a user is a member of three mParticle audiences with the audience IDs of "13053", "13052", and "13051", you can segment for users who match one of those audience with the filter `SegmentMembershipArray` — `includes value` — `13051`.

{% alert note %}
Braze array attributes have a maximum length of 25. If any of your users are members of over 25 audiences, membership information will be truncated by Braze. To work around this, contact your Braze representative to increase your maximum array length threshold.
{% endalert %}

##### One attribute per segment {#per-segment}

mParticle will create a boolean custom attribute for each audience a user belongs to. 예를 들어, mParticle 오디언스가 'Possible Parisians'인 경우, 이 사용자는 `In Possible Parisians` - `equals` - `true` 필터로 세분화할 수 있습니다.

![mParticle 커스텀 속성]({% image_buster /assets/img_archive/mparticle2.png %})

##### 단일 배열 속성과 단일 문자열 속성 {#both-1}

mParticle will send attributes as described by both single array attribute and single string attribute.

##### Both single array attribute and one attribute per segment {#both-2}

mParticle will send attributes as described by both single array attribute and one attribute per segment.

##### Both single string attribute and one attribute per segment {#both-3}

mParticle will send attributes as described by both single string attribute and one attribute per segment.

##### Single array attribute, single string attribute, and one attribute per segment {#multi}

mParticle will send attributes as described by single array attribute, single string attribute, and one attribute per segment.

#### Step 1: Create an audience in mParticle {#send_settings}

To create an audience in mParticle:

1. Navigate to **Audiences** > **Single Workspace** > **\+ New Audience**.
2. To connect Braze as an output for your audience, you must provide the following fields:

| Field Name               | Description                                                                                                                                                                   |
| ------------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| API key                  | Found in the Braze dashboard at **Settings** > **API Keys**.<br><br>If you are using the older navigation, you can find API keys at **Developer Console** > **API Settings**. |
| API key operating system | Select which operating system your Braze API key corresponds to. This selection will limit the types of push tokens forwarded on an audience update.                          |
| Send segments as         | The method of sending audiences to Braze. See the section [Forwarding audiences](#forwarding-audiences) for details.                                                          |
| Workspace REST API key   | Braze REST API key with full permissions. This can be created in the Braze dashboard from **Settings** > **API Keys**.                                                        |
| External identity type   | The mParticle user identity type to forward as an external ID to Braze. We recommend leaving this to the default value, Customer ID.                                          |
| Email identity type      | The mParticle user identity type to forward as the email to Braze.                                                                                                            |
| Braze instance           | Specify which cluster your Braze data will be forwarded to.                                                                                                                   |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{:start="3"}
3\. Lastly **Save** your audience.

You should begin seeing audiences syncing to Braze within a few minutes. Audience membership will only update for users with `external_ids` (that is, not anonymous users). For more information on creating Braze mParticle audience, see the mParticle documentation on [Configuration settings](https://docs.mparticle.com/integrations/braze/audience/#configuration-settings).

#### Step 2: Segment users in Braze

In Braze, to create a segment of these users, navigate to **Segments** under **Engagement** and name your segment. The following are two examples of segments depending on the option you selected for **Send segments as**. 각 옵션에 대한 자세한 내용은 [오디언스 전달](#forwarding-audiences)를 참조하십시오.

- **Single array attribute:** `SegmentMembershipArray`를 필터로 선택합니다. 다음으로, '값 포함' 옵션을 사용하고 원하는 오디언스 ID를 입력합니다. ![mParticle 세그먼트 필터 'SegmentMembershipArray'를 '값 포함'으로 설정하고 오디언스 ID를 입력합니다.]({% image_buster /assets/img_archive/mparticle5.png %})<br><br>
- **세그먼트당 하나의 속성:** 귀하의 커스텀 속성을 필터로 선택하십시오. 다음으로, '같음' 옵션을 사용하고 적절한 논리를 선택합니다. ![mParticle 세그먼트 필터 'in possible parisians'을 '같음' 및 'true'로 설정합니다.]({% image_buster /assets/img_archive/mparticle3.png %})

저장한 후에는 사용자 타겟팅 단계에서 캔버스 또는 캠페인을 생성하는 동안 이 세그먼트를 참조할 수 있습니다.

#### Deactivating and deleting connections

mParticle는 Braze에서 세그먼트를 직접 유지 관리하지 않기 때문에, 해당 mParticle 오디언스 연결이 삭제되거나 비활성화될 때 세그먼트를 삭제하지 않습니다. When this happens, mParticle will not update the audience user attributes in Braze to remove the audience from each user.

To remove the audience from a Braze user before deletion, adjust the audience filters to force the audience size to 0 before deleting an audience. After the audience calculation has completed and returns 0 users, delete the audience. 그런 다음, 오디언스 멤버십은 단일 속성 옵션에 대해 Braze에서 `false`로 업데이트되거나 배열 형식에서 오디언스 ID를 제거합니다.

## Data mapping

Data can be mapped to Braze using the [embedded kit integration](#embedded-kit-integration) if you want to connect your mobile and web apps to Braze through mParticle. You can also use the [server-to-server API integration](#server-api-integration) to forward server-side data to Braze.

Regardless of which approach you choose, you must set up Braze as an output:

### Configure your Braze output settings

mParticle에서 **설정 > 출력 > 출력 추가**로 이동하고 **Braze**를 선택하여 Braze 키트 구성을 엽니다. **Save** when completed.

| Setting name | Description |
| ------------ | ----------- |
| Braze app identifier key | Your Braze app identifier key can be found in the Braze dashboard from **Settings** > **API Keys**. Note that API keys will differ for each platform (iOS, Android, and Web). |
| External identity type | The mParticle user identity type to forward as an external ID to Braze. We recommend leaving this to the default value, Customer ID |
| Email identity type | The mParticle user identity type to forward as an email to Braze. We recommend leaving this to the default value, Email, |
| Braze instance | The cluster your Braze data will be forwarded to; this should be the same cluster your dashboard is on. |
| Enable event stream forwarding | (Server-to-server) When enabled, all events will be forwarded in real-time. If not, all events will be forwarded in bulk. When choosing to enable event stream forwarding, ensure that the data you are passing to Braze will respect [rate limits]({{site.baseurl}}/api/api_limits/). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![]({% image_buster /assets/img_archive/configure_settings.png %})

### Embedded kit integration

mParticle 및 Braze SDK는 내 애플리케이션에 내장된 키트 통합을 통해 존재합니다. However, unlike a direct Braze integration, mParticle takes care of calling the majority of Braze SDK methods for you. The mParticle methods you use to track user data will automatically be mapped to the Braze SDK methods. 

mParticle의 SDK에 대한 이러한 매핑은 [Android](https://github.com/mparticle-integrations/mparticle-android-integration-appboy), [iOS](https://github.com/mparticle-integrations/mparticle-apple-integration-appboy), 및 [Web](https://github.com/mparticle-integrations/mparticle-javascript-integration-braze)에 대해 오픈 소스이며 [mParticle의 GitHub 페이지](https://github.com/mparticle-integrations)에서 찾을 수 있습니다. 

The embedded kit SDK integration allows you to take advantage of our full suite of features (push, in-app messages, and all relevant message analytics tracking).

{% alert note %}
For Content Cards and custom in-app message integrations, call the Braze SDK methods directly.
{% endalert %}

#### Step 1: Integrate the mParticle SDKs

Integrate the appropriate mParticle SDKs into your app based on your platform needs:

* [mParticle for Android](https://docs.mparticle.com/developers/sdk/android/getting-started/)
* [mParticle for iOS](https://docs.mparticle.com/developers/sdk/ios/getting-started/)
* [mParticle for Web](https://docs.mparticle.com/developers/sdk/web/getting-started/)

#### Step 2: Complete mParticle's Braze event kit integration

While the Braze SDK does not need to be directly included within your website or app for this mParticle integration, the following mParticle Appboy Kit must be installed to forward data from your app to Braze.

mParticle's [Braze event kit integration guide](https://docs.mparticle.com/integrations/braze/event/#kit-integration) will walk you through custom mParticle and Braze alignment instructions based on your messaging needs (Push, Location Tracking, etc.).

#### Step 3: Connections settings for your Braze output

mParticle에서 **연결** > **연결** > **[원하는 플랫폼]** > **출력 연결**로 이동하여 Braze를 출력으로 추가합니다. 그런 다음 **저장**을 선택합니다.

![]({% image_buster /assets/img_archive/mParticle_event_config.png %})

Not all connection settings will apply to all platforms and integration types. For a breakdown of connection settings and the platforms they apply to, see [mParticle's documentation](https://docs.mparticle.com/integrations/braze/event/#connection-settings).

### Server API integration

This is an add-on to route your backend data to Braze if you're using mParticle's server-side SDKs (for example, Ruby, Python, etc.). To set up this server-to-server integration with Braze, follow [mParticle's documentation](https://docs.mparticle.com/guides/platform-guide/connections/).

{% alert important %}
서버 간 통합은 인앱 메시징, 콘텐츠 카드 또는 푸시 알림과 같은 Braze UI 기능을 지원하지 않습니다. There also exists automatically captured data, such as device-level fields, that are unavailable through this method. 

Consider a side-by-side integration if you wish to use these features.

For server-side data to be forwarded to Braze, it must include an `external_id`; anonymous users will not be forwarded.
{% endalert %}

#### Connections settings for your Braze output

mParticle에서 **연결 > 연결 > [원하는 플랫폼] > 출력 연결**로 이동하여 Braze를 출력으로 추가합니다. **Save** when completed. 

![]({% image_buster /assets/img_archive/mParticle_connections.png %})

Not all connection settings will apply to all platforms and integration types. For a breakdown of connection settings and the platforms they apply to, see [mParticle's documentation](https://docs.mparticle.com/integrations/braze/event/#connection-settings).

Before enabling "Enriched User Attributes" or "Enriched User Identities" we recommend reviewing [Data point overages](#potential-data-point-overages) to ensure you are aware of how these settings will impact data point usage.

### Data mapping details

#### Data types
Not all data types are supported between both platforms.
- [Custom event properties]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) support string, numeric, boolean, or date objects. It does not support arrays or nested objects.
- [커스텀 속성]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/)은 문자열, 숫자, 불리언, 날짜 객체 및 배열을 지원하지만 객체나 중첩 객체는 지원하지 않습니다. 

{% alert note %}
Braze doesn't support timestamps before year 0 or after year 3000 in `Time` type custom attributes. Braze는 mParticle에서 전송된 이러한 값을 수집하지만, 값은 문자열로 저장됩니다.
{% endalert %}

#### Data mapping

| mParticle data type | Braze data type | Description |
| ------------------- | --------------- | ----------- |
| User attributes (reserved) | Standard attribute | For example, mParticle's `$FirstName` reserved user attribute key is mapped to `first_name` standard attribute field for Braze. |
| User attributes (other) | Custom Attribute | Any user attributes passed to mParticle that fall outside of its reserved user attribute keys are logged in Braze as a custom attribute.<br><br>User attributes support string, numerical, boolean, date, and arrays but do not support objects or nested objects. |
| Custom event | Custom event | mParticle custom events are recognized by Braze as a custom event. Event attributes are forwarded as custom event properties.<br><br>Event attributes passed to Braze as event properties support string, numeric, boolean, or date objects but do not support arrays or nested objects. |
| Purchase commerce event | Purchase event | Purchase commerce events will be mapped to Braze purchase events. <br><br>Toggle the setting value for bundle commerce event data to log purchases at the order-level or product-level. For example, if `false`, a single incoming event with two unique products, promotions, or impressions would result in at least two outgoing Braze events. If set to `true`, it would result in a single outgoing event with a nested products, promotions or impressions array, respectively.<br><br>For more information on the additional commerce fields that will be logged, see [mParticle's documentation](https://docs.mparticle.com/integrations/braze/event/#purchase-events). <br><br>When setting "bundle commerce event data" as `false` product attributes passed to Braze as purchase event properties, support string, numeric, boolean, or date objects but do not support arrays or nested objects.|
| All other commerce events | Custom event | All other commerce events will be mapped to custom events. <br><br>Toggle the setting value for bundle commerce event data to log purchases at the order-level or product-level. For example, if `false`, a single incoming event with two unique products, promotions, or impressions would result in at least two outgoing Braze events. If set to `true`, it would result in a single outgoing event with a nested products, promotions or impressions array, respectively.<br><br>In addition to certain default commerce values, product attributes will be logged as Braze event properties. For more information on the additional commerce fields that will be logged, see [mParticle's documentation](https://docs.mparticle.com/integrations/braze/event/#other-commerce-events)<br><br>When setting "bundle commerce event data" as `false` product attributes passed to Braze as event properties, support string, numeric, boolean, or date objects but do not support arrays or nested objects. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

#### User identity mapping
For each mParticle output, you can select the external identity type to send to Braze as the `external_id`. While the default value is customer ID, you can choose to map another ID, such as `MPID`, to send to Braze as the `external_id`. 고객 ID 외의 식별자를 선택하면 Braze에서 데이터가 전송되는 방식에 영향을 미칠 수 있습니다. 

For example, mapping MPID to your Braze `external_id` will have the following effects:
- Due to the nature of when MPID is assigned, all users will be assigned an `external_id` on session start.
- Currents setup may require additional mapping due to differing data types between MPID and `external_id`.

### Forwarding erasure requests (data subject requests)

Forward erasure requests to Braze by configuring a data subject request output to Braze. To forward erasure requests to Braze, follow [mParticle's documentation](https://docs.mparticle.com/integrations/braze/forwarding-dsr/).

## Potential data point overages

### Enriched user attributes

#### Enabling enrich user attributes/identities (server-to-server only) {#enriched}

In the mParticle connection settings, Braze recommends turning off **Include Enriched User Attributes**. If enabled, mParticle will forward all available user attributes (such as standard attributes, custom attributes, and calculated attributes) from the existing profile to Braze on each logged event. 이로 인해 mParticle이 각 호출에서 동일한 변경되지 않은 속성을 Braze에 전송하므로 데이터 포인트 소비가 높아집니다.

예를 들어, 사용자가 첫 번째 세션 중에 이름, 성 및 전화번호를 추가하고 나중에 뉴스레터에 가입하고 동일한 정보와 이메일을 추가하여 뉴스레터 가입 이벤트를 트리거하는 경우:
- If turned on (default), five data points will be incurred. (sign-up event, email address, first name, last name, and phone number)
- If turned off, two data points will be incurred (sign-up event and email address)

{% alert note %}
Turning off this setting won't check for changing data. It will, however, prevent the integration from sending all user attributes on the user's profile that weren't received on the original inbound batch or explicitly set as an attribute for the event. It is important to still check that only deltas are passed to Braze.
{% endalert %}

#### Considerations of turning off enriched user attributes

There are a few considerations to be aware of when turning off **Include Enriched User Attributes**:
1. The server-to-server integration uses the mParticle events API to send events to Braze. Each request is triggered by an event. When a user attribute is changed, such as updating an email address, but is not associated with a specific event (for example, a profile update custom event), the new value is only passed to an output like Braze as an "enriched attribute" in the payload of the next event triggered by the user. When **Include Enriched User Attributes** is turned off, this new attribute value unassociated with a specific event will not be passed to Braze.
  - To solve this, we recommend creating a separate "user attribute updated" event that only sends the specific user attribute(s) that have been updated to Braze. 이 접근 방식을 사용하면 "사용자 속성 업데이트" 이벤트에 대해 추가 데이터 포인트를 여전히 기록하고 있지만, 기능이 활성화된 상태에서 모든 사용자 속성을 매 호출마다 전송하는 것보다 데이터 포인트 사용량이 훨씬 적습니다.
2. Calculated Attributes are passed to Braze as an enriched user attribute, so when "Enriched User Attributes" is turned off these will no longer be passed to Braze. To forward calculated attributes to Braze when "Enriched User Attributes" are turned off, a [calculated attribute feed](https://docs.mparticle.com/guides/platform-guide/calculated-attributes/using-calculated-attributes/#forward-calculated-attributes-in-the-calculated-attributes-feed) could help without pushing all the attributes. The feed will fire an update downstream to Braze when a calculated attribute changes. 

### Sending unnecessary or duplicate data to Braze
Braze counts a data point each time an attribute is passed to Braze, even if the value is unchanged. For this reason, Braze recommends only forwarding data needed to action on within Braze and ensuring that only deltas of attributes are being passed.

