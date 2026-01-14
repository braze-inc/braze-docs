---
nav_title: "Crear un mensaje RCS"
article_title: Crear un mensaje RCS
page_order: 2
alias: /create_rcs_message/
description: "Este artículo explica cómo crear un mensaje RCS."
page_type: reference
channel:
  - RCS
---

# Crear un mensaje RCS

> Las campañas RCS son estupendas para llegar directamente a tus clientes y conversar con ellos de forma programática. Puedes utilizar Liquid y otros contenidos dinámicos para crear una experiencia personal con tus usuarios y crear un entorno que fomente y mejore una experiencia discreta del usuario con tu marca.

## Crear un mensaje RCS

### Paso 1: Elige dónde construir tu mensaje

¿No estás seguro de si tu mensaje debe enviarse mediante una campaña o un Canvas? Las campañas son mejores para campañas de mensajería únicas y sencillas, mientras que los lienzos son mejores para recorridos de usuario de varios pasos.

{% tabs %}
{% tab Campaign %}
1. Ve a **Mensajería** > **Campañas** y selecciona **Crear campaña**.
2. Selecciona **SMS/MMS/RCS** o, para campañas dirigidas a varios canales, selecciona **Multicanal**.
3. Pon a tu campaña un nombre claro y significativo.
4. Añade [equipos]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) y [etiquetas]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) según sea necesario.
   * Las etiquetas facilitan la búsqueda de tus campañas y la elaboración de informes a partir de ellas. Por ejemplo, al utilizar el [generador de informes]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/), puedes filtrar por determinadas etiquetas.

{: start="5"}
5\. Añade y nombra tantas variantes como necesites para tu campaña. Puedes elegir diferentes plataformas, tipos de mensaje y diseños para cada una de tus variantes añadidas. Para saber más sobre este tema, consulta [Multivariante y pruebas A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).
- **Pruebas de variantes SMS y RCS**: Braze te permite incluir variantes tanto de SMS como de RCS dentro de una misma campaña, permitiéndote comparar el rendimiento de cada una. Puedes añadir variantes de SMS y RCS durante el primer paso de la composición del mensaje.

{: start="6"}
6\. Selecciona un [grupo de suscripción]({{site.baseurl}}/sms_rcs_subscription_groups/) habilitado para RCS. Al seleccionar un grupo de suscripción, Braze añadirá automáticamente un filtro de segmentación, garantizando que sólo los usuarios suscritos reciban la campaña. Sólo se utilizarán los códigos largos y los códigos abreviados que pertenezcan a ese grupo de suscripción para enviar SMS a los usuarios objetivo.
- **SMS alternativo**: Braze recomienda encarecidamente que cada grupo de suscripción que contenga un remitente RCS incluya también al menos un código SMS de alternativa. Esto es importante para la capacidad de entrega en caso de que los mensajes RCS no se entreguen. Algunos motivos pueden ser la incompatibilidad del dispositivo del usuario y la cobertura incompleta del operador en un país o región determinados. Habilitando la alternativa de SMS, tu mensaje seguirá entregándose a tu usuario y nunca perderás la oportunidad de conectar con él.   

{: start="7"}
7\. Elige entre SMS y RCS. Antes de componer los mensajes RCS, elige el canal con el que los envías. Por lo general, recomendamos utilizar RCS siempre que sea posible, ya que ofrece importantes ventajas de interacción con el usuario en comparación con los SMS; sin embargo, siempre proporcionamos la opción de enviar con SMS para que tengas la máxima flexibilidad y control. 

\![Opciones para seleccionar un tipo de mensaje RCS o SMS/MMS.]({% image_buster /assets/img/rcs/rcs_message_type.png %}){: style="max-width:65%;"}

{% alert tip %}
Si todos los mensajes de tu campaña van a ser similares o van a tener el mismo contenido, redacta tu mensaje antes de añadir variantes adicionales. A continuación, puedes elegir **Copiar de variante** en el desplegable **Añadir variante**.
{% endalert %}

