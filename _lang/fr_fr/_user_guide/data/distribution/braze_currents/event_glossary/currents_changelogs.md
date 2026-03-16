---
nav_title: Journal des modifications des événements actuels
page_order: 6
description: "Cette page présente les modifications apportées aux événements pour chaque version de Currents."
tool: Currents
---

# Journal des modifications de Currents

## Modifications apportées à la version 6 (date de publication : 04/03/2026)

### Modifications relatives au stockage

* Modifications apportées au champ « Type d'événement`agentconsole.AgentExecuted` » :
    * Ajout d'un nouveau`string`champ `error`: Description de l'erreur

* Modifications apportées au champ « Type d'événement`agentconsole.ToolInvocation` » :
    * Ajout d'un nouveau`string`champ `request_id`: ID unique pour cette requête LLM globale et exécution complète.

* Modifications apportées au champ « Type d'événement`users.messages.rcs.InboundReceive` » :
    * Ajout d'un nouveau`string`champ `canvas_variation_name`: Nom de la variante canvas reçue par cet utilisateur

### Modifications relatives au partage des données

* Modifications apportées au champ « Type d'événement`agentconsole.AgentExecuted` » :
    * Ajout d'un nouveau`string`champ `canvas_name`: Nom du canvas
    * Ajout d'un nouveau`string`champ `canvas_variation_name`: Nom de la variante canvas reçue par cet utilisateur
    * Ajout d'un nouveau`string`champ `canvas_step_name`: Nom de l'étape du canvas
    * Ajout d'un nouveau`string`champ `error`: Nom de l'erreur

* Modifications apportées au champ « Type d'événement`agentconsole.ToolInvocation` » :
    * Ajout d'un nouveau`string`champ `request_id`: ID unique pour cette requête LLM globale et exécution complète.

* Modifications apportées au champ « Type d'événement`users.behaviors.subscription.GlobalStateChange` » :
    * Ajout d'un nouveau`string`champ `campaign_name`: Nom de la campagne
    * Ajout d'un nouveau`string`champ `message_variation_name`: Nom de la variante du message
    * Ajout d'un nouveau`string`champ `canvas_name`: Nom du canvas
    * Ajout d'un nouveau`string`champ `canvas_variation_name`: Nom de la variante canvas reçue par cet utilisateur
    * Ajout d'un nouveau`string`champ `canvas_step_name`: Nom de l'étape du canvas

* Modifications apportées au champ « Type d'événement`users.behaviors.subscriptiongroup.StateChange` » :
    * Ajout d'un nouveau`string`champ `campaign_name`: Nom de la campagne
    * Ajout d'un nouveau`string`champ `message_variation_name`: Nom de la variante du message
    * Ajout d'un nouveau`string`champ `canvas_name`: Nom du canvas
    * Ajout d'un nouveau`string`champ `canvas_variation_name`: Nom de la variante canvas reçue par cet utilisateur
    * Ajout d'un nouveau`string`champ `canvas_step_name`: Nom de l'étape du canvas

* Modifications apportées au champ « Type d'événement`users.campaigns.Conversion` » :
    * Ajout d'un nouveau`string`champ `campaign_name`: Nom de la campagne
    * Ajout d'un nouveau`string`champ `message_variation_name`: Nom de la variante du message
    * Ajout d'un nouveau`string`champ `conversion_behavior`: Chaîne de caractères codée en JSON décrivant le comportement de conversion

* Modifications apportées au champ « Type d'événement`users.campaigns.EnrollInControl` » :
    * Ajout d'un nouveau`string`champ `campaign_name`: Nom de la campagne
    * Ajout d'un nouveau`string`champ `message_variation_name`: Nom de la variante du message

* Modifications apportées au champ « Type d'événement`users.canvas.Conversion` » :
    * Ajout d'un nouveau`string`champ `canvas_name`: Nom du canvas
    * Ajout d'un nouveau`string`champ `canvas_variation_name`: Nom de la variante canvas reçue par cet utilisateur
    * Ajout d'un nouveau`string`champ `canvas_step_name`: Nom de l'étape du canvas
    * Ajout d'un nouveau`string`champ `conversion_behavior`: Chaîne de caractères codée en JSON décrivant le comportement de conversion

* Modifications apportées au champ « Type d'événement`users.canvas.Entry` » :
    * Ajout d'un nouveau`string`champ `canvas_name`: Nom du canvas
    * Ajout d'un nouveau`string`champ `canvas_variation_name`: Nom de la variante canvas reçue par cet utilisateur
    * Ajout d'un nouveau`string`champ `canvas_step_name`: Nom de l'étape du canvas

* Modifications apportées au champ « Type d'événement`users.canvas.exit.MatchedAudience` » :
    * Ajout d'un nouveau`string`champ `canvas_name`: Nom du canvas
    * Ajout d'un nouveau`string`champ `canvas_variation_name`: Nom de la variante canvas reçue par cet utilisateur
    * Ajout d'un nouveau`string`champ `canvas_step_name`: Nom de l'étape du canvas

* Modifications apportées au champ « Type d'événement`users.canvas.exit.PerformedEvent` » :
    * Ajout d'un nouveau`string`champ `canvas_name`: Nom du canvas
    * Ajout d'un nouveau`string`champ `canvas_variation_name`: Nom de la variante canvas reçue par cet utilisateur
    * Ajout d'un nouveau`string`champ `canvas_step_name`: Nom de l'étape du canvas

* Modifications apportées au champ « Type d'événement`users.canvas.experimentstep.Conversion` » :
    * Ajout d'un nouveau`string`champ `canvas_name`: Nom du canvas
    * Ajout d'un nouveau`string`champ `canvas_variation_name`: Nom de la variante canvas reçue par cet utilisateur
    * Ajout d'un nouveau`string`champ `canvas_step_name`: Nom de l'étape du canvas
    * Ajout d'un nouveau`string`champ `experiment_split_name`: Nom de la division de l'expérience
    * Ajout d'un nouveau`string`champ `conversion_behavior`: Chaîne de caractères codée en JSON décrivant le comportement de conversion

* Modifications apportées au champ « Type d'événement`users.canvas.experimentstep.SplitEntry` » :
    * Ajout d'un nouveau`string`champ `canvas_name`: Nom du canvas
    * Ajout d'un nouveau`string`champ `canvas_variation_name`: Nom de la variante canvas reçue par cet utilisateur
    * Ajout d'un nouveau`string`champ `canvas_step_name`: Nom de l'étape du canvas
    * Ajout d'un nouveau`string`champ `experiment_split_name`: Nom de la division de l'expérience

* Modifications apportées au champ « Type d'événement`users.canvasstep.Progression` » :
    * Ajout d'un nouveau`string`champ `canvas_name`: Nom du canvas
    * Ajout d'un nouveau`string`champ `canvas_variation_name`: Nom de la variante canvas reçue par cet utilisateur
    * Ajout d'un nouveau`string`champ `canvas_step_name`: Nom de l'étape du canvas

* Modifications apportées au champ « Type d'événement`users.messages.banner.Abort` » :
    * Ajout d'un nouveau`string`champ `campaign_name`: Nom de la campagne
    * Ajout d'un nouveau`string`champ `message_variation_name`: Nom de la variante du message

* Modifications apportées au champ « Type d'événement`users.messages.banner.Click` » :
    * Ajout d'un nouveau`string`champ `campaign_name`: Nom de la campagne
    * Ajout d'un nouveau`string`champ `message_variation_name`: Nom de la variante du message

* Modifications apportées au champ « Type d'événement`users.messages.banner.Impression` » :
    * Ajout d'un nouveau`string`champ `campaign_name`: Nom de la campagne
    * Ajout d'un nouveau`string`champ `message_variation_name`: Nom de la variante du message

* Modifications apportées au champ « Type d'événement`users.messages.contentcard.Abort` » :
    * Ajout d'un nouveau`string`champ `campaign_name`: Nom de la campagne
    * Ajout d'un nouveau`string`champ `message_variation_name`: Nom de la variante du message
    * Ajout d'un nouveau`string`champ `canvas_name`: Nom du canvas
    * Ajout d'un nouveau`string`champ `canvas_variation_name`: Nom de la variante canvas reçue par cet utilisateur
    * Ajout d'un nouveau`string`champ `canvas_step_name`: Nom de l'étape du canvas

