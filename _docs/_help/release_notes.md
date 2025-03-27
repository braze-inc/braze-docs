---
nav_title: Release Notes
article_title: Release Notes
page_order: 4
layout: dev_guide
guide_top_header: "Release Notes"
guide_top_text: "This is where you can find all updates to the Braze platform, with the following <a href='/docs/help/release_notes/#most-recent'>most recent platform updates</a>."
page_type: landing
search_rank: 1
description: "This landing page is home to Braze release notes. This is where you can find all updates to the Braze platform and SDKs, as well as a list of deprecated features."

guide_featured_title: "Release notes"
guide_featured_list:
  - name: 2025
    link: /docs/help/release_notes/2025/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: 2024
    link: /docs/help/release_notes/2024/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: 2023
    link: /docs/help/release_notes/2023/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: 2022
    link: /docs/help/release_notes/2022/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: 2021
    link: /docs/help/release_notes/2021/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: 2020
    link: /docs/help/release_notes/2020/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: 2019
    link: /docs/help/release_notes/2019/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: 2018
    link: /docs/help/release_notes/2018/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: 2017
    link: /docs/help/release_notes/2017/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: 2016
    link: /docs/help/release_notes/2016/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: Deprecations
    link: /docs/help/release_notes/deprecations/
    image: /assets/img/braze_icons/calendar-minus-01.svg
  - name: SDK Changelogs
    link: /docs/developer_guide/changelogs/
    image: /assets/img/braze_icons/file-code-01.svg

---

# Most recent Braze release notes {#most-recent}

> Braze releases information on product updates on a monthly cadence, aligning with major Product Releases, though the product is updated with miscellaneous improvements week to week.
> <br>
> <br>
> For more information on any of the updates listed in this section, reach out to your account manager or [open a support ticket]({{site.baseurl}}/help/support/). You can also check out [our SDK Changelogs]({{site.baseurl}}/developer_guide/changelogs) to see more information on our monthly SDK releases, updates, and improvements.

## Deferrals

Braze has updated our definition for what is a soft bounce and is sending a new event called [deferrals]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting/#email-performance) starting February 25, 2025 at 10 am EST.

For Sendgrid customers, we made a change to separate out deferral events from our soft bounce events. We count deferred events as a soft bounce event. This impacts any Sendgrid customer using Currents, Query Builder, SQL Extension, Snowflake Data Sharing, or our Transactional Email product.

### Prior behavior

Before February 25, 2025, a deferred event for an email address on a campaign or Canvas logs a soft bounce event every time. As a result, deferrals are included as part of soft bounce data. This can result in a user or a campaign reporting more soft bounce events than expected. 

### New behavior

Starting February 25, 2025, a deferred event will no longer log a soft bounce event every time. Instead, we'll log a soft bounce event once per send for the email address, no matter how many times the email is retried or deferred.

### What this means

You'll notice a sizable drop in the volume of soft bounce events starting on February 25, 2025, resulting in the following potential changes:

- Decrease in soft bounces for any reports built using Query Builder
- Smaller segment size using SQL Extensions if you’re targeting users that have soft bounced X times over Y period
- Drop in the number of soft bounce events delivered using Currents and any of our features using Snowflake
- Drop in the number of soft bounces for Transactional Email product

For Sparkpost customers, there is no impact on your soft bounce event data, instead you'll start receiving a new email event, deferral, in Currents and Snowflake.

 
## March 4, 2025 release

### Developer Guide detangle

Identical content that's shared across multiple SDKs are starting to be merged together using the docs site's new SDK tabbing feature. This month [SDK integration]({{site.baseurl}}/developer_guide/sdk_integration/), [SDK initialization]({{site.baseurl}}/developer_guide/sdk_initialization/), and [Content Cards]({{site.baseurl}}/developer_guide/content_cards/) were combined. Stay tuned for more updates in the coming months.

### Data flexibility
 
#### Braze IDs for user profiles

A user profile now includes a [Braze ID]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles#user-profiles). You can use this when searching for user profiles.

#### Deferrals

Braze has updated our definition for what is a soft bounce and is sending a new event called [deferrals]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting#email-performance), which is when an email was not immediately delivered, but Braze will retry the email for up to 72 hours after this temporary delivery failure to maximize the chances of successful delivery before attempts for that specific campaign are stopped.

#### Snowflake entity relationships
 
We've mapped the [raw table schemas](https://www.braze.com/docs/assets/download_file/data-sharing-raw-table-schemas.txt) for Snowflake and Braze entity relationships to a new [user-friendly docs page](https://www.braze.com/docs/partners/data_and_infrastructure_agility/data_warehouses/snowflake/entity_relationships). It includes a breakdown of the `USER_MESSAGES` tables belonging to each channel, as well as descriptions for each table's primary, foreign, and native keys.

#### Identity management for external IDs

Using an email address or a hashed email address as your Braze external ID can simplify identity management across your data sources; however, it's important to consider the [potential risks]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/#identified-user-profiles) to user privacy and data security.
 
### Unlocking creativity

#### Liquid tutorials

Added three [Liquid tutorials]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/operators/#tutorials) about how to use operators in the following scenarios.

<table border="1">
  <tr>
    <td>Choosing a message with an integer custom attribute.</td>
    <td><img src="{% image_buster /assets/img/release_notes/2025_05_04/integer.png %}" alt="The compose step in Braze showing a message with an integer custom attribute." /></td>
  </tr>
  <tr>
    <td>Choosing a message with a string custom attribute.</td>
    <td><img src="{% image_buster /assets/img/release_notes/2025_05_04/string.png %}" alt="The compose step in Braze showing a message with a string custom attribute." /></td>
  </tr>
  <tr>
    <td>Aborting a message based on location.</td>
    <td><img src="{% image_buster /assets/img/release_notes/2025_05_04/location.png %}" alt="The compose step in Braze showing a message being aborted based on location." /></td>
  </tr>
