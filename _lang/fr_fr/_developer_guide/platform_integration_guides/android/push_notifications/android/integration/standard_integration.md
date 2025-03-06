---
nav_title: Intégration standard
article_title: Intégration de notifications push standard pour Android
platform: Android
page_order: 0
description: "Cet article explique comment intégrer des notifications push dans votre application Android."
channel:
  - push
search_rank: 3
---

# Intégration de notification push Android standard

> Découvrez comment intégrer les notifications push dans votre application Android.

Grâce aux notifications push, vous pouvez réengager les utilisateurs de votre application en envoyant des contenus pertinents et sensibles au facteur temps directement sur l'écran de leur appareil, même si leur application est fermée. Lorsque vous aurez terminé l'intégration de push pour votre application, n'oubliez pas de consulter nos [meilleures pratiques en matière de push.]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/)

{% alert important %}
Si votre intégration de notifications push Android est déjà en place et que vous souhaitez migrer de l'API obsolète Cloud Messaging de Google, consultez la section [Migration vers l'API Firebase Cloud Messaging]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/migrating_to_firebase_cloud_messaging).
{% endalert %}

## Limite de débit

L'API Firebase Cloud Messaging (FCM) présente une limite de débit par défaut de 600 000 requêtes par minute. Si vous atteignez cette limite, Braze réessaiera automatiquement dans quelques minutes. Pour demander une augmentation, contactez le [service d'assistance de Firebase.](https://firebase.google.com/support)

## S’enregistrer pour la notification push

Dans cette section, vous apprendrez à vous enregistrer pour les notifications push à l'aide de l'API Firebase Cloud Messaging (FCM) de Google. Si vous souhaitez voir un exemple d'application utilisant FCM avec le SDK Android de Braze, consultez [Braze : Exemple d'application Firebase Push](https://github.com/braze-inc/braze-android-sdk/tree/master/samples/firebase-push).

### Étape 1 : Ajoutez Firebase à votre projet

Tout d'abord, ajoutez Firebase à votre projet Android. Pour obtenir des instructions pas à pas, consultez le [guide de configuration de Firebase](https://firebase.google.com/docs/android/setup) de Google.

### Étape 2 : Ajoutez Cloud Messaging à vos dépendances

Ensuite, ajoutez la bibliothèque Cloud Messaging aux dépendances de votre projet. Dans votre projet Android, ouvrez `build.gradle`, puis ajoutez la ligne suivante à votre bloc `dependencies`.

```gradle
implementation "google.firebase:firebase-messaging:+"
```

Vos dépendances devraient ressembler à ce qui suit :

```gradle
dependencies {
  implementation project(':android-sdk-ui')
  implementation "com.google.firebase:firebase-messaging:+"
}
```

### Étape 3 : Activez l'API d'envoi de messages de Firebase Cloud.

Dans Google Cloud, sélectionnez le projet utilisé par votre application Android, puis activez l'[API Firebase Cloud Messaging](https://console.cloud.google.com/apis/library/fcm.googleapis.com).

![API Firebase Cloud Messaging activée]({% image_buster /assets/img/android/push_integration/create_a_service_account/firebase-cloud-messaging-api-enabled.png %}){: style="max-width:80%;"}

### Étape 4 : Créer un compte de service

Ensuite, créez un nouveau compte de service, afin que Braze puisse effectuer des appels API autorisés lors de l'enregistrement des jetons FCM. Dans Google Cloud, sélectionnez **Service Accounts (Comptes de service)**, puis choisissez votre projet. Sur la page **Comptes de service**, sélectionnez **Créer un compte de service**.

![Page d'accueil du compte de service d'un projet avec l'option "Créer un compte de service" en surbrillance.]({% image_buster /assets/img/android/push_integration/create_a_service_account/select-create-service-account.png %})

Saisissez un nom de compte de service, un ID et une description, puis sélectionnez **Create and continue (Créer et continuer)**.

![Le formulaire "Détails du compte de service".]({% image_buster /assets/img/android/push_integration/create_a_service_account/enter-service-account-details.png %})

Dans le champ **Rôle**, recherchez et sélectionnez **Firebase Cloud Messaging API Admin** dans la liste des rôles. Pour un accès plus restrictif, créez un [rôle personnalisé](https://cloud.google.com/iam/docs/creating-custom-roles) avec l'autorisation `cloudmessaging.messages.create`, puis choisissez-le dans la liste. Lorsque vous avez terminé, sélectionnez **Terminé**.

{% alert warning %}
Veillez à sélectionner **Firebase Cloud Messaging _API_ Admin**, et non **Admin Firebase Cloud Messaging**.
{% endalert %}

![Formulaire « Grant this service account access to project » (Accorder à ce compte de service l'accès au projet) avec « Admin API Firebase Cloud Messaging » sélectionné comme rôle.]({% image_buster /assets/img/android/push_integration/create_a_service_account/add-fcm-api-admin.png %})

### Étape 5 : Générer des identifiants JSON

Ensuite, générez les identifiants JSON pour votre compte de service FCM. Dans Google Cloud IAM & Admin, sélectionnez **Service Accounts (Comptes de service)**, puis choisissez votre projet. Recherchez le compte de service FCM [que vous avez créé précédemment](#step-3-create-a-service-account), puis sélectionnez <i class="fa-solid fa-ellipsis-vertical"></i> **Actions** > **Manage Keys (Gérer les clés)**.

![Page d'accueil du compte de service du projet avec le menu "Actions" ouvert.]({% image_buster /assets/img/android/push_integration/generate_json_credentials/select-manage-keys.png %})

Sélectionnez **Ajouter une clé** > **Créer une nouvelle clé**.

![Le compte de service sélectionné avec le menu "Ajouter une clé" ouvert.]({% image_buster /assets/img/android/push_integration/generate_json_credentials/select-create-new-key.png %})

Choisissez **JSON**, puis sélectionnez **Create (Créer)**. Si vous avez créé votre compte de service en utilisant un ID de projet Google Cloud différent de votre ID de projet FCM, vous devrez mettre à jour manuellement la valeur attribuée à l'adresse `project_id` dans votre fichier JSON.

N'oubliez pas l'endroit où vous avez téléchargé la clé : vous en aurez besoin à l'étape suivante.

![Le formulaire de création d'une clé privée avec "JSON" sélectionné.]({% image_buster /assets/img/android/push_integration/generate_json_credentials/select-create.png %}){: style="max-width:65%;"}

{% alert warning %}
Les clés privées peuvent présenter un risque de sécurité si elles sont compromises. Conservez vos identifiants JSON dans un emplacement/localisation sécurisé pour l'instant : vous supprimerez votre clé après l'avoir téléchargée sur Braze.
{% endalert %}

### Étape 6 : Téléchargez vos informations d'identification JSON vers Braze.

Ensuite, chargez vos identifiants JSON dans votre tableau de bord de Braze. Dans Braze, sélectionnez <i class="fa-solid fa-gear"></i> **Paramètres** > **Paramètres des applications**.

![Le menu Paramètres s'ouvre dans Braze avec « Paramètres des applications » en surbrillance.]({% image_buster /assets/img/android/push_integration/upload_json_credentials/select-app-settings.png %})

Sous les **paramètres de notifications push** de votre application Android, choisissez **Firebase**, puis sélectionnez **Charger un fichier JSON** et chargez les identifiants [que vous avez générés précédemment](#step-4-generate-json-credentials). Lorsque vous avez terminé, sélectionnez **Enregistrer.**

![Formulaire des paramètres de notifications push avec Firebase sélectionné comme fournisseur de notifications push.]({% image_buster /assets/img/android/push_integration/upload_json_credentials/upload-json-file.png %})

{% alert warning %}
Les clés privées peuvent présenter un risque de sécurité si elles sont compromises. Maintenant que votre clé est téléchargée sur Braze, supprimez le fichier [que vous avez généré précédemment](#step-4-generate-json-credentials).
{% endalert %}

### Étape 7 : Configurer l'enregistrement automatique des jetons

Lorsqu'un de vos utilisateurs opte pour les notifications push, votre application doit générer un jeton FCM sur son appareil avant que vous puissiez lui envoyer des notifications push. Avec le SDK Braze, vous pouvez activer l'enregistrement automatique des jetons FCM pour l'appareil de chaque utilisateur dans les fichiers de configuration Braze de votre projet.

Tout d'abord, accédez à la console Firebase, ouvrez votre projet, puis sélectionnez <i class="fa-solid fa-gear"></i> **Paramètres** > **Paramètres du projet**.

![Le projet Firebase avec le menu Paramètres ouvert.]({% image_buster /assets/img/android/push_integration/set_up_automatic_token_registration/select-project-settings.png %})

Sélectionnez **Cloud Messaging**, puis sous **API Firebase Cloud Messaging (V1)**, copiez le numéro dans le champ **ID de l'expéditeur**.

![La page Messagerie Cloud du projet Firebase avec l'ID de l'expéditeur mis en évidence.]({% image_buster /assets/img/android/push_integration/set_up_automatic_token_registration/copy-sender-id.png %})

Ensuite, ouvrez votre projet Android Studio et utilisez votre ID d’expéditeur Firebase pour activer l'enregistrement automatique des jetons FCM au sein de votre `braze.xml` ou `BrazeConfig`.

{% tabs local %}
{% tab braze.xml %}
Pour configurer l'enregistrement automatique des jetons FCM, ajoutez les lignes suivantes à votre fichier `braze.xml`:

```xml
<bool translatable="false" name="com_braze_firebase_cloud_messaging_registration_enabled">true</bool>
<string translatable="false" name="com_braze_firebase_cloud_messaging_sender_id">FIREBASE_SENDER_ID</string>
```

Remplacez `FIREBASE_SENDER_ID` par la valeur que vous avez copiée dans les paramètres de votre projet Firebase. Votre site `braze.xml` devrait ressembler à ce qui suit :

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
  <string translatable="false" name="com_braze_api_key">12345ABC-6789-DEFG-0123-HIJK456789LM</string>
  <bool translatable="false" name="com_braze_firebase_cloud_messaging_registration_enabled">true</bool>
<string translatable="false" name="com_braze_firebase_cloud_messaging_sender_id">603679405392</string>
</resources>
```
{% endtab %}
{% tab BrazeConfig %}
Pour configurer l'enregistrement automatique des jetons FCM, ajoutez les lignes suivantes à votre `BrazeConfig` :

{% subtabs global %}
{% subtab JAVA %}
```java
.setIsFirebaseCloudMessagingRegistrationEnabled(true)
.setFirebaseCloudMessagingSenderIdKey("FIREBASE_SENDER_ID")
```
{% endsubtab %}
{% subtab KOTLIN %}
```kotlin
.setIsFirebaseCloudMessagingRegistrationEnabled(true)
.setFirebaseCloudMessagingSenderIdKey("FIREBASE_SENDER_ID")
```
{% endsubtab %}
{% endsubtabs %}

Remplacez `FIREBASE_SENDER_ID` par la valeur que vous avez copiée dans les paramètres de votre projet Firebase. Votre site `BrazeConfig` devrait ressembler à ce qui suit :

{% subtabs global %}
{% subtab JAVA %}
```java
BrazeConfig brazeConfig = new BrazeConfig.Builder()
  .setApiKey("12345ABC-6789-DEFG-0123-HIJK456789LM")
  .setCustomEndpoint("sdk.iad-01.braze.com")
  .setSessionTimeout(60)
  .setHandlePushDeepLinksAutomatically(true)
  .setGreatNetworkDataFlushInterval(10)
  .setIsFirebaseCloudMessagingRegistrationEnabled(true)
  .setFirebaseCloudMessagingSenderIdKey("603679405392")
  .build();
Braze.configure(this, brazeConfig);
```
{% endsubtab %}
{% subtab KOTLIN %}
```kotlin
val brazeConfig = BrazeConfig.Builder()
  .setApiKey("12345ABC-6789-DEFG-0123-HIJK456789LM")
  .setCustomEndpoint("sdk.iad-01.braze.com")
  .setSessionTimeout(60)
  .setHandlePushDeepLinksAutomatically(true)
  .setGreatNetworkDataFlushInterval(10)
  .setIsFirebaseCloudMessagingRegistrationEnabled(true)
  .setFirebaseCloudMessagingSenderIdKey("603679405392")
  .build()
Braze.configure(this, brazeConfig)
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

{% alert tip %}
Si vous souhaitez enregistrer manuellement des jetons FCM, vous pouvez appeler [`Braze.setRegisteredPushToken()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/registered-push-token.html) dans la méthode [`onCreate()`](https://developer.android.com/reference/android/app/Application.html#onCreate()) de votre application.
{% endalert %}

### Étape 8 : Supprimez les demandes automatiques dans votre classe d'application

Pour éviter que Braze ne déclenche des requêtes réseau inutiles à chaque fois que vous envoyez des notifications push silencieuses, supprimez toutes les requêtes réseau automatiques configurées dans la méthode `onCreate()` de votre classe `Application`. Pour plus d'informations, consultez [Référence pour les développeurs Android : Application](https://developer.android.com/reference/android/app/Application).

## Recevoir et afficher les notifications push {#displaying-push}

Après avoir terminé cette section, vous devriez pouvoir recevoir et afficher des notifications push envoyées par Braze.

### Étape 1 : Enregistrer le service de messagerie de Firebase de Braze

{% alert warning %}
Si vous avez déjà un service de messagerie Firebase enregistré, n’effectuez pas cette étape. Au lieu de cela, passez à la section [Utilisation de votre propre service d'envoi messages Firebase](#using-your-own-firebase-messaging-service) et suivez les étapes indiquées.
{% endalert %}

Braze comprend un service pour gérer la réception de notifications push et les intentions d’ouverture. Notre classe `BrazeFirebaseMessagingService` doit être enregistrée dans votre `AndroidManifest.xml` :

```xml
<service android:name="com.braze.push.BrazeFirebaseMessagingService"
  android:exported="false">
  <intent-filter>
    <action android:name="com.google.firebase.MESSAGING_EVENT" />
  </intent-filter>
</service>
```

Notre code de notification utilise également `BrazeFirebaseMessagingService` pour gérer le suivi des ouvertures et des clics. Ce service doit être enregistré dans le `AndroidManifest.xml` pour fonctionner correctement. N'oubliez pas non plus que Braze préfixe les notifications provenant de notre système avec une clé unique afin de ne rendre que les notifications envoyées depuis nos systèmes. Vous pouvez enregistrer des services supplémentaires séparément pour afficher les notifications envoyées par d’autres services FCM. Voir [`AndroidManifest.xml`](https://github.com/braze-inc/braze-android-sdk/blob/master/samples/firebase-push/src/main/AndroidManifest.xml "`AndroidManifest.xml`") dans l'exemple d'application Firebase push.

{% alert important %}
Avant le SDK Braze version 3.1.1, `AppboyFcmReceiver` était utilisé pour gérer les notifications push FCM. La classe `AppboyFcmReceiver` doit être retirée de votre manifeste et remplacée par l’intégration précédente.
{% endalert %}

#### Utilisation d'un service d'envoi de messages Firebase de secours

Si vous souhaitez également utiliser un autre service de messagerie Firebase, vous pouvez également spécifier un service de messagerie Firebase de repli à appeler si votre application reçoit une notification push qui ne provient pas de Braze.

Dans votre `braze.xml`, précisez :

```xml
<bool name="com_braze_fallback_firebase_cloud_messaging_service_enabled">true</bool>
<string name="com_braze_fallback_firebase_cloud_messaging_service_classpath">com.company.OurFirebaseMessagingService</string>
```

ou par le biais de la [configuration de l'exécution :]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/runtime_configuration/)

{% tabs %}
{% tab JAVA %}

```java
BrazeConfig brazeConfig = new BrazeConfig.Builder()
        .setFallbackFirebaseMessagingServiceEnabled(true)
        .setFallbackFirebaseMessagingServiceClasspath("com.company.OurFirebaseMessagingService")
        .build();
Braze.configure(this, brazeConfig);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
val brazeConfig = BrazeConfig.Builder()
        .setFallbackFirebaseMessagingServiceEnabled(true)
        .setFallbackFirebaseMessagingServiceClasspath("com.company.OurFirebaseMessagingService")
        .build()
Braze.configure(this, brazeConfig)
```

{% endtab %}
{% endtabs %}

#### Utiliser votre propre service de messagerie Firebase

Si vous avez déjà enregistré un service d'envoi de messages Firebase, vous pouvez passer des [`RemoteMessage`](https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage) à Braze par l'intermédiaire de [`BrazeFirebaseMessagingService.handleBrazeRemoteMessage()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.push/-braze-firebase-messaging-service/-companion/handle-braze-remote-message.html). Cette méthode n'affichera une notification que si l'objet [`RemoteMessage`](https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage) provient de Braze et l'ignorera si ce n'est pas le cas.

{% tabs %}
{% tab JAVA %}

```java
public class MyFirebaseMessagingService extends FirebaseMessagingService {
  @Override
  public void onMessageReceived(RemoteMessage remoteMessage) {
    super.onMessageReceived(remoteMessage);
    if (BrazeFirebaseMessagingService.handleBrazeRemoteMessage(this, remoteMessage)) {
      // This Remote Message originated from Braze and a push notification was displayed.
      // No further action is needed.
    } else {
      // This Remote Message did not originate from Braze.
      // No action was taken and you can safely pass this Remote Message to other handlers.
    }
  }
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
class MyFirebaseMessagingService : FirebaseMessagingService() {
  override fun onMessageReceived(remoteMessage: RemoteMessage?) {
    super.onMessageReceived(remoteMessage)
    if (BrazeFirebaseMessagingService.handleBrazeRemoteMessage(this, remoteMessage)) {
      // This Remote Message originated from Braze and a push notification was displayed.
      // No further action is needed.
    } else {
      // This Remote Message did not originate from Braze.
      // No action was taken and you can safely pass this Remote Message to other handlers.
    }
  }
}
```

{% endtab %}
{% endtabs %}

### Étape 2 : Conformer les petites icônes aux lignes directrices en matière de conception

Pour des informations générales sur les icônes de notification Android, consultez l'[aperçu des notifications.](https://developer.android.com/guide/topics/ui/notifiers/notifications)

À partir de Android N, vous devez mettre à jour ou supprimer les objets de petites icônes de notification qui impliquent une couleur. Le système Android (et non le SDK Braze) ignore tous les canaux non alpha et de transparence dans les icônes d’action et les petites icônes de notification. En d’autres termes, Android convertit toutes les parties de votre petite icône de notification en monochrome, sauf pour les zones transparentes.

Pour créer correctement un objet d’icône de petite taille :
- Supprimez toutes les couleurs de l’image sauf le blanc.
- Toutes les parties non blanches de l’objet doivent être transparentes.

{% alert note %}
Un symptôme commun d’un objet inapproprié est que la petite icône de notification s’affiche comme un carré monochrome solide. Cela est dû au système Android qui ne parvient pas à trouver de zone transparente dans l’objet de petite icône de notification.
{% endalert %}

Les grandes et petites icônes suivantes sont des exemples d’icônes correctement conçues :

![Une petite icône apparaît dans le coin inférieur d'une grande icône à côté d'un message qui dit "Hey I'm on my way to the bar but..."]({% image_buster /assets/img_archive/large_and_small_notification_icon.png %} "Large and Small Notification Icon")

### Étape 3 : Configurer les icônes de notification

#### Spécifier des icônes dans braze.xml

Braze vous permet de configurer vos icônes de notification en spécifiant des ressources dessinées dans votre `braze.xml` :

```xml
<drawable name="com_braze_push_small_notification_icon">REPLACE_WITH_YOUR_ICON</drawable>
<drawable name="com_braze_push_large_notification_icon">REPLACE_WITH_YOUR_ICON</drawable>
```

Il est nécessaire de définir une petite icône de notification. **Si vous n’en définissez pas, Braze utilisera par défaut l’icône de l’application comme petite icône de notification, ce qui n’est pas forcément idéal.**

Définir une grande icône de notification est facultatif, mais recommandé.

#### Spécifier la couleur d'accentuation de l'icône

La couleur d'accentuation de l'icône de notification peut être modifiée dans votre `braze.xml`. Si la couleur n'est pas spécifiée, la couleur par défaut est le même gris que celui utilisé par Lollipop pour les notifications du système.

```xml
<integer name="com_braze_default_notification_accent_color">0xFFf33e3e</integer>
```

Vous pouvez également utiliser une référence de couleur :

```xml
<color name="com_braze_default_notification_accent_color">@color/my_color_here</color>
```

### Étape 4 : Ajouter des liens profonds

#### Activer l’ouverture automatique du lien profond

Pour permettre à Braze d’ouvrir automatiquement votre application et les liens profonds lorsqu’une notification push est cliquée, définissez `com_braze_handle_push_deep_links_automatically` sur `true` dans votre fichier `braze.xml` :

```xml
<bool name="com_braze_handle_push_deep_links_automatically">true</bool>
```

Cet indicateur peut également être défini par la [configuration de l'exécution :]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/runtime_configuration/)

{% tabs %}
{% tab JAVA %}

```java
BrazeConfig brazeConfig = new BrazeConfig.Builder()
        .setHandlePushDeepLinksAutomatically(true)
        .build();
Braze.configure(this, brazeConfig);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
val brazeConfig = BrazeConfig.Builder()
        .setHandlePushDeepLinksAutomatically(true)
        .build()
Braze.configure(this, brazeConfig)
```

{% endtab %}
{% endtabs %}

Si vous souhaitez gérer de manière personnalisée les liens profonds, vous devrez créer un rappel de poussée qui écoute les poussées reçues et les intentions d'ouverture de Braze. Pour plus d'informations, consultez notre article sur le [traitement personnalisé des reçus de push et des ouvertures]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#android-push-listener-callback).

#### Création de liens profonds personnalisés

Si vous n'avez pas encore ajouté de liens profonds à votre application, suivez les instructions figurant dans la [documentation destinée aux développeurs AndroidGoogle](http://developer.android.com/training/app-indexing/deep-linking.html "Deep Linking Documentation sur") la création de liens profonds. Pour en savoir plus sur les liens profonds, consultez notre [article de FAQ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#what-is-deep-linking).

#### Ajouter des liens profonds

Le tableau de bord de Braze prend en charge la mise en place de liens profonds ou d’URL Web dans les campagnes de notifications push et des Canvas qui seront ouverts lorsque la notification est cliquée.

![Le paramètre "On Click Behavior" dans le tableau de bord de Braze avec "Deep Link Into Application" sélectionné dans le menu déroulant.]({% image_buster /assets/img_archive/deep_link_click_action.png %} "Deep Link Click Action")

#### Personnaliser le comportement de la pile arrière

Par défaut, le SDK Android place l’activité du lanceur principal de votre application hôte dans la pile arrière lorsqu’il suit des liens profonds de notification push. Braze vous permet de définir qu’une activité personnalisée s’ouvre dans la pile arrière à la place de votre activité de lanceur principal ou de désactiver complètement la pile arrière.

Par exemple, pour définir une activité appelée `YourMainActivity` comme activité de la pile arrière à l'aide de la [configuration d'exécution]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/runtime_configuration/):

{% tabs %}
{% tab JAVA %}

```java
BrazeConfig brazeConfig = new BrazeConfig.Builder()
        .setPushDeepLinkBackStackActivityEnabled(true)
        .setPushDeepLinkBackStackActivityClass(YourMainActivity.class)
        .build();
Braze.configure(this, brazeConfig);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
val brazeConfig = BrazeConfig.Builder()
        .setPushDeepLinkBackStackActivityEnabled(true)
        .setPushDeepLinkBackStackActivityClass(YourMainActivity.class)
        .build()
Braze.configure(this, brazeConfig)
```

{% endtab %}
{% endtabs %}

Consultez la configuration équivalente pour votre `braze.xml`. Notez que le nom de la classe doit être identique à celui renvoyé par `Class.forName()`.

```xml
<bool name="com_braze_push_deep_link_back_stack_activity_enabled">true</bool>
<string name="com_braze_push_deep_link_back_stack_activity_class_name">your.package.name.YourMainActivity</string>
```

### Étape 5 : Définir les canaux de notification

Le SDK Android de Braze prend en charge les [canaux de notification Android](https://developer.android.com/preview/features/notification-channels.html). Si une notification Braze ne contient pas d’ID pour un canal de notification ou qu’une notification Braze contient un ID de canal non valide, Braze affichera la notification avec le canal de notification par défaut défini dans le SDK. Les utilisateurs de Braze utilisent les [canaux de notification Android]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/notification_channels/) au sein de la plateforme pour regrouper les notifications.

Pour définir le nom du canal de notification par défaut de Braze auquel l'utilisateur est confronté, procédez comme suit [`BrazeConfig.setDefaultNotificationChannelName()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/set-default-notification-channel-name.html).

Pour définir la description du canal de notification par défaut de Braze à laquelle l'utilisateur est confronté, utilisez la commande [`BrazeConfig.setDefaultNotificationChannelDescription()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/set-default-notification-channel-description.html).

Mettez à jour toutes les campagnes API avec le paramètre [Android push object]({{site.baseurl}}/api/objects_filters/messaging/android_object/) pour inclure le champ `notification_channel`. Si ce champ n'est pas spécifié, Braze enverra la charge utile de notification avec l'ID du canal de [repli du tableau de bord]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/notification_channels/#dashboard-fallback-channel).

En dehors du canal de notification par défaut, Braze ne crée aucun canal. Tous les autres canaux doivent être définis par programmation par l’application hôte, puis entrés dans le tableau de bord de Braze.

Le nom et la description par défaut du canal peuvent également être configurés dans `braze.xml`.

```xml
<string name="com_braze_default_notification_channel_name">Your channel name</string>
<string name="com_braze_default_notification_channel_description">Your channel description</string>
```

### Étape 6 : Tester l’affichage et l’analyse des notifications

#### Tester l’affichage

À ce stade, vous devriez pouvoir voir les notifications envoyées par Braze. Pour tester cela, rendez-vous sur la page **Campagnes de** votre tableau de bord Braze et créez une campagne de **notification push.**  Choisissez **Android Push** et concevez votre message. Cliquez ensuite sur l’icône « Œil » dans le composeur pour obtenir l’expéditeur de test. Saisissez l'ID ou l'adresse e-mail de votre utilisateur actuel et cliquez sur **Envoyer le test.** Vous devriez voir la notification push s’afficher sur votre appareil.

![L'onglet 'Test' d'une campagne de notification push dans le tableau de bord de Braze.]({% image_buster /assets/img_archive/android_push_test.png %} "Android Push Test")

Pour les problèmes liés à l'affichage push, consultez notre [guide de résolution des problèmes.]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/troubleshooting/)

#### Tester l’analyse

À ce stade, vous devez également disposer d’un enregistrement de l’analyse pour les ouvertures de notifications push. En cliquant sur la notification lorsqu'elle arrive, le nombre d'**ouvertures directes** sur la page des résultats de votre campagne devrait augmenter de 1. Consultez notre article sur [les rapports push]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_reporting/) pour en savoir plus sur les analyses/analytiques push.

Pour les problèmes liés à l'analyse/analytique push, consultez notre [guide de résolution des problèmes.]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/troubleshooting/)

#### Tester depuis la ligne de commande

Si vous souhaitez tester les notifications in-app et push via l'interface de ligne de commande, vous pouvez envoyer une seule notification par le biais du terminal via cURL et l ['API de messages.]({{site.baseurl}}/api/endpoints/messaging/) Vous devrez remplacer les champs suivants par les valeurs correctes pour votre cas de test :

- `YOUR_API_KEY` (Allez dans **Paramètres** > **Clés API**.)
- `YOUR_EXTERNAL_USER_ID` ( Recherchez un profil utilisateur sur la page **Recherche d'utilisateurs**).
- `YOUR_KEY1` (facultatif)
- `YOUR_VALUE1` (facultatif)

{% alert note %}
Si vous utilisez l'[ancienne navigation]({{site.baseurl}}/navigation), ces pages se trouvent à un emplacement/localisation différent : <br>\- Les **clés API** sont situées dans la **console de développement** > **Paramètres API**. <br>\- L’option **Rechercher des utilisateurs** est située dans **Utilisateurs** > **Recherche d'utilisateurs**
{% endalert %}

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {YOUR_API_KEY}" -d '{
  "external_user_ids":["YOUR_EXTERNAL_USER_ID"],
  "messages": {
    "android_push": {
      "title":"Test push title",
      "alert":"Test push",
      "extra": {
        "YOUR_KEY1":"YOUR_VALUE1"
      }
    }  
  }
}' https://rest.iad-01.braze.com/messages/send
```

Cet exemple utilise l’instance `US-01`. Si vous n'êtes pas sur cette instance, remplacez l'endpoint `US-01` par [votre endpoint]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/).

## Personnalisation de l'affichage des notifications

### Étape 1 : Créer votre fabrique de notification personnalisée

Dans certains scénarios, vous pourriez désirer personnaliser les notifications push d’une manière qui pourrait être encombrante ou non disponible côté serveur. Pour vous donner un contrôle complet de l'affichage des notifications, nous avons ajouté la possibilité de définir vos propres objets de notification. [`IBrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze-notification-factory/index.html) pour créer des objets de notification qui seront affichés par Braze.

Si une `IBrazeNotificationFactory` personnalisée est définie, Braze appellera la méthode `createNotification()` de votre fabrique lors de la réception de la notification push avant qu’elle ne soit affichée à l’utilisateur. Braze transmettra un `Bundle` contenant les données de notification push Braze et un autre `Bundle` contenant les paires clé-valeur personnalisées envoyées soit via le tableau de bord soit par les API de messagerie :

Braze transmettra un fichier [`BrazeNotificationPayload`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.push/-braze-notification-payload/index.html) contenant les données de la notification push de Braze.

{% tabs %}
{% tab JAVA %}

```java
// Factory method implemented in your custom IBrazeNotificationFactory
@Override
public Notification createNotification(BrazeNotificationPayload brazeNotificationPayload) {
  // Example of getting notification title
  String title = brazeNotificationPayload.getTitleText();

  // Example of retrieving a custom KVP ("my_key" -> "my_value")
  String customKvp = brazeNotificationPayload.getBrazeExtras().getString("my_key");
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
// Factory method implemented in your custom IBrazeNotificationFactory
override fun createNotification(brazeNotificationPayload: BrazeNotificationPayload): Notification {
  // Example of getting notification title
  val title = brazeNotificationPayload.getTitleText()

  // Example of retrieving a custom KVP ("my_key" -> "my_value")
  val customKvp = brazeNotificationPayload.getBrazeExtras().getString("my_key")
}
```

{% endtab %}
{% endtabs %}

Vous pouvez renvoyer `null` à partir de votre méthode `createNotification()` personnalisée pour ne pas afficher du tout la notification, utiliser `BrazeNotificationFactory.getInstance().createNotification()` pour obtenir notre objet `notification` par défaut pour ces données et le modifier avant l'affichage, ou générer un objet `notification` complètement séparé pour l'affichage.

{% alert note %}
Pour consulter la documentation sur les clés de données de notifications push Braze, reportez-vous au [SDK Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-constants/index.html).
{% endalert %}

### Étape 2 : Définir votre fabrique de notification personnalisée

Pour demander à Braze d’utiliser votre fabrique de notification personnalisée, utilisez la méthode `setCustomBrazeNotificationFactory` afin de définir votre [`IBrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze-notification-factory/index.html) :

{% tabs %}
{% tab JAVA %}


```java
setCustomBrazeNotificationFactory(IBrazeNotificationFactory brazeNotificationFactory);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
setCustomBrazeNotificationFactory(brazeNotificationFactory: IBrazeNotificationFactory)
```

{% endtab %}
{% endtabs %}

L’endroit recommandé pour définir votre `IBrazeNotificationFactory` personnalisée est dans la méthode de cycle de vie de l’application `Application.onCreate()` (pas activité). Cela permettra à la fabrique de notification d’être correctement définie chaque fois que le processus de votre application est actif.

{% alert important %}
La création de votre propre notification à partir de zéro est un cas d'utilisation avancé et ne doit être effectuée qu'après des tests approfondis et une compréhension approfondie de la fonctionnalité push de Braze. Par exemple, vous devez vous assurer que vos journaux de notifications push s'ouvrent correctement.
{% endalert %}

Pour annuler la définition de votre [`IBrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze-notification-factory/index.html) personnalisée et revenir à la gestion par défaut de Braze pour les notifications push, transmettez `null` à notre système de définition de fabrique de notification personnalisée :

{% tabs %}
{% tab JAVA %}


```java
setCustomBrazeNotificationFactory(null);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
setCustomBrazeNotificationFactory(null)
```

{% endtab %}
{% endtabs %}

## Amorces de notifications push

Les campagnes d'amorces de notifications push encouragent vos utilisateurs à activer les notifications push sur leur appareil pour votre appli. Ceci peut se faire sans personnalisation du SDK, grâce à notre [amorce de notifications push sans code]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/).

