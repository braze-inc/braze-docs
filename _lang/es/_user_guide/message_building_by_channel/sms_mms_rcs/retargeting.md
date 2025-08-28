---
nav_title: Reorientación de usuarios
article_title: Reorientación de usuarios
description: "Este artículo de referencia explica cómo los usuarios pueden reorientar sus mensajes según las interacciones de un usuario con SMS y RCS."
page_type: reference
page_order: 4
alias: /sms_mms_rcs_user_retargeting/
tool:
  - Campaigns
channel:
  - SMS
  - MMS
  - RCS

---

# Reorientación de usuarios

> Además de cambiar el estado de suscripción del usuario y enviar respuestas automáticas basadas en palabras clave entrantes, Braze también registrará las interacciones con el perfil del usuario para filtrar y activar mensajes.<br><br>Estos filtros y desencadenantes te permiten filtrar acciones basadas en usuarios a los que se han enviado o que han respondido a campañas de SMS, MMS y RCS, o interactuar más con usuarios que han hecho clic en URL acortadas.

{% alert tip %}
Para obtener más información sobre las palabras clave personalizadas y cómo configurar la mensajería bidireccional para aprovechar estas opciones de reorientación, visite nuestro artículo sobre [palabras clave personalizadas]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/keyword_handling/).
{% endalert %}  

## Opciones de reorientación

{% alert note %}
Al crear audiencias con retargeting de usuarios, es posible que desee incluir o excluir a determinados usuarios en función de sus preferencias, y con el fin de cumplir con las leyes de privacidad, como el derecho de "No vender ni compartir" en virtud de la CUP. Los vendedores deben implementar los filtros pertinentes para la elegibilidad de los usuarios dentro de sus criterios de entrada de Canvas y/o Campaña.
{% endalert %}

### Filtrar usuarios por SMS, MMS y RCS

Los usuarios pueden ser filtrados por cuándo recibieron por última vez un SMS, MMS o RCS o si han recibido un SMS, MMS o RCS de una campaña específica. Los filtros se pueden establecer en el paso **Audiencias objetivo** del creador de campañas. 

**Filtrar por último recibido SMS/MMS/RCS**<br>
![Filtro de segmentación Últimos SMS recibidos después del 8 de diciembre de 2020.]({% image_buster /assets/img/sms/filter2.png %})

**Filtrar por mensajes recibidos de la campaña SMS/MMS/RCS **<br>
Filtra los usuarios que han recibido un mensaje de una campaña específica. Con este filtro, también tienes la opción de filtrar a los que no han recibido mensajes de una campaña. <br>
![Filtro de segmentación Ha recibido un mensaje de la campaña "SMS retargeting".]({% image_buster /assets/img/sms/filter1.png %})

### Desencadenar mensajes a medida que los usuarios reciben SMS, MMS o RCS {#trigger-messages}

Para desencadenar mensajes a medida que los usuarios reciben mensajes SMS, MMS o RCS de una campaña específica, selecciona **Interactuar con campaña** como acción desencadenante de una campaña basada en acciones. A continuación, selecciona **Recibir SMS** y la campaña de SMS, MMS o RCS que quieras utilizar.

![]({% image_buster /assets/img/sms/trigger.png %})

### Filtrar por enlaces de seguimiento avanzados

Vuelva a dirigirse a los usuarios que hayan hecho clic en campañas con [enlaces de seguimiento avanzados]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/link_shortening/).
Sólo las campañas que tengan activado el seguimiento avanzado aparecerán en los siguientes desplegables:

**Reorientar a los usuarios que han hecho clic en una campaña específica de SMS, MMS o RCS**
1. Cree un segmento utilizando el filtro **Campaña clicada/abierta**.
2. Selecciona **el enlace sms acortado clicado**.
3. Elija la campaña deseada.

![]({% image_buster /assets/img/sms/retargeting5.png %})

**Reorientar a los usuarios que han hecho clic en un paso específico en Canvas**
1. Cree un segmento utilizando el filtro **Paso pulsado/abierto**.
2. Selecciona **el enlace sms acortado clicado**.
3. Elija el lienzo y el paso de lienzo deseados.

![]({% image_buster /assets/img/keyword_example1.jpg %})

## Reorientación a categorías específicas de palabras clave

