---
nav_title: Creative Details
article_title: Creative Details
page_order: 1
layout: featured
guide_top_header: "Creative Details"
guide_top_text: "Get creative with Content Cards! But you should know some of the guidelines first! After all, you have to know the rules to break them! Check out the following individual message type's Creative Specs or the global Creative Details."
description: "Get creative with Content Cards! This reference article covers creative details such as image size recommendations and dismissal behavior across the three Content Card types."

guide_featured_title: "Message Type Creative Specs"
guide_featured_list:
- name: Classic
  link: /docs/user_guide/message_building_by_channel/content_cards/creative_details/#classic
  image: /assets/img/icon-classic-cc.png
- name: Captioned Image
  link: /docs/user_guide/message_building_by_channel/content_cards/creative_details/#captioned-image
  image: /assets/img/captioned-cc.png
- name: Banner
  link: /docs/user_guide/message_building_by_channel/content_cards/creative_details/#banner
  image: /assets/img/icon-banner-cc.png

channel:
  - content cards
tool: Media

---

## Content Card types

### Classic

The classic card is great for standard messaging and notifications or even visually categorizing messages with icons. The image is optional, but it must be at a 1:1 ratio.  

![Image of a classic card with recommended details and a classic card example][1]{: height="50%" width="50%"}

| Card Capability | Details |
| --- | ---|
| Header Text | 18px; Bolded <br> One line of text is ideal. <br> You may use Liquid here to personalize your message. |
| Message Text | 13px; Regular Weight <br> Two to four lines of text is ideal. <br> You may use Liquid here to personalize your message. |
| Link Text | Optional. <br> 13px <br> Link to webpage or deep link to within  your app. |
| Image | Optional. <br> Must be 1:1 ratio. <br> We recommend an image quality of 60px by 60px. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### Captioned image

The Captioned Image card is a great way to show off and attract attention to important content, like a big sale or a new app feature!

![Image of a Captioned Image card with recommended details and a Captioned Image card example][2]{: height="50%" width="50%"}

| Card Capability | Details |
| --- | ---|
| Header Text | 18px; Bolded <br> One line of text is ideal. <br> You may use Liquid here to personalize your message. |
| Message Text | 13px; Regular Weight <br> Two to four lines of text is ideal. <br> You may use Liquid here to personalize your message. |
| Link Text | Optional. <br> 13px <br> Link to webpage or deep link to within your app. |
| Image | Suggested be 4:3 ratio. <br> 600px minimum width.  <br> Supports hi-res PNG, JPEG, and GIF. |
{: .reset-td-br-1 .reset-td-br-2}

### Banner

If you want fancy, the banner card is for you! this is completely custom to what you want it to be. Just create your content elsewhere and upload it for a beautiful card that's all your own.

![Image of a banner with recommended details and a banner example][3]{: height="50%" width="50%"}

| Card Capability | Details |
| --- | ---|
| Linked Card | Optional. <br> 13px <br> On-click behavior link to a webpage or a deep link to within  your app. |
| Image | Any aspect ratio supported. <br> 600px minimum width.  <br> Supports hi-res PNG, JPEG, and GIF. |
{: .reset-td-br-1 .reset-td-br-2}

## Creative details {#general}

Content Cards come with great out-of-the-box functionality. At this time, card styling cannot be done natively in your Braze account, but you can style your Content Card by type and the Content Card feed during integration. Refer to [Customizing Content Cards][4] for more information.

### Dismissal behavior

For a user to dismiss a card, they can either swipe it away on mobile, or use a `close X` function, as shown in the following screenshot. The `x` will appear on hover for the Web SDK only.

![Image that shows swipe or close dismissal behaviors for a card][5]{: height="70%" width="70%"}

If a user has dismissed all of their cards or you haven't pushed out any new updates, the user's feed will usually look something like this:

![Image of an empty Content Card feed][6]{: height="50%" width="50%"}

### Using GIFs in Content Cards

| Content Cards for Android | Content Cards for iOS | Content Cards for Web |
| --- | --- |---|
| [Install Custom Image Library.]({{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/customization/gifs/) | Included in integration. | Included in Integration. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

<br><br>

[1]: {% image_buster /assets/img/classic-cc.png %}
[2]: {% image_buster /assets/img/captioned-image-cc.png %}
[3]: {% image_buster /assets/img/banner-cc.png %}
[4]: {{site.baseurl}}/user_guide/message_building_by_channel/content_cards/customize/
[5]: {% image_buster /assets/img/dismissal-cc.png %}
[6]: {% image_buster /assets/img/empty-cc.png %}
