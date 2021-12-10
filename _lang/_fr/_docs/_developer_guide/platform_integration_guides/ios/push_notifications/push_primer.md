---
nav_title: "Pousser l'amorce"
article_title: Pousser l'amorce pour iOS
page_order: 6
page_type: Référence
description: "Cet article traite de la façon d'intégrer les primeurs push iOS."
platform: iOS
channel:
  - Pousser
---

# Intégration de Push primer

> Les campagnes Push Primer encouragent vos utilisateurs à activer le push sur leur appareil pour votre application. Obtenir la permission des utilisateurs d'envoyer des messages directement à leur appareil peut être complexe, mais nos guides peuvent vous aider ! <br><br>Ce guide montre les étapes que les développeurs doivent faire pour intégrer Push Priming.

## Étape 1 : Ajouter un snippet dans le fichier AppDelegate.m

{% tabs %}
{% tab OBJECTIVE-C %}

Ajoute la ligne de code suivante à ton fichier `AppDelegate.m` à la place de l'intégration standard :

```objc
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
...
if (@available(iOS 10. , *)) {
    UNUserNotificationCenter *center = [UNUserNotificationCenter currentNotificationCenter];
    [centre getNotificationSettingsWithCompletionHandler:^(UNNotificationSettings * _Nonnull paramètres) {
      if (paramètres. Statut d'uthorization! UNAuthorizationStatusNotDetermined) {
        // l'autorisation a déjà été demandée, doivent suivre les étapes habituelles
        [centre requestAuthorizationWithOptions:(UNAuthorizationOptionAlert | UNAuthorizationOptionSound | UNAuthorizationOptionBadge) completionHandler:^(BOL accordé, NSError * _Nullable error) {
          [[Appboy sharedInstance] pushAuthorizationFromUserNotificationCenter:granted];
        }] ;
        centre. elegate = self;
        [center setNotificationCategories:[ABKPushUtils getAppboyUNNotificationCategorySet]];
        [[UIApplication sharedApplication] registerForRemoteNotifications];
      }
    }];
  } else {
    UIApplication *sharedApplication = [UIApplication sharedApplication];
    UIUserNotificationSettings *notificationSettings = [sharedApplication currentUserNotificationSettings];
    if (notificationSettings. ypes) {
      UIUserNotificationSettings *settings = [UIUserNotificationSettings settingsForTypes:(UIUserNotificationTypeBadge | UIUserNotificationTypeAlert | UIUserNotificationTypeSound) categories:[ABKPushUtils getAppboyUIUserNotificationCategorySet]];
      [sharedApplication registerUserNotificationSettings:settings];
      [sharedApplication registerForRemoteNotifications] ;
    }
}
```
{% endtab %}
{% tab swift %}

Ajoute la ligne de code suivante à ton fichier `AppDelegate.m` à la place de l'intégration standard :

```swift
if #available(iOS 10, *) {
  let center = UNUserNotificationCenter.current()
  centre. etNotificationSettings(completionHandler: { (paramètres) dans
    si paramètres. uthorizationStatus != . otDetermined {
      // l'autorisation a déjà été demandée, avoir besoin de suivre les étapes habituelles
      centre. equestAuthorization(options: [.alert, .sound, .badge]) { (accordé, erreur) in
      Appboy.sharedInstance()?. ushAuthorization(fromUserNotificationCenter: accordé)
      }
      center.delegate = self as? UNUserNotificationCenterDelegate
      center.setNotificationCategories(ABKPushUtils.getAppboyUNNotificationCategorySet())
      UIApplication. hared.registerForRemoteNotifications()
    }
  })
} else {
  let notificationSettiings = UIApplication.shared. urrentUserNotificationSettings
  if notificationSettiings?.types != nil {
    let setting = UIUserNotificationSettings(types: [.alert, .badge, . ound], categories:nil)
    UIApplication.shared.registerUserNotificationSettings(setting)
    UIApplication.shared.registerForRemoteNotifications()
  }
}
```
{% endtab %}
{% endtabs %}

## Étape 2 : Ajouter un vérificateur d'événements personnalisé au fichier AppDelegate.m

