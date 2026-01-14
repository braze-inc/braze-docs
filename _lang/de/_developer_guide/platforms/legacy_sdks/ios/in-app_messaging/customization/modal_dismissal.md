---
nav_title: Ausblenden von Modalen
article_title: Modale Beendigung von In-App-Nachrichten für iOS
platform: iOS
page_order: 29
description: "Dieser Referenzartikel befasst sich mit der modalen Beendigung von In-App-Nachrichten für Ihre iOS-Anwendung."
channel:
  - in-app messages
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Modal durch Tippen außerhalb des Fensters ausblenden

Der Standardwert ist `NO`. Hierdurch wird festgelegt, ob die modale In-App-Nachricht ausgeblendet wird, wenn der Nutzer auf eine Stelle außerhalb der In-App-Nachricht tippt.

Wenn Sie Ausblendungen durch Tippen außerhalb des Fensters aktivieren möchten, fügen Sie ein Wörterbuch namens `Braze` zur Datei `Info.plist` hinzu. Fügen Sie im Wörterbuch `Braze` den booleschen Untereintrag `DismissModalOnOutsideTap` hinzu und setzen Sie den Wert auf `YES`. Siehe hierzu das folgende Code-Snippet. Beachten Sie, dass vor Braze iOS SDK v4.0.2 der Wörterbuchschlüssel `Appboy` anstelle von `Braze` verwendet werden muss.

```
<key>Braze</key>
<dict>
  <key>DismissModalOnOutsideTap</key>
  <boolean>YES</boolean>
</dict>
```

Sie können das Feature auch zur Laufzeit aktivieren, indem Sie `ABKEnableDismissModalOnOutsideTapKey` in `appboyOptions` auf `YES` setzen.

| `DismissModalOnOutsideTap` | Beschreibung |
|----------|-------------|
| `YES`       | Modale In-App-Nachrichten werden ausgeblendet, wenn auf eine Stelle außerhalb des Fensters getippt wird.     |
| `NO`        | Standardmäßig werden modale In-App-Nachrichten beim Tippen auf eine Stelle außerhalb des Fensters nicht ausgeblendet. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }