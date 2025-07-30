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
| Clave API RelayState | Ve a **Configuración** > **Claves de API** y crea una clave de API con permisos `sso.saml.login`, y luego introduce la clave de API generada como parámetro `RelayState` dentro de tu IdP. Para conocer los pasos detallados, consulta [Configurar tu RelayState](#setting-up-your-relaystate). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

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

En la misma página, introduce lo siguiente:

| Requisito | Detalles |
|---|---|
| Nombre SAML | Aparecerá como texto del botón en la pantalla de inicio de sesión.<br>Suele ser el nombre de tu proveedor de identidad, como "Okta". |
| URL de destino | Se proporciona después de configurar Braze en tu IdP.<br> Algunos IdP hacen referencia a esto como URL de SSO o punto final de SAML 2.0. |
| Certificado | El certificado `x.509` proporcionado por su proveedor de identidad.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Asegúrese de que su certificado `x.509` sigue este formato cuando lo añada al panel de control:

```
-----BEGIN CERTIFICATE-----
<certificate>
-----END CERTIFICATE-----
```

![Configuración de SAML SSO con el alternador seleccionado.]({% image_buster /assets/img/samlsso.png %})

### Paso 3: Iniciar sesión en Braze

Guarde su configuración de seguridad y cierre la sesión. A continuación, vuelve a iniciar sesión con tu proveedor de identidad.

![Pantalla de inicio de sesión con SSO habilitado]({% image_buster /assets/img/sso1.png %}){: style="max-width:60%;"}

## Configuración de tu RelayState

1. En Braze, ve a **Configuración** > **API e identificadores**.
2. En la pestaña **Claves de API**, selecciona el botón **Crear clave de API**.
3. En el campo **Nombre de la clave de API**, introduce un nombre para tu clave.
4. Amplía el desplegable **SSO** en **Permisos** y marca **sso.saml.login**.<br><br>![La sección "Permisos" con sso.saml.login marcado.]({% image_buster /assets/img/relaystate_troubleshoot.png %}){: style="max-width:70%;"}<br><br>
5. Selecciona **Crear clave de API**.
6. En la pestaña **Claves de API**, copia el identificador que aparece junto a la clave de API que has creado.
7. Pega la clave de API RelayState en el RelayState de tu IdP (también puede aparecer como "Estado de retransmisión" o "Estado de retransmisión predeterminado" en función de tu IdP).

## Comportamiento del SSO

Los miembros que opten por utilizar el SSO ya no podrán utilizar su contraseña como antes. Los usuarios que sigan utilizando su contraseña podrán a menos que estén restringidos por los siguientes ajustes.

## Restricción

Puedes restringir que los miembros de tu organización solo inicien sesión con Google SSO o SAML SSO. Para activar las restricciones, vaya a **Configuración de seguridad** y seleccione **Aplicar inicio de sesión solo con Google SSO** o **Aplicar inicio de sesión solo con SAML SSO personalizado**.

![Ejemplo de configuración de la sección "Reglas de autenticación" con una longitud mínima de contraseña de 8 caracteres y reutilización de contraseña 3 veces. Las contraseñas caducarán a los 180 días, y los usuarios se desconectarán tras 1.440 minutos de inactividad.]({% image_buster /assets/img/sso3.png %})

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

## Solución de problemas

### ¿Está correctamente configurada la dirección de correo electrónico del usuario?

Si recibes el error `ERROR_CODE_SSO_INVALID_EMAIL`, la dirección de correo electrónico del usuario no es válida. Confirma en el rastreo SAML que el campo `saml2:Attribute Name="email"` coincide con la dirección de correo electrónico que el usuario está utilizando para iniciar sesión. Si utilizas Microsoft Entra ID (antes Azure Active Directory), el mapeado de atributos es `email = user.userprincipalname`.

La dirección de correo electrónico distingue entre mayúsculas y minúsculas y debe coincidir exactamente con la que se configuró en Braze, incluida la configurada en tu proveedor de identidad (como Okta, OneLogin, Microsoft Entra ID y otros).

Otros errores que indican que tienes problemas con la dirección de correo electrónico del usuario son:
- `ERROR_CODE_SSO_EMAIL_DOES_NOT_EXIST`: La dirección de correo electrónico del usuario no está dentro del panel.
- `ERROR_CODE_SSO_SESSION_SIGN_IN_EMAIL_MISSING`: La dirección de correo electrónico del usuario está vacía o mal configurada.
- `ERROR_CODE_SSO_SESSION_SIGN_IN_EMAIL_MISMATCH` o `ERROR_CODE_SSO_SIGN_IN_EMAIL_MISMATCH`: La dirección de correo electrónico del usuario no coincide con la utilizada para configurar el SSO.

### ¿Tienes un certificado SAML válido (x.509 certificate)?

Puedes validar tu certificado SAML utilizando [esta herramienta de validación SAML](https://www.samltool.com/validate_response.php). Ten en cuenta que un certificado SAML caducado es también un certificado SAML no válido.

### ¿Has subido un certificado SAML correcto (x.509 certificate)?

Confirma que el certificado de la sección `ds:X509Certificate` del rastreo SAML coincide con el que subiste a Braze. Esto no incluye la cabecera `-----BEGIN CERTIFICATE-----` y el pie `-----END CERTIFICATE-----`.

### ¿Has escrito o formateado mal tu certificado SAML (x.509 certificate)?

Confirma que no hay espacios en blanco ni caracteres adicionales en el certificado que enviaste en el panel de Braze.

Cuando introduzcas tu certificado en Braze, es necesario que esté codificado con Privacy Enhanced Mail (PEM) y formateado correctamente (incluyendo la cabecera `-----BEGIN CERTIFICATE-----` y el pie de página `-----END CERTIFICATE-----` ). 

Aquí tienes un ejemplo de certificado con el formato correcto:

```
-----BEGIN CERTIFICATE-----
THIS_IS_A_MOCKED_CERTIFICATE_4ysJLTzETANBgkqhkiG9w0BAQsFADA0MTIwMAYDVQQDEylNaWNyb3NvZnQgQXp1cmUgRmVkZXJhdGVkIFNTTyBDZXJ0aWZpY2F0ZTAeFw0yMjA1MjcwOTA4MzFaFw0yNTAbMjcwOTA4MzFaMDQxMjAwBgNVBAMTKU1pY3Jvca9mdCBBenVyZSBGZWRlcmF0ZWQgU1NPIENlcnAFWAOKGPAWIGKJPOAMWANBgkqhkiG9w0BAQEFAAaCAQ8AMIIBCgKCAQEA1+KFJwxoac6jdFztQd+vQu59qM8rgfX5RICk0ODfpXkuDUNudcI0XmOAkKHRoMNPYlmMEf5NSiZ7TMElEPtK9zZlpAoSchxxC0Ndegc1AMFi7i2BsEIqPwrer0G6kx2vuAjdrDROPPafkmwalkfmklaw23FlYmV7doE0Vrj2WxR1PG0eFAdsxPLsO1ny55fPj2ibwaqc0XpDkfTrO9GnFvmZAS8ebYtLZsYAMAGLKWAMLGKAWMLKMFDW6vBDaK290s9FdaWza3GPHTcDstawRhyqbXpVjiqpQ0mtxANW4WduSiohhpeqv05TlSOhx87QalkfmwalfmAWMFLKQEBCwUAA4IBAQBdZ5E9FqICfL1q+G6D1tChKl1Y6I6IVULQb4LESSJRaxv53nakmflwakmMALKFMWOYKAeUWO2hdED54qGMgUnLL6YheQBrsm6ilBC68F7ZFmIzVKycvw65yamWbTMi2f2lF60GNYMrq8sGQUkgO0O2zTN07J9wGTe9M+MAFLKWAMFLKalkmflkawoij4jpcsLXXFZJoHSXnF3+qQuzu+49D6pR2lF7DDW+5+PRoc1QpDSytdXxWzItsjQ6IFRuvIGsbrMg0FVaze7ePdKrc47wSlElno7SQ0H+6g40q25rsDSLO
-----END CERTIFICATE-----
```

### ¿Es válido el token de sesión del usuario?

Haz que el usuario afectado [borre la caché y las cookies de su navegador](https://its.uiowa.edu/services/how-clear-cache-and-cookies-your-web-browser) y, a continuación, vuelva a intentar iniciar sesión con SAML SSO.

### ¿Has configurado tu RelayState?

Si recibes el error `ERROR_CODE_SSO_INVALID_RELAY_STATE`, tu RelayState podría estar mal configurado o ser inexistente. Si aún no lo has hecho, tienes que configurar tu RelayState en tu sistema de gestión de IdP. Para conocer los pasos, consulta [Configurar tu RelayState](#setting-up-your-relaystate). 

### ¿Está el usuario atrapado en un bucle de inicio de sesión entre Okta y Braze?

Si un usuario no puede iniciar sesión porque está bloqueado entre el SSO de Okta y el panel de Braze, tienes que ir a Okta y establecer el destino de la URL SSO en tu [instancia de Braze]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/) (por ejemplo, `https://dashboard-07.braze.com`). 

Si utilizas otro IdP, comprueba si tu empresa ha cargado en Braze el certificado SAML o x.509 correcto.

### ¿Estás utilizando una integración manual?

Si tu empresa no ha descargado la aplicación Braze de la tienda de aplicaciones de tu IdP, tienes que descargar la integración preconstruida. Por ejemplo, si Okta es tu IdP, descargarías la aplicación Braze desde su [página de integración](https://www.okta.com/integrations/braze/).
