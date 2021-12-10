---
nav_title: Amplitude des courants
article_title: Amplitude
page_order: 0
alias: /fr/partners/amplitude_for_currents/
description: "Cet article décrit le partenariat entre Braze Currents et Amplitude, une plate-forme d'analyse de produits et d'intelligence d'affaires."
page_type: partenaire
tool: Courants
search_tag: Partenaire
---

# Amplitude des courants

{% include video.html id="7yadPjDImxQ" align="right" %}

> [Amplitude](https://amplitude.com/) est une plate-forme d'analyse de produit et d'intelligence d'affaires. Vous pouvez exporter les événements de données de votre intégration à Braze vers Amplitude afin d'effectuer une analyse approfondie de vos données de produit et de marketing.

Pour commencer, trouvez les informations suivantes dans votre tableau de bord Amplitude :

-   Clé d'API d'Amplitude

Ajoutez cette information à la page d'intégration d'Amplitude sur le tableau de bord, et appuyez sur Enregistrer.

![Amplitude]({% image_buster /assets/img_archive/currents-amplitude-edit.png %})

{% alert warning %}
Gardez votre clé d'Amplitude API à jour. Si les identifiants de votre connecteur expirent, le connecteur arrêtera d'envoyer des événements. Si cela persiste plus de **48 heures**, les événements du connecteur seront supprimés et les données seront définitivement perdues.
{% endalert %}

La documentation d'Amplitude est disponible [ici](https://amplitude.zendesk.com/hc/en-us/articles/115000217351-Appboy-Amplitude-Integration#how-to-set-up-and-use-the-integration).

## Importation des données

En utilisant le partenariat profond de Braze et Amplitude, vous pouvez configurer votre intégration pour importer des cohortes d'Amplitude directement dans Braze pour le reciblage, créer une boucle complète de données d'un système à l'autre. Cela vous permet d'effectuer une analyse profonde en utilisant Amplitude et d'exécuter de façon transparente vos stratégies en utilisant Braze.

Vous pouvez gérer le processus d'import de données d'Amplitude à partir de la page Partenaires de technologie. Notez que toute intégration que vous configurez comptera dans le volume de données de votre compte.

![Import de cohortes d'amplitude]({% image_buster /assets/img_archive/currents-amplitude-import.png %})


## Détails de l'intégration

Une liste des événements qui peuvent être exportés de Braze à Amplitude est ci-dessous. Tous les événements envoyés à Amplitude incluront `external_user_id de l'utilisateur` comme identifiant d'utilisateur Amplitude. Braze enverra uniquement les données d'événement pour les utilisateurs qui ont soit leur set `external_user_id` ou les utilisateurs anonymes qui ont leur ensemble `device_id`. Les propriétés d'événement spécifiques au Brésil seront envoyées sous la clé `event_properties` dans les données envoyées à Amplitude. Les propriétés de chaque type d'événement sont listées ci-dessous.

Vous pouvez exporter deux types d'événements vers Amplitude: "Message Engagement Events" composé des événements Braze qui sont directement liés à l'envoi de messages, et « Événements de comportement client », y compris les autres activités de l'appli ou du site Web telles que les sessions, les événements personnalisés et les achats suivis à travers la plateforme. Tous les événements réguliers sont préfixés par `[Appboy]`, et tous les événements personnalisés sont préfixés par `[Appboy] [Événement personnalisé]`. Les propriétés d'événements personnalisés et l'achat de propriétés d'événements sont préfixés avec `[Propriété d'événement personnalisée]` et `[Achetez la propriété]`, respectivement.

Toutes les cohortes nommées et importées dans Braze seront préfixées avec `[Amplitude]` et suffixées avec leur `cohort_id`. Cela signifie qu'une cohorte nommée "COHORT_NAME" avec le `cohort_id` "cxyzz3hz" sera intitulée `[Amplitude] COHORT_NAME: cxyzz3hz` dans les filtres Braze.

Veuillez contacter votre responsable de compte ou ouvrir un [ticket d'assistance][support] si vous avez besoin d'accéder à d'autres droits d'événement.

### Synchronisations de cohortes planifiées

Les clients de Braze utilisant Amplitude peuvent planifier les synchronisations de cohortes chronométrées entre Amplitude et Braze. Les peut être configurés comme des synchronisations horaires ou quotidiennes de données à envoyer en Brésil.

{% alert important %}
Les synchronisations planifiées n'enverront que les deltas du jeu de données mis à jour.
{% endalert %}


## Limites de taux

Les courants se connectent à l'API HTTP d'Amplitude, qui a une [limite de débit](https://developers.amplitude.com/docs/http-api-v2#upload-limit) de 30 événements/seconde par appareil et une limite non documentée de 500K événements/jour par appareil. Au-delà de ces seuils, l'Amplitude accélérera les événements qui sont enregistrés par le biais de Courants. Si un appareil de votre intégration envoie au-delà de cette limite de taux, vous pouvez rencontrer un délai dans lequel les événements de tous les appareils apparaîtront en Amplitude.

Les appareils ne doivent pas signaler plus de 30 événements/seconde ou 500K événements/jour dans des circonstances normales, et ce modèle d'événement ne devrait se produire qu'en raison d'une intégration mal configurée. Pour éviter ce type de retard, assurez-vous que votre intégration SDK rapporte des événements à un rythme normal, comme indiqué dans nos instructions d'intégration SDK et évitez d'exécuter des tests automatisés qui génèrent de nombreux événements pour un seul périphérique.

## Points de terminaison de l'API du profil utilisateur d'Amplitude

Pour consulter certains des points de terminaison communs de l'API Amplitude, consultez notre [documentation dédiée à l'API Amplitude]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/amplitude/amplitude_user_profile_api/).

## Événements du comportement du client

### Événements personnalisés

```json
// <Custom Event Name>
{
  "app_id": (string) id pour l'application sur laquelle l'action de l'utilisateur s'est produite,
  "plate-forme": (chaîne) plate-forme de l'appareil (iOS, Android, web, etc. ,
  "os_version": (string) os version du périphérique utilisé pour l'action,
  "device_model": (chaîne) modèle matériel du dispositif
}
```

### Événements d'achat

```json
// Achat
{
  "product_id": (string) id du produit acheté (envoyé dans le champ "productId" de l'API HTTP Amplitude),
  "prix": (float) prix du produit (envoyé dans le champ "prix" de l'API HTTP Amplitut),
  "currency": (chaîne) alpha alpha ISO 4217 code de devise à trois lettres,
  "app_id": (string) id pour l'application sur laquelle l'action de l'utilisateur s'est produite,
  "plate-forme": (chaîne) plate-forme de l'appareil (iOS, Android, web, etc.). ,
  "os_version" : (string) os version du périphérique utilisé pour l'action,
  "device_model": (string) modèle matériel du périphérique
}
```

### Événements de session

```json
// Première session
{
  "session_id": (string) id de la session,
  "app_id": (string) id pour l'application sur laquelle l'action de l'utilisateur s'est produite,
  "plate-forme": (chaîne) plate-forme de l'appareil (iOS, Android, web, etc. ,
  "os_version": (string) os version du périphérique utilisé pour l'action,
  "device_model": (string) modèle matériel de l'appareil
}
// Session Start
{
  "session_id": (string) id de la session,
  "app_id": (string) id de l'application sur laquelle l'action de l'utilisateur s'est produite,
  "plate-forme": (chaîne) plate-forme de l'appareil (iOS, Android, web, etc. ,
  "os_version": (string) os version de l'appareil utilisé pour l'action,
  "device_model": (string) modèle matériel de l'appareil
}
// Session End
{
  "session_id": (string) id de la session,
  "durée": (float) secondes session durée,
  "app_id": (string) id pour l'application sur laquelle l'action de l'utilisateur s'est produite,
  "plate-forme": (chaîne) plate-forme de l'appareil (iOS, Android, web, etc. ,
  "os_version": (string) os version du périphérique utilisé pour l'action,
  "device_model": (string) modèle matériel de l'appareil
}
```

### Événements de localisation

```json
// Emplacement
{
  "longitude": (float) longitude de l'emplacement enregistré,
  "latitude": (float) latitude de l'emplacement enregistré,
  "altitude": (float) altitude de l'emplacement enregistré,
  "ll_accuracy": (float) un pourcentage représentant la précision déterminée de l'OS de l'emplacement enregistré,
  "alt_accuracy": (float) altitude précision de l'emplacement enregistré,
  "app_id": (string) id pour l'application sur laquelle l'action de l'utilisateur s'est produite,
  "platform": (chaîne) plate-forme de l'appareil (iOS, Android, web, etc. ,
  "os_version": (string) os version du périphérique utilisé pour l'action,
  "device_model": (chaîne) modèle matériel de l'appareil
}
```

### Installer les événements d'attribution

```json
// Installez Attribution
{
  "source": (string) la source de l'attribution
}
```

## Événements d'engagement de message

### Événements de notification push

```json
// Envoyer une notification
{
  "campaign_id": (string) id de la campagne si à partir d'une campagne,
  "campaign_name": (chaîne) nom de la campagne,
  "message_variation_id": (string) id de la variation du message si une campagne,
  "canvas_id" : (chaîne) id de la toile si elle provient d'un Canvas,
  "canvas_name" : (chaîne) nom des Canvas
  "canvas_variation_id" : (chaîne) id de la variation de Canvas dans laquelle l'utilisateur est à partir d'un Canvas,
  "canvas_step_id": (string) id de l'étape pour ce message si à partir d'un Canvas,
  "send_id": (string) id du message si spécifié pour la campagne (Voir Send Identifier sous REST API Parameter Definitions),
  "app_id": (string) id pour l'application sur laquelle l'action de l'utilisateur s'est produite,
  "plate-forme": (chaîne) plate-forme de l'appareil (iOS, Android, web, etc. ,
  "dispatch_id": (string) id de l'envoi de message (id unique pour chaque 'transmission' envoyée depuis la plate-forme Braze). Les utilisateurs qui reçoivent un message de planification reçoivent le même dispatch_id. Les messages basés sur l'action ou sur l'API obtiennent un dispatch_id unique par utilisateur.
}
// Push Notification Open
{
  "campaign_id": (string) id de la campagne si à partir d'une campagne,
  "campaign_name": (string) nom de la campagne,
  "message_variation_id": (string) id de la variation de message si d'une campagne,
  "canvas_id" : (chaîne) id de la Toile si à partir d'un Canvas,
  "canvas_name": (chaîne) nom du Canvas,
  "canvas_variation_id": (string) id de la variation de Canvas dans laquelle l'utilisateur est à partir d'un Canvas,
  "canvas_step_id": (string) id de l'étape pour ce message si à partir d'un Canvas,
  "send_id": (string) id du message si spécifié pour la campagne (Voir Send Identifier sous REST API Parameter Definitions),
  "app_id": (string) id de l'application sur laquelle l'action de l'utilisateur s'est produite,
  "plate-forme": (chaîne) plate-forme de l'appareil (iOS, Android, web, etc. ,
  "os_version": (string) os version de l'appareil utilisé pour l'action,
  "device_model": (string) modèle matériel de l'appareil,
  "dispatch_id": (string) id de l'envoi de message (id unique pour chaque 'transmission' envoyée depuis la plate-forme Braze). Les utilisateurs qui reçoivent un message de planification reçoivent le même dispatch_id. Les messages basés sur l'action ou sur l'API obtiennent un dispatch_id unique par utilisateur.
}
// Push Notification iOS Premier Ouverture
{
  "campaign_id": (string) id de la campagne si une campagne,
  "campaign_name": (string) nom de la campagne,
  "message_variation_id": (string) id de la variation de message si d'une campagne,
  "canvas_id" : (chaîne) id de la Toile si à partir d'un Canvas,
  "canvas_name": (chaîne) nom du Canvas,
  "canvas_variation_id": (string) id de la variation de Canvas dans laquelle l'utilisateur est à partir d'un Canvas,
  "canvas_step_id": (string) id de l'étape pour ce message si à partir d'un Canvas,
  "send_id": (string) id du message si spécifié pour la campagne (Voir Send Identifier sous REST API Parameter Definitions),
  "app_id": (string) id de l'application sur laquelle l'action de l'utilisateur s'est produite,
  "plate-forme": (chaîne) plate-forme de l'appareil (iOS, Android, web, etc. ,
  "dispatch_id": (string) id de l'envoi de message (id unique pour chaque 'transmission' envoyée depuis la plateforme Braze). Les utilisateurs qui reçoivent un message de planification reçoivent le même dispatch_id. Les messages basés sur l'action ou sur l'API obtiennent un dispatch_id unique par utilisateur.
}
// Push Notification Bounce
{
  "campaign_id": (string) id de la campagne si à partir d'une campagne,
  "campaign_name": (string) nom de la campagne,
  "message_variation_id": (string) id de la variation de message si d'une campagne,
  "canvas_id" : (chaîne) id de la Toile si à partir d'un Canvas,
  "canvas_name": (chaîne) nom du Canvas,
  "canvas_variation_id": (string) id de la variation de Canvas dans laquelle l'utilisateur est à partir d'un Canvas,
  "canvas_step_id": (string) id de l'étape pour ce message si à partir d'un Canvas,
  "send_id": (string) id du message si spécifié pour la campagne (Voir Send Identifier sous REST API Parameter Definitions),
  "app_id": (string) id pour l'application sur laquelle le rebond a eu lieu,
  "plate-forme": (chaîne) plate-forme de l'appareil (iOS, Android, web, etc. ,
  "dispatch_id": (string) id de l'envoi de message (id unique pour chaque 'transmission' envoyée depuis la plateforme Braze). Les utilisateurs qui reçoivent un message de planification reçoivent le même dispatch_id. Les messages basés sur l'action ou sur l'API obtiennent un dispatch_id unique par utilisateur.
}
```

### Événements par e-mail

```json
// Email Send
// Email Delivery
// Email Open
// Email Click
// Email Bounce
// Email Soft Bounce
// Email Mark As Spam
// Email Unsubscribe
{
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (chaîne) nom de la campagne,
  "message_variation_id": (string) id de la variation du message si une campagne,
  "canvas_id": (string) id de la toile si à partir d'une toile,
  "canvas_name": (string) nom des Canvas,
  "canvas_variation_id": (string) id de la variation de Canvas dans laquelle l'utilisateur est si à partir d'un Canvas,
  "canvas_step_id": (string) id de l'étape pour ce message si à partir d'un Canvas,
  "send_id": (string) id du message si spécifié pour la campagne (Voir Send Identifier under REST API Parameter Definitions),
  "dispatch_id": (string) id de l'envoi de message (id unique pour chaque 'transmission' envoyée depuis la plate-forme Braze). Les utilisateurs qui reçoivent un message de planification reçoivent le même dispatch_id. Les messages basés sur l'action ou sur l'API obtiennent un dispatch_id unique par utilisateur.
  "email_address": (chaîne) adresse email pour cet événement
  "url": (chaîne) l'URL qui a été cliquée (Email Click events seulement)
}
```

### Événements SMS
```json
// SMS Envoyer
{
  "campaign_id": (string) id de la campagne si à partir d'une campagne,
  "campaign_name": (chaîne) nom de la campagne,
  "message_variation_id": (string) id de la variation du message si une campagne,
  "canvas_id" : (chaîne) id de la toile si elle provient d'un Canvas,
  "canvas_name" : (chaîne) nom des Canvas
  "canvas_variation_id" : (chaîne) id de la variation de Canvas dans laquelle l'utilisateur est à partir d'un Canvas,
  "canvas_variation_name": (chaîne) nom de la variation de Canvas dans laquelle l'utilisateur est à partir d'un Canvas,
  "canvas_step_id": (string) id de l'étape pour ce message si à partir d'un Canvas,
  "canvas_step_name": (chaîne) nom de l'étape pour ce message si à partir d'un Canvas,
  "dispatch_id": (string) id de l'envoi de message (id unique pour chaque 'transmission' envoyée depuis la plateforme Braze et les utilisateurs qui reçoivent un message de planification obtiennent le même dispatch_id. Les messages basés sur l'action ou sur l'API obtiennent un dispatch_id unique par utilisateur,
  "send_id": (chaîne) id du message si spécifié pour la campagne (Voir Send Identifier sous REST API Parameter Definitions),
  "to_phone_number": (chaîne) le numéro auquel le message a été envoyé,
  "subscription_group_id": (string) api id du groupe d'abonnement ciblé pour ce message SMS,
}

// SMS Send To Carrier
// SMS Delivery
{
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (chaîne) nom de la campagne,
  "message_variation_id": (string) id de la variation du message si une campagne,
  "canvas_id": (chaîne) id de la toile si elle provient d'un Canvas,
  "canvas_name": (chaîne) nom de la toile,
  "canvas_variation_id": (string) id de la variation de Canvas dans laquelle l'utilisateur est à partir d'un Canvas,
  "canvas_variation_name": (chaîne) nom de la variation de Canvas dans laquelle l'utilisateur est si à partir d'un Canvas,
  "canvas_step_id": (string) id de l'étape pour ce message si à partir d'un Canvas,
  "canvas_step_name": (chaîne) nom de l'étape pour ce message si à partir d'un Canvas,
  "dispatch_id": (string) id de l'envoi de message (id unique pour chaque 'transmission' envoyée depuis la plateforme Braze et les utilisateurs qui reçoivent un message de planification reçoivent le même dispatch_id. Les messages basés sur l'action ou sur l'API obtiennent un dispatch_id unique par utilisateur,
  "send_id": (chaîne) id du message si spécifié pour la campagne (Voir Send Identifier sous REST API Parameter Definitions),
  "to_phone_number": (chaîne) le numéro auquel le message a été envoyé,
  "subscription_group_id": (string) api id du groupe d'abonnement ciblé pour ce message SMS,
  "from_phone_number": (chaîne) le numéro de téléphone du message (Livré et non livré seulement),
}

// Rejet SMS
// Échec d'envoi SMS
{
  "campaign_id": (string) id de la campagne si une campagne,
  "campaign_name": (chaîne) nom de la campagne,
  "message_variation_id": (string) id de la variation de message si une campagne,
  "canvas_id": (string) id de la Toile si à partir d'un Canvas,
  "canvas_name": (string) nom du Canvas,
  "canvas_variation_id": (string) id de la variation de Canvas dans laquelle l'utilisateur est si à partir d'un Canvas,
  "canvas_variation_name": (chaîne) nom de la variation de Canvas dans laquelle l'utilisateur est si à partir d'un Canvas,
  "canvas_step_id": (string) id de l'étape pour ce message si à partir d'un Canvas,
  "canvas_step_name": (chaîne) nom de l'étape pour ce message si à partir d'un Canvas,
  "dispatch_id": (string) id de l'envoi de message (id unique pour chaque 'transmission' envoyée depuis la plateforme Braze et les utilisateurs qui reçoivent un message de planification reçoivent le même dispatch_id. Les messages basés sur l'action ou sur l'API obtiennent un dispatch_id unique par utilisateur,
  "send_id": (chaîne) id du message si spécifié pour la campagne (Voir Send Identifier sous REST API Parameter Definitions),
  "to_phone_number": (chaîne) le numéro auquel le message a été envoyé,
  "subscription_group_id": (string) api id du groupe d'abonnement ciblé pour ce message SMS,
  "from_phone_number": (chaîne) le numéro de téléphone du message (Livré et non livré seulement),
  "error": (chaîne) Message d'erreur pour le rejet ou l'échec de la livraison,
  "provider_error_code": (string) Code d'erreur pour le rejet ou l'échec de livraison,
}
```



### Événements d'abonnement

```json
// Changement d'état du groupe d'abonnement
{
  "campaign_id": (string) id de la campagne si à partir d'une campagne,
  "campaign_name": (chaîne) nom de la campagne,
  "message_variation_id": (string) id de la variation du message si une campagne,
  "canvas_id" : (chaîne) id de la toile si à partir d'une toile,
  "canvas_name" : (chaîne) nom des Canvas
  "canvas_variation_id" : (chaîne) id de la variation de Canvas dans laquelle l'utilisateur est à partir d'un Canvas,
  "canvas_step_id": (string) id de l'étape pour ce message si à partir d'un Canvas,
  "send_id": (string) id du message si spécifié pour la campagne (Voir Send Identifier sous REST API Parameter Definitions),
  "email_address": (chaîne) adresse email pour cet événement,
  "subscription_group_id": (string) id du groupe d'abonnement,
  "subscription_status": (string) status de l'abonnement après la modification : 'Subscribed' ou 'Unsubscribed'
}
```

### Événements des messages dans l'application

```json
// Impression de message In-App
{
  "campaign_id": (string) id de la campagne si à partir d'une campagne,
  "campaign_name": (chaîne) nom de la campagne,
  "message_variation_id": (string) id de la variation de message si depuis une campagne,
  "canvas_id" : (chaîne) id de la toile si elle provient d'un Canvas,
  "canvas_name" : (chaîne) nom des Canvas
  "canvas_variation_id" : (chaîne) id de la variation de Canvas dans laquelle l'utilisateur est à partir d'un Canvas,
  "canvas_step_id": (string) id de l'étape pour ce message si à partir d'un Canvas,
  "send_id": (string) id du message si spécifié pour la campagne (Voir Send Identifier sous REST API Parameter Definitions),
  "app_id": (string) id pour l'application sur laquelle l'action de l'utilisateur s'est produite,
  "plate-forme": (chaîne) plate-forme de l'appareil (iOS, Android, web, etc. ,
  "os_version": (string) os version de l'appareil utilisé pour l'action,
  "device_model": (string) modèle matériel de l'appareil
}
// Message In-App Cliquez sur
{
  "button_id": (string) index du bouton cliqué, si c'est un bouton qui a été cliqué, ou un ID de suivi du clic, si l'événement provient d'un appboyBridge. d'invocation ogClick,
  "campaign_id": (string) id de la campagne si à partir d'une campagne,
  "campaign_name": (string) nom de la campagne,
  "message_variation_id": (string) id de la variation de message si une campagne,
  "canvas_id": (chaîne) id de la toile si elle provient d'un canvas,
  "canvas_name": (chaîne) nom de la toile,
  "canvas_variation_id": (string) id de la variation de Canvas dans laquelle l'utilisateur est à partir d'un Canvas,
  "canvas_step_id": (string) id de l'étape pour ce message si à partir d'un Canvas,
  "send_id": (string) id du message si spécifié pour la campagne (Voir Send Identifier sous REST API Parameter Definitions),
  "app_id": (string) id pour l'application sur laquelle l'action de l'utilisateur s'est produite,
  "plate-forme": (chaîne) plate-forme de l'appareil (iOS, Android, web, etc. ,
  "os_version": (string) os version du périphérique utilisé pour l'action,
  "device_model": (string) modèle matériel de l'appareil
}
```

### Événements du Webhook

```json
// Webhook Send
{
  "campaign_id": (string) id de la campagne si à partir d'une campagne,
  "campaign_name": (chaîne) nom de la campagne,
  "message_variation_id": (string) id de la variation de message si depuis une campagne,
  "canvas_id" : (chaîne) id de la toile si elle provient d'un Canvas,
  "canvas_name" : (chaîne) nom des Canvas
  "canvas_variation_id" : (chaîne) id de la variation de Canvas dans laquelle l'utilisateur est à partir d'un Canvas,
  "canvas_step_id": (string) id de l'étape pour ce message si à partir d'un Canvas,
  "send_id": (string) id du message si spécifié pour la campagne (Voir Send Identifier sous REST API Parameter Definitions)
}
```

### Événements de la carte de contenu

```json
// Envoyer la fiche de contenu
{
  "card_id": (string) id de la carte de contenu qui a été envoyée,
  "campaign_id": (string) id de la campagne si à partir d'une campagne,
  "campaign_name": (chaîne) nom de la campagne,
  "message_variation_id": (string) id de la variation du message si une campagne,
  "canvas_id" : (chaîne) id de la Toile si à partir d'un Canvas,
  "canvas_name" : (chaîne) nom des Canvas
  "canvas_variation_id": (string) id de la variation de Canvas dans laquelle l'utilisateur est à partir d'un Canvas,
  "canvas_step_id": (string) id de l'étape pour ce message si à partir d'un Canvas,
  "send_id": (string) id du message si spécifié pour la campagne (Voir Send Identifier sous REST API Parameter Definitions)
}
```

```json
// Impression de la Carte de Contenu
// Clic de la Carte de Contenu
// Rejeter la Carte de Contenu
{
  "card_id": (string) id de la carte de contenu qui a été vue/cliquée/rejetée,
  "app_id": (string) id pour l'application sur laquelle l'action de l'utilisateur s'est produite,
  "campaign_id": (string) id de la campagne si à partir d'une campagne,
  "campaign_name": (string) nom de la campagne,
  "message_variation_id": (string) id de la variation de message si depuis une campagne,
  "canvas_id" : (chaîne) id de la toile si elle provient d'un Canvas,
  "canvas_name" : (chaîne) nom des Canvas
  "canvas_variation_id": (string) id de la variation de Canvas dans laquelle l'utilisateur est à partir d'un Canvas,
  "canvas_step_id": (string) id de l'étape pour ce message si à partir d'un Canvas,
  "send_id": (string) id du message si spécifié pour la campagne (Voir Send Identifier under REST API Parameter Definitions),
  "plate-forme": (chaîne) plate-forme de l'appareil (iOS, Android, web, etc. ,
  "os_version": (string) os version de l'appareil utilisé pour l'action,
  "device_model": (string) modèle matériel de l'appareil
}
```

### Événements du flux d'actualités

```json
// Impression de la carte de flux d'actualités
{
  "card_id": (string) id de la carte qui a été visualisée,
  "app_id": (string) id pour l'application sur laquelle l'action de l'utilisateur s'est produite,
  "plate-forme": (chaîne) plate-forme de l'appareil (iOS, Android, web, etc. ,
  "os_version": (string) os version du périphérique utilisé pour l'action,
  "device_model": (string) modèle matériel de l'appareil
}
// News Feed Card Click
{
  "card_id": (string) id de la carte cliquée,
  "app_id": (string) id de l'application sur laquelle l'action de l'utilisateur s'est produite,
  "plate-forme": (chaîne) plate-forme de l'appareil (iOS, Android, web, etc. ,
  "os_version": (string) os version de l'appareil utilisé pour l'action,
  "device_model": (string) modèle matériel de l'appareil
}
// News Feed Impression
{
  "app_id": (string) id pour l'application sur laquelle l'action de l'utilisateur s'est produite,
  "plate-forme": (chaîne) plate-forme de l'appareil (iOS, Android, web, etc. ,
  "os_version": (string) os version de l'appareil utilisé pour l'action,
  "device_model": (string) modèle matériel du périphérique
}
```

### Désinstaller les événements

```json
// Désinstaller
{
  "app_id": (string) id pour l'application sur laquelle l'action de l'utilisateur s'est produite
}
```

### Événements de conversion

```json
// Événement de conversion de campagne
{
  "campaign_id": (string) id de la campagne,
  "campaign_name": (string) nom de la campagne,
  "conversion_behavior_index": (int) index du comportement de conversion,
  "conversion_behavior": (chaîne) chaîne encodée en JSON décrivant le comportement de conversion,
  "message_variation_id": (string) id de la variation du message,
  "send_id": (string) id du message si spécifié pour la campagne (Voir Send Identifier sous REST API Parameter Definitions)
}
// Canvas Conversion Event
{
  "canvas_id": (string) id of the Canvas,
  "canvas_name": (string) nom des Canvas,
  "conversion_behavior_index": (int) index du comportement de conversion,
  "conversion_behavior": (string) chaîne encodée en JSON décrivant le comportement de conversion,
  "canvas_variation_id": (string) id de la variation de Canvas dans laquelle l'utilisateur se trouve,
  "canvas_step_id": (string) id de la dernière étape l'utilisateur a été envoyé avant la conversion
}
```

### Événements d'entrée sur le canevas

```json
// Entrée Canvas
{
  "canvas_id": (string) id des Canvas,
  "canvas_name": (string) nom des Canvas,
  "canvas_variation_id": (string) id de la variation de Canvas dans laquelle l'utilisateur se trouve,
  "in_control_group" : (boolean) si l'utilisateur a été inscrit dans le groupe de contrôle d'une Canvas
}
```

### Événements d'inscription à la campagne

```json
// Inscription de groupe de contrôle de campagne
{
  "campaign_id": (string) id de la campagne,
  "campaign_name": (string) nom de la campagne,
  "message_variation_id": (string) id de la variation du message,
  "send_id": (chaîne) id du message si spécifié pour la campagne (Voir Send Identifier sous REST API Parameter Definitions)
}
```

[support]: {{site.baseurl}}/braze_support/
