## Migration des autorisations granulaires

{% alert important %}
Les autorisations granulaires sont actuellement en accès anticipé. Lorsque la migration est planifiée pour votre entreprise, vos administrateurs Braze recevront des e-mails et des bannières sur le tableau de bord les informant de la [migration des autorisations granulaires]({{site.baseurl}}/granular_permissions_migration/).
{% endalert %}

Les intégrations SCIM existantes et [les objets API SCIM hérités]({{site.baseurl}}/scim_api_appendix/?sdktab=legacy%20scim%20api) continueront de fonctionner après la migration des autorisations granulaires prévue fin avril. 

Il n'est pas nécessaire que vous preniez des mesures immédiates. Cependant, nous vous recommandons de vérifier vos intégrations afin d'identifier les autorisations qui seront granularisées. Par exemple, si vous envoyez actuellement`basic_access`  dans l'API, nous vous recommandons de mettre à jour votre intégration après la granularisation afin d'inclure les autorisations spécifiques (par exemple, `"appGroupPermissions":["view_campaigns","edit_campaigns"]`). Braze continuera d'accepter les chaînes de caractères héritées, telles que `basic_access`, après la migration des autorisations granulaires afin que les intégrations existantes ne soient pas interrompues.

## Objet Autorisations

L'objet "Permissions" est un champ que l'on retrouve dans certaines demandes et réponses lors de l'interface avec la ressource utilisateur par le biais des permissions de l'ID SCIM.

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

Un objet Autorisations valide est un objet JSON avec les paires clé-valeur suivantes :

