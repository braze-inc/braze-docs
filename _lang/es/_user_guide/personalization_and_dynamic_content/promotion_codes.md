---
nav_title: Códigos promocionales
article_title: Códigos promocionales
page_order: 5
alias: "/promotion_codes/"
description: "Este artículo de referencia explica cómo crear listas de códigos promocionales y añadirlos a sus campañas y lienzos."

---

# Códigos de promoción

> Los códigos promocionales -también llamados códigos de promoción- son una excelente forma de mantener el interés de los usuarios impulsando las interacciones con un fuerte énfasis en las compras.

Con la funcionalidad Braze Liquid, ofrecemos una forma de hacer que el uso generalizado de códigos de promoción sea muy sencillo, permitiendo que los mensajes se extraigan ahora de la lista de promociones que usted proporcionó, de forma automática e intuitiva. La función de códigos promocionales ofrece fechas de caducidad de hasta seis meses y admite hasta 20 millones de códigos individuales por lista.

{% alert important %}
Los códigos promocionales no pueden enviarse en mensajes in-app.
{% endalert %}

## Crear una lista de códigos promocionales

### Paso 1: Vaya a la sección Código de promoción

![][1]{: style="float:right;max-width:30%;margin-left:15px;"}

En el panel de control, vaya a **Configuración de datos** > **Códigos de promoción** y, a continuación, seleccione **Crear lista de códigos de promoción**.

{% alert note %}
Si utiliza la [navegación anterior]({{site.baseurl}}/navigation), encontrará **los Códigos de promoción** en **Integraciones**.
{% endalert %}

### Paso 2: Nombra y crea tu código de promoción

Asigne un nombre a su lista de códigos promocionales y añada una descripción opcional.

![][2]{: style="max-width:90%"}

A continuación, cree un fragmento de código para el código de promoción. Este fragmento de código será el que utilizará como referencia en Liquid para mostrar este conjunto específico de códigos de promoción. Asegúrese de que se trata de un fragmento de código que no se está utilizando ya en otra lista.

{% alert important %}
Los fragmentos distinguen entre mayúsculas y minúsculas. Por ejemplo, "Cumple_promo" y "cumple_promo" se reconocerán como dos fragmentos diferentes.
{% endalert %}

![][3]{: style="max-width:90%"}

{% alert warning %}
No puedes cambiar el fragmento de código después de guardarlo.
{% endalert %}

### Paso 3: Opciones de código promocional

Cada lista de códigos promocionales tiene una fecha y hora de caducidad correspondientes que se establecen al crearla. La duración máxima de caducidad es de seis meses en el futuro a partir del día en que creas o editas tu lista. Dentro de ese plazo, puedes cambiar y actualizar la fecha de caducidad repetidamente. Esta fecha de caducidad se aplicará a todos los códigos añadidos a esta lista. Una vez caducados, los códigos se eliminarán del sistema Braze y no se enviará ningún mensaje que invoque el fragmento de código de esa lista.

![][4]{: style="max-width:90%"}

También tienes la opción de configurar alertas de umbral opcionales y personalizadas. Si se configuran, estas alertas enviarán un correo electrónico al destinatario designado cuando la lista se esté quedando sin códigos promocionales disponibles en esta lista o cuando su lista de códigos promocionales esté a punto de caducar. El destinatario recibirá una notificación al día.

![][5]

### Paso 4: Carga del código de promoción

Braze no gestiona la creación ni el canje de códigos, lo que significa que debes generar tus códigos promocionales en un archivo CSV y subirlos a Braze. Asegúrate de que el archivo CSV sigue estas directrices:

- Incluye una columna para códigos promocionales.
- Tiene un código promocional por fila.

Puede utilizar nuestra integración con [Voucherify]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/voucherify/) o [Talon.One]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/talonone/) para crear y exportar códigos promocionales.

{% alert note %}
El tamaño máximo del archivo es de 100 MB y el tamaño máximo de la lista es de 20MM de códigos no utilizados. Si descubre que se ha cargado un archivo incorrecto, cargue uno nuevo y el anterior será sustituido.
{% endalert %}

![][6]

Una vez finalizada la carga, seleccione **Guardar lista** para guardar todos los datos y códigos que acaba de introducir.

