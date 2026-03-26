---
nav_title: Vista previa de las rutas de usuario
article_title: Vista previa de las rutas de usuario
page_order: 0.3
alias: /preview_user_paths/
description: "Esta página explica cómo puedes obtener una vista previa de las rutas de usuario en Canvas."
Tool:
  - Canvas
---

# Vista previa de las rutas de usuario en Canvas

> Experimenta el recorrido de Canvas que has creado para tus usuarios. Esto incluye una vista previa de los mensajes que recibirán tus usuarios y el momento en que los recibirán. Estas ejecuciones de prueba actúan como garantía de calidad de que tus mensajes se envían a la audiencia correcta, todo ello antes de enviar tu Canvas.

## Crear una ejecución de prueba

Sigue estos pasos para obtener una vista previa de tu recorrido de usuario:

1. Ve a tu constructor de Canvas. Guarda los cambios no guardados y resuelve los errores.
2. Selecciona **Test Canvas** en el pie de página.
3. Selecciona un usuario de prueba.
4. (Opcional) Selecciona un destinatario para la prueba.
5. Selecciona **Run Test**.

Puedes ejecutar una vista previa si no tienes permiso para editar un Canvas, pero esta vista previa se ejecuta con los cambios no guardados, si los hay.

### Pasos admitidos

Se admiten los siguientes pasos:
- Mensaje 
- Ruta de audiencia
- División de decisiones
- Demora
- Ruta de acción
- Ruta de experimentos
- Actualización de usuario (solo en el editor de interfaz de usuario, lo que significa que se omiten los pasos que utilizan el editor JSON)

Si la prueba coincide con un tipo de paso que no aparece en la lista anterior, se omite el paso no compatible y el usuario de prueba continúa con el siguiente paso compatible.

### Detalles del paso en Canvas

Para ver más detalles sobre los criterios de entrada, selecciona **Ver más**. Los pasos con segmentación muestran los criterios cumplidos o no cumplidos. Los mensajes también muestran esto para las validaciones de entrega y la elegibilidad del canal. Los pasos de mensaje muestran qué canales se enviaron y cuáles no.

### Liquid

Braze procesa la lógica de Liquid durante una ejecución de prueba, incluso si no envías un mensaje de prueba real. Esto significa que la [lógica de cancelación de mensajes]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/#aborting-messages) y otra lógica de Liquid se reflejan y podrían afectar al recorrido del usuario en Canvas.

Si tu vista previa envía el último paso de tu recorrido de usuario en lugar de cancelarlo, es posible que la vista previa esté utilizando la hora actual como la hora que se está evaluando para Liquid, y no la hora real en la que el usuario estaría en el paso según la hora de entrada en Canvas.

## Vistas previas para la temporización

En el caso de los Canvas planificados, el usuario de prueba entra a la siguiente hora de entrada planificada. En el caso de los Canvas basados en acciones con fechas de inicio, el usuario de prueba ingresa en la fecha y hora de inicio. 

Aunque siguen aplicándose las horas de inicio predeterminadas, la hora de entrada se puede configurar en todas las instancias, lo que significa que puedes simular una fecha pasada o futura. Sin embargo, no puedes realizar pruebas antes de la fecha de inicio ni después de la fecha de finalización del Canvas.

Los pasos de mensaje y demora muestran el momento en el que un usuario progresaría o recibiría el mensaje sin necesidad de reconfigurar las demoras. Ten en cuenta que, aunque los pasos indican si se utiliza Intelligent Timing, esta vista previa de la ruta del usuario no calcula una estimación para un usuario de prueba.

En el caso de los Canvas con un desencadenante de acción como "cambio en el valor del atributo personalizado", Braze intenta simular el cambio estableciendo temporalmente el atributo del usuario en el desencadenante como vacío **solo para la ejecución de prueba del Canvas** (esto no afecta al perfil de usuario). Esto tiene como objetivo comprobar que el atributo cambia desde su valor actual.

## Cuándo entran y salen los usuarios

Los usuarios de prueba entran en la vista previa aunque no sean elegibles en la vida real. Si no son elegibles, puedes ver por qué no han cumplido los criterios. Cuando un usuario de prueba entra en la vista previa, asumimos que ha cumplido los criterios de la audiencia objetivo y ha realizado los criterios del desencadenante de acción. Por ejemplo, para un Canvas que utiliza eventos personalizados en los criterios de entrada, se asume que el usuario de prueba ha realizado el evento personalizado tal y como se esperaba en los criterios de entrada. Sin embargo, si el mismo evento personalizado se utiliza en otra parte del Canvas (como en los criterios de salida), ten en cuenta cómo podría afectar esto a tu ruta de usuario.

Los eventos, los desencadenantes de API, los atributos personalizados y las propiedades de entrada de Canvas que se asume que permiten a un usuario de prueba entrar en Canvas no se actualizan en el perfil de usuario real y no persisten más allá de la ejecución de la prueba. Por ejemplo, durante las pruebas, cuando se utiliza un atributo personalizado como desencadenante de Canvas, los criterios de desencadenamiento se aplican a la vista previa del usuario **como si** este hubiera desencadenado el cambio del atributo personalizado.

### Consideración

