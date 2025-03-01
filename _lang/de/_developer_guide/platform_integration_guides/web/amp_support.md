---
nav_title: AMP-Unterstützung
article_title: AMP-Unterstützung für das Internet
platform: Web
page_order: 5
page_type: reference
description: "Dieser Referenzartikel beschreibt die AMP-Unterstützung für Web und wie Sie Braze in eine AMP-Seite integrieren."

---

# AMP-Unterstützung

{% alert note %}
Dieser Abschnitt ist für die Integration nicht erforderlich, es sei denn, Sie versuchen, Braze in eine AMP-Seite zu integrieren.
{% endalert %}

> Dieser Referenzartikel beschreibt die AMP-Unterstützung für Web und wie Sie Braze in eine AMP-Seite integrieren. Accelerated Mobile Pages (AMP) ist ein von Google unterstütztes Projekt, das die Ladezeit von Seiten auf mobilen Geräten verbessern soll, indem es bestimmte Standards durchsetzt, darunter die Beschränkung der Verwendung von JavaScript.

Folglich kann das Braze SDK nicht auf eine AMP-Seite geladen werden. Das AMP-Projekt bietet jedoch eine Komponente, die Internet-Push unterstützt. Die [folgende Anleitung](https://www.ampproject.org/docs/reference/components/amp-web-push) beschreibt, wie Sie diese Komponente einrichten und referenziert die folgende Dokumentation zur Komponente `amp-web-push`.

## Schritt 1: AMP Web-Push-Skript einbinden

Fügen Sie den folgenden asynchronen Tag in Ihren Head ein:

```js
<script async custom-element="amp-web-push" src="https://cdn.ampproject.org/v0/amp-web-push-0.1.js"></script>
```

## Schritt 2: Abo und Abbestellungs-Widget hinzufügen

Sie müssen ein Widget hinzufügen, das es Nutzern:in erlaubt, sich bei Push an- und abzumelden. Diese sollte sich innerhalb des HTML-Bodys befinden und kann nach Ihren Vorstellungen gestaltet werden.

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

## Schritt 3: Hilfs-iFrame und Berechtigungsdialog herunterladen

Die AMP Web Push-Komponente erstellt ein Popup-Fenster, das das Push-Abonnement verwaltet. Daher müssen Sie einige Hilfsdateien in Ihr Projekt einbinden. Laden Sie die Datei [helper-iframe.html](https://cdn.ampproject.org/v0/amp-web-push-helper-frame.html) und die Datei [permission-dialog.html](https://cdn.ampproject.org/v0/amp-web-push-permission-dialog.html) herunter und speichern Sie sie auf Ihrer Website.

## Schritt 4: Erstellen Sie eine Service-Teammitglied-Datei

Erstellen Sie eine Datei `service-worker.js` mit folgendem Inhalt, und legen Sie sie im Stammverzeichnis Ihrer Website ab:

<script src="{{site.baseurl}}/assets/js/embed.js?target=https://github.com/braze-inc/braze-web-sdk/blob/master/sample-builds/cdn/service-worker.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

## Schritt 5: Konfigurieren Sie das AMP Web-Push HTML-Element

Jetzt müssen Sie das HTML-Element `amp-web-push` zu Ihrer Seite hinzufügen. Fügen Sie den folgenden HTML Code in den Textkörper Ihres Dokuments ein:

```js
<amp-web-push
layout="nodisplay"
id="amp-web-push"
helper-iframe-url="FILE_PATH_TO_YOUR_HELPER_IFRAME"
permission-dialog-url="FILE_PATH_TO_YOUR_PERMISSION_DIALOG"
service-worker-url="FILE_PATH_TO_YOUR_SERVICE_WORKER?apiKey={YOUR_API_KEY}&baseUrl={YOUR_BASE_URL}"
>
```

Insbesondere die `service-worker-URL` erfordert das Anhängen von `apiKey` und `baseUrl` (https://dev.appboy.com/api/v3) als Abfrageparameter.

Sie sollten nun für Push-Abos und -Abmeldungen auf Ihrer AMP-Seite konfiguriert sein.
