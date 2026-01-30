---
nav_title: Configuración de seguridad
article_title: Configuración de seguridad
page_order: 2
toc_headers: h2
page_type: reference
description: "Este artículo de referencia cubre la configuración genérica de seguridad entre empresas, incluidas las reglas de autenticación, las listas de IP permitidas, la PII y la autenticación de dos factores (2FA)."

---

# Configuración de seguridad

> Como administrador, la seguridad es una prioridad en tu lista de preocupaciones. La página **Configuración de seguridad** puede ayudarte a gestionar la configuración de seguridad genérica para toda la empresa, incluidas las reglas de autenticación, la lista de IP permitidas y la autenticación de dos factores.

Para acceder a esta página, vaya a **Configuración** > **Configuración de administración** > **Configuración de seguridad**.

## Normas de autenticación

### Longitud de la contraseña

Utiliza este campo para cambiar la longitud mínima requerida de la contraseña. El mínimo predeterminado es de ocho caracteres.

### Complejidad de la contraseña

Selecciona **Forzar contraseñas complejas** para exigir que las contraseñas incluyan al menos uno de los siguientes elementos: 
- Letra mayúscula
- Letra minúscula
- Número
- Carácter especial

### Reutilización de contraseñas

Determina el número mínimo de nuevas contraseñas que deben establecerse antes de que un usuario pueda reutilizar una contraseña. El valor predeterminado es tres.

### Reglas de caducidad de la contraseña

Utilice este campo para establecer cuándo desea que los usuarios de su cuenta Braze restablezcan su contraseña.

### Reglas de duración de la sesión

Utiliza este campo para definir durante cuánto tiempo Braze mantendrá activa tu sesión. Después de que Braze considere que tu sesión está inactiva (sin actividad durante el número de minutos definido), Braze cierra la sesión del usuario. El número máximo de minutos que puedes introducir es de 10.080 (igual a una semana) si en tu empresa se aplica la autenticación de dos factores; de lo contrario, la duración máxima de la sesión es de 1.440 minutos (igual a 24 horas).

### Autenticación de inicio de sesión único (SSO)

Puede restringir a sus usuarios el acceso mediante contraseña o SSO.

Para [SAML SSO]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/), los clientes deben establecer su configuración SAML antes de aplicarla. Si los clientes utilizan Google SSO, solo tienen que hacer cumplir la página de configuración de seguridad, sin ninguna elevación adicional.

## Lista de direcciones IP permitidas del panel

Utilice el campo mostrado para permitir direcciones IP y subredes específicas desde las que los usuarios pueden iniciar sesión en su cuenta (por ejemplo, desde una red de empresa o VPN). Especifique las direcciones IP y subredes como rangos CIDR en una lista separada por comas. Si no se especifica, los usuarios pueden conectarse desde cualquier dirección IP.

## Autenticación de dos factores (2FA)

La autenticación de dos factores es obligatoria para todos los usuarios de Braze. Añade un segundo nivel de verificación de identidad al registro de una cuenta, haciéndolo más seguro que un simple nombre de usuario y contraseña. Si tu panel de control no admite la autenticación de dos factores, ponte en contacto con tu gestor de éxito de clientes. 

Cuando se activa la autenticación de dos factores:

- Además de introducir una contraseña, los usuarios deben introducir un código de verificación al acceder a su cuenta de Braze. El código puede enviarse a través de una aplicación de autenticación, correo electrónico o SMS. 
- La casilla **Recordar esta cuenta durante 30 días** pasa a estar disponible para los usuarios.

Braze bloquea a los usuarios que no configuran su autenticación de dos factores desde su cuenta Braze. Los usuarios de cuentas Braze también pueden configurar la autenticación de dos factores por su cuenta en la **Configuración de la cuenta**, aunque no lo exija el administrador.

Asegúrate de guardar los cambios antes de salir de la página.

### Recuerda esta cuenta durante 30 días {#remember-me}

