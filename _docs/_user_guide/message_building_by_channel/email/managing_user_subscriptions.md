---
nav_title: Email Subscriptions
article_title: User Subscriptions
page_order: 4
description: "This reference article covers the different user subscription states, how to create and manage subscription groups, and how to segment users based on their subscriptions."
channel:
  - email

---

# Email subscriptions

> Learn about the different user subscription states, how to create and manage subscription groups, and how to segment users based on their subscriptions.

## Subscription states {#subscription-states}

Braze has three global subscription states for email users (listed in the following table), which are the final gatekeeper between your messages and your users. For example, users who are considered `unsubscribed` will not receive messages targeted at the global subscription state of `subscribed` or `opted-in`.

| State | Definition |
| ----- | ---------- |
| Opted-in | User has explicitly confirmed they want to receive email. We recommend an explicit opt-in process to get consent from users to send emails. |
| Subscribed | User has neither unsubscribed nor explicitly opted-in to receive emails. This is the default subscription state when a user profile is created. |
| Unsubscribed | User has explicitly unsubscribed from your emails. |
{: .reset-td-br-1 .reset-td-br-2}

{% alert note %}
Braze does not count subscription state changes against your data points, globally, and around subscription groups.
{% endalert %}

### Updating email subscription states

There are three ways a user's email subscription state can be updated:

