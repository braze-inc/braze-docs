---
nav_title: Grupo de control global
article_title: Grupo de control global
alias: /global_control_group/
page_order: 0

description: "Este artículo explica cómo configurar y utilizar correctamente el Grupo de Control Global. También explica cómo consultar los informes y las métricas que genera el uso de estos grupos."
page_type: reference
tool: Reports
search_rank: 1
toc_headers: h2

---

# Grupo de control global

> Utiliza el grupo de control global para especificar un porcentaje de todos los usuarios que no deberían recibir ninguna campaña o Lienzo, lo que te permitirá analizar el impacto global de tus esfuerzos de mensajería a lo largo del tiempo. 

Comparando el comportamiento de los usuarios que reciben mensajes con los que no, puedes comprender mejor cómo tus campañas de marketing y tus Lienzos contribuyen a aumentar las sesiones y los eventos personalizados.

## Funcionamiento del Grupo Mundial de Control

Con el Grupo de Control Global, puede establecer un porcentaje de todos los usuarios como grupo de control. Cuando se guarda, los usuarios del grupo no reciben campañas ni Lienzos. 

{% alert important %}
Tu grupo de control global se aplica a todos los canales, campañas y lienzos, excepto a [las campañas API]({{site.baseurl}}/api/api_campaigns). Esto significa que los usuarios de tu grupo de control siguen recibiendo campañas API. Sin embargo, esta excepción no se aplica a las tarjetas de contenido. Si utilizas una campaña de tarjeta de contenido desencadenada por API, los usuarios de tu grupo de control no las recibirán.
{% endalert %}

### Asignar usuarios aleatoriamente al Grupo de Control Global

Braze selecciona aleatoriamente múltiples rangos de [números de cubos aleatorios]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/ab_testing_with_random_buckets/#step-1-segment-your-users-by-the-random-bucket-attribute) e incluye usuarios de esos cubos seleccionados. Si actualmente utilizas números de contenedor aleatorios para otros fines, consulta [Cosas que debes tener en cuenta](#things-to-watch-for). 

Cuando se genera tu grupo de control global, todos los usuarios con números de contenedor aleatorios forman parte del grupo. Además, los nuevos usuarios que se unan después de este punto (los adquiridos después de que se generara el grupo de control global) que tengan estos números de contenedor aleatorios también se añadirán al grupo de control global. Del mismo modo, si se eliminan muchos usuarios, puedes esperar que el tamaño de tu grupo de control global se reduzca porque un porcentaje de esos usuarios eliminados ha caído en este grupo. Esto mantiene el tamaño de tu grupo como un porcentaje constante en relación con toda tu base de usuarios.

### Asigna aleatoriamente usuarios al grupo de tratamiento para informar

Para que puedas informar sobre la elevación, Braze también crea un grupo de tratamiento. El grupo de tratamiento es un grupo seleccionado aleatoriamente de usuarios que no forman parte de tu grupo de control global, y se genera utilizando el mismo método de número de contenedor aleatorio que el grupo de control global. 

Tu grupo de tratamiento tiene un tamaño similar al de tu grupo de control global, pero es poco probable que tenga exactamente el mismo tamaño. Para [los informes](#reporting), Braze mide los comportamientos de los usuarios de tu grupo de control y de los usuarios de tu muestra de tratamiento. Cada espacio de trabajo tiene como máximo un grupo de control global y un grupo de muestra de tratamiento. El grupo de muestra de tratamiento es el mismo grupo de usuarios, independientemente de cómo configures tus informes de control global.

### Excluir usuarios de las banderas de características

No puedes habilitar [los indicadores de características]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/feature_flags/) para los usuarios de tu grupo de control global. Esto significa que los usuarios de tu grupo de control global tampoco pueden formar parte de los experimentos con banderas de características.

### Excluir usuarios del grupo de control global

No puedes eliminar usuarios concretos del grupo de control global, pero puedes añadir [configuraciones de exclusión]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/#step-3-assign-exclusion-settings) para que las campañas y los lienzos con etiquetas especificadas **no** utilicen el grupo de control global. También puedes habilitar y deshabilitar tu grupo de control global para cambiar los miembros. La duración ideal para barajar usuarios varía en función del tipo de prueba que estés realizando, pero te recomendamos que no lo hagas más de una vez al mes.

## Crear un grupo de control global

### Paso 1: Vaya a la configuración del grupo de control global

