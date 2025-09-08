---
nav_title: Códigos promocionales
article_title: Códigos promocionales
page_order: 5
toc_headers: h2
alias: "/promotion_codes/"
description: "Este artículo de referencia explica cómo crear listas de códigos promocionales y añadirlos a sus campañas y lienzos."
---

# Códigos de promoción

> Esta página explica cómo crear listas de códigos promocionales y añadirlos a tus campañas y Lienzos.

## Cómo funciona

Los códigos promocionales -también llamados códigos de promoción- son una excelente forma de mantener el interés de los usuarios impulsando las interacciones con un fuerte énfasis en las compras. Puedes crear mensajes que tiren de tu lista de códigos promocionales. 

Cada código promocional tiene una fecha de caducidad de hasta seis meses, y puede eliminarse antes de su caducidad poniéndote en contacto con [el Soporte]({{site.baseurl}}/user_guide/administrative/access_braze/support/). Puedes almacenar y gestionar hasta 20 millones de códigos por lista. Al gestionar y analizar el rendimiento de tus códigos promocionales, puedes tomar decisiones específicas para tus estrategias promocionales y de mensajería.

{% alert important %}
Los códigos promocionales no pueden enviarse en mensajes dentro de la aplicación en Canvas. Si participas en el [acceso anticipado](#promotion-codes-iam-campaigns), los códigos promocionales pueden enviarse en campañas de mensajería dentro de la aplicación.
{% endalert %}

## Crear una lista de códigos promocionales

### Paso 1: Ir a la sección Código promocional

![Botón para crear un código promocional.]({% image_buster /assets/img/promocodes/promocode1.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

1. Desde el panel, ve a **Configuración de datos** > Códigos promocionales.
2. Selecciona **Crear lista de códigos promocionales**.

### Paso 2: Indica el código promocional

1. Asigne un nombre a su lista de códigos promocionales y añada una descripción opcional.
2. A continuación, cree un fragmento de código para el código de promoción. 

Aquí tienes algunos detalles que debes tener en cuenta al crear un fragmento de código:

- Una vez guardados, los fragmentos de código no se pueden editar.
- Los fragmentos distinguen entre mayúsculas y minúsculas. Por ejemplo, "Cumple_promo" y "cumple_promo" se reconocerán como dos fragmentos diferentes.
- Utiliza el nombre del fragmento en Liquid para hacer referencia a este conjunto de códigos promocionales.
- Asegúrate de que el fragmento de código no se esté utilizando ya en otra lista.

![Una lista de códigos promocionales llamada "SpringSale2025" con el fragmento de código "spring25".]({% image_buster /assets/img/promocodes/promocode3.png %}){: style="max-width:80%"}

### Paso 3: Elige opciones de código promocional

Cada lista de códigos promocionales tiene una fecha y hora de caducidad correspondientes que se establecen al crearla. La duración máxima de caducidad es de seis meses en el futuro a partir del día en que creas o editas tu lista. 

Dentro de ese plazo, puedes cambiar y actualizar la fecha de caducidad repetidamente. Esta fecha de caducidad se aplicará a todos los códigos añadidos a esta lista. Una vez caducados, los códigos se eliminarán del sistema Braze y no se enviará ningún mensaje que invoque el fragmento de código de esa lista.

![Configuración de caducidad de la lista para que todos los códigos restantes caduquen el 30 de abril de 2025 a las 12 de la mañana.]({% image_buster /assets/img/promocodes/promocode4.png %}){: style="max-width:80%"}

También tienes la opción de configurar alertas de umbral opcionales y personalizadas. Si se configuran, estas alertas enviarán un correo electrónico al destinatario designado cuando la lista se esté quedando sin códigos promocionales disponibles en esta lista o cuando su lista de códigos promocionales esté a punto de caducar. El destinatario recibirá una notificación al día.

![Un ejemplo de alerta de umbral para notificar a "marketing@abc.com" cuando la lista de códigos promocionales caduque en 5 días.]({% image_buster /assets/img/promocodes/promocode5.png %}){: style="max-width:80%"}

### Paso 4: Subir códigos promocionales

Braze no gestiona la creación ni el canje de códigos, lo que significa que debes generar tus códigos promocionales en un archivo CSV y subirlos a Braze. 

Asegúrate de que tu archivo CSV sigue estas directrices:

- Incluye una columna para códigos promocionales.
- Tiene un código promocional por fila.

Puede utilizar nuestra integración con [Voucherify]({{site.baseurl}}/partners/ecommerce/loyalty/voucherify/) o [Talon.One]({{site.baseurl}}/partners/ecommerce/loyalty/talonone/) para crear y exportar códigos promocionales.

{% alert important %}
El tamaño máximo del archivo es de 100 MB y el tamaño máximo de la lista es de 20MM de códigos no utilizados. Si descubre que se ha cargado un archivo incorrecto, cargue uno nuevo y el anterior será sustituido.
{% endalert %}

1. Una vez finalizada la carga, seleccione **Guardar lista** para guardar todos los datos y códigos que acaba de introducir.

![Archivo CSV llamado "springsale" que se ha cargado correctamente.]({% image_buster /assets/img/promocodes/promocode7.png %})

{:start="2"}
2\. Tras seleccionar Guardar, aparecerá una nueva fila en el **Historial de importaciones**.
3\. Para actualizar la tabla y comprobar si la importación ha finalizado, seleccione <span style="font-size: 14px;margin-bottom: .5rem;height: 16px;width: 16px;" class="fas fa-sync" ></span> **Sync** en la parte superior de la tabla.

![Códigos promocionales en proceso de carga.]({% image_buster /assets/img/promocodes/promocode8.png %})

{% alert note %}
Los archivos más grandes tardarán unos minutos en importarse. Mientras esperas, puedes salir de la página y trabajar en algo mientras se realiza la importación. Cuando finalice la importación, el estado cambiará a **Completado** en la tabla.
{% endalert %}

#### Actualizar una lista de códigos promocionales

Para actualizar una lista, seleccione una de las listas existentes. Puede cambiar el nombre, la descripción, la caducidad de la lista y los umbrales de alerta. También puede añadir más códigos a la lista cargando nuevos archivos y seleccionando **Actualizar lista**.

Todos los códigos de la lista tendrán la misma caducidad, independientemente de la fecha de importación.

### Paso 5: Utilizar códigos de promoción

Para enviar códigos promocionales en mensajes:

1. Selecciona **Copiar fragmento** para copiar el fragmento de código que estableciste al crear tu lista de códigos promocionales.

![Una opción para copiar el fragmento de código y pegarlo en tu mensaje.]({% image_buster /assets/img/promocodes/promocode9.png %}){: style="max-width:70%"}

{:start="2"}
2\. A partir de ahí, puedes pegar este código en un mensaje dentro del panel de control.

![Un mensaje de ejemplo "Date un capricho esta primavera con nuestra oferta exclusiva" seguido del fragmento de código.]({% image_buster /assets/img/promocodes/promocode10.png %}){: style="max-width:70%"}

Con [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/), puedes insertar en un mensaje uno de los códigos promocionales únicos del archivo CSV cargado. Ese código se marcará como enviado en el backend Braze para garantizar que ningún otro mensaje envíe ese mismo código.

#### Envío de códigos promocionales a los usuarios

Cuando se utiliza un fragmento de código en una campaña multicanal o en un paso de Canvas, cada usuario recibe siempre un código único. Para los distintos pasos de un Canvas, cada usuario recibe varios códigos de promoción.

Si un usuario es elegible para recibir un código a través de más de un canal, recibirá el mismo código a través de cada canal. Por ejemplo, si un usuario recibe dos mensajes a través de dos canales, sólo recibirá un código. Lo mismo ocurre a efectos de notificación: se enviará un código, que el usuario recibirá a través de los dos canales. Por ejemplo, para un paso en Canvas multicanal, el usuario solo utilizaría un código.

{% alert important %}
Si no quedan códigos promocionales disponibles al enviar mensajes de prueba o en directo desde una campaña que extrae códigos promocionales, el mensaje no se enviará.
{% endalert %}

#### Envío de mensajes de prueba con códigos promocionales

Los envíos de prueba y los envíos de correo electrónico de grupos de siembra utilizarán códigos promocionales a menos que se solicite lo contrario. Póngase en contacto con su gestor de cuenta Braze para actualizar el comportamiento de esta función, de modo que los códigos promocionales no se utilicen durante los envíos de prueba y los envíos de correo electrónico de grupos de semillas.

## Determinar cuántos códigos se han utilizado

Puedes encontrar el recuento de códigos restantes en la columna **Restantes** de la lista de códigos promocionales en la página **Códigos promocionales**.

![Un ejemplo de código promocional con códigos no utilizados.]({% image_buster /assets/img/promocodes/promocode11.png %})

Este recuento de códigos también se puede encontrar al volver a visitar una página de lista de códigos de promoción preexistente. También puedes exportar los códigos no utilizados como un archivo CSV. 

![Un código promocional llamado "Rebajas del Viernes Negro" con 992 códigos restantes.]({% image_buster /assets/img/promocodes/promocode12.png %}){: style="max-width:70%"}

### Utilizar códigos promocionales en campañas de mensajes dentro de la aplicación {#promotion-codes-iam-campaigns}

{% alert important %}
El uso de códigos promocionales en campañas de mensajería dentro de la aplicación está actualmente en acceso temprano. Ponte en contacto con tu director de cuentas de Braze si estás interesado en participar en este acceso anticipado.
{% endalert %}

Después de crear una [campaña de mensajería dentro]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages) de la aplicación, puedes insertar un [fragmento de lista de códigos promocionales]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes#creating-a-promotion-code-list) en el cuerpo de tu mensaje dentro de la aplicación. 

Los códigos promocionales de los mensajes dentro de la aplicación sólo se deducirán y utilizarán cuando un usuario desencadene la visualización del mensaje dentro de la aplicación.

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

Los códigos caducados se borran a los seis meses.

Si el mensaje debería haber contenido un código promocional de una lista vacía o caducada, el mensaje se cancelará. 

Si el mensaje contiene Lógica líquida que inserta condicionalmente un código de promoción, el mensaje sólo se cancelará si debería haber contenido un código de promoción. Si el mensaje no debería haber contenido un código de promoción, el mensaje se enviará normalmente.

### ¿Cómo guardo un código promocional en el perfil de un usuario para poder utilizarlo en mensajes de seguimiento?

Para hacer referencia al mismo código promocional en mensajes posteriores, el código debe guardarse en el perfil de usuario como un atributo personalizado. Esto puede hacerse adjuntando un [Webhook Braze to Braze]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/braze_to_braze_webhooks/) a la misma campaña o paso en Canvas de mensajería.

