---
nav_title: Événements d’engagement sur les messages
layout: message_engagement_events_glossary
page_order: 5
excerpt_separator: ""
page_type: glossary
description: "Ce glossaire répertorie les différents comportements client et événements utilisateur que Braze peut suivre et envoyer via Currents à des entrepôts de données désignés."
tool: Currents
search_rank: 6
---

Contactez votre gestionnaire de compte ou ouvrez un [ticket de support]({{site.baseurl}}/braze_support/) si vous avez besoin d’accéder à d’autres événements. Si vous ne trouvez pas ce dont vous avez besoin dans cet article, consultez notre [Bibliothèque des événements de comportement client]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/customer_behavior_events/) ou nos [Exemples d’échantillons de données Currents](https://github.com/Appboy/currents-examples/tree/master/sample-data).

{% details Explication de la structure d’événement d’engagement par message et des valeurs de la plateforme %}

### Structure d’événement

Cette ventilation des événements montre le type d’information généralement inclus dans un événement d’engagement de message. Avec une bonne compréhension de ses composants, vos développeurs et votre équipe BI peuvent utiliser les données d’événements Currents entrants pour créer des rapports et des graphiques axés sur les données, et tirer parti des précieux indicateurs de données fournis.

![Ventilation d’un événement d’engagement de messages montrant un événement de désabonnement par e-mail avec les propriétés répertoriées groupées par propriétés spécifiques à l’utilisateur, par campagne ou par Canvas, et propriétés spécifiques à l’événement]({% image_buster /assets/img/message_engagement_event.png %})

Les événements d’engagement sur les messages sont composés de propriétés **spécifiques à l’utilisateur**, de propriétés de **suivi de campagne/canvas** et de propriétés **spécifiques à l’événement**.

### Valeurs de la plateforme

Certains événements renvoient une valeur `platform` qui spécifie la plate-forme de l’appareil de l’utilisateur. 
<br>Le tableau suivant détaille les valeurs retournées possibles :

| Appareil de l’utilisateur | Valeur de la plateforme |
| --- | --- |
| iOS | `ios` |
| Android | `android` |
| FireTV | `kindle` |
| Kindle | `kindle` |
| Web | `web` |
| tvOS | `tvos` |
| Roku | `roku` |
{: .reset-td-br-1 .reset-td-br-2}

{% enddetails %}

{% alert important %}
Ces schémas ne s’appliquent qu’aux données d’événements de fichiers plats que nous envoyons aux partenaires d’entrepôt de données (Google Cloud Storage, Amazon S3 et Microsoft Azure Blob Storage). Pour les schémas qui s’appliquent aux autres partenaires, consultez notre liste de [partenaires disponibles]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/available_partners/) et allez sur leurs pages respectives.<br><br>De plus, notez que Currents ignorera les événements avec des charges utiles excessivement importantes de plus de 900 Ko.
{% endalert %}

{% api %}

## Événements de message d’abandon de carte de contenu

{% apitags %}
Abandon, Cartes de contenu
{% endapitags %}

Cet événement se produit si un message Carte de contenu a été abandonné en raison d’heures calmes, de la limitation de débit, d’une limite de fréquence ou d’abandons Liquid.

```json
// Content Card Abort :users_messages_contentcard_abort

{
  "id": (string) globally unique ID of this event,
  "user_id": (string) BSON id of the user that performed this event, 
  "external_user_id": (string) External user ID of the user,
  "app_group_id": (string) BSON id of the app group this user belongs to,
  "app_group_api_id": (string) API ID of the app group this user belongs to,
  "time": (int) unix timestamp at which the event happened,
  "gender": (sting) gender of the user,
  "device_id": (string) id of the device on which the event occurred,
  "abort_type": (string) type of abort, one of: "liquid_abort_message", "quiet_hours", "rate_limit",
  "abort_log": (string) log message describing abort details (MAX: 128 CHARS),
  "dispatch_id" (string) ID of the dispatch this message belongs to,
  "send_id": (string) message send ID this message belongs to,
  "campaign_id": (string) internal-use Braze ID of the campaign this event belongs to,
  "campaign_api_id": (string) API ID of the campaign this event belongs to,
  "message_variation_api_id": (string) API ID of the message variation this user received,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_api_id": (string) BSON id of the experiment step this event belongs to,
  "canvas_variation_api_id": (string) API id of the canvas variation this event belongs to,
  "canvas_step_api_id": (string) API id of the canvas step this event belongs to,
  "canvas_step_message_variation_api_id": (string) API id of the canvas step message variation this user received,
  "content_card_id": (string) id of the card that generated this event
}
```
{% endapi %}

{% api %}

## Événements de message d’abandon d’e-mail

{% apitags %}
Abandon, e-mail
{% endapitags %}

Cet événement se produit si un message e-mail a été abandonné en raison d’heures calmes, de la limitation de débit, d’une limite de fréquence ou d’abandons Liquid.

```json
// Email Abort :users_messages_email_abort

{
  "id": (string) globally unique ID of this event,
  "user_id": (string) BSON id of the user that performed this event, 
  "external_user_id": (string) External user ID of the user,
  "app_group_id": (string) BSON id of the app group this user belongs to,
  "app_group_api_id": (string) API ID of the app group this user belongs to,
  "time": (int) unix timestamp at which the event happened,
  "gender": (sting) gender of the user,
  "device_id": (string) id of the device on which the event occurred,
  "abort_type": (string) type of abort, one of: "liquid_abort_message", "quiet_hours", "rate_limit",
  "abort_log": (string) log message describing abort details (MAX: 128 CHARS),
  "dispatch_id" (string) ID of the dispatch this message belongs to,
  "send_id": (string) message send ID this message belongs to,
  "campaign_id": (string) internal-use Braze ID of the campaign this event belongs to,
  "campaign_api_id": (string) API ID of the campaign this event belongs to,
  "message_variation_api_id": (string) API ID of the message variation this user received,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_api_id": (string) BSON id of the experiment step this event belongs to,
  "canvas_variation_api_id": (string) API id of the canvas variation this event belongs to,
  "canvas_step_api_id": (string) API id of the canvas step this event belongs to,
  "canvas_step_message_variation_api_id": (string) API id of the canvas step message variation this user received,
  "email_address" (string) email address of the user,
  "ip_pool": (string) IP Pool from which the email send was made
}
```
{% endapi %}

{% api %}

## Événements d’abandon de messages in-app

{% apitags %}
Abandon, messages In-App
{% endapitags %}

Cet événement se produit si un message in-app a été abandonné en raison d’heures calmes, de la limitation de débit, d’une limite de fréquence ou d’abandons Liquid.

```json
// In-App Message Abort :users_messages_inappmessage_abort

{
  "id": (string) globally unique ID of this event,
  "user_id": (string) BSON id of the user that performed this event, 
  "external_user_id": (string) External user ID of the user,
  "app_group_id": (string) BSON id of the app group this user belongs to,
  "app_group_api_id": (string) API ID of the app group this user belongs to,
  "time": (int) unix timestamp at which the event happened,
  "app_api_id": (string) API ID of the app on which this event occurred,
  "card_id": (string) BSON id of the card this in app message comes from,
  "card_api_id": (string) API ID of the card,
  "gender": (sting) gender of the user,
  "device_id": (string) id of the device on which the event occurred,
  "sdk_version": (string) version of the Braze SDK in use during the event,
  "platform": (string) platform of the device,
  "os_version": (string) version of the operating system of the device,
  "device_model" (string) model of the device,
  "resolution": (string) resolution of the device,
  "carrier:" (string) carrier of the device,
  "browser": (string) browser of the device,
  "abort_type": (string) type of abort, one of: "liquid_abort_message", "quiet_hours", "rate_limit",
  "abort_log": (string) log message describing abort details (MAX: 128 CHARS),
  "dispatch_id" (string) ID of the dispatch this message belongs to,
  "send_id": (string) message send ID this message belongs to,
  "campaign_id": (string) internal-use Braze ID of the campaign this event belongs to,
  "campaign_api_id": (string) API ID of the campaign this event belongs to,
  "message_variation_api_id": (string) API ID of the message variation this user received,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_api_id": (string) BSON id of the experiment step this event belongs to,
  "canvas_variation_api_id": (string) API id of the canvas variation this event belongs to,
  "canvas_step_api_id": (string) API id of the canvas step this event belongs to,
  "canvas_step_message_variation_api_id": (string) API id of the canvas step message variation this user received,
  "version": (string) which version of in app message, legacy or triggered,
  "ad_id": (string) advertising identifier,
  "ad_id_type": (string) one of 'ios_idfa', 'google_ad_id', OR 'roku_ad_id',
  "ad_tracking_enabled": (string) Whether advertising tracking is enabled for the device
}
```
{% endapi %}

