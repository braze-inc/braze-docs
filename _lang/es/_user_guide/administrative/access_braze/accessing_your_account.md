---
nav_title: Accede a tu cuenta
article_title: Accede a tu cuenta
page_order: 0
page_type: reference
description: "Este artículo explica cómo obtener una cuenta Braze, cómo iniciar sesión una vez obtenido el acceso y cómo restablecer la contraseña Braze."

---

# Accede a tu cuenta

> Este artículo explica cómo obtener tu cuenta de Braze, cómo iniciar sesión una vez que se te haya concedido el acceso y cómo realizar la solución de problemas relacionada con el acceso al panel de control y su rendimiento.

Si es el primer usuario de Braze en su empresa y se conecta por primera vez, recibirá un correo electrónico de bienvenida de `@alerts.braze.com` en el que se le pedirá que confirme su correo electrónico y se conecte el primer día de su contrato.

Después de confirmar tu cuenta, puedes añadir usuarios adicionales desde la página [Usuarios de la empresa]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/) de tu panel. Todos los usuarios recibirán un correo electrónico pidiéndoles que confirmen su cuenta después de haber sido añadidos.

Si no eres el primer usuario de la cuenta Braze de tu empresa, ponte en contacto con el administrador de la cuenta Braze de tu empresa y pídele que cree tu cuenta. A continuación, recibirás un correo electrónico de bienvenida de `@alerts.braze.com` en el que se te pedirá que confirmes tu dirección de correo electrónico e inicies sesión.

## Inicio de sesión

Hablemos sobre cómo iniciar sesión, tanto si es la primera vez como si es la millonésima. Si usted es el primer usuario de su empresa, siga las indicaciones de la sección anterior. Si no es así, puedes iniciar sesión después de que el administrador de Braze de tu empresa cree tu cuenta.

Puedes iniciar sesión desde el sitio [Braze.com](https://www.braze.com) o utilizar la URL del panel que corresponda a tu [instancia de Braze]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/) específica. Para tu comodidad, Braze tiene varias opciones de inicio de sesión único (SSO), como:

* [SAML SSO]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/)
    * [Aprovisionamiento justo a tiempo SAML]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/saml_jit/)
* [Microsoft Entra SSO]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/entra/)
* [Okta]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/okta/)
* [OneLogin]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/onelogin/)

{% alert note %}
Después de iniciar sesión en Braze con SSO, ya no podrás utilizar tu contraseña para iniciar sesión en el panel.
{% endalert %}

## Navegadores compatibles

El panel de Braze es compatible con los siguientes navegadores:
- Chrome (versión 87 o posterior)
- Firefox (versión 85 o posterior)
- Safari (versión 15.4 o posterior)
- Edge (versión 87 o posterior)

Si tu panel de Braze dice que tienes un error inesperado y la herramienta de la consola de tu navegador muestra el error `ReferenceError: structuredClone is not defined`, tu navegador no está actualizado. Si este error se repite, desinstala y vuelve a instalar tu navegador.

## Acceso a varios paneles de Braze

Braze no permite el registro de la misma dirección de correo electrónico para varios usuarios del panel de control en el mismo clúster (por ejemplo, si tienes dos paneles de control en US-01). Puedes utilizar el mismo correo electrónico para crear cuentas en diferentes clústeres (por ejemplo, si tienes un panel en US-01 y otro en US-05). Si necesitas acceder a varios paneles de Braze en el mismo clúster, puedes hacer lo siguiente:

### Usar alias de correo electrónico

Si tu proveedor de correo electrónico es Gmail, puedes crear alias añadiendo un`+`signo seguido de cualquier texto a tu dirección de correo electrónico. Por ejemplo:
- **Correo electrónico original:** `rocky@gmail.com`
- **Correo electrónico alias:** `rocky+1@gmail.com`

Ambas direcciones de correo electrónico dirigirán los mensajes al mismo buzón de entrada, pero Braze las reconocerá como cuentas independientes cuando iniciéis sesión.

### Crea alias separados con otros proveedores.

Si tu proveedor de correo electrónico no admite`+`  alias, puedes crear alias independientes, como configurar`rocky@braze.com`  para reenviar a `rocky.lotito@braze.com`. Esto permite que varias direcciones se canalicen a la misma bandeja de entrada, al tiempo que Braze las reconoce como correos electrónicos diferentes.

### Utilizar desarrolladores de varias empresas

La característica de desarrolladores multiempresa permite compartir una sola cuenta de usuario entre varias empresas. Los usuarios pueden alternar entre los diferentes paneles de control de la empresa desde el menú de su perfil de usuario.

Si tienes SSO y deseas configurar desarrolladores de varias empresas, debes habilitar un ID de entidad SAML personalizado configurando una integración SAML SSO personalizada. Sigue los pasos del [inicio de sesión iniciado por el proveedor de servicios (SP)]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/), pero aplica estos cambios:
- Cambia **el ID de entidad** a`braze_dashboard_<companyID>`  para cada integración del panel de control.
- Ponte en contacto con tu administrador del éxito del cliente o director de cuentas para habilitar la`saml_sso_custom_entity_id`característica flipper en cada panel.

### Consideraciones sobre el inicio de sesión único (SSO)

Si utilizas el inicio de sesión único (SSO), ten en cuenta que tener varias direcciones de correo electrónico diferentes podría dar lugar a complicaciones. Confirma que la configuración de SSO sea correcta para evitar problemas de acceso.

## Solución de problemas

### Restablecer la contraseña

Para restablecer tu contraseña, selecciona el enlace **¿Has olvidado tu contraseña?** en la página para iniciar sesión en el panel. Se te pedirá que introduzcas tu correo electrónico para recibir un enlace para restablecer tu contraseña.

