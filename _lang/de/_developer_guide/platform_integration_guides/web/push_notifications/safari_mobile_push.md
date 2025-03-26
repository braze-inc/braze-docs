---
nav_title: Safari Mobile Web-Push
article_title: Safari Mobile Web-Push
platform: Web
channel: push
page_order: 5
page_type: reference
description: "In diesem Referenzartikel erfahren Sie, wie Sie Web-Push in Safari auf iOS und iPad integrieren."
search_rank: 3
---

# Safari Mobile Web-Push (iOS und iPadOS)

> [Safari v16.4](https://developer.apple.com/documentation/safari-release-notes/safari-16_4-release-notes) unterstützt Mobile Web-Push, d. h. Sie können Nutzer jetzt mit Push-Benachrichtigungen auf iOS und iPadOS interaktiv kontaktieren.<br><br>Dieser Artikel führt Sie durch die notwendigen Schritte, um Mobile Push für Safari einzurichten.

## Schritte zur Integration

Lesen und befolgen Sie zunächst unsere [Standardanleitung zur Web-Push Integration]({{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/integration/). Die folgenden Schritte sind nur erforderlich, um Web-Push auf Safari für iOS und iPadOS zu unterstützen.

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

Im Gegensatz zu den großen Browsern wie Chrome und Firefox ist es bei Safari iOS/iPadOS nicht zulässig, eine Push-Erlaubnis anzufordern, es sei denn, Ihre Website wurde zum Startbildschirm des Nutzers:innen hinzugefügt. 

Mit dem Feature [Zum Homescreen hinzufügen](https://support.apple.com/guide/iphone/bookmark-favorite-webpages-iph42ab2f3a7/ios#iph4f9a47bbc) können Nutzer:innen Ihre Website mit einem Lesezeichen versehen und Ihr Icon auf ihrem wertvollen Homescreen platzieren.

![Ein iPhone mit Optionen zum Setzen von Lesezeichen für eine Website und zum Speichern auf dem Startbildschirm]({% image_buster /assets/img/push_implementation_guide/add-to-homescreen.png %}){: style="max-width:40%"}

### Schritt 5: Zeigen Sie die native Push-Eingabeaufforderung {#push-prompt} an.
Sobald die App zu Ihrem Startbildschirm hinzugefügt wurde, können Sie jetzt die Push-Erlaubnis anfragen, wenn der Nutzer:innen eine Aktion ausführt (z.B. auf einen Button klickt). Dies kann mit der [`requestPushPermission`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#requestpushpermission) Methode oder mit einer [In-App-Nachricht ohne Code-Push-Primer]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_primer_messages/).

{% alert note %}
Wenn Sie die Aufforderung akzeptieren oder ablehnen, müssen Sie die Website löschen und erneut auf Ihrem Startbildschirm installieren, um die Aufforderung erneut anzeigen zu können.
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

Als nächstes senden Sie sich selbst eine [Testnachricht]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/sending_test_messages/), um die Integration zu überprüfen. Nachdem Ihre Integration abgeschlossen ist, können Sie unsere [Push-Nachrichten ohne Code]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_primer_messages/) verwenden, um Ihre Opt-in-Raten zu optimieren.

