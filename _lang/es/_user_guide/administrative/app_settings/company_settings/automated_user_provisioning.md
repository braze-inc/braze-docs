---
nav_title: Aprovisionamiento automático de usuarios
article_title: Aprovisionamiento automático de usuarios
page_order: 10
page_type: reference
description: "Este artículo de referencia explica qué información debe proporcionar para el aprovisionamiento automatizado de usuarios y cómo y dónde utilizar el token generado del Sistema para la gestión de identidades entre dominios (SCIM)."
alias: /scim/automated_user_provisioning/

---

# Aprovisionamiento automático de usuarios

> Utiliza el aprovisionamiento SCIM para crear y administrar automáticamente usuarios de Braze a través de la API. Este artículo te explica qué información debes proporcionar, cómo generar tu token SCIM y dónde encontrar tu punto final de la API SCIM.

{% multi_lang_include early_access_beta_alert.md feature='SCIM provisioning' %}

## Acceso a la configuración de aprovisionamiento SCIM

1. En el panel de Braze, ve a **Configuración** > **Configuración administrativa** > **Aprovisionamiento SCIM** y, a continuación, selecciona **Configurar integración SCIM**.
2. En el paso **de configuración de Braze**, selecciona un método de aprovisionamiento y proporciona la configuración de acceso.

![Una página para configurar la integración SCIM con secciones para seleccionar un método de aprovisionamiento y proporcionar la configuración de acceso.]({% image_buster /assets/img_archive/scim_braze_config.png %}){: style="max-width:70%;"}

{: start="3"}
3\. En el paso **de configuración del IdP**, sigue los pasos indicados en la plataforma para el método de aprovisionamiento seleccionado.

{% tabs %}
{% tab Okta - Braze app %}

{% multi_lang_include early_access_beta_alert.md feature='The Okta integration' %}

Utiliza la opción **Okta - Braze app** si has configurado la aplicación Braze para SAML SSO en Okta. Si configuras una aplicación personalizada para SSO, sigue las instrucciones de la pestaña [Okta - Integración de aplicaciones personalizadas]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/automated_user_provisioning/?tab=okta%20-%20custom%20app%20integration#step-1-set-up-scim-provisioning).

## Paso 1: Configurar el aprovisionamiento SCIM

### Paso 1.1: Habilitar SCIM

