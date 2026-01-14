---
nav_title: Perfis de usuário
article_title: Perfis de usuário
page_order: 9
page_type: reference
tool: 
  - Dashboard
description: "Este artigo de referência descreve como acessar o perfil de um usuário no painel, casos de uso de perfis e o que cada perfil contém."

---

# Perfis de usuário

> Os perfis de usuário são uma ótima maneira de encontrar informações sobre usuários específicos. Todos os dados persistentes associados a um usuário são armazenados em seu perfil de usuário.

## Perfis de acesso

Para acessar o perfil de um usuário, vá para a página **Search Users (Pesquisar usuários** ) e pesquise um usuário por qualquer uma das seguintes opções:

- ID de usuário externo
- ID de brasagem
- E-mail
- Número de telefone
- Token de envio
- Alias de usuário com o formato "[user_alias]:[alias_name]",, como "amplitude_id:user_123"

Se for encontrada uma correspondência, você poderá visualizar as informações que registrou para esse usuário com o SDK do Braze. Caso contrário, se a sua pesquisa retornar vários perfis de usuário, você poderá mesclar cada perfil individualmente ou executar uma mesclagem de usuários em massa. Para obter um passo a passo completo, consulte [Usuários duplicados]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users/).

\![Resultados da pesquisa com um banner que diz "Vários usuários correspondem aos seus critérios de pesquisa" e dois botões denominados Anterior e Próximo.]({% image_buster /assets/img_archive/User_Search_Nonunique.png %}){: style="max-width:60%;"}

## Casos de uso

Os perfis de usuário são um ótimo recurso para solução de problemas e testes, pois você pode acessar facilmente informações sobre o histórico de envolvimento de um usuário, a associação ao segmento, o dispositivo e o sistema operacional.

