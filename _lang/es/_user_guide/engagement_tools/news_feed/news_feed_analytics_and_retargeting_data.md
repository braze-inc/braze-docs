---
nav_title: Análisis de noticias
article_title: Análisis de canales de noticias y datos de reorientación
page_order: 10
page_type: reference
description: "Este artículo de referencia trata del análisis de las noticias y de varios filtros relacionados."
tool: 
- Reports
channel: news feed
hidden: true

---

# Análisis de noticias

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

> Al igual que las campañas programadas, la herramienta News Feed incluye un panel de análisis para controlar las impresiones, los clics y el porcentaje de clics. Al hacer clic en un mensaje de noticias específico en el panel de control, aparece una gran cantidad de análisis visuales. 

En la parte superior de la página, puede seleccionar el intervalo de fechas de los datos y ver una visualización rápida de las métricas más importantes. Además, puedes ver datos específicos sobre este mensaje del canal de noticias, como cuándo se envió y a quién se envió.

![Detalles y análisis del canal de noticias.][19]

Si desplaza la página hacia abajo, podrá ver un desglose más amplio de sus clics e impresiones día a día. Los clics/impresiones totales se comparan fácilmente con los clics e impresiones únicos mediante gráficos de líneas, mientras que el porcentaje de clics se presenta como un gráfico de barras interactivo.

![Gráfico de desglose del rendimiento.][20]

## Datos de reorientación

Puede aprovechar los datos de Braze sobre los usuarios que interactúan con sus noticias a través de filtros de segmentos que le permiten reorientar comportamientos específicos.

### Filtro de impresión de alimentación

Braze rastrea automáticamente cuándo los usuarios ven el feed y cuántas veces lo han visto. Hay dos filtros disponibles:

- Última fuente de noticias vista
- Recuento de visualizaciones del canal de noticias

**Últimas noticias vistas** es una forma eficaz de utilizar otros canales para atraer de nuevo a los usuarios al feed. Esto puede hacerse fácilmente con notificaciones push y notificaciones dentro de la aplicación. Braze ha visto incrementos de más del 100 % en las impresiones del canal de noticias con una segmentación eficaz. A medida que aumenta el conocimiento de la fuente, estos beneficios se mantienen.

**El recuento de visualizaciones del canal de noticias** puede utilizarse para dirigirse a usuarios que nunca han visto la fuente o que la han visto raramente, con el fin de fomentar más impresiones de tus tarjetas.

Considere la posibilidad de utilizar estos filtros en tándem o con otros filtros para crear una llamada a la acción aún más específica.

### Filtro de tarjetas pulsado

Puede crear segmentos basados en cómo los usuarios han interactuado con tarjetas específicas en el feed. El filtro está en la sección de reorientación de la lista de filtros y se llama Tarjeta a la que se hizo clic.

### Ha pulsado el filtro de tarjetas

- Funciona bien para volver a dirigirse a usuarios que han hecho clic en una tarjeta, pero no han seguido la llamada a la acción.
- También es útil para reorientar a los usuarios con contenidos relacionados que puedan interesarles.
- También puede utilizar este filtro para dirigirse a usuarios que no hicieron clic en una tarjeta. Este filtro puede aplicarse a tarjetas concretas para que desaparezcan del feed de un usuario después de que éste haga clic en ellas.
  - Para configurar esto, después de crear una tarjeta vuelva atrás y edite el segmento de destino para incluir **Has not clicked**.
  - Después de que un usuario haga clic en la tarjeta, ésta saldrá automáticamente del feed cuando se inicie la siguiente sesión del usuario.
  - Evite el uso excesivo de esta orientación porque los usuarios pueden acabar con feeds vacíos. La mejor práctica es utilizar una combinación de contenidos estáticos y eliminados automáticamente.
- También funciona bien para volver a dirigirse a los usuarios que no hacen clic en una tarjeta para que sigan con otra llamada a la acción.

![Ejemplo de filtro de segmento que muestra los usuarios objetivo que no han hecho clic en la tarjeta "¡Salud! Qué hacer y qué no hacer al brindar".][14]


[19]: {% image_buster /assets/img_archive/braze_newsfeedanalytics.png %}
[20]: {% image_buster /assets/img_archive/braze_newsfeedanalytics2.png %}
[14]: {% image_buster /assets/img_archive/braze_newsfeedsegment.png %}
