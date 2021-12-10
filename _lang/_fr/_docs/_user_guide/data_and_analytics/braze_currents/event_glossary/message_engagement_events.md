---
nav_title: Événements de participation aux messages
layout: Glossaire de l'engagement
page_order: 5
excerpt_separator: ""
page_type: glossary
description: "Ce glossaire répertorie les divers événements d'engagement de messages que Braze peut suivre et envoyer aux entrepôts de données choisis en utilisant les Courants."
tool: Courants
---

Veuillez contacter votre responsable de compte ou ouvrir un [ticket d'assistance]({{site.baseurl}}/braze_support/) si vous avez besoin d'accéder à d'autres droits d'événement. Si vous ne trouvez pas ce dont vous avez besoin ci-dessous, Consultez notre [Librairie d'événements de comportement client]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/customer_behavior_events/) ou nos exemples de données [courants](https://github.com/Appboy/currents-examples/tree/master/sample-data).

{% details Explanation of Message Engagement Event Structure %}
<br>
Cette répartition de l'événement montre quel type d'information est généralement inclus dans un événement d'engagement de messages. Grâce à une bonne compréhension de ses composants, vos développeurs et votre équipe de stratégie de renseignements commerciaux peuvent utiliser les données des événements entrants pour faire des rapports basés sur des données. et tirer parti d'autres indicateurs de données précieux.

![image]({% image_buster /assets/img/message_engagement_event.png %})

Les événements d'engagement de message sont composés de __propriétés__ spécifiques à l'utilisateur, __propriétés de suivi de campagne/canvas__ et __propriétés spécifiques à l'événement__.

{% enddetails %}

{% alert important %}
Veuillez noter que ces schémas __s'appliquent uniquement aux données d'événement de fichier à plat que nous envoyons aux partenaires de Data Warehouse (Google Cloud Storage, Amazon S3, et Microsoft Azure Blob Storage)__. Pour le schéma qui s'applique aux autres partenaires, veuillez consulter [leurs pages respectives]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/available_partners/).<br><br>De plus, notez que les courants abandonneront les événements avec des charges excessivement grandes de plus de 900KB.
{% endalert %}

{% api %}

## Envoyer des événements

{% apitags %}
Push, envoie
{% endapitags %}

Cet événement se produit lorsque Braze traite un message push pour un utilisateur, le transmettant à Apple Push Notification Service ou Fire Cloud Messaging. Cela ne signifie pas que la poussée a été envoyée à l'appareil, juste qu'un message a été envoyé.

```json
// Push Notification Send: users.messages.pushnotification. fin
{
  "id": (string) id unique de cet événement,
  "user_id": (string) Braze identifiant utilisateur de l'utilisateur,
  "external_user_id": (string) ID externe de l'utilisateur,
  "temps": (int) 10 chiffres heure UTC de l'événement en secondes depuis l'époque,
  "fuseau horaire": (chaîne) IANA fuseau horaire de l'utilisateur au moment de l'événement,
  "app_id": (string) id pour l'application sur laquelle l'action de l'utilisateur s'est produite,
  "campaign_id": (string) id de la campagne si à partir d'une campagne,
  "campaign_name": (chaîne) nom de la campagne,
  "message_variation_id": (string) id de la variation du message si une campagne,
  "canvas_id": (chaîne) id de la toile si elle provient d'un Canvas,
  "canvas_name": (chaîne) nom de la toile,
  "canvas_variation_id": (string) id de la variation de Canvas dans laquelle l'utilisateur est à partir d'un Canvas,
  "canvas_variation_name": (chaîne) nom de la variation de Canvas dans laquelle l'utilisateur est si à partir d'un Canvas,
  "canvas_step_id": (string) id de l'étape pour ce message si à partir d'un Canvas,
  "canvas_step_name": (chaîne) nom de l'étape pour ce message si à partir d'un Canvas,
  "plate-forme": (chaîne) plate-forme de l'appareil (iOS, Android, web, etc. ,
  "device_id": (string) id de l'appareil auquel nous avons fait une tentative de livraison,
  "send_id": (string) id du message si spécifié pour la campagne (Voir Send Identifier under API Identifier Types),
  "dispatch_id": (string) id de l'envoi de message (id unique pour chaque 'transmission' envoyée depuis la plate-forme Braze). Les utilisateurs qui reçoivent un message de planification reçoivent le même dispatch_id. Les messages basés sur l'action ou sur l'API obtiennent un dispatch_id unique par utilisateur.
  "ad_id": (chaîne) identifiant publicitaire,
  "ad_id_type": (chaîne) Un de 'ios_idfa', 'google_ad_id', 'windows_ad_id', OU 'roku_ad_id',
  "ad_tracking_enabled": (boolean) si le suivi publicitaire est activé pour l'appareil
}
```
#### Détails de la propriété
- Pour `ad_id`, `ad_id_type` et `ad_tracking_enabled`, vous devrez explicitement collecter l'idfa iOS et Android Google adid à travers les SDK natifs. En savoir plus à leur sujet ici : [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/optional_idfa_collection/#optional-idfa-collection/), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id).
- Si vous utilisez Kafka pour ingérer des données de [courants]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/) contactez votre Responsable de la Customer Success ou le Gestionnaire de comptes pour activer la fonction flipper pour envoyer `ad_id`.
{% endapi %}
{% api %}

## Envoyer les événements ouverts

{% apitags %}
Push, Ouvre
{% endapitags %}

Cet événement se produit lorsqu'un utilisateur clique directement sur la notification push pour ouvrir l'application. Actuellement, les événements Push Open se réfèrent spécifiquement à "Direct Opens" plutôt qu'à "Total Opens". Cela n'inclut pas les statistiques affichées au niveau de la campagne des « ouvertures influencées » car elles ne sont pas attribuées au niveau de l'utilisateur.

```json
// Push Notification Open: users.messages.pushnotification. stylo
{
  "id": (string) id unique de cet événement,
  "user_id": (string) Braze identifiant utilisateur de l'utilisateur,
  "external_user_id": (string) ID externe de l'utilisateur,
  "temps": (int) 10 chiffres heure UTC de l'événement en secondes depuis l'époque,
  "fuseau horaire": (chaîne) IANA fuseau horaire de l'utilisateur au moment de l'événement,
  "app_id": (string) id pour l'application sur laquelle l'action de l'utilisateur s'est produite,
  "campaign_id": (string) id de la campagne si à partir d'une campagne,
  "campaign_name": (chaîne) nom de la campagne,
  "message_variation_id": (string) id de la variation du message si une campagne,
  "canvas_id": (chaîne) id de la toile si elle provient d'un Canvas,
  "canvas_name": (chaîne) nom de la toile,
  "canvas_variation_id": (string) id de la variation de Canvas dans laquelle l'utilisateur est à partir d'un Canvas,
  "canvas_variation_name": (chaîne) nom de la variation de Canvas dans laquelle l'utilisateur est si à partir d'un Canvas,
  "canvas_step_id": (string) id de l'étape pour ce message si à partir d'un Canvas,
  "canvas_step_name": (chaîne) nom de l'étape pour ce message si à partir d'un Canvas,
  "canvas_step_message_variation_id": (string) ID API de la variation du message de l'étape canvas que cet utilisateur a reçu,
  "plate-forme": (chaîne) plate-forme de l'appareil (iOS, Android, web, etc. ,
  "os_version": (string) os version de l'appareil utilisé pour l'action,
  "device_model": (string) modèle matériel de l'appareil,
  "device_id": (string) id de l'appareil auquel nous avons fait une tentative de livraison,
  "button_action_type": (string) Type d'action de la notification push,
  bouton. Un des [URI, DEEP_LINK, NONE, CLOSE, SHARE]. null sinon
  à partir d'un clic de bouton,
  "button_string": (string) identifiant (button_string) du bouton de notification push cliqué. null si non à partir d'un clic de bouton,
  "send_id": (chaîne) id du message si spécifié pour la campagne (Voir Envoyer l'identifiant sous les types de l'API),
  "dispatch_id" : (string) id du message dispatch (id unique pour chaque 'transmission' envoyée de la plate-forme Braze). Les utilisateurs qui reçoivent un message de planification reçoivent le même dispatch_id. Les messages basés sur l'action ou sur l'API obtiennent un dispatch_id unique par utilisateur.
  "ad_id": (chaîne) identifiant publicitaire,
  "ad_id_type": (chaîne) Un de 'ios_idfa', 'google_ad_id', 'windows_ad_id', OU 'roku_ad_id',
  "ad_tracking_enabled": (boolean) si le suivi publicitaire est activé pour l'appareil
}
```
#### Détails de la propriété
- Pour `ad_id`, `ad_id_type` et `ad_tracking_enabled`, vous devrez explicitement collecter l'idfa iOS et Android Google adid à travers les SDK natifs. En savoir plus à leur sujet ici : [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/optional_idfa_collection/#optional-idfa-collection/), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id).
- Si vous utilisez Kafka pour ingérer des données de [courants]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/) contactez votre Responsable de la Customer Success ou le Gestionnaire de comptes pour activer la fonction flipper pour envoyer `ad_id`.
{% endapi %}
{% api %}

## Notifications push dans les événements d'avant-plan iOS

{% apitags %}
Push, iOS, envoie
{% endapitags %}

Cet événement se produit si un push a été envoyé alors que l'application iOS était au premier plan. Si l'utilisateur voit le push lorsque l'application est au premier plan, est déterminé par la façon dont vos développeurs ont intégré le SDK iOS pour la gestion des push de premier plan détaillée [ici]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/#ios-10).

