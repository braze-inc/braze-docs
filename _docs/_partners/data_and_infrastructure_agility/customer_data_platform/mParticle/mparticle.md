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
- [Sync mParticle cohorts to Braze](#cohort-import) for Braze campaign and Canvas segmentation.
- [Import event data across the two platforms](#data-import). This can be done through the mParticle kit integration and the server-to-server integration if you want to pipe backend data. 
- [Connect data to mParticle through Currents]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/mParticle/mparticle_for_currents/), making it actionable across the entire growth stack. 

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| mParticle account | A [mParticle account](https://app.mparticle.com/login) is required to take advantage of this partnership. |
{: .reset-td-br-1 .reset-td-br-2}

## Integration

### Cohort import

Use Braze and mParticle's partnership to configure your integration and import mParticle cohorts directly into Braze for retargeting, creating a full loop of data from one system to another. Any integration you set up will count towards your account's data point volume.

#### Forwarding Audiences

mParticle offers three ways to set cohort membership attributes, controlled by the "[Send Segments As](#send_settings)" configuration setting. The processing of each option is described below:

- __Single attribute__ (default): mParticle will create a single custom attribute called `SegmentMembership`. The value of this attribute is a list of mParticle audience IDs that match the user. These audience IDs can be found in the mParticle dashboard under __Audiences__. For example, if an mParticle audience "Ibiza dreamers" has an audience ID of "11036", you will be able to segment these users by the audience ID "11036". ![mParticle segment membership][6]<br><br>
- __One attribute per segment__: mParticle will create a custom attribute for each audience that a user belongs to. ![mParticle custom attribute][7]<br><br>
- __Both single attribute and one attribute per segment__

#### Step 1: Create an audience in mParticle {#send_settings}

To create an audience in mParticle, navigate to __Audiences > Single Workspace > + New Audience__. Here you must provide the following fields:

- __API key__: Found in the Braze __Developer Console__ under __Settings__.
- __API key operating system__: Select which operating system your Braze API key corresponds to. This selection will limit the types of push tokens forwarded on an audience update.
- __Send segments as__: The method of sending audiences to Braze: Single Attribute, One Attribute Per Segment, or Both. 
- __App group REST API key__:  Braze REST API key with full permissions. This can be created within the __Braze Dashboard -> Developer Console -> REST API Key -> Create New API Key__
- __External identity type__: The mParticle user identity type to forward as an external ID to Braze. We recommend leaving this to the default value, Customer ID.
- __Email identity type__: The mParticle user identity type to forward as the email to Braze.
- __Braze instance__: Specify which cluster your Braze data will be forwarded to

Lastly __Save__ your audience. 

Check out this article for more information on creating Braze [mParticle audiences](https://docs.mparticle.com/integrations/braze/audience/#configuration-settings).

#### Step 2: Segment users in Braze

In Braze, to create a segment of these users, navigate to **Segments** under **Engagement** and name your segment.
- __Single attribute__: Select `SegmentMembership` as your filter. Next, use the "matches regex" option and input your desired audience ID. ![mParticle segment filter 1][9]<br><br>
- __One attribute per segment__: Select your custom attribute as the filter. Next, use the "equals" option and choose the appropriate logic. ![mParticle segment filter 2][8]

Once saved, you can reference this segment during Canvas or campaign creation in the targeting users step.

#### Deactiviating and deleting connections

Since mParticle does not directly maintain segments in Braze, it will not delete segments when the corresponding mParticle audience connection is deleted or deactivated. When this happens, mParticle will not update the audience user attributes in Braze to remove the audience from each user.

### Data import

Data can be imported by using the [embedded kit integration](#embedded-kit-integration) if you want to connect your mobile and web apps to Braze. You can also use the [server API integration](#server-api-integration) to pipe backend data into Braze.

{% alert note %}
Regardless of which approach you choose, you must integrate the [mParticle embedded kit](#embedded-kit-integration).
{% endalert %}

#### Embedded kit integration

The mParticle and Braze SDK will be present on your application through the embedded kit integration. However, unlike a direct Braze integration, mParticle takes care of calling the majority of Braze SDK code for you. Any mParticle methods you use to track user data will automatically be mapped to Braze's SDK. 

These mappings of mParticle’s SDK for [Android](https://github.com/mparticle-integrations/mparticle-android-integration-appboy), [iOS](https://github.com/mparticle-integrations/mparticle-apple-integration-appboy) and [Web](https://github.com/Appboy/integration-appboy) are open source and can be found on [mParticle’s GitHub page](https://github.com/mparticle-integrations). 

The embedded SDK integration allows you to take advantage of our full suite of features (Push, In-app Messages, News Feed, and all relevant message analytics tracking).

##### Step 1: Integrate the mParticle SDKs

Integrate the appropriate mParticle SDKs into your app based on your platform needs:

* [mParticle for Android](https://docs.mparticle.com/developers/sdk/android/getting-started/)
* [mParticle for iOS](https://docs.mparticle.com/developers/sdk/ios/getting-started/)
* [mParticle for Web](https://docs.mparticle.com/developers/sdk/web/getting-started/)

##### Step 2: Complete mParticle's Braze event kit integration

While the Braze SDK is not required for this mParticle integration, the following mParticle Appboy Kit must be installed to forward data from your app to Braze.

mParticle's [Braze event kit integration guide](https://docs.mparticle.com/integrations/braze/event/#kit-integration) will walk you through custom mParticle and Braze alignment instructions based on your messaging needs (Push, Location Tracking, etc.).

##### Step 3: Configure your mParticle dashboard to enable the Braze kit

In mParticle, navigate to __Setup > Outputs > Add Output__ and select __Braze__ to open the Braze kit configuration. __Save__ once completed. 

![mParticle Event Config UI][3]

Provide the following fields on the Braze configuration page: 
- __API key__: Found in the Braze __Developer Console__ under __Settings__. Note that API keys will differ for each platform (iOS, Android, and Web).
- __External identity type__: The mParticle user identity type to forward as an external ID to Braze. We recommend leaving this to the default value, Customer ID.
- __Braze instance__: Custom
- __Custom REST endpoint__: Your REST endpoint URL. Your endpoint will depend on the [Braze URL for your instance]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints).
- __Custom SDK endpoint__: Given to you by your Braze support or account representative (e.g., `sdk.api.braze.com`). Leave this setting blank if you were not given a custom API endpoint.
- __Custom JavaScript endpoint__: Given to you by your Braze support or account representative. Leave this setting blank if you were not given a custom JavaScript endpoint.

#### Server API integration

This is an add-on to route your backend data to Braze if you're using mParticle's server-side SDKs (e.g., Ruby, Python, etc.). To set up this server-to-server integration with Braze, please follow mParticle's documentation [here](https://docs.mparticle.com/guides/platform-guide/connections/).

##### Connections settings for your Braze output

In mParticle, navigate to __Connections > Connect > [Your desired platform] > Connect Output__ to add Braze as an output. __Save__ once completed. 

![mParticle Connections Setting][4]

Provide the following fields on the Braze output page: 
- __App group REST API key__: A Braze REST API key with full permissions. This can be created within the __Braze Dashboard -> Developer Console -> REST API Key -> Create New API Key__.
- __Custom REST endpoint__: Your REST endpoint URL. Your endpoint will depend on the [Braze URL for your instance]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). This should match the __Custom REST endpoint__ provided in [this step](#step-3-configure-your-mparticle-dashboard-to-enable-the-braze-kit).

##### Data mapping

Not all data types that are supported on mParticle are supported by Braze.
- [Custom event properties]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/) support string, numeric, boolean, or date objects. It does not support arrays or nested objects.
- [Custom attributes]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/) support string, numerical, boolean, date objects and arrays, but does not support objects or nested objects. 

[1]: https://dashboard.braze.com/app_settings/developer_console
[2]: {% image_buster /assets/img_archive/dashboard_keys_locations.png %}
[3]: {% image_buster /assets/img_archive/mParticle_event_config.png %}
[4]: {% image_buster /assets/img_archive/mParticle_connections.png %}
[6]: {% image_buster /assets/img_archive/mparticle1.png %}
[7]: {% image_buster /assets/img_archive/mparticle2.png %}
[8]: {% image_buster /assets/img_archive/mparticle3.png %}
[9]: {% image_buster /assets/img_archive/mparticle4.png %}
[5]: #embedded-kit-integration