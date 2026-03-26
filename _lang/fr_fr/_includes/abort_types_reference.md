Le tableau suivant répertorie les valeurs possibles de `abort_type`. Un type d'abandon décrit la raison spécifique pour laquelle un message n'a pas été envoyé.

{% if include.channel %}
{% assign ch = include.channel %}
{% else %}
{% assign ch = "all" %}
{% endif %}

### Général

Ces types d'abandon peuvent survenir sur n'importe quel canal de communication.

| Valeur `abort_type` | Description |
| --- | --- |
| `liquid_abort_message` | L'étiquette Liquid [abort_message]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/) a été appelée, l'envoi a donc été annulé. |
| `template_parse_error` | Le modèle de message n'a pas pu être analysé en raison d'une erreur de syntaxe ou de rendu, l'envoi a donc été annulé. |
| `rate_limit` | Le message a été abandonné car il a dépassé la [limite de débit]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/) configurée. |
| `campaign_disabled` | La campagne a été désactivée avant que le message ne puisse être envoyé. |
| `campaign_does_not_exist` | La campagne associée à ce message n'existe plus. |
| `campaign_action_does_not_exist` | L'action de campagne associée à ce message n'existe plus. |
| `message_variation_does_not_exist` | La variante de message attribuée à cet utilisateur n'existe plus. |
| `user_not_in_segment` | L'utilisateur ne fait pas partie du segment cible, le message n'a donc pas été envoyé. |
| `trigger_event_blacklisted` | L'événement déclencheur est sur liste de blocage, le message n'a donc pas été envoyé. |
| `exhausted_retries` | Le message n'a pas pu être envoyé après le nombre maximal de tentatives. |
| `frequency_capped` | L'utilisateur a déjà reçu le nombre maximal de messages autorisé par les règles de [limite de fréquence]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#about-frequency-capping) de votre espace de travail. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% unless ch == "newsfeedcard" or ch == "rcs" %}

### Contenu et rendu

| Valeur `abort_type` | Description |
| --- | --- |
| `exhausted_cc_retries` | Le contenu connecté a échoué après le nombre maximal de tentatives, le message a donc été abandonné. |
| `connected_content_not_supported` | Le [contenu connecté]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/) n'est pas pris en charge dans ce contexte, le message a donc été abandonné. |
| `promo_codes_not_supported` | Les codes de promotion ne sont pas pris en charge dans ce contexte, le message a donc été abandonné. |
| `catalog_items_rerender_not_supported` | Le re-rendu des éléments de catalogue n'est pas pris en charge dans ce contexte, le message a donc été abandonné. |
{% if ch == "all" or ch == "email" or ch == "push" or ch == "inappmessage" or ch == "contentcard" or ch == "webhook" or ch == "banner" %}| `blacklisted_media_url` | L'URL du média est sur liste de blocage et ne peut pas être utilisée dans les messages. |
| `blocked_media_url` | L'URL du média a été bloquée par les politiques de sécurité. |
| `invalid_media_url` | L'URL du média n'est pas valide ou n'a pas pu être résolue. |{% endif %}
{% if ch == "all" or ch == "email" or ch == "webhook" %}| `ssl_error` | Une erreur SSL s'est produite lors de l'exécution d'une requête. |
| `invalid_http_status` | Une requête HTTP a renvoyé un code d'état indiquant un échec. |
| `http_timeout` | Une requête HTTP a expiré avant de recevoir une réponse. |
| `missing_hostname` | L'URL de la requête ne contient pas de nom d'hôte. |{% endif %}
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endunless %}

{% if ch == "all" or ch == "email" %}

### E-mail

| Valeur `abort_type` | Description |
| --- | --- |
| `exhausted_link_shortening_retries` | Le raccourcissement de lien a échoué après le nombre maximal de tentatives. |
| `missing_email` | L'utilisateur n'a pas d'adresse e-mail dans son profil. |
| `invalid_domain` | L'adresse e-mail possède un domaine non valide. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endif %}

