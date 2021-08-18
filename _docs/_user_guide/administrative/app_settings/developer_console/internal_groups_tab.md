---
nav_title: Internal Groups Log Tab
article_title: Internal Group Log Tab
page_order: 3
page_type: reference
description: "This reference article covers Internal Groups, a great way to get insight into your test device's SDK or API logs when testing SDK integration."

---

# Internal Groups Tab

Internal Groups are a great way to build and organize internal or 3rd party test groups and provide insight into the SDK or API logs available from your test device during SDK integration testing. You can create an unlimited number of custom Internal Groups with up to 1000 members.

### Creating a Group

Depending on your access and permissions, you can create Internal Groups from the Developer Console in the  

* Click ‘Create Internal Group’ on the top, right to create a new group.
* Give your group a name.
* Choose a group type from those shown (defined below).


![Internal Group][7]

| Group Type     | Use Case     |
| :------------- | :------------- |
| User Event Group| Used for verifying events or logs from your test device.|
|Content Test Group| A similar concept to Test Lists. Can be used across push, email, and in-app messages to send a rendered copy of the message.|
|Seed Group | Automatically sends a copy of the Email to everyone the Seed Group upon send.|
{: .reset-td-br-1 .reset-td-br-2}

### Adding Test Users

After you create your Internal Group you can add test users as members. If you are not already on your Internal Group's management page, click into it. Then, click “Add Test User” and add them as identified or anonymous users, or in Bulk.

![User Logs 1][8]

| Add Test User Tab Name | Description |
| :------------- | :------------- |
| Identified Users |Search for the user by their External User ID or email address.|
|Anonymous Users| Search by IP address. Then, provide a name for each test user that is added. This is the name that all event logs will be associated with on the Event User Log page.|
|Bulk Add Users|Copy and paste a list of email addresses or external ID’s into the provided section. Braze will only allow you to add users that are already known in the database. Remember to upload your .csv files to add users to the database or programmatically create them via the API.|
{: .reset-td-br-1 .reset-td-br-2}

### Content Test Groups

Similar to sending a preview test of a message, the Content Test group saves you time and allows you to launch tests to a pre-defined list of Braze Users simultaneously. This functionality is available for Push, In-App Message, SMS, and Email within Braze.

{% alert note %}
[SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/) test messages can only be sent to valid phone numbers in the database.
{% endalert %}

You can select individual Braze Users or as many Internal Groups to send the message to as you want. The message will utilize the attributes available for each individual User. For Users who have no attributes, the default value set will be utilized.

Additionally, if you preview the message as a ‘random user’, ‘custom user’ or ‘select an existing user’ - the option to send that previewed version is presented. Unchecking the box will allow you to send based on each Users’ attributes versus the previewed version.

Lastly, for clients who use an IP pool to send out email, you can now select which IP pool you would like the email to be sent from by simply selecting the pool from the dropdown available.

Only Groups that are tagged as Content Test will be available on the ‘preview’ section of a message.

![Content test group settings][9]

### Seed Groups

Seed Groups are only meant for the Email channel and allow you to send a copy of each email variant message to members of that group. Seed Groups are not available for API campaigns, though you can include Seed Groups via an API-triggered entry in campaign. This feature is typically used with partners such as Return Path or 250OK to measure deliverability metrics. It can be used to keep a record of the email content for historical/archive purposes. 

Once you have created an Internal Group and tagged it to be used as a Seed Group, you can select it from the "Target Users" section of the campaign composer or on the Send Settings section in a Canvas. Seed emails will have an identifier `[SEED]`, appended to the start of the email subject line. Please note that Seed emails sent will not increment sends in dashboard analytics, and they will not update a user profile's "Campaign Received" list.

_If your Seed Group members report not seeing the message in their inbox, ensure that they are listed in the Internal Group, verify that your subject lines are different and that Gmail has not bundled the emails together, or have them check their SPAM folders._

#### For Campaigns

Seed Groups can be edited from the **Targeting** page when composing an email campaign.

Seed Groups send to each email variant once and are delivered the first time your user receives that particular variant. For scheduled messages this typically is the first time the campaign launches. For action-based or API-triggered campaigns, this will the time the first user is sent a message.

If your campaign is multivariate and your variant has a 0% send percentage, it will not be sent to seed groups. Additionally, if the variant has already been sent and has not been updated to resend in Edit Seed Groups on the Target page, it will not send again by default.

_If there is a recurring campaign and an update is conducted on any one of the variants, you have the option of re-sending to only the updated variants, all variants or to turn off seed group sending upon update._

![Seed_group_campaign][11]

#### For Canvas

Seed groups in Canvas work in a similar fashion to that of any triggered campaign. Braze automatically detects all steps that contain an email message and will send to these when your user first reaches that particular email step.

_If an Email step was updated after the Seed Group was mailed, the option to only send to updated steps/all steps/turn off seeds will be presented._


[7]: {% image_buster /assets/img_archive/internal_group.png %}
[8]: {% image_buster /assets/img_archive/UserLogs1.png %}
[9]: {% image_buster /assets/img_archive/content_test_preview.png %}
[11]: {% image_buster /assets/img_archive/seed_group_campaign.png %}
