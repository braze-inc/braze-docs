---
nav_title: "Référence des tables SQL"
article_title: Référence des tables SQL
page_order: 3
page_type: reference
toc_headers: h2
description: "Cet article contient les tables et les colonnes disponibles pour être interrogées dans le générateur de requêtes ou lors de la génération d'extensions de segments SQL."
tool: Segments
---

<style>
table td {
   word-break: keep-all;
}
</style>

# Référence des tables SQL

Cette page est une référence des tables et des colonnes disponibles pour être interrogées dans le [générateur de requêtes]({{site.baseurl}}/user_guide/analytics/query_builder/) ou lors de la génération d'[extensions de segments SQL.]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/) 

## Sommaire

Tableau | Description
------|------------
[CATALOGS_ITEMS_SHARED](#CATALOGS_ITEMS_SHARED) | Articles de catalogue non supprimés
[CHANGELOGS_GLOBALCONTROLGROUP_SHARED](#CHANGELOGS_GLOBALCONTROLGROUP_SHARED) | Lorsque le groupe de contrôle global est modifié
[USERS_BEHAVIORS_CUSTOMEVENT_SHARED](#USERS_BEHAVIORS_CUSTOMEVENT_SHARED) | Lorsqu’un utilisateur effectue un événement personnalisé
[USERS_BEHAVIORS_INSTALLATTRIBUTION_SHARED](#USERS_BEHAVIORS_INSTALLATTRIBUTION_SHARED) | Lorsqu’un utilisateur installe une application et que nous l’attribuons à un partenaire
[USERS_BEHAVIORS_LOCATION_SHARED](#USERS_BEHAVIORS_LOCATION_SHARED) | Lorsqu’un utilisateur enregistre un emplacement
[USERS_BEHAVIORS_PURCHASE_SHARED](#USERS_BEHAVIORS_PURCHASE_SHARED) | Lorsqu’un utilisateur effectue un achat
[USERS_BEHAVIORS_UNINSTALL_SHARED](#USERS_BEHAVIORS_UNINSTALL_SHARED) | Lorsqu’un utilisateur désinstalle une application
[USERS_BEHAVIORS_UPGRADEDAPP_SHARED](#USERS_BEHAVIORS_UPGRADEDAPP_SHARED) | Lorsqu’un utilisateur met à niveau l’application
[USERS_BEHAVIORS_APP_FIRSTSESSION_SHARED](#USERS_BEHAVIORS_APP_FIRSTSESSION_SHARED) | Lorsqu’un utilisateur effectue sa première session
[USERS_BEHAVIORS_APP_NEWSFEEDIMPRESSION_SHARED](#USERS_BEHAVIORS_APP_NEWSFEEDIMPRESSION_SHARED) | Lorsqu’un utilisateur consulte le fil d’actualité
[USERS_BEHAVIORS_APP_SESSIONEND_SHARED](#USERS_BEHAVIORS_APP_SESSIONEND_SHARED) | Lorsqu’un utilisateur termine une session sur une application
[USERS_BEHAVIORS_APP_SESSIONSTART_SHARED](#USERS_BEHAVIORS_APP_SESSIONSTART_SHARED) | Lorsqu’un utilisateur débute une session sur une application
[USERS_BEHAVIORS_GEOFENCE_DATAEVENT_SHARED](#USERS_BEHAVIORS_GEOFENCE_DATAEVENT_SHARED) | Lorsqu'un utilisateur déclenche une zone de géorepérage (par exemple, lorsqu'il entre ou sort d'un géorepérage). Cet événement a été regroupé avec d'autres événements et reçu par l'intermédiaire du point de terminaison des événements standard ; il est donc possible que le point de terminaison ne l'ait pas reçu en temps réel.
[USERS_BEHAVIORS_GEOFENCE_RECORDEVENT_SHARED](#USERS_BEHAVIORS_GEOFENCE_RECORDEVENT_SHARED) | Lorsqu'un utilisateur déclenche une zone de géorepérage (par exemple, lorsqu'il entre ou sort d'un géorepérage). Cet événement a été reçu par l'endpoint de géorepérage dédié et est donc reçu en temps réel dès que l'appareil d'un utilisateur détecte qu'il a déclenché un géorepérage. <br><br>En outre, en raison de la limitation du taux sur l’endpoint géorepérage, il est possible que certains événements de géorepérage ne soient pas reflétés en tant que RecordEvent. Cependant, tous les événements de géorepérage sont représentés par DataEvent (mais avec potentiellement un certain retard dû au traitement par lots).
[USERS_BEHAVIORS_LIVEACTIVITY_PUSHTOSTARTTOKENCHANGE_SHARED](#USERS_BEHAVIORS_LIVEACTIVITY_PUSHTOSTARTTOKENCHANGE_SHARED) | Lorsqu'un jeton de production/instantané d'une activité en direct change
[USERS_BEHAVIORS_LIVEACTIVITY_UPDATETOKENCHANGE_SHARED](#USERS_BEHAVIORS_LIVEACTIVITY_UPDATETOKENCHANGE_SHARED) | Lorsque le jeton de mise à jour d'une activité en ligne/instantanée change
[USERS_BEHAVIORS_PUSHNOTIFICATION_TOKENSTATECHANGE_SHARED](#USERS_BEHAVIORS_PUSHNOTIFICATION_TOKENSTATECHANGE_SHARED) | Lorsque l'état d'un jeton de notification push change
[USERS_BEHAVIORS_SUBSCRIPTION_GLOBALSTATECHANGE_SHARED](#USERS_BEHAVIORS_SUBSCRIPTION_GLOBALSTATECHANGE_SHARED) | Lorsqu’un utilisateur est abonné ou désabonné globalement d’un canal tel que l’e-mail
[USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED](#USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED) | Lorsqu’un utilisateur est abonné ou désabonné d’un groupe d’abonnement
[USERS_CAMPAIGNS_CONVERSION_SHARED](#USERS_CAMPAIGNS_CONVERSION_SHARED) | Lorsqu’un utilisateur se convertit pour une campagne
[USERS_CAMPAIGNS_ENROLLINCONTROL_SHARED](#USERS_CAMPAIGNS_ENROLLINCONTROL_SHARED) | Lorsqu’un utilisateur est inscrit dans le groupe de contrôle d’une campagne
[USERS_CAMPAIGNS_FREQUENCYCAP_SHARED](#USERS_CAMPAIGNS_FREQUENCYCAP_SHARED) | Lorsqu’un utilisateur atteint une limite de fréquence pour une campagne
[USERS_CAMPAIGNS_REVENUE_SHARED](#USERS_CAMPAIGNS_REVENUE_SHARED) | Lorsqu'un utilisateur génère des chiffres d'affaires au cours de la période de conversion primaire.
[USERS_CANVASSTEP_PROGRESSION_SHARED](#USERS_CANVASSTEP_PROGRESSION_SHARED) | Lorsqu'un utilisateur passe à une étape du canvas
[USERS_CANVAS_CONVERSION_SHARED](#USERS_CANVAS_CONVERSION_SHARED) | Lorsqu'un utilisateur effectue une conversion dans le cadre d'un événement de conversion Canvas
[USERS_CANVAS_ENTRY_SHARED](#USERS_CANVAS_ENTRY_SHARED) | Lorsqu'un utilisateur entre dans un Canvas
[USERS_CANVAS_EXIT_MATCHEDAUDIENCE_SHARED](#USERS_CANVAS_EXIT_MATCHEDAUDIENCE_SHARED) | Lorsqu'un utilisateur quitte un canvas parce qu'il correspond aux critères de sortie de l'audience
[USERS_CANVAS_EXIT_PERFORMEDEVENT_SHARED](#USERS_CANVAS_EXIT_PERFORMEDEVENT_SHARED) | Lorsqu'un utilisateur quitte un canvas parce qu'il a effectué un événement d'exception
[USERS_CANVAS_EXPERIMENTSTEP_CONVERSION_SHARED](#USERS_CANVAS_EXPERIMENTSTEP_CONVERSION_SHARED) | Lorsqu'un utilisateur se convertit pour une étape de l'expérience Canvas
[USERS_CANVAS_EXPERIMENTSTEP_SPLITENTRY_SHARED](#USERS_CANVAS_EXPERIMENTSTEP_SPLITENTRY_SHARED) | Lorsqu'un utilisateur entre dans une étape d’expérience
[USERS_CANVAS_FREQUENCYCAP_SHARED](#USERS_CANVAS_FREQUENCYCAP_SHARED) | Lorsqu'un utilisateur se voit imposer une limite de fréquence pour une étape du canvas
[USERS_CANVAS_REVENUE_SHARED](#USERS_CANVAS_REVENUE_SHARED) | Lorsqu'un utilisateur génère des chiffres d'affaires au cours de la période de l'événement de conversion principal.
[USERS_MESSAGES_BANNER_ABORT_SHARED](#USERS_MESSAGES_BANNER_ABORT_SHARED) | Un message de bannière initialement planifié a été annulé pour une raison quelconque.
[USERS_MESSAGES_BANNER_CLICK_SHARED](#USERS_MESSAGES_BANNER_CLICK_SHARED) | Lorsqu'un utilisateur clique sur une bannière
[USERS_MESSAGES_BANNER_IMPRESSION_SHARED](#USERS_MESSAGES_BANNER_IMPRESSION_SHARED) | Lorsqu'un utilisateur visualise une bannière
[USERS_MESSAGES_CONTENTCARD_ABORT_SHARED](#USERS_MESSAGES_CONTENTCARD_ABORT_SHARED) | Un message de carte de contenu initialement planifié a été abandonné pour une raison quelconque.
[USERS_MESSAGES_CONTENTCARD_CLICK_SHARED](#USERS_MESSAGES_CONTENTCARD_CLICK_SHARED) | Lorsqu’un utilisateur clique sur une carte de contenu
[USERS_MESSAGES_CONTENTCARD_DISMISS_SHARED](#USERS_MESSAGES_CONTENTCARD_DISMISS_SHARED) | Lorsqu’un utilisateur rejette une carte de contenu
[USERS_MESSAGES_CONTENTCARD_IMPRESSION_SHARED](#USERS_MESSAGES_CONTENTCARD_IMPRESSION_SHARED) | Lorsqu’un utilisateur affiche une carte de contenu
[USERS_MESSAGES_CONTENTCARD_SEND_SHARED](#USERS_MESSAGES_CONTENTCARD_SEND_SHARED) | Lorsque nous envoyons une carte de contenu à un utilisateur
[USERS_MESSAGES_EMAIL_ABORT_SHARED](#USERS_MESSAGES_EMAIL_ABORT_SHARED) | Un e-mail initialement planifié a été abandonné pour une raison quelconque.
[USERS_MESSAGES_EMAIL_BOUNCE_SHARED](#USERS_MESSAGES_EMAIL_BOUNCE_SHARED) | Un fournisseur de services de courrier électronique a renvoyé un échec d'envoi définitif. Un échec d'envoi définitif est un échec permanent de la livrabilité.
[USERS_MESSAGES_EMAIL_CLICK_SHARED](#USERS_MESSAGES_EMAIL_CLICK_SHARED) | Lorsqu’un utilisateur a cliqué sur un lien dans un e-mail
[USERS_MESSAGES_EMAIL_DEFERRAL_SHARED](#USERS_MESSAGES_EMAIL_DEFERRAL_SHARED) | Lorsqu'un e-mail est différé
[USERS_MESSAGES_EMAIL_DELIVERY_SHARED](#USERS_MESSAGES_EMAIL_DELIVERY_SHARED) | Lorsqu’un e-mail est livré
[USERS_MESSAGES_EMAIL_MARKASSPAM_SHARED](#USERS_MESSAGES_EMAIL_MARKASSPAM_SHARED) | Lorsqu’un un e-mail est désigné comme étant du spam
[USERS_MESSAGES_EMAIL_OPEN_SHARED](#USERS_MESSAGES_EMAIL_OPEN_SHARED) | Lorsqu’un utilisateur ouvre un e-mail
[USERS_MESSAGES_EMAIL_SEND_SHARED](#USERS_MESSAGES_EMAIL_SEND_SHARED) | Lorsque nous envoyons un e-mail à un utilisateur
[USERS_MESSAGES_EMAIL_SOFTBOUNCE_SHARED](#USERS_MESSAGES_EMAIL_SOFTBOUNCE_SHARED) | Lorsqu’un e-mail subit un rebond doux
[USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED](#USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED) | Lorsqu’un utilisateur se désabonne de l’e-mail
[USERS_MESSAGES_FEATUREFLAG_IMPRESSION_SHARED](#USERS_MESSAGES_FEATUREFLAG_IMPRESSION_SHARED) | Lorsqu'un utilisateur consulte un indicateur de fonctionnalité
[USERS_MESSAGES_INAPPMESSAGE_ABORT_SHARED](#USERS_MESSAGES_INAPPMESSAGE_ABORT_SHARED) | Un message in-app initialement planifié a été abandonné pour une raison quelconque.
[USERS_MESSAGES_INAPPMESSAGE_CLICK_SHARED](#USERS_MESSAGES_INAPPMESSAGE_CLICK_SHARED) | Lorsqu’un utilisateur clique sur un message in-app
[USERS_MESSAGES_INAPPMESSAGE_IMPRESSION_SHARED](#USERS_MESSAGES_INAPPMESSAGE_IMPRESSION_SHARED) | Lorsqu’un utilisateur affiche un message in-app
[USERS_MESSAGES_LINE_ABORT_SHARED](#USERS_MESSAGES_LINE_ABORT_SHARED) | Lorsqu'un message LINE planifié ne peut pas être envoyé, avant de l'envoyer à LINE
[USERS_MESSAGES_LINE_CLICK_SHARED](#USERS_MESSAGES_LINE_CLICK_SHARED) | Lorsqu'un utilisateur clique sur un lien dans un message LINE
[USERS_MESSAGES_LINE_INBOUNDRECEIVE_SHARED](#USERS_MESSAGES_LINE_INBOUNDRECEIVE_SHARED) | Lorsqu'un message LINE est reçu d'un utilisateur
[USERS_MESSAGES_LINE_SEND_SHARED](#USERS_MESSAGES_LINE_SEND_SHARED) | Lorsqu'un message LINE est envoyé à LINE
[USERS_MESSAGES_LIVEACTIVITY_OUTCOME_SHARED](#USERS_MESSAGES_LIVEACTIVITY_OUTCOME_SHARED) | Lorsqu'une ligne/en production/instantanée a un événement de résultat
[USERS_MESSAGES_LIVEACTIVITY_SEND_SHARED](#USERS_MESSAGES_LIVEACTIVITY_SEND_SHARED) | Lorsqu'un message de production/instantané est envoyé
[USERS_MESSAGES_NEWSFEEDCARD_ABORT_SHARED](#USERS_MESSAGES_NEWSFEEDCARD_ABORT_SHARED) | Un message de la carte du fil d'actualité initialement planifié a été annulé pour une raison quelconque.
[USERS_MESSAGES_NEWSFEEDCARD_CLICK_SHARED](#USERS_MESSAGES_NEWSFEEDCARD_CLICK_SHARED) | Lorsqu’un utilisateur clique sur une carte de fil d’actualité
[USERS_MESSAGES_NEWSFEEDCARD_IMPRESSION_SHARED](#USERS_MESSAGES_NEWSFEEDCARD_IMPRESSION_SHARED) | Lorsqu’un utilisateur affiche une carte de fil d’actualité
[USERS_MESSAGES_PUSHNOTIFICATION_ABORT_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_ABORT_SHARED) | Un message de notification push initialement planifié a été abandonné pour une raison quelconque.
[USERS_MESSAGES_PUSHNOTIFICATION_BOUNCE_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_BOUNCE_SHARED) | Lorsqu’une notifications push rebondit
[USERS_MESSAGES_PUSHNOTIFICATION_INFLUENCEDOPEN_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_INFLUENCEDOPEN_SHARED) | Lorsqu’un utilisateur ouvre l’application après avoir reçu une notification sans cliquer sur elle
[USERS_MESSAGES_PUSHNOTIFICATION_IOSFOREGROUND_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_IOSFOREGROUND_SHARED) | Lorsqu'un utilisateur reçoit une notification push alors que l'appli est ouverte. <br><br>Cet événement n'est pas pris en charge par le [SDK Swift](https://github.com/braze-inc/braze-swift-sdk) et est obsolète dans le [SDK Obj-C.](https://github.com/Appboy/appboy-ios-sdk)
[USERS_MESSAGES_PUSHNOTIFICATION_OPEN_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_OPEN_SHARED) | Lorsqu'un utilisateur ouvre une notification push ou clique sur un bouton de notification push (y compris un bouton CLOSE qui n'ouvre PAS l'appli). <br><br> Les boutons d'action push ont des résultats multiples. Les actions « Non », « Refuser » et « Annuler » correspondent à des « clics », et les actions « Accepter » correspondent à des « ouvertures ». Les deux sont conseillés dans ce tableau, mais on peut les distinguer dans la colonne **BUTTON_ACTION_TYPE** colonne. Par exemple, une requête peut être utilisée pour regrouper en fonction d'un `BUTTON_ACTION_TYPE` qui n'est ni Non, ni Refuser, ni Annuler.
[USERS_MESSAGES_PUSHNOTIFICATION_SEND_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_SEND_SHARED) | Lorsque nous envoyons une notification push à un utilisateur
[USERS_MESSAGES_RCS_ABORT_SHARED](#USERS_MESSAGES_RCS_ABORT_SHARED) | Lorsqu'un envoi RCS est interrompu en raison d'une erreur détectée dans Braze et que le message est abandonné
[USERS_MESSAGES_RCS_CLICK_SHARED](#USERS_MESSAGES_RCS_CLICK_SHARED) | Lorsque l'utilisateur final interagit avec un message RCS en tapant ou en cliquant sur un élément de l'interface utilisateur.
[USERS_MESSAGES_RCS_DELIVERY_SHARED](#USERS_MESSAGES_RCS_DELIVERY_SHARED) | Lorsqu'un message RCS est envoyé avec succès à l'appareil mobile d'un utilisateur final
[USERS_MESSAGES_RCS_INBOUNDRECEIVE_SHARED](#USERS_MESSAGES_RCS_INBOUNDRECEIVE_SHARED) | Lorsque Braze reçoit un message RCS provenant de l'utilisateur final
[USERS_MESSAGES_RCS_READ_SHARED](#USERS_MESSAGES_RCS_READ_SHARED) | Lorsque l'utilisateur final ouvre un message RCS sur son appareil
[USERS_MESSAGES_RCS_REJECTION_SHARED](#USERS_MESSAGES_RCS_REJECTION_SHARED) | Lorsqu'un message RCS n'est pas délivré en raison d'une intervention du transporteur
[USERS_MESSAGES_RCS_SEND_SHARED](#USERS_MESSAGES_RCS_SEND_SHARED) | Lorsqu'un message RCS est envoyé par les systèmes de Braze aux partenaires de réception/distribution du dernier kilomètre.
[USERS_MESSAGES_SMS_ABORT_SHARED](#USERS_MESSAGES_SMS_ABORT_SHARED) | Un message SMS initialement planifié a été abandonné pour une raison quelconque.
[USERS_MESSAGES_SMS_CARRIERSEND_SHARED](#USERS_MESSAGES_SMS_CARRIERSEND_SHARED) | Lorsqu'un message SMS est envoyé à l'opérateur
[USERS_MESSAGES_SMS_DELIVERY_SHARED](#USERS_MESSAGES_SMS_DELIVERY_SHARED) | Lorsqu’un message SMS est livré
[USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED](#USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED) | Lorsque Braze n’est pas en mesure de livrer le message SMS au fournisseur de services SMS
[USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED](#USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED) | Lorsqu’un message SMS est reçu d’un utilisateur
[USERS_MESSAGES_SMS_REJECTION_SHARED](#USERS_MESSAGES_SMS_REJECTION_SHARED) | Lorsqu’un message SMS n’est pas livré à un utilisateur
[USERS_MESSAGES_SMS_SEND_SHARED](#USERS_MESSAGES_SMS_SEND_SHARED) | Lorsqu’un message SMS est envoyé
[USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED](#USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED) | Lorsqu’un utilisateur clique sur une URL raccourcie Braze incluse dans un message SMS
[USERS_MESSAGES_WEBHOOK_ABORT_SHARED](#USERS_MESSAGES_WEBHOOK_ABORT_SHARED) | Un message webhook initialement planifié a été interrompu pour une raison quelconque.
[USERS_MESSAGES_WEBHOOK_FAILURE_SHARED](#USERS_MESSAGES_WEBHOOK_FAILURE_SHARED) | Lorsqu'un message webhook est envoyé mais qu'il échoue avec une réponse d'erreur de l'endpoint
[USERS_MESSAGES_WEBHOOK_SEND_SHARED](#USERS_MESSAGES_WEBHOOK_SEND_SHARED) | Lorsque nous envoyons un webhook pour un utilisateur
[USERS_MESSAGES_WHATSAPP_ABORT_SHARED](#USERS_MESSAGES_WHATSAPP_ABORT_SHARED) | Un message WhatsApp initialement planifié a été annulé pour une raison quelconque.
[USERS_MESSAGES_WHATSAPP_CLICK_SHARED](#USERS_MESSAGES_WHATSAPP_CLICK_SHARED) | Lorsqu'un utilisateur clique sur un lien ou un bouton dans un message WhatsApp.
[USERS_MESSAGES_WHATSAPP_DELIVERY_SHARED](#USERS_MESSAGES_WHATSAPP_DELIVERY_SHARED) |Lors de l'envoi d'un message WhatsApp
[USERS_MESSAGES_WHATSAPP_FAILURE_SHARED](#USERS_MESSAGES_WHATSAPP_FAILURE_SHARED) | Lorsqu'un message WhatsApp n'est pas envoyé à un utilisateur
[USERS_MESSAGES_WHATSAPP_INBOUNDRECEIVE_SHARED](#USERS_MESSAGES_WHATSAPP_INBOUNDRECEIVE_SHARED) | Lorsqu'un message WhatsApp est reçu d'un utilisateur
[USERS_MESSAGES_WHATSAPP_READ_SHARED](#USERS_MESSAGES_WHATSAPP_READ_SHARED) | Lorsqu'un utilisateur ouvre un message WhatsApp
[USERS_MESSAGES_WHATSAPP_SEND_SHARED](#USERS_MESSAGES_WHATSAPP_SEND_SHARED) | Lorsque nous envoyons un message WhatsApp pour un utilisateur
[USERS_RANDOMBUCKETNUMBERUPDATE_SHARED](#USERS_RANDOMBUCKETNUMBERUPDATE_SHARED) | Lorsque le numéro de compartiment aléatoire d'un utilisateur est modifié
[USERS_USERDELETEREQUEST_SHARED](#USERS_USERDELETEREQUEST_SHARED) | Lorsqu'un utilisateur est supprimé à la demande d'un client
[USERS_USERORPHAN_SHARED](#USERS_USERORPHAN_SHARED) | Lorsqu'un utilisateur est fusionné avec le profil d'un autre utilisateur et que le profil d'origine est orphelin


## Catalogues

### CATALOGS_ITEMS_SHARED {#CATALOGS_ITEMS_SHARED}

Champ | Type | Description
------|------|------------
`catalog_id` | `string` | ID BSON du catalogue
`item_id` | `string` | BSON ID de l'élément du catalogue
`app_group_id` | `null,` `string` | BSON ID du groupe d'applications
`app_group_api_id` | `null,` `string` | ID API du groupe d'applications
`field_name` | `null,` `string` | Nom du champ
`field_value` | `null,` `string` | Valeur du champ
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Journal des modifications

### CHANGELOGS_GLOBALCONTROLGROUP_SHARED {#CHANGELOGS_GLOBALCONTROLGROUP_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`app_group_id` | `null,` `string` | BSON ID du groupe d'applications auquel appartient cet utilisateur
`app_group_api_id` | `null,` `string` | ID API du groupe d'applications auquel appartient cet utilisateur
`time` | `int` | Horodatage UNIX auquel l'événement s'est produit
`random_bucket_number` | `null, int` | Nouveau numéro de compartiment aléatoire
`global_control_group` | `null, boolean` | Avec cette modification, le numéro de compartiment est inclus dans le groupe de contrôle global.
`previous_global_control_group` | `null, boolean` | Avant cette modification, le numéro de compartiment était inclus dans le groupe de contrôle global, mais ce n'est plus le cas.
`sf_created_at` | `timestamp`, `null` | lorsque cet événement a été repris par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


## Comportements

### USERS_BEHAVIORS_CUSTOMEVENT_SHARED {#USERS_BEHAVIORS_CUSTOMEVENT_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé l'événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`app_api_id` | `null,` `string` | ID API de l’application sur laquelle cette action s’est produite
`time` | `int` | Horodatage Unix du moment où l’utilisateur a effectué l’événement
`gender` | `null,` `string` | [Sexe de l'utilisateur
`country` | `null,` `string` | [Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [Langue de l'utilisateur
`device_id` | `null,` `string` | ID de l’appareil sur lequel l’événement personnalisé s’est produit
`sdk_version` | `null,` `string` | Version du SDK de Braze utilisée lors de l'événement
`platform` | `null,` `string` | Plate-forme de l'appareil
`os_version` | `null,` `string` | Version du système d'exploitation de l'appareil
`device_model` | `null,` `string` | Modèle de l'appareil
`name` | `string` | Nom de l'événement personnalisé
`properties` | `string` | Propriétés personnalisées de l'événement stockées sous la forme d'une chaîne de caractères codée en JSON.
`ad_id` | `null,` `string` | [Identifiant publicitaire
`ad_id_type` | `null,` `string` | Un parmi `ios_idfa`, `google_ad_id`, `windows_ad_id` OU `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Si le suivi publicitaire est activé pour l’appareil ou non
`app_group_id` | `null,` `string` | BSON ID du groupe d'applications auquel appartient cet utilisateur
`sf_created_at` | `timestamp`, `null` | lorsque cet événement a été repris par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_INSTALLATTRIBUTION_SHARED {#USERS_BEHAVIORS_INSTALLATTRIBUTION_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a procédé à l'installation
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`device_id` | `null,` `string` | `device_id` qui est lié à cet utilisateur si celui-ci est anonyme
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`time` | `int` | Horodatage Unix du moment où l’utilisateur a installé
`source` | `string` | la source de l'attribution
`app_group_id` | `null,` `string` | BSON ID du groupe d'applications auquel appartient cet utilisateur
`sf_created_at` | `timestamp`, `null` | lorsque cet événement a été repris par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_LOCATION_SHARED {#USERS_BEHAVIORS_LOCATION_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui enregistre l'emplacement/localisation
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`app_api_id` | `null,` `string` | ID API de l’application sur laquelle ce lieu a été enregistré
`time` | `int` | Date/heure Unix à laquelle la localisation a été enregistrée
`latitude` | `float` | [PII] Latitude de l'emplacement/localisation enregistré
`longitude` | `float` | [Longitude de l'emplacement/localisation enregistré
`altitude` | `null, float` | [PII] altitude de l'emplacement/localisation enregistré
`ll_accuracy` | `null, float` | précision de la latitude et longitude du lieu enregistré
`alt_accuracy` | `null, float` | précision de l’altitude du lieu enregistré
`device_id` | `null,` `string` | ID de l’appareil sur lequel la localisation a été enregistrée
`sdk_version` | `null,` `string` | Version du SDK de Braze utilisée lors de l'enregistrement de l'emplacement/localisation.
`platform` | `null,` `string` | Plate-forme de l'appareil
`os_version` | `null,` `string` | Version du système d'exploitation de l'appareil
`device_model` | `null,` `string` | Modèle de l'appareil
`ad_id` | `null,` `string` | [Identifiant publicitaire
`ad_id_type` | `null,` `string` | Un parmi `ios_idfa`, `google_ad_id`, `windows_ad_id` OU `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Si le suivi publicitaire est activé pour l’appareil ou non
`app_group_id` | `null,` `string` | BSON ID du groupe d'applications auquel appartient cet utilisateur
`sf_created_at` | `timestamp`, `null` | lorsque cet événement a été repris par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_PURCHASE_SHARED {#USERS_BEHAVIORS_PURCHASE_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a effectué un achat
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`app_api_id` | `null,` `string` | ID API de l’application sur laquelle l’achat a eu lieu
`time` | `int` | Horodatage Unix du moment où l’utilisateur a effectué l’achat
`device_id` | `null,` `string` | ID de l’appareil sur lequel l’achat s’est produit
`sdk_version` | `null,` `string` | Version du SDK de Braze utilisée lors de l'achat
`platform` | `null,` `string` | Plate-forme de l'appareil
`os_version` | `null,` `string` | Version du système d'exploitation de l'appareil
`device_model` | `null,` `string` | Modèle de l'appareil
`product_id` | `string` | identifiant du produit acheté
`price` | `float` | Prix d'achat
`currency` | `string` | Monnaie d'achat
`properties` | `string` | Propriétés personnalisées de l'achat stockées sous la forme d'une chaîne de caractères codée en JSON.
`ad_id` | `null,` `string` | [Identifiant publicitaire
`ad_id_type` | `null,` `string` | Un parmi `ios_idfa`, `google_ad_id`, `windows_ad_id` OU `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Si le suivi publicitaire est activé pour l’appareil ou non
`app_group_id` | `null,` `string` | BSON ID du groupe d'applications auquel appartient cet utilisateur
`sf_created_at` | `timestamp`, `null` | lorsque cet événement a été repris par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_UNINSTALL_SHARED {#USERS_BEHAVIORS_UNINSTALL_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a procédé à la désinstallation
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`device_id` | `null,` `string` | `device_id` qui est lié à cet utilisateur si celui-ci est anonyme
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`app_api_id` | `null,` `string` | ID API de l’application qui a été désinstallée
`time` | `int` | Horodatage Unix du moment où l’utilisateur a désinstallé
`app_group_id` | `null,` `string` | BSON ID du groupe d'applications auquel appartient cet utilisateur
`sf_created_at` | `timestamp`, `null` | lorsque cet événement a été repris par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_UPGRADEDAPP_SHARED {#USERS_BEHAVIORS_UPGRADEDAPP_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a mis à jour l'application
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`app_api_id` | `null,` `string` | ID API de l’application mise à niveau par l’utilisateur
`time` | `int` | Horodatage Unix du moment où l’utilisateur a mis à niveau l’application
`device_id` | `null,` `string` | ID de l’appareil sur lequel l’utilisateur a mis à niveau l’application
`sdk_version` | `null,` `string` | Version du SDK de Braze utilisée
`platform` | `null,` `string` | Plate-forme de l'appareil
`os_version` | `null,` `string` | Version du système d'exploitation de l'appareil
`device_model` | `null,` `string` | Modèle de l'appareil
`old_app_version` | `null,` `string` | Ancienne version de l'application
`new_app_version` | `null,` `string` | Nouvelle version de l'application
`app_group_id` | `null,` `string` | BSON ID du groupe d'applications auquel appartient cet utilisateur
`sf_created_at` | `timestamp`, `null` | lorsque cet événement a été repris par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_APP_FIRSTSESSION_SHARED {#USERS_BEHAVIORS_APP_FIRSTSESSION_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui effectue cette action
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`app_api_id` | `null,` `string` | ID API de l’application sur laquelle cette session s’est produite
`time` | `int` | Horodatage Unix du moment où la session a commencé
`session_id` | `string` | UUID de la session
`gender` | `null,` `string` | [Sexe de l'utilisateur
`country` | `null,` `string` | [Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [Langue de l'utilisateur
`device_id` | `null,` `string` | ID de l’appareil sur lequel la session s’est produite
`sdk_version` | `null,` `string` | Version du SDK de Braze utilisée pendant la session
`platform` | `null,` `string` | Plate-forme de l'appareil
`os_version` | `null,` `string` | Version du système d'exploitation de l'appareil
`device_model` | `null,` `string` | Modèle de l'appareil
`app_group_id` | `null,` `string` | BSON ID du groupe d'applications auquel appartient cet utilisateur
`sf_created_at` | `timestamp`, `null` | lorsque cet événement a été repris par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_BEHAVIORS_APP_NEWSFEEDIMPRESSION_SHARED {#USERS_BEHAVIORS_APP_NEWSFEEDIMPRESSION_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID de l'utilisateur de Braze qui a effectué cet événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`app_group_id` | `null,` `string` | BSON ID du groupe d'applications auquel appartient cet utilisateur
`app_group_api_id` | `null,` `string` | ID API du groupe d'applications auquel appartient cet utilisateur
`app_api_id` | `null,` `string` | ID API de l’application sur laquelle cet événement s’est produit
`time` | `int` | Horodatage UNIX auquel l'événement s'est produit
`device_id` | `null,` `string` | ID de l’appareil sur lequel l’événement s’est produit
`sdk_version` | `null,` `string` | Version du SDK de Braze utilisée lors de l'événement
`platform` | `null,` `string` | Plate-forme de l'appareil
`os_version` | `null,` `string` | Version du système d'exploitation de l'appareil
`device_model` | `null,` `string` | Modèle de l'appareil
`sf_created_at` | `timestamp`, `null` | lorsque cet événement a été repris par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_APP_SESSIONEND_SHARED {#USERS_BEHAVIORS_APP_SESSIONEND_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui effectue cette action
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`app_api_id` | `null,` `string` | ID API de l’application sur laquelle cette session s’est produite
`time` | `int` | Horodatage Unix du moment où la session s’est terminée
`duration` | `null, float` | Durée de la session en secondes
`session_id` | `string` | UUID de la session
`device_id` | `null,` `string` | ID de l’appareil sur lequel la session s’est produite
`sdk_version` | `null,` `string` | Version du SDK de Braze utilisée pendant la session
`platform` | `null,` `string` | Plate-forme de l'appareil
`os_version` | `null,` `string` | Version du système d'exploitation de l'appareil
`device_model` | `null,` `string` | Modèle de l'appareil
`app_group_id` | `null,` `string` | BSON ID du groupe d'applications auquel appartient cet utilisateur
`sf_created_at` | `timestamp`, `null` | lorsque cet événement a été repris par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_APP_SESSIONSTART_SHARED {#USERS_BEHAVIORS_APP_SESSIONSTART_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui effectue cette action
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`app_api_id` | `null,` `string` | ID API de l’application sur laquelle cette session s’est produite
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`time` | `int` | Horodatage Unix du moment où la session a commencé
`session_id` | `string` | UUID de la session
`device_id` | `null,` `string` | ID de l’appareil sur lequel la session s’est produite
`sdk_version` | `null,` `string` | Version du SDK de Braze utilisée pendant la session
`platform` | `null,` `string` | Plate-forme de l'appareil
`os_version` | `null,` `string` | Version du système d'exploitation de l'appareil
`device_model` | `null,` `string` | Modèle de l'appareil
`app_group_id` | `null,` `string` | BSON ID du groupe d'applications auquel appartient cet utilisateur
`sf_created_at` | `timestamp`, `null` | lorsque cet événement a été repris par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_GEOFENCE_DATAEVENT_SHARED {#USERS_BEHAVIORS_GEOFENCE_DATAEVENT_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé l'événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`app_api_id` | `null,` `string` | ID API de l’application sur laquelle cette action s’est produite
`time` | `int` | Horodatage Unix du moment où l’utilisateur a effectué l’événement
`device_id` | `null,` `string` | ID de l’appareil sur lequel l’événement personnalisé s’est produit
`sdk_version` | `null,` `string` | Version du SDK de Braze utilisée lors de l'événement
`platform` | `null,` `string` | Plate-forme de l'appareil
`os_version` | `null,` `string` | Version du système d'exploitation de l'appareil
`device_model` | `null,` `string` | Modèle de l'appareil
`event_type` | `string` | Quel type d'événement de géorepérage a été déclenché. (par exemple, « entrer » ou « sortir »)
`location_set_id` | `string` | L’ID de l’ensemble des localisations du géorepérage qui a été déclenché
`geofence_id` | `string` | L’ID de la géorepérage qui a été déclenchée
`app_group_id` | `null,` `string` | BSON ID du groupe d'applications auquel appartient cet utilisateur
`sf_created_at` | `timestamp`, `null` | lorsque cet événement a été repris par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_GEOFENCE_RECORDEVENT_SHARED {#USERS_BEHAVIORS_GEOFENCE_RECORDEVENT_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé l'événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`app_api_id` | `null,` `string` | ID API de l’application sur laquelle cette action s’est produite
`time` | `int` | Horodatage Unix du moment où l’utilisateur a effectué l’événement
`device_id` | `null,` `string` | ID de l’appareil sur lequel l’événement personnalisé s’est produit
`sdk_version` | `null,` `string` | Version du SDK de Braze utilisée lors de l'événement
`platform` | `null,` `string` | Plate-forme de l'appareil
`os_version` | `null,` `string` | Version du système d'exploitation de l'appareil
`device_model` | `null,` `string` | Modèle de l'appareil
`event_type` | `string` | Quel type d'événement de géorepérage a été déclenché. (par exemple, « entrer » ou « sortir »)
`location_set_id` | `string` | L’ID de l’ensemble des localisations du géorepérage qui a été déclenché
`geofence_id` | `string` | L’ID de la géorepérage qui a été déclenchée
`app_group_id` | `null,` `string` | BSON ID du groupe d'applications auquel appartient cet utilisateur
`sf_created_at` | `timestamp`, `null` | lorsque cet événement a été repris par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_BEHAVIORS_LIVEACTIVITY_PUSHTOSTARTTOKENCHANGE_SHARED {#USERS_BEHAVIORS_LIVEACTIVITY_PUSHTOSTARTTOKENCHANGE_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID de l'utilisateur de Braze qui a effectué cet événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`time` | `int` | Horodatage UNIX auquel l'événement s'est produit
`app_group_id` | `null,` `string` | BSON ID du groupe d'applications auquel appartient cet utilisateur
`activity_attributes_type` | `null,` `string` | Type d'attribut de l'activité en ligne/en production/instantanée
`push_to_start_token` | `null,` `string` | Jeton de production/instantanée en ligne/en production/instantanée
`device_id` | `null,` `string` | ID de l’appareil sur lequel l’événement s’est produit
`sdk_version` | `null,` `string` | Version du SDK de Braze utilisée lors de l'événement
`ios_push_token_apns_gateway` | `null, int` | Passerelle APN du jeton de push, s'applique uniquement aux jetons de push iOS, 1 pour le développement, 2 pour la production.
`push_token_state_change_type` | `null,` `string` | Une description du type de changement d'état du jeton de poussée.
`app_group_api_id` | `null,` `string` | ID API du groupe d'applications auquel appartient cet utilisateur
`app_api_id` | `null,` `string` | ID API de l’application sur laquelle cet événement s’est produit
`sf_created_at` | `timestamp`, `null` | lorsque cet événement a été repris par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_BEHAVIORS_LIVEACTIVITY_UPDATETOKENCHANGE_SHARED {#USERS_BEHAVIORS_LIVEACTIVITY_UPDATETOKENCHANGE_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID de l'utilisateur de Braze qui a effectué cet événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`time` | `int` | Horodatage UNIX auquel l'événement s'est produit
`app_group_id` | `null,` `string` | BSON ID du groupe d'applications auquel appartient cet utilisateur
`activity_id` | `null,` `string` | Identifiant de production en ligne/instantané
`update_token` | `null,` `string` | Jeton de mise à jour de l'activité en ligne/instantanée
`device_id` | `null,` `string` | ID de l’appareil sur lequel l’événement s’est produit
`sdk_version` | `null,` `string` | Version du SDK de Braze utilisée lors de l'événement
`ios_push_token_apns_gateway` | `null, int` | Passerelle APN du jeton de push, s'applique uniquement aux jetons de push iOS, 1 pour le développement, 2 pour la production.
`push_token_state_change_type` | `null,` `string` | Une description du type de changement d'état du jeton de poussée.
`app_group_api_id` | `null,` `string` | ID API du groupe d'applications auquel appartient cet utilisateur
`app_api_id` | `null,` `string` | ID API de l’application sur laquelle cet événement s’est produit
`sf_created_at` | `timestamp`, `null` | lorsque cet événement a été repris par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_BEHAVIORS_PUSHNOTIFICATION_TOKENSTATECHANGE_SHARED {#USERS_BEHAVIORS_PUSHNOTIFICATION_TOKENSTATECHANGE_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`time` | `int` | Horodatage UNIX auquel l'événement s'est produit
`user_id` | `string` | ID de l'utilisateur de Braze qui a effectué cet événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`sdk_version` | `null,` `string` | Version du SDK de Braze utilisée lors de l'événement
`platform` | `null,` `string` | Plate-forme de l'appareil
`app_group_id` | `null,` `string` | BSON ID du groupe d'applications auquel appartient cet utilisateur
`push_token` | `null,` `string` | Jeton de l'événement
`push_token_created_at` | `null, int` | Horodatage UNIX auquel le jeton de poussée a été créé
`push_token_updated_at` | `null, int` | Horodatage UNIX de la dernière mise à jour du jeton de poussée.
`push_token_foreground_push_disabled` | `null, boolean` | Drapeau de désactivation de la poussée en avant-plan du jeton de poussée
`push_token_device_id` | `null,` `string` | ID de l'appareil du jeton de poussée
`push_token_provisionally_opted_in` | `null, boolean` | Drapeau d'abonnement provisoire du jeton de poussée
`ios_push_token_apns_gateway` | `null, int` | Passerelle APN du jeton de push, s'applique uniquement aux jetons de push iOS, 1 pour le développement, 2 pour la production.
`web_push_token_public_key` | `null,` `string` | Clé publique du jeton de push, ne s'applique qu'aux jetons de push web.
`web_push_token_user_auth` | `null,` `string` | Authentification de l'utilisateur du jeton de poussée, s'applique uniquement aux jetons de poussée web.
`web_push_token_vapid_public_key` | `null,` `string` | Clé publique VAPID du jeton de poussée, ne s'applique qu'aux jetons de poussée web.
`push_token_state_change_type` | `null,` `string` | Une description du type de changement d'état du jeton de poussée.
`app_group_api_id` | `null,` `string` | ID API du groupe d'applications auquel appartient cet utilisateur
`app_api_id` | `null,` `string` | ID API de l’application sur laquelle cet événement s’est produit
`sf_created_at` | `timestamp`, `null` | lorsque cet événement a été repris par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_SUBSCRIPTION_GLOBALSTATECHANGE_SHARED {#USERS_BEHAVIORS_SUBSCRIPTION_GLOBALSTATECHANGE_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur concerné
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`email_address` | `null,` `string` | [DPI] adresse e-mail de l'utilisateur
`state_change_source` | `null,` `string` | source du changement d’état (REST, SDK, tableau de bord, etc.)
`subscription_status` | `string` | Statut de l'abonnement : Abonné", "Désabonné" ou "Abonné".
`channel` | `null,` `string` | Canal de l'état de l'abonnement global tel que l'e-mail
`time` | `int` | Horodatage Unix du moment où l’état de l’abonnement a changé
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`app_api_id` | `null,` `string` | ID API de l’application à laquelle appartient l’événement
`campaign_id` | `null,` `string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle appartient cet événement
`message_variation_api_id` | `null,` `string` | ID API de la variation de message à laquelle appartient cet événement
`canvas_id` | `null,` `string` | ID de la Braze à usage interne de la toile à laquelle cet événement appartient
`canvas_api_id` | `null,` `string` | ID API du Canvas auquel appartient cet événement
`canvas_variation_api_id` | `null,` `string` | ID API de la variation de Canvas à laquelle appartient cet événement
`canvas_step_api_id` | `null,` `string` | ID API de l'étape de Canvas auquel appartient cet événement
`send_id` | `null,` `string` | ID d’envoi du message à l’origine de cette action de changement d’état d’abonnement
`app_group_id` | `null,` `string` | BSON ID du groupe d'applications auquel appartient cet utilisateur
`channel_identifier` | `null,` `string` | [PII] L'identifiant de l'utilisateur sur la chaîne pour laquelle l'événement est organisé.
`sf_created_at` | `timestamp`, `null` | lorsque cet événement a été repris par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED {#USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur concerné
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`device_id` | `null,` `string` | `device_id` qui est lié à cet utilisateur si celui-ci est anonyme
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`email_address` | `null,` `string` | [DPI] adresse e-mail de l'utilisateur
`phone_number` | `null,` `string` | [Numéro de téléphone de l'utilisateur au format e164
`app_api_id` | `null,` `string` | ID API de l’application à laquelle appartient l’événement
`campaign_id` | `null,` `string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle appartient cet événement
`message_variation_api_id` | `null,` `string` | ID API de la variation de message à laquelle appartient cet événement
`canvas_id` | `null,` `string` | ID de la Braze à usage interne de la toile à laquelle cet événement appartient
`canvas_api_id` | `null,` `string` | ID API du Canvas auquel appartient cet événement
`canvas_variation_api_id` | `null,` `string` | ID API de la variation de Canvas à laquelle appartient cet événement
`canvas_step_api_id` | `null,` `string` | ID API de l'étape de Canvas auquel appartient cet événement
`subscription_group_api_id` | `string` | ID d’API du groupe d'abonnement
`channel` | `null,` `string` | Canal : "e-mail" ou "sms", en fonction du type de canal du groupe d'abonnement.
`subscription_status` | `string` | Statut de l'abonnement : Abonné", "Désabonné" ou "Abonné".
`time` | `int` | Horodatage Unix du moment où l’état de l’abonnement a changé
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`send_id` | `null,` `string` | ID d’envoi du message à l’origine de cette action de changement d’état d’abonnement
`state_change_source` | `null,` `string` | Source du changement d'état (REST, SDK, tableau de bord, etc.)
`app_group_id` | `null,` `string` | BSON ID du groupe d'applications auquel appartient cet utilisateur
`dispatch_id` | `null,` `string` | ID de l’envoi auquel appartient ce message
`channel_identifier` | `null,` `string` | [PII] L'identifiant de l'utilisateur sur la chaîne pour laquelle l'événement est organisé.
`sf_created_at` | `timestamp`, `null` | lorsque cet événement a été repris par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Campagnes

### USERS_CAMPAIGNS_CONVERSION_SHARED {#USERS_CAMPAIGNS_CONVERSION_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`device_id` | `null,` `string` | `device_id` qui est lié à cet utilisateur si celui-ci est anonyme
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`time` | `int` | horodatage Unix du moment où l’événement s’est produit
`app_api_id` | `null,` `string` | ID API de l’application sur laquelle cet événement s’est produit
`dispatch_id` | `null,` `string` | ID de l’envoi auquel appartient ce message
`send_id` | `null,` `string` | ID d'envoi de message auquel ce message appartient
`campaign_id` | `string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle appartient cet événement
`message_variation_api_id` | `null,` `string` | ID API de la variation de message que l’utilisateur a reçue
`conversion_behavior_index` | `null, int` | Index du comportement de conversion
`gender` | `null,` `string` | [Sexe de l'utilisateur
`country` | `null,` `string` | [Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [Langue de l'utilisateur
`app_group_id` | `null,` `string` | BSON ID du groupe d'applications auquel appartient cet utilisateur
`sf_created_at` | `timestamp`, `null` | lorsque cet événement a été repris par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CAMPAIGNS_ENROLLINCONTROL_SHARED {#USERS_CAMPAIGNS_ENROLLINCONTROL_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`device_id` | `null,` `string` | `device_id` qui est lié à cet utilisateur si celui-ci est anonyme
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`time` | `int` | horodatage Unix du moment où l’événement s’est produit
`app_api_id` | `null,` `string` | ID API de l’application sur laquelle cet événement s’est produit
`dispatch_id` | `null,` `string` | ID de l’envoi auquel appartient ce message
`send_id` | `null,` `string` | ID d'envoi de message auquel ce message appartient
`campaign_id` | `string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle appartient cet événement
`message_variation_api_id` | `null,` `string` | ID API de la variation de message que l’utilisateur a reçue
`gender` | `null,` `string` | [Sexe de l'utilisateur
`country` | `null,` `string` | [Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [Langue de l'utilisateur
`app_group_id` | `null,` `string` | BSON ID du groupe d'applications auquel appartient cet utilisateur
`sf_created_at` | `timestamp`, `null` | lorsque cet événement a été repris par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CAMPAIGNS_FREQUENCYCAP_SHARED {#USERS_CAMPAIGNS_FREQUENCYCAP_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`device_id` | `null,` `string` | `device_id` qui est lié à cet utilisateur si celui-ci est anonyme
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`time` | `int` | horodatage Unix du moment où l’événement s’est produit
`dispatch_id` | `null,` `string` | ID de l’envoi auquel appartient ce message
`send_id` | `null,` `string` | ID d'envoi de message auquel ce message appartient
`campaign_id` | `string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle appartient cet événement
`message_variation_api_id` | `null,` `string` | ID API de la variation de message que l’utilisateur a reçue
`channel` | `null,` `string` | Canal auquel appartient cet événement
`gender` | `null,` `string` | [Sexe de l'utilisateur
`country` | `null,` `string` | [Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [Langue de l'utilisateur
`app_group_id` | `null,` `string` | BSON ID du groupe d'applications auquel appartient cet utilisateur
`sf_created_at` | `timestamp`, `null` | lorsque cet événement a été repris par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CAMPAIGNS_REVENUE_SHARED {#USERS_CAMPAIGNS_REVENUE_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`device_id` | `null,` `string` | `device_id` qui est lié à cet utilisateur si celui-ci est anonyme
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`time` | `int` | horodatage Unix du moment où l’événement s’est produit
`app_api_id` | `null,` `string` | ID API de l’application sur laquelle cet événement s’est produit
`dispatch_id` | `null,` `string` | ID de l’envoi auquel appartient ce message
`send_id` | `null,` `string` | ID d'envoi de message auquel ce message appartient
`campaign_id` | `string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle appartient cet événement
`message_variation_api_id` | `null,` `string` | ID API de la variation de message que l’utilisateur a reçue
`gender` | `null,` `string` | [Sexe de l'utilisateur
`country` | `null,` `string` | [Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [Langue de l'utilisateur
`revenue` | `long` | Le chiffre d'affaires d'USD en cents généré
`app_group_id` | `null,` `string` | BSON ID du groupe d'applications auquel appartient cet utilisateur
`sf_created_at` | `timestamp`, `null` | lorsque cet événement a été repris par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Canvas

### USERS_CANVASSTEP_PROGRESSION_SHARED {#USERS_CANVASSTEP_PROGRESSION_SHARED}

| Champ                                  | Type                     | Description                                                                                                     |
| -------------------------------------- | ------------------------ | --------------------------------------------------------------------------------------------------------------- |
| `id`                                   | `string`, `null`    | ID unique au niveau mondial pour cet événement                                                                               |
| `user_id`                              | `string`, `null`    | ID Braze de l'utilisateur qui a réalisé cet événement                                                                   |
| `external_user_id`                     | `string`, `null`    | [PII] ID externe de l'utilisateur                                                                              |
| `device_id`                            | `string`, `null`    | ID de l'appareil lié à cet utilisateur, si l'utilisateur est anonyme                                            |
| `app_group_id`                         | `string`, `null`    | ID Braze de l'espace de travail auquel cet utilisateur appartient                                                                   |
| `app_group_api_id`                     | `string`, `null`    | ID API de l'espace de travail auquel appartient cet utilisateur                                                                    |
| `time`                                 | `int`, `null`       | horodatage Unix du moment où l’événement s’est produit                                                                      |
| `canvas_id`                            | `string`, `null`    | (Réservé à l'usage de Braze) ID de la toile à laquelle appartient cet événement                                                     |
| `canvas_api_id`                        | `string`, `null`    | ID API du Canvas auquel appartient cet événement        |         
| `canvas_variation_api_id`              | `string`, `null`    | ID API de la variation de Canvas à laquelle appartient cet événement                                                            |
| `canvas_step_api_id`                   | `string`, `null`    | ID API de l'étape de Canvas auquel appartient cet événement                                                                 |
| `progression_type`                     | `string`, `null`    | Type d'événement de progression d'étape |
| `is_canvas_entry`                      | `boolean`, `null`   | Qu'il s'agisse de l'entrée dans une première étape du canvas        |
| `exit_reason`                          | `string`, `null`    | S'il s'agit d'une sortie, la raison pour laquelle l'utilisateur a quitté la toile au cours de l'étape.                  |
| `canvas_entry_id`                      | `string`, `null`    | Identifiant unique pour cette instance d'un utilisateur dans un Canvas  |
| `next_step_id`                         | `string`, `null`    | BSON ID de l'étape du canvas suivante |
| `next_step_api_id`                     | `string`, `null`    | ID API de l'étape suivante du canvas |
| `sf_created_at`                        | `timestamp`, `null` | Lorsque cet événement a été repris par le Snowpipe                                                                   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_CONVERSION_SHARED {#USERS_CANVAS_CONVERSION_SHARED}

| Champ                                  | Type                     | Description                                                                                                     |
| -------------------------------------- | ------------------------ | --------------------------------------------------------------------------------------------------------------- |
| `id`                                   | `string`, `null`    | ID unique au niveau mondial pour cet événement                                                                               |
| `user_id`                              | `string`, `null`    | ID Braze de l'utilisateur qui a réalisé cet événement                                                                   |
| `external_user_id`                     | `string`, `null`    | [PII] ID externe de l'utilisateur                                                                              |
| `device_id`                            | `string`, `null`    | ID de l'appareil lié à cet utilisateur, si l'utilisateur est anonyme                                            |
| `app_group_id`                         | `string`, `null`    | ID Braze de l'espace de travail auquel cet utilisateur appartient                                                                   |
| `app_group_api_id`                     | `string`, `null`    | ID API de l'espace de travail auquel appartient cet utilisateur                                                                    |
| `time`                                 | `int`, `null`       | horodatage Unix du moment où l’événement s’est produit                                                                      |
| `app_api_id`                           | `string`, `null`    | ID API de l’application sur laquelle cet événement s’est produit                                                                  |
| `canvas_id`                            | `string`, `null`    | (Réservé à l'usage de Braze) ID de la toile à laquelle appartient cet événement                                                     |
| `canvas_api_id`                        | `string`, `null`    | ID API du Canvas auquel appartient cet événement                                                                      |
| `canvas_variation_api_id`              | `string`, `null`    | ID API de la variation de Canvas à laquelle appartient cet événement                                                            |
| `canvas_step_api_id`                   | `string`, `null`    | ID API de l'étape de Canvas auquel appartient cet événement                                                                 |
| `canvas_step_message_variation_api_id` | `string`, `null`    | ID API de la variation de message de l'étape de Canvas que l’utilisateur a reçue                                                  |
| `conversion_behavior_index`            | `int`, `null`       | Type d'événement de conversion effectué par l'utilisateur, où "0" correspond à une conversion principale et "1" à une conversion secondaire. |
| `gender`                               | `string`, `null`    | [Sexe de l'utilisateur                                                                                        |
| `country`                              | `string`, `null`    | [Pays de l'utilisateur                                                                                       |
| `timezone`                             | `string`, `null`    | Fuseau horaire de l'utilisateur                                                                                            |
| `language`                             | `string`, `null`    | [Langue de l'utilisateur                                                                                      |
| `sf_created_at`                        | `timestamp`, `null` | Lorsque cet événement a été repris par le Snowpipe                                                                   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_ENTRY_SHARED {#USERS_CANVAS_ENTRY_SHARED}

| Champ                     | Type                     | Description                                                          |
| ------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                      | `string`, `null`    | ID unique au niveau mondial pour cet événement                                    |
| `user_id`                 | `string`, `null`    | ID Braze de l'utilisateur qui a réalisé cet événement                        |
| `external_user_id`        | `string`, `null`    | [PII] ID externe de l'utilisateur                                   |
| `device_id`               | `string`, `null`    | ID de l'appareil lié à cet utilisateur, si l'utilisateur est anonyme |
| `app_group_id`            | `string`, `null`    | ID Braze de l'espace de travail auquel cet utilisateur appartient                        |
| `app_group_api_id`        | `string`, `null`    | ID API de l'espace de travail auquel appartient cet utilisateur                         |
| `time`                    | `int`, `null`       | horodatage Unix du moment où l’événement s’est produit                           |
| `canvas_id`               | `string`, `null`    | (Réservé à l'usage de Braze) ID de la toile à laquelle appartient cet événement          |
| `canvas_api_id`           | `string`, `null`    | ID API du Canvas auquel appartient cet événement                           |
| `canvas_variation_api_id` | `string`, `null`    | ID API de la variation de Canvas à laquelle appartient cet événement                 |
| `canvas_step_api_id`      | `string`, `null`    | [Obsolète] API ID de l'étape du canvas à laquelle cet événement appartient.         |
| `gender`                  | `string`, `null`    | [Sexe de l'utilisateur                                             |
| `country`                 | `string`, `null`    | [Pays de l'utilisateur                                            |
| `timezone`                | `string`, `null`    | Fuseau horaire de l'utilisateur                                                 |
| `language`                | `string`, `null`    | [Langue de l'utilisateur                                           |
| `in_control_group`        | `boolean`, `null`   | Vrai si l'utilisateur était inscrit dans le groupe de contrôle                   |
| `sf_created_at`           | `timestamp`, `null` | Lorsque cet événement a été repris par le Snowpipe                        |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_EXIT_MATCHEDAUDIENCE_SHARED {#USERS_CANVAS_EXIT_MATCHEDAUDIENCE_SHARED}

| Champ                     | Type                     | Description                                                          |
| ------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                      | `string`, `null`    | ID unique au niveau mondial pour cet événement                                    |
| `user_id`                 | `string`, `null`    | ID Braze de l'utilisateur qui a réalisé cet événement                        |
| `external_user_id`        | `string`, `null`    | [PII] ID externe de l'utilisateur                                   |
| `app_group_id`            | `string`, `null`    | ID Braze de l'espace de travail auquel cet utilisateur appartient                        |
| `app_group_api_id`        | `string`, `null`    | ID API de l'espace de travail auquel appartient cet utilisateur                         |
| `time`                    | `int`, `null`       | horodatage Unix du moment où l’événement s’est produit                           |
| `canvas_id`               | `string`, `null`    | (Réservé à l'usage de Braze) ID de la toile à laquelle appartient cet événement          |
| `canvas_api_id`           | `string`, `null`    | ID API du Canvas auquel appartient cet événement                           |
| `canvas_variation_api_id` | `string`, `null`    | ID API de la variation de Canvas à laquelle appartient cet événement                 |
| `canvas_step_api_id`      | `string`, `null`    | ID API de l'étape de Canvas auquel appartient cet événement                      |
| `sf_created_at`           | `timestamp`, `null` | Lorsque cet événement a été repris par le Snowpipe                        |

{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_EXIT_PERFORMEDEVENT_SHARED {#USERS_CANVAS_EXIT_PERFORMEDEVENT_SHARED}

| Champ                     | Type                     | Description                                                          |
| ------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                      | `string`, `null`    | ID unique au niveau mondial pour cet événement                                    |
| `user_id`                 | `string`, `null`    | ID Braze de l'utilisateur qui a réalisé cet événement                        |
| `external_user_id`        | `string`, `null`    | [PII] ID externe de l'utilisateur                                   |
| `app_group_id`            | `string`, `null`    | ID Braze de l'espace de travail auquel cet utilisateur appartient                        |
| `app_group_api_id`        | `string`, `null`    | ID API de l'espace de travail auquel appartient cet utilisateur                         |
| `time`                    | `int`, `null`       | horodatage Unix du moment où l’événement s’est produit                           |
| `canvas_id`               | `string`, `null`    | (Réservé à l'usage de Braze) ID de la toile à laquelle appartient cet événement          |
| `canvas_api_id`           | `string`, `null`    | ID API du Canvas auquel appartient cet événement                           |
| `canvas_variation_api_id` | `string`, `null`    | ID API de la variation de Canvas à laquelle appartient cet événement                 |
| `canvas_step_api_id`      | `string`, `null`    | ID API de l'étape de Canvas auquel appartient cet événement                      |
| `sf_created_at`           | `timestamp`, `null` | Lorsque cet événement a été repris par le Snowpipe                        |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_EXPERIMENTSTEP_CONVERSION_SHARED {#USERS_CANVAS_EXPERIMENTSTEP_CONVERSION_SHARED}

| Champ                       | Type                     | Description                                                                                                     |
| --------------------------- | ------------------------ | --------------------------------------------------------------------------------------------------------------- |
| `id`                        | `string`, `null`    | ID unique au niveau mondial pour cet événement                                                                               |
| `user_id`                   | `string`, `null`    | ID Braze de l'utilisateur qui a réalisé cet événement                                                                   |
| `external_user_id`          | `string`, `null`    | [PII] ID externe de l'utilisateur                                                                              |
| `app_group_id`              | `string`, `null`    | ID Braze de l'espace de travail auquel cet utilisateur appartient                                                                   |
| `time`                      | `int`, `null`       | horodatage Unix du moment où l’événement s’est produit                                                                      |
| `app_api_id`                | `string`, `null`    | ID API de l’application sur laquelle cet événement s’est produit                                                                  |
| `canvas_id`                 | `string`, `null`    | (Réservé à l'usage de Braze) ID de la toile à laquelle appartient cet événement                                                     |
| `canvas_api_id`             | `string`, `null`    | ID API du Canvas auquel appartient cet événement                                                                      |
| `canvas_variation_api_id`   | `string`, `null`    | ID API de la variation de Canvas à laquelle appartient cet événement                                                            |
| `canvas_step_api_id`        | `string`, `null`    | ID API de l'étape de Canvas auquel appartient cet événement                                                                 |
| `experiment_step_api_id`    | `string`, `null`    | ID API de l'étape d'expérimentation à laquelle cet événement appartient                                                             |
| `conversion_behavior_index` | `int`, `null`       | Type d'événement de conversion effectué par l'utilisateur, où "0" correspond à une conversion principale et "1" à une conversion secondaire. |
| `sf_created_at`             | `timestamp`, `null` | Lorsque cet événement a été repris par le Snowpipe                                                                   |
| `experiment_split_api_id` | `string`, `null` | ID API de l'expérience à laquelle l'utilisateur s'est inscrit. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_EXPERIMENTSTEP_SPLITENTRY_SHARED {#USERS_CANVAS_EXPERIMENTSTEP_SPLITENTRY_SHARED}

| Champ                     | Type                     | Description                                                          |
| ------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                      | `string`, `null`    | ID unique au niveau mondial pour cet événement                                    |
| `user_id`                 | `string`, `null`    | ID Braze de l'utilisateur qui a réalisé cet événement                        |
| `external_user_id`        | `string`, `null`    | [PII] ID externe de l'utilisateur                                   |
| `app_group_id`            | `string`, `null`    | ID Braze de l'espace de travail auquel cet utilisateur appartient                        |
| `time`                    | `int`, `null`       | horodatage Unix du moment où l’événement s’est produit                           |
| `canvas_id`               | `string`, `null`    | (Réservé à l'usage de Braze) ID de la toile à laquelle appartient cet événement          |
| `canvas_api_id`           | `string`, `null`    | ID API du Canvas auquel appartient cet événement                           |
| `canvas_variation_api_id` | `string`, `null`    | ID API de la variation de Canvas à laquelle appartient cet événement                 |
| `canvas_step_api_id`      | `string`, `null`    | ID API de l'étape de Canvas auquel appartient cet événement                      |
| `experiment_step_api_id`  | `string`, `null`    | ID API de l'étape d'expérimentation à laquelle cet événement appartient                  |
| `in_control_group`        | `boolean`, `null`   | Vrai si l'utilisateur était inscrit dans le groupe de contrôle                   |
| `sf_created_at`           | `timestamp`, `null` | Lorsque cet événement a été repris par le Snowpipe                        |

| `experiment_split_api_id` | `string`, `null` | ID API de l'expérience à laquelle l'utilisateur s'est inscrit |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_FREQUENCYCAP_SHARED {#USERS_CANVAS_FREQUENCYCAP_SHARED}

| Champ                                  | Type                     | Description                                                          |
| -------------------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                                   | `string`, `null`    | ID unique au niveau mondial pour cet événement                                    |
| `user_id`                              | `string`, `null`    | ID Braze de l'utilisateur qui a réalisé cet événement                        |
| `external_user_id`                     | `string`, `null`    | [PII] ID externe de l'utilisateur                                   |
| `device_id`                            | `string`, `null`    | ID de l'appareil lié à cet utilisateur, si l'utilisateur est anonyme |
| `app_group_id`                         | `string`, `null`    | ID Braze de l'espace de travail auquel cet utilisateur appartient                        |
| `app_group_api_id`                     | `string`, `null`    | ID API de l'espace de travail auquel appartient cet utilisateur                         |
| `time`                                 | `int`, `null`       | horodatage Unix du moment où l’événement s’est produit                           |
| `canvas_id`                            | `string`, `null`    | (Réservé à l'usage de Braze) ID de la toile à laquelle appartient cet événement          |
| `canvas_api_id`                        | `string`, `null`    | ID API du Canvas auquel appartient cet événement                           |
| `canvas_variation_api_id`              | `string`, `null`    | ID API de la variation de Canvas à laquelle appartient cet événement                 |
| `canvas_step_api_id`                   | `string`, `null`    | ID API de l'étape de Canvas auquel appartient cet événement                      |
| `canvas_step_message_variation_api_id` | `string`, `null`    | ID API de la variation de message de l'étape de Canvas que l’utilisateur a reçue       |
| `channel`                              | `string`, `null`    | Canal de communication auquel cet événement appartient (e-mail, push, etc.)          |
| `gender`                               | `string`, `null`    | [Sexe de l'utilisateur                                             |
| `country`                              | `string`, `null`    | [Pays de l'utilisateur                                            |
| `timezone`                             | `string`, `null`    | Fuseau horaire de l'utilisateur                                                 |
| `language`                             | `string`, `null`    | [Langue de l'utilisateur                                           |
| `sf_created_at`                        | `timestamp`, `null` | Lorsque cet événement a été repris par le Snowpipe                        |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_REVENUE_SHARED {#USERS_CANVAS_REVENUE_SHARED}

| Champ                                  | Type                     | Description                                                          |
| -------------------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                                   | `string`, `null`    | ID unique au niveau mondial pour cet événement                                    |
| `user_id`                              | `string`, `null`    | ID Braze de l'utilisateur qui a réalisé cet événement                        |
| `external_user_id`                     | `string`, `null`    | [PII] ID externe de l'utilisateur                                   |
| `device_id`                            | `string`, `null`    | ID de l'appareil lié à cet utilisateur, si l'utilisateur est anonyme |
| `app_group_id`                         | `string`, `null`    | ID Braze de l'espace de travail auquel cet utilisateur appartient                        |
| `app_group_api_id`                     | `string`, `null`    | ID API de l'espace de travail auquel appartient cet utilisateur                         |
| `time`                                 | `int`, `null`       | horodatage Unix du moment où l’événement s’est produit                           |
| `canvas_id`                            | `string`, `null`    | (Réservé à l'usage de Braze) ID de la toile à laquelle appartient cet événement          |
| `canvas_api_id`                        | `string`, `null`    | ID API du Canvas auquel appartient cet événement                           |
| `canvas_variation_api_id`              | `string`, `null`    | ID API de la variation de Canvas à laquelle appartient cet événement                 |
| `canvas_step_api_id`                   | `string`, `null`    | ID API de l'étape de Canvas auquel appartient cet événement                      |
| `canvas_step_message_variation_api_id` | `string`, `null`    | ID API de la variation de message de l'étape de Canvas que l’utilisateur a reçue       |
| `gender`                               | `string`, `null`    | [Sexe de l'utilisateur                                             |
| `country`                              | `string`, `null`    | [Pays de l'utilisateur                                            |
| `timezone`                             | `string`, `null`    | Fuseau horaire de l'utilisateur                                                 |
| `language`                             | `string`, `null`    | [Langue de l'utilisateur                                           |
| `revenue`                              | `int`, `null`       | Montant du chiffre d'affaires généré en USD, affiché en cents               |
| `sf_created_at`                        | `timestamp`, `null` | Lorsque cet événement a été repris par le Snowpipe                        |
| `app_api_id` | `string`, `null` | ID API de l’application sur laquelle cet événement s’est produit |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Messages


### USERS_MESSAGES_BANNER_ABORT_SHARED {#USERS_MESSAGES_BANNER_ABORT_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID de l'utilisateur de Braze qui a effectué cet événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`app_group_id` | `null,` `string` | BSON ID du groupe d'applications auquel appartient cet utilisateur
`app_group_api_id` | `null,` `string` | ID API du groupe d'applications auquel appartient cet utilisateur
`time` | `int` | Horodatage UNIX auquel l'événement s'est produit
`app_api_id` | `null,` `string` | ID API de l’application sur laquelle cet événement s’est produit
`campaign_id` | `null,` `string` | BSON ID de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle appartient cet événement
`message_variation_api_id` | `null,` `string` | ID API de la variation de message que l’utilisateur a reçue
`gender` | `null,` `string` | [Sexe de l'utilisateur
`country` | `null,` `string` | [Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [Langue de l'utilisateur
`device_id` | `null,` `string` | ID de l’appareil sur lequel l’événement s’est produit
`sdk_version` | `null,` `string` | Version du SDK de Braze utilisée lors de l'événement
`platform` | `null,` `string` | Plate-forme de l'appareil
`os_version` | `null,` `string` | Version du système d'exploitation de l'appareil
`device_model` | `null,` `string` | Modèle de l'appareil
`resolution` | `null,` `string` | Résolution de l'appareil
`carrier` | `null,` `string` | Opérateur de l'appareil
`browser` | `null,` `string` | Navigateur de l'appareil - extrait de user_agent \- sur lequel l'ouverture s'est produite
`ad_id` | `null,` `string` | [Identifiant publicitaire
`ad_id_type` | `null,` `string` | L'un des ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']
`ad_tracking_enabled` | `null, boolean` | Si le suivi publicitaire est activé pour l’appareil ou non
`abort_type` | `null,` `string` | Type d'abandon, l'un des suivants ['liquid_abort_message', 'quiet_hours', 'rate_limit']
`abort_log` | `null,` `string` | [PII] Message du journal décrivant les détails de l'abandon (jusqu'à 128 caractères)
`banner_placement_id` | `null,` `string` | ID de placement de la bannière spécifiée par le personnalisé
`sf_created_at` | `timestamp`, `null` | lorsque cet événement a été repris par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_BANNER_CLICK_SHARED {#USERS_MESSAGES_BANNER_CLICK_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID de l'utilisateur de Braze qui a effectué cet événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`app_group_id` | `null,` `string` | BSON ID du groupe d'applications auquel appartient cet utilisateur
`app_group_api_id` | `null,` `string` | ID API du groupe d'applications auquel appartient cet utilisateur
`time` | `int` | Horodatage UNIX auquel l'événement s'est produit
`app_api_id` | `null,` `string` | ID API de l’application sur laquelle cet événement s’est produit
`campaign_id` | `null,` `string` | BSON ID de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle appartient cet événement
`message_variation_api_id` | `null,` `string` | ID API de la variation de message que l’utilisateur a reçue
`gender` | `null,` `string` | [Sexe de l'utilisateur
`country` | `null,` `string` | [Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [Langue de l'utilisateur
`device_id` | `null,` `string` | ID de l’appareil sur lequel l’événement s’est produit
`sdk_version` | `null,` `string` | Version du SDK de Braze utilisée lors de l'événement
`platform` | `null,` `string` | Plate-forme de l'appareil
`os_version` | `null,` `string` | Version du système d'exploitation de l'appareil
`device_model` | `null,` `string` | Modèle de l'appareil
`resolution` | `null,` `string` | Résolution de l'appareil
`carrier` | `null,` `string` | Opérateur de l'appareil
`browser` | `null,` `string` | Navigateur de l'appareil - extrait de user_agent \- sur lequel l'ouverture s'est produite
`button_id` | `null,` `string` | ID du bouton cliqué, si ce clic représente un clic sur un bouton
`ad_id` | `null,` `string` | [Identifiant publicitaire
`ad_id_type` | `null,` `string` | L'un des ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']
`ad_tracking_enabled` | `null, boolean` | Si le suivi publicitaire est activé pour l’appareil ou non
`banner_placement_id` | `null,` `string` | ID de placement de la bannière spécifiée par le personnalisé
`sf_created_at` | `timestamp`, `null` | lorsque cet événement a été repris par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_BANNER_IMPRESSION_SHARED {#USERS_MESSAGES_BANNER_IMPRESSION_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID de l'utilisateur de Braze qui a effectué cet événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`app_group_id` | `null,` `string` | BSON ID du groupe d'applications auquel appartient cet utilisateur
`app_group_api_id` | `null,` `string` | ID API du groupe d'applications auquel appartient cet utilisateur
`time` | `int` | Horodatage UNIX auquel l'événement s'est produit
`app_api_id` | `null,` `string` | ID API de l’application sur laquelle cet événement s’est produit
`campaign_id` | `null,` `string` | BSON ID de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle appartient cet événement
`message_variation_api_id` | `null,` `string` | ID API de la variation de message que l’utilisateur a reçue
`gender` | `null,` `string` | [Sexe de l'utilisateur
`country` | `null,` `string` | [Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [Langue de l'utilisateur
`device_id` | `null,` `string` | ID de l’appareil sur lequel l’événement s’est produit
`sdk_version` | `null,` `string` | Version du SDK de Braze utilisée lors de l'événement
`platform` | `null,` `string` | Plate-forme de l'appareil
`os_version` | `null,` `string` | Version du système d'exploitation de l'appareil
`device_model` | `null,` `string` | Modèle de l'appareil
`resolution` | `null,` `string` | Résolution de l'appareil
`carrier` | `null,` `string` | Opérateur de l'appareil
`browser` | `null,` `string` | Navigateur de l'appareil - extrait de user_agent \- sur lequel l'ouverture s'est produite
`ad_id` | `null,` `string` | [Identifiant publicitaire
`ad_id_type` | `null,` `string` | L'un des ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']
`ad_tracking_enabled` | `null, boolean` | Si le suivi publicitaire est activé pour l’appareil ou non
`banner_placement_id` | `null,` `string` | ID de placement de la bannière spécifiée par le personnalisé
`sf_created_at` | `timestamp`, `null` | lorsque cet événement a été repris par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_CONTENTCARD_ABORT_SHARED {#USERS_MESSAGES_CONTENTCARD_ABORT_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`device_id` | `null,` `string` | `device_id` qui est lié à cet utilisateur si celui-ci est anonyme
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`time` | `int` | horodatage Unix du moment où l’événement s’est produit
`dispatch_id` | `null,` `string` | ID de l’envoi auquel appartient ce message
`send_id` | `null,` `string` | ID d'envoi de message auquel ce message appartient
`campaign_id` | `null,` `string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle appartient cet événement
`message_variation_api_id` | `null,` `string` | ID API de la variation de message que l’utilisateur a reçue
`canvas_id` | `null,` `string` | ID de la Braze à usage interne de la toile à laquelle cet événement appartient
`canvas_api_id` | `null,` `string` | ID API du Canvas auquel appartient cet événement
`canvas_variation_api_id` | `null,` `string` | ID API de la variation de Canvas à laquelle appartient cet événement
`canvas_step_api_id` | `null,` `string` | ID API de l'étape de Canvas auquel appartient cet événement
`canvas_step_message_variation_api_id` | `null,` `string` | ID API de la variation de message de l'étape de Canvas que l’utilisateur a reçue
`gender` | `null,` `string` | [Sexe de l'utilisateur
`country` | `null,` `string` | [Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [Langue de l'utilisateur
`abort_type` | `null,` `string` | Type d'abandon, l'un des suivants ['liquid_abort_message', 'quiet_hours', 'rate_limit']
`abort_log` | `null,` `string` | [PII] Message du journal décrivant les détails de l'abandon (maximum de 2 000 caractères)
`app_group_id` | `null,` `string` | BSON ID du groupe d'applications auquel appartient cet utilisateur
`sf_created_at` | `timestamp`, `null` | lorsque cet événement a été repris par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_CONTENTCARD_CLICK_SHARED {#USERS_MESSAGES_CONTENTCARD_CLICK_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`content_card_id` | `string` | ID de la carte qui a généré cet événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`time` | `int` | horodatage Unix du moment où l’événement s’est produit
`app_api_id` | `null,` `string` | ID API de l’application sur laquelle cet événement s’est produit
`dispatch_id` | `null,` `string` | ID de l’envoi auquel appartient ce message
`send_id` | `null,` `string` | ID d'envoi de message auquel ce message appartient
`campaign_id` | `null,` `string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle appartient cet événement
`message_variation_api_id` | `null,` `string` | ID API de la variation de message que l’utilisateur a reçue
`canvas_id` | `null,` `string` | ID de la Braze à usage interne de la toile à laquelle cet événement appartient
`canvas_api_id` | `null,` `string` | ID API du Canvas auquel appartient cet événement
`canvas_variation_api_id` | `null,` `string` | ID API de la variation de Canvas à laquelle appartient cet événement
`canvas_step_api_id` | `null,` `string` | ID API de l'étape de Canvas auquel appartient cet événement
`canvas_step_message_variation_api_id` | `null,` `string` | ID API de la variation de message de l'étape de Canvas que l’utilisateur a reçue
`gender` | `null,` `string` | [Sexe de l'utilisateur
`country` | `null,` `string` | [Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [Langue de l'utilisateur
`device_id` | `null,` `string` | ID de l’appareil sur lequel l’événement s’est produit
`sdk_version` | `null,` `string` | Version du SDK de Braze utilisée lors de l'événement
`platform` | `null,` `string` | Plate-forme de l'appareil
`os_version` | `null,` `string` | Version du système d'exploitation de l'appareil
`device_model` | `null,` `string` | Modèle de l'appareil
`resolution` | `null,` `string` | Résolution de l'appareil
`carrier` | `null,` `string` | Opérateur de l'appareil
`browser` | `null,` `string` | Navigateur de l'appareil
`ad_id` | `null,` `string` | [Identifiant publicitaire
`ad_id_type` | `null,` `string` | Un parmi `ios_idfa`, `google_ad_id`, `windows_ad_id` OU `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Si le suivi publicitaire est activé pour l’appareil ou non
`app_group_id` | `null,` `string` | BSON ID du groupe d'applications auquel appartient cet utilisateur
`sf_created_at` | `timestamp`, `null` | lorsque cet événement a été repris par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_CONTENTCARD_DISMISS_SHARED {#USERS_MESSAGES_CONTENTCARD_DISMISS_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`content_card_id` | `string` | ID de la carte qui a généré cet événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`time` | `int` | horodatage Unix du moment où l’événement s’est produit
`app_api_id` | `null,` `string` | ID API de l’application sur laquelle cet événement s’est produit
`dispatch_id` | `null,` `string` | ID de l’envoi auquel appartient ce message
`send_id` | `null,` `string` | ID d'envoi de message auquel ce message appartient
`campaign_id` | `null,` `string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle appartient cet événement
`message_variation_api_id` | `null,` `string` | ID API de la variation de message que l’utilisateur a reçue
`canvas_id` | `null,` `string` | ID de la Braze à usage interne de la toile à laquelle cet événement appartient
`canvas_api_id` | `null,` `string` | ID API du Canvas auquel appartient cet événement
`canvas_variation_api_id` | `null,` `string` | ID API de la variation de Canvas à laquelle appartient cet événement
`canvas_step_api_id` | `null,` `string` | ID API de l'étape de Canvas auquel appartient cet événement
`canvas_step_message_variation_api_id` | `null,` `string` | ID API de la variation de message de l'étape de Canvas que l’utilisateur a reçue
`gender` | `null,` `string` | [Sexe de l'utilisateur
`country` | `null,` `string` | [Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [Langue de l'utilisateur
`device_id` | `null,` `string` | ID de l’appareil sur lequel l’événement s’est produit
`sdk_version` | `null,` `string` | Version du SDK de Braze utilisée lors de l'événement
`platform` | `null,` `string` | Plate-forme de l'appareil
`os_version` | `null,` `string` | Version du système d'exploitation de l'appareil
`device_model` | `null,` `string` | Modèle de l'appareil
`resolution` | `null,` `string` | Résolution de l'appareil
`carrier` | `null,` `string` | Opérateur de l'appareil
`browser` | `null,` `string` | Navigateur de l'appareil
`ad_id` | `null,` `string` | [Identifiant publicitaire
`ad_id_type` | `null,` `string` | Un parmi `ios_idfa`, `google_ad_id`, `windows_ad_id` OU `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Si le suivi publicitaire est activé pour l’appareil ou non
`app_group_id` | `null,` `string` | BSON ID du groupe d'applications auquel appartient cet utilisateur
`sf_created_at` | `timestamp`, `null` | lorsque cet événement a été repris par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_CONTENTCARD_IMPRESSION_SHARED {#USERS_MESSAGES_CONTENTCARD_IMPRESSION_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`content_card_id` | `string` | ID de la carte qui a généré cet événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`time` | `int` | horodatage Unix du moment où l’événement s’est produit
`app_api_id` | `null,` `string` | ID API de l’application sur laquelle cet événement s’est produit
`dispatch_id` | `null,` `string` | ID de l’envoi auquel appartient ce message
`send_id` | `null,` `string` | ID d'envoi de message auquel ce message appartient
`campaign_id` | `null,` `string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle appartient cet événement
`message_variation_api_id` | `null,` `string` | ID API de la variation de message que l’utilisateur a reçue
`canvas_id` | `null,` `string` | ID de la Braze à usage interne de la toile à laquelle cet événement appartient
`canvas_api_id` | `null,` `string` | ID API du Canvas auquel appartient cet événement
`canvas_variation_api_id` | `null,` `string` | ID API de la variation de Canvas à laquelle appartient cet événement
`canvas_step_api_id` | `null,` `string` | ID API de l'étape de Canvas auquel appartient cet événement
`canvas_step_message_variation_api_id` | `null,` `string` | ID API de la variation de message de l'étape de Canvas que l’utilisateur a reçue
`gender` | `null,` `string` | [Sexe de l'utilisateur
`country` | `null,` `string` | [Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [Langue de l'utilisateur
`device_id` | `null,` `string` | ID de l’appareil sur lequel l’événement s’est produit
`sdk_version` | `null,` `string` | Version du SDK de Braze utilisée lors de l'événement
`platform` | `null,` `string` | Plate-forme de l'appareil
`os_version` | `null,` `string` | Version du système d'exploitation de l'appareil
`device_model` | `null,` `string` | Modèle de l'appareil
`resolution` | `null,` `string` | Résolution de l'appareil
`carrier` | `null,` `string` | Opérateur de l'appareil
`browser` | `null,` `string` | Navigateur de l'appareil
`ad_id` | `null,` `string` | [Identifiant publicitaire
`ad_id_type` | `null,` `string` | Un parmi `ios_idfa`, `google_ad_id`, `windows_ad_id` OU `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Si le suivi publicitaire est activé pour l’appareil ou non
`app_group_id` | `null,` `string` | BSON ID du groupe d'applications auquel appartient cet utilisateur
`sf_created_at` | `timestamp`, `null` | lorsque cet événement a été repris par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_CONTENTCARD_SEND_SHARED {#USERS_MESSAGES_CONTENTCARD_SEND_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`device_id` | `null,` `string` | `device_id` qui est lié à cet utilisateur si celui-ci est anonyme
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`time` | `int` | horodatage Unix du moment où l’événement s’est produit
`dispatch_id` | `null,` `string` | ID de l’envoi auquel appartient ce message
`send_id` | `null,` `string` | ID d'envoi de message auquel ce message appartient
`campaign_id` | `null,` `string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle appartient cet événement
`message_variation_api_id` | `null,` `string` | ID API de la variation de message que l’utilisateur a reçue
`canvas_id` | `null,` `string` | ID de la Braze à usage interne de la toile à laquelle cet événement appartient
`canvas_api_id` | `null,` `string` | ID API du Canvas auquel appartient cet événement
`canvas_variation_api_id` | `null,` `string` | ID API de la variation de Canvas à laquelle appartient cet événement
`canvas_step_api_id` | `null,` `string` | ID API de l'étape de Canvas auquel appartient cet événement
`canvas_step_message_variation_api_id` | `null,` `string` | ID API de la variation de message de l'étape de Canvas que l’utilisateur a reçue
`gender` | `null,` `string` | [Sexe de l'utilisateur
`country` | `null,` `string` | [Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [Langue de l'utilisateur
`content_card_id` | `string` | ID de la carte qui a généré cet événement
`app_group_id` | `null,` `string` | BSON ID du groupe d'applications auquel appartient cet utilisateur
`message_extras` | `null,` `string` | [Une chaîne JSON des paires clé-valeur balisées lors du rendu liquide.
`sf_created_at` | `timestamp`, `null` | lorsque cet événement a été repris par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_ABORT_SHARED {#USERS_MESSAGES_EMAIL_ABORT_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`device_id` | `null,` `string` | `device_id` qui est lié à cet utilisateur si celui-ci est anonyme
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`time` | `int` | horodatage Unix du moment où l’événement s’est produit
`dispatch_id` | `null,` `string` | ID de l’envoi auquel appartient ce message
`send_id` | `null,` `string` | ID d'envoi de message auquel ce message appartient
`campaign_id` | `null,` `string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle appartient cet événement
`message_variation_api_id` | `null,` `string` | ID API de la variation de message que l’utilisateur a reçue
`canvas_id` | `null,` `string` | ID de la Braze à usage interne de la toile à laquelle cet événement appartient
`canvas_api_id` | `null,` `string` | ID API du Canvas auquel appartient cet événement
`canvas_variation_api_id` | `null,` `string` | ID API de la variation de Canvas à laquelle appartient cet événement
`canvas_step_api_id` | `null,` `string` | ID API de l'étape de Canvas auquel appartient cet événement
`canvas_step_message_variation_api_id` | `null,` `string` | ID API de la variation de message de l'étape de Canvas que l’utilisateur a reçue
`gender` | `null,` `string` | [Sexe de l'utilisateur
`country` | `null,` `string` | [Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [Langue de l'utilisateur
`email_address` | `string` | [DPI] adresse e-mail de l'utilisateur
`ip_pool` | `null,` `string` | Ensemble d’IP à partir duquel l’e-mail a été envoyé
`abort_type` | `null,` `string` | Type d'abandon, l'un des suivants ['liquid_abort_message', 'quiet_hours', 'rate_limit']
`abort_log` | `null,` `string` | [PII] Message du journal décrivant les détails de l'abandon (maximum de 2 000 caractères)
`app_group_id` | `null,` `string` | BSON ID du groupe d'applications auquel appartient cet utilisateur
`sf_created_at` | `timestamp`, `null` | lorsque cet événement a été repris par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_BOUNCE_SHARED {#USERS_MESSAGES_EMAIL_BOUNCE_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`device_id` | `null,` `string` | `device_id` qui est lié à cet utilisateur si celui-ci est anonyme
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`time` | `int` | horodatage Unix du moment où l’événement s’est produit
`dispatch_id` | `null,` `string` | ID de l’envoi auquel appartient ce message
`send_id` | `null,` `string` | ID d'envoi de message auquel ce message appartient
`campaign_id` | `null,` `string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle appartient cet événement
`message_variation_api_id` | `null,` `string` | ID API de la variation de message que l’utilisateur a reçue
`canvas_id` | `null,` `string` | ID de la Braze à usage interne de la toile à laquelle cet événement appartient
`canvas_api_id` | `null,` `string` | ID API du Canvas auquel appartient cet événement
`canvas_variation_api_id` | `null,` `string` | ID API de la variation de Canvas à laquelle appartient cet événement
`canvas_step_api_id` | `null,` `string` | ID API de l'étape de Canvas auquel appartient cet événement
`canvas_step_message_variation_api_id` | `null,` `string` | ID API de la variation de message de l'étape de Canvas que l’utilisateur a reçue
`gender` | `null,` `string` | [Sexe de l'utilisateur
`country` | `null,` `string` | [Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [Langue de l'utilisateur
`email_address` | `string` | [DPI] adresse e-mail de l'utilisateur
`sending_ip` | `null,` `string` | Adresse IP à partir de laquelle l’e-mail a été envoyé
`ip_pool` | `null,` `string` | Ensemble d’IP à partir duquel l’e-mail a été envoyé
`bounce_reason` | `null,` `string` | [IIP] Le code de raison SMTP et l'envoi du message convivial reçu pour cet événement de rebond.
`esp` | `null,` `string` | ESP lié à l'événement (SparkPost, SendGrid, ou Amazon SES)
`from_domain` | `null,` `string` | Domaine d'envoi de l'e-mail
`is_drop` | `null, boolean` | Indique que cet événement est décompté comme un événement d’abandon
`app_group_id` | `null,` `string` | BSON ID du groupe d'applications auquel appartient cet utilisateur
`sf_created_at` | `timestamp`, `null` | lorsque cet événement a été repris par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_CLICK_SHARED {#USERS_MESSAGES_EMAIL_CLICK_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`device_id` | `null,` `string` | `device_id` qui est lié à cet utilisateur si celui-ci est anonyme
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`time` | `int` | horodatage Unix du moment où l’événement s’est produit
`dispatch_id` | `null,` `string` | ID de l’envoi auquel appartient ce message
`send_id` | `null,` `string` | ID d'envoi de message auquel ce message appartient
`campaign_id` | `null,` `string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle appartient cet événement
`message_variation_api_id` | `null,` `string` | ID API de la variation de message que l’utilisateur a reçue
`canvas_id` | `null,` `string` | ID de la Braze à usage interne de la toile à laquelle cet événement appartient
`canvas_api_id` | `null,` `string` | ID API du Canvas auquel appartient cet événement
`canvas_variation_api_id` | `null,` `string` | ID API de la variation de Canvas à laquelle appartient cet événement
`canvas_step_api_id` | `null,` `string` | ID API de l'étape de Canvas auquel appartient cet événement
`canvas_step_message_variation_api_id` | `null,` `string` | ID API de la variation de message de l'étape de Canvas que l’utilisateur a reçue
`gender` | `null,` `string` | [Sexe de l'utilisateur
`country` | `null,` `string` | [Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [Langue de l'utilisateur
`email_address` | `string` | [DPI] adresse e-mail de l'utilisateur
`url` | `null,` `string` | URL sur laquelle l’utilisateur a cliqué
`user_agent` | `null,` `string` | Agent utilisateur sur lequel le clic s'est produit
`ip_pool` | `null,` `string` | Ensemble d’IP à partir duquel l’e-mail a été envoyé
`link_id` | `null,` `string` | ID unique du lien sur lequel on a cliqué, tel que créé par Braze
`link_alias` | `null,` `string` | Alias associé à cet ID de lien
`esp` | `null,` `string` | ESP lié à l'événement (SparkPost, SendGrid, ou Amazon SES)
`from_domain` | `null,` `string` | Domaine d'envoi de l'e-mail
`is_amp` | `null, boolean` | Indique qu'il s'agit d'un événement AMP
`app_group_id` | `null,` `string` | BSON ID du groupe d'applications auquel appartient cet utilisateur
`is_suspected_bot_click` | `null, boolean` | Si cet événement a été traité comme un événement bot
`suspected_bot_click_reason` | `null, object` | Pourquoi cet événement a été classé comme bot
`sf_created_at` | `timestamp`, `null` | lorsque cet événement a été repris par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_EMAIL_DEFERRAL_SHARED {#USERS_MESSAGES_EMAIL_DEFERRAL_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`time` | `int` | Horodatage UNIX auquel l'événement s'est produit
`user_id` | `string` | ID de l'utilisateur de Braze qui a effectué cet événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`app_group_id` | `null,` `string` | BSON ID du groupe d'applications auquel appartient cet utilisateur
`app_group_api_id` | `null,` `string` | ID API du groupe d'applications auquel appartient cet utilisateur
`send_id` | `null,` `string` | ID d'envoi de message auquel ce message appartient
`campaign_id` | `null,` `string` | BSON ID de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle appartient cet événement
`message_variation_api_id` | `null,` `string` | ID API de la variation de message que l’utilisateur a reçue
`canvas_id` | `null,` `string` | BSON ID de la toile à laquelle cet événement appartient
`canvas_api_id` | `null,` `string` | ID API du Canvas auquel appartient cet événement
`canvas_variation_api_id` | `null,` `string` | ID API de la variation de Canvas à laquelle appartient cet événement
`canvas_step_api_id` | `null,` `string` | ID API de l'étape de Canvas auquel appartient cet événement
`canvas_step_message_variation_api_id` | `null,` `string` | ID API de la variation de message de l'étape de Canvas que l’utilisateur a reçue
`dispatch_id` | `null,` `string` | ID de l’envoi auquel appartient ce message
`email_address` | `null,` `string` | [PII] Adresse e-mail de l'utilisateur
`recipient_domain` | `null,` `string` | Domaine de l'e-mail du destinataire
`esp` | `null,` `string` | ESP lié à l'événement (Sparkpost ou Sendgrid, ou Amazon SES)
`from_domain` | `null,` `string` | Domaine d'envoi de l'e-mail
`ip_pool` | `null,` `string` | Pool d'adresses IP à partir duquel l'e-mail a été envoyé
`sending_ip` | `null,` `string` | Adresse IP à partir de laquelle l’e-mail a été envoyé
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`deferral_reason` | `null,` `string` | [IIP] Le code de motif SMTP et le message convivial reçus pour cet événement de report.
`attempt_count` | `null, int` | Nombre de tentatives d'envoi du message
`sf_created_at` | `timestamp`, `null` | lorsque cet événement a été repris par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_DELIVERY_SHARED {#USERS_MESSAGES_EMAIL_DELIVERY_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`device_id` | `null,` `string` | `device_id` qui est lié à cet utilisateur si celui-ci est anonyme
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`time` | `int` | horodatage Unix du moment où l’événement s’est produit
`dispatch_id` | `null,` `string` | ID de l’envoi auquel appartient ce message
`send_id` | `null,` `string` | ID d'envoi de message auquel ce message appartient
`campaign_id` | `null,` `string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle appartient cet événement
`message_variation_api_id` | `null,` `string` | ID API de la variation de message que l’utilisateur a reçue
`canvas_id` | `null,` `string` | ID de la Braze à usage interne de la toile à laquelle cet événement appartient
`canvas_api_id` | `null,` `string` | ID API du Canvas auquel appartient cet événement
`canvas_variation_api_id` | `null,` `string` | ID API de la variation de Canvas à laquelle appartient cet événement
`canvas_step_api_id` | `null,` `string` | ID API de l'étape de Canvas auquel appartient cet événement
`canvas_step_message_variation_api_id` | `null,` `string` | ID API de la variation de message de l'étape de Canvas que l’utilisateur a reçue
`gender` | `null,` `string` | [Sexe de l'utilisateur
`country` | `null,` `string` | [Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [Langue de l'utilisateur
`email_address` | `string` | [DPI] adresse e-mail de l'utilisateur
`sending_ip` | `null,` `string` | Adresse IP à partir de laquelle l’e-mail a été envoyé
`ip_pool` | `null,` `string` | Ensemble d’IP à partir duquel l’e-mail a été envoyé
`esp` | `null,` `string` | ESP lié à l'événement (SparkPost, SendGrid, ou Amazon SES)
`from_domain` | `null,` `string` | Domaine d'envoi de l'e-mail
`app_group_id` | `null,` `string` | BSON ID du groupe d'applications auquel appartient cet utilisateur
`sf_created_at` | `timestamp`, `null` | lorsque cet événement a été repris par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_MARKASSPAM_SHARED {#USERS_MESSAGES_EMAIL_MARKASSPAM_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`device_id` | `null,` `string` | `device_id` qui est lié à cet utilisateur si celui-ci est anonyme
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`time` | `int` | horodatage Unix du moment où l’événement s’est produit
`dispatch_id` | `null,` `string` | ID de l’envoi auquel appartient ce message
`send_id` | `null,` `string` | ID d'envoi de message auquel ce message appartient
`campaign_id` | `null,` `string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle appartient cet événement
`message_variation_api_id` | `null,` `string` | ID API de la variation de message que l’utilisateur a reçue
`canvas_id` | `null,` `string` | ID de la Braze à usage interne de la toile à laquelle cet événement appartient
`canvas_api_id` | `null,` `string` | ID API du Canvas auquel appartient cet événement
`canvas_variation_api_id` | `null,` `string` | ID API de la variation de Canvas à laquelle appartient cet événement
`canvas_step_api_id` | `null,` `string` | ID API de l'étape de Canvas auquel appartient cet événement
`canvas_step_message_variation_api_id` | `null,` `string` | ID API de la variation de message de l'étape de Canvas que l’utilisateur a reçue
`gender` | `null,` `string` | [Sexe de l'utilisateur
`country` | `null,` `string` | [Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [Langue de l'utilisateur
`email_address` | `string` | [DPI] adresse e-mail de l'utilisateur
`user_agent` | `null,` `string` | Agent utilisateur sur lequel le signalement du courrier indésirable a eu lieu
`ip_pool` | `null,` `string` | Ensemble d’IP à partir duquel l’e-mail a été envoyé
`esp` | `null,` `string` | ESP lié à l'événement (SparkPost, SendGrid, ou Amazon SES)
`from_domain` | `null,` `string` | Domaine d'envoi de l'e-mail
`app_group_id` | `null,` `string` | BSON ID du groupe d'applications auquel appartient cet utilisateur
`sf_created_at` | `timestamp`, `null` | lorsque cet événement a été repris par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_OPEN_SHARED {#USERS_MESSAGES_EMAIL_OPEN_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`device_id` | `null,` `string` | `device_id` qui est lié à cet utilisateur si celui-ci est anonyme
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`time` | `int` | horodatage Unix du moment où l’événement s’est produit
`dispatch_id` | `null,` `string` | ID de l’envoi auquel appartient ce message
`send_id` | `null,` `string` | ID d'envoi de message auquel ce message appartient
`campaign_id` | `null,` `string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle appartient cet événement
`message_variation_api_id` | `null,` `string` | ID API de la variation de message que l’utilisateur a reçue
`canvas_id` | `null,` `string` | ID de la Braze à usage interne de la toile à laquelle cet événement appartient
`canvas_api_id` | `null,` `string` | ID API du Canvas auquel appartient cet événement
`canvas_variation_api_id` | `null,` `string` | ID API de la variation de Canvas à laquelle appartient cet événement
`canvas_step_api_id` | `null,` `string` | ID API de l'étape de Canvas auquel appartient cet événement
`canvas_step_message_variation_api_id` | `null,` `string` | ID API de la variation de message de l'étape de Canvas que l’utilisateur a reçue
`gender` | `null,` `string` | [Sexe de l'utilisateur
`country` | `null,` `string` | [Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [Langue de l'utilisateur
`email_address` | `string` | [DPI] adresse e-mail de l'utilisateur
`user_agent` | `null,` `string` | Agent utilisateur sur lequel l'ouverture s'est produite
`ip_pool` | `null,` `string` | Ensemble d’IP à partir duquel l’e-mail a été envoyé
`machine_open` | `null,` `string` | La valeur "true" est indiquée si l'événement d'ouverture est déclenché sans l'intervention de l'utilisateur, par exemple, par un appareil Apple sur lequel la protection de la confidentialité du courrier est activée. La valeur peut changer au fil du temps pour fournir plus de granularité.
`esp` | `null,` `string` | ESP lié à l'événement (SparkPost, SendGrid, ou Amazon SES)
`from_domain` | `null,` `string` | Domaine d'envoi de l'e-mail
`is_amp` | `null, boolean` | Indique qu'il s'agit d'un événement AMP
`app_group_id` | `null,` `string` | BSON ID du groupe d'applications auquel appartient cet utilisateur
`sf_created_at` | `timestamp`, `null` | lorsque cet événement a été repris par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_SEND_SHARED {#USERS_MESSAGES_EMAIL_SEND_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`device_id` | `null,` `string` | `device_id` qui est lié à cet utilisateur si celui-ci est anonyme
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`time` | `int` | horodatage Unix du moment où l’événement s’est produit
`dispatch_id` | `null,` `string` | ID de l’envoi auquel appartient ce message
`send_id` | `null,` `string` | ID d'envoi de message auquel ce message appartient
`campaign_id` | `null,` `string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle appartient cet événement
`message_variation_api_id` | `null,` `string` | ID API de la variation de message que l’utilisateur a reçue
`canvas_id` | `null,` `string` | ID de la Braze à usage interne de la toile à laquelle cet événement appartient
`canvas_api_id` | `null,` `string` | ID API du Canvas auquel appartient cet événement
`canvas_variation_api_id` | `null,` `string` | ID API de la variation de Canvas à laquelle appartient cet événement
`canvas_step_api_id` | `null,` `string` | ID API de l'étape de Canvas auquel appartient cet événement
`canvas_step_message_variation_api_id` | `null,` `string` | ID API de la variation de message de l'étape de Canvas que l’utilisateur a reçue
`gender` | `null,` `string` | [Sexe de l'utilisateur
`country` | `null,` `string` | [Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [Langue de l'utilisateur
`email_address` | `string` | [DPI] adresse e-mail de l'utilisateur
`ip_pool` | `null,` `string` | Ensemble d’IP à partir duquel l’e-mail a été envoyé
`message_extras` | `null,` `string` | [Une chaîne JSON des paires clé-valeur balisées lors du rendu de Liquid.
`esp` | `null,` `string` | ESP lié à l'événement (SparkPost, SendGrid, ou Amazon SES)
`from_domain` | `null,` `string` | Domaine d'envoi de l'e-mail
`sf_created_at` | `timestamp`, `null` | Lorsque cet événement a été repris par le Snowpipe
`app_group_id` | `null,` `string` | BSON ID du groupe d'applications auquel appartient cet utilisateur
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_SOFTBOUNCE_SHARED {#USERS_MESSAGES_EMAIL_SOFTBOUNCE_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`device_id` | `null,` `string` | `device_id` qui est lié à cet utilisateur si celui-ci est anonyme
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`time` | `int` | horodatage Unix du moment où l’événement s’est produit
`dispatch_id` | `null,` `string` | ID de l’envoi auquel appartient ce message
`send_id` | `null,` `string` | ID d'envoi de message auquel ce message appartient
`campaign_id` | `null,` `string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle appartient cet événement
`message_variation_api_id` | `null,` `string` | ID API de la variation de message que l’utilisateur a reçue
`canvas_id` | `null,` `string` | ID de la Braze à usage interne de la toile à laquelle cet événement appartient
`canvas_api_id` | `null,` `string` | ID API du Canvas auquel appartient cet événement
`canvas_variation_api_id` | `null,` `string` | ID API de la variation de Canvas à laquelle appartient cet événement
`canvas_step_api_id` | `null,` `string` | ID API de l'étape de Canvas auquel appartient cet événement
`canvas_step_message_variation_api_id` | `null,` `string` | ID API de la variation de message de l'étape de Canvas que l’utilisateur a reçue
`gender` | `null,` `string` | [Sexe de l'utilisateur
`country` | `null,` `string` | [Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [Langue de l'utilisateur
`email_address` | `string` | [DPI] adresse e-mail de l'utilisateur
`sending_ip` | `null,` `string` | Adresse IP à partir de laquelle l’e-mail a été envoyé
`ip_pool` | `null,` `string` | Ensemble d’IP à partir duquel l’e-mail a été envoyé
`bounce_reason` | `null,` `string` | [IIP] Le code de raison SMTP et l'envoi du message convivial reçu pour cet événement de rebond.
`esp` | `null,` `string` | ESP lié à l'événement (SparkPost, SendGrid, ou Amazon SES)
`from_domain` | `null,` `string` | Domaine d'envoi de l'e-mail
`app_group_id` | `null,` `string` | BSON ID du groupe d'applications auquel appartient cet utilisateur
`sf_created_at` | `timestamp`, `null` | lorsque cet événement a été repris par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED {#USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`device_id` | `null,` `string` | `device_id` qui est lié à cet utilisateur si celui-ci est anonyme
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`time` | `int` | horodatage Unix du moment où l’événement s’est produit
`dispatch_id` | `null,` `string` | ID de l’envoi auquel appartient ce message
`send_id` | `null,` `string` | ID d'envoi de message auquel ce message appartient
`campaign_id` | `null,` `string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle appartient cet événement
`message_variation_api_id` | `null,` `string` | ID API de la variation de message que l’utilisateur a reçue
`canvas_id` | `null,` `string` | ID de la Braze à usage interne de la toile à laquelle cet événement appartient
`canvas_api_id` | `null,` `string` | ID API du Canvas auquel appartient cet événement
`canvas_variation_api_id` | `null,` `string` | ID API de la variation de Canvas à laquelle appartient cet événement
`canvas_step_api_id` | `null,` `string` | ID API de l'étape de Canvas auquel appartient cet événement
`canvas_step_message_variation_api_id` | `null,` `string` | ID API de la variation de message de l'étape de Canvas que l’utilisateur a reçue
`gender` | `null,` `string` | [Sexe de l'utilisateur
`country` | `null,` `string` | [Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [Langue de l'utilisateur
`email_address` | `string` | [DPI] adresse e-mail de l'utilisateur
`ip_pool` | `null,` `string` | Ensemble d’IP à partir duquel l’e-mail a été envoyé
`app_group_id` | `null,` `string` | BSON ID du groupe d'applications auquel appartient cet utilisateur
`sf_created_at` | `timestamp`, `null` | lorsque cet événement a été repris par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_FEATUREFLAG_IMPRESSION_SHARED {#USERS_MESSAGES_FEATUREFLAG_IMPRESSION_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`app_api_id` | `null,` `string` | ID API de l’application sur laquelle cet événement s’est produit
`app_group_id` | `null,` `string` | BSON ID du groupe d'applications auquel appartient cet utilisateur
`app_group_api_id` | `null,` `string` | ID API du groupe d'applications auquel appartient cet utilisateur
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle appartient cet événement
`campaign_id` | `null,` `string` | BSON ID de la campagne à laquelle cet événement appartient
`canvas_api_id` | `null,` `string` | ID API du Canvas auquel appartient cet événement
`canvas_id` | `null,` `string` | BSON ID de la toile à laquelle cet événement appartient
`canvas_step_api_id` | `null,` `string` | ID API de l'étape de Canvas auquel appartient cet événement
`canvas_step_message_variation_api_id` | `null,` `string` | ID API de la variation de message de l'étape de Canvas que l’utilisateur a reçue
`canvas_variation_api_id` | `null,` `string` | ID API de la variation de Canvas à laquelle appartient cet événement
`feature_flag_id_name` | `null,` `string` | L'identifiant du déploiement des fonctionnalités
`message_variation_api_id` | `null,` `string` | ID API de la variation de message que l’utilisateur a reçue
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`device_id` | `null,` `string` | ID de l’appareil sur lequel l’événement s’est produit
`time` | `int` | Horodatage UNIX auquel l'événement s'est produit
`gender` | `null,` `string` | [Sexe de l'utilisateur
`browser` | `null,` `string` | Navigateur de l'appareil - extrait de user_agent \- sur lequel l'ouverture s'est produite
`carrier` | `null,` `string` | Opérateur de l'appareil
`country` | `null,` `string` | [Pays de l'utilisateur
`device_model` | `null,` `string` | Modèle de l'appareil
`language` | `null,` `string` | [Langue de l'utilisateur
`os_version` | `null,` `string` | Version du système d'exploitation de l'appareil
`platform` | `null,` `string` | Plate-forme de l'appareil
`resolution` | `null,` `string` | Résolution de l'appareil
`sdk_version` | `null,` `string` | Version du SDK de Braze utilisée lors de l'événement
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`user_id` | `string` | ID de l'utilisateur de Braze qui a effectué cet événement
`sf_created_at` | `timestamp`, `null` | lorsque cet événement a été repris par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_INAPPMESSAGE_ABORT_SHARED {#USERS_MESSAGES_INAPPMESSAGE_ABORT_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`time` | `int` | horodatage Unix du moment où l’événement s’est produit
`app_api_id` | `null,` `string` | ID API de l’application sur laquelle cet événement s’est produit
`card_api_id` | `null,` `string` | ID API de la carte
`dispatch_id` | `null,` `string` | ID de l’envoi auquel appartient ce message
`send_id` | `null,` `string` | ID d'envoi de message auquel ce message appartient
`campaign_id` | `null,` `string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle appartient cet événement
`message_variation_api_id` | `null,` `string` | ID API de la variation de message que l’utilisateur a reçue
`canvas_id` | `null,` `string` | ID de la Braze à usage interne de la toile à laquelle cet événement appartient
`canvas_api_id` | `null,` `string` | ID API du Canvas auquel appartient cet événement
`canvas_variation_api_id` | `null,` `string` | ID API de la variation de Canvas à laquelle appartient cet événement
`canvas_step_api_id` | `null,` `string` | ID API de l'étape de Canvas auquel appartient cet événement
`canvas_step_message_variation_api_id` | `null,` `string` | ID API de la variation de message de l'étape de Canvas que l’utilisateur a reçue
`gender` | `null,` `string` | [Sexe de l'utilisateur
`country` | `null,` `string` | [Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [Langue de l'utilisateur
`device_id` | `null,` `string` | ID de l’appareil sur lequel l’événement s’est produit
`sdk_version` | `null,` `string` | Version du SDK de Braze utilisée lors de l'événement
`platform` | `null,` `string` | Plate-forme de l'appareil
`os_version` | `null,` `string` | Version du système d'exploitation de l'appareil
`device_model` | `null,` `string` | Modèle de l'appareil
`resolution` | `null,` `string` | Résolution de l'appareil
`carrier` | `null,` `string` | Opérateur de l'appareil
`browser` | `null,` `string` | Navigateur de l'appareil
`version` | `string` | Quelle version du message in-app, ancienne ou déclenchée ?
`ad_id` | `null,` `string` | [Identifiant publicitaire
`ad_id_type` | `null,` `string` | Un parmi `ios_idfa`, `google_ad_id`, `windows_ad_id` OU `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Si le suivi publicitaire est activé pour l’appareil ou non
`abort_type` | `null,` `string` | Type d'abandon, l'un des suivants ['liquid_abort_message', 'quiet_hours', 'rate_limit']
`abort_log` | `null,` `string` | [PII] Message du journal décrivant les détails de l'abandon (maximum de 2 000 caractères)
`app_group_id` | `null,` `string` | BSON ID du groupe d'applications auquel appartient cet utilisateur
`sf_created_at` | `timestamp`, `null` | lorsque cet événement a été repris par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_INAPPMESSAGE_CLICK_SHARED {#USERS_MESSAGES_INAPPMESSAGE_CLICK_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`time` | `int` | horodatage Unix du moment où l’événement s’est produit
`app_api_id` | `null,` `string` | ID API de l’application sur laquelle cet événement s’est produit
`card_api_id` | `null,` `string` | ID API de la carte
`dispatch_id` | `null,` `string` | ID de l’envoi auquel appartient ce message
`send_id` | `null,` `string` | ID d'envoi de message auquel ce message appartient
`campaign_id` | `null,` `string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle appartient cet événement
`message_variation_api_id` | `null,` `string` | ID API de la variation de message que l’utilisateur a reçue
`canvas_id` | `null,` `string` | ID de la Braze à usage interne de la toile à laquelle cet événement appartient
`canvas_api_id` | `null,` `string` | ID API du Canvas auquel appartient cet événement
`canvas_variation_api_id` | `null,` `string` | ID API de la variation de Canvas à laquelle appartient cet événement
`canvas_step_api_id` | `null,` `string` | ID API de l'étape de Canvas auquel appartient cet événement
`canvas_step_message_variation_api_id` | `null,` `string` | ID API de la variation de message de l'étape de Canvas que l’utilisateur a reçue
`gender` | `null,` `string` | [Sexe de l'utilisateur
`country` | `null,` `string` | [Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [Langue de l'utilisateur
`device_id` | `null,` `string` | ID de l’appareil sur lequel l’événement s’est produit
`sdk_version` | `null,` `string` | Version du SDK de Braze utilisée lors de l'événement
`platform` | `null,` `string` | Plate-forme de l'appareil
`os_version` | `null,` `string` | Version du système d'exploitation de l'appareil
`device_model` | `null,` `string` | Modèle de l'appareil
`resolution` | `null,` `string` | résolution de l’appareil
`carrier` | `null,` `string` | opérateur de l’appareil
`browser` | `null,` `string` | navigateur de l’appareil
`version` | `string` | quelle version du message in-app, héritée ou déclenchée
`button_id` | `null,` `string` | ID du bouton cliqué, si ce clic représente un clic sur un bouton
`ad_id` | `null,` `string` | [Identifiant publicitaire
`ad_id_type` | `null,` `string` | Un parmi `ios_idfa`, `google_ad_id`, `windows_ad_id` OU `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Si le suivi publicitaire est activé pour l’appareil ou non
`app_group_id` | `null,` `string` | BSON ID du groupe d'applications auquel appartient cet utilisateur
`sf_created_at` | `timestamp`, `null` | lorsque cet événement a été repris par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_INAPPMESSAGE_IMPRESSION_SHARED {#USERS_MESSAGES_INAPPMESSAGE_IMPRESSION_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`time` | `int` | horodatage Unix du moment où l’événement s’est produit
`app_api_id` | `null,` `string` | ID API de l’application sur laquelle cet événement s’est produit
`card_api_id` | `null,` `string` | ID API de la carte
`dispatch_id` | `null,` `string` | ID de l’envoi auquel appartient ce message
`send_id` | `null,` `string` | ID d'envoi de message auquel ce message appartient
`campaign_id` | `null,` `string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle appartient cet événement
`message_variation_api_id` | `null,` `string` | ID API de la variation de message que l’utilisateur a reçue
`canvas_id` | `null,` `string` | ID de la Braze à usage interne de la toile à laquelle cet événement appartient
`canvas_api_id` | `null,` `string` | ID API du Canvas auquel appartient cet événement
`canvas_variation_api_id` | `null,` `string` | ID API de la variation de Canvas à laquelle appartient cet événement
`canvas_step_api_id` | `null,` `string` | ID API de l'étape de Canvas auquel appartient cet événement
`canvas_step_message_variation_api_id` | `null,` `string` | ID API de la variation de message de l'étape de Canvas que l’utilisateur a reçue
`gender` | `null,` `string` | [Sexe de l'utilisateur
`country` | `null,` `string` | [Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [Langue de l'utilisateur
`device_id` | `null,` `string` | ID de l’appareil sur lequel l’événement s’est produit
`sdk_version` | `null,` `string` | Version du SDK de Braze utilisée lors de l'événement
`platform` | `null,` `string` | Plate-forme de l'appareil
`os_version` | `null,` `string` | Version du système d'exploitation de l'appareil
`device_model` | `null,` `string` | Modèle de l'appareil
`resolution` | `null,` `string` | résolution de l’appareil
`carrier` | `null,` `string` | opérateur de l’appareil
`browser` | `null,` `string` | navigateur de l’appareil
`version` | `string` | quelle version du message in-app, héritée ou déclenchée
`ad_id` | `null,` `string` | [Identifiant publicitaire
`ad_id_type` | `null,` `string` | Un parmi `ios_idfa`, `google_ad_id`, `windows_ad_id` OU `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Si le suivi publicitaire est activé pour l’appareil ou non
`app_group_id` | `null,` `string` | BSON ID du groupe d'applications auquel appartient cet utilisateur
`message_extras` | `null,` `string` | [Une chaîne JSON des paires clé-valeur balisées lors du rendu liquide.
`locale_key` | `null,` `string` | [La clé correspondant aux traductions (par exemple 'en-us') utilisées pour composer ce message (null pour la valeur par défaut).
`sf_created_at` | `timestamp`, `null` | lorsque cet événement a été repris par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_LINE_ABORT_SHARED {#USERS_MESSAGES_LINE_ABORT_SHARED}

Champ | Type | Description
------|------|------------
`app_group_api_id` | `null,` `string` | ID API du groupe d'applications auquel appartient cet utilisateur
`app_group_id` | `null,` `string` | BSON ID du groupe d'applications auquel appartient cet utilisateur
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`id` | `string` | ID unique au niveau mondial pour cet événement
`time` | `int` | Horodatage UNIX auquel l'événement s'est produit
`user_id` | `string` | ID de l'utilisateur de Braze qui a effectué cet événement
`abort_log` | `null,` `string` | [PII] Message du journal décrivant les détails de l'abandon (jusqu'à 128 caractères)
`abort_type` | `null,` `string` | Type d'abandon, l'un des suivants ['liquid_abort_message', 'quiet_hours', 'rate_limit']
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle appartient cet événement
`canvas_step_api_id` | `null,` `string` | ID API de l'étape de Canvas auquel appartient cet événement
`canvas_step_message_variation_api_id` | `null,` `string` | ID API de la variation de message de l'étape de Canvas que l’utilisateur a reçue
`device_id` | `null,` `string` | ID de l’appareil sur lequel l’événement s’est produit
`dispatch_id` | `null,` `string` | ID de l’envoi auquel appartient ce message
`line_channel_id` | `null,` `string` | L'ID du canal de la LIGNE auquel le message a été envoyé ou dont il a été reçu.
`line_channel_name` | `null,` `string` | Le nom du canal LINE auquel le message a été envoyé ou reçu.
`message_variation_api_id` | `null,` `string` | ID API de la variation de message que l’utilisateur a reçue
`native_line_id` | `null,` `string` | [PII] L'ID de ligne de l'utilisateur à partir duquel le message a été envoyé ou reçu.
`send_id` | `null,` `string` | ID d'envoi de message auquel ce message appartient
`subscription_group_api_id` | `string` | ID d’API du groupe d'abonnement
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`campaign_name` | `null,` `string` | Nom de la campagne
`canvas_step_name` | `null,` `string` | Nom de l'étape du canvas
`canvas_variation_api_id` | `null,` `string` | ID API de la variation de Canvas à laquelle appartient cet événement
`canvas_api_id` | `null,` `string` | ID API du Canvas auquel appartient cet événement
`sf_created_at` | `timestamp`, `null` | lorsque cet événement a été repris par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_LINE_CLICK_SHARED {#USERS_MESSAGES_LINE_CLICK_SHARED}

Champ | Type | Description
------|------|------------
`app_group_api_id` | `null,` `string` | ID API du groupe d'applications auquel appartient cet utilisateur
`app_group_id` | `null,` `string` | BSON ID du groupe d'applications auquel appartient cet utilisateur
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`id` | `string` | ID unique au niveau mondial pour cet événement
`time` | `int` | Horodatage UNIX auquel l'événement s'est produit
`user_id` | `string` | ID de l'utilisateur de Braze qui a effectué cet événement
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`native_line_id` | `null,` `string` | [PII] L'ID de ligne de l'utilisateur à partir duquel le message a été envoyé ou reçu.
`line_channel_id` | `null,` `string` | L'ID du canal de la LIGNE auquel le message a été envoyé ou dont il a été reçu.
`line_channel_name` | `null,` `string` | Le nom du canal LINE auquel le message a été envoyé ou reçu.
`subscription_group_api_id` | `string` | ID d’API du groupe d'abonnement
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle appartient cet événement
`campaign_name` | `null,` `string` | Nom de la campagne
`message_variation_api_id` | `null,` `string` | ID API de la variation de message que l’utilisateur a reçue
`canvas_api_id` | `null,` `string` | ID API du Canvas auquel appartient cet événement
`canvas_variation_api_id` | `null,` `string` | ID API de la variation de Canvas à laquelle appartient cet événement
`canvas_step_api_id` | `null,` `string` | ID API de l'étape de Canvas auquel appartient cet événement
`canvas_step_message_variation_api_id` | `null,` `string` | ID API de la variation de message de l'étape de Canvas que l’utilisateur a reçue
`canvas_step_name` | `null,` `string` | Nom de l'étape du canvas
`dispatch_id` | `null,` `string` | ID de l’envoi auquel appartient ce message
`device_id` | `null,` `string` | ID de l’appareil sur lequel l’événement s’est produit
`send_id` | `null,` `string` | ID d'envoi de message auquel ce message appartient
`is_suspected_bot_click` | `null, boolean` | Si cet événement a été traité comme un événement bot
`short_url` | `null,` `string` | URL raccourcie qui a été cliquée
`url` | `null,` `string` | URL sur laquelle l’utilisateur a cliqué
`user_agent` | `null,` `string` | Agent utilisateur sur lequel le signalement du courrier indésirable a eu lieu
`sf_created_at` | `timestamp`, `null` | lorsque cet événement a été repris par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_LINE_INBOUNDRECEIVE_SHARED {#USERS_MESSAGES_LINE_INBOUNDRECEIVE_SHARED}

Champ | Type | Description
------|------|------------
`app_group_api_id` | `null,` `string` | ID API du groupe d'applications auquel appartient cet utilisateur
`app_group_id` | `null,` `string` | BSON ID du groupe d'applications auquel appartient cet utilisateur
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`id` | `string` | ID unique au niveau mondial pour cet événement
`time` | `int` | Horodatage UNIX auquel l'événement s'est produit
`user_id` | `string` | ID de l'utilisateur de Braze qui a effectué cet événement
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle appartient cet événement
`campaign_name` | `null,` `string` | Nom de la campagne
`canvas_api_id` | `null,` `string` | ID API du Canvas auquel appartient cet événement
`canvas_step_api_id` | `null,` `string` | ID API de l'étape de Canvas auquel appartient cet événement
`canvas_step_message_variation_api_id` | `null,` `string` | ID API de la variation de message de l'étape de Canvas que l’utilisateur a reçue
`canvas_step_name` | `null,` `string` | Nom de l'étape du canvas
`canvas_variation_api_id` | `null,` `string` | ID API de la variation de Canvas à laquelle appartient cet événement
`device_id` | `null,` `string` | ID de l’appareil sur lequel l’événement s’est produit
`dispatch_id` | `null,` `string` | ID de l’envoi auquel appartient ce message
`line_channel_id` | `null,` `string` | L'ID du canal de la LIGNE auquel le message a été envoyé ou dont il a été reçu.
`line_channel_name` | `null,` `string` | Le nom du canal LINE auquel le message a été envoyé ou reçu.
`media_id` | `null,` `string` | L'ID généré par LINE qui peut être utilisé pour récupérer les médias entrants à partir de LINE.
`message_body` | `null,` `string` | Réponse dactylographiée de l'utilisateur
`message_variation_api_id` | `null,` `string` | ID API de la variation de message que l’utilisateur a reçue
`native_line_id` | `null,` `string` | [PII] L'ID de ligne de l'utilisateur à partir duquel le message a été envoyé ou reçu.
`send_id` | `null,` `string` | ID d'envoi de message auquel ce message appartient
`subscription_group_api_id` | `string` | ID d’API du groupe d'abonnement
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`sf_created_at` | `timestamp`, `null` | lorsque cet événement a été repris par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_LINE_SEND_SHARED {#USERS_MESSAGES_LINE_SEND_SHARED}

Champ | Type | Description
------|------|------------
`app_group_api_id` | `null,` `string` | ID API du groupe d'applications auquel appartient cet utilisateur
`app_group_id` | `null,` `string` | BSON ID du groupe d'applications auquel appartient cet utilisateur
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`id` | `string` | ID unique au niveau mondial pour cet événement
`time` | `int` | Horodatage UNIX auquel l'événement s'est produit
`user_id` | `string` | ID de l'utilisateur de Braze qui a effectué cet événement
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle appartient cet événement
`campaign_name` | `null,` `string` | Nom de la campagne
`canvas_api_id` | `null,` `string` | ID API du Canvas auquel appartient cet événement
`canvas_step_api_id` | `null,` `string` | ID API de l'étape de Canvas auquel appartient cet événement
`canvas_step_message_variation_api_id` | `null,` `string` | ID API de la variation de message de l'étape de Canvas que l’utilisateur a reçue
`canvas_step_name` | `null,` `string` | Nom de l'étape du canvas
`canvas_variation_api_id` | `null,` `string` | ID API de la variation de Canvas à laquelle appartient cet événement
`device_id` | `null,` `string` | ID de l’appareil sur lequel l’événement s’est produit
`dispatch_id` | `null,` `string` | ID de l’envoi auquel appartient ce message
`line_channel_id` | `null,` `string` | L'ID du canal de la LIGNE auquel le message a été envoyé ou dont il a été reçu.
`line_channel_name` | `null,` `string` | Le nom du canal LINE auquel le message a été envoyé ou reçu.
`message_extras` | `null,` `string` | [Une chaîne JSON des paires clé-valeur balisées lors du rendu liquide.
`message_variation_api_id` | `null,` `string` | ID API de la variation de message que l’utilisateur a reçue
`native_line_id` | `null,` `string` | [PII] L'ID de ligne de l'utilisateur à partir duquel le message a été envoyé ou reçu.
`send_id` | `null,` `string` | ID d'envoi de message auquel ce message appartient
`subscription_group_api_id` | `string` | ID d’API du groupe d'abonnement
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`sf_created_at` | `timestamp`, `null` | lorsque cet événement a été repris par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_LIVEACTIVITY_OUTCOME_SHARED {#USERS_MESSAGES_LIVEACTIVITY_OUTCOME_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID de l'utilisateur de Braze qui a effectué cet événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`time` | `int` | Horodatage UNIX auquel l'événement s'est produit
`app_group_id` | `null,` `string` | BSON ID du groupe d'applications auquel appartient cet utilisateur
`activity_id` | `null,` `string` | Identifiant de production en ligne/instantané
`activity_attributes_type` | `null,` `string` | Type d'attribut de l'activité en ligne/en production/instantanée
`push_to_start_token` | `null,` `string` | Jeton de production/instantanée en ligne/en production/instantanée
`update_token` | `null,` `string` | Jeton de mise à jour de l'activité en ligne/instantanée
`live_activity_event_type` | `null,` `string` | Type d'événement de la ligne/en production/instantanée. Un parmi ['start', 'update', 'end']
`live_activity_event_outcome` | `null,` `string` | Résultat de l'activité en ligne/instantanée
`app_group_api_id` | `null,` `string` | ID API du groupe d'applications auquel appartient cet utilisateur
`app_api_id` | `null,` `string` | ID API de l’application sur laquelle cet événement s’est produit
`sf_created_at` | `timestamp`, `null` | lorsque cet événement a été repris par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_LIVEACTIVITY_SEND_SHARED {#USERS_MESSAGES_LIVEACTIVITY_SEND_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID de l'utilisateur de Braze qui a effectué cet événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`time` | `int` | Horodatage UNIX auquel l'événement s'est produit
`app_group_id` | `null,` `string` | BSON ID du groupe d'applications auquel appartient cet utilisateur
`activity_id` | `null,` `string` | Identifiant de production en ligne/instantané
`activity_attributes_type` | `null,` `string` | Type d'attribut de l'activité en ligne/en production/instantanée
`push_to_start_token` | `null,` `string` | Jeton de production/instantanée en ligne/en production/instantanée
`update_token` | `null,` `string` | Jeton de mise à jour de l'activité en ligne/instantanée
`live_activity_event_type` | `null,` `string` | Type d'événement de la ligne/en production/instantanée. Un parmi ['start', 'update', 'end']
`app_group_api_id` | `null,` `string` | ID API du groupe d'applications auquel appartient cet utilisateur
`app_api_id` | `null,` `string` | ID API de l’application sur laquelle cet événement s’est produit
`sf_created_at` | `timestamp`, `null` | lorsque cet événement a été repris par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_NEWSFEEDCARD_ABORT_SHARED {#USERS_MESSAGES_NEWSFEEDCARD_ABORT_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID de l'utilisateur de Braze qui a effectué cet événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`app_group_id` | `null,` `string` | BSON ID du groupe d'applications auquel appartient cet utilisateur
`app_group_api_id` | `null,` `string` | ID API du groupe d'applications auquel appartient cet utilisateur
`time` | `int` | Horodatage UNIX auquel l'événement s'est produit
`app_api_id` | `null,` `string` | ID API de l’application sur laquelle cet événement s’est produit
`card_api_id` | `null,` `string` | ID API de la carte
`gender` | `null,` `string` | [Sexe de l'utilisateur
`country` | `null,` `string` | [Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [Langue de l'utilisateur
`device_id` | `null,` `string` | ID de l’appareil sur lequel l’événement s’est produit
`sdk_version` | `null,` `string` | Version du SDK de Braze utilisée lors de l'événement
`platform` | `null,` `string` | Plate-forme de l'appareil
`os_version` | `null,` `string` | Version du système d'exploitation de l'appareil
`device_model` | `null,` `string` | Modèle de l'appareil
`resolution` | `null,` `string` | Résolution de l'appareil
`carrier` | `null,` `string` | Opérateur de l'appareil
`browser` | `null,` `string` | Navigateur de l'appareil - extrait de user_agent \- sur lequel l'ouverture s'est produite
`abort_type` | `null,` `string` | Type d'abandon, l'un des suivants ['liquid_abort_message', 'quiet_hours', 'rate_limit']
`abort_log` | `null,` `string` | [PII] Message du journal décrivant les détails de l'abandon (jusqu'à 128 caractères)
`sf_created_at` | `timestamp`, `null` | lorsque cet événement a été repris par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_NEWSFEEDCARD_CLICK_SHARED {#USERS_MESSAGES_NEWSFEEDCARD_CLICK_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID de l'utilisateur de Braze qui a effectué cet événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`app_group_id` | `null,` `string` | BSON ID du groupe d'applications auquel appartient cet utilisateur
`app_group_api_id` | `null,` `string` | ID API du groupe d'applications auquel appartient cet utilisateur
`time` | `int` | Horodatage UNIX auquel l'événement s'est produit
`app_api_id` | `null,` `string` | ID API de l’application sur laquelle cet événement s’est produit
`card_api_id` | `null,` `string` | ID API de la carte
`gender` | `null,` `string` | [Sexe de l'utilisateur
`country` | `null,` `string` | [Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [Langue de l'utilisateur
`device_id` | `null,` `string` | ID de l’appareil sur lequel l’événement s’est produit
`sdk_version` | `null,` `string` | Version du SDK de Braze utilisée lors de l'événement
`platform` | `null,` `string` | Plate-forme de l'appareil
`os_version` | `null,` `string` | Version du système d'exploitation de l'appareil
`device_model` | `null,` `string` | Modèle de l'appareil
`resolution` | `null,` `string` | Résolution de l'appareil
`carrier` | `null,` `string` | Opérateur de l'appareil
`browser` | `null,` `string` | Navigateur de l'appareil - extrait de user_agent \- sur lequel l'ouverture s'est produite
`sf_created_at` | `timestamp`, `null` | lorsque cet événement a été repris par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_NEWSFEEDCARD_IMPRESSION_SHARED {#USERS_MESSAGES_NEWSFEEDCARD_IMPRESSION_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID de l'utilisateur de Braze qui a effectué cet événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`app_group_id` | `null,` `string` | BSON ID du groupe d'applications auquel appartient cet utilisateur
`app_group_api_id` | `null,` `string` | ID API du groupe d'applications auquel appartient cet utilisateur
`time` | `int` | Horodatage UNIX auquel l'événement s'est produit
`app_api_id` | `null,` `string` | ID API de l’application sur laquelle cet événement s’est produit
`card_api_id` | `null,` `string` | ID API de la carte
`gender` | `null,` `string` | [Sexe de l'utilisateur
`country` | `null,` `string` | [Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [Langue de l'utilisateur
`device_id` | `null,` `string` | ID de l’appareil sur lequel l’événement s’est produit
`sdk_version` | `null,` `string` | Version du SDK de Braze utilisée lors de l'événement
`platform` | `null,` `string` | Plate-forme de l'appareil
`os_version` | `null,` `string` | Version du système d'exploitation de l'appareil
`device_model` | `null,` `string` | Modèle de l'appareil
`resolution` | `null,` `string` | Résolution de l'appareil
`carrier` | `null,` `string` | Opérateur de l'appareil
`browser` | `null,` `string` | Navigateur de l'appareil - extrait de user_agent \- sur lequel l'ouverture s'est produite
`sf_created_at` | `timestamp`, `null` | lorsque cet événement a été repris par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_PUSHNOTIFICATION_ABORT_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_ABORT_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`device_id` | `null,` `string` | `device_id` auquel nous avons fait une tentative de livraison
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`time` | `int` | horodatage Unix du moment où l’événement s’est produit
`app_api_id` | `null,` `string` | ID API de l’application sur laquelle cet événement s’est produit
`dispatch_id` | `null,` `string` | ID de l’envoi auquel appartient ce message
`send_id` | `null,` `string` | ID d'envoi de message auquel ce message appartient
`campaign_id` | `null,` `string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle appartient cet événement
`message_variation_api_id` | `null,` `string` | ID API de la variation de message que l’utilisateur a reçue
`canvas_id` | `null,` `string` | ID de la Braze à usage interne de la toile à laquelle cet événement appartient
`canvas_api_id` | `null,` `string` | ID API du Canvas auquel appartient cet événement
`canvas_variation_api_id` | `null,` `string` | ID API de la variation de Canvas à laquelle appartient cet événement
`canvas_step_api_id` | `null,` `string` | ID API de l'étape de Canvas auquel appartient cet événement
`canvas_step_message_variation_api_id` | `null,` `string` | ID API de la variation de message de l'étape de Canvas que l’utilisateur a reçue
`gender` | `null,` `string` | [Sexe de l'utilisateur
`country` | `null,` `string` | [Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [Langue de l'utilisateur
`platform` | `string` | Plate-forme de l'appareil
`abort_type` | `null,` `string` | Type d'abandon, l'un des suivants ['liquid_abort_message', 'quiet_hours', 'rate_limit']
`abort_log` | `null,` `string` | [PII] Message du journal décrivant les détails de l'abandon (maximum de 2 000 caractères)
`app_group_id` | `null,` `string` | BSON ID du groupe d'applications auquel appartient cet utilisateur
`sf_created_at` | `timestamp`, `null` | lorsque cet événement a été repris par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_PUSHNOTIFICATION_BOUNCE_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_BOUNCE_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`push_token` | `null,` `string` | Jeton de notification push qui a rebondi
`device_id` | `null,` `string` | `device_id` auquel nous avons fait une tentative de livraison qui a rebondi
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`time` | `int` | horodatage Unix du moment où l’événement s’est produit
`app_api_id` | `null,` `string` | ID API de l’application sur laquelle cet événement s’est produit
`dispatch_id` | `null,` `string` | ID de l’envoi auquel appartient ce message
`send_id` | `null,` `string` | ID d'envoi de message auquel ce message appartient
`campaign_id` | `null,` `string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle appartient cet événement
`message_variation_api_id` | `null,` `string` | ID API de la variation de message que l’utilisateur a reçue
`canvas_id` | `null,` `string` | ID de la Braze à usage interne de la toile à laquelle cet événement appartient
`canvas_api_id` | `null,` `string` | ID API du Canvas auquel appartient cet événement
`canvas_variation_api_id` | `null,` `string` | ID API de la variation de Canvas à laquelle appartient cet événement
`canvas_step_api_id` | `null,` `string` | ID API de l'étape de Canvas auquel appartient cet événement
`canvas_step_message_variation_api_id` | `null,` `string` | ID API de la variation de message de l'étape de Canvas que l’utilisateur a reçue
`gender` | `null,` `string` | [Sexe de l'utilisateur
`country` | `null,` `string` | [Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [Langue de l'utilisateur
`platform` | `null,` `string` | Plate-forme de l'appareil
`ad_id` | `null,` `string` | [PII] ID publicitaire de l'appareil pour lequel nous avons effectué une tentative de réception/distribution.
`ad_id_type` | `null,` `string` | Type de l'ID publicitaire
`ad_tracking_enabled` | `null, boolean` | Si le suivi est activé ou non pour la publicité
`app_group_id` | `null,` `string` | BSON ID du groupe d'applications auquel appartient cet utilisateur
`sf_created_at` | `timestamp`, `null` | lorsque cet événement a été repris par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_PUSHNOTIFICATION_INFLUENCEDOPEN_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_INFLUENCEDOPEN_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`time` | `int` | horodatage Unix du moment où l’événement s’est produit
`app_api_id` | `null,` `string` | ID API de l’application sur laquelle cet événement s’est produit
`dispatch_id` | `null,` `string` | ID de l’envoi auquel appartient ce message
`send_id` | `null,` `string` | ID d'envoi de message auquel ce message appartient
`campaign_id` | `null,` `string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle appartient cet événement
`message_variation_api_id` | `null,` `string` | ID API de la variation de message que l’utilisateur a reçue
`canvas_id` | `null,` `string` | ID de la Braze à usage interne de la toile à laquelle cet événement appartient
`canvas_api_id` | `null,` `string` | ID API du Canvas auquel appartient cet événement
`canvas_variation_api_id` | `null,` `string` | ID API de la variation de Canvas à laquelle appartient cet événement
`canvas_step_api_id` | `null,` `string` | ID API de l'étape de Canvas auquel appartient cet événement
`canvas_step_message_variation_api_id` | `null,` `string` | ID API de la variation de message de l'étape de Canvas que l’utilisateur a reçue
`gender` | `null,` `string` | [Sexe de l'utilisateur
`country` | `null,` `string` | [Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [Langue de l'utilisateur
`device_id` | `null,` `string` | ID de l’appareil sur lequel l’événement s’est produit
`sdk_version` | `null,` `string` | Version du SDK de Braze utilisée lors de l'événement
`platform` | `null,` `string` | Plate-forme de l'appareil
`os_version` | `null,` `string` | Version du système d'exploitation de l'appareil
`device_model` | `null,` `string` | Modèle de l'appareil
`resolution` | `null,` `string` | Résolution de l'appareil
`carrier` | `null,` `string` | Opérateur de l'appareil
`browser` | `null,` `string` | Navigateur de l'appareil
`app_group_id` | `null,` `string` | BSON ID du groupe d'applications auquel appartient cet utilisateur
`sf_created_at` | `timestamp`, `null` | lorsque cet événement a été repris par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Il y a USERS_MESSAGES_PUSHNOTIFICATION_IOSFOREGROUND_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_IOSFOREGROUND_SHARED}

{% alert important %}
Cet événement n'est pas pris en charge par le [SDK Swift](https://github.com/braze-inc/braze-swift-sdk) et est obsolète dans le [SDK Obj-C.](https://github.com/Appboy/appboy-ios-sdk)
{% endalert %}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`time` | `int` | horodatage Unix du moment où l’événement s’est produit
`app_api_id` | `null,` `string` | ID API de l’application sur laquelle cet événement s’est produit
`dispatch_id` | `null,` `string` | ID de l’envoi auquel appartient ce message
`send_id` | `null,` `string` | ID d'envoi de message auquel ce message appartient
`campaign_id` | `null,` `string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle appartient cet événement
`message_variation_api_id` | `null,` `string` | ID API de la variation de message que l’utilisateur a reçue
`canvas_id` | `null,` `string` | ID de la Braze à usage interne de la toile à laquelle cet événement appartient
`canvas_api_id` | `null,` `string` | ID API du Canvas auquel appartient cet événement
`canvas_variation_api_id` | `null,` `string` | ID API de la variation de Canvas à laquelle appartient cet événement
`canvas_step_api_id` | `null,` `string` | ID API de l'étape de Canvas auquel appartient cet événement
`canvas_step_message_variation_api_id` | `null,` `string` | ID API de la variation de message de l'étape de Canvas que l’utilisateur a reçue
`gender` | `null,` `string` | [Sexe de l'utilisateur
`country` | `null,` `string` | [Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [Langue de l'utilisateur
`device_id` | `null,` `string` | ID de l’appareil sur lequel l’événement s’est produit
`sdk_version` | `null,` `string` | Version du SDK de Braze utilisée lors de l'événement
`platform` | `null,` `string` | Plate-forme de l'appareil
`os_version` | `null,` `string` | Version du système d'exploitation de l'appareil
`device_model` | `null,` `string` | Modèle de l'appareil
`resolution` | `null,` `string` | Résolution de l'appareil
`carrier` | `null,` `string` | Opérateur de l'appareil
`browser` | `null,` `string` | Navigateur de l'appareil
`ad_id` | `null,` `string` | [PII] ID publicitaire de l'appareil pour lequel nous avons effectué une tentative de réception/distribution.
`ad_id_type` | `null,` `string` | Type de l'ID publicitaire
`ad_tracking_enabled` | `null, boolean` | Si le suivi est activé ou non pour la publicité
`app_group_id` | `null,` `string` | BSON ID du groupe d'applications auquel appartient cet utilisateur
`sf_created_at` | `timestamp`, `null` | lorsque cet événement a été repris par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_PUSHNOTIFICATION_OPEN_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_OPEN_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`time` | `int` | horodatage Unix du moment où l’événement s’est produit
`app_api_id` | `null,` `string` | ID API de l’application sur laquelle cet événement s’est produit
`dispatch_id` | `null,` `string` | ID de l’envoi auquel appartient ce message
`send_id` | `null,` `string` | ID d'envoi de message auquel ce message appartient
`campaign_id` | `null,` `string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle appartient cet événement
`message_variation_api_id` | `null,` `string` | ID API de la variation de message que l’utilisateur a reçue
`canvas_id` | `null,` `string` | ID de la Braze à usage interne de la toile à laquelle cet événement appartient
`canvas_api_id` | `null,` `string` | ID API du Canvas auquel appartient cet événement
`canvas_variation_api_id` | `null,` `string` | ID API de la variation de Canvas à laquelle appartient cet événement
`canvas_step_api_id` | `null,` `string` | ID API de l'étape de Canvas auquel appartient cet événement
`canvas_step_message_variation_api_id` | `null,` `string` | ID API de la variation de message de l'étape de Canvas que l’utilisateur a reçue
`gender` | `null,` `string` | [Sexe de l'utilisateur
`country` | `null,` `string` | [Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [Langue de l'utilisateur
`device_id` | `null,` `string` | ID de l’appareil sur lequel l’événement s’est produit
`sdk_version` | `null,` `string` | Version du SDK de Braze utilisée lors de l'événement
`platform` | `null,` `string` | Plate-forme de l'appareil
`os_version` | `null,` `string` | Version du système d'exploitation de l'appareil
`device_model` | `null,` `string` | Modèle de l'appareil
`resolution` | `null,` `string` | Résolution de l'appareil
`carrier` | `null,` `string` | Opérateur de l'appareil
`browser` | `null,` `string` | Navigateur de l'appareil
`button_string` | `null,` `string` | Identifiant (button_string) du bouton de notification push cliqué. null s'il ne s'agit pas d'un clic sur un bouton
`button_action_type` | `null,` `string` | Type d’action du bouton de la notification push. L'un des éléments suivants : [URI, DEEP_LINK, NONE, CLOSE]. Nulle si elle ne provient pas d'un clic sur un bouton.
`slide_id` | `null,` `string` | identifiant de diapositive de la diapositive de carrousel de notification push sur laquelle l’utilisateur a cliqué
`slide_action_type` | `null,` `string` | Type d'action de la diapositive du carrousel de poussée
`ad_id` | `null,` `string` | [PII] ID publicitaire de l'appareil pour lequel nous avons effectué une tentative de réception/distribution.
`ad_id_type` | `null,` `string` | Type de l'ID publicitaire
`ad_tracking_enabled` | `null, boolean` | Si le suivi est activé ou non pour la publicité
`app_group_id` | `null,` `string` | BSON ID du groupe d'applications auquel appartient cet utilisateur
`sf_created_at` | `timestamp`, `null` | lorsque cet événement a été repris par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_PUSHNOTIFICATION_SEND_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_SEND_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`push_token` | `null,` `string` | Jeton de notification push auquel nous avons fait une tentative de distribution
`device_id` | `null,` `string` | `device_id` auquel nous avons fait une tentative de livraison
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`time` | `int` | horodatage Unix du moment où l’événement s’est produit
`app_api_id` | `null,` `string` | ID API de l’application sur laquelle cet événement s’est produit
`dispatch_id` | `null,` `string` | ID de l’envoi auquel appartient ce message
`send_id` | `null,` `string` | ID d'envoi de message auquel ce message appartient
`campaign_id` | `null,` `string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle appartient cet événement
`message_variation_api_id` | `null,` `string` | ID API de la variation de message que l’utilisateur a reçue
`canvas_id` | `null,` `string` | ID de la Braze à usage interne de la toile à laquelle cet événement appartient
`canvas_api_id` | `null,` `string` | ID API du Canvas auquel appartient cet événement
`canvas_variation_api_id` | `null,` `string` | ID API de la variation de Canvas à laquelle appartient cet événement
`canvas_step_api_id` | `null,` `string` | ID API de l'étape de Canvas auquel appartient cet événement
`canvas_step_message_variation_api_id` | `null,` `string` | ID API de la variation de message de l'étape de Canvas que l’utilisateur a reçue
`gender` | `null,` `string` | [Sexe de l'utilisateur
`country` | `null,` `string` | [Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [Langue de l'utilisateur
`platform` | `string` | Plate-forme de l'appareil
`ad_id` | `null,` `string` | [PII] ID publicitaire de l'appareil pour lequel nous avons effectué une tentative de réception/distribution.
`ad_id_type` | `null,` `string` | Type de l'ID publicitaire
`ad_tracking_enabled` | `null, boolean` | Si le suivi est activé ou non pour la publicité
`app_group_id` | `null,` `string` | BSON ID du groupe d'applications auquel appartient cet utilisateur
`message_extras` | `null,` `string` | [Une chaîne JSON des paires clé-valeur balisées lors du rendu liquide.
`is_sampled` | `null,` `string` | Indique si l'envoi push a été échantillonné et s'attend à un événement de réception/distribution.
`locale_key` | `null,` `string` | [La clé correspondant aux traductions (par exemple 'en-us') utilisées pour composer ce message (null pour la valeur par défaut).
`sf_created_at` | `timestamp`, `null` | lorsque cet événement a été repris par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_RCS_ABORT_SHARED {#USERS_MESSAGES_RCS_ABORT_SHARED}

Champ | Type | Description
------|------|------------
`app_group_api_id` | `null,` `string` | ID API du groupe d'applications auquel appartient cet utilisateur
`app_group_id` | `null,` `string` | BSON ID du groupe d'applications auquel appartient cet utilisateur
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`id` | `string` | ID unique au niveau mondial pour cet événement
`time` | `int` | Horodatage UNIX auquel l'événement s'est produit
`user_id` | `string` | ID de l'utilisateur de Braze qui a effectué cet événement
`abort_log` | `null,` `string` | [PII] Message du journal décrivant les détails de l'abandon (jusqu'à 128 caractères)
`abort_type` | `null,` `string` | Type d'abandon, l'un des suivants ['liquid_abort_message', 'quiet_hours', 'rate_limit']
`campaign_name` | `null,` `string` | Nom de la campagne
`canvas_id` | `null,` `string` | BSON ID de la toile à laquelle cet événement appartient
`canvas_name` | `null,` `string` | Nom du canvas
`canvas_step_name` | `null,` `string` | Nom de l'étape du canvas
`canvas_variation_name` | `null,` `string` | Nom de la variation de canvas reçue par cet utilisateur
`message_variation_name` | `null,` `string` | Nom de la variation du message
`subscription_group_api_id` | `string` | ID d’API du groupe d'abonnement
`message_variation_api_id` | `null,` `string` | ID API de la variation de message que l’utilisateur a reçue
`canvas_variation_api_id` | `null,` `string` | ID API de la variation de Canvas à laquelle appartient cet événement
`canvas_step_api_id` | `null,` `string` | ID API de l'étape de Canvas auquel appartient cet événement
`canvas_step_message_variation_api_id` | `null,` `string` | ID API de la variation de message de l'étape de Canvas que l’utilisateur a reçue
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle appartient cet événement
`sf_created_at` | `timestamp`, `null` | lorsque cet événement a été repris par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_RCS_CLICK_SHARED {#USERS_MESSAGES_RCS_CLICK_SHARED}

Champ | Type | Description
------|------|------------
`app_group_api_id` | `null,` `string` | ID API du groupe d'applications auquel appartient cet utilisateur
`app_group_id` | `null,` `string` | BSON ID du groupe d'applications auquel appartient cet utilisateur
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`id` | `string` | ID unique au niveau mondial pour cet événement
`time` | `int` | Horodatage UNIX auquel l'événement s'est produit
`user_id` | `string` | ID de l'utilisateur de Braze qui a effectué cet événement
`campaign_name` | `null,` `string` | Nom de la campagne
`canvas_id` | `null,` `string` | BSON ID de la toile à laquelle cet événement appartient
`canvas_name` | `null,` `string` | Nom du canvas
`canvas_step_name` | `null,` `string` | Nom de l'étape du canvas
`device_id` | `null,` `string` | ID de l’appareil sur lequel l’événement s’est produit
`is_suspected_bot_click` | `null, boolean` | Si cet événement a été traité comme un événement bot
`message_variation_name` | `null,` `string` | Nom de la variation du message
`send_id` | `null,` `string` | ID d'envoi de message auquel ce message appartient
`short_url` | `null,` `string` | URL raccourcie qui a été cliquée
`suspected_bot_click_reason` | `null,` `string` | Pourquoi cet événement a été classé comme bot
`user_agent` | `null,` `string` | Agent utilisateur sur lequel le signalement du courrier indésirable a eu lieu
`user_phone_number` | `null,` `string` | [Le numéro de téléphone de l'utilisateur à partir duquel le message a été reçu.
`message_variation_api_id` | `null,` `string` | ID API de la variation de message que l’utilisateur a reçue
`canvas_variation_api_id` | `null,` `string` | ID API de la variation de Canvas à laquelle appartient cet événement
`canvas_step_api_id` | `null,` `string` | ID API de l'étape de Canvas auquel appartient cet événement
`canvas_step_message_variation_api_id` | `null,` `string` | ID API de la variation de message de l'étape de Canvas que l’utilisateur a reçue
`interaction_type` | `null,` `string` | Le type d'interaction qui a généré le clic. Exemple de valeurs chaîne de caractères : Texte URL, Réponse, OpenURL
`element_label` | `null,` `string` | Détails facultatifs concernant l'élément cliqué, tels que le texte d'une suggestion de réponse ou d'un bouton.
`element_type` | `null,` `string` | Indique si une interaction_type commune aux suggestions et aux boutons provient d'une suggestion ou d'un bouton. Exemples : Suggestion, bouton
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle appartient cet événement
`url` | `null,` `string` | URL sur laquelle l’utilisateur a cliqué
`subscription_group_api_id` | `string` | ID d’API du groupe d'abonnement
`canvas_variation_name` | `null,` `string` | Nom de la variation de canvas reçue par cet utilisateur
`sf_created_at` | `timestamp`, `null` | lorsque cet événement a été repris par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_RCS_DELIVERY_SHARED {#USERS_MESSAGES_RCS_DELIVERY_SHARED}

Champ | Type | Description
------|------|------------
`app_group_api_id` | `null,` `string` | ID API du groupe d'applications auquel appartient cet utilisateur
`app_group_id` | `null,` `string` | BSON ID du groupe d'applications auquel appartient cet utilisateur
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`id` | `string` | ID unique au niveau mondial pour cet événement
`time` | `int` | Horodatage UNIX auquel l'événement s'est produit
`user_id` | `string` | ID de l'utilisateur de Braze qui a effectué cet événement
`campaign_name` | `null,` `string` | Nom de la campagne
`canvas_id` | `null,` `string` | BSON ID de la toile à laquelle cet événement appartient
`canvas_name` | `null,` `string` | Nom du canvas
`canvas_step_name` | `null,` `string` | Nom de l'étape du canvas
`canvas_variation_name` | `null,` `string` | Nom de la variation de canvas reçue par cet utilisateur
`device_id` | `null,` `string` | ID de l’appareil sur lequel l’événement s’est produit
`dispatch_id` | `null,` `string` | ID de l’envoi auquel appartient ce message
`message_variation_name` | `null,` `string` | Nom de la variation du message
`send_id` | `null,` `string` | ID d'envoi de message auquel ce message appartient
`subscription_group_api_id` | `string` | ID d’API du groupe d'abonnement
`to_phone_number` | `null,` `string` | [PII] Numéro de téléphone de l'utilisateur recevant le message au format e.164 (par exemple +14155552671)
`message_variation_api_id` | `null,` `string` | ID API de la variation de message que l’utilisateur a reçue
`canvas_variation_api_id` | `null,` `string` | ID API de la variation de Canvas à laquelle appartient cet événement
`canvas_step_api_id` | `null,` `string` | ID API de l'étape de Canvas auquel appartient cet événement
`canvas_step_message_variation_api_id` | `null,` `string` | ID API de la variation de message de l'étape de Canvas que l’utilisateur a reçue
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle appartient cet événement
`from_rcs_sender` | `null,` `string` | L'ID de l'expéditeur RCS ou le nom de l'agent utilisé pour envoyer le message.
`sf_created_at` | `timestamp`, `null` | lorsque cet événement a été repris par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_RCS_INBOUNDRECEIVE_SHARED {#USERS_MESSAGES_RCS_INBOUNDRECEIVE_SHARED}

Champ | Type | Description
------|------|------------
`app_group_api_id` | `null,` `string` | ID API du groupe d'applications auquel appartient cet utilisateur
`app_group_id` | `null,` `string` | BSON ID du groupe d'applications auquel appartient cet utilisateur
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`id` | `string` | ID unique au niveau mondial pour cet événement
`time` | `int` | Horodatage UNIX auquel l'événement s'est produit
`user_id` | `string` | ID de l'utilisateur de Braze qui a effectué cet événement
`action` | `null,` `string` | Action entreprise en réponse à ce message. (par exemple Abonné, Désabonné ou Aucune).
`campaign_name` | `null,` `string` | Nom de la campagne
`canvas_id` | `null,` `string` | BSON ID de la toile à laquelle cet événement appartient
`canvas_name` | `null,` `string` | Nom du canvas
`canvas_step_name` | `null,` `string` | Nom de l'étape du canvas
`media_urls` | `null,` `string` | URL des médias de l'utilisateur
`message_variation_name` | `null,` `string` | Nom de la variation du message
`send_id` | `null,` `string` | ID d'envoi de message auquel ce message appartient
`user_phone_number` | `null,` `string` | [Le numéro de téléphone de l'utilisateur à partir duquel le message a été reçu.
`subscription_group_api_id` | `string` | ID d’API du groupe d'abonnement
`message_body` | `null,` `string` | Réponse dactylographiée de l'utilisateur
`to_rcs_sender` | `null,` `string` | L'expéditeur du RCS entrant auquel le message a été envoyé
`message_variation_api_id` | `null,` `string` | ID API de la variation de message que l’utilisateur a reçue
`canvas_step_api_id` | `null,` `string` | ID API de l'étape de Canvas auquel appartient cet événement
`canvas_variation_api_id` | `null,` `string` | ID API de la variation de Canvas à laquelle appartient cet événement
`canvas_step_message_variation_api_id` | `null,` `string` | ID API de la variation de message de l'étape de Canvas que l’utilisateur a reçue
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle appartient cet événement
`campaign_id` | `null,` `string` | BSON ID de la campagne à laquelle cet événement appartient
`sf_created_at` | `timestamp`, `null` | lorsque cet événement a été repris par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_RCS_READ_SHARED {#USERS_MESSAGES_RCS_READ_SHARED}

Champ | Type | Description
------|------|------------
`app_group_api_id` | `null,` `string` | ID API du groupe d'applications auquel appartient cet utilisateur
`app_group_id` | `null,` `string` | BSON ID du groupe d'applications auquel appartient cet utilisateur
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`id` | `string` | ID unique au niveau mondial pour cet événement
`time` | `int` | Horodatage UNIX auquel l'événement s'est produit
`user_id` | `string` | ID de l'utilisateur de Braze qui a effectué cet événement
`campaign_name` | `null,` `string` | Nom de la campagne
`canvas_id` | `null,` `string` | BSON ID de la toile à laquelle cet événement appartient
`canvas_name` | `null,` `string` | Nom du canvas
`canvas_step_name` | `null,` `string` | Nom de l'étape du canvas
`canvas_variation_name` | `null,` `string` | Nom de la variation de canvas reçue par cet utilisateur
`message_variation_name` | `null,` `string` | Nom de la variation du message
`to_phone_number` | `null,` `string` | [PII] Numéro de téléphone de l'utilisateur recevant le message au format e.164 (par exemple +14155552671)
`message_variation_api_id` | `null,` `string` | ID API de la variation de message que l’utilisateur a reçue
`canvas_variation_api_id` | `null,` `string` | ID API de la variation de Canvas à laquelle appartient cet événement
`canvas_step_api_id` | `null,` `string` | ID API de l'étape de Canvas auquel appartient cet événement
`canvas_step_message_variation_api_id` | `null,` `string` | ID API de la variation de message de l'étape de Canvas que l’utilisateur a reçue
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle appartient cet événement
`sf_created_at` | `timestamp`, `null` | lorsque cet événement a été repris par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_RCS_REJECTION_SHARED {#USERS_MESSAGES_RCS_REJECTION_SHARED}

Champ | Type | Description
------|------|------------
`app_group_api_id` | `null,` `string` | ID API du groupe d'applications auquel appartient cet utilisateur
`app_group_id` | `null,` `string` | BSON ID du groupe d'applications auquel appartient cet utilisateur
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`id` | `string` | ID unique au niveau mondial pour cet événement
`time` | `int` | Horodatage UNIX auquel l'événement s'est produit
`user_id` | `string` | ID de l'utilisateur de Braze qui a effectué cet événement
`campaign_name` | `null,` `string` | Nom de la campagne
`canvas_id` | `null,` `string` | BSON ID de la toile à laquelle cet événement appartient
`canvas_name` | `null,` `string` | Nom du canvas
`canvas_step_name` | `null,` `string` | Nom de l'étape du canvas
`canvas_variation_name` | `null,` `string` | Nom de la variation de canvas reçue par cet utilisateur
`device_id` | `null,` `string` | ID de l’appareil sur lequel l’événement s’est produit
`dispatch_id` | `null,` `string` | ID de l’envoi auquel appartient ce message
`error` | `null,` `string` | Nom de l'erreur
`from_rcs_sender` | `null,` `string` | L'ID de l'expéditeur RCS ou le nom de l'agent utilisé pour envoyer le message.
`is_sms_fallback` | `null, boolean` | Indique si une procédure de secours par SMS a été tentée pour ce message RCS rejeté. Il est lié/apparié à l'événement de réception/distribution de SMS
`message_variation_name` | `null,` `string` | Nom de la variation du message
`provider_error_code` | `null,` `string` | Code d'erreur du fournisseur
`send_id` | `null,` `string` | ID d'envoi de message auquel ce message appartient
`subscription_group_api_id` | `string` | ID d’API du groupe d'abonnement
`message_variation_api_id` | `null,` `string` | ID API de la variation de message que l’utilisateur a reçue
`canvas_variation_api_id` | `null,` `string` | ID API de la variation de Canvas à laquelle appartient cet événement
`canvas_step_api_id` | `null,` `string` | ID API de l'étape de Canvas auquel appartient cet événement
`to_phone_number` | `null,` `string` | [PII] Numéro de téléphone de l'utilisateur recevant le message au format e.164 (par exemple +14155552671)
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle appartient cet événement
`canvas_step_message_variation_api_id` | `null,` `string` | ID API de la variation de message de l'étape de Canvas que l’utilisateur a reçue
`sf_created_at` | `timestamp`, `null` | lorsque cet événement a été repris par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_RCS_SEND_SHARED {#USERS_MESSAGES_RCS_SEND_SHARED}

Champ | Type | Description
------|------|------------
`app_group_api_id` | `null,` `string` | ID API du groupe d'applications auquel appartient cet utilisateur
`app_group_id` | `null,` `string` | BSON ID du groupe d'applications auquel appartient cet utilisateur
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`id` | `string` | ID unique au niveau mondial pour cet événement
`time` | `int` | Horodatage UNIX auquel l'événement s'est produit
`user_id` | `string` | ID de l'utilisateur de Braze qui a effectué cet événement
`campaign_name` | `null,` `string` | Nom de la campagne
`canvas_id` | `null,` `string` | BSON ID de la toile à laquelle cet événement appartient
`canvas_name` | `null,` `string` | Nom du canvas
`canvas_step_name` | `null,` `string` | Nom de l'étape du canvas
`canvas_variation_name` | `null,` `string` | Nom de la variation de canvas reçue par cet utilisateur
`category` | `null,` `string` | Nom de la catégorie de mots-clés, uniquement pour les messages de réponse automatique : "opt-in", "opt-out", "help", ou valeur personnalisée.
`device_id` | `null,` `string` | ID de l’appareil sur lequel l’événement s’est produit
`dispatch_id` | `null,` `string` | ID de l’envoi auquel appartient ce message
`from_rcs_sender` | `null,` `string` | L'ID de l'expéditeur RCS ou le nom de l'agent utilisé pour envoyer le message.
`message_extras` | `null,` `string` | Une chaîne JSON des paires clé-valeur étiquetées lors du rendu liquide.
`message_variation_name` | `null,` `string` | Nom de la variation du message
`send_id` | `null,` `string` | ID d'envoi de message auquel ce message appartient
`subscription_group_api_id` | `string` | ID d’API du groupe d'abonnement
`to_phone_number` | `null,` `string` | [PII] Numéro de téléphone de l'utilisateur recevant le message au format e.164 (par exemple +14155552671)
`message_variation_api_id` | `null,` `string` | ID API de la variation de message que l’utilisateur a reçue
`canvas_variation_api_id` | `null,` `string` | ID API de la variation de Canvas à laquelle appartient cet événement
`canvas_step_message_variation_api_id` | `null,` `string` | ID API de la variation de message de l'étape de Canvas que l’utilisateur a reçue
`canvas_step_api_id` | `null,` `string` | ID API de l'étape de Canvas auquel appartient cet événement
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle appartient cet événement
`sf_created_at` | `timestamp`, `null` | lorsque cet événement a été repris par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_ABORT_SHARED {#USERS_MESSAGES_SMS_ABORT_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`time` | `int` | horodatage Unix du moment où l’événement s’est produit
`campaign_id` | `null,` `string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle appartient cet événement
`message_variation_api_id` | `null,` `string` | ID API de la variation de message que l’utilisateur a reçue
`canvas_id` | `null,` `string` | ID de la Braze à usage interne de la toile à laquelle cet événement appartient
`canvas_api_id` | `null,` `string` | ID API du Canvas auquel appartient cet événement
`canvas_variation_api_id` | `null,` `string` | ID API de la variation de Canvas à laquelle appartient cet événement
`canvas_step_api_id` | `null,` `string` | ID API de l'étape de Canvas auquel appartient cet événement
`canvas_step_message_variation_api_id` | `null,` `string` | ID API de la variation de message de l'étape de Canvas que l’utilisateur a reçue
`subscription_group_api_id` | `null,` `string` | ID externe du groupe d'abonnement
`abort_type` | `null,` `string` | Type d'abandon, l'un des suivants ['liquid_abort_message', 'quiet_hours', 'rate_limit']
`abort_log` | `null,` `string` | [PII] Message du journal décrivant les détails de l'abandon (maximum de 2 000 caractères)
`app_group_id` | `null,` `string` | BSON ID du groupe d'applications auquel appartient cet utilisateur
`sf_created_at` | `timestamp`, `null` | lorsque cet événement a été repris par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_CARRIERSEND_SHARED {#USERS_MESSAGES_SMS_CARRIERSEND_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`device_id` | `null,` `string` | `device_id` qui est lié à cet utilisateur si celui-ci est anonyme
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`time` | `int` | horodatage Unix du moment où l’événement s’est produit
`dispatch_id` | `null,` `string` | ID de l’envoi auquel appartient ce message
`send_id` | `null,` `string` | ID d'envoi de message auquel ce message appartient
`campaign_id` | `null,` `string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle appartient cet événement
`message_variation_api_id` | `null,` `string` | ID API de la variation de message que l’utilisateur a reçue
`canvas_id` | `null,` `string` | ID de la Braze à usage interne de la toile à laquelle cet événement appartient
`canvas_api_id` | `null,` `string` | ID API du Canvas auquel appartient cet événement
`canvas_variation_api_id` | `null,` `string` | ID API de la variation de Canvas à laquelle appartient cet événement
`canvas_step_api_id` | `null,` `string` | ID API de l'étape de Canvas auquel appartient cet événement
`canvas_step_message_variation_api_id` | `null,` `string` | ID API de la variation de message de l'étape de Canvas que l’utilisateur a reçue
`gender` | `null,` `string` | [Sexe de l'utilisateur
`country` | `null,` `string` | [Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [Langue de l'utilisateur
`to_phone_number` | `null,` `string` | Numéro de téléphone [PII] du destinataire
`from_phone_number` | `null,` `string` | numéro de téléphone à partir duquel le message SMS a été envoyé
`subscription_group_api_id` | `null,` `string` | ID externe du groupe d’abonnement
`app_group_id` | `null,` `string` | BSON ID du groupe d'applications auquel appartient cet utilisateur
`sf_created_at` | `timestamp`, `null` | lorsque cet événement a été repris par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_DELIVERY_SHARED {#USERS_MESSAGES_SMS_DELIVERY_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`device_id` | `null,` `string` | `device_id` qui est lié à cet utilisateur si celui-ci est anonyme
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`time` | `int` | horodatage Unix du moment où l’événement s’est produit
`dispatch_id` | `null,` `string` | ID de l’envoi auquel appartient ce message
`send_id` | `null,` `string` | ID d'envoi de message auquel ce message appartient
`campaign_id` | `null,` `string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle appartient cet événement
`message_variation_api_id` | `null,` `string` | ID API de la variation de message que l’utilisateur a reçue
`canvas_id` | `null,` `string` | ID de la Braze à usage interne de la toile à laquelle cet événement appartient
`canvas_api_id` | `null,` `string` | ID API du Canvas auquel appartient cet événement
`canvas_variation_api_id` | `null,` `string` | ID API de la variation de Canvas à laquelle appartient cet événement
`canvas_step_api_id` | `null,` `string` | ID API de l'étape de Canvas auquel appartient cet événement
`canvas_step_message_variation_api_id` | `null,` `string` | ID API de la variation de message de l'étape de Canvas que l’utilisateur a reçue
`gender` | `null,` `string` | [Sexe de l'utilisateur
`country` | `null,` `string` | [Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [Langue de l'utilisateur
`to_phone_number` | `null,` `string` | Numéro de téléphone [PII] du destinataire
`from_phone_number` | `null,` `string` | Numéro de téléphone à partir duquel le message SMS a été envoyé
`subscription_group_api_id` | `null,` `string` | ID externe du groupe d'abonnement
`app_group_id` | `null,` `string` | BSON ID du groupe d'applications auquel appartient cet utilisateur
`is_sms_fallback` | `null, boolean` | Indique si une procédure de secours par SMS a été tentée pour ce message RCS rejeté. Il est lié/apparié à l'événement de réception/distribution de SMS
`sf_created_at` | `timestamp`, `null` | lorsque cet événement a été repris par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED {#USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`device_id` | `null,` `string` | `device_id` qui est lié à cet utilisateur si celui-ci est anonyme
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`time` | `int` | horodatage Unix du moment où l’événement s’est produit
`dispatch_id` | `null,` `string` | ID de l’envoi auquel appartient ce message
`send_id` | `null,` `string` | ID d'envoi de message auquel ce message appartient
`campaign_id` | `null,` `string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle appartient cet événement
`message_variation_api_id` | `null,` `string` | ID API de la variation de message que l’utilisateur a reçue
`canvas_id` | `null,` `string` | ID de la Braze à usage interne de la toile à laquelle cet événement appartient
`canvas_api_id` | `null,` `string` | ID API du Canvas auquel appartient cet événement
`canvas_variation_api_id` | `null,` `string` | ID API de la variation de Canvas à laquelle appartient cet événement
`canvas_step_api_id` | `null,` `string` | ID API de l'étape de Canvas auquel appartient cet événement
`canvas_step_message_variation_api_id` | `null,` `string` | ID API de la variation de message de l'étape de Canvas que l’utilisateur a reçue
`gender` | `null,` `string` | [Sexe de l'utilisateur
`country` | `null,` `string` | [Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [Langue de l'utilisateur
`to_phone_number` | `null,` `string` | Numéro de téléphone [PII] du destinataire
`subscription_group_api_id` | `null,` `string` | ID externe du groupe d’abonnement
`error` | `null,` `string` | nom de l’erreur
`provider_error_code` | `null,` `string` | code d'erreur du fournisseur de services SMS
`app_group_id` | `null,` `string` | BSON ID du groupe d'applications auquel appartient cet utilisateur
`is_sms_fallback` | `null, boolean` | Indique si une procédure de secours par SMS a été tentée pour ce message RCS rejeté. Il est lié/apparié à l'événement de réception/distribution de SMS
`sf_created_at` | `timestamp`, `null` | lorsque cet événement a été repris par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED {#USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `null,` `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail associé au numéro de téléphone entrant.
`time` | `int` | horodatage Unix du moment où l’événement s’est produit
`user_phone_number` | `string` | [PII] le numéro de téléphone de l'utilisateur à partir duquel le message a été reçu.
`subscription_group_id` | `null,` `string` | ID du groupe d’abonnement ciblé pour ce message SMS
`subscription_group_api_id` | `null,` `string` | ID de l’API du groupe d’abonnement ciblé pour ce message SMS
`inbound_phone_number` | `string` | Le numéro d'appel entrant auquel le message a été envoyé
`action` | `string` | Mesures prises en réponse à ce message. Par exemple, `Subscribed`, `Unsubscribed`, ou `None`.
`message_body` | `string` | Réponse de l'utilisateur
`media_urls` | `null, {"type"=>"array", "items"=>["null", "string"]}` | URL des médias de l'utilisateur
`campaign_id` | `null,` `string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle appartient cet événement
`message_variation_api_id` | `null,` `string` | ID API de la variation de message à laquelle appartient cet événement
`canvas_id` | `null,` `string` | ID de la Braze à usage interne de la toile à laquelle cet événement appartient
`canvas_api_id` | `null,` `string` | ID API du Canvas auquel appartient cet événement
`canvas_variation_api_id` | `null,` `string` | ID API de la variation de Canvas à laquelle appartient cet événement
`canvas_step_api_id` | `null,` `string` | ID API de l'étape de Canvas auquel appartient cet événement
`canvas_step_message_variation_api_id` | `null,` `string` | ID API de la variation du message d’étape Canvas auquel appartient cet événement
`app_group_id` | `null,` `string` | BSON ID du groupe d'applications auquel appartient cet utilisateur
`sf_created_at` | `timestamp`, `null` | lorsque cet événement a été repris par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_REJECTION_SHARED {#USERS_MESSAGES_SMS_REJECTION_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`device_id` | `null,` `string` | `device_id` qui est lié à cet utilisateur si celui-ci est anonyme
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`time` | `int` | horodatage Unix du moment où l’événement s’est produit
`dispatch_id` | `null,` `string` | ID de l’envoi auquel appartient ce message
`send_id` | `null,` `string` | ID d'envoi de message auquel ce message appartient
`campaign_id` | `null,` `string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle appartient cet événement
`message_variation_api_id` | `null,` `string` | ID API de la variation de message que l’utilisateur a reçue
`canvas_id` | `null,` `string` | ID de la Braze à usage interne de la toile à laquelle cet événement appartient
`canvas_api_id` | `null,` `string` | ID API du Canvas auquel appartient cet événement
`canvas_variation_api_id` | `null,` `string` | ID API de la variation de Canvas à laquelle appartient cet événement
`canvas_step_api_id` | `null,` `string` | ID API de l'étape de Canvas auquel appartient cet événement
`canvas_step_message_variation_api_id` | `null,` `string` | ID API de la variation de message de l'étape de Canvas que l’utilisateur a reçue
`gender` | `null,` `string` | [Sexe de l'utilisateur
`country` | `null,` `string` | [Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [Langue de l'utilisateur
`to_phone_number` | `null,` `string` | Numéro de téléphone [PII] du destinataire
`from_phone_number` | `null,` `string` | numéro de téléphone à partir duquel le message SMS a été envoyé
`subscription_group_api_id` | `null,` `string` | ID externe du groupe d’abonnement
`error` | `null,` `string` | nom de l’erreur
`provider_error_code` | `null,` `string` | code d'erreur du fournisseur de services SMS
`app_group_id` | `null,` `string` | BSON ID du groupe d'applications auquel appartient cet utilisateur
`is_sms_fallback` | `null, boolean` | Indique si une procédure de secours par SMS a été tentée pour ce message RCS rejeté. Il est lié/apparié à l'événement de réception/distribution de SMS
`sf_created_at` | `timestamp`, `null` | lorsque cet événement a été repris par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_SEND_SHARED {#USERS_MESSAGES_SMS_SEND_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`device_id` | `null,` `string` | `device_id` qui est lié à cet utilisateur si celui-ci est anonyme
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`time` | `int` | horodatage Unix du moment où l’événement s’est produit
`dispatch_id` | `null,` `string` | ID de l’envoi auquel appartient ce message
`send_id` | `null,` `string` | ID d'envoi de message auquel ce message appartient
`campaign_id` | `null,` `string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle appartient cet événement
`message_variation_api_id` | `null,` `string` | ID API de la variation de message que l’utilisateur a reçue
`canvas_id` | `null,` `string` | ID de la Braze à usage interne de la toile à laquelle cet événement appartient
`canvas_api_id` | `null,` `string` | ID API du Canvas auquel appartient cet événement
`canvas_variation_api_id` | `null,` `string` | ID API de la variation de Canvas à laquelle appartient cet événement
`canvas_step_api_id` | `null,` `string` | ID API de l'étape de Canvas auquel appartient cet événement
`canvas_step_message_variation_api_id` | `null,` `string` | ID API de la variation de message de l'étape de Canvas que l’utilisateur a reçue
`gender` | `null,` `string` | [Sexe de l'utilisateur
`country` | `null,` `string` | [Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [Langue de l'utilisateur
`to_phone_number` | `null,` `string` | Numéro de téléphone [PII] du destinataire
`subscription_group_api_id` | `null,` `string` | ID externe du groupe d’abonnement
`category` | `null,` `string` | Nom de catégorie de mot-clé, uniquement renseigné pour les messages de réponse automatique : ’Abonné’, ’Désabonné’, ’Aide’ ou valeur personnalisée
`app_group_id` | `null,` `string` | BSON ID du groupe d'applications auquel appartient cet utilisateur
`message_extras` | `null,` `string` | [Une chaîne JSON des paires clé-valeur balisées lors du rendu liquide.
`sf_created_at` | `timestamp`, `null` | lorsque cet événement a été repris par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED {#USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `null,` `string` | Braze ID de l'utilisateur ciblé par short_url, null si short_url n'a pas utilisé le suivi des clics de l'utilisateur
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur ciblé par short_url s'il existe, nul si short_url n'a pas utilisé le ciblage des clics de l'utilisateur.
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail utilisé pour la génération de short_url
`time` | `int` | Horodatage Unix du moment où la short_url a été cliqué
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`campaign_id` | `null,` `string` | Braze ID de la campagne pour laquelle short_url a été généré, null s'il ne s'agit pas d'une campagne
`campaign_api_id` | `null,` `string` | ID API de la campagne pour laquelle la short_url a été générée, nul si elle ne provient pas d’une campagne
`message_variation_api_id` | `null,` `string` | ID API de la variation de message pour laquelle la short_url a été générée, nul si elle ne provient pas d’une campagne
`canvas_id` | `null,` `string` | Braze ID du Canvas pour lequel short_url a été généré, null s'il ne provient pas d'un Canvas
`canvas_api_id` | `null,` `string` | API ID du Canvas pour lequel short_url a été généré, null s'il ne s'agit pas d'un Canvas
`canvas_variation_api_id` | `null,` `string` | API ID de la variation du canvas pour lequel short_url a été généré, null s'il ne s'agit pas d'un canvas.
`canvas_step_api_id` | `null,` `string` | API ID de l'étape du canvas pour lequel short_url a été généré, null s'il ne s'agit pas d'un canvas.
`canvas_step_message_variation_api_id` | `null,` `string` | API ID de l'étape du canvas pour lequel le message de variation short_url a été généré, null s'il ne s'agit pas d'un canvas.
`url` | `string` | URL originale contenue dans le message vers laquelle redirige la short_url
`short_url` | `string` | URL raccourcie qui a été cliquée
`user_agent` | `null,` `string` | agent utilisateur demandant short_url
`user_phone_number` | `string` | [PII] le numéro de téléphone de l'utilisateur
`device_id` | `null,` `string` | ID de l’appareil sur lequel l’événement s’est produit
`app_group_id` | `null,` `string` | BSON ID du groupe d'applications auquel appartient cet utilisateur
`is_suspected_bot_click` | `null, boolean` | Si cet événement a été traité comme un événement bot
`suspected_bot_click_reason` | `null, object` | Pourquoi cet événement a été classé comme bot
`sf_created_at` | `timestamp`, `null` | lorsque cet événement a été repris par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WEBHOOK_ABORT_SHARED {#USERS_MESSAGES_WEBHOOK_ABORT_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`device_id` | `null,` `string` | `device_id` qui est lié à cet utilisateur si celui-ci est anonyme
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`time` | `int` | horodatage Unix du moment où l’événement s’est produit
`dispatch_id` | `null,` `string` | ID de l’envoi auquel appartient ce message
`send_id` | `null,` `string` | ID d'envoi de message auquel ce message appartient
`campaign_id` | `null,` `string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle appartient cet événement
`message_variation_api_id` | `null,` `string` | ID API de la variation de message que l’utilisateur a reçue
`canvas_id` | `null,` `string` | ID de la Braze à usage interne de la toile à laquelle cet événement appartient
`canvas_api_id` | `null,` `string` | ID API du Canvas auquel appartient cet événement
`canvas_variation_api_id` | `null,` `string` | ID API de la variation de Canvas à laquelle appartient cet événement
`canvas_step_api_id` | `null,` `string` | ID API de l'étape de Canvas auquel appartient cet événement
`canvas_step_message_variation_api_id` | `null,` `string` | ID API de la variation de message de l'étape de Canvas que l’utilisateur a reçue
`gender` | `null,` `string` | [Sexe de l'utilisateur
`country` | `null,` `string` | [Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [Langue de l'utilisateur
`abort_type` | `null,` `string` | Type d'abandon, l'un des suivants ['liquid_abort_message', 'quiet_hours', 'rate_limit']
`abort_log` | `null,` `string` | [PII] Message du journal décrivant les détails de l'abandon (maximum de 2 000 caractères)
`app_group_id` | `null,` `string` | BSON ID du groupe d'applications auquel appartient cet utilisateur
`sf_created_at` | `timestamp`, `null` | lorsque cet événement a été repris par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_WEBHOOK_FAILURE_SHARED {#USERS_MESSAGES_WEBHOOK_FAILURE_SHARED}

Champ | Type | Description
------|------|------------
`http_status_code` | `null, int` | Code d'état HTTP de la réponse
`endpoint_url` | `null,` `string` | L'url de l'endpoint demandé
`app_group_api_id` | `null,` `string` | ID API du groupe d'applications auquel appartient cet utilisateur
`app_group_id` | `null,` `string` | BSON ID du groupe d'applications auquel appartient cet utilisateur
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle appartient cet événement
`campaign_id` | `null,` `string` | BSON ID de la campagne à laquelle cet événement appartient
`canvas_api_id` | `null,` `string` | ID API du Canvas auquel appartient cet événement
`canvas_id` | `null,` `string` | BSON ID de la toile à laquelle cet événement appartient
`canvas_step_api_id` | `null,` `string` | ID API de l'étape de Canvas auquel appartient cet événement
`canvas_step_message_variation_api_id` | `null,` `string` | ID API de la variation de message de l'étape de Canvas que l’utilisateur a reçue
`canvas_variation_api_id` | `null,` `string` | ID API de la variation de Canvas à laquelle appartient cet événement
`content_length` | `null, int` | Longueur du contenu de la réponse
`dispatch_id` | `null,` `string` | ID de l’envoi auquel appartient ce message
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`host` | `null,` `string` | L'hôte de la demande
`id` | `string` | ID unique au niveau mondial pour cet événement
`message_variation_api_id` | `null,` `string` | ID API de la variation de message que l’utilisateur a reçue
`raw_response` | `null,` `string` | Réponse brute tronquée de l'endpoint
`retry_count` | `null, int` | Nombre de tentatives d'essai
`send_id` | `null,` `string` | ID d'envoi de message auquel ce message appartient
`time` | `int` | Horodatage UNIX auquel l'événement s'est produit
`url_path` | `null,` `string` | Le chemin de l'url demandée
`user_id` | `string` | ID de l'utilisateur de Braze qui a effectué cet événement
`webhook_duration` | `null, int` | Durée totale de cette demande en millisecondes
`webhook_failure_source` | `null,` `string` | Pour savoir si une erreur a été créée par Braze ou par l'endpoint lui-même. Le champ source pourrait être External Endpoint, Treat no status code to host unreachable.
`is_terminal` | `null, boolean` | Que cet événement ait été la dernière tentative d'envoi d'un message, ou non.
`sf_created_at` | `timestamp`, `null` | lorsque cet événement a été repris par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WEBHOOK_SEND_SHARED {#USERS_MESSAGES_WEBHOOK_SEND_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`device_id` | `null,` `string` | `device_id` qui est lié à cet utilisateur si celui-ci est anonyme
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`time` | `int` | horodatage Unix du moment où l’événement s’est produit
`dispatch_id` | `null,` `string` | ID de l’envoi auquel appartient ce message
`send_id` | `null,` `string` | ID d'envoi de message auquel ce message appartient
`campaign_id` | `null,` `string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle appartient cet événement
`message_variation_api_id` | `null,` `string` | ID API de la variation de message que l’utilisateur a reçue
`canvas_id` | `null,` `string` | ID de la Braze à usage interne de la toile à laquelle cet événement appartient
`canvas_api_id` | `null,` `string` | ID API du Canvas auquel appartient cet événement
`canvas_variation_api_id` | `null,` `string` | ID API de la variation de Canvas à laquelle appartient cet événement
`canvas_step_api_id` | `null,` `string` | ID API de l'étape de Canvas auquel appartient cet événement
`canvas_step_message_variation_api_id` | `null,` `string` | ID API de la variation de message de l'étape de Canvas que l’utilisateur a reçue
`gender` | `null,` `string` | [Sexe de l'utilisateur
`country` | `null,` `string` | [Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [Langue de l'utilisateur
`app_group_id` | `null,` `string` | BSON ID du groupe d'applications auquel appartient cet utilisateur
`message_extras` | `null,` `string` | [Une chaîne JSON des paires clé-valeur balisées lors du rendu liquide.
`sf_created_at` | `timestamp`, `null` | lorsque cet événement a été repris par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WHATSAPP_ABORT_SHARED {#USERS_MESSAGES_WHATSAPP_ABORT_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`time` | `int` | horodatage Unix du moment où l’événement s’est produit
`to_phone_number` | 	`null,` `string` | Numéro de téléphone [PII] du destinataire
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`device_id` | `null,` `string` | `device_id` qui est lié à cet utilisateur si celui-ci est anonyme
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`app_group_id` | `null,` `string` | ID de l'espace de travail auquel appartient cet utilisateur
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`subscription_group_api_id` | `string` | ID d’API du groupe d'abonnement
`campaign_id` | `null,` `string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle appartient cet événement
`message_variation_api_id` | `null,` `string` | ID API de la variation de message que l’utilisateur a reçue
`canvas_id` | `null,` `string` | ID de la Braze à usage interne de la toile à laquelle cet événement appartient
`canvas_api_id` | `null,` `string` | ID API du Canvas auquel appartient cet événement
`canvas_variation_api_id` | `null,` `string` | ID API de la variation de Canvas à laquelle appartient cet événement
`canvas_step_api_id` | `null,` `string` | ID API de l'étape de Canvas auquel appartient cet événement
`canvas_step_message_variation_api_id` | `null,` `string` | ID API de la variation de message de l'étape de Canvas que l’utilisateur a reçue
`dispatch_id` | `null,` `string` | ID de l’envoi auquel appartient ce message
`abort_type` | `null,` `string` | Type d'abandon, l'un des suivants ['liquid_abort_message', 'quiet_hours', 'rate_limit']
`abort_log` | `null,` `string` | [PII] Message du journal décrivant les détails de l'abandon (maximum de 2 000 caractères)
`sf_created_at` | `timestamp`, `null` | Lorsque cet événement a été repris par le Snowpipe      
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_WHATSAPP_CLICK_SHARED {#USERS_MESSAGES_WHATSAPP_CLICK_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID de l'utilisateur de Braze qui a effectué cet événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`device_id` | `null,` `string` | ID de l’appareil sur lequel l’événement s’est produit
`app_group_id` | `null,` `string` | BSON ID du groupe d'applications auquel appartient cet utilisateur
`app_group_api_id` | `null,` `string` | ID API du groupe d'applications auquel appartient cet utilisateur
`time` | `int` | Horodatage UNIX auquel l'événement s'est produit
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`campaign_id` | `null,` `string` | BSON ID de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle appartient cet événement
`message_variation_api_id` | `null,` `string` | ID API de la variation de message que l’utilisateur a reçue
`canvas_id` | `null,` `string` | BSON ID de la toile à laquelle cet événement appartient
`canvas_api_id` | `null,` `string` | ID API du Canvas auquel appartient cet événement
`canvas_variation_api_id` | `null,` `string` | ID API de la variation de Canvas à laquelle appartient cet événement
`canvas_step_api_id` | `null,` `string` | ID API de l'étape de Canvas auquel appartient cet événement
`canvas_step_message_variation_api_id` | `null,` `string` | ID API de la variation de message de l'étape de Canvas que l’utilisateur a reçue
`url` | `null,` `string` | URL sur laquelle l’utilisateur a cliqué
`short_url` | `null,` `string` | URL raccourcie qui a été cliquée
`user_agent` | `null,` `string` | Agent utilisateur sur lequel le signalement du courrier indésirable a eu lieu
`user_phone_number` | `null,` `string` | [Le numéro de téléphone de l'utilisateur à partir duquel le message a été reçu.
`sf_created_at` | `timestamp`, `null` | lorsque cet événement a été repris par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WHATSAPP_DELIVERY_SHARED {#USERS_MESSAGES_WHATSAPP_DELIVERY_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`time` | `int` | horodatage Unix du moment où l’événement s’est produit
`to_phone_number` | `null,` `string` | Numéro de téléphone [PII] du destinataire
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`device_id` | `null,` `string` | `device_id` qui est lié à cet utilisateur si celui-ci est anonyme
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`from_phone_number` | `null,` `string` | Numéro de téléphone à partir duquel le message WhatsApp a été envoyé.
`app_group_id` | `null,` `string` | ID de l'espace de travail auquel appartient cet utilisateur
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`subscription_group_api_id` | `string` | ID d’API du groupe d'abonnement
`campaign_id` | `null,` `string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle appartient cet événement
`message_variation_api_id` | `null,` `string` | ID API de la variation de message que l’utilisateur a reçue
`canvas_id` | `null,` `string` | ID de la Braze à usage interne de la toile à laquelle cet événement appartient
`canvas_api_id` | `null,` `string` | ID API du Canvas auquel appartient cet événement
`canvas_variation_api_id` | `null,` `string` | ID API de la variation de Canvas à laquelle appartient cet événement
`canvas_step_api_id` | `null,` `string` | ID API de l'étape de Canvas auquel appartient cet événement
`canvas_step_message_variation_api_id` | `null,` `string` | ID API de la variation de message de l'étape de Canvas que l’utilisateur a reçue
`dispatch_id` | `null,` `string` | ID de l’envoi auquel appartient ce message
`sf_created_at` | `timestamp`, `null` | Lorsque cet événement a été repris par le Snowpipe      
`send_id` | `null,` `string` | ID d'envoi de message auquel ce message appartient
`flow_id` | `null,` `string` | L'ID unique du flux dans le gestionnaire WhatsApp. Présente si l'utilisateur répond à un flux WhatsApp.
`template_name` | `null,` `string` | [Nom du modèle dans le gestionnaire WhatsApp. Présente en cas d'envoi d'un message de type "Template".
`message_id` | `null,` `string` | L'ID unique généré par Meta pour ce message.
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WHATSAPP_FAILURE_SHARED {#USERS_MESSAGES_WHATSAPP_FAILURE_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`time` | `int` | horodatage Unix du moment où l’événement s’est produit
`to_phone_number` | `null,` `string` | Numéro de téléphone [PII] du destinataire
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`device_id` | `null,` `string` | `device_id` qui est lié à cet utilisateur si celui-ci est anonyme
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`from_phone_number` | `null,` `string` | Numéro de téléphone à partir duquel le message WhatsApp a été envoyé.
`app_group_id` | `null,` `string` | ID de l'espace de travail auquel appartient cet utilisateur
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`subscription_group_api_id` | `string` | ID d’API du groupe d'abonnement
`campaign_id` | `null,` `string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle appartient cet événement
`message_variation_api_id` | `null,` `string` | ID API de la variation de message que l’utilisateur a reçue
`canvas_id` | `null,` `string` | ID de la Braze à usage interne de la toile à laquelle cet événement appartient
`canvas_api_id` | `null,` `string` | ID API du Canvas auquel appartient cet événement
`canvas_variation_api_id` | `null,` `string` | ID API de la variation de Canvas à laquelle appartient cet événement
`canvas_step_api_id` | `null,` `string` | ID API de l'étape de Canvas auquel appartient cet événement
`canvas_step_message_variation_api_id` | `null,` `string` | ID API de la variation de message de l'étape de Canvas que l’utilisateur a reçue
`dispatch_id` | `null,` `string` | ID de l’envoi auquel appartient ce message
`provider_error_code` | `null,` `string` | Code d'erreur de WhatsApp
`provider_error_title` | `null, ` `string` | Titre d'erreur de WhatsApp
`sf_created_at` | `timestamp`, `null` | Lorsque cet événement a été repris par le Snowpipe      
`send_id` | `null,` `string` | ID d'envoi de message auquel ce message appartient
`message_id` | `null,` `string` | L'ID unique généré par Meta pour ce message.
`template_name` | `null,` `string` | [Nom du modèle dans le gestionnaire WhatsApp. Présente en cas d'envoi d'un message de type "Template".
`flow_id` | `null,` `string` | L'ID unique du flux dans le gestionnaire WhatsApp. Présente si l'utilisateur répond à un flux WhatsApp.
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WHATSAPP_INBOUNDRECEIVE_SHARED {#USERS_MESSAGES_WHATSAPP_INBOUNDRECEIVE_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`time` | `int` | horodatage Unix du moment où l’événement s’est produit
`user_phone_number` | `string` | [PII] le numéro de téléphone de l'utilisateur à partir duquel le message a été reçu
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`inbound_phone_number` | `string` | Le numéro d'appel entrant auquel le message a été envoyé
`device_id` | `null,` `string` | `device_id` qui est lié à cet utilisateur si celui-ci est anonyme
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`app_group_id` | `null,` `string` | ID de l'espace de travail auquel appartient cet utilisateur
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`subscription_group_api_id` | `string` | ID d’API du groupe d'abonnement
`campaign_id` | `null,` `string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle appartient cet événement
`message_variation_api_id` | `null,` `string` | ID API de la variation de message que l’utilisateur a reçue
`canvas_id` | `null,` `string` | ID de la Braze à usage interne de la toile à laquelle cet événement appartient
`canvas_api_id` | `null,` `string` | ID API du Canvas auquel appartient cet événement
`canvas_variation_api_id` | `null,` `string` | ID API de la variation de Canvas à laquelle appartient cet événement
`canvas_step_api_id` | `null,` `string` | ID API de l'étape de Canvas auquel appartient cet événement
`canvas_step_message_variation_api_id` | `null,` `string` | ID API de la variation de message de l'étape de Canvas que l’utilisateur a reçue
`message_body` | `string` | Réponse de l'utilisateur
`quick_reply_text` | `string` | Texte du bouton pressé par l'utilisateur
`media_urls` | `null, {"type"=>"array", "items"=>["null", "string"]}` | URL des médias de l'utilisateur
`action` | `string` | Mesures prises en réponse à ce message. Par exemple, `Subscribed`, `Unsubscribed`, ou `None`.
`sf_created_at` | `timestamp`, `null` | Lorsque cet événement a été repris par le Snowpipe      
`catalog_id` | `null,` `string` | ID de catalogue d'un produit si un produit est référencé dans le message entrant. Sinon, il est vide.
`product_id` | `null,` `string` | identifiant du produit acheté
`flow_id` | `null,` `string` | L'ID unique du flux dans le gestionnaire WhatsApp. Présente si l'utilisateur répond à un flux WhatsApp.
`flow_response_json` | `null,` `string` | [Les valeurs du formulaire auxquelles l'utilisateur a répondu. Présente si l'utilisateur répond à un flux WhatsApp.
`message_id` | `null,` `string` | L'ID unique généré par Meta pour ce message.
`in_reply_to` | `null,` `string` | Le site message_id de l'envoi de messages auquel ce message répondait
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WHATSAPP_READ_SHARED {#USERS_MESSAGES_WHATSAPP_READ_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`time` | `int` | horodatage Unix du moment où l’événement s’est produit
`to_phone_number` | `null,` `string` | Numéro de téléphone [PII] du destinataire
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`device_id` | `null,` `string` | `device_id` qui est lié à cet utilisateur si celui-ci est anonyme
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`from_phone_number` | `null,` `string` | Numéro de téléphone à partir duquel le message WhatsApp a été envoyé.
`app_group_id` | `null,` `string` | ID de l'espace de travail auquel appartient cet utilisateur
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`subscription_group_api_id` | `string` | ID d’API du groupe d'abonnement
`campaign_id` | `null,` `string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle appartient cet événement
`message_variation_api_id` | `null,` `string` | ID API de la variation de message que l’utilisateur a reçue
`canvas_id` | `null,` `string` | ID de la Braze à usage interne de la toile à laquelle cet événement appartient
`canvas_api_id` | `null,` `string` | ID API du Canvas auquel appartient cet événement
`canvas_variation_api_id` | `null,` `string` | ID API de la variation de Canvas à laquelle appartient cet événement
`canvas_step_api_id` | `null,` `string` | ID API de l'étape de Canvas auquel appartient cet événement
`canvas_step_message_variation_api_id` | `null,` `string` | ID API de la variation de message de l'étape de Canvas que l’utilisateur a reçue
`dispatch_id` | `null,` `string` | ID de l’envoi auquel appartient ce message
`sf_created_at` | `timestamp`, `null` | Lorsque cet événement a été repris par le Snowpipe      
`send_id` | `null,` `string` | ID d'envoi de message auquel ce message appartient
`template_name` | `null,` `string` | [Nom du modèle dans le gestionnaire WhatsApp. Présente en cas d'envoi d'un message de type "Template".
`message_id` | `null,` `string` | L'ID unique généré par Meta pour ce message.
`flow_id` | `null,` `string` | L'ID unique du flux dans le gestionnaire WhatsApp. Présente si l'utilisateur répond à un flux WhatsApp.
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WHATSAPP_SEND_SHARED {#USERS_MESSAGES_WHATSAPP_SEND_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`time` | `int` | horodatage Unix du moment où l’événement s’est produit
`to_phone_number` | `null,` `string`	| Numéro de téléphone [PII] du destinataire
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`device_id` | `null,` `string` | `device_id` qui est lié à cet utilisateur si celui-ci est anonyme
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`from_phone_number` | `null,` `string` | le numéro de téléphone à partir duquel le message WhatsApp a été envoyé
`app_group_id` | `null,` `string` | ID de l'espace de travail auquel appartient cet utilisateur
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`subscription_group_api_id` | `string` | ID d’API du groupe d'abonnement
`campaign_id` | `null,` `string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle appartient cet événement
`message_variation_api_id` | `null,` `string` | ID API de la variation de message que l’utilisateur a reçue
`canvas_id` | `null,` `string` | ID de la Braze à usage interne de la toile à laquelle cet événement appartient
`canvas_api_id` | `null,` `string` | ID API du Canvas auquel appartient cet événement
`canvas_variation_api_id` | `null,` `string` | ID API de la variation de Canvas à laquelle appartient cet événement
`canvas_step_api_id` | `null,` `string` | ID API de l'étape de Canvas auquel appartient cet événement
`canvas_step_message_variation_api_id` | `null,` `string` | ID API de la variation de message de l'étape de Canvas que l’utilisateur a reçue
`dispatch_id` | `null,` `string` | ID de l’envoi auquel appartient ce message
`message_extras` | `null,` `string` | [Une chaîne JSON des paires clé-valeur balisées lors du rendu de Liquid.
`sf_created_at` | `timestamp`, `null` | Lorsque cet événement a été repris par le Snowpipe      
`send_id` | `null,` `string` | ID d'envoi de message auquel ce message appartient
`flow_id` | `null,` `string` | L'ID unique du flux dans le gestionnaire WhatsApp. Présente si l'utilisateur répond à un flux WhatsApp.
`template_name` | `null,` `string` | [Nom du modèle dans le gestionnaire WhatsApp. Présente en cas d'envoi d'un message de type "Template".
`message_id` | `null,` `string` | L'ID unique généré par Meta pour ce message.
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Utilisateurs

### USERS_RANDOMBUCKETNUMBERUPDATE_SHARED {#USERS_RANDOMBUCKETNUMBERUPDATE_SHARED}

| Champ                       | Type                     | Description                                        |
| --------------------------- | ------------------------ | -------------------------------------------------- |
| `id`                        | `string`, `null`    | ID unique au niveau mondial pour cet événement                  |
| `app_group_id`              | `string`, `null`    | ID Braze de l'espace de travail auquel cet utilisateur appartient      |
| `app_group_api_id`          | `string`, `null`    | ID API de l'espace de travail auquel appartient cet utilisateur       |
| `user_id`                   | `string`, `null`    | ID Braze de l'utilisateur qui a réalisé cet événement      |
| `external_user_id`          | `string`, `null`    | [PII] ID externe de l'utilisateur                 |
| `time`                      | `int`, `null`       | horodatage Unix du moment où l’événement s’est produit         |
| `random_bucket_number`      | `int`, `null`       | Numéro de compartiment aléatoire actuel attribué à l'utilisateur  |
| `prev_random_bucket_number` | `int`, `null`       | Numéro de compartiment aléatoire précédent attribué à l'utilisateur |
| `sf_created_at`             | `timestamp`, `null` | Lorsque cet événement a été repris par le Snowpipe      |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_USERDELETEREQUEST_SHARED {#USERS_USERDELETEREQUEST_SHARED}

| Champ              | Type                     | Description                                                   |
| ------------------ | ------------------------ | ------------------------------------------------------------- |
| `id`               | `string`, `null`    | ID unique au niveau mondial pour cet événement                             |
| `user_id`          | `string`, `null`    | ID Braze de l'utilisateur qui a été supprimé                          |
| `app_group_id`     | `string`, `null`    | ID Braze de l'espace de travail auquel cet utilisateur appartient                 |
| `app_group_api_id` | `string`, `null`    | ID API de l'espace de travail auquel appartient cet utilisateur                  |
| `time`             | `int`, `null`       | Date Unix à laquelle la demande de suppression de l'utilisateur a été traitée |
| `sf_created_at`    | `timestamp`, `null` | Lorsque cet événement a été repris par le Snowpipe                 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_USERORPHAN_SHARED {#USERS_USERORPHAN_SHARED}

| Champ              | Type                     | Description                                                                   |
| ------------------ | ------------------------ | ----------------------------------------------------------------------------- |
| `id`               | `string`, `null`    | ID unique au niveau mondial pour cet événement                                             |
| `user_id`          | `string`, `null`    | ID Braze de l'utilisateur devenu orphelin                                         |
| `external_user_id` | `string`, `null`    | [PII] ID externe de l'utilisateur                                            |
| `device_id`        | `string`, `null`    | ID de l'appareil lié à cet utilisateur, si l'utilisateur est anonyme          |
| `app_group_id`     | `string`, `null`    | ID Braze de l'espace de travail auquel cet utilisateur appartient                                 |
| `app_group_api_id` | `string`, `null`    | ID API de l'espace de travail auquel appartient cet utilisateur                                  |
| `app_api_id`       | `string`, `null`    | ID API de l'application à laquelle appartenait l'utilisateur orphelin.                               |
| `time`             | `int`, `null`       | Date Unix à laquelle l'utilisateur est devenu orphelin                                 |
| `orphaned_by_id`   | `string`, `null`    | ID Braze de l'utilisateur dont le profil a été fusionné avec le profil de l'utilisateur orphelin. |
| `sf_created_at`    | `timestamp`, `null` | Lorsque cet événement a été repris par le Snowpipe                                 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }
