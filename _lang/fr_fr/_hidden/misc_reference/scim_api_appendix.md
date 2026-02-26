---
nav_title: "Objets API SCIM et annexes"
article_title: Objets API SCIM et annexes
page_order: 8
page_type: reference
description: "Cet article explique les différents objets API SCIM et les annexes."
hidden: true
permalink: "/scim_api_appendix/"
---

# Objets API SCIM et annexes

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
| `companyPermissions` | Facultatif | Tableau | Tableau de chaînes de caractères d’autorisations au niveau de l'entreprise provenant du tableau des [chaînes de caractères d’autorisations de l'entreprise](#company), dans lequel la présence de la chaîne correspond à l'utilisateur disposant de l’autorisation correspondante. |
| `roles` | Facultatif | Tableau | Tableau d'[objets de rôle](#role-object). |
| `appGroup` | Requis | Tableau | Tableau d'[objets d'autorisation de l'espace de travail](#workspace-permission-object). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

### Objet de permissions de l'espace de travail {#workspace-permission-object}

Un objet Autorisations de groupe d'applications valide est un objet JSON avec les paires clé-valeur suivantes :

| Clé | Requis | Type de données | Description |
| --- | --- | --- | --- |
| `appGroupName`| Facultatif | Chaîne de caractères | Nom de l'espace de travail. Utilisé pour spécifier l'espace de travail pour lequel les permissions contenues dans cet objet sont utilisées. | 
| `appGroupId` | Requis si l’`appGroupName` est absent | Chaîne de caractères | ID de l'espace de travail, servant de méthode alternative pour spécifier l'espace de travail. |
| `appGroupPermissionSets` | Facultatif | Tableau | Tableau contenant un seul [objet Ensemble d’autorisations de l’espace de travail](#workspace-permissions-set-object). |
| `appGroupPermissions` | Requis | Tableau | Tableau de chaînes de caractères d’autorisation au niveau de l’espace de travail dans le tableau [Chaînes de caractères des autorisations de l’espace de travail](#workspace-strings), dans lequel la présence de la chaîne de caractères correspond à l’utilisateur disposant de l’autorisation correspondante pour l’espace de travail donné. |
| `team` | Facultatif | Tableau | Tableau d'[objets de permission de Teams](#team-permissions-object). |
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
| `teamPermissions` | Requis | Tableau | Tableau de chaînes de caractères d’autorisations au niveau de l'équipe provenant du tableau des [chaînes de caractères d’autorisations des équipes](#team), dans lequel la présence de la chaîne correspond à l'utilisateur disposant de l’autorisation correspondante pour l'équipe spécifiée. |
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
| Peut gérer les paramètres de l’entreprise | `manage_company_settings` |
| Peut ajouter/supprimer des espaces de travail| `add_remove_app_groups` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Chaînes de caractères des autorisations de l'espace de travail {#workspace-strings}

| Nom de l’autorisation | Chaîne de caractères API SCIM |
| --- | --- |
| Admin | `admin` |
| Campagnes d’accès, Canvas, cartes, segments, bibliothèque multimédia | `basic_access` |
| Approuver et supprimer des canvas | `approve_deny_campaigns` |
| Envoyer des campagnes, des canvas | `send_campaigns_canvases` |
| Publier des cartes | `publish_cards` |
| Modifier les segments | `edit_segments` |
| Exporter les données utilisateur | `export_user_data` |
| Afficher les données d'identification | `view_pii` |
| Voir les profils utilisateur respectueux des données d'identification | `view_user_profile` |
| Gérer les utilisateurs du tableau de bord | `manage_dashboard_users` |
| Gérer les ressources de la bibliothèque multimédia | `manage_media_library` |
| Afficher les données d’utilisation | `view_usage_data` |
| Importer et mettre à jour les données utilisateur | `import_update_user_data` |
| Afficher les détails de facturation | `view_billing_details` |
| Accéder à la Console de développement | `dev_console` |
| Lancer des blocs de contenu | `launch_content_blocks` |
| Gérer les intégrations externes | `manage_external_integrations` |
| Gérer les applications | `manage_apps` |
| Gérer les équipes | `manage_teams` |
| Gérer les événements, attributs, achats | `manage_events_attributes_purchases` |
| Gérer les étiquettes | `manage_tags` |
| Gérer les paramètres des e-mails | `manage_email_settings` |
| Gérer les groupes d’abonnement | `manage_subscription_groups` |
| Gérer les paramètres d’approbation | `manage_approval_settings` |
| Gérer les autorisations sur le tableau de bord des catalogues | `manage_catalogs_dashboard_permission` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Chaînes de caractères de permission d'équipe {#team}

| Nom de l’autorisation | Chaîne de caractères API SCIM |
| --- | --- |
| Admin | `admin` |
| Campagnes d’accès, Canvas, cartes, segments, bibliothèque multimédia | `basic_access` |
| Approuver et supprimer des canvas | `approve_deny_campaigns` |
| Envoyer des campagnes, des canvas | `send_campaigns_canvases` |
| Publier des cartes | `publish_cards` |
| Modifier les segments | `edit_segments` |
| Exporter les données utilisateur | `export_user_data` |
| Afficher le profil utilisateur | `view_user_profile` |
| Gérer les utilisateurs du tableau de bord | `manage_dashboard_users` |
| Gérer les ressources de la bibliothèque multimédia | `manage_media_library` |
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
