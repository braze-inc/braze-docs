---
nav_title: Intégration de Baidu
article_title: Intégration des notifications de Baidu Push pour Android
platform: Android
page_order: 9
description: "Cet article montre comment mettre en place une intégration de Baidu Android."
channel:
  - Pousser
---

# Intégration de Baidu

Braze est capable d'envoyer des notifications push à des appareils Android en utilisant \[Baidu Cloud Push\]\[14\].

> L'utilisation de Baidu Cloud Push __ne nécessite pas__ que vous distribuiez vos applications via l'App Store Baidu.

## Étape 1 : Créer un compte Baidu

Visitez le [Portail Baidu][7]. Vous verrez une page d'accueil similaire à ce qui suit. Cliquez sur __<unk> <unk>__ (Connexion) parmi les options du menu en haut à droite pour ouvrir une boîte de dialogue qui vous permettra de vous connecter ou de créer un nouveau compte.

!\[Baidu Portal\]\[33\]

Pour créer un nouveau compte, dans la fenêtre de connexion, cliquez sur __<unk> <unk> <unk> <unk>__ (Nouveau compte) directement en bas à droite du grand bouton bleu <unk> <unk> (Connexion).

!\[Baidu Login Dialog\]\[38\]

Entrez une adresse e-mail, un mot de passe et un captcha sur la page de création de compte. Acceptez le contrat de licence et cliquez sur __<unk> <unk>__ (Créer un compte) pour vous inscrire.

!\[Page d'inscription de Baidu\]\[17\]

Vous recevrez un courriel de Baidu. Suivez le lien de vérification. Assurez-vous de suivre le lien de vérification dans les 48 heures.

!\[Courriel Baidu Verification\]\[34\]

Sur la page suivante, vous terminerez une vérification par SMS. Choisissez votre code de pays (<unk> <unk> dans l'image d'exemple signifie les États-Unis). Entrez votre numéro de téléphone et cliquez sur __<unk> <unk> <unk> <unk> <unk> <unk>__ (Envoyer SMS). Vous devriez recevoir un message texte contenant un numéro à six chiffres, que vous entrerez dans le <unk> <unk> <unk> (Code). Assurez-vous de saisir votre code de vérification dans les 30 minutes. Cliquez sur __<unk> <unk>__ (Soumettre) pour soumettre. Félicitations ! Vous avez maintenant un compte Baidu.

!\[Baidu Verification SMS\]\[35\]

## Étape 2 : Inscrivez-vous en tant que développeur Baidu

Visitez le [Portail du Développeur Baidu][36]. Ouvrez le menu déroulant en haut à droite de l'écran. Choisissez __<unk> <unk> <unk> <unk>__ (Créer un nouveau compte développeur) pour commencer l'inscription.

!\[Portail du Développeur Baidu\]\[37\]

Sur la page d'inscription, choisissez votre type de compte (<unk> <unk> pour personnel, <unk> <unk> pour l'entreprise) et le type de développeur (le développeur est présélectionné et correct pour la plupart des cas). Entrez votre nom, un bio et un numéro de téléphone avec l'indicatif du pays entre parenthèses (par exemple, (1)xxxxxxxxxxxx). Cliquez sur __<unk> <unk> <unk> <unk> <unk>__ (Send Verification Code) et entrez le code de vérification dans la ligne suivante. Les deux champs suivants, le site web du développeur et le logo du développeur sont optionnels. Acceptez le contrat de licence et cliquez sur <unk> <unk> (Soumettre) pour soumettre. Félicitations ! Vous avez maintenant un compte développeur Baidu.

!\[Inscription du développeur Baidu\]\[13\]

## Étape 3 : Enregistrez votre candidature avec Baidu

Visitez le [Portail du Projet Baidu][11]. Cliquez sur __<unk> <unk> <unk> <unk>__ (Créer un projet).

!\[Portail du Projet Baidu\]\[10\]

Sur la page suivante, entrez le nom de votre application. Les deux cases à cocher suivantes sont d'activer les services supplémentaires de Baidu. Dans la plupart des cas, ceux-ci devraient être laissés vides.

