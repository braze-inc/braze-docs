---
nav_title: Uninstall Tracking
article_title: Desinstalar seguimiento
page_order: 6
page_type: reference
description: "Este artículo de referencia cubre la implementación del seguimiento de desinstalaciones para estadísticas a nivel de campaña y a nivel de aplicación."
tool: Reports

---

# Desinstalar el seguimiento

> Este artículo muestra cómo puede ver las desinstalaciones de aplicaciones agregadas a lo largo del tiempo para localizar tendencias y anomalías, y realizar un seguimiento de las desinstalaciones a nivel de campaña para determinar si una campaña específica está impulsando o impidiendo las instalaciones de aplicaciones.

El seguimiento de la desinstalación en Braze proporciona los siguientes detalles:

1. Estadísticas diarias de desinstalación de aplicaciones en un gráfico de series temporales en la página **de inicio**.
2. Estadísticas de desinstalación a nivel de campaña en un gráfico de series temporales en la página **Detalles de campaña** de una campaña específica. Esta estadística especifica el número de destinatarios de la campaña que se desinstalan cada día.

{% alert note %}
Debes realizar la adhesión voluntaria para desinstalar el seguimiento en tu panel de Braze. Esta característica está disponible para aplicaciones en iOS, Android y Fire OS.
{% endalert %}

## Cómo funciona

Braze recopila automáticamente un nivel básico de información de desinstalación de sus campañas push regulares. Sin embargo, debido a que la frecuencia con la que los diferentes usuarios reciben campañas push puede variar, ofrecemos un seguimiento de desinstalación para proporcionar una instantánea más precisa de la actividad de desinstalación entre sus usuarios.

## Activar el seguimiento de la desinstalación

Puedes activar el seguimiento de desinstalaciones en la página **Configuración de aplicaciones**, en **Ajustes**, para cada aplicación que quieras rastrear.

Cuando activas el seguimiento de desinstalaciones para una aplicación, Braze envía un mensaje push nocturno en segundo plano a los usuarios que no han registrado una sesión ni recibido un push en las últimas 24 horas.

### Configuración

