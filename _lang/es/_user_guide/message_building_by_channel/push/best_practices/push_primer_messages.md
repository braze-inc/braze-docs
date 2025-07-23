---
nav_title: Mensajes Push Primer In-App
article_title: Mensajes Push Primer In-App
page_order: 1
page_type: reference
description: "Este artículo cubre los requisitos previos para los mensajes push primer dentro de la aplicación y cómo configurarlos."
channel: push

---

# Mensajes push primer dentro de la aplicación

![Mensajes push primer dentro de la aplicación de streaming. La notificación dice "¿Recibir notificaciones push de Movie Cannon? Las notificaciones pueden incluir nuevas películas, programas de televisión u otros avisos y pueden desactivarse en cualquier momento."][1]{: style="float:right;max-width:40%;margin-left:15px;border:none;"}

> Sólo se tiene una oportunidad de pedir permiso a los usuarios, por lo que optimizar el registro es crucial para maximizar el alcance de los mensajes push. Para lograrlo, puede utilizar mensajes dentro de la aplicación para explicar qué tipo de mensajes pueden recibir los usuarios si deciden participar, antes de mostrarles el mensaje push nativo. Esto se conoce como push primer.

Para crear un mensaje push primer dentro de la aplicación en Braze, puedes utilizar el comportamiento del botón al hacer clic "Solicitar permiso push" al crear un mensaje dentro de la aplicación para iOS, Android o Web.

## Requisitos previos

