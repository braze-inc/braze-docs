---
nav_title: Guía de preparación
article_title: Guía de preparación de mensajes en la aplicación
page_order: 0.5

page_type: reference
description: "Este artículo aborda algunas cuestiones y buenas prácticas que deberías tener en cuenta antes de crear tus mensajes in-app."
channel: in-app messages

---

# Guía de preparación de mensajes en la aplicación

> Antes de crear tus mensajes in-app, deberías tener en cuenta algunos de los siguientes temas para que crear tu mensaje sea rápido y fácil.

## Consideraciones generales

- Si está creando una campaña, ¿cuántas variantes de este mensaje desea mostrar? Para ideas sobre pruebas de variantes, consulta [Consejos para diferentes canales]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign/#tips-different-channels).
- Si está construyendo un Canvas, ¿se emparejará este mensaje con otros canales de mensajería en ese paso?
- ¿Cuándo quieres [que caduque tu mensaje]({{site.baseurl}}/canvas_in-app_messages/)?

## Criterios de segmentación

- Los mensajes in-app son mejores para los usuarios que visitan regularmente tu aplicación. ¿Incluyes a esta audiencia?
- ¿Dónde quieres que tus usuarios vean tu mensaje? ¿En su aplicación web? ¿En tu aplicación móvil?
- ¿Qué acontecimiento debería desencadenar este mensaje?
- ¿Alguno de tus usuarios utiliza versiones anteriores de tu aplicación? Si es así, es posible que no puedan ver algunos elementos de su mensaje.
- ¿Para qué tipo de dispositivo o dispositivos está creando este mensaje? Recuerda que puedes previsualizar tu mensaje utilizando el cuadro **Previsualizar** o la pestaña **Probar**. Consulte la sección [Pruebas]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/testing/) para obtener más información.

## Consideraciones sobre el contenido

- ¿Qué idiomas utilizarás en este mensaje?
- ¿Cuál es tu encabezado y tu cuerpo de texto? ¿Son llamativos y relevantes para el usuario?
- Los mensajes in-app sólo aparecen durante un tiempo determinado. ¿Su texto es conciso y fácil de recordar?
- ¿Utilizará [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/) para añadir copias personalizadas?
- En el caso de los mensajes in-app a pantalla completa, ¿la imagen u otro medio se encuentra dentro de la [zona segura]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/fullscreen/#image-safe-zone)?
- Para los mensajes de encuesta dentro de la aplicación, ¿desea registrar atributos o envíos? ¿Ha configurado su página de confirmación?

## Consideraciones sobre la conversión

- ¿Cuál es el objetivo de este mensaje? ¿Cómo puedes representarlo en tu mensaje?
- ¿Ofrecen sus botones opciones que tengan sentido para el usuario? ¿Cuál es tu [principal llamada a la acción]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/#buttons)?
- [¿Tienes vínculos en profundidad con otros contenidos de la aplicación][1]? ¿Estás utilizando este mensaje dentro de la aplicación para enviar y aceptar una [solicitud de permiso o de preparación push][21]?
- ¿Tiene una opción de salida de mensajes? Si no, siempre puedes copiar y pegar este fragmento para crear un botón rápido:
    ```html
    <a href="appboy://close">X</a>
    ```


[1]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#deep-linking-to-in-app-content
[21]: {{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/
