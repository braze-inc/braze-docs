---
nav_title: Notifications push
article_title: Notifications push pour Xamarin
platform:
  - Xamarin
  - iOS
  - Android
page_order: 1
description: "Cet article couvre l'intégration des notifications push sur Android et FireOS pour la plate-forme Xamarin."
channel: Pousser
---

# Notifications push

## Android

Consultez [les instructions d'intégration Android][11] pour plus d'informations sur la façon d'intégrer push dans votre application Xamarin Android. En outre, vous pouvez regarder le [exemple d'application][12] pour voir comment les espaces de noms passent de java à c#.

## iOS

Consultez [les instructions d'intégration iOS][1] pour plus d'informations sur la configuration de votre application avec push et stockage de vos identifiants sur notre serveur.

### Demande d'autorisations push

Configurez les permissions push en ajoutant le code suivant à la section `FinishedLaunching` de votre `AppDelegate.cs`:

```csharp
// C#
UIUserNotificationSettings settings = UIUserNotificationSettings.GetSettingsForTypes(UIUserNotificationType.Badge | UIUserNotificationType.Alert | UIUserNotificationType.Sound, null);
UIApplication.SharedApplication.RegisterForRemoteNotifications();
UIApplication.SharedApplication.RegisterUserNotificationSettings(settings);
```

> Si vous avez implémenté une invite opt-in personnalisée, assurez-vous que vous appelez le code ci-dessus TOUS LES fois que l'application s'exécute après qu'ils accordent des autorisations push à votre application. Les applications doivent se réinscrire avec les APN car les jetons de l'appareil peuvent changer arbitrairement.

### Enregistrement des jetons push

Enregistrez-vous pour vos jetons push en ajoutant le code suivant dans la méthode `RegisteredForRemoteNotifications` de votre `AppDelegate.cs`:

```csharp
// C#
Appboy.SharedInstance().RegisterDeviceToken (deviceToken);
```

### Activation des analyses push

Activer le suivi d'ouverture sur les notifications push en ajoutant le code suivant à la méthode `DidReceiveRemoteNotification` de votre `AppDelegate.cs`:

```csharp
// C#
public override void DidReceiveRemoteNotification (UIApplication application, NSDictionary userInfo, Action<UIBackgroundFetchResult> completionHandler)
  {
    Appboy.SharedInstance().RegisterApplicationWithFetchCompletionHandler(application, userInfo, completionHandler);
}
```

### Nombre de badges

Si le nombre de badges [est activé][2], Braze affichera un badge lorsqu'un client a des notifications non lues. Par défaut, ce nombre est de 1. Braze n'effacera le nombre de badges que lorsque l'application est ouverte directement à partir d'une notification Braze push. Pour effacer le nombre de badges, vous pouvez vous référer à la documentation [Xamarin][3] et utiliser le code suivant :

```csharp
// C#
UIApplication.SharedApplication.ApplicationIconBadgeNumber = 0;
```

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/
[2]: {{site.baseurl}}/help/best_practices/utilizing_badge_count/#badge-count-with-braze
[3]: https://developer.xamarin.com/guides/cross-platform/application_fundamentals/notifications/ios/local_notifications_in_ios/#Handling_Notifications
[11]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/
[12]: https://github.com/Appboy/appboy-xamarin-bindings

