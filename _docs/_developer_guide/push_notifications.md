---
nav_title: Push notifications
article_title: "Push notifications for the Braze SDK"
page_order: 2.3
description: "This landing page is home to all things push notifications."
---

# Push notifications

> [Push notifications]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/) allow you to send out notifications from your app when important events occur. You might send a push notification when you have new instant messages to deliver, breaking news alerts to send, or the latest episode of your user's favorite TV show ready for them to download for offline viewing. They are also more efficient than background fetch, as your application only launches when necessary.

If you set **Redirect to Web URL** with **Open Web URL Inside App** unchecked but the link still opens inside the app, the app may be handling the URL (for example, via universal links on iOS or App Links on Android). To open the link in the browser instead, ensure your app delegates the URL to the system browser when the user taps the notification, or adjust your app's URL handling so that the click action matches the Braze dashboard setting. See your platform's push documentation for how click actions and URL handling are configured.

{% sdktabs %}
{% sdktab web %}
{% multi_lang_include developer_guide/web/push_notifications.md %}
{% endsdktab %}

{% sdktab android %}
{% multi_lang_include developer_guide/android/push_notifications.md %}
{% endsdktab %}

{% sdktab swift %}
{% multi_lang_include developer_guide/swift/push_notifications.md %}
{% endsdktab %}

{% sdktab android tv %}
{% multi_lang_include developer_guide/android_tv/push_notifications.md %}
{% endsdktab %}

{% sdktab cordova %}
{% multi_lang_include developer_guide/cordova/push_notifications.md %}
{% endsdktab %}

{% sdktab flutter %}
{% multi_lang_include developer_guide/flutter/push_notifications.md %}
{% endsdktab %}

{% sdktab huawei %}
{% multi_lang_include developer_guide/huawei/push_notifications.md %}
{% endsdktab %}

{% sdktab react native %}
{% multi_lang_include developer_guide/react_native/push_notifications.md %}
{% endsdktab %}

{% sdktab safari %}
{% multi_lang_include developer_guide/safari/push_notifications.md %}
{% endsdktab %}

{% sdktab unity %}
{% multi_lang_include developer_guide/unity/push_notifications.md %}
{% endsdktab %}

{% sdktab .NET MAUI (Xamarin)%}
{% multi_lang_include developer_guide/xamarin/push_notifications.md %}
{% endsdktab %}
{% endsdktabs %}
