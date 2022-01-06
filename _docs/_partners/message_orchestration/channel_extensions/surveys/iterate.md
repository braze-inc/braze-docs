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

The Braze and Iterate integration lets you include Iterate survey links in your email, push, or in-app messages. These links, once received, can automatically record and attribute Iterate survey responses as Braze custom user attributes, allowing you to create powerful new audiences and segments to use in your campaigns. 

## Prerequisites

| Requirement | Origin |
|---|---|
|Iterate account | A [Iterate account](https://iteratehq.com) is required to take advantage of this partnership. |
| Braze REST API key | A Braze REST API Key with `users.track` permissions. <br><br> This can be created within the __Braze Dashboard -> Developer Console -> REST API Key -> Create New API Key__ |
| Braze REST endpoint  | Your REST Endpoint URL. Your endpoint will depend on the [Braze URL for your instance][6]. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Use cases

With Iterate, you can collect nearly any data type ranging from personal info, performance data, preferences, or user preference. What you ask is entirely up to you and what kind of audiences you're looking to build.

## Integration

### Step 1: Connect Braze with Iterate

Log in to your Iterate account and add your Braze REST endpoint and REST API key to your company settings page.

### Step 2: Create your survey

Create a link survey to send out. Once the questions have been written and you've customized the design, select **Send survey -> Integrations -> Braze**.

You'll then see the configuration options to send responses to Braze.
Toggle on the integration to begin sending responses for that survey into Braze. 

Copy the survey link provided. You will need to include this link in your Braze campaign. Note that the Liquid included in the link {% raw %}`?user_braze_id={{${braze_id}}}`{% endraw %} will automatically be replaced for each user upon send.

### Step 3: Share your survey

Your survey can be shared in two ways: by embedding the first question into your message or including a direct link to the survey on the Iterate platform.

![Iterate link options][2]

- **Embed the code**
  - Copy the code snippet under **Email embed code** into the Braze integration section of the **Send survey** tab. Insert the code into the HTML of your Braze email where you would like the beginning of the survey to appear. 
  - If you are having difficulties rendering the survey questions or if they look incorrectly formatted, you will need to go into the **Sending Info** tab in the message composer and uncheck **Inline CSS**.
- **Include a link**
  - Copy the link under **Survey Link** in the Braze integration section of the **Send survey** tab. 

## Step 4: Target users

As users respond, you'll see the data populate on their profiles in real-time. This data can be used to segment users and send personalized follow-up campaigns. For example, if you sent a question "Do you enjoy our products?", you could create segments of users that have the custom user attribute `Do you enjoy our products?` who responded "Yes" or "No", and target these users.

## Customize user attribute names

By default, the user attribute created for a question is the same as the prompt. 
In some cases, you may want to customize this. To do that, click on the **Customize user attribute names** dropdown in the **Create your Survey** step above and enter any custom names you'd like.

[6]: {{site.baseurl}}/api/basics?redirected=true#endpoints
[2]: {% image_buster /assets/img/iterate.png %}