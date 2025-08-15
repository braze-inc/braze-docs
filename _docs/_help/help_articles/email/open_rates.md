---
nav_title: Handling increases in click rates
article_title: Handling Increases in Click Rates
page_order: 1

page_type: solution
description: "This help article walks you through how to handle increases in your email click rates."
channel: email
---

# Handling increases in click rates

Open rates can be an insightful metric to track for your email campaigns. However, these open rates aren't necessarily accurate indicators of human engagement with email campaigns. An open event, by definition, occurs when a user opens an email, meaning a transparent open tracking pixel was successfully downloaded. 

Additionally, use of security scanning tools can inflate open rates. Some of these tools protect their users by scanning incoming emails for malicious content by clicking links to verify their legitimacy. These clicks are often referred to as "bot clicks" or "non-human interaction" (NHI). 

Ultimately, after an email has left our servers, we have limited visibility into what happens next, but here are our recommendations for managing NHI affecting your results:

1. Be aware that this can happen to any sender and nearly any recipient. Clicks, like opens, are not entirely reliable indicators of human interaction with your messages, meaning NHI is not preventable.
2. Because higher positive engagement tends to correlate with lower NHI, it's important to follow email messaging [best practices]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices). This includes getting explicit permission from your users to send email and sunsetting unengaged subscribers on a regular cadence. 
3. Use HTTPS links in your emails when possible. NHI is less common for senders using secure links.
4. If you currently use a single-click unsubscribe process, consider creating a [preference center]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center/overview) that takes users to a page to edit and manage their notification preferences. This can be helpful because NHI can inadvertently unsubscribe users.
5. Consider using [other metrics]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting/#email-performance) to measure your email marketing success, such as conversions, app sessions, or site visits.
6. Add a hidden link in your email campaigns. This link would be something that a human wouldn't notice like white-on-white text or a punctuation mark. Since bots tend to click all links, you can conclude that users generating click events on the invisible link are actually the result of NHI, so the open or click doesn't necessarily indicate positive engagement.