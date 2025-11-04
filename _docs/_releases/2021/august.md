---
nav_title: August
page_order: 4
noindex: true
page_type: update
description: "This article contains release notes for August 2021."
---

# August 2021

## Google Audience Sync

The Braze [Audience Sync to Google]({{site.baseurl}}/partners/canvas_audience_sync/google_audience_sync/) integration enables brands to extend the reach of their cross-channel customer journeys to Google Search, Google Shopping, Gmail, YouTube, and Google Display. Using your first-party customer data, you can securely deliver ads based upon dynamic behavioral triggers, segmentation, and more. Any criteria you'd typically use to trigger a message (for example, push, email, SMS, etc.) as part of a Braze Canvas can be used to trigger an ad to that user via Google's Customer Match.

## Best practice iOS SDK integration guide

This optional [iOS integration SDK guide]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=swift#swift_integrating-the-swift-sdk) takes you on a step-by-step journey on setup best practices when first integrating the iOS SDK and its core components into your application. This guide will help you build a `BrazeManager.swift` helper file that will decouple any dependencies on the Braze iOS SDK from the rest of your production code, resulting in one `import AppboyUI` in your entire application. This approach limits issues that arise from excessive SDK imports, making it easier to track, debug, and alter code. 

## Predictive Purchases

Predictive Purchases give marketers a powerful tool for identifying and messaging users based on their likelihood to make a purchase. When you create a purchase prediction, Braze trains a machine learning model using [gradient boosted decision trees](https://en.wikipedia.org/wiki/Gradient_boosting) to learn from previous purchase activity and predict future purchase activity. Visit our [Predictive Purchases]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events/) doc to learn more. 

## Drag-and-drop editor

With Braze Email, you can create completely custom and personalized email messages in either campaigns or Canvases using our new [drag-and-drop editing experience]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/). Users can now drag editor blocks into their emails, allowing more intuitive customization. 

## User alias import

To target users who don't have an `external_id`, you can [import a list of users with user aliases]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#import-with-user-alias). An alias serves as an alternative unique user identifier. It can be helpful if you are trying to market to anonymous users who haven't signed up or made an account with your app. 

## iOS 15 upgrade guide

This [iOS 15 upgrade guide]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/overview/) outlines changes introduced in iOS 15 (WWDC21) and the required upgrade steps for your Braze iOS SDK integration.

## Android 12 upgrade guide

This [Android 12 upgrade guide]({{site.baseurl}}/developer_guide/platforms/android/android_13/) describes relevant changes introduced in Android 12 (2021) and the required upgrade steps for your Braze Android SDK integration.

## A2P 10DLC

A2P 10DLC refers to a system in the United States that allows businesses to send Application-to-Person (A2P) type messaging via a standard 10-digit long code (10DLC) phone number. 10-digit long codes have traditionally been designed for Person-to-Person (P2P) traffic, causing businesses to be constrained by limited throughput and heightened filtering. This service helps alleviate those issues, improving overall message deliverability, allowing brands to send messages at scale, including links and calls to action, and helping further protect consumers from unwanted messages. 

All customers who currently have and/or use US long codes to send to US customers must register their long codes for 10DLC. To read more about the specifics of 10DLC and why it's required, visit our dedicated [10DLC article]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/user_phone_numbers/10dlc/).

## Two-factor authentication reset

Users experiencing issues logging in via two-factor authentication can reach out to their company admins to [reset their two-factor authentication]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings/#user-authetication-reset).

## New Braze partnerships

### Hightouch - Workflow Automation

The Braze and [Hightouch]({{site.baseurl}}/partners/data_and_analytics/reverse_etl/hightouch/) integration allows you to build better campaigns on Braze with up-to-date customer data from your data warehouse. You want to provide relevant, timely interactions to your customers, and doing so heavily relies on data in your Braze account to be accurate and fresh. By automatically syncing customer data from your data warehouse into Braze, you no longer need to worry about data consistency, and you can focus on building world-class customer experiences.

### Transcend - Data Privacy & Compliance

The Braze and [Transcend]({{site.baseurl}}/partners/ecommerce/payments/transcend/) partnership helps users automate privacy requests by orchestrating data across dozens of data systems. Ultimately, this helps teams comply with regulations like GDPR and CCPA and puts individuals in the driver's seat when it comes to their data.

### Tinyclues - Cohort Import

[Tinyclues]({{site.baseurl}}/partners/data_and_analytics/cohort_import/tinyclues/) is an audience-building feature that offers the capability to increase the number of campaigns and revenue without harming customer experience, and analytics to track the performance of CRM campaigns both online and offline. Together, the Braze and Tinyclues integration offers users a path to better CRM planning and strategy, allowing users to send more targeting campaigns, find new product opportunities, and elevate revenue using an incredibly user-friendly UI.

### optilyz - Direct Mail

[optilyz]({{site.baseurl}}/partners/additional_channels_and_extensions/additional_channels/direct_mail/optilyz/) is a direct mail automation platform that enables you to run more customer-centric, sustainable, and profitable direct mail campaigns. optilyz is used by hundreds of companies across Europe and empowers you to integrate letters, postcards, and self-mailers into your cross-channel marketing and automate and better personalize campaigns. Use the optilyz and Braze webhook integration to send direct mail to your customers.