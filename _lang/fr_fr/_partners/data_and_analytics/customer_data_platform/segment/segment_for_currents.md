---
nav_title: Segment pour Currents
article_title: Segment pour Currents
page_order: 2
alias: /partners/segment_for_currents/
description: "Cet article de référence décrit le partenariat entre Braze Currents et Segment, une plateforme de données clients qui collecte et achemine des informations entre les sources de votre stack marketing."
page_type: partner
tool: Currents
search_tag: Partner

---

# Segment pour Currents  

> [Segment](https://segment.com) est une plateforme de données clients qui vous aide à collecter, nettoyer et activer vos données clients. Cet article de référence donnera un aperçu de la connexion entre Braze Currents et Segment et décrira les exigences et les processus pour une mise en œuvre et une utilisation appropriées.

L'intégration de Braze et de Segment vous permet de tirer parti de Braze Currents pour exporter vos événements Braze vers Segment afin d'approfondir les analyses sur les conversions, la rétention et l'utilisation des produits. 

## Conditions préalables

| Condition | Description |
| ----------- | ----------- |
| Compte Segment | Un [compte Segment](https://app.segment.com/login) est nécessaire pour bénéficier de ce partenariat. |
| Destination Braze | Vous devez déjà avoir [configuré Braze comme destination]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment/#connection-settings/) dans votre intégration de segment.<br><br>Cela inclut la fourniture du centre de données Braze et de la clé API REST appropriés dans vos paramètres de [connexion]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment/#connection-settings). |
| Currents | Pour réexporter les données vers Segment, [Braze]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) Currents doit être configuré pour votre compte. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Intégration

### Étape 1 : Obtenir la clé d'écriture du segment

Dans votre tableau de bord Segment, sélectionnez la source Segment. Ensuite, allez dans **Paramètres > Clés d'API**. Vous trouverez ici la **clé d'écriture des segments**.

{% alert warning %}
Il est important de maintenir à jour la clé de rédaction de votre segment. Si les informations d'identification de votre connecteur expirent, le connecteur cessera d'envoyer des événements. Si cette situation persiste pendant plus de **48 heures**, les événements du connecteur seront abandonnés et les données seront définitivement perdues.
{% endalert %}

### Étape 2 : Création d'un nouveau connecteur Currents

1. Dans Braze, accédez à **Intégrations partenaires** > **Exportation de données**.
2. Cliquez sur **\+ Créer un nouveau flux Currents** > **Exporter des données Segment**.
3. Ensuite, indiquez le nom de l'intégration, l'e-mail du contact, la clé d'écriture du segment et la région du segment.

![La page Segment Currents dans Braze. Vous trouverez ici des champs pour le nom de l'intégration, l'e-mail du contact, la région du segment et la clé API.]({% image_buster /assets/img/segment/segment_currents_integration_config.png %})

### Étape 3 : Exporter les événements d'engagement des messages

Sélectionnez ensuite les événements d'engagement des messages que vous souhaitez exporter. Consultez le tableau des propriétés et des événements d'exportation ci-dessous. Tous les événements envoyés au segment comprendront le site `external_user_id` de l'utilisateur en tant que `userId` et le site `braze_id` de l'utilisateur en tant que `anonymousId`.

N'oubliez pas que Braze n'envoie les données d'événements que pour les utilisateurs sans `external_user_id` si l'option **Inclure les événements des utilisateurs anonymes** est cochée.

{% alert important %}
L'exportation d'utilisateurs anonymes est actuellement en accès anticipé. Contactez votre gestionnaire de compte Braze si vous souhaitez participer à cet accès anticipé.
{% endalert %}

![Liste de tous les événements d'engagement aux messages disponibles sur la page Segment Currents de Braze.]({% image_buster /assets/img/segment/segment_currents_data_config.png %})

Enfin, sélectionnez **Lancer Currents**.

{% alert warning %}
Si vous avez l'intention de créer plusieurs connecteurs Currents identiques (par exemple, deux connecteurs d'événement d'engagement lié aux messages), ils doivent se trouver dans des espaces de travail différents. Étant donné que l'intégration Segment Currents Braze ne peut pas isoler les événements de différentes applications au sein d’un seul espace de travail, s’ils se trouvent dans un même espace, cela entraînera une déduplication inutile des données et des pertes de données.
{% endalert %}

Pour en savoir plus, consultez la [documentation](https://segment.com/docs/connections/sources/catalog/cloud-apps/braze/) sur les segments.

## Mettre à jour votre version actuelle

{% multi_lang_include updating_currents.md %}

## Événements Currents pris en charge

Braze prend en charge l'exportation vers Segment des données suivantes répertoriées dans les glossaires des événements Currents relatifs au [comportement des utilisateurs]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/) et à [l'engagement des messages]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) :
 
### Comportements
- Désinstaller : `users.behaviors.Uninstall`
- Abonnement (changement d'état global) : `users.behaviors.subscription.GlobalStateChange`
- Groupe d'abonnements (changement d'état) : `users.behaviors.subscriptiongroup.StateChange`
  
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

