{% multi_lang_include developer_guide/prerequisites/web.md %} Sie müssen auch [Push-Benachrichtigungen]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=web) für das Internet SDK [einrichten]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=web). Beachten Sie, dass Sie Push-Benachrichtigungen nur an iOS- und iPadOS-Nutzer:innen senden können, die [Safari v16.4](https://developer.apple.com/documentation/safari-release-notes/safari-16_4-release-notes) oder höher verwenden.

## Safari Push für Mobiltelefone einrichten

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

Beliebte Browser (wie Safari, Chrome, FireFox und Edge) unterstützen in ihren neueren Versionen alle Web-Push-Benachrichtigungen. Um die Push-Erlaubnis unter iOS oder iPadOS anzufordern, muss Ihre Website zum Startbildschirm des Nutzers:innen hinzugefügt werden, indem Sie **Freigeben an** > **Zum Startbildschirm hinzufügen** auswählen. Mit [Add to Homescreen](https://support.apple.com/guide/iphone/bookmark-favorite-webpages-iph42ab2f3a7/ios#iph4f9a47bbc) können Nutzer:innen Ihre Website mit einem Lesezeichen versehen, so dass Ihr Symbol auf ihrem wertvollen Home Screen erscheint.

![Ein iPhone mit Optionen zum Setzen von Lesezeichen für eine Website und zum Speichern auf dem Startbildschirm]({% image_buster /assets/img/push_implementation_guide/add-to-homescreen.png %}){: style="max-width:40%"}

### Schritt 5: Zeigen Sie die native Push-Eingabeaufforderung {#push-prompt} an.
Nachdem die App zu Ihrem Startbildschirm hinzugefügt wurde, können Sie jetzt die Push-Erlaubnis anfragen, wenn der Nutzer:innen eine Aktion ausführt (z.B. auf einen Button klickt). Dies kann mit der [`requestPushPermission`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#requestpushpermission) Methode oder mit einer [In-App-Nachricht ohne Code-Push-Primer]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/).

{% alert note %}
Nachdem Sie die Aufforderung akzeptiert oder abgelehnt haben, müssen Sie die Website auf Ihrem Startbildschirm löschen und neu installieren, um die Aufforderung wieder anzeigen zu können.
{% endalert %}

![Eine Push-Abfrage mit der Aufforderung, Push-Benachrichtigungen zuzulassen oder nicht zuzulassen]({% image_buster /assets/img/push_implementation_guide/safari-mobile-push-prompt.png %}){: style="max-width:40%"}

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