* Modifications apportées au champ « Type d'événement`users.messages.contentcard.Click` » :
    * Ajout d'un nouveau`string`champ `campaign_name`: Nom de la campagne
    * Ajout d'un nouveau`string`champ `message_variation_name`: Nom de la variante du message
    * Ajout d'un nouveau`string`champ `canvas_name`: Nom du canvas
    * Ajout d'un nouveau`string`champ `canvas_variation_name`: Nom de la variante canvas reçue par cet utilisateur
    * Ajout d'un nouveau`string`champ `canvas_step_name`: Nom de l'étape du canvas

* Modifications apportées au champ « Type d'événement`users.messages.contentcard.Dismiss` » :
    * Ajout d'un nouveau`string`champ `campaign_name`: Nom de la campagne
    * Ajout d'un nouveau`string`champ `message_variation_name`: Nom de la variante du message
    * Ajout d'un nouveau`string`champ `canvas_name`: Nom du canvas
    * Ajout d'un nouveau`string`champ `canvas_variation_name`: Nom de la variante canvas reçue par cet utilisateur
    * Ajout d'un nouveau`string`champ `canvas_step_name`: Nom de l'étape du canvas

* Modifications apportées au champ « Type d'événement`users.messages.contentcard.Impression` » :
    * Ajout d'un nouveau`string`champ `campaign_name`: Nom de la campagne
    * Ajout d'un nouveau`string`champ `message_variation_name`: Nom de la variante du message
    * Ajout d'un nouveau`string`champ `canvas_name`: Nom du canvas
    * Ajout d'un nouveau`string`champ `canvas_variation_name`: Nom de la variante canvas reçue par cet utilisateur
    * Ajout d'un nouveau`string`champ `canvas_step_name`: Nom de l'étape du canvas

* Modifications apportées au champ « Type d'événement`users.messages.contentcard.Send` » :
    * Ajout d'un nouveau`string`champ `campaign_name`: Nom de la campagne
    * Ajout d'un nouveau`string`champ `message_variation_name`: Nom de la variante du message
    * Ajout d'un nouveau`string`champ `canvas_name`: Nom du canvas
    * Ajout d'un nouveau`string`champ `canvas_variation_name`: Nom de la variante canvas reçue par cet utilisateur
    * Ajout d'un nouveau`string`champ `canvas_step_name`: Nom de l'étape du canvas

* Modifications apportées au champ « Type d'événement`users.messages.email.Abort` » :
    * Ajout d'un nouveau`string`champ `campaign_name`: Nom de la campagne
    * Ajout d'un nouveau`string`champ `message_variation_name`: Nom de la variante du message
    * Ajout d'un nouveau`string`champ `canvas_name`: Nom du canvas
    * Ajout d'un nouveau`string`champ `canvas_variation_name`: Nom de la variante canvas reçue par cet utilisateur
    * Ajout d'un nouveau`string`champ `canvas_step_name`: Nom de l'étape du canvas

* Modifications apportées au champ « Type d'événement`users.messages.email.Bounce` » :
    * Ajout d'un nouveau`string`champ `campaign_name`: Nom de la campagne
    * Ajout d'un nouveau`string`champ `message_variation_name`: Nom de la variante du message
    * Ajout d'un nouveau`string`champ `canvas_name`: Nom du canvas
    * Ajout d'un nouveau`string`champ `canvas_variation_name`: Nom de la variante canvas reçue par cet utilisateur
    * Ajout d'un nouveau`string`champ `canvas_step_name`: Nom de l'étape du canvas

* Modifications apportées au champ « Type d'événement`users.messages.email.Click` » :
    * Ajout d'un nouveau`string`champ `campaign_name`: Nom de la campagne
    * Ajout d'un nouveau`string`champ `message_variation_name`: Nom de la variante du message
    * Ajout d'un nouveau`string`champ `canvas_name`: Nom du canvas
    * Ajout d'un nouveau`string`champ `canvas_variation_name`: Nom de la variante canvas reçue par cet utilisateur
    * Ajout d'un nouveau`string`champ `canvas_step_name`: Nom de l'étape du canvas

* Modifications apportées au champ « Type d'événement`users.messages.email.Deferral` » :
    * Ajout d'un nouveau`string`champ `campaign_name`: Nom de la campagne
    * Ajout d'un nouveau`string`champ `message_variation_name`: Nom de la variante du message
    * Ajout d'un nouveau`string`champ `canvas_name`: Nom du canvas
    * Ajout d'un nouveau`string`champ `canvas_variation_name`: Nom de la variante canvas reçue par cet utilisateur
    * Ajout d'un nouveau`string`champ `canvas_step_name`: Nom de l'étape du canvas

* Modifications apportées au champ « Type d'événement`users.messages.email.Delivery` » :
    * Ajout d'un nouveau`string`champ `campaign_name`: Nom de la campagne
    * Ajout d'un nouveau`string`champ `message_variation_name`: Nom de la variante du message
    * Ajout d'un nouveau`string`champ `canvas_name`: Nom du canvas
    * Ajout d'un nouveau`string`champ `canvas_variation_name`: Nom de la variante canvas reçue par cet utilisateur
    * Ajout d'un nouveau`string`champ `canvas_step_name`: Nom de l'étape du canvas

* Modifications apportées au champ « Type d'événement`users.messages.email.MarkAsSpam` » :
    * Ajout d'un nouveau`string`champ `campaign_name`: Nom de la campagne
    * Ajout d'un nouveau`string`champ `message_variation_name`: Nom de la variante du message
    * Ajout d'un nouveau`string`champ `canvas_name`: Nom du canvas
    * Ajout d'un nouveau`string`champ `canvas_variation_name`: Nom de la variante canvas reçue par cet utilisateur
    * Ajout d'un nouveau`string`champ `canvas_step_name`: Nom de l'étape du canvas

* Modifications apportées au champ « Type d'événement`users.messages.email.Open` » :
    * Ajout d'un nouveau`string`champ `campaign_name`: Nom de la campagne
    * Ajout d'un nouveau`string`champ `message_variation_name`: Nom de la variante du message
    * Ajout d'un nouveau`string`champ `canvas_name`: Nom du canvas
    * Ajout d'un nouveau`string`champ `canvas_variation_name`: Nom de la variante canvas reçue par cet utilisateur
    * Ajout d'un nouveau`string`champ `canvas_step_name`: Nom de l'étape du canvas

* Modifications apportées au champ « Type d'événement`users.messages.email.Retry` » :
    * Ajout d'un nouveau`string`champ `campaign_name`: Nom de la campagne
    * Ajout d'un nouveau`string`champ `message_variation_name`: Nom de la variante du message
    * Ajout d'un nouveau`string`champ `canvas_name`: Nom du canvas
    * Ajout d'un nouveau`string`champ `canvas_variation_name`: Nom de la variante canvas reçue par cet utilisateur
    * Ajout d'un nouveau`string`champ `canvas_step_name`: Nom de l'étape du canvas

* Modifications apportées au champ « Type d'événement`users.messages.email.Send` » :
    * Ajout d'un nouveau`string`champ `campaign_name`: Nom de la campagne
    * Ajout d'un nouveau`string`champ `message_variation_name`: Nom de la variante du message
    * Ajout d'un nouveau`string`champ `canvas_name`: Nom du canvas
    * Ajout d'un nouveau`string`champ `canvas_variation_name`: Nom de la variante canvas reçue par cet utilisateur
    * Ajout d'un nouveau`string`champ `canvas_step_name`: Nom de l'étape du canvas

