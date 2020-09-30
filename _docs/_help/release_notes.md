---
page_order: 2
nav_title: Release Notes
layout: featured
guide_top_header: "Release Notes"
guide_top_text: "This is where you can find all updates to the Braze platform, with the <a href='/docs/help/release_notes/#most-recent'>most recent platform updates</a>, listed below. You can also
check out our <a href='/docs/developer_guide/platform_integration_guides/sdk_changelogs/'>SDK Changelogs</a>."

guide_featured_title: "Release Notes"
guide_featured_list:
  - name: 2020
    link: /docs/help/release_notes/2020/
    fa_icon: fas fa-calendar-alt
  - name: 2019
    link: /docs/help/release_notes/2019/
    fa_icon: fas fa-calendar-alt
  - name: 2018
    link: /docs/help/release_notes/2018/
    fa_icon: fas fa-calendar-alt
  - name: 2017
    link: /docs/help/release_notes/2017/
    fa_icon: fas fa-calendar-alt
  - name: 2016
    link: /docs/help/release_notes/2016/
    fa_icon: fas fa-calendar-alt
  - name: Deprecations
    link: /docs/help/release_notes/deprecations/
    fa_icon: far fa-calendar-times
  - name: SDK Changelogs
    link: /docs/developer_guide/platform_integration_guides/sdk_changelogs/
    fa_icon: fas fa-file-code


---

# Most Recent Braze Release Notes {#most-recent}

> Braze releases information on product updates on a monthly cadence, aligning with major Product Releases, though the product is updated with miscellaneous improvements week to week.
> <br>
> <br>
> For more information on any of the updates listed in this section, reach out to your account manager or to [open a support ticket][support]. You can also check out [our SDK Changelogs]({{site.baseurl}}/developer_guide/platform_integration_guides/sdk_changelogs/) to see more information on our monthly SDK releases, updates, and improvements.

## October

### Report Builder
![Campaign Comparison Example][5]{: style="max-width:80%;"}

The Report Builder allows you to compare the results of multiple campaigns in a single view so that you can easily determine which engagement strategies most impacted your key metrics. Read more [here]({{site.baseurl}}/report_builder)!

### iOS 14 Upgrade Guide
The iOS 14 upgrade guide describes Braze-related changes introduced in iOS 14 and the required upgrade steps for your Braze iOS SDK integration. Some changes to note are future IDFA permission requirements, geofence support, and necessary Xcode upgrades. Check out our [upgrade guide]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/ios_14/) to read more. 

### Android 11 Upgrade Guide
The Android 11 guide describes relevant changes introduced in the Android 11 release and the required upgrade steps for your Braze Android SDK integration. Some changes to not relate to deep links, HTML In-App Messages, and location permissions. Check out our [upgrade guide]({{site.baseurl}}/developer_guide/platform_integration_guides/android/android_11/) to read more.

### Attribution Partners - Click Tracking Guide
Optional attribution partner click tracking documentation has now been added to each attribution partner page, this includes best practices and implementation guidelines to get click tracking working for your campaigns. Visit your [attribution partner]({{site.baseurl}}/partners/advertising_technologies/attribution/) page to read more. 

### New Description Field
Users can now add descriptions to campaigns and Canvases! This new field can be found right under the campaign or Canvas name field when creating or editing an existing campaign or Canvas. 

### Canvas Exception Events
New documention has beed added describing the expected behavior of exception events in Canvases. Visit our [documentation]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/exception_events/) to read more!

## September

### Funnel Reporting
Funnel Reporting offers a visual report that allows you to analyze the journeys your customers take after receiving a [campaign]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/campaign_funnel_report/) or [Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_funnel_reports).

### iOS 14 Upgrade Guide 
In accordance with the changes announced in Apple’s new iOS 14, there are some Braze-related changes and action items required for Braze iOS SDK integrations. For more information, take a look at [this upgrade guide]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/ios_14/).

