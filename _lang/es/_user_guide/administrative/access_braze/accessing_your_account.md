---
nav_title: Acceder a tu cuenta
article_title: Acceder a tu cuenta
page_order: 2
page_type: reference
description: "Este artículo explica cómo obtener tu cuenta Braze, cómo iniciar sesión después de que se te haya concedido acceso y cómo restablecer tu contraseña Braze."

---

# Acceder a tu cuenta

> Este artículo explica cómo obtener tu cuenta Braze, cómo iniciar sesión después de que se te haya concedido acceso y cómo solucionar los problemas de acceso al panel y de rendimiento del panel.

Si eres el primer usuario de Braze en tu empresa y te conectas por primera vez, recibirás un correo electrónico de bienvenida de `@alerts.braze.com` pidiéndote que confirmes tu correo electrónico y te conectes el primer día de tu contrato.

Tras confirmar tu cuenta, puedes añadir usuarios adicionales desde la página [Usuarios de la empresa]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/adding_users_to_your_dashboard/) de tu panel. Todos los usuarios recibirán un correo electrónico pidiéndoles que confirmen su cuenta después de haber sido añadidos.

Si no eres el primer usuario de la cuenta Braze de tu empresa, ponte en contacto con el administrador de la cuenta Braze de tu empresa y pídele que cree tu cuenta. A continuación, recibirás un correo electrónico de bienvenida de `@alerts.braze.com` pidiéndote que confirmes tu correo electrónico e inicies sesión.

## Iniciar sesión

Hablemos de cómo iniciar sesión, ¡ya sea la primera vez o la millonésima! Si eres el primer usuario de tu empresa, sigue las indicaciones del apartado anterior. Si no, puedes iniciar sesión después de que el administrador de Braze de tu empresa cree tu cuenta.

Puedes iniciar sesión desde el [Braze.com](https://www.braze.com) o utilizar la URL del panel que corresponde a tu [instancia de Braze]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/). Para tu comodidad, Braze tiene varias opciones de inicio de sesión único (SSO), como:

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

## Acceder a varios paneles de Braze

Braze no te permite registrar la misma dirección de correo electrónico para varios usuarios de paneles en el mismo clúster (por ejemplo, si tienes dos paneles en US-01). Puedes utilizar el mismo correo electrónico para crear cuentas en diferentes clusters (por ejemplo, si tienes un panel en US-01 y otro en US-05). Si necesitas acceder a varios paneles de Braze en el mismo clúster, puedes hacer lo siguiente:

### Utilizar alias de correo electrónico

Si tu proveedor de correo electrónico es Gmail, puedes crear alias añadiendo un signo `+` seguido de cualquier texto a tu dirección de correo electrónico. Por ejemplo:
- **Correo electrónico original:** `rocky@gmail.com`
- **Alias correo electrónico:** `rocky+1@gmail.com`

Ambas direcciones de correo electrónico dirigirán los mensajes al mismo buzón de entrada, pero Braze las reconocerá como cuentas separadas cuando te conectes.

### Crear alias separados con otros proveedores

Si tu proveedor de correo electrónico no admite el alias `+`, aún puedes crear alias distintos, como configurar `rocky@braze.com` para que se reenvíe a `rocky.lotito@braze.com`. Esto permite que varias direcciones lleguen al mismo buzón de entrada y que Braze las reconozca como correos electrónicos diferentes.

### Utilizar desarrolladores multiempresa

La característica de desarrolladores multiempresa permite compartir una única cuenta de usuario entre varias empresas. Los usuarios pueden alternar entre distintos paneles de empresa desde el menú de su perfil de usuario.

Si tienes SSO y quieres habilitar desarrolladores multiempresa, tienes que habilitar un ID de entidad SAML personalizado configurando una integración SAML SSO personalizada. Sigue los pasos de la [sesión iniciada por el proveedor de servicios (SP)]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/), pero aplica estos cambios:
- Cambia **el ID de entidad** a `braze_dashboard_<companyID>` para cada integración de panel.
- Ponte en contacto con tu administrador del éxito del cliente o director de cuentas para habilitar la función `saml_sso_custom_entity_id` para cada panel.

### Consideraciones para el inicio de sesión único (SSO)

Si utilizas el inicio de sesión único (SSO), ten en cuenta que tener varias direcciones de correo electrónico diferentes puede dar lugar a complicaciones. Confirma que tu configuración SSO es correcta para evitar problemas de acceso.

## Solución de problemas

### Restablecer tu contraseña

Para restablecer tu contraseña, selecciona el enlace **¿Has olvidado tu contraseña?** en la página de inicio de sesión del panel. Se te pedirá que introduzcas tu correo electrónico para recibir un enlace para restablecer tu contraseña.

\![Iniciar sesión en el panel con la pregunta "¿Has olvidado tu contraseña?".]({% image_buster /assets/img_archive/enable_reset.png %}){: style="max-width:60%"}

### Borrar la caché y las cookies de tu navegador

Si tienes problemas con el rendimiento del panel, como que no se cargue el panel o la lista de rendimiento de los segmentos, intenta borrar la caché y las cookies de tu navegador siguiendo los pasos para tu navegador respectivo.

