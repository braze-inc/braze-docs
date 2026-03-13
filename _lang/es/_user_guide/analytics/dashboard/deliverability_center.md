---
nav_title: Centro de capacidad de entrega
article_title: Centro de capacidad de entrega
alias: "/deliverability_center/"
page_order: 4
description: "Este artículo de referencia explica cómo configurar el Centro de entregabilidad, una función que permite a los profesionales del marketing ver sus dominios de envío de correo electrónico y reputaciones de IP y comprender su entregabilidad."
channel:
  - email

---

# Centro de capacidad de entrega

> El Centro de entregabilidad proporciona más información sobre el rendimiento del correo electrónico, ya que admite el uso de [Gmail Postmaster Tools](https://www.gmail.com/postmaster/) para realizar un seguimiento de los correos electrónicos enviados y recopilar datos sobre el dominio de envío.

La entregabilidad del correo electrónico es la clave del éxito de una campaña. Mediante el Centro de entregabilidad del panel de control de Braze, puede ver sus dominios por **Reputación IP** o **Errores de entrega** para descubrir y solucionar cualquier problema potencial con la entregabilidad del correo electrónico. 

Para acceder al Centro de capacidad de entrega, necesitas los [permisos de usuario heredados]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?sdktab=legacy%20permissions) «Acceder a campañas, lienzos, tarjetas, segmentos y biblioteca multimedia» y «Ver datos de uso», o los [permisos granulares]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?sdktab=granular%20permissions) del siguiente menú desplegable para tu espacio de trabajo.

{% details User permissions for the Deliverability Center %}

{% multi_lang_include deprecations/user_permissions.md %}

- Ver campañas
- Editar campañas
- Archivar campañas
- Ver Canvas
- Editar Canvas
- Archivar Canvas
- Ver las reglas de limitación de frecuencia
- Editar reglas de limitación de frecuencia
- Ver priorización de mensajes
- Editar priorización de mensajes
- Ver bloques de contenido
- Ver las feature flags
- Editar conmutador de características
- Archiva feature flags
- Ver segmentos
- Editar segmentos
- Ver plantillas IAM
- Editar plantillas IAM
- Archivar plantillas IAM
- Ver plantillas de correo electrónico
- Editar plantilla de correo electrónico
- Archivar plantillas de correo electrónico
- Ver plantillas webhook
- Editar plantillas webhook
- Archivar plantillas webhook
- Ver plantillas de enlaces
- Editar plantillas de enlaces
- Ver activos de la biblioteca de medios
- Editar activos de la biblioteca de medios
- Eliminar activos de la biblioteca de medios
- Ver ubicaciones
- Editar ubicaciones
- Ubicación de los archivos
- Ver códigos promocionales
- Editar códigos promocionales
- Códigos promocionales de las exportaciones
- Ver centros de preferencia
- Editar centros de preferencia
- Ver informes
- Editar informes
- Ver datos de consumo

{% enddetails %}

## Configuración de tu cuenta Google Postmaster

Antes de conectarte al Centro de entregabilidad, deberás configurar una cuenta de Google Postmaster Tools. Puedes utilizar una cuenta de Gmail personal o del trabajo para configurar Google Postmaster. 

