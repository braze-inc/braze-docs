---
nav_title: Códigos promocionales
article_title: Códigos promocionales
page_order: 5
toc_headers: h2
alias: "/promotion_codes/"
description: "Este artículo de referencia explica cómo crear listas de códigos promocionales y añadirlos a tus campañas y Lienzos."
---

# Códigos promocionales

> Esta página explica cómo crear listas de códigos promocionales y añadirlos a tus campañas y Lienzos.

## Acerca de los códigos promocionales

Los códigos promocionales -también llamados códigos promocionales- son una forma estupenda de mantener el compromiso de los usuarios impulsando las interacciones con un fuerte énfasis en las compras. Puedes crear mensajes que tiren de tu lista de códigos promocionales. 

Cada código promocional tiene una fecha de caducidad de hasta seis meses. Puedes almacenar y gestionar hasta 20 millones de códigos por lista. Al gestionar y analizar el rendimiento de tus códigos promocionales, puedes tomar decisiones específicas para tus estrategias promocionales y de mensajería.

{% alert important %}
Los códigos promocionales no pueden enviarse en mensajes dentro de la aplicación en Canvas.
{% endalert %}

## Crear una lista de códigos promocionales {#create}

### Paso 1: Ir a la sección Código promocional

\![Botón para crear un código promocional.]({% image_buster /assets/img/promocodes/promocode1.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

1. Desde el panel, ve a **Configuración de datos** > Códigos promocionales.
2. Selecciona **Crear lista de códigos promocionales**.

### Paso 2: Indica el código promocional

1. Nombra tu lista de códigos promocionales y añade una descripción opcional.
2. A continuación, crea un fragmento de código para el código promocional. 

Aquí tienes algunos detalles que debes tener en cuenta al crear un fragmento de código:

- Una vez guardados, los fragmentos de código no se pueden editar.
- Los fragmentos de código distinguen entre mayúsculas y minúsculas. Por ejemplo, "Birthday_promo" y "birthday_promo" se reconocerán como dos fragmentos de código diferentes.
- Utiliza el nombre del fragmento en Liquid para hacer referencia a este conjunto de códigos promocionales.
- Asegúrate de que el fragmento de código no se esté utilizando ya en otra lista.

Una lista de códigos promocionales llamada "SpringSale2025" con el fragmento de código "spring25".]({% image_buster /assets/img/promocodes/promocode3.png %}){: style="max-width:80%"}

### Paso 3: Elige opciones de código promocional

Cada lista de códigos promocionales tiene una fecha y hora de caducidad correspondientes que se establecen al crearla. La duración máxima de la caducidad es de seis meses en el futuro a partir del día en que creas o editas tu lista. 

Dentro de ese plazo, puedes cambiar y actualizar la fecha de caducidad repetidamente. Esta fecha de caducidad se aplicará a todos los códigos añadidos a esta lista. Cuando caduquen, los códigos se eliminarán del sistema Braze, y no se enviará ningún mensaje que invoque el fragmento de código de esa lista.

\![Lista de configuraciones de caducidad que todos los códigos restantes caducarán el 30 de abril de 2025 a las 12 de la mañana.]({% image_buster /assets/img/promocodes/promocode4.png %}){: style="max-width:80%"}

También tienes la opción de configurar umbrales de alerta opcionales y personalizados. Si se configuran, estas alertas enviarán un correo electrónico al destinatario designado cuando la lista se esté quedando sin códigos promocionales disponibles en esta lista o cuando tu lista de códigos promocionales esté a punto de caducar. El destinatario recibirá una notificación al día.

\![Ejemplo de alerta de umbral para notificar a "marketing@abc.com" cuando la lista de códigos promocionales caduque en 5 días.]({% image_buster /assets/img/promocodes/promocode5.png %}){: style="max-width:80%"}

### Paso 4: Subir códigos promocionales

Braze no gestiona la creación ni el canje de códigos, lo que significa que debes generar tus códigos promocionales en un archivo CSV y subirlos a Braze. 

Asegúrate de que tu archivo CSV sigue estas directrices:

- Incluye una columna para códigos promocionales.
- Tiene un código promocional por fila.

Puedes utilizar nuestra integración incorporada con [Voucherify]({{site.baseurl}}/partners/ecommerce/loyalty/voucherify/) o [Talon.One]({{site.baseurl}}/partners/ecommerce/loyalty/talonone/) para crear y exportar códigos promocionales.

{% alert important %}
El tamaño máximo del archivo es de 100 MB, y el tamaño máximo de la lista es de 20MM de códigos no utilizados. Si descubres que se ha subido un archivo incorrecto, sube uno nuevo y el anterior será sustituido.
{% endalert %}

1. Una vez finalizada la carga, selecciona **Guardar lista** para guardar todos los datos y códigos que acabas de introducir.

Se ha cargado correctamente un archivo CSV llamado "springsale".]({% image_buster /assets/img/promocodes/promocode7.png %})

