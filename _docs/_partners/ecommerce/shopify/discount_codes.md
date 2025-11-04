---
nav_title: Unique Discount Codes 
article_title: Sending Unique Discount Codes
alias: /shopify_discount_codes/
page_order: 7
description: "This reference article covers a community-submitted use case of using Braze promotion codes with the Shopify Bulk Discount Code Bot to send unique discount codes through your campaigns and Canvases."
---

# Sending unique discount codes through Shopify

> This community-submitted use case shows how to use Braze [promotion codes]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes/) with the Shopify Bulk Discount Code Bot to generate unique discount codes for your campaigns and Canvases. Unique discount codes help avoid the exploitation of generic promotion codes.

{% alert important %}
This is a community-submitted integration and isn’t directly supported by Braze. The Bulk Discount Code Bot is directly supported by Shopify. Only Braze promotion codes are supported by Braze. 
{% endalert %}

## Requirements

| Requirement | Description |
| --- | --- |
| Set up a Shopify store | Confirm you've already [set up a Shopify store with Braze]({{site.baseurl}}/shopify_overview/). |
| Install the Bulk Discount Code Bot app | Download the [Bulk Discount Code Bot](https://apps.shopify.com/bulk-discount-generator) app in the Shopify app store. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Generating unique discount codes

### Step 1: Configure your discount codes

Use the Bulk Discount Code Bot to configure your discount codes based on the number of codes to generate, code length, discount value, and more.

![The configuration options for a discount set.][1]

### Step 2: Export your codes

Find your discount set in the Bulk Discount Code Bot's search bar, then select **Export Codes** > **Download Codes** to download a CSV file to your Downloads folder.

![Search bar with a dropdown displaying the discount set and a row of buttons to select from.][2]{: style="max-width:70%;"}

In the CSV file, delete row 1 to remove the column header “Promo”. This will prevent "Promo" from becoming a discount code in Braze.

![A flowchart showing the removal of the row header "Promo" in a CSV file.][3]{: style="max-width:60%;"}

### Step 3: Add your discount codes to Braze

In Braze, go to **Data Settings** > **Promotion Codes** > **Create Promotion Code List** and [configure your discount codes list]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes/#creating-a-promotion-code-list). Make sure you match the expiration date that was configured by the Bulk Discounts Code Bot.

Then, upload your CSV file and select **Save List**.

### Step 4: Add your discount codes to a Braze campaign or Canvas step

If you want to use your unique discount codes in a single-send campaign, or you don't mind users receiving multiple unique codes across different campaigns or Canvas steps, copy the code's Liquid snippet from the promotion codes list you saved.

![A Liquid code snipppet with a button copy it.][4]{: style="max-width:60%;"}

Paste the Liquid snippet into a campaign or Canvas step. 

![A GIF showing the Liquid snippet being added to a Canvas step.][5]

If you want users to recieve a single unique discount code no matter how many times the discount code is referenced in campaigns or Canvases, create a [User Update]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/) step directly before the first Message step that assigns the discount code to a custom attribute, like "Promo Code".

{% alert tip %}
You can also [create a custom attribute]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/) by going to **Data Settings** > **Custom Attributes**.
{% endalert %}

In the User Update step, do the following for each field:
- **Attribute Name:** Select **Promo Code**.
- **Action:** Select **Update**.
- **Key Value:** Paste the Liquid code snippet.

![A User Update step that updates a "Promo Code" attribute with the Liquid snippet.][6]

Now, you can add the custom attribute {% raw %}`{{custom_attribute.${Promo Code}}}`{% endraw %} to any message, and the discount code will be templated in.

## Discount code behavior

{% details Multichannel campaign or Canvas step %}

When a discount code snippet is used in a multichannel campaign or Canvas step, users always receive a unique code. If a user is eligible to receive a code through more than one channel, they'll receive the same code through each channel. In other words, an eligible user would only receive one code across all the messages sent by that campaign or Canvas step.

{% enddetails %}

{% details Different Canvas steps or separate campaigns %}

When a discount code is referenced by multiple steps in the same Canvas or by separate campaigns, an eligible user will receive multiple unique promotion codes (one code for each Canvas step or campaign).

{% enddetails %}

[1]: {% image_buster /assets/img/Shopify/configure_discount_codes.png %}
[2]: {% image_buster /assets/img/Shopify/export_discount_codes.png %}
[3]: {% image_buster /assets/img/Shopify/edited_codes_csv.png %}
[4]: {% image_buster /assets/img/Shopify/liquid_code_snippet.png %}
[5]: {% image_buster /assets/img/Shopify/liquid_promo_code.gif %}
[6]: {% image_buster /assets/img/Shopify/user_update_step.png %}