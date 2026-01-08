---
nav_title: Log message data
article_title: Log push notification data through the Braze SDK
page_order: 7.2
description: "Learn how to log push notification data through the Braze SDK when using custom notification handling."
noindex: true
---

# Log push notification data

> Learn how to log push notification data when implementing custom push notification handling.

{% alert important %}
This page is only relevant if you're implementing custom push notification handling and bypassing the Braze SDK's default push notification processing. Most users do not need this information—the Braze SDK automatically handles push notification analytics when you follow the standard integration guide.
{% endalert %}

If you're using the Braze SDK's default push notification handling, analytics (opens, receives, dismisses) are logged automatically. You only need the instructions on this page if you've implemented custom notification handling logic that bypasses Braze's automatic processing.

{% sdktabs %}
{% sdktab android %}
{% multi_lang_include developer_guide/android/analytics/logging_push_data.md %}
{% endsdktab %}

{% sdktab swift %}
{% multi_lang_include developer_guide/swift/analytics/logging_push_data.md %}
{% endsdktab %}
{% endsdktabs %}
