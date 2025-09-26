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

> Utiliza el Generador de informes para crear paneles y visualizaciones utilizando informes creados en el Generador de informes o en el Generador de consultas.

Dashboard Builder te permite componer y visualizar paneles de análisis personalizados desde cero y a partir de plantillas suministradas por Braze. Puedes utilizar un origen de datos sin código (Generador de informes) o un origen de datos SQL (Generador de consultas) para potenciar tu panel, o partir de una de las muchas plantillas Braze.

## Crear un panel personalizado

1. Ve a **Análisis** > **Generador de paneles**.
2. Selecciona **Crear panel**.
3. Selecciona qué origen de datos alimentará tus informes:
- **Informes** creados con el Generador de informes
- **Consultas personalizadas** creadas en el Generador de consultas<br><br>![Ventana para seleccionar el origen de datos para tu panel.]({% image_buster /assets/img/select_data_source.png %})<br><br>

Ahora, sigue los pasos correspondientes a tu origen de datos:

{% tabs %}
{% tab Informes %}

{: start="4"}
4\. Selecciona **\+ Añadir ficha** y, a continuación, elige uno de los informes que creaste en [el Generador de informes (Nuevo)]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/).
5\. Selecciona el icono del lápiz para cambiar cómo se muestran el título y el tipo de gráfico en el mosaico.
    \- Puedes alternar entre distintos tipos de gráficos por debajo de la visualización predeterminada. Las opciones actuales incluyen gráficos de barras (horizontales o verticales) y gráficos de líneas (sólo disponibles si seleccionaste **Fecha** como opción de desglose en la configuración del Generador de informes).<br><br>![Alterna entre distintos tipos de gráficos.]({% image_buster /assets/img/report_builder_types.png %})<br><br>
    \- Utiliza el desplegable de métricas para seleccionar qué métricas quieres incluir en tu visualización. Por defecto, la primera columna del informe será la métrica mostrada por defecto.
6\. Selecciona **Guardar** cuando hayas modificado la visualización a tu gusto.
7\. Añade un nombre, una descripción y una etiqueta para que sea más fácil encontrar tu panel más adelante.
{% endtab %}
{% tab Consultas personalizadas %}
{: start="4"}
4\. Selecciona **\+ Añadir ficha** y, a continuación, elige una consulta que hayas ejecutado en el Generador de consultas.
5\. Para editar cómo se muestran los resultados de la consulta en el mosaico, selecciona el icono del lápiz para cambiar el título y el tipo de gráfico.
    \- Puedes alternar entre distintos tipos de gráficos por debajo de la visualización predeterminada. Las opciones actuales incluyen tablas, gráficos de barras (horizontales o verticales) y gráficos de líneas.<br><br>![Alterna entre distintos tipos de gráficos.]({% image_buster /assets/img/query_builder_types.png %})<br><br>
        \- Si eliges una de las opciones de gráfico, utiliza el desplegable **Eje X** para seleccionar una sola columna de los resultados de tu consulta para utilizarla como eje x.
        \- Utiliza el desplegable **del eje Y** para seleccionar las métricas que quieres incluir en tu visualización. Por predeterminado, se mostrarán todas las columnas de los resultados de tu consulta, así que deselecciona las columnas que no te interese ver.<br><br>![Alterna entre distintos tipos de gráficos.]({% image_buster /assets/img/query_builder_axis.png %})<br><br>
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

Adjust the tile size by dragging the bottom right corner of the tile, and adjust the tile position on the panel by dragging the handle at the top right corner of the tile.

## Ejecutar una plantilla de panel de control

1. Ve a **Análisis** > **Generador de paneles**. La página de inicio enumera todos los paneles existentes en tu espacio de trabajo, con las plantillas creadas por Braze en la parte superior. Se indican con "(Braze)" en el título.
2. Selecciona el panel que te interese.
3. Selecciona **Ejecutar panel** para cargar el panel correspondiente utilizando esa plantilla.

### Plantillas de paneles disponibles

Braze proporciona plantillas de paneles preconstruidas para casos de uso frecuente, como el análisis de los ingresos mediante la atribución de último toque. Ten en cuenta que la posibilidad de editar un panel de plantilla aún no está disponible. Ponte en contacto con tu administrador del éxito del cliente si deseas ver determinadas plantillas de paneles en futuras versiones de plantillas.

#### Ingresos - Atribución de última intervención

La plantilla **Ingresos - Atribución al último toque** proporciona una revisión de los ingresos en todas las campañas, lienzos y canales. Todos los datos de ingresos se atribuyen al último mensaje tocado durante la ventana de atribución.

Los toques incluyen _clic de correo electrónico_, _clic de tarjeta de contenido_, _clic de mensaje dentro de la aplicación_, _clic de enlace corto de SMS_, _lectura de WhatsApp_ y _envío de webhook_.

| Métricas | Definición |
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

| Métricas | Definición |
| --- | --- |
| Operadores de dispositivos | Recuento de usuarios en el intervalo de fechas seleccionado que abrieron una notificación push, agrupados por operador del dispositivo. |
| Modelo del dispositivo | Recuento de usuarios en el intervalo de fechas seleccionado que abrieron una notificación push, agrupados por modelo de dispositivo. |
| Sistema operativo del dispositivo | Recuento de usuarios en el intervalo de fechas seleccionado que abrieron una notificación push, agrupados por sistema operativo del dispositivo. |
| Tamaño de la pantalla del dispositivo | Recuento de usuarios en el intervalo de fechas seleccionado que abrieron una notificación push, agrupados por resolución de pantalla del dispositivo (tamaño). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Comparte tu opinión con nosotros

Selecciona el botón **Enviar opinión** o ponte en contacto con tu administrador del éxito del cliente para compartir tu opinión con nosotros.