* Modifications apportées au champ « Type d'événement`users.messages.email.SoftBounce` » :
    * Ajout d'un nouveau`string`champ `campaign_name`: Nom de la campagne
    * Ajout d'un nouveau`string`champ `message_variation_name`: Nom de la variante du message
    * Ajout d'un nouveau`string`champ `canvas_name`: Nom du canvas
    * Ajout d'un nouveau`string`champ `canvas_variation_name`: Nom de la variante canvas reçue par cet utilisateur
    * Ajout d'un nouveau`string`champ `canvas_step_name`: Nom de l'étape du canvas

* Modifications apportées au champ « Type d'événement`users.messages.email.Unsubscribe` » :
    * Ajout d'un nouveau`string`champ `campaign_name`: Nom de la campagne
    * Ajout d'un nouveau`string`champ `message_variation_name`: Nom de la variante du message
    * Ajout d'un nouveau`string`champ `canvas_name`: Nom du canvas
    * Ajout d'un nouveau`string`champ `canvas_variation_name`: Nom de la variante canvas reçue par cet utilisateur
    * Ajout d'un nouveau`string`champ `canvas_step_name`: Nom de l'étape du canvas

* Modifications apportées au champ « Type d'événement`users.messages.featureflag.Impression` » :
    * Ajout d'un nouveau`string`champ `campaign_name`: Nom de la campagne
    * Ajout d'un nouveau`string`champ `canvas_name`: Nom du canvas
    * Ajout d'un nouveau`string`champ `canvas_step_name`: Nom de l'étape du canvas
    * Ajout d'un nouveau`string`champ `canvas_variation_name`: Nom de la variante canvas reçue par cet utilisateur
    * Ajout d'un nouveau`string`champ `message_variation_name`: Nom de la variante du message

* Modifications apportées au champ « Type d'événement`users.messages.inappmessage.Abort` » :
    * Ajout d'un nouveau`string`champ `campaign_name`: Nom de la campagne
    * Ajout d'un nouveau`string`champ `message_variation_name`: Nom de la variante du message
    * Ajout d'un nouveau`string`champ `canvas_name`: Nom du canvas
    * Ajout d'un nouveau`string`champ `canvas_variation_name`: Nom de la variante canvas reçue par cet utilisateur
    * Ajout d'un nouveau`string`champ `canvas_step_name`: Nom de l'étape du canvas

* Modifications apportées au champ « Type d'événement`users.messages.inappmessage.Click` » :
    * Ajout d'un nouveau`string`champ `campaign_name`: Nom de la campagne
    * Ajout d'un nouveau`string`champ `message_variation_name`: Nom de la variante du message
    * Ajout d'un nouveau`string`champ `canvas_name`: Nom du canvas
    * Ajout d'un nouveau`string`champ `canvas_variation_name`: Nom de la variante canvas reçue par cet utilisateur
    * Ajout d'un nouveau`string`champ `canvas_step_name`: Nom de l'étape du canvas

* Modifications apportées au champ « Type d'événement`users.messages.inappmessage.Impression` » :
    * Ajout d'un nouveau`string`champ `campaign_name`: Nom de la campagne
    * Ajout d'un nouveau`string`champ `message_variation_name`: Nom de la variante du message
    * Ajout d'un nouveau`string`champ `canvas_name`: Nom du canvas
    * Ajout d'un nouveau`string`champ `canvas_variation_name`: Nom de la variante canvas reçue par cet utilisateur
    * Ajout d'un nouveau`string`champ `canvas_step_name`: Nom de l'étape du canvas

* Modifications apportées au champ « Type d'événement`users.messages.line.Retry` » :
    * Ajout d'un nouveau`string`champ `campaign_name`: Nom de la campagne
    * Ajout d'un nouveau`string`champ `canvas_step_name`: Nom de l'étape du canvas

* Modifications apportées au champ « Type d'événement`users.messages.pushnotification.Abort` » :
    * Ajout d'un nouveau`string`champ `campaign_name`: Nom de la campagne
    * Ajout d'un nouveau`string`champ `message_variation_name`: Nom de la variante du message
    * Ajout d'un nouveau`string`champ `canvas_name`: Nom du canvas
    * Ajout d'un nouveau`string`champ `canvas_variation_name`: Nom de la variante canvas reçue par cet utilisateur
    * Ajout d'un nouveau`string`champ `canvas_step_name`: Nom de l'étape du canvas

* Modifications apportées au champ « Type d'événement`users.messages.pushnotification.Bounce` » :
    * Ajout d'un nouveau`string`champ `campaign_name`: Nom de la campagne
    * Ajout d'un nouveau`string`champ `message_variation_name`: Nom de la variante du message
    * Ajout d'un nouveau`string`champ `canvas_name`: Nom du canvas
    * Ajout d'un nouveau`string`champ `canvas_variation_name`: Nom de la variante canvas reçue par cet utilisateur
    * Ajout d'un nouveau`string`champ `canvas_step_name`: Nom de l'étape du canvas

* Modifications apportées au champ « Type d'événement`users.messages.pushnotification.InfluencedOpen` » :
    * Ajout d'un nouveau`string`champ `campaign_name`: Nom de la campagne
    * Ajout d'un nouveau`string`champ `message_variation_name`: Nom de la variante du message
    * Ajout d'un nouveau`string`champ `canvas_name`: Nom du canvas
    * Ajout d'un nouveau`string`champ `canvas_variation_name`: Nom de la variante canvas reçue par cet utilisateur
    * Ajout d'un nouveau`string`champ `canvas_step_name`: Nom de l'étape du canvas

* Modifications apportées au champ « Type d'événement`users.messages.pushnotification.IosForeground` » :
    * Ajout d'un nouveau`string`champ `campaign_name`: Nom de la campagne
    * Ajout d'un nouveau`string`champ `message_variation_name`: Nom de la variante du message
    * Ajout d'un nouveau`string`champ `canvas_name`: Nom du canvas
    * Ajout d'un nouveau`string`champ `canvas_variation_name`: Nom de la variante canvas reçue par cet utilisateur
    * Ajout d'un nouveau`string`champ `canvas_step_name`: Nom de l'étape du canvas

* Modifications apportées au champ « Type d'événement`users.messages.pushnotification.Open` » :
    * Ajout d'un nouveau`string`champ `campaign_name`: Nom de la campagne
    * Ajout d'un nouveau`string`champ `message_variation_name`: Nom de la variante du message
    * Ajout d'un nouveau`string`champ `canvas_name`: Nom du canvas
    * Ajout d'un nouveau`string`champ `canvas_variation_name`: Nom de la variante canvas reçue par cet utilisateur
    * Ajout d'un nouveau`string`champ `canvas_step_name`: Nom de l'étape du canvas

* Modifications apportées au champ « Type d'événement`users.messages.pushnotification.Retry` » :
    * Ajout d'un nouveau`string`champ `campaign_name`: Nom de la campagne
    * Ajout d'un nouveau`string`champ `message_variation_name`: Nom de la variante du message
    * Ajout d'un nouveau`string`champ `canvas_name`: Nom du canvas
    * Ajout d'un nouveau`string`champ `canvas_variation_name`: Nom de la variante canvas reçue par cet utilisateur
    * Ajout d'un nouveau`string`champ `canvas_step_name`: Nom de l'étape du canvas

* Modifications apportées au champ « Type d'événement`users.messages.pushnotification.Send` » :
    * Ajout d'un nouveau`string`champ `campaign_name`: Nom de la campagne
    * Ajout d'un nouveau`string`champ `message_variation_name`: Nom de la variante du message
    * Ajout d'un nouveau`string`champ `canvas_name`: Nom du canvas
    * Ajout d'un nouveau`string`champ `canvas_variation_name`: Nom de la variante canvas reçue par cet utilisateur
    * Ajout d'un nouveau`string`champ `canvas_step_name`: Nom de l'étape du canvas

* Modifications apportées au champ « Type d'événement`users.messages.rcs.InboundReceive` » :
    * Ajout d'un nouveau`string`champ `canvas_variation_name`: Nom de la variante canvas reçue par cet utilisateur

