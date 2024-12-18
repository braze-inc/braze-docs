---
nav_title: Tratamiento personalizado de palabras clave
article_title: Tratamiento personalizado de palabras clave
page_order: 3
description: "Este artículo de referencia explica cómo Braze gestiona la mensajería SMS bidireccional y las respuestas automáticas. Esto incluye explicaciones sobre cómo funciona la activación de palabras clave, así como categorías de palabras clave personalizadas y soporte multilingüe."
page_type: reference
channel:
  - SMS

---

# Tratamiento personalizado de palabras clave

> Este artículo de referencia explica cómo Braze gestiona la mensajería SMS bidireccional y las respuestas automáticas. Esto incluye explicaciones sobre cómo funciona la activación de palabras clave, así como categorías de palabras clave personalizadas y soporte multilingüe.

## Mensajería bidireccional (respuestas personalizadas con palabras clave)

La mensajería bidireccional permite enviar mensajes y procesar las respuestas a esos mensajes. Requiere que los usuarios finales envíen una palabra clave a Braze, a la que el usuario recibirá una respuesta automática. Aplicada correctamente, la mensajería bidireccional puede ser una solución sencilla, inmediata y dinámica para el marketing de clientes, ahorrando tiempo y recursos en el camino.

## Gestión de palabras clave y respuestas automáticas

SMS con Braze te da la opción de crear activadores de palabras clave, respuestas personalizadas, definir conjuntos de palabras clave para varios idiomas y establecer categorías de palabras clave personalizadas. 

{% tabs %}
{% tab Añadir desencadenadores de palabras clave %}

#### Añadir activadores de palabras clave

Además de las palabras clave predeterminadas de inclusión y exclusión, también puede definir sus propias palabras clave para activar las respuestas de inclusión, exclusión y ayuda.

Para definir sus propias palabras clave, haga lo siguiente:

1. En el panel de control de Braze, vaya a **Audiencia** > **Grupos de suscripción** y seleccione su grupo de suscripción SMS.<br><br>
2. En **Palabras clave globales SMS**, haga clic en el icono del lápiz situado junto a la categoría de palabras clave a la que desea añadir una palabra clave. ![]({% image_buster /assets/img/sms/sms_keywords.png %})<br><br>
3. En la pestaña que se abre, añada una palabra clave que desee que active esta categoría de palabras clave. Tenga en cuenta que las palabras clave no distinguen entre mayúsculas y minúsculas, y que las palabras clave universales como `START`, `YES` y `UNSTOP` no se pueden cambiar. ![Editar palabras clave para la categoría "Adhesión voluntaria". Las palabras clave añadidas son "START", "UNSTOP" y "YES". El campo de mensaje de respuesta dice "Te has dado de baja de los mensajes de este número. Responde AYUDA para obtener ayuda. Responde STOP para darse de baja. Pueden aplicarse tarifas de mensajes y datos".]({% image_buster /assets/img/sms/keyword_edit2.png %})

Las siguientes reglas se aplican a las palabras clave y a las respuestas a palabras clave:

| Palabras claves | Respuestas a palabras clave |
| -------- | ----------------- |
| \- Caracteres codificados en UTF-8 válidos<br>\- Máximo de 20 palabras clave por categoría en total<br>\- Longitud máxima de 34 caracteres<br>\- Longitud mínima de 1 carácter <br>\- No puede contener espacios<br>\- Debe distinguir entre mayúsculas y minúsculas y ser único para todo el grupo de suscripción | \- No puede estar en blanco<br>\- Longitud máxima de 300 caracteres<br>\- Caracteres UTF-8 válidos |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert tip %}
¿Le interesa saber cómo puede utilizar estas palabras clave en sus campañas y lienzos para reorientar y activar mensajes? Visite nuestro artículo [sobre SMS retargeting]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/retargeting/) para obtener más información.
{% endalert %}
{% endtab %}

{% tab Gestionar las respuestas %}

#### Gestionar las respuestas

Puede gestionar sus propias respuestas que se envían a los usuarios después de que escriban una palabra clave en una categoría de palabras clave específica.

