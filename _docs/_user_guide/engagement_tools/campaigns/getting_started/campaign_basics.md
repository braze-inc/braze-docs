---
nav_title: Campaign Basics
article_title: Campaign Basics
page_order: 1
page_type: reference
description: “This reference article covers the basics of campaigns, covering various questions you should ask yourself as you set up your first campaigns.”
tool: Campaigns

---

# Campaigns: The Basics

## Find Your Strategy with the Five W’s of Visualization

Answer the questions below to get started:

* __What__ am I trying to help the customer do or understand? (Campaign Name)

* __When__ will a user start this experience? Pick one.
  * Enter users at a designated time: __Scheduled__
    * Start a session
    * Perform a custom event
    * Enter a location
    * Interact with or leave another campaign or Canvas
  * Enter user when they perform actions: __Action-Based__
    * Make a purchase
    * Start a session
    * Perform a custom event
    * Enter a location
    * Interact with or leave another campaign or Canvas
  * Enter users when they perform a specific action that triggers an API request to Braze (advanced): __API-Triggered__
    * API-triggered campaigns give you the flexibility to house message content inside of the Braze dashboard while dictating when a message is sent and to whom, via your API.<br><br>

* __Who__ are we trying to reach? (Segment Name with _optional_ additional filters)
  * Custom Data
  * User Activity
  * Retargeting
  * Marketing Activity
  * User Attributes
  * Install Attribution
  * Social Activity<br><br>

* __Why__ am I creating this campaign?
  * Start Session: I want them coming back and engaging with the app.
  * Make Purchase: I want them to buy.
  * Perform Custom Event: I want them to perform a specific action that I’m tracking as a custom event.
  * Upgrades App: I want them to upgrade their app version<br><br>

* __Where__ will we reach them?
  * Email
  * Push (Android, iOS, Windows, web)
  * In-app Messages
  * Content Cards
  * SMS or MMS
  * Webhook<br><br>

* __How__ will we reach them? (Great place to test different messaging configurations)
  * Timing: Schedule or trigger messages using tools like Intelligent Timing and delays after trigger events
  * Cadence & Channel: Use one channel and then another or sent messages on multiple channels simultaneously
  * Content: Build creative copy with strong appeals, value propositions, and CTAs
  * Targeting: Add additional segments and/or filters
  * Triggers: Use customer actions to trigger messages<br><br>

## Building The Customer Journey Campaign

### Name Your Campaign: The “What”

Never underestimate the power of the name. Braze is built for collaboration, so this is an excellent time to get grounded in how you’ll communicate goals with your team. You can add Tags (including Teams Tags) and name both steps and variants within the campaign. For more on customer journeys, check out our [Mapping User Lifecycles LAB course](http://lab.braze.com/mapping-customer-lifecycles)!

### Create Starting Conditions: The “When”

When will a customer run into this campaign? Users can enter your campaign in three ways: scheduled, action-based, or API-triggered.

| Scheduled | Action-Based | API-Triggered |
|---|---|---|
|You can use scheduled delivery when you want to send a campaign out immediately to your target audience, have it regularly sent, or schedule it for a specific time in the future. | These campaigns respond to specific customer behaviors as they happen. These action-based triggers can include opening your app, making a purchase, interacting with another campaign, or triggering any custom event. | Your marketing team and engineers will work together to determine key customer actions on your platform that, once achieved, will trigger an API call to Braze and send your campaigns. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### Select an Entry Audience for Entry: The “Who”

Who are you trying to reach? Here you can use a pre-defined segment and add further filters. Filters include:

| Filter | Description |
|---|---|
| Custom Data | Custom data filters allow you to segment users based on events and attributes you define. With them, you can use features specific to your product. |
| User Activity | User activity filters allow you to segment customers based on their actions and purchases. |
| Retargeting | Retargeting filters allow you to segment customers who have been sent, received, or interacted with previous campaigns or Canvases. |
| Marketing Activity | Marketing filters segment customers based on universal behaviors like last engagement or received campaigns. |
| User Attributes | User attribute filters segment customers by their constant attributes and characteristics. |
| Install Attribution | Install attribution filters segment customers by their first source, adgroup, campaign, or ad. |
| Social Activity | Social activity filters segment customers by their social media activity, namely through connection to Facebook and Twitter. |
{: .reset-td-br-1 .reset-td-br-2}

Only the users who match these target audience criteria can enter the journey.

### Identify Conversion Events: The “Why”
Why are you building this campaign? It’s always important to have a defined goal in mind, and campaigns help you understand how you perform against KPIs like session engagement, purchases, and custom events.

Selecting at least one conversion event will give you the ability to understand your campaign performance.

### Build the Experience: The “How” and “Where”

Consider setting up variants and A/B testing. A variant is a trail each customer follows on their journey. Campaigns support up to eight variants with a control group. While not required, you can name each variant and control the distribution of the target audience following each variant. The sky’s the limit from there—so how do you decide on the shape of your campaign? That’s where your goals, data, and hypothesis come into play. The “how” and “where” brainstorm from above will help you map out the right user journey for your campaign. There are a couple of approaches you can use:
- __Work backward:__ Some goals have smaller sub-goals. For instance, if you’re aiming for converting a free user into a subscription, you may need a page with your subscription services outlined. A visitor may need to see the options before they purchase. You may focus your messaging efforts on showing them this page before a checkout page. Working backward to understand the journey a customer must go through to get to your goal is key to guiding them through to conversion.
- __Start with the status quo and add more:__ Have you ran a similar campaign in the past? Or is one currently running? Use that one message and add to it. Try a new filter or add a follow-up message. Look at your performance and keep optimizing by making incremental changes.
- __Look to others:__ Imitation is the highest form of flattery. Don’t reinvent the wheel. Don’t worry; we have you covered. At the end of this guide, you’ll find some outlines that can help you get started.