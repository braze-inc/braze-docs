---
nav_title: Utilizar códigos
article_title: Utilizar códigos promocionales
page_order: 0.2
description: "Aprende a utilizar códigos promocionales y a ver su uso en tus campañas y Lienzos."
---

# Utilizar códigos promocionales

> Aprende a utilizar códigos promocionales y a ver su uso en tus campañas y Lienzos.

## Requisitos previos

Antes de poder utilizar códigos promocionales, tendrás que [crear una lista de códigos promocionales]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes/create/).

## Utilizar códigos promocionales

Para enviar un código promocional en un mensaje, selecciona **Copiar fragmento** junto a la lista de códigos promocionales [que creaste previamente]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes/create/#create).

![Una opción para copiar el fragmento de código y pegarlo en tu mensaje.]({% image_buster /assets/img/promocodes/promocode9.png %}){: style="max-width:70%"}

Pega los fragmentos de código en uno de tus mensajes en Braze y, a continuación, utiliza [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) para insertar uno de los códigos promocionales únicos de tu lista. Ese código se marca como enviado, garantizando que ningún otro mensaje envíe el mismo código.

![Un mensaje de ejemplo "Date un capricho esta primavera con nuestra oferta exclusiva" seguido del fragmento de código.]({% image_buster /assets/img/promocodes/promocode10.png %}){: style="max-width:70%"}

### Pasos en Canvas

Cuando se utiliza un fragmento de código en una campaña o Canvas con mensajes multicanal, cada usuario recibe un código único. En un Canvas con múltiples pasos que hacen referencia a códigos promocionales, un usuario obtiene un nuevo código por cada paso que introduce.

Para asignar un código promocional en un Canvas y reutilizarlo en los distintos pasos:

1. Asigna el código promocional como atributo personalizado en el primer paso (Actualización de usuario).
2. Utiliza Liquid en pasos posteriores para hacer referencia a ese atributo personalizado en lugar de generar un nuevo código.

Cuando un usuario reúne los requisitos para un código en varios canales, recibe el mismo código en cada canal. Por ejemplo, si reciben mensajes por correo electrónico y push, se envía el mismo código a ambos. Los informes también reflejan un código único.

{% alert note %}
Si no hay códigos promocionales disponibles, los mensajes de prueba o en vivo que dependen de códigos no se envían.
{% endalert %}

### Campañas de mensajería dentro de la aplicación {#promotion-codes-iam-campaigns}

Después de crear una [campaña de mensajería dentro]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages) de la aplicación, puedes insertar un [fragmento de lista de códigos promocionales]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes/manage/#using-promotion-codes-1) en el cuerpo de tu mensaje dentro de la aplicación. Los códigos promocionales de los mensajes dentro de la aplicación sólo se deducen y utilizan cuando un usuario desencadena la visualización del mensaje dentro de la aplicación.

### Mensajes de prueba

Los envíos de prueba y los envíos de correo electrónico de grupo semilla utilizan códigos promocionales a menos que se solicite lo contrario. Póngase en contacto con su gestor de cuenta Braze para actualizar el comportamiento de esta función, de modo que los códigos promocionales no se utilicen durante los envíos de prueba y los envíos de correo electrónico de grupos de semillas.

### Con extras de mensajes para Currents

{% multi_lang_include shopify.md section='Liquid promotion codes with Currents' %}

## Guardar códigos promocionales en perfiles de usuario {#save-to-profile}

Para hacer referencia al mismo código promocional en mensajes posteriores, el código debe guardarse en el perfil de usuario como un atributo personalizado. Esto puede hacerse mediante un [paso de Actualización de usuario]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/) que asigne el código de descuento a un atributo personalizado, como "Código promocional", directamente antes de un paso de Mensaje.

En primer lugar, selecciona lo siguiente para cada campo en el paso Actualizar usuario:

- **Nombre del atributo:** Código promocional
- **Acción:** Actualizar
- **Valor clave:** El fragmento de código Liquid del código promocional, como por ejemplo {% raw %}`{% promotion('spring25') %}`{% endraw %}

En segundo lugar, añade el atributo personalizado (en este ejemplo, {% raw %}`{{custom_attribute.${Promo Code}}}`{% endraw %}) a un mensaje. El código de descuento está en la plantilla.

## Ver el uso del código promocional

Puedes encontrar el recuento de códigos restantes en la columna **Restantes** de la lista de códigos promocionales en la página **Códigos promocionales**.

![Un ejemplo de código promocional con códigos no utilizados.]({% image_buster /assets/img/promocodes/promocode11.png %})

Este recuento de códigos también se puede encontrar al volver a visitar una página de lista de códigos de promoción preexistente. También puedes exportar los códigos no utilizados como un archivo CSV. 

![Un código promocional llamado "Rebajas del Viernes Negro" con 992 códigos restantes.]({% image_buster /assets/img/promocodes/promocode12.png %}){: style="max-width:70%"}

## Envíos multicanal y monocanal

Para las campañas multicanal y de envío único y los Lienzos, todos los códigos de promoción referenciados en el Líquido de un mensaje se deducen para ser utilizados **antes de** enviar el mensaje para asegurarse de que ocurre lo siguiente:

- En un mensaje multicanal se utilizan los mismos códigos de promoción en todos los canales.
- Los códigos promocionales adicionales no se utilizan si un mensaje falla o se cancela.

Si un usuario tiene dos listas de códigos promocionales referenciadas en un mensaje que está dividido por una etiqueta de lógica condicional de Liquid, se siguen deduciendo todos los códigos promocionales, independientemente del flujo condicional que siga el usuario.

Si un usuario entra en un nuevo paso en Canvas o vuelve a entrar en un Canvas, y el fragmento de código promocional Liquid se aplica de nuevo para un mensaje a ese usuario, se utiliza un nuevo código promocional.

### Ejemplo

En el siguiente ejemplo, se deducen las dos listas de códigos promocionales `vip-deal` y `regular-deal`. Aquí está el Liquid:

{% raw %}
```
{% if user.is_vip %}
  {% promotion('vip-deal') %}
{% else %}
  {% promotion('regular-deal') %}
{% endif %} 
```
{% endraw %}

Braze recomienda subir más códigos promocionales de los que estimes utilizar. Si una lista de códigos promocionales caduca o se quedan sin códigos promocionales, se cancelan los mensajes posteriores.

{% alert tip %}
**He aquí una analogía de cómo se utilizan los códigos promocionales en Braze.** <br><br>Imagina que enviar tu mensaje es como enviar una carta por correo postal. Entregas la carta a un empleado y éste ve que tu carta debe incluir un cupón. El empleado saca el primer cupón de la pila y lo añade al sobre. El empleado envía la carta, pero por alguna razón, la carta se pierde en el correo (y el cupón también se ha perdido). <br><br>En este caso, Braze es el empleado de correos, y tu código promocional es el cupón. No podemos recuperarlo después de haberlo sacado de la pila de códigos promocionales, independientemente del resultado del webhook.
{% endalert %}
