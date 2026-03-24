---
nav_title: Preferências de notificação
article_title: Preferências de notificação
page_order: 1
page_type: reference
description: "Este artigo de referência cobre suas opções disponíveis para monitorar o envio de mensagens e a atividade na conta da sua empresa."

---

# Preferências de notificação

> Se você gostaria de monitorar o envio de mensagens e a atividade na conta da sua empresa, pode optar por configurar notificações específicas e selecionar para onde elas vão.

A página **Preferências de Notificação** é onde você pode configurar quem (se alguém) recebe notificações sobre sua empresa. Você pode configurar quem deve receber notificações sobre a entrega de campanhas ou erros técnicos. Você também pode especificar destinatários para o relatório semanal de análise de dados. Para a maioria das notificações, a Braze suporta canais de e-mail e webhook.

![Página de Preferências de Notificação no dashboard da Braze]({% image_buster /assets/img_archive/notification_preferences.png %})

Para acessar esta página, acesse **Configurações** > **Configurações de Admin** > **Preferências de Notificação**.

{% alert tip %}
Você também pode integrar com o Slack para receber notificações. Para ver as etapas, consulte [Envio de mensagens usando webhooks de entrada](https://api.slack.com/incoming-webhooks).
{% endalert %}

## Notificações disponíveis

A tabela a seguir descreve as notificações disponíveis e quais canais são usados para entregá-las.

{% alert note %}
Se você excluir o valor padrão de **Destinatários** de **Todos os Usuários do Dashboard** e quiser adicioná-lo novamente, pode inseri-lo manualmente no campo suspenso.
{% endalert %}

| Notificação | Descrição | Canais de notificação disponíveis |
|--------------|-------------|-----------------|
| Alertas de uso da API | Selecionar esta opção leva você ao **Dashboard de Uso da API**, onde você pode acessar a guia [**Alertas de Uso da API**]({{site.baseurl}}/user_guide/analytics/dashboard/api_usage_alerts/) e configurar alertas para monitorar os volumes de solicitações de API mais importantes. | E-mail, Webhook |
| Erros de credenciais do AWS | Notifica os destinatários quando a Braze recebe um erro ao tentar usar suas credenciais do Amazon Web Services para uma exportação de dados. Isso inclui notificações de erros de credenciais para o Google Cloud Services e o Azure (Microsoft Cloud Services). | E-mail, Webhook |
| Campanha interrompida automaticamente | Notifica os destinatários quando a Braze interrompe uma campanha. | E-mail |
| Canvas interrompido automaticamente | Notifica os destinatários quando a Braze interrompe um Canvas. | E-mail |
| Expiração da interação da campanha | Notifica os destinatários sobre qualquer campanha que esteja prestes a expirar os dados de interação da campanha, juntamente com qualquer informação sobre segmentos, campanhas ou canvas que a referenciem em um filtro de redirecionamento e que foram usados para enviar uma mensagem nos últimos 30 dias. | E-mail |
| Campanha/Canvas atualizado | Notifica os destinatários quando uma campanha ou Canvas ativo é atualizado ou desativado, bem como quando uma campanha ou Canvas inativo é reativado ou rascunhos são lançados. | E-mail |
| Limite de volume de envios de campanha/Canvas atingido | Notifica os destinatários quando uma campanha ou Canvas atinge seu limite de volume de envios. | E-mail | 
| Expiração da interação do Canvas | Notifica os destinatários sobre qualquer Canvas que esteja prestes a expirar os dados de interação do Canvas, juntamente com qualquer informação sobre segmentos, campanhas ou canvas que o referenciem em um filtro de redirecionamento e que foram usados para enviar uma mensagem nos últimos 30 dias. | E-mail |
| Comentários em canvas | Notifica os destinatários quando um Canvas tem novos comentários. | E-mail |
| Erros de Conteúdo conectado | Notifica os destinatários quando um endpoint de Conteúdo conectado apresenta erros. | E-mail |
| Erros de push | Notifica os destinatários quando um endpoint de push apresenta erros. | E-mail, Webhook |
| Limite de campanha agendada atingido | Notifica os destinatários quando o limite de uma campanha agendada recorrente é atingido. | E-mail, Webhook |
| Campanha agendada concluiu os envios | Notifica os destinatários quando uma campanha agendada conclui os envios. | E-mail, Webhook |
| Erros de webhook | Notifica os destinatários quando um endpoint de webhook apresenta erros. | E-mail |
| Relatório semanal de análise de dados | Toda segunda-feira, envia para os destinatários um resumo das atividades da semana anterior no espaço de trabalho. Os destinatários recebem um resumo de todos os espaços de trabalho dos quais fazem parte. | E-mail |
| Limites de volume de envios diários de Canvas/campanha | Envia notificações sempre que um limite de envio é atingido. | E-mail |
| Erro no console de agentes | Notifica os destinatários quando um [agente do console de agentes]({{site.baseurl}}/user_guide/brazeai/agents) atingiu seu limite de execução com a funcionalidade atual. | E-mail |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert note %}
[Usuários suspensos]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/#suspending-company-users) ainda podem receber notificações da Braze.
{% endalert %}

## Relatório semanal de análise de dados

A Braze opcionalmente envia um relatório semanal via e-mail para as pessoas que você designar dentro da sua empresa toda segunda-feira às 5h EST. Você pode selecionar os eventos personalizados a serem incluídos no relatório semanal em **Configurações de Dados** > **Eventos Personalizados**.

Você pode selecionar até cinco eventos para serem incluídos no seu relatório semanal:

![Selecionando eventos para serem incluídos no relatório de análise de dados]({% image_buster /assets/img_archive/company_analytics_report_new.png %})