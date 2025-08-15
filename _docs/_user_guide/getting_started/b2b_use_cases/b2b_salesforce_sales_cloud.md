---
nav_title: Salesforce sales cloud
article_title: Managing leads with Salesforce Sales Cloud
page_order: 3
page_type: reference
description: "Learn how to use Braze webhooks to create and update leads in Salesforce Sales Cloud through the Salesforce sobjects/Lead endpoint."
---

# Managing leads with Salesforce Sales Cloud

> [Salesforce](https://www.salesforce.com/) is one of the world’s leading cloud-based Customer Relationship Management (CRM) platforms designed to help businesses manage their entire sales process, including lead generation, opportunity tracking, and account management.<br><br>This page demonstrates how to use Braze webhooks to create and update leads in Salesforce Sales Cloud through a community-submitted integration.

{% alert important %}
This is a community-submitted integration and isn’t directly supported by Braze. Only official Braze-provided webhook templates are supported by Braze. 
{% endalert %}

## How it works

The Braze and Salesforce Sales Cloud integration uses Braze webhooks to create and update leads in Salesforce Sales Cloud through the Salesforce [sobjects/Lead](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_lead.html) endpoint.

Braze currently offers two integrations to Salesforce Sales Cloud for the following use cases:
1. [Creating a lead in Salesforce Sales Cloud](#creating-lead)
2. [Updating a lead in Salesforce Sales Cloud](#updating-lead)

{% alert note %}
This integration is purely to update Salesforce from Braze as part of your lead acquisition and nurturing efforts. For syncing data from Salesforce back to Braze, check out [B2B data model]({{site.baseurl}}/user_guide/getting_started/b2b_use_cases/b2b_data_models/) or connect with one of our [technology partners]({{site.baseurl}}/partners/home/). 
{% endalert %}

## Prerequisites

This integration requires you to create a connected app in Salesforce Sales Cloud by following the steps in the Salesforce documentation: [Configure a Connected App for the OAuth 2.0 Client Credentials Flow](https://help.salesforce.com/s/articleView?id=sf.connected_app_client_credentials_setup.htm&type=5).

When you configure the necessary OAuth settings for the connected app, keep all oAuth settings with their default values and selections except for the following:
1. Select **Enable for device** flow. You can leave **Callback URL** blank, as it will default to a placeholder.
2. For selected **OAuth Scopes**, add **Manage user data via APIs (api)**.
3. Select **Enable Client Credentials Flow**.

## Creating a lead in Salesforce Sales Cloud {#creating-lead}

As your customer engagement platform, Braze can generate new leads based on user flows such as filling out a form on a landing page. When that happens, you can use a Braze Salesforce Sales Cloud webhook to create a corresponding lead in Salesforce.

### Step 1: Collect your `client_id` and `client_secret`

1. In Salesforce, go to **Platform Tools** > **Apps** > **App Manager**.
2. Find your newly created Braze App and select **View**.
3. Under **Consumer Key and Secret**, select **Manage Consumer Details**.
4. On the resulting page, take note of your **Consumer Key** and **Consumer Secret**. The **Consumer Key** is your `client_id`, and the **Consumer Secret** is your `client_secret`.

### Step 2: Set up your webhook template

Use templates to quickly re-use this webhook across the Braze platform. 

1. In Braze, go to **Templates**, select **Webhook Templates**, then select **+ Create Webhook Template**.
2. Provide a name for the template, such as “Salesforce Sales Cloud > Create Lead”.
3. In the **Compose** tab, enter the following details:

#### Compose webhook 

| Field | Details |
| --- | --- |
| Webhook URL | {% raw %}`https://[insert_instance_name].my.salesforce.com/services/data/v60.0/sobjects/Lead/`{% endraw %} |
| HTTP method | `POST` |
| Request Body | JSON Key/Value Pairs |
{: .reset-td-br-1 .reset-td-br-2 role=”presentation” }

#### Body property key values

Select **+ Add New Body Property** for each of the key/value pairs you want to map over from Braze to Salesforce. You can map over any field you want, so the following table is just one example.

| Key | Value |
| --- | --- |
| firstName | {% raw %}`{{${first_name}}}`{% endraw %} |
| lastName | {% raw %}`{{${last_name}}}`{% endraw %} |
| email | {% raw %}`{{${email_address}}}`{% endraw %} |
| company | {% raw %}`{{custom_attribute.${company}}}`{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 role=”presentation” }

#### Request headers

Select **+ Add New Header** for each of the following request headers.

| Key | Value |
| --- | --- |
| Authorization | {% raw %}`{% connected_content https://[insert_instance_name].my.salesforce.com/services/oauth2/token     :method post     :body client_id=[insert_client_id]&client_secret=[insert_client_secret]&grant_type=client_credentials     :save result %}Bearer {{result.access_token}}`{% endraw %} |
| Content-Type | `application/json` |
{: .reset-td-br-1 .reset-td-br-2 role=”presentation” }

{: start="4" }
4. Select **Save Template**.

![A filled-out webhook template to create a lead.]({% image_buster /assets/img/b2b/create_lead_webhook.png %}){: style="max-width:70%;"}
 
## Updating a lead in Salesforce Sales Cloud {#updating-lead}

To set up a Braze Salesforce Sales Cloud webhook that updates leads in Salesforce, you need a common identifier between Salesforce Sales Cloud and Braze. The example below uses the Salesforce `lead_id` as the Braze `external_id`, but you can also accomplish this by using a `user_alias`. For details on this, refer to [B2B Data]({{site.baseurl}}/user_guide/getting_started/b2b_use_cases/b2b_data_models)

This example specifically demonstrates how to update a lead’s lead stage to “MQL” (Marketing Qualified Lead) after a lead crosses a certain lead threshold. This is a core part of our [B2B lead scoring workflow]({{site.baseurl}}/user_guide/getting_started/b2b_use_cases/lead_scoring/) use case.

### Step 1: Collect your `client_id` and `client_secret`

1. In Salesforce, go to **Platform Tools** > **Apps** > **App Manager**.
2. Find your newly created Braze App and select **View**.
3. Under **Consumer Key and Secret**, select **Manage Consumer Details**.
4. On the resulting page, take note of your **Consumer Key** and **Consumer Secret**.
    - The **Consumer Key** is your `client_id`, and the **Consumer Secret** is your `client_secret`.

### Step 2: Set up your webhook template

1. In Braze, go to **Templates**, select **Webhook Templates**, then select **+ Create Webhook Template**.
2. Provide a name for the template, such as “Salesforce Sales Cloud > Update Lead to MQL”.
3. In the **Compose** tab, enter the following details:

#### Compose webhook 

| Field | Details |
| --- | --- |
|Webhook URL | {% raw %}`https://[insert_instance_name].my.salesforce.com/services/data/v60.0/sobjects/Lead/{{${user_id}}}`{% endraw %} |
| HTTP method | `PATCH` |
| Request Body | JSON Key/Value Pairs |
{: .reset-td-br-1 .reset-td-br-2 role=”presentation” }

#### Body property key values

Select **+ Add New Body Property** for the following key/value pair. Note that `Lead_Stage__c` is an example name. The custom field you use to track MQLs in Salesforce may have a different name, so make sure that they match.

| Key | Value |
| --- | --- |
| `Lead_Stage__c` | `MQL` |
{: .reset-td-br-1 .reset-td-br-2 role=”presentation” }

#### Request headers

Select **+ Add New Header** for each of the following request headers.

| Key | Value |
| --- | --- |
| Authorization | {% raw %}`{% connected_content https://[insert_instance_name].my.salesforce.com/services/oauth2/token     :method post     :body client_id=[insert_client_id]&client_secret=[insert_client_secret]&grant_type=client_credentials     :save result %}Bearer {{result.access_token}}`{% endraw %} |
| Content-Type | `application/json` |
{: .reset-td-br-1 .reset-td-br-2 role=”presentation” }

{: start="4"}
4. Select **Save Template**.

![A filled-out webhook template to update a lead.]({% image_buster /assets/img/b2b/update_lead_webhook.png %}){: style="max-width:70%;"}

## Using these webhooks in an operational workflow

You can quickly add your templates to your operational workflows in Braze, such as:

1. Part of a [new user campaign](#new-lead) that creates a lead in Salesforce
2. Part of a [lead scoring Canvas](#lead-scoring) that updates users who have crossed your MQL threshold to “MQL”, and that updates Salesforce Sales Cloud with the same information

### New lead campaign {#new-lead}

To create a lead in Salesforce when a user provides their email address, you can create a campaign that uses the “Update Lead” webhook template and triggers when a user adds their email address (for example, fills out a web form).

![Step 2 of creating a campaign that is action-based and has the trigger action of “Add an Email Address”.]({% image_buster /assets/img/b2b/salesforce_create_campaign.png %}){: style="max-width:70%;"}

### Lead scoring Canvas for crossing the Marketing Qualified Lead (MQL) threshold {#lead-scoring}

This webhook is covered in the [lead scoring]({{site.baseurl}}/user_guide/getting_started/b2b_use_cases/lead_scoring/#lead-handoff) use case, but you can also check for MQLs and directly update Salesforce within the lead scoring Canvas (as opposed to creating a separate webhook campaign): 

Add a subsequent step to your user update to check if a user has crossed your defined MQL threshold. If they have crossed, update the user’s status to “MQL”, and then update Salesforce with the same “MQL” status by using this webhook template. Salesforce takes care of the rest by routing this lead to the appropriate sales teams using your defined lead routing rules.  

#### Adding Canvas step to check for users who passed the MQL threshold 

1. Add an **Audience Path** step with two groups: “MQL Threshold” and “Everyone Else”.
2. In the “MQL Threshold” group, look for any users who currently don’t have a status of “MQL” (for example, `lead_stage` equals “Lead”), but have a lead score that is over your defined threshold (for example, `lead_score` greater than 50). If so, they move forward to the next step, if not, they exit.

![The “MQL Threshold” Audience Path group with filters for a `lead_stage` equalling “Lead” and a `lead_score` being more than “50”.]({% image_buster /assets/img/b2b/salesforce_check_mql.png %}){: style="max-width:70%;"}

{: start="3" }
3. Add a **User Update** step that updates the user’s `lead_stage` attribute value to “MQL”.

![The “Update to MQL” User Update step that updates the `lead_stage` attribute to have a value of “MQL”.]({% image_buster /assets/img/b2b/salesforce_update_mql.png %}){: style="max-width:70%;"}

{: start="4" }
4. Add a webhook step that updates Salesforce with the new MQL stage.

![The “Update Salesforce” webhook step with completed details.]({% image_buster /assets/img/b2b/salesforce_webhook.png %}){: style="max-width:70%;"}

Now your Canvas flow will update users who’ve crossed your MQL threshold!

![A Canvas user update step that checks if a user crosses the MQL threshold and, if the user does pass, updates Salesforce.]({% image_buster /assets/img/b2b/salesforce_canvas.png %}){: style="max-width:50%;"}

## Troubleshooting

These workflows have limited debugging capability within Salesforce, so we recommend referring to the Braze [Message Activity Log]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab#message-activity-log) to find out why a Webhook failed and if any errors occurred.

For example, an error caused by an invalid URL used for oAuth token retrieval would display as `https://[insert_instance_name].my.salesforce.com/services/oauth2/token is not a valid URL`.

![An error response body stating that the URL isn't a valid URL.]({% image_buster /assets/img/b2b/error_message_invalid_url.png %})

