---
page_order: 10.9
nav_title: Troubleshooting
article_title: Troubleshoot push notifications for the Braze SDK
channel:
  - push notifications
---

# Troubleshoot push notifications

> Learn how to troubleshoot push notifications for the Braze SDK.

{% sdktabs %}
{% sdktab web %}
{% multi_lang_include developer_guide/web/push_notifications/troubleshooting.md %}
{% endsdktab %}

{% sdktab android %}
{% multi_lang_include developer_guide/android/push_notifications/troubleshooting.md %}
{% endsdktab %}

{% sdktab swift %}
{% multi_lang_include developer_guide/swift/push_notifications/troubleshooting.md %}
{% endsdktab %}

{% sdktab fireos %}
{% multi_lang_include developer_guide/android/push_notifications/troubleshooting.md %}
{% endsdktab %}

{% sdktab .NET MAUI (Xamarin) %}
{% multi_lang_include developer_guide/xamarin/push_notifications/troubleshooting.md %}
{% endsdktab %}
{% endsdktabs %}

## Deeplinking is not working when the app is still running in the background on iO (BD-4624)

Add a section to the Swift push troubleshooting guide under "Deep links not working". Include the content from the article: Deeplinks from push clicks opening the app's home page instead of the desired destination, when the app is backgrounded Check to see if you're using any third-party libraries that use the method swizzling. If this is the case, we suggest turning the method off as this can cause issues with Braze methods.


## Slow push sending quick-fixes (BD-4654)

I feel as though the entire KA can be transferred to the docs

