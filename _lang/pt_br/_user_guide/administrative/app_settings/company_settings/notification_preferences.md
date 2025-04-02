---
nav_title: Preferências de notificação
article_title: Preferências de notificação
page_order: 1
page_type: reference
description: "Este artigo de referência cobre suas opções disponíveis para monitorar o envio de mensagens e a atividade na conta da sua empresa."

---

# Preferências de notificação

> Se você gostaria de monitorar o envio de mensagens e a atividade na conta da sua empresa, pode optar por configurar notificações específicas e selecionar para onde elas vão.

A página **Preferências de Notificação** é onde você pode configurar quem (se alguém) recebe notificações sobre sua empresa. Você pode configurar quem deve receber notificações sobre a entrega da campanha ou erros técnicos. Você também pode especificar destinatários para o relatório semanal de análise de dados. Para a maioria das notificações, a Braze suporta canais de e-mail e webhook.

![Página de Preferências de Notificação no dashboard da Braze][61]

Para acessar esta página, acessar **Configurações** > **Configurações de Admin** > **Preferências de Notificação**.

{% alert note %}
Se você estiver usando a [navegação mais antiga]({{site.baseurl}}/navigation), selecione o menu suspenso da sua conta e acessar **Configurações da Empresa** > **Preferências de Notificação**.
{% endalert %}

## Notificações disponíveis

A tabela a seguir lista as notificações disponíveis:

| Notificação | Descrição | Canais de notificação disponíveis |
|--------------|-------------|-----------------|
| Erros de credenciais do AWS | Notifica os destinatários quando a Braze recebe um erro ao tentar usar suas credenciais do Amazon Web Services para uma exportação de dados. Isso inclui notificações de erros de credenciais para o Google Cloud Services e o Azure (Microsoft Cloud Services). | e-mail, Webhook |
| Campanha interrompida automaticamente | Notifica os destinatários quando a Braze interrompe uma campanha. | E-mail |
| Expiração da interação da campanha | Notifica os destinatários sobre qualquer campanha que esteja prestes a expirar os dados de interação da campanha, juntamente com qualquer informação sobre segmentos, campanhas ou canvas que a referenciem em um filtro de redirecionamento e que foram usados para enviar uma mensagem nos últimos 30 dias. | E-mail |
| Campanha/canva atualizado | Notifica os destinatários quando uma campanha ou Canvas ativo é atualizado ou desativado, bem como quando uma campanha ou Canvas inativo é reativado ou rascunhos são lançados. | E-mail |
| Limite de volume de envios de campanhas/canvas atingido | Notifica os destinatários quando uma campanha ou Canva atinge seu limite de volume de envios. | E-mail | 
| Expiração da interação do canva | Notifica os destinatários sobre qualquer canva que esteja prestes a expirar os dados de interação do canva, juntamente com qualquer informação sobre segmentos, campanhas ou canvas que o referenciem em um filtro de redirecionamento e que foram usados para enviar uma mensagem nos últimos 30 dias. | E-mail |
| Cartão do feed de notícias publicado/ativo | Notifica os destinatários quando os cards do feed de notícias são agendados ou publicados. | e-mail, Webhook |
| Erros de credenciais de push | Notifica os destinatários quando as credenciais de push de um app são inválidas e quando elas estão prestes a expirar. | e-mail, Webhook |
| Campanha agendada enviada/não enviada | Notifica os destinatários quando as campanhas programadas começam a ser enviadas ou quando as campanhas programadas tentam enviar, mas não têm usuários elegíveis para enviar. | e-mail, Webhook |
| Limite de campanha agendada atingido | Notifica os destinatários quando o limite de uma campanha agendada recorrente é atingido. | e-mail, Webhook |
| Campanha agendada concluiu os envios | Notifica os destinatários quando uma campanha agendada conclui os envios. | e-mail, Webhook |
| Relatório semanal de análise de dados | Toda segunda, envia para os destinatários um resumo das atividades da semana anterior ocorridas no espaço de trabalho. Os destinatários recebem um resumo de todos os espaços de trabalho dos quais fazem parte. | E-mail |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Relatório semanal de análise de dados

Braze opcionalmente envia um relatório semanal via e-mail para as pessoas que você designar dentro da sua empresa toda segunda-feira às 5h EST. Você pode selecionar os eventos personalizados a serem incluídos no relatório semanal em **Configurações de Dados** > **Eventos Personalizados**.

{% alert note %}
Se você estiver usando a [navegação mais antiga]({{site.baseurl}}/navigation), esta página está localizada em **Gerenciar Configurações** > **Eventos Personalizados**.
{% endalert %}

Você pode selecionar até FIVE eventos para serem incluídos em seu relatório semanal:

![Selecionando eventos para serem incluídos no relatório de análise de dados][22]

## Integração de webhook de entrada do Slack

Slack tem um [app de webhook de entrada][67] que permite que mensagens sejam postadas de fontes externas no Slack. Para começar, abra o app de webhook de entrada.

1. Selecione o canal do Slack que você gostaria que as notificações fossem Acessar e clique em **Adicionar integração de webhooks de entrada**.<br><br>
    ![Adicionar integração de webhooks de entrada no Slack][63]<br><br>
  O Slack gerará um URL que você precisará inserir na Braze para as notificações que deseja receber.<br><br>
2. Copie a **URL do Webhook**.<br><br>
    ![Copiar URL do webhook][64]<br><br>
3. Navegue até a guia **Preferências de notificação** em **Configurações da empresa**.<br><br>
4. Selecione a notificação que você deseja ativar para o Slack. Ou, se você tiver várias notificações que deseja enviar para este canal do Slack, use **Adicionar em Massa** para adicionar o webhook a várias notificações.<br><br>
    ![Selecione as notificações do Slack para ativar][65]{: style="max-width:60%;"}<br><br>
5. Digite a URL que o Slack gerou para você.

Pronto! Você deve começar a receber notificações sobre sua empresa nesse canal do Slack. Você também pode conferir o artigo de ajuda do Slack sobre este tópico: [Envio de mensagens com o Webhooks de entrada][62]].

[22]: {% image_buster /assets/img_archive/company_analytics_report_new.png %}
[63]: {% image_buster /assets/img_archive/slack_f.png %}
[64]: {% image_buster /assets/img_archive/copy_url.png %}
[65]: {% image_buster /assets/img_archive/click_edit_f.png %}
[67]: https://my.slack.com/services/new/incoming-webhook/
[61]: {% image_buster /assets/img_archive/notification_preferences.png %}
Daqui a [62]: https://api.slack.com/incoming-webhooks
