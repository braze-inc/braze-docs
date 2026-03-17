{% multi_lang_include developer_guide/prerequisites/web.md %} Bitte beachten Sie, dass Sie [Push-Benachrichtigungen]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=web) für das Web-SDK [einrichten]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=web) müssen. Bitte beachten Sie, dass Sie Push-Benachrichtigungen nur an iOS- und iPadOS-Nutzer:innen senden können, die [Safari v16.4](https://developer.apple.com/documentation/safari-release-notes/safari-16_4-release-notes) oder höher verwenden.

## Einrichtung von Safari Push für Mobilgeräte

### Schritt 1: Erstellen Sie eine Manifestdatei {#manifest}

Ein [Internet-Anwendungsmanifest](https://developer.mozilla.org/en-US/docs/Web/Manifest) ist eine JSON-Datei, die steuert, wie Ihre Website bei der Installation auf dem Startbildschirm eines Nutzers:innen dargestellt wird.

Sie können zum Beispiel die Hintergrundfarbe und das Symbol festlegen, das der [App Switcher](https://support.apple.com/en-us/HT202070) verwendet, ob er im Vollbildmodus gerendert wird, um einer nativen App zu ähneln, oder ob die App im Hoch- oder Querformat geöffnet werden soll.

Erstellen Sie eine neue Datei `manifest.json` im Stammverzeichnis Ihrer Website mit den folgenden Pflichtfeldern. 

```json
{
  "name": "your app name",
  "short_name": "your app name",
  "display": "fullscreen",
  "icons": [{
    "src": "favicon.ico",
    "sizes": "128x128",
  }]
}
```

Die vollständige Liste der unterstützten Felder finden Sie [hier](https://developer.mozilla.org/en-US/docs/Web/Manifest).

### Schritt 2: Verknüpfen Sie die Manifestdatei {#manifest-link}

Fügen Sie das folgende `<link>`-Tag in das `<head>`-Element Ihrer Website ein, das auf den Speicherort der Manifestdatei verweist.

```html
<link rel="manifest" href="/manifest.json" />
```

### Schritt 3: Fügen Sie ein Service-Teammitglied {#service-worker} hinzu

Ihre Website muss über eine Service-Teammitglied-Datei verfügen, die die Service-Teammitglieder-Bibliothek von Braze importiert, wie in unserer [Anleitung zur Web-Push Integration]({{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/integration/#step-1-configure-your-sites-service-worker) beschrieben.

### Schritt 4: Zum Startbildschirm hinzufügen {#add-to-homescreen}

Beliebte Webbrowser (wie Safari, Chrome, Firefox und Edge) unterstützen in ihren neueren Versionen alle Web-Push-Benachrichtigungen. Um Push-Benachrichtigungen auf iOS oder iPadOS zu aktivieren, muss Ihre Website zum Startbildschirm der Nutzer:innen hinzugefügt werden, indem **„Teilen“** > **„Zum Startbildschirm hinzufügen“** ausgewählt wird. [Mit „Zum Startbildschirm hinzufügen“](https://support.apple.com/guide/iphone/bookmark-favorite-webpages-iph42ab2f3a7/ios#iph4f9a47bbc) können Nutzer:innen Ihre Website mit einem Lesezeichen versehen und Ihr Symbol auf ihrem wertvollen Startbildschirm speichern.

![Ein iPhone, das Optionen zum Setzen eines Lesezeichens für eine Website und zum Speichern auf dem Startbildschirm anzeigt.]({% image_buster /assets/img/push_implementation_guide/add-to-homescreen.png %}){: style="max-width:40%"}

### Schritt 5: Zeigen Sie die native Push-Eingabeaufforderung {#push-prompt} an.
Nachdem die App zu Ihrem Startbildschirm hinzugefügt wurde, können Sie nun eine Push-Berechtigung anfragen, wenn der Nutzer eine Aktion ausführt (z. B. auf einen Button klickt). Dies kann mit der [`requestPushPermission`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#requestpushpermission) Methode oder mit einer [In-App-Nachricht ohne Code-Push-Primer]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/).

{% alert note %}
Nachdem Sie die Aufforderung akzeptiert oder abgelehnt haben, müssen Sie die Website löschen und erneut auf Ihrem Startbildschirm installieren, um die Aufforderung erneut anzeigen zu können.
{% endalert %}

![Eine Push-Benachrichtigung, in der Sie gefragt werden, ob Sie Benachrichtigungen zulassen oder nicht zulassen möchten.]({% image_buster /assets/img/push_implementation_guide/safari-mobile-push-prompt.png %}){: style="max-width:40%"}

Zum Beispiel:

```typescript
import { requestPushPermission } from "@braze/web-sdk";

button.onclick = function(){
    requestPushPermission(() => {
        console.log(`User accepted push prompt`);
    }, (temporary) => {
        console.log(`User ${temporary ? "temporarily dismissed" : "permanently denied"} push prompt`);
    });
};
```

## Nächste Schritte

Als nächstes senden Sie sich selbst eine [Testnachricht]({{site.baseurl}}/developer_guide/in_app_messages/sending_test_messages/), um die Integration zu überprüfen. Nachdem Ihre Integration abgeschlossen ist, können Sie unsere [Push-Nachrichten ohne Code]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/) verwenden, um Ihre Opt-in-Raten zu optimieren.
