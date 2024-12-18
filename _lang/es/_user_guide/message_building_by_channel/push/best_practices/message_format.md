---
nav_title: Formatos de los mensajes
article_title: Mensajes push y formatos de imagen
page_order: 5
page_type: reference
description: "En este artículo se describen los formatos de mensaje e imagen de las notificaciones push."
channel: push

---

# Formatos de mensajes push e imágenes

> Este artículo de referencia describe los formatos de mensaje e imagen de las notificaciones push.

Para obtener los mejores resultados, consulte las siguientes directrices sobre el tamaño de la imagen y la longitud del mensaje cuando elabore sus mensajes push. Puede haber alguna variación en función de la presencia de una imagen, del estado de las notificaciones (iOS) y de la configuración de la pantalla del dispositivo del usuario, así como del tamaño del dispositivo. En caso de duda, el texto debe ser breve y conciso.

## Push para iOS y Android

{% tabs local %}
{% tab Imágenes %}

**Tipo de imagen** | **Tamaño de imagen recomendado** | **Tamaño máximo de imagen** | **Tipos de archivo**
--- | --- | --- | ---
(iOS) 2:1 *Recomendado* | 500 KB | 5 MB | PNG, JPEG, GIF
(Android) ícono push | 500 KB | 5 MB | PNG, JPEG
(Android) Notificación ampliada | 500 KB | 5 MB | PNG, JPEG
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% endtab %}
{% tab Texto %}

| Tipo de mensaje | Longitud recomendada del mensaje (sólo texto) | Longitud de mensaje recomendada (enriquecida)
--- | ---
(iOS) Pantalla de bloqueo | 160 caracteres | 130 caracteres
(iOS) Centro de notificaciones | 160 caracteres | 130 caracteres
(iOS) Alerta de banner | 80 caracteres | 65 caracteres
(Android) Pantalla de bloqueo | 49 caracteres | N/A
(Android) Cajón de notificaciones | 597 caracteres | N/A
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 }

¿Te preguntas cuántos caracteres puedes utilizar en una notificación push de iOS sin que quede truncada? Consulta nuestras [directrices sobre el recuento de caracteres para iOS]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/#character-count).

{% endtab %}
{% tab Tamaño de la carga útil %}

**Plataforma** | **Tamaño**
--- | ---
antes de iOS 8 | 0,256 KB
después de iOS 8 | 2 KB
Android (FCM) | 4 KB
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Ejemplo de imagen %}
{% subtabs %}
{% subtab iOS %}

![Notificación push de iOS con el texto siguiente: "¡Hola! Esto es un push de iOS con una imagen" con un emoji. Hay una pequeña imagen junto al texto.]({% image_buster /assets/img_archive/braze_richpush1.png %}){: style="max-width:50%;"}
![Notificación push de iOS en un push duro con el mismo texto que el mensaje anterior con una imagen ampliada precediendo al texto.]({% image_buster /assets/img_archive/braze_richpush2.png %}){: style="max-width:50%;"}

{% endsubtab %}
{% subtab Android %}

![Notificación push de Android con una imagen grande bajo el texto del mensaje.]({% image_buster /assets/img_archive/android_push_img2.png %})

{% alert note %}
Las notificaciones con imágenes grandes se muestran mejor cuando se utiliza una imagen de al menos 600x300 píxeles.
{% endalert %}

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Ejemplo de texto %}
{% subtabs %}
{% subtab iOS %}

![Notificación push de iOS con el texto siguiente: "¡Hola! Esto es un push de iOS".]({% image_buster /assets/img_archive/iOS_push_notification_small.png %})

{% endsubtab %}
{% subtab Android %}
![Notificación push de Android mostrada en la pantalla de inicio.]({% image_buster /assets/img_archive/Push_Android_2.png %})
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Web push

{% tabs local %}
{% tab Imágenes %}

| **Navegador** | **Tamaño de icono recomendado**
| --- | ---
Chrome | 192 x 192 ≥
Firefox | 192 x 192 ≥
Safari | 192 x 192 ≥ (Los íconos son configurables por campaña con Safari 16 en macOS 13+)
Opera | 192x192 ≥
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

| **Navegador** | **Plataforma** | **Tamaño de imagen grande**
| --- | --- | ---
Chrome | Android | Relación de aspecto 2:1
Firefox | Android | N/A
Chrome | Windows | Relación de aspecto 2:1
Edge | Windows | Relación de aspecto 2:1
Firefox | Windows | N/A
Firefox | Windows | Relación de aspecto 2:1
Safari | macOS | N/A
Chrome | macOS | N/A
Firefox | macOS | N/A
Opera | macOS | N/A
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Texto %}

| **Navegador** | **Plataforma** | **Longitud máxima del título**  | **Longitud máxima del cuerpo del mensaje**
| --- | --- | --- | ---
Chrome | Android | 35 | 50
Firefox | Android | 35 | 50
Chrome | Windows | 50 | 120
Edge | Windows | 50 | 120
Firefox | Windows | 54 | 200
Opera | Windows | 50 | 120
Chrome | macOS | 35 | 50
Safari | macOS | 38 | 84
Firefox | macOS | 38 | 42
Opera | macOS | 38 | 42
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% endtab %}
{% endtabs %}


