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

L’objet Autorisations est un champ trouvé dans certaines des requêtes et réponses lors de l’interfaçage avec la ressource utilisateur via les autorisations d’ID SCIM.

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
| `companyPermissions` | Requis | Tableau | Tableau de chaînes de caractères d’autorisation au niveau de l’entreprise dans le tableau [Company permission strings (chaînes de caractères d’autorisation de l’entreprise)](#company), dans lequel la présence de la chaîne de caractères correspond à l’utilisateur disposant de l’autorisation correspondante. |
| `appGroup` | Requis | Tableau | Tableau d’[objets Autorisation du groupe d’apps](#app-group-permssions-object). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

### Objet Autorisations du groupe d’apps

Un objet Autorisations du groupe d'apps valide est un objet JSON avec les paires clé-valeur suivantes :

| Clé | Requis | Type de données | Description |
| --- | --- | --- | --- |
| `appGroupName`| Facultatif | String | Nom du groupe d’apps. Utilisé pour spécifier le groupe d’apps auquel les autorisations contenues dans cet objet sont destinées. | 
| `appGroupId` | Requis si l’`appGroupName` est absent | String | ID du groupe d’apps, servant de méthode alternative pour spécifier le groupe d’apps. |
| `appGroupPermissions` | Requis | Tableau | Tableau de chaînes de caractères d’autorisation au niveau du groupe d'apps dans le tableau [App group permission strings (chaînes de caractères d’autorisation du groupe d'apps)](#app-group), dans lequel la présence de la chaîne de caractères correspond à l’utilisateur disposant de l’autorisation correspondante pour le groupe d'apps donné. |
| `team` | Facultatif | Tableau | Tableau d’[objets Autorisation de l’équipe](#team-permissions-object). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

### Objet Autorisations de l’équipe

Un objet Autorisation de l’équipe valide est un objet JSON avec les paires clé-valeur suivantes :

| Clé | Requis | Type de données | Description |
| --- | --- | --- | --- |
| `teamName` | Facultatif | String | Nom de l’équipe. Utilisé pour spécifier l’équipe à laquelle les autorisations contenues dans cet objet sont destinées. |
| `teamId` | Requis si l’`teamName` est absent | String | ID de l’équipe, servant de méthode alternative pour spécifier l’équipe. |
| `teamPermissions` | Requis | Tableau | Tableau de chaînes de caractères d’autorisation au niveau de l’équipe dans le tableau [team permission strings (chaînes de caractères d’autorisation de l’équipe)](#team), dans lequel la présence de la chaîne de caractères correspond à l’utilisateur disposant de l’autorisation correspondante pour l’équipe donnée. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Annexes

### Chaînes de caractères d’autorisation de l’entreprise

| Telles qu’affichées dans l’interface utilisateur | Chaîne de caractères API SCIM |
| --- | --- |
| Administrateur | `admin` |
| Peut gérer les paramètres de l’entreprise | `manage_company_settings` |
| Peut ajouter/supprimer des groupes d’apps| `add_remove_app_groups` |
{: .reset-td-br-1 .reset-td-br-2}

### Chaînes de caractères d’autorisation de groupe d’apps

| Nom de l’autorisation | Chaîne de caractères API SCIM |
| --- | --- |
| Admin | `admin` |
| Campagnes d’accès, Canvas, cartes, segments, bibliothèque multimédia | `basic_access` |
| Envoyer des campagnes, des Canvas | `send_campaigns_canvases` |
| Publier des cartes | `publish_cards` |
| Modifier les segments | `edit_segments` |
| Exporter les données utilisateur | `export_user_data` |
| Afficher les Informations personnellement identifiables | `view_pii` |
| Voir les profils utilisateurs respectueux des informations personnellement identifiables | `view_user_profile` |
| Gérer les utilisateurs du tableau de bord | `manage_dashboard_users` |
| Gérer la bibliothèque multimédia | `manage_media_library` |
| Afficher les données d’utilisation | `view_usage_data` |
| Importer et mettre à jour les données utilisateur | `import_update_user_data` |
| Afficher les détails de facturation | `view_billing_details` |
| Accéder à la Developer console | `dev_console` |
| Gérer les intégrations externes | `manage_external_integrations` |
| Gérer les applications | `manage_apps` |
| Gérer les équipes | `manage_teams` |
| Gérer les événements, attributs, achats | `manage_events_attributes_purchases` |
| Gérer les balises | `manage_tags` |
| Gérer les paramètres d’e-mail | `manage_email_settings` |
| Gérer les groupes d’abonnement | `manage_subscription_groups` |
| Gérer les paramètres d’approbation | `manage_approval_settings` |
{: .reset-td-br-1 .reset-td-br-2}

### Chaînes de caractères d’autorisation de l’équipe

| Nom de l’autorisation | Chaîne de caractères API SCIM |
| --- | --- |
| Admin | `admin` |
| Campagnes d’accès, Canvas, cartes, segments, bibliothèque multimédia | `basic_access` |
| Envoyer des campagnes, des Canvas | `send_campaigns_canvases` |
| Publier des cartes | `publish_cards` |
| Modifier les segments | `edit_segments` |
| Exporter les données utilisateur | `export_user_data` |
| Afficher le profil utilisateur | `view_user_profile` |
| Gérer les utilisateurs du tableau de bord | `manage_dashboard_users` |
| Gérer la bibliothèque multimédia | `manage_media_library` |
{: .reset-td-br-1 .reset-td-br-2}

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
{: .reset-td-br-1 .reset-td-br-2}
