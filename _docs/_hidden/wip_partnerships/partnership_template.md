---
nav_title: Your Partner Page
page_order: 1

description: "This is the Google Search and SEO description that will appear, try to make this informative and concise, yet brief."
alias: /partners/your_partner_name/

page_type: partner
hidden: true
---

# [Partner Name]

> Welcome to the Partner Page Template! Here, you'll find everything you need to create your partner page. In this first section, you should describe the partner in the first paragraph in a sentence or two. Also, include a link to that partner's main site.

In the second paragraph, you should explore and explain the relationship between Braze and this partner. This paragraph should explain how Braze and this partner work together to tighten the bond between the Braze User and their customer. Explain the "elevation" that occurs when a Braze User integrates with or leverages this partner and their services.

## Requirements or Pre-Requisites

This section is all about what you need to integrate with the partner and start using their services. The best way to deliver this information is with a quick instructional paragraph that describes any non-technical important details of "need to know" information, like whether or not your integration will be subject to additional security checks or clearances. Then, you should use a chart to describe the technical requirements of the integration.

{% alert important %}
The requirements listed below are typical requirements you might need from Braze. We recommend using the attributed titling, origin, links, and phrasing as listed in the chart below. Be sure to adjust the description so that you know what each of these requirements is used to do.
{% endalert %}

