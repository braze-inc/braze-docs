---
nav_title: Grupo de control global
article_title: Grupo de control global
alias: /global_control_group/
page_order: 0

description: "Este artículo explica cómo configurar y utilizar correctamente el grupo de control global. También explica cómo ver los informes y métricas generados por el uso de estos grupos."
page_type: reference
tool: Reports
search_rank: 1

---

# Grupo de control global

> Utiliza el grupo de control global para especificar un porcentaje de todos los usuarios que no deberían recibir ninguna campaña o Lienzo, lo que te permitirá analizar el impacto global de tus esfuerzos de mensajería a lo largo del tiempo. 

Al comparar los comportamientos de los usuarios que reciben mensajes con los que no, puedes comprender mejor cómo tus campañas de marketing y tus Lienzos dan lugar a un aumento de las sesiones y los eventos personalizados.

## Cómo funciona el grupo de control global

Con el grupo de control global, puedes establecer un porcentaje de todos los usuarios como grupo de control. Una vez guardado, los usuarios del grupo no recibirán campañas ni Lienzos. 

{% alert important %}
Tu grupo de control global se aplica a todos los canales, campañas y lienzos, excepto a [las campañas API]({{site.baseurl}}/api/api_campaigns). Esto significa que los usuarios de tu grupo de control seguirán recibiendo campañas API. Sin embargo, esta excepción no se aplica a las tarjetas de contenido. Si utilizas una campaña de tarjeta de contenido desencadenada por API, los usuarios de tu grupo de control no las recibirán.
{% endalert %}

### Asigna usuarios aleatoriamente al grupo de control global

Braze selecciona aleatoriamente múltiples rangos de [números de contenedor aleatorios]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/ab_testing_with_random_buckets/#step-1-segment-your-users-by-the-random-bucket-attribute) e incluye a los usuarios de esos contenedores seleccionados. Si actualmente utilizas números de contenedor aleatorios para otros fines, consulta [Cosas que debes tener en cuenta](#things-to-watch-for). 

Cuando se genere tu grupo de control global, todos los usuarios con números de contenedor aleatorios formarán parte del grupo. Además, los nuevos usuarios que se unan después de este punto (los adquiridos después de que se generara el grupo de control global) que tengan estos números de contenedor aleatorios también se añadirán al grupo de control global. Del mismo modo, si se eliminan muchos usuarios, es de esperar que el tamaño de tu grupo de control global se reduzca, porque un porcentaje de esos usuarios eliminados habrá caído en este grupo. Esto mantiene el tamaño de tu grupo como un porcentaje constante en relación con toda tu base de uso.

### Asignar usuarios aleatoriamente al grupo de tratamiento para la elaboración de informes

Para que puedas informar sobre la elevación, Braze también crea un grupo de tratamiento. El grupo de tratamiento es un grupo seleccionado aleatoriamente de usuarios que no forman parte de tu grupo de control global, y se genera utilizando el mismo método de número de contenedor aleatorio que el grupo de control global. 

Tu grupo de tratamiento tendrá un tamaño similar al de tu grupo de control global, pero es poco probable que tenga exactamente el mismo tamaño. Para [los informes](#reporting), Braze mide los comportamientos de los usuarios de tu grupo de control y de los usuarios de tu muestra de tratamiento. Cada espacio de trabajo tiene como máximo un grupo de control global y un grupo de muestra de tratamiento. El grupo de muestra de tratamiento es el mismo grupo de usuarios, independientemente de cómo configures tus informes de control global.

### Excluir usuarios de las banderas de características

No puedes habilitar [los indicadores de características]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/feature_flags/) para los usuarios de tu grupo de control global. Esto significa que los usuarios de tu grupo de control global tampoco pueden formar parte de los experimentos con banderas de características.

### Excluir usuarios del grupo de control global

No puedes eliminar usuarios concretos del grupo de control global, pero puedes añadir [configuraciones de exclusión]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/#step-3-assign-exclusion-settings) para que las campañas y los lienzos con etiquetas especificadas **no** utilicen el grupo de control global. También puedes habilitar y deshabilitar tu grupo de control global para cambiar los miembros. La duración ideal para barajar usuarios varía en función del tipo de prueba que estés realizando, pero te recomendamos que no lo hagas más de una vez al mes.

## Crear un grupo de control global

### Paso 1: Navega hasta la Configuración del grupo de control global

