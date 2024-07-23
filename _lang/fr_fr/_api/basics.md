---
nav_title: "Overview API"
article_title: Overview API
page_order: 2.1
description: "Cet article de référence couvre les fondamentaux de l’API, y compris ce qu’est une API REST, sa terminologie et un aperçu des clés API."
page_type: reference
alias: /api/api_key/
---

# Overview API

> Cet article de référence couvre les fondamentaux de l’API, y compris sa terminologie courante, un aperçu des clés API REST, des permissions et de la manière de les sécuriser.

## Collection d’API REST de Braze

| Collection                                                                 | Objectif                                                                               |
|----------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| [Catalogues]({{site.baseurl}}/api/endpoints/catalogs/)                       | Créez et gérez des catalogues et des éléments de catalogue à référencer dans vos campagnes Braze.    |
| [Ingestion de données dans le cloud]({{site.baseurl}}/api/endpoints/cdi/)                | Gérez les intégrations et les synchronisations de vos entrepôts de données.                                    |
| [Listes et adresses e-mail]({{site.baseurl}}/api/endpoints/email/)         | Configurez et gérez la synchronisation bidirectionnelle entre Braze et vos systèmes de messagerie.           |
| [Exporter]({{site.baseurl}}/api/endpoints/export/)                           | Accédez et exportez divers détails de vos campagnes, canevas, indicateurs clés de performance, etc.        |
| [Messages]({{site.baseurl}}/api/endpoints/messaging/)                      | Planifiez, envoyez et gérez vos campagnes et vos canevas.                               |
| [Centre de préférences]({{site.baseurl}}/api/endpoints/preference_center/)     | Créez votre centre de préférences et mettez-en à jour le style.                            |
| [SCIM]({{site.baseurl}}/api/endpoints/scim/)                               | Gérez les identités des utilisateurs dans les applications et services basés sur le cloud.                      |
| [SMS]({{site.baseurl}}/api/endpoints/sms/)                                 | Gérez les numéros de téléphone de vos utilisateurs dans vos groupes d’abonnement.                         |
| [Groupes d’abonnement]({{site.baseurl}}/api/endpoints/subscription_groups/) | Répertoriez et mettez à jour les groupes d’abonnement SMS et e-mail stockés dans le tableau de bord Braze. |
| [Modèles]({{site.baseurl}}/api/endpoints/templates/)                     | Créez et mettez à jour des modèles pour les e-mails et les blocs de contenu.                   |
| [Données utilisateur]({{site.baseurl}}/api/endpoints/user_data/)                     | Identifiez, suivez et gérez vos utilisateurs.                                               |
{: .reset-td-br-1 .reset-td-br-2}

## Définitions relatives aux API

Voici un aperçu des termes que vous pouvez rencontrer dans la documentation de l’API REST de Braze.

### Endpoints

Braze gère plusieurs instances différentes pour notre tableau de bord et nos Endpoints REST. Une fois votre compte provisionné ; vous vous connecterez à l’une des URL suivantes. Utilisez le bon Endpoint REST en vous basant sur l’instance qui vous a été provisionnée. Si vous n’êtes pas sûr, créez un ticket d’assistancesupport ou utilisez le tableau ci-dessous pour faire correspondre l’URL du tableau de bord que vous utilisez au bon Endpoint REST.

{% alert important %}
Quand vous utilisez des endpoints pour des appels API, utilisez le « Endpoint REST ».

Pour l’intégration SDK, utilisez l’[endpoint SDK]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/) et non pas l’endpoint REST.
{% endalert %}

