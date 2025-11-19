## Uso de bloques de editor de mensajes dentro de la aplicación

Los bloques de editor se encuentran en la sección **Construir** para los mensajes dentro de la aplicación. Para utilizarlos, arrastre un bloque de edición dentro de una columna. Se ajustará automáticamente al ancho de la columna. Cada bloque del editor tiene sus propios ajustes, como el control granular del relleno. El panel de la derecha cambia automáticamente a un panel de propiedades para el elemento de contenido seleccionado.

## Tipos

La siguiente tabla describe cómo puede utilizar cada tipo de bloque editor.

| Apellidos | Descripción |
| --- | --- |
| Título | Introduce un texto de título en el mensaje. |
| Párrafo | Introduce un texto de párrafo en el mensaje. |
| Botón | Añade un botón estándar. Las propiedades de este bloque permiten editar, establecer enlaces y registrar análisis. |
| Botón de radio | Añade una lista de opciones de las que los usuarios pueden seleccionar una. Cuando se envía, el perfil de usuario registra el atributo personalizado asociado. |
| Imagen | Inserta una imagen de la [biblioteca multimedia]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/). |
| Enlace | Inserta un hipervínculo en el que los usuarios puedan hacer clic para navegar a una URL especificada. Puede incrustarse dentro de un texto o ser independiente. |
| Espaciador | Añade espacio o relleno entre otros bloques. |
| Código personalizado | Inserta y ejecuta HTML, CSS o JavaScript personalizados para una personalización avanzada.  |
| Captura telefónica | Inserta un campo de formulario para números de teléfono. Cuando se envía, el usuario queda suscrito al [grupo de suscripción de]({{site.baseurl}}/whatsapp_subscription_groups/) [SMS]({{site.baseurl}}/sms_rcs_subscription_groups/) o [WhatsApp]({{site.baseurl}}/whatsapp_subscription_groups/). |
| Captura de correo electrónico | Inserta un campo de formulario para direcciones de correo electrónico. Cuando se envía, la dirección de correo electrónico se añade al perfil de ese usuario en Braze. |
| Desplegable      | Inserta un desplegable con una lista predefinida de elementos entre los que los usuarios pueden seleccionar uno. Puedes añadir a la lista cualquier cadena de atributos personalizada. |
| Casilla de verificación      | Inserta una casilla de verificación. Si el usuario marca la casilla, el atributo del bloque se establece en `true`. Si se deja sin marcar, su atributo se establece en `false`. |
| Grupo de casillas de verificación| Los usuarios pueden elegir entre las múltiples opciones presentadas. Los valores se establecen o se añaden a un atributo personalizado de matriz definida. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Propiedades

En las tablas siguientes se detallan las propiedades de cada bloque de edición.

### Título y párrafo

| Propiedad | Descripción |
| --- | --- |
| Familia de fuente | El estilo de fuente del texto |
| Peso de fuente | Determina el grosor del texto |
| Tamaño de fuente | Determina el tamaño del texto |
| Altura de la línea | Modifica la distancia entre líneas de texto |
| Espaciado de letras | Modifica la distancia entre cada carácter |
| Alineación de texto | Mueve el texto para alinearlo a la izquierda, al centro, a la derecha o justificado |
| Color de texto | Modifica el color del texto |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Botón

| Propiedad | Descripción |
| --- | --- |
| Ancho del botón | Modifica la anchura del botón para que sea automático o manual |
| Familia de fuente | Este es el estilo de fuente para el texto |
| Peso de fuente | Determina el grosor del texto |
| Tamaño de fuente | Determina el tamaño del texto |
| Espaciado de letras | Modifica la distancia entre cada carácter |
| Alineación de botones | Mueve el botón para orientarlo a la izquierda, al centro o a la derecha |
| Color de texto del botón | Modifica el color del texto del botón |
| Color de fondo | Modifica el color del fondo del botón |
| Estilo del borde | Determina el estilo del borde del botón del botón | 
| Radio del borde | Determina cómo de redondeadas quieres las esquinas |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Imagen

| Propiedad | Descripción |
| --- | --- |
| URL | La dirección de alojamiento de la imagen |
| Alineación | Mueve la imagen para orientarla a la izquierda, al centro o a la derecha |
| Color de fondo | Modifica el color del fondo de la imagen |
| Estilo del borde | Determina el estilo del borde de la imagen | 
| Radio del borde | Determina cómo de redondeadas quieres las esquinas de la imagen |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Enlace