{% tabs %}
{% tab OBJECTIVE-C %}
__Vérifie si un événement personnalisé a besoin d'être lancé__<br> Ajoute la ligne de code suivante à votre `AppDelegate.` en plus de celui ci-dessus.
```objc
if (@available(iOS 10. , *)) {
    UNUserNotificationCenter *center = [UNUserNotificationCenter currentNotificationCenter];
    [centre getNotificationSettingsWithCompletionHandler:^(UNNotificationSettings * _Nonnull paramètres) {
      if (paramètres. uthorizationStatus == UNAuthorizationStatusNotDetermined) {
        // ...
        // feu événement personnalisé
        // ...
      }
    }];
  } else {
    UIUserNotificationSettings *notificationSettings = [[UIApplication sharedApplication] currentUserNotificationSettings];
    if (!notificationSettings.types) {
        // …
        // feu événement personnalisé
        // ...
    }
  }
```
{% endtab %}
{% tab swift %}
__Vérifie si un événement personnalisé a besoin d'être lancé__<br> Ajoute la ligne de code suivante à votre `AppDelegate.` en plus de celui ci-dessus.
```swift
if #available(iOS 10, *) {
  let center = UNUserNotificationCenter.current()
  center.getNotificationSettings(completionHandler: { (settings) in
    if settings.authorizationStatus == .notDetermined {
      // ...
      // feu événement personnalisé
      // ...
    }
  })
} else {
let notificationSettiings = UIApplication.shared.currentUserNotificationSettings
  if notificationSettiings?.types != nil {
    // ...
    // feu événement personnalisé
    // ...
```
} }
{% endtab %}
{% endtabs %}

## Étape 3 : Configurez le gestionnaire de profondeurs

{% tabs %}
{% tab OBJECTIVE-C %}
__Deep Link Handler__<br> Placez ce code snippet en dehors de l'application `(BOOL):(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions` méthode à partir de l'étape 1. <br> Pour plus d'informations sur les liens profonds consultez notre [documentation]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/advanced_use_cases/linking/#linking-handling-customization).
```objc
  // ...
  // vérifie que ce lien profond se rapporte à l'invite de poussée
  // ...
  if (@available(iOS 10. , *)) {
    UNUserNotificationCenter *center = [UNUserNotificationCenter currentNotificationCenter];
    [centre requestAuthorizationWithOptions:(UNAuthorizationOptionAlert | UNAuthorizationOptionSound | UNAuthorizationOptionBadge) completionHandler :^(BOL accordé, NSError * _Nullable error) {
      [[Appboy sharedInstance] pushAuthorizationFromUserNotificationCenter:granted];
    }];
    centre. elegate = self;
    [center setNotificationCategories:[ABKPushUtils getAppboyUNNotificationCategorySet]];
    [[UIApplication sharedApplication] registerForRemoteNotifications];
  } else {
    UIUserNotificationSettings *settings = [UIUserNotificationSettings settingsForTypes:(UIUserNotificationTypeBadge | UIUserNotificationTypeAlert | UIUserNotificationTypeAlert | UIUserNotificationTypeSound) categories:[ABKPushUtils getAppboyUIUserNotificationCategorySet]];
      UIApplication *sharedApplication = [UIApplication sharedApplication] ;
      [sharedApplication registerUserNotificationSettings:settings];
      [sharedApplication registerForRemoteNotifications];
}
```
{% endtab %}
{% tab swift %}
__Deep Link Handler__<br> Placez ce code snippet en dehors de l'application `(BOOL):(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions` méthode à partir de l'étape 1. <br> Pour plus d'informations sur les liens profonds consultez notre [documentation]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/advanced_use_cases/linking/#deep-linking-to-app-settings).
```swift
  // ...
  // vérifie que ce lien profond se rapporte à l'invite de poussée
  // ...
  if #available(iOS 10, *) {
    let center = UNUserNotificationCenter.current()
    center.delegate = self as ? UNUserNotificationCenterDelegate
    center.requestAuthorization(options: [.alert, .sound, .badge]) { (accordé, erreur) dans
    Appboy. haredInstance()?.pushAuthorization(fromUserNotificationCenter: accordé)
  }
  UIApplication.shared. egisterForRemoteNotifications()
  } else {
    let setting = UIUserNotificationSettings(types: [.alert, .badge, . ound], categories:nil)
    UIApplication.shared.registerUserNotificationSettings(setting)
    UIApplication.shared.registerForRemoteNotifications()
}
```
{% endtab %}
{% endtabs %}
