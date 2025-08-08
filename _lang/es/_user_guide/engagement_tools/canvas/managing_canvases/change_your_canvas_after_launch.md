---
nav_title: Editar lienzos después del lanzamiento
article_title: Editar lienzos después del lanzamiento
page_order: 0
description: "Este artículo de referencia cubre los diferentes aspectos de un Canvas que pueden modificarse tras el lanzamiento inicial."
alias: "/post-launch_edits/"
page_type: reference
tool:
  - Canvas

---

# Edición de lienzos tras el lanzamiento

> Este artículo de referencia cubre lo que se puede cambiar en un Canvas después del lanzamiento inicial.

Puedes editar tus Lienzos después del lanzamiento:

* Insertar nuevos pasos en Canvas en el recorrido del usuario
* Añadir nuevas variantes y conexiones
* Ajuste de la distribución de variantes
* Detener o reanudar todos los pasos del lienzo

{% alert note %}
La distribución de la variante de control sólo puede reducirse después del lanzamiento.
{% endalert %}

Ten en cuenta las siguientes ediciones permitidas tras el lanzamiento del Canvas, dependiendo del flujo de trabajo con el que se haya creado tu Canvas. Si tu Canvas utiliza el flujo de trabajo original de Canvas, tendrás que clonarlo primero en Canvas Flow para poder realizar ediciones posteriores al lanzamiento.

Puedes eliminar cualquiera de los siguientes elementos de tu recorrido de usuario:

- [Pasos en Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/about/)
- Variantes de Canvas 
- Conexiones entre pasos en Canvas

Si desea editar o añadir más pasos a su recorrido de usuario de Canvas, se aplicarán los siguientes detalles:

- Los usuarios que aún no hayan entrado en el Lienzo podrán acceder a los pasos recién creados. 
- Si tu configuración de entrada en Canvas permite a los usuarios volver a entrar en los pasos, los usuarios que ya hayan superado pasos recién creados serán elegibles para volver a entrar.
- Los usuarios que están actualmente en un Canvas lanzado, pero que no han alcanzado los puntos del recorrido del usuario en los que se añaden nuevos pasos, pueden recibir esos nuevos pasos añadidos. 

Si elimina un paso de [Retraso]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/) o [Rutas de acción]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/), puede redirigir opcionalmente a los usuarios que están esperando actualmente en el paso a otro paso de Canvas. Para los Retrasos, los usuarios permanecerán en el paso hasta el final del periodo de retraso. En el caso de las Rutas de Acción, los usuarios permanecerán en el paso hasta el final de la ventana de evaluación.

Tenga en cuenta que cuando lanza un lienzo inicialmente, Braze pone en cola a los usuarios para el paso de mensaje en el que se encuentran, no para todos los mensajes posteriores del lienzo. Si realiza una edición en el lienzo después del lanzamiento, algunos usuarios ya estarán en cola y no recogerán los cambios. Si detiene el lienzo, lo duplica, lo modifica y lanza esta nueva versión, el lienzo volverá a evaluar a todos los usuarios, no sólo a los que aún no se han puesto en cola.

Consulte la sección [Prácticas recomendadas](#best-practices) para conocer los casos de uso específicos de la edición. En general, es una buena práctica evitar editar Canvas en vivo, ya que puede producirse un comportamiento inesperado.

{% details Editor de lienzos original %}

{% alert important %}
A partir del 28 de febrero de 2023, ya no podrás crear o duplicar Lienzos utilizando la experiencia Canvas original. Braze recomienda a los clientes que utilicen la experiencia Canvas original que se pasen a Canvas Flow. Es una experiencia de edición mejorada para construir y gestionar mejor los lienzos. Más información sobre la [clonación de tus lienzos en el flujo de lienzos]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/cloning_canvases/).
{% endalert %}

No puedes editar o borrar conexiones existentes, y no puedes insertar un paso entre pasos conectados existentes. Si desea editar o añadir más pasos a su recorrido de usuario de Canvas, se aplicarán los siguientes detalles:

- Los usuarios que aún no hayan entrado en el Lienzo podrán acceder a los pasos recién creados. 
- Si tu configuración de entrada en Canvas permite a los usuarios volver a entrar en los pasos, los usuarios que ya hayan superado pasos recién creados serán elegibles para volver a entrar.
- Los usuarios que están actualmente en un Canvas lanzado, pero que no han alcanzado los nuevos pasos añadidos en el recorrido del usuario, pueden recibir esos nuevos pasos añadidos.
- Si un paso de Retraso es el último paso del lienzo, los usuarios que lleguen a ese paso saldrán automáticamente del lienzo y no recibirán ningún paso recién creado.

