---
nav_title: Currents Changelogs
page_order: 6
description: "Diese Seite enthält die Änderungen an den Ereignissen für jede Currents-Version."
tool: Currents
---

# Aktuelles Changelog für Currents

## Änderungen in Version 6 (Veröffentlichungsdatum 04.03.2026)

### Änderungen für die Lagerung

* Änderungen am Feld „Veranstaltungstyp`agentconsole.AgentExecuted`“:
    * Neues`string`Feld `error`hinzugefügt: Beschreibung des Fehlers

* Änderungen am Feld „Veranstaltungstyp`agentconsole.ToolInvocation`“:
    * Neues`string`Feld `request_id`hinzugefügt: eindeutige ID für diese gesamte LLM-Anfrage und vollständige Ausführung.

* Änderungen am Feld „Veranstaltungstyp`users.messages.rcs.InboundReceive`“:
    * Neues`string`Feld `canvas_variation_name`hinzugefügt: Name der Canvas-Variante, die diese Nutzer:in erhalten hat

### Änderungen für den Datenaustausch

* Änderungen am Feld „Veranstaltungstyp`agentconsole.AgentExecuted`“:
    * Neues`string`Feld `canvas_name`hinzugefügt: Name des Canvas
    * Neues`string`Feld `canvas_variation_name`hinzugefügt: Name der Canvas-Variante, die diese Nutzer:in erhalten hat
    * Neues`string`Feld `canvas_step_name`hinzugefügt: Name des Canvas-Schritts
    * Neues`string`Feld `error`hinzugefügt: Fehlername

* Änderungen am Feld „Veranstaltungstyp`agentconsole.ToolInvocation`“:
    * Neues`string`Feld `request_id`hinzugefügt: eindeutige ID für diese gesamte LLM-Anfrage und vollständige Ausführung.

* Änderungen am Feld „Veranstaltungstyp`users.behaviors.subscription.GlobalStateChange`“:
    * Neues`string`Feld `campaign_name`hinzugefügt: Name der Kampagne
    * Neues`string`Feld `message_variation_name`hinzugefügt: Name der Nachricht
    * Neues`string`Feld `canvas_name`hinzugefügt: Name des Canvas
    * Neues`string`Feld `canvas_variation_name`hinzugefügt: Name der Canvas-Variante, die diese Nutzer:in erhalten hat
    * Neues`string`Feld `canvas_step_name`hinzugefügt: Name des Canvas-Schritts

* Änderungen am Feld „Veranstaltungstyp`users.behaviors.subscriptiongroup.StateChange`“:
    * Neues`string`Feld `campaign_name`hinzugefügt: Name der Kampagne
    * Neues`string`Feld `message_variation_name`hinzugefügt: Name der Nachricht
    * Neues`string`Feld `canvas_name`hinzugefügt: Name des Canvas
    * Neues`string`Feld `canvas_variation_name`hinzugefügt: Name der Canvas-Variante, die diese Nutzer:in erhalten hat
    * Neues`string`Feld `canvas_step_name`hinzugefügt: Name des Canvas-Schritts

* Änderungen am Feld „Veranstaltungstyp`users.campaigns.Conversion`“:
    * Neues`string`Feld `campaign_name`hinzugefügt: Name der Kampagne
    * Neues`string`Feld `message_variation_name`hinzugefügt: Name der Nachricht
    * Neues`string`Feld `conversion_behavior`hinzugefügt: JSON-kodierte String-Zeichenfolge, die das Verhalten bei der Konversion beschreibt

* Änderungen am Feld „Veranstaltungstyp`users.campaigns.EnrollInControl`“:
    * Neues`string`Feld `campaign_name`hinzugefügt: Name der Kampagne
    * Neues`string`Feld `message_variation_name`hinzugefügt: Name der Nachricht

* Änderungen am Feld „Veranstaltungstyp`users.canvas.Conversion`“:
    * Neues`string`Feld `canvas_name`hinzugefügt: Name des Canvas
    * Neues`string`Feld `canvas_variation_name`hinzugefügt: Name der Canvas-Variante, die diese Nutzer:in erhalten hat
    * Neues`string`Feld `canvas_step_name`hinzugefügt: Name des Canvas-Schritts
    * Neues`string`Feld `conversion_behavior`hinzugefügt: JSON-kodierte String-Zeichenfolge, die das Verhalten bei der Konversion beschreibt

* Änderungen am Feld „Veranstaltungstyp`users.canvas.Entry`“:
    * Neues`string`Feld `canvas_name`hinzugefügt: Name des Canvas
    * Neues`string`Feld `canvas_variation_name`hinzugefügt: Name der Canvas-Variante, die diese Nutzer:in erhalten hat
    * Neues`string`Feld `canvas_step_name`hinzugefügt: Name des Canvas-Schritts

* Änderungen am Feld „Veranstaltungstyp`users.canvas.exit.MatchedAudience`“:
    * Neues`string`Feld `canvas_name`hinzugefügt: Name des Canvas
    * Neues`string`Feld `canvas_variation_name`hinzugefügt: Name der Canvas-Variante, die diese Nutzer:in erhalten hat
    * Neues`string`Feld `canvas_step_name`hinzugefügt: Name des Canvas-Schritts

* Änderungen am Feld „Veranstaltungstyp`users.canvas.exit.PerformedEvent`“:
    * Neues`string`Feld `canvas_name`hinzugefügt: Name des Canvas
    * Neues`string`Feld `canvas_variation_name`hinzugefügt: Name der Canvas-Variante, die diese Nutzer:in erhalten hat
    * Neues`string`Feld `canvas_step_name`hinzugefügt: Name des Canvas-Schritts

* Änderungen am Feld „Veranstaltungstyp`users.canvas.experimentstep.Conversion`“:
    * Neues`string`Feld `canvas_name`hinzugefügt: Name des Canvas
    * Neues`string`Feld `canvas_variation_name`hinzugefügt: Name der Canvas-Variante, die diese Nutzer:in erhalten hat
    * Neues`string`Feld `canvas_step_name`hinzugefügt: Name des Canvas-Schritts
    * Neues`string`Feld `experiment_split_name`hinzugefügt: Name des Experiments
    * Neues`string`Feld `conversion_behavior`hinzugefügt: JSON-kodierte String-Zeichenfolge, die das Verhalten bei der Konversion beschreibt

* Änderungen am Feld „Veranstaltungstyp`users.canvas.experimentstep.SplitEntry`“:
    * Neues`string`Feld `canvas_name`hinzugefügt: Name des Canvas
    * Neues`string`Feld `canvas_variation_name`hinzugefügt: Name der Canvas-Variante, die diese Nutzer:in erhalten hat
    * Neues`string`Feld `canvas_step_name`hinzugefügt: Name des Canvas-Schritts
    * Neues`string`Feld `experiment_split_name`hinzugefügt: Name des Experiments

* Änderungen am Feld „Veranstaltungstyp`users.canvasstep.Progression`“:
    * Neues`string`Feld `canvas_name`hinzugefügt: Name des Canvas
    * Neues`string`Feld `canvas_variation_name`hinzugefügt: Name der Canvas-Variante, die diese Nutzer:in erhalten hat
    * Neues`string`Feld `canvas_step_name`hinzugefügt: Name des Canvas-Schritts

* Änderungen am Feld „Veranstaltungstyp`users.messages.banner.Abort`“:
    * Neues`string`Feld `campaign_name`hinzugefügt: Name der Kampagne
    * Neues`string`Feld `message_variation_name`hinzugefügt: Name der Nachricht

