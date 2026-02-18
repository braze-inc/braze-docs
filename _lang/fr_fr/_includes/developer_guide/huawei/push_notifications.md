{% multi_lang_include developer_guide/prerequisites/android.md %}

## Mise en place des notifications push

Les téléphones récents fabriqués par [Huawei](https://huaweimobileservices.com/) sont équipés des services mobiles Huawei (HMS), un service utilisé pour envoyer des notifications push au lieu de recourir à Firebase Cloud Messaging (FCM) de Google.

### Étape 1 : Enregistrer un compte de développeur Huawei

Avant de commencer, vous devrez vous enregistrer et configurer un [compte de développeur Huawei](https://developer.huawei.com/consumer/en/console). Dans votre compte Huawei, allez dans **Mes projets > Paramètres du projet > Informations sur l'application**, et notez les adresses `App ID` et `App secret`.

![]({% image_buster /assets/img/huawei/huawei-credentials.png %})

### Étape 2 : Créer une nouvelle application Huawei dans le tableau de bord de Braze

Dans le tableau de bord de Braze, allez dans **Paramètres de l'application**, répertorié sous la navigation **Paramètres**.

Cliquez sur **\+ Ajouter une application**, fournissez un nom (comme Mon application Huawei) et sélectionnez `Android` comme plateforme.

![]({% image_buster /assets/img/huawei/huawei-create-app.png %}){: style="max-width:60%;"}

Une fois que votre nouvelle application Braze a été créée, trouvez les paramètres de notification push et sélectionnez `Huawei` en tant que fournisseur de notification push. Ensuite, fournissez votre `Huawei Client Secret` et `Huawei App ID`.

![]({% image_buster /assets/img/huawei/huawei-dashboard-credentials.png %})

### Étape 3 : Intégrer le SDK de messagerie Huawei à votre application

Huawei a fourni un [codelab d'intégration Android](https://developer.huawei.com/consumer/en/codelab/HMSPushKit/index.html) détaillant l'intégration du Huawei Messaging Service dans votre application. Suivez ces étapes pour commencer.

Après avoir terminé le codelab, vous devrez créer un [service de messages Huawei](https://developer.huawei.com/consumer/en/doc/development/HMS-References/push-HmsMessageService-cls) personnalisé pour obtenir des jetons de poussée et envoyer des messages au SDK de Braze.

{% tabs %}
{% tab JAVA %}

```java
public class CustomPushService extends HmsMessageService {
  @Override
  public void onNewToken(String token) {
    super.onNewToken(token);
    Braze.getInstance(this.getApplicationContext()).setRegisteredPushToken(token);
  }

  @Override
  public void onMessageReceived(RemoteMessage remoteMessage) {
    super.onMessageReceived(remoteMessage);
    if (BrazeHuaweiPushHandler.handleHmsRemoteMessageData(this.getApplicationContext(), remoteMessage.getDataOfMap())) {
      // Braze has handled the Huawei push notification
    }
  }
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
class CustomPushService: HmsMessageService() {
  override fun onNewToken(token: String?) {
    super.onNewToken(token)
    Braze.getInstance(applicationContext).setRegisteredPushToken(token!!)
  }

  override fun onMessageReceived(hmsRemoteMessage: RemoteMessage?) {
    super.onMessageReceived(hmsRemoteMessage)
    if (BrazeHuaweiPushHandler.handleHmsRemoteMessageData(applicationContext, hmsRemoteMessage?.dataOfMap)) {
      // Braze has handled the Huawei push notification
    }
  }
}
```

{% endtab %}
{% endtabs %}

Après avoir ajouté votre service de notification push personnalisé, ajoutez les éléments suivants à votre `AndroidManifest.xml` :

```xml
<service
  android:name="package.of.your.CustomPushService"
  android:exported="false">
  <intent-filter>
    <action android:name="com.huawei.push.action.MESSAGING_EVENT" />
  </intent-filter>
</service>
```

### Étape 4 : Gérer les notifications d'avant-plan

Par défaut, lorsqu'une notification push arrive alors que votre appli est au premier plan, Huawei l'affiche automatiquement. Pour que Braze traite la charge utile de la notification push (pour le suivi analytique, la gestion des liens profonds et le traitement personnalisé), achemine les données push entrantes vers Braze à l'intérieur de votre méthode `HmsMessageService.onMessageReceived`.

Lorsque vous appelez `BrazeHuaweiPushHandler.handleHmsRemoteMessageData`, Braze détermine si la charge utile est une notification push Braze et, le cas échéant, crée et affiche la notification. Pour plus d'informations, consultez la section [Gestion des notifications au premier plan]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android#handling-foreground-notifications) dans la documentation sur les notifications push d'Android.

Pour un exemple complet, consultez la [référence du gestionnaire Huawei](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.push/-braze-huawei-push-handler/index.html) dans la documentation du SDK Android de Braze.

### Étape 5 : Testez vos notifications push (facultatif)

À ce stade, vous avez créé une nouvelle application Android Huawei dans le tableau de bord de Braze, l’avez configurée avec vos identifiants de développeur Huawei et avez intégré les SDK Braze et Huawei dans votre application.

Ensuite, nous pouvons tester l’intégration en essayant une nouvelle campagne de notifications push dans Braze.

#### Étape 5.1 : Créer une nouvelle campagne de notifications push

Dans la page **Campagnes**, créez une nouvelle campagne et choisissez **Notification push** comme type de message.

Après avoir nommé votre campagne, choisissez **Android Push** comme plateforme de push.

![Le compositeur de création de campagne affichant les plateformes de poussée disponibles.]({% image_buster /assets/img/huawei/huawei-test-push-platforms.png %})

Ensuite, composez votre campagne de notification push avec un titre et un message.

#### Étape 5.2 : Envoyer un test de notification push

Dans l'onglet **Test**, entrez votre ID utilisateur, que vous avez défini dans votre application à l'aide de la [méthode`changeUser(USER_ID_STRING)` ]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids/#assigning-a-user-id), et cliquez sur **Envoyer le test** pour envoyer un push de test.

![L'onglet test du compositeur de création de campagne montre que vous pouvez vous envoyer un message test à vous-même en fournissant votre ID utilisateur et en le saisissant dans le champ "Ajouter des utilisateurs individuels".]({% image_buster /assets/img/huawei/huawei-test-send.png %})

À ce stade, vous devriez recevoir une notification push de test sur votre appareil Huawei (HMS) de la part de Braze.

#### Étape 5.3 : Mise en place de la segmentation Huawei (facultatif)

Étant donné que votre application Huawei dans le tableau de bord de Braze est basée sur la plateforme de notification push Android, vous avez la possibilité d’envoyer des notifications push à tous les utilisateurs Android (Firebase Cloud Messaging et Huawei Mobile Services), ou vous pouvez choisir de segmenter votre audience de campagne pour des applications spécifiques.

Pour envoyer des messages push uniquement aux applications Huawei, [créez un nouveau segment]({{ site.baseurl }}/user_guide/engagement_tools/segments/creating_a_segment/#step-3-choose-your-app-or-platform) et sélectionnez votre application Huawei dans la section **Apps**.

![]({% image_buster /assets/img/huawei/huawei-segmentation.png %})

Bien entendu, si vous souhaitez envoyer le même push à tous les fournisseurs de push Android, vous pouvez choisir de ne pas spécifier l'application qui enverra à toutes les applications Android configurées dans l'espace de travail actuel.
