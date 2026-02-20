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

> Experimenta el recorrido de Canvas que has creado para tus usuarios. Esto incluye una vista previa de la sincronización y los mensajes que reciben tus usuarios. Estas ejecuciones de prueba actúan como garantía de calidad de que sus mensajes se envían a la audiencia correcta, todo ello antes de enviar su Canvas.

## Crear una prueba de funcionamiento

Sigue estos pasos para obtener una vista previa de tu recorrido de usuario:

1. Ve a tu constructor de Canvas. Guarde los cambios no guardados y resuelva los errores.
2. Seleccione **Lienzo de prueba** en el pie de página.
3. Seleccione un usuario de prueba.
4. (Opcional) Selecciona un destinatario para la prueba.
5. Seleccione **Ejecutar prueba**.

Puedes ejecutar una vista previa si no tienes permiso para editar un Canvas, pero esta vista previa se ejecuta con los cambios no guardados si los hubiera.

### Pasos admitidos

Se admiten los siguientes pasos:
- Mensaje 
- Ruta de audiencia
- División de decisiones
- Demora
- Ruta de acción
- Ruta del experimento
- Actualización de usuario (sólo en el editor UI, lo que significa que se omiten los pasos que utilizan el editor JSON)

Si la prueba se solapa con un tipo de paso que no aparece en la lista anterior, se omite el paso no admitido y el usuario de prueba continúa con el siguiente paso admitido.

### Detalles del paso de lona

Para ver más detalles sobre los criterios de acceso, selecciona **Ver más**. Los pasos con segmentación muestran los criterios cumplidos o no cumplidos. Los mensajes también lo muestran para las validaciones de entrega y la elegibilidad del canal. Los pasos de los mensajes muestran qué canales se enviaron y cuáles no.

### Liquid

Braze procesa la lógica Liquid durante una ejecución de prueba, aunque no estés enviando un mensaje de prueba real. Esto significa que la [lógica del mensaje de cancelación]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/#aborting-messages) y otra lógica de Liquid se reflejan y podrían afectar al recorrido del usuario de Canvas.

Si tu vista previa envía el último paso de tu recorrido de usuario en lugar de abortarlo, es posible que la vista previa esté utilizando la hora actual como la hora que se está probando para la evaluación de Liquid, y no la hora real en la que el usuario estaría en el paso según la hora de entrada en Canvas.

## Vistas previas para la sincronización

Para los Lienzos programados, el usuario de prueba entra a la siguiente hora de entrada programada. En los Lienzos basados en acciones con fechas de inicio, el usuario de prueba entra en la fecha y hora de inicio. 

Aunque se siguen aplicando las horas de inicio predeterminadas, la hora de entrada es configurable en todas las instancias, lo que significa que puedes simular una fecha en el pasado o en el futuro. Sin embargo, no puedes hacer pruebas antes de la fecha de inicio ni después de la fecha de finalización del Canvas.

Los pasos de Mensaje y Retraso muestran el momento en el que un usuario progresaría o recibiría el mensaje sin necesidad de reconfigurar los retrasos. Ten en cuenta que, aunque los pasos indican si se utiliza Intelligent Timing, esta vista previa de la ruta del usuario no calcula una estimación para un usuario de prueba.

Para los Canvas con una acción desencadenante como "cambio en el valor del atributo personalizado", Braze intenta simular el cambio configurando temporalmente el atributo del usuario en el desencadenante para que esté en blanco **sólo durante la ejecución de prueba del Canvas** (esto no afecta al perfil de usuario). Sirve para comprobar que el atributo cambia respecto a su valor actual.

## Cuando los usuarios entran y salen

Los usuarios de prueba entran en la vista previa aunque no sean elegibles en la vida real. Si no son elegibles, puedes ver por qué no han cumplido los criterios. Cuando un usuario de prueba entra en la vista previa, suponemos que ha cumplido los criterios de la audiencia objetivo y ha realizado los criterios de la acción desencadenante. Por ejemplo, para un Canvas que utiliza eventos personalizados en los criterios de entrada, se supone que el usuario de prueba ha realizado el evento personalizado tal y como se esperaba en los criterios de entrada. Sin embargo, si el mismo evento personalizado se utiliza en otra parte del Canvas (como en los criterios de salida), ten en cuenta cómo podría afectar esto a tu ruta de usuario.

Los eventos, desencadenantes de API, atributos personalizados y propiedades de entrada al Canvas que se supone que permiten a un usuario de prueba entrar en el Canvas no se actualizan en el perfil de usuario real y no persisten más allá de la ejecución de la prueba. Por ejemplo, durante las pruebas, cuando se utiliza un atributo personalizado como desencadenante de Canvas, los criterios de desencadenamiento se aplican a la vista previa del usuario **como si** éste hubiera desencadenado el cambio del atributo personalizado.

### Consideración

