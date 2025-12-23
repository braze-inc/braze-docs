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

Users will be prevented from entering the Canvas and no further messages will be sent out. For email campaigns and Canvases, the stop button does not mean that send will immediately stop. This is because when the send requests are sent out, they cannot be stopped from being delivered to the user.

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

### Can I add a "view this email in a browser" link to my emails?

No, Braze does not offer this functionality. This is because an increasing majority of email is opened on mobile devices and modern email clients, which render images and content without any problems.

**Workaround:** To achieve this same result, you can host the content of your email on an external landing page (such as your website), which can then be linked to from the email campaign you are building using the **Link** tool when editing the email body.

