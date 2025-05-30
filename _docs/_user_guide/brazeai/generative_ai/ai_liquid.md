---
nav_title: BrazeAI Liquid Assistant
article_title: BrazeAI Liquid Assistant
description: "This article will cover how the AI Liquid Assistant works and how you can use it to generate Liquid snippets for your messaging."
page_type: reference
page_order: 5
---

# BrazeAI<sup>TM</sup> Liquid assistant

> The BrazeAI<sup>TM</sup> Liquid Assistant is a chat assistant powered by BrazeAI<sup>TM</sup> that helps generate the Liquid you need to personalize message content.

With the BrazeAI<sup>TM</sup> Liquid Assistant, you can generate Liquid from templates, receive personalized Liquid suggestions, and optimize existing Liquid with the support of BrazeAI<sup>TM</sup>. The assistant also provides annotations explaining the Liquid used, so you can increase your understanding of Liquid and learn to write your own.

## Supported channels

You can use the BrazeAI<sup>TM</sup> Liquid Assistant when creating: 
- SMS messages
- Push notifications
- HTML email messages
    - The assistant works on email messages and not templates and works best on email messages that are already built.
- Canvases

## How it works

The BrazeAI<sup>TM</sup> Liquid Assistant is designed to help you write effective Liquid code tailored to your marketing needs. Trained on both Liquid syntax and how marketers utilize Liquid in their messages, our AI understands the nuances of crafting personalized content. Additionally, by providing the BrazeAI<sup>TM</sup> Liquid Assistant your custom attribute names (such as “favourite_color”) and data types (such as boolean and string), our BrazeAI<sup>TM</sup> Liquid Assistant ensures your messages are precisely targeted and aligned with your goals. Additionally, if you create Brand Guidelines, the BrazeAI<sup>TM</sup> Liquid Assistant may use Brand Guidelines to better personalize the outputs generated and to customize content to our own brand voice. The Brand Guidelines you create will only be used to personalize content for your own use. 

## Generating Liquid code

To launch the BrazeAI<sup>TM</sup> Liquid assistant, select the AI assistant icon in the message composer.

![Message composer with the AI assistant.][1]{: style="max-width:60%;"}

You can choose a [provided prompt](#provided-prompts) or enter your own into the textbox. To generate your Liquid code, select **Update composer**.

![AI assistant window with provided prompts.][2]{: style="max-width:50%;"}
 
You can generate another message using the same prompt by selecting **Regenerate**. To remove the message and revert to your previous one, select **Undo update**.

### Provided prompts

While using the BrazeAI<sup>TM</sup> Liquid Assistant, you might see a variety of prompts to help you get started with Liquid. Some of the prompts are listed below.

#### Use app activity

The **Use app activity** prompt generates Liquid code to help you send different messages based on when your app was last used. You may be asked follow-up questions so the assistant can generate a more accurate result.

![Example output of the "Use app activity" prompt.][3]{: style="max-width:45%;"}

#### Add countdown

This prompt will generate Liquid code that sends a message with how much time until an event happens. It will ask you to provide details about the event date and time.

![Example output of the "Add countdown" prompt.][4]{: style="max-width:45%;"}

#### Inspire me

This prompt appears when there is content in your message box. It generates a list of options you can choose from to personalize your message with Liquid. 

![Example output of the "Inspire me" prompt.][5]{: style="max-width:45%;"}

#### Improve my Liquid

This prompt appears when there is content in your message composer. Select it when you want the assistant to make your code more efficient and easier to read.

![Example output of the "Improve my Liquid" prompt.][6]{: style="max-width:45%;"}

## Supported attributes

| Criterion | Knowledge type | 
| - | - | 
| Liquid (including `for` loops, `if` statements, math, and others) | Coding |
| Default and standard user attributes | Attributes |
| Custom attributes that have any of these data types: {::nomarkdown}<ul><li>Booleans</li><li>Numbers</li><li>Strings</li><li>Arrays</li><li>Time</li></ul>{:/} | Attributes |
| Connected Content | Coding |
{: .reset-td-br-1 .reset-td-br-2 }

## How is my data used and sent to OpenAI?

In order to modify or create your message content, Braze will send your prompts, messages content and/or brand guidelines (if you decide to create them) submitted to the BrazeAI<sup>TM</sup> AI assistant to OpenAI’s API Platform. All queries sent to OpenAI from Braze are anonymized, meaning that OpenAI will not be able to identify from whom the query was sent unless you include uniquely identifiable information in the content you provide. As detailed in [OpenAI’s API platform commitments](https://openai.com/policies/api-data-usage-policies), data sent to OpenAI’s API via Braze is not used to train or improve their models and will be deleted after 30 days. Please ensure that you adhere to OpenAI’s policies relevant to you, which may include its [Usage policies](https://openai.com/policies/usage-policies) and its [Sharing & publication policy](https://openai.com/policies/sharing-publication-policy). Braze makes no warranty of any kind with respect to any AI-generated content.

[1]: {% image_buster /assets/img/ai_liquid/ai_assistant_icon.png %}
[2]: {% image_buster /assets/img/ai_liquid/ai_assistant_window.png %}
[3]: {% image_buster /assets/img/ai_liquid/use_app_activity.png %}
[4]: {% image_buster /assets/img/ai_liquid/add_countdown.png %}
[5]: {% image_buster /assets/img/ai_liquid/inspire_me.png %}
[6]: {% image_buster /assets/img/ai_liquid/improve_my_liquid.png %}
