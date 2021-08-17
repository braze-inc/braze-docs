---
nav_title: Transcend
article_title: Transcend
page_order: 1
description: "Transcend, a data privacy infrastructure platform, helps automate fulfillment of data subject requests by orchestrating data across dozens of data systems, including Braze."
alias: /partners/transcend/
page_type: partner
search_tag: Partner

---

# Transcend

> Transcend is a data privacy infrastructure company that makes it simple for companies to give their users control over their personal data, automatically fulfilling data subject requests inside companies across all of their data systems and vendors. Transcend provides their end-users with a control panel, or "Privacy Center", hosted at `privacy.\<company\>.com` where users can manage their privacy preferences, export their data, or delete it. By making data subject requests painless for companies, Transcend puts users everywhere in the driver's seat of their personal data.

The Braze and Transcend partnership helps users automate privacy requests by orchestrating data across dozens of data systems. Ultimately, this helps teams comply with regulations like GDPR and CCPA and puts individuals in the driver's seat when it comes to their data.

## Prerequisites

| Prerequisites | Origin | Access | Description |
|---|---|---|---|
| Transcend Account & Account Information | Transcend | [https://app.transcend.io/](https://app.transcend.io/) | An active Transcend account with admin privileges is required to utilize the Braze integration. |
| Braze API Key | Braze | You will need to create a new API key.<br><br>This can be created in the __Developer Console -> API Settings -> Create New API Key__ with __users.track__ permissions. | This API key will be used when connecting the Braze data silo to the Transcend platform. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Transcend and Braze Integration

Transcend allows you to programmatically access, erase, and opt users out of communication in the Braze platform in accordance with data privacy regulations.

### Step 1: Setting up the Braze Integration
To get started, log in to [Transcend](https://app.transcend.io/login).

1. In the Transcend platform, navigate to __Data Map__ > __Add Data Silo__ > __Braze__ and select the __Connect__ button.
2. Use your Braze [dashboard URL]({{site.baseurl}}/api/basics/#endpoints) and dedicated REST API key to connect to the Transcend platform to Braze. 
3. Once connected, navigate back to the Transcend __Privacy Center__ tab. Here, you'll need to map the data in Braze to your __Data Practices__. To do this, create a new category and a new __Data Collection__ with the appropriate naming convention (e.g., "Mailing Lists or User Profile"). When you are done, hit __Publish__.
4. Navigate back to your __Data Map__ and click on the Braze data silo. Expand __Manage Datapoints__ and select the collection label (category) that you created in the previous step from the dropdown. You can also choose which data actions (e.g., access or erasure) are enabled for which data points. 
5. Next, while still in the Braze data silo, expand __Manage Identifiers__. Check the respective boxes for which identifiers you'd like enabled. For example, if you'd like Transcend to search users by email address, you'd check the box to enable the email address identifier.

{% alert note %}
If identifiers are not enabled correctly, Transcend may not be able to process requests for certain users.
{% endalert %}

### Step 2: Testing Requests
Transcend recommends testing requests across your Data Map before you start processing requests from end-users. To do this:

1. Go to __Privacy Center__ and click __View your Privacy Center__.
2. From your __Privacy Center__, click __Take Control__, then __Download my data__. You'll need to enter your email or log in to authenticate yourself before submitting the request.
3. Check your email for a message from Transcend. You'll be asked to click on a verification link to verify the request.
4. Next, back in the __Admin Dashboard__, navigate to the __Incoming Requests__ tab, and select your request. If you don't see the request here, contact Transcend at [support@transcend.io](mailto:support@transcend.io).
5. Once you've clicked into your request, navigate to the __Data Silos__ tab and select __Braze__. Inspect and confirm the data returned.
6. Finally, navigate to the __Report tab__ and click __Approve and Send__. You should receive the report at the email address you submitted with the request.

### Step 3: Removing the Braze integration

1. To remove the Braze data silo from your __Data Map__, navigate to your __Data Map__, and click into __Braze__. 
2. At the bottom of the screen, expand __Remove Braze__, and click __Remove Silo__. You'll be prompted to confirm that you'd like to remove the silo. Click __Ok__. 
3. Confirm the silo has been removed by navigating back to your __Data Map__.

[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)
