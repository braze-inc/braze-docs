---
nav_title: Jasper
article_title: Jasper
description: "This reference article outlines the integration between Braze and Jasper."
alias: /partners/jasper/
page_type: partner
search_tag: Partner
---

# Jasper 

> [Jasper](https://www.jasper.ai/) is an AI-powered content platform that empowers your brand to create, manage, and scale high-quality, on-brand content across various channels, including blogs, ads, and social media.

_This integration is maintained by Jasper._

## Overview

The Jasper and Braze integration empowers you to streamline content creation and campaign execution. With Jasper, your marketing teams can generate high-quality, on-brand copy in minutes. Braze will then facilitate the delivery of these messages to the right audience at the optimal time. This integration fosters seamless workflows, reduces manual effort, and drives stronger engagement outcomes.

Benefits of using this integration include:

- **Fast campaign execution:** Launch campaigns in minutes, not weeks.
- **Consistent brand voice:** Use Jasper templates to make sure that generated copy adheres strictly to brand guidelines.
- **Targeted content generation:** Create highly customized messaging with audience segments, style guides, and proprietary knowledge items.
- **Dynamic personalization:** Use Liquid placeholders, like {% raw %}```{{${first_name}}}```{% endraw %}, for scalable personalization within Braze.
- **Error reduction:** Automated workflows minimize copy-paste errors and reduce manual steps.

## Prerequisites

| Requirement   | Description  |
| ------------------- | ---------------- |
| Jasper Account      | You need a Jasper account to utilize this partnership. |
| Braze REST API Key  | A Braze REST API key with the following permissions. <br>  <br>`templates.email.create` <br> `templates.email.update` <br>`content_blocks.create` <br>`content_blocks.update` <br><br>This key can be generated in the Braze dashboard by navigating to **Settings > API Keys**.  |
| Braze REST Endpoint | Your REST endpoint URL. Your specific endpoint depends on the Braze URL for your instance. Refer to the [Braze API Basics: Endpoints]({{site.baseurl}}/api/basics#endpoints) documentation for more details. |
{: .reset-td-br-1 .rest-td-br-2 role=“presentation” }

## Integration methods

There are two methods for generating content in Jasper and updating Braze templates:

1. Use the Jasper API directly
2. Use Jasper Studio to build a Braze-ready custom app

{% tabs %}
{% tab Jasper API %}

## Method: Use Jasper API directly

This method is ideal for programmatically creating and updating email HTML templates in Braze, bypassing manual setup in Jasper and Braze.

### Step 1: Set up Jasper

1. Follow the instructions in [Getting Started](https://developers.jasper.ai/docs/getting-started-1) to generate your Jasper API key.
2. Use Jasper’s pre-built template that is optimized for generating Braze HTML email templates, which has a template ID of  `skl_BC53D8AC5B4B47E8BE557EBB706E9B47`.
3. Collect the values for the following fields, which are required to make a request to generate content for a Braze HTML email template.

| Field | Description |
| --- | --- |
| `emailObjective`| Clearly define the goal of the email. |
| `ctaLink`| The URL for your call-to-action. |
| `unsubscribeLink`| Required for marketing emails. |
| `brandColor`| Your brand's primary color in hexadecimal format (for example, `#4dfa8a`). |
{: .reset-td-br-1 .rest-td-br-2 role=“presentation” }

**Optional fields**

| Field | Description |
| --- | --- |
|`toneId` | Brand voice |
| `audienceId`| Audience segmentation |
| `styleId`| Style guide |
| `knowledgeIds` | Enhanced content context. You can add up to three IDs. |
{: .reset-td-br-1 .rest-td-br-2 role=“presentation” }

{: start="4"}
4. Generate your output by executing the template through the Jasper API. This will produce a JSON payload containing the `subject`, `preheader`, and `body` (HTML content).

{% subtabs %}
{% subtab Sample request %}

### Sample request

{% raw %}
```json
curl --location 'https://api.jasper.ai/v1/templates/skl_BC53D8AC5B4B47E8BE557EBB706E9B47/run?toneId=ton_811696974b3c4db4b3ac0041685c3b7c&knowledgeIds=kno_0a62fc17529e4fe69a71f30b6f0e88a7&audienceId=aud_0199117a690a7cc98481f8700916e2a6' \
--header 'Content-Type: application/json' \
--header 'x-api-key: ••••••' \
--data '{
  "inputs": {
    "emailObjective": "Announce a webinar and highlight Jasper + Braze integration benefits. Use {{${firstname}}} in the subject and body. Body length ~400 words. Include CTA buttons for registration and footer with unsubscribe link. Apply brand color to buttons and links.",
    "ctaLink": "https://yourbrand.com/register",
    "unsubscribeLink": "{{${unsubscribe_link}}}",
    "brandColor":"#4dfa8a"
  },
  "options": {
    "outputCount": 1,
    "outputLanguage": "English",
    "inputLanguage": "English",
    "languageFormality": "less"
  }
}'
```
{% endraw %}

{% endsubtab %}
{% subtab Sample output %}

### Sample output
```
{
  "subject": "GlowUp Serum is Here! Limited-Time 20% Off!",
  "preheader": "GlowUp Serum is here with a 20% launch discount for 7 days only!",
  "body": "<html> ... </html>"
}
```
{% endsubtab %}
{% endsubtabs %}

### Step 2: Set up Braze

Using the `subject`, `preheader`, and `body` generated by Jasper in Step 1, make a POST request to the Braze REST API to [create a new email template]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template/). Make sure your Braze REST API key has the `templates.email.create` and `templates.email.update` permissions.

### Sample Braze API request to create an email template

```json
curl --location --request POST 'https://rest.iad-03.braze.com/templates/email/create' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer <YOUR_BRAZE_API_KEY>' \
--data '{
  "template_name": "email_template_jasperapi_20231104T142300Z",
  "subject": "GlowUp Serum is Here! Limited-Time 20% Off!",
  "preheader": "GlowUp Serum is here with a 20% launch discount for 7 days only!",
  "body": "<html> ... </html>"
}'
```
{% endtab %}
{% tab Jasper Studio %}

## Method: Build a Braze-ready custom app with Jasper Studio

Jasper Studio is a no-code platform within Jasper that allows you to build tailored AI apps without requiring IT support. You can design a custom app that generates JSON structures specifically formatted for the Braze API, or generate content that can be manually added to your Braze messages.

1. On your Jasper home screen, select **Create an App**.
2. Specify the app you want to create, such as **Braze HTML Email Template** or **Content Block Template**.
3. Edit the input prompt fields that Jasper generates. For an HTML email template, you might include input forms for subject line, preheader, HTML body, tags, inline CSS toggle, and the template name.
4. Integrate knowledge embeds with guidance on Liquid best practices for consistent personalization and dynamic content.
5. Refine the instructions provided to the Large Language Model (LLM) for content generation.
6. Provide an example of the desired output, which can include automated JSON output formatted for Braze payloads.
7. Generate and export the following:
- **Direct Copy/Paste:** Content can be copied and pasted directly into the Braze platform.
- **JSON Output:** Generate JSON output. This payload can then be used to directly call the Braze endpoint through `curl` or middleware, or integrated into your email operations workflow.

![Jasper Braze Custom App.]({% image_buster /assets/img/jasper/jasper_custom_app.png %})

{% subtabs %}
{% subtab Sample JSON output (custom app) %}

## Sample JSON output (custom app)

{% raw %}
```json
{
  "template_name": "email_webinar_2025",
  "subject": "Join Our Webinar, {{${firstname}}}!",
  "preheader": "Unlock the potential of seamless integration.",
  "body": "<html> ... </html>",
  "tags": ["jasperapi"],
  "should_inline_css": true
}
```
{% endraw %}

{% endsubtab %}
{% subtab Sample Braze API request (using custom app output) %}

## Sample Braze API request (using custom app output)

{% raw %}
```json
curl --location --request POST 'https://rest.iad-03.braze.com/templates/email/create' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer <YOUR_BRAZE_API_KEY>' \
--data '{
  "template_name": "email_template_jasperapi_20231104T142300Z",
  "subject": "GlowUp Serum is Here! Limited-Time 20% Off!",
  "preheader": "GlowUp Serum is here with a 20% launch discount for 7 days only!",
  "body": "<html> ... </html>"
}'
```
{% endraw %}

{% endsubtab %}
{% endsubtabs %}

Alternatively, if you are a marketer, you can create your custom app to align with brand guidelines to generate content without HTML and copy and paste, and use Braze templates for styling.

{% endtab %}
{% endtabs %}

{% alert note %}
For additional assistance, refer to [Jasper API documentation](https://developers.jasper.ai/reference/gettemplate-1) and the [Jasper Studio Help Center](https://help.jasper.ai/hc/en-us/articles/36783295610395-Jasper-Studio).
{% endalert %}
