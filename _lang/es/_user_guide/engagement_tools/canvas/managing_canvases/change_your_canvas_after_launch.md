---
nav_title: Editar lienzos después del lanzamiento
article_title: Editar lienzos después del lanzamiento
page_order: 0
description: "Este artículo de referencia cubre los distintos aspectos de un Canvas que pueden modificarse tras el lanzamiento inicial."
alias: "/post-launch_edits/"
page_type: reference
tool:
  - Canvas

---

# Editar lienzos después del lanzamiento

> Este artículo de referencia trata de lo que se puede cambiar en un Canvas después del lanzamiento inicial.

Puedes editar tus Lienzos después del lanzamiento:

* Insertar nuevos pasos en Canvas en el recorrido del usuario
* Añadir nuevas variantes y conexiones
* Ajustar la distribución de variantes
* Detener o reanudar todos los pasos en Canvas

{% alert note %}
La distribución de variantes de control sólo puede disminuir después del lanzamiento.
{% endalert %}

Ten en cuenta las siguientes ediciones permitidas tras el lanzamiento del Canvas, dependiendo del flujo de trabajo con el que se haya creado tu Canvas. Si tu Canvas utiliza el flujo de trabajo original de Canvas, tendrás que clonarlo primero en el Flujo de Canvas para poder realizar ediciones posteriores al lanzamiento.

Puedes eliminar cualquiera de los siguientes elementos de tu recorrido de usuario:

- [Pasos en Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/about/)
- Variantes en Canvas 
- Conexiones entre pasos en Canvas

Si quieres editar o añadir más pasos a tu recorrido de usuario de Canvas, se aplicarán los siguientes detalles:

- Los usuarios que aún no hayan entrado en el Canvas son elegibles para cualquier paso recién creado. 
- Si tu configuración de entrada en Canvas permite a los usuarios volver a entrar en los pasos, los usuarios que ya hayan superado los pasos recién creados serán elegibles para volver a entrar.
- Los usuarios que están actualmente en un Canvas lanzado, pero que no han alcanzado los puntos del recorrido del usuario en los que se añaden nuevos pasos, son elegibles para recibir esos nuevos pasos añadidos. 

Si eliminas un paso de [Retraso]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/) o de [Rutas de acción]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/), opcionalmente puedes redirigir a los usuarios que estén esperando en ese paso a otro paso de Canvas. Para los Retrasos, los usuarios permanecerán en el paso hasta el final del periodo de retraso. En el caso de las Rutas de acción, los usuarios permanecerán en el paso hasta el final de la ventana de evaluación.

Ten en cuenta que cuando lanzas un Canvas inicialmente, Braze pone en cola a los usuarios para el paso en Mensaje en el que se encuentran, no para todos los mensajes posteriores en el Canvas. Si realizas una edición en el Canvas después del lanzamiento, algunos usuarios ya estarán en cola y no recogerán los cambios. Si detienes el Canvas, lo duplicas, luego lo modificas y lanzas esta nueva versión, el Canvas volverá a evaluar a todos los usuarios de nuevo, no sólo a los usuarios que aún no se hayan puesto en cola.

Consulta la sección ["Buenas prácticas](#best-practices) " para conocer casos de uso específicos de la edición. En general, es una buena práctica evitar editar Lienzos en vivo, ya que puede haber comportamientos inesperados.

{% details Expand for original Canvas editor details %}

No puedes editar o borrar conexiones existentes, y no puedes insertar un paso entre pasos conectados existentes. Si quieres editar o añadir más pasos a tu recorrido de usuario de Canvas, se aplicarán los siguientes detalles:

- Los usuarios que aún no hayan entrado en el Canvas son elegibles para cualquier paso recién creado. 
- Si tu configuración de entrada en Canvas permite a los usuarios volver a entrar en los pasos, los usuarios que ya hayan superado los pasos recién creados serán elegibles para volver a entrar.
- Los usuarios que están actualmente en un Canvas lanzado, pero que no han alcanzado los pasos recién añadidos en el recorrido del usuario, son elegibles para recibir esos pasos recién añadidos.
- Si un paso de Retraso es el último paso del Canvas, los usuarios que alcancen ese paso avanzarán automáticamente fuera del Canvas y no recibirán ningún paso recién creado.

{% alert important %}
Si actualizas la configuración de **Retraso** o **Ventana** de un paso en Canvas, los usuarios que se encuentren en ese paso en el momento de la actualización respetarán el tiempo de retraso que se les asignó cuando entraron en él. Sólo los nuevos usuarios que entren en el Canvas y los que aún no se hayan puesto en cola para ese paso recibirán el mensaje en el momento actualizado.
{% endalert %}

Al detener un Canvas no saldrán los usuarios que estén esperando recibir un mensaje. Si vuelves a habilitar el Canvas y los usuarios siguen esperando el mensaje, lo recibirán (a menos que haya pasado el tiempo en que se les debería haber enviado el mensaje, entonces no lo recibirán).

{% enddetails %}

## Detalles del Canvas

Puedes editar las siguientes configuraciones e información del Canvas después de iniciar un Canvas:

* Nombre y descripción del Canvas
* Equipos y etiquetas
* Tipo de entrada, horario y controles
* Estado de la suscripción
* Límite de velocidad
* Limitación de frecuencia
* Horas tranquilas
* Audiencia objetivo

Después de lanzar un Canvas:

- Los eventos de conversión no se pueden editar. 
- Los siguientes pasos no se pueden añadir ni eliminar, y no se pueden reordenar para ajustar la clasificación: Rutas [de audiencia]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths/), [rutas de acción]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/) y [rutas de experimentos]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/).
  - **Solución 1:** Crea una nueva Ruta de audiencia, Ruta de acción o Ruta de experimentos y reconfigura las rutas hacia ese nuevo paso.
  - **Solución 2:** Duplica el Canvas para hacer tus ediciones.

