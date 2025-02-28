---
nav_title: Kopfzeilen der Sicherheitsrichtlinien für Inhalte
article_title: Inhaltssicherheitsrichtlinien-Kopfzeilen für das Web
platform: Web
page_order: 25
page_type: reference
description: "Dieser Artikel beschreibt die für das Braze Web SDK benötigten Header der Content-Security-Policy."

---

# Kopfzeilen der Sicherheitsrichtlinien für Inhalte

> Die Content-Security-Policy bietet zusätzliche Sicherheit, indem sie einschränkt, wie und wo Inhalte auf Ihrer Website geladen werden können. Dieser Referenzartikel beschreibt, welche Header der Content-Security-Policy beim Web SDK erforderlich sind.

{% alert important %}
Dieser Artikel richtet sich an Entwickler, die an Websites arbeiten, die CSP-Regeln durchsetzen und mit Braze integriert sind. Es ist nicht als Ratschlag gedacht, wie Sie die Sicherheit angehen sollten.
{% endalert %}

{% multi_lang_include archive/web-v4-rename.md %}

## Nonce-Attribute {#nonce}

Wenn Sie in den Direktiven `script-src` oder `style-src` den Wert `nonce` verwenden, übergeben Sie diesen Wert an die Initialisierungsoption `contentSecurityNonce`, damit er an neu erstellte Skripte und Stile weitergegeben, die vom SDK generiert werden:

```javascript
import * as braze from "@braze/web-sdk";

braze.initialize(apiKey, {
  baseUrl: baseUrl,
  contentSecurityNonce: "YOUR-NONCE-HERE", // assumes a "nonce-YOUR-NONCE-HERE" CSP value
});
```

## Direktiven {#directives}

### connect-src {#connect-src}

|URL|Informationen|
|---|-----------|
|`connect-src https://sdk.iad-01.braze.com`|Ermöglicht dem SDK die Kommunikation mit Braze-APIs. Ändern Sie diese URL so, dass sie dem [API SDK-Endpunkt]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/) für die von Ihnen gewählte `baseUrl` Initialisierungsoption entspricht.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### skript-src {#script-src}

|URL|Informationen|
|---|-----------|
|`script-src https://js.appboycdn.com`|Erforderlich, wenn Sie die im CDN gehostete Integration verwenden.|
|`script-src 'unsafe-eval'`|Erforderlich bei Verwendung des Integrations-Snippets, das einen Verweis auf `appboyQueue` enthält. Wenn Sie diese Direktive nicht verwenden möchten, [integrieren Sie das SDK stattdessen mit NPM]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/?tab=package%20manager).|
|`script-src 'nonce-...'`<br>oder<br>`script-src 'unsafe-inline'`|Erforderlich für bestimmte In-App-Nachrichten, wie z.B. benutzerdefiniertes HTML.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### img-src {#img-src}

|URL|Informationen|
|---|-----------|
|`img-src: appboy-images.com braze-images.com cdn.braze.eu`|Erforderlich bei der Verwendung von Bildern, die im CDN von Braze gehostet werden. Die Hostnamen können je nach Dashboard-Cluster variieren.<br><br>**Wichtig:** Wenn Sie angepasste Schriftarten verwenden, müssen Sie auch `font-src` einbeziehen.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Font Awesome {#font-awesome}

Um die automatische Einbindung von Font Awesome zu deaktivieren, verwenden Sie die Initialisierungsoption `doNotLoadFontAwesome`:

```javascript
import * as braze from "@braze/web-sdk";

braze.initialize(apiKey, {
  baseUrl: baseUrl,
  doNotLoadFontAwesome: true,
});
```

Wenn Sie Font Awesome verwenden möchten, sind die folgenden CSP-Direktiven erforderlich:

- `font-src https://use.fontawesome.com`
- `style-src https://use.fontawesome.com`
- `style-src 'nonce-...'` oder `style-src 'unsafe-inline'`
