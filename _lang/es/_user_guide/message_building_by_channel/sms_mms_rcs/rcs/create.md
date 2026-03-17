---
nav_title: Crear un mensaje RCS
article_title: Crear un mensaje RCS
page_order: 2
alias: /create_rcs_message/
description: "Este artículo explica cómo crear un mensaje RCS."
page_type: reference
channel:
  - RCS
---

# Crear un mensaje RCS

> Las campañas RCS son ideales para llegar directamente a tus clientes y comunicarte con ellos de forma programada. Puede utilizar Liquid y otros contenidos dinámicos para crear una experiencia personal con sus usuarios y crear un entorno que fomente y mejore una experiencia discreta del usuario con su marca.

## Creación de un mensaje RCS

### Paso 1: Elige dónde construir tu mensaje

¿No estás seguro de si tu mensaje debe enviarse mediante una campaña o un Canvas? Las campañas son más adecuadas para campañas de mensajería única y específica, mientras que los lienzos son más adecuados para recorridos de usuarios de varios pasos.

{% tabs %}
{% tab Campaign %}
1. Vaya a **Mensajería** > **Campañas** y seleccione **Crear campaña**.
2. Selecciona **SMS/MMS/RCS** o, para campañas dirigidas a varios canales, selecciona **Multicanal**.
3. Ponle a tu campaña un nombre claro y significativo.
4. Añade [equipos]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) y [etiquetas]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) según sea necesario.
   * Las etiquetas facilitan la búsqueda de sus campañas y la elaboración de informes a partir de ellas. Por ejemplo, al utilizar el [Generador de informes]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/), puede filtrar por etiquetas concretas.

{: start="5"}
5\. Añade y nombra tantas variantes como necesites para tu campaña. Puede elegir diferentes plataformas, tipos de mensaje y diseños para cada una de sus variantes añadidas. Para saber más sobre este tema, consulta [Multivariante y pruebas A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).
- **Pruebas de variantes SMS y RCS**: Braze te permite incluir variantes SMS y RCS en una misma campaña, lo que te permite comparar el rendimiento de cada una de ellas. Puedes añadir variantes SMS y RCS durante el primer paso de la composición del mensaje.

{: start="6"}
6\. Selecciona un [grupo de suscripción]({{site.baseurl}}/sms_rcs_subscription_groups/) habilitado para RCS. Al seleccionar un grupo de suscripción, Braze añadirá automáticamente un filtro de segmentación, garantizando que sólo los usuarios suscritos recibirán la campaña. Sólo los códigos largos y cortos que pertenezcan a ese grupo de suscripción se utilizarán para enviar SMS a los usuarios objetivo.
- **Recurso alternativo SMS**: Braze recomienda encarecidamente que todos los grupos de suscripción que contengan un remitente RCS incluyan también al menos un código SMS como alternativa. Esto es importante para la capacidad de entrega en los casos en que los mensajes RCS no se puedan entregar. Algunas de las razones pueden ser la incompatibilidad de los dispositivos de los usuarios y la cobertura incompleta de los operadores en un país o región determinados. Al habilitar la alternativa por SMS, tu mensaje se seguirá entregando al usuario y nunca perderás la oportunidad de conectarte con él.   

{: start="7"}
7\. Elige entre SMS y RCS. Antes de redactar mensajes RCS, elige el canal por el que los enviarás. Por lo general, recomendamos utilizar RCS siempre que sea posible, ya que ofrece importantes ventajas en cuanto a la interacción de los usuarios con respecto a los SMS; sin embargo, siempre ofrecemos la opción de enviar mensajes SMS para que tengas la máxima flexibilidad y control. 

![Opciones para seleccionar entre un tipo de mensaje RCS o SMS/MMS.]({% image_buster /assets/img/rcs/rcs_message_type.png %}){: style="max-width:65%;"}

{% alert tip %}
Si todos los mensajes de su campaña van a ser similares o van a tener el mismo contenido, redacte su mensaje antes de añadir variantes adicionales. A continuación, puede seleccionar **Copiar de variante** en el desplegable **Añadir variante**.
{% endalert %}

