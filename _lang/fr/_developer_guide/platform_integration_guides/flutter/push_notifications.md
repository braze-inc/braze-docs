---
nav_title: Notifications push
article_title: Notifications push pour Flutter
platform: Flutter
page_order: 2
description: "Cet article couvre l’implémentation et le test des notifications push sur Flutter."
channel: push

---

# Intégration de notifications Push

> Une notification push est une alerte hors application qui apparaît sur l’écran de l’utilisateur lorsqu’une mise à jour importante se produit. Les notifications push constituent un moyen précieux de fournir à vos utilisateurs un contenu urgent et pertinent, ou de les réengager dans votre application. Cet article couvre l’implémentation et le test des notifications push sur Flutter.

{% alert important %}
Braze n’est pas compatible avec la couche wrapper Flutter pour envoyer des notifications push ou des liens profonds. Pour utiliser cette fonctionnalité avec votre application Flutter, vous devez configurer les notifications push séparément pour chaque plateforme native. 
- **Android :** Suivez les [Instructions d’intégration Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/).
- **iOS :** Suivez les [Instructions d’intégration iOS](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b1-standard-push-notifications).
{% endalert %}


## Tester les notifications push

Lorsque vous avez configuré les notifications push dans la couche native, suivez les étapes ci-dessous pour tester votre intégration de notification push.

{% alert important %}
Vous ne pouvez pas tester le comportement des applications liées à la notification push sur un émulateur iOS, car les émulateurs ne prennent pas en charge les jetons de périphérique requis pour envoyer et recevoir une notification push.
{% endalert %}

1. Configurez un utilisateur actif dans l’application Flutter. Pour ce faire, initialisez votre plug-in en appelant `braze.changeUser('your-user-id')`.
2. Dirigez-vous vers la page **Campaigns (Campagnes)** et créez une nouvelle campagne de notification push. Choisissez les plateformes que vous souhaitez tester.
3. Composez votre notification test et rendez-vous sur l’onglet **Test**. Ajoutez les mêmes `user-id` que l’utilisateur de test et cliquez sur **Send Test (Envoyer le test)**.
4. Vous devriez recevoir rapidement la notification sur votre appareil. Vous devrez peut-être vérifier le centre de notification ou mettre à jour les paramètres si elle ne s’affiche pas.
