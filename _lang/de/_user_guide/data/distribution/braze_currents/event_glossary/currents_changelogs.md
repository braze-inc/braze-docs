---
nav_title: Currents Ereignis-Changelogs
page_order: 6
description: "Diese Seite enthält die Ereignisänderungen für jede Currents-Version."
tool: Currents
---

# Currents Changelog

## Änderungen in Version 5 (Veröffentlichungsdatum 2026-02-04)

* Neuer Ereignistyp `agentconsole.AgentExecuted` hinzugefügt.

* Neuer Ereignistyp `agentconsole.ToolInvocation` hinzugefügt.

* Neuer Ereignistyp `users.messages.email.Retry` hinzugefügt.

* Neuer Ereignistyp `users.messages.line.Retry` hinzugefügt.

* Neuer Ereignistyp `users.messages.pushnotification.Retry` hinzugefügt.

* Neuer Ereignistyp `users.messages.sms.Retry` hinzugefügt.

* Neuer Ereignistyp `users.messages.webhook.Retry` hinzugefügt.

* Neuer Ereignistyp `users.messages.whatsapp.Retry` hinzugefügt.

* Das Feld wechselt zum Ereignistyp `users.behaviors.pushnotification.TokenStateChange`:
    * Neues Feld `long` hinzugefügt `time_ms`: Zeitpunkt in Millisekunden, zu dem das Ereignis eintrat


## Änderungen in Version 4 (Erscheinungsdatum 2026-01-08)

* Das Feld wechselt zum Ereignistyp `users.behaviors.pushnotification.TokenStateChange`:
    * Neues Feld `string` hinzugefügt `push_token`: Push-Token des Ereignisses

* Das Feld wechselt zum Ereignistyp `users.messages.pushnotification.Bounce`:
    * Neues Feld `string` hinzugefügt `push_token`: Push-Token des Ereignisses

* Das Feld wechselt zum Ereignistyp `users.messages.pushnotification.Send`:
    * Neues Feld `string` hinzugefügt `push_token`: Push-Token des Ereignisses

* Das Feld wechselt zum Ereignistyp `users.messages.rcs.Click`:
    * Neues Feld `string` hinzugefügt `canvas_variation_name`: Name der Canvas-Variante, die dieser Nutzer:in erhalten hat
    * Das Feld `user_phone_number` ist jetzt *optional*.

* Das Feld wechselt zum Ereignistyp `users.messages.rcs.InboundReceive`:
    * Das Feld `user_id` ist jetzt *optional*.

* Das Feld wechselt zum Ereignistyp `users.messages.rcs.Rejection`:
    * Neues Feld `string` hinzugefügt `canvas_step_message_variation_id`: API-ID der Canvas-Schritt-Nachrichtenvariante, die dieser Benutzer erhalten hat


## Änderungen in Version 3 (Erscheinungsdatum 2025-10-08)

* Neuer Ereignistyp `users.messages.line.Abort` hinzugefügt.

* Neuer Ereignistyp `users.messages.line.Click` hinzugefügt.

* Neuer Ereignistyp `users.messages.line.InboundReceive` hinzugefügt.

* Neuer Ereignistyp `users.messages.line.Send` hinzugefügt.

* Neuer Ereignistyp `users.messages.rcs.Abort` hinzugefügt.

* Neuer Ereignistyp `users.messages.rcs.Click` hinzugefügt.

* Neuer Ereignistyp `users.messages.rcs.Delivery` hinzugefügt.

* Neuer Ereignistyp `users.messages.rcs.InboundReceive` hinzugefügt.

* Neuer Ereignistyp `users.messages.rcs.Read` hinzugefügt.

* Neuer Ereignistyp `users.messages.rcs.Rejection` hinzugefügt.

* Neuer Ereignistyp `users.messages.rcs.Send` hinzugefügt.

* Das Feld wechselt zum Ereignistyp `users.messages.sms.Delivery`:
    * Neues Feld `boolean` hinzugefügt `is_sms_fallback`: Zeigt an, dass eine SMS-Fallback-Nachricht aufgrund einer abgelehnten RCS Nachricht gesendet wurde. Die Nachricht könnte zu einer Zustellung, einem Zustellungsfehler oder einer Ablehnung führen. Es kann über eine Sende-ID und eine Versand-ID mit dem RCS-Ablehnungsereignis verknüpft werden

* Das Feld wechselt zum Ereignistyp `users.messages.sms.DeliveryFailure`:
    * Neues Feld `boolean` hinzugefügt `is_sms_fallback`: Zeigt an, dass eine SMS-Fallback-Nachricht aufgrund einer abgelehnten RCS Nachricht gesendet wurde. Die Nachricht könnte zu einer Zustellung, einem Zustellungsfehler oder einer Ablehnung führen. Es kann über eine Sende-ID und eine Versand-ID mit dem RCS-Ablehnungsereignis verknüpft werden

