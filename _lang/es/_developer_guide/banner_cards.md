---
page_order: 2.2
nav_title: Tarjetas Banner
article_title: Tarjetas Banner
description: "En esta página encontrarás todo lo relacionado con las tarjetas Banner, incluidos artículos sobre cómo crear tarjetas Banner y casos de uso."
channel:
- Banners
---

# Tarjetas Banner

> Con las tarjetas de presentación, puedes crear mensajes personalizados para tus usuarios, al tiempo que amplías el alcance de tus otros canales, como el correo electrónico o las notificaciones push. Al igual que [las tarjetas de contenido]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/about), puedes incrustar tarjetas directamente en tu aplicación o sitio web, lo que te permite interactuar con los usuarios a través de una experiencia natural.

{% alert important %}
Las tarjetas de estandarte están actualmente en acceso anticipado. Ponte en contacto con tu director de cuentas de Braze si estás interesado en participar en este acceso anticipado.
{% endalert %}

## Ejemplos

Como las tarjetas Banner nunca caducan y se personalizan automáticamente cada vez que un usuario inicia una nueva sesión, son ideales para:

- Destacar contenido destacado
- Notificar a los usuarios los próximos eventos
- Compartir actualizaciones sobre programas de fidelización

## Acerca de las tarjetas Banner

### Caducidad de la tarjeta

Por defecto, las tarjetas Banner no caducan; sin embargo, puedes elegir una fecha de finalización si es necesario.

### ID de colocación {#placement-ids}

Las colocaciones de tarjetas de banners son únicas para cada espacio de trabajo y pueden utilizarse en 10 campañas dentro de un mismo espacio de trabajo. Además, a las colocaciones dentro de cada espacio de trabajo se les debe asignar un ID único. Crearás ubicaciones y les asignarás ID cuando [crees una campaña de]({{site.baseurl}}/developer_guide/banner_cards/creating_campaigns/) [Tarjetas Banner]({{site.baseurl}}/developer_guide/banner_cards/embedding_cards/) o [integres Tarjetas Banner en tu aplicación]({{site.baseurl}}/developer_guide/banner_cards/embedding_cards/).

{% alert important %}
Evita modificar los ID de ubicación después de lanzar una campaña de tarjeta de publicidad.
{% endalert %}

### Prioridad de la tarjeta {#card-priority}

Cuando varias campañas hacen referencia al mismo ID de colocación, las tarjetas se muestran por orden de nivel de prioridad. Por predeterminado, las tarjetas de presentación recién creadas se establecen en media, pero puedes [establecer manualmente la prioridad]({{site.baseurl}}/developer_guide/banner_cards/creating_banner_cards/#set-card-priority) en alta, media o baja. Si varias tarjetas comparten el mismo nivel de prioridad, se mostrará primero la tarjeta más reciente.

### Métricas

Estas son las métricas más importantes de la Tarjeta Banner. Para obtener una lista completa de métricas, definiciones y cálculos, consulta el [Glosario de métricas del informe]({{site.baseurl}}/user_guide/data/report_metrics/).

| Métrica | Definición |
| --- | --- |
| [Impresiones totales]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics#total-impressions) | El número de veces que el mensaje se ha cargado y aparece en la pantalla de un usuario, independientemente de la interacción previa (por ejemplo, si a un usuario se le muestra un mensaje dos veces, se le contará dos veces). |
| [Impresiones únicas]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics#unique-impressions) | El número total de usuarios que recibieron y vieron un mensaje determinado en un día. Cada usuario sólo se cuenta una vez. |
| [Clics totales]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics#total-clicks) | El número total (y porcentaje) de usuarios que hicieron clic en el mensaje entregado, independientemente de si el mismo usuario hace clic varias veces. |
| [Clics únicos]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics#unique-clicks) | El número distinto de destinatarios que han hecho clic dentro de un mensaje al menos una vez y se mide por [`dispatch_id`]({{site.baseurl}}/help/help_articles/data/dispatch_id/). Cada usuario sólo se cuenta una vez. |
| [Conversiones primarias]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics#primary-conversions-a-or-primary-conversion-event) | El número de veces que se ha producido un evento definido después de interactuar o ver un mensaje recibido de una campaña Braze. Este evento definido lo determinas tú al crear la campaña. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Próximos pasos

Ahora que ya conoces las tarjetas Banner, estás preparado para los siguientes pasos:

- [Creación de campañas de tarjetas Banner]({{site.baseurl}}/developer_guide/banner_cards/creating_campaigns/)
- [Insertar tarjetas Banner en tu aplicación]({{site.baseurl}}/developer_guide/banner_cards/embedding_cards/)
