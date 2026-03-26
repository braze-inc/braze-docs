---
nav_title: Link shortening
article_title: Link shortening
page_order: 1
description: "This reference article covers how to turn on link shortening in your SMS messages and some frequently asked questions."
page_type: reference
alias: "/link_shortening/"
tool:
  - Campaigns
channel:
  - SMS
  - MMS
  - RCS
---

# Link shortening

> This page covers how to turn on link shortening in your SMS and RCS messages, test shortened links, use your custom domain in shortened links, and more.

{% alert important %}
Braze is gradually rolling out [unified link shortening]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/link_shortening/?sdktab=unified), which consolidates all SMS and RCS shortened links into a single personalized link format (for example, `brz.ai/abcdefgh`).
{% endalert %}

{% sdktabs %}
{% sdktab Legacy %}

{% multi_lang_include link_shortening_temp/legacy_link_shortening.md %}

{% endsdktab %}
{% sdktab Unified %}

{% multi_lang_include link_shortening_temp/unified_link_shortening.md %}

{% endsdktab %}
{% endsdktabs %}
