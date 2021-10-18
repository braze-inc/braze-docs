---
nav_title: Release Notes
article_title: Release Notes
page_order: 4
layout: featured
guide_top_header: "Release Notes"
guide_top_text: "This is where you can find all updates to the Braze platform, with the <a href='/docs/help/release_notes/#most-recent'>most recent platform updates</a>, listed below. You can also
check out our <a href='/docs/developer_guide/platform_integration_guides/sdk_changelogs/'>SDK Changelogs</a>."
page_type: landing
description: "This landing page is home to Braze Release Notes. This is where you can find all updates to the Braze platform and SDKs, as well as a list of deprecated features."

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
> For more information on any of the updates listed in this section, reach out to your account manager or [open a support ticket][support]. You can also check out [our SDK Changelogs]({{site.baseurl}}/developer_guide/platform_integration_guides/sdk_changelogs/) to see more information on our monthly SDK releases, updates, and improvements.

## October 2021

### iOS 15
#### Apple Mail Privacy Protection
Apple’s Mail Privacy Protection (MPP) is a privacy update that will be available for users of the Apple Mail app on iOS 15, iPadOS 15, macOS Monterey, and watchOS 8, released in mid-September. For users who opt-in to MPP, emails will now be preloaded using proxy servers, caching images and hindering the ability to leverage tracking pixels for metrics like [open tracking]({{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/email_settings/#email-open-tracking-pixel/). To learn more about MPP and issues regarding email deliverability metrics and issues with pre-existing campaigns and Canvases that trigger based on these metrics, visit our [documentation]({{site.baseurl}}/user_guide/message_building_by_channel/email/mpp/).

#### Push Features
iOS 15 introduced new notification features to help users stay focused and avoid frequent interruptions throughout the day. We're excited to offer support for these new features, including [Interruption Levels and Relevance Scores]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/).

### Contact Cards
Contact Cards are a standardized file format for sending business and contact information that can be easily imported into address books or contact books. You can now upload and create Contact Cards for your SMS and MMS messages. To read more about how to build Contact Cards in our built-in Contact Card Generator, visit our [documentation]({{site.baseurl}}/user_guide/message_building_by_channel/sms/mms/contact_card/).

### Out-of-the-Box Content Cards Customization
You can create your own Content Cards interface by extending `ABKContentCardsTableViewController` to customize all UI elements and Content Cards behavior. To read more about how to customize the Content Cards Feed, visit our [documentation]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/content_cards/customization/#customizing-the-content-cards-feed/). 

### API Rate Limits
[Rate limits]({{site.baseurl}}/api/basics/#api-limits/) will apply to all customers onboarded after September 16, 2021. 

### Updates to Android and FireOS Developer Guides
Android and FireOS developer guides have merged into one location. Dedicated FireOS articles will be available in this [new Android section]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/fireos/integration/).

### Updates to Funnel and Retention Reports
[Funnel Reports]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_funnel_reports/) and [Retention Reports]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/retention_reports/) are now available for SMS campaigns.

## September 2021

### Google Audience Sync
The Braze [Audience Sync to Google]({{site.baseurl}}/partners/canvas_steps/google_audience_sync/) integration enables brands to extend the reach of their cross-channel customer journeys to Google Search, Google Shopping, Gmail, YouTube, and Google Display. Using your first-party customer data, you can securely deliver ads based upon dynamic behavioral triggers, segmentation, and more. Any criteria you'd typically use to trigger a message (e.g., push, email, SMS, etc.) as part of a Braze Canvas can be used to trigger an ad to that user via Google's Customer Match.

### Best Practice iOS SDK Integration Guide
This optional [iOS integration SDK guide]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/ios_sdk_integration/) takes you on a step-by-step journey on setup best practices when first integrating the iOS SDK and its core components into your application. This guide will help you build a `BrazeManager.swift` helper file that will decouple any dependencies on the Braze iOS SDK from the rest of your production code, resulting in one `import AppboyUI` in your entire application. This approach limits issues that arise from excessive SDK imports, making it easier to track, debug, and alter code. 