{% endtab %}
{% tab Canvas %}
1. [Cree su lienzo]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) utilizando el compositor de lienzos.
2. Una vez que hayas configurado tu Canvas, añade un paso de mensaje **SMS/MMS/RCS** en el generador de lienzos. 
3. Nombra tu paso con algo claro y significativo.
4. Selecciona un [grupo de suscripción]({{site.baseurl}}/sms_rcs_subscription_groups/) habilitado para RCS. Al seleccionar un grupo de suscripción, Braze añadirá automáticamente un filtro de segmentación, garantizando que sólo los usuarios suscritos recibirán la campaña. Solo se utilizarán los códigos largos y abreviados que pertenezcan a ese grupo de suscripción para dirigirse a los usuarios.
- **Recurso alternativo SMS**: Braze recomienda encarecidamente que todos los grupos de suscripción que contengan un remitente RCS incluyan también al menos un código SMS como alternativa. Esto es importante para la capacidad de entrega en los casos en que los mensajes RCS no se puedan entregar. Algunas de las razones pueden ser la incompatibilidad de los dispositivos de los usuarios y la cobertura incompleta de los operadores en un país o región determinados. Al habilitar la alternativa por SMS, tu mensaje se seguirá entregando al usuario y nunca perderás la oportunidad de conectarte con él.

{: start="5"}
5\. Elige entre SMS y RCS. Antes de redactar mensajes RCS, elige el canal por el que los enviarás. Por lo general, recomendamos utilizar RCS siempre que sea posible, ya que ofrece importantes ventajas en cuanto a la interacción de los usuarios con respecto a los SMS; sin embargo, siempre ofrecemos la opción de enviar mensajes SMS para que tengas la máxima flexibilidad y control. 

![Opciones para seleccionar entre un tipo de mensaje RCS o SMS/MMS.]({% image_buster /assets/img/rcs/rcs_message_type.png %}){: style="max-width:65%;"}

{% endtab %}
{% endtabs %}

### Paso 2: Selecciona tu tipo de mensaje RCS

Para el tipo de mensaje RCS, elige entre **Texto** o **Multimedia**.

![Opciones para seleccionar entre un tipo de mensaje de texto o multimedia.]({% image_buster /assets/img/rcs/rcs_text_media.png %}){: style="max-width:65%;"}

{% tabs %}
{% tab Text %}
Como su nombre indica, los mensajes de texto RCS se centran en el texto como medio. Si escribes hasta 160 caracteres, el mensaje RCS se factura como un mensaje de solo texto (o «básico»). Si superas los 160 caracteres o utilizas un elemento enriquecido, el mensaje se factura como un mensaje RCS enriquecido (o «único») (y el límite de caracteres aumenta a 3072 caracteres). 

#### Características

- Los tipos de mensajes de texto incluyen todas las características de SMS. Solo el seguimiento avanzado permite realizar un seguimiento de los clics en URL para ofrecerte informes detallados a nivel de usuario. 
- Además, ahora tienes la opción de incluir atractivos botones **de respuestas sugeridas** y botones **de acción sugeridas** que impulsan interacciones de alto nivel por parte de los usuarios, como visitar una página de destino o realizar un pedido. 
    - **Las respuestas sugeridas** son botones que contienen respuestas sugeridas para que los usuarios hagan clic y las rellenen previamente en su entrada de texto, lo que elimina la fricción de tener que pensar en una respuesta al proporcionarles un conjunto limitado de opciones. 
    - **Las acciones sugeridas** son botones que inician una acción en el dispositivo del usuario. Por lo general, constan de una o dos palabras descriptivas y un icono visual para ayudar al usuario a comprender la función del botón. Braze actualmente admite las acciones sugeridas de OpenURL. Funciona de manera similar a una URL, donde los usuarios que seleccionan el botón son redirigidos a una página web u otra ubicación con identificador de URL. 

![Un GIF con tres acciones sugeridas para un mensaje RCS que promociona estilos de moda en tendencia: «La realeza de los cuentos de hadas», «El mundo académico vanguardista» y «Muéstrame tus otros estilos».]({% image_buster /assets/img/rcs/rcs_suggested_actions.gif %}){: style="max-width:70%;"}

#### Consideraciones

