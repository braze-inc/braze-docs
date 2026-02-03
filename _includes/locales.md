{% if include.section == "Prerequisites" %}
## Prerequisites

To edit and manage [multi-language support]({{site.baseurl}}/multi_language_support/), you must have the "Manage Multi-Language Settings" user permission. To add the locale to a message, you'll need permissions for editing campaigns.

{% alert important %}
Multi-language support is currently in early access. Contact your Braze account manager if you’re interested in participating in this early access.
{% endalert %}

{% endif %}

{% if include.section == "Preview" %}

## Preview your locales

In the **Preview message as user** dropdown within the **Test** tab, select **Custom user** and enter different languages to preview the message to check if your message translates as expected.

{% endif %}

{% if include.section == "Frequently Asked Questions" %}

## Frequently asked questions

#### Can I make a change to the translated copy in one of my locales?
Yes. First, make the edit in the CSV, then upload the file again to make a change to the translated copy.

#### Can I nest translation tags?
No.

#### Can I add HTML styling in the translation tags?
Yes, but be sure to check that the HTML styling is not translated with the content.

#### What validations or extra checks does Braze do?

| Scenario                                                                                                                                                 | Validation in Braze                                                                                            |
|----------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| A translation file is missing locales associated with the current message.                                                                               | This translation file won't be uploaded.                                                                       |
| A translation file is missing text blocks, such as a text within Liquid translation tags, from the current email message.                                | This translation file won't be uploaded.                                                                       |
| The translation file includes the default text that doesn't match the text blocks in the current email message.                                          | This translation file won't be uploaded. Fix this in your CSV before attempting to upload again.               |
| The translation file includes locales that don't exist in **Multi-Language Support** settings.                                                           | These locales will not be saved in Braze.                                                                      |
| The translation file includes text blocks that don't exist in the current message (such as the current draft at the time the translations are uploaded). | The text blocks that don't exist in your current message will not be saved from the translation file to Braze. |
| Removing a locale from the message after that locale has already been uploaded to the message as part of the translation file.                           | Removing the locale will remove any translations associated with the locale in your message.                   |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endif %}
