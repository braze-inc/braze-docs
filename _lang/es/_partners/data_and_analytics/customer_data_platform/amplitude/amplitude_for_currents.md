---
nav_title: Amplitud para corrientes
article_title: Amplitud para corrientes
page_order: 0
description: "Este artículo de referencia describe la asociación entre Braze Currents y Amplitude, una plataforma de análisis de productos e inteligencia empresarial."
page_type: partner
tool: Currents
search_tag: Partner

---

# [![Curso Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/amplitude-integration-with-braze){: style="float:right;width:120px;border:0;" class="noimgborder"}Amplitud para corrientes

> [Amplitude](https://amplitude.com/) es una plataforma de análisis de productos e inteligencia empresarial.

La integración bidireccional de Braze y Amplitude te permite [sincronizar tus cohortes de Amplitude]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amplitude/amplitude_audiences/), rasgos de usuario y eventos de Amplitude en Braze, así como aprovechar Braze Currents para [exportar tus eventos de Braze a Amplitude](#data-export-integration) para realizar análisis más profundos de tus datos de producto y marketing.

## Requisitos previos

| Requisito | Descripción |
|---|---|
| Cuenta de amplitud | Se necesita una [cuenta de Amplitude](https://amplitude.com/) para beneficiarse de esta asociación. |
| Currents | Para poder exportar los datos a Amplitude, debes tener configurado [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) en tu cuenta. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" } 

## Integración de la exportación de datos

Una lista completa de los eventos y propiedades de eventos que se pueden exportar de Braze a Amplitude se puede encontrar en las siguientes secciones. Todos los eventos enviados a Amplitude incluirán la dirección `external_user_id` del usuario como ID de usuario de Amplitude. Las propiedades de los eventos específicos de Brasil se enviarán bajo la clave `event_properties` en los datos enviados a Amplitude.

{% alert important %}
Para utilizar esta función, tu ID de usuario de Amplitude debe coincidir con el ID externo de Braze.
{% endalert %}

Braze sólo enviará datos de eventos para usuarios que tengan su `external_user_id` configurado o usuarios anónimos que tengan su `device_id` configurado. Para los usuarios anónimos, tendrás que sincronizar el ID de tu dispositivo Amplitude con el ID del dispositivo Braze en el SDK. Por ejemplo:

```java
amplitude.setDeviceId(Appboy.getInstance(context).getDeviceId();)
```

Puedes exportar dos tipos de eventos a Amplitude: Eventos de [participación en mensajes](#supported-currents-events), que consisten en los Eventos Braze directamente relacionados con el envío de mensajes, y [Eventos de comportamiento del cliente](#supported-currents-events), incluida otra actividad de la aplicación o del sitio web, como sesiones, eventos personalizados y compras rastreadas a través de la plataforma. Todos los eventos regulares llevan el prefijo `[Appboy]`, y todos los eventos personalizados llevan el prefijo `[Appboy] [Custom Event]`. Las propiedades de eventos personalizados y eventos de compra llevan el prefijo `[Custom event property]` y `[Purchase property]`, respectivamente.

Todas las cohortes nombradas e importadas a Braze llevarán el prefijo `[Amplitude]` y el sufijo `cohort_id`. Esto significa que una cohorte llamada "TEST_COHORT" con el `cohort_id` "abcd1234" se titulará `[Amplitude] TEST_COHORT: abcd1234` en los filtros Braze.

Póngase en contacto con su gestor de cuenta o abra un [ticket de asistencia]({{site.baseurl}}/braze_support/) si necesita acceder a derechos de eventos adicionales.

### Paso 1: Configurar la integración de amplitud en Braze 

En Amplitude, localiza tu clave API de exportación de Amplitude.

{% alert warning %}
Mantén actualizada tu clave de API de Amplitude. Si las credenciales de tu conector caducan, el conector dejará de enviar eventos. Si esto persiste durante más de **48 horas**, los eventos del conector se eliminarán y los datos se perderán permanentemente.
{% endalert %}

### Paso 2: Crear corriente de soldadura

En Braze, vaya a **Corrientes > + Crear corriente > Crear exportación de amplitud**. Proporciona un nombre de integración, un correo electrónico de contacto, una clave API de exportación de Amplitude y una región de Amplitude en los campos indicados. A continuación, seleccione los eventos que desea seguir; se proporciona una lista de los eventos disponibles. Por último, haga clic en **Lanzar actual**

{% alert note %}
Los eventos enviados desde Braze Currents a Amplitude contarán para tu cuota de volumen de eventos de Amplitude.
{% endalert %}

![La página de corrientes de amplitud de Braze. Esta página incluye campos para el nombre de la integración, el correo electrónico de contacto, la clave de API y la región de EEUU. La mitad inferior de la página Currents enumera los eventos Currents disponibles que puede enviar.]({% image_buster /assets/img/amplitude4.png %})

{% tab nota %}
Consulta [los documentos de integración](https://amplitude.zendesk.com/hc/en-us/articles/115000217351-Appboy-Amplitude-Integration#how-to-set-up-and-use-the-integration) de Amplitude para obtener más información.
{% endtab %}

## Límites de tarifa

Currents se conecta a la API HTTP de Amplitude, que tiene una [tasa límite](https://developers.amplitude.com/docs/http-api-v2#upload-limit) de 30 eventos/segundo por dispositivo y un límite no documentado de 500K eventos/día por dispositivo. Si se superan estos umbrales, Amplitud estrangulará los eventos registrados a través de Corrientes. Si un dispositivo de tu integración supera este límite de velocidad, puede que experimentes un retraso en el momento en que los eventos de todos los dispositivos aparezcan en Amplitude.

Los dispositivos no deberían informar de más de 30 eventos/segundo o 500K eventos/día en circunstancias normales, y este patrón de eventos sólo debería producirse debido a una integración mal configurada. Para evitar este tipo de retraso, asegúrese de que su integración SDK notifica los eventos a un ritmo normal, tal y como se especifica en nuestras instrucciones de integración SDK, y absténgase de ejecutar pruebas automatizadas que generen muchos eventos para un único dispositivo.

## Acontecimientos apoyados por Currents

Braze admite la exportación a Amplitude de los siguientes datos enumerados en los glosarios de [comportamiento del usuario]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/) y de eventos de [compromiso de mensajes de]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) Currents:

### Comportamientos
- Evento personalizado: `users.behaviors.CustomEvent`
- Atribución de la instalación: `users.behaviors.InstallAttribution`
- Ubicación: `users.behaviors.Location`
- Compra: `users.behaviors.Purchase`
- Desinstalar: `users.behaviors.Uninstall`
- App (primera sesión, fin de sesión, inicio de sesión)
  - `users.behaviors.app.FirstSession`
  - `users.behaviors.app.SessionEnd`
  - `users.behaviors.app.SessionStart`
- Suscripción (cambio de estado global): `users.behaviors.subscription.GlobalStateChange`
- Grupo de suscripción (cambio de estado): `users.behaviors.subscriptiongroup.StateChange`
  
### Campañas
- Abortar: `users_campaigns_abort`
- Conversión: `users.campaigns.Conversion`
- EnrollinControl: `users.campaigns.EnrollInControl`
  
### Canvas
- Abortar: `users_canvas_abort`
- Conversión: `users.canvas.Conversion`
- Entrada: `users.canvas.Entry`
- Salida (audiencia emparejada, evento realizado)
  - `users.canvas.exit.MatchedAudience`
  - `users.canvas.exit.PerformedEvent`
- Paso del experimento (conversión, entrada dividida)
  - `users.canvas.experimentstep.Conversion`
  - `users.canvas.experimentstep.SplitEntry`

### Mensajes
- Tarjeta de contenido (abortar, hacer clic, descartar, imprimir, enviar)
  - `users.messages.contentcard.Abort`
  - `users.messages.contentcard.Click`
  - `users.messages.contentcard.Dismiss`
  - `users.messages.contentcard.Impression`
  - `users.messages.contentcard.Send`
- Correo electrónico (abortar, rebote, clic, entrega, markasspam, abrir, enviar, softbounce, cancelar suscripción)
- Mensaje in-app (abortar, clic, impresión)
  - `users.messages.inappmessage.Abort`
  - `users.messages.inappmessage.Click`
  - `users.messages.inappmessage.Impression`
- Notificación push (abortar, rebotar, iOSforeground, abrir, enviar)
  - `users.messages.pushnotification.Abort`
  - `users.messages.pushnotification.Bounce`
  - `users.messages.pushnotification.IosForeground`
  - `users.messages.pushnotification.Open`
  - `users.messages.pushnotification.Send`
- SMS (abortar, envío de portadora, entrega, fallo de entrega, recepción entrante, rechazo, envío, clic en enlace corto)
  - `users.messages.sms.Abort`
  - `users.messages.sms.Delivery`
  - `users.messages.sms.DeliveryFailure`
  - `users.messages.sms.InboundReceive`
  - `users.messages.sms.Rejection`
  - `users.messages.sms.Send`
  - `users.messages.sms.ShortLinkClick`
- Webhook (abortar, enviar)
  - `users.messages.webhook.Abort`
  - `users.messages.webhook.Send`
- WhatsApp (abortar, entrega, fallo, recepción entrante, lectura, envío)
  - `users.messages.whatsapp.Abort`
  - `users.messages.whatsapp.Delivery`
  - `users.messages.whatsapp.Failure`
  - `users.messages.whatsapp.InboundReceive`
  - `users.messages.whatsapp.Read`
  - `users.messages.whatsapp.Send`
  
