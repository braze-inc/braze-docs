---
nav_title: "Push Primer"
article_title: Push Primer para iOS
page_order: 6
page_type: reference
description: "Este artículo de referencia trata de cómo integrar los push primers de iOS."
platform: iOS
channel:
  - push
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Integración de push primers

Las campañas push primer animan a tus usuarios a habilitar la función push en su dispositivo para tu aplicación. Obtener el permiso de los usuarios para enviar mensajes directamente a sus dispositivos puede ser complejo, ¡pero nuestras guías pueden ayudarte! Esta guía muestra los pasos que deben dar los desarrolladores para integrar el push priming.

## Paso 1: Añade un fragmento de código en el archivo AppDelegate.m

Añade la siguiente línea de código a tu archivo `AppDelegate.m` en lugar de la integración estándar:

{% tabs %}
{% tab OBJETIVO-C %}

```objc
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
...
if (@available(iOS 10.0, *)) {
    UNUserNotificationCenter *center = [UNUserNotificationCenter currentNotificationCenter];
    [center getNotificationSettingsWithCompletionHandler:^(UNNotificationSettings * _Nonnull settings) {
      if (settings.authorizationStatus != UNAuthorizationStatusNotDetermined) {
        // authorization has already been requested, need to follow usual steps
        [center requestAuthorizationWithOptions:(UNAuthorizationOptionAlert | UNAuthorizationOptionSound | UNAuthorizationOptionBadge) completionHandler:^(BOOL granted, NSError * _Nullable error) {
          [[Appboy sharedInstance] pushAuthorizationFromUserNotificationCenter:granted];
        }];
        center.delegate = self;
        [center setNotificationCategories:[ABKPushUtils getAppboyUNNotificationCategorySet]];
        [[UIApplication sharedApplication] registerForRemoteNotifications];
      }
    }];
  } else {
    UIApplication *sharedApplication = [UIApplication sharedApplication];
    UIUserNotificationSettings *notificationSettings = [sharedApplication currentUserNotificationSettings];
    if (notificationSettings.types) {
      UIUserNotificationSettings *settings = [UIUserNotificationSettings settingsForTypes:(UIUserNotificationTypeBadge | UIUserNotificationTypeAlert | UIUserNotificationTypeSound) categories:[ABKPushUtils getAppboyUIUserNotificationCategorySet]];
      [sharedApplication registerUserNotificationSettings:settings];
      [sharedApplication registerForRemoteNotifications];
    }
  }
```
{% endtab %}
{% tab swift %}

```swift
if #available(iOS 10, *) {
  let center = UNUserNotificationCenter.current()
  center.getNotificationSettings(completionHandler: { (settings) in
    if settings.authorizationStatus != .notDetermined {
      // authorization has already been requested, need to follow usual steps
      center.requestAuthorization(options: [.alert, .sound, .badge]) { (granted, error) in
      Appboy.sharedInstance()?.pushAuthorization(fromUserNotificationCenter: granted)
      }
      center.delegate = self as? UNUserNotificationCenterDelegate
      center.setNotificationCategories(ABKPushUtils.getAppboyUNNotificationCategorySet())
      UIApplication.shared.registerForRemoteNotifications()
    }
  })
} else {
  let notificationSettiings = UIApplication.shared.currentUserNotificationSettings
  if notificationSettiings?.types != nil {
    let setting = UIUserNotificationSettings(types: [.alert, .badge, .sound], categories:nil)
    UIApplication.shared.registerUserNotificationSettings(setting)
    UIApplication.shared.registerForRemoteNotifications()
  }
}
```
{% endtab %}
{% endtabs %}

## Paso 2: Añade un verificador de eventos personalizado al archivo AppDelegate.m 

El siguiente fragmento de código comprueba si es necesario lanzar un evento personalizado. Añade la siguiente línea de código a tu `AppDelegate.m`.

{% tabs %}
{% tab OBJETIVO-C %}
```objc
if (@available(iOS 10.0, *)) {
    UNUserNotificationCenter *center = [UNUserNotificationCenter currentNotificationCenter];
    [center getNotificationSettingsWithCompletionHandler:^(UNNotificationSettings * _Nonnull settings) {
      if (settings.authorizationStatus == UNAuthorizationStatusNotDetermined) {
        // ...
        // fire custom event
        // ...
      }
    }];
  } else {
    UIUserNotificationSettings *notificationSettings = [[UIApplication sharedApplication] currentUserNotificationSettings];
    if (!notificationSettings.types) {
        // …
        // fire custom event
        // ...
    }
  }
```
{% endtab %}
{% tab swift %}
```swift
if #available(iOS 10, *) {
  let center = UNUserNotificationCenter.current()
  center.getNotificationSettings(completionHandler: { (settings) in
    if settings.authorizationStatus == .notDetermined {
      // ...
      // fire custom event
      // ...
    }
  })
} else {
let notificationSettiings = UIApplication.shared.currentUserNotificationSettings
  if notificationSettiings?.types != nil {
    // ...
    // fire custom event
    // ...
  }
}
```
{% endtab %}
{% endtabs %}

## Paso 3: Configurar un controlador de vínculos profundos

Coloca este fragmento de código dentro de tu código de gestión de vínculos profundos. Solo debes ejecutar este código de vínculo profundo para tu mensaje push primer dentro de la aplicación.

Consulta la [personalización del manejo de enlaces]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/advanced_use_cases/linking/#linking-handling-customization) para obtener más información sobre la vinculación en profundidad.

{% tabs %}
{% tab OBJETIVO-C %}
```objc
  // ...
  // check that this deep link relates to the push prompt
  // ...
  if (@available(iOS 10.0, *)) {
    UNUserNotificationCenter *center = [UNUserNotificationCenter currentNotificationCenter];
    [center requestAuthorizationWithOptions:(UNAuthorizationOptionAlert | UNAuthorizationOptionSound | UNAuthorizationOptionBadge) completionHandler:^(BOOL granted, NSError * _Nullable error) {
      [[Appboy sharedInstance] pushAuthorizationFromUserNotificationCenter:granted];
    }];
    center.delegate = self;
    [center setNotificationCategories:[ABKPushUtils getAppboyUNNotificationCategorySet]];
    [[UIApplication sharedApplication] registerForRemoteNotifications];
  } else {
    UIUserNotificationSettings *settings = [UIUserNotificationSettings settingsForTypes:(UIUserNotificationTypeBadge | UIUserNotificationTypeAlert | UIUserNotificationTypeSound) categories:[ABKPushUtils getAppboyUIUserNotificationCategorySet]];
      UIApplication *sharedApplication = [UIApplication sharedApplication];
      [sharedApplication registerUserNotificationSettings:settings];
      [sharedApplication registerForRemoteNotifications];
  }
```
{% endtab %}
{% tab swift %}

```swift
  // ...
  // check that this deep link relates to the push prompt
  // ...
  if #available(iOS 10, *) {
    let center = UNUserNotificationCenter.current()
    center.delegate = self as? UNUserNotificationCenterDelegate
    center.requestAuthorization(options: [.alert, .sound, .badge]) { (granted, error) in
    Appboy.sharedInstance()?.pushAuthorization(fromUserNotificationCenter: granted)
  }
  UIApplication.shared.registerForRemoteNotifications()
  } else {
    let setting = UIUserNotificationSettings(types: [.alert, .badge, .sound], categories:nil)
    UIApplication.shared.registerUserNotificationSettings(setting)
    UIApplication.shared.registerForRemoteNotifications()
  }
```
{% endtab %}
{% endtabs %}
