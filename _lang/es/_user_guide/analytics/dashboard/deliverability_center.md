---
nav_title: Centro de capacidad de entrega
article_title: Centro de capacidad de entrega
page_order: 4
description: "Este artículo de referencia explica cómo configurar el Centro de capacidad de entrega, una característica que permite a los especialistas en marketing ver sus dominios de envío por correo electrónico y reputaciones de IP, y comprender la capacidad de entrega de sus correos electrónicos."
channel:
  - email

---

# Centro de capacidad de entrega

> El Centro de capacidad de entrega proporciona más información sobre el rendimiento de tu correo electrónico, ya que admite el uso de [las Herramientas para postmasters de Gmail](https://www.gmail.com/postmaster/) para realizar un seguimiento de los correos electrónicos enviados y recopilar datos sobre tu dominio de envío.

La capacidad de entrega del correo electrónico es la clave del éxito de una campaña. Con el Centro de capacidad de entrega del panel de Braze, puedes ver tus dominios por **reputación de IP** o **errores de entrega** para descubrir y solucionar posibles problemas de capacidad de entrega del correo electrónico. 

Para acceder al Centro de capacidad de entrega, necesitarás los permisos de usuario "Acceder a campañas, lienzos, tarjetas, segmentos, biblioteca multimedia" y "Ver datos de uso".

## Configuración de tu cuenta Google Postmaster

Antes de conectarte al Centro de entregabilidad, tendrás que configurar una cuenta de Google Postmaster Tools. Puedes utilizar una cuenta de Gmail de trabajo o personal para configurar Google Postmaster. 

1. Ve al [panel de Google Postmaster Tools](https://postmaster.google.com/managedomains?pli=1).
2. En la parte inferior derecha, selecciona el icono más <i class="fas fa-plus-circle"></i>.
3. Introduce tu dominio raíz o subdominio para autentificar tu correo electrónico. Si estás añadiendo y verificando el dominio raíz, esto permitirá que la verificación se aplique en sentido descendente a los subdominios. Por ejemplo, verificando `braze.com`, puedes añadir posteriormente `demo.braze.com` y otros subdominios sin tener que verificarlos individualmente.
4. Google generará un registro TXT que puedes añadir directamente a las DNS de tu dominio. Suele pertenecer a quien administra tus DNS. Para obtener información y orientación sobre cómo actualizar tus DNS específicas, consulta [Verifica tu dominio (pasos específicos del host)](https://support.google.com/a/topic/1409901).
5. Selecciona **Siguiente**. <br>\![Un dominio de ejemplo "demo.braze.com" para autentificar un correo electrónico.]({% image_buster /assets/img_archive/domain_authentication.png %})
6. Una vez añadido el registro TXT a las DNS, vuelve al panel de Google Postmaster Tools y selecciona **Verificar**. Este paso confirma que eres el propietario del dominio, por lo que podrás acceder a las métricas de capacidad de entrega de Gmail en tu cuenta de Postmaster. <br> Un mensaje para verificar la propiedad del dominio "demo.braze.com".]({% image_buster /assets/img_archive/domain_verification.png %})

{% alert tip %}
Asegúrate de que el registro TXT está vinculado al dominio principal, no al subdominio que utilizas a través de Braze.
{% endalert %}

{% alert note %}
Si tus subdominios no están incluidos en el Centro de capacidad de entrega de Google Postmaster, puede deberse a que sólo has añadido el dominio principal a Google Postmaster. Una vez verificados los dominios principales en Google Postmaster, puedes añadir tus subdominios, que se verificarán automáticamente. Este proceso permite a Google informar sobre las métricas a nivel de subdominio, que luego pueden introducirse en el Centro de capacidad de entrega de Braze.
{% endalert %}

## Integración de Google Postmaster

Antes de configurar tu Centro de capacidad de entrega, comprueba que tus dominios se han [añadido a las Herramientas para postmaster de Gmail](https://support.google.com/mail/answer/9981691?hl=en).

Sigue estos pasos para integrarte con Google Postmaster y configurar tu Centro de capacidad de entrega:

1. Ve a **Análisis** > Rendimiento del correo electrónico.
2. Selecciona la pestaña **Centro de capacidad de entrega**. <br>Un centro de capacidad de entrega con Google Postmaster desconectado.]({% image_buster /assets/img_archive/deliverability_center1.png %})
3. Selecciona **Conectar con Google Postmaster**. 
4. Selecciona tu cuenta de Google y, a continuación, selecciona **Permitir** para permitir que Braze vea las métricas de tráfico de correo electrónico de los dominios registrados en Postmaster Tools. 

Tus dominios verificados se mostrarán en el Centro de capacidad de entrega. 

Dos dominios verificados para Google Postmaster con una reputación media y baja.]({% image_buster /assets/img_archive/deliverability_center2.png %})

También puedes acceder a Google Postmaster en el panel de Braze yendo a **Integraciones de socios** > **Socios tecnológicos** > **Google Postmaster**. Tras la integración, Braze extrae los datos de reputación y errores de los últimos 30 días. Los datos pueden no estar disponibles inmediatamente y tardar varios minutos en completarse.

### Métrica y definiciones

Las siguientes métricas y definiciones se aplican a Google Postmaster Tools.

#### Reputación IP 

Para comprender mejor las tasas de reputación IP, consulta esta tabla:

| Tasa de reputación | Definición |
| ----- | ---------- |
| Alta | Tiene un buen historial de generar pocas quejas por correo no deseado (como usuarios que hacen clic en el botón "correo no deseado"). |
| Medio/Justo | Se sabe que genera una interacción positiva, pero ocasionalmente recibe quejas por correo no deseado. La mayoría de los correos electrónicos de este dominio se enviarán al buzón de entrada, excepto cuando aumenten las quejas por correo no deseado. |
| Baja | Se sabe que recibe regularmente elevadas tasas de quejas por correo no deseado. Es probable que los correos electrónicos de este remitente se filtren a la carpeta de correo no deseado. |
| Mal | Tiene un historial de recibir elevadas tasas de reclamaciones por correo no deseado. Los correos electrónicos de este dominio casi siempre se rechazarán en el momento de la conexión o se filtrarán a la carpeta de correo no deseado. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Reputación del dominio 

Utiliza la tabla siguiente para controlar y comprender las tasas de reputación de tu dominio y evitar que te filtren a una carpeta de correo no deseado.

| Tasa de reputación | Definición |
| ----- | ---------- |
| Alta | Tiene un buen historial de quejas por correo no deseado muy bajo. Cumple las directrices de remitente de Gmail. Los correos electrónicos rara vez se filtran a la carpeta de correo no deseado. Tiene un buen historial con una tasa de correo no deseado muy baja. Cumple las [directrices de remitente de Gmail](https://developers.google.com/gmail/markup/registering-with-google). |
| Medio/Justo | Se sabe que genera una interacción positiva, pero ocasionalmente ha recibido un bajo volumen de quejas por correo no deseado. La mayoría de los correos electrónicos de este dominio llegarán al buzón de entrada (excepto cuando se produzca un aumento notable de los niveles de correo no deseado). |
| Baja | Se sabe que recibe regularmente quejas por correo no deseado. Es probable que los correos electrónicos de este remitente se filtren a la carpeta de correo no deseado. |
| Mal | Tiene un historial de recibir elevadas tasas de reclamaciones por correo no deseado. Los correos electrónicos de este dominio casi siempre se rechazarán en el momento de la conexión o se filtrarán a la carpeta de correo no deseado. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Autenticación

Utiliza el panel de autenticación para revisar el porcentaje de mensajes de correo electrónico que han superado el Marco de directivas del remitente (SPF), el Correo identificado por claves de dominio (DKIM) y la Autenticación, notificación y conformidad de mensajes basados en dominios (DMARC).

| Tipo de gráfico | Definición |
| ----- | ---------- |
| FPS | Muestra el porcentaje de correos electrónicos que pasaron el SPF frente a todos los correos electrónicos del dominio que intentaron el SPF. Esto excluye cualquier correo falsificado. |
| DKIM | Muestra el porcentaje de correos electrónicos que pasaron DKIM frente a todos los correos electrónicos del dominio que intentaron DKIM. |
| DMARC | Muestra el porcentaje de correos electrónicos que superaron la alineación DMARC frente a todos los correos electrónicos recibidos del dominio que superaron SPF o DKIM. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Cifrado

Consulta esta tabla para saber qué porcentaje de tu tráfico entrante y saliente está encriptado.

| Plazo | Definición |
| ----- | ---------- |
| Entrada TLS | Muestra el porcentaje de correo entrante (a Gmail) que pasó TLS frente a todo el correo recibido de ese dominio. |
| Salida TLS | Muestra el porcentaje de correo saliente (de Gmail) aceptado a través de TLS frente a todo el correo enviado a ese dominio. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Para más ideas sobre cómo mejorar la [capacidad de]({{site.baseurl}}/user_guide/onboarding_with_braze/email_setup/deliverability_pitfalls_and_spam_traps/#deliverability-pitfalls-and-spam-traps) entrega, lee [Trampas de la capacidad de entrega y trampas del correo no deseado]({{site.baseurl}}/user_guide/onboarding_with_braze/email_setup/deliverability_pitfalls_and_spam_traps/#deliverability-pitfalls-and-spam-traps). Asegúrate de consultar nuestras [Prácticas recomendadas de correo electrónico]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/) para saber qué cosas debes comprobar antes de enviar una campaña de correo electrónico.

## Configuración de los Servicios de Datos de Red Inteligente de Microsoft (SNDS)

Si Microsoft es tu principal proveedor de buzones de correo, puedes utilizar esta integración para acceder a tus datos de reputación de Microsoft y verlos. De este modo, puedes controlar la salud de tus IP para determinar cómo se reciben tus correos electrónicos.

{% alert important %}
Si no ves tus datos en el Centro de capacidad de entrega, ponte en contacto con [el servicio de asistencia]({{site.baseurl}}/user_guide/administrative/access_braze/support/) con una lista de tus direcciones IP.
{% endalert %}

\![Un ejemplo de resultados de Microsoft SNDS, que incluye muestras de IPs, destinatarios, comandos RCPT, comandos de datos, resultado del filtrado, tasa de reclamaciones, inicio y fin del periodo de mensajes trampa y aciertos en la trampa de correo no deseado.]({% image_buster /assets/img_archive/deliverability_center_msnds.png %})

### Métrica y definiciones

Las siguientes métricas se aplican al SNDS de Microsoft.

#### Destinatarios

Esta métrica se refiere al número de destinatarios de los mensajes transmitidos por la IP.

#### Comandos DATA

Esta métrica sigue el número de comandos DATA enviados por la IP. Los comandos DATA forman parte del protocolo SMTP utilizado para enviar correo.

#### Filtrar resultados

Consulta esta tabla para entender los resultados del filtro 

| Resultado | Definición |
| ----- | ---------- |
| Verde | Juzgado como correo no deseado por el filtro de correo no deseado de Microsoft hasta un 10% del tiempo dado. |
| Amarillo | Juzgado como correo no deseado por el filtro de correo no deseado de Microsoft entre el 10% y el 90% del tiempo dado. |
| Rojo | Considerado como correo no deseado por el filtro de correo no deseado de Microsoft hasta más del 90% del tiempo dado.| 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Tasa de reclamaciones

Es la fracción de tiempo en que un mensaje recibido de la IP es reclamado por un usuario de Hotmail o Windows Live durante el periodo de actividad. Los usuarios tienen la opción de denunciar casi todos los mensajes como basura a través de la interfaz de usuario Web. 

Para calcular la tasa de reclamaciones, divide el número de reclamaciones entre el número de destinatarios de los mensajes.  

| Resultado | Definición |
| ----- | ---------- |
| Menos del 0,3 | La tasa de reclamaciones ideal. |
| Más del 0,3 | Revisa tu proceso de registro y asegúrate de que tu enlace para cancelar suscripción funciona. Considera también si el correo podría personalizarse mejor para tu audiencia. |
| Más del 100 | Ten en cuenta que el SNDS muestra las reclamaciones del día en que se comunicaron, no retroactivamente con respecto al día en que se entregó el correo objeto de la reclamación. | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Visitas trampa de correo no deseado

Los aciertos de la trampa de correo no deseado son el número de mensajes enviados a "cuentas trampa", que son cuentas mantenidas por Outlook.com que no solicitan ningún correo. Es probable que cualquier mensaje enviado a estas cuentas trampa se considere correo no deseado, por lo que es importante controlar esta métrica para asegurarse de que es baja. Un número bajo de aciertos en la trampa de correo no deseado significa que los mensajes no se envían a estas cuentas y que, en su lugar, se envían a cuentas reales.

{% alert tip %}
Si buscas registros relacionados con uno de tus dominios verificados en Braze, ten en cuenta que el Centro de capacidad de entrega enumera tus datos de Google Postmaster o Microsoft SNDS, lo que significa que es probable que ninguna de las dos plataformas tenga datos que compartir con Braze. Alternativamente, te sugerimos que mantengas una entrega de correo electrónico constante, ya que esto puede conducir a una mayor reputación.
{% endalert %}


