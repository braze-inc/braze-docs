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

### Include a discount offer

Setting up a discount offer allows you to specify the valid dates for a discount. After determining your discount offer, select a start date and time. You'll have the option of ending your discount offer at a specific time, or selecting to never end it.

### Customize your product carousel

Promotion cards in your product carousel are helpful to provide images to your offer. You can also customize variables in your product carousel and include up to 10 image previews, where each image is unique.

| Customizable Variable | Description |
|---|---|
| Image URL | The URL to your image. Each image in your produc carousel must have a unique URL and use the same aspect ratio (4:5, 1:1, 1.91:1). |
| Target URL | The link for your promotion. |
| Headline | (optional) One or two sentence description for the promotion. Displays under the preview image. |
| Currency | (optional) The currency of the price. |
| Price | The price of the promotion. |
| Discount Value | The amount discounted from the original price. | 
{: .reset-td-br-1 .reset-td-br-2}

{% alert tip %}
We recommend uploading your product images to the Braze Media Library, then copy and pasting the URLs into the appropriate fields. Only static image formats (PNG and JPEG), are accepted. Some image formats (GIF) will upload but not display as expected.
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

## Frequently asked questions

### Why is my promotional message not displaying the promotion card or product carousel in the end user's inbox?

There are many factors that determine whether product carousel will be shown in the Gmail Promotion Tab.

All images in the annotation still have to pass a quality filter. In order for product carousel to populate, it's crucial that all images in the annotation are in the recommended image aspect ratio, high quality or high resolution close-up product images. The images should contain little to no text (preferable). The quality filter also filters inappropriate content, so the images must be family, user, and child-friendly.

Furthermore, Gmail has a density cap on how many product carousels appear in a user’s Gmail Promotion tab. For instance, if a user subscribes to a lot of brands that use product carousel in their promotion email, Gmail eventually puts a cap on how many product carousels are shown. 

[1]: https://developers.google.com/gmail/promotab/
[2]: {% image_buster /assets/img/create-gmail-promo.png %}
[3]: {% image_buster /assets/img/copy-gmail-promo-script.png %}
[4]: {% image_buster /assets/img/promocardmap.png %}
[5]: https://developers.google.com/gmail/promotab/overview#preview_your_annotations
[6]: {% image_buster /assets/img/gmail_preview.png %}
[7]: {{site.baseurl}}/user_guide/message_building_by_channel/email/creating_an_email_campaign/