|Instance|Lien URL|Point de terminaison REST|Point de terminaison du SDK|
|---|---|---|
|US-01| `https://dashboard-01.braze.com` | `https://rest.iad-01.braze.com` | `sdk.iad-01.braze.com` |
|US-02| `https://dashboard-02.braze.com` | `https://rest.iad-02.braze.com` | `sdk.iad-02.braze.com` |
|US-03| `https://dashboard-03.braze.com` | `https://rest.iad-03.braze.com` | `sdk.iad-03.braze.com` |
|US-04| `https://dashboard-04.braze.com` | `https://rest.iad-04.braze.com` | `sdk.iad-04.braze.com` |
|US-05| `https://dashboard-05.braze.com` | `https://rest.iad-05.braze.com` | `sdk.iad-05.braze.com` |
|US-06| `https://dashboard-06.braze.com` | `https://rest.iad-06.braze.com` | `sdk.iad-06.braze.com` |
|US-07| `https://dashboard-07.braze.com` | `https://rest.iad-07.braze.com` | `sdk.iad-07.braze.com` |
|US-08| `https://dashboard-08.braze.com` | `https://rest.iad-08.braze.com` | `sdk.iad-08.braze.com` |
|EU-01| `https://dashboard-01.braze.eu` | `https://rest.fra-01.braze.eu` | `sdk.fra-01.braze.eu` |
|EU-02| `https://dashboard-02.braze.eu` | `https://rest.fra-02.braze.eu` | `sdk.fra-02.braze.eu` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

### Limites de l’API

Pour la plupart des API, la limite de débit par défaut définie par Braze est de 250 000 requêtes par heure. Cependant, certains types de requêtes ont leur propre limite de débit pour une meilleure gestion des grands volumes de données de notre base client. Consultez les []({{site.baseurl}}/api/api_limits/)limites de débit de l’API]({{site.baseurl}}/api/api_limits/) pour plus d’informations

### ID utilisateur 

- **ID d’utilisateur externe** : Le `external_id` sert d’identifiant utilisateur unique pour lequel vous soumettez des données. Cet identifiant doit être identique à celui que vous avez défini dans le SDK Braze afin d’éviter de créer plusieurs profils pour le même utilisateur.
- **ID utilisateur Braze** : `braze_id` sert d’identifiant utilisateur unique défini par Braze. Cet identifiant peut être utilisé pour supprimer des utilisateurs via l’API REST en plus des externalids.

Pour plus d’informations, reportez-vous aux articles suivants en fonction de votre plateforme : [iOS,][9] [Android][10] et [Web][13].

## Clé API REST

Une clé d’interface de programmation d’application REST (clé API REST) est un code unique qui est passé dans une API pour authentifier l’appel API et identifier l’application ou l’utilisateur d’appel. L’accès API s’effectue à l’aide des requêtes Web HTTPS dans l’endpoint de l’API REST de votre entreprise.  Chez Braze, nous utilisons conjointement les clés API REST et nos clés d’identification App pour accéder aux données, et les suivre, les envoyer, les exporter et les analyser afin de vous assurer que tout fonctionne bien de votre côté et du nôtre.

Les espaces de travail et les clés API vont de pair chez Braze. Les espaces de travail sont conçus pour héberger des versions de la même application sur plusieurs plateformes. De nombreux clients utilisent également des espaces de travail pour contenir des versions gratuites et premium de leurs applications sur la même plateforme. Comme vous pouvez le constater, ces espaces de travail utilisent également l’API REST et possèdent leurs propres clés API REST. Ces clés peuvent être personnalisées individuellement pour inclure l’accès à des endpoints spécifiques sur l’API. Chaque appel à l’API doit inclure une clé ayant accès à l’endpoint.

Nous faisons référence à la clé API REST et à la clé API de l’espace de travail en tant que `api_key`. Le `api_key` est inclus dans chaque requête en tant qu’en-tête de requête et agit comme une clé d’authentification qui vous permet d’utiliser nos API REST. Ces API REST sont utilisées pour suivre les utilisateurs, envoyer des messages, exporter des données utilisateur, etc. Quand vous créez une nouvelle clé API REST, vous devez lui accorder l’accès à des endpoints spécifiques. En affectant des autorisations spécifiques à une clé API, vous pouvez limiter de façon précise les appels qu’une clé API peut authentifier.

![Panneau Clés API REST sur la page Clés API.][27]

