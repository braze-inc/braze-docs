{% multi_lang_include developer_guide/prerequisites/cordova.md %} Nachdem Sie das SDK integriert haben, ist die grundlegende Funktionalität der Push-Benachrichtigung standardmäßig aktiviert. Um [Rich-Push-Benachrichtigungen]({{site.baseurl}}/developer_guide/push_notifications/rich/?sdktab=cordova) und [Push-Storys]({{site.baseurl}}/developer_guide/push_notifications/push_stories/?sdktab=cordova) zu verwenden, müssen Sie sie einzeln einrichten.

{% alert warning %}
Jedes Mal, wenn Sie Ihre Cordova Plugins hinzufügen, entfernen oder aktualisieren, überschreibt Cordova das Podfile im Xcode Projekt Ihrer iOS App. Das bedeutet, dass Sie diese Features jedes Mal neu einrichten müssen, wenn Sie Ihre Cordova Plugins ändern.
{% endalert %}

## Deaktivieren grundlegender Push-Benachrichtigungen (nur iOS)

Nachdem Sie das Braze Cordova SDK für iOS integriert haben, ist die grundlegende Funktionalität der Push-Benachrichtigung standardmäßig aktiviert. Um diese Funktion in Ihrer iOS App zu deaktivieren, fügen Sie Folgendes zu Ihrer `config.xml` Datei hinzu. Weitere Informationen finden Sie unter [Optionale Konfigurationen]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=cordova#optional).

```xml
<platform name="ios">
    <preference name="com.braze.ios_disable_automatic_push_registration" value="NO" />
    <preference name="com.braze.ios_disable_automatic_push_handling" value="NO" />
</platform>
```
