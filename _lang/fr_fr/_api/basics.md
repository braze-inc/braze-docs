---
nav_title: "Overview API"
article_title: Overview API
page_order: 2.1
description: "Cet article de référence couvre les fondamentaux de l’API, y compris ce qu’est une API REST, sa terminologie et un aperçu des clés API."
page_type: reference
alias: /api/api_key/
---

# Overview API

> Cet article de référence couvre les bases de l'API, y compris la terminologie commune et un aperçu des clés de l'API REST, des permissions et de la manière de les sécuriser.

## Collection d’API REST de Braze

| Collection                                                                 | Objectif                                                                               |
|----------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| [Catalogues]({{site.baseurl}}/api/endpoints/catalogs/)                       | Créez et gérez des catalogues et des éléments de catalogue à référencer dans vos campagnes Braze.    |
| [Ingestion de données cloud]({{site.baseurl}}/api/endpoints/cdi/)                | Gérez les intégrations et les synchronisations de votre entrepôt de données.                                    |
| [Listes et adresses e-mail]({{site.baseurl}}/api/endpoints/email/)         | Configurez et gérez la synchronisation bidirectionnelle entre Braze et vos paramètres d'e-mail.           |
| [Exporter]({{site.baseurl}}/api/endpoints/export/)                           | Accédez et exportez divers détails de vos campagnes, Canvas, KPI, et plus encore.        |
| [Messages]({{site.baseurl}}/api/endpoints/messaging/)                      | Planifiez, envoyez et gérez vos campagnes et vos canevas.                               |
| [Centre de préférences]({{site.baseurl}}/api/endpoints/preference_center/)     | Créez votre centre de préférences et actualisez son style.                            |
| [SCIM]({{site.baseurl}}/api/endpoints/scim/)                               | Gérer les identités des utilisateurs dans les applications et services basés sur le cloud.                      |
| [SMS]({{site.baseurl}}/api/endpoints/sms/)                                 | Gérez les numéros de téléphone de vos utilisateurs dans vos groupes d'abonnements.                         |
| [Groupes d’abonnement]({{site.baseurl}}/api/endpoints/subscription_groups/) | Répertoriez et mettez à jour les groupes d'abonnement SMS et e-mail stockés dans le tableau de bord de Braze. |
| [Modèles]({{site.baseurl}}/api/endpoints/templates/)                     | Créez et mettez à jour des modèles pour les envois de messages par e-mail et les blocs de contenu.                   |
| [Données utilisateur]({{site.baseurl}}/api/endpoints/user_data/)                     | Identifiez, suivez et gérez vos utilisateurs.                                               |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Définitions relatives aux API

Voici un aperçu des termes que vous pouvez rencontrer dans la documentation de l’API REST de Braze.

### Endpoints

Braze gère un certain nombre d'instances différentes pour notre tableau de bord et nos endpoints REST. Une fois votre compte provisionné ; vous vous connecterez à l’une des URL suivantes. Utilisez le bon Endpoint REST en vous basant sur l’instance qui vous a été provisionnée. En cas de doute, ouvrez un [ticket d'assistance]({{site.baseurl}}/braze_support/) ou utilisez le tableau suivant pour faire correspondre l'URL du tableau de bord que vous utilisez au bon endpoint REST.

{% alert important %}
Lorsque vous utilisez des endpoints pour les appels API, utilisez l'endpoint REST.

Pour l’intégration SDK, utilisez l’[endpoint SDK]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/) et non pas l’endpoint REST.
{% endalert %}

{% multi_lang_include data_centers.md datacenters='instances' %}

### Limites de l’API

Pour la plupart des API, la limite de débit par défaut définie par Braze est de 250 000 requêtes par heure. Cependant, certains types de requêtes ont leur propre limite de débit pour une meilleure gestion des grands volumes de données de notre base client. Consultez les []({{site.baseurl}}/api/api_limits/)limites de débit de l’API]({{site.baseurl}}/api/api_limits/) pour plus d’informations

### ID utilisateur

