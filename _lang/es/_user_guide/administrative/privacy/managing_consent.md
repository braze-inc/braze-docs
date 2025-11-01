---
nav_title: Administrar el consentimiento
article_title: Administrador del consentimiento
page_order: 10
page_type: reference
description: "Este artículo de referencia proporciona consejos sobre cómo gestionar el consentimiento utilizando Braze."
---

# Administrar el consentimiento

> Este artículo de referencia proporciona consejos sobre cómo gestionar el consentimiento de tus usuarios utilizando Braze.

Braze no puede proporcionar asesoramiento específico sobre la interpretación de leyes y reglamentos ni ofrecer orientación sobre la gestión del consentimiento, ya que esto dependerá de la interpretación de la ley que haga tu equipo jurídico. Sin embargo, ofrecemos una serie de herramientas de apoyo a la gestión de suscripciones y consentimientos.

Tu planteamiento debe depender del rigor que exija tu equipo jurídico en función de su interpretación de la ley. Aquí tienes algunas opciones a considerar, ordenadas de más estricta a menos estricta:

- **Equipos:** Utiliza [equipos Braze]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) para una verdadera gobernanza. Se trata de añadir un atributo personalizado a todos los perfiles de usuario para indicar su estado de consentimiento, la fecha de consentimiento, o ambas cosas. A continuación, debes migrar todas las campañas y Canvases al equipo designado y ajustar en consecuencia los permisos de usuario en el panel.
- **Atributo del perfil de usuario:** Añade un atributo de consentimiento a todos los perfiles de usuario. Este atributo indicará si un usuario ha dado su consentimiento o no. En el futuro, podrás incluir un segmento de usuarios que hayan dado su consentimiento (por ejemplo, `consent = true`) en todas tus campañas y Canvases.
- **Grupos de suscripción específicos de cada canal:** Manipula grupos de suscripción para canales específicos (notificaciones push, correo electrónico, etc.) para gestionar el consentimiento. Inicialmente, marca a los usuarios como cancelados de estos canales y sólo márcalos como suscritos después de que hayan dado su consentimiento.

{% alert important %}
Consulta a tu equipo jurídico para determinar el enfoque adecuado para que tu organización cumpla los requisitos de gestión del consentimiento.
{% endalert %}

