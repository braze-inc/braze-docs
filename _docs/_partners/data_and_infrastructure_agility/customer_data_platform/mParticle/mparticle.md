---
nav_title: mParticle
article_title: mParticle
page_order: 0
alias: /partners/mparticle/
description: "This article outlines the partnership between Braze and mParticle, a customer data platform that collects and routes information between sources in your marketing stack."
page_type: partner
search_tag: Partner

---

# mParticle

{% include video.html id="Njhqwd36gZM" align="right" %}

> mParticle's customer data platform empowers you to do more with your data. Sophisticated marketers use mParticle to orchestrate data across their entire growth stack, enabling them to win in key customer journey moments.

The Braze and mParticle integration allows you to seamlessly control the flow of information between the two systems:
- [Sync mParticle audiences to Braze](#cohort-import) for Braze campaign and Canvas segmentation.
- [Share data across the two platforms](#data-import). This can be done through the mParticle kit integration and the server-to-server integration.
- [Send Braze user interaction to mParticle through Currents]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/mParticle/mparticle_for_currents/), making it actionable across the entire growth stack. 

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| mParticle account | An [mParticle account](https://app.mparticle.com/login) is required to take advantage of this partnership. |
| Braze instance | Your Braze instance can be found on the [API overview page]({{site.baseurl}}/api/basics/#endpoints). |
| Braze app identifier key | Your app identifier key. <br><br>This can be found within the **Braze Dashboard > Manage Settings > API Key**. |
| App group REST API key | (Server-to-server) A Braze REST API key<br><br>This can be created within the **Braze Dashboard > Developer Console > API Settings > API Key**. |
{: .reset-td-br-1 .reset-td-br-2}

## Integration

### Audiences

Use Braze and mParticle's partnership to configure your integration and import mParticle audiences directly into Braze for retargeting, creating a full loop of data from one system to another. Any integration you set up will count towards your account's data point volume.

#### Forwarding Audiences

mParticle offers three ways to set cohort membership attributes, controlled by the "[Send Segments As](#send_settings)" configuration setting. The processing of each option is described below:

- **Single attribute** (default): mParticle will create a single custom attribute called `SegmentMembership`. The value of this attribute is a list of mParticle audience IDs that match the user. These audience IDs can be found in the mParticle dashboard under **Audiences**. For example, if an mParticle audience "Ibiza dreamers" has an audience ID of "11036", you will be able to segment these users by the audience ID "11036". ![mParticle segment membership][6]<br><br>
- **One attribute per segment**: mParticle will create a boolean custom attribute for each audience that a user belongs to. ![mParticle custom attribute][7]<br><br>
- **Both single attribute and one attribute per segment**

#### Step 1: Create an audience in mParticle {#send_settings}

To create an audience in mParticle, navigate to **Audiences > Single Workspace > + New Audience**.

To connect Braze as an output for your audience, you must provide the following fields:

- **API key**: Found in the Braze **Developer Console** under **Settings**.
- **API key operating system**: Select which operating system your Braze API key corresponds to. This selection will limit the types of push tokens forwarded on an audience update.
- **Send segments as**: The method of sending audiences to Braze: Single Attribute, One Attribute Per Segment, or Both. 
- **App group REST API key**:  Braze REST API key with full permissions. This can be created within the **Braze Dashboard > Developer Console > REST API Key > Create New API Key**
- **External identity type**: The mParticle user identity type to forward as an external ID to Braze. We recommend leaving this to the default value, Customer ID.
- **Email identity type**: The mParticle user identity type to forward as the email to Braze.
- **Braze instance**: Specify which cluster your Braze data will be forwarded to

Lastly **Save** your audience. 

Check out this article for more information on creating Braze [mParticle audiences](https://docs.mparticle.com/integrations/braze/audience/#configuration-settings).

#### Step 2: Segment users in Braze

In Braze, to create a segment of these users, navigate to **Segments** under **Engagement** and name your segment.
- **Single attribute**: Select `SegmentMembership` as your filter. Next, use the "matches regex" option and input your desired audience ID. ![mParticle segment filter "SegmentMembership" set as "matches Regex" and audience ID.][9]<br><br>
- **One attribute per segment**: Select your custom attribute as the filter. Next, use the "equals" option and choose the appropriate logic. ![mParticle segment filter "in possible parisians" set as "equals" and "true".][8]

Once saved, you can reference this segment during Canvas or campaign creation in the targeting users step.

#### Deactivating and deleting connections

Since mParticle does not directly maintain segments in Braze, it will not delete segments when the corresponding mParticle audience connection is deleted or deactivated. When this happens, mParticle will not update the audience user attributes in Braze to remove the audience from each user.

To remove the audience from a Braze user prior to deletion, adjust the audience filters to force the audience size to 0 before deleting an audience. After the audience calculation has completed and returns 0 users, delete the audience. This ensures the audience membership updates in Braze to `false` for the single attribute option, or removes the audience id from the array format.

### Data mapping

Data can be mapped to Braze by using the [embedded kit integration](#embedded-kit-integration) if you want to connect your mobile and web apps to Braze through mParticle. You can also use the [server-to-server API integration](#server-api-integration) to forward server-side data to Braze.

Regardless of which approach you choose, you must setup Braze as an output:

#### Configure your Braze output settings

In mParticle, navigate to **Setup > Outputs > Add Outputs** and selected **Braze** to open the Braze kit configuration. **Save** once completed.

| Setting name | Description |
| ------------ | ----------- |
| Braze app identifier key | Your Braze app identifier key can be found in the **Braze Developer Console** under **Settings**. Note that API keys will differ for each platform (iOS, Android, and Web). |
| External identity type | The mParticle user identity type to forward as an external ID to Braze. We recommend leaving this to the default value, Customer ID |
| Email identity type | The mParticle user identity type to forward as an email to Braze. We recommend leaving this to the default value, Email, |
| Braze instance | The cluster your Braze data will be forwarded to, this should be the same cluster your dashboard is on. |
| Enable event stream forwarding | (Server-to-server) When enabled, all events will be forwarded in real time. If not, all events will be forwarded in bulk. When choosing to enable event stream forwarding ensure that the data you are passing to Braze will respect [rate-limits]({{site.baseurl}}/api/basics/#api-limits). |
{: .reset-td-br-1 .reset-td-br-2}

![][10]

#### Embedded kit integration

The mParticle and Braze SDK will be present on your application through the embedded kit integration. However, unlike a direct Braze integration, mParticle takes care of calling the majority of Braze SDK methods for you. The mParticle methods you use to track user data will automatically be mapped to Braze's SDK. 

These mappings of mParticle’s SDK for [Android](https://github.com/mparticle-integrations/mparticle-android-integration-appboy), [iOS](https://github.com/mparticle-integrations/mparticle-apple-integration-appboy) and [Web](https://github.com/Appboy/integration-appboy) are open source and can be found on [mParticle’s GitHub page](https://github.com/mparticle-integrations). 

The embedded kit SDK integration allows you to take advantage of our full suite of features (push, in-app messages, News Feed, and all relevant message analytics tracking).

{% alert note %}
For Content Cards and custom in-app message integrations call Braze’s SDK methods directly.
{% endalert %}

##### Step 1: Integrate the mParticle SDKs

Integrate the appropriate mParticle SDKs into your app based on your platform needs:

* [mParticle for Android](https://docs.mparticle.com/developers/sdk/android/getting-started/)
* [mParticle for iOS](https://docs.mparticle.com/developers/sdk/ios/getting-started/)
* [mParticle for Web](https://docs.mparticle.com/developers/sdk/web/getting-started/)

##### Step 2: Complete mParticle's Braze event kit integration

While the Braze SDK does not need to be directly included within your website or app for this mParticle integration, the following mParticle Appboy Kit must be installed to forward data from your app to Braze.

mParticle's [Braze event kit integration guide](https://docs.mparticle.com/integrations/braze/event/#kit-integration) will walk you through custom mParticle and Braze alignment instructions based on your messaging needs (Push, Location Tracking, etc.).

##### Step 3: Connections settings for your Braze output

In mParticle, navigate to **Connections > Connect > [Your desired platform] > Connect Output** to add Braze as an output. **Save** once completed.

![][3]

Provide the following fields on the Braze connection settings page:

<!-- do not include
- **API key**: Found in the Braze **Developer Console** under **Settings**. Note that API keys will differ for each platform (iOS, Android, and Web).
- **External identity type**: The mParticle user identity type to forward as an external ID to Braze. We recommend leaving this to the default value, Customer ID.
- **Braze instance**: Custom
- **Custom REST endpoint**: Your REST endpoint URL. Your endpoint will depend on the [Braze URL for your instance]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints).
- **Custom SDK endpoint**: Given to you by your Braze support or account representative (e.g., `sdk.api.braze.com`). Leave this setting blank if you were not given a custom API endpoint.
- **Custom JavaScript endpoint**: Given to you by your Braze support or account representative. Leave this setting blank if you were not given a custom JavaScript endpoint.
-->

#### Server API integration

This is an add-on to route your backend data to Braze if you're using mParticle's server-side SDKs (e.g., Ruby, Python, etc.). To set up this server-to-server integration with Braze, please follow mParticle's documentation [here](https://docs.mparticle.com/guides/platform-guide/connections/).

{% alert important %}
Server-to-server integration does not support Braze UI features such as in-app messaging, News Feed, Content Cards, or push notifications. There also exists automatically captured data, such as device-level fields, that are not available through this method. 

Consider a side-by-side integration if you wish to use these features.

For server-side data to be forwarded to Braze, it must include an `external_id`, anonymous users will not be forwarded.
{% endalert %}

##### Connections settings for your Braze output

In mParticle, navigate to **Connections > Connect > [Your desired platform] > Connect Output** to add Braze as an output. **Save** once completed. 

![][4]

Provide the following fields on the Braze output page: 
- **App group REST API key**: Reuired for a server-to-server connection. A Braze REST API key with full permissions. This can be created within the **Braze Dashboard > Developer Console > REST API Key > Create New API Key**.
- **Braze SDK session timeout**: Braze SDK time interval for session timeout in seconds.
- **User tags value**: Select the value to be sent to Braze for user tags. The possible values are null or `true`. When `null` and set on a user attribute, the custom attribute (key and value) on the Braze user profile will be removed.
- **Include enriched user attributes**: Server-to-server only. If enabled, mParticle will forward enriched user attributes from the existing user profile. Braze recommends disabling this to conserve data points, for more info see potential data point overages section below.
- **Include enriched user identities**: Server-to-server only. If enabled, mParticle will forward enriched user identities from the existing user profile. Braze recommends disabling this to conserve data points, for more info see potential data point overages section below.
- **Send user attribute lists as arrays**: When enabled mParticle will send each user attribute list as an array, rather than a comma-separated string
- **Forward session events**: When enabled, all session start and end events will be forwarded to Braze as separate events. 
- **Forward screen view messages**: Not supported for server-to-server events. When enabled, all screen view messages will be forwarded to Braze as separate events.
- **Enable API custom attribute type detection**:
- **Enable kit custom attribute type detection**: 

##### Data mapping

Not all data types that are supported on mParticle are supported by Braze.
- [Custom event properties]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/) support string, numeric, boolean, or date objects. It does not support arrays or nested objects.
- [Custom attributes]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/) support string, numerical, boolean, date objects and arrays, but does not support objects or nested objects. 

### Forwarding erasure requests (data subject requests)

Forward erasure requests to Braze by configuring a data subject request output to Braze.

## Potential data point overages

[1]: https://dashboard.braze.com/app_settings/developer_console
[2]: {% image_buster /assets/img_archive/dashboard_keys_locations.png %}
[3]: {% image_buster /assets/img_archive/mParticle_event_config.png %}
[4]: {% image_buster /assets/img_archive/mParticle_connections.png %}
[6]: {% image_buster /assets/img_archive/mparticle1.png %}
[7]: {% image_buster /assets/img_archive/mparticle2.png %}
[8]: {% image_buster /assets/img_archive/mparticle3.png %}
[9]: {% image_buster /assets/img_archive/mparticle4.png %}
[10]: {% image_buster /assets/img_archive/configure_settings.png %}
[5]: #embedded-kit-integration