{% if ch == "all" or ch == "push" %}

### Push

| Valeur `abort_type` | Description |
| --- | --- |
| `invalid_push_payload` | Le payload de la notification push est non valide ou mal formé. |
| `sdk_not_supported` | La version du SDK sur l'appareil de l'utilisateur ne prend pas en charge ce type de notification push. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endif %}

{% if ch == "all" or ch == "sms" %}

### SMS/MMS

| Valeur `abort_type` | Description |
| --- | --- |
| `exhausted_link_shortening_retries` | Le raccourcissement de lien a échoué après le nombre maximal de tentatives. |
| `sms_empty_payload` | Le corps du message SMS est vide. |
| `sms_no_sending_numbers` | Aucun numéro de téléphone d'envoi n'est disponible pour ce groupe d'abonnement. |
| `sms_fatal_provider_error` | Une erreur fatale s'est produite avec le fournisseur SMS, empêchant la distribution du message. |
| `sms_gateway_domain_not_allowed` | Le domaine de la passerelle SMS ne figure pas dans la liste autorisée. |
| `blocked_recipient_country` | Le numéro de téléphone du destinataire se trouve dans un pays bloqué par vos [autorisations géographiques]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_geographic_permissions/). |
| `mms_not_supported` | Le MMS n'est pas pris en charge pour ce destinataire ou ce numéro d'envoi. |
| `no_current_messaging_service` | Aucun service d'envoi de messages actif n'est configuré pour ce groupe d'abonnement. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endif %}

{% if ch == "all" or ch == "whatsapp" %}

### WhatsApp

| Valeur `abort_type` | Description |
| --- | --- |
| `whats_app_no_sending_numbers` | Aucun numéro de téléphone d'envoi n'est disponible pour ce groupe d'abonnement WhatsApp. |
| `whats_app_invalid_template_message` | Le modèle de message WhatsApp est non valide ou n'a pas été approuvé. |
| `whats_app_invalid_response_message` | Le message de réponse WhatsApp est non valide. |
| `whats_app_fatal_provider_error` | Une erreur fatale s'est produite avec le fournisseur WhatsApp, empêchant la distribution du message. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endif %}

{% if ch == "all" or ch == "line" %}

### LINE

| Valeur `abort_type` | Description |
| --- | --- |
| `line_fatal_provider_error` | Une erreur fatale s'est produite avec le fournisseur LINE, empêchant la distribution du message. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endif %}

{% if ch == "all" or ch == "kakao" %}

### Kakao

| Valeur `abort_type` | Description |
| --- | --- |
| `kakao_fatal_provider_error` | Une erreur fatale s'est produite avec le fournisseur Kakao, empêchant la distribution du message. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endif %}

{% if ch == "all" or ch == "contentcard" %}

### Cartes de contenu

| Valeur `abort_type` | Description |
| --- | --- |
| `content_card_size_exceeded` | Le payload de la carte de contenu dépasse la taille maximale autorisée (2 Ko). |
| `content_card_content_invalid` | Le contenu de la carte de contenu est non valide ou contient des caractères non pris en charge. |
| `content_card_expiration_invalid` | La date d'expiration de la carte de contenu est non valide. |
| `content_card_general` | La carte de contenu n'a pas pu être créée en raison d'une erreur générale. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endif %}

{% if ch == "all" or ch == "inappmessage" %}

### Messages in-app

| Valeur `abort_type` | Description |
| --- | --- |
| `no_longer_in_availability_window` | Le message n'a pas pu être envoyé dans la fenêtre de disponibilité configurée, il a donc été abandonné. |
| `maximum_impressions_reached` | Le message in-app a déjà atteint son nombre maximal d'impressions. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endif %}

{% if ch == "all" or ch == "webhook" %}

### Webhooks

| Valeur `abort_type` | Description |
| --- | --- |
| `blocked_webhook_url` | L'URL du webhook a été bloquée par les politiques de sécurité. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endif %}