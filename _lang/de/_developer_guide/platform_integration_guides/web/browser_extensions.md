---
nav_title: Browser-Erweiterungen
article_title: Integration von Browser-Erweiterungen für das Internet
platform: Web
page_order: 20
page_type: reference
description: "Dieser Artikel beschreibt, wie Sie das Braze Web SDK innerhalb Ihrer Browser-Erweiterungen (Google Chrome, Firefox) verwenden können."

---

# Browser-Erweiterung

> Dieser Artikel beschreibt, wie Sie das Braze Web SDK innerhalb Ihrer Browser-Erweiterungen (Google Chrome, Firefox) verwenden können.

Integrieren Sie das Braze Web SDK in Ihre Browser-Erweiterung, um Analytics zu sammeln und Nutzern umfangreiche Nachrichten anzuzeigen. Dazu gehören sowohl **Google Chrome-Erweiterungen** als auch **Firefox-Add-Ons**.

## Was wird unterstützt

Da es sich bei den Erweiterungen um HTML und JavaScript handelt, können Sie Braze im Allgemeinen für Folgendes verwenden:

* **Analytics**: Erfassen Sie angepasste Events, Attribute und identifizieren Sie sogar wiederkehrende Nutzer innerhalb Ihrer Erweiterung. Nutzen Sie diese Profileigenschaften, um kanalübergreifendes Messaging zu betreiben.
* **In-App-Nachrichten**: Triggern Sie In-App-Nachrichten, wenn Nutzer innerhalb Ihrer Erweiterung eine Aktion ausführen, indem Sie unser natives oder angepasstes HTML Messaging verwenden.
* **Content-Cards**: Fügen Sie Ihrer Erweiterung einen Feed mit nativen Karten für Onboarding oder Aktionen hinzu.
* **Web-Push**: Senden Sie zeitnahe Benachrichtigungen, auch wenn Ihre Webseite gerade nicht geöffnet ist.

## Was nicht unterstützt wird

* Service-Teammitglieder werden vom Braze Web SDK nicht unterstützt, aber die entsprechende Funktion befindet sich in der Roadmap.

## Erweiterungstypen

Braze kann in den folgenden Bereichen Ihrer Erweiterung eingesetzt werden:

| Bereich | Details | Was wird unterstützt |
|--------|-------|------|
| Popup-Seite | Die [Popup-Seite](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/user_interface/Popups) ist ein Dialog, der Nutzern:innen angezeigt werden kann, wenn sie auf das Symbol Ihrer Erweiterung in der Browser-Symbolleiste klicken.| Analytics, In-App-Nachrichten und Content-Cards |
| Hintergrund-Skripte | [Hintergrundskripte](https://developer.chrome.com/extensions/background_pages) (nur Manifest v2) ermöglichen es Ihrer Erweiterung, die Nutzer:innen zu inspizieren und mit ihnen zu interagieren oder Webseiten zu verändern (z.B. wie Werbeblocker den Inhalt von Seiten erkennen und verändern). | Analytics, In-App-Nachrichten und Content-Cards.<br><br>Hintergrundskripte sind für Nutzer:innen nicht sichtbar. Für Messaging müssten Sie also mit Tabs des Browsers oder Ihrer Popup-Seite kommunizieren, wenn Sie Nachrichten anzeigen. |
| Optionen Seiten | Auf der [Optionsseite](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/user_interface/Options_pages) können Ihre Nutzer:innen die Einstellungen Ihrer Erweiterung umschalten. Es handelt sich um eine eigenständige HTML-Seite, die einen neuen Tab öffnet. | Analytics, In-App-Nachrichten und Content-Cards |
{: .reset-td-br-1 .reset-td-br-2, .reset-td-br-3 role="presentation" }

## Berechtigungen

Für die Integration des Braze SDK (`braze.min.js`) als lokale Datei, die mit Ihrer Erweiterung gebündelt ist, sind in Ihrem `manifest.json` keine zusätzlichen Berechtigungen erforderlich. 

Wenn Sie jedoch [Google Tag Manager]({{ site.baseurl }}/developer_guide/platform_integration_guides/web/google_tag_manager/), verwenden oder das Braze SDK von einer externen URL aus referenzieren oder eine strenge Richtlinie für die Sicherheit von Inhalten für Ihre Erweiterung festgelegt haben, müssen Sie die [`content_security_policy`](https://developer.chrome.com/extensions/contentSecurityPolicy) Einstellung in Ihrem `manifest.json` anpassen, um entfernte Skriptquellen zuzulassen.

## Erste Schritte

{% alert tip %}
Bevor Sie beginnen, sollten Sie den [Leitfaden zur SDK-Ersteinrichtung ]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/) für das Web SDK lesen, um mehr über unsere JavaScript-Integration im Allgemeinen zu erfahren.  <br><br>Vielleicht möchten Sie auch die [JavaScript SDK-Referenz](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html) referenzieren, um alle Einzelheiten zu den verschiedenen SDK-Methoden und Konfigurationsoptionen zu erfahren.
{% endalert %}

Um das Web SDK von Braze zu integrieren, müssen Sie zunächst eine Kopie der neuesten JavaScript Bibliothek herunterladen. Dazu können Sie NPM verwenden oder es direkt vom [CDN von Braze](https://js.appboycdn.com/web-sdk/latest/braze.min.js) herunterladen.

Wenn Sie es vorziehen, den [Google Tag Manager]({{ site.baseurl }}/developer_guide/platform_integration_guides/web/google_tag_manager/) zu verwenden oder eine extern gehostete Kopie des Braze SDK zu nutzen, sollten Sie bedenken, dass das Laden externer Ressourcen eine Anpassung Ihrer [`content_security_policy`](https://developer.chrome.com/extensions/contentSecurityPolicy) Einstellung in Ihrem `manifest.json` anpassen müssen.

Kopieren Sie die Datei `braze.min.js` nach dem Download in das Verzeichnis Ihrer Erweiterung.

### Erweiterungs-Popups {#popup}

Um Braze zu einem Erweiterungs-Popup hinzuzufügen, referenzieren Sie die lokale JavaScript-Datei in Ihrer `popup.html`, wie Sie es bei einer normalen Website tun würden. Wenn Sie Google Tag Manager verwenden, können Sie Braze stattdessen mit unseren [Google Tag Manager Templates]({{ site.baseurl }}/developer_guide/platform_integration_guides/web/google_tag_manager/) hinzufügen.

```html
<html>
    <title>popup.html</title>
    <!-- Add the Braze library -->
    <script src="/relative/path/to/braze.min.js"></script>
    <script>
    // Initialize Braze here
    </script>
</html>
```

### Hintergrundskript (nur Manifest v2) {#background-script}

Um Braze im Hintergrundskript Ihrer Erweiterung zu verwenden, fügen Sie die Bibliothek von Braze zu `manifest.json` im Array `background.scripts` hinzu. Dadurch wird die globale Variable `braze` im Kontext Ihres Hintergrundskripts verfügbar.


```json
{
    "manifest_version": 2,
    "background": {
        "scripts": [
            "relative/path/to/braze.min.js",
            "background.js"
        ],
    }
}
```

### Optionenseite {#options-page}

Wenn Sie eine Optionsseite verwenden (über die Manifest-Eigenschaften `options` oder `options_ui`), können Sie Braze genauso einbinden wie in der [Anleitung zu `popup.html`](#popup).

## Initialisierung

Sobald das SDK eingebunden ist, können Sie die Bibliothek wie gewohnt initialisieren. 

Da Cookies in Browser-Erweiterungen nicht unterstützt werden, können Sie Cookies deaktivieren, indem Sie mit `noCookies: true` initialisieren.

```javascript
braze.initialize("YOUR-API-KEY-HERE", {
    baseUrl: "YOUR-API-ENDPOINT",
    enableLogging: true,
    noCookies: true
});
```

Weitere Informationen zu den von uns unterstützten Initialisierungsoptionen finden Sie in der [Internet SDK Referenz](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize).

## Push

Popup-Dialoge für Erweiterungen sind nicht für Push-Eingaben zulässig (sie haben keine URL-Leiste in der Navigation). Um also die Push-Erlaubnis im Popup-Dialog einer Erweiterung zu registrieren und anzufragen, müssen Sie eine alternative Domain verwenden, wie beschrieben in [Alternative Push-Domain]({{ site.baseurl }}/developer_guide/platform_integration_guides/web/push_notifications/alternate_push_domain).

