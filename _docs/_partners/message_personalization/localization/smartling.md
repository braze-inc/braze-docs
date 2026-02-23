---
nav_title: Smartling
article_title: Smartling
description: "This reference article outlines the partnership between Braze and Smartling, a cloud-based software for localization. The Braze Connector supports the translation of HTML email templates, Content Blocks, Canvases, and campaign email messages."
alias: /partners/smartling/
page_type: partner
search_tag: Partner
---

# Smartling

> [Smartling](https://www.smartling.com/) is an end-to-end cloud translation management software for customers looking to automate the translation of websites, applications, and customer experiences.

_This integration is maintained by Smartling._

## About the integration

The Braze Connector supports translations for messages in campaigns and Canvases (email, push, and in-app messages), email templates, and Content Blocks. Refer to the following table to learn about the supported channels and features when determining to use the new connector with multi-language support or legacy workflow.

| Channel/Feature | Traditional Editor (ex. HTML) | Drag-and-Drop Editor |
| --------------- | ----------------------------- | -------------------- |
| [Email]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/?tab=email) | ✅ | ✅ |
| [IAM]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/?tab=in-app%20message) | ✅ | ✅ |
| [Push]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/?tab=push) | ✅ | n/a |
| Email Template | Legacy workflow | Legacy workflow|
| Content Blocks |  ✅* |  ✅* |

