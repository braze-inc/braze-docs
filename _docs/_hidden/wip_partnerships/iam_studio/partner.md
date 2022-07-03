---
nav_title: IAM Studio
article_title: IAM Studio
page_order: 1
description: "This article outlines the partnership between Braze and IAM Studio, a message personalization platform which allows you to create personalized, rich in-app experiences and deliver them through Braze."
alias: /partners/iam_studio/
page_type: partner
search_tag: Partner

---

# IAM Studio

> [IAM Studio](https://www.inappmessage.com) is an in-app message solution tool through Braze. which consists of templates of new designs that have never been seen before, does not directly touch long codes.

You can edit easily from image replacement to text modification, deep link settings and custom attribute / events settings. By using IAM Studio, reduce production time and spend your time on more important tasks such as content planning.

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| IAM Studio Account | A [IAM Studio Account](https://www.inappmessage.com/register) is required to take advantage of this partnership. |
{: .reset-td-br-1 .reset-td-br-2}

## Use cases

- Customized onboarding experiences
- In-app experiences for personalized events and promotions
- Gathering customer feedback and ratings based on app behavior
- Quickly testing potential app product ideas

## Integration

### Step 1: Choose the IAM Template

Choose the in-app message template you want to use in the in-app message template gallery.

![IAM Template Gallery Image][1]

### Step 2: Customize the IAM Template

Replace the image, text, and button in the in-app message with the desired value.

{% tabs local %}
{% tab Customize Image %}
![Customize Image]({% image_buster /assets/img/iam_studio/iam_customize_image.png %})
{% endtab %}
{% tab Customize Text %}
![Customize text]({% image_buster /assets/img/iam_studio/iam_customize_text.png %})
{% endtab %}
{% tab Customize Button %}
![Customize button]({% image_buster /assets/img/iam_studio/iam_customize_button.png %})
{% endtab %}
{% endtabs %}

### Step 3: Export the IAM Template, Then IAM HTML Code is Generated.

If all editing is done, press the **EXPORT** button on the upper right.

### Step 4: Copy & Paste IAM HTML Code

In the IAM Editor, click **EXPORT** button and copy the codes with click the **Copy code** Buttons. 

![Export and Copy IAM Code][2]

Paste the **IAM HTML Codes** in the Braze Custom Code **HTML Input Box** in the Braze Campaign Editor.

![Braze Campaign Editor][3]

[1]: {% image_buster /assets/img/iam_studio/iam_template_gallery.png %}
[2]: {% image_buster /assets/img/iam_studio/export_iam_code.png %}
[3]: {% image_buster /assets/img/iam_studio/braze_campaign_editor.png %}