En el panel, ve a **Audiencia** > **Grupo de** control global **.**

### Paso 2: Asigna un porcentaje de todos los usuarios a este grupo de control

Introduce un porcentaje para tu grupo de control y selecciona **Guardar**. Una vez introducido, Braze te muestra una estimación de cuántos usuarios entrarán en tu muestra de control global, tratamiento y tratamiento. Ten en cuenta que cuantos más usuarios tengas en tu espacio de trabajo, más precisa será esta estimación. 

El número de usuarios de tu grupo de control global se actualiza automáticamente tras su configuración inicial para seguir siendo proporcional a este porcentaje cuando se añaden más usuarios a tu espacio de trabajo. Además, los usuarios que se unan después de configurar el grupo de control global y que tengan números de contenedor aleatorios también se añadirán al grupo de control global. Si se añaden muchos usuarios, el tamaño de tu grupo de control global crecerá para mantener un porcentaje constante en relación con toda tu base de usuarios. Cuando aumente el tamaño de tu grupo de control global, los usuarios que estaban antes en el grupo seguirán estando en él (a menos que hagas cambios en tu grupo desactivándolo y creando uno nuevo).

Para conocer las pautas porcentuales, consulta [Pruebas de buenas prácticas](#percentage-guidelines).

\![La configuración del grupo de control global con la configuración de audiencia establecida en "Asignar el cinco por ciento de todos los usuarios al grupo de control global".]({% image_buster /assets/img/control_group/control_group4.png %})

### Paso 3: Asignar configuración de exclusión

Utiliza etiquetas para añadir configuraciones de exclusión a tu grupo de control global. Las campañas o Lienzos que utilicen las etiquetas incluidas en la configuración de exclusión no utilizarán tu grupo de control global. Estas campañas y lienzos se siguen enviando a todos los usuarios de la audiencia objetivo, incluidos los de tu grupo de control global.

{% alert tip %}
Puede que quieras añadir configuraciones de exclusión si tienes mensajes transaccionales que deban enviarse a todos los usuarios.
{% endalert %}

Sección para añadir o editar la configuración de exclusión de tu grupo de control global.]({% image_buster /assets/img/control_group/control_group5.png %})

### Paso 4: Guarda tu grupo de control

En este punto, Braze genera un grupo de usuarios seleccionados aleatoriamente para que constituyan el porcentaje seleccionado de tu base total de usuarios. Cuando se guardan, todas las campañas y Lienzos actualmente activos y futuros dejan de enviarse a los usuarios de este grupo, excepto las campañas o Lienzos que contengan alguna de las etiquetas de tu configuración de exclusión.

## Hacer cambios en tu grupo de control global

Sólo puedes hacer cambios en tu grupo de control global desactivándolo y creando uno nuevo. Por ejemplo, si configuras un grupo de control global que represente el 10% de tu audiencia y quieres reducir su tamaño al 5%, debes desactivar tu grupo de control global actual y volver a habilitar un nuevo grupo de control global. 

Puedes desactivar tu grupo de control global en cualquier momento desde la pestaña **Configuración del grupo de control global**, pero ten en cuenta que al hacerlo los usuarios de este grupo serán inmediatamente elegibles para campañas y Lienzos.

Antes de desactivar tu grupo de control, te recomendamos que [exportes](#export-group-members) un CSV de los usuarios de ese grupo por si necesitas consultarlo más adelante. Cuando desactivas un grupo de control, Braze no tiene forma de restaurar el grupo ni de identificar qué usuarios estaban en él.

Después de desactivar tu Grupo de control, puedes guardar uno nuevo. Cuando introduces un porcentaje y lo guardas, Braze genera un nuevo grupo de usuarios seleccionados aleatoriamente. Si introduces el mismo porcentaje que antes, Braze sigue generando un nuevo grupo de usuarios para tus grupos de control y de tratamiento.

Aparece un cuadro de diálogo titulado "Estás realizando cambios en la configuración de mensajería global" con un texto que advierte de que, una vez desactivado tu grupo de control global, ya no se excluirá de ninguna campaña o lienzo nuevo o activo.]({% image_buster /assets/img/control_group/control_group2.png %}){: style="max-width:60%" }

## Exporta los miembros de tu grupo de control {#export-group-members}

Si quieres ver qué usuarios están en tu grupo de control global, puedes exportar los miembros de tu grupo mediante CSV o API. 

