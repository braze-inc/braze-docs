---
nav_title: Registro de impressões e cliques
article_title: Registro de impressões e cliques
platform: Web
channel: in-app messages
page_order: 3
page_type: reference
description: "Este artigo aborda o registro de impressões e cliques de mensagens no app para o seu aplicativo Web."

---

# Registro de impressões e cliques

> Este artigo aborda como registrar impressões e cliques de mensagens no app para o seu aplicativo da Web.

O registro de [impressões](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#loginappmessageimpression) e [cliques](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#loginappmessagebuttonclick) de mensagens no app é realizado automaticamente quando se usa o método `showInAppMessage` ou `automaticallyShowInAppMessage`.

Se não usar nenhum dos métodos e aceitar exibir a mensagem manualmente usando seu próprio código de interface do usuário, use os seguintes métodos para registrar análises de dados:

```javascript
// Registers that a user has viewed an in-app message with the Braze server.
braze.logInAppMessageImpression(inAppMessage);
// Registers that a user has clicked on the specified in-app message with the Braze server.
braze.logInAppMessageClick(inAppMessage);
// Registers that a user has clicked a specified in-app message button with the Braze server.
braze.logInAppMessageButtonClick(button, inAppMessage);
// Registers that a user has clicked on a link in an HTML in-app message with the Braze server.
braze.logInAppMessageHtmlClick(inAppMessage, buttonId?, url?)
```