{% api %}

## Événements d’abandon de carte de fil d’actualité

{% apitags %}
Abandon, fil d’actualité
{% endapitags %}

Cet événement se produit si un message de Carte de fil d’actualité a été abandonné en raison d’heures calmes, de la limitation de débit, d’une limite de fréquence ou d’abandons Liquid.

```json
// News Feed Card Abort :users_messages_newsfeedcard_abort

{
  "id": (string) globally unique ID of this event,
  "user_id": (string) BSON id of the user that performed this event, 
  "external_user_id": (string) External user ID of the user,
  "app_group_id": (string) BSON id of the app group this user belongs to,
  "app_group_api_id": (string) API ID of the app group this user belongs to,
  "time": (int) unix timestamp at which the event happened,
  "app_api_id": (string) API ID of the app on which this event occurred,
  "card_id": (string) BSON id of the card this in app message comes from,
  "card_api_id": (string) API ID of the card,
  "gender": (sting) gender of the user,
  "device_id": (string) id of the device on which the event occurred,
  "sdk_version": (string) version of the Braze SDK in use during the event,
  "platform": (string) platform of the device,
  "os_version": (string) version of the operating system of the device,
  "device_model" (string) model of the device,
  "resolution": (string) resolution of the device,
  "carrier:" (string) carrier of the device,
  "browser": (string) browser of the device,
  "abort_type": (string) type of abort, one of: "liquid_abort_message", "quiet_hours", "rate_limit",
  "abort_log": (string) log message describing abort details (MAX: 128 CHARS),

}
```
{% endapi %}

{% api %}

## Événements d’abandon de notification push

{% apitags %}
Abandon, notifications push
{% endapitags %}

Cet événement se produit si un message de notification push a été abandonné en raison d’heures calmes, de la limitation de débit, d’une limite de fréquence ou d’abandons Liquid.

```json
// Push Notification Abort :users_messages_pushnotification_abort

{
  "id": (string) globally unique ID of this event,
  "user_id": (string) BSON id of the user that performed this event, 
  "external_user_id": (string) External user ID of the user,
  "app_group_id": (string) BSON id of the app group this user belongs to,
  "app_group_api_id": (string) API ID of the app group this user belongs to,
  "time": (int) unix timestamp at which the event happened,
  "app_api_id": (string) API ID of the app on which this event occurred,
  "gender": (sting) gender of the user,
  "device_id": (string) id of the device on which the event occurred,
  "platform": (string) platform of the device,
  "abort_type": (string) type of abort, one of: "liquid_abort_message", "quiet_hours", "rate_limit",
  "abort_log": (string) log message describing abort details (MAX: 128 CHARS),
  "dispatch_id" (string) ID of the dispatch this message belongs to,
  "send_id": (string) message send ID this message belongs to,
  "campaign_id": (string) internal-use Braze ID of the campaign this event belongs to,
  "campaign_api_id": (string) API ID of the campaign this event belongs to,
  "message_variation_api_id": (string) API ID of the message variation this user received,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_api_id": (string) BSON id of the experiment step this event belongs to,
  "canvas_variation_api_id": (string) API id of the canvas variation this event belongs to,
  "canvas_step_api_id": (string) API id of the canvas step this event belongs to,
  "canvas_step_message_variation_api_id": (string) API id of the canvas step message variation this user received
}
```
{% endapi %}

{% api %}

## Événements d’abandon de message SMS

{% apitags %}
Abandon, SMS
{% endapitags %}

Cet événement se produit si un message SMS a été abandonné en raison d’heures calmes, de la limitation de débit, d’une limite de fréquence ou d’abandons Liquid.

```json
// SMS Abort :users_messages_sms_abort

{
  "id": (string) globally unique ID of this event,
  "user_id": (string) BSON id of the user that performed this event, 
  "external_user_id": (string) External user ID of the user,
  "app_group_id": (string) BSON id of the app group this user belongs to,
  "app_group_api_id": (string) API ID of the app group this user belongs to,
  "time": (int) unix timestamp at which the event happened,
  "abort_type": (string) type of abort, one of: "liquid_abort_message", "quiet_hours", "rate_limit",
  "abort_log": (string) log message describing abort details (MAX: 128 CHARS),
  "campaign_id": (string) internal-use Braze ID of the campaign this event belongs to,
  "campaign_api_id": (string) API ID of the campaign this event belongs to,
  "message_variation_api_id": (string) API ID of the message variation this user received,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_api_id": (string) BSON id of the experiment step this event belongs to,
  "canvas_variation_api_id": (string) API id of the canvas variation this event belongs to,
  "canvas_step_api_id": (string) API id of the canvas step this event belongs to,
  "canvas_step_message_variation_api_id": (string) API id of the canvas step message variation this user received,
  "subscription_group_api_id": (string) external ID of the subscription group
}
```
{% endapi %}

{% api %}

## Événements d’abandon de message Webhook

{% apitags %}
Abandon, Webhooks
{% endapitags %}

Cet événement se produit si un message Webhook a été abandonné en raison d’heures calmes, de la limitation de débit, d’une limite de fréquence ou d’abandons Liquid.

```json
// Webhook Abort :users_messages_webhook_abort

{
  "id": (string) globally unique ID of this event,
  "user_id": (string) BSON id of the user that performed this event, 
  "external_user_id": (string) External user ID of the user,
  "app_group_id": (string) BSON id of the app group this user belongs to,
  "app_group_api_id": (string) API ID of the app group this user belongs to,
  "time": (int) unix timestamp at which the event happened,
  "gender": (sting) gender of the user,
  "country": (string) country of the user,
  "timezone": (string) timezone of the user,
  "language": (string) language of the user,
  "device_id": (string) id of the device on which the event occurred,
  "abort_type": (string) type of abort, one of: "liquid_abort_message", "quiet_hours", "rate_limit",
  "abort_log": (string) log message describing abort details (MAX: 128 CHARS),
  "dispatch_id" (string) ID of the dispatch this message belongs to,
  "send_id": (string) message send ID this message belongs to,
  "campaign_id": (string) internal-use Braze ID of the campaign this event belongs to,
  "campaign_api_id": (string) API ID of the campaign this event belongs to,
  "message_variation_api_id": (string) API ID of the message variation this user received,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_api_id": (string) BSON id of the experiment step this event belongs to,
  "canvas_variation_api_id": (string) API id of the canvas variation this event belongs to,
  "canvas_step_api_id": (string) API id of the canvas step this event belongs to,
  "canvas_step_message_variation_api_id": (string) API id of the canvas step message variation this user received,
}
```
{% endapi %}


{% api %}

## Événements de sortie du Canvas ayant effectué un événement

{% apitags %}
Sortie, Canvas
{% endapitags %}

Cet événement ce produit lorsqu’un utilisateur quitte un Canvas en effectuant un événement.

```json
// Canvas Exit Performed Event: users.canvas.exit.PerformedEvent

{
  "id": (string) globally unique ID of this event,
  "user_id": (string) Braze user id of the user, 
  "external_user_id": (string) External user ID of the user,
  "app_group_id": (string) BSON id of the app group this user belongs to,
  "app_group_api_id": (string) API ID of the app group this user belongs to,
  "time": (int) unix timestamp at which the event happened,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_api_id": (string) BSON id of the experiment step this event belongs to,
  "canvas_variation_api_id": (string) API id of the canvas variation this event belongs to,
  "canvas_step_api_id": (string) API id of the canvas step this event belongs to,
}
```
{% endapi %}

{% api %}

## Événements de sortie du Canvas par correspondance à une audience

{% apitags %}
Sortie, Canvas
{% endapitags %}

Cet événement ce produit lorsqu’un utilisateur quitte un Canvas en correspondant à une audience.

```json
// Canvas Exit Matched Audience: users_canvas_exit_MatchedAudience

{
  "id": (string) globally unique ID of this event,
  "user_id": (string) Braze user id of the user, 
  "external_user_id": (string) External user ID of the user,
  "app_group_id": (string) BSON id of the app group this user belongs to,
  "app_group_api_id": (string) API ID of the app group this user belongs to,
  "time": (int) unix timestamp at which the event happened,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_api_id": (string) BSON id of the experiment step this event belongs to,
  "canvas_variation_api_id": (string) API id of the canvas variation this event belongs to,
  "canvas_step_api_id": (string) API id of the canvas step this event belongs to,
}
```
{% endapi %}
{% api %}
## Événements d’entrée fractionnée Experiment

{% apitags %}
Étape Experiment, Canvas
{% endapitags %}

Cet événement se produit quand un utilisateur entre dans une étape Canvas Experiment.