Para ejecutar una exportación CSV, ve a la pestaña **Configuración del grupo de control global** y haz clic en <i class="fas fa-download"></i> **Exportar**. Para exportar por API, utiliza el [punto final`/users/export/global_control_group` ]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group/).

{% alert important %}
Los grupos de control históricos no se conservan, por lo que sólo puedes exportar los miembros de tu grupo actual. Asegúrate de exportar toda la información necesaria antes de desactivar un grupo de control.
{% endalert %}

## Ver si un usuario está en un grupo de control global

Puedes ver la pertenencia a un grupo de control global yendo a la sección **Varios** en la pestaña **Interacción** del perfil de un usuario individual.

Una sección "Varios" que informa de que el usuario tiene un número de contenedor aleatorio de 6356 y no está en el grupo de control global.]({% image_buster /assets/img/control_group/control_group1.png %}){: style="max-width:50%;"}

## Informar

Consulta [Informes de grupos de control global]({{site.baseurl}}/user_guide/analytics/reporting/global_control_group_reporting/) para obtener información sobre las métricas de los informes.

## Solución de problemas

A medida que configures tus grupos de control global y veas los informes, aquí tienes algunos errores con los que te puedes encontrar:

| Edición | Solución de problemas |
| --- | --- |
| No se puede guardar el porcentaje introducido al designar un grupo de control global. | Este problema se produce si introduces un número no entero o un número entero que no esté comprendido entre 1 y 15 (ambos inclusive). |
| Error "Braze no puede actualizar tu grupo de control global" en la página de configuración de control global. | Esto suele indicar que algún componente de esta página ha cambiado, probablemente debido a acciones realizadas por otro usuario en tu cuenta de Braze. En este caso, actualiza la página y vuelve a intentarlo. |
| El informe del grupo de control global no tiene datos. | Si accedes al Informe de grupo de control global sin haber guardado un grupo de control global, no verás ningún dato en el informe. Crea y guarda un grupo de control global e inténtalo de nuevo. |
| Mi tasa de conversión es del 0% o no veo que se muestre el gráfico, aunque se produzcan más de cero eventos. | Si el número de conversiones es muy pequeño y tus grupos de control o tratamiento son muy grandes, la tasa de conversión puede redondearse a 0% y, por tanto, no aparecer en el gráfico. Puedes verificarlo comprobando la métrica Número total de eventos. Podrías comparar la eficacia de tus dos grupos utilizando la métrica del porcentaje de aumento incremental.  |
| Mi tasa de conversión (u otras métricas) cambian drásticamente en función del periodo de tiempo del que estoy viendo los datos. | Si visualizas los datos en periodos de tiempo cortos, es posible que tus métricas fluctúen de un día para otro o de una semana para otra. Te recomendamos que veas las métricas a lo largo de al menos un mes. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Cosas a tener en cuenta {#things-to-watch-for}

#### Números de contenedor aleatorios superpuestos

Tu grupo de control global se forma utilizando números de contenedor aleatorios y, por tanto, si realizas otras pruebas utilizando filtros de segmento de números de contenedor aleatorios, ten en cuenta que podría haber un solapamiento entre los segmentos que crees y los usuarios de tu grupo de control global.

#### Duplicar direcciones de correo electrónico

Si dos usuarios que tienen ID externas de usuario diferentes tienen la misma dirección de correo electrónico, y uno de estos usuarios está en el grupo de control y el otro no, se seguirá enviando un correo electrónico a esa dirección de correo electrónico siempre que el usuario del grupo de no control sea elegible para recibir un correo electrónico. Cuando esto ocurra, marcaremos ambos perfiles de usuario como que han recibido la campaña o el Canvas que contiene ese correo electrónico.

#### Grupo de control global y grupos de control de mensajes específicos

Es posible tener tanto un grupo de control global como utilizar un grupo de control específico de campaña o específico de Canvas. Tener un grupo de control específico para la campaña o para Canvas te permite medir el impacto de un mensaje concreto.

Los usuarios de tu grupo de control global no pueden recibir más mensajes que los que tienen excepciones de etiqueta, y si añades un control a una campaña o Canvas, Braze retiene una parte de tu grupo de control global para que no reciba esa campaña o Canvas en particular. Esto significa que si un miembro del grupo de control global no es elegible para recibir una campaña o Canvas en particular, tampoco estará presente en el grupo de control de esa campaña o Canvas en concreto.

> En resumen, los usuarios del grupo de control global son filtrados de la audiencia de la campaña o del Canvas antes de la entrada. De los usuarios que entran en la campaña o Canvas, un porcentaje de ellos se asigna a la variante de control.

#### Segmentos del grupo de control global en la consola para desarrolladores

Puedes ver varios segmentos de **control global** en la sección **Identificadores adicionales de API** de la página [Claves de API]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/). Esto se debe a que cada vez que se habilita o deshabilita el grupo de control global, se forma un nuevo grupo de control global. Esto da lugar a varios segmentos etiquetados como "grupo de control global".

