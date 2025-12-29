---
nav_title: Push primer mensajes dentro de la aplicación
article_title: Push Primer Mensajes dentro de la aplicación
page_order: 1
page_type: reference
description: "Este artículo cubre los requisitos previos para los mensajes push primer dentro de la aplicación y cómo configurarlos."
channel: push

---

# Push primer mensajes dentro de la aplicación

Push primer mensaje dentro de la aplicación de streaming. La notificación dice "¿Recibir notificaciones push de Movie Cannon? Las notificaciones pueden incluir nuevas películas, programas de TV u otras notificaciones y pueden desactivarse en cualquier momento."]({% image_buster /assets/img_archive/push_primer_iam.png %}){: style="float:right;max-width:40%;margin-left:15px;border:none;"}

> Sólo tienes una oportunidad de pedir permiso push a los usuarios, así que optimizar tu registro push es crucial para maximizar el alcance de tus mensajes push. Para conseguirlo, puedes utilizar mensajes dentro de la aplicación para explicar qué tipo de mensajes pueden recibir tus usuarios si deciden adherirse, antes de mostrarles el mensaje de adhesión voluntaria push nativo. Esto se denomina imprimación push.

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
- El aviso no se mostrará si la configuración push de la aplicación está explícitamente activada o desactivada, sólo se mostrará a los usuarios con [autorización provisional](https://developer.apple.com/documentation/usernotifications/asking_permission_to_use_notifications#3544375).
  - **La configuración push de la aplicación está activada:** Braze no mostrará el mensaje dentro de la aplicación, ya que el usuario ya ha dado su adhesión voluntaria.
  - **La configuración push de la aplicación está desactivada:** Tendrás que redirigir al usuario a la configuración de notificaciones push de tu aplicación dentro de los ajustes del dispositivo.

### Eliminación manual del código

El mensaje dentro de la aplicación que configures mediante este tutorial llamará automáticamente al código nativo de aviso push cuando un usuario haga clic en el botón de mensaje dentro de la aplicación. Para evitar solicitar permiso de notificación push dos veces, o en el momento equivocado, un desarrollador debe modificar cualquier integración de notificación push existente que haya implementado para asegurarse de que tu mensaje dentro de la aplicación sea la primera cartilla de notificación push que vean tus usuarios.

Tu equipo de desarrolladores debe revisar la implementación de las notificaciones push para tu aplicación o sitio web y eliminar manualmente cualquier código que solicite permiso push. Por ejemplo, eliminarías las referencias al siguiente código:

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

## Paso 1: Crear un mensaje dentro de la aplicación

En primer lugar, [crea un mensaje dentro de la aplicación]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/) y, a continuación, selecciona el tipo de mensaje y el diseño.

Para asegurarte de que tienes espacio suficiente tanto para tu mensaje como para los botones, utiliza un diseño de mensaje a pantalla completa o modal. Si eliges pantalla completa, ten en cuenta que se necesita una imagen.

## Paso 2: Construye tu mensaje

¡Ahora es el momento de añadir tu copia! Recuerda que un cebador push se supone que prepara al usuario para activar las notificaciones push. En el cuerpo de tu mensaje, te sugerimos que destaques las razones por las que tus usuarios deberían tener activadas las notificaciones push. Especifica qué tipo de notificaciones quieres enviar y qué valor pueden aportar.

Por ejemplo, una aplicación de noticias podría utilizar el siguiente push primer:

```plaintext
Breaking news on the go! Enable push notifications to get alerts for major stories and topics that matter to you.
```

Mientras que una aplicación de streaming podría utilizar lo siguiente:

```plaintext
Get push notifications from Movie Cannon? Notifications may include new movies, TV shows, or other notices and can be turned off at any time.
```

Para conocer las mejores prácticas y recursos adicionales, consulta [Crear mensajes de adhesión voluntaria personalizados]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/).

## Paso 3: Especifica el comportamiento del botón {#button-actions}

Para añadir botones a tu mensaje dentro de la aplicación, arrastra dos bloques **Botón** a tu mensaje, que actuarán como botones principal y secundario en tu mensaje dentro de la aplicación. También puedes arrastrar una fila a tu mensaje y luego arrastrar los botones a la fila, de modo que los botones estén en la misma fila horizontal (en lugar de apilados unos encima de otros). Recomendamos "Permitir notificaciones" y "Ahora no" como botones de inicio, pero hay muchos botones diferentes que podrías asignar.

Una vez que hayas añadido la copia de los botones, especifica el comportamiento al hacer clic de cada botón:

- **Botón 1:** Ajústalo a "Cerrar mensaje". Este es tu botón secundario, o la opción "Ahora no".
- **Botón 2:** Ajústalo a "Solicitar permiso push". Este es tu botón principal, o la opción "Permitir notificaciones".

\![Creador de mensajes dentro de la aplicación con dos botones: "Permitir notificaciones" y "Ahora no".]({% image_buster /assets/img_archive/push_primer_button_behavior.png %})

## Paso 4: Programar la entrega

Para configurar tu imprimación push para que se envíe en un momento relevante, debes programar tu mensaje dentro de la aplicación como un mensaje basado en una acción con **Realizar evento personalizado** como acción desencadenante.

Aunque el momento ideal varía, Braze sugiere esperar hasta que un usuario complete algún tipo de [acción de gran valor](https://www.braze.com/resources/videos/mapping-high-value-actions), lo que indica que está empezando a ver valor en tu aplicación o sitio, o cuando exista una necesidad imperiosa que las notificaciones push puedan satisfacer (como después de que haya realizado un pedido y quieras ofrecerle información de seguimiento del envío). De este modo, el aviso beneficia al cliente y no sólo a tu marca.

\![Configuración de entrega basada en acciones para enviar a los usuarios que realizaron el evento personalizado de "Añadir a la lista de seguimiento".]({% image_buster /assets/img_archive/push_primer_trigger.png %})

## Paso 5: Usuarios objetivo

El objetivo de una campaña de imprimación push es avisar a los usuarios de cualquier dispositivo en el que aún no hayan concedido permisos push. Puede tratarse de usuarios primerizos o de usuarios existentes que adquieren un nuevo dispositivo o reinstalan tu aplicación. Para orientar correctamente tu campaña push primer, añade un filtro donde `Foreground Push Enabled For App is false`. Este filtro identifica instalaciones de aplicaciones individuales que aún no han optado por las notificaciones push en primer plano.

{% alert important %}
Si utilizas un filtro a nivel de usuario como `Push Subscription Status is not Opted In`, excluirás a los usuarios que ya hayan recibido la adhesión voluntaria en otro dispositivo, lo que les impedirá recibir el mensaje en su nuevo dispositivo.
{% endalert %}

Más allá de eso, puedes decidir qué segmentos adicionales te parecen más adecuados. Por ejemplo, puedes dirigirte a usuarios que hayan completado una segunda compra, usuarios que acaben de hacerse una cuenta para convertirse en miembros, o incluso usuarios que visiten tu aplicación más de dos veces por semana. Dirigirse a los usuarios de estos segmentos cruciales aumenta la probabilidad de que los usuarios se adhieran voluntariamente y se habiliten para push.

## Paso 6: Eventos de conversión

Braze sugiere configuraciones predeterminadas para las conversiones, pero puede que quieras configurar [eventos de conversión]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/) en torno a los cebadores push.