{% alert tip %}
En plus des clés API REST, il existe un troisième type appelé Clés d’identification qui permet de référencer des objets spécifiques tels que des applications, des modèles, des Canvas, des campagnes, des cartes de contenu et des segments de l’API. Pour plus d’informations, consultez la rubrique [Types d’identifiant API]({{site.baseurl}}/api/identifier_types/).
{% endalert %}

### Autorisations de clé API REST

Les autorisations de clés API sont des autorisations que vous pouvez affecter à un utilisateur ou un groupe pour limiter leur accès à certains appels API. Pour afficher la liste de vos autorisations de clé API, accédez à **Paramètres** > **Clés API**, puis sélectionnez votre clé API.

{% tabs %}
{% tab User Data %}

| Autorisation | Point de terminaison | Descriptif |
|---|---|---|
| `users.track` [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) | | Enregistrez les attributs utilisateur, les événements personnalisés et les achats. |
| `users.delete` [`/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/) | | Supprimer n’importe quel utilisateur. |
| `users.alias.new` | [`/users/alias/new`]({{site.baseurl}}/api/endpoints/user_data/post_user_alias/) |Créez un nouvel alias pour un utilisateur existant. |
| `users.identify` | [`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/) |Identifiez un utilisateur par alias uniquement à l’aide d’un ID externe. |
| `users.export.ids` [`/users/export/ids`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) | |Requête pour obtenir des informations de profil utilisateur par ID utilisateur. |
| `users.export.segment` [`/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/) | |Recherchez des informations sur le profil utilisateur par segment. |
| `users.merge` [`/users/merge`]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/) | | Fusionne deux utilisateurs existants l’un dans l’autre. |
| `users.external_ids.rename` [`/users/external_ids/rename`]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_rename/) | | Modifiez l’ID externe d’un utilisateur existant. |
| `users.external_ids.remove` [`/users/external_ids/remove`]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_remove/) | | Supprimez l’ID externe d’un utilisateur existant. |
| `users.alias.update` [`/users/alias/update`]({{site.baseurl}}/api/endpoints/user_data/post_users_alias_update/) | | Mettre à jour un alias pour un utilisateur existant. |
| `users.export.global_control_group` [`/users/export/global_control_group`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group/) | | Recherchez des informations de profil utilisateur dans le groupe de contrôle global. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

 {% endtab %}
 {% tab Email %}

| Autorisation | Point de terminaison | Descriptif |
|---|---|---|
| `email.unsubscribe` [`/email/unsubscribes`]({{site.baseurl}}/api/endpoints/email/get_query_unsubscribed_email_addresses/) | | Recherchez les adresses e-mail désabonnées.  |
| `email.status` [`/email/status`]({{site.baseurl}}/api/endpoints/email/post_email_subscription_status/) | | Modifier le statut de l’adresse e-mail. |
| `email.hard_bounces` | [`/email/hard_bounces`]({{site.baseurl}}/api/endpoints/email/get_list_hard_bounces/) | Extrayez les adresses e-mail ayant reçu un échec d'envoi définitif. |
| `email.bounce.remove` [`/email/bounce/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_hard_bounces/) | | Supprimez les adresses e-mail de votre liste de rebonds permanents. |
| `email.spam.remove` [`/email/spam/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_spam/) | | Supprimez les adresses e-mail de votre liste de spam. |
| `email.blacklist` | [`/email/blacklist`]({{site.baseurl}}/api/endpoints/email/post_blacklist/) | Ajoutez les adresses e-mail à la liste de blocage. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% endtab %}
{% tab Messages %}

| Autorisation | Point de terminaison | Descriptif |
|---|---|---|
| `messages.send` [`/messages/send `]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/) | | Envoyez un message immédiat à des utilisateurs spécifiques. |
| `messages.schedule.create` [`/messages/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_messages/) | | Planifiez l’envoi d’un message à une heure précise. |
| `messages.schedule.update` [`/messages/schedule/update`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_messages/) | | Mettre à jour un message planifié. |
| `messages.schedule.delete` [`/messages/schedule/delete`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_delete_scheduled_messages/) | | Supprimer un message programmé. |
| `messages.schedule_broadcasts` [`/messages/scheduled_broadcasts`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/get_messages_scheduled/) | | Interroger tous les messages de diffusion programmés. |
| `messages.live_activity.update` [`/messages/live_activity/update`]({{site.baseurl}}/api/endpoints/messaging/live_activity/update/) | | Mettre à jour une activité iOS Live. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% endtab %}
{% tab Campaigns %}

