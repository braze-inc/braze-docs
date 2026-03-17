---
nav_title: Uso de códigos
article_title: Uso de códigos promocionales
page_order: 0.2
description: "Aprende a utilizar los códigos promocionales y consulta su uso en tus campañas y lienzos."
---

# Uso de códigos promocionales

> Aprende a utilizar los códigos promocionales y consulta su uso en tus campañas y lienzos.

## Requisitos previos

Antes de poder utilizar códigos promocionales, deberás [crear una lista]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes/create/) de [códigos promocionales]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes/create/).

## Uso de códigos promocionales

Para enviar un código promocional en un mensaje, selecciona **Copiar fragmento de código** junto a la lista de códigos promocionales [que has creado anteriormente]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes/create/#create).

![Una opción para copiar el fragmento de código y pegarlo en tu mensaje.]({% image_buster /assets/img/promocodes/promocode9.png %}){: style="max-width:70%"}

Pega los fragmentos de código en uno de tus mensajes en Braze y, a continuación, utiliza [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) para insertar uno de los códigos promocionales únicos de tu lista. Ese código se marca como enviado, lo que garantiza que ningún otro mensaje envíe el mismo código.

![Un ejemplo de mensaje: «Date un capricho esta primavera con nuestra oferta exclusiva», seguido del fragmento de código.]({% image_buster /assets/img/promocodes/promocode10.png %}){: style="max-width:70%"}

### A través de los pasos en Canvas

Cuando se utiliza un fragmento de código en una campaña o Canvas con mensajes multicanal, cada usuario recibe un código único. En un Canvas con varios pasos que hacen referencia a códigos promocionales, el usuario obtiene un nuevo código por cada paso que completas.

Para asignar un código promocional en Canvas y reutilizarlo en varios pasos:

1. Asigna el código promocional como un atributo personalizado en el primer paso (Actualización de usuario).
2. Utiliza Liquid en pasos posteriores para hacer referencia a ese atributo personalizado en lugar de generar un nuevo código.

Cuando un usuario cumple los requisitos para obtener un código en varios canales, recibe el mismo código en cada canal. Por ejemplo, si recibís mensajes por correo electrónico y push, se envía el mismo código a ambos. Los informes también reflejan un único código.

{% alert note %}
Si no hay códigos promocionales disponibles, los mensajes de prueba o en vivo que dependen de códigos no se envían.
{% endalert %}

### Campañas de mensajes dentro de la aplicación {#promotion-codes-iam-campaigns}

Después de crear una [campaña de mensajes dentro de la aplicación]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages), puedes insertar un [fragmento de código promocional]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes/manage/#using-promotion-codes-1) en el cuerpo del mensaje dentro de la aplicación. Los códigos promocionales de los mensajes dentro de la aplicación se deducen y utilizan solo cuando el usuario desencadena la visualización del mensaje dentro de la aplicación.

### Mensajes de prueba

Los envíos de prueba y los envíos por correo electrónico del grupo semilla agotan los códigos promocionales, a menos que se solicite lo contrario. Póngase en contacto con su gestor de cuenta Braze para actualizar el comportamiento de esta función, de modo que los códigos promocionales no se utilicen durante los envíos de prueba y los envíos de correo electrónico de grupos de semillas.

### Con extras de mensajes para Currents

{% multi_lang_include shopify.md section='Liquid promotion codes with Currents' %}

## Guardar códigos promocionales en los perfiles de usuario {#save-to-profile}

Para hacer referencia al mismo código promocional en mensajes posteriores, el código debe guardarse en el perfil de usuario como un atributo personalizado. Esto se puede hacer mediante un [paso de actualización de usuario]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/) que asigne el código de descuento a un atributo personalizado, como «Código promocional», justo antes de un paso de mensaje.

En primer lugar, selecciona lo siguiente para cada campo en el paso Actualización de usuario:

- **Nombre del atributo:** Código promocional
- **Acción:** Actualizar
- **Valor clave:** El fragmento de código Liquid del código promocional, como {% raw %}`{% promotion('spring25') %}`{% endraw %}

En segundo lugar, añade el atributo personalizado (en este ejemplo, {% raw %}`{{custom_attribute.${Promo Code}}}`{% endraw %}) a un mensaje. El código de descuento está incluido en la plantilla.

## Ver el uso del código promocional

Puedes encontrar el recuento de códigos restantes en la columna **«Restantes»** de la lista de códigos promocionales en la página **«Códigos promocionales**».

![Un ejemplo de código promocional con códigos sin usar.]({% image_buster /assets/img/promocodes/promocode11.png %})

Este recuento de códigos también se puede encontrar al volver a visitar una página de lista de códigos de promoción preexistente. También puedes exportar los códigos no utilizados como un archivo CSV. 

![Un código promocional llamado «Black Friday Sale» con 992 códigos restantes.]({% image_buster /assets/img/promocodes/promocode12.png %}){: style="max-width:70%"}

## Envíos multicanal y monocanal

Para las campañas multicanal y de envío único y los Lienzos, todos los códigos de promoción referenciados en el Líquido de un mensaje se deducen para ser utilizados **antes de** enviar el mensaje para asegurarse de que ocurre lo siguiente:

- En un mensaje multicanal se utilizan los mismos códigos de promoción en todos los canales.
- Los códigos promocionales adicionales no se utilizan si un mensaje falla o se cancela.

Si un usuario tiene dos listas de códigos promocionales referenciadas en un mensaje que está dividido por una etiqueta de lógica condicional Liquid, todos los códigos promocionales se deducirán, independientemente del flujo condicional que sigas.

Si un usuario ingresa a un nuevo paso en Canvas o vuelve a ingresar a Canvas, y el fragmento de código promocional Liquid se aplica nuevamente para un mensaje a ese usuario, se utiliza un nuevo código promocional.

### Ejemplo

En el siguiente ejemplo, se deducen las listas de códigos`regular-deal` `vip-deal`promocionales  y . Aquí está el Liquid:

{% raw %}
```
{% if user.is_vip %}
  {% promotion('vip-deal') %}
{% else %}
  {% promotion('regular-deal') %}
{% endif %} 
```
{% endraw %}

Braze recomienda subir más códigos promocionales de los que estimas que vas a utilizar. Si una lista de códigos promocionales caduca o se agota, los mensajes posteriores se cancelan.

{% alert tip %}
**He aquí una analogía de cómo se utilizan los códigos promocionales en Braze.** <br><br>Imagina que enviar tu mensaje es como enviar una carta por correo postal. Entregas la carta a un empleado y éste ve que tu carta debe incluir un cupón. El empleado saca el primer cupón de la pila y lo añade al sobre. El empleado envía la carta, pero por alguna razón, la carta se pierde en el correo (y el cupón también se ha perdido). <br><br>En este escenario, Braze es el empleado de correos y tu código promocional es el cupón. No podemos recuperarlo una vez que se ha retirado de la pila de códigos promocionales, independientemente del resultado del webhook.
{% endalert %}
