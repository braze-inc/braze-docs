---
nav_title: Email Preferences
article_title: Email Preferences
page_type: reference
page_order: 14
description: "This reference article covers email preferences in the Braze dashboard, including sending configurations, open tracking pixels, subscription page and footers, and more."
tool: Dashboard
channel: email

---

# Email Preferences

> Email Preferences is where you can set specific outbound email settings like custom footers, custom opt-in and opt-out pages, and more. Including these options in your outbound emails make for a fluid and cohesive experience for your users.

**Email Preferences** can be found under **Settings** in the dashboard.

{% alert note %}
If you are using the [older navigation]({{site.baseurl}}/navigation), this page is called **Email Settings** and is located under **Settings** > **Manage Settings** > **Email Settings**.
{% endalert %}

## Sending configuration

The email settings under the **Sending Configuration** section determine which details are included in your email campaigns. In particular, these settings are mainly related to what your user sees when they receive an email from Braze.

### Outbound email settings

When configuring your email settings, your outbound email settings identify which name and email addresses are used when Braze sends emails to your users.

{% tabs local %}
{% tab Display Name Address %}

In this section, you can add the names and email addresses that can be used when Braze sends emails to your users. The display names and email addresses will be available in the **Edit Sending Info** options as you compose your email campaign. Note that updates made to the outbound email settings do not retroactively affect existing sends. 

![]({% image_buster /assets/img/email_settings/display_name_address.png %})

When setting your "From" addresses, make sure your "From" email domain matches your sending domain (such as marketing.yourdomain.com). Failure to do this may result in SPF and DKIM misalignment. Emails with dynamic "From" addresses will be sent from the IP pool of the corresponding sending domain. All reply-to emails can be set to your root domain.

{% endtab %}
{% tab Reply-To Address %}

Adding an email address in this section allows you to select it as a reply-to address for your email campaign. You can also make an email address the default one by selecting **Make Default**. These email addresses will be available in the **Edit Sending Info** options as you compose your email campaign.

![]({% image_buster /assets/img/email_settings/reply_to_address.png %}){: style="max-width:75%;" }

{% endtab %}
{% tab BCC Address %}

This section allows you to add and manage BCC addresses that can be appended to outbound email messages sent from Braze. Appending a BCC address to an email message will send an identical copy of the message your user receives to your BCC inbox. This is a useful tool to retain copies of messages you sent your users for compliance requirements or customer support issues.

{% alert important %} 
Appending a BBC address to your campaign or Canvas will result in doubling your billable emails for the campaign or Canvas component since Braze will send one message to your user and one to your BCC address.
{% endalert %}

![BCC Address section of the Email Settings tab.]({% image_buster /assets/img/email_settings/bcc_address.png %}){: style="max-width:75%;" }

Once you add an address, the address will be made available to select when composing an email in either campaigns or Canvas steps. Select **Make Default** next to an address to set this address to be selected by default when launching a new email campaign or Canvas component. To override this at the message level, you can select **No BCC** when setting up your message.

If you require that all email messages sent from Braze have a BCC address included, you can select the **Require a BCC address for all your email campaigns** toggle. This will require you to select a default address which will be automatically selected on new email campaigns or Canvas steps. The default address will also be automatically added to all messages triggered through our REST API. There is no need to change the existing API request to include the address.

{% endtab %}
{% endtabs %}

## Open tracking pixel