* Änderungen am Feld „Veranstaltungstyp`users.messages.banner.Click`“:
    * Neues`string`Feld `campaign_name`hinzugefügt: Name der Kampagne
    * Neues`string`Feld `message_variation_name`hinzugefügt: Name der Nachricht

* Änderungen am Feld „Veranstaltungstyp`users.messages.banner.Impression`“:
    * Neues`string`Feld `campaign_name`hinzugefügt: Name der Kampagne
    * Neues`string`Feld `message_variation_name`hinzugefügt: Name der Nachricht

* Änderungen am Feld „Veranstaltungstyp`users.messages.contentcard.Abort`“:
    * Neues`string`Feld `campaign_name`hinzugefügt: Name der Kampagne
    * Neues`string`Feld `message_variation_name`hinzugefügt: Name der Nachricht
    * Neues`string`Feld `canvas_name`hinzugefügt: Name des Canvas
    * Neues`string`Feld `canvas_variation_name`hinzugefügt: Name der Canvas-Variante, die diese Nutzer:in erhalten hat
    * Neues`string`Feld `canvas_step_name`hinzugefügt: Name des Canvas-Schritts

* Änderungen am Feld „Veranstaltungstyp`users.messages.contentcard.Click`“:
    * Neues`string`Feld `campaign_name`hinzugefügt: Name der Kampagne
    * Neues`string`Feld `message_variation_name`hinzugefügt: Name der Nachricht
    * Neues`string`Feld `canvas_name`hinzugefügt: Name des Canvas
    * Neues`string`Feld `canvas_variation_name`hinzugefügt: Name der Canvas-Variante, die diese Nutzer:in erhalten hat
    * Neues`string`Feld `canvas_step_name`hinzugefügt: Name des Canvas-Schritts

* Änderungen am Feld „Veranstaltungstyp`users.messages.contentcard.Dismiss`“:
    * Neues`string`Feld `campaign_name`hinzugefügt: Name der Kampagne
    * Neues`string`Feld `message_variation_name`hinzugefügt: Name der Nachricht
    * Neues`string`Feld `canvas_name`hinzugefügt: Name des Canvas
    * Neues`string`Feld `canvas_variation_name`hinzugefügt: Name der Canvas-Variante, die diese Nutzer:in erhalten hat
    * Neues`string`Feld `canvas_step_name`hinzugefügt: Name des Canvas-Schritts

* Änderungen am Feld „Veranstaltungstyp`users.messages.contentcard.Impression`“:
    * Neues`string`Feld `campaign_name`hinzugefügt: Name der Kampagne
    * Neues`string`Feld `message_variation_name`hinzugefügt: Name der Nachricht
    * Neues`string`Feld `canvas_name`hinzugefügt: Name des Canvas
    * Neues`string`Feld `canvas_variation_name`hinzugefügt: Name der Canvas-Variante, die diese Nutzer:in erhalten hat
    * Neues`string`Feld `canvas_step_name`hinzugefügt: Name des Canvas-Schritts

* Änderungen am Feld „Veranstaltungstyp`users.messages.contentcard.Send`“:
    * Neues`string`Feld `campaign_name`hinzugefügt: Name der Kampagne
    * Neues`string`Feld `message_variation_name`hinzugefügt: Name der Nachricht
    * Neues`string`Feld `canvas_name`hinzugefügt: Name des Canvas
    * Neues`string`Feld `canvas_variation_name`hinzugefügt: Name der Canvas-Variante, die diese Nutzer:in erhalten hat
    * Neues`string`Feld `canvas_step_name`hinzugefügt: Name des Canvas-Schritts

* Änderungen am Feld „Veranstaltungstyp`users.messages.email.Abort`“:
    * Neues`string`Feld `campaign_name`hinzugefügt: Name der Kampagne
    * Neues`string`Feld `message_variation_name`hinzugefügt: Name der Nachricht
    * Neues`string`Feld `canvas_name`hinzugefügt: Name des Canvas
    * Neues`string`Feld `canvas_variation_name`hinzugefügt: Name der Canvas-Variante, die diese Nutzer:in erhalten hat
    * Neues`string`Feld `canvas_step_name`hinzugefügt: Name des Canvas-Schritts

* Änderungen am Feld „Veranstaltungstyp`users.messages.email.Bounce`“:
    * Neues`string`Feld `campaign_name`hinzugefügt: Name der Kampagne
    * Neues`string`Feld `message_variation_name`hinzugefügt: Name der Nachricht
    * Neues`string`Feld `canvas_name`hinzugefügt: Name des Canvas
    * Neues`string`Feld `canvas_variation_name`hinzugefügt: Name der Canvas-Variante, die diese Nutzer:in erhalten hat
    * Neues`string`Feld `canvas_step_name`hinzugefügt: Name des Canvas-Schritts

* Änderungen am Feld „Veranstaltungstyp`users.messages.email.Click`“:
    * Neues`string`Feld `campaign_name`hinzugefügt: Name der Kampagne
    * Neues`string`Feld `message_variation_name`hinzugefügt: Name der Nachricht
    * Neues`string`Feld `canvas_name`hinzugefügt: Name des Canvas
    * Neues`string`Feld `canvas_variation_name`hinzugefügt: Name der Canvas-Variante, die diese Nutzer:in erhalten hat
    * Neues`string`Feld `canvas_step_name`hinzugefügt: Name des Canvas-Schritts

* Änderungen am Feld „Veranstaltungstyp`users.messages.email.Deferral`“:
    * Neues`string`Feld `campaign_name`hinzugefügt: Name der Kampagne
    * Neues`string`Feld `message_variation_name`hinzugefügt: Name der Nachricht
    * Neues`string`Feld `canvas_name`hinzugefügt: Name des Canvas
    * Neues`string`Feld `canvas_variation_name`hinzugefügt: Name der Canvas-Variante, die diese Nutzer:in erhalten hat
    * Neues`string`Feld `canvas_step_name`hinzugefügt: Name des Canvas-Schritts

* Änderungen am Feld „Veranstaltungstyp`users.messages.email.Delivery`“:
    * Neues`string`Feld `campaign_name`hinzugefügt: Name der Kampagne
    * Neues`string`Feld `message_variation_name`hinzugefügt: Name der Nachricht
    * Neues`string`Feld `canvas_name`hinzugefügt: Name des Canvas
    * Neues`string`Feld `canvas_variation_name`hinzugefügt: Name der Canvas-Variante, die diese Nutzer:in erhalten hat
    * Neues`string`Feld `canvas_step_name`hinzugefügt: Name des Canvas-Schritts

* Änderungen am Feld „Veranstaltungstyp`users.messages.email.MarkAsSpam`“:
    * Neues`string`Feld `campaign_name`hinzugefügt: Name der Kampagne
    * Neues`string`Feld `message_variation_name`hinzugefügt: Name der Nachricht
    * Neues`string`Feld `canvas_name`hinzugefügt: Name des Canvas
    * Neues`string`Feld `canvas_variation_name`hinzugefügt: Name der Canvas-Variante, die diese Nutzer:in erhalten hat
    * Neues`string`Feld `canvas_step_name`hinzugefügt: Name des Canvas-Schritts

* Änderungen am Feld „Veranstaltungstyp`users.messages.email.Open`“:
    * Neues`string`Feld `campaign_name`hinzugefügt: Name der Kampagne
    * Neues`string`Feld `message_variation_name`hinzugefügt: Name der Nachricht
    * Neues`string`Feld `canvas_name`hinzugefügt: Name des Canvas
    * Neues`string`Feld `canvas_variation_name`hinzugefügt: Name der Canvas-Variante, die diese Nutzer:in erhalten hat
    * Neues`string`Feld `canvas_step_name`hinzugefügt: Name des Canvas-Schritts

