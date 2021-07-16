---
page_order: 2
nav_title: Release Notes
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

Braze supports a new US cluster, US-05. Refer to our list of Dashboard and REST [Endpoints]({{site.baseurl}}/api/basics/#endpoints) to see more.

### Braze UI Updates

In May 2021, Braze updated the following labels and terms in the Braze Dashboard:

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

## April 2021

### Segment Extension
A [Segment Extension]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension) expands our existing segmentation capabilities by enabling you to target more precise lists of users based on their custom event and purchase behavior in the past 365 days. Once these extension lists are generated, they can then be included/excluded as a filter in your Segments.

### A2P 10DLC
A2P 10DLC refers to a system in the United States that allows businesses to send Application-to-Person (A2P) type messaging via a standard 10-digit long code (10DLC) phone number. 10-digit long codes have traditionally been designed for Person-to-Person (P2P) traffic, causing businesses to be constrained by limited throughput and heightened filtering. __All customers who currently have and/or use long codes are required to register their long codes for 10DLC__. To read more about A2P 10DLC, visit our documentation [here]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/short_and_long_codes/#application-to-person-10-digit-long-codes-a2p-10dlc).

### Global Control Groups
[Global Control Groups]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/) allow you to analyze the overall impact of your messaging efforts over time. These Groups can help you understand how your marketing campaigns and Canvases result in an uplift in sessions and custom events, by comparing the behaviors of users that receive messaging to those that don’t. 

## March 2021

### Fastly Updates
Beginning March 22, 2021, the Braze Services will require TLS connections support Server Name Indication (SNI), as our upstream content delivery network Fastly is migrating all TLS traffic to require SNI. All modern browsers, operating systems, and HTTPS connectivity protocols support SNI. Devices which do not support SNI will no longer be able to connect to Braze. Our traffic estimations indicate this is approximately 0.000001% of end-user devices.

### Audience Paths
[Canvas Audience Paths]({{site.baseurl}}/audience_paths/) allows you to intuitively filter and segment users on a large scale with strategic priority-based user groupings. This new Canvas step replaces the need to create excessive audience-based full steps, allowing you to combine what might have been 8 full steps into one! The introduction of this new step will help you simplify user targeting while clearing up your Canvases from unnecessary clutter and complexity.

## February 2021

### Canvas Report Builder
The Report Builder allows you to compare the results of multiple campaigns or Canvases in a single view so that you can easily determine which engagement strategies most impacted your key metrics. To read more about the Canvas Report Builder, check out our documentation [here]({{site.baseurl}}/user_guide/data_and_analytics/your_reports/report_builder/).

### In-App Message iOS Implementation Guide
This detailed guide covers how to leverage subclassing to create custom slide-up in-app messages, custom modal in-app messages, and custom full in-app messages to add to your Braze campaigns and Canvases. Included are the necessary code consideration, detailed use cases built by our team, and accompanying code snippets. Visit our documentation [here]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/implementation_guide/) to read more. 

### SMS Custom Keyword Categories and Retargeting Options
Braze has expanded our native SMS capabilities to include the ability to add custom keywords for two-way messaging, custom categories for keywords, multi-language support, and keyword retargeting and filtering options. To read more about SMS keyword processing, visit our [SMS documentation]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/keyword_handling/). 

### Playable Partnership is Live
Expand Braze's email capabilities to deliver your best content (high-quality video) to your best audience (email) with Playable. Playable video emails allow you to increase your click-through and post-click metrics with exciting high-quality video content that plays automatically within the inbox. To read more about Playable, visit our documentation [here]({{site.baseurl}}/partners/playable/).

### Zendesk Partnership is Live
Zendesk Support Suite (ZSS) offers businesses the ability to have natural conversations with their customers through omnichannel support using email, webchat, voice, or social messaging apps. ZSS values customer support through tracking and prioritizing interactions, allowing businesses to have a unified historical view of their customers. Powerful tools such as a streamlined ticketing system allow businesses to reach out directly to customers with a personalized approach. Braze offers a server-to-server integration with Zendesk, allowing you to utilize the Braze webhooks that can sync support ticket data between Braze and Zendesk. To read more about our Zendesk integration, visit our documentation [here]({{site.baseurl}}/partners/zendesk/)

### Crowdin Partnership is Live

Crowdin is a cloud-based software for localization management. Braze integration with Crowdin allows you to translate email templates and content blocks. You can synchronize content from your Braze account to your Crowdin project and add translations back to Braze. To read more about our Crowdin integration, visit our article [here]({{site.baseurl}}/partners/crowdin/).


[support]: {{site.baseurl}}/support_contact/
[1]: {{site.baseurl}}/user_guide/engagement_tools/canvas/retention_reports/
[2]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/retention_reports/
[3]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/
[5]: {% image_buster /assets/img/campaign_comparison/campaign_main.png %} 