</table>
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Context steps for Canvas
 
{% multi_lang_include release_type.md release="Early access" %}
 
Use [Context steps]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context) to create or update a set of variables that represent the context of a user (or insights into that user’s behavior) as they move through a Canvas.

#### Personalized delay

{% multi_lang_include release_type.md release="Early access" %}

You can set up a [personalized delay]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/#personalized-delays) for your users by selecting the **Personalize delay** toggle in your Delay step. You can use this with a Context step to select a context variable to delay by.

When setting up a Delay step in your Canvas user journey, you can now create a delay up to 2 years.

#### Reverting automatic synchronization

When [composing an email message]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/creating_an_email_campaign/#step-3-compose-your-email), you can revert to automatic synchronization in the Plaintext tab by selecting the Regenerate from HTML icon, which only appears if the plaintext isn’t synchronizing.

![The revert button for automatic synchronization in Braze.]({% image_buster /assets/img/release_notes/2025_05_04/regenerate_from_html.png %})
 
### Robust channels

#### Android Live Updates

Although Live Updates won’t be officially available until 
[Android 16](https://android-developers.googleblog.com/2025/01/first-beta-android16.html), our [Live Updates for Android]({{site.baseurl}}/developer_guide/push_notifications/live_notifications/?sdktab=android&tab=local) page shows you how to emulate their behavior, so you can display interactive lock-screen notifications similar to [Live Activities for the Swift Braze SDK]({{site.baseurl}}/developer_guide/push_notifications/live_notifications/?sdktab=swift). Unlike official Live Updates, this functionality can be implemented for older Android versions.

#### Copying campaigns with feature flags across workspaces

You can now [copy campaigns with feature flags across workspaces]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/copying_to_workspace/#copying-campaigns-with-feature-flags). To do so, make sure the destination workspace has a feature flag experiment configured with an ID that matches the feature flag referenced in the original campaign.

#### New WhatsApp message types supported

WhatsApp messages now support [video, audio, and document outbound messages]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create#outbound-messages). Contact your Braze account manager if you're interested in participating in the early access.

#### Right-to-left messages

[Creating right-to-left messages]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/localizing_a_campaign/right_to_left_messages) covers best practices for crafting messages in languages that read right-to-left so that your messages display accurately as much as possible.
 
### AI and ML automation
 
#### Item recommendations

[Using item recommendations in messaging]({{site.baseurl}}/user_guide/brazeai/recommendations/using_recommendations) covers the `product_recommendation` Liquid object and includes a tutorial to help you put that knowledge into practice.

### New Braze partnerships
 
#### Email Love - Channel Extensions
 
The Braze and [Email Love]({{site.baseurl}}/partners/message_orchestration/channel_extensions/email_templates) partnership leverages Email Love’s Export to Braze feature and the Braze API to upload your email templates to Braze seamlessly.

#### VWO - A/B Testing
 
The Braze and [VWO]({{site.baseurl}}/partners/data_and_infrastructure_agility/ab_testing/vwo) integration allows you to leverage VWO experiment data to create targeted segments and deliver personalized campaigns.
 
### SDK updates
 
The following SDK updates have been released. Breaking updates are listed below; all other updates can be found by checking the corresponding SDK changelogs.
 
- [React Native](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md)
    - Bumps React Native minimum requirement version to [0.71.0](https://reactnative.dev/blog/2023/01/12/version-071). For more information, refer to [Releases Support Policy](https://github.com/reactwg/react-native-releases#releases-support-policy) in the React Working Group.
    - Bumps the minimum required iOS version to 12.0.
    - Updates the native iOS version bindings from [Braze Swift SDK 7.5.0 to 8.1.0](https://github.com/braze-inc/braze-swift-sdk/compare/7.5.0...8.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Updates the native Android version bindings from [Braze Android SDK 29.0.1 to 30.1.1](https://github.com/braze-inc/braze-android-sdk/compare/v29.0.1...v30.1.1#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).

## February 4, 2025 release

### Braze Docs improvements

#### Contributing Guide
Our recent updates to the [Contributing Guide]({{site.baseurl}}/contributing/your_first_contribution) makes it easier for non-technical users to contribute to Braze Docs.

#### Data and Analytics revamp
To make it easier for you to find what you're looking for, we separated the articles formerly nested under "Data & Analytics" into [Data]({{site.baseurl}}/user_guide/data) and [Analytics]({{site.baseurl}}/user_guide/analytics). 

#### Developer Guide
We've done a huge cleanup of all docs across the [Braze Developer Guide]({{site.baseurl}}/developer_guide/home), which included merging "how-to's" split across multiple pages into a single page.

There's also a new [SDK reference page]({{site.baseurl}}/developer_guide/references) that lists all of the reference documentation and repositories for each Braze SDK.

##### Unreal Engine Braze SDK
We migrated and rewrote all content from the Unreal Engine Braze SDK GitHub repository README into its [dedicated section on Braze Docs]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=unreal%20engine).

### Data flexibility

#### API usage dashboard

{% multi_lang_include release_type.md release="General availability" %}

The [API usage dashboard]({{site.baseurl}}/user_guide/analytics/dashboard/api_usage_dashboard) lets you monitor your incoming REST API traffic into Braze to understand your trends within your usage of our REST APIs and to troubleshoot any potential issues.

#### Adding tags to custom attributes

{% multi_lang_include release_type.md release="General availability" %}

You can [add tags to a custom attribute]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes#adding-tags) after it's created if you have the "Manage Events, Attributes, Purchases" permission. The tags can then be used to filter the list of attributes.

#### Catalog selections and async catalog fields endpoints 

{% multi_lang_include release_type.md release="General availability" %}

The following endpoints are now generally available:
* [POST: Create Catalog Fields]({{site.baseurl}}/api/endpoints/catalogs/catalog_fields/asynchronous/post_create_catalog_fields)
* [DELETE: Delete Catalog Field]({{site.baseurl}}/api/endpoints/catalogs/catalog_fields/asynchronous/delete_catalog_field)
* [DELETE: Delete Catalog Selection]({{site.baseurl}}/api/endpoints/catalogs/catalog_selections/asynchronous/delete_catalog_selection)
* [POST: Create Catalog Selection]({{site.baseurl}}/api/endpoints/catalogs/catalog_selections/asynchronous/post_create_catalog_selections)

#### Using an email address to trigger campaigns or Canvases

{% multi_lang_include release_type.md release="General availability" %}

You can now specify a recipient by email address to trigger your [campaigns]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/targeting_users) and [Canvases]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/?tab=target%20audience#step-2c-set-your-target-entry-audience).