* Änderungen am Feld „Veranstaltungstyp`users.messages.email.Retry`“:
    * Neues`string`Feld `campaign_name`hinzugefügt: Name der Kampagne
    * Neues`string`Feld `message_variation_name`hinzugefügt: Name der Nachricht
    * Neues`string`Feld `canvas_name`hinzugefügt: Name des Canvas
    * Neues`string`Feld `canvas_variation_name`hinzugefügt: Name der Canvas-Variante, die diese Nutzer:in erhalten hat
    * Neues`string`Feld `canvas_step_name`hinzugefügt: Name des Canvas-Schritts

* Änderungen am Feld „Veranstaltungstyp`users.messages.email.Send`“:
    * Neues`string`Feld `campaign_name`hinzugefügt: Name der Kampagne
    * Neues`string`Feld `message_variation_name`hinzugefügt: Name der Nachricht
    * Neues`string`Feld `canvas_name`hinzugefügt: Name des Canvas
    * Neues`string`Feld `canvas_variation_name`hinzugefügt: Name der Canvas-Variante, die diese Nutzer:in erhalten hat
    * Neues`string`Feld `canvas_step_name`hinzugefügt: Name des Canvas-Schritts

* Änderungen am Feld „Veranstaltungstyp`users.messages.email.SoftBounce`“:
    * Neues`string`Feld `campaign_name`hinzugefügt: Name der Kampagne
    * Neues`string`Feld `message_variation_name`hinzugefügt: Name der Nachricht
    * Neues`string`Feld `canvas_name`hinzugefügt: Name des Canvas
    * Neues`string`Feld `canvas_variation_name`hinzugefügt: Name der Canvas-Variante, die diese Nutzer:in erhalten hat
    * Neues`string`Feld `canvas_step_name`hinzugefügt: Name des Canvas-Schritts

* Änderungen am Feld „Veranstaltungstyp`users.messages.email.Unsubscribe`“:
    * Neues`string`Feld `campaign_name`hinzugefügt: Name der Kampagne
    * Neues`string`Feld `message_variation_name`hinzugefügt: Name der Nachricht
    * Neues`string`Feld `canvas_name`hinzugefügt: Name des Canvas
    * Neues`string`Feld `canvas_variation_name`hinzugefügt: Name der Canvas-Variante, die diese Nutzer:in erhalten hat
    * Neues`string`Feld `canvas_step_name`hinzugefügt: Name des Canvas-Schritts

* Änderungen am Feld „Veranstaltungstyp`users.messages.featureflag.Impression`“:
    * Neues`string`Feld `campaign_name`hinzugefügt: Name der Kampagne
    * Neues`string`Feld `canvas_name`hinzugefügt: Name des Canvas
    * Neues`string`Feld `canvas_step_name`hinzugefügt: Name des Canvas-Schritts
    * Neues`string`Feld `canvas_variation_name`hinzugefügt: Name der Canvas-Variante, die diese Nutzer:in erhalten hat
    * Neues`string`Feld `message_variation_name`hinzugefügt: Name der Nachricht

* Änderungen am Feld „Veranstaltungstyp`users.messages.inappmessage.Abort`“:
    * Neues`string`Feld `campaign_name`hinzugefügt: Name der Kampagne
    * Neues`string`Feld `message_variation_name`hinzugefügt: Name der Nachricht
    * Neues`string`Feld `canvas_name`hinzugefügt: Name des Canvas
    * Neues`string`Feld `canvas_variation_name`hinzugefügt: Name der Canvas-Variante, die diese Nutzer:in erhalten hat
    * Neues`string`Feld `canvas_step_name`hinzugefügt: Name des Canvas-Schritts

* Änderungen am Feld „Veranstaltungstyp`users.messages.inappmessage.Click`“:
    * Neues`string`Feld `campaign_name`hinzugefügt: Name der Kampagne
    * Neues`string`Feld `message_variation_name`hinzugefügt: Name der Nachricht
    * Neues`string`Feld `canvas_name`hinzugefügt: Name des Canvas
    * Neues`string`Feld `canvas_variation_name`hinzugefügt: Name der Canvas-Variante, die diese Nutzer:in erhalten hat
    * Neues`string`Feld `canvas_step_name`hinzugefügt: Name des Canvas-Schritts

* Änderungen am Feld „Veranstaltungstyp`users.messages.inappmessage.Impression`“:
    * Neues`string`Feld `campaign_name`hinzugefügt: Name der Kampagne
    * Neues`string`Feld `message_variation_name`hinzugefügt: Name der Nachricht
    * Neues`string`Feld `canvas_name`hinzugefügt: Name des Canvas
    * Neues`string`Feld `canvas_variation_name`hinzugefügt: Name der Canvas-Variante, die diese Nutzer:in erhalten hat
    * Neues`string`Feld `canvas_step_name`hinzugefügt: Name des Canvas-Schritts

* Änderungen am Feld „Veranstaltungstyp`users.messages.line.Retry`“:
    * Neues`string`Feld `campaign_name`hinzugefügt: Name der Kampagne
    * Neues`string`Feld `canvas_step_name`hinzugefügt: Name des Canvas-Schritts

* Änderungen am Feld „Veranstaltungstyp`users.messages.pushnotification.Abort`“:
    * Neues`string`Feld `campaign_name`hinzugefügt: Name der Kampagne
    * Neues`string`Feld `message_variation_name`hinzugefügt: Name der Nachricht
    * Neues`string`Feld `canvas_name`hinzugefügt: Name des Canvas
    * Neues`string`Feld `canvas_variation_name`hinzugefügt: Name der Canvas-Variante, die diese Nutzer:in erhalten hat
    * Neues`string`Feld `canvas_step_name`hinzugefügt: Name des Canvas-Schritts

* Änderungen am Feld „Veranstaltungstyp`users.messages.pushnotification.Bounce`“:
    * Neues`string`Feld `campaign_name`hinzugefügt: Name der Kampagne
    * Neues`string`Feld `message_variation_name`hinzugefügt: Name der Nachricht
    * Neues`string`Feld `canvas_name`hinzugefügt: Name des Canvas
    * Neues`string`Feld `canvas_variation_name`hinzugefügt: Name der Canvas-Variante, die diese Nutzer:in erhalten hat
    * Neues`string`Feld `canvas_step_name`hinzugefügt: Name des Canvas-Schritts

* Änderungen am Feld „Veranstaltungstyp`users.messages.pushnotification.InfluencedOpen`“:
    * Neues`string`Feld `campaign_name`hinzugefügt: Name der Kampagne
    * Neues`string`Feld `message_variation_name`hinzugefügt: Name der Nachricht
    * Neues`string`Feld `canvas_name`hinzugefügt: Name des Canvas
    * Neues`string`Feld `canvas_variation_name`hinzugefügt: Name der Canvas-Variante, die diese Nutzer:in erhalten hat
    * Neues`string`Feld `canvas_step_name`hinzugefügt: Name des Canvas-Schritts

* Änderungen am Feld „Veranstaltungstyp`users.messages.pushnotification.IosForeground`“:
    * Neues`string`Feld `campaign_name`hinzugefügt: Name der Kampagne
    * Neues`string`Feld `message_variation_name`hinzugefügt: Name der Nachricht
    * Neues`string`Feld `canvas_name`hinzugefügt: Name des Canvas
    * Neues`string`Feld `canvas_variation_name`hinzugefügt: Name der Canvas-Variante, die diese Nutzer:in erhalten hat
    * Neues`string`Feld `canvas_step_name`hinzugefügt: Name des Canvas-Schritts