```json
// Experiment Step Split Path Entry: users.canvas.experimentstep.SplitEntry

{
  "id": (string) globally unique ID of this event,
  "user_id": (string) Braze user id of the user, 
  "external_user_id": (string) External user ID of the user,
  "time": (int) unix timestamp at which the event happened,
  "canvas_api_id": (string) BSON id of the experiment step this event belongs to,
  "canvas_variation_api_id": (string) API id of the Canvas variation this event belongs to,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "experiment_step_api_id" (string) API id of the experiment step this event belongs to,
  "experiment_step_id": (string) BSON ID of the experiment step this event belongs to,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "canvas_step_api_id" (string) API id of the step if from a Canvas,   
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  "experiment_split_id": (string) BSON ID of the experiment split the user enrolled in,
  "experiment_split_api_id" (string) API id of the experiment split the user was enrolled in,
  "experiment_split_name": (string) name of the experiment split the user enrolled in,
  "in_control_group": (boolean) whether the user was enrolled in the control group
}
```
{% endapi %}

{% api %}

## Événements de conversion Experiment

{% apitags %}
Étape Experiment, Canvas
{% endapitags %}

Cet événement se produit lorsqu’un utilisateur effectue une conversion pour une étape Canvas Experiment.

```json
// Experiment Step Conversion: users.canvas.experimentstep.Conversion

{
  "id": (string) globally unique ID of this event,
  "user_id": (string) Braze user id of the user, 
  "external_user_id": (string) External user ID of the user,
  "app_id": (string) BSON id of the app this user belongs to,
  "time": (int) unix timestamp at which the event happened,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  "experiment_step_id": (string) BSON ID of the experiment step this event belongs to,
  "experiment_split_id": (string) BSON ID of the experiment split variation this user received,
  "experiment_split_name": (string) name of the experiment split the user enrolled in,
  "conversion_behavior_index": (int) index of the conversion behavior,
  "conversion_behavior": (string): conversion behavior
}
```
{% endapi %}
{% api %}

## Événements d’envoi de notification push

{% apitags %}
Notification push, envois
{% endapitags %}

Cet événement survient lorsque Braze traite un message de notification push pour un utilisateur, en le communiquant au service de notification push d’Apple ou Fire Cloud Messaging. Cela ne signifie pas que la notification push a été livrée sur l’appareil, cela indique juste qu’un message a été envoyé.

