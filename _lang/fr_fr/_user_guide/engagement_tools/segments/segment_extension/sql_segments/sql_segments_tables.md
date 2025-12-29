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

## Table des matières

Tableau | Description
------|------------
[USERS_BEHAVIORS_CUSTOMEVENT_SHARED](#USERS_BEHAVIORS_CUSTOMEVENT_SHARED) | Lorsqu'un utilisateur effectue un événement personnalisé
[USERS_BEHAVIORS_INSTALLATTRIBUTION_SHARED](#USERS_BEHAVIORS_INSTALLATTRIBUTION_SHARED) | Lorsqu'un utilisateur installe une application et que nous l'attribuons à un partenaire.
[USERS_BEHAVIORS_LOCATION_SHARED](#USERS_BEHAVIORS_LOCATION_SHARED) | Lorsqu'un utilisateur enregistre un emplacement/localisation
[USERS_BEHAVIORS_PURCHASE_SHARED](#USERS_BEHAVIORS_PURCHASE_SHARED) | Lorsqu'un utilisateur effectue un achat
[USERS_BEHAVIORS_UNINSTALL_SHARED](#USERS_BEHAVIORS_UNINSTALL_SHARED) | Lorsqu'un utilisateur désinstalle une application
[USERS_BEHAVIORS_UPGRADEDAPP_SHARED](#USERS_BEHAVIORS_UPGRADEDAPP_SHARED) | Lorsqu'un utilisateur met à jour l'application
[USERS_BEHAVIORS_APP_FIRSTSESSION_SHARED](#USERS_BEHAVIORS_APP_FIRSTSESSION_SHARED) | Lors de la première session d'un utilisateur
[USERS_BEHAVIORS_APP_NEWSFEEDIMPRESSION_SHARED](#USERS_BEHAVIORS_APP_NEWSFEEDIMPRESSION_SHARED) | Lorsqu'un utilisateur consulte le fil d'actualité
[USERS_BEHAVIORS_APP_SESSIONEND_SHARED](#USERS_BEHAVIORS_APP_SESSIONEND_SHARED) | Lorsqu'un utilisateur finalise une session sur une application
[USERS_BEHAVIORS_APP_SESSIONSTART_SHARED](#USERS_BEHAVIORS_APP_SESSIONSTART_SHARED) | Lorsqu'un utilisateur commence une session sur une application
[USERS_BEHAVIORS_GEOFENCE_DATAEVENT_SHARED](#USERS_BEHAVIORS_GEOFENCE_DATAEVENT_SHARED) | Lorsqu'un utilisateur déclenche une zone géorepérée (par exemple, lorsqu'il entre ou sort d'un géorepérage). Cet événement a été regroupé avec d'autres événements et reçu par l'intermédiaire de l'endpoint d'événements standard. Il est donc possible que l'endpoint ne l'ait pas reçu en temps réel.
[USERS_BEHAVIORS_GEOFENCE_RECORDEVENT_SHARED](#USERS_BEHAVIORS_GEOFENCE_RECORDEVENT_SHARED) | Lorsqu'un utilisateur déclenche une zone géorepérée (par exemple, lorsqu'il entre ou sort d'un géorepérage). Cet événement a été reçu par l'endpoint dédié au géorepérage et est donc reçu en temps réel dès que l'appareil d'un utilisateur détecte qu'il a déclenché un géorepérage. <br><br>En outre, en raison de la limite de débit sur l'endpoint de géorepérage, il est possible que certains événements de géorepérage ne soient pas reflétés comme un RecordEvent. Tous les événements de géorepérage sont toutefois conseillés par DataEvent (mais potentiellement avec un certain retard dû à la mise en lots).
[USERS_BEHAVIORS_SUBSCRIPTION_GLOBALSTATECHANGE_SHARED](#USERS_BEHAVIORS_SUBSCRIPTION_GLOBALSTATECHANGE_SHARED) | Lorsqu'un utilisateur est abonné ou s'est désabonné globalement d'un canal tel que l'e-mail
[USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED](#USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED) | Lorsqu'un utilisateur est abonné ou désabonné à un groupe d'abonnement.
[USERS_CAMPAIGNS_CONVERSION_SHARED](#USERS_CAMPAIGNS_CONVERSION_SHARED) | Lorsqu'un utilisateur convertit pour une campagne
[USERS_CAMPAIGNS_ENROLLINCONTROL_SHARED](#USERS_CAMPAIGNS_ENROLLINCONTROL_SHARED) | Lorsqu'un utilisateur est inscrit dans le groupe de contrôle d'une campagne
[USERS_CAMPAIGNS_FREQUENCYCAP_SHARED](#USERS_CAMPAIGNS_FREQUENCYCAP_SHARED) | Lorsqu'un utilisateur est soumis à une limite de fréquence pour une campagne
[USERS_CAMPAIGNS_REVENUE_SHARED](#USERS_CAMPAIGNS_REVENUE_SHARED) | Lorsqu'un utilisateur génère des chiffres d'affaires au cours de la période de conversion primaire.
[USERS_CANVASSTEP_PROGRESSION_SHARED](#USERS_CANVASSTEP_PROGRESSION_SHARED) | Lorsqu'un utilisateur passe à une étape du canvas
[USERS_CANVAS_CONVERSION_SHARED](#USERS_CANVAS_CONVERSION_SHARED) | Lorsqu'un utilisateur effectue une conversion dans le cadre d'un événement de conversion Canvas
[USERS_CANVAS_ENTRY_SHARED](#USERS_CANVAS_ENTRY_SHARED) | Lorsqu'un utilisateur entre dans un Canvas
[USERS_CANVAS_EXIT_MATCHEDAUDIENCE_SHARED](#USERS_CANVAS_EXIT_MATCHEDAUDIENCE_SHARED) | Lorsqu'un utilisateur quitte un canvas parce qu'il correspond aux critères de sortie de l'audience
[USERS_CANVAS_EXIT_PERFORMEDEVENT_SHARED](#USERS_CANVAS_EXIT_PERFORMEDEVENT_SHARED) | Lorsqu'un utilisateur quitte un canvas parce qu'il a effectué un événement d'exception
[USERS_CANVAS_EXPERIMENTSTEP_CONVERSION_SHARED](#USERS_CANVAS_EXPERIMENTSTEP_CONVERSION_SHARED) | Lorsqu'un utilisateur se convertit pour une étape de l'expérience Canvas
[USERS_CANVAS_EXPERIMENTSTEP_SPLITENTRY_SHARED](#USERS_CANVAS_EXPERIMENTSTEP_SPLITENTRY_SHARED) | Lorsqu'un utilisateur entre dans un chemin des chemins d'expérience
[USERS_CANVAS_FREQUENCYCAP_SHARED](#USERS_CANVAS_FREQUENCYCAP_SHARED) | Lorsqu'un utilisateur se voit imposer une limite de fréquence pour une étape du canvas
[USERS_CANVAS_REVENUE_SHARED](#USERS_CANVAS_REVENUE_SHARED) | Lorsqu'un utilisateur génère des chiffres d'affaires au cours de la période de l'événement de conversion principal.
[USERS_MESSAGES_CONTENTCARD_ABORT_SHARED](#USERS_MESSAGES_CONTENTCARD_ABORT_SHARED) | Un message de carte de contenu initialement planifié a été annulé pour une raison quelconque.
[USERS_MESSAGES_CONTENTCARD_CLICK_SHARED](#USERS_MESSAGES_CONTENTCARD_CLICK_SHARED) | Lorsqu'un utilisateur clique sur une carte de contenu
[USERS_MESSAGES_CONTENTCARD_DISMISS_SHARED](#USERS_MESSAGES_CONTENTCARD_DISMISS_SHARED) | Lorsqu'un utilisateur ferme une carte de contenu
[USERS_MESSAGES_CONTENTCARD_IMPRESSION_SHARED](#USERS_MESSAGES_CONTENTCARD_IMPRESSION_SHARED) | Lorsqu'un utilisateur consulte une carte de contenu
[USERS_MESSAGES_CONTENTCARD_SEND_SHARED](#USERS_MESSAGES_CONTENTCARD_SEND_SHARED) | Lorsque nous envoyons une carte de contenu à un utilisateur
[USERS_MESSAGES_EMAIL_ABORT_SHARED](#USERS_MESSAGES_EMAIL_ABORT_SHARED) | Un message e-mail initialement planifié a été annulé pour une raison quelconque.
[USERS_MESSAGES_EMAIL_BOUNCE_SHARED](#USERS_MESSAGES_EMAIL_BOUNCE_SHARED) | Un fournisseur de services d'e-mailing a renvoyé un échec d'envoi définitif. Un échec d'envoi définitif signifie un échec de livrabilité définitif.
[USERS_MESSAGES_EMAIL_CLICK_SHARED](#USERS_MESSAGES_EMAIL_CLICK_SHARED) | Lorsqu'un utilisateur clique sur un lien dans un e-mail
[USERS_MESSAGES_EMAIL_DELIVERY_SHARED](#USERS_MESSAGES_EMAIL_DELIVERY_SHARED) | Lorsqu'un e-mail est délivré
[USERS_MESSAGES_EMAIL_MARKASSPAM_SHARED](#USERS_MESSAGES_EMAIL_MARKASSPAM_SHARED) | Lorsqu'un e-mail est marqué comme spam
[USERS_MESSAGES_EMAIL_OPEN_SHARED](#USERS_MESSAGES_EMAIL_OPEN_SHARED) | Lorsqu'un utilisateur ouvre un e-mail
[USERS_MESSAGES_EMAIL_SEND_SHARED](#USERS_MESSAGES_EMAIL_SEND_SHARED) | Lorsque nous envoyons un e-mail à un utilisateur
[USERS_MESSAGES_EMAIL_SOFTBOUNCE_SHARED](#USERS_MESSAGES_EMAIL_SOFTBOUNCE_SHARED) | Lorsqu'un e-mail échoue provisoirement d'envoi
[USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED](#USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED) | Lorsqu'un utilisateur se désabonne d'un e-mail
[USERS_MESSAGES_INAPPMESSAGE_ABORT_SHARED](#USERS_MESSAGES_INAPPMESSAGE_ABORT_SHARED) | Un message in-app initialement planifié a été annulé pour une raison quelconque.
[USERS_MESSAGES_INAPPMESSAGE_CLICK_SHARED](#USERS_MESSAGES_INAPPMESSAGE_CLICK_SHARED) | Lorsqu'un utilisateur clique sur un message in-app
[USERS_MESSAGES_INAPPMESSAGE_IMPRESSION_SHARED](#USERS_MESSAGES_INAPPMESSAGE_IMPRESSION_SHARED) | Lorsqu'un utilisateur consulte un message in-app
[USERS_MESSAGES_NEWSFEEDCARD_ABORT_SHARED](#USERS_MESSAGES_NEWSFEEDCARD_ABORT_SHARED) | Un message de carte fil d'actualité initialement planifié a été annulé pour une raison quelconque.
[USERS_MESSAGES_NEWSFEEDCARD_CLICK_SHARED](#USERS_MESSAGES_NEWSFEEDCARD_CLICK_SHARED) | Lorsqu'un utilisateur clique sur une carte de fil d'actualité
[USERS_MESSAGES_NEWSFEEDCARD_IMPRESSION_SHARED](#USERS_MESSAGES_NEWSFEEDCARD_IMPRESSION_SHARED) | Lorsqu'un utilisateur consulte une carte de fil d'actualité
[USERS_MESSAGES_PUSHNOTIFICATION_ABORT_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_ABORT_SHARED) | Un message de notification push initialement planifié a été interrompu pour une raison quelconque.
[USERS_MESSAGES_PUSHNOTIFICATION_BOUNCE_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_BOUNCE_SHARED) | Quand une notification push rebondit
[USERS_MESSAGES_PUSHNOTIFICATION_INFLUENCEDOPEN_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_INFLUENCEDOPEN_SHARED) | Lorsqu'un utilisateur ouvre l'application après avoir reçu une notification sans cliquer sur celle-ci
[USERS_MESSAGES_PUSHNOTIFICATION_IOSFOREGROUND_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_IOSFOREGROUND_SHARED) | Lorsqu'un utilisateur reçoit une notification push alors que l'app est ouverte.
[USERS_MESSAGES_PUSHNOTIFICATION_OPEN_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_OPEN_SHARED) | Lorsqu'un utilisateur ouvre une notification push ou clique sur un bouton de notification push (y compris un bouton CLOSE qui n'ouvre PAS l'appli). <br><br> Les boutons d'action push ont des résultats multiples. Les actions "Non", "Refus" et "Annulation" sont des "clics", et les actions "Accepter" sont des "ouvertures". Les deux sont conseillés dans ce tableau, mais on peut les distinguer dans la colonne **BUTTON_ACTION_TYPE** colonne. Par exemple, une requête peut être utilisée pour regrouper les données en fonction d'une adresse `BUTTON_ACTION_TYPE` qui n'est ni Non, ni Refus, ni Annulation.
[USERS_MESSAGES_PUSHNOTIFICATION_SEND_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_SEND_SHARED) | Lorsque nous envoyons une notification push à un utilisateur.
[USERS_MESSAGES_SMS_ABORT_SHARED](#USERS_MESSAGES_SMS_ABORT_SHARED) | Un message SMS initialement planifié a été annulé pour une raison quelconque.
[USERS_MESSAGES_SMS_CARRIERSEND_SHARED](#USERS_MESSAGES_SMS_CARRIERSEND_SHARED) | Lorsqu'un message SMS est envoyé à l'opérateur
[USERS_MESSAGES_SMS_DELIVERY_SHARED](#USERS_MESSAGES_SMS_DELIVERY_SHARED) | Lors de l'envoi d'un message SMS
[USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED](#USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED) | Lorsque Braze n'est pas en mesure d'envoyer le message SMS au fournisseur de services SMS
[USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED](#USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED) | Lorsqu'un message SMS est reçu d'un utilisateur
[USERS_MESSAGES_SMS_REJECTION_SHARED](#USERS_MESSAGES_SMS_REJECTION_SHARED) | Lorsqu'un message SMS n'est pas envoyé à un utilisateur
[USERS_MESSAGES_SMS_SEND_SHARED](#USERS_MESSAGES_SMS_SEND_SHARED) | Lors de l'envoi d'un message SMS
[USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED](#USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED) | Lorsqu'un utilisateur clique sur une URL raccourcie de Braze incluse dans un message SMS
[USERS_MESSAGES_WEBHOOK_ABORT_SHARED](#USERS_MESSAGES_WEBHOOK_ABORT_SHARED) | Un message webhook initialement planifié a été annulé pour une raison quelconque.
[USERS_MESSAGES_WEBHOOK_SEND_SHARED](#USERS_MESSAGES_WEBHOOK_SEND_SHARED) | Lorsque nous envoyons un webhook pour un utilisateur
[USERS_MESSAGES_WHATSAPP_ABORT_SHARED](#USERS_MESSAGES_WHATSAPP_ABORT_SHARED) | Un message WhatsApp initialement planifié a été annulé pour une raison quelconque.
[USERS_MESSAGES_WHATSAPP_DELIVERY_SHARED](#USERS_MESSAGES_WHATSAPP_DELIVERY_SHARED) |Lors de l'envoi d'un message WhatsApp
[USERS_MESSAGES_WHATSAPP_FAILURE_SHARED](#USERS_MESSAGES_WHATSAPP_FAILURE_SHARED) | Lorsqu'un message WhatsApp n'est pas envoyé à un utilisateur
[USERS_MESSAGES_WHATSAPP_INBOUNDRECEIVE_SHARED](#USERS_MESSAGES_WHATSAPP_INBOUNDRECEIVE_SHARED) | Lorsqu'un message WhatsApp est reçu d'un utilisateur
[USERS_MESSAGES_WHATSAPP_READ_SHARED](#USERS_MESSAGES_WHATSAPP_READ_SHARED) | Lorsqu'un utilisateur ouvre un message WhatsApp
[USERS_MESSAGES_WHATSAPP_SEND_SHARED](#USERS_MESSAGES_WHATSAPP_SEND_SHARED) | Lorsque nous envoyons un message WhatsApp pour un utilisateur
[USERS_RANDOMBUCKETNUMBERUPDATE_SHARED](#USERS_RANDOMBUCKETNUMBERUPDATE_SHARED) | Lorsque le numéro de compartiment aléatoire d'un utilisateur est modifié
[USERS_USERDELETEREQUEST_SHARED](#USERS_USERDELETEREQUEST_SHARED) | Lorsqu'un utilisateur est supprimé à la demande d'un client
[USERS_USERORPHAN_SHARED](#USERS_USERORPHAN_SHARED) | Lorsqu'un utilisateur est fusionné avec le profil d'un autre utilisateur et que le profil d'origine est orphelin


## Comportements

### USERS_BEHAVIORS_CUSTOMEVENT_SHARED {#USERS_BEHAVIORS_CUSTOMEVENT_SHARED}

Champ d'application | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé l'événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`app_api_id` | `null,` `string` | ID API de l'application sur laquelle cette action s'est produite
`time` | `int` | Horodatage Unix auquel l'utilisateur a effectué l'événement
`gender` | `null,` `string` | [Sexe de l'utilisateur
`country` | `null,` `string` | [Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [Langue de l'utilisateur
`device_id` | `null,` `string` | ID de l'appareil sur lequel l'événement personnalisé s'est produit
`sdk_version` | `null,` `string` | Version du SDK de Braze utilisée lors de l'événement
`platform` | `null,` `string` | Plate-forme de l'appareil
`os_version` | `null,` `string` | Version du système d'exploitation de l'appareil
`device_model` | `null,` `string` | Modèle de l'appareil
`name` | `string` | Nom de l'événement personnalisé
`properties` | `string` | Propriétés personnalisées de l'événement stockées sous la forme d'une chaîne de caractères codée en JSON.
`ad_id` | `null,` `string` | [Identifiant publicitaire
`ad_id_type` | `null,` `string` | Un des éléments suivants : `ios_idfa`, `google_ad_id`, `windows_ad_id`, OR `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Si le suivi publicitaire est activé pour l'appareil.
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_INSTALLATTRIBUTION_SHARED {#USERS_BEHAVIORS_INSTALLATTRIBUTION_SHARED}

Champ d'application | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a procédé à l'installation
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`device_id` | `null,` `string` | `device_id` qui est liée à cet utilisateur si l'utilisateur est anonyme
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`time` | `int` | Date Unix à laquelle l'utilisateur a procédé à l'installation
`source` | `string` | la source de l'attribution
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_LOCATION_SHARED {#USERS_BEHAVIORS_LOCATION_SHARED}

Champ d'application | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui enregistre l'emplacement/localisation
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`app_api_id` | `null,` `string` | ID API de l'app sur laquelle cet emplacement/localisation a été enregistré.
`time` | `int` | Horodatage Unix auquel l'emplacement/localisation a été enregistré
`latitude` | `float` | [PII] Latitude de l'emplacement/localisation enregistré
`longitude` | `float` | [IIP] Longitude de l'emplacement/localisation enregistré
`altitude` | `null, float` | [PII] altitude de l'emplacement/localisation enregistré
`ll_accuracy` | `null, float` | la précision de la latitude et de la longitude de l'emplacement/localisation enregistré
`alt_accuracy` | `null, float` | la précision de l'altitude de l'emplacement/localisation enregistré
`device_id` | `null,` `string` | ID de l'appareil sur lequel l'emplacement/localisation a été enregistré
`sdk_version` | `null,` `string` | Version du SDK de Braze utilisée lors de l'enregistrement de l'emplacement/localisation.
`platform` | `null,` `string` | Plate-forme de l'appareil
`os_version` | `null,` `string` | Version du système d'exploitation de l'appareil
`device_model` | `null,` `string` | Modèle de l'appareil
`ad_id` | `null,` `string` | [Identifiant publicitaire
`ad_id_type` | `null,` `string` | Un des éléments suivants : `ios_idfa`, `google_ad_id`, `windows_ad_id`, OR `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Si le suivi publicitaire est activé pour l'appareil.
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_PURCHASE_SHARED {#USERS_BEHAVIORS_PURCHASE_SHARED}

Champ d'application | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a effectué un achat
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`app_api_id` | `null,` `string` | ID API de l'application sur laquelle l'achat a été effectué.
`time` | `int` | Horodatage Unix auquel l'utilisateur a effectué l'achat
`device_id` | `null,` `string` | ID de l'appareil sur lequel l'achat a été effectué
`sdk_version` | `null,` `string` | Version du SDK de Braze utilisée lors de l'achat
`platform` | `null,` `string` | Plate-forme de l'appareil
`os_version` | `null,` `string` | Version du système d'exploitation de l'appareil
`device_model` | `null,` `string` | Modèle de l'appareil
`product_id` | `string` | ID du produit acheté
`price` | `float` | Prix d'achat
`currency` | `string` | Monnaie d'achat
`properties` | `string` | Propriétés personnalisées de l'achat stockées sous la forme d'une chaîne de caractères codée en JSON.
`ad_id` | `null,` `string` | [Identifiant publicitaire
`ad_id_type` | `null,` `string` | Un des éléments suivants : `ios_idfa`, `google_ad_id`, `windows_ad_id`, OR `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Si le suivi publicitaire est activé pour l'appareil.
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_UNINSTALL_SHARED {#USERS_BEHAVIORS_UNINSTALL_SHARED}

Champ d'application | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a procédé à la désinstallation
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`device_id` | `null,` `string` | `device_id` qui est liée à cet utilisateur si l'utilisateur est anonyme
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`app_api_id` | `null,` `string` | ID API de l'application qui a été désinstallée
`time` | `int` | Date Unix de désinstallation par l'utilisateur
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_UPGRADEDAPP_SHARED {#USERS_BEHAVIORS_UPGRADEDAPP_SHARED}

Champ d'application | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a mis à jour l'application.
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`app_api_id` | `null,` `string` | ID API de l'application mise à niveau par l'utilisateur
`time` | `int` | Date Unix à laquelle l'utilisateur a mis à jour l'application
`device_id` | `null,` `string` | ID de l'appareil sur lequel l'utilisateur a mis à jour l'app.
`sdk_version` | `null,` `string` | Version du SDK de Braze utilisée
`platform` | `null,` `string` | Plate-forme de l'appareil
`os_version` | `null,` `string` | Version du système d'exploitation de l'appareil
`device_model` | `null,` `string` | Modèle de l'appareil
`old_app_version` | `null,` `string` | Ancienne version de l'application
`new_app_version` | `null,` `string` | Nouvelle version de l'application
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_APP_FIRSTSESSION_SHARED {#USERS_BEHAVIORS_APP_FIRSTSESSION_SHARED}

Champ d'application | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui effectue cette action
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`app_api_id` | `null,` `string` | ID API de l'application sur laquelle cette session s'est déroulée.
`time` | `int` | Horodatage Unix du début de la session
`session_id` | `string` | UUID de la session
`gender` | `null,` `string` | [Sexe de l'utilisateur
`country` | `null,` `string` | [Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [Langue de l'utilisateur
`device_id` | `null,` `string` | ID de l'appareil sur lequel la session a eu lieu
`sdk_version` | `null,` `string` | Version du SDK de Braze utilisée pendant la session
`platform` | `null,` `string` | Plate-forme de l'appareil
`os_version` | `null,` `string` | Version du système d'exploitation de l'appareil
`device_model` | `null,` `string` | Modèle de l'appareil
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_APP_NEWSFEEDIMPRESSION_SHARED {#USERS_BEHAVIORS_APP_NEWSFEEDIMPRESSION_SHARED}

Champ d'application | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a consulté le fil d'actualité.
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`app_api_id` | `null,` `string` | ID API de l'app sur laquelle l'utilisateur a consulté le fil d'actualité.
`time` | `int` | Horodatage Unix auquel l'utilisateur a consulté le fil d'actualité.
`device_id` | `null,` `string` | ID de l'appareil sur lequel l'impression a eu lieu
`sdk_version` | `null,` `string` | Version du SDK de Braze utilisée lors de l'impression
`platform` | `null,` `string` | Plate-forme de l'appareil
`os_version` | `null,` `string` | Version du système d'exploitation de l'appareil
`device_model` | `null,` `string` | Modèle de l'appareil
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_APP_SESSIONEND_SHARED {#USERS_BEHAVIORS_APP_SESSIONEND_SHARED}

Champ d'application | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui effectue cette action
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`app_api_id` | `null,` `string` | ID API de l'application sur laquelle cette session s'est déroulée.
`time` | `int` | Horodatage Unix auquel la session s'est terminée
`duration` | `null, float` | Durée de la session
`session_id` | `string` | UUID de la session
`device_id` | `null,` `string` | ID de l'appareil sur lequel la session a eu lieu
`sdk_version` | `null,` `string` | Version du SDK de Braze utilisée pendant la session
`platform` | `null,` `string` | Plate-forme de l'appareil
`os_version` | `null,` `string` | Version du système d'exploitation de l'appareil
`device_model` | `null,` `string` | Modèle de l'appareil
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_APP_SESSIONSTART_SHARED {#USERS_BEHAVIORS_APP_SESSIONSTART_SHARED}

Champ d'application | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui effectue cette action
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`app_api_id` | `null,` `string` | ID API de l'application sur laquelle cette session s'est déroulée.
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`time` | `int` | Horodatage Unix du début de la session
`session_id` | `string` | UUID de la session
`device_id` | `null,` `string` | ID de l'appareil sur lequel la session a eu lieu
`sdk_version` | `null,` `string` | Version du SDK de Braze utilisée pendant la session
`platform` | `null,` `string` | Plate-forme de l'appareil
`os_version` | `null,` `string` | Version du système d'exploitation de l'appareil
`device_model` | `null,` `string` | Modèle de l'appareil
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_GEOFENCE_DATAEVENT_SHARED {#USERS_BEHAVIORS_GEOFENCE_DATAEVENT_SHARED}

Champ d'application | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé l'événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`app_api_id` | `null,` `string` | ID API de l'application sur laquelle cette action s'est produite
`time` | `int` | Horodatage Unix auquel l'utilisateur a effectué l'événement
`device_id` | `null,` `string` | ID de l'appareil sur lequel l'événement personnalisé s'est produit
`sdk_version` | `null,` `string` | Version du SDK de Braze utilisée lors de l'événement
`platform` | `null,` `string` | Plate-forme de l'appareil
`os_version` | `null,` `string` | Version du système d'exploitation de l'appareil
`device_model` | `null,` `string` | Modèle de l'appareil
`event_type` | `string` | Quel type d'événement de géorepérage a été déclenché. (par exemple, "entrée" ou "sortie")
`location_set_id` | `string` | L'ID du jeu d'emplacements/localisation du géorepérage qui a été déclenché.
`geofence_id` | `string` | L'ID du géorepérage qui a été déclenché.
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_GEOFENCE_RECORDEVENT_SHARED {#USERS_BEHAVIORS_GEOFENCE_RECORDEVENT_SHARED}

Champ d'application | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé l'événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`app_api_id` | `null,` `string` | ID API de l'application sur laquelle cette action s'est produite
`time` | `int` | Horodatage Unix auquel l'utilisateur a effectué l'événement
`device_id` | `null,` `string` | ID de l'appareil sur lequel l'événement personnalisé s'est produit
`sdk_version` | `null,` `string` | Version du SDK de Braze utilisée lors de l'événement
`platform` | `null,` `string` | Plate-forme de l'appareil
`os_version` | `null,` `string` | Version du système d'exploitation de l'appareil
`device_model` | `null,` `string` | Modèle de l'appareil
`event_type` | `string` | Quel type d'événement de géorepérage a été déclenché. (par exemple, "entrée" ou "sortie")
`location_set_id` | `string` | L'ID du jeu d'emplacements/localisation du géorepérage qui a été déclenché.
`geofence_id` | `string` | L'ID du géorepérage qui a été déclenché.
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_SUBSCRIPTION_GLOBALSTATECHANGE_SHARED {#USERS_BEHAVIORS_SUBSCRIPTION_GLOBALSTATECHANGE_SHARED}

Champ d'application | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur concerné
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`email_address` | `null,` `string` | [DPI] adresse e-mail de l'utilisateur
`state_change_source` | `null,` `string` | source du changement d'état (REST, SDK, tableau de bord, etc.)
`subscription_status` | `string` | Statut de l'abonnement : Abonné" ou "Désabonné".
`channel` | `null,` `string` | Canal de l'état de l'abonnement global tel que l'e-mail
`time` | `int` | Horodatage Unix auquel l'état de l'abonnement a changé
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`app_api_id` | `null,` `string` | ID API de l'application à laquelle appartient l'événement
`campaign_id` | `null,` `string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle cet événement appartient
`message_variation_api_id` | `null,` `string` | ID API de la variation de message à laquelle cet événement appartient
`canvas_id` | `null,` `string` | ID de la Braze à usage interne de la toile à laquelle cet événement appartient
`canvas_api_id` | `null,` `string` | API ID de la toile à laquelle cet événement appartient
`canvas_variation_api_id` | `null,` `string` | ID API de la variation de Canvas à laquelle cet événement appartient
`canvas_step_api_id` | `null,` `string` | ID API de l'étape du canvas à laquelle cet événement appartient
`send_id` | `null,` `string` | ID d'envoi du message à l'origine de cette action de changement d'état de l'abonnement
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED {#USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED}

Champ d'application | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur concerné
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`device_id` | `null,` `string` | `device_id` qui est liée à cet utilisateur si l'utilisateur est anonyme
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`email_address` | `null,` `string` | [DPI] adresse e-mail de l'utilisateur
`phone_number` | `null,` `string` | [PII] numéro de téléphone de l'utilisateur au format e164
`app_api_id` | `null,` `string` | ID API de l'application à laquelle appartient l'événement
`campaign_id` | `null,` `string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle cet événement appartient
`message_variation_api_id` | `null,` `string` | ID API de la variation de message à laquelle cet événement appartient
`canvas_id` | `null,` `string` | ID de la Braze à usage interne de la toile à laquelle cet événement appartient
`canvas_api_id` | `null,` `string` | API ID de la toile à laquelle cet événement appartient
`canvas_variation_api_id` | `null,` `string` | ID API de la variation de Canvas à laquelle cet événement appartient
`canvas_step_api_id` | `null,` `string` | ID API de l'étape du canvas à laquelle cet événement appartient
`subscription_group_api_id` | `string` | Groupe d'abonnement API ID
`channel` | `null,` `string` | Canal : "e-mail" ou "sms", en fonction du type de canal du groupe d'abonnement.
`subscription_status` | `string` | Statut de l'abonnement : Abonné" ou "Désabonné".
`time` | `int` | Horodatage Unix auquel l'état de l'abonnement a changé
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`send_id` | `null,` `string` | ID d'envoi du message à l'origine de cette action de changement d'état de l'abonnement
`state_change_source` | `null,` `string` | Source du changement d'état (REST, SDK, tableau de bord, etc.)
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Campagnes

### USERS_CAMPAIGNS_CONVERSION_SHARED {#USERS_CAMPAIGNS_CONVERSION_SHARED}

Champ d'application | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`device_id` | `null,` `string` | `device_id` qui est liée à cet utilisateur si l'utilisateur est anonyme
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`time` | `int` | Horodatage Unix auquel l'événement s'est produit
`app_api_id` | `null,` `string` | ID API de l'application sur laquelle cet événement s'est produit.
`dispatch_id` | `null,` `string` | ID de l'envoi auquel ce message appartient
`send_id` | `null,` `string` | ID d'envoi du message auquel ce message appartient
`campaign_id` | `string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle cet événement appartient
`message_variation_api_id` | `null,` `string` | API ID de la variation du message reçu par cet utilisateur
`conversion_behavior_index` | `null, int` | Index du comportement de conversion
`gender` | `null,` `string` | [Sexe de l'utilisateur
`country` | `null,` `string` | [Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [Langue de l'utilisateur
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CAMPAIGNS_ENROLLINCONTROL_SHARED {#USERS_CAMPAIGNS_ENROLLINCONTROL_SHARED}

Champ d'application | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`device_id` | `null,` `string` | `device_id` qui est liée à cet utilisateur si l'utilisateur est anonyme
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`time` | `int` | Horodatage Unix auquel l'événement s'est produit
`app_api_id` | `null,` `string` | ID API de l'application sur laquelle cet événement s'est produit.
`dispatch_id` | `null,` `string` | ID de l'envoi auquel ce message appartient
`send_id` | `null,` `string` | ID d'envoi du message auquel ce message appartient
`campaign_id` | `string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle cet événement appartient
`message_variation_api_id` | `null,` `string` | API ID de la variation du message reçu par cet utilisateur
`gender` | `null,` `string` | [Sexe de l'utilisateur
`country` | `null,` `string` | [Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [Langue de l'utilisateur
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CAMPAIGNS_FREQUENCYCAP_SHARED {#USERS_CAMPAIGNS_FREQUENCYCAP_SHARED}

Champ d'application | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`device_id` | `null,` `string` | `device_id` qui est liée à cet utilisateur si l'utilisateur est anonyme
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`time` | `int` | Horodatage Unix auquel l'événement s'est produit
`dispatch_id` | `null,` `string` | ID de l'envoi auquel ce message appartient
`send_id` | `null,` `string` | ID d'envoi du message auquel ce message appartient
`campaign_id` | `string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle cet événement appartient
`message_variation_api_id` | `null,` `string` | API ID de la variation du message reçu par cet utilisateur
`channel` | `null,` `string` | Canal auquel appartient cet événement
`gender` | `null,` `string` | [Sexe de l'utilisateur
`country` | `null,` `string` | [Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [Langue de l'utilisateur
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CAMPAIGNS_REVENUE_SHARED {#USERS_CAMPAIGNS_REVENUE_SHARED}

Champ d'application | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`device_id` | `null,` `string` | `device_id` qui est liée à cet utilisateur si l'utilisateur est anonyme
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`time` | `int` | Horodatage Unix auquel l'événement s'est produit
`app_api_id` | `null,` `string` | ID API de l'application sur laquelle cet événement s'est produit.
`dispatch_id` | `null,` `string` | ID de l'envoi auquel ce message appartient
`send_id` | `null,` `string` | ID d'envoi du message auquel ce message appartient
`campaign_id` | `string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle cet événement appartient
`message_variation_api_id` | `null,` `string` | API ID de la variation du message reçu par cet utilisateur
`gender` | `null,` `string` | [Sexe de l'utilisateur
`country` | `null,` `string` | [Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [Langue de l'utilisateur
`revenue` | `long` | Le chiffre d'affaires d'USD en cents généré
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Canevas

### USERS_CANVASSTEP_PROGRESSION_SHARED {#USERS_CANVASSTEP_PROGRESSION_SHARED}

| Champ d'application                                  | Type                     | Description                                                                                                     |
| -------------------------------------- | ------------------------ | --------------------------------------------------------------------------------------------------------------- |
| `id`                                   | `string`, `null`    | ID unique au niveau mondial pour cet événement                                                                               |
| `user_id`                              | `string`, `null`    | ID Braze de l'utilisateur qui a réalisé cet événement                                                                   |
| `external_user_id`                     | `string`, `null`    | [PII] ID externe de l'utilisateur                                                                              |
| `device_id`                            | `string`, `null`    | ID de l'appareil lié à cet utilisateur, si l'utilisateur est anonyme                                            |
| `app_group_id`                         | `string`, `null`    | ID Braze de l'espace de travail auquel cet utilisateur appartient                                                                   |
| `app_group_api_id`                     | `string`, `null`    | ID API de l'espace de travail auquel appartient cet utilisateur                                                                    |
| `time`                                 | `int`, `null`       | Horodatage Unix auquel l'événement s'est produit                                                                      |
| `canvas_id`                            | `string`, `null`    | (Réservé à l'usage de Braze) ID de la toile à laquelle appartient cet événement                                                     |
| `canvas_api_id`                        | `string`, `null`    | API ID de la toile à laquelle cet événement appartient        |         
| `canvas_variation_api_id`              | `string`, `null`    | ID API de la variation de Canvas à laquelle cet événement appartient                                                            |
| `canvas_step_api_id`                   | `string`, `null`    | ID API de l'étape du canvas à laquelle cet événement appartient                                                                 |
| `progression_type`                     | `string`, `null`    | Type d'événement de progression d'étape |
| `is_canvas_entry`                      | `boolean`, `null`   | Qu'il s'agisse de l'entrée dans une première étape du canvas        |
| `exit_reason`                          | `string`, `null`    | S'il s'agit d'une sortie, la raison pour laquelle l'utilisateur a quitté la toile au cours de l'étape.                  |
| `canvas_entry_id`                      | `string`, `null`    | Identifiant unique pour cette instance d'un utilisateur dans un Canvas  |
| `next_step_id`                         | `string`, `null`    | BSON ID de l'étape du canvas suivante |
| `next_step_api_id`                     | `string`, `null`    | ID API de l'étape suivante du canvas |
| `sf_created_at`                        | `timestamp`, `null` | Lorsque cet événement a été repris par le Snowpipe                                                                   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_CONVERSION_SHARED {#USERS_CANVAS_CONVERSION_SHARED}

| Champ d'application                                  | Type                     | Description                                                                                                     |
| -------------------------------------- | ------------------------ | --------------------------------------------------------------------------------------------------------------- |
| `id`                                   | `string`, `null`    | ID unique au niveau mondial pour cet événement                                                                               |
| `user_id`                              | `string`, `null`    | ID Braze de l'utilisateur qui a réalisé cet événement                                                                   |
| `external_user_id`                     | `string`, `null`    | [PII] ID externe de l'utilisateur                                                                              |
| `device_id`                            | `string`, `null`    | ID de l'appareil lié à cet utilisateur, si l'utilisateur est anonyme                                            |
| `app_group_id`                         | `string`, `null`    | ID Braze de l'espace de travail auquel cet utilisateur appartient                                                                   |
| `app_group_api_id`                     | `string`, `null`    | ID API de l'espace de travail auquel appartient cet utilisateur                                                                    |
| `time`                                 | `int`, `null`       | Horodatage Unix auquel l'événement s'est produit                                                                      |
| `app_api_id`                           | `string`, `null`    | ID API de l'application sur laquelle cet événement s'est produit.                                                                  |
| `canvas_id`                            | `string`, `null`    | (Réservé à l'usage de Braze) ID de la toile à laquelle appartient cet événement                                                     |
| `canvas_api_id`                        | `string`, `null`    | API ID de la toile à laquelle cet événement appartient                                                                      |
| `canvas_variation_api_id`              | `string`, `null`    | ID API de la variation de Canvas à laquelle cet événement appartient                                                            |
| `canvas_step_api_id`                   | `string`, `null`    | ID API de l'étape du canvas à laquelle cet événement appartient                                                                 |
| `canvas_step_message_variation_api_id` | `string`, `null`    | ID API de la variation du message de l'étape canvas reçue par cet utilisateur.                                                  |
| `conversion_behavior_index`            | `int`, `null`       | Type d'événement de conversion effectué par l'utilisateur, où "0" correspond à une conversion principale et "1" à une conversion secondaire. |
| `gender`                               | `string`, `null`    | [Sexe de l'utilisateur                                                                                        |
| `country`                              | `string`, `null`    | [Pays de l'utilisateur                                                                                       |
| `timezone`                             | `string`, `null`    | Fuseau horaire de l'utilisateur                                                                                            |
| `language`                             | `string`, `null`    | [Langue de l'utilisateur                                                                                      |
| `sf_created_at`                        | `timestamp`, `null` | Lorsque cet événement a été repris par le Snowpipe                                                                   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_ENTRY_SHARED {#USERS_CANVAS_ENTRY_SHARED}

| Champ d'application                     | Type                     | Description                                                          |
| ------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                      | `string`, `null`    | ID unique au niveau mondial pour cet événement                                    |
| `user_id`                 | `string`, `null`    | ID Braze de l'utilisateur qui a réalisé cet événement                        |
| `external_user_id`        | `string`, `null`    | [PII] ID externe de l'utilisateur                                   |
| `device_id`               | `string`, `null`    | ID de l'appareil lié à cet utilisateur, si l'utilisateur est anonyme |
| `app_group_id`            | `string`, `null`    | ID Braze de l'espace de travail auquel cet utilisateur appartient                        |
| `app_group_api_id`        | `string`, `null`    | ID API de l'espace de travail auquel appartient cet utilisateur                         |
| `time`                    | `int`, `null`       | Horodatage Unix auquel l'événement s'est produit                           |
| `canvas_id`               | `string`, `null`    | (Réservé à l'usage de Braze) ID de la toile à laquelle appartient cet événement          |
| `canvas_api_id`           | `string`, `null`    | API ID de la toile à laquelle cet événement appartient                           |
| `canvas_variation_api_id` | `string`, `null`    | ID API de la variation de Canvas à laquelle cet événement appartient                 |
| `canvas_step_api_id`      | `string`, `null`    | [Obsolète] API ID de l'étape du canvas à laquelle cet événement appartient.         |
| `gender`                  | `string`, `null`    | [Sexe de l'utilisateur                                             |
| `country`                 | `string`, `null`    | [Pays de l'utilisateur                                            |
| `timezone`                | `string`, `null`    | Fuseau horaire de l'utilisateur                                                 |
| `language`                | `string`, `null`    | [Langue de l'utilisateur                                           |
| `in_control_group`        | `boolean`, `null`   | Vrai si l'utilisateur était inscrit dans le groupe de contrôle                   |
| `sf_created_at`           | `timestamp`, `null` | Lorsque cet événement a été repris par le Snowpipe                        |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_EXIT_MATCHEDAUDIENCE_SHARED {#USERS_CANVAS_EXIT_MATCHEDAUDIENCE_SHARED}

| Champ d'application                     | Type                     | Description                                                          |
| ------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                      | `string`, `null`    | ID unique au niveau mondial pour cet événement                                    |
| `user_id`                 | `string`, `null`    | ID Braze de l'utilisateur qui a réalisé cet événement                        |
| `external_user_id`        | `string`, `null`    | [PII] ID externe de l'utilisateur                                   |
| `device_id`               | `string`, `null`    | ID de l'appareil lié à cet utilisateur, si l'utilisateur est anonyme |
| `app_group_id`            | `string`, `null`    | ID Braze de l'espace de travail auquel cet utilisateur appartient                        |
| `app_group_api_id`        | `string`, `null`    | ID API de l'espace de travail auquel appartient cet utilisateur                         |
| `time`                    | `int`, `null`       | Horodatage Unix auquel l'événement s'est produit                           |
| `canvas_id`               | `string`, `null`    | (Réservé à l'usage de Braze) ID de la toile à laquelle appartient cet événement          |
| `canvas_api_id`           | `string`, `null`    | API ID de la toile à laquelle cet événement appartient                           |
| `canvas_variation_api_id` | `string`, `null`    | ID API de la variation de Canvas à laquelle cet événement appartient                 |
| `canvas_step_api_id`      | `string`, `null`    | ID API de l'étape du canvas à laquelle cet événement appartient                      |
| `sf_created_at`           | `timestamp`, `null` | Lorsque cet événement a été repris par le Snowpipe                        |

{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_EXIT_PERFORMEDEVENT_SHARED {#USERS_CANVAS_EXIT_PERFORMEDEVENT_SHARED}

| Champ d'application                     | Type                     | Description                                                          |
| ------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                      | `string`, `null`    | ID unique au niveau mondial pour cet événement                                    |
| `user_id`                 | `string`, `null`    | ID Braze de l'utilisateur qui a réalisé cet événement                        |
| `external_user_id`        | `string`, `null`    | [PII] ID externe de l'utilisateur                                   |
| `device_id`               | `string`, `null`    | ID de l'appareil lié à cet utilisateur, si l'utilisateur est anonyme |
| `app_group_id`            | `string`, `null`    | ID Braze de l'espace de travail auquel cet utilisateur appartient                        |
| `app_group_api_id`        | `string`, `null`    | ID API de l'espace de travail auquel appartient cet utilisateur                         |
| `time`                    | `int`, `null`       | Horodatage Unix auquel l'événement s'est produit                           |
| `canvas_id`               | `string`, `null`    | (Réservé à l'usage de Braze) ID de la toile à laquelle appartient cet événement          |
| `canvas_api_id`           | `string`, `null`    | API ID de la toile à laquelle cet événement appartient                           |
| `canvas_variation_api_id` | `string`, `null`    | ID API de la variation de Canvas à laquelle cet événement appartient                 |
| `canvas_step_api_id`      | `string`, `null`    | ID API de l'étape du canvas à laquelle cet événement appartient                      |
| `sf_created_at`           | `timestamp`, `null` | Lorsque cet événement a été repris par le Snowpipe                        |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_EXPERIMENTSTEP_CONVERSION_SHARED {#USERS_CANVAS_EXPERIMENTSTEP_CONVERSION_SHARED}

| Champ d'application                       | Type                     | Description                                                                                                     |
| --------------------------- | ------------------------ | --------------------------------------------------------------------------------------------------------------- |
| `id`                        | `string`, `null`    | ID unique au niveau mondial pour cet événement                                                                               |
| `user_id`                   | `string`, `null`    | ID Braze de l'utilisateur qui a réalisé cet événement                                                                   |
| `external_user_id`          | `string`, `null`    | [PII] ID externe de l'utilisateur                                                                              |
| `device_id`                 | `string`, `null`    | ID de l'appareil lié à cet utilisateur, si l'utilisateur est anonyme                                            |
| `app_group_id`              | `string`, `null`    | ID Braze de l'espace de travail auquel cet utilisateur appartient                                                                   |
| `time`                      | `int`, `null`       | Horodatage Unix auquel l'événement s'est produit                                                                      |
| `app_api_id`                | `string`, `null`    | ID API de l'application sur laquelle cet événement s'est produit.                                                                  |
| `canvas_id`                 | `string`, `null`    | (Réservé à l'usage de Braze) ID de la toile à laquelle appartient cet événement                                                     |
| `canvas_api_id`             | `string`, `null`    | API ID de la toile à laquelle cet événement appartient                                                                      |
| `canvas_variation_api_id`   | `string`, `null`    | ID API de la variation de Canvas à laquelle cet événement appartient                                                            |
| `canvas_step_api_id`        | `string`, `null`    | ID API de l'étape du canvas à laquelle cet événement appartient                                                                 |
| `experiment_step_api_id`    | `string`, `null`    | ID API de l'étape d'expérimentation à laquelle cet événement appartient                                                             |
| `conversion_behavior_index` | `int`, `null`       | Type d'événement de conversion effectué par l'utilisateur, où "0" correspond à une conversion principale et "1" à une conversion secondaire. |
| `sf_created_at`             | `timestamp`, `null` | Lorsque cet événement a été repris par le Snowpipe                                                                   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_EXPERIMENTSTEP_SPLITENTRY_SHARED {#USERS_CANVAS_EXPERIMENTSTEP_SPLITENTRY_SHARED}

| Champ d'application                     | Type                     | Description                                                          |
| ------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                      | `string`, `null`    | ID unique au niveau mondial pour cet événement                                    |
| `user_id`                 | `string`, `null`    | ID Braze de l'utilisateur qui a réalisé cet événement                        |
| `external_user_id`        | `string`, `null`    | [PII] ID externe de l'utilisateur                                   |
| `device_id`               | `string`, `null`    | ID de l'appareil lié à cet utilisateur, si l'utilisateur est anonyme |
| `app_group_id`            | `string`, `null`    | ID Braze de l'espace de travail auquel cet utilisateur appartient                        |
| `time`                    | `int`, `null`       | Horodatage Unix auquel l'événement s'est produit                           |
| `canvas_id`               | `string`, `null`    | (Réservé à l'usage de Braze) ID de la toile à laquelle appartient cet événement          |
| `canvas_api_id`           | `string`, `null`    | API ID de la toile à laquelle cet événement appartient                           |
| `canvas_variation_api_id` | `string`, `null`    | ID API de la variation de Canvas à laquelle cet événement appartient                 |
| `canvas_step_api_id`      | `string`, `null`    | ID API de l'étape du canvas à laquelle cet événement appartient                      |
| `experiment_step_api_id`  | `string`, `null`    | ID API de l'étape d'expérimentation à laquelle cet événement appartient                  |
| `in_control_group`        | `boolean`, `null`   | Vrai si l'utilisateur était inscrit dans le groupe de contrôle                   |
| `sf_created_at`           | `timestamp`, `null` | Lorsque cet événement a été repris par le Snowpipe                        |

{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_FREQUENCYCAP_SHARED {#USERS_CANVAS_FREQUENCYCAP_SHARED}

| Champ d'application                                  | Type                     | Description                                                          |
| -------------------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                                   | `string`, `null`    | ID unique au niveau mondial pour cet événement                                    |
| `user_id`                              | `string`, `null`    | ID Braze de l'utilisateur qui a réalisé cet événement                        |
| `external_user_id`                     | `string`, `null`    | [PII] ID externe de l'utilisateur                                   |
| `device_id`                            | `string`, `null`    | ID de l'appareil lié à cet utilisateur, si l'utilisateur est anonyme |
| `app_group_id`                         | `string`, `null`    | ID Braze de l'espace de travail auquel cet utilisateur appartient                        |
| `app_group_api_id`                     | `string`, `null`    | ID API de l'espace de travail auquel appartient cet utilisateur                         |
| `time`                                 | `int`, `null`       | Horodatage Unix auquel l'événement s'est produit                           |
| `canvas_id`                            | `string`, `null`    | (Réservé à l'usage de Braze) ID de la toile à laquelle appartient cet événement          |
| `canvas_api_id`                        | `string`, `null`    | API ID de la toile à laquelle cet événement appartient                           |
| `canvas_variation_api_id`              | `string`, `null`    | ID API de la variation de Canvas à laquelle cet événement appartient                 |
| `canvas_step_api_id`                   | `string`, `null`    | ID API de l'étape du canvas à laquelle cet événement appartient                      |
| `canvas_step_message_variation_api_id` | `string`, `null`    | ID API de la variation du message de l'étape canvas reçue par cet utilisateur.       |
| `channel`                              | `string`, `null`    | Canal de communication auquel cet événement appartient (e-mail, push, etc.)          |
| `gender`                               | `string`, `null`    | [Sexe de l'utilisateur                                             |
| `country`                              | `string`, `null`    | [Pays de l'utilisateur                                            |
| `timezone`                             | `string`, `null`    | Fuseau horaire de l'utilisateur                                                 |
| `language`                             | `string`, `null`    | [Langue de l'utilisateur                                           |
| `sf_created_at`                        | `timestamp`, `null` | Lorsque cet événement a été repris par le Snowpipe                        |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_REVENUE_SHARED {#USERS_CANVAS_REVENUE_SHARED}

| Champ d'application                                  | Type                     | Description                                                          |
| -------------------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                                   | `string`, `null`    | ID unique au niveau mondial pour cet événement                                    |
| `user_id`                              | `string`, `null`    | ID Braze de l'utilisateur qui a réalisé cet événement                        |
| `external_user_id`                     | `string`, `null`    | [PII] ID externe de l'utilisateur                                   |
| `device_id`                            | `string`, `null`    | ID de l'appareil lié à cet utilisateur, si l'utilisateur est anonyme |
| `app_group_id`                         | `string`, `null`    | ID Braze de l'espace de travail auquel cet utilisateur appartient                        |
| `app_group_api_id`                     | `string`, `null`    | ID API de l'espace de travail auquel appartient cet utilisateur                         |
| `time`                                 | `int`, `null`       | Horodatage Unix auquel l'événement s'est produit                           |
| `canvas_id`                            | `string`, `null`    | (Réservé à l'usage de Braze) ID de la toile à laquelle appartient cet événement          |
| `canvas_api_id`                        | `string`, `null`    | API ID de la toile à laquelle cet événement appartient                           |
| `canvas_variation_api_id`              | `string`, `null`    | ID API de la variation de Canvas à laquelle cet événement appartient                 |
| `canvas_step_api_id`                   | `string`, `null`    | ID API de l'étape du canvas à laquelle cet événement appartient                      |
| `canvas_step_message_variation_api_id` | `string`, `null`    | ID API de la variation du message de l'étape canvas reçue par cet utilisateur.       |
| `gender`                               | `string`, `null`    | [Sexe de l'utilisateur                                             |
| `country`                              | `string`, `null`    | [Pays de l'utilisateur                                            |
| `timezone`                             | `string`, `null`    | Fuseau horaire de l'utilisateur                                                 |
| `language`                             | `string`, `null`    | [Langue de l'utilisateur                                           |
| `revenue`                              | `int`, `null`       | Montant du chiffre d'affaires généré en USD, affiché en cents               |
| `sf_created_at`                        | `timestamp`, `null` | Lorsque cet événement a été repris par le Snowpipe                        |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Messages

### USERS_MESSAGES_CONTENTCARD_ABORT_SHARED {#USERS_MESSAGES_CONTENTCARD_ABORT_SHARED}

Champ d'application | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`device_id` | `null,` `string` | `device_id` qui est liée à cet utilisateur si l'utilisateur est anonyme
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`time` | `int` | Horodatage Unix auquel l'événement s'est produit
`dispatch_id` | `null,` `string` | ID de l'envoi auquel ce message appartient
`send_id` | `null,` `string` | ID d'envoi du message auquel ce message appartient
`campaign_id` | `null,` `string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle cet événement appartient
`message_variation_api_id` | `null,` `string` | API ID de la variation du message reçu par cet utilisateur
`canvas_id` | `null,` `string` | ID de la Braze à usage interne de la toile à laquelle cet événement appartient
`canvas_api_id` | `null,` `string` | API ID de la toile à laquelle cet événement appartient
`canvas_variation_api_id` | `null,` `string` | ID API de la variation de Canvas à laquelle cet événement appartient
`canvas_step_api_id` | `null,` `string` | ID API de l'étape du canvas à laquelle cet événement appartient
`canvas_step_message_variation_api_id` | `null,` `string` | ID API de la variation du message de l'étape canvas reçue par cet utilisateur.
`gender` | `null,` `string` | [Sexe de l'utilisateur
`country` | `null,` `string` | [Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [Langue de l'utilisateur
`abort_type` | `null,` `string` | Type d'abandon, l'un des suivants : `liquid_abort_message` ou `rate_limit`
`abort_log` | `null,` `string` | [PII] Message du journal décrivant les détails de l'abandon (maximum de 2 000 caractères)
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_CONTENTCARD_CLICK_SHARED {#USERS_MESSAGES_CONTENTCARD_CLICK_SHARED}

Champ d'application | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`content_card_id` | `string` | ID de la carte qui a généré cet événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`time` | `int` | Horodatage Unix auquel l'événement s'est produit
`app_api_id` | `null,` `string` | ID API de l'application sur laquelle cet événement s'est produit.
`dispatch_id` | `null,` `string` | ID de l'envoi auquel ce message appartient
`send_id` | `null,` `string` | ID d'envoi du message auquel ce message appartient
`campaign_id` | `null,` `string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle cet événement appartient
`message_variation_api_id` | `null,` `string` | API ID de la variation du message reçu par cet utilisateur
`canvas_id` | `null,` `string` | ID de la Braze à usage interne de la toile à laquelle cet événement appartient
`canvas_api_id` | `null,` `string` | API ID de la toile à laquelle cet événement appartient
`canvas_variation_api_id` | `null,` `string` | ID API de la variation de Canvas à laquelle cet événement appartient
`canvas_step_api_id` | `null,` `string` | ID API de l'étape du canvas à laquelle cet événement appartient
`canvas_step_message_variation_api_id` | `null,` `string` | ID API de la variation du message de l'étape canvas reçue par cet utilisateur.
`gender` | `null,` `string` | [Sexe de l'utilisateur
`country` | `null,` `string` | [Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [Langue de l'utilisateur
`device_id` | `null,` `string` | ID de l'appareil sur lequel l'événement s'est produit
`sdk_version` | `null,` `string` | Version du SDK de Braze utilisée lors de l'événement
`platform` | `null,` `string` | Plate-forme de l'appareil
`os_version` | `null,` `string` | Version du système d'exploitation de l'appareil
`device_model` | `null,` `string` | Modèle de l'appareil
`resolution` | `null,` `string` | Résolution de l'appareil
`carrier` | `null,` `string` | Porteuse de l'appareil
`browser` | `null,` `string` | Navigateur de l'appareil
`ad_id` | `null,` `string` | [Identifiant publicitaire
`ad_id_type` | `null,` `string` | Un des éléments suivants : `ios_idfa`, `google_ad_id`, `windows_ad_id`, OR `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Si le suivi publicitaire est activé pour l'appareil.
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_CONTENTCARD_DISMISS_SHARED {#USERS_MESSAGES_CONTENTCARD_DISMISS_SHARED}

Champ d'application | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`content_card_id` | `string` | ID de la carte qui a généré cet événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`time` | `int` | Horodatage Unix auquel l'événement s'est produit
`app_api_id` | `null,` `string` | ID API de l'application sur laquelle cet événement s'est produit.
`dispatch_id` | `null,` `string` | ID de l'envoi auquel ce message appartient
`send_id` | `null,` `string` | ID d'envoi du message auquel ce message appartient
`campaign_id` | `null,` `string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle cet événement appartient
`message_variation_api_id` | `null,` `string` | API ID de la variation du message reçu par cet utilisateur
`canvas_id` | `null,` `string` | ID de la Braze à usage interne de la toile à laquelle cet événement appartient
`canvas_api_id` | `null,` `string` | API ID de la toile à laquelle cet événement appartient
`canvas_variation_api_id` | `null,` `string` | ID API de la variation de Canvas à laquelle cet événement appartient
`canvas_step_api_id` | `null,` `string` | ID API de l'étape du canvas à laquelle cet événement appartient
`canvas_step_message_variation_api_id` | `null,` `string` | ID API de la variation du message de l'étape canvas reçue par cet utilisateur.
`gender` | `null,` `string` | [Sexe de l'utilisateur
`country` | `null,` `string` | [Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [Langue de l'utilisateur
`device_id` | `null,` `string` | ID de l'appareil sur lequel l'événement s'est produit
`sdk_version` | `null,` `string` | Version du SDK de Braze utilisée lors de l'événement
`platform` | `null,` `string` | Plate-forme de l'appareil
`os_version` | `null,` `string` | Version du système d'exploitation de l'appareil
`device_model` | `null,` `string` | Modèle de l'appareil
`resolution` | `null,` `string` | Résolution de l'appareil
`carrier` | `null,` `string` | Porteuse de l'appareil
`browser` | `null,` `string` | Navigateur de l'appareil
`ad_id` | `null,` `string` | [Identifiant publicitaire
`ad_id_type` | `null,` `string` | Un des éléments suivants : `ios_idfa`, `google_ad_id`, `windows_ad_id`, OR `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Si le suivi publicitaire est activé pour l'appareil.
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_CONTENTCARD_IMPRESSION_SHARED {#USERS_MESSAGES_CONTENTCARD_IMPRESSION_SHARED}

Champ d'application | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`content_card_id` | `string` | ID de la carte qui a généré cet événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`time` | `int` | Horodatage Unix auquel l'événement s'est produit
`app_api_id` | `null,` `string` | ID API de l'application sur laquelle cet événement s'est produit.
`dispatch_id` | `null,` `string` | ID de l'envoi auquel ce message appartient
`send_id` | `null,` `string` | ID d'envoi du message auquel ce message appartient
`campaign_id` | `null,` `string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle cet événement appartient
`message_variation_api_id` | `null,` `string` | API ID de la variation du message reçu par cet utilisateur
`canvas_id` | `null,` `string` | ID de la Braze à usage interne de la toile à laquelle cet événement appartient
`canvas_api_id` | `null,` `string` | API ID de la toile à laquelle cet événement appartient
`canvas_variation_api_id` | `null,` `string` | ID API de la variation de Canvas à laquelle cet événement appartient
`canvas_step_api_id` | `null,` `string` | ID API de l'étape du canvas à laquelle cet événement appartient
`canvas_step_message_variation_api_id` | `null,` `string` | ID API de la variation du message de l'étape canvas reçue par cet utilisateur.
`gender` | `null,` `string` | [Sexe de l'utilisateur
`country` | `null,` `string` | [Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [Langue de l'utilisateur
`device_id` | `null,` `string` | ID de l'appareil sur lequel l'événement s'est produit
`sdk_version` | `null,` `string` | Version du SDK de Braze utilisée lors de l'événement
`platform` | `null,` `string` | Plate-forme de l'appareil
`os_version` | `null,` `string` | Version du système d'exploitation de l'appareil
`device_model` | `null,` `string` | Modèle de l'appareil
`resolution` | `null,` `string` | Résolution de l'appareil
`carrier` | `null,` `string` | Porteuse de l'appareil
`browser` | `null,` `string` | Navigateur de l'appareil
`ad_id` | `null,` `string` | [Identifiant publicitaire
`ad_id_type` | `null,` `string` | Un des éléments suivants : `ios_idfa`, `google_ad_id`, `windows_ad_id`, OR `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Si le suivi publicitaire est activé pour l'appareil.
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_CONTENTCARD_SEND_SHARED {#USERS_MESSAGES_CONTENTCARD_SEND_SHARED}

Champ d'application | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`device_id` | `null,` `string` | `device_id` qui est liée à cet utilisateur si l'utilisateur est anonyme
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`time` | `int` | Horodatage Unix auquel l'événement s'est produit
`dispatch_id` | `null,` `string` | ID de l'envoi auquel ce message appartient
`send_id` | `null,` `string` | ID d'envoi du message auquel ce message appartient
`campaign_id` | `null,` `string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle cet événement appartient
`message_variation_api_id` | `null,` `string` | API ID de la variation du message reçu par cet utilisateur
`canvas_id` | `null,` `string` | ID de la Braze à usage interne de la toile à laquelle cet événement appartient
`canvas_api_id` | `null,` `string` | API ID de la toile à laquelle cet événement appartient
`canvas_variation_api_id` | `null,` `string` | ID API de la variation de Canvas à laquelle cet événement appartient
`canvas_step_api_id` | `null,` `string` | ID API de l'étape du canvas à laquelle cet événement appartient
`canvas_step_message_variation_api_id` | `null,` `string` | ID API de la variation du message de l'étape canvas reçue par cet utilisateur.
`gender` | `null,` `string` | [Sexe de l'utilisateur
`country` | `null,` `string` | [Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [Langue de l'utilisateur
`content_card_id` | `string` | ID de la carte qui a généré cet événement
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_ABORT_SHARED {#USERS_MESSAGES_EMAIL_ABORT_SHARED}

Champ d'application | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`device_id` | `null,` `string` | `device_id` qui est liée à cet utilisateur si l'utilisateur est anonyme
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`time` | `int` | Horodatage Unix auquel l'événement s'est produit
`dispatch_id` | `null,` `string` | ID de l'envoi auquel ce message appartient
`send_id` | `null,` `string` | ID d'envoi du message auquel ce message appartient
`campaign_id` | `null,` `string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle cet événement appartient
`message_variation_api_id` | `null,` `string` | API ID de la variation du message reçu par cet utilisateur
`canvas_id` | `null,` `string` | ID de la Braze à usage interne de la toile à laquelle cet événement appartient
`canvas_api_id` | `null,` `string` | API ID de la toile à laquelle cet événement appartient
`canvas_variation_api_id` | `null,` `string` | ID API de la variation de Canvas à laquelle cet événement appartient
`canvas_step_api_id` | `null,` `string` | ID API de l'étape du canvas à laquelle cet événement appartient
`canvas_step_message_variation_api_id` | `null,` `string` | ID API de la variation du message de l'étape canvas reçue par cet utilisateur.
`gender` | `null,` `string` | [Sexe de l'utilisateur
`country` | `null,` `string` | [Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [Langue de l'utilisateur
`email_address` | `string` | [DPI] adresse e-mail de l'utilisateur
`ip_pool` | `null,` `string` | Pool d'IP à partir duquel l'e-mail a été envoyé
`abort_type` | `null,` `string` | Type d'abandon, l'un des suivants : `liquid_abort_message` ou `rate_limit`
`abort_log` | `null,` `string` | [PII] Message du journal décrivant les détails de l'abandon (maximum de 2 000 caractères)
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_BOUNCE_SHARED {#USERS_MESSAGES_EMAIL_BOUNCE_SHARED}

Champ d'application | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`device_id` | `null,` `string` | `device_id` qui est liée à cet utilisateur si l'utilisateur est anonyme
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`time` | `int` | Horodatage Unix auquel l'événement s'est produit
`dispatch_id` | `null,` `string` | ID de l'envoi auquel ce message appartient
`send_id` | `null,` `string` | ID d'envoi du message auquel ce message appartient
`campaign_id` | `null,` `string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle cet événement appartient
`message_variation_api_id` | `null,` `string` | API ID de la variation du message reçu par cet utilisateur
`canvas_id` | `null,` `string` | ID de la Braze à usage interne de la toile à laquelle cet événement appartient
`canvas_api_id` | `null,` `string` | API ID de la toile à laquelle cet événement appartient
`canvas_variation_api_id` | `null,` `string` | ID API de la variation de Canvas à laquelle cet événement appartient
`canvas_step_api_id` | `null,` `string` | ID API de l'étape du canvas à laquelle cet événement appartient
`canvas_step_message_variation_api_id` | `null,` `string` | ID API de la variation du message de l'étape canvas reçue par cet utilisateur.
`gender` | `null,` `string` | [Sexe de l'utilisateur
`country` | `null,` `string` | [Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [Langue de l'utilisateur
`email_address` | `string` | [DPI] adresse e-mail de l'utilisateur
`sending_ip` | `null,` `string` | Adresse IP à partir de laquelle l'e-mail a été envoyé
`ip_pool` | `null,` `string` | Pool d'IP à partir duquel l'e-mail a été envoyé
`bounce_reason` | `null,` `string` | [IIP] Le code de raison SMTP et l'envoi du message convivial reçu pour cet événement de rebond.
`esp` | `null,` `string` | ESP lié à l'événement (SparkPost, SendGrid, ou Amazon SES)
`from_domain` | `null,` `string` | Domaine d'envoi de l'e-mail
`is_drop` | `null, boolean` | Indique que cet événement est considéré comme un événement de chute.
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_CLICK_SHARED {#USERS_MESSAGES_EMAIL_CLICK_SHARED}

Champ d'application | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`device_id` | `null,` `string` | `device_id` qui est liée à cet utilisateur si l'utilisateur est anonyme
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`time` | `int` | Horodatage Unix auquel l'événement s'est produit
`dispatch_id` | `null,` `string` | ID de l'envoi auquel ce message appartient
`send_id` | `null,` `string` | ID d'envoi du message auquel ce message appartient
`campaign_id` | `null,` `string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle cet événement appartient
`message_variation_api_id` | `null,` `string` | API ID de la variation du message reçu par cet utilisateur
`canvas_id` | `null,` `string` | ID de la Braze à usage interne de la toile à laquelle cet événement appartient
`canvas_api_id` | `null,` `string` | API ID de la toile à laquelle cet événement appartient
`canvas_variation_api_id` | `null,` `string` | ID API de la variation de Canvas à laquelle cet événement appartient
`canvas_step_api_id` | `null,` `string` | ID API de l'étape du canvas à laquelle cet événement appartient
`canvas_step_message_variation_api_id` | `null,` `string` | ID API de la variation du message de l'étape canvas reçue par cet utilisateur.
`gender` | `null,` `string` | [Sexe de l'utilisateur
`country` | `null,` `string` | [Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [Langue de l'utilisateur
`email_address` | `string` | [DPI] adresse e-mail de l'utilisateur
`url` | `null,` `string` | URL sur laquelle l'utilisateur a cliqué
`user_agent` | `null,` `string` | Agent utilisateur sur lequel le clic s'est produit
`ip_pool` | `null,` `string` | Pool d'IP à partir duquel l'e-mail a été envoyé
`link_id` | `null,` `string` | ID unique du lien sur lequel on a cliqué, tel que créé par Braze
`link_alias` | `null,` `string` | Alias associé à cet ID de lien
`esp` | `null,` `string` | ESP lié à l'événement (SparkPost, SendGrid, ou Amazon SES)
`from_domain` | `null,` `string` | Domaine d'envoi de l'e-mail
`is_amp` | `null, boolean` | Indique qu'il s'agit d'un événement AMP
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_DELIVERY_SHARED {#USERS_MESSAGES_EMAIL_DELIVERY_SHARED}

Champ d'application | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`device_id` | `null,` `string` | `device_id` qui est liée à cet utilisateur si l'utilisateur est anonyme
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`time` | `int` | Horodatage Unix auquel l'événement s'est produit
`dispatch_id` | `null,` `string` | ID de l'envoi auquel ce message appartient
`send_id` | `null,` `string` | ID d'envoi du message auquel ce message appartient
`campaign_id` | `null,` `string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle cet événement appartient
`message_variation_api_id` | `null,` `string` | API ID de la variation du message reçu par cet utilisateur
`canvas_id` | `null,` `string` | ID de la Braze à usage interne de la toile à laquelle cet événement appartient
`canvas_api_id` | `null,` `string` | API ID de la toile à laquelle cet événement appartient
`canvas_variation_api_id` | `null,` `string` | ID API de la variation de Canvas à laquelle cet événement appartient
`canvas_step_api_id` | `null,` `string` | ID API de l'étape du canvas à laquelle cet événement appartient
`canvas_step_message_variation_api_id` | `null,` `string` | ID API de la variation du message de l'étape canvas reçue par cet utilisateur.
`gender` | `null,` `string` | [Sexe de l'utilisateur
`country` | `null,` `string` | [Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [Langue de l'utilisateur
`email_address` | `string` | [DPI] adresse e-mail de l'utilisateur
`sending_ip` | `null,` `string` | Adresse IP à partir de laquelle l'e-mail a été envoyé
`ip_pool` | `null,` `string` | Pool d'IP à partir duquel l'e-mail a été envoyé
`esp` | `null,` `string` | ESP lié à l'événement (SparkPost, SendGrid, ou Amazon SES)
`from_domain` | `null,` `string` | Domaine d'envoi de l'e-mail
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_MARKASSPAM_SHARED {#USERS_MESSAGES_EMAIL_MARKASSPAM_SHARED}

Champ d'application | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`device_id` | `null,` `string` | `device_id` qui est liée à cet utilisateur si l'utilisateur est anonyme
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`time` | `int` | Horodatage Unix auquel l'événement s'est produit
`dispatch_id` | `null,` `string` | ID de l'envoi auquel ce message appartient
`send_id` | `null,` `string` | ID d'envoi du message auquel ce message appartient
`campaign_id` | `null,` `string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle cet événement appartient
`message_variation_api_id` | `null,` `string` | API ID de la variation du message reçu par cet utilisateur
`canvas_id` | `null,` `string` | ID de la Braze à usage interne de la toile à laquelle cet événement appartient
`canvas_api_id` | `null,` `string` | API ID de la toile à laquelle cet événement appartient
`canvas_variation_api_id` | `null,` `string` | ID API de la variation de Canvas à laquelle cet événement appartient
`canvas_step_api_id` | `null,` `string` | ID API de l'étape du canvas à laquelle cet événement appartient
`canvas_step_message_variation_api_id` | `null,` `string` | ID API de la variation du message de l'étape canvas reçue par cet utilisateur.
`gender` | `null,` `string` | [Sexe de l'utilisateur
`country` | `null,` `string` | [Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [Langue de l'utilisateur
`email_address` | `string` | [DPI] adresse e-mail de l'utilisateur
`user_agent` | `null,` `string` | Agent utilisateur sur lequel le signalement du courrier indésirable a eu lieu
`ip_pool` | `null,` `string` | Pool d'IP à partir duquel l'e-mail a été envoyé
`esp` | `null,` `string` | ESP lié à l'événement (SparkPost, SendGrid, ou Amazon SES)
`from_domain` | `null,` `string` | Domaine d'envoi de l'e-mail
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_OPEN_SHARED {#USERS_MESSAGES_EMAIL_OPEN_SHARED}

Champ d'application | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`device_id` | `null,` `string` | `device_id` qui est liée à cet utilisateur si l'utilisateur est anonyme
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`time` | `int` | Horodatage Unix auquel l'événement s'est produit
`dispatch_id` | `null,` `string` | ID de l'envoi auquel ce message appartient
`send_id` | `null,` `string` | ID d'envoi du message auquel ce message appartient
`campaign_id` | `null,` `string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle cet événement appartient
`message_variation_api_id` | `null,` `string` | API ID de la variation du message reçu par cet utilisateur
`canvas_id` | `null,` `string` | ID de la Braze à usage interne de la toile à laquelle cet événement appartient
`canvas_api_id` | `null,` `string` | API ID de la toile à laquelle cet événement appartient
`canvas_variation_api_id` | `null,` `string` | ID API de la variation de Canvas à laquelle cet événement appartient
`canvas_step_api_id` | `null,` `string` | ID API de l'étape du canvas à laquelle cet événement appartient
`canvas_step_message_variation_api_id` | `null,` `string` | ID API de la variation du message de l'étape canvas reçue par cet utilisateur.
`gender` | `null,` `string` | [Sexe de l'utilisateur
`country` | `null,` `string` | [Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [Langue de l'utilisateur
`email_address` | `string` | [DPI] adresse e-mail de l'utilisateur
`user_agent` | `null,` `string` | Agent utilisateur sur lequel l'ouverture s'est produite
`ip_pool` | `null,` `string` | Pool d'IP à partir duquel l'e-mail a été envoyé
`machine_open` | `null,` `string` | La valeur "true" est indiquée si l'événement d'ouverture est déclenché sans l'intervention de l'utilisateur, par exemple, par un appareil Apple sur lequel la protection de la confidentialité du courrier est activée. La valeur peut changer au fil du temps afin d'obtenir une plus grande granularité.
`esp` | `null,` `string` | ESP lié à l'événement (SparkPost, SendGrid, ou Amazon SES)
`from_domain` | `null,` `string` | Domaine d'envoi de l'e-mail
`is_amp` | `null, boolean` | Indique qu'il s'agit d'un événement AMP
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_SEND_SHARED {#USERS_MESSAGES_EMAIL_SEND_SHARED}

Champ d'application | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`device_id` | `null,` `string` | `device_id` qui est liée à cet utilisateur si l'utilisateur est anonyme
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`time` | `int` | Horodatage Unix auquel l'événement s'est produit
`dispatch_id` | `null,` `string` | ID de l'envoi auquel ce message appartient
`send_id` | `null,` `string` | ID d'envoi du message auquel ce message appartient
`campaign_id` | `null,` `string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle cet événement appartient
`message_variation_api_id` | `null,` `string` | API ID de la variation du message reçu par cet utilisateur
`canvas_id` | `null,` `string` | ID de la Braze à usage interne de la toile à laquelle cet événement appartient
`canvas_api_id` | `null,` `string` | API ID de la toile à laquelle cet événement appartient
`canvas_variation_api_id` | `null,` `string` | ID API de la variation de Canvas à laquelle cet événement appartient
`canvas_step_api_id` | `null,` `string` | ID API de l'étape du canvas à laquelle cet événement appartient
`canvas_step_message_variation_api_id` | `null,` `string` | ID API de la variation du message de l'étape canvas reçue par cet utilisateur.
`gender` | `null,` `string` | [Sexe de l'utilisateur
`country` | `null,` `string` | [Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [Langue de l'utilisateur
`email_address` | `string` | [DPI] adresse e-mail de l'utilisateur
`ip_pool` | `null,` `string` | Pool d'IP à partir duquel l'e-mail a été envoyé
`message_extras` | `null,` `string` | [Une chaîne JSON des paires clé-valeur balisées lors du rendu de Liquid.
`esp` | `null,` `string` | ESP lié à l'événement (SparkPost, SendGrid, ou Amazon SES)
`from_domain` | `null,` `string` | Domaine d'envoi de l'e-mail
`sf_created_at` | `timestamp`, `null` | Lorsque cet événement a été repris par le Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_SOFTBOUNCE_SHARED {#USERS_MESSAGES_EMAIL_SOFTBOUNCE_SHARED}

Champ d'application | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`device_id` | `null,` `string` | `device_id` qui est liée à cet utilisateur si l'utilisateur est anonyme
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`time` | `int` | Horodatage Unix auquel l'événement s'est produit
`dispatch_id` | `null,` `string` | ID de l'envoi auquel ce message appartient
`send_id` | `null,` `string` | ID d'envoi du message auquel ce message appartient
`campaign_id` | `null,` `string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle cet événement appartient
`message_variation_api_id` | `null,` `string` | API ID de la variation du message reçu par cet utilisateur
`canvas_id` | `null,` `string` | ID de la Braze à usage interne de la toile à laquelle cet événement appartient
`canvas_api_id` | `null,` `string` | API ID de la toile à laquelle cet événement appartient
`canvas_variation_api_id` | `null,` `string` | ID API de la variation de Canvas à laquelle cet événement appartient
`canvas_step_api_id` | `null,` `string` | ID API de l'étape du canvas à laquelle cet événement appartient
`canvas_step_message_variation_api_id` | `null,` `string` | ID API de la variation du message de l'étape canvas reçue par cet utilisateur.
`gender` | `null,` `string` | [Sexe de l'utilisateur
`country` | `null,` `string` | [Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [Langue de l'utilisateur
`email_address` | `string` | [DPI] adresse e-mail de l'utilisateur
`sending_ip` | `null,` `string` | Adresse IP à partir de laquelle l'e-mail a été envoyé
`ip_pool` | `null,` `string` | Pool d'IP à partir duquel l'e-mail a été envoyé
`bounce_reason` | `null,` `string` | [IIP] Le code de raison SMTP et l'envoi du message convivial reçu pour cet événement de rebond.
`esp` | `null,` `string` | ESP lié à l'événement (SparkPost, SendGrid, ou Amazon SES)
`from_domain` | `null,` `string` | Domaine d'envoi de l'e-mail
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED {#USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED}

Champ d'application | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`device_id` | `null,` `string` | `device_id` qui est liée à cet utilisateur si l'utilisateur est anonyme
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`time` | `int` | Horodatage Unix auquel l'événement s'est produit
`dispatch_id` | `null,` `string` | ID de l'envoi auquel ce message appartient
`send_id` | `null,` `string` | ID d'envoi du message auquel ce message appartient
`campaign_id` | `null,` `string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle cet événement appartient
`message_variation_api_id` | `null,` `string` | API ID de la variation du message reçu par cet utilisateur
`canvas_id` | `null,` `string` | ID de la Braze à usage interne de la toile à laquelle cet événement appartient
`canvas_api_id` | `null,` `string` | API ID de la toile à laquelle cet événement appartient
`canvas_variation_api_id` | `null,` `string` | ID API de la variation de Canvas à laquelle cet événement appartient
`canvas_step_api_id` | `null,` `string` | ID API de l'étape du canvas à laquelle cet événement appartient
`canvas_step_message_variation_api_id` | `null,` `string` | ID API de la variation du message de l'étape canvas reçue par cet utilisateur.
`gender` | `null,` `string` | [Sexe de l'utilisateur
`country` | `null,` `string` | [Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [Langue de l'utilisateur
`email_address` | `string` | [DPI] adresse e-mail de l'utilisateur
`ip_pool` | `null,` `string` | Pool d'IP à partir duquel l'e-mail a été envoyé
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_INAPPMESSAGE_ABORT_SHARED {#USERS_MESSAGES_INAPPMESSAGE_ABORT_SHARED}

Champ d'application | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`time` | `int` | Horodatage Unix auquel l'événement s'est produit
`app_api_id` | `null,` `string` | ID API de l'application sur laquelle cet événement s'est produit.
`card_api_id` | `null,` `string` | ID API de la carte
`dispatch_id` | `null,` `string` | ID de l'envoi auquel ce message appartient
`send_id` | `null,` `string` | ID d'envoi du message auquel ce message appartient
`campaign_id` | `null,` `string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle cet événement appartient
`message_variation_api_id` | `null,` `string` | API ID de la variation du message reçu par cet utilisateur
`canvas_id` | `null,` `string` | ID de la Braze à usage interne de la toile à laquelle cet événement appartient
`canvas_api_id` | `null,` `string` | API ID de la toile à laquelle cet événement appartient
`canvas_variation_api_id` | `null,` `string` | ID API de la variation de Canvas à laquelle cet événement appartient
`canvas_step_api_id` | `null,` `string` | ID API de l'étape du canvas à laquelle cet événement appartient
`canvas_step_message_variation_api_id` | `null,` `string` | ID API de la variation du message de l'étape canvas reçue par cet utilisateur.
`gender` | `null,` `string` | [Sexe de l'utilisateur
`country` | `null,` `string` | [Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [Langue de l'utilisateur
`device_id` | `null,` `string` | ID de l'appareil sur lequel l'événement s'est produit
`sdk_version` | `null,` `string` | Version du SDK de Braze utilisée lors de l'événement
`platform` | `null,` `string` | Plate-forme de l'appareil
`os_version` | `null,` `string` | Version du système d'exploitation de l'appareil
`device_model` | `null,` `string` | Modèle de l'appareil
`resolution` | `null,` `string` | Résolution de l'appareil
`carrier` | `null,` `string` | Porteuse de l'appareil
`browser` | `null,` `string` | Navigateur de l'appareil
`version` | `string` | Quelle version du message in-app, ancienne ou déclenchée ?
`ad_id` | `null,` `string` | [Identifiant publicitaire
`ad_id_type` | `null,` `string` | Un des éléments suivants : `ios_idfa`, `google_ad_id`, `windows_ad_id`, OR `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Si le suivi publicitaire est activé pour l'appareil.
`abort_type` | `null,` `string` | Type d'abandon, l'un des suivants : `liquid_abort_message` ou `rate_limit`
`abort_log` | `null,` `string` | [PII] Message du journal décrivant les détails de l'abandon (maximum de 2 000 caractères)
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_INAPPMESSAGE_CLICK_SHARED {#USERS_MESSAGES_INAPPMESSAGE_CLICK_SHARED}

Champ d'application | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`time` | `int` | Horodatage Unix auquel l'événement s'est produit
`app_api_id` | `null,` `string` | ID API de l'application sur laquelle cet événement s'est produit.
`card_api_id` | `null,` `string` | ID API de la carte
`dispatch_id` | `null,` `string` | ID de l'envoi auquel ce message appartient
`send_id` | `null,` `string` | ID d'envoi du message auquel ce message appartient
`campaign_id` | `null,` `string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle cet événement appartient
`message_variation_api_id` | `null,` `string` | API ID de la variation du message reçu par cet utilisateur
`canvas_id` | `null,` `string` | ID de la Braze à usage interne de la toile à laquelle cet événement appartient
`canvas_api_id` | `null,` `string` | API ID de la toile à laquelle cet événement appartient
`canvas_variation_api_id` | `null,` `string` | ID API de la variation de Canvas à laquelle cet événement appartient
`canvas_step_api_id` | `null,` `string` | ID API de l'étape du canvas à laquelle cet événement appartient
`canvas_step_message_variation_api_id` | `null,` `string` | ID API de la variation du message de l'étape canvas reçue par cet utilisateur.
`gender` | `null,` `string` | [Sexe de l'utilisateur
`country` | `null,` `string` | [Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [Langue de l'utilisateur
`device_id` | `null,` `string` | ID de l'appareil sur lequel l'événement s'est produit
`sdk_version` | `null,` `string` | Version du SDK de Braze utilisée lors de l'événement
`platform` | `null,` `string` | Plate-forme de l'appareil
`os_version` | `null,` `string` | Version du système d'exploitation de l'appareil
`device_model` | `null,` `string` | Modèle de l'appareil
`resolution` | `null,` `string` | résolution de l'appareil
`carrier` | `null,` `string` | porteur de l'appareil
`browser` | `null,` `string` | navigateur de l'appareil
`version` | `string` | Quelle version du message in-app, ancienne ou déclenchée ?
`button_id` | `null,` `string` | ID du bouton cliqué, si ce clic représente un clic sur un bouton
`ad_id` | `null,` `string` | [Identifiant publicitaire
`ad_id_type` | `null,` `string` | Un des éléments suivants : `ios_idfa`, `google_ad_id`, `windows_ad_id`, OR `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Si le suivi publicitaire est activé pour l'appareil.
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_INAPPMESSAGE_IMPRESSION_SHARED {#USERS_MESSAGES_INAPPMESSAGE_IMPRESSION_SHARED}

Champ d'application | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`time` | `int` | Horodatage Unix auquel l'événement s'est produit
`app_api_id` | `null,` `string` | ID API de l'application sur laquelle cet événement s'est produit.
`card_api_id` | `null,` `string` | ID API de la carte
`dispatch_id` | `null,` `string` | ID de l'envoi auquel ce message appartient
`send_id` | `null,` `string` | ID d'envoi du message auquel ce message appartient
`campaign_id` | `null,` `string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle cet événement appartient
`message_variation_api_id` | `null,` `string` | API ID de la variation du message reçu par cet utilisateur
`canvas_id` | `null,` `string` | ID de la Braze à usage interne de la toile à laquelle cet événement appartient
`canvas_api_id` | `null,` `string` | API ID de la toile à laquelle cet événement appartient
`canvas_variation_api_id` | `null,` `string` | ID API de la variation de Canvas à laquelle cet événement appartient
`canvas_step_api_id` | `null,` `string` | ID API de l'étape du canvas à laquelle cet événement appartient
`canvas_step_message_variation_api_id` | `null,` `string` | ID API de la variation du message de l'étape canvas reçue par cet utilisateur.
`gender` | `null,` `string` | [Sexe de l'utilisateur
`country` | `null,` `string` | [Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [Langue de l'utilisateur
`device_id` | `null,` `string` | ID de l'appareil sur lequel l'événement s'est produit
`sdk_version` | `null,` `string` | Version du SDK de Braze utilisée lors de l'événement
`platform` | `null,` `string` | Plate-forme de l'appareil
`os_version` | `null,` `string` | Version du système d'exploitation de l'appareil
`device_model` | `null,` `string` | Modèle de l'appareil
`resolution` | `null,` `string` | résolution de l'appareil
`carrier` | `null,` `string` | porteur de l'appareil
`browser` | `null,` `string` | navigateur de l'appareil
`version` | `string` | Quelle version du message in-app, ancienne ou déclenchée ?
`ad_id` | `null,` `string` | [Identifiant publicitaire
`ad_id_type` | `null,` `string` | Un des éléments suivants : `ios_idfa`, `google_ad_id`, `windows_ad_id`, OR `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Si le suivi publicitaire est activé pour l'appareil.
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_NEWSFEEDCARD_ABORT_SHARED {#USERS_MESSAGES_NEWSFEEDCARD_ABORT_SHARED}

Champ d'application | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`time` | `int` | Horodatage Unix auquel l'événement s'est produit
`app_api_id` | `null,` `string` | ID API de l'application sur laquelle cet événement s'est produit.
`card_api_id` | `null,` `string` | ID API de la carte
`gender` | `null,` `string` | [Sexe de l'utilisateur
`country` | `null,` `string` | [Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [Langue de l'utilisateur
`device_id` | `null,` `string` | ID de l'appareil sur lequel l'événement s'est produit
`sdk_version` | `null,` `string` | Version du SDK de Braze utilisée lors de l'événement
`platform` | `null,` `string` | Plate-forme de l'appareil
`os_version` | `null,` `string` | Version du système d'exploitation de l'appareil
`device_model` | `null,` `string` | Modèle de l'appareil
`resolution` | `null,` `string` | résolution de l'appareil
`carrier` | `null,` `string` | porteur de l'appareil
`browser` | `null,` `string` | navigateur de l'appareil
`abort_type` | `null,` `string` | Type d'abandon, l'un des suivants : `liquid_abort_message` ou `rate_limit`
`abort_log` | `null,` `string` | [PII] Message du journal décrivant les détails de l'abandon (maximum de 2 000 caractères)
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_NEWSFEEDCARD_CLICK_SHARED {#USERS_MESSAGES_NEWSFEEDCARD_CLICK_SHARED}

Champ d'application | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`time` | `int` | Horodatage Unix auquel l'événement s'est produit
`app_api_id` | `null,` `string` | ID API de l'application sur laquelle cet événement s'est produit.
`card_api_id` | `null,` `string` | ID API de la carte
`gender` | `null,` `string` | [Sexe de l'utilisateur
`country` | `null,` `string` | [Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [Langue de l'utilisateur
`device_id` | `null,` `string` | ID de l'appareil sur lequel l'événement s'est produit
`sdk_version` | `null,` `string` | Version du SDK de Braze utilisée lors de l'événement
`platform` | `null,` `string` | Plate-forme de l'appareil
`os_version` | `null,` `string` | Version du système d'exploitation de l'appareil
`device_model` | `null,` `string` | Modèle de l'appareil
`resolution` | `null,` `string` | résolution de l'appareil
`carrier` | `null,` `string` | porteur de l'appareil
`browser` | `null,` `string` | navigateur de l'appareil
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_NEWSFEEDCARD_IMPRESSION_SHARED {#USERS_MESSAGES_NEWSFEEDCARD_IMPRESSION_SHARED}

Champ d'application | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`time` | `int` | Horodatage Unix auquel l'événement s'est produit
`app_api_id` | `null,` `string` | ID API de l'application sur laquelle cet événement s'est produit.
`card_api_id` | `null,` `string` | ID API de la carte
`gender` | `null,` `string` | [Sexe de l'utilisateur
`country` | `null,` `string` | [Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [Langue de l'utilisateur
`device_id` | `null,` `string` | ID de l'appareil sur lequel l'événement s'est produit
`sdk_version` | `null,` `string` | Version du SDK de Braze utilisée lors de l'événement
`platform` | `null,` `string` | Plate-forme de l'appareil
`os_version` | `null,` `string` | Version du système d'exploitation de l'appareil
`device_model` | `null,` `string` | Modèle de l'appareil
`resolution` | `null,` `string` | résolution de l'appareil
`carrier` | `null,` `string` | porteur de l'appareil
`browser` | `null,` `string` | navigateur de l'appareil
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_PUSHNOTIFICATION_ABORT_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_ABORT_SHARED}

Champ d'application | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`device_id` | `null,` `string` | `device_id` que nous avons fait une tentative de réception/distribution pour
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`time` | `int` | Horodatage Unix auquel l'événement s'est produit
`app_api_id` | `null,` `string` | ID API de l'application sur laquelle cet événement s'est produit.
`dispatch_id` | `null,` `string` | ID de l'envoi auquel ce message appartient
`send_id` | `null,` `string` | ID d'envoi du message auquel ce message appartient
`campaign_id` | `null,` `string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle cet événement appartient
`message_variation_api_id` | `null,` `string` | API ID de la variation du message reçu par cet utilisateur
`canvas_id` | `null,` `string` | ID de la Braze à usage interne de la toile à laquelle cet événement appartient
`canvas_api_id` | `null,` `string` | API ID de la toile à laquelle cet événement appartient
`canvas_variation_api_id` | `null,` `string` | ID API de la variation de Canvas à laquelle cet événement appartient
`canvas_step_api_id` | `null,` `string` | ID API de l'étape du canvas à laquelle cet événement appartient
`canvas_step_message_variation_api_id` | `null,` `string` | ID API de la variation du message de l'étape canvas reçue par cet utilisateur.
`gender` | `null,` `string` | [Sexe de l'utilisateur
`country` | `null,` `string` | [Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [Langue de l'utilisateur
`platform` | `string` | Plate-forme de l'appareil
`abort_type` | `null,` `string` | Type d'abandon, l'un des suivants : `liquid_abort_message` ou `rate_limit`
`abort_log` | `null,` `string` | [PII] Message du journal décrivant les détails de l'abandon (maximum de 2 000 caractères)
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_PUSHNOTIFICATION_BOUNCE_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_BOUNCE_SHARED}

Champ d'application | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`push_token` | `null,` `string` | Jeton de poussée qui a rebondi
`device_id` | `null,` `string` | `device_id` qui a fait l'objet d'une tentative de réception/distribution et qui a été rejetée
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`time` | `int` | Horodatage Unix auquel l'événement s'est produit
`app_api_id` | `null,` `string` | ID API de l'application sur laquelle cet événement s'est produit.
`dispatch_id` | `null,` `string` | ID de l'envoi auquel ce message appartient
`send_id` | `null,` `string` | ID d'envoi du message auquel ce message appartient
`campaign_id` | `null,` `string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle cet événement appartient
`message_variation_api_id` | `null,` `string` | API ID de la variation du message reçu par cet utilisateur
`canvas_id` | `null,` `string` | ID de la Braze à usage interne de la toile à laquelle cet événement appartient
`canvas_api_id` | `null,` `string` | API ID de la toile à laquelle cet événement appartient
`canvas_variation_api_id` | `null,` `string` | ID API de la variation de Canvas à laquelle cet événement appartient
`canvas_step_api_id` | `null,` `string` | ID API de l'étape du canvas à laquelle cet événement appartient
`canvas_step_message_variation_api_id` | `null,` `string` | ID API de la variation du message de l'étape canvas reçue par cet utilisateur.
`gender` | `null,` `string` | [Sexe de l'utilisateur
`country` | `null,` `string` | [Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [Langue de l'utilisateur
`platform` | `null,` `string` | Plate-forme de l'appareil
`ad_id` | `null,` `string` | [PII] ID publicitaire de l'appareil pour lequel nous avons effectué une tentative de réception/distribution.
`ad_id_type` | `null,` `string` | Type d'ID publicitaire
`ad_tracking_enabled` | `null, boolean` | Si le suivi est activé ou non pour la publicité
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_PUSHNOTIFICATION_INFLUENCEDOPEN_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_INFLUENCEDOPEN_SHARED}

Champ d'application | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`time` | `int` | Horodatage Unix auquel l'événement s'est produit
`app_api_id` | `null,` `string` | ID API de l'application sur laquelle cet événement s'est produit.
`dispatch_id` | `null,` `string` | ID de l'envoi auquel ce message appartient
`send_id` | `null,` `string` | ID d'envoi du message auquel ce message appartient
`campaign_id` | `null,` `string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle cet événement appartient
`message_variation_api_id` | `null,` `string` | API ID de la variation du message reçu par cet utilisateur
`canvas_id` | `null,` `string` | ID de la Braze à usage interne de la toile à laquelle cet événement appartient
`canvas_api_id` | `null,` `string` | API ID de la toile à laquelle cet événement appartient
`canvas_variation_api_id` | `null,` `string` | ID API de la variation de Canvas à laquelle cet événement appartient
`canvas_step_api_id` | `null,` `string` | ID API de l'étape du canvas à laquelle cet événement appartient
`canvas_step_message_variation_api_id` | `null,` `string` | ID API de la variation du message de l'étape canvas reçue par cet utilisateur.
`gender` | `null,` `string` | [Sexe de l'utilisateur
`country` | `null,` `string` | [Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [Langue de l'utilisateur
`device_id` | `null,` `string` | ID de l'appareil sur lequel l'événement s'est produit
`sdk_version` | `null,` `string` | Version du SDK de Braze utilisée lors de l'événement
`platform` | `null,` `string` | Plate-forme de l'appareil
`os_version` | `null,` `string` | Version du système d'exploitation de l'appareil
`device_model` | `null,` `string` | Modèle de l'appareil
`resolution` | `null,` `string` | Résolution de l'appareil
`carrier` | `null,` `string` | Porteuse de l'appareil
`browser` | `null,` `string` | Navigateur de l'appareil
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_PUSHNOTIFICATION_IOSFOREGROUND_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_IOSFOREGROUND_SHARED}

Champ d'application | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`time` | `int` | Horodatage Unix auquel l'événement s'est produit
`app_api_id` | `null,` `string` | ID API de l'application sur laquelle cet événement s'est produit.
`dispatch_id` | `null,` `string` | ID de l'envoi auquel ce message appartient
`send_id` | `null,` `string` | ID d'envoi du message auquel ce message appartient
`campaign_id` | `null,` `string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle cet événement appartient
`message_variation_api_id` | `null,` `string` | API ID de la variation du message reçu par cet utilisateur
`canvas_id` | `null,` `string` | ID de la Braze à usage interne de la toile à laquelle cet événement appartient
`canvas_api_id` | `null,` `string` | API ID de la toile à laquelle cet événement appartient
`canvas_variation_api_id` | `null,` `string` | ID API de la variation de Canvas à laquelle cet événement appartient
`canvas_step_api_id` | `null,` `string` | ID API de l'étape du canvas à laquelle cet événement appartient
`canvas_step_message_variation_api_id` | `null,` `string` | ID API de la variation du message de l'étape canvas reçue par cet utilisateur.
`gender` | `null,` `string` | [Sexe de l'utilisateur
`country` | `null,` `string` | [Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [Langue de l'utilisateur
`device_id` | `null,` `string` | ID de l'appareil sur lequel l'événement s'est produit
`sdk_version` | `null,` `string` | Version du SDK de Braze utilisée lors de l'événement
`platform` | `null,` `string` | Plate-forme de l'appareil
`os_version` | `null,` `string` | Version du système d'exploitation de l'appareil
`device_model` | `null,` `string` | Modèle de l'appareil
`resolution` | `null,` `string` | Résolution de l'appareil
`carrier` | `null,` `string` | Porteuse de l'appareil
`browser` | `null,` `string` | Navigateur de l'appareil
`ad_id` | `null,` `string` | [PII] ID publicitaire de l'appareil pour lequel nous avons effectué une tentative de réception/distribution.
`ad_id_type` | `null,` `string` | Type d'ID publicitaire
`ad_tracking_enabled` | `null, boolean` | Si le suivi est activé ou non pour la publicité
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_PUSHNOTIFICATION_OPEN_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_OPEN_SHARED}

Champ d'application | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`time` | `int` | Horodatage Unix auquel l'événement s'est produit
`app_api_id` | `null,` `string` | ID API de l'application sur laquelle cet événement s'est produit.
`dispatch_id` | `null,` `string` | ID de l'envoi auquel ce message appartient
`send_id` | `null,` `string` | ID d'envoi du message auquel ce message appartient
`campaign_id` | `null,` `string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle cet événement appartient
`message_variation_api_id` | `null,` `string` | API ID de la variation du message reçu par cet utilisateur
`canvas_id` | `null,` `string` | ID de la Braze à usage interne de la toile à laquelle cet événement appartient
`canvas_api_id` | `null,` `string` | API ID de la toile à laquelle cet événement appartient
`canvas_variation_api_id` | `null,` `string` | ID API de la variation de Canvas à laquelle cet événement appartient
`canvas_step_api_id` | `null,` `string` | ID API de l'étape du canvas à laquelle cet événement appartient
`canvas_step_message_variation_api_id` | `null,` `string` | ID API de la variation du message de l'étape canvas reçue par cet utilisateur.
`gender` | `null,` `string` | [Sexe de l'utilisateur
`country` | `null,` `string` | [Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [Langue de l'utilisateur
`device_id` | `null,` `string` | ID de l'appareil sur lequel l'événement s'est produit
`sdk_version` | `null,` `string` | Version du SDK de Braze utilisée lors de l'événement
`platform` | `null,` `string` | Plate-forme de l'appareil
`os_version` | `null,` `string` | Version du système d'exploitation de l'appareil
`device_model` | `null,` `string` | Modèle de l'appareil
`resolution` | `null,` `string` | Résolution de l'appareil
`carrier` | `null,` `string` | Porteuse de l'appareil
`browser` | `null,` `string` | Navigateur de l'appareil
`button_string` | `null,` `string` | Identifiant (button_string) du bouton de notification push cliqué. null s'il ne s'agit pas d'un clic sur un bouton
`button_action_type` | `null,` `string` | Type d'action du bouton d'une notification push. L'un des éléments suivants : [URI, DEEP_LINK, NONE, CLOSE]. Nulle si elle ne provient pas d'un clic sur un bouton.
`slide_id` | `null,` `string` | Identifiant de la diapositive du carrousel sur laquelle l'utilisateur clique
`slide_action_type` | `null,` `string` | Type d'action de la diapositive du carrousel de poussée
`ad_id` | `null,` `string` | [PII] ID publicitaire de l'appareil pour lequel nous avons effectué une tentative de réception/distribution.
`ad_id_type` | `null,` `string` | Type d'ID publicitaire
`ad_tracking_enabled` | `null, boolean` | Si le suivi est activé ou non pour la publicité
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_PUSHNOTIFICATION_SEND_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_SEND_SHARED}

Champ d'application | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`push_token` | `null,` `string` | Jeton de poussée que nous avons fait une tentative de réception/distribution pour
`device_id` | `null,` `string` | `device_id` que nous avons fait une tentative de réception/distribution pour
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`time` | `int` | Horodatage Unix auquel l'événement s'est produit
`app_api_id` | `null,` `string` | ID API de l'application sur laquelle cet événement s'est produit.
`dispatch_id` | `null,` `string` | ID de l'envoi auquel ce message appartient
`send_id` | `null,` `string` | ID d'envoi du message auquel ce message appartient
`campaign_id` | `null,` `string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle cet événement appartient
`message_variation_api_id` | `null,` `string` | API ID de la variation du message reçu par cet utilisateur
`canvas_id` | `null,` `string` | ID de la Braze à usage interne de la toile à laquelle cet événement appartient
`canvas_api_id` | `null,` `string` | API ID de la toile à laquelle cet événement appartient
`canvas_variation_api_id` | `null,` `string` | ID API de la variation de Canvas à laquelle cet événement appartient
`canvas_step_api_id` | `null,` `string` | ID API de l'étape du canvas à laquelle cet événement appartient
`canvas_step_message_variation_api_id` | `null,` `string` | ID API de la variation du message de l'étape canvas reçue par cet utilisateur.
`gender` | `null,` `string` | [Sexe de l'utilisateur
`country` | `null,` `string` | [Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [Langue de l'utilisateur
`platform` | `string` | Plate-forme de l'appareil
`ad_id` | `null,` `string` | [PII] ID publicitaire de l'appareil pour lequel nous avons effectué une tentative de réception/distribution.
`ad_id_type` | `null,` `string` | Type d'ID publicitaire
`ad_tracking_enabled` | `null, boolean` | Si le suivi est activé ou non pour la publicité
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_ABORT_SHARED {#USERS_MESSAGES_SMS_ABORT_SHARED}

Champ d'application | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`time` | `int` | Horodatage Unix auquel l'événement s'est produit
`campaign_id` | `null,` `string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle cet événement appartient
`message_variation_api_id` | `null,` `string` | API ID de la variation du message reçu par cet utilisateur
`canvas_id` | `null,` `string` | ID de la Braze à usage interne de la toile à laquelle cet événement appartient
`canvas_api_id` | `null,` `string` | API ID de la toile à laquelle cet événement appartient
`canvas_variation_api_id` | `null,` `string` | ID API de la variation de Canvas à laquelle cet événement appartient
`canvas_step_api_id` | `null,` `string` | ID API de l'étape du canvas à laquelle cet événement appartient
`canvas_step_message_variation_api_id` | `null,` `string` | ID API de la variation du message de l'étape canvas reçue par cet utilisateur.
`subscription_group_api_id` | `null,` `string` | ID externe du groupe d'abonnement
`abort_type` | `null,` `string` | Type d'abandon, l'un des suivants : `liquid_abort_message` ou `rate_limit`
`abort_log` | `null,` `string` | [PII] Message du journal décrivant les détails de l'abandon (maximum de 2 000 caractères)
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_CARRIERSEND_SHARED {#USERS_MESSAGES_SMS_CARRIERSEND_SHARED}

Champ d'application | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`device_id` | `null,` `string` | `device_id` qui est liée à cet utilisateur si l'utilisateur est anonyme
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`time` | `int` | Horodatage Unix auquel l'événement s'est produit
`dispatch_id` | `null,` `string` | ID de l'envoi auquel ce message appartient
`send_id` | `null,` `string` | ID d'envoi du message auquel ce message appartient
`campaign_id` | `null,` `string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle cet événement appartient
`message_variation_api_id` | `null,` `string` | API ID de la variation du message reçu par cet utilisateur
`canvas_id` | `null,` `string` | ID de la Braze à usage interne de la toile à laquelle cet événement appartient
`canvas_api_id` | `null,` `string` | API ID de la toile à laquelle cet événement appartient
`canvas_variation_api_id` | `null,` `string` | ID API de la variation de Canvas à laquelle cet événement appartient
`canvas_step_api_id` | `null,` `string` | ID API de l'étape du canvas à laquelle cet événement appartient
`canvas_step_message_variation_api_id` | `null,` `string` | ID API de la variation du message de l'étape canvas reçue par cet utilisateur.
`gender` | `null,` `string` | [Sexe de l'utilisateur
`country` | `null,` `string` | [Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [Langue de l'utilisateur
`to_phone_number` | `null,` `string` | Numéro de téléphone [PII] du destinataire
`from_phone_number` | `null,` `string` | numéro de téléphone à partir duquel le message SMS a été envoyé
`subscription_group_api_id` | `null,` `string` | ID externe du groupe d'abonnement
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_DELIVERY_SHARED {#USERS_MESSAGES_SMS_DELIVERY_SHARED}

Champ d'application | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`device_id` | `null,` `string` | `device_id` qui est liée à cet utilisateur si l'utilisateur est anonyme
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`time` | `int` | Horodatage Unix auquel l'événement s'est produit
`dispatch_id` | `null,` `string` | ID de l'envoi auquel ce message appartient
`send_id` | `null,` `string` | ID d'envoi du message auquel ce message appartient
`campaign_id` | `null,` `string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle cet événement appartient
`message_variation_api_id` | `null,` `string` | API ID de la variation du message reçu par cet utilisateur
`canvas_id` | `null,` `string` | ID de la Braze à usage interne de la toile à laquelle cet événement appartient
`canvas_api_id` | `null,` `string` | API ID de la toile à laquelle cet événement appartient
`canvas_variation_api_id` | `null,` `string` | ID API de la variation de Canvas à laquelle cet événement appartient
`canvas_step_api_id` | `null,` `string` | ID API de l'étape du canvas à laquelle cet événement appartient
`canvas_step_message_variation_api_id` | `null,` `string` | ID API de la variation du message de l'étape canvas reçue par cet utilisateur.
`gender` | `null,` `string` | [Sexe de l'utilisateur
`country` | `null,` `string` | [Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [Langue de l'utilisateur
`to_phone_number` | `null,` `string` | Numéro de téléphone [PII] du destinataire
`from_phone_number` | `null,` `string` | Numéro de téléphone à partir duquel le message SMS a été envoyé
`subscription_group_api_id` | `null,` `string` | ID externe du groupe d'abonnement
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED {#USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED}

Champ d'application | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`device_id` | `null,` `string` | `device_id` qui est liée à cet utilisateur si l'utilisateur est anonyme
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`time` | `int` | Horodatage Unix auquel l'événement s'est produit
`dispatch_id` | `null,` `string` | ID de l'envoi auquel ce message appartient
`send_id` | `null,` `string` | ID d'envoi du message auquel ce message appartient
`campaign_id` | `null,` `string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle cet événement appartient
`message_variation_api_id` | `null,` `string` | API ID de la variation du message reçu par cet utilisateur
`canvas_id` | `null,` `string` | ID de la Braze à usage interne de la toile à laquelle cet événement appartient
`canvas_api_id` | `null,` `string` | API ID de la toile à laquelle cet événement appartient
`canvas_variation_api_id` | `null,` `string` | ID API de la variation de Canvas à laquelle cet événement appartient
`canvas_step_api_id` | `null,` `string` | ID API de l'étape du canvas à laquelle cet événement appartient
`canvas_step_message_variation_api_id` | `null,` `string` | ID API de la variation du message de l'étape canvas reçue par cet utilisateur.
`gender` | `null,` `string` | [Sexe de l'utilisateur
`country` | `null,` `string` | [Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [Langue de l'utilisateur
`to_phone_number` | `null,` `string` | Numéro de téléphone [PII] du destinataire
`subscription_group_api_id` | `null,` `string` | ID externe du groupe d'abonnement
`error` | `null,` `string` | nom de l'erreur
`provider_error_code` | `null,` `string` | code d'erreur du fournisseur de services SMS
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED {#USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED}

Champ d'application | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `null,` `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail associé au numéro de téléphone entrant.
`time` | `int` | Horodatage Unix auquel l'événement s'est produit
`user_phone_number` | `string` | [PII] le numéro de téléphone de l'utilisateur à partir duquel le message a été reçu
`subscription_group_id` | `null,` `string` | ID du groupe d'abonnement ciblé pour ce message SMS
`subscription_group_api_id` | `null,` `string` | API ID du groupe d'abonnement ciblé pour ce message SMS
`inbound_phone_number` | `string` | Le numéro d'appel entrant auquel le message a été envoyé
`action` | `string` | Action entreprise en réponse à ce message. Par exemple, `Subscribed`, `Unsubscribed`, ou `None`.
`message_body` | `string` | Réponse de l'utilisateur
`media_urls` | `null, {"type"=>"array", "items"=>["null", "string"]}` | URL des médias de l'utilisateur
`campaign_id` | `null,` `string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle cet événement appartient
`message_variation_api_id` | `null,` `string` | ID API de la variation de message à laquelle cet événement appartient
`canvas_id` | `null,` `string` | ID de la Braze à usage interne de la toile à laquelle cet événement appartient
`canvas_api_id` | `null,` `string` | API ID de la toile à laquelle cet événement appartient
`canvas_variation_api_id` | `null,` `string` | ID API de la variation de Canvas à laquelle cet événement appartient
`canvas_step_api_id` | `null,` `string` | ID API de l'étape du canvas à laquelle cet événement appartient
`canvas_step_message_variation_api_id` | `null,` `string` | ID API de la variation du message de l'étape du canvas à laquelle cet événement appartient.
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_REJECTION_SHARED {#USERS_MESSAGES_SMS_REJECTION_SHARED}

Champ d'application | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`device_id` | `null,` `string` | `device_id` qui est liée à cet utilisateur si l'utilisateur est anonyme
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`time` | `int` | Horodatage Unix auquel l'événement s'est produit
`dispatch_id` | `null,` `string` | ID de l'envoi auquel ce message appartient
`send_id` | `null,` `string` | ID d'envoi du message auquel ce message appartient
`campaign_id` | `null,` `string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle cet événement appartient
`message_variation_api_id` | `null,` `string` | API ID de la variation du message reçu par cet utilisateur
`canvas_id` | `null,` `string` | ID de la Braze à usage interne de la toile à laquelle cet événement appartient
`canvas_api_id` | `null,` `string` | API ID de la toile à laquelle cet événement appartient
`canvas_variation_api_id` | `null,` `string` | ID API de la variation de Canvas à laquelle cet événement appartient
`canvas_step_api_id` | `null,` `string` | ID API de l'étape du canvas à laquelle cet événement appartient
`canvas_step_message_variation_api_id` | `null,` `string` | ID API de la variation du message de l'étape canvas reçue par cet utilisateur.
`gender` | `null,` `string` | [Sexe de l'utilisateur
`country` | `null,` `string` | [Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [Langue de l'utilisateur
`to_phone_number` | `null,` `string` | Numéro de téléphone [PII] du destinataire
`from_phone_number` | `null,` `string` | numéro de téléphone à partir duquel le message SMS a été envoyé
`subscription_group_api_id` | `null,` `string` | ID externe du groupe d'abonnement
`error` | `null,` `string` | nom de l'erreur
`provider_error_code` | `null,` `string` | code d'erreur du fournisseur de services SMS
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_SEND_SHARED {#USERS_MESSAGES_SMS_SEND_SHARED}

Champ d'application | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`device_id` | `null,` `string` | `device_id` qui est liée à cet utilisateur si l'utilisateur est anonyme
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`time` | `int` | Horodatage Unix auquel l'événement s'est produit
`dispatch_id` | `null,` `string` | ID de l'envoi auquel ce message appartient
`send_id` | `null,` `string` | ID d'envoi du message auquel ce message appartient
`campaign_id` | `null,` `string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle cet événement appartient
`message_variation_api_id` | `null,` `string` | API ID de la variation du message reçu par cet utilisateur
`canvas_id` | `null,` `string` | ID de la Braze à usage interne de la toile à laquelle cet événement appartient
`canvas_api_id` | `null,` `string` | API ID de la toile à laquelle cet événement appartient
`canvas_variation_api_id` | `null,` `string` | ID API de la variation de Canvas à laquelle cet événement appartient
`canvas_step_api_id` | `null,` `string` | ID API de l'étape du canvas à laquelle cet événement appartient
`canvas_step_message_variation_api_id` | `null,` `string` | ID API de la variation du message de l'étape canvas reçue par cet utilisateur.
`gender` | `null,` `string` | [Sexe de l'utilisateur
`country` | `null,` `string` | [Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [Langue de l'utilisateur
`to_phone_number` | `null,` `string` | Numéro de téléphone [PII] du destinataire
`subscription_group_api_id` | `null,` `string` | ID externe du groupe d'abonnement
`category` | `null,` `string` | Nom de la catégorie de mots-clés, uniquement pour les messages de réponse automatique : Abonnement", "Désabonnement", "Aide" ou valeur personnalisée
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED {#USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED}

Champ d'application | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `null,` `string` | Braze ID de l'utilisateur ciblé par short_url, null si short_url n'a pas utilisé le suivi des clics de l'utilisateur
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur ciblé par short_url s'il existe, nul si short_url n'a pas utilisé le ciblage des clics de l'utilisateur.
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail utilisé pour la génération de short_url
`time` | `int` | Date Unix à laquelle short_url a été cliqué
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`campaign_id` | `null,` `string` | Braze ID de la campagne pour laquelle short_url a été généré, null s'il ne s'agit pas d'une campagne
`campaign_api_id` | `null,` `string` | API ID de la campagne pour laquelle short_url a été généré, null s'il ne s'agit pas d'une campagne.
`message_variation_api_id` | `null,` `string` | API ID de la variation de message pour laquelle short_url a été généré, null s'il ne s'agit pas d'une campagne.
`canvas_id` | `null,` `string` | Braze ID du Canvas pour lequel short_url a été généré, null s'il ne provient pas d'un Canvas
`canvas_api_id` | `null,` `string` | API ID du Canvas pour lequel short_url a été généré, null s'il ne s'agit pas d'un Canvas
`canvas_variation_api_id` | `null,` `string` | API ID de la variation du canvas pour lequel short_url a été généré, null s'il ne s'agit pas d'un canvas.
`canvas_step_api_id` | `null,` `string` | API ID de l'étape du canvas pour lequel short_url a été généré, null s'il ne s'agit pas d'un canvas.
`canvas_step_message_variation_api_id` | `null,` `string` | API ID de l'étape du canvas pour lequel le message de variation short_url a été généré, null s'il ne s'agit pas d'un canvas.
`url` | `string` | URL original contenu dans le message vers lequel est redirigé par short_url
`short_url` | `string` | URL raccourci qui a été cliqué
`user_agent` | `null,` `string` | agent utilisateur demandant short_url
`user_phone_number` | `string` | [PII] le numéro de téléphone de l'utilisateur
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WEBHOOK_ABORT_SHARED {#USERS_MESSAGES_WEBHOOK_ABORT_SHARED}

Champ d'application | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`device_id` | `null,` `string` | `device_id` qui est liée à cet utilisateur si l'utilisateur est anonyme
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`time` | `int` | Horodatage Unix auquel l'événement s'est produit
`dispatch_id` | `null,` `string` | ID de l'envoi auquel ce message appartient
`send_id` | `null,` `string` | ID d'envoi du message auquel ce message appartient
`campaign_id` | `null,` `string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle cet événement appartient
`message_variation_api_id` | `null,` `string` | API ID de la variation du message reçu par cet utilisateur
`canvas_id` | `null,` `string` | ID de la Braze à usage interne de la toile à laquelle cet événement appartient
`canvas_api_id` | `null,` `string` | API ID de la toile à laquelle cet événement appartient
`canvas_variation_api_id` | `null,` `string` | ID API de la variation de Canvas à laquelle cet événement appartient
`canvas_step_api_id` | `null,` `string` | ID API de l'étape du canvas à laquelle cet événement appartient
`canvas_step_message_variation_api_id` | `null,` `string` | ID API de la variation du message de l'étape canvas reçue par cet utilisateur.
`gender` | `null,` `string` | [Sexe de l'utilisateur
`country` | `null,` `string` | [Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [Langue de l'utilisateur
`abort_type` | `null,` `string` | Type d'abandon, l'un des suivants : `liquid_abort_message` ou `rate_limit`
`abort_log` | `null,` `string` | [PII] Message du journal décrivant les détails de l'abandon (maximum de 2 000 caractères)
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WEBHOOK_SEND_SHARED {#USERS_MESSAGES_WEBHOOK_SEND_SHARED}

Champ d'application | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`device_id` | `null,` `string` | `device_id` qui est liée à cet utilisateur si l'utilisateur est anonyme
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`time` | `int` | Horodatage Unix auquel l'événement s'est produit
`dispatch_id` | `null,` `string` | ID de l'envoi auquel ce message appartient
`send_id` | `null,` `string` | ID d'envoi du message auquel ce message appartient
`campaign_id` | `null,` `string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle cet événement appartient
`message_variation_api_id` | `null,` `string` | API ID de la variation du message reçu par cet utilisateur
`canvas_id` | `null,` `string` | ID de la Braze à usage interne de la toile à laquelle cet événement appartient
`canvas_api_id` | `null,` `string` | API ID de la toile à laquelle cet événement appartient
`canvas_variation_api_id` | `null,` `string` | ID API de la variation de Canvas à laquelle cet événement appartient
`canvas_step_api_id` | `null,` `string` | ID API de l'étape du canvas à laquelle cet événement appartient
`canvas_step_message_variation_api_id` | `null,` `string` | ID API de la variation du message de l'étape canvas reçue par cet utilisateur.
`gender` | `null,` `string` | [Sexe de l'utilisateur
`country` | `null,` `string` | [Pays de l'utilisateur
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`language` | `null,` `string` | [Langue de l'utilisateur
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WHATSAPP_ABORT_SHARED {#USERS_MESSAGES_WHATSAPP_ABORT_SHARED}

Champ d'application | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`time` | `int` | Horodatage Unix auquel l'événement s'est produit
`to_phone_number` | 	`null,` `string` | Numéro de téléphone [PII] du destinataire
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`device_id` | `null,` `string` | `device_id` qui est liée à cet utilisateur si l'utilisateur est anonyme
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`app_group_id` | `null,` `string` | ID de l'espace de travail auquel appartient cet utilisateur
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`subscription_group_api_id` | `string` | Groupe d'abonnement API ID
`campaign_id` | `null,` `string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle cet événement appartient
`message_variation_api_id` | `null,` `string` | API ID de la variation du message reçu par cet utilisateur
`canvas_id` | `null,` `string` | ID de la Braze à usage interne de la toile à laquelle cet événement appartient
`canvas_api_id` | `null,` `string` | API ID de la toile à laquelle cet événement appartient
`canvas_variation_api_id` | `null,` `string` | ID API de la variation de Canvas à laquelle cet événement appartient
`canvas_step_api_id` | `null,` `string` | ID API de l'étape du canvas à laquelle cet événement appartient
`canvas_step_message_variation_api_id` | `null,` `string` | ID API de la variation du message de l'étape canvas reçue par cet utilisateur.
`dispatch_id` | `null,` `string` | ID de l'envoi auquel ce message appartient
`abort_type` | `null,` `string` | Type d'abandon, l'un des suivants : `liquid_abort_message` ou `rate_limit`
`abort_log` | `null,` `string` | [PII] Message du journal décrivant les détails de l'abandon (maximum de 2 000 caractères)
`sf_created_at` | `timestamp`, `null` | Lorsque cet événement a été repris par le Snowpipe      
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WHATSAPP_DELIVERY_SHARED {#USERS_MESSAGES_WHATSAPP_DELIVERY_SHARED}

Champ d'application | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`time` | `int` | Horodatage Unix auquel l'événement s'est produit
`to_phone_number` | `null,` `string` | Numéro de téléphone [PII] du destinataire
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`device_id` | `null,` `string` | `device_id` qui est liée à cet utilisateur si l'utilisateur est anonyme
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`from_phone_number` | `null,` `string` | Numéro de téléphone à partir duquel le message WhatsApp a été envoyé.
`app_group_id` | `null,` `string` | ID de l'espace de travail auquel appartient cet utilisateur
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`subscription_group_api_id` | `string` | Groupe d'abonnement API ID
`campaign_id` | `null,` `string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle cet événement appartient
`message_variation_api_id` | `null,` `string` | API ID de la variation du message reçu par cet utilisateur
`canvas_id` | `null,` `string` | ID de la Braze à usage interne de la toile à laquelle cet événement appartient
`canvas_api_id` | `null,` `string` | API ID de la toile à laquelle cet événement appartient
`canvas_variation_api_id` | `null,` `string` | ID API de la variation de Canvas à laquelle cet événement appartient
`canvas_step_api_id` | `null,` `string` | ID API de l'étape du canvas à laquelle cet événement appartient
`canvas_step_message_variation_api_id` | `null,` `string` | ID API de la variation du message de l'étape canvas reçue par cet utilisateur.
`dispatch_id` | `null,` `string` | ID de l'envoi auquel ce message appartient
`sf_created_at` | `timestamp`, `null` | Lorsque cet événement a été repris par le Snowpipe      
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WHATSAPP_FAILURE_SHARED {#USERS_MESSAGES_WHATSAPP_FAILURE_SHARED}

Champ d'application | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`time` | `int` | Horodatage Unix auquel l'événement s'est produit
`to_phone_number` | `null,` `string` | Numéro de téléphone [PII] du destinataire
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`device_id` | `null,` `string` | `device_id` qui est liée à cet utilisateur si l'utilisateur est anonyme
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`from_phone_number` | `null,` `string` | Numéro de téléphone à partir duquel le message WhatsApp a été envoyé.
`app_group_id` | `null,` `string` | ID de l'espace de travail auquel appartient cet utilisateur
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`subscription_group_api_id` | `string` | Groupe d'abonnement API ID
`campaign_id` | `null,` `string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle cet événement appartient
`message_variation_api_id` | `null,` `string` | API ID de la variation du message reçu par cet utilisateur
`canvas_id` | `null,` `string` | ID de la Braze à usage interne de la toile à laquelle cet événement appartient
`canvas_api_id` | `null,` `string` | API ID de la toile à laquelle cet événement appartient
`canvas_variation_api_id` | `null,` `string` | ID API de la variation de Canvas à laquelle cet événement appartient
`canvas_step_api_id` | `null,` `string` | ID API de l'étape du canvas à laquelle cet événement appartient
`canvas_step_message_variation_api_id` | `null,` `string` | ID API de la variation du message de l'étape canvas reçue par cet utilisateur.
`dispatch_id` | `null,` `string` | ID de l'envoi auquel ce message appartient
`provider_error_code` | `null,` `string` | Code d'erreur de WhatsApp
`provider_error_title` | `null, ` `string` | Titre d'erreur de WhatsApp
`sf_created_at` | `timestamp`, `null` | Lorsque cet événement a été repris par le Snowpipe      
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WHATSAPP_INBOUNDRECEIVE_SHARED {#USERS_MESSAGES_WHATSAPP_INBOUNDRECEIVE_SHARED}

Champ d'application | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`time` | `int` | Horodatage Unix auquel l'événement s'est produit
`user_phone_number` | `string` | [PII] le numéro de téléphone de l'utilisateur à partir duquel le message a été reçu
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`inbound_phone_number` | `string` | Le numéro d'appel entrant auquel le message a été envoyé
`device_id` | `null,` `string` | `device_id` qui est liée à cet utilisateur si l'utilisateur est anonyme
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`app_group_id` | `null,` `string` | ID de l'espace de travail auquel appartient cet utilisateur
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`subscription_group_api_id` | `string` | Groupe d'abonnement API ID
`campaign_id` | `null,` `string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle cet événement appartient
`message_variation_api_id` | `null,` `string` | API ID de la variation du message reçu par cet utilisateur
`canvas_id` | `null,` `string` | ID de la Braze à usage interne de la toile à laquelle cet événement appartient
`canvas_api_id` | `null,` `string` | API ID de la toile à laquelle cet événement appartient
`canvas_variation_api_id` | `null,` `string` | ID API de la variation de Canvas à laquelle cet événement appartient
`canvas_step_api_id` | `null,` `string` | ID API de l'étape du canvas à laquelle cet événement appartient
`canvas_step_message_variation_api_id` | `null,` `string` | ID API de la variation du message de l'étape canvas reçue par cet utilisateur.
`message_body` | `string` | Réponse de l'utilisateur
`quick_reply_text` | `string` | Texte du bouton pressé par l'utilisateur
`media_urls` | `null, {"type"=>"array", "items"=>["null", "string"]}` | URL des médias de l'utilisateur
`action` | `string` | Action entreprise en réponse à ce message. Par exemple, `Subscribed`, `Unsubscribed`, ou `None`.
`sf_created_at` | `timestamp`, `null` | Lorsque cet événement a été repris par le Snowpipe      
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WHATSAPP_READ_SHARED {#USERS_MESSAGES_WHATSAPP_READ_SHARED}

Champ d'application | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`time` | `int` | Horodatage Unix auquel l'événement s'est produit
`to_phone_number` | `null,` `string` | Numéro de téléphone [PII] du destinataire
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`device_id` | `null,` `string` | `device_id` qui est liée à cet utilisateur si l'utilisateur est anonyme
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`from_phone_number` | `null,` `string` | Numéro de téléphone à partir duquel le message WhatsApp a été envoyé.
`app_group_id` | `null,` `string` | ID de l'espace de travail auquel appartient cet utilisateur
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`subscription_group_api_id` | `string` | Groupe d'abonnement API ID
`campaign_id` | `null,` `string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle cet événement appartient
`message_variation_api_id` | `null,` `string` | API ID de la variation du message reçu par cet utilisateur
`canvas_id` | `null,` `string` | ID de la Braze à usage interne de la toile à laquelle cet événement appartient
`canvas_api_id` | `null,` `string` | API ID de la toile à laquelle cet événement appartient
`canvas_variation_api_id` | `null,` `string` | ID API de la variation de Canvas à laquelle cet événement appartient
`canvas_step_api_id` | `null,` `string` | ID API de l'étape du canvas à laquelle cet événement appartient
`canvas_step_message_variation_api_id` | `null,` `string` | ID API de la variation du message de l'étape canvas reçue par cet utilisateur.
`dispatch_id` | `null,` `string` | ID de l'envoi auquel ce message appartient
`sf_created_at` | `timestamp`, `null` | Lorsque cet événement a été repris par le Snowpipe      
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WHATSAPP_SEND_SHARED {#USERS_MESSAGES_WHATSAPP_SEND_SHARED}

Champ d'application | Type | Description
------|------|------------
`id` | `string` | ID unique au niveau mondial pour cet événement
`time` | `int` | Horodatage Unix auquel l'événement s'est produit
`to_phone_number` | `null,` `string`	| Numéro de téléphone [PII] du destinataire
`user_id` | `string` | ID Braze de l'utilisateur qui a réalisé cet événement
`external_user_id` | `null,` `string` | [PII] ID externe de l'utilisateur
`device_id` | `null,` `string` | `device_id` qui est liée à cet utilisateur si l'utilisateur est anonyme
`timezone` | `null,` `string` | Fuseau horaire de l'utilisateur
`from_phone_number` | `null,` `string` | le numéro de téléphone à partir duquel le message WhatsApp a été envoyé
`app_group_id` | `null,` `string` | ID de l'espace de travail auquel appartient cet utilisateur
`app_group_api_id` | `null,` `string` | ID API de l'espace de travail auquel appartient cet utilisateur
`subscription_group_api_id` | `string` | Groupe d'abonnement API ID
`campaign_id` | `null,` `string` | ID Braze à usage interne de la campagne à laquelle cet événement appartient
`campaign_api_id` | `null,` `string` | ID API de la campagne à laquelle cet événement appartient
`message_variation_api_id` | `null,` `string` | API ID de la variation du message reçu par cet utilisateur
`canvas_id` | `null,` `string` | ID de la Braze à usage interne de la toile à laquelle cet événement appartient
`canvas_api_id` | `null,` `string` | API ID de la toile à laquelle cet événement appartient
`canvas_variation_api_id` | `null,` `string` | ID API de la variation de Canvas à laquelle cet événement appartient
`canvas_step_api_id` | `null,` `string` | ID API de l'étape du canvas à laquelle cet événement appartient
`canvas_step_message_variation_api_id` | `null,` `string` | ID API de la variation du message de l'étape canvas reçue par cet utilisateur.
`dispatch_id` | `null,` `string` | ID de l'envoi auquel ce message appartient
`message_extras` | `null,` `string` | [Une chaîne JSON des paires clé-valeur balisées lors du rendu de Liquid.
`sf_created_at` | `timestamp`, `null` | Lorsque cet événement a été repris par le Snowpipe      
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Utilisateurs

### USERS_RANDOMBUCKETNUMBERUPDATE_SHARED {#USERS_RANDOMBUCKETNUMBERUPDATE_SHARED}

| Champ d'application                       | Type                     | Description                                        |
| --------------------------- | ------------------------ | -------------------------------------------------- |
| `id`                        | `string`, `null`    | ID unique au niveau mondial pour cet événement                  |
| `app_group_id`              | `string`, `null`    | ID Braze de l'espace de travail auquel cet utilisateur appartient      |
| `app_group_api_id`          | `string`, `null`    | ID API de l'espace de travail auquel appartient cet utilisateur       |
| `user_id`                   | `string`, `null`    | ID Braze de l'utilisateur qui a réalisé cet événement      |
| `external_user_id`          | `string`, `null`    | [PII] ID externe de l'utilisateur                 |
| `time`                      | `int`, `null`       | Horodatage Unix auquel l'événement s'est produit         |
| `random_bucket_number`      | `int`, `null`       | Numéro de compartiment aléatoire actuel attribué à l'utilisateur  |
| `prev_random_bucket_number` | `int`, `null`       | Numéro de compartiment aléatoire précédent attribué à l'utilisateur |
| `sf_created_at`             | `timestamp`, `null` | Lorsque cet événement a été repris par le Snowpipe      |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_USERDELETEREQUEST_SHARED {#USERS_USERDELETEREQUEST_SHARED}

| Champ d'application              | Type                     | Description                                                   |
| ------------------ | ------------------------ | ------------------------------------------------------------- |
| `id`               | `string`, `null`    | ID unique au niveau mondial pour cet événement                             |
| `user_id`          | `string`, `null`    | ID Braze de l'utilisateur qui a été supprimé                          |
| `app_group_id`     | `string`, `null`    | ID Braze de l'espace de travail auquel cet utilisateur appartient                 |
| `app_group_api_id` | `string`, `null`    | ID API de l'espace de travail auquel appartient cet utilisateur                  |
| `time`             | `int`, `null`       | Date Unix à laquelle la demande de suppression de l'utilisateur a été traitée |
| `sf_created_at`    | `timestamp`, `null` | Lorsque cet événement a été repris par le Snowpipe                 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_USERORPHAN_SHARED {#USERS_USERORPHAN_SHARED}

| Champ d'application              | Type                     | Description                                                                   |
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
