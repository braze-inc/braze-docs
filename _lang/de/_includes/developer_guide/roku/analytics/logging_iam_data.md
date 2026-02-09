{% multi_lang_include developer_guide/prerequisites/android.md %}

## Protokollierung von Nachrichten-Daten

Um die Analytics für Ihre Kampagne zu verarbeiten, müssen Sie sicherstellen, dass bestimmte Funktionen aufgerufen werden.

### Angezeigte Nachrichten

Wenn eine Nachricht angezeigt oder gesehen wird, protokollieren Sie eine Impression:

```brightscript
LogInAppMessageImpression(in_app_message.id, brazetask)
```

### Angeklickte Nachrichten

Sobald ein Nutzer auf die Nachricht klickt, protokollieren Sie einen Klick und verarbeiten dann `in_app_message.click_action`:

```brightscript
LogInAppMessageClick(in_app_message.id, brazetask)
```

### Angeklickte Buttons

Wenn der Nutzer auf einen Button klickt, protokollieren Sie den Button-Klick und verarbeiten dann `inappmessage.buttons[selected].click_action`:

```brightscript
LogInAppMessageButtonClick(inappmessage.id, inappmessage.buttons[selected].id, brazetask)
```

### Nach der Verarbeitung einer Nachricht

Nach der Verarbeitung einer In-App-Nachricht, sollten Sie das Feld löschen:

```brightscript
m.BrazeTask.BrazeInAppMessage = invalid
```
