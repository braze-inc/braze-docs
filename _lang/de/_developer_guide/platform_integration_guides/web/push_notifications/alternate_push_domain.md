---
nav_title: Alternative Web-Push Domain
article_title: Alternative Web-Push Domain
platform: Web
page_order: 20
page_type: reference
description: "Dieser Artikel beschreibt, wie Sie Braze Web-Push in eine andere Domain integrieren."
channel: push

---

# Alternative Web-Push-Domain

> Für die Integration von Web-Push muss Ihre Domain [sicher](https://w3c.github.io/webappsec-secure-contexts/) sein, was im Allgemeinen bedeutet: `https`, `localhost` und andere Ausnahmen, die im [W3C-Push-Standard](https://www.w3.org/TR/service-workers/#security-considerations) definiert sind. Sie müssen auch in der Lage sein, ein Service-Teammitglied im Stammverzeichnis Ihrer Domain zu registrieren oder zumindest die HTTP-Header für diese Datei zu kontrollieren. Dieser Artikel beschreibt, wie Sie Braze Web-Push in eine andere Domain integrieren.

_Wenn Sie nicht in der Lage sind, alle diese Kriterien zu erfüllen_, verwenden Sie diese Anleitung, um einen Workaround einzurichten, mit dem Sie Ihrer Website einen Push-Dialog hinzufügen können. Dieser Artikel wäre zum Beispiel hilfreich, wenn Sie möchten, dass der Nutzer:in von einer `http` (unsicheren) Website oder von einem Popup der Browsererweiterung, das die Anzeige der Push-Anfrage verhindert, zum Opt-in aufgefordert wird.

## Vorbehalte
Denken Sie daran, dass sich die Browser, wie viele andere Umgehungslösungen im Internet, ständig weiterentwickeln und dass dies in Zukunft möglicherweise nicht mehr wie vorgesehen funktioniert.

- Dies setzt voraus, dass:
  - Sie besitzen eine eigene sichere Domain (`https://`) und können ein Service-Teammitglied auf dieser Domain registrieren.
  - Nutzer:innen müssen auf Ihrer Website eingeloggt sein, um sicherzustellen, dass Push-Token mit denselben Profilen verknüpft sind.

{% alert note %}
Push für Shopify kann nicht auf diese Weise implementiert werden. Shopify entfernt Header, die für die Bereitstellung von Push erforderlich sind.
{% endalert %}

## Integration

Um das folgende Beispiel zu verdeutlichen, verwenden wir `http://insecure.com` und `https://secure.com` als unsere beiden Domains mit dem Ziel, Besucher dazu zu bringen, sich für Push auf `http://insecure.com` zu registrieren. Dieses Beispiel könnte auch auf ein `chrome-extension://` Schema für die Popup-Seite einer Browser-Erweiterung angewendet werden.

### Schritt 1: Prompting Flow initiieren

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

### Schritt 2: Für Push registrieren

An dieser Stelle öffnet `secure.com` ein Popup-Fenster, in dem Sie das Braze Web SDK für dieselbe Nutzer-ID initialisieren und die Nutzererlaubnis für Web-Push anfordern können.

**https://secure.com/push-registration.html**

<script src="{{site.baseurl}}/assets/js/embed.js?target=https%3A%2F%2Fgithub.com%2Fbraze-inc%2Fbraze-web-sdk%2Fblob%2Fmaster%2Fsnippets%2Falternate-push-domain-registration.html&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

### Schritt 3: Kommunikation zwischen Domains (optional)

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

