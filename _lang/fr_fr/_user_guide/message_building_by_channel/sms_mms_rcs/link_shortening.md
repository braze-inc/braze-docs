---
nav_title: Raccourcissement de lien
article_title: Raccourcissement de lien
page_order: 3
description: "Cet article de référence explique comment activer le raccourcissement des liens dans vos messages SMS et répond à quelques questions fréquemment posées."
page_type: reference
alias: "/link_shortening/"
tool:
  - Campaigns
channel:
  - SMS
  - MMS
  - RCS
---

# Raccourcissement de lien

> Cette page explique comment activer le raccourcissement des liens dans vos messages SMS et RCS, tester les liens raccourcis, utiliser votre domaine personnalisé dans les liens raccourcis, et bien plus encore.

{% alert important %}
Braze déploie progressivement le [raccourcissement de lien unifié]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/link_shortening/?sdktab=unified), qui regroupe tous les liens raccourcis SMS et RCS en un format de lien personnalisé unique (par exemple, `brz.ai/abcdefgh`).
{% endalert %}

{% sdktabs %}
{% sdktab Legacy %}

{% multi_lang_include link_shortening_temp/legacy_link_shortening.md %}

{% endsdktab %}
{% sdktab Unified %}

{% multi_lang_include link_shortening_temp/unified_link_shortening.md %}

{% endsdktab %}
{% endsdktabs %}