---
nav_title: Notifications Push
article_title: Notifications Push pour React Native
platform: React Native
page_order: 2
description: "Cet article couvre les notifications push sur React Native."
channel: Notification push

---

# Notifications push

L’intégration des notifications push dans React Native nécessite de configurer séparément chaque plateforme native. Suivez les guides respectifs listés pour terminer l’installation.

## Étape 1 : Configuration native complète

- Android: Suivez les [Instructions d’intégration Android][1].
- iOS: Suivez les [Instructions d’intégration iOS][2].

## Étape 2 : Tester l’affichage des notifications push

À ce stade, vous devriez pouvoir envoyer des notifications aux périphériques. Suivez ces étapes pour tester votre intégration de notification push.

{% alert important %}
Vous ne pouvez pas tester le comportement des applications liées à la notification push sur un émulateur iOS, car les émulateurs ne prennent pas en charge les jetons de périphérique requis pour envoyer et recevoir une notification push.
{% endalert %}

1. Définir un utilisateur actif dans l’application React en appelant la méthode `ReactAppboy.changeUserId('your-user-id')`.
2. Dirigez-vous vers la page **Campaigns** et créez une nouvelle campagne de notification push. Choisissez les plateformes que vous souhaitez tester.
3. Composez votre notification test et rendez-vous sur l’onglet **Test**. Ajouter le même `user-id` comme utilisateur de test et cliquez sur **Send Test** (Envoyer le test). Vous devriez recevoir rapidement la notification sur votre périphérique.

![Une campagne de notifications push Braze montrant que vous pouvez ajouter votre propre ID utilisateur en tant que destinataire de test pour essayer votre notification push.][3]

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/
[3]: {% image_buster /assets/img/react-native/push-notification-test.png %} "Push Campaign Test"

