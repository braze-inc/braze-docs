---
nav_title: IAM Studio
article_title: IAM Studio
description: "This reference article outlines the partnership between Braze and IAM Studio, a message personalization platform which allows you to create personalized, rich in-app experiences and deliver them through Braze."
alias: /partners/iam_studio/
page_type: partner
search_tag: Partner

---

# IAM Studio

> [IAM Studio](https://www.inappmessage.com) is a no-code message personalization platform that allows you to create personalized, rich in-app experiences and deliver them through Braze.

_This integration is maintained by IAM Studio.\*s._

## About the integration

With the Braze and IAM Studio integration, you can easily insert customizable in-app message templates into your Braze in-app messages, offering image replacement, text modification, deep link settings, custom attributes, and event settings. Using IAM Studio, you can reduce message production time and dedicate more time to content planning. 

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| IAM Studio account | A [IAM Studio account](https://www.inappmessage.com/register) is required to take advantage of this partnership. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Use cases

- Encouraging the purchase of goods
- User information collection
- Increasing membership registration
- Coupon issuance information

## Integration

### Step 1: Choose a template

Choose an in-app message template you want to use from the in-app message template gallery

![The IAM Studio template gallery shows different templates such as "carousel slide modal", "simple icon modal", "modal full image", and more.]({% image_buster /assets/img/iam_studio/iam_template_gallery.png %})

### Step 2: Customize the template

First, customize the image, text, and button for your content. Be sure to connect **Deeplink** for the image and button.

{% tabs local %}
{% tab Image %}
![The IAM Studio UI showing the options to customize the image. These options include the image, image radius, and image dimmed.]({% image_buster /assets/img/iam_studio/iam_customize_image.png %})
{% endtab %}
{% tab Text %}
![The IAM Studio UI showing the options to customize the title and subtitle of your message. These options include text, formatting, and font.]({% image_buster /assets/img/iam_studio/iam_customize_text.png %})
{% endtab %}
{% tab Button %}
![The IAM Studio UI showing the options to customize the main, left and right button. These options include color, deep link, text, and formatting.]({% image_buster /assets/img/iam_studio/iam_customize_button.png %})
{% endtab %}
{% endtabs %}

Next, create your personalized in-app message by adding custom fonts and using Liquid tags. To enable logging and tracking, select **Log data and track user behavior**.

{% tabs local %}
{% tab Fonts %}
![The IAM Studio UI showing the options to add Liquid. These options include making personalized sentence.]({% image_buster /assets/img/iam_studio/iam_custom_font.png %})
{% endtab %}
{% tab Liquid %}
![The IAM Studio UI showing the options to customize event/attribute logging. These options include that user behavior log.]({% image_buster /assets/img/iam_studio/iam_liquid.png %})
{% endtab %}
{% tab Logging and Tracking %}
![The IAM Studio UI showing the options to customize font. These options include that user can customize font style.]({% image_buster /assets/img/iam_studio/iam_tracking_logging.png %})
{% endtab %}
{% endtabs %}

### Step 3: Export the template

Once all editing has been completed, export the template by clicking **Export**. After exporting, the in-app message HTML code will be generated. Copy this code by clicking the **Copy code** button. 

![]({% image_buster /assets/img/iam_studio/export_iam_code.png %}){: style="max-width:45%;"}

### Step 4: Use code in Braze 

Navigate to Braze, and in your in-app message, paste the custom code in the **HTML Input** box. Make sure to test your message to check it is displaying correctly.

![]({% image_buster /assets/img/iam_studio/braze_campaign_editor.png %}){: style="max-width:85%;"}


