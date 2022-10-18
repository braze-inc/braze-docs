---
nav_title: Canvas Basics
article_title: Canvas Basics
page_order: 1
page_type: reference
description: "This reference article covers the basics of Canvas, covering various questions you should ask your self as you set up your first Canvas."
tool: Canvas

---

# Canvas basics

## Understanding Canvas structure

Before getting started with the finer details of Canvas setup, let's identify the key components that make up a Canvas.

{% tabs %}
  {% tab Canvas %}

  {% endtab %}

  {% tab Journey %}

  {% endtab %}

  {% tab Entry Step %}

  {% endtab %}

  {% tab Variants %}

  {% endtab %}

  {% tab Steps %}

  {% endtab %}
{% endtabs %}

## Building the customer journey

By using the five W's of visualization, you can identify your customer engagement strategies for how to create a personalized message journey for each user. These five W's are: what, when, who, why, and where. 

### The "what": Name your Canvas

> What are you trying to help the user do or understand?

Never underestimate the power of the name. Braze is built for collaboration, so this is a good time to get grounded in how you’ll communicate goals with your team. 

You can add tags and name both steps and variants within the Canvas. For more on customer journeys, check out our Braze Learning course on [mapping user lifecycles](https://learning.braze.com/mapping-customer-lifecycles)!

### The "why": Identify conversion events

> Building upon the "what", why are you building this Canvas? 

It’s always important to have a defined goal in mind and Canvas helps you understand how you are performing against KPIs like session engagement, purchases, and custom events.

Selecting at least one conversion event will give you the ability to understand your campaign performance and also to help you optimize performance within the Canvas as if your Canvas has multiple variants or a control group Braze will use the conversion event to determine the best variation for achieving this goal.

* **Start Session**: I want them coming back and engaging with the app.
* **Make Purchase**: I want them to buy.
* **Perform Custom Event**: I want them to perform a specific action that I’m tracking as a custom event.
* **Upgrades App:** I want them to upgrade their app version.

### The "when": Create starting conditions

> When will a user start this experience?

Your answer will determine the details of when and how your Canvas is delivered to your customer. Users can enter your Canvas in one of two ways: scheduled or action-based triggers.

| Scheduled | Action-Based |
|---|---|
|You can use scheduled delivery when you want to send a Canvas out immediately to your target audience, have it regularly sent, or schedule it for a specific time in the future. | These Canvases respond to specific customer behaviors as they happen. These action-based triggers can include opening your app, making a purchase, interacting with another campaign, or triggering any custom event. |
{: .reset-td-br-1 .reset-td-br-2}

### The "who": Select an audience

> Who are you trying to reach? 

Here you can use a pre-defined segment and add more filters to further focus on connecting to your audience. With these segments, only the users who match the target audience criteria can enter the Canvas journey, leading to a more personalized experience.

| Filter | Description |
|---|---|
| Custom Data | Custom data filters allow you to segment users based on events and attributes you define. With them, you can use features specific to your product. |
| User Activity | User activity filters allow you to segment customers based on their actions and purchases. |
| Retargeting | Retargeting filters allow you to segment customers who have been sent, received, or interacted with previous Campaigns or Canvases. |
| Marketing Activity | Marketing filters segment customers based on universal behaviors like last engagement or received campaigns. |
| User Attributes | User attribute filters segment customers by their constant attributes and characteristics. |
| Install Attribution | Install attribution filters segment customers by their first source, adgroup, campaign, or ad. |
{: .reset-td-br-1 .reset-td-br-2}

### The "where": Locate my audience

> Where can I reach my audience? 

This is where we determine which messaging channels make the most sense for your user journey. With Canvas, you can use any of the following channels:
* Email
* Push (Android, iOS, Windows, web)
* In-app Messages
* Content Cards
* SMS or MMS
* Webhook

1. **Setting up variants**: A variant is the trail each customer follows on their journey. Canvas supports up to eight variants with a control group. While not required, you can name each variant, as well as control the distribution of the target audience following each variant.

2. **Building steps**: A step is a marketing decision point—what is the experience you’re creating? Within a step, you can set triggers or schedule delivery, refine targeting by adding filters or marking [exception events][1] and add channels from email to push to webhooks.

3. **Determining when and how to use steps & variants:** Each Canvas must have at least one variant and at least one step. The sky's the limit from there—so how do you decide on the shape of your Canvas? That’s where your goals, data, and hypothesis come into play. The “how” and “where” brainstorm will help you map out the right shape and structure of your Canvas. There are a couple approaches you can use:
    - **Work backwards**: Some goals have smaller sub-goals. For instance, if you’re aiming for converting a free user into a subscription, you may need a page with your subscription services outlined. A visitor may need to see the options before they purchase. You may focus your messaging efforts on showing them this page before a checkout page. Working backward to understand the journey a customer must go through to get to your goal is key to guiding them through to conversion.
    - **Start with the status quo and add more**: Have you ran a similar campaign in the past? Or is one currently running? Use that one message and add to it. Try a new filter or add a followup message. Look at your performance and keep optimizing by making incremental changes.
    - **Look to others**: Imitation is the highest form of flattery. Don’t reinvent in the wheel. Don’t worry, we have you covered. At the end of this guide, you’ll find some outlines that can help you get started.


### The "how": Build the complete experience

> How do I build my Canvas journey after identifying the five W's?

The "how" collectively summarizes how you'll create your Canvas and how you'll reach your users with your message. For example, in order for a message to be effective, you should optimize the timing of your messaging with regards to the timezones across your different users.

Answering "how" also determines the cadence for sending a Canvas to your audience (i.e., once a week, biweekly, etc.), and which messaging channels to leverage for each Canvas that you build. 


[1]: {{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/exception_events/
