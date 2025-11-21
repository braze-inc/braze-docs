---
nav_title: Tarjetas de contenido
article_title: Tarjetas de contenido
page_order: 1
layout: dev_guide
guide_top_header: "Tarjetas de contenido"
guide_top_text: "Con las tarjetas de contenido, puedes enviar a tus clientes un flujo dinámico y muy específico de contenido enriquecido dentro de las aplicaciones que les gustan, sin interrumpir su experiencia. <br><br>Las tarjetas de contenido se integran directamente en tu aplicación o sitio web, permitiéndote crear buzones de mensajes e interfaces personalizadas que amplían el alcance de otros canales, como el correo electrónico o las notificaciones push. Además, las Tarjetas de Contenido admiten más características personalizadas, como la fijación de tarjetas, el descarte de tarjetas, la entrega basada en API, el Contenido Conectado, tiempos de caducidad de tarjetas personalizados, análisis de tarjetas y una fácil coordinación con las notificaciones push. <br><br>**La disponibilidad de las tarjetas de contenido depende de tu paquete Braze. Ponte en contacto con tu director de cuentas o administrador del éxito del cliente para empezar."
description: "Esta página de inicio alberga las tarjetas de contenido Braze. Aquí encontrarás artículos sobre cómo crear una tarjeta de contenido, cómo personalizar tus tarjetas de contenido, pruebas, informes y mucho más."
channel:
  - content cards
search_rank: 5
guide_featured_title: "Artículos de sección"
guide_featured_list:
- name: Crear una tarjeta de contenido
  link: /docs/user_guide/message_building_by_channel/content_cards/create/
  image: /assets/img/braze_icons/columns-01.svg
- name: Creación de tarjetas
  link: /docs/user_guide/message_building_by_channel/content_cards/create/card_creation
  image: /assets/img/braze_icons/message-check-circle.svg
- name: Detalles creativos
  link: /docs/user_guide/message_building_by_channel/content_cards/creative_details/
  image: /assets/img/braze_icons/brush-02.svg
- name: Prueba
  link: /docs/user_guide/message_building_by_channel/content_cards/testing/
  image: /assets/img/braze_icons/beaker-02.svg
- name: Informar
  link: /docs/user_guide/message_building_by_channel/content_cards/reporting/
  image: /assets/img/braze_icons/pie-chart-01.svg
- name: Buenas prácticas
  link: /docs/user_guide/message_building_by_channel/content_cards/best_practices
  image: /assets/img/braze_icons/check-square-broken.svg
---

## [![Curso de Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/content-cards){: style="float:right;width:120px;border:0;" class="noimgborder"} Ventajas de utilizar tarjetas de contenido

Éstas son sólo algunas de las ventajas de utilizar tarjetas de contenido frente a pedir a tus desarrolladores que incorporen contenido a tu aplicación:

- **Segmentación y personalización más sencillas:** Tus datos de usuario viven en Braze, lo que facilita la definición de tu audiencia y la personalización de tus mensajes con las tarjetas de contenido.
- **Informes centralizados:** Los análisis de tarjeta de contenido se siguen en Braze, para que tengas información de todas tus campañas en una sola ubicación.
- **Recorridos del cliente cohesionados:** Puedes combinar las tarjetas de contenido con otros canales en Braze para crear experiencias de cliente coherentes. Un caso de uso popular es enviar una notificación push, y luego guardar esa notificación como una tarjeta de contenido en tu aplicación para cualquiera que no haya interactuado con el push. Si el contenido está integrado directamente en tu aplicación por tus desarrolladores, entonces está aislado del resto de tu mensajería.
- **No se requiere adhesión voluntaria:** Al igual que los mensajes dentro de la aplicación, las tarjetas de contenido no requieren adhesión voluntaria ni permisos de tus usuarios. Pero mientras que los mensajes dentro de la aplicación no tienen permiso y duran poco, las tarjetas de contenido no tienen permiso y son permanentes. Esto significa que las estrategias de mensajería que combinan mensajes dentro de la aplicación y tarjetas de contenido logran un gran equilibrio.
- **Más control sobre la experiencia de mensajería:** Aunque seguirás necesitando la ayuda de tus desarrolladores para la configuración inicial de las Tarjetas de contenido, después podrás controlar el mensaje, los destinatarios, los plazos y mucho más directamente desde tu panel de Braze.

### Tarjetas de contenido en cifras

Como tú, el especialista en marketing, creas tú mismo las tarjetas de contenido en Braze, puedes actualizar la mensajería y recibir un retorno de la inversión sin tener que revisar completamente tu aplicación o sitio web. Aquí tienes algunas estadísticas útiles sobre el ROI de las tarjetas de contenido:

