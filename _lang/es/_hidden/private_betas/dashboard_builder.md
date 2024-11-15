---
nav_title: Generador de dashboards
article_title: Generador de dashboards
permalink: "/dashboard_builder/"
description: "Este artículo de referencia explica cómo utilizar el Generador de paneles para crear paneles y visualizaciones utilizando informes creados en el Generador de consultas."
page_type: reference
hidden: true
---

# Generador de dashboards

> Utiliza el Generador de paneles para crear paneles y visualizaciones utilizando los informes creados en el Generador de consultas. Puedes empezar con las plantillas de consultas SQL prediseñadas del Generador de consultas o escribir tus propias consultas SQL personalizadas para obtener aún más información.

Braze proporciona plantillas de paneles preconstruidas para casos de uso frecuente, como el análisis de los ingresos mediante la atribución de último toque. Ten en cuenta que la posibilidad de editar un panel de plantilla aún no está disponible.

{% alert note %}
El Creador de paneles está actualmente en acceso anticipado. Ponte en contacto con tu administrador del éxito del cliente si estás interesado en participar en este acceso anticipado.
{% endalert %}

## Ejecutar una plantilla de panel de control

1. Ve a **Análisis** > **Generador de paneles**. La página de inicio enumera todos los paneles existentes en tu espacio de trabajo, con las plantillas creadas por Braze en la parte superior. Se indican con "(Braze)" en el título.
2. Selecciona el panel que te interese.
3. Selecciona **Ejecutar panel** para generar un panel utilizando esa plantilla.

### Plantillas de paneles disponibles

#### Ingresos - Atribución de última intervención

La plantilla **Ingresos - Atribución al último toque** proporciona una revisión de los ingresos en todas las campañas, lienzos y canales. Todos los datos de ingresos se atribuyen al último mensaje tocado durante la ventana de atribución.

Los toques incluyen `Email Click`, `Content Card Click`, `In-App Message Click`, `SMS Delivery`, `WhatsApp Read` y `Webhook Send`.

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

## Crear un panel personalizado

1. Selecciona **Crear panel** o un panel existente y **Editar**. A continuación, selecciona **\+ Añadir baldosa**.
2. Selecciona **Seleccionar consulta existente** y elige una consulta que hayas ejecutado en el Generador de consultas.
3. Para editar cómo se muestran los resultados de la consulta en el mosaico, selecciona el icono del lápiz para cambiar el título y el tipo de gráfico.<br><br>![Vista de edición de mosaicos con opciones para cambiar el título y el tipo de gráfico.][2]{: style="max-width:60%;"}<br><br>
    - Si seleccionas un tipo de gráfico de **Columna**, **Barra** o **Línea**:
        - Selecciona un campo de la consulta para utilizarlo como eje X.
        - Deselecciona las columnas que no te interesen.<br><br>![Desplegable con los tipos de gráficos.][1]{: style="max-width:40%;"}

{: start="4"}        
4\. Asegúrate de guardar los cambios. Si quieres borrar el mosaico, selecciona el icono de la papelera. Los mosaicos borrados no pueden revertirse y deben volver a crearse.
5\. Ajusta el tamaño del mosaico arrastrando el controlador de la esquina inferior derecha, y la posición del mosaico en el panel arrastrando el controlador de la esquina superior derecha.<br><br>![Mosaico arrastrando el controlador.][3]<br><br>
6\. Añade mosaicos adicionales hasta completar tu panel.
7\. Selecciona **Ver panel** y, a continuación, **Ejecutar panel**. Tu panel puede tardar unos minutos en terminar de generar informes.

## Comparte tu opinión con nosotros

No dudes en compartir tu opinión con nosotros poniéndote en contacto con tu administrador del éxito del cliente o respondiendo al correo electrónico de habilitación que has recibido.

[1]: {% image_buster /assets/img/chart_type.png %}
[2]: {% image_buster /assets/img/sample_tile.png %}
[3]: {% image_buster /assets/img/drag_tile.png %}
