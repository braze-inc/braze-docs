---
nav_title: Generador de informes (legado)
article_title: Generador de informes (heredado)
alias: /report_builder_legacy/
page_order: 0
page_type: reference
description: "Esta página explica cómo ejecutar un informe utilizando el generador de informes heredado, incluyendo la creación de informes comparativos de campaña y Canvas, y la creación de informes y gráficos."
tool: 
  - Reports

---

# Generador de informes (heredado)

> El generador de informes te permite comparar los resultados de varias campañas o Canvases en una sola vista, para que puedas determinar fácilmente qué estrategias de interacción han tenido un mayor impacto en tus métricas clave. Tanto para las campañas como para los Lienzos, puedes exportar tus datos y guardar tu informe para consultarlo en el futuro.<br><br>Para obtener una lista descriptiva de las métricas que encontrarás en tus informes, consulta el [Glosario de métricas de los informes]({{site.baseurl}}/user_guide/data/report_metrics/).

\![Ejemplo de comparación de campañas]({% image_buster /assets/img/campaign_comparison/campaign_main.png %}){: style="max-width:80%;"}

Utiliza este informe para responder a las preguntas clave de la interacción, por ejemplo:

- ¿Cuáles fueron las campañas o los Canvases con mejor rendimiento para una etiqueta o canal concretos?
- ¿Qué variantes de las campañas multivariantes tuvieron el mayor aumento respecto al control?  
- ¿Qué campaña de promoción estacional dio lugar a una mayor tasa de compra: las rebajas de verano, las rebajas de otoño o las rebajas de invierno?
- ¿Qué notificaciones push dentro de este Canvas tuvieron las tasas de apertura más altas?
- ¿Qué pasos de este grupo de Lienzos tuvieron más conversiones?
- ¿La Versión 1 de un correo electrónico de bienvenida o la Versión 2 de un correo electrónico de bienvenida produjo una mayor interacción y conversión? ¿Funcionaron los cambios?
- ¿Cómo afectan los distintos métodos de entrega (por ejemplo, 3 push programados, 3 push basados en acciones y 3 push activados por API) a tus tasas de apertura, tasas de conversión o tasas de compra?
- ¿Han repercutido positivamente en tus KPI a lo largo del tiempo las mejoras continuas de los mensajes de usuario que caducan?

{% alert tip %}
Intenta utilizar los mismos eventos de conversión para la conversión A, B, etc. en todas las campañas y Canvases que desees comparar, para que puedas alinear estas conversiones en tus informes del Generador de informes.
{% endalert %}

## Ejecutar un informe

### Paso 1: Crear informe nuevo

Dentro del panel, ve a **Análisis** > **Generador** de informes **.**

Selecciona **Crear informe nuevo** y elige un informe comparativo de campaña o un informe comparativo de Canvas.

Si decides ejecutar un informe sobre campañas, puedes elegir entre un informe **Manual** o **Automatizado**. Los informes pueden contener campañas o Lienzos, pero no ambos a la vez. Todas las campañas y Lienzos que hayan enviado mensajes por última vez en los últimos 12 meses serán elegibles para un informe.

\![Panel de campaña]({% image_buster /assets/img/campaign_comparison/create_report.png %}){: style="max-width:80%;"}

A continuación se exponen las diferencias entre estas dos opciones:

| **Acción** | **Manual** | **Automatización** |
| ---- | ---------- | ------------- |
| **Informe de construcción** | Podrás restringir tu lista de campañas utilizando filtros, y luego marcar campañas específicas. | Construirás tu informe utilizando las opciones de filtrar para acotar tu lista de campañas. |
| **Guardar y ver el informe** | Puedes guardar tu informe. La próxima vez que lo veas, podrás ver la misma campaña que añadiste anteriormente, ya que estas campañas siguen estando dentro de tu filtro "Últimos enviados". | Puedes guardar tu informe. La próxima vez que lo visualices, el informe se actualizará automáticamente para incluir todas las campañas que actualmente coincidan con tus filtros. |
| **Informe de edición** | Puedes seleccionar **Editar informe** para añadir o eliminar campañas de tu informe | Puedes editar tu informe ajustando tus criterios de filtrado. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert note %}
Tanto los informes **manuales** como los **automatizados** pueden incluir un máximo de 250 campañas en un informe.
{% endalert %}