Esta guía utiliza un [comportamiento de botón al hacer clic](#button-actions) que solo es compatible con las versiones más recientes del SDK. Ten en cuenta que es posible que algunos de estos SDK aún no se hayan publicado. Visita los siguientes enlaces para consultar la versión actual:

{% sdk_min_versions swift:5.4.0 android:21.0.0 web:4.0.3 %}

### Notas para los equipos de desarrollo

#### Android

- **Android 12 e inferior:** No se recomienda implementar push primers porque la adhesión voluntaria a push es predeterminada.
- **Android 13 y superior:** Si quieres ver el aviso varias veces mientras realizas la prueba, ve a la configuración del dispositivo y desactiva la función push para que la aplicación vuelva a mostrar el aviso.

#### iOS

- El aviso de iOS sólo puede mostrarse una vez por instalación, por imposición del sistema operativo.
- El aviso no se mostrará si la configuración push de la aplicación está explícitamente activada o desactivada, sólo se mostrará a los usuarios con [autorización provisional](https://developer.apple.com/documentation/usernotifications/asking_permission_to_use_notifications#3544375).
  - Si la configuración push de la aplicación está activada, Braze no muestra el mensaje dentro de la aplicación, ya que el usuario ya está adherido voluntariamente.
  - Si la configuración push de la aplicación está desactivada, debes reenviar al usuario a la configuración de notificaciones de la aplicación en la aplicación de configuración.

##### Eliminación manual del código

El mensaje dentro de la aplicación que configure utilizando este tutorial llamará automáticamente al código nativo de aviso push cuando un usuario haga clic en el botón de mensaje dentro de la aplicación. Para evitar solicitar el permiso de notificaciones push dos veces, o en el momento equivocado, un desarrollador debe modificar cualquier integración de notificaciones push existente que haya implementado para asegurarse de que su mensaje dentro de la aplicación sea la primera imprimación de notificación push que vean sus usuarios.

El desarrollador debe revisar su implementación de notificaciones push para su aplicación o sitio y eliminar manualmente cualquier código que solicite permiso push. Por ejemplo, busque y elimine las referencias al siguiente código:

{% tabs %}
{% tab OBJETIVO-C %}
```objc
requestAuthorizationWithOptions
```
{% endtab %}
{% tab swift %}
```swift
requestAuthorization
```
{% endtab %}
{% tab JavaScript %}
```javascript
braze.requestPushPermission()
// or
appboy.registerAppboyPushMessages()
```
{% endtab %}
{% tab Java %}
```java
android.permission.POST_NOTIFICATIONS
```
{% endtab %}
{% endtabs %}

## Paso 1: Crear un mensaje en la aplicación

[Crea un mensaje dentro de la aplicación][2] como lo harías habitualmente.

Seleccione un tipo de mensaje y un diseño. Para que tengas espacio suficiente para explicar qué notificaciones push pueden esperar tus usuarios (y para permitir botones), Braze sugiere un mensaje a pantalla completa o modal. Ten en cuenta que para un mensaje dentro de la aplicación a pantalla completa, se requiere una imagen. 

## Paso 2: Construye tu mensaje

Ahora es el momento de añadir su copia. Recuerda que un push primer se supone que prepara al usuario para activar las notificaciones push. En el cuerpo del mensaje, te sugerimos que destaques las razones por las que tus usuarios deberían tener activadas las notificaciones push. Especifique qué tipo de notificaciones desea enviar y qué valor pueden aportar.

Por ejemplo, una aplicación de noticias podría utilizar el siguiente push primer:

> Noticias de última hora sobre la marcha Activa las notificaciones push para recibir alertas sobre las principales noticias y temas que te interesan.

Mientras que una aplicación de streaming podría utilizar lo siguiente:

> ¿Recibir notificaciones push de Movie Cannon? Las notificaciones pueden incluir nuevas películas, programas de televisión u otros avisos, y pueden desactivarse en cualquier momento.

Para las mejores prácticas y recursos adicionales, consulta [Crear mensajes de adhesión voluntaria personalizados][3].

## Paso 3: Especifica el comportamiento del botón {#button-actions}

Para añadir botones a tu mensaje in-app, añade texto a los campos de texto **Botón 1** y **Botón 2**, que son los botones secundario y principal de tu mensaje in-app respectivamente. Recomendamos "Permitir notificaciones" y "Ahora no" como botones de inicio, pero hay muchas indicaciones de botones diferentes que podrías asignar.

Una vez que haya añadido la copia de botones, especifique el comportamiento al hacer clic de cada botón:

- **Botón 1:** Ajústelo a "Cerrar mensaje". Este es tu botón secundario, o la opción "Ahora no".
- **Botón 2:** Ajústalo a "Solicitar permiso push". Este es tu botón principal, o la opción "Permitir notificaciones".

![][4]

## Paso 4: Programa la entrega

Para configurar tu push primer para que se envíe en un momento relevante, debes programar tu mensaje in-app como un mensaje basado en una acción con **Ejecutar evento personalizado** como acción desencadenante.

Aunque el momento ideal varía, Braze sugiere esperar hasta que el usuario complete algún tipo de [acción de alto valor](https://www.braze.com/resources/videos/mapping-high-value-actions), lo que indica que están empezando a ver el valor de su aplicación o sitio, o cuando hay una necesidad imperiosa que las notificaciones push pueden abordar (por ejemplo, después de que hayan realizado un pedido y desea ofrecerles información de seguimiento del envío). De este modo, el aviso beneficia al cliente y no sólo a su marca.

![][5]

## Paso 5: Usuarios objetivo

Dado que el objetivo de una campaña de imprimación push es incitar a los usuarios a aceptar la mensajería push, no debe dirigirse a usuarios que ya la hayan aceptado. Para ello, añada un segmento o filtro donde `Push Subscription Status is not Opted In`.

Más allá de eso, puede decidir qué segmentos adicionales le parecen más apropiados. Por ejemplo, puede dirigirse a usuarios que hayan completado una segunda compra, usuarios que acaben de crear una cuenta para convertirse en miembros o incluso usuarios que visiten su aplicación más de dos veces por semana. Dirigirse a los usuarios de estos segmentos cruciales aumenta la probabilidad de que los usuarios acepten y se conviertan en usuarios push.

## Paso 6: Eventos de conversión

Braze sugiere una configuración predeterminada para las conversiones, pero es posible que desee configurar [eventos de conversión]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/) en torno a los cebadores de empuje.

[1]: {% image_buster /assets/img_archive/push_primer_iam.png %}
[2]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/
[3]: {{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/creating_custom_opt-in_prompts/
[4]: {% image_buster /assets/img_archive/push_primer_button_behavior.png %}
[5]: {% image_buster /assets/img_archive/push_primer_trigger.png %}
