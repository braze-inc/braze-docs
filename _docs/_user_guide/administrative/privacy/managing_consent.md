---
nav_title: Managing consent
article_title: Managing Consent
page_order: 10
page_type: reference
description: "This reference article provides tips on how to manage consent using Braze."
---

# Managing consent

> This reference articles provides tips on how to manage consent from your users using Braze.

Braze cannot provide specific advice on interpreting laws and regulations or offer guidance on handling consent management, as this will depend on your legal team's interpretation of the law. However, we offer a range of tools to support subscription and consent management.

Your approach should depend on the strictness required by your legal team based on their interpretation of the law. Here are some options to consider, listed from most strict to least strict:

- **Teams:** Use [Braze teams]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) for true governance. This involves adding a custom attribute to all user profiles to indicate their consent status, consent date, or both. You must then migrate all campaigns and Canvases to the designated team and adjust user permissions on the dashboard accordingly.
- **User profile attribute:** Add a consent attribute to all user profiles. This attribute will indicate whether a user has given consent or not. In the future, you can then include a segment of users who have consented (for example, `consent = true`) to all your campaigns and Canvases.
- **Channel-specific subscription groups:** Manipulate subscription groups for specific channels (push notifications, email, etc.) to manage consent. Initially, mark users as unsubscribed from these channels and only mark them as subscribed after they have consented.

{% alert important %}
Consult your legal team to determine the appropriate approach for your organization's compliance with consent management requirements.
{% endalert %}