![Iniciar sesión en el panel con el mensaje «¿Has olvidado tu contraseña?».]({% image_buster /assets/img_archive/enable_reset.png %}){: style="max-width:60%"}

### Borrar la caché y las cookies del navegador

Si tienes problemas con el rendimiento del panel, como que no se cargue el panel o la lista de rendimiento de los segmentos, intenta borrar la caché y las cookies de tu navegador siguiendo los pasos para tu navegador respectivo.

{% alert important %}
Al borrar las cookies se cerrará tu sesión, por lo que se perderá el trabajo no guardado.
{% endalert %}

- [Borrar las &cookies de la caché en Chrome](https://support.google.com/accounts/answer/32050?hl=en&co=GENIE.Platform%3DDesktop)
- [Borrar cookies en Safari en Mac](https://support.apple.com/en-gb/guide/safari/sfri11471/16.1/mac/13.0)
- [Borrar cookies y datos del sitio en Firefox](https://support.mozilla.org/en-US/kb/clear-cookies-and-site-data-firefox)
- [Eliminar todas las cookies en Microsoft Edge](https://support.microsoft.com/en-us/windows/manage-cookies-in-microsoft-edge-view-allow-block-delete-and-use-168dab11-0753-043d-7c16-ede5947fc64d#bkmk_deleteallcookies)

Si al borrar la caché y las cookies de tu navegador no se resuelven tus problemas, ponte en contacto con [el servicio de asistencia]({{site.baseurl}}/support_contact/).

### Acceder al editor de arrastrar y soltar

Para la mayoría de los usuarios de la empresa, debería cargarse el editor de arrastrar y soltar. Sin embargo, si utilizas una VPN o estás detrás de un cortafuegos, es posible que tengas que añadir un dominio a la lista de permitidos. Ponte en contacto con tu administrador de TI para comprobar que`*.bz-rndr.com`  está en la lista de permitidos.

El editor puede experimentar problemas de carga debido a lo siguiente:

- **Error transitorio:** Se trata de fallos temporales que pueden afectar a la conectividad, la comunicación o la transferencia de datos. Afortunadamente, suelen resolverse por sí solos sin necesidad de una intervención significativa, ya que a menudo son causados por afecciones de corta duración y no indican problemas sistémicos.
- **Error grave:** Esto puede implicar un problema subyacente de infraestructura o de producto.  Puedes consultar nuestra [página del estado del sistema Braze,](https://braze.statuspage.io/) ya que probablemente estemos al tanto de la situación y trabajando activamente para resolverla.

{% alert important %}
Si sigues teniendo problemas, [abre un ticket de soporte]({{site.baseurl}}/user_guide/administrative/access_braze/support/). Antes de hacerlo, comprueba que tu administrador de TI haya confirmado que`*.bz-rndr.com`  está incluido en la lista de permitidos por tu parte.
{% endalert %}

### Acceso a Braze Learning

Si tienes problemas para iniciar sesión en Braze Learning y te encuentras atrapado en un bucle que te redirige al panel, sigue estos pasos:

1. Si tienes varias cuentas de Braze, si inicias sesión dos veces con la cuenta incorrecta, se te redirigirá al panel de Braze. Confirma que estás iniciando sesión en la cuenta correcta. 
2. Si tienes un bloqueador de anuncios, comprueba que esté desactivado. Puede bloquear las cookies necesarias para la funcionalidad de inicio de sesión único.
3. Ve a Configuración de la empresa > Configuración de seguridad y comprueba que el inicio de sesión único (SSO) está activado.
4. Confirma que tu perfil de usuario del panel incluye tanto el nombre como los apellidos. No tener apellido puede interrumpir el proceso para iniciar sesión.
5. Accede a Braze Learning desde tu panel de control yendo a **Soporte** > **Braze Learning**. 
6. Si sigues teniendo problemas, considera la posibilidad de volver a crear tu cuenta. Es posible que los usuarios que accedieron a Braze Learning durante la fase de prueba gratuita tengan dificultades para acceder ahora.

### Problemas con la autenticación de dos factores (2FA)

Si un usuario tiene problemas con la autenticación de dos factores (2FA) y no puede acceder al panel de Braze, puede deberse a varias razones. Lo más habitual es que ya no tengan acceso al número de teléfono con registro o al dispositivo en el que está instalada la aplicación Authy.

Un administrador debe restablecer la autenticación de dos factores (2FA) para el usuario afectado haciendo lo siguiente: 

1. Ve a **Administrar usuarios**.
2. Selecciona **Editar usuario** para el usuario que tiene problemas con la autenticación de dos factores (2FA).
3. Selecciona la opción para restablecer la autenticación de dos factores (2FA).
4. Confirma el restablecimiento de la autenticación de dos factores cuando se te solicite.
5. Si el restablecimiento no resuelve el problema de inmediato, borra las cookies y el caché.

Braze no puede restablecer la autenticación de dos factores (2FA) en nombre de los usuarios por motivos de seguridad, por lo que, si el administrador no puede restablecer la 2FA, crea un ticket de soporte.

#### Consideraciones

- Si la autenticación de dos factores (2FA) se aplica a nivel de empresa: Después del restablecimiento, Braze solicita al usuario que vuelva a configurar la autenticación de dos factores la próxima vez que inicie sesión.
- Si no se aplica la autenticación de dos factores (2FA) a nivel de la empresa: El usuario iniciará sesión en el panel sin necesidad de volver a configurar la autenticación de dos factores (2FA). Si deseas habilitar la autenticación de dos factores (2FA), puedes hacerlo en la configuración de la cuenta.

{% alert note %}
Este proceso de restablecimiento también se aplica a los usuarios que han sido bloqueados de su cuenta por solicitar demasiados tokens en la última hora.
{% endalert %}