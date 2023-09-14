---
nav_title: Sage Torchie
article_title: Sage Torchie
permalink: "/sage_torchie/"
description: "This reference article guides you through various aspects of using Sage Torchie effectively."
hidden: true
---

# Sage Torchie

Sage Torchie is a Braze AI feature powered by OpenAI technology, a third-party provider of Braze. Marketers can prompt Sage Torchie to generate sophisticated Liquid statements, helping them craft personalized SMS messages. This documentation will guide you through the various aspects of using Sage Torchie effectively.

{% alert important %}
Sage Torchie is currently available as a beta feature and is under active development. Reach out to your customer success manager if you're interested in participating in this closed beta.
{% endalert %}

## Overview

Sage Torchie is a Braze AI feature powered by OpenAI technology, a third-party provider of Braze. This feature generates Liquid to help marketers write sophisticated, personalized SMS messages without having to write their own Liquid. Sage Torchie uses [OpenAI's chat API](https://platform.openai.com/docs/api-reference/chat/create) with [functions](https://platform.openai.com/docs/guides/gpt/function-calling) to write SMS messages with Braze-supported Liquid syntax.

All you need to do is give Sage Torchie a prompt, and it will generate your SMS copy with Liquid that you can add to your message composer in Braze with one click. If the bot's suggestion isn't right the first time, refine your prompt or provide feedback for a better result. Sage Torchie will make edits in response to your feedback.

![][1]

## Using Sage Torchie

Sage Torchie is only available for use with SMS messages. If you are selected to trial this beta feature, to access Sage Torchie:

1. Create an SMS message in a campaign or Canvas step.
2. Click the Sage Torchie avatar in the bottom-right of your screen. <br>![][7]{: style="border:none"}
3. Ask Sage Torchie to write your message with Liquid. Check out our [example requests](#example-requests) and [best practices](#best-practices) for help crafting your requests.
4. When Sage Torchie is done, click **Update composer** in the chat to add the new message to your composer.

![][2]{: style="border:none"}

{% alert tip %}
Sage Torchie will try to guess common user attributes, but if it needs help or if you want to use custom attributes, type "&#123;&#123;" to bring up auto-fill inside the chat box.
{% endalert %}

## Example requests

### Basic

You can ask Sage Torchie to do simple Liquid additions, such as adding standalone Liquid tags {% raw %}(like {{${first_name}}}){% endraw %} or creating two versions of a message in Spanish and English.

Here's an example of a basic request:

> I am sending an SMS message to my users to notify them of an upcoming sale this weekend for 40% off all shoes. Write me a message that includes Spanish and English versions depending on the user's preferred language.

![][3]

![][4]

### Advanced

Sage Torchie can also handle advanced Liquid use cases, such as using Connected Content, finding items in an array that match specific conditions, and more.

Here's an example of a more advanced request:

> I am sending an SMS message to my users to recommend restaurants to them. I have an endpoint here: ____ that contains an array of restaurants. Each element contains a name and a rating. Write me a message that recommends the names of 5 restaurants, and only include restaurants if they have a rating of 4 or higher.

![][5]

After Sage Torchie provides a response, you can continue refining your prompt or provide feedback for a better result. Sage Torchie will make edits in response to your feedback. For example, here we could ask Sage Torchie:

> I now want to alter the message copy depending on if it's a weekend or a weekday. Write me a message that changes the copy between those two.

When you click **Update composer**, Sage Torchie will overwrite the message in your composer with the new copy.

![][6]

## Best practices

### General

- **Provide context:** When prompting Sage Torchie, know your end goal for the marketing message. Provide the part of the life cycle the message pertains to and the action that you are prompting the user to take.
- **Direct guidance:** When prompting Sage Torchie, be as specific as possible about what personalization you need. For instance, "Help me welcome users by their first name in an SMS."
- **Ask for variations:** If unsure about a message's effectiveness, ask Sage Torchie for multiple Liquid-based message variations to choose from.
- **Double-check Liquid:** While Sage Torchie is powerful, always test the Liquid code generated to ensure it meets your needs and works correctly.
- **Avoid offensive content:** We filter out responses for offensive content that violates OpenAI’s content policy.

### Attributes

- **Use fallbacks:** Ask Sage Torchie to provide a default option for attributes that may be blank for some users.
- **Clarify attribute names:** If you have specific user attributes in Braze that you want to use, mention them to Sage Torchie. It can craft more relevant Liquid code accordingly. Type "&#123;&#123;" to bring up auto-fill for attributes inside the chat box.

### Message consistency

- **Segmentation matters:** When crafting a message, have a clear idea of which user segment you're targeting. Sage Torchie can help tailor the Liquid accordingly.
- **Maintain brand consistency:** Remind Sage Torchie about your brand's tone or any specific phrases you frequently use so the generated message aligns with your branding.
- **Use past success:** Provide Sage Torchie with examples of past successful messages to guide the generation of new content.

### Connected Content and API

- **Use Connected Content:** Sage Torchie can also generate Connected Content calls. If you have an internal or public API endpoint that you want to bring into your message, provide Sage Torchie with URL and field names when explaining your desired message.

### Collaboration and feedback

- **Iterate regularly:** If the bot's suggestion isn't right the first time, refine your prompt or provide feedback for a better result. Sage Torchie will make edits in response to your feedback.
- **Collaborate and share:** If working in a team, share successful Liquid templates and Sage Torchie interactions to benefit from collective knowledge.

## How is my data used and sent to OpenAI?

In order to check your message content, Braze will send it to OpenAI. All queries sent to OpenAI from Braze are anonymized, meaning that OpenAI will not be able to identify from whom the query was sent unless you include uniquely identifiable information in the message content you provide. Per [OpenAI’s policy](https://openai.com/policies/api-data-usage-policies), data sent to OpenAI’s API via Braze is not used to train or improve their models and will be deleted after 30 days. Braze makes no warranty of any kind with respect to any AI-generated content.

[1]: {% image_buster /assets/img/sage_torchie/sage_torchie1.jpg %}
[2]: {% image_buster /assets/img/sage_torchie/sage_torchie2.png %}
[3]: {% image_buster /assets/img/sage_torchie/sage_torchie3.png %}
[4]: {% image_buster /assets/img/sage_torchie/sage_torchie4.png %}
[5]: {% image_buster /assets/img/sage_torchie/sage_torchie5.png %}
[6]: {% image_buster /assets/img/sage_torchie/sage_torchie6.png %}
[7]: {% image_buster /assets/img/sage_torchie/sage_torchie_icon.png %} 