En el panel de control, vaya a **Audiencia** > **Grupo de control global**.

### Paso 2: Asignar un porcentaje de todos los usuarios a este grupo de control

Introduce un porcentaje para tu grupo de control y selecciona **Guardar**. Una vez introducido, Braze te muestra una estimación de cuántos usuarios entran en tu muestra de control global, tratamiento y tratamiento. Ten en cuenta que cuantos más usuarios tengas en tu espacio de trabajo, más precisa será esta estimación. 

El número de usuarios de tu grupo de control global se actualiza automáticamente tras su configuración inicial para seguir siendo proporcional a este porcentaje cuando se añaden más usuarios a tu espacio de trabajo. Además, los usuarios que se unan después de configurar el grupo de control global y que tengan números de contenedor aleatorios también se añadirán al grupo de control global. Si se añaden muchos usuarios, el tamaño de tu grupo de control global crece para mantener un porcentaje constante respecto a toda tu base de usuarios. Cuando crece el tamaño de tu grupo de control global, los usuarios que estaban antes en el grupo siguen permaneciendo en él (a menos que hagas cambios en tu grupo desactivándolo y creando uno nuevo).

Para obtener directrices sobre porcentajes, consulta [Pruebas de buenas prácticas](#percentage-guidelines).

![La Configuración del Grupo de Control Global con la Configuración de Audiencia establecida en "Asignar el cinco por ciento de todos los usuarios al Grupo de Control Global".]({% image_buster /assets/img/control_group/control_group4.png %})

### Paso 3: Asignar parámetros de exclusión

Utilice etiquetas para añadir configuraciones de exclusión a su Grupo de Control Global. Las campañas o lienzos que utilicen las etiquetas incluidas en la configuración de exclusión no utilizarán su Grupo de control global. Estas campañas y lienzos se siguen enviando a todos los usuarios de la audiencia objetivo, incluidos los de tu grupo de control global.

{% alert tip %}
Puede que quieras añadir configuraciones de exclusión si tienes mensajes transaccionales que deban enviarse a todos los usuarios.
{% endalert %}

![La sección para añadir o editar la configuración de exclusión de tu grupo de control global.]({% image_buster /assets/img/control_group/control_group5.png %})

### Paso 4: Guarda tu grupo de control

En este punto, Braze genera un grupo de usuarios seleccionados aleatoriamente para que constituyan el porcentaje seleccionado de su base total de usuarios. Una vez guardado, todas las campañas y lienzos activos y futuros dejarán de enviarse a los usuarios de este grupo, excepto las campañas o lienzos que contengan alguna de las etiquetas de la configuración de exclusión.

## Hacer cambios en tu grupo de control global

Sólo puedes hacer cambios en tu grupo de control global desactivándolo y creando uno nuevo. Por ejemplo, si configuras un grupo de control global que represente el 10% de tu audiencia y quieres reducir su tamaño al 5%, debes desactivar tu grupo de control global actual y volver a habilitar un nuevo grupo de control global. 

Puedes desactivar tu grupo de control global en cualquier momento desde la pestaña **Configuración del grupo de control global**, pero ten en cuenta que al hacerlo los usuarios de este grupo pasan a ser elegibles inmediatamente para campañas y Lienzos.

Antes de desactivar su grupo de control, le recomendamos que [exporte](#export-group-members) un CSV de los usuarios de ese grupo por si necesita consultarlo más adelante. Cuando se desactiva un grupo de control, no hay forma de que Braze restaure el grupo o identifique qué usuarios estaban en este grupo.

Después de desactivar su Grupo de Control, puede guardar uno nuevo. Al introducir un porcentaje y guardarlo, Braze genera un nuevo grupo de usuarios seleccionados aleatoriamente. Si introduces el mismo porcentaje que antes, Braze genera un nuevo grupo de usuarios para tus grupos de control y de tratamiento.

![Un cuadro de diálogo titulado "Estás realizando cambios en la configuración de mensajería global" con un texto que advierte de que, una vez desactivado tu grupo de control global, ya no queda excluido de ninguna campaña o lienzo nuevo o activo.]({% image_buster /assets/img/control_group/control_group2.png %}){: style="max-width:60%" }

## Exporte los miembros de su grupo de control {#export-group-members}

Si quieres ver qué usuarios están en tu grupo de control global, puedes exportar los miembros de tu grupo mediante CSV o API. 

Para ejecutar una exportación CSV, vaya a la pestaña **Configuración global del grupo de control** y haga clic en <i class="fas fa-download"></i> **Exportar**. Para exportar por API, utiliza el [punto final`/users/export/global_control_group` ]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group/).

{% alert important %}
Los grupos de control históricos no se conservan, por lo que sólo puede exportar los miembros de su grupo actual. Asegúrese de exportar toda la información necesaria antes de desactivar un grupo de control.
{% endalert %}

## Ver si un usuario está en un grupo de control global

Puedes ver la pertenencia a un grupo de control global yendo a la sección **Varios** en la pestaña **Interacción** del perfil de un usuario individual.

![Una sección "Varios" informa de que el usuario tiene un número de contenedor aleatorio de 6356 y no está en el grupo de control global.]({% image_buster /assets/img/control_group/control_group1.png %}){: style="max-width:50%;"}

## Informe

Consulte [Informes de grupos de control global]({{site.baseurl}}/user_guide/analytics/reporting/global_control_group_reporting/) para obtener información sobre las métricas de los informes.

## Solución de problemas

A medida que configures tus grupos de control global y veas los informes, estos son los errores con los que te puedes encontrar:

| Problema | Solución de problemas |
| --- | --- |
| No se puede guardar el porcentaje introducido al designar un Grupo de Control Global. | Este problema se produce si se introduce un número no entero o un número entero que no esté comprendido entre 1 y 15 (ambos inclusive). |
| Error "Braze no puede actualizar su grupo de control global" en la página de configuración de control global. | Esto suele indicar que algún componente de esta página ha cambiado, probablemente debido a acciones realizadas por otro usuario en su cuenta Braze. En este caso, actualice la página y vuelva a intentarlo. |
| El informe del Grupo Global de Control no contiene datos. | Si accedes al Informe de grupo de control global sin haber guardado un grupo de control global, no verás ningún dato en el informe. Cree y guarde un Grupo de Control Global e inténtelo de nuevo. |
| Mi tasa de conversión es del 0% o no estoy viendo la visualización del gráfico, a pesar de que hay más de cero eventos ocurriendo. | Si el número de conversiones es muy pequeño y los grupos de control o tratamiento son muy grandes, la tasa de conversión puede redondearse al 0% y, por tanto, no aparecer en el gráfico. Puedes verificarlo comprobando la métrica Número total de eventos. Puede comparar la eficacia de los dos grupos utilizando la métrica del porcentaje de incremento.  |
| Mi tasa de conversión (u otras métricas) están cambiando drásticamente dependiendo del período de tiempo para el que estoy viendo los datos. | Si visualiza los datos en periodos cortos, es posible que sus métricas fluctúen de un día para otro o de una semana para otra. Le recomendamos que consulte las métricas durante al menos un mes. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Aspectos a tener en cuenta {#things-to-watch-for}

#### Números de cubo aleatorios superpuestos

Tu Grupo de control global se forma utilizando Números de contenedor aleatorios y, por tanto, si realizas otras pruebas utilizando filtros de segmento de Números de contenedor aleatorios, ten en cuenta que podría haber un solapamiento entre los segmentos que crees y los usuarios de tu Grupo de control global.

#### Direcciones de correo electrónico duplicadas

Si dos usuarios con ID externas de usuario diferentes tienen la misma dirección de correo electrónico, y uno de estos usuarios está en el grupo de control y el otro no, se seguirá enviando un correo electrónico a esa dirección de correo electrónico cuando el usuario del grupo de no control sea elegible para recibir un correo electrónico. Cuando esto ocurre, marcamos ambos perfiles de usuario como que han recibido la campaña o Canvas que contiene ese correo electrónico.

#### Grupo de control global y grupos de control específicos de mensajes

Es posible tener un Grupo de Control Global y también utilizar un grupo de control específico de campaña o específico de Canvas. Disponer de un grupo de control específico para la campaña o el lienzo permite medir el impacto de un mensaje concreto.

A los usuarios de su grupo de tratamiento global se les retiene la recepción de cualquier mensaje que no sean aquellos con excepciones de etiquetas, y si añade un control a una campaña o Canvas, Braze retiene una parte de su grupo de tratamiento global de la recepción de esa campaña o Canvas en particular. Esto significa que si un miembro del grupo de control global no es elegible para recibir una campaña o Canvas concreto, no está presente en el grupo de control de esa campaña o Canvas en particular.

> En resumen, los usuarios del Grupo de control global son filtrados de la campaña o del público de Canvas antes de entrar. De los usuarios que entran en la campaña o Canvas, un porcentaje de ellos se asigna a la variante de control.

#### Segmentos del grupo de control global en la consola de desarrollador

Es posible que vea varios segmentos de **Control Global** en la sección **Identificadores de API adicionales** de la página [Claves de API]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/). Esto se debe a que cada vez que se activa o desactiva el Grupo de Control Global, se forma un nuevo Grupo de Control Global. Esto lleva a múltiples segmentos etiquetados como "Grupo de Control Global".

Sólo uno de estos segmentos está activo y puede ser consultado utilizando el [endpoint`/users/export/global_control_group` ]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group/), o exportado desde el cuadro de mandos. La exportación del panel indica específicamente qué subsegmentos componen este grupo de control global.

