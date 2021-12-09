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

The Braze and Voucherify integration allows you to grow your promotional campaigns by sending unique codes through the use of:

- [Connected Content](#generate-unique-codes-using-connected-content): Add unique codes to Braze campaigns via Braze’s Connected Content. With this feature, you can use Voucherify discount coupons, gift card campaigns, loyalty cards, and referral codes.
- [Custom Attributes](#assign-unique-codes-to-users-custom-attributes): Custom attributes enable you to assign Voucherify unique coupons, gift cards, loyalty cards, and referral codes to users' profiles in Braze. As a result, you can send attached codes and attributes in email campaigns and share them with your users.
- [Promotion Codes Lists](#upload-voucherify-codes-to-braze-promo-codes-lists): Use Voucherify generated promotion codes and upload them into Braze.

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
|Voucherify account | A Voucherify account is required to take advantage of this partnership. |
| Braze REST API key | A Braze REST API Key with `users.track` permissions. <br><br> This can be created within the __Braze Dashboard -> Developer Console -> REST API Key -> Create New API Key__ |
{: .reset-td-br-1 .reset-td-br-2}

## Integration

### Generate unique codes using Connected Content

#### Step 1: Build out Voucherify Connected Content call

From the Braze dashboard, create a new campaign. In the email body, add the following code snippet:

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

After you copy the code to the email body, add your application keys and `CAMPAIGN_ID` as described below:

1. Add `VOUCHERIFY-APP-ID` and `VOUCHERIFY-APP-TOKEN` from your Voucherify project settings under **Application Keys**.<br><br>
2. Replace `CAMPAIGN_ID`, you can find the campaign ID in the Voucherify campaign URL.<br>![VOUCHERIFY CAMPAIGN ID]({% image_buster /assets/img/voucherify-cc-campaignId.png %})<br><br>
3. Lastly, add {% raw %}`{{publication.voucher.code}}`{% endraw %} to the email body to display the published code, and select **Preview and Test**. <br><br>We highly advise you to send several test messages to confirm that everything works as it should.
 
{% alert important %}
The {% raw %}`{{source_id}}`{% endraw %} parameter in the email body ensures that each customer will receive only one unique code in a single Braze email campaign, and upon resend, will receive the same code. Visit [Voucherify](https://support.voucherify.io/article/113-braze#sourceid) to change this behavior and see other configurations. 
{% endalert %}

#### Step 2: Send and track user codes
![Code published]({% image_buster /assets/img/voucherify-cc-code-published.png %}){: style="float:right;max-width:30%;margin-bottom:15px;"}
Launch your Braze campaign to send codes to your users, these codes will automatically be assigned to their profile in Voucherify.

When a code gets to the user, it is published to their profile in Voucherify.

If a user redeems the code, you’ll see the redemption details in your Voucherify Dashboard.

![Code redemption]({% image_buster /assets/img/voucherify-redemption.png %})

{% alert important %}
-   When testing the email template, be aware of the Connected Content cache (at least 5 minutes). If you want each test preview to publish a new voucher, you can omit the cache by appending a query parameter to the URL, e.g. {%raw%}`?t=1`{%endraw%}, and increment the number with each test.<br><br>
-   While setting up publication `source_id`, you can differentiate your users by using two different variables: {%raw%}`${user_id}`{%endraw%} which is an external id (seen as source id in a customer profile in Voucherify) and {%raw%}`${braze_id}`{%endraw%} which is an internal id.  
{% endalert %}

### Assign unique codes to users’ custom attributes

#### Step 1: Connect Voucherify account

To connect your Voucherify account, visit the **Integrations Directory** in your Voucherify dashboard, locate the Braze integration, and add your Braze API key. 

![Vouhcerify integration hub]({% image_buster /assets/img/voucherify-integrations-hub.png %}){: style="max-width:70%;"}

#### Step 2: Code distribution 

Next, you must decide whether to distribute codes to Braze in manual mode or define a workflow that triggers code delivery in response to your user's actions. In both situations, Voucherify sends unique codes with their attributes and assigns them as custom attributes in users' profiles.

![Custom Attributes]({% image_buster /assets/img/voucherify-custom-attributes-mapping.png %})

Besides the unique code, you can also attach attributes like when the code was delivered, the code's value, and URLs that direct the customer to the cockpit, where all assigned codes and available rewards will be listed.

{% alert important %}
Please note that before setting up distribution, you need to add your Braze users to the Voucherify dashboard. [Go here to read more](https://support.voucherify.io/article/67-how-to-import-my-customers). 
{% endalert %}

{% tabs %}
{% tab Manual Message %}

Manual mode works as a one-time action that assigns codes to a chosen audience. You can select a Voucherify segment of users or a single user as your receivers and choose a campaign that will be a source of unique codes. 

![Manual mode]({% image_buster /assets/img/voucherify-manual-conditions.png %}){: style="max-width:60%;"}

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

#### Step 3: Use Voucherify custom attributes in your Braze campaign

![Custom attribute assigned]({% image_buster /assets/img/voucherify-custom-attribute.png %}){: style="float:right;max-width:30%;margin-left:15px;"}
When the custom attribute with code is added, you can use it in Braze campaigns. To do this, edit your email body and add {%raw%}`{{custom_attribute.${custom_attribute_with_code}}}`{%endraw%} to display the unique code.<br><br>![Custom attribute in email body]({% image_buster /assets/img/voucherify-custom-attribute-in-email.png %})

You can see the code in your message preview when it's ready.
![email with preview custom attribute]({% image_buster /assets/img/voucherify-email-preview-custom-attribute.png %})

#### Step 4: Track sent codes in Voucherify

![Code published]({% image_buster /assets/img/voucherify-cc-code-published.png %}){: style="float:right;max-width:30%;margin-bottom:15px;"}
Launch your Braze campaign to send codes to your users; these codes will automatically be assigned to their profile in Voucherify.

When a code gets to the user, it is published to their profile in Voucherify.

If a user redeems the code, you’ll see the redemption details in your Voucherify Dashboard.

![Code redemption]({% image_buster /assets/img/voucherify-redemption.png %})

### Upload Voucherify codes to Braze promo codes lists

Next to the Connected Content and custom attributes, you can share Voucherify codes using Braze Promo Codes snippet.

#### Step 1: Export unique codes from your Voucherify campaign

Export the Voucherify code list and edit the CSV file to remove the column's name to leave the list of codes only.

![Redemption Succeed]({% image_buster /assets/img/voucherify-export-Codes.png %})

#### Step 2: Create promotion code list in Braze

Navigate to **Promotion Codes** and click **Create Promotion Code List**.

Next, update the Liquid code snippet that will be used to call from the list. Once the message is sent, this snippet will be populated with a unique code.   

![PROMOTION LIST DETAILS]({% image_buster /assets/img/voucherify-promotion-codes-details.png %}){: style="max-width:70%;"}

You can set attributes for codes such as list expiration and threshold alerts. However, note that Voucherify manages the logic behind your codes regardless of list settings.

Next, upload the CSV file with Voucherify codes.

![CSV Import]({% image_buster /assets/img/promocodes/promocode6.png %})

When the import is done, click **Save**.
 
#### Step 3: Use the code snippet in your Braze campaign

To use codes from the list in a Braze campaign, copy the snippet and add it to the email body.

![Copy snippet]({% image_buster /assets/img/voucherify-promotion-list-copy-snippet.png %}){: style="max-width:60%;"}

![List code snippet in email]({% image_buster /assets/img/voucherify-promotion-list-snippet-email.png %})

Once the message with the code is sent, the same code will not be reused.

If you need help with any of the steps above, visit [Promotion codes]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes).
