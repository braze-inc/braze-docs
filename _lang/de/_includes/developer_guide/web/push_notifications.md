{% multi_lang_include archive/web-v4-rename.md %}

{% multi_lang_include developer_guide/prerequisites/web.md %}

## Push-Protokolle

Web-Push-Benachrichtigungen werden mithilfe des [W3C-Push-Standards](http://www.w3.org/TR/push-api/) implementiert, den die meisten gängigen Browser unterstützen. Weitere Informationen über die spezifischen Push-Protokollstandards und die Browserunterstützung finden Sie in den Ressourcen von [Apple](https://developer.apple.com/notifications/safari-push-notifications/) [, Mozilla](https://developer.mozilla.org/en-us/docs/web/api/push_api#browser_compatibility) und [Microsoft](https://developer.microsoft.com/en-us/microsoft-edge/status/pushapi/).

## Push-Benachrichtigungen einrichten

### Schritt 1: Konfigurieren Sie Ihr Service-Teammitglied

Fügen Sie in der Datei `service-worker.js` Ihres Projekts das folgende Snippet hinzu und setzen Sie die [`manageServiceWorkerExternally`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize) Initialisierungsoption auf `true`, wenn Sie das Internet SDK initialisieren.

<script src="{{site.baseurl}}/assets/js/embed.js?target=https://github.com/braze-inc/braze-web-sdk/blob/master/sample-builds/cdn/service-worker.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

{% alert important %}
Ihr Server muss eine `Content-Type: application/javascript` zurückgeben, wenn er Ihre Service-Teammitglied-Datei bedient. Wenn die Datei Ihres Service-Teammitglieds nicht `service-worker.js` heißt, müssen Sie außerdem die [Initialisierungsoption](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions) `serviceWorkerLocation` verwenden.
{% endalert %}

### Schritt 2: Registrieren Sie den Browser

Um sofort die Push-Berechtigungen eines Nutzers:innen anzufordern, damit sein Browser Push-Benachrichtigungen empfangen kann, rufen Sie `braze.requestPushPermission()` auf. Um zunächst zu testen, ob Push in ihrem Browser unterstützt wird, rufen Sie `braze.isPushSupported()` auf.

Sie können dem Nutzer:innen auch [eine Soft-Push-Eingabeaufforderung senden]({{site.baseurl}}/developer_guide/push_notifications/soft_push_prompts/?sdktab=web), bevor Sie die Push-Erlaubnis anfordern, um Ihre eigene Push-bezogene UI anzuzeigen.

{% alert important %}
Unter macOS müssen sowohl **Google Chrome** als auch **Google Chrome Helper (Alerts)** vom Endnutzer unter **Systemeinstellungen > Benachrichtigungen** aktiviert werden, bevor Push-Benachrichtigungen angezeigt werden können - auch wenn die Berechtigungen erteilt wurden.
{% endalert %}

### Schritt 3: Deaktivieren Sie `skipWaiting` (optional)

Die Datei des Service-Teammitglieds von Braze ruft bei der Installation automatisch `skipWaiting` auf. Wenn Sie diese Funktion deaktivieren möchten, fügen Sie nach dem Import von Braze den folgenden Code in Ihre Service-Teammitglied-Datei ein:

<script src="{{site.baseurl}}/assets/js/embed.js?target=https%3A%2F%2Fgithub.com%2Fbraze-inc%2Fbraze-web-sdk%2Fblob%2Fmaster%2Fsnippets%2Fservice-worker-skip-waiting.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

## Abmelden eines Nutzer:in

Um einen Nutzer:innen abzumelden, rufen Sie `braze.unregisterPush()` auf.

{% alert important %}
Aktuelle Versionen von Safari und Firefox erfordern, dass Sie diese Methode von einem kurzlebigen Event Handler aus aufrufen (z.B. von einem Button-Klick Handler oder einer Soft Push Eingabeaufforderung). Dies steht im Einklang mit [den Best Practices für Chrome-Nutzer ](https://docs.google.com/document/d/1WNPIS_2F0eyDm5SS2E6LZ_75tk6XtBSnR1xNjWJ_DPE) zur Push-Registrierung.
{% endalert %}

## Alternative Domains

Für die Integration von Web-Push muss Ihre Domain [sicher](https://w3c.github.io/webappsec-secure-contexts/) sein, was im Allgemeinen bedeutet: `https`, `localhost` und andere Ausnahmen, die im [W3C-Push-Standard](https://www.w3.org/TR/service-workers/#security-considerations) definiert sind. Sie müssen auch in der Lage sein, ein Service-Teammitglied im Stammverzeichnis Ihrer Domain zu registrieren oder zumindest die HTTP-Header für diese Datei zu kontrollieren. Dieser Artikel beschreibt, wie Sie Braze Web-Push in eine andere Domain integrieren.

### Anwendungsfälle

Wenn Sie nicht alle Kriterien des [W3C-Push-Standards](https://www.w3.org/TR/service-workers/#security-considerations) erfüllen können, können Sie stattdessen diese Methode verwenden, um Ihrer Website einen Push-Dialog hinzuzufügen. Dies kann hilfreich sein, wenn Sie Ihren Nutzer:innen das Opt-in von einer Website `http` oder einem Popup-Fenster einer Browsererweiterung ermöglichen möchten, das die Anzeige Ihrer Push-Anfrage verhindert.

### Überlegungen

Denken Sie daran, dass sich die Browser, wie viele andere Lösungen im Internet, ständig weiterentwickeln und dass diese Methode in Zukunft möglicherweise nicht mehr praktikabel ist. Bevor Sie fortfahren, vergewissern Sie sich, dass:

- Sie besitzen eine eigene sichere Domain (`https://`) und die Berechtigung, ein Service-Teammitglied in dieser Domain zu registrieren.
- Die Nutzer:innen sind auf Ihrer Website angemeldet, so dass die Push-Tokens dem richtigen Profil zugeordnet werden können.

{% alert important %}
Sie können diese Methode nicht verwenden, um Push-Benachrichtigungen für Shopify zu implementieren. Shopify entfernt automatisch die Header, die für die Bereitstellung von Push auf diese Weise erforderlich sind.
{% endalert %}

### Einrichten einer alternativen Push Domain

Um das folgende Beispiel zu verdeutlichen, verwenden wir `http://insecure.com` und `https://secure.com` als unsere beiden Domains mit dem Ziel, Besucher dazu zu bringen, sich für Push auf `http://insecure.com` zu registrieren. Dieses Beispiel könnte auch auf ein `chrome-extension://` Schema für die Popup-Seite einer Browser-Erweiterung angewendet werden.

#### Schritt 1: Prompting Flow initiieren

Auf `insecure.com` öffnen Sie ein neues Fenster zu Ihrer sicheren Domain, indem Sie einen URL-Parameter verwenden, um die externe ID des aktuell angemeldeten Nutzers zu übergeben.

**http://insecure.com**
```html
<button id="opt-in">Opt-In For Push</button>
<script>
// the same ID you would use with `braze.changeUser`:
const user_id = getUserIdSomehow();
// pass the user ID into the secure domain URL:
const secure_url = `https://secure.com/push-registration.html?external_id=${user_id}`;

// when the user takes some action, open the secure URL in a new window
document.getElementById("opt-in").onclick = function(){
    if (!window.open(secure_url, 'Opt-In to Push', 'height=500,width=600,left=150,top=150')) {
        window.alert('The popup was blocked by your browser');
    } else {
        // user is shown a popup window
        // and you can now prompt for push in this window
    }
}
</script>
```

#### Schritt 2: Für Push registrieren

An dieser Stelle öffnet `secure.com` ein Popup-Fenster, in dem Sie das Braze Web SDK für dieselbe Nutzer-ID initialisieren und die Nutzererlaubnis für Web-Push anfordern können.

**https://secure.com/push-registration.html**

<script src="{{site.baseurl}}/assets/js/embed.js?target=https%3A%2F%2Fgithub.com%2Fbraze-inc%2Fbraze-web-sdk%2Fblob%2Fmaster%2Fsnippets%2Falternate-push-domain-registration.html&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

#### Schritt 3: Kommunikation zwischen Domains (optional)

Jetzt, da die Nutzer über diesen Workflow auf `insecure.com` ein Opt-in durchführen können, möchten Sie vielleicht Ihre Website anpassen, je nachdem, ob der Nutzer bereits ein Opt-in hat oder nicht. Es macht keinen Sinn, die Nutzer aufzufordern, sich für Push zu registrieren, wenn sie bereits registriert sind.

Sie können iFrames und die [`postMessage`](https://developer.mozilla.org/en-US/docs/Web/API/Window/postMessage)-API verwenden, um zwischen Ihren beiden Domains zu kommunizieren. 

**insecure.com**

Auf unserer Domain `insecure.com` fragen wir die sichere Domain (auf der Push _tatsächlich_ registriert ist) nach Informationen über die Push-Registrierung des aktuellen Nutzers:innen:

```html
<!-- Create an iframe to the secure domain and run getPushStatus onload-->
<iframe id="push-status" src="https://secure.com/push-status.html" onload="getPushStatus()" style="display:none;"></iframe>

<script>
function getPushStatus(event){
    // send a message to the iframe asking for push status
    event.target.contentWindow.postMessage({type: 'get_push_status'}, 'https://secure.com');
    // listen for a response from the iframe's domain
    window.addEventListener("message", (event) => {
        if (event.origin === "http://insecure.com" && event.data.type === 'set_push_status') {
            // update the page based on the push permission we're told
            window.alert(`Is user registered for push? ${event.data.isPushPermissionGranted}`);
        }
    }   
}
</script>
```

**secure.com/Push-status.html**

<script src="{{site.baseurl}}/assets/js/embed.js?target=https%3A%2F%2Fgithub.com%2Fbraze-inc%2Fbraze-web-sdk%2Fblob%2Fmaster%2Fsnippets%2Falternate-push-domain-status.html&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

## Häufig gestellte Fragen (FAQ)

### Service-Teammitglieder

#### Was ist, wenn ich ein Service-Teammitglied nicht im Stammverzeichnis registrieren kann?

Standardmäßig kann ein Service-Teammitglied nur in demselben Verzeichnis verwendet werden, in dem es registriert ist. Wenn Ihr Service-Teammitglied z.B. in `/assets/service-worker.js` vorhanden ist, können Sie es nur in `example.com/assets/*` oder einem Unterverzeichnis des Ordners `assets` registrieren, nicht aber auf Ihrer Homepage (`example.com/`). Aus diesem Grund empfiehlt es sich, das Service-Teammitglied im Stammverzeichnis (z. B. `https://example.com/service-worker.js`) zu hosten und zu registrieren.

Wenn Sie kein Service-Teammitglied in Ihrer Root-Domain registrieren können, besteht eine Alternative darin, den HTTP-Header [`Service-Worker-Allowed`](https://w3c.github.io/ServiceWorker/#service-worker-script-response) zu verwenden, wenn Sie Ihre Service-Teammitglied-Datei bereitstellen. Wenn Sie Ihren Server so konfigurieren, dass in der Antwort für das Service-Teammitglied `Service-Worker-Allowed: /` zurückgegeben wird, weist dies den Browser an, den Geltungsbereich zu erweitern und die Verwendung aus einem anderen Verzeichnis zuzulassen.

#### Kann ich ein Service-Teammitglied mit Hilfe eines Tag Managers erstellen?

Nein, Service-Teammitglieder müssen auf dem Server Ihrer Website gehostet werden und können nicht über den Tag Manager geladen werden.

### Sicherheit vor Ort

#### Ist HTTPS erforderlich?

Ja Die Internet-Standards verlangen, dass die Domain, die die Erlaubnis zur Push-Benachrichtigung anfragt, sicher ist.

#### Wann gilt eine Website als "sicher"?

Eine Website gilt als sicher, wenn sie einem der folgenden Muster für die sichere Herkunft entspricht. Braze Web-Push-Benachrichtigungen basieren auf diesem offenen Standard, so dass Man-in-the-Middle-Angriffe verhindert werden.

- `(https, , *)`
- `(wss, *, *)`
- `(, localhost, )`
- `(, .localhost, *)`
- `(, 127/8, )`
- `(, ::1/128, *)`
- `(file, *, —)`
- `(chrome-extension, *, —)`

#### Was ist, wenn eine sichere Website nicht verfügbar ist?

Obwohl es sich bewährt hat, die gesamte Website zu sichern, können Kunden, die ihre Domain nicht sichern können, diese Anforderung durch die Verwendung eines sicheren Modals umgehen. Lesen Sie mehr in unserer Anleitung zur Verwendung von [Alternate push domain]({{ site.baseurl }}/developer_guide/platform_integration_guides/web/push_notifications/alternate_push_domain) oder sehen Sie sich eine [funktionierende Demo](http://appboyj.com/modal-test.html) an.
