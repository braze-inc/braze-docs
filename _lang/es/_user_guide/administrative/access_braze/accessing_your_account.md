---
nav_title: Acceder a tu cuenta
article_title: Acceder a tu cuenta
page_order: 2
page_type: reference
description: "Este artículo explica cómo obtener una cuenta Braze, cómo iniciar sesión una vez obtenido el acceso y cómo restablecer la contraseña Braze."

---

# Acceder a tu cuenta

> Este artículo explica cómo obtener tu cuenta Braze, cómo iniciar sesión después de que se te haya concedido acceso y cómo solucionar los problemas de acceso al panel y de rendimiento del panel.

Si es el primer usuario de Braze en su empresa y se conecta por primera vez, recibirá un correo electrónico de bienvenida de `@alerts.braze.com` en el que se le pedirá que confirme su correo electrónico y se conecte el primer día de su contrato.

Tras confirmar tu cuenta, puedes añadir usuarios adicionales desde la página [Usuarios de la empresa]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/adding_users_to_your_dashboard/) de tu panel. Todos los usuarios recibirán un correo electrónico pidiéndoles que confirmen su cuenta después de haber sido añadidos.

Si no eres el primer usuario de la cuenta Braze de tu empresa, ponte en contacto con el administrador de la cuenta Braze de tu empresa y pídele que cree tu cuenta. A continuación, recibirás un correo electrónico de bienvenida de `@alerts.braze.com` en el que se te pedirá que confirmes tu dirección de correo electrónico e inicies sesión.

## Inicio de sesión

Hablemos de cómo iniciar sesión, ¡ya sea la primera vez o la millonésima! Si usted es el primer usuario de su empresa, siga las indicaciones de la sección anterior. Si no, puedes iniciar sesión después de que el administrador de Braze de tu empresa cree tu cuenta.

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

## Solución de problemas

### Restablecer la contraseña

Para restablecer tu contraseña, selecciona el enlace **¿Has olvidado tu contraseña?** en la página de inicio de sesión del panel. Se te pedirá que introduzcas tu correo electrónico para recibir un enlace para restablecer tu contraseña.

![Iniciar sesión en el panel con la pregunta "¿Has olvidado tu contraseña?".]({% image_buster /assets/img_archive/enable_reset.png %}){: style="max-width:60%"}

### Borrar la caché y las cookies de tu navegador

Si tienes problemas con el rendimiento del panel, como que no se cargue el panel o la lista de rendimiento de los segmentos, intenta borrar la caché y las cookies de tu navegador siguiendo los pasos para tu navegador respectivo.

{% alert important %}
Al borrar las cookies se cerrará tu sesión, por lo que se perderá el trabajo no guardado.
{% endalert %}

- [Borrar caché y cookies en Chrome](https://support.google.com/accounts/answer/32050?hl=en&co=GENIE.Platform%3DDesktop)
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
Si sigues teniendo problemas, [abre un ticket de soporte]({{site.baseurl}}/user_guide/administrative/access_braze/support/). Antes de hacerlo, comprueba que tu administrador informático ha confirmado que `*.bz-rndr.com` está incluido en tu lista de permitidos.
{% endalert %}