### Predictive Purchases
Predictive Purchases give marketers a powerful tool for identifying and messaging users based on their likelihood to make a purchase. When you create a Purchase Prediction, Braze trains a machine learning model using [gradient boosted decision trees](https://en.wikipedia.org/wiki/Gradient_boosting) to learn from previous purchase activity and predict future purchase activity. Visit our [Predicitve Purchases]({{site.baseurl}}/user_guide/predictive_suite/predictive_purchases/) doc to learn more. 

### Drag & Drop Editor
With Braze Email, you can create completely custom and personalized email messages in either Campaigns or Canvas using our new Drag & Drop editing experience. Users can now drag editor blocks into their emails, allowing more intuitive customization. To learn how to get started with the Drag & Drop Editor, visit our [documentation]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/overview/). 

### User Alias Import
To target users who don't have an `external_id`, you can import a list of users with user aliases. An alias serves as an alternative unique user identifier. It can be helpful if you are trying to market to anonymous users who haven't signed up or made an account with your app. Visit our [documentation]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#import-with-user-alias) to learn more. 

### iOS 15 Upgrade Guide
This [guide]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/ios_15/) outlines changes introduced in iOS 15 (WWDC21) and the required upgrade steps for your Braze iOS SDK integration.

### Android 12 Upgrade Guide
This [guide]({{site.baseurl}}/developer_guide/platform_integration_guides/android/android_12/) describes relevant changes introduced in Android 12 (2021) and the required upgrade steps for your Braze Android SDK integration.

### A2P 10DLC
A2P 10DLC refers to a system in the United States that allows businesses to send Application-to-Person (A2P) type messaging via a standard 10-digit long code (10DLC) phone number. 10-digit long codes have traditionally been designed for Person-to-Person (P2P) traffic, causing businesses to be constrained by limited throughput and heightened filtering. This service helps alleviate those issues, improving overall message deliverability, allowing brands to send messages at scale, including links and calls to action, and helping further protect consumers from unwanted messages. 

All customers who currently have and/or use US long codes to send to US customers must register their long codes for 10DLC. To read more about the specifics of 10DLC and why it's required, visit our dedicated [10DLC article]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/10dlc/).

### Two-Factor Authentication Reset
Users experiencing issues logging in via two-factor authentication can reach out to their company admins to reset their two-factor authentication. Visit our [documentation]({{site.baseurl}}/user_guide/administrative/company_settings/security_settings/#user-authetication-reset) to learn more. 

### New Braze Partnerships

#### Hightouch - Workflow Automation
The Braze and [Hightouch]({{site.baseurl}}/partners/data_and_infrastructure_agility/workflow_automation/hightouch/) integration allows you to build better campaigns on Braze with up-to-date customer data from your data warehouse. You want to provide relevant, timely interactions to your customers, and doing so heavily relies on data in your Braze account to be accurate and fresh. By automatically syncing customer data from your data warehouse into Braze, you no longer need to worry about data consistency, and you can focus on building world-class customer experiences.

#### Transcend - Data Privacy & Compliance
The Braze and [Transcend]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_privacy/transcend/) partnership helps users automate privacy requests by orchestrating data across dozens of data systems. Ultimately, this helps teams comply with regulations like GDPR and CCPA and puts individuals in the driver's seat when it comes to their data.

#### Tinyclues - Cohort Import
[Tinyclues]({{site.baseurl}}/partners/data_and_infrastructure_agility/cohort_import/tinyclues/) is an audience-building feature that offers the capability to increase the number of campaigns and revenue without harming customer experience, and analytics to track the performance of CRM campaigns both online and offline. Together, the Braze and Tinyclues integration offers users a path to better CRM planning and strategy, allowing users to send more targeting campaigns, find new product opportunities, and elevate revenue using an incredibly user-friendly UI.

#### optilyz - Direct Mail
[optilyz]({{site.baseurl}}/partners/message_orchestration/additional_channels/direct_mail/optilyz/) is a direct mail automation platform that enables you to run more customer-centric, sustainable, and profitable direct mail campaigns. optilyz is used by hundreds of companies across Europe and empowers you to integrate letters, postcards, and self-mailers into your cross-channel marketing and automate and better personalize campaigns. Use the optilyz and Braze webhook integration to send direct mail to your customers.

## August 2021

### Simple Survey In-App Message
Use the new Simple Survey In-App Message template to collect user attributes, insights, and preferences that power your campaign strategy. For example, you can ask users how they’d like to use your app, learn more about their personal preferences, or even ask about their satisfaction with a particular feature. This survey template is supported for both mobile apps and web browsers. Visit our [documentation]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/) to get started.

