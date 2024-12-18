---
nav_title: Solución de problemas
article_title: Solución de problemas de notificaciones push para iOS
platform: Swift
page_order: 28
description: "En este artículo se proporcionan varios escenarios de solución de problemas de notificaciones push de iOS para el SDK Swift."
channel:
  - push

---

# Solución de problemas {#push-troubleshooting}

> En este artículo se proporcionan varios escenarios de solución de problemas de notificaciones push de iOS para el SDK Swift.

## Comprender el flujo de trabajo Braze/APNs

El servicio de notificaciones push de Apple (APN) es la infraestructura para enviar notificaciones push a las aplicaciones que se ejecutan en las plataformas de Apple. Esta es la estructura simplificada de cómo se habilitan las notificaciones push para los dispositivos de tus usuarios y cómo Braze puede enviarles notificaciones push:

1. Configura el certificado push y el perfil de aprovisionamiento
2. Los dispositivos se registran para APN y proporcionan a Braze tokens de notificaciones push
3. Lanza una campaña push de Braze
4. Braze elimina los tokens no válidos

### Paso 1: Configurar el certificado push y el perfil de aprovisionamiento

Al desarrollar tu aplicación, tendrás que crear un certificado SSL para habilitar las notificaciones push. Este certificado se incluirá en el perfil de aprovisionamiento con el que se cree tu aplicación y también deberá cargarse en el panel de Braze. El certificado permite a Braze indicar a los APN que estamos autorizados a enviar notificaciones push en tu nombre.

