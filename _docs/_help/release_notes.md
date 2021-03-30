---
page_order: 2
nav_title: Release Notes
layout: featured
guide_top_header: "Release Notes"
guide_top_text: "This is where you can find all updates to the Braze platform, with the <a href='/docs/help/release_notes/#most-recent'>most recent platform updates</a>, listed below. You can also
check out our <a href='/docs/developer_guide/platform_integration_guides/sdk_changelogs/'>SDK Changelogs</a>."

guide_featured_title: "Release Notes"
guide_featured_list:
  - name: 2021
    link: /docs/help/release_notes/2021/
    fa_icon: fas fa-calendar-alt
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

## December 2020

### Updates to Currents Messaging Event Properties
Within Currents email messaging engagement events (linked below), the tracking property `ip_pool` has been added. The tracking properties `bounce_reason` and `bounce_code` have also been added to `users.messages.email.Bounce` and `users.messages.email.SoftBounce` events. <br>For the full list, check out the [Message Engagement Events Glossary]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events/).

### Predictive Churn FAQ
A frequently asked questions article has been added to the existing Predictive Churn documentation. To read more about these potential errors, timing clarifications, and data considerations, check out our [Predictive Churn]({{site.baseurl}}/user_guide/predictive_suite/predictive_churn/prediction_faq/) FAQ documentation.

### CSV and API Exports Troubleshooting Doc
A troubleshooting doc detailing common CSV and API errors has been added to the Braze documentation. To read more about these errors as well as some frequently asked questions, check out our CSV and API export [troubleshooting]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/) documentation. 

### EduMe Partnership
EduMe is a mobile-based training tool that gives your workforce the knowledge they need to succeed. Use Connected Content in Braze to give your workforce or your customers access to lessons and courses in EduMe. They will be able to access this content seamlessly in their browser, and you will be able to follow their progress as a group or as individuals using the EduMe reporting functionality. For more information, check out our [EduMe]({{site.baseurl}}/partners/channel_extensions/learning/edume/) documentation.

### Pypestream Partnership
Pypestream is a full-stack, conversational AI platform offering patented, all-in-one cloud messaging to transform brands into “always-on” digital entities. With the Braze-Pypestream partnership, brands can seamlessly orchestrate the end-to-end customer lifecycle from initial outreach, routed into a conversational experience, and through to omnichannel follow-up(s) via intelligent retargeting. For more information, check out our [Pypestream]({{site.baseurl}}/partners/advertising_technologies/attribution/pypestream/) documentation.

### Dyspatch Partnership
With Dyspatch, use the intuitive drag and drop email builder to create beautiful, responsive, and engaging emails without needing to write code. Collaborate with your team to create and approve emails within Dyspatch and then upload them to use within Braze, all in a couple of quick steps! For more information, check out our [Dyspatch]({{site.baseurl}}/partners/channel_extensions/creative_and_personalization/email_orchestration/dyspatch/) documentation.

### RudderStack Partnership
RudderStack is an open-source Customer Data Infrastructure for collecting and routing customer event data to your preferred data warehouse and dozens of other analytics providers, such as Braze. It is enterprise-ready and offers a robust transformation framework to process your event data on the fly. For more information, check out our [RudderStack]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/rudderstack/#rudderstack) documentation.

### Jebbit Partnership
Jebbit is a PaaS to which you can build engaging experiences for users to capture first-party data. Jebbit has partnered with Braze so that you can pass user emails and attributes from your Jebbit campaigns as user data to Braze in real-time. This data can then be utilized to drive marketing initiatives like personalized email campaigns and triggers. For more information, check out our [Jebbit]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/jebbit/#jebbit)  documentation.

## November 2020

### Tealium Partnership is live
[Tealium]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/tealium/#about-tealium) is a data hub that makes it easy to connect mobile, web, and alternative data from third-party sources. When connected with Braze, Tealium enables a data flow of custom events, user attributes, and purchases for real-time data action.

### Braze Product Portal
The [Braze Product Portal]({{site.baseurl}}/user_guide/administrative/access_braze/portal/#product-portal-) contains the Braze product roadmap and opportunity for users to submit ideas. You can also see which features have been recently released. The product portal can be found in the upper-right section of the Braze dashboard, under “Resources”.

### iOS Content Card Implementation Guide
Embracing developer-centered technical strategy, Braze has released it's first implementation guide highlighting use-case driven iOS Content Card guidelines and best practices. This comprehensive guide provides unique use cases, video walkthroughs, accompanying code snippets, and guidance on how to log valuable user metrics. To read more about how you can get started implementing iOS Content Cards like a pro, [click here]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/content_cards/implementation_guide/). 

### Swift Package Manager
The Swift Package Manager is integrated with the Swift build system and automatically will download, compile, and link dependencies. Installing the iOS SDK via Swift Package Manager will automate the majority of the installation process for you. For more information, take a look at the [documentation]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_SDK_setup/swift_package_manager).

## October 2020

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

## September 2020

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

## August 2020

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

The [users/track][3] endpoint now has a default rate of 50,000 API requests per minute for dashboard companies created after June 2, 2020. Existing companies created before this date and their app groups will still be allowed unlimited API requests to the users/track endpoint.

Braze is imposing this default on our most heavily used customer-facing endpoint as a step toward our stability and reliability goals for our API and infrastructure. The limit imposed is very liberal, and will affect very few dashboard companies and their regular operations. In the event that you need an increase to this limit, please reach out to your Customer Success Manager to request an increase.

[support]: {{site.baseurl}}/support_contact/
[1]: {{site.baseurl}}/user_guide/engagement_tools/canvas/retention_reports/
[2]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/retention_reports/
[3]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/
[5]: {% image_buster /assets/img/campaign_comparison/campaign_main.png %} 

