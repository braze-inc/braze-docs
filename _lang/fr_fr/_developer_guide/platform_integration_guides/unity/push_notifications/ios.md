---
nav_title: iOS
article_title: Notifications push pour Unity
platform:
  - Unity
  - iOS
channel: push
ex_push_payload: archive/apple/push_payload.json
page_order: 1
description: "Cet article de référence couvre l’intégration de notifications push iOS pour la plateforme Unity."

---

# Intégration de notifications Push pour iOS

> Cet article de référence couvre l’intégration de notifications push iOS pour la plateforme Unity.

## Étape 1 : Choisir une intégration des notifications push automatique ou manuelle

Braze fournit une solution Unity native pour l’automatisation des intégrations de notifications push iOS.

- Si vous préférez réaliser l'intégration manuellement en modifiant votre projet Xcode créé, suivez nos [instructions de notifications push iOS natives]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/).
- Si vous passez d'une intégration manuelle à une intégration automatisée, suivez les instructions relatives à la [transition vers une intégration automatisée]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/sdk_integration/ios/#transitioning-from-manual-to-automated-integration-ios).
- Notre solution de notification push automatique tire parti de la fonctionnalité d’autorisation provisoire d’iOS 12 et n’est pas disponible pour utiliser avec la fenêtre contextuelle d’invite de notification push native.

## Étape 2 : Implémenter l’intégration de notification push automatique

### Configurer les notifications push

Suivez notre [documentation de configuration des notifications push iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/) pour configurer Braze à l'aide d'un fichier `.p8`.

### Activer l’intégration automatique de notifications push

Ouvrez les paramètres de configuration de Braze dans l'éditeur Unity en sélectionnant **Braze > Configuration Braze**.

Cochez **Intégrer Push avec Braze** pour inscrire automatiquement les utilisateurs aux notifications push, transmettre les jetons push à Braze, suivre l'analyse/analytique des ouvertures de push et tirer parti de notre gestion par défaut des notifications push.

### Activer la poussée en arrière-plan (facultatif)

Cochez **Enable Background Push** si vous souhaitez activer `background mode` pour les notifications push. Cela permet au système de réveiller votre application à partir de l’état `suspended` lorsqu’une notification push est reçue, permettant à votre application de télécharger le contenu en réponse aux notifications push. Le fait de cocher cette option est nécessaire pour notre fonctionnalité de suivi de la désinstallation.

![L’éditeur Unity affiche les options de configuration Braze. Dans cet éditeur, les options "Automatiser l'intégration d'Unity iOS", "Intégrer le push avec Braze" et "Activer le push en arrière-plan" sont activées.]({% image_buster /assets/img/unity/ios/unity_ios_enable_background.png %})

### Désactiver l'enregistrement automatique (optionnel)

Les utilisateurs qui n’ont pas encore opté pour des notifications push seront automatiquement autorisés aux notifications push lors de l’ouverture de votre application. Pour désactiver cette fonctionnalité et enregistrer manuellement les utilisateurs pour le push, cochez **Désactiver l'enregistrement push automatique.**

- Si la case **Désactiver l'autorisation provisoire** n'est pas cochée sous iOS 12 ou une version ultérieure, l'utilisateur sera provisoirement (silencieusement) autorisé à recevoir le push silencieux. Si cette option est cochée, l’utilisateur affiche l’invite de notification push native.
- Si vous devez configurer exactement quand l’invite est affichée lors de l’exécution, désactivez l’enregistrement automatique de l’éditeur de configuration Braze et utilisez `AppboyBinding.PromptUserForPushPermissions()` à la place.

![L’éditeur Unity affiche les options de configuration Braze. Dans cet éditeur, les options "Automatiser l'intégration d'Unity iOS", "intégrer le push avec Braze" et "désactiver l'enregistrement automatique du push" sont activées.]({% image_buster /assets/img/unity/ios/unity_ios_disable_auto_push.png %})

## Étape 3 : Définir les auditeurs de notifications push

