---
nav_title: Distributions with Custom Attributes
article_title: Distributions with Custom Attributes
page_order: 3
alias: /partners/voucherify/custom_attributes/
description: "This article outlines Braze integration with Voucherify. Braze integration enables you to send Voucherify codes in your Braze messages. This tutorial will show you how to send unique coupons, gift cards, loyalty, and referral codes to your Braze users."
page_type: partner
search_tag: Partner
---

# Distributions with Custom Attributes

> Braze integration enables you to send Voucherify codes in your Braze messages. In this tutorial, we are going to show you how to send unique coupons, gift cards, loyalty, and referral codes to your Braze users. Voucherify enables you to use [Braze's Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/), [Braze's Custom Attributes]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/), or Braze's [Promo Codes Snippet]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes/) to push codes from Voucherify to Braze. In this tutorial we will show you how to use Braze's Custom Attributes with Voucherify distributions.

{% alert tip %}

**Before you start**

Before you use Braze custom attributes in Voucherify distributions, you need to add your Braze users to the Voucherify dashboard. You can use Braze connected content to synchronize users or import your customers through CSV or API. [Go here](https://support.voucherify.io/article/67-how-to-import-my-customers) to read more about customer import.
{% endalert %}

## Contents

- [How does it work?](#how-does-it-work)
- [**Step 1:** Connect Voucherify to Braze](#step-1-connecting-voucherify-account-to-braze)
- [**Step 2:** Distribute Codes](#step-2-code-distribution)
- [**Step 3:** Use Voucherify custom attributes in your Braze campaign](#step-3-use-voucherify-custom-attributes-in-your-braze-campaign)

---

## How does it work?

Braze Custom Attributes enable you to assign Voucherify codes to custom attributes in user profiles in Braze. You can use unique coupons, gift cards, loyalty cards and referral codes. First, connect Voucherify with Braze, then create a distribution in Voucherify and finally create a campaign in Braze with the custom attribute snippet in your message template.

## Step 1: Connecting Voucherify account to Braze

First, connect your Voucherify account with Braze.

1.  Copy the REST API Key from your Braze account (it should at least have a permission 'users.track')  
    
    ![Braze REST API Key Settings]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_API_key.png %}){: style="margin-top:15px;margin-left:25px;margin-bottom:15px;"}
    
2.  Go to the **Integrations** directory in your Voucherify dashboard, find Braze and choose **Connect.**  
    
    ![Connect Braze Integration]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_integrations.png %}){: style="margin-top:15px;margin-left:25px;margin-bottom:15px;"}
    
3.  Paste the copied API Key from Braze and choose **Connect**:  
    
    ![API key]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_enter_API_key.png %}){: style="max-width:60%;margin-top:15px;margin-left:25px;margin-bottom:15px;"}
    
---

## Step 2: Code distribution

When connected, you can start a new Voucherify [distribution](https://support.voucherify.io/article/19-how-does-the-distribution-manager-work) that assigns a code to the custom attribute in the user profile in Braze. Later on, you can use received attributes with codes in your Braze campaigns.

Please note that before setting up distribution, you need to add your Braze users to the Voucherify dashboard. [Go here to read more.](https://support.voucherify.io/article/67-how-to-import-my-customers)

![Create distribution in Voucherify]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_distribution.png %})

You can distribute codes to Braze using two modes:

- **manual mode** or
- define an **automated workflow** that triggers code delivery in response to an action taken by your users.

In both manual and automatic modes, Voucherify sends unique codes with their attributes and assigns them to Braze Custom Attributes in users' profiles.

![Map fields to custom attributes]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_fields_mapping.png %})

---

{% tabs %}
{% tab Manual Message %}

### Manual distribution

Manual mode works as a one-time action that assigns codes to a chosen audience. Go to the Distributions in your dashboard and run the Distribution Manager with the plus. ![Plus]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_plus.png %}){: style="display: inline;width: 40px;padding: 0px 0px 0px;vertical-align:bottom;margin: 0px 0px 0px;"}

Choose **Manual Message**.

![Manual Message]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_manual_message.png %}){: style="max-width:40%;margin-top:15px;margin-left:25px;margin-bottom:15px;"}

1.  Name your distribution.

    ![Name your distribution]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_name_distribution.png %}){: style="max-width:90%;margin-top:15px;margin-bottom:15px;"}<br>  
    
    Choose a campaign that will be a source of unique codes **(1)** and select a segment of users or a single customer as your receivers **(2)**. Read more about customer segments [here](https://support.voucherify.io/article/51-customer-segments).  
    
    ![Choose campaign and users]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_name_distribution_choose_segment.png %}){: style="max-width:90%;margin-top:15px;margin-bottom:15px;"}  

2.  Go to the **Next step** to add marketing permissions. If you don't collect permissions from your audience, disable the consents verification.  
    
    ![Set marketing permissions]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_consents.png %}){: style="max-width:90%;margin-top:15px;margin-bottom:15px;"}  
    
3.  In the **Next step**, choose Braze as a channel and map custom fields that will be added to the user profile in Braze. You need to add the field representing the *code of the published voucher*; the rest of the fields are optional.  
    
    ![Choose and set up Braze channel]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_channel.png %}){: style="max-width:90%;margin-top:15px;margin-bottom:15px;"}  
    
4.  Choose **Next step** to see a summary of the distribution. Click **Save and send** to deliver codes to user profiles in Braze.  

_Note that all manual distributions are sent with a 10 minute delay._

---

{% endtab %}
{% tab Automatic Workflow %}

### Automatic workflow

Voucherify can push codes to Braze automatically in response to the following triggers:

- **Customer entered/left specific Voucherify segment**
- **Successful code publish** – the message is sent once the code from a campaign is published (assigned) to a customer in Voucherify.
- **Order status changed** (order created, order update, order has been paid, order canceled)
- **Gift credits added** – the message is sent once gift card credits are added to the customer's card.
- **Loyalty points added** – the message is sent once loyalty points are added to the customer's profile.
- **Voucher redeemed** – the message is sent to customers who successfully redeemed vouchers.
- **Voucher redemption rollback** – the message is sent to the customer whose redemption was successfully rolled back.
- **Reward redemption** – the message is sent when a customer redeems a loyalty or referral reward.
- **Custom event was logged for a customer** - the message is triggered once Voucherify logs a particular custom event.

To set up an automatic workflow with Braze and Voucherify, [visit distributions tutorial](https://support.voucherify.io/article/19-how-does-the-distribution-manager-work).

{% endtab %}
{% endtabs %}

---

## Step 3: Use Voucherify custom attributes in your Braze campaign

![Custom Attributes Code]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_code.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

Once the custom attribute with the code is added to the customer's custom attributes in Braze, you can use it in your Braze campaigns.

Edit the message body and add the custom attribute defined in the Voucherify distribution. Place {% raw %}`{{custom_attribute.${custom_attribute_with_code}}}`{% endraw %} to display the unique code.

![Braze email snippet]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_email_body.png %}){: style="max-width:75%;"}

When it's ready, you can see the code in your message preview.

![Braze email example]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_email_preview.png %})
