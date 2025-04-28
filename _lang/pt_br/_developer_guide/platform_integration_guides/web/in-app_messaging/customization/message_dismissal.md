---
nav_title: Descarte de mensagem
article_title: Envio de mensagens no app para a web
platform: Web
channel: in-app messages
page_order: 2
page_type: reference
description: "Este artigo aborda o descarte de mensagens no app para seu aplicativo da Internet."

---

# Descarte de mensagem

> Este artigo aborda como lidar com a rejeição de mensagens no app para seu aplicativo da Internet.

Por padrão, quando uma mensagem no app estiver sendo exibida, pressionar o botão de escape ou clicar no fundo acinzentado da página descartará a mensagem. Configure a [opção de inicialização](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions) `requireExplicitInAppMessageDismissal` para `true` para evitar esse comportamento e exigir um clique explícito no botão para descartar as mensagens. 

```javascript
import * as braze from "@braze/web-sdk";
braze.initialize("YOUR-API-KEY", {
    baseUrl: "YOUR-API-ENDPOINT",
    requireExplicitInAppMessageDismissal: true
});
```

