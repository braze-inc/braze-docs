---
nav_title: Notifications push
article_title: Notifications push pour React Native
platform: React Natif
page_order: 2
description: "Cet article couvre la mise en œuvre des notifications push sur React Native."
channel: Pousser
---

# Notifications push

Intégrer les notifications push dans React Native nécessite la mise en place séparée de chaque plate-forme native. Suivez les guides respectifs ci-dessous pour terminer l'installation.

## Étape 1 : Configuration native complète

- Android : Suivez [les instructions d'intégration Android][1].
- iOS: Suivez [les instructions d'intégration iOS][2].

## Étape 2 : Tester l'affichage des notifications push

À ce stade, vous devriez être en mesure d'envoyer des notifications aux appareils. Suivez les étapes ci-dessous pour tester votre intégration push.

{% alert important %}
Vous ne pouvez pas tester le comportement de l'application liée aux notifications push sur un simulateur iOS car les simulateurs ne prennent pas en charge les jetons de l'appareil requis pour envoyer et recevoir une notification push.
{% endalert %}

1. Définissez un utilisateur actif dans l'application React en appelant la méthode `ReactAppboy.changeUserId('votre-utilisateur-id')`.
2. Rendez-vous sur **Campagnes** et créez une nouvelle campagne **Notification**. Choisissez les plateformes que vous souhaitez tester.
3. Écrivez votre notification de test et dirigez-vous vers l'onglet **Test**. Ajoutez le même `identifiant utilisateur` que l'utilisateur de test et cliquez sur **Envoyer le test**. Vous devriez recevoir la notification sur votre appareil sous peu.

!\[Test de campagne push\]\[3\]
[3]: {% image_buster /assets/img/react-native/push-notification-test.png %} "Push Campaign Test"

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/

