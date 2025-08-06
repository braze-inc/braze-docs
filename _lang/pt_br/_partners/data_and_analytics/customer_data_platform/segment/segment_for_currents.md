---
nav_title: Segmento para Currents
article_title: Segmento para Currents
page_order: 2
alias: /partners/segment_for_currents/
description: "Este artigo de referência descreve a parceria entre o Braze Currents e a Segment, uma plataforma de dados do cliente que coleta e encaminha informações entre fontes em sua pilha de marketing."
page_type: partner
tool: Currents
search_tag: Partner

---

# Segmento para Currents  

> A [Segment](https://segment.com) é uma plataforma de dados do cliente que ajuda você a coletar, limpar e ativar os dados de seus clientes. Este artigo de referência fornecerá uma visão geral da conexão entre Braze Currents e Segment e descreverá os requisitos e processos para a implementação e o uso adequados.

A integração do Braze com o Segment permite que você utilize o Braze Currents para exportar seus eventos do Braze para o Segment, a fim de gerar análises de dados mais detalhadas sobre conversões, retenção e uso do produto. 

## Pré-requisitos

| Requisito | Descrição |
| ----------- | ----------- |
| Conta do segmento | É necessário ter uma [conta da Segment](https://app.segment.com/login) para aproveitar essa parceria. |
| Destino do Braze | Você já deve ter [configurado o Braze como um destino]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment/#connection-settings/) em sua integração com o Segment.<br><br>Isso inclui fornecer o data center correto da Braze e a chave da API REST nas suas [configurações de conexão]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment/#connection-settings). |
| Currents | Para exportar dados de volta para o Segment, você precisa ter o [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) configurado em sua conta. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integração

### Etapa 1: Obter a chave de gravação do segmento

No dashboard da Segment, selecione sua fonte da Segment. Em seguida, acesse **Settings > API keys** (Configurações > Chaves de API). Aqui você encontrará a **chave de gravação de segmento**.

{% alert warning %}
É importante manter sua chave de gravação de segmento atualizada. Se as credenciais do conector expirarem, ele deixará de enviar eventos. Se isso persistir por mais de **48 horas**, os eventos do conector serão descartados e os dados serão perdidos permanentemente.
{% endalert %}

### Etapa 2: Criar um novo conector Currents

1. Na Braze, navegue até **Integrações com parceiros** > **Exportação de dados**.
2. Clique em **\+ Criar nova integração com o Currents** > **Exportar dados do segmento**.
3. Em seguida, forneça nome de integração, e-mail de contato, chave de gravação do Segment e região do Segment.

![A página Segment Currents na Braze. Aqui, você pode encontrar campos para o nome da integração, o e-mail do contato, a região do segmento e a chave de API.]({% image_buster /assets/img/segment/segment_currents_integration_config.png %})

### Etapa 3: Exportar eventos de engajamento com mensagens

Em seguida, selecione os eventos de engajamento com mensagens que você gostaria de exportar. Consulte a tabela de eventos e propriedades de exportação listada a seguir. Todos os eventos enviados ao Segment incluirão o endereço `external_user_id` do usuário como `userId` e o endereço `braze_id` do usuário como `anonymousId`.

Lembre-se de que o Braze só envia dados de usuários sem um `external_user_id` se a opção **Include events from anonymous users (Incluir eventos de usuários anônimos** ) estiver marcada.

{% alert important %}
A exportação anônima de usuários está atualmente em acesso antecipado. Entre em contato com seu gerente de conta Braze se estiver interessado em participar desse acesso antecipado.
{% endalert %}

![Lista de todos os eventos de engajamento com mensagens disponíveis na página Segment Currents no Braze.]({% image_buster /assets/img/segment/segment_currents_data_config.png %})

Por fim, selecione **Abrir Current**.

{% alert warning %}
Se você pretende criar mais de um dos mesmos conectores Currents (por exemplo, dois conectores de eventos de engajamento com mensagens), eles devem estar em espaços de trabalho diferentes. Como a integração do Braze Segment Currents não pode isolar eventos de diferentes apps em um único espaço de trabalho, se isso não for feito, haverá desduplicação de dados desnecessários e perda de dados.
{% endalert %}

Para saber mais, visite a [documentação](https://segment.com/docs/connections/sources/catalog/cloud-apps/braze/) da Segment.

## Como atualizar seu Current

{% multi_lang_include updating_currents.md %}

## Eventos Currents com suporte

O Braze suporta a exportação dos seguintes dados listados nos glossários de eventos de [comportamento do usuário]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/) e [engajamento com mensagem]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) do Currents para o Segment:
 
### Comportamentos
- Desinstalação: `users.behaviors.Uninstall`
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
  - `users.messages.email.Abort`
  - `users.messages.email.Bounce`
  - `users.messages.email.Click`
  - `users.messages.email.Delivery`
  - `users.messages.email.MarkAsSpam`
  - `users.messages.email.Open`
  - `users.messages.email.Send`
  - `users.messages.email.SoftBounce`
  - `users.messages.email.Unsubscribe`
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