- Las tarjetas de contenido son **38 veces** más eficaces que los correos electrónicos para aumentar las ventas en un plazo de 72 horas[^1].
- Utilizar tarjetas de contenido en campañas de fidelización **multiplica por 5 las** conversiones[^1].
- El envío de información a los usuarios a través de notificaciones push, mensajes dentro de la aplicación y tarjetas de contenido **multiplica por 6,9** el número de sesiones, en comparación con la interacción de los usuarios sólo a través de push[^2].
- El envío de información a los usuarios por correo electrónico, mensajes dentro de la aplicación y tarjetas de contenido multiplica **por 3,6** la vida media de los usuarios, en comparación con los usuarios que sólo utilizan el correo electrónico[^2].

## Cómo funciona

Braze proporciona diferentes tipos de tarjeta de contenido para mostrar la tarjeta de contenido: Clásica, Imagen con subtítulos o Imagen. En el fondo, las tarjetas de contenido son en realidad una carga útil de datos, no el aspecto que tienen los datos. 

Ahora pongámonos un poco técnicos. Entre bastidores, hay tres partes principales de una tarjeta de contenido:

- **Modelo:** ¿Qué tipo de datos viven en la tarjeta?
- **Ver:** Cómo es la tarjeta
- **Controlador:** Cómo interactúa el usuario con la tarjeta

Para una implementación predeterminada, añades el contenido de la tarjeta -el modelo- desde el panel o a través de API, y la vista y el controlador se gestionan mediante lo que se denomina un controlador de vista. Un controlador de vistas es el "pegamento" entre la aplicación global y la pantalla.

## Casos de uso

Consulta esta sección para conocer algunos casos de uso habituales de las tarjetas de contenido.

{% alert tip %}
Para inspirarte más, te recomendamos que consultes nuestra [Guía de inspiración de tarjetas de contenido](https://www.braze.com/resources/reports-and-guides/content-cards-inspiration-guide), que incluye más de 20 campañas personalizables, como programas de referidos, lanzamientos de nuevos productos y renovaciones de suscripciones.
{% endalert %}

{% tabs %}
{% tab Onboarding and next steps %}

A medida que los nuevos usuarios exploran tu aplicación y sitio web, guíales a través de los valores y beneficios de lo que ofreces con tarjetas de contenido colocadas estratégicamente. Anima a los usuarios a optar por otros canales de comunicación con una tarjeta de contenido en tu página de inicio, y guarda las tareas de incorporación pendientes en una pestaña dedicada a la incorporación impulsada por las tarjetas de contenido. ¡No olvides eliminar una tarjeta después de que un usuario complete la tarea deseada!

<style>
  .imgDiv {
      text-align: center;
    }
</style>

<div class="imgDiv">
<img src="{% image_buster /assets/img_archive/cc_usecase_onboarding.png %}" style="border:0px">
</div>

{% endtab %}
{% tab Event attendance %}

Muestra tarjetas de contenido en la parte superior de la página de inicio de un usuario para fomentar la asistencia a eventos, utilizando la orientación por ubicación para llegar a los usuarios potenciales allí donde se encuentren. Invitar a los usuarios a eventos físicos relevantes les hace sentirse especiales, especialmente con mensajes personalizados que aprovechan su actividad previa con tu marca.

<div class="imgDiv">
<img src="{% image_buster /assets/img_archive/cc_usecase_event.png %}" style="border:0px">
</div>

{% endtab %}
{% tab Recommendations %}

Utiliza los datos que tienes sobre los comportamientos y preferencias de los usuarios para mostrarles contenido relevante en tiempo real desde las Tarjetas de Contenido de la página de inicio o del buzón de entrada y atraerlos de nuevo a tu oferta de productos.

<div class="imgDiv">
<img src="{% image_buster /assets/img_archive/cc_usecase_recommendation.png %}" style="border:0px">
</div>

{% endtab %}
{% tab Sales and promotions %}

Aprovecha las tarjetas de contenido para destacar mensajes promocionales y ofertas no reclamadas directamente en tu página de inicio o en un buzón de entrada promocional específico. Aporta contenido relevante basado en las compras anteriores de cada cliente para entregar promociones personalizadas que llamen la atención.

<div class="imgDiv">
<img src="{% image_buster /assets/img_archive/cc_usecase_promo.png %}" style="border:0px">
</div>

{% endtab %}
{% endtabs %}

### Otros casos de uso

Aparte de estos casos de uso principales, nuestros clientes utilizan las tarjetas de contenido de muchas formas distintas. El poder de las tarjetas de contenido es su flexibilidad. Si el caso de uso que quieres no se muestra aquí, puedes configurar [los pares clave-valor]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/key_value_pairs/) y enviar las cargas útiles a tu aplicación o sitio web.

## Tarjetas de contenido en tu aplicación

