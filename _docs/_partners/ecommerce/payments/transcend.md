---
nav_title: Transcend
article_title: Transcend
description: "This reference article outlines the partnership between Braze and Transcend, a data privacy infrastructure platform, that helps Braze users automate fulfillment of data subject requests."
alias: /partners/transcend/
page_type: partner
search_tag: Partner

---

# Transcend

> Transcend is a data privacy infrastructure company that makes it simple for companies to give their users control over their data, automatically fulfilling data subject requests inside companies across all of their data systems and vendors. 

_This integration is maintained by Transcend._

## About the integration

The Braze and Transcend partnership helps users automate privacy requests by orchestrating data across dozens of data systems, helping teams comply with regulations like GDPR and CCPA. Transcend provides end-users with a control panel, or privacy center, hosted at `privacy.\<company\>.com` where users can manage their privacy preferences, export their data, or delete it. 

## Prerequisites

| Requirements | Description |
|---|---|
| Transcend account | A [Transcend](https://app.transcend.io/) account with admin privileges is required to take advantage of this partnership. |
| Braze API key | A Braze REST API key with `users.delete, users.alias.new, users.export.ids, email.unsubscribe,`and `email.blacklist` permissions.<br><br>This can be created in the Braze dashboard from **Settings** > **API Keys**. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

Transcend allows you to programmatically access, erase, and opt users out of communication in the Braze platform in accordance with data privacy regulations.

### Step 1: Set up the Braze integration
To get started, log in to [Transcend](https://app.transcend.io/login).
1. Navigate to **Data Map > Add Data Silo > Braze** and select the **Connect** button.<br><br>
2. When your account is provisioned, you will log in to one of the corresponding URLs: `https://dashboard-01.braze.com`, `https://dashboard-02.braze.com, ..., https://dashboard-01.braze.eu`.<br> Use the following [table]({{site.baseurl}}/api/basics/#endpoints) to figure out what subdomain you should include based on your dashboard URL.<br><br>
3. When connected, navigate to the Transcend **Privacy Center** tab. Here, you'll need to map the data in Braze to your data practices. To do this, create a new category and a new Data Collection with the appropriate naming convention (for example, "Mailing Lists or User Profile"). When completed, select **Publish**.<br><br>
4. Navigate back to your Data Map and select the Braze data silo. Expand **Manage Datapoints** and select the collection label (category) you created in the previous step from the dropdown. You can also choose which data actions (for example, access or erasure) are enabled for which data points. <br><br>
5. Next, while still in the Braze data silo, expand **Manage Identifiers**. Check the respective boxes for which identifiers you'd like enabled. For example, if you'd like Transcend to search users by email address, you'd check the box to enable the email address identifier.

{% alert note %}
If identifiers are not enabled correctly, Transcend may not process requests for certain users.
{% endalert %}

### Step 2: Test requests
Transcend recommends testing requests across your Data Map before you start processing requests from end-users.
1. Go to **Privacy Center** in Transcend and select **View your Privacy Center**.<br><br>
2. From your **Privacy Center**, select **Take Control**, then **Download my data**. Enter your email or log in to authenticate yourself before submitting the request.<br><br>
3. Check your email for a message from Transcend. You'll be asked to click on a verification link to verify the request.<br><br>
4. Next, back in the **Admin** dashboard, navigate to the **Incoming Requests** tab, and select your request. Contact Transcend at [support@transcend.io](mailto:support@transcend.io) if you don't see the request here.<br><br>
5. After you've clicked into your request, navigate to the **Data Silos** tab and select **Braze**. Inspect and confirm the data returned.<br><br>
6. Finally, navigate to the **Report** tab and click **Approve and Send**. You should receive the report at the email address you submitted with the request.

## Remove the Braze integration
To remove the Braze data silo from your Transcend Data Map:
1. Navigate to your **Data Map**, and click into **Braze**. <br><br>
2. At the bottom of the screen, expand **Remove Braze** and click **Remove Silo**. You'll be prompted to confirm that you'd like to remove the silo. Click **Ok**. <br><br>
3. Confirm the silo has been removed by navigating back to your Data Map.


