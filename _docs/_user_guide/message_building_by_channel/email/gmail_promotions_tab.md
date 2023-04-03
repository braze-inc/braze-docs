---
nav_title: Gmail Promotions Setup
article_title: Gmail Promotions Setup
page_order: 8
description: "This reference article covers how to use Braze to help you build the Gmail mobile promotions card from your email campaign."
channel:
  - email

---

# Gmail Promotion setup

> The [Gmail mobile Promotions tab][1] allows marketers to send more information via annotations in a "card" rather than just the subject line or pre-header information. Braze has a built-in tool to help you build the card from your email campaign.

## Building the card with Braze

1. [Create your email campaign][7] as you usually would. 
2. Go to the **Content Library** section and select the **Gmail Promotion Setup** tab.
3. Fill out the fields under **Basic Information**. This will help generate the script for your Gmail Promo Tab card under the **Copy and Paste HTML code into `<Head>`** section. <br> ![An example of how to build a card.][2]
4. Choose whether to include discount offers or promotion cards for your Gmail Promotion card.
5. Copy and paste the script into the `<head>` element of your email's HTML.

{% alert warning %}
The Promotions script will only appear if your email lands in the Gmail **Promotions Tab**. Currently, Gmail uses algorithms to determine where your email will land. However, if a user ever marks your email as a promotion, Gmail's algorithm would be ignored, and your email will automatically land in the **Promotions Tab** moving forward.
{% endalert %}

### Customize your card

You can customize many variables for your card, which will map to the following locations shown in the card layout.

![Card layout that maps out the parameters for the company logo, sender, subject line, discount offer and discount code, and related images.][4]

| Customizable Variable | Description |
|---|---|
| Company Logo | Logos should be a square or circle shape and uploaded in `https`, not `http`.|
| Product Image (Single Image Preview) | This is a blank canvas for bringing in product or lifestyle images. In Gmail's preview, they show a sample image that is "`538x138` "with a "`3.9` "aspect ratio. |
| Discount Offer (Deal Badge) | One or two words used to quickly highlight an offer or as a call to action, such as "Free Gift", "2 for 1", or "Limited Offer." |
| Discount Code (Promotion Code) | Use your regular promo code. Only use if there is a promo code. |
| Expiration Date | The start date should be when your email sends, or the promotion starts (if this date is in the future, your email **will not populate** in a bundle). The end date should only be used if you have an expiring offer, and the date needs to be in the future. Old or past-due expiration dates will cause our system to see the offer as stale and will not preview your email. |
{: .reset-td-br-1 .reset-td-br-2}

{% alert tip %}
We recommend uploading your logo and product image to the Braze Media Library, then copy and pasting the URLs into the appropriate fields. Only static image formats (PNG and JPEG), are accepted. Some image formats (GIF) will upload but not display as expected.
{% endalert %}

### Best practices

In addition to adhering to these best practices recommended by Gmail, you can also see what you cards look like with their [Preview your annotations tool][5].

{% alert important %}
While you can use Liquid within this script, we strongly suggest that you test your messaging as much as possible to avoid an error.
{% endalert %}

![An example of what your preview may look like when testing on the Gmail site.][6]

#### Incorporating images

Gmail has seen better results with strong imagery related to the email message. Gmail does not recommend using a text-only design, as this space was designed to bring that visual language, vital to email marketing, to the preview. Don't use images with cut-off text or repeat images in multiple campaigns.

#### Describing offers

Gmail does not suggest using sentences or phrases, such as "You Can Buy 1 Get 1 Free or Discounts on All Shorts and Shirts", as it may clip, no longer draw the eye, and compete with the subject line. This space should only be used to engage your customers with your messaging, so avoid any language similar to "Open this email now" or "Click here for deals". It's best to avoid repeating your subject line.

[1]: https://developers.google.com/gmail/promotab/
[2]: {% image_buster /assets/img/create-gmail-promo.png %}
[3]: {% image_buster /assets/img/copy-gmail-promo-script.png %}
[4]: {% image_buster /assets/img/promocardmap.png %}
[5]: https://developers.google.com/gmail/promotab/overview#preview_your_annotations
[6]: {% image_buster /assets/img/gmail_preview.png %}
[7]: {{site.baseurl}}/user_guide/message_building_by_channel/email/creating_an_email_campaign/
