---
nav_title: Fullstory
article_title: Fullstory
description: "This reference article outlines the partnership between Braze and Fullstory."
alias: /partners/fullstory/
page_type: partner
search_tag: Partner
---

# Fullstory

Fullstory’s behavioral data platform helps technology leaders make better, more informed decisions. By injecting digital behavioral data into their analytics stack, Fullstory's patented technology unlocks the power of quality behavioral data at scale–transforming every digital visit into actionable insights. 

*This integration is maintained by Fullstory*

## About this integration
You can leverage Fullstory insights in Braze to build moment-to-moment pictures of a user's website or app experience to deliver hyper-contextual messaging. Fullstory's Session Summary API makes it possible to capture detailed metadata on a user's browsing behavior for use in Braze messaging, which is particularly powerful when leveraged in a multi-step messaging journey like a Canvas. 

The real-time value of Fullstory’s Session Summary data is best leveraged through Connected Content. By using connected content in a Canvas Context step, you can store Fullstory’s data throughout a user's Canvas journey for use in any subsequent Canvas steps. This also avoids the need to write this data to a Braze user profile through custom events or attributes. 

In the following example, Canvas Context data is leveraged in an Agent AI Canvas step to generate the optimal message to encourage a user to pick back up an abandoned cart. However, you can leverage the data to personalize the message directly, to determine the user's journey via audience paths, or to determine the copy or assets used in subsequent messaging steps.

## Use cases

![Diagram showing Fullstory integration use cases with Braze]({% image_buster /assets/img/fullstory/1.png %})

## Prerequisites

Before you start, you need the following:

|Requirement     | Description |                        
|-----------------------|-----------------|
| A Fullstory Session API Authorization Token   | See Step 1 below.  | 
| A Braze Connected Content Authorization Token enabled | See the note below on Early Access |
| A Braze Canvas Context Step |See the note below on Early Access |
| Enabled Braze AI Agent Step | See the note below on Early Access|
{: .reset-td-br-1 .reset-td-br-2 role=“presentation”}

## Integrating Fullstory

### Step 1: Set up Fullstory for Session Summary API enablement

#### A: Retrieving the [Auth Token](https://developer.fullstory.com/server/authentication/) for the Session Summary API endpoint

To create a Fullstory API key, navigate to the Fullstory platform, then **Settings** > **API Keys**. Select the **Standard** permission level, and immediately copy the key value, as it appears only once.

#### B: Creating a session summary Profile ID