1. **SDK integration**<br>Use the Braze SDK to update a user's subscription state.<br><br>
2. **REST API**<br>Use the [`/users/track` endpoint][users-track] to update the [`email_subscribe`][user_attributes_object] attribute for a given user.<br><br>
3. **User Profile**<br>To manually change the subscription status, first find the user through **Search Users**. Next, under the **Engagement** tab, click the **Unsubscribed**, **Subscribed**, or **Opted In** buttons to change that user's subscription status. If available, the user profile also displays a timestamp for when the user's subscription was last changed.<br><br>
4. **Preference center**<br>[Preference center](#email-preference-center) Liquid can be included at the bottom of your emails, allowing users to opt-in or opt-out of emails. Braze manages the subscription state updates from the preference center.

### Checking email subscription state

![User profile for John Doe with their email subscription state set to Subscribed.][3]{: style="float:right;max-width:35%;margin-left:15px;"}

There are two ways you can check a user's email subscription state with Braze:

1. **User Profile**: You can access individual user profiles through the Braze dashboard on the **[Search Users][5]** page. After finding a user's profile (via email address, phone number, or external user ID), you can select the **Engagement** tab to view and manually adjust a user's subscription state.
<br><br>
2. **Rest API Export**: You can export individual user profiles in JSON format using the export [Users by segment][segment] or [Users by identifier][identifier] endpoints. 

<br><br>
## Subscription groups

Subscription groups are segment filters that can further narrow your audience from the [global subscription states](#subscription-states). You can add up to 100 subscription groups per workspace. These groups allow you to present more granular subscription options to end-users.

For example, suppose you send out multiple categories of email campaigns (promotional, newsletter, product updates). In that case, you can use subscription groups to let your customers pick and choose which email categories they want to subscribe or unsubscribe from in bulk from a single page, using our [email preference center](#email-preference-center). 

Alternatively, you could use subscription groups to let your customers choose how frequently they want to receive emails from you, by creating subscription groups for daily, weekly, or monthly emails.

Use the [Subscription Group REST APIs][25] to programmatically manage the subscription groups that you have stored on the Braze dashboard to the **Subscription Group** page.

### Create a group

To create a subscription group, go to **Audience** > **Subscriptions** and select **+ Create Email Subscription Group**. Give your subscription group a name and description, and click **Save**. All subscription groups are automatically added to your preference center.

{% alert note %}
If you are using the [older navigation]({{site.baseurl}}/navigation), this page is located at **Users** > **Subscription Groups**.
{% endalert %}

![Fields to create a subscription group.][26]{: height="50%" width="50%"}

When creating your segments, set the subscription group name as a filter. This will ensure users who have opted into your group will receive your emails. This is great for monthly newsletters, coupons, membership tiers, and more.

![GIF of a user setting a subscription group name as a filter.][27]{: style="max-width:80%"}

### Archiving groups

Archived subscription groups cannot be edited and will no longer appear in segment filters or in your preference center.  If you attempt to archive a group that is being used as a segment filter in any email, campaign, or Canvas, you will receive an error message that will prevent you from archiving the group until you remove all usages of it.

You can archive your group from the **Subscription Groups** page. Find your group in the list, then click the gear and select **Archive** from the dropdown menu.

Braze will not process any state changes for users in archived groups. For example, if you archive "Subscription Group A" while Susie is considered `subscribed` to it, they will remain "`subscribed`" to this group, even if they clicks an unsubscribe link (this shouldn't matter to Susie, "Subscription Group A" is archived and you can't send any messages using it).

#### See subscription groups in campaign analytics

You can see the number of users who changed their subscription state (subscribed or unsubscribed) from a specific email campaign on that campaign's analytics page.

From the **Campaign Analytics** page for your campaign, scroll down to the **Email Message Performance** section and click the arrow under **Subscription Groups** to see the aggregate count of state changes, as submitted by your customers.

![][30]

## Email preference center

The email preference center is an easy way to manage which users receive certain groups of newsletters and can be found in the dashboard under **Subscription Groups**. Each subscription group you create is added to the preference center list. To learn more about how to add or customize a preference center, refer to [Preference center]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center/preference_center/).

## Changing email subscriptions {#changing-email-subscriptions}

In most cases, your users will manage their email subscription through subscription links that are included in the emails they receive. You must insert a legally-compliant footer with an unsubscribe link at the bottom of every email you send. When users click on the unsubscribe URL in your footer, they should be unsubscribed and taken to a landing page that confirms the change to their subscription.

### Custom footers {#custom-footer}

{% raw %}
Braze provides the ability to set a workspace-wide custom email footer which you can template into every email using the ``{{${email_footer}}}`` Liquid attribute.
{% endraw %}

This way, you don't have to create a new footer for every email template or email campaign you use. Changes you make to your custom footer will be reflected in all new and existing email campaigns. Remember that compliance with the [CAN-SPAM Act of 2003](https://www.ftc.gov/tips-advice/business-center/guidance/can-spam-act-compliance-guide-business) requires you to include a physical address for your company and an unsubscribe link in your emails. 

{% alert warning %}
It is your responsibility to make sure that your custom footer meets those requirements.
{% endalert %}

To create or edit your custom footer, go to **Settings** > **Email Preferences**.

{% alert note %}
If you are using the [older navigation]({{site.baseurl}}/navigation), this page is called **Email Settings** and is located under **Manage Settings**.
{% endalert %}

![][19]

In the **Custom Footer** section, you can choose to turn on custom footers. Once turned on, you will see a window to edit your footer and send a test message.

![][20]

{% raw %}
You will see the default footer, which uses the ``{{${set_user_to_unsubscribed_url}}}`` attribute and Braze's physical mailing address. To comply with CAN-SPAM regulations, your custom footer must include ``{{${set_user_to_unsubscribed_url}}}``. You won't be able to save a custom footer without this attribute.

If using the default footer, which uses the ``{{${set_user_to_unsubscribed_url}}}`` attribute, be sure to select **&#60;other&#62;** for the **Protocol**.

![Protocol and URL values needed for the custom footer.][24]{: style="max-width:50%;"}

![Example email composed without a footer.][21]

> Be very careful to use a template with the custom footer ``{{${email_footer}}}`` or ``{{${set_user_to_unsubscribed_url}}}``when composing an email campaign. A warning will pop up, but it'll be your choice to either send an email with or without an unsubscribe link.

![No-footer campaign composition.][22]

When creating a custom footer, Braze suggests using attributes for personalization. The full set of default and custom attributes are available, but here are a few you may find useful:

| Attribute | Tag |
| --------- | --- |
| User's Email Address | `{{${email_address}}}` |
| User's Custom Unsubscribe URL | `{{${set_user_to_unsubscribed_url}}}` |
| User's Custom Opt-In URL | `{{${set_user_to_opted_in_url}}}` |
| User's Custom Subscribe URL | `{{${set_user_to_subscribed_url}}}` |
| User's Custom Braze Preference Centre URL | `{{${preference_center_url}}}` |
{: .reset-td-br-1 .reset-td-br-2}



As a best practice, Braze recommends including both an unsubscribe link (i.e., ``{{${set_user_to_unsubscribed_url}}}``) and an opt-in link (i.e., ``{{${set_user_to_opted_in_url}}}``) in your custom footer. This way, users will be able to both unsubscribe or opt-in, and you can passively collect opt-in data for a portion of your users.

You can also choose to set a custom footer for plaintext emails from the **Email Settings** tab, which follows the same rules as the custom footer for HTML emails. If you don't include a plaintext footer, Braze will automatically build one from the HTML footer. When your custom footers are to your liking, click **Save** at the bottom of the page.

![Email with Set Custom Plaintext Footer option selected.][23]{: style="max-width:70%" }

### Custom unsubscribe page

When a user clicks on an unsubscribe URL in an email, they are taken to a default landing page that confirms the change to their subscription.

Optionally, you may provide HTML for your custom landing page that users will be directed to (instead of the default page) upon unsubscribing in the **Subscription Pages and Footers** tab of the **Email Settings** page. We recommend including a resubscribe link (i.e., `{{${set_user_to_subscribed_url}}}` ) on this page so that users have the option to resubscribe in case they unsubscribed by accident.

![Custom unsubscribe email in the Custom Unsubscribe Page panel.][11]

{% endraw %}

### Custom opt-in page

Instead of immediately subscribing a user to your email campaigns, creating a custom opt-in page can give your users the opportunity to acknowledge and control their notification preferences. This additional communication can also help your email campaigns stay out of the spam folder since your users will have chosen to be opted-in. Go to **Manage Settings > Email Settings > Subscription Pages and Footers**, and customize the styling in the **Custom Opt-In Page** section to see how that indicates to your users that they've been subscribed.

{% alert tip %}
Braze recommends using a double opt-in process to help your email outreach. This process involves sending an additional confirmation email where a user would confirm their notification preferences again via a link in the email. At this point, the user would be considered opted-in.
{% endalert %}

## Subscriptions and campaign targeting {#subscriptions-and-campaign-targeting}

Campaigns with push or email messages are targeted at users who are subscribed or opted-in by default. You can change this targeting preference when editing a campaign by going to the **Target Users** step and clicking **Advanced Options**.

Braze supports three targeting states:

- Users who are subscribed or opted-in (default).
- Only users who are opted-in.
- All users, including those who have unsubscribed.

{% alert important %}
It is your responsibility to comply with any applicable [spam laws]({{site.baseurl}}/help/best_practices/spam_regulations/#spam-regulations) when using these targeting settings.
{% endalert %}

![Audience targeting example for users who are subscribed or opted in the Advanced Options of the Target Users step.][17]

## Segmenting by user subscriptions {#segmenting-by-user-subscriptions}

The `Email Subscription Status` and `Push Subscription Status` filters allow you to segment your users by their subscription status.

For example, this can be useful if you want to target users who have neither opted in nor out and encourage them to explicitly opt-in to email or push. In that case, you would create a segment with a filter for "Email/Push Subscription Status is Subscribed" and campaigns to this segment will go to users who are subscribed, but not opted in.

![Email Subscription Status used as a segment filter.][18]

[11]: {% image_buster /assets/img/custom_unsubscribe.png %}
[12]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_custom_attributes/#setting-up-user-subscriptions
[13]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_custom_attributes/#setting-up-user-subscriptions
[16]: {% image_buster /assets/img_archive/user-profile-subscription-ui.png %}
[17]: {% image_buster /assets/img_archive/campaign-targeting-subscription-ui.png %}
[18]: {% image_buster /assets/img_archive/not_optin.png %}
[19]: {% image_buster /assets/img_archive/email_settings.png %}
[20]: {% image_buster /assets/img_archive/custom_footer.png %}
[21]: {% image_buster /assets/img_archive/no_unsub_link_warning.png %}
[22]: {% image_buster /assets/img_archive/no_footer_test.png %}
[23]: {% image_buster /assets/img_archive/custom_footer_save_changes.png %}
[24]: {% image_buster /assets/img_archive/email_unsub_protocol.png %}
[25]: {{site.baseurl}}/developer_guide/rest_api/subscription_group_api/
[26]: {% image_buster /assets/img/sub_group_create.png %}
[27]: {% image_buster /assets/img/sub_group_use.gif %}
[28]: {{site.baseurl}}/api/endpoints/preference_center/
[29]: {% image_buster /assets/img/user-sub-state-export.png %}
[30]: {% image_buster /assets/img/campaign_analytics_sub_groups.png %}
[users-track]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/
[user_attributes_object]: {{site.baseurl}}/api/objects_filters/user_attributes_object
[3]: {% image_buster /assets/img/push_example.png %}
[5]: {{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search/
[identifier]: {{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/
[segment]: {{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/
