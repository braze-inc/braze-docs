---
nav_title: Changelogs de Eventos Currents
page_order: 6
description: "Esta página inclui as mudanças de eventos para cada lançamento do Currents."
tool: Currents
---

# changelog do Currents

## Mudanças na Versão 6 (data de lançamento 2026-03-04)

### Mudanças para armazenamento

* Mudanças de campo para o tipo de evento `agentconsole.AgentExecuted`:
    * Campo `string` adicionado `error`: Descrição do erro

* Mudanças de campo para o tipo de evento `agentconsole.ToolInvocation`:
    * Campo `string` adicionado `request_id`: id único para esta solicitação geral de LLM e execução completa

* Mudanças de campo para o tipo de evento `users.messages.rcs.InboundReceive`:
    * Campo `string` adicionado `canvas_variation_name`: Nome da variante do canva recebida por este usuário

### Mudanças para compartilhamento de dados

* Mudanças de campo para o tipo de evento `agentconsole.AgentExecuted`:
    * Campo `string` adicionado `canvas_name`: Nome do Canvas
    * Campo `string` adicionado `canvas_variation_name`: Nome da variante do canva recebida por este usuário
    * Campo `string` adicionado `canvas_step_name`: Nome da etapa do Canvas
    * Campo `string` adicionado `error`: Nome do erro

* Mudanças de campo para o tipo de evento `agentconsole.ToolInvocation`:
    * Campo `string` adicionado `request_id`: id único para esta solicitação geral de LLM e execução completa

* Mudanças de campo para o tipo de evento `users.behaviors.subscription.GlobalStateChange`:
    * Campo `string` adicionado `campaign_name`: Nome da campanha
    * Campo `string` adicionado `message_variation_name`: Nome da variação da mensagem
    * Campo `string` adicionado `canvas_name`: Nome do Canvas
    * Campo `string` adicionado `canvas_variation_name`: Nome da variante do canva recebida por este usuário
    * Campo `string` adicionado `canvas_step_name`: Nome da etapa do Canvas

* Mudanças de campo para o tipo de evento `users.behaviors.subscriptiongroup.StateChange`:
    * Campo `string` adicionado `campaign_name`: Nome da campanha
    * Campo `string` adicionado `message_variation_name`: Nome da variação da mensagem
    * Campo `string` adicionado `canvas_name`: Nome do Canvas
    * Campo `string` adicionado `canvas_variation_name`: Nome da variante do canva recebida por este usuário
    * Campo `string` adicionado `canvas_step_name`: Nome da etapa do Canvas

* Mudanças de campo para o tipo de evento `users.campaigns.Conversion`:
    * Campo `string` adicionado `campaign_name`: Nome da campanha
    * Campo `string` adicionado `message_variation_name`: Nome da variação da mensagem
    * Campo `string` adicionado `conversion_behavior`: String codificada em JSON descrevendo o comportamento de conversão

* Mudanças de campo para o tipo de evento `users.campaigns.EnrollInControl`:
    * Campo `string` adicionado `campaign_name`: Nome da campanha
    * Campo `string` adicionado `message_variation_name`: Nome da variação da mensagem

* Mudanças de campo para o tipo de evento `users.canvas.Conversion`:
    * Campo `string` adicionado `canvas_name`: Nome do Canvas
    * Campo `string` adicionado `canvas_variation_name`: Nome da variante do canva recebida por este usuário
    * Campo `string` adicionado `canvas_step_name`: Nome da etapa do Canvas
    * Campo `string` adicionado `conversion_behavior`: String codificada em JSON descrevendo o comportamento de conversão

* Mudanças de campo para o tipo de evento `users.canvas.Entry`:
    * Campo `string` adicionado `canvas_name`: Nome do Canvas
    * Campo `string` adicionado `canvas_variation_name`: Nome da variante do canva recebida por este usuário
    * Campo `string` adicionado `canvas_step_name`: Nome da etapa do Canvas

* Mudanças de campo para o tipo de evento `users.canvas.exit.MatchedAudience`:
    * Campo `string` adicionado `canvas_name`: Nome do Canvas
    * Campo `string` adicionado `canvas_variation_name`: Nome da variante do canva recebida por este usuário
    * Campo `string` adicionado `canvas_step_name`: Nome da etapa do Canvas

* Mudanças de campo para o tipo de evento `users.canvas.exit.PerformedEvent`:
    * Campo `string` adicionado `canvas_name`: Nome do Canvas
    * Campo `string` adicionado `canvas_variation_name`: Nome da variante do canva recebida por este usuário
    * Campo `string` adicionado `canvas_step_name`: Nome da etapa do Canvas

* Mudanças de campo para o tipo de evento `users.canvas.experimentstep.Conversion`:
    * Campo `string` adicionado `canvas_name`: Nome do Canvas
    * Campo `string` adicionado `canvas_variation_name`: Nome da variante do canva recebida por este usuário
    * Campo `string` adicionado `canvas_step_name`: Nome da etapa do Canvas
    * Campo `string` adicionado `experiment_split_name`: Nome da divisão do experimento
    * Campo `string` adicionado `conversion_behavior`: String codificada em JSON descrevendo o comportamento de conversão

* Mudanças de campo para o tipo de evento `users.canvas.experimentstep.SplitEntry`:
    * Campo `string` adicionado `canvas_name`: Nome do Canvas
    * Campo `string` adicionado `canvas_variation_name`: Nome da variante do canva recebida por este usuário
    * Campo `string` adicionado `canvas_step_name`: Nome da etapa do Canvas
    * Campo `string` adicionado `experiment_split_name`: Nome da divisão do experimento

* Mudanças de campo para o tipo de evento `users.canvasstep.Progression`:
    * Campo `string` adicionado `canvas_name`: Nome do Canvas
    * Campo `string` adicionado `canvas_variation_name`: Nome da variante do canva recebida por este usuário
    * Campo `string` adicionado `canvas_step_name`: Nome da etapa do Canvas

* Mudanças de campo para o tipo de evento `users.messages.banner.Abort`:
    * Campo `string` adicionado `campaign_name`: Nome da campanha
    * Campo `string` adicionado `message_variation_name`: Nome da variação da mensagem

* Mudanças de campo para o tipo de evento `users.messages.banner.Click`:
    * Campo `string` adicionado `campaign_name`: Nome da campanha
    * Campo `string` adicionado `message_variation_name`: Nome da variação da mensagem

* Mudanças de campo para o tipo de evento `users.messages.banner.Impression`:
    * Campo `string` adicionado `campaign_name`: Nome da campanha
    * Campo `string` adicionado `message_variation_name`: Nome da variação da mensagem

* Mudanças de campo para o tipo de evento `users.messages.contentcard.Abort`:
    * Campo `string` adicionado `campaign_name`: Nome da campanha
    * Campo `string` adicionado `message_variation_name`: Nome da variação da mensagem
    * Campo `string` adicionado `canvas_name`: Nome do Canvas
    * Campo `string` adicionado `canvas_variation_name`: Nome da variante do canva recebida por este usuário
    * Campo `string` adicionado `canvas_step_name`: Nome da etapa do Canvas