Para configurar Uninstall Tracking para tu aplicación iOS, utiliza un [método de utilidad]({{site.baseurl}}/developer_guide/analytics/tracking_uninstalls/?sdktab=swift). Para tu aplicación Android, utiliza [`isUninstallTrackingPush()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.push/-braze-notification-payload/is-uninstall-tracking-push.html). Cuando Braze detecta una desinstalación, ya sea a partir del seguimiento de desinstalaciones o de la entrega normal de campañas push, registraremos la mejor hora estimada de la desinstalación en el usuario. Este tiempo se almacena en el perfil del usuario como un atributo estándar y puede utilizarse para definir un segmento de usuarios para las campañas de recuperación.

## Filtrado de segmentos por desinstalaciones

El filtro **Desinstalados** selecciona a los usuarios que han desinstalado tu aplicación en un intervalo de tiempo determinado. Como es difícil determinar la hora exacta de una desinstalación, recomendamos que los filtros de desinstalación tengan rangos de tiempo más amplios para asegurarnos de que todos los que se desinstalan entran en el segmento en algún momento.

Las estadísticas diarias de desinstalaciones se encuentran en la página de **inicio**. 

![Desinstala el segmento.]({% image_buster /assets/img_archive/Uninstall_Segment.png %} "Uninstall Segment")

El gráfico puede desglosarse por aplicación y segmento, de forma similar a otras estadísticas que ofrece Braze. En la sección **Resumen del rendimiento**, seleccione el intervalo de fechas y, si lo desea, una aplicación. A continuación, desplázate hasta el gráfico **Rendimiento en el tiempo** y haz lo siguiente:

1. En el menú desplegable **Estadísticas para**, seleccione **Desinstalaciones**.
2. En el desplegable **Desglose**, seleccione **Por segmento**.
3. En el desplegable **Valores de desglose**, seleccione los segmentos que desea incluir en el gráfico.

{% alert note %}
Las aplicaciones sin seguimiento de desinstalaciones activado informarán de las desinstalaciones de sólo un subconjunto de sus usuarios (aquellos a los que se dirigieron las notificaciones push), por lo que los totales diarios de desinstalaciones pueden ser superiores a los que se muestran.
{% endalert %}

## Desinstalar el seguimiento de campañas

El seguimiento de desinstalación de campañas muestra el número de usuarios que recibieron una campaña específica y posteriormente desinstalaron su aplicación en el periodo de tiempo seleccionado. Esta herramienta permite comprender cómo las campañas pueden estar fomentando comportamientos negativos no deseados de los usuarios y ayuda a medir la eficacia general de las campañas.

Las estadísticas de desinstalación de campañas se encuentran en la página de **análisis de campañas** de una campaña específica. Para las campañas multicanal y multivariante, las desinstalaciones pueden desglosarse por canal y variante, respectivamente.

![Desinstala a nivel de campaña.]({% image_buster /assets/img_archive/campaign_level_uninstall_tracking.png %})

### Cómo funciona

Braze rastrea las desinstalaciones observando cuándo los mensajes push enviados a los dispositivos de los usuarios devuelven una señal, ya sea de Firebase Cloud Messaging (FCM) o de Apple Push Notification Service (APN), de que la aplicación ya no está instalada. Si activas el Uninstall Tracking global para una aplicación, Braze envía un mensaje push silencioso diario a los usuarios para detectar si la han desinstalado. Braze envía esta push «silenciosa» a todos los usuarios (a menos que el usuario haya desactivado las notificaciones silenciosas en la configuración de la aplicación); la push no aparece a los usuarios. Si Braze detecta que un usuario ha desinstalado la aplicación, nosotros:

* Aumenta en uno el recuento total de desinstalaciones de la aplicación.
* Incrementa en uno el recuento de desinstalaciones de cada campaña que el usuario haya recibido correctamente en las últimas 24 horas.
* Si un usuario recibe tres campañas en un periodo de 24 horas y luego las desinstala, incrementamos el recuento de "desinstalaciones" de las tres campañas.

FCM y APN imponen restricciones al Uninstall Tracking. Braze solo incrementa el recuento de desinstalaciones cuando FCM o APN nos informan de que un usuario ha desinstalado la aplicación, pero estos sistemas de terceros pueden notificarnos las desinstalaciones en cualquier momento. Utiliza el Uninstall Tracking para detectar tendencias direccionales en lugar de estadísticas precisas.

Para obtener más información sobre el uso del seguimiento de desinstalaciones, consulta nuestra entrada de blog[ Uninstall Tracking: Una mirada de la industria a sus puntos fuertes y sus limitaciones](https://www.braze.com/blog/uninstall-tracking-an-industry-look-at-its-strengths-and-limitations/).

## Solución de problemas

### ¿Por qué de repente veo un pico de desinstalaciones?

Si observas un pico de desinstalaciones de aplicaciones, puede deberse a que Firebase Cloud Messaging (FCM) y el servicio de notificaciones push de Apple (APNS) revocan tokens antiguos con una frecuencia diferente.

{% alert note %}
Por motivos de privacidad, los proveedores de notificaciones push de Braze pueden revocar los tokens a intervalos irregulares, lo que significa que el número de desinstalaciones puede dispararse en un periodo de tiempo determinado.<br><br>Para validar estos cambios, supervisa el seguimiento de desinstalaciones junto con una métrica de acción del usuario, como la tasa de apertura directa de notificaciones push. Si las desinstalaciones aumentan considerablemente, pero las aperturas directas se mantienen estables, es probable que el pico refleje la revocación de tokens antiguos por parte de un socio, en lugar del comportamiento real de los usuarios.
{% endalert %}

### ¿Por qué el número de desinstalaciones de aplicaciones difiere del que aparece en APN?

La diferencia es esperable. 

Apple utiliza un calendario aleatorio para retrasar la notificación cuando un token de notificaciones push deja de ser válido, lo que significa que, incluso después de que un usuario desinstale una aplicación, APN puede seguir devolviendo respuestas satisfactorias a las notificaciones push durante un periodo de tiempo. Este retraso es intencionado y está diseñado para proteger la privacidad de los usuarios. No se informará ningún rebote o fallo hasta que APN devuelva un`410`estado para un token no válido.

