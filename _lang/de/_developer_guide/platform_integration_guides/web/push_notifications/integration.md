---
nav_title: Integration
article_title: Push-Integration für das Internet
platform: Web
channel: push
page_order: 0
page_type: reference
description: "Dieser Artikel beschreibt, wie Sie Braze Web-Push über das Braze SDK integrieren."

local_redirect: #soft-push-prompts
  soft-push-prompts: '/docs/developer_guide/platform_integration_guides/web/push_notifications/soft_push_prompt/'
search_rank: 3
---

# Integration von Push-Benachrichtigungen

> Eine Push-Benachrichtigung ist eine Benachrichtigung, die auf dem Bildschirm des Nutzers erscheint, wenn ein wichtiges Update stattfindet. Push-Benachrichtigungen können auch dann empfangen werden, wenn Ihre Webseite im Browser des Nutzers:innen gerade nicht geöffnet ist. Push-Benachrichtigungen sind eine wertvolle Möglichkeit, Ihre Nutzer:innen mit zeitkritischen und relevanten Inhalten zu versorgen oder sie mit Ihrer Website zu erneuern. Dieser Referenzartikel  beschreibt die Integration von Braze Web-Push mit dem Braze SDK.

Weitere Ressourcen finden Sie in unseren [Push-Best Practices]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/).

![]({{site.baseurl}}/assets/img_archive/web_push2.png)

