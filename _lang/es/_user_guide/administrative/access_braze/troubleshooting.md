---
nav_title: Solución de problemas
article_title: Solución de problemas Braze Access
page_order: 8
page_type: reference
description: "Este artículo te guía en la solución de problemas que puedas tener al intentar acceder a Braze."

---

# Solución de problemas de acceso Braze

> Este artículo te ayuda a solucionar los problemas que puedas tener al intentar acceder a Braze.

## Bloqueo de la cuenta

Si no puedes acceder a tu cuenta Braze, ¡no te preocupes! Podemos ayudarte a volver a entrar.	

Puedes saber qué tipo de bloqueo estás experimentando por el mensaje de error que recibes:	

- [Veo un error sobre mi contraseña.](#password-error)	
- [No veo ningún error, pero Braze sigue sin dejarme entrar.](#instance-error)	
- [Veo un error sobre la suspensión de la cuenta.](#account-suspension)	

### Error de contraseña

La seguridad de tu cuenta es importante para nosotros, por lo que se requieren contraseñas para acceder a tu cuenta de Braze.	
- Comprueba que estás accediendo a la [instancia]({{site.baseurl}}/user_guide/administrative/access_braze/braze_instances/#braze-instances) correcta [del panel de Braze]({{site.baseurl}}/user_guide/administrative/access_braze/braze_instances/#braze-instances). Compruébalo con tu administrador de cuentas o director de cuentas de Braze.	
- Es posible que tu contraseña haya caducado, por lo que tendrás que [restablecerla]({{site.baseurl}}/user_guide/administrative/access_braze/accessing_your_account/#resetting-your-password).	
- Si utilizas un servicio de [inicio de sesión único]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/), comprueba con el administrador de tu cuenta que la configuración se ha realizado correctamente.	
- Si tu empresa está en varias instancias de Braze, puede que estés utilizando el correo electrónico incorrecto para iniciar sesión.  	

En caso de duda, siempre puedes [restablecer tu contraseña]({{site.baseurl}}/user_guide/administrative/access_braze/accessing_your_account/#resetting-your-password).	

### Error de instancia

Si utilizas la misma máquina que usas habitualmente para conectarte, Braze debería detectar automáticamente la instancia correcta. Sin embargo, en caso de que no sea así o de que te conectes por primera vez, te recomendamos que tengas en cuenta lo siguiente:	

- Comprueba que estás accediendo a la [instancia]({{site.baseurl}}/user_guide/administrative/access_braze/braze_instances/#braze-instances) correcta [del panel de Braze]({{site.baseurl}}/user_guide/administrative/access_braze/braze_instances/#braze-instances). Compruébalo con tu administrador de cuentas o director de cuentas de Braze.
- Si tu empresa está en varias instancias de Braze, puede que estés utilizando el correo electrónico incorrecto para iniciar sesión.	

### Suspensión de la cuenta	

Esto no ocurre muy a menudo, pero nos tomamos muy en serio la suspensión y eliminación de cuentas. Si te encuentras con este error, te recomendamos que te pongas en contacto con el administrador de Braze de tu empresa, con el director de cuentas de Braze o con [Soporte][support].

## El panel de Braze no se carga ni funciona como se esperaba

En primer lugar, comprueba si el panel se carga en otro navegador. Si el problema no persiste en otro navegador, prueba lo siguiente:

- **Vuelve a lanzar el panel:** Cierra la sesión, sal del navegador e intenta acceder a tu panel.
- **Actualiza tu navegador local:** [Borra las cookies y la memoria caché de tu navegador]({{site.baseurl}}/user_guide/administrative/access_braze/accessing_your_account/#browser-cache-and-cookies), e intenta acceder de nuevo a tu panel.
- **Utiliza plugins compatibles o herramientas de terceros:** Los bloqueadores de anuncios o el software de seguridad pueden impedir que se cargue el panel de Braze. Pruébalo desactivando un bloqueador de anuncios y, a continuación, accediendo a tu panel de Braze.
        \- También puedes comprobar los registros de la consola de tu navegador. Los errores relacionados con `ERR_BLOCKED_BY_CLIENT` pueden indicar que el contenido está bloqueado por un bloqueador de anuncios.
- **Comprueba la calidad de tu conexión:** Puede que la calidad de tu conexión sea mala. Intenta iniciar sesión en tu panel de Braze en un dispositivo diferente.
- **Confirma que estás accediendo al cluster correcto:** Asegúrate de que estás accediendo al clúster asignado a tu empresa. Por ejemplo, puedes estar asignado a US-03, pero estás entrando en US-01.
- **Actualiza tu navegador:** Actualiza tu navegador a la última versión [compatible]({{site.baseurl}}/user_guide/administrative/access_braze/accessing_your_account/#supported-browsers) e intenta acceder a tu panel.

Si el problema se produce en todos los navegadores, prueba lo siguiente:

- **Comprueba tu conexión de red:** Intenta desactivar tu VPN, si es posible, o desactiva y vuelve a activar tu conexión de red.
- **Reinicia tu dispositivo:** Prueba a iniciar sesión en tu panel de Braze después de reiniciar el dispositivo.

Si has resuelto los problemas anteriores y tu panel sigue sin cargarse o no funciona como esperabas, ponte en contacto con [el servicio de asistencia]({{site.baseurl}}/braze_support/).

## El usuario no pertenece a ningún espacio de trabajo

Compruébalo yendo a **Configuración** > **Usuarios de la empresa** y comprobando los permisos a nivel de espacio de trabajo del usuario. Añade los espacios de trabajo necesarios a **Espacios de trabajo**.

## Solución de problemas como nuevo usuario

Si eres un nuevo usuario de Braze y tienes problemas para iniciar sesión o acceder a tu cuenta por primera vez, sigue estos pasos para resolver los problemas más comunes:

### Nunca he recibido el correo electrónico de bienvenida

- Comprueba tu carpeta de correo no deseado: Confirma que el correo electrónico de activación de la cuenta no se ha filtrado en tu carpeta de correo no deseado.
- Verifica tu dirección de correo electrónico: Haz que tu administrador compruebe la dirección de correo electrónico asociada a tu nueva cuenta Braze para confirmar que es correcta.
- Políticas informáticas: Confirma con tu equipo de TI que no existen políticas que puedan impedir la recepción del correo electrónico de activación.

### He recibido el correo electrónico, pero estoy atascado configurando la autenticación de dos factores (2FA).

- Restablecer 2FA: Si tienes problemas para configurar la 2FA, tu administrador puede restablecer la 2FA para tu cuenta de usuario en la configuración.
- Volver a añadir usuario: Si los problemas persisten, el administrador puede eliminar tu cuenta de usuario del panel y volver a añadirte. Esto permite crear el usuario con los mismos datos.

Si los problemas continúan después de estos pasos, ponte en contacto con [el servicio de asistencia]({{site.baseurl}}/braze_support/) para obtener más ayuda.