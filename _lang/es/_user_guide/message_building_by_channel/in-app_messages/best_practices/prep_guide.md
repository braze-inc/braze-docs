---
nav_title: Guía de preparación
article_title: Guía de preparación de mensajes dentro de la aplicación
page_order: 0.5

page_type: reference
description: "Este artículo aborda algunas cuestiones y buenas prácticas que deberías tener en cuenta antes de crear tus mensajes dentro de la aplicación."
channel: in-app messages

---

# Guía de preparación de mensajes dentro de la aplicación

> Antes de crear tus mensajes dentro de la aplicación, debes tener en cuenta algunos de los siguientes temas para que la creación de tu mensaje sea rápida y sencilla.

## Consideraciones generales

- Si estás creando una campaña, ¿cuántas variantes de este mensaje te gustaría mostrar? Para ideas sobre pruebas de variantes, consulta [Consejos para diferentes canales]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign/#tips-different-channels).
- Si estás construyendo un Canvas, ¿se emparejará este mensaje con otros canales de mensajería en ese paso?
- ¿Cuándo quieres [que caduque tu mensaje]({{site.baseurl}}/canvas_in-app_messages/)?

## Consideraciones sobre la orientación

- Los mensajes dentro de la aplicación son mejores para los usuarios que visitan regularmente tu aplicación. ¿Incluyes a esta audiencia?
- ¿Dónde quieres que tus usuarios vean tu mensaje? ¿En tu aplicación Web? ¿En tu aplicación móvil?
- ¿Qué acontecimiento debería desencadenar este mensaje?
- ¿Alguno de tus usuarios utiliza versiones antiguas de tu aplicación? Si es así, es posible que no puedan ver algunos elementos de tu mensaje.
- ¿Para qué tipo de dispositivo o dispositivos estás creando este mensaje? Recuerda que puedes obtener una vista previa de tu mensaje utilizando el cuadro **Vista previa** o la pestaña **Prueba**. Consulta la sección [Pruebas]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/testing/) para obtener más información.

## Consideraciones sobre el contenido

- ¿Qué lenguas utilizarás en este mensaje?
- ¿Cuál es tu encabezado y tu cuerpo de texto? ¿Son llamativos y relevantes para tu usuario?
- Los mensajes dentro de la aplicación sólo aparecen durante un tiempo determinado. ¿Es tu texto conciso y memorable?
- ¿Vas a utilizar [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/) para añadir copias personalizadas?
- Para los mensajes dentro de la aplicación a pantalla completa, ¿está tu imagen u otro medio dentro de la [zona segura]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/fullscreen/#image-safe-zone)?
- Para los mensajes dentro de la aplicación del cuestionario, ¿quieres registrar atributos o envíos? ¿Has configurado tu página de confirmación?

## Consideraciones sobre la conversión

- ¿Cuál es el objetivo de este mensaje? ¿Cómo puedes representarlo en tu mensaje?
- ¿Tus botones ofrecen opciones que tengan sentido para tu usuario? ¿Cuál es tu [principal llamada a la acción]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/#buttons)?
- [¿Tienes vínculos en profundidad con otros contenidos de la aplicación]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#deep-linking-to-in-app-content)? ¿Estás utilizando este mensaje dentro de la aplicación para enviar y aceptar una [solicitud de permiso o de push priming]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/)?
- ¿Tienes una opción de salida de mensajes? Si no, siempre puedes copiar y pegar este fragmento de código para crear un botón rápido:
    ```html
    <a href="appboy://close">X</a>
    ```


