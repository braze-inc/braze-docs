---
nav_title: Lead Scoring
article_title: Creating a Lead-Scoring Workflow
page_order: 1
page_type: reference
description: "Learn how to use Braze to do simple lead scoring, external lead scoring, and lead handoffs."
---

# Creating a lead-scoring workflow

> This use case demonstrates how you can use Braze to update user lead scores in real time and automatically hand off leads to your Sales teams.

There are two key steps to creating a lead-scoring workflow in Braze:

1. Create a lead-scoring Canvas in Braze or integrate an external lead-scoring tool:
- [Simple lead scoring](#simple-lead-scoring)
- [External lead scoring](#external-lead-scoring)

2. Create a webhook campaign to send qualified leads to your Sales team:
- [Lead handoff: Marketing Qualified Lead (MQL) to Sales](#lead-handoff)

## Simple lead scoring

### Step 1: Create a Canvas

1. Go to **Messaging** > **Canvas** and select **Create Canvas**, and then fill in your Canvas basics.

2. Give your Canvas a relevant name such as “Lead Scoring Canvas” and, for better findability, tag it with something like “Lead Management”.<br><br>![Step 1 of creating a Canvas with the name “Lead Scoring Canvas” and tag “Lead Management”.]({% image_buster /assets/img/b2b/step_1_simple.png %}){: style="max-width:80%;"}

### Step 2: Set up your entry criteria

1. Proceed to the **Entry Schedule** step and select an **Action-Based** entry schedule. This will enter users into the Canvas when they perform specific actions.

2. In **Action-Based Options**, add these two actions:
    - **Change Custom Attribute Value** with the name of your lead scoring attribute (such as `lead score`). If you haven’t created a lead scoring attribute yet, follow the steps in [Custom attributes]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/). This will enter users into the Canvas whenever their lead score changes.
    - **Add an Email Address**

![Step 2 of creating a Canvas with the entry schedule of “Action-Based” and action-based options of changing a custom attribute “lead score” and adding an email address.]({% image_buster /assets/img/b2b/step_2_simple.png %}){: style="max-width:80%;"}

### Step 3: Identify your target audience

#### Step 3a: Select segments

All users are eligible for lead scoring, so you can add company-specific rules about who to score by selecting which user [segments]({{site.baseurl}}/user_guide/engagement_tools/segments/) to target and applying additional [filters]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/). For example, you can exclude employees, users who are already customers, and similar. 

![Step 3 of creating a Canvas with options for selecting segments and filters to narrow down the entry audience.]({% image_buster /assets/img/b2b/step_3_simple.png %}){: style="max-width:80%;"}

#### Step 3b: Set Canvas re-eligibility

A user will go through this Canvas many times throughout their lifecycle with you, so make sure they can re-enter as quickly as they exited the previous time. This can be accomplished through re-eligibility settings. 

In **Entry Controls**, do the following:
- Select **Allow users to re-enter this Canvas**.
- Select **Specified Window**.
- Set the re-eligibility to “0” **seconds**.

![“Entry Controls” section that has selections for “Allow users to re-enter this Canvas” in a “Specified Window” of 0 seconds.]({% image_buster /assets/img/b2b/entry_controls_simple.png %}){: style="max-width:80%;"}

#### Step 3c: Update send settings

Given the operational nature of this Canvas and the fact that no messages will be sent to these users, you don’t need to adhere to subscription statuses.

Under **Subscription Settings**, for **Send to these users:** select **all users including unsubscribed users**. 

![Step 4 of creating a Canvas for setting message sending options.]({% image_buster /assets/img/b2b/step_4_simple.png %}){: style="max-width:80%;"}

### Step 4: Build your Canvas

#### Step 4a: Add an Action Path

Under your variant, select the plus icon and then select **Action Paths**.

![Canvas with “Action Paths” displaying in the menu opened by the plus icon.]({% image_buster /assets/img/b2b/action_paths_simple.png %}){: style="max-width:60%;"}

#### Step 4b: Create Action Groups

Each Action Group will represent all the actions that lead to the same point increment or decrement. You can set up to eight Action Groups. In this scenario, we'll be setting up four groups.

Add the following groups to your Action Path:

- **Group 1:** All events that count for a 1-point increment.
- **Group 2:** All events that count for a 5-point increment.
- **Group 3:** All events that count for a 1-point decrement.
- **Everyone Else:** Action Paths allow you to define the window to wait and see if a user takes an action, before dropping them into an “everyone else” group. For lead scoring, this is an opportunity to decrement the score for “inactivity”.

![Action Path containing Action Groups for adding one point, five points, and ten points; subtracting one point and ten points; and “Everyone Else”.]({% image_buster /assets/img/b2b/action_paths_selected_simple.png %}){: style="max-width:20%;"}

#### Step 4c: Configure each group to include the relevant events

In each Action Group, select **Select trigger** and choose the event that will add the number of points for that particular Action Group. Add more triggers to include all the events that will increment the lead score by one. For example, a user could increment their score by one when they start a session in any app or perform a custom event (such as registering or joining a webinar). 

![Action Group for adding a point with the triggers of “Starting Session in Any App” and “Performing Custom Event”.]({% image_buster /assets/img/b2b/action_groups_simple.png %}){: style="max-width:80%;"}

#### Step 4d: Add User Update steps

Add a User Update step to each Canvas path created below your Action Path. 

![Canvas displaying the Action Path with branched User Update paths for each Action Group.]({% image_buster /assets/img/b2b/user_update_paths_simple.png %}){: style="max-width:80%;"}

{: start=”2”}
In each User Update step’s **Compose** tab, do the following for the respective fields:

| Field | Action |
| --- | --- |
| **Attribute Name** | Select the lead score attribute you selected in step 2 (`lead score`).|
| **Action** | Change the action to **Increment By** if the path increases the score or **Decrement By** if the path decreases the score |
| **Increment By** or **Decrement By** | Enter the number of points that will be increased or decreased from the lead score.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Step 5: Launch your Canvas

That’s it! Your lead scoring Canvas is ready to launch.

## External lead scoring

Whether using one of our [technology partners]({{site.baseurl}}/partners/home/), your own internal lead scoring model, machine learning, or another lead scoring tool, we have multiple options for you.

### External partners

Check out [Technology partners]({{site.baseurl}}/partners/home) to learn about our B2B partners that offer lead-scoring capabilities. Don’t see your tool there? You can integrate by calling our [`users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track#track-users) API endpoint. 

### Internal lead scoring data models

You can integrate Braze with your internal data models, including lead scoring models, in various ways. See below for some common examples of how our customers have integrated with Braze.

#### Integrated cloud data warehouse

{% tabs %}
{% tab Braze as a data source %}

As your marketing tool, Braze contains extremely relevant data that could supplement your team’s internal lead score model. 

For example, messaging engagement data (such as email opens and clicks, landing page engagement, and others) can determine a lead’s engagement level. You can pass this data back to your cloud data warehouse and make it available as input for your lead scoring models by using Braze streaming export data solutions:

- [Braze Currents]({{site.baseurl}}/user_guide/data/braze_currents/)
- [Snowflake Secure Data Sharing]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/)

{% endtab %}
{% tab Braze as a destination %}

After your internal teams have created and run your lead scoring model, you can pull that data back into Braze so you can better segment and target leads for relevant messaging. You can do this with [Braze Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/cloud_ingestion/overview/). 

With Cloud Data Ingestion, your internal teams will create a new table or view with your user identifiers, the latest lead scores, and the timestamps when the scores were updated. Braze will pick up the table or view and add the lead scores to the user profiles.

{% endtab %}
{% endtabs %}

## Lead handoff: Marketing Qualified Lead (MQL) to Sales {#lead-handoff}

Our recommended approach to lead handoffs is to have a corresponding lead or contact attached to each user in Braze. These leads would enter your Sales teams’ queue when their lead statuses change to an MQL stage, at which point Salesforce would kick off a lead routing or assignment workflow. 

To update the lead record in Salesforce with the lead status from Braze, we recommend using a triggered webhook template.

### Step 1: Create a webhook campaign

### Step 2: Configure your webhook

#### Step 2a: Compose webhook

1. Give your webhook campaign a name, such as “Salesforce > Update lead to MQL”.

2. Enter your webhook URL in the format of {% raw %}`https://YOUR_SALESFORCE_INSTANCE.my.salesforce.com/services/data/v60.0/sobjects/Lead/{{${user_id}}}`{% endraw %}. The Braze user ID of {% raw %}`{{$user_id}}}`{% endraw %} should match your Salesforce contact ID. If not, use an alias instead of {% raw %}`{{$user_id}}}`{% endraw %}.

3. Update the **HTTP Method** to **PATCH**.

4. Configure your payload to only update the lead record in Salesforce if that lead’s lead score crosses your predefined threshold. See the example request body below for a lead score of greater than 100.

{% raw %}
```liquid
{% assign threshold = 100%}
{% if custom_attribute.${lead score} > threshold %}
{
"lead_status": "MQL"
}
{% else %}{% abort_message('not at threshold')%}
{% endif %}
```
{% endraw %}

{: start="5"}
5. Include the following headers:

| Header | Content |
| --- | --- |
| Authorization | {% raw %}`Bearer {{result.access_token}}`{% endraw %}<br><br>To retrieve a token, [configure a connected app](https://help.salesforce.com/s/articleView?id=sf.connected_app_client_credentials_setup.htm&type=5) for the OAuth 2.0 client credentials flow and then use Connected Content to retrieve the bearer from Salesforce: <br><br>{% raw %}<code>{% connected_content https://[instance].my.salesforce.com/services/oauth2/token <br>:method post <br> :body client_id=[client_id]&client_secret=[client_secret]&grant_type=client_credentials <br>:save result %}{% endraw %} <br> Bearer {% raw %}{{result.access_token}}</code>{% endraw %} |
| Content_Type | application/json |
{: .reset-td-br-1 reset-td-br-2}

![Webhook being composed with a Salesforce webhook URL, PATCH HTTP method, raw text request body, and request headers.]({% image_buster /assets/img/b2b/webhook.png %}){: style="max-width:80%;"}

#### Step 2b: Schedule webhook sends

The campaign should trigger anytime the user’s lead score changes. This campaign will trigger for any user whose score changes, but it will only affect users who aren't currently an MQL and have crossed the threshold you set in the previous step.

In the **Schedule Delivery** step, select the following:
- An **Action-Based** delivery type
- A trigger action of **Change Custom Attribute Value** with the name of your lead scoring attribute and an action of **any new value**

#### Step 2c: Identify target audience

In the **Target Audiences** step, include a filter that excludes users whose lead statuses are already at MQL or beyond, such as "`lead_status` `is none of` `MQL`".

![Webhook targeting options with the filter of “lead_status” is none of “MQL”.]({% image_buster /assets/img/b2b/step_3_webhook.png %}){: style="max-width:80%;"}

### Step 3: Launch campaign

Select **Launch** and watch your lead status change in Salesforce as your customers cross the MQL lead score threshold.

