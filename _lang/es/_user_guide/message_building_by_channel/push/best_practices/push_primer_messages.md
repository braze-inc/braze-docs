---
nav_title: Mensajes push primer dentro de la aplicación
article_title: Mensajes Push Primer In-App
page_order: 1
page_type: reference
description: "Este artículo cubre los requisitos previos para los mensajes push primer dentro de la aplicación y cómo configurarlos."
channel: push

---

# Mensajes push primer dentro de la aplicación

![Mensajes push primer dentro de la aplicación de streaming. La notificación dice "¿Recibir notificaciones push de Movie Cannon? Las notificaciones pueden incluir nuevas películas, programas de televisión u otros avisos y pueden desactivarse en cualquier momento."]({% image_buster /assets/img_archive/push_primer_iam.png %}){: style="float:right;max-width:40%;margin-left:15px;border:none;"}

> Sólo se tiene una oportunidad de pedir permiso a los usuarios, por lo que optimizar el registro es crucial para maximizar el alcance de los mensajes push. Para lograrlo, puede utilizar mensajes dentro de la aplicación para explicar qué tipo de mensajes pueden recibir los usuarios si deciden participar, antes de mostrarles el mensaje push nativo. Esto se conoce como push primer.

Para crear un mensaje push primer dentro de la aplicación en Braze, puedes utilizar el comportamiento del botón al hacer clic "Solicitar permiso push" al crear un mensaje dentro de la aplicación para iOS, Android o Web.

## Requisitos previos

