---
nav_title: Notifications push
article_title: Notifications push pour Xamarin
platform: 
  - Xamarin
  - iOS
  - Android
page_order: 1
description: "Cet article couvre l’intégration de notifications push sur Android et FireOS pour la plate-forme Xamarin."
channel: Notification push 
---

# Notifications push

## Android

Consultez les [instructions d’intégration Android][11] pour savoir comment intégrer les notifications push dans votre application Xamarin sur Android. En outre, vous pouvez regarder l’[exemple d’application][12] pour voir comment changent les espaces de noms entre Java et C#.

## iOS

Consultez les [instructions d’intégration iOS][1] pour plus d’informations sur la configuration de votre application pour les notifications push et le stockage de vos informations d’identification sur notre serveur.

### Demander des autorisations de notifications push

Configurez les autorisations de notifications push en ajoutant le code suivant à la section ```FinishedLaunching``` de votre ```AppDelegate.cs``` :

```csharp
// C#
UIUserNotificationSettings settings = UIUserNotificationSettings.GetSettingsForTypes(UIUserNotificationType.Badge | UIUserNotificationType.Alert | UIUserNotificationType.Sound, null);
UIApplication.SharedApplication.RegisterForRemoteNotifications();
UIApplication.SharedApplication.RegisterUserNotificationSettings(settings);
```

>  Si vous avez implémenté une demande d'inscription aux notifications push personnalisée, assurez-vous d’appeler le code précédent CHAQUE fois que l’application s’exécute après qu’elle ait attribué les autorisations de push à votre application. Les applications doivent se réenregistrer avec des APN car les jetons d’appareil peuvent changer arbitrairement.

### Enregistrer des jetons de notification push

Enregistrez vos jetons de notification push en ajoutant le code suivant à la méthode ```RegisteredForRemoteNotifications``` de votre ```AppDelegate.cs``` :

```csharp
// C#
Appboy.SharedInstance().RegisterDeviceToken (deviceToken);
```

### Activer l’analytique de notification push

Activez le suivi ouvert des notifications push en ajoutant le code suivant à la méthode `DidReceiveRemoteNotification` de votre `AppDelegate.cs` :

```csharp
// C#
public override void DidReceiveRemoteNotification (UIApplication application, NSDictionary userInfo, Action<UIBackgroundFetchResult> completionHandler)
  {
    Appboy.SharedInstance().RegisterApplicationWithFetchCompletionHandler(application, userInfo, completionHandler);
  }
```

### Dénombrement des badges

Si [le dénombrement des badges est activé][2], Braze affiche un badge lorsqu’un client a des notifications non lues. Par défaut, ce nombre est 1. Braze ne réinitialise le nombre de badges que lorsque l’application est ouverte directement à partir d’une notification push de Braze. Pour réinitialiser le nombre de badges, consultez [Xamarin][3] et utilisez le code suivant :

```csharp
// C#
UIApplication.SharedApplication.ApplicationIconBadgeNumber = 0;
```

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/
[2]: {{site.baseurl}}/help/best_practices/utilizing_badge_count/#badge-count-with-braze
[3]: https://developer.xamarin.com/guides/cross-platform/application_fundamentals/notifications/ios/local_notifications_in_ios/#Handling_Notifications
[11]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/
[12]: https://github.com/braze-inc/braze-xamarin-sdk

