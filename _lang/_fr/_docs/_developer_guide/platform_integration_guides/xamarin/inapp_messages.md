---
nav_title: Messagerie intégrée
article_title: Messagerie In-App pour Xamarin
platform:
  - Xamarin
  - iOS
  - Android
page_order: 2
description: "Cet article couvre la messagerie iOS, Android et FireOS pour la plateforme Xamarin."
channel: messages intégrés à l'application
---

# Messagerie intégrée

## Android
Voir [les instructions d'intégration Android][11] pour plus d'informations sur la façon d'intégrer les messages dans l'application dans votre application Xamarin Android.  En outre, vous pouvez consulter le [exemple d'application][12] pour les exemples d'implémentation.

## iOS

Les messages intégrés fonctionneront par défaut si vous avez inclus le dossier Appboy.bundle dans votre application.  Sur Xamarin, nous ne prenons pas en charge le style personnalisé des messages dans l'application.  Si vous souhaitez personnaliser votre interface utilisateur dans l'application, veuillez implémenter la méthode ABKInAppMessageControllerDelegate `ABKInAppMessageViewController InAppMessageViewControllerWithInAppMessage(ABKInAppMessage inAppMessage);` et retourne votre contrôleur de vue personnalisé. Cela permettra de s'assurer que Braze vous passe l'objet de message dans l'application plutôt que de l'afficher pour vous. Vous aurez alors la possibilité d'afficher manuellement le contenu de l'objet de message dans l'application.

Consultez [les instructions d'intégration iOS][1] pour plus d'informations sur les meilleures pratiques In-App.  En outre, vous pouvez consulter le [exemple d'application][2] pour les exemples d'implémentation.

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/#in-app-messaging
[11]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/overview/
[12]: https://github.com/Appboy/appboy-xamarin-bindings/tree/master/appboy-component/samples
