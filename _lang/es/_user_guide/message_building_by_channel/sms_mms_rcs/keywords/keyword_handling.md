---
nav_title: Manejo personalizado de palabras clave
article_title: Manejo personalizado de palabras clave
page_order: 3
description: "Este artículo de referencia explica cómo Braze gestiona la mensajería bidireccional SMS, MMS y RCS y las respuestas automáticas. Esto incluye explicaciones sobre cómo desencadenar palabras clave, así como categorías de palabras clave personalizadas y soporte multilingüe."
page_type: reference
channel:
  - SMS
  - MMS
  - RCS

---

# Manejo personalizado de palabras clave

> Este artículo de referencia explica cómo Braze gestiona la mensajería bidireccional SMS, MMS y RCS y las respuestas automáticas. Esto incluye explicaciones sobre cómo desencadenar palabras clave, así como categorías de palabras clave personalizadas y soporte multilingüe.

## Mensajería bidireccional (respuestas personalizadas con palabras clave)

La mensajería bidireccional te permite enviar mensajes y procesar las respuestas a esos mensajes. Requiere que los usuarios finales envíen una palabra clave a Braze, a la que ese usuario recibirá una respuesta automática. Aplicada correctamente, la mensajería bidireccional puede ser una solución sencilla, inmediata y dinámica para el marketing del cliente, ahorrando tiempo y recursos por el camino.

## Gestión de palabras clave y respuestas automáticas

SMS, MMS y RCS con Braze te da la opción de crear desencadenantes de palabras clave, respuestas personalizadas, definir conjuntos de palabras clave para varios idiomas y establecer categorías de palabras clave personalizadas. 

{% tabs %}
{% tab Add Keyword Triggers %}

#### Añadir desencadenadores de palabras clave

Además de las palabras clave predeterminadas de adhesión voluntaria y exclusión voluntaria, también puedes definir tus propias palabras clave para desencadenar respuestas de adhesión voluntaria, exclusión voluntaria y ayuda.

Para definir tus propias palabras clave, haz lo siguiente:

1. En el panel de Braze, ve a **Audiencia** > **Gestión de grupos de suscripción** y selecciona un grupo de suscripción **SMS/MMS/RCS**.<br><br>
2. En **Palabras clave globales**, selecciona el icono del lápiz junto a la categoría de palabras clave a la que quieras añadir una palabra clave. Palabras clave de adhesión voluntaria en las que aparece el icono del lápiz.]({% image_buster /assets/img/sms/sms_keywords.png %})<br><br>
3. En la pestaña que se abre, añade una palabra clave que quieras desencadenar en esta categoría de palabras clave. Ten en cuenta que las palabras clave no distinguen entre mayúsculas y minúsculas, y que las palabras clave universales como `START`, `YES` y `UNSTOP` no se pueden cambiar. Edición de palabras clave para la categoría "Adhesión voluntaria". Las palabras clave añadidas son "INICIAR", "PARAR" y "SÍ". El campo del mensaje de respuesta dice "Te has dado de baja de los mensajes de este número. Responde AYUDA para obtener ayuda. Responder a STOP para cancelar suscripción. Pueden aplicarse tasas de mensajería y datos".]({% image_buster /assets/img/sms/keyword_edit2.png %})

Las siguientes reglas se aplican a las palabras clave y a las respuestas con palabras clave:

| Palabras clave | Respuestas a palabras clave |
| -------- | ----------------- |
| \- Caracteres válidos codificados en UTF-8<br>\- Máximo de 20 palabras clave por categoría en total<br>\- Longitud máxima de 34 caracteres<br>\- Longitud mínima de 1 carácter <br>\- No puede contener espacios<br>\- Debe ser insensible a mayúsculas y minúsculas y único en todo el grupo de suscripción | \- No puede estar en blanco<br>\- Longitud máxima de 300 caracteres<br>\- Caracteres UTF-8 válidos |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert tip %}
¿Te interesa ver cómo se pueden utilizar estas palabras clave en tus campañas y Canvases para reorientar y desencadenar mensajes? Visita [Reorientación]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/retargeting/) para más información.
{% endalert %}
{% endtab %}