Web-Push-Benachrichtigungen werden mithilfe des [W3C-Push-Standards](http://www.w3.org/TR/push-api/) implementiert, den die meisten gängigen Browser unterstützen.

Weitere Informationen zu den Push-Protokollstandards und der Browserunterstützung finden Sie in den Ressourcen von [AppleSafari](https://developer.apple.com/notifications/safari-push-notifications/ "Push-Benachrichtigungen") [MozillaMozilla](https://developer.mozilla.org/en-us/docs/web/api/push_api#browser_compatibility "Push API Browser-Kompatibilität") und [MicrosoftMicrosoft](https://developer.microsoft.com/en-us/microsoft-edge/status/pushapi/ "Push API")

{% multi_lang_include archive/web-v4-rename.md %}

## Integration

### Schritt 1: Konfigurieren Sie das Service-Teammitglied Ihrer Website

- Wenn Sie noch kein Service-Teammitglied haben, erstellen Sie eine neue Datei namens `service-worker.js` mit dem folgenden Snippet und legen Sie diese im Stammverzeichnis Ihrer Website ab.
- Andernfalls, wenn Ihre Website bereits ein Service-Teammitglied registriert, fügen Sie das folgende Snippet in die Datei des Service-Teammitglieds ein und setzen Sie die [`manageServiceWorkerExternally`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize) Initialisierungsoption bei der Initialisierung des Web SDK auf `true`.

<script src="{{site.baseurl}}/assets/js/embed.js?target=https://github.com/braze-inc/braze-web-sdk/blob/master/sample-builds/cdn/service-worker.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

Wenn der Dateiname Ihres Service-Teammitglieds nicht `service-worker.js` lautet, müssen Sie die [Initialisierungsoption](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions) `serviceWorkerLocation` verwenden.

{% alert important %}
Ihr Server muss eine `Content-Type: application/javascript` zurückgeben, wenn er Ihre Service-Teammitglied-Datei bedient.
{% endalert %}

#### Was ist, wenn ich ein Service-Teammitglied nicht im Stammverzeichnis registrieren kann?

Standardmäßig kann ein Service-Teammitglied nur in demselben Verzeichnis verwendet werden, in dem es registriert ist. Wenn Ihr Service-Teammitglied z.B. in `/assets/service-worker.js` vorhanden ist, können Sie es nur in `example.com/assets/*` oder einem Unterverzeichnis des Ordners `assets` registrieren, nicht aber auf Ihrer Homepage (`example.com/`). Aus diesem Grund empfiehlt es sich, das Service-Teammitglied im Stammverzeichnis (z. B. `https://example.com/service-worker.js`) zu hosten und zu registrieren.

Wenn Sie kein Service-Teammitglied in Ihrer Root-Domain registrieren können, besteht eine Alternative darin, den HTTP-Header [`Service-Worker-Allowed`](https://w3c.github.io/ServiceWorker/#service-worker-script-response) zu verwenden, wenn Sie Ihre Service-Teammitglied-Datei bereitstellen. Wenn Sie Ihren Server so konfigurieren, dass in der Antwort für das Service-Teammitglied `Service-Worker-Allowed: /` zurückgegeben wird, weist dies den Browser an, den Geltungsbereich zu erweitern und die Verwendung aus einem anderen Verzeichnis zuzulassen.

#### Kann ich ein Service-Teammitglied mit Hilfe eines Tag Managers erstellen?

Nein, Service-Teammitglieder müssen auf dem Server Ihrer Website gehostet werden und können nicht über den Tag Manager geladen werden.

### Schritt 2: Browser-Registrierung

Damit ein Browser Push-Benachrichtigungen empfangen kann, müssen Sie ihn für Push registrieren, indem Sie `braze.requestPushPermission()` aufrufen. Dadurch werden Nutzer sofort um eine Push-Erlaubnis gebeten. 

Wenn Sie dem Nutzer:innen Ihre eigene Push-bezogene UI zeigen möchten, bevor Sie die Push-Erlaubnis anfragen (bekannt als Soft Push Prompt), können Sie mit `braze.isPushSupported()` testen, ob Push im Browser des Nutzers:innen unterstützt wird. Referenzieren Sie das [Beispiel für die Soft-Push-Aufforderung]({{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/soft_push_prompt/) mit In-App-Nachrichten.

Wenn Sie einen Nutzer abmelden möchten, können Sie dies unter `braze.unregisterPush()` tun.

{% alert important %}
In den neueren Versionen von Safari und Firefox müssen Sie diese Methode von einem kurzlebigen Event Handler aus aufrufen (z.B. von einem Button Click Handler oder einem Soft Push Prompt). Dies steht im Einklang mit [den Best Practices für Chrome-Nutzer ](https://docs.google.com/document/d/1WNPIS_2F0eyDm5SS2E6LZ_75tk6XtBSnR1xNjWJ_DPE) zur Push-Registrierung.
{% endalert %}

### Schritt 3: Konfigurieren Sie Safari Push (optional) {#safari}

{% alert important %}
Dieser Schritt ist ab Safari 16 auf macOS 13 nicht mehr erforderlich. Führen Sie diesen Schritt nur aus, wenn Sie ältere macOS Safari-Versionen unterstützen möchten.
{% endalert %}

Wenn Sie Push-Benachrichtigungen für Safari unter Mac OS X unterstützen möchten, folgen Sie diesen zusätzlichen Anweisungen:

- Erzeugen Sie ein Safari Push-Zertifikat, indem Sie die Anweisungen zur [Registrierung bei Apple](https://developer.apple.com/library/mac/documentation/NetworkingInternet/Conceptual/NotificationProgrammingGuideForWebsites/PushNotifications/PushNotifications.html#//apple_ref/doc/uid/TP40013225-CH3-SW33) befolgen.
- Wählen Sie im Braze-Dashboard auf der Seite **Einstellungen** (wo sich Ihre API-Schlüssel befinden) Ihre Internet App aus. Klicken Sie auf **Safari Push konfigurieren** und folgen Sie den Anweisungen, indem Sie das soeben erstellte Push-Zertifikat hochladen.
- Wenn Sie `braze.initialize` aufrufen, geben Sie bei der optionalen Konfigurationsoption `safariWebsitePushId` die Website Push ID an, die Sie bei der Erstellung Ihres Safari Push-Zertifikats verwendet haben. Zum Beispiel `braze.initialize('YOUR-API-KEY', {safariWebsitePushId: 'web.com.example.domain'})`

## Safari Mobile Push {#safari-mobile}

Safari 16.4+ auf iOS und iPadOS unterstützt Web-Push für Apps, die [dem Homescreen hinzugefügt wurden](https://support.apple.com/guide/iphone/bookmark-favorite-webpages-iph42ab2f3a7/ios#iph4f9a47bbc) und über eine [Web Application Manifest-Datei](https://developer.mozilla.org/en-US/docs/Web/Manifest) verfügen. Nachdem Sie die Schritte zur Integration von Web-Push-Benachrichtigungen abgeschlossen haben, können Sie auch Unterstützung für Mobile Push für Safari bereitstellen. 

Um den mobilen Web-Push für Safari zu unterstützen, befolgen Sie [diese Anleitung]({{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/safari_mobile_push/).

## Soft-Push-Aufforderung

Eine Soft-Push-Anfrage (auch "Push Primer" genannt) hilft Ihnen bei der Verbesserung der Opt-in-Rate bei Erlaubnisanforderungen.

Besuchen Sie [Soft push prompt]({{ site.baseurl }}/developer_guide/platform_integration_guides/web/push_notifications/soft_push_prompt/) um mehr über die Einrichtung einer Soft-Push-Anfrage zu erfahren.

## HTTPS-Anforderung

Die Internet-Standards verlangen, dass die Domain, die die Erlaubnis zur Push-Benachrichtigung anfragt, sicher ist.

### Was macht eine sichere Website aus?

Eine Website gilt als sicher, wenn sie einem der folgenden Muster für die sichere Herkunft entspricht:

- (https, , \*)
- (wss, \*, \*)
- (, localhost, )
- (, .localhost, \*)
- (, 127/8, )
- (, ::1/128, \*)
- (file, \*, —)
- (chrome-extension, \*, —)

Diese Sicherheitsanforderung in der Spezifikation für offene Standards, auf der Braze Web-Push aufbaut, verhindert Man-in-the-Middle-Angriffe.

### Was ist, wenn eine sichere Website nicht verfügbar ist?

Obwohl es sich bewährt hat, die gesamte Website zu sichern, können Kunden, die ihre Domain nicht sichern können, diese Anforderung durch die Verwendung eines sicheren Modals umgehen. Lesen Sie mehr in unserer Anleitung zur Verwendung von [Alternate push domain]({{ site.baseurl }}/developer_guide/platform_integration_guides/web/push_notifications/alternate_push_domain) oder sehen Sie sich eine [funktionierende Demo](http://appboyj.com/modal-test.html) an.

## Erweiterte Einstellungen für Service-Teammitglieder

Unsere Service-Teammitglied-Datei ruft bei der Installation automatisch `skipWaiting` auf. Wenn Sie dies vermeiden möchten, fügen Sie den folgenden Code in Ihre Service-Teammitglied-Datei ein, bevor Sie Braze importieren:

<script src="{{site.baseurl}}/assets/js/embed.js?target=https%3A%2F%2Fgithub.com%2Fbraze-inc%2Fbraze-web-sdk%2Fblob%2Fmaster%2Fsnippets%2Fservice-worker-skip-waiting.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

## Fehlersuche

**Ich habe die Anweisungen zur Integration befolgt, aber ich erhalte immer noch keine Push-Benachrichtigungen.**
- Für Web-Push-Benachrichtigungen muss Ihre Website über HTTPS verfügen.
- Nicht alle Browser können Push-Nachrichten empfangen. Stellen Sie sicher, dass `braze.isPushSupported()` im Browser `true` zurückgibt.
- Wenn ein Nutzer:innen den Push-Zugriff auf eine Website verweigert hat, wird er nicht mehr um Erlaubnis gefragt, es sei denn, er entfernt den Status "verweigert" aus seinen Browsereinstellungen.

