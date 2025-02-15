---
nav_title: Android
article_title: Notificaciones push de Android para Unity
platform: 
  - Unity
  - Android
channel: push
page_order: 1
description: "En este artículo de referencia se cubre la integración de las notificaciones push de Android para la plataforma Unity."

---

# Integración de notificaciones push de Android

> En este artículo de referencia se cubre la integración de las notificaciones push de Android para la plataforma Unity.

Estas instrucciones son para integrar push con [Firebase Cloud Messaging (FCM)](https://firebase.google.com/docs/cloud-messaging/).

Consulta nuestra documentación [de Unity ADM]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/push_notifications/adm_push_notifications/) para obtener instrucciones sobre la integración de ADM.

## Paso 1: Habilitar Firebase

Para empezar, sigue la [documentación de configuración de Firebase Unity](https://firebase.google.com/docs/unity/setup).

{% alert note %}
La integración del SDK Unity de Firebase puede hacer que se anule tu `AndroidManifest.xml`. Si eso ocurre, asegúrate de revertirlo al original.
{% endalert %}

## Paso 2: Configura tus credenciales de Firebase

Tienes que introducir tu clave de servidor Firebase y tu ID de remitente en el panel de Braze. Para ello, accede a [la consola de desarrolladores de Firebase](https://console.firebase.google.com/) y selecciona tu proyecto Firebase. A continuación, selecciona **Mensajería en la nube** en **Configuración** y copia la clave del servidor y el ID del remitente:<br>![]({% image_buster /assets/img_archive/finding_firebase_server_key.png %} "FirebaseServerKey")

En Braze, selecciona tu aplicación Android en la página **Configuración de la aplicación**, en **Administrar configuración**. A continuación, introduce tu clave de servidor de Firebase en el campo **Clave de servidor de mensajería en la nube de Firebase** y el ID de remitente de Firebase en el campo ID de **remitente de mensajería en la nube de Firebase**.

![]({% image_buster /assets/img_archive/fcm_api_insert.png %} "FCMKey")

## Paso 3: Implementar la integración push automática

El SDK de Braze puede gestionar automáticamente el registro push con los servidores de mensajería en la nube de Firebase para que los dispositivos reciban notificaciones push.

![El editor de Unity muestra las opciones de configuración de Braze. En este editor, se establecen las opciones "Automatizar integración Unity Android", "Notificación push Firebase Push", "Configuración push Manejar enlaces Push automáticamente", "Configuración push Notificación push Renderizado HTML habilitado" y "Establecer escuchas Push Deleted/Opened/Received". También se proporcionan los campos "ID de remitente de Firebase", "Icono pequeño/grande dibujable", "Color de acento predeterminado de la notificación".]({% image_buster /assets/img/unity/android/unity_android_push_settings_config.png %} "Configuración push de Android")

- **Habilitado el registro automático de mensajería en la nube Firebase**<br> Ordena al SDK de Braze que recupere y envíe automáticamente un token de notificaciones push de FCM para un dispositivo. 
- **ID de remitente de Firebase Cloud Messaging**<br> El ID de remitente de tu consola Firebase.
- **Gestiona los vínculos profundos push automáticamente**<br> Si el SDK debe gestionar la apertura de vínculos profundos o la apertura de la aplicación cuando se hace clic en las notificaciones push.
- **Pequeño icono de notificación Dibujable**<br>El dibujable debe mostrarse como el icono pequeño siempre que se reciba una notificación push. La notificación utilizará el icono de la aplicación como icono pequeño si no se proporciona ningún icono.

## Paso 4: Configurar escuchas push

Si quieres pasar cargas útiles de notificaciones push a Unity o tomar medidas adicionales cuando un usuario recibe una notificación push, Braze proporciona la opción de configurar escuchas de notificaciones push.

En Braze, selecciona tu aplicación Android en la página **Configuración de la aplicación**, en **Administrar configuración**. A continuación, introduce la clave de tu servidor Firebase en el campo **Configuración de notificaciones push** y el ID de remitente de Firebase en el campo ID de **configuración de notificaciones push**.

#### Escucha recibida push

El receptor de notificaciones push se activa cuando un usuario recibe una notificación push. Para enviar la carga útil push a Unity, establece el nombre de tu objeto del juego y el método de devolución de llamada del receptor push en **Establecer receptor push**.

#### Escucha abierta push

El receptor push abierto se activa cuando un usuario inicia la aplicación haciendo clic en una notificación push. Para enviar la carga útil de push a Unity, establece el nombre de tu objeto del juego y el método de devolución de llamada de escucha abierta push en **Establecer escucha abierta push**.

#### Escucha push eliminada (solo Android)

El receptor de notificaciones push eliminadas se activa cuando un usuario elimina o rechaza una notificación push. Para enviar la carga útil de push a Unity, establece el nombre de tu objeto del juego y el método de devolución de llamada de escucha eliminada push en **Establecer escucha eliminada push**.

#### Ejemplo de implementación de un receptor push

En el siguiente ejemplo se implementa el objeto del juego `BrazeCallback` utilizando un nombre de método de devolución de llamada de `PushNotificationReceivedCallback`, `PushNotificationOpenedCallback` y `PushNotificationDeletedCallback` respectivamente.

![Este gráfico de ejemplo de implementación muestra las opciones de configuración de Braze mencionadas en las secciones anteriores y un fragmento de código en C#.]({% image_buster /assets/img/unity/android/unity_android_full_push_listener.png %} "Android Full Listener Example")

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

  void PushNotificationDeletedCallback(string message) {
#if UNITY_ANDROID
    Debug.Log("PushNotificationDeletedCallback message: " + message);
    PushNotification pushNotification = new PushNotification(message);
    Debug.Log("Push Notification dismissed: " + pushNotification);  
#endif
  }
}
```

### Ejemplo de aplicación

El proyecto de muestra del [repositorio del SDK de Unity de Braze](https://github.com/Appboy/appboy-unity-sdk/tree/master/unity-samples) contiene una aplicación de muestra completa que incluye FCM.

## Vinculación en profundidad a los recursos de la aplicación

Aunque Braze puede gestionar vínculos profundos estándar (como URL de sitios web, URI de Android, etc.) de forma predeterminada, la creación de vínculos profundos personalizados requiere una configuración adicional del Manifiesto.

Para obtener información sobre la configuración, visita [Vinculación en profundidad con recursos de la aplicación](https://developer.android.com/training/app-links/deep-linking).

## Añadir iconos de notificación push Braze

Para añadir iconos push a tu proyecto, crea un plug-in Android Archive (AAR) o una biblioteca Android que contenga los archivos de imagen de los iconos. Para conocer los pasos y la información, consulta la documentación de Unity: [Proyectos de bibliotecas Android y plug-ins de archivos Android](https://docs.unity3d.com/Manual/AndroidAARPlugins.html).