Esta sección cubre las formas más comunes de colocar tarjetas de contenido dentro de tu aplicación o sitio web:

- [Buzón de entrada de mensajes](#message-inbox)
- [Carrusel](#carousel)

La lógica y la implementación de estas colocaciones no están predeterminadas en Braze, por lo que tu equipo de ingeniería debe suministrar y apoyar el trabajo para conseguir estos casos de uso. Para obtener un resumen sobre cómo implementar estas colocaciones, consulta [Crear una tarjeta de contenido personalizada]({{site.baseurl}}/developer_guide/content_cards/creating_cards/).

\![3 tarjetas de contenido de ejemplo, que muestran las distintas opciones de colocación: buzón de entrada de mensajes, carrusel y banner.]({% image_buster /assets/img_archive/cc_placements.png %}){: style="border:0px;"}

### Buzón de entrada de mensajes

\![Un ejemplo de tarjeta de contenido que utiliza la colocación "buzón de entrada de mensajes".]({% image_buster /assets/img_archive/cc_placement_inbox.png %}){: style="float:right;margin-left:15px;max-width:30%;border:0px;"}

Un buzón de entrada de mensajes (también llamado centro de notificaciones o fuente) es un lugar persistente en tu aplicación o sitio web donde puedes mostrar tarjetas de contenido en el formato que prefieras. Cada mensaje en el buzón de entrada es su propia tarjeta de contenido. 

El buzón de entrada de mensajes es una implementación predeterminada que requiere un desarrollo mínimo. Braze proporciona un [controlador de vista](#how-it-works) para un buzón de entrada de mensajes en iOS, Android y Web para facilitar el proceso de creación.

#### Beneficios

- Los usuarios pueden recibir muchas tarjetas en un solo lugar
- Una forma eficaz de hacer resurgir la información perdida o descartada en otros canales (especialmente las notificaciones push).
- No se requiere adhesión voluntaria

#### Comportamiento

Cuando un usuario sea elegible para una tarjeta, ésta aparecerá automáticamente en su buzón de entrada. Las tarjetas de contenido están diseñadas para ser vistas en bloque, de modo que los usuarios puedan ver todas las tarjetas para las que son elegibles a la vez.

Con la implementación predeterminada, las tarjetas de contenido en el buzón de entrada pueden aparecer como tarjetas clásicas (que contienen un título, texto y una imagen opcional), de sólo imagen o de imagen subtitulada. Tú eliges dónde se ubicará el buzón de entrada de mensajes dentro de tu aplicación.

Las tarjetas de contenido vienen con un estilo predeterminado, pero puedes elegir una implementación personalizada para mostrar las tarjetas y la fuente según el aspecto de tu aplicación.

### Carrusel

\![Un ejemplo de tarjeta de contenido que utiliza la colocación "carrusel".]({% image_buster /assets/img_archive/cc_politer_carousel.png %}){: style="float:right;margin-left:15px;max-width:30%;border:0px;"}

Los carruseles muestran varios contenidos en un único espacio que tus clientes pueden deslizar para verlos. Pueden ser una presentación de imágenes, texto, video o una combinación de ellos. Se trata de una implementación personalizada y requiere un poco de trabajo por parte de tus desarrolladores.

#### Beneficios

- Los usuarios pueden recibir muchas tarjetas en un solo lugar
- Una forma atractiva de presentar recomendaciones

#### Comportamiento

Cuando un usuario sea elegible para una tarjeta, ésta aparecerá en un carrusel en cualquier página de tu aplicación a la que se añada el carrusel. Los usuarios pueden deslizar el dedo horizontalmente para ver otras tarjetas destacadas.

Como se trata de una implementación personalizada, tendrás que trabajar con tus desarrolladores para crear tus propias vistas para mostrar las tarjetas de contenido. Las tarjetas predeterminadas clásica, sólo imagen y con subtítulos no son compatibles con esta implementación.

## Integración de tarjetas de contenido

Tus desarrolladores integrarán las tarjetas de contenido cuando integren el SDK de Braze. Para más detalles sobre cómo integrarte con las tarjetas de contenido, consulta los artículos de la guía del desarrollador de tu plataforma:

- [iOS]({{site.baseurl}}/developer_guide/content_cards/?sdktab=swift)
- [Android]({{site.baseurl}}/developer_guide/content_cards/?sdktab=android)
- [Web]({{site.baseurl}}/developer_guide/content_cards/?sdktab=web)

## Fuentes

<span></span>

[^1]: [8 consejos para sacar el máximo partido a tus campañas de retención de clientes](https://www.braze.com/resources/articles/8-tips-for-making-the-most-of-your-customer-retention-campaigns)
[^2]: [Informe: La diferencia del marketing de canales cruzados](https://www.braze.com/resources/reports-and-guides/the-cross-channel-marketing-difference-report)