![][7]

Tras seleccionar Guardar, aparecerá una nueva fila en el **Historial de importaciones**. Para actualizar la tabla y comprobar si la importación ha finalizado, seleccione <span style="font-size: 14px;margin-bottom: .5rem;height: 16px;width: 16px;" class="fas fa-sync" ></span> **Sync** en la parte superior de la tabla.

![][8]

{% alert note %}
Los archivos más grandes tardarán unos minutos en importarse. Mientras esperas, puedes salir de la página y trabajar en algo mientras se realiza la importación. Cuando finalice la importación, verá que el estado cambia a **Completado** en la tabla.
{% endalert %}

#### Actualizar una lista de códigos promocionales

Para actualizar una lista, seleccione una de las listas existentes. Puede cambiar el nombre, la descripción, la caducidad de la lista y los umbrales de alerta. También puede añadir más códigos a la lista cargando nuevos archivos y seleccionando **Actualizar lista**.

Todos los códigos de la lista tendrán la misma caducidad, independientemente de la fecha de importación.

### Paso 5: Utilizar códigos de promoción

Para enviar códigos promocionales en mensajes, seleccione **Copiar fragmento** para copiar el fragmento de código que estableció al crear su lista de códigos promocionales.

![][9]{: style="max-width:70%"}

A partir de ahí, puedes pegar este código en un mensaje dentro del panel de control.

![][10]{: style="max-width:70%"}

Con [Liquid][11], puede insertar en un mensaje uno de los códigos de promoción exclusivos del archivo CSV cargado. Ese código se marcará como enviado en el backend Braze para garantizar que ningún otro mensaje envíe ese mismo código. 

Cuando se utiliza un fragmento de código en una campaña multicanal o en un paso de Canvas, cada usuario recibe siempre un código único. Para los distintos pasos de un Canvas, cada usuario recibe varios códigos de promoción.

Si un usuario concreto es elegible para recibir un código a través de más de un canal, este usuario recibirá el mismo código a través de cada canal. Por ejemplo, si un usuario recibe dos mensajes a través de dos canales, sólo recibirá un código. Lo mismo ocurre a efectos de notificación: se enviará un código, que el usuario recibirá a través de los dos canales. Por ejemplo, para un paso en Canvas multicanal, el usuario solo utilizaría un código.

{% alert important %}
Si no quedan códigos promocionales disponibles al enviar mensajes de prueba o en directo desde una campaña que extrae códigos promocionales, el mensaje no se enviará.
{% endalert %}

#### Envío de mensajes de prueba con códigos promocionales

Los envíos de prueba y los envíos de correo electrónico de grupos de siembra utilizarán códigos promocionales a menos que se solicite lo contrario. Póngase en contacto con su gestor de cuenta Braze para actualizar el comportamiento de esta función, de modo que los códigos promocionales no se utilicen durante los envíos de prueba y los envíos de correo electrónico de grupos de semillas.

## Determinar cuántos códigos se han utilizado

Puede encontrar el recuento de códigos restantes en la columna **Restantes** de la lista de códigos de promoción, situada en la página **Códigos de promoción**.

![][12]{: style="max-width:90%"}

Este recuento de códigos también se puede encontrar al volver a visitar una página de lista de códigos de promoción preexistente. 

![][13]{: style="max-width:50%"}

## Envíos multicanal y monocanal

Para las campañas multicanal y de envío único y los Lienzos, todos los códigos de promoción referenciados en el Líquido de un mensaje se deducen para ser utilizados **antes de** enviar el mensaje para asegurarse de que ocurre lo siguiente:

- En un mensaje multicanal se utilizan los mismos códigos de promoción en todos los canales.
- Los códigos promocionales adicionales no se utilizan si un mensaje falla o se cancela.

Si un usuario tiene dos listas de códigos promocionales referenciadas en un mensaje que está dividido por una etiqueta de lógica condicional Liquid, se seguirán deduciendo todos los códigos promocionales, independientemente del flujo condicional que siga el usuario.

Si un usuario entra en un nuevo paso en Canvas o vuelve a entrar en un Canvas, y el fragmento de código promocional Liquid se aplica de nuevo para un mensaje a ese usuario, se utilizará un nuevo código promocional.