| Requirement | Origin | Access | Description |
|---|---|---|---|
<<<<<<< HEAD
| RudderStack account | RudderStack | [https://app.rudderstack.com/][2] | A RudderStack account is required to set up the RudderStack-Braze integration. |
| Configured source | RudderStack | [https://docs.rudderstack.com/how-to-guides/adding-source-and-destination-rudderstack][3] | A source is essentially the origin of any data sent to RudderStack, such as websites, mobile apps, or backend servers. You are required to configure the source before setting up Braze as a destination in RudderStack. |
| Braze SDK Integration with your device | Braze | To know more about using the Braze SDKs, refer to our documentation on the [web][4], [iOS][5], and [Android][6] platforms. | Braze must be set up on your website or app for the integration to be successful. |

### Step 2.1. Choose the Type of Integration

You can choose to integrate RudderStack's web and native client-side libraries with Braze using either a side-by-side ("Device Mode") integration or a server-to-server ("Cloud Mode") integration.

| Integration Type | Description |
|---|---|
| Side-by-Side / Device Mode | In this mode, RudderStack will send the event data to Braze directly from your client (browser or mobile application). |
| Server-to-Server / Cloud Mode | In this mode, the Braze SDK sends the event data directly to RudderStack, which is then transformed and routed to Braze. |

{{site.data.alerts.note}} Learn more about RudderStack's connection modes and the benefits of each [here][7]. {{site.data.alerts.end}}

#### 2.1.1. Side-by-Side Integration (Device Mode)

In this mode, you can send your events to braze using the Braze SDK set up on your website or mobile app.

{% tabs %}
  {% tab Android %}
    Set up the mappings to the [RudderStack SDK for Android][8] on Braze's GitHub repository, as described in Step 3. <br>
    To complete the Device Mode integration, please refer to the detailed RudderStack instructions for [adding Braze to your Android project][11].
  {% endtab %}
  {% tab iOS %}
    Set up the mappings to the [RudderStack SDK for iOS][9] on Braze's GitHub repository, as described in Step 3. <br>
    To complete the Device Mode integration, please refer to the detailed RudderStack instructions for [adding Braze to your iOS project][11].
  {% endtab %}
  {% tab Web / JavaScript %}
    Set up the mappings to the [RudderStack SDK for JavaScript][10] on Braze's GitHub repository, as described in Step 3. <br>
    To learn more about how the web SDK works, please refer to the detailed RudderStack instructions on the [JavaScript SDK][12].
  {% endtab %}
{% endtabs %}

#### 2.1.2. Server-to-Server Integration (Cloud Mode)

In this mode, the Braze SDK sends the event data directly to RudderStack. RudderStack then transforms this data and routes it to Braze in the expected format. The transformation is done in the RudderStack backend.

To enable the integration, set up your App Group's REST API Key and Braze's REST API endpoint in your Connection Settings (Refer Step 2.2) on the RudderStack dashboard. You will also need to map the RudderStack methods to Braze (Refer Step 3).

{{site.data.alerts.note}} All of RudderStack's server-side SDKs (Java, Python, Node.js, Go, Ruby) support only Cloud Mode. This is because their server-side SDKs operate in the RudderStack backend, and cannot load any Braze-specific SDK. {{site.data.alerts.end}}

{% alert important %} The server-to-server integration does not support Braze's UI features, such as push notifications or in-app messaging. These features are, however, supported by the Device Mode integration. {%endalert%}

### Step 2.2. Configure Braze Settings in RudderStack

Once you've decided on the integration mode and successfully set up the source and the Braze SDK on your device, you will need to configure Braze as a destination in RudderStack. The setup is quite straightforward - you will need to enter the following required fields:

![Braze Settings][1]

| Name | Description |
|---|---|
| App Key | Can be found in the [Developer Console][13] under <b>App Settings</b> - <b>Manage App Group</b> |
| REST API Key | This needs to be created in the Braze dashboard under <b>App Settings</b> - [Developer Console][13] - <b>API Settings</b>. You can find the detailed instructions [here][14]. |
| Data Center | You will need to enter the Data Center details as provided by Braze. It is of the format `INSTANCE`, as explained in the [Braze Instances guide][15]. |
| Native SDK | You can enable or disable this option to use the Braze native SDK to send the events (use the Device Mode). |

### Step 3. Using the Integration - Set Up the Mappings
=======
| Braze API Key | Braze | You will need to create a new API Key.<br><br>This can be created in the __Developer Console -> API Settings -> Create New API Key__ with __users.track__ permissions. | This description should tell you what to do with the Braze API Key. |
| Braze REST Endpoint | Braze | [Braze REST Endpoint List][1] | Your REST Endpoint URL. Your endpoint will depend on the Braze URL for your instance. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## [Type of Integration] Integration
>>>>>>> 19270085... Moved the files to the relevant folders

This is where you break down the integration into steps. Do not just write endless paragraphs - these are technical documents that will be used by marketers and developers alike to get the integration up and running. Your only goal for this section is to write descriptive documentation that helps the Braze User get the job done. By 'Type of Integration' in the section title, we mean to indicate whether or not this is a Side-by-Side integration, server-to-server, or Out-of-the-Box. This enables you to have multiple Integration Sections if there is more than one way to integrate with this partner.

### Step 1: This Is a Short Description of Step One

Just break this down, including any code as necessary. Remember that you can offer several different sets of code - there's no need to only offer one way to integrate.

<<<<<<< HEAD
| RudderStack Field | Braze Field |
|---|---|
| `firstName` | `first_name` |
| `lastName` | `last_name` |
| `birthday` | `dob` |
| `avatar` | `image_url` |
| `address.city` | `home_city` |
| `address.country` | `country` |
| `gender` | `gender` |
=======
### Step 2: This Step Will Describe Images
>>>>>>> 19270085... Moved the files to the relevant folders

You have the option to put images in your documentation, so we recommend you do and do so mindfully.

### Step 3: How Many Steps

Outline thorough usage of the integration - especially if it means inserting liquid into our message composer.

## Customization

This is an __optional__ section. Here, you could outline any specific ways to customize your integration between the two partners.

## Using This Integration

This should describe how to use the integration - let your reader know if they need to push a few buttons or if they don't need to do anything at all after the integration.

### Step 1: This Is a Short Description of Step One

Just your typical step by step how to.

## Use Cases

<<<<<<< HEAD
[1]: {% image_buster /assets/img/partner_file/Braze Settings.png %}
[1]: https://rudderstack.com/
[2]: https://app.rudderstack.com/
[3]: https://docs.rudderstack.com/how-to-guides/adding-source-and-destination-rudderstack
[4]: https://www.braze.com/docs/developer_guide/platform_integration_guides/web/initial_sdk_setup/
[5]: https://www.braze.com/docs/developer_guide/platform_integration_guides/ios/initial_sdk_setup/
[6]: https://www.braze.com/docs/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/
[7]: https://docs.rudderstack.com/get-started/rudderstack-connection-modes
[8]: https://github.com/rudderlabs/rudder-integration-braze-android
[9]: https://github.com/rudderlabs/rudder-integration-braze-ios
[10]: https://github.com/rudderlabs/rudder-sdk-js
[11]: https://docs.rudderstack.com/destinations/braze#adding-device-mode-integration
[12]: https://docs.rudderstack.com/rudderstack-sdk-integration-guides/rudderstack-javascript-sdk
[13]: https://dashboard.braze.com/app_settings/developer_console
[14]: https://www.braze.com/docs/api/basics/?redirected=true#creating-and-managing-rest-api-keys
[15]: https://www.braze.com/docs/user_guide/administrative/access_braze/braze_instances/
[16]: https://docs.rudderstack.com/rudderstack-api-spec
[17]: https://www.braze.com/docs/user_guide/data_and_analytics/custom_data/custom_attributes/
[18]: https://docs.rudderstack.com/destinations/braze#identify
[19]: https://docs.rudderstack.com/destinations/braze#track
[20]: https://docs.rudderstack.com/rudderstack-api-spec/rudderstack-ecommerce-events-specification
[21]: https://www.braze.com/docs/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data/#revenue-data
[22]: https://docs.rudderstack.com/destinations/braze#page
=======
This can be a critical part of your documentation. Though this is optional, this is a good place to outline typical or even novel use cases for the integration. This can be used as a way to sell or upsell the relationship - it provides context, ideas, and most importantly a way to visualize the capabilities of the integration.

[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)
>>>>>>> 19270085... Moved the files to the relevant folders