| Autorisation | Point de terminaison | Descriptif |
|---|---|---|
| `campaigns.trigger.send` [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/) | | Déclencher l’envoi d’une campagne existante. |
| `campaigns.trigger.schedule.create` [`/campaigns/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_campaigns/) | | Planifiez l’envoi futur d’une campagne avec une diffusion déclenchée par l’API. |
| `campaigns.trigger.schedule.update` [`/campaigns/trigger/schedule/update`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_campaigns/) | | Mettre à jour une campagne planifiée avec une diffusion déclenchée par l’API. |
| `campaigns.trigger.schedule.delete` [`/campaigns/trigger/schedule/delete`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_messages/) | |Supprimer une campagne planifiée avec une diffusion déclenchée par l’API. |
| `campaigns.list` [`/campaigns/list`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns/) | | Recherchez une liste de campagnes. |
| `campaigns.data_series` [`/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics/) | | Requête pour l’analyse des campagnes sur une période donnée. |
| `campaigns.details` [`/campaigns/details`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details/) | | Demander les détails d’une campagne spécifique. |
| `sends.data_series` [`/sends/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics/) | | Demander l’analyse des envois de messages sur une plage de temps. |
| `sends.id.create` | [`/sends/id/create`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_create_send_ids/) | Créez un ID d’envoi pour le suivi des messages. |
| `campaigns.url_info.details` [`/campaigns/url_info/details`]({{site.baseurl}}) | | Recherchez les détails de l’URL d’une variante de message spécifique au sein d’une campagne. |
| `transactional.send` [`/transactional/v1/campaigns/{campaign_id}/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_transactional_message/) | | Permet d’envoyer des messages transactionnels à l’aide du point de terminaison de messagerie transactionnelle. |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% tab Canvas %}

| Autorisation | Point de terminaison | Descriptif |
|---|---|---|
| `canvas.trigger.send` [`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/) | | Déclenchez l’envoi d’un canevas existant. |
| `canvas.trigger.schedule.create` | [`/canvas/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases/) | Planifiez le futur envoi d’un canvas avec un envoi déclenché par API. |
| `canvas.trigger.schedule.update` | [`/canvas/trigger/schedule/update`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_canvases/) | Mettez à jour un canvas planifié avec une distribution déclenchée par API. |
| `canvas.trigger.schedule.delete` [`/canvas/trigger/schedule/delete`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_canvases/)| | Supprimer un canevas planifié avec une diffusion déclenchée par l’API. |
| `canvas.list` [`/canvas/list`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases/) | |  Recherchez une liste de canevas. |
| `canvas.data_series` [`/canvas/data_series`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics/) | | Requête pour l’analyse Canvas sur une période donnée. |
| `canvas.details` [`/canvas/details`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details/) | | Recherchez les détails d’un canevas spécifique. |
| `canvas.data_summary` [`/canvas/data_summary`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics_summary/) | | Requête pour les cumuls d’analyses Canvas sur une période donnée. |
| `canvas.url_info.details` [`/canvas/url_info/details`]({{site.baseurl}}/get_canvas_link_alias/) | | Recherchez les détails de l’URL d’une variante de message spécifique dans une étape Canevas. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% endtab %}
{% tab Segments %}

