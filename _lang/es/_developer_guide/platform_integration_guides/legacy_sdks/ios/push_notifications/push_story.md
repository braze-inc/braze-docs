---
nav_title: Historias push
article_title: Historias push para iOS
platform: iOS
page_order: 27
description: "Este artículo de referencia muestra cómo configurar Historias push para tu aplicación iOS."
channel:
  - push

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Configuración de historias push

La función de historias push requiere el framework `UNNotification` y iOS 10. La función solo está disponible a partir de la versión 3.2.1 del SDK de iOS.

## Paso 1: Habilitar push en tu aplicación

Sigue la [integración de notificaciones push]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/) para habilitar el push en tu aplicación.

## Paso 2: Añadir el objetivo de la extensión de contenido de notificación

En el proyecto de tu aplicación, ve al menú **Archivo > Nuevo > Objetivo...** y añade un nuevo objetivo `Notification Content Extension` y actívalo.

![]({% image_buster /assets/img/ios/push_story/add_content_extension.png %})

Xcode debe generar un nuevo objetivo para usted y crear archivos automáticamente para ti, entre ellos:

{% tabs %}
{% tab OBJETIVO-C %}

- `NotificationViewController.h`
- `NotificationViewController.m`
- `MainInterface.storyboard`

{% endtab %}
{% tab swift %}

- `NotificationViewController.swift`
- `MainInterface.storyboard`

{% endtab %}
{% endtabs %}

## Paso 3: Habilitar capacidades

La característica Historias push requiere el modo de fondo en la sección **Capacidades** del objetivo principal de la aplicación. Después de activar los modos en segundo plano, selecciona **Background fetch** y **Remote notifications**.

![]({% image_buster /assets/img/ios/push_story/enable_background_mode.png %})

### Añadir un grupo de aplicaciones

También hay que añadir `Capability App Groups`. Si no tienes ningún grupo de aplicaciones en tu aplicación, ve a la **Capacidad** del objetivo principal de la aplicación, activa `App Groups`, y haz clic en el botón **+**. Utiliza el ID del paquete de tu aplicación para crear el grupo de aplicaciones. Por ejemplo, si el ID del paquete de tu aplicación es `com.company.appname`, puedes llamar a tu grupo de aplicaciones `group.com.company.appname.xyz`. Debes activar `App Groups` tanto para la aplicación principal como para las extensiones de contenido.

{% alert important %}
`App Groups` en este contexto se refiere al [derecho a grupos de aplicaciones](https://developer.apple.com/documentation/bundleresources/entitlements/com_apple_security_application-groups) de Apple y no a tu ID de espacio de trabajo Braze (antes grupo de aplicaciones).
{% endalert %}

Si no añades tu aplicación a un grupo de aplicaciones, es posible que tu aplicación no rellene determinados campos de la carga útil push y no funcione completamente como se espera.

## Paso 4: Añadir el framework de historias push a tu aplicación

{% tabs local %}
{% tab Swift Package Manager %}

Después de seguir [la guía de integración de Swift Package Manager]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/installation_methods/swift_package_manager/), añade `AppboyPushStory` a tu `Notification Content Extension`:

![En Xcode, en frameworks y librerías, selecciona el ícono "+" para añadir un framework.]({% image_buster /assets/img/ios/push_story/spm1.png %})

![]({% image_buster /assets/img/ios/push_story/spm2.png %})

{% endtab %}
{% tab CocoaPods %}

Añade la siguiente línea a tu archivo de bibliotecas:

```ruby
target 'YourContentExtensionTarget' do
  pod 'Appboy-Push-Story'
end
```

Tras actualizar el archivo de bibliotecas, ve al directorio de tu proyecto de aplicación Xcode dentro de tu terminal y ejecuta `pod install`.

{% endtab %}
{% tab Manual %}

