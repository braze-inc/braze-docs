---
nav_title: Centro de preferencias de correo electrónico arrastrar y soltar
article_title: Centro de preferencias de correo electrónico arrastrar y soltar
alias: "/dnd_preference_center/"
description: "Esta página de referencia explica cómo crear un centro de preferencias de correo electrónico con el editor de arrastrar y soltar."
page_order: 2
---

# Crea un centro de preferencias de correo electrónico con arrastrar y soltar

> Con el editor de arrastrar y soltar, puedes crear y personalizar un centro de preferencias para ayudar a gestionar qué usuarios reciben determinados tipos de comunicación. Puedes tener hasta 100 centros de preferencias por espacio de trabajo.

{% multi_lang_include drag_and_drop/drag_and_drop_access.md variable_name='dnd editors' %}

## Paso 1: Crear un centro de preferencias de correo electrónico

Crea un centro de preferencias accediendo a **Audiencia** > **Centros de preferencias de correo electrónico**.

Aquí se mostrará una lista de centros de preferencias personalizados. Selecciona **Crear nuevo** para crear un nuevo centro de preferencias, o selecciona el nombre de uno existente para realizar cambios.

\![Una lista de centros de preferencias personalizados con el nombre, descripción, tipo, estado, fecha de última edición y creado por el usuario.]({% image_buster /assets/img/preference_center/preference_center1.png %})

## Paso 2: Nombre del centro de preferencia de correo electrónico

Los nombres de los centros de preferencias sólo pueden contener caracteres alfanuméricos, guiones o guiones bajos. El nombre que proporciones determinará la sintaxis de la etiqueta de Liquid generada. 

Esta etiqueta de Liquid puede incluirse en cualquier campaña de correo electrónico saliente o paso en Canvas y dirigirá a los usuarios al centro de preferencias.

\![Un ejemplo de Liquid para un centro de preferencias.]({% image_buster /assets/img/preference_center/preference_center2.png %})

## Paso 3: Añadir grupos de suscripción al centro de preferencias

Selecciona **Iniciar editor** para empezar a diseñar tu centro de preferencias en el editor de arrastrar y soltar.

### Definir los grupos de suscripción disponibles

Para determinar qué grupos de suscripción deben mostrarse en el centro de preferencias, selecciona el botón **\+ Añadir grupos de suscripción** para lanzar un modal en el que se pueden seleccionar los grupos de suscripción deseados. Después de seleccionarlos, selecciona el botón **Añadir grupos de suscripción** para añadirlos al centro de preferencias.

Puedes configurar aún más los grupos de suscripción seleccionados seleccionando el bloque inteligente y ajustando las propiedades del bloque.
- Ajustar el orden de los grupos de suscripción
- Añadir o eliminar grupos de suscripción adicionales
- Incluye descripciones
- Añade o elimina una casilla de verificación **Suscribirse a todos** que suscribirá al usuario a todos los grupos de suscripción mostrados en este bloque
- Añade o elimina una casilla de verificación **Cancelar suscripción de todos** que cancelará la suscripción del usuario de todos los grupos de suscripción mostrados en este bloque

\![Un ejemplo de un centro de preferencias con las opciones de suscribirse a todos los mensajes, la mensajería, el boletín y los correos electrónicos semanales, o cancelar la suscripción a todos.]({% image_buster /assets/img/preference_center/preference_center3.png %}){: style="max-width:38%;"}\![]({% image_buster /assets/img/preference_center/preference_center4.png %}){: style="max-width:45%;"}

El botón **Cancelar suscripción a todo**, situado en la parte inferior de la plantilla, no es extraíble y [cancelará globalmente]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-states) la [suscripción]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-states) del usuario a la recepción de cualquier mensaje de correo electrónico.

## Paso 4: Personaliza el centro de preferencias utilizando el editor de arrastrar y soltar

### Configurar estilos comunes

Puedes configurar determinados estilos para que se apliquen en todos los bloques relevantes de tu centro de preferencias desde la pestaña **Estilos comunes**. Los estilos configurados en esta sección se utilizan en todo tu mensaje, excepto cuando los anulas para un bloque específico. Para facilitar el diseño, te recomendamos que configures los estilos a nivel de página antes de personalizar los estilos a nivel de bloque.

Un ejemplo de configuración de estilo común para texto, botones y enlaces.]({% image_buster /assets/img/preference_center/preference_center5.png %}){: style="max-width:45%;"}

{% alert tip %}
Para volver a los estilos comunes, selecciona el botón "X" en las propiedades individuales de los bloques. A continuación, selecciona el contenedor de mensajes, el botón "X" de mensaje o el fondo del editor.
{% endalert %}

## Arrastrar y soltar componentes del centro de preferencias

