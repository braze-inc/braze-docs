---
page_order: 1
nav_title: Deep linking
article_title: Deep linking in push notifications for the Braze SDK
channel:
  - push notifications
---

# Deep linking in push notifications

> Learn how to set up silent push notifications for the Braze SDK.

{% sdktabs %}
{% sdktab android %}
{% multi_lang_include developer_guide/android/_global/deep_linking.md%}
{% endsdktab %}

{% sdktab swift %}
{% multi_lang_include developer_guide/swift/deep_linking.md%}
{% endsdktab %}

{% sdktab flutter %}
{% multi_lang_include developer_guide/flutter/deep_linking.md%}
{% endsdktab %}
{% endsdktabs %}

## Troubleshooting deep links in wrapper SDKs

If deep links from push notifications are not working in a wrapper SDK (such as React Native, Flutter, or Cordova), check the following:

1. **SDK version compatibility:** Compare your Braze SDK version with the [SDK changelog]({{site.baseurl}}/developer_guide/changelogs/) to confirm that your wrapper SDK version supports the version of React Native (or other framework) you're running. Incompatible versions can cause deep link handlers to fail silently.
2. **Native-layer configuration:** Wrapper SDKs rely on the underlying native iOS and Android SDKs for deep link handling. Verify that your native-layer deep link setup (Universal Links / App Links, URL scheme registration) is configured correctly. Refer to the platform-specific tabs above.
3. **Upgrade path:** If upgrading the SDK doesn't resolve the issue, open a [support ticket]({{site.baseurl}}/braze_support/) with your SDK version, framework version, and a description of the expected vs. actual behavior.