Hay dos tipos de [perfiles de aprovisionamiento](https://developer.apple.com/library/content/documentation/IDEs/Conceptual/AppDistributionGuide/MaintainingProfiles/MaintainingProfiles.html) y certificados: de desarrollo y de distribución. Recomendamos utilizar sólo perfiles de distribución y certificados para evitar confusiones. Si decides utilizar perfiles y certificados diferentes para el desarrollo y la distribución, asegúrate de que el certificado cargado en el panel coincide con el perfil de aprovisionamiento que utilizas actualmente.

{% alert warning %}
No cambies el entorno del certificado push (desarrollo frente a producción). Cambiar el certificado push a un entorno incorrecto puede hacer que a tus usuarios se les elimine accidentalmente el token de notificaciones push, haciéndoles inaccesibles por push.
{% endalert %}

### Paso 2: Los dispositivos se registran para APN y proporcionan a Braze tokens de notificaciones push

Cuando los usuarios abran tu aplicación, se les pedirá que acepten notificaciones push. Si aceptan esta indicación, los APN generarán un token de notificaciones push para ese dispositivo concreto. El SDK de Swift enviará de forma inmediata y asíncrona el token de notificaciones push para las aplicaciones que utilicen la [política]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/advanced_use_cases/fine_network_traffic_control/#automatic-request-processing) predeterminada [de descarga automática]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/advanced_use_cases/fine_network_traffic_control/#automatic-request-processing). Una vez que tengamos un token de notificaciones push asociado a un usuario, aparecerá como "Registrado push" en el panel de su perfil de usuario, en la pestaña de **interacción**, y será elegible para recibir notificaciones push de las campañas Braze.

{% alert note %}
A partir de macOS 13, en determinados dispositivos, puedes probar las notificaciones push en un simulador de iOS 16 que se ejecute en Xcode 14. Para más detalles, consulta [las Notas de la versión de Xcode 14](https://developer.apple.com/documentation/xcode-release-notes/xcode-14-release-notes).
{% endalert %}

### Paso 3: Lanzamiento de una campaña push Braze

Cuando se lance una campaña push, Braze hará peticiones a los APN para que entreguen tu mensaje. Braze utilizará el certificado SSL push cargado en el panel para autenticar y verificar que se nos permite enviar notificaciones push a los tokens de notificaciones push proporcionados. Si un dispositivo está en línea, la notificación debería recibirse poco después de que se haya enviado la campaña. Ten en cuenta que Braze establece la [fecha de caducidad](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/sending_notification_requests_to_apns#2947607) predeterminada de los APN para las notificaciones en 30 días.

### Paso 4: Eliminar tokens no válidos

Si [APN](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1) nos informa de que alguno de los tokens de notificaciones push a los que intentábamos enviar un mensaje no es válido, eliminamos esos tokens de los perfiles de usuario a los que estaban asociados.

## Utilizar los registros de errores push

El [Registro de actividad de mensajes]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/) te da la oportunidad de ver todos los mensajes (especialmente los de error) asociados a tus campañas y envíos, incluidos los errores de notificación push. Este registro de errores proporciona una serie de advertencias que pueden ser muy útiles para identificar por qué tus campañas no funcionan como esperabas. Si haces clic en un mensaje de error, se te redirigirá a la documentación pertinente para ayudarte a solucionar una incidencia concreta.

![Registros de errores push que muestran la hora en que se produjo el error, el nombre de la aplicación, el canal, el tipo de error y el mensaje de error.]({% image_buster /assets/img_archive/message_activity_log.png %})

Los errores comunes que puedes ver aquí incluyen notificaciones específicas del usuario, como ["Recibido no registrado enviando a token de notificaciones push".](#received-unregistered-sending)

Además, Braze también proporciona un registro de cambios push en el perfil de usuario, en la pestaña de **interacción**. Este registro de cambios proporciona información sobre el comportamiento del registro push, como la invalidación del token, los errores de registro push, los tokens que se mueven a nuevos usuarios, etc.

![]({% image_buster /assets/img_archive/push_changelog.gif %}){: style="max-width:50%;" }

### Errores del registro de actividad de mensajes

#### Se recibió envío no registrado a token de notificaciones push {#received-unregistered-sending}

- Asegúrate de que el token de notificaciones push que se envía a Braze desde el método `AppDelegate.braze?.notifications.register(deviceToken:)` es válido. Puedes mirar en el **Registro de actividad de mensajes** para ver el token de notificaciones push. Debería parecerse a `6e407a9be8d07f0cdeb9e724733a89445f57a89ec890d63867c482a483506fa6`, una cadena larga que contiene una mezcla de letras y números. Si tu token de notificaciones push tiene un aspecto diferente, comprueba tu [código]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#step-4-register-push-tokens-with-braze) para enviar a Braze los tokens de notificaciones push.
- Asegúrate de que tu perfil de aprovisionamiento push coincide con el entorno que estás probando. Los certificados universales pueden configurarse en el panel de Braze para enviarlos al entorno de APN de desarrollo o de producción. Utilizar un certificado de desarrollador para una aplicación de producción o un certificado de producción para una aplicación de desarrollo no funcionará.
 - Comprueba que el token de notificaciones push que has cargado en Braze coincide con el perfil de aprovisionamiento que utilizaste para crear la aplicación desde la que enviaste el token de notificaciones push.

#### Token de dispositivo no para el tema

Este error indica que el certificado push y el ID de paquete de tu aplicación no coinciden. Comprueba que el certificado push que subiste a Braze coincide con el perfil de aprovisionamiento utilizado para crear la aplicación desde la que se envió el token de notificaciones push.

#### BadDeviceToken enviando a token de notificaciones push

El `BadDeviceToken` es un código de error de APNs y no tiene su origen en Braze. Puede haber varias razones para que se devuelva esta respuesta, entre ellas las siguientes:

- La aplicación recibió un token de notificaciones push que no era válido para las credenciales cargadas en el panel.
- Se ha desactivado la función push en este espacio de trabajo.
- El usuario ha optado por no recibir push.
- La aplicación fue desinstalada.
- Apple actualizó el token de notificaciones push, lo que invalidó el token antiguo.
- La aplicación se creó para un entorno de producción, pero las credenciales push cargadas en Braze están configuradas para un entorno de desarrollo (o al revés).

## Problemas de registro push

### No hay aviso de registro push

Si la aplicación no te pide que te registres para recibir notificaciones push, es probable que haya un problema con tu integración de registro push. Asegúrate de que has seguido nuestra [documentación]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/) e integrado correctamente nuestro registro push. También puedes establecer puntos de interrupción en tu código para asegurarte de que el código de registro push se está ejecutando.

### No se muestran los usuarios "registrados push" en el panel (antes de enviar mensajes)

Asegúrate de que tu aplicación está correctamente configurada para permitir notificaciones push. Los puntos de fallo habituales que hay que comprobar incluyen lo siguiente:

- Comprueba que tu aplicación te pide que permitas las notificaciones push. Normalmente, este mensaje aparecerá la primera vez que abras la aplicación, pero puedes programarlo para que aparezca en cualquier otro momento. Si no aparece donde debería, es probable que el problema esté en la configuración básica de las capacidades push de tu aplicación.
  - Comprueba que los pasos para la [integración push]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/) se han completado correctamente.
  - Comprueba que el perfil de aprovisionamiento con el que se creó tu aplicación incluye permisos para push. Asegúrate de que obtienes todos los perfiles de aprovisionamiento disponibles de tu cuenta de desarrollador de Apple. Para confirmarlo, realiza los siguientes pasos:
    1. En Xcode, ve a **Preferencias > Cuentas** (o utiliza el atajo de teclado <kbd>Comando+</kbd><kbd>,</kbd>).
    2. Selecciona el ID de Apple que utilizas para tu cuenta de desarrollador y haz clic en **Ver detalles**.
    3. En la página siguiente, haz clic en **<i class="fas fa-redo-alt"></i> Actualizar** y confirma que estás extrayendo todos los perfiles de aprovisionamiento disponibles.
- Comprueba que has [habilitado correctamente la función push]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#step-2-enable-push-capabilities) en tu aplicación.
- Comprueba que tu perfil de aprovisionamiento push coincide con el entorno en el que estás realizando las pruebas. Los certificados universales pueden configurarse en el panel de Braze para enviarlos al entorno de APN de desarrollo o de producción. Utilizar un certificado de desarrollador para una aplicación de producción o un certificado de producción para una aplicación de desarrollo no funcionará.
- Comprueba que estás llamando a nuestro método `registerPushToken` estableciendo un punto de interrupción en tu código.
- Asegúrate de que estás probando con un dispositivo (push no funcionará en un simulador) y de que tienes una buena conectividad de red.

## Notificaciones push enviadas pero no mostradas en los dispositivos de los usuarios

### Los usuarios "registrados por push" ya no están habilitados después de enviar mensajes

Esto probablemente indica que el usuario tenía un token de notificaciones push no válido. Esto puede ocurrir por varias razones:

#### Desajuste entre el panel y el certificado de la aplicación

Si el certificado push que has cargado en el panel no es el mismo que el del perfil de aprovisionamiento con el que se creó tu aplicación, las APN rechazarán el token. Comprueba que has cargado el certificado correcto y que has completado otra sesión en la aplicación antes de intentar otra notificación de prueba.

#### Se ha desinstalado la aplicación

Si un usuario ha desinstalado tu aplicación, su token de notificaciones push no será válido y se eliminará en el siguiente envío.

#### Regenerar tu perfil de aprovisionamiento

Como último recurso, empezar de cero y crear un perfil de aprovisionamiento completamente nuevo puede eliminar los errores de configuración que se producen al trabajar con varios entornos, perfiles y aplicaciones al mismo tiempo. Hay muchas "partes móviles" en la configuración de las notificaciones push, así que a veces es mejor volver a intentarlo desde el principio. Esto también te ayudará a aislar el problema si necesitas continuar con la solución de problemas.

### Los mensajes no se entregan a los usuarios "registrados push".

#### La aplicación está en primer plano

En las versiones de iOS que no integran push a través del framework `UserNotifications`, si la aplicación está en primer plano cuando se recibe el mensaje push, éste no se mostrará. Debes poner la aplicación en segundo plano en tus dispositivos de prueba antes de enviar mensajes de prueba.

#### Notificación de prueba programada incorrectamente

Comprueba la programación que has establecido para tu mensaje de prueba. Si está configurada como entrega según la zona horaria local o [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/), es posible que aún no hayas recibido el mensaje (o que tuvieras la aplicación en primer plano cuando lo recibiste).

### Usuario no "registrado para push" para la aplicación que se está probando

Comprueba el perfil de usuario del usuario al que intentas enviar un mensaje de prueba. En la pestaña **"Interacción"**, debería haber una lista de "aplicaciones pushables". Comprueba que la aplicación a la que intentas enviar mensajes de prueba está en esta lista. Los usuarios aparecerán como "Registrados push" si tienen un token de notificaciones push para cualquier aplicación de tu espacio de trabajo, por lo que podría tratarse de un falso positivo.

Lo siguiente indicaría un problema con el registro push o que el token de notificaciones push del usuario ha sido devuelto a Braze como no válido por las APN después de haber sido enviado:

![Un perfil de usuario que muestra la configuración de los contactos de un usuario. En Push, aparece "Sin aplicaciones".]({% image_buster /assets/img_archive/registration_problem.png %}){: style="max-width:50%"}

## Los clics push no se registran {#push-clicks-not-logged}

- Asegúrate de haber seguido los [pasos de la integración push]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#step-5-enable-push-handling).
- Braze no gestiona las notificaciones push recibidas silenciosamente en primer plano (comportamiento push predeterminado en primer plano antes del marco `UserNotifications` ). Esto significa que los enlaces no se abrirán y los clics push no se registrarán. Si tu aplicación aún no ha integrado el framework `UserNotifications`, Braze no gestionará las notificaciones push cuando el estado de la aplicación sea `UIApplicationStateActive`. Asegúrate de que tu aplicación no retrasa las llamadas a [los métodos de gestión push]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#step-5-enable-push-handling); de lo contrario, el SDK de Swift puede tratar las notificaciones push como eventos push silenciosos en primer plano y no gestionarlos.

## Los deep links no funcionan

### Los enlaces Web de los clics push no se abren

Los enlaces de las notificaciones push deben ser compatibles con ATS para poder abrirse en vistas web. Asegúrate de que tus enlaces Web utilizan HTTPS. Consulta nuestro artículo sobre [el cumplimiento de la ATS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/advanced_use_cases/linking/#app-transport-security-ats) para obtener más información.

### Los vínculos profundos de los clics push no se abren

La mayor parte del código que gestiona los vínculos en profundidad también gestiona las aperturas push. Primero, asegúrate de que se registran las aperturas push. Si no es así, [soluciona ese problema](#push-clicks-not-logged) (ya que la solución suele arreglar la gestión de enlaces).

Si se registran aperturas, comprueba si se trata de un problema con el vínculo en profundidad en general o con la gestión de los clics push de vinculación en profundidad. Para ello, prueba a ver si funciona un vínculo profundo desde un clic de mensaje dentro de la aplicación.