*Refer to [Managing translations for Content Blocks](#managing-translations-for-content-blocks) for more information.

### Legacy workflow

Depending on your use case, manage translations for Content Blocks using either the legacy translation workflow or the updated workflow. 

In the updated workflow, using Braze multi-language support and locales in messages, translation tags are added to the Content Block. However, Smartling executes translations at the message level. The content is translated only when the content is included in a Campaign or Canvas and the target locale is set. To learn more, see [Managing translations for Content Blocks](#managing-translations-for-content-blocks).

For email templates, only the legacy workflow is supported. To learn more, see [Managing translations using the legacy workflow](#managing-translations-using-the-legacy-workflow).

## Prerequisites

| Requirement                   | Description                                                                                                                                                         |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Smartling account             | A [Smartling account](https://dashboard.smartling.com/) is required to take advantage of this partnership.                                                          |
| Smartling translation project | To connect your Braze account with Smartling, you must first sign in and [create a translation project](https://help.smartling.com/hc/en-us/articles/115003074093). |
| Braze REST API key            | A Braze REST API key with the following permissions: <br>- campaigns.translations.get<br>- campaigns.translations.update<br>- campaigns.list<br>- campaigns.details<br>- canvas.translations.get<br>- canvas.translations.update<br>- campaigns.details<br>- templates.email.create<br>- templates.email.update<br>- templates.email.list<br>- templates.email.info<br>- templates.translations.get<br>- templates.translations.update<br>- content_blocks.info<br>- content_blocks.list<br>- content_blocks.create<br>- content_blocks.update<br><br> This can be created in the Braze dashboard from **Settings > API Keys**. |
| Braze REST endpoint           | [Your REST endpoint URL]({{site.baseurl}}/api/basics/#endpoints). Your endpoint depends on the Braze URL for your instance.             |
| Braze Multi Language Settings | [Complete Multi Language Settings in Braze]({{site.baseurl}}/user_guide/administrative/app_settings/multi_language_settings/#prerequisites) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Step 1: Set up multi-language settings in Braze

See [Braze's multi-language setup instructions]({{site.baseurl}}/user_guide/administrative/app_settings/multi_language_settings/#prerequisites) for setting up locales in Braze.

### Step 2: Set up the Braze project in Smartling TMS

Refer to the [Smartling documentation](https://help.smartling.com/hc/en-us/articles/13248549217435) for details on connector configuration.

### Connecting Braze to Smartling

1. In your [Smartling account](https://dashboard.smartling.com/), create a [Braze Connector](https://help.smartling.com/hc/en-us/articles/115003074093) project type.

![Braze connection in Smartling.]({% image_buster /assets/img/smartling/image1_Connecting_Braze_to_Smartling.png %})

{: start="2"}
2. In this project, select **Settings** > **Braze Settings** > **Connect to Braze**.
3. Complete the required fields, like API URL and API Key. If the test connection is successful, save the connection. If the test is not successful, confirm you entered the correct API URL and API Key.

![Braze connection in Smartling API settings.]({% image_buster /assets/img/smartling/image2_API.png %})

{: start="4"}
4. Add additional project languages.

![Braze connection in Smartling Project Languages.]({% image_buster /assets/img/smartling/image3_project_languages.png %})

{: start="5"}
5. In Braze Settings, verify that the values in the **Target Language (Braze)** column match the locales configured in Braze multi-language settings. The locale naming convention must match exactly.

![Braze connection in Smartling Language Confirmation.]({% image_buster /assets/img/smartling/image4_language_confirmation.png %})

### Step 3: Add translation tags to your Braze message

See [Braze's instructions]({{site.baseurl}}/user_guide/message_building_by_channel/email/using_locales/?tab%3Dhtml%2520editor#prerequisites) on how to add translation tags to your messages:

- [Email]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/?tab=email)
- [Push]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/?tab=push)
- [In-app messages]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/?tab=in-app%20message)

Here is an example of a HTML email campaign with translation tags.

![Braze email with translation tags.]({% image_buster /assets/img/smartling/image5_translation_tags.png %})

You must save the message as a draft before you can select locales.

### Step 4: Manage translations in Smartling

After you connect and set up the Braze connector, find Braze content in the Braze tab in your Smartling project. For more information, see the [Smartling documentation](https://help.smartling.com/hc/en-us/articles/13248577069979).

Smartling provides advanced features to search and select content by:
- Keyword search
- Braze content type
- Braze tagging

1. In this example, the New Year promotion email campaign was created in [Step 3](#step-3-add-translation-tags-to-your-braze-message).

![Braze email with translation tags.]({% image_buster /assets/img/smartling/image6_ny_promotion.png %})

{: start="2"}
2. After you locate the campaign you want to translate, select the folder, choose the variants, and select **Request Translation**.

![Request Translations.]({% image_buster /assets/img/smartling/image7_request_translation.png %})

{: start="3"}
3. Create a new job for the translation.

![Create a new job for the translation.]({% image_buster /assets/img/smartling/image8_request_translation.png %})

{: start="4"}
4. After the job is authorized, edit each translation in the CAT tool.

![Translation CAT Tool.]({% image_buster /assets/img/smartling/image9_translation_job.png %})

{: start="5"}
5. After the translations are complete, save and submit your translation to Braze.

![Submit translation to Braze.]({% image_buster /assets/img/smartling/image10_translations.png %})

### Step 5: Preview the message as a multi-language user in Braze

In Braze, preview your campaign as a multi-language user to confirm that the translations are applied correctly.

![Multi-language user preview.]({% image_buster /assets/img/smartling/image11_preview.png %})

## Managing translations for Content Blocks

Content Blocks are managed under the **Templates & Media** section in Braze.

### Translation stored as part of the message component

Translation tags belong on the Content Block. However, Smartling executes translations at the message level; the content is translated only when it’s included in a campaign or Canvas and the target locale is set.

### Considerations

- Translation tags must be manually added to the Content Block for both HTML and drag-and-drop Content Block editors.
- Locales are selected at the message level, not on the Content Blocks themselves.
- For Canvas, we recommend using rows to insert Content Blocks into your message instead of manually adding them with a Liquid tag. Dragging a Content Block from the preview into an email makes a local copy; any changes to the "parent" Content Block do not propagate to other campaigns using that block.
- If you do use a Content Block Liquid tag, be sure to include at least one translation tag directly in the email body. Manually adding the translation tag allows you to select the locales from the multi-language dropdown. Smartling picks up the translation tags for the Content Block. You can add a `comment` tag so the text is not visible to the user.

## Managing translations using the legacy workflow

If you prefer to manage translations directly within a Content Block or email template, see the legacy instructions in [Smartling's documentation](https://help.smartling.com/hc/en-us/articles/13248577069979-Translating-with-the-Braze-Connector). This method uses a language attribute and Liquid if/else logic to display text in different languages.

## Frequently asked questions

### Are translation tags supported for the drag-and-drop editor?

For the drag-and-drop editor (email, Content Block, in-app message), you must manually add translation tags as Liquid tags.

### How do you translate text within a Liquid tag?

Smartling recognizes Liquid tags and makes them uneditable variables in the composer. Any other text within the Liquid tag, such as default text or filters like join, also become uneditable in Smartling. However, remove the Liquid tag in Smartling and recreate the Liquid tag with the translated default text. A warning appears when saving the translation.
