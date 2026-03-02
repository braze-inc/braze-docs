---
nav_title: Set up orchestration
article_title: Set up orchestration
page_order: 2
description: "Learn how to connect BrazeAI Decisioning Studio Go to your Customer Engagement Platform to enable personalized communications."
toc_headers: h2
---

# Set up orchestration

> BrazeAI Decisioning Studio™ Go needs to connect to your Customer Engagement Platform (CEP) to orchestrate personalized communications. This article explains how to set up the integration for each supported CEP.

## Supported CEPs

Decisioning Studio Go supports the following Customer Engagement Platforms:

| CEP | Integration Type | Key Features |
|-----|-----------------|--------------|
| **Braze** | API-triggered campaigns | Native integration, real-time triggering |
| **Salesforce Marketing Cloud** | Journey Builder with API Events | SQL query automation, data extensions |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

Select your CEP below to get started with the integration setup.

{% tabs %}
{% tab Braze %}

## Setting up Braze integration

To integrate Decisioning Studio Go with Braze, you'll create an API key, configure an API-triggered campaign, and provide the necessary identifiers to the Decisioning Studio Go portal.

### Step 1: Create a REST API key

1. In the Braze dashboard, go to **Settings** > **APIs and Identifiers** > **API Keys**.
2. Select **Create API Key**.
3. Enter a name for your API key. An example is "DecisioningStudioGoEmail".
4. Select the permissions based on the following categories:
    - **User Data:** select `users.track`, `users.delete`, `users.export.ids`, `users.export.segment`
    - **Messages:** select `messages.send`
    - **Campaigns:** select all listed permissions
    - **Canvas:** select all listed permissions
    - **Segments:** select all listed permissions
    - **Templates:** select all listed permissions

{: start="5"}
5. Select **Create API key**.
6. Copy the API key and paste it into your BrazeAI Decisioning Studio™ Go portal.

### Step 2: Locate your email display name

1. In the Braze dashboard, go to **Settings** > **Email Preferences**.
2. Locate the display name to be used with BrazeAI Decisioning Studio™ Go.
3. Copy and paste the **From Display Name** into the BrazeAI Decisioning Studio™ Go portal as the **Email Display Name**.
4. Copy and paste the associated email address into your BrazeAI Decisioning Studio™ Go portal as the **From email address**, which combines the local part and the domain.

### Step 3: Find your Braze URL and App ID

**To find your Braze URL:**
1. Go to the Braze dashboard.
2. In your browser window, your Braze URL starts with `https://` and ends with `braze.com`. An example Braze URL is `https://dashboard-01.braze.com`.

**To find your App ID (API Key):**

{% alert note %}
Braze offers app IDs (referred to as API keys in the Braze dashboard) that you can use for tracking purposes, such as to associate activity with a specific app in your workspace. If you use app IDs, BrazeAI Decisioning Studio™ Go supports associating an app ID with each experimenter.<br><br>If you do not use app IDs, you can enter any string of characters as a placeholder.
{% endalert %}

1. In the Braze dashboard, go to **Settings** > **App Settings**.
2. Go to the app you want to track.
3. Copy and paste the **API Key** into your BrazeAI Decisioning Studio™ Go portal.

### Step 4: Create an API-triggered campaign

1. In the Braze dashboard, go to **Messaging** > **Campaigns**.
2. Select **Create campaign**.
3. For your campaign type, select **API campaign**.
4. Enter a name for your campaign. An example is "Decisioning Studio Go Email".

![An API campaign named "Decisioning Studio Go Email".]({% image_buster /assets/img/decisioning_studio_go/api_campaign_name.png %})

{: start="5"}
5. For your messaging channel, select **Email**.

![Option to select your messaging channel for API campaign.]({% image_buster /assets/img/decisioning_studio_go/select_api_campaign.png %})

{: start="6"}
6. In **Additional Options**, select the **Allow users to become re-eligible to receive campaign** checkbox.
7. For the time to become re-eligible, enter **1** and select **Hours** from the dropdown.

![Re-eligibility for the API campaign selected.]({% image_buster /assets/img/decisioning_studio_go/additional_options.png %})

{: start="8"}
8. Select **Save Campaign**.