- **ID externe**: Le `external_id` sert d’identifiant utilisateur unique pour lequel vous soumettez des données. Cet identifiant doit être identique à celui que vous avez défini dans le SDK Braze afin d’éviter de créer plusieurs profils pour le même utilisateur.
- **ID de l'utilisateur de Braze**: `braze_id` sert d'identifiant unique de l'utilisateur, défini par Braze. Cet identifiant peut être utilisé pour supprimer des utilisateurs via l'API REST, en plus des external_ids.

Pour plus d'informations, consultez les articles suivants en fonction de votre plateforme : [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids/) et [Web.]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_user_ids/)

## À propos des clés API REST

Une clé d’interface de programmation d’application REST (clé API REST) est un code unique qui est passé dans une API pour authentifier l’appel API et identifier l’application ou l’utilisateur d’appel. L’accès API s’effectue à l’aide des requêtes Web HTTPS dans l’endpoint de l’API REST de votre entreprise.  Chez Braze, nous utilisons conjointement les clés API REST et nos clés d’identification App pour accéder aux données, et les suivre, les envoyer, les exporter et les analyser afin de vous assurer que tout fonctionne bien de votre côté et du nôtre.

Chez Braze, les espaces de travail et les clés API vont de pair. Les espaces de travail sont conçus pour héberger des versions de la même application sur plusieurs plateformes. De nombreux clients utilisent également des espaces de travail pour contenir des versions gratuites et premium de leurs applications sur la même plateforme. Comme vous pouvez le constater, ces espaces de travail utilisent également l’API REST et possèdent leurs propres clés API REST. Ces clés peuvent être personnalisées individuellement pour inclure l’accès à des endpoints spécifiques sur l’API. Chaque appel à l’API doit inclure une clé ayant accès à l’endpoint.

Nous faisons référence à la clé API REST et à la clé API de l’espace de travail en tant que `api_key`. Le `api_key` est inclus dans chaque requête en tant qu'en-tête de requête et agit comme une clé d'authentification qui vous permet d'utiliser nos API REST. Ces API REST sont utilisées pour suivre les utilisateurs, envoyer des messages, exporter des données utilisateur, etc. Quand vous créez une nouvelle clé API REST, vous devez lui accorder l’accès à des endpoints spécifiques. En affectant des autorisations spécifiques à une clé API, vous pouvez limiter de façon précise les appels qu’une clé API peut authentifier.

![Panneau des clés API REST dans l'onglet Clés API.]({% image_buster /assets/img_archive/rest-api-key.png %})

{% alert tip %}
En plus des clés API REST, il existe un troisième type appelé Clés d’identification qui permet de référencer des objets spécifiques tels que des applications, des modèles, des Canvas, des campagnes, des cartes de contenu et des segments de l’API. Pour plus d'informations, reportez-vous aux [types d'identifiants API]({{site.baseurl}}/api/identifier_types/).
{% endalert %}

### Créer des clés API REST

Pour créer une nouvelle clé d’API REST :