Por exemplo, se um usuário relatar um problema e você não tiver certeza de qual dispositivo e sistema operacional ele está usando, poderá usar a [guia Overview (Visão geral](#overview-tab) ) para encontrar essas informações (desde que tenha o e-mail ou o ID do usuário). Também é possível visualizar o idioma de um usuário, o que pode ser útil se você estiver solucionando problemas de uma [campanha multilíngue]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/campaigns_in_multiple_languages/#campaigns-in-multiple-languages) que não se comportou como esperado.

Você pode usar a [guia Engagement (Envolvimento](#engagement-tab) ) para verificar se um determinado usuário recebeu uma campanha. Além disso, se esse usuário específico tiver recebido a campanha, você poderá ver quando ele a recebeu. Você também pode verificar se um usuário está em um determinado segmento e se ele optou por receber push, e-mail ou ambos. Essas informações são úteis para fins de solução de problemas. Por exemplo, você deve verificar essas informações se um usuário não receber uma campanha que você esperava que ele recebesse ou se receber uma campanha que você não esperava que ele recebesse.

## Elementos do perfil do usuário

Há quatro seções principais no perfil de um usuário.

- **Visão geral:** Informações básicas sobre o usuário, dados da sessão, atributos personalizados, eventos personalizados, compras e o dispositivo mais recente em que o usuário efetuou login.
- **Compromisso:** Informações sobre as configurações de contato do usuário, as campanhas recebidas, os segmentos, as estatísticas de comunicação, a atribuição de instalação e o número aleatório do bucket.
- **Histórico de mensagens:** Eventos recentes relacionados a mensagens para esse usuário nos últimos 30 dias.
- **Elegibilidade dos sinalizadores de recursos:** Valide para quais sinalizadores de recursos um usuário está qualificado no momento em implementações, etapas de tela e experimentos. 

### Guia Visão geral {#overview-tab}

A guia **Visão geral** contém informações básicas sobre um usuário e suas interações com seu aplicativo ou site.

| Categoria de visão geral | Contém |
| --- | --- |
| Perfil | Gênero, faixa etária, local, idioma, localidade, fuso horário e aniversário. |
| Visão geral das sessões | Quantas sessões eles tiveram, quando foram as primeiras e as últimas sessões e em quais aplicativos. |
| Atributos personalizados | Quais atributos personalizados são atribuídos a esse usuário e seu valor associado, incluindo atributos personalizados aninhados. |
| Dispositivos recentes | Em quantos dispositivos eles fizeram login, detalhes de cada dispositivo e suas IDs de publicidade associadas (se houver). |
| Eventos personalizados | Quais eventos personalizados foram realizados por esse usuário, quantas vezes e quando foi a última vez que ele realizou cada evento. |
| Compras | Receita vitalícia atribuída a esse usuário, sua última compra, número total de compras e uma lista de cada compra. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Para obter mais informações sobre esses dados, consulte [Coleta de dados do usuário]({{site.baseurl}}/user_guide/data/user_data_collection/).

\![A guia Visão geral de um perfil de usuário.]({% image_buster /assets/img_archive/user_profile2.png %})

### Guia Engajamento {#engagement-tab}

A guia **Envolvimento** contém informações sobre as interações de um usuário com as mensagens que você enviou a ele usando o Braze.

| Categoria de engajamento | Contém |
| --- | --- |
| Configurações de contato | Status da assinatura para e-mail, SMS e push, e os grupos de assinatura aos quais esse usuário está associado para esses três canais. Esta seção também inclui informações de changelog para tokens push. Consulte [e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/), [SMS]({{site.baseurl}}/sms_rcs_subscription_groups/) e [push]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions/) para obter informações sobre como as assinaturas e os opt-ins são definidos. |
| Campanhas recebidas | As campanhas recebidas são marcadas quando o usuário recebe a campanha ou quando detectamos pela primeira vez dados de interação para um usuário. Selecione uma campanha na lista para visualizá-la. |
| Segmentos | Segmentos em que esse usuário está incluído. Selecione um segmento da lista para visualizá-lo. |
| Estatísticas de comunicação | Quando esse usuário recebeu as últimas mensagens suas de cada canal. |
| Atribuição de instalação | Informações sobre como e quando um usuário instalou seu aplicativo. Saiba mais sobre [como entender as instalações do usuário]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/install_attribution/). |
| Diversos | O [número aleatório]({{site.baseurl}}/user_guide/engagement_tools/testing/random_bucket_numbers/) do [balde]({{site.baseurl}}/user_guide/engagement_tools/testing/random_bucket_numbers/) do usuário. |
| Mensagens de tela recebidas | Mensagens do Canvas que esse usuário recebeu e quando. Selecione uma mensagem da lista para visualizá-la. |
| Previsões | Pontuações [de previsão de churn]({{site.baseurl}}/user_guide/brazeai/predictive_churn/) e [previsão de eventos]({{site.baseurl}}/user_guide/brazeai/predictive_events/) para esse usuário. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

A guia Engajamento de um perfil de usuário que exibe suas configurações de contato e estatísticas de comunicação.]({% image_buster /assets/img_archive/profiles_engagement_tab.png %})

### Guia Histórico de mensagens

A guia **Histórico de mensagens** do perfil do usuário mostra eventos recentes relacionados a mensagens (cerca de 40) para um usuário individual nos últimos 30 dias. Esses eventos incluem as mensagens que o usuário enviou, recebeu, com as quais interagiu e muito mais. Observe que os dados dessa guia não são atualizados depois que um usuário é mesclado.

{% alert note %}
Se você tiver comentários sobre essa tabela ou quiser ver eventos específicos, envie um e-mail para [user-targeting@braze.com](mailto:user-targeting@braze.com?subject=Messaging%20History%20Tab%20Feedback) com a linha de assunto "Messaging History Tab Feedback".
{% endalert %}

A guia Messaging History (Histórico de mensagens) mostra quais campanhas e Canvases um usuário recebeu.]({% image_buster /assets/img_archive/profiles_messaging_history_tab.png %})

#### Visualização e compreensão de eventos

Para cada evento na tabela **Histórico de mensagens**, é possível ver o canal de mensagens, o tipo de evento, o registro de data e hora em que o evento ocorreu, a campanha associada ou a mensagem do Canvas e os dados do dispositivo do usuário. Para filtrar eventos específicos, clique em **Filters (Filtros** ) e selecione os eventos na lista.

##### Eventos de engajamento de mensagens

Os seguintes eventos de engajamento de mensagens estão disponíveis para e-mail, SMS, push, mensagens no aplicativo, Content Cards e webhooks. Para saber mais sobre como eventos específicos são rastreados, consulte o [glossário de eventos de engajamento de mensagens]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/).

