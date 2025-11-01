---
nav_title: Análisis de Canvas
article_title: Análisis de Canvas
page_order: 2
page_type: reference
description: "Este artículo de referencia describe los distintos análisis e informes que puedes aprovechar para comprender el rendimiento de tu Canvas."
tool: 
  - Canvas
  - Reports
  
---

# Análisis de Canvas

> Necesitas saber si lo que estás construyendo está moviendo la aguja. Con los análisis de Canvas, puedes construir una imagen completa para comprender cómo las experiencias que estás construyendo están repercutiendo en tus objetivos. 

Una vez que hayas creado tu Canvas y lo hayas puesto en vivo, ve a la página **de Canvas** y selecciona tu Canvas para abrir la página de detalles. Aquí puedes medir y probar el rendimiento de tu Canvas.

## Resumen de Canvas

La parte superior de la página **Detalles del Canvas** contiene las estadísticas principales del Canvas. Estos incluyen el número de mensajes enviados dentro del Canvas, el número total de veces que los clientes han entrado en el Canvas, cuántos se han convertido y su tasa total, los ingresos generados por el Canvas y la audiencia total estimada. 

Este es un buen lugar para obtener un resumen de alto nivel para comprobar cómo está rindiendo tu Canvas en relación con tu objetivo.

\![]({% image_buster /assets/img_archive/Journey_5.png %})

### Cambios desde la última visita

El número de actualizaciones del Canvas realizadas por otros miembros de tu equipo se sigue mediante la métrica *Cambios desde la última vez que lo viste*, en la página de resumen del Canvas. Selecciona **Cambios desde la última vez que lo viste** para ver un registro de cambios de las actualizaciones del nombre, horario, etiquetas, mensaje, audiencia, estado de aprobación o configuración de acceso del equipo de Canvas. Para cada actualización, puedes ver quién la realizó y cuándo. Puedes utilizar este registro de cambios para auditar los cambios en tus Lienzos.

## Visualización del rendimiento

A medida que te desplazas por la página **de Detalles del** Canvas, puedes ver el rendimiento de cada componente, como cuántos usuarios entraron, pasaron al siguiente paso o salieron del Canvas. 

{% alert note %}
En el caso del Flujo Canvas, un usuario saldrá del Canvas después de entrar y recibir la carga útil del mensaje en el último paso del recorrido del usuario.
{% endalert %}

Las métricas también incluyen impresiones, destinatarios únicos, recuento de conversiones e ingresos generados. Puedes hacer clic en un componente para desglosar más los datos y ver el rendimiento específico de cada canal.

\![Dos ejemplos de detalles de rendimiento de los componentes de Canvas. A la izquierda se muestran los detalles de rendimiento de una ruta de usuario con un componente Canvas. A la derecha se muestran los detalles de rendimiento de un componente Canvas ampliado y un paso anidado que muestra el recuento de impresiones de mensajes dentro de la aplicación.]({% image_buster /assets/img_archive/Journey_6.png %})

## Desglose del rendimiento por variante

En la parte inferior de la página **Detalles del Canvas**, haz clic en **Analizar variantes** para abrir el modal **Analizar Canvas**. Este modal contiene tres pestañas: 

- Analizar variantes
- Informe de embudo Canvas
- Informe de retención en Canvas

### Analizar variantes

En la pestaña **Analizar variantes**, puedes ver un desglose del rendimiento por variante y grupo de control, si tienes más de uno. También puedes copiar el identificador de la API de Canvas, descargar un archivo CSV de las métricas y copiar las celdas. La pestaña **Analizar variantes** contiene una tabla que te muestra un desglose de cada variante en varios niveles. 

Puedes deducir rápidamente variantes eficaces e identificar las cadencias, contenidos, desencadenantes, tiempos y mucho más adecuados.

\![]({% image_buster /assets/img_archive/analyze_variants.png %})

Las métricas básicas son las siguientes:  

