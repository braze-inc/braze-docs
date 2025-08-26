---
nav_title: Mixpanel
article_title: Mixpanel
alias: /partners/mixpanel/
description: "Este artigo de referência descreve a parceria entre o Braze e a Mixpanel, uma plataforma de análise de dados, permitindo a importação de coortes da Mixpanel para o Braze para criar segmentos do Braze que podem ser usados para direcionamento de usuários em futuras campanhas ou canvas do Braze."
page_type: partner
search_tag: Partner
tool: Currents

---
 
# [![Curso do Braze Learning] ({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/mixpanel-integration-with-braze/339085/scorm/2u7y2e6qrldh2){: style="float:right;width:120px;border:0;" class="noimgborder"}Mixpanel

> O [Mixpanel](https://mixpanel.com/) é uma plataforma de análise de dados que permite exportar eventos do Mixpanel para realizar análises mais profundas em outras plataformas. Os dados coletados podem então ser usados para criar relatórios personalizados e medir o engajamento e a retenção de usuários.

A integração entre o Braze e o Mixpanel permite a [importação de coortes do Mixpanel para o Braze]({{site.baseurl}}/partners/data_and_analytics/analytics/mixpanel/mixpanel_cohort_import/) para criar segmentos do Braze que podem ser usados para direcionamento de usuários em futuras campanhas ou canvas do Braze. Você também pode aproveitar o Braze Currents para [exportar seus eventos do Braze para o Mixpanel](#data-export-integration), a fim de gerar análises de dados mais detalhadas sobre conversões, retenção e uso do produto. 

## Pré-requisitos

| Requisito | Descrição |
|---|---|
| Conta Mixpanel | É necessário ter uma [conta Mixpanel](https://mixpanel.com/) para usar a parceria. |
| Currents | Para exportar dados de volta para o Mixpanel, você precisa ter o [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) configurado em sua conta. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" } 

## Integração de exportação de dados

Encontre abaixo uma lista completa dos eventos que podem ser exportados da Braze para o Mixpanel. Todos os eventos enviados ao Mixpanel incluem o endereço `external_user_id` do usuário como Mixpanel Distinct ID. No momento, a Braze não envia dados de eventos de usuários sem `external_user_id` definido.

Você pode exportar dois tipos de eventos para o Mixpanel: [Eventos de engajamento com mensagens](#supported-currents-events), que consistem nos Eventos Braze diretamente relacionados ao envio de mensagens, e [Eventos de comportamento do cliente](#supported-currents-events), incluindo outras atividades do app ou do site, como sessões, eventos personalizados e compras rastreadas por meio da plataforma. Todos os eventos personalizados são prefixados com `[Braze Custom Event]`. As propriedades de eventos personalizados e as propriedades de eventos de compra são prefixadas com `[Custom event property]` e `[Purchase property]`, respectivamente.

Entre em contato com o gerente da sua conta ou abra um [ticket de suporte]({{site.baseurl}}/braze_support/) se precisar de acesso a direitos de eventos adicionais.

### Etapa 1: Obter credenciais do Mixpanel

No dashboard do Mixpanel, clique em **Project Settings** (Configurações do projeto) em um projeto novo ou existente. Aqui você encontra o segredo da API do Mixpanel e o token do Mixpanel. Essas credenciais serão usadas na próxima etapa para criar sua conexão com o Currents. 

### Etapa 2: criar Braze Currents

Na Braze, navegue até \*\*Currents > **\+ Criar Current** > **Criar exportação do Mixpanel**. Forneça um nome de integração, e-mail de contato, segredo da API do Mixpanel e token do Mixpanel nos campos listados. Em seguida, selecione os eventos que deseja rastrear; é fornecida uma lista dos eventos disponíveis. Por fim, clique em **Launch Current (Iniciar atual**).

![A página Braze Mixpanel Currents. Essa página inclui campos para nome da integração, e-mail do contato, segredo da API e token de exportação do Mixpanel. A metade inferior da página de Currents lista os eventos de Currents disponíveis que você pode enviar.]({% image_buster /assets/img_archive/mixpanel4.png %}){: style="max-width:80%;"}

{% tab nota %}
Consulte [os documentos de integração](https://help.mixpanel.com/hc/en-us/articles/360001243663) do Mixpanel para saber mais.
{% endtab %}

## Eventos Currents com suporte

O Braze suporta a exportação dos seguintes dados listados nos glossários de eventos de [comportamento do usuário]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/) e [engajamento com mensagem do]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) Currents para o Mixpanel:

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
  
