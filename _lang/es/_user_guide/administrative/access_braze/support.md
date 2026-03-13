---
nav_title: Soporte de Braze
article_title: Soporte
page_order: 7
description: "Esta página te ayudará a localizar el portal de soporte de Braze para enviar tus comentarios sobre los productos Braze. Sólo podrán acceder a esta página los clientes de Braze."
alias: /braze_support/
page_type: reference
search_rank: 7
---

# [![](https://learning.braze.com/the-braze-support-portal/)Curso []({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/the-braze-support-portal/){: style="float:right;width:120px;border:0;" class="noimgborder"}de [Braze Learning](https://learning.braze.com/the-braze-support-portal/) soporte de Braze

## Accede al portal de soporte

Para ponerte en contacto con el equipo de soporte de Braze, navega hasta el panel de Braze. En el panel, selecciona **Soporte** técnico > **Obtener ayuda**.

![El menú desplegable «Soporte» con la opción para obtener ayuda.]({% image_buster /assets/img_archive/get_help.png %}){: style="max-width:60%;"}

En función de tus permisos de Braze y de si eres un contacto de asistencia designado, se te redirigirá al portal de soporte de Braze, donde podrás enviar y realizar el seguimiento de los casos, o a nuestro formulario de asistencia estándar. Si no estás seguro de si eres un contacto de soporte de Braze, ponte en contacto con el administrador de Braze de tu empresa, el gestor de éxito de Braze o el propietario de la cuenta.

## Añadir contactos de asistencia designados

Los contactos de asistencia designados pueden acceder a todos los casos de asistencia de tu empresa, independientemente de quién los haya enviado. Puedes configurar usuarios como contactos de soporte designados directamente desde la página **Editar usuario**. 

1. Ve a **Configuración** > **Usuarios de la empresa** y realiza la búsqueda del usuario por su nombre o dirección de correo electrónico.
2. Selecciona el nombre de usuario o pasa el cursor por encima de la fila del nombre de usuario para mostrar un menú. 
3. En el menú, selecciona **Editar** para ser redirigido a la página **Editar usuario**.
4. Marca la casilla para **establecer a este usuario como contacto de asistencia designado para el portal de soporte de Braze**.

![La casilla de verificación para establecer a un usuario como contacto de soporte designado.]({% image_buster /assets/img_archive/designated_support_contact.png %}){: style="max-width:70%;"}

### Obtener acceso

Una vez que se designa a un usuario como contacto de asistencia, el portal de soporte de Braze le envía un correo electrónico de bienvenida con instrucciones para configurar tu acceso.

## Proporcionar capturas de pantalla de la consola para desarrolladores

Cuando te comuniques con el servicio de asistencia, puede que necesites acceder a tu consola para desarrolladores para proporcionar información adicional:
- Chrome
  1. Haz un clic con el botón derecho del ratón en la página web y selecciona **Inspeccionar**.
  2. Selecciona la pestaña **Consola** en la ventana que se abre.
  3. Haz una captura de pantalla de la pestaña de la consola.<br><br>
- Firefox
  1. Haz un clic con el botón derecho del ratón en la página web y selecciona **«Inspeccionar elemento**».
  2. Selecciona la pestaña **Consola** en la ventana que se abre.
  3. Haz una captura de pantalla de la pestaña de la consola.<br><br>
- Safari
  1. Ve a Safari en la barra de menús de la parte superior de la pantalla y selecciona **Preferencias**.
  2. Selecciona **Avanzado** y, a continuación, marca la casilla situada junto a **Mostrar menú Desarrollo en la barra de menús**. A continuación, puedes salir de la ventana.
  3. Haz un clic con el botón derecho del ratón en la página web y selecciona **«Inspeccionar elemento**».
  4. Selecciona la pestaña **Consola** en la ventana que se abre.
  5. Haz una captura de pantalla de la pestaña de la consola.

## Buenas prácticas para enviar un caso de soporte

### Proporciona toda la información posible

Cuanta más información puedas ofrecer, mejor. Incluye datos específicos como el espacio de trabajo, la URL de la campaña o segmento, y cualquier ID externo relevante. Esto puede ayudarnos a solucionar tus problemas de forma más eficaz.

### Proporcionar una muestra de usuarios

Comparte una muestra de usuarios en lugar de todo el segmento afectado. Proporcionar un número menor de usuarios nos ayuda a reducir nuestro alcance y acelerar nuestras investigaciones.

### Adjuntar registros de red (registros HAR)

Si te pones en contacto con el servicio de asistencia técnica, será útil que el usuario afectado recopile los registros de red (registros HAR) de su navegador mientras se produce el problema. Esto mostrará las solicitudes de red entre el navegador y el servidor para los componentes individuales de una página web, así como el panel de Braze que el usuario está intentando abrir.

Pide al usuario afectado que hagas lo siguiente:

1. Abre las herramientas del desarrollador. Si utilizas Chrome, puedes hacerlo con el atajo de teclado`option`  +`⌘`  +`J`  (en MacOS). Si usas Windows o Linux, puedes hacerlo con el atajo`shift`  +`CTRL`  + `J`.
2. Selecciona **Red** > **Obtener/XHR** o **XHR**.
3. Captura una grabación de pantalla o una captura de pantalla que muestre el **nombre**, **el estado**, **el tamaño** y **la hora** de los elementos.<br><br>![La pestaña «Fetch/XHR» en un navegador Chrome.]({% image_buster /assets/img/network_xhr.png %}){: style="max-width:60%;"}

A continuación, adjunta la grabación o captura de pantalla del usuario al ticket de soporte. Esta información puede ayudar a la investigación del servicio de asistencia técnica.

### Aclarar el comportamiento esperado frente al real

Cuéntanos qué esperabas y qué ocurrió en realidad. Esto puede ayudarnos a reducir las posibles causas del problema.

### Adjunta imágenes relevantes

Considera la posibilidad de adjuntar una captura de pantalla para ilustrar el problema. Facilitar estas imágenes puede ayudarnos significativamente a comprender el problema y acelerar el proceso de resolución.

### Evaluar el impacto

Selecciona el nivel de gravedad adecuado para ayudarnos a asignar los recursos adecuados para solucionar el problema. 

{% alert important %}
Marcar un problema como «crítico» significa que tu instancia de producción está inactiva y que todo el trabajo dentro de Braze se ha detenido.
{% endalert %}

## Solución de problemas de acceso

Si recibes un error al iniciar sesión en el portal de soporte de Braze, como `Check your entry`, asegúrate de haber seguido el enlace del correo electrónico de bienvenida para establecer una contraseña para el portal. Si ya lo has hecho o antes podías iniciar sesión en el portal, crea un ticket de soporte.