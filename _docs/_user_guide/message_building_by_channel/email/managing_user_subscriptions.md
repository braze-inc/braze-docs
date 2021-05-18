---
nav_title: Managing User Subscriptions
page_order: 6
description: "This reference article covers how to manage users' email subscription states."
---
# Managing User Subscriptions

## Global Subscription States {#subscription-states}

Braze has three global subscription states for e-mail users (listed in the chart below), which are the final gatekeeper between your messages and your users. For example, users who are considered `unsubscribed` will not receive messages targeted at the Global Subscription State of `subscribed` or `opted-in`.

| State | Definition |
| ----- | ---------- |
| Opted-in | User has explicitly confirmed he/she wants to receive e-mail. We recommend an explicit opt-in process to acquire consent from users to send e-mail. |
| Subscribed | User has neither unsubscribed nor explicitly opted-in to receive e-mails. A user automatically gets set as Subscribed when a valid e-mail address is added to their user profile. |
| Unsubscribed | User has either explicitly unsubscribed from your e-mails. |
{: .reset-td-br-1 .reset-td-br-2}

{% alert important %}
Please note that these Global Subscription States are different from [Subscription Groups](#subscription-groups), which should be considered filters that can further narrow your audience from the Global Subscription States.
{% endalert %}

## Changing Subscriptions {#changing-subscriptions}

{% alert note %}
Braze does not count subscription state changes against your data points, globally, and around Subscription Groups.
{% endalert %}

### Subscription Groups

_Subscription Groups_ are segment filters that can further narrow your audience from the [Global Subscription States](#subscription-states) above. These Groups (maximum of 25 groups per app group) offer the ability to present more granular subscription options to end users.

For example, if you send out multiple categories of email campaigns, you can offer your customers the option to subscribe or unsubscribe from those groups in bulk from a single page, using our [Email Preference Center](#email-preference-center).

Use the [Subscription Group REST APIs][25] to programmatically manage the subscription groups that you have stored on the Braze dashboard to the Subscription Group page.

#### Create a Group

Create a Subscription Group by going to __Subscription Groups__ in the left navigation, then clicking the `+ Create Email Subscription Group` button. Then, name and describe your group.

![Create a Subscription Group][26]{: height="50%" width="50%"}

Use that name as a filter when creating your segments to ensure that only those users who have elected into that group receive that email or groups of email. This is great for monthly newsletters, coupons, membership tiers, and more!

![Use a Subscription Group][27]{: height="70%" width="70%"}

#### Archiving Groups

Archived Subscription Groups cannot be edited and will no longer appear in Segment Filters.  If you attempt to archive a group that is being used as a Segment Filter in any email, campaign, or canvas, you will receive an error message that will prevent you from archiving the Group until you remove all usages of it.

Archive your Group by going to __Subscription Groups__ in the left navigation; then, find your group in the list. Then, click the gear and select `Archive` from the dropdown menu.

We will not process any state changes for users in these groups. If you archive the Subscription Group A while Susie is considered `subscribed` to it, she will remain "`subscribed`" to this group, even though she has clicked an unsubscribe link (this shouldn't matter to Susie, Subscription Group A is archived and you can't send any messages using it.)

#### Export User Subscription State Changes

You can export your users' subscription state changes via CSV. From the Preference Center page in your account, click `User Subscription Data`, then `CSV Export User Subscription Data` from the dropdown.

![Export][29]

The past 30 days of state changes across all Subscription Groups are exported by default.

#### See Subscription Groups in Campaign Analytics

We also offer the ability to see the number of users who changed their Subscription State from a specific email campaign from that campaign's analytics page.

Scroll down to the `Email Message Performance` section and click the arrow under __Subscription Groups__ to see the aggregate count of state changes, as submitted by your customers.

![Sub Group Performance][30]

### Email Preference Center

The Email Preference Center is an easy way to manage which users receive certain groups of newsletters. Each Subscription Group you create is added to the Preference Center list. Click on the name of the Preference Center to see an interactive preview.

To place a link to the Preference Center in your emails, use the Preference Center Liquid tag and place it in the desired place in your email, similar to the way you insert [unsubscribe urls](#custom-footer).

{% raw %}
```
{{${preference_center_url}}}
```
{% endraw %}

{% alert important %}
Each Preference Center has a checkbox that will allow your users to unsubscribe from all emails.
{% endalert %}

Please note that the Preference Center is intended to be used strictly within the email channel itself. The preference center links are dynamic based on each user and cannot be hosted externally. You may, however, create and host your own custom preference center and use the [Subscription Group REST APIs][25] to keep data in-sync with Braze, see preference center customization below.

#### Customize Your Preference Center

You can create a fully custom HTML Preference Center, which you will host, then sync using our [APIs][28]. Reach out to your Braze representative for more information.

{% alert note %}
At this time, you can only have one Preference Center which will list all of your current Subscription Groups.
{% endalert %}

##### Logo

You can edit the logo and header of your Preference Center. Click the gear, then __Edit__ from the menu that appears.

### Changing Email Subscriptions {#changing-email-subscriptions}
In most cases, your users will manage their email subscription through subscription links that are included in the emails they receive.

You must insert a legally compliant footer with an unsubscribe link at the bottom of every email you send. When users click on the unsubscribe URL in your footer, they should be unsubscribed and taken to a landing page that confirms the change to their subscription. 

#### Custom Footers {#custom-footer}

{% raw %}

Braze provides the ability to set an app group-wide custom email footer which you can template into every email using the ``{{${email_footer}}}`` attribute. In this way, you do not have to create a new footer for every email template or email campaign you use. Changes you make to your custom footer will be reflected in all new and existing email campaigns. Remember that compliance with the [CAN-SPAM Act of 2003](https://www.ftc.gov/tips-advice/business-center/guidance/can-spam-act-compliance-guide-business) requires you to include a physical address for your company and an unsubscribe link in your emails. It is your responsibility to make sure that your custom footer meets those requirements.

To create or edit your custom footer, go to the **Manage Settings** page under **Settings**, and select the **Email Settings** tab.

![Email Settings][19]

In the Custom Footer section, you can choose to turn on Custom Footers. Once turned on, you will see a window to edit your footer and send a test message.

![Custom Footer][20]

You will see the default footer which uses the ``{{${set_user_to_unsubscribed_url}}}`` attribute and Braze's physical mailing address. To comply with CAN-SPAM regulations, your custom footer must include ``{{${set_user_to_unsubscribed_url}}}``; you will not be able to save a custom footer without ``{{${set_user_to_unsubscribed_url}}}``.

If using the default footer which uses the ``{{${set_user_to_unsubscribed_url}}}`` attribute, be sure to select "other" for the Protocol as indicated below.

![Default Unsub URL Protocol][24]

![No Footer-Email Settings][21]

> Be very careful to use a template with the custom footer ``{{${email_footer}}}`` or ``{{${set_user_to_unsubscribed_url}}}``when composing an email campaign. A warning will pop-up, however, the ultimate decision of whether to send an email without an unsubscribe link lies with you.

![No Footer-Campaign Composition][22]

When creating a custom footer, Braze suggests you use attributes for personalization. Here are a few you may find useful:

| Attribute | Tag |
| --------- | --- |
| User's Email Address | `{{${email_address}}}` |
| User's Custom Unsubscribe URL | `{{${set_user_to_unsubscribed_url}}}` |
| User's Custom Opt-In URL | `{{${set_user_to_opted_in_url}}}` |
| User's Custom Subscribe URL | `{{${set_user_to_subscribed_url}}}` |
{: .reset-td-br-1 .reset-td-br-2}

Of course, the full set of default and custom attributes are available to you. As a best practice, Braze recommends including both an unsubscribe link (i.e. ``{{${set_user_to_unsubscribed_url}}}``) and an opt-in link (i.e. ``{{${set_user_to_opted_in_url}}}``) in your custom footer. This way users will be able to both unsubscribe or opt-in and you can passively collect opt-in data for a portion of your users.

You can also choose to set a custom footer for plaintext emails, which follows the same rules as the custom footer for HTML emails. If you choose not to write a plaintext footer, Braze will automatically build one from the HTML footer. When your custom footers are to your liking, press Save at the bottom of the page.

![Save Custom Footer][23]

#### Custom Unsubscribe Landing Page
When a user clicks on an unsubscribe URL in an email, they are taken to a default landing page that confirms the change to their subscription.

Optionally, you may provide HTML for your own custom landing page, which users will be directed to (instead of the default page) upon unsubscribing. This feature is available on the ["Email Settings"][10] page.

We recommend including a resubscribe link (i.e. `{{${set_user_to_subscribed_url}}}` ) on this page so that users have the option to resubscribe in case they unsubscribed by accident.

![Custom Unsubscribe][11]

{% endraw %}

### Changing Push Subscriptions {#changing-push-subscriptions}
Braze's SDKs provide methods for changing a user's push message subscription. Please refer to Braze's technical documentation for your mobile platform for information on configuring these methods:

- [iOS][12]
- [Android and FireOS][13]
- [Windows Universal][14]

### Manually Changing User Subscriptions {#manually-changing-subscriptions}
You can manually change the subscription status for any user in his/her individual user profile. You can find individual user profiles by searching for a user's ID or email address on the "User Search" page. Under the user profile's "Engagement" tab, you'll find a user's current push and email subscription status. Clicking on the "Unsubscribed", "Subscribed", or "Opted In" buttons will allow you to change that user's subscription status. If available, the user profile also displays a timestamp for when the user's subscription was last changed.

![User Profile Subscription UI][16]

## Subscriptions and Campaign Targeting {#subscriptions-and-campaign-targeting}
Campaigns with push or email messages are targeted at users who are subscribed or opted-in by default. You can change this targeting preference when editing a campaign by going to the "Target Users" step and clicking "Advanced Options."

Braze supports three targeting states:

- Users who are subscribed or opted-in (default).
- Only users who are opted-in.
- All users, including those who have unsubscribed.

{% alert important %}
It is your responsibility to comply with any applicable [spam laws]({{site.baseurl}}/help/best_practices/spam_regulations/#spam-regulations) when using these targeting settings.
{% endalert %}

![Campaign Targeting Subscription UI][17]

## Segmenting by User Subscriptions {#segmenting-by-user-subscriptions}
The "Email Subscription Status" and "Push Subscription Status" filters allow you to segment your users by their subscription status.

This can be useful - for example, if you want to target users who have neither opted in nor out and encourage them to explicitly opt-in to email or push. In that case, you would create a segment with a filter for "Email/Push Subscription Status is Subscribed" and campaigns to this segment will go to users who are subscribed but not opted in.

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
