---
nav_title: Justuno
article_title: Justuno
description: "DESCRIPTION."

alias: /partners/justuno
page_type: partner
search_tag: Partner
---

# Justuno

> [Justuno](https://www.justuno.com/) lets you create fully optimized visitor experiences for all of your audiences with dynamic segments, offering the most advanced targeting available&#8212;all without impacting site speed or increasing dev work. Analyze conversion rates by viewing custom analytics like the number of profiles created, influenced return visitor rate, and pages per session to maintain a marketing advantage in your industry. Justuno enables you to increase revenue per visitor, establish meaningful customer engagements, and grow your business. Optimize the entire audience journey end-to-end with a connected platform.

## Use cases

Braze allows any marketer to collect and take action on any amount of data from any source, so they can creatively engage with customers in real time, across channels from one platform.

Integrating Justuno and Braze gives you the best of both worlds. You can combine the customer data saved in Braze with the visitor and customer data saved in Justuno and create more personalized experiences for all audiences. This increases the effectiveness of your marketing campaigns and customer engagements.

## Prerequisites

| Braze Rest API key | A Braze REST API key with the `users.track` and `custom_attributes.get` permissions.<br><br>This can be created in the Braze dashboard from **Settings** > **API Keys**. |
| Braze REST endpoint | Your REST endpoint URL. Your endpoint will depend on the [Braze URL for your instance]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints).|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integrating Justuno with Braze

### Step 1: Create custom attributes in Braze

To sync user attributes from Justuno to Braze, you'll need to create those attributes in Braze if you haven't already. You can do so by going to **Data Settings** > **Custom Attributes**, then creating your custom attributes. For a full walkthrough, see [Managing custom attributes in Braze]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/).

### Step 2: Add the Braze app to Justuno

#### Step 2.1: Add it to your account

To add the Braze app to your Justuno account, go to **Account Settings** > **Apps**, then search for and select the Braze app.

![The "Connect Apps" page in Justuno with the Braze app shown in the list of search results.]({% image_buster /assets/img/justuno/search-for-braze.png %})

Enter the API key and base URL [you created previously](#prerequisites), then select **Connect**.

![The Braze Authentication pop-up window asking for a Braze API key and base URL.]({% image_buster /assets/img/justuno/authenticate-braze.png %}){: style="max-width:75%;"}

#### Step 2.2: Add it to your workflow

To add the Braze app to your [Justuno workflow](https://hub.justuno.com/knowledge/workflows-overview), drag-and-drop the **Sync to App** action into your workflow, then choose **Select App** > **Braze**.

![The "Select App" option located on the "Sync to App" action.]({% image_buster /assets/img/justuno/select-app.png %}){: style="max-width:45%;"}

### Step 3: Connect your Braze subscription groups

To send profile data from Justuno to a specific Braze email or SMS Subscription Group, you'll need to add their ID to the Braze app in your Justuno workflow.

| ID Type                          | Required? | Description                                                                                                   |
|----------------------------------|-----------|---------------------------------------------------------------------------------------------------------------|
| Braze SMS Subscription Group ID  | Yes       | This ID is used to collect SMS consent from user profiles. If no ID is entered in Justuno, profiles will not have consent when Justuno pushes that profile to Braze. |
| Braze Email Subscription Group ID | No        | If this ID is not entered in Justuno, Justuno will send the profile data to Braze as a user with no associated subscription groups. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

#### Step 3.1: Locate the IDs in Braze

To locate these IDs in the Braze dashboard:

1. Go to **Audience** > **Subscriptions**.
2. For each subscription group, note the ID located in the ID column.

#### Step 3.2: Add the IDs to the Braze app

In your Justuno workflow, open the Braze app, then enter the IDs for each subscription group.

![The Braze app opened in a Justuno workflow with the option to add email and SMS subscription group IDs.]({% image_buster /assets/img/justuno/enter-subscription-groups.png %}){: style="max-width:55%;"}

### Step 4: Configure your attributes

The following attributes are automatically synced from Justuno to Braze:

- Email  
- Phone  
- First Name  
- Last Name  
- Language  
- Gender  
- Country

To sync additional attributes:

1. In the Braze app within your workflow, select **Sync Another Property**.
    ![The Braze app opened in a Justuno workflow showing the "Sync Another Property" option.]({% image_buster /assets/img/justuno/sync-another-property.png %}){: style="max-width:55%;"}
2. Choose which Braze attributes you'd like to sync.
3. Match the properties in Justuno with their Braze equivalents (such as social handles, birthday, shopping preferences, survey responses, and similar). Keep in mind, these properties are considered 0 party data or 1st party data. To learn more, refer to [Justuno: Visitor data collection](https://www.justuno.com/guides/zero-first-party-data/).
4. In the workflow builder, choose to **Save**, **Preview**, or **Publish** your workflow.
    ![The "Publish" menu opened with the options to save, preview, or show version history.]({% image_buster /assets/img/justuno/publish-workflow.png %}){: style="max-width:45%;"}

## Things to know

- You must manually input the subscription group ID in the app settings.  
- The following Braze data types are **not supported**: Object, Object Array.  
- Implicit SMS consent is provided when Justuno's SMS consent field is not used.  
- Explicit SMS consent is respected if the Justuno design includes the consent field.