Following [Fullstory's guidance](https://developer.fullstory.com/anywhere/activation/ai-session-summary-api/#step-1-creating-and-managing-summary-profiles), create a session summary profile using the dedicated endpoint. This is where you define what sort of data you want the Session Summary response to provide to Braze.
In the response to this request, Fullstory provides a Session “Profile ID”. This Profile ID is a key component of the connected content request body used in the following use case.


### Step 2: Create the Connected Content Token Auth
1. In Braze, navigate to **Settings > Workspace Settings > Connected Content > Add Credential > Token Authentication**. 

2. Name the authentication “fullstory”.

3. Add the Header key “Authorization”. Supply the Header value Fullstory provided in the previous step. 

4. Under Allowed Domain, submit “api.fullstory.com”.

![Screenshot of Braze showing the Edit Credential fields]({% image_buster /assets/img/fullstory/2.png %})

## Use case: Leverage Fullstory Session Summary data and Braze Canvas Context steps and AI Agents to create dynamic message journeys

Using Fullstory's [Activation Streams](https://help.fullstory.com/hc/en-us/articles/360045134554-Streams), you can trigger Braze Canvases immediately after key user interactions. The power of this integration lies in the unique `client_session_id` (accessible via {% raw %}`{{canvas_entry_properties.${client_session_id}}}`{% endraw %}), which the system passes automatically from Fullstory to Braze. This ID acts as a key, allowing Braze to fetch the complete Session Summary of exactly what the user experienced. 

By leveraging Canvas Context steps and Connected Content, you can use this ID to make an API request to Fullstory, retrieve the session data, and store it as a variable for use later in the journey. 

![Screenshot of Braze Canvas Context step showing the context variable `summary_result` being created and populated with a connected content call to Fullstory, to retrieve a session summary]({% image_buster /assets/img/fullstory/3.png %})

With the Authorization token created earlier, use the following request structure to pull the Session Summary data. 

{% raw %}
```bash
{% connected_content https://api.fullstory.com/v2/sessions/{{canvas_entry_properties.${client_session_id} | url_encode}}/summary?config_profile=[YOUR-FULLSTORY-PROFILE-ID] :auth_credentials fullstory :save summary_result %}
{{summary_result | as_json_string }}
```
{% endraw %}

{% alert Note %}
 The response is stored as the Liquid tag {% raw %}`{{context.${summary_result}.response}}`{% endraw %}. We use this Context tag in subsequent Canvas steps.
{% endalert %}

At this stage, the canvas can access the response to the Connected Content call, which contains the entire message payload for a user's session.

{% details Example Payload from Session Summary API %}

{% raw %}
```bash
{
    "response": {
        "primary_goal": "User attempted to update payment method.",
        "issues_encountered": [
            "Received 'invalid card number' error twice.",
            "Clicked 'Submit' button multiple times with apparent frustration (based on event patterns)."
        ],
        "final_action": "Navigated away from payment page to dashboard.",
        "reason_for_termination_suggestion": "Could not update payment method successfully.",
        "help_pages_visited": [
            "/help/payment-errors"
        ]
    },
    "response_schema": {
        "type": "OBJECT",
        "properties": {
            "primary_goal": {
                "type": "STRING",
                "description": "A summary of the user's main objective during the session."
            },
            "issues_encountered": {
                "type": "ARRAY",
                "description": "A list of problems or errors the user faced.",
                "items": {
                    "type": "STRING",
                    "description": "A description of a single issue."
                }
            },
            "final_action": {
                "type": "STRING",
                "description": "The last significant action the user took before the session ended."
            },
            "reason_for_termination_suggestion": {
                "type": "STRING",
                "description": "A suggested reason for why the user ended their session."
            },
            "help_pages_visited": {
                "type": "ARRAY",
                "description": "A list of URLs for help or documentation pages the user visited.",
                "items": {
                    "type": "STRING",
                    "description": "The URL of a help page."
                }
            }
        },
        "required": [
            "primary_goal",
            "issues_encountered",
            "final_action",
            "reason_for_termination_suggestion",
            "help_pages_visited"
        ]
    }
}
```
{% endraw %}
{% enddetails %}

You can leverage any of the data available in the object above using the context Liquid tag later in the user's Canvas journey. The following steps show how you can use this data in an [AI Agent](https://www.braze.com/docs/user_guide/engagement_tools/canvas/canvas_components/agent_step) Canvas step.

{% alert Note %}
To avoid unexpected behavior, include an Audience Path step after the Context step, which can drop users out of the context if their Context tag is empty, indicating the connected content call failed or otherwise returned no information.

![Screenshot of Braze Audience step]({% image_buster /assets/img/fullstory/3.png %})

{% endalert %}

## Create an AI Agent that can analyze Fullstory’s payloads and produce appropriate copy for your use case

[Braze's agents guidance]({{site.baseurl}}/docs/user_guide/brazeai/agents/creating_agents) outlines how company users can create AI Agents. By inserting an AI Agent step into a Canvas triggered by Fullstory, and including the Canvas Context step outlined above, users can feed their AI Agent Fullstory’s session summary data, for a wide range of purposes. 

In this example, we use this data to allow the AI Agent to generate appropriate message copy for use in a content card, which can encourage the user to return to their abandoned basket.

![Screenshot of Braze Agent Context creator with the prompt]({% image_buster /assets/img/fullstory/4.png %})

Use the same name for the Context Liquid tag created in this step as the context Liquid tag used in the AI Agent step created earlier. 

The prompt required for your use case varies, but for our best practices for creating effective agent prompts, see [Writing Instructions]({{site.baseurl}}/docs/user_guide/brazeai/agents/creating_agents/#writing-instructions) in *Creating Agents*. 


In your canvas, select an AI Agent step and then select the "Session Context" agent created from the drop-down menu. Save the output as a variable, in this case "message", which you can place into message copy by using the Liquid tag {% raw %}`{{context.${message}.message}}`{% endraw %}.

![Screenshot of Braze Agent Context Canvas step with the prompt]({% image_buster /assets/img/fullstory/5.png %})

Create a message step that leverages the AI Agent-created copy. Use the Liquid tag in this step. 

{% alert Note %}

Fullstory's Session Summary API may return sensitive identifiable user data. To ensure compliance while handling PII (Personally Identifiable Information), ensure your Fullstory data capture rules exclude PII before leveraging this use case.

{% endalert %}