---
nav_title: Intégration standard
article_title: Intégration standard des notifications push pour Android
platform: Android
page_order: 0
description: "Cet article couvre la façon d'intégrer les notifications push dans votre application Android."
channel:
  - Pousser
---

# Aperçu

![Exemple de Push d'image en ligne Android]({% image_buster /assets/img/android/push/inline_image_push_android_1.png %}){: style="float:right;max-width:35%;margin-left:15px;border: 0;"}

Une notification push est une alerte hors application qui apparaît à l'écran de l'utilisateur lorsqu'une mise à jour importante se produit. Les notifications push sont un moyen précieux de fournir à vos utilisateurs un contenu sensible au temps et pertinent ou de les réengager avec votre application.

Consultez [notre documentation d'aide][8] pour découvrir les meilleures pratiques.

Braze envoie des notifications push aux appareils Android en utilisant [Firebase Cloud Messaging (FCM)][45].

Les notifications push pour Amazon FireOS utilisent le service Amazon Device Messaging (ADM) plutôt que FCM. Consultez les [instructions d'intégration de Push FireOS][28] pour plus de détails sur l'activation des notifications push pour les applications FireOS.

Pour les appareils sans services Google installés, Braze offre l'option d'envoyer push via Baidu Cloud Push. Visitez [les instructions de poussée de Baidu Cloud][50] pour plus de détails.

## Inscription pour Push

Utilisez [Firebase Cloud Messaging](https://firebase.google.com/docs/cloud-messaging/) (FCM) pour vous inscrire à push. Pour un échantillon complet de l'utilisation de Firebase avec le Braze Android SDK, consultez notre [Firebase Push sample app](https://github.com/Appboy/appboy-android-sdk/tree/master/samples/firebase-push).

### Étape 1 : Activer Firebase

Pour commencer, suivez les instructions à [Ajouter Firebase à votre projet Android][49].

Ensuite, ajoutez la dépendance Firebase Messaging à votre module `build.gradle`:

```gradle
implémentation "com.google.firebase:firebase-core:${FIREBASE_CORE_VERSION}"
implémentation "com.google.firebase:firebase-messaging:${FIREBASE_PUSH_MESSAGING_VERSION}"
```

### Étape 2 : Configurer l'enregistrement des jetons

Les notifications push Braze ne fonctionneront pas tant qu'un jeton Firebase Cloud Messaging (jeton d'enregistrement FCM) n'est pas enregistré. Les jetons d'enregistrement FCM peuvent être enregistrés par Braze SDK automatiquement (recommandé) ou manuellement enregistrés. Les jetons peuvent être enregistrés manuellement en utilisant la méthode [`Braze.registerAppboyPushMessages()`][35].

> Assurez-vous d'utiliser votre ID d'expéditeur Firebase. Il s'agit d'une valeur numérique unique créée lorsque vous créez votre projet Firebase, disponible dans l'onglet Messagerie Cloud du volet Paramètres de la console Firebase. L'identifiant de l'expéditeur est utilisé pour identifier chaque expéditeur qui peut envoyer des messages à l'application client.

##### Option 1 : Inscription automatique

Pour enregistrer automatiquement les jetons d’enregistrement FCM, activez l’enregistrement automatique de Firebase et définissez un ID d’expéditeur de messagerie Firebase Cloud.

Dans votre `braze.xml`:

```xml
<bool translatable="false" name="com_appboy_firebase_cloud_messaging_registration_enabled">vrai</bool>
<string translatable="false" name="com_appboy_firebase_cloud_messaging_sender_id">votre_fcm_sender_id_here</string>
```

Ou dans votre [BrazeConfig][68]:

{% tabs %}
{% tab JAVA %}

```java
BrazeConfig brazeConfig = new BrazeConfig.Builder()
  .setIsFirebaseCloudMessagingRegistrationEnabled(true)
  .setFirebaseCloudMessagingSenderIdKey("VOTRE ID DE SENDER FIREBASE ICI")
  .build();
Braze.configure(ceci, brazeConfig);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
val brazeConfig = BrazeConfig.Builder()
    .setIsFirebaseCloudMessagingRegistrationEnabled(true)
    .setFirebaseCloudMessagingSenderIdKey("VOTRE FIREBASE SENDER ID ICI")
    .build()
Braze.configure(this, brazeConfig)
```

{% endtab %}
{% endtabs %}

Si vous utilisez une inscription automatique Firebase, vous pouvez ignorer les options manuelles ci-dessous.

#### Option 2 : enregistrement manuel

Nous vous recommandons d'appeler [`Brésil. egisterAppboyPushMessages()`][35] depuis votre application [`la méthode onCreate()`][67] pour s'assurer que les jetons de poussée sont distribués de manière fiable sur Braze.

Voir le snippet ci-dessous pour un exemple :

{% tabs %}
{% tab JAVA %}

```java
la classe publique MyApplication étend l'application {
  @Override
  public void onCreate() {
    super. nCreate();
    application de contexte final = ceci;
    FirebaseMessaging. etInstance().getToken().addOnCompleteListener(task -> {
      if (!task.isSuccessful()) {
        Log. (TAG, "Exception lors de l'enregistrement du jeton FCM au Brésil", tâche. etException());
        retourner;
      }

      jeton final de chaîne = tâche. etResult();
      Braze.getInstance(applicationContext).registerAppboyPushMessages(token);
    });
  }
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
class MyApplication: Application() {
  override fun onCreate() {
    super.onCreate()
    FirebaseMessaging. etInstance().token.addOnCompleteListener { task: Task<String?> ->
      if (!task. sSuccessful) {
        Journal. (TAG, "Exception lors de l'enregistrement du jeton FCM au Brésil", tâche. xception)
        return@addOnCompleteListener
      }
      jeton val = tâche. esult
      Braze.getInstance(applicationContext).registerAppboyPushMessages(token)
    }
  }
}
```

{% endtab %}
{% endtabs %}

> Bien que nous vous recommandons fortement d'enregistrer votre jeton d'enregistrement FCM dans votre application [`onCreate()`][67], le jeton peut être enregistré n'importe où dans votre code.

### Étape 3 : Migrer depuis GCM (facultatif)

Si vous migrez de GCM à l'utilisation de Firebase avec Braze, visitez le [Guide de migration GCM][48] pour des instructions sur la façon de passer correctement à l'utilisation de Firebase dans votre application.

### Étape 4 : Définissez vos identifiants de base de feu

Vous devez entrer votre clé de serveur Firebase et votre identifiant Sender dans le tableau de bord Braze :

* Sur la page **Paramètres** (où se trouvent vos clés API), sélectionnez votre application Android.
* Entrez votre clé de serveur Firebase dans le champ **Firebase Cloud Messaging Server Key** , dans la section Paramètres de notification Push.
* Entrez votre ID de Sender Firebase dans le champ **Firebase Cloud Messaging Sender ID** , dans la section Paramètres de notification Push.

!\[fcmimg\]\[16\]

Si vous n'êtes pas familier avec l'emplacement de votre clé de serveur Firebase et de l'identifiant de l'expéditeur, suivez ces étapes :

1. Connectez-vous à la [Console de Développeurs Firebase][58]

2. Sélectionnez votre projet Firebase

3. Allez dans **Paramètres** > **Messagerie Cloud** et copiez la clé du serveur et l'identifiant de l'expéditeur : !\[FirebaseServerKey\]\[59\]

### Étape 5 : Supprimer les anciennes permissions
- Braze ne nécessite plus les autorisations suivantes si vous utilisez Firebase :

  ```xml
  <uses-permission android:name="android.permission.GET_ACCOUNTS" />
  <uses-permission android:name="android.permission.WAKE_LOCK" />
  <uses-permission android:name="com.google.android.c2dm.permission.RECEIVE" />
  <permission android:name="YOUR-APPLICATION-PACKAGE-NAME.permission.C2D_MESSAGE" android:protectionLevel="signature"/>
  <uses-permission android:name="YOUR-APPLICATION-PACKAGE-NAME.permission.C2D_MESSAGE" />
  ```

### Étape 6 : Supprimer les actions automatiques de votre classe d'application

Si vous avez une sous-classe [Application][76] personnalisée, assurez-vous que vous n'avez pas de logique automatique qui fait pingler vos serveurs dans l'application `de votre classe. méthode du cycle de vie nCreate()`. Cela permettra de s'assurer que les notifications push silencieuses de Braze ne causent pas de requêtes inutiles à vos serveurs.

## Affichage du push

Après avoir complété cette section, vous devriez être en mesure de recevoir et d'afficher les notifications push envoyées par Braze.

### Étape 1 : Enregistrer Braze Firebase Messaging Service

{% alert important %}
Si vous avez déjà un service de messagerie Firebase enregistré, ne complétez pas cette étape. Au lieu de cela, passez à [en utilisant votre propre service de messagerie Firebase](#using-your-own-firebase-messaging-service) et complétez les étapes listées ici.
{% endalert %}

Braze comprend un service pour gérer les reçus push et les intentions ouvertes. Notre classe `BrazeFirebaseMessagingService` devra être enregistrée dans votre `AndroidManifest.xml`.

```xml
<service android:name="com.braze.push.BrazeFirebaseMessagingService"
  android:exported="false">
  <intent-filter>
    <action android:name="com.google.firebase.MESSAGING_EVENT" />
  </intent-filter>
</service>
```

Le code de notification de Braze utilise également `BrazeFirebaseMessagingService` pour gérer le suivi des actions ouvertes et des clics. Ce service doit être enregistré dans le `AndroidManifest.xml` pour que cela fonctionne correctement. De plus, gardez à l'esprit que Braze préfixe les notifications de notre système avec une clé unique pour s'assurer que nous ne rendons que les notifications envoyées par les systèmes de Brase. Vous pouvez enregistrer des services supplémentaires séparément pour afficher les notifications envoyées par d'autres services FCM.

{% alert important %}
Avant Braze SDK 3.1.1, `AppboyFcmReceiver` était utilisé pour gérer FCM push. La classe `AppboyFcmReceiver` doit être retirée de votre manifeste et remplacée par l'intégration ci-dessus.
{% endalert %}

**Exemple d'implémentation**

- Voir [`AndroidManifest.xml`][70] dans l'application d'échantillon Push Firebase.

##### Utiliser votre propre service de messagerie Firebase

Si vous avez déjà un service de messagerie Firebase enregistré, vous pouvez passer des objets [`RemoteMessage`][75] à Braze via [BrazeFirebaseMessagingService.handleBrazeRemoteMessage()][74]. Cette méthode n'affichera une notification que si l'objet [`Message distant`][75] originaire de Braze et ignorera en toute sécurité si ce n'est pas le cas.

{% tabs %}
{% tab JAVA %}

```java
la classe publique MyFirebaseMessagingService étend FirebaseMessagingService {
  @Override
  public void onMessageReceived(RemoteMessage) {
    super. nMessageReceived(remoteMessage);
    si (BrazeFirebaseMessagingService. andleBrazeRemoteMessage(this remoteMessage)) {
      // Ce message distant provient de Braze et une notification push a été affichée.
      // Aucune action supplémentaire n'est nécessaire.
    } else {
      // Ce message distant ne provient pas de Braze.
      // Aucune action n'a été prise et vous pouvez passer ce message distant à d'autres gestionnaires en toute sécurité.
    }
  }
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
classe MyFirebaseMessagingService : FirebaseMessagingService() {
  surcharge fun onMessageReceived(remoteMessage: RemoteMessage?) {
    super.onMessageReceived(remoteMessage)
    if (BrazeFirebaseMessagingService.handleBrazeRemoteMessage(this, remoteMessage)) {
      // Ce message distant est originaire de Braze et une notification push a été affichée.
      // Aucune action supplémentaire n'est nécessaire.
    } else {
      // Ce message distant ne provient pas de Braze.
      // Aucune action n'a été prise et vous pouvez passer ce message distant à d'autres gestionnaires en toute sécurité.
    }
  }
}
```

{% endtab %}
{% endtabs %}

### Étape 2 : Assurez-vous que les petites icônes sont conformes aux directives de conception

Pour des informations générales sur les icônes de notification Android, veuillez consulter la [documentation de l'Aperçu des notifications][37].

À partir d'Android N, vous devriez mettre à jour ou supprimer les petites icônes de notification qui impliquent la couleur. Le système Android (pas le Braze SDK) ignore tous les canaux non-alpha/transparence dans les icônes d'action et la petite icône de notification. En d'autres termes, Android convertira toutes les parties de votre petite icône de notification en monochrome, à l'exception des régions transparentes.

Pour créer correctement une petite icône de notification active:
- Supprime toutes les couleurs de l'image sauf le blanc.
- Toutes les autres régions non blanches du bien devraient être transparentes.

{% alert note %}
Un symptôme courant d'une ressource inappropriée est la petite icône de notification qui se traduit par un carré monochrome solide. Ceci est dû au fait que le système Android ne peut pas trouver de régions transparentes dans l'actif de petite icône de notification.
{% endalert %}

Les grandes et petites icônes illustrées ci-dessous sont des exemples d'icônes correctement conçues :

!\[Exemple d'icône Android\]\[38\]

### Étape 3 : Configurer les icônes de notification

#### Spécifier les icônes dans braze.xml

- Braze vous permet de configurer vos icônes de notification en spécifiant des ressources dessinables dans votre `braze.xml`:

```xml
<drawable name="com_appboy_push_small_notification_icon">REPLACE_WITH_YOUR_ICON</drawable>
<drawable name="com_appboy_push_large_notification_icon">REPLACE_WITH_YOUR_ICON</drawable>
```

Définir une petite icône de notification est nécessaire. __Si vous n'en avez pas défini, Braze utilisera par défaut l'icône de l'application en tant que petite icône de notification qui peut sembler sous-optimale.__

Définir une grande icône de notification est facultatif mais recommandé.

#### Spécification de la couleur d'arrière-plan de l'icône

- La couleur d'arrière-plan de l'icône de notification peut être remplacée dans votre `braze.xml`. Si la couleur n'est pas spécifiée, la couleur d'arrière-plan par défaut est la même couleur grise utilisée par Lollipop pour les notifications système. Veuillez voir l'exemple de remplacement de couleur ci-dessous:

```xml
<integer name="com_appboy_default_notification_accent_color">0xFFf33e3e</integer>
```

Vous pouvez également utiliser une référence de couleur, voir:

```xml
<color name="com_appboy_default_notification_accent_color">@color/my_color_ici</color>
```

### Étape 4 : Ajouter des liens profonds

#### Activation de l'ouverture automatique des liens profonds

Pour activer Braze pour ouvrir automatiquement votre application et tous les liens profonds quand une notification push est cliquée, mettez `com_appboy_handle_push_deep_links_automatically` à `true`, dans votre `braze. ml`:

```xml
<bool name="com_appboy_handle_push_deep_links_automatically">vrai</bool>
```

Ce drapeau peut également être défini via la configuration [runtime][65]:

{% tabs %}
{% tab JAVA %}

```java
BrazeConfig brazeConfig = new BrazeConfig.Builder()
        .setHandlePushDeepLinksAutomatial(true)
        .build();
Braze.configure(this, brazeConfig);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
val brazeConfig = BrazeConfig.Builder()
        .setHandlePushDeepLinksAutomatial(true)
        .build()
Braze.configure(ceci, brazeConfig)
```

{% endtab %}
{% endtabs %}

Si vous souhaitez gérer des liens profonds, vous aurez besoin de créer un `BroadcastReceiver` qui écoute les messages reçus et ouverts de Braze. Consultez notre section sur [Recettes et Ouvertures Push sur mesure][52] pour plus d'informations.

#### Création de liens profonds personnalisés

Veuillez suivre les instructions qui se trouvent dans la [Documentation pour les développeurs Android sur Deep Linking][40] si vous n'avez pas déjà ajouté de liens profonds à votre application. Pour plus d'informations sur ce qu'est un lien profond, veuillez consulter notre [FAQ Section][42].

#### Ajout de liens profonds

Le tableau de bord Braze prend en charge la définition de liens profonds ou d'URL Web sur les notifications push qui seront ouvertes lorsque la notification sera cliquée.

!\[Deep_Link_Dash_Example\]\[41\]

#### Personnalisation du comportement de la pile arrière

Le SDK Android par défaut placera l'activité principale de votre application hôte dans la pile arrière lorsque vous suivez les liens profonds. Braze vous permet de définir une activité personnalisée à ouvrir dans la pile arrière à la place de l'activité de votre lanceur principal ou de désactiver complètement la pile arrière.

Par exemple, pour définir une activité appelée `VotreActivité` comme activité de la pile arrière, voir l'exemple suivant en utilisant la [configuration d'exécution][65]:

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

Consultez la configuration équivalente pour votre `braze.xml`. Notez que le nom de la classe doit être le même que celui retourné par `Class.forName()`:

```xml
<bool name="com_appboy_push_deep_link_back_stack_activity_enabled">vrai</bool>
<string name="com_appboy_push_deep_link_back_stack_activity_class_name">votre.package.name.YourMainActivity</string>
```

### Étape 5 : Définir les canaux de notification

Le SDK Android Braze prend en charge [Android Notification Channels][62]. Dans le cas où une notification Braze ne contient pas l'ID d'un canal de notification ou qu'une notification Braze contient un ID de canal invalide, Braze affichera la notification avec le canal de notification par défaut défini dans le SDK. Les utilisateurs de Braze utilisent [les canaux de notification Android][61] au sein de la plateforme pour grouper les notifications.

Pour définir le nom de l'utilisateur face au canal de notification Braze par défaut, veuillez utiliser [`BrazeConfig.setDefaultNotificationChannelName()`][72].

Pour définir l'utilisateur face à la description du canal de notification Braze par défaut, veuillez utiliser [`BrazeConfig.setDefaultNotificationChannelDescription()`][73].

Vous devez vous assurer que toutes les campagnes API avec le paramètre [Android Push Object][63] sont mises à jour pour inclure le champ `notification_channel`. Si ce champ n'est pas spécifié, Braze enverra la charge utile de notification avec l'ID du canal [du tableau de bord][64] de repli.

À part le canal de notification par défaut, Braze ne créera aucun canal. Tous les autres canaux doivent être définis par programme par l'application hôte, puis entrés dans le tableau de bord de Braze.

### Étape 6 : Tester l'affichage et l'analyse des notifications

#### Test de l'affichage

À ce stade, vous devriez être en mesure de voir les notifications envoyées par Braze.  Pour tester ceci, allez sur la page **Campagnes** de votre tableau de bord Braze et créez une campagne **Notification** Push .  Choisissez **Android Push** et concevez votre message. Cliquez ensuite sur l’icône de l’œil dans le compositeur pour obtenir l’expéditeur du test.  Entrez l'ID utilisateur ou l'adresse e-mail de votre utilisateur actuel et cliquez sur **Envoyer le test**.  Vous devriez voir apparaître le push sur votre appareil.

!\[Test push Android\]\[55\]

Pour les problèmes liés à l'affichage push, consultez notre [Guide de dépannage][57].

#### Tests d'analyse

À ce stade, vous devriez également avoir la journalisation analytique pour les notifications push.  Pour tester ceci, consultez nos [Docs sur la création d'une campagne de push][56].  En cliquant sur la notification quand elle arrive, vous devriez avoir le **Direct Ouvre** sur la page de résultats de votre campagne pour augmenter de 1.

Pour les problèmes liés à l'analyse push, consultez notre [Guide de dépannage][57].

#### Tests depuis la ligne de commande

Si vous souhaitez tester les notifications dans l'application et push via la ligne de commande, vous pouvez envoyer une seule notification via le terminal via cURL et la [Messaging API][22]. Vous devrez remplacer les champs suivants par les valeurs correctes pour votre cas de test:

- `YOUR_API_KEY` - disponible sur la page Console Développeur
- `YOUR_EXTERNAL_USER_ID` - disponible sur la page de recherche du profil utilisateur
- `YOUR_KEY1` (facultatif)
- `YOUR_VALUE1` (facultatif)

```
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {{YOUR_API_KEY}}" -d "{\"external_user_ids\":[\"YOUR_EXTERNAL_USER_ID\"],\"messages\":{\"android_push\":{\"title\":\"Test push title\",\"alert\":\"Test push\",\"extra\":{\"YOUR_KEY1\":\"YOUR_VALUE1\"}}" https://rest.iad-01.braze.com/messages/send
```

Ce qui précède est un exemple pour les clients sur l'instance `US-01`. Si vous n'êtes pas sur cette instance, veuillez vous référer à notre [documentation API][66] pour voir à quel point de terminaison vous devez faire des demandes.

## Personnalisation de votre intégration

### Notifications d'affichage personnalisées

#### Étape 1 : Créez votre usine de notification personnalisée

Dans certains scénarios, vous pouvez personnaliser les notifications push d'une manière qui serait lourde ou indisponible côté serveur. Pour vous donner le contrôle complet de l'affichage des notifications, nous avons ajouté la possibilité de définir votre propre [`IBrazeNotificationFactory`][6] pour créer des objets de notification à afficher par Braze.

Si une `IBrazeNotificationFactory personnalisée` est définie, Braze appellera la méthode de votre usine `createNotification()` sur réception push avant que la notification ne soit affichée à l'utilisateur. Braze passera dans un `Bundle` contenant des données de poussée de Braze et un autre `Bundle` contenant des paires clé-valeur personnalisées envoyées soit via le tableau de bord ou les API de messagerie:

Braze passera dans un [`BrazeNotificationPayload`][77] contenant les données de la notification de Braze.

{% tabs %}
{% tab JAVA %}

```java
// Méthode d'usine implémentée dans votre IBrazeNotificationFactory personnalisé
@Override
public Notification createNotification(BrazeNotificationPayload brazeNotificationPayload) {
  // Exemple d'obtenir le titre de la notification
  String title = brazeNotificationPayload. etTitleText();

  // Exemple de récupération d'un KVP personnalisé ("my_key" -> "my_value")
  String customKvp = brazeNotificationPayload.getAppboyExtras().getString("my_key");
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
// Méthode d'usine implémentée dans votre IBrazeNotificationFactory personnalisé
surchargez fun createNotification(brazeNotificationPayload: BrazeNotificationPayload): Notification {
  // Exemple d'obtenir le titre de la notification
  titre val = brazeNotificationPayload. etTitleText()

  // Exemple de récupération d'un KVP personnalisé ("my_key" -> "my_value")
  val customKvp = brazeNotificationPayload.getAppboyExtras().getString("my_key")
}
```

{% endtab %}
{% endtabs %}

Vous pouvez retourner `null` de votre méthode personnalisée `createNotification()` pour ne pas afficher la notification. utiliser `BrazeNotificationFactory. etInstance(). reateNotification()` pour obtenir l'objet `notification` par défaut de Braze pour ces données et le modifier avant l'affichage, ou générer un objet `notification` complètement séparé pour l'affichage.

{% alert note %}
Braze pousser les clés de données sont documentées [ici](https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/Constants.html).
{% endalert %}

#### Étape 2 : Définissez votre usine de notification personnalisée

Pour demander à Braze d'utiliser votre usine de notification personnalisée, utilisez la méthode [sur l'interface Braze][5] pour définir votre [`IBrazeNotificationFactory`][6]:

{% tabs %}
{% tab JAVA %}


```java
format@@0 setCustomBrazeNotificationFactory(IBrazeNotificationFactory brzeNotificationFactory);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
format@@0 setCustomBrazeNotificationFactory(brazeNotificationFactory: IBrazeNotificationFactory)
```

{% endtab %}
{% endtabs %}

Le lieu recommandé pour définir votre `IBrazeNotificationFactory personnalisé` est dans la méthode `Application.onCreate()` du cycle de vie de l'application (pas l'activité).  Cela permettra à l'usine de notification d'être paramétrée correctement chaque fois que le processus de votre application est actif.

{% alert important %}
La création de votre propre notification à partir de zéro est un cas d'utilisation avancé et ne devrait être faite qu'avec des tests approfondis et une compréhension approfondie de la fonctionnalité push de Brase. Par exemple, vous devez vous assurer que vos logs de notification s'ouvrent correctement.
{% endalert %}

Pour supprimer votre [personnalisé`IBrazeNotificationFactory`][6] et revenir à la gestion par défaut de Braze pour push, passer `null` à notre configurateur d'usine de notification personnalisée :

{% tabs %}
{% tab JAVA %}


```java
Personnaliser la Facture de notification de Braze (nulle) ;
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Définir une Facture de notification de Braze (nulle)
```

{% endtab %}
{% endtabs %}

### Gestion personnalisée des reçus, des ouvertures, des licenciements et des paires clé-valeur

Braze diffuse des faits personnalisés lorsque les notifications push sont reçues, ouvertes ou rejetées. Si vous avez un cas d'utilisation spécifique pour ces scénarios (comme le besoin d'écouter des paires clé-valeur personnalisées ou la gestion propriétaire de liens profonds), vous devrez écouter ces faits en créant un `BroadcastReceiver` personnalisé.

#### Étape 1 : Enregistrez votre BroadcastReceiver

Enregistrez votre `BroadcastReceiver personnalisé` pour écouter les effets de Braze ouverts et reçus dans votre [`AndroidManifest.xml`][71].

```xml
<receiver android:name="YOUR-BROADCASTRECEIVER-NAME" android:exported="false" >
  <intent-filter>
    <action android:name="com.braze.push.intent.NOTIFICATION_RECEIVED" />
    <action android:name="com.braze.push.intent.NOTIFICATION_OPENED" />
    <action android:name="com.braze.push.intent.NOTIFICATION_DELETED" />
  </intent-filter>
</receiver>
```

#### Étape 2 : Créer votre BroadcastReceiver

Votre récepteur devrait gérer les intentions diffusées par Braze et lancer votre activité avec eux :

- Il devrait sous-classe [`BroadcastReceiver`][53] et remplacer `onReceive()`.
- La méthode `onReceive()` doit écouter les intentions diffusées par Brésil.
  - Une intention `NOTIFICATION_RECEIVED` sera reçue lorsqu'une notification push arrive.
  - Une intention `NOTIFICATION_OPENED` sera reçue lorsqu'une notification push est cliquée par l'utilisateur.
  - Une intention `NOTIFICATION_DELETED` sera reçue lorsqu'une notification push est rejetée (balayée) par l'utilisateur.
- Le récepteur doit exécuter votre logique personnalisée pour chacun de ces cas.  Si votre récepteur ouvre des liens profonds, Assurez-vous de désactiver l'ouverture automatique de liens profonds en définissant `com_appboy_handle_push_deep_links_automatically` à `false` dans votre `frein. ml`.

Pour un exemple de récepteur personnalisé détaillé, veuillez consulter le lien suivant :

{% tabs %}
{% tab JAVA %}

```java
la classe publique CustomBroadcastReceiver extends BroadcastReceiver {
  private static final String TAG = CustomBroadcastReceiver.class. etName();

  @Override
  public void onReceive(Contexte contexte, Intention) {
    String pushReceivedAction = Constantes. RAZE_PUSH_INTENT_NOTIFICATION_RECEIVED;
    String notificationOpenedAction = Constants.BRAZE_PUSH_INTENT_NOTIFICATION_OPENED;
    String notificationDeletedAction = Constantes. RAZE_PUSH_INTENT_NOTIFICATION_DELETED ;

    Action String = intent.getAction();
    Log.d(TAG, String. ormat("Intention reçue avec l'action %s", action));

    if (pushReceivedAction.equals(action)) {
      Log. (TAG, "Received push notification.");
    } else if (notificationOpenedAction.equals(action)) {
      BrazeNotificationUtils. outeUserWithNotificationOpenedIntent(context intent);
    } else if (notificationDeletedAction.equals(action)) {
      Log.d(TAG, "Received push notification deleted intent. );
    } else {
      Log.d(TAG, String. ormat("Intention ignorée avec l'action non supportée %s", action));
    }
  }
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
class CustomBroadcastReceiver : BroadcastReceiver() {
  override fun onReceive(context: Context, intent: Intent) {
    val pushReceivedAction = Constantes. RAZE_PUSH_INTENT_NOTIFICATION_RECEIVED
    notificationOpenedAction val = Constants.BRAZE_PUSH_INTENT_NOTIFICATION_OPENED
    notification val notificationDeletedAction = Constantes. RAZE_PUSH_INTENT_NOTIFICATION_DELETED

    action val = intent.action
    Log.d(TAG, String. ormat("Intention reçue avec l'action %s", action))

    quand (action) {
      pushReceivedAction -> {
        Journal. (TAG, "Notification push reçue.")
      }
      notificationOpenedAction -> {
        BrazeNotificationUtils.routeUserWithNotificationOpenedIntent(context, intent)
      }
      notificationDeletedAction -> {
        Log.d(TAG, "Received push notification deleted intent.")
      }
      else -> {
        Log.d(TAG, String. ormat("Ignore l'intention avec l'action non prise en charge %s", action))
      }
    }
  }

  compagnon de l'objet {
    val privé TAG = CustomBroadcastReceiver::class. ava.name
  }
}
```

{% endtab %}
{% endtabs %}

{% alert tip %}
Avec les boutons d'action de notification, `BRAZE_PUSH_INTENT_NOTIFICATION_OPENED` se déclenche lorsque des boutons avec `des actions` ou `lien profond` sont cliqués. La gestion des liens profonds et des extras reste la même. Les boutons avec les actions `fermer` ne tirent pas les intentions `BRAZE_PUSH_INTENT_NOTIFICATION_OPENED` et rejettent la notification automatiquement.
{% endalert %}

#### Étape 3 : Accédez aux paires de valeur de clé personnalisée

Les paires clé-valeur personnalisées envoyées soit via le tableau de bord ou les API de messagerie seront accessibles dans votre récepteur de diffusion personnalisé quel que soit l'objectif que vous choisissez:

{% tabs %}
{% tab JAVA %}

```java
// l'intention est le but de Braze push reçu par votre récepteur de diffusion personnalisé.
String deepLink = intent.getStringExtra(Constants.APPBOY_PUSH_DEEP_LINK_KEY);

// Le bundle d'extras extrait de l'intention contient toutes les paires de valeurs clés personnalisées.
Bundle extras = intent.getBundleExtra(Constants.APPBOY_PUSH_EXTRAS_KEY);

// exemple de récupération de la paire clé-valeur spécifique du paquet d'extras.
String myExtra = extras.getString("mon_clé");
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
// l'intention est le but de Braze push reçu par votre récepteur de diffusion personnalisé.
val deepLink = intent.getStringExtra(Constants.APPBOY_PUSH_DEEP_LINK_KEY)

// Le bundle d'extras extrait de l'intention contient toutes les paires clé-valeur personnalisées.
val extras = intent.getBundleExtra(Constants.APPBOY_PUSH_EXTRAS_KEY)

// exemple de récupération de la paire clé-valeur spécifique du paquet d'extras.
val myExtra = extras.getString("my_key")
```

{% endtab %}
{% endtabs %}

{% alert note %}
Braze pousser les clés de données sont documentées [ici](https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/Constants.html).
{% endalert %}
[16]: {% image_buster /assets/img_archive/fcm_api_insert.png %} "FCMKey" [38]: {% image_buster /assets/img_archive/large_and_small_notification_icon. ng %} "Icône de notification grande et petite" [41]: {% image_buster /assets/img_archive/deep_link_click_action. ng %} "Action du lien profond" [55]: {% image_buster /assets/img_archive/android_push_test. ng %} "Android Push Test" [59]: {% image_buster /assets/img_archive/finding_firebase_server_key.png %} "FirebaseServerKey"

[5]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/Appboy.html#setCustomBrazeNotificationFactory-com.braze.IBrazeNotificationFactory-
[6]: https://appboy.github.io/appboy-android-sdk/javadocs/com/braze/IBrazeNotificationFactory.html
[6]: https://appboy.github.io/appboy-android-sdk/javadocs/com/braze/IBrazeNotificationFactory.html
[8]: {{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/
[22]: {{site.baseurl}}/api/endpoints/messaging/
[28]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/fireos/integration/
[35]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/Appboy.html#registerAppboyPushMessages-java.lang.String- "Manual Registration Method"
[35]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/Appboy.html#registerAppboyPushMessages-java.lang.String- "Manual Registration Method"
[37]: https://developer.android.com/guide/topics/ui/notifiers/notifications
[40]: http://developer.android.com/training/app-indexing/deep-linking.html "Google Deep Linking Documentation"
[42]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#what-is-deep-linking
[45]: https://firebase.google.com/docs/cloud-messaging/
[48]: https://developers.google.com/cloud-messaging/android/android-migrate-fcm
[49]: https://firebase.google.com/docs/android/setup
[50]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/baidu_integration/
[52]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/#custom-handling-for-push-receipts-opens-dismissals-and-key-value-pairs
[53]: https://developer.android.com/reference/android/content/BroadcastReceiver.html
[56]: {{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#creating-a-push-message
[57]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/troubleshooting/
[58]: https://console.firebase.google.com/
[61]: {{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#android-notification-options
[62]: https://developer.android.com/preview/features/notification-channels.html
[63]: {{site.baseurl}}/api/objects_filters/messaging/android_object/
[64]: {{site.baseurl}}/user_guide/message_building_by_channel/push/notification_channels/#dashboard-fallback-channel
[65]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/runtime_configuration/
[65]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/runtime_configuration/
[66]: {{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/
[67]: https://developer.android.com/reference/android/app/Application.html#onCreate()
[67]: https://developer.android.com/reference/android/app/Application.html#onCreate()
[68]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/runtime_configuration/#runtime-configuration
[70]: https://github.com/Appboy/appboy-android-sdk/blob/master/samples/firebase-push/src/main/AndroidManifest.xml "AndroidManifest.xml"
[71]: https://github.com/Appboy/appboy-android-sdk/blob/master/samples/custom-broadcast/src/main/AndroidManifest.xml "AndroidManifest.xml"
[72]: https://appboy.github.io/appboy-android-sdk/javadocs/com/braze/configuration/BrazeConfig.Builder.html#setDefaultNotificationChannelName-java.lang.String-
[73]: https://appboy.github.io/appboy-android-sdk/javadocs/com/braze/configuration/BrazeConfig.Builder.html#setDefaultNotificationChannelDescription-java.lang.String-
[74]: hhttps://appboy.github.io/appboy-android-sdk/javadocs/com/braze/push/BrazeFirebaseMessagingService.html#handleBrazeRemoteMessage-android.content.Context-RemoteMessage-
[75]: https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage
[75]: https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage
[76]: https://developer.android.com/reference/android/app/Application
[77]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/models/push/BrazeNotificationPayload.html
