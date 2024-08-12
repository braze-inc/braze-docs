---
nav_title: Amplitude pour Currents
article_title: Amplitude pour Currents
page_order: 0
description: "Cet article présente le partenariat entre currents Braze et Amplitude, une plateforme d’aide à la décision et d’analyse de produits."
page_type: partner
tool: Currents
search_tag: Partenaire

---

# [![Cours d’apprentissage Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/amplitude-integration-with-braze){: style="float:right;width:120px;border:0;" class="noimgborder"}Amplitude pour Currents

> [Amplitude](https://amplitude.com/) est une plateforme d’aide à la décision et d’analyse de produits.

L'intégration bidirectionnelle Braze et Amplitude vous permet de [synchroniser vos cohortes Amplitude]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/amplitude/amplitude_audiences/), vos caractéristiques utilisateur et vos événements dans Braze, ainsi que d'exploiter currents Braze pour [exporter vos événements Braze vers Amplitude](#data-export-integration) afin d'effectuer des analyses plus approfondies de vos données produit et marketing.

## Conditions préalables

| Condition | Description |
|---|---|
| Compte Amplitude | Un [compte Amplitude](https://amplitude.com/) est requis pour profiter de ce partenariat. |
| Currents | Pour réexporter des données dans Amplitude, vous devez avoir configuré [currents Braze]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) pour votre compte. |
{: .reset-td-br-1 .reset-td-br-2} 

## Intégration de l’exportation de données

Les sections suivantes présentent une liste complète des événements et des propriétés de l’événement pouvant être exportés de Braze vers Amplitude. Tous les événements envoyés à Amplitude incluront l’`external_user_id` de l’utilisateur en tant qu’ID utilisateur d’Amplitude. Les propriétés de l’événement spécifiques à Braze seront envoyées sous la clé `event_properties` dans les données envoyées à Amplitude.

Braze enverra uniquement des données d’événements pour les utilisateurs dont l’`external_user_id` est défini ou pour les utilisateurs anonymes dont l’`device_id` est défini. Pour les utilisateurs anonymes, vous devrez synchroniser votre ID d'appareil Amplitude avec l'ID d'appareil Braze dans le SDK. Par exemple :
```java
amplitude.setDeviceId(Apppboy.getInstance(context).getDeviceId();)
```

Vous pouvez exporter deux types d’événements vers Amplitude : Les [événements d’engagement par message](#message-engagement-events), qui incluent les Événements de Braze directement liés à l’envoi de messages, et les [événements de comportement client](#customer-berhavior-events), qui incluent les activités d’autres applications ou sites Web, telles que des sessions, des événements personnalisés et des achats suivis sur la plateforme. Tous les événements standard sont précédés par `[Appboy]`, et tous les événements personnalisés sont précédés par `[Appboy] [Custom Event]`. Les propriétés des événements personnalisés et d’achat sont précédées par `[Custom event property]` et `[Purchase property]`, respectivement.

Toutes les cohortes nommées et importées dans Braze seront précédées par `[Amplitude]` et suivies de leur `cohort_id`. Cela signifie qu’une cohorte nommée « TEST_COHORT » avec le `cohort_id` « abcd1234 » sera intitulée `[Amplitude] TEST_COHORT: abcd1234` dans les filtres Braze.

Contactez votre gestionnaire de compte ou ouvrez un [ticket de support][support] si vous avez besoin d’accéder à d’autres événements.

### Étape 1 : Configurer l’intégration Amplitude dans Braze 

Dans Amplitude, recherchez votre clé API d’exportation Amplitude.

{% alert warning %}
Assurez-vous de maintenir votre clé API Amplitude à jour. Le connecteur arrêtera d’envoyer des événements si les informations d’identification de votre connecteur expirent. Si cela persiste plus de **48 heures**, les événements du connecteur seront supprimés et les données seront perdues définitivement.
{% endalert %}

### Étape 2 : Créer un current Braze

Dans Braze, accédez à **Currents > + Create Current (+ Créer un Current) > Create Amplitude Export (Créer une exportation Amplitude)**. Indiquez le nom de l’intégration, une adresse e-mail de contact, la clé API d’exportation Amplitude et une région pour Amplitude dans les champs répertoriés. Ensuite, sélectionnez les événements que vous souhaitez suivre (consultez la liste des événements disponibles). Enfin, cliquez sur **‬Launch Current (Lancer le Current)**

{% alert note %}
Les événements envoyés de currents Braze à Amplitude seront pris en compte dans votre quota de volume d'événements Amplitude.
{% endalert %}

![La page Braze Amplitude Currents. Cette page comprend des champs pour le nom d’intégration, l’adresse e-mail de contact, la clé API et la région US. La moitié inférieure de la page Currents répertorie les événements Currents que vous pouvez envoyer.]({% image_buster /assets/img/amplitude4.png %})

{% tab note %}
Consultez les [documents d’intégration](https://amplitude.zendesk.com/hc/en-us/articles/115000217351-Appboy-Amplitude-Integration#how-to-set-up-and-use-the-integration) d’Amplitude pour en savoir plus. 
{% endtab %}

## Limites de débit

Les Currents se connectent à l’API HTTP d’Amplitude, qui comporte une [Limitation du débit](https://developers.amplitude.com/docs/http-api-v2#upload-limit) de 30 événements/seconde par appareil et une limite non documentée de 500 000 événements/jour par appareil. Si ces seuils sont dépassés, Amplitude limitera les événements enregistrés dans des Currents. Si un appareil au sein de votre intégration dépasse cette limite de débit, il se peut que les appareils apparaissent dans Amplitude avec un certain retard.

Dans des circonstances normales, les appareils ne doivent pas rapporter plus de 30 événements/seconde ou 500 000 événements/jour, et cette fréquence d’événement ne devrait se produire qu’en cas d’intégration mal configurée. Pour éviter ce type de retard, assurez-vous que votre intégration SDK rapporte des événements à une fréquence normale, tel que spécifié dans nos instructions d’intégration SDK. D’autre part, faites attention à ne pas exécuter de tests automatisés qui génèrent de nombreux événements pour un seul appareil.

## Événements Currents pris en charge

Braze prend en charge l’exportation des données suivantes vers Amplitude, répertoriées dans les glossaires d’événements Currents sur le [comportement de l’utilisateur]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/customer_behavior_events/) et l’[engagement par message]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events/) :

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