Si pruebas una ruta de acción con acciones que se corresponden con criterios de salida (incluidas las propiedades del evento), se desencadenan los criterios de salida y finaliza la ejecución de la prueba. Si pruebas un paso de mensaje que se corresponde con los criterios de salida, estos se desencadenan y la ejecución de la prueba finaliza. 

En este momento, no puedes seleccionar un evento o propiedad específicos dentro de una ruta de acción para activar los criterios de salida (solo la ruta en su conjunto). Si un usuario puede cumplir varios criterios de salida, se muestra como resultado el primero que se procese y que cumpla.

## Rutas de experimentos y variantes en Canvas

- Para los Canvas con variantes de nivel superior, selecciona una variante al inicio de la prueba.
- Para las rutas de experimentos, selecciona la variante por la que progresa el usuario cuando el usuario de prueba se encuentra con el paso.
- Para las rutas de experimentos que utilizan ruta personalizada o variante ganadora, aunque hay un periodo de demora durante el cual el usuario de prueba espera en un paso de mensaje, esta demora no se tiene en cuenta, ya que Braze asume que el usuario avanzó por la variante seleccionada inmediatamente.

## Envíos de prueba

Puedes optar por enviar mensajes de prueba a un grupo de prueba interno o a un usuario individual a medida que se completa la ejecución de la prueba. Esto significa que solo se envían los mensajes que el usuario encuentra a lo largo de la ruta de prueba. Los destinatarios reciben mensajes con sus atributos de forma predeterminada, pero puedes anularlos con los atributos del usuario de prueba.

Para enviar todos los mensajes de prueba de un Canvas a la vez, independientemente de la ruta, y sin vista previa de la ruta, puedes seleccionar **Send All Test Messages** en la pestaña **Test Sends**.

## Capacidad de respuesta

Los pasos en Canvas responden a la temporización al previsualizar los recorridos del usuario. Las actualizaciones realizadas a través del paso Actualización de usuario se reflejan en los pasos posteriores del flujo, pero no se aplican al perfil de usuario real. Los efectos de que un usuario entre en una variante se reflejan en los pasos futuros de una vista previa.

Del mismo modo, los filtros reconocen las acciones que se produjeron como resultado de la interacción del usuario de prueba con otros pasos en Canvas. Por ejemplo, este modo de vista previa reconoce que un usuario se encontró con un paso de mensaje que se "envió" anteriormente en el Canvas, y reconoce que el usuario de prueba "realizó una acción" para avanzar por una ruta de acción.

Consulta los [criterios de salida]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/exit_criteria) para obtener más detalles sobre el comportamiento receptivo.

## Contenido conectado

El contenido conectado se ejecuta si está incluido en Canvas. Esto significa que si pruebas un Canvas que tiene llamadas a contenido conectado o bloques de contenido que contienen contenido conectado, el Canvas puede enviar las llamadas a contenido conectado, lo que modificaría los datos referenciados en otras campañas o Canvas.

Al previsualizar las rutas de usuario, considera la posibilidad de eliminar el contenido conectado que altera los perfiles de usuario o los datos referenciados en otros Canvas o campañas.

## Webhooks

Los webhooks se ejecutan cuando se envían mensajes de prueba, pero no durante la ejecución de la prueba. De forma similar al contenido conectado, considera la posibilidad de eliminar webhooks que alteren perfiles de usuario o datos referenciados en otros Canvas o campañas.

## Variables de contexto y grupos semilla

Para un paso de mensaje con correo electrónico como canal de mensajería, los grupos semilla envían copias semilla de los correos electrónicos cuando un usuario llega a este paso en Canvas. Estas copias semilla no se envían como parte de los recorridos de Canvas propios de los destinatarios del grupo semilla, por lo que Braze no ejecuta [pasos de contexto]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context) ni evalúa variables de contexto para esos destinatarios. Si el contenido de tu correo electrónico hace referencia a variables de contexto, los destinatarios del grupo semilla reciben una copia semilla sin esos datos completados. Para probar mensajes que dependen de datos de variables de contexto, usa la vista previa de **Test Canvas** con envíos de prueba en lugar de grupos semilla.

## Caso de uso

En este escenario, el Canvas está configurado para dirigirse a usuarios que no han tenido una sesión en una aplicación. Este recorrido incluye un paso de mensaje con un correo electrónico de bienvenida, un paso de demora fijado en un día y un paso de rutas de audiencia que se divide en dos rutas: usuarios con al menos una sesión y el resto. Dependiendo de la ruta de audiencia en la que se encuentre el usuario, se envía el siguiente paso de mensaje.

![Un ejemplo de Canvas con un paso de mensaje, un paso de demora, un paso de rutas de audiencia y dos pasos de mensaje.]({% image_buster /assets/img/preview_user_path_example.png %}){:style="max-width:70%"}

Dado que nuestro usuario de prueba cumple los criterios de entrada del Canvas, puede entrar en el Canvas y recorrer el recorrido del usuario. Sin embargo, como nuestro usuario de prueba no ha abierto la aplicación en el último día del calendario, continúa por la ruta "El resto" y recibe una notificación push que dice: "¡Última oportunidad! Completa tu primera tarea para obtener una bonificación exclusiva".

![La sección "Resultados de la prueba" muestra que el usuario de prueba ha cumplido los criterios de entrada y ofrece un resumen de su recorrido, incluyendo los pasos que se le enviaron.]({% image_buster /assets/img/preview_user_path_results_example.png %})