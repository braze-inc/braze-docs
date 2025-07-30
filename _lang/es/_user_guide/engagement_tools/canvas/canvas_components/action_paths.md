---
nav_title: Rutas de acción 
article_title: Rutas de acción 
alias: /action_paths/
page_order: 0.1
page_type: reference
description: "En este artículo de referencia se explica cómo utilizar Rutas de acción, un componente que permite ordenar a los usuarios en función de sus acciones."
tool: Canvas
---

# Rutas de acción 

> Las Rutas de Acción en Canvas te permiten ordenar a tus usuarios en función de sus acciones. 

![Un paso en ruta de acción en un viaje de usuario de Canvas.]({% image_buster /assets/img/canvas_actionpath.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

Utilizando las Rutas de Acción, puedes:

* Personalizar las rutas de los usuarios en función de una acción específica, incluidos los eventos de participación del usuario y los eventos personalizados.
* Retener a los usuarios durante un tiempo determinado para priorizar su próxima ruta en función de sus acciones durante este periodo de evaluación.

## Crear una ruta de acción

Para crear una ruta de acción, añada un componente a su lienzo. Arrastre y suelte el componente desde la barra lateral, o seleccione el botón <i class="fas fa-plus-circle"></i> más en la parte inferior de un paso y seleccione **Rutas de acción**. 

### Configuración de acción

En la **Configuración de la acción**, establezca la **Ventana de evaluación** para determinar cuánto tiempo se retiene a los usuarios en el paso. De modo predeterminado, los usuarios son evaluados en el plazo de un día, aunque puedes ajustar esta ventana por segundos, minutos, horas, días y semanas en función de tu Canvas. El plazo máximo de evaluación de una vía de acción es de 31 días.

En **la Configuración de la acción**, también puede activar el orden de clasificación de los componentes activando la opción **Avanzar usuarios según orden de clasificación**.

![La configuración de la acción con una ventana de evaluación de 1 día.]({% image_buster /assets/img/actionpath_settings.png %})

Por defecto, **la clasificación** está desactivada. Cuando un usuario entra en la ruta de acción y realiza el evento desencadenante asociado a cualquier grupo de acciones, avanzará inmediatamente por el grupo de acciones correspondiente. Si un usuario no realiza un evento desencadenante, avanzará a través del grupo por defecto **Todos los demás** al final del periodo de evaluación.

Cuando se activa **Usuarios avanzados según orden de clasificación**, significa que **la Clasificación** está activada. Por lo tanto, todos los usuarios serán retenidos hasta el final de la ventana de evaluación. Al final del periodo de evaluación, los usuarios avanzarán por el grupo de acción de mayor prioridad al que puedan optar al final de la ventana de evaluación. Los usuarios que no realicen ninguna de las acciones durante la ventana de evaluación avanzarán a través del grupo por defecto **Todos los demás**.

#### Mensajes dentro de la aplicación

Tenga en cuenta que cuando el disparador del grupo de acciones es iniciar una sesión y el siguiente paso es un mensaje in-app, el usuario tendrá que realizar dos inicios de sesión para recibir el mensaje in-app. La primera sesión asigna al usuario al grupo de acciones dentro de la ruta de acción, y la segunda sesión activa el mensaje in-app.

#### Ejemplo de clasificación

Supongamos que tiene una ruta de acción con un periodo de evaluación de un día con dos grupos de acción: Grupo 1 y Grupo 2. El Grupo 1 tiene un evento desencadenante "Iniciar sesión", y el Grupo 2 tiene "Realizar compra". Si **la clasificación** está activada, todos los usuarios de la ruta de acción quedan "retenidos" durante un día. Al final del día, si un usuario ha iniciado una sesión y ha realizado una compra, entonces avanza a la ruta de rango más alto. En este caso, el usuario pasaría al Grupo 1. 

En el ejemplo anterior, si **la clasificación** está desactivada y cuando un usuario realiza uno de los eventos desencadenantes ("Iniciar sesión" o "Realizar compra"), ese usuario avanza en el grupo de acciones correspondiente en función de la acción desencadenante.

Tenga en cuenta que las propiedades de las entradas del lienzo difieren de las propiedades de los eventos. Las propiedades de entrada del lienzo son propiedades del evento que activó el lienzo. Estas propiedades sólo se pueden utilizar en el primer paso completo de un lienzo cuando se utiliza el flujo de trabajo original del lienzo. Cuando se utiliza el Flujo del lienzo, las Propiedades de entrada persistentes están activadas y permiten que las propiedades de entrada se reutilicen en todo el lienzo. Por el contrario, las propiedades de evento se originan a partir de un evento o acción que se produce a medida que el usuario avanza en su flujo de trabajo.

### Grupos de acción

Añada un activador o varios activadores para definir sus grupos de acciones. Aquí puede seleccionar una serie de desencadenantes como, por ejemplo, si los usuarios:

- Realizar una compra
- Iniciar una sesión
- Realiza un [evento personalizado]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)
- Realizar un evento de conversión
- Agregar una dirección de correo electrónico
- Cambiar el valor de un atributo personalizado (no atributos personalizados anidados)
- Actualizar su estado de suscripción o de grupo de suscripción
- Interactuar con una campaña o tarjeta de contenido
- Escribir una ubicación
- Desencadenar una geovalla
- Enviar un mensaje entrante SMS o WhatsApp

![Un grupo de acción denominado "Grupo 1" para los usuarios que realizan cualquier compra.]({% image_buster /assets/img/actionpath_group.png %})

En la configuración de cada grupo de acción, también tienes la opción de seleccionar la casilla **Quiero que este grupo salga del Canvas**, lo que significa que los usuarios de este grupo saldrán del Canvas al final del periodo de evaluación.

### Lienzos con posibilidad de readmisión

Si los usuarios entran varias veces en una ruta de acción y tienen varias entradas en la ruta de acción al mismo tiempo, el comportamiento esperado varía en función del estado **del Ranking**.

| Clasificación | Comportamiento de la ruta de acción |
|---|--------------|
| **Desactivado** | Cuando se realice una acción relevante, Braze deduplicará las entradas y hará avanzar inmediatamente la entrada más antigua por el grupo de acciones relevante. <br><br/> Cuando no se realiza una acción relevante, todas las entradas avanzarán al final de la ventana de evaluación correspondiente. No se producirá ninguna deduplicación. |
| **Activado** | Todas las candidaturas avanzarán al final de la ventana de evaluación correspondiente. No se producirá ninguna deduplicación. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Ten en cuenta que las clasificaciones no son [editables después del lanzamiento]({{site.baseurl}}/post-launch_edits/).