#### Using a phone number to identify a user via the API

{% multi_lang_include release_type.md release="General availability" %}

You can now use a phone number, in addition to an alias and email address, to identify a user through the [`/users/identify` API endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_identify)

#### Getting a SAML trace
We added [steps on how to obtain a SAML trace]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up#obtaining-a-saml-trace), which helps you resolve issues about SAML SSO with Support more efficiently.
 
#### Region-specific data centers
As Braze is growing to serve new areas, we've added an [article about Braze data centers]({{site.baseurl}}/user_guide/data/data_centers) to clarify our operational approach.
 
### Unlocking creativity
 
#### Price drop notifications and back-in-stock notifications

{% multi_lang_include release_type.md release="General availability" %}

You can now notify customers when an item is back-in-stock by setting up [back-in-stock notifications]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog_triggers/back_in_stock_notifications) through a Canvas and catalog.

You can also create [price drop notifications]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog_triggers/price_drop_notifications) to notify customers when an item's price has decreased by setting up price drop notifications in a catalog and Canvas.

#### Preview for selection 

{% multi_lang_include release_type.md release="General availability" %}

After creating a selection, you can [view what a selection would return]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/selections/#test-and-preview) for either a random user or a specific user.

#### Templating catalog items including Liquid 

{% multi_lang_include release_type.md release="General availability" %}

You can [template catalog items that include Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/using_catalogs/#using-liquid).

#### Canvas templates
We added new Canvas templates for [onboarding users with a preferences survey]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/preference_survey) and [creating an email sign-up with double opt-in]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/email_signup).

#### Managing leads with Salesforce Sales Cloud for B2B
One way B2B marketers can use Braze is through an integration with the Salesforce Sales Cloud. Read more about how to implement this [use case]({{site.baseurl}}/user_guide/getting_started/b2b_use_cases/b2b_salesforce_sales_cloud).
 
### Robust channels

#### Suppression lists

{% multi_lang_include release_type.md release="Beta" %}
 
[Suppression lists]({{site.baseurl}}/user_guide/engagement_tools/segments/suppression_lists) specify groups of users who will never receive messages. Admins can create suppression lists with segment filters to narrow down a user group the same way you would for segmentation.

### New Braze partnerships

#### Constructor - Dynamic content
[Constructor]({{site.baseurl}}/partners/message_personalization/dynamic_content/constructor) is a search and product discovery platform that uses AI and machine learning to deliver personalized search, recommendations, and browsing experiences for ecommerce and retail websites.
 
#### Trustpilot - Dynamic content
[Trustpilot]({{site.baseurl}}/partners/message_personalization/dynamic_content/trustpilot) is an online review platform that enables your customers to share feedback and allows you to manage and respond to reviews.

### SDK updates
 
The following SDK updates have been released. Breaking updates are listed below; all other updates can be found by checking the corresponding SDK changelogs.
 
- [Braze Android SDK 34.0.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#3400)
    - Updated the minimum SDK version from 21 (Lollipop) to 25 (Nougat).

## January 7, 2025 release

### Unlocking creativity

#### In-app messages templates

We added [templates]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/) for drag-and-drop in-app messages.

#### B2B Salesforce Sales Cloud lead management

[Managing leads with Salesforce Sales Cloud]({{site.baseurl}}/user_guide/getting_started/b2b_use_cases/b2b_salesforce_sales_cloud/) demonstrates how to use Braze webhooks to create and update leads in Salesforce Sales Cloud through a community-submitted integration.

### Robust channels

#### Canvas templates

We added Braze Canvas templates for [email sign-up with double opt-in]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/email_signup/) and [onboarding with preferences survey]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/preference_survey/).

#### Changes to WhatsApp Opt-in policy

Meta recently updated their [opt-in policy](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/). For additional information, refer to [WhatsApp product updates]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/meta_resources/).

#### Width tool for Content Blocks in the email drag-and-drop editor

You can [adjust the width]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_content_blocks/#using-the-editor-to-add-a-content-block) of your Content Block in the drag-and-drop email editor. The default width is 100%.

### Data flexibility

#### Soft Bounced segment filter

Segment your users by whether they soft bounced X times in Y days. For more information, refer to [Segmentation filters glossary]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#soft-bounced).

#### Anonymous users overview

[Anonymous users]({{site.baseurl}}/user_guide/data/user_data_collection/anonymous_users/) provides an overview of anonymous users and user aliases, outlining their significance and how they can be leveraged in your messages.

#### Global Control Group membership

You can [view Global Control Group membership]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/#view-whether-a-user-is-in-a-global-control-group) by going to the **Engagement** tab of an individual user's profile and scrolling to the **Miscellaneous** section.

### New Braze partnerships

#### Justuno - Leads capture

[Justuno]({{site.baseurl}}/partners/data_and_infrastructure_agility/leads_capture/justuno/) lets you create fully optimized visitor experiences for all of your audiences with dynamic segments, offering the most advanced targeting available&#8212;all without impacting site speed or increasing dev work.

