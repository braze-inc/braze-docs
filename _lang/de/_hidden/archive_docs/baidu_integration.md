---
nav_title: Baidu-Integration
article_title: Baidu Push-Benachrichtigung Integration für Android
platform: Android
permalink: /baidu_integration/
description: "Dieser Artikel zeigt Ihnen, wie Sie eine Baidu Android Integration einrichten."
hidden: true
---
# Baidu-Integration
{% multi_lang_include archive/baidu_deprecation.md %}

Braze kann Push-Benachrichtigungen an Android Geräte über [Baidu Cloud Push]({% image_buster /assets/img_archive/baidu_app_console.png %}) senden. Beachten Sie, dass Sie Ihre Apps **nicht** über den Baidu App Store vertreiben müssen, wenn Sie Baidu Cloud Push verwenden.

## Schritt 1: Erstellen Sie ein Baidu-Konto

Um ein Baidu-Konto zu erstellen, besuchen Sie das [Baidu-Portal](https://www.baidu.com/) und klicken Sie auf **登录** (Anmelden), um einen Dialog aufzurufen, mit dem Sie sich anmelden oder ein neues Konto erstellen können.

![]({% image_buster /assets/img_archive/baidu_portal.png %})

Um ein neues Konto zu erstellen, klicken Sie unten im Anmelde-Dialog auf **立即注册** (neues Konto).

![]({% image_buster /assets/img_archive/baidu_login_dialog.png %}){: style="max-width:70%;"}

Geben Sie Ihren Benutzernamen, Ihre Telefonnummer und Ihr Passwort auf der Seite zur Kontoerstellung ein. Klicken Sie dann auf den Button Bestätigungscode erhalten. Sie erhalten nun eine SMS Nachricht von Baidu mit einem Verifizierungscode. Akzeptieren Sie abschließend die Lizenzvereinbarung und klicken Sie auf **注册** (Konto erstellen), um sich zu registrieren. Wenn diese Einrichtungsschritte fehlschlagen, versuchen Sie, sich über die Baidu Cloud-Anmeldung zu registrieren, wie in diesem [Artikel zur Anmeldung](https://www.adchina.io/how-to-open-a-baidu-account-outside-china/) beschrieben.

![Baidu Registrierung Seite]({% image_buster /assets/img_archive/baidu_signup.png %}){: style="max-width:80%;"}

## Schritt 2: Registrieren Sie sich als Baidu Entwickler:in

Als nächstes müssen Sie sich als Baidu Entwickler:in registrieren. Besuchen Sie zunächst das [Baidu-Entwickler:in-Portal](http://developer.baidu.com/) und wählen Sie **注册** (Neues Entwicklerkonto erstellen), um mit der Registrierung zu beginnen.

![]({% image_buster /assets/img_archive/baidu_dev_portal.png %})

Auf der Registrierungsseite wählen Sie Ihren Kontotyp (个人 für Privatpersonen, 公司 für Unternehmen) und den Typ des Entwicklers:in (der Entwickler ist bereits vorausgewählt und in den meisten Fällen korrekt). Geben Sie Ihren Namen, einen Lebenslauf und Ihre Telefonnummer mit dem Code des Landes in Klammern ein (z.B. (1)xxxxxxxxxx). Klicken Sie auf **发送验证码** (Verifizierungscode senden) und geben Sie den Verifizierungscode in der folgenden Zeile ein. Die nächsten beiden Felder, Website des Entwicklers und Logo des Entwicklers, sind optional. Akzeptieren Sie die Lizenzvereinbarung und klicken Sie auf **提交** (Abschicken), um sie abzuschicken. Sie haben jetzt ein Baidu Entwickler:in-Konto.

![]({% image_buster /assets/img_archive/baidu_dev_reg.png %})

## Schritt 3: Registrieren Sie Ihre Anwendung bei Baidu

Um Ihre Anwendung bei Baidu zu registrieren, besuchen Sie das [Baidu-Projektportal](http://developer.baidu.com/console#app/project) und klicken Sie auf **创建工程** (Projekt erstellen).

![]({% image_buster /assets/img_archive/baidu_project.png %})

Geben Sie auf der folgenden Seite den Namen Ihrer Anwendung ein. Die folgenden beiden Kontrollkästchen dienen zur Aktivierung zusätzlicher Baidu Dienste. In den meisten Fällen sollten Sie diese leer lassen.

![]({% image_buster /assets/img_archive/baidu_app_name.png %})

Nach der Einrichtung Ihrer Anwendung werden Sie zu einer Konsole weitergeleitet, die Informationen über Ihre App anzeigt, darunter auch den API-Schlüssel. Navigieren Sie dann in der Seitenleiste zu **云推送** (Cloud Push). Klicken Sie auf der folgenden Seite auf **推送设置** (Push einrichten).

![]({% image_buster /assets/img_archive/baidu_app_console.png %})

![]({% image_buster /assets/img_archive/baidu_continue.png %})

Geben Sie auf der folgenden Seite den Namen Ihres App-Pakets ein (z. B. `com.braze.sample`) und legen Sie fest, ob und wie lange (in Stunden) Nachrichten zwischengespeichert werden sollen. Damit wird Baidu mitgeteilt, wie lange es noch versuchen soll, Nachrichten an Nutzer:innen zu senden, die offline sind. Klicken Sie auf **保存设置** (Einstellungen speichern), um zu speichern.

![]({% image_buster /assets/img_archive/baidu_configure_cloud.png %})

## Schritt 4: Baidu zu Ihrer Anwendung hinzufügen

Besuchen Sie das [Baidu Push SDK-Portal](http://developer.baidu.com/wiki/index.php?title=docs/cplat/push/sdk/clientsdk) und laden Sie das neueste Baidu Cloud Push SDK für Android herunter.

![]({% image_buster /assets/img_archive/baidu_sdk.png %})

Im SDK finden Sie das Push-Dienst-Jar und die plattformspezifischen nativen Bibliotheken. Integrieren Sie diese in Ihr Projekt. Stellen Sie sicher, dass Ihre App die höchste SDK-Version targetet, die Baidu derzeit unterstützt. Diese Dokumentation ist aktuell für Baidu Cloud Push Android SDK Version `4.6.2.38`.

Fügen Sie die folgenden erforderlichen Baidu-Berechtigungen zur `AndroidManifest.xml` Ihrer Anwendung hinzu.

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

Die Bibliothek von Baidu enthält Broadcast-Empfänger, die eingehende Push-Nachrichten verarbeiten. Deklarieren Sie die internen Baidu-Empfänger in Ihrer Anwendung `AndroidManifest.xml` innerhalb des Elements `<application>`.

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

Außerdem müssen Sie einen Broadcast-Empfänger erstellen, der auf eingehende Push-Nachrichten und -Benachrichtigungen wartet. Deklarieren Sie Ihren Empfänger in Ihrer Anwendung `AndroidManifest.xml` innerhalb des Elements `<application>`. Dieser Empfänger muss `com.baidu.android.pushservice.PushMessageReceiver` erweitern und Methoden implementieren, die Ereignis-Updates vom Baidu Push-Dienst empfangen.

```xml
      <receiver android:name=".MyPushMessageReceiver">
        <intent-filter>
          <action android:name="com.baidu.android.pushservice.action.MESSAGE"/>
          <action android:name="com.baidu.android.pushservice.action.RECEIVE"/>
          <action android:name="com.baidu.android.pushservice.action.notification.CLICK"/>
        </intent-filter>
      </receiver>
```

Fügen Sie in der Methode `onCreate()` Ihrer Hauptaktivität die folgende Zeile ein, mit der Sie Ihre Anwendung bei Baidu registrieren und auf eingehende Push-Nachrichten warten können. Stellen Sie sicher, dass Sie "Your-API-Key" durch den Baidu API-Schlüssel Ihres Projekts ersetzen.

```
PushManager.startWork(getApplicationContext(), PushConstants.LOGIN_TYPE_API_KEY, "Your-API-Key");
```

Schließlich müssen Sie Ihre Nutzer:innen bei Braze registrieren. In der `onBind()` Methode des Baidu Broadcast-Empfängers, den Sie in diesem Schritt erstellt haben, senden Sie die `channelId` mit `Braze.registerAppboyPushMessages(channelId)` an Braze.

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

## Schritt 5: Registrierung von Push-Öffnungen

Baidu unterstützt den Versand zusätzlicher Schlüssel-Wert-Paare mit Push Nachrichten im JSON-Format. Die Methode `public void onNotificationClicked(Context context, String title, String description, String customContentString)` Ihres Broadcast-Empfängers wird immer dann aufgerufen, wenn ein Nutzer:innen auf eine eingehende Push Nachricht klickt. Der Parameter `customContentString` enthält die Extras im JSON-Format. Alle Nachrichten von Braze enthalten die folgenden beiden Schlüssel-Wert-Paare:

  ```json
  {
    "source": "Appboy",
    "cid": "your-campaign-Id"
  }
  ```

Immer wenn `onNotificationClicked` von Ihrem Baidu-Empfänger aufgerufen wird, sollte Ihr Empfänger eine [Absicht](http://developer.android.com/reference/android/content/Intent.html) an Ihre Anwendung senden, die `customContentString` enthält. Ihre Anwendung protokolliert den Klick auf Braze mit Hilfe der `customContentString`.

Der folgende Beispielcode übergibt `customContentString` an Braze und protokolliert einen Klick:

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

## Schritt 6: Extras

Neben den reservierten Schlüsseln, die von Braze verwendet werden, enthält der Parameter `customContentString` auch alle vom Nutzer:innen angepassten Schlüssel-Wert-Paare. Um Ihre Schlüssel-Wert-Paare zu extrahieren, verpacken Sie `customContentString` in ein JSONObject und rufen Sie Ihre Extras ab:

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

## Schritt 7: Baidu-Schlüssel einrichten

Sie müssen Ihren Baidu API-Schlüssel und Ihren Baidu Secret Key in das Braze-Dashboard eingeben. Beide Tasten sind in der Baidu-Anwendungskonsole verfügbar.

Wählen Sie auf der Seite **Einstellungen verwalten** Ihre Android China App aus und geben Sie im Bereich Push-Benachrichtigungen Ihren Baidu API-Schlüssel und Baidu Secret Key ein.

![]({% image_buster /assets/img_archive/baidu_api_key.png %} "APIKey"){: style="max-width:80%;"}

## Zusätzliche Ressourcen

- [Baidu-Portal](https://www.baidu.com/)
- [Baidu Entwickler:in Portal](http://developer.baidu.com/)
- [Baidu Projekt-Portal](http://developer.baidu.com/console#app/project)
- [Baidu Push SDK Portal](http://developer.baidu.com/wiki/index.php?title=docs/cplat/push/sdk/clientsdk)
- [Dokumente zur Baidu Integration](http://developer.baidu.com/wiki/index.php?title=docs/frontia/guide-android/overview)

