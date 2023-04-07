---
nav_title: Intégration standard
article_title: Intégration de notifications push standard pour Android
platform: Android
page_order: 0
description: "Cet article explique comment intégrer des notifications push dans votre application Android."
channel:
  - Notification push
search_rank: 3
---

# Intégration

![Exemple de notifications push d’image insérée pour Android]({% image_buster /assets/img/android/push/inline_image_push_android_1.png %}){: style="float:right;max-width:35%;margin-left:15px;border: 0;"}

Une notification push est une alerte hors application qui apparaît sur l’écran de l’utilisateur lorsqu’une mise à jour importante se produit. Les notifications push constituent un moyen précieux de fournir à vos utilisateurs un contenu urgent et pertinent, ou de les réengager dans votre application.

Braze envoie des notifications push aux appareils Android en utilisant [Firebase Cloud Messaging (FCM)][45].

Découvrez notre [documentation d’aide][8] pour les bonnes pratiques de notification push.

## S’enregistrer pour la notification push 

Utilisez [Firebase Cloud Messaging](https://firebase.google.com/docs/cloud-messaging/) pour vous enregistrer pour les notifications push. Pour un exemple complet d’utilisation de Firebase avec le SDK Braze pour Android, consultez notre [exemple d’application de notification push Firebase](https://github.com/braze-inc/braze-android-sdk/tree/master/samples/firebase-push).

### Étape 1 : Activer Firebase

Pour commencer, suivez les [instructions de Firebase][49] sur l’ajout de Firebase à votre projet Android.

Ensuite, ajoutez la dépendance de messagerie Firebase à votre module `build.gradle` :

```gradle
implementation "com.google.firebase:firebase-core:${FIREBASE_CORE_VERSION}"
implementation "com.google.firebase:firebase-messaging:${FIREBASE_PUSH_MESSAGING_VERSION}"
```

### Étape 2 : Configurer l’enregistrement du jeton

Les notifications push de Braze ne fonctionnent pas tant qu’un jeton Firebase Cloud Messaging (jeton d’enregistrement FCM) n’est pas enregistré. Les jetons d’enregistrement FCM peuvent être enregistrés par le SDK Braze **automatiquement** (recommandé) ou **manuellement**. Les jetons peuvent être enregistrés manuellement à l’aide de la méthode [`Braze.setRegisteredPushToken()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/registered-push-token.html).

Assurez-vous d’utiliser votre ID d’expéditeur Firebase. Il s’agit d’une valeur numérique unique créée lorsque vous créez votre projet Firebase, disponible dans l’onglet **Cloud Messaging (Messagerie cloud)** de la console Firebase, dans le panneau **Settings (Paramètres)**. L’ID d’expéditeur sert à identifier chaque expéditeur qui peut envoyer des messages à l’application client.

{% tabs local %}
{% tab Automatic registration (recommended) %}

Pour enregistrer automatiquement les jetons d’enregistrement FCM, activez l’enregistrement automatique Firebase et définissez un ID d’expéditeur Firebase Cloud Messaging.

Dans votre `braze.xml` :

```xml
<bool translatable="false" name="com_braze_firebase_cloud_messaging_registration_enabled">true</bool>
<string translatable="false" name="com_braze_firebase_cloud_messaging_sender_id">your_fcm_sender_id_here</string>
```

Ou dans votre [`BrazeConfig`]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/runtime_configuration/#runtime-configuration) :

{% subtabs local %}
{% subtab JAVA %}

```java
BrazeConfig brazeConfig = new BrazeConfig.Builder()
  .setIsFirebaseCloudMessagingRegistrationEnabled(true)
  .setFirebaseCloudMessagingSenderIdKey("YOUR FIREBASE SENDER ID HERE")
  .build();
Braze.configure(this, brazeConfig);
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
val brazeConfig = BrazeConfig.Builder()
    .setIsFirebaseCloudMessagingRegistrationEnabled(true)
    .setFirebaseCloudMessagingSenderIdKey("YOUR FIREBASE SENDER ID HERE")
    .build()
Braze.configure(this, brazeConfig)
```

{% endsubtab %}
{% endsubtabs %}

{% endtab %}
{% tab Manual registration %}

Pour enregistrer manuellement vos jetons, nous vous recommandons d’appeler [`Braze.setRegisteredPushToken()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/registered-push-token.html) depuis la méthode [`onCreate()`](https://developer.android.com/reference/android/app/Application.html#onCreate()) de votre application pour garantir que les jetons de notification push sont livrés de manière fiable à Braze.

{% subtabs local %}
{% subtab JAVA %}

```java
public class MyApplication extends Application {
  @Override
  public void onCreate() {
    super.onCreate();
    final Context applicationContext = this;
    FirebaseMessaging.getInstance().getToken().addOnCompleteListener(task -> {
      if (!task.isSuccessful()) {
        Log.w(TAG, "Exception while registering FCM token with Braze.", task.getException());
        return;
      }

      final String token = task.getResult();
      Braze.getInstance(applicationContext).setRegisteredPushToken(token);
    });
  }
}
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
class MyApplication: Application() {
  override fun onCreate() {
    super.onCreate()
    FirebaseMessaging.getInstance().token.addOnCompleteListener { task: Task<String?> ->
      if (!task.isSuccessful) {
        Log.w(TAG, "Exception while registering FCM token with Braze.", task.exception)
        return@addOnCompleteListener
      }
      val token = task.result
      Braze.getInstance(applicationContext).setRegisteredPushToken(token)
    }
  }
}
```

{% endsubtab %}
{% endsubtabs %}

Bien que nous vous recommandions fortement d’enregistrer votre jeton d’enregistrement FCM dans votre application `onCreate()`, il peut être enregistré n’importe où dans votre code.

{% endtab %}
{% endtabs %}

### Étape 3 : Migrer depuis GCM (facultatif)

Si vous migrez de l’utilisation de GCM à celle de Firebase avec Braze, consultez le [Guide de migration GCM][48] pour y trouver des instructions sur la manière de passer à l’utilisation de Firebase dans votre application.

### Étape 4 : Définir vos informations d’identification Firebase

{% alert warning %}
La clé de serveur API Cloud Messaging **Legacy** est requise pour configurer les notifications push Android dans Braze. L’utilisation des identifiants de l’API Firebase Cloud Messaging (V1) ne vous permettra pas d’envoyer des notifications push.
{% endalert %}

Tout d’abord, vous devez localiser votre clé de serveur Cloud Messaging et l’ID d’expéditeur dans la [Developer Console de Firebase][58]. Sélectionnez votre projet Firebase et allez à **Settings > Cloud Messaging (Paramètres > Messagerie cloud)** et copiez la **clé serveur de l’API Cloud Messaging (Legacy)** et l’**ID de l’expéditeur** :

![La plateforme Firebase sous « Settings » (Paramètres), puis « Cloud Messaging » (Messagerie cloud) affiche votre ID de serveur et votre clé de serveur.][80]

{% alert note %}
Si l’API Cloud Messaging est désactivée, cliquez sur les trois points pour activer l’API dans Google Cloud Console, puis actualisez la page **Project settings (Paramètres du projet)**.
{% endalert %}
![L’API Cloud Messaging peut être activée en cliquant sur les trois points à droite.][79]

Saisissez votre clé serveur de l’API Cloud Messaging (Legacy) et votre ID d’expéditeur dans le tableau de bord de Braze :

1. Sur la page **Settings (Paramètres)** (où se trouvent vos clés API), sélectionnez votre application Android.
2. Saisissez votre clé de serveur de l’API Cloud Messaging (Legacy) dans le champ **Firebase Cloud Messaging Server Key (Clé du serveur Firebase Cloud Messaging)**, dans la section des paramètres de notification push.
3. Saisissez votre ID d’expéditeur de l’API Cloud Messaging (Legacy) dans le champ **Firebase Cloud Messaging Sender ID (ID d’expéditeur Firebase Cloud Messaging)**, dans la section des paramètres de notification push.

![][16]

### Étape 5 : Supprimer les anciennes autorisations

Braze n’exige plus les autorisations suivantes lors de l’utilisation de Firebase :

  ```xml
  <uses-permission android:name="android.permission.GET_ACCOUNTS" />
  <uses-permission android:name="android.permission.WAKE_LOCK" />
  <uses-permission android:name="com.google.android.c2dm.permission.RECEIVE" />
  <permission android:name="YOUR-APPLICATION-PACKAGE-NAME.permission.C2D_MESSAGE" android:protectionLevel="signature"/>
  <uses-permission android:name="YOUR-APPLICATION-PACKAGE-NAME.permission.C2D_MESSAGE" />
  ```

### Étape 6 : Supprimer les actions automatiques de votre classe d’application

Si vous avez une sous-classe d’[application][76] personnalisée, assurez-vous que vous n’avez pas de logique automatique qui pingue vos serveurs dans la méthode de cycle de vie `Application.onCreate()` de votre classe. Cela garantira que les notifications push silencieuses de Braze ne provoquent pas de requêtes inutiles auprès de vos serveurs.

## Recevoir et afficher les notifications push {#displaying-push}

Après avoir terminé cette section, vous devriez pouvoir recevoir et afficher des notifications push envoyées par Braze.

### Étape 1 : Enregistrer le service de messagerie de Firebase de Braze

{% alert warning %}
Si vous avez déjà un service de messagerie Firebase enregistré, n’effectuez pas cette étape. Passez à la place à la section [Utiliser votre propre service de messagerie Firebase](#using-your-own-firebase-messaging-service) et suivez les étapes indiquées.
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

Le code de notification de Braze utilise également `BrazeFirebaseMessagingService` pour gérer le suivi des actions d’ouverture et de clic. Ce service doit être enregistré dans le `AndroidManifest.xml` pour fonctionner correctement. Rappelez-vous également que Braze préfixe les notifications depuis notre système avec une clé unique pour garantir que nous n’affichons que les notifications envoyées par les systèmes de Braze. Vous pouvez enregistrer des services supplémentaires séparément pour afficher les notifications envoyées par d’autres services FCM. Consultez [`AndroidManifest.xml`][70] dans l’exemple d’application de notification push Firebase.

{% alert important %}
Avant le SDK Braze version 3.1.1, `AppboyFcmReceiver` était utilisé pour gérer les notifications push FCM. La classe `AppboyFcmReceiver` doit être retirée de votre manifeste et remplacée par l’intégration précédente.
{% endalert %}

##### Utiliser votre propre service de messagerie Firebase

Si vous avez déjà enregistré un service de messagerie Firebase, vous pouvez transmettre des objets [`RemoteMessage`][75] à Braze via [`BrazeFirebaseMessagingService.handleBrazeRemoteMessage()`][74]. Cette méthode n’affichera la notification que si l’objet [`RemoteMessage`][75] provient de Braze et l’ignorera sans danger si ce n’est pas le cas.

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

### Étape 2 : S’assurer que les petites icônes sont conformes aux directives de conception

Pour des informations générales sur les icônes de notification Android, consultez la page [Aperçu des notifications][37].

À partir de Android N, vous devez mettre à jour ou supprimer les objets de petites icônes de notification qui impliquent une couleur. Le système Android (et non le SDK Braze) ignore tous les canaux non alpha et de transparence dans les icônes d’action et les petites icônes de notification. En d’autres termes, Android convertit toutes les parties de votre petite icône de notification en monochrome, sauf pour les zones transparentes.

Pour créer correctement un objet d’icône de petite taille :
- Supprimez toutes les couleurs de l’image sauf le blanc.
- Toutes les parties non blanches de l’objet doivent être transparentes.

{% alert note %}
Un symptôme commun d’un objet inapproprié est que la petite icône de notification s’affiche comme un carré monochrome solide. Cela est dû au système Android qui ne parvient pas à trouver de zone transparente dans l’objet de petite icône de notification.
{% endalert %}

Les grandes et petites icônes suivantes sont des exemples d’icônes correctement conçues :

![Une petite icône apparaissant dans le coin inférieur d’une grande icône à côté d’un message qui dit « Hé je vais au bar, mais… »][38]

### Étape 3 : Configurer les icônes de notification

#### Spécifier des icônes dans braze.xml

Braze vous permet de configurer vos icônes de notification en spécifiant des ressources dessinées dans votre `braze.xml` :

```xml
<drawable name="com_braze_push_small_notification_icon">REPLACE_WITH_YOUR_ICON</drawable>
<drawable name="com_braze_push_large_notification_icon">REPLACE_WITH_YOUR_ICON</drawable>
```

Il est nécessaire de définir une petite icône de notification. **Si vous n’en définissez pas, Braze utilisera par défaut l’icône de l’application comme petite icône de notification ce qui peut ne pas être idéal.**

Définir une grande icône de notification est facultatif, mais recommandé.

#### Spécifier la couleur d’arrière-plan de l’icône

La couleur d’arrière-plan de l’icône de notification peut être remplacée dans votre `braze.xml`. Si la couleur n’est pas spécifiée, la couleur d’arrière-plan par défaut est le même gris utilisé par Lollipop pour les notifications du système.

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

Cet indicateur peut également être défini via la [configuration de temps d’exécution][65] :

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

Si vous souhaitez personnaliser la gestion des liens profonds, vous devrez créer une fonction de rappel de notification push qui écoute la réception de notifications push et l’ouverture des intentions Braze. Consultez notre article [Gestion personnalisée des reçus et des ouvertures de notifications push][52] pour plus d’informations.

#### Création de liens profonds personnalisés

Suivez les instructions qui se trouvent dans la [documentation du développeur Android][40] sur la création de liens profonds si vous n’en avez pas encore ajouté à votre application. Pour en savoir plus sur les liens profonds, consultez notre [article de FAQ][42].

#### Ajouter des liens profonds

Le tableau de bord de Braze prend en charge la mise en place de liens profonds ou d’URL Web dans les campagnes de notifications push et des Canvas qui seront ouverts lorsque la notification est cliquée.

![][41]

#### Personnaliser le comportement de la pile arrière

Par défaut, le SDK Android place l’activité du lanceur principal de votre application hôte dans la pile arrière lorsqu’il suit des liens profonds de notification push. Braze vous permet de définir qu’une activité personnalisée s’ouvre dans la pile arrière à la place de votre activité de lanceur principal ou de désactiver complètement la pile arrière.

Par exemple, pour définir une activité appelée `YourMainActivity` en tant qu’activité de pile arrière en utilisant la [configuration de temps d’exécution][65] :

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

Le SDK Braze pour Android prend en charge les [canaux de notification Android][62]. Si une notification Braze ne contient pas d’ID pour un canal de notification ou qu’une notification Braze contient un ID de canal non valide, Braze affichera la notification avec le canal de notification par défaut défini dans le SDK. Les utilisateurs Braze se servent des [canaux de notification Android][61] au sein de la plateforme pour regrouper les notifications.

Pour définir le nom affiché à l’utilisateur du canal de notification de Braze par défaut, utilisez [`BrazeConfig.setDefaultNotificationChannelName()`][72].

Pour définir la description affichée à l’utilisateur du canal de notification de Braze par défaut, utilisez [`BrazeConfig.setDefaultNotificationChannelDescription()`][73].

Vous devez vous assurer que toutes les campagnes API avec le paramètre d’[objet de notification push Android][63] sont mises à jour pour inclure le champ `notification_channel`. Si ce champ n’est pas spécifié, Braze enverra la charge utile de notification avec l’ID de canal [de repli du tableau de bord][64].

En dehors du canal de notification par défaut, Braze ne crée aucun canal. Tous les autres canaux doivent être définis par programmation par l’application hôte, puis entrés dans le tableau de bord de Braze.

Le nom et la description par défaut du canal peuvent également être configurés dans `braze.xml`.

```xml
<string name="com_braze_default_notification_channel_name">Your channel name</string>
<string name="com_braze_default_notification_channel_description">Your channel description</string>
```

### Étape 6 : Tester l’affichage et l’analytique des notifications

#### Tester l’affichage

À ce stade, vous devriez pouvoir voir les notifications envoyées par Braze. Pour le vérifier, allez sur la page **Campaigns** de votre tableau de bord de Braze et créez une campagne de **notification push**. Choisissez **Android Push (Notification push Android)** et concevez votre message. Cliquez ensuite sur l’icône « Œil » dans le composeur pour obtenir l’expéditeur de test. Saisissez l’ID utilisateur ou l’adresse e-mail de votre utilisateur actuel et cliquez sur **Send Test (Envoyer le test)**. Vous devriez voir la notification push s’afficher sur votre appareil.

![][55]

Pour les problèmes liés à l’affichage de notifications push, consultez notre [guide de résolution des problèmes][57].

#### Tester l’analytique

À ce stade, vous devez également disposer d’un enregistrement de l’analytique pour les ouvertures de notifications push. Cliquer sur la notification à son arrivée doit entraîner une augmentation de 1 de l’**ouverture directe** sur la page de résultats de votre campagne. Consultez notre article sur [signaler une notification push]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_reporting/) pour une description de l’analytique des notifications push.

Pour les problèmes liés à l’analytique des notifications push, consultez notre [guide de résolution des problèmes][57].

#### Tester depuis la ligne de commande

Si vous souhaitez tester des notifications push et in-app à l’aide de la ligne de commande, vous pouvez envoyer une seule notification par le terminal via cURL et l’[API d’envoi de messages][22]. Vous devrez remplacer les champs suivants par les valeurs correctes pour votre cas de test :

- `YOUR_API_KEY` : disponible sur la **Developer Console**
- `YOUR_EXTERNAL_USER_ID` : disponible sur la page **User Profile Search (Recherche de profil utilisateur)**
- `YOUR_KEY1` (facultatif)
- `YOUR_VALUE1` (facultatif)

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

Cet exemple utilise l’instance `US-01`. Si vous n’êtes pas sur cette instance, remplacez l’endpoint `US-01` avec [votre endpoint][66].

## Personnaliser votre intégration

### Affichage personnalisé des notifications

#### Étape 1 : Créer votre fabrique de notification personnalisée

Dans certains scénarios, vous pourriez désirer personnaliser les notifications push d’une manière qui pourrait être encombrante ou non disponible côté serveur. Pour vous donner un contrôle complet de l’affichage des notifications, nous avons ajouté la possibilité de définir votre propre [`IBrazeNotificationFactory`][6] pour créer des objets de notification à afficher par Braze.

Si une `IBrazeNotificationFactory` personnalisée est définie, Braze appellera la méthode `createNotification()` de votre fabrique lors de la réception de la notification push avant qu’elle ne soit affichée à l’utilisateur. Braze transmettra un `Bundle` contenant les données de notification push Braze et un autre `Bundle` contenant les paires clé-valeur personnalisées envoyées soit via le tableau de bord soit par les API de messagerie :

Braze transmettra un [`BrazeNotificationPayload`][77] contenant les données de la notification push Braze.

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

Vous pouvez renvoyer `null` de votre méthode `createNotification()` personnalisée pour ne pas afficher la notification du tout, utiliser `BrazeNotificationFactory.getInstance().createNotification()` pour obtenir la valeur par défaut de l’objet `notification` de Braze pour ces données et le modifier avant affichage ou générer un objet `notification` complètement séparé à afficher.

{% alert note %}
Pour consulter la documentation sur les clés de données de la notification push Braze, reportez-vous au [SDK Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-constants/index.html).
{% endalert %}

#### Étape 2 : Définir votre fabrique de notification personnalisée

Pour demander à Braze d’utiliser votre fabrique de notification personnalisée, utilisez la méthode `setCustomBrazeNotificationFactory` pour définir votre[`IBrazeNotificationFactory`][6] :

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
Créer votre propre notification à partir de zéro est un cas d’usage avancé et ne doit être fait qu’après des tests minutieux et avec une compréhension approfondie des fonctionnalités de notification push Braze. Par exemple, vous devez vous assurer que votre notification enregistre correctement les ouvertures de notifications push.
{% endalert %}

Pour annuler la définition de votre [`IBrazeNotificationFactory`][6] personnalisé et retourner à la gestion par défaut de Braze pour gérer les notifications push, transmettez `null` à notre système de définition de fabrique de notification personnalisée :

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

[6]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze-notification-factory/index.html
[8]: {{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/
[16]: {% image_buster /assets/img_archive/fcm_api_insert.png %} "FCMKey"
[22]: {{site.baseurl}}/api/endpoints/messaging/
[28]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/fireos/integration/
[37]: https://developer.android.com/guide/topics/ui/notifiers/notifications
[38]: {% image_buster /assets/img_archive/large_and_small_notification_icon.png %} "Large and Small Notification Icon"
[40]: http://developer.android.com/training/app-indexing/deep-linking.html "Google Deep Linking Documentation"
[41]: {% image_buster /assets/img_archive/deep_link_click_action.png %} "Deep Link Click Action"
[42]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#what-is-deep-linking
[45]: https://firebase.google.com/docs/cloud-messaging/
[48]: https://developers.google.com/cloud-messaging/android/android-migrate-fcm
[49]: https://firebase.google.com/docs/android/setup
[52]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#android-push-listener-callback
[55]: {% image_buster /assets/img_archive/android_push_test.png %} "Android Push Test"
[56]: {{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#creating-a-push-message
[57]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/troubleshooting/
[58]: https://console.firebase.google.com/
[59]: {% image_buster /assets/img_archive/finding_firebase_server_key.png %} "FirebaseServerKey"
[61]: {{site.baseurl}}/user_guide/message_building_by_channel/push/android/notification_channels/
[62]: https://developer.android.com/preview/features/notification-channels.html
[63]: {{site.baseurl}}/api/objects_filters/messaging/android_object/
[64]: {{site.baseurl}}/user_guide/message_building_by_channel/push/android/notification_channels/#dashboard-fallback-channel
[65]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/runtime_configuration/
[66]: {{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/
[67]: https://developer.android.com/reference/android/app/Application.html#onCreate()
[68]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/runtime_configuration/#runtime-configuration
[70]: https://github.com/braze-inc/braze-android-sdk/blob/master/samples/firebase-push/src/main/AndroidManifest.xml "AndroidManifest.xml"
[72]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/set-default-notification-channel-name.html
[73]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/set-default-notification-channel-description.html
[74]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.push/-braze-firebase-messaging-service/handle-braze-remote-message.html
[75]: https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage
[76]: https://developer.android.com/reference/android/app/Application
[77]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.push/-braze-notification-payload/index.html
[78]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-constants/index.html
[79]: {% image_buster /assets/img_archive/cloud_messaging_legacy_disabled.png %} "Firebase Legacy Disabled"
[80]: {% image_buster /assets/img_archive/cloud_messaging_legacy_enabled.png %} "Firebase Server Key"