### Changes to IDFA and IDFV for iOS 14
In iOS 14, users must decide if they want to opt-in to ad tracking and let apps and ad networks read their IDFA when visiting an app. As a result, Braze’s strategy is to instead use the “identifier for vendors” (i.e. IDFA) so you can continue to track users across different devices. For more information, take a look at [this section in the iOS 14 upgrade guide]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/ios_14/#idfa).

### Email Validation
This new email syntax validation process is an upgrade to Braze’s existing one. This is a check to verify that emails updated or imported into Braze are correct. For more information, take a look at [these guidelines and notes]({{site.baseurl}}/user_guide/onboarding_with_braze/email_setup/email_validation).

### Random Bucket User Event in Currents
The random bucket number (i.e. RBN) occurs every time a new user is created within their app group. During this event, each new user gets assigned a random bucket number that you can then use to create uniformly distributed segments of random users. Use this to group a range of random bucket number values and compare performance across your campaigns and campaign variants. To see if this event is available to you, take a look at the [customer behavior events glossary]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/customer_behavior_events/).

### Canvas Components - Coming Soon!
Braze has added four new Canvas components to help make increase the flexibility and functionality of your Canvases. These new components include: [Decision Split Step]({{site.baseurl}}/decision_split/), [Delay Step]({{site.baseurl}}/delay_step/), [Messaging Steps]({{site.baseurl}}/message_step/), and [Audience Sync to Facebook]({{site.baseurl}}/audience_sync_facebook/).
- __Canvas Decision Split, Delay, and Messaging Steps__<br>Decision splits can be used to create Canvas branches depending on whether a user matches a defined query. Delay steps allow you to add a stand-alone delay to your Canvas without the need for a corresponding message. Messaging steps allow you to add a standalone message where you want in your Canvas flow.
- __Audience Sync to Facebook__<br>Using the Braze Audience Sync to Facebook, brands can elect to add their own users’ data from their own Braze integration to Facebook Custom Audiences to deliver advertisements based upon behavioral triggers, segmentation, and more. Any criteria you’d normally use to trigger a message (Push, Email, SMS, Webhook, etc) in a Braze Canvas based upon your user data can now be used to trigger an ad to that user in Facebook via Custom Audiences.

### SMS Inbound Received Events
A new messaging engagement event has been added to Currents. This event occurs when one of your users sends an SMS to a phone number in one of your Braze SMS subscription groups. For more information, check out our [messaging and engagement events glossary]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events/).

## August

### External ID Migration Endpoints
Braze has released two new External ID Migration endpoints. These endpoints allow customers to rename or remove their users' Braze external IDs by utilizing the Braze API. These endpoints can be leveraged to migrate users with different naming schemas while still retaining historical data on those users. Check out our docs to learn more about the [`users.external_ids.rename`]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_rename/) and [`users.external_ids.remove`]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_remove/) endpoints.

### Predictive Churn
Braze's Predictive Suite puts machine learning directly in your hands. Starting with [Predictive Churn]({{site.baseurl}}/user_guide/predictive_suite/), it’s easier than ever to effectively leverage and act on data seamlessly within the Braze platform. With it, you can create a tailored machine learning model to predict the risk of churn for a specific customer base, and then message the users that machine learning determines are at-risk before it’s too late. Previews of this feature will appear in eligible Braze customers' dashboards in early August. Contact your Account Manager for access to the full feature.

### Updates to Currents Tracking Properties
Within certain Currents message engagement events (linked below), the tracking properties `canvas_variation_name` and `canvas_step_name` have been added. For a full list, check out the [Message Engagement Events Glossary]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events/) and the [Currents Changelog]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/).

### Amazon Personalize Partnership
Amazon Personalize uses machine learnings to help create high-quality recommendations for your website and applications. Amazon personalize enables you to improve customer engagement by powering real-time personalized product and content recommendations, and targeted marketing promotions. For more information, check out our [Amazon Personalize]({{site.baseurl}}/partners/data_augmentation/recommendation/amazon_personalize/) documentation.

