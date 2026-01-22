{% multi_lang_include developer_guide/prerequisites/react_native.md %}

## Configuración de las notificaciones push {#setting-up-push-notifications}

### Paso 1: Completa la configuración inicial

{% tabs local %}
{% tab Expo %}
#### Requisitos previos

Antes de poder utilizar Expo para las notificaciones push, tendrás que [configurar el complemento Braze Expo]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/sdk_integration/?tab=expo).

#### Paso 1.1: Actualiza tu archivo `app.json` 

A continuación, actualiza tu archivo `app.json` para Android e iOS:

- **Android:** Añade la opción `enableFirebaseCloudMessaging`.
- **iOS:** Añade la opción `enableBrazeIosPush`.

#### Paso 1.2: Añade tu ID de remitente de Google

Primero, ve a la Consola Firebase, abre tu proyecto y selecciona <i class="fa-solid fa-gear"></i> **Configuración** > **Configuración del proyecto**.

![El proyecto Firebase con el menú "Configuración" abierto.]({% image_buster /assets/img/android/push_integration/set_up_automatic_token_registration/select-project-settings.png %})

Selecciona **Mensajería en la nube** y, a continuación, en **API de mensajería en la nube de Firebase (V1)**, copia el **ID del remitente** en el portapapeles.

![La página "Cloud Messaging" del proyecto Firebase con el "Sender ID" resaltado.]({% image_buster /assets/img/android/push_integration/set_up_automatic_token_registration/copy-sender-id.png %})

A continuación, abre el archivo `app.json` de tu proyecto y establece la propiedad `firebaseCloudMessagingSenderId` en el ID del remitente de tu portapapeles. Por ejemplo:

```
"firebaseCloudMessagingSenderId": "693679403398"
```

#### Paso 1.3: Añade la ruta a tu JSON de Servicios de Google

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

Ten en cuenta que tendrás que utilizar esta configuración en lugar de las instrucciones de configuración nativas si dependes de bibliotecas de notificaciones push adicionales como [Expo Notifications](https://docs.expo.dev/versions/latest/sdk/notifications/).
{% endtab %}

{% tab Android nativo %}
Si no utilizas el complemento Braze Expo, o en su lugar deseas configurar estos ajustes de forma nativa, regístrate para push consultando la [guía de integración push nativa de Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/?tab=android/).
{% endtab %}

{% tab iOS nativo %}
Si no utilizas el complemento Braze Expo, o en su lugar deseas configurar estos ajustes de forma nativa, regístrate para push siguiendo los siguientes pasos de la [guía de integración push nativa de iOS]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift):

#### Paso 1.1: Solicitud de permisos push

Si no tienes previsto solicitar permisos push al iniciar la aplicación, omite la llamada a `requestAuthorizationWithOptions:completionHandler:` en tu AppDelegate. Entonces, pasa al [Paso 2](#reactnative_step-2-request-push-notifications-permission). Si no, sigue la [guía de integración nativa de iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/?tab=objective-c#automatic-push-integration).

#### Paso 1.2 (Opcional): Migra tu clave push

Si antes utilizabas `expo-notifications` para administrar tu clave push, ejecuta `expo fetch:ios:certs` desde la carpeta raíz de tu aplicación. Esto descargará tu clave push (un archivo .p8), que luego podrás cargar en el panel de Braze.
{% endtab %}
{% endtabs %}

### Paso 2: Solicitar permiso para notificaciones push

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

#### Paso 2.1: Escuchar notificaciones push (opcional)

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

##### Campos de evento de notificación push

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
| `is_silent`        | Booleano   | Si `true`, la carga útil se recibe en silencio. Para más detalles sobre el envío de notificaciones push silenciosas en Android, consulta [Notificaciones push silenciosas en Android]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=android). Para más detalles sobre el envío de notificaciones push silenciosas en iOS, consulta [Notificaciones push silenciosas en iOS]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift). |
| `is_braze_internal`| Booleano   | Esto será `true` si se envió una carga útil de notificación para una función interna del SDK, como la sincronización de geovallas, la sincronización de Feature flags o el seguimiento de desinstalación. La carga útil se recibe de forma silenciosa para el usuario. |
| `image_url`        | Cadena    | Especifica la URL asociada a la imagen de notificación. |
| `braze_properties` | Objeto    | Representa las propiedades Braze asociadas a la campaña (pares clave-valor). |
| `ios`              | Objeto    | Representa campos específicos de iOS. |
| `android`          | Objeto    | Representa campos específicos de Android. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Paso 3: Habilitar la vinculación en profundidad (opcional)

