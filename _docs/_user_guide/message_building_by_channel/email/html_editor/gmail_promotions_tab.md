---
nav_title: Gmail promotions setup
article_title: Gmail Promotions Setup
page_order: 8
description: "This reference article covers how to use Braze to help you build the Gmail mobile promotions card from your email campaign."
channel:
  - email
toc_headers: h2
---

# Gmail Promotion setup

> The [Gmail mobile Promotions tab](https://developers.google.com/gmail/promotab/) allows marketers to send more information via annotations in a "card" rather than just the subject line or preheader information. Braze has a built-in tool to help you build the card from your email campaign.

## Prerequisite

First, forward your domains and subdomains to Google’s Promotions Tab outreach team at <a href="mailto:p-promo-outreach@google.com">p-promo-outreach@google.com</a> to be added to Gmail’s allowlist. This allows you to use any feature that shows rich imagery, such as the product carousel for the Gmail Promotions tab.

## Building the card with Braze

Follow these steps to build a Gmail promotion card for an email campaign. Note that navigating away from the **Content** section in the editor will reset the fields and information in the **Gmail Promotion** tab. Complete the setup of your promotion card, and copy the HTML generated so you don't lose your HTML code.

### Step 1: Create an email campaign

First, [create your email campaign]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/creating_an_email_campaign/), and select the **HTML code editor** as your editing experience.

### Step 2: Add details to Gmail Promotion card

Next, go to the **Content** section of the HTML editor and select the **Gmail Promotion** tab. Fill out the fields under **Basic Information**, then select **Generate HTML Code**. This will help generate the script for your Gmail Promo Tab card under the **Copy and Paste HTML code into `<Head>`** section.

![An example of how to build a card.]({% image_buster /assets/img/create-gmail-promo.png %})

### Step 3: Customize your Gmail Promotion card

Choose whether to include a discount offer, deal card, promotion card, or all options for your Gmail Promotion card.

{% tabs %}
{% tab Discount offer %}

Setting up a discount offer allows you to specify the valid dates for a discount. 

1. Select the **Discount Offer** toggle.
2. For **Offer**, enter a short summary for the discount. An example is "20% off".
3. For **Code**, add the promotion code that a user needs to apply at checkout.
4. Then, select the start date and time for the discount offer.
5. Determine if the discount offer should end at a specific time or never end.

![Options to specify the offer value, code, and start date and time for a discount offer.]({% image_buster /assets/img/gmail_promo_discount_details.png %}){: style="max-width:70%;"}

{% endtab %}
{% tab Deal Cards %}

Use Deal Cards to provide key deal information directly at the top of email bodies. This allows recipients to quickly understand the offer details and take action. For example, you can use Deal Cards to promote limited-time offers and reduce the need for users to search for details within emails.

1. Select the **Deal Card** toggle.
2. For **Offer**, enter a short summary for the discount. An example is "20% off all shoes".
3. (optional) For **Code**, add the promotion code that a user needs to apply at checkout.
4. Enter at least one of the following URLs. 
-  **Offer Page URL:** The URL for the specific offer landing page. This creates a "Shop now" (or similar) button. We recommend providing this URL for your Deal Card. 
- **Merchant Homepage URL:** The URL for your main homepage. Use this field only if a specific offer page URL isn't available.
5. (optional) Add a start date for the offer.
6. Determine if the offer should end at a specific time or never end.

![Options to specify the offer value, code, and start date and time for a Deal Card.]({% image_buster /assets/img/gmail_promo_deal_cards.png %}){: style="max-width:70%;"}

{% endtab %}
{% tab Promotion cards %}

Promotion cards in your product carousel are helpful to provide images to your offer. You can also customize variables in your product carousel and include up to ten image previews, where each image is unique.

1. Select the **Promotion Cards** toggle.
2. Select **Add promotion card**. Each image in your product carousel must have a unique URL and use the same aspect ratio (4:5, 1:1, 1.91:1).
3. Include an image URL.
4. For **Target URL**, add the link for your promotion.

{% alert tip %}
We recommend uploading your product images to the media library, then copying and pasting the URLs into the appropriate fields. Only static image formats (PNG and JPEG) are accepted. Some image formats (GIF) will upload but not display as expected.
{% endalert %}

