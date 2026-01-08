---
nav_title: Preferências de notificação
article_title: Preferências de Notificação
page_order: 1
page_type: reference
description: "Este artigo de referência cobre suas opções disponíveis para monitorar mensagens e atividades em sua conta da empresa."

---

# Preferências de notificação

> Se você gostaria de monitorar as mensagens e atividades em sua conta da empresa, pode escolher configurar notificações específicas e selecionar para onde elas vão.

A página **Preferências de Notificação** é onde você pode configurar quem (se alguém) recebe notificações sobre sua empresa. Você pode configurar quem deve receber notificações sobre a entrega de campanhas ou erros técnicos. Você também pode especificar destinatários para o relatório analítico semanal. Para a maioria das notificações, o Braze suporta canais de email e webhook.

\![Página de Preferências de Notificação no painel do Braze]({% image_buster /assets/img_archive/notification_preferences.png %})

Para acessar esta página, vá para **Configurações** > **Configurações do Administrador** > **Preferências de Notificação**.

## Notificações disponíveis

A tabela a seguir descreve as notificações disponíveis e quais canais são usados para entregá-las.

| Notificação | Descrição | Canais de notificação disponíveis |
|--------------|-------------|-----------------|
| Erros de Credenciais da AWS | Notifica os destinatários quando o Braze recebe um erro ao tentar usar suas credenciais da Amazon Web Services para uma exportação de dados. Isso inclui notificações de erro de credenciais para Google Cloud Services e Azure (Serviços de Nuvem da Microsoft). | Email, Webhook |
| Campanha Parada Automaticamente | Notifica os destinatários quando o Braze parou uma campanha. | Email |
| Expiração da Interação da Campanha | Notifica os destinatários sobre qualquer campanha que está prestes a expirar os dados de interação da campanha, juntamente com qualquer informação sobre segmentos, campanhas ou Canvases que a referenciam em um filtro de retargeting e foram usados para enviar uma mensagem nos últimos 30 dias. | Email |
| Campanha/Canvas Atualizado | Notifica os destinatários quando uma campanha ou Canvas ativa é atualizada ou desativada, assim como quando uma campanha ou Canvas inativa é reativada ou rascunhos são lançados. | Email |
| Limite de Volume da Campanha/Canvas Atingido | Notifica os destinatários quando uma campanha ou Canvas atinge seu limite de volume. | Email | 
| Expiração da Interação do Canvas | Notifica os destinatários sobre qualquer Canvas que está prestes a expirar os dados de interação do Canvas, juntamente com qualquer informação sobre segmentos, campanhas ou Canvases que a referenciam em um filtro de retargeting e foram usados para enviar uma mensagem nos últimos 30 dias. | Email |
| Erros de Credenciais de Push | Notifica os destinatários quando as credenciais de push de um aplicativo são inválidas e quando as credenciais de push de um aplicativo estão prestes a expirar. | Email, Webhook |
| Campanha Agendada Enviada/Não Enviada | Notifica os destinatários quando campanhas agendadas começam a ser enviadas ou quando campanhas agendadas tentam enviar, mas não têm usuários elegíveis para enviar. | Email, Webhook |
| Limite de Campanha Agendada Atingido | Notifica os destinatários quando o limite para uma campanha agendada recorrente foi atingido. | Email, Webhook |
| Campanha Agendada Terminou de Enviar | Notifica os destinatários quando uma campanha agendada terminou de enviar. | Email, Webhook |
| Relatório Semanal de Análise | Envia um resumo da atividade do espaço de trabalho da semana passada para os destinatários toda segunda-feira. Os destinatários recebem um resumo para cada espaço de trabalho ao qual pertencem. | Email |
| Limites diários de volume de Canvas/Campanha | Envia notificações sempre que um limite de envio é alcançado. | Email |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Relatório analítico semanal

A Braze envia opcionalmente um relatório semanal por e-mail para indivíduos que você designar dentro da sua empresa toda segunda-feira às 5 da manhã EST. Você pode selecionar os eventos personalizados a serem incluídos no relatório semanal em **Configurações de Dados** > **Eventos Personalizados**.

Você pode selecionar até cinco eventos para serem incluídos no seu relatório semanal:

\![Selecionando eventos a serem incluídos no Relatório de Análise]({% image_buster /assets/img_archive/company_analytics_report_new.png %})

## Integração de webhook de entrada do Slack

O Slack possui um [aplicativo de webhook de entrada](https://my.slack.com/services/new/incoming-webhook/) que permite que mensagens sejam postadas de fontes externas no Slack. Para começar, abra o aplicativo de webhook de entrada.

1. Selecione o canal do Slack para o qual você gostaria que as notificações fossem enviadas e clique em **Adicionar Integração de Webhooks de Entrada**.<br><br>
    \![Adicionar integração de webhooks de entrada no Slack]({% image_buster /assets/img_archive/slack_f.png %})<br><br>
  O Slack gerará uma URL que você precisará inserir na Braze para as notificações que deseja receber.<br><br>
2. Copie a **URL do Webhook**.<br><br>
    \![Copiar URL do webhook]({% image_buster /assets/img_archive/copy_url.png %})<br><br>
3. Navegue até a aba **Preferências de Notificação** em **Configurações da Empresa**.<br><br>
4. Selecione a notificação que você deseja ativar para o Slack. Ou, se você tiver várias notificações que deseja enviar para este canal do Slack, use **Adicionar em Massa** para adicionar o webhook a várias notificações.<br><br>
    \![Selecione as notificações do Slack para habilitar]({% image_buster /assets/img_archive/click_edit_f.png %}){: style="max-width:60%;"}<br><br>
5. Insira a URL que o Slack gerou para você.

É isso aí! Você deve começar a receber notificações sobre sua empresa neste canal do Slack. Você também pode conferir o artigo de ajuda do Slack sobre este tópico: [Enviando mensagens usando Webhooks de Entrada](https://api.slack.com/incoming-webhooks).

