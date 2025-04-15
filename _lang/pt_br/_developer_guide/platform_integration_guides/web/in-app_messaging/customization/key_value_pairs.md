---
nav_title: Pares Chave-Valor
article_title: Pares de valores-chave de mensagens no app para a Web
platform: Web
channel: in-app messages
page_order: 9
page_type: reference
description: "Este artigo aborda como aproveitar os pares de valores-chave de mensagens no app para exibir informações para seu aplicativo da Internet."

---

# Pares chave-valor

> Este artigo aborda como aproveitar os pares de valores-chave de mensagens no app para exibir informações para seu aplicativo da Internet.

Os objetos de mensagem no app podem conter pares de valores-chave como sua propriedade `extras`. Elas são especificadas no dashboard em **Configurações** ao criar uma campanha de mensagens no app. Eles podem ser usados para enviar dados com uma mensagem no app para tratamento posterior pelo seu site. Por exemplo:

```javascript
import * as braze from "@braze/web-sdk";

braze.subscribeToInAppMessage(function(inAppMessage) {
  // control group messages should always be "shown"
  // this will log an impression and not show a visible message
  if (inAppMessage instanceof braze.ControlMessage) {
    return braze.showInAppMessage(inAppMessage);
  }


  if (inAppMessage instanceof braze.InAppMessage) {
    const extras = inAppMessage.extras;
    if (extras) {
      for (const key in extras) {
        console.log("key: " + key + ", value: " + extras[key]);
      }
    }
  }
  braze.showInAppMessage(inAppMessage);
});
```
