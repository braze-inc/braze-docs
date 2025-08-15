---
nav_title: Creative details
article_title: Creative Details for Content Cards
page_order: 1
description: "This article covers creative details such as image size recommendations and dismissal behavior across the three standard Content Card types."
channel:
  - content cards
tool: Media

---

# Creative details for Content Cards

> Customizing Content Cards and the feed they are located in can't be done during the campaign creation process—you must work with your engineers and developers to build and customize your cards. For technical details, visit our [developer documentation]({{site.baseurl}}/developer_guide/getting_started/customization_overview).

## Content Card types

{% tabs %}
{% tab Classic %}

The classic card is great for standard messaging and notifications or even visually categorizing messages with icons. The image is optional, but it must be at a 1:1 ratio.

![Image of a classic card with recommended details and a classic card example]({% image_buster /assets/img/content_card_classic.png %}){: style="max-width:45%;border:0;"}

| Card Capability | Details |
| --- | ---|
| Header Text | 18px; Bolded <br> One line of text is ideal. <br> You may use Liquid here to personalize your message. |
| Message Text | 13px; Regular Weight <br> Two to four lines of text is ideal. <br> You may use Liquid here to personalize your message. |
| Link Text | Optional. <br> 13&nbsp;px <br> Link to web page or deep link to within  your app. |
| Image | Optional. <br> Must be 1:1 ratio. <br> We recommend an image quality of 60 x 60&nbsp;px. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Captioned Image %}

The Captioned Image card is a great way to show off and attract attention to important content, like a big sale or a new app feature.

![Image of a Captioned Image card with recommended details and a Captioned Image card example]({% image_buster /assets/img/content_card_captioned.png %}){: style="max-width:90%;border:0;"}

| Card Capability | Details |
| --- | ---|
| Header Text | 18px; Bolded <br> One line of text is ideal. <br> You may use Liquid here to personalize your message. |
| Message Text | 13px; Regular Weight <br> Two to four lines of text is ideal. <br> You may use Liquid here to personalize your message. |
| Link Text | Optional. <br> 13&nbsp;px <br> Link to web page or deep link to within your app. |
| Image | Suggested be 4:3 ratio. <br> 600&nbsp;px minimum width.  <br> Supports high-resolution PNG, JPEG, and GIF. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Image-only %}

If you want more creative control, the image-only card is for you. Create your image using any tooling you like and upload the image to this card type.

![Image of an image-only Content Card with recommended details and an image-only example]({% image_buster /assets/img/content_card_banner.png %}){: style="max-width:45%;border:0;"}

| Card Capability | Details |
| --- | ---|
| Linked Card | Optional. <br> 13&nbsp;px <br> On-click behavior link to a web page or a deep link to within your app. |
| Image | Any aspect ratio supported. <br> 600&nbsp;px minimum width.  <br> Supports high-resolution PNG, JPEG, and GIF. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

## Global creative details {#general}

Content Cards come with great functionality from the very beginning. At this time, card styling cannot be done natively in your Braze account, but you can style your Content Card by type and the Content Card feed during integration. Refer to [Customizing Content Cards]({{site.baseurl}}/developer_guide/content_cards/) for more information.

### Dismissal behavior

For a user to dismiss a card, they can either swipe it away on mobile, or use a `close X` function, as shown in the following screenshot. The `x` will appear on hover for the Web SDK only.

![Image that shows swipe or close dismissal behaviors for a card]({% image_buster /assets/img/dismissal-cc.png %})

If a user has dismissed all of their cards or you haven't pushed out any new updates, the user's feed will usually look something like this:

![Image of an empty Content Card feed]({% image_buster /assets/img/empty-cc.png %}){: style="max-width:45%"}

{% alert tip %}
Keep Content Cards relevant by setting them to dismiss when a user takes relevant actions. For example, set promotional Content Cards to be dismissed as soon as users make a purchase so they don't continue to see an offer for something they already bought.
{% endalert %}

### Using GIFs in Content Cards

| Content Cards for Android | Content Cards for iOS | Content Cards for Web |
| --- | --- |---|
| The Android SDK does not provide animated GIF support by default. For more details on activating GIF support, refer to [GIFs]({{site.baseurl}}/developer_guide/content_cards/embedding_gifs/?sdktab=android). | The Swift SDK does not provide animated GIF support by default. For more details on activating GIF support, refer to the [GIF support tutorial](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c3-gif-support). | GIF support is included by default in the Web SDK integration. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

<br><br>

