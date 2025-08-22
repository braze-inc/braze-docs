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
[USERS_BEHAVIORS_SUBSCRIPTION_GLOBALSTATECHANGE_SHARED](#USERS_BEHAVIORS_SUBSCRIPTION_GLOBALSTATECHANGE_SHARED) | Lorsqu’un utilisateur est abonné ou désabonné globalement d’un canal tel que l’e-mail
[USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED](#USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED) | Lorsqu’un utilisateur est abonné ou désabonné d’un groupe d’abonnement
[USERS_CAMPAIGNS_CONVERSION_SHARED](#USERS_CAMPAIGNS_CONVERSION_SHARED) | Lorsqu’un utilisateur se convertit pour une campagne
[USERS_CAMPAIGNS_ENROLLINCONTROL_SHARED](#USERS_CAMPAIGNS_ENROLLINCONTROL_SHARED) | Lorsqu’un utilisateur est inscrit dans le groupe de contrôle d’une campagne
[USERS_CAMPAIGNS_FREQUENCYCAP_SHARED](#USERS_CAMPAIGNS_FREQUENCYCAP_SHARED) | Lorsqu’un utilisateur atteint une limite de fréquence pour une campagne
[USERS_CAMPAIGNS_REVENUE_SHARED](#USERS_CAMPAIGNS_REVENUE_SHARED) | Lorsqu'un utilisateur génère des chiffres d'affaires au cours de la période de conversion primaire.
[UTILISATEURS_CANVASSTEP_PROGRESSION_PARTAGÉE](#USERS_CANVASSTEP_PROGRESSION_SHARED) | Lorsqu'un utilisateur passe à une étape du canvas
[USERS_CANVAS_CONVERSION_SHARED](#USERS_CANVAS_CONVERSION_SHARED) | Lorsqu'un utilisateur effectue une conversion dans le cadre d'un événement de conversion Canvas
[USERS_CANVAS_ENTRY_SHARED](#USERS_CANVAS_ENTRY_SHARED) | Lorsqu'un utilisateur entre dans un Canvas
[USERS_CANVAS_EXIT_MATCHEDAUDIENCE_SHARED](#USERS_CANVAS_EXIT_MATCHEDAUDIENCE_SHARED) | Lorsqu'un utilisateur quitte un canvas parce qu'il correspond aux critères de sortie de l'audience
[USERS_CANVAS_EXIT_PERFORMEDEVENT_SHARED](#USERS_CANVAS_EXIT_PERFORMEDEVENT_SHARED) | Lorsqu'un utilisateur quitte un canvas parce qu'il a effectué un événement d'exception
[USERS_CANVAS_EXPERIMENTSTEP_CONVERSION_SHARED](#USERS_CANVAS_EXPERIMENTSTEP_CONVERSION_SHARED) | Lorsqu'un utilisateur se convertit pour une étape de l'expérience Canvas
[USERS_CANVAS_EXPERIMENTSTEP_SPLITENTRY_SHARED](#USERS_CANVAS_EXPERIMENTSTEP_SPLITENTRY_SHARED) | Lorsqu'un utilisateur entre dans une étape d’expérience
[USERS_CANVAS_FREQUENCYCAP_SHARED](#USERS_CANVAS_FREQUENCYCAP_SHARED) | Lorsqu'un utilisateur se voit imposer une limite de fréquence pour une étape du canvas
[USERS_CANVAS_REVENUE_SHARED](#USERS_CANVAS_REVENUE_SHARED) | Lorsqu'un utilisateur génère des chiffres d'affaires au cours de la période de l'événement de conversion principal.
[USERS_MESSAGES_CONTENTCARD_ABORT_SHARED](#USERS_MESSAGES_CONTENTCARD_ABORT_SHARED) | Un message de carte de contenu initialement planifié a été abandonné pour une raison quelconque.
[USERS_MESSAGES_CONTENTCARD_CLICK_SHARED](#USERS_MESSAGES_CONTENTCARD_CLICK_SHARED) | Lorsqu’un utilisateur clique sur une carte de contenu
[USERS_MESSAGES_CONTENTCARD_DISMISS_SHARED](#USERS_MESSAGES_CONTENTCARD_DISMISS_SHARED) | Lorsqu’un utilisateur rejette une carte de contenu
[USERS_MESSAGES_CONTENTCARD_IMPRESSION_SHARED](#USERS_MESSAGES_CONTENTCARD_IMPRESSION_SHARED) | Lorsqu’un utilisateur affiche une carte de contenu
[USERS_MESSAGES_CONTENTCARD_SEND_SHARED](#USERS_MESSAGES_CONTENTCARD_SEND_SHARED) | Lorsque nous envoyons une carte de contenu à un utilisateur
[USERS_MESSAGES_EMAIL_ABORT_SHARED](#USERS_MESSAGES_EMAIL_ABORT_SHARED) | Un e-mail initialement planifié a été abandonné pour une raison quelconque.
[USERS_MESSAGES_EMAIL_BOUNCE_SHARED](#USERS_MESSAGES_EMAIL_BOUNCE_SHARED) | Un fournisseur de services de courrier électronique a renvoyé un échec d'envoi définitif. Un échec d'envoi définitif est un échec permanent de la livrabilité.
[USERS_MESSAGES_EMAIL_CLICK_SHARED](#USERS_MESSAGES_EMAIL_CLICK_SHARED) | Lorsqu’un utilisateur a cliqué sur un lien dans un e-mail
[USERS_MESSAGES_EMAIL_DELIVERY_SHARED](#USERS_MESSAGES_EMAIL_DELIVERY_SHARED) | Lorsqu’un e-mail est livré
[USERS_MESSAGES_EMAIL_MARKASSPAM_SHARED](#USERS_MESSAGES_EMAIL_MARKASSPAM_SHARED) | Lorsqu’un un e-mail est désigné comme étant du spam
[USERS_MESSAGES_EMAIL_OPEN_SHARED](#USERS_MESSAGES_EMAIL_OPEN_SHARED) | Lorsqu’un utilisateur ouvre un e-mail
[USERS_MESSAGES_EMAIL_SEND_SHARED](#USERS_MESSAGES_EMAIL_SEND_SHARED) | Lorsque nous envoyons un e-mail à un utilisateur
[USERS_MESSAGES_EMAIL_SOFTBOUNCE_SHARED](#USERS_MESSAGES_EMAIL_SOFTBOUNCE_SHARED) | Lorsqu’un e-mail subit un rebond doux
[USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED](#USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED) | Lorsqu’un utilisateur se désabonne de l’e-mail
[USERS_MESSAGES_INAPPMESSAGE_ABORT_SHARED](#USERS_MESSAGES_INAPPMESSAGE_ABORT_SHARED) | Un message in-app initialement planifié a été abandonné pour une raison quelconque.
[USERS_MESSAGES_INAPPMESSAGE_CLICK_SHARED](#USERS_MESSAGES_INAPPMESSAGE_CLICK_SHARED) | Lorsqu’un utilisateur clique sur un message in-app
[USERS_MESSAGES_INAPPMESSAGE_IMPRESSION_SHARED](#USERS_MESSAGES_INAPPMESSAGE_IMPRESSION_SHARED) | Lorsqu’un utilisateur affiche un message in-app
[USERS_MESSAGES_NEWSFEEDCARD_ABORT_SHARED](#USERS_MESSAGES_NEWSFEEDCARD_ABORT_SHARED) | Un message de carte de fil d’actualité initialement planifié a été abandonné pour une raison quelconque.
[USERS_MESSAGES_NEWSFEEDCARD_CLICK_SHARED](#USERS_MESSAGES_NEWSFEEDCARD_CLICK_SHARED) | Lorsqu’un utilisateur clique sur une carte de fil d’actualité
[USERS_MESSAGES_NEWSFEEDCARD_IMPRESSION_SHARED](#USERS_MESSAGES_NEWSFEEDCARD_IMPRESSION_SHARED) | Lorsqu’un utilisateur affiche une carte de fil d’actualité
[UTILISATEURS_MESSAGES_PUSHNOTIFICATION_ABORT_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_ABORT_SHARED) | Un message de notification push initialement planifié a été abandonné pour une raison quelconque.
[UTILISATEURS_MESSAGES_PUSHNOTIFICATION_BOUNCE_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_BOUNCE_SHARED) | Lorsqu’une notifications push rebondit
[UTILISATEURS_MESSAGES_PUSHNOTIFICATION_INFLUENCEDOPEN_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_INFLUENCEDOPEN_SHARED) | Lorsqu’un utilisateur ouvre l’application après avoir reçu une notification sans cliquer sur elle
[USERS_MESSAGES_PUSHNOTIFICATION_IOSFOREGROUND_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_IOSFOREGROUND_SHARED) | Lorsqu’un utilisateur a reçu une notification push pendant que l’application était ouverte
[UTILISATEURS_MESSAGES_PUSHNOTIFICATION_OPEN_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_OPEN_SHARED) | Lorsqu'un utilisateur ouvre une notification push ou clique sur un bouton de notification push (y compris un bouton CLOSE qui n'ouvre PAS l'appli). <br><br> Les boutons d'action push ont des résultats multiples. Les actions « Non », « Refuser » et « Annuler » correspondent à des « clics », et les actions « Accepter » correspondent à des « ouvertures ». Tous ces cas sont représentés dans ce tableau, mais ils sont différenciés dans la colonne **BUTTON_ACTION_TYPE**. Par exemple, une requête peut être utilisée pour regrouper en fonction d'un `BUTTON_ACTION_TYPE` qui n'est ni Non, ni Refuser, ni Annuler.
[UTILISATEURS_MESSAGES_PUSHNOTIFICATION_SEND_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_SEND_SHARED) | Lorsque nous envoyons une notification push à un utilisateur
[UTILISATEURS_MESSAGES_SMS_ABORT_SHARED](#USERS_MESSAGES_SMS_ABORT_SHARED) | Un message SMS initialement planifié a été abandonné pour une raison quelconque.
[USERS_MESSAGES_SMS_CARRIERSEND_SHARED](#USERS_MESSAGES_SMS_CARRIERSEND_SHARED) | Lorsqu'un message SMS est envoyé à l'opérateur
[USERS_MESSAGES_SMS_DELIVERY_SHARED](#USERS_MESSAGES_SMS_DELIVERY_SHARED) | Lorsqu’un message SMS est livré
[USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED](#USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED) | Lorsque Braze n’est pas en mesure de livrer le message SMS au fournisseur de services SMS
[UTILISATEURS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED](#USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED) | Lorsqu’un message SMS est reçu d’un utilisateur
[USERS_MESSAGES_SMS_REJECTION_SHARED](#USERS_MESSAGES_SMS_REJECTION_SHARED) | Lorsqu’un message SMS n’est pas livré à un utilisateur
[UTILISATEURS_MESSAGES_SMS_SEND_SHARED](#USERS_MESSAGES_SMS_SEND_SHARED) | Lorsqu’un message SMS est envoyé
[UTILISATEURS_MESSAGES_SMS_SHORTLINKCLICK_SHARED](#USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED) | Lorsqu’un utilisateur clique sur une URL raccourcie Braze incluse dans un message SMS
[UTILISATEURS_MESSAGES_WEBHOOK_ABORT_SHARED](#USERS_MESSAGES_WEBHOOK_ABORT_SHARED) | Un message webhook initialement planifié a été interrompu pour une raison quelconque.
[UTILISATEURS_MESSAGES_WEBHOOK_SEND_SHARED](#USERS_MESSAGES_WEBHOOK_SEND_SHARED) | Lorsque nous envoyons un webhook pour un utilisateur
[UTILISATEURS_MESSAGES_WHATSAPP_ABORT_SHARED](#USERS_MESSAGES_WHATSAPP_ABORT_SHARED) | Un message WhatsApp initialement planifié a été annulé pour une raison quelconque.
[USERS_MESSAGES_WHATSAPP_DELIVERY_SHARED](#USERS_MESSAGES_WHATSAPP_DELIVERY_SHARED) |Lors de l'envoi d'un message WhatsApp
[UTILISATEURS_MESSAGES_WHATSAPP_FAILURE_SHARED](#USERS_MESSAGES_WHATSAPP_FAILURE_SHARED) | Lorsqu'un message WhatsApp n'est pas envoyé à un utilisateur
[UTILISATEURS_MESSAGES_WHATSAPP_INBOUNDRECEIVE_SHARED](#USERS_MESSAGES_WHATSAPP_INBOUNDRECEIVE_SHARED) | Lorsqu'un message WhatsApp est reçu d'un utilisateur
[UTILISATEURS_MESSAGES_WHATSAPP_READ_SHARED](#USERS_MESSAGES_WHATSAPP_READ_SHARED) | Lorsqu'un utilisateur ouvre un message WhatsApp
[UTILISATEURS_MESSAGES_WHATSAPP_SEND_SHARED](#USERS_MESSAGES_WHATSAPP_SEND_SHARED) | Lorsque nous envoyons un message WhatsApp pour un utilisateur
[USERS_RANDOMBUCKETNUMBERUPDATE_SHARED](#USERS_RANDOMBUCKETNUMBERUPDATE_SHARED) | Lorsque le numéro de compartiment aléatoire d'un utilisateur est modifié
[USERS_USERDELETEREQUEST_SHARED](#USERS_USERDELETEREQUEST_SHARED) | Lorsqu'un utilisateur est supprimé à la demande d'un client
[USERS_USERORPHAN_SHARED](#USERS_USERORPHAN_SHARED) | Lorsqu'un utilisateur est fusionné avec le profil d'un autre utilisateur et que le profil d'origine est orphelin


## Comportements

### USERS_BEHAVIORS_CUSTOMEVENT_SHARED {#USERS_BEHAVIORS_CUSTOMEVENT_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé l'événement
`external_user_id` | `null,` `string` | [Données d'identification] ID externe de l'utilisateur
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`app_api_id` | `null,` `string` | ID API de l’application sur laquelle cette action s’est produite
`time` | `int` | Horodatage Unix du moment où l’utilisateur a effectué l’événement
`gender` | `null,` `string` | [Données d'identification] Sexe de l'utilisateur
`country` | `null,` `string` | [PII] Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [PII] Langue de l'utilisateur
`device_id` | `null,` `string` | ID de l’appareil sur lequel l’événement personnalisé s’est produit
`sdk_version` | `null,` `string` | Version du SDK de Braze utilisée lors de l'événement
`platform` | `null,` `string` | Plate-forme de l'appareil
`os_version` | `null,` `string` | Version du système d'exploitation de l'appareil
`device_model` | `null,` `string` | Modèle de l'appareil
`name` | `string` | Nom de l'événement personnalisé
`properties` | `string` | Propriétés personnalisées de l'événement stockées sous la forme d'une chaîne de caractères codée en JSON.
`ad_id` | `null,` `string` | [PII] Identifiant publicitaire
`ad_id_type` | `null,` `string` | Un parmi `ios_idfa`, `google_ad_id`, `windows_ad_id` OU `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Si le suivi publicitaire est activé pour l’appareil ou non
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_INSTALLATTRIBUTION_SHARED {#USERS_BEHAVIORS_INSTALLATTRIBUTION_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a procédé à l'installation
`external_user_id` | `null,` `string` | [Données d'identification] ID externe de l'utilisateur
`device_id` | `null,` `string` | `device_id` qui est lié à cet utilisateur si celui-ci est anonyme
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`time` | `int` | Horodatage Unix du moment où l’utilisateur a installé
`source` | `string` | la source de l'attribution
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_LOCATION_SHARED {#USERS_BEHAVIORS_LOCATION_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui enregistre l'emplacement/localisation
`external_user_id` | `null,` `string` | [Données d'identification] ID externe de l'utilisateur
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`app_api_id` | `null,` `string` | ID API de l’application sur laquelle ce lieu a été enregistré
`time` | `int` | Date/heure Unix à laquelle la localisation a été enregistrée
`latitude` | `float` | [PII] Latitude de l'emplacement/localisation enregistré
`longitude` | `float` | [PII] Longitude de l'emplacement/localisation enregistré
`altitude` | `null, float` | [PII] altitude de l'emplacement/localisation enregistré
`ll_accuracy` | `null, float` | précision de la latitude et longitude du lieu enregistré
`alt_accuracy` | `null, float` | précision de l’altitude du lieu enregistré
`device_id` | `null,` `string` | ID de l’appareil sur lequel la localisation a été enregistrée
`sdk_version` | `null,` `string` | Version du SDK de Braze utilisée lors de l'enregistrement de l'emplacement/localisation.
`platform` | `null,` `string` | Plate-forme de l'appareil
`os_version` | `null,` `string` | Version du système d'exploitation de l'appareil
`device_model` | `null,` `string` | Modèle de l'appareil
`ad_id` | `null,` `string` | [PII] Identifiant publicitaire
`ad_id_type` | `null,` `string` | Un parmi `ios_idfa`, `google_ad_id`, `windows_ad_id` OU `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Si le suivi publicitaire est activé pour l’appareil ou non
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_PURCHASE_SHARED {#USERS_BEHAVIORS_PURCHASE_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a effectué un achat
`external_user_id` | `null,` `string` | [Données d'identification] ID externe de l'utilisateur
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
`ad_id` | `null,` `string` | [PII] Identifiant publicitaire
`ad_id_type` | `null,` `string` | Un parmi `ios_idfa`, `google_ad_id`, `windows_ad_id` OU `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Si le suivi publicitaire est activé pour l’appareil ou non
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_UNINSTALL_SHARED {#USERS_BEHAVIORS_UNINSTALL_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a procédé à la désinstallation
`external_user_id` | `null,` `string` | [Données d'identification] ID externe de l'utilisateur
`device_id` | `null,` `string` | `device_id` qui est lié à cet utilisateur si celui-ci est anonyme
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`app_api_id` | `null,` `string` | ID API de l’application qui a été désinstallée
`time` | `int` | Horodatage Unix du moment où l’utilisateur a désinstallé
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_UPGRADEDAPP_SHARED {#USERS_BEHAVIORS_UPGRADEDAPP_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a mis à jour l'application
`external_user_id` | `null,` `string` | [Données d'identification] ID externe de l'utilisateur
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
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_APP_FIRSTSESSION_SHARED {#USERS_BEHAVIORS_APP_FIRSTSESSION_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui effectue cette action
`external_user_id` | `null,` `string` | [Données d'identification] ID externe de l'utilisateur
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`app_api_id` | `null,` `string` | ID API de l’application sur laquelle cette session s’est produite
`time` | `int` | Horodatage Unix du moment où la session a commencé
`session_id` | `string` | UUID de la session
`gender` | `null,` `string` | [Données d'identification] Sexe de l'utilisateur
`country` | `null,` `string` | [PII] Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [PII] Langue de l'utilisateur
`device_id` | `null,` `string` | ID de l’appareil sur lequel la session s’est produite
`sdk_version` | `null,` `string` | Version du SDK de Braze utilisée pendant la session
`platform` | `null,` `string` | Plate-forme de l'appareil
`os_version` | `null,` `string` | Version du système d'exploitation de l'appareil
`device_model` | `null,` `string` | Modèle de l'appareil
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### UTILISATEURS_COMPORTEMENTS_APP_NEWSFEEDIMPRESSION_SHARED {#USERS_BEHAVIORS_APP_NEWSFEEDIMPRESSION_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a consulté le fil d'actualité.
`external_user_id` | `null,` `string` | [Données d'identification] ID externe de l'utilisateur
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`app_api_id` | `null,` `string` | ID API de l’application sur laquelle l’utilisateur a vu le fil d’actualité
`time` | `int` | Horodatage Unix du moment où l’utilisateur a vu le fil d’actualité
`device_id` | `null,` `string` | ID de l’appareil sur lequel l’impression s’est produite
`sdk_version` | `null,` `string` | Version du SDK de Braze utilisée lors de l'impression
`platform` | `null,` `string` | Plate-forme de l'appareil
`os_version` | `null,` `string` | Version du système d'exploitation de l'appareil
`device_model` | `null,` `string` | Modèle de l'appareil
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### UTILISATEURS_COMPORTEMENTS_APP_SESSIONEND_SHARED {#USERS_BEHAVIORS_APP_SESSIONEND_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui effectue cette action
`external_user_id` | `null,` `string` | [Données d'identification] ID externe de l'utilisateur
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`app_api_id` | `null,` `string` | ID API de l’application sur laquelle cette session s’est produite
`time` | `int` | Horodatage Unix du moment où la session s’est terminée
`duration` | `null, float` | Durée de la session
`session_id` | `string` | UUID de la session
`device_id` | `null,` `string` | ID de l’appareil sur lequel la session s’est produite
`sdk_version` | `null,` `string` | Version du SDK de Braze utilisée pendant la session
`platform` | `null,` `string` | Plate-forme de l'appareil
`os_version` | `null,` `string` | Version du système d'exploitation de l'appareil
`device_model` | `null,` `string` | Modèle de l'appareil
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### UTILISATEURS_COMPORTEMENTS_APP_SESSIONSTART_SHARED {#USERS_BEHAVIORS_APP_SESSIONSTART_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui effectue cette action
`external_user_id` | `null,` `string` | [Données d'identification] ID externe de l'utilisateur
`app_api_id` | `null,` `string` | ID API de l’application sur laquelle cette session s’est produite
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`time` | `int` | Horodatage Unix du moment où la session a commencé
`session_id` | `string` | UUID de la session
`device_id` | `null,` `string` | ID de l’appareil sur lequel la session s’est produite
`sdk_version` | `null,` `string` | Version du SDK de Braze utilisée pendant la session
`platform` | `null,` `string` | Plate-forme de l'appareil
`os_version` | `null,` `string` | Version du système d'exploitation de l'appareil
`device_model` | `null,` `string` | Modèle de l'appareil
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### UTILISATEURS_COMPORTEMENTS_GEOFENCE_DATAEVENT_SHARED {#USERS_BEHAVIORS_GEOFENCE_DATAEVENT_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé l'événement
`external_user_id` | `null,` `string` | [Données d'identification] ID externe de l'utilisateur
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
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_GEOFENCE_RECORDEVENT_SHARED {#USERS_BEHAVIORS_GEOFENCE_RECORDEVENT_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé l'événement
`external_user_id` | `null,` `string` | [Données d'identification] ID externe de l'utilisateur
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
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_SUBSCRIPTION_GLOBALSTATECHANGE_SHARED {#USERS_BEHAVIORS_SUBSCRIPTION_GLOBALSTATECHANGE_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur concerné
`external_user_id` | `null,` `string` | [Données d'identification] ID externe de l'utilisateur
`email_address` | `null,` `string` | [PII] adresse e-mail de l'utilisateur
`state_change_source` | `null,` `string` | source du changement d’état (REST, SDK, tableau de bord, etc.)
`subscription_status` | `string` | Statut de l'abonnement : 'Abonné' ou 'Désabonné'
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
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED {#USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur concerné
`external_user_id` | `null,` `string` | [Données d'identification] ID externe de l'utilisateur
`device_id` | `null,` `string` | `device_id` qui est lié à cet utilisateur si celui-ci est anonyme
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`email_address` | `null,` `string` | [PII] adresse e-mail de l'utilisateur
`phone_number` | `null,` `string` | [PII] numéro de téléphone de l'utilisateur au format e164
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
`subscription_status` | `string` | Statut de l'abonnement : 'Abonné' ou 'Désabonné'
`time` | `int` | Horodatage Unix du moment où l’état de l’abonnement a changé
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`send_id` | `null,` `string` | ID d’envoi du message à l’origine de cette action de changement d’état d’abonnement
`state_change_source` | `null,` `string` | Source du changement d'état (REST, SDK, tableau de bord, etc.)
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Campagnes

### USERS_CAMPAIGNS_CONVERSION_SHARED {#USERS_CAMPAIGNS_CONVERSION_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [Données d'identification] ID externe de l'utilisateur
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
`gender` | `null,` `string` | [Données d'identification] Sexe de l'utilisateur
`country` | `null,` `string` | [PII] Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [PII] Langue de l'utilisateur
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CAMPAIGNS_ENROLLINCONTROL_SHARED {#USERS_CAMPAIGNS_ENROLLINCONTROL_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [Données d'identification] ID externe de l'utilisateur
`device_id` | `null,` `string` | `device_id` qui est lié à cet utilisateur si celui-ci est anonyme
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`time` | `int` | horodatage Unix du moment où l’événement s’est produit
`app_api_id` | `null,` `string` | ID API de l’application sur laquelle cet événement s’est produit
`dispatch_id` | `null,` `string` | ID de l’envoi auquel appartient ce message
`send_id` | `null,` `string` | ID d'envoi de message auquel ce message appartient
`campaign_id` | `string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle appartient cet événement
`message_variation_api_id` | `null,` `string` | ID API de la variation de message que l’utilisateur a reçue
`gender` | `null,` `string` | [Données d'identification] Sexe de l'utilisateur
`country` | `null,` `string` | [PII] Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [PII] Langue de l'utilisateur
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CAMPAIGNS_FREQUENCYCAP_SHARED {#USERS_CAMPAIGNS_FREQUENCYCAP_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [Données d'identification] ID externe de l'utilisateur
`device_id` | `null,` `string` | `device_id` qui est lié à cet utilisateur si celui-ci est anonyme
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`time` | `int` | horodatage Unix du moment où l’événement s’est produit
`dispatch_id` | `null,` `string` | ID de l’envoi auquel appartient ce message
`send_id` | `null,` `string` | ID d'envoi de message auquel ce message appartient
`campaign_id` | `string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle appartient cet événement
`message_variation_api_id` | `null,` `string` | ID API de la variation de message que l’utilisateur a reçue
`channel` | `null,` `string` | Canal auquel appartient cet événement
`gender` | `null,` `string` | [Données d'identification] Sexe de l'utilisateur
`country` | `null,` `string` | [PII] Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [PII] Langue de l'utilisateur
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CAMPAIGNS_REVENUE_SHARED {#USERS_CAMPAIGNS_REVENUE_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [Données d'identification] ID externe de l'utilisateur
`device_id` | `null,` `string` | `device_id` qui est lié à cet utilisateur si celui-ci est anonyme
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`time` | `int` | horodatage Unix du moment où l’événement s’est produit
`app_api_id` | `null,` `string` | ID API de l’application sur laquelle cet événement s’est produit
`dispatch_id` | `null,` `string` | ID de l’envoi auquel appartient ce message
`send_id` | `null,` `string` | ID d'envoi de message auquel ce message appartient
`campaign_id` | `string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle appartient cet événement
`message_variation_api_id` | `null,` `string` | ID API de la variation de message que l’utilisateur a reçue
`gender` | `null,` `string` | [Données d'identification] Sexe de l'utilisateur
`country` | `null,` `string` | [PII] Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [PII] Langue de l'utilisateur
`revenue` | `long` | Le chiffre d'affaires d'USD en cents généré
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Canvas

### UTILISATEURS_CANVASSTEP_PROGRESSION_PARTAGÉE {#USERS_CANVASSTEP_PROGRESSION_SHARED}

| Champ                                  | Type                     | Description                                                                                                     |
| -------------------------------------- | ------------------------ | --------------------------------------------------------------------------------------------------------------- |
| `id`                                   | `string`, `null`    | ID unique au niveau mondial pour cet événement                                                                               |
| `user_id`                              | `string`, `null`    | ID Braze de l'utilisateur qui a réalisé cet événement                                                                   |
| `external_user_id`                     | `string`, `null`    | [Données d'identification] ID externe de l'utilisateur                                                                              |
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
| `external_user_id`                     | `string`, `null`    | [Données d'identification] ID externe de l'utilisateur                                                                              |
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
| `gender`                               | `string`, `null`    | [Données d'identification] Sexe de l'utilisateur                                                                                        |
| `country`                              | `string`, `null`    | [PII] Pays de l'utilisateur                                                                                       |
| `timezone`                             | `string`, `null`    | Fuseau horaire de l'utilisateur                                                                                            |
| `language`                             | `string`, `null`    | [PII] Langue de l'utilisateur                                                                                      |
| `sf_created_at`                        | `timestamp`, `null` | Lorsque cet événement a été repris par le Snowpipe                                                                   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### UTILISATEURS_CANVAS_ENTRY_SHARED {#USERS_CANVAS_ENTRY_SHARED}

| Champ                     | Type                     | Description                                                          |
| ------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                      | `string`, `null`    | ID unique au niveau mondial pour cet événement                                    |
| `user_id`                 | `string`, `null`    | ID Braze de l'utilisateur qui a réalisé cet événement                        |
| `external_user_id`        | `string`, `null`    | [Données d'identification] ID externe de l'utilisateur                                   |
| `device_id`               | `string`, `null`    | ID de l'appareil lié à cet utilisateur, si l'utilisateur est anonyme |
| `app_group_id`            | `string`, `null`    | ID Braze de l'espace de travail auquel cet utilisateur appartient                        |
| `app_group_api_id`        | `string`, `null`    | ID API de l'espace de travail auquel appartient cet utilisateur                         |
| `time`                    | `int`, `null`       | horodatage Unix du moment où l’événement s’est produit                           |
| `canvas_id`               | `string`, `null`    | (Réservé à l'usage de Braze) ID de la toile à laquelle appartient cet événement          |
| `canvas_api_id`           | `string`, `null`    | ID API du Canvas auquel appartient cet événement                           |
| `canvas_variation_api_id` | `string`, `null`    | ID API de la variation de Canvas à laquelle appartient cet événement                 |
| `canvas_step_api_id`      | `string`, `null`    | [Obsolète] ID d’API de l'étape du canvas à laquelle cet événement appartient         |
| `gender`                  | `string`, `null`    | [Données d'identification] Sexe de l'utilisateur                                             |
| `country`                 | `string`, `null`    | [PII] Pays de l'utilisateur                                            |
| `timezone`                | `string`, `null`    | Fuseau horaire de l'utilisateur                                                 |
| `language`                | `string`, `null`    | [PII] Langue de l'utilisateur                                           |
| `in_control_group`        | `boolean`, `null`   | Vrai si l'utilisateur était inscrit dans le groupe de contrôle                   |
| `sf_created_at`           | `timestamp`, `null` | Lorsque cet événement a été repris par le Snowpipe                        |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### UTILISATEURS_CANVAS_EXIT_MATCHEDAUDIENCE_SHARED {#USERS_CANVAS_EXIT_MATCHEDAUDIENCE_SHARED}

| Champ                     | Type                     | Description                                                          |
| ------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                      | `string`, `null`    | ID unique au niveau mondial pour cet événement                                    |
| `user_id`                 | `string`, `null`    | ID Braze de l'utilisateur qui a réalisé cet événement                        |
| `external_user_id`        | `string`, `null`    | [Données d'identification] ID externe de l'utilisateur                                   |
| `device_id`               | `string`, `null`    | ID de l'appareil lié à cet utilisateur, si l'utilisateur est anonyme |
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
| `external_user_id`        | `string`, `null`    | [Données d'identification] ID externe de l'utilisateur                                   |
| `device_id`               | `string`, `null`    | ID de l'appareil lié à cet utilisateur, si l'utilisateur est anonyme |
| `app_group_id`            | `string`, `null`    | ID Braze de l'espace de travail auquel cet utilisateur appartient                        |
| `app_group_api_id`        | `string`, `null`    | ID API de l'espace de travail auquel appartient cet utilisateur                         |
| `time`                    | `int`, `null`       | horodatage Unix du moment où l’événement s’est produit                           |
| `canvas_id`               | `string`, `null`    | (Réservé à l'usage de Braze) ID de la toile à laquelle appartient cet événement          |
| `canvas_api_id`           | `string`, `null`    | ID API du Canvas auquel appartient cet événement                           |
| `canvas_variation_api_id` | `string`, `null`    | ID API de la variation de Canvas à laquelle appartient cet événement                 |
| `canvas_step_api_id`      | `string`, `null`    | ID API de l'étape de Canvas auquel appartient cet événement                      |
| `sf_created_at`           | `timestamp`, `null` | Lorsque cet événement a été repris par le Snowpipe                        |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### UTILISATEURS_CANVAS_EXPERIMENTSTEP_CONVERSION_SHARED {#USERS_CANVAS_EXPERIMENTSTEP_CONVERSION_SHARED}

| Champ                       | Type                     | Description                                                                                                     |
| --------------------------- | ------------------------ | --------------------------------------------------------------------------------------------------------------- |
| `id`                        | `string`, `null`    | ID unique au niveau mondial pour cet événement                                                                               |
| `user_id`                   | `string`, `null`    | ID Braze de l'utilisateur qui a réalisé cet événement                                                                   |
| `external_user_id`          | `string`, `null`    | [Données d'identification] ID externe de l'utilisateur                                                                              |
| `device_id`                 | `string`, `null`    | ID de l'appareil lié à cet utilisateur, si l'utilisateur est anonyme                                            |
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
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### UTILISATEURS_CANVAS_EXPERIMENTSTEP_SPLITENTRY_SHARED {#USERS_CANVAS_EXPERIMENTSTEP_SPLITENTRY_SHARED}

| Champ                     | Type                     | Description                                                          |
| ------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                      | `string`, `null`    | ID unique au niveau mondial pour cet événement                                    |
| `user_id`                 | `string`, `null`    | ID Braze de l'utilisateur qui a réalisé cet événement                        |
| `external_user_id`        | `string`, `null`    | [Données d'identification] ID externe de l'utilisateur                                   |
| `device_id`               | `string`, `null`    | ID de l'appareil lié à cet utilisateur, si l'utilisateur est anonyme |
| `app_group_id`            | `string`, `null`    | ID Braze de l'espace de travail auquel cet utilisateur appartient                        |
| `time`                    | `int`, `null`       | horodatage Unix du moment où l’événement s’est produit                           |
| `canvas_id`               | `string`, `null`    | (Réservé à l'usage de Braze) ID de la toile à laquelle appartient cet événement          |
| `canvas_api_id`           | `string`, `null`    | ID API du Canvas auquel appartient cet événement                           |
| `canvas_variation_api_id` | `string`, `null`    | ID API de la variation de Canvas à laquelle appartient cet événement                 |
| `canvas_step_api_id`      | `string`, `null`    | ID API de l'étape de Canvas auquel appartient cet événement                      |
| `experiment_step_api_id`  | `string`, `null`    | ID API de l'étape d'expérimentation à laquelle cet événement appartient                  |
| `in_control_group`        | `boolean`, `null`   | Vrai si l'utilisateur était inscrit dans le groupe de contrôle                   |
| `sf_created_at`           | `timestamp`, `null` | Lorsque cet événement a été repris par le Snowpipe                        |

{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### UTILISATEURS_CANVAS_FREQUENCYCAP_SHARED {#USERS_CANVAS_FREQUENCYCAP_SHARED}

| Champ                                  | Type                     | Description                                                          |
| -------------------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                                   | `string`, `null`    | ID unique au niveau mondial pour cet événement                                    |
| `user_id`                              | `string`, `null`    | ID Braze de l'utilisateur qui a réalisé cet événement                        |
| `external_user_id`                     | `string`, `null`    | [Données d'identification] ID externe de l'utilisateur                                   |
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
| `gender`                               | `string`, `null`    | [Données d'identification] Sexe de l'utilisateur                                             |
| `country`                              | `string`, `null`    | [PII] Pays de l'utilisateur                                            |
| `timezone`                             | `string`, `null`    | Fuseau horaire de l'utilisateur                                                 |
| `language`                             | `string`, `null`    | [PII] Langue de l'utilisateur                                           |
| `sf_created_at`                        | `timestamp`, `null` | Lorsque cet événement a été repris par le Snowpipe                        |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### UTILISATEURS_CANVAS_REVENUE_SHARED {#USERS_CANVAS_REVENUE_SHARED}

| Champ                                  | Type                     | Description                                                          |
| -------------------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                                   | `string`, `null`    | ID unique au niveau mondial pour cet événement                                    |
| `user_id`                              | `string`, `null`    | ID Braze de l'utilisateur qui a réalisé cet événement                        |
| `external_user_id`                     | `string`, `null`    | [Données d'identification] ID externe de l'utilisateur                                   |
| `device_id`                            | `string`, `null`    | ID de l'appareil lié à cet utilisateur, si l'utilisateur est anonyme |
| `app_group_id`                         | `string`, `null`    | ID Braze de l'espace de travail auquel cet utilisateur appartient                        |
| `app_group_api_id`                     | `string`, `null`    | ID API de l'espace de travail auquel appartient cet utilisateur                         |
| `time`                                 | `int`, `null`       | horodatage Unix du moment où l’événement s’est produit                           |
| `canvas_id`                            | `string`, `null`    | (Réservé à l'usage de Braze) ID de la toile à laquelle appartient cet événement          |
| `canvas_api_id`                        | `string`, `null`    | ID API du Canvas auquel appartient cet événement                           |
| `canvas_variation_api_id`              | `string`, `null`    | ID API de la variation de Canvas à laquelle appartient cet événement                 |
| `canvas_step_api_id`                   | `string`, `null`    | ID API de l'étape de Canvas auquel appartient cet événement                      |
| `canvas_step_message_variation_api_id` | `string`, `null`    | ID API de la variation de message de l'étape de Canvas que l’utilisateur a reçue       |
| `gender`                               | `string`, `null`    | [Données d'identification] Sexe de l'utilisateur                                             |
| `country`                              | `string`, `null`    | [PII] Pays de l'utilisateur                                            |
| `timezone`                             | `string`, `null`    | Fuseau horaire de l'utilisateur                                                 |
| `language`                             | `string`, `null`    | [PII] Langue de l'utilisateur                                           |
| `revenue`                              | `int`, `null`       | Montant du chiffre d'affaires généré en USD, affiché en cents               |
| `sf_created_at`                        | `timestamp`, `null` | Lorsque cet événement a été repris par le Snowpipe                        |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Messages

### UTILISATEURS_MESSAGES_CONTENTCARD_ABORT_SHARED {#USERS_MESSAGES_CONTENTCARD_ABORT_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [Données d'identification] ID externe de l'utilisateur
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
`gender` | `null,` `string` | [Données d'identification] Sexe de l'utilisateur
`country` | `null,` `string` | [PII] Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [PII] Langue de l'utilisateur
`abort_type` | `null,` `string` | Type d'abandon, l'un des suivants : `liquid_abort_message` ou `rate_limit`
`abort_log` | `null,` `string` | [Données d'identification] Message du journal décrivant les détails de l'abandon (128 caractères maximum)
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### UTILISATEURS_MESSAGES_CONTENTCARD_CLICK_SHARED {#USERS_MESSAGES_CONTENTCARD_CLICK_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`content_card_id` | `string` | ID de la carte qui a généré cet événement
`external_user_id` | `null,` `string` | [Données d'identification] ID externe de l'utilisateur
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
`gender` | `null,` `string` | [Données d'identification] Sexe de l'utilisateur
`country` | `null,` `string` | [PII] Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [PII] Langue de l'utilisateur
`device_id` | `null,` `string` | ID de l’appareil sur lequel l’événement s’est produit
`sdk_version` | `null,` `string` | Version du SDK de Braze utilisée lors de l'événement
`platform` | `null,` `string` | Plate-forme de l'appareil
`os_version` | `null,` `string` | Version du système d'exploitation de l'appareil
`device_model` | `null,` `string` | Modèle de l'appareil
`resolution` | `null,` `string` | Résolution de l'appareil
`carrier` | `null,` `string` | Opérateur de l'appareil
`browser` | `null,` `string` | Navigateur de l'appareil
`ad_id` | `null,` `string` | [PII] Identifiant publicitaire
`ad_id_type` | `null,` `string` | Un parmi `ios_idfa`, `google_ad_id`, `windows_ad_id` OU `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Si le suivi publicitaire est activé pour l’appareil ou non
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### UTILISATEURS_MESSAGES_CONTENTCARD_DISMISS_SHARED {#USERS_MESSAGES_CONTENTCARD_DISMISS_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`content_card_id` | `string` | ID de la carte qui a généré cet événement
`external_user_id` | `null,` `string` | [Données d'identification] ID externe de l'utilisateur
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
`gender` | `null,` `string` | [Données d'identification] Sexe de l'utilisateur
`country` | `null,` `string` | [PII] Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [PII] Langue de l'utilisateur
`device_id` | `null,` `string` | ID de l’appareil sur lequel l’événement s’est produit
`sdk_version` | `null,` `string` | Version du SDK de Braze utilisée lors de l'événement
`platform` | `null,` `string` | Plate-forme de l'appareil
`os_version` | `null,` `string` | Version du système d'exploitation de l'appareil
`device_model` | `null,` `string` | Modèle de l'appareil
`resolution` | `null,` `string` | Résolution de l'appareil
`carrier` | `null,` `string` | Opérateur de l'appareil
`browser` | `null,` `string` | Navigateur de l'appareil
`ad_id` | `null,` `string` | [PII] Identifiant publicitaire
`ad_id_type` | `null,` `string` | Un parmi `ios_idfa`, `google_ad_id`, `windows_ad_id` OU `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Si le suivi publicitaire est activé pour l’appareil ou non
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_CONTENTCARD_IMPRESSION_SHARED {#USERS_MESSAGES_CONTENTCARD_IMPRESSION_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`content_card_id` | `string` | ID de la carte qui a généré cet événement
`external_user_id` | `null,` `string` | [Données d'identification] ID externe de l'utilisateur
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
`gender` | `null,` `string` | [Données d'identification] Sexe de l'utilisateur
`country` | `null,` `string` | [PII] Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [PII] Langue de l'utilisateur
`device_id` | `null,` `string` | ID de l’appareil sur lequel l’événement s’est produit
`sdk_version` | `null,` `string` | Version du SDK de Braze utilisée lors de l'événement
`platform` | `null,` `string` | Plate-forme de l'appareil
`os_version` | `null,` `string` | Version du système d'exploitation de l'appareil
`device_model` | `null,` `string` | Modèle de l'appareil
`resolution` | `null,` `string` | Résolution de l'appareil
`carrier` | `null,` `string` | Opérateur de l'appareil
`browser` | `null,` `string` | Navigateur de l'appareil
`ad_id` | `null,` `string` | [PII] Identifiant publicitaire
`ad_id_type` | `null,` `string` | Un parmi `ios_idfa`, `google_ad_id`, `windows_ad_id` OU `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Si le suivi publicitaire est activé pour l’appareil ou non
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### UTILISATEURS_MESSAGES_CONTENTCARD_SEND_SHARED {#USERS_MESSAGES_CONTENTCARD_SEND_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [Données d'identification] ID externe de l'utilisateur
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
`gender` | `null,` `string` | [Données d'identification] Sexe de l'utilisateur
`country` | `null,` `string` | [PII] Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [PII] Langue de l'utilisateur
`content_card_id` | `string` | ID de la carte qui a généré cet événement
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### UTILISATEURS_MESSAGES_EMAIL_ABORT_SHARED {#USERS_MESSAGES_EMAIL_ABORT_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [Données d'identification] ID externe de l'utilisateur
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
`gender` | `null,` `string` | [Données d'identification] Sexe de l'utilisateur
`country` | `null,` `string` | [PII] Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [PII] Langue de l'utilisateur
`email_address` | `string` | [PII] adresse e-mail de l'utilisateur
`ip_pool` | `null,` `string` | Ensemble d’IP à partir duquel l’e-mail a été envoyé
`abort_type` | `null,` `string` | Type d'abandon, l'un des suivants : `liquid_abort_message` ou `rate_limit`
`abort_log` | `null,` `string` | [Données d'identification] Message du journal décrivant les détails de l'abandon (128 caractères maximum)
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_BOUNCE_SHARED {#USERS_MESSAGES_EMAIL_BOUNCE_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [Données d'identification] ID externe de l'utilisateur
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
`gender` | `null,` `string` | [Données d'identification] Sexe de l'utilisateur
`country` | `null,` `string` | [PII] Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [PII] Langue de l'utilisateur
`email_address` | `string` | [PII] adresse e-mail de l'utilisateur
`sending_ip` | `null,` `string` | Adresse IP à partir de laquelle l’e-mail a été envoyé
`ip_pool` | `null,` `string` | Ensemble d’IP à partir duquel l’e-mail a été envoyé
`bounce_reason` | `null,` `string` | [Données d'identification] Le code de raison SMTP et le message convivial reçus pour cet événement de rebond
`esp` | `null,` `string` | ESP lié à l'événement (SparkPost, SendGrid, ou Amazon SES)
`from_domain` | `null,` `string` | Domaine d'envoi de l'e-mail
`is_drop` | `null, boolean` | Indique que cet événement est décompté comme un événement d’abandon
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_CLICK_SHARED {#USERS_MESSAGES_EMAIL_CLICK_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [Données d'identification] ID externe de l'utilisateur
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
`gender` | `null,` `string` | [Données d'identification] Sexe de l'utilisateur
`country` | `null,` `string` | [PII] Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [PII] Langue de l'utilisateur
`email_address` | `string` | [PII] adresse e-mail de l'utilisateur
`url` | `null,` `string` | URL sur laquelle l’utilisateur a cliqué
`user_agent` | `null,` `string` | Agent utilisateur sur lequel le clic s'est produit
`ip_pool` | `null,` `string` | Ensemble d’IP à partir duquel l’e-mail a été envoyé
`link_id` | `null,` `string` | ID unique du lien sur lequel on a cliqué, tel que créé par Braze
`link_alias` | `null,` `string` | Alias associé à cet ID de lien
`esp` | `null,` `string` | ESP lié à l'événement (SparkPost, SendGrid, ou Amazon SES)
`from_domain` | `null,` `string` | Domaine d'envoi de l'e-mail
`is_amp` | `null, boolean` | Indique qu'il s'agit d'un événement AMP
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_DELIVERY_SHARED {#USERS_MESSAGES_EMAIL_DELIVERY_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [Données d'identification] ID externe de l'utilisateur
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
`gender` | `null,` `string` | [Données d'identification] Sexe de l'utilisateur
`country` | `null,` `string` | [PII] Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [PII] Langue de l'utilisateur
`email_address` | `string` | [PII] adresse e-mail de l'utilisateur
`sending_ip` | `null,` `string` | Adresse IP à partir de laquelle l’e-mail a été envoyé
`ip_pool` | `null,` `string` | Ensemble d’IP à partir duquel l’e-mail a été envoyé
`esp` | `null,` `string` | ESP lié à l'événement (SparkPost, SendGrid, ou Amazon SES)
`from_domain` | `null,` `string` | Domaine d'envoi de l'e-mail
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### UTILISATEURS_MESSAGES_EMAIL_MARKASSPAM_SHARED {#USERS_MESSAGES_EMAIL_MARKASSPAM_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [Données d'identification] ID externe de l'utilisateur
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
`gender` | `null,` `string` | [Données d'identification] Sexe de l'utilisateur
`country` | `null,` `string` | [PII] Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [PII] Langue de l'utilisateur
`email_address` | `string` | [PII] adresse e-mail de l'utilisateur
`user_agent` | `null,` `string` | Agent utilisateur sur lequel le signalement du courrier indésirable a eu lieu
`ip_pool` | `null,` `string` | Ensemble d’IP à partir duquel l’e-mail a été envoyé
`esp` | `null,` `string` | ESP lié à l'événement (SparkPost, SendGrid, ou Amazon SES)
`from_domain` | `null,` `string` | Domaine d'envoi de l'e-mail
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_OPEN_SHARED {#USERS_MESSAGES_EMAIL_OPEN_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [Données d'identification] ID externe de l'utilisateur
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
`gender` | `null,` `string` | [Données d'identification] Sexe de l'utilisateur
`country` | `null,` `string` | [PII] Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [PII] Langue de l'utilisateur
`email_address` | `string` | [PII] adresse e-mail de l'utilisateur
`user_agent` | `null,` `string` | Agent utilisateur sur lequel l'ouverture s'est produite
`ip_pool` | `null,` `string` | Ensemble d’IP à partir duquel l’e-mail a été envoyé
`machine_open` | `null,` `string` | La valeur "true" est indiquée si l'événement d'ouverture est déclenché sans l'intervention de l'utilisateur, par exemple, par un appareil Apple sur lequel la protection de la confidentialité du courrier est activée. La valeur peut changer au fil du temps pour fournir plus de granularité.
`esp` | `null,` `string` | ESP lié à l'événement (SparkPost, SendGrid, ou Amazon SES)
`from_domain` | `null,` `string` | Domaine d'envoi de l'e-mail
`is_amp` | `null, boolean` | Indique qu'il s'agit d'un événement AMP
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### UTILISATEURS_MESSAGES_EMAIL_SEND_SHARED {#USERS_MESSAGES_EMAIL_SEND_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [Données d'identification] ID externe de l'utilisateur
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
`gender` | `null,` `string` | [Données d'identification] Sexe de l'utilisateur
`country` | `null,` `string` | [PII] Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [PII] Langue de l'utilisateur
`email_address` | `string` | [PII] adresse e-mail de l'utilisateur
`ip_pool` | `null,` `string` | Ensemble d’IP à partir duquel l’e-mail a été envoyé
`message_extras` | `null,` `string` | [Données d'identification] Chaîne JSON des paires clé-valeur balisées lors du rendu Liquid
`esp` | `null,` `string` | ESP lié à l'événement (SparkPost, SendGrid, ou Amazon SES)
`from_domain` | `null,` `string` | Domaine d'envoi de l'e-mail
`sf_created_at` | `timestamp`, `null` | Lorsque cet événement a été repris par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### UTILISATEURS_MESSAGES_EMAIL_SOFTBOUNCE_SHARED {#USERS_MESSAGES_EMAIL_SOFTBOUNCE_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [Données d'identification] ID externe de l'utilisateur
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
`gender` | `null,` `string` | [Données d'identification] Sexe de l'utilisateur
`country` | `null,` `string` | [PII] Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [PII] Langue de l'utilisateur
`email_address` | `string` | [PII] adresse e-mail de l'utilisateur
`sending_ip` | `null,` `string` | Adresse IP à partir de laquelle l’e-mail a été envoyé
`ip_pool` | `null,` `string` | Ensemble d’IP à partir duquel l’e-mail a été envoyé
`bounce_reason` | `null,` `string` | [Données d'identification] Le code de raison SMTP et le message convivial reçus pour cet événement de rebond
`esp` | `null,` `string` | ESP lié à l'événement (SparkPost, SendGrid, ou Amazon SES)
`from_domain` | `null,` `string` | Domaine d'envoi de l'e-mail
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED {#USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [Données d'identification] ID externe de l'utilisateur
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
`gender` | `null,` `string` | [Données d'identification] Sexe de l'utilisateur
`country` | `null,` `string` | [PII] Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [PII] Langue de l'utilisateur
`email_address` | `string` | [PII] adresse e-mail de l'utilisateur
`ip_pool` | `null,` `string` | Ensemble d’IP à partir duquel l’e-mail a été envoyé
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### UTILISATEURS_MESSAGES_INAPPMESSAGE_ABORT_SHARED {#USERS_MESSAGES_INAPPMESSAGE_ABORT_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [Données d'identification] ID externe de l'utilisateur
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
`gender` | `null,` `string` | [Données d'identification] Sexe de l'utilisateur
`country` | `null,` `string` | [PII] Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [PII] Langue de l'utilisateur
`device_id` | `null,` `string` | ID de l’appareil sur lequel l’événement s’est produit
`sdk_version` | `null,` `string` | Version du SDK de Braze utilisée lors de l'événement
`platform` | `null,` `string` | Plate-forme de l'appareil
`os_version` | `null,` `string` | Version du système d'exploitation de l'appareil
`device_model` | `null,` `string` | Modèle de l'appareil
`resolution` | `null,` `string` | Résolution de l'appareil
`carrier` | `null,` `string` | Opérateur de l'appareil
`browser` | `null,` `string` | Navigateur de l'appareil
`version` | `string` | Quelle version du message in-app, ancienne ou déclenchée ?
`ad_id` | `null,` `string` | [PII] Identifiant publicitaire
`ad_id_type` | `null,` `string` | Un parmi `ios_idfa`, `google_ad_id`, `windows_ad_id` OU `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Si le suivi publicitaire est activé pour l’appareil ou non
`abort_type` | `null,` `string` | Type d'abandon, l'un des suivants : `liquid_abort_message` ou `rate_limit`
`abort_log` | `null,` `string` | [Données d'identification] Message du journal décrivant les détails de l'abandon (128 caractères maximum)
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### UTILISATEURS_MESSAGES_INAPPMESSAGE_CLICK_SHARED {#USERS_MESSAGES_INAPPMESSAGE_CLICK_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [Données d'identification] ID externe de l'utilisateur
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
`gender` | `null,` `string` | [Données d'identification] Sexe de l'utilisateur
`country` | `null,` `string` | [PII] Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [PII] Langue de l'utilisateur
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
`ad_id` | `null,` `string` | [PII] Identifiant publicitaire
`ad_id_type` | `null,` `string` | Un parmi `ios_idfa`, `google_ad_id`, `windows_ad_id` OU `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Si le suivi publicitaire est activé pour l’appareil ou non
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_INAPPMESSAGE_IMPRESSION_SHARED {#USERS_MESSAGES_INAPPMESSAGE_IMPRESSION_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [Données d'identification] ID externe de l'utilisateur
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
`gender` | `null,` `string` | [Données d'identification] Sexe de l'utilisateur
`country` | `null,` `string` | [PII] Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [PII] Langue de l'utilisateur
`device_id` | `null,` `string` | ID de l’appareil sur lequel l’événement s’est produit
`sdk_version` | `null,` `string` | Version du SDK de Braze utilisée lors de l'événement
`platform` | `null,` `string` | Plate-forme de l'appareil
`os_version` | `null,` `string` | Version du système d'exploitation de l'appareil
`device_model` | `null,` `string` | Modèle de l'appareil
`resolution` | `null,` `string` | résolution de l’appareil
`carrier` | `null,` `string` | opérateur de l’appareil
`browser` | `null,` `string` | navigateur de l’appareil
`version` | `string` | quelle version du message in-app, héritée ou déclenchée
`ad_id` | `null,` `string` | [PII] Identifiant publicitaire
`ad_id_type` | `null,` `string` | Un parmi `ios_idfa`, `google_ad_id`, `windows_ad_id` OU `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Si le suivi publicitaire est activé pour l’appareil ou non
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_NEWSFEEDCARD_ABORT_SHARED {#USERS_MESSAGES_NEWSFEEDCARD_ABORT_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [Données d'identification] ID externe de l'utilisateur
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`time` | `int` | horodatage Unix du moment où l’événement s’est produit
`app_api_id` | `null,` `string` | ID API de l’application sur laquelle cet événement s’est produit
`card_api_id` | `null,` `string` | ID API de la carte
`gender` | `null,` `string` | [Données d'identification] Sexe de l'utilisateur
`country` | `null,` `string` | [PII] Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [PII] Langue de l'utilisateur
`device_id` | `null,` `string` | ID de l’appareil sur lequel l’événement s’est produit
`sdk_version` | `null,` `string` | Version du SDK de Braze utilisée lors de l'événement
`platform` | `null,` `string` | Plate-forme de l'appareil
`os_version` | `null,` `string` | Version du système d'exploitation de l'appareil
`device_model` | `null,` `string` | Modèle de l'appareil
`resolution` | `null,` `string` | résolution de l’appareil
`carrier` | `null,` `string` | opérateur de l’appareil
`browser` | `null,` `string` | navigateur de l’appareil
`abort_type` | `null,` `string` | Type d'abandon, l'un des suivants : `liquid_abort_message` ou `rate_limit`
`abort_log` | `null,` `string` | [Données d'identification] Message du journal décrivant les détails de l'abandon (128 caractères maximum)
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_NEWSFEEDCARD_CLICK_SHARED {#USERS_MESSAGES_NEWSFEEDCARD_CLICK_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [Données d'identification] ID externe de l'utilisateur
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`time` | `int` | horodatage Unix du moment où l’événement s’est produit
`app_api_id` | `null,` `string` | ID API de l’application sur laquelle cet événement s’est produit
`card_api_id` | `null,` `string` | ID API de la carte
`gender` | `null,` `string` | [Données d'identification] Sexe de l'utilisateur
`country` | `null,` `string` | [PII] Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [PII] Langue de l'utilisateur
`device_id` | `null,` `string` | ID de l’appareil sur lequel l’événement s’est produit
`sdk_version` | `null,` `string` | Version du SDK de Braze utilisée lors de l'événement
`platform` | `null,` `string` | Plate-forme de l'appareil
`os_version` | `null,` `string` | Version du système d'exploitation de l'appareil
`device_model` | `null,` `string` | Modèle de l'appareil
`resolution` | `null,` `string` | résolution de l’appareil
`carrier` | `null,` `string` | opérateur de l’appareil
`browser` | `null,` `string` | navigateur de l’appareil
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_NEWSFEEDCARD_IMPRESSION_SHARED {#USERS_MESSAGES_NEWSFEEDCARD_IMPRESSION_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [Données d'identification] ID externe de l'utilisateur
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`time` | `int` | horodatage Unix du moment où l’événement s’est produit
`app_api_id` | `null,` `string` | ID API de l’application sur laquelle cet événement s’est produit
`card_api_id` | `null,` `string` | ID API de la carte
`gender` | `null,` `string` | [Données d'identification] Sexe de l'utilisateur
`country` | `null,` `string` | [PII] Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [PII] Langue de l'utilisateur
`device_id` | `null,` `string` | ID de l’appareil sur lequel l’événement s’est produit
`sdk_version` | `null,` `string` | Version du SDK de Braze utilisée lors de l'événement
`platform` | `null,` `string` | Plate-forme de l'appareil
`os_version` | `null,` `string` | Version du système d'exploitation de l'appareil
`device_model` | `null,` `string` | Modèle de l'appareil
`resolution` | `null,` `string` | résolution de l’appareil
`carrier` | `null,` `string` | opérateur de l’appareil
`browser` | `null,` `string` | navigateur de l’appareil
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### UTILISATEURS_MESSAGES_PUSHNOTIFICATION_ABORT_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_ABORT_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [Données d'identification] ID externe de l'utilisateur
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
`gender` | `null,` `string` | [Données d'identification] Sexe de l'utilisateur
`country` | `null,` `string` | [PII] Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [PII] Langue de l'utilisateur
`platform` | `string` | Plate-forme de l'appareil
`abort_type` | `null,` `string` | Type d'abandon, l'un des suivants : `liquid_abort_message` ou `rate_limit`
`abort_log` | `null,` `string` | [Données d'identification] Message du journal décrivant les détails de l'abandon (128 caractères maximum)
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### UTILISATEURS_MESSAGES_PUSHNOTIFICATION_BOUNCE_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_BOUNCE_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [Données d'identification] ID externe de l'utilisateur
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
`gender` | `null,` `string` | [Données d'identification] Sexe de l'utilisateur
`country` | `null,` `string` | [PII] Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [PII] Langue de l'utilisateur
`platform` | `null,` `string` | Plate-forme de l'appareil
`ad_id` | `null,` `string` | [Données d'identification] ID publicitaire de l'appareil sur lequel nous avons fait une tentative de distribution
`ad_id_type` | `null,` `string` | Type de l'ID publicitaire
`ad_tracking_enabled` | `null, boolean` | Si le suivi est activé ou non pour la publicité
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### UTILISATEURS_MESSAGES_PUSHNOTIFICATION_INFLUENCEDOPEN_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_INFLUENCEDOPEN_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [Données d'identification] ID externe de l'utilisateur
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
`gender` | `null,` `string` | [Données d'identification] Sexe de l'utilisateur
`country` | `null,` `string` | [PII] Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [PII] Langue de l'utilisateur
`device_id` | `null,` `string` | ID de l’appareil sur lequel l’événement s’est produit
`sdk_version` | `null,` `string` | Version du SDK de Braze utilisée lors de l'événement
`platform` | `null,` `string` | Plate-forme de l'appareil
`os_version` | `null,` `string` | Version du système d'exploitation de l'appareil
`device_model` | `null,` `string` | Modèle de l'appareil
`resolution` | `null,` `string` | Résolution de l'appareil
`carrier` | `null,` `string` | Opérateur de l'appareil
`browser` | `null,` `string` | Navigateur de l'appareil
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_PUSHNOTIFICATION_IOSFOREGROUND_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_IOSFOREGROUND_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [Données d'identification] ID externe de l'utilisateur
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
`gender` | `null,` `string` | [Données d'identification] Sexe de l'utilisateur
`country` | `null,` `string` | [PII] Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [PII] Langue de l'utilisateur
`device_id` | `null,` `string` | ID de l’appareil sur lequel l’événement s’est produit
`sdk_version` | `null,` `string` | Version du SDK de Braze utilisée lors de l'événement
`platform` | `null,` `string` | Plate-forme de l'appareil
`os_version` | `null,` `string` | Version du système d'exploitation de l'appareil
`device_model` | `null,` `string` | Modèle de l'appareil
`resolution` | `null,` `string` | Résolution de l'appareil
`carrier` | `null,` `string` | Opérateur de l'appareil
`browser` | `null,` `string` | Navigateur de l'appareil
`ad_id` | `null,` `string` | [Données d'identification] ID publicitaire de l'appareil sur lequel nous avons fait une tentative de distribution
`ad_id_type` | `null,` `string` | Type de l'ID publicitaire
`ad_tracking_enabled` | `null, boolean` | Si le suivi est activé ou non pour la publicité
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### UTILISATEURS_MESSAGES_PUSHNOTIFICATION_OPEN_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_OPEN_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [Données d'identification] ID externe de l'utilisateur
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
`gender` | `null,` `string` | [Données d'identification] Sexe de l'utilisateur
`country` | `null,` `string` | [PII] Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [PII] Langue de l'utilisateur
`device_id` | `null,` `string` | ID de l’appareil sur lequel l’événement s’est produit
`sdk_version` | `null,` `string` | Version du SDK de Braze utilisée lors de l'événement
`platform` | `null,` `string` | Plate-forme de l'appareil
`os_version` | `null,` `string` | Version du système d'exploitation de l'appareil
`device_model` | `null,` `string` | Modèle de l'appareil
`resolution` | `null,` `string` | Résolution de l'appareil
`carrier` | `null,` `string` | Opérateur de l'appareil
`browser` | `null,` `string` | Navigateur de l'appareil
`button_string` | `null,` `string` | Identifiant (chaîne_de_bouton) du bouton de notification push cliqué. null s'il ne s'agit pas d'un clic sur un bouton.
`button_action_type` | `null,` `string` | Type d’action du bouton de la notification push. Un des éléments suivants : [URI, DEEP_LINK, NONE, CLOSE]. null s'il ne provient pas d'un clic sur un bouton
`slide_id` | `null,` `string` | identifiant de diapositive de la diapositive de carrousel de notification push sur laquelle l’utilisateur a cliqué
`slide_action_type` | `null,` `string` | Type d'action de la diapositive du carrousel de poussée
`ad_id` | `null,` `string` | [Données d'identification] ID publicitaire de l'appareil sur lequel nous avons fait une tentative de distribution
`ad_id_type` | `null,` `string` | Type de l'ID publicitaire
`ad_tracking_enabled` | `null, boolean` | Si le suivi est activé ou non pour la publicité
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### UTILISATEURS_MESSAGES_PUSHNOTIFICATION_SEND_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_SEND_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [Données d'identification] ID externe de l'utilisateur
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
`gender` | `null,` `string` | [Données d'identification] Sexe de l'utilisateur
`country` | `null,` `string` | [PII] Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [PII] Langue de l'utilisateur
`platform` | `string` | Plate-forme de l'appareil
`ad_id` | `null,` `string` | [Données d'identification] ID publicitaire de l'appareil sur lequel nous avons fait une tentative de distribution
`ad_id_type` | `null,` `string` | Type de l'ID publicitaire
`ad_tracking_enabled` | `null, boolean` | Si le suivi est activé ou non pour la publicité
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### UTILISATEURS_MESSAGES_SMS_ABORT_SHARED {#USERS_MESSAGES_SMS_ABORT_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [Données d'identification] ID externe de l'utilisateur
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
`abort_type` | `null,` `string` | Type d'abandon, l'un des suivants : `liquid_abort_message` ou `rate_limit`
`abort_log` | `null,` `string` | [Données d'identification] Message du journal décrivant les détails de l'abandon (128 caractères maximum)
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_CARRIERSEND_SHARED {#USERS_MESSAGES_SMS_CARRIERSEND_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [Données d'identification] ID externe de l'utilisateur
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
`gender` | `null,` `string` | [Données d'identification] Sexe de l'utilisateur
`country` | `null,` `string` | [PII] Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [PII] Langue de l'utilisateur
`to_phone_number` | `null,` `string` | [PII] numéro de téléphone du destinataire
`from_phone_number` | `null,` `string` | numéro de téléphone à partir duquel le message SMS a été envoyé
`subscription_group_api_id` | `null,` `string` | ID externe du groupe d’abonnement
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_DELIVERY_SHARED {#USERS_MESSAGES_SMS_DELIVERY_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [Données d'identification] ID externe de l'utilisateur
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
`gender` | `null,` `string` | [Données d'identification] Sexe de l'utilisateur
`country` | `null,` `string` | [PII] Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [PII] Langue de l'utilisateur
`to_phone_number` | `null,` `string` | [PII] numéro de téléphone du destinataire
`from_phone_number` | `null,` `string` | Numéro de téléphone à partir duquel le message SMS a été envoyé
`subscription_group_api_id` | `null,` `string` | ID externe du groupe d'abonnement
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED {#USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [Données d'identification] ID externe de l'utilisateur
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
`gender` | `null,` `string` | [Données d'identification] Sexe de l'utilisateur
`country` | `null,` `string` | [PII] Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [PII] Langue de l'utilisateur
`to_phone_number` | `null,` `string` | [PII] numéro de téléphone du destinataire
`subscription_group_api_id` | `null,` `string` | ID externe du groupe d’abonnement
`error` | `null,` `string` | nom de l’erreur
`provider_error_code` | `null,` `string` | code d'erreur du fournisseur de services SMS
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### UTILISATEURS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED {#USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `null,` `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [Données d'identification] ID externe de l'utilisateur
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail associé au numéro de téléphone entrant.
`time` | `int` | horodatage Unix du moment où l’événement s’est produit
`user_phone_number` | `string` | [PII] le numéro de téléphone de l'utilisateur à partir duquel le message a été reçu
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
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_REJECTION_SHARED {#USERS_MESSAGES_SMS_REJECTION_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [Données d'identification] ID externe de l'utilisateur
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
`gender` | `null,` `string` | [Données d'identification] Sexe de l'utilisateur
`country` | `null,` `string` | [PII] Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [PII] Langue de l'utilisateur
`to_phone_number` | `null,` `string` | [PII] numéro de téléphone du destinataire
`from_phone_number` | `null,` `string` | numéro de téléphone à partir duquel le message SMS a été envoyé
`subscription_group_api_id` | `null,` `string` | ID externe du groupe d’abonnement
`error` | `null,` `string` | nom de l’erreur
`provider_error_code` | `null,` `string` | code d'erreur du fournisseur de services SMS
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### UTILISATEURS_MESSAGES_SMS_SEND_SHARED {#USERS_MESSAGES_SMS_SEND_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [Données d'identification] ID externe de l'utilisateur
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
`gender` | `null,` `string` | [Données d'identification] Sexe de l'utilisateur
`country` | `null,` `string` | [PII] Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [PII] Langue de l'utilisateur
`to_phone_number` | `null,` `string` | [PII] numéro de téléphone du destinataire
`subscription_group_api_id` | `null,` `string` | ID externe du groupe d’abonnement
`category` | `null,` `string` | Nom de catégorie de mot-clé, uniquement renseigné pour les messages de réponse automatique : ’Abonné’, ’Désabonné’, ’Aide’ ou valeur personnalisée
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### UTILISATEURS_MESSAGES_SMS_SHORTLINKCLICK_SHARED {#USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `null,` `string` | ID Braze de l'utilisateur ciblé par short_url, null si short_url n'a pas utilisé le suivi des clics de l'utilisateur.
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur ciblé par short_url s'il existe, null si short_url n'a pas utilisé le ciblage des clics de l'utilisateur.
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail utilisé pour générer short_url
`time` | `int` | Date Unix à laquelle short_url a été cliqué
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`campaign_id` | `null,` `string` | ID Braze de la campagne pour laquelle le short_url a été généré, null s'il ne s'agit pas d'une campagne.
`campaign_api_id` | `null,` `string` | API ID de la campagne pour laquelle short_url a été généré, null s'il ne s'agit pas d'une campagne.
`message_variation_api_id` | `null,` `string` | API ID de la variation du message pour lequel le short_url a été généré, null s'il ne s'agit pas d'une campagne.
`canvas_id` | `null,` `string` | ID Braze de la toile pour laquelle le short_url a été généré, null s'il ne s'agit pas d'une toile.
`canvas_api_id` | `null,` `string` | API ID du Canvas pour lequel short_url a été généré, null s'il ne provient pas d'un Canvas
`canvas_variation_api_id` | `null,` `string` | API ID de la toile pour laquelle la variation short_url a été générée, null si elle ne provient pas d'une toile.
`canvas_step_api_id` | `null,` `string` | API ID de l'étape du canvas pour laquelle le short_url a été généré, null s'il ne provient pas d'un canvas
`canvas_step_message_variation_api_id` | `null,` `string` | API ID de l'étape du canvas pour lequel le message de variation short_url a été généré, null s'il ne s'agit pas d'un canvas.
`url` | `string` | URL original contenu dans le message qui est redirigé par short_url
`short_url` | `string` | URL raccourcie qui a été cliquée
`user_agent` | `null,` `string` | agent utilisateur demandant le short_url
`user_phone_number` | `string` | [PII] le numéro de téléphone de l'utilisateur
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### UTILISATEURS_MESSAGES_WEBHOOK_ABORT_SHARED {#USERS_MESSAGES_WEBHOOK_ABORT_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [Données d'identification] ID externe de l'utilisateur
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
`gender` | `null,` `string` | [Données d'identification] Sexe de l'utilisateur
`country` | `null,` `string` | [PII] Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [PII] Langue de l'utilisateur
`abort_type` | `null,` `string` | Type d'abandon, l'un des suivants : `liquid_abort_message` ou `rate_limit`
`abort_log` | `null,` `string` | [Données d'identification] Message du journal décrivant les détails de l'abandon (128 caractères maximum)
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### UTILISATEURS_MESSAGES_WEBHOOK_SEND_SHARED {#USERS_MESSAGES_WEBHOOK_SEND_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [Données d'identification] ID externe de l'utilisateur
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
`gender` | `null,` `string` | [Données d'identification] Sexe de l'utilisateur
`country` | `null,` `string` | [PII] Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [PII] Langue de l'utilisateur
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WHATSAPP_ABORT_SHARED {#USERS_MESSAGES_WHATSAPP_ABORT_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`time` | `int` | horodatage Unix du moment où l’événement s’est produit
`to_phone_number` | 	`null,` `string` | [PII] numéro de téléphone du destinataire
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [Données d'identification] ID externe de l'utilisateur
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
`abort_type` | `null,` `string` | Type d'abandon, l'un des suivants : `liquid_abort_message` ou `rate_limit`
`abort_log` | `null,` `string` | [Données d'identification] Message du journal décrivant les détails de l'abandon (128 caractères maximum)
`sf_created_at` | `timestamp`, `null` | Lorsque cet événement a été repris par le Snowpipe      
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WHATSAPP_DELIVERY_SHARED {#USERS_MESSAGES_WHATSAPP_DELIVERY_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`time` | `int` | horodatage Unix du moment où l’événement s’est produit
`to_phone_number` | `null,` `string` | [PII] numéro de téléphone du destinataire
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [Données d'identification] ID externe de l'utilisateur
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
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### UTILISATEURS_MESSAGES_WHATSAPP_FAILURE_SHARED {#USERS_MESSAGES_WHATSAPP_FAILURE_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`time` | `int` | horodatage Unix du moment où l’événement s’est produit
`to_phone_number` | `null,` `string` | [PII] numéro de téléphone du destinataire
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [Données d'identification] ID externe de l'utilisateur
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
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### UTILISATEURS_MESSAGES_WHATSAPP_INBOUNDRECEIVE_SHARED {#USERS_MESSAGES_WHATSAPP_INBOUNDRECEIVE_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`time` | `int` | horodatage Unix du moment où l’événement s’est produit
`user_phone_number` | `string` | [PII] le numéro de téléphone de l'utilisateur à partir duquel le message a été reçu
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [Données d'identification] ID externe de l'utilisateur
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
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### UTILISATEURS_MESSAGES_WHATSAPP_READ_SHARED {#USERS_MESSAGES_WHATSAPP_READ_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`time` | `int` | horodatage Unix du moment où l’événement s’est produit
`to_phone_number` | `null,` `string` | [PII] numéro de téléphone du destinataire
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [Données d'identification] ID externe de l'utilisateur
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
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### UTILISATEURS_MESSAGES_WHATSAPP_SEND_SHARED {#USERS_MESSAGES_WHATSAPP_SEND_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`time` | `int` | horodatage Unix du moment où l’événement s’est produit
`to_phone_number` | `null,` `string`	| [PII] numéro de téléphone du destinataire
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [Données d'identification] ID externe de l'utilisateur
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
`message_extras` | `null,` `string` | [Données d'identification] Chaîne JSON des paires clé-valeur balisées lors du rendu Liquid
`sf_created_at` | `timestamp`, `null` | Lorsque cet événement a été repris par le Snowpipe      
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Utilisateurs

### USERS_RANDOMBUCKETNUMBERUPDATE_SHARED {#USERS_RANDOMBUCKETNUMBERUPDATE_SHARED}

| Champ                       | Type                     | Description                                        |
| --------------------------- | ------------------------ | -------------------------------------------------- |
| `id`                        | `string`, `null`    | ID unique au niveau mondial pour cet événement                  |
| `app_group_id`              | `string`, `null`    | ID Braze de l'espace de travail auquel cet utilisateur appartient      |
| `app_group_api_id`          | `string`, `null`    | ID API de l'espace de travail auquel appartient cet utilisateur       |
| `user_id`                   | `string`, `null`    | ID Braze de l'utilisateur qui a réalisé cet événement      |
| `external_user_id`          | `string`, `null`    | [Données d'identification] ID externe de l'utilisateur                 |
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
| `external_user_id` | `string`, `null`    | [Données d'identification] ID externe de l'utilisateur                                            |
| `device_id`        | `string`, `null`    | ID de l'appareil lié à cet utilisateur, si l'utilisateur est anonyme          |
| `app_group_id`     | `string`, `null`    | ID Braze de l'espace de travail auquel cet utilisateur appartient                                 |
| `app_group_api_id` | `string`, `null`    | ID API de l'espace de travail auquel appartient cet utilisateur                                  |
| `app_api_id`       | `string`, `null`    | ID API de l'application à laquelle appartenait l'utilisateur orphelin.                               |
| `time`             | `int`, `null`       | Date Unix à laquelle l'utilisateur est devenu orphelin                                 |
| `orphaned_by_id`   | `string`, `null`    | ID Braze de l'utilisateur dont le profil a été fusionné avec le profil de l'utilisateur orphelin. |
| `sf_created_at`    | `timestamp`, `null` | Lorsque cet événement a été repris par le Snowpipe                                 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }
