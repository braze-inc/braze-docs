---
nav_title: Changelogs do evento Currents
page_order: 6
description: "Esta página inclui as alterações de eventos para cada versão do Currents."
tool: Currents
---

# Currents changelog

## Alterações na versão 5 (data de lançamento 2026-02-04)

* Adição de um novo tipo de evento `agentconsole.AgentExecuted`.

* Adição de um novo tipo de evento `agentconsole.ToolInvocation`.

* Adição de um novo tipo de evento `users.messages.email.Retry`.

* Adição de um novo tipo de evento `users.messages.line.Retry`.

* Adição de um novo tipo de evento `users.messages.pushnotification.Retry`.

* Adição de um novo tipo de evento `users.messages.sms.Retry`.

* Adição de um novo tipo de evento `users.messages.webhook.Retry`.

* Adição de um novo tipo de evento `users.messages.whatsapp.Retry`.

* O campo muda para o tipo de evento `users.behaviors.pushnotification.TokenStateChange`:
    * Adição do novo campo `long` `time_ms` : Tempo em milissegundos em que o evento ocorreu


## Alterações na versão 4 (data de lançamento 2026-01-08)

* O campo muda para o tipo de evento `users.behaviors.pushnotification.TokenStateChange`:
    * Adição do novo campo `string` `push_token` : Token por push do evento

* O campo muda para o tipo de evento `users.messages.pushnotification.Bounce`:
    * Adição do novo campo `string` `push_token` : Token por push do evento

* O campo muda para o tipo de evento `users.messages.pushnotification.Send`:
    * Adição do novo campo `string` `push_token` : Token por push do evento

* O campo muda para o tipo de evento `users.messages.rcs.Click`:
    * Adição do novo campo `string` `canvas_variation_name` : Nome da variante do canva recebida por este usuário
    * O campo `user_phone_number` agora é *opcional*.

* O campo muda para o tipo de evento `users.messages.rcs.InboundReceive`:
    * O campo `user_id` agora é *opcional*.

* O campo muda para o tipo de evento `users.messages.rcs.Rejection`:
    * Adição do novo campo `string` `canvas_step_message_variation_id` : API ID da variação da mensagem da etapa do canva que este usuário recebeu


## Alterações na versão 3 (data de lançamento 2025-10-08)

* Adição de um novo tipo de evento `users.messages.line.Abort`.

* Adição de um novo tipo de evento `users.messages.line.Click`.

* Adição de um novo tipo de evento `users.messages.line.InboundReceive`.

* Adição de um novo tipo de evento `users.messages.line.Send`.

* Adição de um novo tipo de evento `users.messages.rcs.Abort`.

* Adição de um novo tipo de evento `users.messages.rcs.Click`.

* Adição de um novo tipo de evento `users.messages.rcs.Delivery`.

* Adição de um novo tipo de evento `users.messages.rcs.InboundReceive`.

* Adição de um novo tipo de evento `users.messages.rcs.Read`.

* Adição de um novo tipo de evento `users.messages.rcs.Rejection`.

* Adição de um novo tipo de evento `users.messages.rcs.Send`.

* O campo muda para o tipo de evento `users.messages.sms.Delivery`:
    * Adição do novo campo `boolean` `is_sms_fallback` : Indica que uma mensagem SMS fallback foi enviada devido a uma mensagem RCS rejeitada. A mensagem pode resultar em entrega, falha de entrega ou rejeição, Ele pode ser vinculado ao evento RCS Rejection por meio de uma ID de envio e uma ID de despacho

* O campo muda para o tipo de evento `users.messages.sms.DeliveryFailure`:
    * Adição do novo campo `boolean` `is_sms_fallback` : Indica que uma mensagem SMS fallback foi enviada devido a uma mensagem RCS rejeitada. A mensagem pode resultar em entrega, falha de entrega ou rejeição, Ele pode ser vinculado ao evento RCS Rejection por meio de uma ID de envio e uma ID de despacho

* O campo muda para o tipo de evento `users.messages.sms.Rejection`:
    * Adição do novo campo `boolean` `is_sms_fallback` : Indica que uma mensagem SMS fallback foi enviada devido a uma mensagem RCS rejeitada. A mensagem pode resultar em entrega, falha de entrega ou rejeição, Ele pode ser vinculado ao evento RCS Rejection por meio de uma ID de envio e de uma ID de despacho. (Propriedade do evento)

* O campo muda para o tipo de evento `users.messages.whatsapp.Delivery`:
    * Adição do novo campo `string` `flow_id` : A ID exclusiva do fluxo no WhatsApp Manager. Presente se a mensagem incluir uma CTA para responder a um fluxo do WhatsApp
    * Adição do novo campo `string` `template_name` : [IPI] Nome do modelo no gerenciador do WhatsApp. Presente se estiver enviando uma mensagem de modelo
    * Adição do novo campo `string` `message_id` : A ID exclusiva gerada pelo Meta para essa mensagem

* O campo muda para o tipo de evento `users.messages.whatsapp.Failure`:
    * Adição do novo campo `string` `message_id` : A ID exclusiva gerada pelo Meta para essa mensagem
    * Adição do novo campo `string` `template_name` : [IPI] Nome do modelo no gerenciador do WhatsApp. Presente se estiver enviando uma mensagem de modelo
    * Adição do novo campo `string` `flow_id` : A ID exclusiva do fluxo no WhatsApp Manager. Presente se a mensagem incluir uma CTA para responder a um fluxo do WhatsApp

* O campo muda para o tipo de evento `users.messages.whatsapp.InboundReceive`:
    * Adição do novo campo `string` `catalog_id` : ID do catálogo de produto, caso um produto seja mencionado na mensagem recebida (caso contrário, permanece vazio).
    * Adição do novo campo `string` `product_id` : SKU do produto, caso um produto seja mencionado na mensagem recebida (caso contrário, permanece vazio).
    * Adição do novo campo `string` `flow_id` : A ID exclusiva do fluxo no WhatsApp Manager. Presente se o usuário estiver respondendo a um fluxo do WhatsApp.
    * Adicionado novo campo `string` `flow_response_json` : [IPI] Os valores do formulário com os quais o usuário respondeu. Presente se o usuário estiver respondendo a um fluxo do WhatsApp.
    * Adição do novo campo `string` `message_id` : A ID exclusiva gerada pelo Meta para essa mensagem
    * Adição do novo campo `string` `in_reply_to` : O endereço message_id da mensagem à qual esta mensagem estava respondendo

* O campo muda para o tipo de evento `users.messages.whatsapp.Read`:
    * Adição do novo campo `string` `template_name` : [IPI] Nome do modelo no gerenciador do WhatsApp. Presente se estiver enviando uma mensagem de modelo
    * Adição do novo campo `string` `message_id` : A ID exclusiva gerada pelo Meta para essa mensagem
    * Adição do novo campo `string` `flow_id` : A ID exclusiva do fluxo no WhatsApp Manager. Presente se a mensagem incluir uma CTA para responder a um fluxo do WhatsApp

* O campo muda para o tipo de evento `users.messages.whatsapp.Send`:
    * Adição do novo campo `string` `flow_id` : A ID exclusiva do fluxo no WhatsApp Manager. Presente se a mensagem incluir uma CTA para responder a um fluxo do WhatsApp
    * Adição do novo campo `string` `template_name` : [IPI] Nome do modelo no Gerenciador do WhatsApp. Presente se estiver enviando uma mensagem de modelo
    * Adição do novo campo `string` `message_id` : A ID exclusiva gerada pelo Meta para essa mensagem

