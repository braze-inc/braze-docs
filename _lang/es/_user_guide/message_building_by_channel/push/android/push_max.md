---
nav_title: Push Max
article_title: Push Max
page_type: reference
description: "Push Max amplifica las notificaciones push de Android haciendo un seguimiento de las notificaciones push fallidas y reenviando el push cuando es más probable que el usuario lo reciba."

permalink: /user_guide/message_building_by_channel/push/android/push_max/
platform: Android
channel:
  - Push

---

# Push Max

> Infórmate sobre Push Max y cómo puedes utilizar esta característica para mejorar potencialmente la capacidad de entrega de las notificaciones push de Android a los [dispositivos OEM chinos]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/chinese_push_deliverability/).

## ¿Qué es Push Max?

Push Max amplifica las notificaciones push de Android haciendo un seguimiento de las notificaciones push fallidas y reenviando el push cuando es más probable que el usuario lo reciba.

Algunos dispositivos Android fabricados por fabricantes chinos de equipos originales (OEM), como Xiaomi, OPPO y Vivo, emplean un sólido esquema de optimización de la batería para prolongar su duración. Este comportamiento puede tener la consecuencia no deseada de cerrar el procesamiento en segundo plano de la aplicación, lo que reduce la capacidad de entrega de notificaciones push en estos dispositivos si la aplicación no está en primer plano. Esta circunstancia se da con mayor frecuencia en los mercados de Asia-Pacífico (APAC).

## Disponibilidad

- Disponible sólo para notificaciones push de Android
- No se admite para mensajes basados en acciones o desencadenados por la API.
- No se admite cuando se selecciona la opción de [enviar sólo al último dispositivo utilizado por el usuario]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#device-options) 

## Requisitos previos

Las notificaciones push enviadas mediante Push Max sólo se entregarán a dispositivos que tengan al menos la siguiente [versión mínima del SDK]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions):

{% sdk_min_versions android:29.0.1 %}

## Utilizar Push Max

{% tabs %}
{% tab Campaigns %}

Para utilizar Push Max en tu campaña:

1. Crea una campaña push.
2. Selecciona **Android Push** como plataforma.
3. Ve al paso **Programar la entrega**.
4. Selecciona **Enviar con Push Max**.

\![Sección Capacidad de entrega push de Android del paso Programar entrega con la opción "Enviar usando Push Max".]({% image_buster /assets/img_archive/push_max_campaigns.png %})

{% endtab %}
{% tab Canvas %}

Para utilizar Push Max en tu Canvas:

1. Añade un paso en Canvas con un mensaje.
2. Selecciona **Android Push** como plataforma.
3. Ve a la pestaña **Configuración de la entrega**.
4. Selecciona **Enviar con Push Max**.

\![Pestaña de configuración de entrega de un paso de mensajes push de Android con la opción "Enviar usando Push Max".]({% image_buster /assets/img_archive/push_max_canvas.png %})

{% endtab %}
{% endtabs %}

Las dos características siguientes, Intelligent Timing y Time to Live, pueden utilizarse junto con Push Max para aumentar potencialmente la capacidad de entrega de tus notificaciones push de Android.

### Intelligent Timing

Push Max funciona mejor cuando está activada la [función Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/). Intelligent Timing puede calcular y enviar la notificación push en el momento en que es más probable que el usuario esté utilizando la aplicación y sea más probable que se entregue el push.

### Tiempo de vida (TTL)

El tiempo de vida (TTL) puede realizar un seguimiento de las notificaciones push fallidas a la mensajería en la nube de Firebase (FCM) y reintentar la notificación cuando sea probable que el usuario la reciba.

Por defecto, el Tiempo de vida está predeterminado en 28 días, que es el máximo. Puedes disminuir el TTL predeterminado para todos los nuevos mensajes push de Android desde **Configuración** > **Configuración del espacio de trabajo** > **Configuración push**, o puedes configurar el número de días en función de cada mensaje en la pestaña **Configuración** al redactar una notificación push de Android.

\![Campo Tiempo de vida ajustado a 28 días.]({% image_buster /assets/img_archive/time_to_live.png %}){: style="max-width:60%"}

## Lo que debes saber

### Códigos promocionales

Te recomendamos que no utilices [códigos promocionales]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes/) Braze en mensajes en los que esté activado Push Max.

Esto se debe a que los códigos promocionales son únicos. Si una notificación push que contiene un código promocional no se entrega, cuando esa notificación se vuelva a enviar debido a Push Max, se enviará un nuevo código promocional. Esto puede hacer que consumas códigos promocionales más rápido de lo esperado.

### Propiedades del evento Canvas y propiedades de la entrada

Es posible que Push Max no funcione como se espera si incluyes en tu mensaje referencias Liquid a [propiedades de entrada del Canvas o propiedades del evento]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties). Esto se debe a que las propiedades de la entrada y del evento no están disponibles cuando Push Max intenta reenviar el mensaje.