{% alert important %}
Al borrar las cookies se cerrará tu sesión, por lo que se perderá el trabajo no guardado.
{% endalert %}

- [Borrar caché & cookies en Chrome](https://support.google.com/accounts/answer/32050?hl=en&co=GENIE.Platform%3DDesktop)
- [Borrar cookies en Safari en Mac](https://support.apple.com/en-gb/guide/safari/sfri11471/16.1/mac/13.0)
- [Borrar cookies y datos del sitio en Firefox](https://support.mozilla.org/en-US/kb/clear-cookies-and-site-data-firefox)
- [Eliminar todas las cookies en Microsoft Edge](https://support.microsoft.com/en-us/windows/manage-cookies-in-microsoft-edge-view-allow-block-delete-and-use-168dab11-0753-043d-7c16-ede5947fc64d#bkmk_deleteallcookies)

Si al borrar la caché y las cookies de tu navegador no se resuelven tus problemas, ponte en contacto con [el servicio de asistencia]({{site.baseurl}}/support_contact/).

### Acceder al editor de arrastrar y soltar

Para la mayoría de los usuarios de Braze, debería cargarse el editor de arrastrar y soltar. Sin embargo, si utilizas una VPN o estás detrás de un cortafuegos, puede que tengas que permitir un dominio. Ponte en contacto con tu administrador informático para comprobar que `*.bz-rndr.com` está en la lista de permitidos.

El editor puede experimentar problemas de carga debido a lo siguiente:

- **Error transitorio:** Son fallos temporales que pueden afectar a la conectividad, la comunicación o la transferencia de datos. Afortunadamente, suelen resolverse por sí solas sin requerir una intervención importante, ya que suelen estar causadas por afecciones de corta duración y no indican problemas sistémicos.
- **Error grave:** Puede tratarse de un problema de infraestructura o de producto.  Puedes consultar nuestra [página sobre el estado del sistema Braze](https://braze.statuspage.io/), ya que probablemente seamos conscientes de la situación y estemos trabajando activamente para resolverla.

{% alert important %}
Si sigues teniendo problemas, [abre un ticket de soporte]({{site.baseurl}}/user_guide/administrative/access_braze/support/). Antes de hacerlo, comprueba que tu administrador informático ha confirmado que `*.bz-rndr.com` está en la lista de permitidos de tu sistema.
{% endalert %}

### Acceder a Braze Learning

Si tienes problemas para iniciar sesión en Braze Learning y te encuentras atrapado en un bucle que te redirige al panel, sigue estos pasos:

1. Si tienes varias cuentas de Braze, al iniciar sesión con la cuenta incorrecta dos veces se te enviará al panel de Braze. Confirma que estás accediendo a la cuenta correcta. 
2. Si tienes un bloqueador de anuncios, confirma que está desactivado. Puede bloquear las cookies necesarias para la funcionalidad de inicio de sesión único.
3. Ve a Configuración de la empresa > Configuración de seguridad y comprueba que el inicio de sesión único (SSO) está activado.
4. Confirma que el perfil de usuario de tu panel incluye nombre y apellidos. No tener un apellido puede interrumpir el proceso de iniciar sesión.
5. Accede a Braze Learning desde tu panel yendo a **Soporte** > Braze Learning. 
6. Si sigues teniendo problemas, considera la posibilidad de volver a crear tu cuenta. Los usuarios que accedieron a Braze Learning durante la fase de prueba gratuita pueden tener dificultades para acceder ahora.

### Problemas de autenticación de dos factores (2FA)

Si un usuario tiene problemas con la autenticación de dos factores (2FA) y no puede acceder al panel de Braze, puede deberse a varias razones. Lo más habitual es que ya no tengan acceso al número de teléfono registrado o al dispositivo en el que está instalada la aplicación Authy.

Un administrador debe restablecer el 2FA para el usuario afectado haciendo lo siguiente: 

1. Ve a **Gestionar usuarios**.
2. Selecciona **Editar usuario** para el usuario que experimenta problemas con 2FA.
3. Elige la opción de Restablecer 2FA.
4. Confirma el restablecimiento 2FA cuando se te solicite.
5. Si el restablecimiento no resuelve inmediatamente el problema, borra las cookies y la memoria caché.

Braze no puede restablecer la 2FA en nombre de los usuarios por motivos de seguridad, así que si el administrador no puede restablecer la 2FA, debe crearse un ticket de soporte.

#### Consideraciones

- Si se aplica la 2FA a nivel de empresa: Tras el restablecimiento, se pedirá al usuario que vuelva a configurar su 2FA la próxima vez que se conecte.
- Si la 2FA no se aplica a nivel de empresa: El usuario iniciará sesión en el panel sin necesidad de volver a configurar la 2FA. Si desean habilitar la 2FA, pueden hacerlo en Configuración de la cuenta.

{% alert note %}
Este proceso de restablecimiento también se aplica a los usuarios a los que se les ha bloqueado la cuenta por haber solicitado demasiados tokens en la última hora.
{% endalert %}