```json
// Push Notification iOS Premier: users.messages.pushnotification. osForeground
{
  "id": (string) id unique de cet événement,
  "user_id": (string) Braze identifiant utilisateur de l'utilisateur,
  "external_user_id": (string) ID externe de l'utilisateur,
  "temps": (int) 10 chiffres heure UTC de l'événement en secondes depuis l'époque,
  "fuseau horaire": (chaîne) IANA fuseau horaire de l'utilisateur au moment de l'événement,
  "app_id": (string) id pour l'application sur laquelle l'action de l'utilisateur s'est produite,
  "campaign_id": (string) id de la campagne si à partir d'une campagne,
  "campaign_name": (chaîne) nom de la campagne,
  "message_variation_id": (string) id de la variation du message si une campagne,
  "canvas_id": (chaîne) id de la toile si elle provient d'un Canvas,
  "canvas_name": (chaîne) nom de la toile,
  "canvas_variation_id": (string) id de la variation de Canvas dans laquelle l'utilisateur est à partir d'un Canvas,
  "canvas_variation_name": (chaîne) nom de la variation de Canvas dans laquelle l'utilisateur est si à partir d'un Canvas,
  "canvas_step_id": (string) id de l'étape pour ce message si à partir d'un Canvas,
  "canvas_step_name": (chaîne) nom de l'étape pour ce message si à partir d'un Canvas,
  "plate-forme": (chaîne) plate-forme de l'appareil (iOS, Android, web, etc. ,
  "device_id": (string) id de l'appareil auquel nous avons fait une tentative de livraison,
  "send_id": (string) id du message si spécifié pour la campagne (Voir Send Identifier under API Identifier Types),
  "dispatch_id": (string) id de l'envoi de message (id unique pour chaque 'transmission' envoyée depuis la plate-forme Braze). Les utilisateurs qui reçoivent un message de planification reçoivent le même dispatch_id. Les messages basés sur l'action ou sur l'API obtiennent un dispatch_id unique par utilisateur.
  "ad_id": (chaîne) identifiant publicitaire,
  "ad_id_type": (chaîne) Un de 'ios_idfa', 'google_ad_id', 'windows_ad_id', OU 'roku_ad_id',
  "ad_tracking_enabled": (boolean) si le suivi publicitaire est activé pour l'appareil
}
```
#### Détails de la propriété
- Pour `ad_id`, `ad_id_type` et `ad_tracking_enabled`, vous devrez explicitement collecter l'idfa iOS et Android Google adid à travers les SDK natifs. En savoir plus à leur sujet ici : [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/optional_idfa_collection/#optional-idfa-collection/), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id).
- Si vous utilisez Kafka pour ingérer des données de [courants]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/) contactez votre Responsable de la Customer Success ou le Gestionnaire de comptes pour activer la fonction flipper pour envoyer `ad_id`.
{% endapi %}
{% api %}

## Rebond des notifications push

{% apitags %}
Pousser, envoyer, rebondir
{% endapitags %}

Cet événement se produit quand une erreur est reçue soit par le service de notification Push d'Apple soit par Fire Cloud Messaging. Cela signifie que le message push a été rebondi et donc pas livré à l’appareil de l’utilisateur.

```json
// Notification Push Bounce: users.messages.pushnotification. bondir
{
  "id": (string) id unique de cet événement,
  "user_id": (string) Braze identifiant utilisateur de l'utilisateur,
  "external_user_id": (string) ID externe de l'utilisateur,
  "temps": (int) 10 chiffres heure UTC de l'événement en secondes depuis l'époque,
  "fuseau horaire": (chaîne) IANA fuseau horaire de l'utilisateur au moment de l'événement,
  "app_id": (string) id pour l'application sur laquelle le bounce a eu lieu,
  "campaign_id": (string) id de la campagne si à partir d'une campagne,
  "campaign_name": (chaîne) nom de la campagne,
  "message_variation_id": (string) id de la variation du message si une campagne,
  "canvas_id": (chaîne) id de la toile si elle provient d'un Canvas,
  "canvas_name": (chaîne) nom de la toile,
  "canvas_variation_id": (string) id de la variation de Canvas dans laquelle l'utilisateur est à partir d'un Canvas,
  "canvas_variation_name": (chaîne) nom de la variation de Canvas dans laquelle l'utilisateur est si à partir d'un Canvas,
  "canvas_step_id": (string) id de l'étape pour ce message si à partir d'un Canvas,
  "canvas_step_name": (chaîne) nom de l'étape pour ce message si à partir d'un Canvas,
  "plate-forme": (chaîne) plate-forme de l'appareil (iOS, Android, web, etc. ,
  "device_id": (string) id de l'appareil auquel nous avons fait une tentative de livraison,
  "send_id": (string) id du message si spécifié pour la campagne (Voir Send Identifier under API Identifier Types),
  "dispatch_id": (string) id de l'envoi de message (id unique pour chaque 'transmission' envoyée depuis la plate-forme Braze). Les utilisateurs qui reçoivent un message de planification reçoivent le même dispatch_id. Les messages basés sur l'action ou sur l'API obtiennent un dispatch_id unique par utilisateur.
  "ad_id": (chaîne) identifiant publicitaire,
  "ad_id_type": (chaîne) Un de 'ios_idfa', 'google_ad_id', 'windows_ad_id', OU 'roku_ad_id',
  "ad_tracking_enabled": (boolean) si le suivi publicitaire est activé pour l'appareil
}
```
#### Détails de la propriété
- Si vous utilisez Kafka pour ingérer des données de [courants]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/) contactez votre Responsable de la Customer Success ou le Gestionnaire de comptes pour activer la fonction flipper pour envoyer `ad_id`.
{% endapi %}
{% api %}

## Envoyer des événements par e-mail

{% apitags %}
Courriel, Envoie
{% endapitags %}

Cet événement se produit lorsqu'une demande d'envoi de courriel a été communiquée avec succès entre Braze et Sendgrid. Cela ne veut pas dire que l'e-mail a été reçu dans la boîte de réception de l'utilisateur final

```json
// Email Send: users.messages.email. end
{
  // Propriétés spécifiques à l'utilisateur
  "id": (string) id unique de cet événement,
  "user_id": (string) Braze identifiant utilisateur de l'utilisateur,
  "external_user_id": (string) ID externe de l'utilisateur,
  "temps": (int) 10 chiffres heure UTC de l'événement en secondes depuis l'époque,
  "fuseau horaire" : (chaîne) IANA fuseau horaire de l'utilisateur au moment de l'événement,
  // Propriétés de suivi Campaign/Canvas
  "campaign_id": (string) id de la campagne si à partir d'une campagne,
  "campaign_name": (chaîne) nom de la campagne,
  "message_variation_id": (string) id de la variation de message si une campagne,
  "canvas_id": (string) id de la Toile si à partir d'un Canvas,
  "canvas_name": (string) nom des Canvas,
  "canvas_variation_id": (string) id de la variation de Canvas dans laquelle l'utilisateur est si à partir d'un Canvas,
  "canvas_variation_name": (chaîne) nom de la variation de Canvas dans laquelle l'utilisateur est si à partir d'un Canvas,
  "canvas_step_id": (string) id de l'étape pour ce message si à partir d'un Canvas,
  "canvas_step_name": (chaîne) nom de l'étape pour ce message si à partir d'un Canvas,
  // Propriétés spécifiques à l'évènement
  "send_id": (string) id du message si spécifié pour la campagne (Voir Send Identifier sous API Identifier Types),
  "dispatch_id": (string) id de l'envoi de message (id unique pour chaque 'transmission' envoyée depuis la plate-forme Braze). Les utilisateurs qui reçoivent un message de planification reçoivent le même dispatch_id. Les messages basés sur l'action ou sur l'API obtiennent un dispatch_id unique par utilisateur,
  "email_address": (string) adresse email pour cet événement,
  "ip_pool": (string) pool IP utilisé pour l'envoi de message
}
```
#### Détails de la propriété
- Le comportement de `dispatch_id` diffère entre Canvas et les campagnes car Braze traite les pas de Canvas (à l'exception des pas d'entrée, qui peuvent être programmés) en tant qu'événements déclenchés, même lorsqu'ils sont "programmés". [En savoir plus sur le comportement de `dispatch_id` dans Canvas et les campagnes ici]({{site.baseurl}}/help/help_articles/data/dispatch_id/).
{% endapi %}


{% api %}

## Évènements de livraison par e-mail

{% apitags %}
Courriel, livraison
{% endapitags %}

Cet événement se produit lorsqu'un e-mail envoyé a été envoyé avec succès à la boîte de réception des utilisateurs finaux.

```json
// Livraison d'e-mail: users.messages.email. elivery
{
  "id": (string) id unique de cet événement,
  "user_id": (string) Braze identifiant utilisateur de l'utilisateur,
  "external_user_id": (string) ID externe de l'utilisateur,
  "temps": (int) 10 chiffres heure UTC de l'événement en secondes depuis l'époque,
  "fuseau horaire": (chaîne) IANA fuseau horaire de l'utilisateur au moment de l'événement,
  "campaign_id": (string) id de la campagne si à partir d'une campagne,
  "campaign_name": (string) nom de la campagne,
  "message_variation_id": (string) id de la variation de message si une campagne,
  "canvas_id": (chaîne) id de la toile si une toile
  "canvas_name": (string) nom des Canvas,
  "canvas_variation_id": (string) id de la variation de Canvas dans laquelle l'utilisateur est à partir d'un Canvas,
  "canvas_variation_name": (chaîne) nom de la variation de Canvas dans laquelle l'utilisateur est si à partir d'un Canvas,
  "canvas_step_id": (string) id de l'étape pour ce message si à partir d'un Canvas,
  "canvas_step_name": (string) nom de l'étape pour ce message si à partir d'un Canvas,
  "send_id": (string) id du message si spécifié pour la campagne (Voir Send Identifier under API Identifier Types),
  "dispatch_id": (string) id de l'envoi de message (id unique pour chaque 'transmission' envoyée depuis la plate-forme Braze). Les utilisateurs qui reçoivent un message de planification reçoivent le même dispatch_id. Les messages basés sur l'action ou sur l'API obtiennent un dispatch_id unique par utilisateur.
  "email_address": (chaîne) adresse email pour cet événement
  "sending_ip": (string) l'adresse IP à partir de laquelle le message a été envoyé (Email Delivery, Bounce, et SoftBounce événements seulement. Ne sera affiché que sur les événements si le message a été réellement tenté. Pour certains autres bounces, les informations pourraient être perdues si le serveur du destinataire a déjà accepté le courrier et seulement après la fermeture de la connexion a décidé qu'il ne pouvait pas livrer le courrier),
  "ip_pool": (string) pool IP utilisé pour l'envoi de message
}
```
#### Détails de la propriété
- Le comportement de `dispatch_id` diffère entre Canvas et les campagnes car Braze traite les pas de Canvas (à l'exception des pas d'entrée, qui peuvent être programmés) en tant qu'événements déclenchés, même lorsqu'ils sont "programmés". [En savoir plus sur le comportement de `dispatch_id` dans Canvas et les campagnes ici]({{site.baseurl}}/help/help_articles/data/dispatch_id/).
{% endapi %}


