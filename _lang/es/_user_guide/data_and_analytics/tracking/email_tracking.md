---
nav_title: Píxel de apertura de correo electrónico y seguimiento de clics
article_title: Píxel de apertura de correo electrónico y seguimiento de clics
page_order: 1
page_type: reference
description: "Este artículo de referencia explica cómo implementar el seguimiento de píxeles abiertos y de clics."

---

# Píxel de apertura de correo electrónico y seguimiento de clics

> El [seguimiento de píxeles abiertos][open_tracking] y de clics puede activarse o desactivarse para cada perfil de usuario. Esta flexibilidad le ayuda a cumplir las leyes de privacidad regionales, donde el perfil de un usuario individual puede indicar que ya no quiere ser rastreado.

## Activar el píxel de apertura o el seguimiento de clics

Al importar o actualizar un perfil de usuario a través de [API][api_doc] o [CSV][csv_doc], hay dos campos disponibles para modificar:

- `email_open_tracking_disabled`: Acepta `true` o `false`. Seleccione `false` para añadir el píxel de seguimiento de apertura a todos los correos electrónicos futuros enviados a este usuario.
- `email_click_tracking_disabled`: Acepta `true` o `false`. Seleccione `false` para añadir el seguimiento de clics a todos los enlaces de un futuro correo electrónico enviado a este usuario.

Como referencia, esta información se refleja en el perfil del usuario en el correo electrónico **Configuración del contacto**, situado en la pestaña **Compromiso**.

![Campos de píxel de seguimiento de clics y apertura de correo electrónico en la pestaña Compromiso del perfil de un usuario.][1]{: style="max-width:60%;"}

[open_tracking]: {{site.baseurl}}/user_guide/administrative/app_settings/email_settings/#changing-location-of-tracking-pixel
[api_doc]: {{site.baseurl}}/api/objects_filters/user_attributes_object/#braze-user-profile-fields
[csv_doc]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv
[1]: {% image_buster /assets/img_archive/open_click_user_profile.png %}
