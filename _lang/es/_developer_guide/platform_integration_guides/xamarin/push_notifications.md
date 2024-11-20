---
nav_title: Notificaciones push
article_title: Notificaciones push para Xamarin
platform: 
  - Xamarin
  - iOS
  - Android
page_order: 1
description: "En este artículo se cubre la integración de notificaciones push de Android, FireOS e iOS para la plataforma Xamarin."
channel: push
toc_headers: h2
---

# Integración de notificaciones push

> Aprende a configurar las notificaciones push de Android, FireOS e iOS para Xamarin.

## Requisitos previos

Para utilizar esta característica, tendrás que [integrar Braze SDK para la plataforma Xamarin]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/initial_sdk_setup/).

## Integración de notificaciones push

{% tabs %}
{% tab Android %}
{% alert tip %}
Para ver cómo cambian los espacios de nombres entre Java y C#, consulta nuestra [aplicación de ejemplo Xample en GitHub](https://github.com/braze-inc/braze-xamarin-sdk/tree/master/appboy-component/samples/android-net-maui/BrazeAndroidMauiSampleApp/BrazeAndroidMauiSampleApp).
{% endalert %}

Para integrar las notificaciones push para Xamarin, tendrás que completar los pasos para las notificaciones push nativas de Android. Los pasos siguientes son sólo un resumen. Para una guía completa, consulta la [guía de notificaciones push nativas]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/).

### Paso 1: Actualiza tu proyecto

1. Añade Firebase a tu proyecto Android.
2. Añade la biblioteca de Mensajería en la nube a la página `build.gradle` de tu proyecto Android:
  ```gradle
  implementation "google.firebase:firebase-messaging:+"
  ```

### Paso 2: Crea tus credenciales JSON

1. En Google Cloud, habilita la [API de Firebase Cloud Messaging](https://console.cloud.google.com/apis/library/fcm.googleapis.com).
2. Selecciona **Cuentas de servicio** > tu proyecto > **Crear cuenta de servicio**, e introduce un nombre de cuenta de servicio, un ID y una descripción. Cuando hayas terminado, selecciona **Crear y continuar**.
3. En el campo **Rol**, busca y selecciona **Administrador de la API de mensajería en la nube de Firebase** en la lista de roles.
4. En **Cuentas de servicio**, elige tu proyecto y selecciona <i class="fa-solid fa-ellipsis-vertical"></i> **Acciones** > **Gestionar claves** > **Añadir clave** > **Crear nueva clave**. Elige **JSON** y selecciona **Crear**.

### Paso 3: Sube tus credenciales JSON

1. En Braze, selecciona <i class="fa-solid fa-gear"></i> **Configuración** > Configuración de la aplicación **.** En la **configuración de notificaciones push** de tu aplicación Android, elige **Firebase**, luego selecciona **Cargar archivo JSON** y carga las credenciales que generaste anteriormente. Cuando hayas terminado, selecciona **Guardar**.
2. Habilita el registro automático del token FCM, accediendo a la Consola Firebase. Abre tu proyecto y selecciona <i class="fa-solid fa-gear"></i> **Configuración** > **Configuración del proyecto**. Selecciona **Mensajería en la nube** y, a continuación, en **API de mensajería en la nube de Firebase (V1)**, copia el número en el campo **ID del remitente**.
3. En tu proyecto de Android Studio agrega lo siguiente a tu `braze.xml`.

  ```xml
  <bool translatable="false" name="com_braze_firebase_cloud_messaging_registration_enabled">true</bool>
  <string translatable="false" name="com_braze_firebase_cloud_messaging_sender_id">FIREBASE_SENDER_ID</string>
  ```

{% alert important %}
Para evitar que Braze desencadene solicitudes de red innecesarias cada vez que envíes notificaciones push silenciosas, elimina cualquier solicitud de red automática configurada en el método `onCreate()` de tu clase `Application`. Para más información, consulta [Referencia para desarrolladores de Android: Aplicación](https://developer.android.com/reference/android/app/Application).
{% endalert %}
{% endtab %}

{% tab ios %}
### Paso 1: Completa la configuración inicial

Consulta [las instrucciones de integración de Swift]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration) para obtener información sobre la configuración de tu aplicación con push y el almacenamiento de tus credenciales en nuestro servidor. Consulta la aplicación de ejemplo [MAUI de iOS](https://github.com/braze-inc/braze-xamarin-sdk/tree/master/appboy-component/samples/ios-net-maui/BrazeiOSMauiSampleApp) para más detalles.

### Paso 2: Solicitar permiso para notificaciones push

Nuestro SDK de Xamarin ahora admite la configuración push automática. Configura la automatización push y los permisos añadiendo el siguiente código a la configuración de tu instancia de Braze:

```csharp
configuration.Push.Automation = new BRZConfigurationPushAutomation(true);
configuration.Push.Automation.RequestAuthorizationAtLaunch = false;
```

Consulta la aplicación de ejemplo [MAUI de iOS](https://github.com/braze-inc/braze-xamarin-sdk/tree/master/appboy-component/samples/ios-net-maui/BrazeiOSMauiSampleApp) para más detalles. Para obtener más información, consulta la documentación de Xamarin sobre [Notificaciones de usuario mejoradas en Xamarin.iOS](https://learn.microsoft.com/en-us/previous-versions/xamarin/ios/platform/user-notifications/enhanced-user-notifications?tabs=macos).
{% endtab %}
{% endtabs %}
