---
nav_title: FAQ
article_title: Email FAQ
page_order: 12
description: "This page provides answers to frequently asked questions about Email messaging."
channel: email

---

# Frequently asked questions

> This article provides answers to some frequently asked questions about emails.

### Can I add a "view this email in a browser" link to my emails?

No, Braze does not offer this functionality. This is because an increasing majority of email is opened on mobile devices and modern email clients, which render images and content without any problems.

**Workaround:** To achieve this same result, you can host the content of your email on an external landing page (such as your website), which can then be linked to from the email campaign you are building using the **Link** tool when editing the email body.

### What happens when an email is sent out and multiple profiles have the same email address?

If multiple users with matching emails are all in-segment to receive a campaign, a random user profile with that email address is chosen at the time of send. This way the email is only sent once and is deduplicated, which ensures that it doesn't hit the same email multiple times.

Note that this deduplication occurs if the users targeted are included in the same dispatch. Therefore, triggered campaigns may result in multiple sends to the same email address (even within a time period where users could be excluded due to reeligibility) if differing users with matching emails log the trigger event at different times. Users are not deduped by email on Canvas entry, so it's possible that users are not deduped beyond the first step of a Canvas if they are progressing at slightly different times due to rate limited entry. When a user tied to a given email address opens or clicks an email, all user profiles which share that email address are marked as opening and clicking the campaign.

#### Exception: API-triggered campaigns

API-triggered campaigns will dedupe or send dupes depending on where the audience is defined. In short, the duplicate emails must be directly targeted as separate `user_ids` within the call in order to receive multiple details. Here are three possible scenarios for API-triggered campaigns:

- **Scenario 1: Duplicate emails in target segment:** If the same email appears in multiple user profiles that are grouped together in dashboard's audience filters for an API-triggered campaign, only one of the profiles will get the email.
- **Scenario 2: Duplicate emails in different `user_ids` within recipients object:** If the same email appears within multiple `External_user_IDs` referenced by the "recipients" object, the email will be sent twice.
- **Scenario 3: Duplicate emails due to duplicate user_ids within recipients object:** If you try to add the same user profile twice, only one of the profiles will get the email.

### What is a "good" email deliverability rate?

Typically, the "magic number" is around 95% messages delivered with a bounce rate no higher than 3%. If your deliverability dips below that, there is usually cause for concern.

However, a rate can be higher than 95% and still have deliverability issues. For example, if all of your bounces are coming from one particular domain, that is a clear signal that there is a reputation issue with that provider.

Additionally, messages may be getting delivered and ending up in Spam, indicating potentially serious reputation issues. It's important to monitor not just the number of messages being delivered, but also open and click rates to determine whether users are actually seeing the messages in their inboxes. Because providers usually don't report every spam instance, a spam rate of even 1% could be cause for concern and further analysis.

Finally, your business and the types of emails you send may also affect deliverability. For example, someone sending mostly [transactional emails][1] should expect to see a better rate than someone sending many marketing messages.

### Why are my email deliverability metrics not adding up to 100%?

Email deliverability metrics (deliveries, bounces, and spam rate) may not add up to 100% because of emails that are soft bounced and then not delivered after the retry period of up to 72 hours.

Soft bounces are emails that bounce due to a temporary or transient issue such as "mailbox full", "server temporarily not available", and more. If the soft bounced email is still not delivered after 72 hours, this email will not be accounted for in the campaign deliverability metrics.

### Can Braze track unsubscribe links counted towards the "Unsubscribe" metric

Braze does not offer this functionality as unsubscribe links are custom and clicks to an unsubscribe link does not guarantee an unsubscribe actually occurred. 

**Workaround:** To achieve this same result, you could send an API call to Braze to update any user profiles where you recorded unsubscribes from your custom link. 

### What are open tracking pixels?

Open [tracking pixels]({{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/email_settings/#email-open-tracking-pixel) leverage a sender's email click tracking domain to track email open events. The pixel is an image tag appended to the email's HTML. It is most commonly the last HTML element within the body tag. When a user loads up their email, a request is made to populate the image from the branded tracking domain, which logs an open event.

### How can I update user's email subscription groups?

- **Rest API:** User profiles can be programmatically set by the [`/subscription/status/set` endpoint]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/) by using Braze's REST API.

### How can I check a user's email subscription group?

- **User Profile:** Individual user profiles can be accessed through the Braze dashboard by selecting **User Search** from the sidebar. Here, you can look up user profiles by email address, phone number, or external user ID. Once in a user profile, under the Engagement tab, you can view a user's email subscription groups.

{% alert note %}
If you are using our [updated navigation]({{site.baseurl}}/navigation), **User Search** is now **Search Users** and can be found under **Audience**.
{% endalert %}

- **Rest API:** Individual user profiles subscription group can be viewed by the [List user’s subscription groups endpoint][9] or [List user’s subscription group status endpoint][8] by using Braze's REST API. 

### What happens when an email campaign or Canvas is stopped?

Users will be prevented from entering the Canvas and no further messages will be sent out. For email campaigns and Canvases, the stop button does not mean that send will immediately stop. This is because once the send requests are sent out, they cannot be stopped from being delivered to the user.

### Why am I seeing more email clicks than opens?

You may be seeing more clicks than opens for any of the following reasons:
- Users are performing multiple clicks on the body of the email within a single open.
- Users click on some email links within the preview pane of their phones. In this case, Braze logs this email as being clicked but not opened.
- Users reopen an email that they previewed earlier.

[8]: {{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/
[9]: {{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups/
[1]: {{site.baseurl}}/api/api_campaigns/transactional_api_campaign