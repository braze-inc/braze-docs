---
nav_title: FAQ
article_title: Email FAQ
page_order: 15
description: "This page provides answers to frequently asked questions about email messaging."
channel: email

---

# Frequently asked questions

> This article provides answers to some frequently asked questions about emails.

### What happens when an email is sent out and multiple profiles have the same email address?

If multiple users with matching emails are all in a segment to receive a campaign, a random user profile with that email address is chosen at the time of send. This way the email is only sent once and is deduplicated, ensuring that the email doesn't hit the same email address multiple times.

There are three scenarios that can make it seem like a user received an email twice:

- **An error occurred during campaign or Canvas creation:** The user may not receive the literal same send twice, but may receive two separate emails with the same subject line. When a campaign or Canvas is duplicated, check email configuration details such as images or subject lines. You can also refer to changelogs to see if the campaign or Canvas was modified after launch—a duplicate may share the same subject line as the original when the user received it.
- **Multiple user profiles have email forwarding:** If a user has multiple accounts in a given app but one account forwards mail, the user receives the campaign once per inbox; mail can appear twice in the inbox where messages are forwarded. Only some providers indicate when an email was forwarded from another account.
- **Email configuration at the recipient:** Some clients merge inboxes ("universal inbox"). If the same campaign targets multiple accounts that share one inbox, it can look like one person got the campaign twice when two distinct profiles were actually messaged. The recipient can confirm whether multiple accounts are combined in one inbox.

Note that this deduplication occurs if the users targeted are included in the same dispatch. Triggered campaigns may result in multiple sends to the same email address (even within a time period where users could be excluded due to re-eligibility) if differing users with matching email addresses log the trigger event at different times. Users are not deduped by email on Canvas entry, so it's possible that users are not deduped beyond the first step of a Canvas if they are progressing at slightly different times due to rate limited entry. When a user tied to a given email address opens or clicks an email, all user profiles that share the email address are marked as opening and clicking the campaign.

#### Exception: API-triggered campaigns

API-triggered campaigns will deduplicate or send deduplicates depending on where the audience is defined. In short, the duplicate emails must be directly targeted as separate `user_ids` within the API call in order to receive multiple details. Here are three possible scenarios for API-triggered campaigns:

