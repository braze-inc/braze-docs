---
nav_title: Dispensa de modais
article_title: Dispensa de modais de mensagens no app para iOS
platform: iOS
page_order: 29
description: "Este artigo de referência aborda a dispensa do modal de envio de mensagens no app para o seu aplicativo iOS."
channel:
  - in-app messages
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Dispensa com toque fora do modal

O valor padrão é `NO`. Determina se o modal será descartado quando o usuário tocar fora da mensagem no app.

Para ativar as dispensas com toque fora do modal, adicione um dicionário chamado `Braze` ao seu arquivo `Info.plist`. No dicionário `Braze`, adicione a subentrada booleana `DismissModalOnOutsideTap` e defina o valor como `YES`, conforme mostrado no seguinte trecho de código. Note que, antes do SDK da Braze para iOS v4.0.2, a chave do dicionário `Appboy` deve ser usada no lugar de `Braze`.

```
<key>Braze</key>
<dict>
  <key>DismissModalOnOutsideTap</key>
  <boolean>YES</boolean>
</dict>
```

Você também pode ativar o recurso em tempo de execução, definindo `ABKEnableDismissModalOnOutsideTapKey` como `YES` em `appboyOptions`.

| `DismissModalOnOutsideTap` | Descrição |
|----------|-------------|
| `YES`       | Os modais de mensagens no app serão descartados com um toque externo.     |
| `NO`        | Por padrão, as mensagens modais no app não serão descartadas com um toque externo. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }