---
nav_title: Intégration Baidu
article_title: Intégration de notifications push Baidu pour Android
platform: Android
permalink: /baidu_integration/
description: "Cet article montre comment configurer une intégration Baidu pour Android."
hidden: true
---
# Intégration Baidu
{% multi_lang_include archive/baidu_deprecation.md %}

Braze peut envoyer des notifications push aux appareils Android à l'aide de [Baidu Cloud Push][14]. Notez que l’utilisation de notifications push Cloud Baidu **ne nécessite pas** la distribution de vos applications via l’App Store Baidu.

## Étape 1 : Créer un compte Baidu

Pour créer un compte Baidu, visitez le [portail Baidu][7] et cliquez sur **登录** (Se connecter) pour faire apparaître une boîte de dialogue qui vous permettra de vous connecter ou de créer un nouveau compte.

![][33]

Pour créer un nouveau compte, en bas de la boîte de dialogue d'identification, cliquez sur **立即注册** (nouveau compte).

![][38]{: style="max-width:70%;"}

Saisissez votre nom d’utilisateur, votre numéro de téléphone et votre mot de passe dans la page de création de compte. Ensuite, cliquez sur le bouton « Recevoir le code de vérification ». Vous recevrez alors un SMS de Baidu contenant un code de vérification. Enfin, acceptez l'accord de licence et cliquez sur **注册** (créer un compte) pour vous enregistrer. Si ces étapes de configuration échouent, essayez de vous enregistrer à l’aide de la connexion Cloud Baidu telle que décrite dans cet [article sur la connexion](https://www.adchina.io/how-to-open-a-baidu-account-outside-china/).

![Page d'inscription de Baidu][17]{: style="max-width:80%;"}

## Étape 2 : S’enregistrer en tant que développeur Baidu

Ensuite, vous devez vous inscrire en tant que développeur Baidu. Tout d'abord, visitez le [portail des développeurs du Baidu][36] et choisissez **注册** (créer un nouveau compte de développeur) pour commencer l'enregistrement.

![][37]

Sur la page d’inscription, choisissez votre type de compte (个人 pour les particuliers, 公司 pour les entreprises) et le type développeur (développeur est présélectionné et correct dans la plupart des cas). Saisissez votre nom, une biographie et un numéro de téléphone avec le code de pays entre parenthèses (par exemple, (1)xxxxxxxxxx). Cliquez sur **发送验证码** (envoyer le code de vérification) et entrez le code de vérification dans la ligne suivante. Les deux champs suivants, le site Internet du développeur et le logo du développeur, sont facultatifs. Acceptez l'accord de licence et cliquez sur **提交** (envoyer) pour valider. Vous avez maintenant un compte de développeur Baidu.

![][13]

## Étape 3 : Enregistrer votre application avec Baidu

Pour enregistrer votre application auprès de Baidu, visitez le [portail de projets Baidu][11] et cliquez sur **创建工程** (créer un projet).

![][10]

Sur la page suivante, saisissez le nom de votre application. Les deux cases à cocher suivantes sont destinées à activer des services Baidu supplémentaires. Dans la plupart des cas, elles doivent rester vides.

![][26]

Lors de la configuration de votre application, vous serez redirigé vers une console qui affiche des informations sur votre application, y compris la clé API. Ensuite, cliquez sur **云推送** (cloud push) dans la barre latérale. Sur la page suivante, cliquez sur **推送设置** (set up push).

![][14]

![][29]

Sur la page suivante, saisissez le nom du paquet de votre application (par exemple, `com.braze.sample`) et indiquez si les messages doivent être mis en cache et, le cas échéant, pendant combien de temps (en heures). Cela indique à Baidu pendant combien de temps continuer à essayer d’envoyer des messages aux utilisateurs hors ligne. Cliquez sur **保存设置** (enregistrer les paramètres) pour enregistrer.

![][39]

## Étape 4 : Ajouter Baidu à votre application

Visitez le [portail SDK de notification push Baidu][40] et téléchargez le dernier SDK Android de notifications push Cloud Baidu.

![][41]

Dans le SDK, vous trouverez le .jar de service de notification push et les bibliothèques natives spécifiques à la plateforme. Intégrez-les à votre projet. Assurez-vous que votre application cible la version SDK la plus élevée actuellement prise en charge par Baidu. Cette documentation est à jour concernant la version du SDK Android pour la notification push cloud de Baidu `4.6.2.38`.

Ajoutez les autorisations Baidu suivantes au `AndroidManifest.xml` de votre application.

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

La bibliothèque de Baidu contient des récepteurs de diffusion qui traitent les messages de notification push entrants. Déclarer les récepteurs Baidu internes dans le `AndroidManifest.xml` de votre application à l’intérieur de l’élément `<application>`.

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

Vous devrez également créer un récepteur de diffusion qui écoute les messages et les notifications de notifications push entrants. Déclarer votre récepteur dans le `AndroidManifest.xml` de votre application à l’intérieur de l’élément `<application>`. Ce récepteur devra étendre `com.baidu.android.pushservice.PushMessageReceiver` et implémenter des méthodes qui reçoivent des mises à jour d’événements depuis le service de notification push Baidu.

```xml
      <receiver android:name=".MyPushMessageReceiver">
        <intent-filter>
          <action android:name="com.baidu.android.pushservice.action.MESSAGE"/>
          <action android:name="com.baidu.android.pushservice.action.RECEIVE"/>
          <action android:name="com.baidu.android.pushservice.action.notification.CLICK"/>
        </intent-filter>
      </receiver>
```

Dans la méthode `onCreate()` de votre activité principale, ajoutez la ligne suivante qui enregistrera votre application auprès de Baidu et commencera à écouter les messages de notifications push entrants. Assurez-vous de remplacer « Your-API-Key » (Votre clé API) par la clé API Baidu de votre projet.

```
PushManager.startWork(getApplicationContext(), PushConstants.LOGIN_TYPE_API_KEY, "Your-API-Key");
```

Enfin, vous devrez enregistrer vos utilisateurs auprès de Braze. Dans la méthode `onBind()` de votre récepteur de diffusion Baidu que vous avez créée dans cette étape, envoyez `channelId` à Braze en utilisant `Braze.registerAppboyPushMessages(channelId)`.

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).setRegisteredPushToken(channelId);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).setRegisteredPushToken(channelId)
```

{% endtab %}
{% endtabs %}

## Étape 5 : Enregistrer l’ouverture de notifications push

Baidu prend en charge l’envoi de paires clé-valeur supplémentaires avec des messages de notification push au format JSON. La méthode `public void onNotificationClicked(Context context, String title, String description, String customContentString)` de votre récepteur de diffusion sera appelée chaque fois qu’un utilisateur clique sur un message de notification push entrant. Le paramètre `customContentString` contient les compléments au format JSON. Tous les messages de Braze contiendront les deux paires clé-valeur suivantes :

  ```json
  {
    "source": "Appboy",
    "cid": "your-campaign-Id"
  }
  ```

Chaque fois que `onNotificationClicked` est appelé, votre récepteur Baidu doit envoyer une [intention][44] à votre application contenant `customContentString`. Votre application enregistrera le clic sur Braze en utilisant le `customContentString`.

L’exemple de code suivant transmet `customContentString` à Braze et enregistre un clic :

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
BrazeNotificationUtils.logBaiduNotificationClick(context, customContentString)
```