{% tab Manage responses %}

#### Administrar las respuestas

Puedes gestionar tus propias respuestas que se envían a los usuarios después de que escriban una palabra clave en una categoría específica de palabras clave.

1. En el panel de Braze, ve a **Audiencia** > **Gestión de grupos de suscripción** y selecciona un grupo de suscripción **SMS/MMS/RCS**. <br><br>
2. En **Palabras clave globales**, selecciona una categoría de palabras clave para editar una respuesta seleccionando el icono del lápiz. Palabras clave de adhesión voluntaria en las que aparece el icono del lápiz.]({% image_buster /assets/img/sms/sms_keywords.png %})<br><br> 
3. En la pestaña que se abre, edita tu respuesta. Ten en cuenta nuestras [seis reglas para cumplirlas correctamente]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_laws_and_regulations/#the-six-rules-to-get-compliance-right) cuando crees tu respuesta, y lee las siguientes reglas que se aplican a las palabras clave y a las respuestas con palabras clave. \![Respuestas]({% image_buster /assets/img/sms/keyword_home.png %}){: style="max-width:70%;"}<br><br>
4. Para acortar automáticamente las URL estáticas en tu respuesta, selecciona el alternador **Acortamiento de enlaces**. El contador de caracteres se actualizará para mostrar la longitud prevista de la URL acortada. Un GIF que muestra cómo se actualiza el contador de caracteres cuando está activado el botón "Acortar enlace".]({% image_buster /assets/img/sms/link_shortening.gif %}){: style="max-width:60%;"}

##### Consideraciones

| Palabras clave | Respuestas a palabras clave |
| -------- | ----------------- |
| \- Caracteres válidos codificados en UTF-8<br>\- Máximo de 20 palabras clave por categoría en total<br>\- Longitud máxima de 34 caracteres<br>\- Longitud mínima de 1 carácter <br>\- No puede contener espacios<br>\- Debe ser insensible a mayúsculas y minúsculas y único en todo el grupo de suscripción | \- No puede estar en blanco<br>\- Longitud máxima de 300 caracteres<br>\- Caracteres UTF-8 válidos |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

{% alert tip %}
Si un Canvas basado en acciones es desencadenado por un mensaje SMS, MMS o RCS entrante, puedes hacer referencia a las propiedades de SMS, MMS o RCS en el primer [paso]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) en Canvas.
{% endalert %}

## Soporte multilingüe

Al enviar a determinados países, puede ser necesario que el remitente admita palabras clave de entrada y respuestas de salida con un idioma local. Para ello, Braze te permite crear una configuración de palabras clave específica para cada idioma.
\![Desplegable que muestra los idiomas a añadir como configuración de palabras clave.]({% image_buster /assets/img/sms/multi-language.png %}){: style="float:right;max-width:50%;margin-left:10px;"}

### Crear palabras clave específicas para cada idioma

Selecciona **Añadir un idioma** y selecciona tu idioma de destino o busca un idioma en el desplegable.

{% alert important %}
Los idiomas que no son el inglés no vienen con palabras clave y respuestas preestablecidas, por lo que los remitentes tendrán que trabajar con sus equipos jurídicos y de marketing para añadir las palabras clave necesarias a este conjunto. De lo contrario, Braze no gestionará los mensajes entrantes localizados para esos idiomas.
{% endalert %}

Si necesitas eliminar una lengua, selecciona el botón **Eliminar lengua** en la parte inferior derecha.

Página "Palabras clave globales" con la pestaña "Italiano" seleccionada. Existen pestañas adicionales para cada idioma añadido.]({% image_buster /assets/img/sms/multi-language2.png %})

## Categorías personalizadas de palabras clave

Además de las tres categorías de palabras clave predeterminadas (adhesión voluntaria, exclusión voluntaria y ayuda), también puedes crear hasta 25 categorías de palabras clave propias. Esto te permite identificar palabras clave arbitrarias y configurar respuestas específicas para tu negocio. Un ejemplo de categoría podría ser "PROMO" o "DESCUENTO", que podría suscitar una respuesta sobre las promociones que están teniendo lugar este mes. 