1. Allez dans **Paramètres** > **API et identifiants**.
2. Sélectionnez **Créer une clé API**.
3. Donnez un nom à votre nouvelle clé pour l'identifier d'un coup d'œil.
4. Spécifier les sous-réseaux et [adresses IP autorisés](#api-ip-allowlisting) pour cette nouvelle clé.
5. Sélectionnez les [autorisations](#rest-api-key-permissions) que vous souhaitez associer à votre nouvelle clé.

{% alert important %}
N'oubliez pas qu'après avoir créé une nouvelle clé API, vous ne pouvez pas modifier l'étendue des autorisations ou les adresses IP autorisées. Cette restriction est en place pour des raisons de sécurité. Si vous devez modifier le périmètre d’une clé, créez une nouvelle clé avec les autorisations mises à jour et implémentez cette clé à la place de l’ancienne. Une fois la mise en œuvre terminée, vous pouvez supprimer l'ancienne clé.
{% endalert %}

### Autorisations de clé API REST

Les autorisations de clés API sont des autorisations que vous pouvez affecter à un utilisateur ou un groupe pour limiter leur accès à certains appels API. Pour afficher la liste des autorisations de votre clé API, allez dans **Paramètres** > **API et identifiants**, et sélectionnez votre clé API.

{% tabs %}
{% tab Données de l'utilisateur %}

| Autorisation | Endpoint | Description |
|---|---|---|
| `users.track` | [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) | Enregistrer les attributs utilisateur, les événements personnalisés et les achats. |
| `users.delete` | [`/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/) | Supprimer un utilisateur. |
| `users.alias.new` | [`/users/alias/new`]({{site.baseurl}}/api/endpoints/user_data/post_user_alias/) |Créer un nouvel alias pour un utilisateur existant. |
| `users.identify` | [`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/) |Identifier un utilisateur alias d'un ID externe. |
| `users.export.ids` | [`/users/export/ids`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) |Extraire les données de profil utilisateur par ID d'utilisateur. |
| `users.export.segment` | [`/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/) |Demande d'informations sur le profil utilisateur par segmentation. |
| `users.merge` | [`/users/merge`]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/) | Fusionne deux utilisateurs existants. |
| `users.external_ids.rename` | [`/users/external_ids/rename`]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_rename/) | Changer l’ID externe d’un utilisateur existant. |
| `users.external_ids.remove` | [`/users/external_ids/remove`]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_remove/) | Supprimer l’ID externe d’un utilisateur existant. |
| `users.alias.update` | [`/users/alias/update`]({{site.baseurl}}/api/endpoints/user_data/post_users_alias_update/) | Mettre à jour un alias pour un utilisateur existant. |
| `users.export.global_control_group` | [`/users/export/global_control_group`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group/) | Extraire les données des profils d'utilisateur dans le groupe de contrôle global. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

 {% endtab %}
 {% tab E-mail %}

| Autorisation | Endpoint | Description |
|---|---|---|
| `email.unsubscribe` | [`/email/unsubscribes`]({{site.baseurl}}/api/endpoints/email/get_query_unsubscribed_email_addresses/) | Extraire les adresses e-mail désinscrites.  |
| `email.status` | [`/email/status`]({{site.baseurl}}/api/endpoints/email/post_email_subscription_status/) | Modifier l’état de l’adresse e-mail. |
| `email.hard_bounces` | [`/email/hard_bounces`]({{site.baseurl}}/api/endpoints/email/get_list_hard_bounces/) | Extraire les adresses e-mail ayant reçu un échec d'envoi définitif. |
| `email.bounce.remove` | [`/email/bounce/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_hard_bounces/) | Supprimer des adresses e-mail de votre liste d'e-mails ayant reçu un échec d'envoi définitif. |
| `email.spam.remove` | [`/email/spam/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_spam/) | Supprimer les adresses e-mail de votre liste de spam. |
| `email.blacklist` | [`/email/blacklist`]({{site.baseurl}}/api/endpoints/email/post_blacklist/) | Liste de blocage des adresses e-mail. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Messages %}

| Autorisation | Endpoint | Description |
|---|---|---|
| `messages.send` | [`/messages/send `]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/) | Envoyez un message immédiat à des utilisateurs spécifiques. |
| `messages.schedule.create` | [`/messages/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_messages/) | Planifier un message à envoyer à une heure précise. |
| `messages.schedule.update` | [`/messages/schedule/update`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_messages/) | Mettre à jour un message planifié. |
| `messages.schedule.delete` | [`/messages/schedule/delete`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_delete_scheduled_messages/) | Supprimer un message planifié. |
| `messages.schedule_broadcasts` | [`/messages/scheduled_broadcasts`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/get_messages_scheduled/) | Extraire tous les messages de diffusion programmés. |
| `messages.live_activity.update` | [`/messages/live_activity/update`]({{site.baseurl}}/api/endpoints/messaging/live_activity/update/) | Mettre à jour une activité iOS Live. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Campagnes %}

| Autorisation | Endpoint | Description |
|---|---|---|
| `campaigns.trigger.send` | [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/) | Déclencher l’envoi d’une campagne existante. |
| `campaigns.trigger.schedule.create` | [`/campaigns/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_campaigns/) | Planifier le futur envoi d’une campagne avec une livraison déclenchée par API. |
| `campaigns.trigger.schedule.update` | [`/campaigns/trigger/schedule/update`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_campaigns/) | Mettre à jour une campagne planifiée avec une livraison déclenchée par API. |
| `campaigns.trigger.schedule.delete` | [`/campaigns/trigger/schedule/delete`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_messages/) |Supprimez une campagne planifiée avec une réception/distribution déclenchée par l'API. |
| `campaigns.list` | [`/campaigns/list`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns/) | Extraire la liste des campagnes. |
| `campaigns.data_series` | [`/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics/) | Extraire les données d'analyse d'une campagne sur une période donnée. |
| `campaigns.details` | [`/campaigns/details`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details/) | Extraire les données d’une campagne spécifique. |
| `sends.data_series` | [`/sends/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics/) | Extraire l’analyse des messages envoyés sur une période donnée. |
| `sends.id.create` | [`/sends/id/create`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_create_send_ids/) | Créez un ID d'envoi pour le suivi de l'envoi des messages. |
| `campaigns.url_info.details` | [`/campaigns/url_info/details`]({{site.baseurl}}) | Extraire les données des URL d’une variation de message donnée dans une campagne. |
| `transactional.send` | [`/transactional/v1/campaigns/{campaign_id}/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_transactional_message/) | Permet d'envoyer des messages transactionnels à l'aide de l'endpoint de messagerie transactionnelle. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Canvas %}

| Autorisation | Endpoint | Description |
|---|---|---|
| `canvas.trigger.send` | [`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/) | Déclencher l’envoi d’un canvas existant. |
| `canvas.trigger.schedule.create` | [`/canvas/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases/) | Planifier le futur envoi d’un canvas avec un envoi déclenché par API. |
| `canvas.trigger.schedule.update` | [`/canvas/trigger/schedule/update`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_canvases/) | Mettre à jour un canvas planifié avec un envoi déclenché par API. |
| `canvas.trigger.schedule.delete` | [`/canvas/trigger/schedule/delete`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_canvases/)| Supprimer un canvas programmé avec un envoi déclenché par API. |
| `canvas.list` | [`/canvas/list`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases/) |  Extraire la liste des Canvas. |
| `canvas.data_series` | [`/canvas/data_series`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics/) | Extraire l'analyse de Canvas sur une période donnée. |
| `canvas.details` | [`/canvas/details`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details/) | Extraire les données d’un Canvas spécifique. |
| `canvas.data_summary` | [`/canvas/data_summary`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics_summary/) | Extraire les cumuls des analyses de Canvas sur une période donnée. |
| `canvas.url_info.details` | [`/canvas/url_info/details`]({{site.baseurl}}/get_canvas_link_alias/) | Demande d'informations sur l'URL d'une variation de message spécifique au sein d'une étape du canvas. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Segmentations %}

| Autorisation | Endpoint | Description |
|---|---|---|
| `segments.list` | [`/segments/list`]({{site.baseurl}}/api/endpoints/export/segments/get_segment/) | Demande d'une liste de segments. |
| `segments.data_series` | [`/segments/data_series`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_analytics/) | Demande d'analyses/analytiques de segments sur une période donnée. |
| `segments.details` | [`/segments/details`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_details/) | Demande de détails sur un segment spécifique. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Achats %}

