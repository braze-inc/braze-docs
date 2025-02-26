---
nav_title: Gestión del consentimiento
article_title: Gestión del consentimiento
page_order: 10
page_type: reference
description: "Este artículo de referencia proporciona consejos sobre cómo gestionar el consentimiento utilizando Braze."
---

# Gestión del consentimiento

> Este artículo de referencia ofrece consejos sobre cómo gestionar el consentimiento de sus usuarios utilizando Braze.

Braze no puede proporcionar asesoramiento específico sobre la interpretación de leyes y reglamentos ni ofrecer orientación sobre la gestión del consentimiento, ya que esto dependerá de la interpretación de la ley que haga su equipo jurídico. No obstante, ofrecemos una serie de herramientas de apoyo a la gestión de suscripciones y consentimientos.

Su planteamiento debe depender del rigor que exija su equipo jurídico en función de su interpretación de la ley. He aquí algunas opciones a considerar, ordenadas de la más estricta a la menos estricta:

- **Equipos:** Utiliza [equipos Braze][1] para una verdadera gobernanza. Se trata de añadir un atributo personalizado a todos los perfiles de usuario para indicar su estado de consentimiento, la fecha de consentimiento o ambos. A continuación, debe migrar todas las campañas y Canvases al equipo designado y ajustar los permisos de usuario en el panel de control en consecuencia.
- **Atributo del perfil de usuario:** Añadir un atributo de consentimiento a todos los perfiles de usuario. Este atributo indicará si un usuario ha dado su consentimiento o no. En el futuro, podrá incluir un segmento de usuarios que hayan dado su consentimiento (por ejemplo, `consent = true`) en todas sus campañas y Canvases.
- **Grupos de suscripción específicos de cada canal:** Manipule grupos de suscripción para canales específicos (notificaciones push, correo electrónico, etc.) para gestionar el consentimiento. Inicialmente, marca a los usuarios como no suscritos a estos canales y sólo márcalos como suscritos después de que hayan dado su consentimiento.

{% alert important %}
Consulte a su equipo jurídico para determinar el enfoque adecuado para que su organización cumpla los requisitos de gestión del consentimiento.
{% endalert %}

[1]: {{site.baseurl}}/user_guide/administrative/manage_your_braze_users/teams/
