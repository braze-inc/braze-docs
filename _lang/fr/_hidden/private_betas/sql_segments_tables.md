---
nav_title: "Tables Segment Extensions SQL"
permalink: "/sql_segments_tables/"
hidden: true
toc_headers: h2
---

<style>
table td {
   word-break: keep-all;
}
</style>

# Tables Segment Extensions SQL

Cette page est une référence des tables et des colonnes pouvant être interrogées lors de la génération des [Segment Extensions SQL]({{site.baseurl}}/sql_segments).

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
[USERS_BEHAVIORS_GEOFENCE_DATAEVENT_SHARED](#USERS_BEHAVIORS_GEOFENCE_DATAEVENT_SHARED) | Lorsqu’un utilisateur déclenche une zone de geofence (par exemple, lorsqu’il entre ou sort d’une geofence). Cet événement a été groupé avec d’autres événements et reçu par le biais de l’endpoint des événements standard, et peut donc ne pas avoir été reçu par l’endpoint en temps réel.
[USERS_BEHAVIORS_GEOFENCE_RECORDEVENT_SHARED](#USERS_BEHAVIORS_GEOFENCE_RECORDEVENT_SHARED) | Lorsqu’un utilisateur déclenche une zone de geofence (par exemple, lorsqu’il entre ou sort d’une geofence). Cet événement a été reçu par le biais de l’endpoint Geofence dédié, et est donc reçu en temps réel dès que l’appareil d’un utilisateur détecte qu’il a déclenché une geofence. <br><br>En outre, en raison de la limitation du taux sur l’endpoint geofence, il est possible que certains événements de geofence ne soient pas reflétés en tant que RecordEvent. Cependant, tous les événements de geofence sont représentés par DataEvent (mais avec potentiellement un certain retard dû au traitement par lots).
[USERS_BEHAVIORS_SUBSCRIPTION_GLOBALSTATECHANGE_SHARED](#USERS_BEHAVIORS_SUBSCRIPTION_GLOBALSTATECHANGE_SHARED) | Lorsqu’un utilisateur est abonné ou désabonné globalement d’un canal tel que l’e-mail
[USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED](#USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED) | Lorsqu’un utilisateur est abonné ou désabonné d’un groupe d’abonnement
[USERS_CAMPAIGNS_ABORT_SHARED](#USERS_CAMPAIGNS_ABORT_SHARED) | Un message de campagne initialement planifié a été abandonné pour une raison quelconque.
[USERS_CAMPAIGNS_CONVERSION_SHARED](#USERS_CAMPAIGNS_CONVERSION_SHARED) | Lorsqu’un utilisateur se convertit pour une campagne
[USERS_CAMPAIGNS_ENROLLINCONTROL_SHARED](#USERS_CAMPAIGNS_ENROLLINCONTROL_SHARED) | Lorsqu’un utilisateur est inscrit dans le groupe de contrôle d’une campagne
[USERS_CAMPAIGNS_FREQUENCYCAP_SHARED](#USERS_CAMPAIGNS_FREQUENCYCAP_SHARED) | Lorsqu’un utilisateur atteint une limite de fréquence pour une campagne
[USERS_CAMPAIGNS_REVENUE_SHARED](#USERS_CAMPAIGNS_REVENUE_SHARED) | Lorsqu’un utilisateur génère des revenus avec, au cours de la période de conversion principale
[USERS_MESSAGES_CONTENTCARD_ABORT_SHARED](#USERS_MESSAGES_CONTENTCARD_ABORT_SHARED) | Un message de carte de contenu initialement planifié a été abandonné pour une raison quelconque.
[USERS_MESSAGES_CONTENTCARD_CLICK_SHARED](#USERS_MESSAGES_CONTENTCARD_CLICK_SHARED) | Lorsqu’un utilisateur clique sur une carte de contenu
[USERS_MESSAGES_CONTENTCARD_DISMISS_SHARED](#USERS_MESSAGES_CONTENTCARD_DISMISS_SHARED) | Lorsqu’un utilisateur rejette une carte de contenu
[USERS_MESSAGES_CONTENTCARD_IMPRESSION_SHARED](#USERS_MESSAGES_CONTENTCARD_IMPRESSION_SHARED) | Lorsqu’un utilisateur affiche une carte de contenu
[USERS_MESSAGES_CONTENTCARD_SEND_SHARED](#USERS_MESSAGES_CONTENTCARD_SEND_SHARED) | Lorsque nous envoyons une carte de contenu à un utilisateur
[USERS_MESSAGES_EMAIL_ABORT_SHARED](#USERS_MESSAGES_EMAIL_ABORT_SHARED) | Un e-mail initialement planifié a été abandonné pour une raison quelconque.
[USERS_MESSAGES_EMAIL_BOUNCE_SHARED](#USERS_MESSAGES_EMAIL_BOUNCE_SHARED) | Un fournisseur de services de courrier électronique a renvoyé un hard bounce. Un hard bounce signifie un échec permanent de la délivrabilité.
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
[USERS_MESSAGES_PUSHNOTIFICATION_ABORT_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_ABORT_SHARED) | Un message de notification push initialement planifié a été abandonné pour une raison quelconque.
[USERS_MESSAGES_PUSHNOTIFICATION_BOUNCE_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_BOUNCE_SHARED) | Lorsqu’une notifications push rebondit
[USERS_MESSAGES_PUSHNOTIFICATION_INFLUENCEDOPEN_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_INFLUENCEDOPEN_SHARED) | Lorsqu’un utilisateur ouvre l’application après avoir reçu une notification sans cliquer sur elle
[USERS_MESSAGES_PUSHNOTIFICATION_IOSFOREGROUND_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_IOSFOREGROUND_SHARED) | Lorsqu’un utilisateur a reçu une notification push pendant que l’application était ouverte
[USERS_MESSAGES_PUSHNOTIFICATION_OPEN_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_OPEN_SHARED) | Lorsqu’un utilisateur ouvre une notification push ou clique sur un bouton de notification push (y compris un bouton FERMER qui n’ouvre PAS l’application)
[USERS_MESSAGES_PUSHNOTIFICATION_SEND_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_SEND_SHARED) | Lorsque nous envoyons une notification push à un utilisateur
[USERS_MESSAGES_SMS_ABORT_SHARED](#USERS_MESSAGES_SMS_ABORT_SHARED) | Un message SMS initialement planifié a été abandonné pour une raison quelconque.
[USERS_MESSAGES_SMS_CARRIERSEND_SHARED](#USERS_MESSAGES_SMS_CARRIERSEND_SHARED) | Lorsqu’un message SMS est envoyé au transporteur
[USERS_MESSAGES_SMS_DELIVERY_SHARED](#USERS_MESSAGES_SMS_DELIVERY_SHARED) | Lorsqu’un message SMS est livré
[USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED](#USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED) | Lorsque Braze n’est pas en mesure de livrer le message SMS au fournisseur de services SMS
[USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED](#USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED) | Lorsqu’un message SMS est reçu d’un utilisateur
[USERS_MESSAGES_SMS_REJECTION_SHARED](#USERS_MESSAGES_SMS_REJECTION_SHARED) | Lorsqu’un message SMS n’est pas livré à un utilisateur
[USERS_MESSAGES_SMS_SEND_SHARED](#USERS_MESSAGES_SMS_SEND_SHARED) | Lorsqu’un message SMS est envoyé
[USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED](#USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED) | Lorsqu’un utilisateur clique sur une URL raccourcie Braze incluse dans un message SMS
[USERS_MESSAGES_WEBHOOK_ABORT_SHARED](#USERS_MESSAGES_WEBHOOK_ABORT_SHARED) | Un message webhook initialement planifié a été abandonné pour une raison quelconque.
[USERS_MESSAGES_WEBHOOK_SEND_SHARED](#USERS_MESSAGES_WEBHOOK_SEND_SHARED) | Lorsque nous envoyons un webhook pour un utilisateur


## Comportements

### USERS_BEHAVIORS_CUSTOMEVENT_SHARED {#USERS_BEHAVIORS_CUSTOMEVENT_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID global unique de cet événement
`user_id` | `string` | ID BSON de l’utilisateur qui a effectué l’événement
`external_user_id` | `null,`&nbsp;`string` | [Informations personnellement identifiables] ID utilisateur externe de l’utilisateur
`app_group_api_id` | `null,`&nbsp;`string` | ID API du groupe d’apps auquel appartient cet utilisateur
`app_api_id` | `null,`&nbsp;`string` | ID API de l’application sur laquelle cette action s’est produite
`time` | `int` | Horodatage Unix du moment où l’utilisateur a effectué l’événement
`gender` | `null,`&nbsp;`string` | [Informations personnellement identifiables] sexe de l’utilisateur
`country` | `null,`&nbsp;`string` | [Informations personnellement identifiables] pays de l’utilisateur
`timezone` | `null,`&nbsp;`string` | fuseau horaire de l’utilisateur
`language` | `null,`&nbsp;`string` | [Informations personnellement identifiables] langue de l’utilisateur
`device_id` | `null,`&nbsp;`string` | ID de l’appareil sur lequel l’événement personnalisé s’est produit
`sdk_version` | `null,`&nbsp;`string` | version du SDK Braze utilisée pendant l’événement
`platform` | `null,`&nbsp;`string` | plateforme de l’appareil
`os_version` | `null,`&nbsp;`string` | version du système d’exploitation de l’appareil
`device_model` | `null,`&nbsp;`string` | modèle de l’appareil
`name` | `string` | nom de l’événement personnalisé
`properties` | `string` | propriétés personnalisées pour cet événement stockées sous forme de chaîne de caractères codée en JSON
`ad_id` | `null,`&nbsp;`string` | [Informations personnellement identifiables] Identifiant publicitaire
`ad_id_type` | `null,`&nbsp;`string` | Un parmi `ios_idfa`, `google_ad_id`, `windows_ad_id` OU `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Si le suivi publicitaire est activé pour l’appareil ou non
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS_BEHAVIORS_INSTALLATTRIBUTION_SHARED {#USERS_BEHAVIORS_INSTALLATTRIBUTION_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID global unique de cet événement
`user_id` | `string` | ID BSON de l’utilisateur qui a installé
`external_user_id` | `null,`&nbsp;`string` | [Informations personnellement identifiables] ID utilisateur externe de l’utilisateur
`device_id` | `null,`&nbsp;`string` | `device_id` qui est lié à cet utilisateur si celui-ci est anonyme
`app_group_api_id` | `null,`&nbsp;`string` | ID API du groupe d’apps auquel appartient cet utilisateur
`time` | `int` | Horodatage Unix du moment où l’utilisateur a installé
`source` | `string` | the source de l’attribution
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS_BEHAVIORS_LOCATION_SHARED {#USERS_BEHAVIORS_LOCATION_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID global unique de cet événement
`user_id` | `string` | ID BSON de l’utilisateur qui enregistre l’emplacement
`external_user_id` | `null,`&nbsp;`string` | [Informations personnellement identifiables] ID utilisateur externe de l’utilisateur
`app_group_api_id` | `null,`&nbsp;`string` | ID API du groupe d’apps auquel appartient cet utilisateur
`app_api_id` | `null,`&nbsp;`string` | ID API de l’application sur laquelle ce lieu a été enregistré
`time` | `int` | Horodatage Unix du moment où le lieu a été enregistré
`latitude` | `float` | [Informations personnellement identifiables] latitude du lieu enregistré
`longitude` | `float` | [Informations personnellement identifiables] longitude du lieu enregistré
`altitude` | `null, float` | [Informations personnellement identifiables] altitude du lieu enregistré
`ll_accuracy` | `null, float` | précision de la latitude et longitude du lieu enregistré
`alt_accuracy` | `null, float` | précision de l’altitude du lieu enregistré
`device_id` | `null,`&nbsp;`string` | ID de l’appareil sur lequel le lieu a été enregistré
`sdk_version` | `null,`&nbsp;`string` | version du SDK Braze utilisé lorsque le lieu a été enregistré
`platform` | `null,`&nbsp;`string` | plateforme de l’appareil
`os_version` | `null,`&nbsp;`string` | version du système d’exploitation de l’appareil
`device_model` | `null,`&nbsp;`string` | modèle de l’appareil
`ad_id` | `null,`&nbsp;`string` | [Informations personnellement identifiables] Identifiant publicitaire
`ad_id_type` | `null,`&nbsp;`string` | Un parmi `ios_idfa`, `google_ad_id`, `windows_ad_id` OU `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Si le suivi publicitaire est activé pour l’appareil ou non
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS_BEHAVIORS_PURCHASE_SHARED {#USERS_BEHAVIORS_PURCHASE_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID global unique de cet événement
`user_id` | `string` | ID BSON de l’utilisateur qui a effectué un achat
`external_user_id` | `null,`&nbsp;`string` | [Informations personnellement identifiables] ID utilisateur externe de l’utilisateur
`app_group_api_id` | `null,`&nbsp;`string` | ID API du groupe d’apps auquel appartient cet utilisateur
`app_api_id` | `null,`&nbsp;`string` | ID API de l’application sur laquelle l’achat a eu lieu
`time` | `int` | Horodatage Unix du moment où l’utilisateur a effectué l’achat
`device_id` | `null,`&nbsp;`string` | ID de l’appareil sur lequel l’achat s’est produit
`sdk_version` | `null,`&nbsp;`string` | version du SDK Braze utilisée pendant l’achat
`platform` | `null,`&nbsp;`string` | plateforme de l’appareil
`os_version` | `null,`&nbsp;`string` | version du système d’exploitation de l’appareil
`device_model` | `null,`&nbsp;`string` | modèle de l’appareil
`product_id` | `string` | identifiant du produit acheté
`price` | `float` | prix de l’achat
`currency` | `string` | devise de l’achat
`properties` | `string` | propriétés personnalisées pour cet achat stockées sous forme de chaîne de caractères codée en JSON
`ad_id` | `null,`&nbsp;`string` | [Informations personnellement identifiables] Identifiant publicitaire
`ad_id_type` | `null,`&nbsp;`string` | Un parmi `ios_idfa`, `google_ad_id`, `windows_ad_id` OU `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Si le suivi publicitaire est activé pour l’appareil ou non
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS_BEHAVIORS_UNINSTALL_SHARED {#USERS_BEHAVIORS_UNINSTALL_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID global unique de cet événement
`user_id` | `string` | ID BSON de l’utilisateur qui a désinstallé
`external_user_id` | `null,`&nbsp;`string` | [Informations personnellement identifiables] ID utilisateur externe de l’utilisateur
`device_id` | `null,`&nbsp;`string` | `device_id` qui est lié à cet utilisateur si celui-ci est anonyme
`app_group_api_id` | `null,`&nbsp;`string` | ID API du groupe d’apps auquel appartient cet utilisateur
`app_api_id` | `null,`&nbsp;`string` | ID API de l’application qui a été désinstallée
`time` | `int` | Horodatage Unix du moment où l’utilisateur a désinstallé
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS_BEHAVIORS_UPGRADEDAPP_SHARED {#USERS_BEHAVIORS_UPGRADEDAPP_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID global unique de cet événement
`user_id` | `string` | ID BSON de l’utilisateur qui a mis à niveau l’application
`external_user_id` | `null,`&nbsp;`string` | [Informations personnellement identifiables] ID utilisateur externe de l’utilisateur
`app_group_api_id` | `null,`&nbsp;`string` | ID API du groupe d’apps auquel appartient cet utilisateur
`app_api_id` | `null,`&nbsp;`string` | ID API de l’application mise à niveau par l’utilisateur
`time` | `int` | Horodatage Unix du moment où l’utilisateur a mis à niveau l’application
`device_id` | `null,`&nbsp;`string` | ID de l’appareil sur lequel l’utilisateur a mis à niveau l’application
`sdk_version` | `null,`&nbsp;`string` | version du SDK Braze utilisé
`platform` | `null,`&nbsp;`string` | plateforme de l’appareil
`os_version` | `null,`&nbsp;`string` | version du système d’exploitation de l’appareil
`device_model` | `null,`&nbsp;`string` | modèle de l’appareil
`old_app_version` | `null,`&nbsp;`string` | ancienne version de l’application
`new_app_version` | `null,`&nbsp;`string` | new version de l’application
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS_BEHAVIORS_APP_FIRSTSESSION_SHARED {#USERS_BEHAVIORS_APP_FIRSTSESSION_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID global unique de cet événement
`user_id` | `string` | ID BSON de l’utilisateur qui effectue cette action
`external_user_id` | `null,`&nbsp;`string` | [Informations personnellement identifiables] ID utilisateur externe de l’utilisateur
`app_group_api_id` | `null,`&nbsp;`string` | ID API du groupe d’apps auquel appartient cet utilisateur
`app_api_id` | `null,`&nbsp;`string` | ID API de l’application sur laquelle cette session s’est produite
`time` | `int` | Horodatage Unix du moment où la session a commencé
`session_id` | `string` | UUID de la session
`gender` | `null,`&nbsp;`string` | [Informations personnellement identifiables] sexe de l’utilisateur
`country` | `null,`&nbsp;`string` | [Informations personnellement identifiables] pays de l’utilisateur
`timezone` | `null,`&nbsp;`string` | fuseau horaire de l’utilisateur
`language` | `null,`&nbsp;`string` | [Informations personnellement identifiables] langue de l’utilisateur
`device_id` | `null,`&nbsp;`string` | ID de l’appareil sur lequel la session s’est produite
`sdk_version` | `null,`&nbsp;`string` | version du SDK Braze utilisée pendant la session
`platform` | `null,`&nbsp;`string` | plateforme de l’appareil
`os_version` | `null,`&nbsp;`string` | version du système d’exploitation de l’appareil
`device_model` | `null,`&nbsp;`string` | model de l’appareil
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS_BEHAVIORS_APP_NEWSFEEDIMPRESSION_SHARED {#USERS_BEHAVIORS_APP_NEWSFEEDIMPRESSION_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID global unique de cet événement
`user_id` | `string` | ID BSON de l’utilisateur qui a vu le fil d’actualité
`external_user_id` | `null,`&nbsp;`string` | [Informations personnellement identifiables] ID utilisateur externe de l’utilisateur
`app_group_api_id` | `null,`&nbsp;`string` | ID API du groupe d’apps auquel appartient cet utilisateur
`app_api_id` | `null,`&nbsp;`string` | ID API de l’application sur laquelle l’utilisateur a vu le fil d’actualité
`time` | `int` | Horodatage Unix du moment où l’utilisateur a vu le fil d’actualité
`device_id` | `null,`&nbsp;`string` | ID de l’appareil sur lequel l’impression s’est produite
`sdk_version` | `null,`&nbsp;`string` | version du SDK Braze utilisée pendant l’impression
`platform` | `null,`&nbsp;`string` | plateforme de l’appareil
`os_version` | `null,`&nbsp;`string` | version du système d’exploitation de l’appareil
`device_model` | `null,`&nbsp;`string` | model de l’appareil
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS_BEHAVIORS_APP_SESSIONEND_SHARED {#USERS_BEHAVIORS_APP_SESSIONEND_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID global unique de cet événement
`user_id` | `string` | ID BSON de l’utilisateur qui effectue cette action
`external_user_id` | `null,`&nbsp;`string` | [Informations personnellement identifiables] ID utilisateur externe de l’utilisateur
`app_group_api_id` | `null,`&nbsp;`string` | ID API du groupe d’apps auquel appartient cet utilisateur
`app_api_id` | `null,`&nbsp;`string` | ID API de l’application sur laquelle cette session s’est produite
`time` | `int` | Horodatage Unix du moment où la session s’est terminée
`duration` | `null, float` | durée de la session
`session_id` | `string` | UUID de la session
`device_id` | `null,`&nbsp;`string` | ID de l’appareil sur lequel la session s’est produite
`sdk_version` | `null,`&nbsp;`string` | version du SDK Braze utilisée pendant la session
`platform` | `null,`&nbsp;`string` | plateforme de l’appareil
`os_version` | `null,`&nbsp;`string` | version du système d’exploitation de l’appareil
`device_model` | `null,`&nbsp;`string` | model de l’appareil
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS_BEHAVIORS_APP_SESSIONSTART_SHARED {#USERS_BEHAVIORS_APP_SESSIONSTART_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID global unique de cet événement
`user_id` | `string` | ID BSON de l’utilisateur qui effectue cette action
`external_user_id` | `null,`&nbsp;`string` | [Informations personnellement identifiables] ID utilisateur externe de l’utilisateur
`app_api_id` | `null,`&nbsp;`string` | ID API de l’application sur laquelle cette session s’est produite
`app_group_api_id` | `null,`&nbsp;`string` | ID API du groupe d’apps auquel appartient cet utilisateur
`time` | `int` | Horodatage Unix du moment où la session a commencé
`session_id` | `string` | UUID de la session
`device_id` | `null,`&nbsp;`string` | ID de l’appareil sur lequel la session s’est produite
`sdk_version` | `null,`&nbsp;`string` | version du SDK Braze utilisée pendant la session
`platform` | `null,`&nbsp;`string` | plateforme de l’appareil
`os_version` | `null,`&nbsp;`string` | version du système d’exploitation de l’appareil
`device_model` | `null,`&nbsp;`string` | model de l’appareil
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS_BEHAVIORS_GEOFENCE_DATAEVENT_SHARED {#USERS_BEHAVIORS_GEOFENCE_DATAEVENT_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID global unique de cet événement
`user_id` | `string` | ID BSON de l’utilisateur qui a effectué l’événement
`external_user_id` | `null,`&nbsp;`string` | [Informations personnellement identifiables] ID utilisateur externe de l’utilisateur
`app_group_api_id` | `null,`&nbsp;`string` | ID API du groupe d’apps auquel appartient cet utilisateur
`app_api_id` | `null,`&nbsp;`string` | ID API de l’application sur laquelle cette action s’est produite
`time` | `int` | Horodatage Unix du moment où l’utilisateur a effectué l’événement
`device_id` | `null,`&nbsp;`string` | ID de l’appareil sur lequel l’événement personnalisé s’est produit
`sdk_version` | `null,`&nbsp;`string` | version du SDK Braze utilisée pendant l’événement
`platform` | `null,`&nbsp;`string` | plateforme de l’appareil
`os_version` | `null,`&nbsp;`string` | version du système d’exploitation de l’appareil
`device_model` | `null,`&nbsp;`string` | modèle de l’appareil
`event_type` | `string` | Quel type d’événement de geofence a été déclenché (par ex., « entrée » ou « sortie »)
`location_set_id` | `string` | L’ID de l’ensemble d’emplacements de la geofence qui a été déclenchée
`geofence_id` | `string` | L’ID de la geofence qui a été déclenchée
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS_BEHAVIORS_GEOFENCE_RECORDEVENT_SHARED {#USERS_BEHAVIORS_GEOFENCE_RECORDEVENT_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID global unique de cet événement
`user_id` | `string` | ID BSON de l’utilisateur qui a effectué l’événement
`external_user_id` | `null,`&nbsp;`string` | [Informations personnellement identifiables] ID utilisateur externe de l’utilisateur
`app_group_api_id` | `null,`&nbsp;`string` | ID API du groupe d’apps auquel appartient cet utilisateur
`app_api_id` | `null,`&nbsp;`string` | ID API de l’application sur laquelle cette action s’est produite
`time` | `int` | Horodatage Unix du moment où l’utilisateur a effectué l’événement
`device_id` | `null,`&nbsp;`string` | ID de l’appareil sur lequel l’événement personnalisé s’est produit
`sdk_version` | `null,`&nbsp;`string` | version du SDK Braze utilisée pendant l’événement
`platform` | `null,`&nbsp;`string` | plateforme de l’appareil
`os_version` | `null,`&nbsp;`string` | version du système d’exploitation de l’appareil
`device_model` | `null,`&nbsp;`string` | modèle de l’appareil
`event_type` | `string` | Quel type d’événement de geofence a été déclenché (par ex., « entrée » ou « sortie »)
`location_set_id` | `string` | L’ID de l’ensemble d’emplacements de la geofence qui a été déclenchée
`geofence_id` | `string` | L’ID de la geofence qui a été déclenchée
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS_BEHAVIORS_SUBSCRIPTION_GLOBALSTATECHANGE_SHARED {#USERS_BEHAVIORS_SUBSCRIPTION_GLOBALSTATECHANGE_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID global unique de cet événement
`user_id` | `string` | ID BSON de l’utilisateur affecté
`external_user_id` | `null,`&nbsp;`string` | [Informations personnellement identifiables] ID utilisateur externe de l’utilisateur
`email_address` | `null,`&nbsp;`string` | [Informations personnellement identifiables] adresse e-mail de l’utilisateur
`state_change_source` | `null,`&nbsp;`string` | source du changement d’état (REST, SDK, tableau de bord, etc.)
`subscription_status` | `string` | statut d’abonnement : 'Abonné' ou 'Désabonné'
`channel` | `null,`&nbsp;`string` | canal de l’état d’abonnement global tel que l’e-mail
`time` | `int` | Horodatage Unix du moment où l’état de l’abonnement a changé
`timezone` | `null,`&nbsp;`string` | fuseau horaire de l’utilisateur
`app_group_api_id` | `null,`&nbsp;`string` | ID API du groupe d’apps auquel appartient cet utilisateur
`app_api_id` | `null,`&nbsp;`string` | ID API de l’application à laquelle appartient l’événement
`campaign_id` | `null,`&nbsp;`string` | ID Braze à usage interne de la campagne à laquelle appartient cet événement
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la campagne à laquelle appartient cet événement
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de message à laquelle appartient cet événement
`canvas_id` | `null,`&nbsp;`string` | ID Braze à usage interne du Canvas auquel appartient cet événement
`canvas_api_id` | `null,`&nbsp;`string` | ID API du Canvas auquel appartient cet événement
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de Canvas à laquelle appartient cet événement
`canvas_step_api_id` | `null,`&nbsp;`string` | ID API du Canvas Step auquel appartient cet événement
`send_id` | `null,`&nbsp;`string` | message ID d’envoi de l’endroit d’où provient cette action de changement d’état d’abonnement
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED {#USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID global unique de cet événement
`user_id` | `string` | ID BSON de l’utilisateur affecté
`external_user_id` | `null,`&nbsp;`string` | [Informations personnellement identifiables] ID utilisateur externe de l’utilisateur
`device_id` | `null,`&nbsp;`string` | `device_id` qui est lié à cet utilisateur si celui-ci est anonyme
`app_group_api_id` | `null,`&nbsp;`string` | ID API du groupe d’apps auquel appartient cet utilisateur
`email_address` | `null,`&nbsp;`string` | [Informations personnellement identifiables] adresse e-mail de l’utilisateur
`phone_number` | `null,`&nbsp;`string` | [Informations personnellement identifiables] numéro de téléphone de l’utilisateur au format E.164
`app_api_id` | `null,`&nbsp;`string` | ID API de l’application à laquelle appartient l’événement
`campaign_id` | `null,`&nbsp;`string` | ID Braze à usage interne de la campagne à laquelle appartient cet événement
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la campagne à laquelle appartient cet événement
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de message à laquelle appartient cet événement
`canvas_id` | `null,`&nbsp;`string` | ID Braze à usage interne du Canvas auquel appartient cet événement
`canvas_api_id` | `null,`&nbsp;`string` | ID API du Canvas auquel appartient cet événement
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de Canvas à laquelle appartient cet événement
`canvas_step_api_id` | `null,`&nbsp;`string` | ID API du Canvas Step auquel appartient cet événement
`subscription_group_api_id` | `string` | ID API de groupe d’abonnement
`channel` | `null,`&nbsp;`string` | canal : ’email’ ou ’sms’, selon le type de canal du groupe d’abonnement
`subscription_status` | `string` | statut d’abonnement : 'Abonné' ou 'Désabonné'
`time` | `int` | Horodatage Unix du moment où l’état de l’abonnement a changé
`timezone` | `null,`&nbsp;`string` | fuseau horaire de l’utilisateur
`send_id` | `null,`&nbsp;`string` | ID d’envoi du message d’où provient cette action de changement d’état d’abonnement
`state_change_source` | `null,`&nbsp;`string` | source du changement d’état (REST, SDK, tableau de bord, etc.)
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Campagnes

### USERS_CAMPAIGNS_ABORT_SHARED {#USERS_CAMPAIGNS_ABORT_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID global unique de cet événement
`user_id` | `string` | ID BSON de l’utilisateur qui a effectué cet événement
`external_user_id` | `null,`&nbsp;`string` | [Informations personnellement identifiables] ID utilisateur externe de l’utilisateur
`device_id` | `null,`&nbsp;`string` | `device_id` qui est lié à cet utilisateur si celui-ci est anonyme
`app_group_api_id` | `null,`&nbsp;`string` | ID API du groupe d’apps auquel appartient cet utilisateur
`time` | `int` | horodatage Unix du moment où l’événement s’est produit
`dispatch_id` | `null,`&nbsp;`string` | ID de l’envoi auquel appartient ce message
`send_id` | `null,`&nbsp;`string` | ID d’envoi de message auquel appartient ce message
`campaign_id` | `string` | ID Braze à usage interne de la campagne à laquelle appartient cet événement
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la campagne à laquelle appartient cet événement
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de message que l’utilisateur a reçue
`channel` | `null,`&nbsp;`string` | canal auquel cet événement appartient
`gender` | `null,`&nbsp;`string` | [Informations personnellement identifiables] sexe de l’utilisateur
`country` | `null,`&nbsp;`string` | [Informations personnellement identifiables] pays de l’utilisateur
`timezone` | `null,`&nbsp;`string` | fuseau horaire de l’utilisateur
`language` | `null,`&nbsp;`string` | [Informations personnellement identifiables] langue de l’utilisateur
`abort_type` | `null,`&nbsp;`string` | type d’abandon, l’un des éléments suivants : `liquid_abort_message`, `quiet_hours`, `rate_limit`
`abort_log` | `null,`&nbsp;`string` | [Informations personnellement identifiables] message du journal décrivant les détails de l’abandon (128 caractères maximum)
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS_CAMPAIGNS_CONVERSION_SHARED {#USERS_CAMPAIGNS_CONVERSION_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID global unique de cet événement
`user_id` | `string` | ID BSON de l’utilisateur qui a effectué cet événement
`external_user_id` | `null,`&nbsp;`string` | [Informations personnellement identifiables] ID utilisateur externe de l’utilisateur
`device_id` | `null,`&nbsp;`string` | `device_id` qui est lié à cet utilisateur si celui-ci est anonyme
`app_group_api_id` | `null,`&nbsp;`string` | ID API du groupe d’apps auquel appartient cet utilisateur
`time` | `int` | horodatage Unix du moment où l’événement s’est produit
`app_api_id` | `null,`&nbsp;`string` | ID API de l’application sur laquelle cet événement s’est produit
`dispatch_id` | `null,`&nbsp;`string` | ID de l’envoi auquel appartient ce message
`send_id` | `null,`&nbsp;`string` | ID d’envoi de message auquel appartient ce message
`campaign_id` | `string` | ID Braze à usage interne de la campagne à laquelle appartient cet événement
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la campagne à laquelle appartient cet événement
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de message que l’utilisateur a reçue
`conversion_behavior_index` | `null, int` | index du comportement de conversion
`gender` | `null,`&nbsp;`string` | [Informations personnellement identifiables] sexe de l’utilisateur
`country` | `null,`&nbsp;`string` | [Informations personnellement identifiables] pays de l’utilisateur
`timezone` | `null,`&nbsp;`string` | fuseau horaire de l’utilisateur
`language` | `null,`&nbsp;`string` | [Informations personnellement identifiables] langue de l’utilisateur
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS_CAMPAIGNS_ENROLLINCONTROL_SHARED {#USERS_CAMPAIGNS_ENROLLINCONTROL_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID global unique de cet événement
`user_id` | `string` | ID BSON de l’utilisateur qui a effectué cet événement
`external_user_id` | `null,`&nbsp;`string` | [Informations personnellement identifiables] ID utilisateur externe de l’utilisateur
`device_id` | `null,`&nbsp;`string` | `device_id` qui est lié à cet utilisateur si celui-ci est anonyme
`app_group_api_id` | `null,`&nbsp;`string` | ID API du groupe d’apps auquel appartient cet utilisateur
`time` | `int` | horodatage Unix du moment où l’événement s’est produit
`app_api_id` | `null,`&nbsp;`string` | ID API de l’application sur laquelle cet événement s’est produit
`dispatch_id` | `null,`&nbsp;`string` | ID de l’envoi auquel appartient ce message
`send_id` | `null,`&nbsp;`string` | ID d’envoi de message auquel appartient ce message
`campaign_id` | `string` | ID Braze à usage interne de la campagne à laquelle appartient cet événement
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la campagne à laquelle appartient cet événement
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de message que l’utilisateur a reçue
`gender` | `null,`&nbsp;`string` | [Informations personnellement identifiables] sexe de l’utilisateur
`country` | `null,`&nbsp;`string` | [Informations personnellement identifiables] pays de l’utilisateur
`timezone` | `null,`&nbsp;`string` | fuseau horaire de l’utilisateur
`language` | `null,`&nbsp;`string` | [Informations personnellement identifiables] langue de l’utilisateur
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS_CAMPAIGNS_FREQUENCYCAP_SHARED {#USERS_CAMPAIGNS_FREQUENCYCAP_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID global unique de cet événement
`user_id` | `string` | ID BSON de l’utilisateur qui a effectué cet événement
`external_user_id` | `null,`&nbsp;`string` | [Informations personnellement identifiables] ID utilisateur externe de l’utilisateur
`device_id` | `null,`&nbsp;`string` | `device_id` qui est lié à cet utilisateur si celui-ci est anonyme
`app_group_api_id` | `null,`&nbsp;`string` | ID API du groupe d’apps auquel appartient cet utilisateur
`time` | `int` | horodatage Unix du moment où l’événement s’est produit
`dispatch_id` | `null,`&nbsp;`string` | ID de l’envoi auquel appartient ce message
`send_id` | `null,`&nbsp;`string` | ID d’envoi de message auquel appartient ce message
`campaign_id` | `string` | ID Braze à usage interne de la campagne à laquelle appartient cet événement
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la campagne à laquelle appartient cet événement
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de message que l’utilisateur a reçue
`channel` | `null,`&nbsp;`string` | canal auquel cet événement appartient
`gender` | `null,`&nbsp;`string` | [Informations personnellement identifiables] sexe de l’utilisateur
`country` | `null,`&nbsp;`string` | [Informations personnellement identifiables] pays de l’utilisateur
`timezone` | `null,`&nbsp;`string` | fuseau horaire de l’utilisateur
`language` | `null,`&nbsp;`string` | [Informations personnellement identifiables] langue de l’utilisateur
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS_CAMPAIGNS_REVENUE_SHARED {#USERS_CAMPAIGNS_REVENUE_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID global unique de cet événement
`user_id` | `string` | ID BSON de l’utilisateur qui a effectué cet événement
`external_user_id` | `null,`&nbsp;`string` | [Informations personnellement identifiables] ID utilisateur externe de l’utilisateur
`device_id` | `null,`&nbsp;`string` | `device_id` qui est lié à cet utilisateur si celui-ci est anonyme
`app_group_api_id` | `null,`&nbsp;`string` | ID API du groupe d’apps auquel appartient cet utilisateur
`time` | `int` | horodatage Unix du moment où l’événement s’est produit
`app_api_id` | `null,`&nbsp;`string` | ID API de l’application sur laquelle cet événement s’est produit
`dispatch_id` | `null,`&nbsp;`string` | ID de l’envoi auquel appartient ce message
`send_id` | `null,`&nbsp;`string` | ID d’envoi de message auquel appartient ce message
`campaign_id` | `string` | ID Braze à usage interne de la campagne à laquelle appartient cet événement
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la campagne à laquelle appartient cet événement
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de message que l’utilisateur a reçue
`gender` | `null,`&nbsp;`string` | [Informations personnellement identifiables] sexe de l’utilisateur
`country` | `null,`&nbsp;`string` | [Informations personnellement identifiables] pays de l’utilisateur
`timezone` | `null,`&nbsp;`string` | fuseau horaire de l’utilisateur
`language` | `null,`&nbsp;`string` | [Informations personnellement identifiables] langue de l’utilisateur
`revenue` | `long` | the montant du chiffre d’affaires généré en USD et en centimes
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Messages

### USERS_MESSAGES_CONTENTCARD_ABORT_SHARED {#USERS_MESSAGES_CONTENTCARD_ABORT_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID global unique de cet événement
`user_id` | `string` | ID BSON de l’utilisateur qui a effectué cet événement
`external_user_id` | `null,`&nbsp;`string` | [Informations personnellement identifiables] ID utilisateur externe de l’utilisateur
`device_id` | `null,`&nbsp;`string` | `device_id` qui est lié à cet utilisateur si celui-ci est anonyme
`app_group_api_id` | `null,`&nbsp;`string` | ID API du groupe d’apps auquel appartient cet utilisateur
`time` | `int` | horodatage Unix du moment où l’événement s’est produit
`dispatch_id` | `null,`&nbsp;`string` | ID de l’envoi auquel appartient ce message
`send_id` | `null,`&nbsp;`string` | ID d’envoi de message auquel appartient ce message
`campaign_id` | `null,`&nbsp;`string` | ID Braze à usage interne de la campagne à laquelle appartient cet événement
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la campagne à laquelle appartient cet événement
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de message que l’utilisateur a reçue
`canvas_id` | `null,`&nbsp;`string` | ID Braze à usage interne du Canvas auquel appartient cet événement
`canvas_api_id` | `null,`&nbsp;`string` | ID API du Canvas auquel appartient cet événement
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de Canvas à laquelle appartient cet événement
`canvas_step_api_id` | `null,`&nbsp;`string` | ID API du Canvas Step auquel appartient cet événement
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de message de Canvas Step que l’utilisateur a reçue
`gender` | `null,`&nbsp;`string` | [Informations personnellement identifiables] sexe de l’utilisateur
`country` | `null,`&nbsp;`string` | [Informations personnellement identifiables] pays de l’utilisateur
`timezone` | `null,`&nbsp;`string` | fuseau horaire de l’utilisateur
`language` | `null,`&nbsp;`string` | [Informations personnellement identifiables] langue de l’utilisateur
`abort_type` | `null,`&nbsp;`string` | type d’abandon, l’un des éléments suivants : `liquid_abort_message`, `quiet_hours`, `rate_limit`
`abort_log` | `null,`&nbsp;`string` | [Informations personnellement identifiables] message du journal décrivant les détails de l’abandon (128 caractères maximum)
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS_MESSAGES_CONTENTCARD_CLICK_SHARED {#USERS_MESSAGES_CONTENTCARD_CLICK_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID global unique de cet événement
`user_id` | `string` | ID BSON de l’utilisateur qui a effectué cet événement
`content_card_id` | `string` | ID de la carte qui a généré cet événement
`external_user_id` | `null,`&nbsp;`string` | [Informations personnellement identifiables] ID utilisateur externe de l’utilisateur
`app_group_api_id` | `null,`&nbsp;`string` | ID API du groupe d’apps auquel appartient cet utilisateur
`time` | `int` | horodatage Unix du moment où l’événement s’est produit
`app_api_id` | `null,`&nbsp;`string` | ID API de l’application sur laquelle cet événement s’est produit
`dispatch_id` | `null,`&nbsp;`string` | ID de l’envoi auquel appartient ce message
`send_id` | `null,`&nbsp;`string` | ID d’envoi de message auquel appartient ce message
`campaign_id` | `null,`&nbsp;`string` | ID Braze à usage interne de la campagne à laquelle appartient cet événement
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la campagne à laquelle appartient cet événement
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de message que l’utilisateur a reçue
`canvas_id` | `null,`&nbsp;`string` | ID Braze à usage interne du Canvas auquel appartient cet événement
`canvas_api_id` | `null,`&nbsp;`string` | ID API du Canvas auquel appartient cet événement
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de Canvas à laquelle appartient cet événement
`canvas_step_api_id` | `null,`&nbsp;`string` | ID API du Canvas Step auquel appartient cet événement
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de message de Canvas Step que l’utilisateur a reçue
`gender` | `null,`&nbsp;`string` | [Informations personnellement identifiables] sexe de l’utilisateur
`country` | `null,`&nbsp;`string` | [Informations personnellement identifiables] pays de l’utilisateur
`timezone` | `null,`&nbsp;`string` | fuseau horaire de l’utilisateur
`language` | `null,`&nbsp;`string` | [Informations personnellement identifiables] langue de l’utilisateur
`device_id` | `null,`&nbsp;`string` | ID de l’appareil sur lequel l’événement s’est produit
`sdk_version` | `null,`&nbsp;`string` | version du SDK Braze utilisée pendant l’événement
`platform` | `null,`&nbsp;`string` | plateforme de l’appareil
`os_version` | `null,`&nbsp;`string` | version du système d’exploitation de l’appareil
`device_model` | `null,`&nbsp;`string` | modèle de l’appareil
`resolution` | `null,`&nbsp;`string` | résolution de l’appareil
`carrier` | `null,`&nbsp;`string` | transporteur de l’appareil
`browser` | `null,`&nbsp;`string` | navigateur de l’appareil
`ad_id` | `null,`&nbsp;`string` | [Informations personnellement identifiables] Identifiant publicitaire
`ad_id_type` | `null,`&nbsp;`string` | Un parmi `ios_idfa`, `google_ad_id`, `windows_ad_id` OU `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Si le suivi publicitaire est activé pour l’appareil ou non
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS_MESSAGES_CONTENTCARD_DISMISS_SHARED {#USERS_MESSAGES_CONTENTCARD_DISMISS_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID global unique de cet événement
`user_id` | `string` | ID BSON de l’utilisateur qui a effectué cet événement
`content_card_id` | `string` | ID de la carte qui a généré cet événement
`external_user_id` | `null,`&nbsp;`string` | [Informations personnellement identifiables] ID utilisateur externe de l’utilisateur
`app_group_api_id` | `null,`&nbsp;`string` | ID API du groupe d’apps auquel appartient cet utilisateur
`time` | `int` | horodatage Unix du moment où l’événement s’est produit
`app_api_id` | `null,`&nbsp;`string` | ID API de l’application sur laquelle cet événement s’est produit
`dispatch_id` | `null,`&nbsp;`string` | ID de l’envoi auquel appartient ce message
`send_id` | `null,`&nbsp;`string` | ID d’envoi de message auquel appartient ce message
`campaign_id` | `null,`&nbsp;`string` | ID Braze à usage interne de la campagne à laquelle appartient cet événement
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la campagne à laquelle appartient cet événement
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de message que l’utilisateur a reçue
`canvas_id` | `null,`&nbsp;`string` | ID Braze à usage interne du Canvas auquel appartient cet événement
`canvas_api_id` | `null,`&nbsp;`string` | ID API du Canvas auquel appartient cet événement
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de Canvas à laquelle appartient cet événement
`canvas_step_api_id` | `null,`&nbsp;`string` | ID API du Canvas Step auquel appartient cet événement
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de message de Canvas Step que l’utilisateur a reçue
`gender` | `null,`&nbsp;`string` | [Informations personnellement identifiables] sexe de l’utilisateur
`country` | `null,`&nbsp;`string` | [Informations personnellement identifiables] pays de l’utilisateur
`timezone` | `null,`&nbsp;`string` | fuseau horaire de l’utilisateur
`language` | `null,`&nbsp;`string` | [Informations personnellement identifiables] langue de l’utilisateur
`device_id` | `null,`&nbsp;`string` | ID de l’appareil sur lequel l’événement s’est produit
`sdk_version` | `null,`&nbsp;`string` | version du SDK Braze utilisée pendant l’événement
`platform` | `null,`&nbsp;`string` | plateforme de l’appareil
`os_version` | `null,`&nbsp;`string` | version du système d’exploitation de l’appareil
`device_model` | `null,`&nbsp;`string` | modèle de l’appareil
`resolution` | `null,`&nbsp;`string` | résolution de l’appareil
`carrier` | `null,`&nbsp;`string` | transporteur de l’appareil
`browser` | `null,`&nbsp;`string` | navigateur de l’appareil
`ad_id` | `null,`&nbsp;`string` | [Informations personnellement identifiables] Identifiant publicitaire
`ad_id_type` | `null,`&nbsp;`string` | Un parmi `ios_idfa`, `google_ad_id`, `windows_ad_id` OU `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Si le suivi publicitaire est activé pour l’appareil ou non
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS_MESSAGES_CONTENTCARD_IMPRESSION_SHARED {#USERS_MESSAGES_CONTENTCARD_IMPRESSION_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID global unique de cet événement
`user_id` | `string` | ID BSON de l’utilisateur qui a effectué cet événement
`content_card_id` | `string` | ID de la carte qui a généré cet événement
`external_user_id` | `null,`&nbsp;`string` | [Informations personnellement identifiables] ID utilisateur externe de l’utilisateur
`app_group_api_id` | `null,`&nbsp;`string` | ID API du groupe d’apps auquel appartient cet utilisateur
`time` | `int` | horodatage Unix du moment où l’événement s’est produit
`app_api_id` | `null,`&nbsp;`string` | ID API de l’application sur laquelle cet événement s’est produit
`dispatch_id` | `null,`&nbsp;`string` | ID de l’envoi auquel appartient ce message
`send_id` | `null,`&nbsp;`string` | ID d’envoi de message auquel appartient ce message
`campaign_id` | `null,`&nbsp;`string` | ID Braze à usage interne de la campagne à laquelle appartient cet événement
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la campagne à laquelle appartient cet événement
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de message que l’utilisateur a reçue
`canvas_id` | `null,`&nbsp;`string` | ID Braze à usage interne du Canvas auquel appartient cet événement
`canvas_api_id` | `null,`&nbsp;`string` | ID API du Canvas auquel appartient cet événement
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de Canvas à laquelle appartient cet événement
`canvas_step_api_id` | `null,`&nbsp;`string` | ID API du Canvas Step auquel appartient cet événement
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de message de Canvas Step que l’utilisateur a reçue
`gender` | `null,`&nbsp;`string` | [Informations personnellement identifiables] sexe de l’utilisateur
`country` | `null,`&nbsp;`string` | [Informations personnellement identifiables] pays de l’utilisateur
`timezone` | `null,`&nbsp;`string` | fuseau horaire de l’utilisateur
`language` | `null,`&nbsp;`string` | [Informations personnellement identifiables] langue de l’utilisateur
`device_id` | `null,`&nbsp;`string` | ID de l’appareil sur lequel l’événement s’est produit
`sdk_version` | `null,`&nbsp;`string` | version du SDK Braze utilisée pendant l’événement
`platform` | `null,`&nbsp;`string` | plateforme de l’appareil
`os_version` | `null,`&nbsp;`string` | version du système d’exploitation de l’appareil
`device_model` | `null,`&nbsp;`string` | modèle de l’appareil
`resolution` | `null,`&nbsp;`string` | résolution de l’appareil
`carrier` | `null,`&nbsp;`string` | transporteur de l’appareil
`browser` | `null,`&nbsp;`string` | navigateur de l’appareil
`ad_id` | `null,`&nbsp;`string` | [Informations personnellement identifiables] Identifiant publicitaire
`ad_id_type` | `null,`&nbsp;`string` | Un parmi `ios_idfa`, `google_ad_id`, `windows_ad_id` OU `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Si le suivi publicitaire est activé pour l’appareil ou non
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS_MESSAGES_CONTENTCARD_SEND_SHARED {#USERS_MESSAGES_CONTENTCARD_SEND_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID global unique de cet événement
`user_id` | `string` | ID BSON de l’utilisateur qui a effectué cet événement
`external_user_id` | `null,`&nbsp;`string` | [Informations personnellement identifiables] ID utilisateur externe de l’utilisateur
`device_id` | `null,`&nbsp;`string` | `device_id` qui est lié à cet utilisateur si celui-ci est anonyme
`app_group_api_id` | `null,`&nbsp;`string` | ID API du groupe d’apps auquel appartient cet utilisateur
`time` | `int` | horodatage Unix du moment où l’événement s’est produit
`dispatch_id` | `null,`&nbsp;`string` | ID de l’envoi auquel appartient ce message
`send_id` | `null,`&nbsp;`string` | ID d’envoi de message auquel appartient ce message
`campaign_id` | `null,`&nbsp;`string` | ID Braze à usage interne de la campagne à laquelle appartient cet événement
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la campagne à laquelle appartient cet événement
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de message que l’utilisateur a reçue
`canvas_id` | `null,`&nbsp;`string` | ID Braze à usage interne du Canvas auquel appartient cet événement
`canvas_api_id` | `null,`&nbsp;`string` | ID API du Canvas auquel appartient cet événement
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de Canvas à laquelle appartient cet événement
`canvas_step_api_id` | `null,`&nbsp;`string` | ID API du Canvas Step auquel appartient cet événement
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de message de Canvas Step que l’utilisateur a reçue
`gender` | `null,`&nbsp;`string` | [Informations personnellement identifiables] sexe de l’utilisateur
`country` | `null,`&nbsp;`string` | [Informations personnellement identifiables] pays de l’utilisateur
`timezone` | `null,`&nbsp;`string` | fuseau horaire de l’utilisateur
`language` | `null,`&nbsp;`string` | [Informations personnellement identifiables] langue de l’utilisateur
`content_card_id` | `string` | ID de la carte qui a généré cet événement
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS_MESSAGES_EMAIL_ABORT_SHARED {#USERS_MESSAGES_EMAIL_ABORT_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID global unique de cet événement
`user_id` | `string` | ID BSON de l’utilisateur qui a effectué cet événement
`external_user_id` | `null,`&nbsp;`string` | [Informations personnellement identifiables] ID utilisateur externe de l’utilisateur
`device_id` | `null,`&nbsp;`string` | `device_id` qui est lié à cet utilisateur si celui-ci est anonyme
`app_group_api_id` | `null,`&nbsp;`string` | ID API du groupe d’apps auquel appartient cet utilisateur
`time` | `int` | horodatage Unix du moment où l’événement s’est produit
`dispatch_id` | `null,`&nbsp;`string` | ID de l’envoi auquel appartient ce message
`send_id` | `null,`&nbsp;`string` | ID d’envoi de message auquel appartient ce message
`campaign_id` | `null,`&nbsp;`string` | ID Braze à usage interne de la campagne à laquelle appartient cet événement
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la campagne à laquelle appartient cet événement
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de message que l’utilisateur a reçue
`canvas_id` | `null,`&nbsp;`string` | ID Braze à usage interne du Canvas auquel appartient cet événement
`canvas_api_id` | `null,`&nbsp;`string` | ID API du Canvas auquel appartient cet événement
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de Canvas à laquelle appartient cet événement
`canvas_step_api_id` | `null,`&nbsp;`string` | ID API du Canvas Step auquel appartient cet événement
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de message de Canvas Step que l’utilisateur a reçue
`gender` | `null,`&nbsp;`string` | [Informations personnellement identifiables] sexe de l’utilisateur
`country` | `null,`&nbsp;`string` | [Informations personnellement identifiables] pays de l’utilisateur
`timezone` | `null,`&nbsp;`string` | fuseau horaire de l’utilisateur
`language` | `null,`&nbsp;`string` | [Informations personnellement identifiables] langue de l’utilisateur
`email_address` | `string` | [Informations personnellement identifiables] adresse e-mail de l’utilisateur
`ip_pool` | `null,`&nbsp;`string` | Ensemble d’IP à partir duquel l’e-mail a été envoyé
`abort_type` | `null,`&nbsp;`string` | type d’abandon, l’un des éléments suivants : `liquid_abort_message`, `quiet_hours`, `rate_limit`
`abort_log` | `null,`&nbsp;`string` | [Informations personnellement identifiables] message du journal décrivant les détails de l’abandon (128 caractères maximum)
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS_MESSAGES_EMAIL_BOUNCE_SHARED {#USERS_MESSAGES_EMAIL_BOUNCE_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID global unique de cet événement
`user_id` | `string` | ID BSON de l’utilisateur qui a effectué cet événement
`external_user_id` | `null,`&nbsp;`string` | [Informations personnellement identifiables] ID utilisateur externe de l’utilisateur
`device_id` | `null,`&nbsp;`string` | `device_id` qui est lié à cet utilisateur si celui-ci est anonyme
`app_group_api_id` | `null,`&nbsp;`string` | ID API du groupe d’apps auquel appartient cet utilisateur
`time` | `int` | horodatage Unix du moment où l’événement s’est produit
`dispatch_id` | `null,`&nbsp;`string` | ID de l’envoi auquel appartient ce message
`send_id` | `null,`&nbsp;`string` | ID d’envoi de message auquel appartient ce message
`campaign_id` | `null,`&nbsp;`string` | ID Braze à usage interne de la campagne à laquelle appartient cet événement
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la campagne à laquelle appartient cet événement
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de message que l’utilisateur a reçue
`canvas_id` | `null,`&nbsp;`string` | ID Braze à usage interne du Canvas auquel appartient cet événement
`canvas_api_id` | `null,`&nbsp;`string` | ID API du Canvas auquel appartient cet événement
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de Canvas à laquelle appartient cet événement
`canvas_step_api_id` | `null,`&nbsp;`string` | ID API du Canvas Step auquel appartient cet événement
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de message de Canvas Step que l’utilisateur a reçue
`gender` | `null,`&nbsp;`string` | [Informations personnellement identifiables] sexe de l’utilisateur
`country` | `null,`&nbsp;`string` | [Informations personnellement identifiables] pays de l’utilisateur
`timezone` | `null,`&nbsp;`string` | fuseau horaire de l’utilisateur
`language` | `null,`&nbsp;`string` | [Informations personnellement identifiables] langue de l’utilisateur
`email_address` | `string` | [Informations personnellement identifiables] adresse e-mail de l’utilisateur
`sending_ip` | `null,`&nbsp;`string` | Adresse IP à partir de laquelle l’e-mail a été envoyé
`ip_pool` | `null,`&nbsp;`string` | Ensemble d’IP à partir duquel l’e-mail a été envoyé
`bounce_reason` | `null,`&nbsp;`string` | [Informations personnellement identifiables] Le code de motif SMTP et le message convivial reçus pour cet événement de rebond
`esp` | `null,`&nbsp;`string` | ESP lié à l’événement (SparkPost ou SendGrid)
`from_domain` | `null,`&nbsp;`string` | domaine d’envoi pour l’e-mail
`is_drop` | `null, boolean` | indicates que cet événement est décompté comme un événement d’abandon
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS_MESSAGES_EMAIL_CLICK_SHARED {#USERS_MESSAGES_EMAIL_CLICK_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID global unique de cet événement
`user_id` | `string` | ID BSON de l’utilisateur qui a effectué cet événement
`external_user_id` | `null,`&nbsp;`string` | [Informations personnellement identifiables] ID utilisateur externe de l’utilisateur
`device_id` | `null,`&nbsp;`string` | `device_id` qui est lié à cet utilisateur si celui-ci est anonyme
`app_group_api_id` | `null,`&nbsp;`string` | ID API du groupe d’apps auquel appartient cet utilisateur
`time` | `int` | horodatage Unix du moment où l’événement s’est produit
`dispatch_id` | `null,`&nbsp;`string` | ID de l’envoi auquel appartient ce message
`send_id` | `null,`&nbsp;`string` | ID d’envoi de message auquel appartient ce message
`campaign_id` | `null,`&nbsp;`string` | ID Braze à usage interne de la campagne à laquelle appartient cet événement
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la campagne à laquelle appartient cet événement
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de message que l’utilisateur a reçue
`canvas_id` | `null,`&nbsp;`string` | ID Braze à usage interne du Canvas auquel appartient cet événement
`canvas_api_id` | `null,`&nbsp;`string` | ID API du Canvas auquel appartient cet événement
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de Canvas à laquelle appartient cet événement
`canvas_step_api_id` | `null,`&nbsp;`string` | ID API du Canvas Step auquel appartient cet événement
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de message de Canvas Step que l’utilisateur a reçue
`gender` | `null,`&nbsp;`string` | [Informations personnellement identifiables] sexe de l’utilisateur
`country` | `null,`&nbsp;`string` | [Informations personnellement identifiables] pays de l’utilisateur
`timezone` | `null,`&nbsp;`string` | fuseau horaire de l’utilisateur
`language` | `null,`&nbsp;`string` | [Informations personnellement identifiables] langue de l’utilisateur
`email_address` | `string` | [Informations personnellement identifiables] adresse e-mail de l’utilisateur
`url` | `null,`&nbsp;`string` | URL sur laquelle l’utilisateur a cliqué
`user_agent` | `null,`&nbsp;`string` | agent utilisateur sur lequel le clic a eu lieu
`ip_pool` | `null,`&nbsp;`string` | Ensemble d’IP à partir duquel l’e-mail a été envoyé
`link_id` | `null,`&nbsp;`string` | ID unique pour le lien sur lequel vous avez cliqué, tel que créé par Braze
`link_alias` | `null,`&nbsp;`string` | alias associé à cet ID de lien
`esp` | `null,`&nbsp;`string` | ESP lié à l’événement (SparkPost ou SendGrid)
`from_domain` | `null,`&nbsp;`string` | domaine d’envoi pour l’e-mail
`is_amp` | `null, boolean` | indicates qu’il s’agit d’un événement AMP
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS_MESSAGES_EMAIL_DELIVERY_SHARED {#USERS_MESSAGES_EMAIL_DELIVERY_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID global unique de cet événement
`user_id` | `string` | ID BSON de l’utilisateur qui a effectué cet événement
`external_user_id` | `null,`&nbsp;`string` | [Informations personnellement identifiables] ID utilisateur externe de l’utilisateur
`device_id` | `null,`&nbsp;`string` | `device_id` qui est lié à cet utilisateur si celui-ci est anonyme
`app_group_api_id` | `null,`&nbsp;`string` | ID API du groupe d’apps auquel appartient cet utilisateur
`time` | `int` | horodatage Unix du moment où l’événement s’est produit
`dispatch_id` | `null,`&nbsp;`string` | ID de l’envoi auquel appartient ce message
`send_id` | `null,`&nbsp;`string` | ID d’envoi de message auquel appartient ce message
`campaign_id` | `null,`&nbsp;`string` | ID Braze à usage interne de la campagne à laquelle appartient cet événement
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la campagne à laquelle appartient cet événement
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de message que l’utilisateur a reçue
`canvas_id` | `null,`&nbsp;`string` | ID Braze à usage interne du Canvas auquel appartient cet événement
`canvas_api_id` | `null,`&nbsp;`string` | ID API du Canvas auquel appartient cet événement
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de Canvas à laquelle appartient cet événement
`canvas_step_api_id` | `null,`&nbsp;`string` | ID API du Canvas Step auquel appartient cet événement
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de message de Canvas Step que l’utilisateur a reçue
`gender` | `null,`&nbsp;`string` | [Informations personnellement identifiables] sexe de l’utilisateur
`country` | `null,`&nbsp;`string` | [Informations personnellement identifiables] pays de l’utilisateur
`timezone` | `null,`&nbsp;`string` | fuseau horaire de l’utilisateur
`language` | `null,`&nbsp;`string` | [Informations personnellement identifiables] langue de l’utilisateur
`email_address` | `string` | [Informations personnellement identifiables] adresse e-mail de l’utilisateur
`sending_ip` | `null,`&nbsp;`string` | Adresse IP à partir de laquelle l’e-mail a été envoyé
`ip_pool` | `null,`&nbsp;`string` | Ensemble d’IP à partir duquel l’e-mail a été envoyé
`esp` | `null,`&nbsp;`string` | ESP lié à l’événement (SparkPost ou SendGrid)
`from_domain` | `null,`&nbsp;`string` | sending domaine pour l’e-mail
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS_MESSAGES_EMAIL_MARKASSPAM_SHARED {#USERS_MESSAGES_EMAIL_MARKASSPAM_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID global unique de cet événement
`user_id` | `string` | ID BSON de l’utilisateur qui a effectué cet événement
`external_user_id` | `null,`&nbsp;`string` | [Informations personnellement identifiables] ID utilisateur externe de l’utilisateur
`device_id` | `null,`&nbsp;`string` | `device_id` qui est lié à cet utilisateur si celui-ci est anonyme
`app_group_api_id` | `null,`&nbsp;`string` | ID API du groupe d’apps auquel appartient cet utilisateur
`time` | `int` | horodatage Unix du moment où l’événement s’est produit
`dispatch_id` | `null,`&nbsp;`string` | ID de l’envoi auquel appartient ce message
`send_id` | `null,`&nbsp;`string` | ID d’envoi de message auquel appartient ce message
`campaign_id` | `null,`&nbsp;`string` | ID Braze à usage interne de la campagne à laquelle appartient cet événement
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la campagne à laquelle appartient cet événement
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de message que l’utilisateur a reçue
`canvas_id` | `null,`&nbsp;`string` | ID Braze à usage interne du Canvas auquel appartient cet événement
`canvas_api_id` | `null,`&nbsp;`string` | ID API du Canvas auquel appartient cet événement
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de Canvas à laquelle appartient cet événement
`canvas_step_api_id` | `null,`&nbsp;`string` | ID API du Canvas Step auquel appartient cet événement
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de message de Canvas Step que l’utilisateur a reçue
`gender` | `null,`&nbsp;`string` | [Informations personnellement identifiables] sexe de l’utilisateur
`country` | `null,`&nbsp;`string` | [Informations personnellement identifiables] pays de l’utilisateur
`timezone` | `null,`&nbsp;`string` | fuseau horaire de l’utilisateur
`language` | `null,`&nbsp;`string` | [Informations personnellement identifiables] langue de l’utilisateur
`email_address` | `string` | [Informations personnellement identifiables] adresse e-mail de l’utilisateur
`user_agent` | `null,`&nbsp;`string` | agent utilisateur sur lequel le signalement de courrier indésirable a eu lieu
`ip_pool` | `null,`&nbsp;`string` | Ensemble d’IP à partir duquel l’e-mail a été envoyé
`esp` | `null,`&nbsp;`string` | ESP lié à l’événement (SparkPost ou SendGrid)
`from_domain` | `null,`&nbsp;`string` | sending domaine pour l’e-mail
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS_MESSAGES_EMAIL_OPEN_SHARED {#USERS_MESSAGES_EMAIL_OPEN_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID global unique de cet événement
`user_id` | `string` | ID BSON de l’utilisateur qui a effectué cet événement
`external_user_id` | `null,`&nbsp;`string` | [Informations personnellement identifiables] ID utilisateur externe de l’utilisateur
`device_id` | `null,`&nbsp;`string` | `device_id` qui est lié à cet utilisateur si celui-ci est anonyme
`app_group_api_id` | `null,`&nbsp;`string` | ID API du groupe d’apps auquel appartient cet utilisateur
`time` | `int` | horodatage Unix du moment où l’événement s’est produit
`dispatch_id` | `null,`&nbsp;`string` | ID de l’envoi auquel appartient ce message
`send_id` | `null,`&nbsp;`string` | ID d’envoi de message auquel appartient ce message
`campaign_id` | `null,`&nbsp;`string` | ID Braze à usage interne de la campagne à laquelle appartient cet événement
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la campagne à laquelle appartient cet événement
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de message que l’utilisateur a reçue
`canvas_id` | `null,`&nbsp;`string` | ID Braze à usage interne du Canvas auquel appartient cet événement
`canvas_api_id` | `null,`&nbsp;`string` | ID API du Canvas auquel appartient cet événement
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de Canvas à laquelle appartient cet événement
`canvas_step_api_id` | `null,`&nbsp;`string` | ID API du Canvas Step auquel appartient cet événement
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de message de Canvas Step que l’utilisateur a reçue
`gender` | `null,`&nbsp;`string` | [Informations personnellement identifiables] sexe de l’utilisateur
`country` | `null,`&nbsp;`string` | [Informations personnellement identifiables] pays de l’utilisateur
`timezone` | `null,`&nbsp;`string` | fuseau horaire de l’utilisateur
`language` | `null,`&nbsp;`string` | [Informations personnellement identifiables] langue de l’utilisateur
`email_address` | `string` | [Informations personnellement identifiables] adresse e-mail de l’utilisateur
`user_agent` | `null,`&nbsp;`string` | agent utilisateur sur lequel l’ouverture a eu lieu
`ip_pool` | `null,`&nbsp;`string` | Ensemble d’IP à partir duquel l’e-mail a été envoyé
`machine_open` | `null,`&nbsp;`string` | Renseigné avec « true » si l’événement d’ouverture est déclenché sans engagement de l’utilisateur, par exemple, par un appareil Apple avec la protection de la confidentialité dans Mail activée. La valeur peut changer au fil du temps pour fournir plus de granularité.
`esp` | `null,`&nbsp;`string` | ESP lié à l’événement (SparkPost ou SendGrid)
`from_domain` | `null,`&nbsp;`string` | domaine d’envoi pour l’e-mail
`is_amp` | `null, boolean` | indicates qu’il s’agit d’un événement AMP
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS_MESSAGES_EMAIL_SEND_SHARED {#USERS_MESSAGES_EMAIL_SEND_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID global unique de cet événement
`user_id` | `string` | ID BSON de l’utilisateur qui a effectué cet événement
`external_user_id` | `null,`&nbsp;`string` | [Informations personnellement identifiables] ID utilisateur externe de l’utilisateur
`device_id` | `null,`&nbsp;`string` | `device_id` qui est lié à cet utilisateur si celui-ci est anonyme
`app_group_api_id` | `null,`&nbsp;`string` | ID API du groupe d’apps auquel appartient cet utilisateur
`time` | `int` | horodatage Unix du moment où l’événement s’est produit
`dispatch_id` | `null,`&nbsp;`string` | ID de l’envoi auquel appartient ce message
`send_id` | `null,`&nbsp;`string` | ID d’envoi de message auquel appartient ce message
`campaign_id` | `null,`&nbsp;`string` | ID Braze à usage interne de la campagne à laquelle appartient cet événement
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la campagne à laquelle appartient cet événement
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de message que l’utilisateur a reçue
`canvas_id` | `null,`&nbsp;`string` | ID Braze à usage interne du Canvas auquel appartient cet événement
`canvas_api_id` | `null,`&nbsp;`string` | ID API du Canvas auquel appartient cet événement
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de Canvas à laquelle appartient cet événement
`canvas_step_api_id` | `null,`&nbsp;`string` | ID API du Canvas Step auquel appartient cet événement
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de message de Canvas Step que l’utilisateur a reçue
`gender` | `null,`&nbsp;`string` | [Informations personnellement identifiables] sexe de l’utilisateur
`country` | `null,`&nbsp;`string` | [Informations personnellement identifiables] pays de l’utilisateur
`timezone` | `null,`&nbsp;`string` | fuseau horaire de l’utilisateur
`language` | `null,`&nbsp;`string` | [Informations personnellement identifiables] langue de l’utilisateur
`email_address` | `string` | [Informations personnellement identifiables] adresse e-mail de l’utilisateur
`ip_pool` | `null,`&nbsp;`string` | Ensemble d’IP à partir duquel l’e-mail a été envoyé
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS_MESSAGES_EMAIL_SOFTBOUNCE_SHARED {#USERS_MESSAGES_EMAIL_SOFTBOUNCE_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID global unique de cet événement
`user_id` | `string` | ID BSON de l’utilisateur qui a effectué cet événement
`external_user_id` | `null,`&nbsp;`string` | [Informations personnellement identifiables] ID utilisateur externe de l’utilisateur
`device_id` | `null,`&nbsp;`string` | `device_id` qui est lié à cet utilisateur si celui-ci est anonyme
`app_group_api_id` | `null,`&nbsp;`string` | ID API du groupe d’apps auquel appartient cet utilisateur
`time` | `int` | horodatage Unix du moment où l’événement s’est produit
`dispatch_id` | `null,`&nbsp;`string` | ID de l’envoi auquel appartient ce message
`send_id` | `null,`&nbsp;`string` | ID d’envoi de message auquel appartient ce message
`campaign_id` | `null,`&nbsp;`string` | ID Braze à usage interne de la campagne à laquelle appartient cet événement
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la campagne à laquelle appartient cet événement
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de message que l’utilisateur a reçue
`canvas_id` | `null,`&nbsp;`string` | ID Braze à usage interne du Canvas auquel appartient cet événement
`canvas_api_id` | `null,`&nbsp;`string` | ID API du Canvas auquel appartient cet événement
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de Canvas à laquelle appartient cet événement
`canvas_step_api_id` | `null,`&nbsp;`string` | ID API du Canvas Step auquel appartient cet événement
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de message de Canvas Step que l’utilisateur a reçue
`gender` | `null,`&nbsp;`string` | [Informations personnellement identifiables] sexe de l’utilisateur
`country` | `null,`&nbsp;`string` | [Informations personnellement identifiables] pays de l’utilisateur
`timezone` | `null,`&nbsp;`string` | fuseau horaire de l’utilisateur
`language` | `null,`&nbsp;`string` | [Informations personnellement identifiables] langue de l’utilisateur
`email_address` | `string` | [Informations personnellement identifiables] adresse e-mail de l’utilisateur
`sending_ip` | `null,`&nbsp;`string` | Adresse IP à partir de laquelle l’e-mail a été envoyé
`ip_pool` | `null,`&nbsp;`string` | Ensemble d’IP à partir duquel l’e-mail a été envoyé
`bounce_reason` | `null,`&nbsp;`string` | [Informations personnellement identifiables] Le code de motif SMTP et le message convivial reçus pour cet événement de rebond
`esp` | `null,`&nbsp;`string` | ESP lié à l’événement (SparkPost ou SendGrid)
`from_domain` | `null,`&nbsp;`string` | sending domaine pour l’e-mail
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED {#USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID global unique de cet événement
`user_id` | `string` | ID BSON de l’utilisateur qui a effectué cet événement
`external_user_id` | `null,`&nbsp;`string` | [Informations personnellement identifiables] ID utilisateur externe de l’utilisateur
`device_id` | `null,`&nbsp;`string` | `device_id` qui est lié à cet utilisateur si celui-ci est anonyme
`app_group_api_id` | `null,`&nbsp;`string` | ID API du groupe d’apps auquel appartient cet utilisateur
`time` | `int` | horodatage Unix du moment où l’événement s’est produit
`dispatch_id` | `null,`&nbsp;`string` | ID de l’envoi auquel appartient ce message
`send_id` | `null,`&nbsp;`string` | ID d’envoi de message auquel appartient ce message
`campaign_id` | `null,`&nbsp;`string` | ID Braze à usage interne de la campagne à laquelle appartient cet événement
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la campagne à laquelle appartient cet événement
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de message que l’utilisateur a reçue
`canvas_id` | `null,`&nbsp;`string` | ID Braze à usage interne du Canvas auquel appartient cet événement
`canvas_api_id` | `null,`&nbsp;`string` | ID API du Canvas auquel appartient cet événement
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de Canvas à laquelle appartient cet événement
`canvas_step_api_id` | `null,`&nbsp;`string` | ID API du Canvas Step auquel appartient cet événement
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de message de Canvas Step que l’utilisateur a reçue
`gender` | `null,`&nbsp;`string` | [Informations personnellement identifiables] sexe de l’utilisateur
`country` | `null,`&nbsp;`string` | [Informations personnellement identifiables] pays de l’utilisateur
`timezone` | `null,`&nbsp;`string` | fuseau horaire de l’utilisateur
`language` | `null,`&nbsp;`string` | [Informations personnellement identifiables] langue de l’utilisateur
`email_address` | `string` | [Informations personnellement identifiables] adresse e-mail de l’utilisateur
`ip_pool` | `null,`&nbsp;`string` | Ensemble d’IP à partir duquel l’e-mail a été envoyé
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS_MESSAGES_INAPPMESSAGE_ABORT_SHARED {#USERS_MESSAGES_INAPPMESSAGE_ABORT_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID global unique de cet événement
`user_id` | `string` | ID BSON de l’utilisateur qui a effectué cet événement
`external_user_id` | `null,`&nbsp;`string` | [Informations personnellement identifiables] ID utilisateur externe de l’utilisateur
`app_group_api_id` | `null,`&nbsp;`string` | ID API du groupe d’apps auquel appartient cet utilisateur
`time` | `int` | horodatage Unix du moment où l’événement s’est produit
`app_api_id` | `null,`&nbsp;`string` | ID API de l’application sur laquelle cet événement s’est produit
`card_api_id` | `null,`&nbsp;`string` | ID API de la carte
`dispatch_id` | `null,`&nbsp;`string` | ID de l’envoi auquel appartient ce message
`send_id` | `null,`&nbsp;`string` | ID d’envoi de message auquel appartient ce message
`campaign_id` | `null,`&nbsp;`string` | ID Braze à usage interne de la campagne à laquelle appartient cet événement
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la campagne à laquelle appartient cet événement
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de message que l’utilisateur a reçue
`canvas_id` | `null,`&nbsp;`string` | ID Braze à usage interne du Canvas auquel appartient cet événement
`canvas_api_id` | `null,`&nbsp;`string` | ID API du Canvas auquel appartient cet événement
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de Canvas à laquelle appartient cet événement
`canvas_step_api_id` | `null,`&nbsp;`string` | ID API du Canvas Step auquel appartient cet événement
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de message de Canvas Step que l’utilisateur a reçue
`gender` | `null,`&nbsp;`string` | [Informations personnellement identifiables] sexe de l’utilisateur
`country` | `null,`&nbsp;`string` | [Informations personnellement identifiables] pays de l’utilisateur
`timezone` | `null,`&nbsp;`string` | fuseau horaire de l’utilisateur
`language` | `null,`&nbsp;`string` | [Informations personnellement identifiables] langue de l’utilisateur
`device_id` | `null,`&nbsp;`string` | ID de l’appareil sur lequel l’événement s’est produit
`sdk_version` | `null,`&nbsp;`string` | version du SDK Braze utilisée pendant l’événement
`platform` | `null,`&nbsp;`string` | plateforme de l’appareil
`os_version` | `null,`&nbsp;`string` | version du système d’exploitation de l’appareil
`device_model` | `null,`&nbsp;`string` | modèle de l’appareil
`resolution` | `null,`&nbsp;`string` | résolution de l’appareil
`carrier` | `null,`&nbsp;`string` | transporteur de l’appareil
`browser` | `null,`&nbsp;`string` | navigateur de l’appareil
`version` | `string` | quelle version du message in-app, héritée ou déclenchée
`ad_id` | `null,`&nbsp;`string` | [Informations personnellement identifiables] Identifiant publicitaire
`ad_id_type` | `null,`&nbsp;`string` | Un parmi `ios_idfa`, `google_ad_id`, `windows_ad_id` OU `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Si le suivi publicitaire est activé pour l’appareil ou non
`abort_type` | `null,`&nbsp;`string` | type d’abandon, l’un des éléments suivants : `liquid_abort_message`, `quiet_hours`, `rate_limit`
`abort_log` | `null,`&nbsp;`string` | [Informations personnellement identifiables] message du journal décrivant les détails de l’abandon (128 caractères maximum)
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS_MESSAGES_INAPPMESSAGE_CLICK_SHARED {#USERS_MESSAGES_INAPPMESSAGE_CLICK_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID global unique de cet événement
`user_id` | `string` | ID BSON de l’utilisateur qui a effectué cet événement
`external_user_id` | `null,`&nbsp;`string` | [Informations personnellement identifiables] ID utilisateur externe de l’utilisateur
`app_group_api_id` | `null,`&nbsp;`string` | ID API du groupe d’apps auquel appartient cet utilisateur
`time` | `int` | horodatage Unix du moment où l’événement s’est produit
`app_api_id` | `null,`&nbsp;`string` | ID API de l’application sur laquelle cet événement s’est produit
`card_api_id` | `null,`&nbsp;`string` | ID API de la carte
`dispatch_id` | `null,`&nbsp;`string` | ID de l’envoi auquel appartient ce message
`send_id` | `null,`&nbsp;`string` | ID d’envoi de message auquel appartient ce message
`campaign_id` | `null,`&nbsp;`string` | ID Braze à usage interne de la campagne à laquelle appartient cet événement
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la campagne à laquelle appartient cet événement
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de message que l’utilisateur a reçue
`canvas_id` | `null,`&nbsp;`string` | ID Braze à usage interne du Canvas auquel appartient cet événement
`canvas_api_id` | `null,`&nbsp;`string` | ID API du Canvas auquel appartient cet événement
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de Canvas à laquelle appartient cet événement
`canvas_step_api_id` | `null,`&nbsp;`string` | ID API du Canvas Step auquel appartient cet événement
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de message de Canvas Step que l’utilisateur a reçue
`gender` | `null,`&nbsp;`string` | [Informations personnellement identifiables] sexe de l’utilisateur
`country` | `null,`&nbsp;`string` | [Informations personnellement identifiables] pays de l’utilisateur
`timezone` | `null,`&nbsp;`string` | fuseau horaire de l’utilisateur
`language` | `null,`&nbsp;`string` | [Informations personnellement identifiables] langue de l’utilisateur
`device_id` | `null,`&nbsp;`string` | ID de l’appareil sur lequel l’événement s’est produit
`sdk_version` | `null,`&nbsp;`string` | version du SDK Braze utilisée pendant l’événement
`platform` | `null,`&nbsp;`string` | plateforme de l’appareil
`os_version` | `null,`&nbsp;`string` | version du système d’exploitation de l’appareil
`device_model` | `null,`&nbsp;`string` | modèle de l’appareil
`resolution` | `null,`&nbsp;`string` | résolution de l’appareil
`carrier` | `null,`&nbsp;`string` | transporteur de l’appareil
`browser` | `null,`&nbsp;`string` | navigateur de l’appareil
`version` | `string` | quelle version du message in-app, héritée ou déclenchée
`button_id` | `null,`&nbsp;`string` | ID du bouton cliqué, si ce clic représente un clic sur un bouton
`ad_id` | `null,`&nbsp;`string` | [Informations personnellement identifiables] Identifiant publicitaire
`ad_id_type` | `null,`&nbsp;`string` | Un parmi `ios_idfa`, `google_ad_id`, `windows_ad_id` OU `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Si le suivi publicitaire est activé pour l’appareil ou non
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS_MESSAGES_INAPPMESSAGE_IMPRESSION_SHARED {#USERS_MESSAGES_INAPPMESSAGE_IMPRESSION_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID global unique de cet événement
`user_id` | `string` | ID BSON de l’utilisateur qui a effectué cet événement
`external_user_id` | `null,`&nbsp;`string` | [Informations personnellement identifiables] ID utilisateur externe de l’utilisateur
`app_group_api_id` | `null,`&nbsp;`string` | ID API du groupe d’apps auquel appartient cet utilisateur
`time` | `int` | horodatage Unix du moment où l’événement s’est produit
`app_api_id` | `null,`&nbsp;`string` | ID API de l’application sur laquelle cet événement s’est produit
`card_api_id` | `null,`&nbsp;`string` | ID API de la carte
`dispatch_id` | `null,`&nbsp;`string` | ID de l’envoi auquel appartient ce message
`send_id` | `null,`&nbsp;`string` | ID d’envoi de message auquel appartient ce message
`campaign_id` | `null,`&nbsp;`string` | ID Braze à usage interne de la campagne à laquelle appartient cet événement
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la campagne à laquelle appartient cet événement
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de message que l’utilisateur a reçue
`canvas_id` | `null,`&nbsp;`string` | ID Braze à usage interne du Canvas auquel appartient cet événement
`canvas_api_id` | `null,`&nbsp;`string` | ID API du Canvas auquel appartient cet événement
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de Canvas à laquelle appartient cet événement
`canvas_step_api_id` | `null,`&nbsp;`string` | ID API du Canvas Step auquel appartient cet événement
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de message de Canvas Step que l’utilisateur a reçue
`gender` | `null,`&nbsp;`string` | [Informations personnellement identifiables] sexe de l’utilisateur
`country` | `null,`&nbsp;`string` | [Informations personnellement identifiables] pays de l’utilisateur
`timezone` | `null,`&nbsp;`string` | fuseau horaire de l’utilisateur
`language` | `null,`&nbsp;`string` | [Informations personnellement identifiables] langue de l’utilisateur
`device_id` | `null,`&nbsp;`string` | ID de l’appareil sur lequel l’événement s’est produit
`sdk_version` | `null,`&nbsp;`string` | version du SDK Braze utilisée pendant l’événement
`platform` | `null,`&nbsp;`string` | plateforme de l’appareil
`os_version` | `null,`&nbsp;`string` | version du système d’exploitation de l’appareil
`device_model` | `null,`&nbsp;`string` | modèle de l’appareil
`resolution` | `null,`&nbsp;`string` | résolution de l’appareil
`carrier` | `null,`&nbsp;`string` | transporteur de l’appareil
`browser` | `null,`&nbsp;`string` | navigateur de l’appareil
`version` | `string` | quelle version du message in-app, héritée ou déclenchée
`ad_id` | `null,`&nbsp;`string` | [Informations personnellement identifiables] Identifiant publicitaire
`ad_id_type` | `null,`&nbsp;`string` | Un parmi `ios_idfa`, `google_ad_id`, `windows_ad_id` OU `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Si le suivi publicitaire est activé pour l’appareil ou non
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS_MESSAGES_NEWSFEEDCARD_ABORT_SHARED {#USERS_MESSAGES_NEWSFEEDCARD_ABORT_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID global unique de cet événement
`user_id` | `string` | ID BSON de l’utilisateur qui a effectué cet événement
`external_user_id` | `null,`&nbsp;`string` | [Informations personnellement identifiables] ID utilisateur externe de l’utilisateur
`app_group_api_id` | `null,`&nbsp;`string` | ID API du groupe d’apps auquel appartient cet utilisateur
`time` | `int` | horodatage Unix du moment où l’événement s’est produit
`app_api_id` | `null,`&nbsp;`string` | ID API de l’application sur laquelle cet événement s’est produit
`card_api_id` | `null,`&nbsp;`string` | ID API de la carte
`gender` | `null,`&nbsp;`string` | [Informations personnellement identifiables] sexe de l’utilisateur
`country` | `null,`&nbsp;`string` | [Informations personnellement identifiables] pays de l’utilisateur
`timezone` | `null,`&nbsp;`string` | fuseau horaire de l’utilisateur
`language` | `null,`&nbsp;`string` | [Informations personnellement identifiables] langue de l’utilisateur
`device_id` | `null,`&nbsp;`string` | ID de l’appareil sur lequel l’événement s’est produit
`sdk_version` | `null,`&nbsp;`string` | version du SDK Braze utilisée pendant l’événement
`platform` | `null,`&nbsp;`string` | plateforme de l’appareil
`os_version` | `null,`&nbsp;`string` | version du système d’exploitation de l’appareil
`device_model` | `null,`&nbsp;`string` | modèle de l’appareil
`resolution` | `null,`&nbsp;`string` | résolution de l’appareil
`carrier` | `null,`&nbsp;`string` | transporteur de l’appareil
`browser` | `null,`&nbsp;`string` | navigateur de l’appareil
`abort_type` | `null,`&nbsp;`string` | type d’abandon, l’un des éléments suivants : `liquid_abort_message`, `quiet_hours`, `rate_limit`
`abort_log` | `null,`&nbsp;`string` | [Informations personnellement identifiables] message du journal décrivant les détails de l’abandon (128 caractères maximum)
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS_MESSAGES_NEWSFEEDCARD_CLICK_SHARED {#USERS_MESSAGES_NEWSFEEDCARD_CLICK_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID global unique de cet événement
`user_id` | `string` | ID BSON de l’utilisateur qui a effectué cet événement
`external_user_id` | `null,`&nbsp;`string` | [Informations personnellement identifiables] ID utilisateur externe de l’utilisateur
`app_group_api_id` | `null,`&nbsp;`string` | ID API du groupe d’apps auquel appartient cet utilisateur
`time` | `int` | horodatage Unix du moment où l’événement s’est produit
`app_api_id` | `null,`&nbsp;`string` | ID API de l’application sur laquelle cet événement s’est produit
`card_api_id` | `null,`&nbsp;`string` | ID API de la carte
`gender` | `null,`&nbsp;`string` | [Informations personnellement identifiables] sexe de l’utilisateur
`country` | `null,`&nbsp;`string` | [Informations personnellement identifiables] pays de l’utilisateur
`timezone` | `null,`&nbsp;`string` | fuseau horaire de l’utilisateur
`language` | `null,`&nbsp;`string` | [Informations personnellement identifiables] langue de l’utilisateur
`device_id` | `null,`&nbsp;`string` | ID de l’appareil sur lequel l’événement s’est produit
`sdk_version` | `null,`&nbsp;`string` | version du SDK Braze utilisée pendant l’événement
`platform` | `null,`&nbsp;`string` | plateforme de l’appareil
`os_version` | `null,`&nbsp;`string` | version du système d’exploitation de l’appareil
`device_model` | `null,`&nbsp;`string` | modèle de l’appareil
`resolution` | `null,`&nbsp;`string` | résolution de l’appareil
`carrier` | `null,`&nbsp;`string` | transporteur de l’appareil
`browser` | `null,`&nbsp;`string` | browser de l’appareil
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS_MESSAGES_NEWSFEEDCARD_IMPRESSION_SHARED {#USERS_MESSAGES_NEWSFEEDCARD_IMPRESSION_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID global unique de cet événement
`user_id` | `string` | ID BSON de l’utilisateur qui a effectué cet événement
`external_user_id` | `null,`&nbsp;`string` | [Informations personnellement identifiables] ID utilisateur externe de l’utilisateur
`app_group_api_id` | `null,`&nbsp;`string` | ID API du groupe d’apps auquel appartient cet utilisateur
`time` | `int` | horodatage Unix du moment où l’événement s’est produit
`app_api_id` | `null,`&nbsp;`string` | ID API de l’application sur laquelle cet événement s’est produit
`card_api_id` | `null,`&nbsp;`string` | ID API de la carte
`gender` | `null,`&nbsp;`string` | [Informations personnellement identifiables] sexe de l’utilisateur
`country` | `null,`&nbsp;`string` | [Informations personnellement identifiables] pays de l’utilisateur
`timezone` | `null,`&nbsp;`string` | fuseau horaire de l’utilisateur
`language` | `null,`&nbsp;`string` | [Informations personnellement identifiables] langue de l’utilisateur
`device_id` | `null,`&nbsp;`string` | ID de l’appareil sur lequel l’événement s’est produit
`sdk_version` | `null,`&nbsp;`string` | version du SDK Braze utilisée pendant l’événement
`platform` | `null,`&nbsp;`string` | plateforme de l’appareil
`os_version` | `null,`&nbsp;`string` | version du système d’exploitation de l’appareil
`device_model` | `null,`&nbsp;`string` | modèle de l’appareil
`resolution` | `null,`&nbsp;`string` | résolution de l’appareil
`carrier` | `null,`&nbsp;`string` | transporteur de l’appareil
`browser` | `null,`&nbsp;`string` | browser de l’appareil
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS_MESSAGES_PUSHNOTIFICATION_ABORT_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_ABORT_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID global unique de cet événement
`user_id` | `string` | ID BSON de l’utilisateur qui a effectué cet événement
`external_user_id` | `null,`&nbsp;`string` | [Informations personnellement identifiables] ID utilisateur externe de l’utilisateur
`device_id` | `null,`&nbsp;`string` | `device_id` auquel nous avons fait une tentative de livraison
`app_group_api_id` | `null,`&nbsp;`string` | ID API du groupe d’apps auquel appartient cet utilisateur
`time` | `int` | horodatage Unix du moment où l’événement s’est produit
`app_api_id` | `null,`&nbsp;`string` | ID API de l’application sur laquelle cet événement s’est produit
`dispatch_id` | `null,`&nbsp;`string` | ID de l’envoi auquel appartient ce message
`send_id` | `null,`&nbsp;`string` | ID d’envoi de message auquel appartient ce message
`campaign_id` | `null,`&nbsp;`string` | ID Braze à usage interne de la campagne à laquelle appartient cet événement
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la campagne à laquelle appartient cet événement
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de message que l’utilisateur a reçue
`canvas_id` | `null,`&nbsp;`string` | ID Braze à usage interne du Canvas auquel appartient cet événement
`canvas_api_id` | `null,`&nbsp;`string` | ID API du Canvas auquel appartient cet événement
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de Canvas à laquelle appartient cet événement
`canvas_step_api_id` | `null,`&nbsp;`string` | ID API du Canvas Step auquel appartient cet événement
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de message de Canvas Step que l’utilisateur a reçue
`gender` | `null,`&nbsp;`string` | [Informations personnellement identifiables] sexe de l’utilisateur
`country` | `null,`&nbsp;`string` | [Informations personnellement identifiables] pays de l’utilisateur
`timezone` | `null,`&nbsp;`string` | fuseau horaire de l’utilisateur
`language` | `null,`&nbsp;`string` | [Informations personnellement identifiables] langue de l’utilisateur
`platform` | `string` | plateforme de l’appareil
`abort_type` | `null,`&nbsp;`string` | type d’abandon, l’un des éléments suivants : `liquid_abort_message`, `quiet_hours`, `rate_limit`
`abort_log` | `null,`&nbsp;`string` | [Informations personnellement identifiables] message du journal décrivant les détails de l’abandon (128 caractères maximum)
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS_MESSAGES_PUSHNOTIFICATION_BOUNCE_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_BOUNCE_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID global unique de cet événement
`user_id` | `string` | ID BSON de l’utilisateur qui a effectué cet événement
`external_user_id` | `null,`&nbsp;`string` | [Informations personnellement identifiables] ID utilisateur externe de l’utilisateur
`push_token` | `null,`&nbsp;`string` | jeton de notification push qui a rebondi
`device_id` | `null,`&nbsp;`string` | `device_id` auquel nous avons fait une tentative de livraison qui a rebondi
`app_group_api_id` | `null,`&nbsp;`string` | ID API du groupe d’apps auquel appartient cet utilisateur
`time` | `int` | horodatage Unix du moment où l’événement s’est produit
`app_api_id` | `null,`&nbsp;`string` | ID API de l’application sur laquelle cet événement s’est produit
`dispatch_id` | `null,`&nbsp;`string` | ID de l’envoi auquel appartient ce message
`send_id` | `null,`&nbsp;`string` | ID d’envoi de message auquel appartient ce message
`campaign_id` | `null,`&nbsp;`string` | ID Braze à usage interne de la campagne à laquelle appartient cet événement
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la campagne à laquelle appartient cet événement
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de message que l’utilisateur a reçue
`canvas_id` | `null,`&nbsp;`string` | ID Braze à usage interne du Canvas auquel appartient cet événement
`canvas_api_id` | `null,`&nbsp;`string` | ID API du Canvas auquel appartient cet événement
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de Canvas à laquelle appartient cet événement
`canvas_step_api_id` | `null,`&nbsp;`string` | ID API du Canvas Step auquel appartient cet événement
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de message de Canvas Step que l’utilisateur a reçue
`gender` | `null,`&nbsp;`string` | [Informations personnellement identifiables] sexe de l’utilisateur
`country` | `null,`&nbsp;`string` | [Informations personnellement identifiables] pays de l’utilisateur
`timezone` | `null,`&nbsp;`string` | fuseau horaire de l’utilisateur
`language` | `null,`&nbsp;`string` | [Informations personnellement identifiables] langue de l’utilisateur
`platform` | `null,`&nbsp;`string` | plateforme de l’appareil
`ad_id` | `null,`&nbsp;`string` | [Informations personnellement identifiables] ID publicitaire de l’appareil auquel nous avons essayé de livrer
`ad_id_type` | `null,`&nbsp;`string` | type de l’identifiant publicitaire
`ad_tracking_enabled` | `null, boolean` | whether ou l’absence de suivi est activée pour la publicité
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS_MESSAGES_PUSHNOTIFICATION_INFLUENCEDOPEN_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_INFLUENCEDOPEN_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID global unique de cet événement
`user_id` | `string` | ID BSON de l’utilisateur qui a effectué cet événement
`external_user_id` | `null,`&nbsp;`string` | [Informations personnellement identifiables] ID utilisateur externe de l’utilisateur
`app_group_api_id` | `null,`&nbsp;`string` | ID API du groupe d’apps auquel appartient cet utilisateur
`time` | `int` | horodatage Unix du moment où l’événement s’est produit
`app_api_id` | `null,`&nbsp;`string` | ID API de l’application sur laquelle cet événement s’est produit
`dispatch_id` | `null,`&nbsp;`string` | ID de l’envoi auquel appartient ce message
`send_id` | `null,`&nbsp;`string` | ID d’envoi de message auquel appartient ce message
`campaign_id` | `null,`&nbsp;`string` | ID Braze à usage interne de la campagne à laquelle appartient cet événement
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la campagne à laquelle appartient cet événement
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de message que l’utilisateur a reçue
`canvas_id` | `null,`&nbsp;`string` | ID Braze à usage interne du Canvas auquel appartient cet événement
`canvas_api_id` | `null,`&nbsp;`string` | ID API du Canvas auquel appartient cet événement
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de Canvas à laquelle appartient cet événement
`canvas_step_api_id` | `null,`&nbsp;`string` | ID API du Canvas Step auquel appartient cet événement
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de message de Canvas Step que l’utilisateur a reçue
`gender` | `null,`&nbsp;`string` | [Informations personnellement identifiables] sexe de l’utilisateur
`country` | `null,`&nbsp;`string` | [Informations personnellement identifiables] pays de l’utilisateur
`timezone` | `null,`&nbsp;`string` | fuseau horaire de l’utilisateur
`language` | `null,`&nbsp;`string` | [Informations personnellement identifiables] langue de l’utilisateur
`device_id` | `null,`&nbsp;`string` | ID de l’appareil sur lequel l’événement s’est produit
`sdk_version` | `null,`&nbsp;`string` | version du SDK Braze utilisée pendant l’événement
`platform` | `null,`&nbsp;`string` | plateforme de l’appareil
`os_version` | `null,`&nbsp;`string` | version du système d’exploitation de l’appareil
`device_model` | `null,`&nbsp;`string` | modèle de l’appareil
`resolution` | `null,`&nbsp;`string` | résolution de l’appareil
`carrier` | `null,`&nbsp;`string` | transporteur de l’appareil
`browser` | `null,`&nbsp;`string` | browser de l’appareil
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS_MESSAGES_PUSHNOTIFICATION_IOSFOREGROUND_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_IOSFOREGROUND_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID global unique de cet événement
`user_id` | `string` | ID BSON de l’utilisateur qui a effectué cet événement
`external_user_id` | `null,`&nbsp;`string` | [Informations personnellement identifiables] ID utilisateur externe de l’utilisateur
`app_group_api_id` | `null,`&nbsp;`string` | ID API du groupe d’apps auquel appartient cet utilisateur
`time` | `int` | horodatage Unix du moment où l’événement s’est produit
`app_api_id` | `null,`&nbsp;`string` | ID API de l’application sur laquelle cet événement s’est produit
`dispatch_id` | `null,`&nbsp;`string` | ID de l’envoi auquel appartient ce message
`send_id` | `null,`&nbsp;`string` | ID d’envoi de message auquel appartient ce message
`campaign_id` | `null,`&nbsp;`string` | ID Braze à usage interne de la campagne à laquelle appartient cet événement
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la campagne à laquelle appartient cet événement
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de message que l’utilisateur a reçue
`canvas_id` | `null,`&nbsp;`string` | ID Braze à usage interne du Canvas auquel appartient cet événement
`canvas_api_id` | `null,`&nbsp;`string` | ID API du Canvas auquel appartient cet événement
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de Canvas à laquelle appartient cet événement
`canvas_step_api_id` | `null,`&nbsp;`string` | ID API du Canvas Step auquel appartient cet événement
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de message de Canvas Step que l’utilisateur a reçue
`gender` | `null,`&nbsp;`string` | [Informations personnellement identifiables] sexe de l’utilisateur
`country` | `null,`&nbsp;`string` | [Informations personnellement identifiables] pays de l’utilisateur
`timezone` | `null,`&nbsp;`string` | fuseau horaire de l’utilisateur
`language` | `null,`&nbsp;`string` | [Informations personnellement identifiables] langue de l’utilisateur
`device_id` | `null,`&nbsp;`string` | ID de l’appareil sur lequel l’événement s’est produit
`sdk_version` | `null,`&nbsp;`string` | version du SDK Braze utilisée pendant l’événement
`platform` | `null,`&nbsp;`string` | plateforme de l’appareil
`os_version` | `null,`&nbsp;`string` | version du système d’exploitation de l’appareil
`device_model` | `null,`&nbsp;`string` | modèle de l’appareil
`resolution` | `null,`&nbsp;`string` | résolution de l’appareil
`carrier` | `null,`&nbsp;`string` | transporteur de l’appareil
`browser` | `null,`&nbsp;`string` | navigateur de l’appareil
`ad_id` | `null,`&nbsp;`string` | [Informations personnellement identifiables] ID publicitaire de l’appareil auquel nous avons essayé de livrer
`ad_id_type` | `null,`&nbsp;`string` | type de l’identifiant publicitaire
`ad_tracking_enabled` | `null, boolean` | whether ou l’absence de suivi est activée pour la publicité
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS_MESSAGES_PUSHNOTIFICATION_OPEN_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_OPEN_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID global unique de cet événement
`user_id` | `string` | ID BSON de l’utilisateur qui a effectué cet événement
`external_user_id` | `null,`&nbsp;`string` | [Informations personnellement identifiables] ID utilisateur externe de l’utilisateur
`app_group_api_id` | `null,`&nbsp;`string` | ID API du groupe d’apps auquel appartient cet utilisateur
`time` | `int` | horodatage Unix du moment où l’événement s’est produit
`app_api_id` | `null,`&nbsp;`string` | ID API de l’application sur laquelle cet événement s’est produit
`dispatch_id` | `null,`&nbsp;`string` | ID de l’envoi auquel appartient ce message
`send_id` | `null,`&nbsp;`string` | ID d’envoi de message auquel appartient ce message
`campaign_id` | `null,`&nbsp;`string` | ID Braze à usage interne de la campagne à laquelle appartient cet événement
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la campagne à laquelle appartient cet événement
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de message que l’utilisateur a reçue
`canvas_id` | `null,`&nbsp;`string` | ID Braze à usage interne du Canvas auquel appartient cet événement
`canvas_api_id` | `null,`&nbsp;`string` | ID API du Canvas auquel appartient cet événement
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de Canvas à laquelle appartient cet événement
`canvas_step_api_id` | `null,`&nbsp;`string` | ID API du Canvas Step auquel appartient cet événement
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de message de Canvas Step que l’utilisateur a reçue
`gender` | `null,`&nbsp;`string` | [Informations personnellement identifiables] sexe de l’utilisateur
`country` | `null,`&nbsp;`string` | [Informations personnellement identifiables] pays de l’utilisateur
`timezone` | `null,`&nbsp;`string` | fuseau horaire de l’utilisateur
`language` | `null,`&nbsp;`string` | [Informations personnellement identifiables] langue de l’utilisateur
`device_id` | `null,`&nbsp;`string` | ID de l’appareil sur lequel l’événement s’est produit
`sdk_version` | `null,`&nbsp;`string` | version du SDK Braze utilisée pendant l’événement
`platform` | `null,`&nbsp;`string` | plateforme de l’appareil
`os_version` | `null,`&nbsp;`string` | version du système d’exploitation de l’appareil
`device_model` | `null,`&nbsp;`string` | modèle de l’appareil
`resolution` | `null,`&nbsp;`string` | résolution de l’appareil
`carrier` | `null,`&nbsp;`string` | transporteur de l’appareil
`browser` | `null,`&nbsp;`string` | navigateur de l’appareil
`button_string` | `null,`&nbsp;`string` | identifiant (button_string) du bouton cliqué de la notification push. Vide si ne provient pas d’un clic de bouton
`button_action_type` | `null,`&nbsp;`string` | Type d’action du bouton de la notification push. Un parmi [URI, DEEP_LINK, NONE, CLOSE, SHARE]. Vide si ne provient pas d’un clic de bouton
`slide_id` | `null,`&nbsp;`string` | identifiant de diapositive de la diapositive de carrousel de notification push sur laquelle l’utilisateur a cliqué
`slide_action_type` | `null,`&nbsp;`string` | type d’action de la diapositive de carrousel de notification push
`ad_id` | `null,`&nbsp;`string` | [Informations personnellement identifiables] ID publicitaire de l’appareil auquel nous avons essayé de livrer
`ad_id_type` | `null,`&nbsp;`string` | type de l’identifiant publicitaire
`ad_tracking_enabled` | `null, boolean` | whether ou l’absence de suivi est activée pour la publicité
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS_MESSAGES_PUSHNOTIFICATION_SEND_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_SEND_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID global unique de cet événement
`user_id` | `string` | ID BSON de l’utilisateur qui a effectué cet événement
`external_user_id` | `null,`&nbsp;`string` | [Informations personnellement identifiables] ID utilisateur externe de l’utilisateur
`push_token` | `null,`&nbsp;`string` | jeton de notification push auquel nous avons fait une tentative de livraison
`device_id` | `null,`&nbsp;`string` | `device_id` auquel nous avons fait une tentative de livraison
`app_group_api_id` | `null,`&nbsp;`string` | ID API du groupe d’apps auquel appartient cet utilisateur
`time` | `int` | horodatage Unix du moment où l’événement s’est produit
`app_api_id` | `null,`&nbsp;`string` | ID API de l’application sur laquelle cet événement s’est produit
`dispatch_id` | `null,`&nbsp;`string` | ID de l’envoi auquel appartient ce message
`send_id` | `null,`&nbsp;`string` | ID d’envoi de message auquel appartient ce message
`campaign_id` | `null,`&nbsp;`string` | ID Braze à usage interne de la campagne à laquelle appartient cet événement
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la campagne à laquelle appartient cet événement
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de message que l’utilisateur a reçue
`canvas_id` | `null,`&nbsp;`string` | ID Braze à usage interne du Canvas auquel appartient cet événement
`canvas_api_id` | `null,`&nbsp;`string` | ID API du Canvas auquel appartient cet événement
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de Canvas à laquelle appartient cet événement
`canvas_step_api_id` | `null,`&nbsp;`string` | ID API du Canvas Step auquel appartient cet événement
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de message de Canvas Step que l’utilisateur a reçue
`gender` | `null,`&nbsp;`string` | [Informations personnellement identifiables] sexe de l’utilisateur
`country` | `null,`&nbsp;`string` | [Informations personnellement identifiables] pays de l’utilisateur
`timezone` | `null,`&nbsp;`string` | fuseau horaire de l’utilisateur
`language` | `null,`&nbsp;`string` | [Informations personnellement identifiables] langue de l’utilisateur
`platform` | `string` | plateforme de l’appareil
`ad_id` | `null,`&nbsp;`string` | [Informations personnellement identifiables] ID publicitaire de l’appareil auquel nous avons essayé de livrer
`ad_id_type` | `null,`&nbsp;`string` | type de l’identifiant publicitaire
`ad_tracking_enabled` | `null, boolean` | whether ou l’absence de suivi est activée pour la publicité
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS_MESSAGES_SMS_ABORT_SHARED {#USERS_MESSAGES_SMS_ABORT_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID global unique de cet événement
`user_id` | `string` | ID BSON de l’utilisateur qui a effectué cet événement
`external_user_id` | `null,`&nbsp;`string` | [Informations personnellement identifiables] ID utilisateur externe de l’utilisateur
`app_group_api_id` | `null,`&nbsp;`string` | ID API du groupe d’apps auquel appartient cet utilisateur
`time` | `int` | horodatage Unix du moment où l’événement s’est produit
`campaign_id` | `null,`&nbsp;`string` | ID Braze à usage interne de la campagne à laquelle appartient cet événement
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la campagne à laquelle appartient cet événement
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de message que l’utilisateur a reçue
`canvas_id` | `null,`&nbsp;`string` | ID Braze à usage interne du Canvas auquel appartient cet événement
`canvas_api_id` | `null,`&nbsp;`string` | ID API du Canvas auquel appartient cet événement
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de Canvas à laquelle appartient cet événement
`canvas_step_api_id` | `null,`&nbsp;`string` | ID API du Canvas Step auquel appartient cet événement
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de message de Canvas Step que l’utilisateur a reçue
`subscription_group_api_id` | `null,`&nbsp;`string` | ID externe du groupe d’abonnement
`abort_type` | `null,`&nbsp;`string` | type d’abandon, l’un des éléments suivants : `liquid_abort_message`, `quiet_hours`, `rate_limit`
`abort_log` | `null,`&nbsp;`string` | [Informations personnellement identifiables] message du journal décrivant les détails de l’abandon (128 caractères maximum)
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS_MESSAGES_SMS_CARRIERSEND_SHARED {#USERS_MESSAGES_SMS_CARRIERSEND_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID global unique de cet événement
`user_id` | `string` | ID BSON de l’utilisateur qui a effectué cet événement
`external_user_id` | `null,`&nbsp;`string` | [Informations personnellement identifiables] ID utilisateur externe de l’utilisateur
`device_id` | `null,`&nbsp;`string` | `device_id` qui est lié à cet utilisateur si celui-ci est anonyme
`app_group_api_id` | `null,`&nbsp;`string` | ID API du groupe d’apps auquel appartient cet utilisateur
`time` | `int` | horodatage Unix du moment où l’événement s’est produit
`dispatch_id` | `null,`&nbsp;`string` | ID de l’envoi auquel appartient ce message
`send_id` | `null,`&nbsp;`string` | ID d’envoi de message auquel appartient ce message
`campaign_id` | `null,`&nbsp;`string` | ID Braze à usage interne de la campagne à laquelle appartient cet événement
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la campagne à laquelle appartient cet événement
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de message que l’utilisateur a reçue
`canvas_id` | `null,`&nbsp;`string` | ID Braze à usage interne du Canvas auquel appartient cet événement
`canvas_api_id` | `null,`&nbsp;`string` | ID API du Canvas auquel appartient cet événement
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de Canvas à laquelle appartient cet événement
`canvas_step_api_id` | `null,`&nbsp;`string` | ID API du Canvas Step auquel appartient cet événement
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de message de Canvas Step que l’utilisateur a reçue
`gender` | `null,`&nbsp;`string` | [Informations personnellement identifiables] sexe de l’utilisateur
`country` | `null,`&nbsp;`string` | [Informations personnellement identifiables] pays de l’utilisateur
`timezone` | `null,`&nbsp;`string` | fuseau horaire de l’utilisateur
`language` | `null,`&nbsp;`string` | [Informations personnellement identifiables] langue de l’utilisateur
`to_phone_number` | `null,`&nbsp;`string` | [Informations personnellement identifiables] numéro de téléphone du destinataire
`from_phone_number` | `null,`&nbsp;`string` | numéro de téléphone à partir duquel le message SMS a été envoyé
`subscription_group_api_id` | `null,`&nbsp;`string` | external ID du groupe d’abonnement
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS_MESSAGES_SMS_DELIVERY_SHARED {#USERS_MESSAGES_SMS_DELIVERY_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID global unique de cet événement
`user_id` | `string` | ID BSON de l’utilisateur qui a effectué cet événement
`external_user_id` | `null,`&nbsp;`string` | [Informations personnellement identifiables] ID utilisateur externe de l’utilisateur
`device_id` | `null,`&nbsp;`string` | `device_id` qui est lié à cet utilisateur si celui-ci est anonyme
`app_group_api_id` | `null,`&nbsp;`string` | ID API du groupe d’apps auquel appartient cet utilisateur
`time` | `int` | horodatage Unix du moment où l’événement s’est produit
`dispatch_id` | `null,`&nbsp;`string` | ID de l’envoi auquel appartient ce message
`send_id` | `null,`&nbsp;`string` | ID d’envoi de message auquel appartient ce message
`campaign_id` | `null,`&nbsp;`string` | ID Braze à usage interne de la campagne à laquelle appartient cet événement
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la campagne à laquelle appartient cet événement
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de message que l’utilisateur a reçue
`canvas_id` | `null,`&nbsp;`string` | ID Braze à usage interne du Canvas auquel appartient cet événement
`canvas_api_id` | `null,`&nbsp;`string` | ID API du Canvas auquel appartient cet événement
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de Canvas à laquelle appartient cet événement
`canvas_step_api_id` | `null,`&nbsp;`string` | ID API du Canvas Step auquel appartient cet événement
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de message de Canvas Step que l’utilisateur a reçue
`gender` | `null,`&nbsp;`string` | [Informations personnellement identifiables] sexe de l’utilisateur
`country` | `null,`&nbsp;`string` | [Informations personnellement identifiables] pays de l’utilisateur
`timezone` | `null,`&nbsp;`string` | fuseau horaire de l’utilisateur
`language` | `null,`&nbsp;`string` | [Informations personnellement identifiables] langue de l’utilisateur
`to_phone_number` | `null,`&nbsp;`string` | [Informations personnellement identifiables] numéro de téléphone du destinataire
`from_phone_number` | `null,`&nbsp;`string` | numéro de téléphone à partir duquel le message SMS a été envoyé
`subscription_group_api_id` | `null,`&nbsp;`string` | external ID du groupe d’abonnement
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED {#USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID global unique de cet événement
`user_id` | `string` | ID BSON de l’utilisateur qui a effectué cet événement
`external_user_id` | `null,`&nbsp;`string` | [Informations personnellement identifiables] ID utilisateur externe de l’utilisateur
`device_id` | `null,`&nbsp;`string` | `device_id` qui est lié à cet utilisateur si celui-ci est anonyme
`app_group_api_id` | `null,`&nbsp;`string` | ID API du groupe d’apps auquel appartient cet utilisateur
`time` | `int` | horodatage Unix du moment où l’événement s’est produit
`dispatch_id` | `null,`&nbsp;`string` | ID de l’envoi auquel appartient ce message
`send_id` | `null,`&nbsp;`string` | ID d’envoi de message auquel appartient ce message
`campaign_id` | `null,`&nbsp;`string` | ID Braze à usage interne de la campagne à laquelle appartient cet événement
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la campagne à laquelle appartient cet événement
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de message que l’utilisateur a reçue
`canvas_id` | `null,`&nbsp;`string` | ID Braze à usage interne du Canvas auquel appartient cet événement
`canvas_api_id` | `null,`&nbsp;`string` | ID API du Canvas auquel appartient cet événement
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de Canvas à laquelle appartient cet événement
`canvas_step_api_id` | `null,`&nbsp;`string` | ID API du Canvas Step auquel appartient cet événement
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de message de Canvas Step que l’utilisateur a reçue
`gender` | `null,`&nbsp;`string` | [Informations personnellement identifiables] sexe de l’utilisateur
`country` | `null,`&nbsp;`string` | [Informations personnellement identifiables] pays de l’utilisateur
`timezone` | `null,`&nbsp;`string` | fuseau horaire de l’utilisateur
`language` | `null,`&nbsp;`string` | [Informations personnellement identifiables] langue de l’utilisateur
`to_phone_number` | `null,`&nbsp;`string` | [Informations personnellement identifiables] numéro de téléphone du destinataire
`subscription_group_api_id` | `null,`&nbsp;`string` | ID externe du groupe d’abonnement
`error` | `null,`&nbsp;`string` | nom de l’erreur
`provider_error_code` | `null,`&nbsp;`string` | error code du fournisseur de services SMS
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED {#USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID global unique de cet événement
`user_id` | `null,`&nbsp;`string` | ID BSON de l’utilisateur qui a effectué cet événement
`external_user_id` | `null,`&nbsp;`string` | [Informations personnellement identifiables] ID utilisateur externe de l’utilisateur
`app_group_api_id` | `null,`&nbsp;`string` | ID API du groupe d’apps associé au numéro de téléphone entrant
`time` | `int` | horodatage Unix du moment où l’événement s’est produit
`user_phone_number` | `string` | [Informations personnellement identifiables] le numéro de téléphone de l’utilisateur à partir duquel le message a été reçu
`subscription_group_id` | `null,`&nbsp;`string` | ID du groupe d’abonnement ciblé pour ce message SMS
`subscription_group_api_id` | `null,`&nbsp;`string` | ID de l’API du groupe d’abonnement ciblé pour ce message SMS
`inbound_phone_number` | `string` | le numéro entrant auquel le message a été envoyé
`action` | `string` | Action entreprise en réponse à ce message (par ex., Souscrit, Non-abonné ou Aucun).
`message_body` | `string` | réponse de l’utilisateur
`media_urls` | `null, {"type"=>"array", "items"=>["null", "string"]}` | URL multimédias de l’utilisateur
`campaign_id` | `null,`&nbsp;`string` | ID Braze à usage interne de la campagne à laquelle appartient cet événement
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la campagne à laquelle appartient cet événement
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de message à laquelle appartient cet événement
`canvas_id` | `null,`&nbsp;`string` | ID Braze à usage interne du Canvas auquel appartient cet événement
`canvas_api_id` | `null,`&nbsp;`string` | ID API du Canvas auquel appartient cet événement
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de Canvas à laquelle appartient cet événement
`canvas_step_api_id` | `null,`&nbsp;`string` | ID API du Canvas Step auquel appartient cet événement
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation du message d’étape Canvas auquel appartient cet événement
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS_MESSAGES_SMS_REJECTION_SHARED {#USERS_MESSAGES_SMS_REJECTION_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID global unique de cet événement
`user_id` | `string` | ID BSON de l’utilisateur qui a effectué cet événement
`external_user_id` | `null,`&nbsp;`string` | [Informations personnellement identifiables] ID utilisateur externe de l’utilisateur
`device_id` | `null,`&nbsp;`string` | `device_id` qui est lié à cet utilisateur si celui-ci est anonyme
`app_group_api_id` | `null,`&nbsp;`string` | ID API du groupe d’apps auquel appartient cet utilisateur
`time` | `int` | horodatage Unix du moment où l’événement s’est produit
`dispatch_id` | `null,`&nbsp;`string` | ID de l’envoi auquel appartient ce message
`send_id` | `null,`&nbsp;`string` | ID d’envoi de message auquel appartient ce message
`campaign_id` | `null,`&nbsp;`string` | ID Braze à usage interne de la campagne à laquelle appartient cet événement
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la campagne à laquelle appartient cet événement
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de message que l’utilisateur a reçue
`canvas_id` | `null,`&nbsp;`string` | ID Braze à usage interne du Canvas auquel appartient cet événement
`canvas_api_id` | `null,`&nbsp;`string` | ID API du Canvas auquel appartient cet événement
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de Canvas à laquelle appartient cet événement
`canvas_step_api_id` | `null,`&nbsp;`string` | ID API du Canvas Step auquel appartient cet événement
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de message de Canvas Step que l’utilisateur a reçue
`gender` | `null,`&nbsp;`string` | [Informations personnellement identifiables] sexe de l’utilisateur
`country` | `null,`&nbsp;`string` | [Informations personnellement identifiables] pays de l’utilisateur
`timezone` | `null,`&nbsp;`string` | fuseau horaire de l’utilisateur
`language` | `null,`&nbsp;`string` | [Informations personnellement identifiables] langue de l’utilisateur
`to_phone_number` | `null,`&nbsp;`string` | [Informations personnellement identifiables] numéro de téléphone du destinataire
`from_phone_number` | `null,`&nbsp;`string` | numéro de téléphone à partir duquel le message SMS a été envoyé
`subscription_group_api_id` | `null,`&nbsp;`string` | ID externe du groupe d’abonnement
`error` | `null,`&nbsp;`string` | nom de l’erreur
`provider_error_code` | `null,`&nbsp;`string` | error code du fournisseur de services SMS
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS_MESSAGES_SMS_SEND_SHARED {#USERS_MESSAGES_SMS_SEND_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID global unique de cet événement
`user_id` | `string` | ID BSON de l’utilisateur qui a effectué cet événement
`external_user_id` | `null,`&nbsp;`string` | [Informations personnellement identifiables] ID utilisateur externe de l’utilisateur
`device_id` | `null,`&nbsp;`string` | `device_id` qui est lié à cet utilisateur si celui-ci est anonyme
`app_group_api_id` | `null,`&nbsp;`string` | ID API du groupe d’apps auquel appartient cet utilisateur
`time` | `int` | horodatage Unix du moment où l’événement s’est produit
`dispatch_id` | `null,`&nbsp;`string` | ID de l’envoi auquel appartient ce message
`send_id` | `null,`&nbsp;`string` | ID d’envoi de message auquel appartient ce message
`campaign_id` | `null,`&nbsp;`string` | ID Braze à usage interne de la campagne à laquelle appartient cet événement
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la campagne à laquelle appartient cet événement
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de message que l’utilisateur a reçue
`canvas_id` | `null,`&nbsp;`string` | ID Braze à usage interne du Canvas auquel appartient cet événement
`canvas_api_id` | `null,`&nbsp;`string` | ID API du Canvas auquel appartient cet événement
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de Canvas à laquelle appartient cet événement
`canvas_step_api_id` | `null,`&nbsp;`string` | ID API du Canvas Step auquel appartient cet événement
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de message de Canvas Step que l’utilisateur a reçue
`gender` | `null,`&nbsp;`string` | [Informations personnellement identifiables] sexe de l’utilisateur
`country` | `null,`&nbsp;`string` | [Informations personnellement identifiables] pays de l’utilisateur
`timezone` | `null,`&nbsp;`string` | fuseau horaire de l’utilisateur
`language` | `null,`&nbsp;`string` | [Informations personnellement identifiables] langue de l’utilisateur
`to_phone_number` | `null,`&nbsp;`string` | [Informations personnellement identifiables] numéro de téléphone du destinataire
`subscription_group_api_id` | `null,`&nbsp;`string` | ID externe du groupe d’abonnement
`category` | `null,`&nbsp;`string` | Nom de catégorie de mot-clé, uniquement renseigné pour les messages de réponse automatique : ’Abonné’, ’Désabonné’, ’Aide’ ou valeur personnalisée
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED {#USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID global unique de cet événement
`user_id` | `null,`&nbsp;`string` | ID BSON de l’utilisateur ciblé par short_url, nul si la short_url n’a pas utilisé le suivi des clics de l’utilisateur
`external_user_id` | `null,`&nbsp;`string` | [Informations personnellement identifiables] ID externe de l’utilisateur ciblé par short_url s’il existe, nul si la short_url n’a pas utilisé le suivi des clics de l’utilisateur
`app_group_api_id` | `null,`&nbsp;`string` | ID API du groupe d’apps utilisé pour générer la short_url
`time` | `int` | Horodatage Unix du moment où la short_url a été cliqué
`timezone` | `null,`&nbsp;`string` | fuseau horaire de l’utilisateur
`campaign_id` | `null,`&nbsp;`string` | ID BSON de la campagne pour laquelle la short_url a été générée, nul si elle ne provient pas d’une campagne
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la campagne pour laquelle la short_url a été générée, nul si elle ne provient pas d’une campagne
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de message pour laquelle la short_url a été générée, nul si elle ne provient pas d’une campagne
`canvas_id` | `null,`&nbsp;`string` | ID BSON du Canvas pour lequel la short_url a été générée, nul si elle ne provient pas d’un Canvas
`canvas_api_id` | `null,`&nbsp;`string` | ID API du Canvas pour lequel la short_url a été générée, nul si elle ne provient pas d’un Canvas
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation Canvas pour laquelle la short_url a été générée, nul si elle ne provient pas d’un Canvas
`canvas_step_api_id` | `null,`&nbsp;`string` | ID API de l’étape Canvas pour laquelle la short_url a été générée, nul si elle ne provient pas d’un Canvas
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de message de l’étape Canvas pour laquelle la short_url a été générée, nul si elle ne provient pas d’un Canvas
`url` | `string` | URL originale contenue dans le message vers laquelle redirige la short_url
`short_url` | `string` | URL raccourcie qui a été cliquée
`user_agent` | `null,`&nbsp;`string` | agent utilisateur demandant short_url
`user_phone_number` | `string` | [Informations personnellement identifiables] Le numéro de téléphone de l’utilisateur
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS_MESSAGES_WEBHOOK_ABORT_SHARED {#USERS_MESSAGES_WEBHOOK_ABORT_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID global unique de cet événement
`user_id` | `string` | ID BSON de l’utilisateur qui a effectué cet événement
`external_user_id` | `null,`&nbsp;`string` | [Informations personnellement identifiables] ID utilisateur externe de l’utilisateur
`device_id` | `null,`&nbsp;`string` | `device_id` qui est lié à cet utilisateur si celui-ci est anonyme
`app_group_api_id` | `null,`&nbsp;`string` | ID API du groupe d’apps auquel appartient cet utilisateur
`time` | `int` | horodatage Unix du moment où l’événement s’est produit
`dispatch_id` | `null,`&nbsp;`string` | ID de l’envoi auquel appartient ce message
`send_id` | `null,`&nbsp;`string` | ID d’envoi de message auquel appartient ce message
`campaign_id` | `null,`&nbsp;`string` | ID Braze à usage interne de la campagne à laquelle appartient cet événement
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la campagne à laquelle appartient cet événement
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de message que l’utilisateur a reçue
`canvas_id` | `null,`&nbsp;`string` | ID Braze à usage interne du Canvas auquel appartient cet événement
`canvas_api_id` | `null,`&nbsp;`string` | ID API du Canvas auquel appartient cet événement
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de Canvas à laquelle appartient cet événement
`canvas_step_api_id` | `null,`&nbsp;`string` | ID API du Canvas Step auquel appartient cet événement
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de message de Canvas Step que l’utilisateur a reçue
`gender` | `null,`&nbsp;`string` | [Informations personnellement identifiables] sexe de l’utilisateur
`country` | `null,`&nbsp;`string` | [Informations personnellement identifiables] pays de l’utilisateur
`timezone` | `null,`&nbsp;`string` | fuseau horaire de l’utilisateur
`language` | `null,`&nbsp;`string` | [Informations personnellement identifiables] langue de l’utilisateur
`abort_type` | `null,`&nbsp;`string` | type d’abandon, l’un des éléments suivants : `liquid_abort_message`, `quiet_hours`, `rate_limit`
`abort_log` | `null,`&nbsp;`string` | [Informations personnellement identifiables] message du journal décrivant les détails de l’abandon (128 caractères maximum)
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### USERS_MESSAGES_WEBHOOK_SEND_SHARED {#USERS_MESSAGES_WEBHOOK_SEND_SHARED}

Champ | Type | Description
------|------|------------
`id` | `string` | ID global unique de cet événement
`user_id` | `string` | ID BSON de l’utilisateur qui a effectué cet événement
`external_user_id` | `null,`&nbsp;`string` | [Informations personnellement identifiables] ID utilisateur externe de l’utilisateur
`device_id` | `null,`&nbsp;`string` | `device_id` qui est lié à cet utilisateur si celui-ci est anonyme
`app_group_api_id` | `null,`&nbsp;`string` | ID API du groupe d’apps auquel appartient cet utilisateur
`time` | `int` | horodatage Unix du moment où l’événement s’est produit
`dispatch_id` | `null,`&nbsp;`string` | ID de l’envoi auquel appartient ce message
`send_id` | `null,`&nbsp;`string` | ID d’envoi de message auquel appartient ce message
`campaign_id` | `null,`&nbsp;`string` | ID Braze à usage interne de la campagne à laquelle appartient cet événement
`campaign_api_id` | `null,`&nbsp;`string` | ID API de la campagne à laquelle appartient cet événement
`message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de message que l’utilisateur a reçue
`canvas_id` | `null,`&nbsp;`string` | ID Braze à usage interne du Canvas auquel appartient cet événement
`canvas_api_id` | `null,`&nbsp;`string` | ID API du Canvas auquel appartient cet événement
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de Canvas à laquelle appartient cet événement
`canvas_step_api_id` | `null,`&nbsp;`string` | ID API du Canvas Step auquel appartient cet événement
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID API de la variation de message de Canvas Step que l’utilisateur a reçue
`gender` | `null,`&nbsp;`string` | [Informations personnellement identifiables] sexe de l’utilisateur
`country` | `null,`&nbsp;`string` | [Informations personnellement identifiables] pays de l’utilisateur
`timezone` | `null,`&nbsp;`string` | fuseau horaire de l’utilisateur
`language` | `null,`&nbsp;`string` | [Informations personnellement identifiables] langue de l’utilisateur
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}
