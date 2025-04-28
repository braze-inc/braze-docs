---
nav_title: Amplitude pour Currents
article_title: Amplitude pour Currents
page_order: 0
description: "Cet article de référence présente le partenariat entre Braze Currents et Amplitude, une plateforme d'analyse de produits et d'aide à la décision."
page_type: partner
tool: Currents
search_tag: Partner

---

# [![Cours Braze]{% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/amplitude-integration-with-braze){: style="float:right;width:120px;border:0;" class="noimgborder"}Amplitude pour Currents

> [Amplitude](https://amplitude.com/) est une plateforme d'analyse de produits et d'aide à la décision.

L'intégration bidirectionnelle entre Braze et Amplitude vous permet de [synchroniser vos cohortes]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/amplitude/amplitude_audiences/), traits d'utilisateurs et événements Amplitude dans Braze, ainsi que d'exploiter Braze Currents pour [exporter vos événements Braze vers Amplitude](#data-export-integration) afin de réaliser des analyses plus approfondies de vos données produit et marketeur.

## Conditions préalables

| Condition | Description |
|---|---|
| Compte d'Amplitude | Un [compte Amplitude](https://amplitude.com/) est nécessaire pour bénéficier de ce partenariat. |
| Currents | Pour pouvoir exporter des données dans Amplitude, vous devez avoir configuré [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) pour votre compte. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" } 

## Intégration de l'exportation des données

Vous trouverez une liste complète des événements et propriétés d'événement pouvant être exportés de Braze vers Amplitude dans les sections suivantes. Tous les événements envoyés à Amplitude contiendront le paramètre `external_user_id` comme ID d'utilisateur Amplitude. Les propriétés d'événement propres à Braze seront envoyées sous la clé `event_properties` dans les données envoyées à Amplitude.

{% alert important %}
Pour utiliser cette fonctionnalité, votre utilisateur d'Amplitude doit correspondre à l'ID externe de Braze.
{% endalert %}

Braze n'enverra des données d'événement que pour les utilisateurs dont l'adresse `external_user_id` est définie ou pour les utilisateurs anonymes dont l'adresse `device_id` est définie. Pour les utilisateurs anonymes, vous devez synchroniser votre ID d'appareil Amplitude avec l'ID d'appareil Braze dans le SDK. Par exemple :

```java
amplitude.setDeviceId(Appboy.getInstance(context).getDeviceId();)
```

Vous pouvez exporter deux types d'événements vers Amplitude : [Événements d'engagement des messages](#supported-currents-events) constitués des événements Braze directement liés à l'envoi de messages, et [événements de comportement des clients](#supported-currents-events), y compris d'autres activités de l'application ou du site Web telles que les sessions, les événements personnalisés et les achats suivis via la plateforme. Tous les événements réguliers sont précédés du préfixe `[Appboy]`, et tous les événements personnalisés sont précédés du préfixe `[Appboy] [Custom Event]`. Les propriétés d'événements personnalisés et d'achats sont précédées des préfixes `[Custom event property]` et `[Purchase property]`, respectivement.

Toutes les cohortes nommées et importées dans Braze seront préfixées par `[Amplitude]` et suffixées par leur `cohort_id`. Ainsi, une cohorte nommée "TEST_COHORT" dont le paramètre `cohort_id` est défini sur "abcd1234" sera intitulée `[Amplitude] TEST_COHORT: abcd1234` dans les filtres Braze.

Contactez votre gestionnaire de compte ou ouvrez un [ticket d'assistance][support] si vous avez besoin d'accéder à des droits d'événements supplémentaires.

### Étape 1 : Configurer l'intégration de l'Amplitude dans Braze 

Dans Amplitude, recherchez votre clé API d'exportation Amplitude.

{% alert warning %}
Maintenez votre clé API Amplitude à jour. Si les informations d'identification de votre connecteur expirent, le connecteur cessera d'envoyer des événements. Si cette situation persiste pendant plus de **48 heures**, les événements du connecteur seront abandonnés et les données seront définitivement perdues.
{% endalert %}

### Étape 2 : Créer des flux Currents Braze

Dans Braze, naviguez vers **Currents > + Créer un flux Currents > Créer une exportation Amplitude**. Fournissez un nom d'intégration, un e-mail de contact, une clé API d'exportation Amplitude et une région Amplitude dans les champs répertoriés. Ensuite, sélectionnez les événements que vous souhaitez suivre ; une liste des événements disponibles est fournie. Enfin, cliquez sur **Lancer le flux Currents**

{% alert note %}
Les événements envoyés de Braze Currents vers Amplitude sont comptabilisés dans votre quota de volume d'événements Amplitude.
{% endalert %}

![La page Braze Amplitude Currents. Cette page contient des champs permettant de définir le nom de l'intégration, l'e-mail du contact, la clé API et la région des États-Unis. La moitié inférieure de la page Currents énumère les événements Currents disponibles que vous pouvez envoyer.]({% image_buster /assets/img/amplitude4.png %})

{% tab Remarque %}
Consultez la [documentation sur l’intégration](https://amplitude.zendesk.com/hc/en-us/articles/115000217351-Appboy-Amplitude-Integration#how-to-set-up-and-use-the-integration) d’Amplitude pour en savoir plus.
{% endtab %}

## Limites de débit

Currents se connecte à l'API HTTP d'Amplitude, qui a une [limite de débit](https://developers.amplitude.com/docs/http-api-v2#upload-limit) de 30 événements/seconde par appareil et une limite non documentée de 500 000 événements/jour par appareil. Si ces seuils sont dépassés, Amplitude limitera le nombre d'événements enregistrés via Currents. Si un appareil de votre intégration dépasse cette limite de débit, il se peut que les événements de tous les appareils apparaissent avec un certain retard dans Amplitude.

Les appareils ne devraient pas signaler plus de 30 événements par seconde ou 500 000 événements par jour dans des circonstances normales, et ce type d'événement ne devrait se produire qu'en raison d'une intégration mal configurée. Pour éviter ce type de retard, veillez à ce que votre intégration SDK signale les événements à un rythme normal, comme indiqué dans nos instructions d'intégration SDK, et évitez d'exécuter des tests automatisés qui génèrent de nombreux événements pour un seul appareil.

## Événements soutenus par Currents

Braze prend en charge l'exportation vers Amplitude des données suivantes répertoriées dans les glossaires des [comportements des utilisateurs]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/) et des [événements d’engagement lié aux messages]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) :

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
- E-mail (annulation, rebond, clic, distribution, markasspam, ouverture, envoi, softbounce, désinscription)
- Message in-app (abandon, clic, impression)
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