```json
// Push Notification Send: users.messages.pushnotification.Send
{
  "id": (string) unique id of this event,
  "user_id": (string) Braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (string) IANA time zone of the user at the time of the event,
  "app_id": (string) id for the app on which the user action occurred,
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "message_variation_name": (string) the name of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  "platform": (string) platform of the device (one of 'ios', 'android', 'web', 'kindle', 'tvos', OR 'roku'),
  "device_id": (string) id of the device that we made a delivery attempt to,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "dispatch_id": (string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform). Users who are sent a schedule message get the same dispatch_id. Action-based or API-triggered messages get a unique dispatch_id per user.,
  "ad_id": (string) advertising identifier,
  "ad_id_type": (string) One of 'ios_idfa', 'google_ad_id', OR 'roku_ad_id',
  "ad_tracking_enabled": (boolean) whether advertising tracking is enabled for the device
}
```
#### Détails de la propriété
- Pour `ad_id`, `ad_id_type` et `ad_tracking_enabled`, vous devrez collecter explicitement les IDFA iOS et les ADID Android Google via les SDK natifs. Pour en savoir plus cliquez ici : [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/optional_idfa_collection/#optional-idfa-collection/), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id).
- Si vous utilisez Kafka pour ingérer des données [Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/), contactez votre gestionnaire du succès des clients ou votre gestionnaire de compte pour activer la bascule de fonctionnalité pour envoyer un `ad_id`.
{% endapi %}
{% api %}

## Événements d’ouvertures de notification push

{% apitags %}
Notification push, Ouvertures
{% endapitags %}

Cet événement se produit lorsqu’un utilisateur clique directement sur la notification push pour ouvrir l’application. Actuellement, les événements d’ouverture de notification push se rapportent spécifiquement aux « Ouvertures directes » plutôt qu’au « total des ouvertures». Cela n’inclut pas les statistiques affichées au niveau des « ouvertures influencées » de la campagne, car elles ne sont pas attribuées au niveau de l’utilisateur.

```json
// Push Notification Open: users.messages.pushnotification.Open
{
  "id": (string) unique id of this event,
  "user_id": (string) Braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (string) IANA time zone of the user at the time of the event,
  "app_id": (string) id for the app on which the user action occurred,
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "message_variation_name": (string) the name of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  "canvas_step_message_variation_id": (string) API id of the Canvas step message variation this user received,
  "platform": (string) platform of the device (one of 'ios', 'android', 'web', 'kindle', 'tvos', OR 'roku'),
  "os_version": (string) os version of device used for the action,
  "device_model": (string) hardware model of the device,
  "device_id": (string) id of the device that we made a delivery attempt to,
  "button_action_type": (string) Action type of the push notification,
  button. One of [URI, DEEP_LINK, NONE, CLOSE, SHARE]. null if not
  from a button click,
  "button_string": (string) identifier (button_string) of the push notification button clicked. null if not from a button click,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "dispatch_id": (string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform). Users who are sent a schedule message get the same dispatch_id. Action-based or API-triggered messages get a unique dispatch_id per user.,
  "ad_id": (string) advertising identifier,
  "ad_id_type": (string) One of 'ios_idfa', 'google_ad_id', OR 'roku_ad_id',
  "ad_tracking_enabled": (boolean) whether advertising tracking is enabled for the device
}
```
#### Détails de la propriété
- Pour `ad_id`, `ad_id_type` et `ad_tracking_enabled`, vous devrez collecter explicitement les IDFA iOS et les ADID Android Google via les SDK natifs. Pour en savoir plus cliquez ici : [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/optional_idfa_collection/#optional-idfa-collection/), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id).
- Si vous utilisez Kafka pour ingérer des données [Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/), contactez votre gestionnaire du succès des clients ou votre gestionnaire de compte pour activer la bascule de fonctionnalité pour envoyer un `ad_id`.
{% endapi %}
{% api %}

## Notifications push dans les événements de foreground (premier plan) iOS

{% apitags %}
Notification push, iOS, Envois
{% endapitags %}

Veuillez noter que cet événement n’est pas supporté par notre [SDK Swift](https://github.com/braze-inc/braze-swift-sdk).

Cet événement est maintenant déprécié sur notre [SDK Obj-C](https://github.com/Appboy/appboy-ios-sdk).

```json
// Push Notification iOS Foreground: users.messages.pushnotification.IosForeground
{
  "id": (string) unique id of this event,
  "user_id": (string) Braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (string) IANA time zone of the user at the time of the event,
  "app_id": (string) id for the app on which the user action occurred,
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "message_variation_name": (string) the name of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  "platform": (string) platform of the device (one of 'ios', 'android', 'web', 'kindle', 'tvos', OR 'roku'),
  "device_id": (string) id of the device that we made a delivery attempt to,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "dispatch_id": (string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform). Users who are sent a schedule message get the same dispatch_id. Action-based or API-triggered messages get a unique dispatch_id per user.,
  "ad_id": (string) advertising identifier,
  "ad_id_type": (string) One of 'ios_idfa', 'google_ad_id', OR 'roku_ad_id',
  "ad_tracking_enabled": (boolean) whether advertising tracking is enabled for the device
}
```
#### Détails de la propriété
- Pour `ad_id`, `ad_id_type` et `ad_tracking_enabled`, vous devrez collecter explicitement les IDFA iOS et les ADID Android Google via les SDK natifs. Pour en savoir plus cliquez ici : [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/optional_idfa_collection/#optional-idfa-collection/), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id).
- Si vous utilisez Kafka pour ingérer des données [Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/), contactez votre gestionnaire du succès des clients ou votre gestionnaire de compte pour activer la bascule de fonctionnalité pour envoyer un `ad_id`.
{% endapi %}
{% api %}

## Rebond (bounce) de notifications Push

{% apitags %}
Notification push, Envois, Rebonds
{% endapitags %}

Cet événement survient lorsqu’une erreur est reçue du service de notification Push d’Apple ou de Fire Cloud Messaging. Cela signifie que le message de notification push a « rebondi » et n’est donc pas arrivé sur l’appareil de l’utilisateur.

```json
// Push Notification Bounce: users.messages.pushnotification.Bounce
{
  "id": (string) unique id of this event,
  "user_id": (string) Braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (string) IANA time zone of the user at the time of the event,
  "app_id": (string) id for the app on which the bounce occurred,
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "message_variation_name": (string) the name of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  "platform": (string) platform of the device (one of 'ios', 'android', 'web', 'kindle', 'tvos', OR 'roku'),
  "device_id": (string) id of the device that we made a delivery attempt to,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "dispatch_id": (string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform). Users who are sent a schedule message get the same dispatch_id. Action-based or API-triggered messages get a unique dispatch_id per user.,
  "ad_id": (string) advertising identifier,
  "ad_id_type": (string) One of 'ios_idfa', 'google_ad_id', OR 'roku_ad_id',
  "ad_tracking_enabled": (boolean) whether advertising tracking is enabled for the device
}
```
#### Détails de la propriété
- Si vous utilisez Kafka pour ingérer des données [Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/), contactez votre gestionnaire du succès des clients ou votre gestionnaire de compte pour activer la bascule de fonctionnalité pour envoyer un `ad_id`.
{% endapi %}
{% api %}

## Événements d’envoi d’e-mail

{% apitags %}
E-mail, envoi
{% endapitags %}

Cet événement se produit lorsqu’une demande d’envoi d’e-mail a été transmise avec succès entre Braze et SendGrid. Mais cela ne signifie pas que l’e-mail est arrivé dans la boîte de réception de l’utilisateur final.

```json
// Email Send: users.messages.email.Send
{
  // User Specific Properties
  "id": (string) unique id of this event,
  "user_id": (string) Braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (string) IANA time zone of the user at the time of the event,
  // Campaign/Canvas Tracking Properties
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "message_variation_name": (string) the name of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  // Event Specific Properties
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "dispatch_id": (string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform). Users who are sent a schedule message get the same dispatch_id. Action-based or API-triggered messages get a unique dispatch_id per user,
  "email_address": (string) email address for this event,
  "ip_pool": (string) IP pool used for message sending
}
```
#### Détails de la propriété
- Le comportement pour `dispatch_id` diffère entre Canvas et les campagnes, car Braze traite les étapes Canvas (à l’exception des étapes d’entrée, qui peuvent être programmées) comme des événements déclenchés, même lorsqu’ils sont « programmés ». En savoir plus sur [comportement de dispatch ID]({{site.baseurl}}/help/help_articles/data/dispatch_id/).
{% endapi %}


{% api %}

## Événements de livraison d’e-mail

{% apitags %}
E-mail, livraison
{% endapitags %}

Cet événement se produit lorsqu’un e-mail envoyé est arrivé dans la boîte de réception des utilisateurs finaux.

```json
// Email Delivery: users.messages.email.Delivery
{
  "id": (string) unique id of this event,
  "user_id": (string) Braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (string) IANA time zone of the user at the time of the event,
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "message_variation_name": (string) the name of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "dispatch_id": (string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform). Users who are sent a schedule message get the same dispatch_id. Action-based or API-triggered messages get a unique dispatch_id per user.,
  "email_address": (string) email address for this event,
  "sending_ip": (string) the IP address from which the message was sent (Email Delivery, Bounce, and SoftBounce events only. Will only be shown on events if the message was actually attempted for delivery. For certain other bounces, the information could be lost if the recipient server has already accepted the mail and only later after the connection is closed decided it could not deliver the mail),
  "ip_pool": (string) IP pool used for message sending,
  "esp": (string) ESP related to the event (SparkPost or SendGrid),
  "from_domain": (string) sending domain for the email
}
```
#### Détails de la propriété
- Le comportement pour `dispatch_id` diffère entre Canvas et les campagnes, car Braze traite les étapes Canvas (à l’exception des étapes d’entrée, qui peuvent être programmées) comme des événements déclenchés, même lorsqu’ils sont « programmés ». En savoir plus sur [comportement de dispatch ID]({{site.baseurl}}/help/help_articles/data/dispatch_id/).
{% endapi %}


{% api %}

## Événements d’ouverture d’e-mail

{% apitags %}
E-mail, ouverture
{% endapitags %}

Cet événement se produit lorsqu’un utilisateur ouvre un e-mail. Plusieurs événements peuvent être générés pour une même campagne si un utilisateur ouvre l’e-mail plusieurs fois.

```json
// Email Open: users.messages.email.Open
{
  "id": (string) unique id of this event,
  "user_id": (string) Braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (string) IANA time zone of the user at the time of the event,
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "message_variation_name": (string) the name of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "dispatch_id": (string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform). Users who are sent a schedule message get the same dispatch_id. Action-based or API-triggered messages get a unique dispatch_id per user.,
  "email_address": (string) email address for this event,
  "ip_pool": (string) IP pool used for message sending,
  "user_agent": (string) description of the user's system and browser for the event,
  "machine_open": (string) Indicator of whether the e-mail was opened by an automated process, such as Apple or Google mail pre-fetching. Currently "true" or null, but additional granularity (e.g., "Apple" or "Google" to indicate which process made the fetch) may be added in the future.,
  "esp": (string) ESP related to the event (SparkPost or SendGrid),
  "from_domain": (string) sending domain for the email,
  "is_amp": (boolean) indicates that this is an AMP event
}
```
#### Détails de la propriété
- Le comportement pour `dispatch_id` diffère entre Canvas et les campagnes, car Braze traite les étapes Canvas (à l’exception des étapes d’entrée, qui peuvent être programmées) comme des événements déclenchés, même lorsqu’ils sont « programmés ». En savoir plus sur [comportement de dispatch ID]({{site.baseurl}}/help/help_articles/data/dispatch_id/).
{% endapi %}



{% api %}

## Événements de clic sur un e-mail

{% apitags %}
E-mail, clics
{% endapitags %}

Cet événement se produit lorsqu’un utilisateur clique sur un e-mail. Plusieurs événements peuvent être générés pour une même campagne si un utilisateur clique plusieurs fois sur un lien ou clique sur plusieurs liens dans l’e-mail.

```json
// Email Click: users.messages.email.Click
{
  "id": (string) unique id of this event,
  "user_id": (string) Braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (string) IANA time zone of the user at the time of the event,
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "message_variation_name": (string) the name of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "dispatch_id": (string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform). Only included when campaign_id is present. Users who are sent a schedule message get the same dispatch_id. Action-based or API-triggered messages get a unique dispatch_id per user.,
  "email_address": (string) email address for this event,
  "url": (string) the URL that was clicked,
  "ip_pool": (string) IP pool used for message sending,
  "user_agent": (string) description of the user's system and browser for the event,
  "link_id": (string) unique value generated by Braze for the URL - null unless link aliasing is enabled,
  "link_alias": (string) alias name set when the message was sent - null unless link aliasing is enabled,
  "esp": (string) ESP related to the event (SparkPost or SendGrid),
  "from_domain": (string) sending domain for the email,
  "is_amp": (boolean) indicates that this is an AMP event
}
```
#### Détails de la propriété
- Le comportement pour `dispatch_id` diffère entre Canvas et les campagnes, car Braze traite les étapes Canvas (à l’exception des étapes d’entrée, qui peuvent être programmées) comme des événements déclenchés, même lorsqu’ils sont « programmés ». En savoir plus sur [comportement de dispatch ID]({{site.baseurl}}/help/help_articles/data/dispatch_id/).
{% endapi %}

{% api %}

## Événement de rebond d’e-mail

{% apitags %}
E-mail, bounce
{% endapitags %}

Cet événement survient lorsqu’un fournisseur de services Internet renvoie un hard bounce. Un hard bounce signifie un échec permanent de la délivrabilité.

```json
// Email Bounce: users.messages.email.Bounce
{
  "id": (string) unique id of this event,
  "user_id": (string) Braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (string) IANA time zone of the user at the time of the event,
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "message_variation_name": (string) the name of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "dispatch_id": (string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform). Users who are sent a schedule message get the same dispatch_id. Action-based or API-triggered messages get a unique dispatch_id per user.,
  "email_address": (string) email address for this event,
  "sending_ip": (string) the IP address from which the message was sent (Email Delivery, Bounce, and SoftBounce events only. Will only be shown on events if the message was actually attempted for delivery. For certain other bounces, the information could be lost if the recipient server has already accepted the mail and only later after the connection is closed decided it could not deliver the mail),
  "ip_pool": (string) IP pool used for message sending (for certain bounce cases, IP pool will not be provided) ,
  "bounce_reason": (string) reason for bounce provided by server,
  "esp": (string) ESP related to the event (SparkPost or SendGrid),
  "from_domain": (string) sending domain for the email,
  "is_drop": (boolean) indicates that this event counts as a drop event
}
```
#### Détails de la propriété
- Le comportement pour `dispatch_id` diffère entre Canvas et les campagnes, car Braze traite les étapes Canvas (à l’exception des étapes d’entrée, qui peuvent être programmées) comme des événements déclenchés, même lorsqu’ils sont « programmés ». En savoir plus sur [comportement de dispatch ID]({{site.baseurl}}/help/help_articles/data/dispatch_id/).
{% endapi %}

{% api %}

## Événement de « soft bounce » d’e-mail

{% apitags %}
E-mail, bounce
{% endapitags %}

Cet événement se produit lorsqu’un fournisseur de services Internet renvoie un soft bounce. Un soft bounce signifie qu’un e-mail n’a pas pu être livré en raison d’une défaillance temporaire de la délivrabilité.

```json
// Email Soft Bounce: users.messages.email.SoftBounce
{
  "id": (string) unique id of this event,
  "user_id": (string) Braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (string) IANA time zone of the user at the time of the event,
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "message_variation_name": (string) the name of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "dispatch_id": (string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform). Users who are sent a schedule message get the same dispatch_id. Action-based or API-triggered messages get a unique dispatch_id per user.,
  "email_address": (string) email address for this event,
  "sending_ip": (string) the IP address from which the message was sent (Email Delivery, Bounce, and SoftBounce events only. Will only be shown on events if the message was actually attempted for delivery. For certain other bounces, the information could be lost if the recipient server has already accepted the mail and only later after the connection is closed decided it could not deliver the mail),
  "ip_pool": (string) IP pool used for message sending(for certain bounce cases, IP pool will not be provided),
  "bounce_reason": (string) reason for bounce provided by server,
  "esp": (string) ESP related to the event (SparkPost or SendGrid),
  "from_domain": (string) sending domain for the email
}
```
#### Détails de la propriété
- Le comportement pour `dispatch_id` diffère entre Canvas et les campagnes, car Braze traite les étapes Canvas (à l’exception des étapes d’entrée, qui peuvent être programmées) comme des événements déclenchés, même lorsqu’ils sont « programmés ». En savoir plus sur [comportement de dispatch ID]({{site.baseurl}}/help/help_articles/data/dispatch_id/).
{% endapi %}

{% api %}

## Événements de spam pour un e-mail

{% apitags %}
E-mail, Spam
{% endapitags %}

Cet événement se produit lorsque l’utilisateur final clique sur le bouton « spam » sur l’e-mail. Notez que cela ne représente pas le fait que l’e-mail soit allé dans le dossier Spam, car Braze ne suit pas ça.

```json
// Email Mark As Spam: users.messages.email.MarkAsSpam
{
  "id": (string) unique id of this event,
  "user_id": (string) Braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (string) IANA time zone of the user at the time of the event,
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "message_variation_name": (string) the name of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "dispatch_id": (string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform). Users who are sent a schedule message get the same dispatch_id. Action-based or API-triggered messages get a unique dispatch_id per user.,
  "email_address": (string) email address for this event,
  "ip_pool": (string) IP pool used for message sending,
  "user_agent": (string) This field is no longer used in any destination for this event and will always be empty,
  "esp": (string) ESP related to the event (SparkPost or SendGrid),
  "from_domain": (string) sending domain for the email
}
```
#### Détails de la propriété

Le comportement pour `dispatch_id` diffère entre Canvas et les campagnes, car Braze traite les étapes Canvas (à l’exception des étapes d’entrée, qui peuvent être programmées) comme des événements déclenchés, même lorsqu’ils sont « programmés ». En savoir plus sur [comportement de dispatch ID]({{site.baseurl}}/help/help_articles/data/dispatch_id/).
{% endapi %}


{% api %}

## E-mail événements de désabonnement

{% apitags %}
E-mail, abonnement
{% endapitags %}

Cet événement se produit lorsque l’utilisateur final a cliqué sur « Se désabonner » dans l’e-mail.

{% alert important %}
L’événement `Unsubscribe` est en fait un événement de clic spécialisé qui se lance quand votre utilisateur clique sur le lien de désabonnement de l’e-mail (qu’il s’agisse d’un lien de désinscription habituel au sein de corps ou du pied de page de l’e-mail ou en utilisant l’[en-tête de désinscription de la liste]({{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/email_settings#include-a-list-unsubscribe-header)), pas le moment où l’état de l’utilisateur passe à « désabonné ». Si le changement de statut d’abonnement est envoyé via l’API, il ne déclenchera pas d’événement sur Currents.
{% endalert %}

```json
// Email Unsubscribe: users.messages.email.Unsubscribe
{
  "id": (string) unique id of this event,
  "user_id": (string) Braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (string) IANA time zone of the user at the time of the event,
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "message_variation_name": (string) the name of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "dispatch_id": (string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform). Users who are sent a schedule message get the same dispatch_id. Action-based or API-triggered messages get a unique dispatch_id per user.,
  "email_address": (string) email address for this event,
  "ip_pool": (string) IP pool used for message sending
}
```
#### Détails de la propriété

Le comportement pour `dispatch_id` diffère entre Canvas et les campagnes, car Braze traite les étapes Canvas (à l’exception des étapes d’entrée, qui peuvent être programmées) comme des événements déclenchés, même lorsqu’ils sont « programmés ». En savoir plus sur [comportement de dispatch ID]({{site.baseurl}}/help/help_articles/data/dispatch_id/).
{% endapi %}

{% api %}

## Événements d’abonnement

{% apitags %}
Abonnement, e-mail, SMS
{% endapitags %}

Cet événement se produit lorsque le statut d’abonnement d’un utilisateur dans un groupe d’abonnement change.

{% alert important %}
Les groupes d’abonnement sont disponibles uniquement pour les canaux e-mail et SMS.
{% endalert %}

```json
// Subscription Group State Change: users.behaviors.subscriptiongroup.StateChange
{
  "id": (string) unique id of this event,
  "user_id": (string) Braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "state_change_source": (string) Source of the state change, e.g: REST, SDK, Dashboard, Preference Center etc.,
  "channel": (string) either 'sms', 'email', or 'whats_app',
  "time": (int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (string) IANA time zone of the user at the time of the event,
  "app_id": (string) id for the app on which the user action occurred,
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "message_variation_name": (string) the name of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "email_address": (string) email address for this user,
  "phone_number": (string) phone number of the user (presented in e.164 format),
  "subscription_group_id": (string) id of the subscription group,
  "subscription_status": (string) status of the subscription after the change: 'Subscribed' or 'Unsubscribed'
}
```

#### Détails de la propriété

`state_change_source` renvoie une chaîne de caractères d’une ou deux lettres en fonction de la source. Les sources disponibles et les chaînes de caractères associées sont répertoriées ci-dessous :

| Source | Lettre |
| --- | --- |
| SDK | s |
| Tableau de bord | d |
| Page d’abonnement | p |
| API REST | r |
| Fournisseur d’attribution | a |
| Importation CSV | c |
| Centre de préférence amélioré | e |
| SMS entrant | i |
| SMS sortant | o |
| Migration | m |
| Fusion d’utilisateurs | g |
| Remplissage | b |
| Fournisseur de Shopify | sh |
{: .reset-td-br-1 .reset-td-br-2}

{% endapi %}


{% api %}

## Événements d’impression de messages in-app

{% apitags %}
Messages in-app, Impressions
{% endapitags %}

Cet événement se produit lorsqu’un utilisateur visualise un message in-app.

```json
// In-App Message Impression: users.messages.inappmessage.Impression
{
  "id": (string) unique id of this event,
  "user_id": (string) Braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (string) IANA time zone of the user at the time of the event,
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "message_variation_name": (string) the name of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "app_id": (string) id for the app on which the user action occurred,
  "platform": (string) platform of the device (one of 'ios', 'android', 'web', 'kindle', 'tvos', OR 'roku'),
  "os_version": (string) os version of device used for the action,
  "device_model": (string) hardware model of the device,
  "device_id": (string) id of the device on which the event occurred,
  "ad_id": (string) advertising identifier,
  "ad_id_type": (string) One of 'ios_idfa', 'google_ad_id', OR 'roku_ad_id',
  "ad_tracking_enabled": (boolean) whether advertising tracking is enabled for the device
}
```
#### Détails de la propriété
- Pour `ad_id`, `ad_id_type` et `ad_tracking_enabled`, vous devrez collecter explicitement les IDFA iOS et les ADID Android Google via les SDK natifs. Pour en savoir plus cliquez ici : [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/optional_idfa_collection/#optional-idfa-collection/), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id).
- Si vous utilisez Kafka pour ingérer des données [Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/), contactez votre gestionnaire du succès des clients ou votre gestionnaire de compte pour activer la bascule de fonctionnalité pour envoyer un `ad_id`.
{% endapi %}

{% api %}

## Événements de clics sur un message in-app

{% apitags %}
Messages in-app, clics
{% endapitags %}

Cet événement se produit lorsqu’un utilisateur clique sur un message in-app.

```json
// In-App Message Click: users.messages.inappmessage.Click
{
  "id": (string) unique id of this event,
  "user_id": (string) Braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (string) IANA time zone of the user at the time of the event,
  "button_id": (string) index of the button clicked if it was a button that was clicked, tracking ID of the click if the event came from an appboyBridge.logClick invocation, or choice_id if the in app-message type is a simple survey,
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "message_variation_name": (string) the name of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "app_id": (string) id for the app on which the user action occurred,
  "platform": (string) platform of the device (one of 'ios', 'android', 'web', 'kindle', 'tvos', OR 'roku'),
  "os_version": (string) os version of device used for the action,
  "device_model": (string) hardware model of the device,
  "device_id": (string) id of the device on which the event occurred,
  "ad_id": (string) advertising identifier,
  "ad_id_type": (string) One of 'ios_idfa', 'google_ad_id', OR 'roku_ad_id',
  "ad_tracking_enabled": (boolean) whether advertising tracking is enabled for the device
}
```
#### Détails de la propriété
- Pour `ad_id`, `ad_id_type` et `ad_tracking_enabled`, vous devrez collecter explicitement les IDFA iOS et les ADID Android Google via les SDK natifs. Pour en savoir plus cliquez ici : [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/optional_idfa_collection/#optional-idfa-collection/), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id).
- Si vous utilisez Kafka pour ingérer des données [Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/), contactez votre gestionnaire du succès des clients ou votre gestionnaire de compte pour activer la bascule de fonctionnalité pour envoyer un `ad_id`.
{% endapi %}


{% api %}

## Événements d’envoi de webhook

{% apitags %}
Webhooks, envois
{% endapitags %}

Cet événement se produit lorsqu’un webhook a été traité et envoyé à la tierce partie spécifiée dans le webhook. Notez que cela n’indique pas si la demande a été reçue ou non.

```json
// Webhook Send: users.messages.webhook.Send
{
  "id": (string) unique id of this event,
  "user_id": (string) Braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (string) IANA time zone of the user at the time of the event,
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "message_variation_name": (string) the name of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under API Identifier Types)
}
```
{% endapi %}

{% api %}
## Événements d’envoi de carte de contenu

{% apitags %}
Cartes de contenu, envois
{% endapitags %}

Cet événement se produit lorsqu’une carte de contenu est envoyée à un utilisateur.

```json
// Content Card Send: users.messages.contentcard.Send
{
  "id": (string) unique id of this event,
  "user_id": (string) Braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (string) IANA time zone of the user at the time of the event,
  "content_card_id": (string) id of the content card that was sent,
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "message_variation_name": (string) the name of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "device_id": (string) id of the device on which the event occurred
}
```

{% endapi %}

{% api %}
## Événements d’impression de carte de contenu

{% apitags %}
Cartes de contenu, Impressions
{% endapitags %}

Cet événement se produit lorsqu’un utilisateur visualise une carte de contenu.

```json
// Content Card Impression: users.messages.contentcard.Impression
{
  "id": (string) unique id of this event,
  "user_id": (string) Braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (string) IANA time zone of the user at the time of the event,
  "app_id": (string) id for the app on which the user action occurred,
  "content_card_id": (string) id of the content card that was viewed/clicked/dismissed,
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "message_variation_name": (string) the name of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "platform": (string) platform of the device (one of 'ios', 'android', 'web', 'kindle', 'tvos', OR 'roku'),
  "os_version": (string) os version of device used for the action,
  "device_model": (string) hardware model of the device,
  "device_id": (string) id of the device on which the event occurred,
  "ad_id": (string) advertising identifier,
  "ad_id_type": (string) One of 'ios_idfa', 'google_ad_id', OR 'roku_ad_id',
  "ad_tracking_enabled": (boolean) whether advertising tracking is enabled for the device
}
```
#### Détails de la propriété
- Pour `ad_id`, `ad_id_type` et `ad_tracking_enabled`, vous devrez collecter explicitement les IDFA iOS et les ADID Android Google via les SDK natifs. Pour en savoir plus cliquez ici : [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/optional_idfa_collection/#optional-idfa-collection/), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id).
- Si vous utilisez Kafka pour ingérer des données [Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/), contactez votre gestionnaire du succès des clients ou votre gestionnaire de compte pour activer la bascule de fonctionnalité pour envoyer un `ad_id`.
{% endapi %}

{% api %}
## Événements de clic sur carte de contenu

{% apitags %}
Cartes de contenu, clics
{% endapitags %}

Cet événement se produit lorsqu’un utilisateur clique sur une carte de contenu.

```json
// Content Card Click: users.messages.contentcard.Click
{
  "id": (string) unique id of this event,
  "user_id": (string) Braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (string) IANA time zone of the user at the time of the event,
  "app_id": (string) id for the app on which the user action occurred,
  "content_card_id": (string) id of the content card that was viewed/clicked/dismissed,
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "message_variation_name": (string) the name of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "platform": (string) platform of the device (one of 'ios', 'android', 'web', 'kindle', 'tvos', OR 'roku'),
  "os_version": (string) os version of device used for the action,
  "device_model": (string) hardware model of the device,
  "device_id": (string) id of the device on which the event occurred,
  "ad_id": (string) advertising identifier,
  "ad_id_type": (string) One of 'ios_idfa', 'google_ad_id', OR 'roku_ad_id',
  "ad_tracking_enabled": (boolean) whether advertising tracking is enabled for the device
}
```
#### Détails de la propriété
- Pour `ad_id`, `ad_id_type` et `ad_tracking_enabled`, vous devrez collecter explicitement les idfa iOS et les adid Android Google via les SDK natifs. Pour en savoir plus cliquez ici : [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/optional_idfa_collection/#optional-idfa-collection/), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id).
- Si vous utilisez Kafka pour ingérer des données [Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/), contactez votre gestionnaire du succès des clients ou votre gestionnaire de compte pour activer la bascule de fonctionnalité pour envoyer un `ad_id`.
{% endapi %}


{% api %}
## Événements de fermeture de carte de contenu

{% apitags %}
Cartes de contenu, rejet
{% endapitags %}

Cet événement se produit lorsqu’un utilisateur rejette une carte de contenu.

```json
// Content Card Dismiss: users.messages.contentcard.Dismiss
{
  "id": (string) unique id of this event,
  "user_id": (string) Braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (string) IANA time zone of the user at the time of the event,
  "app_id": (string) id for the app on which the user action occurred,
  "content_card_id": (string) id of the content card that was viewed/clicked/dismissed,
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "message_variation_name": (string) the name of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "platform": (string) platform of the device (one of 'ios', 'android', 'web', 'kindle', 'tvos', OR 'roku'),
  "os_version": (string) os version of device used for the action,
  "device_model": (string) hardware model of the device,
  "device_id": (string) id of the device on which the event occurred,
  "ad_id": (string) advertising identifier,
  "ad_id_type": (string) One of 'ios_idfa', 'google_ad_id', OR 'roku_ad_id',
  "ad_tracking_enabled": (boolean) whether advertising tracking is enabled for the device
}
```
#### Détails de la propriété
- Pour `ad_id`, `ad_id_type` et `ad_tracking_enabled`, vous devrez collecter explicitement les idfa iOS et les adid Android Google via les SDK natifs. Pour en savoir plus cliquez ici : [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/optional_idfa_collection/#optional-idfa-collection/), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id).
- Si vous utilisez Kafka pour ingérer des données [Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/), contactez votre gestionnaire du succès des clients ou votre gestionnaire de compte pour activer la bascule de fonctionnalité pour envoyer un `ad_id`.
{% endapi %}

{% api %}

## Événement d’impression du Fil d'actualité

{% alert note %}
Le Fil d’actualité est obsolète. Braze recommande aux clients qui utilisent notre outil de fil d’actualités de passer à notre canal de communication de cartes de contenu : il est plus flexible, plus personnalisable et plus fiable. Consultez le [guide de migration]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/) pour en savoir plus.
{% endalert %}

{% apitags %}
Fil d'actualité, Impressions
{% endapitags %}

Cet événement se produit lorsqu’un utilisateur regarde le fil d’actualités.

{% alert tip %}
Le schéma [Impression du Fil d'actualité]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/customer_behavior_events/#news-feed-impression-event) (`users.behaviors.app.NewsFeedImpression`) se trouve dans le glossaire des événements de comportement client, car ces données n’ont pas été classées comme événement d’engagement sur message. 
{% endalert %}

```json
// News Feed Card Impression: users.messages.newsfeedcard.Impression
{
  "id": (string) unique id of this event,
  "user_id": (string) Braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (string) IANA time zone of the user at the time of the event,
  "card_id": (string) id of the card that was viewed,
  "app_id": (string) id for the app on which the user action occurred,
  "platform": (string) platform of the device (one of 'ios', 'android', 'web', 'kindle', 'tvos', OR 'roku'),
  "os_version": (string) os version of device used for the action,
  "device_model": (string) hardware model of the device,
  "device_id": (string) id of the device on which the event occurred
}
```
{% endapi %}


{% api %}

## Événements de clics sur Fil d'actualité

{% apitags %}
Fil d'actualité, clics
{% endapitags %}

Cet événement se produit lorsqu’un utilisateur clique sur le fil d’actualités.

{% alert tip %}
Le schéma [Impression du Fil d'actualité]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/customer_behavior_events/#news-feed-impression-event) (`users.behaviors.app.NewsFeedImpression`) se trouve dans le glossaire des événements de comportement client, car ces données n’ont pas été classées comme événement d’engagement sur message. 
{% endalert %}

```json
// News Feed Card Click: users.messages.newsfeedcard.Click
{
  "id": (string) unique id of this event,
  "user_id": (string) Braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (string) IANA time zone of the user at the time of the event,
  "card_id": (string) id of the card that was clicked,
  "app_id": (string) id for the app on which the user action occurred,
  "platform": (string) platform of the device (one of 'ios', 'android', 'web', 'kindle', 'tvos', OR 'roku'),
  "os_version": (string) os version of device used for the action,
  "device_model": (string) hardware model of the device,
  "device_id": (string) id of the device on which the event occurred
}
```
{% endapi %}

{% api %}

## Événements de clic SMS

{% apitags %}
SMS, clics
{% endapitags %}

Cet événement se produit lorsqu’un utilisateur clique sur un lien court SMS.

```json
// SMS Send: users.messages.sms.ShortLinkClick
{
  "id": (string) unique id of this event,
  "user_id": (string) Braze user ID of the user targeted by short_url,
  "external_user_id": (string) External ID of the user, null if short_url,
  "device_id": (string) Device ID of the user targeted by short_url if user is anonymous, 
  "time": (int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (string) IANA timezone of the user at the time of the event, null if short_url did not use user click tracking,
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign if from a campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "message_variation_name": (string) the name of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas if from a Canvas,
  "canvas_variation_id": (string) ID of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (string) name of the Canvas variation a user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  "canvas_step_message_variation_id": (string) ID of the message variation if from a Canvas,
  "canvas_step_message_variation_name": (string) name of the message variation if from a Canvas,
  "url": (string) original URL contained in message that was shortened for click tracking,
  "short_url": (string) shortened URL that is sent to user for click tracking,
  "user_agent": (string) User-Agent header of the device performing the click event,
  "user_phone_number": (string) Phone number of the user that short_url was sent to
}
```
{% endapi %}
{% api %}
## Événements d’envoi SMS

{% apitags %}
SMS, envois
{% endapitags %}

Cet événement se produit lorsqu’un utilisateur envoie un SMS.

```json
// SMS Send: users.messages.sms.Send
{
  "id": (string) unique id of this event,
  "user_id": (string) Braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (string) IANA time zone of the user at the time of the event,
  "from_phone_number": (string) the from phone number of the message (Delivered and Undelivered only),
  "subscription_group_id": (string) id of the subscription group targeted for this SMS message,
  "to_phone_number": (string) the number the message was sent to,
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "message_variation_name": (string) the name of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  "dispatch_id": (string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform and users who are sent a schedule message get the same dispatch_id. Action-based or API-triggered messages get a unique dispatch_id per user
  "send_id": (string) message send ID this message belongs to,
  "category" : (string) If the SMS was sent as a result of auto-response to one of your global SMS keywords, the Category will be reflected here (e.g Opt-In, Opt-Out, Help) 
}
```
{% endapi %}

{% api %}

## Événements d’envoi SMS à l’opérateur

{% apitags %}
SMS, livraison
{% endapitags %}

Cet événement survient lorsqu’un SMS est envoyé à l’opérateur.

```json
// SMS Delivery: users.messages.sms.CarrierSend
{
  "id": (string) unique id of this event,
  "user_id": (string) Braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (string) IANA time zone of the user at the time of the event,
  "from_phone_number": (string) the from phone number of the message (Delivered and Undelivered only),
  "subscription_group_id": (string) id of the subscription group targeted for this SMS message,
  "to_phone_number": (string) the number the message was sent to,
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "message_variation_name": (string) the name of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  "dispatch_id": (string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform and users who are sent a schedule message get the same dispatch_id. Action-based or API-triggered messages get a unique dispatch_id per user,
  "send_id": (string) message send ID this message belongs to
}
```
{% endapi %}

{% api %}

## Événements de livraison SMS

{% apitags %}
SMS, livraison
{% endapitags %}

Cet événement se produit lorsqu’un SMS a été envoyé avec succès sur le téléphone mobile de l’utilisateur.

```json
// SMS Delivery: users.messages.sms.Delivery
{
  "id": (string) unique id of this event,
  "user_id": (string) Braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (string) IANA time zone of the user at the time of the event,
  "from_phone_number": (string) the from phone number of the message (Delivered and Undelivered only),
  "subscription_group_id": (string) id of the subscription group targeted for this SMS message,
  "to_phone_number": (string) the number the message was sent to,
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "message_variation_name": (string) the name of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  "dispatch_id": (string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform and users who are sent a schedule message get the same dispatch_id. Action-based or API-triggered messages get a unique dispatch_id per user,
  "send_id": (string) message send ID this message belongs to
}
```
{% endapi %}

{% api %}

## Événements de rejet SMS

{% apitags %}
SMS, Rejet
{% endapitags %}

Cet événement survient lorsqu’un envoi SMS est rejeté par l’opérateur ce qui peut se produire pour plusieurs raisons. Utilisez cet événement et les codes d’erreur fournis pour résoudre les problèmes liés à la livraison de SMS.

```json
// SMS Rejection: users.messages.sms.Rejection
{
  "id": (string) unique id of this event,
  "user_id": (string) Braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (string) IANA time zone of the user at the time of the event,
  "from_phone_number": (string) the from phone number of the message (Delivered and Undelivered only),
  "subscription_group_id": (string) id of the subscription group targeted for this SMS message,
  "subscription_group_api_id": (string) api id of the subscription group targeted for this SMS message,
  "to_phone_number": (string) the number the message was sent to,
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "message_variation_name": (string) the name of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  "dispatch_id": (string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform and users who are sent a schedule message get the same dispatch_id. Action-based or API-triggered messages get a unique dispatch_id per user,
  "send_id": (string) message send ID this message belongs to,
  "error": (string) the Braze provided error (Rejection and Delivery Failure events only),
  "provider_error_code": (string) the provider's reason code as to why the message was not sent (Rejection and Delivery Failure events only)
}
```
{% endapi %}


{% api %}

## Événements d’échec de livraison SMS

{% apitags %}
SMS, livraison
{% endapitags %}

Cet événement survient lorsqu’un SMS rencontre un problème de livraison. Utilisez cet événement et les codes d’erreur fournis pour résoudre les problèmes liés à la livraison de SMS.

```json
// SMS Delivery Failure: users.messages.sms.DeliveryFailure
{
  "id": (string) unique id of this event,
  "user_id": (string) Braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (string) IANA time zone of the user at the time of the event,
  "from_phone_number": (string) the from phone number of the message (Delivered and Undelivered only),
  "subscription_group_id": (string) id of the subscription group targeted for this SMS message,
  "subscription_group_api_id": (string) api id of the subscription group targeted for this SMS message,
  "to_phone_number": (string) the number the message was sent to,
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "message_variation_name": (string) the name of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  "dispatch_id": (string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform and users who are sent a schedule message get the same dispatch_id. Action-based or API-triggered messages get a unique dispatch_id per user,
  "send_id": (string) message send ID this message belongs to,
  "error": (string) the Braze provided error (Rejection and Delivery Failure events only),
  "provider_error_code": (string) the provider's reason code as to why the message was not sent (Rejection and Delivery Failure events only)
}
```
{% endapi %}
{% api %}

## Événements de réception de SMS entrant

{% apitags %}
SMS, EntrantReçu
{% endapitags %}

Cet événement se produit lorsque l’un de vos utilisateurs envoie un SMS à un numéro de téléphone dans l’un de vos groupes d’abonnement SMS Braze. 

Notez que lorsque Braze reçoit un SMS entrant, nous attribuons ce message entrant à tout utilisateur qui partage ce numéro de téléphone. Par conséquent, vous pouvez recevoir plusieurs événements par message entrant si plusieurs utilisateurs de votre instance Braze partagent le même numéro de téléphone. Si vous devez attribuer des ID Utilisateurs spécifiques sur la base des messages précédents envoyés à cet utilisateur, vous pouvez utiliser l’événement SMS Livré pour attribuer des événements entrants reçus à l’ID utilisateur qui a reçu le plus récemment un message de votre numéro Braze.

Si nous détectons que ce message entrant est une réponse à une campagne sortante ou à une étape Canvas envoyée par Braze, nous inclurons également les métadonnées Canvas ou Campagne avec l’événement. Braze définit une réponse comme un message entrant dans les quatre heures suivant un message sortant. Cependant, il y a un cache d’une minute pour les informations d’attribution de campagne sur le dernier SMS sortant reçu.

```json
// SMS Inbound Received: users.messages.sms.InboundReceive
{
  "id": (string) unique id of this event,
  "user_id": (string) Braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "app_group_id": (string) API ID of the app group associated with the inbound phone number,
  "time": (int) 10-digit UTC time of the event in seconds since the epoch,
  "user_phone_number": (string) the phone number of the user who sent the message to your Braze number,
  "subscription_group_id": (string) id of the subscription group which the phone number the user messaged belongs to,
  "inbound_phone_number": (string) the phone number the message was sent to,
  "inbound_media_urls": (string) the URLs of inbound media attachments if received, 
  "action" : (string) the subscription action Braze took as a result of this message (either `subscribed`, `unsubscribed` or `none` based on the message body. `None` indicates this inbound message did not match any of your keywords to opt-in or opt-out a user),
  "message_body" : (string) the body of the message sent by the user,
  "campaign_id": (string) id of the campaign if Braze identifies this inbound message is a reply to a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if Braze identifies this inbound message is a reply to a campaign,
  "message_variation_name": (string) the name of the message variation if Braze identifies this inbound message is a reply to a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "canvas_step_name": (string) name of the step for this message if from a Canvas
}
```
{% endapi %}


{% api %}

## Événements de conversion de campagne

{% apitags %}
Campagne, conversion
{% endapitags %}

Cet événement se produit lorsqu’un utilisateur effectue une action définie comme événement de conversion dans une campagne.

{% alert important %}
Notez que l’événement de conversion est encodé dans le champ`conversion_behavior`, qui inclut le type d’événement de conversion, la fenêtre (période) et des informations supplémentaires en fonction du type d’événement de conversion. Le champ `conversion_behavior_index` représente l’événement de conversion, c.-à-d. 0 = A, 1 = B, 2 = C, 3 = D.
{% endalert %}

```json
// Campaign Conversion Event: users.campaigns.Conversion
{
  "id": (string) unique id of this event,
  "user_id": (string) Braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (string) IANA time zone of the user at the time of the event,
  "app_id": (string) id for the app on which the user action occurred,
  "campaign_id": (string) id of the campaign,
  "campaign_name": (string) name of the campaign,
  "conversion_behavior_index": (int) index of the conversion behavior,
  "conversion_behavior": (string) JSON-encoded string describing the conversion behavior,
  "message_variation_id": (string) id of the message variation,
  "message_variation_name": (string) the name of the message variation,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under API Identifier Types)
}
```
{% endapi %}


{% api %}

## Événements de conversion Canvas

{% apitags %}
Canvas, Conversion
{% endapitags %}

Cet événement se produit lorsqu’un utilisateur effectue une action définie comme un événement de conversion dans Canvas.

{% alert important %}
Notez que l’événement de conversion est encodé dans le champ`conversion_behavior`, qui inclut le type d’événement de conversion, la fenêtre (période) et des informations supplémentaires en fonction du type d’événement de conversion. Le champ `conversion_behavior_index` représente l’événement de conversion, c.-à-d. 0 = A, 1 = B, 2 = C, 3 = D.
{% endalert %}

```json
// Canvas Conversion Event: users.canvas.Conversion
{
  "id": (string) unique id of this event,
  "user_id": (string) Braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (string) IANA time zone of the user at the time of the event,
  "app_id": (string) id for the app on which the user action occurred,
  "canvas_id": (string) id of the Canvas,
  "canvas_name": (string) name of the Canvas,
  "conversion_behavior_index": (int) index of the conversion behavior,
  "conversion_behavior": (string) JSON-encoded string describing the conversion behavior,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the last step the user was sent before the conversion
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
}
```
{% endapi %}


{% api %}

## Événements d’entrée Canvas

{% apitags %}
Canvas, Entrée
{% endapitags %}

Cet événement se produit lorsqu’un utilisateur entre dans le Canvas. Cet événement vous dit dans quelle variante l’utilisateur est entré.

```json
// Canvas Entry Event: users.canvas.Entry
{
  "id": (string) unique id of this event,
  "user_id": (string) Braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (string) IANA time zone of the user at the time of the event,
  "canvas_id": (string) id of the Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step the user entered into,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  "in_control_group": (boolean) whether the user was enrolled in the control group for a Canvas
}
```

{% endapi %}

{% api %}
## Événements d’inscription à un groupe de contrôle de campagne

{% apitags %}
Campagne, entrée
{% endapitags %}

Cet événement se produit lorsqu’un utilisateur est inscrit dans une variante de contrôle définie sur une campagne à plusieurs variantes. Cet événement est généré car il n’y aura pas d’événement d’envoi sur canal pour cet utilisateur.

```json
// Campaign Control Group Enrollment: users.campaigns.EnrollInControl
{
  "id": (string) unique id of this event,
  "user_id": (string) Braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "app_id": (string) id for the app on which the user action occurred,
  "time": (int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (string) IANA time zone of the user at the time of the event,
  "campaign_id": (string) id of the campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation,
  "message_variation_name": (string) the name of the message variation,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under API Identifier Types)
}
```

{% endapi %}

{% api %}

## Événements de changement d’état global

{% apitags %}
Abonnement
{% endapitags %}

Cet événement se produit lorsque le statut global d’abonnement de l’utilisateur change.

```json
// Global State Change: users.behaviors.subscription.GlobalStateChange
{
  "id": (string) unique ID of this event,
  "user_id": (string) Braze BSON id of the user with this global subscription state change,
  "external_user_id": (string) External ID of the user,
  "email_address": (string) User email address,
  "state_change_source": (string) Source of the state change, e.g: REST, SDK, Dashboard, Preference Center etc.,
  "subscription_status": (string) Global subscription status: Subscribed, Unsubscribed and Opt-In,
  "channel": (string) Channel: only email for now,
  "time": (string) 10-digit UTC time of the state change event in seconds since the epoch,
  "timezone": (string) IANA timezone of the user at the time of the event,
  "app_group_id": (string) BSON id of the app group this user belongs to,
  "app_group_api_id": (string) API id of the app group this user belongs to,
  "app_api_id": (string) API id of the app the event belongs to,
  "campaign_id": (string) BSON id of the Campaign if from a Campaign,
  "campaign_api_id": (string) API id of the Campaign if from a Campaign,
  "message_variation_api_id": (string) API id of the message variation if from a Campaign,
  "canvas_id": (string) BSON id of the Canvas if from a Canvas,
  "canvas_api_id": (string) API id of the Canvas if from a Canvas,
  "canvas_variation_api_id  ": (string) API id of the Canvas variation if from a Canvas,
  "canvas_step_api_id": (string) API id of the Canvas step if from a Canvas,
  "send_id": (string) Message send id this subscription state change action originated from
}
```

#### Détails de la propriété

`state_change_source` renvoie une chaîne de caractères d’une ou deux lettres en fonction de la source. Les sources disponibles et les chaînes de caractères associées sont répertoriées ci-dessous :

| Source | Lettre |
| --- | --- |
| SDK | s |
| Tableau de bord | d |
| Page d’abonnement | p |
| API REST | r |
| Fournisseur d’attribution | a |
| Importation CSV | c |
| Centre de préférence amélioré | e |
| SMS entrant | i |
| SMS sortant | o |
| Migration | m |
| Fusion d’utilisateurs | g |
| Remplissage | b |
| Fournisseur de Shopify | sh |
{: .reset-td-br-1 .reset-td-br-2}

{% endapi %}
{% api %}
## Événements de désinstallation

{% apitags %}
Désinstallation
{% endapitags %}

Cet événement se produit lorsqu’un utilisateur désinstalle une application. Utilisez ces données pour suivre les utilisateurs qui désinstallent une application. C’est actuellement un événement d’engagement via message, mais cela sera changé en événement de comportement utilisateur dans le futur.

{% alert important %}
Cet événement n’est pas déclenché au moment précis où l’utilisateur désinstalle réellement l’application, car cette action est impossible à suivre exactement. Braze envoie une notification push silencieuse quotidienne pour déterminer si l’application existe toujours sur l’appareil de votre utilisateur, et si nous obtenons une erreur sur cette notification push silencieuse, on suppose alors que l’application a été désinstallée.
{% endalert %}

```json
// Uninstall Event: users.behaviors.Uninstall
{
  "id": (string) unique id of this event,
  "user_id": (string) Braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) 10-digit UTC time of the event in seconds since the epoch,
  "app_id": (string) id for the app on which the user action occurred,
  "device_id": (string) id of the device on which the session occurred
}
```

{% endapi %}