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

Ces instructions concernent l'intégration de push avec [Firebase Cloud Messaging (FCM).](https://firebase.google.com/docs/cloud-messaging/)

Consultez notre documentation Unity [ADM]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/push_notifications/adm_push_notifications/) pour les instructions d'intégration de l'ADM.

## Étape 1 : Activer Firebase

Pour commencer, suivez la [documentation de configuration de Firebase Unity](https://firebase.google.com/docs/unity/setup).

{% alert note %}
L’intégration du SDK Firebase Unity peut entraîner le remplacement de votre `AndroidManifest.xml`. Si cela se produit, assurez-vous de revenir à l’original.
{% endalert %}

## Étape 2 : Définir vos informations d’identification Firebase

Vous devez saisir votre clé de serveur Firebase et votre ID d’expéditeur dans le tableau de bord de Braze : Pour ce faire, connectez-vous à la [Firebase Developers Console](https://console.firebase.google.com/) et sélectionnez votre projet Firebase. Ensuite, sélectionnez l'option **Cloud Messaging** sous **Settings** et copiez la clé du serveur et l'ID de l'expéditeur :<br>![]({% image_buster /assets/img_archive/finding_firebase_server_key.png %} "FirebaseServerKey")

Dans Braze, sélectionnez votre application Android sur la page **Paramètres de l'application**, sous **Gérer les paramètres**. Saisissez ensuite votre clé de serveur Firebase dans le champ **Clé du serveur Firebase Cloud Messaging** et ID d’expéditeur Firebase dans le champ ID **Expéditeur de Firebase Cloud Messaging**.

![]({% image_buster /assets/img_archive/fcm_api_insert.png %} "FCMKey")

## Étape 3 : Implémenter l’intégration de notification push automatique

Le SDK Braze peut gérer automatiquement l’enregistrement des notifications push avec les serveurs Firebase Cloud Messaging pour que les appareils reçoivent des notifications push.

![L’éditeur Unity affiche les options de configuration Braze. Dans cet éditeur, « Automatiser l’intégration d’Android Unity », « Notification Push Firebase Push », « Configuration Push gère les liens profonds Push automatiquement », « Configuration Push Rendu HTML des notification push activé » et « Définir les auditeurs Push Deleted/Opened/Received » sont définis. Les champs "Firebase Sender ID", "Small/Large Icon Drawable", "Default Notification Accent Color" sont également fournis.]({% image_buster /assets/img/unity/android/unity_android_push_settings_config.png %} "Android Push Settings")

- **Activation de l'enregistrement automatique de l'envoi de messages dans le nuage Firebase**<br> Donne l’ordre au SDK Braze de récupérer et d’envoyer automatiquement un jeton de notification push FCM pour un appareil. 
- **ID de l’expéditeur de Firebase Cloud Messaging**<br> L’identifiant de l’expéditeur provenant de votre console Firebase.
- **Manipulez automatiquement les liens profonds (Push Deeplinks)**<br> Si le SDK doit traiter des liens profonds ou ouvrir l’application lorsque des notifications push sont cliquées.
- **Petite icône de notification dessinable**<br>Le drawable doit être affiché comme petite icône chaque fois qu’une notification push est reçue. La notification utilisera l’icône de l’application comme petite icône si aucune icône n’est fournie.

## Étape 4 : Définir les auditeurs de notifications push

Si vous souhaitez transmettre des charges utiles de notification push à Unity ou prendre des mesures supplémentaires lorsqu’un utilisateur reçoit une notification push, Braze offre la possibilité de définir des auditeurs de notification push.

Dans Braze, sélectionnez votre application Android sur la page **Paramètres de l'application**, sous **Gérer les paramètres**. Saisissez ensuite votre clé de serveur Firebase dans le champ **Paramètres des notifications push** et ID d’expéditeur Firebase dans le champ ID **Paramètres des notifications push**.

#### L’auditeur a reçu la notification push

L’auditeur de notification push reçu est déclenché lorsqu’un utilisateur reçoit une notification push. Pour envoyer la charge utile push à Unity, définissez le nom de votre objet de jeu et poussez la méthode de rappel de l'auditeur reçu sous la rubrique **Définir l'auditeur reçu des notifications push**.

#### Auditeur ouvert de notification push

L’auditeur ouvert est déclenché lorsqu’un utilisateur lance l’application en cliquant sur une notification push. Pour envoyer la charge utile de notification push à Unity, définissez le nom de votre objet de jeu et appuyez sur la méthode de rappel de l’écoute ouverte dans **Définir l’auditeur ouvert de notifications push**.

#### Auditeur push supprimé (Android uniquement)

L’auditeur push supprimé est déclenché lorsqu’un utilisateur balaye ou rejette une notification push. Pour envoyer la charge utile push à Unity, définissez le nom de votre objet de jeu et la méthode de rappel push deleted listener sous la rubrique **Définir l’auditeur supprimé des notifications push**.

#### Exemple d’implémentation d’auditeur de notification push

L’exemple suivant implémente l’objet de jeu `BrazeCallback` utilisant respectivement un nom de méthode de rappel de `PushNotificationReceivedCallback`, `PushNotificationOpenedCallback`, et `PushNotificationDeletedCallback`.

![Cet exemple d'implémentation graphique présente les options de configuration de Braze mentionnées dans les sections précédentes ainsi qu'un extrait de code C#.]({% image_buster /assets/img/unity/android/unity_android_full_push_listener.png %} "Android Full Listener Example")

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

L’exemple de projet dans le [référentiel du SDK Unity de Braze](https://github.com/Appboy/appboy-unity-sdk/tree/master/unity-samples) contient un exemple d’application parfaitement fonctionnelle incluant FCM.

## Ressources liens profonds vers in-app

Bien que Braze puisse gérer des liens profonds standard par défaut (tels que les URL de sites Internet, les URI Android, etc.), la création de liens profonds personnalisés nécessite une configuration du Manifeste supplémentaire.

Pour obtenir des conseils sur la configuration, consultez la page [Création de liens profonds vers des ressources In-App](https://developer.android.com/training/app-links/deep-linking).

## Ajout d'icônes de notification push Braze

Pour ajouter des icônes push à votre projet, créez un plug-in Android Archive (AAR) ou une bibliothèque Android contenant les fichiers d'image des icônes. Pour connaître les étapes et les informations, reportez-vous à la documentation d'Unity : [Projets de bibliothèques Android et plug-ins Android Archive](https://docs.unity3d.com/Manual/AndroidAARPlugins.html).