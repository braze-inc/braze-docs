---
nav_title: Acortamiento de enlaces
article_title: Acortamiento de enlaces
page_order: 3
description: "Este artículo de referencia explica cómo activar el acortamiento de enlaces en tus mensajes SMS y algunas preguntas frecuentes."
page_type: reference
alias: "/link_shortening/"
tool:
  - Campaigns
channel:
  - SMS
  - MMS
  - RCS
---

# Acortamiento de enlaces

> En esta página se explica cómo activar el acortamiento de enlaces en tus mensajes SMS y RCS, probar enlaces acortados, utilizar tu dominio personalizado en enlaces acortados y mucho más.

{% alert important %}
Braze está implementando gradualmente el [acortamiento de enlaces unificado]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/link_shortening/?sdktab=unified), que consolida todos los enlaces acortados de SMS y RCS en un único formato de enlace personalizado (por ejemplo, `brz.ai/abcdefgh`).
{% endalert %}

{% sdktabs %}
{% sdktab Legacy %}

{% multi_lang_include link_shortening_temp/legacy_link_shortening.md %}

{% endsdktab %}
{% sdktab Unified %}

{% multi_lang_include link_shortening_temp/unified_link_shortening.md %}

{% endsdktab %}
{% endsdktabs %}