Estas palabras clave personalizadas funcionan de forma "permanente", lo que significa que cualquier usuario suscrito a tu servicio de mensajería puede enviar mensajes de texto con palabras clave y recibir una respuesta en cualquier momento. Además de este comportamiento, también tienes la opción de definir palabras clave específicas a las que sólo se puede enviar en [determinados momentos]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/keyword_handling/#lifecycle-specific-keywords) del ciclo de vida de tu usuario. 

\![Palabras clave para una categoría "Promoción". Si un usuario envía un mensaje de texto con la palabra "YO", recibirá un mensaje con un código promocional.]({% image_buster /assets/img/sms/sms_custom_keyword.png %})

### Crear una categoría personalizada

Para crear una categoría personalizada de palabras clave, haz lo siguiente:

1. Edita el grupo de suscripción adecuado.
2. Selecciona **Añadir palabra clave personalizada**. Campos para añadir nuevas palabras clave.]({% image_buster /assets/img/sms/sms_custom_step.png %}){: style="max-width:90%;"}
3. Proporciona un nombre de categoría de palabras clave y define qué palabras clave puede escribir un usuario para recibir el mensaje de respuesta.

Una vez creada esta categoría de palabras clave, estará disponible para [filtrar y desencadenar]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/retargeting/) en tus campañas y Canvases.

Las palabras clave creadas en categorías de palabras clave personalizadas cumplen todas las normas y validaciones para la creación de nuevas palabras clave. 

### Palabras clave específicas del ciclo de vida

Si tienes un caso de uso en el que te gustaría limitar cuándo un cliente puede enviar una palabra clave específica durante su ciclo de vida (por ejemplo, durante su primera incorporación inicial) para recibir una respuesta, puedes utilizar el desencadenante **Enviar SMS entrantes al grupo de suscripción dentro de la categoría de palabras clave OTRA** en tu campaña o Canvas y definir las palabras clave que tus usuarios pueden enviar en un momento dado.

Este desencadenador admite filtrar el mensaje entrante específico utilizando es o no es comparaciones del mensaje, así como coincide o no coincide con reglas regex para validar la entrada del usuario.

#### Canvas

\![Paso en Canvas basado en una acción con el desencadenante Enviar SMS entrantes al grupo de suscripción "Servicio de mensajería" dentro de la categoría de palabras clave "Otros" en la que el cuerpo del mensaje coincide con la expresión regular "símbolo de intercalación omitir".]({% image_buster /assets/img/sms/canvas_trigger.png %}){: style="max-width:90%;"}

#### Campaña

\![Campaña basada en acciones con el desencadenante Enviar SMS entrantes al grupo de suscripción "Servicio de mensajería de marketing A" dentro de la categoría de palabras clave "Otros" donde el cuerpo del mensaje es "Palabra clave1" o es "Palabra clave2" o no es "Palabra clave A".]({% image_buster /assets/img/sms/campaign_trigger.png %}){: style="max-width:90%;"}

### Tratar con palabras clave desconocidas

Aunque no es obligatorio, recomendamos encarecidamente configurar una respuesta automática para cuando los usuarios envíen palabras clave entrantes que no coincidan con una palabra clave existente. Este mensaje notificará al usuario que la palabra clave no se reconoce y le ofrecerá alguna orientación. 

Esto puede hacerse creando una campaña de SMS, MMS o RCS con un mensaje como "¡Lo siento! No reconocimos esa palabra clave, el texto STOP para parar o AYUDA para ayudar". A continuación, en el paso de entrega, selecciona **Entrega basada en acciones** y utiliza el desencadenante **Enviado SMS entrantes al grupo de suscripción dentro de la categoría de palabras clave OTROS**.

Envío basado en acciones para una campaña con el desencadenante "Envío de SMS entrantes al grupo de suscripción dentro de la categoría de palabras clave "Otros"".]({% image_buster /assets/img/sms/sms_other.png %})

{% alert tip %}
¿Te interesa ver cómo se pueden utilizar estas palabras clave y categorías de palabras clave en tus campañas y Canvases para reorientar y desencadenar mensajes? Visita [Reorientación]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/retargeting/) para más información.
{% endalert %}

