---
nav_title: Gmail promotions setup
article_title: Gmail Promotions Setup
page_order: 8
description: "This reference article covers how to use Braze to help you build the Gmail mobile promotions card from your email campaign."
channel:
  - email

---

# Gmail Promotion setup

> The [Gmail mobile Promotions tab](https://developers.google.com/gmail/promotab/) allows marketers to send more information via annotations in a "card" rather than just the subject line or preheader information. Braze has a built-in tool to help you build the card from your email campaign.

## Prerequisite

First, forward your domains and subdomains to Google’s Promotions Tab outreach team at <a href="mailto:p-promo-outreach@google.com">p-promo-outreach@google.com</a> to be added to Gmail’s allowlist. This allows you to use any feature that shows rich imagery, such as the product carousel for the Gmail Promotions tab.

## Building the card with Braze

Follow these steps to build a Gmail promotion card for an email campaign. Note that navigating away from the **Content** section in the editor will reset the fields and information in the **Gmail Promotion** tab. Complete the setup of your promotion card, and copy the HTML generated so you don't lose your HTML code.

1. [Create your email campaign]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/creating_an_email_campaign/), and select the **HTML Editor** as your editing experience.
2. Go to the **Content** section in the HTML editor, and select the **Gmail Promotion** tab.
3. Fill out the fields under **Basic Information**, then click **Generate HTML Code**. This will help generate the script for your Gmail Promo Tab card under the **Copy and Paste HTML code into `<Head>`** section. <br> ![An example of how to build a card.]({% image_buster /assets/img/create-gmail-promo.png %})
4. Choose whether to include only a discount offer, promotion cards, or both for your Gmail Promotion card. <br> ![Options to include a discount offer and promotion cards.]({% image_buster /assets/img_archive/gmail_promo_discount.png %}){: style="max-width:70%;"}
5. Copy and paste the script into the `<head>` element of your email's HTML.

{% alert warning %}
The Promotions script only appears if your email lands in the Gmail Promotions tab. Currently, Gmail uses algorithms to determine where your email will land. However, if a user ever marks your email as a promotion, Gmail's algorithm will be ignored, and your email will automatically land in the Promotions tab moving forward.
{% endalert %}

### Including a discount offer

Setting up a discount offer allows you to specify the valid dates for a discount. After determining your discount offer, select a start date and time. You have the option of ending your discount offer at a specific time, or selecting to never end it.

![Options to specify the offer value, code, and start date and time for a discount offer.]({% image_buster /assets/img/gmail_promo_discount_details.png %}){: style="max-width:70%;"}

### Customizing your product carousel

Promotion cards in your product carousel are helpful to provide images to your offer. You can also customize variables in your product carousel and include up to ten image previews, where each image is unique.

![An example of a product carousel from a company named Motto with the email heading "Our best selling socks are on sale", with three images of socks and their discounted prices.]({% image_buster /assets/img_archive/product_carousel.png %}){: style="max-width:40%;"}

| Customizable Variable | Description |
|---|---|
| Image URL | The URL to your image. Each image in your product carousel must have a unique URL and use the same aspect ratio (4:5, 1:1, 1.91:1). |
| Target URL | The link for your promotion. |
| Headline | (optional) One or two sentence description for the promotion. Displays under the preview image. |
| Currency | (optional) The currency of the price. |
| Price | The price of the promotion. |
| Discount Value | The amount discounted from the original price. | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert tip %}
We recommend uploading your product images to the media library, then copy and pasting the URLs into the appropriate fields. Only static image formats (PNG and JPEG), are accepted. Some image formats (GIF) will upload but not display as expected.
{% endalert %}

### Best practices

In general, adhere to these [best practices recommended by Gmail](https://developers.google.com/gmail/promotab/best-practices). 

{% alert tip %}
While you can use Liquid within this script, we strongly suggest that you test your messaging as much as possible to avoid an error.
{% endalert %}

#### Incorporating images

Gmail has seen better results with strong imagery related to the email message. Gmail does not recommend using a text-only design, as this space was designed to bring visual language, which is vital to email marketing, to the preview. Don't use images with cut-off text or repeat images in multiple campaigns.

#### Describing offers

Gmail does not suggest using sentences or phrases, such as "You Can Buy 1 Get 1 Free or Discounts on All Shorts and Shirts", as it may clip, no longer draw the eye, and compete with the subject line. This space should only be used to engage your customers with your messaging, so avoid any language similar to "Open this email now" or "Click here for deals". It's best to avoid repeating your subject line.

## Frequently asked questions

### Why is my promotional message not displaying the promotion card or product carousel in the end user's inbox?

There are many factors that determine whether product carousel will be shown in the Gmail Promotion tab.

All images in the annotation still have to pass a quality filter. In order for product carousel to populate, it's crucial that all images in the annotation are in the recommended image aspect ratio, high quality or high resolution close-up product images. The images should contain little to no text (preferable). The quality filter also filters inappropriate content, so the images must be family, user, and child-friendly.

Furthermore, Gmail has a density cap on how many product carousels appear in a user’s Gmail Promotion tab. For instance, if a user subscribes to a lot of brands that use product carousel in their promotion email, Gmail eventually puts a cap on how many product carousels are shown.

Due to Google's privacy and safety regulations, emails with annotations must be widely sent for the annotation to work. It's recommend to launch a campaign and send it to at least 100 recipients for Google's system to detect it as a "mass send." Image URLs may not vary across recipients.

### How are clicks on a promotion card or product carousel tracked?

Braze or any other ESPs are not able to insert link tracking on links in the header section. This means clicks cannot be tracked on a promotion card or product carousel.

### Is there a way to see how many users received a product carousel?

Gmail determines when and who to display the card to, so there isn't a guarantee that every recipient will see the product carousel.