- **Scenario 1: Duplicate emails in target segment:** If the same email appears in multiple user profiles that are grouped together in dashboard's audience filters for an API-triggered campaign, only one of the profiles will receive the email.
- **Scenario 2: Duplicate emails in different `user_ids` within recipients object:** If the same email appears within multiple `External_user_IDs` referenced by the `recipients`` object, the email will be sent twice.
- **Scenario 3: Duplicate emails due to duplicate user_ids within recipients object:** If you try to add the same user profile twice, only one of the profiles will get the email.

### Will updates to my outbound email settings apply retroactively?

No. Updates made to the outbound email settings do not retroactively affect existing sends. For example, changing your default display name in the email settings will not automatically replace the existing default display name in your active campaigns or Canvases. 

### What is a "good" email delivery rate?

Typically, the "magic number" is around 98% of messages delivered with a bounce rate no higher than 3%. If your delivery dips below that, there is usually cause for concern.

However, a rate can be higher than 98% and still have deliverability issues. For example, if all of your bounces are coming from one particular domain, that is a clear signal that there is a reputation issue with that provider.

Additionally, messages may be getting delivered and ending up in Spam, indicating potentially serious reputation issues. It's important to monitor not just the number of messages being delivered, but also open and click rates to determine whether users are actually seeing the messages in their inboxes. Because providers usually don't report every spam instance, a spam rate of even 1% could be cause for concern and further analysis.

Finally, your business and the types of emails you send may also affect delivery. For example, someone sending mostly [transactional emails]({{site.baseurl}}/api/api_campaigns/transactional_api_campaign) should expect to see a better rate than someone sending many marketing messages.

### Why are my email delivery metrics not adding up to 100%?

Email delivery metrics (deliveries, bounces, and spam rate) may not add up to 100% because of emails that are soft bounced and then not delivered after the retry period of up to 72 hours.

Soft bounces are emails that bounce due to a temporary or transient issue such as "mailbox full," "server temporarily not available," and more. If a soft bounced email is still not delivered after 72 hours, this email will not be accounted for in the campaign delivery metrics.

### What are open tracking pixels?

[Open tracking pixels]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/#changing-location-of-tracking-pixel) leverage a sender's email click tracking domain to track email open events. The pixel is an image tag appended to the email's HTML. It is most commonly the last HTML element within the body tag. When a user loads their email, a request is made to populate the image from the branded tracking domain, which logs an open event.

### What happens when an email campaign or Canvas is stopped?

Users will be prevented from entering the Canvas and no further messages will be sent out. For email campaigns and Canvases, the stop button does not mean that send will immediately stop. After a request is sent to the ESP (SparkPost or SendGrid), it will be processed and delivered even if the campaign or Canvas has been stopped.

While Braze won't send further requests once the campaign or Canvas is stopped, analytics may still increase while the ESP finishes processing requests already in flight.

### Why am I seeing more email clicks than opens?

You may be seeing more clicks than opens for any of the following reasons:
- Users are performing multiple clicks on the body of the email within a single open.
- Users click on some email links within the preview pane of their phones. In this case, Braze logs this email as being clicked but not opened.
- Users reopen an email that they previewed earlier.

### Why am I seeing zero email opens and clicks?

You may be seeing zero email opens and clicks if there's a misconfiguration with your tracking domain. This can be due to any of the following reasons:
- There is an SSL issue where tracking URLs are `http` instead of `https`.
- There is an issue with your CDN where the user agent string on the open events, click events, or both aren't populating.

### What are the potential risks of triggering server clicks?

Certain elements of an email message, such as overly long messages or too many exclamation marks, have the potential to trigger email security responses. These responses can impact reporting, IP reputation, and can result in users unsubscribing. 

For best practices on how to handle these responses, refer to [Handling increases in click rates]({{site.baseurl}}/help/help_articles/email/open_rates/).

### Can Braze track unsubscribe links counted toward the "Unsubscribe" metric?

Braze tracks unsubscribe links if the following Liquid is used within emails: {%raw%}`${set_user_to_unsubscribed_url}`{%endraw%}

### Why am I seeing a different number of unsubscribes than clicks on my unsubscribe link?

If there are more _Unsubscribes_ than users who clicked the unsubscribe link in the email body, list-unsubscribe header actions often explain the gap—a click on the list-unsubscribe header counts as an _Unsubscribe_ but not as a _Click_ on the body link.

If the total number of clicks on the body unsubscribe link is greater than the number of _Unsubscribes_, users may have clicked the link more than once.

### Can I add a "view this email in a browser" link to my emails?

No, Braze does not offer this functionality. This is because an increasing majority of email is opened on mobile devices and modern email clients, which render images and content without any problems.

**Workaround:** To achieve this same result, you can host the content of your email on an external landing page (such as your website), which can then be linked to from the email campaign you are building using the **Link** tool when editing the email body.

### Why are my users being auto-unsubscribed by email security software?

Some corporate email security tools (such as Barracuda, Proofpoint, and similar services) pre-fetch or scan all URLs in incoming emails, including unsubscribe links. This can cause unintended unsubscribes when the security tool follows the one-click list-unsubscribe link.

To mitigate this:

- **Recommend recipients allowlist your sending domain:** Work with the affected recipients' IT teams to add your sending domain and Braze tracking domains to their email security allow list.
- **Use a preference center:** Instead of a direct unsubscribe link, use a [preference center]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center/overview/) that requires user interaction to confirm the unsubscribe action. Security scanners typically won't complete multi-step forms.
- **Review unsubscribe logs:** Check the `User-Agent` header and IP address in your Currents unsubscribe event data to identify patterns consistent with automated scanning (such as consistent `User-Agent` headers across multiple unsubscribes).

For more details on how server-side scanning can affect email metrics, refer to [Handling increases in click rates]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting/#handling-increases-in-click-rates).

### Why has my machine open rate changed unexpectedly?

[Machine opens]({{site.baseurl}}/user_guide/analytics/reporting/report_metrics/#machine-opens) are triggered by email security features such as Apple Mail Privacy Protection (MPP), which pre-loads email content (including the tracking pixel) without the user physically opening the email. Machine open rates can fluctuate based on:

- Changes in the proportion of your audience using Apple Mail or other privacy-enabled email clients.
- Updates to email provider privacy features or bot detection behaviors.
- Changes in your audience segmentation or targeting.

Machine open percentages are not a reliable measure of actual engagement. For a more accurate view of email performance, focus on *Other Opens* (non-machine opens) and *Unique Clicks*. You can also compare these metrics over time using the [Email Performance Dashboard]({{site.baseurl}}/user_guide/analytics/dashboard/email_performance_dashboard/).

### Does the *Unique Opens* metric include machine opens?

No. *Unique Opens* count only [Other Opens]({{site.baseurl}}/user_guide/analytics/reporting/report_metrics/#other-opens), which excludes emails identified as machine opens. *Machine Opens* are tracked separately. In the **Campaign Analytics** view and **Report Builder**, you can view both metrics independently.

### Why does my email delivery volume not match my send volume?

After an email is sent, the recipient's inbox decides when it is delivered. Messages can be deferred for hours or days because of a full mailbox, ESP throttling from a given IP, and similar reasons.

When deferred messages are delivered on a different calendar day than the send day, _Deliveries_ can exceed _Sends_ for the same date range. When many deferrals land on one day, _Sends_ can exceed _Deliveries_ for that range.

### Why am I seeing a warning to include an unsubscribe link when my email already has one?

This warning can persist for campaigns duplicated from a campaign that did not have an unsubscribe link. To clear it:

- For HTML emails, go to the **Plaintext** tab, then select **Regenerate from HTML**.
- After duplicating, duplicate the variant, then remove the original variant. **Do not** select the original variant, or the warning can carry over.

### What are reasons why my user hasn't received an email campaign?

- The message may be in Spam—ask the user to check.
- They weren't eligible to receive email.
- The address is invalid or doesn't exist.
- They may have missed or deleted the message.

### How can I optimize images in Outlook?

Outlook often uses Microsoft Word–style rendering, which can add a border around images. You can wrap content so it hides in Office clients using standard conditional comments, for example:

```html
<!--[if !mso]><!-- -->
<span>Content hidden in Outlook desktop</span>
<!--<![endif]-->
```

### Can I use SVG or WEBP images in my email messages?

SVG images won't render in Gmail web or Gmail iOS. WEBP is not consistently supported across clients.

Use widely supported formats such as PNG or JPEG so images render reliably.

### Can Liquid variables assigned in one part of the message composer be used in another?

No. Each part of the email (subject, body, headers, buttons, and so on) is generated separately, so Liquid assigned in one field is not available in another. Assign variables in each field that needs them.

### My email template is missing. Where is it?

Go to **Templates** > **Email Templates**. You can filter by type (HTML or drag-and-drop).

Confirm you have permission to view templates—see [User permissions]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/).