!\[Nom de l'App Baidu\]\[26\]

Lors de la configuration de votre application, vous serez amené sur une console qui affiche des informations sur votre application, y compris la clé API. Cliquez sur le lien de poussée dans le nuage dans le menu à gauche de la console. Sur la page suivante, cliquez sur __<unk> <unk> <unk> <unk>__ (Définir Poussée vers le haut).

!\[Baidu App Console\]\[14\]

!\[Baidu Continue\]\[29\]

Sur la page suivante, entrez le nom du package de votre application (par exemple com.braze.sample) et indiquez s'il faut mettre en cache les messages et, si oui, combien de temps. Cela indique à Baidu combien de temps pour continuer à essayer d'envoyer des messages aux utilisateurs hors ligne. Cliquez sur __<unk> <unk> <unk> <unk>__ (Enregistrer les paramètres) pour enregistrer.

!\[Baidu Configurer le Cloud\]\[39\]

## Étape 4 : Ajoutez Baidu à votre application

Visitez le [Baidu Push SDK Portal][40] et téléchargez la dernière version de Baidu Cloud Push Android SDK.

!\[Baidu SDK Portal\]\[41\]

Dans le SDK, vous trouverez le jar du service push et les bibliothèques natives spécifiques à la plate-forme. Intégrez ces éléments dans votre projet. Assurez-vous que votre application cible la version SDK la plus élevée actuellement prise en charge par Baidu. Cette documentation est à jour pour Baidu Cloud Push Android SDK version `4.6.2.38`.

Ajoutez les permissions Baidu suivantes requises à votre application `AndroidManifest.xml`.

```xml
    <uses-permission android:name="android.permission.READ_PHONE_STATE" />
    <uses-permission android:name="android.permission.RECEIVE_BOOT_COMPLETED" />
    <uses-permission android:name="android.permission.WRITE_SETTINGS" />
    <uses-permission android:name="android.permission.VIBRATE" />
    <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
    <uses-permission android:name="android.permission.DISABLE_KEYGUARD" />
    <uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
    <uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />
```

La bibliothèque de Baidu contient des récepteurs de diffusion qui gèrent les messages push entrants. Déclarer les récepteurs internes Baidu dans l'élément `AndroidManifest.xml` de votre application à l'intérieur de l'élément `<application>`.

```xml
  <!-- 用于接收系统消息以保证 PushService 正常运行 -->
      <receiver
        android:name="com.baidu.android.pushservice.PushServiceReceiver"
        android:process=":bdservice_v1">
        <intent-filter>
          <action android:name="android.intent.action.BOOT_COMPLETED"/>
          <action android:name="android.net.conn.CONNECTIVITY_CHANGE"/>
          <action android:name="com.baidu.android.pushservice.action.notification.SHOW"/>
          <action android:name="com.baidu.android.pushservice.action.media.CLICK"/>
        </intent-filter>
      </receiver>
      <!-- Push 服务接收客户端发送的各种请求-->
      <!-- 注意:RegistrationReceiver 在 2.1.1 及之前版本有拼写失误,为 RegistratonReceiver ,用 新版本 SDK 时请更改为如下代码-->
      <receiver
        android:name="com.baidu.android.pushservice.RegistrationReceiver"
        android:process=":bdservice_v1">
        <intent-filter>
          <action android:name="com.baidu.android.pushservice.action.METHOD"/>
          <action android:name="com.baidu.android.pushservice.action.BIND_SYNC"/>
        </intent-filter>
        <intent-filter>
          <action android:name="android.intent.action.PACKAGE_REMOVED"/>
          <data android:scheme="package"/>
        </intent-filter>
      </receiver>
      <!-- Push 服务 -->
      <!-- 注意:在 4.0 (包含)之后的版本需加上如下所示的 intent-filter action -->
      <service
        android:name="com.baidu.android.pushservice.PushService"
        android:exported="true"
        android:process=":bdservice_v1">
        <intent-filter >
          <action android:name="com.baidu.android.pushservice.action.PUSH_SERVICE"/>
        </intent-filter>
      </service>
```

Vous devrez également créer un récepteur de diffusion qui écoute les messages push entrants et les notifications. Déclarer votre propre récepteur dans l'élément `AndroidManifest.xml`de votre application, à l'intérieur de l'élément `<application>`. Ce récepteur devra étendre `com.baidu.android.pushservice.PushMessageReceiver` et mettre en œuvre des méthodes qui reçoivent des mises à jour d'événements du service push Baidu.

```xml
      <receiver android:name=".MyPushMessageReceiver">
        <intent-filter>
          <action android:name="com.baidu.android.pushservice.action.MESSAGE"/>
          <action android:name="com.baidu.android.pushservice.action.RECEIVE"/>
          <action android:name="com.baidu.android.pushservice.action.notification.CLICK"/>
        </intent-filter>
      </receiver>
```

In your main activity's `onCreate()` method, add the following line, which will register your application with Baidu and begin listening for incoming push messages. Assurez-vous de remplacer « Votre clé API » par la clé d'API Baidu de votre projet.

```
PushManager.startWork(getApplicationContext(), PushConstants.LOGIN_TYPE_API_KEY, "Votre clé API");
```

Enfin, vous devrez enregistrer vos utilisateurs auprès de Braze. Dans la méthode `onBind()` du récepteur de diffusion Baidu que vous avez créé dans la partie 5, envoyer le `channelId` à Braze en utilisant `Braze. egisterAppboyPushMessages(channelId)`.

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(contexte).registerAppboyPushMessages(channelId);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(contexte).registerAppboyPushMessages(channelId)
```

{% endtab %}
{% endtabs %}

## Étape 5 : Inscription de push s'ouvre

Baidu prend en charge l'envoi de paires clés supplémentaires avec messages push au format JSON. Votre récepteur de diffusion `public vide onNotificationClicked(Contexte contextuel, titre de la chaîne, description de la chaîne, String customContentString)` la méthode sera appelée chaque fois qu'un utilisateur clique sur un message push entrant. Le paramètre `customContentString` contient les options au format JSON. Tous les messages de Braze contiendront les deux paires clé-valeur suivantes :

  ```json
  {
    "source": "Appboy",
    "cid": "votre-identifiant-campagne"
}
  ```
Chaque fois que `onNotificationClicked` est appelé votre récepteur Baidu, votre récepteur devrait envoyer une [intention][44] à votre application contenant `customContentString`. Votre application va enregistrer le clic sur Braze en utilisant la `customContentString`.

L'exemple suivant passe `customContentString` à Braze et enregistre un clic.

{% tabs %}
{% tab JAVA %}

  ```java
  String customContentString = intent.getStringExtra(ChinaPushMessageReceiver.NOTIFICATION_CLICKED_KEY);
  BrazeNotificationUtils.logBaiduNotificationClick(mApplicationContext, customContentString);
  ```

{% endtab %}
{% tab KOTLIN %}

```kotlin
val customContentString = intent.getStringExtra(ChinaPushMessageReceiver.NOTIFICATION_CLICKED_KEY)
BrazeNotificationUtils.logBaiduNotificationClick(context customContentString)
```

{% endtab %}
{% endtabs %}

## Étape 6: Extras

Outre les clés réservées utilisées par Braze, le paramètre `customContentString` contiendra également toutes les paires de valeur clé personnalisée définies par l'utilisateur. Pour extraire vos paires clés-valeurs, enveloppez `customContentString` dans un JSONObject et récupérez vos extras.

{% tabs %}
{% tab JAVA %}

```java
essayez {
  JSONObject myExtras = new JSONObject(customContentString);
  String myValue = myExtras. ptString("my_key", null);
} catch (Exception e) {
  Log.e(TAG, "Attrape une exception de traitement customContentString");
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
essayer {
  val myExtras = JSONObject(customContentString)
  val myValue = myExtras. ptString("my_key", null)
} catch (e: Exception) {
  Log.e(TAG, "Attrape une exception de traitement customContentString", e)
}
```

{% endtab %}
{% endtabs %}

## Étape 7: Configurez les clés Baidu

Vous devez entrer votre clé d'API Baidu et Baidu Secret Key dans le tableau de bord de Braze. Les deux clés sont disponibles à partir de la console de l'application Baidu.

Sur la page **Paramètres** (où se trouvent vos clés API), sélectionnez votre application Android Chine. Entrez votre clé API Baidu et la clé secrète Baidu dans leurs champs respectifs dans la section Notifications push.

!\[APIKey\]\[19\]{: style="max-width:80%;"}

## Ressource

- [Baidu Portal][7]
- [Portail Développeur Baidu][36]
- [Portail du projet Baidu][11]
- [Portail Baidu Push SDK][40]
- [Docs d'intégration de Baidu][43]
\[10]: {% image_buster /assets/img_archive/baidu_project.png %} [13]: {% image_buster /assets/img_archive/baidu_dev_reg. ng %} [14\]\[14\] : {% image_buster /assets/img_archive/baidu_app_console.png %} [17]: {% image_buster /assets/img_archive/baidu_signup. ng %} [19]: {% image_buster /assets/img_archive/baidu_api_key.png %} "APIKey" [26]: {% image_buster /assets/img_archive/baidu_app_name. ng %} [29]: {% image_buster /assets/img_archive/baidu_continue. ng %} [33]: {% image_buster /assets/img_archive/baidu_portal.png %} [34]: {% image_buster /assets/img_archive/baidu_email. ng %} [35]: {% image_buster /assets/img_archive/baidu_text.png %} [37]: {% image_buster /assets/img_archive/baidu_dev_portal. ng %} [38]: {% image_buster /assets/img_archive/baidu_login_dialog. ng %} [39]: {% image_buster /assets/img_archive/baidu_configure_cloud.png %} [41]: {% image_buster /assets/img_archive/baidu_sdk.png %}

[7]: https://www.baidu.com/

[7]: https://www.baidu.com/
[11]: http://developer.baidu.com/console#app/project
[11]: http://developer.baidu.com/console#app/project
[36]: http://developer.baidu.com/
[36]: http://developer.baidu.com/
[40]: http://developer.baidu.com/wiki/index.php?title=docs/cplat/push/sdk/clientsdk
[40]: http://developer.baidu.com/wiki/index.php?title=docs/cplat/push/sdk/clientsdk
[43]: http://developer.baidu.com/wiki/index.php?title=docs/frontia/guide-android/overview
[44]: http://developer.android.com/reference/android/content/Intent.html
