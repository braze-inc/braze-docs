---
nav_title: Internal Groups Tab
article_title: Internal Group Tab
page_order: 3
page_type: reference
description: "This reference article covers Internal Groups, a great way to get insight into your test device's SDK or API logs when testing SDK integration."
---

# Internal Groups tab

Internal Groups are a great way to build and organize internal or third-party test groups and provide insight into the SDK or API logs available from your test device during SDK integration testing. You can create an unlimited number of custom Internal Groups with up to 1,000 members.

{% alert note %}
You need the **Access Dev Console** [permissions]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#limited-and-team-role-permissions) for your app group to create and manage Internal Groups.
{% endalert %}

## Creating a group

To create an Internal Group, perform the following steps:

1. Go to the **Developer Console** and select the **Internal Groups** tab.
2. Click **Create Internal Group**.
3. Give your group a meaningful name.
4. Choose one or more group types (defined below).


!\[Internal Group\]\[7\]

| Group Type         | Use Case                                                                                                                     |
|:------------------ |:---------------------------------------------------------------------------------------------------------------------------- |
| User Event Group   | Used for verifying events or logs from your test device.                                                                     |
| Content Test Group | A similar concept to Test Lists. Can be used across push, email, and in-app messages to send a rendered copy of the message. |
| Seed Group         | Automatically sends a copy of the email to everyone the Seed Group upon send.                                                |
{: .reset-td-br-1 .reset-td-br-2}

### Adding test users

After you create your Internal Group, you can add test users as members of that group. From your Internal Group's management page, click **Add Test User** and either add them in bulk, as identified users, or as anonymous users.

!\[User Logs 1\]\[8\]

| Addition Method  | Description                                                                                                                                                                                                                                                                         |
|:---------------- |:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Identified Users | Search for the user by their external user ID or email address.                                                                                                                                                                                                                     |
| Anonymous Users  | Search by IP address. Then, provide a name for each test user that is added. This is the name that all event logs will be associated with on the [Event User Log]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/) page.              |
| Bulk Add Users   | Copy and paste a list of email addresses or external IDs into the provided section. You can only add users that are already known in the dashboard. For more information, refer to [User Import]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/). |
{: .reset-td-br-1 .reset-td-br-2}

### Content test groups

Similar to sending a preview test of a message, the Content Test group saves you time and allows you to launch tests to a pre-defined list of Braze users simultaneously. This functionality is available for push, in-app message, SMS, email, and Content Cards within Braze.

{% alert note %}
[SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/) test messages can only be sent to valid phone numbers in the database.
{% endalert %}

You can select individual Braze users or as many Internal Groups to send the message to as you want. If your message includes any Liquid or other dynamic personalization, Braze will use the attributes available for each individual user to personalize the message contents. For users who have no attributes, Braze will use the default value set.

Additionally, if you preview the message as a random user, custom user, or existing user, you can send that previewed version instead. Clearing the checkbox allows you to send based on each users’ attributes versus the previewed version.

Lastly, if you use an IP pool to send out email, you can select which IP pool you would like the email to be sent from by selecting the pool from the dropdown available.

Only groups that are tagged as Content Test Groups will be available on the preview section of a message.

!\[Content test group settings\]\[9\]{: style="max-width:50%" }

### Seed groups

Seed Groups are only meant for the email channel and allow you to send a copy of each email variant message to members of that group. Seed Groups are not available for API campaigns, although you can include Seed Groups via an API-triggered entry in campaign. This feature is typically used with partners such as Return Path or 250OK to measure deliverability metrics. It can be used to keep a record of the email content for historical and archival purposes.

Once you have created an Internal Group and tagged it to be used as a Seed Group, you can select it from the **Target Users** step of the campaign composer, or on the **Send Settings** step in a Canvas. Seed emails will have the identifier `[SEED]`, appended to the start of the email subject line. Please note that Seed emails sent don't increment sends in dashboard analytics, and they don't update a user profile's **Campaign Received** list.

{% alert tip %}
If your Seed Group members report not seeing the message in their inbox, ensure that they are listed in the Internal Group, verify that your subject lines are different and that Gmail has not bundled the emails together, or have them check their SPAM folders.
{% endalert %}

#### For campaigns

Seed Groups can be edited from the **Targeting** page when composing an email campaign.

Seed Groups send to each email variant once and are delivered the first time your user receives that particular variant. For scheduled messages this typically is the first time the campaign launches. For action-based or API-triggered campaigns, this will be the time the first user is sent a message.

If your campaign is multivariate and your variant has a 0% send percentage, it will not be sent to seed groups. Additionally, if the variant has already been sent and has not been updated to resend in **Edit Seed Groups** on the **Target** step, it will not send again by default.

{% alert note %}
If there is a recurring campaign and an update is conducted on any one of the variants, you have the option of re-sending to only the updated variants, all variants, or to turn off seed group sending upon update.
{% endalert %}

!\[Seed group campaign\]\[11\]

#### For Canvas

Seed groups in Canvas work in a similar fashion to that of any triggered campaign. Braze automatically detects all steps that contain an email message and will send to these when your user first reaches that particular email step.

If an email step was updated after the Seed Group was mailed, the option to only send to updated steps, all steps, or turn off seeds will be presented.
[7]: {% image_buster /assets/img_archive/internal_group.png %} [8]: {% image_buster /assets/img_archive/UserLogs1.png %} [9]: {% image_buster /assets/img_archive/content_test_preview.png %} [11]: {% image_buster /assets/img_archive/seed_group_campaign.png %}