1. En Okta, ve a **Aplicaciones** > **Aplicaciones** y selecciona **Crear integración de aplicaciones**. Selecciona **SAML 2.0** como método de inicio de sesión.
2. Rellena los siguientes datos (que tienen su ubicación en el [paso **de configuración**](#accessing-scim-provisioning-settings) de Braze [**IdP**](#accessing-scim-provisioning-settings)) para crear una aplicación personalizada:
- Logotipo de la aplicación
- URL de inicio de sesión único
- URL de la audiencia (ID de la entidad SP)
3. Selecciona el **Acabado**.
4. Selecciona la pestaña **General**. 
5. En la sección **Configuración de la aplicación**, selecciona **Editar**.
6. En el campo **Aprovisionamiento**, selecciona **SCIM**. 

### Paso 1.2: Desactivar la visibilidad de la aplicación

1. En el campo **Visibilidad de la aplicación**, selecciona la casilla de verificación **No mostrar el icono de la aplicación al usuario**. Esto impide que los usuarios accedan al SSO a través de la aplicación, que está destinada exclusivamente a SCIM. 
2. Seleccione **Guardar**.

### Paso 1.3: Configurar la integración SCIM

1. Selecciona la pestaña **Aprovisionamiento**.
2. En **Configuración** > **Integración** > **Conexión SCIM,** selecciona **Editar** y rellena los campos que aparecen en la tabla de la página **Configuración del aprovisionamiento SCIM**.

### Paso 1.4: Prueba las credenciales de la API

Selecciona **«Credenciales de API de prueba**». Aparecerá un mensaje de verificación si la integración se ha realizado correctamente y podrás guardar los cambios.

### Paso 1.5: Habilitar el aprovisionamiento de la aplicación

1. En **Aprovisionamiento** > **Configuración** > **A la aplicación** > **Aprovisionamiento a la aplicación**, selecciona **Editar**.
2. Habilita lo siguiente:
    - Crear usuarios
    - Actualizar atributos de usuarios
    - Desactivar usuarios
3. Revisa y configura la sección **Asignación de atributos** con los mapeos que aparecen en la tabla de la página **Configuración del aprovisionamiento SCIM**.

## Paso 2: Asignar usuarios a la aplicación

1. Selecciona la pestaña **Asignación**.
2. Selecciona **Asignar** y elige una opción.
3. Asigna la aplicación a las personas que deben tener acceso a Braze.
4. Selecciona **Hecho** cuando hayas completado la tarea.

{% endtab %}
{% tab Okta - Custom app integration %}

{% multi_lang_include early_access_beta_alert.md feature='The Okta integration' %}

Utiliza la opción **Okta - Integración de aplicaciones personalizadas** si configuras una aplicación personalizada para SSO. Si configuras la aplicación Braze para SAML SSO en Okta, sigue las instrucciones de la pestaña [Okta - Braze app]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/automated_user_provisioning/?tab=okta%20-%20braze%20app#step-1-set-up-scim-provisioning).

## Paso 1: Configurar el aprovisionamiento SCIM

### Paso 1.1: Habilitar SCIM

1. En Okta, ve a tu aplicación Braze.
2. Selecciona la pestaña **General**.
3. En la sección **Configuración de la aplicación**, selecciona **Editar**.
4. En el campo **Aprovisionamiento**, selecciona **SCIM**.
5. Seleccione **Guardar**.

### Paso 1.2: Configurar la integración SCIM

1. Selecciona la pestaña **Aprovisionamiento**.
2. En **Configuración** > **Integración** > **Conexión SCIM**, selecciona **Editar** y rellena los campos que aparecen en la tabla de la página **Configurar aprovisionamiento SCIM**.
3. Prueba las credenciales de la API seleccionando **Probar credenciales de la API**.
4. Seleccione **Guardar**.

### Paso 1.3: Habilitar el aprovisionamiento de la aplicación

1. En **Aprovisionamiento** > **Configuración** > **A la aplicación** > **Aprovisionamiento a la aplicación**, selecciona **Editar**.
2. Habilita lo siguiente:
    - Crear usuarios
    - Actualizar atributos de usuarios
    - Desactivar usuarios
3. Revisa y configura la sección **Asignación de atributos** con los mapeos que aparecen en la tabla de la página **Configuración del aprovisionamiento SCIM**.

## Paso 2: Asignar usuarios a la aplicación

1. Selecciona la pestaña **Asignación**.
2. Selecciona **Asignar** y elige una opción.
3. Asigna la aplicación a las personas que deben tener acceso a Braze.
4. Selecciona **Hecho**.

{% endtab %}
{% tab Entra ID %}

{% multi_lang_include early_access_beta_alert.md feature='The Entra ID integration' %}

## Paso 1: Configurar la aplicación de aprovisionamiento SCIM

### Paso 1.1: Inicia sesión en el centro de administración de Microsoft Entra.

Inicia sesión en tu centro de administración de Microsoft Entra.

### Paso 1.2: Crea y configura tu aplicación SCIM.

1. En el menú de navegación, ve a **Entra ID** > **Aplicaciones empresariales**.
2. Selecciona **Nueva aplicación**.
3. Selecciona **Crear tu propia aplicación**.
4. En el panel, introduce un nombre para tu aplicación.
5. En la sección **«¿Qué deseas hacer con tu aplicación?»**, selecciona **«Integración de una aplicación que no se encuentra en la galería (No galería)**».
6. Seleccione **Crear**.

### Paso 1.3: Configurar la integración SCIM

1. Ve a la sección **Administrar** > **Aprovisionamiento** de tu aplicación SCIM.
2. Selecciona **Conectar tu aplicación** o **Nueva configuración** y rellena los campos que aparecen en la tabla de la página **Configuración del aprovisionamiento SCIM**.

### Paso 1.4: Habilitar el aprovisionamiento de la aplicación

1. Ve a la sección **Administrar** > **Mapeo de atributos (vista previa)** de tu aplicación SCIM.
2. Selecciona **Proporcionar usuarios de Microsoft Entra ID**.
3. Revisa y configura la sección **de mapeo de atributos** para que coincida con los atributos que aparecen en la tabla de la página **Configuración del aprovisionamiento SCIM**.
4. Cierra la página **de mapeo de atributos**.

## Paso 2: Asignar usuarios a la aplicación

1. Ve a **Administrador** > **Usuarios y grupos**.
2. Selecciona **Añadir usuario/grupo**.
3. Selecciona **Ninguno seleccionado** para asignar usuarios a la aplicación.
4. Selecciona el botón **Seleccionar** para confirmar la asignación.

{% endtab %}
{% tab Custom %}

## Paso 1: Configura tu configuración SCIM

- **Espacio de trabajo predeterminado:** Selecciona el espacio de trabajo donde se deben añadir los nuevos usuarios de forma predeterminada. Si no especificas un espacio de trabajo en tu [solicitud de API SCIM]({{site.baseurl}}/post_create_user_account/), Braze asigna a los usuarios a este espacio de trabajo.
- **Origen del servicio:** Introduce el dominio de origen de tus solicitudes SCIM. Braze utiliza esto en el`X-Request-Origin`encabezado para verificar de dónde proceden las solicitudes.
- **Lista de direcciones IP permitidas (opcional):** Puedes restringir las solicitudes SCIM a direcciones IP específicas. Introduce una lista separada por comas o un rango de direcciones IP que deseas permitir. El`X-Request-Origin`encabezado de cada solicitud se utiliza para comprobar la dirección IP de la solicitud con la lista de permitidos.

![Formulario de configuración de aprovisionamiento SCIM con tres campos: Espacio de trabajo predeterminado, origen del servicio y lista de IP permitidas opcional. El botón «Generar token SCIM» está desactivado.]({% image_buster /assets/img/scim_unfilled.png %})

## Paso 2: Generar un token SCIM

Después de completar los campos obligatorios, pulsa **Generar token SCIM** para generar un token SCIM y ver tu punto final de la API SCIM. Asegúrate de copiar el token SCIM antes de salir de la página. **Este token solo aparece una vez.** 

![Campos SCIM API Endpoint y SCIM token mostrados con valores enmascarados y botones de copiar. Debajo del campo del token hay un botón «Restablecer token».]({% image_buster /assets/img/scim.png %})

Braze espera que todas las solicitudes SCIM contengan el token de portador de la API SCIM adjunto mediante un encabezado HTTP `Authorization`.

{% endtab %}
{% endtabs %}