| Autorisation | Endpoint | Description |
|---|---|---|
| `purchases.product_list` | [`/purchases/product_list`]({{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id/) | Extraire la liste des produits achetés dans votre application. |
| `purchases.revenue_series` | [`/purchases/revenue_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_revenue_series/) | Extraire le montant total dépensé par jour dans votre application sur une période donnée. |
| `purchases.quantity_series` | [`/purchases/quantity_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_number_of_purchases/) | Extraire le nombre total d’achats effectués par jour dans votre application sur une période donnée. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Evénements %}

| Autorisation | Endpoint | Description |
|---|---|---|
| `events.list` | [`/events/list`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events/) | Extraire la liste des événements personnalisés. |
| `events.data_series` | [`/events/data_series`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_analytics/) | Extraire les occurrences d’un événement personnalisé sur une période donnée. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Sessions %}

| Autorisation | Endpoint | Description |
|---|---|---|
| `sessions.data_series` | [`/sessions/data_series`]({{site.baseurl}}/api/endpoints/export/sessions/get_sessions_analytics/) | Extraire les sessions par jour sur une période donnée. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab ICP %}

| Autorisation | Endpoint | Description |
|---|---|---|
| `kpi.dau.data_series` | [`/kpi/dau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_dau_date/) |  Extraire les utilisateurs actifs uniques par jour sur une période donnée. |
| `kpi.mau.data_series` | [`/kpi/mau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_mau_30_days/) | Extraire les utilisateurs actifs uniques sur une fenêtre de 30 jours glissants sur une période donnée. |
| `kpi.new_users.data_series` | [`/kpi/new_users/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_daily_new_users_date/) | Extraire les nouveaux utilisateurs par jour sur une période donnée. |
| `kpi.uninstalls.data_series` | [`/kpi/uninstalls/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_uninstalls_date/) | Extraire les désinstallations d’applications par jour sur une période donnée. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Modèles %}

