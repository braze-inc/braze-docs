---
nav_title: Encurtamento de links
article_title: Encurtamento de link
page_order: 3
description: "Este artigo de referência aborda como ativar o encurtamento de links em suas mensagens SMS e algumas perguntas frequentes."
page_type: reference
alias: "/link_shortening/"
tool:
  - Campaigns
channel:
  - SMS
  - MMS
  - RCS
---

# Encurtamento de links

> Esta página aborda como ativar o encurtamento de links em suas mensagens SMS e RCS, testar links encurtados, usar seu domínio personalizado em links encurtados e mais.

{% alert important %}
A Braze está implementando gradualmente o [encurtamento de links unificado]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/link_shortening/?sdktab=unified), que consolida todos os links encurtados de SMS e RCS em um único formato de link personalizado (por exemplo, `brz.ai/abcdefgh`).
{% endalert %}

{% sdktabs %}
{% sdktab Legacy %}

{% multi_lang_include link_shortening_temp/legacy_link_shortening.md %}

{% endsdktab %}
{% sdktab Unified %}

{% multi_lang_include link_shortening_temp/unified_link_shortening.md %}

{% endsdktab %}
{% endsdktabs %}