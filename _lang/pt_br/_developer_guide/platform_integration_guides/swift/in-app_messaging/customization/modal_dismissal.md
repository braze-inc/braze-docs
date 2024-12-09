---
nav_title: Dispensa de modais
article_title: Dispensa do modal de mensagens no app para iOS
platform: Swift
page_order: 7
description: "Este artigo de referência aborda a dispensa do modal de envio de mensagens no app para o Swift SDK."
channel:
  - in-app messages
---

# Demissão modal

> Para ativar a dispensa por toques externos, você pode modificar a propriedade `dismissOnBackgroundTap` na estrutura `Attributes` do tipo de mensagem no app que deseja personalizar. 

Por exemplo, se quiser ativar esse recurso para mensagens no app com imagens modais, você pode configurar o seguinte:

{% tabs %}
{% tab swift %}

```swift
BrazeInAppMessageUI.ModalImageView.Attributes.defaults.dismissOnBackgroundTap = true
```

{% endtab %}
{% tab OBJECTIVE C %}

A personalização via `Attributes` não está disponível em Objective C.

{% endtab %}
{% endtabs %}

O valor padrão é `false`. Isso determina se o modal será descartado quando o usuário tocar fora da mensagem no app.

| `DismissModalOnOutsideTap` | Descrição |
|----------|-------------|
| `true`         | Os modais de mensagens no app serão descartados com um toque externo.     |
| `false`        | Por padrão, as mensagens modais no app não serão descartadas com um toque externo. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Para saber mais sobre a personalização de mensagens no app, consulte este [artigo](https://braze-inc.github.io/braze-swift-sdk/documentation/braze/in-app-message-customization).