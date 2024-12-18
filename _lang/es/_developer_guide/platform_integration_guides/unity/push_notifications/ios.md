---
nav_title: iOS
article_title: Notificaciones push para Unity
platform:
  - Unity
  - iOS
channel: push
ex_push_payload: archive/apple/push_payload.json
page_order: 1
description: "En este artículo de referencia se cubre la integración de notificaciones push de iOS para la plataforma Unity."

---

# Integración de notificaciones push de iOS

> En este artículo de referencia se cubre la integración de notificaciones push de iOS para la plataforma Unity.

## Paso 1: Elige integración push automática o manual

Braze proporciona una solución nativa de Unity para automatizar las integraciones push de iOS.

- Si prefieres completar la integración manualmente modificando tu proyecto Xcode creado, sigue nuestras [instrucciones nativas de push para iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/).
- Si estás pasando de una integración manual a una automatizada, sigue las instrucciones de [Transición a una integración automatizada]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/sdk_integration/ios/#transitioning-from-manual-to-automated-integration-ios).
- Nuestra solución de notificación push automática aprovecha la característica de Autorización Provisional de iOS 12 y no se puede utilizar con la ventana emergente de notificación push nativa.

## Paso 2: Implementar la integración push automática

### Configurar notificaciones push

Sigue nuestra [documentación de configuración de notificaciones push de iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/) para configurar Braze mediante un archivo `.p8`.

### Habilitar la integración push automática

Abre los ajustes de configuración de Braze en el editor de Unity navegando hasta **Braze > Configuración de Braze**.

Marca **Integrar Push con Braze** para registrar automáticamente usuarios para notificaciones push, pasar tokens de notificaciones push a Braze, hacer un seguimiento de los análisis de aperturas push y aprovechar nuestra gestión predeterminada de notificaciones push.

### Habilitar push en segundo plano (opcional)

Marca **Activar Push en segundo plano** si quieres habilitar `background mode` para las notificaciones push. Esto permite al sistema despertar tu aplicación del estado `suspended` cuando llega una notificación push, habilitando tu aplicación para descargar contenido en respuesta a las notificaciones push. Marcar esta opción es necesario para nuestra funcionalidad de seguimiento de la desinstalación.

![El editor de Unity muestra las opciones de configuración de Braze. En este editor están habilitadas las opciones "Automatización de la integración de Unity con iOS", "Integración de push con Braze" y "Habilitación de push en segundo plano".]({% image_buster /assets/img/unity/ios/unity_ios_enable_background.png %})

### Desactivar el registro automático (opcional)

Los usuarios que aún no hayan optado por la adhesión voluntaria a las notificaciones push serán autorizados automáticamente a recibir notificaciones push al abrir tu aplicación. Para desactivar esta característica y registrar manualmente a los usuarios para push, marca **Desactivar registro push automático**.

- Si la opción **Desactivar autorización provisional** no está marcada en iOS 12 o posterior, el usuario estará autorizado provisionalmente (de forma silenciosa) a recibir push silenciosos. Si está marcada, se mostrará al usuario el aviso push nativo.
- Si necesitas configurar exactamente cuándo se muestra el aviso en tiempo de ejecución, desactiva el registro automático desde el editor de configuración de Braze y utiliza en su lugar `AppboyBinding.PromptUserForPushPermissions()`.

![El editor de Unity muestra las opciones de configuración de Braze. En este editor están habilitadas las opciones "Automatizar la integración de Unity en iOS", "integrar push con Braze" y "desactivar el registro push automático".]({% image_buster /assets/img/unity/ios/unity_ios_disable_auto_push.png %})

## Paso 3: Configurar escuchas push

Si quieres pasar cargas útiles de notificaciones push a Unity o tomar medidas adicionales cuando un usuario recibe una notificación push, Braze proporciona la opción de configurar escuchas de notificaciones push.

### Escucha recibida push

El receptor de notificaciones push se activa cuando un usuario recibe una notificación push mientras utiliza activamente la aplicación (por ejemplo, cuando la aplicación está en primer plano). Configura la escucha push recibida en el editor de configuración de Braze. Si necesitas configurar la escucha de tu objeto del juego en tiempo de ejecución, utiliza `AppboyBinding.ConfigureListener()` y especifica `BrazeUnityMessageType.PUSH_RECEIVED`.

![El editor de Unity muestra las opciones de configuración de Braze. En este editor, se amplía la opción "Establecer receptor de recepción push" y se proporcionan el "Nombre del objeto del juego" (AppBoyCallback) y el "Nombre del método de devolución de llamada" (PushNotificationReceivedCallback).]({% image_buster /assets/img/unity/ios/unity_ios_push_received.png %})

### Escucha abierta push

El receptor push abierto se activa cuando un usuario inicia la aplicación haciendo clic en una notificación push. Para enviar la carga útil de push a Unity, establece el nombre de tu objeto del juego y el método de devolución de llamada de la escucha push abierta en la opción **Establecer escucha push abierta**:

![El editor de Unity muestra las opciones de configuración de Braze. En este editor, se amplía la opción "Establecer receptor de recepción push" y se proporcionan el "Nombre del objeto del juego" (AppBoyCallback) y el "Nombre del método de devolución de llamada" (PushNotificationOpenedCallback).]({% image_buster /assets/img/unity/ios/unity_ios_push_opened.png %})

Si necesitas configurar la escucha de tu objeto del juego en tiempo de ejecución, utiliza `AppboyBinding.ConfigureListener()` y especifica `BrazeUnityMessageType.PUSH_OPENED`.

### Ejemplo de implementación de un receptor push

El siguiente ejemplo implementa el objeto del juego `AppboyCallback` utilizando un nombre de método de devolución de llamada de `PushNotificationReceivedCallback` y `PushNotificationOpenedCallback`, respectivamente.

![Este gráfico de ejemplo de implementación muestra las opciones de configuración de Braze mencionadas en las secciones anteriores y un fragmento de código en C#.]({% image_buster /assets/img/unity/ios/unity_ios_appboy_callback.png %})

```csharp
public class MainMenu : MonoBehaviour {
  void PushNotificationReceivedCallback(string message) {
#if UNITY_ANDROID
    Debug.Log("PushNotificationReceivedCallback message: " + message);
    PushNotification pushNotification = new PushNotification(message);
    Debug.Log("Push Notification received: " + pushNotification);   
#elif UNITY_IOS
    ApplePushNotification pushNotification = new ApplePushNotification(message);
    Debug.Log("Push received Notification event: " + pushNotification);   
#endif  
  }

  void PushNotificationOpenedCallback(string message) {
#if UNITY_ANDROID
    Debug.Log("PushNotificationOpenedCallback message: " + message);
    PushNotification pushNotification = new PushNotification(message);
    Debug.Log("Push Notification opened: " + pushNotification);  
#elif UNITY_IOS
    ApplePushNotification pushNotification = new ApplePushNotification(message);
    Debug.Log("Push opened Notification event: " + pushNotification);   
#endif  
  }
}
```

## Características avanzadas

### Devolución de llamada de token de notificaciones push

Para recibir una copia de los tokens de dispositivo Braze del SO, establece un delegado mediante `AppboyBinding.SetPushTokenReceivedFromSystemDelegate()`.

### Otras características

Para implementar características avanzadas como vínculos profundos, recuento de señales y sonidos personalizados, visita nuestras [instrucciones push nativas de iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/).