### Liquid Use Case Library
Wondering how to do that one thing with Liquid? Just looking for inspiration? Check out our new [Liquid Use Case Library]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/liquid_use_cases/) for a collection of use cases ranging from Anniversaries and Birthdays to Platform Targeting and more.

### Email Tracking
Open pixel tracking and click tracking can now be disabled per user profile. This flexibility helps customers support regional privacy laws, where an individual user profile might indicate they no longer want to be tracked. Visit our [documentation]({{site.baseurl}}/user_guide/data_and_analytics/tracking/email_tracking/) to learn more.

### SDK Data Collection Options
Learn more about how the Braze SDK can be integrated to allow for flexible data collection in our new documentation on [SDK Data Collection Options]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/sdk_data_collection/).

### SSL Overview
Learn more about SSL at Braze, why SSL is important, and how you can acquire an SSL certificate in our new [SSL Overview]({{site.baseurl}}/user_guide/onboarding_with_braze/email_setup/ssl/) documentation.

### Amplitude User Profile API Endpoints
Amplitude’s User Profile API serves Amplitude user profiles. This includes user properties, computed user properties, a list of cohort IDs of cohorts that include the user, and recommendations. Refer to [Amplitude User Profile API Endpoints]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/amplitude/amplitude_user_profile_api/) to learn more.

### Campaign Details Endpoint
The GET [`/campaigns/details`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details/) API endpoint has added a dedicated `message` response for the in-app message channel. Documentation on this can be found [here]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details/#messages).

## July 2021

### Transactional Email Campaigns
Transactional emails are those sent to facilitate an agreed-upon transaction between a sender and the recipient. Braze's Transactional email campaign type is purpose-built for sending automated, non-promotional email messages like order confirmations, password resets, billing alerts, or other business-critical notifications. In addition, a corresponding [transactional email endpoint]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_transactional_message/) has been created. Transactional emails and the new endpoint are only available as part of select Braze packages. Visit our [documentation]({{site.baseurl}}/api/api_campaigns/transactional_campaigns) to learn more. 

### Nested Object Support for Event Properties
Braze now supports [nested objects]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/nested_object_support/) for custom events and purchase events. Nested objects allow you to send arrays of data as properties of custom events and purchases. This nested data can be used for templating personalized information in API-triggered messages through the use of Liquid and dot notation.

### New HMAC Liquid Encoding Filters
New `hmac_sha1` and `hmac_sha256` Liquid encoding filters have been added to the Braze platform. Documentation on these new filters can be found [here]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/).

### Purchase Event Page
Curious about the details of purchase events at Braze? Visit our dedicated [purchase event documentation]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/purchase_events/) to learn more.

### New Partners 

#### Nexla - Workflow Automation Partner
[Nexla]({{site.baseurl}}/partners/nexla) is the leader in unified data operations and a 2021 Gartner Cool Vendor. Customers that use Currents to send data to data warehouses can leverage Nexla to extract, transform, and load that data to other locations, making data easily accessible across your entire ecosystem. Nexla enables you to use Braze Currents to get data in a custom format delivered to your destination of choice by a simple point and click. 

#### Amperity - Customer Data Platform Partner
[Amperity]({{site.baseurl}}/partners/amperity/) is a comprehensive enterprise customer data platform, helping brands get to know their customers, make strategic decisions, and consistently take the right course of action to serve their consumers better. Amperity supports the Braze platform by providing a unified view of your customers across its CDP and Braze allowing you to send valuable Amperity data to Braze.

#### Digioh - Survey Partner
[Digioh]({{site.baseurl}}/partners/digioh/) helps you grow your lists, capture first-party data, and put your data to use in your Braze campaigns. The drag-and-drop builder makes it easy to create on-brand forms, pop-ups, preference centers, landing pages, and surveys that connect you with your customers.

#### AppsFlyer Audiences - Attribution/Analytics Partner
[AppsFlyer]({{site.baseurl}}/partners/message_orchestration/attribution/appsflyer/) is a mobile marketing analytics and attribution platform that helps you analyze and optimize your apps through marketing analytics mobile attribution, and deep linking. [AppsFlyer Audiences]({{site.baseurl}}/partners/appsflyer_audiences/) allow you to build audience segments and pass these segments directly to Braze to create powerful customer engagement campaigns.

## June 2021

