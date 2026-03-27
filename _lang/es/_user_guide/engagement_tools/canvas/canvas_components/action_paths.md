---
nav_title: Rutas de acción
article_title: Rutas de acción 
alias: /action_paths/
page_order: 1
page_type: reference
description: "En este artículo de referencia se explica cómo utilizar Rutas de acción, un componente que permite ordenar a los usuarios en función de sus acciones."
tool: Canvas
---

# Rutas de acción 

> Las Rutas de Acción en Canvas te permiten ordenar a tus usuarios en función de sus acciones. 

![Un paso de rutas de acción en un recorrido de usuario de Canvas.]({% image_buster /assets/img/canvas_actionpath.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

Utilizando las Rutas de Acción, puedes:

* Personalizar las rutas de los usuarios en función de una acción específica, incluidos los eventos de participación del usuario y los eventos personalizados.
* Retener a los usuarios durante un tiempo determinado para priorizar su próxima ruta en función de sus acciones durante este periodo de evaluación.

## Creación de una ruta de acción

Para crear una ruta de acción, añada un componente a su lienzo. Arrastre y suelte el componente desde la barra lateral, o seleccione el botón <i class="fas fa-plus-circle"></i> más en la parte inferior de un paso y seleccione **Rutas de acción**.

### Configuración de acción

En la **Configuración de la acción**, establezca la **Ventana de evaluación** para determinar cuánto tiempo se retiene a los usuarios en el paso. De modo predeterminado, los usuarios son evaluados en el plazo de un día, aunque puedes ajustar esta ventana por segundos, minutos, horas, días y semanas en función de tu Canvas. El plazo máximo de evaluación de una vía de acción es de 31 días.

En **la Configuración de la acción**, también puede activar el orden de clasificación de los componentes activando la opción **Avanzar usuarios según orden de clasificación**.

![La configuración de la acción con una ventana de evaluación de 1 día.]({% image_buster /assets/img/actionpath_settings.png %})

Por defecto, **la clasificación** está desactivada. Cuando un usuario ingresa en la ruta de acción y realiza el evento desencadenante asociado a cualquier grupo de acciones, avanzas inmediatamente a través del grupo de acciones relevante en función de la **primera acción válida** que realices después de ingresar en el paso. Si un usuario realiza una segunda acción que coincide con un grupo de acciones diferente, no cambia de ruta: la primera acción determina tu ruta. Si un usuario no realiza un evento desencadenante, avanzas al grupo predeterminado **«Todos los demás»** al final del período de evaluación.

Cuando se activa la opción **«Usuarios avanzados según orden de clasificación»**, significa que **la clasificación** está activada. Por lo tanto, todos los usuarios quedan retenidos hasta el final del periodo de evaluación. Al final del periodo de evaluación, los usuarios avanzan al grupo de acción de mayor prioridad al que son elegibles al final del periodo de evaluación. Los usuarios que no realicen ninguna de las acciones durante el periodo de evaluación avanzarán a través del grupo predeterminado **«Todos los demás**».

{% alert tip %}
Para dirigir a los usuarios en función de sus atributos actuales o su pertenencia a un segmento, en lugar de las acciones que realizan, utiliza [las rutas de audiencia]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths/).
{% endalert %}

Ten en cuenta que puedes desencadenar una ruta de acción cuando cambia un objeto de atributo personalizado anidado, pero no para matrices de atributos personalizados anidados ni cambios en los tipos de datos de matrices de objetos.

#### Mensajes dentro de la aplicación

Ten en cuenta que cuando el desencadenante del grupo de acciones inicia una sesión y el siguiente paso es un mensaje dentro de la aplicación, el usuario debe iniciar dos sesiones para recibir el mensaje dentro de la aplicación. La primera sesión asigna al usuario al grupo de acciones dentro de la ruta de acción, y la segunda sesión activa el mensaje in-app.

#### Ejemplo de clasificación

Supongamos que tiene una ruta de acción con un periodo de evaluación de un día con dos grupos de acción: Grupo 1 y Grupo 2. El Grupo 1 tiene un evento desencadenante "Iniciar sesión", y el Grupo 2 tiene "Realizar compra". Si **la clasificación** está activada, todos los usuarios de la ruta de acción quedan "retenidos" durante un día. Al final del día, si un usuario ha iniciado una sesión y ha realizado una compra, entonces avanza a la ruta de rango más alto. En este caso, el usuario pasaría al Grupo 1. 

En el ejemplo anterior, si **la clasificación** está desactivada y un usuario realiza una de las acciones desencadenantes («Iniciar sesión» o «Realizar compra»), ese usuario avanza en el grupo de acciones relevante en función de la acción desencadenante.

Tenga en cuenta que las propiedades de las entradas del lienzo difieren de las propiedades de los eventos. Las propiedades de entrada del lienzo son propiedades del evento que activó el lienzo. Estas propiedades sólo se pueden utilizar en el primer paso completo de un lienzo cuando se utiliza el flujo de trabajo original del lienzo. Al utilizar Canvas, las propiedades de entrada persistentes están habilitadas y permiten que las propiedades de entrada se reutilicen en todo Canvas. Por el contrario, las propiedades de evento se originan a partir de un evento o acción que se produce a medida que el usuario avanza en su flujo de trabajo.

### Grupos de acción

Añada un activador o varios activadores para definir sus grupos de acciones. Aquí puedes seleccionar una serie de desencadenantes, como por ejemplo, si los usuarios:

- Realizar una compra
- Iniciar una sesión
- Realizar un [evento personalizado]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)
- Realizar un evento de conversión
- Agregar una dirección de correo electrónico
- Cambia el valor de un atributo personalizado.
  - Esto incluye añadir un nuevo atributo con un valor al perfil de usuario por primera vez (cuando el atributo no estaba presente anteriormente).
  - Los desencadenadores de atributos no están disponibles para los atributos de matriz.
- Actualizar su estado de suscripción o de grupo de suscripción
- Interactuar con una campaña o tarjeta de contenido
- Escribir una ubicación
- Desencadenar una geovalla
- Enviar un mensaje entrante SMS o WhatsApp

![Un grupo de acción denominado «Grupo 1» para los usuarios que realicen cualquier compra.]({% image_buster /assets/img/actionpath_group.png %})

En cada configuración de grupo de acciones, también tienes la opción de seleccionar la casilla de verificación **Quiero que este grupo salga de Canvas**, lo que significa que los usuarios de este grupo saldrán de Canvas al final del período de evaluación.

### Lienzos con posibilidad de readmisión

Si los usuarios introducen una ruta de acción varias veces y tienen varias entradas en la ruta de acción al mismo tiempo, el comportamiento esperado varía en función del estado **de** **clasificación**.

| Clasificación | Comportamiento de la ruta de acción |
|---|--------------|
| **Desactivado** | Cuando se realiza una acción relevante, Braze deduplica las entradas y realiza el avance inmediato de la entrada más antigua a través del grupo de acciones relevante. <br><br> Cuando no se realiza una acción relevante, todas las entradas avanzan al final de la ventana de evaluación correspondiente. No se produce ninguna deduplicación. |
| **Activado** | Todas las entradas avanzan al final del periodo de evaluación correspondiente. No se produce ninguna deduplicación. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Ten en cuenta que las clasificaciones no son [editables después del lanzamiento]({{site.baseurl}}/post-launch_edits/).
