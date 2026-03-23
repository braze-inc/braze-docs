## Migration des autorisations granulaires

{% alert important %}
Les autorisations granulaires sont actuellement en accès anticipé. Lorsque la migration est planifiée pour votre entreprise, vos administrateurs Braze recevront des e-mails et des bannières sur le tableau de bord les informant de la [migration des autorisations granulaires]({{site.baseurl}}/granular_permissions_migration/).
{% endalert %}

Les intégrations SCIM existantes et [les objets API SCIM hérités]({{site.baseurl}}/scim_api_appendix/?sdktab=legacy%20scim%20api) continueront de fonctionner après la migration des autorisations granulaires prévue fin avril. 

Aucune action immédiate n'est requise de votre part. Cependant, nous vous recommandons de vérifier vos intégrations afin d'identifier les autorisations qui seront granularisées. Par exemple, si vous envoyez actuellement `basic_access` dans l'API, nous vous suggérons de mettre à jour votre intégration après la granularisation afin d'inclure les autorisations spécifiques (par exemple, `"appGroupPermissions":["view_campaigns","edit_campaigns"]`). Braze continuera d'accepter les chaînes de caractères héritées, telles que `basic_access`, après la migration des autorisations granulaires, afin que les intégrations existantes ne soient pas interrompues.

## Objet Autorisations

L'objet Autorisations est un champ présent dans certaines demandes et réponses lors de l'interaction avec la ressource utilisateur via les autorisations d'ID SCIM.

{% alert note %}
Les groupes d'applications ont été renommés en espaces de travail dans Braze, mais les clés de cette page font toujours référence à l'ancienne terminologie (par exemple, `appGroup`, `appGroupName`).
{% endalert %}

```
{
  "permissions": {
    "companyPermissions": (required, array),
    "appGroup": (required, array)
  }
}
```

Un objet Autorisations valide est un objet JSON avec les paires clé-valeur suivantes :