* Modifications apportées au champ « Type d'événement`users.messages.sms.Abort` » :
    * Ajout d'un nouveau`string`champ `campaign_name`: Nom de la campagne
    * Ajout d'un nouveau`string`champ `message_variation_name`: Nom de la variante du message
    * Ajout d'un nouveau`string`champ `canvas_name`: Nom du canvas
    * Ajout d'un nouveau`string`champ `canvas_variation_name`: Nom de la variante canvas reçue par cet utilisateur
    * Ajout d'un nouveau`string`champ `canvas_step_name`: Nom de l'étape du canvas

* Modifications apportées au champ « Type d'événement`users.messages.sms.CarrierSend` » :
    * Ajout d'un nouveau`string`champ `campaign_name`: Nom de la campagne
    * Ajout d'un nouveau`string`champ `message_variation_name`: Nom de la variante du message
    * Ajout d'un nouveau`string`champ `canvas_name`: Nom du canvas
    * Ajout d'un nouveau`string`champ `canvas_variation_name`: Nom de la variante canvas reçue par cet utilisateur
    * Ajout d'un nouveau`string`champ `canvas_step_name`: Nom de l'étape du canvas

* Modifications apportées au champ « Type d'événement`users.messages.sms.Delivery` » :
    * Ajout d'un nouveau`string`champ `campaign_name`: Nom de la campagne
    * Ajout d'un nouveau`string`champ `message_variation_name`: Nom de la variante du message
    * Ajout d'un nouveau`string`champ `canvas_name`: Nom du canvas
    * Ajout d'un nouveau`string`champ `canvas_variation_name`: Nom de la variante canvas reçue par cet utilisateur
    * Ajout d'un nouveau`string`champ `canvas_step_name`: Nom de l'étape du canvas

* Modifications apportées au champ « Type d'événement`users.messages.sms.DeliveryFailure` » :
    * Ajout d'un nouveau`string`champ `campaign_name`: Nom de la campagne
    * Ajout d'un nouveau`string`champ `message_variation_name`: Nom de la variante du message
    * Ajout d'un nouveau`string`champ `canvas_name`: Nom du canvas
    * Ajout d'un nouveau`string`champ `canvas_variation_name`: Nom de la variante canvas reçue par cet utilisateur
    * Ajout d'un nouveau`string`champ `canvas_step_name`: Nom de l'étape du canvas

* Modifications apportées au champ « Type d'événement`users.messages.sms.InboundReceive` » :
    * Ajout d'un nouveau`string`champ `campaign_name`: Nom de la campagne
    * Ajout d'un nouveau`string`champ `message_variation_name`: Nom de la variante du message
    * Ajout d'un nouveau`string`champ `canvas_name`: Nom du canvas
    * Ajout d'un nouveau`string`champ `canvas_variation_name`: Nom de la variante canvas reçue par cet utilisateur
    * Ajout d'un nouveau`string`champ `canvas_step_name`: Nom de l'étape du canvas

* Modifications apportées au champ « Type d'événement`users.messages.sms.Rejection` » :
    * Ajout d'un nouveau`string`champ `campaign_name`: Nom de la campagne
    * Ajout d'un nouveau`string`champ `message_variation_name`: Nom de la variante du message
    * Ajout d'un nouveau`string`champ `canvas_name`: Nom du canvas
    * Ajout d'un nouveau`string`champ `canvas_variation_name`: Nom de la variante canvas reçue par cet utilisateur
    * Ajout d'un nouveau`string`champ `canvas_step_name`: Nom de l'étape du canvas

* Modifications apportées au champ « Type d'événement`users.messages.sms.Retry` » :
    * Ajout d'un nouveau`string`champ `campaign_name`: Nom de la campagne
    * Ajout d'un nouveau`string`champ `message_variation_name`: Nom de la variante du message
    * Ajout d'un nouveau`string`champ `canvas_name`: Nom du canvas
    * Ajout d'un nouveau`string`champ `canvas_variation_name`: Nom de la variante canvas reçue par cet utilisateur
    * Ajout d'un nouveau`string`champ `canvas_step_name`: Nom de l'étape du canvas

* Modifications apportées au champ « Type d'événement`users.messages.sms.Send` » :
    * Ajout d'un nouveau`string`champ `campaign_name`: Nom de la campagne
    * Ajout d'un nouveau`string`champ `message_variation_name`: Nom de la variante du message
    * Ajout d'un nouveau`string`champ `canvas_name`: Nom du canvas
    * Ajout d'un nouveau`string`champ `canvas_variation_name`: Nom de la variante canvas reçue par cet utilisateur
    * Ajout d'un nouveau`string`champ `canvas_step_name`: Nom de l'étape du canvas

* Modifications apportées au champ « Type d'événement`users.messages.sms.ShortLinkClick` » :
    * Ajout d'un nouveau`string`champ `campaign_name`: Nom de la campagne
    * Ajout d'un nouveau`string`champ `message_variation_name`: Nom de la variante du message
    * Ajout d'un nouveau`string`champ `canvas_name`: Nom du canvas
    * Ajout d'un nouveau`string`champ `canvas_variation_name`: Nom de la variante canvas reçue par cet utilisateur
    * Ajout d'un nouveau`string`champ `canvas_step_name`: Nom de l'étape du canvas

* Modifications apportées au champ « Type d'événement`users.messages.webhook.Abort` » :
    * Ajout d'un nouveau`string`champ `campaign_name`: Nom de la campagne
    * Ajout d'un nouveau`string`champ `message_variation_name`: Nom de la variante du message
    * Ajout d'un nouveau`string`champ `canvas_name`: Nom du canvas
    * Ajout d'un nouveau`string`champ `canvas_variation_name`: Nom de la variante canvas reçue par cet utilisateur
    * Ajout d'un nouveau`string`champ `canvas_step_name`: Nom de l'étape du canvas

* Modifications apportées au champ « Type d'événement`users.messages.webhook.Failure` » :
    * Ajout d'un nouveau`string`champ `campaign_name`: Nom de la campagne
    * Ajout d'un nouveau`string`champ `canvas_name`: Nom du canvas
    * Ajout d'un nouveau`string`champ `canvas_step_name`: Nom de l'étape du canvas
    * Ajout d'un nouveau`string`champ `canvas_variation_name`: Nom de la variante canvas reçue par cet utilisateur
    * Ajout d'un nouveau`string`champ `message_variation_name`: Nom de la variante du message

* Modifications apportées au champ « Type d'événement`users.messages.webhook.Retry` » :
    * Ajout d'un nouveau`string`champ `campaign_name`: Nom de la campagne
    * Ajout d'un nouveau`string`champ `message_variation_name`: Nom de la variante du message
    * Ajout d'un nouveau`string`champ `canvas_name`: Nom du canvas
    * Ajout d'un nouveau`string`champ `canvas_variation_name`: Nom de la variante canvas reçue par cet utilisateur
    * Ajout d'un nouveau`string`champ `canvas_step_name`: Nom de l'étape du canvas

* Modifications apportées au champ « Type d'événement`users.messages.webhook.Send` » :
    * Ajout d'un nouveau`string`champ `campaign_name`: Nom de la campagne
    * Ajout d'un nouveau`string`champ `message_variation_name`: Nom de la variante du message
    * Ajout d'un nouveau`string`champ `canvas_name`: Nom du canvas
    * Ajout d'un nouveau`string`champ `canvas_variation_name`: Nom de la variante canvas reçue par cet utilisateur
    * Ajout d'un nouveau`string`champ `canvas_step_name`: Nom de l'étape du canvas

* Modifications apportées au champ « Type d'événement`users.messages.whatsapp.Abort` » :
    * Ajout d'un nouveau`string`champ `campaign_name`: Nom de la campagne
    * Ajout d'un nouveau`string`champ `message_variation_name`: Nom de la variante du message
    * Ajout d'un nouveau`string`champ `canvas_name`: Nom du canvas
    * Ajout d'un nouveau`string`champ `canvas_variation_name`: Nom de la variante canvas reçue par cet utilisateur
    * Ajout d'un nouveau`string`champ `canvas_step_name`: Nom de l'étape du canvas

