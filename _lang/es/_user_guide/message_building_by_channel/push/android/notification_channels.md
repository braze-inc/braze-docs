---
nav_title: "Canales de notificación"
article_title: Canales de notificación push 
page_order: 4
page_type: reference
description: "En este artículo de referencia se tratan temas relacionados con los canales de notificaciones push de Android, como la transición a Android O, cómo añadir un canal a Braze, cómo establecer un canal de reserva y mucho más."
platform: Android
channel:
  - push

---

# Canales de notificación

> [Los canales](https://www.braze.com/blog/android-o-push-notifications-channels/) de notificación son una forma de organizar las notificaciones push que se añadieron con Android O. A partir de O, todas las notificaciones push deben tener un canal de notificación que indique el tipo de mensaje (por ejemplo, "notificaciones de chat" o "notificaciones de seguimiento"). Los usuarios pueden controlar los aspectos de sus notificaciones (por ejemplo, la repetición, los ajustes de ruido/vibración, la exclusión voluntaria, etc.) en función de los canales individuales.

## Transición a Android O

Los canales de notificación sólo pueden crearse en el código de su aplicación y no pueden crearse mediante programación en el cuadro de mandos de Braze. Recomendamos a su equipo de ingenieros que trabaje con los responsables de marketing para garantizar que los canales de notificación deseados se añaden correctamente al panel de control.

A partir de Android O, las notificaciones push requieren un canal válido para mostrarse. Si tu aplicación está destinada a Android O o posterior, debes utilizar la versión 2.1.0 o posterior del SDK de Braze. Su equipo de desarrollo debe definir los canales que desea utilizar, así como los ajustes de notificación sugeridos (por ejemplo, importancia, sonido, luces) para cada canal en el código de su aplicación. Puedes encontrar la documentación para desarrolladores de Android [aquí](https://developer.android.com/preview/features/notification-channels.html) y la documentación para desarrolladores de Braze [aquí.]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/#step-5-define-notification-channels)

{% alert note %}
Android admite la localización de nombres de canal, por lo que en el código de su aplicación, puede asociar un ID de canal con múltiples traducciones de un nombre de canal.
{% endalert %}

Una vez creados estos canales, sus ingenieros tendrán que pasar los ID de canal asociados a su equipo de marketing. Su equipo debe introducir los nombres y los ID de los canales en el panel Braze para utilizarlos en sus campañas y Canvases.

Para añadir un canal al cuadro de mandos de Braze, navegue hasta el compositor push de Android, seleccione el campo de canales de notificación y, a continuación, seleccione "gestionar canales".
{% alert important %}
Sólo los usuarios con permisos que incluyan "gestionar aplicaciones" podrán gestionar canales.
{% endalert %}

## Canal por defecto del SDK

Android requiere un canal válido para mostrar notificaciones push en el nivel de API 26 (Android O) o posterior. Braze Android SDK 2.1.0 incluye un canal predeterminado denominado "General", que se creará y utilizará si no se especifican canales adicionales en el panel o si se intenta enviar a un canal no válido. Puede cambiar el nombre de esta etiqueta en el SDK y proporcionar una descripción del canal. Le recomendamos que lo tenga en cuenta para ofrecer una mejor experiencia al usuario.  

Una vez añadido un canal a su aplicación, puede optar por eliminarlo. Sin embargo, los consumidores siempre podrán ver el número de canales que has [eliminado].[3] El panel de control de Braze no incluye soporte para la creación programática de canales - los canales deben ser creados y definidos en el código de tu aplicación para proporcionar una experiencia fluida.

Una vez más, te recomendamos que te coordines con tu equipo de ingeniería para garantizar una transición fluida a la orientación a Android O.

## Canal de reserva del cuadro de mandos

Braze te permite especificar un canal alternativo para el panel. El propósito del canal de reserva del salpicadero es proporcionar un ID de canal para los mensajes push heredados sin selección explícita de canal. Definimos una selección de canal como la elección de un canal en nuestro compositor push de Android.

Los mensajes que no tengan un canal seleccionado se enviarán con el ID de canal de reserva del salpicadero. Cuando cambie el canal alternativo del panel de control, cualquier mensaje que no tenga un canal seleccionado explícitamente se enviará con el ID del nuevo canal alternativo.

He aquí un ejemplo del comportamiento esperado del canal de retroceso del salpicadero:

El canal de reserva de su panel de control se llama "Marketing" y tiene 10 mensajes push de Android para los que nunca ha seleccionado un canal. Estas campañas se envían a través del canal "Marketing" porque el canal "Marketing" es el canal de reserva del panel de control.

Además, tiene 15 mensajes que ha seleccionado para enviar a través del canal "Notificaciones sociales" y cinco mensajes que ha seleccionado para enviar a través del canal "Marketing".

A continuación, decide cambiar el canal predeterminado de su panel de control de "Marketing" a "Actualizaciones".

En esta situación, las 10 campañas sin selección de canal que antes se enviaban a través del canal "Marketing" ahora se enviarán a través del canal "Actualizaciones" porque estos mensajes se envían a través del canal de reserva. Los 15 mensajes que se enviaban a través del canal "Notificaciones sociales" seguirán enviándose a través del canal "Notificaciones sociales". Los cinco mensajes que se enviaban a través del canal "Marketing" se seguirán enviando a través de ese canal.

En caso de que se proporcione a Braze un ID de canal no válido (por ejemplo, si proporciona un ID de canal que sus desarrolladores no crearon en el SDK), enviaremos la notificación a través de su canal predeterminado del SDK. Por lo tanto, le recomendamos encarecidamente que pruebe sus canales de notificación a través del panel de Braze durante el desarrollo.

Para comprender mejor el comportamiento esperado de los canales, consulte la siguiente tabla:

|Escenario |Resultado  |    
| ---|-------------
|**La empresa ABC** se actualiza a un SDK compatible con Android O<br>**La empresa ABC** no añade ningún canal al cuadro de mandos de Braze<br>**La empresa ABC** no cambia el nombre de su canal SDK por defecto | Las notificaciones push enviadas a dispositivos Android O crearán un canal llamado "General" y las notificaciones se enviarán a través del canal "General"
|**La empresa XYZ** se actualiza a un SDK compatible con Android O <br>**La empresa XYZ** no añade ningún canal al cuadro de mandos de Braze<br>**La empresa XYZ** cambia el nombre de su canal SDK por defecto a "Marketing". | Las notificaciones push enviadas a dispositivos Android O crearán un canal llamado "Marketing" y las notificaciones se enviarán a través del canal "Marketing"
|**La empresa LMN** se actualiza a un SDK compatible con Android O <br>**La empresa LMN** define dos canales en su código de aplicación, "Promociones" y "Actualización de pedidos" <br>**La empresa LMN** añade los identificadores de canal para "Promociones" y "Actualización de pedidos" al cuadro de mandos de Braze. <br>**La empresa LMN** designa "Promociones" como canal alternativo del panel<br>**La empresa LMN** renombra su canal SDK predeterminado a "Marketing" | Las notificaciones push enviadas a dispositivos Android O no crearán un canal<br><br>A menos que el vendedor especifique explícitamente que las notificaciones deben enviarse a través del canal "Actualización de pedidos" o "Marketing", todas las notificaciones creadas antes de que los canales se añadieran al panel se enviarán a través del canal "Promociones".<br><br>El canal predeterminado del SDK, "Marketing", sólo se crea y utiliza si la empresa intenta enviar una notificación a través de un ID de canal no válido o si se selecciona explícitamente
|**La empresa HIJ** se actualiza a Android O pero no actualiza a la versión 2.1.0 o posterior del SDK para Android de Braze | Las notificaciones enviadas a usuarios con Android O o posterior no aparecen |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Añadir canales al salpicadero Braze

1. Abra cualquier campaña o lienzo que incluya un push de Android y haga clic en **Editar campaña**.
2. Navegue hasta el compositor de mensajes push de Android.
3. Haga clic en **Gestionar canales de notificación**. Todos los canales añadidos aquí estarán disponibles globalmente para todas las campañas y lienzos. Debe tener [permisos]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#limited-and-team-role-permissions) de "Gestión de aplicaciones" para su espacio de trabajo para gestionar canales.

Cuando se aplica un canal de notificación a una campaña específica o a un paso de Canvas, el recuento de **usuarios a los que se puede llegar** (situado en el paso Público objetivo) para Android Push no parece cambiar. Sin embargo, sólo los usuarios suscritos al canal de notificación seleccionado verán el mensaje, y los análisis de su campaña (como los clics) se medirán en función de esta audiencia.

![]({% image_buster /assets/img_archive/Click_Here.png %})

{:start="4"}
4\. Haga clic en **Añadir canal de notificación**.
5\. Introduzca el nombre y el ID del canal de notificación que desea añadir.<br><br>![]({% image_buster /assets/img_archive/Enter_Channel.png %})<br><br>
6\. Repite los pasos 4 y 5 para cada canal de notificación que quieras añadir.
7\. Pulse **Guardar** para guardar los cambios.

## Especificar el canal alternativo

Tu canal alternativo es el canal con el que Braze intentará enviar tu mensaje Android si no has seleccionado un canal para el mensaje. Las únicas campañas y lienzos que tendrán mensajes de Android sin una selección de canal son las campañas y lienzos que se crearon antes de que su equipo añadiera canales al panel Braze. Si cambia su canal de reserva, el cambio se aplicará globalmente a todas las campañas y lienzos sin una selección explícita de canal.

1. Abra cualquier campaña o Canvas existente.
2. Navega hasta el compositor push de Android.
3. Seleccione **Gestionar canales de notificación** después de ampliar las opciones de canales de notificación. <br><br>![]({% image_buster /assets/img_archive/Change_Fallback.png %}){: style="max-width:80%;"}<br><br>
4. Añade el canal al panel (si aún no se ha añadido).
5. Seleccione el dial de radio situado junto al canal que desea designar como canal alternativo.
6. Guarda los cambios. Sus cambios se aplicarán globalmente.

## Añadir canales a los mensajes push de Android

1. Navega hasta el compositor push de Android en cualquier campaña o Canvas.
2. Seleccione el canal que desea utilizar en el menú desplegable. Si no tiene un menú desplegable, sino la vista siguiente, tendrá que añadir canales antes de seleccionarlos para las campañas.

![]({% image_buster /assets/img_archive/No_Select.png %})

[3]: https://developer.android.com/preview/features/notification-channels.html#DeletingChannels