{% api %}

## Envoyer un e-mail aux événements ouverts

{% apitags %}
Courriel, s'ouvre
{% endapitags %}

Cet événement se produit lorsqu'un utilisateur ouvre un e-mail. Plusieurs événements peuvent être générés pour la même campagne si un utilisateur ouvre l'e-mail plusieurs fois.

```json
// Courriel Open: users.messages.email. stylo
{
  "id": (string) id unique de cet événement,
  "user_id": (string) Braze identifiant utilisateur de l'utilisateur,
  "external_user_id": (string) ID externe de l'utilisateur,
  "temps": (int) 10 chiffres heure UTC de l'événement en secondes depuis l'époque,
  "fuseau horaire": (chaîne) IANA fuseau horaire de l'utilisateur au moment de l'événement,
  "campaign_id": (string) id de la campagne si à partir d'une campagne,
  "campaign_name": (string) nom de la campagne,
  "message_variation_id": (string) id de la variation de message si une campagne,
  "canvas_id" : (chaîne) id de la toile si elle provient d'un canvas,
  "canvas_name": (chaîne) nom de la toile,
  "canvas_variation_id": (string) id de la variation de Canvas dans laquelle l'utilisateur est à partir d'un Canvas,
  "canvas_variation_name": (chaîne) nom de la variation de Canvas dans laquelle l'utilisateur est si à partir d'un Canvas,
  "canvas_step_id": (string) id de l'étape pour ce message si à partir d'un Canvas,
  "canvas_step_name": (string) nom de l'étape pour ce message si à partir d'un Canvas,
  "send_id": (string) id du message si spécifié pour la campagne (Voir Send Identifier under API Identifier Types),
  "dispatch_id": (string) id de l'envoi de message (id unique pour chaque 'transmission' envoyée depuis la plate-forme Braze). Les utilisateurs qui reçoivent un message de planification reçoivent le même dispatch_id. Les messages basés sur l'action ou sur l'API obtiennent un dispatch_id unique par utilisateur.
  "email_address": (chaîne) adresse email pour cet événement
  "user_agent": (string) description du système de l'utilisateur et du navigateur pour l'événement (Email Click, Open, et les événements MarkAsSpam seulement),
  "ip_pool": (string) pool IP utilisé pour l'envoi de message
}
```
#### Détails de la propriété
- Le comportement de `dispatch_id` diffère entre Canvas et les campagnes car Braze traite les pas de Canvas (à l'exception des pas d'entrée, qui peuvent être programmés) en tant qu'événements déclenchés, même lorsqu'ils sont "programmés". [En savoir plus sur le comportement de `dispatch_id` dans Canvas et les campagnes ici]({{site.baseurl}}/help/help_articles/data/dispatch_id/).
{% endapi %}



{% api %}

## Evénements des clics par e-mail

{% apitags %}
E-mail, clics
{% endapitags %}

Cet événement se produit lorsqu'un utilisateur clique sur un email. Plusieurs événements peuvent être générés pour la même campagne si un utilisateur clique plusieurs fois ou clique sur différents liens dans l'email.

```json
// Email Click: users.messages.email. lick
{
  "id": (string) unique id de cet événement,
  "user_id": (string) Braze identifiant utilisateur de l'utilisateur,
  "external_user_id": (string) ID externe de l'utilisateur,
  "temps": (int) 10 chiffres heure UTC de l'événement en secondes depuis l'époque,
  "fuseau horaire": (chaîne) IANA fuseau horaire de l'utilisateur au moment de l'événement,
  "campaign_id": (string) id de la campagne si à partir d'une campagne,
  "campaign_name": (string) nom de la campagne,
  "message_variation_id": (string) id de la variation de message si une campagne,
  "canvas_id": (chaîne) id de la toile si une toile
  "canvas_name": (string) nom des Canvas,
  "canvas_variation_id": (string) id de la variation de Canvas dans laquelle l'utilisateur est à partir d'un Canvas,
  "canvas_variation_name": (chaîne) nom de la variation de Canvas dans laquelle l'utilisateur est si à partir d'un Canvas,
  "canvas_step_id": (string) id de l'étape pour ce message si à partir d'un Canvas,
  "canvas_step_name": (string) nom de l'étape pour ce message si à partir d'un Canvas,
  "send_id": (string) id du message si spécifié pour la campagne (Voir Send Identifier under API Identifier Types),
  "dispatch_id": (string) id de l'envoi de message (id unique pour chaque 'transmission' envoyée depuis la plate-forme Braze). Uniquement inclus lorsque campaign_id est présent. Les utilisateurs qui reçoivent un message de planification reçoivent le même dispatch_id. Les messages basés sur l'action ou sur l'API obtiennent un dispatch_id unique par utilisateur.
  "email_address": (chaîne) adresse email pour cet événement,
  "url": (chaîne) l'url qui a été cliqué (Email Click events seulement),
  "user_agent": (string) description du système de l'utilisateur et du navigateur pour l'événement (Email Click, Open, et les événements MarkAsSpam seulement),
  "ip_pool": (string) pool IP utilisé pour l'envoi de messages
}
```
#### Détails de la propriété
- Le comportement de `dispatch_id` diffère entre Canvas et les campagnes car Braze traite les pas de Canvas (à l'exception des pas d'entrée, qui peuvent être programmés) en tant qu'événements déclenchés, même lorsqu'ils sont "programmés". [En savoir plus sur le comportement de `dispatch_id` dans Canvas et les campagnes ici]({{site.baseurl}}/help/help_articles/data/dispatch_id/).
{% endapi %}

{% api %}

## Évènement de rebond par e-mail

{% apitags %}
Courriel, rebond
{% endapitags %}

Cet événement se produit lorsqu'un fournisseur de services Internet renvoie un bounce dur. Un rebond dur signifie une défaillance de délivrabilité permanente.

```json
// Courriel Bounce: users.messages.email. bondir
{
  "id": (string) id unique de cet événement,
  "user_id": (string) Braze identifiant utilisateur de l'utilisateur,
  "external_user_id": (string) ID externe de l'utilisateur,
  "temps": (int) 10 chiffres heure UTC de l'événement en secondes depuis l'époque,
  "fuseau horaire": (chaîne) IANA fuseau horaire de l'utilisateur au moment de l'événement,
  "campaign_id": (string) id de la campagne si à partir d'une campagne,
  "campaign_name": (string) nom de la campagne,
  "message_variation_id": (string) id de la variation de message si une campagne,
  "canvas_id": (chaîne) id de la toile si une toile
  "canvas_name": (string) nom des Canvas,
  "canvas_variation_id": (string) id de la variation de Canvas dans laquelle l'utilisateur est à partir d'un Canvas,
  "canvas_variation_name": (chaîne) nom de la variation de Canvas dans laquelle l'utilisateur est si à partir d'un Canvas,
  "canvas_step_id": (string) id de l'étape pour ce message si à partir d'un Canvas,
  "canvas_step_name": (string) nom de l'étape pour ce message si à partir d'un Canvas,
  "send_id": (string) id du message si spécifié pour la campagne (Voir Send Identifier under API Identifier Types),
  "dispatch_id": (string) id de l'envoi de message (id unique pour chaque 'transmission' envoyée depuis la plate-forme Braze). Les utilisateurs qui reçoivent un message de planification reçoivent le même dispatch_id. Les messages basés sur l'action ou sur l'API obtiennent un dispatch_id unique par utilisateur.
  "email_address": (chaîne) adresse email pour cet événement
  "sending_ip": (string) l'adresse IP à partir de laquelle le message a été envoyé (Email Delivery, Bounce, et SoftBounce événements seulement. Ne sera affiché que sur les événements si le message a été réellement tenté. Pour certains autres bounces, les informations pourraient être perdues si le serveur du destinataire a déjà accepté le courrier et seulement après la fermeture de la connexion a décidé qu'il ne pouvait pas livrer le courrier),
  "ip_pool": (string) pool IP utilisé pour l'envoi de messages (pour certains cas de rebondissement, Le pool d'IP ne sera pas fourni) ,
  "bounce_reason": (string) raison de rebond fournie par le serveur
}
```
#### Détails de la propriété
- Le comportement de `dispatch_id` diffère entre Canvas et les campagnes car Braze traite les pas de Canvas (à l'exception des pas d'entrée, qui peuvent être programmés) en tant qu'événements déclenchés, même lorsqu'ils sont "programmés". [En savoir plus sur le comportement de `dispatch_id` dans Canvas et les campagnes ici]({{site.baseurl}}/help/help_articles/data/dispatch_id/).
{% endapi %}

{% api %}

## Envoyer un e-mail à l'évènement soft bounce

{% apitags %}
Courriel, rebond
{% endapitags %}

Cet événement se produit lorsqu'un fournisseur de services Internet renvoie un rebond doux. Un rebond souple signifie qu'un e-mail n'a pas pu être envoyé en raison d'une défaillance temporaire de délivrabilité.