* Modifications apportées au champ « Type d'événement`users.messages.whatsapp.Click` » :
    * Ajout d'un nouveau`string`champ `campaign_name`: Nom de la campagne
    * Ajout d'un nouveau`string`champ `message_variation_name`: Nom de la variante du message
    * Ajout d'un nouveau`string`champ `canvas_name`: Nom du canvas
    * Ajout d'un nouveau`string`champ `canvas_variation_name`: Nom de la variante canvas reçue par cet utilisateur
    * Ajout d'un nouveau`string`champ `canvas_step_name`: Nom de l'étape du canvas

* Modifications apportées au champ « Type d'événement`users.messages.whatsapp.Delivery` » :
    * Ajout d'un nouveau`string`champ `campaign_name`: Nom de la campagne
    * Ajout d'un nouveau`string`champ `message_variation_name`: Nom de la variante du message
    * Ajout d'un nouveau`string`champ `canvas_name`: Nom du canvas
    * Ajout d'un nouveau`string`champ `canvas_variation_name`: Nom de la variante canvas reçue par cet utilisateur
    * Ajout d'un nouveau`string`champ `canvas_step_name`: Nom de l'étape du canvas

* Modifications apportées au champ « Type d'événement`users.messages.whatsapp.Failure` » :
    * Ajout d'un nouveau`string`champ `campaign_name`: Nom de la campagne
    * Ajout d'un nouveau`string`champ `message_variation_name`: Nom de la variante du message
    * Ajout d'un nouveau`string`champ `canvas_name`: Nom du canvas
    * Ajout d'un nouveau`string`champ `canvas_variation_name`: Nom de la variante canvas reçue par cet utilisateur
    * Ajout d'un nouveau`string`champ `canvas_step_name`: Nom de l'étape du canvas

* Modifications apportées au champ « Type d'événement`users.messages.whatsapp.InboundReceive` » :
    * Ajout d'un nouveau`string`champ `campaign_name`: Nom de la campagne
    * Ajout d'un nouveau`string`champ `canvas_name`: Nom du canvas
    * Ajout d'un nouveau`string`champ `canvas_step_name`: Nom de l'étape du canvas
    * Ajout d'un nouveau`string`champ `canvas_variation_name`: Nom de la variante canvas reçue par cet utilisateur
    * Ajout d'un nouveau`string`champ `message_variation_name`: Nom de la variante du message

* Modifications apportées au champ « Type d'événement`users.messages.whatsapp.Read` » :
    * Ajout d'un nouveau`string`champ `campaign_name`: Nom de la campagne
    * Ajout d'un nouveau`string`champ `message_variation_name`: Nom de la variante du message
    * Ajout d'un nouveau`string`champ `canvas_name`: Nom du canvas
    * Ajout d'un nouveau`string`champ `canvas_variation_name`: Nom de la variante canvas reçue par cet utilisateur
    * Ajout d'un nouveau`string`champ `canvas_step_name`: Nom de l'étape du canvas

* Modifications apportées au champ « Type d'événement`users.messages.whatsapp.Retry` » :
    * Ajout d'un nouveau`string`champ `campaign_name`: Nom de la campagne
    * Ajout d'un nouveau`string`champ `message_variation_name`: Nom de la variante du message
    * Ajout d'un nouveau`string`champ `canvas_name`: Nom du canvas
    * Ajout d'un nouveau`string`champ `canvas_variation_name`: Nom de la variante canvas reçue par cet utilisateur
    * Ajout d'un nouveau`string`champ `canvas_step_name`: Nom de l'étape du canvas

* Modifications apportées au champ « Type d'événement`users.messages.whatsapp.Send` » :
    * Ajout d'un nouveau`string`champ `campaign_name`: Nom de la campagne
    * Ajout d'un nouveau`string`champ `canvas_name`: Nom du canvas
    * Ajout d'un nouveau`string`champ `canvas_step_name`: Nom de l'étape du canvas
    * Ajout d'un nouveau`string`champ `canvas_variation_name`: Nom de la variante canvas reçue par cet utilisateur
    * Ajout d'un nouveau`string`champ `message_variation_name`: Nom de la variante du message

## Modifications apportées à la version 5 (date de publication : 04/02/2026)

### Modifications relatives au stockage

* Ajout d'un nouveau type d'événement`agentconsole.AgentExecuted`.

* Ajout d'un nouveau type d'événement`agentconsole.ToolInvocation`.

* Ajout d'un nouveau type d'événement`users.messages.email.Retry`.

* Ajout d'un nouveau type d'événement`users.messages.line.Retry`.

* Ajout d'un nouveau type d'événement`users.messages.pushnotification.Retry`.

* Ajout d'un nouveau type d'événement`users.messages.sms.Retry`.

* Ajout d'un nouveau type d'événement`users.messages.webhook.Retry`.

* Ajout d'un nouveau type d'événement`users.messages.whatsapp.Retry`.

* Modifications apportées au champ « Type d'événement`users.behaviors.pushnotification.TokenStateChange` » :
    * Ajout d'un nouveau`long`champ `time_ms`: Heure en millisecondes à laquelle l'événement s'est produit

### Modifications relatives au partage des données

* Ajout d'un nouveau type d'événement`agentconsole.AgentExecuted`.

* Ajout d'un nouveau type d'événement`agentconsole.ToolInvocation`.

* Ajout d'un nouveau type d'événement`users.messages.email.Retry`.

* Ajout d'un nouveau type d'événement`users.messages.line.Retry`.

* Ajout d'un nouveau type d'événement`users.messages.pushnotification.Retry`.

* Ajout d'un nouveau type d'événement`users.messages.sms.Retry`.

* Ajout d'un nouveau type d'événement`users.messages.webhook.Retry`.

* Ajout d'un nouveau type d'événement`users.messages.whatsapp.Retry`.

* Modifications apportées au champ « Type d'événement`users.behaviors.pushnotification.TokenStateChange` » :
    * Ajout d'un nouveau`long`champ `time_ms`: Heure en millisecondes à laquelle l'événement s'est produit

## Modifications apportées à la version 4 (date de publication : 07/01/2026)

### Modifications relatives au stockage

* Modifications apportées au champ « Type d'événement`users.behaviors.pushnotification.TokenStateChange` » :
    * Ajout d'un nouveau`string`champ `push_token`: Jeton Push de l'événement

* Modifications apportées au champ « Type d'événement`users.messages.pushnotification.Bounce` » :
    * Ajout d'un nouveau`string`champ `push_token`: Jeton Push de l'événement

* Modifications apportées au champ « Type d'événement`users.messages.pushnotification.Send` » :
    * Ajout d'un nouveau`string`champ `push_token`: Jeton Push de l'événement

* Modifications apportées au champ « Type d'événement`users.messages.rcs.Click` » :
    * Ajout d'un nouveau`string`champ `canvas_variation_name`: Nom de la variante canvas reçue par cet utilisateur
    * Le champ`user_phone_number`est désormais *facultatif*.

* Modifications apportées au champ « Type d'événement`users.messages.rcs.InboundReceive` » :
    * Le champ`user_id`est désormais *facultatif*.

* Modifications apportées au champ « Type d'événement`users.messages.rcs.Rejection` » :
    * Ajout d'un nouveau`string`champ `canvas_step_message_variation_id`: ID API de la variation de message de l'étape de Canvas que l’utilisateur a reçue

### Modifications relatives au partage des données

* Modifications apportées au champ « Type d'événement`users.messages.rcs.Click` » :
    * Ajout d'un nouveau`string`champ `canvas_variation_name`: Nom de la variante canvas reçue par cet utilisateur
    * Le champ`user_phone_number`est désormais *facultatif*.

* Modifications apportées au champ « Type d'événement`users.messages.rcs.InboundReceive` » :
    * Le champ`user_id`est désormais *facultatif*.

* Modifications apportées au champ « Type d'événement`users.messages.rcs.Rejection` » :
    * Ajout d'un nouveau`string`champ `canvas_step_message_variation_api_id`: ID API de la variation de message de l'étape de Canvas que l’utilisateur a reçue

## Modifications apportées à la version 3 (date de publication : 08/10/2025)

