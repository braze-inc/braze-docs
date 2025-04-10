---
nav_title: Acerca de las tarjetas de contenido
article_title: Acerca de las tarjetas de contenido
page_order: 0
description: "Este artículo de referencia ofrece una visión general del canal Braze Content Card y de los casos de uso más comunes."
channel:
  - content cards
search_rank: 4
---

# [![Curso de Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/content-cards){: style="float:right;width:120px;border:0;" class="noimgborder"} Acerca de las tarjetas de contenido

> Las tarjetas de contenido se incrustan directamente en tu aplicación o sitio web para que puedas atraer a los usuarios con una experiencia natural y fluida. Te dan más control sobre la experiencia de tu aplicación o sitio web, y te permiten crear buzones de mensajería, carruseles y banners, y ampliar el alcance de otros canales (como el correo electrónico o las notificaciones push).

Las tarjetas de contenido son una característica adicional y deben adquirirse. Para empezar a utilizar las tarjetas de contenido, póngase en contacto con su gestor de éxito de clientes de Braze o con nuestro equipo de asistencia.

{% alert note %}
Si utilizas nuestra herramienta de noticias, te recomendamos que te pases a nuestro canal de mensajería de tarjetas de contenido: es más flexible, personalizable y fiable. La fuente de noticias también está obsoleta. Consulte nuestra [Guía de migración]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/) o póngase en contacto con su gestor de cuenta Braze para obtener más información.
{% endalert %}

## Ventajas de utilizar tarjetas de contenido

Éstas son sólo algunas de las ventajas de utilizar tarjetas de contenido frente a pedir a tus desarrolladores que incorporen contenido a tu aplicación:

- **Segmentación y personalización más sencillas:** Los datos de sus usuarios viven en Braze, lo que facilita la definición de su audiencia y la personalización de sus mensajes con las tarjetas de contenido.
- **Informes centralizados:** Los análisis de tarjeta de contenido se siguen en Braze, para que tengas información de todas tus campañas en una sola ubicación.
- **Recorridos del cliente cohesivos:** Puede combinar las tarjetas de contenido con otros canales en Braze para crear experiencias de cliente coherentes. Un caso de uso popular es el envío de una notificación push, y luego guardar esa notificación como una tarjeta de contenido en su aplicación para cualquier persona que no se involucró con el empuje. Si el contenido está integrado directamente en tu aplicación por tus desarrolladores, entonces está aislado del resto de tu mensajería.
- **No se requiere adhesión voluntaria:** Al igual que los mensajes dentro de la aplicación, las tarjetas de contenido no requieren adhesión voluntaria ni permisos de tus usuarios. Pero mientras que los mensajes dentro de la aplicación no tienen permiso y duran poco, las tarjetas de contenido no tienen permiso y son permanentes. Esto significa que las estrategias de mensajería que combinan mensajes dentro de la aplicación y tarjetas de contenido logran un gran equilibrio.
- **Más control sobre la experiencia de mensajería:** Aunque seguirás necesitando la ayuda de tus desarrolladores para la configuración inicial de las Tarjetas de contenido, después podrás controlar el mensaje, los destinatarios, los plazos y mucho más directamente desde tu panel de Braze.

### Tarjetas de contenido en cifras

Como tú, el especialista en marketing, creas tú mismo las tarjetas de contenido en Braze, puedes actualizar la mensajería y recibir un retorno de la inversión sin tener que revisar completamente tu aplicación o sitio web. Aquí tienes algunas estadísticas útiles sobre el ROI de las tarjetas de contenido:

- Las tarjetas de contenido son **38 veces** más eficaces que los correos electrónicos para aumentar las ventas en un plazo de 72 horas.[^1]]
- Utilizar tarjetas de contenido en campañas de fidelización **multiplica por 5** las conversiones.[^1]
- El envío de información a los usuarios a través de notificaciones push, mensajes dentro de la aplicación y tarjetas de contenido **multiplica por 6,9** el número de sesiones, en comparación con la interacción de los usuarios sólo a través de push[^2].]
- El envío de información a los usuarios por correo electrónico, mensajes dentro de la aplicación y tarjetas de contenido multiplica **por 3,6** la vida media de los usuarios, en comparación con los usuarios que sólo utilizan el correo electrónico[^2].]

## Cómo funciona

En el fondo, las tarjetas de contenido son en realidad una carga útil de datos, no el aspecto que tienen los datos. Braze proporciona vistas de plantilla (banner, modal, imagen con leyenda) para mostrar los datos de la tarjeta de contenido, que es en definitiva el aspecto que tiene su mensaje.

