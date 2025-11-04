---
nav_title: "Historias push"
article_title: Historias push
page_order: 2
page_type: reference
description: "Este artículo de referencia explica qué son las historias push, cómo crear una y algunas preguntas frecuentes."
channel:
  - push

---

# Historias push

> Las historias push son un nuevo tipo de notificación push introducido por Braze. Esta característica toma la funcionalidad de carrusel de fotos popularizada en Instagram y Facebook y permite a los especialistas en marketing crear un carrusel de páginas dentro de un push que cuente una historia rica y cohesionada. Estas páginas constan de una imagen, una acción de clic, un título y una descripción. Tus usuarios pueden deslizarse por estas páginas y ver la historia contada por ti.

| Ejemplo de Android (Ampliado) | Ejemplo de IOS (Ampliado) |
| :-----: | :----------: |
| \![]({% image_buster /assets/img_archive/pushstories_android_preview.png %}) | \![]({% image_buster /assets/img_archive/pushstories_ios_preview.png %}) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
En las versiones 3.13.0+ del SDK de iOS, debido a un cambio en la forma en que el SDK descarga las imágenes, no se mostrará una miniatura de la primera imagen en la vista condensada del push. Asegúrate de que el texto de tu mensaje pide a los usuarios que amplíen el push para ver las imágenes.
{% endalert %}

## Requisitos previos

Se necesitan las siguientes versiones del SDK para recibir historias push:

{% sdk_min_versions swift:5.0.0 android:2.2.0 %}


## Cómo utilizar las historias push

\![]({% image_buster /assets/img_archive/pushstories_composer_dropdown2.png %}){: style="float:right;max-width:50%;margin-left:15px;margin-bottom:15px;"}

Para utilizar las historias push, haz lo siguiente:

1. Crea una [campaña push]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/).
2. Para tu **Tipo de notificación**, selecciona **Historias push**.
3. Selecciona **iOS** o **Android**. Ten en cuenta que si seleccionas ambas opciones para un mensaje push, no aparecerá la opción de crear una historia push. 

### Compositor de historias push

Para crear una página, realiza los siguientes pasos:

1. Haz clic en **Gestionar páginas** desde el compositor principal.
    <br><br>\![]({% image_buster /assets/img_archive/pushstories_add_pages.png %}){: style="max-width:70%"}<br><br>
2. Inserta una imagen para cada página, junto con el comportamiento de clic para esa imagen.
3. Si lo deseas, añade un **Título** y una **Descripción** para cada página. Si utilizas un título y una descripción para una página, deben insertarse para todas las páginas.

Las vistas previas se reflejarán y son interactivas.

\![]({% image_buster /assets/img_archive/pushstories_composer.png %}){: style="max-width:60%"}

{% alert important %}
Si introduces imágenes con [Contenido conectado]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/#about-connected-content), asegúrate de que la URL de tu imagen comienza por `https://`. Si utilizas `http://`, tu aplicación se bloqueará.
{% endalert %}

### Especificaciones de imagen y texto

Las siguientes especificaciones de imagen y texto se aplican a la parte del carrusel de fotos de las historias push. Para obtener información sobre el push básico con el que interactúan los usuarios para activar la historia push, consulta las [directrices de texto para push]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/#native-mobile-push-notifications).

{% tabs %}
{% tab Images %}

- **Relación de imagen:** 2:1 (obligatorio)
- **Tamaño de imagen recomendado:** 500 KB
- **Tamaño máximo de la imagen:** 5 MB
- **Tipos de archivos:** PNG, JPEG

{% endtab %}
{% tab Text %}

- **Título:** 30 caracteres (recomendado)
- **Descripción:** 30 caracteres (recomendado)

{% alert note %}
Aunque la longitud de los caracteres puede variar de un dispositivo a otro, el título y la descripción de las historias push están limitados a una línea cada uno. El resto de tu mensaje quedará truncado. Prueba siempre tu mensaje en un dispositivo real.
{% endalert %}

{% endtab %}
{% endtabs %}

### Segmentación de historias push

Cuando creas una campaña o Canvas, puedes filtrar a qué usuarios quieres dirigirte en función de si han hecho clic en una página de historias push. A continuación, selecciona la campaña y la página que quieres utilizar para dirigirte a tus usuarios.

### Análisis de historias push

El análisis será muy similar a la sección de análisis actual para notificaciones push. En los análisis de historias push, puedes abrir la métrica **Direct Opens** para ver los clics por página.

Tabla de rendimiento de push de iOS con ejemplos de análisis y detalles ampliados de la métrica Direct Opens.]({% image_buster /assets/img_archive/pushstories_analytics.png %})

## Solución de problemas

### iOS

#### Me he enviado una historia push pero no he recibido la notificación

Apple cuenta con normas específicas que impiden que se envíen determinados tipos de notificaciones a un dispositivo en función de una serie de factores diferentes. Esto incluye evaluar el plan de datos de los clientes, el tamaño de las notificaciones y la capacidad de almacenamiento de los clientes. Como resultado, a veces no se enviará ninguna notificación a tus clientes.

Son limitaciones impuestas por Apple que debes tener en cuenta al diseñar tu historia push.

#### Me envié una historia push, pero en su lugar vi la vista condensada

En determinadas situaciones en las que no se carguen todas las páginas, por ejemplo, debido a una pérdida de conexión de datos, las historias push sólo mostrarán la notificación condensada.

### Android

#### Las historias push no salen después de hacer clic en la imagen 

Por predeterminado, las historias push no se descartan en Android después de que el usuario haga clic en la imagen. Si quieres rechazar la notificación, llama a [`cancelNotification`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.push/-braze-notification-utils/index.html#-1466259649%2FFunctions%2F-1725759721).  