* Das Feld wechselt zum Ereignistyp `users.messages.sms.Rejection`:
    * Neues Feld `boolean` hinzugefügt `is_sms_fallback`: Zeigt an, dass eine SMS-Fallback-Nachricht aufgrund einer abgelehnten RCS Nachricht gesendet wurde. Die Nachricht könnte zu einer Zustellung, einem Zustellungsfehler oder einer Ablehnung führen. Es kann über eine Sende-ID und eine Versand-ID mit dem RCS-Ablehnungsereignis verknüpft werden. Es kann über eine Sende-ID und eine Versand-ID mit dem RCS-Ablehnungsereignis verknüpft werden. (Event-Eigenschaften)

* Das Feld wechselt zum Ereignistyp `users.messages.whatsapp.Delivery`:
    * Neues Feld `string` hinzugefügt `flow_id`: Die eindeutige ID des Flows im WhatsApp Manager:in. Vorhanden, wenn die Nachricht eine CTA enthält, um auf einen WhatsApp Flow zu antworten
    * Neues Feld `string` hinzugefügt `template_name`: [PII] Name des Templates im WhatsApp Manager. Vorhanden, wenn Sie eine Template Nachricht senden
    * Neues Feld `string` hinzugefügt `message_id`: Die eindeutige ID, die von Meta für diese Nachricht generiert wurde

* Das Feld wechselt zum Ereignistyp `users.messages.whatsapp.Failure`:
    * Neues Feld `string` hinzugefügt `message_id`: Die eindeutige ID, die von Meta für diese Nachricht generiert wurde
    * Neues Feld `string` hinzugefügt `template_name`: [PII] Name des Templates im WhatsApp Manager. Vorhanden, wenn Sie eine Template Nachricht senden
    * Neues Feld `string` hinzugefügt `flow_id`: Die eindeutige ID des Flows im WhatsApp Manager:in. Vorhanden, wenn die Nachricht eine CTA enthält, um auf einen WhatsApp Flow zu antworten

* Das Feld wechselt zum Ereignistyp `users.messages.whatsapp.InboundReceive`:
    * Neues Feld `string` hinzugefügt `catalog_id`: Katalog ID eines Produkts, wenn ein Produkt in der eingehenden Nachricht referenziert wird. Andernfalls ist sie leer.
    * Neues Feld `string` hinzugefügt `product_id`: Produkt SKU, wenn ein Produkt in der eingehenden Nachricht referenziert wird. Andernfalls ist sie leer.
    * Neues Feld `string` hinzugefügt `flow_id`: Die eindeutige ID des Flows im WhatsApp Manager:in. Vorhanden, wenn der Nutzer:in auf einen WhatsApp Flow antwortet.
    * Neues Feld `string` hinzugefügt `flow_response_json`: [PII] Die Formularwerte, mit denen der Nutzer:innen geantwortet hat. Vorhanden, wenn der Nutzer:in auf einen WhatsApp Flow antwortet.
    * Neues Feld `string` hinzugefügt `message_id`: Die eindeutige ID, die von Meta für diese Nachricht generiert wurde
    * Neues Feld `string` hinzugefügt `in_reply_to`: Die message_id der Nachricht, auf die diese Nachricht geantwortet hat

* Das Feld wechselt zum Ereignistyp `users.messages.whatsapp.Read`:
    * Neues Feld `string` hinzugefügt `template_name`: [PII] Name des Templates im WhatsApp Manager. Vorhanden, wenn Sie eine Template Nachricht senden
    * Neues Feld `string` hinzugefügt `message_id`: Die eindeutige ID, die von Meta für diese Nachricht generiert wurde
    * Neues Feld `string` hinzugefügt `flow_id`: Die eindeutige ID des Flows im WhatsApp Manager:in. Vorhanden, wenn die Nachricht eine CTA enthält, um auf einen WhatsApp Flow zu antworten

* Das Feld wechselt zum Ereignistyp `users.messages.whatsapp.Send`:
    * Neues Feld `string` hinzugefügt `flow_id`: Die eindeutige ID des Flows im WhatsApp Manager:in. Vorhanden, wenn die Nachricht eine CTA enthält, um auf einen WhatsApp Flow zu antworten
    * Neues Feld `string` hinzugefügt `template_name`: [PII] Name des Templates im WhatsApp Manager. Vorhanden, wenn Sie eine Template Nachricht senden
    * Neues Feld `string` hinzugefügt `message_id`: Die eindeutige ID, die von Meta für diese Nachricht generiert wurde