- En cuanto al límite de caracteres del texto, puedes escribir hasta 160 caracteres en un mensaje RCS solo de texto (básico) o hasta 3072 en un mensaje RCS enriquecido (único). 
- En cuanto al límite de botones, puedes añadir hasta cinco botones por mensaje. Estos botones pueden ser acciones sugeridas o respuestas sugeridas.
- Los bloques de texto largos y el exceso de botones pueden frustrar a los usuarios, por lo que, siempre que sea posible, recomendamos apostar por la simplicidad. 
- En algunos casos, puede resultar más rentable enviar mensajes de texto más largos a través de RCS que mediante SMS. Esto se debe a que los mensajes SMS más largos se dividen en varios segmentos, cada uno de los cuales es facturable, mientras que los mensajes RCS se facturan por mensaje. Ponte en contacto con tu director de cuentas de Braze para obtener más detalles y orientación.
{% endtab %}

{% tab Media %}
Los mensajes multimedia RCS te permiten utilizar formatos multimedia que promueven la interacción que no son posibles con los SMS. Entre ellos se incluyen archivos de imagen, video y documentos. Estas opciones multimedia existen para ayudarte a aumentar aún más la interacción con tu audiencia y habilitar casos de uso completamente nuevos. Por el momento, solo se admite la carga de imágenes a través de la [biblioteca multimedia]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/). 

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

#### Características

- Los tipos de mensajes multimedia admiten todo lo que está disponible en los tipos de mensajes de texto, lo que incluye texto, respuestas sugeridas y acciones sugeridas.
- Admite archivos de imagen, incluidos los formatos JPEG y PNG. Los archivos de imagen están disponibles mediante su carga desde la biblioteca multimedia. 
- Admite archivos de video, incluidos los formatos MP4, MPEG y MV4. Los archivos de video se pueden añadir mediante URL directamente en el creador de mensajes. 
- Admite archivos de documentos en formato PDF. Los archivos de documentos se pueden añadir a través de la URL directamente en el creador de mensajes. 

![Compositor RCS con opción para cargar un archivo multimedia.]({% image_buster /assets/img/rcs/rcs_media_type.png %})

#### Especificaciones del archivo

| Tipo de archivo | Especificaciones |
| --- | --- |
| Todo | \- El tamaño del archivo está limitado a 100 MB. <br><br>\- La URL del archivo puede tener hasta 2048 caracteres. |
| Archivos de imagen | Los formatos de archivo compatibles incluyen JPG, JPEG y GIF.
| Archivos de video | Los formatos de archivo compatibles incluyen H263, M4V, MP4, MPEG-4, MPEG y WEBM. |
| Archivos de documentos | Formatos de archivo compatibles: PDF |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Consideraciones

La experiencia del usuario al recibir mensajes RCS puede variar ligeramente en función de una serie de factores, entre los que se incluyen la cobertura del operador en el país de destino, el hardware del dispositivo móvil y el sistema operativo del dispositivo móvil. 

En términos generales, RCS tiene una integración más natural con los dispositivos Android (este método fue implementado en gran medida por Google, y la mensajería RCS entre pares está ampliamente adoptada entre la comunidad Android). Los distintos dispositivos pueden ofrecer una experiencia con diferentes velocidades y calidades.  
{% endtab %}
{% endtabs %}

### Paso 3: Redacta tu mensaje RCS.

Escribe tu mensaje utilizando lenguajes y personalización ([Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/), [contenido conectado]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/) y emojis) según sea necesario. Asegúrate de respetar nuestros límites de copia de mensajes para reducir las posibilidades de que te cobren más de la cuenta.

{% alert important %}
Antes de continuar, lee nuestras [directrices sobre los límites de los mensajes RCS](#step-2-select-your-rcs-message-type). Los mensajes RCS se [cobran por mensaje]({{site.baseurl}}/sms_rcs_billing_calculators/), por lo que es recomendable comprender los matices de lo que se puede incluir en cada tipo de mensaje RCS.
{% endalert %}

### Paso 4: Vista previa y prueba de tu mensaje

Dado que la representación RCS está controlada por el sistema operativo del usuario, el fabricante del dispositivo, el operador y la aplicación de mensajería (por ejemplo, Google Messages frente a Mensajes de Apple), la apariencia de los mensajes puede variar. Como resultado, es posible que la vista previa de RCS que se muestra en Braze no coincida exactamente con lo que recibe finalmente el usuario final. Las diferencias pueden incluir el diseño, el tamaño de los medios, los botones, los elementos de marca o las características compatibles. Braze recomienda siempre previsualizar y probar el mensaje antes de enviarlo. Utiliza la pestaña **Prueba** para enviar un RCS de prueba a grupos de prueba de contenido o a usuarios individuales, y realiza la vista previa del mensaje como usuario directamente en Braze. Sin embargo, siempre que sea posible, la representación final debe validarse en dispositivos reales, ya que Braze no puede garantizar una paridad perfecta en todas las combinaciones de sistemas operativos, dispositivos y operadores.


### Paso 5: Construye el resto de tu campaña o Canvas

A continuación, crea el resto de tu campaña o Canvas. Consulta las siguientes secciones para obtener más información sobre cómo utilizar mejor nuestras herramientas para crear mensajes RCS.

#### Paso 5.1: Elige la programación o desencadenante de la entrega

Los mensajes RCS pueden entregarse según una hora programada, una acción o un activador API. Para más información, consulta [Programar tu campaña]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/).

