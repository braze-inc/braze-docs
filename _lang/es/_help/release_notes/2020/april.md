---
nav_title: Abril
page_order: 9
noindex: true
page_type: update
description: "Este artículo contiene notas de la versión de abril de 2020."
---
# Abril de 2020

## Asociación con Movable Ink

Movable Ink ofrece a los clientes de Braze la posibilidad de utilizar características de Intelligent Creative como temporizadores de cuenta atrás, encuestas y rasca y gana en sus campañas push, de mensajes dentro de la aplicación y de tarjetas de contenido. Movable Ink y Braze potencian un enfoque más completo de los mensajes dinámicos basados en datos, proporcionando a los usuarios elementos en tiempo real sobre las cosas que importan.

¡Empieza a [integrar Movable Ink]({{site.baseurl}}/partners/message_personalization/dynamic_content/visual_and_interactive_content/movable_ink/) en tus campañas!

## Intelligent Timing

Al programar una campaña, puedes utilizar [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/) (antes Entrega inteligente) para entregar tu mensaje a cada usuario en el momento en que Braze determine que es más probable que una persona interactúe.

Las actualizaciones de esta característica incluyen:
- **Aclaración de las horas tranquilas**: La funcionalidad de Horas tranquilas sigue siendo la misma, pero se ha ajustado la interfaz de usuario para clarificarla.
- **Adición de la vista previa del gráfico**: Ahora puedes generar un gráfico para ver cuántos usuarios recibirán mensajes por cada hora del día con Intelligent Timing, así como qué proporción de usuarios tienen datos suficientes para calcular una hora óptima.
- **Adición de la alternativa personalizada**: Ahora puedes elegir la hora local a la que enviar a los usuarios un mensaje cuando carezcan de datos de interacción suficientes para calcular una hora óptima

## Exportación de audiencias de Facebook

Braze ofrece la posibilidad de exportar manualmente tus usuarios desde la página Segmentos de Braze para crear audiencias personalizadas de Facebook. Se trata de una exportación de audiencia única y estática, y sólo creará nuevas [audiencias personalizadas de Facebook]({{site.baseurl}}/partners/facebook/).

Actualmente disponible para todos los clusters, existe un nuevo proceso de exportación de Facebook Audience de Braze, que agiliza el proceso con sencillos pasos de integración. Ya no tendrás que poner en la lista blanca los URI de redirección de OAuth para enviar audiencias personalizadas ni complicarte con la configuración de la aplicación de Facebook para la integración.

{% alert important %}
Ten en cuenta que todos los clientes que actualmente utilizan Facebook Audiences personalizados, deben reintegrar sus Braze Segments con estos nuevos pasos.
{% endalert%}


## Actualizaciones de la API del bloque de contenido y de la plantilla de correo electrónico

Los puntos finales de las API [template/email/list]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates/) y [content_block/list]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks/) se han actualizado para incluir un nuevo campo `tags`. Este campo mostrará, como una matriz, cualquier etiqueta que se aplique al bloque o plantilla de correo electrónico actual.

## Personalización de la dirección del remitente

Al crear un mensaje de correo electrónico en Braze, ahora puedes personalizar la Dirección del remitente del mensaje en la sección **Información de envío** de la composición del correo electrónico. Puedes utilizar cualquiera de nuestras [etiquetas de personalización]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/) compatibles

![Personalización de la dirección]({% image_buster /assets/img/personalized-from-name.png %}){: style="max-width:80%"}

