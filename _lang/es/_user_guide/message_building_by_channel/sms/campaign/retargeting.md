---
nav_title: Reorientación de usuarios
article_title: Reorientación de usuarios por SMS
description: "Este artículo de referencia cubre cómo los usuarios pueden reorientar sus mensajes a través de las interacciones SMS de los usuarios."
page_type: reference
tool:
  - Campaigns
channel:
  - SMS

---

# Reorientación de usuarios

> Además de cambiar el estado de suscripción del usuario y enviar respuestas automáticas basadas en palabras clave entrantes, Braze también registrará las interacciones con el perfil del usuario para filtrar y activar mensajes.<br><br>Estos filtros y activadores permiten filtrar los usuarios que han recibido mensajes SMS, los que han recibido mensajes SMS de una campaña SMS específica y activar los mensajes a medida que los usuarios reciben mensajes SMS de una campaña SMS específica. 

{% alert tip %}
Para obtener más información sobre las palabras clave personalizadas y cómo configurar la mensajería bidireccional para aprovechar estas opciones de reorientación, visite nuestro artículo sobre [palabras clave personalizadas]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/keyword_handling/).
{% endalert %}  

## Opciones de reorientación

{% alert note %}
Al crear audiencias con retargeting de usuarios, es posible que desee incluir o excluir a determinados usuarios en función de sus preferencias, y con el fin de cumplir con las leyes de privacidad, como el derecho de "No vender ni compartir" en virtud de la CUP. Los vendedores deben implementar los filtros pertinentes para la elegibilidad de los usuarios dentro de sus criterios de entrada de Canvas y/o Campaña.
{% endalert %}

### Filtrar usuarios por SMS

Los usuarios pueden ser filtrados por la última vez que recibieron un SMS o si han recibido un SMS de una campaña de SMS específica. Los filtros pueden establecerse en el paso Usuarios objetivo del generador de campañas. 

**Filtrar por último SMS recibido**<br>
![Filtro de segmentación Último SMS recibido después del 8 de diciembre de 2020.][2]

**Filtrar por mensajes recibidos de la campaña SMS**<br>
Filtra los usuarios que han recibido un mensaje de una campaña SMS específica. Con este filtro, también tiene la opción de filtrar a aquellos que no han recibido mensajes de una campaña de SMS. <br>
![Filtro de segmentación Ha recibido un mensaje de la campaña "SMS retargeting".][1]

### Activar mensajes a medida que los usuarios reciben SMS {#trigger-messages}

Para activar mensajes a medida que los usuarios reciben mensajes SMS de una campaña específica, seleccione **Interactuar con la campaña** como acción activadora para una campaña basada en acciones. A continuación, seleccione **Recibir SMS** y la campaña de SMS que desea utilizar.

![][3]

### Filtrar por enlaces de seguimiento avanzados

Vuelva a dirigirse a los usuarios que hayan hecho clic en campañas con [enlaces de seguimiento avanzados]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/link_shortening/).
Sólo las campañas que tengan activado el seguimiento avanzado aparecerán en los siguientes desplegables:

**Volver a dirigirse a los usuarios que han hecho clic en una campaña de SMS específica**
1. Cree un segmento utilizando el filtro **Campaña clicada/abierta**.
2. Selecciona **los sms en los que se hizo clic**.
3. Elija la campaña deseada.

![][15]

**Reorientar a los usuarios que han hecho clic en un paso específico en Canvas**
1. Cree un segmento utilizando el filtro **Paso pulsado/abierto**.
2. Selecciona **los sms en los que se hizo clic**.
3. Elija el lienzo y el paso de lienzo deseados.

![][16]

## Reorientación a categorías específicas de palabras clave

Además de las tres categorías de palabras clave predeterminadas (Opt-in, Opt-out y Ayuda), también puede crear hasta 25 categorías de palabras clave propias, lo que le permite identificar palabras clave y respuestas arbitrarias. Estas categorías pueden utilizarse para filtrar y reorientar. Para obtener más información sobre las categorías de palabras clave de los SMS y cómo configurarlas, consulte [SMS retargeting]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/retargeting/). 

### Filtrar por recencia

Filtre la frecuencia con la que un usuario responde a su programa de SMS. Este filtro evaluará la última fecha en la que un usuario envió un SMS entrante que esté dentro de una de las categorías de palabras clave. 

![Filtro de segmentación Último SMS enviado al grupo de suscripción "Marketing SMS" con la palabra clave "Opt-in" después del 11 de agosto de 2020.][6]

### Filtrar por campaña o atribución Canvas

Filtra los usuarios que han respondido a una campaña SMS o a un componente Canvas, una categoría de palabras clave o una etiqueta específicos.

