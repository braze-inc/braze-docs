---
nav_title: Email Settings
article_title: Email Settings
page_type: reference
page_order: 3
description: "This reference article covers email settings in the Braze Dashboard."
tool: Dashboard
channel: email

---

# Email Settings

Email settings can be found within the **Manage Settings** page of the Dashboard. Here, Braze allows you to set specific outbound email settings like display name, reply-to address, custom footers, custom opt-in and opt-out pages, and more. Including features like these in your outbound emails make for a fluid and cohesive customer experience.

## Outbound Email Settings

### Multiple Sending Emails

Use the outbound email settings below to change the name and email address used when Braze sends emails to your users. Using these settings, you may also include additional sending and reply-to addresses. These addresses will be available when building your campaign through the **Edit Sending Info** options available as you compose your campaign email.

Here, you may also exclude the "Reply-To" email and exclusively send replies to the "From" address.

![Outbound Email][1]

This feature allows you to:

- Set up multiple sending and reply-to email addresses
- Set a default sending and reply-to address
- Exclude the reply-to option and send replies to the "From" address

When setting your "From" addresses, make sure your "From" email domain matches your sending domain (i.e., marketing.yourdomain.com). Failure to do this may result in SPF and DKIM misalignment. All reply-to emails can be set to your root domain.

### BCC Addresses

The **BCC Address** settings allow you to add and manage BCC addresses that can be appended to outbound email messages sent from Braze. Appending a BCC address to an email message will send an identical copy of the message your user receives to your BCC inbox. This is a useful tool to retain copies of messages you sent your users for compliance requirements or customer support issues.

{% alert important %} 
Appending a BCC address to your campaign or Canvas step will result in your billable emails for the campaign or Canvas step being doubled as Braze sends one message to your user and one to your BCC address. Please contact your Customer Success Manager to enable this feature. 
{% endalert %}

![BCC Address][11]

Once you add an address, the address will be made available to select when composing an email in either campaigns or Canvas steps. Select **Make Default** next to an address to set this address to be selected by default when launching a new email campaign or Canvas step. If you'd like to override this at the message level, you can select **No BCC** when setting up your message.

If you require that all email messages sent from Braze have a BCC address included, you can check **Require a BCC address for all your email campaigns**. This will require you to select a default address which will be automatically selected on new email campaigns or Canvas steps. The default address will also be automatically added to all messages triggered through our REST API. 

There is no need to change the existing API request to include the address. Checking the box in the Braze dashboard to require BCC will set the address at the time of sending.  

![Require BCC][12]

### Custom Footer

For commercial emails, the [CAN-SPAM Act][5] requires that all commercial emails include an unsubscribe option. With the custom footer settings, you are able to remain CAN-SPAM compliant while also customizing your email opt-out footer. In order to remain compliant, you must add your custom footer to all emails sent as part of campaigns for this app group. To read more about custom footer Liquid templating, check out our [documentation]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#changing-email-subscriptions).

![Custom Footer][0]

Requirements:

- Must include an unsubscribe URL and physical mailing address.
- Custom Footers should be less than 100KB.

Learn more about email best practices [here][7].

## Custom Unsubscribe Page

Within the email settings, Braze lets you set a **Custom Unsubscribe Page**. This page will be viewable once a user has selected Unsubscribe from the bottom of an email. This feature is great if you want your branding and message to remain consistent throughout your user lifecycle.

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

The email opening tracking pixel is an invisible 1px by 1px image that automatically gets inserted into your email HTML. This pixel helps Braze detect whether the end-users have opened your email. Email open information can be very useful, helping users determine effective marketing strategies by understanding the corresponding open rates.

### Placing the Tracking Pixel

Braze's default behavior is to append the tracking pixel to the bottom of your email. For the vast majority of users, this is the ideal place to put the pixel. While the pixel is already styled to cause as few visual changes as possible, any unintentional visual changes would be the least visible at the bottom of an email. This is also the default for email providers such as SendGrid and SparkPost.

However, a small subset of companies may prefer that the pixel get templated to a different location. One advantage of not placing the tracking pixel at the bottom is avoiding cases where it gets cut off by clients (e.g., Gmail) that truncate emails after a certain amount of kilobytes.

### Changing Location of Tracking Pixel

Braze currently supports overriding the ESP's default open tracking pixel location (the last tag in the <body> of an email) to move it to the first tag in the <body>.
  
![open_pixel][13]

To change the location:
1. Go to __Manage App Group__, then __Email Settings__ in your Braze account.
2. Click the checkbox under __Custom Open Tracking Pixel Settings__. 
3. Press __Save__.

Once saved, Braze will send special instructions to the ESP in order to place the open tracking pixel at the top of all HTML emails.
  
{% alert important %} 
SSL enablement will wrap the URL of the tracking pixel with HTTPS instead of HTTP - if your SSL is misconfigured, it may affect the efficacy of the tracking pixel. 
{% endalert %}
  
## Toggle-Capable Features

![switch][2]{: style="float:right;max-width:30%;margin-left:15px;"}

The three email settings listed below are features that require no additional action other than toggling it on or off by using the corresponding switch. Please read each setting for further details.

### Resubscribe Users when Their Email Changes

You may automatically resubscribe users when they change their email address. For example, if a previously unsubscribed app group user changes their email address to one that is not on Braze's unsubscribe list, they will automatically become resubscribed.

Learn more about best practices for email list management [here][8].

### Include a List-Unsubscribe Header

![list_unsub_1][00]{: style="float:right;max-width:60%;margin-left:15px;"}

This feature allows you to automatically include a List-Unsubscribe email header for emails sent to subscribed or opted-in users. This List-Unsubscribe header allows email providers to include an "Unsubscribe" button when displaying an email.

#### Benefits of the List-Unsubscribe Header

Some recipients prefer to have an Unsubscribe link available in the same place for all emails, rather than having to find links in each mailing. When enabled, this feature puts a prominent Unsubscribe link in the header of the email client, making it easier to unsubscribe and therefore less likely that customers will mark your email as Spam. This has a significant impact on your reputation and deliverability as an email sender.

#### How the List-Unsubscribe Header Works

Navigate to **Email Settings** within your AppGroup. Toggle List-Unsubscribe to **ON**.

![list_unsub_3] [59]

When enabled, this feature will add a standard list-unsubscribe 'mailto:' header to all eligible outgoing emails.  Upon receipt of a list-unsubscribe request from an end-user, Braze will ensure the same person who was sent the email is being unsubscribed.  If there is no match, we will not process this request.

> This feature only applies to emails that target users who are “subscribed or opted in” or “opted-in only.”

The header is not added for messages targeting “all users including unsubscribed users,” as these represent transactional messages which do not need an unsubscribe function.

*Currently ‘Windows Live Hotmail’ and ‘Gmail’ support this feature.*

{% alert note %}
If you use Mailjet, you do not have the flexibility to choose on/off for this feature - it will be `ON` by default.
{% endalert %}

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
[7]: {{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/managing_email_subscriptions/#unsubscribed-email-addresses
[8]: {{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/
[10]: {{site.baseurl}}/user_guide/message_building_by_channel/email/css_inline/
[11]: {% image_buster /assets/img/email_settings/bcc_address.png %}
[12]: {% image_buster /assets/img/email_settings/require_bcc.png %}
[13]: {% image_buster /assets/open_pixel.png %}
[59]: {% image_buster /assets/img_archive/list_unsub_img3_new.png %}