Los informes de Canvas funcionan de forma similar a un informe de campaña manual, en el sentido de que las selecciones de Canvas y las actualizaciones de los informes también deben hacerse manualmente. Puedes incluir un máximo de cinco Lienzos en un informe.

### Paso 2: Elige tus métricas

Después de crear tu informe, encontrarás una tabla en blanco que contiene campañas en cada fila. La tabla se rellenará después de que selecciones **Editar columnas** y elijas las métricas que quieras añadir.

Opciones de campaña]({% image_buster /assets/img/campaign_comparison/campaign_comparison_columns.png %}){: style="max-width:80%;"}

Tu tabla se rellenará con las métricas que elijas. Para las definiciones de estas métricas, consulta el [Glosario de Métricas del Informe]({{site.baseurl}}/user_guide/data/report_metrics/). Algunas métricas sólo están disponibles para los informes de comparación de campañas.

También puedes alternar los cálculos de la **Media** de cualquier tasa o métrica numérica y el **Total** de cualquier métrica numérica.

### Paso 3: Elige un periodo de tiempo

Puedes seleccionar un periodo de tiempo específico para ver los datos de tu informe. Si una determinada campaña, Canvas, variante en Canvas o componente de Canvas no tiene datos para el periodo de tiempo seleccionado, los resultados de esa fila estarán en blanco. 

\![Métrica numérica de la campaña]({% image_buster /assets/img/campaign_comparison/metric.png %}){: style="max-width:60%;"}

### Paso 4: Pon un nombre a tu informe y guárdalo

Pon un nombre a tu informe antes de guardarlo. Si se guarda un informe sin nombrarlo, Braze aplicará un nombre predeterminado de "Informe de Comparación de Campañas".

\![Nota de campaña]({% image_buster /assets/img/campaign_comparison/comparison_name.png %}){: style="max-width:60%;"}

Cuando estés listo, selecciona **Guardar**. Los informes guardados se pueden ver más adelante en la página **del generador de informes**.

## Informe de comparación de campañas con campañas multivariantes

Para cualquier campaña multivariante, puedes ver estas métricas desglosadas por tus variantes y grupo de control haciendo clic en la flecha situada junto al nombre de la campaña. Las filas que contienen tus variantes incluirán los resultados de rendimiento de esa variante, y la fila que contiene tu control incluirá sólo los resultados de tus eventos de conversión. 

\![Nota de campaña]({% image_buster /assets/img/campaign_comparison/compare_note.png %}){: style="float:right;max-width:15%;margin-left:15px;"}

Las métricas que rellenan la fila de tu campaña general reflejarán el rendimiento de sus variantes, pero no incluirán el rendimiento del control. Por ejemplo, el Evento de conversión primaria A de tu campaña general será la suma del Evento de conversión primaria A de tus variantes, y esto no incluirá el Evento de conversión primaria A de tu control.

{% alert important %}
Si eliminas una variante de una campaña multivariante, los datos de esa variante no estarán disponibles para su uso en un informe futuro.
{% endalert %}

## Desglose del informe comparativo de Canvas

Dentro de un informe Canvas, puedes ver tus Canvas desglosados por variantes, pasos o mensajes.

### Variante

Si seleccionas el **desglose por variante**, podrás ver las estadísticas de alto nivel de todos tus Canvas, así como las estadísticas de cada variante, que pueden ampliarse seleccionando la flecha situada junto al nombre del Canvas.

Variantes]({% image_buster /assets/img/campaign_comparison/campaign_comparison1.png %}){: style="max-width:90%;"}

### Pasos 

Si seleccionas el **desglose por pasos**, podrás ver las métricas a nivel de paso, y cada fila del informe contendrá la fila de un paso.

\![Pasos]({% image_buster /assets/img/campaign_comparison/campaign_comparison2.png %}){: style="max-width:90%;"}

### Mensaje

De forma similar a un desglose por pasos, al seleccionar **desglose por mensajes** se muestra el nombre de los pasos en cada fila. Sin embargo, dentro de **las columnas de edición**, tendrás acceso a las métricas a nivel de mensaje, como las estadísticas específicas del canal, como los clics por correo electrónico y las aperturas push.

