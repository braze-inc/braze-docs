---
nav_title: Okta
article_title: Okta
page_order: 4
page_type: tutorial
description: "Este artículo te mostrará cómo configurar Braze para utilizar Okta en el inicio de sesión único." 

---

# Okta 

> Okta conecta a cualquier persona con cualquier aplicación en cualquier dispositivo. Es un servicio de gestión de identidades de nivel empresarial, creado para la nube, pero compatible con muchas aplicaciones locales. Con Okta, tu equipo de TI puede gestionar el acceso de cualquier empleado a cualquier aplicación o dispositivo.

## Requisitos

| Requisito | Detalles |
| ----------- | ------- |
| Okta activado para tu cuenta | Ponte en contacto con tu director de cuentas Braze para activar esta opción en tu cuenta. |
| Privilegios de administrador de Okta | Asegúrate de que tienes privilegios de administrador antes de configurar Okta. |
| Privilegios de administrador de Braze | Asegúrate de que tienes privilegios de administrador antes de configurar Okta. |
| Clave de API de RelayState | Para habilitar la sesión de IdP, ve a **Configuración** > **Claves de API** y crea una clave de API con permisos `sso.saml.login`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Paso 1: Configurar Braze

### Paso 1a: Ve a Configuración de seguridad en Braze

Después de que tu director de cuentas haya habilitado SAML SSO para tu cuenta, ve a **Configuración** > **Configuración de administración** > **Configuración de seguridad** y alterna la sección SAML SSO a **ON**.

\![Okta SAML SSO habilitado en la página Configuración de seguridad.]({% image_buster/assets/img/Okta/okta1.png %})

### Paso 1b: Editar configuración SAML SSO

Desde tu panel de administración de Okta, se te proporcionará una URL de destino (URL de inicio de sesión) y un certificado `x.509`, que deberás introducir en la página de **configuración de seguridad** de tu cuenta Braze.

\![]({% image_buster /assets/img/Okta/okta5.png %}){: style="max-width:75%"}

| Requisito | Detalles |
|---|---|
| `SAML Name` | Aparecerá como texto del botón en la pantalla de iniciar sesión. Suele ser el nombre de tu proveedor de identidad, por ejemplo, "Okta". |
| `Target URL` | Esta es la URL para iniciar sesión que proporciona el panel de administración de Okta. Encuéntralo yendo a **Aplicaciones** > tu aplicación > pestaña **General** > **App Embed Link** > **Embed Link**. |
| `Certificate` | El certificado codificado PEM de `x.509` lo proporciona tu proveedor de identidad. Debes copiarlo y pegarlo en este campo. Recupéralo en Okta yendo a **Certificados de firma SAML** y seleccionando **Acciones** > **Descargar certificado**. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Selecciona **Guardar cambios** en la parte inferior de la página cuando hayas terminado.

## Paso 2: Configurar Okta

En Okta, selecciona la pestaña **Iniciar sesión** de la aplicación SAML de Braze y, a continuación, haz clic en **Editar**. 

A continuación, introduce la clave de API RelayState con permiso `sso.saml.login` en el campo **Estado de retransmisión predeterminado**. 

\![Okta RelayState predeterminado en la pestaña Iniciar sesión.]({% image_buster /assets/img/Okta/okta2.png %}){: style="max-width:75%"}

Asegúrate de guardar esta nueva configuración.

{% alert tip %}
Si quieres que los usuarios de tu cuenta Braze sólo inicien sesión con SAML SSO, puedes [restringir la autenticación de inicio de sesión único]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/#restriction) desde la página **Configuración de la empresa**.
{% endalert %}

## Paso 3: Iniciar sesión

¡Ahora deberías poder iniciar sesión en Braze utilizando Okta!

\![Iniciar sesión en el panel de Braze con Okta SSO habilitado.]({% image_buster /assets/img/Okta/okta4.png %}){: style="max-width:60%"}