| Clé | Requis | Type de données | Description |
| --- | --- | --- | --- |
| `companyPermissions` | Facultatif | Tableau | Tableau de [chaînes de caractères de permissions au niveau de l'entreprise]({{site.baseurl}}/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_company), dans lequel la présence de la chaîne de caractères indique que l'utilisateur dispose de la permission correspondante. |
| `roles` | Facultatif | Tableau | Tableau d'[objets de rôle]({{site.baseurl}}/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_role-object). |
| `appGroup` | Requis | Tableau | Tableau d'[objets d'autorisation de l'espace de travail]({{site.baseurl}}/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_workspace-permissions-object). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

### Objet d'autorisations de l'espace de travail

Un objet Autorisations de groupe d'applications valide est un objet JSON avec les paires clé-valeur suivantes :

| Clé | Requis | Type de données | Description |
| --- | --- | --- | --- |
| `appGroupName`| Facultatif | Chaîne de caractères | Nom de l'espace de travail. Utilisé pour spécifier l'espace de travail pour lequel les permissions contenues dans cet objet sont utilisées. | 
| `appGroupId` | Requis si l’`appGroupName` est absent | Chaîne de caractères | ID de l'espace de travail, servant de méthode alternative pour spécifier l'espace de travail. |
| `appGroupPermissionSets` | Facultatif | Tableau | Tableau contenant un seul [objet Ensemble d’autorisations de l’espace de travail]({{site.baseurl}}/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_workspace-permissions-set-object). |
| `appGroupPermissions` | Requis | Tableau | Tableau de chaînes de caractères d’autorisation au niveau de l’espace de travail dans le tableau [Chaînes de caractères des autorisations de l’espace de travail]({{site.baseurl}}/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_workspace-strings), dans lequel la présence de la chaîne de caractères correspond à l’utilisateur disposant de l’autorisation correspondante pour l’espace de travail donné. |
| `team` | Facultatif | Tableau | Tableau d'[objets de permission de Teams]({{site.baseurl}}/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_team-permissions-object). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

### Objet Ensemble d’autorisations de l'espace de travail {#workspace-permissions-set-object}

Un objet Autorisations de l’espace de travail valide est un objet JSON avec les paires clé-valeur suivantes :

| Clé | Requis | Type de données | Description |
| --- | --- | --- | --- |
| `appGroupPermissionSetName` | Facultatif | Chaîne de caractères | Nom de l'ensemble de permissions de l'espace de travail attribué à l'utilisateur pour cet espace de travail. |
| `appGroupPermissionSetID` | Requis si l’`appGroupPermissionSetName` est absent | Chaîne de caractères | ID de l'espace de travail, servant de méthode alternative pour spécifier le jeu de permissions de l'espace de travail attribué à l'utilisateur pour cet espace de travail. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

### Objet Autorisations de l’équipe

Un objet de permission d'équipe valide est un objet JSON avec les paires clé-valeur suivantes :

| Clé | Requis | Type de données | Description |
| --- | --- | --- | --- |
| `teamName` | Facultatif | Chaîne de caractères | Nom de l'équipe, qui peut être utilisé pour spécifier à quelle équipe sont destinées les autorisations de cet objet. |
| `teamId` | Requis si l’`teamName` est absent | Chaîne de caractères | ID de l’équipe, servant de méthode alternative pour spécifier l’équipe. |
| `teamPermissions` | Requis | Tableau | Tableau de chaînes de caractères d’autorisations au niveau de l'équipe provenant du tableau des [chaînes de caractères d’autorisations des équipes]({{site.baseurl}}/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_team), dans lequel la présence de la chaîne correspond à l'utilisateur disposant de l’autorisation correspondante pour l'équipe spécifiée. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Objet de rôle

Un objet de rôle valide est un objet JSON avec les paires clé-valeur suivantes :

| Clé | Requis | Type de données | Description |
| --- | --- | --- | --- |
| `roleName` | Facultatif | Chaîne de caractères | Nom du rôle attribué à l'utilisateur. |
| `roleId` | Requis si l’`roleName` est absent | Chaîne de caractères | ID du rôle, servant de méthode alternative pour spécifier le rôle. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Annexes

### Chaînes de caractères d'autorisation de l'entreprise {#company}

| Telles qu’affichées dans l’interface utilisateur | Chaîne de caractères API SCIM |
| --- | --- |
| Administrateur | `admin` |
| Gérer les paramètres de l'entreprise | `manage_company_settings` |
| Créer et supprimer des espaces de travail| `add_remove_app_groups` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Chaînes de caractères des autorisations de l'espace de travail {#workspace-strings}

| Nom de l’autorisation | Chaîne de caractères API SCIM |
| --- | --- |
| Afficher les campagnes | `view_campaigns` |
| Modifier les campagnes | `edit_campaigns` |
| Archiver les campagnes | `archive_campaigns` |
| Afficher les canvas | `view_canvases` |
| Modifier les canvas | `edit_canvases` |
| Archiver les canvas | `archive_canvases` |
| Afficher les règles de limite de fréquence | `view_frequency_caps` |
| Modifier les règles de limitation de fréquence | `edit_frequency_caps` |
| Afficher l'ordre de priorité des messages | `view_message_prioritization` |
| Modifier l'ordre de priorité des messages | `edit_message_prioritization` |
| Afficher les blocs de contenu | `view_content_blocks` |
| Modifier les blocs de contenu | `edit_content_blocks` |
| Archiver les blocs de contenu | `archive_content_blocks` |
| Voir les indicateurs de fonctionnalité | `view_feature_flags` |
| Modifier l’indicateur de fonctionnalité | `edit_feature_flags` |
| Indicateurs de fonctionnalité d'archivage | `archive_feature_flags` |
| Afficher le segment | `view_segments` |
| Modifier les segments | `edit_segments` |
| Segments d'archives | `archive_segments` |
| Voir le groupe de contrôle global | `view_global_control_group` |
| Modifier le groupe de contrôle global | `edit_global_control_group` |
| Afficher les modèles IAM | `view_iam_templates` |
| Modifier les modèles IAM | `edit_iam_templates` |
| Archiver les modèles IAM | `archive_iam_templates` |
| Afficher les modèles d'e-mail | `view_email_templates` |
| Modifier les modèles d’e-mail | `edit_email_templates` |
| Archiver les modèles d'e-mail | `archive_email_templates` |
| Afficher les modèles de webhook | `view_webhook_templates` |
| Modifier les modèles de webhook | `edit_webhook_templates` |
| Archiver les modèles de webhook | `archive_webhook_templates` |
| Afficher les modèles de lien | `view_link_templates` |
| Modifier les modèles de lien | `edit_link_templates` |
| Voir les ressources de la bibliothèque multimédia | `view_media_library_assets` |
| Afficher les emplacements | `view_locations` |
| Modifier les emplacements | `edit_locations` |
| Emplacement des archives | `archive_locations` |
| Consulter les codes de promotion | `view_promotion_codes` |
| Modifier les codes de promotion | `edit_promotion_codes` |
| Codes de promotion des exportations | `export_promotion_codes` |
| Afficher les centres de préférences | `view_preference_centers` |
| Modifier les centres de préférences | `edit_preference_centers` |
| Modifier les rapports | `edit_reports` |
| Afficher les placements | `view_placements` |
| Modifier les emplacements | `edit_placements` |
| Archiver les placements | `archive_placements` |
| Afficher les modèles de bannières | `view_banner_templates` |
| Afficher les paramètres multilingues | `view_multi_language_settings` |
| Utiliser l'opérateur | `use_operator` |
| Afficher les agents de Decisioning Studio | `view_decisioning_studio_agents` |
| Voir l'audience de BrazeAI Decisioning Studio™ |`view_decisioning_studio_audience` |
| Afficher l'événement de conversion dans Decisioning Studio | `view_decisioning_studio_conversion_event` |
| Voir les mécanismes de contrôle de Decisioning Studio | `view_decisioning_studio_guardrails` |
| Lancez des campagnes | `launch_campaigns` |
| Lancer des canvas | `launch_canvases` |
| Modifier les utilisateurs du tableau de bord | `edit_dashboard_users` |
| Modifier les ressources de la bibliothèque multimédia | `edit_media_library_assets` |
| Supprimer des ressources de la bibliothèque multimédia | `delete_media_library_assets` |
| Voir les importations d'utilisateurs | `view_import_users` |
| Importer des utilisateurs	| `import_users` |
| Modifier les données d'utilisateur | `edit_user_data` |
| Voir les enregistrements de fusion d'utilisateurs | `view_user_merge_records` |
| Fusionner les utilisateurs dupliqués | `merge_duplicate_users` |
| Voir les clés API | `view_api_keys` |
| Modifier les clés API | `edit_api_keys` |
| Afficher les groupes internes | `view_internal_user_groups` |
| Modifier les groupes internes | `edit_internal_user_groups` |
| Supprimer les groupes internes | `delete_internal_user_groups` |
| Afficher le journal d'activité des messages | `view_message_activity_log` |
| Journal des événements utilisateurs | `view_event_user_log` |
| Voir les identifiants de l'API | `view_api_identifiers` |
| Voir le tableau de bord d'utilisation de l'API | `view_api_usage_dashboard` |
| Voir les limites de l'API | `view_api_limits` |
| Voir les alertes d'utilisation de l'API | `view_api_usage_alerts` |
| Modifier les alertes d'utilisation de l'API | `edit_api_usage_alerts` |
| Afficher le débogueur SDK | `view_sdk_debugger` |
| Modifier le débogueur SDK | `edit_sdk_debugger` |
| Lancer des blocs de contenu | `launch_content_blocks` |
| Modifier l'ingestion de données cloud | `edit_cloud_data_ingestion` |
| Afficher les paramètres de l'application | `view_app_settings` |
| Modifier les paramètres de l'application | `edit_app_settings` |
| Afficher les paramètres des notifications push | `view_push_settings` |
| Modifier les paramètres des notifications push | `edit_push_settings` |
| Voir les équipes | `view_teams` |
| Modifier les équipes | `edit_teams` |
| Archiver les équipes | `archive_teams` |
| Afficher les attributs personnalisés | `view_custom_attributes` |
| Modifier des attributs personnalisés | `edit_custom_attributes` |
| Ajouter des attributs personnalisés à la liste de blocage | `blocklist_custom_attributes` |
| Supprimer des attributs personnalisés | `delete_custom_attributes` |
| Exporter des attributs personnalisés | `export_custom_attributes` |
| Afficher les événements personnalisés	 | `view_custom_events` |
| Modifier des événements personnalisés | `edit_custom_events` |
| Ajouter des événements personnalisés à la liste de blocage | `blocklist_custom_events` |
| Supprimer des événements personnalisés | `delete_custom_events` |
| Exportation d'événements personnalisés | `export_custom_events` |
| Modifier la segmentation des propriétés d'événements personnalisés | `edit_custom_event_property_segmentation` |
| Afficher les produits | `view_products` |
| Modifier des produits	 | `edit_products` |
| Ajouter des produits à la liste de blocage | `blocklist_products` |
| Modifier la segmentation des propriétés d'achat | `edit_purchase_property_segmentation` |
| Afficher les balises | `view_tags` |
| Modifier les balises | `edit_tags` |
| Supprimer les balises | `delete_tags` |
| Afficher les paramètres d'e-mail	| `view_email_settings` |
| Modifier les paramètres d'e-mail | `edit_email_settings` |
| Afficher les catalogues | `view_catalogs` |
| Modifier les catalogues	 | `edit_catalogs` |
| Exporter des catalogues | `export_catalogs` |
| Supprimer les catalogues | `delete_catalogs` |
| Consulter les paramètres de WhatsApp | `view_whatsapp_settings` |
| Modifier les partenaires technologiques | `edit_technology_partners` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Chaînes de caractères de permission d'équipe {#team}

| Nom de l’autorisation | Chaîne de caractères API SCIM |
| --- | --- |
| Afficher les campagnes | `view_campaigns` |
| Modifier les campagnes | `edit_campaigns` |
| Archiver les campagnes | `archive_campaigns` |
| Afficher les canvas | `view_canvases` |
| Modifier les canvas | `edit_canvases` |
| Archiver les canvas | `archive_canvases` |
| Afficher les règles de limite de fréquence | `view_frequency_caps` |
| Modifier les règles de limitation de fréquence | `edit_frequency_caps` |
| Afficher l'ordre de priorité des messages | `view_message_prioritization` |
| Modifier l'ordre de priorité des messages | `edit_message_prioritization` |
| Afficher les blocs de contenu | `view_content_blocks` |
| Voir les indicateurs de fonctionnalité | `view_feature_flags` |
| Modifier l’indicateur de fonctionnalité | `edit_feature_flags` |
| Indicateurs de fonctionnalité d'archivage | `archive_feature_flags` |
| Afficher le segment | `view_segments` |
| Modifier les segments | `edit_segments` |
| Modifier le groupe de contrôle global | `edit_global_control_group` |
| Afficher les modèles IAM | `view_iam_templates` |
| Modifier les modèles IAM | `edit_iam_templates` |
| Archiver les modèles IAM | `archive_iam_templates` |
| Afficher les modèles d'e-mail | `view_email_templates` |
| Modifier les modèles d’e-mail | `edit_email_templates` |
| Archiver les modèles d'e-mail | `archive_email_templates` |
| Afficher les modèles de webhook | `view_webhook_templates` |
| Modifier les modèles de webhook | `edit_webhook_templates` |
| Archiver les modèles de webhook | `archive_webhook_templates` |
| Afficher les modèles de lien | `view_link_templates` |
| Modifier les modèles de lien | `edit_link_templates` |
| Voir les ressources de la bibliothèque multimédia | `view_media_library_assets` |
| Afficher les emplacements | `view_locations` |
| Modifier les emplacements | `edit_locations` |
| Emplacement des archives | `archive_locations` |
| Consulter les codes de promotion | `view_promotion_codes` |
| Modifier les codes de promotion | `edit_promotion_codes` |
| Codes de promotion des exportations | `export_promotion_codes` |
| Afficher les centres de préférences | `view_preference_centers` |
| Modifier les centres de préférences | `edit_preference_centers` |
| Consulter les rapports | `view_reports` |
| Créer des rapports | `create_reports` |
| Modifier les rapports | `edit_reports` |
| Afficher les modèles de bannières | `view_banner_templates` |
| Afficher les paramètres multilingues | `view_multi_language_settings` |
| Utiliser l'opérateur | `use_operator` |
| Afficher les agents de Decisioning Studio | `view_decisioning_studio_agents` |
| Afficher l'événement de conversion dans Decisioning Studio | `view_decisioning_studio_conversion_event` |
| Lancez des campagnes | `launch_campaigns` |
| Lancer des canvas | `launch_canvases` |
| Modifier les utilisateurs du tableau de bord | `edit_dashboard_users` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Chaînes de caractères du service

| Telles qu’affichées dans l’interface utilisateur | Chaîne de caractères API SCIM |
| --- | --- |
| Agence/tiers | `agency` |
| BI/analyses | `bi` |
| Cadre supérieur | `c_suite` |
| Ingénierie | `engineering` |
| Finance | `finance` |
| Marketing/éditorial | `marketing` |
| Gestion des produits | `pm` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }