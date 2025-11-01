---
nav_title: OneLogin
article_title: OneLogin
page_order: 5
page_type: tutorial
description: "Este artículo te explicará cómo configurar Braze para utilizar OneLogin para el inicio de sesión único."

---

# OneLogin

> [OneLogin](https://www.onelogin.com/) es una plataforma de identidad en la nube que proporciona una solución integral para gestionar las identidades de los usuarios. OneLogin se integra con aplicaciones en la nube y locales mediante SAML 2.0, para el inicio de sesión único (SSO), el aprovisionamiento de usuarios, la autenticación multifactor, etc.

## Requisitos

Al configurarlo, se te pedirá que proporciones una URL de inicio de sesión y una URL de servicio de consumidor de aserciones (ACS).  

| Requisito | Detalles |
|---|---|
| Dominio Braze | Necesitarás tu dominio Braze para configurar Braze dentro de OneLogin. Si tu instancia es `US-01`, tendrás que introducir la URL de tu panel en el panel de OneLogin. <br><br> Por ejemplo, si la URL de tu panel es `https://dashboard-01.braze.com`, tienes que introducir `dashboard-01.braze.com`.  |
| Clave de API de RelayState | Para habilitar la sesión de IdP, ve a **Configuración** > **Claves de API** y crea una clave de API con permisos `sso.saml.login`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Inicio de sesión iniciado por IdP en OneLogin

### Paso 1: Configura la aplicación Braze

1. Inicia sesión en [OneLogin](https://app.onelogin.com/login). Haz clic en **Administración**.\![Página de Administración de OneLogin.]({% image_buster /assets/img/onelogin_1.jpg %})<br><br>
2. Ve a **Aplicaciones** > **Añadir aplicaciones** en la barra de navegación superior. Busca "Braze" y selecciona la aplicación Braze.\![Resultados de la búsqueda de Braze en OneLogin.]({% image_buster /assets/img/onelogin_2.jpg %})<br><br>
3. Guarda la aplicación Braze en tu empresa\![]({% image_buster /assets/img/onelogin_3.jpg %})<br><br>
4. Cuando se haya guardado, ve a **Configuración** y añade tu **dominio Braze** y tu clave de API **RelayState**.\![Pestaña Configuración de OneLogin para la aplicación Braze.]({% image_buster /assets/img/onelogin_4.png %})<br><br>
5. Braze espera las afirmaciones SAML en un [formato específico]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/#configure-your-identity-provider). En **Parámetros**, los atributos admitidos por Braze deben estar rellenados previamente. Comprueba que son correctos\![Braze los parámetros SAML en OneLogin.]({% image_buster /assets/img/onelogin_5.jpg %})<br><br>
6. Copia el **certificado** y el **punto final SAML 2.0 (HTTP)** necesarios para configurar el panel Braze desde la pestaña **SSO**.\![Certificados para copiar desde la pestaña SSO de la aplicación Braze en OneLogin.]({% image_buster /assets/img/onelogin_6.jpg %})

### Paso 2: Configurar OneLogin en Braze

Una vez que hayas configurado Braze en tu OneLogin, te proporcionarán una URL de destino (`SAML 2.0 Endpoint (HTTP)`) y un certificado `x.509` que introducirás en tu cuenta Braze.

Después de que el director de cuentas haya habilitado SAML SSO para tu cuenta, ve a **Configuración** > **Configuración de administración** > **Configuración de seguridad** y alterna la sección SAML SSO a **ON (Activado)**

En esta página, introduce lo siguiente:

| Requisito | Detalles |
|---|---|
| `SAML Name` | Aparecerá como texto del botón en la pantalla de iniciar sesión. Suele ser el nombre de tu proveedor de identidad, como "OneLogin". |
| `Target URL` | Esta es la URL `SAML 2.0 Endpoint (HTTP)` proporcionada por OneLogin.|
| `Certificate` | El certificado codificado PEM `x.509` lo proporciona tu OneLogin. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

\![Configuración de SAML SSO con el alternador seleccionado.]({% image_buster /assets/img/samlsso.png %})

{% alert tip %}
Si quieres que los usuarios de tu cuenta Braze sólo inicien sesión con SAML SSO, puedes [restringir la autenticación de inicio de sesión único]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/#restriction) desde la página **Configuración de la empresa**.
{% endalert %}

