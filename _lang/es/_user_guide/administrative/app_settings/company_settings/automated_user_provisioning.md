---
nav_title: Aprovisionamiento automatizado de usuarios
article_title: Aprovisionamiento automatizado de usuarios
page_order: 10
page_type: reference
description: "Este artículo de referencia explica qué información debes proporcionar para la automatización de la provisión de usuarios y cómo y dónde utilizar el token generado por el Sistema de Gestión de Identidades entre Dominios (SCIM)."
alias: /scim/automated_user_provisioning/

---

# Aprovisionamiento automatizado de usuarios

> Utiliza el aprovisionamiento SCIM para crear y administrar automáticamente usuarios Braze a través de la API. Este artículo te explica qué información debes proporcionar, cómo generar tu token SCIM y dónde encontrar tu punto final de la API SCIM.

## Paso 1: Acceder a la configuración de privionización del SCIM

En el panel de Braze, ve a **Configuración** > **Configuración de administrador** > **Aprovisionamiento SCIM**.

## Paso 2: Configura tus ajustes SCIM

Para habilitar el aprovisionamiento SCIM, proporciona la siguiente información:

- **Espacio de trabajo predeterminado:** Selecciona el espacio de trabajo en el que se añadirán por defecto los nuevos usuarios. Si no especificas un espacio de trabajo en tu [solicitud de API SCIM]({{site.baseurl}}/post_create_user_account/), Braze asigna usuarios a este espacio de trabajo.
- **Origen del servicio:** Introduce el dominio de origen de tus peticiones SCIM. Braze lo utiliza en el encabezado `X-Request-Origin` para verificar de dónde proceden las solicitudes.
- **Lista de IP permitidas (opcional):** Puedes restringir las peticiones SCIM a determinadas direcciones IP.
Introduce una lista o rango de direcciones IP separadas por comas para permitirlas. El encabezado `X-Request-Origin` de cada solicitud se utilizará para comprobar la dirección IP de la solicitud con la lista permitida.

{% alert note %}
Este punto final SCIM no se integra directamente con los proveedores de identidad.
{% endalert %}

Formulario de configuración del aprovisionamiento SCIM con tres campos: Espacio de trabajo predeterminado, origen del servicio y lista opcional de IP permitidas. El botón "Generar token SCIM" está desactivado.]({% image_buster /assets/img/scim_unfilled.png %})

## Paso 3: Consigue tu token SCIM y tu punto final

Tras rellenar los campos obligatorios, pulsa **Generar to** ken SCIM para generar un token SCIM y ver tu punto final de API SCIM. Asegúrate de copiar el token SCIM antes de salir navegando. **Este token sólo se presentará una vez.** 

Los campos "SCIM API Endpoint" y "SCIM Token" se muestran con valores enmascarados y botones de copia. Debajo del campo token hay un botón "Restablecer token".]({% image_buster /assets/img/scim.png %})

Braze espera que todas las solicitudes SCIM contengan el token de portador de la API SCIM adjunto mediante un encabezado HTTP `Authorization`.

