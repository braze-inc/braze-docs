---
nav_title: Constructor de paneles
article_title: Constructor de paneles
alias: "/dashboard_builder/"
description: "Este artículo de referencia explica cómo utilizar el Generador de paneles para crear paneles y visualizaciones utilizando informes creados en el Generador de consultas."
page_type: reference
tool:
    - Reports
page_order: 6.1
---

# Constructor de paneles

> Utiliza el Generador de informes para crear paneles y visualizaciones utilizando informes creados en el Generador de informes o en el Generador de consultas.

Dashboard Builder te permite componer y visualizar paneles de análisis personalizados desde cero y a partir de paneles suministrados por Braze. Puedes utilizar un origen de datos sin código (Generador de informes) o un origen de datos SQL (Generador de consultas) para potenciar tu panel, o partir de uno de los muchos paneles suministrados por Braze.

## Crear un panel personalizado

1. Ve a **Análisis** > **Generador de paneles**.
2. Selecciona **Crear panel**.
3. Selecciona qué origen de datos alimentará tus informes:
- **Informes** creados con el Generador de informes
- **Consultas personalizadas** creadas en el Generador de consultas<br><br>Ventana para seleccionar el origen de datos de tu panel.]({% image_buster /assets/img/select_data_source.png %})<br><br>

Ahora, sigue los pasos correspondientes a tu origen de datos:

{% tabs %}
{% tab Reports %}

{: start="4"}
4\. Selecciona **\+ Añadir ficha** y, a continuación, elige uno de los informes que creaste en [el Generador de informes (Nuevo)]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/).
5\. Selecciona el icono del lápiz para cambiar cómo se muestran el título y el tipo de gráfico en el mosaico.
    \- Puedes alternar entre distintos tipos de gráficos por debajo de la visualización predeterminada. Las opciones actuales incluyen gráficos de barras (horizontales o verticales) y gráficos de líneas (sólo disponibles si seleccionaste **Fecha** como opción de desglose en la configuración del Generador de informes).<br><br>Alterna diferentes tipos de gráficos.]({% image_buster /assets/img/report_builder_types.png %})<br><br>
    \- Utiliza el desplegable de métricas para seleccionar qué métricas quieres incluir en tu visualización. Por defecto, la primera columna del informe será la métrica mostrada por defecto.
6\. Selecciona **Guardar** cuando hayas modificado la visualización a tu gusto.
7\. Añade un nombre, una descripción y una etiqueta para que sea más fácil encontrar tu panel más adelante.
{% endtab %}
{% tab Custom Queries %}
{: start="4"}
4\. Selecciona **\+ Añadir ficha** y, a continuación, elige una consulta que hayas ejecutado en el Generador de consultas.
5\. Para editar cómo se muestran los resultados de la consulta en el mosaico, selecciona el icono del lápiz para cambiar el título y el tipo de gráfico.
    \- Puedes alternar entre distintos tipos de gráficos por debajo de la visualización predeterminada. Las opciones actuales incluyen tablas, gráficos de barras (horizontales o verticales) y gráficos de líneas.<br><br>Alterna diferentes tipos de gráficos.]({% image_buster /assets/img/query_builder_types.png %})<br><br>
        \- Si eliges una de las opciones de gráfico, utiliza el desplegable **Eje X** para seleccionar una sola columna de los resultados de tu consulta para utilizarla como eje x.
        \- Utiliza el desplegable **del eje Y** para seleccionar las métricas que quieres incluir en tu visualización. Por predeterminado, se mostrarán todas las columnas de los resultados de tu consulta, así que deselecciona las columnas que no te interese ver.<br><br>Alterna diferentes tipos de gráficos.]({% image_buster /assets/img/query_builder_axis.png %})<br><br>
        \- (Opcional) Puedes utilizar el desplegable **Agrupación** para agrupar los resultados de tu consulta. Por ejemplo, si tienes el ID de campaña como resultado de una columna y quieres sumar todas las filas con ese valor, utiliza el desplegable **Agrupar**.  
        \- (Opcional) Para editar los datos que se muestran, selecciona la consulta adjunta al visual y edítala en [el Generador de consultas]({{site.baseurl}}/user_guide/analytics/query_builder/).
