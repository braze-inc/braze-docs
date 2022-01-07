---
nav_title: Mixpanel pour les courants
article_title: Mixpanel pour les courants
page_order: 0
alias: /fr/partners/mixpanel_for_currents/
description: "Cet article décrit le partenariat entre Braze Currents et Mixpanel, une plate-forme d'analyse des affaires."
page_type: partenaire
search_tag: Partenaire
tool: Courants
---

# Mixpanel pour les courants

> [Mixpanel](https://mixpanel.com/) est une plateforme d'analyse commerciale qui vous permet d'exporter des événements de Braze vers Mixpanel pour effectuer une analyse plus approfondie. Les données collectées peuvent ensuite être utilisées pour construire des rapports personnalisés et mesurer l'engagement et la rétention des utilisateurs.

Pour commencer, trouvez les informations suivantes dans votre tableau de bord Mixpanel dans le menu `Paramètres > Paramètres du projet`:

-   Secret API Mixpanel
-   Jeton Mixpanel

Ajoutez ces informations à la page d'intégration de Mixpanel Currents sur le tableau de bord, et appuyez sur Enregistrer.

![Mixpanel]({% image_buster /assets/img_archive/currents-mixpanel-edit.png %})

{% alert important %}
Il est important de garder votre API Mixpanel Secret et jeton Mixpanel à jour ; si les identifiants de votre connecteur expirent, le connecteur cessera d'envoyer des événements. Si cela persiste plus de **48 heures**, les événements du connecteur seront supprimés et les données seront définitivement perdues.
{% endalert %}

## Détails de l'intégration

Une liste des événements qui peuvent être exportés de Braze vers Mixpanel est ci-dessous. Tous les événements envoyés à Mixpanel incluront `external_user_id de l'utilisateur` en tant qu'ID Distinct de Mixpanel. En ce moment, Braze n'envoie pas de données d'événement pour les utilisateurs qui n'ont pas leur `external_user_id`.

Vous pouvez exporter deux types d'événements vers Mixpanel: "Message Engagement Events" composé des événements Braze qui sont directement liés à l'envoi de messages, et « Événements de comportement client », y compris les autres activités de l'appli ou du site Web telles que les sessions, les événements personnalisés et les achats suivis à travers la plateforme. Tous les événements personnalisés sont préfixés par `[événement personnalisé Braze]`. Les propriétés d'événements personnalisés et l'achat de propriétés d'événements sont préfixés avec `[Propriété d'événement personnalisée]` et `[Achetez la propriété]`, respectivement.

Veuillez contacter votre responsable de compte ou ouvrir un [ticket d'assistance][support] si vous avez besoin d'accéder à d'autres droits d'événement.

## Import de cohortes Mixpanel

Utilisez le partenariat de Braze et Mixpanel pour configurer votre intégration et importer des cohortes Mixpanel directement dans Braze pour le reargeting, créer une boucle complète de données d'un système à l'autre. Cela vous permet d'effectuer une analyse plus approfondie à l'aide de Mixpanel et d'exécuter de façon transparente vos stratégies en utilisant Braze.

Vous pouvez gérer le processus d'import de Mixpanel Cohort à partir de la page des partenaires technologiques de votre compte Braze. Toute intégration que vous avez configurée comptera dans le volume de données de votre compte.

![Importation de cohortes Mixpanel]({% image_buster /assets/img_archive/currents-mixpanel-import.png %})

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
  "product_id": (string) id du produit acheté (envoyé dans le champ "productId" de Mixpanel HTTP API),
  "prix": (float) prix du produit (envoyé dans le champ "prix" de Mixpanel HTTP API),
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

### Désinstaller les événements

```json
// Désinstaller
{
  "app_id": (string) id pour l'application sur laquelle l'action de l'utilisateur s'est produite
}
```

## Événements d'engagement de message

### Événements de notification push

```json
// Envoyer une notification
{
  "campaign_id": (string) id de la campagne si à partir d'une campagne,
  "campaign_name": (chaîne) nom de la campagne,
  "message_variation_id": (string) id de la variation de message si depuis une campagne,
  "canvas_id" : (chaîne) id de la toile si elle provient d'un Canvas,
  "canvas_name" : (chaîne) nom des Canvas
  "canvas_variation_id" : (chaîne) id de la variation de Canvas dans laquelle l'utilisateur est à partir d'un Canvas,
  "canvas_step_id": (string) id de l'étape pour ce message si à partir d'un Canvas,
  "send_id": (string) id du message si spécifié pour la campagne (Voir Envoyer l'identifiant sous les types de l'API),
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
  "send_id": (chaîne) id du message si spécifié pour la campagne (Voir Envoyer l'identifiant sous les types de l'API),
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
  "send_id": (chaîne) id du message si spécifié pour la campagne (Voir Envoyer l'identifiant sous les types de l'API),
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
  "send_id": (chaîne) id du message si spécifié pour la campagne (Voir Envoyer l'identifiant sous les types de l'API),
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
  "send_id": (string) id du message si spécifié pour la campagne (Voir Send Identifier under API Identifier Types),
  "dispatch_id": (string) id de l'envoi de message (id unique pour chaque 'transmission' envoyée depuis la plate-forme Braze). Les utilisateurs qui reçoivent un message de planification reçoivent le même dispatch_id. Les messages basés sur l'action ou sur l'API obtiennent un dispatch_id unique par utilisateur.
  "email_address": (chaîne) adresse email pour cet événement,
  "url": (chaîne) l'URL qui a été cliquée (Email Click events seulement),
  "user_agent": (string) description du système et du navigateur de l'utilisateur pour l'événement (Email Click, Ouvrir et MarkAsSpam seulement),
  "link_id": (chaîne) valeur unique générée par Braze pour l'URL (Email Click events seulement),
  "link_alias": (chaîne) nom d'alias défini lors de l'envoi du message (Email Click events seulement),
  "machine_open": (chaîne) Indicateur pour savoir si le courrier électronique a été ouvert par un processus automatisé, tel qu'Apple ou Google mail pre-fetching. Actuellement "vrai" ou nul, mais une granularité supplémentaire (par exemple "Apple" ou "Google" pour indiquer quel processus a fait le fetch) peut être ajoutée dans le futur. (Évènements ouverts seulement)
}
```

Le comportement de `dispatch_id` diffère entre Canvas et les campagnes car Braze traite les pas de Canvas (à l'exception des pas d'entrée, qui peuvent être programmés) en tant qu'événements déclenchés, même lorsqu'ils sont "programmés". En savoir plus sur le comportement de [`dispatch_id`]({{site.baseurl}}/help/help_articles/data/dispatch_id/) dans les campagnes et Canvases. Pour plus d'informations, reportez-vous au [comportement client et événements utilisateur]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/customer_behavior_events/) et [événements d'engagement de message]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events/).


