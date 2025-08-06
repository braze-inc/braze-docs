---
nav_title: mParticle para Currents
article_title: mParticle para Currents
alias: /partners/mparticle_for_currents/
description: "Esse artigo de referência descreve a parceria entre a Braze Currents e a mParticle, uma plataforma de dados do cliente que coleta e encaminha informações entre fontes em sua pilha de marketing."
page_type: partner
tool: Currents
search_tag: Partner

---

# mParticle para Currents

> [A mParticle](https://www.mparticle.com) é uma plataforma de dados do cliente que coleta e encaminha informações de várias fontes para uma variedade de outros locais em sua pilha de marketing.

A integração entre a Braze e o mParticle permite que você controle com praticidade o fluxo de informações entre os dois sistemas. Com [Currents]({{site.baseurl}}/user_guide/data/braze_currents/), você também pode conectar dados ao mParticle para torná-los acionáveis em todo o growth stack. 

## Pré-requisitos

| Requisito | Descrição |
| ----------- | ----------- |
| Currents | Para exportar dados de volta para o mParticle, você precisa ter o [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) configurado em sua conta. |
| Conta mParticle | É necessário ter uma [conta mParticle](https://app.mparticle.com/login) para usar essa parceria. |
| mParticle chave e segredo de servidor para servidor | Eles podem ser obtidos navegando até seu dashboard do mParticle e criando os [feeds necessários](#step-1-create-feeds) que permitem que o mParticle receba dados de interação do Braze para as plataformas iOS, Android e Web.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Sobre as credenciais do mParticle

mParticle tem credenciais em nível de app e em nível de espaço de trabalho que impactam como seus eventos são enviados.

- **Nível do App:** mParticle separará eventos por cada aplicativo individual, o que significa que as credenciais de nível de aplicativo que você fornece para seu aplicativo iOS só podem ser usadas para enviar eventos específicos do iOS.
- **Espaço de trabalho:** mParticle agrupa todos os eventos (que **não** são específicos do app), o que significa que as credenciais de nível de espaço de trabalho que você fornece ao seu grupo de app serão usadas para enviar todos os seus eventos não específicos do app.

Você pode pensar nisso como o mParticle ingerindo um "feed" com base em cada aplicativo individual. Por exemplo, se você tiver um app para iOS, um para Android e um para Web, seus eventos serão desconexos. Isso significa que, se você fornecer as mesmas credenciais para cada app, então um mParticle feed será usado para receber todos os dados de todos os seus apps, sem duplicação.

## Integração

### Etapa 1: Criar feeds

Na conta de administrador do mParticle, navegue até **Setup > Inputs** (Configuração > Entradas). Localize o **Braze** no **diretório** do mParticle e adicione a integração do feed.

A integração do feed da Braze suporta quatro feeds separados: iOS, Android, Web e Unbound. O feed não vinculado pode ser usado para eventos como e-mails que não estão conectados a uma plataforma. Você precisará criar uma entrada para cada feed da plataforma principal. Você pode criar entradas adicionais em **Setup > Inputs**, na guia **Feed Configurations (Configurações de feed** ).

![]({% image_buster /assets/img/braze-feed-inputs.png %})

Para cada feed, em **Agir como plataforma**, selecione a plataforma correspondente na lista. Se você não encontrar uma opção para selecionar um feed **act-as**, os dados serão tratados como não vinculados, mas ainda poderão ser encaminhados para as saídas do data warehouse.

![A primeira caixa de diálogo de integração, solicitando que você forneça um nome de configuração, determine um status de feed e selecione uma plataforma para atuar como.]({% image_buster /assets/img/braze-feed-act1.png %}){: style="max-width:40%;"}  ![A segunda caixa de diálogo de integração mostrando a chave de servidor para servidor e o segredo de servidor para servidor.]({% image_buster /assets/img/braze-feed-act2.png %}){: style="max-width:37%;"}

Ao criar cada entrada, o mParticle fornecerá uma chave e um segredo. Copie essas credenciais, certificando-se de notar para qual feed cada par de credenciais se destina.

### Etapa 2: criar Currents

Na Braze, navegue até **Currents > + Criar Currents > Exportação do mParticle**. Forneça um nome de integração, e-mail de contato e a chave de API do mParticle e a chave secreta do mParticle para cada plataforma. Em seguida, selecione os eventos que deseja rastrear; é fornecida uma lista dos eventos disponíveis. Por fim, clique em **Abrir Current**

![A página mParticle Currents no Braze. Aqui você encontra campos para o nome da integração, o e-mail do contato, a chave de API e a chave secreta.]({% image_buster /assets/img_archive/currents-mparticle-edit.png %})

{% alert important %}
É importante manter sua chave de API do mParticle e a chave secreta do mParticle atualizadas; se as credenciais do conector expirarem, o conector deixará de enviar eventos. Se isso persistir por mais de **48 horas**, os eventos do conector serão descartados e os dados serão perdidos permanentemente.
{% endalert %}

Todos os eventos enviados ao mParticle incluirão o endereço `external_user_id` do usuário como `customerid`. No momento, a Braze não envia dados de eventos de usuários sem `external_user_id` definido. Se quiser mapear o `external_user_id` para um ID diferente no mParticle que não seja o `customerid` padrão, entre em contato com o gerente de sucesso do cliente da Braze. 

## Eventos Currents com suporte

O Braze suporta a exportação dos seguintes dados listados nos glossários de eventos de [comportamento do usuário]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/) e de [engajamento com mensagem]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) do Currents para o mParticle:

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
- Mensagem no app (abortar, clicar, impressão)
  - `users.messages.inappmessage.Abort`
  - `users.messages.inappmessage.Click`
  - `users.messages.inappmessage.Impression`
- Notificações por push (abortar, bounce, abrir, enviar)
  - `users.messages.pushnotification.Abort`
  - `users.messages.pushnotification.Bounce`
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


Para saber mais sobre a integração do mParticle, visite a documentação [aqui](http://docs.mparticle.com/integrations/braze/feed).

