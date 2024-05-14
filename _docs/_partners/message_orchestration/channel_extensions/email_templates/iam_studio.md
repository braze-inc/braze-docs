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

With the Braze and IAM Studio integration, you can easily insert customizable in-app message templates into your Braze in-app messages, offering image replacement, text modification, deep link settings, custom attributes, and event settings. Using IAM Studio, you can reduce message production time and dedicate more time to content planning. 

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| IAM Studio account | A [IAM Studio account](https://www.inappmessage.com/register) is required to take advantage of this partnership. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Use cases

- Encouraging the purchase of goods
- User information collection
- Increasing membership registration
- Coupon issuance information

## Integration

### Step 1: Choose a template

Choose an in-app message template you want to use from the in-app message template gallery

![The IAM Studio template gallery shows different templates such as "carousel slide modal", "simple icon modal", "modal full image", and more.][1]

### Step 2: Customize the template

#### Customize contents
Add the images and edit text, button with your desired content. Connect **Deeplink** on the image and button

{% tabs local %}
{% tab Customize Image %}
![The IAM Studio UI showing the options to customize the image. These options include the image, image radius, and image dimmed.]({% image_buster /assets/img/iam_studio/iam_customize_image.png %})
{% endtab %}
{% tab Customize Text %}
![The IAM Studio UI showing the options to customize the title and subtitle of your message. These options include text, formatting, and font.]({% image_buster /assets/img/iam_studio/iam_customize_text.png %})
{% endtab %}
{% tab Customize Button %}
![The IAM Studio UI showing the options to customize the main, left and right button. These options include color, deep link, text, and formatting.]({% image_buster /assets/img/iam_studio/iam_customize_button.png %})
{% endtab %}
{% endtabs %}

#### Improve in-app message
Strengthen your brand identity through **Custom font** and create personalized in-app message through **Liquid**. Set button and custom attribute•event to **log data and track user behavior**

{% tabs local %}
{% tab Custom Font %}
![The IAM Studio UI showing the options to add Liquid. These options include making personalized setence.]({% image_buster /assets/img/iam_studio/iam_custom_font.png %})
{% endtab %}
{% tab Liquid %}
![The IAM Studio UI showing the options to customize event/attribute logging. These options include that user behavior log.]({% image_buster /assets/img/iam_studio/iam_liquid.png %})
{% endtab %}
{% tab TRACKING/LOGGING %}
![The IAM Studio UI showing the options to customize font. These options include that user can customize font style.]({% image_buster /assets/img/iam_studio/iam_tracking_logging.png  %})
{% endtab %}
{% endtabs %}

### Step 3: Export the template

Once all editing has been completed, export the template by clicking **Export**. After exporting, the in-app message HTML code will be generated. Copy this code by clicking the **Copy code** button. 

![][2]{: style="max-width:45%;"}

### Step 4: Use code in Braze 

Navigate to Braze, and in your in-app message, paste the custom code in the **HTML Input** box. Make sure to test your message to check it is displaying correctly.

![][3]{: style="max-width:85%;"}

[1]: {% image_buster /assets/img/iam_studio/iam_template_gallery.png %}
[2]: {% image_buster /assets/img/iam_studio/export_iam_code.png %}
[3]: {% image_buster /assets/img/iam_studio/braze_campaign_editor.png %}