## Pruebas de buenas prácticas

### Tamaño óptimo del grupo de control {#percentage-guidelines}

Hay que tener en cuenta dos reglas principales\*\*:
1. Su grupo de control no debe ser inferior a 1000 usuarios.
2. El grupo de control no debe superar el 10% de su audiencia.

Si su audiencia total es inferior a 10.000, debe aumentar el porcentaje para crear un grupo de más de 1.000 usuarios; en este caso, no debe aumentar el porcentaje por encima del 15%. Ten en cuenta que cuanto menor sea el tamaño total de tu espacio de trabajo, más difícil será realizar una prueba estadísticamente rigurosa.

- Algunas de las ventajas y desventajas que hay que tener en cuenta al pensar en el tamaño del grupo de control son que se necesita un número significativamente grande de clientes en el grupo de control para que cualquier análisis de comportamiento creado sea fiable. Sin embargo, cuanto mayor sea el grupo de control, menos clientes recibirán sus campañas, lo que supone un inconveniente si las utiliza para impulsar la participación y las conversiones.
- El porcentaje ideal de tu audiencia total depende de lo grande que sea tu audiencia total. Cuanto mayor sea tu audiencia total, menor puede ser tu porcentaje. Sin embargo, si tienes poca audiencia, necesitarás un porcentaje mayor para tu grupo de control.

