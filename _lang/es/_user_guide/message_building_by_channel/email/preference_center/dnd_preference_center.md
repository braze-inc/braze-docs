---
nav_title: Centro de preferencias de correo electrónico de arrastrar y soltar
article_title: Centro de preferencias de correo electrónico de arrastrar y soltar
alias: "/dnd_preference_center/"
description: "Esta página de referencia explica cómo crear un centro de preferencias de correo electrónico con el editor de arrastrar y soltar."
page_order: 2
---

# Crear un centro de preferencias de correo electrónico con arrastrar y soltar

> Mediante el editor de arrastrar y soltar, puede crear y personalizar un centro de preferencias para ayudar a gestionar qué usuarios reciben determinados tipos de comunicación. Puede tener hasta 50 centros de preferencia por espacio de trabajo.

{% multi_lang_include drag_and_drop_access.md variable_name='editores dnd' %}

## Paso 1: Crear un centro de preferencias de correo electrónico

Cree un centro de preferencias accediendo a **Audiencia** > **Suscripciones** > **Centro de preferencias de correo electrónico**.

Aquí se mostrará una lista de centros de preferencias personalizados. Seleccione **Crear nuevo** para crear un nuevo centro de preferencias o seleccione el nombre de uno existente para realizar cambios.

![Una lista de centros de preferencias personalizados con el nombre, descripción, tipo, estado, fecha de última edición y creado por el usuario.]({% image_buster /assets/img/preference_center/preference_center1.png %})

## Paso 2: Nombre del centro de preferencias de correo electrónico

Los nombres de los centros de preferencias sólo pueden contener caracteres alfanuméricos, guiones o guiones bajos. El nombre que proporcione determinará la sintaxis de la etiqueta Liquid generada. 

Esta etiqueta Liquid puede incluirse en cualquier campaña de correo electrónico saliente o en los pasos de Canvas y dirigirá a los usuarios al centro de preferencias.

![Un ejemplo de Liquid para un centro de preferencias.]({% image_buster /assets/img/preference_center/preference_center2.png %})

## Paso 3: Añadir grupos de suscripción al centro de preferencias

Seleccione **Iniciar editor** para empezar a diseñar su centro de preferencias en el editor de arrastrar y soltar.

### Definir los grupos de suscripción disponibles

Para determinar qué grupos de suscripción deben mostrarse en el centro de preferencias, seleccione el botón **\+ Añadir grupos de suscripción** para iniciar un modal en el que se pueden seleccionar los grupos de suscripción deseados. Después de seleccionarlos, seleccione el botón **Añadir grupos de suscripción** para añadirlos al centro de preferencias.

Puede configurar aún más los grupos de suscripción seleccionados seleccionando el bloque inteligente y ajustando las propiedades del bloque.
- Ajustar el orden de los grupos de suscripción
- Añadir o eliminar grupos de suscripción adicionales
- Incluir descripciones
- Añada o elimine una casilla de verificación **Suscribirse a todo** que suscribirá al usuario a todos los grupos de suscripción mostrados en este bloque
- Añada o elimine una casilla de verificación **Cancelar suscripción a todo** que cancelará la suscripción del usuario a todos los grupos de suscripción mostrados en este bloque.

![Un ejemplo de un centro de preferencias con las opciones de suscribirse a todos los mensajes, marketing, boletín y correos electrónicos semanales, o cancelar suscripción a todos.]({% image_buster /assets/img/preference_center/preference_center3.png %}){: style="max-width:38%;"} ![]({% image_buster /assets/img/preference_center/preference_center4.png %}){: style="max-width:45%;"}

El botón **Darse de baja de todo**, situado en la parte inferior de la plantilla, es inamovible y [dará de baja globalmente]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-states) al usuario de la recepción de cualquier mensaje de correo electrónico.

## Paso 4: Personaliza el centro de preferencias con el editor de arrastrar y soltar

### Configurar estilos comunes

En la pestaña **Estilos comunes** puede establecer que determinados estilos se apliquen a todos los bloques relevantes de su centro de preferencias. Los estilos definidos en esta sección se utilizan en todo el mensaje, excepto cuando se anulan para un bloque específico. Para facilitar el diseño, recomendamos configurar los estilos a nivel de página antes de personalizar los estilos a nivel de bloque.

![Un ejemplo de configuración de estilo común para texto, botones y enlaces.]({% image_buster /assets/img/preference_center/preference_center5.png %}){: style="max-width:45%;"}

{% alert tip %}
Para volver a los estilos comunes, seleccione el botón "X" en las propiedades de cada bloque. A continuación, selecciona el contenedor de mensajes, el botón "X" de mensaje o el fondo del editor.
{% endalert %}