| Canal | Eventos de engajamento disponíveis |
| --- | --- |
| E-mail | Salto<br>Clique em<br>Eventos de diferimento<br>Entrega<br>Marcar como spam<br>Aberto (consulte [a nota sobre o evento aberto por e-mail](#note-on-email-open-event))<br>Enviar<br>Salto suave<br>Cancelar inscrição |
| SMS | Envio da operadora<br>Entrega<br>Falha na entrega<br>Recebimento de entrada<br>Rejeição<br>Enviar |
| Empurrar | Salto<br>Influenciado aberto<br>Primeiro plano do iOS<br>Aberto<br>Enviar |
| Mensagem no aplicativo | Clique em<br>Impressão |
| Cartões de conteúdo | Clique em<br>Dispensar<br>Impressão<br>Enviar |
| Webhooks | Enviar |
| WhatsApp | Abortar<br>Entrega<br>Falha<br>Frequência limitada<br>Recebimento de entrada<br>Ler<br>Enviar |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

##### Eventos de interrupção de mensagens

Os eventos de abortamento de mensagem ocorrem quando uma mensagem enviada a um usuário foi abortada devido à lógica condicional no [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/) ou no [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/aborting_connected_content#aborting-messages), ou devido a tempos limite de renderização do Liquid.

Os eventos de interrupção estão disponíveis para os seguintes canais:

- E-mail
- SMS
- Empurrar
- Webhooks

No momento, os eventos de abortar não estão disponíveis para mensagens in-app e Content Cards.

##### Eventos de limite de frequência

Um evento de limite de frequência ocorre quando um usuário está qualificado para receber uma mensagem, mas não a recebe de fato devido às configurações [de limite de frequência]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping). Você pode personalizar as configurações de limitação de frequência em **Settings** > **Frequency Capping Rules**.

##### Destinos em branco

Alguns envios de mensagens podem aparecer no Histórico de mensagens com destinos em branco (indicados por "-"). Isso ocorre porque alguns canais, como Content Cards e webhooks, não coletam dados do dispositivo no envio da mensagem.

Os envios de cartões de conteúdo são registrados quando o cartão está disponível para ser visualizado. Como os Content Cards podem ser visualizados em vários dispositivos, os dados do dispositivo não são registrados para um envio. Em vez disso, essas informações são registradas na impressão (quando o cartão é realmente visualizado). Os webhooks são enviados a um endpoint do sistema (não a um dispositivo), portanto, os dados do dispositivo não são aplicáveis.

#### Observação sobre o evento aberto por e-mail {#note-on-email-open-event}

O rastreamento de abertura de e-mails é propenso a erros em qualquer ferramenta, inclusive no Braze. Com uma variedade de recursos de proteção de privacidade oferecidos por diferentes clientes de e-mail que bloqueiam o carregamento automático de imagens ou as carregam proativamente no servidor, os eventos de abertura de e-mail são suscetíveis a falsos positivos e falsos negativos.

Embora as estatísticas de abertura de e-mail possam ser úteis em conjunto, por exemplo, para comparar a eficácia de diferentes linhas de assunto, não se deve presumir que um evento de abertura individual para um usuário individual seja significativo.

#### Por que alguns campos estão em branco na guia Histórico de mensagens?

Alguns campos podem estar ausentes na guia **Histórico de mensagens** de um usuário nos seguintes cenários:

- Quando um evento não tem dados para **Mensagem enviada**, isso indica que a campanha não tem nenhuma variação de mensagem.
- Quando um evento está sem dados para **Campaign/Canvas** e **Message Sent**, isso indica que essa mensagem foi enviada de uma campanha de API (não de campanhas acionadas por API) que não especificou os endereços `campaign_id` e `message_variation_id`. Esses campos são opcionais e podem ser deixados de fora do corpo da solicitação. Quando esses campos são especificados, essas informações são preenchidas nos registros do histórico de mensagens.
   - Se uma determinada mensagem estiver totalmente ausente do histórico de mensagens, mas aparecer no registro **Campanhas recebidas**, é provável que o usuário tenha recebido a campanha antes de ser identificado como o usuário atual. Se um perfil existente for órfão, o registro **Campaigns Received (Campanhas recebidas** ) será transferido, mas o histórico de mensagens não. 
- Quando faltam dados para **Campaign/Canvas**, pode ter sido enviado um teste manual. Os testes manuais são registrados na guia **Histórico de mensagens**, mas a campanha ou o Canvas que foi enviado não será registrado.