* Mudanças de campo para o tipo de evento `users.messages.contentcard.Click`:
    * Campo `string` adicionado `campaign_name`: Nome da campanha
    * Campo `string` adicionado `message_variation_name`: Nome da variação da mensagem
    * Campo `string` adicionado `canvas_name`: Nome do Canvas
    * Campo `string` adicionado `canvas_variation_name`: Nome da variante do canva recebida por este usuário
    * Campo `string` adicionado `canvas_step_name`: Nome da etapa do Canvas

* Mudanças de campo para o tipo de evento `users.messages.contentcard.Dismiss`:
    * Campo `string` adicionado `campaign_name`: Nome da campanha
    * Campo `string` adicionado `message_variation_name`: Nome da variação da mensagem
    * Campo `string` adicionado `canvas_name`: Nome do Canvas
    * Campo `string` adicionado `canvas_variation_name`: Nome da variante do canva recebida por este usuário
    * Campo `string` adicionado `canvas_step_name`: Nome da etapa do Canvas

* Mudanças de campo para o tipo de evento `users.messages.contentcard.Impression`:
    * Campo `string` adicionado `campaign_name`: Nome da campanha
    * Campo `string` adicionado `message_variation_name`: Nome da variação da mensagem
    * Campo `string` adicionado `canvas_name`: Nome do Canvas
    * Campo `string` adicionado `canvas_variation_name`: Nome da variante do canva recebida por este usuário
    * Campo `string` adicionado `canvas_step_name`: Nome da etapa do Canvas

* Mudanças de campo para o tipo de evento `users.messages.contentcard.Send`:
    * Campo `string` adicionado `campaign_name`: Nome da campanha
    * Campo `string` adicionado `message_variation_name`: Nome da variação da mensagem
    * Campo `string` adicionado `canvas_name`: Nome do Canvas
    * Campo `string` adicionado `canvas_variation_name`: Nome da variante do canva recebida por este usuário
    * Campo `string` adicionado `canvas_step_name`: Nome da etapa do Canvas

* Mudanças de campo para o tipo de evento `users.messages.email.Abort`:
    * Campo `string` adicionado `campaign_name`: Nome da campanha
    * Campo `string` adicionado `message_variation_name`: Nome da variação da mensagem
    * Campo `string` adicionado `canvas_name`: Nome do Canvas
    * Campo `string` adicionado `canvas_variation_name`: Nome da variante do canva recebida por este usuário
    * Campo `string` adicionado `canvas_step_name`: Nome da etapa do Canvas

* Mudanças de campo para o tipo de evento `users.messages.email.Bounce`:
    * Campo `string` adicionado `campaign_name`: Nome da campanha
    * Campo `string` adicionado `message_variation_name`: Nome da variação da mensagem
    * Campo `string` adicionado `canvas_name`: Nome do Canvas
    * Campo `string` adicionado `canvas_variation_name`: Nome da variante do canva recebida por este usuário
    * Campo `string` adicionado `canvas_step_name`: Nome da etapa do Canvas

* Mudanças de campo para o tipo de evento `users.messages.email.Click`:
    * Campo `string` adicionado `campaign_name`: Nome da campanha
    * Campo `string` adicionado `message_variation_name`: Nome da variação da mensagem
    * Campo `string` adicionado `canvas_name`: Nome do Canvas
    * Campo `string` adicionado `canvas_variation_name`: Nome da variante do canva recebida por este usuário
    * Campo `string` adicionado `canvas_step_name`: Nome da etapa do Canvas

* Mudanças de campo para o tipo de evento `users.messages.email.Deferral`:
    * Campo `string` adicionado `campaign_name`: Nome da campanha
    * Campo `string` adicionado `message_variation_name`: Nome da variação da mensagem
    * Campo `string` adicionado `canvas_name`: Nome do Canvas
    * Campo `string` adicionado `canvas_variation_name`: Nome da variante do canva recebida por este usuário
    * Campo `string` adicionado `canvas_step_name`: Nome da etapa do Canvas

* Mudanças de campo para o tipo de evento `users.messages.email.Delivery`:
    * Campo `string` adicionado `campaign_name`: Nome da campanha
    * Campo `string` adicionado `message_variation_name`: Nome da variação da mensagem
    * Campo `string` adicionado `canvas_name`: Nome do Canvas
    * Campo `string` adicionado `canvas_variation_name`: Nome da variante do canva recebida por este usuário
    * Campo `string` adicionado `canvas_step_name`: Nome da etapa do Canvas

* Mudanças de campo para o tipo de evento `users.messages.email.MarkAsSpam`:
    * Campo `string` adicionado `campaign_name`: Nome da campanha
    * Campo `string` adicionado `message_variation_name`: Nome da variação da mensagem
    * Campo `string` adicionado `canvas_name`: Nome do Canvas
    * Campo `string` adicionado `canvas_variation_name`: Nome da variante do canva recebida por este usuário
    * Campo `string` adicionado `canvas_step_name`: Nome da etapa do Canvas

* Mudanças de campo para o tipo de evento `users.messages.email.Open`:
    * Campo `string` adicionado `campaign_name`: Nome da campanha
    * Campo `string` adicionado `message_variation_name`: Nome da variação da mensagem
    * Campo `string` adicionado `canvas_name`: Nome do Canvas
    * Campo `string` adicionado `canvas_variation_name`: Nome da variante do canva recebida por este usuário
    * Campo `string` adicionado `canvas_step_name`: Nome da etapa do Canvas

* Mudanças de campo para o tipo de evento `users.messages.email.Retry`:
    * Campo `string` adicionado `campaign_name`: Nome da campanha
    * Campo `string` adicionado `message_variation_name`: Nome da variação da mensagem
    * Campo `string` adicionado `canvas_name`: Nome do Canvas
    * Campo `string` adicionado `canvas_variation_name`: Nome da variante do canva recebida por este usuário
    * Campo `string` adicionado `canvas_step_name`: Nome da etapa do Canvas

* Mudanças de campo para o tipo de evento `users.messages.email.Send`:
    * Campo `string` adicionado `campaign_name`: Nome da campanha
    * Campo `string` adicionado `message_variation_name`: Nome da variação da mensagem
    * Campo `string` adicionado `canvas_name`: Nome do Canvas
    * Campo `string` adicionado `canvas_variation_name`: Nome da variante do canva recebida por este usuário
    * Campo `string` adicionado `canvas_step_name`: Nome da etapa do Canvas

* Mudanças de campo para o tipo de evento `users.messages.email.SoftBounce`:
    * Campo `string` adicionado `campaign_name`: Nome da campanha
    * Campo `string` adicionado `message_variation_name`: Nome da variação da mensagem
    * Campo `string` adicionado `canvas_name`: Nome do Canvas
    * Campo `string` adicionado `canvas_variation_name`: Nome da variante do canva recebida por este usuário
    * Campo `string` adicionado `canvas_step_name`: Nome da etapa do Canvas