| Autorisation | Point de terminaison | Descriptif |
|---|---|---|
| `segments.list` [`/segments/list`]({{site.baseurl}}/api/endpoints/export/segments/get_segment/) | | Recherchez une liste de segments. |
| `segments.data_series` [`/segments/data_series`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_analytics/) | | Requête pour l’analyse des segments sur une plage de temps. |
| `segments.details` [`/segments/details`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_details/) | | Demander les détails d’un segment spécifique. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% endtab %}
{% tab Purchases %}

| Autorisation | Point de terminaison | Descriptif |
|---|---|---|
| `purchases.product_list` [`/purchases/product_list`]({{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id/) | | Recherchez la liste des produits achetés dans votre application. |
| `purchases.revenue_series` [`/purchases/revenue_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_revenue_series/) | | Recherchez le montant total dépensé par jour dans votre application sur une période donnée. |
| `purchases.product_list` [`/purchases/product_list`]({{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id/) | | Recherchez une liste d’événements personnalisés. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% endtab %}
{% tab Events %}

| Autorisation | Point de terminaison | Descriptif |
|---|---|---|
| `events.list` [`/events/list`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events/) | | Recherchez une liste d’événements personnalisés. |
| `events.data_series` [`/events/data_series`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_analytics/) | | Interroger les occurrences d’un événement personnalisé sur une plage de temps. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% endtab %}
{% tab News Feed %}

{% alert note %}
Le Fil d’actualité est obsolète. Braze recommande aux clients qui utilisent notre outil de fil d’actualités de passer à notre canal de communication de cartes de contenu : il est plus flexible, plus personnalisable et plus fiable. Consultez le [guide de migration]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/) pour en savoir plus.
{% endalert %}

| Autorisation | Point de terminaison | Descriptif |
|---|---|---|
| `feed.list` [`/feed/list`]({{site.baseurl}}/api/endpoints/export/news_feed/get_news_feed_cards/) | | Recherchez la liste des cartes du fil d’actualité. |
| `feed.data_series` [`/feed/data_series`]({{site.baseurl}}/api/endpoints/export/news_feed/get_news_feed_card_analytics/) | | Requête pour des analyses de fil d’actualité sur une période donnée. |
| `feed.details` [`/feed/details`]({{site.baseurl}}/api/endpoints/export/news_feed/get_news_feed_card_details/) | | Recherchez les détails d’un fil d’actualité spécifique. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% endtab %}
{% tab Sessions %}

| Autorisation | Point de terminaison | Descriptif |
|---|---|---|
| `sessions.data_series` [`/sessions/data_series`]({{site.baseurl}}/api/endpoints/export/sessions/get_sessions_analytics/) | |  Recherchez des utilisateurs actifs uniques par jour sur une plage de temps. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% endtab %}
{% tab KPIs %}

| Autorisation | Point de terminaison | Descriptif |
|---|---|---|
| `kpi.dau.data_series` [`/kpi/dau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_dau_date/) | |  Recherchez des utilisateurs actifs uniques par jour sur une plage de temps. |
| `kpi.mau.data_series` | [`/kpi/mau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_mau_30_days/) | Extrayez les utilisateurs actifs uniques sur une fenêtre de 30 jours glissants sur une période donnée. |
| `kpi.new_users.data_series` [`/kpi/new_users/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_daily_new_users_date/) | | Rechercher de nouveaux utilisateurs par jour sur une plage de temps. |
| `kpi.uninstalls.data_series` [`/kpi/uninstalls/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_uninstalls_date/) | | Recherchez les désinstallations d’applications par jour sur une période donnée. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% endtab %}
{% tab Templates %}

| Autorisation | Point de terminaison | Descriptif |
|---|---|---|
| `templates.email.create` [`/templates/email/create`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template/) | | Créez un nouveau modèle d’e-mail sur le tableau de bord. |
| `templates.email.info` [`/templates/email/info`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_see_email_template_information/) | | Demander des informations sur un modèle spécifique. |
| `templates.email.list` [`/templates/email/list`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates/) | | Recherchez une liste de modèles d’e-mails. |
| `templates.email.update` [`/templates/email/update`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_update_email_template/) | | Mettre à jour un modèle d’e-mail stocké sur le tableau de bord. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% endtab %}
{% tab SSO %}

| Autorisation | Descriptif |
|---|---|---|
| `sso.saml.login` | Configurez la connexion effectuée par le fournisseur d’identité. Pour plus d’informations, consultez la rubrique [Le fournisseur de services (SP) a initié une connexion]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% endtab %}
{% tab Content Blocks %}

| Autorisation | Point de terminaison | Descriptif |
|---|---|---|
| `content_blocks.info` [`/content_blocks/info`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information/) | | Demander des informations sur un modèle spécifique. |
| `content_blocks.list` [`/content_blocks/list`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks/) | | Recherchez une liste de blocs de contenu. |
| `content_blocks.create` [`/content_blocks/create`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_create_email_content_block/) | | Créez un nouveau bloc de contenu sur le tableau de bord. |
| `content_blocks.info` [`/content_blocks/info`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information/) | | Obtenez un centre de préférences. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% endtab %}
{% tab Preference Center %}

| Autorisation | Point de terminaison | Descriptif |
|---|---|---|
| `preference_center.get` [`/preference_center/v1/{preferenceCenterExternalId}`]({{site.baseurl}}/api/endpoints/preference_center/get_view_details_preference_center) | | Obtenez un centre de préférences. |
| `preference_center.list` [`/preference_center/v1/list`]({{site.baseurl}}/api/endpoints/preference_center/get_list_preference_center/) | | Répertorier les centres de préférences. |
| `preference_center.update` | [`/preference_center/v1`]({{site.baseurl}}/api/endpoints/preference_center/post_create_preference_center)<br><br>[`/preference_center/v1/{preferenceCenterExternalID}`]({{site.baseurl}}/api/endpoints/preference_center/put_update_preference_center/) | Créez ou mettez à jour un centre de préférences. |
| `preference_center.user.get` [`/preference_center/v1/{preferenceCenterExternalId}/url/{userId}`]({{site.baseurl}}/api/endpoints/preference_center/get_create_url_preference_center) | | Obtenez un lien vers le centre de préférences pour un utilisateur. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% endtab %}
{% tab Subscription %}

| Autorisation | Point de terminaison | Descriptif |
|---|---|---|
| `subscription.status.set` [`/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/) | | Définissez l’état du groupe d’abonnement. |
| `subscription.status.get` [`/subscription/status/get`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/) | | Obtenir l’état du groupe d’abonnement. |
| `subscription.groups.get` [`/subscription/user/status`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups/) | | Obtenir l’état des groupes d’abonnement auxquels des utilisateurs spécifiques sont explicitement abonnés et désabonnés. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% endtab %}
{% tab SMS %}

| Autorisation | Point de terminaison | Descriptif |
|---|---|---|
| `sms.invalid_phone_numbers` [`/sms/invalid_phone_numbers`]({{site.baseurl}}/api/endpoints/sms/get_query_invalid_numbers/) | | Recherchez des numéros de téléphone non valides. |
| `sms.invalid_phone_numbers.remove` [`/sms/invalid_phone_numbers/remove`]({{site.baseurl}}/api/endpoints/sms/post_remove_invalid_numbers/) | | Supprimez l’indicateur de numéro de téléphone non valide pour les utilisateurs. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% endtab %}
{% tab Catalogs %}