### Pasos individuales

Para los pasos en Canvas individuales, puedes editar los siguientes detalles después del lanzamiento:

* Nombre
* Contenido del mensaje
* Desencadenantes
* Audiencia
* Eventos de excepción
* Retrasos

Sin embargo, el tipo de programación y los porcentajes de control del paso no son editables tras el lanzamiento. Para los pasos de rutas de acción y rutas de audiencia, las clasificaciones no son editables tras el lanzamiento.

### Porcentajes de variantes en Canvas

Después de lanzar un Canvas, sólo puedes disminuir los porcentajes de la variante de control. Si se modifica el porcentaje de una variante en Canvas, verás que tus usuarios pueden redistribuirse a otras variantes.

Inicialmente, a estos usuarios se les asigna aleatoriamente una variante concreta antes de recibir una campaña por primera vez. A partir de ese momento, cada vez que reciba la campaña (o que el usuario vuelva a entrar en una variante de Canvas), recibirá la misma variante, a menos que se modifiquen los porcentajes de la variante.

Si cambian los porcentajes de variantes, los usuarios pueden ser redistribuidos a otras variantes. Los usuarios permanecerán en estas variantes hasta que se vuelvan a modificar los porcentajes. Ten en cuenta que en los Canvas que utilicen filtrar con filtros `NOT` con números de contenedor aleatorios, es posible que los usuarios no reciban la misma rama cada vez en su recorrido de usuario cuando vuelvan a entrar en el Canvas.

#### Grupos de control

Los grupos de control siguen siendo coherentes si el porcentaje de variantes no varía. Si se disminuye o aumenta el porcentaje de un grupo de control, los usuarios que anteriormente recibieron mensajes no podrían entrar en el grupo de control en un envío posterior, ni ningún usuario del grupo de control recibiría nunca un mensaje.

### Hora de envío local

Los lienzos programados para lanzarse a una hora de envío local pueden editarse hasta 24 horas antes de la hora de envío programada. Esta ventana se denomina "zona segura". 

{% alert tip %}
Si pretendes hacer ediciones más amplias que lleven a crear una nueva copia del Canvas por completo, recuerda excluir a los usuarios que recibieron el primer Canvas y reajustar las horas de programación del Canvas para tener en cuenta el envío por zona horaria.
{% endalert %}

### Borrar variantes

Cuando se eliminan variantes de un Canvas, ocurre lo siguiente:

- Se eliminarán los pasos dentro de la variante (incluidos los compartidos por otras variantes). 
- Se eliminarán los análisis por pasos y los análisis de nivel superior del Canvas, como el _Total de entradas_, el _Total de salidas_ y la _Tasa de conversión_.
- Los usuarios de las variantes eliminadas salen de los pasos y no se envían los mensajes siguientes.

### Propiedades de entrada en Canvas

Las propiedades de entrada en Canvas no están plantillas en los pasos cuando se envían. Esto significa que cuando se editen las propiedades de entrada al Canvas después de que se haya lanzado el Canvas, estos cambios sólo se aplicarán a los nuevos usuarios que entren en el Canvas. Si tu Canvas permite que los usuarios vuelvan a entrar en él, los usuarios que vuelvan a entrar estarán determinados por las propiedades de entrada al Canvas actualizadas.

## Buenas prácticas

Echa un vistazo a estas prácticas recomendadas que debes tener en cuenta cuando edites o añadas algo a tu Canvas después de haberlo lanzado.

{% alert important %}
En general, evita hacer cambios mientras el Canvas esté activo y poniendo usuarios en cola.
{% endalert %}

### Pasos desconectados

