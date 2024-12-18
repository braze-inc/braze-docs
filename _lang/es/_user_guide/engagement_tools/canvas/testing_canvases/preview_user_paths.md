---
nav_title: Vista previa de las rutas de usuario
article_title: Vista previa de las rutas de usuario
page_order: 0.3
alias: /preview_user_paths/
description: "Este artículo de referencia explica cómo previsualizar las rutas de usuario en Canvas."
Tool:
  - Canvas
---

# Vista previa de las rutas de usuario en Canvas

> Experimenta el recorrido de Canvas que has creado para tus usuarios. Esto incluye una vista previa de la sincronización y los mensajes que recibirán. Estas ejecuciones de prueba actúan como garantía de calidad de que sus mensajes se envían a la audiencia correcta, todo ello antes de enviar su Canvas.

## Iniciar una prueba

Sigue estos pasos para obtener una vista previa de tu recorrido de usuario:

1. Ve a tu constructor de Canvas. Guarde los cambios no guardados y resuelva los errores.
2. Seleccione **Lienzo de prueba** en el pie de página.
3. Seleccione un usuario de prueba.
4. (opcional) Seleccione un destinatario para la prueba.
5. Seleccione **Ejecutar prueba**.

Puede ejecutar una vista previa si no tiene permiso para editar un Lienzo, pero esta vista previa se ejecutará con los cambios no guardados si los hubiera.

### Pasos admitidos

Se admiten los siguientes pasos:
- Mensaje 
- Ruta de audiencia
- División de decisiones
- Demora
- Ruta de acción
- Ruta del experimento
- Actualización de usuario (sólo en el editor de interfaz de usuario, lo que significa que se omitirán los pasos utilizando el editor JSON)

Si la prueba se solapa con un tipo de paso que no figura en la lista anterior, se omitirá el paso no admitido y el usuario de la prueba continuará con el siguiente paso admitido.

### Detalles del paso de lona

Para ver más detalles sobre los criterios de entrada, seleccione **Ver más**. Los pasos con segmentación mostrarán los criterios cumplidos o no cumplidos. Los mensajes también mostrarán esto para las validaciones de entrega y la elegibilidad del canal. Los pasos de los mensajes mostrarán qué canales se enviaron y cuáles no.

### Liquid

La lógica Liquid se procesará durante una ejecución de prueba, aunque no envíes un mensaje de prueba real. Esto significa que la [lógica del mensaje de cancelación]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/#aborting-messages) y otra lógica de Liquid se reflejan y podrían afectar al recorrido del usuario de Canvas.

## Vistas previas para la sincronización

Para los lienzos programados, el usuario de la prueba entrará a la siguiente hora de entrada programada. Para los lienzos basados en acciones con fechas de inicio, el usuario de la prueba entrará en la fecha y hora de inicio. 

Aunque se siguen aplicando las horas de inicio predeterminadas, la hora de entrada es configurable en todos los casos, lo que significa que puede simular una fecha en el pasado o en el futuro. Sin embargo, no puede realizar pruebas antes de la fecha de inicio ni después de la fecha de finalización del lienzo.

Los pasos de Mensaje y Retraso muestran el momento en el que un usuario progresaría o recibiría el mensaje sin necesidad de reconfigurar los retrasos. Tenga en cuenta que aunque los pasos indicarán si se utiliza la Temporización Inteligente, esta vista previa de la ruta del usuario no calcula una estimación para un usuario de prueba.

## Cuando los usuarios entran y salen

Los usuarios de prueba entrarán en la vista previa aunque no sean elegibles en la vida real. Si no reúnen los requisitos, se puede entender por qué no habrían cumplido los criterios. Puede ver los resultados en la barra lateral para cuando los usuarios entran y salen del Canvas.

- Si prueba una Ruta de Acción con acciones que corresponden a criterios de salida (incluyendo propiedades de eventos), se activarán los criterios de salida y finalizará la ejecución de la prueba.
- Si prueba un paso de Mensaje que corresponde a criterios de salida, se activarán los criterios de salida y finalizará la ejecución de la prueba.
- En este momento, no puede seleccionar un evento o propiedad específicos dentro de una ruta de acción para activar los criterios de salida (sólo la ruta en su conjunto). Si un usuario puede cumplir varios criterios de salida, se mostrará como resultado el primero que se procese y que cumpla.
- Los eventos, los activadores de la API y las propiedades de la entrada del lienzo no se aplican en función de la entrada del lienzo. No afectarán a los resultados de los pasos siguientes.

