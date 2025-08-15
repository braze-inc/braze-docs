---
nav_title: Push Max
article_title: Push Max
page_type: reference
description: "Push Max amplifica las notificaciones push de Android siguiendo las notificaciones push fallidas y reenviando la notificación push cuando el usuario tenga más probabilidades de recibirla."

permalink: /user_guide/message_building_by_channel/push/android/push_max/
platform: Android
channel:
  - Push

---

# Push Max

> Obtenga información sobre Push Max y cómo puede utilizar esta función para mejorar potencialmente la capacidad de entrega de las notificaciones push de Android a los [dispositivos OEM chinos]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/chinese_push_deliverability/).

## ¿Qué es Push Max?

Push Max amplifica las notificaciones push de Android siguiendo las notificaciones push fallidas y reenviando la notificación push cuando el usuario tenga más probabilidades de recibirla.

Algunos dispositivos Android fabricados por fabricantes chinos de equipos originales (OEM), como Xiaomi, OPPO y Vivo, emplean un sólido esquema de optimización de la batería para prolongar su duración. Este comportamiento puede tener la consecuencia no deseada de cerrar el procesamiento de aplicaciones en segundo plano, lo que reduce la capacidad de entrega de notificaciones push en estos dispositivos si la aplicación no está en primer plano. Esta circunstancia se da con mayor frecuencia en los mercados de Asia-Pacífico (APAC).

## Disponibilidad

- Disponible sólo para las notificaciones push de Android
- No compatible con mensajes basados en acciones o activados por la API
- No se admite cuando se selecciona la opción de [enviar sólo al último dispositivo utilizado por el usuario]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#device-options).

## Requisitos previos

Las notificaciones push enviadas mediante Push Max sólo se entregarán a dispositivos que tengan al [menos la siguiente versión mínima del SDK]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions):

{% sdk_min_versions android:29.0.1 %}

## Utilizar Push Max

{% tabs %}
{% tab Campañas %}

Para utilizar Push Max en tu campaña:

1. Crea una campaña push.
2. Seleccione **Android Push** como plataforma.
3. Ve al paso **Programar la entrega**.
4. Seleccione **Enviar usando Push Max**.

![Sección Capacidad de entrega push de Android del paso Programar la entrega con la opción "Enviar usando Push Max".]({% image_buster /assets/img_archive/push_max_campaigns.png %})

{% endtab %}
{% tab Canvas %}

Para utilizar Push Max en su lienzo:

1. Añade un paso de Mensaje a tu Canvas.
2. Seleccione **Android Push** como plataforma.
3. Vaya a la pestaña **Configuración de la entrega**.
4. Seleccione **Enviar usando Push Max**.

![Pestaña de configuración de entrega de un paso de mensaje push de Android con la opción "Enviar usando Push Max".]({% image_buster /assets/img_archive/push_max_canvas.png %})

{% endtab %}
{% endtabs %}

Las dos funciones siguientes, Intelligent Timing y Time to Live, pueden utilizarse conjuntamente con Push Max para aumentar potencialmente la capacidad de entrega de sus notificaciones push para Android.

### Intelligent Timing

Push Max funciona mejor cuando [la sincronización inteligente]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/) está activada. Intelligent Timing puede calcular y enviar la notificación push en el momento en que es más probable que el usuario esté utilizando la aplicación y que la notificación push llegue a su destino.

### Tiempo de vida (TTL)

Time to Live (TTL) puede rastrear notificaciones push fallidas a Firebase Cloud Messaging (FCM) y reintentar la notificación cuando es probable que el usuario la reciba.

Por defecto, el tiempo de vida está fijado en 28 días, que es el máximo. Puede reducir el TTL predeterminado para todos los nuevos mensajes push de Android desde **Configuración** > **Configuración del área de trabajo** > **Tiempo de vida (TTL) de push**, o puede configurar el número de días por mensaje en la pestaña **Configuración** al redactar una notificación push de Android.

![Campo Tiempo de vida configurado a 28 días.]({% image_buster /assets/img_archive/time_to_live.png %}){: style="max-width:60%"}

## Lo que hay que saber

### Códigos de promoción

Te recomendamos que no utilices [códigos promocionales]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes/) Braze en mensajes en los que Push Max esté activado.

Esto se debe a que los códigos de promoción son únicos. Si una notificación push que contiene un código promocional no se entrega, cuando esa notificación se reenvíe debido a Push Max, se enviará un nuevo código promocional. Esto puede hacer que consuma los códigos promocionales más rápido de lo esperado.

### Propiedades de los eventos Canvas y propiedades de entrada

Es posible que Push Max no funcione como se espera si incluye en su mensaje referencias líquidas a [las propiedades de entrada del lienzo o a las propiedades de los eventos]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties). Esto se debe a que las propiedades de entrada y evento no están disponibles cuando Push Max está intentando reenviar el mensaje.