* Änderungen am Feld „Veranstaltungstyp`users.messages.pushnotification.Open`“:
    * Neues`string`Feld `campaign_name`hinzugefügt: Name der Kampagne
    * Neues`string`Feld `message_variation_name`hinzugefügt: Name der Nachricht
    * Neues`string`Feld `canvas_name`hinzugefügt: Name des Canvas
    * Neues`string`Feld `canvas_variation_name`hinzugefügt: Name der Canvas-Variante, die diese Nutzer:in erhalten hat
    * Neues`string`Feld `canvas_step_name`hinzugefügt: Name des Canvas-Schritts

* Änderungen am Feld „Veranstaltungstyp`users.messages.pushnotification.Retry`“:
    * Neues`string`Feld `campaign_name`hinzugefügt: Name der Kampagne
    * Neues`string`Feld `message_variation_name`hinzugefügt: Name der Nachricht
    * Neues`string`Feld `canvas_name`hinzugefügt: Name des Canvas
    * Neues`string`Feld `canvas_variation_name`hinzugefügt: Name der Canvas-Variante, die diese Nutzer:in erhalten hat
    * Neues`string`Feld `canvas_step_name`hinzugefügt: Name des Canvas-Schritts

* Änderungen am Feld „Veranstaltungstyp`users.messages.pushnotification.Send`“:
    * Neues`string`Feld `campaign_name`hinzugefügt: Name der Kampagne
    * Neues`string`Feld `message_variation_name`hinzugefügt: Name der Nachricht
    * Neues`string`Feld `canvas_name`hinzugefügt: Name des Canvas
    * Neues`string`Feld `canvas_variation_name`hinzugefügt: Name der Canvas-Variante, die diese Nutzer:in erhalten hat
    * Neues`string`Feld `canvas_step_name`hinzugefügt: Name des Canvas-Schritts

* Änderungen am Feld „Veranstaltungstyp`users.messages.rcs.InboundReceive`“:
    * Neues`string`Feld `canvas_variation_name`hinzugefügt: Name der Canvas-Variante, die diese Nutzer:in erhalten hat

* Änderungen am Feld „Veranstaltungstyp`users.messages.sms.Abort`“:
    * Neues`string`Feld `campaign_name`hinzugefügt: Name der Kampagne
    * Neues`string`Feld `message_variation_name`hinzugefügt: Name der Nachricht
    * Neues`string`Feld `canvas_name`hinzugefügt: Name des Canvas
    * Neues`string`Feld `canvas_variation_name`hinzugefügt: Name der Canvas-Variante, die diese Nutzer:in erhalten hat
    * Neues`string`Feld `canvas_step_name`hinzugefügt: Name des Canvas-Schritts

* Änderungen am Feld „Veranstaltungstyp`users.messages.sms.CarrierSend`“:
    * Neues`string`Feld `campaign_name`hinzugefügt: Name der Kampagne
    * Neues`string`Feld `message_variation_name`hinzugefügt: Name der Nachricht
    * Neues`string`Feld `canvas_name`hinzugefügt: Name des Canvas
    * Neues`string`Feld `canvas_variation_name`hinzugefügt: Name der Canvas-Variante, die diese Nutzer:in erhalten hat
    * Neues`string`Feld `canvas_step_name`hinzugefügt: Name des Canvas-Schritts

* Änderungen am Feld „Veranstaltungstyp`users.messages.sms.Delivery`“:
    * Neues`string`Feld `campaign_name`hinzugefügt: Name der Kampagne
    * Neues`string`Feld `message_variation_name`hinzugefügt: Name der Nachricht
    * Neues`string`Feld `canvas_name`hinzugefügt: Name des Canvas
    * Neues`string`Feld `canvas_variation_name`hinzugefügt: Name der Canvas-Variante, die diese Nutzer:in erhalten hat
    * Neues`string`Feld `canvas_step_name`hinzugefügt: Name des Canvas-Schritts

* Änderungen am Feld „Veranstaltungstyp`users.messages.sms.DeliveryFailure`“:
    * Neues`string`Feld `campaign_name`hinzugefügt: Name der Kampagne
    * Neues`string`Feld `message_variation_name`hinzugefügt: Name der Nachricht
    * Neues`string`Feld `canvas_name`hinzugefügt: Name des Canvas
    * Neues`string`Feld `canvas_variation_name`hinzugefügt: Name der Canvas-Variante, die diese Nutzer:in erhalten hat
    * Neues`string`Feld `canvas_step_name`hinzugefügt: Name des Canvas-Schritts

* Änderungen am Feld „Veranstaltungstyp`users.messages.sms.InboundReceive`“:
    * Neues`string`Feld `campaign_name`hinzugefügt: Name der Kampagne
    * Neues`string`Feld `message_variation_name`hinzugefügt: Name der Nachricht
    * Neues`string`Feld `canvas_name`hinzugefügt: Name des Canvas
    * Neues`string`Feld `canvas_variation_name`hinzugefügt: Name der Canvas-Variante, die diese Nutzer:in erhalten hat
    * Neues`string`Feld `canvas_step_name`hinzugefügt: Name des Canvas-Schritts

* Änderungen am Feld „Veranstaltungstyp`users.messages.sms.Rejection`“:
    * Neues`string`Feld `campaign_name`hinzugefügt: Name der Kampagne
    * Neues`string`Feld `message_variation_name`hinzugefügt: Name der Nachricht
    * Neues`string`Feld `canvas_name`hinzugefügt: Name des Canvas
    * Neues`string`Feld `canvas_variation_name`hinzugefügt: Name der Canvas-Variante, die diese Nutzer:in erhalten hat
    * Neues`string`Feld `canvas_step_name`hinzugefügt: Name des Canvas-Schritts

* Änderungen am Feld „Veranstaltungstyp`users.messages.sms.Retry`“:
    * Neues`string`Feld `campaign_name`hinzugefügt: Name der Kampagne
    * Neues`string`Feld `message_variation_name`hinzugefügt: Name der Nachricht
    * Neues`string`Feld `canvas_name`hinzugefügt: Name des Canvas
    * Neues`string`Feld `canvas_variation_name`hinzugefügt: Name der Canvas-Variante, die diese Nutzer:in erhalten hat
    * Neues`string`Feld `canvas_step_name`hinzugefügt: Name des Canvas-Schritts

* Änderungen am Feld „Veranstaltungstyp`users.messages.sms.Send`“:
    * Neues`string`Feld `campaign_name`hinzugefügt: Name der Kampagne
    * Neues`string`Feld `message_variation_name`hinzugefügt: Name der Nachricht
    * Neues`string`Feld `canvas_name`hinzugefügt: Name des Canvas
    * Neues`string`Feld `canvas_variation_name`hinzugefügt: Name der Canvas-Variante, die diese Nutzer:in erhalten hat
    * Neues`string`Feld `canvas_step_name`hinzugefügt: Name des Canvas-Schritts

* Änderungen am Feld „Veranstaltungstyp`users.messages.sms.ShortLinkClick`“:
    * Neues`string`Feld `campaign_name`hinzugefügt: Name der Kampagne
    * Neues`string`Feld `message_variation_name`hinzugefügt: Name der Nachricht
    * Neues`string`Feld `canvas_name`hinzugefügt: Name des Canvas
    * Neues`string`Feld `canvas_variation_name`hinzugefügt: Name der Canvas-Variante, die diese Nutzer:in erhalten hat
    * Neues`string`Feld `canvas_step_name`hinzugefügt: Name des Canvas-Schritts

