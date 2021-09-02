---
nav_title: Voucherify
article_title: Voucherify
alias: /partners/voucherify/
description: "This article outlines the partnership between Braze and Voucherify, an all-in-one promotional platform that allows users to automatically send personalized coupons, gift cards, loyalty cards, referral codes, and more – all through their Braze account while tracking redemptions and campaign growth at every step."
page_type: partner
search_tag: Partner

---

# Voucherify

> [Voucherify](https://www.voucherify.io/) is an all-in-one promotional platform that allows for personalized campaigns and loyalty programs that drive user engagement and retention. 

With the Braze and Voucherify integration, users can automatically send personalized coupons, gift cards, loyalty cards, referral codes, and more – all through their Braze account while tracking redemptions and campaign growth at every step.

## How does it work?
Leverage the power of Voucherify and grow your promotional campaigns by sending unique codes through the use of:
- __[Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content)__: Add unique codes to Braze campaigns via Braze’s Connected Content. You can use Voucherify discount coupons, gift card campaigns, loyalty cards, and referral codes with this feature.
- __[Custom Attributes]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes)__: Custom attributes enable you to assign Voucherify unique coupons, gift cards, loyalty cards, and referral codes to users’ profiles in Braze. As a result, you can send attached codes and their attributes in email campaigns and share them with your users.
- __[Promotion Codes Lists]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes)__: Use Voucherify generated promotion codes and upload them into Braze.

## Prerequisites

