---
title: "Movable Ink"
article_title: Movable Ink
alias: "/partners/movable_ink/"
description: "Este artículo de referencia describe la asociación entre Braze y Movable Ink, una plataforma de software basada en la nube que ofrece a los especialistas en marketing digital una forma de crear experiencias visuales atractivas y únicas que emocionen a los clientes."
page_type: partner
search_tag: Partner

---

# Movable Ink

> [Movable Ink](https://www.movableink.com/) es una plataforma de software basada en la nube que ofrece a los especialistas en marketing digital una forma de crear experiencias visuales atractivas y únicas que emocionen a los clientes. La plataforma Movable Ink proporciona valiosas opciones de personalización que pueden insertarse fácilmente en tus campañas. 

_Esta integración está mantenida por Movable Ink._

## Sobre la integración

Amplía nuestras capacidades creativas aprovechando las características de Creatividad Inteligente de Movable Ink, como el sondeo, el temporizador de cuenta atrás y el rasca y gana. La integración de Movable Ink y Braze potencia un enfoque más completo de los mensajes dinámicos basados en datos, proporcionando a los usuarios elementos en tiempo real sobre las cosas que importan.

## Requisitos previos

| Requisito | Descripción |
|---|---|
| Cuenta Movable Ink | Se necesita una cuenta Movable Ink para beneficiarse de esta asociación. |
| Origen de datos | Tendrás que conectar un origen de datos a Movable Ink. Esto puede hacerse mediante CSV, importación del sitio web o API. Asegúrate de que pasas los datos con un identificador unificador entre Braze y Movable Ink (por ejemplo, `external_id`).
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Casos prácticos

- Recapitulaciones mensuales o de extremo a extremo personalizadas.
- Personaliza dinámicamente imágenes para correo electrónico, push o notificaciones enriquecidas basándote en el último comportamiento conocido.<br>
	Por ejemplo: 
	- Utiliza un mensaje push enriquecidas para crear dinámicamente un calendario de eventos extrayendo datos de la API. 
	- Utilizar el temporizador de cuenta atrás para notificar a los usuarios cuando se acerca una gran venta (por ejemplo, el Viernes Negro, el Día de San Valentín o las ofertas de las fiestas).
	- Utiliza la característica Rasca y gana como una forma divertida e interactiva de desembolsar códigos promocionales.

## Capacidades compatibles con Movable Ink

Intelligent Creative tiene muchas ofertas que los usuarios de Braze pueden aprovechar. La siguiente lista muestra qué capacidades son compatibles. 

| Capacidad de Movable Ink | Característica | Notificación push enriquecida | Mensajería dentro de la aplicación / tarjetas de contenido / correo electrónico | Detalles |
| ---------------------- |---| ---------------------- | -------------------------------- | ------- |
| Optimizador Creativo | Contenido de la pantalla A/B | ✗ | ✔ | |
|| Optimiza | ✗ | ✔* | \* Debes utilizar la solución de vinculación profunda de Branch |
| Normas de selección | Fecha | ✔* | ✔ | \* Se admite pero no se recomienda porque las notificaciones push se almacenan en caché al recibirlas y no se actualizan. |
|| Día de la semana | ✔* | ✔ | \* Se admite pero no se recomienda porque las notificaciones push se almacenan en caché al recibirlas y no se actualizan. |
|| Hora del día | ✔* | ✔ | \* Se admite pero no se recomienda porque las notificaciones push se almacenan en caché al recibirlas y no se actualizan. |
| Historias/Actividad de comportamiento | | ✔* | ✔* | \* El identificador único de usuario utilizado para Braze debe estar vinculado al identificador de tu ESP. |
| Vinculación en profundidad dentro de la aplicación | | ✔* | ✔* | \* Para ofrecer una experiencia optimizada a tus clientes, utiliza una solución de vinculación en profundidad establecida a través de Branch, o una solución validada con el equipo de Experiencia del Cliente de Movable Ink. |
| Aplicaciones | Temporizador de cuenta atrás | ✔* | ✔ | \* Se admite pero no se recomienda porque las notificaciones push se almacenan en caché al recibirlas y no se actualizan. |
|| Encuesta | ✗ | ✔* | \* Después de votar, dejará la aplicación para ser una página de inicio móvil |
|| Rascar | ✔* | ✔* | \* Al hacer clic, saldrás de la aplicación para vivir la experiencia de Rasca y Gana |
|| Video | ✔* | ✔* | \* Sólo GIF animados, <br>Para Android, Braze requiere [soporte GIF]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/customization/gifs/) en la implementación |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Integración

