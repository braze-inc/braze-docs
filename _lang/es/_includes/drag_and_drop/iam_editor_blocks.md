## Uso de bloques de editor de mensajes dentro de la aplicación

Los bloques de editor se encuentran en la sección **«Crear»** para los mensajes dentro de la aplicación. Para utilizarlos, arrastre un bloque de edición dentro de una columna. Se ajustará automáticamente al ancho de la columna. Cada bloque del editor tiene sus propios ajustes, como el control granular del relleno. El panel de la derecha cambia automáticamente a un panel de propiedades para el elemento de contenido seleccionado.

## Tipos

La siguiente tabla describe cómo puede utilizar cada tipo de bloque editor.

| Apellidos | Descripción |
| --- | --- |
| Título | Introduce un texto de título en el mensaje. |
| Párrafo | Introduce un párrafo de texto en el mensaje. |
| Botón | Añade un botón estándar. Las propiedades de este bloque permiten editar, establecer enlaces y registrar análisis. |
| Botón de radio | Añade una lista de opciones entre las que los usuarios pueden seleccionar una. Cuando se envía, el perfil de usuario registra el atributo personalizado asociado, que debe ser una cadena para poder guardarse. Los atributos personalizados con otros tipos de datos no se guardan en el perfil de usuario. |
| Imagen | Inserta una imagen de la [biblioteca multimedia]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/). |
| Enlace | Inserta un hipervínculo en el que los usuarios pueden hacer clic para navegar a una URL específica. Se puede integrar en el texto o utilizarse de forma independiente. |
| Espaciador | Añade espacio o relleno entre otros bloques. |
| Código personalizado | Inserta y ejecuta HTML, CSS o JavaScript personalizados para una personalización avanzada.  |
| Captura telefónica | Inserta un campo de formulario para números de teléfono. Una vez enviado, el usuario queda suscrito al [grupo de suscripción]({{site.baseurl}}/whatsapp_subscription_groups/) [por]({{site.baseurl}}/sms_rcs_subscription_groups/) [SMS]({{site.baseurl}}/sms_rcs_subscription_groups/) o [WhatsApp]({{site.baseurl}}/whatsapp_subscription_groups/). |
| Captura de correo electrónico | Inserta un campo de formulario para direcciones de correo electrónico. Una vez enviada, la dirección de correo electrónico se añade al perfil de usuario en Braze. |
| Desplegable      | Inserta un menú desplegable con una lista predefinida de elementos entre los que los usuarios pueden seleccionar uno. Puedes añadir cualquier cadena de atributos personalizados a la lista. |
| Casilla de verificación      | Inserta una casilla de verificación. Si el usuario marca la casilla, el atributo del bloque se establece en `true`. Si no se comprueba, tu atributo se establece en `false`. |
| Grupo de casillas de verificación| Los usuarios pueden seleccionar entre varias opciones presentadas. Los valores se establecen o se añaden a un atributo personalizado de matriz definido. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Propiedades

En las tablas siguientes se detallan las propiedades de cada bloque de edición.

### Título y párrafo

| Propiedad | Descripción |
| --- | --- |
| Familia de fuente | El estilo de fuente para el texto |
| Peso de fuente | Determina el grosor del texto. |
| Tamaño de fuente | Determina el tamaño del texto. |
| Altura de la línea | Modifica la distancia entre líneas de texto |
| Espaciado de letras | Modifica la distancia entre cada carácter |
| Alineación de texto | Mueve el texto para alinearlo a la izquierda, al centro, a la derecha o justificado |
| Color de texto | Modifica el color del texto |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Botón

| Propiedad | Descripción |
| --- | --- |
| Ancho del botón | Modifica el ancho del botón para que sea automático o manual. |
| Familia de fuente | Este es el estilo de fuente para el texto. |
| Peso de fuente | Determina el grosor del texto. |
| Tamaño de fuente | Determina el tamaño del texto. |
| Espaciado de letras | Modifica la distancia entre cada carácter |
| Alineación de botones | Mueve el botón hacia la izquierda, el centro o la derecha. |
| Color de texto del botón | Modifica el color del texto del botón. |
| Color de fondo | Modifica el color del fondo del botón. |
| Estilo del borde | Determina el estilo del borde del botón. | 
| Radio del borde | Determina cómo de redondeadas quieres las esquinas |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Imagen

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

| Propiedad | Descripción |
| --- | --- |
| URL | La dirección alojada para la imagen. |
| Alineación | Mueve la imagen hacia la izquierda, el centro o la derecha. |
| Color de fondo | Modifica el color del fondo de la imagen. |
| Estilo del borde | Determina el estilo del borde de la imagen. | 
| Radio del borde | Determina el grado de redondeo que deseas para las esquinas de la imagen. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Enlace