{% endtab %}
{% endtabs %}

## Étape 6 : Compléments

En plus des clés réservées utilisées par Braze, le paramètre `customContentString` contiendra également toutes les paires clé-valeur personnalisées définies par l’utilisateur. Pour extraire vos paires clé-valeur, enveloppez `customContentString` dans un objet JSONObject et récupérez vos compléments :

{% tabs %}
{% tab JAVA %}

```java
try {
  JSONObject myExtras = new JSONObject(customContentString);
  String myValue = myExtras.optString("my_key", null);
} catch (Exception e) {
  Log.e(TAG, "Caught an exception processing customContentString");
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
try {
  val myExtras = JSONObject(customContentString)
  val myValue = myExtras.optString("my_key", null)
} catch (e: Exception) {
  Log.e(TAG, "Caught an exception processing customContentString", e)
}
```

{% endtab %}
{% endtabs %}

## Étape 7 : Configurer les clés Baidu

Vous devez saisir votre clé API Baidu et votre clé secrète Baidu dans le tableau de bord de Braze. Les deux clés sont disponibles à partir de la console d’application Baidu.

Sur la page **Gérer les paramètres**, sélectionnez votre application Android China et entrez votre clé API Baidu et votre clé secrète Baidu dans la section des notifications push.

![][19]{: style="max-width:80%;"}

## Ressources complémentaires

- [Portail Baidu][7]
- [Portail des développeurs de Baidu][36]
- [Portail du projet Baidu][11]
- [Portail du SDK des notifications push Baidu][40]
- [Documentation sur l'intégration de Baidu][43]

[7]: https://www.baidu.com/
[10]: {% image_buster /assets/img_archive/baidu_project.png %}
Il y a [11]: http://developer.baidu.com/console#app/project
[13]: {% image_buster /assets/img_archive/baidu_dev_reg.png %}
[14]: {% image_buster /assets/img_archive/baidu_app_console.png %}
[17]: {% image_buster /assets/img_archive/baidu_signup.png %}
[19]: {% image_buster /assets/img_archive/baidu_api_key.png %} "APIKey"
[26]: {% image_buster /assets/img_archive/baidu_app_name.png %}
[29]: {% image_buster /assets/img_archive/baidu_continue.png %}
[33]: {% image_buster /assets/img_archive/baidu_portal.png %}
[34]: {% image_buster /assets/img_archive/baidu_email.png %}
[35]: {% image_buster /assets/img_archive/baidu_text.png %}
Il y a [36]: http://developer.baidu.com/
[37]: {% image_buster /assets/img_archive/baidu_dev_portal.png %}
[38]: {% image_buster /assets/img_archive/baidu_login_dialog.png %}
[39]: {% image_buster /assets/img_archive/baidu_configure_cloud.png %}
Il y a [40]: http://developer.baidu.com/wiki/index.php?title=docs/cplat/push/sdk/clientsdk
[41]: {% image_buster /assets/img_archive/baidu_sdk.png %}
Il y a [43]: http://developer.baidu.com/wiki/index.php?title=docs/frontia/guide-android/overview
Il y a [44]: http://developer.android.com/reference/android/content/Intent.html