### Modifications relatives au stockage

* Ajout d'un nouveau type d'événement`users.messages.line.Abort`.

* Ajout d'un nouveau type d'événement`users.messages.line.Click`.

* Ajout d'un nouveau type d'événement`users.messages.line.InboundReceive`.

* Ajout d'un nouveau type d'événement`users.messages.line.Send`.

* Ajout d'un nouveau type d'événement`users.messages.rcs.Abort`.

* Ajout d'un nouveau type d'événement`users.messages.rcs.Click`.

* Ajout d'un nouveau type d'événement`users.messages.rcs.Delivery`.

* Ajout d'un nouveau type d'événement`users.messages.rcs.InboundReceive`.

* Ajout d'un nouveau type d'événement`users.messages.rcs.Read`.

* Ajout d'un nouveau type d'événement`users.messages.rcs.Rejection`.

* Ajout d'un nouveau type d'événement`users.messages.rcs.Send`.

* Modifications apportées au champ « Type d'événement`users.messages.sms.Delivery` » :
    * Ajout d'un nouveau`boolean`champ `is_sms_fallback`: Indique qu'un message SMS de secours a été envoyé en raison du rejet d'un message RCS. Le message peut aboutir à une réception/distribution, à un échec de réception/distribution ou à un rejet. Il peut être associé à l'événement de rejet RCS via un ID d'envoi et un ID d'expédition.

* Modifications apportées au champ « Type d'événement`users.messages.sms.DeliveryFailure` » :
    * Ajout d'un nouveau`boolean`champ `is_sms_fallback`: Indique qu'un message SMS de secours a été envoyé en raison du rejet d'un message RCS. Le message peut aboutir à une réception/distribution, à un échec de réception/distribution ou à un rejet. Il peut être associé à l'événement de rejet RCS via un ID d'envoi et un ID d'expédition.

* Modifications apportées au champ « Type d'événement`users.messages.sms.Rejection` » :
    * Ajout d'un nouveau`boolean`champ `is_sms_fallback`: Indique qu'un message SMS de secours a été envoyé en raison du rejet d'un message RCS. Le message peut aboutir à une réception/distribution, à un échec de réception/distribution ou à un rejet. Il est possible de le relier à l'événement RCS Rejection via un ID d'envoi et un ID d'expédition. Il est possible de le relier à l'événement RCS Rejection via un ID d'envoi et un ID d'expédition. (Propriété d'événement)

* Modifications apportées au champ « Type d'événement`users.messages.whatsapp.Delivery` » :
    * Ajout d'un nouveau`string`champ `flow_id`: ID unique du flux dans WhatsApp gestionnaire. Présent si le message comprend un CTA pour répondre à un flux WhatsApp.
    * Ajout d'un nouveau`string`champ `template_name`: [PII] Nom du modèle dans le gestionnaire WhatsApp. Veuillez indiquer si vous envoyez un message type.
    * Ajout d'un nouveau`string`champ `message_id`: ID unique généré par Meta pour ce message

* Modifications apportées au champ « Type d'événement`users.messages.whatsapp.Failure` » :
    * Ajout d'un nouveau`string`champ `message_id`: ID unique généré par Meta pour ce message
    * Ajout d'un nouveau`string`champ `template_name`: [PII] Nom du modèle dans le gestionnaire WhatsApp. Veuillez indiquer si vous envoyez un message type.
    * Ajout d'un nouveau`string`champ `flow_id`: ID unique du flux dans WhatsApp gestionnaire. Présent si le message comprend un CTA pour répondre à un flux WhatsApp.

* Modifications apportées au champ « Type d'événement`users.messages.whatsapp.InboundReceive` » :
    * Ajout d'un nouveau`string`champ `catalog_id`: ID catalogue d'un produit si celui-ci est mentionné dans le message entrant. Sinon, veuillez laisser vide.
    * Ajout d'un nouveau`string`champ `product_id`: Unité de gestion des stocks si un produit est mentionné dans le message entrant. Sinon, veuillez laisser vide.
    * Ajout d'un nouveau`string`champ `flow_id`: ID unique du flux dans WhatsApp gestionnaire. Présent si l'utilisateur répond à un flux WhatsApp.
    * Ajout d'un nouveau`string`champ `flow_response_json`: [PII] Les valeurs du formulaire fournies par l'utilisateur. Présent si l'utilisateur répond à un flux WhatsApp.
    * Ajout d'un nouveau`string`champ `message_id`: ID unique généré par Meta pour ce message
    * Ajout d'un nouveau`string`champ `in_reply_to`: Lemessage_idcontenu du message auquel ce message répondait

* Modifications apportées au champ « Type d'événement`users.messages.whatsapp.Read` » :
    * Ajout d'un nouveau`string`champ `template_name`: [PII] Nom du modèle dans le gestionnaire WhatsApp. Veuillez indiquer si vous envoyez un message type.
    * Ajout d'un nouveau`string`champ `message_id`: ID unique généré par Meta pour ce message
    * Ajout d'un nouveau`string`champ `flow_id`: ID unique du flux dans WhatsApp gestionnaire. Présent si le message comprend un CTA pour répondre à un flux WhatsApp.

* Modifications apportées au champ « Type d'événement`users.messages.whatsapp.Send` » :
    * Ajout d'un nouveau`string`champ `flow_id`: ID unique du flux dans WhatsApp gestionnaire. Présent si le message comprend un CTA pour répondre à un flux WhatsApp.
    * Ajout d'un nouveau`string`champ `template_name`: [PII] Nom du modèle dans le gestionnaire de WhatsApp. Veuillez indiquer si vous envoyez un message type.
    * Ajout d'un nouveau`string`champ `message_id`: ID unique généré par Meta pour ce message

### Modifications relatives au partage des données

* Ajout d'un nouveau type d'événement`users.messages.line.Abort`.

* Ajout d'un nouveau type d'événement`users.messages.line.Click`.

* Ajout d'un nouveau type d'événement`users.messages.line.InboundReceive`.

* Ajout d'un nouveau type d'événement`users.messages.line.Send`.

* Ajout d'un nouveau type d'événement`users.messages.rcs.Abort`.

* Ajout d'un nouveau type d'événement`users.messages.rcs.Click`.

* Ajout d'un nouveau type d'événement`users.messages.rcs.Delivery`.

* Ajout d'un nouveau type d'événement`users.messages.rcs.InboundReceive`.

* Ajout d'un nouveau type d'événement`users.messages.rcs.Read`.

* Ajout d'un nouveau type d'événement`users.messages.rcs.Rejection`.

* Ajout d'un nouveau type d'événement`users.messages.rcs.Send`.

* Modifications apportées au champ « Type d'événement`users.messages.sms.Delivery` » :
    * Ajout d'un nouveau`boolean`champ `is_sms_fallback`: Indique si une solution de repli SMS a été tentée pour ce message RCS rejeté. Il est associé à l'événement « Réception/distribution de SMS ».

* Modifications apportées au champ « Type d'événement`users.messages.sms.DeliveryFailure` » :
    * Ajout d'un nouveau`boolean`champ `is_sms_fallback`: Indique si une solution de repli SMS a été tentée pour ce message RCS rejeté. Il est associé à l'événement « Réception/distribution de SMS ».

* Modifications apportées au champ « Type d'événement`users.messages.sms.Rejection` » :
    * Ajout d'un nouveau`boolean`champ `is_sms_fallback`: Indique si une solution de repli SMS a été tentée pour ce message RCS rejeté. Il est associé à l'événement « Réception/distribution de SMS ».

* Modifications apportées au champ « Type d'événement`users.messages.whatsapp.Delivery` » :
    * Ajout d'un nouveau`string`champ `flow_id`: ID unique du flux dans WhatsApp gestionnaire. Présent si l'utilisateur répond à un flux WhatsApp.
    * Ajout d'un nouveau`string`champ `template_name`: [PII] Nom du modèle dans le gestionnaire WhatsApp. Veuillez indiquer si vous envoyez un message type.
    * Ajout d'un nouveau`string`champ `message_id`: ID unique généré par Meta pour ce message