```json
// Email Soft Bounce: users.messages.email. oftBounce
{
  "id": (string) id unique de cet événement,
  "user_id": (string) Braze identifiant utilisateur de l'utilisateur,
  "external_user_id": (string) ID externe de l'utilisateur,
  "temps": (int) 10 chiffres heure UTC de l'événement en secondes depuis l'époque,
  "fuseau horaire": (chaîne) IANA fuseau horaire de l'utilisateur au moment de l'événement,
  "campaign_id": (string) id de la campagne si à partir d'une campagne,
  "campaign_name": (string) nom de la campagne,
  "message_variation_id": (string) id de la variation de message si une campagne,
  "canvas_id": (chaîne) id de la toile si une toile
  "canvas_name": (string) nom des Canvas,
  "canvas_variation_id": (string) id de la variation de Canvas dans laquelle l'utilisateur est à partir d'un Canvas,
  "canvas_variation_name": (chaîne) nom de la variation de Canvas dans laquelle l'utilisateur est si à partir d'un Canvas,
  "canvas_step_id": (string) id de l'étape pour ce message si à partir d'un Canvas,
  "canvas_step_name": (string) nom de l'étape pour ce message si à partir d'un Canvas,
  "send_id": (string) id du message si spécifié pour la campagne (Voir Send Identifier under API Identifier Types),
  "dispatch_id": (string) id de l'envoi de message (id unique pour chaque 'transmission' envoyée depuis la plate-forme Braze). Les utilisateurs qui reçoivent un message de planification reçoivent le même dispatch_id. Les messages basés sur l'action ou sur l'API obtiennent un dispatch_id unique par utilisateur.
  "email_address": (chaîne) adresse email pour cet événement
  "sending_ip": (string) l'adresse IP à partir de laquelle le message a été envoyé (Email Delivery, Bounce, et SoftBounce événements seulement. Ne sera affiché que sur les événements si le message a été réellement tenté. Pour certains autres bounces, les informations pourraient être perdues si le serveur du destinataire a déjà accepté le courrier et seulement après la fermeture de la connexion a décidé qu'il ne pouvait pas livrer le courrier),
  "ip_pool": (string) pool IP utilisé pour l'envoi de messages (pour certains cas de rebondissement, Le pool d'IP ne sera pas fourni),
  "bounce_reason": (string) raison de rebond fournie par le serveur
}
```
#### Détails de la propriété
- Le comportement de `dispatch_id` diffère entre Canvas et les campagnes car Braze traite les pas de Canvas (à l'exception des pas d'entrée, qui peuvent être programmés) en tant qu'événements déclenchés, même lorsqu'ils sont "programmés". [En savoir plus sur le comportement de `dispatch_id` dans Canvas et les campagnes ici]({{site.baseurl}}/help/help_articles/data/dispatch_id/).
{% endapi %}

{% api %}

## Événements de spam par e-mail

{% apitags %}
Courriel, spam
{% endapitags %}

Cet événement se produit lorsque l'utilisateur final clique sur le bouton « spam » du courriel. Notez que cela ne représente pas le fait que le courriel est allé dans le dossier spam car Braze ne suit pas cela.

```json
// Email Marquer comme spam : users.messages.email. arkAsSpam
{
  "id": (string) id unique de cet événement,
  "user_id": (string) Braze identifiant utilisateur de l'utilisateur,
  "external_user_id": (string) ID externe de l'utilisateur,
  "temps": (int) 10 chiffres heure UTC de l'événement en secondes depuis l'époque,
  "fuseau horaire": (chaîne) IANA fuseau horaire de l'utilisateur au moment de l'événement,
  "campaign_id": (string) id de la campagne si à partir d'une campagne,
  "campaign_name": (string) nom de la campagne,
  "message_variation_id": (string) id de la variation de message si une campagne,
  "canvas_id": (chaîne) id de la toile si une toile
  "canvas_name": (string) nom des Canvas,
  "canvas_variation_id": (string) id de la variation de Canvas dans laquelle l'utilisateur est à partir d'un Canvas,
  "canvas_variation_name": (chaîne) nom de la variation de Canvas dans laquelle l'utilisateur est si à partir d'un Canvas,
  "canvas_step_id": (string) id de l'étape pour ce message si à partir d'un Canvas,
  "canvas_step_name": (string) nom de l'étape pour ce message si à partir d'un Canvas,
  "send_id": (string) id du message si spécifié pour la campagne (Voir Send Identifier under API Identifier Types),
  "dispatch_id": (string) id de l'envoi de message (id unique pour chaque 'transmission' envoyée depuis la plate-forme Braze). Les utilisateurs qui reçoivent un message de planification reçoivent le même dispatch_id. Les messages basés sur l'action ou sur l'API obtiennent un dispatch_id unique par utilisateur.
  "email_address": (chaîne) adresse email pour cet événement
  "user_agent": (string) description du système de l'utilisateur et du navigateur pour l'événement (Email Click, Open, et les événements MarkAsSpam seulement),
  "ip_pool": (string) pool IP utilisé pour l'envoi de message
}
```
#### Détails de la propriété
- Le comportement de `dispatch_id` diffère entre Canvas et les campagnes car Braze traite les pas de Canvas (à l'exception des pas d'entrée, qui peuvent être programmés) en tant qu'événements déclenchés, même lorsqu'ils sont "programmés". [En savoir plus sur le comportement de `dispatch_id` dans Canvas et les campagnes ici]({{site.baseurl}}/help/help_articles/data/dispatch_id/).
{% endapi %}


{% api %}

## Événements de désinscription par e-mail

{% apitags %}
E-mail, Abonnement
{% endapitags %}

Cet événement se produit lorsque l'utilisateur final a cliqué sur "se désabonner" de l'email.

{% alert important %}
Veuillez noter que l'événement `Se désabonner` est en fait un événement de clic spécialisé qui est déclenché lorsque votre utilisateur _clique sur le lien de désinscription dans l'e-mail_, __pas__ lorsque l'utilisateur change d'état pour se désabonner.
{% endalert %}

```json
// Email Unsubscribe: users.messages.email. nsubscribe
{
  "id": (string) id unique de cet événement,
  "user_id": (string) Braze identifiant utilisateur de l'utilisateur,
  "external_user_id": (string) ID externe de l'utilisateur,
  "temps": (int) 10 chiffres heure UTC de l'événement en secondes depuis l'époque,
  "fuseau horaire": (chaîne) IANA fuseau horaire de l'utilisateur au moment de l'événement,
  "campaign_id": (string) id de la campagne si à partir d'une campagne,
  "campaign_name": (string) nom de la campagne,
  "message_variation_id": (string) id de la variation de message si une campagne,
  "canvas_id": (chaîne) id de la toile si une toile
  "canvas_name": (string) nom des Canvas,
  "canvas_variation_id": (string) id de la variation de Canvas dans laquelle l'utilisateur est à partir d'un Canvas,
  "canvas_variation_name": (chaîne) nom de la variation de Canvas dans laquelle l'utilisateur est si à partir d'un Canvas,
  "canvas_step_id": (string) id de l'étape pour ce message si à partir d'un Canvas,
  "canvas_step_name": (string) nom de l'étape pour ce message si à partir d'un Canvas,
  "send_id": (string) id du message si spécifié pour la campagne (Voir Send Identifier under API Identifier Types),
  "dispatch_id": (string) id de l'envoi de message (id unique pour chaque 'transmission' envoyée depuis la plate-forme Braze). Les utilisateurs qui reçoivent un message de planification reçoivent le même dispatch_id. Les messages basés sur l'action ou sur l'API obtiennent un dispatch_id unique par utilisateur.
  "email_address": (chaîne) adresse email pour cet événement,
  "ip_pool": (chaîne) pool d'IP utilisé pour l'envoi de message
}
```
#### Détails de la propriété
- Le comportement de `dispatch_id` diffère entre Canvas et les campagnes car Braze traite les pas de Canvas (à l'exception des pas d'entrée, qui peuvent être programmés) en tant qu'événements déclenchés, même lorsqu'ils sont "programmés". [En savoir plus sur le comportement de `dispatch_id` dans Canvas et les campagnes ici]({{site.baseurl}}/help/help_articles/data/dispatch_id/).
{% endapi %}

{% api %}

## Événements d'abonnement

{% apitags %}
Abonnement, E-mail, SMS
{% endapitags %}

Cet événement se produit lorsque l'état d'abonnement d'un utilisateur dans un groupe d'abonnement change.

{% alert important %}
Les groupes d'abonnement ne sont actuellement disponibles que pour les canaux de messagerie électronique et SMS.
{% endalert %}

```json
// Changement d'état du groupe d'abonnement: users.behaviors.subscriptiongroup. tateChange
{
  "id": (string) id unique de cet événement,
  "user_id": (string) Braze identifiant utilisateur de l'utilisateur,
  "external_user_id": (string) ID externe de l'utilisateur,
  "canal": (chaîne) soit 'sms' soit 'email',
  "temps": (int) 10 chiffres heure UTC de l'événement en secondes depuis l'époque,
  "fuseau horaire" : (chaîne) IANA fuseau horaire de l'utilisateur au moment de l'événement,
  "app_id": (string) id pour l'application sur laquelle l'action de l'utilisateur s'est produite,
  "campaign_id": (string) id de la campagne si à partir d'une campagne,
  "campaign_name": (string) nom de la campagne,
  "message_variation_id": (string) id de la variation de message si une campagne,
  "canvas_id": (string) id de la Toile si à partir d'une toile,
  "canvas_name": (string) nom de la Toile,
  "canvas_variation_id": (string) id de la variation de Canvas dans laquelle l'utilisateur est si à partir d'un Canvas,
  "canvas_variation_name": (chaîne) nom de la variation de Canvas dans laquelle l'utilisateur est si à partir d'un Canvas,
  "canvas_step_id": (string) id de l'étape pour ce message si à partir d'un Canvas,
  "canvas_step_name": (chaîne) nom de l'étape pour ce message si à partir d'un Canvas,
  "send_id": (string) id du message si spécifié pour la campagne (Voir Send Identifier under API Identifier Types),
  "email_address": (string) adresse email pour cet utilisateur,
  "phone_number": (string) numéro de téléphone de l'utilisateur (présenté dans e. 64 format),
  "subscription_group_id": (string) id du groupe d'abonnement,
  "subscription_status": (string) status de l'abonnement après la modification : 'Subscribed' ou 'Unsubscribed'
}
```
{% endapi %}


{% api %}

## Événements du message dans l'application

{% apitags %}
Messages In-App, Impressions
{% endapitags %}

Cet événement se produit lorsqu'un utilisateur voit un message dans l'application.

