---
nav_title: Fullstory
article_title: Fullstory
description: "This reference article outlines the partnership between Braze and Fullstory."
alias: /partners/fullstory/
page_type: partner
search_tag: Partner
---

# Fullstory

Fullstory’s behavioral data platform helps technology leaders make better, more informed decisions. By injecting digital behavioral data into their analytics stack, our patented technology unlocks the power of quality behavioral data at scale–transforming every digital visit into actionable insights. 

<-- Only include the following line if the partner manages the integration. If Braze manages the integration, don’t include it. -->
*This integration is maintained by Fullstory*

## About this integration
<-- Highlight the relationship between your company and Braze and how this partnership helps your customers. →
Fullstory insights can be leveraged in Braze to build moment-to-moment pictures of a users website or app experience to deliver hyper-contextual messaging. Fullstory’s Session Summary API makes it possible to capture detailed meta data on a users browsing behaviour for use in Braze messaging, which is particularly powerful when leveraged in a multi-step messaging journey like a Canvas. 

The real-time value of Fullstory’s Session Summary data is best leveraged through Connected Content. By using connected content in a Canvas Context step, Fullstory’s data can be stored throughout a users Canvas journey for use in any subsequent Canvas steps. This also avoids the need to write this data to a Braze user profile through Custom events or attributes. 

 In the example below, Canvas Context data is leveraged in an Agent AI Canvas step to generate the optimal message to encourage a user to pick back up an abandoned cart. However the data can be leveraged to personalize the message directly, to determine the users journey via audience paths, or to determine the copy or assets used in subsequent messaging steps.


ADDITIONAL_INFORMATION.

## Use cases


CONTENT.

![ALT_TEXT]({% image_buster /assets/img/fullstory/1.png %})

## Prerequisites

Before you start, you need the following:

|Requirement     | Description |                        
|-----------------------|-----------------|
| A Fullstory Session API Authorization Token   | See Step1 Below.  | 
| A Braze Connected Content Authorization Token enabled | See the note below on Early Access |
| A Braze Canvas Context Step |See the note below on Early Access |
| Enabled Braze AI Agent Step | See the note below on Early Access|
{: .reset-td-br-1 .reset-td-br-2 role=“presentation”}

## Integrating Fullstory

### Step 1: Fullstory setup for Session Summary API enablement
	#### A: Retrieving[ Auth Token]|(https://developer.fullstory.com/server/authentication/) for Session Summary API endpoint
To create a Fullstory API key, navigate to the Fullstory platform, then Settings > API Keys. Select the "Standard" permission level, and copy the key value immediately, as it will only be displayed once.
#### B: Creating a session summary Profile ID
Following the Guidance provided by Fullstory [in their documentation](https://developer.staging.fullstory.com/anywhere/activation/ai-session-summary-api/#step-1-creating-and-managing-summary-profiles), create a session summary profile using the dedicated enpoint. This is where you define what sort of data you’d like the Session Summary response to provide to Braze.
In the response to this request, Fullstory will provide a Session “Profile ID”. This Profile ID is a key component of the connected content request body used in the use case below


### Step 2: Create Connected Content Token Auth
Navigate to Settings > Workspace Settings > Connected Content > Add Credential > Token Authentication. 

Name the authentication “fullstory”.

Add the Head key “Authorization”. Supply the Header value provided by Fullstory in the previous step. 

Under Allowed Domain, submit “api.fullstory.com”.

![Screenshot of Braze showing the Edit Credential fields]({% image_buster /assets/img/fullstory/2.png %})


## Use case: Leverage Fullstory Session Summary data & Braze Canvas Context steps & AI Agents to create dynamic message journeys

Using Fullstory’s [Activation Steam’s](https://help.fullstory.com/hc/en-us/articles/360045134554-Streams) , Fullstory can send API triggers to Braze to launch Camaigns or Canvases. An advantage of this tool is that it allows Fullstory to pass a user’s “Session ID” to Braze, which allows Fullstory to match a Braze user to their records. Fullstory’s Canvas Trigger requests will include a property “client session id”, which can be access in the Canvas journey using the liquid tag {{canvas_entry_properties.${client_session_id}.

Canvas Context steps allow users to set variables that can be used for the length of a users Canvas journey. Connected Content calls can be used in Context steps , which allows users to make API requests to pull data from Fullstory’s Session Summary API’s and set the response data as a context variable

![Screenshot of Braze Canvas Context step showing the context variable “summary_result” being created and populated with a connected content call to Fullstory, to retrieve a session summary({% image_buster /assets/img/fullstory/3.png %})

Using the Authorisation token created earlier, users can make a request to pull data for each user in the Canvas, to retrieve Session Summary Data on their most recent website or app activity. 

The structure of the Connected content call is as follows:

```bash
{% connected_content https://api.fullstory.com/v2/sessions/{{canvas_entry_properties.${client_session_id} | url_encode}}/summary?config_profile=[YOUR-FULLSTORY-PROFILE-ID] :auth_credentials fullstory :save summary_result %}
{{summary_result | as_json_string }}
```
{% alert Note %}
 The response is stored as the liquid tag {%context.${summary_result}.response}}. We will use this Context tag in subsequent Canvas steps.
{% endalert %}

At this stage, the canvas will be able to access the response to the Connected Content call, which will contain the entire message payload for a users session.

<details>
<summary>Example Payload from Session Summary API:</summary>

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
</details>


Any of the data available in the object above can be leveraged using the context liquid tag later in the user’s Canvas journey. The following steps will show how this data can be leveraged in an [AI Agent](https://www.braze.com/docs/user_guide/engagement_tools/canvas/canvas_components/agent_step) Canvas step.

{% alert Note %}
For the avoidance of unexpected behaviour, an Audience Path step could be included after the Context step, which can drop users out of the context if their Context tag is empty, indicating the connected content call failed or otherwise returned no information

![Screenshot of Braze Audience step({% image_buster /assets/img/fullstory/3.png %})

{% endalert %}

## 1 Create an AI Agent that can analyze Fullstory’s payloads and produce appropriate copy for your use case

[This guidance]({{site.baseurl}}/docs/user_guide/brazeai/agents/creating_agents) outlines how Braze users can create AI Agents. By inserting an AI Agent step into a Canvas triggered by Fullstory, and including the Canvas Context step outlined above, users can feed their AI Agent Fullstory’s session summary data, for a wide range of purposes. 

In this example, we’ll look at using this data in order to allow the AI Agent to generate appropriate message copy for use in a content card, which can encourage the user to return to their abandoned basket

![Screenshot of Braze Agent Context creator with the prompt({% image_buster /assets/img/fullstory/4.png %})

The name used for the Context Liquid tag created in this step should be the same as the context liquid tag used in the AI Agent step created earlier. 

The prompt required for your use case will vary, but our Best Practices for creating effective Agent prompts can be found [here]({{site.baseurl}}/docs/user_guide/brazeai/agents/creating_agents/#writing-instructions). 


In your canvas, select an AI Agent Step and then select the “Session Context” agent created from the dropdown. Be sure to save the output as a variable, in this case “message”, which can be placed into message copy by using the liquid tag {{context.${message}.message}}.

![Screenshot of Braze Agent Context Canvas step with the prompt({% image_buster /assets/img/fullstory/5.png %})

Create a message step which leverages the AI Agent created copy. The liquid tag can be found in this step. 

{% alert Note %}

Fullstory’s session Summary API’s may return sensitive identifiable user data. To ensure compliance while handling PII,  ensure your Fullstory data capture rules exclude PII (Personally Identifiable Information) before leveraging this use case.

{% endalert %}
