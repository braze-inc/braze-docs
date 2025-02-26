---
nav_title: Notificaciones push
article_title: Notificaciones push para React Native
platform: React Native
page_order: 2
toc_headers: h2
description: "Este artículo trata sobre la implementación de notificaciones push en React Native."
channel: push

---

# Integración de notificaciones push

> Este artículo de referencia explica cómo configurar las notificaciones push para React Native. La integración de las notificaciones push requiere configurar cada plataforma nativa por separado. Sigue las respectivas guías indicadas para finalizar la instalación.

## Paso 1: Completa la configuración inicial

{% tabs %}
{% tab Expo %}
Configura las opciones `enableBrazeIosPush` y `enableFirebaseCloudMessaging` en tu archivo `app.json` para habilitar la función push para iOS y Android, respectivamente. Consulta las instrucciones de configuración [aquí]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/react_sdk_setup/#step-2-complete-native-setup) para más detalles.

Ten en cuenta que tendrás que utilizar esta configuración en lugar de las instrucciones de configuración nativas si dependes de bibliotecas de notificaciones push adicionales como [Expo Notifications](https://docs.expo.dev/versions/latest/sdk/notifications/).
{% endtab %}

{% tab Android %}
### Paso 1.1: Registro para push

Regístrate para recibir mensajes push mediante la API Firebase Cloud Messaging (FCM) de Google. Para una guía completa, consulta los siguientes pasos de la [guía de integración push para Android nativo]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/):

1. [Añade Firebase a tu proyecto]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-1-add-firebase-to-your-project).
2. [Añade Cloud Messaging a tus dependencias]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-2-add-cloud-messaging-to-your-dependencies).
3. [Crea una cuenta de servicio]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-3-create-a-service-account).
4. [Generar credenciales JSON]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-4-generate-json-credentials).
5. [Carga tus credenciales JSON en Braze]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-5-upload-your-json-credentials-to-braze).

### Paso 1.2: Añade tu ID de remitente de Google

Primero, ve a la Consola Firebase, abre tu proyecto y selecciona <i class="fa-solid fa-gear"></i> **Configuración** > **Configuración del proyecto**.

![El proyecto Firebase con el menú "Configuración" abierto.]({% image_buster /assets/img/android/push_integration/set_up_automatic_token_registration/select-project-settings.png %})

Selecciona **Mensajería en la nube** y, a continuación, en **API de mensajería en la nube de Firebase (V1)**, copia el **ID del remitente** en el portapapeles.

![La página "Cloud Messaging" del proyecto Firebase con el "Sender ID" resaltado.]({% image_buster /assets/img/android/push_integration/set_up_automatic_token_registration/copy-sender-id.png %})

A continuación, abre el archivo `app.json` de tu proyecto y establece la propiedad `firebaseCloudMessagingSenderId` en el ID del remitente de tu portapapeles. Por ejemplo:

```
"firebaseCloudMessagingSenderId": "693679403398"
```

### Paso 1.3: Añade la ruta a tu JSON de Servicios de Google

En el archivo `app.json` de tu proyecto, añade la ruta a tu archivo `google-services.json`. Este archivo es necesario para establecer `enableFirebaseCloudMessaging: true` en tu configuración.

```json
{
  "expo": {
    "android": {
      "googleServicesFile": "PATH_TO_GOOGLE_SERVICES"
    },
    "plugins": [
      [
        "@braze/expo-plugin",
        {
          "androidApiKey": "YOUR-ANDROID-API-KEY",
          "iosApiKey": "YOUR-IOS-API-KEY",
          "enableBrazeIosPush": true,
          "enableFirebaseCloudMessaging": true,
          "firebaseCloudMessagingSenderId": "YOUR-FCM-SENDER-ID",
          "androidHandlePushDeepLinksAutomatically": true
        }
      ],
    ]
  }
}
```
{% endtab %}

{% tab iOS %}
### Paso 1.1: Cargar certificados APN

Genera un certificado del servicio de notificaciones push de Apple (APN) y cárgalo en el panel de Braze. Para más información, consulta [Cargar tu certificado de APN]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#step-1-upload-your-apns-certificate).

### Paso 1.2: Elige un método de integración

