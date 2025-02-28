---
nav_title: Integration
article_title: Anleitung zur Integration von In-App-Nachrichten für Roku
platform: Roku
page_order: 2
description: "Diese Referenzanleitung beschreibt, wie Sie In-App-Nachrichten für Roku integrieren. Zudem enthält sie wichtige Hinweise zur Code-Anpassung."
channel:
  - in-app messages
---

# Integration von In-App-Nachrichten

> Dieser Implementierungsleitfaden enthält Hinweise zur Code-Anpassung für In-App Nachrichten und begleitende Code-Snippets. Wir stellen Ihnen zwar einen Beispiel-Integrationscode zur Verfügung, aber Sie müssen eine Logik hinzufügen, um die ausgelösten Nachrichten in Ihrer gewünschten Benutzeroberfläche zu verarbeiten und anzuzeigen. 

Da der Code Ihrer App einzigartig ist, sind voraussichtlich nicht alle aufgeführten Schritte für Ihren Anwendungsfall relevant. Wenn Sie beispielsweise keine verzögerte Anzeige von In-App-Nachrichten verwenden, brauchen Sie die betreffende Logik nicht zu implementieren.

## SDK-Anforderungen {#supported-sdk-versions}

In-App-Nachrichten werden nur an Roku-Geräte mit der unterstützten SDK-Mindestversion gesendet:

{% sdk_min_versions roku:0.1.2 %}

## Einrichtung von In-App-Nachrichten

Zum Verarbeiten von In-App-Nachrichten können Sie in `BrazeTask.BrazeInAppMessage` einen Beobachter hinzufügen:

```brightscript
m.BrazeTask.observeField("BrazeInAppMessage", "onInAppMessageReceived")
```

Dann haben Sie innerhalb Ihres Handlers Zugriff auf die höchste In-App-Nachricht, die Ihre Kampagnen ausgelöst haben:

```brightscript
sub onInAppMessageReceived()
  in_app_message = m.BrazeTask.BrazeInAppMessage
  ...
end sub
```

## In-App-Nachrichtenfelder

Im Folgenden sind die Felder aufgeführt, die Sie für Ihre In-App-Nachrichten benötigen:

| Felder | Beschreibung |
| ------ | ----------- |
| `buttons` | Liste der Schaltflächen (kann eine leere Liste sein). |
| `click_action` | `"URI"` oder `"NONE"`. Verwenden Sie dieses Feld, um anzugeben, ob die In-App-Nachricht einen URI-Link öffnen oder die Nachricht schließen soll, wenn Sie darauf klicken. Wenn es keine Buttons gibt, sollte dies geschehen, wenn der Nutzer auf "OK" klickt, wenn die In-App-Nachricht angezeigt wird. |
| `dismiss_type` | `"AUTO_DISMISS"` oder `"SWIPE"`. Verwenden Sie dieses Feld, um anzugeben, ob Ihre In-App-Nachricht automatisch ausgeblendet werden soll oder eine Swipe-Geste zum Ausblenden erforderlich ist. |
| `display_delay` | Wartezeit (in Sekunden), bis die In-App-Nachricht angezeigt wird. |
| `duration` | Anzeigedauer der Nachricht (in Millisekunden), wenn `dismiss_type` auf `"AUTO_DISMISS"` festgelegt ist. |
| `extras` | Schlüssel-Werte-Paare. |
| `header` | Der Kopfzeilentext. |
| `id` | Die ID, die zum Protokollieren von Impressionen oder Klicks verwendet wird. |
| `image_url` | Bild-URL der In-App-Nachricht. |
| `message` | Text der Nachricht. |
| `uri` | URI, an die die Nutzer basierend auf der `click_action` weitergeleitet werden. Dieses Feld muss enthalten sein, wenn `click_action` `"URI"` ist. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Bei In-App-Nachrichten mit Buttons wird die `click_action` der Nachricht ebenfalls in die endgültige Nutzlast aufgenommen, wenn die Klickaktion vor dem Hinzufügen des Button-Textes hinzugefügt wird.
{% endalert %}

### Styling-Felder
Über das Dashboard können verschiedene Styling-Felder ausgewählt werden:

| Felder | Beschreibung |
| ------ | ----------- |
| `bg_color` | Hintergrundfarbe. |
| `close_button_color` | Farbe des Schließen-Buttons |
| `frame_color` | Farbe des Overlays für den Hintergrundbildschirm. |
| `header_text_color` | Textfarbe der Überschrift. |
| `message_text_color` | Farbe des Nachrichtentextes. |
| `text_align` | "START", "CENTER" oder "END". Ihre ausgewählte Textausrichtung. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Alternativ können Sie die In-App-Nachricht implementieren und sie innerhalb Ihrer Roku-Anwendung mit einer Standardpalette gestalten:

### Button-Felder

| Felder | Beschreibung |
| ------ | ----------- |
| `click_action` | `"URI"` oder `"NONE"`. Verwenden Sie dieses Feld, um anzugeben, ob die In-App-Nachricht einen URI-Link öffnen oder die Nachricht schließen soll, wenn Sie darauf klicken. |
| `id` | ID-Wert des Buttons. |
| `text` | Der Text, der auf der Schaltfläche angezeigt werden soll. |
| `uri` | URI, an die die Nutzer basierend auf der `click_action` weitergeleitet werden. Dieses Feld muss enthalten sein, wenn `click_action` `"URI"` ist. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Umgang mit Interaktionen

Um die Analytics für Ihre Kampagne zu verarbeiten, müssen Sie sicherstellen, dass bestimmte Funktionen aufgerufen werden.

##### Wenn eine Nachricht angezeigt wird

Wenn eine Nachricht angezeigt oder gesehen wird, protokollieren Sie eine Impression:
```brightscript
LogInAppMessageImpression(in_app_message.id, brazetask)
```

##### Wenn ein Benutzer auf eine Nachricht klickt
Sobald ein Nutzer auf die Nachricht klickt, protokollieren Sie einen Klick und verarbeiten dann `in_app_message.click_action`:
```brightscript
LogInAppMessageClick(in_app_message.id, brazetask)
```

##### Wenn ein Nutzer auf einen Button klickt
Wenn der Nutzer auf einen Button klickt, protokollieren Sie den Button-Klick und verarbeiten dann `inappmessage.buttons[selected].click_action`:

```brightscript
LogInAppMessageButtonClick(inappmessage.id, inappmessage.buttons[selected].id, brazetask)
```

##### Nach der Verarbeitung einer In-App-Nachricht
Nach der Verarbeitung einer In-App-Nachricht, sollten Sie das Feld löschen:
```brightscript
m.BrazeTask.BrazeInAppMessage = invalid
```
