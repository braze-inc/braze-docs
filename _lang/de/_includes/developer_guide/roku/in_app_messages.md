{% multi_lang_include developer_guide/prerequisites/roku.md %} Außerdem werden In-App-Nachrichten nur an Geräte gesendet, auf denen die minimal unterstützte SDK-Version läuft:

{% sdk_min_versions roku:0.1.2 %}

## Nachrichtentypen

{% tabs %}
{% multi_lang_include developer_guide/_shared/in_app_messages/message_types/android.md %}
{% multi_lang_include developer_guide/_shared/in_app_messages/message_types/swift.md %}
{% endtabs %}

## Aktivieren von In-App-Nachrichten

### Schritt 1: Einen Beobachter hinzufügen

Zum Verarbeiten von In-App-Nachrichten können Sie in `BrazeTask.BrazeInAppMessage` einen Beobachter hinzufügen:

```brightscript
m.BrazeTask.observeField("BrazeInAppMessage", "onInAppMessageReceived")
```

### Schritt 2: Zugriff auf getriggerte Nachrichten

Dann haben Sie innerhalb Ihres Handlers Zugriff auf die höchste In-App-Nachricht, die Ihre Kampagnen ausgelöst haben:

```brightscript
sub onInAppMessageReceived()
  in_app_message = m.BrazeTask.BrazeInAppMessage
  ...
end sub
```

## Felder für Nachrichten

### Handhabung

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

### Styling

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

### Buttons

| Felder | Beschreibung |
| ------ | ----------- |
| `click_action` | `"URI"` oder `"NONE"`. Verwenden Sie dieses Feld, um anzugeben, ob die In-App-Nachricht einen URI-Link öffnen oder die Nachricht schließen soll, wenn Sie darauf klicken. |
| `id` | ID-Wert des Buttons. |
| `text` | Der Text, der auf der Schaltfläche angezeigt werden soll. |
| `uri` | URI, an die die Nutzer basierend auf der `click_action` weitergeleitet werden. Dieses Feld muss enthalten sein, wenn `click_action` `"URI"` ist. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
