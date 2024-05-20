---
nav_title: Mixpanel pour Currents
article_title: Mixpanel pour Currents
page_order: 0
alias: /partners/mixpanel_for_currents/
description: "Cet article de référence présente le partenariat entre Currents Braze et Mixpanel, une plateforme d’analyses commerciales qui vous permet d’importer des cohortes Mixpanel dans Braze pour créer des segments Braze qui peuvent être utilisés afin de cibler des utilisateurs dans de futures campagnes ou de futurs Canvas de Braze."
page_type: partner
search_tag: Partenaire
tool: Currents

---
 
# [![Cours d’apprentissage Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/mixpanel-integration-with-braze/339085/scorm/2u7y2e6qrldh2){: style="float:right;width:120px;border:0;" class="noimgborder"}Mixpanel pour Currents

> [Mixpanel](https://mixpanel.com/) est une plateforme d’analyses commerciales qui vous permet d’exporter des événements depuis Mixpanel vers d’autres plateformes afin d’effectuer des analyses plus poussées. Les données collectées peuvent ensuite être utilisées pour créer des rapports personnalisés et mesurer le taux d’engagement et de rétention des utilisateurs.

L’intégration de Braze et Mixpanel vous permet d’[importer des cohortes Mixpanel dans Braze](#data-import-integration) pour créer des segments Braze qui peuvent être utilisés afin de cibler des utilisateurs dans de futures campagnes ou de futurs Canvas de Braze. Vous pouvez également tirer parti des currents Braze pour [exporter vos événements Braze dans Mixpanel](#data-export-integration) et effectuer des analyses plus approfondies sur les conversions, la rétention et l’utilisation des produits. 

## Conditions préalables

| Condition | Description |
|---|---|
| Compte Mixpanel | Un [Compte Mixpanel](https://mixpanel.com/) est requis pour profiter de ce partenariat. |
| Currents | Pour exporter des données dans Mixpanel, vous devez avoir configuré [currents Braze]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) pour votre compte. |
{: .reset-td-br-1 .reset-td-br-2} 

## Intégration de l’importation de données

Utilisez le partenariat entre Braze et Mixpanel pour configurer votre intégration et importer des cohortes Mixpanel directement dans Braze afin de les recibler, créant ainsi une boucle de données complète d’un système à l’autre. Cela vous permet d’effectuer des analyses plus approfondies à l’aide de Mixpanel et d’exécuter vos stratégies de manière harmonieuse avec Braze.

Toutes les intégrations que vous avez configurées seront prises en compte dans le volume de points de données de votre compte.

{% alert important %}
Conformément aux politiques de conservation des données de Mixpanel, les événements envoyés avant le 1er janvier 2010 seront supprimés pendant l’importation.
{% endalert %}

### Étape 1 : Obtenir la clé d’importation des données Braze

Dans Braze, accédez à **Technology Partners (Partenaires technologiques)** et sélectionnez **Mixpanel**. Ici, vous trouverez l’endpoint REST pour générer votre clé d’importation des données Braze. Une fois la clé générée, vous pouvez créer une nouvelle clé ou invalider une clé existante. La clé d’importation des données et l’endpoint REST sont utilisés à l’étape suivante lors de la configuration d’un postback dans le tableau de bord de Mixpanel.<br><br>![]({% image_buster /assets/img_archive/currents-mixpanel-edit.png %})

### Étape 2 : Configurer l’intégration Braze dans Mixpanel

Dans Mixpanel, accédez à **Data Management > Integrations (Gestion des données > Intégrations).** Ensuite, sélectionnez l’onglet Intégration Braze, puis cliquez sur **Connect (Connexion)**. Dans l’invite qui apparaît, fournissez la clé d’importation des données de Braze et l’endpoint REST, puis cliquez sur **Continue (Continuer)**.

![]({% image_buster /assets/img_archive/mixpanel2.png %}){: style="max-width:50%;"}

### Étape 3 : Exporter une cohorte Mixpanel vers Braze

Dans Mixpanel, accédez à **Data Management > Cohorts (Gestion des données > Cohortes).** Sélectionnez la cohorte que vous souhaitez envoyer à Braze, puis cliquez sur **Export to Braze (Exporter vers Braze)**. Enfin, sélectionnez une synchronisation ponctuelle ou dynamique. La synchronisation dynamique synchronisera votre cohorte Braze toutes les 15 minutes pour qu’elle corresponde aux utilisateurs dans Mixpanel. 

![]({% image_buster /assets/img_archive/mixpanel3.png %}){: style="max-width:50%;"}

### Étape 4 : Segmenter des utilisateurs dans Braze

Dans Braze, pour créer un segment avec ces utilisateurs, accédez à **Segments** sous **Engagement**, nommez votre segment et sélectionnez **Mixpanel_Cohorts** en tant que filtre. Ensuite, utilisez l’option « includes » et choisissez la cohorte que vous avez créée dans Mixpanel. 

![Dans le générateur de segments de Braze, le filtre des attributs utilisateur « Cohortes Mixpanel » est défini sur « includes » et « cohorte de Braze ».]({% image_buster /assets/img_archive/mixpanel1.png %})

Une fois enregistré, vous pouvez référencer ce segment pendant la création d’un Canvas ou d’une campagne dans l’étape de ciblage des utilisateurs.

## Intégration de l’exportation de données

Vous trouverez ci-dessous une liste complète des événements qui peuvent être exportés de Braze vers Mixpanel. Tous les événements envoyés à Mixpanel incluront l’`external_user_id` de l’utilisateur comme ID distinct de Mixpanel. À l’heure actuelle, Braze n’envoie pas de données d’événements aux utilisateurs qui n’ont pas d’`external_user_id` défini.

Vous pouvez exporter deux types d’événements vers Mixpanel : Les [événements d’engagement par message](#message-engagement-events), qui incluent les Événements de Braze directement liés à l’envoi de messages, et les [événements de comportement client](#customer-behavior-events), qui incluent les activités d’autres applications ou sites Web, telles que des sessions, des événements personnalisés et des achats suivis sur la plateforme. Tous les événements personnalisés sont précédés par `[Braze Custom Event]`. Les propriétés de l’événement personnalisé et d’achat sont précédées par `[Custom event property]` et `[Purchase property]`, respectivement.

Contactez votre gestionnaire de compte ou ouvrez un [ticket de support][support] si vous avez besoin d’accéder à d’autres événements.

### Étape 1 : Obtenir les informations d’identification Mixpanel

Dans votre tableau de bord Mixpanel, cliquez sur **Project Settings (Paramètres du projet)** dans un nouveau projet nouveau ou dans un projet existant. Vous trouverez ici la clé secrète API Mixpanel et le jeton Mixpanel. Ces informations d’identification seront utilisées lors de la prochaine étape pour créer vos connexions Currents. 

### Étape 2 : Créer un current Braze

Dans Braze, accédez à **Currents > + Create Current (+ Créer un Current) > Create Mixpanel Export (Créer une exportation Mixpanel)**. Fournissez un nom d’intégration, une adresse e-mail de contact, une clé secrète API Mixpanel et un jeton Mixpanel dans les champs répertoriés. Ensuite, sélectionnez les événements que vous souhaitez suivre (consultez la liste des événements disponibles). Enfin, cliquez sur **‬Launch Current (Lancer le Current)**

![Page Braze Mixpanel Currents. Cette page comprend des champs pour le nom d’intégration, l’adresse e-mail de contact, la clé secrète API et le jeton d’exportation de Mixpanel. La moitié inférieure de la page Currents répertorie les événements Currents que vous pouvez envoyer.]({% image_buster /assets/img_archive/mixpanel4.png %}){: style="max-width:80%;"}

{% tab note %}
Consultez les [documents d’intégration](https://help.mixpanel.com/hc/en-us/articles/360001243663) de Mixpanel pour en savoir plus. 
{% endtab %}

## Événements Currents pris en charge

Braze prend en charge l’exportation des données suivantes vers Mixpanel, répertoriées dans les glossaires d’événements Currents sur le [comportement de l’utilisateur]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/customer_behavior_events/) et l’[engagement par message]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events/) :

### Comportements
- Événement personnalisé : `users.behaviors.CustomEvent`
- Attribution d’installation : `users.behaviors.InstallAttribution`
- Position : `users.behaviors.Location`
- Achat : `users.behaviors.Purchase`
- Désinstallation : `users.behaviors.Uninstall`
- Application (première session, impression de fil d’actualité, fin de session, début de session)
  - `users.behaviors.app.FirstSession`
  - `users.behaviors.app.NewsFeedImpression`
  - `users.behaviors.app.SessionEnd`
  - `users.behaviors.app.SessionStart`
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

[support]: {{site.baseurl}}/braze_support/
[1]: {% image_buster /assets/img_archive/mixpanel1.png %}
[2]: {% image_buster /assets/img_archive/mixpanel2.png %}
[3]: {% image_buster /assets/img_archive/mixpanel3.png %}
[4]: {% image_buster /assets/img_archive/mixpanel4.png %}