Para habilitar Braze para que gestione los vínculos profundos dentro de los componentes React cuando se hace clic en una notificación push, aplica primero los pasos descritos en la biblioteca [React Native Linking](https://reactnative.dev/docs/linking), o con la solución que prefieras. Después, sigue los pasos adicionales que se indican a continuación.

Para saber más sobre qué son los vínculos profundos, consulta nuestro [artículo de Preguntas frecuentes]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#what-is-deep-linking).

{% tabs local %}
{% tab Android nativo %}
Si utilizas el [complemento Braze Expo]({{site.baseurl}}/developer_guide/platforms/react_native/sdk_integration/?tab=expo#step-2-choose-a-setup-option), puedes gestionar automáticamente los vínculos profundos de las notificaciones push configurando `androidHandlePushDeepLinksAutomatically` en `true` en tu `app.json`.

Para gestionar manualmente los vínculos profundos, consulta la documentación nativa de Android: [Añadir vínculos en profundidad]({{site.baseurl}}/developer_guide/push_notifications/deep_linking).

{% endtab %}
{% tab iOS nativo %}
#### Paso 3.1: Almacena la carga útil de la notificación push al iniciar la aplicación
{% alert note %}
Omite el paso 3.1 si utilizas el complemento Braze Expo, ya que esta función se gestiona automáticamente.
{% endalert %}

Para iOS, añade `populateInitialPayloadFromLaunchOptions` al método `didFinishLaunchingWithOptions` de tu AppDelegate. Por ejemplo:

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
  [[BrazeReactUtils sharedInstance] populateInitialPayloadFromLaunchOptions:launchOptions];

  return [super application:application didFinishLaunchingWithOptions:launchOptions];
}
```

#### Paso 3.2: Manejar vínculos profundos desde un estado cerrado

Además de los escenarios básicos gestionados por [React Native Linking](https://reactnative.dev/docs/linking), implementa el método `Braze.getInitialPushPayload` y recupera el valor `url` para tener en cuenta los vínculos en profundidad de las notificaciones push que abren tu aplicación cuando no se está ejecutando. Por ejemplo:

```javascript
// Handles deep links when an iOS app is launched from a hard close via push click.
// This edge case is not handled in the React Native Linking library and is provided as a workaround by Braze.
Braze.getInitialPushPayload(pushPayload => {
  if (pushPayload) {
    console.log('Braze.getInitialPushPayload is ' + pushPayload);
    showToast('Initial URL is ' + pushPayload.url);
    handleOpenUrl({ pushPayload.url });
  }
});
```
{% alert note %}
Braze proporciona esta solución, ya que la API de enlace de React Native no admite este escenario debido a una condición de carrera en el inicio de la aplicación.
{% endalert %}

#### Paso 3.3 Habilitar Enlaces Universales (opcional)

Para habilitar la [vinculación universal]({{site.baseurl}}/developer_guide/push_notifications/deep_linking/?sdktab=swift#universal-links), crea un archivo `BrazeReactDelegate.h` en tu directorio `iOS` y añade el siguiente fragmento de código.

```objc
#import <Foundation/Foundation.h>
#import <BrazeKit/BrazeKit-Swift.h>

@interface BrazeReactDelegate: NSObject<BrazeDelegate>

@end
```

A continuación, crea un archivo `BrazeReactDelegate.m` y añade el siguiente fragmento de código. Sustituye `YOUR_DOMAIN_HOST` por tu dominio real.

```objc
#import "BrazeReactDelegate.h"
#import <UIKit/UIKit.h>

@implementation BrazeReactDelegate

/// This delegate method determines whether to open a given URL.
///
/// Reference the `BRZURLContext` object to get additional details about the URL payload.
- (BOOL)braze:(Braze *)braze shouldOpenURL:(BRZURLContext *)context {
  if ([[context.url.host lowercaseString] isEqualToString:@"YOUR_DOMAIN_HOST"]) {
    // Sample custom handling of universal links
    UIApplication *application = UIApplication.sharedApplication;
    NSUserActivity* userActivity = [[NSUserActivity alloc] initWithActivityType:NSUserActivityTypeBrowsingWeb];
    userActivity.webpageURL = context.url;
    // Routes to the `continueUserActivity` method, which should be handled in your `AppDelegate`.
    [application.delegate application:application
                 continueUserActivity:userActivity restorationHandler:^(NSArray<id<UIUserActivityRestoring>> * _Nullable restorableObjects) {}];
    return NO;
  }
  // Let Braze handle links otherwise
  return YES;
}

@end
```

A continuación, crea y registra tu `BrazeReactDelegate` en `didFinishLaunchingWithOptions` del archivo `AppDelegate.m` de tu proyecto.

```objc
#import "BrazeReactUtils.h"
#import "BrazeReactDelegate.h"

@interface AppDelegate ()

// Keep a strong reference to the BrazeDelegate to ensure it is not deallocated.
@property (nonatomic, strong) BrazeReactDelegate *brazeDelegate;

@end

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions
{
  // Other setup code

  self.brazeDelegate = [[BrazeReactDelegate alloc] init];
  braze.delegate = self.brazeDelegate;
}
```

Para ver un ejemplo de integración, consulta nuestra aplicación de muestra [aquí](https://github.com/braze-inc/braze-react-native-sdk/blob/master/BrazeProject/ios/BrazeProject/AppDelegate.mm).
{% endtab %}
{% endtabs %}

### Paso 4: Enviar una notificación push de prueba

En este punto, deberías poder enviar notificaciones a los dispositivos. Sigue los pasos siguientes para probar tu integración push.

{% alert note %}
A partir de macOS 13, en determinados dispositivos, puedes probar las notificaciones push de iOS en un simulador de iOS 16+ que se ejecute en Xcode 14 o superior. Para más detalles, consulta [las Notas de la versión de Xcode 14](https://developer.apple.com/documentation/xcode-release-notes/xcode-14-release-notes).
{% endalert %}

1. Establece un usuario activo en la aplicación React Native llamando al método `Braze.changeUserId('your-user-id')`.
2. Ve a **Campañas** y crea una nueva campaña de notificación push. Elige las plataformas que deseas probar.
3. Redacta tu notificación de prueba y dirígete a la pestaña **Prueba**. Añade el mismo `user-id` que el usuario de prueba y haz clic en **Enviar prueba**. En breve recibirás la notificación en tu dispositivo.

![Una campaña push de Braze en la que puedes añadir tu propio ID de usuario como destinatario de prueba para probar tu notificación push.]({% image_buster /assets/img/react-native/push-notification-test.png %} "Push Campaign Test")

## Utilizar el plugin Expo

Después de [configurar las notificaciones push para la Expo](#reactnative_setting-up-push-notifications), puedes utilizarla para gestionar los siguientes comportamientos de las notificaciones push, sin necesidad de escribir ningún código en las capas nativas de Android o iOS.

### Reenviar push de Android a FMS adicionales

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

### Utilizar extensiones de aplicación con los Servicios de Aplicación Expo {#app-extensions}

Si utilizas Expo Application Services (EAS) y has habilitado `enableBrazeIosRichPush` o `enableBrazeIosPushStories`, tendrás que declarar los identificadores de paquete correspondientes para cada extensión de aplicación en tu proyecto. Hay varias formas de abordar este paso, dependiendo de cómo esté configurado tu proyecto para gestionar la firma de código con EAS.

Una forma de hacerlo es utilizar la configuración de `appExtensions` en tu archivo `app.json` siguiendo la [documentación sobre extensiones de aplicación](https://docs.expo.dev/build-reference/app-extensions/) de Expo. Alternativamente, puedes configurar la opción `multitarget` en tu archivo `credentials.json` siguiendo la [documentación sobre credenciales locales](https://docs.expo.dev/app-signing/local-credentials/#multi-target-project) de Expo.

### Solución de problemas

Estos son los pasos habituales para la solución de problemas en las integraciones de notificaciones push con el SDK Braze React Native y el plugin Expo.

#### Las notificaciones push han dejado de funcionar {#troubleshooting-stopped-working}

Si las notificaciones push a través del plugin Expo han dejado de funcionar:

1. Comprueba que el SDK de Braze sigue realizando el seguimiento de las sesiones.
2. Comprueba que el SDK no se haya desactivado mediante una llamada explícita o implícita a `wipeData`.
3. Revisa cualquier actualización reciente de Expo o de sus bibliotecas relacionadas, ya que puede haber conflictos con tu configuración de Braze.
4. Revisa las dependencias del proyecto añadidas recientemente y comprueba si anulan manualmente tus métodos existentes de delegado de notificación push.

{% alert tip %}
Para las integraciones de iOS, también puedes consultar nuestro [tutorial de configuración de notificaciones push](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b1-standard-push-notifications) para ayudarte a identificar posibles conflictos con las dependencias de tu proyecto.
{% endalert %}

#### El token del dispositivo no se registra en Braze {#troubleshooting-token-registration}

Si el token de tu dispositivo no se registra en Braze, revisa primero [Las notificaciones push han dejado de funcionar](#troubleshooting-stopped-working).

Si el problema persiste, es posible que haya una dependencia independiente que interfiera con la configuración de las notificaciones push de Braze. Puedes intentar eliminarlo o llamar manualmente a `Braze.registerPushToken` en su lugar.
