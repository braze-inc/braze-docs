---
nav_title: Notifications push
article_title: Notifications push pour Flutter
platform: Flutter
page_order: 2
description: "Cet article couvre les notifications push sur Flutter."
channel: notification push

---

# Notifications push

L’intégration des notifications push dans Flutter nécessite de configurer séparément chaque plateforme native. Suivez les guides d’intégration respectifs pour terminer l’installation.

## Étape 1 : Configuration native complète

- **Android :** Suivez les [Instructions d’intégration Android][1].
- **iOS :** Suivez les [Instructions d’intégration iOS][2].

## Étape 2 : Tester l’affichage des notifications push

Suivez ces étapes pour tester votre intégration de notification push.

{% alert important %}
Vous ne pouvez pas tester le comportement des applications liées à la notification push sur un émulateur iOS car les émulateurs ne prennent pas en charge les jetons de périphérique requis pour envoyer et recevoir une notification push.
{% endalert %}

1. Configurez un utilisateur actif dans l’application Flutter. Pour ce faire, initialisez votre plug-in en appelant `braze.changeUser('your-user-id')`.
2. Dirigez-vous vers la page **Campaigns** et créez une nouvelle campagne de notification push. Choisissez les plates-formes que vous souhaitez tester.
3. Composez votre notification test et rendez-vous sur l’onglet **Test**. Ajoutez les mêmes `user-id` que l’utilisateur de test et cliquez sur **Send Test (Envoyer un test)**.
4. Vous devriez recevoir rapidement la notification sur votre appareil. Vous devrez peut-être vérifier le centre de notification ou mettre à jour les paramètres si elle ne s’affiche pas.


[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/
