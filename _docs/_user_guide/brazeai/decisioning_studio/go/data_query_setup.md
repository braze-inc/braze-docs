---
nav_title: Setting up SFMC data query automation
article_title: Setting up SFMC data query automation for BrazeAI Decisioning Studio
page_order: 2
description: "Learn how to set up and integrate BrazeAI Decisioning Studio<sup>TM</sup> Go into Braze."
---

# Setting up SFMC data query automation for BrazeAI Decisioning Studio™ Go

> Set up your data query automation in Salesforce Marketing Cloud and integrate with BrazeAI Decisioning Studio™ Go.

## Step 1: Create a new automation

1. From your Salesforce Marketing Cloud home, go to **Journey Builder** and select **Automation Studio**.

![]({% image_buster /assets/img/decisioning_studio_go/query13.png %})

{: start="2"}
2. Select **New Automation**.
3. Drag and drop a **Schedule** node as the **Starting Source**.

![]({% image_buster /assets/img/decisioning_studio_go/query14.png %})

{: start="4"}
4. In the **Schedule** node, select **Configure**.
5. Set the following for the schedule: 
    - **Start Date:** Tomorrow's calendar day 
    - **Time:** **12:00 AM** 
    - **Time Zone:** **(GMT-05:00) Eastern (US & Canada)**
6. For **Repeat**, select **Daily**.
7. Set this schedule to never end.
8. Select **Done** to save the schedule.

![]({% image_buster /assets/img/decisioning_studio_go/query12.png %})

## Step 2: Create your SQL queries

Next, we'll create 2 SQL queries: a subscribers query and an engagement query. These queries allow BrazeAI Decisioning Studio™ Go to retrieve data to populate the audience and ingest engagement events.

{% tabs %}
{% tab Subscribers query %}
1. Drag and drop an **SQL Query** into the canvas.
2. Select **Choose**.
3. Select **Create New Query Activity**.
4. Give the query a name and external key. We recommend using the suggested name and external key for the subscriber query provided in your BrazeAI Decisioning Studio™ Go portal. 

![]({% image_buster /assets/img/decisioning_studio_go/query11.png %})

{: start="5"}
5. Select **Next**.
6. In your BrazeAI Decisioning Studio™ Go portal, locate the System data SQL query under **Subscriber Query Resources**.
7. Copy and paste the query into the text box and select **Next**.

![]({% image_buster /assets/img/decisioning_studio_go/query10.png %})

{: start="8"}
8. In your BrazeAI Decisioning Studio™ Go portal, in the the **Resources to use** section, locate the external key of the target data extension. Then, paste it into the search box to search.

![]({% image_buster /assets/img/decisioning_studio_go/query9.png %})

{: start="9"}
9. Select the data extension that matches the external key you searched for. The target data extension name is also provided in your BrazeAI Decisioning Studio™ Go portal to cross-reference. The **Data Extension** for the subscriber query should end in a `BASE_AUDIENCE_DATA` suffix.

![]({% image_buster /assets/img/decisioning_studio_go/query8.png %})

{: start="10"}
10. Select **Overwrite** then **Next**.
{% endtab %}
{% tab Engagement query %}
1. Drag and drop an **SQL Query** into the canvas.

![]({% image_buster /assets/img/decisioning_studio_go/query7.png %})

{: start="2"}
2. Select **Choose**.
3. Select **Create New Query Activity**.
4. Give the query a name and external key. We recommend using the suggested name and external key for the engagement query provided in your BrazeAI Decisioning Studio™ Go portal. 

![]({% image_buster /assets/img/decisioning_studio_go/query6.png %})

{: start="5"}
5. Select **Next**.
6. In your BrazeAI Decisioning Studio™ Go portal, locate the System data SQL query under **Engagement Query Resources**.
7. Copy and paste the query into the text box and select **Next**.

![]({% image_buster /assets/img/decisioning_studio_go/query5.png %})

{: start="8"}
8. Locate and select the target Data Extension for the Engagement Query specified in your BrazeAI Decisioning Studio™ Go portal. 

{% alert tip %}
The target data extension name is also provided in your BrazeAI Decisioning Studio™ Go portal to cross-reference.  Make sure you're looking at the target Data Extension for the Engagement Query. The **Data Extension** for the engagement query should end with an ENGAGEMENT_DATA suffix.
{% endalert %}

![]({% image_buster /assets/img/decisioning_studio_go/query4.png %})

{: start="9"}
9. Select **Overwrite** then **Next**.

{% endtab %}
{% endtabs %}

## Step 3: Run the automation

1. Give the automation a name and select **Save**.

![]({% image_buster /assets/img/decisioning_studio_go/query3.png %})

{: start="2"}
2. Next, select **Run Once** to confirm everything is working as expected.
3. Select both queries and select **Run**.

![]({% image_buster /assets/img/decisioning_studio_go/query2.png %})

{: start="4"}
4. Select **Run Now**.

![]({% image_buster /assets/img/decisioning_studio_go/query1.png %})

Now, you can check to make sure the automation is running successfully. Contact Braze Support for further assistance if your automation isn't running as expected.
