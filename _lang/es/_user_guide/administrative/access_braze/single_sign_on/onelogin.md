---
nav_title: OneLogin
article_title: OneLogin
page_order: 5
page_type: tutorial
description: "Este artículo le mostrará cómo configurar Braze para utilizar OneLogin para el inicio de sesión único."

---

# OneLogin

> [OneLogin](https://www.onelogin.com/) es una plataforma de identidad en la nube que proporciona una solución integral para gestionar las identidades de los usuarios. OneLogin se integra con aplicaciones en la nube y locales mediante SAML 2.0, para el inicio de sesión único (SSO), el aprovisionamiento de usuarios, la autenticación multifactor, etc.

## Requisitos

Tras la configuración, se le pedirá que proporcione una URL de inicio de sesión y una URL de Assertion Consumer Service (ACS).  

| Requisito | Detalles |
|---|---|
| Dominio Braze | Necesitará su dominio Braze para configurar Braze en OneLogin. Si su instancia es `US-01`, deberá introducir la URL de su panel de control en el panel de control de OneLogin. <br><br> Por ejemplo, si la URL de tu panel es `https://dashboard-01.braze.com`, tienes que introducir `dashboard-01.braze.com`.  |
| Clave API RelayState | Para habilitar la sesión de IdP, ve a **Configuración** > **Claves de API** y crea una clave de API con permisos `sso.saml.login`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Inicio de sesión iniciado por IdP en OneLogin

### Paso 1: Configurar la aplicación Braze

1. Inicie sesión en [OneLogin](https://app.onelogin.com/login). Haga clic en **Administración**.![Página de administración de OneLogin.]({% image_buster /assets/img/onelogin_1.jpg %})<br><br>
2. Vaya a **Aplicaciones** > **Añadir aplicaciones** en la barra de navegación superior. Busque "Braze" y seleccione la aplicación Braze.![Resultados de la búsqueda de Braze en OneLogin.]({% image_buster /assets/img/onelogin_2.jpg %})<br><br>
3. Guarda la aplicación Braze en tu empresa.![]({% image_buster /assets/img/onelogin_3.jpg %})<br><br>
4. Una vez guardado, vaya a **Configuración** y añada su **dominio Braze** y su clave API **RelayState**.![Pestaña de configuración de OneLogin para la aplicación Braze.]({% image_buster /assets/img/onelogin_4.png %})<br><br>
5. Braze espera las aserciones SAML en un [formato específico]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/#configure-your-identity-provider). En **Parámetros**, los atributos soportados por Braze deberían estar precargados. Compruebe que son correctos.![Parámetros SAML de Braze en OneLogin.]({% image_buster /assets/img/onelogin_5.jpg %})<br><br>
6. Copia el **certificado** y el **punto final SAML 2.0 (HTTP)** necesarios para configurar el panel de Braze desde la pestaña **SSO**.![Certificados para copiar desde la pestaña SSO de la aplicación Braze en OneLogin.]({% image_buster /assets/img/onelogin_6.jpg %})

### Paso 2: Configurar OneLogin en Braze

Una vez que haya configurado Braze en su OneLogin, le proporcionarán una URL de destino (`SAML 2.0 Endpoint (HTTP)`) y un certificado `x.509` que deberá introducir en su cuenta Braze.

Una vez que el administrador de su cuenta haya activado SAML SSO para su cuenta, vaya a **Configuración** > **Configuración de administración** > **Configuración de seguridad** y **active la** sección SAML SSO.

En esta página, introduzca lo siguiente:

| Requisito | Detalles |
|---|---|
| `SAML Name` | Aparecerá como texto del botón en la pantalla de inicio de sesión. Suele ser el nombre de tu proveedor de identidad, como "OneLogin". |
| `Target URL` | Esta es la URL `SAML 2.0 Endpoint (HTTP)` proporcionada por OneLogin.|
| `Certificate` | El certificado codificado PEM `x.509` lo proporciona tu OneLogin. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![Configuración de SAML SSO con el alternador seleccionado.]({% image_buster /assets/img/samlsso.png %})

{% alert tip %}
Si desea que los usuarios de su cuenta Braze sólo inicien sesión con SAML SSO, puede [restringir la autenticación de inicio de sesión único]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/#restriction) desde la página **Configuración de la empresa**.
{% endalert %}