**Filtrar por respuesta a una categoría de campaña específica**<br>
![Campaña con el filtro "Ha respondido al SMS" para la campaña "SMS-283" "Promoción". Debajo del filtro, la función menciona "Este filtro caducará 25 meses después de que se envíe el último mensaje desde "Promoción" si no se está utilizando en ninguna campaña activa."][12]

**Filtrar por respuesta a una campaña o Canvas con una etiqueta específica**
![Campaña con el filtro "Ha respondido al SMS" para campaña o Canvas con la etiqueta "Servicio de mensajería en acera C".][13]

**Filtrar por respuesta a un paso específico**
![Campaña con el filtro "Ha respondido al SMS" para el paso "Doble adhesión voluntaria por SMS" "Paso - Ayuda".][11]

### Mensajes de activación por palabra clave

Los mensajes pueden activarse a medida que los usuarios envían mensajes entrantes basándose en categorías de palabras clave (el usuario envió cualquiera de las palabras clave) u otras palabras clave (el usuario envió una palabra clave que no entra en ninguna de las categorías existentes). Estos desencadenantes se configuran en el paso Entrega del constructor de campañas.

Cuando se evalúa si un mensaje entrante cumple un evento desencadenante definido, los espacios iniciales y finales se eliminan antes de que comience la evaluación.

{% alert tip %}
Si un Canvas basado en acciones es desencadenado por un mensaje SMS entrante, puedes hacer referencia a las propiedades del SMS en cualquier paso en Canvas hasta la siguiente ruta de acción.
{% endalert %}

**Activación por categoría de palabras clave entrantes**<br>
![Campaña SMS basada en acciones con el filtro de segmentación Palabra clave enviada "Adhesión voluntaria" al grupo de suscripción "Marketing por SMS".][7]{: style="margin-top:10px;"}

**Activación por palabras clave arbitrarias**<br>
Tenga en cuenta que al activar un mensaje en una respuesta de palabra clave "Otra", tendrá la oportunidad de evaluar el cuerpo de la palabra clave en una coincidencia de texto exacta. Esta coincidencia sigue las mismas reglas que las anotadas: Sólo se procesará el **mensaje exacto, de una sola palabra** ( _sin distinguir_ mayúsculas de minúsculas). Una palabra clave enviada de `Hello Braze!` no coincidiría con los criterios mostrados en el siguiente ejemplo.
![Campaña de SMS basada en acciones con la categoría de palabras clave "Otros" en la que el cuerpo del mensaje es exactamente "Hola" o "Eh".][8]{: style="margin-top:10px;"}

**Palabras clave de la plantilla**<br>
Al activar una campaña o un componente del lienzo en un SMS o MMS entrante, puede incorporar opcionalmente el texto o los archivos multimedia adjuntos que el usuario envió al cuerpo de la campaña o del lienzo con Liquid. Esto le permitirá acceder a la respuesta del usuario, que podrá incluir en su respuesta, aplicarle lógica condicional o cualquier otra cosa que pueda hacer con Liquid. 

{% raw %}

```liquid
Sorry, we didn't recognize {{sms.${inbound_message_body}}}. Text HELP for help or STOP to stop.
```

```liquid
{% if {{sms.${inbound_message_body}}} == "SNEAKERS" %}
OK, you're subscribed to updates on all our sneaker deals!
{% elsif {{sms.${inbound_message_body}}} == "SHIRTS" %}
Shirt deals coming up for you!
{% else %}
Want to receive a specific deal? Just text us the category you're interested in. For example SHIRTS or SNEAKERS.
{% endif %}
```

{% endraw %}

[1]: {% image_buster /assets/img/sms/filter1.png %}
[2]: {% image_buster /assets/img/sms/filter2.png %}
[3]: {% image_buster /assets/img/sms/trigger.png %}
[6]: {% image_buster /assets/img/sms/retargeting1.png %}
[7]: {% image_buster /assets/img/sms/retargeting2.png %}
[8]: {% image_buster /assets/img/sms/retargeting3.png %}
[16]: {% image_buster /assets/img/keyword_example1.jpg %}
[17]: {% image_buster /assets/img/keyword_example2.jpg %}
[11]: {% image_buster /assets/img/sms/clicked_opened_step.png %}
[12]: {% image_buster /assets/img/sms/clicked_opened_campaign.png %}
[13]: {% image_buster /assets/img/sms/clicked_opened_campaign_canvas_tag.png %}
[15]: {% image_buster /assets/img/sms/retargeting5.png %}
[16]: {% image_buster /assets/img/sms/retargeting4.png %}
