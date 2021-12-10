---
nav_title: Android
article_title: Notifications push Android pour l'unité
platform:
  - Unité
  - Android
channek: Pousser
page_order: 1
description: "Cet article de référence couvre l'intégration des notifications push d'Android pour la plate-forme Unity."
---

# Notifications push

Ces instructions sont pour intégrer push avec [Firebase Cloud Messaging (FCM)][9].

Pour les instructions d'intégration ADM, reportez-vous à notre documentation [Unity ADM][64].

## Étape 1 : Activer Firebase

Pour commencer, suivez les instructions à [Firebase Unity Setup Docs][11].

Notez que l'intégration du SDK Firebase Unity peut causer le dépassement de votre `AndroidManifest.xml`. Si cela se produit, assurez-vous de revenir à son moi original.

## Étape 2 : Définissez vos identifiants Firebase

Vous devez entrer votre clé de serveur Firebase et votre identifiant Sender dans le tableau de bord Braze :

* Sur la page des paramètres de l'application (où se trouvent vos clés API), sélectionnez votre application Android.
* Entrez votre clé de serveur Firebase dans le champ "Firebase Cloud Messaging Server Key" dans la section Paramètres de notification Push.
* Entrez votre identifiant Firebase Sender dans le champ intitulé "Firebase Cloud Messaging Sender ID" dans la section Paramètres des notifications Push.

!\[FCMKey\]\[15\]

Si vous n'êtes pas familier avec l'emplacement de votre clé de serveur Firebase et de l'identifiant de l'expéditeur, suivez ces étapes :

1. Connectez-vous à la [Console de Développeurs Firebase][58]

2. Sélectionnez votre projet Firebase

3. Sélectionnez la messagerie dans le Cloud sous Paramètres et copiez la clé du serveur et l'identifiant de l'expéditeur : !\[FirebaseServerKey\]\[59\]

## Étape 3 : Implémenter l'intégration automatique de push

Le Braze SDK peut automatiquement gérer l'enregistrement push avec les serveurs de messagerie Firebase Cloud afin que les appareils reçoivent des notifications push.

!\[AndroidPushSettings\]\[62\]

- **"Enregistrement automatique de messagerie Firebase Cloud activé"**

Demande au SDK Braze de récupérer et d'envoyer automatiquement un jeton de push FCM pour un appareil.

- **"Firebase Cloud Messaging ID"**

L'ID de l'expéditeur de votre console Firebase.

- **« Manipuler les profondeurs automatiquement »**

Si le SDK doit gérer l'ouverture de profondeurs ou l'ouverture de l'application lorsque les notifications push sont cliquées.

- **"Petite icône de notification dessinable"**

Le dessin qui doit être affiché comme une petite icône à chaque fois qu'une notification push est reçue. Si aucune icône n'est fournie, la notification utilisera l'icône de l'application comme une petite icône.

## Étape 4 : Définir les écouteurs push

Si vous souhaitez passer des payloads de notification push à Unity ou prendre des mesures supplémentaires lorsqu'un utilisateur reçoit une notification push, Braze offre la possibilité de régler les écouteurs de notification push.

* Sur la page **Paramètres** (où se trouvent vos clés API), sélectionnez votre application Android.
* Entrez votre clé de serveur Firebase dans le champ **Firebase Cloud Messaging Server Key** , dans la section Paramètres de notification Push.
* Entrez votre ID de Sender Firebase dans le champ **Firebase Cloud Messaging Sender ID** , dans la section Paramètres de notification Push.

#### Envoyer l'écouteur reçu

L'auditeur push reçu est déclenché lorsqu'un utilisateur reçoit une notification push. Pour envoyer le bloc push à United, définissez le nom de votre méthode de callback d'écoute de Game Object et Push Received sous la rubrique "Set Push Received Listener".

#### Envoyer l'écouteur ouvert

L'auditeur ouvert Push est déclenché lorsqu'un utilisateur lance l'application en cliquant sur une notification push. Pour envoyer le bloc push à United, définissez le nom de votre méthode de rappel de Game Object et Push Opened listener sous la rubrique "Set Push Opened Listener".

#### Envoyer l'écouteur supprimé (Android uniquement)

L'auditeur supprimé est déclenché lorsqu'un utilisateur glisse ou rejette une notification push. Pour envoyer le bloc push à United, définissez le nom de votre méthode de callback d'écoute de Game Object and Push Deleted listener dans la section "Set Push Supted Listener".

#### Exemple d'implémentation de l'écouteur push

L'exemple suivant implémente l'objet `BrazeCallback` en utilisant un nom de méthode de rappel de `PushNotificationReceivedCallback`, `PushNotificationOpenedCallback`, et `PushNotificationDeletedCallback` respectivement.

!\[Game Object Linking\]\[63\]

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

  void PushNotificationDeletedCallback(string message) {
#if UNITY_ANDROID
    Debug. og("PushNotificationDeletedCallback message: " + message);
    PushNotification pushNotification = new PushNotification(message);
    Debug. og("Notification push rejetée : " + pushNotification);  
#endif
  }
}
```

### Exemple d'implémentation

Le projet d'exemple dans le dépôt [Braze Unity SDK][13] contient un exemple d'application fonctionnelle qui inclut FCM.

## Liaison profonde vers les ressources de l'application

Bien que Braze puisse gérer les liens profonds standards (comme les urls de site web, uris Android, etc. hors de la boîte, la création de liens profonds personnalisés nécessite une configuration supplémentaire de Manifest .

Voir la documentation d'Android sur [« Deep Linking» pour les ressources In-App][26]
[15]: {% image_buster /assets/img_archive/fcm_api_insert.png %} "FCMKey" [59]: {% image_buster /assets/img_archive/finding_firebase_server_key.png %} "FirebaseServerKey" [62]: {% image_buster /assets/img/unity/android/unity_android_push_settings_config. ng %} "Paramètres de poussée d'Android" [63]: {% image_buster /assets/img/unity/android/unity_android_full_push_listener.png %} "Exemple Android Full Listener Example"

[9]: https://firebase.google.com/docs/cloud-messaging/
[11]: https://firebase.google.com/docs/unity/setup
[13]: https://github.com/Appboy/appboy-unity-sdk/tree/master/unity-samples
[26]: https://developer.android.com/training/app-links/deep-linking
[58]: https://console.firebase.google.com/
[64]: {{site.baseurl}}/developer_guideplatform_integration_guides/unity/push_notifications/adm_push_notifications/