### Step 5: Copy your campaign and message IDs

1. In your API campaign, copy the **Campaign ID**. Then, go to the BrazeAI Decisioning Studio™ Go portal and paste the **Campaign ID**.

![An example message variation ID to be copy and pasted.]({% image_buster /assets/img/decisioning_studio_go/campaign_id.png %})

{: start="2"}
2. Copy the **Message Variation ID**. Then, go to the BrazeAI Decisioning Studio™ Go portal and paste the **Message Variation ID**.

### Step 6: Locate a test user ID

To test your integration, you'll need a user ID:

1. In the Braze dashboard, go to **Audience** > **Search Users**.
2. Search for the user by their external user ID, user alias, email, phone number, or push token.
3. Copy the user ID to reference in your setup.

![Example user profile from locating a user with their ID.]({% image_buster /assets/img/decisioning_studio_go/user_id.png %})

{% endtab %}
{% tab Salesforce Marketing Cloud %}

## Setting up SFMC integration

To integrate Decisioning Studio Go with Salesforce Marketing Cloud, you'll set up an app package, create a data query automation, and build a Journey to handle triggered sends.

### Part 1: Set up an SFMC app package

1. Go to your Marketing Cloud home page.
2. Open the menu in the global header and select **Setup**.
3. Go to **Apps** under **Platform Tools** in the side panel navigation, then select **Installed Packages**.
4. Select **New** to create an app package.
5. Give the app package a name and description.

![An app package with the name "Experimenter 1 - Test 5".]({% image_buster /assets/img/decisioning_studio_go/sfmc_app_package1.png %})

{: start="6"}
6. Select **Add Component**.
7. For the **Component Type**, select **API Integration**. Then, select **Next**.
8. For the **Integration Type**, select **Server-to-server**. Then, select **Next**.
9. Select the following recommended scopes for your app package only:
    - Channels > Email > Read, Write, Send
    - Channels > OTT > Read
    - Channels > Push > Read
    - Channels > SMS > Read
    - Channels > Social > Read
    - Channels > Web > Read
    - Assets > Documents and Images > Read, Write
    - Assets > Saved Content > Read, Write
    - Automation > Automations > Read, Write, Execute
    - Automation > Journeys > Read, Write, Execute, Activate/Stop/Pause/Send/Schedule
    - Contacts > Audiences > Read
    - Contacts > List and Subscribers > Read, Write
    - Cross Cloud Platform > Market Audience > View
    - Cross Cloud Platform > Market Audience Member > View
    - Cross Cloud Platform > Marketing Cloud Connect > Read
    - Data > Data Extensions > Read, Write
    - Data > File Locations > Read
    - Data > Tracking Events > Read, Write
    - Event notifications > Callbacks > Read
    - Event notifications > Subscriptions > Read

{% details Show image of recommended scopes %}

![The recommended scopes for Salesforce Marketing Cloud app package.]({% image_buster /assets/img/decisioning_studio_go/app_package_scopes.png %})

{% enddetails %}

{: start="10"}
10. Select **Save**.
11. Copy and paste the following fields into the BrazeAI Decisioning Studio™ Go portal: **Client Id**, **Client Secret**, **Authentication Base URI**, **REST Base URI**, **SOAP Base URI**.

### Part 2: Set up a data query automation

#### Step 1: Create a new automation

1. From your Salesforce Marketing Cloud home, go to **Journey Builder** and select **Automation Studio**.

![Automation Studio option in Journey Builder navigation.]({% image_buster /assets/img/decisioning_studio_go/query13.png %})

{: start="2"}
2. Select **New Automation**.
3. Drag and drop a **Schedule** node as the **Starting Source**.

!["Schedule" as the starting source of a Journey.]({% image_buster /assets/img/decisioning_studio_go/query14.png %})

{: start="4"}
4. In the **Schedule** node, select **Configure**.
5. Set the following for the schedule:
    - **Start Date:** Tomorrow's calendar day
    - **Time:** **12:00 AM**
    - **Time Zone:** **(GMT-05:00) Eastern (US & Canada)**
6. For **Repeat**, select **Daily**.
7. Set this schedule to never end.
8. Select **Done** to save the schedule.

