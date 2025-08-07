---
nav_title: Link in neuer Registerkarte öffnen
article_title: In-App-Nachricht Link in neuem Tab für Internet öffnen
platform: Web
channel: in-app messages
page_order: 8
page_type: reference
description: "In diesem Artikel erfahren Sie, wie Sie Ihre In-App-Nachricht-Links so einstellen, dass sie in einem neuen Tab für Ihre Internet-Anwendung geöffnet werden."

---

# Link in neuem Tab öffnen

> In diesem Artikel erfahren Sie, wie Sie Ihre In-App-Nachricht-Links so einstellen, dass sie in einem neuen Tab für Ihre Internet-Anwendung geöffnet werden.

Um festzulegen, dass Ihre In-App-Nachricht-Links in einem neuen Tab geöffnet werden, setzen Sie die Option `openInAppMessagesInNewTab` auf `true`, um zu erzwingen, dass alle Links von In-App-Nachrichten-Klicks in einem neuen Tab oder Fenster geöffnet werden.

```javascript
braze.initialize('api-key', { openInAppMessagesInNewTab: true} );
```
