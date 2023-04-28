---
nav_title: Segment.io pour Currents
article_title: Segment.io pour Currents
page_order: 1.2
alias: /partners/segment_for_currents/
description: "Cet article de référence présente le partenariat entre Currents Braze et Segment.io, une plateforme de données client qui recueille et transfère des informations entre les différentes sources de votre pile marketing."
page_type: partner
tool: Currents
search_tag: Partenaire

---

# Segment.io pour Currents  

> [Segment.io](https://segment.com) est une plateforme de données client qui vous aide à collecter, nettoyer et activer vos données client. Cet article de référence présente un aperçu de la connexion entre Currents Braze et Segment et décrit les exigences et les processus nécessaires pour assurer une mise en œuvre et une utilisation adaptées.

L’intégration de Braze et Segment.io vous permet de tirer parti de Currents Braze pour exporter vos événements Braze dans Segment.io et effectuer des analyses plus avancées sur les conversions, la rétention et l’utilisation des produits. 

## Conditions préalables

| Condition | Description |
| ----------- | ----------- |
| Compte Segment.io | Un [compte Segment.io](https://app.segment.com/login) est requis pour profiter de ce partenariat. |
| Utiliser Braze en tant que destination | Vous devez avoir déjà [configuré Braze en tant que destination]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/segment/segment/#connection-settings/) dans votre intégration Segment.io.<br><br>Vous devez également avoir fourni le bon centre de données Braze et la bonne clé API REST dans vos [paramètres de connexion]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/segment/segment/#connection-settings). |
| Currents | Pour réexporter des données dans Segment.io, vous devez avoir configuré [Currents Braze]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) pour votre compte. |
{: .reset-td-br-1 .reset-td-br-2}

## Intégration

### Étape 1 : Obtenir la clé d’écriture Segment.io

1. Dans votre tableau de bord Segment.io, sélectionnez votre source Segment.io. Ensuite, accédez à **Settings > API keys (Paramètres > Clés API)**. Vous trouverez ici la **clé d’écriture Segment.io**.
2. Dans Braze, accédez à **Currents > + Create Currents > Create Segment.io Export (Currents > + Créer des Currents > Créer une exportation Segment.io)**.
3. Ensuite, fournissez un nom d’intégration, une adresse e-mail de contact, une clé d’écriture et la région Segment.io.

![La page Currents Segment.io dans Braze. Ici, vous pouvez trouver des champs pour le nom de l’intégration, l’adresse e-mail de contact, la région Segment et la clé API.][3]

{% alert warning %}
Il est important de garder votre clé d’écriture Segment.io à jour. Le connecteur arrêtera d’envoyer des événements si les informations d’identification de votre connecteur expirent. Si cela persiste plus de **48 heures**, les événements du connecteur seront supprimés et les données seront perdues définitivement.
{% endalert %}

### Étape 2 : Exporter des événements d’engagement par message 

Ensuite, sélectionnez les événements d’engagement par message que vous souhaitez exporter. Reportez-vous aux événements d’exportation et au tableau des propriétés ci-dessous. Tous les événements envoyés à Segment.io incluront l’`external_user_id` de l’utilisateur en tant que `userId`. À l’heure actuelle, Braze n’envoie pas de données d’événements aux utilisateurs qui n’ont pas d’`external_user_id` défini.

![Liste de tous les événements d’engagement par message disponibles sur la page Currents Segment.io de Braze.][2]

Enfin, cliquez sur **Lancer Current**.

{% alert warning %}
Si vous avez l’intention de créer plusieurs connecteurs Currents identiques (par exemple, deux connecteurs d’événement d’engagement par message), ces connecteurs doivent faire partie de différents groupes d’apps. L’intégration Currents Segment.io dans Braze ne permet pas d’isoler des événements de différentes applications dans un seul groupe d’apps, le non-respect de cette consigne entraînera des dédoublements et des pertes de données. 
{% endalert %}

Pour en savoir plus, consultez la [documentation](https://segment.com/docs/sources/cloud-apps/appboy/) de Segment.io.

## Événements Currents pris en charge

Braze prend en charge l’exportation des données suivantes vers Segment.io, répertoriées dans les glossaires d’événements Currents sur le [comportement de l’utilisateur]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/customer_behavior_events/) et l’[engagement par message]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events/) :
 