| Autorisation | Point de terminaison | Descriptif |
|---|---|---|
| `catalogs.add_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/post_create_catalog_items_bulk/) | Ajoutez plusieurs produits à un catalogue existant. |
| `catalogs.update_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/patch_catalog_items_bulk/) | Mettez à jour plusieurs produits dans un catalogue existant. |
| `catalogs.delete_items` [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/delete_catalog_items_bulk) | | Supprimer plusieurs éléments d’un catalogue existant. |
| `catalogs.get_item` [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details/) | | Obtenez un seul article d’un catalogue existant. |
| `catalogs.update_item` [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/put_update_catalog_item/) | | Mettre à jour un seul élément dans un catalogue existant. |
| `catalogs.create_item` [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/post_create_catalog_item/) | | Créez un seul élément dans un catalogue existant. |
| `catalogs.delete_item` [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/delete_catalog_item/) | | Supprimer un seul élément d’un catalogue existant. |
| `catalogs.replace_item` [` /catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/put_update_catalog_item/) | | Remplacer un seul élément d’un catalogue existant. |
| `catalogs.create` [`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/post_create_catalog/) | | Créez un catalogue. |
| `catalogs.get` [`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs/) | | Obtenir une liste de catalogues |
| `catalogs.delete` [`/catalogs/{catalog_name}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/delete_catalog/) | | Supprimer un catalogue. |
| `catalogs.get_items` [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk/) | | Obtenez un aperçu des articles à partir d’un catalogue existant. |
| `catalogs.replace_items` [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/put_update_catalog_items/) | | Remplacer des éléments dans un catalogue existant. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% endtab %}
{% endtabs %}

