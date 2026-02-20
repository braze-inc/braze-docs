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

Esta característica requiere [el comportamiento del botón al hacer clic](#button-actions), que es compatible con las siguientes versiones mínimas o posteriores:

{% sdk_min_versions swift:5.4.0 android:21.0.0 web:4.0.3 %}

Además, ten en cuenta los siguientes detalles específicos de la plataforma:

{% tabs local %}
{% tab android %}
|Versión del SO|Información adicional
\|----------|----------------------|
| **Android 12 y anteriores** | No se recomienda implementar primers push porque la adhesión voluntaria a push es predeterminada. |
| **Android 13+** | Si un usuario deniega dos veces tu solicitud de permiso push, Android bloquea las solicitudes posteriores, incluidos los mensajes de cartilla push de Braze. Para conceder el permiso después de esto, los usuarios deben habilitar manualmente la función push para tu aplicación en la configuración de su dispositivo. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
{% endtab %}

{% tab swift %}
### Información general

- El indicador push sólo puede mostrarse una vez por instalación, por imposición del sistema operativo.
- El aviso no aparece si la configuración push de la aplicación está explícitamente activada o desactivada. Sólo se muestra para usuarios con [autorización provisional](https://developer.apple.com/documentation/usernotifications/asking_permission_to_use_notifications#3544375).
  - **La configuración push de la aplicación está activada:** Braze no muestra el mensaje dentro de la aplicación, porque el usuario ya ha dado su adhesión voluntaria.
  - **La configuración push de la aplicación está desactivada:** Tienes que redirigir al usuario a la configuración de notificaciones push de tu aplicación dentro de los ajustes del dispositivo.

### Eliminación manual del código

El mensaje dentro de la aplicación que configures utilizando este tutorial llama automáticamente al código nativo de aviso push cuando un usuario hace clic en el botón de mensaje dentro de la aplicación. Para evitar solicitar el permiso de notificaciones push dos veces, o en el momento equivocado, un desarrollador debe modificar cualquier integración de notificaciones push existente que haya implementado para asegurarse de que su mensaje dentro de la aplicación sea la primera imprimación de notificación push que vean sus usuarios.

Tu equipo de desarrolladores debe revisar la implementación de las notificaciones push para tu aplicación o sitio web y eliminar manualmente cualquier código que solicite permiso push. Por ejemplo, elimina las referencias al siguiente código:

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

Primero, [crea un mensaje dentro de la aplicación]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/) y, a continuación, selecciona el tipo de mensaje y el diseño.

Para asegurarte de que tienes espacio suficiente tanto para tu mensaje como para los botones, utiliza un diseño de mensaje a pantalla completa o modal. Si eliges pantalla completa, ten en cuenta que se necesita una imagen.

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

Para las mejores prácticas y recursos adicionales, consulta [Crear mensajes de adhesión voluntaria personalizados]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/).

## Paso 3: Especifica el comportamiento del botón {#button-actions}

Para añadir botones a tu mensaje dentro de la aplicación, arrastra dos bloques **Botón** a tu mensaje, que actuarán como botones principal y secundario en tu mensaje dentro de la aplicación. También puedes arrastrar una fila a tu mensaje y luego arrastrar los botones a la fila, de modo que los botones estén en la misma fila horizontal (en lugar de apilados unos encima de otros). Recomendamos "Permitir notificaciones" y "Ahora no" como botones de inicio, pero hay muchos botones diferentes que puedes asignar.

Una vez que haya añadido la copia de botones, especifique el comportamiento al hacer clic de cada botón:

- **Botón 1:** Ajústelo a "Cerrar mensaje". Este es tu botón secundario, o la opción "Ahora no".
- **Botón 2:** Ajústalo a "Solicitar permiso push". Este es tu botón principal, o la opción "Permitir notificaciones".

![Creador de mensajes dentro de la aplicación con dos botones: "Permitir notificaciones" y "Ahora no".]({% image_buster /assets/img_archive/push_primer_button_behavior.png %})

## Paso 4: Programa la entrega

Para configurar tu push primer para que se envíe en un momento relevante, debes programar tu mensaje in-app como un mensaje basado en una acción con **Ejecutar evento personalizado** como acción desencadenante.