* Änderungen am Feld „Veranstaltungstyp`users.messages.webhook.Abort`“:
    * Neues`string`Feld `campaign_name`hinzugefügt: Name der Kampagne
    * Neues`string`Feld `message_variation_name`hinzugefügt: Name der Nachricht
    * Neues`string`Feld `canvas_name`hinzugefügt: Name des Canvas
    * Neues`string`Feld `canvas_variation_name`hinzugefügt: Name der Canvas-Variante, die diese Nutzer:in erhalten hat
    * Neues`string`Feld `canvas_step_name`hinzugefügt: Name des Canvas-Schritts

* Änderungen am Feld „Veranstaltungstyp`users.messages.webhook.Failure`“:
    * Neues`string`Feld `campaign_name`hinzugefügt: Name der Kampagne
    * Neues`string`Feld `canvas_name`hinzugefügt: Name des Canvas
    * Neues`string`Feld `canvas_step_name`hinzugefügt: Name des Canvas-Schritts
    * Neues`string`Feld `canvas_variation_name`hinzugefügt: Name der Canvas-Variante, die diese Nutzer:in erhalten hat
    * Neues`string`Feld `message_variation_name`hinzugefügt: Name der Nachricht

* Änderungen am Feld „Veranstaltungstyp`users.messages.webhook.Retry`“:
    * Neues`string`Feld `campaign_name`hinzugefügt: Name der Kampagne
    * Neues`string`Feld `message_variation_name`hinzugefügt: Name der Nachricht
    * Neues`string`Feld `canvas_name`hinzugefügt: Name des Canvas
    * Neues`string`Feld `canvas_variation_name`hinzugefügt: Name der Canvas-Variante, die diese Nutzer:in erhalten hat
    * Neues`string`Feld `canvas_step_name`hinzugefügt: Name des Canvas-Schritts

* Änderungen am Feld „Veranstaltungstyp`users.messages.webhook.Send`“:
    * Neues`string`Feld `campaign_name`hinzugefügt: Name der Kampagne
    * Neues`string`Feld `message_variation_name`hinzugefügt: Name der Nachricht
    * Neues`string`Feld `canvas_name`hinzugefügt: Name des Canvas
    * Neues`string`Feld `canvas_variation_name`hinzugefügt: Name der Canvas-Variante, die diese Nutzer:in erhalten hat
    * Neues`string`Feld `canvas_step_name`hinzugefügt: Name des Canvas-Schritts

* Änderungen am Feld „Veranstaltungstyp`users.messages.whatsapp.Abort`“:
    * Neues`string`Feld `campaign_name`hinzugefügt: Name der Kampagne
    * Neues`string`Feld `message_variation_name`hinzugefügt: Name der Nachricht
    * Neues`string`Feld `canvas_name`hinzugefügt: Name des Canvas
    * Neues`string`Feld `canvas_variation_name`hinzugefügt: Name der Canvas-Variante, die diese Nutzer:in erhalten hat
    * Neues`string`Feld `canvas_step_name`hinzugefügt: Name des Canvas-Schritts

* Änderungen am Feld „Veranstaltungstyp`users.messages.whatsapp.Click`“:
    * Neues`string`Feld `campaign_name`hinzugefügt: Name der Kampagne
    * Neues`string`Feld `message_variation_name`hinzugefügt: Name der Nachricht
    * Neues`string`Feld `canvas_name`hinzugefügt: Name des Canvas
    * Neues`string`Feld `canvas_variation_name`hinzugefügt: Name der Canvas-Variante, die diese Nutzer:in erhalten hat
    * Neues`string`Feld `canvas_step_name`hinzugefügt: Name des Canvas-Schritts

* Änderungen am Feld „Veranstaltungstyp`users.messages.whatsapp.Delivery`“:
    * Neues`string`Feld `campaign_name`hinzugefügt: Name der Kampagne
    * Neues`string`Feld `message_variation_name`hinzugefügt: Name der Nachricht
    * Neues`string`Feld `canvas_name`hinzugefügt: Name des Canvas
    * Neues`string`Feld `canvas_variation_name`hinzugefügt: Name der Canvas-Variante, die diese Nutzer:in erhalten hat
    * Neues`string`Feld `canvas_step_name`hinzugefügt: Name des Canvas-Schritts

* Änderungen am Feld „Veranstaltungstyp`users.messages.whatsapp.Failure`“:
    * Neues`string`Feld `campaign_name`hinzugefügt: Name der Kampagne
    * Neues`string`Feld `message_variation_name`hinzugefügt: Name der Nachricht
    * Neues`string`Feld `canvas_name`hinzugefügt: Name des Canvas
    * Neues`string`Feld `canvas_variation_name`hinzugefügt: Name der Canvas-Variante, die diese Nutzer:in erhalten hat
    * Neues`string`Feld `canvas_step_name`hinzugefügt: Name des Canvas-Schritts

* Änderungen am Feld „Veranstaltungstyp`users.messages.whatsapp.InboundReceive`“:
    * Neues`string`Feld `campaign_name`hinzugefügt: Name der Kampagne
    * Neues`string`Feld `canvas_name`hinzugefügt: Name des Canvas
    * Neues`string`Feld `canvas_step_name`hinzugefügt: Name des Canvas-Schritts
    * Neues`string`Feld `canvas_variation_name`hinzugefügt: Name der Canvas-Variante, die diese Nutzer:in erhalten hat
    * Neues`string`Feld `message_variation_name`hinzugefügt: Name der Nachricht

* Änderungen am Feld „Veranstaltungstyp`users.messages.whatsapp.Read`“:
    * Neues`string`Feld `campaign_name`hinzugefügt: Name der Kampagne
    * Neues`string`Feld `message_variation_name`hinzugefügt: Name der Nachricht
    * Neues`string`Feld `canvas_name`hinzugefügt: Name des Canvas
    * Neues`string`Feld `canvas_variation_name`hinzugefügt: Name der Canvas-Variante, die diese Nutzer:in erhalten hat
    * Neues`string`Feld `canvas_step_name`hinzugefügt: Name des Canvas-Schritts

* Änderungen am Feld „Veranstaltungstyp`users.messages.whatsapp.Retry`“:
    * Neues`string`Feld `campaign_name`hinzugefügt: Name der Kampagne
    * Neues`string`Feld `message_variation_name`hinzugefügt: Name der Nachricht
    * Neues`string`Feld `canvas_name`hinzugefügt: Name des Canvas
    * Neues`string`Feld `canvas_variation_name`hinzugefügt: Name der Canvas-Variante, die diese Nutzer:in erhalten hat
    * Neues`string`Feld `canvas_step_name`hinzugefügt: Name des Canvas-Schritts

* Änderungen am Feld „Veranstaltungstyp`users.messages.whatsapp.Send`“:
    * Neues`string`Feld `campaign_name`hinzugefügt: Name der Kampagne
    * Neues`string`Feld `canvas_name`hinzugefügt: Name des Canvas
    * Neues`string`Feld `canvas_step_name`hinzugefügt: Name des Canvas-Schritts
    * Neues`string`Feld `canvas_variation_name`hinzugefügt: Name der Canvas-Variante, die diese Nutzer:in erhalten hat
    * Neues`string`Feld `message_variation_name`hinzugefügt: Name der Nachricht

## Änderungen in Version 5 (Veröffentlichungsdatum: 04.02.2026)

### Änderungen für die Lagerung

* Neuer Veranstaltungstyp `agentconsole.AgentExecuted`hinzugefügt.

* Neuer Veranstaltungstyp `agentconsole.ToolInvocation`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.email.Retry`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.line.Retry`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.pushnotification.Retry`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.sms.Retry`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.webhook.Retry`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.whatsapp.Retry`hinzugefügt.