Para la entrega basada en acciones, también puedes establecer la duración de la campaña y las horas tranquilas.

Especifica tus controles de entrega, como permitir que los usuarios vuelvan a ser elegibles para recibir la campaña o habilitar reglas de limitación de frecuencia.

#### Paso 5.2: Elige los usuarios a los que dirigirte

Dirígete a los usuarios seleccionando segmentos o filtros para delimitar tu audiencia. Ya deberías haber seleccionado el grupo de suscripción, que limita los usuarios según el nivel o la categoría de comunicación que desean tener contigo.

{% multi_lang_include target_audiences.md %}

A continuación, seleccionas la audiencia más amplia de tus segmentos y la reduces aún más con [filtros]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/) opcionales. Automáticamente recibirás una vista previa de cómo es aproximadamente la población de ese segmento. Ten en cuenta que la pertenencia exacta al segmento siempre se calcula antes de enviar el mensaje.

{% alert tip %}
¿Te interesa utilizar el reorientamiento RCS para dirigirte a los usuarios en función de sus interacciones SMS y RCS? Consulta [«Reorientación]({{site.baseurl}}/sms_mms_rcs_user_retargeting/)».
{% endalert %}

#### Paso 5.3: Elegir eventos de conversión

Braze te permite realizar un seguimiento de la frecuencia con la que los usuarios realizan acciones específicas, o eventos de conversión, después de recibir una campaña. Puede permitir una ventana de hasta 30 días durante la cual se contabilizará una conversión si el usuario realiza la acción especificada.

Los eventos de conversión le ayudan a medir el éxito de su campaña. Por ejemplo:
- Si utilizas la segmentación geográfica para desencadenar un mensaje RCS cuyo objetivo final es que el usuario realice una compra, configura el evento de conversión como **«Compra**».
- Si estás intentando dirigir al usuario a tu aplicación, configura el evento de conversión en **Iniciar sesión**.

También puede establecer eventos de conversión personalizados basados en su caso de uso específico. Sé creativo a la hora de decidir cómo quieres medir realmente el éxito de tu campaña.

### Paso 6: Revisar y desplegar

Una vez que hayas terminado de crear tu campaña o Canvas, revisa los detalles, pruébalo y envíalo.

A continuación, consulta [Informes para SMS, MMS y RCS]({{site.baseurl}}/sms_mms_rcs_reporting/) para saber cómo puedes acceder a los resultados de tus campañas RCS.

## Consejos

### Uso de Liquid para la personalización de mensajes

Si tienes pensado utilizar Liquid, asegúrate de incluir un valor predeterminado para la personalización elegida, de modo que, si el perfil de usuario del destinatario está incompleto, no reciba un marcador de posición en`Hi, !` blanco  en lugar de su nombre o una frase coherente.

### Generar copia de IA

¿Necesitas ayuda para crear un texto que genere interacción? Prueba a utilizar el [asistente de redacción de IA]({{site.baseurl}}/user_guide/brazeai/generative_ai/copywriting/). Introduce el nombre o la descripción de un producto y la IA generará un texto de marketing similar al humano para que lo utilices en tu mensajería.

![Creador de mensajes con un icono para abrir el asistente de redacción de textos publicitarios con IA.]({% image_buster /assets/img/rcs/rcs_ai_copywriter.png %}){: style="max-width:70%;"}

## Preguntas más frecuentes

### ¿Puedes enviar mensajes de voz pregrabados con RCS?

Sí, puedes utilizar mensajes multimedia para admitir archivos de audio.