## Rutas de experimentos y variantes en Canvas

- Para los lienzos con variantes de nivel superior, seleccione una variante al inicio de la prueba.
- Para Experiment Paths, seleccione la variante por la que progresa el usuario cuando el usuario de prueba se encuentra con el paso.
- Para las Rutas de Experimento que utilizan Ruta Personalizada o Variante Ganadora, aunque hay un periodo de retraso durante el cual el usuario de prueba espera en un paso de Mensaje, este retraso no se tiene en cuenta ya que Braze asume que el usuario avanzó por la variante seleccionada inmediatamente.

## Envíos de prueba

Puede optar por enviar mensajes de prueba a un grupo de prueba interno o a un usuario individual a medida que se completa la ejecución de la prueba. Esto significa que sólo se enviarán los mensajes que el usuario encuentre a lo largo de la ruta de prueba. Por defecto, los destinatarios recibirán los mensajes con sus propios atributos, pero puede sustituirlos por los atributos del usuario de prueba.

Para enviar todos los mensajes de prueba de un lienzo a la vez, independientemente de la ruta y sin previsualizar la ruta, puede seleccionar **Enviar todos los mensajes de prueba** en la pestaña **Envíos de prueba**.

## Capacidad de respuesta

Los pasos del lienzo responden a la temporización al previsualizar los recorridos del usuario. Las actualizaciones realizadas a través del paso Actualización de usuario se reflejan en los pasos posteriores del flujo, pero no se aplican al perfil de usuario real. Los efectos de que un usuario introduzca una variante se reflejan en los pasos futuros de una vista previa.

Del mismo modo, los filtros reconocerán las acciones que se produjeron como resultado de la interacción del usuario de prueba con otros pasos del lienzo. Por ejemplo, este modo de vista previa reconoce que un usuario encontró un paso de Mensaje que fue "enviado" anteriormente en el Canvas, y reconocerá que el usuario de prueba "tomó acción" para avanzar a través de una ruta de acción.

Consulte los [Criterios de salida]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/exit_criteria) para obtener más detalles sobre el comportamiento receptivo.

## Contenido conectado

El Contenido Conectado se ejecutará si está incluido en el Lienzo. Si su Lienzo incluye Contenido Conectado, elimine el Contenido Conectado que esté configurado para alterar perfiles de usuario o datos a los que se haga referencia en otros Lienzos o campañas. También puede optar por no previsualizar el recorrido del usuario.

## Webhooks

Los webhooks se ejecutarán cuando se envíen los mensajes de prueba, pero no durante la ejecución de la prueba. De forma similar al Contenido Conectado, considere eliminar los webhooks que estén configurados para alterar los perfiles de usuario o los datos a los que se hace referencia en otros Canvases o campañas.

## Casos de uso

En este escenario, el Canvas está configurado para dirigirse a usuarios que no han tenido una sesión en una app. Este recorrido incluye un paso de Mensaje con un correo electrónico de bienvenida, un paso de Retraso fijado en un día y un paso de Rutas de audiencia que se divide en dos rutas: usuarios con al menos una sesión y todos los demás. Dependiendo de la ruta de audiencia en la que se encuentre el usuario, se enviará el siguiente paso de Mensaje.

![][1]{:style="max-width:70%"}

Dado que nuestro usuario de prueba cumple los criterios de entrada del Canvas, puede entrar en el Canvas y recorrer el recorrido del usuario. Sin embargo, como nuestro usuario de prueba no ha abierto la aplicación en el último día natural, seguirá por el camino "Todos los demás" y recibirá una notificación push con el texto siguiente: "¡Última oportunidad! Completa tu primera tarea para obtener una bonificación exclusiva".

![][2]

[1]: {% image_buster /assets/img/preview_user_path_example.png %}
[2]: {% image_buster /assets/img/preview_user_path_results_example.png %}