* Änderungen am Feld „Veranstaltungstyp`users.behaviors.pushnotification.TokenStateChange`“:
    * Neues`long`Feld `time_ms`hinzugefügt: Zeitpunkt in Millisekunden, zu dem das Ereignis stattfand

### Änderungen für den Datenaustausch

* Neuer Veranstaltungstyp `agentconsole.AgentExecuted`hinzugefügt.

* Neuer Veranstaltungstyp `agentconsole.ToolInvocation`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.email.Retry`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.line.Retry`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.pushnotification.Retry`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.sms.Retry`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.webhook.Retry`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.whatsapp.Retry`hinzugefügt.

* Änderungen am Feld „Veranstaltungstyp`users.behaviors.pushnotification.TokenStateChange`“:
    * Neues`long`Feld `time_ms`hinzugefügt: Zeitpunkt in Millisekunden, zu dem das Ereignis stattfand

## Änderungen in Version 4 (Veröffentlichungsdatum: 07.01.2026)

### Änderungen für die Lagerung

* Änderungen am Feld „Veranstaltungstyp`users.behaviors.pushnotification.TokenStateChange`“:
    * Neues`string`Feld `push_token`hinzugefügt: Push-Token der Veranstaltung

* Änderungen am Feld „Veranstaltungstyp`users.messages.pushnotification.Bounce`“:
    * Neues`string`Feld `push_token`hinzugefügt: Push-Token der Veranstaltung

* Änderungen am Feld „Veranstaltungstyp`users.messages.pushnotification.Send`“:
    * Neues`string`Feld `push_token`hinzugefügt: Push-Token der Veranstaltung

* Änderungen am Feld „Veranstaltungstyp`users.messages.rcs.Click`“:
    * Neues`string`Feld `canvas_variation_name`hinzugefügt: Name der Canvas-Variante, die diese Nutzer:in erhalten hat
    * Das Feld`user_phone_number`ist nun *optional*.

* Änderungen am Feld „Veranstaltungstyp`users.messages.rcs.InboundReceive`“:
    * Das Feld`user_id`ist nun *optional*.

* Änderungen am Feld „Veranstaltungstyp`users.messages.rcs.Rejection`“:
    * Neues`string`Feld `canvas_step_message_variation_id`hinzugefügt: API-ID der Canvas-Schritt-Nachrichtenvariante, die dieser Benutzer erhalten hat

### Änderungen für den Datenaustausch

* Änderungen am Feld „Veranstaltungstyp`users.messages.rcs.Click`“:
    * Neues`string`Feld `canvas_variation_name`hinzugefügt: Name der Canvas-Variante, die diese Nutzer:in erhalten hat
    * Das Feld`user_phone_number`ist nun *optional*.

* Änderungen am Feld „Veranstaltungstyp`users.messages.rcs.InboundReceive`“:
    * Das Feld`user_id`ist nun *optional*.

* Änderungen am Feld „Veranstaltungstyp`users.messages.rcs.Rejection`“:
    * Neues`string`Feld `canvas_step_message_variation_api_id`hinzugefügt: API-ID der Canvas-Schritt-Nachrichtenvariante, die dieser Benutzer erhalten hat

## Änderungen in Version 3 (Veröffentlichungsdatum 08.10.2025)

### Änderungen für die Lagerung

* Neuer Veranstaltungstyp `users.messages.line.Abort`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.line.Click`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.line.InboundReceive`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.line.Send`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.rcs.Abort`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.rcs.Click`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.rcs.Delivery`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.rcs.InboundReceive`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.rcs.Read`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.rcs.Rejection`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.rcs.Send`hinzugefügt.

* Änderungen am Feld „Veranstaltungstyp`users.messages.sms.Delivery`“:
    * Neues`boolean`Feld `is_sms_fallback`hinzugefügt: Zeigt an, dass aufgrund einer abgelehnten RCS-Nachricht eine SMS-Fallback-Nachricht gesendet wurde. Die Nachricht kann zur Zustellung gebracht werden, nicht zugestellt werden oder abgelehnt werden. Es kann über eine Sende-ID und eine Versand-ID mit dem RCS-Ablehnungsereignis verknüpft werden.

* Änderungen am Feld „Veranstaltungstyp`users.messages.sms.DeliveryFailure`“:
    * Neues`boolean`Feld `is_sms_fallback`hinzugefügt: Zeigt an, dass aufgrund einer abgelehnten RCS-Nachricht eine SMS-Fallback-Nachricht gesendet wurde. Die Nachricht kann zur Zustellung gebracht werden, nicht zugestellt werden oder abgelehnt werden. Es kann über eine Sende-ID und eine Versand-ID mit dem RCS-Ablehnungsereignis verknüpft werden.

* Änderungen am Feld „Veranstaltungstyp`users.messages.sms.Rejection`“:
    * Neues`boolean`Feld `is_sms_fallback`hinzugefügt: Zeigt an, dass aufgrund einer abgelehnten RCS-Nachricht eine SMS-Fallback-Nachricht gesendet wurde. Die Nachricht kann zur Zustellung gebracht werden, nicht zugestellt werden oder abgelehnt werden. Es kann über eine Sende-ID und eine Versand-ID mit dem RCS-Ablehnungsereignis verknüpft werden. Es kann über eine Sende-ID und eine Versand-ID mit dem RCS-Ablehnungsereignis verknüpft werden. (Event-Eigenschaft)

* Änderungen am Feld „Veranstaltungstyp`users.messages.whatsapp.Delivery`“:
    * Neues`string`Feld `flow_id`hinzugefügt: Die eindeutige ID des Flows im WhatsApp Manager. Anzeigen, wenn die Nachricht einen CTA enthält, um auf einen WhatsApp-Flow zu antworten
    * Neues`string`Feld `template_name`hinzugefügt: [PII] Name des Templates im WhatsApp-Manager. Bitte angeben, wenn eine Template-Nachricht gesendet wird
    * Neues`string`Feld `message_id`hinzugefügt: Die von Meta für diese Nachricht generierte eindeutige ID

* Änderungen am Feld „Veranstaltungstyp`users.messages.whatsapp.Failure`“:
    * Neues`string`Feld `message_id`hinzugefügt: Die von Meta für diese Nachricht generierte eindeutige ID
    * Neues`string`Feld `template_name`hinzugefügt: [PII] Name des Templates im WhatsApp-Manager. Bitte angeben, wenn eine Template-Nachricht gesendet wird
    * Neues`string`Feld `flow_id`hinzugefügt: Die eindeutige ID des Flows im WhatsApp Manager. Anzeigen, wenn die Nachricht einen CTA enthält, um auf einen WhatsApp-Flow zu antworten

* Änderungen am Feld „Veranstaltungstyp`users.messages.whatsapp.InboundReceive`“:
    * Neues`string`Feld `catalog_id`hinzugefügt: Katalog-ID eines Produkts, falls ein Produkt in der eingehenden Nachricht referenziert wird. Andernfalls leer.
    * Neues`string`Feld `product_id`hinzugefügt: Produkt-SKU, falls ein Produkt in der eingehenden Nachricht referenziert wird. Andernfalls leer.
    * Neues`string`Feld `flow_id`hinzugefügt: Die eindeutige ID des Flows im WhatsApp Manager. Anwesend, wenn die Nutzer:in auf einen WhatsApp-Flow reagiert.
    * Neues`string`Feld `flow_response_json`hinzugefügt: [PII] Die von den Nutzern:innen eingegebenen Formularwerte. Anwesend, wenn die Nutzer:in auf einen WhatsApp-Flow reagiert.
    * Neues`string`Feld `message_id`hinzugefügt: Die von Meta für diese Nachricht generierte eindeutige ID
    * Neues`string`Feld `in_reply_to`hinzugefügt: Dermessage_idInhalt der Nachricht, auf die diese Nachricht eine Antwort darstellt.