* Mudanças de campo para o tipo de evento `users.messages.email.Unsubscribe`:
    * Campo `string` adicionado `campaign_name`: Nome da campanha
    * Campo `string` adicionado `message_variation_name`: Nome da variação da mensagem
    * Campo `string` adicionado `canvas_name`: Nome do Canvas
    * Campo `string` adicionado `canvas_variation_name`: Nome da variante do canva recebida por este usuário
    * Campo `string` adicionado `canvas_step_name`: Nome da etapa do Canvas

* Mudanças de campo para o tipo de evento `users.messages.featureflag.Impression`:
    * Campo `string` adicionado `campaign_name`: Nome da campanha
    * Campo `string` adicionado `canvas_name`: Nome do Canvas
    * Campo `string` adicionado `canvas_step_name`: Nome da etapa do Canvas
    * Campo `string` adicionado `canvas_variation_name`: Nome da variante do canva recebida por este usuário
    * Campo `string` adicionado `message_variation_name`: Nome da variação da mensagem

* Mudanças de campo para o tipo de evento `users.messages.inappmessage.Abort`:
    * Campo `string` adicionado `campaign_name`: Nome da campanha
    * Campo `string` adicionado `message_variation_name`: Nome da variação da mensagem
    * Campo `string` adicionado `canvas_name`: Nome do Canvas
    * Campo `string` adicionado `canvas_variation_name`: Nome da variante do canva recebida por este usuário
    * Campo `string` adicionado `canvas_step_name`: Nome da etapa do Canvas

* Mudanças de campo para o tipo de evento `users.messages.inappmessage.Click`:
    * Campo `string` adicionado `campaign_name`: Nome da campanha
    * Campo `string` adicionado `message_variation_name`: Nome da variação da mensagem
    * Campo `string` adicionado `canvas_name`: Nome do Canvas
    * Campo `string` adicionado `canvas_variation_name`: Nome da variante do canva recebida por este usuário
    * Campo `string` adicionado `canvas_step_name`: Nome da etapa do Canvas

* Mudanças de campo para o tipo de evento `users.messages.inappmessage.Impression`:
    * Campo `string` adicionado `campaign_name`: Nome da campanha
    * Campo `string` adicionado `message_variation_name`: Nome da variação da mensagem
    * Campo `string` adicionado `canvas_name`: Nome do Canvas
    * Campo `string` adicionado `canvas_variation_name`: Nome da variante do canva recebida por este usuário
    * Campo `string` adicionado `canvas_step_name`: Nome da etapa do Canvas

* Mudanças de campo para o tipo de evento `users.messages.line.Retry`:
    * Campo `string` adicionado `campaign_name`: Nome da campanha
    * Campo `string` adicionado `canvas_step_name`: Nome da etapa do Canvas

* Mudanças de campo para o tipo de evento `users.messages.pushnotification.Abort`:
    * Campo `string` adicionado `campaign_name`: Nome da campanha
    * Campo `string` adicionado `message_variation_name`: Nome da variação da mensagem
    * Campo `string` adicionado `canvas_name`: Nome do Canvas
    * Campo `string` adicionado `canvas_variation_name`: Nome da variante do canva recebida por este usuário
    * Campo `string` adicionado `canvas_step_name`: Nome da etapa do Canvas

* Mudanças de campo para o tipo de evento `users.messages.pushnotification.Bounce`:
    * Campo `string` adicionado `campaign_name`: Nome da campanha
    * Campo `string` adicionado `message_variation_name`: Nome da variação da mensagem
    * Campo `string` adicionado `canvas_name`: Nome do Canvas
    * Campo `string` adicionado `canvas_variation_name`: Nome da variante do canva recebida por este usuário
    * Campo `string` adicionado `canvas_step_name`: Nome da etapa do Canvas

* Mudanças de campo para o tipo de evento `users.messages.pushnotification.InfluencedOpen`:
    * Campo `string` adicionado `campaign_name`: Nome da campanha
    * Campo `string` adicionado `message_variation_name`: Nome da variação da mensagem
    * Campo `string` adicionado `canvas_name`: Nome do Canvas
    * Campo `string` adicionado `canvas_variation_name`: Nome da variante do canva recebida por este usuário
    * Campo `string` adicionado `canvas_step_name`: Nome da etapa do Canvas

* Mudanças de campo para o tipo de evento `users.messages.pushnotification.IosForeground`:
    * Campo `string` adicionado `campaign_name`: Nome da campanha
    * Campo `string` adicionado `message_variation_name`: Nome da variação da mensagem
    * Campo `string` adicionado `canvas_name`: Nome do Canvas
    * Campo `string` adicionado `canvas_variation_name`: Nome da variante do canva recebida por este usuário
    * Campo `string` adicionado `canvas_step_name`: Nome da etapa do Canvas

* Mudanças de campo para o tipo de evento `users.messages.pushnotification.Open`:
    * Campo `string` adicionado `campaign_name`: Nome da campanha
    * Campo `string` adicionado `message_variation_name`: Nome da variação da mensagem
    * Campo `string` adicionado `canvas_name`: Nome do Canvas
    * Campo `string` adicionado `canvas_variation_name`: Nome da variante do canva recebida por este usuário
    * Campo `string` adicionado `canvas_step_name`: Nome da etapa do Canvas

* Mudanças de campo para o tipo de evento `users.messages.pushnotification.Retry`:
    * Campo `string` adicionado `campaign_name`: Nome da campanha
    * Campo `string` adicionado `message_variation_name`: Nome da variação da mensagem
    * Campo `string` adicionado `canvas_name`: Nome do Canvas
    * Campo `string` adicionado `canvas_variation_name`: Nome da variante do canva recebida por este usuário
    * Campo `string` adicionado `canvas_step_name`: Nome da etapa do Canvas

* Mudanças de campo para o tipo de evento `users.messages.pushnotification.Send`:
    * Campo `string` adicionado `campaign_name`: Nome da campanha
    * Campo `string` adicionado `message_variation_name`: Nome da variação da mensagem
    * Campo `string` adicionado `canvas_name`: Nome do Canvas
    * Campo `string` adicionado `canvas_variation_name`: Nome da variante do canva recebida por este usuário
    * Campo `string` adicionado `canvas_step_name`: Nome da etapa do Canvas

* Mudanças de campo para o tipo de evento `users.messages.rcs.InboundReceive`:
    * Campo `string` adicionado `canvas_variation_name`: Nome da variante do canva recebida por este usuário

* Mudanças de campo para o tipo de evento `users.messages.sms.Abort`:
    * Campo `string` adicionado `campaign_name`: Nome da campanha
    * Campo `string` adicionado `message_variation_name`: Nome da variação da mensagem
    * Campo `string` adicionado `canvas_name`: Nome do Canvas
    * Campo `string` adicionado `canvas_variation_name`: Nome da variante do canva recebida por este usuário
    * Campo `string` adicionado `canvas_step_name`: Nome da etapa do Canvas

* Mudanças de campo para o tipo de evento `users.messages.sms.CarrierSend`:
    * Campo `string` adicionado `campaign_name`: Nome da campanha
    * Campo `string` adicionado `message_variation_name`: Nome da variação da mensagem
    * Campo `string` adicionado `canvas_name`: Nome do Canvas
    * Campo `string` adicionado `canvas_variation_name`: Nome da variante do canva recebida por este usuário
    * Campo `string` adicionado `canvas_step_name`: Nome da etapa do Canvas