1. Acceda [al panel de Google Postmaster Tools](https://postmaster.google.com/managedomains?pli=1).
2. En la parte inferior derecha, selecciona el ícono más <i class="fas fa-plus-circle"></i>.
3. Introduce tu dominio raíz o subdominio para autentificar tu correo electrónico. Si estás añadiendo y verificando el dominio raíz, esto permite que la verificación se aplique a los subdominios. Por ejemplo, al verificar `braze.com`, más adelante podrás añadir`demo.braze.com`  y otros subdominios sin necesidad de verificarlos individualmente.

{% alert important %}
Asegúrate de que el registro TXT esté vinculado al dominio principal, no al subdominio que utilizas a través de Braze.
{% endalert %}

{: start="4"}
4\. Google genera un registro TXT que se puede añadir directamente al DNS de tu dominio. Generalmente pertenece a quien gestiona su DNS. Para obtener información y orientación sobre cómo actualizar tus DNS específicas, consulta [Verifica tu dominio (pasos específicos del host)](https://support.google.com/a/topic/1409901).
5\. Seleccione **Siguiente**. <br>![Un dominio de ejemplo "demo.braze.com" para autenticar un correo electrónico.]({% image_buster /assets/img_archive/domain_authentication.png %})
6\. Una vez añadido el registro TXT a las DNS, vuelva al panel de Google Postmaster Tools y seleccione **Verificar**. Este paso confirma que eres el propietario del dominio, por lo que puedes acceder a las métricas de capacidad de entrega de Gmail en tu cuenta de Postmaster. <br> ![Un mensaje para verificar la propiedad del dominio «demo.braze.com».]({% image_buster /assets/img_archive/domain_verification.png %})

{% alert note %}
Si los subdominios no se incluyen en el Centro de entregabilidad de Google Postmaster, puede deberse a que sólo se ha añadido el dominio principal a Google Postmaster. Una vez verificados los dominios principales en Google Postmaster, puedes añadir tus subdominios, que se verifican automáticamente. Este proceso permite a Google informar sobre las métricas a nivel de subdominio, que luego se pueden extraer en el Centro de entregabilidad Braze.
{% endalert %}

## Integración de Google Postmaster

Antes de configurar tu Centro de capacidad de entrega, comprueba que tus dominios se hayan [añadido a las Herramientas para administradores de correo de Gmail](https://support.google.com/mail/answer/9981691?hl=en).

Sigue estos pasos para integrarte con Google Postmaster y configurar tu Centro de entregabilidad:

1. Vaya a **Análisis** > **Rendimiento del correo electrónico**.
2. Seleccione la pestaña **Centro de entregabilidad**. <br>![Un centro de capacidad de entrega sin conexión con Google Postmaster.]({% image_buster /assets/img_archive/deliverability_center1.png %})
3. Selecciona **Conectar con Google Postmaster**. 
4. Selecciona tu cuenta de Google y, a continuación, selecciona **Permitir** para permitir que Braze vea las métricas de tráfico de correo electrónico de los dominios registrados en Postmaster Tools. 

Tus dominios verificados se muestran en el Centro de capacidad de entrega. 

![Dos dominios verificados para Google Postmaster con una reputación media y baja.]({% image_buster /assets/img_archive/deliverability_center2.png %})

También puedes acceder a Google Postmaster en el panel de Braze yendo a **Integraciones de socios** > **Socios tecnológicos** > **Google Postmaster**. Tras la integración, Braze extrae los datos de reputación y errores de los últimos 30 días. Es posible que los datos no estén disponibles inmediatamente y que tarden varios minutos en rellenarse.

### Métricas y definiciones

Las siguientes métricas y definiciones se aplican a Google Postmaster Tools.

#### Reputación de IP 

Para comprender mejor las tasas de reputación IP, consulta esta tabla:

| Tasa de reputación | Definición |
| ----- | ---------- |
| Alta | Tiene un buen historial de generar pocas quejas por spam (como usuarios que hacen clic en el botón "spam"). |
| Media/Justa | Se sabe que genera un compromiso positivo, pero ocasionalmente recibe quejas por spam. La mayoría de los correos electrónicos de este dominio se envían al buzón de entrada, excepto cuando aumentan las denuncias por correo no deseado. |
| Baja | Conocido por recibir regularmente elevados índices de quejas por spam. Es probable que los correos electrónicos del remitente se filtren a la carpeta de correo no deseado. |
| Mal | Tiene un historial de recibir elevados índices de quejas por spam. Los correos electrónicos procedentes de este dominio casi siempre se rechazan en el momento de la conexión o se filtran a la carpeta de correo no deseado. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Reputación de dominio 

Utilice la siguiente tabla para controlar y comprender las calificaciones de reputación de su dominio y evitar que se filtre a una carpeta de spam.

| Tasa de reputación | Definición |
| ----- | ---------- |
| Alta | Tiene un buen historial de quejas por correo no deseado muy bajo. Cumple las directrices de envío de Gmail. Los correos electrónicos rara vez se filtran a la carpeta de correo no deseado. Tiene un buen historial con una tasa de correo no deseado muy baja. Cumple las [directrices de remitente de Gmail](https://developers.google.com/gmail/markup/registering-with-google). |
| Media/Justa | Se sabe que genera una interacción positiva, pero en ocasiones ha recibido un pequeño volumen de denuncias por correo no deseado. La mayoría de los correos electrónicos de este dominio llegan al buzón de entrada (excepto cuando hay un aumento notable en los niveles de correo no deseado). |
| Baja | Conocido por recibir quejas de spam con regularidad. Es probable que los correos electrónicos del remitente se filtren a la carpeta de correo no deseado. |
| Mal | Tiene un historial de recibir elevados índices de quejas por spam. Los correos electrónicos procedentes de este dominio casi siempre se rechazan en el momento de la conexión o se filtran a la carpeta de correo no deseado. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Autenticación

Utiliza el panel de autenticación para revisar el porcentaje de mensajes de correo electrónico que han superado el Marco de directivas del remitente (SPF), el Correo identificado por claves de dominio (DKIM) y la Autenticación, notificación y conformidad de mensajes basados en dominios (DMARC).

| Tipo de gráfico | Definición |
| ----- | ---------- |
| SPF | Muestra el porcentaje de correos electrónicos que superaron el SPF frente a todos los correos electrónicos del dominio que intentaron el SPF. Esto excluye cualquier correo falsificado. |
| DKIM | Muestra el porcentaje de correos electrónicos que pasaron DKIM frente a todos los correos electrónicos del dominio que intentaron DKIM. |
| DMARC | Muestra el porcentaje de correos electrónicos que superaron la alineación DMARC frente a todos los correos electrónicos recibidos del dominio que superaron SPF o DKIM. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Cifrado

Consulte esta tabla para saber qué porcentaje de su tráfico entrante y saliente está cifrado.

| Plazo | Definición |
| ----- | ---------- |
| Entrada TLS | Muestra el porcentaje de correo entrante (a Gmail) que ha pasado TLS frente a todo el correo recibido de ese dominio. |
| TLS de salida | Muestra el porcentaje de correo saliente (de Gmail) aceptado a través de TLS frente a todo el correo enviado a ese dominio. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Para obtener más ideas sobre cómo mejorar la capacidad de entrega, lee [«Errores comunes en la capacidad de entrega y trampas de correo no deseado]({{site.baseurl}}/user_guide/onboarding_with_braze/email_setup/deliverability_pitfalls_and_spam_traps/#deliverability-pitfalls-and-spam-traps)». Asegúrate de consultar nuestras [prácticas recomendadas]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/) para [el correo electrónico]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/) para saber qué debes comprobar antes de enviar una campaña por correo electrónico.

## Configuración de los Servicios de Datos de Red Inteligente de Microsoft (SNDS)

Si Microsoft es tu principal proveedor de buzones de correo, puedes utilizar esta integración para acceder a tus datos de reputación de Microsoft y verlos. De este modo, puede supervisar la salud de sus IP para determinar cómo se reciben sus mensajes de correo electrónico.

{% alert important %}
Si no ve sus datos en el Centro de entregabilidad, póngase en contacto con [el servicio de asistencia]({{site.baseurl}}/user_guide/administrative/access_braze/support/) con una lista de sus direcciones IP.
{% endalert %}

![Un ejemplo de resultados de Microsoft SNDS, que incluye direcciones IP de muestra, destinatarios, comandos RCPT, comandos de datos, resultados de filtrado, tasa de quejas, inicio y fin del periodo de mensajes trampa y resultados de trampas de correo no deseado.]({% image_buster /assets/img_archive/deliverability_center_msnds.png %})

### Métricas y definiciones

Las siguientes métricas se aplican a Microsoft SNDS.

#### Destinatarios

Esta métrica se refiere al número de destinatarios de los mensajes transmitidos por la IP.

#### Comandos DATA

Esta métrica registra el número de comandos DATA enviados por la IP. Los comandos DATA forman parte del protocolo SMTP utilizado para enviar correo.

#### Filtrar resultados

Consulte esta tabla para comprender los resultados del filtro 

| Resultado | Definición |
| ----- | ---------- |
| Verde | Juzgado como correo no deseado por el filtro de correo no deseado de Microsoft hasta un 10 % del período de tiempo especificado. |
| Amarillo | El filtro de correo no deseado de Microsoft consideró que tu correo electrónico era correo no deseado entre un 10 % y un 90 % del período de tiempo especificado. |
| Rojo | Juzgado como correo no deseado por el filtro de correo no deseado de Microsoft hasta más de un 90 % del período de tiempo especificado.| 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Tasa de reclamaciones

Esta es la fracción de tiempo que un mensaje recibido desde la IP es reclamado por un usuario de Hotmail o Windows Live durante el período de actividad. Los usuarios tienen la opción de reportar casi todos los mensajes como basura a través de la interfaz de usuario web. 

Para calcular el porcentaje de reclamaciones, hay que dividir el número de reclamaciones por el número de destinatarios del mensaje.  

| Resultado | Definición |
| ----- | ---------- |
| Inferior a 0,3 % | La tasa de reclamaciones ideal. |
| Superior a 0,3 % | Revise su proceso de suscripción y asegúrese de que el enlace para darse de baja funciona. Además, considera si el correo podría recibir una mayor personalización para tu audiencia. |
| Superior al 100 % | Tenga en cuenta que el SNDS muestra las reclamaciones para el día en que fueron notificadas, no retroactivamente con respecto al día en que se entregó el correo objeto de la reclamación. | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Impactos de las trampas de correo no deseado

Los accesos trampa de spam son el número de mensajes enviados a "cuentas trampa", que son cuentas mantenidas por Outlook.com que no solicitan ningún correo. Es probable que cualquier mensaje enviado a estas cuentas trampa se considere correo no deseado, por lo que es importante supervisar esta métrica para asegurarse de que sea baja. Un bajo número de trampas de correo no deseado significa que los mensajes no se envían a estas cuentas, sino a cuentas reales.

{% alert tip %}
Si estás buscando registros relacionados con uno de tus dominios verificados en Braze, ten en cuenta que el Centro de capacidad de entrega muestra tus datos de Google Postmaster o Microsoft SNDS, lo que significa que es probable que ninguna de estas plataformas tenga datos que compartir con Braze. Alternativamente, sugerimos mantener una entrega de correo electrónico consistente, ya que esto puede conducir a una mayor reputación.
{% endalert %}


