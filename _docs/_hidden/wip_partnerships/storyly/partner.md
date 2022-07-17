---
nav_title: Storyly
article_title: Storyly | Braze
page_order: 1

description: "Braze & Storyly integration will enable app owners to target their segments and feed Braze with more first party data."
alias: /partners/storyly/

page_type: partner
search_tag: Partner
hidden: true

---

# Storyly

> [Storyly](https://www.storyly.io/) is a lightweight SDK that brings stories to your app or website. With an intuitive design studio, insightful analytics, and seamless connectivity, Storyly is a powerful tool for enriching the audience experience. 

The Braze and Storyly integration allows you to use all your segments in Braze as an audience in Storyly platform. With this integration, you can:
- Target your segments with specific stories
- Use user attributes to personalize your story contents

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| Storyly Account | A Storyly account is required to take advantage of this partnership. |
| Storyly SDK | In addition to the required Braze SDK, you must install the [Storyly SDK](https://integration.storyly.io/) |
| Braze REST API key | A Braze REST API key with the following permissions <br><br> `users.export.ids`<br> `users.export.segments`<br> `segments.list`<br> `segments.details` <br><br> This can be created within the **Braze Dashboard > Developer Console > REST API Key > Create New API Key**. |
| Braze REST endpoint | [Your REST endpoint URL][1]. Your endpoint will depend on the Braze URL for your instance. |
{: .reset-td-br-1 .reset-td-br-2}

## Use cases

With the Braze and Storyly integration, app owners can show stories to all segments in Braze and personalize the stories with user attributes.

#### Case 1: Targeting Braze segments in Storyly
After the integration finished, you will be able to create **Audience** based on your Braze segments. This could be demographic or behavioral segment. Users who lives in specific location, users who took a specific action on your app, users who are interested in specific products could be targeted and you can offer them specific stories to increase conversion.

#### Case 2: Personalized stories with user attributes
User attributes on Braze are also usable to generate dynamic stories on Storyly. This could be name, products on the basket or even favorited products. Every end-user will see a unique personalized story. Personalization is helpful to increase conversion rates on stories and the overall story engagement rate.


## Integration

Braze Storyly integration is explained in the following [video](https://www.youtube.com/watch?v=3-OEqQs48Zw).
<br>You can also check [Storyly](https://help.storyly.io/en/articles/6354805-connect-your-braze-audiences-with-storyly) documentation. 

{% alert important %}
Please be sure that your Storyly integration holds **custom parameter**. It will be matched with Braze **external id** user property. <br>Custom parameter implementation is explained here for [iOS](https://integration.storyly.io/ios/personalization-customaudience.html), [android](https://integration.storyly.io/android/personalization-customaudience.html), [react native](https://integration.storyly.io/react-native/personalization-customaudience.html), [flutter](https://integration.storyly.io/flutter/personalization-customaudience.html) and [web](https://integration.storyly.io/web/personalization-customaudience.html) .
{% endalert %}

### Step 1: Set the integration on Storyly Dashboard

This can be created within the **Storyly Dashboard > Settings > Integrations > Connect with Braze**. 
<br>You will need your Braze REST API Key and Braze REST endpoint. 

### Step 2: Get your segments 

You can use Braze segments to create Storyly Audience. This can be created within the **Storyly Dashboard > Settings > Audiences > New Audience > Create Audience with Braze**.
There will be two options:
- One-time sync
- Daily sync<br>For the specific campaign stories you should select **One-time sync**, for the long term stories you should select **Daily sync**.


[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints