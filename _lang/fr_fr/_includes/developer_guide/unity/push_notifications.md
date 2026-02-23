{% multi_lang_include developer_guide/prerequisites/unity.md %}

## Mise en place de la notification push

### Étape 1 : Mise en place de la plate-forme

{% tabs %}
{% tab Android %}
#### Étape 1.1 : Activer Firebase

Pour commencer, suivez la [documentation de configuration de Firebase Unity](https://firebase.google.com/docs/unity/setup).

{% alert note %}
L’intégration du SDK Firebase Unity peut entraîner le remplacement de votre `AndroidManifest.xml`. Si cela se produit, assurez-vous de revenir à l’original.
{% endalert %}

#### Étape 1.2 : Définir vos informations d’identification Firebase

Vous devez saisir votre clé de serveur Firebase et votre ID d’expéditeur dans le tableau de bord de Braze : Pour ce faire, connectez-vous à la [Firebase Developers Console](https://console.firebase.google.com/) et sélectionnez votre projet Firebase. Ensuite, sélectionnez l'option **Cloud Messaging** sous **Settings** et copiez la clé du serveur et l'ID de l'expéditeur :<br>![]({% image_buster /assets/img_archive/finding_firebase_server_key.png %} "FirebaseServerKey")

Dans Braze, sélectionnez votre application Android sur la page **Paramètres de l'application**, sous **Gérer les paramètres**. Saisissez ensuite votre clé de serveur Firebase dans le champ **Clé du serveur Firebase Cloud Messaging** et ID d’expéditeur Firebase dans le champ ID **Expéditeur de Firebase Cloud Messaging**.

![]({% image_buster /assets/img_archive/fcm_api_insert.png %} "FCMKey")
{% endtab %}

{% tab Swift %}
#### Étape 1.1 : Vérifier la méthode d'intégration

Braze fournit une solution Unity native pour l’automatisation des intégrations de notifications push iOS. Si vous souhaitez plutôt configurer et gérer votre intégration manuellement, consultez [Swift : Notifications push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift).

Sinon, passez à l'étape suivante.

{% alert note %}
Notre solution de notification push automatique tire parti de la fonctionnalité d’autorisation provisoire d’iOS 12 et n’est pas disponible pour utiliser avec la fenêtre contextuelle d’invite de notification push native.
{% endalert %}
{% endtab %}

{% tab Amazon Device Messaging %}
#### Étape 1.1 : Activer ADM

1. Créez un compte sur le [portail des développeurs Amazon Apps & Games](https://developer.amazon.com/public) si vous ne l'avez pas encore fait.
2. Obtenez les [identifiants OAuth (ID client et secret client) et une clé API ADM](https://developer.amazon.com/public/apis/engage/device-messaging/tech-docs/02-obtaining-adm-credentials).
3. Activez **Enregistrement ADM automatique activé** dans la fenêtre de configuration de Braze Unity. 
  - Vous pouvez également ajouter la ligne suivante à votre `res/values/braze.xml` pour activer l’enregistrement ADM :

  ```xml
  <bool name="com_braze_push_adm_messaging_registration_enabled">true</bool>
  ```
{% endtab %}
{% endtabs %}

### Étape 2 : Configurer les notifications push

{% tabs %}
{% tab Android %}
#### Étape 2.1 : Configurer les paramètres de poussée

Le SDK Braze peut gérer automatiquement l’enregistrement des notifications push avec les serveurs Firebase Cloud Messaging pour que les appareils reçoivent des notifications push. Dans Unity, activez **Automate Unity Android Integration**, puis configurez les paramètres de **notification push** suivants.

| Réglage                                | Description                                                                                                                                              |
|----------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Activation de l'enregistrement automatique de l'envoi de messages dans le nuage Firebase | Donne l’ordre au SDK Braze de récupérer et d’envoyer automatiquement un jeton de notification push FCM pour un appareil.                                                                |
| ID de l’expéditeur de Firebase Cloud Messaging     | L’identifiant de l’expéditeur provenant de votre console Firebase.                                                                                                                |
| Manipulez automatiquement les liens profonds (Push Deeplinks)    | Si le SDK doit traiter des liens profonds ou ouvrir l’application lorsque des notifications push sont cliquées.                                                  |
| Petite icône de notification dessinable       | Le drawable doit être affiché comme petite icône chaque fois qu’une notification push est reçue. La notification utilisera l’icône de l’application comme petite icône si aucune icône n’est fournie. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
{% endtab %}

{% tab Swift %}
#### Étape 2.1 : Téléchargez votre jeton APN

{% multi_lang_include developer_guide/swift/apns_token.md %}

#### Étape 2.2 : Activer la poussée automatique

Ouvrez les paramètres de configuration de Braze dans l'éditeur Unity en sélectionnant **Braze > Configuration Braze**.

Cochez **Intégrer Push avec Braze** pour inscrire automatiquement les utilisateurs aux notifications push, transmettre les jetons push à Braze, suivre l'analyse/analytique des ouvertures de push et tirer parti de notre gestion par défaut des notifications push.

#### Étape 2.3 : Activer la poussée en arrière-plan (facultatif)

Cochez **Enable Background Push** si vous souhaitez activer `background mode` pour les notifications push. Cela permet au système de réveiller votre application à partir de l’état `suspended` lorsqu’une notification push est reçue, permettant à votre application de télécharger le contenu en réponse aux notifications push. Le fait de cocher cette option est nécessaire pour notre fonctionnalité de suivi de la désinstallation.

![L’éditeur Unity affiche les options de configuration Braze. Dans cet éditeur, « Automate Unity iOS integration » (Automatiser l’intégration d’Unity iOS », « Integrate push with Braze » (Intégrer les notifications push avec Braze), et « Enable background push » (Activer les notifications push en arrière-plan) sont activés.]({% image_buster /assets/img/unity/ios/unity_ios_enable_background.png %})

#### Étape 2.4 : Désactiver l'enregistrement automatique (optionnel)

Les utilisateurs qui n’ont pas encore opté pour des notifications push seront automatiquement autorisés aux notifications push lors de l’ouverture de votre application. Pour désactiver cette fonctionnalité et enregistrer manuellement les utilisateurs pour le push, cochez **Désactiver l'enregistrement push automatique.**

- Si la case **Désactiver l'autorisation provisoire** n'est pas cochée sous iOS 12 ou une version ultérieure, l'utilisateur sera provisoirement (silencieusement) autorisé à recevoir le push silencieux. Si cette option est cochée, l’utilisateur affiche l’invite de notification push native.
- Si vous devez configurer exactement quand l’invite est affichée lors de l’exécution, désactivez l’enregistrement automatique de l’éditeur de configuration Braze et utilisez `AppboyBinding.PromptUserForPushPermissions()` à la place.

![L’éditeur Unity affiche les options de configuration Braze. Dans cet éditeur, « Automate Unity iOS integration » (Automatiser l’intégration d’Unity iOS), « integrate push with braze » (Intégrer les notifications push avec Braze), et « disable automatic push registration » (Désactiver l’enregistrement automatique des notifications push) sont activés.]({% image_buster /assets/img/unity/ios/unity_ios_disable_auto_push.png %})
{% endtab %}

{% tab Amazon Device Messaging %}
#### Étape 2.1 : Mise à jour `AndroidManifest.xml`

Si votre application n’a pas de `AndroidManifest.xml`, vous pouvez utiliser ce qui suit comme modèle. Sinon, si vous avez déjà un `AndroidManifest.xml`, assurez-vous que l’une des sections manquantes suivantes est ajoutée à votre `AndroidManifest.xml` existant.

```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
          package="REPLACE_WITH_YOUR_PACKAGE_NAME">

  <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
  <uses-permission android:name="android.permission.INTERNET" />
  <permission
    android:name="REPLACE_WITH_YOUR_PACKAGE_NAME.permission.RECEIVE_ADM_MESSAGE"
    android:protectionLevel="signature" />
  <uses-permission android:name="REPLACE_WITH_YOUR_PACKAGE_NAME.permission.RECEIVE_ADM_MESSAGE" />
  <uses-permission android:name="com.amazon.device.messaging.permission.RECEIVE" />

  <application android:icon="@drawable/app_icon" 
               android:label="@string/app_name">

    <!-- Calls the necessary Braze methods to ensure that analytics are collected and that push notifications are properly forwarded to the Unity application. -->
    <activity android:name="com.braze.unity.BrazeUnityPlayerActivity" 
      android:label="@string/app_name" 
      android:configChanges="fontScale|keyboard|keyboardHidden|locale|mnc|mcc|navigation|orientation|screenLayout|screenSize|smallestScreenSize|uiMode|touchscreen" 
      android:screenOrientation="sensor">
      <meta-data android:name="android.app.lib_name" android:value="unity" />
      <meta-data android:name="unityplayer.ForwardNativeEventsToDalvik" android:value="true" />
      <intent-filter>
        <action android:name="android.intent.action.MAIN" />
        <category android:name="android.intent.category.LAUNCHER" />
      </intent-filter>
    </activity>

    <receiver android:name="com.braze.push.BrazeAmazonDeviceMessagingReceiver" android:permission="com.amazon.device.messaging.permission.SEND">
      <intent-filter>
          <action android:name="com.amazon.device.messaging.intent.RECEIVE" />
          <action android:name="com.amazon.device.messaging.intent.REGISTRATION" />
          <category android:name="REPLACE_WITH_YOUR_PACKAGE_NAME" />
      </intent-filter>
    </receiver>
  </application>
</manifest>
```

#### Étape 2.2 : Stocker votre clé API ADM

Tout d'abord, [générez une clé API ADM pour votre application](https://developer.amazon.com/public/apis/engage/device-messaging/tech-docs/02-obtaining-adm-credentials), puis enregistrez la clé dans un fichier nommé `api_key.txt` et ajoutez-le dans le répertoire [`Assets/`](https://docs.unity3d.com/Manual/AndroidAARPlugins.html) de votre projet.

{% alert important %}
Amazon ne reconnaîtra pas votre clé si `api_key.txt` contient des caractères blancs, comme un saut de ligne.
{% endalert %}

Ensuite, dans votre fichier `mainTemplate.gradle`, ajoutez ce qui suit :

```gradle
task copyAmazon(type: Copy) {
    def unityProjectPath = $/file:///**DIR_UNITYPROJECT**/$.replace("\\", "/")
    from unityProjectPath + '/Assets/api_key.txt'
    into new File(projectDir, 'src/main/assets')
}

preBuild.dependsOn(copyAmazon)
```

#### Étape 2.3 : Ajouter un Jar ADM

Le fichier Jar ADM requis peut être placé n'importe où dans votre projet, conformément à la [documentation JAR d'Unity](https://docs.unity3d.com/Manual/AndroidJARPlugins.html).

#### Étape 2.4 : Ajouter un identifiant secret client et un identifiant client à votre tableau de bord de Braze

Enfin, vous devez ajouter le Secret Client et l'ID Client que vous avez obtenus dans [l'Étape 1](#unity_step-1-enable-adm) à la page **Gérer les paramètres** du tableau de bord de Braze.

![]({% image_buster /assets/img_archive/fire_os_dashboard.png %})
{% endtab %}
{% endtabs %}

### Étape 3 : Définir les auditeurs de notifications push

{% tabs %}
{% tab Android %}
#### Étape 3.1 : Activer l'écoute des messages reçus par push

L’auditeur de notification push reçu est déclenché lorsqu’un utilisateur reçoit une notification push. Pour envoyer la charge utile push à Unity, définissez le nom de votre objet de jeu et poussez la méthode de rappel de l'auditeur reçu sous la rubrique **Définir l'auditeur reçu des notifications push**.

#### Étape 3.2 : Activation de l'auditeur push ouvert

L’auditeur ouvert est déclenché lorsqu’un utilisateur lance l’application en cliquant sur une notification push. Pour envoyer la charge utile de notification push à Unity, définissez le nom de votre objet de jeu et appuyez sur la méthode de rappel de l’écoute ouverte dans **Définir l’auditeur ouvert de notifications push**.

#### Étape 3.3 : Activation de l'auditeur "push deleted

L’auditeur push supprimé est déclenché lorsqu’un utilisateur balaye ou rejette une notification push. Pour envoyer la charge utile push à Unity, définissez le nom de votre objet de jeu et la méthode de rappel push deleted listener sous la rubrique **Définir l’auditeur supprimé des notifications push**.

#### Exemple d'écoute push

L’exemple suivant implémente l’objet de jeu `BrazeCallback` utilisant respectivement un nom de méthode de rappel de `PushNotificationReceivedCallback`, `PushNotificationOpenedCallback`, et `PushNotificationDeletedCallback`.

![Ce graphique d’exemple d’implémentation montre les options de configuration Braze mentionnées dans les sections précédentes et un extrait de code C#.]({% image_buster /assets/img/unity/android/unity_android_full_push_listener.png %} "Android Full Listener Example")

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
{% endtab %}

{% tab Swift %}
#### Étape 3.1 : Activer l'écoute des messages reçus par push

Le récepteur push reçu est déclenché lorsqu'un utilisateur reçoit une notification push alors qu'il utilise activement l'application (par exemple, lorsque l'application est au premier plan). Définissez l’auditeur de notification push reçu dans l’éditeur de configuration Braze. Si vous devez configurer votre auditeur d’objet de jeu lors de l’exécution, utilisez `AppboyBinding.ConfigureListener()` et spécifiez `BrazeUnityMessageType.PUSH_RECEIVED`.

![L’éditeur Unity affiche les options de configuration Braze. Dans cet éditeur, l’option « Set Push Received Listener » (Définir l’écoute reçue par le push) est étendue, et le « Game Object Name » (Nom de l’objet de jeu) et « Callback Method Name » (Nom de la méthode de rappel) (PushNotificationAdministredCallback) sont fournis.]({% image_buster /assets/img/unity/ios/unity_ios_push_received.png %})

#### Étape 3.2 : Activation de l'auditeur push ouvert

L’auditeur ouvert est déclenché lorsqu’un utilisateur lance l’application en cliquant sur une notification push. Pour envoyer la charge utile de notifications push à Unity, définissez le nom de votre objet de jeu et de la méthode de rappel d’écoute ouverte des notifications push sous l’option **Définir l’auditeur ouvert de notifications push** :

![L’éditeur Unity affiche les options de configuration Braze. Dans cet éditeur, l’option « Set Push Received Listener » (Définir l’écoute reçue par le push) est étendue, et le « Game Object Name » (Nom de l’objet de jeu) et « Callback Method Name » (Nom de la méthode de rappel) (PushNotificationOpenedCallback) sont fournis.]({% image_buster /assets/img/unity/ios/unity_ios_push_opened.png %})

Si vous devez configurer votre auditeur d’objet de jeu lors de l’exécution, utilisez `AppboyBinding.ConfigureListener()` et spécifiez `BrazeUnityMessageType.PUSH_OPENED`.

#### Exemple d'écoute push

L’exemple suivant implémente l’objet de jeu `AppboyCallback` utilisant respectivement un nom de méthode de rappel de `PushNotificationReceivedCallback` et `PushNotificationOpenedCallback`.

![Ce graphique d’exemple d’implémentation montre les options de configuration Braze mentionnées dans les sections précédentes et un extrait de code C#.]({% image_buster /assets/img/unity/ios/unity_ios_appboy_callback.png %})

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
{% endtab %}

{% tab Amazon Device Messaging %}
En mettant à jour votre site `AndroidManifest.xml` à l'[étape précédente](#unity_step-21-update-androidmanifestxml), des "push listeners" ont été automatiquement mis en place lorsque vous avez ajouté les lignes suivantes. Aucune autre configuration n'est donc nécessaire.

```xml
<action android:name="com.amazon.device.messaging.intent.RECEIVE" />
<action android:name="com.amazon.device.messaging.intent.REGISTRATION" />
```

{% alert note %}
Pour en savoir plus sur les "push listeners" d'ADM, consultez le site [Amazon : Intégrer l'envoi de messages des appareils Amazon](https://developer.amazon.com/docs/video-skills-fire-tv-apps/integrate-adm.html).
{% endalert %}
{% endtab %}
{% endtabs %}

## Configurations optionnelles

{% tabs %}
{% tab Android %}
#### Ressources liens profonds vers in-app

Bien que Braze puisse gérer des liens profonds standard par défaut (tels que les URL de sites Internet, les URI Android, etc.), la création de liens profonds personnalisés nécessite une configuration du Manifeste supplémentaire.

Pour obtenir des conseils sur la configuration, consultez la page [Création de liens profonds vers des ressources In-App](https://developer.android.com/training/app-links/deep-linking).

#### Ajout d'icônes de notification push Braze

Pour ajouter des icônes push à votre projet, créez un plug-in Android Archive (AAR) ou une bibliothèque Android contenant les fichiers d'image des icônes. Pour connaître les étapes et les informations, reportez-vous à la documentation d'Unity : [Projets de bibliothèques Android et plug-ins Android Archive](https://docs.unity3d.com/Manual/AndroidAARPlugins.html).
{% endtab %}

{% tab Swift %}
#### Fonction de rappel de jeton de notification push

Pour recevoir une copie des jetons d'appareil de Braze à partir du système d'exploitation, définissez un délégué à l'aide de `AppboyBinding.SetPushTokenReceivedFromSystemDelegate()`.
{% endtab %}

{% tab Amazon Device Messaging %}
Il n'y a pas de configurations optionnelles pour ADM à l'heure actuelle.
{% endtab %}
{% endtabs %}