* Änderungen am Feld „Veranstaltungstyp`users.messages.whatsapp.Read`“:
    * Neues`string`Feld `template_name`hinzugefügt: [PII] Name des Templates im WhatsApp-Manager. Bitte angeben, wenn eine Template-Nachricht gesendet wird
    * Neues`string`Feld `message_id`hinzugefügt: Die von Meta für diese Nachricht generierte eindeutige ID
    * Neues`string`Feld `flow_id`hinzugefügt: Die eindeutige ID des Flows im WhatsApp Manager. Anzeigen, wenn die Nachricht einen CTA enthält, um auf einen WhatsApp-Flow zu antworten

* Änderungen am Feld „Veranstaltungstyp`users.messages.whatsapp.Send`“:
    * Neues`string`Feld `flow_id`hinzugefügt: Die eindeutige ID des Flows im WhatsApp Manager. Anzeigen, wenn die Nachricht einen CTA enthält, um auf einen WhatsApp-Flow zu antworten
    * Neues`string`Feld `template_name`hinzugefügt: [PII] Name des Templates im WhatsApp Manager. Bitte angeben, wenn eine Template-Nachricht gesendet wird
    * Neues`string`Feld `message_id`hinzugefügt: Die von Meta für diese Nachricht generierte eindeutige ID

### Änderungen für den Datenaustausch

* Neuer Veranstaltungstyp `users.messages.line.Abort`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.line.Click`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.line.InboundReceive`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.line.Send`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.rcs.Abort`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.rcs.Click`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.rcs.Delivery`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.rcs.InboundReceive`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.rcs.Read`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.rcs.Rejection`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.rcs.Send`hinzugefügt.

* Änderungen am Feld „Veranstaltungstyp`users.messages.sms.Delivery`“:
    * Neues`boolean`Feld `is_sms_fallback`hinzugefügt: Gibt an, ob für diese abgelehnte RCS-Nachricht ein SMS-Fallback versucht wurde. Es ist mit dem Ereignis „SMS-Zustellung“ verknüpft/gekoppelt.

* Änderungen am Feld „Veranstaltungstyp`users.messages.sms.DeliveryFailure`“:
    * Neues`boolean`Feld `is_sms_fallback`hinzugefügt: Gibt an, ob für diese abgelehnte RCS-Nachricht ein SMS-Fallback versucht wurde. Es ist mit dem Ereignis „SMS-Zustellung“ verknüpft/gekoppelt.

* Änderungen am Feld „Veranstaltungstyp`users.messages.sms.Rejection`“:
    * Neues`boolean`Feld `is_sms_fallback`hinzugefügt: Gibt an, ob für diese abgelehnte RCS-Nachricht ein SMS-Fallback versucht wurde. Es ist mit dem Ereignis „SMS-Zustellung“ verknüpft/gekoppelt.

* Änderungen am Feld „Veranstaltungstyp`users.messages.whatsapp.Delivery`“:
    * Neues`string`Feld `flow_id`hinzugefügt: Die eindeutige ID des Flows im WhatsApp Manager. Anwesend, wenn die Nutzer:in auf einen WhatsApp-Flow reagiert.
    * Neues`string`Feld `template_name`hinzugefügt: [PII] Name des Templates im WhatsApp-Manager. Bitte angeben, wenn eine Template-Nachricht gesendet wird
    * Neues`string`Feld `message_id`hinzugefügt: Die von Meta für diese Nachricht generierte eindeutige ID

* Änderungen am Feld „Veranstaltungstyp`users.messages.whatsapp.Failure`“:
    * Neues`string`Feld `message_id`hinzugefügt: Die von Meta für diese Nachricht generierte eindeutige ID
    * Neues`string`Feld `template_name`hinzugefügt: [PII] Name des Templates im WhatsApp-Manager. Bitte angeben, wenn eine Template-Nachricht gesendet wird
    * Neues`string`Feld `flow_id`hinzugefügt: Die eindeutige ID des Flows im WhatsApp Manager. Anwesend, wenn die Nutzer:in auf einen WhatsApp-Flow reagiert.

* Änderungen am Feld „Veranstaltungstyp`users.messages.whatsapp.InboundReceive`“:
    * Neues`string`Feld `catalog_id`hinzugefügt: Katalog-ID eines Produkts, falls ein Produkt in der eingehenden Nachricht referenziert wird. Andernfalls leer.
    * Neues`string`Feld `product_id`hinzugefügt: ID des gekauften Produkts
    * Neues`string`Feld `flow_id`hinzugefügt: Die eindeutige ID des Flows im WhatsApp Manager. Anwesend, wenn die Nutzer:in auf einen WhatsApp-Flow reagiert.
    * Neues`string`Feld `flow_response_json`hinzugefügt: [PII] Die von den Nutzern:innen eingegebenen Formularwerte. Anwesend, wenn die Nutzer:in auf einen WhatsApp-Flow reagiert.
    * Neues`string`Feld `message_id`hinzugefügt: Die von Meta für diese Nachricht generierte eindeutige ID
    * Neues`string`Feld `in_reply_to`hinzugefügt: Dermessage_idInhalt der Nachricht, auf die diese Nachricht eine Antwort darstellt.

* Änderungen am Feld „Veranstaltungstyp`users.messages.whatsapp.Read`“:
    * Neues`string`Feld `template_name`hinzugefügt: [PII] Name des Templates im WhatsApp-Manager. Bitte angeben, wenn eine Template-Nachricht gesendet wird
    * Neues`string`Feld `message_id`hinzugefügt: Die von Meta für diese Nachricht generierte eindeutige ID
    * Neues`string`Feld `flow_id`hinzugefügt: Die eindeutige ID des Flows im WhatsApp Manager. Anwesend, wenn die Nutzer:in auf einen WhatsApp-Flow reagiert.

* Änderungen am Feld „Veranstaltungstyp`users.messages.whatsapp.Send`“:
    * Neues`string`Feld `flow_id`hinzugefügt: Die eindeutige ID des Flows im WhatsApp Manager. Anwesend, wenn die Nutzer:in auf einen WhatsApp-Flow reagiert.
    * Neues`string`Feld `template_name`hinzugefügt: [PII] Name des Templates im WhatsApp-Manager. Bitte angeben, wenn eine Template-Nachricht gesendet wird
    * Neues`string`Feld `message_id`hinzugefügt: Die von Meta für diese Nachricht generierte eindeutige ID

## Änderungen in Version 2 (Veröffentlichungsdatum null)

### Änderungen für die Lagerung

* Neuer Veranstaltungstyp `users.behaviors.app.FirstSession`hinzugefügt.

* Neuer Veranstaltungstyp `users.behaviors.app.SessionEnd`hinzugefügt.

* Neuer Veranstaltungstyp `users.behaviors.app.SessionStart`hinzugefügt.

* Neuer Veranstaltungstyp `users.behaviors.CustomEvent`hinzugefügt.

* Neuer Veranstaltungstyp `users.behaviors.InstallAttribution`hinzugefügt.

* Neuer Veranstaltungstyp `users.behaviors.liveactivity.PushToStartTokenChange`hinzugefügt.

* Neuer Veranstaltungstyp `users.behaviors.liveactivity.UpdateTokenChange`hinzugefügt.

* Neuer Veranstaltungstyp `users.behaviors.Location`hinzugefügt.

* Neuer Veranstaltungstyp `users.behaviors.Purchase`hinzugefügt.

