---
nav_title: Company Wide Settings
page_order: 5
description: "The Company Settings Page allows you to change the name of your company, set your timezone and request to delete your company."
---

# Company Wide Settings Management

## Company Settings Page

The [Company Settings Page][1] allows you to change the name of your company, set your timezone and request to delete your company.

{% alert note %}
Note that only Admins and users with explicit permissions to manage Company Settings will see this page.
{% endalert %}

### Consequences of Switching Your Time Zone

If you choose to switch your time zone, you may face a variety of consequences:

- While campaigns scheduled for specific times in specific locations (i.e. 9pm Eastern Time) will run properly on schedule until edited, both campaign analytics and future campaign schedules will be affected by the change.
- Any card scheduling that is not assigned to Local Time may be affected, with active cards potentially appearing as finished (or vice versa).
- Segmentation filters of the form "Has done X before/after `Date`" will have the time adjusted because the initial date will now be localized in Pacific Time.

### Notification Preferences

The Notification Preferences Page is where you can configure who (if anyone) receives notifications about your company. You can configure who should receive notifications regarding campaign and News Feed Card delivery, technical errors. You can also specify recipients for the weekly analytics report. For most notifications, Braze supports email and webhook channels.

![Notification_Preferences][61]

The available notifications are in the table below:

| Notification | Description | Webhook Support |
|--------------|-------------|-----------------|
| AWS Credential Errors               | Notifies recipients when Braze receives an error while attempting to use your Amazon Web Services credentials for a data export.                        | Yes             |
| Scheduled Campaign Sent/Not Sent    | Notifies recipients when scheduled campaigns begin sending or when scheduled campaigns attempted to send, but had no eligible users to send to.         | Yes             |
| Scheduled Campaign Limit Met        | Notifies recipients when a scheduled recurring campaign is not sent because the total campaign limit has been met.                                      | Yes             |
| Scheduled Campaign Finished Sending | Notifies recipients when a scheduled campaign has finished sending.                                                                                     | Yes             |
| Webhook Timeouts                    | Notifies recipients when a webhook URL times out more than 300 times in 5 minutes. This notification sends no more than once every two hours.           | Yes             |
| Push Credential Errors              | Notifies recipients when an app's push credentials are invalid and when an app's push credentials are expiring soon.                                    | Yes             |
| Connected Content Timeouts          | Notifies recipients when a Connected Content URL times out more than 300 times in 5 minutes. This notification sends no more than once every two hours. | Yes             |
| News Feed Card Published/Live        | Notifies recipients when News Feed cards are scheduled or published.                                                                                     | Yes             |
| Weekly Analytics Report             | Sends a summary of the past week's app group activity to recipients every Monday. Recipients receive a summary for each app group that they belong to.  | No              |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### Slack Incoming Webhook Integration

Slack has an [incoming webhook app][62] that allows messages to be posted from external sources into Slack. To get started, open the [incoming webhook app][67].

- Click "Add Configuration"

![add_configuration][63]

- Select the Slack channel that you'd like the notifications to go to

- Slack will generate a URL that you'll need to enter into the settings for the notifications that you wish to receive

![copy_url][64]

- Navigate to the Notification Preferences page in Company Settings

- Click into the notification that you wish to enable for Slack. Or, if you have multiple notifications that you want to send to this Slack Channel, you can use our "Bulk Add" feature to add the webhook to multiple notifications

![click_edit][65]

- Enter the URL that Slack generated for you

That's it! You should start receiving notifications about your company to this Slack Channel!

### Weekly Analytics Reporting

Braze optionally sends a weekly report via email to individuals you designate within your company every Monday at 5AM EST. The custom events to be included in the weekly report are selected on the Custom Events Management Tab within the ["Manage Settings"][19] page of the dashboard. You may select up to 5 events to be included in your weekly report:

![Analytics Report Event Selection][22]

### Additional Email Settings

You also can access the [Settings - Email Settings Tab][8] to edit:

- The name which will be displayed by default on your emails
- The default reply-to address for your emails
- Your custom unsubscribe page
  - If you do not provide a custom unsubscribe page Braze will handle unsubscribes automatically

![email settings][7]

## List-Unsubscribe Settings

### Overview
Although most marketers add a one-click Unsubscribe link to their email, it is best practice to provide a special email header (“List-Unsubscribe”) that allows email service providers such as Gmail and Windows Live Hotmail to provide their own Unsubscribe functionality:

![list_unsub_1] [57]


### Benefits of the List-Unsubscribe Header
Some recipients prefer to have an Unsubscribe link available in the same place for all emails, rather than having to find links in each mailing. When enabled, this feature puts a prominent Unsubscribe link in the header of the email client, making it easier to unsubscribe and therefore less likely that customers will mark your email as Spam. This has a significant impact on your reputation and deliverability as an email sender.

