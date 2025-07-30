---
nav_title: Configuración de push
article_title: Configuración de push
page_order: 16
page_type: reference
description: "Este artículo ofrece un resumen de la configuración push en el panel de Braze."
channel: push

---

# Configuración de push

> La página de **Configuración push** te permite configurar los ajustes clave para tus notificaciones push, incluido el Tiempo de vida push (TTL) y la prioridad predeterminada del FCM para las campañas de Android. Estas configuraciones ayudan a optimizar la entrega y la eficacia de tus notificaciones push, garantizando una mejor experiencia a tus usuarios.

## ¿Qué es Push TTL?

El TTL para notificación push controla el tiempo que Braze intentará entregar una notificación push a los dispositivos que estén desconectados en el momento de enviar la campaña. Si un dispositivo vuelve a conectarse después de que expire el TTL, el mensaje no se entregará. Esta configuración no eliminará una notificación si el dispositivo del usuario ya la ha recibido; sólo controla el tiempo que el proveedor push intenta entregar una notificación.

## Configuración predeterminada de los valores TTL de Push

Por defecto, Braze establece el TTL de Push al máximo para cada servicio de mensajería push. 

| Servicio de mensajería push | TTL máximo |
| --- | --- |
| Web (a través de los servicios FCM o Web Push) | 28 días |
| Firebase Cloud Messaging (FCM) | 28 días |
| Kindle (ADM) | 31 días |
| Huawei (HMS) | 15 días |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Esta configuración se aplica globalmente a todas las campañas push, a menos que se establezca un TTL diferente para un mensaje concreto. Para ajustar el TTL de un mensaje, consulta [Configuración avanzada de la campaña]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/advanced_campaign_settings/#ttl).

Para establecer un predeterminado diferente Push TTL:

1. Ve a **Configuración** > Administrar configuración > Configuración push.
2. Para cada plataforma Android, define un valor predeterminado de tiempo de vida. Puedes establecer incrementos más pequeños, como horas o segundos, para un control más preciso.
3. Selecciona **Guardar** para aplicar los cambios.

![Configuración TTL push para Firebase, Web, Kindle y dispositivos Huawei.]({% image_buster /assets/img/push_ttl.png %})

## Prioridad predeterminada de FCM para las campañas de Android

Puedes establecer la prioridad predeterminada de Firebase Cloud Messaging (FCM) para todas las campañas push de Android. Esta prioridad determina cómo se entrega la notificación push a los dispositivos de los usuarios.

Las opciones prioritarias del FCM son:

| Prioridad | Descripción | Casos de uso |
| --- | --- | --- |
| Normal | Prioridad de entrega estándar que optimiza el uso de la batería | Contenido que no requiere atención inmediata |
| Alta | Los mensajes se envían inmediatamente | Notificaciones sensibles al tiempo que requieren una entrega rápida |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Para configurar la prioridad predeterminada del FCM:

1. Ve a **Configuración** > Administrar configuración > Configuración push.
2. En la sección Prioridad del FCM, selecciona "Normal" o "Alta" como configuración predeterminada.
3. Selecciona **Guardar** para aplicar los cambios.

![Configuración de la prioridad de entrega de Android.]({% image_buster /assets/img/push_fcm_priority_settings.png %})

Esta configuración se aplica globalmente a todas las nuevas campañas push de Android, a menos que se seleccione una prioridad diferente al crear una campaña específica. 

{% alert note %}
Si FCM detecta que tu aplicación envía con frecuencia mensajes de alta prioridad que no dan lugar a notificaciones visibles para el usuario o a la interacción del usuario, esos mensajes pueden ser automáticamente despriorizados a la prioridad normal.
{% endalert %}

Para obtener información más detallada sobre los niveles de prioridad y la despriorización del FCM, consulta [Configuración avanzada de la campaña]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/advanced_campaign_settings/#fcm-priority).

