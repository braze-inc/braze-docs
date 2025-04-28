---
nav_title: Mixpanel
article_title: Mixpanel
alias: /partners/mixpanel_for_currents/
description: "Cet article de référence présente le partenariat entre Braze et Mixpanel, une plateforme d'analyse/analytique commerciale, vous permettant d'importer des Cohortes Mixpanel dans Braze pour créer des segments Braze qui peuvent être utilisés pour cibler les utilisateurs dans les futures campagnes ou Canvases Braze."
page_type: partner
search_tag: Partner
tool: Currents

---
 
# [![Cours Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/mixpanel-integration-with-braze/339085/scorm/2u7y2e6qrldh2){: style="float:right;width:120px;border:0;" class="noimgborder"}Mixpanel

> [Mixpanel](https://mixpanel.com/) est une plateforme d'analyse commerciale qui vous permet d'exporter des événements de Mixpanel vers d'autres plateformes afin d'effectuer des analyses plus approfondies. Les données collectées peuvent ensuite être utilisées pour créer des rapports personnalisés et mesurer l'engagement et la rétention des utilisateurs.

L'intégration de Braze et Mixpanel vous permet d'[importer des cohortes Mixpanel dans Braze]({{site.baseurl}}/partners/data_and_infrastructure_agility/cohort_import/mixpanel/) afin de créer des segments Braze qui peuvent être utilisés pour cibler les utilisateurs dans les futures campagnes Braze ou Canvases. Vous pouvez également tirer parti de Braze Currents pour [exporter vos événements de Braze vers Mixpanel](#data-export-integration) afin d'obtenir des analyses plus approfondies sur les conversions, la rétention et l'utilisation des produits. 

## Conditions préalables

| Condition | Description |
|---|---|
| Compte Mixpanel | Un [compte Mixpanel](https://mixpanel.com/) est nécessaire pour profiter de ce partenariat. |
| Currents | Pour pouvoir exporter des données vers Mixpanel, vous devez avoir configuré [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) pour votre compte. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" } 

## Intégration de l'exportation des données

Vous trouverez ci-dessous une liste complète des événements qui peuvent être exportés de Braze vers Mixpanel. Tous les événements envoyés à Mixpanel comprendront l'adresse `external_user_id` de l'utilisateur comme ID distinct de Mixpanel. À l'heure actuelle, Braze n'envoie pas de données d'événement pour les utilisateurs dont le site `external_user_id` n'est pas paramétré.

Vous pouvez exporter deux types d'événements vers Mixpanel : Les [événements d'engagement des messages](#supported-currents-events) constitués des événements Braze directement liés à l'envoi de messages, et des [événements de comportement des clients](#supported-currents-events) comprenant d'autres activités de l'application ou du site Web telles que les sessions, les événements personnalisés et les achats suivis par l'intermédiaire de la plateforme. Tous les événements personnalisés sont précédés du préfixe `[Braze Custom Event]`. Les propriétés d'événements personnalisés et les propriétés d'événements d'achat sont précédées des préfixes `[Custom event property]` et `[Purchase property]`, respectivement.

Contactez votre gestionnaire de compte ou ouvrez un [ticket d'assistance][support] si vous avez besoin d'accéder à des droits d'événements supplémentaires.

### Étape 1 : Obtenir les informations d'identification de Mixpanel

Dans votre tableau de bord Mixpanel, cliquez sur les **paramètres du projet**, qu'il s'agisse d'un nouveau projet ou d'un projet existant. Vous y trouverez le secret de l'API de Mixpanel et le jeton de Mixpanel. Ces informations d'identification seront utilisées à l'étape suivante pour créer votre connexion à Currents. 

### Étape 2 : Créer des flux Braze Currents

Dans Braze, naviguez vers \*\*Currents > **\+ Créer un flux Currents** > **Créer un export Mixpanel.** Indiquez le nom de l'intégration, l'e-mail du contact, le secret de l'API Mixpanel et le jeton Mixpanel dans les champs répertoriés. Ensuite, sélectionnez les événements que vous souhaitez suivre ; une liste des événements disponibles est fournie. Enfin, cliquez sur **Lancer le flux Currents**.

![La page Braze Mixpanel Currents. Cette page comprend des champs pour spécifier le nom de l'intégration, l'e-mail du contact, le secret de l’API et le jeton d'exportation Mixpanel. La moitié inférieure de la page Currents énumère les événements Currents disponibles que vous pouvez envoyer.]({% image_buster /assets/img_archive/mixpanel4.png %}){: style="max-width:80%;"}

{% tab note %}
Consultez la [documentation sur l'intégration de](https://help.mixpanel.com/hc/en-us/articles/360001243663) Mixpanel pour en savoir plus.
{% endtab %}

## Événements soutenus par Currents

Braze prend en charge l'exportation vers Mixpanel des données suivantes répertoriées dans les glossaires des [comportements des utilisateurs]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/) et [des événements d'engagement lié aux messages]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) :

### Comportements
- Événement personnalisé : `users.behaviors.CustomEvent`
- Attribution d'installation : `users.behaviors.InstallAttribution`
- Emplacement : `users.behaviors.Location`
- Achat : `users.behaviors.Purchase`
- Désinstaller : `users.behaviors.Uninstall`
- App (première session, fin de la session, début de la session)
  - `users.behaviors.app.FirstSession`
  - `users.behaviors.app.SessionEnd`
  - `users.behaviors.app.SessionStart`
- Abonnement (changement d'état global) : `users.behaviors.subscription.GlobalStateChange`
- Groupe d'abonnement (changement d'état) : `users.behaviors.subscriptiongroup.StateChange`
  
### Campagnes
- Abandonner : `users_campaigns_abort`
- Conversion : `users.campaigns.Conversion`
- EnrollinControl : `users.campaigns.EnrollInControl`
  
### Canevas
- Abandonner : `users_canvas_abort`
- Conversion : `users.canvas.Conversion`
- Entrée : `users.canvas.Entry`
- Sortie (audience assortie, événement réalisé)
  - `users.canvas.exit.MatchedAudience`
  - `users.canvas.exit.PerformedEvent`
- Étape de l'expérience (conversion, entrée fractionnée)
  - `users.canvas.experimentstep.Conversion`
  - `users.canvas.experimentstep.SplitEntry`

### Messages
- Carte de contenu (abandon, clic, fermeture de la carte de contenu, impression, envoi)
  - `users.messages.contentcard.Abort`
  - `users.messages.contentcard.Click`
  - `users.messages.contentcard.Dismiss`
  - `users.messages.contentcard.Impression`
  - `users.messages.contentcard.Send`
- E-mail (abandon, rebond, clic, distribution, marquage comme spam, ouverture, envoi, rejet temporaire, désinscription)
  - `users.messages.email.Abort`
  - `users.messages.email.Bounce`
  - `users.messages.email.Click`
  - `users.messages.email.Delivery`
  - `users.messages.email.MarkAsSpam`
  - `users.messages.email.Open`
  - `users.messages.email.Send`
  - `users.messages.email.SoftBounce`
  - `users.messages.email.Unsubscribe`
- message intégré à l'application (abandon, clic, impression)
  - `users.messages.inappmessage.Abort`
  - `users.messages.inappmessage.Click`
  - `users.messages.inappmessage.Impression`
- Notification push (abandon, rebond, iOSforeground, ouverture, envoi)
  - `users.messages.pushnotification.Abort`
  - `users.messages.pushnotification.Bounce`
  - `users.messages.pushnotification.IosForeground`
  - `users.messages.pushnotification.Open`
  - `users.messages.pushnotification.Send`
- SMS (abandon, envoi par transporteur, réception, échec de la réception, réception entrante, rejet, envoi, clic sur un lien court)
  - `users.messages.sms.Abort`
  - `users.messages.sms.Delivery`
  - `users.messages.sms.DeliveryFailure`
  - `users.messages.sms.InboundReceive`
  - `users.messages.sms.Rejection`
  - `users.messages.sms.Send`
  - `users.messages.sms.ShortLinkClick`
- Webhook (annuler, envoyer)
  - `users.messages.webhook.Abort`
  - `users.messages.webhook.Send`
- WhatsApp (abandon, distribution, échec, réception entrante, lecture, envoi)
  - `users.messages.whatsapp.Abort`
  - `users.messages.whatsapp.Delivery`
  - `users.messages.whatsapp.Failure`
  - `users.messages.whatsapp.InboundReceive`
  - `users.messages.whatsapp.Read`
  - `users.messages.whatsapp.Send`
  
[support]: {{site.baseurl}}/braze_support/
[1]: {% image_buster /assets/img_archive/mixpanel1.png %}
[2]: {% image_buster /assets/img_archive/mixpanel2.png %}
[3]: {% image_buster /assets/img_archive/mixpanel3.png %}
[4]: {% image_buster /assets/img_archive/mixpanel4.png %}
