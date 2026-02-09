---
nav_title: September
page_order: 4
noindex: true
page_type: update
description: "This article contains release notes for September 2020."
---

# September

## Funnel Reporting

Funnel Reporting offers a visual report that allows you to analyze the journeys your customers take after receiving a [campaign]({{site.baseurl}}/user_guide/analytics/reporting/funnel_reports/) or [Canvas]({{site.baseurl}}/user_guide/analytics/reporting/funnel_reports/).

## iOS 14 upgrade guide

In accordance with the changes announced in Apple's new iOS 14, there are some Braze-related changes and action items required for Braze iOS SDK integrations. For more information, take a look at this [upgrade guide]({{site.baseurl}}/ios_14/).

## Changes to IDFA and IDFV for iOS 14

In iOS 14, users must decide if they want to opt-in to ad tracking and let apps and ad networks read their IDFA when visiting an app. As a result, Braze's strategy is to instead use the "identifier for vendors" (such as IDFV) so you can continue to track users across different devices. For more information, take a look at the [iOS 14 upgrade guide]({{site.baseurl}}/ios_14/).

## Email validation

This new email syntax validation process is an upgrade to Braze's existing one. This is a check to verify that emails updated or imported into Braze are correct. For more information, take a look at [these guidelines and notes]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/email_validation/).

## Random bucket user event in Currents

The random bucket number (such as RBN) occurs every time a new user is created within their workspace. During this event, each new user gets assigned a random bucket number that you can then use to create uniformly distributed segments of random users. Use this to group a range of random bucket number values and compare performance across your campaigns and campaign variants. To see if this event is available to you, take a look at the Currents [customer behavior events glossary]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/).

## Canvas components - Coming soon!

Braze has added four new Canvas components to help make increase the flexibility and functionality of your Canvases. These new components include: [Decision Split Step]({{site.baseurl}}/decision_split/), [Delay Step]({{site.baseurl}}/delay_step/), [Messaging Steps]({{site.baseurl}}/message_step/), and [Audience Sync to Facebook]({{site.baseurl}}/audience_sync_facebook/).
- **Canvas Decision Split, Delay, and Messaging Steps**<br>Decision splits can be used to create Canvas branches depending on whether a user matches a defined query. Delay steps allow you to add a stand-alone delay to your Canvas without the need for a corresponding message. Messaging steps allow you to add a standalone message where you want in your Canvas flow.
- **Audience Sync to Facebook**<br>Using the Braze Audience Sync to Facebook, brands can elect to add their own users' data from their own Braze integration to Facebook Custom Audiences to deliver advertisements based upon behavioral triggers, segmentation, and more. Any criteria you'd normally use to trigger a message (Push, Email, SMS, Webhook, etc) in a Braze Canvas based upon your user data can now be used to trigger an ad to that user in Facebook via Custom Audiences.

## SMS inbound received events

A new messaging engagement event has been added to Currents. This event occurs when one of your users sends an SMS to a phone number in one of your Braze SMS subscription groups. For more information, check out our Currents [messaging and engagement events glossary]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/).
