---
nav_title: Link-Verkürzung
article_title: Link-Verkürzung
page_order: 3
description: "In diesem Referenzartikel erfahren Sie, wie Sie die Linkverkürzung in Ihren SMS-Nachrichten aktivieren können und welche Fragen häufig gestellt werden."
page_type: reference
alias: "/link_shortening/"
tool:
  - Campaigns
channel:
  - SMS
  - MMS
  - RCS
---

# Link-Verkürzung

> Auf dieser Seite erfahren Sie, wie Sie die Linkverkürzung in Ihren SMS- und RCS-Nachrichten aktivieren, verkürzte Links testen, Ihre angepasste Domain in verkürzten Links verwenden und vieles mehr.

{% alert important %}
Braze führt schrittweise die [einheitliche Linkverkürzung]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/link_shortening/?sdktab=unified) ein, die alle verkürzten SMS- und RCS-Links in ein einziges personalisiertes Linkformat zusammenführt (z. B. `brz.ai/abcdefgh`).
{% endalert %}

{% sdktabs %}
{% sdktab Legacy %}

{% multi_lang_include link_shortening_temp/legacy_link_shortening.md %}

{% endsdktab %}
{% sdktab Unified %}

{% multi_lang_include link_shortening_temp/unified_link_shortening.md %}

{% endsdktab %}
{% endsdktabs %}