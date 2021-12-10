---
nav_title: iOS
article_title: Notifications push pour l'unité
platform:
  - Unité
  - iOS
channel: Pousser
ex_push_payload: archive/apple/push_payload.json
page_order: 1
description: "Cet article de référence couvre l'intégration des notifications push iOS pour la plate-forme Unity."
---

# Notifications push

## Étape 1 : Choisissez l'intégration automatique ou manuelle de push

Braze fournit une solution native Unity pour automatiser les intégrations de push iOS.

- Si vous préférez compléter l'intégration manuellement en modifiant votre projet Xcode construit, veuillez suivre nos [instructions natives pour iOS Push][8].
- Si vous passez d'une intégration manuelle à une intégration automatisée, suivez les instructions sur [Transitioning from Manual to Automated Integration][2].
- Notre solution automatique de notification push tire parti de la fonctionnalité d'autorisation provisoire d'iOS 12 et n'est pas disponible avec la fenêtre pop-up native.

## Étape 2 (facultatif) : Implémenter l'intégration automatique de push

### Configurer les notifications push

Suivez les instructions de notre [documentation de configuration de notification Push iOS][8] pour configurer Braze à l'aide d'un fichier `.p8` ou `.p12`.

### Activer l'intégration automatique des push

Dans l'éditeur d'unité, ouvrez les paramètres de configuration de Braze en naviguant vers "Braze" > "Configuration de Braze".

!\[activer la notification push\]\[24\]

Cochez "Intégrer Push avec Braze" pour enregistrer automatiquement les utilisateurs pour les notifications push, passer des jetons push au Brésil, suivez les analyses pour les ouvertures de push, et profitez de la gestion par défaut des notifications push de Brase.

!\[Integrate Push With Braze\]\[27\]

### (Optionnel) : Activer le push en arrière-plan

Cochez "Activer le Push en arrière-plan" si vous souhaitez activer le `mode d'arrière-plan` pour les notifications push. Cela permet au système de réveiller votre application depuis l'état `suspendu` quand une notification push arrive, permettant à votre application de télécharger du contenu en réponse aux notifications push. La vérification de cette option est nécessaire pour la fonctionnalité de suivi de la désinstallation de Brase.

!\[Enabling Background Push\]\[29\]

### (Optionnel) : Désactiver l'enregistrement automatique

Les utilisateurs qui n'ont pas encore opté pour les notifications push seront automatiquement autorisés à être repoussés à l'ouverture de votre application. Pour désactiver cette fonctionnalité et enregistrer manuellement les utilisateurs en mode push, cochez "Désactiver l'enregistrement automatique".

- Si "Désactiver l'autorisation provisoire" n'est pas cochée, sur iOS 12 et supérieur, l'utilisateur sera provisoirement (silencieusement) autorisé à recevoir une poussée silencieuse. Si coché, l'utilisateur sera affiché l'invite de push native.

- Si vous avez besoin de configurer exactement quand l'invite est affichée à l'exécution, désactiver l'enregistrement automatique de l'éditeur de configuration de Braze et utiliser `AppboyBinding. romptUserForPushPermissions()` à la place.

!\[Désactiver l'inscription automatique des pousss\]\[28\]

## Étape 3 : Définir les écouteurs push

Si vous souhaitez passer des payloads de notification push à Unity ou prendre des mesures supplémentaires lorsqu'un utilisateur reçoit une notification push, Braze offre la possibilité de régler les écouteurs de notification push.

### Envoyer l'écouteur reçu

L'auditeur push reçu est déclenché lorsqu'un utilisateur reçoit une notification push alors qu'il utilise activement l'application (c'est-à-dire que l'application est au premier plan). Définit l'écouteur reçu dans l'éditeur de configuration de Braze.

!\[Ecouteur reçu par push\]\[30\]

- Si vous avez besoin de configurer l'écouteur d'objet du jeu à l'exécution, utilisez `AppboyBinding.ConfigureListener()` et spécifiez `BrazeUnityMessageType.PUSH_RECEIVED`.

### Envoyer l'écouteur ouvert

L'auditeur ouvert Push est déclenché lorsqu'un utilisateur lance l'application en cliquant sur une notification push. Pour envoyer le bloc push à United, définissez le nom de votre méthode de rappel Game Object et Push Opened listener sous le foldout "Set Push Opened Listener" comme suit:

!\[Ecouteur ouvert Push\]\[31\]


- Si vous avez besoin de configurer l'écouteur d'objet du jeu à l'exécution, utilisez `AppboyBinding.ConfigureListener()` et spécifiez `BrazeUnityMessageType.PUSH_OPENED`.

### Exemple d'implémentation de l'écouteur push

L'exemple suivant implémente l'objet de jeu `AppboyCallback` en utilisant un nom de méthode de rappel de `PushNotificationReceivedCallback` et `PushNotificationOpenedCallback` respectivement.

!\[Game Object Linking\]\[32\]

```csharp
public class Menu principal : MonoBehaviour {
  void PushNotificationReceivedCallback(string message) {
#if UNITY_ANDROID
    Debug. og("PushNotificationReceivedCallback message: " + message);
    PushNotification pushNotification = new PushNotification(message);
    Debug. og("Notification push reçue : " + pushNotification);   
#elif UNITY_IOS
    ApplePushNotification pushNotification = new ApplePushNotification(message);
    Debug. og("Événement de notification push reçu : " + pushNotification);   
#endif  
  }

  void PushNotificationOpenedCallback(string message) {
#if UNITY_ANDROID
    Debug. og("PushNotificationOpenedCallback message: " + message);
    PushNotification pushNotification = new PushNotification(message);
    Debug. og("Notification push ouverte: " + pushNotification);  
#elif UNITY_IOS
    ApplePushNotification pushNotification = new ApplePushNotification(message);
    Debug. og("Événement de notification ouvert push : " + pushNotification);   
#endif  
  }
}
```

## Fonctionnalités avancées

### Push token callback

To receive a copy of device tokens that Braze receives from the OS, set a delegate using `AppboyBinding.SetPushTokenReceivedFromSystemDelegate()`.

### Autres fonctionnalités

Pour implémenter des fonctionnalités avancées telles que des liens profonds, des compteurs de badges et des sons personnalisés, consultez nos [instructions natives][8].
[10]: {% image_buster /assets/img_archive/ios_provisioning.png %} "pushNotification2.png" [11]: {% image_buster /assets/img_archive/AppleProvisioningOptions.png %} "AppleProvisioningOptions. ng" [12]: {% image_buster /assets/img_archive/push_cert_gen.png %} "pushNotification3.png" [24]: {% image_buster /assets/img_archive/Enable_push_capabilities.png %} [27]: {% image_buster /assets/img/unity/ios/unity_ios_api_key. ng %} [28]: {% image_buster /assets/img/unity/ios/unity_ios_disable_auto_push.png %} [29]: {% image_buster /assets/img/unity/ios/unity_ios_enable_background.png %} [30]: {% image_buster /assets/img/unity/ios/unity_ios_push_received. ng %} [31]: {% image_buster /assets/img/unity/ios/unity_ios_push_opened.png %} [32]: {% image_buster /assets/img/unity/ios/unity_ios_appboy_callback.png %}

[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/unity/sdk_integration/ios/#transitioning-from-manual-to-automated-integration-ios
[8]: {{site.baseurl}}/developer_guide/platform_integration_guides/unity/push_notifications/ios/
[8]: {{site.baseurl}}/developer_guide/platform_integration_guides/unity/push_notifications/ios/
[8]: {{site.baseurl}}/developer_guide/platform_integration_guides/unity/push_notifications/ios/
