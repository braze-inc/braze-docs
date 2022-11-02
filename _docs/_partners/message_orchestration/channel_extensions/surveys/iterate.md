---
nav_title: Iterate
article_title: Iterate
alias: /partners/iterate/
description: "This article outlines the partnership between Braze and Iterate, allowing you to enrich customer data by using surveys to add additional insights."
page_type: partner
search_tag: Partner

---

# Iterate

> [Iterate](https://iteratehq.com) makes it easy to learn from your customers, offering smart, user-friendly research tools that look and feel like your brand.

Iterate's integration with Braze allows you to deliver Iterate surveys natively and seamlessly within your product or campaigns. Survey responses can be recorded as custom user attributes in Braze allowing you to build a complete picture of your users, or create powerful new audiences and segments.

With the Braze SDK installed in your app or website, you can use the segmentation and targeting tools available in Braze to deliver surveys via in-app messages to a specific portion of your audience, based on any trigger or custom segment. 
Iterate surveys can also be embedded directly into your email campaigns, or included as links in your push or other campaign types.

## Prerequisites

| Requirement | Origin |
|---|---|
|Iterate account | A [Iterate account](https://iteratehq.com) is required to take advantage of this partnership. |
| Braze REST API key | A Braze REST API key with `users.track` permissions. <br><br> This can be created within the **Braze Dashboard > Developer Console > REST API Key > Create New API Key**. <br><br> To send surveys via Braze In-App Messages, you'll also need the `kpi.mau.data_series` permission.|
| Braze REST endpoint  | Your REST endpoint URL. Your endpoint will depend on the [Braze URL for your instance][6]. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Use cases

With Iterate you can collect nearly any type of data. Ranging from personal info (name, age, email), performance data (NPS, Customer Satisfaction, star ratings), preferences (preferred device, preferred frequency of communication), or personality (favorite book, dog, or cat person). What you ask is entirely up to you and what kind of data you are looking to collect, or audiences you're looking to build.

## Integration

### Getting started: Connect Braze with Iterate

Log in to your Iterate account and add your Braze REST endpoint and REST API key to your company settings page.

### Deliver surveys as an in-app message

#### 1. Create your survey

Turn on the toggle within your Iterate Settings to enable in-app message surveys.

Create a new survey in Iterate. For the survey type, choose "Send via Braze In-App Message". Add questions, and if appropriate a prompt message to be shown before the survey.

#### 2. Deliver your survey

In the "Publish" tab for your survey, copy the code snippet under "Copy and paste your embed code".

Create a new In-App Messaging campaign in Braze. In the "Message Type" menu, select "Custom Code". Scroll down to the Compose area, and paste the code into the HTML input.

In the "On-click Behavior" menu, select "Wait for User to Dismiss"

Continue setting up your campaign as you would any other in-app messaging campaign, choosing a delivery method and targeting an audience.

### Deliver surveys via email or link/push

#### 1. Create your survey

Create an email/link survey type within Iterate. Once the questions have been written and you've customized the design, select **Send survey > Integrations > Braze**.

You'll then see the configuration options to send responses to Braze. Toggle on the integration to enable sending responses for that survey into Braze. 

#### 2. Share your survey

Your survey can be shared in two ways: by embedding the first question into your message or including a direct link to the survey on the Iterate platform.

![Iterate link options][2]

- **Embed the code**
  - Copy the code snippet under **Email embed code** within the Braze integration section of the **Send survey** tab. Insert the code into the HTML of your Braze email where you would like the beginning of the survey to appear. 
  - If you are having difficulties rendering the survey questions or if they look incorrectly formatted, you will need to go into the **Sending Info** tab in the message composer and uncheck **Inline CSS**.
- **Include a link**
  - Copy the link under **Survey Link** in the Braze integration section of the **Send survey** tab. Note that the Liquid included in the link {% raw %}`?user_braze_id={{${braze_id}}}`{% endraw %} will automatically be replaced for each user upon send.

### Braze custom events

Each time a respondent answers a survey question Iterate triggers a custom event within Braze named survey-question-response. Custom events allow you to trigger any number and type of follow-up campaigns.

### Customize user attribute names

By default, the user attribute created for a question is the same as the prompt. 
In some cases, you may want to customize this. To do that, click on the **Customize user attribute names** dropdown in the **Create your Survey** step and enter any custom names you'd like.

### Next steps: Build follow-up campaigns

As users respond, you'll see the data populate on their profiles in real-time. This data can be used to segment users and send personalized follow-up campaigns. For example, if you sent a question "Do you enjoy our products?", you could create segments of users that have the custom user attribute `Do you enjoy our products?` who responded "Yes" or "No", and target these users.

[6]: {{site.baseurl}}/api/basics?redirected=true#endpoints
[2]: {% image_buster /assets/img/iterate.png %}