## Arrastrar y soltar componentes del centro de preferencias

El editor de arrastrar y soltar utiliza dos componentes clave para que la composición del centro de preferencias sea rápida y sencilla: filas y bloques. Todos los bloques deben colocarse en fila.

{% tabs %}
{% tab Filas %}

Las filas son unidades estructurales que definen la composición horizontal de una sección del mensaje mediante celdas.

![Opción para seleccionar el tipo de fila de tu mensaje.]({% image_buster /assets/img/preference_center/preference_center6.png %}){: style="max-width:45%;"}

Cuando se selecciona una fila, puede añadir o eliminar el número de columnas que necesite en la sección Personalización de columnas para colocar diferentes elementos de contenido uno al lado del otro. También puede deslizar para ajustar el tamaño de las columnas existentes.

![Opciones para personalizar las propiedades de tu columna, incluyendo el color de fondo, el estilo del borde, el radio del borde y el relleno.]({% image_buster /assets/img/preference_center/preference_center7.png %}){: style="max-width:45%;"}

Como práctica recomendada, formatee las propiedades de fila y columna antes de formatear los bloques dentro de las filas. Puedes ajustar el espaciado y la alineación en muchos sitios, así que empezar desde la base facilita la edición sobre la marcha.

{% endtab %}
{% tab Bloques %}

Los bloques representan distintos tipos de contenido que puedes utilizar en tu mensaje. Arrastre uno dentro de un segmento de fila existente, que se ajustará automáticamente a la anchura de la celda.

![Opción para seleccionar bloques, incluyendo título, párrafo, botón, imagen y espaciador.]({% image_buster /assets/img/preference_center/preference_center8.png %}){: style="max-width:45%;"}

Cada bloque tiene sus propios ajustes, como el control granular del relleno. El panel de la derecha cambia automáticamente a un panel de estilos para el elemento de contenido seleccionado. Para más información, consulta [Propiedades del bloque de editor]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/editor_blocks/).

Si está utilizando el bloque de código personalizado en su centro de preferencias, es posible que los marcos en línea no se generen en el código personalizado cuando se entreguen a sus usuarios.

{% endtab %}
{% endtabs %}

## Paso 5: Personalice su página de confirmación

No olvides personalizar la página de confirmación. Puede editar esta página seleccionando **Página de confirmación** en la parte superior de la ventana del editor de arrastrar y soltar. Esta página se mostrará a los usuarios después de actualizar sus preferencias utilizando el centro de preferencias. Las mismas posibilidades de estilo anteriores se aplican también a esta página.

![Un ejemplo de página de confirmación para comunicar que se han actualizado las preferencias del usuario.]({% image_buster /assets/img/preference_center/preference_center9.png %}){: style="max-width:65%;"}

## Paso 6: Vista previa e inicio del centro de preferencias

Puede previsualizar su centro de preferencias seleccionando la pestaña **Vista previa** dentro del editor. Sin embargo, la función de prueba está desactivada. Después de editar su centro de preferencias, puede cerrar el editor seleccionando el botón **Hecho**.

Verá una vista previa tanto del centro de preferencias como de la página de confirmación. Seleccione **Guardar como borrador** para volver a este centro de preferencias más tarde o, si está satisfecho, seleccione **Iniciar centro de preferencias**.

Al iniciar el centro de preferencias, se le pedirá que confirme el nombre, ya que no se puede editar después de iniciarlo. Después de confirmar el nombre, el centro de preferencias se iniciará y estará listo para su uso.

## Utilizar el centro de preferencias

{% multi_lang_include preference_center_warning.md %}

Para colocar un enlace al centro de preferencias en sus correos electrónicos, copie la etiqueta Liquid del centro de preferencias deseado seleccionando el icono **Copiar Liquid**.

![La opción Copiar Liquid en la fila de un centro de preferencias.]({% image_buster /assets/img/preference_center/preference_center10.png %}){: style="max-width:75%;"}

Añada la etiqueta Liquid en el lugar deseado de su correo electrónico, de forma similar a como se insertan [las URL de cancelación de suscripción]({{site.baseurl}}/user_guide/message_building_by_channel/email/custom_email_footer/#adding-a-custom-unsubscribe-link).

## Tratamiento de errores

Si se produce un error cuando un usuario selecciona **Guardar** en un centro de preferencias, se le mostrará el siguiente mensaje de error predeterminado, que no puede personalizarse ni modificarse en el editor. Sin embargo, en estas páginas se sigue admitiendo la localización de los mensajes de error. 

![Aparece un error con la nota "Hubo un problema al guardar tus preferencias. Por favor, inténtalo de nuevo"]({% image_buster /assets/img/preference_center/preference_center11.png %}){: style="max-width:55%;"}

