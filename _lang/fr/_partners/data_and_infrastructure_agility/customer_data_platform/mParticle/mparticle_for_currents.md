---
nav_title: mParticle pour Currents
article_title: mParticle pour Currents
page_order: 0.5
alias: /partners/mparticle_for_currents/
description: "Cet article de référence présente le partenariat entre Currents Braze et mParticle, une plateforme de données client qui recueille et achemine des informations entre les différentes sources de votre pile marketing."
page_type: partner
tool: Currents
search_tag: Partenaire

---

# mParticle pour Currents

> [mParticle](https://www.mparticle.com) est une plateforme de données client qui collecte et transfère des informations issues de plusieurs sources vers divers emplacements de votre pile marketing.

L’intégration de Braze et de mParticle permet de contrôler de manière harmonieuse le flux d’informations entre les deux systèmes. Avec Currents, vous pouvez également connecter des données à mParticle pour les rendre utilisables sur toute la pile d’outils de croissance. 

## Conditions préalables

| Condition | Description |
| ----------- | ----------- |
| Compte mParticle | Un [compte mParticle](https://app.mparticle.com/login) est requis pour profiter de ce partenariat. |
| Currents | Pour réexporter des données dans mParticle, vous devez avoir configuré [Currents Braze]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) pour votre compte. |
| Clé de serveur à serveur mParticle<br><br>Clé secrète de serveur à serveur mParticle | Vous pouvez obtenir ces clés en accédant à votre tableau de bord de mParticle et en créant les [flux nécessaires](#step-1-create-feeds) qui permettent à mParticle de recevoir des données d’interaction Braze pour les plateformes iOS, Android et Web.|
{: .reset-td-br-1 .reset-td-br-2}

## Intégration

### Étape 1 : Créer des flux

À partir de votre compte administrateur mParticle, accédez à **Setup > Inputs (Configuration > Entrées)**. Recherchez **Braze** dans le **Directory (Répertoire)** mParticle et ajoutez l’intégration de flux.

L’intégration de flux Braze prend en charge quatre flux distincts : iOS, Android, Web et indépendant. Le flux indépendant peut être utilisé pour des événements, tels que des e-mails qui ne sont pas connectés à une plateforme. Vous devrez créer une entrée pour chaque flux de plateforme principal. Vous pouvez créer des entrées supplémentaires à partir de **Setup (Configuration) > Inputs (Entrées)**, sur l’onglet **Feed Configurations (Configurations des flux)**.

![][1]

Pour chaque flux, sélectionnez la plateforme correspondante dans la liste sous **Act as Platform (Agir en tant que plateforme)**. Si vous ne voyez pas d’option pour sélectionner un flux **act-as (agir en tant que)**, les données seront traitées comme indépendantes, mais pourront toujours être transmises aux sorties d’entrepôt de données.

![La première boîte de dialogue d’intégration vous invite à nommer la configuration, à déterminer un statut de flux et à sélectionner une plateforme « agir en tant que ».][2]{: style="max-width:40%;"}  ![La deuxième boîte de dialogue d’intégration affichant la clé serveur à serveur et la clé secrète serveur à serveur.][3]{: style="max-width:37%;"}

mParticle vous fournira une clé et une clé secrète au moment où vous créerez chaque entrée. Copiez ces informations d’identification en faisant attention à bien noter le flux auquel correspond chaque paire d’identifiants.

### Étape 2 : Créer un Current

Dans Braze, accédez à **Currents > + Create Current (+ Créer un Current) > Create mParticle Export (Créer une exportation mParticle)**. Fournissez un nom d’intégration, une adresse e-mail de contact, la clé API mParticle et la clé secrète mParticle pour chaque plateforme. Ensuite, sélectionnez les événements que vous souhaitez suivre (consultez la liste des événements disponibles). Enfin, cliquez sur **‬Launch Current (Lancer le Current)**

![La page mParticle Currents dans Braze. Ici, vous pouvez trouver des champs pour le nom de l’intégration, l’adresse e-mail de contact, la clé API et la clé secrète.]({% image_buster /assets/img_archive/currents-mparticle-edit.png %})

{% alert important %}
Il est important de garder votre clé API mParticle et votre clé secrète mParticle à jour : si les informations d’identification de votre connecteur expirent, le connecteur cessera d’envoyer des événements. Si cela persiste plus de **48 heures**, les événements du connecteur seront supprimés et les données seront perdues définitivement.
{% endalert %}

Tous les événements envoyés à mParticle incluront l’`external_user_id` de l’utilisateur en tant que `customerid`. À l’heure actuelle, Braze n’envoie pas de données d’événements aux utilisateurs qui n’ont pas d’`external_user_id` défini.

## Événements Currents pris en charge

Braze prend en charge l’exportation des données suivantes vers mParticle, répertoriées dans les glossaires d’événements Currents sur le [comportement de l’utilisateur]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/customer_behavior_events/) et l’[engagement par message]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events/) :

### Comportements
- Désinstallation : `users.behaviors.Uninstall`
- Application (impression du fil d’actualité) : `users.behaviors.app.NewsFeedImpression`
- Abonnement (changement de statut global) : `users.behaviors.subscription.GlobalStateChange`
- Groupe d’abonnement (changement de statut) : `users.behaviors.subscriptiongroup.StateChange`
  
### Campagnes
<!--- Abort// not live yet-->
- Conversion : `users.campaigns.Conversion`
- Contrôle de l’inscription : `users.campaigns.EnrollInControl`
  
### Canvas
<!--- Abort// not live yet-->
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
- Message in-app (abandon, clic, impression)
  - `users.messages.inappmessage.Abort`
  - `users.messages.inappmessage.Click`
  - `users.messages.inappmessage.Impression`
- Carte de fil d’actualité (abandon, clic, impression)
  - `users.messages.newsfeedcard.Abort`
  - `users.messages.newsfeedcard.Click`
  - `users.messages.newsfeedcard.Impression`
- Notification push (abandon, rebond, ouverture, envoi)
  - `users.messages.pushnotification.Abort`
  - `users.messages.pushnotification.Bounce`
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

Pour en savoir plus sur l’intégration de mParticle, consultez la documentation de mParticle [ici](http://docs.mparticle.com/integrations/braze/feed).

[1]: {% image_buster /assets/img/braze-feed-inputs.png %}
[2]: {% image_buster /assets/img/braze-feed-act1.png %}
[3]: {% image_buster /assets/img/braze-feed-act2.png %}
