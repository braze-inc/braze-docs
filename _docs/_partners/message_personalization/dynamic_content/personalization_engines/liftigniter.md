---
nav_title: Liftigniter
article_title: LiftIgniter
alias: /partners/liftigniter/
description: "This reference article outlines the partnership between Braze and LiftIgniter, a leading personalization platform, helping enterprises transform their customer experiences."
page_type: partner
search_tag: Partner

---

# Liftigniter

> LiftIgniter is a leading personalization platform helping enterprises transform their customer experiences through real-time personalization across every touchpoint.

_This integration is maintained by Liftigniter._

## About the integration

The LiftIgniter and Braze integration leverage Connected Content to allow you to recommend interesting topics such as news articles, clothing, and other retail items and videos.

## Prerequisites

| Requirement| Description|
| ---| ---|
| LiftIgniter account | A [LiftIgniter account](https://console.liftigniter.com/login) is required to take advantage of this partnership. |
| LiftIgniter API integration | You must [integrate](https://support.liftigniter.com/support/solutions/articles/30000024667-api-integration-overview) LiftIgniter into your site or app to be able to pull recommendations from there. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Integration

Use [LiftIgniter's REST API](https://documenter.getpostman.com/view/2166502/liftigniter/7TFGvSV#9bdf75da-edd6-45ec-9c28-a0edefad1389) to insert personalized content into your messages. After you have your LiftIgniter account and LiftIgniter is integrated into your app, add the following template into your message composer to call content into your messages, replacing information as needed (`x-api-key`, `theapikey`, etc.).

{% raw %}
```
{% connected_content https://query.petametrics.com/v3/lkdk9usg5av95fvs/userId/model :method post :headers {"x-api-key": "theapikey"} :body "UseActivity"=false :content_type application/json :save json %}
```

Next, write your message, defining the content you would like to call with JSON. For example, `{{json.items[0].title}}`.

{% endraw %}

![An image showing a push campaign that includes LiftIgniter specific Connected Content calls. There is also Connected Content logic added to the image field.]({% image_buster /assets/img/liftigniter.png %})

Once you put this message into the composer body, you can preview your message. You can even pull in images, shown in the following example:

![A preview image of what the message will look like after it's sent.]({% image_buster /assets/img/liftigniter2.png %})


