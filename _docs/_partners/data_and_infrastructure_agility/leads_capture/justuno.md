---
nav_title: Justuno
article_title: Justuno
description: "DESCRIPTION."

alias: /partners/justuno
page_type: partner
search_tag: Partner
---

# Justuno

> [Justuno](https://www.justuno.com/) is...


## Use cases

Braze allows any marketer to collect and take action on any amount of data from any source, so they can creatively engage with customers in real time, across channels from one platform.

Integrating Justuno and Braze will give you the best of both worlds. Users will be able to combine the customer data saved in Braze with the visitor and customer data saved in Justuno and create more personalized experiences for the all audiences. This will increase the effectiveness of the marketing campaigns and customer engagements.

## Prerequisites

| Braze Rest API key | A Braze REST API key with the `users.track` and `custom_attributes.get` permissions.<br><br>This can be created in the Braze dashboard from **Settings** > **API Keys**. |
| Braze REST endpoint | Your REST endpoint URL. Your endpoint will depend on the [Braze URL for your instance][2].|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integrating Justuno with Braze

### Step 1: Sync lead-capture workflows

To send profile data collected with Justuno to a specific Braze Email or SMS Subscription Groups, you'll need the following information from the Braze dashboard.

| ID Type                          | Required? | Description                                                                                                   |
|----------------------------------|-----------|---------------------------------------------------------------------------------------------------------------|
| Braze SMS Subscription Group ID  | Yes       | This ID is used to collect SMS consent from user profiles. If no ID is entered in Justuno, profiles will not have consent when Justuno pushes that profile to Braze. |
| Braze Email Subscription Group ID | No        | If this ID is not entered in Justuno, Justuno will send the profile data to Braze as a user with no associated subscription groups. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

To locate these IDs:

1. In Braze, go to **Audience** > **Subscriptions**.
2. For each subscription group, note the ID located in the ID column.

{% alert tip %}
Keep these IDs close by, so you can easily reference them later.
{% endalert %}

### Step 2: Create custom attributes in Braze

Before you can sync any user attributes from Justuno, you'll need to create the equivalent custom attributes in Braze if you haven't already.

To create and manage custom attributes in Braze, go to **Data Settings** > **Custom Attributes**, then create your custom attributes. For a full walkthrough, see [Managing custom attributes in Braze]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/).

### Step 3: Set up Justuno workflow

After the integration is set up, the following attributes will be automatically synced to Braze from Justuno:

- Email  
- Phone  
- First Name  
- Last Name  
- Language  
- Gender  
- Country

To sync additional attributes:

1. In your Justuno Workflow, select **Sync Another Property**.
2. Choose which Braze attributes you'd like to sync.
3. Match the properties in Justuno with their Braze equivalents (such as social handles, birthday, shopping preferences, survey responses, etc.). Keep in mind, these properties are considered 0 party data or 1st party data. To learn more, see [Justuno: Visitor data collection](https://www.justuno.com/guides/zero-first-party-data/).
4. In the workflow builder, choose to **Save**, **Preview**, or **Publish** your workflow.

## Things to know

- Users must manually input the subscription group ID in the app settings.  
- The following Braze data types are **not supported**: Object, Object Array.  
- Implicit SMS consent is provided when Justuno's SMS consent field is not used.  
- Explicit SMS consent is respected if the Justuno design includes the consent field.
