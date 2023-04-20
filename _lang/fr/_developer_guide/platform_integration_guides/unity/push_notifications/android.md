---
nav_title: Android
article_title: Notifications push Android pour Unity
platform: 
  - Unity
  - Android
channel: push
page_order: 1
description: "Cet article de référence couvre l’intégration de notifications push Android pour la plateforme Unity."

---

# Intégration de notifications Push pour Android

> Cet article de référence couvre l’intégration de notifications push Android pour la plateforme Unity.

Ces instructions sont destinées à intégrer les notifications push à [Firebase Cloud Messaging (FCM)][9].

Voir notre documentation [ADM Unity][64] pour les instructions d’intégration ADM.

## Étape 1 : Activer Firebase

Pour commencer, suivez la [Documentation de configuration de Firebase Unity][11].

{% alert note %}
L’intégration du SDK Firebase Unity peut entraîner le remplacement de votre `AndroidManifest.xml`. Si cela se produit, assurez-vous de revenir à l’original.
{% endalert %}

## Étape 2 : Définir vos informations d’identification Firebase

Vous devez saisir votre clé de serveur Firebase et votre ID d’expéditeur dans le tableau de bord de Braze : Pour ce faire, connectez-vous à la [Console Firebase Developers][58] et sélectionnez votre projet Firebase. Ensuite, sélectionnez **Cloud Messaging** dans **Paramètres** et copiez la clé serveur et l’ID de l’expéditeur :<br>![][59]

Dans Braze, sélectionnez votre application Android sur la page **Configuration de l’application** dans **Gérer les paramètres**. Saisissez ensuite votre clé de serveur Firebase dans le champ **Clé du serveur de messagerie cloud Firebase** et ID d’expéditeur Firebase dans le champ ID **Expéditeur de messagerie cloud Firebase**.

![][15]

## Étape 3 : Implémenter l’intégration de notification push automatique

Le SDK Braze peut gérer automatiquement l’enregistrement des notifications push avec les serveurs Firebase Cloud Messaging pour que les périphériques reçoivent des notifications push.

![L’éditeur Unity affiche les options de configuration Braze. Dans cet éditeur, « Automatiser l’intégration d’Android Unity », « Notification Push Firebase Push », « Configuration Push gère les liens profonds Push automatiquement », « Configuration Push Rendu HTML des notification push activé » et « Définir les auditeurs Push Supprimé/Ouvert/Reçu » sont définis. Les champs « Firebase Sender ID » (ID expéditeur Firebase), « Small/Grand Icon » (Possibilité de retrait de petite/grande icône), « Default Notification Accent Color » (Couleur de la notification par défaut) sont également fournis.][62]

- **Enregistrement automatique de Firebase Cloud Messaging activé**<br> Donne l’ordre au SDK Braze de récupérer et d’envoyer automatiquement un jeton de notification push FCM pour un appareil. 
- **ID de l’expéditeur de Firebase Cloud Messaging**<br> L’identifiant de l’expéditeur provenant de votre console Firebase.
- **Traite les liens ciblés des notifications push automatiquement**<br> Si le SDK doit traiter des liens profonds ou ouvrir l’application lorsque des notifications push sont cliquées.
- **Petite icône de notification Drawable**<br>Le drawable doit être affiché comme petite icône chaque fois qu’une notification push est reçue. La notification utilisera l’icône de l’application comme petite icône si aucune icône n’est fournie.

## Étape 4 : Définir les auditeurs de notifications push

Si vous souhaitez transmettre des charges utiles de notification push à Unity ou prendre des mesures supplémentaires lorsqu’un utilisateur reçoit une notification push, Braze offre la possibilité de définir des auditeurs de notification push.

Dans Braze, sélectionnez votre application Android sur la page **Configuration de l’application** dans **Gérer les paramètres**. Saisissez ensuite votre clé de serveur Firebase dans le champ **Paramètres de notification Push** et ID d’expéditeur Firebase dans le champ ID **Paramètres de notification Push**.

#### L’auditeur a reçu la notification push

L’auditeur de notification push reçu est déclenché lorsqu’un utilisateur reçoit une notification push. Pour envoyer la charge utile de notification push à Unity, définissez le nom de votre objet de jeu et appuyez sur la méthode de rappel de l’auditeur reçu sous **Définir l’auditeur reçu de notification push**.

#### Auditeur ouvert de notification push

L’auditeur ouvert est déclenché lorsqu’un utilisateur lance l’application en cliquant sur une notification push. Pour envoyer la charge utile de notification push à Unity, définissez le nom de votre objet de jeu et appuyez sur la méthode de rappel de l’écoute ouverte dans **Définir l’auditeur ouvert de notifications push** :

#### Auditeur push supprimé (Android uniquement)

L’auditeur push supprimé est déclenché lorsqu’un utilisateur balaye ou rejette une notification push. Pour envoyer la charge utile des notifications push à Unity, définissez le nom de votre objet de jeu et la méthode de rappel de l’auditeur supprimé des notifications push dans **Définir l’auditeur supprimé des notifications push**.

#### Exemple d’implémentation d’auditeur de notification push

L’exemple suivant implémente l’objet de jeu `BrazeCallback` utilisant respectivement un nom de méthode de rappel de `PushNotificationReceivedCallback`, `PushNotificationOpenedCallback`, et `PushNotificationDeletedCallback`.

![Ce graphique d’exemple d’implémentation montre les options de configuration Braze mentionnées dans les sections précédentes et un extrait de code C#.][63]

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

  void PushNotificationDeletedCallback(string message) {
#if UNITY_ANDROID
    Debug.Log("PushNotificationDeletedCallback message: " + message);
    PushNotification pushNotification = new PushNotification(message);
    Debug.Log("Push Notification dismissed: " + pushNotification);  
#endif
  }
}
```

### Exemple d’implémentation

Le projet d’échantillon dans le [Référentiel de développement du SDK Braze Unity][13] contient une application parfaitement fonctionnelle incluant FCM.

## Ressources liens profonds vers in-app

Bien que Braze puisse gérer des liens profonds standard par défaut (tels que les URL de sites Internet, les URI Android, etc.), la création de liens profonds personnalisés nécessite une configuration du Manifeste supplémentaire.

Pour obtenir des conseils sur la configuration, consultez [Ressources de liens profonds vers in-app][26].

[8]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/troubleshooting/
[9]: https://firebase.google.com/docs/cloud-messaging/
[11]: https://firebase.google.com/docs/unity/setup
[12]: https://firebase.google.com/docs/android/setup
[13]: https://github.com/Appboy/appboy-unity-sdk/tree/master/unity-samples
[15]: {% image_buster /assets/img_archive/fcm_api_insert.png %} "FCMKey"
[26]: https://developer.android.com/training/app-links/deep-linking
[58]: https://console.firebase.google.com/
[59]: {% image_buster /assets/img_archive/finding_firebase_server_key.png %} "FirebaseServerKey"
[61]: {{site.baseurl}}/developer_guide/platform_integration_guides/unity/advanced_use_cases
[62]: {% image_buster /assets/img/unity/android/unity_android_push_settings_config.png %} "Android Push Settings"
[63]: {% image_buster /assets/img/unity/android/unity_android_full_push_listener.png %} "Android Full Listener Example"
[64]: {{site.baseurl}}/developer_guideplatform_integration_guides/unity/push_notifications/adm_push_notifications/