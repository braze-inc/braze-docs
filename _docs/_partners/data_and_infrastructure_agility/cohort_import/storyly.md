---
nav_title: Storyly
article_title: Storyly
description: "The Braze and Storyly integration enables app owners to target their segments and feed Braze with more first-party data."
alias: /partners/storyly/
page_type: partner
search_tag: Partner

---

# Storyly

> [Storyly](https://www.storyly.io/) is a lightweight SDK that brings stories to your app or website. With an intuitive design studio, insightful analytics, and seamless connectivity, Storyly is a powerful tool for enriching the audience experience. 

The Braze and Storyly integration allows you to use your segments in Braze as an audience in the Storyly platform. With this integration, you can:
- Target your segments with specific stories
- Use user attributes to personalize your story contents

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| Storyly account | A Storyly account is required to take advantage of this partnership. |
| Storyly SDK | In addition to the required Braze SDK, you must install the [Storyly SDK](https://integration.storyly.io/). |
| Braze REST API key | A Braze REST API key with the following permissions <br><br> `users.export.ids`<br> `users.export.segments`<br> `segments.list`<br> `segments.details` <br><br> This can be created within the **Braze Dashboard > Developer Console > REST API Key > Create New API Key**. |
| Braze REST endpoint | [Your REST endpoint URL][1]. Your endpoint will depend on the Braze URL for your instance. |
{: .reset-td-br-1 .reset-td-br-2}

## Use cases

With the Braze and Storyly integration, app owners can show stories to all segments in Braze and personalize the stories with user attributes.

Some common use cases include:

__Target Braze segments in Storyly__<br>After the integration is finished, you can create an Storyly audience based on your Braze segments. This could be a demographic or behavioral segment. For example, target users who live in a specific location, those who take a specific action on your app, or those interested in specific products with specific stories to increase conversion.<br>
__Personalized stories with user attributes__<br>Braze user attributes are also usable in Storyly to generate dynamic stories. This could include a user's name, products in a basket, or even favorited products, providing end users unique personalized stories. Personalization helps increase conversion rates on stories and the overall story engagement rate.

## Data export integration

The Braze Storyly integration is explained in the following video:

{% include video.html id="3-OEqQs48Zw" source="youtube" %}

Make sure that your Storyly integration holds custom parameters. These paramters will be matched to the Braze `external id` user property. Custom parameter implementation is explained here for [iOS](https://integration.storyly.io/ios/personalization-customaudience.html), [Android](https://integration.storyly.io/android/personalization-customaudience.html), [React Native](https://integration.storyly.io/react-native/personalization-customaudience.html), [Flutter](https://integration.storyly.io/flutter/personalization-customaudience.html), and [Web](https://integration.storyly.io/web/personalization-customaudience.html) .

You can also refer to the [Storyly](https://help.storyly.io/en/articles/6354805-connect-your-braze-audiences-with-storyly) documentation for more information.

### Step 1: Set the integration on Storyly dashboard

An integration be created within the **Storyly Dashboard > Settings > Integrations > Connect with Braze**. Here, you will need your Braze REST API key and Braze REST endpoint. 

### Step 2: Get your segments 

Next, you can use Braze segments to create a Storyly audience. This can be created within the **Storyly Dashboard > Settings > Audiences > New Audience > Create Audience with Braze**.

Here, there will be two syncing options. Select **One-time sync** for specific campaign stories, or **Daily Sync** for long-term stories.

[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints