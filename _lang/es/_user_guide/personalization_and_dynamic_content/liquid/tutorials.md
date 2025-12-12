---
nav_title: Tutoriales
article_title: "Tutorías: Escribir código Liquid"
page_order: 11
description: "Esta página de referencia contiene tutoriales para principiantes que te ayudarán a empezar a utilizar el código Liquid."
page_type: tutorial
---

# Tutorías: Escribir código Liquid

> ¿Eres nuevo en Liquid? Estos tutoriales te ayudarán a empezar a escribir código Liquid para casos de uso aptos para principiantes. Cada tutorial abarca una combinación diferente de objetivos de aprendizaje, como la lógica condicional y los operadores.

Cuando hayas terminado con estos tutoriales, serás capaz de:

- Escribe código Liquid para casos de uso comunes
- Encadena la lógica condicional de Liquid para personalizar los mensajes en función de los datos de usuario
- Utiliza variables y filtros para escribir ecuaciones que utilicen los valores de los atributos
- Reconocer los comandos básicos del código Liquid y formarse una idea general de lo que hace el código.

| Tutorial | Objetivos de aprendizaje |
| --- | --- |
| [Personalización de mensajes para segmentos de usuarios](#segments) | valores predeterminados, lógica condicional |
| [Recordatorios de carrito de la compra abandonado](#reminders) | operadores, lógica condicional |
| [Cuenta atrás del evento](#countdown) | variables, filtros de fechas |
| [Mensaje mensual de cumpleaños](#birthday) | variables, filtros de fechas, operadores |
| [Promociona tu producto favorito](#favorite-product) | variables, filtros de fechas, ecuaciones, operadores |
{: .reset-br-td-1 .reset-br-td-2}

## Mensajes personalizados para segmentos de usuarios {#segments}

Personalicemos mensajes para diferentes segmentos de usuarios, como clientes VIP y nuevos suscriptores.

1. Abre el mensaje con saludos personalizados para enviar cuando tengas y no tengas el nombre de pila de un usuario. Para ello, crea una etiqueta de Liquid que incluya el atributo `first_name` y un valor predeterminado que se utilizará si `first_name` está en blanco. En este caso, vamos a utilizar "viajero" como valor predeterminado.

{% raw %}
```liquid
Happy summer, {{${first_name} | default: "traveler"}}!
```
{% endraw %}

{: start="2"}
2\. Ahora, vamos a proporcionar el mensaje a enviar si el usuario es un cliente VIP. Para ello tendremos que utilizar una etiqueta de lógica condicional: `if`. Esta etiqueta dirá que si el atributo personalizado `vip_status` es igual a `VIP`, se llevará a cabo lo siguiente Liquid. En este caso, se enviará un mensaje específico.

{% raw %}
```liquid
{% if {{custom_attribute.${vip_status}}} == 'VIP' %}
Thank you for being a VIP customer! Enjoy your exclusive discount code: VIPSUMMR464.
```
{% endraw %}

{: start="3"}
3\. Enviemos un mensaje personalizado para los usuarios que son nuevos suscriptores. Utilizaremos la etiqueta de lógica condicional `elsif` para especificar que si el `vip_status` del usuario es `new`, se enviará el siguiente mensaje.

{% raw %}
```liquid
{% elsif {{custom_attribute.${vip_status}}} == 'new' %}
Thank you for subscribing! Enjoy your welcome discount code: NEWTRAVEL257.
```
{% endraw %}

{: start="4"}
4\. ¿Qué pasa con los usuarios que no son VIP o nuevos? Podemos enviar un mensaje a todos los demás usuarios con la etiqueta `else`, que especifica que se envíe el siguiente mensaje si no se cumplen las condiciones anteriores. Entonces podemos cerrar la lógica condicional con la etiqueta `endif`, ya que no hay más estados VIP que considerar.

{% raw %}
```liquid
{% else %}
Thanks for traveling with us! Enjoy your unique discount code: SUMMRTRVLS240.
{% endif %}
```
{% endraw %}

{% details Full Liquid code %}
{% raw %}
```liquid
Happy summer, {{${first_name} | default: "traveler"}}!
{% if {{custom_attribute.${vip_status}}} == 'VIP' %}
Thank you for being a VIP customer! Enjoy your exclusive discount code: VIPSUMMR464.
{% elsif {{custom_attribute.${vip_status}}} == 'new' %}
Thank you for subscribing! Enjoy your welcome discount code: NEWTRAVEL257.
{% else %}
Thanks for traveling with us! Enjoy your unique discount code: SUMMRTRVLS240.
{% endif %}
```
{% endraw %}
{% enddetails %}

## Recordatorios de carrito de la compra abandonado {#reminders}

Enviemos mensajes personalizados para recordar a los usuarios los artículos que han dejado en su cesta. Además, los personalizaremos para que se envíen en función del número de artículos que tengan en su cesta, de modo que si tienen más de tres artículos o menos, los enumeraremos todos. Si hay más de tres elementos, enviaremos un mensaje más conciso.

1. Comprobemos si el carrito del usuario está vacío abriendo una lógica condicional Liquid con el operador `!=`, que significa "no es igual". En este caso, estableceremos la condición de que el atributo personalizado `cart_items` no sea igual a un valor en blanco.

{% raw %}
```liquid
{% if {{custom_attribute.${cart_items}}} != blank %}
```
{% endraw %}

{: start="2"}
2\. A continuación, tendremos que limitar nuestro enfoque y comprobar si el carro tiene más de tres artículos utilizando el operador \`>', que significa "mayor que".

{% raw %}
```liquid
{% if {{custom_attribute.${cart_items}}} | size > 3 %}
```
{% endraw %}

{: start="3"}
3\. Escribe un mensaje que salude al usuario por su nombre de pila o, si no está disponible, utiliza "allí" como valor predeterminado. Incluye lo que debe indicarse si hay más de tres artículos en el carrito. Como no queremos abrumar al usuario con una lista completa, vamos a enumerar las tres primeras `cart_items`.

{% raw %}
```liquid
Hi {{${first_name} | default: 'there'}}, don't forget to complete your purchase! Your items {{custom_attribute.${cart_items[0]}}}, {{custom_attribute.${cart_items[1]}}}, {{custom_attribute.${cart_items[2]}}}, and others are waiting for you.
```
{% endraw %}

{: start="4"}
4\. Utiliza la etiqueta `else` para especificar lo que debe ocurrir si no se cumplen las condiciones anteriores (en otras palabras, si `cart_items` está en blanco o es menos de tres), y luego proporciona el mensaje que se debe enviar. Como tres elementos no ocupan mucho espacio, podemos enumerarlos todos. Utilizaremos el operador Liquid `join` y `,` para especificar que los elementos deben aparecer en la lista separados por comas. Cierra la lógica con `endif`.

{% raw %}
```liquid
{% else %}
Hi {{${first_name} | default: 'there'}}, don't forget to complete your purchase! Your items: {{{custom_attribute.${cart_items}}} | join: ', '}  are waiting for you. 
{% endif %}
```
{% endraw %}

{: start="5"}
5\. Utiliza `else` y luego un `abort_message` para indicar al código Liquid que no envíe un mensaje si el carrito no cumple ninguna de las condiciones anteriores. En otras palabras, si el carro está vacío. Cierra la lógica con `endif`.

{% raw %}
```liquid
{% else %}
{% abort_message('No items in cart') %}
{% endif %}
```
{% endraw %}

{% details Full Liquid code %}
{% raw %}
```liquid
{% if {{custom_attribute.${cart_items}}} != blank %}
{% if {{custom_attribute.${cart_items}}} | size > 3 %}
Hi {{${first_name} | default: 'there'}}, don't forget to complete your purchase! Your items {{custom_attribute.${cart_items[0]}}}, {{custom_attribute.${cart_items[1]}}}, {{custom_attribute.${cart_items[2]}}}, and others are waiting for you.
{% else %}
Hi {{${first_name} | default: 'there'}}, don't forget to complete your purchase! Your items: {{{custom_attribute.${cart_items}}} | join: ', '}  are waiting for you.
{% endif %}
{% else %}
{% abort_message('No items in cart') %}
{% endif %}
```
{% endraw %}
{% enddetails %}

## Cuenta atrás del evento {#countdown}

Enviemos a los usuarios un mensaje que indique cuántos días faltan para una venta de aniversario. Para ello, utilizaremos variables para poder crear ecuaciones que manipulen los valores de los atributos.

1. En primer lugar, asignemos la variable `sale_date` al atributo personalizado `anniversary_date`, y apliquemos el filtro `date: "s"`. Esto convierte el `anniversary_date` a un formato de marca de tiempo que se expresa en segundos, y luego asigna ese valor a `sale_date`.

{% raw %}
```liquid
{% assign sale_date = {{custom_attribute.${anniversary_date}}} | date: "%s" %}
```
{% endraw %}

{: start="2"}
2\. También tenemos que asignar una variable para capturar la fecha y hora de hoy. Asignemos la variable `today` a `now` (la fecha y hora actuales), y luego apliquemos el filtro `date: "%s"`.

{% raw %}
```liquid
{% assign today =  'now' | date: "%s"  %}
```
{% endraw %}

{: start="3"}
3\. Ahora calculemos cuántos segundos hay entre ahora (`today`) y la Venta de Aniversario (`sale_date`). Para ello, asigna a la variable `difference` el valor de `sale_date` menos `today`.

{% raw %}
```liquid
{% assign difference =  event_date | minus: today %}
```
{% endraw %}

{: start="4"}
4\. Ahora tenemos que convertir `difference` en un valor al que podamos hacer referencia en un mensaje, ya que no es lo ideal decirle al usuario cuántos segundos faltan para una venta. Asignemos `difference_days` a `event_date` y dividámoslo por `86400` para obtener el número de días.

{% raw %}
```liquid
{% assign difference_days = difference | divided_by: 86400 %}
```
{% endraw %}

{: start="5"}
5\. Por último, vamos a crear el mensaje a enviar.

{% raw %}
```liquid
Get ready! Our Anniversary Sale is in {{ difference_days }} days!
```
{% endraw %}

{% details Full Liquid code %}
{% raw %}
```liquid
{% assign sale_date = {{custom_attribute.${anniversary_date}}} | date: "%s" %}
{% assign today =  'now' | date: "%s"  %}
{% assign difference =  event_date | minus: today %}
{% assign difference_days = difference | divided_by: 86400 %}
Get ready! Our Anniversary Sale is in {{ difference_days }} days!
```
{% endraw %}
{% enddetails %}

## Mensaje mensual de cumpleaños {#birthday}

Enviemos una promoción especial a todos los usuarios cuyo cumpleaños caiga dentro del mes de hoy. Los usuarios que no cumplan años este mes no recibirán ningún mensaje.

1. Primero, saquemos el mes de hoy. Asignaremos la variable `this_month` a `now` (la fecha y hora actuales), y luego utilizaremos el filtro `date: "%B"` para especificar que la variable debe ser igual al mes.

{% raw %}
```liquid
{% assign this_month = 'now' | date: "%B" %}
```
{% endraw %}

{: start="2"}
2\. Ahora, vamos a obtener el mes de nacimiento del usuario en `date_of_birth`. Asignaremos la variable `birth_month` a `date_of_birth`, y luego utilizaremos el filtro `date: "%B"`.

{% raw %}
```liquid
{% assign birth_month = {{${date_of_birth}}} | date: "%B" %}
```
{% endraw %}

{: start="3"}
3\. Ahora que tenemos dos variables que tienen como valor un mes, podemos compararlas con lógica condicional. Establezcamos la condición `date_of_birth` igual a la del usuario `birth_month`.

{% raw %}
```liquid
{% if {{this_month}} == {{birth_month}} %}
```
{% endraw %}

{: start="4"}
4\. Vamos a crear el mensaje a enviar si este mes es también el mes de nacimiento del usuario.

{% raw %}
```liquid
We heard {{this_month}} is a special month! Enjoy a 50% discount on your purchase with code BIRTHDAY50 until the end of {{this_month}}.
```
{% endraw %}

{: start="5"}
5\. Utiliza la etiqueta `else` para especificar qué ocurre si no se cumple la condición (porque este mes no es el mes de nacimiento del usuario).

{% raw %}
```liquid
{% else %} 
```
{% endraw %}

{: start="6"}
6\. No queremos enviar un mensaje si el mes de nacimiento del usuario no es este mes, así que utilizaremos `abort_message` para cancelar el mensaje y, a continuación, cerraremos la lógica condicional con `endif`.

{% raw %}
```liquid
{% abort_message("Not their birthday month") %}
{% endif %}
```
{% endraw %}

{% details Full Liquid code %}
{% raw %}
```liquid
{% assign this_month = 'now' | date: "%B" %}
{% assign birth_month = {{${date_of_birth}}} | date: "%B" %}
{% if {{this_month}} == {{birth_month}} %}
We heard {{this_month}} is a special month! Enjoy a 50% discount on your purchase with code BIRTHDAY50 until the end of {{this_month}}.
{% else %} 
{% abort_message("Not their birthday month") %}
{% endif %}
```
{% endraw %}
{% enddetails %}

## Promoción del producto favorito {#favorite-product}

Promocionemos el producto favorito de un usuario si su última fecha de compra fue hace más de seis meses.

1. En primer lugar, utilizaremos la lógica condicional para comprobar si tenemos el producto favorito del usuario y la fecha de la última compra.

{% raw %}
```liquid
{% if {{custom_attribute.${favorite_product}}} == blank or {{custom_attribute.${last_purchase_date}}} == blank %}
```
{% endraw %}

{: start="2"}
2\. Entonces diremos que si no tenemos el producto favorito del usuario o la fecha de la última compra, no enviemos un mensaje.

{% raw %}
```liquid
{% abort_message("No favorite product or last purchase date") %}
```
{% endraw %}

{: start="3"}
3\. Utilizaremos `else` para especificar lo que debe ocurrir si no se cumple la condición anterior ( _porque_ tenemos el producto favorito del usuario y la fecha de la última compra).

{% raw %}
```liquid
{% else %}
```
{% endraw %}

{: start="4"}
4\. Si tenemos la fecha de compra, tenemos que asignarla a una variable para poder compararla con la fecha de hoy. En primer lugar, vamos a crear un valor para la fecha de hoy asignando la variable `today` a `now` (la fecha y hora actuales) y utilizando el filtro `date: "%s"` para convertir el valor a un formato de marca de tiempo expresado en segundos. Añadiremos el filtro `plus: 0` para añadir un "0" a la marca de tiempo. Esto no cambia el valor de la marca de tiempo, pero es útil para utilizar la marca de tiempo en futuras ecuaciones.


{% raw %}
```liquid
{% assign today = 'now' | date: "%s" | plus: 0 %}
```
{% endraw %}

{: start="5"}
5\. Ahora vamos a capturar la fecha de la última compra en segundos asignando la variable `last_purchase_date` al atributo personalizado `last_purchase_date` y utilizando el filtro `date: "s"`. Añadiremos de nuevo el filtro `plus: 0`.

{% raw %}
```liquid
{% assign last_purchase_date = {{custom_attribute.${last_purchase_date}}} | date: "%s" | plus: 0 %}
```
{% endraw %}

{: start="6"}
6\. Como la fecha de la última compra y la fecha de hoy están en segundos, tendremos que calcular cuántos segundos hay en seis meses. Hagamos una ecuación (aproximadamente 6 meses * 30,44 días * 24 horas * 60 minutos * 60 segundos) y asignémosla a la variable `six_months`. Utilizaremos `times` para especificar la multiplicación de unidades de tiempo.

{% raw %}
```liquid
{% assign six_months = 6 | times: 30.44 | times: 24 | times: 60 | times: 60 %}
```
{% endraw %}

{: start="7"}
7\. Ahora que todos nuestros valores de tiempo están en segundos, podemos utilizar sus valores en ecuaciones. Asignemos una variable llamada `today_minus_last_purchase_date` que tome el valor de hoy y le reste el `last_purchase_date`. Esto nos da cuántos segundos han pasado desde la última compra.

{% raw %}
```liquid
{% assign today_minus_last_purchase_date = {{today | minus: last_purchase_date}} %}
```
{% endraw %}

{: start="8"}
8\. Ahora vamos a comparar directamente nuestros valores temporales en lógica condicional. Definamos la condición como que `today_minus_last_purchase_date` sea mayor o igual (`>=`) a seis meses. En otras palabras, la última fecha de compra fue hace al menos seis meses.

{% raw %}
```liquid
{% if today_minus_last_purchase_date >= six_months %}
```
{% endraw %}

{: start="9"}
9\. Vamos a crear el mensaje para enviar si la última compra fue hace al menos seis meses.

{% raw %}
```liquid
We noticed it’s been a while since you last purchased {{custom_attribute.${favorite_product}}}. Have you checked out our latest offerings?
```
{% endraw %}

{: start="10"}
10\. Utilizaremos la etiqueta `else` para especificar lo que debe ocurrir si no se cumple la condición (porque la compra no se realizó hace al menos seis meses).

{% raw %}
```liquid
{% else %}
```
{% endraw %}

{: start="11"}
11\. Incluiremos un `abort_message` para cancelar el mensaje.

{% raw %}
```liquid
{% abort_message("No favorite product or last purchase date") %}
```
{% endraw %}

{: start="12"}
12\. Para terminar, terminaremos el Liquid con dos etiquetas `endif`. La primera `endif` cierra la comprobación condicional del producto favorito o de la fecha de la última compra, y la segunda `endif` cierra la comprobación condicional de que la fecha de la última compra sea de hace al menos seis meses.

{% raw %}
```liquid
{% endif %}
{% endif %}
```
{% endraw %}

{% details Full Liquid code %}
{% raw %}
```liquid
{% if {{custom_attribute.${favorite_product}}} == blank or {{custom_attribute.${last_purchase_date}}} == blank %}
{% abort_message("No favorite product or last purchase date") %}
{% else %}
{% assign today = 'now' | date: "%s" | plus: 0 %}
{% assign last_purchase_date = {{custom_attribute.${last_purchase_date}}} | date: "%s" | plus: 0 %}
{% assign six_months = 6 | times: 30.44 | times: 24 | times: 60 | times: 60 %}
{% assign today_minus_last_purchase_date = {{today | minus: last_purchase_date}} %}
{% if today_minus_last_purchase_date >= six_months %}
We noticed it’s been a while since you last purchased {{custom_attribute.${favorite_product}}}. Have you checked out our latest offerings?
{% else %}
{% abort_message("Last purchase was less than six months ago") %}
{% endif %}
{% endif %}
```
{% endraw %}
{% enddetails %}
