---
nav_title: Rutas de acción
article_title: Rutas de acción 
alias: /action_paths/
page_order: 0.1
page_type: reference
description: "Este artículo de referencia explica cómo utilizar las Rutas de acción, un componente que te permite ordenar a los usuarios en función de sus acciones."
tool: Canvas
---

# Rutas de acción 

> Las rutas de acción en Canvas te permiten clasificar a tus usuarios en función de sus acciones. 

\![Un paso en rutas de acción en un viaje de usuario de Canvas.]({% image_buster /assets/img/canvas_actionpath.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

Utilizando las Rutas de acción, puedes:

* Personaliza las rutas de los usuarios en función de una acción concreta, incluidos los eventos de interacción con los usuarios y los eventos personalizados.
* Retener a los usuarios durante un tiempo determinado para priorizar su próxima ruta en función de sus acciones durante este periodo de evaluación.

## Crear una ruta de acción

Para crear una ruta de acción, añade un componente a tu Canvas. Arrastra y suelta el componente desde la barra lateral, o selecciona el botón <i class="fas fa-plus-circle"></i> más en la parte inferior de un paso y selecciona **Rutas de acción**. 

### Configuración de la acción

En la **Configuración de la acción**, establece la **Ventana de evaluación** para determinar cuánto tiempo se retiene a los usuarios en el paso. Por defecto, los usuarios son evaluados en el plazo de un día, pero puedes ajustar esta ventana en segundos, minutos, horas, días y semanas en función de tu Canvas. El plazo máximo de evaluación de una ruta de acción es de 31 días.

Dentro de **la Configuración de la acción**, también puedes activar el orden jerárquico para tus componentes alternando **Avanzar usuarios según orden jerárquico**.

\![La configuración de la acción con una ventana de evaluación de 1 día.]({% image_buster /assets/img/actionpath_settings.png %})

Por defecto, **el Ranking** está desactivado. Cuando un usuario entra en la ruta de acción y realiza el evento desencadenante asociado a cualquier grupo de acción, avanzará inmediatamente por el grupo de acción correspondiente. Si un usuario no realiza un evento desencadenante, avanzará por el grupo predeterminado **Todos los demás** al final del periodo de evaluación.

Cuando se activa **Usuarios avanzados según orden de clasificación**, significa que **la Clasificación** está activada. Así, todos los usuarios serán retenidos hasta el final de la ventana de evaluación. Al final del periodo de evaluación, los usuarios avanzarán por el grupo de acción de mayor prioridad para el que sean elegibles al final de la ventana de evaluación. Los usuarios que no realicen ninguna de las acciones durante la ventana de evaluación avanzarán a través del grupo predeterminado **Todos los demás**.

#### Mensajes dentro de la aplicación

Ten en cuenta que cuando el desencadenante del grupo de aplicaciones inicia una sesión y el siguiente paso es un mensaje dentro de la aplicación, el usuario tendrá que realizar dos inicios de sesión para recibir el mensaje dentro de la aplicación. La primera sesión asigna al usuario al grupo de acción dentro de la ruta de acción, y la segunda sesión desencadena el mensaje dentro de la aplicación.

#### Ejemplo de estado de la clasificación

Supongamos que tienes una ruta de acción con un periodo de evaluación de un día con dos grupos de acción: Grupo 1 y Grupo 2. El Grupo 1 tiene un evento desencadenante "Iniciar Sesión", y el Grupo 2 tiene "Realizar Compra". Si **el Ranking** está activado, todos los usuarios de la ruta de acción quedan "retenidos" durante un día. Al final del día, si un usuario ha iniciado una sesión y ha realizado una compra, entonces avanza a la ruta de rango más alto. En este caso, el usuario avanzaría al Grupo 1. 

En el ejemplo anterior, si **la Clasificación** está desactivada y cuando un usuario realiza uno de los eventos desencadenantes ("Iniciar sesión" o "Realizar compra"), ese usuario avanza en el grupo de acciones correspondiente en función de la acción desencadenante.

Ten en cuenta que las propiedades de entrada del Canvas difieren de las propiedades del evento. Las propiedades de entrada al Canvas son propiedades del evento que desencadenó el Canvas. Estas propiedades sólo pueden utilizarse en el primer paso completo de un Canvas cuando se utiliza el flujo de trabajo original de Canvas. Al utilizar Canvas, se habilitan las propiedades de entrada persistentes, que permiten reutilizar las propiedades de entrada en todo el Canvas. Por el contrario, las propiedades del evento tienen su origen en un acontecimiento o acción que se produce cuando el usuario recorre su flujo de trabajo.

### Grupos de acción

Añade un desencadenante o varios desencadenantes para definir tus grupos de acciones. Aquí, puedes seleccionar una serie de desencadenantes como, por ejemplo, si los usuarios:

- Haz una compra
- Iniciar una sesión
- Realiza un [evento personalizado]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)
- Realiza un evento de conversión
- Añadir una dirección de correo electrónico
- Cambia el valor de un atributo personalizado (incluidas las matrices, pero no los atributos personalizados anidados). Esto incluye añadir un nuevo atributo con un valor a un perfil de usuario por primera vez (cuando el atributo no estaba presente anteriormente).
- Actualizar su estado de suscripción o el estado del grupo de suscripción
- Interactúa con una campaña o tarjeta de contenido
- Introduce una ubicación
- Desencadenar una geovalla
- Enviar un mensaje entrante SMS o WhatsApp

\![Un grupo de acción llamado "Grupo 1" para los usuarios que realizan cualquier compra.]({% image_buster /assets/img/actionpath_group.png %})

En la configuración de cada grupo de acción, también tienes la opción de seleccionar la casilla **Quiero que este grupo salga del Canvas**, lo que significa que los usuarios de este grupo saldrán del Canvas al final del periodo de evaluación.

### Lienzos con reelegibilidad

Si los usuarios entran varias veces en una ruta de acción y tienen varias entradas en la ruta de acción al mismo tiempo, el comportamiento esperado varía en función del estado **del Ranking**.

| Estado de la clasificación | Comportamiento de la ruta de acción |
|---|--------------|
| **Fuera de** | Cuando se realice una acción relevante, Braze deduplicará las entradas y hará avanzar inmediatamente la entrada más antigua por el grupo de acciones relevante. <br><br/> Cuando no se realice una acción relevante, todas las entradas avanzarán al final de la ventana de evaluación correspondiente. No se producirá ninguna deduplicación. |
| **En** | Todas las entradas avanzarán al final de la ventana de evaluación correspondiente. No se producirá ninguna deduplicación. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Ten en cuenta que las clasificaciones no son [editables después del lanzamiento]({{site.baseurl}}/post-launch_edits/).


