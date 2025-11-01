---
nav_title: Journal des modifications des événements actuels
page_order: 6
description: "Cette page comprend les modifications apportées aux événements pour chaque version de Currents."
tool: Currents
---

# Journal des modifications actuelles

## Changements dans la version 3 (date de publication 2025-10-08)

* Ajout d'un nouveau type d'événement : `users.messages.rcs.Click`.

* Ajout d'un nouveau type d'événement : `users.messages.rcs.Rejection`.

* Ajout d'un nouveau type d'événement : `users.messages.line.Abort`.

* Ajout d'un nouveau type d'événement : `users.messages.line.Send`.

* Ajout d'un nouveau type d'événement : `users.messages.line.InboundReceive`.

* Ajout d'un nouveau type d'événement : `users.messages.line.Click`.

* Ajout d'un nouveau type d'événement : `users.messages.rcs.Delivery`.

* Ajout d'un nouveau type d'événement : `users.messages.rcs.InboundReceive`.

* Ajout d'un nouveau type d'événement : `users.messages.rcs.Read`.

* Ajout d'un nouveau type d'événement : `users.messages.rcs.Send`.

* Ajout d'un nouveau type d'événement : `users.messages.rcs.Abort`.

* Le champ change pour le type d'événement `users.messages.whatsapp.Send`:
    * Ajout d'un nouveau champ `string` `flow_id` : L'ID unique du flux dans le gestionnaire WhatsApp. Présente si le message comprend un CTA pour répondre à un flux WhatsApp.
    * Ajout d'un nouveau champ `string` `template_name` : [PII] Nom du modèle dans le gestionnaire WhatsApp. Présente en cas d'envoi d'un message type
    * Ajout d'un nouveau champ `string` `message_id` : L'ID unique généré par Meta pour ce message.

* Le champ change pour le type d'événement `users.messages.whatsapp.Read`:
    * Ajout d'un nouveau champ `string` `template_name` : [PII] Nom du modèle dans le gestionnaire WhatsApp. Présente en cas d'envoi d'un message type
    * Ajout d'un nouveau champ `string` `message_id` : L'ID unique généré par Meta pour ce message.
    * Ajout d'un nouveau champ `string` `flow_id` : L'ID unique du flux dans le gestionnaire WhatsApp. Présente si le message comprend un CTA pour répondre à un flux WhatsApp.

* Le champ change pour le type d'événement `users.messages.whatsapp.InboundReceive`:
    * Ajout d'un nouveau champ `string` `catalog_id` : ID de catalogue d'un produit si un produit est référencé dans le message entrant. Sinon, il est vide.
    * Ajout d'un nouveau champ `string` `product_id` : Unité de gestion des stocks du produit si un produit est référencé dans le message entrant. Sinon, il est vide.
    * Ajout d'un nouveau champ `string` `flow_id` : L'ID unique du flux dans le gestionnaire WhatsApp. Présente si l'utilisateur répond à un flux WhatsApp.
    * Ajout d'un nouveau champ `string` `flow_response_json` : [PII] Les valeurs du formulaire auxquelles l'utilisateur a répondu. Présente si l'utilisateur répond à un flux WhatsApp.
    * Ajout d'un nouveau champ `string` `message_id` : L'ID unique généré par Meta pour ce message.
    * Ajout d'un nouveau champ `string` `in_reply_to` : Le site message_id de l'envoi de messages auquel ce message répondait

* Le champ change pour le type d'événement `users.messages.whatsapp.Failure`:
    * Ajout d'un nouveau champ `string` `message_id` : L'ID unique généré par Meta pour ce message.
    * Ajout d'un nouveau champ `string` `template_name` : [PII] Nom du modèle dans le gestionnaire WhatsApp. Présente en cas d'envoi d'un message type
    * Ajout d'un nouveau champ `string` `flow_id` : L'ID unique du flux dans le gestionnaire WhatsApp. Présente si le message comprend un CTA pour répondre à un flux WhatsApp.

* Le champ change pour le type d'événement `users.messages.whatsapp.Delivery`:
    * Ajout d'un nouveau champ `string` `flow_id` : L'ID unique du flux dans le gestionnaire WhatsApp. Présente si le message comprend un CTA pour répondre à un flux WhatsApp.
    * Ajout d'un nouveau champ `string` `template_name` : [PII] Nom du modèle dans le gestionnaire WhatsApp. Présente en cas d'envoi d'un message type
    * Ajout d'un nouveau champ `string` `message_id` : L'ID unique généré par Meta pour ce message.

* Le champ change pour le type d'événement `users.messages.sms.Rejection`:
    * Ajout d'un nouveau champ `boolean` `is_sms_fallback` : Indique qu'un message SMS de secours a été envoyé en raison d'un message RCS rejeté. Le message peut donner lieu à une réception/distribution ou à un rejet. Il peut être lié à l'événement de rejet du RCS par l'intermédiaire d'un ID d'envoi et d'un ID d'expédition.
Il peut être lié à l'événement de rejet du RCS par l'intermédiaire d'un ID d'envoi et d'un ID de distribution. (propriétés d'événement)

* Le champ change pour le type d'événement `users.messages.sms.DeliveryFailure`:
    * Ajout d'un nouveau champ `boolean` `is_sms_fallback` : Indique qu'un message SMS de secours a été envoyé en raison d'un message RCS rejeté. Le message peut donner lieu à une réception/distribution ou à un rejet. Il peut être lié à l'événement de rejet du RCS par l'intermédiaire d'un ID d'envoi et d'un ID d'expédition.

* Le champ change pour le type d'événement `users.messages.sms.Delivery`:
    * Ajout d'un nouveau champ `boolean` `is_sms_fallback` : Indique qu'un message SMS de secours a été envoyé en raison d'un message RCS rejeté. Le message peut donner lieu à une réception/distribution ou à un rejet. Il peut être lié à l'événement de rejet du RCS par l'intermédiaire d'un ID d'envoi et d'un ID d'expédition.

