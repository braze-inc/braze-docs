---
nav_title: Intelligent Selection
article_title: Intelligent Selection
page_order: 1.0
description: "Este artículo describe Intelligent Selection, una función que analiza el rendimiento de una campaña o Canvas recurrente dos veces al día y ajusta automáticamente el porcentaje de usuarios que reciben cada variante de mensaje."
search_rank: 10
toc_headers: h2
---

# Intelligent Selection {#intelligent-selection}

> Intelligent Selection es una función que analiza el rendimiento de una campaña o Canvas recurrente dos veces al día y ajusta automáticamente el porcentaje de usuarios que reciben cada variante de mensaje.

## Acerca de Intelligent Selection

Una variante que parece rendir mejor se enviará a más usuarios, mientras que las variantes con peor rendimiento se dirigirán a menos usuarios. Cada ajuste se realiza mediante un [algoritmo estadístico](https://en.wikipedia.org/wiki/Multi-armed_bandit) que garantiza que Braze ajusta por diferencias de rendimiento reales y no por casualidad.

![Sección de pruebas A/B de una campaña con Intelligent Selection activado.]({% image_buster /assets/img/intelligent_selection1.png %})

Intelligent Selection:

- revisa repetidamente los datos de rendimiento y desplaza el tráfico de la campaña gradualmente hacia las variantes ganadoras;
- comprueba que más usuarios reciban tu mejor variante sin sacrificar la confianza estadística;
- descarta variantes con peor rendimiento e identifica variantes de alto rendimiento más rápido que una [prueba A/B tradicional]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/);
- prueba con más frecuencia y con mayor confianza en que tus usuarios verán tu mejor mensaje.

Intelligent Selection funciona mejor para campañas que envían más de una vez. Para campañas de un solo envío, recomendamos una [prueba A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) tradicional.

## Requisitos previos

Antes de añadir Intelligent Selection a tu campaña, asegúrate de que:

- tu campaña se envía en un horario recurrente (los envíos únicos no son compatibles);
- has añadido al menos dos variantes de mensaje;
- has definido un evento de conversión para medir el rendimiento entre variantes;
- la ventana de re-elegibilidad es de 24 horas o más (las ventanas más cortas no son compatibles, ya que afectarían la integridad de la variante de control).

Para un Canvas: el paso de mensaje incluye al menos dos variantes y al menos un evento de conversión.

Para los pasos de añadir a campañas y Canvas, tiempo de ejecución, distribución de variantes y FAQ, consulta la versión completa de este artículo en el índice de la izquierda o la ayuda del dashboard de Braze.