```json
// Impression de message dans l'application: users.messages.inappmessage. mpression
{
  "id": (string) id unique de cet événement,
  "user_id": (string) Braze identifiant utilisateur de l'utilisateur,
  "external_user_id": (string) ID externe de l'utilisateur,
  "temps": (int) 10 chiffres heure UTC de l'événement en secondes depuis l'époque,
  "fuseau horaire": (chaîne) IANA fuseau horaire de l'utilisateur au moment de l'événement,
  "campaign_id": (string) id de la campagne si à partir d'une campagne,
  "campaign_name": (string) nom de la campagne,
  "message_variation_id": (string) id de la variation de message si une campagne,
  "canvas_id" : (chaîne) id de la toile si elle provient d'un canvas,
  "canvas_name": (chaîne) nom de la toile,
  "canvas_variation_id": (string) id de la variation de Canvas dans laquelle l'utilisateur est à partir d'un Canvas,
  "canvas_variation_name": (chaîne) nom de la variation de Canvas dans laquelle l'utilisateur est si à partir d'un Canvas,
  "canvas_step_id": (string) id de l'étape pour ce message si à partir d'un Canvas,
  "canvas_step_name": (string) nom de l'étape pour ce message si à partir d'un Canvas,
  "card_id": (string) ID API de la carte de ce message dans l'application,
  "send_id": (string) id du message si spécifié pour la campagne (Voir Send Identifier under API Identifier Types),
  "app_id": (string) id pour l'application sur laquelle l'action de l'utilisateur s'est produite,
  "plate-forme": (chaîne) plate-forme de l'appareil (iOS, Android, web, etc. ,
  "os_version": (string) os version du périphérique utilisé pour l'action,
  "device_model": (string) modèle matériel de l'appareil,
  "device_id": (string) id de l'appareil sur lequel l'événement s'est produit,
  "ad_id": (string) identifiant publicitaire,
  "ad_id_type": (string) Un de 'ios_idfa', 'google_ad_id', 'windows_ad_id', OU 'roku_ad_id',
  "ad_tracking_enabled": (boolean) si le suivi publicitaire est activé pour l'appareil
}
```
#### Détails de la propriété
- Pour `ad_id`, `ad_id_type` et `ad_tracking_enabled`, vous devrez explicitement collecter l'idfa iOS et Android Google adid à travers les SDK natifs. En savoir plus à leur sujet ici : [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/optional_idfa_collection/#optional-idfa-collection/), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id).
- Si vous utilisez Kafka pour ingérer des données de [courants]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/) contactez votre Responsable de la Customer Success ou le Gestionnaire de comptes pour activer la fonction flipper pour envoyer `ad_id`.
{% endapi %}

{% api %}

## Évènements des clics dans le message de l'application

{% apitags %}
Messages dans l'application, clics
{% endapitags %}

Cet événement se produit lorsqu'un utilisateur clique sur un message dans l'application.

```json
// Click Message In-App : users.messages.inappmessage. lick
{
  "id": (string) id unique de cet événement,
  "user_id": (string) Braze identifiant utilisateur de l'utilisateur,
  "external_user_id": (string) ID externe de l'utilisateur,
  "temps": (int) 10 chiffres heure UTC de l'événement en secondes depuis l'époque,
  "fuseau horaire": (chaîne) IANA fuseau horaire de l'utilisateur au moment de l'événement,
  "button_id" : (chaîne) index du bouton cliqué, si c'est un bouton qui a été cliqué, ou un ID de suivi du clic, si l'événement provient d'un appboyBridge. d'invocation ogClick,
  "campaign_id": (string) id de la campagne si à partir d'une campagne,
  "campaign_name": (string) nom de la campagne,
  "message_variation_id": (string) id de la variation de message si une campagne,
  "canvas_id": (chaîne) id de la toile si une toile
  "canvas_name": (string) nom des Canvas,
  "canvas_variation_id": (string) id de la variation de Canvas dans laquelle l'utilisateur est à partir d'un Canvas,
  "canvas_variation_name": (chaîne) nom de la variation de Canvas dans laquelle l'utilisateur est si à partir d'un Canvas,
  "canvas_step_id": (string) id de l'étape pour ce message si à partir d'un Canvas,
  "canvas_step_name": (chaîne) nom de l'étape pour ce message si à partir d'un Canvas,
  "card_id": (string) ID API de la carte de ce message dans l'application,
  "send_id": (string) id du message si spécifié pour la campagne (Voir Send Identifier under API Identifier Types),
  "app_id": (string) id pour l'application sur laquelle l'action de l'utilisateur s'est produite,
  "plate-forme": (chaîne) plate-forme de l'appareil (iOS, Android, web, etc. ,
  "os_version": (string) os version du périphérique utilisé pour l'action,
  "device_model": (string) modèle matériel de l'appareil,
  "device_id": (string) id de l'appareil sur lequel l'événement s'est produit,
  "ad_id": (string) identifiant publicitaire,
  "ad_id_type": (string) Un de 'ios_idfa', 'google_ad_id', 'windows_ad_id', OU 'roku_ad_id',
  "ad_tracking_enabled": (boolean) si le suivi publicitaire est activé pour l'appareil
}
```
#### Détails de la propriété
- Pour `ad_id`, `ad_id_type` et `ad_tracking_enabled`, vous devrez explicitement collecter l'idfa iOS et Android Google adid à travers les SDK natifs. En savoir plus à leur sujet ici : [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/optional_idfa_collection/#optional-idfa-collection/), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id).
- Si vous utilisez Kafka pour ingérer des données de [courants]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/) contactez votre Responsable de la Customer Success ou le Gestionnaire de comptes pour activer la fonction flipper pour envoyer `ad_id`.
{% endapi %}


{% api %}

## Événements d'envoi de Webhook

{% apitags %}
Webhooks, Envoie
{% endapitags %}

Cet événement se produit lorsqu'un webhook a été traité et envoyé à une tierce partie spécifiée dans ce webhook. Notez que cela ne signifie pas si la demande a été reçue ou non.

```json
// Webhook Send: users.messages.webhook. fin
{
  "id": (string) id unique de cet événement,
  "user_id": (string) Braze identifiant utilisateur de l'utilisateur,
  "external_user_id": (string) ID externe de l'utilisateur,
  "temps": (int) 10 chiffres heure UTC de l'événement en secondes depuis l'époque,
  "fuseau horaire": (chaîne) IANA fuseau horaire de l'utilisateur au moment de l'événement,
  "campaign_id": (string) id de la campagne si à partir d'une campagne,
  "campaign_name": (string) nom de la campagne,
  "message_variation_id": (string) id de la variation de message si une campagne,
  "canvas_id": (chaîne) id de la toile si une toile
  "canvas_name": (string) nom des Canvas,
  "canvas_variation_id": (string) id de la variation de Canvas dans laquelle l'utilisateur est à partir d'un Canvas,
  "canvas_variation_name": (chaîne) nom de la variation de Canvas dans laquelle l'utilisateur est si à partir d'un Canvas,
  "canvas_step_id": (string) id de l'étape pour ce message si à partir d'un Canvas,
  "canvas_step_name": (string) nom de l'étape pour ce message si à partir d'un Canvas,
  "send_id": (string) id du message si spécifié pour la campagne (Voir Send Identifier under API Identifier Types)
}
```
{% endapi %}

{% api %}
## Événements d'envoi de la carte de contenu

{% apitags %}
Cartes de Contenu, Envoie
{% endapitags %}

Cet événement se produit quand une fiche de contenu est envoyée à un utilisateur.

```json
// Content Card Send: users.messages.contentcard. fin
{
  "id": (string) id unique de cet événement,
  "user_id": (string) Braze identifiant utilisateur de l'utilisateur,
  "external_user_id": (string) ID externe de l'utilisateur,
  "temps": (int) 10 chiffres heure UTC de l'événement en secondes depuis l'époque,
  "fuseau horaire": (chaîne) IANA fuseau horaire de l'utilisateur au moment de l'événement,
  "content_card_id" : (string) id de la carte de contenu qui a été envoyée,
  "campaign_id": (string) id de la campagne si à partir d'une campagne,
  "campaign_name": (string) nom de la campagne,
  "message_variation_id": (string) id de la variation de message si une campagne,
  "canvas_id": (chaîne) id de la toile si une toile
  "canvas_name": (string) nom des Canvas,
  "canvas_variation_id": (string) id de la variation de Canvas dans laquelle l'utilisateur est à partir d'un Canvas,
  "canvas_variation_name": (chaîne) nom de la variation de Canvas dans laquelle l'utilisateur est si à partir d'un Canvas,
  "canvas_step_id": (string) id de l'étape pour ce message si à partir d'un Canvas,
  "canvas_step_name": (chaîne) nom de l'étape pour ce message si à partir d'un Canvas,
  "send_id": (string) id du message si spécifié pour la campagne (Voir Send Identifier under API Identifier Types),
  "device_id": (string) id de l'appareil sur lequel l'événement s'est produit
}
```

{% endapi %}

{% api %}
## Événements de l'impression de la carte de contenu

{% apitags %}
Cartes de contenu, Impressions
{% endapitags %}

Cet événement se produit lorsqu'un utilisateur voit une fiche de contenu.

```json
// Impression de la carte de contenu : users.messages.contentcard. mpression
{
  "id": (string) id unique de cet événement,
  "user_id": (string) Braze identifiant utilisateur de l'utilisateur,
  "external_user_id": (string) ID externe de l'utilisateur,
  "temps": (int) 10 chiffres heure UTC de l'événement en secondes depuis l'époque,
  "fuseau horaire": (chaîne) IANA fuseau horaire de l'utilisateur au moment de l'événement,
  "app_id": (string) id pour l'application sur laquelle l'action de l'utilisateur s'est produite,
  "content_card_id": (string) id de la carte de contenu qui a été vue/cliquée/rejetée,
  "campaign_id": (string) id de la campagne si à partir d'une campagne,
  "campaign_name": (string) nom de la campagne,
  "message_variation_id": (string) id de la variation de message si une campagne,
  "canvas_id": (string) id de la Toile si à partir d'un Canvas,
  "canvas_name": (string) nom du Canvas,
  "canvas_variation_id": (string) id de la variation de Canvas dans laquelle l'utilisateur est si à partir d'un Canvas,
  "canvas_variation_name": (chaîne) nom de la variation de Canvas dans laquelle l'utilisateur est si à partir d'un Canvas,
  "canvas_step_id": (string) id de l'étape pour ce message si à partir d'un Canvas,
  "canvas_step_name": (chaîne) nom de l'étape pour ce message si à partir d'un Canvas,
  "send_id": (string) id du message si spécifié pour la campagne (Voir Send Identifier under API Identifier Types),
  "plate-forme": (chaîne) plate-forme de l'appareil (iOS, Android, web, etc. ,
  "os_version": (string) os version du périphérique utilisé pour l'action,
  "device_model": (string) modèle matériel de l'appareil,
  "device_id": (string) id de l'appareil sur lequel l'événement s'est produit,
  "ad_id": (string) identifiant publicitaire,
  "ad_id_type": (string) Un de 'ios_idfa', 'google_ad_id', 'windows_ad_id', OU 'roku_ad_id',
  "ad_tracking_enabled": (boolean) si le suivi publicitaire est activé pour l'appareil
}
```
#### Détails de la propriété
- Pour `ad_id`, `ad_id_type` et `ad_tracking_enabled`, vous devrez explicitement collecter l'idfa iOS et Android Google adid à travers les SDK natifs. En savoir plus à leur sujet ici : [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/optional_idfa_collection/#optional-idfa-collection/), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id).
- Si vous utilisez Kafka pour ingérer des données de [courants]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/) contactez votre Responsable de la Customer Success ou le Gestionnaire de comptes pour activer la fonction flipper pour envoyer `ad_id`.
{% endapi %}

