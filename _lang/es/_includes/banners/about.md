# Banners

> Con Banners, puedes crear mensajes personalizados para tus usuarios, al tiempo que amplías el alcance de tus otros canales, como el correo electrónico o las notificaciones push. Puedes integrar banners directamente en tu aplicación o sitio web, lo que te permite interactuar con los usuarios a través de una experiencia que resulta natural.

![Ejemplo de banner mostrado en un dispositivo.]({% image_buster /assets/img/banners/sample_banner.png %})

## Requisitos previos

La disponibilidad de los banners depende de tu paquete Braze. Ponte en contacto con tu director de cuentas o administrador del éxito del cliente para empezar.

## ¿Por qué utilizar banners?

Los banners permiten a los equipos de marketing y de producto realizar la personalización dinámica del contenido de las aplicaciones o los sitios web, reflejando la elegibilidad y el comportamiento de los usuarios en tiempo real. Muestran mensajes de forma persistente en línea, proporcionando experiencias no intrusivas y contextuales que se actualizan automáticamente al inicio de cada sesión de usuario.

Una vez completada la integración de los banners en una aplicación o sitio web, los especialistas en marketing pueden diseñarlos y lanzarlos utilizando un sencillo editor de arrastrar y soltar, lo que elimina la necesidad de asistencia continua por parte de los desarrolladores, reduce la complejidad y mejora la eficiencia.

| Casos de uso | Explicación |
| --- | --- |
| Anuncios | Mantén los anuncios, como los próximos eventos o los cambios en las políticas, en un lugar destacado de la experiencia de la aplicación. |
| Personalizar ofertas | Muestra promociones e incentivos personalizados basados en el historial de navegación, el contenido del carrito, el nivel de suscripción y el estado de fidelización de cada usuario. |
| Dirigirse a la interacción de nuevos usuarios | Guía a los nuevos usuarios a través de los flujos de incorporación y la configuración de la cuenta. |
| Ventas y promociones | Destaca el contenido destacado, los productos de tendencia y las campañas de marca en curso de forma persistente y directa en tu página de inicio sin interrumpir la experiencia del usuario. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Características

Las características de los banners incluyen:

- **Creación sencilla de contenido:** Crea y realiza la vista previa de tu banner utilizando un editor de arrastrar y soltar compatible con imágenes, texto, botones, formularios de captura de correo electrónico, código personalizado y mucho más.
- **Colocaciones flexibles:** Define múltiples ubicaciones dentro de tu aplicación o sitio web donde puedan aparecer los banners, lo que habilita una orientación precisa a contextos específicos o experiencias de usuario.
- **Personalización dinámica:** Los banners se actualizan de manera dinámica con cada nueva sesión de usuario, lo que garantiza que el contenido se mantenga actualizado y personalizado gracias a las herramientas de personalización integradas de Braze y la lógica Liquid.
- **Priorización nativa:** Establece la prioridad de visualización cuando varios banners se dirigen al mismo espacio publicitario, asegurándote de que el mensaje adecuado llegue a los usuarios en el momento adecuado.
- **Bloque de editor de código personalizado:** Utiliza el bloque de editor de código personalizado para añadir código HTML personalizado y así realizar personalizaciones avanzadas o integrarlo fácilmente con tus estilos web actuales.

## Acerca de los banners {#about-banners}

### Identificadores de ubicación {#placement-id}

Las ubicaciones de los banners son ubicaciones específicas de tu aplicación o sitio web [que creas con el SDK de Braze]({{site.baseurl}}/developer_guide/banners/placements/) y que designan dónde pueden aparecer los banners.

Las ubicaciones más habituales son la parte superior de la página de inicio, las páginas de detalles de los productos y los procesos de pago. Una vez creadas las ubicaciones, se pueden [asignar]({{site.baseurl}}/user_guide/message_building_by_channel/banners/create/) banners [en tu campaña de banners]({{site.baseurl}}/user_guide/message_building_by_channel/banners/create/).

No hay un límite fijo en el número de ubicaciones que puedes crear por espacio de trabajo, y puedes crear tantos ID de ubicación como requiera tu experiencia. Cada ubicación debe ser única dentro de un espacio de trabajo. Un único ID de ubicación puede ser referenciado por hasta 25 mensajes activos al mismo tiempo.

{% alert important %}
Evita modificar los ID de ubicación después de lanzar una campaña de banners.
{% endalert %}

### Prioridad del banner {#priority}

Cuando varios mensajes de banner hacen referencia al mismo ID de ubicación, los banners se muestran por orden de prioridad: alta, media o baja. De forma predeterminada, los banners están configurados en medio, pero puedes [establecer manualmente la prioridad]({{site.baseurl}}/user_guide/message_building_by_channel/banners/create/#set-priority) cuando crees o edites tu campaña de banners. 

Si varios banners tienen la misma prioridad, se mostrará primero el banner más reciente para el que el usuario sea elegible.

### Solicitudes de colocación {#requests}

{% multi_lang_include banners/placement_requests.md %}

### Entrega de mensajes

Los mensajes de banner se entregan a tu aplicación o sitio web como contenido HTML, normalmente representado dentro de un iframe. Esto garantiza que tus banners se muestren de forma coherente en todos los dispositivos y te ayuda a mantener sus estilos y scripts separados del resto del código.

Los iframes permiten actualizaciones de contenido dinámicas y de personalización que no requieren cambios en tu código base. Cada iframe recupera y muestra el código HTML de cada sesión de usuario utilizando la lógica de personalización y segmentación de la campaña.

{% multi_lang_include alerts/important_alerts.md alert='network dependency' %}

### Dimensiones y tamaños

Esto es lo que debes saber sobre las dimensiones y el tamaño de los banners:

- Aunque el compositor te permite realizar una vista previa de los banners en diferentes dimensiones, esa información no se guarda ni se envía al SDK.
- El HTML ocupa todo el ancho del contenedor en el que se representa.
- Recomendamos crear un elemento de dimensiones fijas y probar esas dimensiones en Composer.

## Limitaciones

Cada espacio de trabajo puede admitir hasta 200 campañas activas de Banner. Si se alcanza este límite, tendrás que [archivar o desactivar]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/about_statuses/#changing-the-status) una campaña existente antes de crear una nueva.

Además, los mensajes de banner no admiten las siguientes características:

- Campañas activadas por API y basadas en acciones
- Contenido conectado
- Códigos promocionales
- Despidos controlados por el usuario
- `catalog_items` usando la[`:rerender`]({{site.baseurl}}/user_guide/data/activation/catalogs/using_catalogs/#using-liquid)[etiqueta]({{site.baseurl}}/user_guide/data/activation/catalogs/using_catalogs/#using-liquid)

{% alert tip %}
¿Quieres ayudar a priorizar lo que viene después? Contacta [con banners-feedback@braze.com](mailto:banners-feedback@braze.com).
{% endalert %}

## Próximos pasos

Ahora que ya sabes qué son los banners, estás listo para los siguientes pasos:

1. [Creación de ubicaciones para banners en tu aplicación o sitio web]({{site.baseurl}}/developer_guide/banners/placements/)
2. [Creación de campañas de banners en Braze]({{site.baseurl}}/user_guide/message_building_by_channel/banners/create/)
3. [Tutorial: Mostrar un banner por ID de ubicación]({{site.baseurl}}/developer_guide/banners/tutorial_displaying_banners)
