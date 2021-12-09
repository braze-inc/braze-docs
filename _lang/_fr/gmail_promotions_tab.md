---
nav_title: Gmail Promotions Tab
article_title: Gmail Promotions Tab
page_order: 7
description: "Gmail has updated the mobile Promotions tab to allow marketers to send more information via annotations in a 'card'. This article covers how to use Braze to help you build the card from our product."
channel:
  - email
---

# Gmail Promotion tool

Gmail has updated [the mobile Promotions tab][1] to allow marketers to send more information via annotations in a "card" rather than just the subject line or pre-header information. Braze has built a tool to help you build the card from our product.

## Building the card with Braze

Building the card in Braze is easy!

First, create your email campaign, as you normally would. Then, as you're editing the content of your email, click the **Gmail Promo** tab. Here, you'll be able to fill out fields that will generate the script for your Gmail Promo Tab card.

!\[Build Your Card\]\[2\]

After you've finished filling out the fields, you'll see a completed script at the bottom of your editor. Copy and paste it into the "`<head>` "section/element of your email's `HTML`.

!\[Copy Your Script\]\[3\]

{% alert warning %}

The Promotions script will only appear if your email lands in the Gmail **Promotions Tab**. Currently, Gmail uses algorithms to determine where your email will land. However, if a user ever marks your email as a promotion, Gmail's algorithm would be ignored, and your email will automatically land in the **Promotions Tab** moving forward.

{% endalert %}

### Customize your card

You can customize many variables for your card, which will map to the locations shown in the card layout below.

!\[Promo Card Map\]\[4\]

| Customizable Variable                | Description                                                                                                                                                                                                                                                                                                                                                                     |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Company Logo                         | Logos should be a square or circle shape and should be uploaded in "`https` ", not "`http` ".                                                                                                                                                                                                                                                                                   |
| Product Image (Single Image Preview) | This is a blank Canvas for you to bring in product or lifestyle images. In Gmail's preview, they show a sample image that is "`538x138` "with a "`3.9` "aspect ratio.                                                                                                                                                                                                           |
| Discount Offer (Green Deal Badge)    | One or two words used to quickly highlight an offer or as a call to action, such as "Free Gift", "2 for 1", or "Limited Offer."                                                                                                                                                                                                                                                 |
| Discount Code (Promo Code)           | Use your regular promo code. Only use if there is a promo code.                                                                                                                                                                                                                                                                                                                 |
| Expiration Date                      | The start date should be when your email sends or the promotion starts (if this date is in the future, your email __will not populate__ in a bundle). The end date should only be used if you have an expiring offer, and the date needs to be in the future. Old or past-due expiration dates will cause our system to see the offer as stale and will not preview your email. |
{: .reset-td-br-1 .reset-td-br-2}

{% alert tip %}
We recommend that you upload your logo and product image to the Braze Media Library, then copy and paste the URLs from there into the appropriate fields. Only static image formats like `.png` and `.jpeg` are accepted. Some image formats, like `.gif`, will upload but not act as expected.
{% endalert %}

{% alert warning %}
While you can use Liquid within this script, we strongly suggest that you test as much as possible to avoid an error.
{% endalert %}

### Best practices

In addition to adhering to the following best practices recommended by Gmail, you can use their [Preview Your Annotations][5] tool to see what their cards look like.

#### Product image

Gmail has seen better results with strong imagery related to the email message. Gmail does not recommend using a text-only design, as this space was designed to bring that visual language, vital to email marketing, to the preview. Don't use images with cut-off text or repeat images in multiple campaigns.

#### Discount offer

Gmail does not suggest using sentences or phrases, such as "You Can Buy 1 Get 1 Free or Discounts on All Shorts and Shirts", as it may clip, no longer draw the eye, and compete with the subject line. Again, this space should only be used for your messaging to engage your customers with your email, so avoid any language around "Open this email now" or "Click here for deals". Do not repeat your subject line.
[2]: {% image_buster /assets/img/create-gmail-promo.gif %} [3]: {% image_buster /assets/img/copy-gmail-promo-script.gif %} [4]: {% image_buster /assets/img/promocardmap.png %}

[1]: https://developers.google.com/gmail/promotab/
[5]: https://developers.google.com/gmail/promotab/overview#preview_your_annotations