[![Braze Learning course]({% image_buster /assets/img/bl_icon2.png %})](https://learning.braze.com/email-open-tracking-pixel/){: style="float:right;width:120px;border:0;" class="noimgborder"}

The email opening tracking pixel is an invisible 1 x 1&nbsp;px image that automatically gets inserted into your email HTML. This pixel helps Braze detect whether the end-users have opened your email. Email open information can be very useful, helping users determine effective marketing strategies by understanding the corresponding open rates.

### Placing the tracking pixel

The default behavior in Braze is to append the tracking pixel to the bottom of your email. For the majority of users, this is the ideal place to put the pixel. While the pixel is already styled to cause as few visual changes as possible, any unintentional visual changes would be the least visible at the bottom of an email. This is also the default for email providers such as SendGrid and SparkPost.

### Changing location of tracking pixel

Braze currently supports overriding the ESP's default open tracking pixel location (the last tag in the `<body>` of an email) to move it to the first tag in the `<body>`.
  
![][13]{: style="max-width:80%;" }

To change the location:

1. In Braze, go to **Settings** > **Email Preferences**.
2. Click the checkbox under **Custom Open Tracking Pixel Settings**. 
3. Press **Save**.

{% alert note %}
If you are using the [older navigation]({{site.baseurl}}/navigation), this is located at **Manage Settings** > **Email Settings**.
{% endalert %}

Once saved, Braze will send special instructions to the ESP in order to place the open tracking pixel at the top of all HTML emails.
  
{% alert important %} 
SSL enablement will wrap the URL of the tracking pixel with HTTPS instead of HTTP-if your SSL is misconfigured, it may affect the efficacy of the tracking pixel. 
{% endalert %}

## List-unsubscribe header

{% alert note %}
Beginning on February 15, 2024, new companies will have the list-unsubscribe header (with one-click unsubscribe) enabled by default.
{% endalert %}

Using a list-unsubscribe header allows your recipients to unsubscribe easily from marketing emails by displaying an **Unsubscribe** button within the mailbox UI, and not the message body.

![]({% image_buster /assets/img_archive/list_unsub_img1.png %}){: style="float:right;max-width:60%;margin-left:15px;"}

When a recipient clicks **Unsubscribe**, the mailbox provider sends the unsubscribe request to the destination defined in the email header.

Enabling list-unsubscribe is a deliverability best practice and a requirement at some of the premier mailbox providers. It encourages end users to safely remove themselves from unwanted messages versus hitting the spam button in an email client, the latter of which is detrimental to sending reputation and email deliverability.

### How it works

![]({% image_buster /assets/img/email_settings/target_audiences_example.png %}){: style="float:right;max-width:60%;margin-left:15px;"}

When turned on, this feature is applied to the entire workspace, not the company-level. It's added to campaigns and Canvases that are set up to send to users who are subscribed or opted-in, or opted-in users only in the **Target Audiences** step of the campaign and Canvas builders.

Braze doesn't add the header for what is considered transactional, so if a message is set to send to all users including unsubscribed users, the list-unsubscribe header will not be attached to the message. Additionally, the header is not added for messages delivered via test send because the list-unsubscribe header is only generated and added for targeting user profiles in Braze.

### Default list-unsubscribe header

{% alert important %}
Gmail intends for senders to implement the one-click unsubscribe for all their outgoing commercial, promotional messages as of June 1, 2024. For more information see [Gmail’s sender guidelines](https://support.google.com/mail/answer/81126?hl=en#subscriptions&zippy=%2Crequirements-for-sending-or-more-messages-per-day:~:text=Make%20it%20easy%20to%20unsubscribe) and [Gmail’s Email Sender Guidelines FAQ](https://support.google.com/a/answer/14229414#zippy=%2Cwhat-time-range-or-duration-is-used-when-calculating-spam-rate%2Cif-the-list-header-is-missing-is-the-message-body-checked-for-a-one-click-unsubscribe-link%2Cif-unsubscribe-links-are-temporarily-unavailable-due-to-maintenance-or-other-reasons-are-messages-flagged-as-spam%2Ccan-a-one-click-unsubscribe-link-to-a-landing-or-preferences-page%2Cwhat-is-a-bulk-sender%2Chow-can-bulk-senders-make-sure-theyre-meeting-the-sender-guidelines%2Cdo-the-sender-guidelines-apply-to-messages-sent-to-google-workspace-accounts%2Cdo-the-sender-guidelines-apply-to-messages-sent-from-google-workspace-accounts%2Cwhat-happens-if-senders-dont-meet-the-requirements-in-the-sender-guidelines%2Cif-messages-are-rejected-because-they-dont-meet-the-sender-guidelines-do-you-send-an-error-message-or-other-alert%2Cwhat-happens-when-sender-spam-rate-exceeds-the-maximum-spam-rate-allowed-by-the-guidelines%2Cwhat-is-the-dmarc-alignment-requirement-for-bulk-senders%2Cif-messages-fail-dmarc-authentication-can-they-be-delivered-using-ip-allow-lists-or-spam-bypass-lists-or-will-these-messages-be-quarantined%2Ccan-bulk-senders-get-technical-support-for-email-delivery-issues%2Cdo-all-messages-require-one-click-unsubscribe:~:text=for%20mitigations.-,Unsubscribe%20links,-Do%20all%20messages). Yahoo announced an early 2024 timeline for the updating requirements. For more information refer to [More Secure, Less Spam: Enforcing Email Standards for a Better Experience](https://blog.postmaster.yahooinc.com/).
{% endalert %}

If you use the Braze unsubscribe feature to process unsubscribes on your behalf directly, you can select **Email Unsubscribe Header** and save the “Braze default” as the setting. Braze will generate the one-click unsubscribe and mailto header to be added to your promotional emails. Using one-click unsubscribe for the list-unsubscribe header ([RFC 8058](https://datatracker.ietf.org/doc/html/rfc8058)) focuses on a straightforward way for recipients to opt-out from emails, and is a requirement from Yahoo and Gmail for bulk senders. 

When Braze receives a list-unsubscribe request from a user, this user's global email subscription state is set to unsubscribed. If there isn't a match, Braze will not process this request.

![Option to automatically include a list-unsubscribe header for emails sent to subscribed or opted-in users.]({% image_buster /assets/img/email_settings/email_unsubscribe_header.png %}){: style="max-width:80%;"}

### One-click unsubscribe

Using one-click unsubscribe for the list-unsubscribe header ([RFC 8058](https://datatracker.ietf.org/doc/html/rfc8058)) focuses on providing an easy way for recipients to opt-out from emails. 

#### Requirements

If you're sending emails using your own custom unsubscribe functionality, you must meet the following requirements to make sure the one-click unsubscribe URL that you set up is in accordance with RFC 8058:

* The URL must be able to handle unsubscribe POST requests
* The URL must start with `https://`
* The URL must be wrapped between `<` and `>`
* The URL must not return an HTTPS redirect. One-click unsubscribe links that go to a landing or other type of web page don't comply with RFC 8058
* The message must have a valid DKIM signature

{% alert note %}
Gmail intends for senders to implement the one-click unsubscribe for all their outgoing commercial, promotional messages as of June 1, 2024. For more information see [Gmail’s sender guidelines](https://support.google.com/mail/answer/81126?hl=en#subscriptions&zippy=%2Crequirements-for-sending-or-more-messages-per-day:~:text=Make%20it%20easy%20to%20unsubscribe) and [Gmail’s Email Sender Guidelines FAQ](https://support.google.com/a/answer/14229414#zippy=%2Cwhat-time-range-or-duration-is-used-when-calculating-spam-rate%2Cif-the-list-header-is-missing-is-the-message-body-checked-for-a-one-click-unsubscribe-link%2Cif-unsubscribe-links-are-temporarily-unavailable-due-to-maintenance-or-other-reasons-are-messages-flagged-as-spam%2Ccan-a-one-click-unsubscribe-link-to-a-landing-or-preferences-page%2Cwhat-is-a-bulk-sender%2Chow-can-bulk-senders-make-sure-theyre-meeting-the-sender-guidelines%2Cdo-the-sender-guidelines-apply-to-messages-sent-to-google-workspace-accounts%2Cdo-the-sender-guidelines-apply-to-messages-sent-from-google-workspace-accounts%2Cwhat-happens-if-senders-dont-meet-the-requirements-in-the-sender-guidelines%2Cif-messages-are-rejected-because-they-dont-meet-the-sender-guidelines-do-you-send-an-error-message-or-other-alert%2Cwhat-happens-when-sender-spam-rate-exceeds-the-maximum-spam-rate-allowed-by-the-guidelines%2Cwhat-is-the-dmarc-alignment-requirement-for-bulk-senders%2Cif-messages-fail-dmarc-authentication-can-they-be-delivered-using-ip-allow-lists-or-spam-bypass-lists-or-will-these-messages-be-quarantined%2Ccan-bulk-senders-get-technical-support-for-email-delivery-issues%2Cdo-all-messages-require-one-click-unsubscribe:~:text=for%20mitigations.-,Unsubscribe%20links,-Do%20all%20messages). Yahoo announced an early 2024 timeline for the updating requirements. For more information refer to [More Secure, Less Spam: Enforcing Email Standards for a Better Experience](https://blog.postmaster.yahooinc.com/).<br><br>
Braze intends to add support for one-click unsubscribe in early 2024, as well as the ability to add your "mailto:" and one-click unsubscribe URL that’s setup by the sender in the list-unsubscribe header.
{% endalert %}

#### Mailbox provider support

The following table summarizes mailbox provider support for “mailto:” header, list-unsubscribe URL, and one-click unsubscribe ([RFC 8058](https://datatracker.ietf.org/doc/html/rfc8058)).

| List-unsubscribe header | Mailto: header | List-unsubscribe URL | One-click unsubscribe (RFC 8058) | 
| ----- | --- | --- | --- |
| Gmail | Supported* | Supported | Supported |
| Gmail Mobile | Not supported | Not supported | Not supported |
| Apple Mail | Supported | Not supported | Not supported |
| Outlook.com | Supported | Not supported | Not supported |
| Yahoo! Mail | Supported* | Not supported | Supported |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

_*Yahoo and Gmail will eventually deprecate the "mailto:" header and will only support one-click._

Displaying the header is ultimately determined by the mailbox provider. To check if the list-unsubscribe header is included in the raw (text) email for the recipient in Gmail, do the following:

1. Select **Show Original** in the email. This opens a new tab with the raw version of the email and its headers.
2. Search for "List-Unsubscribe".

If the header is in the raw version of the email but is not displayed, the mailbox provider has determined to not show the unsubscribe option, meaning we don't have further insight as to why the mailbox provider isn't displaying the header. Seeing the list-unsubscribe header is ultimately reputation-based. In most cases, the better your sender reputation with the inbox, the less likely the list-unsubscribe header will appear. 

## Append email subject lines

Use the toggle to include "[TEST]" and "[SEED]" in your test and seed email subject lines. This can help identify any email campaigns sent as tests.

![]({% image_buster /assets/img/email_settings/test_and_seed_email_subject_line.png %}){: style="max-width:70%;"}

## Inline CSS on new emails by default

CSS inlining is a technique that automatically inlines CSS styles for your emails and new emails. For some email clients, this can improve the way that your emails render.

Changing this setting will not affect any of your existing email messages or templates. You can override this default at any time while composing messages or templates. For more information, refer to [CSS inlining][10].

## Resubscribe users when their email changes

You may automatically resubscribe users when they change their email address. For example, if a previously unsubscribed workspace user changes their email address to one that is not on the unsubscribe list for Braze, they will automatically become resubscribed.

![]({% image_buster /assets/img/email_settings/resubscribe_users.png %}){: style="max-width:90%;" }

## Subscription pages and footers

{% tabs local %}
{% tab Custom Footer %}

For commercial emails, the [CAN-SPAM Act](https://en.wikipedia.org/wiki/CAN-SPAM_Act_of_2003) requires that all commercial emails include an unsubscribe option. With the custom footer settings, you are able to remain CAN-SPAM compliant while also customizing your email opt-out footer. In order to remain compliant, you must add your custom footer to all emails sent as part of campaigns for this workspace.

Note the following requirements when creating a custom footer for your email messaging:
- Must include an unsubscribe URL and physical mailing address.
- Should be less than 100 KB.

![]({% image_buster /assets/img/email_settings/custom_footer.png %})

To learn more about custom footer Liquid templating, check out our documentation on [Custom footers]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#changing-email-subscriptions).

{% endtab %}
{% tab Custom Unsubscribe Page %}

Braze lets you set a **Custom Unsubscribe Page** with your own HTML. This page will appear after a user has selected to unsubscribe from the bottom of an email. Note that this page should be less than 750 KB. 

![]({% image_buster /assets/img/email_settings/custom_unsubscribe.png %})

Learn more about best practices for email list management in [Managing email subscriptions]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/managing_email_subscriptions/#unsubscribed-email-addresses).

{% endtab %}
{% tab Custom Opt-In Page %}

You can create a custom opt-in page using your own HTML. Including this in your email can be especially beneficial if you want your branding and message to remain consistent throughout your user lifecycle. Note that this page should be less than 750 KB. 

![]({% image_buster /assets/img/email_settings/custom_opt_in.png %})

Learn more about best practices for email list management in [Managing email subscriptions]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/managing_email_subscriptions/#unsubscribed-email-addresses).

{% endtab %}
{% endtabs %}

[0]: {% image_buster /assets/img_archive/list_unsub_img1.png %}
[1]: {% image_buster /assets/img/email_settings/outbound_email.png %}
[2]: {% image_buster /assets/img/email_settings/switch.gif %}
[6]: https://learning.braze.com/email-open-tracking-pixel
[7]: {{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/managing_email_subscriptions/#unsubscribed-email-addresses
[8]: {{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/
[10]: {{site.baseurl}}/user_guide/message_building_by_channel/email/css_inline/
[13]: {% image_buster /assets/img/open_pixel.png %}
