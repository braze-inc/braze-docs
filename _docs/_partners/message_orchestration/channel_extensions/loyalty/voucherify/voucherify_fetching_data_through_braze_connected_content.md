---
nav_title: Fetching data through Connected Content
article_title: Fetching data through Connected Content
page_order: 2
alias: /partners/voucherify/connected_content/
description: "This article outlines how you can fetch data from Voucherify API through Braze Connected Content and send messages to specific Braze segments."
page_type: partner
search_tag: Partner
---

# Fetching data through Connected Content

> With Braze Connected content you can fetch data from Voucherify API and send messages to specific Braze segments. In this tutorial, you’ll see how to set up connected content scripts to publish Voucherify coupons, invite new referrers, retrieve loyalty cards balance and more.

## Contents

- [How does it work?](#how-does-it-work)
- [Security](#security)  

    - [Rate limiter](#security)
    - [Cache](#security)
    - [Retry](#security)
    - [Unique publications](#security)
    - [Join once](#security)  

- [Examples](#examples)  

    - [Publish coupon code](#publish-and-send-unique-coupon-code)
    - [Invite new referrers](#invite-new-referrers)
    - [Fetch loyalty card balance](#fetch-loyalty-card-balance)
    - [Create custom code](#create-custom-code) 

- [Displaying fetched data in Braze messages](#display-fetched-data-in-braze-messages)

---

## How does it work?

The very basic schema of the script looks as follows:

![Script overview]({% image_buster /assets/img/voucherify/voucherify_cc_script_overview.png %})

---

## Security

Note that without the following settings each time a connected content message is triggered, it calls the Voucherify API at least two times.

The following settings reduce the number of API calls invoiced by Braze and cut the risk of hitting the hard-blocking API limit that may break the message delivery.

{% tabs %}
{% tab Rate Limiter %}

#### Rate Limiter

First, [limit the number of messages]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#delivery-speed-rate-limiting) sent by Braze per minute. This secures both Braze and Voucherify APIs against hitting too much traffic from your campaign. When targeting users during campaign setup, choose to limit the sending rate to 500 messages per minute.

![Braze rate limiter]({% image_buster /assets/img/voucherify/voucherify_cc_limiter.png %})

{% endtab %}
{% tab Caching %}

#### Add caching to POST calls

{% alert tip %}
All examples of Connected Content in this tutorial include default caching to reduce the number of API calls triggered by Braze. Note that removing cache from your script will double the number of Voucherify API calls used by Connected Content.
{% endalert %}

Connected Content calls made via HTTP POST don’t cache by default and will make two API requests per each published code. This behavior can drain your hourly and monthly limits. The caching mechanism will allow you to limit that to one API call per voucher publication. To add caching to POST calls, you must perform two steps:

- Add a {% raw %}`:cache_max_age`{% endraw %} attribute. By default, the caching duration is 5 minutes. You can customize the duration using seconds. It can be set between 5 minutes to 4 hours. Example: {% raw %}`:cache_max_age 3600`{% endraw %} will cache for 1 hour.
- Provide a caching key {% raw %}`cache_id={{cache_id}}`{% endraw %} in the destination endpoint query parameter so Braze can identify a unique publication. First, define the variable and then append the unique query string to your endpoint. This will differentiate each publication by the {% raw %}`source_id`{% endraw %}.

![Add caching to braze email template]({% image_buster /assets/img/voucherify/voucherify_cc_cache.png %})

_Note the consequences:_ Braze caches the API calls based on the URL. The unique string used as a query parameter is ignored by Voucherify, but it distinguishes different API requests for Braze and allows to cache each unique attempt separately. Without that query parameter, every customer will receive the same coupon code for the cache duration.

{% endtab %}
{% tab Retry attribute %}

#### Retry attribute

Connected Content does not validate the Voucherify response, so we additionally recommend adding a [retry]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/connected_content_retries) attribute in the Connected Content script. The connected content logic will try to retry 5 times before aborting the message (it will respect the rate limiter). This method will help prevent cases of failed code publishing when it takes a little longer to fetch data from Voucherify.

If you do not use {% raw %}`:retry`{% endraw %}, then irrespective of the response returned from Voucherify, Braze will attempt to send the distribution, which may result in generating emails without a published code.

![Add retry attribute to Braze email template]({% image_buster /assets/img/voucherify/voucherify_cc_retry.png %})

{% endtab %}
{% tab Unique publications %}

#### Unique publication per customer

The {% raw %}`source_id`{% endraw %} parameter in the script body provides that each customer can receive only one unique code in a single Braze campaign. As a result, even if Braze unintentionally multiplies the request, each user will receive the same unique code that was published to him/her in the first message.

![Add source id to Braze email template]({% image_buster /assets/img/voucherify/voucherify_cc_sourceId_unique_publication.png %})

You can modify {% raw %}`{{source_id}}`{% endraw %} and its effect on publications by using the following configurations:

| Configuration                                                                                         | Effect                                                                                                                                                                                                                                                    |
| ----------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| {% raw %}`{{campaign.${dispatch_id}}}`{% endraw %}                                                    | Ensures that all customers within a single send-out will use the same publication.                                                                                                                                                                        |
| {% raw %}`{{campaign.${api_id}}}`{% endraw %}                                                         | Ensures that all customers within a single campaign will use the same publication.                                                                                                                                                                        |
| {% raw %}`{{${user_id}}}`{% endraw %} or {% raw %}`{{${braze_id}}}`{% endraw %}                       | Ensures that every customer will use the same publication no matter which campaign is sent (you can use {% raw %}`${user_id}`{% endraw %} which is an {% raw %}`external_id`{% endraw %} and {% raw %}`${braze_id}`{% endraw %} which is an internal id). |
| {% raw %}`{{campaign.${dispatch_id}}}`{% endraw %} and {% raw %}`{{campaign.${user_id}}}`{% endraw %} | Each customer within a single send-out will use the same unique publication.                                                                                                                                                                              |

{% endtab %}
{% tab Join-once %}

#### Customer can join only once

If your Voucherify campaign has a limit _Customers can join only once_, remove publication source id from the script body. Voucherify will make sure that each Braze message to the same customer will deliver the same code that was published in the first place.

![Customer can join only once]({% image_buster /assets/img/voucherify/voucherify_cc_join_once.png %}){: style="max-width:50%;"}

Your Connected Content script should be as follows:

{% raw %}

```liquid
{% assign braze_campaign_id = {{campaign.${api_id}}} %}
{% assign customer_id = {{${user_id}}} %}
{% assign cache_id = braze_campaign_id | append: customer_id %}
{% assign voucherify_campaign_id = "VOUCHERIFY-CAMPAIGN_ID" %}

{% connected_content
   https://api.voucherify.io/v1/publications?cache_id={{cache_id}}
   :method post
   :headers {
	"X-App-Id": "VOUCHERIFY-APP-ID",
	"X-App-Token": "VOUCHERIFY-APP-TOKEN"
   }
   :body campaign={{voucherify_campaign_id}}&customer={{customer_id}}&channel=Braze
   :content_type application/json
   :cache_max_age
   :retry
   :save publication
 %}
```

{% endraw %}
{% endtab %}
{% endtabs %}

---

## Examples

{% alert important %}
Keep in mind that all examples below use Voucherify publication source id, and Braze cache and retry parameters to limit API calls invoked by a Braze campaign. You must be aware of the following consequences:

- It isn't possible to publish and send different codes to the same customer in a single Braze campaign.
- If your Voucherify campaign uses the _join only once feature_, you need to remove source_id from the connected content body as described in the join-once tab above.
  {% endalert %}

#### Publish and send unique coupon code

In this example, the Connected Content script calls Voucherify API to publish a unique coupon code and send it in the Braze message. Each Braze user receives only one unique code.

{% raw %}

```liquid
{% assign braze_campaign_id = {{campaign.${api_id}}} %}
{% assign customer_id = {{${user_id}}} %}
{% assign source_id = braze_campaign_id | append: customer_id %}
{% assign voucherify_campaign_id = "VOUCHERIFY-CAMPAIGN_ID" %}
{% assign cache_id = source_id %}

{% connected_content
   YOUR API ENDPOINT/v1/publications?cache_id={{cache_id}}
   :method post
   :headers {
        "X-App-Id": "VOUCHERIFY-APP-ID",
        "X-App-Token": "VOUCHERIFY-APP-TOKEN"
   }
   :body campaign={{voucherify_campaign_id}}&customer={{customer_id}}&channel=Braze&source_id={{source_id}}
   :content_type application/json
   :cache_max_age
   :retry
   :save publication
 %}
```

{% endraw %}

#### Invite new referrers

This Connected Content script enables you to publish and send unique referral codes to selected Braze users. Each user receives only one referral code to share with other users and gain new referrals.

{% raw %}

```liquid
{% assign braze_campaign_id = {{campaign.${api_id}}} %}
{% assign customer_id = {{${user_id}}} %}
{% assign source_id = braze_campaign_id | append: customer_id %}
{% assign voucherify_campaign_id = "VOUCHERIFY-CAMPAIGN_ID" %}
{% assign cache_id = source_id %}

{% connected_content
   YOUR API ENDPOINT/v1/publications?cache_id={{cache_id}}
   :method post
   :headers {
        "X-App-Id": "VOUCHERIFY-APP-ID",
        "X-App-Token": "VOUCHERIFY-APP-TOKEN"
   }
   :body campaign={{voucherify_campaign_id}}&customer={{customer_id}}&channel=Braze&source_id={{source_id}}
   :content_type application/json
   :cache_max_age
   :retry
   :save publication
 %}
```

{% endraw %}

#### Fetch loyalty card balance

Here is an example of a Connected Content script that pulls the current loyalty balance based on the loyalty card code that was sent beforehand to Braze as a custom attribute. Note that you need to store the loyalty card code as a custom attribute in Braze user’s profile before using this script.

{% raw %}

```liquid
{% assign braze_campaign_id = {{campaign.${api_id}}} %}
{% assign customer_id = {{${user_id}}} %}
{% assign source_id = braze_campaign_id | append: customer_id %}
{% assign voucherify_campaign_id = "VOUCHERIFY-CAMPAIGN_ID" %}
{% assign cache_id = source_id %}

{% connected_content
   YOUR API ENDPOINT/v1/loyalties/{{voucherify_campaign_id}}/members/{{custom_attribute.${loyalty.card}}}?cache_id={{cache_id}}
   :method get
   :headers {
        "X-App-Id": "VOUCHERIFY-APP-ID",
        "X-App-Token": "VOUCHERIFY-APP-TOKEN"
   }
   :content_type application/json
   :cache_max_age
   :retry
   :save member
 %}
```

{% endraw %}

#### Create custom code

Connected Content is a powerful tool allowing the introduction of creative scenarios. You can create a custom coupon code based on the customer’s profile information.

Here is an example of a code snippet that will take into account the customer’s phone number for generating a unique code. In this example, the Connected Content script calls the Voucherify API to publish a custom coupon code.

1.  First, we will define all variables that we need. Then, we will create a coupon code starting with a prefix “SummerTime-” and the rest of the code will be the customer’s phone number. You can decide on the custom attribute that you would like to base your coupon codes on.  
    
    {% raw %}
    
    ```liquid
    {% assign braze_campaign_id = {{campaign.${dispatch_id}}} %}
    {% assign customer_id = {{${user_id}}} %}
    {% assign phoneNumber = {{${phone_number}}} %}
    {% assign source_id = braze_campaign_id | append: customer_id %}
    {% assign cache_id = source_id %}
    {% assign voucherify_campaign_id = "VOUCHERIFY-CAMPAIGN_ID" %}
    {% assign prefix = "SummerTime-" %}
    ```
    
    {% endraw %}
    
2.  Next, we request Voucherify to generate a single code in the campaign. We provide the name of the coupon code to be created in the URL:  
    
    {% raw %}
    
    ```liquid
    {% connected_content
       YOUR-API-ENDPOINT/v1/campaigns/{{voucherify_campaign_id}}/vouchers/{{prefix}}{{phoneNumber}}?cache_id={{cache_id}}
       :method post
       :headers {
            "X-App-Id": "VOUCHERIFY-APP-ID",
            "X-App-Token": "VOUCHERIFY-APP-TOKEN"
       }
       :content_type application/json
       :cache_max_age 
       :save voucher_created
       :retry
    %}  
    ```  
    
    {% endraw %}  

3.  Finally, we can publish the code we just created. The code snippet looks almost the same as you used for generating a random voucher from a campaign. However, this time we are targeting a specific voucher code.  
    
    {% raw %}  
    
    ```liquid
    {% connected_content
       YOUR-API-ENDPOINT/v1/publications?cache_id={{cache_id}}
       :method post
       :headers {
           "X-App-Id": "VOUCHERIFY-APP-ID",
           "X-App-Token": "VOUCHERIFY-APP-TOKEN"
       }
       :body voucher={{prefix}}{{phoneNumber}}&customer={{customer_id}}&channel=Braze&source_id={{source_id}}
       :content_type application/json
       :cache_max_age 
       :save publication
       :retry
    %}
    ```
    
    {% endraw %}

As a result, the customer receives the following email:  

![Braze rate limiter]({% image_buster /assets/img/voucherify/voucherify_cc_custom_code_email.png %})

Here is the complete snippet used in this example:

{% raw %}

```liquid
{% assign braze_campaign_id = {{campaign.${dispatch_id}}} %}
{% assign customer_id = {{${user_id}}} %}
{% assign phoneNumber = {{${phone_number}}} %}
{% assign source_id = braze_campaign_id | append: customer_id %}
{% assign cache_id = source_id %}
{% assign voucherify_campaign_id = "VOUCHERIFY-CAMPAIGN_ID" %}
{% assign prefix = "Your Prefix" %}

{% connected_content
   YOUR-API-ENDPOINT/v1/campaigns/{{voucherify_campaign_id}}/vouchers/{{prefix}}{{phoneNumber}}?cache_id={{cache_id}}
   :method post
   :headers {
        "X-App-Id": "VOUCHERIFY-APP-ID",
        "X-App-Token": "VOUCHERIFY-APP-TOKEN"
   }
   :content_type application/json
   :cache_max_age 
   :save voucher_created
   :retry
%} 

{% connected_content
   YOUR-API-ENDPOINT/v1/publications?cache_id={{cache_id}}
   :method post
   :headers {
       "X-App-Id": "VOUCHERIFY-APP-ID",
       "X-App-Token": "VOUCHERIFY-APP-TOKEN"
   }
   :body voucher={{prefix}}{{phoneNumber}}&customer={{customer_id}}&channel=Braze&source_id={{source_id}}
   :content_type application/json
   :cache_max_age 
   :save publication
   :retry
%}
```

{% endraw %}

---

## Display fetched data in Braze messages

We’re assuming you already have a Braze campaign or canva in which you want to use the connected content script.

#### Step 1: Add connected content script to message template

1.  Copy and paste the Connected Content script under the {% raw %}`<body>`{% endraw %} tag in a message HTML template. 
    Replace **CAMPAIGN_ID** with a Voucherify {% raw %}`campaign_id`{% endraw %} copied from the URL address of Voucherify campaign dashboard.  
    
    ![Fetch campaign ID from URL]({% image_buster /assets/img/voucherify/voucherify_cc_campaignId.png %}){: style="margin-top:15px;margin-bottom:15px;"}
    
    {% raw %}
    
    ```
    assign voucherify_campaign_id = "camp_Y7h1meBSyybsNs7UpSVVZZce"
    ```
    
    {% endraw %}

2.  Paste your API endpoint. If you don't know what your API endpoint is, you can check it in the **Project settings** > **General** > **API endpoint**.<br>  
    
    ![API Endpoint]({% image_buster /assets/img/voucherify/voucherify_cc_endpoint.png %}){: style="margin-top:15px;margin-bottom:15px;"}
    
    {% raw %}
    
    ```
    YOUR API ENDPOINT/v1/publications?cache_id={{cache_id}}
    ```
    
    {% endraw %}
    
    | Shared Cluster   | Endpoint for Braze Connected Content          |
    | ---------------- | --------------------------------------------- |
    | Europe (default) | https://api.voucherify.io/v1/publications     |
    | United States    | https://us1.api.voucherify.io/v1/publications |
    | Asia (Singapore) | https://as1.api.voucherify.io/v1/publications |
    
3.  Add your API keys for authentication. You can find  Voucherify-App-Id and Voucherify-App-Token in your **Project Settings > General > Application Keys.**<br>

    ![Application Keys]({% image_buster /assets/img/voucherify/voucherify_cc_app_keys.png %}){: style="margin-top:15px;margin-bottom:15px;"}
    
    {% raw %}
    
    ```
    "X-App-Id": "VOUCHERIFY-APP-ID",
    "X-App-Token": "VOUCHERIFY-APP-TOKEN"
    ```
    
    {% endraw %}
    
Now your Connected Content script is ready to go.

{% raw %}

```liquid
{% assign braze_campaign_id = {{campaign.${api_id}}} %}
{% assign customer_id = {{${user_id}}} %}
{% assign source_id = braze_campaign_id | append: customer_id %}
{% assign voucherify_campaign_id = "camp_Y7h1meBSyybsNs7UpSVVZZce" %}
{% assign cache_id = source_id %}

{% connected_content
   https://api.voucherify.io/v1/publications?cache_id={{cache_id}}
   :method post
   :headers {
        "X-App-Id": "490a3fb6-a",
        "X-App-Token": "328099d5-a"
   }
   :body campaign={{voucherify_campaign_id}}&customer={{customer_id}}&channel=Braze&source_id={{source_id}}
   :content_type application/json
   :cache_max_age
   :retry
   :save publication
 %}
```

{% endraw %}

#### Step 2: Create snippet to display fetched data

Responses from the Voucherify API is stored by connected content under the value of {% raw %}`:save`{% endraw %} parameter. For example:

{% raw %}

```liquid
:save member
```
{% endraw %}

This enables you to retrieve and display data from a Voucherify response in Braze messages.

You can create snippets that display the published code, loyalty card balance, expiration date, and other parameters included in JSON format response from the Voucherify API.

For example, to display the published code in a message template, you need to create a snippet that fetches a unique code from the voucher object.

Connected content script:

![Connected content script showing where you save a Voucherify response]({% image_buster /assets/img/voucherify/voucherify_cc_save_parameter.png %})

Snippet in Braze message template:

{% raw %}

```liquid
{{publication.voucher.code}}
```

{% endraw %}

As a result, each customer gets a message with a unique code automatically assigned to their profile. Each time a code is received by the user, it is published to his/her profile in Voucherify.

To display a loyalty card balance fetched from the Voucherify API, you need to create the following snippet:

{% raw %}

```liquid
{{member.loyalty_card.balance}}
```

{% endraw %}

where the member is a value of the {% raw %}`:save`{% endraw %} parameter in Connected Content script.

{% raw %}

```liquid
:save member
```

{% endraw %}

We highly advise you not to entirely depend on the 'Preview mode' and to send several test messages to confirm that everything works as it should.

#### Step 3: Set up rate limiter

When setting up a campaign target, use advanced settings to limit the number of messages sent per minute.

![Braze rate limiter]({% image_buster /assets/img/voucherify/voucherify_cc_limiter.png %})

Read more about Rate Limiter and Frequency Capping in Braze [documentation]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#delivery-speed-rate-limiting).
