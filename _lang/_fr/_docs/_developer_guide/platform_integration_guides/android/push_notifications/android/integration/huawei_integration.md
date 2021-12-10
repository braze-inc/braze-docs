---
nav_title: Intégration de Huawei
article_title: Intégration de Huawei Push pour Android
platform: Android
page_order: 9
description: "Cet article couvre la façon de mettre en place une intégration Huawei Android."
channel:
  - Pousser
---

# Intégration de Huawei

Les nouveaux téléphones fabriqués par [Huawei][1] sont équipés de Huawei Mobile Services (HMS) - un service utilisé pour fournir des messages push _au lieu de_ Messagerie Firebase Cloud (FCM) de Google.

Ce guide vous montrera comment configurer votre intégration à Huawei Android afin d'envoyer des push via Braze, et profitez de toutes les fonctionnalités de Braze existantes, y compris la segmentation, l'analytique, la toile, et plus!

## Étape 1 : Inscrivez-vous pour un compte développeur Huawei

Avant de commencer, vous devrez vous inscrire et configurer un compte de développeur [Huawei][2].

Dans votre compte Huawei, allez à **Mes Projets** > **Paramètres du Projet** > **Informations de l'application**, et prenez note du `ID de l'application` et du `secret de l'application`.

!\[Huawei App Credentials\]\[3\]

Dans la prochaine étape, vous entrerez ces identifiants dans le tableau de bord de Braze qui permettra à Braze d'envoyer push au nom de votre application Huawei.

## Étape 2 : Créez une nouvelle application Huawei dans le tableau de bord Braze

Dans le tableau de bord de Braze, allez à **Gérer les paramètres**, listé sous la navigation **Paramètres**.

Cliquez sur **+ Ajouter une application**, donnez un nom (i.e. Mon application Huawei), sélectionnez `Android` comme Plateforme, et choisissez `Huawei (HMS)` comme Fournisseur Push.

