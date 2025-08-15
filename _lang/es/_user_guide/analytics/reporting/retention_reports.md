---
nav_title: Informes de retención
article_title: Informes de retención para campañas y lonas
page_order: 5
tool: Reports
page_type: reference
description: "Esta página explica cómo medir la retención de usuarios que realizaron un evento de retención seleccionado en una campaña o Canvas concretos."
---

# Informes de retención

> La retención de usuarios es una de las métricas más importantes para cualquier profesional del marketing. Mantener a los usuarios comprometidos volviendo a por más indica que el negocio va viento en popa. Braze le permite medir la retención de usuarios directamente en la página **Analytics** de su campaña o Canvas.

{% alert important %}
Los informes de retención no están disponibles para las campañas activadas por API.
{% endalert %}

## Ejecutar un informe de retención

### Paso 1: Seleccione un intervalo de fechas

![Fecha del informe]({% image_buster /assets/img/date_select_retention.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

Para empezar, visite cualquier campaña o Canvas en el panel de control de Braze y seleccione un intervalo de fechas para el informe. Seleccionar un intervalo de fechas adecuado es crucial por la forma en que afecta a los informes de retención. 

Este informe incluirá todos los usuarios que entraron inicialmente en la campaña o Canvas durante esta ventana, y de esos usuarios, aparecerán en el informe los datos de aquellos que realizaron su evento de retención durante el intervalo de fechas.

Para seleccionar un intervalo de fechas, ve a la página **de análisis de** la campaña o de Canvas y selecciona varios intervalos o establece un intervalo personalizado para tu informe.

### Paso 2: Seleccione un evento de retención

{% tabs %}
{% tab Campaña %}

A continuación, ve a la sección **Retención de campaña**. La retención de campaña le muestra la tasa en la que cualquier usuario que ha recibido esta campaña específica ha realizado un evento de retención (especificado por usted en el informe de retención) durante los 30 días desde el momento en que recibió la campaña.

{% endtab %}
{% tab Canvas %}

A continuación, selecciona **Analizar variantes**. Desde aquí, puede analizar sus variantes, consultar su informe de embudo y ver su informe de retención. La retención de Canvas le muestra la tasa en la que cualquier usuario que ha recibido este Canvas específico ha realizado un evento de retención (especificado por usted en el informe de retención) durante los 30 días desde el momento en que recibió el Canvas.

{% endtab %}
{% endtabs %}

![Selecciona un evento de Retención]({% image_buster /assets/img/retention_1.png %}){: style="max-width:80%"}

### Paso 3: Generar el informe

Cuando hayas seleccionado un evento de retención, selecciona **Ejecutar informe** para iniciar la consulta.

![Ejecutar informe]({% image_buster /assets/img/retention_2.png %}){: style="max-width:80%"}

Esta consulta puede tardar unos minutos en ejecutarse, dependiendo de la cantidad de datos que haya que recuperar para generar los resultados. Si tarda demasiado, verás una notificación pidiéndote que vuelvas a intentar cargar el informe. Puede que tengas que esperar hasta cinco minutos antes de que se cargue el informe.

Una vez generado el informe, no se puede volver a ejecutar con el mismo evento de retención durante 24 horas. Siempre verá una marca de tiempo de la última vez que se generó el informe, y una opción para regenerarlo, si ha pasado más de un día. Sin embargo, puede cambiar el evento de retención y volver a ejecutar el informe para ver el impacto de la campaña en diferentes KPI.

El informe sólo mostrará los días en los que la campaña o el Canvas enviaron mensajes. Para algunas campañas y lienzos, eso puede significar que el informe sólo muestre un día si sólo se envió una vez. Si es recurrente o se activa, es posible que aparezcan varios días en la tabla.

{% tabs %}
{% tab Campaña %}

![Informe completo]({% image_buster /assets/img/campaign_retention3.png %})

{% endtab %}
{% tab Canvas %}

![Informe completo]({% image_buster /assets/img/canvas_retention_report.png %}){: style="max-width:70%"}

{% endtab %}
{% endtabs %}

## Explicación del informe

El informe de retención ofrece tanto una fórmula de retención rodante como una fórmula de retención por rangos. Para ver su informe de campaña o de Canvas con uno de estos tipos de retención, seleccione **Retención continua** o **Retención por intervalos** para su **Tipo de retención**.

### Retención escalonada

La retención continua mide cuántos usuarios vuelven y realizan el evento de retención en o después de cualquiera de los días enumerados en la parte superior del informe. Así, si un usuario inició una sesión entre el tercer y el séptimo día, se contará como usuario retenido en las columnas "3 días", "1 día" y "0 días". Cualquier usuario que se contabilice como retenido después de la marca de 30 días desde que se envió la campaña o el Canvas se contabilizará en la columna "30 días" de esa fila.

Un usuario que complete el evento varias veces durante un periodo de más de 30 días se contabilizará como parte de varios periodos de tiempo. Por ejemplo, un usuario que complete una sesión después de un día se incrementará en las columnas para >0 y >1. Si después completan la prueba al cabo de tres días, volverán a incrementarse en las columnas anteriores (>0 y >1), lo que podría hacer que la tasa de retención superara el 100%.

#### Cómo leer los informes de retención rodante

La forma de leer el gráfico del informe de retención para una columna del día tres sería Y% o Y número de usuarios (en función de las unidades elegidas) que realizaron el evento tres o más días después de recibir la campaña el día Z.

![Informe escalonado]({% image_buster /assets/img/campaign_retention3.png %})

Como otro ejemplo, refiriéndonos a la tabla de la imagen anterior, el 25 de marzo, un total de 38 usuarios realizaron el evento de retención. La retención en el día cero fue del 68,42%, lo que significa que el 68,42% de los usuarios realizaron el evento de retención cero o más días (en el día cero o más tarde) después de recibir la campaña. La retención el séptimo día fue del 57,89%, lo que significa que el 57,89% de los usuarios realizaron el evento siete días o más (el séptimo día o más tarde) después de recibir la campaña.

Esta información puede ser útil si quieres saber el porcentaje de usuarios que han utilizado y no han utilizado tu producto 30 días después de su primer uso. Un valor porcentual o numérico en la columna del día 30 le indica el porcentaje de usuarios que volvieron el día 30 o después.

### Conservación de la gama

La retención por intervalos mide cuántos usuarios vuelven en el intervalo de días indicado en la parte superior del informe. Así pues, si un usuario iniciara una sesión entre los días 3 y 7 y volviera a hacerlo el día 13, se contaría como retenido tanto en el intervalo de "Día 3-7" como en el de "Día 7-14".

#### Cómo leer los informes de retención de la gama

Los informes de rangos son unos de los más intuitivos de leer. Indican claramente, de todos los usuarios de una cohorte, qué porcentaje de esos usuarios realizó el evento de retención dentro de un intervalo de fechas determinado. Por ejemplo, en la siguiente imagen, haciendo referencia a la cohorte Todos los usuarios, en el intervalo de fechas "Día 0 (0-24hrs)", el 35,71% de la cohorte realizó el informe de retención. Si un usuario realiza varios eventos de retención dentro de varios intervalos de fechas, se contarán como retenidos para cada intervalo.

![Informe de retención]({% image_buster /assets/img/range_retention.png %})

### Componentes del informe de retención

- **Columna de usuarios**: El valor mostrado es el número de usuarios únicos que realizaron la acción de inicio dentro del periodo de tiempo seleccionado; el recuento de usuarios para el día actual se excluirá ya que se está calculando. 
- **Filas de la cohorte Z**: Muestra los días en los que la campaña o Canvas estuvo enviando mensajes.
- **Día X Columnas**: Días comprendidos entre 0 y 30 días en varios incrementos.
- **Fila de Todos los usuarios**: También conocida como fila de resumen del informe, resume los datos de retención de todo el periodo de tiempo. Tenga en cuenta que si un usuario ha recibido la campaña o Canvas en varias cohortes, sus resultados se contarán dos veces aquí. 
- **Porcentajes/Números**: Muestra el porcentaje o número de usuarios que realizaron el evento X o más días después de recibir la campaña o Canvas el día Z. Estos porcentajes son los porcentajes medios ponderados. Los valores incompletos se señalarán con un asterisco.
- **Intervalo de fechas**: Establecido en la página de **detalles de** la campaña o del lienzo, el intervalo de fechas incluye a todos los usuarios que recibieron la campaña o el lienzo durante esta ventana, y de esos usuarios, aparecerán en el informe los datos de aquellos que realizaron su evento de retención durante el intervalo de fechas.
- **Unidades**: Puede ajustar las unidades entre el porcentaje de usuarios y el número de usuarios en la esquina superior derecha del gráfico, las unidades específicas pueden resultar más significativas a la hora de juzgar el impacto de una campaña o Canvas.
- **Mapeado de colores**: En su informe de retención, los porcentajes o el número de usuarios más altos se asignan a tonos más oscuros de azul. A los porcentajes o números de usuarios más bajos se les asignan tonos más claros de azul. Esto se hace para ayudar a los usuarios a visualizar estos datos.
- **Gráfico del Informe de retención**: Este gráfico resume los resultados de todas las cohortes para el intervalo de fechas seleccionado.

### Rendimiento por variante

La visualización de su informe de retención por variante le permite comparar la retención continua para cada variante o variación de mensaje para el periodo de tiempo seleccionado, así como el Grupo de control. Este informe puede visualizarse cambiando **Mostrar rendimiento para** a **Por variante**.

Algunos casos de uso para mostrar el rendimiento por variante:

- ¿Tiene algunas variantes o experimentos en los que los resultados parecen un esfuerzo inútil o no tienen significación estadística? Echa otro vistazo y comprueba si uno u otro tuvo un impacto de cola más larga.
- Comprueba cómo es la retención si no enviaste ningún mensaje indagando en los datos de retención del grupo de control.

{% tabs %}
{% tab Campaña %}

![Vista por variante]({% image_buster /assets/img/variant_view.png %})

{% endtab %}
{% tab Canvas %}

![Vista por variante]({% image_buster /assets/img/variant_view_canvas.png %})

{% endtab %}
{% endtabs %}

#### Informe de retención por componentes variantes

- **Intervalo de fechas**: Establecido en la página **Detalles de** la campaña o del lienzo, el intervalo de fechas incluye a todos los usuarios que recibieron la campaña o el lienzo durante esta ventana, y de esos usuarios, aparecerán en el informe los datos de aquellos que realizaron su evento de retención durante el intervalo de fechas. Cada día se mide la tasa de retención, el porcentaje de cambio respecto al grupo de control y la confianza.
- **Tasa de retención**: Muestra la tasa de retención por variante. La tasa de retención equivale al número de usuarios que han realizado el evento de retención dividido por el total de usuarios que han recibido la campaña o Canvas.
- **Porcentaje de cambio respecto al control**: Cuantifica el cambio porcentual por variante respecto al grupo de control.
- **Confianza**: {% multi_lang_include metrics.md metric='Confidence' %} Braze compara la tasa de conversión de cada variante con la tasa de conversión del control mediante un procedimiento estadístico llamado Prueba Z para calcular un porcentaje de [confianza]({{site.baseurl}}/user_guide/intelligence/multivariate_testing/#understanding-confidence).
- **Unidades**: Puede ajustar las unidades entre el porcentaje de usuarios y el número de usuarios en la esquina superior derecha del gráfico, las unidades específicas pueden resultar más significativas a la hora de juzgar el impacto de una campaña o Canvas.
- **Gráfico de variante**: Este gráfico resume los resultados por variante para el intervalo de fechas seleccionado.

## Aspectos a tener en cuenta en los informes de retención

Los informes de retención son fáciles de generar, pero difíciles de interpretar y utilizar. Para ayudar a los profesionales del marketing, hemos reunido un par de temas y preguntas que deben tenerse en cuenta al examinar los informes de retención.

- Tenga en cuenta las tendencias del día de la semana para las campañas recurrentes (por ejemplo, ¿las cohortes de los lunes obtienen mejores resultados que las de los sábados?)
- ¿Dónde empieza a disminuir el impacto? Esto podría ser una señal de que se necesita una nueva campaña o Canvas que se dirija a los usuarios en ese momento como otro impulso a la retención. 
- ¿Observas fatiga de mensajería?
- ¿Tuvo un impacto positivo una optimización específica que hiciste en una campaña o Canvas hace X días?



