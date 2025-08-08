---
nav_title: Generador de informes (heredado)
article_title: Generador de informes (heredado)
alias: /report_builder_legacy/
page_order: 0
page_type: reference
description: "Esta página explica cómo ejecutar un informe utilizando el generador de informes heredado, incluyendo la creación de informes comparativos de campaña y Canvas, y la creación de informes y gráficos."
tool: 
  - Reports

---

# Generador de informes (heredado)

> El generador de informes le permite comparar los resultados de varias campañas o lienzos en una sola vista para que pueda determinar fácilmente qué estrategias de participación han tenido un mayor impacto en sus métricas clave. Tanto para las campañas como para los Lienzos, puedes exportar tus datos y guardar tu informe para consultarlo en el futuro.<br><br>Para obtener una lista descriptiva de las métricas que encontrarás en tus informes, consulta el [Glosario de métricas de los informes]({{site.baseurl}}/user_guide/data/report_metrics/).

![Ejemplo de comparación de campaña]({% image_buster /assets/img/campaign_comparison/campaign_main.png %}){: style="max-width:80%;"}

Utilice este informe para responder a preguntas clave de compromiso, por ejemplo:

- ¿Cuáles han sido las campañas o los lienzos con mejores resultados para una etiqueta o un canal específicos?
- ¿Qué variantes de las campañas multivariantes registraron el mayor aumento con respecto al control?  
- ¿Qué campaña de promoción estacional generó un mayor índice de compras: las rebajas de verano, las rebajas de otoño o las rebajas de invierno?
- ¿Qué notificaciones push dentro de este Canvas tuvieron las tasas de apertura más altas?
- ¿Qué pasos de este grupo de Lienzos tuvieron más conversiones?
- ¿La versión 1 de un correo electrónico de bienvenida o la versión 2 de un correo electrónico de bienvenida consiguió una mayor participación y conversión? ¿Funcionaron los cambios?
- ¿Cómo afectan los distintos métodos de entrega (por ejemplo, 3 push programados, 3 push basados en acciones y 3 push desencadenados por API) a tus tasas de apertura, tasas de conversión o tasas de compra?
- ¿Han repercutido positivamente en sus indicadores clave de rendimiento las continuas mejoras de los mensajes de los usuarios rezagados a lo largo del tiempo?

{% alert tip %}
Intenta utilizar los mismos eventos de conversión para la conversión A, B, etc. en todas las campañas y Canvases que desees comparar, para que puedas alinear estas conversiones en tus informes del Generador de informes.
{% endalert %}

## Ejecutar un informe

### Paso 1: Crear un nuevo informe

En el panel de control, vaya a **Análisis** > **Generador de informes**.

Selecciona **Crear informe nuevo** y elige un informe comparativo de campaña o un informe comparativo de Canvas.

Si decide realizar un informe sobre las campañas, puede seleccionar entre un informe **Manual** o **Automatizado**. Los informes pueden contener campañas o lienzos, pero no ambos a la vez. Todas las campañas y Lienzos que hayan enviado mensajes por última vez en los últimos 12 meses serán elegibles para un informe.

![Panel de campaña]({% image_buster /assets/img/campaign_comparison/create_report.png %}){: style="max-width:80%;"}

A continuación se exponen las diferencias entre estas dos opciones:

| **Acción** | **Manual** | **Automatización** |
| ---- | ---------- | ------------- |
| **Informe de construcción** | Podrá restringir su lista de campañas utilizando filtros y, a continuación, marcar campañas específicas. | Construirá su informe utilizando las opciones de filtro para acotar su lista de campañas. |
| **Guardar y ver el informe** | Puede guardar su informe. La próxima vez que la visualice, podrá ver la misma campaña que añadió anteriormente, ya que estas campañas siguen estando dentro de su filtro "Últimas enviadas". | Puede guardar su informe. La próxima vez que lo visualice, el informe se actualizará automáticamente para incluir todas las campañas que coincidan actualmente con sus filtros. |
| **Informe de edición** | Puedes seleccionar **Editar informe** para añadir o eliminar campañas de tu informe | Puede editar su informe ajustando los criterios de filtrado. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert note %}
Tanto los informes **manuales** como los **automatizados** pueden incluir un máximo de 250 campañas en un informe.
{% endalert %}

