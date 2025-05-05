---
nav_title: Huawei-Integration
article_title: Huawei Push-Integration für Android
platform: Android
page_order: 9
description: "Dieser Artikel beschreibt, wie Sie eine Huawei-Android-Integration einrichten."
channel:
  - push

---

# Huawei Push-Integration

> Neuere von [Huawei](https://huaweimobileservices.com/) hergestellte Telefone sind mit Huawei Mobile Serviceleistungen; Dienste (HMS) ausgestattet - einem Dienst, der Push anstelle von Googles Firebase Cloud Messaging (FCM) zustellt.<br><br>In dieser Anleitung erfahren Sie, wie Sie Ihre Huawei Android Integration einrichten, um Push über Braze zu senden und alle bestehenden Features von Braze zu nutzen, einschließlich Segmentierung, Analytics, Canvas und mehr!

## Schritt 1: Registrieren Sie sich für ein Huawei-Entwickler:in-Konto

Bevor Sie beginnen, müssen Sie sich registrieren und ein [Huawei Entwicklerkonto](https://developer.huawei.com/consumer/en/console) einrichten. Gehen Sie in Ihrem Huawei-Konto zu **Meine Projekte > Projekteinstellungen > App-Informationen** und notieren Sie sich die `App ID` und `App secret`.

![]({% image_buster /assets/img/huawei/huawei-credentials.png %})

## Schritt 2: Erstellen Sie eine neue Huawei App im Braze-Dashboard

Gehen Sie im Braze-Dashboard zu **App-Einstellungen**, die unter der Navigation **Einstellungen** aufgeführt sind.

Klicken Sie auf **\+ App hinzufügen**, geben Sie einen Namen an (z.B. My Huawei App), wählen Sie `Android` als Plattform.

![]({% image_buster /assets/img/huawei/huawei-create-app.png %}){: style="max-width:60%;"}

Sobald Sie Ihre neue Braze App erstellt haben, suchen Sie die Einstellungen für Push-Benachrichtigungen und wählen Sie `Huawei` als Push-Anbieter aus. Geben Sie als nächstes Ihre `Huawei Client Secret` und `Huawei App ID` an.

![]({% image_buster /assets/img/huawei/huawei-dashboard-credentials.png %})

## Schritt 3: Integrieren Sie das Huawei-Messaging-SDK in Ihre App

Huawei hat ein [Android-Integrations-Codelab](https://developer.huawei.com/consumer/en/codelab/HMSPushKit/index.html) zur Verfügung gestellt, das die Integration des Huawei-Messaging-Dienstes in Ihre Anwendung beschreibt. Folgen Sie diesen Schritten, um loszulegen.

Nachdem Sie das Codelab abgeschlossen haben, müssen Sie einen angepassten [Huawei Serviceleistungen; Dienste](https://developer.huawei.com/consumer/en/doc/development/HMS-References/push-HmsMessageService-cls) erstellen, um Push-Token zu erhalten und Nachrichten an das Braze SDK weiterzuleiten.

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

Nachdem Sie Ihren angepassten Push-Dienst hinzugefügt haben, fügen Sie Folgendes zu Ihrem `AndroidManifest.xml` hinzu:

```xml
<service
  android:name="package.of.your.CustomPushService"
  android:exported="false">
  <intent-filter>
    <action android:name="com.huawei.push.action.MESSAGING_EVENT" />
  </intent-filter>
</service>
```

## Schritt 4: Senden Sie einen Huawei-Push

Zu diesem Zeitpunkt haben Sie im Braze-Dashboard eine neue Huawei Android App erstellt, diese mit Ihren Zugangsdaten als Huawei-Entwickler:in konfiguriert und die SDKs von Braze und Huawei in Ihre App integriert.

Als Nächstes können wir die Integration testen, indem wir eine neue Push-Kampagne in Braze ausprobieren.

### Erstellen Sie eine neue Kampagne mit Push-Benachrichtigungen

Erstellen Sie auf der Seite **Kampagnen** eine neue Kampagne und wählen Sie **Push-Benachrichtigung** als Typ Ihrer Nachricht.

Nachdem Sie Ihre Kampagne benannt haben, wählen Sie **Android Push** als Push-Plattform.

![Der Composer für die Erstellung von Kampagnen, der die verfügbaren Push-Plattformen anzeigt.]({% image_buster /assets/img/huawei/huawei-test-push-platforms.png %})

Als nächstes stellen Sie Ihre Push-Kampagne mit einem Titel und einer Nachricht zusammen.

### Senden Sie einen Test-Push

Geben Sie auf dem Tab **Test** Ihre Nutzer:innen ID ein, die Sie in Ihrer App mit der [Methode`changeUser(USER_ID_STRING)` ]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids/#assigning-a-user-id) festgelegt haben, und klicken Sie auf **Test senden**, um einen Push zu senden.

![Der Tab "Test" im Composer zur Erstellung von Kampagnen zeigt Ihnen, dass Sie eine Nachricht an sich selbst senden können, indem Sie Ihre Nutzer-ID in das Feld "Einzelne Nutzer hinzufügen" eingeben.]({% image_buster /assets/img/huawei/huawei-test-send.png %})

Zu diesem Zeitpunkt sollten Sie eine Push-Benachrichtigung von Braze auf Ihrem Huawei (HMS) Gerät erhalten.

### Segmentierung von Huawei einrichten (optional)

Da Ihre Huawei App im Braze-Dashboard auf der Android-Push-Plattform aufbaut, haben Sie die Flexibilität, Push an alle Android-Benutzer zu senden (Firebase Cloud Messaging und Huawei Mobile Serviceleistungen; Dienste), oder Sie können die Zielgruppen Ihrer Kampagne auf bestimmte Apps segmentieren.

Um Push nur an Huawei Apps zu senden, [erstellen Sie ein neues Segment]({{ site.baseurl }}/user_guide/engagement_tools/segments/creating_a_segment/#step-3-choose-your-app-or-platform) und wählen Sie Ihre Huawei App im Bereich **Apps** aus.

![]({% image_buster /assets/img/huawei/huawei-segmentation.png %})

Wenn Sie denselben Push an alle Android-Push-Anbieter senden möchten, können Sie die App, die an alle im aktuellen Workspace konfigurierten Android-Apps gesendet werden soll, natürlich nicht angeben.

## Analytics

Sobald Ihre Kampagne gestartet ist, sehen Sie die Analytics für Ihre Kampagne oder Canvas für Android Push aggregiert. Weitere Informationen zu Android Push Analytics und Einstellungen finden Sie in unserer [Anleitung für Nutzer:innen]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_reporting/).

