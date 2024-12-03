---
nav_title: Abrir link em uma nova guia
article_title: Abrir link de mensagem no app em nova guia para a Web
platform: Web
channel: in-app messages
page_order: 8
page_type: reference
description: "Este artigo aborda como definir os links de mensagens no app para abrir em uma nova guia para seu aplicativo da Internet."

---

# Abrir link em uma nova guia

> Este artigo aborda como definir os links de mensagens no app para abrir em uma nova guia para seu aplicativo da Internet.

Para configurar os links das mensagens no app para abrirem em uma nova guia, defina a opção `openInAppMessagesInNewTab` como `true` para forçar todos os links de cliques em mensagens no app a abrirem em uma nova guia ou janela.

```javascript
braze.initialize('api-key', { openInAppMessagesInNewTab: true} );
```