### Paso 1: Crear un origen de datos para Movable Ink

Los clientes tendrán que crear un origen de datos que puede ser un CSV, la importación de un sitio web o la integración de una API.

![Diferentes opciones de origen de datos que aparecerán: Carga CSV, sitio web o integración API.]({% image_buster /assets/img/movable_ink/movable_ink1.png %})

{% tabs local %}
{% tab Origen de datos CSV %}
- **Origen de datos CSV**: Cada fila debe tener al menos una columna de segmento y una columna de contenido. Una vez cargado tu CSV, selecciona qué columnas deben utilizarse para orientar el contenido. [Ejemplo de archivo CSV]({% image_buster /assets/download_file/movable_ink_CSV.csv %})

![Los campos que aparecerán al seleccionar "CSV" como origen de datos.]({% image_buster /assets/img/movable_ink/movable_ink2.png %})
{% endtab %}
{% tab Origen de datos del sitio web %}
- **Origen de datos del sitio web**: Cada fila debe tener al menos una columna de segmento y una columna de contenido. Una vez cargado tu CSV, selecciona qué columnas deben utilizarse para orientar el contenido.
  - Dentro de este proceso, tendrás que mapear:
    - Qué campos se utilizarán como Segmentos
    - Qué campos quieres como campos de datos que se puedan personalizar dinámicamente en la creatividad (por ejemplo: atributos de usuario o atributos personalizados como nombre, apellidos, ciudad, etc.)

![Los campos que aparecerán al seleccionar "Sitio web" como origen de datos.]({% image_buster /assets/img/movable_ink/movable_ink3.png %})
{% endtab %}
{% tab Integraciones API %}
- **Integraciones API**: Utiliza la API de tu empresa para impulsar contenidos directamente desde una respuesta API.

![Los campos que aparecerán al seleccionar "Integración de API" como origen de datos]({% image_buster /assets/img/movable_ink/movable_ink4.png %})
{% endtab %}
{% endtabs %}

### Paso 2: Crea una campaña en la plataforma Movable Ink

Desde la pantalla de inicio de Movable Ink, crea una campaña. Puedes seleccionar entre correo electrónico de HTML, correo electrónico de imagen o un bloque que puede utilizarse en cualquier canal, incluidos push, mensajes dentro de la aplicación y tarjetas de contenido (sugerido).

También te sugerimos que eches un vistazo a las distintas opciones de contenido disponibles mediante bloques.

![Una imagen del aspecto de la plataforma Movable Ink al crear una nueva campaña Movable Ink.]({% image_buster /assets/img/movable_ink/movable_ink5.png %}){: style="max-width:70%"}

Movable Ink tiene un sencillo editor para que arrastres y sueltes elementos como texto o imágenes. Si has rellenado tu origen de datos, puedes generar dinámicamente una imagen utilizando las propiedades de los datos. Además, también puedes crear alternativas dentro de este flujo para los usuarios si se envía la campaña y un usuario no se ajusta a los criterios de personalización.

![El editor de bloques Movable Ink mostrando los diferentes elementos personalizables.]({% image_buster /assets/img/movable_ink/create_campaign2.png %})