* Neuer Veranstaltungstyp `users.behaviors.pushnotification.TokenStateChange`hinzugefügt.

* Neuer Veranstaltungstyp `users.behaviors.subscription.GlobalStateChange`hinzugefügt.

* Neuer Veranstaltungstyp `users.behaviors.subscriptiongroup.StateChange`hinzugefügt.

* Neuer Veranstaltungstyp `users.behaviors.Uninstall`hinzugefügt.

* Neuer Veranstaltungstyp `users.campaigns.Conversion`hinzugefügt.

* Neuer Veranstaltungstyp `users.campaigns.EnrollInControl`hinzugefügt.

* Neuer Veranstaltungstyp `users.canvas.Conversion`hinzugefügt.

* Neuer Veranstaltungstyp `users.canvas.Entry`hinzugefügt.

* Neuer Veranstaltungstyp `users.canvas.exit.MatchedAudience`hinzugefügt.

* Neuer Veranstaltungstyp `users.canvas.exit.PerformedEvent`hinzugefügt.

* Neuer Veranstaltungstyp `users.canvas.experimentstep.Conversion`hinzugefügt.

* Neuer Veranstaltungstyp `users.canvas.experimentstep.SplitEntry`hinzugefügt.

* Neuer Veranstaltungstyp `users.canvasstep.Progression`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.banner.Abort`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.banner.Click`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.banner.Impression`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.contentcard.Abort`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.contentcard.Click`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.contentcard.Dismiss`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.contentcard.Impression`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.contentcard.Send`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.email.Abort`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.email.Bounce`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.email.Click`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.email.Deferral`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.email.Delivery`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.email.MarkAsSpam`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.email.Open`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.email.Send`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.email.SoftBounce`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.email.Unsubscribe`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.featureflag.Impression`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.inappmessage.Abort`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.inappmessage.Click`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.inappmessage.Impression`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.liveactivity.Outcome`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.liveactivity.Send`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.pushnotification.Abort`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.pushnotification.Bounce`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.pushnotification.IosForeground`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.pushnotification.Open`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.pushnotification.Send`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.sms.Abort`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.sms.CarrierSend`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.sms.Delivery`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.sms.DeliveryFailure`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.sms.InboundReceive`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.sms.Rejection`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.sms.Send`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.sms.ShortLinkClick`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.webhook.Abort`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.webhook.Failure`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.webhook.Send`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.whatsapp.Abort`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.whatsapp.Click`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.whatsapp.Delivery`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.whatsapp.Failure`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.whatsapp.InboundReceive`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.whatsapp.Read`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.whatsapp.Send`hinzugefügt.

* Neuer Veranstaltungstyp `users.RandomBucketNumberUpdate`hinzugefügt.

### Änderungen für den Datenaustausch

* Neuer Veranstaltungstyp `changelogs.GlobalControlGroup`hinzugefügt.

* Neuer Veranstaltungstyp `users.behaviors.app.FirstSession`hinzugefügt.

* Neuer Veranstaltungstyp `users.behaviors.app.NewsFeedImpression`hinzugefügt.

* Neuer Veranstaltungstyp `users.behaviors.app.SessionEnd`hinzugefügt.

* Neuer Veranstaltungstyp `users.behaviors.app.SessionStart`hinzugefügt.

* Neuer Veranstaltungstyp `users.behaviors.CustomEvent`hinzugefügt.

* Neuer Veranstaltungstyp `users.behaviors.geofence.DataEvent`hinzugefügt.

* Neuer Veranstaltungstyp `users.behaviors.geofence.RecordEvent`hinzugefügt.

* Neuer Veranstaltungstyp `users.behaviors.InstallAttribution`hinzugefügt.

* Neuer Veranstaltungstyp `users.behaviors.liveactivity.PushToStartTokenChange`hinzugefügt.

* Neuer Veranstaltungstyp `users.behaviors.liveactivity.UpdateTokenChange`hinzugefügt.

* Neuer Veranstaltungstyp `users.behaviors.Location`hinzugefügt.

* Neuer Veranstaltungstyp `users.behaviors.Purchase`hinzugefügt.

* Neuer Veranstaltungstyp `users.behaviors.pushnotification.TokenStateChange`hinzugefügt.

* Neuer Veranstaltungstyp `users.behaviors.subscription.GlobalStateChange`hinzugefügt.

* Neuer Veranstaltungstyp `users.behaviors.subscriptiongroup.StateChange`hinzugefügt.

* Neuer Veranstaltungstyp `users.behaviors.Uninstall`hinzugefügt.

* Neuer Veranstaltungstyp `users.behaviors.UpgradedApp`hinzugefügt.

* Neuer Veranstaltungstyp `users.campaigns.Conversion`hinzugefügt.

* Neuer Veranstaltungstyp `users.campaigns.EnrollInControl`hinzugefügt.

* Neuer Veranstaltungstyp `users.campaigns.FrequencyCap`hinzugefügt.

* Neuer Veranstaltungstyp `users.campaigns.Revenue`hinzugefügt.

* Neuer Veranstaltungstyp `users.canvas.Conversion`hinzugefügt.

* Neuer Veranstaltungstyp `users.canvas.Entry`hinzugefügt.

* Neuer Veranstaltungstyp `users.canvas.exit.MatchedAudience`hinzugefügt.

* Neuer Veranstaltungstyp `users.canvas.exit.PerformedEvent`hinzugefügt.

* Neuer Veranstaltungstyp `users.canvas.experimentstep.Conversion`hinzugefügt.

* Neuer Veranstaltungstyp `users.canvas.experimentstep.SplitEntry`hinzugefügt.

* Neuer Veranstaltungstyp `users.canvas.FrequencyCap`hinzugefügt.

* Neuer Veranstaltungstyp `users.canvas.Revenue`hinzugefügt.

* Neuer Veranstaltungstyp `users.canvasstep.Progression`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.banner.Abort`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.banner.Click`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.banner.Impression`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.contentcard.Abort`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.contentcard.Click`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.contentcard.Dismiss`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.contentcard.Impression`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.contentcard.Send`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.email.Abort`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.email.Bounce`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.email.Click`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.email.Deferral`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.email.Delivery`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.email.MarkAsSpam`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.email.Open`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.email.Send`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.email.SoftBounce`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.email.Unsubscribe`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.featureflag.Impression`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.inappmessage.Abort`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.inappmessage.Click`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.inappmessage.Impression`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.liveactivity.Outcome`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.liveactivity.Send`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.newsfeedcard.Abort`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.newsfeedcard.Click`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.newsfeedcard.Impression`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.pushnotification.Abort`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.pushnotification.Bounce`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.pushnotification.InfluencedOpen`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.pushnotification.IosForeground`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.pushnotification.Open`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.pushnotification.Send`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.sms.Abort`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.sms.CarrierSend`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.sms.Delivery`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.sms.DeliveryFailure`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.sms.InboundReceive`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.sms.Rejection`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.sms.Send`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.sms.ShortLinkClick`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.webhook.Abort`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.webhook.Failure`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.webhook.Send`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.whatsapp.Abort`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.whatsapp.Click`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.whatsapp.Delivery`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.whatsapp.Failure`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.whatsapp.InboundReceive`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.whatsapp.Read`hinzugefügt.

* Neuer Veranstaltungstyp `users.messages.whatsapp.Send`hinzugefügt.

* Neuer Veranstaltungstyp `users.RandomBucketNumberUpdate`hinzugefügt.

* Neuer Veranstaltungstyp `users.UserDeleteRequest`hinzugefügt.

* Neuer Veranstaltungstyp `users.UserOrphan`hinzugefügt.