Si no tienes previsto solicitar permisos push al lanzar la aplicación, omite la llamada a `requestAuthorizationWithOptions:completionHandler:` en tu AppDelegate, y salta al [Paso 2](#step-2-request-push-notifications-permission). Si no, sigue la [guía de integración nativa de iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/?tab=objective-c#automatic-push-integration).

Cuando hayas terminado, continúa con [el Paso 1.3](#step-13-migrate-your-push-key).

### Paso 1.3: Migra tu clave push

Si antes utilizabas `expo-notifications` para administrar tu clave push, ejecuta `expo fetch:ios:certs` desde la carpeta raíz de tu aplicación. Esto descargará tu clave push (un archivo .p8), que luego podrás cargar en el panel de Braze.
{% endtab %}
{% endtabs %}

## Paso 2: Solicitar permiso para notificaciones push

Utiliza el método `Braze.requestPushPermission()` (disponible a partir de la v1.38.0) para solicitar permiso para notificaciones push al usuario en iOS y Android 13+. Para Android 12 e inferiores, este método no funciona.

Este método recibe un parámetro obligatorio que especifica qué permisos debe solicitar el SDK al usuario en iOS. Estas opciones no tienen efecto en Android.

```javascript
const permissionOptions = {
  alert: true,
  sound: true,
  badge: true,
  provisional: false
};

Braze.requestPushPermission(permissionOptions);
```

### Paso 2.1: Escuchar notificaciones push (opcional)

Además, puedes suscribirte a eventos en los que Braze haya detectado y gestionado una notificación push entrante. Utiliza la tecla de escucha `Braze.Events.PUSH_NOTIFICATION_EVENT`.

{% alert important %}
Los eventos push recibidos de iOS sólo se desencadenarán para las notificaciones en primer plano y `content-available` para las notificaciones en segundo plano. No se desencadenará para las notificaciones recibidas mientras están terminadas ni para las notificaciones en segundo plano sin el campo `content-available`.
{% endalert %}

```javascript
Braze.addListener(Braze.Events.PUSH_NOTIFICATION_EVENT, data => {
  console.log(`Push Notification event of type ${data.payload_type} seen. Title ${data.title}\n and deeplink ${data.url}`);
  console.log(JSON.stringify(data, undefined, 2));
});
```

#### Campos de evento de notificación push

Para obtener una lista completa de los campos de notificación push, consulta la tabla siguiente:

| Nombre del campo         | Tipo      | Descripción |
| ------------------ | --------- | ----------- |
| `payload_type`     | Cadena    | Especifica el tipo de carga útil de la notificación. Los dos valores que se envían desde el SDK de React Native de Braze son `push_opened` y `push_received`. |
| `url`              | Cadena    | Especifica la URL abierta por la notificación. |
| `use_webview`      | Booleano   | Si `true`, la URL se abrirá en la aplicación en una vista web modal. Si `false`, la URL se abrirá en el navegador del dispositivo. |
| `title`            | Cadena    | Representa el título de la notificación. |
| `body`             | Cadena    | Representa el cuerpo o texto del contenido de la notificación. |
| `summary_text`     | Cadena    | Representa el texto resumido de la notificación. Está mapeado desde `subtitle` en iOS. |
| `badge_count`      | Número   | Representa el recuento de señales de la notificación. |
| `timestamp`        | Número | Representa la hora a la que la aplicación recibió la carga útil. |
| `is_silent`        | Booleano   | Si `true`, la carga útil se recibe en silencio. Para más detalles sobre el envío de notificaciones push silenciosas en Android, consulta [Notificaciones push silenciosas en Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/silent_push_notifications). Para más detalles sobre el envío de notificaciones push silenciosas en iOS, consulta [Notificaciones push silenciosas en iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/silent_push_notifications/). |
| `is_braze_internal`| Booleano   | Esto será `true` si se envió una carga útil de notificación para una función interna del SDK, como la sincronización de geovallas, la sincronización de Feature flags o el seguimiento de desinstalación. La carga útil se recibe de forma silenciosa para el usuario. |
| `image_url`        | Cadena    | Especifica la URL asociada a la imagen de notificación. |
| `braze_properties` | Objeto    | Representa las propiedades Braze asociadas a la campaña (pares clave-valor). |
| `ios`              | Objeto    | Representa campos específicos de iOS. |
| `android`          | Objeto    | Representa campos específicos de Android. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Paso 3: Habilitar la vinculación en profundidad (opcional)

Para habilitar Braze para que gestione los vínculos profundos dentro de los componentes React cuando se hace clic en una notificación push, sigue los pasos adicionales.

{% tabs %}
{% tab Expo %}
Nuestra [aplicación de muestra BrazeProject](https://github.com/braze-inc/braze-react-native-sdk/tree/master/BrazeProject) contiene un ejemplo completo de vínculos en profundidad implementados. Para saber más sobre qué son los vínculos profundos, consulta nuestro [artículo de Preguntas frecuentes]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#what-is-deep-linking).

{% endtab %}
{% tab Android %}
Para Android, la configuración de los vínculos profundos es idéntica a la [configuración de los vínculos profundos en las aplicaciones nativas de Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration#step-4-add-deep-links). Si quieres que el SDK de Braze gestione automáticamente los vínculos profundos push, configura `androidHandlePushDeepLinksAutomatically: true` en tu `app.json`.

{% endtab %}
{% tab iOS %}
### Paso 3.1: Añade capacidades de vinculación en profundidad

Para iOS, añade `populateInitialUrlFromLaunchOptions` al método `didFinishLaunchingWithOptions` de tu AppDelegate. Por ejemplo:

```objc
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions
{
  self.moduleName = @"BrazeProject";
  self.initialProps = @{};

  BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:apiKey endpoint:endpoint];
  configuration.triggerMinimumTimeInterval = 1;
  configuration.logger.level = BRZLoggerLevelInfo;
  Braze *braze = [BrazeReactBridge initBraze:configuration];
  AppDelegate.braze = braze;

  [self registerForPushNotifications];
  [[BrazeReactUtils sharedInstance] populateInitialUrlFromLaunchOptions:launchOptions];

  return [super application:application didFinishLaunchingWithOptions:launchOptions];
}
```

### Paso 3.2: Configurar la gestión de los vínculos profundos

Utiliza el método `Linking.getInitialURL()` para los vínculos profundos que abren tu aplicación, y el método `Braze.getInitialURL` para los vínculos profundos dentro de las notificaciones push que abren tu aplicación cuando no se está ejecutando. Por ejemplo:

```javascript
Linking.getInitialURL()
  .then(url => {
    if (url) {
      console.log('Linking.getInitialURL is ' + url);
      showToast('Linking.getInitialURL is ' + url);
      handleOpenUrl({ url });
    }
  })
  .catch(err => console.error('Error getting initial URL', err));

// Handles deep links when an iOS app is launched from a hard close via push click.
Braze.getInitialURL(url => {
  if (url) {
    console.log('Braze.getInitialURL is ' + url);
    showToast('Braze.getInitialURL is ' + url);
    handleOpenUrl({ url });
  }
});
```
{% alert note %}
Braze proporciona esta solución, ya que la API de enlace de React Native no admite este escenario debido a una condición de carrera en el inicio de la aplicación.
{% endalert %}
{% endtab %}
{% endtabs %}

## Paso 4: Prueba de visualización de notificaciones push

En este punto, deberías poder enviar notificaciones a los dispositivos. Sigue los pasos siguientes para probar tu integración push.

{% alert note %}
A partir de macOS 13, en determinados dispositivos, puedes probar las notificaciones push de iOS en un simulador de iOS 16+ que se ejecute en Xcode 14 o superior. Para más detalles, consulta [las Notas de la versión de Xcode 14](https://developer.apple.com/documentation/xcode-release-notes/xcode-14-release-notes).
{% endalert %}

1. Establece un usuario activo en la aplicación React llamando al método `Braze.changeUserId('your-user-id')`.
2. Ve a **Campañas** y crea una nueva campaña de notificación push. Elige las plataformas que deseas probar.
3. Redacta tu notificación de prueba y dirígete a la pestaña **Prueba**. Añade el mismo `user-id` que el usuario de prueba y haz clic en **Enviar prueba**. En breve recibirás la notificación en tu dispositivo.

![Una campaña push de Braze en la que puedes añadir tu propio ID de usuario como destinatario de prueba para probar tu notificación push.]({% image_buster /assets/img/react-native/push-notification-test.png %} "Push Campaign Test")

## Reenviar push de Android a FMS adicionales

Si quieres utilizar un servicio de mensajería Firebase (FMS) adicional, puedes especificar un FMS alternativo al que llamar si tu aplicación recibe un push que no procede de Braze. Por ejemplo:

```json
{
  "expo": {
    "plugins": [
      [
        "@braze/expo-plugin",
        {
          ...
          "androidFirebaseMessagingFallbackServiceEnabled": true,
          "androidFirebaseMessagingFallbackServiceClasspath": "com.company.OurFirebaseMessagingService"
        }
      ]
    ]
  }
}
```

## Configurar extensiones de aplicación con Expo

### Habilitar las notificaciones push enriquecidas para iOS

{% alert tip %}
Las notificaciones push enriquecidas están disponibles para Android de forma predeterminada.
{% endalert %}

Para habilitar las notificaciones push enriquecidas en iOS mediante Expo, configura la propiedad `enableBrazeIosRichPush` en `true` en tu objeto `expo.plugins` en `app.json`:

```json
{
  "expo": {
    "plugins": [
      [
        "@braze/expo-plugin",
        {
          ...
          "enableBrazeIosRichPush": true
        }
      ]
    ]
  }
}
```

Por último, añade el identificador de paquete de esta extensión de aplicación a la configuración de credenciales de tu proyecto: `<your-app-bundle-id>.BrazeExpoRichPush`. Para más detalles sobre este proceso, consulta [Utilizar extensiones de aplicación con los Servicios de Aplicación Expo](#app-extensions).

### Habilitación de historias push para iOS

{% alert tip %}
Las historias push están disponibles para Android de forma predeterminada.
{% endalert %}

Para habilitar las historias push en iOS mediante Expo, asegúrate de que tienes un grupo de aplicaciones definido para tu aplicación. Para más información, consulta [Añadir un grupo de aplicaciones]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/push_story/#adding-an-app-group).

A continuación, configura la propiedad `enableBrazeIosPushStories` en `true` y asigna el ID de tu grupo de aplicaciones a `iosPushStoryAppGroup` en tu objeto `expo.plugins` en `app.json`:

```json
{
  "expo": {
    "plugins": [
      [
        "@braze/expo-plugin",
        {
          ...
          "enableBrazeIosPushStories": true,
          "iosPushStoryAppGroup": "group.com.company.myApp.PushStories"
        }
      ]
    ]
  }
}
```

Por último, añade el identificador de paquete de esta extensión de aplicación a la configuración de credenciales de tu proyecto: `<your-app-bundle-id>.BrazeExpoPushStories`. Para más detalles sobre este proceso, consulta [Utilizar extensiones de aplicación con los Servicios de Aplicación Expo](#app-extensions).

{% alert warning %}
Si utilizas historias push con los servicios de aplicaciones Expo, asegúrate de utilizar la bandera `EXPO_NO_CAPABILITY_SYNC=1` al ejecutar `eas build`. Hay un problema conocido en la línea de comandos que elimina la capacidad de Grupos de aplicaciones del perfil de aprovisionamiento de tu extensión.
{% endalert %}

### Utilizar extensiones de aplicación con los Servicios de Aplicación Expo {#app-extensions}

Si utilizas Expo Application Services (EAS) y has habilitado `enableBrazeIosRichPush` o `enableBrazeIosPushStories`, tendrás que declarar los identificadores de paquete correspondientes para cada extensión de aplicación en tu proyecto. Hay varias formas de abordar este paso, dependiendo de cómo esté configurado tu proyecto para gestionar la firma de código con EAS.

Una forma de hacerlo es utilizar la configuración de `appExtensions` en tu archivo `app.json` siguiendo la [documentación sobre extensiones de aplicación](https://docs.expo.dev/build-reference/app-extensions/) de Expo. Alternativamente, puedes configurar la opción `multitarget` en tu archivo `credentials.json` siguiendo la [documentación sobre credenciales locales](https://docs.expo.dev/app-signing/local-credentials/#multi-target-project) de Expo.