* Mudanças de campo para o tipo de evento `users.messages.sms.Delivery`:
    * Campo `string` adicionado `campaign_name`: Nome da campanha
    * Campo `string` adicionado `message_variation_name`: Nome da variação da mensagem
    * Campo `string` adicionado `canvas_name`: Nome do Canvas
    * Campo `string` adicionado `canvas_variation_name`: Nome da variante do canva recebida por este usuário
    * Campo `string` adicionado `canvas_step_name`: Nome da etapa do Canvas

* Mudanças de campo para o tipo de evento `users.messages.sms.DeliveryFailure`:
    * Campo `string` adicionado `campaign_name`: Nome da campanha
    * Campo `string` adicionado `message_variation_name`: Nome da variação da mensagem
    * Campo `string` adicionado `canvas_name`: Nome do Canvas
    * Campo `string` adicionado `canvas_variation_name`: Nome da variante do canva recebida por este usuário
    * Campo `string` adicionado `canvas_step_name`: Nome da etapa do Canvas

* Mudanças de campo para o tipo de evento `users.messages.sms.InboundReceive`:
    * Campo `string` adicionado `campaign_name`: Nome da campanha
    * Campo `string` adicionado `message_variation_name`: Nome da variação da mensagem
    * Campo `string` adicionado `canvas_name`: Nome do Canvas
    * Campo `string` adicionado `canvas_variation_name`: Nome da variante do canva recebida por este usuário
    * Campo `string` adicionado `canvas_step_name`: Nome da etapa do Canvas

* Mudanças de campo para o tipo de evento `users.messages.sms.Rejection`:
    * Campo `string` adicionado `campaign_name`: Nome da campanha
    * Campo `string` adicionado `message_variation_name`: Nome da variação da mensagem
    * Campo `string` adicionado `canvas_name`: Nome do Canvas
    * Campo `string` adicionado `canvas_variation_name`: Nome da variante do canva recebida por este usuário
    * Adicionado novo campo `string` `canvas_step_name`: Nome da etapa do canva

* Mudanças no tipo de evento `users.messages.sms.Retry`:
    * Adicionado novo campo `string` `campaign_name`: Nome da campanha
    * Adicionado novo campo `string` `message_variation_name`: Nome da variação da mensagem
    * Adicionado novo campo `string` `canvas_name`: Nome do canva
    * Adicionado novo campo `string` `canvas_variation_name`: Nome da variante do canva recebida por este usuário
    * Adicionado novo campo `string` `canvas_step_name`: Nome da etapa do canva

* Mudanças no tipo de evento `users.messages.sms.Send`:
    * Adicionado novo campo `string` `campaign_name`: Nome da campanha
    * Adicionado novo campo `string` `message_variation_name`: Nome da variação da mensagem
    * Adicionado novo campo `string` `canvas_name`: Nome do canva
    * Adicionado novo campo `string` `canvas_variation_name`: Nome da variante do canva recebida por este usuário
    * Adicionado novo campo `string` `canvas_step_name`: Nome da etapa do canva

* Mudanças no tipo de evento `users.messages.sms.ShortLinkClick`:
    * Adicionado novo campo `string` `campaign_name`: Nome da campanha
    * Adicionado novo campo `string` `message_variation_name`: Nome da variação da mensagem
    * Adicionado novo campo `string` `canvas_name`: Nome do canva
    * Adicionado novo campo `string` `canvas_variation_name`: Nome da variante do canva recebida por este usuário
    * Adicionado novo campo `string` `canvas_step_name`: Nome da etapa do canva

* Mudanças no tipo de evento `users.messages.webhook.Abort`:
    * Adicionado novo campo `string` `campaign_name`: Nome da campanha
    * Adicionado novo campo `string` `message_variation_name`: Nome da variação da mensagem
    * Adicionado novo campo `string` `canvas_name`: Nome do canva
    * Adicionado novo campo `string` `canvas_variation_name`: Nome da variante do canva recebida por este usuário
    * Adicionado novo campo `string` `canvas_step_name`: Nome da etapa do canva

* Mudanças no tipo de evento `users.messages.webhook.Failure`:
    * Adicionado novo campo `string` `campaign_name`: Nome da campanha
    * Adicionado novo campo `string` `canvas_name`: Nome do canva
    * Adicionado novo campo `string` `canvas_step_name`: Nome da etapa do canva
    * Adicionado novo campo `string` `canvas_variation_name`: Nome da variante do canva recebida por este usuário
    * Adicionado novo campo `string` `message_variation_name`: Nome da variação da mensagem

* Mudanças no tipo de evento `users.messages.webhook.Retry`:
    * Adicionado novo campo `string` `campaign_name`: Nome da campanha
    * Adicionado novo campo `string` `message_variation_name`: Nome da variação da mensagem
    * Adicionado novo campo `string` `canvas_name`: Nome do canva
    * Adicionado novo campo `string` `canvas_variation_name`: Nome da variante do canva recebida por este usuário
    * Adicionado novo campo `string` `canvas_step_name`: Nome da etapa do canva

* Mudanças no tipo de evento `users.messages.webhook.Send`:
    * Adicionado novo campo `string` `campaign_name`: Nome da campanha
    * Adicionado novo campo `string` `message_variation_name`: Nome da variação da mensagem
    * Adicionado novo campo `string` `canvas_name`: Nome do canva
    * Adicionado novo campo `string` `canvas_variation_name`: Nome da variante do canva recebida por este usuário
    * Adicionado novo campo `string` `canvas_step_name`: Nome da etapa do canva

* Mudanças no tipo de evento `users.messages.whatsapp.Abort`:
    * Adicionado novo campo `string` `campaign_name`: Nome da campanha
    * Adicionado novo campo `string` `message_variation_name`: Nome da variação da mensagem
    * Adicionado novo campo `string` `canvas_name`: Nome do canva
    * Adicionado novo campo `string` `canvas_variation_name`: Nome da variante do canva recebida por este usuário
    * Adicionado novo campo `string` `canvas_step_name`: Nome da etapa do canva

* Mudanças no tipo de evento `users.messages.whatsapp.Click`:
    * Adicionado novo campo `string` `campaign_name`: Nome da campanha
    * Adicionado novo campo `string` `message_variation_name`: Nome da variação da mensagem
    * Adicionado novo campo `string` `canvas_name`: Nome do canva
    * Adicionado novo campo `string` `canvas_variation_name`: Nome da variante do canva recebida por este usuário
    * Adicionado novo campo `string` `canvas_step_name`: Nome da etapa do canva

* Mudanças no tipo de evento `users.messages.whatsapp.Delivery`:
    * Adicionado novo campo `string` `campaign_name`: Nome da campanha
    * Adicionado novo campo `string` `message_variation_name`: Nome da variação da mensagem
    * Adicionado novo campo `string` `canvas_name`: Nome do canva
    * Adicionado novo campo `string` `canvas_variation_name`: Nome da variante do canva recebida por este usuário
    * Adicionado novo campo `string` `canvas_step_name`: Nome da etapa do canva