| Autorisation | Endpoint | Description |
|---|---|---|
| `templates.email.create` | [`/templates/email/create`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template/) | Créer un nouveau modèle d’e-mail sur le tableau de bord. |
| `templates.email.info` | [`/templates/email/info`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_see_email_template_information/) | Extraire les données d’un modèle spécifique. |
| `templates.email.list` | [`/templates/email/list`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates/) | Extraire la liste des modèles d’e-mail. |
| `templates.email.update` | [`/templates/email/update`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_update_email_template/) | Mettre à jour un modèle d’e-mail stocké sur le tableau de bord. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab SSO %}

| Autorisation | Description |
|---|---|---|
| `sso.saml.login` | Configurer l'identifiant initié par le fournisseur d'identité. Pour plus d'informations, reportez-vous à l'[identification initiée par le fournisseur de services (PS)]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Blocs de contenu %}

| Autorisation | Endpoint | Description |
|---|---|---|
| `content_blocks.info` | [`/content_blocks/info`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information/) | Extraire les données d’un modèle spécifique. |
| `content_blocks.list` | [`/content_blocks/list`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks/) | Extraire la liste des blocs de contenu. |
| `content_blocks.create` | [`/content_blocks/create`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_create_email_content_block/) | Créer un nouveau bloc de contenu sur le tableau de bord. |
| `content_blocks.update` | [`/content_blocks_update`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block/) | Mettre à jour un bloc de contenu existant dans le tableau de bord. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Centre de préférences %}

| Autorisation | Endpoint | Description |
|---|---|---|
| `preference_center.get` | [`/preference_center/v1/{preferenceCenterExternalId}`]({{site.baseurl}}/api/endpoints/preference_center/get_view_details_preference_center) | Obtenir un centre de préférences. |
| `preference_center.list` | [`/preference_center/v1/list`]({{site.baseurl}}/api/endpoints/preference_center/get_list_preference_center/) | Répertorier les centres de préférences. |
| `preference_center.update` | [`/preference_center/v1`]({{site.baseurl}}/api/endpoints/preference_center/post_create_preference_center)<br><br>[`/preference_center/v1/{preferenceCenterExternalID}`]({{site.baseurl}}/api/endpoints/preference_center/put_update_preference_center/) | Créez ou mettez à jour un centre de préférences. |
| `preference_center.user.get` | [`/preference_center/v1/{preferenceCenterExternalId}/url/{userId}`]({{site.baseurl}}/api/endpoints/preference_center/get_create_url_preference_center) | Obtenir le lien d’un centre de préférence pour un utilisateur. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Abonnement %}

