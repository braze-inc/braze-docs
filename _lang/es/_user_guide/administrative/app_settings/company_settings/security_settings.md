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

Utiliza este campo para definir durante cuánto tiempo Braze mantendrá activa tu sesión. Después de que Braze considere que su sesión está inactiva (sin actividad durante el número de minutos definido), se cerrará la sesión del usuario. El número máximo de minutos que puedes introducir es de 10.080 (igual a una semana) si en tu empresa se aplica la autenticación de dos factores; de lo contrario, la duración máxima de la sesión será de 1.440 minutos (igual a 24 horas).

### Autenticación de inicio de sesión único (SSO)

Puede restringir a sus usuarios el acceso mediante contraseña o SSO.

Para [SAML SSO]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/), los clientes deben establecer su configuración SAML antes de aplicarla. Si los clientes utilizan Google SSO, solo tienen que hacer cumplir la página de configuración de seguridad, sin ninguna elevación adicional.

## Lista de direcciones IP permitidas del panel

Utilice el campo mostrado para permitir direcciones IP y subredes específicas desde las que los usuarios pueden iniciar sesión en su cuenta (por ejemplo, desde una red de empresa o VPN). Especifique las direcciones IP y subredes como rangos CIDR en una lista separada por comas. Si no indicas nada, los usuarios podrán iniciar sesión desde cualquier dirección IP.

## Autenticación de dos factores

La autenticación de dos factores es obligatoria para todos los usuarios de Braze. Añade un segundo nivel de verificación de identidad al registro de una cuenta, haciéndolo más seguro que un simple nombre de usuario y contraseña. Si tu panel de control no admite la autenticación de dos factores, ponte en contacto con tu gestor de éxito de clientes. 

Cuando se activa la autenticación de dos factores:

- Además de introducir una contraseña, los usuarios tendrán que introducir un código de verificación al acceder a su cuenta de Braze. El código puede enviarse a través de una aplicación de autenticación, correo electrónico o SMS. 
- La casilla **Recordar esta cuenta durante 30 días** pasa a estar disponible para los usuarios.

Los usuarios que no configuren su autenticación de dos factores quedarán bloqueados en su cuenta Braze. Los usuarios de cuentas Braze también pueden configurar la autenticación de dos factores por su cuenta en la **Configuración de la cuenta**, aunque no lo exija el administrador.

Asegúrate de guardar los cambios antes de salir de la página.

### Recuerda esta cuenta durante 30 días {#remember-me}

Esta característica está disponible cuando está activada la autenticación de dos factores.

Cuando seleccionas **Recordar esta cuenta durante 30 días**, se almacena una cookie en tu dispositivo, que sólo te pedirá que inicies sesión con la autenticación de dos factores una vez en el transcurso de 30 días. 

![Casilla Recordar esta cuenta durante 30 días]({% image_buster /assets/img/remember_me.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

Los clientes con varias cuentas en una misma empresa pueden tener problemas al utilizar esta función debido a que la cookie está vinculada a un dispositivo específico. Si los usuarios utilizan el mismo dispositivo para iniciar sesión en varias cuentas, la cookie se sustituirá para las cuentas previamente autorizadas en ese dispositivo. Braze espera que sólo haya un dispositivo asociado a una cuenta, no un dispositivo para varias cuentas.

### Restablecer la autenticación de usuario

Si tienes problemas para iniciar sesión con la autenticación de dos factores, ponte en contacto con los administradores de tu empresa para restablecer la autenticación de dos factores. Los administradores pueden realizar los siguientes pasos:

1. Vaya a **Configuración** > **Usuarios de la empresa**.
2. Seleccione el usuario de la lista proporcionada.
3. Seleccione **Restablecer** en **Autenticación de dos factores**.

Un restablecimiento puede resolver problemas comunes de autenticación, como problemas con aplicaciones de autenticación, verificación de correo electrónico que no se envía, fallo de inicio de sesión debido a interrupciones de SMS o error del usuario, y más.

## Acceso elevado

El Acceso Elevado añade una capa extra de seguridad para las acciones sensibles en tu panel Braze. Cuando están activos, los usuarios tienen que volver a verificar su cuenta antes de exportar un segmento o ver una clave de API. Para utilizar el Acceso Elevado, ve a **Configuración** > **Configuración de administrador** > **Configuración de seguridad** y altérnalo. 

Si un usuario no puede volver a verificar, será redirigido al punto donde lo dejó y no podrá continuar con la acción sensible. Después de volver a verificar con éxito, no tendrán que volver a hacerlo durante la siguiente hora, a menos que cierren la sesión antes.

![Alternar Acceso Elevado.]({% image_buster /assets/img/elevated_access.png %})

## Descargar un informe de incidentes de seguridad

El informe de eventos de seguridad es un informe CSV de eventos de seguridad como invitaciones a cuentas, eliminaciones de cuentas, intentos de inicio de sesión fallidos y exitosos, y otras actividades. Puedes utilizarlo para realizar auditorías internas.

Para descargar este informe, haga lo siguiente:

1. Vaya a **Configuración** > **Configuración del administrador**.
2. Seleccione la pestaña **Configuración de seguridad** y vaya a la sección **Descarga de eventos de seguridad**.
2. Seleccione **Descargar informe**. 

Este informe sólo contiene los 10.000 eventos de seguridad más recientes de su cuenta. Si necesita datos de eventos específicos, póngase en contacto con el servicio de asistencia técnica.

{% details Sucesos de seguridad notificados %}

### Iniciar sesión y cuenta 
- Firmado en
- Error al iniciar sesión
- Configuración de la autenticación de dos factores completada
- Reinicio de la autenticación de dos factores completado
- Desarrollador autorizado 2FA
- Desarrollador adicional añadido
- Desarrollador Suspendido
- Desarrollador no suspendido
- Desarrollador Actualizado
- Desarrollador eliminado
- Estado de la suscripción del usuario actualizado
- Usuario actualizado

### Acceso elevado
- Iniciado Flujo de Acceso Elevado
- Flujo de acceso elevado completado
- Verificación 2FA fallida para acceso elevado

### Campaña
- Campaña añadida
- Campaña editada

### Canvas
- Viaje añadido
- Viaje editado

### Segment
- Segmento añadido
- Segmento editado
- Datos exportados a CSV
- Segmento exportado mediante API

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

### Configuración de la empresa
- Grupo de aplicaciones añadido
- Aplicación añadida
- Configuración de la empresa modificada

### Plantilla de correo electrónico
- Plantilla de correo electrónico añadida
- Plantilla de correo electrónico actualizada

### Push credenciales
- Credenciales push actualizadas
- Credenciales push eliminadas

### Depurador de SDK
- Iniciada la sesión del depurador SDK
- Registro del depurador SDK exportado
{% enddetails %}

## Ver información personal identificable (PII) {#view-pii}

El permiso **Ver PII** sólo es accesible para unos pocos usuarios seleccionados de Braze. Por defecto, todos los administradores tienen activado el permiso **Ver PII** en los permisos de usuario. Esto significa que pueden ver los siguientes atributos estándar y personalizados en todo el cuadro de mandos. Cuando se desactiva este permiso para los usuarios, éstos no podrán ver esta información.

Para conocer las capacidades de permisos de equipo existentes, consulta [Configurar permisos de usuario]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#available-limited-and-team-role-permissions).

### Definir la PII

Puedes definir qué campos se designan como PII en el panel. Para ello, ve a **Configuración de la empresa** > **Configuración de seguridad**.

Los siguientes campos se pueden ocultar a los usuarios de Braze que no tengan permisos de **Ver IIP**.

| Atributos estándar | Atributos personalizados |
| ------------------- | ----------------- |
| {::nomarkdown} <ul> <li>Dirección de correo electrónico </li> <li> Número de teléfono </li> <li> Nombre </li> <li> Apellido </li> <li> Género </li> <li> Cumpleaños </li> <li> ID de los dispositivos </li> <li> Ubicación más reciente </li> </ul> {:/} | {::nomarkdown} <ul> <li> Todos los atributos personalizados<ul><li>Los atributos personalizados individuales pueden marcarse como PII si no necesita ocultar todos los atributos.</li></ul></li> </ul> {:/} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Zonas limitadas

A continuación se asume que todos los campos están configurados como PII, y que los usuarios mencionados son los que utilizan la plataforma Braze.

| Navegación por el panel | Resultado | Notas |
| -------------------- | ------ | ----- |
| Búsqueda de usuarios | El usuario que se conecta no puede buscar por dirección de correo electrónico, número de teléfono, nombre o apellidos: {::nomarkdown} <ul> <li> No se mostrarán los atributos estándar y personalizados anteriores al visualizar un perfil de usuario. </li> <li> No se pueden editar los atributos estándar anteriores de un perfil de usuario desde el panel de Braze. </li> </ul> {:/} | El acceso a esta sección sigue requiriendo el acceso para ver el perfil del usuario. |
| Importación de usuarios | El usuario no puede descargar archivos desde la página de **importación de usuarios**. | |
| {::nomarkdown} <ul> <li> Segmentos </li> <li> Campañas </li> <li> Canvas </li> </ul> {:/} | En el desplegable **Datos de usuario**: {::nomarkdown} <ul> <li> El usuario no tendrá la opción <b>CSV Exportar dirección de correo electrónico</b>. </li> <li> El usuario no dispondrá de los atributos estándar y de cliente anteriores en el archivo CSV al seleccionar <b>CSV Exportar datos de usuario</b>. </li> </ul> {:/} | |
| Grupo de prueba interno | El usuario no tendrá acceso a los atributos estándar anteriores de ningún usuario añadido al grupo de prueba interno. | |
| Registro de actividad de mensajes | El usuario no tendrá acceso a los atributos estándar anteriores para ningún usuario identificado en el registro de actividad de mensajes. | |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert note %}
Al previsualizar un mensaje, no se aplica el permiso **Ver PII**, por lo que los usuarios pueden ver los atributos estándar anteriores si se hizo referencia a ellos en el mensaje a través de Liquid.
{% endalert %}

## Preferencias de eliminación de datos 

Puedes utilizar esta configuración para establecer preferencias sobre si determinados campos deben eliminarse durante el proceso de eliminación de usuarios para eventos. Estas preferencias sólo afectan a los datos de los usuarios que han sido eliminados de Braze. 

Cuando se elimina un usuario, Braze elimina toda la PII de los datos de eventos, pero conserva los datos anonimizados para fines de análisis. Algunos campos definidos por el usuario pueden contener IIP si envía información de usuario final a Braze. Si estos campos contienen IIP, puede optar por eliminar los datos cuando los datos de eventos se anonimicen para los usuarios eliminados; si los campos no contienen IIP, pueden conservarse para análisis.

Usted es responsable de determinar las preferencias correctas para su espacio de trabajo. La mejor forma de determinar la configuración adecuada es revisar con los equipos internos que envían datos de eventos a Braze y con los equipos que utilizan extras de mensajes en Braze para confirmar si los campos pueden contener IIP.  

### Campos relevantes  

| Nombre o tipo de evento | Campo | Notas |
| -------------------- | ------ | ----- |
| Evento personalizado | Propiedades |  |
| Evento de compra | Propiedades |  |
| Envío de mensajes | message_extras | Varios tipos de eventos contienen un campo `message_extras`. La preferencia se aplica a todos los tipos de eventos de envío de mensajes compatibles con `message_extras`, incluidos los tipos de eventos que se añadan en el futuro. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert warning %}
**La eliminación es permanente.** Si opta por eliminar cualquier campo de Snowflake para usuarios eliminados, la configuración se aplicará a todos los datos históricos de sus espacios de trabajo y a cualquier evento para usuarios eliminados en el futuro. Después de que Braze haya ejecutado el proceso para aplicar la configuración a los datos de eventos históricos de los usuarios eliminados, los datos **no se podrán restaurar**.
{% endalert %}

### Configurar preferencias

Establezca las preferencias por defecto marcando las casillas de los campos que deben eliminarse si se borra un usuario. Seleccione cualquiera de los campos que contengan IIP. Esta preferencia se aplicará a todos los espacios de trabajo actuales y futuros, a menos que los espacios de trabajo se añadan explícitamente a un grupo de preferencias.

Para personalizar las preferencias por espacio de trabajo, puedes añadir grupos de preferencias con una configuración distinta a la predeterminada. Aplicamos la configuración predeterminada a todos los espacios de trabajo que no se hayan añadido a un grupo de preferencias adicional, incluidos los espacios de trabajo que se creen en el futuro.  

![Sección Preferencias de borrado de datos con alternar activado para personalizar las preferencias de borrado de datos por espacio de trabajo.]({% image_buster /assets/img/deletion_preferences_1.png %})


