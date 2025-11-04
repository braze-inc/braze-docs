---
nav_title: Internal groups
article_title: Internal Group
page_order: 10
page_type: reference
description: "This reference article covers internal groups, a great way to get insight into your test device's SDK or API logs when testing SDK integration."

---

# Internal Groups

> Internal groups are a great way to build and organize internal or third-party test groups. They provide insight into your SDK or API logs and are useful when testing your SDK integration. You can create an unlimited number of custom internal groups with up to 1,000 users.

{% alert tip %}
We also recommend checking out our [Testing and Troubleshooting](https://learning.braze.com/path/developer/testing-and-troubleshooting) Braze Learning course, which covers how to use internal groups to conduct your own troubleshooting and debugging.
{% endalert %}

## Prerequisites

Before you can create and manage internal groups, you need the [Access Dev Console permission]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#limited-and-team-role-permissions) for your workspace.

## Creating an internal group

To create an internal group, do the following: 

1. Go to **Settings** > **Internal Groups**.
2. Select **Create internal group**.
3. Give your group a name, such as "Email test group".
4. Choose one or more group types, as listed in the following table.

| Group type         | Description                                                                                 |
|--------------------|---------------------------------------------------------------------------------------------|
| **User Event Group**   | Used for verifying events or logs from your test device.                                    |
| **Content Test Group** | Can be used across push, email, and in-app messages to send a rendered copy of the message. |
| **Seed Group**         | Automatically sends a copy of the email to everyone in the Seed Group upon send.               |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![An internal group named "Email test group".]({% image_buster /assets/img_archive/internal_group.png %})

### Adding test users

After you create your internal group, you can add test users as members of that group. 

1. From your internal group's management page, select **Add test users**.
2. Choose from the following methods for searching and selecting your test users.

| Method                  | Description                                                                                                                                                                                                                                          |
|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Add identified user** | Search for the user by their external user ID, email address, phone number, or push token.                                                                                                                                                           |
| **Add anonymous user**  | Search by IP address. Then, provide a name for each test user that is added. This is the name that all event logs will be associated with on the [Event User Log]({{site.baseurl}}/user_guide/administrative/app_settings/event_user_log_tab/) page. |
| **Bulk add users**      | Copy and paste a list of email addresses or external IDs. You can only add users who are already known in the dashboard. For more information, refer to [User import]({{site.baseurl}}/user_guide/data/user_data_collection/user_import/).          |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![Internal Group Settings when creating a new internal group]({% image_buster /assets/img_archive/internal_group_add_user.png %})

### Content Test Groups

Similar to sending a preview test of a message, the Content Test Group saves you time and allows you to launch tests to a pre-defined list of Braze users simultaneously. This is available for push, in-app messages, SMS, email, and Content Cards in Braze. Only groups tagged as Content Test Groups will be available in the preview section of a message.

{% alert note %}
[SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/) test messages can only be sent to valid phone numbers in the database.
{% endalert %}

You can select individual Braze users or as many internal groups to send the message to. If your message includes any Liquid or other dynamic personalization, Braze will use the attributes available for each user to personalize the message contents. For users who have no attributes, Braze will use the default value set.

Additionally, if you preview the message as a random user, a custom user, or an existing user, you can send that previewed version instead. Clearing the checkbox allows you to send based on each user's attributes versus the previewed version.

If you use an IP pool to send out an email, you can select which IP pool you would like the email to be sent from by selecting the pool from the dropdown available.

![The Test section of the in-app message editor to select the Content Test Group.]({% image_buster /assets/img_archive/content_test_preview.png %}){: style="max-width:60%" }

### Seed Groups

Seed Groups are only supported for the email channel. You can add users to a Seed Group to send copies of each email variant message to all members of the group.

Seed Groups aren't available for API campaigns, but you can include Seed Groups using an API-triggered entry in the campaign. You can use this to measure deliverability metrics and to keep a record of your email content for historical and archival purposes. 

After creating an internal group and tagging it to be used as a Seed Group, you can select it from the **Target Audiences** step of the campaign editor, or on the **Send Settings** step in a Canvas. 

Seed emails will have `[SEED]` appended to the start of the email subject line. Note that seed emails **do not**:

- Increment sends in the dashboard analytics.
- Impact email analytics or retargeting. 
- Update a user profile's **Campaign Received** list.
- Impact frequency capping.
- Account for or impact the delivery speed rate limits.

{% alert tip %}
If your Seed Group members report not seeing the message in their inbox, check that they're listed in the internal group, verify that your subject lines are different and that Gmail has not bundled the emails together, or have them check their spam folders.
{% endalert %}

#### For campaigns

When composing an email campaign, you can edit your Seed Groups in the **Target Audiences** section of the editor.

Seed Groups send to each email variant once and are delivered the first time your user receives that particular variant. For scheduled messages, this typically is the first time the campaign launches. For action-based or API-triggered campaigns, this will be the time the first user is sent a message.

If your campaign is multivariate and your variant has a 0% send percentage, it won't be sent to Seed Groups. Additionally, if the variant has already been sent and hasn't been updated to resend in **Edit Seed Groups** on the **Target** step, it won't be sent again by default.

{% alert note %}
If you have a recurring campaign and any one of the variants is updated, you can choose to send again to only the updated variants or all variants, or turn off Seed Group sending upon update.
{% endalert %}

![The "Email seed test" Seed Group selected to be sent the Variant 1 email campaign.]({% image_buster /assets/img_archive/seed_group_campaign.png %})

#### For Canvas

Seed groups in Canvas work similarly to any triggered campaign. Braze automatically detects all steps that contain an email message and will send to these when your user first reaches that particular email step.

If an email step was updated after the Seed Group was mailed, the option to only send to updated steps, all steps, or turn off seeds will be presented.

