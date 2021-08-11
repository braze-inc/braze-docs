---
nav_title: Certona
article_title: Certona
alias: /partners/certona/
description: "This article outlines the partnership between Braze and Certona,a real-time, omnichannel personalization solution that offers personalization across the customer lifecycle. Use Certona with Braze's Connected Content partner to easily insert content recommendations across multichannel campaigns."
page_type: partner
search_tag: Partner

---

# About Certona

> Certona's platform drives personalization across the customer lifecycle. From highly individualized email campaigns to machine-learning-powered product recommendations, Certona ensures that you’re harnessing the power of personalization.

Use Certona with Braze's Connected Content partner to easily insert content recommendations across multichannel campaigns.

## Prerequisites

| Requirement| Origin| Access| Description|
| ---| ---| ---|
|Certona Account | Certona | https://manage.certona.com/ | You'll need this account to access other resources and tools needed to incorporate and leverage Certona data with Braze. |
| Certona REST API Endpoint | Certona | https://manage.certona.com/ | This endpoint is used directly in your message (in the Braze Campaign Message Composer) to pull recommended content based on User ID. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Integration

Use Certona's REST API to insert personalized content into your messages. Once you have your Certona account and Certona is integrated into your app, use this template to call content into your messages.

{% raw %}

Paste the following template into your message composer and change out the information as needed.

```
{% connected_content http://res-x.com/ws/r2/resonance.aspx :save recommendations %}
```

Then, write your message as shown below, defining the content you would like to call with json. For example, `{{recommendations.CertonaObject.RecommendedItems[0].Items[0].name}}`.

{% endraw %}


![certona][1]

Once you put this message into the composer body, you can preview your message. You can even pull in images, as seen in the example below:

![certona2][2]

[1]: {% image_buster /assets/img/certona.png %}
[2]: {% image_buster /assets/img/certona2.png %}