Los informes de Canvas funcionan de forma similar a un informe de campaña manual en el sentido de que las selecciones de Canvas y las actualizaciones de los informes también deben realizarse manualmente. Puede incluir un máximo de cinco lienzos en un informe.

### Paso 2: Elija sus métricas

Después de crear tu informe, encontrarás una tabla en blanco que contiene campañas en cada fila. La tabla se rellenará después de que seleccione **Editar columnas** y elija las métricas que desea añadir.

![Opciones de campaña]({% image_buster /assets/img/campaign_comparison/campaign_comparison_columns.png %}){: style="max-width:80%;"}

Su tabla se rellenará con las métricas que elija. Para las definiciones de estas métricas, consulte el [Glosario de métricas del Informe]({{site.baseurl}}/user_guide/data/report_metrics/). Algunas métricas sólo están disponibles para los informes de comparación de campañas.

También puede alternar los cálculos para la **Media** de cualquier tasa o métrica numérica y el **Total** para cualquier métrica numérica.

### Paso 3: Elija un periodo de tiempo

Puede seleccionar un periodo de tiempo específico para ver los datos de su informe. Si una determinada campaña, Canvas, variante en Canvas o componente de Canvas no tiene datos para el periodo de tiempo seleccionado, los resultados de esa fila estarán en blanco. 

![Campaña métrica numérica]({% image_buster /assets/img/campaign_comparison/metric.png %}){: style="max-width:60%;"}

### Paso 4: Asigne un nombre a su informe y guárdelo

Nombra tu informe antes de guardarlo. Si se guarda un informe sin nombrarlo, Braze aplicará un nombre por defecto de "Informe de comparación de campañas".

![Nota de campaña]({% image_buster /assets/img/campaign_comparison/comparison_name.png %}){: style="max-width:60%;"}

Cuando estés listo, selecciona **Guardar**. Los informes guardados pueden consultarse posteriormente en la página **del generador de informes**.

## Informe de comparación de campañas con campañas multivariantes

Para cualquier campaña multivariante, puede ver estas métricas desglosadas por sus variantes y grupo de control haciendo clic en la flecha situada junto al nombre de la campaña. Las filas que contienen sus variantes incluirán los resultados de rendimiento para esa variante, y la fila que contiene su control incluirá sólo los resultados para sus eventos de conversión. 

![Nota de campaña]({% image_buster /assets/img/campaign_comparison/compare_note.png %}){: style="float:right;max-width:15%;margin-left:15px;"}

Las métricas que rellenan la fila de tu campaña general reflejarán el rendimiento de sus variantes, pero no incluirán el rendimiento del control. Por ejemplo, el Evento de conversión primaria A de tu campaña general será la suma del Evento de conversión primaria A de tus variantes, y esto no incluirá el Evento de conversión primaria A de tu control.

{% alert important %}
Si eliminas una variante de una campaña multivariante, los datos de esa variante no estarán disponibles para su uso en un informe futuro.
{% endalert %}

## Desglose del informe comparativo de Canvas

Dentro de un informe de Canvas, puede ver sus Canvases desglosados por variante, pasos o mensaje.

### Variante

Si seleccionas el **desglose por variante**, podrás ver las estadísticas de alto nivel de todos tus Canvas, así como las estadísticas de cada variante, que pueden ampliarse seleccionando la flecha situada junto al nombre del Canvas.

![Variantes]({% image_buster /assets/img/campaign_comparison/campaign_comparison1.png %}){: style="max-width:90%;"}

### Pasos 

Si seleccionas el **desglose por pasos**, podrás ver las métricas a nivel de paso, y cada fila del informe contendrá la fila de un paso.

![Pasos]({% image_buster /assets/img/campaign_comparison/campaign_comparison2.png %}){: style="max-width:90%;"}

### Mensaje

