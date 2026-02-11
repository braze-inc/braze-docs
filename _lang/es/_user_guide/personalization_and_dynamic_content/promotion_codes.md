---
nav_title: Códigos de promoción
article_title: Códigos promocionales
page_order: 5
toc_headers: h2
alias: "/promotion_codes/"
description: "Infórmate sobre las listas de códigos promocionales, para que puedas añadirlos a tus campañas y Lienzos."
---

# Códigos de promoción

> Infórmate sobre las listas de códigos promocionales, para que puedas añadirlos a tus campañas y Lienzos.

## Acerca de los códigos promocionales

Los códigos promocionales te permiten insertar valores únicos y limitados en el tiempo en los mensajes para impulsar las conversiones. Cada lista puede contener hasta 20 millones de códigos, y cada código puede durar hasta seis meses antes de caducar.

Cuando Braze envía un mensaje con un código promocional, el código se deduce antes de que se envíe el mensaje. Para garantizar que los códigos sean coherentes, únicos y nunca reutilizados:

- Un mensaje fallido sigue consumiendo el código.
- En los envíos multicanal, se aplica el mismo código a todos los canales.
- Con Liquid condicional, todas las listas referenciadas tienen códigos deducidos, aunque sólo se muestre una rama.
- Introducir o volver a introducir un paso en Canvas consume un nuevo código.

Si colocas varios fragmentos de la misma lista en un mensaje, Braze aplicará el mismo código a todos los fragmentos. Para evitar quedarte sin códigos, te recomendamos que subas más códigos de los que esperas utilizar.

{% tabs local %}
{% tab Example %}
Piensa en los códigos promocionales como en los cupones de una oficina de correos. Una vez que el empleado saca un cupón de la pila para tu carta, desaparece, aunque la carta nunca llegue.  

Por ejemplo, en la siguiente condicional Liquid, se deducen los códigos de ambas listas (`vip-deal` y `regular-deal`), aunque cada usuario sólo vea una rama:

{% raw %}
```liquid
{% if user.is_vip %}
  {% promotion('vip-deal') %}
{% else %}
  {% promotion('regular-deal') %}
{% endif %}
```
{% endraw %}
{% endtab %}
{% endtabs %}

{% alert important %}
Los códigos promocionales no pueden enviarse en mensajes dentro de la aplicación en Canvas.
{% endalert %}

## Próximos pasos

¿Buscas próximos pasos? Empieza por aquí:

- [Crear una lista de códigos promocionales]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes/create/)
- [Utilizar códigos promocionales]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes/manage/#using-promotion-codes)
- [Ver el uso del código promocional]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes/manage/#viewing-promotion-code-usage)

## Preguntas más frecuentes

### ¿Qué canales de mensajería puedo utilizar con los códigos promocionales?

Actualmente, los códigos de promoción son compatibles con correo electrónico, push móvil, push web, tarjetas de contenido, webhook, SMS y WhatsApp. Las campañas Braze Transactional Email y los mensajes in-app no admiten actualmente códigos promocionales.

### ¿Los envíos de prueba y de semillas cuentan para el uso?

Por defecto, los envíos de prueba y los envíos de correo electrónico del grupo inicial utilizarán códigos de promoción por usuario, por envío de prueba. Sin embargo, puedes ponerte en contacto con tu director de cuentas de Braze para actualizar este comportamiento y no utilizar códigos promocionales durante las pruebas.

### ¿Qué ocurre cuando varios canales de mensajería utilizan el mismo fragmento de código promocional?

Si un usuario concreto es elegible para recibir un código a través de varios canales, recibirá el mismo código a través de cada canal. Sólo se utilizará un código promocional, independientemente de los canales recibidos.

### ¿Puedo utilizar varios fragmentos de código Liquid para hacer referencia a la misma lista de códigos promocionales en un mensaje?

Sí. Braze aplicará el mismo código promocional en todas las instancias de ese fragmento en el mensaje, asegurándose de que el usuario sólo reciba un código único.

### ¿Qué ocurre cuando una lista de códigos promocionales caduca o está vacía?

Los códigos caducados se eliminan a los seis meses.

Si el mensaje debería haber contenido un código promocional de una lista vacía o caducada, el mensaje se cancelará. 

Si el mensaje contiene Lógica líquida que inserta condicionalmente un código de promoción, el mensaje sólo se cancelará si debería haber contenido un código de promoción. Si el mensaje no debía contener un código promocional, el mensaje se enviará normalmente.

### Si he cargado códigos promocionales erróneos, ¿puedo actualizarlos?

Sí. Puedes resolverlo eliminando toda la lista o utilizando un marcador de posición para borrarla. Para más información, consulta [Actualizar una lista de códigos promocionales]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes/create/#updating-a-promotion-code-list).

### ¿Puedo guardar un código promocional en el perfil de un usuario para futuros mensajes?

Sí. Puedes guardar códigos promocionales en el perfil de un usuario mediante un paso de Actualización de usuario. Para más información, consulta [Guardar códigos promocionales en perfiles de usuario]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes/manage/#save-to-profile).
