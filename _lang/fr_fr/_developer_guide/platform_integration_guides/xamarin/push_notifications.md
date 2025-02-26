---
nav_title: Notifications push
article_title: Notifications push pour Xamarin
platform: 
  - Xamarin
  - iOS
  - Android
page_order: 1
description: "Cet article couvre l’intégration de notifications push sur Android, FireOS et iOS pour la plate-forme Xamarin."
channel: push
toc_headers: h2
---

# Intégration de notifications Push

> Découvrez comment configurer les notifications push Android, FireOS et iOS pour Xamarin.

## Conditions préalables

Pour utiliser cette fonctionnalité, vous devrez [intégrer le SDK Braze pour la plateforme Xamarin]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/initial_sdk_setup/).

## Intégration des notifications push

{% tabs %}
{% tab android %}
{% alert tip %}
Pour voir comment les espaces de noms changent entre Java et C#, consultez notre [exemple d'application Xample sur GitHub](https://github.com/braze-inc/braze-xamarin-sdk/tree/master/appboy-component/samples/android-net-maui/BrazeAndroidMauiSampleApp/BrazeAndroidMauiSampleApp).
{% endalert %}

Pour intégrer les notifications push pour Xamarin, vous devrez suivre les étapes pour les notifications push Android natives. Les étapes suivantes ne sont qu'un résumé. Pour une présentation complète, consultez le [guide sur les notifications push natives]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/).

### Étape 1 : Mettre à jour votre projet

1. Ajoutez Firebase à votre projet Android.
2. Ajoutez la bibliothèque Cloud Messaging au `build.gradle` de votre projet Android :
  ```gradle
  implementation "google.firebase:firebase-messaging:+"
  ```

### Étape 2 : Créez vos identifiants JSON

1. Dans Google Cloud, activez l'[API Firebase Cloud Messaging](https://console.cloud.google.com/apis/library/fcm.googleapis.com).
2. Sélectionnez **Comptes de service** > votre projet > **Créer un compte de service**, puis saisissez un nom de compte de service, un ID et une description. Lorsque vous avez terminé, sélectionnez **Créer et continuer**.
3. Dans le champ **Rôle**, recherchez et sélectionnez **Firebase Cloud Messaging API Admin** dans la liste des rôles.
4. Dans **Comptes de service**, choisissez votre projet, puis sélectionnez <i class="fa-solid fa-ellipsis-vertical"></i> **Actions** > **Gérer les clés** > **Ajouter une clé** > **Créer une nouvelle clé**. Choisissez **JSON**, puis sélectionnez **Créer**.

### Étape 3 : Téléchargez vos informations d'identification JSON

1. Dans Braze, sélectionnez <i class="fa-solid fa-gear"></i> **Paramètres** > **Paramètres des applications**. Sous les **paramètres de notifications push** de votre application Android, choisissez **Firebase**, puis sélectionnez **Charger un fichier JSON** et chargez les identifiants que vous avez générés précédemment. Lorsque vous avez terminé, sélectionnez **Enregistrer.**
2. Activez l'enregistrement automatique des jetons FCM à partir de la console Firebase. Ouvrez votre projet, puis sélectionnez <i class="fa-solid fa-gear"></i> **Paramètres** > **Paramètres du projet**. Sélectionnez **Cloud Messaging**, puis sous **API Firebase Cloud Messaging (V1)**, copiez le numéro dans le champ **ID de l'expéditeur**.
3. Dans votre projet Android Studio, ajoutez ce qui suit à votre `braze.xml`.

  ```xml
  <bool translatable="false" name="com_braze_firebase_cloud_messaging_registration_enabled">true</bool>
  <string translatable="false" name="com_braze_firebase_cloud_messaging_sender_id">FIREBASE_SENDER_ID</string>
  ```

{% alert important %}
Pour éviter que Braze ne déclenche des requêtes réseau inutiles à chaque fois que vous envoyez des notifications push silencieuses, supprimez toutes les requêtes réseau automatiques configurées dans la méthode `onCreate()` de votre classe `Application`. Pour plus d'informations, consultez [Référence pour les développeurs Android : Application](https://developer.android.com/reference/android/app/Application).
{% endalert %}
{% endtab %}

{% tab ios %}
### Étape 1 : Terminer la configuration initiale

Consultez les [instructions d'intégration de Swift]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration) pour obtenir des informations sur la configuration de votre application avec push et le stockage de vos identifiants sur notre serveur. Reportez-vous à l'exemple d'application [iOS MAUI](https://github.com/braze-inc/braze-xamarin-sdk/tree/master/appboy-component/samples/ios-net-maui/BrazeiOSMauiSampleApp) pour plus de détails.

### Étape 2 : Demander une autorisation de notification push

Notre SDK Xamarin prend désormais en charge la configuration automatique du push. Configurez l'automatisation du push et les autorisations en ajoutant le code suivant à la configuration de votre instance Braze :

```csharp
configuration.Push.Automation = new BRZConfigurationPushAutomation(true);
configuration.Push.Automation.RequestAuthorizationAtLaunch = false;
```

Reportez-vous à l'exemple d'application [iOS MAUI](https://github.com/braze-inc/braze-xamarin-sdk/tree/master/appboy-component/samples/ios-net-maui/BrazeiOSMauiSampleApp) pour plus de détails. Pour plus de détails, consultez la documentation Xamarin relative aux [notifications utilisateur améliorées sur Xamarin.iOS](https://learn.microsoft.com/en-us/previous-versions/xamarin/ios/platform/user-notifications/enhanced-user-notifications?tabs=macos).
{% endtab %}
{% endtabs %}