### Conversion Correlation
This guide covers the [Conversion Correlation]({{site.baseurl}}/user_guide/engagement_tools/testing/conversion_correlation/) analysis on the **Campaign Analytics** page, which gives you insight into what user attributes and behaviors help or hurt the outcomes you set for campaigns. Covered is an overview of the analysis, what is checked, when it's available, and how Braze checks for significance.

### Global Control Group Report
We've updated the metrics on the [Global Control Groups]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/) report to better help you analyze the overall impact of your messaging efforts over time. Key changes include adding **Events per User** and **Estimated Group Size**, and adjusting the calculation for **Incremental Uplift** to reflect the difference in total events between your treatment and control groups.

### Reports Overview
Not sure where to start with analyzing your campaigns or Canvases? The [Reports Overview]({{site.baseurl}}/user_guide/data_and_analytics/your_reports/reports_overview/) provides guidance on which reports and analytics you can use to answer common marketing strategy questions.

### New US-05 Cluster
Braze supports a new US cluster, US-05. Refer to our list of dashboard and REST [Endpoints]({{site.baseurl}}/api/basics/#endpoints) to see more.

### Braze UI Updates
In May 2021, Braze updated the following labels and terms in the Braze dashboard:

- App Usage --> Overview
- App Settings --> Settings
- Manage App Group --> Manage Settings
- Money Spent In-App --> Money Spent
- App Usage (User Profile) --> Sessions Overview
- Import a CSV of user information to add and/or update users in this App Group --> Import a CSV of user information to add or update users

## May 2021

### iOS Push Advanced Implementation Guide
This detailed guide covers how to leverage push notification content app extensions to get the most out of your push messages. Included are three custom use cases built by our team (interactive push, data capture push, and progress based push), accompanying code snippets, and guidance on logging analytics. Visit our documentation here to read [more](/docs/developer_guide/platform_integration_guides/ios/push_notifications/implementation_guide/).

### VFC support for Multimedia Message Service (MMS)
vCards, also known as Virtual Contact Files (.VCF), are a standardized file format for sending business/contact information that can be easily imported into address/contact books. These VFC files can now be sent through MMS and added to the Braze media library. Visit our MMS documentation to [learn more]({{site.baseurl}}/user_guide/message_building_by_channel/sms/mms/create/). 

### Updates to User Delete
In October of 2020, we made improvements to how our user delete handles data subject's phone number or email address. More information about this can be found [here](https://www.braze.com/docs/help/release_notes/2020/october/)

### New Braze Partnerships

#### Airbridge - Attribution Partner
The Airbridge and Braze integration allow you to pass all organic and non-organic install attribution data to Braze to build more personalized marketing campaigns and understand exactly where users were acquired. Visit our Airbridge documentation [here]({{site.baseurl}}/partners/message_orchestration/attribution/airbridge/).

#### Kubit - Analytics Partner
Kubit is a no-code, self-service analytics platform that delivers instant product insights. Through the seamless no-code integration with Braze, you can import user Cohort information into Braze and launch engagement campaigns to target specific Cohorts. In addition, through the use of Snowflake Secure Data Sharing, you can integrate the raw campaign and impression data from Braze with product analytics in Kubit to measure the impact of these campaigns in real-time. Visit our Kubit documentation [here]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/kubit/).

#### Census - Customer Data Platform Partner
Census allows you to keep your customer success, sales, and marketing teams all on the same page by keeping your customer data in sync, all without ongoing help from your engineering department. Visit our Census documentation [here]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/census/)

#### Treasure Data - Customer Data Platform Partner
Treasure Data helps drive relevant customer experiences by harmonizing data, insights, and engagement to work in perfect unison. Armed with actionable indicators, CX Teams, including marketing, sales, and customer service can effectively optimize spend, and personalize omnichannel interactions across the entire customer journey. Visit our Treasure Data documentation [here]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/treasure_data/).

### Phrasee - A/B Testing
Braze customer engagement develops relationships through multichannel marketing. Working together with Phrasee, Braze can deploy brand language, at scale, across channels that are customized to your brand voice. Phrasee’s deep learning engine handles the testing, monitors the results, and generates new language based on what it’s learned. Visit our Phrasee documentation [here]({{site.baseurl}}/partners/data_and_infrastructure_agility/ab_testing/phrasee/).


[support]: {{site.baseurl}}/support_contact/