### Vizbee Partnership
Vizbee enables all smartphones and smart TVs in your home to work together as one seamless device for great user experiences. Vizbee helps leverage existing mobile app marketing channels like notifications, deep-links, and emails to acquire and engage viewership across all CTV devices (like Roku, FireTV, Samsung TV, LG TV, etc.) For more information, check out our [Vizbee]({{site.baseurl}}/partners/channel_extensions/deep_linking/vizbee_for_tv_deeplinking/) documentation. 

### Bluedot Partnership
Bluedot is a location platform that provides an accurate and straightforward geofencing for apps. You can use Bluedot’s SDK to message smarter, automate mobile order check-ins, optimize workflows, and create functionless experiences. For more information, check out our [Bluedot]({{site.baseurl}}/partners/data_augmentation/contextual_location/bluedot/#bluedot) documentation. 

### Iterate Partnership
Iterate makes it easy to learn from your customer, offering smart, user-friendly survey tools that look and feel like your brand. For more information, check out our [Iterate]({{site.baseurl}}/partners/additional_channels/surveys/iterate/) documentation. 

## July 2020
### Promotion Codes
Using Liquid, you can have your messages pull from a list of [promotion codes]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes/#promotion-codes) you upload. This feature offers expiry dates of up to six months and supports u to 20MM individual codes per list.

### Variant Retention Report
When looking at a retention report for a [campaign]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/retention_reports/) or [canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/retention_reports/), you can now view the results broken down by variant. 

### 'Filter' option for campaigns and canvases
The filter option for canvas and campaign GET list endpoints allow your customers to know the last time a campaign or canvas message was updated.