El editor de arrastrar y soltar utiliza dos componentes clave para que la composición del centro de preferencias sea rápida y sencilla: filas y bloques. Todos los bloques deben colocarse en fila.

{% tabs %}
{% tab Rows %}

Las filas son unidades estructurales que definen la composición horizontal de una sección del mensaje mediante celdas.

\![Opción para seleccionar el tipo de fila de tu mensaje.]({% image_buster /assets/img/preference_center/preference_center6.png %}){: style="max-width:45%;"}

Cuando se selecciona una fila, puedes añadir o eliminar el número de columnas que necesites en la sección Personalización de columnas para colocar distintos elementos de contenido uno junto a otro. También puedes deslizar para ajustar el tamaño de las columnas existentes.

Opciones para personalizar las propiedades de tu columna, como el color de fondo, el estilo del borde, el radio del borde y el relleno.]({% image_buster /assets/img/preference_center/preference_center7.png %}){: style="max-width:45%;"}

Como práctica recomendada, da formato a las propiedades de las filas y columnas antes de dar formato a los bloques dentro de las filas. Puedes ajustar el espaciado y la alineación en muchos lugares, por lo que empezar desde la base facilita la edición sobre la marcha.

{% endtab %}
{% tab Blocks %}

Los bloques representan distintos tipos de contenido que puedes utilizar en tu mensaje. Arrastra uno dentro de un segmento de fila existente, que se ajustará automáticamente a la anchura de la celda.

\![Opción para seleccionar bloques, incluyendo título, párrafo, botón, imagen y espaciador.]({% image_buster /assets/img/preference_center/preference_center8.png %}){: style="max-width:45%;"}

Cada bloque tiene su propia configuración, como el control granular del relleno. El panel de la derecha cambia automáticamente a un panel de estilo para el elemento de contenido seleccionado. Para más información, consulta [Propiedades del bloque de editor]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/editor_blocks/).

Si utilizas el bloque Código personalizado en tu centro de preferencias, es posible que los marcos en línea no se generen en el código personalizado cuando se entreguen a tus usuarios.

{% endtab %}
{% endtabs %}

## Paso 5: Personaliza tu página de confirmación

¡No olvides personalizar la página de confirmación! Puedes editar esta página seleccionando **Página de confirmación** en la parte superior de la ventana del editor de arrastrar y soltar. Esta página se mostrará a los usuarios después de actualizar sus preferencias utilizando el centro de preferencias. Las mismas capacidades de estilo anteriores se aplican también a esta página.

\![Ejemplo de página de confirmación para comunicar que se han actualizado las preferencias del usuario.]({% image_buster /assets/img/preference_center/preference_center9.png %}){: style="max-width:65%;"}

## Paso 6: Vista previa e inicia tu centro de preferencias

Puedes previsualizar tu centro de preferencias seleccionando la pestaña **Vista previa** dentro del editor. Sin embargo, la funcionalidad de prueba está desactivada. Después de editar tu centro de preferencias, puedes cerrar el editor seleccionando el botón **Hecho**.

Verás una vista previa tanto del centro de preferencias como de la página de confirmación. Selecciona **Guardar como Borrador** para volver a este centro **de** preferencias más tarde, o si estás satisfecho, selecciona **Iniciar Centro de Preferencias**.

Al iniciar el centro de preferencias, se te pedirá que confirmes el nombre, ya que no se puede editar después de iniciarlo. Después de confirmar el nombre, el centro de preferencias se iniciará y estará listo para su uso.

## Utilizar el centro de preferencias

{% multi_lang_include alerts/important_alerts.md alert='Preference Center warning' %}

Para colocar un enlace al centro de preferencias en tus correos electrónicos, copia la etiqueta de Liquid del centro de preferencias deseado seleccionando el icono **Copiar Liquid**.

\![La opción Copiar Liquid en la fila de un centro de preferencias.]({% image_buster /assets/img/preference_center/preference_center10.png %}){: style="max-width:75%;"}

Añade la etiqueta de Liquid en el lugar deseado de tu correo electrónico, de forma similar a como se insertan [las URL para cancelar suscripción]({{site.baseurl}}/user_guide/message_building_by_channel/email/custom_email_footer/#adding-a-custom-unsubscribe-link).

## Tratamiento de errores

Si se produce un error cuando un usuario selecciona **Guardar** en un centro de preferencias, se le mostrará el siguiente mensaje de error predeterminado, que no se puede personalizar ni adaptar en el editor. Sin embargo, la localización de los mensajes de error sigue siendo posible en estas páginas. 

Aparece un error con la nota "Se ha producido un problema al guardar tus preferencias. Inténtalo de nuevo".]({% image_buster /assets/img/preference_center/preference_center11.png %}){: style="max-width:55%;"}