Si vous souhaitez transmettre des charges utiles de notification push à Unity ou prendre des mesures supplémentaires lorsqu’un utilisateur reçoit une notification push, Braze offre la possibilité de définir des auditeurs de notification push.

### L’auditeur a reçu la notification push

Le récepteur push reçu est déclenché lorsqu'un utilisateur reçoit une notification push alors qu'il utilise activement l'application (par exemple, lorsque l'application est au premier plan). Définissez l’auditeur de notification push reçu dans l’éditeur de configuration Braze. Si vous devez configurer votre auditeur d’objet de jeu lors de l’exécution, utilisez `AppboyBinding.ConfigureListener()` et spécifiez `BrazeUnityMessageType.PUSH_RECEIVED`.

![L’éditeur Unity affiche les options de configuration Braze. Dans cet éditeur, l'option "Set Push Received Listener" est développée, et le "Game Object Name" (AppBoyCallback) et le "Callback Method Name" (PushNotificationReceivedCallback) sont fournis.]({% image_buster /assets/img/unity/ios/unity_ios_push_received.png %})

### Auditeur ouvert de notification push

L’auditeur ouvert est déclenché lorsqu’un utilisateur lance l’application en cliquant sur une notification push. Pour envoyer la charge utile de notifications push à Unity, définissez le nom de votre objet de jeu et de la méthode de rappel d’écoute ouverte des notifications push sous l’option **Définir l’auditeur ouvert de notifications push** :

![L’éditeur Unity affiche les options de configuration Braze. Dans cet éditeur, l'option "Set Push Received Listener" est développée, et le "Game Object Name" (AppBoyCallback) et le "Callback Method Name" (PushNotificationOpenedCallback) sont fournis.]({% image_buster /assets/img/unity/ios/unity_ios_push_opened.png %})

Si vous devez configurer votre auditeur d’objet de jeu lors de l’exécution, utilisez `AppboyBinding.ConfigureListener()` et spécifiez `BrazeUnityMessageType.PUSH_OPENED`.

### Exemple d’implémentation d’auditeur de notification push

L’exemple suivant implémente l’objet de jeu `AppboyCallback` utilisant respectivement un nom de méthode de rappel de `PushNotificationReceivedCallback` et `PushNotificationOpenedCallback`.

![Cet exemple graphique d'implémentation présente les options de configuration de Braze mentionnées dans les sections précédentes ainsi qu'un extrait de code C#.]({% image_buster /assets/img/unity/ios/unity_ios_appboy_callback.png %})

```csharp
public class MainMenu : MonoBehaviour {
  void PushNotificationReceivedCallback(string message) {
#if UNITY_ANDROID
    Debug.Log("PushNotificationReceivedCallback message: " + message);
    PushNotification pushNotification = new PushNotification(message);
    Debug.Log("Push Notification received: " + pushNotification);   
#elif UNITY_IOS
    ApplePushNotification pushNotification = new ApplePushNotification(message);
    Debug.Log("Push received Notification event: " + pushNotification);   
#endif  
  }

  void PushNotificationOpenedCallback(string message) {
#if UNITY_ANDROID
    Debug.Log("PushNotificationOpenedCallback message: " + message);
    PushNotification pushNotification = new PushNotification(message);
    Debug.Log("Push Notification opened: " + pushNotification);  
#elif UNITY_IOS
    ApplePushNotification pushNotification = new ApplePushNotification(message);
    Debug.Log("Push opened Notification event: " + pushNotification);   
#endif  
  }
}
```

## Fonctionnalités avancées

### Fonction de rappel de jeton de notification push

Pour recevoir une copie des jetons d'appareil de Braze à partir du système d'exploitation, définissez un délégué à l'aide de `AppboyBinding.SetPushTokenReceivedFromSystemDelegate()`.

### Autres fonctions

Pour implémenter des fonctionnalités avancées telles que des liens profonds, des nombres de badges et des sons personnalisés, consultez nos [instructions de notifications push iOS natives]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/).

