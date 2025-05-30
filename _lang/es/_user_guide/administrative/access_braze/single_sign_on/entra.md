---
nav_title: Microsoft Entra SSO
article_title: Microsoft Entra SSO
page_order: 3
page_type: tutorial
description: "Este artículo te explicará cómo configurar las funciones de inicio de sesión único de Microsoft Entra con Braze."

---

# Microsoft Entra SSO

> [Microsoft Entra SSO](https://learn.microsoft.com/en-us/entra/identity/saas-apps/braze-tutorial) es el servicio de gestión de identidades y accesos basado en la nube de Microsoft, que ayuda a tus empleados a iniciar sesión y acceder a los recursos. Puedes utilizar Entra SSO para controlar el acceso a tus aplicaciones y a los recursos de tus aplicaciones, en función de tus requisitos empresariales.

## Requisitos

Tras la configuración, se le pedirá que proporcione una URL de inicio de sesión y una URL de Assertion Consumer Service (ACS).  

| Requisito | Detalles |
|---|---|
| URL de inicio de sesión | `https://<SUBDOMAIN>.braze.com/sign_in` <br><br> Para el subdominio, utilice el subdominio de coordinación que aparece en la [URL de tu instancia Braze]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/). Por ejemplo, si tu instancia es `US-01`, tu URL es `https://dashboard-01.braze.com`. Esto significa que su subdominio será `dashboard-01`. |
| URL del Servicio de Consumidor de Afirmaciones (ACS) | `https://<SUBDOMAIN>.braze.com/auth/saml/callback` <br> Para algunos proveedores de identidad, también puede denominarse URL de respuesta, URL de audiencia o URI de audiencia. |
| ID de la entidad | `braze_dashboard`|
| Clave API RelayState | Para habilitar el inicio de sesión del proveedor de identidad, vaya a **Configuración** > **Claves API** y cree una clave API con permisos `sso.saml.login`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Inicio de sesión iniciado por el proveedor de servicios (SP) en Microsoft Entra SSO

### Paso 1: Añadir Braze desde la galería

1. En tu centro de administración de Microsoft Entra, ve a **Identidad** > **Aplicaciones** > **Aplicaciones de empresa** y, a continuación, selecciona **Nueva aplicación**.
2. Busca **Braze** en el cuadro de búsqueda, selecciónalo en el panel de resultados y, a continuación, selecciona **Añadir**.

### Paso 2: Configurar Microsoft Entra SSO

1. En tu centro de administración de Microsoft Entra, ve a la página de integración de tu aplicación Braze y selecciona **Inicio de sesión único**.
2. En la página **Seleccionar un método de inicio de sesión único**, selecciona **SAML** como método.
3. En la página **Configurar inicio de sesión único con SAML**, selecciona el icono de edición de **Configuración básica de SAML**.
4. Configure la aplicación en modo iniciado por IdP introduciendo una **URL de respuesta** que combine su [instancia Braze]({{site.baseurl}}/user_guide/administrative/access_braze/braze_instances/#braze-instances) con el siguiente patrón: `https://<SUBDOMAIN>.braze.com/auth/saml/callback`.
5. Opcionalmente, configure RelayState introduciendo su clave API generada por Relay State en el campo **Relay State (Opcional)**.
6. Si desea configurar la aplicación en modo iniciado por SP, seleccione **Establecer URL adicionales** e introduzca una URL de inicio de sesión que combine su [instancia Braze]({{site.baseurl}}/user_guide/administrative/access_braze/braze_instances/#braze-instances) con el siguiente patrón: `https://<SUBDOMAIN>.braze.com/sign_in`.
7. Formatee las afirmaciones SAML en el formato específico esperado por Braze. Consulte las siguientes fichas sobre atributos de usuario y reclamaciones de usuario para comprender cómo deben formatearse estos atributos y valores.

{% tabs %}
{% tab Atributos del usuario %}
Puede gestionar los valores de estos atributos desde la sección **Atributos de usuario** de la página **Integración de aplicaciones**.

Utilice las siguientes combinaciones de atributos:

- `givenname` = `user.givenname`
- `surname`= `user.surname`
- `emailaddress` = `user.mail`
- `name` = `user.userprincipalname`
- `email` = `user.userprincipalname`
- `first_name` = `user.givenname`
- `last_name` = `user.surname`
- `Unique User Identifier` = `user.userprincipalname`

{% alert important %}
Es muy importante que el campo de correo electrónico coincida con lo que está configurado para sus usuarios en Braze. En la mayoría de los casos, será el mismo que `user.userprincipalname`. Sin embargo, si tiene una configuración diferente, trabaje con el administrador del sistema para asegurarse de que estos campos coinciden exactamente.
{% endalert %}

{% endtab %}
{% tab Reclamaciones de usuarios %}

En la página **Configurar inicio de sesión único con SAML**, seleccione **Editar** para abrir el cuadro de diálogo **Atributos de usuario**. A continuación, edite las reclamaciones de los usuarios de acuerdo con el formato adecuado.

Utilice las siguientes combinaciones de nombres de reclamaciones:

- `claims/givenname` = `user.givenname`
- `claims/surname` = `user.surname`
- `claims/emailaddress` = `user.userprincipalname`
- `claims/name` = `user.userprincipalname`
- `claims/nameidentifier` = `user.userprincipalname`

{% alert important %}
Es muy importante que el campo de correo electrónico coincida con lo que está configurado para sus usuarios en Braze. En la mayoría de los casos, será el mismo que `user.userprincipalname`. Sin embargo, si tiene una configuración diferente, trabaje con el administrador del sistema para asegurarse de que estos campos coinciden exactamente.
{% endalert %}

Puede gestionar estas reclamaciones y valores de usuario desde la sección **Gestionar reclamación**.

{% endtab %}
{% endtabs %}

{: start="8"}
8\. Vaya a la página **Configurar el inicio de sesión único con SAML** y, a continuación, desplácese hasta la sección **Certificado de firma SAML** y descargue el **certificado adecuado (Base64)** en función de sus requisitos.
9\. Vaya a la sección **Configurar Braze** y copie las URL adecuadas para utilizarlas en la [configuración de Braze](#step-3).

### Paso 3: Configurar Microsoft Entra SSO en Braze {#step-3}

Una vez que hayas configurado Braze en el centro de administración de Microsoft Entra, Microsoft Entra te proporcionará una URL de destino (URL de inicio de sesión) y **x.509** certificado que introducirás en tu cuenta Braze.

Después de que tu director de cuentas haya habilitado SAML SSO para tu cuenta, haz lo siguiente:

1. Ve a **Configuración** > **Configuración del administrador** > **Configuración de seguridad** y alterna la sección SAML SSO a **ON**.
2. En la misma página, añada lo siguiente:

| Requisito | Detalles |
|---|---|
| `SAML Name` | Aparecerá como texto del botón en la pantalla de inicio de sesión. Suele ser el nombre de tu proveedor de identidad, como "Microsoft Entra". |
| `Target URL` | Esta es la URL para iniciar sesión proporcionada por Microsoft Entra.|
| `Certificate` | El certificado codificado PEM de `x.509` lo proporciona tu proveedor de identidad. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert tip %}
Si desea que los usuarios de su cuenta Braze sólo inicien sesión con SAML SSO, puede [restringir la autenticación de inicio de sesión único]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/#restriction) desde la página **Configuración de la empresa**.
{% endalert %}
