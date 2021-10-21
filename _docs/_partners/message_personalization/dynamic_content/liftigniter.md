---
nav_title: Liftigniter
article_title: Liftigniter
alias: /partners/liftigniter/
description: "This article outlines the partnership between Braze and LiftIgniter, a leading personalization platform helping enterprises transform their customer experiences."
page_type: partner
search_tag: Partner

---

# About liftigniter

> LiftIgniter is a leading personalization platform helping enterprises transform their customer experiences through real-time personalization across every touch point.

Use Liftigniter with Braze’s Connected Content to allow brands to recommend interesting topics such as news articles, clothing and other retail items, and videos.

## Prerequisites

| requirement| origin| access| description|
| ---| ---| ---|
|Liftigniter Account | Liftigniter | https://console.liftigniter.com/login | You'll need this account to access other resources and tools needed to incorporate and leverage Liftigniter data with Braze. |
| Liftigniter API Integration | Liftigniter| https://support.liftigniter.com/support/solutions/articles/30000024667-api-integration-overview | You must integrate Liftigniter into your site or app to be able to pull recommendations from there. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Integration

use [liftigniter's rest api](https://documenter.getpostman.com/view/2166502/liftigniter/7tfgvsv#9bdf75da-edd6-45ec-9c28-a0edefad1389) to insert personalized content into your messages. once you have your liftigniter account and liftigniter is integrated into your app, use this template to call content into your messages. feel free to reach out to liftigniter's support team with any questions.

{% raw %}

Paste the following template into your message composer and change out the information as needed (`x-api-key`, `theapikey`, etc.).

```
{% connected_content https://query.petametrics.com/v3/lkdk9usg5av95fvs/userId/model :method post :headers {“x-api-key”: “theapikey”} :body “UseActivity”=false :content_type application/json :save json %}
```

Then, write your message as shown below, defining the content you would like to call with json. For example, `{{json.items[0].title}}`.

{% endraw %}

![liftigniter][1]

Once you put this message into the composer body, you can preview your message. You can even pull in images, as seen in the example below:

![liftigniter][2]

[1]: {% image_buster /assets/img/liftigniter.png %}
[2]: {% image_buster /assets/img/liftigniter2.png %}
