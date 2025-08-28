---
nav_title: Setembro
page_order: 4
noindex: true
page_type: update
description: "Este artigo contém notas de versão para setembro de 2019."
---

# Setembro de 2019

## App Braze no OneLogin

Os clientes poderão simplesmente pesquisar e selecionar o Braze no [OneLogin]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/onelogin/) para login iniciado por SP ou IdP. Isso significa que os clientes não precisarão adicionar um aplicativo personalizado no OneLogin. Como resultado, isso deve preencher previamente determinadas configurações, como atribuições que vimos surgir desde o lançamento do SAML SSO.

## Parceria com a Rokt Calendar

[O Rokt Calendar]({{site.baseurl}}/partners/home/) oferece aos clientes do Braze a capacidade de alinhar suas iniciativas de marketing personalizado e estender o conteúdo personalizado ao calendário do usuário final. Dessa forma, a experiência do usuário final é mais perfeita e desenvolve ainda mais a fidelidade aos serviços de nossos clientes. Os clientes poderão...

- Enviar um convite de calendário por meio da plataforma Braze para "salvar a data" e ampliar nossa comunicação
- Atualizar um convite existente se o conteúdo do evento tiver sido alterado.

## Parceria Passkit

Com o [Passkit]({{site.baseurl}}/partners/additional_channels_and_extensions/additional_channels/mobile_wallet/passkit/), os clientes da Braze poderão expandir seu engajamento com o cliente para a carteira móvel. Eles poderão personalizar as campanhas de carteira usando a poderosa segmentação do Braze e orquestrar junto com canais como push, mensagens no app e muito mais.

## Retorno do valor da ID de despacho por meio de endpoints de envio de mensagens

O endereço `dispatch_id` de uma mensagem será incluído nas seguintes respostas do ponto de extremidade de envio de mensagens:
- [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/#sending-messages-via-api-triggered-delivery)
- [`/campaigns/trigger/schedule`]({{site.baseurl}}/api/endpoints/messaging/#create-schedule-endpoint)
- [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/#sending-messages-immediately-via-api-only)
- [`/messages/schedule`]({{site.baseurl}}/api/endpoints/messaging/#create-schedule-endpoint)
- [`/canvases/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/#canvas)
- [`/canvases/trigger/schedule`]({{site.baseurl}}/api/endpoints/messaging/#api-triggered-canvases)

Dessa forma, os clientes que usam envio de mensagens transacionais podem rastrear a chamada de volta por meio do Currents.

## Changelogs dos canvas

Você já se perguntou mais sobre os detalhes de quem está trabalhando em um canva na sua conta? Não se pergunte mais! Agora você pode acessar os changelogs dos canvas.

![Changelogs dos canva]({% image_buster /assets/img/canvas-changelog1.png %})
![Changelogs dos canva]({% image_buster /assets/img/canvas-changelog2.png %})