{% endtab %}
{% tab Canvas %}
1. [Crea tu Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) utilizando el compositor de Canvas.
2. Después de configurar tu Canvas, añade un paso en Canvas para mensajes **SMS/MMS/RCS**. 
3. Nombra tu paso con algo claro y significativo.
4. Selecciona un [grupo de suscripción]({{site.baseurl}}/sms_rcs_subscription_groups/) habilitado para RCS. Al seleccionar un grupo de suscripción, Braze añadirá automáticamente un filtro de segmentación, garantizando que sólo los usuarios suscritos reciban la campaña. Sólo los códigos largos y los códigos abreviados que pertenezcan a ese grupo de suscripción se utilizarán para dirigirse a los usuarios.
- **SMS alternativo**: Braze recomienda encarecidamente que cada grupo de suscripción que contenga un remitente RCS incluya también al menos un código SMS de alternativa. Esto es importante para la capacidad de entrega en caso de que los mensajes RCS no se entreguen. Algunos motivos pueden ser la incompatibilidad del dispositivo del usuario y la cobertura incompleta del operador en un país o región determinados. Habilitando la alternativa de SMS, tu mensaje seguirá entregándose a tu usuario y nunca perderás la oportunidad de conectar con él.

{: start="5"}
5\. Elige entre SMS y RCS. Antes de componer los mensajes RCS, elige el canal con el que los envías. Por lo general, recomendamos utilizar RCS siempre que sea posible, ya que ofrece importantes ventajas de interacción con el usuario en comparación con los SMS; sin embargo, siempre proporcionamos la opción de enviar con SMS para que tengas la máxima flexibilidad y control. 

\![Opciones para seleccionar un tipo de mensaje RCS o SMS/MMS.]({% image_buster /assets/img/rcs/rcs_message_type.png %}){: style="max-width:65%;"}

{% endtab %}
{% endtabs %}

### Paso 2: Selecciona tu tipo de mensaje RCS

Para el tipo de mensaje RCS, elige entre **Texto** o **Multimedia**.

\![Opciones para seleccionar un tipo de mensaje de Texto o Multimedia.]({% image_buster /assets/img/rcs/rcs_text_media.png %}){: style="max-width:65%;"}

{% tabs %}
{% tab Text %}
Como su nombre indica, los mensajes de texto RCS se centran en el texto como medio. Si escribes hasta 160 caracteres, el mensaje de RCS se factura como mensaje de sólo texto (o "básico"). Si superas los 160 caracteres o utilizas un elemento enriquecido, el mensaje se factura como un mensaje RCS enriquecido (o "único") (y el límite de caracteres aumenta a 3072 caracteres). 

#### Características

- Los tipos de mensajes de texto incluyen todas las características de los SMS. Sólo el seguimiento avanzado es posible para que el seguimiento de clics en URL te proporcione granularidad de informes a nivel de usuario. 
- Además, ahora tienes la opción de incluir atractivos botones de **Respuestas sugeridas** y **Acciones sugeridas** que impulsen las acciones de los usuarios con mayor interacción, como visitar una página de destino o realizar un pedido. 
    - **Las respuestas sugeridas** son botones que contienen respuestas sugeridas para que los usuarios hagan clic en ellas y las introduzcan previamente en su texto, eliminando la fricción de tener que pensar en una respuesta al proporcionarles un conjunto limitado de opciones. 
    - **Las Acciones sugeridas** son botones que inician una acción en el dispositivo del usuario. Suelen consistir en una o dos palabras descriptivas y un icono visual para ayudar al usuario a entender lo que hace el botón. Braze admite actualmente las Acciones sugeridas de OpenURL. Funciona de forma similar a una URL, en la que los usuarios que seleccionan el botón son redirigidos a una página web o a otra ubicación identificada con una URL. 

Un GIF de tres acciones sugeridas para un mensaje RCS que promociona los estilos de moda más actuales: "Realeza de cuento de hadas", "Academia atrevida" y "Enséñame tus otros estilos".]({% image_buster /assets/img/rcs/rcs_suggested_actions.gif %}){: style="max-width:70%;"}

#### Consideraciones