Requirement   |Origin| Description
--------------|------|-------------
Braze API Key    |[Braze Settings](https://dashboard.braze.com/sign_in)| A REST API Key linked to your Braze account with the __users.track__ permission enabled

## Send Unique Codes via Connected Content

Add unique codes to Braze campaigns via Braze’s Connected Content. You can use Voucherify discount coupons, gift card campaigns, loyalty cards, and referral codes with this feature.

### Step 1: Create a New Campaign

From the Braze Dashboard, create a new campaign, define your campaign name, choose an email template, and edit the email body.

### Step 2: Add Code Snippet to Email Body

Add a code snippet with code publication settings under the ```<body>``` tag in the email template.

{% raw %}
```
{% assign campaign_id = {{campaign.${api_id}}} %}
{% assign customer_id = {{${user_id}}} %}
{% assign source_id = campaign_id | append: customer_id %}

{% connected_content
	https://api.voucherify.io/v1/publications
	:method post
	:headers {
		"X-App-Id": "VOUCHERIFY-APP-ID",
		"X-App-Token": "VOUCHERIFY-APP-TOKEN"
	}

	:body campaign=CAMPAIGN_ID&customer={{${user_id}}}&channel=Braze&source_id={{source_id}}
	:content_type application/json
	:save publication
%}
```
{% endraw %}

After you copy the code to the email body, add your API keys and campaign id as described below:

1.  Add `VOUCHERIFY-APP-ID` and `VOUCHERIFY-APP-TOKEN` from your Voucherify Project Settings (section Application Keys).<br><br>
2. Replace `CAMPAIGN_ID`, a unique identifier of your Voucherify campaign. You can find the campaign ID in the URL while displaying the campaign details in the Voucherify dashboard.<br>![VOUCHERIFY CAMPAIGN ID]({% image_buster /assets/img/voucherify-cc-campaignId.png %})<br><br>
3. Lastly, add the {% raw %}`{{publication.voucher.code}}`{% endraw %} to the email body to display the published code, and select Preview and Test. In the preview, you should see a random code from your Voucherify Campaign. <br><br>We highly advise you not to depend on the Preview mode entirely and to send several test messages to confirm that everything works as it should.<br>![CONNECTED CONTENT PREVIEW]({% image_buster /assets/img/voucherify-cc-preview.png %})
 
{% alert important %}
The {% raw %}`{{source_id}}`{% endraw %} parameter in the email body ensures that each customer will receive only one unique code in a single Braze email campaign. It prevents sending other codes to the same customer. Even if Braze unintentionally multiplies messages, the user will receive the same code that was published to them in the first message. If you'd like to change this effect, [go here](https://support.voucherify.io/article/113-braze#sourceid) to see other {% raw %}`{{source_id}}`{% endraw %} configurations. 
{% endalert %}

### Step 3: Send Messages with Codes to your Users

Finish modeling the campaign settings and activate the workflow with Launch Campaign.

Each user defined in the campaign Target Users will get an email with a unique code automatically assigned to their profile in Voucherify.

### Step 4: Track Sent Codes in Voucherify
![CODE PUBLISHED]({% image_buster /assets/img/voucherify-cc-code-published.png %}){: style="float:right;max-width:30%;margin-bottom:15px;"}
When a code gets to the user, it is published to their profile in Voucherify.

If a user redeems the code, you’ll see the redemption details in your Voucherify Dashboard.

![CODE REDEMPTION]({% image_buster /assets/img/voucherify-redemption.png %})

{% alert important %}
-   When testing the email template be aware of the Connected Content cache (at least 5 minutes). If you want each test preview to publish a new voucher, you can omit the cache by appending a query parameter to the URL, e.g. {%raw%}`?t=1`{%endraw%}, and increment the number with each test.<br><br>
-   X-Voucherify-API-Version (optional) – if your project uses the API Version older than v2017-04-20, then you should use a slightly different syntax `:save voucher` instead of `:save publication` and to display the code type {%raw%}{{voucher.code}}{%endraw%}.<br><br> 
-   While setting up publication `source_id` you can differentiate your users by using two different variables: {%raw%}`${user_id}`{%endraw%} which is an external id (seen as source id in a customer profile in Voucherify) and {%raw%}`${braze_id}`{%endraw%} which is an internal id.  
{% endalert %}

## Assign Unique Codes to Users’ Custom Attributes

Braze custom attributes enable you to assign Voucherify unique coupons, gift cards, loyalty cards, and referral codes to users’ profiles in Braze. As a result, you can send attached codes and their attributes in email campaigns and share them with your users.

### Step 1: Connect your Voucherify Account with Braze

Copy the REST API Key from your Braze account. Your API key should have __user.track__ permissions.

Next, visit to the Integrations Directory in your Voucherify Dashboard, find Braze integration and paste the copied REST API Key:

![VOUCHERIFY INTEGRATION HUB]({% image_buster /assets/img/voucherify-integrations-hub.png %}){: style="max-width:70%;"}

When both accounts are connected, you can start a new Voucherify distribution that assigns unique codes to the custom attributes in the users’ profiles in Braze.

### Step 2: Launch Voucherify Distribution

You can distribute codes to Braze using manual mode or define an automated workflow that triggers code delivery in response to your users’ actions.

In both manual and automatic mode, Voucherify sends unique codes with their attributes and assigns them to custom attributes in users' profiles.

![CUSTOM ATTRIBUTES]({% image_buster /assets/img/voucherify-custom-attributes-mapping.png %})

Besides the unique code, you can also attach the date when the code was delivered to Braze, the code’s value, and URLs that direct to the customer cockpit and the customer cockpit preference center. Voucherify customer cockpit displays all assigned codes and available rewards.

{% alert important %}
Please note that before setting up distribution, you need to add your Braze users to the Voucherify dashboard. [Go here to read more](https://support.voucherify.io/article/67-how-to-import-my-customers). 
{% endalert %}

{% tabs %}
{% tab Manual Message %}

Manual mode works as a one-time action that assigns codes to a chosen audience. You can select a Voucherify segment of users or a single user as your receivers and choose a campaign that will be a source of unique codes. 

![MANUAL MODE]({% image_buster /assets/img/voucherify-manual-conditions.png %}){: style="max-width:60%;"}

To set up manual distribution with Braze and Voucherify, [visit a Voucherify step-by-step tutorial](https://support.voucherify.io/article/113-braze#CustomAttributes).
{% endtab %}
{% tab Automatic Workflow %}

Set an automated workflow that delivers codes to Braze in response to actions taken by your users:
-   __Customer entered/left specific Voucherify segment.__
-   __Successful code publication__ – the message is sent once the code from a campaign is published (assigned) to a customer in Voucherify.
-   __Order status changed__ (order created, order update, order paid, order canceled).
-   __Gift credits added__ – the message is sent once gift card credits are added to the customer's card.
-   __Loyalty points added__ – the message is sent once loyalty points are added to the customer's profile.
-   __Voucher redeemed__ – the message is sent to customers who successfully redeemed vouchers.
-   __Voucher redemption rollback__ – the message is sent to the customer whose redemption was successfully rolled back.
-   __Reward redemption__ – the message is sent when a customer redeems a loyalty or referral reward.

To set up an automatic workflow with Braze and Voucherify, [visit a Voucherify step-by-step tutorial](https://support.voucherify.io/article/19-how-does-the-distribution-manager-work).
{% endtab %}
{% endtabs %}
### Step 3: Use Custom Attribute with Code in Braze Campaigns
![CUSTOM ATTRIBUTE ASSIGNED]({% image_buster /assets/img/voucherify-custom-attribute.png %}){: style="float:right;max-width:30%;margin-left:15px;"}
When the custom attribute with code is added, you can use it in Braze campaigns.

Edit your email body and add the custom attribute defined in the Voucherify distribution. Type {%raw%}`{{custom_attribute.${custom_attribute_with_code}}}`{%endraw%} to display the unique code.<br><br>![CUSTOM ATTRIBUTE IN EMAIL BODY]({% image_buster /assets/img/voucherify-custom-attribute-in-email.png %})

When it's ready, you can see the code in your message preview.
![EMAIL PREVIEW WITH CUSTOM ATTRIBUTE]({% image_buster /assets/img/voucherify-email-preview-custom-attribute.png %})

### Step 4: Track Sent Codes in Voucherify

Each time a code gets to the user, it is assigned to their profile in Voucherify.

When a user redeems the code, you’ll see the redemption details in your Voucherify Dashboard.

![REDEMPTION SUCCEED]({% image_buster /assets/img/voucherify-redemption.png %})

## Upload Voucherify Codes to Braze Promo Codes Lists

Next to the Connected Content and custom attributes, you can share Voucherify codes using Braze Promo Codes snippet.

### Step 1: Export Unique Codes from Voucherify Campaign.

Edit the CSV file and remove the name of the column to leave the list of codes only.

![REDEMPTION SUCCEED]({% image_buster /assets/img/voucherify-export-Codes.png %})

### Step 2: Create Promotion Code List in Braze
![CREATE PROMOTION LIST]({% image_buster /assets/img/voucherify-create-Promotion-Codes.png %}){: style="float:right;max-width:30%;margin-left:15px;"}
Go to the Promotion Codes in the Braze Integrations section and click Create Promotion Code List.  

You can use the Voucherify campaign name to name the list to ensure data consistency. Besides the name, add the code snippet that refers to the codes from the list. The snippet will be populated with a unique code once the message is sent. 

![PROMOTION LIST DETAILS]({% image_buster /assets/img/voucherify-promotion-codes-details.png %}){: style="max-width:70%;"}

You can set attributes for codes such as List Expiration and Threshold Alerts. However, note that Voucherify manages the logic behind your codes regardless of list settings.

![PROMOTION LIST EXPIRATION]({% image_buster /assets/img/voucherify-promotion-codes-list-expiration.png %}){: style="max-width:70%;"}

Upload the CSV file with Voucherify codes.

![CSV IMPORT]({% image_buster /assets/img/voucherify-import-codes-braze.png %})

When the import is done, click Save to confirm the list details.
 
### Step 3: Use Code Snippet in Braze Campaign
To use codes from the list in a Braze campaign, Copy Snippet and add it to the email body.

![COPY SNIPPET]({% image_buster /assets/img/voucherify-promotion-list-copy-snippet.png %}){: style="max-width:60%;"}

Add the code snippet to display a code from the list.

![LIST CODE SNIPPET IN EMAIL]({% image_buster /assets/img/voucherify-promotion-list-snippet-email.png %})

Once the message with code is sent, the same code won’t be used ever again.

If you need help with any of the steps above, visit [our detailed Braze Promo Codes User Guide]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes).
