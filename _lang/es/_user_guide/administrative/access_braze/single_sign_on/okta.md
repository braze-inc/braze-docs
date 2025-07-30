---
nav_title: Okta
article_title: Okta
page_order: 4
page_type: tutorial
description: "Este artículo te mostrará cómo configurar Braze para utilizar Okta en el inicio de sesión único." 

---

# Okta 

> Okta conecta a cualquier persona con cualquier aplicación en cualquier dispositivo. Es un servicio de gestión de identidades de nivel empresarial, creado para la nube, pero compatible con muchas aplicaciones locales. Con Okta, su equipo de TI puede gestionar el acceso de cualquier empleado a cualquier aplicación o dispositivo.

## Requisitos

| Requisito | Detalles |
| ----------- | ------- |
| Okta activado para tu cuenta | Póngase en contacto con su gestor de cuenta Braze para activar esta opción en su cuenta. |
| Privilegios de administrador de Okta | Asegúrese de tener privilegios de administrador antes de configurar Okta. |
| Privilegios de administrador de Braze | Asegúrese de tener privilegios de administrador antes de configurar Okta. |
| Clave API RelayState | Para habilitar la sesión de IdP, ve a **Configuración** > **Claves de API** y crea una clave de API con permisos `sso.saml.login`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Paso 1: Configurar Braze

### Paso 1a: Vaya a Configuración de seguridad en Braze

Después de que su administrador de cuenta haya habilitado SAML SSO para su cuenta, vaya a **Configuración** > **Configuración de administración** > **Configuración de seguridad** y **active la** sección SAML SSO.

![Okta SAML SSO habilitado en la página de configuración de seguridad.]({% image_buster/assets/img/Okta/okta1.png %})

### Paso 1b: Editar la configuración de SAML SSO

Desde el panel de administración de Okta, se le proporcionará una URL de destino (URL de inicio de sesión) y un certificado `x.509`, que deberá introducir en la página **Configuración de seguridad** de su cuenta Braze.

![]({% image_buster /assets/img/Okta/okta5.png %}){: style="max-width:75%"}

| Requisito | Detalles |
|---|---|
| `SAML Name` | Aparecerá como texto del botón en la pantalla de inicio de sesión. Suele ser el nombre de su proveedor de identidad, por ejemplo, "Okta". |
| `Target URL` | Esta es la URL de inicio de sesión proporcionada por el panel de administración de Okta. Encuéntrelo yendo a **Aplicaciones** > su aplicación > pestaña **General** > **App Embed Link** > **Embed Link**. |
| `Certificate` | El certificado codificado PEM de `x.509` lo proporciona tu proveedor de identidad. Debe copiarlo y pegarlo en este campo. Recupérelo en Okta yendo a **SAML Signing Certificates** y seleccionando **Actions** > **Download certificate**. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Seleccione **Guardar cambios** en la parte inferior de la página cuando haya terminado.

## Paso 2: Configurar Okta

En Okta, seleccione la pestaña **Iniciar sesión** de la aplicación Braze SAML y, a continuación, haga clic en **Editar**. 

A continuación, introduce la clave de API RelayState con permiso `sso.saml.login` en el campo **Estado de relay predeterminado**. 

![Okta RelayState predeterminado en la pestaña Sign On.]({% image_buster /assets/img/Okta/okta2.png %}){: style="max-width:75%"}

Asegúrese de guardar estos nuevos ajustes.

{% alert tip %}
Si desea que los usuarios de su cuenta Braze sólo inicien sesión con SAML SSO, puede [restringir la autenticación de inicio de sesión único]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/#restriction) desde la página **Configuración de la empresa**.
{% endalert %}

## Paso 3: Iniciar sesión

Ahora debería poder iniciar sesión en Braze utilizando Okta.

![Inicio de sesión en el panel de Braze con Okta SSO habilitado.]({% image_buster /assets/img/Okta/okta4.png %}){: style="max-width:60%"}