- Para los límites de caracteres en el texto, puedes escribir hasta 160 caracteres para un mensaje RCS de sólo texto (básico) o hasta 3072 para un mensaje RCS enriquecido (único). 
- Para los límites de botones, puedes añadir hasta cinco botones por mensaje. Estos botones pueden ser acciones sugeridas o respuestas sugeridas.
- Los bloques de texto largos y demasiados botones pueden frustrar a los usuarios, así que, siempre que sea posible, recomendamos inclinarse por la sencillez. 
- En algunos casos, puede ser más rentable enviar mensajes más largos sólo de texto a través de RCS que con SMS. Esto se debe a que los mensajes SMS más largos se dividen en varios segmentos, cada uno de los cuales es facturable, mientras que los mensajes RCS se facturan por mensaje. Ponte en contacto con tu director de cuentas Braze para obtener más detalles y orientación.
{% endtab %}

{% tab Media %}
Los mensajes multimedia RCS te permiten utilizar formatos multimedia atractivos que no son posibles con los SMS. Incluyen archivos de imagen, video y documentación. Estas opciones de medios existen para ayudarte a conseguir una interacción aún más profunda con tu audiencia y habilitar casos de uso totalmente nuevos. Por el momento, sólo es posible subir imágenes a través de la [biblioteca multimedia]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/). 

#### Características

- Los tipos de mensajes multimedia admiten todo lo disponible en los tipos de mensajes de texto, lo que incluye texto, respuestas sugeridas y acciones sugeridas.
- Admite archivos de imagen, incluidos los formatos JPEG y PNG. Los archivos de imagen están disponibles a través de la biblioteca multimedia. 
- Admite archivos de video, incluidos los formatos MP4, MPEG y MV4. Los archivos de video se pueden añadir por URL directamente en el creador de mensajes. 
- Admite archivos de documentación en formato PDF. Los archivos de documentación se pueden añadir a través de la URL directamente en el creador de mensajes. 

\![RCS compositor con una opción para subir un archivo multimedia.]({% image_buster /assets/img/rcs/rcs_media_type.png %})

#### Especificaciones del archivo

| Tipo de archivo | Especificaciones |
| --- | --- |
| Todos | \- El tamaño del archivo está limitado a 100 MB <br><br>\- La URL del archivo puede tener hasta 2048 caracteres |
| Archivos de imagen | Los formatos de archivo compatibles son JPG, JPEG y GIF
| Archivos de video | Los formatos de archivo compatibles son H263, M4V, MP4, MPEG-4, MPEG, WEBM |
| Archivos de documentación | Formatos de archivo compatibles: PDF |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Consideraciones

La experiencia del usuario al recibir mensajes RCS puede variar ligeramente en función de varios factores, como la cobertura del operador en el país de destino, el hardware del dispositivo móvil y el sistema operativo del dispositivo móvil. 

En general, RCS se integra de forma más natural con los dispositivos Android (este método fue implementado en gran medida por Google, y la mensajería RCS de igual a igual está ampliamente adoptada entre la comunidad Android). Diferentes dispositivos pueden ofrecer la experiencia a diferentes velocidades y calidades.  
{% endtab %}
{% endtabs %}

### Paso 3: Redacta tu mensaje RCS

Escribe tu mensaje utilizando los idiomas y la personalización[(Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/), [contenido conectado]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/) y emojis) que necesites. Asegúrate de respetar nuestros límites de copia de mensajes para reducir las posibilidades de que te cobren cargos por excedente.

{% alert important %}
Antes de continuar, lee nuestras [directrices sobre los límites de los mensajes RCS](#step-2-select-your-rcs-message-type). Los mensajes RCS se [cobran por mensaje]({{site.baseurl}}/sms_rcs_billing_calculators/), por lo que es una buena idea entender los matices de lo que se puede incluir en cada tipo de mensaje RCS.
{% endalert %}

### Paso 4: Vista previa y prueba de tu mensaje

Braze recomienda siempre previsualizar y probar tu mensaje antes de enviarlo. Ve a la pestaña de **Prueba** para enviar un RCS de prueba a grupos de prueba de contenido o a usuarios individuales, o ve una vista previa del mensaje como usuario directamente en Braze.

### Paso 5: Construye el resto de tu campaña o Canvas

A continuación, construye el resto de tu campaña o Canvas. Consulta las siguientes secciones para obtener más detalles sobre cómo utilizar mejor nuestras herramientas para crear mensajes RCS.

#### Paso 5.1: Elige el calendario o desencadenar la entrega

Los mensajes RCS pueden entregarse en función de una hora programada, una acción o un desencadenante de la API. Para más información, consulta [Programar tu campaña]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/).

