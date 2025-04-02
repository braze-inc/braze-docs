---
nav_title: Configuración de TTL de notificaciones push
article_title: Configuración de TTL de notificaciones push
page_order: 16
page_type: reference
description: "Este artículo de referencia trata sobre la página de configuración de Push Time to Live en el panel de control de Braze."
channel: push

---

# Configuración de TTL de notificaciones push

> Más información sobre la página de configuración de tiempo de vida push en el panel de Braze.

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

1. Ve a **Configuración** > **Administrar configuración** > **Configuración de Push TTL**.
2. Para cada plataforma Android, define un valor predeterminado de tiempo de vida. Puedes establecer incrementos más pequeños, como horas o segundos, para un control más preciso.
3. Selecciona **Guardar** para aplicar los cambios.

![Pulsar la pestaña de Ajustes de Tiempo en Directo en Gestionar Ajustes][1]


[1]: {% image_buster /assets/img/push_ttl.png %}
