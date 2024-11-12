---
nav_title: Ada
article_title: Ada
description: "This reference article outlines the partnership between Braze and Ada, an AI-powered platform that automates and personalizes customer interactions. This integration allows you to augment user profiles with data collected from your automated Ada conversations."
alias: /partners/ada/
page_type: partner
search_tag: Partner

---

# Ada

> [Ada](https://ada.cx) is a brand interaction platform that automates and personalizes customer experience using conversational AI. Use Ada to tailor your messaging and segment campaigns based on user data, measure and analyze conversations to uncover new opportunities, and use insights from chatting with customers to enrich your user profiles.  

The Braze and Ada integration allows you to augment user profiles with data collected from your automated Ada conversations. You can set custom user attributes based on the information you collect during an Ada chat and record custom events in Braze at specified points in an Ada conversation. By connecting your Ada chatbot to Braze, you can learn more about your consumers based on what questions they ask about your brand or by proactively starting conversations with them, asking them questions that allow you to learn more about their interests and preferences.

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| Ada account | An [Ada](https://ada.cx) account with the Braze and Answer Utilities applications enabled is required to take advantage of this partnership. |
| Braze REST API key | A Braze REST API key with `users.track` permissions. <br><br> This can be created in the Braze dashboard from **Settings** > **API Keys**. |
| Braze REST endpoint | [Your REST endpoint URL][1]. Your endpoint will depend on the Braze URL for your instance. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Use cases

Common use cases for the Braze and Ada integration include:
- Tracking different interactions your consumers have with your Ada bot as custom events in Braze, so you know which customers have engaged with proactive campaigns in Ada, been handed off to support agents, asked specific questions, or completed certain actions.
- Asking your consumers about their interests, preferences, demographics, and more. Update their profile in Braze automatically with this new information using custom attributes.

## Integration

To integrate Braze and Ada, you must first set up the Braze application in your Ada dashboard and work with your Ada team to set up a user ID metavariable in your Ada embed script. Then, you'll drag the Braze block into the Answer editor wherever you want to send information back to Braze - either an event or an attribute.

### Step 1: Set up the Braze app in Ada

On the Ada dashboard, go to **Settings > Integrations > Handoff Integrations**.

Next to Braze, click **Connect** and provide the following information:
- **REST Endpoint**: enter your Braze REST endpoint URL. 
- **API Key**: enter your Braze REST API key. 
- **App ID**: enter the app ID you wish to associate Ada chatters with.

### Step 2: Pass through an identifier from Braze to Ada

To confirm you're updating the correct user, you'll need to reach out to your Ada team and they can help you make the necessary modifications to the Ada embed script to receive an identifier from Braze. This integration is designed to accept an external ID, but it's possible to pass other identifiers, such as a user alias. 

### Step 3: Drop the Braze block into the relevant Answers

To use the Braze block, drag it from the block drawer into the appropriate Answer, and select an action. With the Braze block, you can perform two actions:
* Track Event
* Update Attribute

{% tabs local %}
{% tab track event %}

#### Answer Utilities block

1. Drag the Answer Utilities block from the block drawer into position directly above your Braze block. 
2. Select the **Format Date** action, and enter `today` in the **Date** field.
3. Enter `iso` in the **Output Format** field. Under **Save Response As Variable**, create a variable for **Formatted Date** called `iso_time`.

![The Answer Utilities block with fields populated as described in preceding text.]({% image_buster /assets/img/ada/ada-braze-2.png %})

#### Braze block

**4.** In the Braze block, enter the `external_id` metavariable set up by Ada in the previous step in the **External ID** field.<br>
**5.** In the **Event Name** field, enter the name of the Braze event you wish to track.<br>
**6.** In the **Time of Event** field, enter the `iso_time` variable you created in the Answer Utilities block.<br>
**7.** Select a fallback answer to surface if an issue occurs while posting the event to Braze.

![The Braze block with fields populated as described in preceding text.]({% image_buster /assets/img/ada/ada-braze-3.png %})

{% endtab %}
{% tab update attribute %}

#### Braze block

1. In the Braze block, enter the `external_id` metavariable set up by Ada in the previous step in the **External ID** field. 
2. In the **Attribute Name** field, enter the name of the Braze attribute you wish to track. 
3. In the **Attribute Value** field, enter the value you wish to set, which can be text, a variable, or a combination of text and variables. 
4. Select a fallback answer to surface if an issue occurs while posting the attribute to Braze.

![The Braze block with fields populated as described in preceding text.]({% image_buster /assets/img/ada/ada-braze-4.png %})

{% endtab %}
{% endtabs %}

[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[2]: {% image_buster /assets/img/ada/ada-braze-1.png %}
[3]: {% image_buster /assets/img/ada/ada-braze-2.png %}
[4]: {% image_buster /assets/img/ada/ada-braze-3.png %}
[5]: {% image_buster /assets/img/ada/ada-braze-4.png %}