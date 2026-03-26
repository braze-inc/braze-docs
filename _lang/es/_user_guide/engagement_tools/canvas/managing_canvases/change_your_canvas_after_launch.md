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

# Editar lienzos después del lanzamiento

> Este artículo de referencia cubre lo que se puede cambiar en un Canvas después del lanzamiento inicial.

Puedes editar tus Lienzos después del lanzamiento:

* Insertar nuevos pasos en Canvas en el recorrido del usuario
* Añadir nuevas variantes y conexiones
* Ajuste de la distribución de variantes
* Detener o reanudar todos los pasos del lienzo

{% alert note %}
La distribución de la variante de control sólo puede reducirse después del lanzamiento.
{% endalert %}

Puedes eliminar cualquiera de los siguientes elementos de tu recorrido de usuario:

- [Pasos en Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/about/)
- Variantes de Canvas 
- Conexiones entre pasos en Canvas

Si deseas editar o añadir más pasos a tu recorrido de usuario de Canvas, se aplicarán los siguientes detalles:

- Los usuarios que aún no hayan entrado en el Lienzo podrán acceder a los pasos recién creados. 
- Si tu configuración de entrada en Canvas permite a los usuarios volver a entrar en los pasos, los usuarios que ya hayan superado pasos recién creados serán elegibles para volver a entrar.
- Los usuarios que están actualmente en un Canvas lanzado, pero que no han alcanzado los puntos del recorrido del usuario en los que se añaden nuevos pasos, pueden recibir esos nuevos pasos añadidos. 

Si elimina un paso de [Retraso]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/) o [Rutas de acción]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/), puede redirigir opcionalmente a los usuarios que están esperando actualmente en el paso a otro paso de Canvas. En caso de retrasos, los usuarios permanecen en el paso hasta que finaliza el periodo de retraso. En el caso de las rutas de acción, los usuarios permanecen en el paso hasta el final de la ventana de evaluación.

Tenga en cuenta que cuando lanza un lienzo inicialmente, Braze pone en cola a los usuarios para el paso de mensaje en el que se encuentran, no para todos los mensajes posteriores del lienzo. Si realizas una modificación en Canvas después del lanzamiento, es posible que algunos usuarios ya estén en cola y no vean los cambios. Si detienes el Canvas, lo duplicas, lo modificas y lanzas esta nueva versión, el Canvas volverá a evaluar a todos los usuarios, no solo a aquellos que aún no se hayan puesto en cola.