![An example schedule defined for January 25, 2024 at 12 am ET, to repeat every day.]({% image_buster /assets/img/decisioning_studio_go/query12.png %})

#### Step 2: Create your SQL queries

Next, create 2 SQL queries: a subscribers query and an engagement query. These queries allow BrazeAI Decisioning Studio™ Go to retrieve data to populate the audience and ingest engagement events.

**Subscribers query:**

1. Drag and drop an **SQL Query** into the canvas.
2. Select **Choose**.
3. Select **Create New Query Activity**.
4. Give the query a name and external key. We recommend using the suggested name and external key for the subscriber query provided in your BrazeAI Decisioning Studio™ Go portal.

![An example "OFE_Subscribers_query_Test5" and the external key.]({% image_buster /assets/img/decisioning_studio_go/query11.png %})

{: start="5"}
5. Select **Next**.
6. In your BrazeAI Decisioning Studio™ Go portal, locate the System data SQL query under **Subscriber Query Resources**.
7. Copy and paste the query into the text box and select **Next**.

![An example query in the SQL Query section.]({% image_buster /assets/img/decisioning_studio_go/query10.png %})

{: start="8"}
8. In your BrazeAI Decisioning Studio™ Go portal, in the **Resources to use** section, locate the external key of the target data extension. Then, paste it into the search bar to search.

![An external key pasted into the search bar]({% image_buster /assets/img/decisioning_studio_go/query9.png %})

{: start="9"}
9. Select the data extension that matches the external key you searched for. The target data extension name is also provided in your BrazeAI Decisioning Studio™ Go portal to cross-reference. The **Data Extension** for the subscriber query should end in a `BASE_AUDIENCE_DATA` suffix.

![The data extension name that matches the example external key.]({% image_buster /assets/img/decisioning_studio_go/query8.png %})

{: start="10"}
10. Select **Overwrite** then **Next**.

**Engagement query:**

1. Drag and drop an **SQL Query** into the canvas.

!["SQL Query" added as an activity in the Journey.]({% image_buster /assets/img/decisioning_studio_go/query7.png %})

{: start="2"}
2. Select **Choose**.
3. Select **Create New Query Activity**.
4. Give the query a name and external key. We recommend using the suggested name and external key for the engagement query provided in your BrazeAI Decisioning Studio™ Go portal.

![An example "OFE_Engagement_query" and the external key.]({% image_buster /assets/img/decisioning_studio_go/query6.png %})

{: start="5"}
5. Select **Next**.
6. In your BrazeAI Decisioning Studio™ Go portal, locate the System data SQL query under **Engagement Query Resources**.
7. Copy and paste the query into the text box and select **Next**.

![An example query in the SQL Query section.]({% image_buster /assets/img/decisioning_studio_go/query5.png %})

{: start="8"}
8. Locate and select the target Data Extension for the Engagement Query specified in your BrazeAI Decisioning Studio™ Go portal.

{% alert tip %}
The target data extension name is also provided in your BrazeAI Decisioning Studio™ Go portal to cross-reference. Make sure you're looking at the target Data Extension for the Engagement Query. The **Data Extension** for the engagement query should end with an ENGAGEMENT_DATA suffix.
{% endalert %}

{: start="9"}
9. Select **Overwrite** then **Next**.

![The data extension name that matches the example external key.]({% image_buster /assets/img/decisioning_studio_go/query4.png %})

#### Step 3: Run the automation

1. Give the automation a name and select **Save**.

![An example automation "OFE_Experimenter_Test5_Automation".]({% image_buster /assets/img/decisioning_studio_go/query3.png %})

{: start="2"}
2. Next, select **Run Once** to confirm everything is working as expected.
3. Select both queries and select **Run**.

![An automation "OFE_Experimenter_Test5_Automation" with a list of selected SQL query activities to run.]({% image_buster /assets/img/decisioning_studio_go/query2.png %})

{: start="4"}
4. Select **Run Now**.

![A selected SQL Query activity.]({% image_buster /assets/img/decisioning_studio_go/query1.png %})

Now, you can check to make sure the automation is running successfully. Contact Braze Support for further assistance if your automation isn't running as expected.

### Part 3: Create your SFMC Journey

#### Step 1: Set up the Journey