- **Identificador de variante de la API:** El identificador API de tu variante, que puedes utilizar en tus llamadas a la API.
- **Total de entradas:** El número total de usuarios que han entrado en la variante en Canvas.
- **Total de envíos:** El número total de mensajes enviados en la variante en Canvas.
- **Pasos totales:** El número total de pasos en la variante en Canvas.
- **Ingresos totales:** Los ingresos totales en dólares de los destinatarios de Canvas dentro de la ventana de conversión primaria establecida.

{% alert note %}
Al igual que las conversiones, los ingresos se siguen técnicamente a nivel de Canvas, pero se atribuyen al componente más reciente y a la variante más reciente de la que el usuario ha recibido un mensaje (o ha entrado, si aún no ha recibido un mensaje).<br><br>
Por ejemplo, si un usuario completa dos pasos y luego realiza una compra, esos ingresos se atribuyen al segundo componente, y a la variante que introdujo. Si entran en el Canvas pero realizan una compra antes de recibir el primer componente del Canvas, esos ingresos se atribuyen a la variante en la que entraron, pero no a ningún componente.
{% endalert %}

Además, puedes ver un desglose más explícito de los [eventos de conversión]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/), entre los que se incluyen los siguientes:

- Totales y tasas de conversión de cada evento de conversión
- Elevación frente a la variante de control
- Confianza estadística para cada evento de conversión

### Cómo se realiza el seguimiento de las conversiones 

Un usuario sólo puede convertir una vez por evento de conversión por entrada en Canvas. Las conversiones se asignan al mensaje más reciente recibido por el usuario para esa entrada. El resumen de Canvas refleja todas las conversiones realizadas por los usuarios en esa ruta y si recibieron o no un mensaje. Cada paso posterior sólo mostrará las conversiones que se produjeron mientras ese fue el paso más reciente que recibió el usuario. 

Considera el siguiente ejemplo: un Canvas tiene 10 notificaciones push y el evento de conversión es "Abre aplicación" (o "Inicio de sesión").
- El usuario A abre la aplicación después de entrar, pero antes de recibir el primer mensaje.
- El usuario B abre la aplicación después de cada notificación push.

El resumen de Canvas mostrará dos conversiones, mientras que los pasos individuales mostrarán una conversión en el primer paso y ninguna en todos los pasos siguientes. Si las horas tranquilas están activas cuando se produce el evento de conversión, se aplicarán las mismas reglas. 

Supongamos que tenemos un Canvas con Horas tranquilas y se producen los siguientes eventos:

1. El usuario A entra en un Canvas.
2. El primer paso es un Retraso dentro de las Horas tranquilas establecidas, por lo que el mensaje se suprime.
3. El usuario A realiza el evento de conversión.

El usuario A contará como convertido en la variante en Canvas general, pero no el paso, ya que no recibió el paso.

Para nuestro último ejemplo, supongamos que tenemos un Canvas con la re-elegibilidad activada. Si un usuario que vuelve a ser elegible realiza el evento de conversión en la primera entrada y en la segunda, se contarán dos conversiones.

### Informe de embudo

El informe de embudo ofrece un informe visual que te permite analizar los recorridos que realizan tus clientes tras recibir un Canvas. Si tu Canvas utiliza un grupo de control o múltiples variantes, podrás comprender cómo las diferentes variantes han impactado en el embudo de conversión a un nivel más granular y optimizar en base a estos datos. Para más información sobre los informes de embudo, consulta [Informes de embudo]({{site.baseurl}}/user_guide/analytics/reporting/funnel_reports/).

### Informe de retención

La retención de usuarios es una de las métricas más importantes para cualquier especialista en marketing. Mantener a los usuarios comprometidos volviendo a por más indica que el negocio va viento en popa. Braze te permite ahora medir la retención de usuarios directamente en la página **de análisis de Canvas**. Para más información sobre cómo leer e interpretar tu informe de retención, consulta [Informes de retención]({{site.baseurl}}/user_guide/analytics/reporting/retention_reports/).

