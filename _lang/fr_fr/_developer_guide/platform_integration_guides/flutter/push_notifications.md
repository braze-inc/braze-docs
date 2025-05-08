---
nav_title: Notifications push
article_title: Notifications push pour Flutter
platform: Flutter
page_order: 2
description: "Cet article couvre l’implémentation et le test des notifications push sur Flutter."
channel: push

---

# Intégration de notifications Push

> Cet article de référence explique comment configurer les notifications push pour Flutter. L’intégration des notifications push nécessite de configurer séparément chaque plateforme native. Suivez les guides respectifs listés pour terminer l’installation.

## Étape 1 : Terminer la configuration initiale

{% tabs %}
{% tab Android %}
### Étape 1.1 : Enregistrer la notification push

Enregistrez-vous pour les notifications push en utilisant l'API Firebase Cloud Messaging (FCM) de Google. Pour accéder à une présentation complète, reportez-vous aux étapes suivantes du [guide d'intégration des notifications push Native Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/) :

1. [Ajoutez Firebase à votre projet]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-1-add-firebase-to-your-project).
2. [Ajoutez Cloud Messaging à vos dépendances]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-2-add-cloud-messaging-to-your-dependencies).
3. [Créez un compte de service]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-3-create-a-service-account).
4. [Générez des identifiants JSON]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-4-generate-json-credentials).
5. [Téléchargez vos informations d'identification JSON sur Braze]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-5-upload-your-json-credentials-to-braze).

### Étape 1.2 : Obtenez votre ID d'expéditeur Google

Tout d'abord, accédez à la console Firebase, ouvrez votre projet, puis sélectionnez <i class="fa-solid fa-gear"></i> **Paramètres** > **Paramètres du projet**.

![Le projet Firebase avec le menu Paramètres ouvert.]({% image_buster /assets/img/android/push_integration/set_up_automatic_token_registration/select-project-settings.png %})

Sélectionnez **Messagerie Cloud**, puis sous **API Firebase Cloud Messaging (V1)**, copiez l'**ID de l'expéditeur** dans votre presse-papiers.

![La page Messagerie Cloud du projet Firebase avec l'ID de l'expéditeur mis en évidence.]({% image_buster /assets/img/android/push_integration/set_up_automatic_token_registration/copy-sender-id.png %})

### Étape 1.3 : Mettez à jour votre `braze.xml`

Ajoutez ce qui suit à votre fichier `braze.xml`. Remplacez `FIREBASE_SENDER_ID` par l'ID de l'expéditeur que vous avez copié précédemment.

```xml
<bool translatable="false" name="com_braze_firebase_cloud_messaging_registration_enabled">true</bool>
<string translatable="false" name="com_braze_firebase_cloud_messaging_sender_id">FIREBASE_SENDER_ID</string>
```

{% endtab %}

{% tab iOS %}
### Étape 1.1 : Télécharger les certificats APN

Générez un certificat pour le service de notification push d'Apple (APNs) et téléchargez-le dans le tableau de bord de Braze. Pour accéder à une description complète, voir [Charger votre certificat APN]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#step-1-upload-your-apns-certificate).

### Étape 1.2 : Ajoutez la prise en charge des notifications push à votre application.

Suivez le [guide d'intégration native pour iOS.]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/?tab=objective-c#automatic-push-integration)

{% endtab %}
{% endtabs %}

## Étape 2 : Écouter les événements de notification push (facultatif).

Pour écouter les événements de notifications push que Braze a détectés et traités, appelez `subscribeToPushNotificationEvents()` et transmettez un argument à exécuter.

{% alert note %}
Les événements de notification push de Braze sont disponibles sur Android et iOS. En raison des différences entre les plateformes, iOS ne détectera les événements push de Braze que lorsqu'un utilisateur aura interagi avec une notification.
{% endalert %}

```dart
// Create stream subscription
StreamSubscription pushEventsStreamSubscription;

pushEventsStreamSubscription = braze.subscribeToPushNotificationEvents((BrazePushEvent pushEvent) {
  print("Push Notification event of type ${pushEvent.payloadType} seen. Title ${pushEvent.title}\n and deeplink ${pushEvent.url}");
  // Handle push notification events
});

// Cancel stream subscription
pushEventsStreamSubscription.cancel();
```

#### Champs d'événements de la notification push

{% alert note %}
En raison des limitations de la plateforme sur iOS, le SDK Braze peut uniquement traiter les charges utiles des notifications push lorsque l'appli est au premier plan. Les écouteurs ne se déclencheront pour le type d'événement `push_opened` sur iOS qu'après qu'un utilisateur aura interagi avec une notification push.
{% endalert %}

Pour obtenir une liste complète des champs de notifications push, reportez-vous au tableau ci-dessous :

| Nom du champ         | Type      | Description |
| ------------------ | --------- | ----------- |
| `payloadType`     | Chaîne de caractères    | Spécifie le type de charge utile de la notification. Les deux valeurs envoyées par le SDK Braze pour Flutter sont `push_opened` et `push_received`.  Seuls les événements `push_opened` sont pris en charge sur iOS. |
| `url`              | Chaîne de caractères    | Spécifie l'URL qui a été ouvert par la notification. |
| `useWebview`      | Valeur booléenne   | Si la valeur est `true`, l'URL s'ouvrira dans l'application, dans une fenêtre WebView modale. Si la valeur est `false`, l'URL s'ouvrira dans le navigateur de l'appareil. |
| `title`            | Chaîne de caractères    | Représente le titre de la notification. |
| `body`             | Chaîne de caractères    | Représente le corps ou le contenu du texte de la notification. |
| `summaryText`     | Chaîne de caractères    | Représente le texte résumé de la notification. Celle-ci est mappée à partir de `subtitle` sur iOS. |
| `badgeCount`      | Nombre   | Représente le nombre de badges de la notification. |
| `timestamp`        | Nombre | Représente l'heure à laquelle la charge utile a été reçue par l'application. |
| `isSilent`        | Valeur booléenne   | Si la valeur est `true`, la charge utile est reçue en silence. Pour plus de détails sur l'envoi de notifications push silencieuses sur Android, reportez-vous à la section [Notifications push silencieuses sur Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/silent_push_notifications). Pour plus de détails sur l'envoi de notifications push silencieuses sur iOS, reportez-vous à la section [Notifications push silencieuses sur iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/silent_push_notifications/). |
| `isBrazeInternal`| Valeur booléenne   | Cette adresse sera `true` si une charge utile de notification a été envoyée pour une fonctionnalité interne du SDK, telle que la synchronisation des géorepérages, la synchronisation des indicateurs de fonctionnalités ou le suivi des désinstallations. La charge utile est reçue silencieusement par l'utilisateur. |
| `imageUrl`        | Chaîne de caractères    | Spécifie l'URL associée à l'image de notification. |
| `brazeProperties` | Objet    | Représente les propriétés de Braze associées à la campagne (paires clé-valeur). |
| `ios`              | Objet    | Représente les champs spécifiques à iOS. |
| `android`          | Objet    | Représente les champs spécifiques à Android. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Étape 3 : Tester l’affichage des notifications push

Pour tester votre intégration après avoir configuré les notifications push dans la couche native :

1. Configurez un utilisateur actif dans l’application Flutter. Pour ce faire, initialisez votre plug-in en appelant `braze.changeUser('your-user-id')`.
2. Allez dans **Campagnes** et créez une nouvelle campagne de notification push. Choisissez les plateformes que vous souhaitez tester.
3. Composez votre notification test et sélectionnez l’onglet **Test**. Ajoutez le même `user-id` que l'utilisateur test et cliquez sur **Envoyer le test**.
4. Vous devriez recevoir rapidement la notification sur votre appareil. Vous devrez peut-être vérifier le centre de notification ou mettre à jour les paramètres si elle ne s’affiche pas.

{% alert tip %}
À partir de Xcode 14, vous pouvez tester les notifications push à distance sur un simulateur iOS.
{% endalert %}
