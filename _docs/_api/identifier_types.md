---
nav_title: "API Identifier Types"
article_title: API Identifier Types
page_order: 2.2
description: "This reference article covers the different types of API Identifiers that exist in the Braze dashboard, where you can find them, and what they are used for." 
page_type: reference

---

# API Identifier Types

> This reference guide touches on the different types of API Identifiers that can be found within the Braze dashboard, their purpose, where you can find them, and how they are typically used. For information on REST API Keys or App Group API Keys, refer to the [Rest API Key Overview]({{site.baseurl}}/api/api_key/)

The following API Identifiers can be used to access your template, canvas, campaign, segment, send  or card from Braze's external API. All messages should follow [UTF-8][1] encoding.

{% tabs %}
{% tab Template Ids %}

## Template API Identifier

A [Template]({{site.baseurl}}/api/endpoints/templates/) API Identifier or Template ID is an out-of-the-box key by Braze for a given template within the dashboard. Template IDs are unique for each template and can be used to reference templates through the API. 

Templates are great for if your company contracts out your HTML designs for campaigns. Once the templates have been built, you now have a template that is not specific to a campaign but can be applied to a series of campaigns like a newsletter.

### Where can I find it?
You can find your Template ID one of two ways:

1. In the dashboard, open up "Templates & Media" under "Engagement" and select a pre-existing template. If the template you want does not exist yet, create one and save it. At the bottom of the individual template page, you will be able to find your Template API Identifier.<br><br>
2. Braze offers an "Additional API Identifiers" search, here you can quickly look up specific identifiers. It can be found at the bottom of the "API settings" within the "Developer Console" page.

### What can it be used for?

- Update templates over API
- Grab information on a specific template

<br>
{% endtab %}
{% tab Canvas IDs %}

## Canvas API Identifier

A [Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/) API Identifier or Canvas ID is an out-of-the-box key by Braze for a given Canvas within the dashboard. Canvas IDs are unique to each Canvas and can be used to reference Canvases through the API. 

Note that if you have a Canvas that has variants, there exists an overall Canvas ID as well as individual variant Canvas IDs nested under the main Canvas. 

### Where can I find it?
You can find your Canvas ID one of two ways:

1. In the dashboard, open up "Canvas" under "Engagement" and select a pre-existing Canvas. If the Canvas you want does not exist yet, create one and save it. At the bottom of an individual Canvas page, you will find an "Analyze Variants" button, upon clicking it, a window will appear with the Canvas API Identifier located at the bottom. <br><br>
2. Braze offers an "Additional API Identifiers" search, here you can quickly look up specific identifiers. It can be found at the bottom of the "API settings" within the "Developer Console" page.

### What can it be used for?
- Track analytics on a specific message
- Grab high-level aggregate stats on Canvas performance
- Grab details on a specific Canvas
- With Currents to bring in user-level data for a "bigger picture" approach to canvases
- With API trigger delivery in order to collect statistics for transactional messages

<br>
{% endtab %}
{% tab Campaign IDs %}

## Campaign API Identifier

A [Campaign]({{site.baseurl}}/user_guide/engagement_tools/campaigns/) API Identifier or campaign ID is an out-of-the-box key by Braze for a given campaign within the dashboard. Campaign IDs are unique to each campaign and can be used to reference campaigns through the API. 

Note that if you have a campaign that has variants, there is both an overall campaign ID as well as individual variant campaign IDs nested under the main campaign. 

### Where can I find it?
You can find your campaign ID one of two ways:

1. In the dashboard, open up **Campaigns** under **Engagement** and select a pre-existing campaign. If the campaign you want does not exist yet, create one and save it. At the bottom of the individual campaign page, you will be able to find your **Campaign API Identifier**.<br><br>
2. Braze offers an **Additional API Identifiers** search, here you can quickly look up specific identifiers. You can find this at the bottom of the **API Settings** tab in the **Developer Console**.

### What can it be used for?
- Track analytics on a specific message
- Grab high-level aggregate stats on campaign performance
- Grab details on a specific campaign
- With Currents to bring in user-level data for a "bigger picture" approach to campaigns
- With API trigger delivery in order to collect statistics for transactional messages

<br>
{% endtab %}
{% tab Segment IDs %}

## Segment API Identifier

A [Segment]({{site.baseurl}}/user_guide/engagement_tools/segments/) API Identifier or Segment ID is an out-of-the-box key by Braze for a given Segment within the dashboard. Segment IDs are unique to each segment and can be used to reference segments through the API. 

### Where can I find it?
You can find your Segment ID one of two ways:

1. In the dashboard, open up "Segments" under "Engagement" and select a pre-existing segment. If the Segment you want does not exist yet, create one and save it. At the bottom of the individual segment page, you will be able to find your Segment API Identifier. <br><br>
2. Braze offers an "Additional API Identifiers" search, here you can quickly look up specific identifiers. It can be found at the bottom of the "API settings" within the "Developer Console" page.

### What can it be used for?
- Get details on a specific segment
- Retrieve analytics of a specific segment
- Pull how many times a custom event was recorded for a particular segment
- Specify and send a campaign to a members of a segment from within the API

{% endtab %}
{% tab Card IDs %}

## Card API Identifier

A Card API Identifier or Card ID is an out-of-the-box key by Braze for a given News Feed Card within the dashboard. Card IDs are unique to each [News Feed]({{site.baseurl}}/user_guide/engagement_tools/news_feed/) Card and can be used to reference Cards through the API. 

### Where can I find it?
You can find your Card ID one of two ways:

1. In the dashboard, open up "News Feed" under "Engagement" and select a pre-existing News Feed. If the News Feed you want does not exist yet, create one and save it. At the bottom of the individual News Feed page, you will be able to find your unique Card API Identifier. <br><br>
2. Braze offers an "Additional API Identifiers" search, here you can quickly look up specific identifiers. It can be found at the bottom of the "API settings" within the "Developer Console" page.

### What can it be used for?
- Retrieve relevant information on a card
- Track events related to Content Cards and engagement

<br>
{% endtab %}
{% tab Send IDs %}

## Send Identifier

A Send Identifier or Send ID is a key either generated by Braze or created by you for a given message send under which the analytics should be tracked. The send identifier allows you to pull back analytics for a specific instance of a campaign send via the [`sends/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics/) endpoint.

### Where can I find it?

API and API trigger campaigns that are sent as a broadcast will automatically generate a send identifier if a send identifier is not provided. If you want to specify your own send identifier, you will have to first create one via the [`sends/id/create`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_create_send_ids/) endpoint. The identifier must be all ASCII characters and at most 64 characters long. You can reuse a send identifier across multiple sends of the same campaign if you want to group analytics of those sends together.

### What can it be used for?
- Send and track message performance programmatically, without campaign creation for each send.

<br>
{% endtab %}
{% endtabs %}

[1]: https://en.wikipedia.org/wiki/UTF-8