| Autorisation | Endpoint | Description |
|---|---|---|
| `subscription.status.set` | [`/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/) | Définir le statut du groupe d’abonnement. |
| `subscription.status.get` | [`/subscription/status/get`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/) | Obtenir le statut du groupe d’abonnement. |
| `subscription.groups.get` | [`/subscription/user/status`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups/) | Obtenir le statut des groupes d'abonnement auxquels des utilisateurs spécifiques sont explicitement abonnés et désabonnés. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab SMS %}

| Autorisation | Endpoint | Description |
|---|---|---|
| `sms.invalid_phone_numbers` | [`/sms/invalid_phone_numbers`]({{site.baseurl}}/api/endpoints/sms/get_query_invalid_numbers/) | Extraire les numéros de téléphone non valides. |
| `sms.invalid_phone_numbers.remove` | [`/sms/invalid_phone_numbers/remove`]({{site.baseurl}}/api/endpoints/sms/post_remove_invalid_numbers/) | Supprimer le drapeau de numéro de téléphone non valide d’utilisateurs. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Catalogues %}

| Autorisation | Endpoint | Description |
|---|---|---|
| `catalogs.add_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/post_create_catalog_items_bulk/) | Ajouter plusieurs produits à un catalogue existant. |
| `catalogs.update_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/patch_catalog_items_bulk/) | Mettre à jour plusieurs produits dans un catalogue existant. |
| `catalogs.delete_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/delete_catalog_items_bulk) | Supprimer plusieurs produits d’un catalogue existant. |
| `catalogs.get_item` | [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details/) | Obtenir un produit unique d’un catalogue existant. |
| `catalogs.update_item` | [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/put_update_catalog_item/) | Mettre à jour un produit unique dans un catalogue existant. |
| `catalogs.create_item` | [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/post_create_catalog_item/) | Créer un produit unique dans un catalogue existant. |
| `catalogs.delete_item` | [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/delete_catalog_item/) | Supprimer un produit unique d’un catalogue existant. |
| `catalogs.replace_item` | [` /catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/put_update_catalog_item/) | Remplacer un produit unique d’un catalogue existant. |
| `catalogs.create` | [`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/post_create_catalog/) | Créer un catalogue. |
| `catalogs.get` | [`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs/) | Obtenir une liste de catalogues |
| `catalogs.delete` | [`/catalogs/{catalog_name}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/delete_catalog/) | Supprimer un catalogue. |
| `catalogs.get_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk/) | Obtenir l’aperçu des produits d’un catalogue existant. |
| `catalogs.replace_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/put_update_catalog_items/) | Remplacer des articles dans un catalogue existant. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Authentification SDK %}

| Autorisation | Endpoint | Description |
|---|---|---|
| `sdk_authentication.create` | [`/app_group/sdk_authentication/create`]({{site.baseurl}}/api/endpoints/sdk_authentication/post_create_sdk_authentication_key) | Créez une nouvelle clé d'authentification SDK pour votre application. |
| `sdk_authentication.primary` | [`/app_group/sdk_authentication/primary`]({{site.baseurl}}/api/endpoints/sdk_authentication/put_primary_sdk_authentication_key/) | Marquez une clé d'authentification SDK comme clé principale pour votre application. |
| `sdk_authentication.delete` | [`/app_group/sdk_authentication/delete`]({{site.baseurl}}/api/endpoints/sdk_authentication/delete_sdk_authentication_key) | Supprimez une clé d'authentification SDK pour votre application. |
| `sdk_authentication.keys` | [`/app_group/sdk_authentication/keys`]({{site.baseurl}}/api/endpoints/sdk_authentication/get_sdk_authentication_keys) | Obtenez toutes les clés d'authentification du SDK pour votre application. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% endtabs %}

### Gestion des clés API REST

Vous pouvez afficher les détails des clés API REST existantes ou les supprimer à partir de **Paramètres** > **API et identifiants** > onglet **Clés API**. Notez que les clés API REST ne peuvent pas être modifiées après leur création.

L'onglet **Clés API** contient les informations suivantes pour chaque clé :

| Champ        | Description                                                                                                         |
| ------------ | :------------------------------------------------------------------------------------------------------------------ |
| Nom de clé API | Nom donné à la clé lors de sa création.                                                                            |
| Identifiant   | La clé API.                                                                                                        |
| Créé par   | L'adresse e-mail de l'utilisateur qui a créé la clé. Ce champ indiquera "N/A" pour les clés créées avant juin 2023. |
| Date de création | Date de création de cette clé.                                                                                      |
| Vu pour la dernière fois    | Date de la dernière utilisation de cette clé. Ce champ indiquera "N/A" pour les clés qui n'ont jamais été utilisées.                  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Pour afficher les détails d'une clé API, passez la souris sur la clé et sélectionnez <i class="fa-solid fa-eye" alt="View"></i> **View.** Cela comprend toutes les autorisations dont dispose cette clé, les adresses IP inscrites sur la liste blanche (le cas échéant) et si cette clé est inscrite sur la liste blanche des adresses IP de Braze.

