---
nav_title: Iterate
article_title: Iterate
alias: /partners/iterate/
description: "This article outlines the partnership between Braze and Iterate allowing you to enrich customer data by using surveys to add additional insights."
page_type: partner
search_tag: Partner

---

# Iterate

> [iterate](https://iteratehq.com) makes it easy to learn from your customers, offering smart, user-friendly research tools that look and feel like your brand.

Iterate integrates with Braze by recording survey responses as custom user attributes in Braze allowing you to create powerful new audiences and segments.

## Requirements

to connect braze with iterate you'll need the following three items:

| Requirement | Origin | Description |
|---|---|---|
| Braze API Key | Braze | You will need to create a new API Key.<br><br>This can be created in the __Developer Console -> API Settings -> Create New API Key__ with __users.track__ permissions.
| [Braze REST Endpoint][6] | Braze | Your REST Endpoint URL. Your endpoint will depend on the Braze URL for your instance. |
| Iterate Account | Iterate | You will need to have a Iterate account. Visit their [website](https://iteratehq.com/) to get started. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Integration details

Fill in gaps and enrich your customer data by sending out a link to your Iterate survey via any channel in Braze: email, push, or in-app message. The link will include the user's Braze id, which will be used to identify that user. When they fill out the survey the responses to each question will be set as a custom user attribute. 

### Step 1: connect braze with iterate

Log in to your Iterate account and add both your **Braze REST Endpoint** and **API key with the `users.track`** permission to your company settings page.

### Step 2: create your survey

Create the link survey you'll be sending out. Once the questions have been written and you've customized the design, go to *Send survey* and select *Integrations*, then *Braze*. You'll then see the configuration options to send responses to Braze.

Toggle on the integration to begin sending responses for that survey into Braze. Copy the survey link listed, this is what you'll include in your campaign. Note the {% raw %}`?user_braze_id={{${braze_id}}}`{% endraw %} which Braze will automatically replace with the correct Braze id of the user you're sending to in the campaign.

### Step 3: share your survey

Next, simply start your campaign including that link and as users respond you'll see the data populate on their profiles in real-time.

## Customize user attribute names

By default, the user attribute created for a question is the same as it's prompt. For example, a question with the prompt: "Overall, how satisfied are you with Iterate?" will be added as the user attribute `Overall, how satisfied are you with Iterate?` in Braze. In some cases you may want to customize that, to do that, click on the *Customize user attribute names* dropdown in the **Create your Survey** step above and enter any custom names you'd like.

## Use cases

With Iterate you can collect nearly any type of data. Ranging from personal info (name, age, email), performance data (NPS, Customer Satisfaction, star ratings), preferences (preferred device, preferred frequency of communication), or personality (favorite book, dog or cat person). What you ask is entirely up to you and what kind of audiences you're looking to build.

[6]: {{site.baseurl}}/api/basics?redirected=true#endpoints