Descarga la última versión de `AppboyPushStory.zip` de la [página de versiones de GitHub](https://github.com/Appboy/appboy-ios-sdk/releases), extráela y añade los siguientes archivos a la página `Notification Content Extension` de tu proyecto:
- `Resources/ABKPageView.nib`
- `AppboyPushStory.xcframework`

![]({% image_buster /assets/img/ios/push_story/manual1.png %})

{% alert important %}
Asegúrate de que la opción **No incrustar** está seleccionada para **AppboyPushStory.xcframework** en la columna **Incrustar**.
{% endalert %}

Añade la bandera `-ObjC` al `Notification Content Extension` de tu proyecto en **Configuración de compilación > Otras banderas del enlazador**.

{% endtab %}
{% endtabs %}

## Paso 5: Actualizar tu controlador de vista de notificación

{% tabs %}
{% tab OBJETIVO-C %}

En tu `NotificationViewController.h`, añade las siguientes líneas para añadir nuevas propiedades e importar los archivos de cabecera:

```objc
#import <AppboyPushStory/AppboyPushStory.h>
```

```objc
@property (nonatomic) IBOutlet ABKStoriesView *storiesView;
@property (nonatomic) ABKStoriesViewDataSource *dataSource;
```

En tu `NotificationViewController.m`, elimina la implementación predeterminada y añade el siguiente código:

```objc
@implementation NotificationViewController

- (void)didReceiveNotification:(UNNotification *)notification {
  self.dataSource = [[ABKStoriesViewDataSource alloc] initWithNotification:notification
                                                               storiesView:self.storiesView
                                                                  appGroup:@"YOUR-APP-GROUP-IDENTIFIER"];
}

- (void)didReceiveNotificationResponse:(UNNotificationResponse *)response
                     completionHandler:(void (^)(UNNotificationContentExtensionResponseOption option))completion {
  UNNotificationContentExtensionResponseOption option = [self.dataSource didReceiveNotificationResponse:response];
  completion(option);
}

- (void)viewWillDisappear:(BOOL)animated {
  [self.dataSource viewWillDisappear];
  [super viewWillDisappear:animated];
}

@end
```

{% endtab %}
{% tab swift %}

En tu `NotificationViewController.swift`, añade la siguiente línea para importar los archivos de cabecera:

```swift
import AppboyPushStory
```

A continuación, elimina la implementación predeterminada y añade el siguiente código:

```swift
class NotificationViewController: UIViewController, UNNotificationContentExtension {

  @IBOutlet weak var storiesView: ABKStoriesView!
  var dataSource: ABKStoriesViewDataSource?
    
  func didReceive(_ notification: UNNotification) {
    dataSource = ABKStoriesViewDataSource(notification: notification, storiesView: storiesView, appGroup: "YOUR-APP-GROUP-IDENTIFIER")
  }
    
  func didReceive(_ response: UNNotificationResponse, completionHandler completion: @escaping (UNNotificationContentExtensionResponseOption) -> Void) {
    if dataSource != nil {
      let option: UNNotificationContentExtensionResponseOption = dataSource!.didReceive(response)
      completion(option)
    }
  }
    
  override func viewWillDisappear(_ animated: Bool) {
    dataSource?.viewWillDisappear()
    super.viewWillDisappear(animated)
  }
}
```

{% endtab %}
{% endtabs %}

## Paso 6: Configura el guión gráfico de la extensión del contenido de la notificación

Abre el guión gráfico de `Notification Content Extension` y coloca un nuevo `UIView` en el controlador de la vista de notificación. Cambia el nombre de la clase a `ABKStoriesView`. Haz que la anchura y la altura de la vista se ajusten automáticamente al marco de la vista principal del controlador de la vista de notificación.

![]({% image_buster /assets/img/ios/push_story/abkstoriesview_class.png %})

![]({% image_buster /assets/img/ios/push_story/abkstoriesview_size.png %})

A continuación, enlaza el IBOutlet `storiesView` del controlador de la vista de notificación con el `ABKStoriesView` añadido.

![]({% image_buster /assets/img/ios/push_story/abkstoriesview_outlet.png %})

## Paso 7: Configura el plist de extensión del contenido de las notificaciones

Abre el archivo `Info.plist` de `Notification Content Extension` y añade y cambia las siguientes claves en `NSExtension \ NSExtensionAttributes`:

`UNNotificationExtensionCategory` = `ab_cat_push_story_v2` ( tipo`String` )
`UNNotificationExtensionDefaultContentHidden` = `YES` ( tipo`Boolean` )
`UNNotificationExtensionInitialContentSizeRatio` = `0.65` ( tipo`Number` )

![]({% image_buster /assets/img/ios/push_story/notificationcontentextension_plist.png %})

## Paso 8: Actualizar la integración de Braze en tu aplicación principal

##### Opción 1: Tiempo de ejecución

En el diccionario `appboyOptions` utilizado para configurar tu instancia de Braze, añade una entrada `ABKPushStoryAppGroupKey` y establece el valor de tu identificador de la API de tu espacio de trabajo.

{% tabs %}
{% tab OBJETIVO-C %}

```objc
NSMutableDictionary *appboyOptions = [NSMutableDictionary dictionary];
appboyOptions[ABKPushStoryAppGroupKey] = @"YOUR-APP-GROUP-IDENTIFIER";
[Appboy startWithApiKey:@"YOUR-API-KEY"
          inApplication:application
      withLaunchOptions:launchOptions
      withAppboyOptions:appboyOptions];
```

{% endtab %}
{% tab swift %}

```swift
let appboyOptions: [AnyHashable: Any] = [
  ABKPushStoryAppGroupKey : "YOUR-APP-GROUP-IDENTIFIER"
]
Appboy.start(withApiKey: "YOUR-API-KEY", in:application, withLaunchOptions:launchOptions, withAppboyOptions:appboyOptions)
```

{% endtab %}
{% endtabs %}

##### Opción 2: Info.plist

Alternativamente, para configurar el espacio de trabajo de historias push desde tu archivo `Info.plist`, añade un diccionario llamado `Braze` a tu archivo `Info.plist`. Dentro del diccionario `Braze`, añade una subentrada de tipo cadena `PushStoryAppGroup` y establece el valor en el identificador de tu espacio de trabajo. Ten en cuenta que, antes de la versión 4.0.2 del SDK de iOS de Braze, debe usarse la clave de diccionario `Appboy` en lugar de `Braze`.

## Próximos pasos

A continuación, consulta los pasos para la integración de [botones de acción]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/customization/action_buttons/), necesaria para que los botones se muestren en un mensaje de historias push.