* Mudanças no tipo de evento `users.messages.whatsapp.Failure`:
    * Adicionado novo campo `string` `campaign_name`: Nome da campanha
    * Adicionado novo campo `string` `message_variation_name`: Nome da variação da mensagem
    * Adicionado novo campo `string` `canvas_name`: Nome do canva
    * Adicionado novo campo `string` `canvas_variation_name`: Nome da variante do canva recebida por este usuário
    * Adicionado novo campo `string` `canvas_step_name`: Nome da etapa do canva

* Mudanças no tipo de evento `users.messages.whatsapp.InboundReceive`:
    * Adicionado novo campo `string` `campaign_name`: Nome da campanha
    * Adicionado novo campo `string` `canvas_name`: Nome do canva
    * Adicionado novo campo `string` `canvas_step_name`: Nome da etapa do canva
    * Adicionado novo campo `string` `canvas_variation_name`: Nome da variante do canva recebida por este usuário
    * Adicionado novo campo `string` `message_variation_name`: Nome da variação da mensagem

* Mudanças no tipo de evento `users.messages.whatsapp.Read`:
    * Adicionado novo campo `string` `campaign_name`: Nome da campanha
    * Adicionado novo campo `string` `message_variation_name`: Nome da variação da mensagem
    * Adicionado novo campo `string` `canvas_name`: Nome do canva
    * Adicionado novo campo `string` `canvas_variation_name`: Nome da variante do canva recebida por este usuário
    * Adicionado novo campo `string` `canvas_step_name`: Nome da etapa do canva

* Mudanças no tipo de evento `users.messages.whatsapp.Retry`:
    * Adicionado novo campo `string` `campaign_name`: Nome da campanha
    * Adicionado novo campo `string` `message_variation_name`: Nome da variação da mensagem
    * Adicionado novo campo `string` `canvas_name`: Nome do canva
    * Adicionado novo campo `string` `canvas_variation_name`: Nome da variante do canva recebida por este usuário
    * Adicionado novo campo `string` `canvas_step_name`: Nome da etapa do canva

* Mudanças no tipo de evento `users.messages.whatsapp.Send`:
    * Adicionado novo campo `string` `campaign_name`: Nome da campanha
    * Adicionado novo campo `string` `canvas_name`: Nome do canva
    * Adicionado novo campo `string` `canvas_step_name`: Nome da etapa do canva
    * Adicionado novo campo `string` `canvas_variation_name`: Nome da variante do canva recebida por este usuário
    * Adicionado novo campo `string` `message_variation_name`: Nome da variação da mensagem

## Mudanças na Versão 5 (data de lançamento 2026-02-04)

### Mudanças para armazenamento

* Adicionado novo tipo de evento `agentconsole.AgentExecuted`.

* Adicionado novo tipo de evento `agentconsole.ToolInvocation`.

* Adicionado novo tipo de evento `users.messages.email.Retry`.

* Adicionado novo tipo de evento `users.messages.line.Retry`.

* Adicionado novo tipo de evento `users.messages.pushnotification.Retry`.

* Adicionado novo tipo de evento `users.messages.sms.Retry`.

* Adicionado novo tipo de evento `users.messages.webhook.Retry`.

* Adicionado novo tipo de evento `users.messages.whatsapp.Retry`.

* Mudanças no tipo de evento `users.behaviors.pushnotification.TokenStateChange`:
    * Adicionado novo campo `long` `time_ms`: Tempo em milissegundos quando o evento aconteceu

### Mudanças para compartilhamento de dados

* Adicionado novo tipo de evento `agentconsole.AgentExecuted`.

* Adicionado novo tipo de evento `agentconsole.ToolInvocation`.

* Adicionado novo tipo de evento `users.messages.email.Retry`.

* Adicionado novo tipo de evento `users.messages.line.Retry`.

* Adicionado novo tipo de evento `users.messages.pushnotification.Retry`.

* Adicionado novo tipo de evento `users.messages.sms.Retry`.

* Adicionado novo tipo de evento `users.messages.webhook.Retry`.

* Adicionado novo tipo de evento `users.messages.whatsapp.Retry`.

* Mudanças no tipo de evento `users.behaviors.pushnotification.TokenStateChange`:
    * Adicionado novo campo `long` `time_ms`: Tempo em milissegundos quando o evento aconteceu

## Mudanças na Versão 4 (data de lançamento 2026-01-07)

### Mudanças para armazenamento

* Mudanças no tipo de evento `users.behaviors.pushnotification.TokenStateChange`:
    * Adicionado novo campo `string` `push_token`: Token por push do evento

* Mudanças no tipo de evento `users.messages.pushnotification.Bounce`:
    * Adicionado novo campo `string` `push_token`: Token por push do evento

* Mudanças no tipo de evento `users.messages.pushnotification.Send`:
    * Adicionado novo campo `string` `push_token`: Token por push do evento

* Mudanças no tipo de evento `users.messages.rcs.Click`:
    * Adicionado novo campo `string` `canvas_variation_name`: Nome da variante do canva recebida por este usuário
    * Campo `user_phone_number` agora é *opcional*.

* Mudanças no tipo de evento `users.messages.rcs.InboundReceive`:
    * Campo `user_id` agora é *opcional*.

* Mudanças no tipo de evento `users.messages.rcs.Rejection`:
    * Adicionado novo campo `string` `canvas_step_message_variation_id`: API ID da variação da mensagem da etapa do canva que este usuário recebeu

### Mudanças para compartilhamento de dados

* Mudanças no tipo de evento `users.messages.rcs.Click`:
    * Adicionado novo campo `string` `canvas_variation_name`: Nome da variante do canva recebida por este usuário
    * Campo `user_phone_number` agora é *opcional*.

* Mudanças no tipo de evento `users.messages.rcs.InboundReceive`:
    * Campo `user_id` agora é *opcional*.

* Mudanças no tipo de evento `users.messages.rcs.Rejection`:
    * Adicionado novo campo `string` `canvas_step_message_variation_api_id`: API ID da variação da mensagem da etapa do canva que este usuário recebeu

## Mudanças na Versão 3 (data de lançamento 2025-10-08)

### Mudanças para armazenamento

* Adicionado novo tipo de evento `users.messages.line.Abort`.

* Adicionado novo tipo de evento `users.messages.line.Click`.

* Adicionado novo tipo de evento `users.messages.line.InboundReceive`.

* Adicionado novo tipo de evento `users.messages.line.Send`.

* Adicionado novo tipo de evento `users.messages.rcs.Abort`.

* Adicionado novo tipo de evento `users.messages.rcs.Click`.

* Adicionado novo tipo de evento `users.messages.rcs.Delivery`.

* Adicionado novo tipo de evento `users.messages.rcs.InboundReceive`.

* Adicionado novo tipo de evento `users.messages.rcs.Read`.

* Adicionado novo tipo de evento `users.messages.rcs.Rejection`.

* Adicionado novo tipo de evento `users.messages.rcs.Send`.

* Mudanças no tipo de evento `users.messages.sms.Delivery`:
    * Adicionado novo campo `boolean` `is_sms_fallback`: Indica que uma mensagem de fallback SMS foi enviada devido a uma mensagem RCS rejeitada. A mensagem pode resultar em entrega, falha de entrega ou rejeição, Pode ser vinculado ao evento de Rejeição RCS via um ID de envio e ID de despacho

