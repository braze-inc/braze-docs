---
nav_title: Generador de dashboards
article_title: Generador de dashboards
alias: "/dashboard_builder/"
description: "Este artículo de referencia explica cómo utilizar el Generador de paneles para crear paneles y visualizaciones utilizando informes creados en el Generador de consultas."
page_type: reference
tool:
    - Reports
page_order: 6.1
---

# Generador de dashboards

> Utiliza Dashboard Builder para crear paneles y visualizaciones utilizando informes creados en el generador de informes Report Builder o en Query Builder.

Dashboard Builder te permite crear y visualizar paneles de análisis personalizados desde cero y a partir de los paneles proporcionados por Braze. Puedes utilizar un origen de datos sin código (generador de informes) o un origen de datos SQL (Query Builder) para alimentar tu panel de control, o bien empezar desde uno de los muchos paneles proporcionados por Braze.

## Creación de un panel personalizado

1. Ve a **Análisis** > **Generador de paneles**.
2. Selecciona **Crear panel**.
3. Selecciona el origen de datos que alimentará tus informes:
- **Informes** creados en el generador de informes.
- **Consultas personalizadas** creadas en el Generador de consultas<br><br>![Ventana para seleccionar el origen de datos para tu panel.]({% image_buster /assets/img/select_data_source.png %})<br><br>

Ahora, sigue los pasos correspondientes a tu origen de datos:

{% tabs %}
{% tab Reports %}

{: start="4"}
4\. Selecciona **\+ Añadir mosaico** y, a continuación, elige uno de los informes que has creado en [el generador de informes (Nuevo)]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/).

{% alert important %}
Después de añadir un informe del generador de informes a un mosaico de Dashboard Builder, el mosaico no se conecta al informe original. Si editas el informe original en el generador de informes, debes eliminar el mosaico del panel existente y crear uno nuevo utilizando el informe actualizado como origen de datos.
{% endalert %}

{: start="5"}
5\. Selecciona el icono del lápiz para cambiar la forma en que se muestran el título y el tipo de gráfico en el mosaico.
    \- Puedes alternar entre diferentes tipos de gráficos debajo de la visualización predeterminada. Las opciones actuales incluyen gráficos de barras (horizontales o verticales) y gráficos de líneas (solo disponibles si has seleccionado **Fecha** como opción de desglose en la configuración del generador de informes).<br><br>![Alternar entre diferentes tipos de gráficos.]({% image_buster /assets/img/report_builder_types.png %})<br><br>
    \- Utiliza el menú desplegable de métricas para seleccionar qué métricas incluir en tu visualización. De forma predeterminada, la primera columna del informe será la métrica mostrada predeterminada.
6\. Selecciona **Guardar** después de haber cambiado la visualización a tu gusto.
7\. Añade un nombre, una descripción y una etiqueta para que tu panel sea más fácil de encontrar más adelante.
{% endtab %}
{% tab Custom Queries %}
{: start="4"}
4\. Selecciona **\+ Añadir mosaico** y, a continuación, elige una consulta que hayas ejecutado en el Generador de consultas.
5\. Para editar cómo se muestran los resultados de la consulta en el mosaico, selecciona el icono del lápiz para cambiar el título y el tipo de gráfico.
    \- Puedes alternar entre diferentes tipos de gráficos debajo de la visualización predeterminada. Las opciones actuales incluyen tablas, gráficos de barras (horizontales o verticales) y gráficos de líneas.<br><br>![Alternar entre diferentes tipos de gráficos.]({% image_buster /assets/img/query_builder_types.png %})<br><br>
        \- Si eliges una de las opciones de gráfico, utiliza el menú desplegable **del eje X** para seleccionar una sola columna de los resultados de la consulta que se utilizará como eje X.
        \- Utiliza el menú desplegable **del eje Y** para seleccionar las métricas que deseas incluir en tu visualización. De forma predeterminada, se mostrarán todas las columnas de los resultados de la consulta, por lo que debes deseleccionar las columnas que no te interesen.<br><br>![Alternar entre diferentes tipos de gráficos.]({% image_buster /assets/img/query_builder_axis.png %})<br><br>
        \- (Opcional) Puedes utilizar el menú desplegable **Agrupación** para agrupar los resultados de la consulta. Por ejemplo, si tienes el ID de campaña como resultado de una columna y deseas sumar todas las filas con ese valor, utiliza el menú desplegable **Agrupación**.  
        \- (Opcional) Para editar los datos que se muestran, selecciona la consulta adjunta al elemento visual y realiza las modificaciones en [el Generador de consultas]({{site.baseurl}}/user_guide/analytics/query_builder/).