Sólo uno de estos segmentos está activo y puede consultarse mediante el [punto final`/users/export/global_control_group` ]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group/), o exportarse desde el panel. La exportación del panel indica específicamente qué subsegmentos componen este grupo de control global.

## Pruebas de buenas prácticas

### Tamaño óptimo del grupo de control {#percentage-guidelines}

Dos reglas principales a tener en cuenta son\*\*:
1. Tu grupo de control no debe ser inferior a 1000 usuarios.
2. Tu grupo de control no debe ser más del 10% de toda tu audiencia.

Si tienes una audiencia total inferior a 10.000, debes aumentar el porcentaje para crear un grupo de más de 1.000 usuarios; en este caso, no debes aumentar el porcentaje por encima del 15%. Ten en cuenta que cuanto menor sea el tamaño total de tu espacio de trabajo, más difícil será realizar una prueba estadísticamente rigurosa.

- Algunas compensaciones a tener en cuenta cuando pienses en el tamaño de tu grupo de control son que necesitas un número significativamente grande de clientes en tu grupo de control para que cualquier análisis de comportamiento creado sea digno de confianza. Sin embargo, cuanto mayor sea tu grupo de control, menos clientes recibirán tus campañas, lo que supone un inconveniente si utilizas tus campañas para impulsar la interacción y las conversiones.
- El porcentaje ideal dependerá del tamaño de tu audiencia total. Cuanto mayor sea tu audiencia total, menor puede ser tu porcentaje. Sin embargo, si tienes poca audiencia, necesitarás un porcentaje mayor para tu grupo de control.

### Duración del experimento 

#### Elige una duración ideal {#reshuffle}

La duración del experimento antes de reorganizar los miembros del grupo de control depende de lo que estés probando y de los comportamientos de referencia de tus usuarios. Si no estás seguro, un buen punto de partida es un trimestre (tres meses), pero no debes bajar de un mes.

Para determinar la duración adecuada de tu experimento, considera qué preguntas esperas responder. Por ejemplo, ¿quieres ver si hay diferencia en las sesiones? Si es así, piensa en la frecuencia con la que tus usuarios tienen sesiones de forma orgánica. Las marcas cuyos usuarios tienen sesiones todos los días pueden realizar experimentos más cortos que las marcas cuyos usuarios tienen sesiones sólo un par de veces al mes. 

O puede que te interese un evento personalizado, por lo que puede que tu experimento tenga que durar más que un experimento en el que examinas sesiones, si es probable que tus usuarios desencadenen ese evento personalizado con menos frecuencia.

{% alert tip %}
Cuanto más tiempo mantengas el mismo grupo de control, más divergirá del grupo de tratamiento, lo que puede crear un sesgo. Restablecer el grupo de control global reequilibra la población.
{% endalert %}

#### Intenta limitar la finalización prematura de los experimentos

Debes decidir cuánto tiempo vas a realizar tu experimento antes de empezarlo, y luego sólo debes terminar tu experimento y recoger los resultados finales después de alcanzar este punto predeterminado. Terminar tu experimento antes de tiempo, o siempre que veas datos prometedores, introducirá un sesgo.

#### Piensa en métricas valiosas

Ten en cuenta los comportamientos de referencia de las métricas que más te interesan. ¿Te interesan las tasas de compra de los planes de suscripción que se renuevan sólo anualmente? ¿O tienen los clientes un hábito semanal para el evento que te gustaría medir? Piensa en el tiempo que tardan los usuarios en alterar potencialmente sus comportamientos debido a tu mensajería. Después de decidir cuánto tiempo debe durar tu experimento, asegúrate de no terminar tu experimento ni registrar los resultados finales antes de tiempo, o tus conclusiones podrían estar sesgadas.

