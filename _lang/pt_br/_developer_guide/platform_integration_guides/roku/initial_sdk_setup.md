---
nav_title: Configuração inicial do SDK
article_title: Configuração inicial do SDK para Roku
platform: Roku
page_order: 0
page_type: reference
description: "Esta página descreve as etapas iniciais de configuração do SDK da Braze para Roku."
search_rank: 1
---

# integração inicial de SDK

> Este artigo de referência ensina como instalar o SDK da Braze para Roku. Instalar o SDK da Braze para Roku fornecerá a você funcionalidades básicas de análise de dados e segmentação.

{% alert tip %}
Confira nosso app de amostra para Roku no GitHub: [TorchieTV](https://github.com/braze-inc/braze-roku-sdk/tree/main/torchietv).
{% endalert %}

## Etapa 1: Adicionar arquivos

Os arquivos do SDK da Braze podem ser encontrados no diretório `sdk_files` no repositório [Braze Roku SDK](https://github.com/braze-inc/braze-roku-sdk).

1. Adicione `BrazeSDK.brs` ao seu app no diretório `source`.
2. Adicione `BrazeTask.brs` e `BrazeTask.xml` ao seu app no diretório `components`.

## Etapa 2: Adicionar referências

Adicione uma referência a `BrazeSDK.brs` em sua cena principal usando o seguinte elemento `script`:

```
<script type="text/brightscript" uri="pkg:/source/BrazeSDK.brs"/>
```

## Etapa 3: Configurar

Dentro de `main.brs`, defina a configuração da Braze no nó global:

```brightscript
globalNode = screen.getGlobalNode()
config = {}
config_fields = BrazeConstants().BRAZE_CONFIG_FIELDS
config[config_fields.API_KEY] = {YOUR_API_KEY}
' example endpoint: "https://sdk.iad-01.braze.com/"
config[config_fields.ENDPOINT] = {YOUR_ENDPOINT}
config[config_fields.HEARTBEAT_FREQ_IN_SECONDS] = 5
globalNode.addFields({brazeConfig: config})
```

Você pode encontrar seu [endpoint de SDK]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/) e chave de API no dashboard da Braze.

## Etapa 4: Inicializar Braze

Inicialize a instância Braze:

```brightscript
m.BrazeTask = createObject("roSGNode", "BrazeTask")
m.Braze = getBrazeInstance(m.BrazeTask)
```

## Ativar registro (opcional) {#logging}

Para depurar sua integração com a Braze, você pode visualizar o console de depuração do Roku para logs da Braze. Consulte [Depuração de código](https://developer.roku.com/docs/developer-program/debugging/debugging-channels.md) dos desenvolvedores do Roku para saber mais.

## Integração básica de SDK completa

A Braze já deve estar coletando dados do seu aplicativo com o SDK da Braze para Roku. 

Consulte os seguintes artigos sobre como [registrar atributos]({{site.baseurl}}/developer_guide/platform_integration_guides/roku/analytics/setting_custom_attributes/), [eventos]({{site.baseurl}}/developer_guide/platform_integration_guides/roku/analytics/logging_custom_events/) e [compras]({{site.baseurl}}/developer_guide/platform_integration_guides/roku/analytics/logging_purchases/) em nosso SDK.

Para saber mais sobre envio de mensagens no app no Roku, consulte nosso [guia de integração de mensagem no app]({{site.baseurl}}/developer_guide/platform_integration_guides/roku/in-app_messaging/overview/).


