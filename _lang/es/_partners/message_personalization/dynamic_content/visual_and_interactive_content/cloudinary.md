---
nav_title: Cloudinary
article_title: Cloudinary
description: "Este artículo de referencia describe la asociación entre Braze y cloudinary."
alias: /partners/cloudinary/
page_type: partner
search_tag: Partner
---

# Cloudinary

> [Cloudinary](https://www.cloudinary.com?utm_source=braze_partner_page) es una plataforma de imágenes y video que se utiliza para gestionar, editar, optimizar y entregar imágenes y video a escala a cualquier campaña a través de canales y recorridos del cliente. Cuando se integra y habilita, la gestión de medios de Cloudinary potencia la entrega de activos dinámica, contextual y personalizada para tus campañas Braze y Canvases. 

## Acerca de esta integración

Conectar Cloudinary a Braze da a las marcas acceso a los medios visuales almacenados en los activos de Cloudinary para utilizarlos en los canales de mensajería de Braze. Con los enlaces dinámicos de Cloudinary, puedes seleccionar y personalizar imágenes y videos en tiempo real basándote en los atributos de usuario de Braze. Juntos, Cloudinary y Braze permiten crear campañas visualmente ricas y personalizadas que cuentan la historia de cada producto y entregan experiencias únicas a escala.

En esta página se describen cuatro métodos posibles, aunque no exhaustivos, de integración entre Cloudinary y Braze. Estos métodos de integración se basan principalmente en la modificación de enlaces de activos copiados manualmente de la biblioteca multimedia de Cloudinary. 

{% alert important %}
Son posibles métodos de integración más avanzados, como el uso de [contenido conectado]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content) para llamar a la [API de administración](https://cloudinary.com/documentation/admin_api#banner) de Cloudinary, pero el enfoque variará según el cliente. Ponte en contacto con tu administrador del éxito del cliente de Cloudinary y Braze para que te oriente.
{% endalert %}

## Requisitos previos

| Requisitos     | Descripción |                        
|-----------------------|-----------------|
| Cuenta Cloudinary  | Se requiere una [Cuenta Cloudinary](https://cloudinary.com/users/register_free?utm_source=braze+docs+page) para beneficiarse de esta asociación  |
{: .reset-td-br-1 .reset-td-br-2 role=“presentation”}

## Métodos de integración

{% alert tip %}
Algunos de estos métodos de integración utilizan las Transformaciones Cloudinary de `f_auto` y `q_auto`, que ofrecen una personalización más profunda del comportamiento y la apariencia de los activos de [imagen](https://cloudinary.com/documentation/image_transformations#banner) y [video](https://cloudinary.com/documentation/video_manipulation_and_delivery#banner). Para más información sobre cómo modificar el enlace de un activo de Cloudinary para incluir Transformaciones, consulta [Estructura de la URL de Transformación](https://cloudinary.com/documentation/image_transformations#transformation_url_structure).
{% endalert %}

{% tabs %}
{% tab Cloudinary DAM %}

## Selecciona activos de campaña a través de Cloudinary DAM

La forma más directa de utilizar imágenes y videos directamente desde el DAM de Cloudinary en tus campañas y lienzos Braze es extraer la URL de la **página de** activos de la biblioteca multimedia de Cloudinary **.** 

![Una vista en cuadrícula de la Biblioteca de Activos de Imagen de Cloudinary, con la parte superior derecha de una de las imágenes resaltada, mostrando un tooltip de "Copiar URL".]({% image_buster /assets/img/cloudinary/one.png %})

### Configuración de imágenes y GIFs

1. Copia la URL de la imagen o GIF del DAM en Cloudinary yendo a **Activos** > **Biblioteca multimedia** > **Activos** > **Copiar URL**.
2. Crea la etiqueta de imagen en HTML, y luego añade `f_auto,q_auto` a la URL copiada para optimizar la imagen o GIF.

#### Ejemplo de URL de imagen

{% raw %}
```bash
<img src="https://res.cloudinary.com/demo/image/upload/v1678993440/f_auto,q_auto/cld-sample.jpg" alt="Summer Campaign">
</img>
```
{% endraw %}

### Configuración de videos

1. Copia la imagen o el enlace GIF del DAM en Cloudinary yendo a **Activos** > **Biblioteca multimedia** > **Activos** > **Copiar URL**.
2. Crea la etiqueta video en HTML, y luego añade `f_auto,q_auto` a la URL copiada para optimizar automáticamente el formato y la calidad del video.

#### Ejemplo de URL de video

{% raw %}
```bash
<video class="video" autoplay muted playsinline controls>
  <source src="https://res.cloudinary.com/demo/video/upload/v1651840278/f_auto,q_auto/samples/cld-sample-video.mp4">
</video>
```
{% endraw %}

Consulta [el video]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/video/) para ver consideraciones específicas sobre Android e iOS. 

{% endtab %}
{% tab Convert videoes into GIFs %}

## Convierte videos en GIFs para correos electrónicos

Utiliza la [Transformación Cloudinary](https://cloudinary.com/documentation/image_transformations/) de `f_auto:animated` para convertir automáticamente activos de video en GIFs. Esto es especialmente valioso si utilizas el canal de correo electrónico Braze, ya que los GIF están optimizados para reducir la carga útil del correo electrónico, que, si es demasiado alta, puede causar problemas de capacidad de entrega. 

### Configuración de la conversión

1. Copia la URL del video desde el DAM de Cloudinary.
2. Crea la etiqueta de imagen y añade `f_auto:animated,fl_lossy` para reducir el tamaño del GIF y elegir el mejor formato animado para el cliente.
3. Añade `c_scale,w_nnn` para que se corresponda con la anchura deseada del GIF en el diseño del correo electrónico.
4. Añade `e_loop` para hacer un bucle con la animación.

#### Ejemplo de URL GIF

{% raw %}
```
https://res.cloudinary.com/demo/video/upload/c_scale,w_500,e_loop/f_auto:animated,fl_lossy/samples/cld-sample-video.gif
```
{% endraw %}

{% endtab %}
{% tab Target attributes %}

## Selecciona dinámicamente los activos de la campaña en función de los atributos de segmentación

Este método de integración habilita la personalización dinámica de los medios, seleccionando de forma inteligente el mejor activo para cada usuario en función de sus atributos en tiempo real. 

Si incluyes etiquetas Liquid como parámetros en un enlace Cloudinary dentro de un mensaje de campaña Braze, cuando se envíe el mensaje, los atributos Braze asociados sustituirán dinámicamente a las etiquetas Liquid. Puede tratarse de datos específicos del usuario, como el idioma o el nivel de cliente. Cloudinary utilizará entonces esos atributos para determinar qué activo de la campaña se ajusta mejor a ese usuario, y le devolverá automáticamente la imagen o el video correctos. Esto hace que los destinatarios sólo reciban activos que sean contextualmente relevantes y aprobados por la marca.

### Cómo funciona

Cloudinary organiza los activos de la campaña mediante [etiquetas](https://cloudinary.com/documentation/assets_onboarding_metadata_tags_tutorial#tags) y [metadatos estructurados (SMD](https://cloudinary.com/documentation/assets_onboarding_metadata_tags_tutorial#structured_metadata) ) para facilitar su búsqueda. 

Cada activo de campaña se agrupa bajo una etiqueta de campaña (por ejemplo, `spring_launch`) y se enriquece con campos de metadatos estructurados que corresponden a atributos Braze como `language=en` o `tier=gold`. Cuando Braze llama al enlace Cloudinary, una [función personalizada](https://cloudinary.com/documentation/custom_functions#javascript_filters) procesa los atributos entrantes, busca el activo con etiquetas y metadatos coincidentes y, a continuación, devuelve la coincidencia más adecuada. 

Si no se encuentra una coincidencia exacta, la función selecciona automáticamente una alternativa o "siguiente mejor" opción para la continuidad en cada experiencia. Cuando se selecciona el activo, la capa de transformación de Cloudinary (por ejemplo, `f_auto` o `q_auto`) optimiza los medios para su entrega. Esta combinación de etiquetado, metadatos y funciones personalizadas ofrece a los desarrolladores una forma flexible, basada en API, de automatizar la entrega personalizada de activos.

{% alert tip %}
Consulta [el repositorio GitHub](https://github.com/cloudinary-devs/braze-personalization) de Cloudinary [`braze-personalization` para obtener instrucciones sobre cómo crear y aplicar funciones personalizadas, y un ejemplo de función personalizada para la selección de activos y opciones de alternativa para una campaña determinada.](https://github.com/cloudinary-devs/braze-personalization)  Para más información, ponte en contacto con el equipo de soporte de Cloudinary.
{% endalert %}

### Requisitos previos

Para habilitar la selección dinámica de activos, Cloudinary debe ser capaz de devolver un conjunto de activos basados en etiquetas y metadatos. Si el tipo de entrega de la lista está restringido, Cloudinary no puede proporcionar la lista dinámica necesaria para la selección personalizada de activos en las campañas Braze.
- Desbloquea el tipo de entrega de la lista: Abre la Configuración de Seguridad en tu Consola Cloudinary, y borra el elemento de la lista Recursos en Tipos de imagen restringidos.

### Configuración de selección dinámica

1. Configura la etiqueta y los metadatos de los activos en Cloudinary.
2. Sube tu función personalizada al DAM de Cloudinary.
3. Crea la URL Cloudinary para la etiqueta deseada.
4. Utilizando la URL de la etiqueta como base, añade etiquetas Liquid de imagen dinámica para incorporar atributos Braze y la función personalizada.

#### Ejemplo de URL

Este ejemplo supone que los activos en Cloudinary tienen dos campos SMD definidos ("localización" y "audiencia") rellenados con los valores esperados correspondientes a los atributos Braze. Además, los activos necesarios para la campaña han recibido la etiqueta "muestras", y la función personalizada `segmentedBanner.js` se ha cargado en la cuenta de Cloudinary. 

{% raw %}
```bash

// Use the appropriate Braze attributes.
{% assign audience = {{custom_attribute.${sample_audience_identifier}}} %} 
{% assign locale = {{${language}}}%} 

// The URL for the "samples" tag used in the campaign is https://papish.cloudinary.us/image/list/v1690000000/samples.json, which is the base for the dynamic image URL.
<img src="https://papish.cloudinary.us/image/list/f_auto,q_auto/$locale_#{locale}/$audience_!{audience}!/fn_select:js:v1700000000:segmentedBanner.js/v1690000000/campaigns/samples.json" alt="Banner"> 
```
{% endraw %}

##### URL de salida

- URL de salida para usuarios con audiencia `internal` y localización `en`: 
```
https://papish.cloudinary.us/image/list/f_auto,q_auto/$locale_!en!/$audience_!Internal!/fn_select:js:v1700000000:segmentedBanner.js/v1690000000/samples.json
```
- URL de salida para usuarios con audiencia `external` y localización `es`: 
```
https://papish.cloudinary.us/image/list/$locale_!es!/$audience_!External!/fn_select:js:v1700000000:segmentedBanner.js/v1690000000/samples.json
```
- URL de la imagen alternativa: 
```
https://papish.cloudinary.us/image/list/$locale_!unknown!/$audience_!unknown!/fn_select:js:v1700000000:segmentedBanner.js/v1690000000/samples.json
```

{% endtab %}
{% tab Personalized image generation %}

## Generación de imágenes personalizadas

[Las transformaciones de superposición de texto](https://cloudinary.com/documentation/accessible_media_visual_audio_clarity#text_overlays_on_images_and_videos/) de Cloudinary utilizan datos de usuario de Braze directamente dentro de un activo de Cloudinary. 

El siguiente ejemplo demuestra cómo se puede utilizar la Transformación `l_text` para insertar el nombre de un usuario en un activo. Se puede conseguir una mayor personalización aprovechando las etiquetas de Liquid al desarrollar campañas y Lienzos para determinar qué texto debe rellenar los parámetros de `l_text`.

Para obtener más orientación sobre cómo pueden utilizarse los parámetros de Transformación para diseñar un activo, ponte en contacto con tu equipo de soporte de Cloudinary.

### Ejemplo `l_text` Transformación

{% raw %}
```bash
{% assign first_name = {{${first_name}}}%} 
{% assign second_name = {{${last_name}}}%} 

<img src="https://res.cloudinary.com/demo/image/upload/l_text:Arial_300:%20{{first_name}}%20{{second_name}}%20,co_white,b_rgb:00000080/fl_layer_apply,g_north_west,y_200/docs/white-church-europe-sea.jpg">
```
{% endraw %}

#### Ejemplo de URL de salida

{% raw %}
```bash
<img src="https://res.cloudinary.com/demo/image/upload/l_text:Arial_300:%20John%20Smith%20,co_white,b_rgb:00000080/fl_layer_apply,g_north_west,y_200/docs/white-church-europe-sea.jpg">
```
{% endraw %}

![Una iglesia blanca con tejado azul que mira al mar, en la parte superior izquierda de la imagen las palabras "John Smith" se imponen sobre un gran rectángulo oscuro opaco.]({% image_buster /assets/img/cloudinary/two.png %})

```
{% endtab %}
{% endtabs %}