6\. Selecciona **Guardar** cuando hayas modificado la visualización a tu gusto.
7\. Añade un nombre, una descripción y una etiqueta para que sea más fácil encontrar tu panel más adelante.
{% endtab %}
{% endtabs %}

{: start="8"}
8\. Repite los pasos 4-7 para tu método respectivo hasta crear el panel que desees.
9\. Selecciona **Ver panel** > selecciona **Ejecutar panel**. 

Tu panel puede tardar unos minutos en terminar de generar informes.

{% alert note %}
Puedes añadir hasta 10 mosaicos a un panel.
{% endalert %}

## Administrar los mosaicos del panel de control

### Borrar baldosas

Elimina un mosaico del panel de control seleccionando **Eliminar mosaico** en la parte inferior del mosaico. **Esta acción no se puede revertir.**

### Baldosas duplicadas

Haz una copia de tu ficha seleccionando **Duplicar ficha** en la parte inferior de la ficha.

### Ajusta el tamaño y la posición de las baldosas

Adjust the tile size by dragging the bottom-right corner of the tile, and adjust the tile position on the panel by dragging the handle at the top right corner of the tile.

## Ejecutar un panel de control

1. Ve a **Análisis** > **Generador de paneles**. La página de inicio enumera todos los paneles existentes en tu espacio de trabajo, con los paneles creados por Braze en la parte superior. Se indican con "(Braze)" en el título.
2. Selecciona el panel que te interese.
3. Selecciona **Ejecutar panel** para cargar el panel correspondiente utilizando ese panel.

### Paneles disponibles

Braze proporciona paneles preconstruidos para casos de uso frecuente, como el análisis de los ingresos mediante la atribución de último toque. Nota que la posibilidad de editar un panel aún no está disponible. Ponte en contacto con tu administrador del éxito del cliente si quieres ver un panel determinado en el futuro.

#### Ingresos - Atribución Último Toque

El panel **Ingresos - Atribución de último toque** proporciona una revisión de los ingresos en campañas, Canvases y canales. Todos los datos de ingresos se atribuyen al último mensaje tocado durante la ventana de atribución.

Los toques incluyen _Clic de correo electrónico_ (clic de enlace), _Clic de tarjeta de contenido_, _Clic de mensaje dentro de la aplicación_ (excluyendo los botones de cierre), _Apertura push_, _Clic de enlace corto de SMS_, _Lectura de WhatsApp_ y _Envío de webhook_.

| Métrica | Definición |
| --- | --- |
| Total Ingresos Último Toque | Suma de todos los eventos de ingresos de campaña y Canvas con un evento de último toque dentro del intervalo de fechas y la ventana de atribución seleccionados. |
| Conversiones totales de compra | Un recuento de todos los eventos de ingresos de campaña y Canvas con un evento de último contacto cualificado. |
| Días medios para la conversión | El tiempo medio entre todos los eventos de compra de campaña y Canvas con un evento de último toque cualificado. |
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
| Modelo de dispositivo | Recuento de usuarios en el intervalo de fechas seleccionado que abrieron una notificación push, agrupados por modelo de dispositivo. |
| Sistema operativo del dispositivo | Recuento de usuarios en el intervalo de fechas seleccionado que abrieron una notificación push, agrupados por sistema operativo del dispositivo. |
| Tamaño de la pantalla del dispositivo | Recuento de usuarios en el intervalo de fechas seleccionado que abrieron una notificación push, agrupados por resolución de pantalla del dispositivo (tamaño). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Información del segmento - Correo electrónico

