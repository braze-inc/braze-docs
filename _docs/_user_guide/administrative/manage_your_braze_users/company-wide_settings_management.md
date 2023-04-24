---
nav_title: Company Settings
article_title: Company Settings
page_order: 5
page_type: reference
description: "This reference article covers company-wide settings, like changing the name of your company, setting your time zone, notification preferences, security settings, and more."

---

# Company Settings

## Managing your company settings

The **Company Settings** page allows you to change the name of your company, set your time zone, and request to delete your company.

{% alert note %}
Only admins and users with explicit permissions to manage company settings will see this page.
{% endalert %}

### Consequences of switching your time zone

If you choose to switch your time zone, you may experience a variety of consequences, including:

- While campaigns scheduled for specific times in specific locations (i.e., 9 pm Eastern Time) will run properly on schedule until edited, both campaign analytics and future campaign schedules will be affected by the change.
- Any card scheduling that is not assigned to local time may be affected, with active cards potentially appearing as finished (or vice versa).
- Segmentation filters of the form "Has done X before/after `Date`" will have the time adjusted because the initial date will now be localized in Pacific Time.

### Notification preferences

The **Notification Preferences** page is where you can configure who (if anyone) receives notifications about your company. You can configure who should receive notifications about campaign and News Feed Card delivery or technical errors. You can also specify recipients for the weekly analytics report. For most notifications, Braze supports email and webhook channels.

![Notification Preferences page in the Braze dashboard][61]

The following table lists available notifications:

| Notification | Description | Available notification channels |
|--------------|-------------|-----------------|
| AWS Credential Errors | Notifies recipients when Braze receives an error while attempting to use your Amazon Web Services credentials for a data export. | Email, Webhook |
| Campaign Automatically Stopped | Notifies recipients when Braze has stopped a campaign. | Email |
| Campaign Interaction Expiration | Notifies recipients about any campaign that is due for campaign interaction data expiration, along with any information about segments, campaigns, or Canvases that reference it in a retargeting filter and were used to send a message in the previous 30 days. | Email |
| Campaign/Canvas Updated | Notifies recipients when an active campaign/canvas is updated or deactivated, as well as when an inactive campaign/canvas is reactivated or when drafts are launched. | Email |
| Canvas Interaction Expiration | Notifies recipients about any Canvas that is due for Canvas interaction data expiration, along with any information about segments, campaigns, or Canvases that reference it in a retargeting filter and were used to send a message in the previous 30 days. | Email |
| News Feed Card Published/Live | Notifies recipients when Newsfeed cards are scheduled or published. | Email, Webhook |
| Push Credential Errors | Notifies recipients when an app's push credentials are invalid and when an app's push credentials are expiring soon. | Email, Webhook |
| Scheduled Campaign Sent/Not Sent | Notifies recipients when scheduled campaigns begin sending or when scheduled campaigns attempted to send but had no eligible users to send to. | Email, Webhook |
| Scheduled Campaign Limit Met | Notifies recipients when the limit for a recurring scheduled campaign has been reached. | Email, Webhook |
| Scheduled Campaign Finished Sending | Notifies recipients when a scheduled campaign has finished sending. | Email, Webhook |
| Weekly Analytics Report | Sends a summary of the past week's app group activity to recipients every Monday. Recipients receive a summary for each app group that they belong to. | Email |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### Slack incoming webhook integration

Slack has an [incoming webhook app][67] that allows messages to be posted from external sources into Slack. To get started, open the incoming webhook app. 

1. Select the Slack channel that you'd like the notifications to go to and click **Add Incoming Webhooks Integration**.<br><br>
    ![Add incoming webhooks integration in Slack][63]<br><br>
  Slack will generate a URL that you'll need to enter into Braze for the notifications that you wish to receive.<br><br>
2. Copy the **Webhook URL**.<br><br>
    ![Copy webhook URL][64]<br><br>
3. Navigate to the **Notification Preferences** tab in **Company Settings**.<br><br>
4. Select the notification that you wish to enable for Slack. Or, if you have multiple notifications that you want to send to this Slack channel, use **Bulk Add** to add the webhook to multiple notifications.<br><br>
    ![Select Slack notifications to enable][65]{: style="max-width:60%;"}<br><br>
5. Enter the URL that Slack generated for you.

That's it! You should start receiving notifications about your company to this Slack channel. You can also check out Slack's help article on this topic: [Sending messages using Incoming Webhooks][62].

### Weekly analytics reporting

Braze optionally sends a weekly report via email to individuals you designate within your company every Monday at 5 am EST. The custom events to be included in the weekly report are selected on the **Custom Events** tab within the **Manage Settings** page of the dashboard. You may select up to five events to be included in your weekly report:

![Selecting events to be included in the Analytics Report][22]