1. En el panel de control de Braze, vaya a **Audiencia** > **Grupos de suscripción** y seleccione su grupo de suscripción SMS. <br><br>
2. En **Palabras clave globales SMS**, seleccione una categoría de palabras clave para editar una respuesta seleccionando el icono del lápiz. ![]({% image_buster /assets/img/sms/sms_keywords.png %})<br><br> 
3. En la pestaña que se abre, edita tu respuesta. Tenga en cuenta nuestras [seis reglas para cumplirlas correctamente]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_laws_and_regulations/#the-six-rules-to-get-compliance-right) al crear su respuesta, y lea las siguientes reglas que se aplican a las palabras clave y a las respuestas con palabras clave. ![Respuestas]({% image_buster /assets/img/sms/keyword_home.png %})<br><br>
4. Para acortar automáticamente las URL estáticas en su respuesta, seleccione la opción **Acortar enlaces**. El contador de caracteres se actualizará para mostrar la longitud prevista de la URL acortada. ![Un GIF que muestra la actualización del contador de caracteres cuando está activada la opción "Acortar enlaces".]({% image_buster /assets/img/sms/link_shortening.gif %}){: style="max-width:50%;"}

##### Consideraciones

| Palabras claves | Respuestas a palabras clave |
| -------- | ----------------- |
| \- Caracteres codificados en UTF-8 válidos<br>\- Máximo de 20 palabras clave por categoría en total<br>\- Longitud máxima de 34 caracteres<br>\- Longitud mínima de 1 carácter <br>\- No puede contener espacios<br>\- Debe distinguir entre mayúsculas y minúsculas y ser único para todo el grupo de suscripción | \- No puede estar en blanco<br>\- Longitud máxima de 300 caracteres<br>\- Caracteres UTF-8 válidos |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

{% alert tip %}
Si un lienzo basado en acciones se activa mediante un mensaje SMS entrante, puede hacer referencia a las propiedades de SMS en el primer [paso de mensaje]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) del lienzo.
{% endalert %}

## Asistencia en varios idiomas

Al enviar a determinados países, es posible que el remitente deba admitir palabras clave de entrada y respuestas de salida con un idioma local. Para ello, Braze permite crear una configuración de palabras clave específica para cada idioma.
![][16]{: style="float:right;max-width:40%;margin-left:10px;"}

### Creación de palabras clave específicas para cada idioma

Haga clic en **Añadir un idioma** y seleccione su idioma de destino o busque un idioma en el menú desplegable.

{% alert important %}
Tenga en cuenta que otros idiomas no vienen con palabras clave y respuestas preestablecidas como el inglés, por lo que los remitentes tendrán que trabajar con sus equipos de marketing y jurídicos para añadir las palabras clave necesarias a este conjunto. De lo contrario, Braze no gestionará los mensajes entrantes localizados para esos idiomas.
{% endalert %}

Si necesita eliminar un idioma, haga clic en el botón **Eliminar idioma** de la parte inferior derecha.

![Página de Palabras clave globales de SMS con la pestaña "Francés" seleccionada. Existen pestañas adicionales para cada idioma añadido.][5]

## Categorías de palabras clave personalizadas

Además de las tres categorías de palabras clave predeterminadas (Opt-in, Opt-out y Ayuda), también puede crear hasta 25 categorías de palabras clave propias. Esto le permite identificar palabras clave arbitrarias y configurar respuestas específicas para su negocio. Un ejemplo de categoría podría ser "PROMO" o "DESCUENTO", que podría suscitar una respuesta sobre las promociones que tienen lugar este mes. 

Estas palabras clave personalizadas funcionan de forma "permanente", lo que significa que cualquier usuario suscrito a su servicio de mensajes puede enviar mensajes de texto con palabras clave y recibir una respuesta en cualquier momento. Además de este comportamiento, también tiene la opción de definir palabras clave específicas a las que sólo se puede enviar en [determinados momentos]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/keyword_handling/#lifecycle-specific-keywords) del ciclo de vida del usuario. 

![Palabras clave para una categoría "Dobleoptin". Si un usuario escribe "Y", recibe el mensaje "Gracias por confirmar tu inscripción en Hair Cuttery SMS".][12]

### Crear una categoría personalizada

Para crear una categoría de palabras clave personalizada, haga lo siguiente:

1. Edite el grupo de suscripción correspondiente.
2. Haga clic en **Añadir palabra clave personalizada**. ![][13]{: style="max-width:90%;"}
3. Proporcione un nombre de categoría de palabras clave y defina qué palabras clave puede escribir un usuario para recibir el mensaje de respuesta.

Una vez creada esta categoría de palabras clave, estará disponible para [filtrar y activar]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/retargeting/) en sus campañas y Canvases.

Las palabras clave creadas en categorías de palabras clave personalizadas cumplen todas las normas y validaciones para la creación de nuevas palabras clave. 

### Palabras clave específicas del ciclo de vida

Si tiene un caso de uso en el que desea limitar cuándo un cliente puede enviar una palabra clave específica durante su ciclo de vida (por ejemplo, durante su primera incorporación inicial) para recibir una respuesta, puede utilizar el activador **SMS entrantes enviados al grupo de suscripción dentro de la categoría de palabras clave OTRA** en su campaña o Canvas y definir las palabras clave que sus usuarios pueden enviar en un momento dado.

Este activador admite el filtrado del mensaje entrante específico mediante comparaciones de si el mensaje es o no es, así como reglas regex de coincidencia o no coincidencia para validar la entrada del usuario.

#### Canvas

![Paso Canvas basado en acciones con el activador Enviar SMS entrantes al grupo de suscripción "Servicio de mensajería" dentro de la categoría de palabras clave "Otros" cuando el cuerpo del mensaje coincida con la expresión regular "caret symbol skip."][14]{: style="max-width:90%;"}

#### Campaña

![Campaña basada en acciones con el disparador Enviar SMS entrantes al grupo de suscripción "Servicio de mensajes de marketing A" dentro de la categoría de palabras clave "Otros" donde el cuerpo del mensaje es "Palabra clave1" o es "Palabra clave2" o no es "Palabra clave A".][15]{: style="max-width:90%;"}

### Palabras clave desconocidas

Aunque no es obligatorio, recomendamos encarecidamente configurar una respuesta automática para cuando los usuarios envíen SMS con palabras clave que no coincidan con una palabra clave existente. Este mensaje notificará al usuario que la palabra clave no es reconocida y le ofrecerá alguna orientación. 

Esto puede hacerse creando una campaña de SMS con un mensaje como "¡Lo sentimos! No reconocimos esa palabra clave, el texto STOP para parar o HELP para ayudar". A continuación, en el paso de entrega, seleccione **Entrega basada en acciones** y utilice el activador **Envío de SMS entrantes al grupo de suscripción dentro de la categoría de palabras clave OTRO**.

![]({% image_buster /assets/img/sms/sms_other.png %})

{% alert tip %}
¿Le interesa saber cómo puede utilizar estas palabras clave y categorías de palabras clave en sus campañas y lienzos para reorientar y activar mensajes? Visite nuestro artículo [sobre SMS retargeting]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/retargeting/) para obtener más información.
{% endalert %}

[oblink]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#setup-process
[1]: {% image_buster /assets/img/sms/keyword_edit2.png %}
[2]: {% image_buster /assets/img/sms/keyword_home.png %}
[unknown]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/unknown_phone_numbers/
[endpoint]: {{site.baseurl}}/api/endpoints/user_data/post_user_alias/
[IMAGE2]: {% image_buster /assets/img/sms/sms_message_body.png %}
[5]: {% image_buster /assets/img/sms/multi-language2.png %}
[12]: {% image_buster /assets/img/sms/sms_custom_keyword.png %}
[13]: {% image_buster /assets/img/sms/sms_custom_step.png %}
[14]: {% image_buster /assets/img/sms/canvas_trigger.png %}
[15]: {% image_buster /assets/img/sms/campaign_trigger.png %}
[16]: {% image_buster /assets/img/sms/multi-language.png %}