Puedes lanzar tu Canvas con pasos desconectados y también guardar estos Canvas después del lanzamiento. Antes de desconectar un paso de tu flujo de trabajo, te recomendamos que compruebes la vista de análisis de los pasos para usuarios pendientes.

Supongamos que un usuario se encuentra en un paso desconectado de tu flujo de trabajo Canvas. Este usuario avanzará al paso siguiente si lo hay. La configuración del paso dictará cómo debe avanzar el usuario. 

Al crear o editar pasos desconectados, puedes hacer cambios en estos pasos independientes sin tener que conectarlos directamente al resto de tu Canvas. Esto te ayudará a probar tus pasos antes de volver a lanzar tu Canvas. 

### Paso de ruta de experimentos

Si tu Canvas tiene un experimento de ruta ganadora o de ruta personalizada activo o en curso y actualizas el Canvas activo, independientemente de si actualizas el propio paso de ruta de experimentos, el experimento en curso finalizará y el paso de experimentos no determinará una ruta ganadora o rutas personalizadas. Para reiniciar el experimento, puedes desconectar la Ruta de experimentos existente y lanzar una nueva, o duplicar el Canvas y lanzar un nuevo Canvas. De lo contrario, los usuarios fluirán por la ruta de experimentos como si no se hubiera seleccionado ningún método de optimización.

### Retrasos temporales

¡Editar Lienzos con retrasos puede ser un poco complicado! Por tanto, ten en cuenta los siguientes detalles cuando edites tus Lienzos.

Si actualizas el retraso en un paso de Retraso o ventana de evaluación en el paso Rutas de acción, sólo los nuevos usuarios que entren en el Canvas y los usuarios que no hayan estado en cola para ese paso recibirán el mensaje con el retraso actualizado.

Si eliminas un paso con una demora de tiempo (como Retraso o Rutas de acción) y decides redirigir a esos usuarios a otro paso en Canvas, los usuarios sólo serán redirigidos una vez que se haya completado la demora de tiempo del paso. Por ejemplo, supongamos que eliminas un paso Retraso con un retraso de un día y rediriges a esos usuarios a un paso Mensaje. En este caso, los usuarios sólo serán redirigidos una vez transcurrido el plazo de un día.

Si tu Canvas tiene uno o más pasos de rutas de experimentos, eliminar pasos podría invalidar los resultados de este paso.

### Lienzos de parada

Al detener un Canvas no saldrán los usuarios que estén esperando en un paso. Si vuelves a habilitar el Canvas y los usuarios siguen esperando, completarán el paso y pasarán al siguiente. Sin embargo, si ha pasado el tiempo en el que el usuario debería haber avanzado al siguiente paso, saldrá del Canvas. 

Por ejemplo, supongamos que tienes un Canvas creado mediante el flujo de trabajo Flujo de Canvas configurado para lanzarse a las 14:00 con una variante con dos pasos: un paso Retraso con una hora de retraso que va a un paso Mensaje. 

Un usuario entra en este Canvas a las 14:01 y entra en el paso de Retraso al mismo tiempo. Esto significa que se programará que el usuario pase al siguiente paso del recorrido del usuario (el paso Mensaje) a las 15:01. Si detienes el Canvas a las 14:30 y vuelves a habilitarlo a las 15:30, el usuario saldrá del Canvas ya que son más de las 15:01. Sin embargo, si vuelves a habilitar el Canvas a las 14:40 h, el usuario pasará al paso en Mensaje como estaba previsto a las 15:01 h.

## Lo que debes saber

Los siguientes problemas comunes pueden desencadenarse al editar o añadir más componentes a cualquier otro componente de un Canvas después de iniciarlo. 

{% alert important %}
Los siguientes problemas son evitables. Si necesitas editar un Canvas después de que se haya lanzado, te recomendamos que primero confirmes que todos los usuarios que ya han entrado en el Canvas han completado su recorrido de usuario. Además, te sugerimos que no elimines pasos que ya hayan procesado al menos a un usuario.
{% endalert %}

- Faltan datos de notificación (cuando se borran y se vuelven a añadir variantes de mensajes)
- Los usuarios no siguen el camino esperado
- Los mensajes se envían en momentos inesperados
- Las ediciones no sobrescriben los datos de Currents, por lo que puedes notar discrepancias entre los pasos en Canvas (como `canvas_step_ids` que no existe en el Canvas debido a una eliminación).
- Los usuarios pueden recibir dos veces el mismo mensaje
- Se interrumpe la recepción de mensajes por parte de los usuarios debido al límite de velocidad existente
  - Cuando se envían usuarios a un Canvas, se aplica al usuario el límite de velocidad aplicado al Canvas cuando se envía un usuario. Una vez enviado el Canvas, el límite de velocidad no se puede editar para ese usuario, por lo que aumentar o disminuir el límite de velocidad después del lanzamiento no afectará a los usuarios que ya hayan sido enviados.