### Additional email settings

You also can access the **Email Settings** tab to edit:

- The name which will be displayed by default on your emails
- The default reply-to address for your emails
- Your custom unsubscribe page
  - If you do not provide a custom unsubscribe page Braze will handle unsubscribes automatically

![Outbound Email Settings section of the Email Settings tab][7]

## List-unsubscribe settings

![Unsubscribe from this mailing list link in an email header][57]{: style="float:right;max-width:60%;margin-left:15px;"}

Although most marketers add a one-click unsubscribe link to their email, it is best practice to provide a special email header ("List-Unsubscribe") that allows email service providers such as Gmail and Windows Live Hotmail to provide their own Unsubscribe functionality:

For more information about list-unsubscribe, refer to [Email Settings][2]

## Security settings

The security settings page is where you can configure authentication rules, dashboard IP whitelisting, and two-factor authentication. These settings are located in the **Security Settings** tab of the **Company Settings** page.

![Security Settings tab of the Company Settings page][50]

### Authentication rules

Company administrators can configure authentication requirements for signing into Braze including setting password requirements (minimum password length, password complexity, password expiration), and enforcing Google authentication.  If the company administrator decides to set password authentication rules to become more strict, as soon as these rules are set, account users will be informed by email to change their passwords accordingly.

![Authentication Rules section of the Security Settings tab][51]

### Dashboard IP whitelisting

Your team can add a whitelist of specific IP addresses, ranges and subnets from which users can log in to your company's Braze account.

To mark specific IP addresses and subnets as whitelisted, fill in the IP addresses and subnets to whitelist and press Save Changes at the bottom of the page. IP ranges and subnets should be specified in CIDR (Classless Inter-Domain Routing) notation. For example, whitelisting `63.45.134.*` would be expressed in CIDR notation as `63.45.134.0/24`

For more information on CIDR notation see [RFC 4632][84].

![Dashboard IP Whitelisting section of the Security Settings tab][52]

### Two-factor authentication

Two-factor authentication adds an extra layer of identity verification upon login. By enabling two-factor authentication, Braze will require two methods of verification to log in to your Braze account: your password and your mobile phone.  Braze uses [Authy][56], a two-factor authentication service, to help secure your account.

#### Two-factor authentication Authy set up overview

1. Download the Authy App.
2. Navigate to **Two-Factor Authentication** under **Account Settings** and enter your phone number.
3. There will be a notification sent to the device instructing to open Authy to obtain the code for Braze.
4. Open the Authy App on the device linked to obtain the code. 
5. Navigate to **Two-Factor Authentication** settings and enter the code. 

If you would like to enforce two-factor authentication for the whole company, turn on two-factor authentication under the **Security Settings** tab and click **Save Changes** at the bottom of the page.

![Two-Factor Authentication section of the Security Settings tab][53]

When your company enforces two-factor authentication, account users must set up two-factor authentication on their own account upon log in or else they will be locked out. Account users can also go to their account settings page to enable it. There is an option to change your mobile phone number in case an account user would like to authenticate using a different mobile phone number.  In addition, if two-factor authentication is optional for your company under **Security Settings**, account users will have the option to disable two-factor authentication.
If you have any trouble enabling or verifying with two-factor authentication, contact your account administrator or open a [support ticket]({{site.baseurl}}/braze_support/).

Under the **Manage Users** tab, there will be an additional column that indicates which account users have turned on two-factor authentication.

![Account Users section on the Manage Users page][55]

[2]: {{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/email_settings/#include-a-list-unsubscribe-header
[7]: {% image_buster /assets/img_archive/email_settings_custom_new.png %}
[22]: {% image_buster /assets/img_archive/company_analytics_report_new.png %}
[50]: {% image_buster /assets/img_archive/security_settings_new.png %}
[51]: {% image_buster /assets/img_archive/authentication_rules_new.png %}
[52]: {% image_buster /assets/img_archive/dashboard_ip_whitelisting_new.png %}
[53]: {% image_buster /assets/img_archive/two_factor_authentication_new.png %}
[55]: {% image_buster /assets/img_archive/two_factor_authentication_manage_users_new.png %}
[56]: https://www.authy.com
[57]: {% image_buster /assets/img_archive/list_unsub_img1.png %}
[61]: {% image_buster /assets/img_archive/notification_preferences.png %}
[62]: https://api.slack.com/incoming-webhooks
[63]: {% image_buster /assets/img_archive/slack_f.png %}
[64]: {% image_buster /assets/img_archive/copy_url.png %}
[65]: {% image_buster /assets/img_archive/click_edit_f.png %}
[67]: https://my.slack.com/services/new/incoming-webhook/
[84]: https://tools.ietf.org/html/rfc4632