Ahora pongámonos un poco técnicos. Entre bastidores, hay tres partes principales de una tarjeta de contenido:

- **Modelo:** ¿Qué tipo de datos contiene la tarjeta?
- **Visualización:** Aspecto de la tarjeta
- **Controlador:** Cómo interactúa el usuario con la tarjeta

Para una implementación predeterminada, añades el contenido de la tarjeta -el modelo- desde el panel o a través de API, y la vista y el controlador se gestionan mediante lo que se denomina un controlador de vista. Un controlador de vista es el "pegamento" entre la aplicación global y la pantalla.

## Ejemplos

Consulta esta sección para conocer algunos casos de uso habituales de las tarjetas de contenido.

{% alert tip %}
Para inspirarte más, te recomendamos que consultes nuestra [Guía de inspiración de tarjetas de contenido](https://www.braze.com/resources/reports-and-guides/content-cards-inspiration-guide), que incluye más de 20 campañas personalizables, como programas de referidos, lanzamientos de nuevos productos y renovaciones de suscripciones.
{% endalert %}

{% tabs %}
{% tab Incorporación y próximos pasos %}

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
{% tab Asistencia a eventos %}

Muestra tarjetas de contenido en la parte superior de la página de inicio de un usuario para fomentar la asistencia a eventos, utilizando la orientación por ubicación para llegar a los usuarios potenciales allí donde se encuentren. Invitar a los usuarios a eventos físicos relevantes les hace sentirse especiales, especialmente con mensajes personalizados que aprovechan su actividad previa con tu marca.

<div class="imgDiv">
<img src="{% image_buster /assets/img_archive/cc_usecase_event.png %}" style="border:0px">
</div>

{% endtab %}
{% tab Recomendaciones %}

Utilice los datos de que dispone sobre los comportamientos y preferencias de los usuarios para mostrarles contenido relevante en tiempo real desde la página de inicio o las tarjetas de contenido de la bandeja de entrada y atraerlos hacia su oferta de productos.

<div class="imgDiv">
<img src="{% image_buster /assets/img_archive/cc_usecase_recommendation.png %}" style="border:0px">
</div>

{% endtab %}
{% tab Ventas y promociones %}

Aproveche las tarjetas de contenido para destacar mensajes promocionales y ofertas no reclamadas directamente en su página de inicio o en una bandeja de entrada promocional específica. Aporte contenido relevante basado en las compras anteriores de cada cliente para ofrecer promociones personalizadas que llamen la atención.

<div class="imgDiv">
<img src="{% image_buster /assets/img_archive/cc_usecase_promo.png %}" style="border:0px">
</div>

{% endtab %}
{% endtabs %}

### Otros casos de uso

Aparte de estos casos de uso principales, nuestros clientes utilizan las tarjetas de contenido de muchas formas distintas. El poder de las tarjetas de contenido reside en su flexibilidad. Si el caso de uso que quieres no se muestra aquí, puedes configurar [los pares clave-valor]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/key_value_pairs/) y enviar las cargas útiles a tu aplicación o sitio web.

## Colocación de tarjetas de contenido

Esta sección cubre las tres formas más comunes de colocar tarjetas de contenido dentro de tu aplicación o sitio web:

