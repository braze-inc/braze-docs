---
nav_title: Configuración de TTL de notificaciones push
article_title: Configuración de TTL de notificaciones push
page_order: 16
page_type: reference
description: "Este artículo de referencia trata sobre la página de configuración de Push Time to Live en el panel de control de Braze."
channel: push

---

# Configuración de TTL de notificaciones push

> Más información sobre la página de configuración de Push Time-to-Live en el panel de control de Braze.

La página **Push Time-To-Live (TTL)** permite controlar la duración del intento de entrega para los dispositivos sin conexión. Esto significa que si el dispositivo de un usuario está desconectado en el momento del envío de la campaña, Braze intentará entregar el mensaje hasta la hora establecida.

{% alert note %}
Si utilizas la [navegación antigua]({{site.baseurl}}/navigation), puedes encontrar esta página en **Configuración** > **Gestionar configuración** > **Configuración Push TTL**.
{% endalert %}

Esta función no eliminará una notificación si el dispositivo del usuario ya la ha recibido; sólo controlará el tiempo que el proveedor de notificaciones push intentará enviar una notificación.

![Pulsar la pestaña de Ajustes de Tiempo en Directo en Gestionar Ajustes][1]

{% alert tip %}
Recuerda hacer clic en **Guardar** antes de salir de la página.
{% endalert %}

[1]: {% image_buster /assets/img/push_ttl.png %}
