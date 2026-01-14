---
nav_title: Reorientar al usuario
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

# Reorientar al usuario

> Además de cambiar el estado de suscripción del usuario y enviar respuestas automáticas basadas en palabras clave entrantes, Braze también registrará las interacciones con el perfil de usuario para filtrar y desencadenar mensajes.<br><br>Estos filtros y desencadenantes te permiten filtrar acciones basadas en usuarios a los que se han enviado o que han respondido a campañas de SMS, MMS y RCS, o interactuar más con usuarios que han hecho clic en URL acortadas.

{% alert tip %}
Para saber más sobre las palabras clave personalizadas y cómo configurar la mensajería bidireccional para aprovechar estas opciones de reorientación, visita nuestro artículo sobre [palabras clave personalizadas]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/keyword_handling/).
{% endalert %}  

## Opciones de reorientación

{% alert note %}
Cuando construyas audiencias con reorientación de usuarios, es posible que desees incluir o excluir a determinados usuarios en función de sus preferencias, y con el fin de cumplir con las leyes de privacidad, como el derecho de "No vender ni compartir" en virtud de la CUP. Los especialistas en marketing deben aplicar los filtros pertinentes para la elegibilidad de los usuarios dentro de los criterios de entrada de su Canvas y/o campaña.
{% endalert %}

### Filtrar usuarios por SMS, MMS y RCS

Los usuarios pueden ser filtrados por cuándo recibieron por última vez un SMS, MMS o RCS o si han recibido un SMS, MMS o RCS de una campaña específica. Los filtros se pueden establecer en el paso **Audiencias objetivo** del creador de campañas. 

**Filtrar por último SMS/MMS/RCS recibido**<br>
\![Filtro de segmentación Último SMS recibido después del 8 de diciembre de 2020.]({% image_buster /assets/img/sms/filter2.png %})

**Filtrar por mensajes recibidos de la campaña SMS/MMS/RCS**<br>
Filtra los usuarios que han recibido un mensaje de una campaña específica. Con este filtro, también tienes la opción de filtrar a los que no han recibido mensajes de una campaña. <br>
\![Filtro de segmentación Ha recibido un mensaje de la campaña "SMS reorientación".]({% image_buster /assets/img/sms/filter1.png %})

### Desencadenar mensajes a medida que los usuarios reciben SMS, MMS o RCS {#trigger-messages}

Para desencadenar mensajes a medida que los usuarios reciben mensajes SMS, MMS o RCS de una campaña específica, selecciona **Interactuar con campaña** como acción desencadenante de una campaña basada en acciones. A continuación, selecciona **Recibir SMS** y la campaña de SMS, MMS o RCS que quieras utilizar.

\![]({% image_buster /assets/img/sms/trigger.png %})

### Filtrar por enlaces de seguimiento avanzado

Reorienta a los usuarios que han hecho clic en campañas con [enlaces de seguimiento avanzado]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/link_shortening/).
Sólo las campañas que tengan habilitado el seguimiento avanzado aparecerán en los siguientes desplegables:

**Reorientar a los usuarios que han hecho clic en una campaña específica de SMS, MMS o RCS**
1. Crea un segmento utilizando el filtro **Campaña clicada/abierta**.
2. Selecciona **el enlace sms acortado clicado**.
3. Elige la campaña deseada.

\![]({% image_buster /assets/img/sms/retargeting5.png %})

**Reorientar a los usuarios que han hecho clic en un paso específico de Canvas**
1. Crea un segmento utilizando el filtro **Paso hecho clic/Abierto**.
2. Selecciona **el enlace sms acortado clicado**.
3. Elige el Canvas y el paso en Canvas deseados.

\![]({% image_buster /assets/img/keyword_example1.jpg %})

## Reorientación específica por categoría de palabras clave

Además de las tres categorías predeterminadas de palabras clave (adhesión voluntaria, exclusión voluntaria y ayuda), también puedes crear hasta 25 categorías de palabras clave propias, lo que te permite identificar palabras clave y respuestas arbitrarias. Estas categorías pueden utilizarse para filtrar y reorientar. Para saber más sobre las categorías globales de palabras clave y cómo configurarlas, consulta [Procesamiento de palabras clave]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/). 