6\. Selecciona **Guardar** después de haber cambiado la visualización a tu gusto.
7\. Añade un nombre, una descripción y una etiqueta para que tu panel sea más fácil de encontrar más adelante.
{% endtab %}
{% endtabs %}

{: start="8"}
8\. Repite los pasos 4 a 7 para tu método respectivo hasta crear el panel que desees.
9\. Selecciona **Ver panel de control** > selecciona **Ejecutar panel de control**. 

Tu panel puede tardar unos minutos en terminar de generar los informes.

{% alert note %}
Puedes añadir hasta 10 mosaicos a un panel.
{% endalert %}

## Administrar mosaicos del panel de control

### Eliminar mosaicos

Eliminar un mosaico del panel seleccionando **Eliminar mosaico** en la parte inferior del mosaico. **Esta acción no se puede revertir.**

### Azulejos duplicados

Haz una copia de tu mosaico seleccionando **Duplicar mosaico** en la parte inferior del mosaico.

### Adjustar el tamaño y la posición de los mosaicos

Ajusta el tamaño del mosaico arrastrando la esquina inferior derecha del mismo y ajusta la posición del mosaico en el panel arrastrando el controlador situado en la esquina superior derecha del mosaico.

## Ejecutar un panel

1. Ve a **Análisis** > **Generador de paneles**. La página de inicio muestra todos los paneles existentes en tu espacio de trabajo, con los paneles creados por Braze en la parte superior. Se indican con "(Braze)" en el título.
2. Selecciona el panel que te interese.
3. Selecciona **Ejecutar panel** para cargar el panel correspondiente utilizando ese panel.

### Paneles disponibles

Braze ofrece paneles predefinidos para casos de uso frecuentes, como el análisis de ingresos mediante la atribución de último contacto. Ten en cuenta que la función para editar un panel aún no está disponible. Ponte en contacto con tu administrador del éxito del cliente si deseas ver algún panel en el futuro.

#### Ingresos - Atribución de última intervención

El panel de control **«Ingresos: atribución al último contacto»** ofrece una visión general de los ingresos de todas las campañas, lienzos y canales. Todos los datos de ingresos se atribuyen al último mensaje tocado durante la ventana de atribución.

Las interacciones incluyen _clics en correos electrónicos_ (clics en enlaces), _clics en tarjetas de contenido_, _clics en mensajes dentro de la aplicación_ (excluyendo los botones de cierre), _aperturas de notificaciones push_, _clics en enlaces cortos de SMS_, _lecturas de WhatsApp_ y _envíos de webhooks_.

| Métrica | Definición |
| --- | --- |
| Total de ingresos de último contacto | Suma de todos los eventos de ingresos de campaña y Canvas con un evento de último toque dentro del intervalo de fechas y la ventana de atribución seleccionados. |
| Conversiones totales de compra | Un recuento de todos los eventos de ingresos de campaña y Canvas con un evento de último contacto cualificado. |
| Días promedio para la conversión | El tiempo medio entre todos los eventos de compra de campaña y Canvas con un evento de último toque cualificado. |
| Ingresos por destinatario | Suma de los ingresos procedentes de eventos de ingresos cualificados dividida por el número de usuarios únicos que recibieron un mensaje dentro del intervalo de fechas. |
| Compradores únicos | Recuento de los usuarios únicos con un evento de ingresos cualificado. |
| Ingresos por país | Suma de todos los eventos de ingresos de campaña y Canvas con un evento de último toque, agrupados por país. |
| Ingresos por campaña | Suma de todos los eventos de ingresos de campaña y Canvas con un evento de último contacto cualificado, agrupados por campaña. |
| Ingresos por variante de campaña | Suma de todos los eventos de ingresos de campaña y Canvas con un evento de último contacto que cumpla los requisitos, agrupados por variante de campaña. |
| Ingresos por Canvas | Suma de todos los eventos de ingresos de campaña y Canvas con un evento de último contacto que cumpla los requisitos, agrupados por Canvas. |
| Ingresos por variante en Canvas | Suma de todos los eventos de ingresos de campaña y Canvas con un evento de último contacto que cumpla los requisitos, agrupados por variante en Canvas. |
| Compras por producto | Recuento de todas las compras agrupadas por producto. |
| Ingresos por canal | Suma de todos los eventos de ingresos de campaña y Canvas con un evento de último contacto cualificado, agrupados por canal. | 
| Series temporales de ingresos | Suma de todos los eventos de ingresos de campaña y Canvas con un evento de último contacto que cumpla los requisitos, agrupados por día en UTC. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Dispositivos y operadores

