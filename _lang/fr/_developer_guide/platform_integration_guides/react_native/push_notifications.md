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

{% tabs %}
{% tab Expo %}

Configurer les invites `enableBrazeIosPush` et `enableFirebaseCloudMessaging` afin d’activer les notifications push pour iOS et Android, respectivement.

### Configuration Android

#### Étape 1.1
Paramétrez `firebaseCloudMessagingSenderId` l’invit config dans votre `app.json`. Consultez les [instructions d’intégration Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration#step-4-set-your-firebase-credentials) sur la récupération de votre ID expéditeur. 

#### Étape 1.2
Ajoutez votre `google-services.json` ficher à votre dossier d’application `assets`. Ce fichier est nécessaire lors du paramétrage de `enableFirebaseCloudMessaging: true` dans votre configuration.

```json
{
  "expo": {
    "plugins": [
      [
        "@braze/expo-plugin",
        {
          "androidApiKey": "YOUR-ANDROID-API-KEY",
          "iosApiKey": "YOUR-IOS-API-KEY",
          "enableBrazeIosPush": true,
          "enableFirebaseCloudMessaging": true,
          "firebaseCloudMessagingSenderId": "YOUR-FCM-SENDER-ID"
        }
      ],
    ]
  }
}
```

{% endtab %}
{% tab Android %}

Suivez les [Instructions d’intégration Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/).

{% endtab %}
{% tab iOS %}

Suivez les [Instructions d’intégration iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/). Si vous préférez ne pas demander une autorisation de notification push lors du lancement de l’application, vous devez omettre l’appel `requestAuthorizationWithOptions:completionHandler:` dans votre AppDelegate et suivre les étapes ci-dessous.

{% endtab %}
{% endtabs %}

## Étape 2 : Demander une autorisation de notification push

Utilisez la méthode `Braze.requestPushPermission()` (disponible sur v1.38.2 et supérieures) pour demander une autorisation des notifications push à l’utilisateur sur iOS et Android 13 et supérieurs. Pour Android 12 et inférieurs, cette méthode n’est pas opérationnelle.

Cette méthode intègre in paramètre requis qui précise les autorisations que SDK doit demander à l’utilisateur sur iOS. Ces options n’ont pas d’effet sur Android.

```javascript
const permissionOptions = {
  alert: true,
  sound: true,
  badge: true,
  provisional: false
};

Braze.requestPushPermission(permissionOptions);
```

#### Étape 2.1 : Ecouter les notifications push sur Android (facultatif)

```javascript
Braze.addListener(Braze.Events.PUSH_NOTIFICATION_EVENT, data => {
  console.log(`Événement de notification push du type ${data.push_event_type} constaté. Titre ${data.title}\n et lien profond ${data.deeplink}`);
  console.log(JSON.stringify(data, undefined, 2));
});
```

## Étape 3 : Tester l’affichage des notifications push

À ce stade, vous devriez pouvoir envoyer des notifications aux périphériques. Suivez ces étapes pour tester votre intégration de notification push.

{% alert important %}
Vous ne pouvez pas tester le comportement des applications liées à la notification push sur un émulateur iOS, car les émulateurs ne prennent pas en charge les jetons de périphérique requis pour envoyer et recevoir une notification push.
{% endalert %}

1. Définir un utilisateur actif dans l’application React en appelant la méthode `Braze.changeUserId('your-user-id')`.
2. Dirigez-vous vers la page **Campaigns** et créez une nouvelle campagne de notification push. Choisissez les plateformes que vous souhaitez tester.
3. Composez votre notification test et rendez-vous sur l’onglet **Test**. Ajouter le même `user-id` comme utilisateur de test et cliquez sur **Envoyer le test**. Vous devriez recevoir rapidement la notification sur votre périphérique.

![Une campagne de notifications push Braze montrant que vous pouvez ajouter votre propre ID utilisateur en tant que destinataire de test pour essayer votre notification push.][1]

[1]: {% image_buster /assets/img/react-native/push-notification-test.png %} "Push Campaign Test"
