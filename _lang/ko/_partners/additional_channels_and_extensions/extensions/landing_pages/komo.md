---
nav_title: Komo
article_title: Komo
description: "This reference article outlines the partnership between Braze and Komo, a customer engagement platform specializing in gamification, interactive content, competitions, prizing, and loyalty. Through this integration, first and zero-party data captured in Komo can be published to Braze."
alias: /partners/komo/
page_type: partner
search_tag: Partner

---

# Komo

> [Komo](https://komo.tech/) is a customer engagement platform specializing in gamification, interactive content, competitions, prizing, and loyalty.

_This integration is maintained by Komo._

## About the integration

The Braze and Komo integration allows you to gather first and zero-party data through Komo Engagement Hubs. These hubs are dynamic microsites that offer interactive content and gamification features. The user data collected from these hubs are then transmitted to the Braze API.

- Ingest first and zero-party user data gather from Komo to Braze in real-time
- Ingest market research and user preference data when they answer surveys, polls, and quiz questions
- Progressively build user profiles in Braze over time as the user continues to engage and share more data about themselves
- Standardize the look and feel of transactional emails sent through Braze

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| Komo account | You will need an active Komo account to take advantage of this partnership. Visit [Komo](https://komo.tech/) to start a trial now. |
| Braze REST API key | A Braze REST API key with `users.track` permissions. <br><br> This can be created in the Braze dashboard from **Settings** > **API Keys**. |
| Braze REST endpoint | [Your REST endpoint URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Your endpoint will depend on the Braze URL for your instance.<br><br>For example, it should look something like: https://rest.iad-03.braze.com |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Use cases

{% tabs local %}
{% tab Data Capture - Form Submission %}

When a user submits a customizable data capture form in Komo, the Komo fields mapped in the Braze integration will be passed to Braze via the `/users/track/` API call.

Data capture forms exist either at the start or end of Cards.

{% endtab %}
{% tab Market Research - Coming soon %}

Coming soon, Komo will be adding the ability to pass through market research data captured when a user answers a quiz question, poll, personality test, swiper, etc. This data will enable you to enhance a user's profile beyond data captured in form submissions.

{% endtab %}
{% endtabs %}

## Integration

### Step 1: Publish a Komo Engagement Hub and card

You will need to publish a Komo Engagement Hub with at least one card containing a data capture form. When published, you can test the user experience end-to-end and verify the integration is working correctly.

![]({% image_buster /assets/img/komo/komo_hub_publish.png %})

### Step 2: Add the Braze integration

In Komo, go to the **Hub Settings** tab, and select the **Integrations** section. Next, find the Braze integration from the list, and select the **Connect** button to enable the integration.

![]({% image_buster /assets/img/komo/komo_hub_settings_integrations.png %})

![]({% image_buster /assets/img/komo/komo_hub_settings_braze_connect.png %})

#### Configure user mapping

The first thing you will need to configure is how you will map users captured in Komo to users within Braze. If you are capturing the `braze_id` or `external_id` by a field within Komo, then you can select the appropriate key; otherwise, select the most common option will be a user alias of email or phone.

![]({% image_buster /assets/img/komo/komo_hub_settings_braze_key.png %}){: style="max-width:65%;"}

Next, you will need to define a map of the Komo fields you want to transfer into Braze attributes. Komo captures a large amount of data, so only the fields mapped in the Braze integration will be sent to Braze.

![]({% image_buster /assets/img/komo/komo_hub_settings_braze_settings.png %}){: style="max-width:65%;"}

Finally, add your API key and REST endpoint URL and click **Save** to enable the integration.

## Using the integration

Once your integration has been completed, you can use the Komo data sent to Braze to create segments for targeting.