Además de las tres categorías de palabras clave predeterminadas (Opt-in, Opt-out y Ayuda), también puede crear hasta 25 categorías de palabras clave propias, lo que le permite identificar palabras clave y respuestas arbitrarias. Estas categorías pueden utilizarse para filtrar y reorientar. Para saber más sobre las categorías globales de palabras clave y cómo configurarlas, consulta [Procesamiento de palabras clave]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/). 

### Filtrar por recencia

Filtra la frecuencia con la que un usuario responde a tu programa de SMS, MMS o RCS. Este filtro evaluará la última fecha en la que un usuario envió un mensaje entrante que esté dentro de una de las categorías de palabras clave. 

![Filtro de segmentación Último SMS enviado al grupo de suscripción "Marketing SMS" con la palabra clave "Adhesión voluntaria" después del 11 de agosto de 2020.]({% image_buster /assets/img/sms/retargeting1.png %})

### Filtrar por campaña o atribución Canvas

Filtra a los usuarios que hayan respondido a una campaña específica de SMS, MMS o RCS o a un componente de Canvas, una categoría de palabras clave o una etiqueta.

**Filtrar por responder a una campaña específica con categoría de palabra clave**<br>
![Campaña con el filtro "Ha respondido al SMS" para la campaña "SMS-283" "Promoción". Debajo del filtro, la característica menciona "Este filtro caducará 25 meses después de que se envíe el último mensaje desde "Promoción" si no se está utilizando en ninguna campaña activa."]({% image_buster /assets/img/sms/clicked_opened_campaign.png %})

**Filtrar por respuesta a una campaña o Canvas con una etiqueta específica**
![Campaña con el filtro "Ha respondido a SMS" para campaña o Canvas con etiqueta "Servicio de mensajería de acera C".]({% image_buster /assets/img/sms/clicked_opened_campaign_canvas_tag.png %})

**Filtrar por respuesta a un paso específico**
![Campaña con el filtro "Ha respondido a SMS" para el paso "SMS Doble Opt" "Paso - Ayuda".]({% image_buster /assets/img/sms/clicked_opened_step.png %})

### Mensajes de activación por palabra clave

Los mensajes pueden activarse a medida que los usuarios envían mensajes entrantes basándose en categorías de palabras clave (el usuario envió cualquiera de las palabras clave) u otras palabras clave (el usuario envió una palabra clave que no entra en ninguna de las categorías existentes). Estos desencadenantes se configuran en el paso Entrega del constructor de campañas.

Cuando se evalúa si un mensaje entrante cumple un evento desencadenante definido, los espacios iniciales y finales se eliminan antes de que comience la evaluación.

{% alert tip %}
Si un Canvas basado en acciones es desencadenado por un mensaje SMS o MMS entrante, puedes hacer referencia a [las propiedades SMS Liquid compatibles]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/) en cualquier paso en Canvas hasta la siguiente ruta de acción.
{% endalert %}

**Activación por categoría de palabras clave entrantes**<br>
![Campaña SMS basada en acciones con el filtro de segmentación Palabra clave enviada "Adhesión voluntaria" al grupo de suscripción "Marketing SMS".]({% image_buster /assets/img/sms/retargeting2.png %}){: style="margin-top:10px;"}

**Activación por palabras clave arbitrarias**<br>
Tenga en cuenta que al activar un mensaje en una respuesta de palabra clave "Otra", tendrá la oportunidad de evaluar el cuerpo de la palabra clave en una coincidencia de texto exacta. Esta coincidencia sigue las mismas reglas que las anotadas: Sólo se procesará el **mensaje exacto, de una sola palabra** ( _sin distinguir_ mayúsculas de minúsculas). Una palabra clave enviada de `Hello Braze!` no coincidiría con los criterios mostrados en el siguiente ejemplo.
![Campaña de mensajería SMS basada en acciones con la categoría de palabras clave "Otros", en la que el cuerpo del mensaje es exactamente "Hola" o "Eh".]({% image_buster /assets/img/sms/retargeting3.png %}){: style="margin-top:10px;"}

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

[16]: {% image_buster /assets/img/keyword_example1.jpg %}
[16]: {% image_buster /assets/img/sms/retargeting4.png %}