### Casos de uso

Para el siguiente ejemplo, se deducirán ambas listas de códigos de promoción `vip-deal` y `regular-deal`. Aquí está el Liquid:

{% raw %}
```
{% if user.is_vip %}
  {% promotion('vip-deal') %}
{% else %}
  {% promotion('regular-deal') %}
{% endif %} 
```
{% endraw %}

Braze recomienda cargar más códigos de promoción de los que calcula que se utilizarán. Si una lista de códigos de promoción caduca o se agotan los códigos de promoción, se cancelarán los mensajes posteriores.

{% alert tip %}
**He aquí una analogía de cómo se utilizan los códigos promocionales en Braze.** <br><br>Imagina que enviar tu mensaje es como enviar una carta por correo postal. Entregas la carta a un empleado y éste ve que tu carta debe incluir un cupón. El empleado saca el primer cupón de la pila y lo añade al sobre. El empleado envía la carta, pero por alguna razón, la carta se pierde en el correo (y el cupón también se ha perdido). <br><br>En este caso, Braze es el empleado de correos y tu código promocional es el cupón. No podemos recuperarlo después de que haya sido retirado de la pila de códigos de promoción, independientemente del resultado del webhook.
{% endalert %}

## Preguntas más frecuentes

### ¿Qué canales de mensajería puedo utilizar con los códigos promocionales?

Actualmente, los códigos de promoción son compatibles con correo electrónico, push móvil, push web, tarjetas de contenido, webhook, SMS y WhatsApp. Las campañas Braze Transactional Email y los mensajes in-app no admiten actualmente códigos promocionales.

### ¿Consumirán mis códigos promocionales los envíos de prueba y los envíos iniciales?

Por defecto, los envíos de prueba y los envíos de correo electrónico del grupo inicial utilizarán códigos de promoción por usuario, por envío de prueba. Sin embargo, puede ponerse en contacto con su gestor de cuenta Braze para actualizar este comportamiento y no utilizar códigos promocionales durante las pruebas.

### ¿Cómo funcionan los códigos promocionales en una campaña multicanal o en un paso de Canvas?

Los códigos de promoción se deducen antes de enviar el mensaje. Si los canales de mensajería de la campaña o Canvas envían, esto puede provocar que se utilice el código de promoción por motivos como las horas de silencio, los límites de tarifa, la limitación de frecuencia, los criterios de salida, etc. Sin embargo, si se envía alguno de los canales de mensajes, se utilizará un solo código de promoción.

### ¿Qué ocurre si tengo varios fragmentos de Liquid que hacen referencia a la misma lista de códigos promocionales en mi mensaje?

El mismo código promocional será la plantilla para todas las instancias del fragmento de código Liquid en tu mensaje.

### ¿Qué ocurre cuando una lista de códigos promocionales caduca o está vacía?

Si el mensaje debería haber contenido un código promocional de una lista vacía o caducada, el mensaje se cancelará.

Si el mensaje contiene Lógica líquida que inserta condicionalmente un código de promoción, el mensaje sólo se cancelará si debería haber contenido un código de promoción. Si el mensaje no debería haber contenido un código de promoción, el mensaje se enviará normalmente.

[1]:{% image_buster /assets/img/promocodes/promocode1.png %}
[2]:{% image_buster /assets/img/promocodes/promocode2.png %}
[3]:{% image_buster /assets/img/promocodes/promocode3.png %}
[4]:{% image_buster /assets/img/promocodes/promocode4.png %}
[5]:{% image_buster /assets/img/promocodes/promocode5.png %}
[6]:{% image_buster /assets/img/promocodes/promocode6.png %}
[7]:{% image_buster /assets/img/promocodes/promocode7.png %}
[8]:{% image_buster /assets/img/promocodes/promocode8.png %}
[9]:{% image_buster /assets/img/promocodes/promocode9.png %}
[10]:{% image_buster /assets/img/promocodes/promocode10.png %}
[11]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/
[12]: {% image_buster /assets/img/promocodes/promocode11.png %}
[13]: {% image_buster /assets/img/promocodes/promocode12.png %}
