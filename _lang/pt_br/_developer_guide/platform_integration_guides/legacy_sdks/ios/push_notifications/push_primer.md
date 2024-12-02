---
nav_title: "Push Primer"
article_title: Manual do Push para iOS
page_order: 6
page_type: reference
description: "Este artigo de referência aborda como integrar os primers push do iOS."
platform: iOS
channel:
  - push
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Integração do push primer

Campanhas de push primer incentivam os usuários a ativar os pushes do seu app nos dispositivos deles. Obter a permissão dos usuários para enviar mensagens diretamente para seus dispositivos pode ser complexo, mas nossos guias podem ajudar! Este guia mostra as etapas que os desenvolvedores devem seguir para integrar push primers.

## Etapa 1: Adicionar snippet no arquivo AppDelegate.m 

Adicione a seguinte linha de código ao seu arquivo `AppDelegate.m` no lugar da integração padrão:

{% tabs %}
{% tab OBJECTIVE C %}

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

## Etapa 2: Anexar o verificador de eventos personalizado ao arquivo AppDelegate.m 

O seguinte trecho de código verifica se um evento personalizado precisa ser disparado. Adicione a seguinte linha de código em seu site `AppDelegate.m`.

{% tabs %}
{% tab OBJECTIVE C %}
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

## Etapa 3: Configurar um manipulador de deep links

Coloque o seguinte trecho de código em seu código de manipulação de deep links. Você só deve executar esse código de deep link para a mensagem no app do seu push primer.

Para saber mais sobre deep links, consulte a [personalização do manuseio de links]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/advanced_use_cases/linking/#linking-handling-customization).

{% tabs %}
{% tab OBJECTIVE C %}
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