Antes de finalizar tu campaña, asegúrate de obtener una vista previa de las imágenes dinámicas y de probar los parámetros de consulta para ver qué aspecto tendrán las imágenes al visualizarlas. ¡Una vez completado, se generará una URL dinámica que podrás insertar en Braze!

Para más información sobre cómo utilizar la Plataforma Movable Ink, visita el [centro de soporte de Movable Ink](https://support.movableink.com/)

### Paso 3: Obtener la URL del contenido de Movable Ink

Para incluir contenido de Movable Ink en los mensajes de Braze, debes localizar la URL de origen que Movable Ink te ha proporcionado. 

Para obtener la URL de origen, debes haber configurado el contenido en el panel de Movable Ink y, a partir de ahí, finalizar y exportar tu contenido. En la página **Finalizar**, copia la URL de origen(`img src`) de la etiqueta creativa.

![La página que aparece después de haber completado tu campaña Movable Ink, aquí encontrarás la URL de tu contenido.]({% image_buster /assets/img/movable_ink/obtain_url.png %}){: style="max-width:80%;"}

A continuación, en la Plataforma Braze, pega la URL en el campo correspondiente. Los campos adecuados para tu canal de mensajería se encuentran en el paso 4. Por último, sustituye cualquier etiqueta de fusión (como {% raw %}```&mi_u=%%email%%```{% endraw %}) por la variable de Liquid correspondiente (como {% raw %}```&mi_u={{${email_address}}}```{% endraw %}).

### Paso 4: Experiencia Braze

{% tabs local %}
{% tab Correo electrónico %}
En la plataforma Braze, pega tu etiqueta creativa en el cuerpo de tu correo electrónico.![]({% image_buster /assets/img/movable_ink/web2.png %}){: style="max-width:90%"}<br><br>

{% endtab %}
{% tab Notificación push %}

1. En la Plataforma Braze:
	- Android Push: Pega la URL en los campos **Imagen de icono push** e **Imagen de notificación expandida**.<br>![]({% image_buster /assets/img/movable_ink/android.png %}){: style="max-width:60%"}<br><br>
	- Push de iOS: Pega la URL en el campo Enlace **multimedia** e indica el formato de archivo que utilizas.<br>![]({% image_buster /assets/img/movable_ink/ios.png %}){: style="max-width:60%"}<br><br>
	- Web Push: Pega la URL en los campos **Imagen de icono push** e **Imagen de notificación grande**.<br>![]({% image_buster /assets/img/movable_ink/web.png %}){: style="max-width:60%"}<br><br>
2. Para asegurarte de que las imágenes no se almacenan en caché, antepone a la URL del mensaje etiquetas de Liquid vacías: <br>{% raw %}```{% if true %}{% endif %}https://movable-ink-image-url-goes-here```{% endraw %}

{% endtab %}
{% tab Mensaje dentro de la aplicación %}

1. En la plataforma Braze, pega la URL en el campo **Medios de notificación enriquecida**.![]({% image_buster /assets/img/movable_ink/image.png %}){: style="max-width:60%"}<br><br>
2. Proporciona una URL única para evitar el almacenamiento en caché. Para confirmar que las imágenes en tiempo real de Movable Ink funcionan y no se verán afectadas por el almacenamiento en caché, utiliza Liquid para añadir una marca de tiempo al final de la URL de la imagen de Movable Ink.

Para ello, utiliza la siguiente sintaxis, sustituyendo la URL de la imagen según sea necesario:
{% raw %}
```
{% assign timestamp = "now" | date: "%s" %}
{% assign img = "https://movable-ink-image-url-goes-here" | append:timestamp %}
{{img}}
```
{% endraw %}
Esta plantilla tomará la hora actual (en segundos), la añadirá al final de la pestaña de la imagen de Movable Ink (como parámetro de consulta) y, a continuación, mostrará el resultado final. Puedes obtener una vista previa con la pestaña **Prueba**, que evaluará el código y mostrará una vista previa.

**3\.** Por último, reevalúa la pertenencia a un segmento. Para ello, habilita la opción `Re-evaluate audience membership and liquid at send-time` situada en el paso **Audiencias** objetivo de una campaña. Si esta opción no está disponible, ponte en contacto con tu administrador del éxito del cliente o con el soporte de Braze. Esta opción indicará a los SDK de Braze que vuelvan a solicitar la campaña, proporcionando una URL única cada vez que se desencadene un mensaje dentro de la aplicación.

{% endtab %}
{% tab Tarjeta de contenido %}

1. En la plataforma Braze, pega la URL en el campo **Medios de notificación enriquecida**.![]({% image_buster /assets/img/movable_ink/image.png %}){: style="max-width:60%"}<br><br>
2. Para móvil: Las imágenes de las tarjetas de contenido en iOS y Android se almacenan en caché cuando se reciben y no se actualizan. 
  - Como solución, programa tu campaña como un mensaje recurrente diario, semanal o mensual, con su correspondiente caducidad, para que la tarjeta de contenido vuelva a planificarse. Por ejemplo, una tarjeta de contenido que debe actualizarse una vez al día debe configurarse como un envío diario programado con una caducidad de 1 día.
3. Para garantizar que las imágenes en tiempo real de Movable Ink funcionen y no se vean afectadas por el almacenamiento en caché cuando se vuelva a crear la plantilla de la tarjeta de contenido, utiliza Liquid para añadir una marca de tiempo al final de la URL de la imagen de Movable Ink.

Para ello, utiliza la siguiente sintaxis, sustituyendo la URL de la imagen según sea necesario:
{% raw %}
```
{% assign timestamp = "now" | date: "%s" %}
{% assign img = "https://movable-ink-image-url-goes-here" | append:timestamp %}
{{img}}
```
{% endraw %}
Esta plantilla tomará la hora actual (en segundos), la añadirá al final de la pestaña de la imagen de Movable Ink (como parámetro de consulta) y, a continuación, mostrará el resultado final. Puedes obtener una vista previa con la pestaña **Prueba**, que evaluará el código y mostrará una vista previa.

{% endtab %}
{% endtabs %}

## Solución de problemas

### ¿Las imágenes dinámicas no se muestran correctamente? ¿Con qué canal tienes dificultades?
- **Push**: Asegúrate de que tienes una lógica vacía antes de la URL de tu imagen Movable Ink: <br>{% raw %}```{% if true %}{% endif %}https://movable-ink-image-url-goes-here```{% endraw %}
- **Mensajes dentro de la aplicación y tarjetas de contenido**: Asegúrate de que la URL de la imagen es única para cada impresión. Esto puede hacerse añadiendo el Liquid adecuado para que cada URL sea diferente. Consulta [las instrucciones de los mensajes dentro de la aplicación y de la tarjeta de contenido]({{site.baseurl}}/partners/message_personalization/dynamic_content/visual_and_interactive_content/movable_ink/#step-4-braze-experience). 
- **La imagen no se carga**: Asegúrate de sustituir cualquier "etiqueta de fusión" por los campos Liquid correspondientes en el panel de Braze. Por ejemplo: {% raw %}```https://mi-msg.com/p/rp/image.png?mi_u=%%email%%```{% endraw %} con {% raw %}```https://mi-msg.com/p/rp/image.png?mi_u={{${email_address}}}```{% endraw %}.

### ¿Tienes problemas para mostrar GIFs en Android?
- Android requiere soporte GIF en la implementación. Sigue el artículo de [personalización de mensajes dentro de la aplicación]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/customization/gifs/) de Android si no tienes esta configuración.


[1]: https://www.movableink.com/
[origen de datos]: ({% image_buster /assets/img/movable_ink/movable_ink1.png %})
[1]: ({% image_buster /assets/img/movable_ink/android.png %})
[2]: ({% image_buster /assets/img/movable_ink/ios.png %})
[3]: ({% image_buster /assets/img/movable_ink/web.png %})