{:start="2"}
2\. Tras seleccionar Guardar, aparecerá una nueva fila en el **Historial de Importaciones**.
3\. Para actualizar la tabla y ver si tu importación ha finalizado, selecciona <span style="font-size: 14px;margin-bottom: .5rem;height: 16px;width: 16px;" class="fas fa-sync" ></span> **Sincronizar** en la parte superior de la tabla.

Códigos promocionales en proceso de carga.]({% image_buster /assets/img/promocodes/promocode8.png %})

{% alert note %}
Los archivos más grandes tardarán unos minutos en importarse. Mientras esperas, puedes salir de la página y trabajar en algo mientras se realiza la importación. Cuando finalice la importación, el estado cambiará a **Completado** en la tabla.
{% endalert %}

## Actualizar una lista de códigos promocionales

Para actualizar una lista, selecciona una de tus listas existentes. Puedes cambiar el nombre, la descripción, la caducidad de la lista y el umbral de alertas. También puedes añadir más códigos a la lista cargando nuevos archivos y seleccionando **Actualizar lista**. Todos los códigos de la lista tendrán la misma caducidad, independientemente de la fecha de importación.

{% alert important %}
Los códigos promocionales no se pueden eliminar.
{% endalert %}

### Modificación de la lista de códigos promocionales incorrectos 

Si has cargado un archivo CSV con los códigos promocionales incorrectos y has seleccionado **Guardar lista**, puedes resolverlo por cualquiera de los dos métodos:

- Desaparece toda la lista: Deja de utilizar la lista actual de códigos promocionales en cualquier campaña, Lienzo o plantilla. A continuación, sube el archivo CSV con los códigos correctos y utilízalos en tu mensajería.
- Utiliza los códigos incorrectos: Crea una campaña que envíe códigos promocionales de la lista de códigos promocionales incorrectos a un marcador de posición hasta que se utilicen todos los códigos incorrectos. A continuación, carga los códigos promocionales correctos en la misma lista.

## Utilizar códigos promocionales {#update}

Para enviar un código promocional en un mensaje, selecciona **Copiar fragmento** junto a la lista de códigos promocionales [que creaste previamente](#create).

\![Una opción para copiar el fragmento de código y pegarlo en tu mensaje.]({% image_buster /assets/img/promocodes/promocode9.png %}){: style="max-width:50%"}

Pega los fragmentos de código en uno de tus mensajes en Braze y, a continuación, utiliza [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) para insertar uno de los códigos promocionales únicos de tu lista. Ese código se marcará como enviado, asegurando que ningún otro mensaje envíe el mismo código.

\![Un mensaje de ejemplo "Date un capricho esta primavera con nuestra oferta exclusiva" seguido del fragmento de código.]({% image_buster /assets/img/promocodes/promocode10.png %}){: style="max-width:50%"}

### Pasos en Canvas

Cuando se utiliza un fragmento de código en una campaña o Canvas con mensajes multicanal, cada usuario recibe un código único. En un Canvas con múltiples pasos que hacen referencia a códigos promocionales, un usuario obtiene un nuevo código por cada paso que introduce.

Para asignar un código promocional en un Canvas y reutilizarlo en los distintos pasos:

1. Asigna el código promocional como atributo personalizado en el primer paso (Actualización de usuario).
2. Utiliza Liquid en pasos posteriores para hacer referencia a ese atributo personalizado en lugar de generar un nuevo código.

Cuando un usuario reúne los requisitos para un código en varios canales, recibe el mismo código en cada canal. Por ejemplo, si reciben mensajes por correo electrónico y push, se envía el mismo código a ambos. Los informes también reflejan un código único.

{% alert note %}
Si no hay códigos promocionales disponibles, los mensajes de prueba o en vivo que dependan de códigos no se enviarán.
{% endalert %}

### Campañas de mensajes dentro de la aplicación {#promotion-codes-iam-campaigns}

Después de crear una [campaña de mensajería dentro]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages) de la aplicación, puedes insertar un [fragmento de lista de códigos promocionales]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes#creating-a-promotion-code-list) en el cuerpo de tu mensaje dentro de la aplicación. 

Los códigos promocionales de los mensajes dentro de la aplicación sólo se deducirán y utilizarán cuando un usuario desencadene la visualización del mensaje dentro de la aplicación.

### En mensajes de prueba

Los envíos de prueba y los envíos de correo electrónico de grupos semilla utilizarán códigos promocionales a menos que se solicite lo contrario. Ponte en contacto con tu director de cuentas Braze para actualizar el comportamiento de esta característica, de modo que los códigos promocionales no se utilicen durante los envíos de prueba y los envíos por correo electrónico de grupo semilla.

### Con extras de mensajes para Currents

{% multi_lang_include shopify.md section='Liquid promotion codes with Currents' %}

## Guardar códigos promocionales en perfiles de usuario {#save-to-profile}

Para hacer referencia al mismo código promocional en mensajes posteriores, el código debe guardarse en el perfil de usuario como un atributo personalizado. Esto puede hacerse mediante un [paso de Actualización de usuario]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/) que asigne el código de descuento a un atributo personalizado, como "Código promocional", directamente antes de un paso de Mensaje.

Primero, selecciona lo siguiente para cada campo en el paso Actualización de usuario:

- **Nombre del atributo:** Código promocional
- **Acción:** Actualización
- **Valor clave:** El fragmento de código Liquid del código promocional, como por ejemplo {% raw %}`{% promotion('spring25') %}`{% endraw %}

En segundo lugar, añade el atributo personalizado (en este ejemplo, {% raw %}`{{custom_attribute.${Promo Code}}`{% endraw %}) a un mensaje. El código de descuento estará en la plantilla.

## Ver el uso del código promocional

Puedes encontrar el recuento de códigos restantes en la columna **Restantes** de la lista de códigos promocionales en la página **Códigos promocionales**.

\![Un ejemplo de código promocional con códigos no utilizados.]({% image_buster /assets/img/promocodes/promocode11.png %})

Este recuento de códigos también se puede encontrar al volver a visitar una página de lista de códigos promocionales preexistente. También puedes exportar los códigos no utilizados como un archivo CSV. 

Un código promocional llamado "Rebajas del Viernes Negro" con 992 códigos restantes.]({% image_buster /assets/img/promocodes/promocode12.png %}){: style="max-width:50%"}

## Envíos multicanal y monocanal

En las campañas multicanal y de envío único y en los Lienzos, todos los códigos promocionales a los que se hace referencia en el Líquido de un mensaje se deducen para utilizarlos **antes de** enviar el mensaje y asegurarse de que ocurre lo siguiente:

- En un mensaje multicanal se utilizan los mismos códigos promocionales en todos los canales.
- Los códigos promocionales adicionales no se utilizan si un mensaje falla o se cancela.

