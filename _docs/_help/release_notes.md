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

## April 2021

### Segment Extension
A Segment Extension expands our existing segmentation capabilities by enabling you to target more precise lists of users based on their custom event and purchase behavior in the past 365 days. Once these extension lists are generated, they can then be included/excluded as a filter in your Segments. When creating a Segment Extension, you can also specify that the list be regenerated once every 24 hours. Read more about Segment Extensions [here]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension). 

### A2P 10DLC
A2P 10DLC refers to a system in the United States that allows businesses to send Application-to-Person (A2P) type messaging via a standard 10-digit long code (10DLC) phone number. 10-digit long codes have traditionally been designed for Person-to-Person (P2P) traffic, causing businesses to be constrained by limited throughput and heightened filtering. __All customers who currently have and/or use long codes are required to register their long codes for 10DLC__. To read more about A2P 10DLC, visit our documentation [here]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/short_and_long_codes/#application-to-person-10-digit-long-codes-a2p-10dlc).

### Global Control Groups
Global Control Groups allow you to analyze the overall impact of your messaging efforts over time. These Groups can help you understand how your marketing campaigns and Canvases result in an uplift in sessions and custom events, by comparing the behaviors of users that receive messaging to those that don’t. To read more about Global Control Groups, visit our documentation [here]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/).

## March 2021

### Fastly Updates
Beginning March 22, 2021, the Braze Services will require TLS connections support Server Name Indication (SNI), as our upstream content delivery network Fastly is migrating all TLS traffic to require SNI. All modern browsers, operating systems, and HTTPS connectivity protocols support SNI. Devices which do not support SNI will no longer be able to connect to Braze. Our traffic estimations indicate this is approximately 0.000001% of end user devices.

### Audience Paths
[Canvas Audience Paths]({{site.baseurl}}/audience_paths/) allows you to intuitively filter and segment users on a large scale with strategic priority-based user-groupings. This new Canvas step replaces the need to create excessive audience-based full steps, allowing you to combine what might have been 8 full steps into one! The introduction of this new step will help you simplify user targeting while clearing up your Canvases from unnecessary clutter and complexity.

### Total Data Points Dashboard
A [Total Data Points Dashboard]({{site.baseurl}}/subscription_and_usage/) has been added to the subscription and usage component of the Braze dashboard. This dashboard will allow you to look at contract details, app group data point usage across the current billing cycle, and data point usage over time.  

## February 2021

### Canvas Report Builder
The Report Builder allows you to compare the results of multiple campaigns or Canvases in a single view so that you can easily determine which engagement strategies most impacted your key metrics. To read more about the Canvas Report Builder, check out our documentation [here]({{site.baseurl}}/user_guide/data_and_analytics/your_reports/report_builder/).

### In-App Message iOS Implementation Guide
This detailed guide covers how to leverage subclassing to create custom slideup in-app messages, custom modal in-app messages, and custom full in-app messages to add to your Braze campaigns and Canvases. Included are the necessary code consideration, detailed use cases built by our team, and accompanying code snippets. Visit our documentation [here]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/implementation_guide/) to read more. 

### SMS Custom Keyword Categories and Retargeting Options
Braze has expanded our native SMS capabilities to include the ability to add custom keywords for two-way messaging, custom categories for keywords, multi-language support, and keyword retargeting and filtering options. To read more about SMS keyword processing, visit our [SMS documentation]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/keyword_handling/). 

### Playable Partnership is Live
Expand Braze's email capabilities to deliver your best content (high-quality video) to your best audience (email) with Playable. Playable video emails allow you to increase your click-through and post-click metrics with exciting high-quality video content that plays automatically within the inbox. To read more about Playable, visit our documentation [here]({{site.baseurl}}/partners/playable/).

### Zendesk Partnership is Live
Zendesk Support Suite (ZSS) offers businesses the ability to have natural conversations with their customers through omnichannel support using email, webchat, voice, or social messaging apps. ZSS values customer support through tracking and prioritizing interactions, allowing businesses to have a unified historical view of their customers. Powerful tools such as a streamlined ticketing system allow businesses to reach out directly to customers with a personalized approach. Braze offers a server-to-server integration with Zendesk, allowing you to utilize the Braze webhooks that can sync support ticket data between Braze and Zendesk. To read more about our Zendesk integration, visit our documentation [here]({{site.baseurl}}/partners/zendesk/)

### Crowdin Partnership is Live

Crowdin is a cloud-based software for localization management. Braze integration with Crowdin allows you to translate email templates and content blocks. You can synchronize content from your Braze account to your Crowdin project and add translations back to Braze. To read more about our Crowdin integration, visit our article [here]({{site.baseurl}}/partners/crowdin/).

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

[support]: {{site.baseurl}}/support_contact/
[1]: {{site.baseurl}}/user_guide/engagement_tools/canvas/retention_reports/
[2]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/retention_reports/
[3]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/
[5]: {% image_buster /assets/img/campaign_comparison/campaign_main.png %} 

