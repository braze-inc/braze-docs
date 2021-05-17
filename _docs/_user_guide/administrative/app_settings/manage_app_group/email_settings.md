---
nav_title: Email Settings
page_type: reference
page_order: 3
---

# Email Settings

Email settings can be found within the Manage Settings page of the Dashboard. Here, Braze allows you to set specific outbound email settings like display name, reply-to address, custom footers, custom opt-in and opt-out pages, and more. Including features like these in your outbound emails make for a fluid and cohesive customer experience.

## Outbound Email Settings

### Multiple Sending Emails

Use the outbound email settings below to change the name and email address used when Braze sends emails to your users. Using these settings, you may also include additional sending and reply-to addresses. These addresses will be available when building your campaign through the "Edit Sending Info" options available as you compose your campaign email. Here, you may also exclude the Reply-To email and exclusively send replies to the "From" address.

![Outbound Email][1]

This feature allows you to:
- Set Up Multiple Sending and Reply-To Email Addresses
- Set Default Sending and Reply-To Address
- Exclude Reply-To option and send replies to the "From" Address

When setting your "From" addresses, make sure your "From" email domain, matches your sending domain (i.e. marketing.yourdomain.com), failure to do this may result in SPF and DKIM misalignment. All reply-to emails can be set to your root domain. 

### BCC Addresses

The BCC Address settings will allow you to add and manage BCC addresses that can be appended to outbound email messages sent from Braze. Appending a BCC address to a email message will send an identical copy of the message your user receives to your BCC inbox. This is a useful tool to retain copies of messages you sent your users for compliance requirements or customer support issues. 

Appending a BCC address to your Campaign or Canvas step will result in your billable emails for the Campaign or Canvas step being doubled as Braze sends one message to your user, and one to your BCC address. Please contact your Customer Success Manager to enable this feature. 

![BCC Address][11]

Once you add an address, the address will be made available to select when composing an email in either Campaigns or Canvas steps. Selecting "Make Default" next to an address will set this address to be selected by default when launching a new email Campaign or Canvas step. If you'd like to override this at the message level, you can select "No BCC" when setting up your message.

If you require that all email messages sent from Braze have a BCC address included, you can check "Require a BCC address for all your email campaigns". This will require you select a default address which will be automatically selected on new email Campaigns or Canvas steps. The default address will also be automatically added to all messages triggered through our REST API. There is no need to change existing API request to include the address. Checking the box in the Braze dashboard to require BCC will set the address at the time of send.  

![Require BCC][12]



### Custom Footer

For commercial emails, the [CAN-SPAM Act][5] requires that all commercial emails include an unsubscribe option. With the custom footer settings, you are able to remain CAN-SPAM compliant, while also customizing your email opt-out footer. Braze will append this footer to all emails sent as part of Campaigns for this App Group.

![Custom Footer][0]

Requirements:
- Must include an unsubscribe URL and physical mailing address
- Custom Footers should be less than 100KB

Learn more about email best practices [here][7].

## Custom Unsubscribe Page

Within the email settings, Braze lets you set a Custom Unsubscribe Page. This page will be viewable once a user has selected Unsubscribe from the bottom of an email. This feature is great if you want your branding and message to remain consistent throughout your user lifecycle.

![Custom Unsubscribe][3]

Requirements:
- Must provide your own HTML for this feature.
- Unsubscribe pages should be less than 750KB.

Learn more about best practices for email list management [here][7].

## Custom Opt-In Page

Within the email settings, Braze lets you set a Custom Opt-In Page. This feature is great if you want your branding and message to remain consistent throughout your user lifecycle.

![Custom Opt-In][4]

Requirements:
- Must provide your own HTML for this feature.
- Unsubscribe pages should be less than 750KB.

Learn more about best practices for email list management [here][7].

## Email Open Tracking Pixel

The email opening tracking pixel is an invisible 1px by 1px image that automatically gets inserted into your email HTML. This pixel helps Braze detect whether the end users have opened your email. Email open information can be very useful, helping our clients determine effective marketing strategies understanding and assess the corresponding open rates.

For more information regarding the email open tracking pixel, check out our short [LAB course][6].

## Toggle-Capable Features
![switch][2]{: style="float:right;max-width:30%;margin-left:15px;"}

The three email settings listed below are features that require no additional action other than toggling it on or off by using the corresponding switch. Please read each setting for further details.

### Resubscribe Users when Their Email Changes

You may automatically resubscribe users when they change their e-mail address. For example, if a previously unsubscribed app group user changes their e-mail address to one that is not on Braze's unsubscribe list, they will automatically become resubscribed.

Learn more about best practices for e-mail list management [here][8].

### Include a List-Unsubscribe Header

![list_unsub_1][00]{: style="float:right;max-width:60%;margin-left:15px;"}

This feature allows you to automatically include a List-Unsubscribe email header for emails sent to subscribed or opted-in users. This List-Unsubscribe header allows email providers to include an "Unsubscribe" button when displaying an email.

Learn more about List-Unsubscribe headers [here][9].

### Inline CSS on New Emails by Default

CSS inlining is a technique that automatically inlines your emails' CSS styles. For some email clients, this can improve the way that your emails render. This feature automatically inlines CSS on new emails by default.

Changing this setting will not affect any of your existing email messages or templates. You can override this default at any time while composing messages or templates.

For more information, check out our CSS Inlining [Documentation][10]

[00]: {% image_buster /assets/img_archive/list_unsub_img1.png %}
[0]: {% image_buster /assets/img/email_settings/custom_footer.png %}
[1]: {% image_buster /assets/img/email_settings/outbound_email.png %}
[2]: {% image_buster /assets/img/email_settings/switch.gif %}
[3]: {% image_buster /assets/img/email_settings/custom_unsubscribe.png %}
[4]: {% image_buster /assets/img/email_settings/custom_opt_in.png %}
[5]: https://en.wikipedia.org/wiki/CAN-SPAM_Act_of_2003
[6]: https://lab.braze.com/email-open-tracking-pixel
[7]: {{site.baseurl}}/help/best_practices/email/managing_email_subscriptions/#unsubscribed-email-addresses
[8]: {{site.baseurl}}/help/best_practices/email/managing_email_subscriptions/
[9]: {{site.baseurl}}/user_guide/administrative/manage_your_braze_users/company-wide_settings_management/#list-unsubscribe-settings
[10]: {{site.baseurl}}/user_guide/message_building_by_channel/email/css_inline/
[11]: {% image_buster /assets/img/email_settings/bcc_address.png %}
[12]: {% image_buster /assets/img/email_settings/require_bcc.png %}