Aunque el momento ideal varía, Braze sugiere esperar hasta que el usuario complete algún tipo de [acción de alto valor](https://www.braze.com/resources/videos/mapping-high-value-actions), lo que indica que están empezando a ver el valor de su aplicación o sitio, o cuando hay una necesidad imperiosa que las notificaciones push pueden abordar (por ejemplo, después de que hayan realizado un pedido y desea ofrecerles información de seguimiento del envío). De este modo, el aviso beneficia al cliente y no sólo a su marca.

![Configuración de entrega basada en acciones para enviar a los usuarios que realizaron el evento personalizado de "Añadir a la lista de seguimiento".]({% image_buster /assets/img_archive/push_primer_trigger.png %})

## Paso 5: Usuarios objetivo

El objetivo de una campaña de imprimación push es avisar a los usuarios de cualquier dispositivo en el que aún no hayan concedido permisos push. Puede tratarse de usuarios primerizos o de usuarios existentes que adquieren un nuevo dispositivo o reinstalan tu aplicación.

{% alert important %}
**Supresión automática con push primer sin código**: Si utilizas la imprimación push sin código (la acción del botón "Solicitar permiso push"), no necesitas añadir filtros de suscripción push a tu segmentación. El SDK suprime automáticamente el mensaje dentro de la aplicación en los dispositivos que ya tienen un token de notificaciones push activo, independientemente del estado de notificaciones push del usuario en otros dispositivos. Para obtener más información sobre la orientación a usuarios con varios dispositivos, consulta [Orientación a usuarios con varios dispositivos](#targeting-users-with-multiple-devices).
{% endalert %}

Si no utilizas el primer push sin código, añade un filtro donde `Foreground Push Enabled For App is false`. Este filtro identifica instalaciones de aplicaciones individuales que aún no han optado por las notificaciones push en primer plano.

{% alert important %}
Utilizar un filtro a nivel de usuario como `Push Subscription Status is not Opted In` excluye a los usuarios que ya han optado por la adhesión voluntaria en otro dispositivo, impidiéndoles recibir el aviso en su nuevo dispositivo.
{% endalert %}

Más allá de eso, puede decidir qué segmentos adicionales le parecen más apropiados. Por ejemplo, puede dirigirse a usuarios que hayan completado una segunda compra, usuarios que acaben de crear una cuenta para convertirse en miembros o incluso usuarios que visiten su aplicación más de dos veces por semana. Dirigirse a los usuarios de estos segmentos cruciales aumenta la probabilidad de que los usuarios acepten y se conviertan en usuarios push.

### Dirigirse a usuarios con múltiples dispositivos

Dado que Braze captura los datos de usuario a nivel de perfil y no a nivel de dispositivo, dirigirse a usuarios que poseen varios dispositivos puede resultar complicado. Los filtros de suscripción push en la segmentación incluyen o excluyen a los usuarios en función del estado de suscripción de un único dispositivo, en lugar del estado de suscripción del dispositivo específico al que va dirigido. Además, los estados provisionales en iOS añaden complejidad, ya que estos dispositivos técnicamente tienen tokens de notificaciones push en primer plano, pero los usuarios no están explícitamente adheridos.

#### El problema de los filtros de suscripción push

Cuando un usuario tiene varios dispositivos con diferentes estados de suscripción push, es posible que los filtros de suscripción push de tu segmentación no se dirijan a algunos dispositivos. Considera estos supuestos:

{% details Scenario 1: User has two devices on different platforms %}

**El usuario tiene dos dispositivos:**
- Dispositivo A: Android, adhesión voluntaria a push
- Dispositivo B: iOS, sin adhesión voluntaria a push

**Filtros de segmento que no funcionan:**
- `Push enabled = false` - El usuario tiene habilitación push en su dispositivo Android, por lo que no entra en el segmento. El segmento no incluye el dispositivo iOS.
- `Push subscription status is not opted in` - El usuario tiene habilitación push en su dispositivo Android, por lo que no entra en el segmento. El segmento no incluye el dispositivo iOS.

**Filtros de segmento que funcionan:**
- `Push enabled for iOS = false` - El usuario tiene habilitación push en su dispositivo Android, pero sólo nos dirigimos a dispositivos iOS, así que el usuario entra en el segmento. El segmento incluye el dispositivo iOS.

{% enddetails %}

{% details Scenario 2: User has two iOS devices with different states %}

**El usuario tiene dos dispositivos iOS:**
- Dispositivo A: Adhesión voluntaria a push
- Dispositivo B: Habilitación provisional pero sin adhesión voluntaria

**Filtros de segmento que no funcionan:**
- `Push enabled = false` - El dispositivo A es de adhesión voluntaria al push, por lo que el usuario no entra en el segmento. El segmento no incluye el dispositivo B.
- `Provisionally opted in = true` - El dispositivo A está totalmente adherido voluntariamente, lo que significa que no está en estado provisional. El usuario no entra en el segmento. El segmento no incluye el dispositivo B.
- `Push enabled for app > iOS = false` - El dispositivo A tiene adhesión voluntaria a push en iOS, por lo que el usuario no entra en el segmento. El segmento no incluye el dispositivo B.
- `Push subscription status is not opted in` - El dispositivo A es de adhesión voluntaria al push, por lo que el usuario no entra en el segmento. El segmento no incluye el dispositivo B.

**Resultado:** El uso de cualquier combinación de estos filtros push hace que el segmento excluya al menos un dispositivo.

{% enddetails %}

{% details Scenario 3: User has three or more devices on the same OS %}

**El usuario tiene tres dispositivos:**
- Dispositivo A: Adhesión voluntaria a push
- Dispositivo B: No adhesión voluntaria a push
- Dispositivo C: No adhesión voluntaria a push

**Filtros de segmento que no funcionan:**
- `Push enabled = false` - El dispositivo A es de adhesión voluntaria al push, por lo que el usuario no entra en el segmento. El segmento no incluye los dispositivos B y C.
- `Push enabled for app > X = false` - El dispositivo A está adherido voluntariamente al push de la aplicación especificada, por lo que el usuario no entra en el segmento. El segmento no incluye los dispositivos B y C.
- `Push subscription status is not opted in` - El dispositivo A es de adhesión voluntaria al push, por lo que el usuario no entra en el segmento. El segmento no incluye los dispositivos B y C.

**Resultado:** Utilizar cualquier combinación de estos filtros push deja al menos un dispositivo sin filtrar.

{% enddetails %}

#### Solución: Utiliza el primer push sin código

La solución recomendada es utilizar el cebador push sin código (la acción del botón "Solicitar permiso push") sin filtros adicionales de segmentación del estado push.

{% alert important %}
**Supresión automática**: El primer push sin código se suprime automáticamente en los dispositivos que ya tienen un token de notificaciones push activo. El SDK comprueba si un usuario en su dispositivo específico ya tiene un token de notificaciones push. Si el SDK descubre que el usuario ya ha optado por la adhesión (por ejemplo, a partir de una solicitud anterior o a través de la configuración del dispositivo), el SDK suprime automáticamente el mensaje dentro de la aplicación sin necesidad de filtros de segmentación adicionales. La cartilla se muestra en todos los demás escenarios, incluso si un usuario ha optado provisionalmente por el push.
{% endalert %}

La ventaja de utilizar la imprimación push sin código es que la funcionalidad está soportada por el SDK de Braze. Como el SDK puede detectar el estado del token de notificaciones push en el dispositivo concreto que muestra el mensaje, no necesitas depender de filtros de segmentación a nivel de perfil que pueden excluir a usuarios con varios dispositivos.

#### Consideraciones

**No requiere código push primer**: Debes utilizar la imprimación push sin código para que funcione la supresión automática. Si configuras una lógica personalizada o vínculos profundos en lugar de utilizar la acción del botón "Solicitar permiso push", el SDK no puede identificar que estás intentando mostrar una carátula push. Esto hace que se muestre el mensaje independientemente del estado de suscripción de ese dispositivo.

**Suprimir para los usuarios que optaron por no participar**: Puede que quieras suprimir el mensaje dentro de la aplicación para los usuarios que hayan optado explícitamente por no recibir push (por ejemplo, desde la solicitud nativa o la configuración del dispositivo) y reorientar a esos usuarios con una campaña de nutrición separada. Para ello, utiliza la siguiente lógica Liquid en combinación con la cartilla sin código:

{% raw %}
```liquid
{% if targeted_device.${foreground_push_enabled} == false %} 
{% abort_message('user turned off push notifications') %} 
{% endif %}
- message goes here -
```
{% endraw %}

El filtro `targeted_device` Liquid sólo tiene en cuenta el dispositivo en el que se muestra el mensaje, en lugar del perfil de usuario. En ese dispositivo, `foreground_push_enabled` se establece en `true` cuando hay un token de notificaciones push activo en primer plano y se establece en `false` cuando el sistema operativo informa de que las notificaciones push se han desactivado (por ejemplo, el usuario las desactivó explícitamente). Para los dispositivos completamente nuevos que aún no han respondido a un estado de permiso push, `foreground_push_enabled` está sin configurar y no tiene valor. Dado que la condición Liquid comprueba específicamente `{% raw %}``false`{% endraw %}, suprime la imprimación sólo para los dispositivos con una adhesión voluntaria explícita, mientras que los dispositivos en este estado desconocido siguen cumpliendo los requisitos y pueden recibir la imprimación push.

## Paso 6: Eventos de conversión

Braze sugiere una configuración predeterminada para las conversiones, pero es posible que desee configurar [eventos de conversión]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/) en torno a los cebadores de empuje.