Para la entrega basada en acciones, también puedes configurar la duración de la campaña y las horas tranquilas.

Especifica tus controles de entrega, como permitir que los usuarios vuelvan a ser elegibles para recibir la campaña o habilitar normas de limitación de frecuencia.

#### Paso 5.2: Elige los usuarios a los que dirigirte

Dirígete a los usuarios eligiendo segmentos o filtros para reducir tu audiencia. Ya deberías haber seleccionado el grupo de suscripción, que restringe a los usuarios según el nivel o categoría de comunicación que quieren tener contigo.

{% multi_lang_include target_audiences.md %}

A continuación, seleccionarás la audiencia más amplia de tus segmentos y reducirás aún más ese segmento con [filtros]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/) opcionales. Automáticamente recibirás una vista previa de cómo es la población aproximada de ese segmento en este momento. Ten en cuenta que la pertenencia exacta a un segmento siempre se calcula justo antes de enviar el mensaje.

{% alert tip %}
¿Te interesa utilizar la reorientación RCS para dirigirte a los usuarios en función de sus interacciones con SMS y RCS? Consulta [Reorientar]({{site.baseurl}}/sms_mms_rcs_user_retargeting/).
{% endalert %}

#### Paso 5.3: Elige eventos de conversión

Braze te permite hacer un seguimiento de la frecuencia con la que los usuarios realizan acciones específicas, o eventos de conversión, después de recibir una campaña. Puedes permitir una ventana de hasta 30 días durante la cual se contabilizará una conversión si el usuario realiza la acción especificada.

Los eventos de conversión te ayudan a medir el éxito de tu campaña. Por ejemplo:
- Si utilizas la geolocalización para desencadenar un mensaje RCS cuyo objetivo final es que el usuario realice una compra, establece el evento de conversión en **Compra**.
- Si intentas conducir al usuario a tu aplicación, establece el evento de conversión como **Inicio de sesión**.

También puedes establecer eventos de conversión personalizados basados en tu caso de uso específico. Sé creativo con la forma en que realmente quieres medir el éxito de tu campaña.

### Paso 6: Revisar y desplegar

Cuando hayas terminado de crear tu campaña o Canvas, revisa sus detalles, pruébala y ¡envíala!

A continuación, consulta [Informes para SMS, MMS y RCS]({{site.baseurl}}/sms_mms_rcs_reporting/) para saber cómo puedes acceder a los resultados de tus campañas RCS.

## Consejos

### Utilizar Liquid para la personalización de mensajes

Si piensas utilizar Liquid, asegúrate de incluir un valor predeterminado para la personalización elegida, de modo que, si el perfil de usuario del destinatario está incompleto, no reciba un marcador de posición en blanco `Hi, !` en lugar de su nombre o una frase coherente.

### Generar copia de IA

¿Necesitas ayuda para crear textos atractivos? Prueba a utilizar el [asistente de redacción AI]({{site.baseurl}}/user_guide/brazeai/generative_ai/copywriting/). Introduce el nombre o la descripción de un producto y la IA generará textos de marketing similares a los humanos para que los utilices en tus mensajes.

\![Creador de mensajes con un icono para abrir el asistente de redacción AI.]({% image_buster /assets/img/rcs/rcs_ai_copywriter.png %}){: style="max-width:70%;"}

## Preguntas más frecuentes

### ¿Puedo enviar mensajes de voz pregrabados con RCS?

Sí, puedes utilizar mensajes multimedia para admitir archivos de audio.