### Filtrar por recencia

Filtra la frecuencia con la que un usuario responde a tu programa de SMS, MMS o RCS. Este filtro evaluará la última fecha en la que un usuario envió un mensaje entrante que esté dentro de una de las categorías de palabras clave. 

\![Filtro de segmentación Último SMS enviado al grupo de suscripción "Marketing SMS" con la palabra clave "Adhesión voluntaria" después del 11 de agosto de 2020.]({% image_buster /assets/img/sms/retargeting1.png %})

### Filtrar por atributo de campaña o Canvas

Filtra a los usuarios que hayan respondido a una campaña específica de SMS, MMS o RCS o a un componente de Canvas, una categoría de palabras clave o una etiqueta.

**Filtrar por responder a una campaña específica con categoría de palabra clave**<br>
\![Campaña con el filtro "Ha respondido a SMS" para la campaña "SMS-283" "Promoción". Debajo del filtro, la característica menciona "Este filtro caducará 25 meses después de que se envíe el último mensaje desde "Promoción" si no se está utilizando en ninguna campaña activa."]({% image_buster /assets/img/sms/clicked_opened_campaign.png %})

**Filtrar por responder a una campaña o Canvas con una etiqueta específica**
\![Campaña con el filtro "Ha respondido a SMS" para campaña o Canvas con etiqueta "Servicio de mensajería en acera C".]({% image_buster /assets/img/sms/clicked_opened_campaign_canvas_tag.png %})

**Filtrar por haber respondido a un paso concreto**
\![Campaña con el filtro "Ha respondido a SMS" para el paso "SMS Doble Opt" "Paso - Ayuda".]({% image_buster /assets/img/sms/clicked_opened_step.png %})

### Desencadenar mensajes por palabra clave

Se pueden desencadenar mensajes a medida que los usuarios envían mensajes entrantes basados en categorías de palabras clave (el usuario envió cualquiera de las palabras clave) u otras palabras clave (el usuario envió una palabra clave que no entra en ninguna de las categorías existentes). Estos desencadenantes se configuran en el paso Entrega del constructor de campañas.

Al evaluar si un mensaje entrante cumple un evento desencadenante definido, se eliminan los espacios iniciales y finales antes de que comience la evaluación.

{% alert tip %}
Si un Canvas basado en acciones es desencadenado por un mensaje SMS o MMS entrante, puedes hacer referencia a [las propiedades SMS Liquid compatibles]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/) en cualquier paso en Canvas hasta la siguiente ruta de acción.
{% endalert %}

**Desencadenar por categoría de palabras clave entrantes**<br>
\![Campaña SMS basada en acciones con el filtro de segmentación Palabra clave enviada "Adhesión voluntaria" al grupo de suscripción "Marketing por SMS".]({% image_buster /assets/img/sms/retargeting2.png %}){: style="margin-top:10px;"}

**Desencadenar por palabras clave arbitrarias**<br>
Nota: cuando desencadenes un mensaje en una respuesta de palabra clave "Otra", tendrás la oportunidad de evaluar el cuerpo de la palabra clave en una coincidencia de texto exacta. Este partido sigue las mismas reglas que las anotadas: Sólo se procesará el **mensaje exacto, de una sola palabra** ( _sin distinguir_ mayúsculas de minúsculas). Una palabra clave enviada de `Hello Braze!` no cumpliría los criterios que se muestran en el siguiente ejemplo.
\![Campaña de SMS basada en acciones con la categoría de palabras clave "Otros" en la que el cuerpo del mensaje es exactamente "Hola" o "Eh".]({% image_buster /assets/img/sms/retargeting3.png %}){: style="margin-top:10px;"}

**Palabras clave de la plantilla**<br>
Al desencadenar una campaña o un componente de Canvas en un SMS o MMS entrante, puedes, opcionalmente, crear plantillas de los archivos adjuntos de texto o multimedia que tu usuario envió al cuerpo de tu campaña o Canvas con Liquid. Esto te habilitará para acceder a la respuesta del usuario, que luego podrás incluir en tu respuesta, aplicarle lógica condicional o cualquier otra cosa que puedas hacer con Liquid. 

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
