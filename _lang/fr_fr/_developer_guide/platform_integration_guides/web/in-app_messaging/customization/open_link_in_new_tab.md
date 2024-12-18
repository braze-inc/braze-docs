---
nav_title: Ouvrir le lien dans un nouvel onglet
article_title: Ouvrir le lien d’un message in-app dans un nouvel onglet pour le Web
platform: Web
channel: in-app messages
page_order: 8
page_type: reference
description: "Cet article explique comment configurer les liens de messages in-app pour qu’ils s’ouvrent dans un nouvel onglet de votre application Web."

---

# Ouvrir le lien dans un nouvel onglet

> Cet article explique comment configurer les liens de messages in-app pour qu’ils s’ouvrent dans un nouvel onglet de votre application Web.

Pour configurer les liens de messages in-app pour qu’ils s’ouvrent dans un nouvel onglet, définissez l’option `openInAppMessagesInNewTab` sur `true` pour forcer tous les liens du message in-app à s’ouvrir dans un nouvel onglet ou une nouvelle fenêtre.

```javascript
braze.initialize('api-key', { openInAppMessagesInNewTab: true} );
```
