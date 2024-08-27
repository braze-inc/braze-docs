---
nav_title: AI Liquid Assistant
article_title: AI Liquid Assistant
description: "This article will cover how Sage AI Liquid Assistant works and how you can use it to generate Liquid snippets for your messaging."
page_type: reference
page_order: 5
---

# AI Liquid assistant

> The Sage AI Liquid Assistant is a chat assistant powered by Sage AI that helps generate the Liquid you need to personalize message content. 

With the AI Liquid Assistant, you can generate Liquid from templates, receive personalized Liquid suggestions, and optimize existing Liquid with the support of Sage AI. The AI Liquid Assistant also provides annotations explaining the Liquid used, so you can increase your understanding of Liquid and learn to write your own.

{% alert important %}
The AI Liquid Assistant is currently in beta for a limited number of customers who actively use the push and SMS channels. If you're interested in being considered for the beta, reach out to your customer success manager.
{% endalert %}

## How it works

The AI Liquid Assistant is designed to help you write effective Liquid code tailored to your marketing needs. Trained on both Liquid syntax and how marketers use Liquid in their messages, our AI understands the nuances of crafting personalized content. Additionally, by providing the AI Liquid Assistant with your custom attribute names (such as `favourite_color`) and data types (such as a boolean or string), our AI Assistant ensures your messages are precisely targeted and aligned with your goals.

## Generating Liquid code

To launch the AI Liquid assistant, select the AI assistant icon in the message composer.

![Message composer with the AI assistant.][1]{: style="max-width:50%;"}

You can choose a [provided prompt](#provided-prompts) or enter your own into the textbox. To generate your Liquid code, select **Update composer**.

![AI assistant window with provided prompts.][2]{: style="max-width:50%;"}
 
You can generate another message using the same prompt by selecting **Regenerate**. To remove the message and revert to your previous one, select **Undo update**.

### Provided prompts

While using the AI Liquid Assistant, you might see a variety of prompts to help you get started with Liquid. Some of the prompts are listed below.

#### Use app activity

The **Use app activity** prompt generates Liquid code to help you send different messages based on when your app was last used. You may be asked follow-up questions so the assistant can generate a more accurate result.

![Example output of the "Use app activity" prompt.][3]{: style="max-width:45%;"}

#### Add countdown

This prompt will generate Liquid code that sends a message with how much time until an event happens. It will ask you to provide details about the event date and time.

![Example output of the "Add countdown" prompt.][4]{: style="max-width:45%;"}

#### Inspire me

This prompt appears when there is content in your message box. It generates a list of options you can choose from to personalize your message with Liquid. 

![Example output of the "Inspire me" prompt.][5]{: style="max-width:60%;"}

#### Improve my Liquid

This prompt appears when there is content in your message composer. Select it when you want the assistant to make your code more efficient and easier to read.

![Example output of the "Improve my Liquid" prompt.][6]{: style="max-width:45%;"}

## Supported attributes in beta

| Criterion | Knowledge type | 
| - | - | 
| Liquid (including `for` loops, `if` statements, math, and others) | Coding |
| Default and standard user attributes | Attributes |
| Custom attributes that have any of these data types: {::nomarkdown}<ul><li>Booleans</li><li>Numbers</li><li>Strings</li><li>Arrays</li><li>Time</li></ul>{:/} | Attributes |
| Connected Content | Coding |
{: .reset-td-br-1 .reset-td-br-2 }

## How is my data used and sent to OpenAI?

To modify or create your message content, Braze will send your prompts, messages, and content submitted to the Liquid AI Assistant to OpenAI’s API platform. All queries sent to OpenAI from Braze are anonymized, meaning that OpenAI will not be able to identify from whom the query was sent unless you include uniquely identifiable information in the content you provide. As detailed in [OpenAI’s API platform commitments](https://openai.com/policies/api-data-usage-policies), data sent to OpenAI’s API via Braze is not used to train or improve their models and will be deleted after 30 days. Make sure to adhere to OpenAI’s policies relevant to you, which may include its [Usage policies](https://openai.com/policies/usage-policies) and its [Sharing & publication policy](https://openai.com/policies/sharing-publication-policy). Braze makes no warranty of any kind with respect to any AI-generated content

[1]: {% image_buster /assets/img/ai_liquid/ai_assistant_icon.png %}
[2]: {% image_buster /assets/img/ai_liquid/ai_assistant_window.png %}
[3]: {% image_buster /assets/img/ai_liquid/use_app_activity.png %}
[4]: {% image_buster /assets/img/ai_liquid/add_countdown.png %}
[5]: {% image_buster /assets/img/ai_liquid/inspire_me.png %}
[6]: {% image_buster /assets/img/ai_liquid/improve_my_liquid.png %}