{% api %}
## Événements des clics sur la carte de contenu

{% apitags %}
Cartes de contenu, clics
{% endapitags %}

Cet événement se produit lorsqu'un utilisateur clique sur une fiche de contenu.

```json
// Content Card Click: users.messages.contentcard. lick
{
  "id": (string) unique id de cet événement,
  "user_id": (string) Braze identifiant utilisateur de l'utilisateur,
  "external_user_id": (string) ID externe de l'utilisateur,
  "temps": (int) 10 chiffres heure UTC de l'événement en secondes depuis l'époque,
  "fuseau horaire": (chaîne) IANA fuseau horaire de l'utilisateur au moment de l'événement,
  "app_id": (string) id pour l'application sur laquelle l'action de l'utilisateur s'est produite,
  "content_card_id": (string) id de la carte de contenu qui a été vue/cliquée/rejetée,
  "campaign_id": (string) id de la campagne si à partir d'une campagne,
  "campaign_name": (string) nom de la campagne,
  "message_variation_id": (string) id de la variation de message si une campagne,
  "canvas_id": (string) id de la Toile si à partir d'un Canvas,
  "canvas_name": (string) nom du Canvas,
  "canvas_variation_id": (string) id de la variation de Canvas dans laquelle l'utilisateur est si à partir d'un Canvas,
  "canvas_variation_name": (chaîne) nom de la variation de Canvas dans laquelle l'utilisateur est si à partir d'un Canvas,
  "canvas_step_id": (string) id de l'étape pour ce message si à partir d'un Canvas,
  "canvas_step_name": (chaîne) nom de l'étape pour ce message si à partir d'un Canvas,
  "send_id": (string) id du message si spécifié pour la campagne (Voir Send Identifier under API Identifier Types),
  "plate-forme": (chaîne) plate-forme de l'appareil (iOS, Android, web, etc. ,
  "os_version": (string) os version du périphérique utilisé pour l'action,
  "device_model": (string) modèle matériel de l'appareil,
  "device_id": (string) id de l'appareil sur lequel l'événement s'est produit,
  "ad_id": (string) identifiant publicitaire,
  "ad_id_type": (string) Un de 'ios_idfa', 'google_ad_id', 'windows_ad_id', OU 'roku_ad_id',
  "ad_tracking_enabled": (boolean) si le suivi publicitaire est activé pour l'appareil
}
```
#### Détails de la propriété
- Pour `ad_id`, `ad_id_type` et `ad_tracking_enabled`, vous devrez explicitement collecter l'idfa iOS et Android Google adid à travers les SDK natifs. En savoir plus à leur sujet ici : [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/optional_idfa_collection/#optional-idfa-collection/), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id).
- Si vous utilisez Kafka pour ingérer des données de [courants]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/) contactez votre Responsable de la Customer Success ou le Gestionnaire de comptes pour activer la fonction flipper pour envoyer `ad_id`.
{% endapi %}


{% api %}
## Événements de rejet de la carte de contenu

{% apitags %}
Cartes de contenu, licenciement
{% endapitags %}

Cet événement se produit lorsqu'un utilisateur rejette une carte de contenu.

```json
// Content Card Dismiss: users.messages.contentcard. ismiss
{
  "id": (string) id unique de cet événement,
  "user_id": (string) Braze identifiant utilisateur de l'utilisateur,
  "external_user_id": (string) ID externe de l'utilisateur,
  "temps": (int) 10 chiffres heure UTC de l'événement en secondes depuis l'époque,
  "fuseau horaire": (chaîne) IANA fuseau horaire de l'utilisateur au moment de l'événement,
  "app_id": (string) id pour l'application sur laquelle l'action de l'utilisateur s'est produite,
  "content_card_id": (string) id de la carte de contenu qui a été vue/cliquée/rejetée,
  "campaign_id": (string) id de la campagne si à partir d'une campagne,
  "campaign_name": (string) nom de la campagne,
  "message_variation_id": (string) id de la variation de message si une campagne,
  "canvas_id": (string) id de la Toile si à partir d'un Canvas,
  "canvas_name": (string) nom du Canvas,
  "canvas_variation_id": (string) id de la variation de Canvas dans laquelle l'utilisateur est si à partir d'un Canvas,
  "canvas_variation_name": (chaîne) nom de la variation de Canvas dans laquelle l'utilisateur est si à partir d'un Canvas,
  "canvas_step_id": (string) id de l'étape pour ce message si à partir d'un Canvas,
  "canvas_step_name": (chaîne) nom de l'étape pour ce message si à partir d'un Canvas,
  "send_id": (string) id du message si spécifié pour la campagne (Voir Send Identifier under API Identifier Types),
  "plate-forme": (chaîne) plate-forme de l'appareil (iOS, Android, web, etc. ,
  "os_version": (string) os version du périphérique utilisé pour l'action,
  "device_model": (string) modèle matériel de l'appareil,
  "device_id": (string) id de l'appareil sur lequel l'événement s'est produit,
  "ad_id": (string) identifiant publicitaire,
  "ad_id_type": (string) Un de 'ios_idfa', 'google_ad_id', 'windows_ad_id', OU 'roku_ad_id',
  "ad_tracking_enabled": (boolean) si le suivi publicitaire est activé pour l'appareil
}
```
#### Détails de la propriété
- Pour `ad_id`, `ad_id_type` et `ad_tracking_enabled`, vous devrez explicitement collecter l'idfa iOS et Android Google adid à travers les SDK natifs. En savoir plus à leur sujet ici : [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/optional_idfa_collection/#optional-idfa-collection/), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id).
- Si vous utilisez Kafka pour ingérer des données de [courants]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/) contactez votre Responsable de la Customer Success ou le Gestionnaire de comptes pour activer la fonction flipper pour envoyer `ad_id`.
{% endapi %}

{% api %}

## Événement "Infos"

{% apitags %}
Flux d'actualités, Impressions
{% endapitags %}

Cet événement se produit lorsqu'un utilisateur consulte le flux d'actualités.

