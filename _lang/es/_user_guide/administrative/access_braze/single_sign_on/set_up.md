---
nav_title: Configuración de SAML SSO
article_title: Configuración de SAML SSO
page_order: 0
page_type: tutorial
description: "Este artículo le explicará cómo activar el inicio de sesión único SAML para su cuenta Braze."

---

# Inicio de sesión iniciado por el proveedor de servicios (SP)

> Este artículo te explicará cómo habilitar el inicio de sesión único SAML para tu cuenta Braze y cómo obtener un rastreo SAML.

## Requisitos

Tras la configuración, se le pedirá que proporcione una URL de inicio de sesión y una URL de Assertion Consumer Service (ACS).  

| Requisito | Detalles |
|---|---|
| URL del Servicio de Consumidor de Afirmaciones (ACS) | `https://<SUBDOMAIN>.braze.com/auth/saml/callback` <br><br> Para los dominios de la Unión Europea, la URL ASC es `https://<SUBDOMAIN>.braze.eu/auth/saml/callback`. <br><br> Para algunos IdP, también puede denominarse URL de respuesta, URL de inicio de sesión, URL de audiencia o URI de audiencia. |
| ID de la entidad | `braze_dashboard` |
| Clave API RelayState | Ve a **Configuración** > **Claves de API** y crea una clave de API con permisos `sso.saml.login`, y luego introduce la clave de API generada como parámetro `RelayState` dentro de tu IdP. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Si utilizas la [navegación más antigua]({{site.baseurl}}/navigation), puedes encontrar tus claves de API en **Configuración** en **Consola de desarrollador** > **Configuración de API**.
{% endalert %}

## Configuración de SAML SSO

### Paso 1: Configura tu proveedor de identidad

Configure Braze como proveedor de servicios (SP) en su proveedor de identidad (IdP) con la siguiente información. Además, configure la asignación de atributos SAML.

{% alert important %}
Si tiene previsto utilizar Okta como proveedor de identidad, asegúrese de utilizar la integración prediseñada que encontrará en el [sitio web de Okta](https://www.okta.com/integrations/braze/).
{% endalert %}

| Atributo SAML | ¿Es necesario? | Atributos SAML aceptados |
|---|---|---|
|`email` | Obligatoria | `email` <br> `mail` <br> `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/email` |
| `first_name` | Opcional | `first_name` <br> `firstname` <br> `firstName`<br>`http://schemas.xmlsoap.org/ws/2005/05/identity/claims/first_name` |
| `last_name` | Opcional | `last_name` <br> `lastname` <br> `lastName` <br>`http://schemas.xmlsoap.org/ws/2005/05/identity/claims/last_name` |

{% alert note %}
Braze sólo requiere `email` en la aserción SAML.
{% endalert %}

### Paso 2: Configurar Braze

Cuando termine de configurar Braze en su proveedor de identidad, éste le proporcionará una URL de destino y un certificado `x.509` para que los introduzca en su cuenta Braze.

Después de que su administrador de cuenta active SAML SSO para su cuenta, vaya a **Configuración** > **Configuración de administración** > **Configuración de seguridad** y **active la** sección SAML SSO.

{% alert note %}
Si utiliza la [navegación anterior]({{site.baseurl}}/navigation), seleccione el icono de su cuenta y vaya a **Configuración de la empresa** > **Configuración de seguridad** para encontrar la sección SAML SSO.
{% endalert %}

En la misma página, introduce lo siguiente:

| Requisito | Detalles |
|---|---|
| `SAML Name` | Aparecerá como texto del botón en la pantalla de inicio de sesión.<br>Suele ser el nombre de tu proveedor de identidad, como "Okta". |
| `Target URL` | Se proporciona después de configurar Braze en tu IdP.<br> Algunos IdP hacen referencia a esto como URL de SSO o punto final de SAML 2.0. |
| `Certificate` | El certificado `x.509` proporcionado por su proveedor de identidad.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Asegúrese de que su certificado `x.509` sigue este formato cuando lo añada al panel de control:

```
-----BEGIN CERTIFICATE-----
<certificate>
-----END CERTIFICATE-----
```

![Abrir la configuración de seguridad y añadir detalles de SAML SSO]({% image_buster /assets/img/samlsso.gif %})

### Paso 3: Iniciar sesión en Braze

Guarde su configuración de seguridad y cierre la sesión. A continuación, vuelve a iniciar sesión con tu proveedor de identidad.

![Pantalla de inicio de sesión con SSO habilitado]({% image_buster /assets/img/sso1.png %}){: style="max-width:40%;"}

## Comportamiento del SSO

Los miembros que opten por utilizar el SSO ya no podrán utilizar su contraseña como antes. Los usuarios que sigan utilizando su contraseña podrán a menos que estén restringidos por los siguientes ajustes.

## Restricción

Puedes restringir que los miembros de tu organización solo inicien sesión con Google SSO o SAML SSO. Para activar las restricciones, vaya a **Configuración de seguridad** y seleccione **Aplicar inicio de sesión solo con Google SSO** o **Aplicar inicio de sesión solo con SAML SSO personalizado**.

![Sección Reglas de autenticación de la página Configuración de seguridad]({% image_buster /assets/img/sso3.png %})

Al activar las restricciones, los usuarios de Braze de su empresa ya no podrán iniciar sesión utilizando una contraseña, aunque hayan iniciado sesión con una contraseña anteriormente.

## Obtener una traza SAML

Si experimentas problemas de inicio de sesión relacionados con el SSO, obtener un rastreo SAML puede ayudarte a solucionar los problemas de tu conexión SSO identificando lo que se envía en las peticiones SAML.

### Requisitos previos

Para ejecutar un rastreo SAML, necesitarás un rastreador SAML. Aquí tienes dos opciones posibles según tu navegador:

- [Google Chrome](https://chromewebstore.google.com/detail/saml-tracer/mpdajninpobndbfcldcmbpnnbhibjmch)
- [Mozilla Firefox](https://addons.mozilla.org/en-US/firefox/addon/saml-tracer/)

### Paso 1: Abre el rastreador SAML

Selecciona el rastreador SAML en la barra de navegación de tu navegador. Asegúrate de que no está seleccionada la opción **Pausa**, ya que esto impedirá que el rastreador SAML capture lo que se envía en las solicitudes SAML. Cuando el rastreador SAML esté abierto, verás que rellena el rastreo.

![Rastreador SAML para Google Chrome.]({% image_buster /assets/img/saml_tracer_example.png %})

### Paso 2: Iniciar sesión en Braze mediante SSO

Ve a tu panel de Braze e intenta iniciar sesión mediante SSO. Si encuentras un error, abre el rastreador SAML e inténtalo de nuevo. Un rastreo SAML se ha recopilado correctamente si hay una fila con una URL como `https://dashboard-XX.braze.com/auth/saml/callback` y una etiqueta SAML naranja.

### Paso 3: Exportar y enviar a Braze

Selecciona **Exportar**. Para **Seleccionar perfil de filtrado de cookies**, selecciona **Ninguno**. A continuación, selecciona **Exportar**. Esto generará un archivo JSON que puedes enviar al soporte de Braze para una mayor solución de problemas.

![Menú "Exportar preferencias de rastreo SAML" con la opción "Ninguna" seleccionada.]({% image_buster /assets/img/export_saml_trace_preferences.png %})