!\[Créer l'application Huawei dans le tableau de bord de Braze\]\[4\]

Une fois que votre nouvelle application Braze a été créée, vous serez affiché une `clé API`, et une section pour **Paramètres de notification Push** où vous entrerez vos identifiants Huawei de l'étape précédente.

## Étape 3 : Entrez les identifiants Huawei dans le tableau de bord Braze

Utilisation des identifiants de votre compte Huawei Developer, entrez dans l'App ID `Huawei` et `Huawei App Secret` dans votre application Huawei Braze nouvellement créée. Lorsque vous avez terminé, enregistrez vos modifications.

!\[Identifiants du tableau de bord Huawei\]\[12\]

## Étape 4 : Intégrez le SDK de messagerie Huawei dans votre application

Huawei a fourni un [code d'intégration Android][13] détaillant comment intégrer le service de messagerie Huawei dans votre application.

Après avoir complété ces étapes, vous devrez créer un [service de messagerie Huawei][14] personnalisé pour obtenir des jetons push et des messages vers le SDK de Braze.

{% tabs %}
{% tab JAVA %}

```java
de classe publique CustomPushService étend HmsMessageService {
  @Override
  public void onNewToken(String token) {
    super. nNewToken(jeton);
    Brésil. etInstance(this.getApplicationContext()).registerAppboyPushMessages(token);
  }

  

 @Override
  public void onMessageReceived(RemoteMessage remoteMessage) {
    super. nMessageReceived(remoteMessage);
    if (BrazeHuaweiPushHandler.handleHmsRemoteMessageData(this.getApplicationContext(), remoteMessage. etDataOfMap())) {
      // Braze a géré la notification push Huawei
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
    Braze.getInstance(applicationContext).registerAppboyPushMessages(token!!)
  }

  outrepasser le fun onMessageReceived(hmsRemoteMessage: RemoteMessage?) {
    super.onMessageReceived(hmsRemoteMessage)
    if (BrazeHuaweiPushHandler.handleHmsRemoteMessageData(applicationContext, hmsRemoteMessage?.dataOfMap)) {
      // Braze a géré la notification Huawei push
    }
  }
}
```

{% endtab %}
{% endtabs %}

Après avoir ajouté votre service push personnalisé, ajoutez ce qui suit à votre `AndroidManifest.xml`.

```xml
<service
  android:name="package.of.your.CustomPushService"
  android:exported="false">
  <intent-filter>
    <action android:name="com.huawei.push.action.MESSAGING_EVENT" />
  </intent-filter>
</service>
```

## Étape 5 : Envoyer une poussée Huawei

À ce stade, vous avez créé une nouvelle application Android Huawei dans le tableau de bord de Braze, l'a configuré avec vos identifiants Huawei Developer, et ont intégré les SDK Braze et Huawei dans votre application.

Ensuite, nous pouvons tester l'intégration en testant une nouvelle campagne Push au Brésil.

### Créer une nouvelle campagne de notification push

Dans la page **Campagnes** , créez une nouvelle campagne et choisissez **Notification** comme type de message.

Après que vous ayez nommé votre campagne, choisissez **Android Push** comme plate-forme Push .

!\[Choisissez un canal de diffusion Android\]\[5\]

Ensuite, composez votre campagne de push avec un titre et un message.

!\[Composer un message push Huawei sur Android\]\[6\]

### Envoyer un test push

Dans l’onglet **Tester** entrez votre identifiant d'utilisateur que vous avez défini dans votre application en utilisant la méthode [`changeUser(USER_ID_STRING)`][9], et cliquez sur **Envoyer le test** pour envoyer la poussée de test.

!\[Huawei Test Envoyer\]\[7\]

À ce stade, vous devriez recevoir une notification de test push sur votre appareil Huawei (HMS) de Brasil !

### Mise en place de la segmentation Huawei (facultatif)

Depuis que votre application Huawei dans le tableau de bord de Braze est construite sur la plateforme Android Push, vous avez la flexibilité d'envoyer des messages push à tous les utilisateurs d'Android (Firebase Cloud Messaging et Huawei Mobile Services), ou vous pouvez choisir de segmenter le public de votre campagne vers des applications spécifiques.

Pour envoyer des push à seulement des applications Huawei, \[créez un nouveau Segment\]\[15\] et sélectionnez votre application Huawei dans la section "Apps".

!\[Segmentation\]\[8\]

Bien sûr, si vous voulez envoyer le même push à tous les fournisseurs de push Android, vous pouvez choisir de ne pas spécifier l'application qui sera envoyée à toutes les applications Android configurées dans le groupe d'applications actuel.

## Analyses

Une fois votre campagne lancée, vous verrez des analyses pour votre campagne ou Canvas agrégés pour Android Push. Pour plus d'informations sur les analyses et les paramètres de Push d'Android, consultez notre [Guide de l'utilisateur pour Pousser][10].
[3]: {% image_buster /assets/img/huawei/huawei-credentials.png %} [4]: {% image_buster /assets/img/huawei/huawei-create-app. ng %} [5]: {% image_buster /assets/img/huawei/huawei-test-push-platforms.png %} [6]: {% image_buster /assets/img/huawei/huawei-test-push-composer. ng %} [7]: {% image_buster /assets/img/huawei/huawei-test-send.png %} [8]: {% image_buster /assets/img/huawei/huawei-segmentation. ng %} [12]: {% image_buster /assets/img/huawei/huawei-dashboard-credentials.png %} [15]: {{ site.baseurl }}/user_guide/engagement_tools/segments/creating_a_segment/#step-3-choose-your-app-or-platform

[1]: https://huaweimobileservices.com/
[2]: https://developer.huawei.com/consumer/en/console
[9]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids/#assigning-a-user-id
[10]: {{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#results-data-push
[13]: https://developer.huawei.com/consumer/en/codelab/HMSPushKit/index.html
[14]: https://developer.huawei.com/consumer/en/doc/development/HMS-References/push-HmsMessageService-cls
