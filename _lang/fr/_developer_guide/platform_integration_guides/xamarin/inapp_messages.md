---
nav_title: Envoi de messages in-app
article_title: Messagerie in-App pour Xamarin
platform: 
  - Xamarin
  - iOS
  - Android
page_order: 2
description: "Cet article couvre la messagerie in-app sur iOS, Android et FireOS pour la plateforme Xamarin."
channel: messages In-App

---

# Envoi de messages in-app

## Android
Consultez les [instructions d’intégration Android][11] pour plus d’informations sur l’intégration des messages in-app dans votre application Xamarin pour Android.  En outre, vous pouvez consulter [l’exemple d’application][12] pour un exemple d’implémentation.

## iOS

Les messages in-app fonctionnent par défaut si vous avez inclus le dossier Appboy.bundle dans votre application. Sur Xamarin, nous ne prenons pas actuellement en charge le style personnalisé des messages in-app. Si vous souhaitez personnaliser l’IU de votre message in-app, implémentez la ABKInAppMessageControllerDelegate méthode `ABKInAppMessageViewController InAppMessageViewControllerWithInAppMessage(ABKInAppMessage inAppMessage);` et retournez votre contrôleur de vue personnalisé. Cela vous permettra de vous assurer que Braze vous transmet l’objet du message in-app plutôt que de l’afficher pour vous. Vous aurez alors la possibilité d’afficher manuellement le contenu de l’objet du message in-app.

Consultez les [instructions d’intégration iOS][1] pour plus d’informations sur les bonnes pratiques in-app. En outre, vous pouvez consulter [l’exemple d’application][2] pour un exemple d’implémentation.

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/#in-app-messaging
[2]: https://github.com/Appboy/appboy-xamarin-bindings/tree/master/appboy-component/samples
[11]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/overview/
[12]: https://github.com/Appboy/appboy-xamarin-bindings/tree/master/appboy-component/samples