Si pruebas una ruta de acción con acciones que corresponden a criterios de salida (incluidas las propiedades del evento), se desencadenan los criterios de salida y finaliza la ejecución de la prueba. Si pruebas un paso de Mensaje que corresponde a criterios de salida, se desencadenan los criterios de salida y finaliza la ejecución de la prueba. 

En este momento, no puede seleccionar un evento o propiedad específicos dentro de una ruta de acción para activar los criterios de salida (sólo la ruta en su conjunto). Si un usuario puede cumplir varios criterios de salida, se mostrará como resultado el primero que se procese y que cumpla.

## Rutas de experimentos y variantes en Canvas

- Para los lienzos con variantes de nivel superior, seleccione una variante al inicio de la prueba.
- Para Experiment Paths, seleccione la variante por la que progresa el usuario cuando el usuario de prueba se encuentra con el paso.
- Para las Rutas de Experimento que utilizan Ruta Personalizada o Variante Ganadora, aunque hay un periodo de retraso durante el cual el usuario de prueba espera en un paso de Mensaje, este retraso no se tiene en cuenta ya que Braze asume que el usuario avanzó por la variante seleccionada inmediatamente.

## Envíos de prueba

Puede optar por enviar mensajes de prueba a un grupo de prueba interno o a un usuario individual a medida que se completa la ejecución de la prueba. Esto significa que sólo se envían los mensajes que el usuario encuentra a lo largo de la ruta de prueba. Por defecto, los destinatarios reciben los mensajes con sus atributos, pero puedes sustituirlos por los atributos del usuario de prueba.

Para enviar todos los mensajes de prueba de un Canvas a la vez, independientemente de la ruta, y sin vista previa de la ruta, puedes seleccionar **Enviar todos los mensajes de prueba** en la pestaña **Envíos de prueba**.

## Capacidad de respuesta

Los pasos del lienzo responden a la temporización al previsualizar los recorridos del usuario. Las actualizaciones realizadas a través del paso Actualización de usuario se reflejan en los pasos posteriores del flujo, pero no se aplican al perfil de usuario real. Los efectos de que un usuario introduzca una variante se reflejan en los pasos futuros de una vista previa.

Del mismo modo, los filtros reconocen las acciones que se produjeron como resultado de la interacción del usuario de prueba con otros pasos en Canvas. Por ejemplo, este modo de vista previa reconoce que un usuario se encontró con un paso en Canvas de Mensaje que fue "enviado" anteriormente, y reconoce que el usuario de prueba "tomó medidas" para avanzar por una ruta de acción.

Consulte los [Criterios de salida]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/exit_criteria) para obtener más detalles sobre el comportamiento receptivo.

## Contenido conectado

El Contenido conectado se ejecuta si está incluido en el Canvas. Esto significa que si pruebas un Canvas que tiene llamadas a Contenido conectado o Bloques de contenido que contienen Contenido conectado, el Canvas puede enviar las llamadas a Contenido conectado, lo que modificaría los datos referenciados en otras campañas o Canvases.

Al previsualizar las rutas de usuario, considera la posibilidad de eliminar el Contenido conectado que altera los perfiles de usuario o los datos referenciados en otros Lienzos o campañas.

## Webhooks

Los webhooks se ejecutan cuando se envían los mensajes de prueba, pero no durante la ejecución de la prueba. De forma similar al Contenido conectado, considera la posibilidad de eliminar webhooks que alteren perfiles de usuario o datos referenciados en otros Lienzos o campañas.

## Casos de uso

En este escenario, el Canvas está configurado para dirigirse a usuarios que no han tenido una sesión en una app. Este recorrido incluye un paso de Mensaje con un correo electrónico de bienvenida, un paso de Retraso fijado en un día y un paso de Rutas de audiencia que se divide en dos rutas: usuarios con al menos una sesión y todos los demás. Dependiendo de la ruta de audiencia en la que se encuentre un usuario, se enviará el siguiente paso Mensaje.

![Un ejemplo de Canvas con un paso de Mensaje, un paso de Retraso, un paso de Rutas de audiencia y dos pasos de Mensaje.]({% image_buster /assets/img/preview_user_path_example.png %}){:style="max-width:70%"}

Dado que nuestro usuario de prueba cumple los criterios de entrada del Canvas, puede entrar en el Canvas y recorrer el recorrido del usuario. Sin embargo, como nuestro usuario de prueba no ha abierto la aplicación en el último día del calendario, sigue por el camino "Todos los demás" y recibe una notificación push que dice: "¡Última oportunidad! Completa tu primera tarea para obtener una bonificación exclusiva".

![La sección "Resultados de la prueba" muestra que el usuario de prueba ha cumplido los criterios de entrada y proporciona un resumen de su recorrido, incluidos los pasos que se le enviaron.]({% image_buster /assets/img/preview_user_path_results_example.png %})