### Événements SMS

```json
// SMS Envoyer
{
  "campaign_id": (string) id de la campagne si à partir d'une campagne,
  "campaign_name": (chaîne) nom de la campagne,
  "message_variation_id": (string) id de la variation du message si une campagne,
  "canvas_id" : (chaîne) id de la toile si à partir d'une toile,
  "canvas_name" : (chaîne) nom des Canvas
  "canvas_variation_id" : (chaîne) id de la variation de Canvas dans laquelle l'utilisateur est à partir d'un Canvas,
  "canvas_variation_name": (chaîne) nom de la variation de Canvas dans laquelle l'utilisateur est à partir d'un Canvas,
  "canvas_step_id": (string) id de l'étape pour ce message si à partir d'un Canvas,
  "canvas_step_name": (chaîne) nom de l'étape pour ce message si à partir d'un Canvas,
  "send_id": (string) id du message si spécifié pour la campagne (Voir Envoyer l'identifiant sous les types de l'API),
  "dispatch_id": (string) id de l'envoi de message (id unique pour chaque 'transmission' envoyée depuis la plate-forme Braze). Les utilisateurs qui reçoivent un message de planification reçoivent le même dispatch_id. Les messages basés sur l'action ou sur l'API obtiennent un dispatch_id unique par utilisateur.
  "to_phone_number": (chaîne) le numéro auquel le message a été envoyé,
  "subscription_group_id": (string) api id du groupe d'abonnement ciblé pour ce message SMS,
}

// SMS Send To Carrier
// SMS Delivery
{
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (chaîne) nom de la campagne,
  "message_variation_id": (string) id de la variation du message si une campagne,
  "canvas_id": (chaîne) id de la toile si elle provient d'une toile,
  "canvas_name": (chaîne) nom de la toile,
  "canvas_variation_id": (string) id de la variation de Canvas dans laquelle l'utilisateur est à partir d'un Canvas,
  "canvas_variation_name": (chaîne) nom de la variation de Canvas dans laquelle l'utilisateur est si à partir d'un Canvas,
  "canvas_step_id": (string) id de l'étape pour ce message si à partir d'un Canvas,
  "canvas_step_name": (string) nom de l'étape pour ce message si à partir d'un Canvas,
  "send_id": (string) id du message si spécifié pour la campagne (Voir Send Identifier under API Identifier Types),
  "dispatch_id": (string) id de l'envoi de message (id unique pour chaque 'transmission' envoyée depuis la plate-forme Braze). Les utilisateurs qui reçoivent un message de planification reçoivent le même dispatch_id. Les messages basés sur l'action ou sur l'API obtiennent un dispatch_id unique par utilisateur.
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
  "canvas_id": (string) id de la toile si une toile
  "canvas_name": (string) nom des Canvas,
  "canvas_variation_id": (string) id de la variation de Canvas dans laquelle l'utilisateur est à partir d'un Canvas,
  "canvas_variation_name": (chaîne) nom de la variation de Canvas dans laquelle l'utilisateur est si à partir d'un Canvas,
  "canvas_step_id": (string) id de l'étape pour ce message si à partir d'un Canvas,
  "canvas_step_name": (chaîne) nom de l'étape pour ce message si à partir d'un Canvas,
  "send_id": (string) id du message si spécifié pour la campagne (Voir Send Identifier under API Identifier Types),
  "dispatch_id": (string) id de l'envoi de message (id unique pour chaque 'transmission' envoyée depuis la plate-forme Braze). Les utilisateurs qui reçoivent un message de planification reçoivent le même dispatch_id. Les messages basés sur l'action ou sur l'API obtiennent un dispatch_id unique par utilisateur.
  "to_phone_number": (chaîne) le numéro auquel le message a été envoyé,
  "subscription_group_id": (string) api id du groupe d'abonnement ciblé pour ce message SMS,
  "error": (chaîne) Message d'erreur pour le rejet ou l'échec de la livraison,
  "provider_error_code": (string) Code d'erreur pour l'échec de rejet ou de livraison,
}

// SMS reçu entrant
{
  "inbound_phone_number": (string) numéro de téléphone sur lequel le message a été reçu,
  "subscription_group_id": (string) api id du groupe d'abonnement duquel ce message SMS a été reçu,
  "user_phone_number": (chaîne) le nombre à partir duquel le message a été envoyé,
  "action": (chaîne) l'action d'abonnement Braze a pris suite à ce message (soit `abonné`, `unsubscribed` ou `none` basé sur le corps du message. `Aucun` indique que ce message entrant ne correspond à aucun de vos mots-clés pour opt-in ou opt-out un utilisateur),
  "message_body": (chaîne) le texte du message,
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
  "send_id": (string) id du message si spécifié pour la campagne (Voir Envoyer l'identifiant sous les types de l'API),
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
  "send_id": (string) id du message si spécifié pour la campagne (Voir Envoyer l'identifiant sous les types de l'API),
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
  "send_id": (string) id du message si spécifié pour la campagne (Voir Send Identifier under API Identifier Types),
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
  "send_id": (string) id du message si spécifié pour la campagne (Voir Envoyer l'identifiant sous les types API Identifier)
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
  "send_id": (string) id du message si spécifié pour la campagne (Voir Envoyer l'identifiant sous les types API Identifiants)
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
  "send_id": (string) id du message si spécifié pour la campagne (Voir Send Identifier under API Identifier Types),
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

### Événements de conversion

```json
// Événement de conversion de campagne
{
  "campaign_id": (string) id de la campagne,
  "campaign_name": (string) nom de la campagne,
  "conversion_behavior_index": (int) index du comportement de conversion,
  "conversion_behavior": (chaîne) chaîne encodée en JSON décrivant le comportement de conversion,
  "message_variation_id": (string) id de la variation du message,
  "send_id": (string) id du message si spécifié pour la campagne (Voir Send Identifier under API Identifier Types)
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
  "send_id": (chaîne) id du message si spécifié pour la campagne (Voir Send Identifier under API Identifier Types)
}
```

[support]: {{site.baseurl}}/braze_support/