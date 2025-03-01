---
nav_title: SDK-Ersteinrichtung
article_title: Ersteinrichtung für das Braze Web SDK
platform: Web
page_order: 0
page_type: reference
---

# Erste SDK-Einrichtung für das Web

> Dieser Referenzartikel beschreibt, wie Sie das Braze Web SDK installieren. Mit dem Braze Web SDK können Sie Analysen sammeln und Ihren Webbenutzern umfangreiche In-App-Nachrichten, Push-Nachrichten und Content Card-Nachrichten anzeigen. In unserer [](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html "JavaScript-DokumentationJSDocs") finden Sie eine vollständige technische Referenz.

{% multi_lang_include archive/web-v4-rename.md %}

## Schritt 1: Installieren Sie die Braze-Bibliothek

Sie können die Braze-Bibliothek mit einer der folgenden Methoden installieren. Wenn Ihre Website eine `Content-Security-Policy` verwendet, lesen Sie vor der Installation der Bibliothek unseren [Leitfaden zu den Sicherheitsrichtlinien für Inhalte]({{site.baseurl}}/developer_guide/platform_integration_guides/web/content_security_policy/).

{% alert important %}
Während die meisten Werbeblocker das Braze Web SDK nicht blockieren, sind einige restriktivere Werbeblocker dafür bekannt, dass sie Probleme verursachen.
{% endalert %}

{% tabs local %}
{% tab Paketmanager %}
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
{% endtab %}

{% tab Google Tag Manager %}
Das Braze Web SDK kann über die Template-Bibliothek von Google Tag Manager installiert werden. Es werden zwei Tags unterstützt:

1. Initialisierungs-Tag: Lädt das Web SDK auf Ihre Website und legt optional die externe Nutzer-ID fest.
2. Aktions-Tags: Zum Triggern angepasster Events, für Käufe, zum Ändern von Nutzer-IDs oder zum Umschalten des SDK-Trackings.

Weitere Informationen finden Sie in der [Anleitung zur Integration von Google Tag Manager]({{site.baseurl}}/developer_guide/platform_integration_guides/web/google_tag_manager/).
{% endtab %}

{% tab Braze CDN %}
Fügen Sie das Braze Web SDK direkt in den HTML-Code ein, indem Sie auf das auf unserem CDN gehostete Skript verweisen, das die Bibliothek asynchron lädt.

<script src="{{site.baseurl}}/assets/js/embed.js?target=https%3A%2F%2Fgithub.com%2Fbraze-inc%2Fbraze-web-sdk%2Fblob%2Fmaster%2Fsnippets%2Floading-snippet.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>
{% endtab %}
{% endtabs %}

## Schritt 2: Initialisieren Sie das SDK

Sobald das Braze Web SDK zu Ihrer Website hinzugefügt wurde, initialisieren Sie die Bibliothek mit dem API-Schlüssel und der [SDK-Endpunkt-URL]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints), die Sie unter **Einstellungen** > **App-Einstellungen** in Ihrem Braze Dashboard finden.

{% alert note %}
Wenn Sie die Braze-Initialisierungsoptionen in einem Tag Manager konfiguriert haben, können Sie diesen Schritt überspringen.
{% endalert %}

Eine vollständige Liste der Optionen für `braze.initialize()` sowie unsere anderen JavaScript-Methoden finden Sie in unserer [JavaScript-Dokumentation](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize).

