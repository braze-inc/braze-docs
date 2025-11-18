# Banners

> Con Banners, puedes crear mensajes personalizados para tus usuarios, a la vez que amplías el alcance de tus otros canales, como el correo electrónico o las notificaciones push. Puedes incrustar banners directamente en tu aplicación o sitio web, lo que te permite interactuar con los usuarios a través de una experiencia natural.

![Un ejemplo de Banner renderizado en un dispositivo.]({% image_buster /assets/img/banners/sample_banner.png %})

## Requisitos previos

La disponibilidad de los banners depende de tu paquete Braze. Ponte en contacto con tu director de cuentas o administrador del éxito del cliente para empezar.

## ¿Por qué utilizar Banners?

Los banners permiten a los equipos de marketing y de producto personalizar el contenido de la aplicación o del sitio web de forma dinámica, reflejando en tiempo real la elegibilidad y el comportamiento del usuario. Muestran mensajes en línea de forma persistente, proporcionando experiencias no intrusivas y contextualmente relevantes que se actualizan automáticamente al inicio de cada sesión de usuario.

Una vez integrados los banners en una aplicación o sitio web, los especialistas en marketing pueden diseñarlos y lanzarlos con un sencillo editor de arrastrar y soltar, lo que elimina la necesidad de asistencia continua de los desarrolladores, reduce la complejidad y mejora la eficacia.

| Casos de uso | Explicación |
| --- | --- |
| Anuncios | Mantén anuncios como próximos eventos o cambios en la política a la vanguardia de la experiencia de la aplicación. |
| Personalización de ofertas | Muestra promociones e incentivos personalizados en función del historial de navegación de cada usuario, el contenido de su carrito, su nivel de suscripción y su estado de fidelización. |
| Centrarse en la interacción con nuevos usuarios | Guía a los nuevos usuarios a través de los flujos de incorporación y la configuración de la cuenta. |
| Ventas y promociones | Destaca el contenido destacado, los productos de moda y las campañas de marca en curso de forma persistente y directa en tu página de inicio, sin interrumpir la experiencia del usuario. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Características

Entre las características de las Banderas se incluyen:

- **Fácil creación de contenidos:** Crea y previsualiza tu Banner utilizando un editor visual de arrastrar y soltar con soporte para imágenes, texto, botones, formularios de captura de correo electrónico, código personalizado y mucho más.
- **Colocaciones flexibles:** Define múltiples ubicaciones dentro de tu aplicación o sitio web en las que puedan aparecer las Banners, habilitando una orientación precisa a contextos específicos o experiencias de usuario.
- **Personalización dinámica:** Los banners se actualizan dinámicamente con cada nueva sesión de usuario, garantizando que el contenido se mantenga actualizado y personalizado mediante las herramientas de personalización integradas de Braze y la lógica de Liquid.
- **Priorización nativa:** Establece la prioridad de visualización cuando varias Banners se dirijan a la misma ubicación, garantizando que el mensaje correcto llegue a los usuarios en el momento adecuado.
- **Soporte HTML personalizado:** Incorpora bloques HTML personalizados para una personalización avanzada o una integración perfecta con tus estilos web existentes.

## Acerca de las pancartas {#about-banners}

### ID de colocación {#placement-id}

Las ubicaciones de banners son ubicaciones específicas en tu aplicación o sitio web [que creas con el SDK de Braze]({{site.baseurl}}/developer_guide/banners/placements/) y que designan dónde pueden aparecer los banners.

Las ubicaciones más comunes son la parte superior de tu página de inicio, las páginas de detalles del producto y los flujos de pago. Una vez creadas las ubicaciones, los banners se pueden [asignar en tu campaña de banners]({{site.baseurl}}/user_guide/message_building_by_channel/banners/creating_campaigns/).

No hay un límite fijo en el número de colocaciones que puedes crear por espacio de trabajo, y puedes crear tantos ID de colocación como requiera tu experiencia. Cada colocación debe ser única dentro de un espacio de trabajo. Un único ID de colocación puede ser referenciado por hasta 10 campañas activas al mismo tiempo.

{% alert important %}
Evita modificar los ID de ubicación después de lanzar una campaña de Banner.
{% endalert %}

### Prioridad del banner {#priority}

Cuando varias campañas hacen referencia al mismo ID de ubicación, los banners se muestran por orden de prioridad: alta, media o baja. Por defecto, los Banners recién creados están predeterminados como medios, pero puedes [establecer manualmente la prioridad]({{site.baseurl}}/user_guide/message_building_by_channel/banners/creating_campaigns/#set-priority) cuando crees o edites tu campaña de Banners. 

Si hay varios banners configurados con la misma prioridad, se mostrará primero el más reciente para el que el usuario sea elegible.

### Solicitudes de colocación {#requests}

{% multi_lang_include banners/placement_requests.md %}

### Entrega de mensajes

Los mensajes de banner se entregan a tu aplicación o sitio web como contenido HTML, normalmente dentro de un iframe. Esto garantiza que tus banners se muestren de forma coherente en todos los dispositivos, y te ayuda a mantener sus estilos y secuencias de comandos separados del resto del código.

Los iframes permiten actualizaciones de contenido dinámicas y personalizadas que no requieren cambios en tu código base. Cada iframe recupera y muestra el HTML de cada sesión de usuario utilizando la lógica de segmentación y personalización de campañas.

### Dimensiones y tamaño

Esto es lo que debes saber sobre las dimensiones y el tamaño de los estandartes:

- Aunque el compositor te permite previsualizar Banners en diferentes dimensiones, esa información no se guarda ni se envía al SDK.
- El HTML ocupará todo el ancho del contenedor en el que se muestre.
- Te recomendamos que hagas un elemento de dimensión fija y pruebes esas dimensiones en Compositor.

## Limitaciones

Cada espacio de trabajo puede soportar hasta 200 campañas de Banner activas. Si se alcanza este límite, tendrás que [archivar o desactivar]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/about_statuses/#changing-the-status) una campaña existente antes de crear una nueva.

Además, los mensajes de Banner no admiten las siguientes características:

- Integración en Canvas
- Campañas activadas por API y basadas en acciones
- Contenido conectado
- Códigos promocionales
- Despidos controlados por el usuario
- `catalog_items` utilizando la [etiqueta`:rerender` ]({{site.baseurl}}/user_guide/data/activation/catalogs/using_catalogs/#using-liquid)

{% alert tip %}
¿Quieres ayudar a priorizar lo siguiente? Ponte en contacto con [banners-feedback@braze.com](mailto:banners-feedback@braze.com).
{% endalert %}

## Próximos pasos

Ahora que ya conoces los Banners, estás preparado para los siguientes pasos:

1. [Creación de banners en tu aplicación o sitio web]({{site.baseurl}}/developer_guide/banners/placements/)
2. [Crear campañas de banners en Braze]({{site.baseurl}}/user_guide/message_building_by_channel/banners/creating_campaigns/)
3. [Tutorial: Mostrar un Banner por ID de Colocación]({{site.baseurl}}/developer_guide/banners/tutorial_displaying_banners)
