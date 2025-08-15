---
nav_title: Distributions with custom attributes
article_title: Distributions with Custom Attributes with Voucherify
page_order: 3
alias: /partners/voucherify/custom_attributes/
description: "This reference article outlines Braze integration with Voucherify. Braze integration enables you to send Voucherify codes in your Braze messages."
page_type: partner
search_tag: Partner
---

# Distributions with custom attributes

> Braze integration enables you to send Voucherify codes in your Braze messages. This reference article covers how to use Braze custom attributes with Voucherify distributions.

_This integration is maintained by Voucherify._

{% alert tip %}
Before you use Braze custom attributes in Voucherify distributions, you need to add your Braze users to the Voucherify dashboard. You can use Braze Connected Content to synchronize users or import your customers through CSV or API. Visit [Voucherify](https://support.voucherify.io/article/67-how-to-import-my-customers) to learn more.
{% endalert %}

Braze custom attributes enable you to assign Voucherify codes to custom attributes in user profiles in Braze. You can use unique coupons, gift cards, loyalty cards, and referral codes. First, connect Voucherify with Braze, create a distribution in Voucherify, and finally create a campaign in Braze with the custom attribute snippet in your message template.

## Step 1: Connecting your Voucherify account to Braze

First, connect your Voucherify account with Braze.

1. Copy the REST API key from your Braze account.
2. Go to the **Integrations** directory in your Voucherify dashboard, find Braze and choose **Connect.**  
    
    ![]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_integrations.png %}){: style="margin-top:15px;margin-left:25px;margin-bottom:15px;"}
    
3. Paste the Braze API key and choose **Connect**:  
    
    ![]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_enter_API_key.png %}){: style="max-width:60%;margin-top:15px;margin-left:25px;margin-bottom:15px;"}


## Step 2: Code distribution

When connected, you can start a new Voucherify [distribution](https://support.voucherify.io/article/19-how-does-the-distribution-manager-work) that assigns a code to the custom attribute in the user profile in Braze. Later on, you can use received attributes with codes in your Braze campaigns.

Before setting up distribution, you need to add your Braze users to the Voucherify dashboard. Visit [Voucherify](https://support.voucherify.io/article/67-how-to-import-my-customers) to learn more.

![]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_distribution.png %})

You can distribute codes to Braze using two modes:

- **Manual mode**
- Define an **automated workflow** that triggers code delivery in response to an action taken by your users.

In both manual and automatic modes, Voucherify sends unique codes with their attributes and assigns them to Braze Custom Attributes in users' profiles.

![Map fields to custom attributes]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_fields_mapping.png %})

{% tabs %}
{% tab Manual distribution %}

Manual mode is a one-time action that assigns codes to a chosen audience. Go to the **Distributions** in your dashboard, run the distribution manager with the plus, and Choose **Manual Message**.

1.  Name your distribution.

    ![]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_name_distribution.png %}){: style="max-width:90%;margin-top:15px;margin-bottom:15px;"}<br>  
    
    Choose a campaign that will be a source of unique codes **(1)** and select a segment of users or a single customer as your receivers **(2)**. Visit [Voucherify](https://support.voucherify.io/article/51-customer-segments) to learn more about customer segments.  
    
    ![]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_name_distribution_choose_segment.png %}){: style="max-width:90%;margin-top:15px;margin-bottom:15px;"}  

2.  Next, add marketing permissions. If you don't collect permissions from your audience, disable the consent verification.  
    
    ![]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_consents.png %}){: style="max-width:90%;margin-top:15px;margin-bottom:15px;"}  
    
3.  Choose Braze as a channel and map custom fields that will be added to the user profile in Braze. You need to add the field representing the code of the published voucher; the rest of the fields are optional.  
    
    ![]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_channel.png %}){: style="max-width:90%;margin-top:15px;margin-bottom:15px;"}  
    
4.  When completed, you can see a summary of the distribution. Click **Save and send** to deliver codes to user profiles in Braze.  

_Note that all manual distributions are sent with a 10-minute delay._

{% endtab %}
{% tab Automatic Workflow %}

Voucherify can push codes to Braze automatically in response to the following triggers:

- **Customer entered/left specific Voucherify segment**
- **Successful code publish** – the message is sent when the code from a campaign is published (assigned) to a customer in Voucherify.
- **Order status changed** (order created, order updated, order has been paid, order canceled)
- **Gift credits added** – the message is sent when gift card credits are added to the customer's card.
- **Loyalty points added** – the message is sent when loyalty points are added to the customer's profile.
- **Voucher redeemed** – the message is sent to customers who successfully redeemed vouchers.
- **Voucher redemption rollback** – the message is sent to the customer whose redemption was successfully rolled back.
- **Reward redemption** – the message is sent when a customer redeems a loyalty or referral reward.
- **Custom event was logged for a customer** - the message is triggered when Voucherify logs a particular custom event.

To set up an automatic workflow with Braze and Voucherify, [visit distributions tutorial](https://support.voucherify.io/article/19-how-does-the-distribution-manager-work).

{% endtab %}
{% endtabs %}

## Step 3: Use Voucherify custom attributes in your Braze campaign

![]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_code.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

Once the custom attribute with the code is added to the customer's custom attributes in Braze, you can use it in your campaigns.

Edit the message body and add the custom attribute defined in the Voucherify distribution. Place {% raw %}`{{custom_attribute.${custom_attribute_with_code}}}`{% endraw %} to display the unique code.

![]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_email_body.png %}){: style="max-width:75%;"}

When it's ready, you can see the code in your message preview.

![]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_email_preview.png %})