#### Odicci - Customer data platform

Integrate Braze with [Odicci]({{site.baseurl}}/partners/message_personalization/dynamic_content/odicci/), a platform that empowers businesses to acquire, engage and retain customers through loyalty driven omnichannel experiences.

#### Optimizely - A/B testing

The Braze and [Optimizely]({{site.baseurl}}/partners/data_and_infrastructure_agility/ab_testing/optimizely/) integration is a two-way integration that allows you to:

- Sync your Braze customer segments and events to Optimizely Data Platform (ODP) nightly to enrich Optimizely customer profiles, reports, and segmentation.
- Send Braze Currents events from Braze to Optimizely’s reporting tool.
- Sync ODP customer data and events to Braze to enrich your Braze customer data and trigger Braze messaging based on customer events in ODP.

## December 10, 2024 release

### SDK user location by IP address

As of November 26, 2024, Braze will detect user locations from the geolocated country using the IP address from the start of the first SDK session. Braze will use the IP address to set the country value on user profiles that are created via the SDK, and that IP based country setting will be available during and after the first session. Refer to [Location tracking]({{site.baseurl}}/user_guide/engagement_tools/locations_and_geofences/location_tracking/) for more details.

### Elevated Access setting

[Elevated Access]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings/#elevated-access) adds an extra layer of security for sensitive actions in your Braze dashboard. When active, users need to re-verify their account before exporting a segment or viewing an API key. To use Elevated Access, go to **Settings** > **Admin Settings** > **Security Settings** and toggle it on.

### Permission for viewing personally identifiable information (PII)

For admins, you can [allow users to view PII]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#list-of-permissions) as defined by your company in the dashboard in message previews that use Liquid variables to access user properties. 

For workspaces, you can allow users to view PII as defined by your company in the dashboard, or view user profiles but redact fields your company has identified as PII.

### Data flexibility

#### Data lake schemas

The following schemas have been added to the raw table schemas:
- `USERS_CANVASSTEP_PROGRESSION_SHARED`: Progression events for a user in a Canvas
- `CHANGELOGS_GLOBALCONTROLGROUP_SHARED`: Identify which random bucket numbers are in the current and previous Global Control Group
- `USERS_MESSAGES_FEATUREFLAG_IMPRESSION_SHARED`: Impression events for when a user views an feature flag

#### Account-based segmentation

You can do [business-to-business (B2B) account-based segmentation]({{site.baseurl}}/user_guide/getting_started/b2b_use_cases/account_based_segmentation/) in two ways, depending on how you set up your B2B data model:

- When using catalogs for your business objects
- When using connected sources for your business objects

#### Segmentation filters

Refer to [Segmentation filters]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters) for the full list of segmentation filters and their descriptions.

##### User profile created at

Segment your users by when their user profile was created. If a user was added by CSV or API, then this filter reflects the date they were added. If the user isn't added by CSV or API and has their first session tracked by the SDK, then this filter reflects the date of that first session.

##### Sending phone number

Segment your users by the e.164 phone number field. You can use regular expressions with this filter to segment by phone numbers with a specific country code.

### New Braze partnerships

#### Narvar - eCommerce

