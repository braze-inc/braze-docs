---
nav_title: Intégration Huawei
article_title: Intégration de notifications push Huawei pour Android
platform: Android
page_order: 9
description: "Cet article montre comment configurer une intégration Huawei pour Android."
channel:
  - Notification push

---

# Intégration de notification push Huawei

> Les téléphones plus récents fabriqués par [Huawei][1] sont équipés des services mobiles Huawei (HMS), un service utilisé pour envoyer des notifications push au lieu de la messagerie cloud Firebase (FCM) de Google.<br><br>Ce guide vous montrera comment configurer votre intégration Huawei pour Android pour envoyer des notifications push via Braze et profiter de toutes les fonctionnalités existantes de Braze, y compris la segmentation, l’analytique, Canvas, et bien plus encore !

## Étape 1 : Enregistrer un compte de développeur Huawei

Avant de commencer, vous devrez vous enregistrer et configurer un [compte de développeur Huawei][2]. Dans votre compte Huawei, allez à **My Projects > Project Settings > App Information (Mes projets > Paramètres du projet > Informations sur l’application)** et notez `App ID` et `App secret`.

![][3]

## Étape 2 : Créer une nouvelle application Huawei dans le tableau de bord de Braze

Dans le tableau de bord de Braze, allez à **Manage Settings** qui se trouvent dans **Settings (Paramètres)**.

Cliquez sur **+ Add App (+ Ajouter une application)**, fournissez un nom (par ex., Mon application Huawei) et sélectionnez `Android` comme étant la plateforme.

![][4]{: style="max-width:60%;"}

Une fois que votre nouvelle application Braze a été créée, trouvez les paramètres de notification push et sélectionnez `Huawei` en tant que fournisseur de notification push. Ensuite, fournissez votre `Huawei App ID` et `Huawei App Secret`.

![][12]

## Étape 3 : Intégrer le SDK de messagerie Huawei à votre application

Huawei a fourni un [laboratoire de code d’intégration Android][13] détaillant l’intégration du service de messagerie Huawei dans votre application. Suivez ces étapes pour commencer.

Après avoir terminé le laboratoire de code, vous devrez créer un [service de messages Huawei][14] personnalisé pour obtenir des jetons de notification push et transmettre des messages au SDK Braze.

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

## Étape 4 : Envoyer une notification push Huawei

À ce stade, vous avez créé une nouvelle application Android Huawei dans le tableau de bord de Braze, l’avez configurée avec vos identifiants de développeur Huawei et avez intégré les SDK Braze et Huawei dans votre application.

Ensuite, nous pouvons tester l’intégration en essayant une nouvelle campagne de notifications push dans Braze.

### Créer une nouvelle campagne de notifications push

Dans la page **Campaigns**, créez une nouvelle campagne et choisissez **Notification Push** comme type de message.

Après avoir donné un nom à votre campagne, choisissez **notification push Android** comme plateforme de notification.

![L’assistant de création de campagne affiche les plateformes de notification push disponibles.][5]

Ensuite, composez votre campagne de notification push avec un titre et un message.

### Envoyer un test de notification push

Dans l’onglet **Test (Test)** saisissez votre ID utilisateur, que vous avez défini dans votre application en utilisant la [`changeUser(USER_ID_STRING)`méthode ][9], et cliquez sur **Send Test (Envoyer un test)** pour envoyer un test de notification push.

![L’onglet Test de l’assistant de création de campagne montre que vous pouvez envoyer un message de test en fournissant votre ID utilisateur et en l’entrant dans le champ « Add Individual Users » (Ajouter des utilisateurs individuels).][7]

À ce stade, vous devriez recevoir une notification push de test sur votre appareil Huawei (HMS) de la part de Braze.

### Configurer la segmentation Huawei (facultatif)

Étant donné que votre application Huawei dans le tableau de bord de Braze est construite sur la plateforme de notification push Android, vous avez la possibilité d’envoyer des notifications push à tous les utilisateurs Android (Firebase Cloud Messaging et Huawei Mobile Services), ou vous pouvez choisir de segmenter votre audience de campagne pour des applications spécifiques.

Pour envoyer des notifications push uniquement vers les applications Huawei, [créez un nouveau segment][15] et sélectionnez votre application Huawei dans la section **Apps (Applications)**.

![][8]

Bien sûr, si vous souhaitez envoyer la même notification push à tous les fournisseurs de services de notifications Android, vous pouvez choisir de ne pas spécifier l’application, qui enverra donc à toutes les applications Android configurées dans le groupe d’apps actuel.

## Analytique

Une fois votre campagne lancée, vous verrez l’analytique de votre campagne ou agrégée par Canvas pour les notifications push Android. Consultez notre [guide de l’utilisateur de notification push][10] pour plus d’informations sur l’analytique et les paramètres des notifications push Android.

[1]: https://huaweimobileservices.com/
[2]: https://developer.huawei.com/consumer/en/console
[3]: {% image_buster /assets/img/huawei/huawei-credentials.png %}
[4]: {% image_buster /assets/img/huawei/huawei-create-app.png %}
[5]: {% image_buster /assets/img/huawei/huawei-test-push-platforms.png %}
[6]: {% image_buster /assets/img/huawei/huawei-test-push-composer.png %}
[7]: {% image_buster /assets/img/huawei/huawei-test-send.png %}
[8]: {% image_buster /assets/img/huawei/huawei-segmentation.png %}
[9]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids/#assigning-a-user-id
[10]: {{site.baseurl}}/user_guide/message_building_by_channel/push/push_reporting/
[12]: {% image_buster /assets/img/huawei/huawei-dashboard-credentials.png %}
[13]: https://developer.huawei.com/consumer/en/codelab/HMSPushKit/index.html
[14]: https://developer.huawei.com/consumer/en/doc/development/HMS-References/push-HmsMessageService-cls
[15]: {{ site.baseurl }}/user_guide/engagement_tools/segments/creating_a_segment/#step-3-choose-your-app-or-platform