* Mudanças no tipo de evento `users.messages.sms.DeliveryFailure`:
    * Adicionado novo campo `boolean` `is_sms_fallback`: Indica que uma mensagem de fallback SMS foi enviada devido a uma mensagem RCS rejeitada. A mensagem pode resultar em entrega, falha de entrega ou rejeição, Pode ser vinculado ao evento de Rejeição RCS via um ID de envio e ID de despacho

* Mudanças no tipo de evento `users.messages.sms.Rejection`:
    * Adicionado novo campo `boolean` `is_sms_fallback`: Indica que uma mensagem de fallback SMS foi enviada devido a uma mensagem RCS rejeitada. A mensagem pode resultar em entrega, falha de entrega ou rejeição, Pode ser vinculado ao evento de Rejeição RCS via um ID de envio e ID de despacho Pode ser vinculado ao evento de Rejeição RCS via um ID de envio e ID de despacho. (Propriedade do evento)

* Mudanças no tipo de evento `users.messages.whatsapp.Delivery`:
    * Adicionado novo campo `string` `flow_id`: O ID único do Fluxo no Gerenciador do WhatsApp. Presente se a mensagem incluir um CTA para responder a um Fluxo do WhatsApp
    * Adicionado novo campo `string` `template_name`: [IPI] Nome do modelo no gerenciador do WhatsApp. Presente se enviando uma Mensagem de Modelo
    * Adicionado novo campo `string` `message_id`: O ID único gerado pela Meta para esta mensagem

* Mudanças no tipo de evento `users.messages.whatsapp.Failure`:
    * Adicionado novo campo `string` `message_id`: O ID único gerado pela Meta para esta mensagem
    * Adicionado novo campo `string` `template_name`: [IPI] Nome do modelo no gerenciador do WhatsApp. Presente se enviando uma Mensagem de Modelo
    * Adicionado novo campo `string` `flow_id`: O ID único do Fluxo no Gerenciador do WhatsApp. Presente se a mensagem incluir um CTA para responder a um Fluxo do WhatsApp

* Mudanças no tipo de evento `users.messages.whatsapp.InboundReceive`:
    * Adicionado novo campo `string` `catalog_id`: ID do catálogo de produto, caso um produto seja mencionado na mensagem recebida (caso contrário, permanece vazio).
    * Adicionado novo campo `string` `product_id`: SKU do produto, caso um produto seja mencionado na mensagem recebida (caso contrário, permanece vazio).
    * Adicionado novo campo `string` `flow_id`: O ID único do Fluxo no Gerenciador do WhatsApp. Presente se o usuário estiver respondendo a um Fluxo do WhatsApp.
    * Adicionado novo campo `string` `flow_response_json`: [IPI] Os valores do formulário com os quais o usuário respondeu. Presente se o usuário estiver respondendo a um Fluxo do WhatsApp.
    * Adicionado novo campo `string` `message_id`: O ID único gerado pela Meta para esta mensagem
    * Adicionado novo campo `string` `in_reply_to`: O message_id da mensagem à qual esta mensagem estava respondendo

* Mudanças no tipo de evento `users.messages.whatsapp.Read`:
    * Adicionado novo campo `string` `template_name`: [IPI] Nome do modelo no gerenciador do WhatsApp. Presente se enviando uma Mensagem de Modelo
    * Adicionado novo campo `string` `message_id`: O ID único gerado pela Meta para esta mensagem
    * Adicionado novo campo `string` `flow_id`: O ID único do Fluxo no Gerenciador do WhatsApp. Presente se a mensagem incluir um CTA para responder a um Fluxo do WhatsApp

* Mudanças no tipo de evento `users.messages.whatsapp.Send`:
    * Adicionado novo campo `string` `flow_id`: O ID único do Fluxo no Gerenciador do WhatsApp. Presente se a mensagem incluir um CTA para responder a um Fluxo do WhatsApp
    * Adicionado novo campo `string` `template_name`: [IPI] Nome do modelo no Gerenciador do WhatsApp. Presente se enviando uma Mensagem de Modelo
    * Adicionado novo campo `string` `message_id`: O ID único gerado pela Meta para esta mensagem

### Mudanças para compartilhamento de dados

* Adicionado novo tipo de evento `users.messages.line.Abort`.

* Adicionado novo tipo de evento `users.messages.line.Click`.

* Adicionado novo tipo de evento `users.messages.line.InboundReceive`.

* Adicionado novo tipo de evento `users.messages.line.Send`.

* Adicionado novo tipo de evento `users.messages.rcs.Abort`.

* Adicionado novo tipo de evento `users.messages.rcs.Click`.

* Adicionado novo tipo de evento `users.messages.rcs.Delivery`.

* Adicionado novo tipo de evento `users.messages.rcs.InboundReceive`.

* Adicionado novo tipo de evento `users.messages.rcs.Read`.

* Adicionado novo tipo de evento `users.messages.rcs.Rejection`.

* Adicionado novo tipo de evento `users.messages.rcs.Send`.

* Mudanças no tipo de evento `users.messages.sms.Delivery`:
    * Adicionado novo campo `boolean` `is_sms_fallback`: Indica se a tentativa de fallback de SMS foi feita para esta mensagem RCS rejeitada. Está vinculado/pareado ao evento de Entrega de SMS

* Mudanças no tipo de evento `users.messages.sms.DeliveryFailure`:
    * Adicionado novo campo `boolean` `is_sms_fallback`: Indica se a tentativa de fallback de SMS foi feita para esta mensagem RCS rejeitada. Está vinculado/pareado ao evento de Entrega de SMS

* Mudanças no tipo de evento `users.messages.sms.Rejection`:
    * Adicionado novo campo `boolean` `is_sms_fallback`: Indica se a tentativa de fallback de SMS foi feita para esta mensagem RCS rejeitada. Está vinculado/pareado ao evento de Entrega de SMS

* Mudanças no tipo de evento `users.messages.whatsapp.Delivery`:
    * Adicionado novo campo `string` `flow_id`: O ID único do Fluxo no Gerenciador do WhatsApp. Presente se o usuário estiver respondendo a um Fluxo do WhatsApp.
    * Adicionado novo campo `string` `template_name`: [IPI] Nome do modelo no gerenciador do WhatsApp. Presente se enviando uma Mensagem de Modelo
    * Adicionado novo campo `string` `message_id`: O ID único gerado pela Meta para esta mensagem

* Mudanças no tipo de evento `users.messages.whatsapp.Failure`:
    * Adicionado novo campo `string` `message_id`: O ID único gerado pela Meta para esta mensagem
    * Adicionado novo campo `string` `template_name`: [IPI] Nome do modelo no gerenciador do WhatsApp. Presente se enviando uma Mensagem de Modelo
    * Adicionado novo campo `string` `flow_id`: O ID único do Fluxo no Gerenciador do WhatsApp. Presente se o usuário estiver respondendo a um Fluxo do WhatsApp.

