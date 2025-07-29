---
nav_title: Centro de capacidad de entrega
article_title: Centro de capacidad de entrega
page_order: 4
description: "Este artículo de referencia explica cómo configurar el Centro de entregabilidad, una función que permite a los profesionales del marketing ver sus dominios de envío de correo electrónico y reputaciones de IP y comprender su entregabilidad."
channel:
  - email

---

# Centro de capacidad de entrega

> 

La entregabilidad del correo electrónico es la clave del éxito de una campaña. Mediante el Centro de entregabilidad del panel de control de Braze, puede ver sus dominios por **Reputación IP** o **Errores de entrega** para descubrir y solucionar cualquier problema potencial con la entregabilidad del correo electrónico. 

Para acceder al Centro de capacidad de entrega, necesitarás los [permisos de usuario]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/)"Acceder a campañas, Canvas, tarjetas, segmentos, biblioteca multimedia" y "Ver datos de uso".

## Configuración de tu cuenta Google Postmaster

Antes de conectarte al Centro de entregabilidad, deberás configurar una cuenta de Google Postmaster Tools. Puedes utilizar una cuenta de Gmail laboral o personal para configurar Google Postmaster. 

1. Acceda [al panel de Google Postmaster Tools](https://postmaster.google.com/managedomains?pli=1).
2. En la parte inferior derecha, selecciona el ícono más <i class="fas fa-plus-circle"></i>.
3. Introduce tu dominio raíz o subdominio para autentificar tu correo electrónico. Si estás añadiendo y verificando el dominio raíz, esto permitirá que la verificación se aplique en sentido descendente a los subdominios. Por ejemplo, verificando `braze.com`, puedes añadir posteriormente `demo.braze.com` y otros subdominios sin tener que verificarlos individualmente.
4. Google generará un registro TXT que puede añadirse directamente a las DNS de su dominio. Generalmente pertenece a quien gestiona su DNS. Para obtener información y orientación sobre cómo actualizar tus DNS específicas, consulta [Verifica tu dominio (pasos específicos del host)](https://support.google.com/a/topic/1409901).
5. Seleccione **Siguiente**. <br>
6. Una vez añadido el registro TXT a las DNS, vuelva al panel de Google Postmaster Tools y seleccione **Verificar**. Este paso confirma que eres el propietario del dominio, por lo que podrás acceder a las métricas de entregabilidad de Gmail en tu cuenta de Postmaster. <br> 

{% alert tip %}
Asegúrese de que el registro TXT está vinculado al dominio principal, no al subdominio que está utilizando a través de Braze.
{% endalert %}

{% alert note %}
Si los subdominios no se incluyen en el Centro de entregabilidad de Google Postmaster, puede deberse a que sólo se ha añadido el dominio principal a Google Postmaster. Una vez verificados los dominios principales en Google Postmaster, puedes añadir tus subdominios, que se verificarán automáticamente. Este proceso permite a Google informar sobre las métricas a nivel de subdominio, que luego se pueden extraer en el Centro de entregabilidad Braze.
{% endalert %}

## Integración de Google Postmaster



Sigue estos pasos para integrarte con Google Postmaster y configurar tu Centro de entregabilidad:

1. Vaya a **Análisis** > **Rendimiento del correo electrónico**.
2. Seleccione la pestaña **Centro de entregabilidad**. <br>
3. Selecciona **Conectar con Google Postmaster**. 
4. Selecciona tu cuenta de Google y, a continuación, selecciona **Permitir** para permitir que Braze vea las métricas de tráfico de correo electrónico de los dominios registrados en Postmaster Tools. 

Sus dominios verificados se mostrarán en el Centro de entregabilidad. 



También puedes acceder a Google Postmaster en el panel de Braze yendo a **Integraciones de socios** > **Socios tecnológicos** > **Google Postmaster**. Tras la integración, Braze extrae los datos de reputación y errores de los últimos 30 días. Es posible que los datos no estén disponibles inmediatamente y que tarden varios minutos en rellenarse.

### Métricas y definiciones

Las siguientes métricas y definiciones se aplican a Google Postmaster Tools.

#### Reputación de IP 

Para comprender mejor las tasas de reputación IP, consulta esta tabla:

| Tasa de reputación | Definición |
| ----- | ---------- |
| Alta | Tiene un buen historial de generar pocas quejas por spam (como usuarios que hacen clic en el botón "spam"). |
| Media/Justa | Se sabe que genera un compromiso positivo, pero ocasionalmente recibe quejas por spam. La mayoría de los correos electrónicos de este dominio se enviarán a la bandeja de entrada, excepto cuando aumenten las quejas por spam. |
| Baja | Conocido por recibir regularmente elevados índices de quejas por spam. Es probable que los correos electrónicos de este remitente se filtren a la carpeta de correo no deseado. |
| Mal | Tiene un historial de recibir elevados índices de quejas por spam. Los correos electrónicos de este dominio casi siempre se rechazarán en el momento de la conexión o se filtrarán a la carpeta de correo no deseado. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Reputación de dominio 

Utilice la siguiente tabla para controlar y comprender las calificaciones de reputación de su dominio y evitar que se filtre a una carpeta de spam.

| Tasa de reputación | Definición |
| ----- | ---------- |
| Alta | Tiene un buen historial de quejas por correo no deseado muy bajo. Cumple las directrices de envío de Gmail. Los correos electrónicos rara vez se filtran a la carpeta de spam. Tiene un buen historial con una tasa de correo no deseado muy baja.  |
| Media/Justa | Se sabe que genera un compromiso positivo, pero ocasionalmente ha recibido un bajo volumen de quejas por spam. La mayoría de los correos electrónicos de este dominio llegarán a la bandeja de entrada (excepto cuando se produzca un aumento notable de los niveles de spam). |
| Baja | Conocido por recibir quejas de spam con regularidad. Es probable que los correos electrónicos de este remitente se filtren a la carpeta de correo no deseado. |
| Mal | Tiene un historial de recibir elevados índices de quejas por spam. Los correos electrónicos de este dominio casi siempre se rechazarán en el momento de la conexión o se filtrarán a la carpeta de correo no deseado. |
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

 

## Configuración de los Servicios de Datos de Red Inteligente de Microsoft (SNDS)

Si Microsoft es tu principal proveedor de buzones de correo, puedes utilizar esta integración para acceder a tus datos de reputación de Microsoft y verlos. De este modo, puede supervisar la salud de sus IP para determinar cómo se reciben sus mensajes de correo electrónico.

{% alert important %}
Si no ve sus datos en el Centro de entregabilidad, póngase en contacto con [el servicio de asistencia]({{site.baseurl}}/user_guide/administrative/access_braze/support/) con una lista de sus direcciones IP.
{% endalert %}



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
| Superior a 0,3 % | Revise su proceso de suscripción y asegúrese de que el enlace para darse de baja funciona. Considere también si el correo podría personalizarse mejor para su público. |
| Superior al 100 % | Tenga en cuenta que el SNDS muestra las reclamaciones para el día en que fueron notificadas, no retroactivamente con respecto al día en que se entregó el correo objeto de la reclamación. | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Impactos de las trampas de correo no deseado

Los accesos trampa de spam son el número de mensajes enviados a "cuentas trampa", que son cuentas mantenidas por Outlook.com que no solicitan ningún correo.  

{% alert tip %}
Si está buscando registros relacionados con uno de sus dominios verificados en Braze, tenga en cuenta que el Centro de entregabilidad enumera sus datos de Google Postmaster o Microsoft SNDS, lo que significa que es probable que ninguna de las dos plataformas tenga datos que compartir con Braze. Alternativamente, sugerimos mantener una entrega de correo electrónico consistente, ya que esto puede conducir a una mayor reputación.
{% endalert %}


