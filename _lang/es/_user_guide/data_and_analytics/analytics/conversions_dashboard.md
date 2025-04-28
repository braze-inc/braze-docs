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
5. (opcional) Selecciona una capa de **Desglose** para ver diferentes dimensiones de los datos, como por variante, paso en Canvas, país o idioma.
6. (opcional) Si quieres calcular las conversiones de un evento que no se configuró como evento de conversión en la campaña o Canvas, activa [Usar eventos personalizados](#using-custom-events).
7. Selecciona un [método de atribución](#attribution-methods) para analizar los mensajes seleccionados.

{% alert note %}
Si estás analizando conversiones de varios canales, tu **Método de atribución** será, por defecto, **la Atribución de último contacto**.
{% endalert %}

{:start="8"}
8\. Selecciona **Crear** para ejecutar el informe.

Tras cargar la página, selecciona un **Evento de conversión** para filtrar el informe en busca de datos de conversión. Las selecciones disponibles incluirán los eventos preconfigurados en los lienzos y campañas. Si seleccionaste un evento personalizado al configurar tu informe (paso 6), esta opción no estará disponible.

### Uso de eventos personalizados

Para calcular las conversiones de un evento que no se configuró como evento de conversión en la campaña o Canvas, selecciona un evento personalizado específico para utilizarlo como evento de conversión. 

1. Cuando configure su informe, active **Usar eventos personalizados**.
2. Selecciona un evento personalizado para utilizarlo como evento de conversión.
3. Seleccione la ventana de conversión dentro de la cual debería haberse producido ese evento para que se contabilice como conversión.

{% alert note %}
Si seleccionas un evento personalizado, no verás el desplegable **Evento de conversión** en la página y tendrás que volver a ejecutar el informe para ver las conversiones de diferentes eventos personalizados.
{% endalert %}

## Comprender tu informe

El informe se divide en tres secciones:

- [Detalles de la conversión](#conversion-details)
- [Embudo de conversión](#conversion-funnel)
- [Conversiones a lo largo del tiempo](#conversions-over-time)

### Detalles de la conversión

La tabla de detalles de conversión siempre muestra una columna para *Destinatarios* y otra para *Conversiones* (tasa y total). Las otras dos columnas de la tabla que aparecen dependen de las opciones seleccionadas al configurar el informe. La siguiente tabla describe las métricas posibles.

| Métrica indicada | Descripción |
| --- | --- |
| Destinatarios | El número de usuarios que recibieron un mensaje a través del canal seleccionado dentro del intervalo de fechas del informe. |
| Tasa de conversión (destinatarios) | Calculada como: (Número de conversiones) / (Número de destinatarios) |
| Método de atribución | Definido por el [método de atribución](#attribution-methods) que seleccionaste al configurar el informe. Para la atribución de Último Toque o si se seleccionan varios canales, aparece como [Toques](#terms-to-know). |
| Tasa de conversión (método de atribución) | Definido por el [método de atribución](#attribution-methods) que seleccionaste al configurar el informe. Si se seleccionan varios canales, el atributo predeterminado es el de última pulsación. |
{: .reset-td-br-1 .reset-td-br-2 }

![]({% image_buster /assets/img_archive/conversions2_details.png %})

Si seleccionaste detalles a nivel de desglose para campañas o Lienzos al [configurar tu informe](#setting-up-your-report) (paso 5), puedes hacer clic en <i class="fas fa-angle-down"></i> para ampliar la tabla.

### Embudo de conversión

Este gráfico de barras muestra los recuentos absolutos de cada [evento de compromiso]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events) en función del canal seleccionado. El recuento de conversiones se definirá según el método de atribución seleccionado.

Por defecto, se muestran todas las campañas y lienzos seleccionados. Para anular la selección de una campaña o Canvas, selecciona el nombre de la campaña o Canvas que quieras excluir. Para obtener más detalles sobre el acto de compromiso, puede pasar el ratón por encima de cada barra.

Para descargar los datos de las series temporales, selecciona una opción de descarga: PNG, JPEG, PDF, SVG o CSV.

{% alert note %}
Este gráfico sólo muestra los datos de un canal cada vez. Utilice el menú desplegable **Canal** del gráfico para seleccionar un único canal.
{% endalert %}

![]({% image_buster /assets/img_archive/conversions2_funnel.png %}){: style="max-width:70%"}

### Conversiones a lo largo del tiempo

Este gráfico de series temporales incluye una representación de las conversiones por campaña o Canvas a lo largo del tiempo. Por defecto, se muestran todas las campañas y lienzos seleccionados. Para anular la selección de una campaña o un Canvas, haz clic en el nombre de la campaña o el Canvas que deseas excluir.

Para descargar los datos de las series temporales, selecciona <i class="fas fa-bars"></i> y luego elige la opción de descarga. Las opciones disponibles son PNG, JPEG, PDF, SVG o CSV.

![]({% image_buster /assets/img_archive/conversions2_over_time.png %}){: style="max-width:70%"}

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
| Toque | Una interacción física o punto de contacto con un mensaje.<br><br>Los toques pueden incluir:<br>{::nomarkdown}<ul><li>Clic en correo electrónico</li><li>Apertura de notificaciones push</li><li>Clic en tarjeta de contenido</li><li>Clic en mensaje dentro de la aplicación</li><li>Entrega de SMS</li></ul>{:/} |