### Duración del experimento 

#### Elija una duración ideal {#reshuffle}

La duración del experimento antes de reorganizar los miembros del grupo de control depende de lo que se esté probando y del comportamiento de referencia de los usuarios. Si no está seguro, un buen punto de partida es un trimestre (tres meses), pero no debe ser inferior a un mes.

Para determinar la duración adecuada de tu experimento, considera qué preguntas esperas responder. Por ejemplo, ¿quieres ver si hay diferencias en las sesiones? Si es así, piense en la frecuencia con la que sus usuarios tienen sesiones de forma orgánica. Las marcas cuyos usuarios tienen sesiones todos los días pueden realizar experimentos más cortos que las marcas cuyos usuarios tienen sesiones sólo un par de veces al mes. 

O puede que te interese un evento personalizado, por lo que puede que tu experimento tenga que durar más que un experimento en el que examinas sesiones, si es probable que tus usuarios desencadenen ese evento personalizado con menos frecuencia.

{% alert tip %}
Cuanto más tiempo mantengas al mismo grupo de control, más divergirá del grupo de tratamiento, lo que puede crear un sesgo. El restablecimiento del grupo de control global reequilibra la población.
{% endalert %}

#### Trate de limitar la finalización prematura de los experimentos

Antes de comenzar el experimento, debe decidir cuánto tiempo va a durar y, a continuación, sólo debe terminar el experimento y recopilar los resultados finales una vez alcanzado este punto predeterminado. Terminar tu experimento antes de tiempo, o siempre que veas datos prometedores, introduce un sesgo.

#### Piense en métricas valiosas

Tenga en cuenta los comportamientos de referencia para las métricas que más le interesan. ¿Te interesan las tasas de compra de los planes de suscripción que sólo se renuevan anualmente? ¿O tienen los clientes un hábito semanal para el evento que le gustaría medir? Piense en el tiempo que tardan los usuarios en alterar potencialmente sus comportamientos debido a su mensaje. Después de decidir cuánto tiempo debe durar tu experimento, asegúrate de no terminar tu experimento ni registrar los resultados finales antes de tiempo, o tus conclusiones podrían estar sesgadas.