### Comportements
- Désinstallation : `users.behaviors.Uninstall`
- Application (impression du fil d’actualité)
  - `users.behaviors.app.NewsFeedImpression`
- Abonnement (changement de statut global) : `users.behaviors.subscription.GlobalStateChange`
- Groupe d’abonnement (changement de statut) : `users.behaviors.subscriptiongroup.StateChange`
  
### Campagnes
- Abandonner : `users_campaigns_abort`
- Conversion : `users.campaigns.Conversion`
- Contrôle de l’inscription : `users.campaigns.EnrollInControl`
  
### Canvas
- Abandonner : `users_canvas_abort`
- Conversion : `users.canvas.Conversion`
- Entrée : `users.canvas.Entry`
- Sortie (correspond à l’audience, événement réalisé)
  - `users.canvas.exit.MatchedAudience`
  - `users.canvas.exit.PerformedEvent`
- Étape de l’expérience (conversion, entrée fractionnée)
  - `users.canvas.experimentstep.Conversion`
  - `users.canvas.experimentstep.SplitEntry`

### Messages
- Carte de contenu (abandon, clic, rejet, impression, envoi)
  - `users.messages.contentcard.Abort`
  - `users.messages.contentcard.Click`
  - `users.messages.contentcard.Dismiss`
  - `users.messages.contentcard.Impression`
  - `users.messages.contentcard.Send`
- E-mail (abandon, rebond, clic, livraison, marqué comme courrier indésirable, ouverture, envoi, soft bounce, désabonnement)
  - `users.messages.email.Abort`
  - `users.messages.email.Bounce`
  - `users.messages.email.Click`
  - `users.messages.email.Delivery`
  - `users.messages.email.MarkAsSpam`
  - `users.messages.email.Open`
  - `users.messages.email.Send`
  - `users.messages.email.SoftBounce`
  - `users.messages.email.Unsubscribe`
- Message in-app (abandon, clic, impression)
  - `users.messages.inappmessage.Abort`
  - `users.messages.inappmessage.Click`
  - `users.messages.inappmessage.Impression`
- Carte de fil d’actualité (abandon, clic, impression)
  - `users.messages.newsfeedcard.Abort`
  - `users.messages.newsfeedcard.Click`
  - `users.messages.newsfeedcard.Impression`
- Notification push (abandon, rebond, premier plan iOS, ouverture, envoi)
  - `users.messages.pushnotification.Abort`
  - `users.messages.pushnotification.Bounce`
  - `users.messages.pushnotification.IosForeground`
  - `users.messages.pushnotification.Open`
  - `users.messages.pushnotification.Send`
- SMS (abandon, envoi par le transporteur, livraison, échec de livraison, réception entrante, rejet, envoi, clic sur le lien court)
  - `users.messages.sms.Abort`
  - `users.messages.sms.CarrierSend`
  - `users.messages.sms.Delivery`
  - `users.messages.sms.DeliveryFailure`
  - `users.messages.sms.InboundReceive`
  - `users.messages.sms.Rejection`
  - `users.messages.sms.Send`
  - `users.messages.sms.ShortLinkClick`
- Webhook (abandon, envoi)
  - `users.messages.webhook.Abort`
  - `users.messages.webhook.Send`

[1]: {% image_buster /assets/img/segment/segment_currents1.png %}
[2]: {% image_buster /assets/img/segment/segment_currents.png %}
[3]: {% image_buster /assets/img/segment/segment.png %}