- [Buzón de entrada de mensajes](#message-inbox)
- [Carrusel](#carousel)
- [Banner](#banner)

La lógica y la implementación de estas colocaciones no están predeterminadas en Braze, por lo que tu equipo de ingeniería debe suministrar y apoyar el trabajo para conseguir estos casos de uso. Para obtener un resumen sobre cómo implementar estas colocaciones, consulta [Crear una tarjeta de contenido personalizada]({{site.baseurl}}/developer_guide/content_cards/creating_custom_content_cards/).

![3 tarjetas de contenido de ejemplo, que muestran las diferentes opciones de colocación: bandeja de entrada de mensajes, carrusel y banner.]({% image_buster /assets/img_archive/cc_placements.png %}){: style="border:0px;"}

### Buzón de entrada de mensajes

![Un ejemplo de tarjeta de contenido que utiliza la colocación "buzón de entrada de mensajes".]({% image_buster /assets/img_archive/cc_placement_inbox.png %}){: style="float:right;margin-left:15px;max-width:30%;border:0px;"}

Una bandeja de entrada de mensajes (también llamada centro de notificaciones o feed) es un lugar persistente en tu aplicación o sitio web donde puedes mostrar Tarjetas de contenido en el formato que prefieras. Cada mensaje de la bandeja de entrada es su propia tarjeta de contenido. 

El buzón de entrada de mensajes es una implementación predeterminada que requiere un desarrollo mínimo. Braze proporciona un [controlador de vista](#how-it-works) para un buzón de entrada de mensajes en iOS, Android y Web para facilitar el proceso de creación.

#### Beneficios

- Los usuarios pueden recibir muchas tarjetas en un solo lugar
- Una forma eficaz de hacer resurgir la información perdida o descartada en otros canales (especialmente las notificaciones push).
- No se requiere adhesión voluntaria

#### Comportamiento

Cuando un usuario pueda optar a una tarjeta, ésta aparecerá automáticamente en su bandeja de entrada. Las tarjetas de contenido están diseñadas para ser vistas en bloque, de modo que los usuarios puedan ver todas las tarjetas para las que son elegibles a la vez.

Con la implementación predeterminada, las tarjetas de contenido de la bandeja de entrada pueden aparecer como tarjetas clásicas (que contienen un título, texto y una imagen opcional), de sólo imagen o de imagen con leyenda. Tú eliges dónde se ubicará la bandeja de entrada de mensajes en tu aplicación.

Las tarjetas de contenido vienen con un estilo predeterminado, pero puedes elegir una implementación personalizada para mostrar las tarjetas y el feed de acuerdo con el aspecto de tu aplicación.

### Carrusel

![Un ejemplo de tarjeta de contenido utilizando la colocación "carrusel".]({% image_buster /assets/img_archive/cc_politer_carousel.png %}){: style="float:right;margin-left:15px;max-width:30%;border:0px;"}

Los carruseles muestran varias piezas de contenido en un único espacio que sus clientes pueden deslizar para verlas. Pueden ser una presentación de imágenes, texto, video o una combinación de ellos. Esta es una implementación personalizada y requiere un poco de trabajo por parte de sus desarrolladores.

#### Beneficios

- Los usuarios pueden recibir muchas tarjetas en un solo lugar
- Una forma atractiva de presentar recomendaciones

#### Comportamiento

Cuando un usuario sea elegible para una tarjeta, ésta aparecerá en un carrusel en cualquier página de su aplicación a la que se añada el carrusel. Los usuarios pueden deslizar el dedo horizontalmente para ver otras tarjetas destacadas.

Dado que se trata de una implementación personalizada, tendrá que trabajar con sus desarrolladores para crear sus propias vistas para mostrar las tarjetas de contenido. Las tarjetas predeterminadas clásica, sólo imagen y con subtítulos no son compatibles con esta implementación.

### Banner

![Un ejemplo de tarjeta de contenido que utiliza la colocación "banner".]({% image_buster /assets/img_archive/cc_placement_banner.png %}){: style="float:right;margin-left:15px;max-width:30%;border:0px;"}

Las tarjetas de contenido pueden aparecer como un banner dinámico que se muestra de forma persistente en su página de inicio o en la parte superior de otras páginas designadas.

#### Beneficios

- Persiste en la página a diferencia de un mensaje in-app, por lo que tiene más tiempo para llegar a su público
- Una buena forma de mostrar nuevos contenidos en un lugar destacado de su página de inicio.

#### Comportamiento

Los usuarios pueden ver y participar en los contenidos más relevantes para ellos. Dado que se trata de una implementación personalizada, tendrá que trabajar con sus desarrolladores para personalizar las vistas para mostrar las Tarjetas de contenido.

## Integración de tarjetas de contenido

Tus desarrolladores integrarán las tarjetas de contenido cuando integren el SDK de Braze. Para obtener más información sobre cómo integrarse con las tarjetas de contenido, consulte los artículos de la guía para desarrolladores de su plataforma:

- [ iOSiOS]({{site.baseurl}}/developer_guide/platforms/swift/content_cards/ "Guía de integración de la tarjeta de contenido")
- [ AndroidAndroid]({{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/integration/ "Guía de integración de la tarjeta de contenido")
- [ WebWeb]({{site.baseurl}}/developer_guide/platform_integration_guides/web/content_cards/integration/ "Guía de integración de la tarjeta de contenido")

## Fuentes

<span></span>

[^1]: [8 consejos para sacar el máximo partido a sus campañas de fidelización de clientes](https://www.braze.com/resources/articles/8-tips-for-making-the-most-of-your-customer-retention-campaigns)
[^2]: [Informe: La diferencia del marketing multicanal](https://www.braze.com/resources/reports-and-guides/the-cross-channel-marketing-difference-report)