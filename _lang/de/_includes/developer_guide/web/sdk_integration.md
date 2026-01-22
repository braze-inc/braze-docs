## Über das Internet Braze SDK

Mit dem Web Braze SDK können Sie Analytics sammeln und Ihren Nutzer:innen In-App-Nachrichten, Push- und Content-Card-Nachrichten anzeigen. Weitere Informationen finden Sie in der [Braze JavaScript referenzierenden Dokumentation](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html).

{% multi_lang_include archive/web-v4-rename.md %}

## Integration des Internet SDK

Sie können das Internet Braze SDK mit den folgenden Methoden integrieren. Weitere Optionen finden Sie unter [Andere Integrationsmethoden](#web_other-integration-methods).

- **Code-basierte Integration:** Integrieren Sie das Internet Braze SDK direkt in Ihre Codebasis, indem Sie Ihren bevorzugten Package Manager oder das Braze CDN verwenden. So haben Sie die volle Kontrolle darüber, wie das SDK geladen und konfiguriert wird.
- **Google Tag Manager:** Eine Lösung ohne Code, mit der Sie das Web Braze SDK integrieren können, ohne den Code Ihrer Website zu ändern. Weitere Informationen finden Sie unter [Google Tag Manager mit dem Braze SDK]({{site.baseurl}}/developer_guide/sdk_integration/google_tag_manager/).

{% tabs local %}
{% tab Code-basierte Integration %}
### Schritt 1: Installieren Sie die Braze-Bibliothek

Sie können die Braze-Bibliothek mit einer der folgenden Methoden installieren. Wenn Ihre Website jedoch eine `Content-Security-Policy` verwendet, sollten Sie die [Richtlinie zur Sicherheit von Inhalten]({{site.baseurl}}/developer_guide/platforms/web/content_security_policy/) lesen, bevor Sie fortfahren.

{% alert important %}
Während die meisten Werbeblocker das Braze Web SDK nicht blockieren, sind einige restriktivere Werbeblocker dafür bekannt, dass sie Probleme verursachen.
{% endalert %}

{% subtabs %}
{% subtab package manager %}
Wenn Ihre Website die Paketmanager NPM oder Yarn verwendet, können Sie das [NPM-Paket von Braze](https://www.npmjs.com/package/@braze/web-sdk) als Abhängigkeit hinzufügen.

Ab v3.0.0 sind nun auch Typescript-Definitionen enthalten. Hinweise zum Upgrade von 2.x auf 3.x finden Sie in unserem [Changelog](https://github.com/braze-inc/braze-web-sdk/blob/master/UPGRADE_GUIDE.md).

```bash
npm install --save @braze/web-sdk
# or, using yarn:
# yarn add @braze/web-sdk
```

Nach der Installation können Sie die Bibliothek auf die übliche Weise mittels `import` oder `require` verwenden:

```typescript
import * as braze from "@braze/web-sdk";
// or, using `require`
const braze = require("@braze/web-sdk");
```
{% endsubtab %}

{% subtab braze cdn %}
Fügen Sie das Braze Web SDK direkt in den HTML-Code ein, indem Sie auf das auf unserem CDN gehostete Skript verweisen, das die Bibliothek asynchron lädt.

<script src="{{site.baseurl}}/assets/js/embed.js?target=https%3A%2F%2Fgithub.com%2Fbraze-inc%2Fbraze-web-sdk%2Fblob%2Fmaster%2Fsnippets%2Floading-snippet.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>
{% endsubtab %}
{% endsubtabs %}

### Schritt 2: Initialisieren Sie das SDK

Nachdem das Braze Web SDK zu Ihrer Website hinzugefügt wurde, initialisieren Sie die Bibliothek mit dem API-Schlüssel und der [SDK-Endpunkt-URL]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints), die Sie in Ihrem Braze-Dashboard unter **Einstellungen** > **App-Einstellungen** finden. Eine vollständige Liste der Optionen für `braze.initialize()` sowie unsere anderen JavaScript-Methoden finden Sie in der [Braze JavaScript Dokumentation](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize).

```javascript
// initialize the SDK
braze.initialize('YOUR-API-KEY-HERE', {
    baseUrl: "YOUR-SDK-ENDPOINT-HERE",
    enableLogging: false, // set to `true` for debugging
    allowUserSuppliedJavascript: false, // set to `true` to support custom HTML messages
});

// optionally show all in-app messages without custom handling
braze.automaticallyShowInAppMessages();

// if you use Content Cards
braze.subscribeToContentCardsUpdates(function(cards){
    // cards have been updated
});

// optionally set the current user's external ID before starting a new session
// you can also call `changeUser` later in the session after the user logs in
if (isLoggedIn){
    braze.changeUser(userIdentifier);
}

// `openSession` should be called last - after `changeUser` and `automaticallyShowInAppMessages`
braze.openSession();
```

{% alert important %}
Anonyme Nutzer auf Mobil- oder Webgeräten können zu Ihrer [MAU]({{site.baseurl}}/user_guide/data_and_analytics/reporting/understanding_your_app_usage_data/#monthly-active-users) gezählt werden. Vielleicht möchten Sie das SDK deshalb lieber bedingt laden oder initialisieren, um diese Nutzer von der MAU-Zählung auszuschließen.
{% endalert %}
{% endtab %}

{% tab Google Tag Manager %}
{% multi_lang_include developer_guide/web/google_tag_manager/initialization_tag.md %}
{% endtab %}
{% endtabs %}

## Optionale Konfigurationen

### Protokollieren

Um die Protokollierung schnell zu aktivieren, können Sie `?brazeLogging=true` als Parameter in die URL Ihrer Website einfügen. Alternativ können Sie auch die [einfache](#web_basic-logging) oder [benutzerdefinierte](#web_custom-logging) Protokollierung aktivieren.

#### Grundlegende Protokollierung

{% tabs local %}
{% tab vor der Initialisierung %}
Verwenden Sie `enableLogging`, um grundlegende Nachrichten zur Fehlersuche auf der JavaScript-Konsole zu protokollieren, bevor das SDK initialisiert wird.

```javascript
enableLogging: true
```

Ihre Methode sollte in etwa so aussehen wie die folgende:

```javascript
braze.initialize('API-KEY', {
    baseUrl: 'API-ENDPOINT',
    enableLogging: true
});
braze.openSession();
```
{% endtab %}

{% tab nach der Initialisierung %}
Verwenden Sie `braze.toggleLogging()`, um grundlegende Nachrichten zur Fehlersuche in der JavaScript-Konsole zu protokollieren, nachdem das SDK initialisiert wurde. Ihre Methode sollte in etwa so aussehen wie die folgende:

```javascript
braze.initialize('API-KEY', {
    baseUrl: 'API-ENDPOINT',
});
braze.openSession();
...
braze.toggleLogging();
```
{% endtab %}
{% endtabs %}

{% alert important %}
Die Basisprotokolle sind für alle Nutzer sichtbar. Daher sollten Sie diese Funktion deaktivieren oder zu [`setLogger`](#web_custom-logging) wechseln, bevor Sie Ihren Code für die Produktionsumgebung freigeben.
{% endalert %}

#### Benutzerdefinierte Protokollierung

Verwenden Sie `setLogger`, um angepasste Nachrichten zur Fehlersuche in der JavaScript-Konsole zu protokollieren. Im Gegensatz zu den Basisprotokollen sind diese Protokolle für die Benutzer nicht sichtbar.

```javascript
setLogger(loggerFunction: (message: STRING) => void): void
```

Ersetzen Sie `STRING` durch Ihre Nachricht als einzelnen String-Parameter. Ihre Methode sollte in etwa so aussehen wie die folgende:

```javascript
braze.initialize('API-KEY');
braze.setLogger(function(message) {
    console.log("Braze Custom Logger: " + message);
});
braze.openSession();
```

## Upgraden des SDK

{% multi_lang_include archive/web-v4-rename.md %}

Wenn Sie das Braze Web SDK von unserem Content Delivery Network aus referenzieren, z. B. durch `https://js.appboycdn.com/web-sdk/a.a/braze.min.js` (wie in unseren Anweisungen für die Standard-Integration empfohlen), erhalten Ihre Nutzer automatisch kleinere Updates (Fehlerbehebungen und abwärtskompatible Features; in den obigen Beispielen die Versionen `a.a.a` bis `a.a.z`), wenn sie Ihre Website aktualisieren.

Wenn wir jedoch größere Änderungen veröffentlichen, müssen Sie das Braze Web SDK manuell upgraden, um sicherzustellen, dass sich die Änderungen nicht auf Ihre Integration auswirken. Wenn Sie unser SDK herunterladen und selbst hosten, erhalten Sie keine automatischen Versions-Updates und sollten manuell upgraden, um die neuesten Features und Fehlerbehebungen zu erhalten.

Um auf dem aktuellen Stand zu bleiben, empfehlen wir Ihnen, mit dem RSS-Reader oder einem anderen Dienst Ihrer Wahl [unsere Release-Feed zu abonnieren](https://github.com/braze-inc/braze-web-sdk/tags.atom). Einen vollständigen Überblick über die Release-Historie unseres Web SDK finden Sie in [unserem Changelog](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md). So führen Sie ein Upgrade des Braze Web SDK durch:

- Aktualisieren Sie die Version der Braze Bibliothek, indem Sie die Versionsnummer von `https://js.appboycdn.com/web-sdk/[OLD VERSION NUMBER]/braze.min.js` ändern. Sie können die Aktualisierung auch in Abhängigkeiten des Paketmanagers vornehmen.
- Wenn Sie Web-Push integriert haben, aktualisieren Sie die Service-Worker-Datei auf Ihrer Website - standardmäßig befindet sich diese Datei unter `/service-worker.js` im Stammverzeichnis Ihrer Website, aber der Speicherort kann bei einigen Integrationen angepasst werden. Sie müssen auf das Stammverzeichnis zugreifen, um eine Service Worker-Datei zu hosten.

Diese beiden Dateien müssen in Abstimmung miteinander aktualisiert werden, damit sie ordnungsgemäß funktionieren.

## Andere Methoden der Integration

### Accelerated Mobile Pages (AMP)
{% details Mehr sehen %}
#### Schritt 1: AMP Web-Push-Skript einbinden

Fügen Sie den folgenden asynchronen Tag in Ihren Head ein:

```js
<script async custom-element="amp-web-push" src="https://cdn.ampproject.org/v0/amp-web-push-0.1.js"></script>
```

#### Schritt 2: Abo-Widgets hinzufügen

Fügen Sie ein Widget in den Body Ihres HTML-Formats ein, mit dem Nutzer:innen sich bei Push anmelden und abmelden können.

```js
<!-- A subscription widget -->
<amp-web-push-widget visibility="unsubscribed" layout="fixed" width="250" height="80">
  <button on="tap:amp-web-push.subscribe">Subscribe to Notifications</button>
</amp-web-push-widget>

<!-- An unsubscription widget -->
<amp-web-push-widget visibility="subscribed" layout="fixed" width="250" height="80">
  <button on="tap:amp-web-push.unsubscribe">Unsubscribe from Notifications</button>
</amp-web-push-widget>
```

#### Schritt 3: Fügen Sie `helper-iframe` und `permission-dialog`

Die AMP Web-Push-Komponente erstellt ein Popup-Fenster für Push-Abonnements. Um dieses Feature zu aktivieren, müssen Sie die folgenden Hilfsdateien zu Ihrem Projekt hinzufügen:

- [`helper-iframe.html`](https://cdn.ampproject.org/v0/amp-web-push-helper-frame.html)
- [`permission-dialog.html`](https://cdn.ampproject.org/v0/amp-web-push-permission-dialog.html)

#### Schritt 4: Erstellen Sie eine Service-Teammitglied-Datei

Erstellen Sie eine Datei `service-worker.js` im Stammverzeichnis Ihrer Website und fügen Sie das folgende Snippet hinzu:

<script src="{{site.baseurl}}/assets/js/embed.js?target=https://github.com/braze-inc/braze-web-sdk/blob/master/sample-builds/cdn/service-worker.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

#### Schritt 5: Konfigurieren Sie das AMP Web-Push HTML-Element

Fügen Sie das folgende `amp-web-push` HTML-Element in Ihren HTML-Body ein. Denken Sie daran, dass Sie Ihre [`apiKey` und `baseUrl`](https://documenter.getpostman.com/view/4689407/SVYrsdsG) als Abfrageparameter an `service-worker-URL` anhängen müssen.

```js
<amp-web-push
layout="nodisplay"
id="amp-web-push"
helper-iframe-url="FILE_PATH_TO_YOUR_HELPER_IFRAME"
permission-dialog-url="FILE_PATH_TO_YOUR_PERMISSION_DIALOG"
service-worker-url="FILE_PATH_TO_YOUR_SERVICE_WORKER?apiKey={YOUR_API_KEY}&baseUrl={YOUR_BASE_URL}"
>
```
{% enddetails %}

### Definition asynchroner Module (AMD)

#### Unterstützung deaktivieren

Wenn Ihre Website RequireJS oder einen anderen AMD-Modul-Loader verwendet, Sie es aber vorziehen, das Braze Web SDK über eine der anderen Optionen in dieser Liste zu laden, können Sie eine Version der Bibliothek laden, die keine AMD-Unterstützung enthält. Diese Version der Bibliothek kann vom folgenden CDN-Standort geladen werden:

<script src="{{site.baseurl}}/assets/js/embed.js?target=https%3A%2F%2Fgithub.com%2Fbraze-inc%2Fbraze-web-sdk%2Fblob%2Fmaster%2Fsnippets%2Fno-amd-library.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

#### Modul-Lader

Wenn Sie RequireJS oder andere AMD-Modul-Loader verwenden, empfehlen wir Ihnen, selbst eine Kopie unserer Bibliothek zu hosten und genauso auf sie zu verweisen, wie Sie es mit anderen Ressourcen tun würden:

```javascript
require(['path/to/braze.min.js'], function(braze) {
  braze.initialize('YOUR-API-KEY-HERE', { baseUrl: 'YOUR-SDK-ENDPOINT' });
  braze.automaticallyShowInAppMessages();
  braze.openSession();
});
```

### Elektronen {#electron}

Offiziell unterstützt Electron keine Web-Push-Benachrichtigungen (siehe dieses [GitHub-Problem](https://github.com/electron/electron/issues/6697)). Es gibt andere [Open-Source-Umgehungen](https://github.com/MatthieuLemoine/electron-push-receiver), die Sie ausprobieren können, die aber nicht von Braze getestet wurden.

### Jest-Framework {#jest}

Bei der Verwendung von Jest wird möglicherweise eine Fehlermeldung ähnlich der von `SyntaxError: Unexpected token 'export'` angezeigt. Passen Sie für die Fehlerbehebung Ihre Konfiguration in `package.json` so an, dass das Braze SDK ignoriert wird:

```
"jest": {
  "transformIgnorePatterns": [
    "/node_modules/(?!@braze)"
  ]
}
```

### SSR-Rahmenwerke {#ssr}

Wenn Sie ein Server-Side Rendering (SSR)-Framework wie Next.js verwenden, kann es zu Fehlern kommen, da das SDK für die Ausführung in einer Browserumgebung gedacht ist. Sie können diese Probleme beheben, indem Sie das SDK dynamisch importieren.

Dabei können Sie weiterhin die Vorteile des Tree-Shaking nutzen, indem Sie die benötigten Teile des SDK in eine separate Datei exportieren, die Sie dann dynamisch in Ihre Komponente importieren.

```javascript
// MyComponent/braze-exports.js
// export the parts of the SDK you need here
export { initialize, openSession } from "@braze/web-sdk";

// MyComponent/MyComponent.js
// import the functions you need from the braze exports file
useEffect(() => {
    import("./braze-exports.js").then(({ initialize, openSession }) => {
        initialize("YOUR-API-KEY-HERE", {
            baseUrl: "YOUR-SDK-ENDPOINT",
            enableLogging: true,
        });
        openSession();
    });
}, []);
```

Wenn Sie Ihre App mit Webpack bündeln, können Sie alternativ die Magic Comments nutzen, um nur die benötigten Teile des SDK dynamisch zu importieren.

```javascript
// MyComponent.js
useEffect(() => {
    import(
        /* webpackExports: ["initialize", "openSession"] */
        "@braze/web-sdk"
    ).then(({ initialize, openSession }) => {
        initialize("YOUR-API-KEY-HERE", {
            baseUrl: "YOUR-SDK-ENDPOINT",
            enableLogging: true,
        });
        openSession();
    });
}, []);
```

### Tealium iQ

Tealium iQ bietet eine einfache, schlüsselfertige Braze-Integration. Um die Integration zu konfigurieren, suchen Sie in der Tealium Tag Management-Schnittstelle nach Braze und geben Sie den API-Schlüssel des Web SDK von Ihrem Dashboard an.

Für weitere Details oder ausführliche Unterstützung bei der Tealium-Konfiguration lesen Sie bitte unsere [Integrationsdokumentation]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/tealium/#about-tealium) oder wenden Sie sich an Ihren Tealium-Kundenbetreuer.

### Vite {#vite}

Wenn Sie Vite verwenden und eine Warnung zu zirkulären Abhängigkeiten oder `Uncaught TypeError: Class extends value undefined is not a constructor or null` sehen, müssen Sie das Braze SDK möglicherweise von der [Abhängigkeitsidentifizierung](https://vitejs.dev/guide/dep-pre-bundling.html#customizing-the-behavior) ausschließen:

```
optimizeDeps: {
    exclude: ['@braze/web-sdk']
},
```

### Andere Tag Manager

Braze kann auch mit anderen Tag Management-Lösungen kompatibel sein. Folgen Sie dazu unsere Integrationsanweisungen innerhalb eines angepassten HTML-Tags. Wenden Sie sich an eine Vertretung von Braze, wenn Sie Hilfe bei der Evaluierung dieser Lösungen benötigen.
