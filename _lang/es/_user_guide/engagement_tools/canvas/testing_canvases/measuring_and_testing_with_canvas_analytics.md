---
nav_title: Análisis de Canvas
article_title: Análisis de Canvas
page_order: 2
page_type: reference
description: "Este artículo de referencia describe los distintos análisis e informes que puede aprovechar para comprender el rendimiento de su Canvas."
tool: 
  - Canvas
  - Reports
  
---

# Análisis de Canvas

> Necesitas saber si lo que estás construyendo está moviendo la aguja. Con los análisis de Canvas, puede crear una imagen completa para comprender cómo las experiencias que está creando están influyendo en sus objetivos. 

Una vez que haya creado su lienzo y lo haya activado, vaya a la página **del lienzo** y selecciónelo para abrir la página de detalles. Aquí puedes medir y probar el rendimiento de tu Canvas.

## Visión general del lienzo

La parte superior de la página **Detalles de Canvas** contiene las estadísticas principales de Canvas. Estos incluyen el número de mensajes enviados dentro del Canvas, el número total de veces que los clientes han entrado en el Canvas, cuántos han convertido y su tasa total, los ingresos generados por el Canvas y la audiencia total estimada. 

Este es un buen lugar para obtener una visión general de alto nivel para comprobar cómo está funcionando su lienzo en comparación con su objetivo.

![]({% image_buster /assets/img_archive/Journey_5.png %})

### cambios desde la última visualización

El número de actualizaciones del Canvas realizadas por otros miembros de tu equipo se sigue mediante la métrica *Cambios desde la última vez que lo viste*, en la página de resumen del Canvas. Selecciona **Cambios desde la última vez que lo viste** para ver un registro de cambios de las actualizaciones del nombre, horario, etiquetas, mensaje, audiencia, estado de aprobación o configuración de acceso del equipo de Canvas. Para cada actualización, puedes ver quién la realizó y cuándo. Puedes utilizar este registro de cambios para auditar los cambios en tus Lienzos.

## Visualización del rendimiento

A medida que se desplaza por la página de **detalles del lienzo**, puede ver el rendimiento de cada componente, por ejemplo, cuántos usuarios entraron, pasaron al siguiente paso o salieron del lienzo. 

{% alert note %}
Para el Canvas Flow, un usuario saldrá del Canvas después de entrar y recibir la carga útil del mensaje en el último paso del recorrido del usuario.
{% endalert %}

Las métricas también incluyen impresiones, destinatarios únicos, recuento de conversiones e ingresos generados. Puede hacer clic en un componente para desglosar más los datos y ver el rendimiento específico de cada canal.

![Dos ejemplos de detalles de rendimiento de los componentes de Canvas. A la izquierda se muestran los detalles de rendimiento de una ruta de usuario con un componente Canvas. A la derecha se muestran los detalles de rendimiento de un componente Canvas ampliado y un paso anidado que muestra el recuento de impresiones de mensajes dentro de la aplicación.]({% image_buster /assets/img_archive/Journey_6.png %})

## Desglose del rendimiento por variante

En la parte inferior de la página **Detalles del lienzo**, haga clic en **Analizar variantes** para abrir el modal **Analizar lienzo**. Este modal contiene tres pestañas: 

- Analizar variantes
- Informe de embudo de Canvas
- Informe de retención de Canvas

### Analizar variantes

En la pestaña **Analizar variantes**, puede ver un desglose del rendimiento por variante y grupo de control, si tiene más de una. También puede copiar el identificador API de Canvas, descargar un archivo CSV de las métricas y copiar las celdas. La pestaña **Analizar variantes** contiene una tabla que le muestra un desglose de cada variante a varios niveles. 

Puedes deducir rápidamente variantes eficaces e identificar las cadencias, contenidos, desencadenantes, tiempos adecuados y mucho más.

![]({% image_buster /assets/img_archive/analyze_variants.png %})

Las métricas básicas son las siguientes:  

- **Identificador API de variantes:** El identificador API de su variante, que puede utilizar en sus llamadas API.
- **Total de entradas:** El número total de usuarios que han entrado en la variante Canvas.
- **Total de envíos:** El número total de mensajes enviados en la variante Canvas.
- **Pasos totales:** El número total de pasos en la variante Canvas.
- **Ingresos totales:** Los ingresos totales en dólares de los destinatarios de Canvas dentro de la ventana de conversión primaria establecida.

{% alert note %}
Al igual que las conversiones, los ingresos se rastrean técnicamente en el nivel Canvas, pero se atribuyen al componente más reciente y a la variante más reciente de la que el usuario ha recibido un mensaje (o ha entrado, si aún no ha recibido un mensaje).<br><br>
Por ejemplo, si un usuario completa dos pasos y luego realiza una compra, ese ingreso se atribuye al segundo componente, y a la variante que introdujo. Si entran en el Canvas pero realizan una compra antes de recibir el primer componente del Canvas, esos ingresos se atribuyen a la variante en la que entraron, pero no a ningún componente.
{% endalert %}

Además, puede ver un desglose más explícito de los [eventos de conversión]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/), entre los que se incluyen los siguientes:

- Totales y tasas de conversión para cada evento de conversión
- Elevación frente a la variante de control
- Confianza estadística para cada evento de conversión

### Informe de embudo

Los informes de embudo ofrecen un informe visual que le permite analizar los recorridos que realizan sus clientes después de recibir un Canvas. Si su Canvas utiliza un grupo de control o múltiples variantes, podrá comprender cómo las diferentes variantes han impactado en el embudo de conversión a un nivel más granular y optimizar en base a estos datos. Para más información sobre los informes de embudo, consulta [Informes de embudo]({{site.baseurl}}/user_guide/analytics/reporting/funnel_reports/).

### Informe de retención

La retención de usuarios es una de las métricas más importantes para cualquier profesional del marketing. Mantener a los usuarios comprometidos volviendo a por más indica que el negocio va viento en popa. Braze ahora le permite medir la retención de usuarios directamente en la página **de Canvas Analytics**. Para más información sobre cómo leer e interpretar su informe de retención, consulte [Informes de retención]({{site.baseurl}}/user_guide/analytics/reporting/retention_reports/).