| Métrica  | Definición  |
|---|---|
| Métricas semanales de correo electrónico (tasas) | Tasas de interacción por correo electrónico (tasas de entrega, rebote, apertura, clic, cancelación suscripción) agrupadas por segmentos y mostradas como series temporales semanales.|
| Métricas semanales de correo electrónico (recuentos) | Recuentos de interacción con el correo electrónico (envíos, entregas, rebotes, aperturas, clics, cancelaciones de suscripción) agrupados por segmentos y mostrados como series temporales semanales.|
| Métricas semanales de compra (tasas) | Tasas de conversión de compras (ingresos por destinatario) a partir de aperturas y clics de correo electrónico, agrupadas por segmentos y mostradas como una serie temporal semanal.|
| Métricas semanales de compra (recuentos) | Recuentos de compras y totales de ingresos de aperturas y clics de correo electrónico, agrupados por segmento y mostrados como una serie temporal semanal.|
| Interacción por correo electrónico por segmento | Tabla resumen que muestra las métricas totales de interacción del correo electrónico (enviados, entregados, rebotes, aperturas, clics, cancelaciones de suscripción y sus tasas) agregadas por segmento.|
| Compras & Ingresos por segmento | Tabla resumen que muestra las métricas de compra totales (compras, ingresos e ingresos por destinatario) de aperturas y clics de correo electrónico, agregadas por segmento.|
| Las 10 mejores campañas en cuanto a métricas de interacción | Lista clasificada de campañas con las métricas de interacción por correo electrónico más altas (métrica configurable para la clasificación).|
| Las 10 campañas con las métricas de interacción más bajas | Lista ordenada de las campañas con las métricas de interacción por correo electrónico más bajas (métrica configurable para la clasificación).|
| Los 10 mejores lienzos para las métricas de interacción | Lista ordenada de las Lienzos con las métricas de interacción por correo electrónico más altas (métrica configurable para la clasificación).|
| Los 10 lienzos más bajos para las métricas de interacción | Lista ordenada de las Lienzos con las métricas de interacción por correo electrónico más bajas (métrica configurable para la clasificación).|
| Las 10 mejores campañas en métricas de compra | Lista clasificada de las campañas con las métricas de conversión de compra más altas a partir de la interacción por correo electrónico (métrica configurable para la clasificación).|
| Las 10 campañas con las métricas de compra más bajas | Lista clasificada de las campañas con las métricas de conversión de compra más bajas a partir de la interacción por correo electrónico (métrica configurable para la clasificación).|
| Los 10 mejores lienzos para métricas de compra | Lista clasificada de Lienzos con las métricas de conversión de compra más altas a partir de la interacción por correo electrónico (métrica configurable para la clasificación).|
| Los 10 lienzos más bajos para las métricas de compra | Lista ordenada de las Lonas con las métricas de conversión de compra más bajas a partir de la interacción por correo electrónico (métrica configurable para la clasificación).|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Análisis de sesión

| Métrica | Definición  |
|---|---|
| \# Nº de sesiones por día (serie temporal) | Recuento de sesiones únicas agrupadas por día dentro del intervalo de fechas seleccionado, mostrado como una serie temporal.|
| Nº medio de sesiones por usuario | Cantidad media de sesiones por usuario calculada como el total de sesiones dividido por los usuarios únicos dentro del intervalo de fechas seleccionado.|
| Las campañas se convierten en sesiones | Recuento de sesiones únicas que se produjeron al mismo tiempo que las conversiones de campaña, agrupadas por ID de campaña y clasificadas por recuento de sesiones.|
| Los lienzos se convierten en sesiones | Recuento de sesiones únicas que se produjeron al mismo tiempo que las conversiones de Canvas, agrupadas por ID de Canvas y clasificadas por recuento de sesiones.|
| Nº total de sesiones por usuario | Lista de los 1.000 usuarios principales por su número total de sesiones dentro del intervalo de fechas seleccionado.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Comparte tu opinión con nosotros

Selecciona el botón **Enviar opinión** o ponte en contacto con tu administrador del éxito del cliente para compartir tu opinión con nosotros.

