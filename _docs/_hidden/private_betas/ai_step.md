---
nav_title: AI Step
article_title: AI Step
permalink: /ai_step/
description: "This reference article covers the Canvas AI step."
Tool:
  - Canvas
hidden: true
---

# AI step

> The AI step within Canvas leverages ChatGPT to automate personalized marketing by interpreting user-generated inputs (such as survey feedback), determining the appropriate response, and triggering messages—all within Braze. ChatGPT is powered by OpenAI, a third party.

{% alert note %}
The AI step is currently available as a beta feature. Contact your customer success manager if you're interested in participating in this beta trial.
{% endalert %}

## Creating an AI step {#create-ai-step}
 
1. Add a new step to your Canvas and select the **AI Step**. <br><br>![AI step in the Canvas builder]({% image_buster /assets/img/ai_step1.png %}){: style="max-width: 30%;"}<br><br>
2. Create a prompt that tells the AI how to respond to various user actions. Responses can include updating a custom attribute or sending a message. This prompt can use Liquid to assign different response outputs based on different user attributes or inputs. <br><br>To assign outputs that can then be used to personalize future messages within the same Canvas, create a prompt that saves variables with specific names (for example, “message” and “sentiment score”). <br><br> ![Sample AI prompt used in the AI step settings to send a personalized message based on a generated sentiment score. This example is stated under the "Customer sentiment responses" section.]({% image_buster /assets/img/ai_step2.png %}) <br><br>
3. Use the **Preview** tab to test what the AI might output for specific users.<br><br> ![The Preview tab of the AI step settings showing an AI-generated personalized message for three parameters: a first name of Cameron, a product name of shoes, and the text "comfy but my shoe lace already broke"]({% image_buster /assets/img/ai_step3.png %})

## Referencing AI output using Liquid
Reference the AI output in later steps by inserting the Liquid logic `{% raw %}{{ai_step_output.${key_name}}}{% endraw %}`. You can set the `key_name` within the prompt in the AI step.

For example, if you use the variables “message” and “sentiment score”, you can use `{% raw %}{{ai_step_output.${message}}}{% endraw %}` to personalize a subsequent message in that same Canvas.

You can also log the output of any AI step as a custom attribute by using the user update Canvas step, where you read the AI step output (for example, `{% raw %}{{ai_step_output.${sentiment_score}}}{% endraw %}`). If the output isn’t stored as a custom attribute, then it can’t be used in any other places besides subsequent steps of the same Canvas.

## AI step stats

AI steps have the following step-level stats:

- **Proceeded to next step:** Number of users that proceeded to the following step(s) in the Canvas
- **Exited Canvas:** Number of users that exited the Canvas because your AI step was the last step
- **Output succeeded:** Number of users for whom the AI step successfully generated output
- **Output failed:** Number of users for whom the AI step failed to generate output, in which case, users will still proceed to any subsequent steps.

### Understanding your AI step outputs

There are a few scenarios where Braze will discard the output of the AI step and send the customer to the next step:
- If the output exceeds 1,024 characters
- If the output isn’t in JSON
- If the prompt fails OpenAI’s [moderation](https://platform.openai.com/docs/guides/moderation/overview) requirements, which flags inappropriate user-generated content

## AI step use cases

### Customer sentiment responses

As demonstrated by the example in [Creating an AI step](#create-ai-step), you can ask the AI to send follow-up messages based on sentiment scores generated from customer feedback.
- Positive sentiment scores - Trigger a push notification that asks users to leave a review
- Medium sentiment scores - Trigger an email that asks users if they’d like additional help
- Low sentiment scores - Trigger a webhook that notifies the user Help Desk, so that a support representative can craft a nuanced follow-up

#### Example AI prompt

This example was used in [Creating an AI step](#create-ai-step).

A customer has purchased "`{% raw %}{{canvas_entry_properties.${product_name}}}{% endraw %}`", and given the product feedback: "`{% raw %}{{canvas_entry_properties.${text}}}{% endraw %}`". Create a sentiment score as an integer between 0 to 100. Then create a personalized message. This should return two variables, "message" and "sentiment score."

### Survey follow-ups

If you run an in-app or in-browser survey with a free-response section, you can use AI steps to analyze free responses and follow up appropriately. 

For example, if a makeup retailer has a survey asking, “What products would you like to nominate for this year’s beauty awards?”, they could use a prompt that identifies and assigns an attribute for the user’s favorite product types and brands, and then personalize future content based on this data.

#### Example AI prompt

Identify the user's favorite brand using their response. Then create a message that thanks users for filling out the survey and mentions how Beauty Experts also love their favorite brand. This should return two variables, "message" and "favorite brand."

![Preview tab of the AI step settings showing an AI-generated personalized message for the survey response parameter of "I love Estee Lauder face creams" that thanks the user for filling out the survey and then recommends a face cream.]({% image_buster /assets/img/ai_step4.png %})

### Behavior-driven recommendations

Customers can ask the AI to analyze user behaviors and send recommendation messages. 

For example, you can create a prompt to analyze users’ 50 most recent purchases and set their most commonly purchased category as a new custom attribute. Then, you can send personalized email recommendations for each user’s favorite category.

#### Example AI prompt

A customer has purchased the following products: "`{% raw %}{{custom_attribute.${Products Purchased}}}{% endraw %}`". Identify the user's most purchased product category. This should return a new variable for "most purchased category."

![Preview tab of the AI step settings showing the AI-generated variable of "book" for the parameter of most purchased category.]({% image_buster /assets/img/ai_step5.png %})

## Rate limits

There is a limit of 10 requests per minute (RPM) per company. This means that for any AI step, up to 10 users may receive that step during any given minute and any users beyond the 10 will automatically advance to the next step. When the next minute begins, users can again receive the AI step, but prior users that triggered the rate limit will not be retried.

## AI step limitations

- This feature leverages GPT-3.5.
- This feature uses the Braze OpenAI API key. You cannot use your own OpenAI API key.
- There is a limit of 5 requests per minute (RPM) per workspace and 10 RPM per company.
- This feature is not HIPAA compliant and customers should not send any personally identifiable information (PII) or protected health information (PHI).

## How is my data used and sent to OpenAI?

In order to analyze and create your message content, Braze will send your prompts to OpenAI’s API Platform. All queries sent to OpenAI from Braze are anonymized, meaning that OpenAI will not be able to identify from whom the query was sent unless you include uniquely identifiable information in the message content you provide. As detailed in [OpenAI’s API Platform Commitments](https://openai.com/policies/api-data-usage-policies), data sent to OpenAI’s API via Braze is not used to train or improve their models and will be deleted after 30 days. Please ensure that you adhere to OpenAI’s policies relevant to you, including the [Usage Policy](https://openai.com/policies/usage-policies). Braze makes no warranty of any kind with respect to any AI-generated content. 

[1]: {% image_buster /assets/img/ai_step1.png %} 
[2]: {% image_buster /assets/img/ai_step2.png %} 
[3]: {% image_buster /assets/img/ai_step3.png %} 
[4]: {% image_buster /assets/img/ai_step4.png %} 
[5]: {% image_buster /assets/img/ai_step5.png %} 