{% alert tip %}
  Le schéma [Impression du flux d'actualités (`users.behaviors.app. ewsFeedImpression`) est situé dans les événements de comportement client]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/customer_behavior_events/#news-feed-impression-event), car ces données sont catégorisées comme telles, plutôt que d'être catégorisées comme un événement d'engagement de messages.
{% endalert %}

```json
// News Feed Card Impression: users.messages.newsfeedcard. mpression
{
  "id": (string) id unique de cet événement,
  "user_id": (string) Braze identifiant utilisateur de l'utilisateur,
  "external_user_id": (string) ID externe de l'utilisateur,
  "temps": (int) 10 chiffres heure UTC de l'événement en secondes depuis l'époque,
  "fuseau horaire": (chaîne) IANA fuseau horaire de l'utilisateur au moment de l'événement,
  "card_id": (chaîne) id de la carte qui a été consultée,
  "app_id": (string) id pour l'application sur laquelle l'action de l'utilisateur s'est produite,
  "plate-forme": (chaîne) plate-forme de l'appareil (iOS, Android, web, etc. ,
  "os_version": (string) os version du périphérique utilisé pour l'action,
  "device_model": (string) modèle matériel de l'appareil,
  "device_id": (string) id de l'appareil sur lequel l'événement s'est produit
}
```
{% endapi %}


{% api %}

## Cliquez sur les événements du flux d'actualités

{% apitags %}
Flux d'actualités, clics
{% endapitags %}

Cet événement se produit lorsqu'un utilisateur clique sur le fil d'actualité.

{% alert tip %}
  Le schéma [Impression du flux d'actualités (`users.behaviors.app. ewsFeedImpression`) est situé dans les événements de comportement client]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/customer_behavior_events/#news-feed-impression-event), car ces données sont catégorisées comme telles, plutôt que d'être catégorisées comme un événement d'engagement de messages.
{% endalert %}

```json
// News Feed Card Click: users.messages.newsfeedcard. lick
{
  "id": (string) id unique de cet événement,
  "user_id": (string) Braze identifiant utilisateur de l'utilisateur,
  "external_user_id": (string) ID externe de l'utilisateur,
  "temps": (int) 10 chiffres heure UTC de l'événement en secondes depuis l'époque,
  "fuseau horaire": (chaîne) IANA fuseau horaire de l'utilisateur au moment de l'événement,
  "card_id" : (chaîne) id de la carte cliquée,
  "app_id": (string) id pour l'application sur laquelle l'action de l'utilisateur s'est produite,
  "plate-forme": (chaîne) plate-forme de l'appareil (iOS, Android, web, etc. ,
  "os_version": (string) os version du périphérique utilisé pour l'action,
  "device_model": (string) modèle matériel de l'appareil,
  "device_id": (string) id de l'appareil sur lequel l'événement s'est produit
}
```
{% endapi %}

{% api %}

## Envoyer des événements par SMS

{% apitags %}
SMS, Envoie
{% endapitags %}

Cet événement se produit lorsqu'un utilisateur envoie un SMS.

```json
// SMS Send: users.messages.sms. fin
{
  "id": (string) id unique de cet événement,
  "user_id": (string) Braze identifiant utilisateur de l'utilisateur,
  "external_user_id": (string) ID externe de l'utilisateur,
  "temps": (int) 10 chiffres heure UTC de l'événement en secondes depuis l'époque,
  "fuseau horaire": (chaîne) IANA fuseau horaire de l'utilisateur au moment de l'événement,
  "from_phone_number" : (chaîne) le numéro de téléphone du message (Livré et non livré seulement),
  "subscription_group_id": (string) id du groupe d'abonnement ciblé pour ce message SMS,
  "to_phone_number": (chaîne) le numéro auquel le message a été envoyé,
  "campaign_id": (string) id de la campagne si à partir d'une campagne,
  "campaign_name": (string) nom de la campagne,
  "message_variation_id": (string) id de la variation de message si une campagne,
  "canvas_id": (string) id de la Toile si à partir d'un Canvas,
  "canvas_name": (string) nom du Canvas,
  "canvas_variation_id": (string) id de la variation de Canvas dans laquelle l'utilisateur est à partir d'un Canvas,
  "canvas_variation_name": (chaîne) nom de la variation de Canvas dans laquelle l'utilisateur est si à partir d'un Canvas,
  "canvas_step_id": (string) id de l'étape pour ce message si à partir d'un Canvas,
  "canvas_step_name": (chaîne) nom de l'étape pour ce message si à partir d'un Canvas,
  "dispatch_id": (string) id de l'envoi de message (id unique pour chaque 'transmission' envoyée depuis la plateforme Braze et les utilisateurs qui reçoivent un message de planification reçoivent le même dispatch_id. Les messages basés sur l'action ou sur l'API obtiennent un dispatch_id unique par utilisateur
  "send_id": (string) message send ID auquel ce message appartient,
  "catégorie" : (chaîne) Si le SMS a été envoyé à la suite d'une réponse automatique à l'un de vos mots-clés SMS globaux, la Catégorie sera reflétée ici (e. Opt-In, Opt-out, Help) 
}
```
{% endapi %}

{% api %}

## Envoyer des SMS aux événements de l'opérateur

{% apitags %}
SMS, livraison
{% endapitags %}

Cet événement se produit lorsqu'un SMS est envoyé à l'opérateur.

```json
// Livraison de SMS: users.messages.sms. arrierSend
{
  "id": (string) id unique de cet événement,
  "user_id": (string) Braze identifiant utilisateur de l'utilisateur,
  "external_user_id": (string) ID externe de l'utilisateur,
  "temps": (int) 10 chiffres heure UTC de l'événement en secondes depuis l'époque,
  "fuseau horaire": (chaîne) IANA fuseau horaire de l'utilisateur au moment de l'événement,
  "from_phone_number" : (chaîne) le numéro de téléphone du message (Livré et non livré seulement),
  "subscription_group_id": (string) id du groupe d'abonnement ciblé pour ce message SMS,
  "to_phone_number": (chaîne) le numéro auquel le message a été envoyé,
  "campaign_id": (string) id de la campagne si à partir d'une campagne,
  "campaign_name": (string) nom de la campagne,
  "message_variation_id": (string) id de la variation de message si une campagne,
  "canvas_id": (string) id de la Toile si à partir d'un Canvas,
  "canvas_name": (string) nom du Canvas,
  "canvas_variation_id": (string) id de la variation de Canvas dans laquelle l'utilisateur est à partir d'un Canvas,
  "canvas_variation_name": (chaîne) nom de la variation de Canvas dans laquelle l'utilisateur est si à partir d'un Canvas,
  "canvas_step_id": (string) id de l'étape pour ce message si à partir d'un Canvas,
  "canvas_step_name": (chaîne) nom de l'étape pour ce message si à partir d'un Canvas,
  "dispatch_id": (string) id de l'envoi de message (id unique pour chaque 'transmission' envoyée depuis la plateforme Braze et les utilisateurs qui reçoivent un message de planification reçoivent le même dispatch_id. Les messages basés sur l'action ou déclenchés par l'API obtiennent un dispatch_id unique par utilisateur,
  "send_id": (string) message send ID que ce message appartient à
}
```
{% endapi %}

{% api %}

## Événements d'envoi de SMS

{% apitags %}
SMS, livraison
{% endapitags %}

Cet événement se produit lorsqu'un SMS a été envoyé avec succès au téléphone mobile des utilisateurs.

```json
// Livraison de SMS: users.messages.sms. elivery
{
  "id": (string) id unique de cet événement,
  "user_id": (string) Braze identifiant utilisateur de l'utilisateur,
  "external_user_id": (string) ID externe de l'utilisateur,
  "temps": (int) 10 chiffres heure UTC de l'événement en secondes depuis l'époque,
  "fuseau horaire": (chaîne) IANA fuseau horaire de l'utilisateur au moment de l'événement,
  "from_phone_number" : (chaîne) le numéro de téléphone du message (Livré et non livré seulement),
  "subscription_group_id": (string) id du groupe d'abonnement ciblé pour ce message SMS,
  "to_phone_number": (chaîne) le numéro auquel le message a été envoyé,
  "campaign_id": (string) id de la campagne si à partir d'une campagne,
  "campaign_name": (string) nom de la campagne,
  "message_variation_id": (string) id de la variation de message si une campagne,
  "canvas_id": (string) id de la Toile si à partir d'un Canvas,
  "canvas_name": (string) nom du Canvas,
  "canvas_variation_id": (string) id de la variation de Canvas dans laquelle l'utilisateur est à partir d'un Canvas,
  "canvas_variation_name": (chaîne) nom de la variation de Canvas dans laquelle l'utilisateur est si à partir d'un Canvas,
  "canvas_step_id": (string) id de l'étape pour ce message si à partir d'un Canvas,
  "canvas_step_name": (chaîne) nom de l'étape pour ce message si à partir d'un Canvas,
  "dispatch_id": (string) id de l'envoi de message (id unique pour chaque 'transmission' envoyée depuis la plateforme Braze et les utilisateurs qui reçoivent un message de planification reçoivent le même dispatch_id. Les messages basés sur l'action ou déclenchés par l'API obtiennent un dispatch_id unique par utilisateur,
  "send_id": (string) message send ID que ce message appartient à
}
```
{% endapi %}

{% api %}

## Événements de rejet de SMS

{% apitags %}
SMS, Rejet
{% endapitags %}

Cet événement se produit lorsqu'un SMS est rejeté par l'opérateur, cela peut se produire pour plusieurs raisons. Utilisez cet événement et les codes d'erreur fournis pour aider à résoudre les problèmes liés à l'envoi de SMS.

```json
// SMS Rejection: users.messages.sms. ejection
{
  "id": (string) id unique de cet événement,
  "user_id": (string) Braze identifiant utilisateur de l'utilisateur,
  "external_user_id": (string) ID externe de l'utilisateur,
  "temps": (int) 10 chiffres heure UTC de l'événement en secondes depuis l'époque,
  "fuseau horaire": (chaîne) IANA fuseau horaire de l'utilisateur au moment de l'événement,
  "from_phone_number" : (chaîne) le numéro de téléphone du message (Livré et non livré seulement),
  "subscription_group_id": (string) id du groupe d'abonnement ciblé pour ce message SMS,
  "subscription_group_api_id": (string) api id du groupe d'abonnement ciblé pour ce message SMS,
  "to_phone_number": (chaîne) le numéro auquel le message a été envoyé,
  "campaign_id": (string) id de la campagne si à partir d'une campagne,
  "campaign_name": (chaîne) nom de la campagne,
  "message_variation_id": (string) id de la variation du message si une campagne,
  "canvas_id": (string) id de la Toile si à partir d'un Canvas,
  "canvas_name": (string) nom des Canvas,
  "canvas_variation_id": (string) id de la variation de Canvas dans laquelle l'utilisateur est à partir d'un Canvas,
  "canvas_variation_name": (chaîne) nom de la variation de Canvas dans laquelle l'utilisateur est si à partir d'un Canvas,
  "canvas_step_id": (string) id de l'étape pour ce message si à partir d'un Canvas,
  "canvas_step_name": (chaîne) nom de l'étape pour ce message si à partir d'un Canvas,
  "dispatch_id": (string) id de l'envoi de message (id unique pour chaque 'transmission' envoyée depuis la plateforme Braze et les utilisateurs qui reçoivent un message de planification reçoivent le même dispatch_id. Les messages basés sur l'action ou sur l'API obtiennent un dispatch_id unique par utilisateur,
  "send_id": (string) message send ID auquel ce message appartient,
  "erreur" : (chaîne) erreur fournie par Braze (événements de rejet et d'échec de livraison seulement),
  "provider_error_code": (string) le code de raison du fournisseur quant à la raison pour laquelle le message n'a pas été envoyé (événements Rejet et Delivery Failure seulement)
}
```
{% endapi %}


{% api %}

## Événements d'échec d'envoi de SMS

{% apitags %}
SMS, livraison
{% endapitags %}

Cet événement se produit lorsqu'un SMS fait l'expérience de l'échec de l'envoi. Utilisez cet événement et les codes d'erreur fournis pour aider à résoudre les problèmes liés à l'envoi de SMS.

```json
// SMS Delivery Failure: users.messages.sms. eliveryFailure
{
  "id": (string) id unique de cet événement,
  "user_id": (string) Braze identifiant utilisateur de l'utilisateur,
  "external_user_id": (string) ID externe de l'utilisateur,
  "temps": (int) 10 chiffres heure UTC de l'événement en secondes depuis l'époque,
  "fuseau horaire": (chaîne) IANA fuseau horaire de l'utilisateur au moment de l'événement,
  "from_phone_number" : (chaîne) le numéro de téléphone du message (Livré et non livré seulement),
  "subscription_group_id": (string) id du groupe d'abonnement ciblé pour ce message SMS,
  "subscription_group_api_id": (string) api id du groupe d'abonnement ciblé pour ce message SMS,
  "to_phone_number": (chaîne) le numéro auquel le message a été envoyé,
  "campaign_id": (string) id de la campagne si à partir d'une campagne,
  "campaign_name": (chaîne) nom de la campagne,
  "message_variation_id": (string) id de la variation du message si une campagne,
  "canvas_id": (string) id de la Toile si à partir d'un Canvas,
  "canvas_name": (string) nom des Canvas,
  "canvas_variation_id": (string) id de la variation de Canvas dans laquelle l'utilisateur est à partir d'un Canvas,
  "canvas_variation_name": (chaîne) nom de la variation de Canvas dans laquelle l'utilisateur est si à partir d'un Canvas,
  "canvas_step_id": (string) id de l'étape pour ce message si à partir d'un Canvas,
  "canvas_step_name": (chaîne) nom de l'étape pour ce message si à partir d'un Canvas,
  "dispatch_id": (string) id de l'envoi de message (id unique pour chaque 'transmission' envoyée depuis la plateforme Braze et les utilisateurs qui reçoivent un message de planification reçoivent le même dispatch_id. Les messages basés sur l'action ou sur l'API obtiennent un dispatch_id unique par utilisateur,
  "send_id": (string) message send ID auquel ce message appartient,
  "erreur" : (chaîne) erreur fournie par Braze (événements de rejet et d'échec de livraison seulement),
  "provider_error_code": (string) le code de raison du fournisseur quant à la raison pour laquelle le message n'a pas été envoyé (événements Rejet et Delivery Failure seulement)
}
```
{% endapi %}
{% api %}

## Événements SMS reçus

{% apitags %}
SMS, InboundReceived
{% endapitags %}

Cet événement se produit lorsqu'un de vos utilisateurs envoie un SMS à un numéro de téléphone dans l'un de vos groupes d'abonnement SMS Braze. Remarque lorsque Braze reçoit un SMS entrant, nous attribuons ce message entrant à tout utilisateur qui partage ce numéro de téléphone. Par conséquent, vous pouvez recevoir plusieurs événements par message entrant si plusieurs utilisateurs de votre instance Braze partagent le même numéro de téléphone. Si vous avez besoin d'attribution d'identifiants d'utilisateur spécifiques en fonction des messages envoyés à cet utilisateur, vous pouvez utiliser l'événement SMS Delivered pour attribuer les événements entrants à l'ID de l'utilisateur qui a reçu le plus récemment un message de votre numéro Braze. Si nous détectons que ce message entrant est une réponse à une campagne sortante ou une étape de toile envoyée par Braze, Nous inclurons également la campagne ou les métadonnées de toile avec l'événement. Braze définit une réponse comme un message entrant dans les quatre heures suivant un message sortant.

```json
// SMS entrant reçu: users.messages.sms. nboundReceived
{
  "id": (string) id unique de cet événement,
  "user_id": (string) Braze identifiant utilisateur de l'utilisateur,
  "external_user_id": (string) ID externe de l'utilisateur,
  "app_group_id": (chaîne) ID API du groupe d'applications associé au numéro de téléphone entrant,
  "temps": (int) 10 chiffres heure UTC de l'événement en secondes depuis l'époque,
  "user_phone_number" : (chaîne) le numéro de téléphone de l'utilisateur qui a envoyé le message à votre numéro de Braze,
  "subscription_group_id": (string) id du groupe d'abonnement auquel le numéro de téléphone auquel appartient l'utilisateur envoyé,
  "inbound_phone_number": (chaîne) le numéro de téléphone auquel le message a été envoyé,
  "action" : (chaîne) l'action d'abonnement que Braze a prise à la suite de ce message (soit `abonné`, `unsubscribed` ou `none` basé sur le corps du message. `Aucun` indique que ce message entrant ne correspond à aucun de vos mots-clés pour opt-in ou opt-out un utilisateur),
  "message_body" : (chaîne) le corps du message envoyé par l'utilisateur,
  "campaign_id": (string) id de la campagne si Braze identifie ce message entrant est une réponse à une campagne,
  "campaign_name": (chaîne) nom de la campagne,
  "message_variation_id": (string) id de la variation du message si Braze identifie ce message entrant est une réponse à une campagne,
  "canvas_id" : (chaîne) id de la toile si elle provient d'un Canvas,
  "canvas_name" : (chaîne) nom des Canvas
  "canvas_variation_id" : (chaîne) id de la variation de Canvas dans laquelle l'utilisateur est à partir d'un Canvas,
  "canvas_variation_name": (chaîne) nom de la variation de Canvas dans laquelle l'utilisateur est à partir d'un Canvas,
  "canvas_step_id": (string) id de l'étape pour ce message si à partir d'un Canvas,
  "canvas_step_name": (chaîne) nom de l'étape pour ce message si une toile
}
```
{% endapi %}


{% api %}

## Événements de conversion de campagne

{% apitags %}
Campagne, Conversion
{% endapitags %}

Cet événement se produit lorsqu'un utilisateur fait une action qui a été définie comme événement de conversion dans une campagne.

{% alert important %}
Veuillez noter que l'événement de conversion est codé dans le champ `conversion_behavior` qui comprend le type d'événement de conversion, la fenêtre (période de temps) et des informations supplémentaires en fonction du type d'événement de conversion. Le champ `conversion_index` représente quel événement de conversion. i.e., 0 = A, 1 = B, 2 = C, 3 = D.
{% endalert %}

```json
// Événement de conversion de campagne: users.campaigns. onversion
{
  "id": (string) id unique de cet événement,
  "user_id": (string) Braze identifiant utilisateur de l'utilisateur,
  "external_user_id": (string) ID externe de l'utilisateur,
  "temps": (int) 10 chiffres heure UTC de l'événement en secondes depuis l'époque,
  "fuseau horaire": (chaîne) IANA fuseau horaire de l'utilisateur au moment de l'événement,
  "app_id": (string) id pour l'application sur laquelle l'action de l'utilisateur s'est produite,
  "campaign_id": (string) id de la campagne,
  "campaign_name": (chaîne) nom de la campagne,
  "conversion_behavior_index": (int) index du comportement de conversion,
  "conversion_behavior": (chaîne) chaîne encodée en JSON décrivant le comportement de conversion,
  "message_variation_id": (string) id de la variation du message,
  "send_id": (string) id du message si spécifié pour la campagne (Voir Send Identifier under API Identifier Types)
}
```
{% endapi %}


{% api %}

## Événements de conversion de toile

{% apitags %}
Canvas, Conversion
{% endapitags %}

Cet événement se produit lorsqu'un utilisateur fait une action qui a été définie comme un événement de conversion dans canvas.

{% alert important %}
Veuillez noter que l'événement de conversion est codé dans le champ `conversion_behavior` qui comprend le type d'événement de conversion, la fenêtre (période de temps) et des informations supplémentaires en fonction du type d'événement de conversion. Le champ `conversion_index` représente quel événement de conversion. i.e., 0 = A, 1 = B, 2 = C, 3 = D.
{% endalert %}

```json
// Événement de conversion de Canvas : users.canvas. onversion
{
  "id": (string) id unique de cet événement,
  "user_id": (string) Braze identifiant utilisateur de l'utilisateur,
  "external_user_id": (string) ID externe de l'utilisateur,
  "temps": (int) 10 chiffres heure UTC de l'événement en secondes depuis l'époque,
  "fuseau horaire": (chaîne) IANA fuseau horaire de l'utilisateur au moment de l'événement,
  "app_id": (string) id pour l'application sur laquelle l'action de l'utilisateur s'est produite,
  "canvas_id": (chaîne) id de la toile,
  "canvas_name": (chaîne) nom des Canvas,
  "conversion_behavior_index": (int) index du comportement de conversion,
  "conversion_behavior": (string) chaîne encodée en JSON décrivant le comportement de conversion,
  "canvas_variation_id": (string) id de la variation de Canvas dans laquelle l'utilisateur se trouve,
  "canvas_variation_name": (chaîne) nom de la variation de Canvas dans laquelle l'utilisateur est si à partir d'un Canvas,
  "canvas_step_id": (string) id de la dernière étape l'utilisateur a été envoyé avant la conversion
  "canvas_step_name": (string) nom de l'étape pour ce message si à partir d'un Canvas,
}
```
{% endapi %}


{% api %}

## Événements d'entrée sur le canevas

{% apitags %}
Canevas, Entrée
{% endapitags %}

Cet événement se produit lorsqu'un utilisateur entre dans la toile. Cet événement vous indique la variante dans laquelle l'utilisateur a entré.

```json
// Événement Canvas Entrée: users.canvas. ntry
{
  "id": (string) id unique de cet événement,
  "user_id": (string) Braze identifiant utilisateur de l'utilisateur,
  "external_user_id": (string) ID externe de l'utilisateur,
  "temps": (int) 10 chiffres heure UTC de l'événement en secondes depuis l'époque,
  "fuseau horaire": (chaîne) IANA fuseau horaire de l'utilisateur au moment de l'événement,
  "canvas_id" : (chaîne) id du Canvas,
  "canvas_name": (chaîne) nom des Canvas,
  "canvas_variation_id": (chaîne) id de la variation de Canvas dans laquelle l'utilisateur se trouve,
  "canvas_variation_name": (chaîne) nom de la variation de Canvas dans laquelle l'utilisateur est à partir d'un Canvas,
  "canvas_step_name": (string) retournera toujours 'null' pour cet événement d'engagement,
  "canvas_step_id": (string) id de l'étape dans laquelle l'utilisateur a entré,
  "canvas_step_name": (chaîne) nom de l'étape pour ce message si à partir d'un Canvas,
  "in_control_group": (boolean) si l'utilisateur a été inscrit dans le groupe de contrôle pour une Canvas
}
```

{% endapi %}

{% api %}
## Événements d'inscription de groupe de contrôle de campagne

{% apitags %}
Campagne, Entrée
{% endapitags %}

Cet événement se produit lorsqu'un utilisateur est inscrit dans une variante de contrôle définie sur une campagne multi-variantes. Cet événement est généré car il n'y aura pas d'événement d'envoi de canal pour cet utilisateur.

```json
// Inscription au groupe de contrôle de campagne: users.campaigns. nrollInControl
{
  "id": (string) id unique de cet événement,
  "user_id": (string) Braze identifiant utilisateur de l'utilisateur,
  "external_user_id": (string) ID externe de l'utilisateur,
  "app_id": (string) id pour l'application sur laquelle l'action de l'utilisateur s'est produite,
  "temps": (int) 10 chiffres heure UTC de l'événement en secondes depuis l'époque,
  "fuseau horaire" : (chaîne) IANA fuseau horaire de l'utilisateur au moment de l'événement,
  "campaign_id": (string) id de la campagne,
  "campaign_name": (string) nom de la campagne,
  "message_variation_id": (string) id de la variation du message,
  "send_id": (string) id du message si spécifié pour la campagne (Voir Send Identifier under API Identifier Types)
}
```

{% endapi %}