Consulte la sección [Prácticas recomendadas](#best-practices) para conocer los casos de uso específicos de la edición. En general, es una buena práctica evitar editar Canvas en vivo, ya que puede producirse un comportamiento inesperado.

{% details Expand for original Canvas editor details %}

Ten en cuenta las siguientes modificaciones permitidas en Canvas tras el lanzamiento, dependiendo del flujo de trabajo con el que se haya creado tu Canvas. Si tu Canvas utiliza el flujo de trabajo original de Canvas, primero tendrás que clonarlo en Canvas Flow para poder realizar modificaciones tras el lanzamiento.

No puedes editar ni eliminar conexiones existentes, ni insertar un paso entre pasos conectados existentes. Si deseas editar o añadir más pasos a tu recorrido de usuario de Canvas, se aplicarán los siguientes detalles:

- Los usuarios que aún no hayan entrado en el Lienzo podrán acceder a los pasos recién creados. 
- Si tu configuración de entrada en Canvas permite a los usuarios volver a entrar en los pasos, los usuarios que ya hayan superado pasos recién creados serán elegibles para volver a entrar.
- Los usuarios que están actualmente en un Canvas lanzado, pero que no han alcanzado los nuevos pasos añadidos en el recorrido del usuario, pueden recibir esos nuevos pasos añadidos.
- Si un paso de Retraso es el último paso del lienzo, los usuarios que lleguen a ese paso saldrán automáticamente del lienzo y no recibirán ningún paso recién creado.

{% alert important %}
Si actualizas la configuración **de** **Retardo** o **Ventana** para un paso en Canvas, los usuarios que se encuentren en ese paso en el momento de la actualización se ajustarán al tiempo de retardo que se les asignó cuando entraron originalmente en él. Solo los nuevos usuarios que entran en Canvas y aquellos que aún no han sido incluidos en la cola para ese paso reciben el mensaje a la hora actualizada.
{% endalert %}

Al detener un Canvas, no se cierra la sesión de los usuarios que están esperando recibir un mensaje. Si vuelves a habilitar Canvas y los usuarios siguen esperando el mensaje, lo recibirán (a menos que haya pasado el tiempo en que se les debería haber enviado el mensaje, en cuyo caso no lo recibirán).

{% enddetails %}

## Detalles del lienzo

Puedes editar la configuración y los detalles siguientes después de iniciar un Canvas:

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
* Retrasos (solo para pasos de retraso)

Sin embargo, el tipo de programación del paso y los porcentajes de control no son editables después del lanzamiento. En los pasos de rutas de acción y rutas de audiencia, las clasificaciones y las ventanas de evaluación no se pueden editar después del lanzamiento.

### Porcentajes de variantes del lienzo

Después de lanzar un lienzo, sólo puede disminuir los porcentajes de variantes de control. Si se modifica el porcentaje de una variante en Canvas, descubrirá que sus usuarios pueden redistribuirse a otras variantes.

Inicialmente, a estos usuarios se les asigna aleatoriamente una variante concreta antes de recibir una campaña por primera vez. A partir de ese momento, cada vez que se reciba la campaña (o el usuario vuelva a entrar en una variante en Canvas), recibirás la misma variante, a menos que se modifiquen los porcentajes de las variantes.

Si los porcentajes de variantes cambian, los usuarios pueden redistribuirse a otras variantes. Los usuarios permanecen en estas variantes hasta que se vuelven a modificar los porcentajes. Tenga en cuenta que para los lienzos que utilizan la ramificación con filtros `NOT` con números de cubo aleatorios, es posible que los usuarios no reciban la misma ramificación cada vez en su recorrido de usuario cuando vuelvan a entrar en el lienzo.

#### Grupos de control

Los grupos de control siguen siendo coherentes si el porcentaje de variantes no varía. Si se disminuye o aumenta el porcentaje de un grupo de control, los usuarios que antes recibían mensajes no podrían entrar en el grupo de control en un envío posterior, ni ningún usuario del grupo de control recibiría nunca un mensaje.

### Hora de envío local

Los lienzos programados para enviarse a una hora local pueden editarse hasta 24 horas antes de la hora de envío programada. Esta ventana se denomina "zona segura". 

{% alert tip %}
Si tiene intención de realizar ediciones más extensas que conlleven la creación de una nueva copia completa del lienzo, recuerde excluir a los usuarios que recibieron el primer lienzo y reajustar las horas de programación del lienzo para tener en cuenta el envío por zona horaria.
{% endalert %}

Cuando se configura un horario de entrada para que los usuarios entren inmediatamente después del inicio, Canvas se inicia en el momento más cercano en incrementos de 5 minutos. Por ejemplo, si actualizas un Canvas para que los usuarios accedan inmediatamente a las 8:31 a. m. PST, la hora de inicio se establece a las 8:30 a. m. PST y en la zona horaria de la empresa.

### Borrar variantes

Cuando se eliminan variantes de un Canvas, ocurre lo siguiente:

- Se eliminan los pasos dentro de la variante (incluidos los compartidos por otras variantes). 
- Se eliminan los análisis por pasos y los análisis de nivel superior para Canvas, como _Entradas totales_, _Salidas totales_ y _Tasa de conversión_.
- Los usuarios de las variantes eliminadas salen de los pasos y no se envían los mensajes siguientes.

### Propiedades de entrada del lienzo

Las propiedades de entrada en Canvas no están plantillas en los pasos cuando se envían. Esto significa que cuando se editan las propiedades de entrada de Canvas después de que se haya iniciado Canvas, estos cambios solo se aplican a los nuevos usuarios que entran en Canvas. Si tu Canvas permite a los usuarios volver a entrar en él, los usuarios que vuelvan a entrar se determinarán según las propiedades de entrada actualizadas del Canvas.

## Buenas prácticas

Echa un vistazo a estas prácticas recomendadas que debes tener en cuenta cuando edites o añadas algo a tu Canvas después de haberlo lanzado.

{% alert important %}
En general, evita realizar cambios mientras Canvas está activo y los usuarios están en cola.
{% endalert %}

### Pasos desconectados

Puedes lanzar tu Canvas con pasos desconectados y también guardar estos Canvases post-lanzamiento. Antes de desconectar un paso de su flujo de trabajo, le recomendamos que compruebe la vista analítica de los pasos para los usuarios pendientes.

Supongamos que un usuario se encuentra en un paso desconectado de su flujo de trabajo Canvas. Este usuario realiza el avance al siguiente paso, si lo hay. La configuración del paso determina cómo debe avanzar el usuario. 

Al crear o editar pasos desconectados, puede realizar cambios en estos pasos independientes sin tener que conectarlos directamente al resto de su Lienzo. Esto te ayudará a probar los pasos antes de volver a iniciar Canvas. 

### Paso de ruta de experimentos

Si tu Canvas tiene un experimento de ruta ganadora o ruta personalizada activo o en curso y actualizas el Canvas activo (independientemente de si actualizas el paso de la ruta de experimentos en sí), el experimento en curso finaliza y el paso de ruta de experimentos no determina una ruta ganadora ni rutas personalizadas. Para reiniciar el experimento, puedes desconectar la ruta de experimentos existente e iniciar una nueva, o duplicar el Canvas y crear uno nuevo. De lo contrario, los usuarios seguirán la ruta de experimentos como si no se hubiera seleccionado ningún método de optimización.

### Retrasos temporales

Editar lienzos con retrasos temporales puede resultar un poco complicado, así que ten en cuenta los siguientes detalles al realizar modificaciones en tus lienzos:

- Si actualizas el retraso en un paso de retraso, solo los nuevos usuarios que entren en el lienzo y los usuarios que no hayan sido puestos en cola para ese paso recibirán el mensaje con el retraso actualizado.
- Si eliminas un paso con un retraso temporal (como Retraso o Rutas de acción) y decides redirigir a esos usuarios a otro paso en Canvas, los usuarios solo serán redirigidos una vez que haya finalizado el retraso temporal del paso. Por ejemplo, supongamos que eliminas un paso de retraso de un día y rediriges a esos usuarios a un paso de mensaje. En este caso, los usuarios solo son redirigidos una vez transcurrido el plazo de un día.
- Si tu Canvas tiene uno o más pasos de rutas de experimentos, eliminar pasos podría invalidar los resultados de este paso.

### Detener Canvas

Al detener un Canvas, no se cierra la sesión de los usuarios que están esperando en un paso en Canvas. Si vuelves a habilitar Canvas y los usuarios siguen esperando, completarán el paso y pasarán al siguiente. Sin embargo, si ha pasado el tiempo en el que el usuario debería haber avanzado al siguiente paso, se sale del Canvas. 

Por ejemplo, supongamos que tienes un lienzo creado con el flujo de trabajo Canvas Flow configurado para iniciarse a las 2 p. m. con una variante de dos pasos: un paso de retraso de una hora que pasa a un paso de mensaje. 

Un usuario entra en este Canvas a las 14:01 y entra en el paso de Retraso al mismo tiempo. Esto significa que tú estás programado para pasar al siguiente paso del recorrido del usuario (el paso Mensaje) a las 3:01 p. m. Si detienes Canvas a las 2:30 p. m. y lo vuelves a habilitar a las 3:30 p. m., el usuario sale de Canvas, ya que son más de las 3:01 p. m. Sin embargo, si vuelves a habilitar el lienzo a las 2:40 p. m., el usuario pasa al paso Mensaje como se espera a las 3:01 p. m.

## Lo que hay que saber

Los siguientes problemas comunes pueden desencadenarse al editar o añadir más componentes a cualquier otro componente de un Canvas después de su lanzamiento. 

{% alert important %}
Los siguientes problemas se pueden evitar. Si necesitas realizar modificaciones en un Canvas después de su lanzamiento, te recomendamos que primero confirmes que todos los usuarios que ya han accedido al Canvas hayan completado su recorrido. Además, te recomendamos que no elimines pasos que ya hayan sido procesados por al menos un usuario.
{% endalert %}

- Datos de informe faltantes (cuando se eliminan y vuelven a añadir variantes de mensajes)
- Los usuarios no están siguiendo la ruta esperada.
- Los mensajes se envían en momentos inesperados.
- Las ediciones no sobrescriben los datos de Currents, por lo que es posible que observes discrepancias entre los pasos en Canvas (como`canvas_step_ids`  que no existen en Canvas debido a su eliminación).
- Los usuarios pueden recibir el mismo mensaje dos veces.
- Los usuarios no recibirán mensajes debido al límite de velocidad existente.
  - Cuando actualizas el límite de velocidad en un Canvas activo, el nuevo límite se aplica a todos los mensajes que se envíen en el futuro, incluidos los usuarios que ya están en el Canvas. Sin embargo, debido al almacenamiento en caché interno (hasta 30 segundos), puede haber un breve retraso antes de que se aplique completamente el nuevo límite de velocidad. Ten en cuenta que Braze pone en cola a los usuarios para el paso del mensaje en el que se encuentran actualmente, por lo que el límite de velocidad que se aplica es el que está vigente cuando se envía realmente el mensaje de cada paso.
- Cuando un Canvas se [detiene automáticamente]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/about_statuses/#available-statuses), también se eliminan los borradores posteriores al lanzamiento del Canvas.