1. In Salesforce Marketing Cloud, go to **Journey Builder** > **Journey Builder**.
2. Select **Create New Journey**.
3. For your journey type, select **Multi-Step Journey**, then select **Create**.

![An API Event entry source connected to a Decision Split node and multiple Email nodes.]({% image_buster /assets/img/decisioning_studio_go/journey1.png %})

#### Step 2: Build the Journey

**Create an entry source:**

1. For your entry source, drag **API Event** to the Journey Builder.

!["API Event" selected as the entry source.]({% image_buster /assets/img/decisioning_studio_go/journey2.png %})

{: start="2"}
2. In the **API Event**, select **Create an event**.

![The "create an event" option in the API Event.]({% image_buster /assets/img/decisioning_studio_go/journey3.png %})

{: start="3"}
3. Select **Select Data Extension**. Locate and select the data extension that BrazeAI Decisioning Studio™ Go will be writing recommendations to.
4. Select **Summary** to save your changes.
5. Select **Done** to save the API event.

![API event summary.]({% image_buster /assets/img/decisioning_studio_go/journey4.png %}){: style="max-width:80%;"}

**Add a Decision Split:**

1. Drag and drop a **Decision Split** after the **API Entry Event**.
2. In the **Decision Split** details, select **Edit** for the first path.

![Decision Split details with the "Edit" button.]({% image_buster /assets/img/decisioning_studio_go/journey5.png %})

{: start="3"}
3. Update the **Decision Split** to use the template ID passed in by the recommendations data extension. Locate the appropriate field under **Journey Data**.

![The Journey Data section in Path 1 of the Decision Split.]({% image_buster /assets/img/decisioning_studio_go/journey6.png %})

{: start="4"}
4. Select your entry event and locate the desired template ID field, then drag it into the workspace.

![The email template ID to include.]({% image_buster /assets/img/decisioning_studio_go/journey7.png %})

{: start="5"}
5. Enter the template ID of your first email template, then select **Done**.
6. Select **Summary** to save this path.
7. Add a path for each of your email templates, then repeat steps 4-6 above to set the filter criteria so that the template ID matches the ID value of each template.
8. Select **Done** to save the **Decision Split** node.

![Two paths in a Decision Split for each email template ID.]({% image_buster /assets/img/decisioning_studio_go/journey10.png %}){: style="max-width:65%;"}

**Add an Email for each Decision Split:**

1. Drag an **Email** node into each path of the **Decision Split**.
2. Select **Email**, then select the appropriate template that should go in each Path (meaning the template with the ID value should match the logic in your Decision Split).

![An Email node added to the Journey.]({% image_buster /assets/img/decisioning_studio_go/journey9.png %})

#### Step 3: Activate the Journey

After setting up your Journey, activate it and share the following details with the BrazeAI Decisioning Studio™ Go team:

* Journey ID
* Journey name
* API event definition key
* Recommendations data extension external key

{% alert note %}
The BrazeAI Decisioning Studio™ Go portal shows you the SFMC automation it provisioned to export the subscribers and engagement data once daily. If you open this automation in SFMC, make sure to unpause and turn it back to live.
{% endalert %}

1. In the BrazeAI Decisioning Studio™ Go portal, copy the **Journey name**.
2. Next, in Salesforce Marketing Cloud Journey Builder, paste the Journey name into the search bar.
3. Select the Journey name. Note that the Journey is currently in Draft status.
4. Select **Validate**.

![The completed Journey to activate.]({% image_buster /assets/img/decisioning_studio_go/activate3.png %})

{: start="5"}
5. Then, review the validation results and select **Activate**.

![Recommendations listed in the Validation Rules section.]({% image_buster /assets/img/decisioning_studio_go/activate1.png %}){: style="max-width:60%;"}

{: start="6"}
6. In the **Activate Journey** summary, select **Activate** again.

![Summary for the Journey.]({% image_buster /assets/img/decisioning_studio_go/activate2.png %}){: style="max-width:85%;"}

You're all set! You can now begin triggering sends through BrazeAI Decisioning Studio™ Go.

{% endtab %}
{% endtabs %}

## Next steps

Now that you've set up orchestration, proceed to design your agent:

- [Design your agent]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/design_your_agent/)
