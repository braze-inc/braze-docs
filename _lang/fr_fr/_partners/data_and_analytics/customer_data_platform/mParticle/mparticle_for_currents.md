---
nav_title: mParticle pour Currents
article_title: mParticle pour Currents
alias: /partners/mparticle_for_currents/
description: "Cet article de référence présente le partenariat entre Braze Currents et mParticle, une plateforme de données client qui collecte et achemine les données entre les sources de votre pile marketing."
page_type: partner
tool: Currents
search_tag: Partner

---

# mParticle pour Currents

> [mParticle](https://www.mparticle.com) est une plateforme de données client qui collecte et achemine des informations provenant de sources multiples vers divers autres emplacements de votre pile marketing.

L'intégration de Braze et mParticle vous permet de contrôler de façon fluide le flux d'informations entre les deux systèmes. Avec [Currents]({{site.baseurl}}/user_guide/data/braze_currents/), vous pouvez également connecter les données à mParticle pour les rendre exploitables dans l'ensemble des outils de croissance. 

## Conditions préalables

| Condition | Description |
| ----------- | ----------- |
| Currents | Pour pouvoir exporter des données dans mParticle, vous devez avoir configuré [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) pour votre compte. |
| Compte mParticle | Un [compte mParticle](https://app.mparticle.com/login) est nécessaire pour profiter de ce partenariat. |
| Clé et secret du serveur mParticle | Vous pouvez les obtenir en naviguant dans votre tableau de bord de mParticle et en créant les [flux nécessaires](#step-1-create-feeds) qui permettent à mParticle de recevoir les données d'interaction de Braze pour les plateformes iOS, Android et Web.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## À propos de mParticle credentials

mParticle dispose d'informations d'identification au niveau de l'application et de l'espace de travail, qui ont une incidence sur la manière dont vos événements sont envoyés.

- **Au niveau de l'application :** mParticle séparera les événements par chaque application individuelle, ce qui signifie que les informations d'identification au niveau de l'application que vous donnez à votre application iOS ne peuvent être utilisées que pour envoyer des événements spécifiques à iOS.
- **Au niveau de l'espace de travail :** mParticle regroupe tous les événements (qui ne sont **pas** spécifiques à une application), ce qui signifie que les informations d'identification au niveau de l'espace de travail que vous donnez à votre groupe d'applications seront utilisées pour envoyer tous vos événements non spécifiques à une application.

Vous pouvez considérer que mParticle ingère un "flux" basé sur chaque application individuelle. Par exemple, si vous avez une application pour iOS, une pour Android et une pour le Web, vos événements seront décousus. Cela signifie que si vous fournissez les mêmes données d'identification pour chaque application, un seul flux mParticle sera utilisé pour recevoir toutes les données de toutes vos applications, sans duplication.

## Intégration

### Étape 1 : Créer des flux

Depuis votre compte administrateur mParticle, accédez à **Configuration > Entrées**. Recherchez **Braze** dans le **répertoire** mParticle et ajoutez l'intégration des flux.

La fonction d'intégration des flux de Braze prend en charge quatre flux distincts : iOS, Android, Web et générique. Le flux non lié peut être utilisé pour des événements tels que des e-mails qui ne sont pas connectés à une plateforme. Vous devrez créer une entrée pour chaque flux de la plateforme principale. Vous pouvez créer des entrées supplémentaires à partir de **Configuration > Entrées**, dans l'onglet **Configurations d'alimentation.** 

![]({% image_buster /assets/img/braze-feed-inputs.png %})

Pour chaque flux, sous **Agir en tant que plateforme**, sélectionnez la plateforme correspondante dans la liste. Si vous ne voyez pas d'option pour sélectionner un flux **act-as**, les données seront traitées comme non liées, mais peuvent toujours être transmises aux sorties de l'entrepôt de données.

![La première boîte de dialogue d'intégration vous invite à fournir un nom de configuration, à déterminer l'état des flux et à sélectionner une plate-forme à utiliser.]({% image_buster /assets/img/braze-feed-act1.png %}){: style="max-width:40%;"}  ![La deuxième boîte de dialogue d'intégration affiche la clé et le secret serveur-serveur.]({% image_buster /assets/img/braze-feed-act2.png %}){: style="max-width:37%;"}

Lorsque vous créez chaque entrée, mParticle vous fournit une clé et un secret. Copiez ces informations d'identification, en veillant à noter à quel flux correspond chaque paire d'informations d'identification.

### Étape 2 : Créer un flux Currents

Dans Braze, naviguez vers **Currents > + Créer un flux Currents > Créer un export mParticle**. Indiquez un nom d'intégration, un e-mail de contact ainsi que la clé API mParticle et la clé secrète mParticle pour chaque plateforme. Ensuite, sélectionnez les événements que vous souhaitez suivre ; une liste des événements disponibles est fournie. Enfin, cliquez sur **Lancer le flux Currents**

![La page mParticle Currents dans Braze. Cette page contient des champs permettant de spécifier le nom de l'intégration, l'e-mail du contact, la clé API et la clé secrète.]({% image_buster /assets/img_archive/currents-mparticle-edit.png %})

{% alert important %}
Il est important de tenir à jour votre clé API mParticle et votre clé secrète mParticle ; si les informations d'identification de votre connecteur expirent, le connecteur cessera d'envoyer des événements. Si cette situation persiste pendant plus de **48 heures**, les événements du connecteur seront abandonnés et les données seront définitivement perdues.
{% endalert %}

Tous les événements envoyés à mParticle comprendront le site `external_user_id` de l'utilisateur en tant que `customerid`. À l'heure actuelle, Braze n'envoie pas de données d'événement pour les utilisateurs dont le site `external_user_id` n'est pas paramétré. Si vous souhaitez mapper le paramètre `external_user_id` à un autre ID dans mParticle qui n’est pas l'ID par défaut `customerid`, veuillez contacter votre gestionnaire du succès des clients Braze. 

## Événements soutenus par Currents

Braze prend en charge l'exportation vers mParticle des données comportementales suivantes répertoriées dans les glossaires des [comportements des utilisateurs]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/) et des événements d'[engagement aux messages de]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) Braze Currents :

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
- E-mail (annulation, rebond, clic, distribution, markasspam, ouverture, envoi, softbounce, désinscription)
- Message in-app (abandon, clic, impression)
  - `users.messages.inappmessage.Abort`
  - `users.messages.inappmessage.Click`
  - `users.messages.inappmessage.Impression`
- Notification push (abandon, rebond, ouverture, envoi)
  - `users.messages.pushnotification.Abort`
  - `users.messages.pushnotification.Bounce`
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


Pour en savoir plus sur l'intégration de mParticle, consultez leur documentation [ici](http://docs.mparticle.com/integrations/braze/feed).

