---
nav_title: Seguimiento de clics LINE
article_title: LINE Seguimiento de clics
page_order: 2
description: "Esta página explica cómo activar el seguimiento de clics en tus mensajes de LINE, probar los enlaces acortados, utilizar tu dominio personalizado en los enlaces rastreados y mucho más."
page_type: reference
alias: /line/click_tracking/
channel:
 - LINE
---

# Seguimiento de clics LINE

> Esta página explica cómo activar el seguimiento de clics en tus mensajes de LINE, probar los enlaces acortados, utilizar tu dominio personalizado en los enlaces rastreados y mucho más.


Cuando el seguimiento de clics de LINE está activado, Braze acorta automáticamente tus URL, añade mecanismos de seguimiento y registra los clics en tiempo real. Mientras que LINE te ofrece datos agregados de clics, Braze te proporciona información granular sobre el usuario que es oportuna y procesable. Estos datos te permiten crear estrategias de segmentación y reorientación más específicas, como segmentar a los usuarios en función de su comportamiento al hacer clic y desencadenar mensajes en respuesta a clics concretos.

El seguimiento de clics de LINE puede utilizarse para mensajes de texto, enriquecidos y basados en tarjetas. Admite enlaces dentro de botones y áreas mapeadas con imágenes que tengan una URL como acción al hacer clic. También puedes personalizar las URL utilizando Liquid y dominios personalizados.

## Cómo funciona

Puedes administrar la configuración del seguimiento de clics de LINE en la pestaña **Configuración** mientras redactas un mensaje. Si está activada, las URL se acortarán utilizando el dominio predeterminado de Braze (`https://brz.ai`) o el dominio personalizado especificado para el grupo de suscripción, y se personalizarán para el usuario.

Las URL que empiecen por `http://` o `https://` se acortarán. Puedes tener hasta 25 URL en un mensaje. Las URL acortadas que contengan personalización Liquid (como seguimiento a nivel de usuario o parámetros UTM) serán válidas durante dos meses.

## Configuración del seguimiento de clics

### Mensajes de texto

Para configurar el seguimiento de clics de un mensaje de texto:

1. Arrastra un mensaje de **texto** al compositor y añade una URL al campo de texto.