Si un usuario tiene dos listas de códigos promocionales referenciadas en un mensaje que está dividido por una etiqueta de lógica condicional de Liquid, se seguirán deduciendo todos los códigos promocionales, independientemente del flujo condicional que siga el usuario.

Si un usuario entra en un nuevo paso en Canvas o vuelve a entrar en un Canvas, y el fragmento de código promocional Liquid se aplica de nuevo para un mensaje a ese usuario, se utilizará un nuevo código promocional.

### Ejemplo

En el siguiente ejemplo, se deducirán las dos listas de códigos promocionales `vip-deal` y `regular-deal`. Aquí está el Liquid:

{% raw %}
```
{% if user.is_vip %}
  {% promotion('vip-deal') %}
{% else %}
  {% promotion('regular-deal') %}
{% endif %} 
```
{% endraw %}

Braze recomienda subir más códigos promocionales de los que calculas que se utilizarán. Si una lista de códigos promocionales caduca o se agotan los códigos promocionales, se cancelarán los mensajes posteriores.

{% alert tip %}
**He aquí una analogía de cómo se utilizan los códigos promocionales en Braze.** <br><br>Imagina que enviar tu mensaje es como enviar una carta a Correos. Le das la carta a un empleado y éste ve que tu carta debe incluir un cupón. El empleado saca el primer cupón de la pila y lo añade al sobre. El secretario envía la carta, pero por alguna razón, la carta se pierde en el correo (y el cupón ahora también se ha perdido). <br><br>En este caso, Braze es el empleado de correos, y tu código promocional es el cupón. No podemos recuperarlo después de haberlo sacado de la pila de códigos promocionales, independientemente del resultado del webhook.
{% endalert %}

## Preguntas más frecuentes

### ¿Qué canales de mensajería puedo utilizar con los códigos promocionales?

Actualmente se admiten códigos promocionales para correo electrónico, push móvil, push web, tarjetas de contenido, webhook, SMS y WhatsApp. Las campañas de correo electrónico transaccional de Braze y los mensajes dentro de la aplicación no admiten actualmente códigos promocionales.

### ¿Los envíos de prueba y de semillas cuentan para el uso?

Por defecto, los envíos de correo electrónico de prueba y de grupo semilla utilizarán códigos promocionales por usuario, por envío de prueba. Sin embargo, puedes ponerte en contacto con tu director de cuentas de Braze para actualizar este comportamiento y no utilizar códigos promocionales durante las pruebas.

### ¿Qué ocurre cuando varios canales de mensajería utilizan el mismo fragmento de código promocional?

Si un usuario concreto es elegible para recibir un código a través de varios canales, recibirá el mismo código a través de cada canal. Sólo se utilizará un código promocional, independientemente de los canales recibidos.

### ¿Puedo utilizar varios fragmentos de código Liquid para hacer referencia a la misma lista de códigos promocionales en un mensaje?

Sí. Braze aplicará el mismo código promocional en todas las instancias de ese fragmento en el mensaje, asegurándose de que el usuario sólo reciba un código único.

### ¿Qué ocurre cuando una lista de códigos promocionales está caducada o vacía?

Los códigos caducados se eliminan a los seis meses.

Si el mensaje debería haber contenido un código promocional de una lista vacía o caducada, el mensaje se cancelará. 

Si el mensaje contiene la lógica Liquid que inserta condicionalmente un código promocional, el mensaje sólo se cancelará si debería haber contenido un código promocional. Si el mensaje no debía contener un código promocional, el mensaje se enviará normalmente.

### Si he cargado códigos promocionales erróneos, ¿puedo actualizarlos?

Sí. Puedes resolverlo eliminando toda la lista o utilizando un marcador de posición para borrarla. Para más información, consulta [Actualizar códigos promocionales](#update).

### ¿Puedo guardar un código promocional en el perfil de un usuario para futuros mensajes?

Sí. Puedes guardar códigos promocionales en el perfil de un usuario mediante un paso de Actualización de usuario. Para más información, consulta [Guardar códigos promocionales en perfiles de usuario](#save-to-profile).