Informe]({% image_buster /assets/img/campaign_comparison/campaign_comparison3.png %}){: style="max-width:90%;"}

Ten en cuenta que, dentro del panel de Braze, puedes obtener una vista previa de las 50 primeras filas de tu informe Canvas. Puedes acceder al informe completo cuando exportes un CSV.

## Acceder a los informes guardados

Cuando accedes a un **Informe manual** guardado, puedes ver las mismas campañas que añadiste anteriormente, ya que estas campañas siguen estando dentro de tu filtro "Último envío".

Cuando accedas a un **Informe automático** guardado, el informe se actualizará automáticamente para incluir todas las campañas que actualmente coincidan con tus filtros. Por ejemplo, si tu informe filtró campañas con la etiqueta "Promoción", cada vez que veas este informe, podrás ver todas las campañas con la etiqueta "Promoción", incluso si estas campañas se crearon después de que hicieras este informe.

## Editar informes

En un **Informe Manual**, puedes editar un informe seleccionando **Editar**. Desde ahí, puedes seleccionar o deseleccionar campañas para incluirlas en tu informe.

En un **Informe automático**, sólo tienes que alternar los filtros para limitar los resultados de tu informe.

## Exportar informes

También puedes seleccionar **Exportar** para descargar tu informe a CSV.

Si tu informe contiene alguna campaña multivariante, tu exportación incluirá dos archivos CSV: 

- Un archivo que contiene sólo las métricas de nivel superior de cada campaña
- Un archivo que contiene métricas a nivel de variante

El archivo que contenga métricas variantes tendrá `variant_` añadido al principio de su nombre. La primera vez que exportes un informe automatizado, aparecerá una ventana emergente pidiéndote permiso para descargar varios archivos: haz clic en **Permitir**.

Descarga de la campaña]({% image_buster /assets/img/campaign_comparison/download.png %}){: style="max-width:60%;"}

### Exportar informes de comparación de Canvas

Tu exportación CSV reflejará la vista de desglose en la que estabas cuando seleccionaste **Exportar**. Por ejemplo, si estabas en la vista de desglose por pasos, tu exportación contendrá datos sobre las métricas de tus pasos. Para exportar datos de un desglose diferente, tendrás que navegar primero a ese desglose y seleccionar **Exportar** desde allí.

Si descargas un informe de desglose de variantes en Canvas, recibirás dos archivos CSV:

- Un archivo que contiene sólo las métricas de nivel superior de cada Canvas
- Un archivo que contiene métricas a nivel de variante

## Tablas de construcción 

Utiliza gráficos para visualizar una métrica seleccionada en tu informe. Los gráficos están disponibles para los informes que presentan campañas y tienen al menos una métrica añadida a sus columnas.

\![Gráfico de rendimiento de la campaña con métrica Mensaje enviado seleccionado]({% image_buster /assets/img/campaign_comparison/report_builder_charts.png %})

Por defecto, el gráfico de cada informe mostrará la métrica en la primera columna del informe. Para seleccionar una métrica diferente para el gráfico, elige tu métrica en el desplegable. Cualquier métrica de tu tabla de informes estará disponible para mostrarse en tu gráfico.

Puedes representar gráficamente un máximo de tres métricas. Las unidades de todas las métricas deben ser las mismas: por ejemplo, si eliges una tasa en el primer desplegable, sólo podrás seleccionar tasas en el segundo.

Si tu gráfico sólo contiene una métrica, mostrará hasta 30 campañas en orden descendente según la métrica que hayas seleccionado. Por ejemplo, si la métrica de tu gráfico son los clics de correo electrónico, entonces tu gráfico mostrará las 30 campañas de correo electrónico con más clics, ordenadas de mayor a menor número de clics. Si tu informe contiene más de 30 campañas, sólo se mostrarán en el gráfico las 30 principales. Si seleccionas más de una métrica, tu gráfico sólo mostrará las cinco mejores campañas basadas en la primera métrica seleccionada.

Actualmente, los gráficos no se guardan al guardar el informe.



