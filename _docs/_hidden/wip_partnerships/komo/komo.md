---
nav_title: Komo
article_title: Komo
page_order: 1
description: "This article outlines the partnership between Braze and Komo, a customer engagement platform specializing in gamification, interactive content, competitions, prizing, and loyalty. Through this integration, first and zero-party data captured in Komo can be published to Braze."
alias: /partners/komo/
page_type: partner
search_tag: Partner
hidden: true

---

# Komo

> [Komo][7] is a customer engagement platform specializing in gamification, interactive content, competitions, prizing, and loyalty.

With the integration of Braze and Komo, you can now gather first and zero-party data through Komo Engagement Hubs. These hubs are dynamic microsites that offer interactive content and gamification features. The user data collected from these hubs are then transmitted to the Braze API.

## What are the benefits?

- Ingest first and zero-party user data gather from Komo to Braze in real-time.
- Ingest market research and user preference data when they answer surveys, polls, and quiz questions.
- Progressively build user profiles in Braze over time as the user continues to engage and share more data about themselves.
- Standardize the look and feel of transactional emails sent through Braze.

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| Komo account | You will need an active Komo account to take advantage of this partnership. Visit [Komo][7] to start a trial now.
| Komo Engagement Hub | You will need to publish a Komo Engagement Hub. |
| Braze REST API key | A Braze REST API key with `users.track` permissions. <br><br> This can be created within the **Braze Dashboard > Developer Console > REST API Key > Create New API Key**. |
| Braze REST endpoint | [Your REST endpoint URL][1]. Your endpoint will depend on the Braze URL for your instance. For example, it should look something like: https://rest.iad-03.braze.com |


## Use cases

{% tabs local %}
{% tab Data Capture (Form Submission) %}

When a user submits a customizable data capture form in Komo, the Komo fields that are mapped in the Braze integration will be passed to Braze via the Track User API call.

Data Capture forms exist either at the start or end of Cards.

{% endtab %}
{% tab Market Research (Coming soon) %}

Coming soon, we will be adding the ability in the integration to pass through market research data captured when a user answers a quiz question, poll, personality test, swiper, etc. This data will enable you to enhance a user's profile beyond data captured in form submissions.

{% endtab %}
{% endtabs %}

## Integration

### Step 1: Publish a Komo Engagement Hub and Card

You will need to publish a Komo Engagement Hub with at least one Card containing a data capture form. Once published, you can test the user experience end-to-end and verify the integration is working correctly.

![][2]

### Step 2: Add the Braze integration

Next, go to the Hub Settings tab inside of the Komo Portal and select the Integrations section on the left:  

![][3]

Then, find the Braze integration from the list, and select the Connect button to enable the integration:  

![][4]

The first thing you will need to configure is how you will map users captured in Komo to users within Braze; if you are capturing the `braze_id` or `external_id` by a field within Komo, then you can select the appropriate key, otherwise, select the most common option will be a user alias of email or phone.

![][5]

Next, you will need to define a map of the Komo fields you want to transfer into Braze attributes. Komo captures a large amount of data, so only the fields mapped in the Braze integration will be sent to Braze.

![][6]

Finally, you will need to add your API key, see prerequisites above, if you need to create one. And your [REST endpoint URL][1].

Lastly, hit save to enable the integration.


[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[2]: {% image_buster /assets/img/komo/komo_hub_publish.png %}
[3]: {% image_buster /assets/img/komo/komo_hub_settings_integrations.png %}
[4]: {% image_buster /assets/img/komo/komo_hub_settings_braze_connect.png %}
[5]: {% image_buster /assets/img/komo/komo_hub_settings_braze_key.png %}
[6]: {% image_buster /assets/img/komo/komo_hub_settings_braze_settings.png %}
[7]: https://komo.tech/
