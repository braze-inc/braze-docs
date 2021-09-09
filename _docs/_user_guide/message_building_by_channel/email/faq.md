---
nav_title: FAQs
article_title: Email FAQs
page_order: 25
description: "This page provides answers to frequently asked questions about Email messaging."
channel: email

---

# Email FAQs

### Can I add a "view this email in a browser" link to my emails?

No, Braze does not offer this functionality. This is because an increasing majority of email is opened on mobile devices and modern email clients, which render images and content without any problems.

**Workaround:** To achieve this same result, you can host the content of your email on an external landing page (such as your website), which can then be linked to from the email campaign you are building using the **Link** tool when editing the email body.

### What happens when an email is sent out and multiple profiles have the same email address?

If multiple users with matching emails are all in-segment to receive a campaign, a random user profile with that email address is chosen at the time of send. This way the email is only sent once and is deduplicated, which ensures that it doesn’t hit the same email multiple times.

Note that this deduplication occurs if the users targeted are included in the same dispatch. Therefore triggered campaigns may result in multiple sends to the same email address (even within a time period where users could be excluded due to reeligibility) if differing users with matching emails log the trigger event at different times. Users are not deduped by email on Canvas entry, so it’s possible that users are not deduped beyond the first step of a Canvas if they are progressing at slightly different times due to rate limited entry.

When a user tied to a given email address opens or clicks an email, all user profiles which share that email address are marked as opening and clicking the campaign. You can identify targeted users from the user profile download within **User Search**. The user who actually received the email will have a timestamp set for the “received_email” field in the associated campaign summary; other users won’t have this field, just “date”.

**Exception: API-Triggered Campaigns**

API-triggered campaigns will dedupe or send dupes depending on where the audience is defined. In short, the duplicate emails must be directly targeted as separate `User_ids` within the call in order to receive multiple details. Here are three possible scenarios for API-triggered campaigns:

- **Scenario 1: Duplicate emails in target segment (DEDUPED):** If the same email appears in multiple user profiles that are grouped together in dashboard’s audience filters for an API-triggered campaign, only one of the profiles will get the email.
- **Scenario 2: Duplicate emails in different user_ids within recipients object (DUPE SENDS):** If the same email appears within multiple `External_user_IDs` referenced by the “recipients” object, the email will be sent twice.
- **Scenario 3: Duplicate emails due to duplicate user_ids within recipients object (DEDUPED):** If you try to add the same user profile twice, only one of the profiles will get the email.

### What is a "good" email deliverability rate?

Typically, the “magic number” is around 95% messages delivered, with a bounce rate no higher than 3%. If your deliverability dips below that, there is usually cause for concern.

However, a rate can be above 95% and still have deliverability issues. For example, if all of your bounces are coming from one particular domain, that is a clear signal that there is a reputation issue with that provider.

Additionally, messages may be getting delivered and ending up in Spam, indicating potentially serious reputation issues. It’s important to monitor not just the number of messages being delivered, but also open and click rates to determine whether users are actually seeing the messages in their inboxes. Because providers usually don’t report every spam instance, a spam rate of even 1% could be cause for concern and further analysis.

Finally, your business and the types of emails you send may also affect deliverability. For example, someone sending mostly transactional emails should expect to see a better rate than someone sending many marketing messages.