\![LÍNEA creador de mensajes con un mensaje de texto que contiene una URL larga: https://braze.com/docs/user_guide/message_building_by_channel/line/create/]({% image_buster /assets/img/line/click_tracking_text_message.png %})

{: start="2"}
2\. Ve a la pestaña **Configuración** y confirma que **el Seguimiento de clics** está activado. El seguimiento de clics está activado predeterminadamente para todos los mensajes nuevos.

{% alert note %}
Puedes ver vistas previas del enlace acortado mientras estás en la pestaña **Configuración** o **Vista previa & Prueba**. El enlace completo se mostrará en el compositor mientras construyes tu mensaje.
{% endalert %}

\![LINE pestaña "Configuración" del creador de mensajes con " con "Seguimiento de clics" activado y una vista previa Mensaje de texto que contiene una URL acortada: https://olaf.brz.ai/p/9rcfdqdD]({% image_buster /assets/img/line/click_tracking_settings.png %})

### Mensajes enriquecidos

Para configurar el seguimiento de clics de un mensaje enriquecido:

1. Arrastra un **mensaje enriquecido** al compositor y selecciona una plantilla.
2. Selecciona **URI** para el **comportamiento Al hacer clic** para el área tappable aplicable.
3. Introduce una URL en el campo **Abrir URL**.

\![LINE creador de mensajes con un mensaje enriquecido con dos áreas tapables que tienen cada una una URL.]({% image_buster /assets/img/line/rich_message_click_tracking.png %})

{: start="4"}
4\. Ve a la pestaña **Configuración** y confirma que **el Seguimiento de clics** está activado. El seguimiento de clics está activado predeterminadamente para todos los mensajes nuevos.

### Mensajes basados en tarjetas

Para configurar el seguimiento de clics de un mensaje basado en tarjetas:

1. Arrastra un **mensaje basado en tarjetas** al compositor.
2. Selecciona **URI** para el **comportamiento Al hacer clic** para las áreas de tarjetas o botones aplicables.

\![Creador de mensajes de LINE con un mensaje basado en tarjetas con dos botones que tienen cada uno una URL.]({% image_buster /assets/img/line/card_based_message_click_tracking.png %})

{: start="3"}
3\. Ve a la pestaña **Configuración** y confirma que **el Seguimiento de clics** está activado. El seguimiento de clics está activado predeterminadamente para todos los mensajes nuevos.

{% alert note %}
Las URL de los campos **Título** o **Descripción** no se acortarán porque en estos campos no se puede hacer clic dentro de LINE.
{% endalert %}

## Dominios personalizados

El seguimiento de clics de LINE te permite utilizar tu propio dominio para personalizar el aspecto de tus URL acortadas, lo que ayuda a mostrar una imagen de marca coherente. Para más información, consulta [Dominios personalizados]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/link_shortening/custom_domains).

## Personalización líquida en URLs

Puedes construir dinámicamente tu URL directamente dentro del compositor Braze, lo que te permite añadir parámetros UTM dinámicos a tus URL o enviar a los usuarios enlaces únicos (como dirigir a los usuarios a su carrito abandonado o a un producto específico que vuelva a estar en stock).
Las URL pueden generarse dinámicamente mediante el uso de cualquiera de las etiquetas de personalización de Liquid admitidas.

{% raw %}
```
https://example.com/?campaign_utm={{campaign.${api_id}}}&user_attribute={{custom_attribute.${attribute1}}}
```
{% endraw %}

También puedes acortar variables Liquid definidas de forma personalizada, como se muestra en el siguiente ejemplo:

{% raw %}
```liquid
{% assign url_var = {{event_properties.${url_slug}}} %}
https://example.com/{{url_var}}
```
{% endraw %}

## Acortar URLs generadas por variables Liquid

Braze acorta las URL renderizadas por Liquid, incluso las incluidas en propiedades desencadenadas por la API. Por ejemplo, si {% raw %}`{{api_trigger_properties.${url_value}}}`{% endraw %} representa una URL válida, acortaremos y haremos un seguimiento de esa URL antes de enviar el mensaje de LINE.

## Prueba

Antes de lanzar tu campaña o Canvas, es una buena práctica previsualizar y probar primero tu mensaje. Para ello, ve a la pestaña **Prueba** para obtener una vista previa y enviar un mensaje LINE a grupos de prueba de contenido o a un usuario individual.

Esta vista previa se actualizará con la personalización pertinente y la URL acortada. 

{% alert important %}
Si se crea un borrador dentro de un Canvas activo, no se generará una URL acortada. La URL acortada real se genera cuando se activa el borrador de Canvas.
{% endalert %}

## Informar

La tabla de rendimiento de LINE incluye la columna **Clics totales**, que muestra un recuento de eventos de clic por variante y una tasa de clics asociada. Para más detalles sobre las métricas de LINE, consulta [Rendimiento de los mensajes de LINE]({{site.baseurl}}/user_guide/message_building_by_channel/line/reporting).

\![Rendimiento de un paso en Canvas.]({% image_buster /assets/img/line/line_step_performance.png %}){: style="max-width:30%;"}

Los datos de los clics aparecerán automáticamente en el panel de análisis. 

\![Panel de análisis del rendimiento de LINE.]({% image_buster /assets/img/line/line_performance.png %})

## Reorientar a los usuarios

Puedes reorientar a los usuarios que hayan hecho clic en una URL de un mensaje de LINE utilizando los siguientes filtros de segmentación y desencadenantes:

- Desencadenantes basados en la acción
    - Interactúa con la campaña
    - Interactúa con Step

\![LÍNEA desencadenante de entrega basada en acciones.]({% image_buster /assets/img/line/line_action_based.png %})

- Filtros de segmentación
    - Campaña clicada/abierta
    - Campaña clicada/abierta o Canvas con etiqueta 
    - Paso clicado/abierto

\![Grupo de filtros que muestra los tres filtros de segmentación: "Campaña clicada/abierta", "Campaña clicada/abierta o Canvas con etiqueta" y "Paso clicado/abierto".]({% image_buster /assets/img/line/line_segmentation_filters.png %})

## Preguntas más frecuentes

### ¿Los enlaces que recibo al realizar el envío de prueba son URL reales?

Sí, se generarán URL reales al realizar el envío de prueba. Sin embargo, la URL exacta enviada en una campaña lanzada puede diferir de la enviada en un envío de prueba.

### ¿Puedo añadir parámetros UTM a una URL antes de acortarla?

Sí, se pueden añadir parámetros estáticos y dinámicos.

### ¿Durante cuánto tiempo son válidas las URL acortadas?

Las URL personalizadas son válidas durante dos meses desde el momento del registro de la URL.

### ¿Es necesario instalar el SDK de Braze para acortar las URL?

No, el seguimiento de clics funciona sin ninguna integración de SDK.

### ¿Puedo saber qué usuarios individuales hacen clic en una URL?

Sí. Cuando el seguimiento de clics está activado, puedes reorientar a los usuarios que han hecho clic en las URL utilizando [los filtros de reorientación de LINE](#retargeting-users).

### ¿Funciona el seguimiento de clics con vínculos profundos o universales?

El seguimiento de los clics no funciona con los vínculos en profundidad. Puedes acortar enlaces universales de proveedores como Branch o Appsflyer, pero Braze no puede solucionar los problemas que puedan surgir al hacerlo (como romper la atribución o no redirigir).

### ¿Las vistas previas en la aplicación LINE cuentan como clics?

No, no contribuyen a la tasa de clics de los mensajes de LINE.