### Currents 'ad-id'
Updated [storage connect documentation]( {{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events/#content-card-click-events) to reflect the new `ad-id` (advertiser ID) fields to Currents.

### BCC functionality
The [BCC Address setting]({{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/email_settings/) allows you to add and manage BCC address that can be appeneded to outbound email messages sent from Braze. 

## June 2020

### Retention Reports 

Retention Reports now offer Range Retention - Range Retention measures how many users come back and perform a selected retention event during specific intervals of time. To read more about Range Retention and Retention Reports, visit out [Canvas][1] and [Campaign][2] docs. 

### Users/Track API Updates

The [users/track][3] endpoint now has a default rate of 50,000 API requests per minute for dashboard companies created after June 2nd, 2020. Existing companies created before this date and their app groups will still be allowed unlimited API requests to the users/track endpoint.

Braze is imposing this default on our most heavily used customer-facing endpoint as a step toward our stability and reliability goals for our API and infrastructure. The limit imposed is very liberal, and will affect very few dashboard companies and their regular operations. In the event that you need an increase to this limit, please reach out to your Customer Success Manager to request an increase.

## May 2020

### Google Tag Manager

Added documentation and examples of how to deploy and manage Braze's Android SDK using [Google Tag Manager]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/android_google_tag_manager/).

### New Blacklist Email API Endpoint
You can now [blacklist]({{site.baseurl}}/api/endpoints/email/post_blacklist/) email addresses via the Braze API. Blacklisting an email address will unsubscribe the user from email and mark them as hard bounced.

### API Key Change for Braze Endpoints

As of May 2020, Braze has changed how we read API keys to be more secure. Now API keys should be passed in as a request header. Examples can be found on individual endpoint pages under __Example Request__, as well as in the __API Key Explantion__ below.

Braze will continue to support the `api_key` being passed through the request body and URL parameters, but will eventually be sunset (TBD). __Please update your API calls accordingly.__ These changes have been updated within [Postman](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#intro) and will soon be input into the Braze [Swagger UI](https://www.braze.com/docs/api/interactive). 
{% details API Key Explanation %}
{% tabs %}
{% tab GET Request %}
This example uses the /email/hard_bounces endpoint.

__Before: API Key in Request Body__
```
curl --location --request GET 'https://rest.iad-01.braze.com/email/hard_bounces?api_key=YOUR_REST_API_KEY&start_date=2019-01-01&end_date=2019-02-01&limit=100&offset=1&email=foo@braze.com' \
```
__Now: API Key in Header__
```
curl --location --request GET 'https://rest.iad-01.braze.com/email/hard_bounces?start_date=2019-01-01&end_date=2019-02-01&limit=100&offset=1&email=foo@braze.com' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'
```
{% endtab %}
{% tab POST Request %}
This example uses the /user/track endpoint.

__Before: API Key in Request Body__
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--data-raw '{
  "api_key": YOUR-API-KEY-HERE ,
  "attributes": [ 
  {
    "external_id":"user_id",
      "string_attribute": "sherman",
      "boolean_attribute_1": true,
      "integer_attribute": 25,
      "array_attribute": ["banana", "apple"]
    }
    ]
}'
```
__Now: API Key in Header__
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
  "attributes": [ 
  {
    "external_id":"user_id",
      "string_attribute": "sherman",
      "boolean_attribute_1": true,
      "integer_attribute": 25,
      "array_attribute": ["banana", "apple"]
    }
    ]
}'
```
{% endtab %}
{% endtabs %}
{% enddetails %}

## April 2020

### Movable Ink Partnership

Movable Ink provides Braze customers the ability to use Intelligent Creative features like __Countdown Timers, Polls, and Scratch Offs in their Push, In-App Message and Content Card campaigns__. Movable Ink and Braze power a more well-rounded approach to dynamic data-driven messages, providing users with real-time elements about the things that matter.

For more information on how to start integrating Movable Ink into your campaigns, check out our [documentation]({{site.baseurl}}/partners/channel_extensions/creative_and_personalization/intelligent_creative/movable_ink/).

### Intelligent Timing

When scheduling a campaign, you can use Intelligent Timing (previously Intelligent Delivery) to deliver your message to each user at the time which Braze determines that an individual is most likely to engage.

Updates to this feature include:
- __Clarification of Quiet Hours__ - Quiet Hours functionality remains the same, but the UI has been adjusted for clarification.
- __Addition of Preview Chart__ - you may now generate a chart to see how many users will receive messages for each hour of the day with Intelligent Timing, as well as what proportion of users have enough data to compute an optimal time.
- __Addition of Custom Fallback__ - you may now choose the local time at which to send users a message when they lack sufficient engagement data to compute an optimal time

Check out our [documentation]({{site.baseurl}}/user_guide/intelligence/intelligent_timing/) for more information. 

### Facebook Audience Export

Braze provides the ability to manually export your users from the Braze Segments page to create Facebook Custom Audiences. This is a one-time, static audience export and will only create new Facebook Custom Audiences.

__Currently available for all Clusters__, a new Braze Facebook Audience Export process exists, streamlining the process with simple integration steps. You will no longer need to whitelist OAuth Redirect URI's to send custom audiences or mess around within Facebook App Settings to integrate. 

{% alert important %}
__Please note that all clients currently using Facebook Custom Audiences, MUST reintegrate their Braze Segments with these new steps.__
{% endalert%}

For access to the new simplified Facebook Audience Export steps, check out our documentation [here]({{site.baseurl}}/partners/facebook/).

### Content Block and Email Template API Updates

The [template/email/list]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates/) and [content_block/list]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks/) API endpoints have been updated to include a new `tags` field. This field will list as an array, any tags that apply to the current block or email template.

### Personalized From-Address

When creating an email message within Braze, you can now personalize the From Address of the message in the "Sending Info" section of email composition. You can use any of [our supported personalization tags]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/)

![Personalized From Address][0]{: style="max-width:80%"}

[support]: {{site.baseurl}}/support_contact/
[0]: {% image_buster /assets/img/personalized-from-name.png %}
[1]: {{site.baseurl}}/user_guide/engagement_tools/canvas/retention_reports/
[2]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/retention_reports/
[3]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/
[5]: {% image_buster /assets/img/campaign_comparison/campaign_main.png %} 

