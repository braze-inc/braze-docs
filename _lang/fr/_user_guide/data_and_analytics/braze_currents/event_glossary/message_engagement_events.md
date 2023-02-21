---
nav_title: Événements d’engagement sur les messages
layout: message_engagement_events_glossary
page_order: 5
excerpt_separator: ""
page_type: glossary
description: "Ce glossaire répertorie les différents comportements client et événements utilisateur que Braze peut suivre et envoyer via Currents à des entrepôts de données désignés."
tool: Currents
search_rank: 4
---

Contactez votre gestionnaire de compte ou ouvrez un [ticket de support]({{site.baseurl}}/braze_support/) si vous avez besoin d’accéder à d’autres événements. Si vous ne trouvez pas ce dont vous avez besoin dans cet article, consultez notre [Bibliothèque des événements de comportement client]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/customer_behavior_events/) ou nos [Exemples d’échantillons de données Currents](https://github.com/Appboy/currents-examples/tree/master/sample-data).

{% details Explication de la structure d’événement d’engagement par message et des valeurs de la plateforme %}

### Structure d’événement

Cette ventilation des événements montre le type d’information généralement inclus dans un événement d’engagement de message. Avec une bonne compréhension de ses composants, vos développeurs et votre équipe BI peuvent utiliser les données d’événements Currents entrants pour créer des rapports et des graphiques axés sur les données, et tirer parti des métriques de données fournies.

![Ventilation d’un événement d’engagement de messages montrant un événement de désabonnement par e-mail avec les propriétés répertoriées groupées par propriétés spécifiques à l’utilisateur, par campagne ou par Canvas, et propriétés spécifiques à l’événement]({% image_buster /assets/img/message_engagement_event.png %})

Les événements d’engagement sur les messages sont composés de propriétés **spécifique à l’utilisateur**, de propriétés de **suivi de campagne/Canvas**, et de propriétés **spécifiques à l’événement**.

### Valeurs de la plateforme

Certains événements renvoient une valeur qui spécifie la `plateforme` de l’appareil de l’utilisateur. 
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

## Événements de sortie du Canvas ayant effectué un événement

{% apitags %}
Sortie, Canvas
{% endapitags %}

Cet événement ce produit lorsqu’un utilisateur quitte un Canvas en effectuant un événement.

```json
// Sortie du Canvas ayant effectué un événement : users.canvas.exit.PerformedEvent
// Détails de sortie du Canvas ayant effectué un événement : users_canvas_exit_PerformedEvent_Details

{
  "id": (string) ID global unique de cet événement,
  "user_id": (string) ID utilisateur Braze de l’utilisateur, 
  "external_user_id": (string) ID utilisateur externe de l’utilisateur,
  "app_group_id": (string) ID BSON du groupe d’apps auquel appartient cet utilisateur,
  "app_group_api_id": (string) ID API du groupe d’apps auquel appartient cet utilisateur,
  "time": (int) horodatage Unix de l’événement,
  "canvas_id": (string) ID du Canvas s’il provient d’un Canvas,
  "canvas_variation_id": (string) ID de la variation Canvas dans laquelle se trouve l’utilisateur,
  "canvas_step_id": (string) ID BSON de l’étape Canvas à laquelle appartient cet événement,
  "canvas_api_id": (string) ID API du Canvas auquel appartient cet événement,,
  "canvas_variation_api_id": (string) ID API de la variation de canvas auquel appartient cet événement,
  "canvas_step_api_id": (string) ID API de l’étape canvas à laquelle appartient cet événement,
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
// Sortie du Canvas par correspondance à une audience : users_canvas_exit_MatchedAudience
// Détails de sortie du Canvas par correspondance à une audience : users_canvas_exit_MatchedAudience_Details

{
  "id": (string) ID global unique de cet événement,
  "user_id": (string) ID utilisateur Braze de l’utilisateur, 
  "external_user_id": (string) ID utilisateur externe de l’utilisateur,
  "app_group_id": (string) ID BSON du groupe d’apps auquel appartient cet utilisateur,
  "app_group_api_id": (string) ID API du groupe d’apps auquel appartient cet utilisateur,
  "time": (int) horodatage Unix de l’événement,
  "canvas_id": (string) ID du Canvas s’il provient d’un Canvas,
  "canvas_variation_id": (string) ID de la variation Canvas dans laquelle se trouve l’utilisateur,
  "canvas_step_id": (string) ID BSON de l’étape Canvas à laquelle appartient cet événement,
  "canvas_api_id": (string) ID BSON de l’étape d’expérience à laquelle appartient cet événement,
  "canvas_variation_api_id": (string) ID API de la variation de canvas auquel appartient cet événement,
  "canvas_step_api_id": (string) ID API de l’étape canvas à laquelle appartient cet événement,
}
```
{% endapi %}
{% api %}
## Événements d’entrée fractionnée Experiment

{% apitags %}
Étape d’expérience, Canvas
{% endapitags %}

Cet événement se produit quand un utilisateur entre dans un parcours d’étape de Canvas Experiment.

```json
// Entrée dans un parcours séparé d’étape d’expérience : users.canvas.experimentstep.SplitEntry

{
  "id": (string) ID global unique de cet événement,
  "user_id": (string) ID utilisateur Braze de l’utilisateur, 
  "external_user_id": (string) ID utilisateur externe de l’utilisateur,
  "time": (int) horodatage Unix de l’événement,
  "canvas_id": (string) ID du Canvas s’il provient d’un Canvas,
  "canvas_name": (string) nom du Canvas,
  "canvas_variation_id": (string) ID de la variation Canvas dans laquelle se trouve l’utilisateur,
  "canvas_variation_name": (string) nom de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "experiment_step_id": (string) ID BSON de l’étape d’expérience à laquelle appartient cet événement,
  "canvas_step_id": (string) ID de l’étape pour ce message s’il provient d’un Canvas,
  "canvas_step_name": (string) nom de l’étape pour ce message s’il provient d’un Canvas,
  "experiment_split_id": (string) ID BSON de la division d’expérience à laquelle l’utilisateur s’est inscrit,
  "experiment_split_name": (string) nom de la division d’expérience à laquelle l’utilisateur s’est inscrit,
  "in_control_group": (boolean) si l’utilisateur était inscrit dans le groupe de contrôle
}
```
{% endapi %}

{% api %}

## Événements de conversion d’expérience

{% apitags %}
Étape d’expérience, Canvas
{% endapitags %}

Cet événement se produit quand un utilisateur se convertit pour une étape de Canvas Experiment.

```json
// Conversion vers une étape d’expérience : users.canvas.experimentstep.Conversion

{
  "id": (string) ID global unique de cet événement,
  "user_id": (string) ID utilisateur Braze de l’utilisateur, 
  "external_user_id": (string) ID utilisateur externe de l’utilisateur,
  "app_group_id": (string) ID BSON du groupe d’apps auquel appartient cet utilisateur,
  "time": (int) horodatage Unix de l’événement,
  "workflow_id": (string) ID Braze à usage interne du flux de travail auquel cet événement appartient,
  "experiment_step_id": (string) ID BSON de l’étape d’expérience à laquelle appartient cet événement,
  "experiment_split_id": (string) ID BSON de la variation de répartition du test reçue par cet utilisateur,
  "conversion_behavior_index": (int) index du comportement de conversion
}
```
{% endapi %}
{% api %}

## Événements d’envoi Push

{% apitags %}
Push, envois
{% endapitags %}

Cet événement survient lorsque Braze traite un message de notification push pour un utilisateur, en le communiquant au service de notification push d’Apple ou Fire Cloud Messaging. Cela ne signifie pas que la notification push a été livrée sur l’appareil, cela indique juste qu’un message a été envoyé.

```json
// Envoi de Notification Push : users.messages.pushnotification.Send
{
  "id": (string) ID unique pour cet événement,
  "user_id": (string) ID utilisateur Braze de l’utilisateur,
  "external_user_id": (string) ID externe de l’utilisateur,
  "time": (int) heure en UTC à 10 chiffres de l’événement, en secondes, depuis la période,
  "timezone": (string) fuseau horaire de l’utilisateur au format IANA à l’heure de l’événement,
  "app_id": (string)ID de l’application sur laquelle l’action de l’utilisateur s’est produite,
  "campaign_id": (string) ID de la campagne si provenant d’une campagne,
  "campaign_name": (string) nom de la campagne,
  "message_variation_id": (string) ID de la variation du message si provenant d’une campagne,
  "message_variation_name": (string) le nom de la variation du message si provenant d’une campagne,
  "canvas_id": (string) ID du Canvas s’il provient d’un Canvas,
  "canvas_name": (string) nom du Canvas,
  "canvas_variation_id": (string) ID de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_variation_name": (string) nom de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_step_id": (string) ID de l’étape pour ce message s’il provient d’un Canvas,
  "canvas_step_name": (string) nom de l’étape pour ce message s’il provient d’un Canvas,
  "platform": (string) plateforme de l’appareil (un parmi 'ios', 'android', 'web', 'kindle', 'tvos' OU 'roku'),
  "device_id": (string)ID de l’appareil auquel nous avons essayé de livrer,
  "send_id": (string) ID du message si spécifié pour la campagne (voir Envoyer un identifiant sous Types d’identifiant API),
  "dispatch_id": (string) ID de distribution du message (ID unique pour chaque « transmission » envoyée depuis la plateforme Braze). Les utilisateurs qui reçoivent un message planifié reçoivent le même dispatch_id. Les messages basés sur des actions ou les messages déclenchés par API reçoivent un dispatch_id unique pour chaque utilisateur,
  "ad_id": (string) identifiant publicitaire,
  "ad_id_type": (string) Un parmi 'ios_idfa', 'google_ad_id', 'windows_ad_id' OU 'roku_ad_id',
  "ad_tracking_enabled": (boolean) si le suivi publicitaire est activé pour l’appareil ou non
}
```
#### Détails de la propriété
- Pour `ad_id`, `ad_id_type` et `ad_tracking_enabled`, vous devrez collecter explicitement les IDFA iOS et les ADID Android Google via les SDK natifs. Pour en savoir plus, cliquez ici : [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/optional_idfa_collection/#optional-idfa-collection/), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id).
- Si vous utilisez Kafka pour ingérer des données [Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/) , contactez votre gestionnaire du succès des clients ou votre gestionnaire de compte pour activer la bascule Oui/Non pour l’envoi`ad_id`.
{% endapi %}
{% api %}

## Événements d’ouvertures de Push

{% apitags %}
Push, Ouvertures
{% endapitags %}

Cet événement se produit lorsqu’un utilisateur clique directement sur la notification Push pour ouvrir l’application. Actuellement, les événements d’ouverture de Push se rapportent spécifiquement aux « Ouvertures directes » plutôt qu’au « total des ouvertures». Cela n’inclut pas les statistiques affichées au niveau des « ouvertures influencées » de la campagne car elles ne sont pas attribuées au niveau de l’utilisateur.

```json
// Envoi de Notification Push : users.messages.pushnotification.Open
{
  "id": (string) ID unique pour cet événement,
  "user_id": (string) ID utilisateur Braze de l’utilisateur,
  "external_user_id": (string) ID externe de l’utilisateur,
  "time": (int) heure en UTC à 10 chiffres de l’événement, en secondes, depuis la période,
  "timezone": (string) fuseau horaire de l’utilisateur au format IANA à l’heure de l’événement,
  "app_id": (string)ID de l’application sur laquelle l’action de l’utilisateur s’est produite,
  "campaign_id": (string) ID de la campagne si provenant d’une campagne,
  "campaign_name": (string) nom de la campagne,
  "message_variation_id": (string) ID de la variation du message si provenant d’une campagne,
  "message_variation_name": (string) le nom de la variation du message si provenant d’une campagne,
  "canvas_id": (string) ID du Canvas s’il provient d’un Canvas,
  "canvas_name": (string) nom du Canvas,
  "canvas_variation_id": (string) ID de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_variation_name": (string) nom de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_step_id": (string) ID de l’étape pour ce message s’il provient d’un Canvas,
  "canvas_step_name": (string) nom de l’étape pour ce message s’il provient d’un Canvas,
  "canvas_step_message_variation_id": (string)ID API de la variation de message de l’étape Canvas que cet utilisateur a reçue,
  "platform": (string) plateforme de l’appareil (un parmi 'ios', 'android', 'web', 'kindle', 'tvos' OU 'roku'),
  "os_version": (string) version du système d’exploitation de l’appareil utilisé pour l’action,
  "device_model": (string) modèle matériel de l’appareil,
  "device_id": (string)ID de l’appareil auquel nous avons essayé de livrer,
  "button_action_type": (string) Type d’action de la notification push,
  bouton. Un parmi [URI, DEEP_LINK, NONE, CLOSE, SHARE]. Vide si ne provient pas
  d’un clic de bouton,
  "button_string": de l’identifiant (string) (button_string) du bouton cliqué de la notification push. Vide si ne provient pas d’un clic de bouton,
  "send_id": (string) ID du message si spécifié pour la campagne (voir Envoyer un identifiant sous Types d’identifiant API),
  "dispatch_id": (string) ID de distribution du message (ID unique pour chaque « transmission » envoyée depuis la plateforme Braze). Les utilisateurs qui reçoivent un message planifié reçoivent le même dispatch_id. Les messages basés sur des actions ou les messages déclenchés par API reçoivent un dispatch_id unique pour chaque utilisateur,
  "ad_id": (string) identifiant publicitaire,
  "ad_id_type": (string) Un parmi 'ios_idfa', 'google_ad_id', 'windows_ad_id' OU 'roku_ad_id',
  "ad_tracking_enabled": (boolean) si le suivi publicitaire est activé pour l’appareil ou non
}
```
#### Détails de la propriété
- Pour `ad_id`, `ad_id_type` et `ad_tracking_enabled`, vous devrez collecter explicitement les IDFA iOS et les ADID Android Google via les SDK natifs. Pour en savoir plus, cliquez ici : [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/optional_idfa_collection/#optional-idfa-collection/), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id).
- Si vous utilisez Kafka pour ingérer des données [Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/) , contactez votre gestionnaire du succès des clients ou votre gestionnaire de compte pour activer la bascule Oui/Non pour l’envoi`ad_id`.
{% endapi %}
{% api %}

## Notifications push dans les événements de foreground (premier plan) iOS

{% apitags %}
Notification push, iOS, envois
{% endapitags %}

Veuillez noter que cet événement n’est pas supporté par notre [SDK Swift](https://github.com/braze-inc/braze-swift-sdk).

Cet événement est maintenant déprécié sur notre [SDK Obj-C](https://github.com/Appboy/appboy-ios-sdk).

```json
// Avant-plan iOS de la notification push : users.messages.pushnotification.IosForeground
{
  "id": (string) ID unique pour cet événement,
  "user_id": (string) ID utilisateur Braze de l’utilisateur,
  "external_user_id": (string) ID externe de l’utilisateur,
  "time": (int) heure en UTC à 10 chiffres de l’événement, en secondes, depuis la période,
  "timezone": (string) fuseau horaire de l’utilisateur au format IANA à l’heure de l’événement,
  "app_id": (string)ID de l’application sur laquelle l’action de l’utilisateur s’est produite,
  "campaign_id": (string) ID de la campagne si provenant d’une campagne,
  "campaign_name": (string) nom de la campagne,
  "message_variation_id": (string) ID de la variation du message si provenant d’une campagne,
  "message_variation_name": (string) le nom de la variation du message si provenant d’une campagne,
  "canvas_id": (string) ID du Canvas s’il provient d’un Canvas,
  "canvas_name": (string) nom du Canvas,
  "canvas_variation_id": (string) ID de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_variation_name": (string) nom de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_step_id": (string) ID de l’étape pour ce message s’il provient d’un Canvas,
  "canvas_step_name": (string) nom de l’étape pour ce message s’il provient d’un Canvas,
  "platform": (string) plateforme de l’appareil (un parmi 'ios', 'android', 'web', 'kindle', 'tvos' OU 'roku'),
  "device_id": (string)ID de l’appareil auquel nous avons essayé de livrer,
  "send_id": (string) ID du message si spécifié pour la campagne (voir Envoyer un identifiant sous Types d’identifiant API),
  "dispatch_id": (string) ID de distribution du message (ID unique pour chaque « transmission » envoyée depuis la plateforme Braze). Les utilisateurs qui reçoivent un message planifié reçoivent le même dispatch_id. Les messages basés sur des actions ou les messages déclenchés par API reçoivent un dispatch_id unique pour chaque utilisateur,
  "ad_id": (string) identifiant publicitaire,
  "ad_id_type": (string) Un parmi 'ios_idfa', 'google_ad_id', 'windows_ad_id' OU 'roku_ad_id',
  "ad_tracking_enabled": (boolean) si le suivi publicitaire est activé pour l’appareil ou non
}
```
#### Détails de la propriété
- Pour `ad_id`, `ad_id_type` et `ad_tracking_enabled`, vous devrez collecter explicitement les IDFA iOS et les ADID Android Google via les SDK natifs. Pour en savoir plus, cliquez ici : [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/optional_idfa_collection/#optional-idfa-collection/), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id).
- Si vous utilisez Kafka pour ingérer des données [Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/) , contactez votre gestionnaire du succès des clients ou votre gestionnaire de compte pour activer la bascule Oui/Non pour l’envoi`ad_id`.
{% endapi %}
{% api %}

## Rebond (bounce) de notifications Push

{% apitags %}
Push, Envois, Rebonds
{% endapitags %}

Cet événement survient lorsqu’une erreur est reçue du service de notification Push d’Apple ou de la messagerie cloud Fire. Cela signifie que le message de notification push a « rebondi » et n’est donc pas arrivé sur l’appareil de l’utilisateur.

```json
// Rejet de la notification push : users.messages.pushnotification.Bounce
{
  "id": (string) ID unique pour cet événement,
  "user_id": (string) ID utilisateur Braze de l’utilisateur,
  "external_user_id": (string) ID externe de l’utilisateur,
  "time": (int) heure en UTC à 10 chiffres de l’événement, en secondes, depuis la période,
  "timezone": (string) fuseau horaire de l’utilisateur au format IANA à l’heure de l’événement,
  "app_id": (string) ID de l’application sur laquelle le renvoi s’est produit,
  "campaign_id": (string) ID de la campagne si provenant d’une campagne,
  "campaign_name": (string) nom de la campagne,
  "message_variation_id": (string) ID de la variation du message si provenant d’une campagne,
  "message_variation_name": (string) le nom de la variation du message si provenant d’une campagne,
  "canvas_id": (string) ID du Canvas s’il provient d’un Canvas,
  "canvas_name": (string) nom du Canvas,
  "canvas_variation_id": (string) ID de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_variation_name": (string) nom de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_step_id": (string) ID de l’étape pour ce message s’il provient d’un Canvas,
  "canvas_step_name": (string) nom de l’étape pour ce message s’il provient d’un Canvas,
  "platform": (string) plateforme de l’appareil (un parmi 'ios', 'android', 'web', 'kindle', 'tvos' OU 'roku'),
  "device_id": (string)ID de l’appareil auquel nous avons essayé de livrer,
  "send_id": (string) ID du message si spécifié pour la campagne (voir Envoyer un identifiant sous Types d’identifiant API),
  "dispatch_id": (string) ID de distribution du message (ID unique pour chaque « transmission » envoyée depuis la plateforme Braze). Les utilisateurs qui reçoivent un message planifié reçoivent le même dispatch_id. Les messages basés sur des actions ou les messages déclenchés par API reçoivent un dispatch_id unique pour chaque utilisateur,
  "ad_id": (string) identifiant publicitaire,
  "ad_id_type": (string) Un parmi 'ios_idfa', 'google_ad_id', 'windows_ad_id' OU 'roku_ad_id',
  "ad_tracking_enabled": (boolean) si le suivi publicitaire est activé pour l’appareil ou non
}
```
#### Détails de la propriété
- Si vous utilisez Kafka pour ingérer des données [Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/) , contactez votre gestionnaire du succès des clients ou votre gestionnaire de compte pour activer la bascule Oui/Non pour l’envoi`ad_id`.
{% endapi %}
{% api %}

## Événements d’envoi d’e-mail

{% apitags %}
E-mail, envoi
{% endapitags %}

Cet événement se produit lorsqu’une demande d’envoi d’e-mail a été transmise avec succès entre Braze et Sendgrid. Mais cela ne signifie pas que l’e-mail est arrivé dans la boîte de réception de l’utilisateur final.

```json
// E-mail envoyé : users.messages.email.Send
{
  // Propriétés spécifiques à l’utilisateur
  "id": (string) ID unique pour cet événement,
  "user_id": (string) ID utilisateur Braze de l’utilisateur,
  "external_user_id": (string) ID externe de l’utilisateur,
  "time": (int) heure en UTC à 10 chiffres de l’événement, en secondes, depuis la période,
  "timezone": (string) fuseau horaire de l’utilisateur au format IANA à l’heure de l’événement,
  // Propriétés de suivi de Campagne/Canvas
  "campaign_id": (string) ID de la campagne si provenant d’une campagne,
  "campaign_name": (string) nom de la campagne,
  "message_variation_id": (string) ID de la variation du message si provenant d’une campagne,
  "message_variation_name": (string) le nom de la variation du message si provenant d’une campagne,
  "canvas_id": (string) ID du Canvas s’il provient d’un Canvas,
  "canvas_name": (string) nom du Canvas,
  "canvas_variation_id": (string) ID de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_variation_name": (string) nom de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_step_id": (string) ID de l’étape pour ce message s’il provient d’un Canvas,
  "canvas_step_name": (string) nom de l’étape pour ce message s’il provient d’un Canvas,
  // Propriétés spécifiques à l’événement
  "send_id": (string) ID du message si spécifié pour la campagne (voir Envoyer un identifiant sous Types d’identifiant API),
  "dispatch_id": (string) ID de distribution du message (ID unique pour chaque « transmission » envoyée depuis la plateforme Braze). Les utilisateurs qui reçoivent un message planifié reçoivent le même dispatch_id. Les messages basés sur des actions ou les messages déclenchés par API reçoivent un dispatch_id unique pour chaque utilisateur,
  "email_address": (string) adresse e-mail pour cet événement,
  "ip_pool": (string) ensemble d’IP utilisé pour l’envoi de messages
}
```
#### Détails de la propriété
- Le comportement pour `dispatch_id` diffère entre Canvas et les campagnes, car Braze traite les étapes Canvas (à l’exception des étapes d’entrée, qui peuvent être programmées) comme des événements déclenchés, même lorsqu’ils sont « programmés ». En savoir plus sur [comportement de dispatch ID]({{site.baseurl}}/help/help_articles/data/dispatch_id/).
{% endapi %}


{% api %}

## Événements de livraison d’e-mail

{% apitags %}
Email, livraison
{% endapitags %}

Cet événement se produit lorsqu’un e-mail envoyé est arrivé dans la boîte de réception des utilisateurs finaux.

```json
// Livraison par e-mail : users.messages.email.Delivery
{
  "id": (string) ID unique pour cet événement,
  "user_id": (string) ID utilisateur Braze de l’utilisateur,
  "external_user_id": (string) ID externe de l’utilisateur,
  "time": (int) heure en UTC à 10 chiffres de l’événement, en secondes, depuis la période,
  "timezone": (string) fuseau horaire de l’utilisateur au format IANA à l’heure de l’événement,
  "campaign_id": (string) ID de la campagne si provenant d’une campagne,
  "campaign_name": (string) nom de la campagne,
  "message_variation_id": (string) ID de la variation du message si provenant d’une campagne,
  "message_variation_name": (string) le nom de la variation du message si provenant d’une campagne,
  "canvas_id": (string) ID du Canvas s’il provient d’un Canvas,
  "canvas_name": (string) nom du Canvas,
  "canvas_variation_id": (string) ID de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_variation_name": (string) nom de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_step_id": (string) ID de l’étape pour ce message s’il provient d’un Canvas,
  "canvas_step_name": (string) nom de l’étape pour ce message s’il provient d’un Canvas,
  "send_id": (string) ID du message si spécifié pour la campagne (voir Envoyer un identifiant sous Types d’identifiant API),
  "dispatch_id": (string) ID de distribution du message (ID unique pour chaque « transmission » envoyée depuis la plateforme Braze). Les utilisateurs qui reçoivent un message planifié reçoivent le même dispatch_id. Les messages basés sur des actions ou les messages déclenchés par API reçoivent un dispatch_id unique pour chaque utilisateur,
  "email_address": (string) adresse e-mail pour cet événement,
  "sending_ip": (string) l’adresse IP depuis laquelle le message a été envoyé (événements de livraison de message, bounce et SoftBounce uniquement. Ne sera affiché dans les événements que si la livraison du message a été effectivement tentée. Pour d’autres types de bounces, l’information pourrait être perdue si le serveur destinataire a déjà accepté l’e-mail et que, après que la connexion est fermée, a décidé qu’il ne pouvait pas livrer l’e-mail),
  "ip_pool": (string) ensemble d’IP utilisé pour l’envoi de messages,
  "esp": (string) fournisseur de services d’e-mail lié à l’événement (Sparkpost ou Sendgrid),
  "from_domain": (string) domaine d’envoi pour l’e-mail
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
// Ouverture E-mail : users.messages.email.Open
{
  "id": (string) ID unique pour cet événement,
  "user_id": (string) ID utilisateur Braze de l’utilisateur,
  "external_user_id": (string) ID externe de l’utilisateur,
  "time": (int) heure en UTC à 10 chiffres de l’événement, en secondes, depuis la période,
  "timezone": (string) fuseau horaire de l’utilisateur au format IANA à l’heure de l’événement,
  "campaign_id": (string) ID de la campagne si provenant d’une campagne,
  "campaign_name": (string) nom de la campagne,
  "message_variation_id": (string) ID de la variation du message si provenant d’une campagne,
  "message_variation_name": (string) le nom de la variation du message si provenant d’une campagne,
  "canvas_id": (string) ID du Canvas s’il provient d’un Canvas,
  "canvas_name": (string) nom du Canvas,
  "canvas_variation_id": (string) ID de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_variation_name": (string) nom de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_step_id": (string) ID de l’étape pour ce message s’il provient d’un Canvas,
  "canvas_step_name": (string) nom de l’étape pour ce message s’il provient d’un Canvas,
  "send_id": (string) ID du message si spécifié pour la campagne (voir Envoyer un identifiant sous Types d’identifiant API),
  "dispatch_id": (string) ID de distribution du message (ID unique pour chaque « transmission » envoyée depuis la plateforme Braze). Les utilisateurs qui reçoivent un message planifié reçoivent le même dispatch_id. Les messages basés sur des actions ou les messages déclenchés par API reçoivent un dispatch_id unique pour chaque utilisateur,
  "email_address": (string) adresse e-mail pour cet événement,
  "ip_pool": (string) ensemble d’IP utilisé pour l’envoi de messages,
  "user_agent": (string) description du système et le navigateur de l’utilisateur pour l’événement,
  "machine_open": (string) Indicateur permettant de savoir si l’e-mail a été ouvert par un processus automatisé, comme la fonction de pré-récupération des e-mails d’Apple ou de Google. Actuellement « true » ou nul, mais une granularité supplémentaire pourrait être ajoutée à l’avenir (p. ex., « Apple » ou « Google » pour indiquer quel processus a récupéré l’e-mail),
  "esp": (string) fournisseur de services d’e-mail lié à l’événement (Sparkpost ou Sendgrid),
  "from_domain": (string) domaine d’envoi pour l’e-mail,
  "is_amp": (boolean) indique s’il s’agit d’un événement AMP
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
// Clic d’e-mail : users.messages.email.Click
{
  "id": (string) ID unique pour cet événement,
  "user_id": (string) ID utilisateur Braze de l’utilisateur,
  "external_user_id": (string) ID externe de l’utilisateur,
  "time": (int) heure en UTC à 10 chiffres de l’événement, en secondes, depuis la période,
  "timezone": (string) fuseau horaire de l’utilisateur au format IANA à l’heure de l’événement,
  "campaign_id": (string) ID de la campagne si provenant d’une campagne,
  "campaign_name": (string) nom de la campagne,
  "message_variation_id": (string) ID de la variation du message si provenant d’une campagne,
  "message_variation_name": (string) le nom de la variation du message si provenant d’une campagne,
  "canvas_id": (string) ID du Canvas s’il provient d’un Canvas,
  "canvas_name": (string) nom du Canvas,
  "canvas_variation_id": (string) ID de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_variation_name": (string) nom de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_step_id": (string) ID de l’étape pour ce message s’il provient d’un Canvas,
  "canvas_step_name": (string) nom de l’étape pour ce message s’il provient d’un Canvas,
  "send_id": (string) ID du message si spécifié pour la campagne (voir Envoyer un identifiant sous Types d’identifiant API),
  "dispatch_id": (string) ID de distribution du message (ID unique pour chaque « transmission » envoyée depuis la plateforme Braze). Inclus uniquement lorsque campaign_id est présent. Les utilisateurs qui reçoivent un message planifié reçoivent le même dispatch_id. Les messages basés sur des actions ou les messages déclenchés par API reçoivent un dispatch_id unique pour chaque utilisateur,
  "email_address": (string) adresse e-mail pour cet événement,
  "url": (string) l’URL qui a été cliquée,
  "ip_pool": (string) ensemble d’IP utilisé pour l’envoi de messages,
  "user_agent": (string) description du système et le navigateur de l’utilisateur pour l’événement,
  "link_id": (string) valeur unique de l’URL générée par Braze ; vide sauf si l’aliasage de lien est activé,
  "link_alias": (string) nom de l’alias défini quand le message a été envoyé ; vide sauf si l’aliasage de lien est activé,
  "esp": (string) fournisseur de services d’e-mail lié à l’événement (Sparkpost ou Sendgrid),
  "from_domain": (string) domaine d’envoi pour l’e-mail,
  "is_amp": (boolean) indique s’il s’agit d’un événement AMP
}
```
#### Détails de la propriété
- Le comportement pour `dispatch_id` diffère entre Canvas et les campagnes, car Braze traite les étapes Canvas (à l’exception des étapes d’entrée, qui peuvent être programmées) comme des événements déclenchés, même lorsqu’ils sont « programmés ». En savoir plus sur [comportement de dispatch ID]({{site.baseurl}}/help/help_articles/data/dispatch_id/).
{% endapi %}

{% api %}

## Événement de rebond d’e-mail

{% apitags %}
E-mail, rebond (bounce)
{% endapitags %}

Cet événement survient lorsqu’un fournisseur de services Internet renvoie un hard bounce. Un hard bounce signifie un échec permanent de la délivrabilité.

```json
// Bounce d’e-mail : users.messages.email.Bounce
{
  "id": (string) ID unique pour cet événement,
  "user_id": (string) ID utilisateur Braze de l’utilisateur,
  "external_user_id": (string) ID externe de l’utilisateur,
  "time": (int) heure en UTC à 10 chiffres de l’événement, en secondes, depuis la période,
  "timezone": (string) fuseau horaire de l’utilisateur au format IANA à l’heure de l’événement,
  "campaign_id": (string) ID de la campagne si provenant d’une campagne,
  "campaign_name": (string) nom de la campagne,
  "message_variation_id": (string) ID de la variation du message si provenant d’une campagne,
  "message_variation_name": (string) le nom de la variation du message si provenant d’une campagne,
  "canvas_id": (string) ID du Canvas s’il provient d’un Canvas,
  "canvas_name": (string) nom du Canvas,
  "canvas_variation_id": (string) ID de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_variation_name": (string) nom de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_step_id": (string) ID de l’étape pour ce message s’il provient d’un Canvas,
  "canvas_step_name": (string) nom de l’étape pour ce message s’il provient d’un Canvas,
  "send_id": (string) ID du message si spécifié pour la campagne (voir Envoyer un identifiant sous Types d’identifiant API),
  "dispatch_id": (string) ID de distribution du message (ID unique pour chaque « transmission » envoyée depuis la plateforme Braze). Les utilisateurs qui reçoivent un message planifié reçoivent le même dispatch_id. Les messages basés sur des actions ou les messages déclenchés par API reçoivent un dispatch_id unique pour chaque utilisateur,
  "email_address": (string) adresse e-mail pour cet événement,
  "sending_ip": (string) l’adresse IP depuis laquelle le message a été envoyé (événements de livraison de message, bounce et SoftBounce uniquement. Ne sera affiché dans les événements que si la livraison du message a été effectivement tentée. Pour d’autres types de bounces, l’information pourrait être perdue si le serveur destinataire a déjà accepté l’e-mail et que, après que la connexion est fermée, a décidé qu’il ne pouvait pas livrer l’e-mail),
  "ip_pool": (string) ensemble d’IP utilisé pour l’envoi de message (pour certains cas de bounce, l’ensemble d’IP ne sera pas fourni),
  "bounce_reason": (string) raison fournie par le serveur pour le bounce,
  "esp": (string) fournisseur de services d’e-mail lié à l’événement (Sparkpost ou Sendgrid),
  "from_domain": (string) domaine d’envoi pour l’e-mail,
  "is_drop": (boolean) indique si cet événement est décompté comme un événement d’abandon
}
```
#### Détails de la propriété
- Le comportement pour `dispatch_id` diffère entre Canvas et les campagnes, car Braze traite les étapes Canvas (à l’exception des étapes d’entrée, qui peuvent être programmées) comme des événements déclenchés, même lorsqu’ils sont « programmés ». En savoir plus sur [comportement de dispatch ID]({{site.baseurl}}/help/help_articles/data/dispatch_id/).
{% endapi %}

{% api %}

## Événement de « soft bounce » d’e-mail

{% apitags %}
E-mail, rebond (bounce)
{% endapitags %}

Cet événement se produit lorsqu’un fournisseur de services Internet renvoie un soft bounce. Un soft bounce signifie qu’un e-mail n’a pas pu être livré en raison d’une défaillance temporaire de la délivrabilité.

```json
// Soft bounce d’e-mail : users.messages.email.SoftBounce
{
  "id": (string) ID unique pour cet événement,
  "user_id": (string) ID utilisateur Braze de l’utilisateur,
  "external_user_id": (string) ID externe de l’utilisateur,
  "time": (int) heure en UTC à 10 chiffres de l’événement, en secondes, depuis la période,
  "timezone": (string) fuseau horaire de l’utilisateur au format IANA à l’heure de l’événement,
  "campaign_id": (string) ID de la campagne si provenant d’une campagne,
  "campaign_name": (string) nom de la campagne,
  "message_variation_id": (string) ID de la variation du message si provenant d’une campagne,
  "message_variation_name": (string) le nom de la variation du message si provenant d’une campagne,
  "canvas_id": (string) ID du Canvas s’il provient d’un Canvas,
  "canvas_name": (string) nom du Canvas,
  "canvas_variation_id": (string) ID de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_variation_name": (string) nom de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_step_id": (string) ID de l’étape pour ce message s’il provient d’un Canvas,
  "canvas_step_name": (string) nom de l’étape pour ce message s’il provient d’un Canvas,
  "send_id": (string) ID du message si spécifié pour la campagne (voir Envoyer un identifiant sous Types d’identifiant API),
  "dispatch_id": (string) ID de distribution du message (ID unique pour chaque « transmission » envoyée depuis la plateforme Braze). Les utilisateurs qui reçoivent un message planifié reçoivent le même dispatch_id. Les messages basés sur des actions ou les messages déclenchés par API reçoivent un dispatch_id unique pour chaque utilisateur,
  "email_address": (string) adresse e-mail pour cet événement,
  "sending_ip": (string) l’adresse IP depuis laquelle le message a été envoyé (événements de livraison de message, bounce et SoftBounce uniquement. Ne sera affiché dans les événements que si la livraison du message a été effectivement tentée. Pour d’autres types de bounces, l’information pourrait être perdue si le serveur destinataire a déjà accepté l’e-mail et que, après que la connexion est fermée, a décidé qu’il ne pouvait pas livrer l’e-mail),
  "ip_pool": (string) ensemble d’IP utilisé pour l’envoi de message (pour certains cas de bounce, l’ensemble d’IP ne sera pas fourni),
  "bounce_reason": (string) raison fournie par le serveur pour le bounce,
  "esp": (string) fournisseur de services d’e-mail lié à l’événement (Sparkpost ou Sendgrid),
  "from_domain": (string) domaine d’envoi pour l’e-mail
}
```
#### Détails de la propriété
- Le comportement pour `dispatch_id` diffère entre Canvas et les campagnes, car Braze traite les étapes Canvas (à l’exception des étapes d’entrée, qui peuvent être programmées) comme des événements déclenchés, même lorsqu’ils sont « programmés ». En savoir plus sur [comportement de dispatch ID]({{site.baseurl}}/help/help_articles/data/dispatch_id/).
{% endapi %}

{% api %}

## Événements de spam pour un e-mail

{% apitags %}
Email, Spam
{% endapitags %}

Cet événement se produit lorsque l’utilisateur final clique sur le bouton « spam » sur l’e-mail. Notez que cela ne représente pas le fait que l’e-mail soit allé dans le dossier Spam, car Braze ne suit pas ça.

```json
// E-mail indiqué comme étant un courrier indésirable : users.messages.email.MarkAsSpam
{
  "id": (string) ID unique pour cet événement,
  "user_id": (string) ID utilisateur Braze de l’utilisateur,
  "external_user_id": (string) ID externe de l’utilisateur,
  "time": (int) heure en UTC à 10 chiffres de l’événement, en secondes, depuis la période,
  "timezone": (string) fuseau horaire de l’utilisateur au format IANA à l’heure de l’événement,
  "campaign_id": (string) ID de la campagne si provenant d’une campagne,
  "campaign_name": (string) nom de la campagne,
  "message_variation_id": (string) ID de la variation du message si provenant d’une campagne,
  "message_variation_name": (string) le nom de la variation du message si provenant d’une campagne,
  "canvas_id": (string) ID du Canvas s’il provient d’un Canvas,
  "canvas_name": (string) nom du Canvas,
  "canvas_variation_id": (string) ID de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_variation_name": (string) nom de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_step_id": (string) ID de l’étape pour ce message s’il provient d’un Canvas,
  "canvas_step_name": (string) nom de l’étape pour ce message s’il provient d’un Canvas,
  "send_id": (string) ID du message si spécifié pour la campagne (voir Envoyer un identifiant sous Types d’identifiant API),
  "dispatch_id": (string) ID de distribution du message (ID unique pour chaque « transmission » envoyée depuis la plateforme Braze). Les utilisateurs qui reçoivent un message planifié reçoivent le même dispatch_id. Les messages basés sur des actions ou les messages déclenchés par API reçoivent un dispatch_id unique pour chaque utilisateur,
  "email_address": (string) adresse e-mail pour cet événement,
  "ip_pool": (string) ensemble d’IP utilisé pour l’envoi de messages,
  "user_agent": (string) Ce champ n’est plus utilisé pour les destinations de cet événement et sera toujours vide,
  "esp": (string) fournisseur de services d’e-mail lié à l’événement (Sparkpost ou Sendgrid),
  "from_domain": (string) domaine d’envoi pour l’e-mail
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
L’événement `désabonné` est en fait un événement de clic spécialisé qui se lance quand votre utilisateur clique sur le lien de désabonnement de l’e-mail (qu’il s’agisse d’un lien de désinscription au sein du corps ou du pied de page de l’e-mail ou en utilisant l’[en-tête de désinscription de la liste]({{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/email_settings#include-a-list-unsubscribe-header)), pas le moment où l’état de l’utilisateur passe à « désabonné ». Si le changement de statut d’abonnement est envoyé via l’API, il ne déclenchera pas d’événement sur Currents.
{% endalert %}

```json
// Désabonnement par e-mail : users.messages.email.Unsubscribe
{
  "id": (string) ID unique pour cet événement,
  "user_id": (string) ID utilisateur Braze de l’utilisateur,
  "external_user_id": (string) ID externe de l’utilisateur,
  "time": (int) heure en UTC à 10 chiffres de l’événement, en secondes, depuis la période,
  "timezone": (string) fuseau horaire de l’utilisateur au format IANA à l’heure de l’événement,
  "campaign_id": (string) ID de la campagne si provenant d’une campagne,
  "campaign_name": (string) nom de la campagne,
  "message_variation_id": (string) ID de la variation du message si provenant d’une campagne,
  "message_variation_name": (string) le nom de la variation du message si provenant d’une campagne,
  "canvas_id": (string) ID du Canvas s’il provient d’un Canvas,
  "canvas_name": (string) nom du Canvas,
  "canvas_variation_id": (string) ID de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_variation_name": (string) nom de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_step_id": (string) ID de l’étape pour ce message s’il provient d’un Canvas,
  "canvas_step_name": (string) nom de l’étape pour ce message s’il provient d’un Canvas,
  "send_id": (string) ID du message si spécifié pour la campagne (voir Envoyer un identifiant sous Types d’identifiant API),
  "dispatch_id": (string) ID de distribution du message (ID unique pour chaque « transmission » envoyée depuis la plateforme Braze). Les utilisateurs qui reçoivent un message planifié reçoivent le même dispatch_id. Les messages basés sur des actions ou les messages déclenchés par API reçoivent un dispatch_id unique pour chaque utilisateur,
  "email_address": (string) adresse e-mail pour cet événement,
  "ip_pool": (string) ensemble d’IP utilisé pour l’envoi de messages
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
// Changement de l’état du groupe d’abonnement : users.behaviors.subscriptiongroup.StateChange
{
  "id": (string) ID unique pour cet événement,
  "user_id": (string) ID utilisateur Braze de l’utilisateur,
  "external_user_id": (string) ID externe de l’utilisateur,
  "channel": (string) « sms », « e-mail » ou « whats_app »,
  "time": (int) heure en UTC à 10 chiffres de l’événement, en secondes, depuis la période,
  "timezone": (string) fuseau horaire de l’utilisateur au format IANA à l’heure de l’événement,
  "app_id": (string)ID de l’application sur laquelle l’action de l’utilisateur s’est produite,
  "campaign_id": (string) ID de la campagne si provenant d’une campagne,
  "campaign_name": (string) nom de la campagne,
  "message_variation_id": (string) ID de la variation du message si provenant d’une campagne,
  "message_variation_name": (string) le nom de la variation du message si provenant d’une campagne,
  "canvas_id": (string) ID du Canvas s’il provient d’un Canvas,
  "canvas_name": (string) nom du Canvas,
  "canvas_variation_id": (string) ID de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_variation_name": (string) nom de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_step_id": (string) ID de l’étape pour ce message s’il provient d’un Canvas,
  "canvas_step_name": (string) nom de l’étape pour ce message s’il provient d’un Canvas,
  "send_id": (string) ID du message si spécifié pour la campagne (voir Envoyer un identifiant sous Types d’identifiant API),
  "email_address": (string) adresse e-mail pour cet utilisateur,
  "phone_number": (string) numéro de téléphone de l’utilisateur (affiché au format e.164),
  "subscription_group_id": (string) ID du groupe d’abonnement,
  "subscription_status": (string) statut de l’abonnement après le changement : 'Abonné' ou 'Désabonné'
}
```
{% endapi %}


{% api %}

## Événements d’impression de messages dans l’application

{% apitags %}
Messages In-App, Impressions
{% endapitags %}

Cet événement se produit lorsqu’un utilisateur visualise un message in-app.

```json
// Impression de message in-app : users.messages.inappmessage.Impression
{
  "id": (string) ID unique pour cet événement,
  "user_id": (string) ID utilisateur Braze de l’utilisateur,
  "external_user_id": (string) ID externe de l’utilisateur,
  "time": (int) heure en UTC à 10 chiffres de l’événement, en secondes, depuis la période,
  "timezone": (string) fuseau horaire de l’utilisateur au format IANA à l’heure de l’événement,
  "campaign_id": (string) ID de la campagne si provenant d’une campagne,
  "campaign_name": (string) nom de la campagne,
  "message_variation_id": (string) ID de la variation du message si provenant d’une campagne,
  "message_variation_name": (string) le nom de la variation du message si provenant d’une campagne,
  "canvas_id": (string) ID du Canvas s’il provient d’un Canvas,
  "canvas_name": (string) nom du Canvas,
  "canvas_variation_id": (string) ID de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_variation_name": (string) nom de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_step_id": (string) ID de l’étape pour ce message s’il provient d’un Canvas,
  "canvas_step_name": (string) nom de l’étape pour ce message s’il provient d’un Canvas,
  "card_id": (string) obsolète,
  "send_id": (string) ID du message si spécifié pour la campagne (voir Envoyer un identifiant sous Types d’identifiant API),
  "app_id": (string)ID de l’application sur laquelle l’action de l’utilisateur s’est produite,
  "platform": (string) plateforme de l’appareil (un parmi 'ios', 'android', 'web', 'kindle', 'tvos' OU 'roku'),
  "os_version": (string) version du système d’exploitation de l’appareil utilisé pour l’action,
  "device_model": (string) modèle matériel de l’appareil,
  "device_id": (string) ID de l’appareil sur lequel l’événement s’est produit,
  "ad_id": (string) identifiant publicitaire,
  "ad_id_type": (string) Un parmi 'ios_idfa', 'google_ad_id', 'windows_ad_id' OU 'roku_ad_id',
  "ad_tracking_enabled": (boolean) si le suivi publicitaire est activé pour l’appareil ou non
}
```
#### Détails de la propriété
- Pour `ad_id`, `ad_id_type` et `ad_tracking_enabled`, vous devrez collecter explicitement les IDFA iOS et les ADID Android Google via les SDK natifs. Pour en savoir plus, cliquez ici : [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/optional_idfa_collection/#optional-idfa-collection/), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id).
- Si vous utilisez Kafka pour ingérer des données [Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/) , contactez votre gestionnaire du succès des clients ou votre gestionnaire de compte pour activer la bascule Oui/Non pour l’envoi`ad_id`.
{% endapi %}

{% api %}

## Événements de clics sur Message In-App

{% apitags %}
Messages in-app , clics
{% endapitags %}

Cet événement se produit lorsqu’un utilisateur clique sur un message in-app.

```json
// Clic sur le message in-app : users.messages.inappmessage.Click
{
  "id": (string) ID unique pour cet événement,
  "user_id": (string) ID utilisateur Braze de l’utilisateur,
  "external_user_id": (string) ID externe de l’utilisateur,
  "time": (int) heure en UTC à 10 chiffres de l’événement, en secondes, depuis la période,
  "timezone": (string) fuseau horaire de l’utilisateur au format IANA à l’heure de l’événement,
  "button_id": (string) index du bouton cliqué, s’il s’agit d’un bouton cliqué, ou ID de suivi du clic, si l’événement provient d’un appel appboyBridge.logClick,
  "campaign_id": (string) ID de la campagne si provenant d’une campagne,
  "campaign_name": (string) nom de la campagne,
  "message_variation_id": (string) ID de la variation du message si provenant d’une campagne,
  "message_variation_name": (string) le nom de la variation du message si provenant d’une campagne,
  "canvas_id": (string) ID du Canvas s’il provient d’un Canvas,
  "canvas_name": (string) nom du Canvas,
  "canvas_variation_id": (string) ID de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_variation_name": (string) nom de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_step_id": (string) ID de l’étape pour ce message s’il provient d’un Canvas,
  "canvas_step_name": (string) nom de l’étape pour ce message s’il provient d’un Canvas,
  "card_id": (string) obsolète,
  "send_id": (string) ID du message si spécifié pour la campagne (voir Envoyer un identifiant sous Types d’identifiant API),
  "app_id": (string)ID de l’application sur laquelle l’action de l’utilisateur s’est produite,
  "platform": (string) plateforme de l’appareil (un parmi 'ios', 'android', 'web', 'kindle', 'tvos' OU 'roku'),
  "os_version": (string) version du système d’exploitation de l’appareil utilisé pour l’action,
  "device_model": (string) modèle matériel de l’appareil,
  "device_id": (string) ID de l’appareil sur lequel l’événement s’est produit,
  "ad_id": (string) identifiant publicitaire,
  "ad_id_type": (string) Un parmi 'ios_idfa', 'google_ad_id', 'windows_ad_id' OU 'roku_ad_id',
  "ad_tracking_enabled": (boolean) si le suivi publicitaire est activé pour l’appareil ou non
}
```
#### Détails de la propriété
- Pour `ad_id`, `ad_id_type` et `ad_tracking_enabled`, vous devrez collecter explicitement les IDFA iOS et les ADID Android Google via les SDK natifs. Pour en savoir plus, cliquez ici : [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/optional_idfa_collection/#optional-idfa-collection/), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id).
- Si vous utilisez Kafka pour ingérer des données [Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/) , contactez votre gestionnaire du succès des clients ou votre gestionnaire de compte pour activer la bascule Oui/Non pour l’envoi`ad_id`.
{% endapi %}


{% api %}

## Événements d’envoi de webhook

{% apitags %}
Webhooks, Sends
{% endapitags %}

Cet événement se produit lorsqu’un webhook a été traité et envoyé à la tierce partie spécifiée dans le webhook. Notez que cela n’indique pas si la demande a été reçue ou non.

```json
// Envoi de webhook : users.messages.webhook.Send
{
  "id": (string) ID unique pour cet événement,
  "user_id": (string) ID utilisateur Braze de l’utilisateur,
  "external_user_id": (string) ID externe de l’utilisateur,
  "time": (int) heure en UTC à 10 chiffres de l’événement, en secondes, depuis la période,
  "timezone": (string) fuseau horaire de l’utilisateur au format IANA à l’heure de l’événement,
  "campaign_id": (string) ID de la campagne si provenant d’une campagne,
  "campaign_name": (string) nom de la campagne,
  "message_variation_id": (string) ID de la variation du message si provenant d’une campagne,
  "message_variation_name": (string) le nom de la variation du message si provenant d’une campagne,
  "canvas_id": (string) ID du Canvas s’il provient d’un Canvas,
  "canvas_name": (string) nom du Canvas,
  "canvas_variation_id": (string) ID de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_variation_name": (string) nom de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_step_id": (string) ID de l’étape pour ce message s’il provient d’un Canvas,
  "canvas_step_name": (string) nom de l’étape pour ce message s’il provient d’un Canvas,
  "send_id": (string) ID du message si spécifié pour la campagne (voir Envoyer un identifiant sous Types d’identifiant API)
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
// Envoi de carte de contenu : users.messages.contentcard.Send
{
  "id": (string) ID unique pour cet événement,
  "user_id": (string) ID utilisateur Braze de l’utilisateur,
  "external_user_id": (string) ID externe de l’utilisateur,
  "time": (int) heure en UTC à 10 chiffres de l’événement, en secondes, depuis la période,
  "timezone": (string) fuseau horaire de l’utilisateur au format IANA à l’heure de l’événement,
  "content_card_id": (string) ID de la carte de contenu qui a été envoyée,
  "campaign_id": (string) ID de la campagne si provenant d’une campagne,
  "campaign_name": (string) nom de la campagne,
  "message_variation_id": (string) ID de la variation du message si provenant d’une campagne,
  "message_variation_name": (string) le nom de la variation du message si provenant d’une campagne,
  "canvas_id": (string) ID du Canvas s’il provient d’un Canvas,
  "canvas_name": (string) nom du Canvas,
  "canvas_variation_id": (string) ID de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_variation_name": (string) nom de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_step_id": (string) ID de l’étape pour ce message s’il provient d’un Canvas,
  "canvas_step_name": (string) nom de l’étape pour ce message s’il provient d’un Canvas,
  "send_id": (string) ID du message si spécifié pour la campagne (voir Envoyer un identifiant sous Types d’identifiant API),
  "device_id": (string)ID de l’appareil sur lequel l’événement s’est produit
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
// Impression de carte de contenu : users.messages.contentcard.Impression
{
  "id": (string) ID unique pour cet événement,
  "user_id": (string) ID utilisateur Braze de l’utilisateur,
  "external_user_id": (string) ID externe de l’utilisateur,
  "time": (int) heure en UTC à 10 chiffres de l’événement, en secondes, depuis la période,
  "timezone": (string) fuseau horaire de l’utilisateur au format IANA à l’heure de l’événement,
  "app_id": (string)ID de l’application sur laquelle l’action de l’utilisateur s’est produite,
  "content_card_id": (string) ID de la carte de contenu qui a été visualisée/clicked/dismissed,
  "campaign_id": (string) ID de la campagne si provenant d’une campagne,
  "campaign_name": (string) nom de la campagne,
  "message_variation_id": (string) ID de la variation du message si provenant d’une campagne,
  "message_variation_name": (string) le nom de la variation du message si provenant d’une campagne,
  "canvas_id": (string) ID du Canvas s’il provient d’un Canvas,
  "canvas_name": (string) nom du Canvas,
  "canvas_variation_id": (string) ID de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_variation_name": (string) nom de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_step_id": (string) ID de l’étape pour ce message s’il provient d’un Canvas,
  "canvas_step_name": (string) nom de l’étape pour ce message s’il provient d’un Canvas,
  "send_id": (string) ID du message si spécifié pour la campagne (voir Envoyer un identifiant sous Types d’identifiant API),
  "platform": (string) plateforme de l’appareil (un parmi 'ios', 'android', 'web', 'kindle', 'tvos' OU 'roku'),
  "os_version": (string) version du système d’exploitation de l’appareil utilisé pour l’action,
  "device_model": (string) modèle matériel de l’appareil,
  "device_id": (string) ID de l’appareil sur lequel l’événement s’est produit,
  "ad_id": (string) identifiant publicitaire,
  "ad_id_type": (string) Un parmi 'ios_idfa', 'google_ad_id', 'windows_ad_id' OU 'roku_ad_id',
  "ad_tracking_enabled": (boolean) si le suivi publicitaire est activé pour l’appareil ou non
}
```
#### Détails de la propriété
- Pour `ad_id`, `ad_id_type` et `ad_tracking_enabled`, vous devrez collecter explicitement les IDFA iOS et les adid Android Google via les SDK natifs. Pour en savoir plus, cliquez ici : [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/optional_idfa_collection/#optional-idfa-collection/), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id).
- Si vous utilisez Kafka pour ingérer des données [Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/) , contactez votre gestionnaire du succès des clients ou votre gestionnaire de compte pour activer la bascule Oui/Non pour l’envoi`ad_id`.
{% endapi %}

{% api %}
## Événements de clic sur carte de contenu

{% apitags %}
Cartes de contenu, clics
{% endapitags %}

Cet événement se produit lorsqu’un utilisateur clique sur une carte de contenu.

```json
// Clic de carte de contenu : users.messages.contentcard.Click
{
  "id": (string) ID unique pour cet événement,
  "user_id": (string) ID utilisateur Braze de l’utilisateur,
  "external_user_id": (string) ID externe de l’utilisateur,
  "time": (int) heure en UTC à 10 chiffres de l’événement, en secondes, depuis la période,
  "timezone": (string) fuseau horaire de l’utilisateur au format IANA à l’heure de l’événement,
  "app_id": (string)ID de l’application sur laquelle l’action de l’utilisateur s’est produite,
  "content_card_id": (string) ID de la carte de contenu qui a été visualisée/clicked/dismissed,
  "campaign_id": (string) ID de la campagne si provenant d’une campagne,
  "campaign_name": (string) nom de la campagne,
  "message_variation_id": (string) ID de la variation du message si provenant d’une campagne,
  "message_variation_name": (string) le nom de la variation du message si provenant d’une campagne,
  "canvas_id": (string) ID du Canvas s’il provient d’un Canvas,
  "canvas_name": (string) nom du Canvas,
  "canvas_variation_id": (string) ID de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_variation_name": (string) nom de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_step_id": (string) ID de l’étape pour ce message s’il provient d’un Canvas,
  "canvas_step_name": (string) nom de l’étape pour ce message s’il provient d’un Canvas,
  "send_id": (string) ID du message si spécifié pour la campagne (voir Envoyer un identifiant sous Types d’identifiant API),
  "platform": (string) plateforme de l’appareil (un parmi 'ios', 'android', 'web', 'kindle', 'tvos' OU 'roku'),
  "os_version": (string) version du système d’exploitation de l’appareil utilisé pour l’action,
  "device_model": (string) modèle matériel de l’appareil,
  "device_id": (string) ID de l’appareil sur lequel l’événement s’est produit,
  "ad_id": (string) identifiant publicitaire,
  "ad_id_type": (string) Un parmi 'ios_idfa', 'google_ad_id', 'windows_ad_id' OU 'roku_ad_id',
  "ad_tracking_enabled": (boolean) si le suivi publicitaire est activé pour l’appareil ou non
}
```
#### Détails de la propriété
- Pour `ad_id`, `ad_id_type` et `ad_tracking_enabled`, vous devrez collecter explicitement les idfa iOS et les adid Android Google via les SDK natifs. Pour en savoir plus, cliquez ici : [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/optional_idfa_collection/#optional-idfa-collection/), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id).
- Si vous utilisez Kafka pour ingérer des données [Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/) , contactez votre gestionnaire du succès des clients ou votre gestionnaire de compte pour activer la bascule Oui/Non pour l’envoi`ad_id`.
{% endapi %}


{% api %}
## Événements de fermeture de carte de contenu

{% apitags %}
Cartes de contenu, rejet
{% endapitags %}

Cet événement se produit lorsqu’un utilisateur rejette une carte de contenu.

```json
// Rejet d’une carte de contenu : users.messages.contentcard.Dismiss
{
  "id": (string) ID unique pour cet événement,
  "user_id": (string) ID utilisateur Braze de l’utilisateur,
  "external_user_id": (string) ID externe de l’utilisateur,
  "time": (int) heure en UTC à 10 chiffres de l’événement, en secondes, depuis la période,
  "timezone": (string) fuseau horaire de l’utilisateur au format IANA à l’heure de l’événement,
  "app_id": (string)ID de l’application sur laquelle l’action de l’utilisateur s’est produite,
  "content_card_id": (string) ID de la carte de contenu qui a été visualisée/clicked/dismissed,
  "campaign_id": (string) ID de la campagne si provenant d’une campagne,
  "campaign_name": (string) nom de la campagne,
  "message_variation_id": (string) ID de la variation du message si provenant d’une campagne,
  "message_variation_name": (string) le nom de la variation du message si provenant d’une campagne,
  "canvas_id": (string) ID du Canvas s’il provient d’un Canvas,
  "canvas_name": (string) nom du Canvas,
  "canvas_variation_id": (string) ID de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_variation_name": (string) nom de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_step_id": (string) ID de l’étape pour ce message s’il provient d’un Canvas,
  "canvas_step_name": (string) nom de l’étape pour ce message s’il provient d’un Canvas,
  "send_id": (string) ID du message si spécifié pour la campagne (voir Envoyer un identifiant sous Types d’identifiant API),
  "platform": (string) plateforme de l’appareil (un parmi 'ios', 'android', 'web', 'kindle', 'tvos' OU 'roku'),
  "os_version": (string) version du système d’exploitation de l’appareil utilisé pour l’action,
  "device_model": (string) modèle matériel de l’appareil,
  "device_id": (string) ID de l’appareil sur lequel l’événement s’est produit,
  "ad_id": (string) identifiant publicitaire,
  "ad_id_type": (string) Un parmi 'ios_idfa', 'google_ad_id', 'windows_ad_id' OU 'roku_ad_id',
  "ad_tracking_enabled": (boolean) si le suivi publicitaire est activé pour l’appareil ou non
}
```
#### Détails de la propriété
- Pour `ad_id`, `ad_id_type` et `ad_tracking_enabled`, vous devrez collecter explicitement les idfa iOS et les adid Android Google via les SDK natifs. Pour en savoir plus, cliquez ici : [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/optional_idfa_collection/#optional-idfa-collection/), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id).
- Si vous utilisez Kafka pour ingérer des données [Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/) , contactez votre gestionnaire du succès des clients ou votre gestionnaire de compte pour activer la bascule Oui/Non pour l’envoi`ad_id`.
{% endapi %}

{% api %}

## Événement d’impression du Fil d'actualité

{% alert note %}
Les fils d’actualités deviennent obsolètes. Braze recommande aux clients qui utilisent notre outil de fil d’actualités de passer à notre canal de communication de cartes de contenu - il est plus flexible, plus personnalisable et plus fiable. Consultez le [guide de migration]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/) pour en savoir plus.
{% endalert %}

{% apitags %}
Fil d'actualité, Impressions
{% endapitags %}

Cet événement se produit lorsqu’un utilisateur regarde le fil d’actualités.

{% alert tip %}
Le schéma [Impression du Fil d'actualité]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/customer_behavior_events/#news-feed-impression-event) (`users.behaviors.app.NewsFeedImpression`) se trouve dans le glossaire des événements de comportement client, car ces données n’ont pas été classées comme événement d’engagement sur message. 
{% endalert %}

```json
// Impression de carte de fil d’actualité : users.messages.newsfeedcard.Impression
{
  "id": (string) ID unique pour cet événement,
  "user_id": (string) ID utilisateur Braze de l’utilisateur,
  "external_user_id": (string) ID externe de l’utilisateur,
  "time": (int) heure en UTC à 10 chiffres de l’événement, en secondes, depuis la période,
  "timezone": (string) fuseau horaire de l’utilisateur au format IANA à l’heure de l’événement,
  "card_id": (string) ID de la carte qui a été visualisée,
  "app_id": (string)ID de l’application sur laquelle l’action de l’utilisateur s’est produite,
  "platform": (string) plateforme de l’appareil (un parmi 'ios', 'android', 'web', 'kindle', 'tvos' OU 'roku'),
  "os_version": (string) version du système d’exploitation de l’appareil utilisé pour l’action,
  "device_model": (string) modèle matériel de l’appareil,
  "device_id": (string)ID de l’appareil sur lequel l’événement s’est produit
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
// Clic de carte de fil d’actualité : users.messages.newsfeedcard.Click
{
  "id": (string) ID unique pour cet événement,
  "user_id": (string) ID utilisateur Braze de l’utilisateur,
  "external_user_id": (string) ID externe de l’utilisateur,
  "time": (int) heure en UTC à 10 chiffres de l’événement, en secondes, depuis la période,
  "timezone": (string) fuseau horaire de l’utilisateur au format IANA à l’heure de l’événement,
  "card_id": (string) ID de la carte qui a été cliquée,
  "app_id": (string)ID de l’application sur laquelle l’action de l’utilisateur s’est produite,
  "platform": (string) plateforme de l’appareil (un parmi 'ios', 'android', 'web', 'kindle', 'tvos' OU 'roku'),
  "os_version": (string) version du système d’exploitation de l’appareil utilisé pour l’action,
  "device_model": (string) modèle matériel de l’appareil,
  "device_id": (string)ID de l’appareil sur lequel l’événement s’est produit
}
```
{% endapi %}

{% api %}

## Événements d’envoi SMS

{% apitags %}
SMS, envoi
{% endapitags %}

Cet événement se produit lorsqu’un utilisateur envoie un SMS.

```json
// Envoi de SMS : users.messages.sms.Send
{
  "id": (string) ID unique pour cet événement,
  "user_id": (string) ID utilisateur Braze de l’utilisateur,
  "external_user_id": (string) ID externe de l’utilisateur,
  "time": (int) heure en UTC à 10 chiffres de l’événement, en secondes, depuis la période,
  "timezone": (string) fuseau horaire de l’utilisateur au format IANA à l’heure de l’événement,
  "from_phone_number": (string) le numéro de téléphone de l’expéditeur du message (remis et non remis uniquement),
  "subscription_group_id": (string) ID du groupe d’abonnement ciblé pour ce message SMS,
  "to_phone_number": (string) le numéro auquel le message a été envoyé,
  "campaign_id": (string) ID de la campagne si provenant d’une campagne,
  "campaign_name": (string) nom de la campagne,
  "message_variation_id": (string) ID de la variation du message si provenant d’une campagne,
  "message_variation_name": (string) le nom de la variation du message si provenant d’une campagne,
  "canvas_id": (string) ID du Canvas s’il provient d’un Canvas,
  "canvas_name": (string) nom du Canvas,
  "canvas_variation_id": (string) ID de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_variation_name": (string) nom de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_step_id": (string) ID de l’étape pour ce message s’il provient d’un Canvas,
  "canvas_step_name": (string) nom de l’étape pour ce message s’il provient d’un Canvas,
  "dispatch_id": (string) ID de l’envoi du message (id unique pour chaque « transmission » envoyée depuis la plateforme Braze et les utilisateurs qui reçoivent un message programmé obtiennent le même dispatch_id. Les messages basés sur des actions ou les messages déclenchés par API reçoivent un dispatch_id unique pour chaque utilisateur
  "send_id": (string) ID d’envoi de message auquel appartient ce message,
  "category" : (string) Si le SMS a été envoyé à la suite d’une réponse automatique à un de vos mots-clés SMS globaux, la catégorie sera affichée ici (e.g Abonné, Désabonné, Aide) 
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
// Livraison SMS : users.messages.sms.CarrierSend
{
  "id": (string) ID unique pour cet événement,
  "user_id": (string) ID utilisateur Braze de l’utilisateur,
  "external_user_id": (string) ID externe de l’utilisateur,
  "time": (int) heure en UTC à 10 chiffres de l’événement, en secondes, depuis la période,
  "timezone": (string) fuseau horaire de l’utilisateur au format IANA à l’heure de l’événement,
  "from_phone_number": (string) le numéro de téléphone de l’expéditeur du message (remis et non remis uniquement),
  "subscription_group_id": (string) ID du groupe d’abonnement ciblé pour ce message SMS,
  "to_phone_number": (string) le numéro auquel le message a été envoyé,
  "campaign_id": (string) ID de la campagne si provenant d’une campagne,
  "campaign_name": (string) nom de la campagne,
  "message_variation_id": (string) ID de la variation du message si provenant d’une campagne,
  "message_variation_name": (string) le nom de la variation du message si provenant d’une campagne,
  "canvas_id": (string) ID du Canvas s’il provient d’un Canvas,
  "canvas_name": (string) nom du Canvas,
  "canvas_variation_id": (string) ID de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_variation_name": (string) nom de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_step_id": (string) ID de l’étape pour ce message s’il provient d’un Canvas,
  "canvas_step_name": (string) nom de l’étape pour ce message s’il provient d’un Canvas,
  "dispatch_id": (string) ID de l’envoi du message (id unique pour chaque « transmission » envoyée depuis la plateforme Braze et les utilisateurs qui reçoivent un message programmé obtiennent le même dispatch_id. Les messages basés sur des actions ou les messages déclenchés par API reçoivent un dispatch_id unique pour chaque utilisateur,
  "send_id": (string) ID d’envoi de message auquel appartient ce message
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
// Livraison SMS : users.messages.sms.Delivery
{
  "id": (string) ID unique pour cet événement,
  "user_id": (string) ID utilisateur Braze de l’utilisateur,
  "external_user_id": (string) ID externe de l’utilisateur,
  "time": (int) heure en UTC à 10 chiffres de l’événement, en secondes, depuis la période,
  "timezone": (string) fuseau horaire de l’utilisateur au format IANA à l’heure de l’événement,
  "from_phone_number": (string) le numéro de téléphone de l’expéditeur du message (remis et non remis uniquement),
  "subscription_group_id": (string) ID du groupe d’abonnement ciblé pour ce message SMS,
  "to_phone_number": (string) le numéro auquel le message a été envoyé,
  "campaign_id": (string) ID de la campagne si provenant d’une campagne,
  "campaign_name": (string) nom de la campagne,
  "message_variation_id": (string) ID de la variation du message si provenant d’une campagne,
  "message_variation_name": (string) le nom de la variation du message si provenant d’une campagne,
  "canvas_id": (string) ID du Canvas s’il provient d’un Canvas,
  "canvas_name": (string) nom du Canvas,
  "canvas_variation_id": (string) ID de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_variation_name": (string) nom de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_step_id": (string) ID de l’étape pour ce message s’il provient d’un Canvas,
  "canvas_step_name": (string) nom de l’étape pour ce message s’il provient d’un Canvas,
  "dispatch_id": (string) ID de l’envoi du message (id unique pour chaque « transmission » envoyée depuis la plateforme Braze et les utilisateurs qui reçoivent un message programmé obtiennent le même dispatch_id. Les messages basés sur des actions ou les messages déclenchés par API reçoivent un dispatch_id unique pour chaque utilisateur,
  "send_id": (string) ID d’envoi de message auquel appartient ce message
}
```
{% endapi %}

{% api %}

## Événements de rejet SMS

{% apitags %}
SMS, Rejet
{% endapitags %}

Cet événement survient lorsqu’un envoi SMS est rejeté par l’opérateur ce qui peut se produire pour plusieurs raisons. Utilisez cet événement et les codes d’erreur fournis pour résoudre les problèmes liés à la livraison du SMS.

```json
// Rejet SMS : users.messages.sms.Rejection
{
  "id": (string) ID unique pour cet événement,
  "user_id": (string) ID utilisateur Braze de l’utilisateur,
  "external_user_id": (string) ID externe de l’utilisateur,
  "time": (int) heure en UTC à 10 chiffres de l’événement, en secondes, depuis la période,
  "timezone": (string) fuseau horaire de l’utilisateur au format IANA à l’heure de l’événement,
  "from_phone_number": (string) le numéro de téléphone de l’expéditeur du message (remis et non remis uniquement),
  "subscription_group_id": (string) ID du groupe d’abonnement ciblé pour ce message SMS,
  "subscription_group_api_id": (string)ID de l’API du groupe d’abonnement ciblé pour ce message SMS,
  "to_phone_number": (string) le numéro auquel le message a été envoyé,
  "campaign_id": (string) ID de la campagne si provenant d’une campagne,
  "campaign_name": (string) nom de la campagne,
  "message_variation_id": (string) ID de la variation du message si provenant d’une campagne,
  "message_variation_name": (string) le nom de la variation du message si provenant d’une campagne,
  "canvas_id": (string) ID du Canvas s’il provient d’un Canvas,
  "canvas_name": (string) nom du Canvas,
  "canvas_variation_id": (string) ID de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_variation_name": (string) nom de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_step_id": (string) ID de l’étape pour ce message s’il provient d’un Canvas,
  "canvas_step_name": (string) nom de l’étape pour ce message s’il provient d’un Canvas,
  "dispatch_id": (string) ID de l’envoi du message (id unique pour chaque « transmission » envoyée depuis la plateforme Braze et les utilisateurs qui reçoivent un message programmé obtiennent le même dispatch_id. Les messages basés sur des actions ou les messages déclenchés par API reçoivent un dispatch_id unique pour chaque utilisateur,
  "send_id": (string) ID d’envoi de message auquel appartient ce message,
  "error": (string) l’erreur fournie par Braze (uniquement les événements de rejet et d’échec de livraison),
  "provider_error_code": (string) le code de la raison expliquant pourquoi le message n’a pas été envoyé, fourni par le fournisseur (uniquement les événements de rejet et d’échec de livraison)
}
```
{% endapi %}


{% api %}

## Événements d’échec de livraison SMS

{% apitags %}
SMS, livraison
{% endapitags %}

Cet événement survient lorsqu’un SMS rencontre une problème de livraison. Utilisez cet événement et les codes d’erreur fournis pour résoudre les problèmes liés à la livraison de SMS.

```json
// Échec de livraison SMS : users.messages.sms.DeliveryFailure
{
  "id": (string) ID unique pour cet événement,
  "user_id": (string) ID utilisateur Braze de l’utilisateur,
  "external_user_id": (string) ID externe de l’utilisateur,
  "time": (int) heure en UTC à 10 chiffres de l’événement, en secondes, depuis la période,
  "timezone": (string) fuseau horaire de l’utilisateur au format IANA à l’heure de l’événement,
  "from_phone_number": (string) le numéro de téléphone de l’expéditeur du message (remis et non remis uniquement),
  "subscription_group_id": (string) ID du groupe d’abonnement ciblé pour ce message SMS,
  "subscription_group_api_id": (string)ID de l’API du groupe d’abonnement ciblé pour ce message SMS,
  "to_phone_number": (string) le numéro auquel le message a été envoyé,
  "campaign_id": (string) ID de la campagne si provenant d’une campagne,
  "campaign_name": (string) nom de la campagne,
  "message_variation_id": (string) ID de la variation du message si provenant d’une campagne,
  "message_variation_name": (string) le nom de la variation du message si provenant d’une campagne,
  "canvas_id": (string) ID du Canvas s’il provient d’un Canvas,
  "canvas_name": (string) nom du Canvas,
  "canvas_variation_id": (string) ID de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_variation_name": (string) nom de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_step_id": (string) ID de l’étape pour ce message s’il provient d’un Canvas,
  "canvas_step_name": (string) nom de l’étape pour ce message s’il provient d’un Canvas,
  "dispatch_id": (string) ID de l’envoi du message (id unique pour chaque « transmission » envoyée depuis la plateforme Braze et les utilisateurs qui reçoivent un message programmé obtiennent le même dispatch_id. Les messages basés sur des actions ou les messages déclenchés par API reçoivent un dispatch_id unique pour chaque utilisateur,
  "send_id": (string) ID d’envoi de message auquel appartient ce message,
  "error": (string) l’erreur fournie par Braze (uniquement les événements de rejet et d’échec de livraison),
  "provider_error_code": (string) le code de la raison expliquant pourquoi le message n’a pas été envoyé, fourni par le fournisseur (uniquement les événements de rejet et d’échec de livraison)
}
```
{% endapi %}
{% api %}

## Événements de réception de SMS entrant

{% apitags %}
SMS, InboundReceived
{% endapitags %}

Cet événement se produit lorsque l’un de vos utilisateurs envoie un SMS à un numéro de téléphone dans l’un de vos groupes d’abonnement SMS Braze . 

Lorsque Braze reçoit un SMS entrant, nous attribuons ce message entrant à tout utilisateur qui partage ce numéro de téléphone. Par conséquent, vous pouvez recevoir plusieurs événements par message entrant si plusieurs utilisateurs de votre instance Braze partagent le même numéro de téléphone. Si vous devez attribuer des ID Utilisateurs spécifiques sur la base des messages précédents envoyés à cet utilisateur, vous pouvez utiliser l’événement SMS Livré pour attribuer des événements entrants reçus à l’ID utilisateur qui a reçu le plus récemment un message de votre numéro Braze.

Si nous détectons que ce message entrant est une réponse à une campagne sortante ou à un composant Canvas envoyé par Braze, nous inclurons également les métadonnées de la campagne ou du Canvas avec l’événement. Braze définit une réponse comme un message entrant dans les quatre heures suivant un message sortant. Cependant, il existe un cache d’une minute pour les informations attribuées de la campagne provenant du dernier SMS sortant reçu.

```json
// SMS entrant reçu : users.messages.sms.InboundReceive
{
  "id": (string) ID unique pour cet événement,
  "user_id": (string) ID utilisateur Braze de l’utilisateur,
  "external_user_id": (string) ID externe de l’utilisateur,
  "app_group_id": (string) ID API du groupe d’apps associé au numéro de téléphone entrant,
  "time": (int) heure en UTC à 10 chiffres de l’événement, en secondes, depuis la période,
  "user_phone_number": (string) le numéro de téléphone de l’utilisateur qui a envoyé le message à votre numéro Braze,
  "subscription_group_id": (string) ID du groupe d’abonnement auquel appartient le numéro qui a été contacté par l’utilisateur,
  "inbound_phone_number": (string) le numéro de téléphone auquel le message a été envoyé,
  "inbound_media_urls": (string) les URL des médias joints entrants s’ils ont été reçus, 
  "action" : (string) l’action d’inscription prise par Braze à la suite de ce message (`subscribed` (abonné), `unsubscribed` (désabonné) ou `none` (aucun) sur la base du corps du message. `None` (Aucun) indique que ce message entrant ne correspond à aucun de vos mots-clés pour l’abonnement ou le désabonnement d’un utilisateur),
  "message_body" : (string) le corps du message envoyé par l’utilisateur,
  "campaign_id": (string) ID de la campagne si Braze a déterminé que ce message entrant répond à une campagne,
  "campaign_name": (string) nom de la campagne,
  "message_variation_id": (string) ID de la variation de message si Braze a déterminé que ce message entrant répond à une campagne,
  "message_variation_name": (string) le nom de la variation de message si Braze a déterminé que ce message entrant répond à une campagne,
  "canvas_id": (string) ID du Canvas s’il provient d’un Canvas,
  "canvas_name": (string) nom du Canvas,
  "canvas_variation_id": (string) ID de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_variation_name": (string) nom de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_step_id": (string) ID de l’étape pour ce message s’il provient d’un Canvas,
  "canvas_step_name": (string) nom de l’étape pour ce message s’il provient d’un Canvas
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
Notez que l’événement de conversion est encodé dans le champ `conversion_behavior`, qui inclut le type d’événement de conversion, la fenêtre (période) et les informations supplémentaires en fonction du type d’événement de conversion. Le champ `conversion_behavior_index` représente l’événement de conversion. c.-à-d., 0 = A, 1 = B, 2 = C, 3 = D.
{% endalert %}

```json
// Événement de conversion d’une campagne : users.campaigns.Conversion
{
  "id": (string) ID unique pour cet événement,
  "user_id": (string) ID utilisateur Braze de l’utilisateur,
  "external_user_id": (string) ID externe de l’utilisateur,
  "time": (int) heure en UTC à 10 chiffres de l’événement, en secondes, depuis la période,
  "timezone": (string) fuseau horaire de l’utilisateur au format IANA à l’heure de l’événement,
  "app_id": (string)ID de l’application sur laquelle l’action de l’utilisateur s’est produite,
  "campaign_id": (string) ID de la campagne,
  "campaign_name": (string) nom de la campagne,
  "conversion_behavior_index": (int) index du comportement de conversion,
  "conversion_behavior": (string) chaîne de caractères encodée en JSON décrivant le comportement de conversion,
  "message_variation_id": (string) ID de la variation du message,
  "message_variation_name": (string) le nom de la variation de message,
  "send_id": (string) ID du message si spécifié pour la campagne (voir Envoyer un identifiant sous Types d’identifiant API)
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
Notez que l’événement de conversion est encodé dans le champ `conversion_behavior`, qui inclut le type d’événement de conversion, la fenêtre (période) et les informations supplémentaires en fonction du type d’événement de conversion. Le champ `conversion_behavior_index` représente l’événement de conversion. c.-à-d., 0 = A, 1 = B, 2 = C, 3 = D.
{% endalert %}

```json
// Événement de conversion Canvas : users.canvas.Conversion
{
  "id": (string) ID unique pour cet événement,
  "user_id": (string) ID utilisateur Braze de l’utilisateur,
  "external_user_id": (string) ID externe de l’utilisateur,
  "time": (int) heure en UTC à 10 chiffres de l’événement, en secondes, depuis la période,
  "timezone": (string) fuseau horaire de l’utilisateur au format IANA à l’heure de l’événement,
  "app_id": (string)ID de l’application sur laquelle l’action de l’utilisateur s’est produite,
  "canvas_id": (string) ID du Canvas,
  "canvas_name": (string) nom du Canvas,
  "conversion_behavior_index": (int) index du comportement de conversion,
  "conversion_behavior": (string) chaîne de caractères encodée en JSON décrivant le comportement de conversion,
  "canvas_variation_id": (string) ID de la variation Canvas dans laquelle se trouve l’utilisateur,
  "canvas_variation_name": (string) nom de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_step_id": (string) ID de la dernière étape à laquelle l’utilisateur a été envoyé avant la conversion
  "canvas_step_name": (string) nom de l’étape pour ce message s’il provient d’un Canvas,
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
// Événement d’entrée dans le Canvas : users.canvas.Entry
{
  "id": (string) ID unique pour cet événement,
  "user_id": (string) ID utilisateur Braze de l’utilisateur,
  "external_user_id": (string) ID externe de l’utilisateur,
  "time": (int) heure en UTC à 10 chiffres de l’événement, en secondes, depuis la période,
  "timezone": (string) fuseau horaire de l’utilisateur au format IANA à l’heure de l’événement,
  "canvas_id": (string) ID du Canvas,
  "canvas_name": (string) nom du Canvas,
  "canvas_variation_id": (string) ID de la variation Canvas dans laquelle se trouve l’utilisateur,
  "canvas_variation_name": (string) nom de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_step_id": (string) ID de l’étape dans laquelle l’utilisateur est entré,
  "canvas_step_name": (string) nom de l’étape pour ce message s’il provient d’un Canvas,
  "in_control_group": (boolean) si l’utilisateur était inscrit dans le groupe de contrôle pour un Canvas
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
// Inscription dans le groupe de contrôle de la campagne : users.campaigns.EnrollInControl
{
  "id": (string) ID unique pour cet événement,
  "user_id": (string) ID utilisateur Braze de l’utilisateur,
  "external_user_id": (string) ID externe de l’utilisateur,
  "app_id": (string)ID de l’application sur laquelle l’action de l’utilisateur s’est produite,
  "time": (int) heure en UTC à 10 chiffres de l’événement, en secondes, depuis la période,
  "timezone": (string) fuseau horaire de l’utilisateur au format IANA à l’heure de l’événement,
  "campaign_id": (string) ID de la campagne,
  "campaign_name": (string) nom de la campagne,
  "message_variation_id": (string) ID de la variation du message,
  "message_variation_name": (string) le nom de la variation de message,
  "send_id": (string) ID du message si spécifié pour la campagne (voir Envoyer un identifiant sous Types d’identifiant API)
}
```

{% endapi %}

{% api %}
## Événements de désinstallation

{% apitags %}
Désinstallation
{% endapitags %}

Cet événement se produit lorsqu’un utilisateur désinstalle une application. Utilisez ces données pour suivre les utilisateurs qui désinstallent une application. Même s’il s’agit actuellement d’un message d’événement d’engagement, ceci deviendra un événement de comportement de l’utilisateur dans l’avenir.

{% alert important %}
Cet événement n’est pas déclenché au moment précis où l’utilisateur désinstalle réellement l’application, car cette action est impossible à suivre exactement. Braze envoie une notification push silencieuse quotidienne pour déterminer si l’application existe toujours sur le périphérique de votre utilisateur, et si nous obtenons une erreur sur cette notification push silencieuse, on suppose alors que l’application a été désinstallée.
{% endalert %}

```json
// Événement de désinstallation : users.behaviors.Uninstall
{
  "id": (string) ID unique pour cet événement,
  "user_id": (string) ID utilisateur Braze de l’utilisateur,
  "external_user_id": (string) ID externe de l’utilisateur,
  "time": (int) heure en UTC à 10 chiffres de l’événement, en secondes, depuis la période,
  "app_id": (string)ID de l’application sur laquelle l’action de l’utilisateur s’est produite,
  "device_id": (string) ID de l’appareil sur lequel la session s’est produite
}
```

{% endapi %}