The Braze and [Narvar](https://corp.narvar.com/) integration enables brands to leverage Narvar’s notification events to trigger messages directly from Braze, keeping customers informed with timely updates.

#### Zeotap for Currents - Customer data platform

The Braze and [Zeotap](https://zeotap.com/) integration empowers you to extend the scale and reach of your campaigns by syncing Zeotap customer segments to Braze user profiles. With [Currents]({{site.baseurl}}/user_guide/data/braze_currents/), you can also connect data to Zeotap to make it actionable across the entire growth stack.

#### Notify - Dynamic content

The Braze and [Notify](https://notifyai.io/) integration empowers marketers to effectively drive engagement across various platforms. Instead of relying on traditional marketing methods, a Braze API-triggered campaign can leverage Notify's capabilities to deliver personalized messaging through multiple channels, including email, SMS, push notifications, and more.

#### Contentful - Dynamic content

The Braze and [Contentful](https://www.contentful.com/) integration allows you to dynamically use Connected Content to pull content from Contentful into your Braze campaigns.

#### Outgrow - Leads capture 

The Braze and [Outgrow](https://outgrow.co/) integration lets you automatically transfer user data from Outgrow into Braze, enabling highly personalized and targeted campaigns.

### SDK updates

The following SDK updates have been released. Breaking updates are listed below; all other updates can be found by checking the corresponding SDK changelogs.

- [Web SDK 5.6.1](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
- [Flutter SDK 12.0.0](https://github.com/braze-inc/braze-flutter-sdk/releases/tag/12.0.0)
    - Updates the native iOS bridge [from Braze Swift SDK 10.3.1 to 11.3.0](https://github.com/braze-inc/braze-swift-sdk/compare/10.3.1...11.3.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)
    - Updates the native Android bridge [from Braze Android SDK 32.1.0 to 33.1.0](https://github.com/braze-inc/braze-android-sdk/compare/v32.1.0...v33.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)
- [Swift SDK 11.0.1](https://github.com/braze-inc/braze-swift-sdk/blob/11.0.1/CHANGELOG.md)

## November 12, 2024 release
 
### Data flexibility
 
#### Speed limit for `/users/track`

The speed limit for the [`/users/track` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) has been updated to 3,000 per 3 seconds.
 
### Unlocking creativity

#### Canvas Use Cases

We've put together some use cases showcasing the different ways you can leverage a Braze Canvas. If you're looking for inspiration, choose a use case below to get started.

- [Abandoned Cart]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/abandoned_cart/)
- [Back In Stock]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/back_in_stock/)
- [Feature Adoption]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/feature_adoption/)
- [Lapsed User]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/lapsed_user/)
- [Onboarding]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/onboarding/)
- [Post-Purchase Feedback]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/post_purchase_feedback/)

### Robust channels

#### LINE

{% multi_lang_include release_type.md release="General availability" %}

Braze's LINE integration is now generally available! LINE  is the most popular messaging app in Japan, with over 95 million monthly active users. In addition to messaging, LINE offers its users an “all-in-one” platform for social media, gaming, shopping, and payments.

To get started, see our [LINE documentation]({{site.baseurl}}/user_guide/message_building_by_channel/line/).
 
#### LinkedIn Audience Sync

{% multi_lang_include release_type.md release="Beta" %}

You can now use LinkedIn with [Braze Audience Sync]({{site.baseurl}}/partners/canvas_steps/), a tool that helps you extend the reach of your campaigns to many of the top social and advertising technologies. To join the beta, reach out to your Braze Success Manager.
 
### Improving the developer guide
 
We're in the process of making major improvements to the [Braze Developer Guide]({{site.baseurl}}/developer_guide/home/). As a first step, we simplified the navigation and reduced the number of nested sections. 

|Before|After|
|------|-----|
|!["The old navigation for the Braze Developer Guide."]({% image_buster /assets/img/release_notes/developer_guide_improvements/old_navigation.png %})|!["The new navigation for the Braze Developer Guide."]({% image_buster /assets/img/release_notes/developer_guide_improvements/new_navigation.png %})|

### New Braze partnerships
 
#### MyPostcard

[MyPostcard](https://www.mypostcard.com/), a leading global postcard app, empowers you to execute direct mail campaigns with ease, providing a seamless and profitable way to connect with your customers. To get started, see [Integrating MyPostcard with Braze]({{site.baseurl}}/partners/message_orchestration/additional_channels/direct_mail/mypostcard/).
 
### SDK updates
 
The following SDK updates have been released. Breaking updates are listed below; all other updates can be found by checking the corresponding SDK changelogs.
 
- [Expo Plugin 3.0.0](https://github.com/braze-inc/braze-expo-plugin/blob/main/CHANGELOG.md)
    - This version requires 13.1.0 of the Braze React Native SDK.
    - Replaces the iOS BrazeAppDelegate method call of BrazeReactUtils.populateInitialUrl with BrazeReactUtils.populateInitialPayload.
        - This update resolves an issue where push opened events would not be triggered when clicking on a notification while the application is in a terminated state.
        - To fully leverage this update, replace all calls of Braze.getInitialURL with Braze.getInitialPushPayload in your JavaScript code. The initial URL can now be accessed via the url property of the initial push payload.
- [Braze Segment Swift Plugin 5.0.0](https://github.com/braze-inc/braze-segment-swift/blob/main/CHANGELOG.md)
    - Updates the Braze Swift SDK bindings to require releases from the 11.1.1+ SemVer denomination.
    - This allows compatibility with any version of the Braze SDK from 11.1.1 up to, but not including, 12.0.0.
    - Refer to the changelog entry for 11.1.1 for more information on potential breaking changes.

## October 15, 2024 release

### Data flexibility

#### Campaigns and Canvases

While creating campaigns and Canvases, you can calculate the exact number of reachable users in your target audience instead of the default estimation by selecting [Calculate exact statistics]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#statistics-for-segment-size).

#### API Android objects

The [`android_priority` parameter]({{site.baseurl}}/api/objects_filters/messaging/android_object/#additional-parameter-details) will accept values either “normal” or “high” to specify the FCM sender priority. By default, notification messages are sent with high priority, and data messages are sent with normal priority.

For more information on how different values impact delivery, see [Android message priority](https://firebase.google.com/docs/cloud-messaging/android/message-priority/).

#### SDK

Use the [Braze SDK's built-in debugger]({{site.baseurl}}/developer_guide/debugging/) to troubleshoot issues for your SDK-powered channels without needing to enable verbose logging in your app.

#### Live Activities

We updated the [frequently asked questions]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/live_activities/faq/) for Swift Live Activities with a few new questions and answers.

#### Custom events

[Event property objects]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-properties) that contain array or object values can now have an event property payload of up to 100&nbsp;KB.

#### Random bucket numbers

Use [random audience re-entry with random bucket numbers]({{site.baseurl}}/user_guide/engagement_tools/testing/random_bucket_numbers/#random-audience-re-entry-using-random-bucket-numbers) for A/B testing or targeting specific user groups in your campaigns.

#### Segment Extensions

You can [refresh segment extensions on a recurring schedule]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/#setting-up-a-recurring-refresh) by selecting the frequency at which the extensions will refresh (daily, weekly, or monthly) and the specific time the refresh will occur.

### Robust channels

#### SMS

We added [Adding UTM parameters]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/link_shortening/#using-link-shortening) to demonstrate how you can use UTM parameters in an SMS message, so you track the performance of campaigns in third-party analytics tools, such as Google Analytics.

#### Landing pages

[Connect your own domain]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/customizing_urls/) to your Braze workspace to customize your landing page URLs with your brand.

#### LINE and Braze

{% multi_lang_include release_type.md release="Beta" %}

We added new documentation:

- [LINE message types]({{site.baseurl}}/line/create/message_types/) covers the LINE message types you can compose, including aspects and limitations, and is part of the LINE beta collection.
- [User account linking]({{site.baseurl}}/line/line_setup/#user-account-linking) allows users to link their LINE account to your app’s user account. You can then use Liquid in Braze, such as {% raw %}`{{line_id}}`{% endraw %}, to create a personalized URL for the user that passes the user's LINE ID back to your website or app, which can then be associated with a known user.

#### WhatsApp and Braze

[WhatsApp Business Accounts (WABA)]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/#step-2-whatsapp-setup) can now be shared with multiple Business Solution Providers.

### New Braze partnerships

#### Future Anthem - Dynamic Content

The Braze and [Future Anthem]({{site.baseurl}}/partners/message_personalization/dynamic_content/future_anthem/) partnership leverages Amplifier AI to deliver content personalization, real-time experiences, and dynamic audiences. Amplifier AI works across sports, casinos, and lottery, allowing you to enhance Braze player profiles with industry-specific player attributes, such as a favorite game, engagement score, expected next bet, and more.

### Settings

#### Indentifier field-level encryption

{% multi_lang_include release_type.md release="General availability" %}

Using [identifier field-level encryption]({{site.baseurl}}/user_guide/analytics/field_level_encryption/), you can seamlessly encrypt email addresses with AWS Key Management Service (KMS) to minimize personally identifiable information (PII) shared in Braze. Encryption replaces sensitive data with ciphertext, which is unreadable encrypted information.

### SDK updates

The following SDK updates have been released. Breaking updates are listed below; all other updates can be found by checking the corresponding SDK changelogs.

- [Swift SDK 10.3.1](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1110)
- [Swift SDK 11.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1110)
    - Adds support for [Swift 6 strict concurrency checking](https://developer.apple.com/documentation/swift/adoptingswift6)
        - Relevant public Braze classes and data types now conform to the `Sendable` protocol and can be safely used across concurrency contexts.
        - Main thread-only APIs are now marked with the `@MainActor` attribute.
        - We recommend using Xcode 16.0 or later to take advantage of these features while minimizing the number of warnings generated by the compiler. Previous versions of Xcode may still be used, but some features may generate warnings.
    - When integrating push notification support manually, you may need to update the `UNUserNotificationCenterDelegate` conformance to use the `@preconcurrency` attribute to prevent warnings.
        - Applying the `@preconcurrency` attribute on protocol conformance is only available in Xcode 16.0 or later. Reference our sample integration code [here](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples/Swift/Sources/PushNotifications-Manual).
- [React Native SDK 13.0.0](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md#1300)
    - Updates the native Android version bindings from [Braze Android SDK 31.1.0 to 32.1.0](https://github.com/braze-inc/braze-android-sdk/compare/v31.1.0...v32.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Updates the native iOS version bindings from [Braze Swift SDK 10.3.0 to 11.0.0](https://github.com/braze-inc/braze-swift-sdk/compare/10.3.0...11.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
- [Flutter SDK 11.1.0](https://pub.dev/packages/braze_plugin/changelog#1110)
- [Swift SDK 11.1.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1110)
- [Android SDK 33.0.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#3300)
    - Updated Kotlin from 1.8 to Kotlin 2.0.
- [Web SDK 5.5.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md#550)

## September 17, 2024 release

### Data flexibility

#### Braze Cloud Data Ingestion for S3

You can use [Cloud Data Ingestion (CDI) for S3]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/file_storage_integrations/#aws-definitions) to directly integrate one or more S3 buckets in your AWS account with Braze. When new files are published to S3, a message is posted to SQS, and Braze Cloud Data Ingestion takes in those new files.

#### Monthly active users CY 24-25

For customers who have purchased Monthly Active Users - CY 24-25, Braze manages different rate limits on its `/users/track` endpoint. For details, refer to [POST: Track Users]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#monthly-active-users-cy-24-25). 

### Unlocking creativity

#### Templating catalog items including Liquid

{% multi_lang_include release_type.md release="Early access" %}

Use the `:rerender` flag in a Liquid tag to [render a catalog item's Liquid content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog/#using-liquid). For example, if you render the following Liquid content:

{% raw %}
```liquid
Hi ${first_name}
{% catalog_items Messages greet_msg :rerender %}
{{ items[0].Welcome_Message }}
```
{% endraw %}

This will display as the following:

{% raw %}
```
Hi Peter,
Welcome to our store, Peter!
```
{% endraw %}

### Robust channels

#### WhatsApp response messages

{% multi_lang_include release_type.md release="General availability" %}

You can use [response messages]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create#response-messages) to reply to inbound WhatsApp messages from your users. These messages are built in-app on Braze during your composition experience and can be edited at any time. You can use Liquid to match the response message language to the appropriate users.

#### Canvas templates

{% multi_lang_include release_type.md release="General availability" %}

Create [Canvas templates]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_templates/) to refine your messaging by creating a consistent framework that can be easily customized to fit your specific goals across your Canvases.

#### Landing pages

{% multi_lang_include release_type.md release="Beta" %}

Braze [landing pages]({{site.baseurl}}/user_guide/engagement_tools/landing_pages) are standalone webpages that can drive your user acquisition and engagement strategy.

#### Changes since last viewed

You can view the number of updates to your [Canvases]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/#changes-since-last-viewed), campaigns, and [segments]({{site.baseurl}}/user_guide/engagement_tools/segments/managing_segments/#changes-since-last-viewed) by other members of your team by referring to the *Changes Since Last Viewed* metric on the respective overview pages (such as the overview page for an [email campaign]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting#changes-since-last-viewed)). 

#### Troubleshooting webhook and Connected Content requests 

[This article]({{site.baseurl}}/help/help_articles/api/webhook_connected_content_errors) covers how to troubleshoot webhook and Connected Content error codes, including what the errors are and steps to resolve them.

### New Braze partnerships

#### Inbox Monster - Analytics

[Inbox Monster]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/inbox_monster/) is an inbox signals platform that helps enterprise brands land every send. It's an integrated suite of solutions for deliverability, creative rendering, and SMS monitoring, that empowers modern customer relationship managment (CRM) teams and ends the sending scaries.

#### SessionM - Loyalty

[SessionM]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/sessionm/) is a customer engagement and loyalty platform that provides campaign management features and loyalty management solutions to help marketers drive targeted outreach to increase engagement and profitability.

### AI and ML automation

#### Trending item recommendations

In addition to the "AI Personalized" model, the [AI item recommendations]({{site.baseurl}}/user_guide/sage_ai/recommendations/about_item_recommendations/#trending) feature also includes a recommendation model for "Trending", which features items that had the most positive momentum when it comes to recent user interactions.

### Settings

#### Roles

{% multi_lang_include release_type.md release="General availability" %}

[Roles]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#creating-a-role) allow for more structure by bundling together your individual custom permissions with workspace access controls. This is especially useful if you have many brands or regional workspaces in one dashboard. With roles, you can add dashboard users to the right workspaces and directly grant them the associated permissions. 

#### Security event report

We added a complete list of the [security events]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings/#downloading-a-security-event-report) that may appear in your downloaded security report event.

#### Message usage report

{% multi_lang_include release_type.md release="Early access" %}

The [message usage dashboard]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_campaign_analytics/message_usage/) provides self-service insights into your SMS and WhatsApp credit usage for a comprehensive view of historical and current usage compared against contract allotments. These insights can reduce your confusion and help you make adjustments to prevent overage risks.

### SDK

#### Delayed initialization for the Braze Swift SDK

Set up [delayed initialization]({{site.baseurl}}/developer_guide/sdk_initalization/?sdktab=swift) to initialize your Braze Swift SDK asynchronously while ensuring push notification handling is preserved. This can be useful when you need to set up other services before initializing the SDK, such as fetching configuration data from a server, or waiting for user consent.

### SDK updates

The following SDK updates have been released. Breaking updates are listed below; all other updates can be found by checking the corresponding SDK changelogs.

- [Android SDK 32.1.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#3210)
- [Segment Kotlin SDK 2.0.0](https://github.com/braze-inc/braze-segment-kotlin/blob/main/CHANGELOG.md#200)
- [Swift SDK 10.1.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1010)
- [React Native SDK 12.1.0](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md#1210)
- [Cordova SDK 10.0.0](https://github.com/braze-inc/braze-cordova-sdk/blob/master/CHANGELOG.md#1000)
    - This version now requires Cordova Android 13.0.0.
    - Refer to the [Cordova release announcement](https://cordova.apache.org/announcements/2024/05/23/cordova-android-13.0.0.html) for a full list of project dependency requirements.- Updated the native Android bridge [from Braze Android SDK 30.3.0 to 32.1.0](https://github.com/braze-inc/braze-android-sdk/compare/v30.3.0...v32.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Updated the native iOS bridge [from Braze Swift SDK 9.2.0 to 10.1.0](https://github.com/braze-inc/braze-swift-sdk/compare/9.2.0...10.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
- [Swift SDK 10.2.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1020)
- [Unity 7.0.0](https://github.com/braze-inc/braze-unity-sdk/blob/master/CHANGELOG.md#700)
    - Updated the native Android bridge [from Braze Android SDK 30.3.0 to 32.1.0](https://github.com/braze-inc/braze-android-sdk/compare/v30.3.0...v32.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Updated the native iOS bridge [from Braze Swift SDK 9.0.0 to 10.1.0](https://github.com/braze-inc/braze-swift-sdk/compare/9.0.0...10.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
- [Braze Segment Swift Plugin 4.0.0](https://github.com/braze-inc/braze-segment-swift/blob/main/CHANGELOG.md#400)
    - Updates the Braze Swift SDK bindings to require releases from the `10.2.0+` SemVer denomination.
        - This allows compatibility with any version of the Braze SDK from `10.2.0` up to, but not including, `11.0.0`.
        - Refer to the changelog entry for [`10.0.0`](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1000) for more information on potential breaking changes.
- [Flutter SDK 11.0.0](https://pub.dev/packages/braze_plugin/changelog#1100)
    - Updates the native Android bridge [from Braze Android SDK 30.4.0 to 32.1.0](https://github.com/braze-inc/braze-android-sdk/compare/v30.4.0...v32.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
        - Changes the behavior of `wipeData()` on Android to retain external subscriptions (like `subscribeToContentCards()`) after being called.
    - Updates the native iOS bridge [from Braze Swift SDK 9.0.0 to 10.2.0](https://github.com/braze-inc/braze-swift-sdk/compare/9.0.0...10.2.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
- [Swift SDK 10.3.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1030)
- [Unity 7.1.0](https://github.com/braze-inc/braze-unity-sdk/blob/master/CHANGELOG.md#710)
- [React Native SDK 12.2.0](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md#1220)

## August 20, 2024 release

### New use cases

#### Catalogs

You can bring in any type of data into a catalog. Typically, the data is metadata about offerings, such as products, discounts, promotions, events, and similar. Read our [use cases]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs) and learn how you can use this data to target users with highly relevant messaging.

#### Intelligence Suite

The Intelligence Suite provides powerful features to analyze user history and campaign and Canvas performance, then make automatic adjustments to increase engagement, viewership, and conversions. For a few examples of how these features can benefit different industries, check out our [use cases]({{site.baseurl}}/user_guide/brazeai/intelligence).

### Home dashboard update

You can [pick up where you left off]({{site.baseurl}}/user_guide/data_and_analytics/analytics/home_dashboard/#pick-up-where-you-left-off) in the Braze dashboard with easy access to files you've recently edited or created. This section appears at the top of the **Home** page of the Braze dashboard.

### Data flexibility

#### Data Transformation templates and new destination

{% multi_lang_include release_type.md release="General availability" %}

Build your Data Transformation using our dedicated [template library]({{site.baseurl}}/user_guide/data_and_analytics/data_transformation/creating_a_transformation#step-2-create-a-transformation) to help you get started with certain external platforms, instead of default code. You can now select **POST: Send messages immediately via API Only** as your destination to transform webhooks from a source platform to send immediate messages to your users.

#### Merge users in bulk

{% multi_lang_include release_type.md release="General availability" %}

If you encounter duplicate user profiles, you can [bulk merge]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users#bulk-merging) these users to help streamline your data.

#### Export custom attributes

{% multi_lang_include release_type.md release="General availability" %}

You can [export the list of custom attributes]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#exporting-data) as a CSV file by selecting **Export all** on the **Custom Attributes** page. The CSV file will be generated, and a download link will be emailed to you.

#### Currents IP allowlisting

Braze will send Currents data from the listed IPs, which are automatically and dynamically added to any API keys that have been opted-in for [allowlisting]({{site.baseurl}}/user_guide/data/braze_currents/setting_up_currents/).

### Robust channels

#### New segment builder experience

{% multi_lang_include release_type.md release="General availability" %}

Build a segment using our [updated experience]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment). Segments update in real-time as data changes, and you can create as many segments as needed for your targeting and messaging purposes.

#### Metrics by segments

Use [Query Builder]({{site.baseurl}}/user_guide/analytics/query_builder/) report templates to break down performance metrics for campaigns, Canvas, variants, and steps by segments.

#### Phone number acquisition

To use the WhatsApp messaging channel, you'll need a phone number that meets WhatsApp’s requirements for its [Cloud API](https://developers.facebook.com/docs/whatsapp/cloud-api/phone-numbers) or [On-Premises API](https://developers.facebook.com/docs/whatsapp/on-premises/phone-numbers). 

You must acquire your phone number yourself, as Braze won't provision the number for you. You can either purchase a physical phone with a SIM card through your business phone provider or use one of our partners: Twilio or Infoblip. **You must have your own Twilio or Infobip account because this cannot be done through Braze.**

### New Braze partnerships

#### Zendesk Chat - Instant Chat

The Braze and [Zendesk Chat]({{site.baseurl}}/partners/zendesk_chat/) integration uses webhooks from each platform to set up a two-way SMS conversation. When a user requests support, a ticket is created in Zendesk. Agent responses are forwarded to Braze through an API-triggered SMS campaign, and user replies are sent back to Zendesk.

### SDK updates

The following SDK updates have been released. Breaking updates are listed below; all other updates can be found by checking the corresponding SDK changelogs.

- [Android SDK 32.0.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md)
- [Swift SDK 10.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
    - The following changes have been made when subscribing to Push events with [`Braze.Notifications.subscribeToUpdates(payloadTypes:_:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/notifications-swift.class/subscribetoupdates(payloadtypes:_:)):
        - The `update` closure will now be triggered by both "Push Opened" and "Push Received" events by default. Previously, it would only be triggered by "Push Opened" events.
            - To continue subscribing only to "Push Opened" events, pass in `[.opened]` for the parameter `payloadTypes`. Alternatively, implement your `update` closure to check that the `type` from the `Braze.Notifications.Payload` is `.opened`.
        - When receiving a push notification with `content-available: true`, the [`Braze.Notifications.Payload.type`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/notifications-swift.class/payload/type) will now be `.received` instead of `.opened`.
    - Marks the following deprecated APIs as unavailable:
        - `Braze.Configuration.Api.Flavor`
        - `Braze.Configuration.Api.flavor`
        - `Braze.Configuration.Api.SdkMetadata`
        - `Braze.Configuration.Api.addSdkMetadata(_:)`
        - `Braze.ContentCard.ClickAction.uri(_:useWebview:)`
        - `Braze.ContentCard.ClickAction.uri`
        - `Braze.InAppMessage.ClickAction.uri(_:useWebview:)`
        - `Braze.InAppMessage.ClickAction.uri`
        - `Braze.InAppMessage.ModalImage.imageUri`
        - `Braze.InAppMessage.Full.imageUri`
        - `Braze.InAppMessage.FullImage.imageUri`
        - `Braze.InAppMessage.Themes.default`
        - `Braze.deviceId(queue:completion:)`
        - `Braze._objc_deviceId(completion:)`
        - `Braze.deviceId()`
        - `Braze.User.setCustomAttributeArray(key:array:fileID:line:)`
        - `Braze.User.addToCustomAttributeArray(key:value:fileID:line:)`
        - `Braze.User.removeFromCustomAttributeArray(key:value:fileID:line:)`
        - `Braze.User._objc_addToCustomAttributeArray(key:value:)`
        - `Braze.User._objc_removeFromCustomAttributeArray(key:value:)`
        - `gifViewProvider`
        - `GifViewProvider.default`
    - Removes the deprecated APIs:
        - `Braze.Configuration.DeviceProperty.pushDisplayOptions`
        - `Braze.InAppMessageRaw.Context.Error.extraProcessClickAction`
    - Removes the deprecated `BrazeLocation` class in favor of `BrazeLocationProvider`.
- [Xamarin SDK Version 6.0.0](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/CHANGELOG.md)
    - Added support for .NET 8.0 for the iOS and Android bindings as .NET 7.0 has reached end of life support.
        - This removes support for .NET 7.0.
    - Updated the Android binding from [Braze Android 30.4.0 to 32.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v30.4.0...v32.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Updated the iOS binding from [Braze Swift SDK 9.0.0 to 10.0.0](https://github.com/braze-inc/braze-swift-sdk/compare/9.0.0...10.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
        - When subscribing to push notification events, the subscription will be triggered on iOS for both "Push Received" and "Push Opened", instead of only for "Push Opened" events.
- [React Native SDK 12.0.0](https://github.com/braze-inc/braze-react-native-sdk/blob/12.0.0/CHANGELOG.md)
    - Updates the native iOS version bindings from [Braze Swift SDK 9.0.0 to 10.0.0](https://github.com/braze-inc/braze-swift-sdk/compare/9.0.0...10.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
        - When subscribing to push notification events, the subscription will be triggered on iOS for both `push_received` and `push_opened`, instead of only for `push_opened` events.
