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

# Notifications push

## Étape 1 : Choisir une intégration des notifications push automatique ou manuelle

Braze fournit une solution Unity native pour l’automatisation des intégrations de notifications push iOS.

- Si vous préférez terminer manuellement l’intégration en modifiant votre projet Xcode construit, suivez notre [instructions de notifications push iOS natives][8].
- Si vous passez d’une intégration manuelle à une intégration automatique, suivez les instructions sur la [Transition vers une intégration automatisée][2].
- Notre solution de notification push automatique tire parti de la fonctionnalité d’autorisation provisoire d’iOS 12 et n’est pas disponible pour utiliser avec la fenêtre contextuelle d’invite de notification push native.

## Étape 2 : Implémenter l’intégration de notification push automatique

### Configurer les notifications push

Suivez notre [Documentation de configuration de notification push iOS][8] pour configurer Braze en utilisant un fichier `.p8` ou `.p12`.

### Activer l’intégration automatique de notifications push

Ouvrez les paramètres de configuration de Braze dans l’éditeur Unity en naviguant vers **Braze > Configuration Braze**.

Cochez **Intégrer les notifications push avec Braze** pour enregistrer automatiquement les utilisateurs pour les notifications push, passer des jetons push à Braze, suivre les analyses pour les ouvertures de notifications push et profiter de la gestion par défaut des notifications push de Braze.

### (Facultatif) : Activer les notifications push d’arrière-plan

Cochez **Activer les notifications push d’arrière-plan** si vous souhaitez activer `background mode` pour les notifications push. Cela permet au système de réveiller votre application à partir de l’état `suspended` lorsqu’une notification push est reçue, permettant à votre application de télécharger le contenu en réponse aux notifications push. Cocher cette option est nécessaire pour la fonctionnalité de suivi de désinstallation de Braze.

![L’éditeur Unity affiche les options de configuration Braze. Dans cet éditeur, « Automate Unity iOS integration » (Automatiser l’intégration d’Unity iOS », « Integrate push with Braze » (Intégrer les notifications push avec Braze), et « Enable background push » (Activer les notifications push en arrière-plan) sont activés.][29]

### (Facultatif) : Désactiver l’enregistrement automatique

Les utilisateurs qui n’ont pas encore opté pour des notifications push seront automatiquement autorisés aux notifications push lors de l’ouverture de votre application. Pour désactiver cette fonction et enregistrer manuellement les utilisateurs pour les notifications push, vérifiez **Désactiver l’enregistrement automatique des notifications push**.

- Si **Désactiver l’autorisation provisoire** n’est pas coché sur iOS 12 version ultérieure, l’utilisateur sera provisoirement (en silence) autorisé à recevoir une notification push silencieuse. Si cette option est cochée, l’utilisateur affiche l’invite de notification push native.
- Si vous devez configurer exactement quand l’invite est affichée lors de l’exécution, désactivez l’enregistrement automatique de l’éditeur de configuration Braze et utilisez `AppboyBinding.PromptUserForPushPermissions()` à la place.

![L’éditeur Unity affiche les options de configuration Braze. Dans cet éditeur, « Automate Unity iOS integration » (Automatiser l’intégration d’Unity iOS), « integrate push with braze » (Intégrer les notifications push avec Braze), et « disable automatic push registration » (Désactiver l’enregistrement automatique des notifications push) sont activés.][28]

## Étape 3 : Définir les auditeurs de notifications push

Si vous souhaitez transmettre des charges utiles de notification push à Unity ou prendre des mesures supplémentaires lorsqu’un utilisateur reçoit une notification push, Braze offre la possibilité de définir des auditeurs de notification push.

### L’auditeur a reçu la notification push

L’auditeur reçu est déclenché lorsqu’un utilisateur reçoit une notification push tout en utilisant activement l’application (c’est-à-dire, l’application est à l’avant-plan). Définissez l’auditeur de notification push reçu dans l’éditeur de configuration Braze. Si vous devez configurer votre auditeur d’objet de jeu lors de l’exécution, utilisez `AppboyBinding.ConfigureListener()` et spécifiez `BrazeUnityMessageType.PUSH_RECEIVED`.

![L’éditeur Unity affiche les options de configuration Braze. Dans cet éditeur, l’option « Définir l’écouteur de notification push reçue » est étendue, et le « Nom de l’objet de jeu » (AppBoyCallback) et « Nom de la méthode de fonction de rappel » (PushNotificationReceivedCallback) sont fournis.][30]

### Auditeur ouvert de notification push

L’auditeur ouvert est déclenché lorsqu’un utilisateur lance l’application en cliquant sur une notification push. Pour envoyer la charge utile de notification push à Unity, définissez le nom de votre objet de jeu et appuyez sur la méthode de rappel de l’écoute ouverte sous l’option **Définir l’auditeur ouvert de notifications push** :

![L’éditeur Unity affiche les options de configuration Braze. Dans cet éditeur, l’option « Définir l’écouteur de notification push reçue » est étendue, et le « Nom de l’objet de jeu » (AppBoyCallback) et « Nom de la méthode de fonction de rappel » (PushNotificationOpenedCallback) sont fournis.][31]

Si vous devez configurer votre auditeur d’objet de jeu lors de l’exécution, utilisez `AppboyBinding.ConfigureListener()` et spécifiez `BrazeUnityMessageType.PUSH_OPENED`.

### Exemple d’implémentation d’auditeur de notification push

L’exemple suivant implémente l’objet de jeu `AppboyCallback` utilisant respectivement un nom de méthode de rappel de `PushNotificationReceivedCallback` et `PushNotificationOpenedCallback`.

![Ce graphique d’exemple d’implémentation montre les options de configuration Braze mentionnées dans les sections précédentes et un extrait de code C#.][32]

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

Pour recevoir une copie des jetons de périphérique de Braze à partir du système d’exploitation, définissez un délégué à l’aide de `AppboyBinding.SetPushTokenReceivedFromSystemDelegate()`.

### Autres fonctions

Pour implémenter des fonctionnalités avancées telles que des liens profonds, des nombres de badges et des sons personnalisés, consultez notre [instructions de notifications push iOS natives][8].

[1]: #manual-push-integration
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/unity/sdk_integration/ios/#transitioning-from-manual-to-automated-integration-ios
[8]: {{site.baseurl}}/developer_guide/platform_integration_guides/unity/push_notifications/ios/
[9]: https://developer.apple.com/ios/manage/overview/index.action "iOS Provisioning Portal"
[10]: {% image_buster /assets/img_archive/ios_provisioning.png %} "pushNotification2.png"
[11]: {% image_buster /assets/img_archive/AppleProvisioningOptions.png %} "AppleProvisioningOptions.png"
[12]: {% image_buster /assets/img_archive/push_cert_gen.png %} "pushNotification3.png"
[15]: https://github.com/Appboy/appboy-unity-sdk/blob/master/unity-samples/iOS/Roll-A-Ball-Ios/Classes/UnityAppController.mm "sample AppController.mm"
[24]: {% image_buster /assets/img_archive/Enable_push_capabilities.png %}
[27]: {% image_buster /assets/img/unity/ios/unity_ios_api_key.png %}
[28]: {% image_buster /assets/img/unity/ios/unity_ios_disable_auto_push.png %}
[29]: {% image_buster /assets/img/unity/ios/unity_ios_enable_background.png %}
[30]: {% image_buster /assets/img/unity/ios/unity_ios_push_received.png %}
[31]: {% image_buster /assets/img/unity/ios/unity_ios_push_opened.png %}
[32]: {% image_buster /assets/img/unity/ios/unity_ios_appboy_callback.png %}