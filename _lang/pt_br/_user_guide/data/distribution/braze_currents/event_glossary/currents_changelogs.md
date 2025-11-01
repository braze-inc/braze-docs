---
nav_title: Registros de alterações do evento Currents
page_order: 6
description: "Esta página inclui as alterações de eventos para cada versão do Currents."
tool: Currents
---

# Registro de mudanças atual

## Alterações na versão 3 (data de lançamento 2025-10-08)

* Adição de um novo tipo de evento `users.messages.rcs.Click`.

* Adição de um novo tipo de evento `users.messages.rcs.Rejection`.

* Adição de um novo tipo de evento `users.messages.line.Abort`.

* Adição de um novo tipo de evento `users.messages.line.Send`.

* Adição de um novo tipo de evento `users.messages.line.InboundReceive`.

* Adição de um novo tipo de evento `users.messages.line.Click`.

* Adição de um novo tipo de evento `users.messages.rcs.Delivery`.

* Adição de um novo tipo de evento `users.messages.rcs.InboundReceive`.

* Adição de um novo tipo de evento `users.messages.rcs.Read`.

* Adição de um novo tipo de evento `users.messages.rcs.Send`.

* Adição de um novo tipo de evento `users.messages.rcs.Abort`.

* O campo muda para o tipo de evento `users.messages.whatsapp.Send`:
    * Adição do novo campo `string` `flow_id` : A ID exclusiva do fluxo no WhatsApp Manager. Presente se a mensagem incluir uma CTA para responder a um fluxo do WhatsApp
    * Adição do novo campo `string` `template_name` : [PII] Nome do modelo no Gerenciador do WhatsApp. Presente se estiver enviando uma mensagem de modelo
    * Adição do novo campo `string` `message_id` : A ID exclusiva gerada pelo Meta para essa mensagem

* O campo muda para o tipo de evento `users.messages.whatsapp.Read`:
    * Adição do novo campo `string` `template_name` : [PII] Nome do modelo no gerenciador do WhatsApp. Presente se estiver enviando uma mensagem de modelo
    * Adição do novo campo `string` `message_id` : A ID exclusiva gerada pelo Meta para essa mensagem
    * Adição do novo campo `string` `flow_id` : A ID exclusiva do fluxo no WhatsApp Manager. Presente se a mensagem incluir uma CTA para responder a um fluxo do WhatsApp

* O campo muda para o tipo de evento `users.messages.whatsapp.InboundReceive`:
    * Adição do novo campo `string` `catalog_id` : ID do catálogo de um produto, se houver referência a um produto na mensagem de entrada. Caso contrário, vazio.
    * Adição do novo campo `string` `product_id` : SKU do produto, se houver referência a um produto na mensagem recebida. Caso contrário, vazio.
    * Adição do novo campo `string` `flow_id` : A ID exclusiva do fluxo no WhatsApp Manager. Presente se o usuário estiver respondendo a um fluxo do WhatsApp.
    * Adicionado novo campo `string` `flow_response_json` : [PII] Os valores do formulário com os quais o usuário respondeu. Presente se o usuário estiver respondendo a um fluxo do WhatsApp.
    * Adição do novo campo `string` `message_id` : A ID exclusiva gerada pelo Meta para essa mensagem
    * Adição do novo campo `string` `in_reply_to` : O endereço message_id da mensagem à qual esta mensagem estava respondendo

* O campo muda para o tipo de evento `users.messages.whatsapp.Failure`:
    * Adição do novo campo `string` `message_id` : A ID exclusiva gerada pelo Meta para essa mensagem
    * Adição do novo campo `string` `template_name` : [PII] Nome do modelo no gerenciador do WhatsApp. Presente se estiver enviando uma mensagem de modelo
    * Adição do novo campo `string` `flow_id` : A ID exclusiva do fluxo no WhatsApp Manager. Presente se a mensagem incluir uma CTA para responder a um fluxo do WhatsApp

* O campo muda para o tipo de evento `users.messages.whatsapp.Delivery`:
    * Adição do novo campo `string` `flow_id` : A ID exclusiva do fluxo no WhatsApp Manager. Presente se a mensagem incluir uma CTA para responder a um fluxo do WhatsApp
    * Adição do novo campo `string` `template_name` : [PII] Nome do modelo no gerenciador do WhatsApp. Presente se estiver enviando uma mensagem de modelo
    * Adição do novo campo `string` `message_id` : A ID exclusiva gerada pelo Meta para essa mensagem

* O campo muda para o tipo de evento `users.messages.sms.Rejection`:
    * Adição do novo campo `boolean` `is_sms_fallback` : Indica que uma mensagem de SMS fallback foi enviada devido a uma mensagem RCS rejeitada. A mensagem pode resultar em entrega, falha na entrega ou rejeição. Ele pode ser vinculado ao evento RCS Rejection por meio de uma ID de envio e uma ID de despacho
Ele pode ser vinculado ao evento RCS Rejection por meio de uma ID de envio e uma ID de despacho. (Propriedade do evento)

* O campo muda para o tipo de evento `users.messages.sms.DeliveryFailure`:
    * Adição do novo campo `boolean` `is_sms_fallback` : Indica que uma mensagem de SMS fallback foi enviada devido a uma mensagem RCS rejeitada. A mensagem pode resultar em entrega, falha na entrega ou rejeição. Ele pode ser vinculado ao evento RCS Rejection por meio de uma ID de envio e uma ID de despacho

* O campo muda para o tipo de evento `users.messages.sms.Delivery`:
    * Adição do novo campo `boolean` `is_sms_fallback` : Indica que uma mensagem de SMS fallback foi enviada devido a uma mensagem RCS rejeitada. A mensagem pode resultar em entrega, falha na entrega ou rejeição. Ele pode ser vinculado ao evento RCS Rejection por meio de uma ID de envio e uma ID de despacho

