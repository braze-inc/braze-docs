---
nav_title: Soporte de Braze
article_title: Soporte
description: "Esta página te ayudará a localizar el portal de soporte de Braze para enviar tus comentarios sobre los productos Braze. Sólo podrán acceder a esta página los clientes de Braze."
alias: /braze_support/
page_type: reference
search_rank: 7
---

# [![Curso de Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/the-braze-support-portal/){: style="float:right;width:120px;border:0;" class="noimgborder"}Soporte de Braze

## Accede al portal de soporte

Para ponerte en contacto con el equipo de soporte de Braze, navega hasta el panel de Braze. En el panel, selecciona **Asistencia** > **Obtener ayuda**.

![El desplegable "Soporte" con la opción de obtener ayuda.]({% image_buster /assets/img_archive/get_help.png %}){: style="max-width:60%;"}

Dependiendo de tus permisos Braze y de si eres un contacto de soporte designado (premium), se te redirigirá al portal de soporte Braze, donde puedes enviar y seguir casos, o a nuestro formulario de soporte estándar. Si no estás seguro de ser un contacto de soporte de Braze, ponte en contacto con el administrador de Braze de tu empresa, el director de éxito de Braze o el propietario de la cuenta.

## Añadir contactos de asistencia designados

Los contactos de soporte designados pueden acceder a todos los casos de soporte de tu empresa, independientemente de quién los haya enviado. Puedes establecer usuarios como contactos de soporte designados directamente desde la página **Editar usuario**. 

1. Ve a **Configuración** > **Usuarios de la empresa** y, a continuación, busca al usuario por su nombre o dirección de correo electrónico.
2. Selecciona el nombre de usuario o pasa el ratón por encima de la fila del nombre de usuario para que aparezca un menú. 
3. En el menú, selecciona **Editar** para ser redirigido a la página **Editar usuario**.
4. Marca la casilla de verificación de **Establecer este usuario como contacto de soporte designado para el portal de soporte de Braze**.

![La casilla de verificación para configurar a un usuario como contacto de soporte designado.]({% image_buster /assets/img_archive/designated_support_contact.png %}){: style="max-width:70%;"}

El número de contactos de soporte designados que puedes establecer depende de tu límite de contactos. Ponte en contacto con tu administrador del éxito del cliente para obtener más información.

### Obtener acceso

Después de designar a un usuario como contacto de asistencia, el portal de asistencia de Braze le enviará un correo electrónico de bienvenida con instrucciones para configurar su acceso.

## Proporcionar capturas de pantalla de la consola para desarrolladores

Cuando te comuniques con el servicio de asistencia, puede que necesites acceder a tu consola para desarrolladores para proporcionar información adicional:
- Chrome
  1. Haz clic con el botón derecho del ratón en la página web y selecciona **Inspeccionar**.
  2. Selecciona la pestaña **Consola** en la ventana que se abre.
  3. Haz una captura de pantalla de la pestaña de la consola.<br><br>
- Firefox
  1. Haz clic con el botón derecho del ratón en la página web y selecciona **Inspeccionar elemento**.
  2. Selecciona la pestaña **Consola** en la ventana que se abre.
  3. Haz una captura de pantalla de la pestaña de la consola.<br><br>
- Safari
  1. Ve a Safari en la barra de menús de la parte superior de la pantalla y selecciona **Preferencias**.
  2. Selecciona **Avanzado** y, a continuación, marca la casilla situada junto a **Mostrar menú Desarrollar en la barra de menús**. A continuación, puedes salir de la ventana.
  3. Haz clic con el botón derecho del ratón en la página web y selecciona **Inspeccionar elemento**.
  4. Selecciona la pestaña **Consola** en la ventana que se abre.
  5. Haz una captura de pantalla de la pestaña de la consola.

## Buenas prácticas para enviar un caso de soporte

### Proporciona toda la información posible

Cuanta más información puedas ofrecer, mejor. Incluye datos específicos como el espacio de trabajo, la URL de la campaña o segmento, y cualquier ID externo relevante. Esto puede ayudarnos a solucionar tus problemas de forma más eficaz.

### Proporcionar una muestra de usuarios

Comparte una muestra de usuarios en lugar de todo el segmento afectado. Proporcionar un número menor de usuarios nos ayuda a reducir nuestro alcance y a acelerar nuestras investigaciones.

### Adjuntar registros de red (registros HAR)

Si te pones en contacto con el servicio de asistencia, será útil que el usuario afectado recopile los registros de red (registros HAR) de su navegador mientras se produce el problema. Esto mostrará las peticiones de red entre el navegador y el servidor para los componentes individuales de una página web, así como el panel de Braze que el usuario está intentando abrir.

Haz que el usuario afectado haga lo siguiente:

1. Abre sus herramientas de desarrollador. Si utilizas Chrome, puedes hacerlo utilizando el atajo de teclado `option` + `⌘` + `J` (en macOS). Si utilizas Windows o Linux, puedes hacerlo con el atajo `shift` + `CTRL` + `J`.
2. Selecciona **Red** > **Obtener/XHR** o **XHR**.
3. Haz una grabación o captura de pantalla que muestre el **Nombre**, **Estado**, **Tamaño** y **Hora** de los elementos.<br><br>![La pestaña "Fetch/XHR" en un navegador Chrome.]({% image_buster /assets/img/network_xhr.png %}){: style="max-width:60%;"}

A continuación, adjunta la grabación o captura de pantalla del usuario al ticket de soporte. Esta información puede ayudar a la investigación de Apoyo.

### Aclarar el comportamiento esperado frente al real

Cuéntanos qué esperabas y qué ocurrió en realidad. Esto puede ayudarnos a reducir las posibles causas del problema.

### Adjunta imágenes relevantes

Considera la posibilidad de adjuntar una captura de pantalla para ilustrar el problema. Facilitar estas imágenes puede ayudarnos significativamente a comprender el problema y acelerar el proceso de resolución.

### Evaluar el impacto

Selecciona el nivel de gravedad adecuado para ayudarnos a asignar los recursos adecuados para solucionar el problema. 

{% alert important %}
Marcar un problema como "Crítico" significa que tu instancia de producción no funciona y que todo el trabajo en Braze se ha detenido.
{% endalert %}

