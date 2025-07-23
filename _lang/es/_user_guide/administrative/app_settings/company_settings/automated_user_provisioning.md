---
nav_title: Aprovisionamiento automático de usuarios
article_title: Aprovisionamiento automático de usuarios
page_order: 10
page_type: reference
description: "Este artículo de referencia explica qué información debe proporcionar para el aprovisionamiento automatizado de usuarios y cómo y dónde utilizar el token generado del Sistema para la gestión de identidades entre dominios (SCIM)."
alias: /scim/automated_user_provisioning/

---

# Aprovisionamiento automático de usuarios

> Aprenda lo que necesita proporcionar para el aprovisionamiento automatizado de usuarios y cómo y dónde utilizar su token generado de System for Cross-domain Identity Management (SCIM) y el punto final de la API de SCIM. A continuación, puede llamar a este punto final con su API para aprovisionar automáticamente nuevos usuarios del cuadro de mandos.

Para acceder a esta página, vaya a **Configuración** > **Configuración de administración** > **Aprovisionamiento SCIM**.

## Cómo conseguir tu token SCIM

Tendrás que proporcionar la siguiente información para obtener tu token SCIM:

1. Selecciona un espacio de trabajo predeterminado al que se añadirán los nuevos desarrolladores del panel. Si no especifica un espacio de trabajo en la [llamada a la API SCIM de creación de usuarios]({{site.baseurl}}/post_create_user_account/), éstos se añadirán aquí.
2. Proporcionar un origen de servicio. El origen del servicio es la forma en que Braze identifica de dónde procede la solicitud.
3. Opcionalmente, proporcione una lista separada por comas o un rango de direcciones IP permitidas para solicitudes SCIM. La cabecera `X-Origin-Request` de cada solicitud se utilizará para comprobar la dirección IP de la solicitud con la lista permitida.<br><br>

{% alert note %}
Este punto final SCIM no se integra directamente con los proveedores de identidad.
{% endalert %}

![][1]

Después de rellenar los campos obligatorios, puedes generar un token SCIM y ver tu punto final API SCIM. **Este token solo se presentará una vez.** Braze espera que todas las solicitudes SCIM contengan el token de portador de la API SCIM adjunto mediante un encabezado HTTP `Authorization`.

[1]: {% image_buster /assets/img/scim.png %}