Esta característica requiere que [el botón](#button-actions) tenga [un comportamiento al hacer clic](#button-actions), lo cual es compatible con las siguientes versiones mínimas o posteriores:

{% sdk_min_versions swift:5.4.0 android:21.0.0 web:4.0.3 %}

Además, hay una nota sobre los siguientes detalles específicos de la plataforma:

{% tabs local %}
{% tab android %}
|Versión del sistema operativo|Información adicional|
\|----------|----------------------|
| **Android 12 y versiones anteriores** | No se recomienda implementar activadores push, ya que la adhesión voluntaria a push está activada de forma predeterminada. |
| **Android 13+** | Si un usuario rechaza dos veces tu solicitud de permiso para enviar notificaciones push, Android bloqueará las solicitudes posteriores, incluidos los mensajes introductorios de Braze. Para conceder el permiso después de esto, los usuarios deben habilitar manualmente las notificaciones push para tu aplicación en la configuración de sus dispositivos. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
{% endtab %}

{% tab swift %}
### Información general

- El mensaje de push solo se puede mostrar una vez por instalación, según lo exige el sistema operativo.
- El mensaje no se muestra si la configuración de notificaciones push de la aplicación está activada o desactivada explícitamente. Solo se muestra a los usuarios con [autorización provisional](https://developer.apple.com/documentation/usernotifications/asking_permission_to_use_notifications#3544375).
  - **La configuración de notificaciones push de la aplicación está activada:** Braze no muestra el mensaje dentro de la aplicación, ya que el usuario ya ha realizado la adhesión voluntaria.
  - **La configuración de notificaciones push de la aplicación está desactivada:** Debes redirigir al usuario a la configuración de las notificaciones push de tu aplicación dentro de la configuración del dispositivo.

### Eliminación manual del código

El mensaje dentro de la aplicación que configuraste siguiendo este tutorial activa automáticamente el código de notificación push nativo cuando un usuario hace clic en el botón de mensajes dentro de la aplicación. Para evitar solicitar el permiso de notificaciones push dos veces, o en el momento equivocado, un desarrollador debe modificar cualquier integración de notificaciones push existente que haya implementado para asegurarse de que su mensaje dentro de la aplicación sea la primera imprimación de notificación push que vean sus usuarios.

Tu equipo de desarrollo debe revisar la implementación de las notificaciones push para tu aplicación o sitio web y eliminar manualmente cualquier código que solicite permiso para enviarlas. Por ejemplo, elimina las referencias al siguiente código:

{% subtabs %}
{% subtab OBJECTIVE-C %}
```objc
requestAuthorizationWithOptions
```
{% endsubtab %}
{% subtab swift %}
```swift
requestAuthorization
```
{% endsubtab %}
{% subtab JavaScript %}
```javascript
braze.requestPushPermission()
// or
appboy.registerAppboyPushMessages()
```
{% endsubtab %}
{% subtab Java %}
```java
android.permission.POST_NOTIFICATIONS
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Paso 1: Crear un mensaje en la aplicación

Primero, [crea un mensaje dentro de la aplicación]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/) y, a continuación, selecciona el tipo y el diseño del mensaje.

Para asegurarte de que tienes suficiente espacio tanto para tu mensaje como para los botones, utiliza un diseño de mensaje a pantalla completa o modal. Si eliges la opción de pantalla completa, hay una nota que indica que es necesario incluir una imagen.

## Paso 2: Construye tu mensaje

Ahora es el momento de añadir su copia. Recuerda que un push primer se supone que prepara al usuario para activar las notificaciones push. En el cuerpo del mensaje, te sugerimos que destaques las razones por las que tus usuarios deberían tener activadas las notificaciones push. Especifique qué tipo de notificaciones desea enviar y qué valor pueden aportar.

Por ejemplo, una aplicación de noticias podría utilizar el siguiente push primer:

```plaintext
Breaking news on the go! Enable push notifications to get alerts for major stories and topics that matter to you.
```

Mientras que una aplicación de streaming podría utilizar lo siguiente:

```plaintext
Get push notifications from Movie Cannon? Notifications may include new movies, TV shows, or other notices and can be turned off at any time.
```

Para conocer las prácticas recomendadas y obtener recursos adicionales, consulta [Creación]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/) de [mensajes de adhesión voluntaria personalizados]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/).

## Paso 3: Especifica el comportamiento del botón {#button-actions}

Para añadir botones a tu mensaje dentro de la aplicación, arrastra dos bloques **Botón** al mensaje, que actuarán como botones principal y secundario en tu mensaje dentro de la aplicación. También puedes arrastrar una fila al mensaje y, a continuación, arrastrar los botones a la fila, de modo que los botones queden en la misma fila horizontal (en lugar de apilados unos encima de otros). Recomendamos «Permitir notificaciones» y «Ahora no» como botones iniciales, pero hay muchos otros botones diferentes que puedes asignar.

Una vez que haya añadido la copia de botones, especifique el comportamiento al hacer clic de cada botón:

- **Botón 1:** Ajústelo a "Cerrar mensaje". Este es tu botón secundario, o la opción "Ahora no".
- **Botón 2:** Ajústalo a "Solicitar permiso push". Este es tu botón principal, o la opción "Permitir notificaciones".

![Creador de mensajes dentro de la aplicación con dos botones: «Permitir notificaciones» y «Ahora no».]({% image_buster /assets/img_archive/push_primer_button_behavior.png %})

## Paso 4: Programa la entrega

Para configurar tu push primer para que se envíe en un momento relevante, debes programar tu mensaje in-app como un mensaje basado en una acción con **Ejecutar evento personalizado** como acción desencadenante.

Aunque el momento ideal varía, Braze sugiere esperar hasta que el usuario complete algún tipo de [acción de alto valor](https://www.braze.com/resources/videos/mapping-high-value-actions), lo que indica que están empezando a ver el valor de su aplicación o sitio, o cuando hay una necesidad imperiosa que las notificaciones push pueden abordar (por ejemplo, después de que hayan realizado un pedido y desea ofrecerles información de seguimiento del envío). De este modo, el aviso beneficia al cliente y no sólo a su marca.

![Configuración de entrega basada en acciones para enviar a los usuarios que realizaron el evento personalizado «Añadir a la lista de seguimiento».]({% image_buster /assets/img_archive/push_primer_trigger.png %})

## Paso 5: Usuarios objetivo

El objetivo de una campaña de introducción de notificaciones push es avisar a los usuarios en cualquier dispositivo en el que aún no hayan concedido permisos push. Esto puede incluir a usuarios nuevos o existentes que adquieren un dispositivo nuevo o reinstalan tu aplicación.

{% alert important %}
**Supresión automática con imprimación push sin código**: Si utilizas la introducción sin código (la acción del botón «Solicitar permiso para enviar notificaciones push»), no es necesario que añadas filtros de suscripción a notificaciones push a tu segmentación. El SDK suprime automáticamente el mensaje dentro de la aplicación en los dispositivos que ya tienen un token de notificaciones push activo, independientemente del estado de push del usuario en otros dispositivos. Para obtener más información sobre cómo dirigirte a usuarios con varios dispositivos, consulta [Dirigirse a usuarios con varios dispositivos](#targeting-users-with-multiple-devices).
{% endalert %}

Si no estás utilizando el iniciador push sin código, añade un filtro donde puedes `Foreground Push Enabled For App is false`filtrar. Este filtro identifica las instalaciones de aplicaciones individuales que aún no han realizado la adhesión voluntaria a las notificaciones push en primer plano.

{% alert important %}
El uso de un filtro a nivel de usuario como`Push Subscription Status is not Opted In`  excluye a los usuarios que ya han realizado la adhesión voluntaria en otro dispositivo, lo que impide que reciban el mensaje de adhesión voluntaria en su nuevo dispositivo.
{% endalert %}

Más allá de eso, puede decidir qué segmentos adicionales le parecen más apropiados. Por ejemplo, puede dirigirse a usuarios que hayan completado una segunda compra, usuarios que acaben de crear una cuenta para convertirse en miembros o incluso usuarios que visiten su aplicación más de dos veces por semana. Dirigirse a los usuarios de estos segmentos cruciales aumenta la probabilidad de que los usuarios acepten y se conviertan en usuarios push.

### Dirigirse a usuarios con múltiples dispositivos

Dado que Braze recopila datos de usuario a nivel de perfil en lugar de a nivel de dispositivo, puede resultar complicado dirigirse a usuarios que poseen varios dispositivos. Los filtros de suscripción push en la segmentación incluyen o excluyen a los usuarios en función del estado de suscripción de un único dispositivo, en lugar del estado de suscripción del dispositivo específico al que se dirige. Además, los estados provisionales en iOS añaden complejidad, ya que estos dispositivos técnicamente tienen tokens de notificaciones push en primer plano, pero los usuarios no han realizado una adhesión voluntaria.

#### El problema con los filtros de suscripción push

Cuando un usuario tiene varios dispositivos con diferentes estados de suscripción push, es posible que los filtros de suscripción push de tu segmentación no logren dirigirse a algunos dispositivos. Considera estos escenarios:

{% details Scenario 1: User has two devices on different platforms %}

**El usuario tiene dos dispositivos:**
- Dispositivo A: Android, adhesión voluntaria a recibir notificaciones push
- Dispositivo B: iOS, sin adhesión voluntaria a la opción push

**Filtros de segmento que no funcionan:**
- `Push enabled = false` - El usuario tiene habilitada la función push en su dispositivo Android, por lo que no entra en el segmento. El segmento no incluye el dispositivo iOS.
- `Push subscription status is not opted in` - El usuario tiene habilitada la función push en su dispositivo Android, por lo que no entra en el segmento. El segmento no incluye el dispositivo iOS.

**Filtros de segmento que funcionan:**
- `Push enabled for iOS = false` - El usuario tiene habilitada la función push en su dispositivo Android, pero solo nos dirigimos a dispositivos iOS, por lo que el usuario entra en el segmento. El segmento incluye el dispositivo iOS.

{% enddetails %}

{% details Scenario 2: User has two iOS devices with different states %}

**El usuario tiene dos dispositivos iOS:**
- Dispositivo A: Ha realizado una adhesión voluntaria para recibir notificaciones push.
- Dispositivo B: Habilitado provisionalmente, pero sin adhesión voluntaria

**Filtros de segmento que no funcionan:**
- `Push enabled = false` - El dispositivo A ha realizado la adhesión voluntaria a las notificaciones push, por lo que el usuario no entra en el segmento. El segmento no incluye el dispositivo B.
- `Provisionally opted in = true` - El dispositivo A ha realizado la adhesión voluntaria, lo que significa que no se encuentra en estado provisional. El usuario no entra en el segmento. El segmento no incluye el dispositivo B.
- `Push enabled for app > iOS = false` - El dispositivo A ha realizado la adhesión voluntaria a las notificaciones push en iOS, por lo que el usuario no entra en el segmento. El segmento no incluye el dispositivo B.
- `Push subscription status is not opted in` - El dispositivo A ha realizado la adhesión voluntaria a las notificaciones push, por lo que el usuario no entra en el segmento. El segmento no incluye el dispositivo B.

**Resultado:** El uso de cualquier combinación de estos filtros push da como resultado que el segmento excluya al menos un dispositivo.

{% enddetails %}

{% details Scenario 3: User has three or more devices on the same OS %}

**El usuario tiene tres dispositivos:**
- Dispositivo A: Ha realizado una adhesión voluntaria para recibir notificaciones push.
- Dispositivo B: No ha realizado la adhesión voluntaria para recibir notificaciones push.
- Dispositivo C: No ha realizado la adhesión voluntaria para recibir notificaciones push.

**Filtros de segmento que no funcionan:**
- `Push enabled = false` - El dispositivo A ha realizado la adhesión voluntaria a las notificaciones push, por lo que el usuario no entra en el segmento. El segmento no incluye los dispositivos B y C.
- `Push enabled for app > X = false` - El dispositivo A ha realizado la adhesión voluntaria a la plataforma de push para la aplicación especificada, por lo que el usuario no entra en el segmento. El segmento no incluye los dispositivos B y C.
- `Push subscription status is not opted in` - El dispositivo A ha realizado la adhesión voluntaria a las notificaciones push, por lo que el usuario no entra en el segmento. El segmento no incluye los dispositivos B y C.

**Resultado:** El uso de cualquier combinación de estos filtros push deja al menos un dispositivo sin seleccionar.

{% enddetails %}

#### Solución: Utiliza la guía básica de push sin código

La solución recomendada es utilizar el iniciador push sin código (la acción del botón «Solicitar permiso push») sin filtros adicionales de segmentación del estado push.

{% alert important %}
**Supresión automática**: La función push sin código se suprime automáticamente en los dispositivos que ya tienen un token de notificaciones push activo. El SDK comprueba si un usuario en su dispositivo específico ya tiene un token de notificaciones push. Si el SDK detecta que el usuario ya ha realizado la adhesión voluntaria (por ejemplo, en una solicitud anterior o a través de la configuración del dispositivo), el SDK suprime automáticamente el mensaje dentro de la aplicación sin necesidad de aplicar filtros de segmentación adicionales. La guía muestra todos los demás escenarios, incluido el caso en el que un usuario haya realizado una adhesión voluntaria a las notificaciones push.
{% endalert %}

La ventaja de utilizar el iniciador push sin código es que la funcionalidad es compatible con el SDK de Braze. Dado que el SDK puede detectar el estado del token de notificaciones push en el dispositivo específico que muestra el mensaje, no es necesario depender de filtros de segmentación a nivel de perfil que pueden excluir a los usuarios con varios dispositivos.

#### Consideraciones

**No se requiere conocimiento previo de programación push**: Debes utilizar el iniciador push sin código para que la supresión automática funcione. Si configuras una lógica personalizada o vínculos profundos en lugar de utilizar la acción del botón «Solicitar permiso para enviar notificaciones push», el SDK no podrá identificar que estás intentando mostrar una notificación push. Esto hace que se muestre el mensaje independientemente del estado de la suscripción de ese dispositivo.

**Supresión para los usuarios que se han dado de baja**: Es posible que desees suprimir el mensaje dentro de la aplicación para los usuarios que hayan optado explícitamente por no recibir notificaciones push (por ejemplo, desde la solicitud nativa o la configuración del dispositivo) y reorientar a esos usuarios con una campaña de fidelización independiente. Para ello, utiliza la siguiente lógica Liquid en combinación con la introducción sin código:

{% raw %}
```liquid
{% if targeted_device.${foreground_push_enabled} == false %} 
{% abort_message('user turned off push notifications') %} 
{% endif %}
- message goes here -
```
{% endraw %}

El filtro`targeted_device` Liquid solo tiene en cuenta el dispositivo en el que se muestra el mensaje, en lugar del perfil de usuario. En ese dispositivo,`foreground_push_enabled`  se establece en`true`  cuando hay un token de notificaciones push activo en primer plano y se establece en`false`  cuando el sistema operativo informa de que las notificaciones push se han desactivado (por ejemplo, el usuario las ha desactivado explícitamente). En el caso de dispositivos completamente nuevos que aún no han respondido a un estado de permiso push,`foreground_push_enabled`  no está configurado y no tiene ningún valor. Dado que la condición Liquid comprueba específicamente`{% raw %}``false`{% endraw %}, solo suprime el primer para los dispositivos con una exclusión explícita, mientras que los dispositivos en este estado desconocido siguen siendo aptos y pueden recibir el primer push.

## Paso 6: Eventos de conversión

Braze sugiere una configuración predeterminada para las conversiones, pero es posible que desee configurar [eventos de conversión]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/) en torno a los cebadores de empuje.