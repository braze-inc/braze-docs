---
nav_title: "Canales de notificación"
article_title: Canales de notificación push 
page_order: 4
page_type: reference
description: "Este artículo de referencia trata temas relacionados con el canal de notificaciones push de Android, como la transición a Android O, cómo añadir un canal a Braze, cómo configurar un canal alternativo y mucho más."
platform: Android
channel:
  - push

---

# Canales de notificación

> [Los canales de notificación](https://www.braze.com/blog/android-o-push-notifications-channels/) son una forma de organizar las notificaciones push que se añadieron con Android O. A partir de O, todas las notificaciones push deben tener un canal de notificación que indique el tipo de mensaje (por ejemplo, "notificaciones de chat" o "notificaciones de seguimiento"). De este modo, tus usuarios pueden controlar aspectos de su notificación (por ejemplo, la repetición, la configuración de ruido/vibración o la exclusión voluntaria, etc.) basándose en canales individuales.

## Transición a Android O

Los canales de notificación sólo pueden crearse en el código de tu aplicación y no pueden crearse mediante programación en el panel de Braze. Recomendamos que tu equipo de ingeniería trabaje con tus especialistas en marketing para asegurarse de que los canales de notificación deseados se añaden correctamente al panel.

A partir de Android O, las notificaciones push requieren un canal válido para mostrarse. Si tu aplicación está destinada a Android O o posterior, debes utilizar la versión 2.1.0 o posterior del SDK de Braze. Tu equipo de desarrolladores debe definir los canales que quieres utilizar, así como las configuraciones de notificación sugeridas (por ejemplo, importancia, sonido, luces) para cada canal en el código de tu aplicación. Puedes encontrar la documentación para desarrolladores de Android [aquí](https://developer.android.com/preview/features/notification-channels.html) y la documentación para desarrolladores de Braze [aquí.]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/#step-5-define-notification-channels)

{% alert note %}
Android admite la localización de los nombres de los canales, por lo que en el código de tu aplicación puedes asociar un ID de canal a varias traducciones del nombre de un canal.
{% endalert %}

Una vez creados estos canales, tus ingenieros tendrán que pasar los ID de canal asociados a tu equipo de marketing. Tu equipo debe introducir los nombres de los canales y los ID de los canales en el panel de Braze para utilizarlos en tus campañas y Canvases.

Para añadir un canal al panel de Braze, navega hasta el compositor push de Android, selecciona el campo de canales de notificación y, a continuación, selecciona "administrar canales".
{% alert important %}
Sólo los usuarios con permisos que incluyan "administrar aplicaciones" podrán administrar canales.
{% endalert %}

## Canal predeterminado SDK

Android requiere un canal válido para mostrar notificaciones push en el nivel de API 26 (Android O) o posterior. Braze Android SDK 2.1.0 incluye un canal predeterminado llamado "General", que se creará y utilizará si no especificas canales adicionales en el panel o si intentas enviar a un canal no válido. Puedes cambiar el nombre de esta etiqueta en el SDK y proporcionar una descripción del canal. Te recomendamos que lo tengas en cuenta para ofrecer una mejor experiencia al usuario.  

Una vez añadido un canal a tu solicitud, puedes optar por eliminarlo. Sin embargo, los consumidores siempre podrán ver el número de canales que has [eliminado].[3] El panel de Braze no incluye soporte para crear canales mediante programación: los canales deben crearse y definirse en el código de tu aplicación para proporcionar una experiencia sin problemas.

Una vez más, te recomendamos que te coordines con tu equipo de ingeniería para garantizar una transición sin problemas hacia Android O.

## Canal alternativo del panel de control

Braze te permite especificar un canal alternativo para el panel. El objetivo del canal alternativo del panel es proporcionar un ID de canal para los mensajes push heredados sin selección explícita de canal. Definimos la selección de un canal como la elección de un canal en nuestro compositor push de Android.

Los mensajes que no tengan un canal seleccionado se enviarán con el ID de canal alternativo del panel. Cuando cambies el canal alternativo de tu panel, cualquier mensaje que no tenga un canal seleccionado explícitamente se enviará con el ID del nuevo canal alternativo.

Aquí tienes un ejemplo del comportamiento esperado del canal de alternativa del panel:

El canal alternativo de tu panel se llama "Marketing" y tienes 10 mensajes push de Android para los que nunca has seleccionado un canal. Estas campañas se envían a través del canal "Marketing" porque el canal "Marketing" es el canal alternativo del panel.

Además, tienes 15 mensajes que has seleccionado para enviar a través del canal "Notificaciones sociales" y cinco mensajes que has seleccionado para enviar a través del canal "Marketing".

Entonces decides cambiar el canal predeterminado de tu panel de "Marketing" a "Actualizaciones".

En esta situación, las 10 campañas sin selección de canal que antes se enviaban a través del canal "Marketing" ahora se enviarán a través del canal "Actualizaciones" porque estos mensajes se envían a través del canal de alternativa. Los 15 mensajes que se enviaban a través del canal "Notificaciones sociales" seguirán enviándose a través del canal "Notificaciones sociales". Los cinco mensajes que se enviaban a través del canal "Marketing" se seguirán enviando a través del canal "Marketing".

En caso de que se proporcione a Braze un ID de canal no válido (por ejemplo, si proporcionas un ID de canal que tus desarrolladores no crearon en el SDK), entregaremos la notificación a través del canal predeterminado de tu SDK. Por lo tanto, te recomendamos encarecidamente que pruebes tus canales de notificación a través del panel de Braze durante el desarrollo.

Para comprender mejor el comportamiento esperado de los canales, consulta la tabla siguiente:

|Escenario |Resultado  |    
| ---|-------------
|**La empresa ABC** actualiza un SDK compatible con Android O<br>**La empresa ABC** no añade ningún canal al panel de Braze<br>**La empresa ABC** no cambia el nombre de su canal predeterminado SDK | Las notificaciones push enviadas a dispositivos Android O crearán un canal llamado "General" y las notificaciones se enviarán a través del canal "General".
|**La empresa XYZ** actualiza a un SDK compatible con Android O <br>**La empresa XYZ** no añade ningún canal al panel de Braze<br>**La empresa XYZ** cambia el nombre de su canal predeterminado SDK a "Marketing". | Las notificaciones push enviadas a dispositivos Android O crearán un canal llamado "Marketing" y las notificaciones se enviarán a través del canal "Marketing".
|**La empresa LMN** se actualiza a un SDK compatible con Android O <br>**La empresa LMN** define dos canales en su código de aplicación, "Promociones" y "Actualización de pedidos" <br>**La empresa LMN** añade los ID de canal para "Promociones" y "Actualización de pedidos" al panel de Braze <br>**La empresa LMN** designa "Promociones" como canal alternativo del panel de control<br>**La empresa LMN** cambia el nombre de su canal predeterminado SDK a "Marketing". | Las notificaciones push enviadas a dispositivos Android O no crearán un canal<br><br>A menos que el especialista en marketing especifique explícitamente que las notificaciones deben enviarse a través del canal "Actualizaciones de pedidos" o "Marketing", todas las notificaciones creadas antes de añadir los canales al panel se enviarán a través del canal "Promociones".<br><br>El canal predeterminado del SDK, "Marketing", sólo se crea y utiliza si la empresa intenta enviar una notificación a través de un ID de canal no válido o si se ha seleccionado explícitamente.
|**La empresa HIJ** actualiza a Android O pero no actualiza el SDK para Android de Braze a 2.1.0 o posterior | Las notificaciones enviadas a usuarios que ejecutan Android O o posterior no aparecen |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Añadir canales al panel de Braze

1. Abre cualquier campaña o Canvas que incluya un push de Android y haz clic en **Editar campaña**.
2. Navega hasta el creador de mensajes push de Android.
3. Haz clic en **Gestionar canales de notificación**. Todos los canales añadidos aquí estarán disponibles globalmente para todas las campañas y Lienzos. Debes tener [permisos]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#limited-and-team-role-permissions) de "Administrar aplicaciones" en tu espacio de trabajo para administrar canales.

Cuando apliques un canal de notificación a una campaña específica o a un paso en Canvas, tu recuento de **Usuarios alcanzables** (situado en el paso Audiencia objetivo) para Android Push no parecerá cambiar. Sin embargo, sólo los usuarios suscritos al canal de notificación seleccionado verán el mensaje, y los análisis de tu campaña (como los clics) se medirán en función de esta audiencia.

\![]({% image_buster /assets/img_archive/Click_Here.png %})

{:start="4"}
4\. Haz clic en **Añadir canal de notificación**.
5\. Introduce el nombre y el ID del canal de notificación que quieras añadir.<br><br>\![]({% image_buster /assets/img_archive/Enter_Channel.png %})<br><br>
6\. Repite los pasos 4 y 5 para cada canal de notificación que quieras añadir.
7\. Pulsa **Guardar** para guardar los cambios.

## Especificar tu canal alternativo

Tu canal alternativo es el canal con el que Braze intentará enviar tu mensaje de Android si no has seleccionado un canal para el mensaje. Las únicas campañas y Lienzos que tendrán mensajes de Android sin selección de canal son las campañas y Lienzos que se crearon antes de que tu equipo añadiera canales al panel de Braze. Si cambias tu canal alternativo, el cambio se aplicará globalmente a todas las campañas y Lienzos sin una selección explícita de canal.

1. Abre cualquier campaña o Canvas existente.
2. Navega hasta el compositor push de Android.
3. Selecciona **Gestionar canales de notificación** tras ampliar las opciones del canal de notificación. <br><br>\![]({% image_buster /assets/img_archive/Change_Fallback.png %}){: style="max-width:80%;"}<br><br>
4. Añade el canal al panel (si aún no se ha añadido).
5. Selecciona el radio junto al canal que quieras designar como canal alternativo.
6. Guarda los cambios. Tus cambios se aplicarán globalmente.

## Añadir canales a tus mensajes push de Android

1. Navega hasta el compositor push de Android en cualquier campaña o Canvas.
2. Selecciona en el desplegable el canal que quieres utilizar. Si no tienes un desplegable, sino la vista siguiente, tendrás que añadir canales antes de seleccionarlos para las campañas.

\![]({% image_buster /assets/img_archive/No_Select.png %})

[3]: https://developer.android.com/preview/features/notification-channels.html#DeletingChannels