* Mudanças no tipo de evento `users.messages.whatsapp.InboundReceive`:
    * Adicionado novo campo `string` `catalog_id`: ID do catálogo de produto, caso um produto seja mencionado na mensagem recebida (caso contrário, permanece vazio).
    * Adicionado novo campo `string` `product_id`: ID do produto adquirido
    * Adicionado novo campo `string` `flow_id`: O ID único do Fluxo no Gerenciador do WhatsApp. Presente se o usuário estiver respondendo a um Fluxo do WhatsApp.
    * Adicionado novo campo `string` `flow_response_json`: [IPI] Os valores do formulário com os quais o usuário respondeu. Presente se o usuário estiver respondendo a um Fluxo do WhatsApp.
    * Adicionado novo campo `string` `message_id`: O ID único gerado pela Meta para esta mensagem
    * Adicionado novo campo `string` `in_reply_to`: O message_id da mensagem à qual esta mensagem estava respondendo

* Mudanças no tipo de evento `users.messages.whatsapp.Read`:
    * Adicionado novo campo `string` `template_name`: [IPI] Nome do modelo no gerenciador do WhatsApp. Presente se enviando uma Mensagem de Modelo
    * Adicionado novo campo `string` `message_id`: O ID único gerado pela Meta para esta mensagem
    * Adicionado novo campo `string` `flow_id`: O ID único do Fluxo no Gerenciador do WhatsApp. Presente se o usuário estiver respondendo a um Fluxo do WhatsApp.

* Mudanças no tipo de evento `users.messages.whatsapp.Send`:
    * Adicionado novo campo `string` `flow_id`: O ID único do Fluxo no Gerenciador do WhatsApp. Presente se o usuário estiver respondendo a um Fluxo do WhatsApp.
    * Adicionado novo campo `string` `template_name`: [IPI] Nome do modelo no gerenciador do WhatsApp. Presente se enviando uma Mensagem de Modelo
    * Adicionado novo campo `string` `message_id`: O ID único gerado pela Meta para esta mensagem

## Mudanças na Versão 2 (data de lançamento nula)

### Mudanças para armazenamento

* Adicionado novo tipo de evento `users.behaviors.app.FirstSession`.

* Adicionado novo tipo de evento `users.behaviors.app.SessionEnd`.

* Adicionado novo tipo de evento `users.behaviors.app.SessionStart`.

* Adicionado novo tipo de evento `users.behaviors.CustomEvent`.

* Adicionado novo tipo de evento `users.behaviors.InstallAttribution`.

* Adicionado novo tipo de evento `users.behaviors.liveactivity.PushToStartTokenChange`.

* Adicionado novo tipo de evento `users.behaviors.liveactivity.UpdateTokenChange`.

* Adicionado novo tipo de evento `users.behaviors.Location`.

* Adicionado novo tipo de evento `users.behaviors.Purchase`.

* Adicionado novo tipo de evento `users.behaviors.pushnotification.TokenStateChange`.

* Adicionado novo tipo de evento `users.behaviors.subscription.GlobalStateChange`.

* Adicionado novo tipo de evento `users.behaviors.subscriptiongroup.StateChange`.

* Adicionado novo tipo de evento `users.behaviors.Uninstall`.

* Adicionado novo tipo de evento `users.campaigns.Conversion`.

* Adicionado novo tipo de evento `users.campaigns.EnrollInControl`.

* Adicionado novo tipo de evento `users.canvas.Conversion`.

* Adicionado novo tipo de evento `users.canvas.Entry`.

* Adicionado novo tipo de evento `users.canvas.exit.MatchedAudience`.

* Adicionado novo tipo de evento `users.canvas.exit.PerformedEvent`.

* Adicionado novo tipo de evento `users.canvas.experimentstep.Conversion`.

* Adicionado novo tipo de evento `users.canvas.experimentstep.SplitEntry`.

* Adicionado novo tipo de evento `users.canvasstep.Progression`.

* Adicionado novo tipo de evento `users.messages.banner.Abort`.

* Adicionado novo tipo de evento `users.messages.banner.Click`.

* Adicionado novo tipo de evento `users.messages.banner.Impression`.

* Adicionado novo tipo de evento `users.messages.contentcard.Abort`.

* Adicionado novo tipo de evento `users.messages.contentcard.Click`.

* Adicionado novo tipo de evento `users.messages.contentcard.Dismiss`.

* Adicionado novo tipo de evento `users.messages.contentcard.Impression`.

* Adicionado novo tipo de evento `users.messages.contentcard.Send`.

* Adicionado novo tipo de evento `users.messages.email.Abort`.

* Adicionado novo tipo de evento `users.messages.email.Bounce`.

* Adicionado novo tipo de evento `users.messages.email.Click`.

* Adicionado novo tipo de evento `users.messages.email.Deferral`.

* Adicionado novo tipo de evento `users.messages.email.Delivery`.

* Adicionado novo tipo de evento `users.messages.email.MarkAsSpam`.

* Adicionado novo tipo de evento `users.messages.email.Open`.

* Adicionado novo tipo de evento `users.messages.email.Send`.

* Adicionado novo tipo de evento `users.messages.email.SoftBounce`.

* Adicionado novo tipo de evento `users.messages.email.Unsubscribe`.

* Adicionado novo tipo de evento `users.messages.featureflag.Impression`.

* Adicionado novo tipo de evento `users.messages.inappmessage.Abort`.

* Adicionado novo tipo de evento `users.messages.inappmessage.Click`.

* Adicionado novo tipo de evento `users.messages.inappmessage.Impression`.

* Adicionado novo tipo de evento `users.messages.liveactivity.Outcome`.

* Adicionado novo tipo de evento `users.messages.liveactivity.Send`.

* Adicionado novo tipo de evento `users.messages.pushnotification.Abort`.

* Adicionado novo tipo de evento `users.messages.pushnotification.Bounce`.

* Adicionado novo tipo de evento `users.messages.pushnotification.IosForeground`.

* Adicionado novo tipo de evento `users.messages.pushnotification.Open`.

* Adicionado novo tipo de evento `users.messages.pushnotification.Send`.

* Adicionado novo tipo de evento `users.messages.sms.Abort`.

* Adicionado novo tipo de evento `users.messages.sms.CarrierSend`.

* Adicionado novo tipo de evento `users.messages.sms.Delivery`.

* Adicionado novo tipo de evento `users.messages.sms.DeliveryFailure`.

* Adicionado novo tipo de evento `users.messages.sms.InboundReceive`.

* Adicionado novo tipo de evento `users.messages.sms.Rejection`.

* Adicionado novo tipo de evento `users.messages.sms.Send`.

* Adicionado novo tipo de evento `users.messages.sms.ShortLinkClick`.

* Adicionado novo tipo de evento `users.messages.webhook.Abort`.

* Adicionado novo tipo de evento `users.messages.webhook.Failure`.

* Adicionado novo tipo de evento `users.messages.webhook.Send`.

* Adicionado novo tipo de evento `users.messages.whatsapp.Abort`.

* Adicionado novo tipo de evento `users.messages.whatsapp.Click`.

* Adicionado novo tipo de evento `users.messages.whatsapp.Delivery`.