![La liste des autorisations des clés API dans le tableau de bord de Braze.]({% image_buster /assets/img_archive/view-api-key.png %})

Notez que lors de la [suppression d'un utilisateur]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/adding_users_to_your_dashboard/), les clés API associées qu'il a créées ne seront pas supprimées. Pour supprimer une clé, survolez-la et sélectionnez <i class="fa-solid fa-trash-can" alt="Delete"></i> **Supprimer**.

![Une clé API nommée "Last Seen" avec l'icône de la corbeille en surbrillance, indiquant "Delete".]({% image_buster /assets/img_archive/api-key-options.png %}){: style="max-width:30%;"}

### Sécurité clé API REST

Les clés API servent à authentifier les appels de l’API. Quand vous créez une nouvelle clé API REST, vous devez lui accorder l’accès à des endpoints spécifiques. En affectant des autorisations spécifiques à une clé API, vous pouvez limiter de façon précise les appels qu’une clé API peut authentifier.

Étant donné que les clés API REST permettent d’accéder à des endpoints API REST potentiellement sensibles, sécurisez ces clés et partagez-les uniquement avec des partenaires de confiance. Elles ne doivent jamais être exposées publiquement. Par exemple, n’utilisez pas cette clé pour faire des appels AJAX depuis votre site Web ou pour l’exposer autrement de façon publique.

Une bonne pratique de sécurité est d’accorder à un utilisateur uniquement les accès nécessaires pour qu’il puisse accomplir son travail ; ce principe peut également être appliqué aux Clés API en affectant des autorisations pour chaque clé. Ces autorisations vous offrent une meilleure sécurité et un meilleur contrôle sur les différentes parties de votre compte.

{% alert warning %}
Étant donné que les clés d'API REST permettent d'accéder à des endpoints d'API REST potentiellement sensibles, assurez-vous qu'elles sont stockées et utilisées en toute sécurité. Par exemple, n’utilisez pas cette clé pour faire des appels AJAX depuis votre site Web ou pour l’exposer autrement de façon publique.
{% endalert %}

En cas d’exposition accidentelle d’une clé, elle pourra être supprimée à partir de la console de développement. Pour obtenir de l'aide sur ce processus, ouvrez un [ticket d'assistance.]({{site.baseurl}}/braze_support/)

### Liste d’adresses IP autorisées

Pour renforcer la sécurité, vous pouvez établir une liste des adresses IP et sous-réseaux qui sont exclusivement autorisés à envoyer des requêtes à l’API REST pour une clé API REST donnée. Vous définissez pour cela une liste d’autorisations, également appelée « Liste blanche ». Pour autoriser des adresses IP ou des sous-réseaux spécifiques, indiquez-les dans la section **Liste blanche d’adresses IP (Whitelist IPs) **lors de la création d’une nouvelle clé API REST :

![Option permettant d'autoriser une liste d'adresses IP lors de la création d'une clé API.]({% image_buster /assets/img_archive/api-key-ip-whitelisting.png %})

Si vous n’en spécifiez aucune, les requêtes pourront être envoyées depuis n’importe quelle adresse IP.

{% alert tip %}
Vous créez un Webhook Braze à Braze en utilisant une liste blanche ? Consultez notre liste d'[adresses IP à mettre sur liste blanche.]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#ip-whitelisting)
{% endalert %}

## Ressources complémentaires

### Bibliothèque client Ruby

Si vous utilisez Ruby pour implémenter Braze, vous pouvez utiliser notre [Bibliothèque Client Ruby](https://github.com/braze-inc/braze-api-client-ruby) pour réduire le temps d’importation des données. Une bibliothèque cliente est une collection de code spécifique à un langage de programmation (dans ce cas, Ruby) qui facilite l’utilisation d’une API.

La bibliothèque client Ruby prend en charge les [endpoints utilisateur]({{site.baseurl}}/api/endpoints/user_data).

{% alert important %}
Cette bibliothèque cliente est actuellement en version bêta. Voulez-vous nous aider à améliorer cette bibliothèque ? Envoyez-nous vos commentaires à [smb-product@braze.com](mailto:smb-product@braze.com).
{% endalert %}

