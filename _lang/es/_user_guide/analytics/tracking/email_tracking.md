---
nav_title: Píxel de apertura de correo electrónico y seguimiento de clics
article_title: Píxel de apertura de correo electrónico y seguimiento de clics
page_order: 1
page_type: reference
description: "Este artículo de referencia explica cómo implementar el seguimiento de píxeles abiertos y de clics."

---

# Píxel de apertura de correo electrónico y seguimiento de clics

> El [seguimiento de píxeles abiertos]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/#changing-location-of-tracking-pixel) y de clics puede activarse o desactivarse para cada perfil de usuario. Esta flexibilidad le ayuda a cumplir las leyes de privacidad regionales, donde el perfil de un usuario individual puede indicar que ya no quiere ser rastreado.

## Activar el píxel de apertura o el seguimiento de clics

Al importar o actualizar un perfil de usuario a través de [API]({{site.baseurl}}/api/objects_filters/user_attributes_object/#braze-user-profile-fields) o [CSV]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv), hay dos campos disponibles para modificar:

- `email_open_tracking_disabled`: Acepta `true` o `false`. Seleccione `false` para añadir el píxel de seguimiento de apertura a todos los correos electrónicos futuros enviados a este usuario. Disponible sólo para SparkPost y SendGrid.
- `email_click_tracking_disabled`: Acepta `true` o `false`. Seleccione `false` para añadir el seguimiento de clics a todos los enlaces de un futuro correo electrónico enviado a este usuario. Disponible sólo para SparkPost y SendGrid.

Como referencia, esta información se refleja en el perfil del usuario en el correo electrónico **Configuración del contacto**, situado en la pestaña **Compromiso**.

![Campos del píxel de apertura de correo electrónico y seguimiento de clics en la pestaña de interacción del perfil de un usuario]({% image_buster /assets/img_archive/open_click_user_profile.png %}){: style="max-width:60%;"}