Esta característica está disponible cuando está activada la autenticación de dos factores.

Cuando seleccionas **Recordar esta cuenta durante 30 días**, se almacena una cookie en tu dispositivo, que sólo te pedirá que inicies sesión con la autenticación de dos factores una vez en el transcurso de 30 días. 

![Casilla de verificación Recordar esta cuenta durante 30 días]({% image_buster /assets/img/remember_me.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

Los clientes con varias cuentas en una misma empresa pueden tener problemas al utilizar esta función debido a que la cookie está vinculada a un dispositivo específico. Si los usuarios utilizan el mismo dispositivo para iniciar sesión en varias cuentas, la cookie se sustituirá para las cuentas previamente autorizadas en ese dispositivo. Braze espera que sólo haya un dispositivo asociado a una cuenta, no un dispositivo para varias cuentas.

### Restablecer la autenticación de usuario

Si tienes problemas para iniciar sesión con la autenticación de dos factores, ponte en contacto con los administradores de tu empresa para restablecer la autenticación de dos factores. Los administradores pueden realizar los siguientes pasos:

1. Vaya a **Configuración** > **Usuarios de la empresa**.
2. Seleccione el usuario de la lista proporcionada.
3. Seleccione **Restablecer** en **Autenticación de dos factores**.

Un restablecimiento puede resolver problemas comunes de autenticación, como problemas con aplicaciones de autenticación, verificación de correo electrónico que no se envía, fallo de inicio de sesión debido a interrupciones de SMS o error del usuario, y más.

### Requisitos para la 2FA a nivel de empresa

En primer lugar, comprueba si el 2FA está habilitado para tu panel yendo a **Configuración de la empresa** > **Configuración de seguridad** > **Autenticación de dos factores**. Si el botón alternativo está en gris, 2FA no se ha activado para tu empresa y no es obligatorio para todos los usuarios del panel.

#### Opciones del usuario cuando 2FA no es obligatorio

Si la 2FA no se aplica a nivel de empresa, los usuarios individuales pueden configurar la 2FA para sí mismos en su página de Configuración de la cuenta. En este caso, los usuarios no quedarán bloqueados en sus cuentas si no lo configuran. Puedes identificar qué usuarios han optado por habilitar la 2FA consultando la página Gestionar usuarios.

#### Requisitos cuando la 2FA es obligatoria

Si la 2FA se aplica a nivel de empresa, los usuarios que no la configuren en sus propias cuentas al iniciar sesión quedarán bloqueados en el panel. Los usuarios deben completar la configuración 2FA para mantener el acceso.

{% alert important %}
La 2FA es necesaria para todos los usuarios de Braze sólo si el inicio de sesión único (SSO) no está habilitado. Si se utiliza SSO, no es necesario aplicar 2FA a nivel de empresa.
{% endalert %}

## Configuración de la autenticación de dos factores (2FA)

### Configurar 2FA con Authy

1. Descarga la aplicación Authy desde la tienda de aplicaciones de tu dispositivo.
2. En Braze, introduce tu número de teléfono.
3. Toca la notificación enviada a tu dispositivo para que abras la aplicación Authy.
4. Inicia la aplicación Authy en tu dispositivo para recuperar el código.
5. En Braze, introduce el código de verificación que recibiste de Authy.

Si tienes problemas durante el proceso de instalación y se te redirige a la página de inicio de Braze o a la pantalla de iniciar sesión, prueba lo siguiente:

- Utiliza el modo incógnito o navegación privada: Intenta configurarlo de nuevo con una ventana de navegación de incógnito o privada. Esto puede evitar problemas causados por extensiones o complementos del navegador.
- Prueba con otro perfil de navegador: Si el problema persiste, considera la posibilidad de utilizar un perfil de navegador diferente para eliminar los conflictos con los plugins instalados.

### Configurar 2FA cuando no se aplica

Para activar manualmente la autenticación de dos factores (2FA) en tu cuenta Braze cuando no se aplica, sigue estos pasos:

1. Descarga una aplicación 2FA como Authy, Google Authenticator, Okta Verify o similar desde App Store (iOS), Google Play Store (Android) o la Web. O, si prefieres configurar la 2FA con correo electrónico o SMS, salta al paso 2.
2. En Braze, ve a Gestionar cuenta, desplázate hasta la sección **Autenticación de dos factores** y, a continuación, selecciona **Iniciar configuración**.
3. Introduce tu contraseña en el modal de iniciar sesión y, a continuación, selecciona **Comprobar contraseña**.
4. En el modal **Configuración de autenticación de dos factores**, introduce tu número de teléfono y, a continuación, selecciona **Habilitar**.
5. Copia el código de siete dígitos generado en tu aplicación 2FA, correo electrónico o mensaje SMS, luego vuelve a Braze y pégalo en el modal de **Configuración de autenticación de dos factores**. Selecciona **Verificar**.
6. (Opcional) Para evitar introducir 2FA durante los próximos 30 días, habilita la opción **Recordar esta cuenta durante 30 días**.

## Acceso elevado

El Acceso Elevado añade una capa extra de seguridad para las acciones sensibles en tu panel Braze. Cuando están activos, los usuarios tienen que volver a verificar su cuenta antes de exportar un segmento o ver una clave de API. Para utilizar el Acceso Elevado, ve a **Configuración** > **Configuración de administrador** > **Configuración de seguridad** y altérnalo. 

Si un usuario no puede volver a verificar, será redirigido al punto donde lo dejó y no podrá continuar con la acción sensible. Después de volver a verificar con éxito, no tendrán que volver a hacerlo durante la siguiente hora, a menos que cierren la sesión antes.

![Alterna el Acceso Elevado.]({% image_buster /assets/img/elevated_access.png %})

## Descargar un informe de sucesos de seguridad {#security-event-report}

El informe de eventos de seguridad es un informe CSV de eventos de seguridad como invitaciones a cuentas, eliminaciones de cuentas, intentos de inicio de sesión fallidos y exitosos, y otras actividades. Puedes utilizarlo para realizar auditorías internas.

Para descargar este informe, haga lo siguiente:

1. Vaya a **Configuración** > **Configuración del administrador**.
2. Seleccione la pestaña **Configuración de seguridad** y vaya a la sección **Descarga de eventos de seguridad**.
3. Seleccione **Descargar informe**. 

Esta descarga manual de informes sólo contiene los 10.000 eventos de seguridad más recientes de tu cuenta.

Para exportar eventos de seguridad a Amazon S3 sin este límite de filas, consulta [Exportación de eventos de seguridad con Amazon S3]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings/security_export_s3/).

{% details Reported security events %}
### Iniciar sesión y cuenta
- Firmado en
- Error al iniciar sesión
- Configuración de la autenticación de dos factores completada
- Reinicio de la autenticación de dos factores completado
- Desarrollador autorizado 2FA
- Desarrollador adicional añadido
- Cuenta añadida
- Desarrollador Suspendido
- Desarrollador no suspendido
- Desarrollador Actualizado
- Desarrollador eliminado
- Cuenta eliminada
- Estado de la suscripción del usuario actualizado
- Usuario actualizado
- Cuenta de desarrollador actualizada

### Acceso elevado
- Iniciado Flujo de Acceso Elevado
- Flujo de acceso elevado completado
- Verificación 2FA fallida para acceso elevado
- Habilitación del control de acceso elevado
- Acceso Elevado para Discapacitados Aplicación de la Ley

Campaña
- Campaña añadida
- Campaña editada

Canvas
- Viaje añadido
- Viaje editado

### Segment
- Segmento añadido
- Segmento editado
- Datos exportados a CSV
- Segmento exportado mediante API
- Segmento Usuarios Eliminado
- Cohorte autorizada

### Clave de API REST
- Añadida clave de API REST
- Eliminada la clave de API REST

### Credencial de autenticación básica
- Añadida la credencial Basic Auth
- Actualizada la credencial de Autenticación Básica
- Eliminada la credencial de Autenticación Básica

### Permiso
- Desarrollador autorizado 2FA
- Permiso de cuenta actualizado
- Equipo añadido
- Equipo editado
- Equipo archivado
- Equipo no archivado
- Conjunto de permisos del grupo de aplicaciones creado
- Grupo de aplicaciones editadas Conjunto de permisos
- Eliminado el conjunto de permisos del grupo de aplicaciones
- Rol personalizado creado
- Rol personalizado actualizado
- Rol personalizado eliminado

### Configuración de la empresa
- Grupo de aplicaciones añadido
- Aplicación añadida
- Configuración de la empresa modificada
- Configuración de seguridad de la empresa actualizada
- Actualizada la Exportación a la Nube de Eventos de Seguridad
- Añadido dominio personalizado de Páginas de Aterrizaje
- Eliminado el dominio personalizado de las páginas de destino
- Dominio personalizado creado
- Dominio personalizado Eliminado
- Habilitación del grupo de control global
- Grupo de control global desactivado
- Exclusiones de control global actualizadas
- Lista de SMS permitidos del grupo de suscripción actualizada

### Plantilla de correo electrónico
- Plantilla de correo electrónico añadida
- Plantilla de correo electrónico actualizada

### Push credenciales
Credenciales push actualizadas
Credenciales push eliminadas

### Depurador de SDK
- Iniciada la sesión del depurador SDK
- Registro del depurador SDK exportado

### Usuarios
- Usuarios eliminados
- Usuarios vistos
- Inicio de la importación de usuarios
- Estado del grupo de suscripción de usuarios actualizado
- Usuario eliminado
- Cancelada la eliminación de un solo usuario
- Cancelado el borrado masivo de usuarios

### Catálogos
- Catálogo Creado
- Catálogo Eliminado

### Agentes de Braze
- Agente creado
- Agente editado

### Operador BrazeAI 
- Respuesta solicitada del operador BrazeAI
- El operador de BrazeAI respondió
{% enddetails %}

## Ver información personal identificable (PII) {#view-pii}

El permiso **Ver PII** sólo es accesible para unos pocos usuarios seleccionados de Braze. Por defecto, todos los administradores tienen activado el permiso **Ver PII** en los permisos de usuario. Esto significa que pueden ver todos los atributos estándar y personalizados que tu empresa haya definido como PII en todo el panel. Cuando este permiso esté desactivado para los usuarios, éstos no podrán ver ninguno de esos atributos.

{% alert note %}
Necesitas el permiso **Ver PII** para utilizar [el Generador de consultas]({{site.baseurl}}/user_guide/analytics/query_builder/building_queries/), porque permite acceder directamente a algunos datos de clientes.
{% endalert %}

Para conocer las capacidades de permisos de equipo existentes, consulta [Configurar permisos de usuario]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#available-limited-and-team-role-permissions).

### Definir la PII

{% alert important %}
Seleccionar y definir determinados campos como campos PII sólo afecta a lo que los Usuarios pueden ver en el panel Braze y no afecta a cómo se gestionan los datos del Usuario final en dichos campos PII.<br><br>Consulta a tu equipo jurídico para alinear la configuración de tu panel con las normativas y políticas de privacidad aplicables a tu empresa, incluidas las relacionadas con la [retención de datos]({{site.baseurl}}/data_retention/).
{% endalert %}

Puedes seleccionar los campos que tu empresa designe como PII en el panel. Para ello, ve a **Configuración de la empresa** > **Configuración de administrador** > **Configuración de seguridad**.

Los siguientes atributos pueden designarse como PII y ocultarse a los usuarios de Braze que no tengan permisos de **Ver PII**.

#### Posibles atributos PII

| Atributos estándar | Atributos personalizados |
| ------------------- | ----------------- |
| {::nomarkdown} <ul> <li>Dirección de correo electrónico </li> <li> Número de teléfono </li> <li> Nombre </li> <li> Apellido </li> <li> Género </li> <li> Cumpleaños </li> <li> ID de los dispositivos </li> <li> Ubicación más reciente </li> </ul> {:/} | {::nomarkdown} <ul> <li> Todos los atributos personalizados<ul><li>Los atributos personalizados individuales pueden marcarse como PII si no necesita ocultar todos los atributos.</li></ul></li> </ul> {:/} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Zonas limitadas

A continuación se asume que todos los campos están configurados como PII, y que los usuarios mencionados son los que utilizan la plataforma Braze. Además, los atributos "precedentes" se refieren a los de la tabla [Atributos PII potenciales](#potential-pii-attributes). Eliminar los permisos de PII de un usuario puede afectar a la usabilidad más allá de estas áreas enumeradas.

| Navegación por el panel | Resultado | Notas |
| -------------------- | ------ | ----- |
| Búsqueda de usuarios | El usuario que se conecta no puede buscar por dirección de correo electrónico, número de teléfono, nombre o apellidos: {::nomarkdown} <ul> <li> No se mostrarán los atributos estándar y personalizados anteriores al visualizar un perfil de usuario. </li> <li> No se pueden editar los atributos estándar anteriores de un perfil de usuario desde el panel de Braze. </li> <li> No se puede actualizar el estado de suscripción en un perfil de usuario. </li></ul> {:/} | El acceso a esta sección sigue requiriendo acceso para ver el perfil de usuario. |
| Importación de usuarios | El usuario no puede descargar archivos desde la página de **importación de usuarios**. | |
| {::nomarkdown} <ul> <li> Segmentos </li> <li> Campañas </li> <li> Canvas </li> </ul> {:/} | En el desplegable **Datos de usuario**: {::nomarkdown} <ul> <li> El usuario no tendrá la opción <b>CSV Exportar dirección de correo electrónico</b>. </li> <li> El usuario no dispondrá de los atributos estándar y personalizados anteriores en el archivo CSV al seleccionar <b>Exportar datos de usuario CSV</b>. </li> </ul> {:/} | |
| Grupo de prueba interno | El usuario no tendrá acceso a los atributos estándar anteriores de ningún usuario añadido al grupo de prueba interno. | |
| Registro de actividad de mensajes | El usuario no tendrá acceso a los atributos estándar anteriores para ningún usuario identificado en el registro de actividad de mensajes. | |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert note %}
Al previsualizar un mensaje, no se aplica el permiso **Ver PII**, por lo que los usuarios pueden ver los [atributos estándar anteriores](#potential-pii-attributes) si se hizo referencia a ellos en el mensaje a través de Liquid.
{% endalert %}

## Preferencias de eliminación de datos 

Puedes utilizar esta configuración para establecer preferencias sobre si Braze debe eliminar determinados campos durante el proceso de eliminación de usuarios para eventos. Estas preferencias sólo afectan a los datos de los usuarios que Braze ha eliminado. 

Cuando se elimina un usuario, Braze elimina toda la PII de los datos de eventos, pero conserva los datos anonimizados para fines de análisis. Algunos campos definidos por el usuario pueden contener IIP si envía información de usuario final a Braze. Si estos campos contienen PII, puedes optar por eliminar los datos cuando Braze anonimice los datos de eventos de los usuarios eliminados; si los campos no contienen PII, puedes conservarlos para análisis.

Usted es responsable de determinar las preferencias correctas para su espacio de trabajo. La mejor forma de determinar la configuración adecuada es revisar con los equipos internos que envían datos de eventos a Braze y con los equipos que utilizan extras de mensajes en Braze para confirmar si los campos pueden contener IIP.  

### Campos relevantes  

| Nombre o tipo de evento | Campo | Notas |
| -------------------- | ------ | ----- |
| Evento personalizado | Propiedades |  |
| Evento de compra | Propiedades |  |
| Envío de mensajes | message_extras | Varios tipos de eventos contienen un campo `message_extras`. La preferencia se aplica a todos los tipos de eventos de envío de mensajes compatibles con `message_extras`, incluidos los tipos de eventos que se añadan en el futuro. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert warning %}
**La eliminación es permanente.** Si optas por eliminar cualquier campo de Snowflake para los usuarios eliminados, la configuración se aplica a todos los datos históricos de tus espacios de trabajo y a cualquier evento de usuarios eliminados en el futuro. Después de que Braze haya ejecutado el proceso para aplicar la configuración a los datos de eventos históricos de los usuarios eliminados, **no podrás restaurar** los datos.
{% endalert %}

### Configurar preferencias

Establece preferencias predeterminadas marcando las casillas de los campos que Braze debe eliminar si se borra un usuario. Seleccione cualquiera de los campos que contengan IIP. Esta preferencia se aplica a todos los espacios de trabajo actuales y futuros, a menos que los espacios de trabajo se añadan explícitamente a un grupo de preferencias.

Para personalizar las preferencias por espacio de trabajo, puedes añadir grupos de preferencias con una configuración distinta a la predeterminada. Aplicamos la configuración predeterminada a todos los espacios de trabajo que no se hayan añadido a un grupo de preferencias adicional, incluidos los espacios de trabajo que se creen en el futuro.  

![Sección Preferencias de eliminación de datos con alternar activada para personalizar las preferencias de eliminación de datos por espacio de trabajo.]({% image_buster /assets/img/deletion_preferences_1.png %})

## Solución de problemas 

### Problemas con el bucle de configuración de la autenticación de dos factores (2FA)

Si te encuentras atrapado en un bucle después de introducir correctamente tu número de teléfono para la 2FA y se te redirige de nuevo a la página de iniciar sesión, es probable que se deba a que no se ha podido verificar en el primer intento. Para resolver este problema, sigue estos pasos:

1. Desactiva los bloqueadores de publicidad.
2. Habilita las cookies en la configuración de tu navegador.
3. Reinicia tu PC o portátil.
4. Intenta configurar 2FA de nuevo.

Si el problema persiste después de estos pasos, ponte en contacto con [el servicio de asistencia]({{site.baseurl}}/braze_support/) para que te ayuden.

### No se puede habilitar la autenticación de dos factores (2FA)

Si la 2FA está habilitada pero no ocurre nada cuando seleccionas el botón **Habilitar**, puede deberse a que tu navegador bloquea la redirección necesaria para enviar el código de verificación a través de SMS. Aquí tienes los pasos para solucionar este problema:

1. Suspende temporalmente los bloqueadores de publicidad que tengas habilitados en tu navegador.
2. Confirma que has habilitado las cookies de terceros en la configuración de tu navegador.
3. Intenta configurar 2FA.

### El código de verificación no se envía

Si tienes problemas al introducir tu número de teléfono en la página de Authy y no recibes un SMS, sigue estos pasos:

1. Instala la aplicación Authy en tu teléfono e inicia sesión en el autenticador Authy.
2. Introduce tu número de teléfono y comprueba en la aplicación Authy si hay cambios o notificaciones por SMS.
3. Si sigues sin recibir el SMS, prueba a utilizar una conexión de red diferente, como la red de tu casa o una Wi-Fi no corporativa. Las redes corporativas pueden tener políticas de seguridad que interfieran en la entrega de SMS.

Si el problema persiste, elimina el perfil antiguo en la aplicación Authy y escanea de nuevo el código QR para configurar la 2FA. Asegúrate de haber desactivado cualquier bloqueador de anuncios, habilitado las cookies de terceros o utilizado un navegador diferente antes de volver a intentar la configuración.