{% alert important %}
Si actualizas la configuración de **Retraso** o **Ventana** de un paso en Canvas, los usuarios que se encuentren en ese paso en el momento de la actualización respetarán el tiempo de retraso que se les asignó cuando entraron en él. Sólo los nuevos usuarios que entren en el Canvas y los que aún no se hayan puesto en cola para ese paso recibirán el mensaje en el momento actualizado.
{% endalert %}

Al detener un Canvas no saldrán los usuarios que estén esperando recibir un mensaje. Si vuelves a activar el Canvas y los usuarios siguen esperando el mensaje, lo recibirán (a menos que haya pasado el tiempo en el que se les debería haber enviado el mensaje, entonces no lo recibirán).

{% enddetails %}

## Detalles del lienzo

Puedes editar las siguientes configuraciones e información del Canvas después de iniciar un Canvas:

* Nombre y descripción del lienzo
* Equipos y etiquetas
* Tipo de entrada, horario y controles
* Estado de la suscripción
* Limitación de velocidad
* Limitación de frecuencia
* Horas tranquilas
* Audiencia objetivo

Después de lanzar un Canvas:

- Los eventos de conversión no se pueden editar. 
- Los siguientes pasos no se pueden añadir ni eliminar, y no se pueden reordenar para ajustar la clasificación: [Rutas de audiencia]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths/), [rutas de acción]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/) y [rutas de experimentos]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/).
  - **Solución:** Crea una nueva Ruta de audiencia, Ruta de acción o Ruta de experimentos y reconfigura las rutas hacia ese nuevo paso.
  - **Solución 2:** Duplica el Canvas para hacer tus ediciones.

### Pasos individuales

Para los pasos individuales de Canvas, puede editar los siguientes detalles después del lanzamiento:

* Apellidos
* Contenido del mensaje
* Activadores
* Audiencia
* Eventos de excepción
* Retrasos

Sin embargo, el tipo de programación del paso y los porcentajes de control no son editables después del lanzamiento. Para los pasos de Rutas de acción y Rutas de audiencia, las clasificaciones no son editables después del lanzamiento.

### Porcentajes de variantes del lienzo

Después de lanzar un lienzo, sólo puede disminuir los porcentajes de variantes de control. Si se modifica el porcentaje de una variante en Canvas, descubrirá que sus usuarios pueden redistribuirse a otras variantes.

Inicialmente, a estos usuarios se les asigna aleatoriamente una variante concreta antes de recibir una campaña por primera vez. A partir de ese momento, cada vez que se reciba la campaña sucesivamente (o el usuario vuelva a entrar en una variante de Canvas), recibirá la misma variante a menos que se modifiquen los porcentajes de la variante.

Si los porcentajes de variantes cambian, los usuarios pueden redistribuirse a otras variantes. Los usuarios permanecerán en estas variantes hasta que se vuelvan a modificar los porcentajes. Tenga en cuenta que para los lienzos que utilizan la ramificación con filtros `NOT` con números de cubo aleatorios, es posible que los usuarios no reciban la misma ramificación cada vez en su recorrido de usuario cuando vuelvan a entrar en el lienzo.

#### Grupos de control

Los grupos de control siguen siendo coherentes si el porcentaje de variantes no varía. Si se disminuye o aumenta el porcentaje de un grupo de control, los usuarios que antes recibían mensajes no podrían entrar en el grupo de control en un envío posterior, ni ningún usuario del grupo de control recibiría nunca un mensaje.

### Hora de envío local

Los Canvas programados para lanzarse a una hora de envío local pueden editarse hasta 24 horas antes de la hora de envío programada. Esta ventana se denomina "zona segura". 

{% alert tip %}
Si tiene intención de realizar ediciones más extensas que conlleven la creación de una nueva copia completa del lienzo, recuerde excluir a los usuarios que recibieron el primer lienzo y reajustar las horas de programación del lienzo para tener en cuenta el envío por zona horaria.
{% endalert %}

### Borrar variantes

Cuando se eliminan variantes de un Canvas, ocurre lo siguiente:

- Se eliminarán los pasos dentro de la variante (incluidos los compartidos por otras variantes). 
- Se eliminarán los análisis por pasos y los análisis de nivel superior del Canvas, como el _Total de entradas_, el _Total de salidas_ y la _Tasa de conversión_.
- Los usuarios de las variantes eliminadas salen de los pasos y no se envían los mensajes siguientes.

### Propiedades de entrada del lienzo

Las propiedades de entrada en Canvas no están plantillas en los pasos cuando se envían. Esto significa que cuando se editen las propiedades de entrada al Canvas después de que se haya lanzado el Canvas, estos cambios sólo se aplicarán a los nuevos usuarios que entren en el Canvas. Si tu Canvas permite que los usuarios vuelvan a entrar en él, los usuarios que vuelvan a entrar estarán determinados por las propiedades de entrada al Canvas actualizadas.

## Buenas prácticas

Echa un vistazo a estas prácticas recomendadas que debes tener en cuenta cuando edites o añadas algo a tu Canvas después de haberlo lanzado.

### Pasos desconectados

Puedes lanzar tu Canvas con pasos desconectados y también guardar estos Canvases post-lanzamiento. Antes de desconectar un paso de su flujo de trabajo, le recomendamos que compruebe la vista analítica de los pasos para los usuarios pendientes.

Supongamos que un usuario se encuentra en un paso desconectado de su flujo de trabajo Canvas. Este usuario avanzará al paso siguiente si lo hubiera. La configuración del paso dictará cómo debe avanzar el usuario. 

Al crear o editar pasos desconectados, puede realizar cambios en estos pasos independientes sin tener que conectarlos directamente al resto de su Lienzo. Esto te ayudará a probar tus pasos antes de volver a lanzar tu Canvas. 

### Paso de ruta de experimentos

Si tu Canvas tiene un experimento activo o en curso y actualizas el Canvas activo (aunque no sea al paso de Ruta de experimentos), el experimento en curso finalizará. Para reiniciar el experimento, puedes desconectar la Ruta de experimentos existente y lanzar una nueva, o duplicar el Canvas y lanzar un nuevo Canvas.

### Retrasos temporales

Editar Canvas con retrasos temporales puede ser un poco complicado. Por lo tanto, tenga en cuenta los siguientes detalles cuando edite sus lienzos.

Si actualiza el retraso en un paso de Retraso o ventana de evaluación en el paso Vías de acción, sólo los nuevos usuarios que entren en el lienzo y los usuarios que no se hayan puesto en cola para ese paso recibirán el mensaje con el tiempo de retraso actualizado.

Si elimina un paso con temporización (como Retraso o Rutas de acción) y decide redirigir a esos usuarios a otro paso de Canvas, los usuarios sólo serán redirigidos una vez finalizada la temporización del paso. Por ejemplo, supongamos que elimina un paso de Retraso con un retraso de un día y redirige a esos usuarios a un paso de Mensaje. En este caso, los usuarios sólo serán redirigidos una vez transcurrido el plazo de un día.

Si tu Canvas tiene uno o más pasos de rutas de experimentos, eliminar pasos podría invalidar los resultados de este paso.

### Detener Canvas

Al detener un Canvas no saldrán los usuarios que estén esperando en un paso. Si vuelve a activar el Lienzo y los usuarios siguen esperando, completarán el paso y pasarán al siguiente. Sin embargo, si el tiempo en el que el usuario debería haber avanzado al siguiente paso ha pasado, en su lugar saldrá del Canvas. 

Por ejemplo, supongamos que tiene un lienzo creado con el flujo de trabajo Flujo de lienzos configurado para lanzarse a las 14:00 con una variante con dos pasos: un paso Retraso con un retraso de una hora que va a un paso Mensaje. 

Un usuario entra en este Canvas a las 14:01 y entra en el paso de Retraso al mismo tiempo. Esto significa que se programará que el usuario pase al siguiente paso del recorrido del usuario (el paso Mensaje) a las 15:01. Si detienes el Canvas a las 2:30 pm y vuelves a activarlo a las 3:30 pm, el usuario saldrá del Canvas ya que son más de las 3:01 pm. Sin embargo, si vuelves a habilitar el Canvas a las 14:40 h, el usuario pasará al paso en Mensaje como estaba previsto a las 15:01 h.