| Métrica | Definición |
| --- | --- |
| Operadores de dispositivos | Recuento de usuarios en el intervalo de fechas seleccionado que abrieron una notificación push, agrupados por operador del dispositivo. |
| Modelo del dispositivo | Recuento de usuarios en el intervalo de fechas seleccionado que abrieron una notificación push, agrupados por modelo de dispositivo. |
| Sistema operativo del dispositivo | Recuento de usuarios en el intervalo de fechas seleccionado que abrieron una notificación push, agrupados por sistema operativo del dispositivo. |
| Tamaño de la pantalla del dispositivo | Recuento de usuarios en el intervalo de fechas seleccionado que abrieron una notificación push, agrupados por resolución de pantalla del dispositivo (tamaño). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Información del segmento: correo electrónico

| Métrica  | Definición  |
|---|---|
| Métricas semanales de correo electrónico (tasas) | Tasas de interacción con el correo electrónico (entrega, rebote, apertura, clics, tasa de cancelación de suscripciones) agrupadas por segmento y mostradas como series temporales semanales.|
| Métricas semanales de correo electrónico (recursos) | Recuento de interacciones con el correo electrónico (enviados, entregados, rebotados, abiertos, clics, cancelaciones de suscripción) agrupados por segmento y mostrados como series temporales semanales.|
| Métricas de compra semanales (tasas) | Tasa de conversión de compras (ingresos por destinatario) a partir de aperturas y clics en correos electrónicos, agrupadas por segmento y mostradas como una serie temporal semanal.|
| Métricas de compra semanales (recuentos) | Recuento de compras e ingresos totales por aperturas y clics en correos electrónicos, agrupados por segmento y mostrados como una serie temporal semanal.|
| Interacción con el correo electrónico por segmento | Tabla resumen que muestra las métricas totales de interacción con el correo electrónico (enviados, entregados, rebotados, abiertos, clics, bajas y sus respectivas tasas) agregadas por segmento.|
| Compras&  Ingresos por segmento | Tabla resumen que muestra las métricas totales de compra (compras, ingresos e ingresos por destinatario) a partir de las aperturas y los clics de los correos electrónicos, agregadas por segmento.|
| Las 10 mejores campañas en cuanto a métricas de interacción | Lista clasificada de campañas con las métricas de interacción por correo electrónico más altas (métrica configurable para la clasificación).|
| Las 10 campañas con peores métricas de interacción | Lista clasificada de campañas con las métricas de interacción por correo electrónico más bajas (métrica configurable para la clasificación).|
| Las 10 mejores lienzos para métricas de interacción | Lista clasificada de lienzos con las métricas de interacción por correo electrónico más altas (métrica configurable para la clasificación).|
| Las 10 peores lienzos para las métricas de interacción | Lista clasificada de lienzos con las métricas de interacción por correo electrónico más bajas (métrica configurable para la clasificación).|
| Las 10 mejores campañas para métricas de compra | Lista clasificada de campañas con las métricas de conversión de compra más altas a partir de la interacción con el correo electrónico (métrica configurable para la clasificación).|
| Las 10 peores campañas en cuanto a métricas de compra | Lista clasificada de campañas con las métricas de conversión de compra más bajas a partir de la interacción con el correo electrónico (métrica configurable para la clasificación).|
| Las 10 mejores lienzos para métricas de compra | Lista clasificada de lienzos con las métricas de conversión de compra más altas a partir de la interacción con el correo electrónico (métrica configurable para la clasificación).|
| Las 10 lienzos menos vendidos Métricas de compra | Lista clasificada de lienzos con las métricas de conversión de compra más bajas a partir de la interacción con el correo electrónico (métrica configurable para la clasificación).|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Análisis de sesiones

| Métrica | Definición  |
|---|---|
| Número de sesiones por día (serie temporal) | Recuento de sesiones únicas agrupadas por día dentro del intervalo de fechas seleccionado, mostradas como una serie temporal.|
| Promedio de sesiones por usuario | La cantidad de sesiones por usuario se calcula como el total de sesiones dividido por los usuarios únicos dentro del intervalo de fechas seleccionado.|
| Las campañas se convierten en sesiones | Recuento de sesiones únicas que se produjeron al mismo tiempo que las conversiones de la campaña, agrupadas por ID de campaña y clasificadas por número de sesiones.|
| Los lienzos se convierten en sesiones | Recuento de sesiones únicas que se produjeron al mismo tiempo que las conversiones de Canvas, agrupadas por ID de Canvas y clasificadas por número de sesiones.|
| Número total de sesiones por usuario | Lista de los 1000 usuarios principales según su recuento total de sesiones dentro del intervalo de fechas seleccionado.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Comparte tu opinión con nosotros

Selecciona el botón **Enviar comentarios** o ponte en contacto con tu administrador del éxito del cliente para compartir tus comentarios con nosotros.

