---
nav_title: Iterate
alias: /partners/iterate/
description: "This article outlines the partnership between Braze and Iterate allowing you to enrich customer data by using surveys to add additional insights."
page_type: partner
---

# Iterate

> [Iterate](https://iteratehq.com) makes it easy to learn from your customers, offering smart, user-friendly research tools that look and feel like your brand.

Iterate integrates with Braze by recording survey responses as custom user attributes in Braze allowing you to create powerful new audiences and segments.

## Requirements

To connect Braze with Iterate you'll need the following two items:

| Requirement | Origin | Access | Description |
|---|---|---|---|
|Braze App Group REST API Key | Braze platform | Manage App Group > App Settings Page | An API key with the `users.track` permission. |
|Braze API Endpoint | Braze platform | Check out our [listed endpoints]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints) or open a support ticket. | Your cluster REST endpoint. |

## Integration Details

Fill in gaps and enrich your customer data by sending out a link to your Iterate survey via any channel in Braze: email, push, or in-app message. The link will include the user's braze id, which will be used to identify that user. When they fill out the survey the responses to each question will be set as a custom user attribute.

### Step 1: Connect Braze with Iterate

Log in to your Iterate account and add both your **cluster REST endpoint** and **API key with the `users.track`** permission to your company settings page.

### Step 2: Create your Survey

Create the link survey you'll be sending out. Once the questions have been written and you've customized the design, go to *Send survey* and select *Integrations*, then *Braze*. You'll then see the configuration options to send responses to Braze.

Toggle on the integration to begin sending responses for that survey into Braze. Copy the survey link listed, this is what you'll include in your campaign. Note the `?user_braze_id={{${braze_id}}}` which Braze will automatically replace with the correct braze id of the user you're sending to in the campaign.

### Step 3: Share your Survey

Next, simply start your campaign including that link and as users respond you'll see the data populate on their profiles in real-time.

## Customize User Attribute Names

By default, the user attribute created for a question is the same as it's prompt. For example a question with the prompt: "Overall, how satisfied are you with Iterate?" will be added as the user attribute `Overall, how satisfied are you with Iterate?` in Braze. In some cases you may want to customize that, to do that click on the *Customize user attribute names* dropdown in the **Create your Survey** step above and enter any custom names you'd like.

## Use Cases

With Iterate you can collect nearly any type of data. Ranging from personal info (name, age, email), performance data (NPS, Customer Satisfaction, star ratings), preferences (preferred device, preferred frequency of communication), or personality (favorite book, dog or cat person). What you ask is entirely up to you and what kind of audiences you're looking to build.
