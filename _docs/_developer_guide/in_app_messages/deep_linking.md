---
page_order: 1
nav_title: Deep linking
article_title: In-app message deep-linking for the Braze SDK
channel:
  - push notifications
---

# In-app message deep-linking

> Learn how to deep link within an in-app message for the Braze SDK.

{% sdktabs %}
{% sdktab android %}
{% multi_lang_include developer_guide/android/_global/deep_linking.md%}
{% endsdktab %}

{% sdktab swift %}
{% multi_lang_include developer_guide/swift/deep_linking.md%}
{% endsdktab %}
{% endsdktabs %}

### UTM tag calculations

Braze reports _Total Clicks_ for all links in a campaign or Canvas step, which can include links that don't have UTM tags. This means you may see a different (often lower) result in your Google Analytics campaign tracking links compared to the _Total Clicks_ displayed in your campaign performance or Report Builder.