De forma similar a un desglose por pasos, al seleccionar **desglose por mensaje** se muestra el nombre de los pasos en cada fila. Sin embargo, dentro de las **columnas de edición**, tendrá acceso a las métricas a nivel de mensaje, como las estadísticas específicas del canal, como los clics de correo electrónico y las aperturas push.

![Informe]({% image_buster /assets/img/campaign_comparison/campaign_comparison3.png %}){: style="max-width:90%;"}

Tenga en cuenta que en el panel de control de Braze puede previsualizar las 50 primeras filas del informe Canvas. Puede acceder al informe completo cuando exporte un CSV.

## Acceso a los informes guardados

Cuando accedes a un **Informe manual** guardado, puedes ver las mismas campañas que añadiste anteriormente, ya que estas campañas siguen estando dentro de tu filtro "Último envío".

Cuando acceda a un **Informe automático** guardado, el informe se actualizará automáticamente para incluir todas las campañas que coincidan actualmente con sus filtros. Por ejemplo, si tu informe filtró campañas con la etiqueta "Promoción", cada vez que veas este informe, podrás ver todas las campañas con la etiqueta "Promoción", incluso si estas campañas se crearon después de que hicieras este informe.

## Edición de informes

En un **Informe Manual**, puedes editar un informe seleccionando **Editar**. A partir de ahí, puede seleccionar o anular la selección de campañas para incluirlas en su informe.

En un **informe automático**, basta con activar los filtros para limitar los resultados del informe.

## Exportación de informes

También puedes seleccionar **Exportar** para descargar tu informe a CSV.

Si su informe contiene alguna campaña multivariante, su exportación incluirá dos archivos CSV: 

- Un archivo que contiene sólo las métricas de nivel superior de cada campaña
- Un archivo que contiene métricas a nivel de variante

El archivo que contiene las métricas de variantes tendrá `variant_` añadido al principio de su nombre. La primera vez que exporte un informe automatizado, aparecerá una ventana emergente pidiéndole permiso para descargar varios archivos: haga clic en **Permitir**.

![Campaña Descarga]({% image_buster /assets/img/campaign_comparison/download.png %}){: style="max-width:60%;"}

### Exportación de informes de comparación de lienzos

Tu exportación CSV reflejará la vista de desglose en la que estabas cuando seleccionaste **Exportar**. Por ejemplo, si estabas en la vista de desglose por pasos, tu exportación contendrá datos sobre las métricas de tus pasos. Para exportar datos de un desglose diferente, tendrás que navegar primero a ese desglose y seleccionar **Exportar** desde allí.

Si descarga un informe Canvas de desglose de variantes, recibirá dos archivos CSV:

- Un archivo que contiene sólo las métricas de nivel superior para cada lienzo
- Un archivo que contiene métricas a nivel de variante

## Gráfico de construcción 

Utilice gráficos para visualizar una métrica seleccionada en su informe. Los gráficos están disponibles para los informes que incluyen campañas y tienen al menos una métrica añadida a sus columnas.

![Gráfico de rendimiento de la campaña con métrica Mensaje enviado seleccionado]({% image_buster /assets/img/campaign_comparison/report_builder_charts.png %})

Por defecto, el gráfico de cada informe mostrará la métrica en la primera columna del informe. Para seleccionar una métrica diferente para el gráfico, elija su métrica en el menú desplegable. Cualquier métrica de la tabla del informe podrá mostrarse en el gráfico.

Puede representar gráficamente un máximo de tres métricas. Las unidades para todas las métricas deben ser las mismas; por ejemplo, si elige una tasa en el primer desplegable, sólo se podrán seleccionar tasas en el segundo desplegable.

Si el gráfico sólo contiene una métrica, mostrará hasta 30 campañas en orden descendente en función de la métrica seleccionada. Por ejemplo, si la métrica de su gráfico es clics de correo electrónico, entonces su gráfico mostrará las 30 campañas de correo electrónico con más clics, ordenadas de mayor a menor número de clics. Si su informe contiene más de 30 campañas, sólo se mostrarán en el gráfico las 30 primeras. Si selecciona más de una métrica, el gráfico sólo mostrará las cinco mejores campañas según la primera métrica seleccionada.

Actualmente, los gráficos no se guardan al guardar el informe.