| Propiedad | Descripción |
| --- | --- |
| Familia de fuente | Este es el estilo de fuente para el texto. |
| Peso de fuente | Determina el grosor del texto. |
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

### Captura de teléfono

| Propiedad | Descripción |
| --- | --- |
| Grupo de suscripción | El [grupo de suscripción]({{site.baseurl}}/whatsapp_subscription_groups/) [por]({{site.baseurl}}/sms_rcs_subscription_groups/) [SMS]({{site.baseurl}}/sms_rcs_subscription_groups/) o [WhatsApp]({{site.baseurl}}/whatsapp_subscription_groups/) al que se suscribirá el usuario al recopilar su número de teléfono, con la opción de recopilar números de todos los países. |
| Alineación de texto | Mueve el texto para alinearlo a la izquierda, al centro, a la derecha o justificado |
| Texto del marcador de posición | Un número de teléfono marcador de posición para mostrar. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Captura de correo electrónico

| Propiedad | Descripción |
| --- | --- |
| Familia de fuente | El estilo de fuente para el texto |
| Peso de fuente | Determina el grosor del texto. |
| Tamaño de fuente | Determina el tamaño del texto. |
| Altura de la línea | Modifica la distancia entre líneas de texto |
| Color de texto | Modifica el color del texto |
| Espaciado de letras | Modifica la distancia entre cada carácter |
| Alineación de texto | Mueve el texto para alinearlo a la izquierda, al centro, a la derecha o justificado |
| Texto del marcador de posición | Una dirección de correo electrónico de marcador de posición para mostrar. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Acciones

Puedes asignar una acción que se produzca cuando un usuario pulse un botón, un enlace o una imagen del mensaje. También puedes utilizar [Liquid]({{site.baseurl}}/liquid/) para realizar la personalización de las acciones. En las siguientes tablas se proporcionan detalles sobre las acciones de cada bloque de editor.

### Botón

| Acción | Descripción |
| --- | --- |
| Enviar formulario cuando se haya hecho clic en el botón | Envía el formulario y realiza la acción seleccionada al hacer clic. Desactiva esta opción para que solo se produzca el comportamiento al hacer clic. |
| Establecer comportamientos separados para cada plataforma | Personaliza el comportamiento del botón para cada plataforma por separado. |
| Comportamiento al hacer clic | Determina la acción que se realizará cuando el usuario haga clic en el botón, como cerrar el mensaje, abrir la URL web, realizar un enlace profundo a una página específica de la aplicación, ir a otra página o [solicitar permiso para enviar notificaciones push]({{site.baseurl}}/push_primer/). |
| Registrar atributos o eventos personalizados | Determina si al hacer clic en el botón se actualizará el perfil de usuario con datos personalizados. También puedes seleccionar el identificador para la presentación de informes. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Imagen

Para conocer las especificaciones de las imágenes, consulta las [especificaciones]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/image_specs/#in-app-messages) de [imágenes de mensajes dentro de la aplicación]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/image_specs/#in-app-messages).

| Acción | Descripción |
| --- | --- |
| Texto alternativo | La copia escrita que aparece en lugar de una imagen si ésta no se carga. Los lectores de pantalla leen el texto alternativo para explicar las imágenes, por lo que debes utilizar un lenguaje sencillo para proporcionar información clave sobre una imagen. |
| Enviar formulario cuando se haya hecho clic en la imagen | Envía el formulario y realiza la acción seleccionada al hacer clic. Desactiva esta opción para que solo se produzca el comportamiento al hacer clic. |
| Establecer comportamientos separados para cada plataforma | Personaliza el comportamiento de la imagen para cada plataforma por separado. |
| Comportamiento al hacer clic | Determina la acción que se realizará cuando el usuario haga clic en la imagen, como cerrar el mensaje, abrir la URL web, realizar un enlace profundo a una página específica de la aplicación, ir a otra página o [solicitar permiso para enviar notificaciones push]({{site.baseurl}}/push_primer/). |
| Registrar atributos o eventos personalizados | Determina si al hacer clic en la imagen se actualizará el perfil de usuario con datos personalizados. También puedes seleccionar el identificador para la presentación de informes. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Enlace

| Acción | Descripción |
| --- | --- |
| URL | El hipervínculo para navegar a |
| Identificador para la elaboración de informes | Determina qué identificador se utiliza para la presentación de informes. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