* Modifications apportées au champ « Type d'événement`users.messages.whatsapp.Failure` » :
    * Ajout d'un nouveau`string`champ `message_id`: ID unique généré par Meta pour ce message
    * Ajout d'un nouveau`string`champ `template_name`: [PII] Nom du modèle dans le gestionnaire WhatsApp. Veuillez indiquer si vous envoyez un message type.
    * Ajout d'un nouveau`string`champ `flow_id`: ID unique du flux dans WhatsApp gestionnaire. Présent si l'utilisateur répond à un flux WhatsApp.

* Modifications apportées au champ « Type d'événement`users.messages.whatsapp.InboundReceive` » :
    * Ajout d'un nouveau`string`champ `catalog_id`: ID catalogue d'un produit si celui-ci est mentionné dans le message entrant. Sinon, veuillez laisser vide.
    * Ajout d'un nouveau`string`champ `product_id`: identifiant du produit acheté
    * Ajout d'un nouveau`string`champ `flow_id`: ID unique du flux dans WhatsApp gestionnaire. Présent si l'utilisateur répond à un flux WhatsApp.
    * Ajout d'un nouveau`string`champ `flow_response_json`: [PII] Les valeurs du formulaire fournies par l'utilisateur. Présent si l'utilisateur répond à un flux WhatsApp.
    * Ajout d'un nouveau`string`champ `message_id`: ID unique généré par Meta pour ce message
    * Ajout d'un nouveau`string`champ `in_reply_to`: Lemessage_idcontenu du message auquel ce message répondait

* Modifications apportées au champ « Type d'événement`users.messages.whatsapp.Read` » :
    * Ajout d'un nouveau`string`champ `template_name`: [PII] Nom du modèle dans le gestionnaire WhatsApp. Veuillez indiquer si vous envoyez un message type.
    * Ajout d'un nouveau`string`champ `message_id`: ID unique généré par Meta pour ce message
    * Ajout d'un nouveau`string`champ `flow_id`: ID unique du flux dans WhatsApp gestionnaire. Présent si l'utilisateur répond à un flux WhatsApp.

* Modifications apportées au champ « Type d'événement`users.messages.whatsapp.Send` » :
    * Ajout d'un nouveau`string`champ `flow_id`: ID unique du flux dans WhatsApp gestionnaire. Présent si l'utilisateur répond à un flux WhatsApp.
    * Ajout d'un nouveau`string`champ `template_name`: [PII] Nom du modèle dans le gestionnaire WhatsApp. Veuillez indiquer si vous envoyez un message type.
    * Ajout d'un nouveau`string`champ `message_id`: ID unique généré par Meta pour ce message

## Modifications apportées à la version 2 (date de publication non disponible)

### Modifications relatives au stockage

* Ajout d'un nouveau type d'événement`users.behaviors.app.FirstSession`.

* Ajout d'un nouveau type d'événement`users.behaviors.app.SessionEnd`.

* Ajout d'un nouveau type d'événement`users.behaviors.app.SessionStart`.

* Ajout d'un nouveau type d'événement`users.behaviors.CustomEvent`.

* Ajout d'un nouveau type d'événement`users.behaviors.InstallAttribution`.

* Ajout d'un nouveau type d'événement`users.behaviors.liveactivity.PushToStartTokenChange`.

* Ajout d'un nouveau type d'événement`users.behaviors.liveactivity.UpdateTokenChange`.

* Ajout d'un nouveau type d'événement`users.behaviors.Location`.

* Ajout d'un nouveau type d'événement`users.behaviors.Purchase`.

* Ajout d'un nouveau type d'événement`users.behaviors.pushnotification.TokenStateChange`.

* Ajout d'un nouveau type d'événement`users.behaviors.subscription.GlobalStateChange`.

* Ajout d'un nouveau type d'événement`users.behaviors.subscriptiongroup.StateChange`.

* Ajout d'un nouveau type d'événement`users.behaviors.Uninstall`.

* Ajout d'un nouveau type d'événement`users.campaigns.Conversion`.

* Ajout d'un nouveau type d'événement`users.campaigns.EnrollInControl`.

* Ajout d'un nouveau type d'événement`users.canvas.Conversion`.

* Ajout d'un nouveau type d'événement`users.canvas.Entry`.

* Ajout d'un nouveau type d'événement`users.canvas.exit.MatchedAudience`.

* Ajout d'un nouveau type d'événement`users.canvas.exit.PerformedEvent`.

* Ajout d'un nouveau type d'événement`users.canvas.experimentstep.Conversion`.

* Ajout d'un nouveau type d'événement`users.canvas.experimentstep.SplitEntry`.

* Ajout d'un nouveau type d'événement`users.canvasstep.Progression`.

* Ajout d'un nouveau type d'événement`users.messages.banner.Abort`.

* Ajout d'un nouveau type d'événement`users.messages.banner.Click`.

* Ajout d'un nouveau type d'événement`users.messages.banner.Impression`.

* Ajout d'un nouveau type d'événement`users.messages.contentcard.Abort`.

* Ajout d'un nouveau type d'événement`users.messages.contentcard.Click`.

* Ajout d'un nouveau type d'événement`users.messages.contentcard.Dismiss`.

* Ajout d'un nouveau type d'événement`users.messages.contentcard.Impression`.

* Ajout d'un nouveau type d'événement`users.messages.contentcard.Send`.

* Ajout d'un nouveau type d'événement`users.messages.email.Abort`.

* Ajout d'un nouveau type d'événement`users.messages.email.Bounce`.

* Ajout d'un nouveau type d'événement`users.messages.email.Click`.

* Ajout d'un nouveau type d'événement`users.messages.email.Deferral`.

* Ajout d'un nouveau type d'événement`users.messages.email.Delivery`.

* Ajout d'un nouveau type d'événement`users.messages.email.MarkAsSpam`.

* Ajout d'un nouveau type d'événement`users.messages.email.Open`.

* Ajout d'un nouveau type d'événement`users.messages.email.Send`.

* Ajout d'un nouveau type d'événement`users.messages.email.SoftBounce`.

* Ajout d'un nouveau type d'événement`users.messages.email.Unsubscribe`.

* Ajout d'un nouveau type d'événement`users.messages.featureflag.Impression`.

* Ajout d'un nouveau type d'événement`users.messages.inappmessage.Abort`.

* Ajout d'un nouveau type d'événement`users.messages.inappmessage.Click`.

* Ajout d'un nouveau type d'événement`users.messages.inappmessage.Impression`.

* Ajout d'un nouveau type d'événement`users.messages.liveactivity.Outcome`.

* Ajout d'un nouveau type d'événement`users.messages.liveactivity.Send`.

* Ajout d'un nouveau type d'événement`users.messages.pushnotification.Abort`.

* Ajout d'un nouveau type d'événement`users.messages.pushnotification.Bounce`.

* Ajout d'un nouveau type d'événement`users.messages.pushnotification.IosForeground`.

* Ajout d'un nouveau type d'événement`users.messages.pushnotification.Open`.

* Ajout d'un nouveau type d'événement`users.messages.pushnotification.Send`.

* Ajout d'un nouveau type d'événement`users.messages.sms.Abort`.

* Ajout d'un nouveau type d'événement`users.messages.sms.CarrierSend`.

* Ajout d'un nouveau type d'événement`users.messages.sms.Delivery`.

* Ajout d'un nouveau type d'événement`users.messages.sms.DeliveryFailure`.

* Ajout d'un nouveau type d'événement`users.messages.sms.InboundReceive`.

* Ajout d'un nouveau type d'événement`users.messages.sms.Rejection`.

* Ajout d'un nouveau type d'événement`users.messages.sms.Send`.

* Ajout d'un nouveau type d'événement`users.messages.sms.ShortLinkClick`.

* Ajout d'un nouveau type d'événement`users.messages.webhook.Abort`.

* Ajout d'un nouveau type d'événement`users.messages.webhook.Failure`.

* Ajout d'un nouveau type d'événement`users.messages.webhook.Send`.

