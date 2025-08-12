---
nav_title: Usuarios perdidos en el segmento
article_title: Usuarios perdidos en el segmento
page_order: 1

page_type: solution
description: "Este artículo de ayuda te guía a través de los pasos para la solución de problemas si no aparecen usuarios en tu segmento, pero esperas que aparezcan más."
tool: Segments
---

# Usuarios que faltan en el segmento

Hay dos soluciones posibles cuando ves `0` usuarios, pero anticipaste más:
* [Calcular estadísticas exactas](#calculate-exact-statistics)
* [Verificar la transferencia de datos](#verify-data-transfer)

## Calcular estadísticas exactas

Las estadísticas del segmento podrían estar proporcionando una estimación. La estimación se calcula a partir de una muestra aleatoria con un intervalo de confianza del 95 % de que el resultado está dentro de `+/- 1%`. Cuanto menor sea tu base de usuarios, más probable es que el tamaño de tu segmento sea una estimación aproximada. Haz clic en **Calcular estadísticas exactas** en el panel **Detalles del segmento**. Esto calculará el número exacto de usuarios de tu segmento.

![Panel de detalles del segmento que muestra la opción Calcular estadísticas exactas]({% image_buster /assets/img_archive/trouble8.png %})

## Verifica la transferencia de datos

Es posible que los datos que estás filtrando no se estén enviando a Braze. Para comprobar qué eventos personalizados se envían a Braze, consulta tu [Informe de eventos personalizados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-analytics).

Selecciona el evento personalizado junto con las fechas y la aplicación específicas para ver qué datos se transfieren realmente a Braze. Si observas que se están enviando datos `0` a Braze, el siguiente paso es evaluar cómo estás enviando los eventos a Braze.

![Gráfico que muestra el recuento de eventos personalizados como cero]({% image_buster /assets/img_archive/trouble9.png %})

{% alert important %}
Los datos que ves en el panel de Braze pueden no tener la misma sintaxis que los que envías a Braze. Asegúrate de que coinciden exactamente.
{% endalert %}

¿Aún necesitas ayuda? Abre un [ticket de soporte]({{site.baseurl}}/braze_support/).

_Última actualización el 5 de enero de 2021_

