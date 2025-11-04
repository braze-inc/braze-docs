---
nav_title: Certona
article_title: Certona
alias: /partners/certona/
description: "This reference article outlines the partnership between Braze and Certona, a real-time, omnichannel personalization solution that offers personalization across the customer lifecycle. Use Certona with Braze Connected Content partner to easily insert content recommendations across multichannel campaigns."
page_type: partner
search_tag: Partner

---

# Certona

> Certona's platform drives personalization across the customer lifecycle. From highly individualized email campaigns to machine-learning-powered product recommendations, Certona ensures that you're harnessing the power of personalization.

_This integration is maintained by Certona._

## About the integration

The Braze and Certona integration leverages Certona's machine learning product recommendations in Braze campaigns and Canvases through Connected Content.

## Prerequisites

| Requirement| Description|
| ---| ---|
| [Certona account](https://manage.certona.com/) | A Certona account is required to take advantage of this partnership. |
| [Certona REST API endpoint](https://manage.certona.com/) | This endpoint is used directly in your Braze campaign message to pull recommended content based on user ID. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

Use Certona's REST API to insert personalized content into your messages. This can be done by adding the following Connected Content template into your Braze message composer along with your Certona REST API endpoint.

{% raw %}
```liquid
{% connected_content {CERTONA_REST_API_KEY} :save recommendations %}
```

Next, define the content you would like to call such as relevant text or images. For example, `{{recommendations.CertonaObject.RecommendedItems[0].Items[0].name}}`.

{% endraw %}

![An image of a push campaign with Certona related Connected Content included in the message body.]({% image_buster /assets/img/certona.png %})

Once you put this message into the composer body, preview your Connected Content call to make sure you have displayed the correct information.

![An image showing the "Test" tab, encouraging users to thoroughly test their message before send.]({% image_buster /assets/img/certona2.png %})