| Propiedad | Descripción |
| --- | --- |
| Familia de fuente | Este es el estilo de fuente para el texto |
| Peso de fuente | Determina el grosor del texto |
| Espaciado de letras | Modifica la distancia entre cada carácter |
| Color de texto | Modifica el color del texto |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Espaciador

| Propiedad | Descripción |
| --- | --- |
| Color de fondo | Modifica el color de fondo del espaciador |
| Altura | Modifica la altura del separador. También puedes modificarlo utilizando los tiradores de redimensionamiento del espaciador. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Código personalizado

| Propiedad | Descripción |
| --- | --- |
| Código personalizado | Te permite añadir, editar o eliminar HTML, CSS y JavaScript para un mensaje in-app. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Captura telefónica

| Propiedad | Descripción |
| --- | --- |
| Grupo de suscripción | El [grupo de suscripción a]({{site.baseurl}}/whatsapp_subscription_groups/) [SMS]({{site.baseurl}}/sms_rcs_subscription_groups/) o WhatsApp al que se suscribirá el usuario recogiendo su número de teléfono, con la opción de recoger números de todos los países. |
| Alineación de texto | Mueve el texto para alinearlo a la izquierda, al centro, a la derecha o justificado |
| Texto del marcador de posición | Un marcador de posición de número de teléfono para mostrar |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Captura de correo electrónico

| Propiedad | Descripción |
| --- | --- |
| Familia de fuente | El estilo de fuente del texto |
| Peso de fuente | Determina el grosor del texto |
| Tamaño de fuente | Determina el tamaño del texto |
| Altura de la línea | Modifica la distancia entre líneas de texto |
| Color de texto | Modifica el color del texto |
| Espaciado de letras | Modifica la distancia entre cada carácter |
| Alineación de texto | Mueve el texto para alinearlo a la izquierda, al centro, a la derecha o justificado |
| Texto del marcador de posición | Una dirección de correo electrónico de marcador de posición para mostrar |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Acciones

Puedes asignar una acción que se produzca cuando un usuario pulse un botón, enlace o imagen del mensaje. También puedes utilizar [Liquid]({{site.baseurl}}/liquid/) para personalizar las acciones. En las tablas siguientes se detallan las acciones de cada bloque de editor.

### Botón

| Acción | Descripción |
| --- | --- |
| Enviar formulario cuando se haya hecho clic en el botón | Envía el formulario y ejecuta el comportamiento seleccionado al hacer clic. Desactiva esta opción para que solo se produzca el comportamiento al hacer clic. |
| Establecer comportamientos separados para cada plataforma | Personaliza el comportamiento del botón para cada plataforma por separado. |
| Comportamiento al hacer clic | Determina la acción cuando el usuario hace clic en el botón, como cerrar el mensaje, abrir la URL web, hacer un enlace profundo a una página específica de la aplicación, ir a otra página o [solicitar permiso push]({{site.baseurl}}/push_primer/). |
| Registrar atributos o eventos personalizados | Determina si al hacer clic en el botón se actualizará el perfil del usuario con datos personalizados. También puedes seleccionar el identificador para los informes. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Imagen

Para las especificaciones de imagen, consulta nuestras [especificaciones de imagen de mensajes dentro de la aplicación]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/image_specs/#in-app-messages).

| Acción | Descripción |
| --- | --- |
| Texto alternativo | La copia escrita que aparece en lugar de una imagen si ésta no se carga. Los lectores de pantalla anuncian el texto alternativo para explicar las imágenes, así que utiliza un lenguaje sencillo para proporcionar información clave sobre una imagen. |
| Enviar formulario cuando se haya hecho clic en la imagen | Envía el formulario y ejecuta el comportamiento seleccionado al hacer clic. Desactiva esta opción para que solo se produzca el comportamiento al hacer clic. |
| Establecer comportamientos separados para cada plataforma | Personaliza el comportamiento de la imagen para cada plataforma por separado. |
| Comportamiento al hacer clic | Determina la acción cuando el usuario hace clic en la imagen, como cerrar el mensaje, abrir la URL web, hacer un enlace profundo a una página específica de la aplicación, ir a otra página o [solicitar permiso push]({{site.baseurl}}/push_primer/). |
| Registrar atributos o eventos personalizados | Determina si al hacer clic en la imagen se actualizará el perfil del usuario con datos personalizados. También puedes seleccionar el identificador para los informes. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Enlace

| Acción | Descripción |
| --- | --- |
| URL | El hipervínculo para navegar a |
| Identificador para la elaboración de informes | Determina qué identificador se utiliza para informar |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