| Clé | Requis | Type de données | Description |
| --- | --- | --- | --- |
| `companyPermissions` | Facultatif | Tableau | Tableau de [chaînes de caractères d'autorisations au niveau de la société]({{site.baseurl}}/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_company), dans lequel la présence de la chaîne de caractères indique que l'utilisateur dispose de l'autorisation correspondante. |
| `roles` | Facultatif | Tableau | Tableau d'[objets de rôle]({{site.baseurl}}/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_role-object). |
| `appGroup` | Requis | Tableau | Tableau d'[objets d'autorisations de l'espace de travail]({{site.baseurl}}/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_workspace-permissions-object). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

### Objet d'autorisations de l'espace de travail

Un objet d'autorisations de groupe d'applications valide est un objet JSON avec les paires clé-valeur suivantes :

| Clé | Requis | Type de données | Description |
| --- | --- | --- | --- |
| `appGroupName`| Facultatif | Chaîne de caractères | Nom de l'espace de travail. Permet de spécifier l'espace de travail auquel s'appliquent les autorisations contenues dans cet objet. | 
| `appGroupId` | Requis si `appGroupName` est absent | Chaîne de caractères | ID de l'espace de travail, servant de méthode alternative pour spécifier l'espace de travail. |
| `appGroupPermissionSets` | Facultatif | Tableau | Tableau contenant un seul [objet Ensemble d'autorisations de l'espace de travail]({{site.baseurl}}/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_workspace-permissions-set-object). |
| `appGroupPermissions` | Requis | Tableau | Tableau de chaînes de caractères d'autorisations au niveau de l'espace de travail, issu du tableau [Chaînes de caractères des autorisations de l'espace de travail]({{site.baseurl}}/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_workspace-strings), dans lequel la présence de la chaîne de caractères indique que l'utilisateur dispose de l'autorisation correspondante pour l'espace de travail spécifié. |
| `team` | Facultatif | Tableau | Tableau d'[objets d'autorisations d'équipe]({{site.baseurl}}/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_team-permissions-object). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

### Objet Ensemble d'autorisations de l'espace de travail {#workspace-permissions-set-object}

Un objet Ensemble d'autorisations de l'espace de travail valide est un objet JSON avec les paires clé-valeur suivantes :

| Clé | Requis | Type de données | Description |
| --- | --- | --- | --- |
| `appGroupPermissionSetName` | Facultatif | Chaîne de caractères | Nom de l'ensemble d'autorisations de l'espace de travail attribué à l'utilisateur pour cet espace de travail. |
| `appGroupPermissionSetID` | Requis si `appGroupPermissionSetName` est absent | Chaîne de caractères | ID de l'espace de travail, servant de méthode alternative pour spécifier l'ensemble d'autorisations de l'espace de travail attribué à l'utilisateur pour cet espace de travail. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

### Objet d'autorisations d'équipe

Un objet d'autorisations d'équipe valide est un objet JSON avec les paires clé-valeur suivantes :

| Clé | Requis | Type de données | Description |
| --- | --- | --- | --- |
| `teamName` | Facultatif | Chaîne de caractères | Nom de l'équipe, qui permet de spécifier à quelle équipe s'appliquent les autorisations de cet objet. |
| `teamId` | Requis si `teamName` est absent | Chaîne de caractères | ID de l'équipe, servant de méthode alternative pour spécifier l'équipe. |
| `teamPermissions` | Requis | Tableau | Tableau de chaînes de caractères d'autorisations au niveau de l'équipe, issu du tableau des [chaînes de caractères d'autorisations d'équipe]({{site.baseurl}}/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_team), dans lequel la présence de la chaîne de caractères indique que l'utilisateur dispose de l'autorisation correspondante pour l'équipe spécifiée. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Objet de rôle

Un objet de rôle valide est un objet JSON avec les paires clé-valeur suivantes :

| Clé | Requis | Type de données | Description |
| --- | --- | --- | --- |
| `roleName` | Facultatif | Chaîne de caractères | Nom du rôle attribué à l'utilisateur. |
| `roleId` | Requis si `roleName` est absent | Chaîne de caractères | ID du rôle, servant de méthode alternative pour spécifier le rôle. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Annexes

### Chaînes de caractères d'autorisations de la société {#company}

| Telles qu'affichées dans l'interface utilisateur | Chaîne de caractères API SCIM |
| --- | --- |
| Administrateur | `admin` |
| Gérer les paramètres de la société | `manage_company_settings` |
| Créer et supprimer des espaces de travail| `add_remove_app_groups` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Chaînes de caractères des autorisations de l'espace de travail {#workspace-strings}

| Nom de l'autorisation | Chaîne de caractères API SCIM |
| --- | --- |
| Afficher les campagnes | `view_campaigns` |
| Modifier les campagnes | `edit_campaigns` |
| Archiver les campagnes | `archive_campaigns` |
| Afficher les Canvas | `view_canvases` |
| Modifier les Canvas | `edit_canvases` |
| Archiver les Canvas | `archive_canvases` |
| Afficher les règles de limite de fréquence | `view_frequency_caps` |
| Modifier les règles de limite de fréquence | `edit_frequency_caps` |
| Afficher la priorisation des messages | `view_message_prioritization` |
| Modifier la priorisation des messages | `edit_message_prioritization` |
| Afficher les blocs de contenu | `view_content_blocks` |
| Modifier les blocs de contenu | `edit_content_blocks` |
| Archiver les blocs de contenu | `archive_content_blocks` |
| Afficher les indicateurs de fonctionnalité | `view_feature_flags` |
| Modifier les indicateurs de fonctionnalité | `edit_feature_flags` |
| Archiver les indicateurs de fonctionnalité | `archive_feature_flags` |
| Afficher les segments | `view_segments` |
| Modifier les segments | `edit_segments` |
| Archiver les segments | `archive_segments` |
| Afficher le groupe de contrôle global | `view_global_control_group` |
| Modifier le groupe de contrôle global | `edit_global_control_group` |
| Afficher les modèles IAM | `view_iam_templates` |
| Modifier les modèles IAM | `edit_iam_templates` |
| Archiver les modèles IAM | `archive_iam_templates` |
| Afficher les modèles d'e-mail | `view_email_templates` |
| Modifier les modèles d'e-mail | `edit_email_templates` |
| Archiver les modèles d'e-mail | `archive_email_templates` |
| Afficher les modèles de webhook | `view_webhook_templates` |
| Modifier les modèles de webhook | `edit_webhook_templates` |
| Archiver les modèles de webhook | `archive_webhook_templates` |
| Afficher les modèles de lien e-mail | `view_link_templates` |
| Modifier les modèles de lien e-mail | `edit_link_templates` |
| Afficher les ressources de la bibliothèque multimédia | `view_media_library_assets` |
| Afficher les emplacements | `view_locations` |
| Modifier les emplacements | `edit_locations` |
| Archiver les emplacements | `archive_locations` |
| Afficher les codes de promotion | `view_promotion_codes` |
| Modifier les codes de promotion | `edit_promotion_codes` |
| Exporter les codes de promotion | `export_promotion_codes` |
| Afficher les centres de préférences | `view_preference_centers` |
| Modifier les centres de préférences | `edit_preference_centers` |
| Modifier les rapports | `edit_reports` |
| Afficher les placements | `view_placements` |
| Modifier les placements | `edit_placements` |
| Archiver les placements | `archive_placements` |
| Afficher les modèles de bannières | `view_banner_templates` |
| Afficher les paramètres multilingues | `view_multi_language_settings` |
| Utiliser l'opérateur | `use_operator` |
| Afficher les agents de Decisioning Studio | `view_decisioning_studio_agents` |
| Afficher l'audience de Decisioning Studio |`view_decisioning_studio_audience` |
| Afficher l'événement de conversion de Decisioning Studio | `view_decisioning_studio_conversion_event` |
| Afficher les garde-fous de Decisioning Studio | `view_decisioning_studio_guardrails` |
| Lancer des campagnes | `launch_campaigns` |
| Lancer des Canvas | `launch_canvases` |
| Modifier les utilisateurs du tableau de bord | `edit_dashboard_users` |
| Modifier les ressources de la bibliothèque multimédia | `edit_media_library_assets` |
| Supprimer les ressources de la bibliothèque multimédia | `delete_media_library_assets` |
| Afficher les importations d'utilisateurs | `view_import_users` |
| Importer des utilisateurs	| `import_users` |
| Modifier les données utilisateur | `edit_user_data` |
| Afficher les enregistrements de fusion d'utilisateurs | `view_user_merge_records` |
| Fusionner les utilisateurs en double | `merge_duplicate_users` |
| Afficher les clés API | `view_api_keys` |
| Modifier les clés API | `edit_api_keys` |
| Afficher les groupes internes | `view_internal_user_groups` |
| Modifier les groupes internes | `edit_internal_user_groups` |
| Supprimer les groupes internes | `delete_internal_user_groups` |
| Afficher le journal d'activité des messages | `view_message_activity_log` |
| Afficher le journal des événements utilisateurs | `view_event_user_log` |
| Afficher les identifiants API | `view_api_identifiers` |
| Afficher le tableau de bord d'utilisation de l'API | `view_api_usage_dashboard` |
| Afficher les limites de l'API | `view_api_limits` |
| Afficher les alertes d'utilisation de l'API | `view_api_usage_alerts` |
| Modifier les alertes d'utilisation de l'API | `edit_api_usage_alerts` |
| Afficher le débogueur SDK | `view_sdk_debugger` |
| Modifier le débogueur SDK | `edit_sdk_debugger` |
| Lancer des blocs de contenu | `launch_content_blocks` |
| Modifier l'ingestion de données cloud | `edit_cloud_data_ingestion` |
| Afficher les paramètres de l'application | `view_app_settings` |
| Modifier les paramètres de l'application | `edit_app_settings` |
| Afficher les paramètres des notifications push | `view_push_settings` |
| Modifier les paramètres des notifications push | `edit_push_settings` |
| Afficher les équipes | `view_teams` |
| Modifier les équipes | `edit_teams` |
| Archiver les équipes | `archive_teams` |
| Afficher les attributs personnalisés | `view_custom_attributes` |
| Modifier les attributs personnalisés | `edit_custom_attributes` |
| Ajouter des attributs personnalisés à la liste de blocage | `blocklist_custom_attributes` |
| Supprimer des attributs personnalisés | `delete_custom_attributes` |
| Exporter des attributs personnalisés | `export_custom_attributes` |
| Afficher les événements personnalisés	 | `view_custom_events` |
| Modifier les événements personnalisés | `edit_custom_events` |
| Ajouter des événements personnalisés à la liste de blocage | `blocklist_custom_events` |
| Supprimer des événements personnalisés | `delete_custom_events` |
| Exporter des événements personnalisés | `export_custom_events` |
| Modifier la segmentation des propriétés d'événements personnalisés | `edit_custom_event_property_segmentation` |
| Afficher les produits | `view_products` |
| Modifier les produits	 | `edit_products` |
| Ajouter des produits à la liste de blocage | `blocklist_products` |
| Modifier la segmentation des propriétés d'achat | `edit_purchase_property_segmentation` |
| Afficher les étiquettes | `view_tags` |
| Modifier les étiquettes | `edit_tags` |
| Supprimer les étiquettes | `delete_tags` |
| Afficher les paramètres d'e-mail	| `view_email_settings` |
| Modifier les paramètres d'e-mail | `edit_email_settings` |
| Afficher les catalogues | `view_catalogs` |
| Modifier les catalogues	 | `edit_catalogs` |
| Exporter les catalogues | `export_catalogs` |
| Supprimer les catalogues | `delete_catalogs` |
| Afficher les paramètres WhatsApp | `view_whatsapp_settings` |
| Modifier les partenaires technologiques | `edit_technology_partners` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Chaînes de caractères d'autorisations d'équipe {#team}

| Nom de l'autorisation | Chaîne de caractères API SCIM |
| --- | --- |
| Afficher les campagnes | `view_campaigns` |
| Modifier les campagnes | `edit_campaigns` |
| Archiver les campagnes | `archive_campaigns` |
| Afficher les Canvas | `view_canvases` |
| Modifier les Canvas | `edit_canvases` |
| Archiver les Canvas | `archive_canvases` |
| Afficher les règles de limite de fréquence | `view_frequency_caps` |
| Modifier les règles de limite de fréquence | `edit_frequency_caps` |
| Afficher la priorisation des messages | `view_message_prioritization` |
| Modifier la priorisation des messages | `edit_message_prioritization` |
| Afficher les blocs de contenu | `view_content_blocks` |
| Afficher les indicateurs de fonctionnalité | `view_feature_flags` |
| Modifier les indicateurs de fonctionnalité | `edit_feature_flags` |
| Archiver les indicateurs de fonctionnalité | `archive_feature_flags` |
| Afficher les segments | `view_segments` |
| Modifier les segments | `edit_segments` |
| Modifier le groupe de contrôle global | `edit_global_control_group` |
| Afficher les modèles IAM | `view_iam_templates` |
| Modifier les modèles IAM | `edit_iam_templates` |
| Archiver les modèles IAM | `archive_iam_templates` |
| Afficher les modèles d'e-mail | `view_email_templates` |
| Modifier les modèles d'e-mail | `edit_email_templates` |
| Archiver les modèles d'e-mail | `archive_email_templates` |
| Afficher les modèles de webhook | `view_webhook_templates` |
| Modifier les modèles de webhook | `edit_webhook_templates` |
| Archiver les modèles de webhook | `archive_webhook_templates` |
| Afficher les modèles de lien e-mail | `view_link_templates` |
| Modifier les modèles de lien e-mail | `edit_link_templates` |
| Afficher les ressources de la bibliothèque multimédia | `view_media_library_assets` |
| Afficher les emplacements | `view_locations` |
| Modifier les emplacements | `edit_locations` |
| Archiver les emplacements | `archive_locations` |
| Afficher les codes de promotion | `view_promotion_codes` |
| Modifier les codes de promotion | `edit_promotion_codes` |
| Exporter les codes de promotion | `export_promotion_codes` |
| Afficher les centres de préférences | `view_preference_centers` |
| Modifier les centres de préférences | `edit_preference_centers` |
| Afficher les rapports | `view_reports` |
| Créer des rapports | `create_reports` |
| Modifier les rapports | `edit_reports` |
| Afficher les modèles de bannières | `view_banner_templates` |
| Afficher les paramètres multilingues | `view_multi_language_settings` |
| Utiliser l'opérateur | `use_operator` |
| Afficher les agents de Decisioning Studio | `view_decisioning_studio_agents` |
| Afficher l'événement de conversion de Decisioning Studio | `view_decisioning_studio_conversion_event` |
| Lancer des campagnes | `launch_campaigns` |
| Lancer des Canvas | `launch_canvases` |
| Modifier les utilisateurs du tableau de bord | `edit_dashboard_users` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Chaînes de caractères de département

| Telles qu'affichées dans l'interface utilisateur | Chaîne de caractères API SCIM |
| --- | --- |
| Agence/tiers | `agency` |
| BI/analytique | `bi` |
| Direction générale | `c_suite` |
| Ingénierie | `engineering` |
| Finance | `finance` |
| Marketing/éditorial | `marketing` |
| Gestion des produits | `pm` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }