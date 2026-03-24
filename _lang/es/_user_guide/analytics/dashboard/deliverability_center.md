---
nav_title: Centro de capacidad de entrega
article_title: Centro de capacidad de entrega
alias: "/deliverability_center/"
page_order: 4
description: "Este artículo de referencia explica cómo configurar el Centro de capacidad de entrega, una función que permite a los especialistas en marketing ver sus dominios de envío de correo electrónico y reputaciones de IP, y comprender su capacidad de entrega."
channel:
  - email

---

# Centro de capacidad de entrega

> El Centro de capacidad de entrega proporciona más información sobre el rendimiento de tu correo electrónico, ya que admite el uso de [Gmail Postmaster Tools](https://www.gmail.com/postmaster/) para realizar un seguimiento de los datos de los correos electrónicos enviados y recopilar datos sobre tu dominio de envío.

La capacidad de entrega del correo electrónico es la clave del éxito de una campaña. Mediante el Centro de capacidad de entrega en el dashboard de Braze, puedes ver tus dominios por **Reputación de IP** o **Errores de entrega** para descubrir y solucionar cualquier problema potencial con la capacidad de entrega del correo electrónico. 

Para acceder al Centro de capacidad de entrega, necesitas los [permisos de usuario heredados]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?sdktab=legacy%20permissions) "Acceder a Campaigns, Canvas, tarjetas, Segments, biblioteca multimedia" y "Ver datos de uso", o los [permisos granulares]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?sdktab=granular%20permissions) del siguiente menú desplegable para tu espacio de trabajo.

{% details Permisos de usuario para el Centro de capacidad de entrega %}

{% multi_lang_include deprecations/user_permissions.md %}

- Ver Campaigns
- Editar Campaigns
- Archivar Campaigns
- Ver Canvas
- Editar Canvas
- Archivar Canvas
- Ver reglas de limitación de frecuencia
- Editar reglas de limitación de frecuencia
- Ver priorización de mensajes
- Editar priorización de mensajes
- Ver bloques de contenido
- Ver conmutadores de características
- Editar conmutadores de características
- Archivar conmutadores de características
- Ver Segments
- Editar Segments
- Ver plantillas IAM
- Editar plantillas IAM
- Archivar plantillas IAM
- Ver plantillas de correo electrónico
- Editar plantillas de correo electrónico
- Archivar plantillas de correo electrónico
- Ver plantillas de webhook
- Editar plantillas de webhook
- Archivar plantillas de webhook
- Ver plantillas de enlaces de correo electrónico
- Editar plantillas de enlaces de correo electrónico
- Ver activos de la biblioteca multimedia
- Editar activos de la biblioteca multimedia
- Eliminar activos de la biblioteca multimedia
- Ver ubicaciones
- Editar ubicaciones
- Archivar ubicaciones
- Ver códigos promocionales
- Editar códigos promocionales
- Exportar códigos promocionales
- Ver centros de preferencia
- Editar centros de preferencia
- Ver informes
- Editar informes
- Ver datos de uso

{% enddetails %}

## Configuración de tu cuenta de Google Postmaster

Antes de conectarte al Centro de capacidad de entrega, deberás configurar una cuenta de Google Postmaster Tools. Puedes utilizar una cuenta de Gmail personal o del trabajo para configurar Google Postmaster. 

1. Accede al [panel de Google Postmaster Tools](https://postmaster.google.com/managedomains?pli=1).
2. En la parte inferior derecha, selecciona el icono más <i class="fas fa-plus-circle"></i>.
3. Introduce tu dominio raíz (principal) para autenticar tu correo electrónico. Asegúrate de que el registro TXT esté vinculado a este dominio raíz (principal), **no** al subdominio que utilizas a través de Braze. Verificar el dominio raíz (principal) te permite añadir subdominios posteriormente en Postmaster Tools sin crear registros TXT adicionales. Por ejemplo, al verificar `braze.com`, más adelante puedes añadir `demo.braze.com` como un subdominio independiente en Postmaster Tools para ver métricas a nivel de subdominio.
4. Google genera un registro TXT que se puede añadir directamente al DNS de tu dominio. Generalmente pertenece a quien gestiona tu DNS. Para obtener información y orientación sobre cómo actualizar tu DNS específico, consulta [Verificar tu dominio (pasos específicos del host)](https://support.google.com/a/topic/1409901).
5. Selecciona **Next**. <br>![Un dominio de ejemplo "demo.braze.com" para autenticar un correo electrónico.]({% image_buster /assets/img_archive/domain_authentication.png %})
6. Una vez añadido el registro TXT al DNS, vuelve al panel de Google Postmaster Tools y selecciona **Verify**. Este paso confirma que eres el propietario del dominio, para que puedas acceder a las métricas de capacidad de entrega de Gmail en tu cuenta de Postmaster. <br> ![Un mensaje para verificar la propiedad del dominio "demo.braze.com".]({% image_buster /assets/img_archive/domain_verification.png %})

{% alert note %}
Si tus subdominios no aparecen en el Centro de capacidad de entrega de Google Postmaster, puede deberse a que solo se ha añadido el dominio raíz (principal) a Google Postmaster. Una vez verificados los dominios raíz en Google Postmaster, puedes añadir tus subdominios, que se verifican automáticamente. Este proceso permite a Google informar sobre métricas a nivel de subdominio, que luego se pueden extraer en el Centro de capacidad de entrega de Braze.
{% endalert %}

## Integración de Google Postmaster

Antes de configurar tu Centro de capacidad de entrega, comprueba que tus dominios se hayan [añadido a Gmail Postmaster Tools](https://support.google.com/mail/answer/9981691?hl=en).

Sigue estos pasos para integrarte con Google Postmaster y configurar tu Centro de capacidad de entrega:

1. Ve a **Análisis** > **Rendimiento del correo electrónico**.
2. Selecciona la pestaña **Centro de capacidad de entrega**. <br>![Un Centro de capacidad de entrega sin conexión con Google Postmaster.]({% image_buster /assets/img_archive/deliverability_center1.png %})
3. Selecciona **Conectar con Google Postmaster**. 
4. Selecciona tu cuenta de Google y luego selecciona **Permitir** para permitir que Braze vea las métricas de tráfico de correo electrónico de los dominios registrados en Postmaster Tools. 

Tus dominios verificados se muestran en el Centro de capacidad de entrega. 

![Dos dominios verificados para Google Postmaster con una reputación media y baja.]({% image_buster /assets/img_archive/deliverability_center2.png %})

También puedes acceder a Google Postmaster en el dashboard de Braze yendo a **Integraciones de socios** > **Socios tecnológicos** > **Google Postmaster**. Tras la integración, Braze extrae los datos de reputación y errores de los últimos 30 días. Es posible que los datos no estén disponibles de inmediato y que tarden varios minutos en cargarse.

### Métricas y definiciones

Las siguientes métricas y definiciones se aplican a Google Postmaster Tools.

#### Reputación de IP 

Para comprender mejor las calificaciones de reputación de IP, consulta esta tabla:

| Calificación de reputación | Definición |
| ----- | ---------- |
| Alta | Tiene un buen historial de generar pocas quejas por correo no deseado (como usuarios que hacen clic en el botón "spam"). |
| Media/Justa | Se sabe que genera interacción positiva, pero ocasionalmente recibe quejas por correo no deseado. La mayoría de los correos electrónicos de este dominio se envían al buzón de entrada, excepto cuando aumentan las quejas por correo no deseado. |
| Baja | Conocido por recibir regularmente tasas elevadas de quejas por correo no deseado. Es probable que los correos electrónicos de este remitente se filtren a la carpeta de correo no deseado. |
| Mala | Tiene un historial de recibir tasas elevadas de quejas por correo no deseado. Los correos electrónicos procedentes de este dominio casi siempre se rechazan en el momento de la conexión o se filtran a la carpeta de correo no deseado. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Reputación de dominio 

Utiliza la siguiente tabla para supervisar y comprender las calificaciones de reputación de tu dominio y evitar que tus correos se filtren a una carpeta de correo no deseado.

| Calificación de reputación | Definición |
| ----- | ---------- |
| Alta | Tiene un buen historial de quejas por correo no deseado muy bajas. Cumple las directrices de remitente de Gmail. Los correos electrónicos rara vez se filtran a la carpeta de correo no deseado. Tiene un buen historial con una tasa de correo no deseado muy baja. Cumple las [directrices de remitente de Gmail](https://developers.google.com/gmail/markup/registering-with-google). |
| Media/Justa | Se sabe que genera interacción positiva, pero en ocasiones ha recibido un volumen bajo de quejas por correo no deseado. La mayoría de los correos electrónicos de este dominio llegan al buzón de entrada (excepto cuando hay un aumento notable en los niveles de correo no deseado). |
| Baja | Conocido por recibir quejas por correo no deseado con regularidad. Es probable que los correos electrónicos de este remitente se filtren a la carpeta de correo no deseado. |
| Mala | Tiene un historial de recibir tasas elevadas de quejas por correo no deseado. Los correos electrónicos procedentes de este dominio casi siempre se rechazan en el momento de la conexión o se filtran a la carpeta de correo no deseado. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Autenticación

Utiliza el panel de autenticación para revisar el porcentaje de correos electrónicos que han superado el Marco de directivas del remitente (SPF), el Correo identificado por claves de dominio (DKIM) y la Autenticación, notificación y conformidad de mensajes basados en dominios (DMARC).

| Tipo de gráfico | Definición |
| ----- | ---------- |
| SPF | Muestra el porcentaje de correos electrónicos que superaron SPF frente a todos los correos electrónicos del dominio que intentaron SPF. Esto excluye cualquier correo falsificado. |
| DKIM | Muestra el porcentaje de correos electrónicos que superaron DKIM frente a todos los correos electrónicos del dominio que intentaron DKIM. |
| DMARC | Muestra el porcentaje de correos electrónicos que superaron la alineación DMARC frente a todos los correos electrónicos recibidos del dominio que superaron SPF o DKIM. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Cifrado

Consulta esta tabla para saber qué porcentaje de tu tráfico entrante y saliente está cifrado.

| Término | Definición |
| ----- | ---------- |
| TLS de entrada | Muestra el porcentaje de correo entrante (a Gmail) que superó TLS frente a todo el correo recibido de ese dominio. |
| TLS de salida | Muestra el porcentaje de correo saliente (de Gmail) aceptado a través de TLS frente a todo el correo enviado a ese dominio. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Para obtener más ideas sobre cómo mejorar la capacidad de entrega, lee [Errores comunes en la capacidad de entrega y trampas de correo no deseado]({{site.baseurl}}/user_guide/onboarding_with_braze/email_setup/deliverability_pitfalls_and_spam_traps/#deliverability-pitfalls-and-spam-traps). Asegúrate de consultar nuestras [prácticas recomendadas para el correo electrónico]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/) para saber qué debes comprobar antes de enviar una campaña por correo electrónico.

## Configuración de los Servicios de datos de red inteligente de Microsoft (SNDS)

Si Microsoft es tu principal proveedor de buzones de correo, puedes utilizar esta integración para acceder a tus datos de reputación de Microsoft y consultarlos. De este modo, puedes supervisar el estado de tus IP para determinar cómo se reciben tus correos electrónicos.

{% alert important %}
Si no ves tus datos en el Centro de capacidad de entrega, ponte en contacto con [Soporte]({{site.baseurl}}/user_guide/administrative/access_braze/support/) con una lista de tus direcciones IP.
{% endalert %}

![Un ejemplo de resultados de Microsoft SNDS, que incluye direcciones IP de muestra, destinatarios, comandos RCPT, comandos de datos, resultados de filtrado, tasa de quejas, inicio y fin del periodo de mensajes trampa y resultados de trampas de correo no deseado.]({% image_buster /assets/img_archive/deliverability_center_msnds.png %})

### Métricas y definiciones

Las siguientes métricas se aplican a Microsoft SNDS.

#### Destinatarios

Esta métrica se refiere al número de destinatarios de los mensajes transmitidos por la IP.

#### Comandos DATA

Esta métrica registra el número de comandos DATA enviados por la IP. Los comandos DATA forman parte del protocolo SMTP utilizado para enviar correo.

#### Resultados de filtrado

Consulta esta tabla para comprender los resultados del filtro. 

| Resultado | Definición |
| ----- | ---------- |
| Verde | Considerado correo no deseado por el filtro de correo no deseado de Microsoft hasta un 10 % del periodo de tiempo especificado. |
| Amarillo | Considerado correo no deseado por el filtro de correo no deseado de Microsoft entre un 10 % y un 90 % del periodo de tiempo especificado. |
| Rojo | Considerado correo no deseado por el filtro de correo no deseado de Microsoft más del 90 % del periodo de tiempo especificado.| 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Tasa de quejas

Es la fracción de tiempo en que un mensaje recibido desde la IP es reportado como no deseado por un usuario de Hotmail o Windows Live durante el periodo de actividad. Los usuarios tienen la opción de reportar casi todos los mensajes como basura a través de la interfaz de usuario web. 

Para calcular la tasa de quejas, divide el número de quejas entre el número de destinatarios del mensaje.  

| Resultado | Definición |
| ----- | ---------- |
| Inferior a 0,3 % | La tasa de quejas ideal. |
| Superior a 0,3 % | Revisa tu proceso de registro y asegúrate de que el enlace para cancelar suscripción funciona. Además, considera si el correo podría personalizarse mejor para tu audiencia. |
| Superior al 100 % | Ten en cuenta que SNDS muestra las quejas del día en que fueron reportadas, no retroactivamente respecto al día en que se entregó el correo objeto de la queja. | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Impactos en trampas de correo no deseado

Los impactos en trampas de correo no deseado son el número de mensajes enviados a "cuentas trampa", que son cuentas mantenidas por Outlook.com que no solicitan ningún correo. Es probable que cualquier mensaje enviado a estas cuentas trampa se considere correo no deseado, por lo que es importante supervisar esta métrica para asegurarte de que sea baja. Un número bajo de impactos en trampas de correo no deseado significa que los mensajes no se envían a estas cuentas, sino a cuentas reales.

{% alert tip %}
Si estás buscando registros relacionados con uno de tus dominios verificados en Braze, ten en cuenta que el Centro de capacidad de entrega muestra tus datos de Google Postmaster o Microsoft SNDS, lo que significa que es probable que ninguna de estas plataformas tenga datos que compartir con Braze. Como alternativa, te sugerimos mantener una entrega de correo electrónico consistente, ya que esto puede conducir a una mayor reputación. 
{% endalert %}