### How the List-Unsubscribe Header Works
Navigate to ‘Email Settings’ within your AppGroup.

Set List-Unsubscribe to ‘ON'
![list_unsub_3] [59]

> This feature only applies to emails that target users who are “subscribed or opted in” or “opted-in only.”

The header is not added for messages targeting “all users including unsubscribed users,” as these represent transactional messages which do not need an unsubscribe function.

*Currently ‘Windows Live Hotmail’ and ‘Gmail’ support this feature.*

{% alert note %}
If you use Mailjet, you do not have the flexibility to choose on/off for this feature - it will be `ON` by default.
{% endalert %}

## Security Settings

The security settings page is where you can configure authentication rules, dashboard IP whitelisting, and two-factor authentication. These settings are located in the ["Security Settings" tab of the Company Settings page][83].

![Security Settings][50]

### Authentication Rules

Company administrators can configure authentication requirements for signing into Braze including setting password requirements (minimum password length, password complexity, password expiration), and enforcing Google authentication.  If the company administrator decides to set password authentication rules to become more strict, as soon as these rules are set, account users will be informed by email to change their passwords accordingly.

![Authentication Rules][51]

### Dashboard IP Whitelisting

Your team can add a whitelist of specific IP addresses, ranges and subnets from which users can log in to your company's Braze account.

To mark specific IP addresses and subnets as whitelisted, fill in the IP addresses and subnets to whitelist and press Save Changes at the bottom of the page. IP ranges and subnets should be specified in CIDR (Classless Inter-Domain Routing) notation. For example, whitelisting `63.45.134.*` would be expressed in CIDR notation as `63.45.134.0/24`

For more information on CIDR notation see [RFC 4632][84].

![Dashboard IP Whitelisting][52]

### Two-Factor Authentication

Two-factor authentication adds an extra layer of identity verification upon login. By enabling two-factor authentication, Braze will require two methods of verification to log in to your Braze account: your password and your mobile phone.  Braze uses [Authy][56], a two-factor authentication service, to help secure your account.

#### Two-Factory Authentication Authy Set Up Overview
1. Download the Authy App.
2. Navigate to Two-Factor Authentication under Account Settings and enter your phone number.
3. There will be a notification sent to the device instructing to open Authy to obtain the code for Braze.
4. Open the Authy App on the device linked to obtain the code. 
5. Navigate to Two-Factor Authentication settings and enter the code. 

If you would like to enforce two-factor authentication for the whole company, turn on two-factor authentication under the Security Settings tab and press Save Changes at the bottom of the page.

![Two-Factor Authentication - Company Settings][53]

When your company enforces two-factor authentication, account users must set up two-factor authentication on their own account upon log in or else they will be locked out. Account users can also go to their account settings page to enable it. There is an option to change your mobile phone number in case an account user would like to authenticate using a different mobile phone number.  In addition, if two-factor authentication is optional for your company under Security Settings, account users will have the option to disable two-factor authentication.
If you have any trouble enabling/verifying with two-factor authentication, please contact your account administrator or [open a support ticket][support].

Under the Manage Users page, there will be an additional column that indicates which account users have turned on two-factor authentication.

![Two-Factor Authentication - Manage Users][55]

[1]: https://dashboard-01.braze.com/company_settings/company_settings/ "Company Settings Page"
[7]: {% image_buster /assets/img_archive/email_settings_custom_new.png %}
[8]: https://dashboard-01.braze.com/app_settings/app_settings/email/ "Email App Settings"
[19]: https://dashboard-01.braze.com/app_settings/app_settings/ "App Settings Page"
[22]: {% image_buster /assets/img_archive/company_analytics_report_new.png %}
[support]: {{site.baseurl}}/support_contact/
[50]: {% image_buster /assets/img_archive/security_settings_new.png %}
[51]: {% image_buster /assets/img_archive/authentication_rules_new.png %}
[52]: {% image_buster /assets/img_archive/dashboard_ip_whitelisting_new.png %}
[53]: {% image_buster /assets/img_archive/two_factor_authentication_new.png %}
[55]: {% image_buster /assets/img_archive/two_factor_authentication_manage_users_new.png %}
[56]: https://www.authy.com
[57]: {% image_buster /assets/img_archive/list_unsub_img1.png %}
[59]: {% image_buster /assets/img_archive/list_unsub_img3_new.png %}
[61]: {% image_buster /assets/img_archive/notification_preferences.png %}
[62]: https://api.slack.com/incoming-webhooks
[63]: {% image_buster /assets/img_archive/slack_f.png %}
[64]: {% image_buster /assets/img_archive/copy_url.png %}
[65]: {% image_buster /assets/img_archive/click_edit_f.gif %}
[67]: https://my.slack.com/services/new/incoming-webhook/









[83]: https://dashboard-01.braze.com/company_settings/company_settings/security-management/
[84]: https://tools.ietf.org/html/rfc4632
