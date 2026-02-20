---
nav_title: Panel de conversiones
article_title: Panel de conversiones
alias: "/conversions_dashboard_v2/"
description: "El panel de control de conversiones le permite analizar las conversiones entre campañas, Canvases y canales, utilizando diferentes métodos de atribución."
page_order: 3
page_type: reference
tool: 
  - Reports
---

# Panel de conversiones

> El panel de conversiones analiza las conversiones entre campañas, Canvases y canales, utilizando varios [métodos de atribución](#attribution-methods). Al medir tus conversiones, puedes especificar el marco temporal, el evento de conversión y la ventana de conversión.

## Configurar el informe

Para configurar su informe de panel de conversiones:

1. Ve a **Análisis** > **Conversiones**.
2. Selecciona un **intervalo de fechas** para tu informe, hasta una ventana de 90 días.
3. Selecciona las campañas o los lienzos (o ambos) que quieras analizar. 
   - (opcional) Filtra campañas y Lienzos seleccionando una etiqueta.  
4. Selecciona el **canal o canales** que quieres analizar para tus mensajes.
5. Selecciona un **Desglose por** capas para ver diferentes dimensiones de los datos, como por variante, paso en Canvas, país o idioma.
6. (Opcional) Si quieres calcular las conversiones de un evento que no se configuró como evento de conversión en la campaña o Canvas, activa [Usar eventos personalizados](#using-custom-events).
7. Selecciona un [método de atribución](#attribution-methods) para analizar los mensajes seleccionados.

{% alert note %}
Si estás analizando conversiones de varios canales, tu **Método de atribución** será, por defecto, **la Atribución de último contacto**.
{% endalert %}

{:start="8"}
8\. Selecciona **Crear** para ejecutar el informe.

Tras cargar la página, selecciona un **Evento de conversión** para filtrar el informe en busca de datos de conversión. Las selecciones disponibles incluirán los eventos preconfigurados en los lienzos y campañas. Si seleccionaste un evento personalizado al configurar tu informe (paso 6), esta opción no estará disponible.

### Uso de eventos personalizados

Para que las métricas de eventos personalizados aparezcan en el panel de conversiones, debes tener un evento de conversión y un evento de entrada en Canvas en el intervalo de fechas especificado en la página. 

Para calcular las conversiones de un evento que no se configuró como evento de conversión en la campaña o Canvas, selecciona un evento personalizado específico para utilizarlo como evento de conversión. 

1. Cuando configure su informe, active **Usar eventos personalizados**.
2. Selecciona un evento personalizado para utilizarlo como evento de conversión.
3. Seleccione la ventana de conversión dentro de la cual debería haberse producido ese evento para que se contabilice como conversión.

{% alert note %}
Si seleccionas un evento personalizado, no verás el desplegable **Evento de conversión** en la página y tendrás que volver a ejecutar el informe para ver las conversiones de diferentes eventos personalizados.
{% endalert %}

### Consideraciones

Para que un usuario se contabilice en el informe, debe cumplir los siguientes criterios dentro del intervalo de fechas seleccionado:
1. Entra en el Canvas o campaña.
2. Registra un [método de atribución]({{site.baseurl}}/user_guide/analytics/dashboard/conversions_dashboard/#attribution-methods).
3. Realiza el evento de conversión.

Por ejemplo, supongamos que un usuario hace lo siguiente:
1. Entra en el Canvas el 30 de septiembre.
2. Registra un método de atribución el 1 de octubre.
3. Realiza el evento de conversión el 2 de octubre.

Este usuario **no** aparecerá en un informe con un intervalo de fechas del 1 al 7 de octubre. Esto se debe a que el usuario entró en el Canvas antes del periodo del informe, aunque el evento de conversión se produjo dentro del intervalo de fechas definido. Para que el usuario aparezca en un informe, el intervalo de fechas debe incluir el 30 de septiembre.

## Comprender tu informe

El informe se divide en tres secciones:

- [Detalles de la conversión](#conversion-details)
- [Embudo de conversión](#conversion-funnel)
- [Conversiones a lo largo del tiempo](#conversions-over-time)

### Detalles de la conversión

La tabla de detalles de conversión siempre muestra una columna para *Destinatarios* y otra para *Conversiones* (tasa y total). Las otras dos columnas de la tabla que aparecen dependen de las opciones seleccionadas al configurar el informe. 

![Tabla de detalles de la conversión que muestra Toques como método de atribución para las columnas tres y cuatro.]({% image_buster /assets/img_archive/conversions2_details.png %}){: style="border:none"}

La siguiente tabla describe las métricas posibles.

| Métrica indicada | Descripción |
| --- | --- |
| Destinatarios | El número de usuarios que recibieron un mensaje a través del canal seleccionado dentro del intervalo de fechas del informe. |
| Tasa de conversión (destinatarios) | Calculada como: (Número de conversiones) / (Número de destinatarios) |
| Método de atribución | Definido por el [método de atribución](#attribution-methods) que seleccionaste al configurar el informe. Para la atribución de Último Toque o si se seleccionan varios canales, aparece como [Toques](#terms-to-know). |
| Tasa de conversión (método de atribución) | Definido por el [método de atribución](#attribution-methods) que seleccionaste al configurar el informe. Si se seleccionan varios canales, el atributo predeterminado es el de última pulsación. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Si seleccionaste detalles a nivel de desglose para campañas o Lienzos al [configurar tu informe](#setting-up-your-report) (paso 5), puedes hacer clic en <i class="fas fa-angle-down"></i> para ampliar la tabla.

### Embudo de conversión

Este gráfico de barras muestra los recuentos absolutos de cada [evento de compromiso]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) en función del canal seleccionado. El recuento de conversiones se definirá según el método de atribución seleccionado.

Por defecto, se muestran todas las campañas y lienzos seleccionados. Para anular la selección de una campaña o Canvas, selecciona el nombre de la campaña o Canvas que quieras excluir. Para obtener más detalles sobre el acto de compromiso, puede pasar el ratón por encima de cada barra.

Para descargar los datos de las series temporales, selecciona una opción de descarga: PNG, JPEG, PDF, SVG o CSV.

{% alert note %}
Este gráfico sólo muestra los datos de un canal cada vez. Utilice el menú desplegable **Canal** del gráfico para seleccionar un único canal.
{% endalert %}

![Gráfico de barras del embudo de conversiones de dos campañas de correo electrónico que muestran resultados similares para el correo electrónico entregado, el correo electrónico abierto, el correo electrónico en el que se ha hecho clic y las conversiones.]({% image_buster /assets/img_archive/conversions2_funnel.png %})

### Conversiones a lo largo del tiempo

Este gráfico de series temporales incluye una representación de las conversiones por campaña o Canvas a lo largo del tiempo. Por defecto, se muestran todas las campañas y lienzos seleccionados. Para anular la selección de una campaña o un Canvas, haz clic en el nombre de la campaña o el Canvas que deseas excluir.

Para descargar los datos de las series temporales, selecciona <i class="fas fa-bars"></i> y luego elige la opción de descarga. Las opciones disponibles son PNG, JPEG, PDF, SVG o CSV.

![Gráfico de series temporales de conversiones de dos campañas de correo electrónico, que muestra las conversiones por día.]({% image_buster /assets/img_archive/conversions2_over_time.png %})

### Métodos de atribución

| Método de atribución | Definición | Cálculo de la tasa | Opciones específicas del canal |
| --- | --- | --- | --- |
| Al llegar | Número total de conversiones que se han producido tras la recepción del mensaje | Calculado como (Conversiones únicas recibidas) / (Destinatarios únicos) | {::nomarkdown}<ul><li>Al recibir el correo electrónico</li><li>Tras la entrega del SMS</li></ul>{:/} |
| Al enviar | Número total de conversiones que se han producido tras el envío del mensaje | Calculado como (Conversiones de envíos únicos) / (Destinatarios únicos) | {::nomarkdown}<ul><li>Al pulsar enviar</li><li>Al enviar la tarjeta de contenido</li><li>Tras el envío del SMS</li></ul>{:/} |
| Al abrir | Número total de conversiones que se produjeron tras la apertura del mensaje | Calculado como (Conversiones únicas abiertas) / (Destinatarios únicos) | {::nomarkdown}<ul><li>Al abrir el correo electrónico</li><li>Al pulsar abrir</li></ul>{:/} |
| Al hacer clic | Número total de conversiones que se produjeron clic en el mensaje | Calculado como (Conversiones de clics únicos) / (Destinatarios únicos) | {::nomarkdown}<ul><li>Al hacer clic en el correo electrónico</li><li>Al hacer clic en Tarjeta de contenido</li><li>Tras hacer clic en IAM</li></ul>{:/} |
| En la impresión | Número total de conversiones que se produjeron después de una impresión | Calculado como (Conversiones de impresiones únicas) / (Destinatarios únicos) | {::nomarkdown}<ul><li>Tras la impresión de IAM</li><li>Tras la impresión de la tarjeta de contenido</li></ul>{:/} |
| En el último toque | Conversiones que dan todo el crédito al último mensaje tocado o pulsado durante la ventana de conversión. | Calculado como (Número de toques) / (Destinatarios únicos) | La atribución al último contacto se selecciona automáticamente si se añaden varios canales al informe.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Términos que debe conocer

| Plazo | Definición |
| --- | --- |
| Toque | Una interacción física o punto de contacto con un mensaje.<br><br>Los toques pueden incluir:<br>{::nomarkdown}<ul><li>Clic en correo electrónico</li><li>Apertura de notificaciones push</li><li>Clic en tarjeta de contenido</li><li>Clic en mensaje dentro de la aplicación</li><li>SMS Clic</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Solución de problemas

### ¿Por qué tengo bajas conversiones de campaña o de Canvas?

Es posible que tus conversiones no sean tan altas como esperabas en comparación con campañas anteriores o con tus expectativas. Las conversiones son un asunto delicado, pero dependen de unas cuantas funciones sencillas de nuestra plataforma: el seguimiento de eventos y los plazos de conversión.

Para solucionar el problema, te recomendamos que compruebes el seguimiento de tus eventos y los plazos de conversión.

#### Seguimiento de eventos

Cuando una campaña desencadena un inicio de sesión o un evento personalizado, debes asegurarte de que este evento, o sesión, se produce con la frecuencia suficiente para desencadenar el mensaje. Consulta el [panel de inicio]({{site.baseurl}}/user_guide/analytics/dashboard/home_dashboard/) para ver los datos de la sesión, o tu informe de [eventos personalizado]({{site.baseurl}}/user_guide/analytics/reporting/configuring_reporting/).

#### Plazos de conversión

Para cada evento de conversión que selecciones por campaña, establece la [fecha límite]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/#creating-a-campaign-with-conversion-tracking). Esto significa que estás estableciendo un límite de tiempo dentro del cual debe producirse una conversión para que cuente en cada campaña respectiva.

Comprueba que has revisado la información sobre [las reglas de seguimiento de la conversión]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/#conversion-tracking-rules) para entender las métricas de tu campaña. Para las conversiones de usuario en Canvas, consulta [las preguntas frecuentes sobre Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/faqs/#how-are-user-conversions-tracked-in-a-canvas). 