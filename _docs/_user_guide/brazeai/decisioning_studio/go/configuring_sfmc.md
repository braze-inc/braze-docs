---
nav_title: Configuring with Salesforce Marketing Cloud
article_title: Configuring with Salesforce Marketing Cloud for BrazeAI Decisioning Studio Go
page_order: 5
description: "Learn how to set up a data query automation and Journey in Salesforce Marketing Cloud for use with BrazeAI Decisioning Studio<sup>TM</sup> Go."
toc_headers: h2
---

# Configuring with Salesforce Marketing Cloud for BrazeAI Decisioning Studio™ Go

> Set up a Journey in Salesforce Marketing Cloud (SFMC) to begin triggering sends through BrazeAI Decisioning Studio™ Go.

## Setting up a data query automation

### Step 1: Create a new automation

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

### Step 2: Create your SQL queries

Next, we'll create 2 SQL queries: a subscribers query and an engagement query. These queries allow BrazeAI Decisioning Studio™ Go to retrieve data to populate the audience and ingest engagement events.

{% tabs %}
{% tab Subscribers query %}
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
8. In your BrazeAI Decisioning Studio™ Go portal, in the the **Resources to use** section, locate the external key of the target data extension. Then, paste it into the search bar to search.

![An external key pasted into the search bar]({% image_buster /assets/img/decisioning_studio_go/query9.png %})

{: start="9"}
9. Select the data extension that matches the external key you searched for. The target data extension name is also provided in your BrazeAI Decisioning Studio™ Go portal to cross-reference. The **Data Extension** for the subscriber query should end in a `BASE_AUDIENCE_DATA` suffix.

![The data extension name that matches the example external key.]({% image_buster /assets/img/decisioning_studio_go/query8.png %})

{: start="10"}
10. Select **Overwrite** then **Next**.
{% endtab %}
{% tab Engagement query %}
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
The target data extension name is also provided in your BrazeAI Decisioning Studio™ Go portal to cross-reference.  Make sure you're looking at the target Data Extension for the Engagement Query. The **Data Extension** for the engagement query should end with an ENGAGEMENT_DATA suffix.
{% endalert %}

{: start="9"}
9. Select **Overwrite** then **Next**.

![The data extension name that matches the example external key.]({% image_buster /assets/img/decisioning_studio_go/query4.png %})

{% endtab %}
{% endtabs %}

### Step 3: Run the automation

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

## Creating your SFMC Journey

### Step 1: Set up the Journey

1. In Salesforce Marketing Cloud, go to **Journey Builder** > **Journey Builder**.
2. Select **Create New Journey**.
3. For your journey type, select **Multi-Step Journey**, then select **Create**.

![An API Event entry source connected to a Decision Split node and multiple Email nodes.]({% image_buster /assets/img/decisioning_studio_go/journey1.png %})

### Step 2: Build the Journey

#### Step 2.1: Create an entry source

1. For your entry source, drag **API Event** to the Journey Builder.

!["API Event" selected as the entry source.]({% image_buster /assets/img/decisioning_studio_go/journey2.png %})

2. In the **API Event**, select **Create an event**.

![The "create an event" option in the API Event.]({% image_buster /assets/img/decisioning_studio_go/journey3.png %})

{: start="3"}
3. Select **Select Data Extension**. Locate and select the data extension that BrazeAI Decisioning Studio™ Go will be writing recommendations to.
4. Select **Summary** to save your changes.
5. Select **Done** to save the API event.

![API event summary.]({% image_buster /assets/img/decisioning_studio_go/journey4.png %}){: style="max-width:80%;"}

#### Step 2.2: Add a Decision Split

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

#### Step 2.3: Add an Email for each Decision Split

1. Drag an **Email** node into each path of the **Decision Split**.
2. Select **Email**, then select the appropriate template that should go in each Path (meaning the template with the ID value should match the logic in your Decision Split).

![An Email node added to the Journey.]({% image_buster /assets/img/decisioning_studio_go/journey9.png %})

### Step 3: Activate the Journey

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