{: start="5"}
5. Customize your promotion card by adding a headline, currency, price, and discount value.

| Customizable property | Description |
|---|---|
| Headline | (optional) One or two sentence description for the promotion. Displays under the preview image. |
| Currency | (optional) The currency of the price. |
| Price | The price of the promotion. |
| Discount Value | The amount discounted from the original price. | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![An example of a product carousel from a company named Motto with the email heading "Our best-selling socks are on sale", with three images of socks and their discounted prices.]({% image_buster /assets/img_archive/product_carousel.png %}){: style="max-width:40%;"}

{% endtab %}
{% endtabs %}

### Step 4: Generate and paste HTML code

After building your Gmail Promotion card, select **Generate HTML code**. Copy and paste the script into the `<head>` element of your email's HTML. 

{% alert tip %}
For the drag-and-drop editor, copy and paste the generated HTML code into the [custom head tags]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/overview/#custom-head-tags) section under **Sending Settings**.
{% endalert %}

{% alert warning %}
The Promotions script only appears if your email lands in the Gmail Promotions tab. Currently, Gmail uses algorithms to determine where your email will land. However, if a user ever marks your email as a promotion, Gmail's algorithm will be ignored, and your email will automatically land in the Promotions tab moving forward.
{% endalert %}

## Best practices

In general, adhere to these [best practices recommended by Gmail](https://developers.google.com/gmail/promotab/best-practices). 

{% alert tip %}
While you can use Liquid within this script, we strongly suggest that you test your messaging as much as possible to avoid an error.
{% endalert %}

## Measuring Gmail Cards

Gmail does not return analytics on these cards, and email service providers (ESPs) like Braze cannot insert their own link tracking on links in the header section (including promotion cards and product carousels). However, you can append UTM parameters or unique codes to the URLs during setup. These parameters allow you to track engagement using your own website analytics or conversion tracking, because the tracking is part of the URL itself—not inserted by the ESP. ESP-level click tracking is not available for these links.

### Incorporate images

Gmail has seen better results with strong imagery related to the email message. Gmail does not recommend using a text-only design, as this space was designed to bring visual language, which is vital to email marketing, to the preview. Don't use images with cut-off text or repeat images in multiple campaigns.

### Describe offers

Gmail does not suggest using sentences or phrases, such as "You Can Buy 1 Get 1 Free or Discounts on All Shorts and Shirts", as it may clip, no longer draw the eye, and compete with the subject line. This space should only be used to engage your customers with your messaging, so avoid any language similar to "Open this email now" or "Click here for deals". It's best to avoid repeating your subject line.

## Frequently asked questions

### Why is my promotional message not displaying the promotion card or product carousel in the end user's inbox?

There are many factors that determine whether the product carousel will be shown in the Gmail Promotions tab.

All images in the annotation still have to pass a quality filter. In order for the product carousel to populate, all images in the annotation must be in the recommended image aspect ratio and be high-quality, high-resolution close-up product images. The images should contain little to no text. The quality filter also filters inappropriate content, so the images must be family, user, and child-friendly.

Furthermore, Gmail has a density cap on how many product carousels appear in a user’s Gmail Promotions tab. For instance, if a user subscribes to a lot of brands that use product carousels in their promotion email, Gmail eventually puts a cap on how many product carousels are shown.

Due to Google's privacy and safety regulations, emails with annotations must be widely sent for the annotation to work. It's recommended to launch a campaign and send it to at least 100 recipients for Google's system to detect it as a "mass send." Image URLs may not vary across recipients.

### How are clicks on a promotion card or product carousel tracked?

Braze or any other ESPs are not able to insert link tracking on links in the header section. This means clicks cannot be tracked on a promotion card or product carousel.

### Is there a way to see how many users received a product carousel?

Gmail determines when and who to display the card to, so there isn't a guarantee that every recipient will see the product carousel.

### Why don't I see annotations in my Gmail Promotions tab?

Annotations aren't supported for Google Workspace. To preview annotations, you can create a personal email address with Gmail.

Note that annotations don't render in the **Primary** tab or in any other tab in the Gmail mobile app. Annotations won't display after a user opens an email or if you're using the `DiscountOffer` annotation type and the time and date have already expired.