* Ajout d'un nouveau type d'événement`users.messages.whatsapp.Abort`.

* Ajout d'un nouveau type d'événement`users.messages.whatsapp.Click`.

* Ajout d'un nouveau type d'événement`users.messages.whatsapp.Delivery`.

* Ajout d'un nouveau type d'événement`users.messages.whatsapp.Failure`.

* Ajout d'un nouveau type d'événement`users.messages.whatsapp.InboundReceive`.

* Ajout d'un nouveau type d'événement`users.messages.whatsapp.Read`.

* Ajout d'un nouveau type d'événement`users.messages.whatsapp.Send`.

* Ajout d'un nouveau type d'événement`users.RandomBucketNumberUpdate`.

### Modifications relatives au partage des données

* Ajout d'un nouveau type d'événement`changelogs.GlobalControlGroup`.

* Ajout d'un nouveau type d'événement`users.behaviors.app.FirstSession`.

* Ajout d'un nouveau type d'événement`users.behaviors.app.NewsFeedImpression`.

* Ajout d'un nouveau type d'événement`users.behaviors.app.SessionEnd`.

* Ajout d'un nouveau type d'événement`users.behaviors.app.SessionStart`.

* Ajout d'un nouveau type d'événement`users.behaviors.CustomEvent`.

* Ajout d'un nouveau type d'événement`users.behaviors.geofence.DataEvent`.

* Ajout d'un nouveau type d'événement`users.behaviors.geofence.RecordEvent`.

* Ajout d'un nouveau type d'événement`users.behaviors.InstallAttribution`.

* Ajout d'un nouveau type d'événement`users.behaviors.liveactivity.PushToStartTokenChange`.

* Ajout d'un nouveau type d'événement`users.behaviors.liveactivity.UpdateTokenChange`.

* Ajout d'un nouveau type d'événement`users.behaviors.Location`.

* Ajout d'un nouveau type d'événement`users.behaviors.Purchase`.

* Ajout d'un nouveau type d'événement`users.behaviors.pushnotification.TokenStateChange`.

* Ajout d'un nouveau type d'événement`users.behaviors.subscription.GlobalStateChange`.

* Ajout d'un nouveau type d'événement`users.behaviors.subscriptiongroup.StateChange`.

* Ajout d'un nouveau type d'événement`users.behaviors.Uninstall`.

* Ajout d'un nouveau type d'événement`users.behaviors.UpgradedApp`.

* Ajout d'un nouveau type d'événement`users.campaigns.Conversion`.

* Ajout d'un nouveau type d'événement`users.campaigns.EnrollInControl`.

* Ajout d'un nouveau type d'événement`users.campaigns.FrequencyCap`.

* Ajout d'un nouveau type d'événement`users.campaigns.Revenue`.

* Ajout d'un nouveau type d'événement`users.canvas.Conversion`.

* Ajout d'un nouveau type d'événement`users.canvas.Entry`.

* Ajout d'un nouveau type d'événement`users.canvas.exit.MatchedAudience`.

* Ajout d'un nouveau type d'événement`users.canvas.exit.PerformedEvent`.

* Ajout d'un nouveau type d'événement`users.canvas.experimentstep.Conversion`.

* Ajout d'un nouveau type d'événement`users.canvas.experimentstep.SplitEntry`.

* Ajout d'un nouveau type d'événement`users.canvas.FrequencyCap`.

* Ajout d'un nouveau type d'événement`users.canvas.Revenue`.

* Ajout d'un nouveau type d'événement`users.canvasstep.Progression`.

* Ajout d'un nouveau type d'événement`users.messages.banner.Abort`.

* Ajout d'un nouveau type d'événement`users.messages.banner.Click`.

* Ajout d'un nouveau type d'événement`users.messages.banner.Impression`.

* Ajout d'un nouveau type d'événement`users.messages.contentcard.Abort`.

* Ajout d'un nouveau type d'événement`users.messages.contentcard.Click`.

* Ajout d'un nouveau type d'événement`users.messages.contentcard.Dismiss`.

* Ajout d'un nouveau type d'événement`users.messages.contentcard.Impression`.

* Ajout d'un nouveau type d'événement`users.messages.contentcard.Send`.

* Ajout d'un nouveau type d'événement`users.messages.email.Abort`.

* Ajout d'un nouveau type d'événement`users.messages.email.Bounce`.

* Ajout d'un nouveau type d'événement`users.messages.email.Click`.

* Ajout d'un nouveau type d'événement`users.messages.email.Deferral`.

* Ajout d'un nouveau type d'événement`users.messages.email.Delivery`.

* Ajout d'un nouveau type d'événement`users.messages.email.MarkAsSpam`.

* Ajout d'un nouveau type d'événement`users.messages.email.Open`.

* Ajout d'un nouveau type d'événement`users.messages.email.Send`.

* Ajout d'un nouveau type d'événement`users.messages.email.SoftBounce`.

* Ajout d'un nouveau type d'événement`users.messages.email.Unsubscribe`.

* Ajout d'un nouveau type d'événement`users.messages.featureflag.Impression`.

* Ajout d'un nouveau type d'événement`users.messages.inappmessage.Abort`.

* Ajout d'un nouveau type d'événement`users.messages.inappmessage.Click`.

* Ajout d'un nouveau type d'événement`users.messages.inappmessage.Impression`.

* Ajout d'un nouveau type d'événement`users.messages.liveactivity.Outcome`.

* Ajout d'un nouveau type d'événement`users.messages.liveactivity.Send`.

* Ajout d'un nouveau type d'événement`users.messages.newsfeedcard.Abort`.

* Ajout d'un nouveau type d'événement`users.messages.newsfeedcard.Click`.

* Ajout d'un nouveau type d'événement`users.messages.newsfeedcard.Impression`.

* Ajout d'un nouveau type d'événement`users.messages.pushnotification.Abort`.

* Ajout d'un nouveau type d'événement`users.messages.pushnotification.Bounce`.

* Ajout d'un nouveau type d'événement`users.messages.pushnotification.InfluencedOpen`.

* Ajout d'un nouveau type d'événement`users.messages.pushnotification.IosForeground`.

* Ajout d'un nouveau type d'événement`users.messages.pushnotification.Open`.

* Ajout d'un nouveau type d'événement`users.messages.pushnotification.Send`.

* Ajout d'un nouveau type d'événement`users.messages.sms.Abort`.

* Ajout d'un nouveau type d'événement`users.messages.sms.CarrierSend`.

* Ajout d'un nouveau type d'événement`users.messages.sms.Delivery`.

* Ajout d'un nouveau type d'événement`users.messages.sms.DeliveryFailure`.

* Ajout d'un nouveau type d'événement`users.messages.sms.InboundReceive`.

* Ajout d'un nouveau type d'événement`users.messages.sms.Rejection`.

* Ajout d'un nouveau type d'événement`users.messages.sms.Send`.

* Ajout d'un nouveau type d'événement`users.messages.sms.ShortLinkClick`.

* Ajout d'un nouveau type d'événement`users.messages.webhook.Abort`.

* Ajout d'un nouveau type d'événement`users.messages.webhook.Failure`.

* Ajout d'un nouveau type d'événement`users.messages.webhook.Send`.

* Ajout d'un nouveau type d'événement`users.messages.whatsapp.Abort`.

* Ajout d'un nouveau type d'événement`users.messages.whatsapp.Click`.

* Ajout d'un nouveau type d'événement`users.messages.whatsapp.Delivery`.

* Ajout d'un nouveau type d'événement`users.messages.whatsapp.Failure`.

* Ajout d'un nouveau type d'événement`users.messages.whatsapp.InboundReceive`.

* Ajout d'un nouveau type d'événement`users.messages.whatsapp.Read`.

* Ajout d'un nouveau type d'événement`users.messages.whatsapp.Send`.

* Ajout d'un nouveau type d'événement`users.RandomBucketNumberUpdate`.

* Ajout d'un nouveau type d'événement`users.UserDeleteRequest`.

* Ajout d'un nouveau type d'événement`users.UserOrphan`.
