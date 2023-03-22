---
nav_title: IAM Studio
article_title: IAM Studio
description: "This reference article outlines the partnership between Braze and IAM Studio, a message personalization platform which allows you to create personalized, rich in-app experiences and deliver them through Braze."
alias: /partners/iam_studio/
page_type: partner
search_tag: Partner

---

# IAM Studio

{:.subintro}
[IAM Studio](https://www.inappmessage.com) is a no-code message personalization platform that allows you to create personalized, rich in-app experiences and deliver them through Braze.

With the Braze and IAM Studio integration, you can easily insert customizable in-app message templates into your Braze in-app messages, offering image replacement, text modification, deep link settings, custom attributes, and event settings. Using IAM Studio, you can reduce message production time and dedicate more time to content planning. 

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| IAM Studio account | A [IAM Studio account](https://www.inappmessage.com/register) is required to take advantage of this partnership. |
{: .reset-td-br-1 .reset-td-br-2}

## Use cases

- Customized onboarding experiences
- In-app experiences for personalized events and promotions
- Gathering customer feedback and ratings based on app behavior
- Quickly testing potential app product ideas

## Integration

### Step 1: Choose a template

Login to IAM Studio and choose an in-app message template you want to use from the in-app message template gallery.

![The IAM Studio template gallery shows different templates such as "modal slick contents", "full survey", "modal full image", and more.][1]

### Step 2: Customize the template

Next, replace the images, text, and buttons with your desired content.

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

### Step 3: Export the template

Once all editing has been completed, export the template by clicking **Export**. After exporting, the in-app message HTML code will be generated. Copy this code by clicking the **Copy code** button. 

![][2]{: style="max-width:45%;"}

### Step 4: Use code in Braze 

Navigate to Braze, and in your in-app message, paste the custom code in the **HTML Input** box. Make sure to test your message to ensure it is displaying correctly.

![][3]{: style="max-width:85%;"}

[1]: {% image_buster /assets/img/iam_studio/iam_template_gallery.png %}
[2]: {% image_buster /assets/img/iam_studio/export_iam_code.png %}
[3]: {% image_buster /assets/img/iam_studio/braze_campaign_editor.png %}