* Adicionado novo tipo de evento `users.messages.whatsapp.Failure`.

* Adicionado novo tipo de evento `users.messages.whatsapp.InboundReceive`.

* Adicionado novo tipo de evento `users.messages.whatsapp.Read`.

* Adicionado novo tipo de evento `users.messages.whatsapp.Send`.

* Adicionado novo tipo de evento `users.RandomBucketNumberUpdate`.

### Mudanças para compartilhamento de dados

* Adicionado novo tipo de evento `changelogs.GlobalControlGroup`.

* Adicionado novo tipo de evento `users.behaviors.app.FirstSession`.

* Adicionado novo tipo de evento `users.behaviors.app.NewsFeedImpression`.

* Adicionado novo tipo de evento `users.behaviors.app.SessionEnd`.

* Adicionado novo tipo de evento `users.behaviors.app.SessionStart`.

* Adicionado novo tipo de evento `users.behaviors.CustomEvent`.

* Adicionado novo tipo de evento `users.behaviors.geofence.DataEvent`.

* Adicionado novo tipo de evento `users.behaviors.geofence.RecordEvent`.

* Adicionado novo tipo de evento `users.behaviors.InstallAttribution`.

* Adicionado novo tipo de evento `users.behaviors.liveactivity.PushToStartTokenChange`.

* Adicionado novo tipo de evento `users.behaviors.liveactivity.UpdateTokenChange`.

* Adicionado novo tipo de evento `users.behaviors.Location`.

* Adicionado novo tipo de evento `users.behaviors.Purchase`.

* Adicionado novo tipo de evento `users.behaviors.pushnotification.TokenStateChange`.

* Adicionado novo tipo de evento `users.behaviors.subscription.GlobalStateChange`.

* Adicionado novo tipo de evento `users.behaviors.subscriptiongroup.StateChange`.

* Adicionado novo tipo de evento `users.behaviors.Uninstall`.

* Adicionado novo tipo de evento `users.behaviors.UpgradedApp`.

* Adicionado novo tipo de evento `users.campaigns.Conversion`.

* Adicionado novo tipo de evento `users.campaigns.EnrollInControl`.

* Adicionado novo tipo de evento `users.campaigns.FrequencyCap`.

* Adicionado novo tipo de evento `users.campaigns.Revenue`.

* Adicionado novo tipo de evento `users.canvas.Conversion`.

* Adicionado novo tipo de evento `users.canvas.Entry`.

* Adicionado novo tipo de evento `users.canvas.exit.MatchedAudience`.

* Adicionado novo tipo de evento `users.canvas.exit.PerformedEvent`.

* Adicionado novo tipo de evento `users.canvas.experimentstep.Conversion`.

* Adicionado novo tipo de evento `users.canvas.experimentstep.SplitEntry`.

* Adicionado novo tipo de evento `users.canvas.FrequencyCap`.

* Adicionado novo tipo de evento `users.canvas.Revenue`.

* Adicionado novo tipo de evento `users.canvasstep.Progression`.

* Adicionado novo tipo de evento `users.messages.banner.Abort`.

* Adicionado novo tipo de evento `users.messages.banner.Click`.

* Adicionado novo tipo de evento `users.messages.banner.Impression`.

* Adicionado novo tipo de evento `users.messages.contentcard.Abort`.

* Adicionado novo tipo de evento `users.messages.contentcard.Click`.

* Adicionado novo tipo de evento `users.messages.contentcard.Dismiss`.

* Adicionado novo tipo de evento `users.messages.contentcard.Impression`.

* Adicionado novo tipo de evento `users.messages.contentcard.Send`.

* Adicionado novo tipo de evento `users.messages.email.Abort`.

* Adicionado novo tipo de evento `users.messages.email.Bounce`.

* Adicionado novo tipo de evento `users.messages.email.Click`.

* Adicionado novo tipo de evento `users.messages.email.Deferral`.

* Adicionado novo tipo de evento `users.messages.email.Delivery`.

* Adicionado novo tipo de evento `users.messages.email.MarkAsSpam`.

* Adicionado novo tipo de evento `users.messages.email.Open`.

* Adicionado novo tipo de evento `users.messages.email.Send`.

* Adicionado novo tipo de evento `users.messages.email.SoftBounce`.

* Adicionado novo tipo de evento `users.messages.email.Unsubscribe`.

* Adicionado novo tipo de evento `users.messages.featureflag.Impression`.

* Adicionado novo tipo de evento `users.messages.inappmessage.Abort`.

* Adicionado novo tipo de evento `users.messages.inappmessage.Click`.

* Adicionado novo tipo de evento `users.messages.inappmessage.Impression`.

* Adicionado novo tipo de evento `users.messages.liveactivity.Outcome`.

* Adicionado novo tipo de evento `users.messages.liveactivity.Send`.

* Adicionado novo tipo de evento `users.messages.newsfeedcard.Abort`.

* Adicionado novo tipo de evento `users.messages.newsfeedcard.Click`.

* Adicionado novo tipo de evento `users.messages.newsfeedcard.Impression`.

* Adicionado novo tipo de evento `users.messages.pushnotification.Abort`.

* Adicionado novo tipo de evento `users.messages.pushnotification.Bounce`.

* Adicionado novo tipo de evento `users.messages.pushnotification.InfluencedOpen`.

* Adicionado novo tipo de evento `users.messages.pushnotification.IosForeground`.

* Adicionado novo tipo de evento `users.messages.pushnotification.Open`.

* Adicionado novo tipo de evento `users.messages.pushnotification.Send`.

* Adicionado novo tipo de evento `users.messages.sms.Abort`.

* Adicionado novo tipo de evento `users.messages.sms.CarrierSend`.

* Adicionado novo tipo de evento `users.messages.sms.Delivery`.

* Adicionado novo tipo de evento `users.messages.sms.DeliveryFailure`.

* Adicionado novo tipo de evento `users.messages.sms.InboundReceive`.

* Adicionado novo tipo de evento `users.messages.sms.Rejection`.

* Adicionado novo tipo de evento `users.messages.sms.Send`.

* Adicionado novo tipo de evento `users.messages.sms.ShortLinkClick`.

* Adicionado novo tipo de evento `users.messages.webhook.Abort`.

* Adicionado novo tipo de evento `users.messages.webhook.Failure`.

* Adicionado novo tipo de evento `users.messages.webhook.Send`.

* Adicionado novo tipo de evento `users.messages.whatsapp.Abort`.

* Adicionado novo tipo de evento `users.messages.whatsapp.Click`.

* Adicionado novo tipo de evento `users.messages.whatsapp.Delivery`.

* Adicionado novo tipo de evento `users.messages.whatsapp.Failure`.

* Adicionado novo tipo de evento `users.messages.whatsapp.InboundReceive`.

* Adicionado novo tipo de evento `users.messages.whatsapp.Read`.

* Adicionado novo tipo de evento `users.messages.whatsapp.Send`.

* Adicionado novo tipo de evento `users.RandomBucketNumberUpdate`.

* Adicionado novo tipo de evento `users.UserDeleteRequest`.

* Adicionado novo tipo de evento `users.UserOrphan`.