## Création de clés API REST

Pour créer une nouvelle clé d’API REST :

1. Accédez à **Paramètres** > **Clés API**. Cette page affiche vos clés API existantes.

{% alert note %}
Si vous utilisez [l’ancienne navigation]({{site.baseurl}}/navigation), vous pouvez créer une clé API à partir de **la console** développeur > **Paramètres de l’API**.
{% endalert %}

{:start="2"}
2\. Cliquez sur **\+ Créer une nouvelle clé API**.
3\. Nommer votre nouvelle clé pour pouvoir l’identifier facilement
4\. Sélectionnez les [autorisations](#rest-api-key-permissions) que vous souhaitez associer à votre nouvelle clé.
5\. Spécifier les sous-réseaux et [adresses IP autorisés](#api-ip-allowlisting) pour cette nouvelle clé.

{% alert important %}
Gardez à l’esprit qu’une fois que vous avez créé une nouvelle clé API, vous ne pouvez plus modifier les autorisations ni la liste des adresses IP autorisées. Cette restriction est en place pour des raisons de sécurité. Si vous devez modifier le périmètre d’une clé, créez une nouvelle clé avec les autorisations mises à jour et implémentez cette clé à la place de l’ancienne. Une fois que votre implémentation est terminée, vous pouvez supprimer l’ancienne clé.
{% endalert %}

## Gestion des clés API REST

Les clés d’API REST ne peuvent pas être modifiées après leur création. Toutefois, vous pouvez afficher les détails des clés API REST existantes ou les supprimer à partir de la page **Clés API** . La liste **Clés API Rest** affiche les informations suivantes en un coup d’œil pour chaque clé :

| Champ        | Description                                                                                                         |
| ------------ | :------------------------------------------------------------------------------------------------------------------ |
| Nom de la clé API | Nom donné à la clé lors de sa création.                                                                            |
| Identifiant | La clé API.                                                                                                        |
| Créé par | Adresse e-mail de l’utilisateur qui a créé la clé. Ce champ s’affichera comme "N/A" for keys created before June 2023. |
| Date Created | The date this key was created.                                                                                      |
| Last Seen    | The date this key was last used. This field will show as "N/A" for keys that have never been used.                  |
{: .reset-td-br-1 .reset-td-br-2}

Pour afficher les détails d’une clé spécifique, sélectionnez celle-ci dans la liste. Vous pouvez alors voir toutes les autorisations de cette clé, les adresses IP de la liste blanche (le cas échéant) et si cette clé est activée dans la liste blanche des adresses IP de Braze.

![][30]

Pour supprimer une clé, cliquez sur <i class="fas fa-gear" alt="Settings"></i> l’option correspondante et sélectionnez-la.

![][29]

## Sécurité clé API REST

Les clés API servent à authentifier les appels de l’API. Quand vous créez une nouvelle clé API REST, vous devez lui accorder l’accès à des endpoints spécifiques. En affectant des autorisations spécifiques à une clé API, vous pouvez limiter de façon précise les appels qu’une clé API peut authentifier.

Étant donné que les clés API REST permettent d’accéder à des endpoints API REST potentiellement sensibles, sécurisez ces clés et partagez-les uniquement avec des partenaires de confiance. Elles ne doivent jamais être exposées publiquement. Par exemple, n’utilisez pas cette clé pour faire des appels AJAX depuis votre site Web ou pour l’exposer autrement de façon publique.

Une bonne pratique de sécurité est d’accorder à un utilisateur uniquement les accès nécessaires pour qu’il puisse accomplir son travail ; ce principe peut également être appliqué aux Clés API en affectant des autorisations pour chaque clé. Ces autorisations vous offrent une meilleure sécurité et un meilleur contrôle sur les différentes parties de votre compte. 

![Autorisations de clé API disponibles lors de la création d’une clé API.] [25]

{% alert warning %}
Comme les clés API REST permettent d’accéder à des endpoints de l’API REST potentiellement sensibles, veillez à ce qu’elles soient stockées et utilisées de façon sécurisée. Par exemple, n’utilisez pas cette clé pour faire des appels AJAX depuis votre site Web ou pour l’exposer autrement de façon publique.
{% endalert %}

En cas d’exposition accidentelle d’une clé, elle pourra être supprimée à partir de la console de développement. Pour obtenir de l’aide sur ce processus, ouvrez un [ticket d’assistance][support].

### Liste d’adresses IP autorisées

Pour renforcer la sécurité, vous pouvez établir une liste des adresses IP et sous-réseaux qui sont exclusivement autorisés à envoyer des requêtes à l’API REST pour une clé API REST donnée. Vous définissez pour cela une liste d’autorisations, également appelée « Liste blanche ». Pour autoriser des adresses IP ou des sous-réseaux spécifiques, indiquez-les dans la section **Liste blanche d’adresses IP (Whitelist IPs) **lors de la création d’une nouvelle clé API REST : 

![Possibilité de créer une liste blanche d’adresses IP lors de la création d’une clé API][26]

Si vous n’en spécifiez aucune, les requêtes pourront être envoyées depuis n’importe quelle adresse IP.

{% alert tip %}
Vous créez un Webhook Braze à Braze en utilisant une liste blanche ? Consultez notre [liste d’adresses IP à autoriser (IPs to whitelist).]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#ip-whitelisting)
{% endalert %}

## Ressources complémentaires

### Bibliothèque client Ruby

Si vous utilisez Ruby pour implémenter Braze, vous pouvez utiliser notre [Bibliothèque Client Ruby](https://github.com/braze-inc/braze-api-client-ruby) pour réduire le temps d’importation des données. Une bibliothèque cliente est une collection de code spécifique à un langage de programmation (dans ce cas, Ruby) qui facilite l’utilisation d’une API.

La bibliothèque client Ruby prend en charge les [endpoints Utilisateur]({{site.baseurl}}/api/endpoints/user_data).

{% alert note %}
Cette bibliothèque cliente est actuellement en version bêta. Voulez-vous nous aider à améliorer cette bibliothèque ? Envoyez vos commentaires à [smb-product@braze.com](mailto:smb-product@braze.com).
{% endalert %}

[1]: https://en.wikipedia.org/wiki/UTF-8
[7]: {{site.baseurl}}/api/objects_filters/connected_audience/
[9]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/
[10]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids/
[13]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_user_ids/
[2]: {{site.baseurl}}/api/identifier_types/
[5]: {{site.baseurl}}/api/basics/
[6]: https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#intro
[25]: {% image_buster /assets/img_archive/api-key-permissions.png %}
[26]: {% image_buster /assets/img_archive/api-key-ip-whitelisting.png %}
[support]: {{site.baseurl}}/braze_support/
[28]: {% image_buster /assets/img_archive/create-new-key.png %}
[29]: {% image_buster /assets/img_archive/api-key-options.png %}
[27]: {% image_buster /assets/img_archive/rest-api-key.png %}
[30]: {% image_buster /assets/img_archive/view-api-key.png %}
