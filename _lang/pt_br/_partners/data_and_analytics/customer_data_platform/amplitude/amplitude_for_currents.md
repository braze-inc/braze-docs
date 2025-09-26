---
nav_title: Amplitude para Currents
article_title: Amplitude para Currents
page_order: 0
description: "Este artigo de referência descreve a parceria entre o Braze Currents e a Amplitude, uma plataforma de análise de dados e business intelligence de produtos."
page_type: partner
tool: Currents
search_tag: Partner

---

# [![Curso do Braze Learning] ({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/amplitude-integration-with-braze){: style="float:right;width:120px;border:0;" class="noimgborder"}Amplitude para Currents

> A [Amplitude](https://amplitude.com/) é uma plataforma de análise de dados e business intelligence de produtos.

A integração bidirecional entre o Braze e o Amplitude permite [sincronizar suas coortes]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amplitude/amplitude_audiences/), características de usuários e eventos do Amplitude no Braze, bem como aproveitar o Braze Currents para exportar seus eventos do Braze para o Amplitude a fim de realizar análises mais profundas dos dados de seu produto e marketing.

## Pré-requisitos

| Requisito | Descrição |
|---|---|
| Conta de Amplitude | É necessário ter uma [conta da Amplitude](https://amplitude.com/) para usar essa parceria. |
| Currents | Para exportar dados de volta para o Amplitude, você precisa ter o [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) configurado em sua conta. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" } 

## Integração de exportação de dados

Uma lista completa dos eventos e das propriedades de eventos que podem ser exportados do Braze para o Amplitude pode ser encontrada nas seções a seguir. Todos os eventos enviados ao Amplitude incluirão o endereço `external_user_id` do usuário como ID de usuário do Amplitude. As propriedades de eventos específicos do Braze serão enviadas sob a chave `event_properties` nos dados enviados ao Amplitude.

{% alert important %}
Para usar esse recurso, sua ID de usuário do Amplitude deve corresponder à ID externa do Braze.
{% endalert %}

O Braze só enviará dados de eventos para usuários que tenham definido o endereço `external_user_id` ou para usuários anônimos que tenham definido o endereço `device_id`. Para os usuários anônimos, será necessário sincronizar o ID do dispositivo da Amplitude com o ID do dispositivo da Braze no SDK. Por exemplo:

```java
amplitude.setDeviceId(Appboy.getInstance(context).getDeviceId();)
```

Você pode exportar dois tipos de eventos para o Amplitude: [Eventos de engajamento com mensagens](#supported-currents-events), que consistem nos eventos Braze diretamente relacionados ao envio de mensagens, e [eventos de comportamento do cliente](#supported-currents-events), incluindo outras atividades do app ou do site, como sessões, eventos personalizados e compras rastreadas por meio da plataforma. Todos os eventos regulares são prefixados com `[Appboy]`, e todos os eventos personalizados são prefixados com `[Appboy] [Custom Event]`. As propriedades de eventos personalizados e de compra têm os prefixos `[Custom event property]` e `[Purchase property]`, respectivamente.

Todas as coortes nomeadas e importadas para a Braze terão o prefixo `[Amplitude]` e o sufixo `cohort_id`. Isso significa que uma coorte chamada "TEST_COHORT" com o endereço `cohort_id` "abcd1234" terá o título `[Amplitude] TEST_COHORT: abcd1234` nos filtros da Braze.

Entre em contato com o gerente da sua conta ou abra um [ticket de suporte]({{site.baseurl}}/braze_support/) se precisar de acesso a direitos de eventos adicionais.

### Etapa 1: Configurar a integração da Amplitude no Braze 

No Amplitude, localize sua chave de API de exportação do Amplitude.

{% alert warning %}
Mantenha sua chave de API do Amplitude atualizada. Se as credenciais do conector expirarem, ele deixará de enviar eventos. Se isso persistir por mais de **48 horas**, os eventos do conector serão descartados e os dados serão perdidos permanentemente.
{% endalert %}

### Etapa 2: criar um Braze Current

Na Braze, navegue até **Currents > + Criar Currents > Exportação do Amplitude**. Forneça um nome de integração, e-mail de contato, chave de API de exportação do Amplitude e região do Amplitude nos campos listados. Em seguida, selecione os eventos que deseja rastrear; é fornecida uma lista dos eventos disponíveis. Por fim, clique em **Abrir Current**.

{% alert note %}
Os eventos enviados do Braze Currents para o Amplitude contarão para sua cota de volume de eventos do Amplitude.
{% endalert %}

![A página Braze Amplitude Currents. Essa página inclui campos para nome de integração, e-mail de contato, chave de API e região dos EUA. A metade inferior da página de Currents lista os eventos de Currents disponíveis que você pode enviar.]({% image_buster /assets/img/amplitude4.png %})

{% tab nota %}
Consulte [os documentos de integração](https://amplitude.zendesk.com/hc/en-us/articles/115000217351-Appboy-Amplitude-Integration#how-to-set-up-and-use-the-integration) do Amplitude para saber mais.
{% endtab %}

## Limites de frequência

Os Currents se conectam à API HTTP do Amplitude, que tem um [limite de frequência](https://developers.amplitude.com/docs/http-api-v2#upload-limit) de 30 eventos/segundo por dispositivo e um limite não documentado de 500 mil eventos/dia por dispositivo. Se esses limites forem excedidos, o Amplitude limitará os eventos registrados pelo Currents. Se um dispositivo em sua integração exceder esse limite de frequência, poderá haver uma postergação quando os eventos de todos os dispositivos aparecerem no Amplitude.

Os dispositivos não devem relatar mais de 30 eventos/segundo ou 500 mil eventos/dia em circunstâncias normais, e esse padrão de evento só deve ocorrer caso a integração tenha sido mal configurada. Para evitar esse tipo de postergação, confirme se sua integração de SDK relata eventos a uma taxa normal, conforme especificado nas nossas instruções de integração de SDK, e evite executar testes automatizados que gerem muitos eventos para um único dispositivo.

## Eventos Currents com suporte

O Braze suporta a exportação dos seguintes dados listados nos glossários de eventos de [comportamento do usuário]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/) e [engajamento com mensagem do]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) Currents para o Amplitude:

### Comportamentos
- Evento personalizado: `users.behaviors.CustomEvent`
- Atribuição da instalação: `users.behaviors.InstallAttribution`
- Local: `users.behaviors.Location`
- Compra: `users.behaviors.Purchase`
- Desinstalação: `users.behaviors.Uninstall`
- App (primeira sessão, fim da sessão, início da sessão)
  - `users.behaviors.app.FirstSession`
  - `users.behaviors.app.SessionEnd`
  - `users.behaviors.app.SessionStart`
- Inscrição (mudança de estado global): `users.behaviors.subscription.GlobalStateChange`
- Grupo de inscrições (mudança de estado): `users.behaviors.subscriptiongroup.StateChange`
  
### Campanhas
- Abortar: `users_campaigns_abort`
- Conversão: `users.campaigns.Conversion`
- EnrollinControl: `users.campaigns.EnrollInControl`
  
### Canva
- Abortar: `users_canvas_abort`
- Conversão: `users.canvas.Conversion`
- Entrada: `users.canvas.Entry`
- Saída (público correspondente, evento realizado)
  - `users.canvas.exit.MatchedAudience`
  - `users.canvas.exit.PerformedEvent`
- Etapa do experimento (conversão, entrada dividida)
  - `users.canvas.experimentstep.Conversion`
  - `users.canvas.experimentstep.SplitEntry`

### Mensagens
- Cartão de conteúdo (abortar, clicar, descartar, impressão, enviar)
  - `users.messages.contentcard.Abort`
  - `users.messages.contentcard.Click`
  - `users.messages.contentcard.Dismiss`
  - `users.messages.contentcard.Impression`
  - `users.messages.contentcard.Send`
- E-mail (abortar, bounce, clicar, entrega, markasspam, abrir, enviar, softbounce, cancelar inscrição)
- Mensagem no app (abortar, clicar, impressão)
  - `users.messages.inappmessage.Abort`
  - `users.messages.inappmessage.Click`
  - `users.messages.inappmessage.Impression`
- Notificações por push (abortar, bounce, iOSforeground, abrir, enviar)
  - `users.messages.pushnotification.Abort`
  - `users.messages.pushnotification.Bounce`
  - `users.messages.pushnotification.IosForeground`
  - `users.messages.pushnotification.Open`
  - `users.messages.pushnotification.Send`
- SMS (abortar, envio da operadora, entrega, falha na entrega, recebimento de entrada, rejeição, envio, clique em link curto)
  - `users.messages.sms.Abort`
  - `users.messages.sms.Delivery`
  - `users.messages.sms.DeliveryFailure`
  - `users.messages.sms.InboundReceive`
  - `users.messages.sms.Rejection`
  - `users.messages.sms.Send`
  - `users.messages.sms.ShortLinkClick`
- Webhook (abortar, enviar)
  - `users.messages.webhook.Abort`
  - `users.messages.webhook.Send`
- WhatsApp (abortar, entrega, falha, recebimento de entrada, leitura, envio)
  - `users.messages.whatsapp.Abort`
  - `users.messages.whatsapp.Delivery`
  - `users.messages.whatsapp.Failure`
  - `users.messages.whatsapp.InboundReceive`
  - `users.messages.whatsapp.Read`
  - `users.messages.whatsapp.Send`
  
