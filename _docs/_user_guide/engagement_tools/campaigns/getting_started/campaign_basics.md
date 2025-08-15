---
nav_title: Campaign basics
article_title: Campaign Basics
page_order: 1
page_type: reference
description: "This reference article covers the basics of campaigns, covering various questions you should ask yourself as you set up your first campaigns."
tool: Campaigns

---

# Campaigns basics

> This reference article covers the basics of campaigns, covering various questions you should ask yourself as you set up your first campaigns.

## Understanding campaign structure

Before getting started with the finer details of setting up campaigns, let's identify the key details for understanding how campaigns work across different messaging channels.

Campaigns are a single message step to connect to your users on channels, or more commonly referred to as messaging channels. These messaging channels include Content Cards, email, in-app messages, push, SMS and MMS, and webhooks. By understanding where your customers reside, you can leverage the appropriate messaging channels to communicate.

## Building the customer journey

Because campaigns can be built uniquely depending on the messaging channel, you can use these five W's of visualization to help identify and conceptualize your customer engagement strategies and goals.

### The "what": Name your campaign

> What are you trying to help the user do or understand?

Never underestimate the power of the name. Braze is built for collaboration, so this is an excellent time to get grounded in how you'll communicate goals with your team. For more on customer journeys, check out our [Mapping User Lifecycles](https://learning.braze.com/mapping-customer-lifecycles) Braze Learning course!

### The "when": Create starting conditions

> When will a customer encounter this campaign? 

Users can enter your campaign in three ways: at a set date and time (scheduled), when they perform a specific action (action-based), or when they do something that triggers an API call (API-triggered). 

Scheduled delivery involves adjusting your campaigns to send at a specific time, and optionally, for a specified cadence. Action-based campaigns respond to specific customer behaviors as they happen in real-time. This can include making a purchase or interacting with another campaign. API-triggered campaigns can be set up to determine key customer actions on your platform that, when achieved, will trigger an API call to Braze and send your campaigns.

### The "who": Select an entry audience

> Who are you trying to reach? 

You can use pre-defined [segments]({{site.baseurl}}/user_guide/engagement_tools/segments) to target users based on their demographic, behavioral, or technical characteristics and actions. Add more filters when building your campaign to tailor your segment further. Only the users who match these target audience criteria can enter the journey. Check out this table for a quick summary of the available filter types.

| Filter | Description |
|---|---|
| Custom Data | Segment users based on events and attributes you define. Can use features specific to your product. |
| User Activity | Segment customers based on their actions and purchases. |
| Retargeting | Segment customers who have been sent, received, or interacted with previous campaigns. |
| Marketing Activity | Segment customers based on universal behaviors like last engagement or received campaigns. |
| User Attributes | Segment customers by their constant attributes and characteristics. |
| Install Attribution | Segment customers by their first source, ad group, campaign, or ad. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### The "why": Identify conversion events

> Why are you building this campaign? 

It's always important to have a defined goal in mind, and campaigns help you understand how you perform against KPIs like session engagement, purchases, and custom events. Selecting at least one [conversion event]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/) will give you the ability to understand your campaign performance.

### The "where": Find my audience

> Where can I best reach my audience?

This is where we determine which messaging channels make the most sense for your user journey. Ideally, you'd want to reach your users where they're most active.

### The "how": Build the experience

> How do I build my campaign after identifying the five W's?

Consider setting up variants and A/B testing as you become more savvy with campaign building. Note that campaigns support up to eight variants with a control group. Use your campaign analytics to make informed choices as you build your campaign, adjusting anything from your segmented audience to your actual messaging content.

