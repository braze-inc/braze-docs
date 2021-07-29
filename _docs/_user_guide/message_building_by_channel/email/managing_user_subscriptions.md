---
nav_title: Managing User Subscriptions
page_order: 6
description: "This reference article covers the different user subscription states, how to create and manage subscription groups, and how to segment users based on their subscriptions."

tool:
  - Dashboard

channel:
  - email

---
# Managing User Subscriptions

## Global Subscription States {#subscription-states}

Braze has three global subscription states for email users (listed in the chart below), which are the final gatekeeper between your messages and your users. For example, users who are considered `unsubscribed` will not receive messages targeted at the Global Subscription State of `subscribed` or `opted-in`.

| State | Definition |
| ----- | ---------- |
| Opted-in | User has explicitly confirmed they want to receive email. We recommend an explicit opt-in process to get consent from users to send emails. |
| Subscribed | User has neither unsubscribed nor explicitly opted-in to receive emails. A user automatically gets set as `subscribed` when a valid email address is added to their user profile. |
| Unsubscribed | User has explicitly unsubscribed from your emails. |
{: .reset-td-br-1 .reset-td-br-2}

{% alert important %}
These Global Subscription States are different from [subscription groups](#subscription-groups), which act as filters that can further narrow your audience from the Global Subscription States.
{% endalert %}

## Changing Subscriptions {#changing-subscriptions}

{% alert note %}
Braze does not count subscription state changes against your data points, globally, and around subscription groups.
{% endalert %}

### Subscription Groups

Subscription groups are segment filters that can further narrow your audience from the [Global Subscription States](#subscription-states) above. You can add up to 25 subscription groups per app group. These groups allow you to present more granular subscription options to end-users.

For example, suppose you send out multiple categories of email campaigns (Promotional, Newsletter, Product Updates). In that case, you can use subscription groups to let your customers pick and choose which email categories they want to subscribe or unsubscribe from in bulk from a single page, using our [Email Preference Center](#email-preference-center). 

Alternatively, you could use subscription groups to let your customers choose how frequently they want to receive emails from you, by creating subscription groups for daily, weekly, or monthly emails.

Use the [Subscription Group REST APIs][25] to programmatically manage the subscription groups that you have stored on the Braze dashboard to the **Subscription Group** page.

#### Create a Group

To create a subscription group, go to the __Subscription Groups__ page, then click **+ Create Email Subscription Group**. Give your subscription group a name and description, and click **Save**. All subscription groups are automatically added to your Preference Center.

![Create a Subscription Group][26]{: height="50%" width="50%"}

When creating your segments, set the subscription group name as a filter. This will ensure users who have opted into your group will receive your emails. This is great for monthly newsletters, coupons, membership tiers, and more!

![Use a Subscription Group][27]{: height="70%" width="70%"}

#### Archiving Groups

Archived subscription groups cannot be edited and will no longer appear in segment filters or in your Preference Center.  If you attempt to archive a group that is being used as a segment filter in any email, campaign, or Canvas, you will receive an error message that will prevent you from archiving the group until you remove all usages of it.

You can archive your group from the __Subscription Groups__ page. Find your group in the list, then click the gear and select **Archive** from the dropdown menu.

Braze will not process any state changes for users in archived groups. For example, if you archive "Subscription Group A" while Susie is considered `subscribed` to it, they will remain "`subscribed`" to this group, even if they clicks an unsubscribe link (this shouldn't matter to Susie, "Subscription Group A" is archived and you can't send any messages using it).

#### Export User Subscription State Changes

You can export your users' subscription state changes via CSV file. From the **Preference Center** page, click **User Subscription Data**, then select **CSV Export User Subscription Data** from the dropdown.

![Export][29]

By default, the past 30 days of state changes across all subscription groups are exported.

#### See Subscription Groups in Campaign Analytics

You can see the number of users who changed their Subscription State (subscribed or unsubscribed) from a specific email campaign on that campaign's analytics page.

From the **Campaign Analytics** page for your campaign, scroll down to the **Email Message Performance** section and click the arrow under __Subscription Groups__ to see the aggregate count of state changes, as submitted by your customers.

![Sub Group Performance][30]

### Email Preference Center

The Email Preference Center is an easy way to manage which users receive certain groups of newsletters. Each subscription group you create is added to the Preference Center list. Click on the name of the Preference Center to see an interactive preview.

To place a link to the Preference Center in your emails, use the Preference Center Liquid tag (below) and add it to the desired place in your email, similar to the way you insert [unsubscribe urls](#custom-footer).

{% raw %}
```
{{${preference_center_url}}}
```
{% endraw %}

{% alert note %}
The Preference Center has a checkbox that will allow your users to unsubscribe from all emails.
{% endalert %}

The Preference Center is intended to be used strictly within the email channel itself. The Preference Center links are dynamic, based on each user, and cannot be hosted externally. You may, however, create and host your own custom Preference Center and use the [Subscription Group REST APIs][25] to keep data in sync with Braze. Refer to the next section for more.

#### Customize Your Preference Center

You can create a fully custom HTML Preference Center, which you will host, then sync to Braze using our [APIs][28]. Reach out to your Braze representative for more information.

{% alert note %}
At this time, you can only have one Preference Center, which will list all of your current subscription groups.
{% endalert %}

##### Logo

You can edit the logo and header of your Preference Center. Click the gear, then click __Edit__ from the menu that appears.

### Changing Email Subscriptions {#changing-email-subscriptions}

In most cases, your users will manage their email subscription through subscription links that are included in the emails they receive.

You must insert a legally-compliant footer with an unsubscribe link at the bottom of every email you send. When users click on the unsubscribe URL in your footer, they should be unsubscribed and taken to a landing page that confirms the change to their subscription.

#### Custom Footers {#custom-footer}

{% raw %}
Braze provides the ability to set an app group-wide custom email footer which you can template into every email using the ``{{${email_footer}}}`` Liquid attribute.
{% endraw %}

This way, you don't have to create a new footer for every email template or email campaign you use. Changes you make to your custom footer will be reflected in all new and existing email campaigns. Remember that compliance with the [CAN-SPAM Act of 2003](https://www.ftc.gov/tips-advice/business-center/guidance/can-spam-act-compliance-guide-business) requires you to include a physical address for your company and an unsubscribe link in your emails. 

{% alert warning %}
It is your responsibility to make sure that your custom footer meets those requirements.
{% endalert %}

To create or edit your custom footer, go to the **Manage Settings** page, and select the **Email Settings** tab.

![Email Settings][19]

In the **Custom Footer** section, you can choose to turn on Custom Footers. Once turned on, you will see a window to edit your footer and send a test message.

![Custom Footer][20]

{% raw %}
You will see the default footer, which uses the ``{{${set_user_to_unsubscribed_url}}}`` attribute and Braze's physical mailing address. To comply with CAN-SPAM regulations, your custom footer must include ``{{${set_user_to_unsubscribed_url}}}``. You won't be able to save a custom footer without this attribute.

If using the default footer, which uses the ``{{${set_user_to_unsubscribed_url}}}`` attribute, be sure to select **&#60;other&#62;** for the **Protocol**, as indicated below.

![Default Unsub URL Protocol][24]

![No Footer-Email Settings][21]

> Be very careful to use a template with the custom footer ``{{${email_footer}}}`` or ``{{${set_user_to_unsubscribed_url}}}``when composing an email campaign. A warning will pop up; however, the ultimate decision of whether to send an email without an unsubscribe link lies with you.

![No Footer-Campaign Composition][22]

When creating a custom footer, Braze suggests you use attributes for personalization. Here are a few you may find useful:

| Attribute | Tag |
| --------- | --- |
| User's Email Address | `{{${email_address}}}` |
| User's Custom Unsubscribe URL | `{{${set_user_to_unsubscribed_url}}}` |
| User's Custom Opt-In URL | `{{${set_user_to_opted_in_url}}}` |
| User's Custom Subscribe URL | `{{${set_user_to_subscribed_url}}}` |
{: .reset-td-br-1 .reset-td-br-2}

Of course, the full set of default and custom attributes are available to you. As a best practice, Braze recommends including both an unsubscribe link (i.e. ``{{${set_user_to_unsubscribed_url}}}``) and an opt-in link (i.e. ``{{${set_user_to_opted_in_url}}}``) in your custom footer. This way, users will be able to both unsubscribe or opt-in, and you can passively collect opt-in data for a portion of your users.

You can also choose to set a custom footer for plaintext emails, which follows the same rules as the custom footer for HTML emails. If you choose not to write a plaintext footer, Braze will automatically build one from the HTML footer. When your custom footers are to your liking, click **Save** at the bottom of the page.

![Save Custom Footer][23]

#### Custom Unsubscribe Landing Page

When a user clicks on an unsubscribe URL in an email, they are taken to a default landing page that confirms the change to their subscription.

Optionally, you may provide HTML for your custom landing page that users will be directed to (instead of the default page) upon unsubscribing. This feature is available on the [Email Settings][10] page.

We recommend including a resubscribe link (i.e. `{{${set_user_to_subscribed_url}}}` ) on this page so that users have the option to resubscribe in case they unsubscribed by accident.

![Custom Unsubscribe][11]

{% endraw %}

### Changing Push Subscriptions {#changing-push-subscriptions}

Braze's SDKs provide methods for changing a user's push message subscription. Please refer to Braze's technical documentation for your mobile platform for information on configuring these methods:

- [iOS][12]
- [Android and FireOS][13]
- [Windows Universal][14]

### Manually Changing User Subscriptions {#manually-changing-subscriptions}

You can manually change the subscription status for any user in their user profile. You can find individual user profiles by searching for a user's ID or email address on the **User Search** page. Under the user profile's **Engagement** tab, you'll find a user's current push and email subscription status. 

Click the **Unsubscribed**, **Subscribed**, or **Opted In** buttons to change that user's subscription status. If available, the user profile also displays a timestamp for when the user's subscription was last changed.

![User Profile Subscription UI][16]{: style="max-width:60%" }

## Subscriptions and Campaign Targeting {#subscriptions-and-campaign-targeting}

Campaigns with push or email messages are targeted at users who are subscribed or opted-in by default. You can change this targeting preference when editing a campaign by going to the **Target Users** step and clicking **Advanced Options**.

Braze supports three targeting states:

- Users who are subscribed or opted-in (default).
- Only users who are opted-in.
- All users, including those who have unsubscribed.

{% alert important %}
It is your responsibility to comply with any applicable [spam laws]({{site.baseurl}}/help/best_practices/spam_regulations/#spam-regulations) when using these targeting settings.
{% endalert %}

![Campaign Targeting Subscription UI][17]

## Segmenting by User Subscriptions {#segmenting-by-user-subscriptions}

The `Email Subscription Status` and `Push Subscription Status` filters allow you to segment your users by their subscription status.

For example, this can be useful if you want to target users who have neither opted in nor out and encourage them to explicitly opt-in to email or push. In that case, you would create a segment with a filter for "Email/Push Subscription Status is Subscribed" and campaigns to this segment will go to users who are subscribed, but not opted in.

![Subscription Filter][18]

[10]: https://dashboard-01.braze.com/app_settings/app_settings/email/ "Email App Settings"
[11]: {% image_buster /assets/img/custom_unsubscribe.png %}
[12]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/setting_custom_attributes/#setting-up-user-subscriptions
[13]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_custom_attributes/#setting-up-user-subscriptions
[14]: {{site.baseurl}}/developer_guide/platform_integration_guides/windows_universal/analytics/setting_custom_attributes/#managing-notification-subscription-statuses
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
[28]: {{site.baseurl}}/developer_guide/rest_api/subscription_group_api/
[29]: {% image_buster /assets/img/user-sub-state-export.png %}
[30]: {% image_buster /assets/img/campaign_analytics_sub_groups.png %}
