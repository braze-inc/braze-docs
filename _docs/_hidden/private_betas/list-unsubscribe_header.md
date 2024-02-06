---
nav_title: List-Unsubscribe Header
article_title: List-Unsubscribe Header
permalink: /list-unsubscribe/
hidden: true
---

## List-unsubscribe header

Using a list-unsubscribe header allows your recipients to unsubscribe easily from marketing emails by displaying an **Unsubscribe** button within the mailbox UI, and is not a part of the message body itself.

![]({% image_buster /assets/img_archive/list_unsub_img1.png %}){: style="float:right;max-width:60%;margin-left:15px;"}

When a recipient clicks **Unsubscribe**, the mailbox provider sends the unsubscribe request to the destination defined in the email header.

Enabling list-unsubscribe is a deliverability best practice and a requirement at some of the premier mailbox providers. It encourages end users to safely remove themselves from unwanted messages versus hitting the spam button in an email client, the latter of which is detrimental to sending reputation and email deliverability.

### How it works

![]({% image_buster /assets/img/email_settings/target_audiences_example.png %}){: style="float:right;max-width:60%;margin-left:15px;"}

When turned on, this feature is applied to the entire workspace, not the company-level. It's added to campaigns and Canvases that are set up to send to users who are subscribed or opted-in, or opted-in users only in the **Target Audiences** step of the campaign and Canvas builders.

Braze doesn't add the header for what is considered transactional, so if a message is set to send to all users including unsubscribed users, the list-unsubscribe header will not be attached to the message. Additionally, header is not added for messages delivered via test send since the list-unsubscribe header is only generated and added for targeting user profiles in Braze.

### Default list-unsubscribe header

{% alert note %}
Gmail intends for senders to implement the one-click unsubscribe for all their outgoing commercial, promotional messages as of June 1, 2024. For more information see [Gmail’s sender guidelines](https://support.google.com/mail/answer/81126?hl=en#subscriptions&zippy=%2Crequirements-for-sending-or-more-messages-per-day:~:text=Make%20it%20easy%20to%20unsubscribe) and [Gmail’s Email Sender Guidelines FAQ](https://support.google.com/a/answer/14229414#zippy=%2Cwhat-time-range-or-duration-is-used-when-calculating-spam-rate%2Cif-the-list-header-is-missing-is-the-message-body-checked-for-a-one-click-unsubscribe-link%2Cif-unsubscribe-links-are-temporarily-unavailable-due-to-maintenance-or-other-reasons-are-messages-flagged-as-spam%2Ccan-a-one-click-unsubscribe-link-to-a-landing-or-preferences-page%2Cwhat-is-a-bulk-sender%2Chow-can-bulk-senders-make-sure-theyre-meeting-the-sender-guidelines%2Cdo-the-sender-guidelines-apply-to-messages-sent-to-google-workspace-accounts%2Cdo-the-sender-guidelines-apply-to-messages-sent-from-google-workspace-accounts%2Cwhat-happens-if-senders-dont-meet-the-requirements-in-the-sender-guidelines%2Cif-messages-are-rejected-because-they-dont-meet-the-sender-guidelines-do-you-send-an-error-message-or-other-alert%2Cwhat-happens-when-sender-spam-rate-exceeds-the-maximum-spam-rate-allowed-by-the-guidelines%2Cwhat-is-the-dmarc-alignment-requirement-for-bulk-senders%2Cif-messages-fail-dmarc-authentication-can-they-be-delivered-using-ip-allow-lists-or-spam-bypass-lists-or-will-these-messages-be-quarantined%2Ccan-bulk-senders-get-technical-support-for-email-delivery-issues%2Cdo-all-messages-require-one-click-unsubscribe:~:text=for%20mitigations.-,Unsubscribe%20links,-Do%20all%20messages). Yahoo announced an early 2024 timeline for the updating requirements. For more information refer to [More Secure, Less Spam: Enforcing Email Standards for a Better Experience](https://blog.postmaster.yahooinc.com/).
{% endalert %}

If you use Braze’s unsubscribe functionality to process unsubscribes on your behalf directly, you can toggle on the Email Unsubscribe Header and save the “Braze default” as the setting. Braze will generate the one-click unsubscribe and mailto header to be added to your promotional emails. Using one-click unsubscribe for the list-unsubscribe header ([RFC 8058](https://datatracker.ietf.org/doc/html/rfc8058)) focuses on providing an easy way for recipients to opt-out from emails, and is a requirement from Yahoo and Gmail for bulk senders. 

When Braze receives a list-unsubscribe request from a user, this user's global email subscription state is set to unsubscribed. If there isn't a match, Braze will not process this request.

![Option to automatically include a list-unsubscribe header for emails sent to subscribed or opted-in users.]({% image_buster /assets/img/email_settings/email_unsubscribe_header.png %}){: style="max-width:80%;"}

### Customizing the list-unsubscribe header

#### Requirements

If you're sending emails using your own custom unsubscribe functionality, you must meet the following requirements to make sure the one-click unsubscribe URL that you set up is in accordance with RFC 8058.

* The URL must be able to handle unsubscribe POST requests
* The URL must be HTTPS
* The URL must not return an HTTPS redirect. One-click unsubscribe links that go to a landing or other type of web page don't comply with RFC 8058
* The message must have a valid DKIM signature

Select **Custom list-unsubscribe header** to add your own configured one-click unsubscribe endpoint, and optionally "mailto:". Braze requires an input for URL to support a custom list-unsubscribe header since the one-click unsubscribe HTTP is a requirement from Yahoo/Gmail for bulk senders.

![]({% image_buster /assets/img/email_settings/email_unsubscribe_header_custom.png %}){: style="max-width:80%;"}