```javascript
// initialize the SDK
braze.initialize('YOUR-API-KEY-HERE', {
    baseUrl: "YOUR-SDK-ENDPOINT-HERE"
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

## Schritt 3: Push-Benachrichtigungen einrichten (optional)

Um Push-Benachrichtigungen für das Braze Web SDK einzurichten, ist ein zusätzliches Setup erforderlich. Eine vollständige Übersicht finden Sie unter [Push-Benachrichtigungen für das Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/integration/).

## Protokollieren

Um die Protokollierung schnell zu aktivieren, können Sie `?brazeLogging=true` als Parameter in die URL Ihrer Website einfügen. Alternativ können Sie auch die [einfache](#basic-logging) oder [benutzerdefinierte](#custom-logging) Protokollierung aktivieren.

### Grundlegende Protokollierung

{% tabs local %}
{% tab vor der Initialisierung %}
Verwenden Sie `enableLogging`, um grundlegende Debugging-Meldungen in der JavaScript-Konsole zu protokollieren, bevor das SDK initialisiert wird.

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
Verwenden Sie `braze.toggleLogging()`, um grundlegende Debugging-Meldungen in der JavaScript-Konsole zu protokollieren, nachdem das SDK initialisiert wurde. Ihre Methode sollte in etwa so aussehen wie die folgende:

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
Die Basisprotokolle sind für alle Nutzer sichtbar. Daher sollten Sie diese Funktion deaktivieren oder zu [`setLogger`](#custom-logging) wechseln, bevor Sie Ihren Code für die Produktionsumgebung freigeben.
{% endalert %}

### Benutzerdefinierte Protokollierung

Verwenden Sie `setLogger`, um angepasste Debugging-Meldungen JavaScript-Konsole zu protokollieren. Im Gegensatz zu den Basisprotokollen sind diese Protokolle für die Benutzer nicht sichtbar.

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

## Alternative Integrationsmethoden

### Serverseitige Rendering-Frameworks {#ssr}

Wenn Sie ein serverseitiges Rendering-Framework wie Next.js verwenden, können Fehler auftreten, da das SDK für die Ausführung in einer Browserumgebung vorgesehen ist. Sie können diese Probleme beheben, indem Sie das SDK dynamisch importieren.

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

### Vite-Unterstützung {#vite}

Wenn Sie Vite verwenden und eine Warnung zu zirkulären Abhängigkeiten oder `Uncaught TypeError: Class extends value undefined is not a constructor or null` sehen, müssen Sie das Braze SDK möglicherweise von der [Abhängigkeitsidentifizierung](https://vitejs.dev/guide/dep-pre-bundling.html#customizing-the-behavior) ausschließen:

```
optimizeDeps: {
    exclude: ['@braze/web-sdk']
},
```

### Electron-Unterstützung {#electron}

Offiziell unterstützt Electron keine Web-Push-Benachrichtigungen (siehe dieses [GitHub-Problem](https://github.com/electron/electron/issues/6697)). Es gibt andere [Open-Source-Umgehungen](https://github.com/MatthieuLemoine/electron-push-receiver), die Sie ausprobieren können, die aber nicht von Braze getestet wurden.

### AMD-Modul-Lader

Wenn Sie RequireJS oder andere AMD-Modul-Loader verwenden, empfehlen wir Ihnen, selbst eine Kopie unserer Bibliothek zu hosten und genauso auf sie zu verweisen, wie Sie es mit anderen Ressourcen tun würden:

```javascript
require(['path/to/braze.min.js'], function(braze) {
  braze.initialize('YOUR-API-KEY-HERE', { baseUrl: 'YOUR-SDK-ENDPOINT' });
  braze.automaticallyShowInAppMessages();
  braze.openSession();
});
```
### Alternative Keine AMD-Installation

Wenn Ihre Website RequireJS oder einen anderen AMD-Modul-Loader verwendet, Sie es aber vorziehen, das Braze Web SDK über eine der anderen oben genannten Optionen zu laden, können Sie eine Version der Bibliothek laden, die keine AMD-Unterstützung enthält. Diese Version der Bibliothek kann vom folgenden CDN-Standort geladen werden:

<script src="{{site.baseurl}}/assets/js/embed.js?target=https%3A%2F%2Fgithub.com%2Fbraze-inc%2Fbraze-web-sdk%2Fblob%2Fmaster%2Fsnippets%2Fno-amd-library.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

### Tealium iQ
Tealium iQ bietet eine einfache, schlüsselfertige Braze-Integration. Um die Integration zu konfigurieren, suchen Sie in der Tealium Tag Management-Schnittstelle nach Braze und geben Sie den API-Schlüssel des Web SDK von Ihrem Dashboard an.

Für weitere Details oder ausführliche Unterstützung bei der Tealium-Konfiguration lesen Sie bitte unsere [Integrationsdokumentation]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/tealium/#about-tealium) oder wenden Sie sich an Ihren Tealium-Kundenbetreuer.

### Andere Tag Manager
Braze kann auch mit anderen Tag Management-Lösungen kompatibel sein. Folgen Sie dazu unsere Integrationsanweisungen innerhalb eines angepassten HTML-Tags. Wenden Sie sich an eine Vertretung von Braze, wenn Sie Hilfe bei der Evaluierung dieser Lösungen benötigen.

### Fehlerbehebung für das Jest-Framework {#jest}

Bei der Verwendung von Jest wird möglicherweise eine Fehlermeldung ähnlich der von `SyntaxError: Unexpected token 'export'` angezeigt. Passen Sie für die Fehlerbehebung Ihre Konfiguration in `package.json` so an, dass das Braze SDK ignoriert wird:

```
"jest": {
  "transformIgnorePatterns": [
    "/node_modules/(?!@braze)"
  ]
}
```
